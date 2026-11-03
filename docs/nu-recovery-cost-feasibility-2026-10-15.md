# R06 bounded recovery cost: execution record

> **Timing note, 3 November 2026 (user decision):**
> - The millisecond and wall-clock timings below were measured on the Home PC, which was **memory-constrained**. Treat them as **provisional and possibly distorted** by memory pressure. The recorded values are unchanged.
> - Timings are valid only within one machine and configuration. Never compare them with timings from another machine.
> - The Linux server is now the reference machine. A paired, repeated re-run of all arms there, under one declared configuration, will give the reference timings (NEEDS-HUMAN item 10).
> - The data-only results (state equality, verdicts) are not affected by this note.
> - The original reconstruction feasibility **timeout** may also reflect memory pressure: the same run passed on the Linux server on 2 November.

## Current status

All twelve assigned measured processes passed, giving six complete pairs.
History acquisition was faster in every pair, while the direct history recovery
call was slower in every pair. Request-to-ready differences went both ways.
These are descriptive first-use component costs for one fixed checkpoint and
machine; the routes retain different payload scopes, so they do not isolate
persistence overhead or establish a maintenance benefit.

The original reconstruction feasibility process timed out before its first
setup observation. A separate unscored diagnostic then completed the contract
without a stack attachment. The [prospective release](../experiments/nu-r06-recovery-cost/measured-series-release-2026-10-15.md)
recorded that disposition before the measured series began. The original
timeout remains failed and unexplained; neither feasibility nor diagnostic
times enter the measured results.

This is a local construction under the user's October 15 authorization. It
compares two ways to recover the already selected represented B0 service;
it does not measure repair success, ordinary agent access or human steering.
The [prospective contract](../experiments/nu-r06-recovery-cost/pre-execution-contract.md)
and [setup amendment](../experiments/nu-r06-recovery-cost/pre-build-setup-amendment-2026-10-15.md)
own the observations and falsifiers.

## Measured result

Values below are milliseconds, shown as **median [minimum, maximum]**. Each
route has six valid observations and the paired column has six assigned pairs.
The paired column summarizes each pair's H-minus-R difference; it is not the
difference between the two route medians. Raw ticks and per-attempt observations
are retained in the [compact receipt](../experiments/nu-r06-recovery-cost/result-receipt.json).

| Component | H: history | R: reconstruction | Paired H minus R |
| --- | --- | --- | --- |
| Acquire recovery material | 2.38 [2.21, 4.71] | 5.39 [3.81, 10.24] | -2.28 [-7.46, -0.75] |
| Direct recovery call | 33.70 [19.91, 44.35] | 14.58 [10.23, 35.50] | +12.00 [+3.22, +30.81] |
| Recovery request to next callback entry | 353.57 [284.19, 370.18] | 368.83 [263.58, 394.97] | -14.14 [-110.78, +97.50] |

Readiness includes intervening engine work and is much longer than the direct
call in these observations. A shorter acquisition or direct call therefore
does not determine end-to-end readiness. No timestamp overhead, collection,
outlier or startup duration was subtracted, and no observation was replaced.
The sample provides no population-effect estimate or steady-state result.

All measured processes exited 0 without a timeout, with 15 callbacks and exactly
ten source-ordered TimeUpdate/Update pairs. Parent verification rehashed the
retained outputs and checked complete seed/drift/ready models and projections
against the verified FH trace, the common absent-scene boundary, selected/idling
and halted phases, unit deltas, sampled Left/Right states, raw clock arithmetic,
identical recorded source/binary inputs and the assigned execution order.
The FH drift had already been independently calculated from source using
float32 arithmetic. This verification checks the declared represented service;
it does not observe arbitrary native state, physical input or external effects.

Secondary approximate managed-allocation differences, in KiB, were:

| Observation-sample interval | H: median [range] | R: median [range] |
| --- | --- | --- |
| Pre- to post-acquisition | 47.85 [39.88, 63.98] | 628.91 [616.64, 636.61] |
| Pre-recovery to ready-entry sample | 1,714.75 [1,603.51, 1,816.57] | 4,921.02 [4,685.63, 5,053.80] |

