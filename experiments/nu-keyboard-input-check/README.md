# Keyboard input check (new work, not the R02 input gate)

Sends real X input (XTEST) to the unchanged standalone MMCC Breakout game and judges the result from screenshots only. The protocol and results are in [docs/nu-keyboard-input-check-2026-11-02.md](../../docs/nu-keyboard-input-check-2026-11-02.md). This package does not use or read the stopped `experiments/nu-r02-input-feasibility/` draft.

```bash
RUNS=/path/to/scratch   # outside the repo
python3 experiments/nu-keyboard-input-check/prepare.py $RUNS/source .artifacts/r03-feasibility-20261015/nu-064f7ae.tar
cp -r .artifacts/nuget-packages $RUNS/nuget
NUGET_PACKAGES=$RUNS/nuget scripts/linux_nu_env.sh $RUNS build -- python3 experiments/nu-keyboard-input-check/build.py $RUNS/source
NU_DISPLAY=:95 scripts/linux_nu_env.sh $RUNS run-01 -- python3 -I experiments/nu-keyboard-input-check/input_check.py \
  "$RUNS/source/Projects/Breakout Mmcc/bin/Release/net10.0" $RUNS/run-01
```

Required Notice: Copyright (C) Bryan Edds. Nu is licensed under the [Nu Game Engine Noncommercial License](https://github.com/bryanedds/Nu/blob/master/License.md).
