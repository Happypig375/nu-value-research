"""Compare B1 traces from two platforms (read-only; added 2026-11-02 for the Linux reproduction).

For each arm, the seeded-B0 row, the event schedules and all twenty continuation steps must
carry identical models and projections. Values are compared exactly as the probe stores them
(single-precision bit patterns as hex). Absolute engine counters, paths, timing and runtime
identity are excluded, as in the original B1 contract. One in-memory single-bit corruption per
arm must be detected. See docs/nu-r03-linux-reproduction-2026-11-02.md.

Usage: compare_platforms.py WINDOWS_ROOT LINUX_ROOT OUTPUT_JSON
where each root holds history/probe/trace.jsonl and fresh/probe/trace.jsonl (paths given as
--windows-history etc. override the defaults).
"""

import argparse
import copy
import json
from pathlib import Path


def load(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def fixed_records(trace):
    seed = [r for r in trace if r["event"] == "seeded-B0"]
    steps = [r for r in trace if r["event"] == "continuation-step"]
    schedules = [r for r in trace if r["event"] == "event-schedule"]
    final = [r for r in trace if r["event"] == "continuation-next-halted"]
    records = [("seeded-B0", {"model": s["model"], "projection": s["projection"]}) for s in seed]
    records += [(f"schedule-{s['phase']}", {"order": s["order"], "updates": s["updates"],
                                            "timeUpdates": s["timeUpdates"]}) for s in schedules]
    records += [(f"step-{r['step']:02d}", {"model": r["model"], "projection": r["projection"],
                                          "projectionErrors": r["projectionErrors"],
                                          "advancing": r["advancing"]}) for r in steps]
    records += [("next-halted", {"model": f["model"], "projection": f["projection"]}) for f in final]
    return records


def compare(left, right):
    a, b = fixed_records(left), fixed_records(right)
    names = [n for n, _ in a]
    if names != [n for n, _ in b]:
        return {"equal": False, "reason": "record sequence differs", "left": names, "right": [n for n, _ in b]}
    differing = [n for (n, x), (_, y) in zip(a, b)
                 if json.dumps(x, sort_keys=True) != json.dumps(y, sort_keys=True)]
    return {"equal": not differing, "records": len(a), "differing": differing}


def corrupt_one_bit(trace):
    corrupted = copy.deepcopy(trace)
    step = next(r for r in corrupted if r["event"] == "continuation-step" and r["step"] == 10)
    x = step["model"]["ballPosition"][0]
    step["model"]["ballPosition"][0] = f"{int(x, 16) ^ 1:08X}"
    return corrupted


def main():
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("windows_root", type=Path)
    parser.add_argument("linux_root", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("output must be new")
    result = {"arms": {}, "corruptionChecks": {}}
    for arm in ("history", "fresh"):
        win = load(args.windows_root / arm / "probe/trace.jsonl")
        lin = load(args.linux_root / arm / "probe/trace.jsonl")
        result["arms"][arm] = compare(win, lin)
        result["corruptionChecks"][arm] = {"detected": not compare(win, corrupt_one_bit(lin))["equal"]}
    result["pass"] = (all(v["equal"] for v in result["arms"].values())
                      and all(v["detected"] for v in result["corruptionChecks"].values()))
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
