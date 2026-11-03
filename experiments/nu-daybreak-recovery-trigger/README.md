# Branch A: deliberate recovery fault trigger (package)

**What this tests:** whether Gaia (Nu's editor) recovers when the game's own code throws an exception, and what that recovery gives back. The exception is a deliberate division by zero in Breakout's `Update` handler. The protocol, the source check and the results are in [docs/nu-daybreak-recovery-trigger-2026-11-03.md](../../docs/nu-daybreak-recovery-trigger-2026-11-03.md).

Files:
- `prepare.py` extracts the pinned Nu archive into a new folder after checking its hash and commit. It installs a read-only observer bridge into Gaia, and with `--fault` adds the two fault lines to `Gameplay.fs`. It prints a receipt.
- `Probe.fs` / `Probe.fsproj` start real Gaia with Breakout Mmcc in Gameplay edit mode and record observations at Gaia's post-ImGui hook. Arms `a0`, `a1` and `a2` are defined in protocol section 4.1.
- `run.py` runs one arm with a 600 s deadline and keeps stdout/stderr, the trace and a process receipt.
- `check.py` applies the pass/fail conditions of section 4.4.

Linux commands (see `scripts/linux_nu_env.sh`; build in scratch, never in the checkout):

```bash
python prepare.py nu-064f7ae.tar SRC_NOFAULT          # A0 tree
python prepare.py nu-064f7ae.tar SRC_FAULT --fault    # A1/A2 tree
dotnet build PKG/Probe.fsproj -c Release -p:NuSource=SRC -p:SourceRevisionId=064f7ae92a8506689cd91aff5e6804a375d6ef3d
python run.py a1 "SRC_FAULT/Projects/Breakout Mmcc/bin/Release/net10.0/Breakout Mmcc.dll" OUT/a1-01 --probe PKG/bin/Release/net10.0/Probe.dll
python check.py --a0 OUT/a0-01 --a1 OUT/a1-01 --a2 OUT/a2-01 --out OUT/verdict.json
```

Required Notice: Copyright (C) Bryan Edds. Gaia and Nu are licensed under the [Nu Game Engine Noncommercial License](https://github.com/bryanedds/Nu/blob/master/License.md).
