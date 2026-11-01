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

## Results (added 2 November 2026, after the runs)

**Conclusion: the frozen R04 package reproduces on this Linux server.** All nine variants built. The four reference variants passed, and the five faults were caught at exactly their predicted gates. Every fixed record of the reference variants matches Windows exactly. One environment fix was needed: Mesa's software renderer offers OpenGL 4.5, and Nu at this revision asks for 4.6.

| Step | Result |
| --- | --- |
| 1. SDK | `10.0.302` (runtime 10.0.10), per-user in `~/.local/share/dotnet-sdk-10.0.302`. |
| 2. Prepare | Exit 0 in 10 s. Every Nu, application and instrumentation hash equals the Windows preflight-08 receipt. The two probe files equal the amended probes the published Windows runs used (`amended-probes-01/source`). |
| 3. Build | All nine exit 0, about 70–76 s each. **334 warnings each, codes NU1608/NU1901/NU1902 only, same as Windows.** Binary hashes differ from Windows, as expected: builds embed absolute source paths. |
| 4. Run | See the attempts below. Final: 4/4 references pass, 5/5 faults caught at their predicted gate. Runs took about 25–33 s each; none came near the 600 s deadline. |

**Attempts, all retained:**

1. `baseline-explicit` attempt 01: **failed in 1.4 s**. OpenGL.Net threw `ArgumentNullException` in `Gl.QueryContextVersion`: requesting Nu's OpenGL 4.6 core context from Mesa 23.2.1 llvmpipe (which offers 4.5) returned no version string. No probe observation was made.
2. `baseline-explicit` attempt 02: same package, plus the environment-only Mesa override `MESA_GL_VERSION_OVERRIDE=4.6` and `MESA_GLSL_VERSION_OVERRIDE=460`. Nu logged `Initialized OpenGL 4.6 (Core Profile) Mesa 23.2.1`. **Passed.**
3. The other eight variants, attempt 01 each, with the same environment: all as predicted.

**Comparison with Windows** (`compare_platforms.py`, same record selection as the original receipt script; a self-test on Windows-against-Windows reproduces the published counts):

| Variant | Linux outcome | Fixed records equal to Windows? |
| --- | --- | --- |
| baseline-explicit / baseline-wildcard | pass / pass | **yes**, 13 of 13 each |
| pause-explicit / pause-wildcard | pass / pass | **yes**, 22 of 22 each |
| fault-missing-toggle | caught at `pause-reached` | identical except the stack-trace file path |
| fault-hidden-content | caught at `pause-projection` | identical except the stack-trace file path |
| fault-advancing-time | caught at `pause-frozen-model` | identical except the stack-trace file path |
| fault-reset-resume | caught at `resume-retained` | identical up to the fault. Afterwards only ball direction and brick colours differ, because the fault resets to a fresh, randomised start. The stack path differs too. |
| fault-stale-quit | caught at `quit-reset` | **yes**, 22 of 22 |

On Linux, explicit and wildcard also agree exactly (baselines and pause arms), as they did on Windows.

**Limits.** These hold in addition to the protocol's limits.
- The OpenGL override makes Mesa claim a version its software renderer does not fully support. Nothing rendered was scored, and no shader error appeared in these runs. Still, any later work that depends on what is drawn must not assume rendering parity with Windows.
- Audio went through SDL on a machine with no sound device. Only the request hook is observed, as on Windows.
- This repeats the frozen observations on a second platform. It adds no new comparison and establishes no benefit.

**What this changes.** The 26 October blocker "no suitable native environment" is resolved for this pinned R04 package. Later R04 work named in the [behavioral contract](nu-r04-behavioral-contract-2026-10-26.md) can use this server: ordinary access, comparable outside observations, and a differently organised correct implementation. Such work needs its own protocol first.

**Files.**
- Tracked: [linux_run.sh](../experiments/nu-r04-pause-runtime/linux_run.sh) (environment wrapper), [compare_platforms.py](../experiments/nu-r04-pause-runtime/compare_platforms.py) and the comparison output [linux-platform-comparison-2026-11-02.json](../experiments/nu-r04-pause-runtime/linux-platform-comparison-2026-11-02.json).
- Private, ignored: `.artifacts/r04-linux-reproduction-20261102/` holds all run folders (traces, stdout/stderr, process receipts, environment files), the prepare/build receipts and logs, the SDK identity and the deletion log. The 35 GB build tree was deleted afterwards; it can be rebuilt from committed inputs in about 12 minutes.
