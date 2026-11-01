"""Summarize screen-persistence run receipts into one comparison JSON.

Usage: compare.py RUNS_ROOT
Reads every run-*/probe/trace.jsonl and run-*/process.json under RUNS_ROOT and
checks the protocol's cross-arm conditions: each arm's declared result, the
transfer file hash agreement between export and import arms, and the export
inspection fields. Prints and writes comparison.json under RUNS_ROOT.
"""
import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser(__doc__)
parser.add_argument("runs", type=Path)
args = parser.parse_args()
runs = args.runs.resolve()


def read_trace(trace_path):
    records = []
    with trace_path.open() as handle:
        for line in handle:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


arms = {}
for process_path in sorted(runs.glob("run-*/process.json")):
    run_dir = process_path.parent
    process = json.loads(process_path.read_text())
    trace_path = run_dir / "probe/trace.jsonl"
    entry = {"run": run_dir.name, "exit_code": process.get("exit_code"),
             "timed_out": process.get("timed_out"),
             "elapsed_seconds": process.get("elapsed_seconds")}
    if trace_path.exists():
        records = read_trace(trace_path)
        by_event = {}
        for record in records:
            by_event.setdefault(record.get("event"), []).append(record)
        entry["events"] = sorted(by_event)
        result = by_event.get("result", [{}])[-1]
        entry["result"] = result
        for event in ("export-inspection", "diagnostic", "import-groups", "negative-controls", "exception"):
            if event in by_event:
                entry[event] = by_event[event][-1]
    arms[run_dir.name] = entry

export_runs = {name: e for name, e in arms.items() if name.startswith("run-export-") and e.get("result", {}).get("pass")}
import_runs = {name: e for name, e in arms.items() if name.startswith("run-import-") and e.get("result", {}).get("pass")}
summary = {
    "runs": arms,
    "export_pass": bool(export_runs),
    "import_pass": bool(import_runs),
    "transfer_hash_agreement": None,
    "export_inspection": None,
    "diagnostic": None,
}
if export_runs:
    inspection = next(iter(export_runs.values())).get("export-inspection")
    summary["export_inspection"] = inspection
    if inspection and import_runs:
        transfer = runs / "transfer/gameplay-screen.nuscreen"
        if transfer.exists():
            import hashlib
            current = hashlib.sha256(transfer.read_bytes()).hexdigest()
            summary["transfer_hash_agreement"] = current == inspection.get("fileSha256")
diagnostics = [e.get("diagnostic") for name, e in arms.items()
               if name.startswith("run-replace-nodestroy-") and e.get("diagnostic")]
if diagnostics:
    summary["diagnostic"] = diagnostics[-1]

out = runs / "comparison.json"
out.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
print(json.dumps(summary, indent=2))
