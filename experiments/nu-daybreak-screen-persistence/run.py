"""Run one screen-persistence arm with a process deadline and preserve its receipt and logs."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time


def main():
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("mode", choices=("export", "import", "replace-nodestroy"))
    parser.add_argument("project_dll", type=Path)
    parser.add_argument("reference", type=Path, help="B0 reference checkpoint directory (gameplay.symbol, projection.json)")
    parser.add_argument("transfer", type=Path, help="transfer directory holding gameplay-screen.nuscreen")
    parser.add_argument("output", type=Path)
    parser.add_argument("--timeout", type=float, default=600)
    parser.add_argument("--probe", type=Path, default=Path(__file__).parent / "bin/Release/net10.0/Probe.dll")
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("timeout must be positive")
    probe, project = args.probe.resolve(strict=True), args.project_dll.resolve(strict=True)
    reference = args.reference.resolve(strict=True)
    output, transfer = args.output.resolve(), args.transfer.resolve()
    if args.mode == "export" and transfer.exists() and any(transfer.iterdir()):
        parser.error("export transfer directory must be new or empty")
    if args.mode != "export" and not (transfer / "gameplay-screen.nuscreen").exists():
        parser.error("import transfer file is missing")
    output.mkdir(parents=True, exist_ok=False)
    command = ["dotnet", str(probe), args.mode, str(project), str(reference), str(transfer), str(output / "probe")]
    receipt = {
        "command": command,
        "timeout_seconds": args.timeout,
        "probe_sha256": hashlib.sha256(probe.read_bytes()).hexdigest(),
        "application_sha256": hashlib.sha256(project.read_bytes()).hexdigest(),
        "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "timed_out": False,
    }
    start = time.monotonic()
    with (output / "stdout.log").open("wb") as stdout, (output / "stderr.log").open("wb") as stderr:
        try:
            process = subprocess.Popen(command, stdout=stdout, stderr=stderr,
                                       creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0)
            receipt["pid"] = process.pid
            try:
                receipt["exit_code"] = process.wait(timeout=args.timeout)
            except subprocess.TimeoutExpired:
                receipt["timed_out"] = True
                if os.name == "nt":
                    cleanup = subprocess.run(["taskkill", "/PID", str(process.pid), "/T", "/F"],
                                             capture_output=True, text=True, timeout=15)
                    receipt["deadline_cleanup_exit"] = cleanup.returncode
                else:
                    process.kill()
                receipt["exit_code"] = process.wait(timeout=15)
        except Exception as error:
            receipt["driver_error"] = repr(error)
    receipt["elapsed_seconds"] = time.monotonic() - start
    (output / "process.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    return 0 if receipt.get("exit_code") == 0 and not receipt["timed_out"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
