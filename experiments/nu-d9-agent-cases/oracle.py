"""D9 direction 4 behavioural oracle: does a Breakout Mmcc build implement the Paused task?

Runs the game (built with the oracle's observer Program.fs, see prepare.py) on our own Xvfb with NVIDIA Vulkan,
presses real keys and clicks through XTEST (the X helpers are imported unchanged from
experiments/nu-vulkan-keyboard-timing/keyboard_timing.py), and judges checks (a)-(e) from the game's own per-frame
trace (entity positions and texts), never from screenshots. Protocol: docs/nu-d9-agent-cases-2026-11-11.md.

Usage: oracle.py GAME_DLL_DIR OUTPUT_DIR [--deadline 300]
Needs DISPLAY/XAUTHORITY for a private Xvfb (scripts/linux_nu_vulkan_env.sh sets them).
"""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import signal
import subprocess
import time

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("kt", HERE.parent / "nu-vulkan-keyboard-timing" / "keyboard_timing.py")
kt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(kt)

XK_P, XK_RIGHT = 0x0070, 0xFF53
TAP = 0.08            # seconds a P tap is held
SETTLE = 0.4          # seconds after a P tap before a window is judged
STILL = 0.01          # max position change (virtual units) that counts as "not moving"
STEP = 6.5            # max distance of the first resumed ball position from the paused one (about 2 updates)
MOVED = 8.0           # paddle travel (virtual units) that counts as "moved" after holding Right for 0.25 s


def norm(text):
    return None if text is None else text.strip().rstrip("!.").strip().lower()


class Trace:
    def __init__(self, path):
        self.path, self.fh, self.buf, self.frames = path, None, "", []

    def pump(self):
        if self.fh is None:
            if not self.path.exists():
                return
            self.fh = self.path.open("r")
        chunk = self.fh.read()
        if not chunk:
            return
        self.buf += chunk
        *lines, self.buf = self.buf.split("\n")
        now = time.monotonic()
        for line in lines:
            if line.strip():
                rec = json.loads(line)
                rec["t"] = now
                self.frames.append(rec)

    def last(self):
        self.pump()
        return self.frames[-1] if self.frames else None

    def window(self, seconds, during=None):
        """Collect the frames that arrive in the next `seconds`; `during(elapsed)` may act (e.g. press keys)."""
        self.pump()
        start_index, start = len(self.frames), time.monotonic()
        while time.monotonic() - start < seconds:
            if during:
                during(time.monotonic() - start)
            time.sleep(0.01)
            self.pump()
        return self.frames[start_index:]


def same(p, q):
    return p is not None and q is not None and abs(p[0] - q[0]) <= STILL and abs(p[1] - q[1]) <= STILL


