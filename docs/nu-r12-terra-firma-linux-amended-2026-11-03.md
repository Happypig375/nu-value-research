# R12 Terra Firma reopen pair on Linux, under a declared amendment (3 November 2026)

**Status: protocol fixed before any build or run.** Results are added afterwards in their own section and do not change this protocol.

## Why

On 2 November the unchanged Terra Firma package stopped at its asset stage on Linux ([record](nu-r12-terra-firma-linux-reproduction-2026-11-02.md)). Its asset check tests a Windows-only read-only file flag, which Linux files never have, so all 248 assets failed that one check. The asset bytes themselves were identical to Windows.

On 3 November the user decided (decision D9, item 8a in NEEDS-HUMAN) that this package should be reproduced on Linux through a declared, dated amendment, for example by treating file mode as the read-only signal, so that all results are consistently Linux.

The package ([record](nu-terra-firma-reopen-feasibility-2026-10-18.md), `experiments/nu-r12-terra-firma/`) loads Nu's existing 3D Terra Firma scene in a hidden real SDL/OpenGL world (L0), observes it, saves it, and reopens the saved bytes in a fresh process (L1). On Windows the pair passed the declared checks:
- the 197-entity correspondence;
- 166 explicit links;
- 11 saved source histories;
- selected properties of 32 palms and 4 villas;
- 0 invalid and 0 adverse findings;
- all 17 synthetic checker controls.

The question is: **does this pair pass on Linux, with only the declared amendment?**

Authority: user decision D9 (3 November 2026). This is the completed reopen pair, not the later Terra Firma revision series and not the stopped R12 material-intent draft (untracked, unopened). No new arm, no candidate or model call, nothing Daybreak-only.

## The amendment (the only change to the package)

`experiments/nu-r12-terra-firma-linux/linux_amendment.py` copies the committed package into a new scratch folder, checks every original file hash, and changes exactly these lines of `run.py` in the copy. The committed package is not touched.

| Line(s) | Windows original | Linux amendment | Why |
| --- | --- | --- | --- |
| 216 | an asset fails unless the Windows `FILE_ATTRIBUTE_READONLY` flag is set | an asset fails if its file mode has **any** write bit (owner, group or other) | On Linux, .NET's read-only attribute is the absence of write bits. This is the same check the Windows run made, expressed in the Linux signal. |
| 338 and 344 | records `st_file_attributes` of the L1 scene before and after replacing it | records it with `getattr(…, None)` | That attribute does not exist on Linux, so the L1 stage would crash before launching. The value is only recorded, never checked. |

## Two more Windows-bound steps, replaced without changing the package

- **Build acceptance.** `run.py run` requires `source-binary-seal.json` and `native-acceptance.json` in the build folder. On Windows these came from the parent's review scripts in `.artifacts/r12-propagation-20261018/`.
  - The seal is made with the same two scripts, run on copies: `inspect-terra-build.fsx` reads the PE/PDB metadata without loading the assembly, then `seal-terra-build.py` checks that all 8 original source units and the observer `Program.fs` match their recorded hashes.
  - The Windows acceptance script hard-codes the Windows DLL and PDB hashes, which differ on Linux because builds embed paths. It is replaced by `experiments/nu-r12-terra-firma-linux/accept_linux_build.py`. That script checks the same facts (ready flags, exit 0, PE/PDB seal 8+1, seal matches binary, Server GC and TieredPGO in the runtime config, package inputs unchanged, observer and protocol hashes) and writes the acceptance with my name on it. There is **no second reviewer**.
- **Output location.** `run.py` writes only inside `.artifacts/r12-propagation-20261018/` under its own repository root. As on 2 November, the scratch tree gets copies of the three authority files that `run.py` reads from there (hash-checked by `run.py`), so the preserved Windows folder is never written.

## What stays fixed

- Every other package byte: `Program.fs` (observer), the project file, `compare.py`, `check_controls.py`, `PROTOCOL.md`, `global.json`.
- The private prerequisites, read only and hash-checked by `run.py`:
  - the Nu archive `.artifacts/r03-feasibility-20261015/nu-064f7ae.tar`;
  - the existing Windows-built pipeline host (`.artifacts/r03-feasibility-20261015/source/Nu/Nu.Pipe/bin/Release/net10.0`);
  - the accepted Windows-built R05 runtime host (`.artifacts/r05-events-20261015/bin/Release/net10.0`).
- The stage order: `assets`, `build`, seal and acceptance, `run` L0, `run` L1 with L0 as predecessor, `compare.py`, then `check_controls.py` on the original scene.
- The 180-second deadline for each native run.

## What differs from Windows (environment only)

