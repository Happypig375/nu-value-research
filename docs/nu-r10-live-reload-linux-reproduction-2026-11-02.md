# R10 live code reload: Linux reproduction check (2 November 2026)

**Status: protocol fixed before any build or run.** Results are added afterwards in their own section and do not change this protocol.

## Why

The R04 pause package and the R03 history pair now reproduce unchanged on this server ([R04](nu-r04-linux-reproduction-2026-11-02.md), [R03](nu-r03-linux-reproduction-2026-11-02.md)). The R10 live-reload pair from 15 October ([record](nu-live-reload-feasibility-2026-10-15.md)) is the retained native result most likely to behave differently on Linux.

In that pair, Gaia (Nu's editor) holds a halted game at the fixed B0 checkpoint. One line of the game's source is edited: each brick goes from 100 points to 200. Gaia's ordinary reload core then recompiles the game with F# Interactive (the F# scripting compiler built into Gaia) and installs the new code in the running process. After one update, the live game must equal a fresh process started from the same checkpoint with the reward-200 build.

The reload depends on platform details that the other packages don't touch:
- F# Interactive compiling and loading assemblies at run time;
- the script Gaia generates, which loads source files by relative path;
- private F# Interactive fields that the bridge reaches by reflection.

The question is: **does this pair reproduce on this server, unchanged?**

Authority: user pre-approval of autonomous development (2 November), as for R04/R03. This is the completed live-reload pair, **not** the stopped R10 schema-migration construction (its returned draft stays untracked and untouched), nor the initializer-only schema reload. No new arm, no candidate or model call, nothing Daybreak-only.

## What stays fixed

- Package `experiments/nu-r10-live-reload/` exactly as committed (`prepare.py`, `LiveReload.fs`/`.fsproj`, `run.py`, `compare.py`). It is copied byte for byte to scratch without its ignored `bin/`/`obj/`, so build outputs stay out of the checkout.
- Nu source: the preserved exact archive (SHA-256 `eb0aa771…f92b`), passed with `prepare.py --archive`. `prepare.py` checks that hash itself. This is the same archive used for R03; the Windows run made its own `git archive` with the same hash.
- Seed `experiments/nu-history-b1/checkpoint/gameplay.symbol`.
- .NET SDK 10.0.302 (per-user install), Release configuration, the README's commands, and `run.py`'s 900-second deadline.

## What differs from Windows

The same environment as the passing R04/R03 Linux runs, through `scripts/linux_nu_env.sh`:
- Xvfb with a private cookie, and Mesa llvmpipe with the OpenGL 4.6 override;
- `SDL_VIDEO_DRIVER=x11`;
- a scratch NuGet cache seeded from `.artifacts/nuget-packages/`.

## Steps and pass conditions

1. **Prepare:** exit 0. The original and instrumented hashes must equal the Windows `prepare-receipt.json`: `Gaia.fs` `0cf653d4…` → `0700ba14…` and `Gameplay.fs` `571e2a5c…` → `736132f1…`. A difference is a Linux difference.
2. **Baseline build** (reward 100): exit 0; warning codes recorded.
3. **Live run** (`run.py live … --gameplay-source`): exit 0. The runner waits for the probe's ready signal at the checkpoint, makes exactly one `BrickReward = 100` → `200` edit, and lets the reload proceed. The probe's result must pass, including its built-in data controls (score-100, reset and wrong-brick checks rejected).
4. **Fresh build** (reward 200, `--no-restore`): exit 0.
5. **Fresh run:** exit 0, with the probe passing.
6. **`compare.py`** on the Linux pair must pass. It checks:
   - checkpoint models and projections equal across arms and before reload;
   - post-update models and projections equal, at game time 150 with score 300, 28 bricks, brick `@455` removed and the declared ball bits;
   - the `(TimeUpdate, Update)` order with one game update;
   - no Left/Right input;
   - one code-reload event, with the installed model and dispatcher types consistent.
7. **Across platforms:** the Linux `comparison.json` must equal the accepted Windows `final2-comparison.json` in every field except the two whole-trace hashes, which contain paths and timing. That covers the checkpoint and post-update model/projection hashes, the event word, the delta and the post summary. The generated F# Interactive type names (`FSI_0005.Breakout.Gameplay` etc.) are compared too. A different `FSI_NNNN` number would mean a different count of earlier interactive submissions; it is recorded as a difference but does not fail the behavioural check.

## What counts as a different result

Any of these is a **Linux difference**. It is recorded as found, not fixed and rerun:
- a build failure, crash, timeout or missing ready signal;
- a reload error from F# Interactive;
- a probe gate failing;
- a comparison mismatch.

The stop rule applies: five unresolved failures at one unchanged step means stop. Environment-only fixes are allowed and each is logged as its own attempt. No package byte may change.

## What this check cannot show

The original limits stay:
- the reload goes through the guarded reload core, not the F9 key or menu path;
- no native input replay;
- no audio or framebuffer observation;
- one supported edit with an unchanged schema.

A pass shows only that this bounded reload observation reproduces on this server. It says nothing about the separate schema-reload result, the stopped migration construction, or any benefit.

## Results (added 2 November 2026, after the runs)

**Conclusion: the R10 live-reload pair reproduces on this Linux server at the first attempt, and every compared field equals the accepted Windows run.** F# Interactive compiled the one-line edit inside the running Gaia process and installed it under the same generated type name as on Windows. Live and fresh agree after one update.

| Step | Result |
| --- | --- |
| 1. Prepare | Exit 0. `Gaia.fs` `0cf653d4…` → `0700ba14…` and `Gameplay.fs` `571e2a5c…` → `736132f1…`, **equal to Windows**. The 8 package files were copied unchanged (hash list in the evidence folder). |
| 2. Baseline build | Exit 0 in 75 s, 334 warnings, codes NU1608/NU1901/NU1902 only. |
| 3. Live run | Exit 0 in 66 s. The ready signal arrived at the checkpoint, and the one edit was made. Its before/after hashes and the ready signal's checkpoint/projection hashes **equal the Windows `edit.json`**. The reload installed `FSI_0005.Breakout.Gameplay` with reward 200, and the probe passed. |
| 4. Fresh build | Exit 0 in 12 s, same warning codes. |
| 5. Fresh run | Exit 0 in 25 s; probe passed. |
| 6. `compare.py` | **Pass.** |
| 7. Across platforms | All 11 compared fields **equal Windows `final2-comparison.json`**: checkpoint and post-update model/projection hashes, the event word, the one-update delta, the post summary (time 150, score 300, 5 lives, 28 bricks, `@455` removed, same ball bits), and the three generated type names, including `FSI_0005`. Only the two whole-trace hashes were excluded, as declared. Receipt: `platform-comparison.json`. |

**Attempts:** one of each step, all passing. Nothing was retried. Evidence: `.artifacts/r10-live-reload-linux-20261102/`.

**Limits.** These hold in addition to the protocol's limits.
- The same OpenGL-override caveat as R04/R03 applies.
- Binary hashes differ from Windows because builds embed paths. Linux probe `5e2e5a09…`; application `c4cd619d…` (reward 100) and `32d559ae…` (reward 200).
