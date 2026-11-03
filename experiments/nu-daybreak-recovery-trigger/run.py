"""Run one arm (a0, a1 or a2) of the branch A recovery-trigger check with a process deadline.

Keeps stdout/stderr, the probe trace and a process receipt in a new output directory.
Protocol: docs/nu-daybreak-recovery-trigger-2026-11-03.md, section 4.
"""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("arm", choices=("a0", "a1", "a2"))
    parser.add_argument("project_dll", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--probe", type=Path, required=True)
    parser.add_argument("--timeout", type=float, default=600)
    args = parser.parse_args()
    probe, project = args.probe.resolve(strict=True), args.project_dll.resolve(strict=True)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    command = ["dotnet", str(probe), args.arm, str(project), str(output / "probe")]
    receipt = {
        "arm": args.arm,
        "command": command,
        "timeout_seconds": args.timeout,
        "probe_sha256": hashlib.sha256(probe.read_bytes()).hexdigest(),
        "application_sha256": hashlib.sha256(project.read_bytes()).hexdigest(),
        "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "timed_out": False,
    }
    start = time.monotonic()
    with (output / "stdout.log").open("wb") as stdout, (output / "stderr.log").open("wb") as stderr:
        process = subprocess.Popen(command, stdout=stdout, stderr=stderr)
        receipt["pid"] = process.pid
        try:
            receipt["exit_code"] = process.wait(timeout=args.timeout)
        except subprocess.TimeoutExpired:
            receipt["timed_out"] = True
            process.kill()
            receipt["exit_code"] = process.wait(timeout=15)
    receipt["elapsed_seconds"] = round(time.monotonic() - start, 3)
    (output / "process.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