Generation-0 counts increased in 0/6 H and 2/6 R acquisition intervals, and
3/6 H and 6/6 R recovery-to-ready intervals. Each increase was one collection;
no generation-1/2 increase occurred in these intervals. These process-wide
sample differences include observer and concurrent engine/runtime work outside
the primary timed calls. They are not isolated operation allocations or native
allocation measurements, and no collection was adjusted away. Heap, working-set
and private-byte snapshots describe the target process and remain secondary;
they do not measure retained-checkpoint size or memory release.

## Comparison and interpretation

Both routes use one common executable, exact Nu source
`064f7ae92a8506689cd91aff5e6804a375d6ef3d`, .NET SDK 10.0.302, functional
accompanied Gaia/MMCC Breakout and a static 60-update clock. Both begin from
the same fixed B0 model and selected projection, execute ten observed
TimeUpdate/Update pairs with unit deltas and Left/Right held states sampled up
at every Update, and
must recover the full declared target at the next halted post-content boundary.

| Route | Acquisition | Recovery | Represented scope |
| --- | --- | --- | --- |
| H: history | Actual guarded Gaia snapshot | Actual guarded Gaia undo | Retains the broader functional World state; the checked output is B0. |
| R: reconstruction | Serialize the live Gameplay value | Deserialize it and set Gameplay | Retains a model payload; the same B0 output must be reconstructed. |

This is a comparison of two supported operations for the declared output.
Their payload scopes differ; it is not an isolated persistence-mechanism effect
or proof of whole-world equivalence. The isolated R06 bridge uses a weak exact
identity witness for the next RestorePoint, avoiding an additional strong
WorldState root solely for checking. Its allocation and guard work remain
inside H. Historical R03 source and executables are preserved.

The three primary durations are acquisition, the direct recovery call, and
recovery request to the literal next callback-entry timestamp. Raw Stopwatch
ticks and frequency are retained. Oracle, trace and process time are separate;
there is no guessed overhead subtraction. Approximate managed allocation,
collection counts and heap/process snapshots provide secondary context, not
native allocation, retained-checkpoint size or proven memory reclamation.

The [fixed attempt plan](../experiments/nu-r06-recovery-cost/attempt-plan.json)
assigns FH/FR as unscored feasibility, then six pairs in order
`H1 R1 R2 H2 H3 R3 R4 H4 H5 R5 R6 H6`. Each process has a 600-second deadline
and 1,200-callback watchdog. Preserve every failure, missing result and
interruption. Describe valid completed outcomes with route medians/ranges and
paired H-minus-R differences; do not infer population benefit, remove outliers
or extend the sample after observing results. First-use JIT, OS cache and
temporal conditions remain part of this local case.

## Reconstruction alignment

The [R04 diagnostic](nu-pause-runtime-feasibility-2026-10-15.md) found a matching
model with two stale projected brick positions. Source supports a generated-key
collision with initialization-only properties; the failed attempt did not
record its fresh initial keys. The common R06 setup therefore changes only
the existing fresh model's state to Quit, waits one halted post-content
callback, and verifies unchanged model values, zero Update/TimeUpdate events,
the same selected/idling screen and an absent scene before installing B0.
It performs no new random-model construction or Quit event.

This work lies before either route's acquisition and timers. It does not change
the planned recovery after the ten identity-preserving drift steps. It is
explicit setup work, not a claim that direct model replacement generally
preserves existing entity initialization or native state.

## Build and preflight attempts

| Attempt | Observed outcome |
| --- | --- |
| Source preparation 01–05 | The initial archive-hash constant error stopped before build. Later receipts preserve source review, weak-reference and callback-timestamp corrections, full 3,240-file archive verification, and the line-ending-normalized Gaia review diff. The selected isolated tree changes only the exact reviewed Gaia bridge. |
| Source preparations 06–08 | The common absent-scene setup and its wording clarification precede runtime. A later build-driver correction changes output placement, with no model, recovery, timer or oracle change. |
| Build 01 | Failed with two MSB3073 post-build errors and 396 warnings. Central output relocation broke the pinned projects' hardcoded Nu.Pipe path. No R06 executable or runtime result was produced. |
| Build 02 | Passed with 400 warnings and zero errors. Nu builds at its expected paths inside the isolated tree; byte-identical R06/B0 project copies build in a separate private folder. Historical working-tree outputs are not targeted. |
| Dependency verification | All 48 managed assets and 17 Windows x64 runtime targets resolve. The initial verifier incorrectly demanded exact framework 10.0.0; its retained false negative was corrected for patch roll-forward to installed 10.0.10. This is static verification, not a loaded-runtime observation. |

