"""Run the declared D9 direction-2 series (live editing with a schema change), amendment 4.

Feasibility round F4 (unscored): L-A, M-A, R-A. Then 3 scored repeats; within each repeat the 9 route x case runs in
rotating order (routes L M R, M R L, R L M; cases A Z N within each route). Before every L/M run the scratch
Gameplay.fs is restored from the pinned tar (the probe applies the schema edit itself). R runs two processes:
R1 (old code) saves the seeded model, R2 (fresh process, new code) reconstructs it. Idle-GPU rule as in direction 1
(amendment 1 there). Vulkan wrapper, nice -n 10, 300 s deadline per process. Outcomes do not stop the series;
infrastructure failures (timeout, launch exception, missing Vulkan line) do.
Protocol: docs/nu-d9-directions-2-4-packets-2026-11-10.md, direction 2 and amendments 1-4.
Usage: series.py SCRATCH RUNS [--only F4 1 2 3]
"""
import argparse
import importlib.util
import json
import subprocess
import tarfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
WRAPPER = REPO / "scripts" / "linux_nu_vulkan_env.sh"
TAR = REPO / ".artifacts/vulkan-timing-20261103/nu-47ef39e.tar"
SEED = REPO / "experiments/nu-history-b1/checkpoint/gameplay.symbol"
spec = importlib.util.spec_from_file_location("d1series", REPO / "experiments" / "nu-d9-recovery-routes" / "series.py")
d1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d1)
ROTATIONS = ["LMR", "MRL", "RLM"]


def restore_gameplay(scratch):
    with tarfile.open(TAR) as t:
        data = t.extractfile("Projects/Breakout Mmcc/Gameplay.fs").read()
    (scratch / "src2/Projects/Breakout Mmcc/Gameplay.fs").write_bytes(data)


def run(scratch, runs, attempt, args, log):
    idle = d1.wait_idle(log)
    if not idle["idle"]:
        return {"attempt": attempt, "outcome": "not-run: GPU not idle", "gpu_before": idle}
    out = runs / attempt
    probe_pkg = "pkg3" if args[0] == "R2" else "pkg2"
    command = ["bash", str(WRAPPER), str(runs), attempt, "--", "dotnet", str(scratch / probe_pkg / "bin/Release/net10.0/Probe.dll")] + args + [str(SEED), str(out)]
    t0 = time.time()
    with (runs / f"{attempt}.stdout.log").open("wb") as so:
        p = subprocess.Popen(command, stdout=so, stderr=subprocess.STDOUT, start_new_session=True)
        try:
            code, timed_out = p.wait(timeout=300), False
        except subprocess.TimeoutExpired:
            subprocess.run(["kill", "-KILL", "--", f"-{p.pid}"])
            code, timed_out = p.wait(15), True
    text = (runs / f"{attempt}.stdout.log").read_text(errors="replace")
    return {"attempt": attempt, "args": args[:2], "exit_code": code, "timed_out": timed_out,
            "start_utc_ms": int(t0 * 1000), "end_utc_ms": int(time.time() * 1000), "gpu_before": idle,
            "vulkan_device_logged": "Selected Vulkan Device NVIDIA GeForce RTX 4090 D" in text}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("scratch", type=Path)
    ap.add_argument("runs", type=Path)
    ap.add_argument("--only", nargs="*")
    a = ap.parse_args()
    scratch, runs = a.scratch.resolve(), a.runs.resolve()
    runs.mkdir(parents=True, exist_ok=True)
    ledger = runs / "series-ledger.jsonl"
    log = lambda m: print(f"{time.strftime('%H:%M:%S')} {m}", flush=True)
    plan = [("F4", r, "A") for r in "LMR"]
    for rep in "123":
        for r in ROTATIONS[int(rep) - 1]:
            for c in "AZN":
                plan.append((rep, r, c))
    for rnd, route, case in plan:
        if a.only and rnd not in a.only:
            continue
        base = f"{rnd}-{route}-{case}"
        if any((runs / n).exists() for n in (base, base + "-R1")):
            log(f"{base} exists; skipping")
            continue
        if route == "R":
            transfer = runs / f"{base}-transfer"
            steps = [(base + "-R1", ["R1", case, str(scratch / "src2/Projects/Breakout Mmcc/bin/Release/net10.0/Breakout Mmcc.dll"), str(transfer)]),
                     (base + "-R2", ["R2", case, str(scratch / "src3/Projects/Breakout Mmcc/bin/Release/net10.0/Breakout Mmcc.dll"), str(transfer)])]
        else:
            restore_gameplay(scratch)
            steps = [(base, [route, case, str(scratch / "src2/Projects/Breakout Mmcc/bin/Release/net10.0/Breakout Mmcc.dll"),
                             str(scratch / "src2/Projects/Breakout Mmcc/Gameplay.fs")])]
        for attempt, args in steps:
            rec = run(scratch, runs, attempt, args, log)
            rec.update({"round": rnd, "route": route, "case": case})
            ledger.open("a").write(json.dumps(rec) + "\n")
            log(f"{attempt}: exit {rec.get('exit_code')} timeout={rec.get('timed_out')} vulkan={rec.get('vulkan_device_logged')}")
            if rec.get("timed_out") or rec.get("exit_code") == 3 or not rec.get("vulkan_device_logged", False):
                log("infrastructure failure: stopping (protocol)")
                return 1
    restore_gameplay(scratch)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
