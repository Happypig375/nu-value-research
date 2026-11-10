"""Run D9 history-sequence rounds (protocol docs/nu-d9-history-sequence-2026-11-11.md, section 6).
Usage: series.py APP_DIR OUT_DIR ROUND [ROUND ...]   ROUND is F, 1, 2 or 3. Run under scripts/linux_nu_vulkan_env.sh.
Each sequence run: op process, then fresh reopen processes for saved1 (not for N) and saved2, then check.py."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROUNDS = {"F": ["N", "PP", "HP", "HH"], "1": ["N", "PP", "HP", "HH"], "2": ["N", "HP", "HH", "PP"], "3": ["N", "HH", "PP", "HP"]}
DEADLINE = 300


def gpu_idle(log):
    start = time.monotonic()
    while time.monotonic() - start < 900:
        gaia = subprocess.run(["pgrep", "-af", "[N]u\\.Gaia\\.dll"], capture_output=True, text=True).stdout.strip()
        u = []
        for _ in range(2):
            r = subprocess.run(["nvidia-smi", "--query-gpu=utilization.gpu", "--format=csv,noheader,nounits"], capture_output=True, text=True)
            u.append(int(r.stdout.strip() or 100))
            time.sleep(2)
        apps = subprocess.run(["nvidia-smi", "--query-compute-apps=pid,process_name", "--format=csv,noheader"], capture_output=True, text=True).stdout.strip()
        if not gaia and max(u) < 10:
            log({"event": "gpu-idle", "util": u, "apps": apps})
            return True
        time.sleep(10)
    log({"event": "gpu-never-idle"})
    return False


def process(app, folder, env, name):
    folder.mkdir(parents=True, exist_ok=True)
    t0 = time.monotonic()
    with (folder / f"{name}.stdout.log").open("wb") as so, (folder / f"{name}.stderr.log").open("wb") as se:
        p = subprocess.Popen(["dotnet", str(app / "Terra Firma.dll")], cwd=app, env=env, stdout=so, stderr=se)
        try:
            code = p.wait(DEADLINE)
        except subprocess.TimeoutExpired:
            p.kill(); p.wait(30); code = "timeout"
    (folder / f"{name}.exit_code.txt").write_text(str(code))
    return code, round(time.monotonic() - t0, 2)


def main():
    app, out = Path(sys.argv[1]).resolve(strict=True), Path(sys.argv[2]).resolve()
    out.mkdir(parents=True, exist_ok=True)
    ledger = (out / "ledger.jsonl").open("a")

    def log(rec):
        rec["utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        ledger.write(json.dumps(rec) + "\n"); ledger.flush(); print(json.dumps(rec), flush=True)

    for rnd in sys.argv[3:]:
        for seq in ROUNDS[rnd]:
            run = out / f"round-{rnd}" / seq
            if not gpu_idle(log):
                return 3
            code, wall = process(app, run, dict(os.environ, PROBE_MODE="op", PROBE_SEQ=seq, PROBE_IN="Assets/Gameplay/Scene.nugroup", PROBE_OUT=str(run)), "op")
            log({"event": "op", "round": rnd, "seq": seq, "exit": code, "wall_s": wall})
            if code != 0:
                log({"event": "stop", "reason": f"op failed ({code})"}); return 2
            for tag in (["reopen2"] if seq == "N" else ["reopen1", "reopen2"]):
                saved = run / ("saved1.nugroup" if tag == "reopen1" else "saved2.nugroup")
                code, wall = process(app, run, dict(os.environ, PROBE_MODE="reopen", PROBE_SEQ=seq, PROBE_IN=str(saved), PROBE_OUT=str(run), PROBE_TAG=tag), tag)
                log({"event": tag, "round": rnd, "seq": seq, "exit": code, "wall_s": wall})
                if code != 0:
                    log({"event": "stop", "reason": f"{tag} failed ({code})"}); return 2
            r = subprocess.run(["python3", "-I", str(HERE / "check.py"), str(run)], capture_output=True, text=True)
            log({"event": "score", "round": rnd, "seq": seq, "summary": r.stdout.strip()[-1200:], "stderr": r.stderr[-400:]})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
