# Daybreak branch B: ordinary screen serializer round-trip — source verification, design and protocol (2 November 2026)

**Status: protocol fixed before any build or run.** The results section is appended after execution and does not change this protocol.

Authority: user decision of 2 November 2026 assigning the two Daybreak-only branches to a Kimi K3 session via GitHub Copilot CLI; brief `.orchestration/TASK-daybreak-kimi.md`. This document covers **branch B** (ordinary screen serializer / runtime persistence, including export/import). Branch A (deliberate recovery fault-trigger) is not started: its private candidate is not on the server (NEEDS-HUMAN item K1, 2026-11-02), and the orchestrator directed this session to do branch B first.

All source statements concern Nu `064f7ae92a8506689cd91aff5e6804a375d6ef3d` (archive `.artifacts/r03-feasibility-20261015/nu-064f7ae.tar`, SHA-256 `eb0aa771…f92b`, re-verified 2 November) and Prime 11.5.1 (NuGet package in `.artifacts/nuget-packages/prime/11.5.1/`; the DLL's informational version reads `11.5.1+4026f3156865d536d0c4d36f1dc361485df8117a`, and the Prime source at that commit was fetched from GitHub for reading only; archive SHA-256 `2ec5b546…8766c`). Both source trees were read from copies in scratch, never modified.

The private delegated source candidate (`screen-persistence-source-20261025/`, expected evidence hash `abe47eac…2e18`) is not on the server, so nothing below checks it. Every claim is verified here directly against the pinned sources. If the candidate arrives later, its claims can be compared against this note.

## 1. Source-verification note (branch B decisive routes)

Format: claim — citation — verdict. "Verified" means read directly at the pinned revision on 2 November 2026.

1. **A screen file is a `ScreenDescriptor`: dispatcher name + screen properties + group descriptors.** `World.writeScreen` writes the dispatcher name, writes all screen-state properties except `Order`, and appends `World.writeGroups` of the screen's groups. `Nu/Nu/World/WorldScreen.fs:257-266` — **verified**.
2. **`World.writeScreenToFile` writes that descriptor as pretty-printed symbolic text, via a temp file then rename.** `WorldScreen.fs:276-285` — **verified**.
3. **Groups and entities created by the MMCC/ImSim content API are excluded from screen and group files.** `writeScreens`/`writeGroups`/`writeEntities` each filter to `GetPersistent && GetProtection <> DeclarativeProtection` (`WorldScreen.fs:269-274`, `Nu/Nu/World/WorldGroup.fs:239-246`, `Nu/Nu/World/WorldModuleEntity.fs:2454-2466`), and the content API sets `DeclarativeProtection` on the entities, groups and screens it creates (`Nu/Nu/World/WorldContent.fs:225,252,291,313`). MMCC Breakout declares its `GameplayScene` group and all gameplay entities through `Content` (`Projects/Breakout Mmcc/Gameplay.fs:230-310`), so a Gameplay screen file contains **no group or entity content** — **verified**. Consequence: the file carries the screen's own state (including the model); live entity content is not in the file and can only be rebuilt by the content API from the model.
4. **`World.writeScreen` (singular) applies no persistence/protection filter to the screen itself** — the filter exists only in `writeScreens` (plural, game-level). `WorldScreen.fs:257-266` vs `267-274` — **verified**. A declaratively protected screen can therefore still be exported individually via `writeScreenToFile`.
5. **The screen `Model` is written.** `Constants.Engine.NonPersistentPropertyNames` (`Nu/Nu/Core/Constants.fs:114-163`) excludes `Dispatcher`, `Content`, `Protection`, `Id`, the game eye frusta, `TransitionState`, `Nav3d`, and entity transform-derived/publishing flags; `Model` is **not** excluded, and `Name` is excluded only when generated (`Nu/Nu/Overlayer/Reflection.fs:99-103`, `isPropertyNonPersistent`). Written with the screen are therefore: `Model`, `Persistent`, `Incoming`, `Outgoing`, `RequestedSong`, `SlideOpt`, `Name`, plus any persistent Xtension properties; excluded are `Dispatcher`, `Content`, `Protection`, `TransitionState`, `Nav3d`, `Order`, `Id` — **verified** (writeMemberProperty/writeXtension: `Reflection.fs:373-410`; `writeScreen`'s own predicate additionally drops `Order`).
6. **`ScreenState.Model` is a Prime `DesignerProperty`** (`DesignerType : Type`, `DesignerValue : obj`). `Nu/Nu/World/WorldTypes.fs:1083-1099` — **verified**.
7. **`DesignerProperty` round-trips through Prime's `SymbolicConverter` as `[<assembly-qualified type name> <value symbol>]`.** Write: Prime `SymbolicConverter.fs:79-85` (commit `4026f31`, version 11.5.1). Read: `SymbolicConverter.fs:386-401`. Nu's reader additionally requires the first element to be a `Text` naming a resolvable type before attempting conversion (`Reflection.fs:233-244`, `tryReadMemberProperty`) — **verified**. The Breakout `Gameplay` record is a plain `[<SymbolicExpansion>]` record of int64, union, nested records, `Map<string, Brick>` and ints (`Gameplay.fs:54-70`), all within the converter's generic record/union/map support — **verified** by reading; actual round-trip is checked at runtime as a declared gate (§4).
8. **`World.readScreenFromFile` parses the descriptor and calls `World.readScreen`** (`WorldScreen.fs:328-332`). `readScreen` looks up the dispatcher by name (fails if absent), makes a fresh `ScreenState`, attaches dispatcher property definitions, reads file properties onto it, optionally overrides the name, then `World.addScreen true …` and `World.readGroups`, then `WorldModuleInternal.tryProcessScreen true` (`WorldScreen.fs:287-322`) — **verified**.
9. **`addScreen true` replaces an existing same-address screen state; only a newly added screen is registered.** `Nu/Nu/World/WorldModuleScreen.fs:470-475` — **verified**. (This matches the corrected claim in the reviewed 25 October note; the original independent review's contrary claim was wrong.)
10. **`readScreen` contains no local transaction and no child cleanup.** Nothing in `readScreen` destroys groups/entities that existed before the import, and nothing restores the pre-import state on failure (`WorldScreen.fs:287-322`) — **verified**.
11. **Zero-process is a no-op for MMCC screens.** `tryProcessScreen` calls `dispatcher.TryProcess` (`Nu/Nu/World/WorldImSim.fs:54-56`); `TryProcess` is overridden only by the ImSim dispatchers (`Nu/Nu/World/WorldModule2.fs:2174,2561,2787,3012`), and the base default is `()` (`Nu/Nu/World/WorldTypes.fs:544-545`). The MMCC screen dispatcher (`WorldModule2.fs:2830`) does not override it — **verified**.
12. **MMCC content re-synchronizes when the model is set, not every frame.** `setScreenModelGeneric`/`setScreenModelProperty` call `dispatcher.TrySynchronize` on change (`WorldModuleScreen.fs:129-138,158-169`); `notifyScreenModelChange` forces the same (`WorldModuleScreen.fs:487-490`). MMCC `Register` sets the model with `initializing=true`, converting an existing value or falling back to the constructor-argument initial model (`WorldModule2.fs:2848-2863`) — **verified**.
13. **`GameplayDispatcher.GetFallbackModel` returns `Gameplay.initial` when the screen is selected, else `Gameplay.empty`** (`Gameplay.fs:196-199`), and the fallback is consulted only when the stored model cannot be converted to the requested type (`WorldModuleScreen.fs:140-156`, `getScreenModelGeneric`) — **verified**. An imported, type-correct `Gameplay` value is therefore not overwritten by the fallback.
14. **Selection resets the model.** `Screen.SelectEvent => StartPlaying` and the `StartPlaying` handler set `Gameplay.initial`, which generates fresh random brick names and colors (`Gameplay.fs:206-208,213-216,75-83`) — **verified**. Any import that is followed by a screen (re)selection loses the imported model. The protocol's import policy must not re-select the screen after import.
15. **Destroying a screen does not clear or republish the game's selected-screen field.** `destroyScreenImmediate` unregisters the screen, destroys its groups and removes its state (`WorldScreen.fs:201-211`); `setGameSelectedScreenOpt` only fires on an actual value change (`Nu/Nu/World/WorldModuleGame.fs:115-154`) — **verified**.
16. **Content sync with an empty old content creates declared groups/entities that are missing and never removes existing ones.** `Content.synchronizeScreen` differentiates old versus new declared children; removals come only from the *old* declared set. Groups added are read from their `.nugroup` file when declared `groupFromFile`, or created, then synchronized with `GroupContent.empty` (`WorldContent.fs:257-293`). Prediction for an import that leaves pre-import entities in place: stale entities survive alongside the newly declared ones — **verified as source route; runtime behavior is the diagnostic arm's observation** (§3).
17. **Gaia at this revision has no screen-file command.** The editor exposes Save Group (Ctrl+S) and Save Entity only (`Nu/Nu.Gaia/Gaia.fs:2595,2622,1862`; group save/load wrappers at `Gaia.fs:1169-1222`); `writeScreenToFile`/`readScreenFromFile` have **no caller anywhere in the pinned tree** outside their definition (whole-tree search, 2 November) — **verified**. The screen-file route is therefore an engine API route, not an existing editor workflow; this experiment characterizes the API, not a UI feature.
18. **Group-level save is insufficient for a gameplay checkpoint** (it omits the parent screen's model): `writeGroupToFile` writes one group's descriptor only (`WorldGroup.fs:248-257`) — **verified**. (Already established in the 25 October note; re-confirmed here.)

No claim read for this branch came out wrong; none remains unresolved that blocks the design. The previous session's reviewed note (`docs/nu-recovery-target-and-serialization-2026-10-25.md`) is consistent with the above on every point it covers, including its corrected replacement claim (item 9).

## 2. Typed round-trip design

**What is written:** one `ScreenDescriptor` file for the `Gameplay` screen, produced by `World.writeScreenToFile` from the live, halted screen. The typed value written and read back is `ScreenDescriptor`; the gameplay state travels inside it as the `Model` property, a `DesignerProperty` symbol `[<assembly-qualified name of Breakout.Gameplay> <gameplay value symbol>]`.

**What is read back:** `World.readScreenFromFile` → `World.readScreen` → a fresh `ScreenState` whose `Model` is the file's `Gameplay` value, installed at the same screen address via `addScreen true`.

**Type identity across processes:** the same pinned Breakout assembly defines `Gameplay` in both processes, so the assembly-qualified type name in the file resolves (`Type.GetType`) in the reader. The runtime gates include an explicit `scvalue<Gameplay>` round-trip of the exported model symbol (export side) and full field equality against the B0 reference (import side).

## 3. Destination, selection and content policy

- **Destination file:** one transfer file, `transfer/gameplay-screen.nuscreen`, written by the export arm and consumed by the import arms. It is data produced by the experiment and is preserved as evidence. The transfer directory must be empty before the export arm (same discipline as the B0 checkpoint directory).
- **Which screen:** only the `Gameplay` screen. No other screen is exported or imported. The game and the `Splash`/`Title` screens are out of scope.
- **Selection:** the Gameplay screen is already selected and idling in Gaia's Gameplay edit mode when the experiment acts (same starting posture as the accepted B0 probes). The import never re-selects the screen afterwards, because selection fires `StartPlaying` and would reset the model (item 14). The screen's selected/idling state is asserted again after import.
- **Primary import policy (arm `import`): existing-address state replacement with prior group destruction.** While halted: (1) destroy the screen's existing groups immediately (`World.destroyGroupsImmediate (World.getGroups …)`), removing all pre-import gameplay entities; (2) `World.readScreenFromFile` replaces the screen state (the screen is not new, so no re-registration, item 9); (3) `World.notifyScreenModelChange` forces one content synchronization, which rebuilds the group (from `Assets/Gameplay/Scene.nugroup`) and every declared entity from the imported model with an empty old content (item 16). Rationale: the file carries no children (item 3), so the policy must remove pre-import children explicitly; destroying the screen itself is avoided because the editor holds it selected (item 15) and destroying a selected screen is the riskier editor-state interference.
- **Diagnostic arm (`replace-nodestroy`):** same as `import` but without step (1). Declared prediction: the imported model is installed correctly (model equality holds), but the 30 pre-import brick entities survive beside the 29 imported ones (59 brick sprites; entity-name set differs from the B0 reference). Either outcome is recorded; a falsified prediction is reported as such, not treated as a probe failure.
- **Content policy (what counts):** the file is expected to contain the screen dispatcher name, `Model`, `Persistent`, `Incoming`, `Outgoing`, `RequestedSong`, `SlideOpt`, `Name`, and zero group descriptors. The export arm parses the file back and records the actual property set and group count as data; the round-trip claims below are about the model and the rebuilt content, not about byte-level file completeness.

## 4. The one common outcome check

Reference: the B0 checkpoint values observed in the closed history-04 process — `experiments/nu-history-b1/checkpoint/gameplay.symbol` (SHA-256 `ffee72d9…bc783a`; the 7-field model) and `experiments/nu-history-b1/checkpoint/projection.json` (SHA-256 `f62c9f3a…3cbd`; the projected entity observation with keys names, paddle, ball, bricks, scoreText, messageText, rotation). The old process is closed; these are independent expected data only, and a reproduced state is **not** a resumed historical world.

**The check (both must hold at a halted boundary in the import arm's fresh process):**
1. **Model equality:** `Simulants.Gameplay.GetGameplay world` equals the B0 model field-by-field with bit-exact single-precision encodings (same `modelData`/`equalModel` encoding as the reviewed reference observer).
2. **Projection equality:** the projected entity observation (all scene entity names; paddle/ball/brick positions, sizes, colors; score and message text; static-model rotation; `projectionErrors` empty) serializes to exactly the reference `projection.json` string.

**Negative controls (declared before running):** in each arm, the freshly started game (30 randomly colored bricks, score 0) must fail both the model equality and the projection equality against B0 before any intervention; a control that passes invalidates the arm. The export arm additionally requires the post-install, pre-export state to pass the full check (otherwise the export's input was not B0).

## 5. Protocol

Harness: the same functional, accompanied Gaia harness as the accepted B0/B1 and R04 packages — `Nu.initPlus` + `Gaia.run` with `ProjectEditModeOpt = Some "Gameplay"`, static 60-update timing, and the narrow opt-in research bridge (a post-ImGui-postprocess callback) installed into an isolated copy of the pinned Gaia source. The bridge text is byte-identical to the one in `experiments/nu-history-b0/prepare.py` (its snapshot/undo members are unused here). Application code is unchanged. The probe is a separate assembly referencing Gaia and the Breakout project, so Gaia gains no static Breakout dependency.

**Arm `export`:**
1. First callback: assert halted, Gameplay selected and idling, functional mode, initial contract (score 0, 30 bricks, Playing). Run both negative controls. Install the B0 model via the application's supported setter (`Simulants.Gameplay.SetGameplay`), exactly as the accepted B0 fresh reconstruction did.
2. Next halted boundary: require the full common outcome check against B0 (this certifies the export's input). Then `World.writeScreenToFile` the Gameplay screen to the transfer file. Parse the file back as `ScreenDescriptor`; record dispatcher name, sorted property names, group-descriptor count, and whether the `Model` symbol converts back to a `Gameplay` equal to B0. Emit all of this as trace data.
3. Next halted boundary: require the common check again (export did not disturb the world). Exit 0.

**Arm `import`:** fresh process, empty transfer check waived (file must exist and match the export arm's recorded SHA-256).
1. First callback: same assertions and negative controls. Destroy the screen's groups; record that the gameplay entities are gone. `World.readScreenFromFile` the transfer file; `World.notifyScreenModelChange`.
2. Next halted boundary: require the full common outcome check (§4), plus halted and Gameplay selected/idling. Exit 0.
3. Failure of any requirement exits 1 with the failing label in the trace.

**Arm `replace-nodestroy` (diagnostic):** as `import` without the group destruction. At the next halted boundary require model equality, and record the entity-name set versus B0 as data. The run passes if the observation completes and the model matches; the projected names are expected to diverge (59 brick sprites), which is the declared prediction, recorded either way.

**Execution rules:** SDK 10.0.302 (per-user install, `DOTNET_MULTILEVEL_LOOKUP=0`); isolated source copy in scratch (archive hash re-verified by `prepare.py`, which also refuses to patch a modified Gaia.fs); NuGet cache seeded from `.artifacts/nuget-packages/` into a private scratch cache; Xvfb display `:94` with an Xauthority cookie, `-nolisten tcp`, Mesa software OpenGL with `MESA_GL_VERSION_OVERRIDE=4.6 MESA_GLSL_VERSION_OVERRIDE=460` (the environment-only fix established by the R04 Linux reproduction), `LIBGL_ALWAYS_SOFTWARE=1 SDL_VIDEO_DRIVER=x11`; 600-second process deadline per run; every attempt preserved under `.artifacts/daybreak-screen-persistence-20261102/`; five unresolved failures at one unchanged step stop that step and are reported; environment-only fixes are allowed and logged as separate attempts; the probe, oracle and sources are frozen once the first run starts. Builds and runs happen only after this document and the package are committed.

**What this experiment cannot show:** preservation of anything outside the file and the model-derived content: native/physics state, audio already emitted, eye/camera state, transition state, event journals and tasklets, Gaia's own editing state, RNG continuation, and any resumed old process. Rendering parity with Windows is not claimed (software renderer). This is a serializer round-trip characterization at one checkpoint in one application and mode — not a benefit claim, not a UI workflow, and not a history-free-memory arm.

## Results (appended after execution)

**Conclusion: export works and writes exactly the verified scope; the stock import API is broken at the pinned revision.** `World.writeScreenToFile` produced the expected file from the live halted screen, and the model inside it round-trips to B0 through the symbolic format. `World.readScreenFromFile` cannot install it: `World.readScreen` constructs the imported screen at a one-name address (`Screen (ntoa screenState.Name)`, `WorldScreen.fs:309`) instead of the game-rooted two-name address used everywhere else (`Game.Handle / name`, e.g. `createScreen4` at `WorldScreen.fs:228`). Both import arms crashed with the same engine exception before any observation. The branch-B question "saved through the ordinary serializer and loaded back so that B0 is reproduced" is answered: **export, yes; stock import, no — a reproducible engine defect, observed, not inferred.**

### Attempts (all preserved; evidence in `.artifacts/daybreak-screen-persistence-20261102/`)

Builds: attempt 01 — operator shell error (`dotnet` not on PATH; nothing ran). Attempt 02 — compile error FS0072 (probe `world` parameter needed a type annotation). Attempt 03 — compiled, but probe DLL not used further. Attempt 04 — compile error FS0001 (one missed lazy-reference use). Attempt 05 — **compiled** (probe `c3c010d7…8fb7`, Breakout DLL `1ca025c3…908c`). Runs:

| Run | Outcome | Detail |
| --- | --- | --- |
| export-01 | failed in 0.37 s (SIGABRT) | Probe construction bug: parsed the B0 reference before `Nu.initPlus` registered Nu's math converters. Never reached the engine. |
| export-02 | **passed** in 28.7 s | Negative controls rejected the fresh board; B0 installed via the supported setter; full common check passed before and after export. |
| import-01 | **failed** in 22.3 s | `InvalidCastException` (`Nu.Screen`→`Nu.Group`) inside `readScreenFromFile`, during first-time MMCC content sync. |
| replace-nodestroy-01 | **failed** in 23.3 s | Identical exception without the group-destruction step, so the defect is in the import API itself, not in this policy. |

The orchestrator's stop rule (two failures at the same step) is met at the import step; the crash is deterministic by construction (see below), so no further identical reruns were spent.

### What the export file actually contains (observed)

`transfer/gameplay-screen.nuscreen`, 3,045 bytes, SHA-256 `a1827a05…c3e6f`: dispatcher `GameplayDispatcher`; exactly the properties `Incoming, Model, Name, Outgoing, Persistent, RequestedSong, SlideOpt`; **zero group descriptors** — the declaratively protected `Scene` group and its entities are excluded, matching the source reading. The `Model` property parses back to a `Gameplay` value bit-equal to the B0 reference. So the file carries the complete screen model and declared screen properties, and no live entity content — as the protocol predicted from source.

### Why import fails (observed exception + source mechanism)

Stack: `readScreenFromFile` (`WorldScreen.fs:331`) → `readScreen` (`:310`) → `addScreen` (`WorldModuleScreen.fs:474`) → `registerScreen` (`:456`) → MMCC `Register` (`WorldModule2.fs:2863`) → `TrySynchronize` → `Content.synchronizeScreen` (`WorldContent.fs:277`) → `InvalidCastException: Unable to cast object of type 'Nu.Screen' to type 'Nu.Group'`.

Mechanism: `readScreen` builds the screen as `Screen (ntoa screenState.Name)` — a one-name address (`[|"Gameplay"|]`), while the real screen lives at the two-name game-rooted address (`[|"Game"; "Gameplay"|]`). Two consequences, both observed in the trace: (1) `getScreenExists` misses the existing screen, so the import is treated as a new screen and re-registered; (2) content sync derives child addresses from the wrong parent names, producing two-name addresses that `deriveFromNames` (`WorldSimulant.fs:237-248`: length 2 → Screen, 3 → Group) maps to `Screen`, which the sync then casts to `Group` — the crash. Without MMCC content the same defect would silently install the imported state at an address nothing else reads. This path has no callers anywhere in the pinned tree (§1 item 17), so the defect was never exercised at this revision. Whether later Nu revisions fixed it was not checked (out of scope).

### Interpretation and limits

- What round-trips through Nu's ordinary serializer: the screen's declared properties and the complete seven-field gameplay model, bit-exact, verified against the closed history-04 B0 reference on the export side (`modelRoundTripEqualsB0: true`; common check passed pre- and post-export).
- What does not round-trip through the stock API: installation of that file back into a world. The import defect blocks the declared common outcome check in the fresh process, so **no claim of reproduced B0 state after import is made**. The negative controls and export-side checks did pass, so the export half of the round-trip is genuinely evidenced.
- The diagnostic arm's frozen prediction (stale entities survive a no-destroy replace) was not reached: the same API defect crashes first. Recorded as not-observed, neither confirmed nor falsified.
- Out of scope as before: native/physics state, audio, eye/camera, transitions, journals/tasklets, editor state, RNG continuation, resumed processes; no benefit claim; rendering parity not claimed (software renderer, Mesa override as in the R04 Linux reproduction).
- Costs so far: one authored probe (~280 lines) plus scripts reusing the reviewed harness; 5 builds and 4 runs; the whole cycle (fix, build ~90 s, run ~25 s) is cheap, but correcting the engine defect means patching engine source — a different evidence class (adapted source), not the ordinary API, and not done here.

### Next step (not started)

A written amendment could test a corrected import (engine patch rooting the address at `Game.Handle`, or a caller-side descriptor walk using only public APIs — none exists, since `addScreen` is internal) to answer whether the file format round-trips once the addressing defect is removed. That is a new question with a different evidence class; it needs its own protocol first.

## Amendment: corrected-import arms (written 2 November 2026, ~19:20 HKT, before any build or run)

**Status: protocol fixed before building or running.** Results go in their own section below and do not change this amendment.

**Authority.** User decision D41 (2 November, about 19:10 HKT, relayed by the orchestrator) approves re-running the import test with the one-line fix, and says Claude may run this harness. This covers only the corrected-import rerun described here. It does not open branch A or any other Daybreak work.

**Question.** Once the one-line address bug in `World.readScreen` is removed, does the exported screen file load back into a fresh process so that the B0 state is reproduced (the common check in §4)?

**Evidence class.** This uses **adapted engine source**: pinned Nu 064f7ae plus one changed line. It is not the stock API. The finding above stands unchanged: stock import is broken at 064f7ae.

**The change.** `Nu/Nu/World/WorldScreen.fs` line 309, in `readScreen`: `Screen (ntoa screenState.Name)` becomes `Game.Handle / screenState.Name`. This is the address form `createScreen4` already uses. The same fix is upstream as bryanedds/Nu#1466. A new script, `apply_import_fix.py`, applies it after `prepare.py`. It refuses to run unless the file matches the archive byte for byte and the old line appears exactly once, on line 309. Its receipt must show that only line 309 changed.

**Not a blind test.** An engineering check of the fix, outside this protocol, already ran these three arms with the same patch (`~/workspace/nu-import-fix/fix-evidence/daybreak-064f7ae-patched/`, 2 November, about 16:50 HKT). It found:
- **export:** the same file hash, `a1827a05…`;
- **import:** passed;
- **replace without destroy:** 47 entities, 30 brick entities against 29 bricks in the model.

So this run repeats that check under a written protocol. It is not a fresh prediction. The diagnostic arm's prediction stays as it was frozen in §3: stale entities survive, giving 30 + 29 = 59 brick entities. I do not revise it.

**What stays the same.** These files are unchanged and used as committed: `prepare.py`, `Probe.fs`, `Probe.fsproj`, `build.py`, `run.py`, `linux_run.sh` and `compare.py`. The same goes for the B0 reference (`experiments/nu-history-b1/checkpoint/`), the arm definitions, the pass conditions in §4 and §5, the 600-second limit per run, and the Linux environment (Xvfb on `:94`, Mesa software OpenGL with the 4.6 override).

**Environment only.** `NUGET_PACKAGES` points at a private scratch copy of `.artifacts/nuget-packages/`. This avoids the FSharp.Core package difference between the Windows and Linux SDKs, as in the other Linux checks. The runs root is in scratch. Evidence is copied to the new folder `.artifacts/daybreak-screen-persistence-20261102/corrected-import/`. Kimi's existing evidence files are not touched.

**Order:**
1. `prepare.py` (fresh extract, then the Gaia bridge);
2. `apply_import_fix.py`;
3. `build.py`;
4. arm `export` 01, starting with an empty transfer folder;
5. arm `import` 01;
6. arm `replace-nodestroy` 01;
7. `compare.py`.

**Pass and fail, fixed now:**
- **Patch:** the receipt lists only line 309 as changed. Anything else stops the run before building.
- **Build:** exits 0.
- **Export:** passes under the original conditions. The negative controls must reject the fresh board, and the full check must pass before and after the export. I expect the file SHA-256 to be `a1827a05…`. A different hash is recorded as a difference; on its own it is not a failure.
- **Import (the main result):** passes only if **all** of these hold:
  - exit 0 with no timeout;
  - the trace ends with `result.pass = true` at phase `verified`. That means the negative controls rejected the fresh board, the groups were destroyed, and at the next halted boundary the model and the projected scene both equal B0, with the world halted and Gameplay selected;
  - `compare.py` reports `transfer_hash_agreement = true`.

  Anything else means the corrected import **fails**, and the failure is recorded as found.
- **Replace without destroy (diagnostic):** the arm passes, as before, if the observation completes and the model equals B0. The frozen prediction counts as confirmed only if `predictionObserved` is true (59 brick entities and a projection that differs from B0). Otherwise it is falsified, and I report the actual counts.
- **Declared follow-up analysis (reading traces only, no reruns):** from the `post-import-diagnostic` observation, compare the brick entity names on screen with two lists: the 30 names on the freshly started board (`initial`) and the 29 names in the B0 model. This says which entities are actually present.

**Rules.** Each arm runs once. If an arm fails, I record the failure and do not tune anything. Environment-only fixes are allowed and logged as new attempts. Five unresolved failures at one unchanged step means stop. The probe, the comparison script and the reference are frozen.

**Limits.** All limits in "What this experiment cannot show" still apply. This run also cannot say anything about stock Nu at 064f7ae, about later Nu revisions, or about an editor workflow. Gaia has no screen-file command.

**Cleanup.** After the evidence is copied and checked, the scratch source tree, build outputs and NuGet copy are deleted, and the deletion is logged here.

## Corrected-import results (added 2 November 2026, ~19:50 HKT, after the runs)

**Conclusion: with the one-line address fix, the screen file loads back and reproduces the B0 state exactly.** The main import arm passed every condition fixed in the amendment, at the first attempt. So Nu's screen file format does round-trip the gameplay state once the addressing bug is removed. Stock Nu at 064f7ae still cannot do this: the result comes from adapted engine source, as the amendment states.

**Attempts.** One of each step, and none failed: prepare, patch, build, three runs and the comparison. Evidence is in `.artifacts/daybreak-screen-persistence-20261102/corrected-import/`. Kimi's earlier evidence in the parent folder was not touched.

| Step | Result |
| --- | --- |
| Patch | Receipt: only line 309 of `WorldScreen.fs` changed (SHA-256 `2ccf6378…` → `cd53e3d7…`). The Gaia bridge was installed as before (`19964b82…`). |
| Build | Exit 0 (probe `6d5e20ab…`, Breakout `a10e0e86…`; DLL hashes include build paths). |
| export-01 | **Passed** in 27.8 s. The negative controls rejected the fresh board, and the full check passed before and after export. The file is 3,045 bytes with SHA-256 `a1827a05…c3e6f`, **identical to Kimi's stock-engine export**. That is expected: the patch touches only the read side. |
| import-01 | **Passed** in 27.2 s: exit 0, `result.pass = true` at phase `verified`. Both negative controls rejected the fresh board. The `Scene` group was destroyed and the file was read back. At the next halted boundary, the model and the projected scene both equal B0, with the world halted and Gameplay selected. `compare.py` reports `transfer_hash_agreement = true`. |
| replace-nodestroy-01 | **The arm passed** in 27.3 s: the observation completed and the model equals B0. **The frozen prediction is falsified:** `predictionObserved = false`. There were 47 entities and 30 brick entities against 29 bricks in the model, not 59, and the projection differs from B0. |

These numbers match the earlier engineering check outside this protocol: same export hash, import passed, and 47/30/29 in the diagnostic arm.

**Why the prediction failed (declared trace analysis, `diagnostic-name-analysis.json`).** The freshly started board and B0 share brick names: the brick names come from the same deterministic startup. The 30 bricks on the fresh board include all 29 B0 bricks, plus `@449`, which had already been destroyed by the time B0 was saved.

After the no-destroy import:
- **The 29 bricks in the model are on screen**, at the model's positions and colours (no projection errors).
- **One stale entity, `@449`, survives** because nothing removes it.
- No other entity is present beyond the 17 non-brick scene entities.

So the direction of the prediction held: content that is not in the imported model survives a replace without destroy. The count was wrong, because the prediction assumed the old and new brick names would not overlap. The shared names mean content sync updated the 29 existing bricks in place instead of adding new ones.

**What this adds to branch B:**
- **Round-trip with the fix:** export plus corrected import reproduces the B0 model and projected scene in a fresh process, checked against the closed reference with negative controls. This is a reproduced state, not a resumed historical world.
- **Policy matters:** importing without first removing the screen's existing groups leaves stale entities. Here that was one leftover brick, an extra live object that the model does not know about. The protocol's destroy-then-import policy is needed.
- **Unchanged:** stock import at 064f7ae is broken. Nothing here covers native or physics state, audio, camera, transitions, journals, editor state, random-number continuation, later Nu revisions, an editor workflow or any benefit. Rendering parity is not claimed (software renderer).

**Cleanup (logged).** After the evidence was copied and hash-checked, I deleted:
- this session's scratch source tree (3.1 GB);
- the build tree (645 MB);
- the NuGet cache copy (1.0 GB).

All of it can be rebuilt from the archive, `prepare.py`, `apply_import_fix.py` and `build.py`. My Xvfb on `:94` is stopped. Kimi's scratch `/tmp/kimi-daybreak-20261102/` was already gone when I checked.
