"""Run a D9 direction 3 round list (protocol docs/nu-d9-content-revision-2026-11-11.md, section 5).

Usage: series.py APP_DIR OUT_DIR ROUND [ROUND ...]   ROUND is F, 1, 2 or 3.
Each run: an op process then a fresh reopen process (TerraProbe), then check.py. Run under
scripts/linux_nu_vulkan_env.sh (DISPLAY, XAUTHORITY and the NVIDIA Vulkan driver).
"""
import json
import os
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROUNDS = {
    "F": ["N", "T1-P", "T1-O", "T2-P", "T2-O", "T3-P", "T3-O"],
    "1": ["N", "T1-P", "T1-O", "T2-P", "T2-O", "T3-P", "T3-O"],
    "2": ["N", "T2-O", "T2-P", "T3-O", "T3-P", "T1-O", "T1-P"],
    "3": ["N", "T3-P", "T3-O", "T1-P", "T1-O", "T2-P", "T2-O"],
}
DEADLINE = 300


def gpu_idle(log):
    """Direction 1 amendment 1 idle rule, plus no Gaia from any project (Nu-Gaia holds the GPU while it runs one)."""
    start = time.monotonic()
    while time.monotonic() - start < 1800:
        gaia = subprocess.run(["pgrep", "-af", "[N]u\\.Gaia\\.dll"], capture_output=True, text=True).stdout.strip()
        u = []
        for _ in range(2):
            r = subprocess.run(["nvidia-smi", "--query-gpu=utilization.gpu", "--format=csv,noheader,nounits"],
                               capture_output=True, text=True)
            u.append(int(r.stdout.strip() or 100))
            time.sleep(2)
        apps = subprocess.run(["nvidia-smi", "--query-compute-apps=pid,process_name,used_memory", "--format=csv,noheader"],
                              capture_output=True, text=True).stdout.strip()
        if not gaia and max(u) < 10:
            log({"event": "gpu-idle", "util": u, "apps": apps, "waited_s": round(time.monotonic() - start, 1)})
            return True
        time.sleep(10)
    log({"event": "gpu-never-idle"})
    return False


def process(app, folder, env):
    folder.mkdir(parents=True)
    t0 = time.monotonic()
    with (folder / "stdout.log").open("wb") as so, (folder / "stderr.log").open("wb") as se:
        p = subprocess.Popen(["dotnet", str(app / "Terra Firma.dll")], cwd=app, env=env, stdout=so, stderr=se)
        try:
            code = p.wait(DEADLINE)
        except subprocess.TimeoutExpired:
            p.kill()
            p.wait(30)
            code = "timeout"
    (folder / "exit_code.txt").write_text(str(code))
    return code, round(time.monotonic() - t0, 2)


def main():
    app, out = Path(sys.argv[1]).resolve(strict=True), Path(sys.argv[2]).resolve()
    out.mkdir(parents=True, exist_ok=True)
    ledger = (out / "ledger.jsonl").open("a")

    def log(rec):
        rec["utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        ledger.write(json.dumps(rec) + "\n")
        ledger.flush()
        print(json.dumps(rec), flush=True)

    for rnd in sys.argv[3:]:
        for label in ROUNDS[rnd]:
            task, cond = ("NONE", "N") if label == "N" else label.split("-")
            run = out / f"round-{rnd}" / label
            if not gpu_idle(log):
                return 3
            env = dict(os.environ, PROBE_MODE="op", PROBE_TASK=task, PROBE_COND=cond,
                       PROBE_IN="Assets/Gameplay/Scene.nugroup", PROBE_OUT=str(run / "op"))
            code, wall = process(app, run / "op", env)
            log({"event": "op", "round": rnd, "run": label, "exit": code, "wall_s": wall})
            if code != 0 or not (run / "op" / "saved.nugroup").exists():
                log({"event": "stop", "reason": f"op process failed ({code})", "run": label})
                return 2
            env = dict(os.environ, PROBE_MODE="reopen", PROBE_TASK=task, PROBE_COND=cond,
                       PROBE_IN=str(run / "op" / "saved.nugroup"), PROBE_OUT=str(run / "reopen"))
            code, wall = process(app, run / "reopen", env)
            log({"event": "reopen", "round": rnd, "run": label, "exit": code, "wall_s": wall})
            if code != 0:
                log({"event": "stop", "reason": f"reopen process failed ({code})", "run": label})
                return 2
            r = subprocess.run(["python3", "-I", str(HERE / "check.py"), str(run)], capture_output=True, text=True)
            log({"event": "score", "round": rnd, "run": label, "summary": r.stdout.strip()[-1500:], "stderr": r.stderr[-500:]})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
