# R10 schema reload on Linux, under a declared amendment (3 November 2026)

**Status: protocol fixed before any build or run.** Results are added afterwards in their own section and do not change this protocol.

## Why

On 3 November the user decided (decision D9, item 8a in NEEDS-HUMAN) that the two October packages that refuse to run on Linux should be reproduced here too, through declared, dated amendments, so that all results are consistently Linux. This is one of them.

The package is R10's **initializer-only schema reload** ([record](nu-schema-reload-feasibility-2026-10-16.md), package `experiments/nu-r10-schema-reload/`). In it, Gaia (Nu's editor) holds a halted Breakout game at the fixed B0 checkpoint. A source edit adds a new model field, `BrickReward`, with the initial value 200 in `Gameplay.empty`, and uses it for scoring. Gaia's ordinary code reload installs the edit in the running process.
- On Windows, the **live** arm kept all seven old fields but the new field came out as **0, not 200**. After one brick hit the score was 100. That is a valid, failed application mapping.
- The **fresh** reference process started with reward 200, rebuilt the checkpoint, and scored 300 after the same hit.

The question is: **does the same outcome appear on Linux?**

Authority: user decision D9 (3 November 2026). This is the completed initializer-only package, **not** the stopped explicit-migration construction (its untracked draft files in `experiments/nu-r10-schema-migration/` stay unopened). No new arm, no candidate or model call, nothing Daybreak-only.

## The amendment (the only change to the package)

The package checks for Windows in three places. `experiments/nu-r10-schema-reload-linux/linux_amendment.py` copies the committed package into a new scratch folder, checks every original file hash, and changes exactly these lines in the copy. The committed package is not touched.

| File | Line(s) | Windows original | Linux amendment |
| --- | --- | --- | --- |
| `seal_build.py` | 111–114 | the toolchain must report OS `Windows` and runtime identifier `win-x64` | it must report OS `Linux`, `dotnet --info` OS name `ubuntu`, and `linux-x64` |
| `compare.py` | 165 | each trace's OS string must contain `Windows` | it must contain `Ubuntu` (this server's .NET reports `Ubuntu 22.04.5 LTS`) |
| `objective_checks.py` | 96 and 442 | synthetic traces say `Microsoft Windows 10.0.19045`; the wrong-OS control uses `Linux` | synthetic traces say `Ubuntu 22.04.5 LTS`; the wrong-OS control uses `Microsoft Windows 10.0.19045` |

The amendment keeps each check's strength: the build and the traces must still come from one declared platform, and a trace from another platform is still rejected.

## What stays fixed

- Every other package byte: the probe (`SchemaReload.fs`/`.fsproj`), `prepare.py`, `schema_edit.py`, `source_manifest.py`, `run.py`, the frozen independent oracle (`oracle.json`, SHA-256 `327d804d…`), the contract and its clarification.
- Nu source: the preserved archive `.artifacts/r03-feasibility-20261015/nu-064f7ae.tar` (SHA-256 `eb0aa771…f92b`). `prepare.py` checks it.
- Seed: `experiments/nu-history-b1/checkpoint/gameplay.symbol` (SHA-256 `ffee72d9…783a`). `run.py` checks it.
- .NET SDK 10.0.302 and runtime 10.0.10 (both in the per-user install), Release configuration, the README's commands, and `run.py`'s deadlines: 900 s overall and 420 s to the checkpoint.

## What differs from Windows (environment only)

- The same environment as the passing 2 November Linux reproductions, through `scripts/linux_nu_env.sh`: Xvfb on display `:95` with a private cookie and no TCP, Mesa llvmpipe with the OpenGL 4.6 override, `SDL_VIDEO_DRIVER=x11`.
- A scratch NuGet cache seeded from `.artifacts/nuget-packages/` (the Windows cache, which avoids the FSharp.Core package difference).
- **Acceptance.** On Windows, an independent reviewer and the parent accepted the source, the runner, the oracle and each build receipt before the native launches. Here I check each sealed receipt myself and record its hash. There is no second reviewer.
- Paths: scratch copies outside the repository, as in the other Linux checks.

## Steps and pass conditions

1. **Prepare:** exit 0. Original and instrumented hashes must equal Windows: `Gaia.fs` `0cf653d4…` → `0700ba14…`, and `Gameplay.fs` V0 `571e2a5c…` unchanged.
2. **Full-graph build** (V0): exit 0 with zero errors. Warning counts are recorded.
3. **Seal V0** with the amended `seal_build.py`: exit 0. The receipt's file count is recorded (Windows: 1,145 independent copies; Linux may differ because native libraries differ per platform).
4. **Objective checks** (amended `objective_checks.py`, with the V0 receipt): run once. **Prediction:** every check passes except one: "primary cleanup failure forces direct fallback and unresolved-tree stop". That control injects a failing Windows `taskkill` command, and `run.py`'s non-Windows branch never calls that command, so the control cannot pass on Linux. This is a known limit of the unchanged runner's Linux branch, not something I will patch. Any other failing check is a Linux difference.
5. **Live run** (`run.py live`): exit 0 with `runnerPass` true. The runner makes the three-anchor V1 edit at the checkpoint.
6. **V1 build** (`--no-restore`) and **seal V1**: exit 0. The V1 source must have SHA-256 `b8a2cac2…feccb8`.
7. **Fresh run** (`run.py fresh` with the live binding): exit 0 with `runnerPass` true.
8. **`compare.py`** on the Linux pair: completes without error.
9. **Across platforms**, the Linux `comparison.json` must equal the Windows `comparison-01.json` in every verdict field: observation processes passed; live required reward installed **false**; live mapping **false**; fresh initialization **true**; live and fresh preservation **true**; both continuations attempted and passed; live observed reward **0**; fresh observed reward **200**; checkpoint fields and projection equal; post-update model and projection **not** equal; matched successful preservation pair **false**. The paths and whole-trace hashes are excluded, because they contain paths and timing.
10. **Also recorded** (not pass/fail): the generated F# Interactive type names (Windows: `FSI_0005.Breakout.Gameplay`), the post-update models of both arms compared with the Windows traces, build warning counts, and timings.

## What counts as a different result

Any of these is a **Linux difference**. It is recorded as found, not fixed and rerun:
- a build failure, crash, timeout or missing ready signal;
- a reload error from F# Interactive;
- a runner or comparison failure;
- any step-9 verdict that differs from Windows, **including a live reward of 200**. That would be a different scientific result, not a better one.

The stop rule applies: five unresolved failures at one unchanged step means stop that step. Environment-only fixes (display, library path, exact SDK) are allowed, and each is logged as its own attempt. A change to any package byte beyond the declared amendment would need a new written amendment first.

## What this check cannot show

The original limits stay: the reload goes through Gaia's guarded reload core, not the F9 key or menu; no native input replay; no audio or framebuffer observation; one schema and one edit. A matching result shows only that this bounded observation reproduces on this server. It does not resume the stopped migration construction, and it says nothing about benefit.
