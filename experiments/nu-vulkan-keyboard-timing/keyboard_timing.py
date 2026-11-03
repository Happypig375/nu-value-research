"""Keyboard input and release timing on Vulkan-era Nu (master 47ef39e), NVIDIA GPU, our own Xvfb.

Port of the 2 November keyboard input check and key-release check (experiments/nu-keyboard-input-check/,
experiments/nu-key-release-check/) to standalone MMCC Breakout at Nu master, judged only from screenshots.
The X input (XTEST), window handling, screenshot decoding and paddle/brick detection are copied unchanged from
input_check.py (lines 73-251). New here: timed press/release trials, because on the GPU the game runs about as fast
as or faster than screenshots can be taken, so updates can no longer be counted as distinct frames.
Protocol: docs/nu-vulkan-timing-reference-2026-11-03.md, part 2.

Usage: keyboard_timing.py GAME_DLL_DIR OUTPUT_DIR [--deadline 600] [--trials 3]
Needs DISPLAY/XAUTHORITY for a private Xvfb (scripts/linux_nu_vulkan_env.sh sets them).
"""
import argparse
import ctypes
import json
import os
import signal
import struct
import subprocess
import time
import zlib
from pathlib import Path

WINDOW_NAME = b"Breakout Mmcc"
EXPECTED_SIZE = (1280, 720)          # 640x360 virtual resolution, DisplayScalar 2 (App.config)
VIRTUAL = (640, 360)
XK_LEFT, XK_RIGHT = 0xFF51, 0xFF53
MATCH = 40                           # max per-channel difference for "paddle colour"
DARK = 48                            # max channel for "dark" wall pixels
BRIGHT = 96                          # max channel threshold for a "lit" brick centre
BRICKS = [(i * 64 - 128, j * 16 + 64) for i in range(5) for j in range(6)]
PADDLE_ROWS = (-157, -160, -163)
MOVE = 64                            # virtual units the paddle must travel each way
STILL = 4                            # virtual units allowed for "did not move"

# ---------- X11 / XTEST through ctypes ----------
X11 = ctypes.CDLL("libX11.so.6")
XTST = ctypes.CDLL("libXtst.so.6")
Win = ctypes.c_ulong
X11.XOpenDisplay.restype = ctypes.c_void_p
X11.XOpenDisplay.argtypes = [ctypes.c_char_p]
X11.XDefaultRootWindow.restype = Win
X11.XDefaultRootWindow.argtypes = [ctypes.c_void_p]
X11.XQueryTree.argtypes = [ctypes.c_void_p, Win, ctypes.POINTER(Win), ctypes.POINTER(Win),
                           ctypes.POINTER(ctypes.POINTER(Win)), ctypes.POINTER(ctypes.c_uint)]
X11.XFetchName.argtypes = [ctypes.c_void_p, Win, ctypes.POINTER(ctypes.c_char_p)]
X11.XFree.argtypes = [ctypes.c_void_p]


class XTextProperty(ctypes.Structure):
    _fields_ = [("value", ctypes.c_void_p), ("encoding", ctypes.c_ulong), ("format", ctypes.c_int), ("nitems", ctypes.c_ulong)]


X11.XGetWMName.argtypes = [ctypes.c_void_p, Win, ctypes.POINTER(XTextProperty)]
X11.XGetGeometry.argtypes = [ctypes.c_void_p, Win, ctypes.POINTER(Win), ctypes.POINTER(ctypes.c_int),
                             ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_uint),
                             ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_uint),
                             ctypes.POINTER(ctypes.c_uint)]
X11.XTranslateCoordinates.argtypes = [ctypes.c_void_p, Win, Win, ctypes.c_int, ctypes.c_int,
                                      ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int),
                                      ctypes.POINTER(Win)]