Build 02 warnings comprise four FS0046, six NU1608, 247 NU1901 and 143 NU1902
occurrences; no dependency was upgraded. Its receipt SHA-256 is
`6945a68aa7e1bbea5084a3ed822e1370ff2e35a384c6c752c5439fd32df19fb2`.
The executable SHA-256 is
`207d6027af9a793e1b3fabfcdd8f073ee572d89b72d33dfd632bb90bc8298fd4`.
The asset-bearing Breakout DLL matches the probe's copy, and all 148 application
asset identities were checked. Parent verification covers 242 unique declared
source, input, executable, host, dependency and asset files. Other-platform
runtime manifest integrity is recorded separately from physical Windows-file
verification.

Complete logs, source snapshots, manifests and checks remain under ignored
`.artifacts/r06-recovery-cost-20261015/`. These checks establish preparation
for the bounded runtime comparison. They do not price construction, workflow
integration, diagnosis, verification or the total work of a useful repair.

## Feasibility observations

| Assigned process | Observed outcome | Interpretation |
| --- | --- | --- |
| FH, history, first attempt | Probe and engine exited 0. The complete clear, B0, ten-pair drift and recovered B0 observations passed; 15 callbacks, ten Updates and ten TimeUpdates. | One successful unscored history feasibility observation. |
| FR, reconstruction, first attempt | Deadline reached; probe process terminated with exit 1 and successful process-tree cleanup. Configuration is the only trace event, and no result record exists. | No first setup observation was recorded; callback entry itself is unknown. Acquisition and recovery have no observations. |
| FRD1, additional reconstruction diagnostic | Target exited 0 at 35.75 seconds, before its conditional 60-second stack boundary. No stack was attempted. Clear, B0, ten-pair drift and recovered B0 passed with 15 callbacks. | One additional unscored feasibility observation; original FR remains failed. |

Parent verification checked FH's complete seed/recovered models and projections
against the fixed reference, independently calculated its ten-step float32
model trajectory, and matched the drift projection to the accepted prior B1
step ten. The common clear changed only the initial model's state. Both event
streams had unit deltas and the declared order; sampled Left/Right states were
up at every Update. Acquisition, direct recovery, readiness and oracle timestamp
ordering were valid. Subsequent parent verification matched FRD1's complete
seed, drift and ready models/projections to FH, and checked its clear, event,
phase, sampled input and clock evidence separately.

FH took 40.922 seconds as a whole process. FR's wrapper finished after 604.687
seconds, including deadline cleanup after the fixed 600-second allowance.
These are process-accounting observations, not recovery-operation times. The
last FR stdout message reports OpenGL initialization; there is no evidence yet
locating the intervening startup wait or attributing it to a route-specific
operation. Local machine load and startup conditions were not experimentally
controlled. FRD1 does not explain that earlier wait or establish startup
reliability.

## Additional startup diagnostic and execution decision

FRD1 used the unchanged accepted binary with a distinct diagnostic ID and the
same 600-second deadline. Its prospective driver would collect one managed
stack only if the process remained alive without a first setup observation at
60 seconds. The target instead exited successfully at 35.75 seconds; the
60-second observation was explicitly not reached. The full wrapper, including
exit context collection, took 37.094 seconds. No diagnostic attachment,
timeout, cleanup action or observer error occurred.

The private tool installation and launcher preparation are retained, including
rejected launcher versions and their corrections before execution. The accepted
launcher separated deadline supervision from context collection, checked exact
reviewed identities and environment fields, and limited process control to its
owned target/helper. Context data show ordinary host load, not quiescence or
the cause of the earlier failure. Unavailable Win32 fields' error numbers have
a known reporting limitation and are not used for causal diagnosis.

Parent acceptance of the complete unattached FRD1 observation supports attempting
the original descriptive series. The dated release preserves FH, failed FR,
and additional FRD1 as separate unscored records; freezes the original measured
order and implementation; and requires stopping on the first unexpected failure.
This is a maintainer execution decision under existing local authorization,
not human approval or evidence of comparative benefit.
