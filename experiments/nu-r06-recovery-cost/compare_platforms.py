"""Compare per-pair timing directions of two frozen R06 summaries (read-only; added 2026-11-02).

Reads the `summary.json` written by the frozen summarize.py for each platform and reports, per
component, how many valid pairs had history (H) minus reconstruction (R) below zero, plus route and
paired medians. Absolute times are not comparable across machines; only directions are compared.
See docs/nu-r06-linux-reproduction-2026-11-02.md.

Usage: compare_platforms.py WINDOWS_SUMMARY_JSON LINUX_SUMMARY_JSON OUTPUT_JSON
"""

import argparse
import json
from pathlib import Path

COMPONENTS = ("acquisition", "directRecovery", "requestToReady")


def directions(summary):
    pairs = summary["descriptiveSummaries"]["pairs"]
    out = {}
    for component in COMPONENTS:
        values = [p["differences"][component]["historyMinusReconstructionMilliseconds"]
                  for p in pairs if p["validCompletePair"]]
        out[component] = {
            "validPairs": len(values),
            "historyFasterPairs": sum(v < 0 for v in values),
            "historySlowerPairs": sum(v > 0 for v in values),
            "perPairHistoryMinusReconstructionMs": values,
        }
    for row in summary["descriptiveSummaries"]["historyMinusReconstruction"]:
        out[row["component"]]["pairedMedianMs"] = row["medianMilliseconds"]
    for row in summary["descriptiveSummaries"]["byRoute"]:
        out[row["component"]][f"routeMedianMs{row['route']}"] = row["medianMilliseconds"]
    return out


def consistent(d):
    n = d["validPairs"]
    if n and d["historyFasterPairs"] == n:
        return "H faster in every pair"
    if n and d["historySlowerPairs"] == n:
        return "H slower in every pair"
    return "mixed"


def main():
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("windows", type=Path)
    parser.add_argument("linux", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("output must be new")
    win, lin = (directions(json.loads(p.read_text(encoding="utf-8"))) for p in (args.windows, args.linux))
    result = {"components": {}}
    for component in COMPONENTS:
        w, l = consistent(win[component]), consistent(lin[component])
        result["components"][component] = {
            "windows": win[component] | {"pattern": w},
            "linux": lin[component] | {"pattern": l},
            "patternReplicated": w == l and w != "mixed",
            "samePattern": w == l,
        }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for component, row in result["components"].items():
        print(f"{component}: windows={row['windows']['pattern']} linux={row['linux']['pattern']} "
              f"(H faster in {row['linux']['historyFasterPairs']}/{row['linux']['validPairs']} Linux pairs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
