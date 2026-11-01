# Small October probes: Linux reproduction check (2 November 2026)

**Status: protocol fixed before any build or run.** Results are added afterwards in their own section and do not change this protocol.

## Why

The four larger native packages from 15 October reproduce unchanged on this server, and R06 is running. Six smaller probes remain. Most exercise compilers or managed libraries rather than the full engine. Reproducing them completes the Linux inventory of the retained October results, and three of them allow an exact cross-platform check:
- R01 compares physics-trace hashes;
- R05 and R12 reuse the very Nu binaries built on Windows.

Authority: user pre-approval of autonomous development (2 November). No new arm, no candidate or model call. None of these is a stopped R02/R10/R12 construction or a Daybreak-only branch. Each probe runs **once**, unchanged, from its committed package, with a new output folder.

## The probes and their pass conditions

Each runner's own success rule is the pass condition. Windows values are compared as stated.

1. **R04 compiler diagnostics** (`experiments/nu-r04-diagnostics/`, [record](nu-diagnostic-feasibility-2026-10-15.md)).
   - Command: `run-probe.ps1 -NuSourceRoot .artifacts/r03-feasibility-20261015/source`. The preserved Windows source tree is read only, through its `source-integrity.json`.
   - Pass: the runner exits 0, which it does only when all six builds and run exits reproduce `original-results.tsv` and both FS0025 counts match.
2. **R04 actual-application diagnostics** (`experiments/nu-r04-application-diagnostics/`, [record](nu-application-diagnostic-feasibility-2026-10-15.md)).
   - Command: `run-probe.ps1 -NuArchive .artifacts/r03-feasibility-20261015/nu-064f7ae.tar`, extracted inside its own output folder.
   - Pass: all four variant builds exit 0, and each matches `original-results.tsv` in exit code, warning/error counts, selected and total FS0025, and prediction pass.
   - Assembly hashes are expected to differ, because builds embed paths. That is recorded, not failed.
3. **R05 event observation** (`experiments/nu-r05-events/`, [record](nu-event-feasibility-2026-10-15.md)).
   - Command: `run-probe.ps1 -NuSourceRoot .artifacts/r03-feasibility-20261015/source`. This uses the **Windows-built** Release `Nu.dll` (`5bcf797d…`), read only. The runner checks that it doesn't change.
   - Pass: the runner exits 0, and its observations equal the `result-receipt.json` record.
4. **R10 Prime conversion** (`experiments/nu-r10-conversion/`, [record](nu-conversion-feasibility-2026-10-15.md)).
   - Command: the README's locked restore, build and run.
   - Pass: run exit 0, which means all eight frozen cases match; build has 0 warnings and 0 errors; and the loaded Prime DLL hash is `61A67158…`.
5. **R12 public propagation** (`experiments/nu-r12-propagation/`, [record](nu-propagation-feasibility-2026-10-18.md)).
   - Command: `run_probe.py build --host .artifacts/r05-events-20261015/bin/Release/net10.0`, then `run_probe.py run`. The host is the preserved Windows R05 host, whose `Nu.dll` has the sealed hash `e96cd61d…` the guard requires. It is read only, and the runner copies it.
   - Pass: run exit 0 (completed mechanism check), with observations equal to the receipt.
6. **R01 platform** (`experiments/nu-r01-platform/`, [record](nu-platform-feasibility-2026-10-15.md)).
   - Command: the README's locked restore, build and run.
   - Pass: run exit 0. `dependencyCarryPositive` must be false for the moving condition, as recorded.
   - The project targets .NET 8. A per-user .NET 8 runtime is installed, and its version is recorded, because the Windows runtime patch version was not recorded.
   - Cross-platform: the three output hashes (`summary.json`, both traces) are compared with the receipt (`7F8E05FB…`, `FA73315E…`, `E715CEC5…`). Equal hashes would show identical single-precision physics on both platforms. A difference is recorded as a platform difference with the first differing step. It is not a failure, because Box2D.NET's arithmetic may differ between runtimes.

## What differs from Windows

- Linux; PowerShell 7.4.6 (per-user, as in the R02 check) runs the `.ps1` runners as `pwsh -NoProfile -File`, where the READMEs say `powershell`. The READMEs allow PowerShell 7.
- The runners use their own empty package caches, so packages come from nuget.org, hash-checked by NuGet.
- No display is needed: none of these opens a window.
- The preserved `.artifacts/` inputs are read only. A file list with sizes and modification times is taken before and after the batch, to show they did not change.

## What counts as a different result

Any runner failure, or any mismatch with the recorded Windows observations other than the declared expected differences (paths, assembly hashes, R01's trace hashes), is a **Linux difference**. It is recorded as found, not fixed and rerun. Environment-only fixes are allowed, each logged as its own attempt. No package byte changes. The five-failure stop rule applies per probe.

## What this check cannot show

Each probe keeps its original limits:
- compiler diagnostics and small pure functions (R04);
- a stub world (R05/R12);
- an isolated mapping (R10);
- a direct physics dependency without a Nu world (R01).

Passing shows only that these bounded observations reproduce on this server.
