"""Prepare Nu master 47ef39e for the D9 recovery-routes comparison (direction 1).

Extracts the pinned git-archive tar (hash and commit checked) into a new folder, installs a read-only Gaia
observer bridge (plus Gaia's own Advance and F7 functions), and adds the two-line deliberate test fault
(division by zero when the gameplay clock reaches 30) to Breakout Mmcc's Update handler. Nothing else changes.
Protocol: docs/nu-d9-recovery-routes-2026-11-10.md.
"""
import argparse
import hashlib
import json
from pathlib import Path
import tarfile

COMMIT = "47ef39e176424675f067c378c3a5f86f9c5ec3be"
ARCHIVE_SHA256 = "3dcae8b0c61103b12b215b631bcca96fc219bfced876e1d35753db348581faac"
GAIA = "Nu/Nu.Gaia/Gaia.fs"
GAMEPLAY = "Projects/Breakout Mmcc/Gameplay.fs"
ANCHOR = "    let rec private runWithCleanUpAndErrorProtection firstFrameCallbackOpt world ="
CALL = "World.runWithoutCleanUp tautology ignore ignore imGuiRender imGuiProcess imGuiPostProcess firstFrameCallbackOpt world"
BRIDGE = """    // Research-only observer bridge (D9 recovery routes). Read-only accessors plus Gaia's own ordinary Advance (F5)
    // and restore point (F7) functions. No recovery, undo, switch or update logic is changed.
    let mutable private researchPostProcess : World -> unit = ignore
    let setResearchPostProcess callback = researchPostProcess <- callback
    let researchToggleAdvancing (world : World) = toggleTimeAdvancing world
    let researchCreateRestorePoint (world : World) = createRestorePoint world
    let researchPastsCount () = List.length Pasts
    let researchFuturesCount () = List.length Futures
    let researchPastsHeadKind () = match Pasts with (kind, _) :: _ -> string kind | [] -> ""
    let researchMessageBox () = MessageBoxOpt

    let private imGuiPostProcessWithResearch world =
        imGuiPostProcess world
        researchPostProcess world

"""
FAULT_ANCHOR = "        | Update ->\n            let gameplay = Gameplay.update gameplay world\n"
FAULT = ("        | Update ->\n"
         "            let rampCountdown = 30L - gameplay.GameplayTime // DELIBERATE TEST FAULT (research)\n"
         "            let _ = 100L / rampCountdown\n"
         "            let gameplay = Gameplay.update gameplay world\n")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def edit(path, pairs):
    raw = path.read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig")
    crlf = "\r\n" in text
    body = text.replace("\r\n", "\n")
    for old, new in pairs:
        if body.count(old) != 1:
            raise SystemExit(f"anchor not unique in {path}: {old[:60]!r}")
        body = body.replace(old, new)
    if crlf:
        body = body.replace("\n", "\r\n")
    out = (b"\xef\xbb\xbf" if bom else b"") + body.encode("utf-8")
    path.write_bytes(out)
    return {"original_sha256": sha(raw), "edited_sha256": sha(out)}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("archive", type=Path)
    ap.add_argument("destination", type=Path)
    a = ap.parse_args()
    if sha(a.archive.read_bytes()) != ARCHIVE_SHA256:
        raise SystemExit("archive hash differs from the pinned archive")
    if a.destination.exists() and any(a.destination.iterdir()):
        raise SystemExit("destination must be new or empty")
    a.destination.mkdir(parents=True, exist_ok=True)
    with tarfile.open(a.archive) as tar:
        if tar.pax_headers.get("comment") != COMMIT:
            raise SystemExit("archive does not identify the pinned Nu commit")
        tar.extractall(a.destination, filter="data")
    receipt = {"archive_sha256": ARCHIVE_SHA256, "commit": COMMIT}
    receipt["gaia"] = edit(a.destination / GAIA, [(ANCHOR, BRIDGE + ANCHOR),
        (CALL, CALL.replace("imGuiPostProcess firstFrameCallbackOpt", "imGuiPostProcessWithResearch firstFrameCallbackOpt"))])
    receipt["gameplay_fault"] = edit(a.destination / GAMEPLAY, [(FAULT_ANCHOR, FAULT)])
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
