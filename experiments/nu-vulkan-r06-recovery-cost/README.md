# R06 recovery cost on Vulkan-era Nu (reference re-run)

A port of `experiments/nu-r06-recovery-cost/` to Nu master `47ef39e`, run with Vulkan on the NVIDIA GPU. It is a new experiment; its timings are valid only on this server and configuration. The protocol, the port changes and the results are in [docs/nu-vulkan-timing-reference-2026-11-03.md](../../docs/nu-vulkan-timing-reference-2026-11-03.md), part 1.

```bash
S=/path/to/scratch   # outside the repo
python3 -I prepare.py .artifacts/vulkan-timing-20261103/nu-47ef39e.tar $S/src
NUGET_PACKAGES=$S/nuget scripts/linux_nu_vulkan_env.sh $S build -- dotnet build $S/pkg/RecoveryCost.fsproj -c Release -p:NuSource=$S/src
python3 -I series.py $S/pkg/bin/Release/net10.0/RecoveryCost.dll "$S/src/Projects/Breakout Mmcc/bin/Release/net10.0/Breakout Mmcc.dll" experiments/nu-history-b1/checkpoint RUNS
python3 -I summarize.py RUNS --out RUNS/summary.json
```

Required Notice: Copyright (C) Bryan Edds. Gaia and Nu are licensed under the [Nu Game Engine Noncommercial License](https://github.com/bryanedds/Nu/blob/master/License.md).
