"""Linux amendment 2026-11-03 for the R10 initializer-only schema reload package.

Copies the committed package `experiments/nu-r10-schema-reload/` (plus its frozen
contract and clarification) into a NEW scratch tree that keeps the repository
layout, checks every original file hash, then makes exactly the declared text
replacements below. The committed package is never written.

Declared replacements (see docs/nu-r10-schema-reload-linux-reproduction-2026-11-03.md):
  seal_build.py      toolchain platform check: Windows/win-x64 -> Linux/ubuntu/linux-x64
  compare.py         trace OS check: "Windows" substring -> "Ubuntu" substring
  objective_checks.py synthetic fixture OS and the wrong-OS control value swapped

Usage: python linux_amendment.py REPO_ROOT NEW_SCRATCH_ROOT
Writes NEW_SCRATCH_ROOT/experiments/nu-r10-schema-reload/ and
NEW_SCRATCH_ROOT/linux-amendment-receipt.json.
"""

import hashlib
import json
import shutil
import sys
from pathlib import Path

PACKAGE = "experiments/nu-r10-schema-reload"
ORIGINALS = {
    "README.md": "af1f77f3238154ae58e199f40246216b17c1ad802b426ac2f21f6930893b4a05",
    "SchemaReload.fs": "76f942e7947c1bfc9a45c848edccfda3ee222669a69f094a8b66870243784ee8",
    "SchemaReload.fsproj": "f11da3e50cd4cc08b348276eddbec91389991a98d5abe6d9aee6b225d0dde47b",
    "compare.py": "19989e9799a6e5bae0a90da2bae041db6280f0f2ed44bb35812ad204601800d5",
    "objective_checks.py": "0b8e84d6837058b5890698cae4d0fedaa60fdbcf3af5098a54c29aa1e2d25629",
    "oracle.json": "327d804d8d780f70894476267f0995554764798309b6a5fa1b88c1fe69b1cb2c",
    "pre-execution-contract.md": "4c6bc39e4927c593f14026373d8e1a147a721c15dc1228a260c1643cf0006076",
    "prepare.py": "48f024449d9e7051db2574d6e1c344ca1e0cd9a1000466d7c883722f1e1068f6",
    "protocol-amendment-01.md": "8ac641cedeb4d130773d70e8367e3effb285f1a6f670f1ca8975ad284a5a8465",
    "run.py": "2ca150b216a0ce248bdf18b839504fefdab3d0e60cf4eb94c97aa53fa5d9dd81",
    "schema_edit.py": "0c6a8b56c9adce1565416e66a5e69c368f440f99e92983ab57b5bc4566add747",
    "seal_build.py": "ca95441ba0d3054d72d66f5ddc346b03cb2dc4177c37e3b2b8c42a5497b775a9",
    "source_manifest.py": "56b7ef0e08b488eafd3dd4bacd4240fb9f58aceb40c6ca0b9f3995d8eacdba12",
}

REPLACEMENTS = {
    "seal_build.py": [
        (
            '    if result["os"]["system"] != "Windows" or result["os"]["dotnetName"] != "Windows":\n'
            '        raise ValueError("frozen probe requires Windows")\n'
            '    if result["architecture"]["machine"].upper() not in ("AMD64", "X86_64") or result["architecture"]["rid"] != "win-x64":\n'
            '        raise ValueError("frozen probe requires Windows x64")\n',
            '    # Linux amendment 2026-11-03: the frozen platform is this Ubuntu x64 server.\n'
            '    if result["os"]["system"] != "Linux" or result["os"]["dotnetName"] != "ubuntu":\n'
            '        raise ValueError("amended probe requires Linux (ubuntu)")\n'
            '    if result["architecture"]["machine"].upper() not in ("AMD64", "X86_64") or result["architecture"]["rid"] != "linux-x64":\n'
            '        raise ValueError("amended probe requires Linux x64")\n',
        ),
    ],
    "compare.py": [
        (
            '    if not isinstance(configuration.get("os"), str) or "Windows" not in configuration["os"]:\n',
            '    if not isinstance(configuration.get("os"), str) or "Ubuntu" not in configuration["os"]:  # Linux amendment 2026-11-03\n',
        ),
    ],
    "objective_checks.py": [
        (
            '            "os": "Microsoft Windows 10.0.19045",\n',
            '            "os": "Ubuntu 22.04.5 LTS",  # Linux amendment 2026-11-03\n',
        ),
        (
            '        ("os", "Linux", "wrong-os"),\n',
            '        ("os", "Microsoft Windows 10.0.19045", "wrong-os"),  # Linux amendment 2026-11-03\n',
        ),
    ],
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    repo, scratch = Path(sys.argv[1]).resolve(strict=True), Path(sys.argv[2]).resolve()
    if scratch.exists():
        raise SystemExit("scratch root must be new")
    source = repo / PACKAGE
    target = scratch / PACKAGE
    target.mkdir(parents=True)
    receipt = {"schemaVersion": 1, "amendment": "linux-2026-11-03", "source": str(source), "target": str(target), "files": {}}
    for name, expected in ORIGINALS.items():
        if sha(source / name) != expected:
            raise SystemExit(f"original {name} differs from the committed package")
        shutil.copy2(source / name, target / name)
    for name, pairs in REPLACEMENTS.items():
        path = target / name
        raw = path.read_bytes()
        text = raw.decode("utf-8")
        newline = "\r\n" if "\r\n" in text else "\n"
        for old, new in pairs:
            old_n, new_n = old.replace("\n", newline), new.replace("\n", newline)
            if text.count(old_n) != 1:
                raise SystemExit(f"anchor not found exactly once in {name}: {old!r}")
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
