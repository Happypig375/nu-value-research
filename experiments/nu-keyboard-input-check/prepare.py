"""Extract the pinned Nu archive, unchanged, into a new directory.

Keyboard input check (docs/nu-keyboard-input-check-2026-11-02.md). This is new
work, separate from the stopped R02 input-construction gate; it uses none of
that draft. Usage: prepare.py NEW_SOURCE_DIR ARCHIVE

Required Notice: Copyright (C) Bryan Edds. Nu is licensed under the Nu Game
Engine Noncommercial License. https://github.com/bryanedds/Nu/blob/master/License.md
"""
import argparse
import hashlib
import json
import tarfile
from pathlib import Path

ARCHIVE_SHA256 = "eb0aa77197de1971d79aa0657c2af5cf33b99ba8302a24ba44f3306cca4bf92b"
COMMIT = "064f7ae92a8506689cd91aff5e6804a375d6ef3d"

parser = argparse.ArgumentParser()
parser.add_argument("source", type=Path)
parser.add_argument("archive", type=Path)
args = parser.parse_args()
source = args.source.resolve()
if source.exists():
    raise SystemExit("source directory must not exist")
digest = hashlib.sha256()
with args.archive.open("rb") as handle:
    for block in iter(lambda: handle.read(1 << 20), b""):
        digest.update(block)
if digest.hexdigest() != ARCHIVE_SHA256:
    raise SystemExit(f"Archive SHA-256 mismatch: {digest.hexdigest()}")
with tarfile.open(args.archive) as tf:
    if tf.pax_headers.get("comment") != COMMIT:
        raise SystemExit("Archive does not identify the selected Nu commit")
    source.mkdir(parents=True)
    tf.extractall(source)
game = source / "Projects/Breakout Mmcc"
print(json.dumps({
    "archive_sha256": ARCHIVE_SHA256,
    "commit": COMMIT,
    "source_modified": False,
    "program_fs_sha256": hashlib.sha256((game / "Program.fs").read_bytes()).hexdigest(),
    "gameplay_fs_sha256": hashlib.sha256((game / "Gameplay.fs").read_bytes()).hexdigest(),
    "app_config_sha256": hashlib.sha256((game / "App.config").read_bytes()).hexdigest(),
}, indent=2))
