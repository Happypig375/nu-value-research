"""Build a Breakout Mmcc source set for the D9 direction 4 oracle (protocol section 3).

Usage: build_for_oracle.py OTREE SOURCE_DIR GAMES_DIR NAME LOG_DIR
  Restores OTREE's Breakout Mmcc sources to shipped master (from the pinned archive), copies every .fs/.fsproj file
  of SOURCE_DIR over them (a candidate's final folder, or a reference holding only Gameplay.fs), replaces Program.fs
  with the oracle's observer (OracleProgram.fs), builds Release, and copies the output to GAMES_DIR/NAME.
  Exit 0 if built; 1 if the build failed (recorded as "does not build").
"""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile

HERE = Path(__file__).resolve().parent
ARCHIVE = HERE.parent.parent / ".artifacts/vulkan-timing-20261103/nu-47ef39e.tar"
PROJECT = "Projects/Breakout Mmcc"


def main():
    otree, source, games, logs = (Path(p).resolve() for p in (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[5]))
    name = sys.argv[4]
    project = otree / PROJECT
    with tarfile.open(ARCHIVE) as tar:   # restore shipped sources (bin/obj stay, so builds are incremental)
        members = [m for m in tar.getmembers() if m.name.startswith(PROJECT + "/") and m.isfile()
                   and Path(m.name).suffix in (".fs", ".fsproj")]
        tar.extractall(otree, members=members, filter="data")
    copied = []
    for f in sorted(source.iterdir()):
        if f.is_file() and f.suffix in (".fs", ".fsproj") and f.name != "Program.fs":
            shutil.copyfile(f, project / f.name)
            copied.append(f.name)
    program_changed = (source / "Program.fs").exists() and \
        hashlib.sha256((source / "Program.fs").read_bytes()).hexdigest() != \
        "0dd465d63e18b71d9e61da4dfb32205115fca1fc83f8d95e390a083d417c6082"
    shutil.copyfile(HERE / "OracleProgram.fs", project / "Program.fs")
    logs.mkdir(parents=True, exist_ok=True)
    log = logs / f"build-{name}.log"
    with log.open("w") as fh:
        r = subprocess.run(["nice", "-n", "10", "dotnet", "build", str(project / "Breakout Mmcc.fsproj"), "-c", "Release"],
                           stdout=fh, stderr=subprocess.STDOUT)
    receipt = {"name": name, "copied": copied, "candidate_changed_program_fs": program_changed,
               "build_exit": r.returncode,
               "sources": {f.name: hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(project.glob("*.fs"))}}
    if r.returncode == 0:
        dest = games / name
        shutil.rmtree(dest, ignore_errors=True)
        shutil.copytree(project / "bin/Release/net10.0", dest)
    (logs / f"build-{name}.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt))
    return 0 if r.returncode == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
