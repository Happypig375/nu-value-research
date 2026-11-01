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

## Results (added 2 November 2026, after the runs)

**Conclusion: all six small probes reproduce on this Linux server.**
- R01's Box2D physics traces are bit-for-bit identical to Windows once Windows line endings are restored.
- R05 and R12 ran the very Nu binaries built on Windows and gave identical observations.
- One environment failure (R10 conversion attempt 01) exposed a real platform difference in the .NET SDKs.

| Probe | Result |
| --- | --- |
| R04 compiler diagnostics | Runner exit 0. **All six cases match `original-results.tsv`**: build exits, run exits 0/2/1/1/2/0, and unique and raw FS0025 counts. |
| R04 application diagnostics | Runner exit 0. **All four variants match Windows** in build exit, warnings (210/210/211/210), unique warnings (150/150/151/150), selected and total FS0025 (0/0/1/0) and prediction pass. Assembly hashes differ, as declared. |
| R05 events | Runner exit 0. **All three observations equal the receipt**: cascade `game,screen,group`; resolve-stop `game,screen`; unsubscribe `plain:before`. It used the Windows-built `Nu.dll` `5bcf797d…` unchanged. That is the build in the preserved source tree; the original R05 used the corrected build `e96cd61d…`, also from Windows. |
| R10 Prime conversion | Attempt 02: restore, build (0 warnings, 0 errors) and run exit 0. **8/8 cases pass**, and the loaded Prime DLL is `61a67158…`, equal to the receipt. |
| R12 propagation | Build and run exit 0, disposition `completed_pass`, on the preserved Windows R05 host (sealed `Nu.dll` `e96cd61d…`, copied exactly). **All records equal Windows** except for three excluded kinds of field: paths, the OS name and the list of loaded runtime assemblies. The other exception is the entity `Order` numbers, which Nu derives from the system clock (rate 10 MHz on Windows, 1 GHz on Linux; 11 distinct values on both). |
| R01 platform | Restore, build and run exit 0; `dependencyCarryPositive` false, as recorded. **`summary.json` and both traces are byte-identical to Windows after converting LF to CRLF** (`7F8E05FB…`, `E715CEC5…`, `FA73315E…`). It ran on the .NET 8.0.33 runtime, per-user. |

**Attempts, all retained** (`.artifacts/small-probes-linux-20261102/`):
- **R10 conversion attempt 01** failed at locked restore with NU1403. FSharp.Core 10.1.302 resolved from the Linux SDK's bundled `library-packs` folder has a different content hash (`wFeX…`) from the lock file's (`bN7X…`). The preserved Windows package cache shows the locked package came from the Windows SDK's own `library-packs`. **The two SDKs ship different FSharp.Core 10.1.302 packages under the same version, and the DLLs inside differ too** (`fsharp-core-dll-compare.txt`).
- **R10 conversion attempt 02** seeded its cache from the preserved Windows package cache (an environment-only fix, which the README allows: "or an existing package cache") and passed.
- The R03, R04, R06, R10 live-reload and R02 Linux runs earlier today seeded the same Windows cache, so they used the Windows FSharp.Core. The four PowerShell or Python runners here (both R04 probes, R05, R12) use their own empty caches. They therefore compiled against the Linux SDK's FSharp.Core and still matched.
- No other failures.

**Preserved inputs.** The file list (path, size, modification time) of `.artifacts/r03-feasibility-20261015/source` and `.artifacts/r05-events-20261015/bin` was identical before and after the batch (4,640 files).

**Not covered:** the R10 initializer-only schema reload and the R12 Terra Firma packages. They are larger native packages and need their own protocols.
