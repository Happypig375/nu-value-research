"""Fail-closed wrapper over a scored direction 3 run, version 2 (D9 offline validation, 10 Nov 2026).

Fixes the reviewer's V1 on v1: any error reading any input is a FAIL with a reason (never a crash), and the process
exit code is 0 only for PASS (1 for FAIL). PASS only if check.py's score.json says pass AND both exit_code.txt read
exactly "0" AND both stdout logs contain the NVIDIA Vulkan device line. check.py itself is unchanged.
Usage: validate_run_v2.py RUN_DIR
"""
import json
from pathlib import Path
import sys

LINE = "Selected Vulkan Device NVIDIA GeForce RTX 4090 D"


def read(path):
    try:
        return path.read_bytes().decode("utf-8", errors="replace"), None
    except Exception as e:
        return None, type(e).__name__


def main():
    run = Path(sys.argv[1])
    reasons = []
    text, err = read(run / "score.json")
    try:
        ok = err is None and json.loads(text).get("pass") is True
    except Exception:
        ok = False
    if not ok:
        reasons.append("check.py did not pass" if err is None else f"score.json unreadable ({err})")
    for name in ("op", "reopen"):
        text, err = read(run / name / "exit_code.txt")
        if err:
            reasons.append(f"{name} exit code unreadable ({err})")
        elif text.strip() != "0":
            reasons.append(f"{name} exit code not 0")
        text, err = read(run / name / "stdout.log")
        if err:
            reasons.append(f"{name} stdout unreadable ({err})")
        elif LINE not in text:
            reasons.append(f"{name} device line missing")
    print("PASS" if not reasons else "FAIL: " + "; ".join(reasons))
    return 0 if not reasons else 1


if __name__ == "__main__":
    raise SystemExit(main())
