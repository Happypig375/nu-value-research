"""Fail-closed wrapper over a scored direction 3 run (D9 offline validation, 10 Nov 2026).

Usage: validate_run.py RUN_DIR   -> prints PASS or FAIL: reasons. PASS only if check.py's score.json says pass AND
both processes' exit_code.txt read 0 AND both stdout logs contain the NVIDIA Vulkan device line. Missing files fail.
The frozen check.py records these facts but leaves them out of its pass; this wrapper does not change check.py.
"""
import json
from pathlib import Path
import sys

LINE = "Selected Vulkan Device NVIDIA GeForce RTX 4090 D"
run = Path(sys.argv[1])
reasons = []
try:
    if json.loads((run / "score.json").read_text()).get("pass") is not True:
        reasons.append("check.py did not pass")
except Exception as e:
    reasons.append(f"score.json unreadable ({type(e).__name__})")
for name in ("op", "reopen"):
    try:
        if (run / name / "exit_code.txt").read_text().strip() != "0":
            reasons.append(f"{name} exit code not 0")
    except FileNotFoundError:
        reasons.append(f"{name} exit code missing")
    try:
        if LINE not in (run / name / "stdout.log").read_text(errors="replace"):
            reasons.append(f"{name} device line missing")
    except FileNotFoundError:
        reasons.append(f"{name} stdout missing")
print("PASS" if not reasons else "FAIL: " + "; ".join(reasons))
