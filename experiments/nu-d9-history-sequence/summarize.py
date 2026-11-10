"""Summarize the scored D9 history-sequence rounds (protocol section 5). Usage: summarize.py SERIES_DIR OUT_JSON"""
import json
from pathlib import Path
import re
import statistics as st
import sys

series, out = Path(sys.argv[1]), Path(sys.argv[2])
rows = []
for rnd in ("1", "2", "3"):
    for seq in ("N", "PP", "HP", "HH"):
        s = json.loads((series / f"round-{rnd}" / seq / "score.json").read_text())
        rows.append(s)
summary = {}
for seq in ("N", "PP", "HP", "HH"):
    g = [r for r in rows if r["seq"] == seq]
    c = lambda k: [len(r.get(k, [])) for r in g]
    summary[seq] = {"runs": len(g), "pass": sum(r["pass"] for r in g), "processes_ok": all(r["processes_ok"] for r in g),
                    "missed_after1": c("missed_after1"), "missed_reopen1": c("missed_reopen1"),
                    "missed_after2": c("missed_after2"), "missed_reopen2": c("missed_reopen2"),
                    "unrequested": [a + b for a, b in zip(c("unrequested1"), c("unrequested2"))],
                    "persistence": [a + b for a, b in zip(c("persistence1"), c("persistence2"))],
                    "derived_disagreements": c("derived_disagreements"), "control_diffs": c("control_diffs"),
                    "step1_ms_median": st.median(r["step1_ms"] for r in g), "step2_ms_median": st.median(r["step2_ms"] for r in g),
                    "metadata_step1": [r.get("metadata_step1") for r in g][:1], "metadata_step2": [r.get("metadata_step2") for r in g][:1]}
    if seq == "HP":
        problems = [p for r in g for m in r["missed_after2"] for p in m.get("problems", [])]
        summary[seq]["missed_after2_problem_kinds"] = sorted({json.dumps(p) for p in problems})
        missed_names = sorted({m["entity"] for r in g for m in r["missed_after2"]})
        summary[seq]["missed_includes_source"] = "Game/Gameplay/Scene/Villa/Palm" in missed_names
# independent raw read of one adverse member (round 1 HP), straight from the snapshot strings
hp = series / "round-1" / "HP"
a2 = json.loads((hp / "after2.json").read_text()); r2 = json.loads((hp / "reopen2.json").read_text())
fam = json.loads((hp / "probe.json").read_text())["family"]
m = [x for x in fam if x != "Game/Gameplay/Scene/Villa/Palm"][0]
grab = lambda raw, f: (re.search(r"\[" + f + r" (\[[^\]]*\]\]|None|\[Some [^\]]*\])", raw or "") or [None, None])[1]
summary["raw_check_round1_HP"] = {"member": m,
    "after2_raw_AlbedoOpt": grab(a2[m]["props"].get("MaterialProperties"), "AlbedoOpt"),
    "after2_raw_RoughnessOpt": grab(a2[m]["props"].get("MaterialProperties"), "RoughnessOpt"),
    "reopen2_raw_RoughnessOpt": grab(r2[m]["props"].get("MaterialProperties"), "RoughnessOpt"),
    "source_after2_raw_RoughnessOpt": grab(a2["Game/Gameplay/Scene/Villa/Palm"]["props"].get("MaterialProperties"), "RoughnessOpt")}
out.write_text(json.dumps({"summary": summary, "rows": [{k: (len(v) if isinstance(v, list) else v) for k, v in r.items()} for r in rows]}, indent=1))
print(json.dumps(summary, indent=1))
