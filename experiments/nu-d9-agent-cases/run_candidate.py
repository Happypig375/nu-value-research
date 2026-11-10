"""Run one D9 direction 4 candidate (protocol docs/nu-d9-agent-cases-2026-11-11.md, section 2).

Usage: run_candidate.py NN E|W ARTIFACTS SCRATCH NUGET [--limit 1800]
  - makes SCRATCH/cand-NN-V with prepare.py (candidate layout) and builds it once (Debug);
  - reads quota, runs `claude -p` in that folder with the fixed flags and a clean environment, reads quota again;
  - copies the final Breakout Mmcc sources to ARTIFACTS/cand-NN-V/final/ and writes run.json with the isolation scan.
The candidate is never shown this file, the oracle or any reference solution.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import time

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
ARCHIVE = REPO / ".artifacts/vulkan-timing-20261103/nu-47ef39e.tar"
QUOTA = "/home/happypig375/workspace/orchestrator/.orchestration/google-auth-supervision-20261109/read_quota.py"
PROJECT = "Projects/Breakout Mmcc"
HOME = os.environ["HOME"]
DOTNET = f"{HOME}/.dotnet"
RESTRICTED = [str(REPO), f"{HOME}/workspace", f"{HOME}/.claude"]
FLAGS = ["--model", "claude-opus-5-5", "--effort", "medium", "--setting-sources", "project,local",
         "--tools", "Bash,Read,Edit,Write,Glob,Grep", "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
         "--dangerously-skip-permissions", "--output-format", "stream-json", "--verbose", "--no-session-persistence"]


def quota():
    r = subprocess.run(["python3", "-I", QUOTA, "--main"], capture_output=True, text=True, timeout=60)
    try:
        return json.loads(r.stdout.strip().splitlines()[-1])
    except Exception:
        return {"status": "unreadable", "stdout_tail": r.stdout[-300:], "stderr_tail": r.stderr[-300:]}


def sources(project):
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(project.iterdir())
            if p.is_file() and p.suffix in (".fs", ".fsproj", ".fsx")}


def isolation(stream, cand, allowed, scratch):
    """List every path a tool call names; flag those outside the candidate folder and the allowed prefixes."""
    flags, calls = [], 0
    for line in stream.read_text().splitlines():
        try:
            rec = json.loads(line)
        except ValueError:
            continue
        if rec.get("type") != "assistant":
            continue
        for block in rec.get("message", {}).get("content", []):
            if block.get("type") != "tool_use":
                continue
            calls += 1
            inp = block.get("input", {})
            texts = [str(inp.get(k)) for k in ("file_path", "path", "notebook_path") if inp.get(k)]
            if block.get("name") == "Bash":
                texts += re.findall(r"(?:^|(?<=[\s'\"=:<>|;&(]))((?:~|\$HOME|/)[^\s'\"|;&<>()]*)", inp.get("command", ""))
            for t in texts:
                if t.startswith(("~", "$HOME")):
                    flags.append({"tool": block.get("name"), "path": t})
                    continue
                if not t.startswith("/") or t == "/":
                    continue
                if t.startswith(str(cand)) or t.startswith(allowed[1]):
                    continue
                if t.startswith(str(scratch)) or any(t.startswith(r) for r in RESTRICTED):
                    flags.append({"tool": block.get("name"), "path": t})
                    continue
                if any(t.startswith(p) for p in allowed):
                    continue
                flags.append({"tool": block.get("name"), "path": t})
    return calls, flags


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("nn")
    ap.add_argument("variant", choices=("E", "W"))
    ap.add_argument("artifacts", type=Path)
    ap.add_argument("scratch", type=Path)
    ap.add_argument("nuget", type=Path)
    ap.add_argument("--limit", type=int, default=1800)
    a = ap.parse_args()
    name = f"cand-{a.nn}-{a.variant}"
    cand, out = (a.scratch / name).resolve(), (a.artifacts / name).resolve()
    out.mkdir(parents=True, exist_ok=False)
    env = {"HOME": HOME, "USER": os.environ.get("USER", ""), "LANG": "C.UTF-8", "TERM": "dumb",
           "PATH": f"{DOTNET}:{HOME}/.local/bin:/usr/local/bin:/usr/bin:/bin", "DOTNET_ROOT": DOTNET, "NUGET_PACKAGES": str(a.nuget),
           "DOTNET_CLI_TELEMETRY_OPTOUT": "1", "DOTNET_NOLOGO": "1", "DOTNET_MULTILEVEL_LOOKUP": "0",
           "MSBUILDDISABLENODEREUSE": "1", "DOTNET_CLI_USE_MSBUILD_SERVER": "0"}
    run = {"name": name, "variant": a.variant, "flags": FLAGS, "limit_seconds": a.limit}
    prep = subprocess.run(["python3", "-I", str(HERE / "prepare.py"), "tree", str(ARCHIVE), str(cand),
                           "--variant", a.variant, "--candidate"], capture_output=True, text=True, check=True)
    run["prepare"] = json.loads(prep.stdout)
    with (out / "prebuild.log").open("w") as fh:
        b = subprocess.run(["nice", "-n", "10", "dotnet", "build", f"{cand}/{PROJECT}/Breakout Mmcc.fsproj"],
                           cwd=cand, env=env, stdout=fh, stderr=subprocess.STDOUT)
    run["prebuild_exit"] = b.returncode
    if b.returncode != 0:
        raise SystemExit("prebuild failed")
    shutil.rmtree(out / "start", ignore_errors=True)
    shutil.copytree(cand / PROJECT, out / "start", ignore=shutil.ignore_patterns("bin", "obj", "Assets"))
    run["start_sources"] = sources(cand / PROJECT)
    run["quota_before"] = quota()
    task = (cand / "TASK.md").read_text()
    t0 = time.monotonic()
    with (out / "stream.jsonl").open("w") as so, (out / "stderr.log").open("w") as se:
        p = subprocess.Popen(["claude", "-p", task, *FLAGS], cwd=cand, env=env, stdout=so, stderr=se,
                             start_new_session=True)
        try:
            run["exit_code"] = p.wait(a.limit)
            run["stopped_at_limit"] = False
        except subprocess.TimeoutExpired:
            os.killpg(p.pid, 15)
            run["exit_code"] = p.wait(30)
            run["stopped_at_limit"] = True
    run["wall_seconds"] = round(time.monotonic() - t0, 1)
    run["quota_after"] = quota()
    shutil.copytree(cand / PROJECT, out / "final", ignore=shutil.ignore_patterns("bin", "obj", "Assets"))
    run["final_sources"] = sources(cand / PROJECT)
    run["changed"] = sorted(k for k in set(run["start_sources"]) | set(run["final_sources"])
                            if run["start_sources"].get(k) != run["final_sources"].get(k))
    result = None
    for line in (out / "stream.jsonl").read_text().splitlines():
        try:
            rec = json.loads(line)
        except ValueError:
            continue
        if rec.get("type") == "result":
            result = rec
    if result:
        run["result"] = {k: result.get(k) for k in ("subtype", "is_error", "num_turns", "duration_ms", "usage", "result")}
    allowed = [DOTNET, str(a.nuget), "/tmp", "/usr", "/bin", "/dev/null", "/proc/cpuinfo"]
    run["tool_calls"], run["isolation_flags"] = isolation(out / "stream.jsonl", cand, allowed, a.scratch.resolve())
    (out / "run.json").write_text(json.dumps(run, indent=2) + "\n")
    print(json.dumps({k: run.get(k) for k in ("name", "exit_code", "wall_seconds", "changed", "tool_calls",
                                                "isolation_flags", "stopped_at_limit")}, indent=2))
    shutil.rmtree(cand)  # regenerable; its sources are saved above, so later candidates cannot see them
    print("quota", run["quota_before"].get("seven_day"), "->", run["quota_after"].get("seven_day"))


if __name__ == "__main__":
    main()
