"""Supplemental, post-hoc quit-while-paused predicate, version 1 (D9 offline validation, 10 Nov 2026).

Usage: quit_paused_v1.py RESULT_JSON [RESULT_JSON ...]   (read-only; prints one JSON line per input)
pass    = the old oracle check (d) is true AND details.d.paused_before_quit is literally true
fail    = old (d) is false, or paused_before_quit is false
unknown = old (d) missing, or paused_before_quit absent / not a boolean
It reads recorded oracle results only. It does not re-run the game or prove that pause worked; paused_before_quit is
the oracle's own 0.3 s check that the Ball entity did not move after a P tap (paddle not checked; absent ball -> false).
"""
import json
import sys


def judge(result):
    old_d = result.get("checks", {}).get("d")
    pause = result.get("details", {}).get("d", {}).get("paused_before_quit", None)
    if not isinstance(old_d, bool):
        return "unknown", old_d, pause, "old check (d) missing"
    if old_d is False:
        return "fail", old_d, pause, "old check (d) failed"
    if not isinstance(pause, bool):
        return "unknown", old_d, pause, "paused_before_quit absent or not a boolean"
    return ("pass" if pause else "fail"), old_d, pause, "" if pause else "not paused before quit"


for path in sys.argv[1:]:
    verdict, old_d, pause, why = judge(json.load(open(path)))
    print(json.dumps({"file": path, "old_d": old_d, "paused_before_quit": pause, "quit_paused_v1": verdict, "why": why}))
