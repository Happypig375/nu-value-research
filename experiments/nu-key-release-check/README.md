# Key-release check, counted in game updates (new work, not the R02 input gate)

Follow-up to `experiments/nu-keyboard-input-check/`. It sends real X input (XTEST) to the unchanged standalone MMCC Breakout game and counts distinct rendered frames as game updates to tell display lag from a stuck key. Protocol and results: [docs/nu-key-release-check-2026-11-02.md](../../docs/nu-key-release-check-2026-11-02.md). It does not use or read the stopped `experiments/nu-r02-input-feasibility/` draft.

```bash
RUNS=/path/to/scratch   # outside the repo
python3 experiments/nu-keyboard-input-check/prepare.py $RUNS/source .artifacts/r03-feasibility-20261015/nu-064f7ae.tar
cp -r .artifacts/nuget-packages $RUNS/nuget
NU_DISPLAY=:95 NUGET_PACKAGES=$RUNS/nuget scripts/linux_nu_env.sh $RUNS build -- python3 experiments/nu-keyboard-input-check/build.py $RUNS/source
NU_DISPLAY=:95 scripts/linux_nu_env.sh $RUNS run-01 -- python3 -I experiments/nu-key-release-check/release_check.py \
  "$RUNS/source/Projects/Breakout Mmcc/bin/Release/net10.0" $RUNS/run-01
```

Required Notice: Copyright (C) Bryan Edds. Nu is licensed under the [Nu Game Engine Noncommercial License](https://github.com/bryanedds/Nu/blob/master/License.md).
