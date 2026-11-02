"""Apply the one-line screen-import address fix to a prepared pinned Nu source tree.

Corrected-import amendment (docs/nu-daybreak-screen-persistence-2026-11-02.md,
"Amendment: corrected-import arms"). Run after prepare.py and before build.py.

The change is the same as upstream bryanedds/Nu#1466: in World.readScreen
(Nu/Nu/World/WorldScreen.fs, line 309 at 064f7ae) the imported screen is
addressed under the game, as World.createScreen4 already does. The script
refuses to run unless the file on disk is byte-identical to the archive copy,
the old line occurs exactly once, and it is on line 309. It changes nothing else.

Usage: apply_import_fix.py PREPARED_SOURCE ARCHIVE

Required Notice:
Copyright (C) Bryan Edds.
Nu is licensed under the Nu Game Engine Noncommercial License.
https://github.com/bryanedds/Nu/blob/master/License.md
"""
import argparse
import hashlib
import io
import json
import tarfile
from pathlib import Path

ARCHIVE_SHA256 = "eb0aa77197de1971d79aa0657c2af5cf33b99ba8302a24ba44f3306cca4bf92b"
COMMIT = "064f7ae92a8506689cd91aff5e6804a375d6ef3d"
RELATIVE = "Nu/Nu/World/WorldScreen.fs"
OLD = "            let screen = Screen (ntoa screenState.Name)\n"
NEW = "            let screen = Game.Handle / screenState.Name\n"
LINE = 309

parser = argparse.ArgumentParser()
parser.add_argument("source", type=Path)
parser.add_argument("archive", type=Path)
args = parser.parse_args()
archive_bytes = args.archive.resolve(strict=True).read_bytes()
archive_hash = hashlib.sha256(archive_bytes).hexdigest()
if archive_hash != ARCHIVE_SHA256:
    raise SystemExit(f"Archive SHA-256 mismatch: {archive_hash}")
with tarfile.open(fileobj=io.BytesIO(archive_bytes)) as tf:
    if tf.pax_headers.get("comment") != COMMIT:
        raise SystemExit("Archive does not identify the selected Nu commit")
    original = tf.extractfile(RELATIVE).read()

target = args.source.resolve(strict=True) / RELATIVE
if target.read_bytes() != original:
    raise SystemExit("WorldScreen.fs differs from the archive; refusing to patch it")
text = original.decode("utf-8")
newline = "\r\n" if "\r\n" in text else "\n"
old, new = OLD.replace("\n", newline), NEW.replace("\n", newline)
if text.count(old) != 1:
    raise SystemExit("Expected exactly one occurrence of the old readScreen line")
lines = text.splitlines(keepends=True)
if lines[LINE - 1] != old:
    raise SystemExit(f"Old line is not on line {LINE}")
lines[LINE - 1] = new
patched = "".join(lines).encode("utf-8")
target.write_bytes(patched)
changed = [i + 1 for i, (a, b) in enumerate(zip(original.decode("utf-8").splitlines(), patched.decode("utf-8").splitlines())) if a != b]
receipt = {
    "file": RELATIVE,
    "archive_sha256": archive_hash,
    "commit": COMMIT,
    "original_sha256": hashlib.sha256(original).hexdigest(),
    "patched_sha256": hashlib.sha256(patched).hexdigest(),
    "changed_lines": changed,
    "line_count_unchanged": len(original.splitlines()) == len(patched.splitlines()),
    "upstream_reference": "bryanedds/Nu#1466",
}
if changed != [LINE] or not receipt["line_count_unchanged"]:
    raise SystemExit(f"Unexpected change set: {receipt}")
print(json.dumps(receipt, indent=2))
