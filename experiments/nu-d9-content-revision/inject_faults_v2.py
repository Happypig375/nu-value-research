"""Fault-injection positive controls for the frozen direction 3 scorer, version 2 (D9 offline validation, 10 Nov 2026).

Addresses the reviewer's V3-V5 on v1: content faults go into BOTH after.json and reopen.json unless the fault is about
persistence (so persistence hits are not side effects); the unrelated change is a real Position value change on a
non-family entity; untested branches get their own faults (missed after reopen, the control N branch, T2's local keep,
T3's roughness rule, a family member's non-material property); more wrapper faults. Each fault goes into its own copy;
the frozen check.py scores it, then validate_run_v2.py.
Usage: inject_faults_v2.py SERIES_ROUND_DIR OUT_DIR   (reads SERIES_ROUND_DIR/{N,T1-O,T2-O,T3-O}; writes only OUT_DIR)
"""
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
src, out = Path(sys.argv[1]).resolve(strict=True), Path(sys.argv[2]).resolve()
out.mkdir(parents=True, exist_ok=False)
rows, notes = [], {}


def copy(base, name):
    d = out / name
    shutil.copytree(src / base, d)
    (d / "score.json").unlink(missing_ok=True)
    return d


def edit(path, fn):
    data = json.loads(path.read_text())
    fn(data)
    path.write_text(json.dumps(data))


def both(d, fn):
    edit(d / "op/after.json", fn)
    edit(d / "reopen/reopen.json", fn)


def bump_position(entity):
    def fn(s):
        old = s[entity]["props"]["Position"]
        nums = re.findall(r"-?\d+(?:\.\d+)?(?:[eE]-?\d+)?", old)
        s[entity]["props"]["Position"] = old.replace(nums[0], repr(float(nums[0]) + 1.0), 1)
    return fn


probe = json.loads((src / "T1-O/op/probe.json").read_text())
family, local = probe["family"], probe["local"]
after = json.loads((src / "T1-O/op/after.json").read_text())
nonfam = sorted(a for a in after if a not in family and "Position" in after[a]["props"])[0]
member = [m for m in family if m != local][3]

d = copy("T1-O", "F-a2-unrelated-position"); both(d, bump_position(nonfam)); notes[d.name] = f"{nonfam}.Position +1 (after and reopen)"
d = copy("T1-O", "F-b2-entity-removed"); both(d, lambda s: s.pop(nonfam)); notes[d.name] = f"{nonfam} removed (after and reopen)"
d = copy("T1-O", "F-c2-entity-added"); both(d, lambda s: s.__setitem__("Game/Gameplay/Scene/InjectedExtra", json.loads(json.dumps(s[nonfam])))); notes[d.name] = "extra entity (after and reopen)"
d = copy("T1-O", "F-g-family-nonmaterial"); both(d, bump_position(member)); notes[d.name] = f"{member}.Position +1 (after and reopen)"
before = json.loads((src / "T1-O/op/before.json").read_text())
d = copy("T1-O", "F-d2-missed-after-reopen-only"); edit(d / "reopen/reopen.json", lambda s: s[member].__setitem__("material", before[member]["material"])); notes[d.name] = f"{member} albedo reset in reopen.json only"
d = copy("T2-O", "F-h-T2-local-keep-broken"); both(d, lambda s: s[local]["material"].__setitem__("albedo", [0.25, 0.5, 0.75, 1.0])); notes[d.name] = f"{local} given the shared tint in T2"
d = copy("T3-O", "F-i-T3-roughness-missed"); both(d, lambda s: s[member]["material"].__setitem__("roughness", None)); notes[d.name] = f"{member} roughness reset in T3"
d = copy("N", "F-j-control-changed"); edit(d / "op/after.json", bump_position(nonfam)); notes[d.name] = f"control N: {nonfam}.Position +1 in after.json only"
d = copy("T1-O", "W-4-reopen-device-missing"); p = d / "reopen/stdout.log"; p.write_text(p.read_text(errors="replace").replace("Selected Vulkan Device NVIDIA GeForce RTX 4090 D", "removed"))
d = copy("T1-O", "W-5-op-exit-missing"); (d / "op/exit_code.txt").unlink()
d = copy("T1-O", "W-6-op-stdout-missing"); (d / "op/stdout.log").unlink()
d = copy("T1-O", "W-7-exit-is-directory"); (d / "op/exit_code.txt").unlink(); (d / "op/exit_code.txt").mkdir()
d = copy("T1-O", "W-8-exit-non-utf8"); (d / "op/exit_code.txt").write_bytes(b"\xff\xfe0")
d = copy("T1-O", "W-9-exit-text-0-0"); (d / "op/exit_code.txt").write_text("0 0")
for base in ("N", "T1-O", "T2-O", "T3-O"):
    copy(base, f"BASE-{base}")
for d in sorted(out.iterdir()):
    subprocess.run(["python3", "-I", str(HERE / "check.py"), str(d)], capture_output=True, text=True)
    if d.name == "W-9-score-missing":
        pass
    score = json.loads((d / "score.json").read_text()) if (d / "score.json").is_file() else {}
    v = subprocess.run(["python3", "-I", str(HERE / "validate_run_v2.py"), str(d)], capture_output=True, text=True)
    rows.append({"copy": d.name, "fault": notes.get(d.name), "check_py_pass": score.get("pass"),
                 "missed_op": len(score.get("missed_after_op", [])), "missed_reopen": len(score.get("missed_after_reopen", [])),
                 "unrequested": len(score.get("unrequested_changes", [])), "persistence": len(score.get("persistence_differences", [])),
                 "control_diffs": len(score.get("control_after_vs_before", [])), "wrapper": v.stdout.strip(), "wrapper_exit": v.returncode,
                 "wrapper_stderr": v.stderr.strip()[-150:]})
d = out / "W-10-score-missing"; shutil.copytree(src / "T1-O", d); (d / "score.json").unlink(missing_ok=True)
v = subprocess.run(["python3", "-I", str(HERE / "validate_run_v2.py"), str(d)], capture_output=True, text=True)
rows.append({"copy": d.name, "fault": "score.json missing (check.py not run)", "wrapper": v.stdout.strip(), "wrapper_exit": v.returncode})
(out / "results.json").write_text(json.dumps(rows, indent=1))
for r in rows:
    print(json.dumps(r))
