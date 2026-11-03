"""Run the declared R06 Vulkan-era series: 1 unscored feasibility process per route, then 20 measured pairs.

Order (alternating, balanced): F-H, F-R, then H R R H H R R H ... (20 pairs, 40 processes).
Before each process: wait until the GPU is idle (no process on it other than root's Xorg, utilization < 10 %),
polling every 15 s for up to 30 min; record the wait. Each process runs through scripts/linux_nu_vulkan_env.sh
(NVIDIA Vulkan on our own Xvfb, nice -n 10; logs load, memory and nvidia-smi samples), with a 600 s deadline.
A measured process that fails stops the series (protocol: investigate before continuing; amendment needed).
Protocol: docs/nu-vulkan-timing-reference-2026-11-03.md, part 1.
Usage: series.py PROBE_DLL BREAKOUT_DLL CHECKPOINT_DIR RUNS_DIR [--only ID ...]
"""
import argparse
import json
import re
import subprocess
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WRAPPER = REPO / "scripts" / "linux_nu_vulkan_env.sh"


def plan():
    attempts = [("F-H", "H", "feasibility"), ("F-R", "R", "feasibility")]
    for p in range(1, 21):
        first, second = ("H", "R") if p % 2 == 1 else ("R", "H")
        attempts.append((f"{first}{p:02d}", first, "measured"))
        attempts.append((f"{second}{p:02d}", second, "measured"))
    return attempts


def gpu_state():
    util = subprocess.run(["nvidia-smi", "--query-gpu=utilization.gpu,memory.used", "--format=csv,noheader,nounits"],
                          capture_output=True, text=True).stdout.strip()
    table = subprocess.run(["nvidia-smi"], capture_output=True, text=True).stdout
    procs = [line for line in table.splitlines() if re.match(r"^\|\s+\d+\s+N/A", line)]
    foreign = [line for line in procs if "/usr/lib/xorg/Xorg" not in line]
    u = int(util.split(",")[0]) if util else 100
    return {"utilization": u, "memory_used_mib": util.split(",")[1].strip() if util else None,
            "foreign_processes": [" ".join(line.split()) for line in foreign]}


def wait_idle(log):
    start = time.monotonic()
    polls = 0
    while True:
        state = gpu_state()
        polls += 1
        if state["utilization"] < 10 and not state["foreign_processes"]:
            return {"idle": True, "waited_seconds": round(time.monotonic() - start, 1), "polls": polls, "state": state}
        if time.monotonic() - start > 1800:
            return {"idle": False, "waited_seconds": round(time.monotonic() - start, 1), "polls": polls, "state": state}
        log(f"GPU busy ({state}); waiting 15 s")
        time.sleep(15)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("probe", type=Path)
    ap.add_argument("breakout", type=Path)
    ap.add_argument("checkpoint", type=Path)
    ap.add_argument("runs", type=Path)
    ap.add_argument("--only", nargs="*", help="run only these attempt ids (e.g. F-H F-R)")
    a = ap.parse_args()
    runs = a.runs.resolve()
    runs.mkdir(parents=True, exist_ok=True)
    ledger = runs / "series-ledger.jsonl"

    def log(msg):
        print(f"{time.strftime('%H:%M:%S')} {msg}", flush=True)

    for attempt_id, route, kind in plan():
        if a.only and attempt_id not in a.only:
            continue
        out = runs / attempt_id
        if out.exists():
            log(f"{attempt_id} already exists; skipping (never overwrite an attempt)")
            continue
        idle = wait_idle(log)
        record = {"attempt": attempt_id, "route": route, "kind": kind, "gpu_before": idle,
                  "loadavg_before": Path("/proc/loadavg").read_text().strip(),
                  "started": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
        if not idle["idle"]:
            record["outcome"] = "not-run: GPU not idle within 30 min"
            ledger.open("a").write(json.dumps(record) + "\n")
            log(f"{attempt_id}: GPU never idle; stopping")
            return 3
        command = ["bash", str(WRAPPER), str(runs), attempt_id, "--", "dotnet", str(a.probe.resolve()),
                   route, kind, attempt_id, str(a.breakout.resolve()), str(a.checkpoint.resolve()), str(out)]
        t0 = time.monotonic()
        with (runs / f"{attempt_id}.stdout.log").open("wb") as so, (runs / f"{attempt_id}.stderr.log").open("wb") as se:
            p = subprocess.Popen(command, stdout=so, stderr=se, start_new_session=True)
            try:
                code = p.wait(timeout=600)
                timed_out = False
            except subprocess.TimeoutExpired:
                subprocess.run(["kill", "-KILL", "--", f"-{p.pid}"])
                code = p.wait(15)
                timed_out = True
        record.update({"exit_code": code, "timed_out": timed_out, "elapsed_seconds": round(time.monotonic() - t0, 3)})
        result = out / "result.json"
        record["result"] = json.loads(result.read_text()) if result.exists() else None
        ok = code == 0 and not timed_out and record["result"] is not None and record["result"].get("pass") is True
        record["outcome"] = "pass" if ok else "fail"
        ledger.open("a").write(json.dumps(record) + "\n")
        log(f"{attempt_id} ({route}, {kind}): {record['outcome']} in {record['elapsed_seconds']} s")
        if not ok and kind == "measured":
            log("measured process failed: stopping the series (protocol)")
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
