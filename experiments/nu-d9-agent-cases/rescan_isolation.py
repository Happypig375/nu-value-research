"""Re-run run_candidate.py's isolation scan on a saved candidate (after the scanner's regex fix of 11 Nov 2026)."""
import importlib.util
import json
from pathlib import Path
import sys

spec = importlib.util.spec_from_file_location("rc", Path(__file__).resolve().parent / "run_candidate.py")
rc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rc)
out, scratch, nuget = (Path(p) for p in sys.argv[1:4])
run = json.loads((out / "run.json").read_text())
cand = scratch.resolve() / run["name"]
allowed = [rc.DOTNET, str(nuget), "/tmp", "/usr", "/bin", "/dev/null", "/proc/cpuinfo"]
calls, flags = rc.isolation(out / "stream.jsonl", cand, allowed, scratch.resolve())
run["isolation_flags_v1"] = run.pop("isolation_flags")
run["tool_calls"], run["isolation_flags"] = calls, flags
(out / "run.json").write_text(json.dumps(run, indent=2) + "\n")
print(json.dumps({"name": run["name"], "tool_calls": calls, "isolation_flags": flags}))