X11.XKeysymToKeycode.restype = ctypes.c_ubyte
X11.XKeysymToKeycode.argtypes = [ctypes.c_void_p, ctypes.c_ulong]
X11.XSetInputFocus.argtypes = [ctypes.c_void_p, Win, ctypes.c_int, ctypes.c_ulong]
X11.XSync.argtypes = [ctypes.c_void_p, ctypes.c_int]
XTST.XTestQueryExtension.argtypes = [ctypes.c_void_p] + [ctypes.POINTER(ctypes.c_int)] * 4
XTST.XTestFakeKeyEvent.argtypes = [ctypes.c_void_p, ctypes.c_uint, ctypes.c_int, ctypes.c_ulong]
XTST.XTestFakeMotionEvent.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_ulong]
XTST.XTestFakeButtonEvent.argtypes = [ctypes.c_void_p, ctypes.c_uint, ctypes.c_int, ctypes.c_ulong]



class X:
    def __init__(self):
        self.d = X11.XOpenDisplay(None)
        if not self.d:
            raise SystemExit("cannot open X display")
        ints = [ctypes.c_int() for _ in range(4)]
        if not XTST.XTestQueryExtension(self.d, *[ctypes.byref(i) for i in ints]):
            raise SystemExit("XTEST extension missing")
        self.root = X11.XDefaultRootWindow(self.d)

    def windows(self, w=None):
        w = self.root if w is None else w
        root, parent, children, n = Win(), Win(), ctypes.POINTER(Win)(), ctypes.c_uint()
        if not X11.XQueryTree(self.d, w, ctypes.byref(root), ctypes.byref(parent), ctypes.byref(children), ctypes.byref(n)):
            return []
        kids = [children[i] for i in range(n.value)]
        if children:
            X11.XFree(children)
        out = []
        for k in kids:
            out.append(k)
            out.extend(self.windows(k))
        return out

    def name(self, w):
        # Amendment 1: read WM_NAME's raw bytes whatever its encoding (SDL3 writes UTF8_STRING,
        # which XFetchName does not return).
        prop = XTextProperty()
        if X11.XGetWMName(self.d, w, ctypes.byref(prop)) and prop.value:
            value = ctypes.string_at(prop.value, prop.nitems) if prop.format == 8 else None
            X11.XFree(prop.value)
            return value
        return None

    def geometry(self, w):
        root, x, y, width, height, bw, depth = Win(), ctypes.c_int(), ctypes.c_int(), ctypes.c_uint(), ctypes.c_uint(), ctypes.c_uint(), ctypes.c_uint()
        X11.XGetGeometry(self.d, w, ctypes.byref(root), ctypes.byref(x), ctypes.byref(y), ctypes.byref(width),
                         ctypes.byref(height), ctypes.byref(bw), ctypes.byref(depth))
        ax, ay, child = ctypes.c_int(), ctypes.c_int(), Win()
        X11.XTranslateCoordinates(self.d, w, self.root, 0, 0, ctypes.byref(ax), ctypes.byref(ay), ctypes.byref(child))
        return ax.value, ay.value, width.value, height.value

    def find(self):
        for w in self.windows():
            if self.name(w) == WINDOW_NAME:
                return w
        return None

    def focus(self, w):
        X11.XSetInputFocus(self.d, w, 2, 0)   # RevertToParent, CurrentTime: what a window manager does on click
        X11.XSync(self.d, 0)

    def key(self, keysym, down):
        code = X11.XKeysymToKeycode(self.d, keysym)
        XTST.XTestFakeKeyEvent(self.d, code, 1 if down else 0, 0)
        X11.XSync(self.d, 0)
        return code

    def click(self, x, y):
        XTST.XTestFakeMotionEvent(self.d, -1, x, y, 0)
        X11.XSync(self.d, 0)
        time.sleep(0.1)
        XTST.XTestFakeButtonEvent(self.d, 1, 1, 0)
        X11.XSync(self.d, 0)
        time.sleep(0.08)
        XTST.XTestFakeButtonEvent(self.d, 1, 0, 0)
        X11.XSync(self.d, 0)


