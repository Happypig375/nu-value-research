# Keyboard input and release timing on Vulkan-era Nu (reference re-run)

A port of the 2 November keyboard input and key-release checks to standalone MMCC Breakout at Nu master `47ef39e`, run with Vulkan on the NVIDIA GPU and judged from screenshots only. It is a new experiment; its timings are valid only on this server and configuration. The protocol and the results are in [docs/nu-vulkan-timing-reference-2026-11-03.md](../../docs/nu-vulkan-timing-reference-2026-11-03.md), part 2.

```bash
python3 -I ../nu-vulkan-r06-recovery-cost/prepare.py .artifacts/vulkan-timing-20261103/nu-47ef39e.tar $S/src-game --no-bridge
NUGET_PACKAGES=$S/nuget scripts/linux_nu_vulkan_env.sh $S build -- dotnet build "$S/src-game/Projects/Breakout Mmcc/Breakout Mmcc.fsproj" -c Release
python3 -I series.py "$S/src-game/Projects/Breakout Mmcc/bin/Release/net10.0" RUNS
python3 -I summarize.py RUNS --out RUNS/summary.json
```

Required Notice: Copyright (C) Bryan Edds. Nu is licensed under the [Nu Game Engine Noncommercial License](https://github.com/bryanedds/Nu/blob/master/License.md).
