"""Fault-injection positive controls for the frozen direction 3 scorer (D9 offline validation, 10 Nov 2026).

Usage: inject_faults.py BASE_RUN_DIR OUT_DIR   (BASE is only read; each fault goes into its own copy in OUT_DIR,
which is then scored with the unchanged check.py and with validate_run.py)
"""
import json
from pathlib import Path
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
base, out = Path(sys.argv[1]).resolve(strict=True), Path(sys.argv[2]).resolve()
out.mkdir(parents=True, exist_ok=False)
family = json.loads((base / "op" / "probe.json").read_text())["family"]
after0 = json.loads((base / "op" / "after.json").read_text())
non_family = next(a for a in after0 if a not in family and after0[a]["props"])
prop = sorted(after0[non_family]["props"])[0]
member = family[3]


def copy(name):
    d = out / name
    shutil.copytree(base, d)
    (d / "score.json").unlink(missing_ok=True)
    return d


def edit(path, fn):
    data = json.loads(path.read_text())
    fn(data)
    path.write_text(json.dumps(data))


faults = {}
d = copy("F-a-unrelated-property"); edit(d / "op/after.json", lambda s: s[non_family]["props"].__setitem__(prop, s[non_family]["props"][prop] + " ")); faults[d.name] = f"{non_family}.{prop}"
d = copy("F-b-entity-removed"); edit(d / "op/after.json", lambda s: s.pop(non_family)); faults[d.name] = non_family
d = copy("F-c-entity-added"); edit(d / "op/after.json", lambda s: s.__setitem__("Game/Gameplay/Scene/InjectedExtra", json.loads(json.dumps(s[non_family])))); faults[d.name] = "InjectedExtra"
before = json.loads((base / "op/before.json").read_text())
d = copy("F-d-missed-edit"); edit(d / "op/after.json", lambda s: s[member].__setitem__("material", before[member]["material"])); faults[d.name] = member
d = copy("F-e-reopen-corrupted"); edit(d / "reopen/reopen.json", lambda s: s[non_family]["props"].__setitem__(prop, "corrupted")); faults[d.name] = f"{non_family}.{prop}"
d = copy("F-f-other-material-field"); edit(d / "op/after.json", lambda s: s[member]["material"].__setitem__("record", s[member]["material"]["record"].replace("[MetallicOpt None]", "[MetallicOpt [Some 0.5]]"))); faults[d.name] = member
d = copy("W-1-op-exit-1"); (d / "op/exit_code.txt").write_text("1")
d = copy("W-2-reopen-exit-missing"); (d / "reopen/exit_code.txt").unlink()
d = copy("W-3-device-line-removed"); p = d / "op/stdout.log"; p.write_text(p.read_text(errors="replace").replace("Selected Vulkan Device NVIDIA GeForce RTX 4090 D", "Selected Vulkan Device (removed by fault injection)"))
copy("BASE-copy")
rows = []
for d in sorted(out.iterdir()):
    c = subprocess.run(["python3", "-I", str(HERE / "check.py"), str(d)], capture_output=True, text=True)
    score = json.loads((d / "score.json").read_text()) if (d / "score.json").exists() else {}
    v = subprocess.run(["python3", "-I", str(HERE / "validate_run.py"), str(d)], capture_output=True, text=True)
    rows.append({"copy": d.name, "fault_target": faults.get(d.name), "check_py_pass": score.get("pass"),
                 "missed_after_op": len(score.get("missed_after_op", [])), "missed_after_reopen": len(score.get("missed_after_reopen", [])),
                 "unrequested": len(score.get("unrequested_changes", [])), "persistence": len(score.get("persistence_differences", [])),
                 "check_py_error": c.stderr.strip()[-200:], "validate_run": v.stdout.strip()})
(out / "results.json").write_text(json.dumps(rows, indent=1))
for r in rows:
    print(json.dumps(r))
