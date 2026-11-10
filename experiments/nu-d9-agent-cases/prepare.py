"""Prepare Nu master 47ef39e trees for D9 direction 4 (coding agents with and without explicit case enumeration).

  prepare.py tree ARCHIVE DEST --variant E|W [--candidate]
      Extract the pinned git-archive tar (hash and commit checked) into a new folder. Variant E is the shipped
      Breakout Mmcc source. Variant W replaces the one gameplay-state match arm `| Playing | Quit -> gameplay` with
      `| _ -> gameplay` (behaviourally identical before the task). --candidate keeps only what a candidate needs to
      build Breakout Mmcc: Nu/, Projects/Breakout Mmcc/, License.md and ReadMe.md, and writes TASK.md.
  prepare.py oracle PROJECT_DIR
      Replace PROJECT_DIR/Program.fs with the oracle's observer Program.fs (OracleProgram.fs) and print the hashes.

Protocol: docs/nu-d9-agent-cases-2026-11-11.md.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import tarfile

COMMIT = "47ef39e176424675f067c378c3a5f86f9c5ec3be"
ARCHIVE_SHA256 = "3dcae8b0c61103b12b215b631bcca96fc219bfced876e1d35753db348581faac"
GAMEPLAY = "Projects/Breakout Mmcc/Gameplay.fs"
E_ARM = "        // no update while gameplay is inactive\n        | Playing | Quit -> gameplay\n"
W_ARM = "        // no update while gameplay is inactive\n        | _ -> gameplay\n"
KEEP = ("Nu/", "Projects/Breakout Mmcc/", "License.md", "ReadMe.md")
HERE = Path(__file__).resolve().parent
TASK = """# Task

Add a `Paused` gameplay state. Pressing P toggles pause during play. While paused, nothing moves and the message reads 'Paused'. Quitting while paused works as before.

The game is `Projects/Breakout Mmcc` (Nu game engine, F#) in this folder. Work only inside this folder. You may build with `dotnet build "Projects/Breakout Mmcc/Breakout Mmcc.fsproj"`. Do not run the game: no display is available. When you are done, reply with a short summary of your change.
"""


def sha(data):
    return hashlib.sha256(data).hexdigest()


def edit(path, old, new):
    raw = path.read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig")
    crlf = "\r\n" in text
    body = text.replace("\r\n", "\n")
    if body.count(old) != 1:
        raise SystemExit(f"anchor not unique in {path}")
    body = body.replace(old, new)
    if crlf:
        body = body.replace("\n", "\r\n")
    out = (b"\xef\xbb\xbf" if bom else b"") + body.encode("utf-8")
    path.write_bytes(out)
    return {"original_sha256": sha(raw), "edited_sha256": sha(out)}


def tree(a):
    if sha(a.archive.read_bytes()) != ARCHIVE_SHA256:
        raise SystemExit("archive hash differs from the pinned archive")
    if a.destination.exists() and any(a.destination.iterdir()):
        raise SystemExit("destination must be new or empty")
    a.destination.mkdir(parents=True, exist_ok=True)
    with tarfile.open(a.archive) as tar:
        if tar.pax_headers.get("comment") != COMMIT:
            raise SystemExit("archive does not identify the pinned Nu commit")
        members = [m for m in tar.getmembers() if not a.candidate or m.name.startswith(KEEP)]
        tar.extractall(a.destination, members=members, filter="data")
    receipt = {"archive_sha256": ARCHIVE_SHA256, "commit": COMMIT, "variant": a.variant, "candidate": a.candidate}
    gameplay = a.destination / GAMEPLAY
    if a.variant == "W":
        receipt["gameplay"] = edit(gameplay, E_ARM, W_ARM)
    else:
        receipt["gameplay"] = {"sha256": sha(gameplay.read_bytes())}
    if a.candidate:
        (a.destination / "TASK.md").write_text(TASK)
        receipt["task_sha256"] = sha(TASK.encode())
    print(json.dumps(receipt, indent=2))


def oracle(a):
    program = a.project / "Program.fs"
    before = sha(program.read_bytes()) if program.exists() else None
    shutil.copyfile(HERE / "OracleProgram.fs", program)
    print(json.dumps({"program_before_sha256": before, "oracle_program_sha256": sha(program.read_bytes())}, indent=2))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("tree")
    t.add_argument("archive", type=Path)
    t.add_argument("destination", type=Path)
    t.add_argument("--variant", choices=("E", "W"), required=True)
    t.add_argument("--candidate", action="store_true")
    o = sub.add_parser("oracle")
    o.add_argument("project", type=Path)
    a = ap.parse_args()
    tree(a) if a.cmd == "tree" else oracle(a)


if __name__ == "__main__":
    main()