def dist(p, q):
    return ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("game_dir", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--deadline", type=float, default=300)
    a = ap.parse_args()
    game_dir, out = a.game_dir.resolve(strict=True), a.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    trace = Trace(out / "trace.jsonl")
    log = (out / "oracle-events.jsonl").open("w")
    t0 = time.monotonic()

    def emit(event, **data):
        log.write(json.dumps({"event": event, "t": round(time.monotonic() - t0, 3), **data}) + "\n")
        log.flush()

    env = dict(os.environ, ORACLE_TRACE=str(out / "trace.jsonl"))
    game = subprocess.Popen(["dotnet", str(game_dir / "Breakout Mmcc.dll")], cwd=game_dir, env=env,
                            stdout=(out / "game-stdout.log").open("wb"), stderr=(out / "game-stderr.log").open("wb"),
                            start_new_session=True)
    emit("launched", pid=game.pid)
    result = {"checks": {}, "details": {}, "invalid": None}
    x = kt.X()

    def alive():
        return game.poll() is None

    def finish():
        if alive():
            os.killpg(game.pid, signal.SIGTERM)
            try:
                game.wait(15)
            except subprocess.TimeoutExpired:
                os.killpg(game.pid, signal.SIGKILL)
                game.wait(15)
        result["game_exit_code"] = game.returncode
        result["elapsed_seconds"] = round(time.monotonic() - t0, 1)
        stdout = (out / "game-stdout.log").read_text(errors="replace")
        result["vulkan_device_line"] = "Selected Vulkan Device NVIDIA GeForce RTX 4090 D" in stdout
        if result["invalid"] is None and not result["vulkan_device_line"]:
            result["invalid"] = "no NVIDIA Vulkan device line in the game log"
        checks = result["checks"]
        result["pass"] = (result["invalid"] is None and all(checks.get(k) for k in "abcde"))
        (out / "result.json").write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps({"pass": result["pass"], "checks": checks, "invalid": result["invalid"]}))
        return 0 if result["invalid"] is None else 2

    def fail_rest(reason):
        for k in "abcde":
            result["checks"].setdefault(k, False)
        result["details"]["stopped"] = reason
        emit("stopped", reason=reason)

    try:
        window = None
        while window is None and alive() and time.monotonic() - t0 < 120:
            window = x.find()
            if window is None:
                time.sleep(0.5)
        if window is None:
            if alive():
                result["invalid"] = "game window not found within 120 s"
            else:
                fail_rest(f"game exited before its window appeared (exit {game.returncode})")
            return finish()
        time.sleep(1.0)
        rect = x.geometry(window)
        x.focus(window)
        emit("window", rect=rect)

        def at(vx, vy):
            return (rect[0] + int(round(rect[2] / 2 + vx * rect[2] / kt.VIRTUAL[0])),
                    rect[1] + int(round(rect[3] / 2 - vy * rect[3] / kt.VIRTUAL[1])))

        def tap(keysym):
            x.key(keysym, True)
            time.sleep(TAP)
            x.key(keysym, False)

        def wait_screen(name, seconds):
            start = time.monotonic()
            while alive() and time.monotonic() - start < seconds:
                f = trace.last()
                if f and f["screen"] == name:
                    return True
                time.sleep(0.05)
            return False

        def start_play(label):
            """Click Play (up to 3 times) until the Gameplay screen shows a moving ball. Returns frames or None."""
            for attempt in range(1, 4):
                x.click(*at(0, 0))
                emit("click", target="Play", attempt=attempt, label=label)
                if wait_screen("Gameplay", 30):
                    start = time.monotonic()
                    while alive() and time.monotonic() - start < 10:
                        frames = trace.window(0.3)
                        balls = [f.get("ball") for f in frames if f.get("ball")]
                        if len(balls) >= 2 and not same(balls[0], balls[-1]):
                            emit("gameplay-moving", label=label, clicks=attempt)
                            return frames
                    return None
                time.sleep(5)
            return None

        def wait_title_stable():
            start = time.monotonic()
            while alive() and time.monotonic() - a.deadline < t0 and time.monotonic() - start < 120:
                if wait_screen("Title", 1) and all(f["screen"] == "Title" for f in trace.window(2.0)):
                    return True
            return False

        def hold_right(seconds):
            x.key(XK_RIGHT, True)
            time.sleep(seconds)
            x.key(XK_RIGHT, False)

        if not wait_title_stable():
            result["invalid"] = "title screen never became stable"
            return finish()
        if start_play("first") is None:
            fail_rest("gameplay with a moving ball not reached after 3 Play clicks")
            return finish()

        # (e) normal play: the ball moves (seen above) and Right moves the paddle
        p0 = trace.last()["paddle"]
        hold_right(0.25)
        time.sleep(0.1)
        p1 = trace.last()["paddle"]
        result["details"]["e"] = {"paddle_before": p0, "paddle_after": p1, "ball_moving": True}
        result["checks"]["e"] = p0 is not None and p1 is not None and p1[0] - p0[0] >= MOVED

        # (a) pause stops paddle and ball, (b) the message reads "Paused"
        tap(XK_P)
        emit("key", key="P", purpose="pause")
        time.sleep(SETTLE)
        pressed = {"down": False, "up": False}

        def right_mid_window(elapsed):
            if elapsed >= 0.2 and not pressed["down"]:
                x.key(XK_RIGHT, True)
                pressed["down"] = True
            if elapsed >= 0.7 and not pressed["up"]:
                x.key(XK_RIGHT, False)
                pressed["up"] = True

        w1 = trace.window(1.0, right_mid_window)
        if not pressed["up"]:
            x.key(XK_RIGHT, False)
        in_play = [f for f in w1 if f["screen"] == "Gameplay"]
        positions_ok = (len(w1) >= 10 and len(in_play) == len(w1)
                        and all(f.get("paddle") and f.get("ball") for f in w1)
                        and all(same(f["paddle"], w1[0]["paddle"]) and same(f["ball"], w1[0]["ball"]) for f in w1))
        messages = sorted({str(f.get("message")) for f in w1})
        result["details"]["a"] = {"frames": len(w1), "first": {k: w1[0].get(k) for k in ("paddle", "ball")} if w1 else None,
                                  "last": {k: w1[-1].get(k) for k in ("paddle", "ball")} if w1 else None}
        result["details"]["b"] = {"messages_seen": messages}
        result["checks"]["a"] = positions_ok
        result["checks"]["b"] = bool(w1) and all(norm(f.get("message")) == "paused" for f in w1)

        # (c) resume continues from the same state
        s = w1[-1] if w1 else trace.last()
        trace.pump()
        since = len(trace.frames)   # amendment 4: judge from the frame before the tap (resume acts on key-down)
        tap(XK_P)
        emit("key", key="P", purpose="resume")
        trace.window(1.0 - TAP)
        w2 = trace.frames[since:]
        moved = next((f for f in w2 if f.get("ball") and s.get("ball") and not same(f["ball"], s["ball"])), None)
        c = {"paused_ball": s.get("ball"), "first_moved_ball": moved and moved["ball"],
             "score_before": s.get("score"), "score_at_resume": moved and moved.get("score"),
             "lives_before": s.get("lives"), "lives_at_resume": moved and moved.get("lives")}
        late = [f for f in w2 if f["t"] - w2[0]["t"] >= 0.5] if w2 else []
        c["messages_after_resume"] = sorted({str(f.get("message")) for f in late})
        q0 = trace.last().get("paddle")
        hold_right(0.25)
        time.sleep(0.1)
        q1 = trace.last().get("paddle")
        c["paddle_before"], c["paddle_after"] = q0, q1
        result["details"]["c"] = c
        result["checks"]["c"] = bool(
            moved and s.get("ball") and dist(moved["ball"], s["ball"]) <= STEP
            and moved.get("score") == s.get("score") and moved.get("lives") == s.get("lives")
            and late and all(norm(f.get("message")) != "paused" for f in late)
            and q0 and q1 and q1[0] - q0[0] >= MOVED)

        # (d) Quit while paused returns to the title, and a new game starts normally
        tap(XK_P)
        emit("key", key="P", purpose="pause before quit")
        time.sleep(SETTLE)
        w3 = trace.window(0.3)
        d = {"paused_before_quit": bool(w3) and all(same(f.get("ball"), w3[0].get("ball")) for f in w3)}
        quit_pos = trace.last().get("quit")
        d["quit_entity"] = quit_pos
        if quit_pos is None:
            d["title_reached"] = False
            result["checks"]["d"] = False
        else:
            x.click(*at(*quit_pos))
            emit("click", target="Quit", at=quit_pos)
            d["title_reached"] = wait_screen("Title", 8)
            replay = start_play("replay") if d["title_reached"] else None
            if replay:
                f = trace.last()
                d["replay"] = {"lives": f.get("lives"), "message": f.get("message"), "score": f.get("score")}
            result["checks"]["d"] = bool(d["title_reached"] and replay and trace.last().get("lives") == 5
                                         and norm(trace.last().get("message")) != "paused")
        result["details"]["d"] = d
        return finish()
    except Exception as exc:  # an oracle error is never scored as a candidate failure
        result["invalid"] = f"oracle error: {exc!r}"
        return finish()


if __name__ == "__main__":
    raise SystemExit(main())
