"""Warning record for one D9 direction 4 candidate (protocol section 4), from its saved tool log.

Usage: warnings.py CANDIDATE_ARTIFACT_DIR   (prints JSON; run only after the oracle validation has passed)
For each Bash tool result that looks like a build (contains "Build succeeded" or "error" lines from dotnet build),
records whether FS0025 (incomplete pattern match) appeared for Gameplay.fs. Also reports the final source's S1 arm.
"""
import json
from pathlib import Path
import re
import sys


def main():
    out = Path(sys.argv[1])
    uses, builds = {}, []
    for line in (out / "stream.jsonl").read_text().splitlines():
        try:
            rec = json.loads(line)
        except ValueError:
            continue
        for block in rec.get("message", {}).get("content", []) if isinstance(rec.get("message"), dict) else []:
            if block.get("type") == "tool_use" and block.get("name") == "Bash":
                uses[block["id"]] = block["input"].get("command", "")
            if block.get("type") == "tool_result" and block.get("tool_use_id") in uses:
                content = block.get("content")
                text = content if isinstance(content, str) else " ".join(c.get("text", "") for c in content or [] if isinstance(c, dict))
                command = uses[block["tool_use_id"]]
                if "dotnet build" in command or "dotnet msbuild" in command:
                    builds.append({"command": command[:200],
                                   "fs0025_gameplay": bool(re.search(r"Gameplay\.fs\(\d+,\d+\): warning FS0025", text)),
                                   "errors": len(re.findall(r": error ", text)),
                                   "succeeded": "Build succeeded" in text})
    final = (out / "final" / "Gameplay.fs").read_text(encoding="utf-8-sig")
    update = final[final.find("static member update"):final.find("// this is our gameplay MMCC message type")]
    arms = [l.strip() for l in update.splitlines() if l.strip().startswith("|")]
    record = {
        "builds": len(builds),
        "fs0025_seen": any(b["fs0025_gameplay"] for b in builds),
        "fs0025_cleared_later": any(b["fs0025_gameplay"] for b in builds) and not builds[-1]["fs0025_gameplay"],
        "last_build_succeeded": builds[-1]["succeeded"] if builds else None,
        "final_update_arms": arms,
        "final_has_catch_all_arm": any(re.match(r"\|\s*_\s*->", a) for a in arms),
        "final_lists_paused_in_update": any("Paused" in a for a in arms),
        "build_log": builds,
    }
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
