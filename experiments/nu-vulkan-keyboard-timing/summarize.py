"""Summarize keyboard-timing repeats K01..K10 (the unscored feasibility repeat KF is excluded): press latency, release stop time, overshoot, update rate (descriptive).

Usage: summarize.py RUNS_DIR [--out summary.json]. Valid only on this server and configuration.
"""
import argparse
import json
import statistics
from pathlib import Path


def describe(xs):
    xs = sorted(x for x in xs if x is not None)
    if not xs:
        return None
    q = statistics.quantiles(xs, n=4) if len(xs) >= 2 else [xs[0]] * 3
    return {"n": len(xs), "median": round(statistics.median(xs), 2), "q1": round(q[0], 2), "q3": round(q[2], 2),
            "min": xs[0], "max": xs[-1]}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("runs", type=Path)
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()
    trials, repeats = [], []
    for res in sorted(a.runs.glob("K[0-9][0-9]/result.json")):
        r = json.loads(res.read_text())
        repeats.append({"repeat": res.parent.name, "validity": r.get("validity"), "invalid": r.get("invalid"),
                        "secondary": r.get("secondary")})
        if r.get("validity", {}) and r["validity"].get("pass"):
            trials += [dict(t, repeat=res.parent.name) for t in r["trials"] if t.get("valid") and not t.get("interrupted_by_game_over")]
    out = {"repeats": repeats, "valid_trials": len(trials)}
    for key in ("Right", "Left", "all"):
        ts = [t for t in trials if key == "all" or t["key"] == key]
        out[key] = {
            "press_latency_upper_ms": describe([t["press_latency_ms"]["upper"] for t in ts]),
            "press_latency_lower_ms": describe([t["press_latency_ms"]["lower"] for t in ts]),
            "release_stop_upper_ms": describe([t["release_stop_ms"]["upper"] for t in ts]),
            "release_stop_lower_ms": describe([t["release_stop_ms"]["lower"] for t in ts]),
            "overshoot_updates": describe([t["overshoot_updates"] for t in ts]),
            "updates_per_s": describe([t["updates_per_s"] for t in ts]),
            "screenshot_median_ms": describe([t["screenshot_ms"]["median"] for t in ts]),
        }
    text = json.dumps(out, indent=2)
    if a.out:
        a.out.write_text(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
