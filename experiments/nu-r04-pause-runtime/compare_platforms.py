"""Compare Linux R04 runs with the published Windows amended runs.

Uses the same fixed-record selection as the original receipt script
(.artifacts/r04-pause-runtime-20261015/amended-probes-01/make_reference_receipt.py):
drop "configuration" and "preseed-cleared-observation" rows; for pause-family arms stop
inclusively at "resumed-after-one". Records are compared as canonical JSON.

Usage: compare_platforms.py WINDOWS_ROOT LINUX_RUNS_ROOT OUTPUT_JSON
WINDOWS_ROOT holds runtime-amended-<arm>-01/; LINUX_RUNS_ROOT holds run-<arm>-NN/ folders
(the highest NN per arm is used, and all attempts are listed).
"""

from __future__ import annotations

import collections
import hashlib
import json
from pathlib import Path
import sys

ARMS = [
    "baseline-explicit", "baseline-wildcard", "pause-explicit", "pause-wildcard",
    "fault-missing-toggle", "fault-hidden-content", "fault-advancing-time",
    "fault-reset-resume", "fault-stale-quit",
]
EXPECTED_GATE = {
    "fault-missing-toggle": "pause-reached",
    "fault-hidden-content": "pause-projection",
    "fault-advancing-time": "pause-frozen-model",
    "fault-reset-resume": "resume-retained",
    "fault-stale-quit": "quit-reset",
}


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha(value: object) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def rows_of(directory: Path) -> list[dict]:
    path = directory / "probe" / "trace.jsonl"
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def fixed(arm: str, rows: list[dict]) -> list[dict]:
    result = []
    for row in rows:
        if row.get("event") not in ("configuration", "preseed-cleared-observation"):
            result.append(row)
        if not arm.startswith("baseline") and row.get("event") == "resumed-after-one":
            break
    return result


def first_difference(left: list[dict], right: list[dict]) -> dict | None:
    for index, (a, b) in enumerate(zip(left, right)):
        if canonical(a) != canonical(b):
            keys = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
            return {"index": index, "event": a.get("event"), "differing_keys": keys[:20]}
    if len(left) != len(right):
        return {"index": min(len(left), len(right)), "length_linux": len(left), "length_windows": len(right)}
    return None


def summary(directory: Path, rows: list[dict]) -> dict:
    process_path = directory / "process.json"
    process = json.loads(process_path.read_text(encoding="utf-8")) if process_path.exists() else {}
    results = [r for r in rows if r.get("event") == "result"]
    exits = [r for r in rows if r.get("event") == "engine-exit"]
    return {
        "folder": directory.name,
        "exit_code": process.get("exit_code"),
        "timed_out": process.get("timed_out"),
        "elapsed_seconds": process.get("elapsed_seconds"),
        "result": results[0] if len(results) == 1 else {"count": len(results)},
        "engine_exit": exits[0] if len(exits) == 1 else {"count": len(exits)},
        "exceptions": sum(1 for r in rows if r.get("event") in ("exception", "launch-exception")),
        "event_counts": dict(collections.Counter(r.get("event") for r in rows)),
    }


def main() -> int:
    windows_root, linux_root, output = (Path(a) for a in sys.argv[1:4])
    report: dict = {"arms": {}, "linux_explicit_vs_wildcard": {}}
    linux_fixed: dict[str, list[dict]] = {}
    for arm in ARMS:
        attempts = sorted(linux_root.glob(f"run-{arm}-[0-9][0-9]"))
        entry: dict = {"linux_attempts": [a.name for a in attempts]}
        if not attempts:
            entry["status"] = "not run"
            report["arms"][arm] = entry
            continue
        linux_dir = attempts[-1]
        windows_dir = windows_root / f"runtime-amended-{arm}-01"
        lin_rows, win_rows = rows_of(linux_dir), rows_of(windows_dir)
        entry["linux"] = summary(linux_dir, lin_rows)
        entry["windows"] = summary(windows_dir, win_rows)
        lf, wf = fixed(arm, lin_rows), fixed(arm, win_rows)
        linux_fixed[arm] = lf
        entry["fixed_records"] = {
            "count_linux": len(lf), "count_windows": len(wf),
            "exact_json_equal": lf == wf,
            "sha256_linux": sha(lf), "sha256_windows": sha(wf),
            "first_difference": first_difference(lf, wf),
        }
        lres = entry["linux"]["result"]
        if arm in EXPECTED_GATE:
            entry["expected_gate"] = EXPECTED_GATE[arm]
            entry["gate_matches_prediction"] = lres.get("pass") is False and lres.get("detail") == EXPECTED_GATE[arm]
        else:
            entry["reference_passed"] = lres.get("pass") is True and entry["linux"]["exit_code"] == 0
        report["arms"][arm] = entry
    for left, right in (("baseline-explicit", "baseline-wildcard"), ("pause-explicit", "pause-wildcard")):
        if left in linux_fixed and right in linux_fixed:
            report["linux_explicit_vs_wildcard"][f"{left} vs {right}"] = {
                "exact_json_equal": linux_fixed[left] == linux_fixed[right],
                "first_difference": first_difference(linux_fixed[left], linux_fixed[right]),
            }
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    for arm, entry in report["arms"].items():
        fr = entry.get("fixed_records", {})
        verdict = entry.get("reference_passed", entry.get("gate_matches_prediction", entry.get("status")))
        print(f"{arm}: verdict={verdict} fixed_equal_windows={fr.get('exact_json_equal')} counts={fr.get('count_linux')}/{fr.get('count_windows')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
