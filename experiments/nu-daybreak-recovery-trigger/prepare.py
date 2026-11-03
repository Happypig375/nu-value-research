"""Prepare one pinned Nu source tree for the branch A recovery-trigger check.

Extracts the pinned archive into a new directory, installs the read-only Gaia
observer bridge, and (with --fault) adds the two-line deliberate test fault to
Breakout Mmcc's Gameplay.fs. Nothing else is changed. Prints a JSON receipt.

Protocol: docs/nu-daybreak-recovery-trigger-2026-11-03.md, section 4.
"""

import argparse
import hashlib
import json
from pathlib import Path
import tarfile

COMMIT = "064f7ae92a8506689cd91aff5e6804a375d6ef3d"
ARCHIVE_SHA256 = "eb0aa77197de1971d79aa0657c2af5cf33b99ba8302a24ba44f3306cca4bf92b"
GAIA = "Nu/Nu.Gaia/Gaia.fs"
GAMEPLAY = "Projects/Breakout Mmcc/Gameplay.fs"

BRIDGE_ANCHOR = "    let rec private runWithCleanUpAndErrorProtection firstFrame world ="
BRIDGE = """    // Research-only observer bridge (branch A recovery-trigger check). Read-only accessors plus
    // Gaia's own ordinary Advance route; no recovery, undo, switch or update logic is changed.
    let mutable private researchPostProcess : World -> unit = ignore
    let setResearchPostProcess callback = researchPostProcess <- callback
    let researchToggleAdvancing (world : World) = toggleAdvancing world
    let researchPastsCount () = List.length Pasts
    let researchFuturesCount () = List.length Futures
    let researchPastsHeadState () = match Pasts with (_, state) :: _ -> Some state | [] -> None
    let researchPastsHeadIsAdvance () = match Pasts with (Advance, _) :: _ -> true | _ -> false
    let researchMessageBox () = MessageBoxOpt

    let private imGuiPostProcessWithResearch world =
        imGuiPostProcess world
        researchPostProcess world

"""
RUN_CALL = "World.runWithoutCleanUp tautology ignore ignore imGuiRender imGuiProcess imGuiPostProcess firstFrame world"

FAULT_ANCHOR = "        | Update ->\n            let gameplay = Gameplay.update gameplay world\n"
FAULT = ("        | Update ->\n"
         "            let rampCountdown = 30L - gameplay.GameplayTime // DELIBERATE TEST FAULT (research)\n"
         "            let _ = 100L / rampCountdown\n"
         "            let gameplay = Gameplay.update gameplay world\n")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def edit(path, anchor, replacement, label):
    raw = path.read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig")
    crlf = "\r\n" in text
    body = text.replace("\r\n", "\n")
    if body.count(anchor) != 1:
        raise SystemExit(f"{label}: anchor is not unique in {path}")
    body = body.replace(anchor, replacement)
    if crlf:
        body = body.replace("\n", "\r\n")
    out = (b"\xef\xbb\xbf" if bom else b"") + body.encode("utf-8")
    path.write_bytes(out)
    return {"file": str(path), "original_sha256": sha(raw), "edited_sha256": sha(out), "crlf": crlf, "bom": bom}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("destination", type=Path, help="new, empty directory")
    parser.add_argument("--fault", action="store_true", help="add the deliberate test fault")
    args = parser.parse_args()
    archive_bytes = args.archive.read_bytes()
    if sha(archive_bytes) != ARCHIVE_SHA256:
        raise SystemExit("archive hash differs from the pinned archive")
    dest = args.destination
    if dest.exists() and any(dest.iterdir()):
        raise SystemExit("destination must be new or empty")
    dest.mkdir(parents=True, exist_ok=True)
    with tarfile.open(args.archive) as tar:
        if tar.pax_headers.get("comment") != COMMIT:
            raise SystemExit("archive does not identify the pinned Nu commit")
        tar.extractall(dest, filter="data")
    receipt = {"archive_sha256": ARCHIVE_SHA256, "commit": COMMIT, "fault": args.fault}
    gaia = dest / GAIA
    body = gaia.read_bytes().decode("utf-8-sig")
    if body.count(RUN_CALL) != 1:
        raise SystemExit("Gaia run call is not unique")
    receipt["bridge"] = edit(gaia, BRIDGE_ANCHOR, BRIDGE + BRIDGE_ANCHOR, "bridge")
    receipt["bridge_call"] = edit(gaia, RUN_CALL, RUN_CALL.replace("imGuiPostProcess firstFrame", "imGuiPostProcessWithResearch firstFrame"), "bridge call")
    gameplay = dest / GAMEPLAY
    if args.fault:
        receipt["fault_edit"] = edit(gameplay, FAULT_ANCHOR, FAULT, "fault")
    else:
        receipt["gameplay_sha256_unchanged"] = sha(gameplay.read_bytes())
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
