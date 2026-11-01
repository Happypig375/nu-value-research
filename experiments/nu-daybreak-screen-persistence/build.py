"""Build the probe and the pinned Breakout/Gaia projects into a scratch build tree.

Usage: build.py PREPARED_SOURCE BUILD_DIR
The build directory must be new or empty. Probe sources are copied there so the
package directory stays free of build outputs. Requires DOTNET_ROOT/PATH to
select SDK 10.0.302 (see linux_run.sh for the environment).
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

parser = argparse.ArgumentParser(__doc__)
parser.add_argument("source", type=Path, help="prepared (patched) pinned Nu source tree")
parser.add_argument("build", type=Path, help="new or empty build directory")
args = parser.parse_args()
source, build = args.source.resolve(), args.build.resolve()
if build.exists() and any(build.iterdir()):
    parser.error("build directory must be new or empty")
(build / "probe").mkdir(parents=True)
package = Path(__file__).parent
for name in ("Probe.fs", "Probe.fsproj"):
    shutil.copy2(package / name, build / "probe" / name)
command = ["dotnet", "build", "Probe.fsproj", "-c", "Release",
           f"-p:NuSource={source}",
           "-p:SourceRevisionId=064f7ae92a8506689cd91aff5e6804a375d6ef3d"]
with (build / "build.log").open("w") as log:
    process = subprocess.run(command, cwd=build / "probe", stdout=log, stderr=subprocess.STDOUT)
probe_dll = build / "probe/bin/Release/net10.0/Probe.dll"
game_dll = source / "Projects/Breakout Mmcc/bin/Release/net10.0/Breakout Mmcc.dll"
log_text = (build / "build.log").read_text(errors="replace")
receipt = {
    "command": command,
    "exit_code": process.returncode,
    "warning_lines": sum(1 for line in log_text.splitlines() if ": warning " in line),
    "probe_dll_sha256": hashlib.sha256(probe_dll.read_bytes()).hexdigest() if probe_dll.exists() else None,
    "breakout_dll": str(game_dll),
    "breakout_dll_sha256": hashlib.sha256(game_dll.read_bytes()).hexdigest() if game_dll.exists() else None,
}
(build / "build-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
raise SystemExit(0 if process.returncode == 0 else 1)
