"""Score one D9 direction 3 run (protocol docs/nu-d9-content-revision-2026-11-11.md, section 4).

Usage: check.py RUN_DIR  (holds op/ and reopen/ from TerraProbe; prints and writes RUN_DIR/score.json)
"""
import json
from pathlib import Path
import sys

TINT = [0.25, 0.5, 0.75, 1.0]
LOCAL = [1.0, 0.0, 0.0, 1.0]
ROUGH = 0.75


def strip_fields(record, fields):
    """Remove `[Field ...]` groups (balanced brackets) for the given field names from a Prime record string."""
    out, i = [], 0
    while i < len(record):
        hit = next((f for f in fields if record.startswith("[" + f + " ", i)), None)
        if hit is None:
            out.append(record[i])
            i += 1
            continue
        depth = 0
        while i < len(record):
            depth += {"[": 1, "]": -1}.get(record[i], 0)
            i += 1
            if depth == 0:
                break
        while i < len(record) and record[i] == " ":
            i += 1
    return "".join(out).strip()


def required(task, address, local):
    """(albedo, roughness) required for a family member; None means 'as loaded'."""
    if task == "T1":
        return TINT, None
    if task == "T2":
        return (LOCAL if address == local else TINT), None
    if task == "T3":
        return (LOCAL if address == local else None), ROUGH
    return None, None


def check_family(snap, before, family, task, local):
    missed = []
    for address in family:
        e, b = snap.get(address), before.get(address)
        if e is None or e["material"] is None or b is None or b["material"] is None:
            missed.append({"entity": address, "why": "missing entity or material"})
            continue
        want_albedo, want_rough = required(task, address, local)
        want_albedo = b["material"]["albedo"] if want_albedo is None else want_albedo
        want_rough = b["material"]["roughness"] if want_rough is None else want_rough
        rest_now = strip_fields(e["material"]["record"], ("AlbedoOpt", "RoughnessOpt"))
        rest_before = strip_fields(b["material"]["record"], ("AlbedoOpt", "RoughnessOpt"))
        problems = []
        if e["material"]["albedo"] != want_albedo:
            problems.append({"albedo": e["material"]["albedo"], "want": want_albedo})
        if e["material"]["roughness"] != want_rough:
            problems.append({"roughness": e["material"]["roughness"], "want": want_rough})
        if rest_now != rest_before:
            problems.append({"other_material_fields_changed": True})
        if problems:
            missed.append({"entity": address, "problems": problems})
    return missed


def unrequested(after, before, family):
    changes = []
    for address in sorted(set(after) | set(before)):
        if address not in after or address not in before:
            changes.append({"entity": address, "change": "added" if address in after else "removed"})
            continue
        pa, pb = after[address]["props"], before[address]["props"]
        for name in sorted(set(pa) | set(pb)):
            if name == "MaterialProperties" and address in family:
                continue
            if pa.get(name) != pb.get(name):
                changes.append({"entity": address, "property": name, "before": pb.get(name), "after": pa.get(name)})
    return changes


def differences(a, b):
    out = []
    for address in sorted(set(a) | set(b)):
        if address not in a or address not in b:
            out.append({"entity": address, "only_in": "reopen" if address in a else "after"})
            continue
        for name in sorted(set(a[address]["props"]) | set(b[address]["props"])):
            if a[address]["props"].get(name) != b[address]["props"].get(name):
                out.append({"entity": address, "property": name})
    return out


def main():
    run = Path(sys.argv[1])
    op, re_ = run / "op", run / "reopen"
    probe = json.loads((op / "probe.json").read_text())
    task, family, local = probe["task"], probe["family"], probe["local"]
    before = json.loads((op / "before.json").read_text())
    after = json.loads((op / "after.json").read_text())
    reopen = json.loads((re_ / "reopen.json").read_text())
    score = {"run": run.name, "task": task, "cond": probe["cond"], "family_size": len(family), "local": local,
             "op_ms": probe["op_ms"], "prep_ms": probe["prep_ms"], "save_ms": probe["save_ms"], "load_ms": probe["load_ms"],
             "reopen_load_ms": json.loads((re_ / "probe.json").read_text())["load_ms"], "note": probe["note"]}
    if task == "NONE":
        score["control_after_vs_before"] = differences(after, before)
        score["persistence_differences"] = differences(reopen, after)
        score["pass"] = not score["control_after_vs_before"] and not score["persistence_differences"]
    else:
        score["missed_after_op"] = check_family(after, before, family, task, local)
        score["missed_after_reopen"] = check_family(reopen, before, family, task, local)
        score["unrequested_changes"] = unrequested(after, before, set(family))
        score["persistence_differences"] = differences(reopen, after)
        score["pass"] = not (score["missed_after_op"] or score["missed_after_reopen"]
                             or score["unrequested_changes"] or score["persistence_differences"])
    for name in ("op", "reopen"):
        log = (run / name / "stdout.log")
        score[f"{name}_vulkan_device_line"] = log.exists() and "Selected Vulkan Device NVIDIA GeForce RTX 4090 D" in log.read_text(errors="replace")
        rc = run / name / "exit_code.txt"
        score[f"{name}_exit_code"] = int(rc.read_text()) if rc.exists() else None
    (run / "score.json").write_text(json.dumps(score, indent=2) + "\n")
    short = {k: (len(v) if isinstance(v, list) else v) for k, v in score.items()}
    print(json.dumps(short))


if __name__ == "__main__":
    main()
