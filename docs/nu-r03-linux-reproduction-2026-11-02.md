# R03 history pair (B0 and B1): Linux reproduction check (2 November 2026)

**Status: protocol fixed before any build or run.** Results are added afterwards in their own section and do not change this protocol.

## Why

The frozen R04 pause package reproduced unchanged on this Linux server earlier today ([record](nu-r04-linux-reproduction-2026-11-02.md)). The next most important retained native results are the R03 history pair from 15 October:

- **B0** ([record](nu-history-feasibility-2026-10-15.md)): real Gaia (Nu's editor) in functional mode plays MMCC Breakout until it first scores, takes an undo snapshot, lets the game run on for at least ten more updates, then uses Gaia's real undo. The model and the projected entities must be exactly as they were at the snapshot. A second, fresh process rebuilds the same checkpoint through the game's ordinary setter, and two deliberately wrong checkpoints must fail.
- **B1** ([record](nu-history-continuation-2026-10-15.md)): two fresh processes start from the same fixed B0 checkpoint. One goes through snapshot → ten updates → undo first, the other doesn't. Both then run exactly twenty more updates. The two traces must agree at every step and match a hand-calculated ball path, including a wall bounce at update 5.

The question here is narrow: **do these two packages reproduce on this server, unchanged?** B1 also allows a stronger check than R04 did. Its input is fixed, so the twenty-step trace on Linux can be compared bit for bit with the Windows trace. That tests whether Nu's single-precision game arithmetic gives identical results on both platforms.

Authority: user pre-approval of autonomous development (2 November), as for the R04 check. This adds no new arm or comparison, makes no candidate or model call, and does not touch R02, R10, R12, R03 native-001 or the two Daybreak-only branches. B0 and B1 are separate packages that already passed; this is not a retry of the terminal R03 native-001 attempt.

## What stays fixed

- Packages `experiments/nu-history-b0/` and `experiments/nu-history-b1/` exactly as committed: the bridge installer `prepare.py`, probe sources, project files, `run.py` and `compare.py`. They are copied byte for byte to a scratch folder, without their ignored `bin/` and `obj/` folders, so builds happen outside the checkout.
- Nu source: `.artifacts/r03-feasibility-20261015/nu-064f7ae.tar` (commit `064f7ae`; `prepare.py` checks the archive's commit comment). It is extracted fresh into scratch. The preserved Windows `source/` tree is not used or modified.
- B1's fixed input `experiments/nu-history-b1/checkpoint/` (B1's `run.py` checks its hashes before launch).
- .NET SDK **10.0.302**, per-user install, as for R04. Release configuration, `SourceRevisionId=064f7ae92a8506689cd91aff5e6804a375d6ef3d`, as in the README commands.
- 600-second process deadline per run (`run.py`), and the probes' own limits (B0: 600 updates and 1,200 callbacks; B1: 200 callbacks).

## What differs from the Windows runs

The environment is the same as the passing R04 Linux runs:
- Linux x64 and the Xvfb virtual display with a private auth cookie.
- Mesa llvmpipe software OpenGL with `MESA_GL_VERSION_OVERRIDE=4.6` / `MESA_GLSL_VERSION_OVERRIDE=460` (R04 showed Nu needs OpenGL 4.6 and llvmpipe offers 4.5).
- `LIBGL_ALWAYS_SOFTWARE=1` and `SDL_VIDEO_DRIVER=x11`.

All of this goes through one environment-only wrapper, `scripts/linux_nu_env.sh`, which logs the environment of every run. The NuGet cache is a scratch copy seeded from `.artifacts/nuget-packages/`; anything missing comes from nuget.org, with hashes checked by NuGet.

## Steps and pass conditions

1. **Prepare:** extract the archive, then run `nu-history-b0/prepare.py`. It must exit 0. Its instrumented-file hash must equal the bridge-generated hash recorded on Windows, `19964b82…6cdfc5` (`.artifacts/r03-feasibility-20261015/instrumentation-reproduction-final.json`). That receipt records that the source actually executed on Windows differed from this only in three CRLF line endings. A different hash is a Linux difference.
2. **Build:** `dotnet build` of `Probe.fsproj`, then of `B1.fsproj`, as in the READMEs. Both must exit 0. Warning counts and codes are recorded; a difference from Windows is recorded but is not a failure.
3. **B0 history run** (`run.py history`, new checkpoint folder): exit 0, with the probe's own result passing. That means a noninitial halted checkpoint was reached and taken, at least ten real drift updates followed, and Gaia's undo restored the complete model and projection, with update counts unchanged across undo and the next halted boundary.
   - The checkpoint values are **not expected to equal Windows**. The ball's starting direction is random, so the first scoring state differs between runs.
   - A run that ends only because no scoring state came within 600 updates (the ball kept missing the paddle) is "not reached". That is a chance outcome, not a platform difference. Up to **three** history attempts are allowed for this reason only, each in a new folder and all kept. Any other failure counts as a Linux difference.
4. **B0 fresh run** (`run.py fresh`, using the Linux checkpoint from step 3): exit 0, with the probe passing. The complete reconstruction must match at the next halted boundary, and both negative controls (unchanged initial state; score omitted) must fail equality, as on Windows.
5. **B1 history run, then B1 fresh run** (`run.py`, new folders): each exits 0 with the probe passing.
6. **B1 comparison on Linux:** the frozen `compare.py` on the two Linux traces must pass. That covers twenty matched complete models and projections, the predicted `(TimeUpdate, Update)` order, and the three in-memory corruption checks.
7. **B1 across platforms**, using a new small script `experiments/nu-history-b1/compare_platforms.py` that only reads traces:
   - For each arm, the seeded-B0 row and all twenty continuation-step **models and projections must equal the Windows ones exactly**. Values are compared as stored, i.e. as single-precision bit patterns. Absolute engine counters, paths, timing and runtime identity are excluded, as in the original contract.
   - The frozen `compare.py` is also run on the two mixed pairs (Windows history with Linux fresh, and Linux history with Windows fresh). Both must pass.

## What counts as a different result

Any of these is a **Linux difference**. It is recorded as found, not fixed and rerun:
- a build failure, missing native library, crash or timeout;
- a probe gate failing for any reason other than B0's declared "not reached";
- an event order or count that differs from the contract;
- a B1 model or projection value that differs from Windows at any step.

The stop rule applies: five unresolved failures at one unchanged step means stop and report. Environment-only fixes (display variables, library path) are allowed, each logged as its own attempt, but never to hide a behavioural difference. Changing a probe, bridge, oracle or source file is not allowed in this check.

## What this check cannot show

The limits of the original B0/B1 records still apply:
- no framebuffer or displayed-image equality;
- no audio observation;
- no native physics or contact restoration;
- no input replay;
- one pinned application in functional mode.

Software rendering means no performance claim; elapsed times are not comparisons. A pass shows only that these bounded history observations reproduce on this server. If B1 matches bit for bit, that holds for this twenty-step managed trajectory only, not for Nu's determinism in general. Nothing here bears on maintenance benefit or agent access.
