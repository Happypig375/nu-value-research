"""Prepare the Nu master (47ef39e) source tree for the Vulkan-era R06 recovery-cost port.

Extracts the pinned git-archive tar into a new folder (after checking its hash and commit), then installs the
research bridge into Gaia: the R03 B0 snapshot/undo bridge with R06's weak identity witness, ported to master's
names (TimeAdvancing; firstFrameCallbackOpt). No application, engine or other Gaia logic changes. Prints a receipt.
Protocol: docs/nu-vulkan-timing-reference-2026-11-03.md, part 1.
"""
import argparse
import hashlib
import json
from pathlib import Path
import tarfile

COMMIT = "47ef39e176424675f067c378c3a5f86f9c5ec3be"
ARCHIVE_SHA256 = "3dcae8b0c61103b12b215b631bcca96fc219bfced876e1d35753db348581faac"
GAIA = "Nu/Nu.Gaia/Gaia.fs"
ANCHOR = "    let rec private runWithCleanUpAndErrorProtection firstFrameCallbackOpt world ="
CALL = "World.runWithoutCleanUp tautology ignore ignore imGuiRender imGuiProcess imGuiPostProcess firstFrameCallbackOpt world"
BRIDGE = """    // Research-only instrumentation (R06 Vulkan-era port). No application or engine update logic changes.
    let mutable private researchPostProcess : World -> unit = ignore
    let mutable private researchCheckpoint : WeakReference<WorldState> option = None

    let setResearchPostProcess callback = researchPostProcess <- callback

    let researchSnapshot (world : World) =
        if world.Imperative || world.TimeAdvancing then
            invalidOp "Research checkpoint must be functional and halted."
        snapshot RestorePoint world
        researchCheckpoint <- Some (WeakReference<WorldState> (snd (List.head Pasts)))

    let researchUndo (world : World) =
        match researchCheckpoint, Pasts with
        | Some expectedWeak, (RestorePoint, actual) :: _ ->
            let mutable expected = Unchecked.defaultof<WorldState>
            if expectedWeak.TryGetTarget &expected && Object.ReferenceEquals (expected, actual)
            then tryUndo world
            else invalidOp "Research checkpoint is not the next Gaia undo target."
        | _ -> invalidOp "Research checkpoint is not the next Gaia undo target."

    let private imGuiPostProcessWithResearch world =
        imGuiPostProcess world
        researchPostProcess world

"""


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("destination", type=Path, help="new, empty directory")
    parser.add_argument("--no-bridge", action="store_true", help="extract only (standalone game builds)")
    args = parser.parse_args()
    archive = args.archive.read_bytes()
    if sha(archive) != ARCHIVE_SHA256:
        raise SystemExit("archive hash differs from the pinned archive")
    dest = args.destination
    if dest.exists() and any(dest.iterdir()):
        raise SystemExit("destination must be new or empty")
    dest.mkdir(parents=True, exist_ok=True)
    with tarfile.open(args.archive) as tar:
        if tar.pax_headers.get("comment") != COMMIT:
            raise SystemExit("archive does not identify the pinned Nu commit")
        tar.extractall(dest, filter="data")
    receipt = {"archive_sha256": ARCHIVE_SHA256, "commit": COMMIT, "bridge": not args.no_bridge}
    if not args.no_bridge:
        gaia = dest / GAIA
        raw = gaia.read_bytes()
        text = raw.decode("utf-8-sig")
        crlf = "\r\n" in text
        body = text.replace("\r\n", "\n")
        if body.count(ANCHOR) != 1 or body.count(CALL) != 1:
            raise SystemExit("Gaia bridge anchors are not unique")
        body = body.replace(ANCHOR, BRIDGE + ANCHOR).replace(
            CALL, CALL.replace("imGuiPostProcess firstFrameCallbackOpt", "imGuiPostProcessWithResearch firstFrameCallbackOpt"))
        if crlf:
            body = body.replace("\n", "\r\n")
        out = (b"\xef\xbb\xbf" if raw.startswith(b"\xef\xbb\xbf") else b"") + body.encode("utf-8")
        gaia.write_bytes(out)
        receipt["gaia_original_sha256"] = sha(raw)
        receipt["gaia_bridged_sha256"] = sha(out)
    receipt["gameplay_sha256"] = sha((dest / "Projects/Breakout Mmcc/Gameplay.fs").read_bytes())
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
