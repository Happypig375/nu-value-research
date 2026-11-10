"""Run the declared D9 recovery-routes series (direction 1).

Unscored feasibility round Z (H, F, C), then 5 scored rounds in rotating order:
  round 1: H F C, round 2: F C H, round 3: C H F, round 4: H F C, round 5: F C H.
Route C runs two processes: C1 (imperative session; the fault ends it) then C2 (fresh process imports the file).
Before each process: wait for an idle GPU (as in experiments/nu-vulkan-r06-recovery-cost/series.py). Each process
runs through scripts/linux_nu_vulkan_env.sh (NVIDIA Vulkan on our own Xvfb, nice -n 10) with a 300 s deadline.
Outcomes are recorded, not acted on: an adverse result does not stop the series. An infrastructure failure
(timeout, launch exception, missing Vulkan device) stops it.
Protocol: docs/nu-d9-recovery-routes-2026-11-10.md.
Usage: series.py PROBE_DLL BREAKOUT_DLL RUNS_DIR [--only Z ...]
"""
import argparse
import importlib.util
import json
import subprocess
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
WRAPPER = REPO / "scripts" / "linux_nu_vulkan_env.sh"
spec = importlib.util.spec_from_file_location("r06series", REPO / "experiments" / "nu-vulkan-r06-recovery-cost" / "series.py")
r06 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r06)
ROUNDS = [("Z", "HFC"), ("1", "HFC"), ("2", "FCH"), ("3", "CHF"), ("4", "HFC"), ("5", "FCH")]


def run_process(probe, breakout, runs, attempt, mode, transfer, log):
    idle = r06.wait_idle(log)
    if not idle["idle"]:
        return {"attempt": attempt, "mode": mode, "outcome": "not-run: GPU not idle", "gpu_before": idle}
    out = runs / attempt
    command = ["bash", str(WRAPPER), str(runs), attempt, "--", "dotnet", str(probe), mode, str(breakout), str(transfer), str(out)]
    t0 = time.time()
    with (runs / f"{attempt}.stdout.log").open("wb") as so, (runs / f"{attempt}.stderr.log").open("wb") as se:
        p = subprocess.Popen(command, stdout=so, stderr=se, start_new_session=True)
        try:
            code, timed_out = p.wait(timeout=300), False
        except subprocess.TimeoutExpired:
            subprocess.run(["kill", "-KILL", "--", f"-{p.pid}"])
            code, timed_out = p.wait(15), True
    stdout = (runs / f"{attempt}.stdout.log").read_text(errors="replace")
    return {"attempt": attempt, "mode": mode, "exit_code": code, "timed_out": timed_out,
            "start_utc_ms": int(t0 * 1000), "end_utc_ms": int(time.time() * 1000),
            "vulkan_device_logged": "Selected Vulkan Device NVIDIA GeForce RTX 4090 D" in stdout,
            "gpu_before": idle, "loadavg_before": Path("/proc/loadavg").read_text().strip()}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("probe", type=Path)
    ap.add_argument("breakout", type=Path)
    ap.add_argument("runs", type=Path)
    ap.add_argument("--only", nargs="*")
    a = ap.parse_args()
    runs = a.runs.resolve()
    runs.mkdir(parents=True, exist_ok=True)
    ledger = runs / "series-ledger.jsonl"

    def log(m):
        print(f"{time.strftime('%H:%M:%S')} {m}", flush=True)

    for rnd, order in ROUNDS:
        if a.only and rnd not in a.only:
            continue
        for route in order:
            base = f"{rnd}-{route}"
            if (runs / base).exists() or (runs / f"{base}1").exists():
                log(f"{base} exists; skipping (never overwrite an attempt)")
                continue
            transfer = runs / f"{base}-transfer"
            modes = [("C1", f"{base}1"), ("C2", f"{base}2")] if route == "C" else [(route, base)]
            for mode, attempt in modes:
                rec = run_process(a.probe.resolve(), a.breakout.resolve(), runs, attempt, mode, transfer, log)
                rec["round"], rec["route"] = rnd, route
                ledger.open("a").write(json.dumps(rec) + "\n")
                log(f"{attempt} ({mode}): exit {rec.get('exit_code')} timed_out={rec.get('timed_out')} vulkan={rec.get('vulkan_device_logged')}")
                infra = rec.get("timed_out") or rec.get("exit_code") == 3 or not rec.get("vulkan_device_logged", False)
                if infra:
                    log("infrastructure failure: stopping the series (protocol)")
                    return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
