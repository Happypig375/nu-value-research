# R06 recovery-cost series: Linux reproduction check (2 November 2026)

**Status: protocol fixed before any build or run.** Results are added afterwards in their own section and do not change this protocol.

## Why

Four packages from 15 October now reproduce unchanged on this server: R04, the R03 history pair, R10 live reload and the R02 lifecycle pair. The R06 component-cost series ([record](nu-recovery-cost-feasibility-2026-10-15.md)) is different. It measures **time**, so a second machine tests whether its findings depend on the machine.

R06 compares two ways to return a running Gaia game to the same B0 checkpoint after ten updates of drift:
- **H:** Gaia's own snapshot and undo.
- **R:** serialize the game model in memory, then set it back through the game's ordinary setter.

On Windows, all twelve measured processes passed. Three timing findings came out:
- taking the snapshot (**acquisition**) was faster with H in all six pairs;
- the **recovery operation** itself was slower with H in all six pairs;
- **request-to-ready** time went both ways.

Separately, the first unscored R feasibility process (FR) timed out during Gaia startup before any observation. The cause was never explained.

Two questions:
1. Does the series reproduce here, unchanged?
2. Do the two consistent timing directions hold on a different machine and operating system?

The FR timeout gets a second chance to show up, but a single run cannot explain it.

Authority: user pre-approval of autonomous development (2 November). No new arm, no candidate or model call, nothing Daybreak-only. These are new attempts. They replace no original attempt.

## What stays fixed

- Package `experiments/nu-r06-recovery-cost/` exactly as committed, plus the B0/B1 files its scripts read (`experiments/nu-history-b0/`, `experiments/nu-history-b1/`). All are copied byte for byte into a scratch folder with the same layout. `build.py` and `run.py` check these identities themselves.
- Nu archive `.artifacts/r03-feasibility-20261015/nu-064f7ae.tar`. `prepare.py` compares every archive member and accepts only the reviewed Gaia bridge as a difference.
- .NET SDK 10.0.302; the frozen `attempt-plan.json` order `FH FR H1 R1 R2 H2 H3 R3 R4 H4 H5 R5 R6 H6`; the 600-second deadline; the probe's 1,200-callback watchdog; and the frozen `summarize.py`.

## What differs from Windows

- The same environment as the earlier Linux checks, through `scripts/linux_nu_env.sh`: Xvfb and Mesa llvmpipe with the OpenGL 4.6 override.
- A different machine: 224 shared cores, run with `nice`. Other users' jobs may run concurrently, so timing noise is expected to be larger than on the Windows desktop.
- **Acceptance.** On Windows, each build and launch had independent and parent review. Here I accept the build receipt after checking:
  - preparation and build both pass;
  - the only source difference is the reviewed Gaia file;
  - the build is complete.

  The accepted hash is recorded. This is weaker than the original, and it is stated as such.

## Steps and pass conditions

1. **Prepare:** exit 0. The receipt must report Gaia as the only exception, and its instrumented hash is recorded and compared with the Windows receipt.
2. **Build:** exit 0. Warning codes are recorded.
3. **FH, then FR** (unscored feasibility). Each passes if the probe reports the declared B0 output at the next halted callback.
   - If FH fails, the series stops (the README's rule).
   - If FR fails, the failure is recorded with its phase. The measured series still runs, as it did on Windows after the original FR timeout. The prospective Windows release document allowed that and changed no binary or timing policy.
   - No feasibility attempt is repeated.
4. **Measured series**, in the frozen order, one process at a time. Each must pass the probe's semantic oracle. Any unexpected failure stops the remaining attempts (the README's rule). It is recorded, not replaced.
5. **Summary:** the frozen `summarize.py` over all fourteen receipts, into a new folder.

## What is compared with Windows

Recorded as found. Timing differences are expected and are not failures.
- Pass counts (Windows: 12/12 measured; FH pass; FR timeout).
- **Direction per pair:**
  - acquisition, H faster than R? (Windows: 6 of 6);
  - direct recovery, H slower than R? (Windows: 6 of 6);
  - request-to-ready (Windows: mixed).

  A direction that holds in all six pairs on both machines is reported as replicated. Otherwise the Linux count is reported as it is.
