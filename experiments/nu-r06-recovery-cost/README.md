# R06 one-checkpoint recovery component probe

> **Timing note, 3 November 2026 (user decision):**
> - The millisecond and wall-clock timings below were measured on the Home PC, which was **memory-constrained**. Treat them as **provisional and possibly distorted** by memory pressure. The recorded values are unchanged.
> - Timings are valid only within one machine and configuration. Never compare them with timings from another machine.
> - The Linux server is now the reference machine. A paired, repeated re-run of all arms there, under one declared configuration, will give the reference timings (NEEDS-HUMAN item 10).
> - The data-only results (state equality, verdicts) are not affected by this note.

All twelve assigned measured processes passed. History acquisition was faster in each pair, direct history recovery was slower in each pair, and request-to-ready differences went both ways. The original reconstruction feasibility timeout remains failed and unexplained; a separate unattached diagnostic preceded the prospective measured-series release. See the [execution record](../../docs/nu-recovery-cost-feasibility-2026-10-15.md) and [compact receipt](result-receipt.json) for observations, failures and scope.

This directory implements the frozen comparison in `pre-execution-contract.md`. The contract predates implementation and must remain byte-identical. The probe is a component-cost feasibility experiment, not a maintenance, debugging, native-physics, retention-release, or human/agent benefit study.

## Prepared variant

One `RecoveryCost` binary accepts route `H` or `R` as a process argument. Both routes start a fresh functional, accompanied Gaia process and select settled MMCC Gameplay. Before seeding B0 they follow the prospective `pre-build-setup-amendment-2026-10-15.md`: observe the fresh state, set that existing model with only `GameplayState = Quit`, require an exact empty-content boundary one halted callback later, then seed and validate the fixed R03 B0 checkpoint. They then acquire route-specific recovery material, execute the same ten `(TimeUpdate, Update)` pairs with `GameDelta.Updates=1`, halt inside Update 10, validate the same complete drift model/projection, and recover to the same next-callback B0 boundary.

- `H` calls the reviewed guarded Gaia snapshot and undo operations.
- `R` serializes the live `Gameplay` value in memory, then deserializes it and calls the supported `SetGameplay` setter.

R06 uses a fresh source tree extracted from the exact archive. Its only
archive-source difference is the reviewed Gaia bridge. The published B0 hook
is installed first, then its guard's second strong `WorldState` reference is
replaced by a `WeakReference<WorldState>` identity witness. The witness remains
live because Gaia's ordinary next RestorePoint owns the actual target. Its
allocation and identity check remain inside the measured H route.

The common oracle retains canonical JSON/value data, not an extra target `Gameplay` or `WorldState` root. The readiness timestamp is the first instruction at the next research callback entry. No equality scan, JSON serialization, or file write occurs after recovery starts and before that timestamp. Direct operation timing and request-to-ready timing use raw `Stopwatch` ticks and retain `Stopwatch.Frequency`.

GC collection counts, approximate process-wide allocated bytes, managed heap and process-memory snapshots are recorded at declared boundaries without forced collections or outcome conditioning. A zero allocated-byte difference does not establish zero allocation. Heap and process memory are secondary observations only; the managed-heap sample excludes fragmentation and is not a retained-root measure. Phase differences can include observer and concurrent process work. The bridge has no history eviction/release or `World.switch` subsystem timing, so the probe makes no retained-root, release, native-cost, or bounded-policy claim.

`attempt-plan.json` freezes two unscored feasibility processes followed by the six measured pairs in the contract's exact order. `run.py` accepts only those IDs, rejects existing output directories, requires the explicitly accepted build-receipt hash, rechecks every recorded source/input/binary identity, retains process identity/logs, and enforces the 600-second deadline. The 1,200-callback watchdog is inside the probe. A semantic or infrastructure failure is retained and stops the measured series for investigation; this driver does not replace attempts.

## Prepared files

- `prepare.py`: creates a fresh source tree, compares every regular archive member, installs the reviewed B0 bridge, substitutes the weak witness, and accepts Gaia as the sole exact reviewed exception. Missing files, unexpected non-generated files, or any other content difference fail preparation; generated outputs are reported separately.
- `build.py`: requires SDK 10.0.302, the passing preparation receipt, and a new output directory. It copies the byte-identical probe and B0 project inputs into the new private build directory. Pinned Nu builds at its expected bin/obj paths within the isolated source tree, preserving its Nu.Pipe post-build paths. The receipt identifies sources, fixed inputs, executable/host files, and the actual asset-bearing application DLL.
- `run.py`: runs one preassigned process after verifying the accepted build and identities.
- `RecoveryCost.fs`: shared H/R probe and observer.
- `RecoveryCost.fsproj`, `global.json`: pinned build entry.
- `attempt-plan.json`: immutable prospective attempt order.
- `pre-build-setup-amendment-2026-10-15.md`: prospective common seed-reconciliation correction prompted by the retained R04 diagnostic.
- `measured-series-release-2026-10-15.md`: prospective disposition of the original FR timeout and separate FRD1 diagnostic, accepted before the original measured assignments. It changes no binary, timing or observation policy.

## Commands after parent preflight and runtime release

Use new source, receipt, build and runtime paths for reproduction; existing attempt directories must be preserved. Review the resulting preparation/build receipts and exact identities before a launch. The commands below build fresh copies rather than modify the recorded attempts.

```powershell
py -3.12 experiments/nu-r06-recovery-cost/prepare.py `
  .artifacts/r06-recovery-cost-20261015/reproduction-source-01 `
  .artifacts/r03-feasibility-20261015/nu-064f7ae.tar `
  .artifacts/r06-recovery-cost-20261015/reproduction-prepare-01.json

py -3.12 experiments/nu-r06-recovery-cost/build.py `
  .artifacts/r06-recovery-cost-20261015/reproduction-source-01 `
  .artifacts/r06-recovery-cost-20261015/reproduction-build-01 `
  --prepare-receipt .artifacts/r06-recovery-cost-20261015/reproduction-prepare-01.json

$buildReceipt = '.artifacts/r06-recovery-cost-20261015/reproduction-build-01/build.json'
$acceptedBuildSha256 = (Get-FileHash $buildReceipt -Algorithm SHA256).Hash.ToLowerInvariant()

py -3.12 experiments/nu-r06-recovery-cost/run.py FH `
  $buildReceipt `
  .artifacts/r06-recovery-cost-20261015/reproduction-FH-01 `
  --accept-build-sha256 $acceptedBuildSha256
```

Run `FR` only after retaining and reviewing `FH`. Any unexpected failure stops later attempts for investigation. Only after both route feasibility boundaries are accepted may measured IDs follow exactly: `H1 R1 R2 H2 H3 R3 R4 H4 H5 R5 R6 H6`. Each receives a new output directory. Review the fresh source/build preflight and reserve serial native execution before launching. The recorded original series completed all twelve once; reproductions are new attempts and do not replace any original result.

## Offline reporting

`summarize.py` accepts explicit retained process receipts and a new output directory. It preserves pass, failure, invalid and not-run assignments; checks recorded identities and clocks; and excludes feasibility observations from measured route and paired summaries. It does not replay the semantic oracle. `summarize_validation.py` preserves synthetic validation of clock arithmetic, zero-duration operations, impossible ordering, missingness and identity conflicts. The v4 reporting implementation was accepted before the first runtime observation.

The README recorded by build02 is retained privately before this publication update. These results and reproduction-wording corrections do not change the executed probe, build driver, contract, timing policy or original attempt plan. A fresh reproduction build records the current README; the original execution receipt retains its original input identity.
