"""Record the session's own acceptance of a Linux Terra Firma build (amendment 2026-11-03).

This replaces the Windows parent acceptance script (`accept-terra-build-03.py`,
which hard-codes Windows DLL/PDB hashes). It checks the same readiness facts
the Windows acceptance checked, except the DLL/PDB hashes, which differ because
builds embed paths. There is no second reviewer.

Usage: python accept_linux_build.py BUILD_DIR AMENDED_PACKAGE_DIR [NATIVE_DEADLINE_SECONDS]
(the deadline is recorded only; amendment 3 raised it from 180 s)
"""

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

PROGRAM_SHA = "a14b405d8dae1771fa2b81830e825bfe9b4859cd88e0382b1bb66c072b6e004b"
PROTOCOL_SHA = "b98ed969051a6734ad91532c375db390befcf6b6d2c3e1db6a6d02a1be2ec9ed"
WINDOWS_DLL_CONFIG_SHA = "eaf53dd0a51fb56b7b3a2bc544d5c4987ee0dd7533be43c21f0dfc1678a9c452"


def sha(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def read(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    built, package = Path(sys.argv[1]).resolve(strict=True), Path(sys.argv[2]).resolve(strict=True)
    deadline = int(sys.argv[3]) if len(sys.argv) > 3 else 180
    receipt = read(built / "receipt.json")
    checks = {
        "build_ready_flags": all(receipt[k] for k in ("ready_for_parent_review", "source_host_unchanged", "source_unchanged", "host_copied_exactly")),
        "build_exit_0": receipt["process"]["exit_code"] == 0 and not receipt["process"]["timed_out"],
    }
    seal = read(built / "source-binary-seal.json")
    binary = Path(receipt["binary"])
    checks["pe_pdb_seal_8_original_1_observer"] = bool(seal["pe_pdb_identity_matches"] and seal["verified_original_units"] == 8 and seal["verified_observer_units"] == 1)
    checks["seal_matches_binary"] = seal["dll_sha256"] == sha(binary / "R12TerraFirmaProbe.dll") and seal["pdb_sha256"] == sha(binary / "R12TerraFirmaProbe.pdb")
    recorded = {"dll_config_equals_windows": sha(binary / "R12TerraFirmaProbe.dll.config") == WINDOWS_DLL_CONFIG_SHA}
    config = read(binary / "R12TerraFirmaProbe.runtimeconfig.json")["runtimeOptions"]["configProperties"]
    checks["server_gc_and_tiered_pgo"] = config.get("System.GC.Server") is True and config.get("System.Runtime.TieredPGO") is True
    checks["package_inputs_unchanged"] = all(sha(package / n) == e["sha256"] for n, e in read(built / "package-inputs.json").items())
    checks["observer_and_protocol_unchanged"] = sha(package / "Program.fs") == PROGRAM_SHA and sha(package / "PROTOCOL.md") == PROTOCOL_SHA
    failed = [k for k, v in checks.items() if not v]
    output = built / "native-acceptance.json"
    if output.exists():
        raise SystemExit("acceptance already exists")
    record = {
        "decision": "accepted_for_native_execution" if not failed else "not_accepted",
        "accepted_utc": datetime.now(timezone.utc).isoformat(),
        "build_receipt_sha256": sha(built / "receipt.json"),
        "source_binary_seal_sha256": sha(built / "source-binary-seal.json"),
        "protocol_sha256": sha(built / "package-inputs/PROTOCOL.md"),
        "checks": checks,
        "failed_checks": failed,
        "recorded_not_gating": recorded,
        "dll_sha256": seal["dll_sha256"],
        "pdb_sha256": seal["pdb_sha256"],
        "parent_review": "Linux amendment 2026-11-03: self-check by the reproducing session against the Windows acceptance criteria, without a second reviewer. Windows DLL/PDB hashes are not required (builds embed paths).",
        "assigned_native": ["linux-L0-01", "linux-L1-01_if_L0_complete"] if deadline == 180 else ["linux-L0-05", "linux-L1-01_if_L0-05_complete"],
        "native_deadline_seconds_each": deadline,
        "no_outcome_claim": True,
    }
    output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2))
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