- Route medians, with Windows for reference: acquisition H 2.38 ms / R 5.39 ms; direct recovery H 33.7 ms / R 14.6 ms; request-to-ready H 354 ms / R 369 ms. Absolute values are not comparable across machines; only directions are compared.
- Clock rates differ (Windows `Stopwatch` 10 MHz, Linux 1 GHz). `summarize.py` already converts ticks to milliseconds using the recorded frequency.

## What counts as a different result

Any of these is a **Linux difference**. It is recorded as found, not fixed and rerun:
- a build failure, crash or timeout;
- a semantic oracle failure;
- a summarizer rejection.

The stop rule applies: five unresolved failures at one unchanged step means stop. Environment-only fixes are allowed, each logged as its own attempt, but no package byte may change.

## What this check cannot show

The original limits stay:
- component timings within one process, not maintenance, debugging or practical cost;
- no native-physics restoration, no release of retained history, no human or agent benefit.

Six pairs on a shared machine is a small sample. Replicated directions would show only that these two component orderings are not specific to one machine.

## Results (added 2 November 2026, after the runs)

**Conclusion: the R06 series reproduces on this Linux server. All fourteen processes passed, including FR, which timed out at startup on Windows.**
- **Acquisition** (taking the snapshot) replicated exactly: H was faster in all six pairs on both machines.
- **Direct recovery** did **not** fully replicate. H was slower in five of six Linux pairs; in pair 5 it was faster by 0.019 ms (6.547 vs 6.566 ms, effectively a tie). On Windows, H was slower in all six.
- **Request-to-ready** stayed mixed, as on Windows.

| Step | Result |
| --- | --- |
| 1. Prepare | Exit 0. Gaia is the only reviewed exception, instrumented to `67f46559…`, and the source manifest is `cbc4fea8…`. **Both equal the accepted Windows preparation** (`source-preparation-06.json`). 31 package files were copied unchanged. |
| 2. Build | Exit 0. **400 warnings: FS0046 4, NU1608 6, NU1901 247, NU1902 143. Identical to the Windows build-02 counts.** Sources were stable across the build. I accepted receipt `b03f9e81…`. |
| 3. Feasibility | FH **pass**. FR **pass**: the declared B0 output was reached at the next halted callback. On Windows, FR timed out during Gaia startup with no observation. That timeout therefore did not recur here. One run cannot explain it, but it was not a fixed property of the R route or the package. |
| 4. Measured | **12 of 12 pass**, in the frozen order, about 29 s each. All share one identity signature, and no integrity flag was raised. |
| 5. Summary | Frozen `summarize.py` exit 0; `measuredSeriesMismatch: false`. |

**Timing.** Medians in milliseconds. Absolute values are not comparable across machines; directions are.

| Component | Windows H / R | Linux H / R | H − R per pair, Linux | Pattern, Windows → Linux |
| --- | --- | --- | --- | --- |
| Acquisition | 2.38 / 5.39 | 0.60 / 1.75 | −1.2, −1.1, −1.2, −1.1, −1.1, −1.2 | H faster 6/6 → **6/6 (replicated)** |
| Direct recovery | 33.7 / 14.6 | 6.35 / 4.20 | +2.3, +1.1, +2.1, +2.3, −0.02, +2.7 | H slower 6/6 → **5/6** |
| Request-to-ready | 354 / 369 | 299 / 276 | −16.8, +50.3, +81.8, −36.0, +128.1, +12.2 | mixed → mixed |

Comparison receipt: `.artifacts/r06-linux-20261102/platform-comparison.json`, made by `experiments/nu-r06-recovery-cost/compare_platforms.py`. Its Windows-against-Windows self-test reproduces the published pattern.

**Reading it.**
- Gaia's snapshot is cheaper to take than serializing the model, on both machines and with a very stable gap on Linux (about 1.1–1.2 ms).
- Gaia's undo operation is usually, but not always, more expensive than setting a deserialized model. On Linux the gap is smaller (median 2.2 ms vs 12.0 ms) and one pair is a tie. "H recovery slower in every pair" was therefore a property of the Windows sample, not a rule.
- Time from request to the next ready callback is dominated by the frame schedule (about 300 ms) and shows no consistent direction on either machine.

**Limits.** These hold in addition to the protocol's limits.
- The build acceptance had no second reviewer.
- The machine is shared, and runs were niced.
- Six pairs per machine.
- Software rendering. Request-to-ready includes frame time, which differs with the renderer.
