"""Run the declared keyboard-timing series: one unscored feasibility repeat (KF), then 10 repeats (K01..K10).
Each repeat is a fresh standalone game process.

Before each repeat: wait until the GPU is idle (as in the R06 series). Each repeat runs keyboard_timing.py through
scripts/linux_nu_vulkan_env.sh (NVIDIA Vulkan on our own Xvfb, nice -n 10; load, memory, nvidia-smi logged).
Protocol: docs/nu-vulkan-timing-reference-2026-11-03.md, part 2.
Usage: series.py GAME_DLL_DIR RUNS_DIR [--only K01 ...]
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


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("game_dir", type=Path)
    ap.add_argument("runs", type=Path)
    ap.add_argument("--only", nargs="*")
    a = ap.parse_args()
    runs = a.runs.resolve()
    runs.mkdir(parents=True, exist_ok=True)
    ledger = runs / "series-ledger.jsonl"
    for rid in ["KF"] + [f"K{k:02d}" for k in range(1, 11)]:
        if a.only and rid not in a.only:
            continue
        out = runs / rid
        if out.exists():
            print(f"{rid} exists; skipping (never overwrite an attempt)")
            continue
        idle = r06.wait_idle(lambda m: print(m, flush=True))
        record = {"attempt": rid, "gpu_before": idle, "loadavg_before": Path("/proc/loadavg").read_text().strip(),
                  "started": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
        if not idle["idle"]:
            record["outcome"] = "not-run: GPU not idle within 30 min"
            ledger.open("a").write(json.dumps(record) + "\n")
            return 3
        command = ["bash", str(WRAPPER), str(runs), rid, "--", str(REPO / ".venv" / "bin" / "python"), "-I",
                   str(HERE / "keyboard_timing.py"), str(a.game_dir.resolve()), str(out)]
        t0 = time.monotonic()
        with (runs / f"{rid}.console.log").open("wb") as so:
            code = subprocess.run(command, stdout=so, stderr=subprocess.STDOUT, timeout=700).returncode
        record.update({"exit_code": code, "elapsed_seconds": round(time.monotonic() - t0, 1)})
        res = out / "result.json"
        record["outcome"] = {0: "pass", 1: "fail", 2: "invalid"}.get(code, f"exit {code}")
        record["validity"] = json.loads(res.read_text())["validity"] if res.exists() else None
        ledger.open("a").write(json.dumps(record) + "\n")
        print(f"{rid}: {record['outcome']} in {record['elapsed_seconds']} s", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
