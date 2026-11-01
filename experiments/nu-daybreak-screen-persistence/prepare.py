"""Install the reviewed, narrow observer bridge in an isolated pinned Gaia export.

Byte-identical bridge text to experiments/nu-history-b0/prepare.py (the reviewed
B0/B1/R04 instrumentation). Additionally verifies the archive SHA-256 and
extracts it when the source directory is missing.

Required Notice:
Copyright (C) Bryan Edds.
Gaia is licensed under the Nu Game Engine Noncommercial License.
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

parser = argparse.ArgumentParser()
parser.add_argument("source", type=Path)
parser.add_argument("archive", type=Path)
args = parser.parse_args()
source = args.source.resolve()
archive = args.archive.resolve()

archive_bytes = archive.read_bytes()
archive_hash = hashlib.sha256(archive_bytes).hexdigest()
if archive_hash != ARCHIVE_SHA256:
    raise SystemExit(f"Archive SHA-256 mismatch: {archive_hash}")

relative = "Nu/Nu.Gaia/Gaia.fs"
with tarfile.open(fileobj=io.BytesIO(archive_bytes)) as tf:
    if tf.pax_headers.get("comment") != COMMIT:
        raise SystemExit("Archive does not identify the selected Nu commit")
    original = tf.extractfile(relative).read()
    if not source.exists():
        source.mkdir(parents=True)
        tf.extractall(source)

target = source / relative
if target.read_bytes() != original:
    raise SystemExit("Gaia source differs from archive; refusing to overwrite it")
body = original.decode("utf-8-sig")
anchor = "    let rec private runWithCleanUpAndErrorProtection firstFrame world ="
bridge = """    // Research-only instrumentation. No application or engine update logic changes.
    let mutable private researchPostProcess : World -> unit = ignore
    let mutable private researchCheckpoint : WorldState option = None

    let setResearchPostProcess callback = researchPostProcess <- callback

    let researchSnapshot (world : World) =
        if world.Imperative || world.Advancing then
            invalidOp "Research checkpoint must be functional and halted."
        snapshot RestorePoint world
        researchCheckpoint <- Some (snd (List.head Pasts))

    let researchUndo (world : World) =
        match researchCheckpoint, Pasts with
        | Some expected, (RestorePoint, actual) :: _ when Object.ReferenceEquals (expected, actual) ->
            tryUndo world
        | _ -> invalidOp "Research checkpoint is not the next Gaia undo target."

    let private imGuiPostProcessWithResearch world =
        imGuiPostProcess world
        researchPostProcess world

"""
call = "World.runWithoutCleanUp tautology ignore ignore imGuiRender imGuiProcess imGuiPostProcess firstFrame world"
if body.count(anchor) != 1 or body.count(call) != 1:
    raise SystemExit("Unexpected Gaia implementation; bridge anchors are not unique")
body = body.replace(anchor, bridge + anchor).replace(
    call, call.replace("imGuiPostProcess firstFrame", "imGuiPostProcessWithResearch firstFrame")
)
if not body.endswith("\n"):
    body += "\n"
target.write_text(body, encoding="utf-8", newline="")
receipt = {
    "file": relative,
    "archive_sha256": archive_hash,
    "commit": COMMIT,
    "original_sha256": hashlib.sha256(original).hexdigest(),
    "instrumented_sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
    "application_sources_modified": False,
}
print(json.dumps(receipt, indent=2))