# ---------- screenshots ----------
class Shot:
    def __init__(self, label, rgb, width, height, t):
        self.label, self.rgb, self.w, self.h, self.t = label, rgb, width, height, t

    def px(self, vx, vy):
        x = int(round(self.w / 2 + vx * self.w / VIRTUAL[0]))
        y = int(round(self.h / 2 - vy * self.h / VIRTUAL[1]))
        x, y = min(max(x, 0), self.w - 1), min(max(y, 0), self.h - 1)
        i = (y * self.w + x) * 3
        return tuple(self.rgb[i:i + 3])

    def png(self, path):
        raw = bytearray()
        stride = self.w * 3
        for y in range(self.h):
            raw.append(0)
            raw.extend(self.rgb[y * stride:(y + 1) * stride])

        def chunk(kind, data):
            return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
        path.write_bytes(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", self.w, self.h, 8, 2, 0, 0, 0))
                         + chunk(b"IDAT", zlib.compress(bytes(raw), 6)) + chunk(b"IEND", b""))


def screenshot(label, window, t0):
    # Amendment 2: capture the game window itself (`xwd -id`), not the root. The game's DirectColor
    # window makes `xwd -root` use a mixed-visual layout. DirectColor pixels index the colour map
    # that xwd stores in the file, so each channel is mapped through it.
    data = subprocess.run(["xwd", "-id", str(window), "-silent"], capture_output=True, check=True).stdout
    h = struct.unpack(">25I", data[:100])
    header_size, fmt, width, height, byte_order, bpp, bpl = h[0], h[2], h[4], h[5], h[7], h[11], h[12]
    vclass, rmask, gmask, bmask, ncolors = h[13], h[14], h[15], h[16], h[19]
    if fmt != 2 or bpp != 32 or (rmask, gmask, bmask) != (0xFF0000, 0xFF00, 0xFF):
        raise SystemExit(f"unexpected xwd format {fmt} {bpp} {rmask:x}")
    luts = [bytearray(range(256)) for _ in range(3)]
    if vclass == 5:  # DirectColor
        for k in range(ncolors):
            pixel, red, green, blue = struct.unpack(">IHHH", data[header_size + 12 * k:header_size + 12 * k + 10])
            luts[0][(pixel & rmask) >> 16] = red >> 8
            luts[1][(pixel & gmask) >> 8] = green >> 8
            luts[2][pixel & bmask] = blue >> 8
    luts = [bytes(lut) for lut in luts]
    pixels = data[header_size + ncolors * 12:]
    rgb = bytearray(width * height * 3)
    for row in range(height):
        line = pixels[row * bpl:row * bpl + width * 4]
        if byte_order == 0:        # LSBFirst: B G R X
            r, g, b = line[2::4], line[1::4], line[0::4]
        else:                      # MSBFirst: X R G B
            r, g, b = line[1::4], line[2::4], line[3::4]
        o = row * width * 3
        n = width * 3
        rgb[o:o + n:3], rgb[o + 1:o + n:3], rgb[o + 2:o + n:3] = r.translate(luts[0]), g.translate(luts[1]), b.translate(luts[2])
    return Shot(label, rgb, width, height, round(time.monotonic() - t0, 3))


# ---------- judging rules (fixed by the protocol) ----------
def diff(a, b):
    return max(abs(p - q) for p, q in zip(a, b))


def gameplay_signature(s):
    left = sum(max(s.px(-164, y)) <= DARK for y in range(-170, 171, 10))
    right = sum(max(s.px(164, y)) <= DARK for y in range(-170, 171, 10))
    top = sum(max(s.px(x, 176)) <= DARK for x in range(-150, 151, 10))
    # Amendment 3: sample 4 units above each brick centre; the brick image has a black line at its exact centre.
    lit = [max(s.px(x, y + 4)) >= BRIGHT for x, y in BRICKS]
    upper = sum(lit[k] for k, (x, y) in enumerate(BRICKS) if y >= 128)
    ok = left >= 32 and right >= 32 and top >= 28 and sum(lit) >= 25 and upper >= 8
    return ok, {"leftDark": left, "rightDark": right, "topDark": top, "litBricks": sum(lit), "litUpperBricks": upper}


def paddle_reference(s):
    samples = [s.px(x, -160) for x in (-24, -16, -8, 0, 8, 16, 24)]
    median = tuple(sorted(c[k] for c in samples)[3] for k in range(3))
    close = sum(diff(c, median) <= MATCH for c in samples)
    return (median if close >= 6 else None), {"samples": samples, "median": median, "close": close}


