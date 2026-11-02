# Daybreak branch B: ordinary screen serializer export/import probe

This is an instrumented local feasibility experiment, not an agent task or a cost/benefit study. It asks whether a running gameplay screen's state can be saved through Nu's ordinary screen serializer (`World.writeScreenToFile`/`readScreenFromFile`) and reproduced in a fresh process, checked against the closed B0 checkpoint values. The protocol, source verification, policies and outcome check are fixed in [docs/nu-daybreak-screen-persistence-2026-11-02.md](../../docs/nu-daybreak-screen-persistence-2026-11-02.md); read it first. The results are appended there.

Harness: the same functional, halted Gaia Gameplay edit-mode setup as `experiments/nu-history-b0` with the same byte-identical research bridge (post-ImGui-postprocess callback only; the bridge's snapshot/undo members are unused). Application code is unchanged.

## Reproduction (Linux, this server)

Requires the per-user .NET SDK 10.0.302 and the pinned archive `.artifacts/r03-feasibility-20261015/nu-064f7ae.tar`. All state lives in a scratch runs root outside the repo (example: `/tmp/kimi-daybreak-20261102/runs`).

```bash
export DOTNET_ROOT=$HOME/.local/share/dotnet-sdk-10.0.302 PATH=$DOTNET_ROOT:$PATH DOTNET_MULTILEVEL_LOOKUP=0
python3 experiments/nu-daybreak-screen-persistence/prepare.py $RUNS/source .artifacts/r03-feasibility-20261015/nu-064f7ae.tar
python3 experiments/nu-daybreak-screen-persistence/build.py $RUNS/source $RUNS/build
experiments/nu-daybreak-screen-persistence/linux_run.sh $RUNS/source export 01 $RUNS
experiments/nu-daybreak-screen-persistence/linux_run.sh $RUNS/source import 01 $RUNS
experiments/nu-daybreak-screen-persistence/linux_run.sh $RUNS/source replace-nodestroy 01 $RUNS
python3 experiments/nu-daybreak-screen-persistence/compare.py $RUNS
```

**Corrected-import amendment** (adapted engine source, see the record's amendment section): run `python3 experiments/nu-daybreak-screen-persistence/apply_import_fix.py $RUNS/source .artifacts/r03-feasibility-20261015/nu-064f7ae.tar` after `prepare.py` and before `build.py`. It changes only line 309 of `Nu/Nu/World/WorldScreen.fs` (the same fix as upstream bryanedds/Nu#1466). Set `NUGET_PACKAGES` to a private copy of `.artifacts/nuget-packages/` for the build.

`export` requires an empty transfer directory (`$RUNS/transfer`); the import arms require the transfer file it writes. Every attempt must be preserved; rerun under a new `ATTEMPT_NN`, clearing the transfer directory only before a new export attempt.

Required Notice: Copyright (C) Bryan Edds. Nu and Gaia are licensed under the [Nu Game Engine Noncommercial License](https://github.com/bryanedds/Nu/blob/master/License.md).
