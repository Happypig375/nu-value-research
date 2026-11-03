"""Apply the section 4.4 pass/fail conditions to receipts from run.py.

Usage: check.py --a0 DIR --a1 DIR --a2 DIR [--out verdict.json]
Each DIR is a run.py output directory. A missing arm is reported as not run.
Protocol: docs/nu-daybreak-recovery-trigger-2026-11-03.md, section 4.4.
"""

import argparse
import json
from pathlib import Path

RECOVERED_PREFIX = "Unexpected exception!\nRewound to previous world.\nError due to:"


def load(directory):
    d = Path(directory)
    process = json.loads((d / "process.json").read_text(encoding="utf-8"))
    events = [json.loads(line) for line in (d / "probe" / "trace.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    stdout = (d / "stdout.log").read_text(encoding="utf-8", errors="replace")
    return process, events, stdout


def first(events, name):
    return next((e for e in events if e["event"] == name), None)


def error_blocks(stdout, marker):
    """Text from each log line containing marker up to the next log line header."""
    blocks, lines, current = [], stdout.splitlines(), None
    for line in lines:
        if "|Info|" in line or "|Warning|" in line or "|Error|" in line:
            if current is not None:
                blocks.append("\n".join(current))
                current = None
            if marker in line:
                current = [line]
        elif current is not None:
            current.append(line)
    if current is not None:
        blocks.append("\n".join(current))
    return blocks


def check_a1(directory):
    process, events, stdout = load(directory)
    settled = first(events, "settled-S0")
    p0 = settled["P0"] if settled else None
    checks, recorded = {}, {}
    invalid = first(events, "trigger-not-reached") is not None or any(
        e["event"] == "probe-exception" and "(invalid)" in e["message"] for e in events)
    blocks = error_blocks(stdout, "Unexpected exception!")
    checks["a_two_faults_logged_divide_by_zero_in_gameplay"] = len(blocks) == 2 and all(
        "Attempted to divide by zero." in b and "Gameplay" in b for b in blocks)
    checks["a_no_could_not_rewind"] = "Could not rewind world" not in stdout
    for n in (1, 2):
        imm, sett = first(events, f"recovery-{n}-immediate"), first(events, f"recovery-{n}-settled")
        checks[f"b_pass{n}_hook_fired_after_fault"] = imm is not None and sett is not None
        if imm:
            checks[f"c_pass{n}_halted_futures0_pasts_P0"] = (not imm["advancing"]) and imm["futures"] == 0 and imm["pasts"] == p0
            checks[f"c_pass{n}_message_box"] = (imm["messageBox"] or "").startswith(RECOVERED_PREFIX)
            checks[f"d_pass{n}_model_equals_S0_immediate"] = imm["modelEqualsS0"]
            recorded[f"pass{n}_live_state_is_K"] = imm["liveStateIsK"]
            recorded[f"pass{n}_last_good_hook_time"] = imm["lastGoodHookTime"]
            recorded[f"pass{n}_projection_equals_S0_immediate"] = imm["projectionEqualsS0"]
            recorded[f"pass{n}_updates_timeupdates_at_recovery"] = [imm["updates"], imm["timeUpdates"]]
        if sett:
            checks[f"d_pass{n}_model_equals_S0_settled"] = sett["modelEqualsS0"]
            checks[f"e_pass{n}_projection_equals_S0_settled"] = sett["projectionEqualsS0"]
    engine = first(events, "engine-exit")
    checks["g_exit_code_0"] = (not process["timed_out"]) and process.get("exit_code") == 0 and engine is not None and engine["exitCode"] == 0
    recorded["and_halted_variant_seen"] = "Rewound to previous world and halted." in stdout
    recorded["clock_irregular_events"] = [e for e in events if e["event"] == "clock-irregular"]
    recorded["elapsed_seconds"] = process["elapsed_seconds"]
    required = ["a_two_faults_logged_divide_by_zero_in_gameplay", "a_no_could_not_rewind"] + [
        f"{k}_pass{n}_{s}" for n in (1, 2) for k, s in
        (("b", "hook_fired_after_fault"), ("c", "halted_futures0_pasts_P0"), ("c", "message_box"),
         ("d", "model_equals_S0_immediate"), ("d", "model_equals_S0_settled"), ("e", "projection_equals_S0_settled"))] + ["g_exit_code_0"]
    passed = all(checks.get(name) is True for name in required)
    verdict = "INVALID" if invalid else ("PASS" if passed else "ADVERSE")
    return {"verdict": verdict, "checks": checks, "missing": [n for n in required if n not in checks], "recorded": recorded}


def check_a0(directory):
    process, events, stdout = load(directory)
    settled = first(events, "settled-S0")
    hit = first(events, "a0-60-updates")
    engine = first(events, "engine-exit")
    checks = {
        "no_exception_logged": "Unexpected exception!" not in stdout and "divide by zero" not in stdout,
        "reached_60_updates_advancing": hit is not None and hit["advancing"],
        "no_message_box": hit is not None and hit["messageBox"] is None,
        "pasts_P0_plus_1": hit is not None and settled is not None and hit["pasts"] == settled["P0"] + 1,
        "exit_code_0": (not process["timed_out"]) and process.get("exit_code") == 0 and engine is not None and engine["exitCode"] == 0,
    }
    return {"verdict": "PASS" if all(checks.values()) else "FAIL", "checks": checks, "elapsed_seconds": process["elapsed_seconds"]}


def check_a2(directory):
    process, events, stdout = load(directory)
    engine = first(events, "engine-exit")
    checks = {
        "advanced_with_snapshot": first(events, "advance-1") is not None,
        "could_not_rewind_logged": "Could not rewind world" in stdout and "Attempted to divide by zero." in stdout,
        "no_recovery_observed": first(events, "recovery-1-immediate") is None,
        "exit_code_1": (not process["timed_out"]) and process.get("exit_code") == 1 and engine is not None and engine["exitCode"] == 1,
    }
    return {"verdict": "PASS" if all(checks.values()) else "FAIL", "checks": checks, "elapsed_seconds": process["elapsed_seconds"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--a0")
    parser.add_argument("--a1")
    parser.add_argument("--a2")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    result = {}
    for arm, fn in (("a0", check_a0), ("a1", check_a1), ("a2", check_a2)):
        directory = getattr(args, arm)
        result[arm] = fn(directory) if directory else {"verdict": "NOT RUN"}
    controls_ok = result["a0"]["verdict"] == "PASS" and result["a2"]["verdict"] == "PASS"
    result["a1_interpretable"] = controls_ok
    text = json.dumps(result, indent=2)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
