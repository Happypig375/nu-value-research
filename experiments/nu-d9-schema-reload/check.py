"""Score the D9 direction-2 series (amendment 4 outcome): per route x case, did the run reach the common outcome?

Common outcome: (1) the old fields are preserved, (2) the new field equals the case's required value
(A 200, Z 0, N 75), and (3) after one update the seeded brick is gone and the score is 100 + the required value.
Usage: check.py RUNS [--out verdict.json]
"""
import argparse
import json
from pathlib import Path


def evs(p):
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()] if p.exists() else []


def first(ev, name):
    return next((e for e in ev if e["event"] == name), None)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("runs", type=Path)
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()
    ledger = [json.loads(l) for l in (a.runs / "series-ledger.jsonl").read_text().splitlines() if l.strip()]
    seen, results = set(), {}
    for r in ledger:
        base = f"{r['round']}-{r['route']}-{r['case']}"
        if base in seen:
            continue
        seen.add(base)
        last = base + "-R2" if r["route"] == "R" else base
        ev = evs(a.runs / last / "trace.jsonl")
        obs = first(ev, {"L": "post-reload", "M": "post-migration", "R": "post-reconstruction"}[r["route"]])
        cont = first(ev, "continuation")
        reload_ = first(evs(a.runs / base / "trace.jsonl"), "reload-called") if r["route"] != "R" else None
        req = {"A": "200", "Z": "0", "N": "75"}[r["case"]]
        checks = {
            "old_fields_preserved": bool(obs and obs["oldFieldsPreserved"]),
            "new_field_equals_required": bool(obs and obs["brickReward"] == req),
            "brick_hit_scores_required": bool(cont and cont["hitBrickRemoved"] and cont["score"] == str(100 + int(req))),
        }
        results[base] = {"round": r["round"], "route": r["route"], "case": r["case"], "pass": all(checks.values()), "checks": checks,
                         "observed_new_field": obs["brickReward"] if obs else None, "continuation_score": cont["score"] if cont else None,
                         "reload_ms": reload_["reloadMs"] if reload_ else None}
    summary = {}
    for route in "LMR":
        for case in "AZN":
            rs = [v for k, v in results.items() if v["route"] == route and v["case"] == case and v["round"] != "F4"]
            summary[f"{route}-{case}"] = {"scored": len(rs), "passed": sum(v["pass"] for v in rs),
                                          "observed_new_field": sorted({v["observed_new_field"] for v in rs if v["observed_new_field"]})}
    out = {"attempts": results, "summary": summary}
    if a.out:
        a.out.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