- `scripts/linux_nu_env.sh`: Xvfb on display `:96` with a private cookie and no TCP, Mesa llvmpipe with the OpenGL 4.6 override.
- A scratch NuGet cache seeded from `.artifacts/nuget-packages/`.
- **Assimp.** Terra Firma loads 3D models through Assimp. The R05 host was built on Windows and holds only `assimp.dll`; Nu at this revision looks for `libassimp.so` on Linux. The pinned archive itself ships `Nu/Nu/libassimp.so`. I put that one file, extracted from the hash-checked archive into a separate scratch folder, on `LD_LIBRARY_PATH` for the native runs, and record its hash. It is not copied into the application folder, so the protected application files stay as they are.
- Software rendering, so timing means nothing.

## Steps and pass conditions

1. **Assets:** exit 0 and `ready_for_parent_review` true, with all 248 expected outputs accounted for, including 120 transformed images. The published files must again be byte-identical to Windows `terra-assets-01` (they were on 2 November). If Nu.Pipe leaves write bits on Linux, the amended check fails; that is a Linux difference, not a reason to loosen the check.
2. **Build:** exit 0 with `ready_for_parent_review` true. Warning counts are recorded (Windows: 72 warnings, 0 errors).
3. **Seal and acceptance:** the seal finds 8 original units and 1 observer with matching PE/PDB identity, and `accept_linux_build.py` accepts.
4. **L0, then L1:** each exits 0 within 180 s with `complete_observation_and_save` true.
5. **`compare.py`:** disposition `passed_declared_checks` with scope `pair`, 0 invalid and 0 adverse, as on Windows.
6. **`check_controls.py`:** all 17 synthetic controls pass, as on Windows.
7. **Also recorded** (not pass/fail):
   - the L0 and L1 saved-scene hashes against Windows (both `0bdb814d…`);
   - the live-entity counts per observation (Windows: 233, with 36 generated protected entities);
   - the Linux findings and descriptive output against Windows `terra-comparison-01.json`.

   Nu's entity `Order` numbers come from a clock that runs differently on Linux, so byte differences in saved scenes are expected and are not failures by themselves.

## What counts as a different result

Any of these is a **Linux difference**. It is recorded as found, not fixed and rerun:
- a stage failure, crash or timeout;
- an invalid or adverse comparison;
- a control failure;
- a correspondence count different from Windows.

The stop rule applies: five unresolved failures at one unchanged step means stop that step. Environment-only fixes (display, library path, exact SDK) are allowed, and each is logged as its own attempt. A change to any package byte beyond the declared amendment would need a new written amendment first.

## What this check cannot show

The original limits stay: no decoded visual appearance or framebuffer check; no input; no native resource restoration; no propagation or revision; no authoring benefit. The asset check covers presence, container signatures, exact untransformed bytes and the read-only signal, not how textures look.

## Amendment 2 (3 November 2026, ~17:20 HKT), written after two L0 attempts and before any further run

**Attempts so far** (all retained in `.artifacts/r12-terra-linux-amended-20261103/`):
- Assets, build, seal and acceptance: all passed at the first attempt (details in the results section).
- **L0 attempt 01 failed** on an environment gap. The Windows-built host has only Windows physics natives, and the run stopped with `DllNotFoundException: libbulletc`. The pinned archive ships exactly two Linux natives in `Nu/Nu/`: `libassimp.so` (already declared above) and `libbulletc.so`. Attempt 02 adds `libbulletc.so` from the same archive to the same `LD_LIBRARY_PATH` folder. This is the same kind of environment fix as Assimp; no package byte changed.
- **L0 attempt 02 timed out.** All three callbacks ran. Both captures A and B were written, and the saved scene was written 18 s after launch. Its SHA-256 `0bdb814d…` **equals the Windows L0 and L1 saves**. Then the probe called `World.exit`, and the process never returned. No further callback ran. `run.py` killed it at the 180 s deadline (exit −9), so `complete_observation_and_save` is false, no `summary.json` exists, and L1 cannot start. That is a Linux difference: a hang after the engine was asked to exit.

