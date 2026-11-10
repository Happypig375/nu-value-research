"""Apply the D9 recovery-routes pass conditions and summarize (direction 1).

Usage: check.py RUNS_DIR [--out verdict.json]
Per scored attempt (rounds 1-5): did the route reach the common outcome, how much progress was lost, how long from
the fault to a ready world, and how long the checkpoint took. Round Z is feasibility and is reported separately.
Protocol: docs/nu-d9-recovery-routes-2026-11-10.md, section 4.
"""
import argparse
import json
import statistics
from pathlib import Path

FAULT_CLOCK = 30
REWOUND = "Unexpected exception!\nRewound to previous world.\nError due to: Attempted to divide by zero."


def events(runs, attempt):
    p = runs / attempt / "trace.jsonl"
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()] if p.exists() else []


def first(evs, name):
    return next((e for e in evs if e["event"] == name), None)


def history_route(runs, attempt, ledger):
    ev = events(runs, attempt)
    rec, s1, s10, cont, ex = (first(ev, n) for n in ("recovery-immediate", "recovered-first-hook", "recovered-settled", "continuation", "engine-exit"))
    cp = first(ev, "checkpoint")
    checks = {
        "fault_caught_and_rewound": rec is not None and (rec.get("messageBox") or "").startswith(REWOUND),
        "halted_futures_0": rec is not None and not rec["advancing"] and rec["futures"] == 0,
        "model_scene_equal_recovery_point_first_hook": bool(s1 and s1["modelEqualsExpected"] and s1["projectionEqualsExpected"]),
        "model_scene_equal_recovery_point_settled": bool(s10 and s10["modelEqualsExpected"] and s10["projectionEqualsExpected"] and not s10["projectionErrors"]),
        "continuation_equals_original_run": bool(cont and cont["modelEqualsOriginalRunAtSameClock"]),
        "exit_code_0": ledger.get(attempt, {}).get("exit_code") == 0 and ex is not None and ex["exitCode"] == 0,
    }
    recovered = s1["gameplayTime"] if s1 else None
    return {"pass": all(checks.values()), "checks": checks, "recovered_clock": recovered,
            "lost_updates": FAULT_CLOCK - recovered if recovered is not None else None,
            "fault_to_ready_ms_upper": rec["gapFromLastHookMs"] if rec else None,
            "checkpoint_ms": cp["checkpointMs"] if cp else None, "processes": 1}


def file_route(runs, base, ledger):
    e1, e2 = events(runs, base + "1"), events(runs, base + "2")
    cp, ex1 = first(e1, "checkpoint"), first(e1, "engine-exit")
    imp, s1, s10, cont, ex2 = (first(e2, n) for n in ("import", "recovered-first-hook", "recovered-settled", "continuation", "engine-exit"))
    stdout1 = (runs / f"{base}1.stdout.log").read_text(errors="replace") if (runs / f"{base}1.stdout.log").exists() else ""
    checks = {
        "checkpoint_written": cp is not None and cp.get("fileBytes", 0) > 0,
        "session_ended_by_fault": ex1 is not None and ex1["exitCode"] == 1 and "Could not rewind world" in stdout1,
        "import_done": imp is not None,
        "model_scene_equal_checkpoint_first_hook": bool(s1 and s1["modelEqualsExpected"] and s1["projectionEqualsExpected"]),
        "model_scene_equal_checkpoint_settled": bool(s10 and s10["modelEqualsExpected"] and s10["projectionEqualsExpected"] and not s10["projectionErrors"]),
        "continuation_equals_original_run": bool(cont and cont["modelEqualsOriginalRunAtSameClock"]),
        "restart_exit_code_0": ledger.get(base + "2", {}).get("exit_code") == 0 and ex2 is not None and ex2["exitCode"] == 0,
    }
    recovered = s1["gameplayTime"] if s1 else None
    f2r = (s1["utcMs"] - ex1["lastHookUtcMs"]) if (s1 and ex1 and ex1.get("lastHookUtcMs")) else None
    return {"pass": all(checks.values()), "checks": checks, "recovered_clock": recovered,
            "lost_updates": FAULT_CLOCK - recovered if recovered is not None else None,
            "fault_to_ready_ms_upper": f2r, "checkpoint_ms": cp["checkpointMs"] if cp else None,
            "import_ms": imp["importMs"] if imp else None, "processes": 2}


def describe(xs):
    xs = sorted(x for x in xs if x is not None)
    if not xs:
        return None
    return {"n": len(xs), "median": round(statistics.median(xs), 2), "min": round(xs[0], 2), "max": round(xs[-1], 2)}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("runs", type=Path)
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()
    ledger = {}
    for l in (a.runs / "series-ledger.jsonl").read_text().splitlines():
        if l.strip():
            r = json.loads(l)
            ledger[r["attempt"]] = r
    results = {}
    for rnd in ["Z", "Z2", "1", "2", "3", "4", "5"]:
        for route in "HFC":
            base = f"{rnd}-{route}"
            if route == "C" and (base + "1") in ledger:
                results[base] = file_route(a.runs, base, ledger)
            elif base in ledger:
                results[base] = history_route(a.runs, base, ledger)
    summary = {}
    for route in "HFC":
        scored = [v for k, v in results.items() if k.endswith(route) and not k.startswith("Z")]
        summary[route] = {"scored": len(scored), "passed": sum(v["pass"] for v in scored),
                          "lost_updates": describe([v["lost_updates"] for v in scored]),
                          "fault_to_ready_ms_upper": describe([v["fault_to_ready_ms_upper"] for v in scored]),
                          "checkpoint_ms": describe([v["checkpoint_ms"] for v in scored]),
                          "import_ms": describe([v.get("import_ms") for v in scored])}
    out = {"attempts": results, "summary": summary}
    text = json.dumps(out, indent=2)
    if a.out:
        a.out.write_text(text + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
