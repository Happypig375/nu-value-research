"""Supplemental, post-hoc quit-while-paused predicate, version 2 (D9 offline validation, 10 Nov 2026).

Fixes the reviewer's V2 on v1: the oracle's `invalid` field and malformed records now give unknown instead of pass or a
crash. Rule, in order: unknown if the record is unreadable or not an object, `invalid` is not null, old (d) is not a
boolean, or details.d.paused_before_quit is absent / not a boolean; otherwise fail if old (d) is false or the pause
evidence is false; otherwise pass. Reads recorded oracle results only: it does not re-run or repair the live oracle and
does not prove pause on its own (paused_before_quit = the Ball entity did not move for 0.3 s after a P tap; a ball that is
stationary for another reason would also give true; paddle not checked).
Usage: quit_paused_v2.py RESULT_JSON [...]   Exit code 0 always; the verdict is in each JSON line.
"""
import json
import sys


def judge(path):
    try:
        r = json.load(open(path))
    except Exception as e:
        return "unknown", None, None, f"unreadable ({type(e).__name__})"
    if not isinstance(r, dict):
        return "unknown", None, None, "record is not an object"
    if r.get("invalid") is not None:
        return "unknown", None, None, "oracle run marked invalid"
    checks = r.get("checks") if isinstance(r.get("checks"), dict) else {}
    old_d = checks.get("d")
    details = r.get("details") if isinstance(r.get("details"), dict) else {}
    dd = details.get("d") if isinstance(details.get("d"), dict) else {}
    pause = dd.get("paused_before_quit")
    if not isinstance(old_d, bool):
        return "unknown", old_d, pause, "old check (d) missing or not a boolean"
    if not isinstance(pause, bool):
        return "unknown", old_d, pause, "paused_before_quit absent or not a boolean"
    if not old_d:
        return "fail", old_d, pause, "old check (d) failed"
    return ("pass", old_d, pause, "") if pause else ("fail", old_d, pause, "not paused before quit")


for p in sys.argv[1:]:
    v, d, pz, why = judge(p)
    print(json.dumps({"file": p, "old_d": d, "paused_before_quit": pz, "quit_paused_v2": v, "why": why}))