**What I will do next, and only this:**
1. **L0 attempt 03, diagnostic only.** Same environment and inputs as attempt 02. A watcher waits for `saved-Scene.nugroup`, waits 20 s more, then records the managed thread stacks of the probe process with `dotnet-stack report` (Microsoft's diagnostics tool, installed in scratch). It may also record native thread names from `/proc`. **This attempt is not scored, whatever happens.** Even if it exits normally, it does not replace attempt 02, and it is never used as L1's predecessor.
2. If the stacks point to a cause **outside the package**, I may make **one** scored L0 attempt 04 with that environment-only fix, declared in a short dated note before the run. Examples of such causes: the audio driver, the display, or a native library. If attempt 04 is complete, L1, `compare.py` and the controls follow as planned. A fix that needs a package or engine change is out of scope; I stop and report it instead.
3. If the stacks don't show an environment cause, I stop the native stage here. Then `check_controls.py` (synthetic, never loads Nu) still runs, and the result stays "L0 observes and saves identically to Windows, but hangs on exit on Linux; L1 not reached".

The stop rule still counts every attempt at the L0 step, the diagnostic included: 01 environment, 02 hang, 03 diagnostic, 04 optional. That leaves no fifth try.

### Note before L0 attempt 04 (3 November 2026, ~17:15 HKT)

**Diagnostic attempt 03 (unscored)** hung the same way: same saved scene `0bdb814d…`, killed at 180 s. The stacks taken 20 s after the save (`.artifacts/r12-terra-linux-amended-20261103/L0-03-diagnostic/`) show the cause. **It is not a deadlock.**
- The main thread is in `World.cleanUp`, waiting (`Thread.Join`) for the renderer thread to finish.
- The renderer thread is still drawing a frame. It is building a reflection map (`LightMap.CreateReflectionMap` → `renderGeometry` → `DrawPhysicallyBasedDeferredLightMappingSurface`), and a Mesa software-renderer thread (`llvmpipe-0`) is running.
- On a GPU this frame is quick. On the software renderer, with the 4 renderer threads the wrapper sets by default (`LP_NUM_THREADS=4`), it takes longer than the rest of the 180 s budget.

That is an environment cause (rendering speed), so amendment 2 allows **one** scored attempt with an environment-only fix: **L0 attempt 04 sets `LP_NUM_THREADS=32`**, so Mesa's software renderer uses 32 threads instead of 4. `scripts/linux_nu_env.sh` already reads this variable; nothing else changes. If L0-04 is complete, L1 runs with the same setting. If L0-04 still times out, the native stage stops there.

## Results (added 3 November 2026, after the attempts)

**Conclusion: with the amendment, Terra Firma's asset preparation and build pass on Linux, and L0 loads, observes and saves the scene exactly as on Windows. Its two captures and its saved file are byte-identical to the Windows ones. But L0 never exits within the package's fixed 180-second deadline.** After the save, the engine's shutdown waits for one last software-rendered 3D frame (a reflection map), and that frame takes longer than the remaining time. More renderer threads did not fix it. So L0 never counts as complete, and **L1 (the fresh-process reopen) and the pair comparison were not reached.** The 17 synthetic checker controls pass.

| Step | Result |
| --- | --- |
| Assets | Exit 0 in 54 s, `ready_for_parent_review` **true**: 0 closure failures for all 248 expected outputs. Nu.Pipe gives the published assets mode `0444` (no write bits), so the amended read-only check passes. All **251 published files are byte-identical to Windows** `terra-assets-01`. The extra `AssetGraph.tracker` is reported as on Windows. |
| Build | Exit 0, `ready_for_parent_review` true, **72 warnings and 0 errors, as on Windows**. DLL `3879d069…`, PDB `76940c5f…` (different from Windows because builds embed paths). |
| Seal and acceptance | PE/PDB identity matches; 8 original units and 1 observer verified. `accept_linux_build.py` accepted with no failed check; the copied `App.config` equals Windows. |
| L0 attempt 01 | **Failed (environment):** `DllNotFoundException: libbulletc`. The Windows-built host has no Linux physics native. |
| L0 attempt 02 (+ `libbulletc.so` from the pinned archive) | **Timed out (killed at 180 s, exit −9).** All 3 callbacks ran, and captures A and B and the save were written 18 s after launch. Then shutdown never finished. |
| L0 attempt 03 (diagnostic, unscored) | Same hang. The thread stacks show the main thread waiting in `World.cleanUp` for the renderer thread, which is still drawing a reflection-map frame on the software renderer. Not a deadlock. |
| L0 attempt 04 (`LP_NUM_THREADS=32`) | **Timed out the same way** (save 15 s after launch, killed at 180 s). Per amendment 2, the native stage stops here. |
| L1, `compare.py` | **Not reached:** L1 requires a complete L0. |
| `check_controls.py` | Attempt 01 failed on my command (Python isolated mode `-I` hid the package's own `compare` module; nothing was written). Attempt 02: **17 of 17 controls pass, as on Windows.** |

**What L0 did observe, compared with Windows** (attempts 02 and 04 agree exactly):
- Captures `A.nugroup` and `B.nugroup`, `saved-Scene.nugroup` and its canonical form: all **byte-identical to Windows** L0 (`10ab23a3…`, `0bdb814d…`). The saved file also equals the Windows L1 save.
- Live entities in A and B: **233, with 36 generated protected entities**, the same as Windows.
- `original-expectations.json` differs in hash; it records paths.

These are observations from incomplete processes. They support "the load and save behave identically on Linux". They do not show the reopen, because L1 never ran.

**Attempts:** assets 1, build 1, seal 1, acceptance 1, L0 4 (one environment failure, two scored timeouts, one unscored diagnostic), controls 2 (one my command error). Nothing was rerun beyond what amendment 2 declared. Evidence: `.artifacts/r12-terra-linux-amended-20261103/`. That folder holds the receipts and observations of every L0 attempt, the build and seal records, the thread stacks, the hash lists of the two archive natives (`libassimp.so` `52321db7…`, `libbulletc.so` `0ddb5f81…`) and the asset hash list. I deleted the scratch trees and logged it in `DELETIONS.log`.

**Notes and limits.**
- The wrapper's environment log does not print `LP_NUM_THREADS`, because its filter pattern is too narrow. `wrapper-lp-check.txt` shows that the wrapper passes the value 32 through.
- The fix that would most likely complete L0 is a longer deadline or a GPU. A longer deadline is a package change (the 180 s deadline is frozen in `run.py`), so it would need a new written amendment and the user's agreement. I did not make it.
- The amendment, the build acceptance and the diagnosis were checked by me only, without a second reviewer.

## Amendment 3 (3 November 2026, ~17:45 HKT): longer deadline for the native runs, written before any further run

**Authority:** the user approved NEEDS-HUMAN item 9, relayed by the orchestrator on 3 November: extend Terra Firma's time limit on Linux so that L0 can exit and the reopen (L1) and the comparison can finish ("server time is practically free").

**The only new change.** `run.py` gives each native run (L0, L1) a 180-second deadline (line 366: `process(command, app, output, 180, environment)`). Amendment 3 raises it to **1,800 seconds per process**. The amendment script applies this only when called with `--deadline 1800`; without the option it makes exactly the amendment-1 copy (same `run.py` hash, `d12b17b1…`). `accept_linux_build.py` records the deadline in the acceptance file. Nothing is checked differently.

**Why 1,800 s.** In attempts 02 and 04 the save came 15–18 s after launch. Shutdown was then still waiting on the renderer when the process was killed, more than 160 s later. The last frame's real length is unknown; it is only known to be over about 160 s. 1,800 s allows more than ten times that. It still bounds a true hang to 30 minutes per process. Server time is cheap and the frame is a one-off at shutdown, so a generous bound is better than a tight guess that could waste the run.

**Everything else stays as in amendments 1 and 2:**
- the file-mode read-only signal and the `getattr` change from amendment 1;
- `libassimp.so` and `libbulletc.so` from the pinned archive on `LD_LIBRARY_PATH`;
- **`LP_NUM_THREADS=32`**, the software-renderer setting attempt 04 used;
- display `:96` (Xvfb, private cookie, no TCP), the OpenGL 4.6 override, the seeded NuGet cache, `nice -n 10`;
- the stage order and every pass condition in "Steps and pass conditions" above, including the comparison with Windows `terra-comparison-01.json`.

**Rebuilding first (required, not a rerun for a better result).** I deleted the scratch asset and build trees after attempt 04. `run.py run` needs them, and the build stage snapshots the package files, including `run.py`, so the build must be redone with the amended `run.py`. So the sequence is:
1. assets again (`linux-assets-02`) and build again (`linux-build-02`) from the amendment-3 copy;
2. PE/PDB seal and `accept_linux_build.py` again;
3. **L0 attempt 05**;
4. **L1 attempt 01**, with L0-05 as its predecessor;
5. `compare.py` on L0-05 and L1-01;
6. `check_controls.py` again. It is synthetic and never loads Nu, but it reads the amended `run.py` copy, so it is rerun once on the new copy.

The assets, build, seal and acceptance must pass as before: the same 251 asset hashes, the same 72 warnings and an 8+1 seal. If any of them fails or differs, that is recorded as a difference.

**Pass conditions** (unchanged from the protocol):
- L0 and L1 each exit 0 within the deadline with `complete_observation_and_save` true;
- `compare.py` gives `passed_declared_checks` with scope `pair` and 0 invalid / 0 adverse findings. That covers the 197 original entities, 19 roots, 166 explicit links, 11 saved source histories, 32 palms and 4 villas, as on Windows;
- all 17 controls pass.

Each process's exit time is recorded.

**What counts as a failure or difference:** any crash, timeout (now at 1,800 s), incomplete observation, invalid or adverse comparison, correspondence count different from Windows, or control failure. It is recorded as found, not fixed and rerun.

**Stop rule.** The count at the L0 step continues: attempts 01, 02 and 04 are failures, and 03 was an unscored diagnostic. If L0-05 fails, that is the fourth failure. One more environment-only attempt would then be allowed, declared in a dated note before it runs; after that, stop. L1 starts its own count at 01.
