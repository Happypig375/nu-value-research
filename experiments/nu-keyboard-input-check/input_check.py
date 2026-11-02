"""Send real key and mouse events through the X server to the unchanged standalone
MMCC Breakout game, and judge the result only from screenshots.

Keyboard input check (docs/nu-keyboard-input-check-2026-11-02.md). New work,
separate from the stopped R02 input-construction gate; it uses none of that draft.

Input: the X server's XTEST extension (libXtst), the same route a physical
keyboard's events take into SDL's X11 backend. Observation: `xwd -root`
screenshots, cropped to the game window. Nothing is read from inside the game.

Usage: input_check.py GAME_DLL_DIR OUTPUT_DIR [--deadline 600]
Needs DISPLAY/XAUTHORITY for a private Xvfb (scripts/linux_nu_env.sh sets them).
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
        p = ctypes.c_char_p()
        if X11.XFetchName(self.d, w, ctypes.byref(p)) and p.value is not None:
            return p.value
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


def screenshot(label, rect, t0):
    data = subprocess.run(["xwd", "-root", "-silent"], capture_output=True, check=True).stdout
    h = struct.unpack(">25I", data[:100])
    header_size, fmt, width, height, byte_order, bpp, bpl = h[0], h[2], h[4], h[5], h[7], h[11], h[12]
    rmask, gmask, bmask, ncolors = h[14], h[15], h[16], h[19]
    if fmt != 2 or bpp != 32 or (rmask, gmask, bmask) != (0xFF0000, 0xFF00, 0xFF):
        raise SystemExit(f"unexpected xwd format {fmt} {bpp} {rmask:x}")
    pixels = data[header_size + ncolors * 12:]
    wx, wy, ww, wh = rect
    rgb = bytearray(ww * wh * 3)
    for row in range(wh):
        line = pixels[(wy + row) * bpl + wx * 4:(wy + row) * bpl + (wx + ww) * 4]
        if byte_order == 0:        # LSBFirst: B G R X
            r, g, b = line[2::4], line[1::4], line[0::4]
        else:                      # MSBFirst: X R G B
            r, g, b = line[1::4], line[2::4], line[3::4]
        o = row * ww * 3
        rgb[o:o + ww * 3:3], rgb[o + 1:o + ww * 3:3], rgb[o + 2:o + ww * 3:3] = r, g, b
    return Shot(label, rgb, ww, wh, round(time.monotonic() - t0, 3))


# ---------- judging rules (fixed by the protocol) ----------
def diff(a, b):
    return max(abs(p - q) for p, q in zip(a, b))


def gameplay_signature(s):
    left = sum(max(s.px(-164, y)) <= DARK for y in range(-170, 171, 10))
    right = sum(max(s.px(164, y)) <= DARK for y in range(-170, 171, 10))
    top = sum(max(s.px(x, 176)) <= DARK for x in range(-150, 151, 10))
    lit = [max(s.px(x, y)) >= BRIGHT for x, y in BRICKS]
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
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("game_dir", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--deadline", type=float, default=600)
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

    result = {"primary": None, "secondary": {}, "invalid": None}
    game = subprocess.Popen(["dotnet", str(game_dir / "Breakout Mmcc.dll")], cwd=game_dir,
                            stdout=(out / "game-stdout.log").open("wb"), stderr=(out / "game-stderr.log").open("wb"),
                            start_new_session=True)
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
        print(json.dumps(result, indent=2))
        return code

    def invalid(reason):
        result["invalid"] = reason
        emit("invalid", reason=reason)
        return finish(2)

    # 1. window
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
        s = screenshot(label or "poll", rect, t0)
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
                    shots[label] = s
                    emit("gameplay-reached", label=label, clicks=attempt, signature=sig)
                    return s, attempt
                time.sleep(0.2)
            emit("gameplay-not-reached", attempt=attempt, signature=sig)
            time.sleep(10)
        return None, 3

    # 2. title, then Play by a real mouse click
    if not wait_title("title-1", 10):
        return invalid("title screen never became stable")
    g, clicks = play("gameplay-1")
    if g is None:
        result["primary"] = {"pass": False, "reason": "gameplay not reached after 3 Play clicks"}
        return finish(1)

    # 3. calibrate the paddle colour at its known start (x = 0) and run the no-input control
    ref, cal = paddle_reference(g)
    emit("paddle-reference", **cal)
    if ref is None:
        return invalid("paddle colour not uniform at its start position")
    c0 = locate_paddle(g, ref)
    time.sleep(0.5)
    c1s = shot("control-no-input")
    c1 = locate_paddle(c1s, ref)
    emit("control", c0=c0, c1=c1, lives=lives(c1s, ref))
    if c0 is None or abs(c0) > STILL:
        return invalid(f"paddle not found at x=0 in first gameplay screenshot (found {c0})")
    control_ok = c1 is not None and abs(c1 - c0) <= STILL

    # 4. hold Right, then Left; poll screenshots while held
    def hold(keysym, name, goal):
        code = x.key(keysym, True)
        emit("key-down", key=name, keycode=code)
        polls, start = [], time.monotonic()
        while time.monotonic() - start < 20:
            c = locate_paddle(shot(), ref)
            polls.append([round(time.monotonic() - t0, 3), c])
            if c is not None and goal(c):
                break
        x.key(keysym, False)
        emit("key-up", key=name, polls=polls)
        time.sleep(0.3)
        s = shot(f"after-{name.lower()}")
        c = locate_paddle(s, ref)
        emit("after-key", key=name, centre=c, lives=lives(s, ref))
        return c

    right = hold(XK_RIGHT, "Right", lambda c: c >= MOVE)
    left = hold(XK_LEFT, "Left", lambda c: c <= -MOVE)
    time.sleep(1.0)
    rest = shot("after-release")
    c4 = locate_paddle(rest, ref)
    emit("after-release", centre=c4, lives=lives(rest, ref))
    checks = {
        "gameplay_reached_by_click": True,
        "play_clicks": clicks,
        "no_input_control_still": control_ok,
        "right_moved": right is not None and right >= MOVE,
        "left_moved": left is not None and left <= -MOVE,
        "stopped_after_release": c4 is not None and left is not None and abs(c4 - left) <= STILL,
    }
    result["primary"] = {"pass": all(v for k, v in checks.items() if k != "play_clicks"), "checks": checks,
                         "centres": {"c0": c0, "c1": c1, "after_right": right, "after_left": left, "after_release": c4}}

    # 5. secondary: Quit by click -> title -> Play by click gives a fresh board -> Quit -> Exit by click
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
    return finish(0 if result["primary"]["pass"] else 1)


if __name__ == "__main__":
    raise SystemExit(main())
