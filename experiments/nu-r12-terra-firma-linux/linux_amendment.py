"""Linux amendment 2026-11-03 for the R12 Terra Firma load/save/reopen package.

Copies the committed package `experiments/nu-r12-terra-firma/` into a NEW scratch
tree that keeps the repository layout, checks every original file hash, then
makes exactly the declared text replacements in run.py. The committed package
is never written.

Declared replacements (see docs/nu-r12-terra-firma-linux-amended-2026-11-03.md):
  run.py asset closure: the Windows FILE_ATTRIBUTE_READONLY flag is replaced by
         file mode as the read-only signal (no write bit for owner, group or other).
  run.py L1 scene replacement records: `st_file_attributes` (absent on Linux, so
         the L1 stage would crash with AttributeError) is read with getattr(..., None).

Amendment 3 (3 November 2026, user-approved NEEDS-HUMAN item 9): with
`--deadline SECONDS`, the native run stage's per-process deadline in run.py
(`process(command, app, output, 180, environment)`, line 366) is raised to SECONDS.
Without the option the output is exactly the amendment-1 copy.

Usage: python linux_amendment.py REPO_ROOT NEW_SCRATCH_ROOT [--deadline SECONDS]
"""

import hashlib
import json
import shutil
import sys
from pathlib import Path

PACKAGE = "experiments/nu-r12-terra-firma"
ORIGINALS = {
    ".gitattributes": "dd17d5a3bc18af909677783d1eb743b025898be0c002f7a17cc75177a8b4f9bc",
    "PROTOCOL.md": "b98ed969051a6734ad91532c375db390befcf6b6d2c3e1db6a6d02a1be2ec9ed",
    "Program.fs": "a14b405d8dae1771fa2b81830e825bfe9b4859cd88e0382b1bb66c072b6e004b",
    "R12TerraFirmaProbe.fsproj": "f53414f36deed176811039e8c1a012b915fe5f7616b6a0a88b4d34b6cf3ddac8",
    "README.md": "a526ccf35b19ac5fc6ccf565de99d602fb06a606a30707589dd90d0870c97bbf",
    "check_controls.py": "792e2bbf4f2fcbaacbe0e6aa313f8b01d46bf9618cef4c4054741c06041ecc91",
    "compare.py": "130d7ff863721e01b058494046a218c74ff04825e056e490ede1d722ac229e9b",
    "execution-receipt.json": "d742be6452622c2ad70cbb0c4642dd234d9167f044daeaac58b01dab78f21792",
    "global.json": "1e23a26d555754d3c37fcf4fc27e0633e0e7b2c24e041f30c3d053227936a5cc",
    "run.py": "367e0ae4924e1a1d0b71fe408362423d4a4f1423795da67b11a68ca84e71201a",
}

REPLACEMENTS = {
    "run.py": [
        (
            "        if not (published_attrs[relative]['windows_attributes'] or 0) & stat.FILE_ATTRIBUTE_READONLY:\n",
            "        if published_attrs[relative]['mode'] & (stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH):  # Linux amendment 2026-11-03\n",
            1,
        ),
        (
            "'windows_attributes': (app / SCENE).stat().st_file_attributes})\n",
            "'windows_attributes': getattr((app / SCENE).stat(), 'st_file_attributes', None)})  # Linux amendment 2026-11-03\n",
            2,
        ),
    ],
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    argv = sys.argv[1:]
    deadline = None
    if "--deadline" in argv:
        index = argv.index("--deadline")
        deadline = int(argv[index + 1])
        del argv[index:index + 2]
        if deadline <= 180:
            raise SystemExit("amendment 3 only raises the 180 s deadline")
        REPLACEMENTS["run.py"].append((
            "    result = process(command, app, output, 180, environment)\n",
            f"    result = process(command, app, output, {deadline}, environment)  # Linux amendment 3, 2026-11-03\n",
            1,
        ))
    repo, scratch = Path(argv[0]).resolve(strict=True), Path(argv[1]).resolve()
    if scratch.exists():
        raise SystemExit("scratch root must be new")
    source = repo / PACKAGE
    target = scratch / PACKAGE
    target.mkdir(parents=True)
    receipt = {"schemaVersion": 1, "amendment": "linux-2026-11-03" + (f"+deadline-{deadline}" if deadline else ""), "source": str(source), "target": str(target), "files": {}}
    for name, expected in ORIGINALS.items():
        if sha(source / name) != expected:
            raise SystemExit(f"original {name} differs from the committed package")
        shutil.copy2(source / name, target / name)
    for name, triples in REPLACEMENTS.items():
        path = target / name
        text = path.read_bytes().decode("utf-8")
        newline = "\r\n" if "\r\n" in text else "\n"
        for old, new, count in triples:
            old_n, new_n = old.replace("\n", newline), new.replace("\n", newline)
            if text.count(old_n) != count:
                raise SystemExit(f"anchor not found exactly {count} time(s) in {name}: {old!r}")
            text = text.replace(old_n, new_n)
        path.write_bytes(text.encode("utf-8"))
    for name, expected in ORIGINALS.items():
        after = sha(target / name)
        receipt["files"][name] = {"originalSha256": expected, "amendedSha256": after, "changed": after != expected}
    changed = sorted(n for n, f in receipt["files"].items() if f["changed"])
    if changed != sorted(REPLACEMENTS):
        raise SystemExit(f"unexpected changed set {changed}")
    (scratch / "linux-amendment-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
