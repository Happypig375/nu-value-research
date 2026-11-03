"""Summarize the R06 Vulkan-era series ledger: per-route and paired component times (descriptive only).

Usage: summarize.py RUNS_DIR [--out summary.json]
Times are milliseconds from Stopwatch ticks. Only measured processes that passed enter the summaries; every
attempt is listed. Valid only on this server and configuration (3 November 2026 timing rule).
"""
import argparse
import json
import statistics
from pathlib import Path

COMPONENTS = ("acquisitionTicks", "recoveryDirectTicks", "requestToReadyTicks")


def ms(result, key):
    t = result.get(key, -1)
    return None if t is None or t < 0 else t * 1000.0 / result["stopwatchFrequency"]


def describe(xs):
    xs = sorted(x for x in xs if x is not None)
    if not xs:
        return None
    q = statistics.quantiles(xs, n=4) if len(xs) >= 2 else [xs[0]] * 3
    return {"n": len(xs), "median": round(statistics.median(xs), 4), "q1": round(q[0], 4), "q3": round(q[2], 4),
            "min": round(xs[0], 4), "max": round(xs[-1], 4)}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("runs", type=Path)
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()
    rows = [json.loads(line) for line in (a.runs / "series-ledger.jsonl").read_text().splitlines() if line.strip()]
    attempts = [{"attempt": r["attempt"], "route": r["route"], "kind": r["kind"], "outcome": r["outcome"],
                 "elapsed_seconds": r.get("elapsed_seconds"),
                 "gpu_wait_seconds": r["gpu_before"]["waited_seconds"],
                 "ms": {c: (ms(r["result"], c) if r.get("result") and r["result"].get("pass") else None) for c in COMPONENTS}}
                for r in rows]
    measured = [x for x in attempts if x["kind"] == "measured" and x["outcome"] == "pass"]
    by_route = {route: {c: describe([x["ms"][c] for x in measured if x["route"] == route]) for c in COMPONENTS}
                for route in ("H", "R")}
    pairs = {}
    for x in measured:
        pairs.setdefault(x["attempt"][1:], {})[x["route"]] = x
    paired = {}
    for c in COMPONENTS:
        diffs = [p["H"]["ms"][c] - p["R"]["ms"][c] for p in pairs.values() if "H" in p and "R" in p]
        paired[c] = {"history_minus_reconstruction": describe(diffs),
                     "history_slower_pairs": sum(d > 0 for d in diffs), "history_faster_pairs": sum(d < 0 for d in diffs),
                     "ties": sum(d == 0 for d in diffs), "complete_pairs": len(diffs)}
    summary = {"attempts": attempts, "by_route_ms": by_route, "paired_ms": paired,
               "note": "Descriptive only; valid on this server and configuration; no cross-machine comparison."}
    text = json.dumps(summary, indent=2)
    if a.out:
        a.out.write_text(text + "\n")
    print(json.dumps({"by_route_ms": by_route, "paired_ms": paired}, indent=2))


if __name__ == "__main__":
    main()