def locate_paddle(s, ref):
    scale = s.w / VIRTUAL[0]
    centres = []
    for vy in PADDLE_ROWS:
        y = int(round(s.h / 2 - vy * s.h / VIRTUAL[1]))
        x0, x1 = int(round(s.w / 2 - 160 * scale)), int(round(s.w / 2 + 160 * scale))
        best, run_start = None, None
        for x in range(x0, x1 + 1):
            i = (y * s.w + x) * 3
            match = x < x1 and diff(tuple(s.rgb[i:i + 3]), ref) <= MATCH
            if match and run_start is None:
                run_start = x
            elif not match and run_start is not None:
                width = (x - run_start) / scale
                if best is None or width > best[0]:
                    best = (width, (run_start + x - 1) / 2)
                run_start = None
        if best and 48 <= best[0] <= 80:
            centres.append(round((best[1] - s.w / 2) / scale, 2))
    if len(centres) < 2:
        return None
    centres.sort()
    return centres[len(centres) // 2]


def lives(s, ref):
    return sum(diff(s.px(-240, -16 * (i + 1)), ref) <= MATCH for i in range(5))


# ---------- the check ----------


# ---------- timing trials (new in this port; fixed by the protocol) ----------
TRIAL_TRAVEL = 32       # release once a screenshot shows the paddle this far (virtual units) from the trial start
MOVED = 2               # a change of at least this much counts as movement
STABLE_SECONDS = 0.5    # the paddle counts as stopped once unchanged (within 0.5 units) for this long
UNITS_PER_UPDATE = 4    # Gameplay.update moves the paddle 4 units per update while a key is held


def timed_shot(window, t0):
    start = time.monotonic() - t0
    s = screenshot(None, window, t0)
    return s, round(start, 4), s.t


def trial(x, window, ref, t0, keysym, name, sign, emit):
    s, a, b = timed_shot(window, t0)
    p0 = locate_paddle(s, ref)
    if p0 is None:
        return {"key": name, "valid": False, "reason": "paddle not found before the trial"}
    polls = []
    x.key(keysym, True)
    t_down = round(time.monotonic() - t0, 4)
    released, t_up = False, None
    deadline = time.monotonic() + 8
    while time.monotonic() < deadline:
        s, a, b = timed_shot(window, t0)
        c = locate_paddle(s, ref)
        polls.append([a, b, c])
        if not released and c is not None and sign * (c - p0) >= TRIAL_TRAVEL:
            x.key(keysym, False)
            t_up = round(time.monotonic() - t0, 4)
            released = True
        if released and c is not None:
            stable_since = None
            for pa, pb, pc in reversed(polls):
                if pc is None or abs(pc - c) > 0.5 or pa < t_up:
                    break
                stable_since = pa
            if stable_since is not None and b - stable_since >= STABLE_SECONDS:
                break
    if not released:
        x.key(keysym, False)
        t_up = round(time.monotonic() - t0, 4)
    emit("trial-polls", key=name, p0=p0, t_down=t_down, t_up=t_up, polls=polls)
    found = [(pa, pb, pc) for pa, pb, pc in polls if pc is not None]
    if not released or not found:
        return {"key": name, "valid": False, "reason": "paddle did not travel 32 units within 8 s", "p0": p0}
    final = found[-1][2]
    first_move = next(((pa, pb, pc) for pa, pb, pc in found if abs(pc - p0) >= MOVED), None)
    before_move = [(pa, pb, pc) for pa, pb, pc in found if first_move and pb <= first_move[0]]
    before_up = [(pa, pb, pc) for pa, pb, pc in found if pb <= t_up]
    after_up = [(pa, pb, pc) for pa, pb, pc in found if pa >= t_up]
    last_change = None
    for pa, pb, pc in after_up:
        if abs(pc - final) > 0.5:
            last_change = (pa, pb, pc)
    first_final = next(((pa, pb, pc) for pa, pb, pc in after_up if abs(pc - final) <= 0.5 and (last_change is None or pa > last_change[1])), None)
    moving = [(pa, pb, pc) for pa, pb, pc in found if first_move and pa >= first_move[0] and pb <= t_up]
    speed = None
    if len(moving) >= 2 and moving[-1][1] > moving[0][1]:
        speed = abs(moving[-1][2] - moving[0][2]) / (((moving[-1][0] + moving[-1][1]) - (moving[0][0] + moving[0][1])) / 2)
    at_up = before_up[-1][2] if before_up else None
    shots = [pb - pa for pa, pb, pc in polls]
    return {
        "key": name, "valid": True, "p0": p0, "final": final, "t_down": t_down, "t_up": t_up,
        "press_latency_ms": {"upper": round((first_move[1] - t_down) * 1000, 1) if first_move else None,
                             "lower": round((max(before_move[-1][0], t_down) - t_down) * 1000, 1) if before_move else 0.0},
        "release_stop_ms": {"upper": round((first_final[1] - t_up) * 1000, 1) if first_final else None,
                            "lower": round((last_change[0] - t_up) * 1000, 1) if last_change else 0.0},
        "overshoot_units": round(sign * (final - at_up), 2) if at_up is not None else None,
        "overshoot_updates": round(sign * (final - at_up) / UNITS_PER_UPDATE, 2) if at_up is not None else None,
        "speed_units_per_s": round(speed, 1) if speed else None,
        "updates_per_s": round(speed / UNITS_PER_UPDATE, 1) if speed else None,
        "screenshot_ms": {"median": round(sorted(shots)[len(shots) // 2] * 1000, 1), "max": round(max(shots) * 1000, 1), "n": len(shots)},
        "stopped": True,
    }


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
    ap.add_argument("--deadline", type=float, default=600)
    ap.add_argument("--trials", type=int, default=3)
    a = ap.parse_args()
    game_dir, out = a.game_dir.resolve(strict=True), a.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    trace = (out / "trace.jsonl").open("w")
    t0 = time.monotonic()
    shots = {}

    def emit(event, **data):
        rec = {"event": event, "t": round(time.monotonic() - t0, 3), **data}
        trace.write(json.dumps(rec) + "\n")
        trace.flush()
        return rec

    result = {"validity": None, "trials": [], "secondary": {}, "invalid": None}
    game = subprocess.Popen(["dotnet", str(game_dir / "Breakout Mmcc.dll")], cwd=game_dir,
                            stdout=(out / "game-stdout.log").open("wb"), stderr=(out / "game-stderr.log").open("wb"),
                            start_new_session=True)
    children.append(game)
    emit("launched", pid=game.pid)
    x = X()

    def alive():
        return game.poll() is None

    def overdue():
        return time.monotonic() - t0 > a.deadline

    def finish(code):
        if alive():
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
        print(json.dumps({k: result[k] for k in ("validity", "invalid", "secondary", "game_exit_code")}, indent=2))
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
        return invalid("game window not found within 120 s" if alive() else f"game exited early ({game.returncode})")
    time.sleep(1.0)
    rect = x.geometry(window)
    emit("window", id=window, rect=rect)
    if tuple(rect[2:]) != EXPECTED_SIZE:
        return invalid(f"window size {rect[2:]} is not {EXPECTED_SIZE}")
    x.focus(window)

    def shot(label=None):
        s = screenshot(label or "poll", window, t0)
        if label:
            shots[label] = s
        return s

    def centre_of(vx, vy):
        return rect[0] + int(round(rect[2] / 2 + vx * rect[2] / VIRTUAL[0])), rect[1] + int(round(rect[3] / 2 - vy * rect[3] / VIRTUAL[1]))

    def wait_title(label, min_wait):
        start = time.monotonic()
        prev, same = None, 0
        while alive() and not overdue() and time.monotonic() - start < 120:
            s = shot()
            region = [s.px(vx, vy) for vx in range(-100, 101, 10) for vy in range(-40, 41, 10)]
            same = same + 1 if region == prev else 0
            prev = region
            if same >= 2 and time.monotonic() - start >= min_wait and not gameplay_signature(s)[0]:
                shots[label] = s
                emit("title-stable", label=label)
                return True
            time.sleep(1.0)
        return False

    def play(label):
        sig = {}
        for attempt in range(1, 4):
            px, py = centre_of(0, 0)
            x.click(px, py)
            emit("click", target="Play", at=[px, py], attempt=attempt)
            start = time.monotonic()
            while alive() and time.monotonic() - start < 30:
                s = shot()
                ok, sig = gameplay_signature(s)
                if ok:
                    emit("gameplay-reached", label=label, clicks=attempt, signature=sig)
                    settle = time.monotonic()
                    while time.monotonic() - settle < 30:
                        samples = [s.px(vx, -160) for vx in (-24, -16, -8, 0, 8, 16, 24)]
                        if gameplay_signature(s)[0] and all(min(c) >= 240 for c in samples):
                            break
                        time.sleep(0.5)
                        s = shot()
                    else:
                        emit("gameplay-not-settled", label=label)
                    shots[label] = s
                    emit("gameplay-settled", label=label, paddle_colour=paddle_reference(s)[0])
                    return s, attempt
                time.sleep(0.2)
            emit("gameplay-not-reached", attempt=attempt, signature=sig)
            time.sleep(10)
        return None, 3

    if not wait_title("title-1", 10):
        return invalid("title screen never became stable")
    g, clicks = play("gameplay-1")
    if g is None:
        result["validity"] = {"pass": False, "reason": "gameplay not reached after 3 Play clicks"}
        return finish(1)
    ref, cal = paddle_reference(g)
    emit("paddle-reference", **cal)
    if ref is None:
        return invalid("paddle colour not uniform at its start position")
    c0 = locate_paddle(g, ref)
    time.sleep(0.5)
    c1 = locate_paddle(shot("control-no-input"), ref)
    emit("control", c0=c0, c1=c1)
    if c0 is None or abs(c0) > STILL:
        return invalid(f"paddle not found at x=0 in first gameplay screenshot (found {c0})")
    control_ok = c1 is not None and abs(c1 - c0) <= STILL

    for k in range(a.trials):
        for keysym, name, sign in ((XK_RIGHT, "Right", 1), (XK_LEFT, "Left", -1)):
            r = trial(x, window, ref, t0, keysym, name, sign, emit)
            r["index"] = k + 1
            result["trials"].append(r)
            emit("trial", **r)
            time.sleep(0.3)
    shot("after-trials")
    result["validity"] = {"pass": control_ok and all(t["valid"] for t in result["trials"]),
                          "gameplay_reached_by_click": True, "play_clicks": clicks, "no_input_control_still": control_ok,
                          "all_trials_moved_and_stopped": all(t["valid"] for t in result["trials"])}

    qx, qy = centre_of(232, -144)
    x.click(qx, qy)
    emit("click", target="Quit", at=[qx, qy])
    left_gameplay = wait_title("title-2", 3)
    result["secondary"]["quit_reached_title"] = left_gameplay
    if left_gameplay:
        g2, clicks2 = play("gameplay-2")
        if g2 is not None:
            c = locate_paddle(g2, ref)
            n = lives(g2, ref)
            result["secondary"]["replay"] = {"reached": True, "clicks": clicks2, "paddle_centre": c, "lives": n,
                                             "fresh": c is not None and abs(c) <= STILL and n == 5}
            x.click(qx, qy)
            emit("click", target="Quit", at=[qx, qy])
            if wait_title("title-3", 3):
                ex, ey = centre_of(0, -96)
                x.click(ex, ey)
                emit("click", target="Exit", at=[ex, ey])
                try:
                    game.wait(30)
                    emit("game-exited", exit_code=game.returncode)
                    result["secondary"]["exit_by_click"] = game.returncode == 0
                except subprocess.TimeoutExpired:
                    result["secondary"]["exit_by_click"] = False
        else:
            result["secondary"]["replay"] = {"reached": False}
    return finish(0 if result["validity"]["pass"] else 1)


if __name__ == "__main__":
    raise SystemExit(main())
