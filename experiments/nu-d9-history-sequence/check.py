"""Score one D9 history-sequence run (protocol docs/nu-d9-history-sequence-2026-11-11.md, section 5).
Usage: check.py RUN_DIR  (writes RUN_DIR/score.json, prints a summary line)"""
import json
from pathlib import Path
import re
import sys

TINT = [0.25, 0.5, 0.75, 1.0]
ROUGH = 0.75
LINE = "Selected Vulkan Device NVIDIA GeForce RTX 4090 D"


def field(record, name):
    """Independently derive a field's value from the raw Prime record string: None, a float, or a list of floats."""
    i = record.find("[" + name + " ")
    if i < 0:
        return "absent"
    depth, j = 0, i
    while j < len(record):
        depth += {"[": 1, "]": -1}.get(record[j], 0); j += 1
        if depth == 0:
            break
    body = record[i + len(name) + 2:j - 1].strip()
    if body == "None":
        return None
    nums = [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?(?:[eE]-?\d+)?", body)]
    return nums if len(nums) > 1 else nums[0]


def strip(record, names):
    out, i = [], 0
    while i < len(record):
        hit = next((n for n in names if record.startswith("[" + n + " ", i)), None)
        if hit is None:
            out.append(record[i]); i += 1; continue
        depth = 0
        while i < len(record):
            depth += {"[": 1, "]": -1}.get(record[i], 0); i += 1
            if depth == 0:
                break
        while i < len(record) and record[i] == " ":
            i += 1
    return "".join(out).strip()


def raw_mp(e):
    return e["props"].get("MaterialProperties")


def missed(snap, before, family, stage):
    out = []
    for a in family:
        e, b = snap.get(a), before.get(a)
        if not e or not b or e["material"] is None or b["material"] is None:
            out.append({"entity": a, "why": "missing"}); continue
        want_alb = TINT
        want_rough = ROUGH if stage == 2 else b["material"]["roughness"]
        probs = []
        if e["material"]["albedo"] != want_alb: probs.append({"albedo": e["material"]["albedo"]})
        if e["material"]["roughness"] != want_rough: probs.append({"roughness": e["material"]["roughness"]})
        if strip(e["material"]["record"], ("AlbedoOpt", "RoughnessOpt")) != strip(b["material"]["record"], ("AlbedoOpt", "RoughnessOpt")):
            probs.append({"other_fields_changed": True})
        if probs: out.append({"entity": a, "problems": probs})
    return out


def derived_disagreements(snap, family):
    """Compare the probe's summary with values derived here from the raw MaterialProperties string (when present)."""
    out = []
    for a in family:
        e = snap.get(a)
        raw = raw_mp(e) if e else None
        if raw is None:
            if e and e["material"] and (e["material"]["albedo"] is not None or e["material"]["roughness"] is not None):
                out.append({"entity": a, "why": "summary non-default but no raw MaterialProperties"})
            continue
        alb, rough = field(raw, "AlbedoOpt"), field(raw, "RoughnessOpt")
        if alb != e["material"]["albedo"] or rough != e["material"]["roughness"]:
            out.append({"entity": a, "raw": [alb, rough], "summary": [e["material"]["albedo"], e["material"]["roughness"]]})
    return out


def unrequested(snap, before, family):
    out = []
    for a in sorted(set(snap) | set(before)):
        if a not in snap or a not in before:
            out.append({"entity": a, "change": "added" if a in snap else "removed"}); continue
        for n in sorted(set(snap[a]["props"]) | set(before[a]["props"])):
            if n == "MaterialProperties" and a in family:
                continue
            if snap[a]["props"].get(n) != before[a]["props"].get(n):
                out.append({"entity": a, "property": n})
    return out


def persistence(r, a):
    out = []
    for x in sorted(set(r) | set(a)):
        if x not in r or x not in a:
            out.append({"entity": x}); continue
        for n in sorted(set(r[x]["props"]) | set(a[x]["props"])):
            if r[x]["props"].get(n) != a[x]["props"].get(n):
                out.append({"entity": x, "property": n})
    return out


def metadata(snap, prev, family, source):
    return {"order_changed": sum(1 for a in snap if a in prev and snap[a]["order"] != prev[a]["order"]),
            "history_changed": sum(1 for a in snap if a in prev and snap[a]["history"] != prev[a]["history"]),
            "source_history_has_MaterialProperties": "MaterialProperties" in (snap[source]["history"] or ""),
            "family_with_raw_MaterialProperties": sum(1 for a in family if raw_mp(snap[a]) is not None)}


def main():
    run = Path(sys.argv[1])
    probe = json.loads((run / "probe.json").read_text())
    family, seq = probe["family"], probe["seq"]
    source = "Game/Gameplay/Scene/Villa/Palm"
    L = lambda n: json.loads((run / n).read_text())
    before, after2, reopen2 = L("before.json"), L("after2.json"), L("reopen2.json")
    s = {"run": f"{run.parent.name}/{run.name}", "seq": seq, "family_size": len(family),
         "step1_ms": probe["step1_ms"], "step2_ms": probe["step2_ms"], "save2_ms": probe["save2_ms"]}
    if seq == "N":
        s["control_diffs"] = persistence(after2, before)
        s["persistence2"] = persistence(reopen2, after2)
        s["metadata_before"] = metadata(before, before, family, source)
        s["pass_live"] = not s["control_diffs"] and not s["persistence2"]
    else:
        after1, reopen1 = L("after1.json"), L("reopen1.json")
        s["missed_after1"] = missed(after1, before, family, 1)
        s["missed_reopen1"] = missed(reopen1, before, family, 1)
        s["missed_after2"] = missed(after2, before, family, 2)
        s["missed_reopen2"] = missed(reopen2, before, family, 2)
        s["derived_disagreements"] = derived_disagreements(after1, family) + derived_disagreements(after2, family) + derived_disagreements(reopen2, family)
        s["unrequested1"] = unrequested(after1, before, set(family))
        s["unrequested2"] = unrequested(after2, before, set(family))
        s["persistence1"] = persistence(reopen1, after1)
        s["persistence2"] = persistence(reopen2, after2)
        s["metadata_before"] = metadata(before, before, family, source)
        s["metadata_step1"] = metadata(after1, before, family, source)
        s["metadata_step2"] = metadata(after2, after1, family, source)
        s["pass_live"] = not any(s[k] for k in ("missed_after1", "missed_reopen1", "missed_after2", "missed_reopen2",
                                               "unrequested1", "unrequested2", "persistence1", "persistence2"))
    procs = ["op", "reopen2"] + ([] if seq == "N" else ["reopen1"])
    s["processes_ok"] = all((run / f"{p}.exit_code.txt").is_file() and (run / f"{p}.exit_code.txt").read_text().strip() == "0"
                            and LINE in (run / f"{p}.stdout.log").read_text(errors="replace") for p in procs)
    s["pass"] = s["pass_live"] and s["processes_ok"]
    (run / "score.json").write_text(json.dumps(s, indent=1))
    print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in s.items()}))


if __name__ == "__main__":
    main()
