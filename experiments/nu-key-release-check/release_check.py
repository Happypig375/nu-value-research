"""Key-release check, counted in game updates (docs/nu-key-release-check-2026-11-02.md).

Follow-up to the keyboard input check. It sends real X input (XTEST) to the unchanged
standalone MMCC Breakout game and judges only from screenshots of its window. Time is
counted in distinct rendered frames: Nu renders once per update and the rotating cube
changes every update, so each new distinct frame is one game update. The run checks
that assumption itself: while a key is held, the paddle must move 4 units per new frame.

New work, separate from the stopped R02 input gate; it uses none of that draft.
Helpers (X input, capture, paddle and gameplay rules) are imported unchanged from
experiments/nu-keyboard-input-check/input_check.py (as of commit 4be9c8f).

Usage: release_check.py GAME_DLL_DIR OUTPUT_DIR [--deadline 900]
"""
import argparse
import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "nu-keyboard-input-check"))
import input_check as ic  # noqa: E402

CONTROL_FRAMES = 10      # distinct frames with no input before any key
RELEASE_FRAMES = 30      # distinct frames observed after each key-up
LAG_LIMIT = 5            # movement allowed on at most this many frames after key-up
STILL_DELTA = 2          # virtual units: a frame "moved" if the centre changed by more
STEP, STEP_TOL = 4, 1    # expected paddle step per update while a key is held
STEP_SHARE = 0.8         # share of held moving frames that must show a 4 +/- 1 step
FRAME_TIMEOUT = 20       # seconds to wait for one new distinct frame


def title_visible(s):
    # Play, Credits and Exit buttons are green on the Title (0, 97, 2 in earlier captures).
    pts = [s.px(-50, 0), s.px(-50, -48), s.px(-50, -96)]
    return all(g >= 64 and r <= 32 and b <= 32 for r, g, b in pts)


def main():
    children = []
    try:
        return run(children)
    finally:
        for game in children:
            if game.poll() is None:
                os.killpg(game.pid, signal.SIGKILL)


