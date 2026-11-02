"""Build the unchanged standalone MMCC Breakout game. Usage: build.py PREPARED_SOURCE

Requires DOTNET_ROOT/PATH for SDK 10.0.302 and NUGET_PACKAGES pointing at a
private copy of .artifacts/nuget-packages (see the protocol).
"""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("source", type=Path)
args = parser.parse_args()
source = args.source.resolve(strict=True)
project = source / "Projects/Breakout Mmcc/Breakout Mmcc.fsproj"
command = ["dotnet", "build", str(project), "-c", "Release"]
log_path = source.parent / "build.log"
with log_path.open("w") as log:
    process = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT)
dll = source / "Projects/Breakout Mmcc/bin/Release/net10.0/Breakout Mmcc.dll"
text = log_path.read_text(errors="replace")
receipt = {
    "command": command,
    "exit_code": process.returncode,
    "warning_lines": sum(1 for line in text.splitlines() if ": warning " in line),
    "error_lines": sum(1 for line in text.splitlines() if ": error " in line),
    "dll": str(dll),
    "dll_sha256": hashlib.sha256(dll.read_bytes()).hexdigest() if dll.exists() else None,
}
(source.parent / "build-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt, indent=2))
raise SystemExit(0 if process.returncode == 0 and dll.exists() else 1)
