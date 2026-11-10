# D9 direction 1: three routes back to work after a game-code fault (package)

Compares Gaia's automatic rewind (H), an F7 restore point (F) and a screen checkpoint file plus restart (C) on Nu master `47ef39e`, with Vulkan on the NVIDIA GPU. The protocol and results are in [docs/nu-d9-recovery-routes-2026-11-10.md](../../docs/nu-d9-recovery-routes-2026-11-10.md).

```bash
python3 -I prepare.py .artifacts/vulkan-timing-20261103/nu-47ef39e.tar $S/src
NUGET_PACKAGES=$S/nuget scripts/linux_nu_vulkan_env.sh $S build -- dotnet build $S/pkg/Probe.fsproj -c Release -p:NuSource=$S/src
python3 -I series.py $S/pkg/bin/Release/net10.0/Probe.dll "$S/src/Projects/Breakout Mmcc/bin/Release/net10.0/Breakout Mmcc.dll" RUNS
python3 -I check.py RUNS --out RUNS/verdict.json
```

Required Notice: Copyright (C) Bryan Edds. Gaia and Nu are licensed under the [Nu Game Engine Noncommercial License](https://github.com/bryanedds/Nu/blob/master/License.md).