def run(children):
    ap = argparse.ArgumentParser()
    ap.add_argument("game_dir", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--deadline", type=float, default=900)
    a = ap.parse_args()
    game_dir, out = a.game_dir.resolve(strict=True), a.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    trace = (out / "trace.jsonl").open("w")
    frames_log = (out / "frames.jsonl").open("w")
    t0 = time.monotonic()
    shots = {}
    result = {"verdict": None, "invalid": None, "windows": {}, "secondary": {}}

    def emit(event, **data):
        trace.write(json.dumps({"event": event, "t": round(time.monotonic() - t0, 3), **data}) + "\n")
        trace.flush()

    game = subprocess.Popen(["dotnet", str(game_dir / "Breakout Mmcc.dll")], cwd=game_dir,
                            stdout=(out / "game-stdout.log").open("wb"), stderr=(out / "game-stderr.log").open("wb"),
                            start_new_session=True)
    children.append(game)
    emit("launched", pid=game.pid)
    x = ic.X()

    def alive():
        return game.poll() is None and time.monotonic() - t0 < a.deadline

    def finish(code):
        if game.poll() is None:
            os.killpg(game.pid, signal.SIGTERM)
            try:
                game.wait(15)
            except subprocess.TimeoutExpired:
                os.killpg(game.pid, signal.SIGKILL)
                game.wait(15)
            emit("game-terminated-by-harness", exit_code=game.returncode)
        result["game_exit_code"] = game.returncode
        result["elapsed_seconds"] = round(time.monotonic() - t0, 1)
        for label, s in shots.items():
            s.png(out / f"{label}.png")
        (out / "result.json").write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps(result, indent=2))
        return code

    def invalid(reason):
        result["invalid"] = reason
        emit("invalid", reason=reason)
        return finish(2)

    window = None
    while window is None and alive() and time.monotonic() - t0 < 120:
        window = x.find()
        if window is None:
            time.sleep(0.5)
    if window is None:
        return invalid("game window not found")
    time.sleep(1.0)
    rect = x.geometry(window)
    emit("window", id=window, rect=rect)
    if tuple(rect[2:]) != ic.EXPECTED_SIZE:
        return invalid(f"window size {rect[2:]}")
    x.focus(window)

    def shot(label=None):
        s = ic.screenshot(label or "poll", window, t0)
        if label:
            shots[label] = s
        return s

    def at(vx, vy):
        return (rect[0] + int(round(rect[2] / 2 + vx * rect[2] / ic.VIRTUAL[0])),
                rect[1] + int(round(rect[3] / 2 - vy * rect[3] / ic.VIRTUAL[1])))

    def wait_title(label):
        start = time.monotonic()
        while alive() and time.monotonic() - start < 180:
            s = shot()
            if title_visible(s):
                time.sleep(1.0)
                s2 = shot()
                if title_visible(s2):
                    shots[label] = s2
                    emit("title-visible", label=label)
                    return True
            time.sleep(0.5)
        return False

    def play(label):
        for attempt in range(1, 4):
            x.click(*at(0, 0))
            emit("click", target="Play", attempt=attempt)
            start = time.monotonic()
            while alive() and time.monotonic() - start < 60:
                s = shot()
                if ic.gameplay_signature(s)[0]:
                    settle = time.monotonic()
                    while time.monotonic() - settle < 30:
                        samples = [s.px(vx, -160) for vx in (-24, -16, -8, 0, 8, 16, 24)]
                        if ic.gameplay_signature(s)[0] and all(min(c) >= 240 for c in samples):
                            shots[label] = s
                            emit("gameplay-settled", label=label, clicks=attempt)
                            return s
                        time.sleep(0.5)
                        s = shot()
                    emit("gameplay-not-settled", label=label)
                    return None
                time.sleep(0.2)
            emit("gameplay-not-reached", attempt=attempt)
        return None

    if not wait_title("title-1"):
        return invalid("Title never visible")
    g = play("gameplay-1")
    if g is None:
        return invalid("gameplay not reached or not settled")
    ref, cal = ic.paddle_reference(g)
    emit("paddle-reference", **cal)
    if ref is None:
        return invalid("paddle colour not uniform")

    # ---- the frame stream: each new distinct screenshot is one game update ----
    state = {"prev": g, "n": 0, "key": None}

    def next_frame(phase):
        start = time.monotonic()
        while alive() and time.monotonic() - start < FRAME_TIMEOUT:
            s = shot()
            if s.rgb != state["prev"].rgb:
                state["prev"] = s
                state["n"] += 1
                c = ic.locate_paddle(s, ref)
                rec = {"frame": state["n"], "t": s.t, "phase": phase, "key": state["key"], "centre": c, "lives": ic.lives(s, ref)}
                frames_log.write(json.dumps(rec) + "\n")
                frames_log.flush()
                return rec, s
        return None, None

    c0 = ic.locate_paddle(g, ref)
    if c0 is None or abs(c0) > ic.STILL:
        return invalid(f"paddle not at x=0 at start (found {c0})")
    control = []
    for _ in range(CONTROL_FRAMES):
        rec, _s = next_frame("control")
        if rec is None:
            return invalid("game stopped producing frames during the control")
        control.append(rec["centre"])
    control_ok = all(c is not None and abs(c - c0) <= STILL_DELTA for c in control)
    emit("control", c0=c0, centres=control, still=control_ok)
    if not control_ok:
        return invalid("paddle moved (or was lost) with no input")

    def hold_and_release(keysym, name, goal):
        last = ic.locate_paddle(state["prev"], ref)
        state["key"] = name
        x.key(keysym, True)
        down_frame = state["n"]
        emit("key-down", key=name, frame=down_frame)
        held, first_move = [], None
        while True:
            rec, s = next_frame(f"hold-{name}")
            if rec is None:
                x.key(keysym, False)
                return {"error": "no frames while held"}
            since = rec["frame"] - down_frame
            c = rec["centre"]
            if c is not None and last is not None:
                step = abs(c - last)
                if first_move is None and step > STILL_DELTA:
                    first_move = since
                if first_move is not None:
                    held.append(step)
            if c is not None:
                last = c
            if c is not None and goal(c):
                break
            if first_move is None and since >= 60:
                x.key(keysym, False)
                return {"fail": "no visible movement within 60 frames of key-down"}
            if since >= 400:
                x.key(keysym, False)
                return {"error": "goal not reached within 400 frames"}
        shots[f"before-release-{name.lower()}"] = s
        x.key(keysym, False)
        state["key"] = None
        emit("key-up", key=name, frame=state["n"])
        after = []
        for _ in range(RELEASE_FRAMES):
            rec, s = next_frame(f"release-{name}")
            if rec is None:
                return {"error": "game stopped producing frames after release"}
            after.append(rec)
        shots[f"after-release-{name.lower()}"] = s
        prev_c, moves, unlocated = last, [], []
        for k, rec in enumerate(after, 1):
            c = rec["centre"]
            if c is None:
                unlocated.append(k)
                continue
            if abs(c - prev_c) > STILL_DELTA:
                moves.append(k)
            prev_c = c
        last_move = max(moves) if moves else 0
        steps_ok = sum(abs(st - STEP) <= STEP_TOL for st in held)
        return {
            "press_lag_frames": first_move,
            "held_moving_frames": len(held),
            "held_steps": held,
            "clock_share_4_unit_steps": round(steps_ok / len(held), 3) if held else 0.0,
            "centre_at_key_up": last,
            "release_moving_frames": moves,
            "release_unlocated_frames": unlocated,
            "release_lag_frames": last_move,
            "still_frames_after_last_move": RELEASE_FRAMES - last_move,
            "final_centre": prev_c,
            "final_lives": after[-1]["lives"],
            "at_clamp": abs(abs(prev_c) - 128) <= STILL_DELTA,
        }

    def check(window_result, name):
        if "error" in window_result:
            return invalid(f"{name}: {window_result['error']}")
        if len(window_result["release_unlocated_frames"]) > 5:
            return invalid(f"{name}: paddle not located on more than 5 release frames")
        return None

    right = hold_and_release(ic.XK_RIGHT, "Right", lambda c: c >= ic.MOVE)
    result["windows"]["Right"] = right
    if "fail" in right:
        result["verdict"] = "key-not-delivered"
        return finish(1)
    bad = check(right, "Right")
    if bad is not None:
        return bad
    left = hold_and_release(ic.XK_LEFT, "Left", lambda c: c <= -ic.MOVE)
    result["windows"]["Left"] = left
    if "fail" in left:
        result["verdict"] = "key-not-delivered"
        return finish(1)
    bad = check(left, "Left")
    if bad is not None:
        return bad

    clock_ok = all(w["clock_share_4_unit_steps"] >= STEP_SHARE for w in (right, left))
    lives_ok = all(w["final_lives"] >= 1 for w in (right, left))
    result["clock_validated"] = clock_ok
    if not clock_ok:
        return invalid("frame clock not validated (held steps were not 4 units per new frame)")
    if not lives_ok:
        return invalid("all lives lost before a release window ended")
    stuck = [n for n, w in (("Right", right), ("Left", left))
             if w["release_lag_frames"] > LAG_LIMIT or w["at_clamp"]]
    result["verdict"] = "release-works" if not stuck else "stuck-key"
    result["stuck_windows"] = stuck

    # secondary: leave by real clicks
    x.click(*at(232, -144))
    emit("click", target="Quit")
    if wait_title("title-2"):
        x.click(*at(0, -96))
        emit("click", target="Exit")
        try:
            game.wait(30)
            result["secondary"]["exit_by_click"] = game.returncode == 0
        except subprocess.TimeoutExpired:
            result["secondary"]["exit_by_click"] = False
    return finish(0 if not stuck else 1)


if __name__ == "__main__":
    raise SystemExit(main())
