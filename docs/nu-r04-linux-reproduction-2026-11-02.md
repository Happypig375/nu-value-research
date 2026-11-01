# R04 pause runtime: Linux reproduction check (2 November 2026)

**Status: protocol fixed before any build or run.** The results section is added afterwards and does not change this protocol.

## Why

The 26 October handoff named "no suitable native environment" as the blocker for further R04 evidence. On 1 November the nu-gaia-agentic workspace built and ran current Nu headless on this server. This check asks a narrower question first: **does the frozen R04 package from 15 October reproduce on this Linux server, unchanged?** If it does, the server becomes a usable environment for later R04/R03 work. If it doesn't, the first failing step says what is missing.

Authority: the user approved this bounded check on 2 November ("autonomous idea refinement and development are pre-approved"; NEEDS-HUMAN item 3). It adds no new experimental arm, no candidate or model run, and does not resume R02, R10, R12 or the Daybreak-only work.

## What stays fixed

- Package: `experiments/nu-r04-pause-runtime/` exactly as committed (prepare, build and run scripts, probe sources, patches).
- Nu source: `.artifacts/r03-feasibility-20261015/nu-064f7ae.tar`, SHA-256 `eb0aa771…f92b` (checked by `prepare.py`), commit `064f7ae`.
- B0 checkpoint: `experiments/nu-history-b1/checkpoint/gameplay.symbol`, SHA-256 `ffee72d9…a3a`.
- .NET SDK **10.0.302**, as `build.py` and `run.py` require. It is installed per-user in its own folder and selected only for these commands.
- 600-second deadline per run (enforced by `run.py`).

## What differs from the Windows runs (the treatment)

- Linux x64 (Ubuntu, kernel 6.8) instead of Windows.
- No GPU display: Xvfb virtual display with Mesa's software OpenGL (llvmpipe).
- Linux native libraries come from the same NuGet packages (SDL3, Jolt and others ship linux-x64 builds). Nu at this revision expects a system `libassimp` on Linux. If the run needs it, a user-level copy is supplied by `LD_LIBRARY_PATH`, and its origin and hash are recorded.
- The NuGet cache is seeded from the server copy of the original package cache (`.artifacts/nuget-packages/`); missing packages come from nuget.org. NuGet checks package hashes either way.
- All work happens in a scratch copy outside the workspace; the preserved `.artifacts/` trees are read only.

## Steps and pass conditions

1. **SDK:** `dotnet --version` prints `10.0.302` with the per-user install.
2. **Prepare:** `prepare.py` exits 0 and its receipt passes its own pin/hash checks for all nine arms.
3. **Build:** `build.py` exits 0 for all nine graphs and records four binaries per arm. Compared with Windows (all nine built with 334 warnings, codes NU1608/NU1901/NU1902 only), a different warning count or code is recorded as a platform difference, not a failure.
4. **Run, one at a time, in this order:** `baseline-explicit`, `baseline-wildcard`, `pause-explicit`, `pause-wildcard`, then the five faults. Each goes into a new output folder.
   - The four reference arms should exit 0. The five faults should exit 1, each at the gate named in `fault-gates.md`, with the engine itself exiting normally.
   - The fixed records should equal the Windows records under the same canonical JSON comparison: 13 per baseline, and 22 per pause arm through the resumed pair.

## What counts as a different result

Any of these is a **Linux difference** and is recorded as found, not fixed and rerun: a build failure, a missing native library, a crash or timeout, a reference arm failing a gate, a fault caught at a different gate (or not caught), or a record that differs from Windows.

The project's stop rule applies: five unresolved failures at one unchanged step means stop and report. Environment fixes that change no package byte (display variables, the library path, installing the exact SDK) are allowed. Each is logged as its own attempt, and none may be used to hide a behavioural difference. Changing a probe, patch, oracle or source file is **not** allowed in this check.

## What this check cannot show

The same limits as the original R04 record apply: synthetic clicks, an audio request hook rather than real playback, one pinned application and mode. Software rendering means no framebuffer or performance claim. Passing shows only that the frozen R04 observations reproduce on this server. It says nothing about maintenance benefit, the value of pause, or agent access.

## Results

(Added after the runs.)
