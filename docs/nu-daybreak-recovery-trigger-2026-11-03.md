# Branch A: deliberate recovery fault trigger — source check, eligibility and protocol (3 November 2026)

**Conclusion first.**
- **Eligible.** An ordinary exception thrown by the game's own code while the game runs inside Gaia (Nu's editor) does reach Gaia's existing recovery path. I checked every link of that path in the pinned Nu source.
- **The named fault:** a deliberate integer division by zero in Breakout's own gameplay message handler. It fires when the gameplay clock reaches 30 updates. This copies the method Nu's maintainer used in 2017 to test this same recovery feature.
- **What recovery should give, by source reading only:** the world as it was at the last editor snapshot, halted. Work since that snapshot is lost, and the code is not repaired, so the same fault fires again. Sound already played and the random-number state are not rewound.
- **Nothing was built or run.** Section 4 is the protocol for the build/run step. The orchestrator gives that step to the Kimi K3 lane, with a credit ceiling.

## 0. Authority and scope

- **User decision D9 (3 November 2026, relayed by the orchestrator), item K1:** reproducing branch A is approved. This Claude Opus session does steps 1 and 2: the source-verification note and the written eligibility decision. If eligible, it writes the protocol and stops. It must not build or run a fault trigger.
- **The private draft is still missing.** The earlier worker's unaccepted candidate (`value-preparation/recovery-reachability-20261025/`, evidence SHA-256 `e137ca45…f7f3`, coverage `713082c7…235e`) is still not on this server (checked 3 November under `~/workspace/home-port/.orchestration/rescued/nu-value-recovery*/` and `local/home-port-external-20261031/`). So every claim below comes from **my own reading**, not from checking that draft. If the draft arrives, comparing it against this note is a separate, later pass.
- **Unchanged rules:** R03 native-001 stays final. The R02/R10/R12 returned drafts were not opened. No candidate, participant or paid run. This note is source reading only. It is not a build, a runtime observation or a benefit claim.

## 1. Sources read

- **Nu**, commit `064f7ae92a8506689cd91aff5e6804a375d6ef3d`. Archive `.artifacts/r03-feasibility-20261015/nu-064f7ae.tar`, SHA-256 `eb0aa77197de1971d79aa0657c2af5cf33b99ba8302a24ba44f3306cca4bf92b` (re-checked 3 November). I extracted it to session scratch, outside the repo, and read it without changes.
- **Prime 11.5.1**, source at commit `4026f31` (GitHub archive SHA-256 `2ec5b546…8766c`, the same archive the branch B work used). No link in this path turned out to need it: the event dispatch code (`EventGraph`) is inside Nu at this revision.
- **Nu history on GitHub:** commits `a4a3de4` and `c4f76ed` (11 February 2017, issue #151), read with `gh api`.
- **Already-integrated background:** [recovery target and serialization](nu-recovery-target-and-serialization-2026-10-25.md) and the [R03 B0 package](../experiments/nu-history-b0/README.md), which already drives real functional Gaia with a small observer "bridge".

Paths below are relative to the archive root. "Gaia.fs" means `Nu/Nu.Gaia/Gaia.fs`.

## 2. Source-verification note

Terms used here:
- **Functional mode:** each world change makes a new immutable world state, so old states can be kept for undo.
- **Imperative mode:** the world changes in place; Gaia turns undo off.
- **K:** the last editor snapshot (the head of Gaia's `Pasts` list).
- **G:** the last good state before the fault.
- **F:** the state when the exception is caught.

The decisive claims, each marked **verified**, **wrong** or **unresolved**:

| # | Claim | Source (file:line at `064f7ae`) | Verdict |
| --- | --- | --- | --- |
| 1 | Breakout's gameplay screen turns its engine `UpdateEvent` into its own `Update` message, and that message runs `Gameplay.update`. | `Projects/Breakout Mmcc/Gameplay.fs:206`, `:210`, `:221-222` | verified |
| 2 | The engine calls a screen's update, and publishes `UpdateEvent`, only while the world is advancing and that screen is selected. So the fault cannot fire while Gaia is halted. | `Nu/Nu/World/WorldModule2.fs:1492`; `Nu/Nu/World/WorldScreen.fs:142-150` | verified |
| 3 | No layer between that event and the main loop catches the exception: event publishing (`WorldModule.fs:681` onward and `EventGraph/EventGraph.fs:243-247`), the subscription handler (`WorldContent.fs:25-28`, `:61-63`), the signal router (`World.fs:55-56`), the screen dispatcher's typed signal path (`WorldModule2.fs:2876-2879`, `:2816-2820`) and `Signal.processSignal` (`WorldTypes.fs:2465-2483`). The update step's only `try` is a `try … finally` that clears caches and lets the exception through (`WorldModule2.fs:1468-1519`). | as listed | verified |
| 4 | The exception therefore leaves `World.runWithoutCleanUp` (`WorldModule2.fs:1968-2152`). | `WorldModule2.fs:2005-2008` | verified |
| 5 | Gaia runs the whole loop inside `runWithCleanUpAndErrorProtection`, whose `with exn` catches anything that escapes. | Gaia.fs:4517-4537 | verified |
| 6 | Recovery calls `tryUndo`, which works only in functional mode and only when `Pasts` is not empty. | Gaia.fs:617-640 (test at :618-619) | verified |
| 7 | **Gaia's default is functional mode.** Imperative mode is an opt-in checkbox: "Use Imperative Execution (faster, but no Undo / Redo)". The standalone game's default is the opposite (imperative). | `Nu/Nu.Gaia/GaiaPrelude.fs:63-67`; Gaia.fs:77, :3854; standalone `Nu/Nu/World/WorldPrelude.fs:377` | verified |
| 8 | Gaia's ordinary Advance (F5 or the Advance button) takes a snapshot *before* it starts advancing. So any run started from the editor has at least one past state, K. | Gaia.fs:1394-1397, :1753, :505-508 | verified. Limit: advancing turned on by other code (game code, a test bridge calling `World.setAdvancing`) takes no snapshot. |
| 9 | The recovery target is K, not G or F. `tryUndo` switches to the head of `Pasts`, pushes F onto `Futures`, and then the handler clears `Futures`. There is no redo back to F. | Gaia.fs:620-626, :4523 | verified |
| 10 | The handler reads `wasAdvancing` *after* switching, so it describes K, not F. K from an Advance snapshot was taken while halted, so the expected log line is "Rewound to previous world." without "and halted". Runtime has not checked this. | Gaia.fs:1395-1397, :4524-4528; `Advancing` lives in the world state's `AmbientState` (`WorldTypes.fs:2044-2045`) | verified (source); the log text is a prediction |
| 11 | After recovery the editor keeps running: the handler logs the error, sets a modal "Message!" box and calls itself again with `firstFrame = false`. The box closes on Okay, Enter or Escape. | Gaia.fs:4531-4533, :4104-4114 | verified. Limit: the recursive call sits inside `try … with`, so it is not a tail call. Each recovery adds stack frames. Many repeated faults were not analysed. |
| 12 | With no past state (or in imperative mode), the handler logs "Could not rewind world" and returns exit code 1. The editor process ends; it does not re-enter. | Gaia.fs:4534-4537; `Nu/Nu/Core/Constants.fs:62`; `Nu/Nu.Gaia/Program.fs:18` | verified. This sharpens the 25 October note, which said only that re-entry "is not established". |
| 13 | `World.switch` rebuilds, rather than rewinds, several engine parts: it wipes memoized content, installs the old world state, switches the ambient state (which **copies** the state record, so the live state is no longer the same object as K), synchronizes viewports, rebuilds spatial trees, and clears and re-registers native physics from the restored state. | `WorldModule2.fs:993-1019`; `WorldModule.fs:386-388` | verified |
| 14 | Some things are **not** rewound: sound already queued or played, the random-number state (`Random.Shared`), and engine global flags outside the world state. The flag `UpdatingSimulants` is set before the update step and is only cleared after it, so it stays `true` until the next frame's update step ends. Gaia restores only its own selection and camera. | `Nu/Nu/Core/Gen.fs:63-64`; `WorldModule2.fs:2006-2008`; `WorldModule.fs:37`; Gaia.fs:627-639 | verified (source). How much these matter is unknown. |
| 15 | Gaia's selection fix-up after undo only changes the editor's own variables. It sends no engine selection event, so it does not trigger Breakout's `StartPlaying` (which would reset the model). | Gaia.fs:549-555, :628 | verified |
| 16 | "Soft Rewind" (in the exception dialog) is reached only by exceptions inside Gaia's own editor-UI `try` block. A game-update exception goes to the outer handler instead. The engine-side `World.imGuiProcess` runs outside that block. | Gaia.fs:4307-4399 (catch at :4399), :4402; `WorldModule2.fs:2111-2112` | verified |
| 17 | The dialog's "Hard Rewind" ignores `tryUndo`'s result. | Gaia.fs:4272-4274 | verified (as stated on 25 October) |
| 18 | **New:** an exception raised while setting a property in Gaia's property editor is swallowed silently. `Pasts` is restored and no dialog appears. A game-code fault reached that way reaches neither recovery route. | Gaia.fs:3134-3135, :3145-3146 | verified |
| 19 | **New:** if a screen receives a signal that is not of its current message type, the dispatcher retries by converting it. Any exception inside that retry is caught and logged as "Incompatible signal type". A game-code fault after a code reload that changed the message type could be hidden this way. | `WorldModule2.fs:2880-2889` | route verified. Whether ordinary reload reaches it is **unresolved**; the protocol below uses no reload. |
| 20 | The standalone game (no editor) runs through `World.run` → `runPlus` → `World.runWithCleanUp`. That logs the exception, cleans up and exits with code 1. There is no recovery. | `Projects/Breakout Mmcc/Program.fs`; `Nu/Nu/World/World.fs:489-493`, `:484`; `WorldModule2.fs:2155-2163` | verified |
| 21 | Breakout's random events (ball direction, brick colours) use unseeded `Random.Shared`. A fault tied to a collision would therefore fire at an unpredictable time. | `Gen.fs:63-64`; `Gameplay.fs` `Ball.initial`, `Brick.make` | verified |
| 22 | The maintainer tested this recovery feature with a deliberate fault in game code. Commit `a4a3de4` ("Fixed fix for #151", 11 Feb 2017) added `let _ = 1 / 0` right after bullet creation in `Projects/BlazeVector/BlazeDispatchers.fs`. One commit later, `c4f76ed`, removed it. | GitHub, read 3 November | verified |

Nothing I checked was **wrong** compared with the 25 October synthesis. Claims 12, 13, 18 and 19 add detail it did not have.

## 3. Eligibility decision

**Decision: eligible.**

**The fault, named F-DIV0-UPDATE.**
- **Where:** in `Projects/Breakout Mmcc/Gameplay.fs`, inside `GameplayDispatcher.Message`, case `Update`, before `Gameplay.update` is called. The game's own code; nothing in the engine or Gaia changes.
- **What:** add these two lines and nothing else:

  ```fsharp
  let rampCountdown = 30L - gameplay.GameplayTime // DELIBERATE TEST FAULT (research)
  let _ = 100L / rampCountdown
  ```

  On the update where the gameplay clock reads 30, this throws `System.DivideByZeroException`. That is the 31st advancing update after the clock starts at 0. Updates before and after it do not throw.

**Why this is a fair, ordinary game-code error:**
- **Location:** it is in the game's own message handler, where everyday game bugs live. It is not in the engine, Gaia or a test harness.
- **Kind:** an unhandled .NET arithmetic exception, the kind an unguarded divisor produces in normal development. Nothing in it targets recovery internals: it does not throw during the state switch, corrupt the world before throwing, or touch Gaia.
- **Precedent:** it copies the maintainer's own test of this feature (claim 22): a division by zero in game code, fired by ordinary gameplay.
- **Ordinary editor setup:** Gaia's default functional mode, started with Gaia's own Advance. No special settings are needed (claims 7 and 8).
- **Repeatable timing:** it depends on the gameplay clock, not on random collisions (claim 21) or on input. Input to Gaia is not established here, and R03 native-001, the earlier Gaia gesture attempt, is final.
- **Honest label:** it is a *deliberate test fault*, not a bug found in the wild. It tells us whether recovery is reached and what it gives back. It says nothing about how often such faults happen.

**The route to recovery (claims 1 to 9):**
1. Gaia Advance takes snapshot K.
2. The engine update publishes `UpdateEvent`.
3. Breakout's `Update` message runs and throws.
4. The exception passes uncaught through the event, signal and update layers.
5. It leaves `runWithoutCleanUp`.
6. Gaia's outer `with exn` catches it.
7. `tryUndo` switches to K, `Futures` is cleared, the error is logged, a message box is shown, and the loop re-enters.

**Faults considered and rejected:**
- **Tied to a collision:** fires at a random time (claim 21).
- **Tied to a key press:** needs input to Gaia, which is not established.
- **Raised through the property editor:** swallowed, so it never reaches recovery (claim 18).
- **Raised after a code reload:** may be hidden (claim 19).
- **Thrown inside Gaia, or during the switch itself:** not game code, and not fair to the recovery feature.

**What the source predicts recovery gives (to be tested in section 4, not claimed here):**
- **Restored:** K's world state, including the gameplay model and advancing = false. The memoized content, spatial trees and physics registration are rebuilt from it.
- **Lost:** all progress between K and the fault, with no redo.
- **Not rewound:** sound already played, the random-number state and global flags.
- **Not repaired:** the code. Advancing again from K reaches the same fault, and the next Advance snapshot gives recovery another K.

## 4. Protocol for the build/run step (for the Kimi K3 lane; not run by this session)

This protocol is fixed before any build or run. The build/run session commits its package and any amendment **before** each attempt. It appends results to this file, in a new section, without changing sections 1 to 4.

### 4.1 Question and comparison

**Question:** when F-DIV0-UPDATE fires in ordinary functional Gaia, is Gaia's outer recovery reached? Does it restore K and keep the editor usable? What is lost?

Arms. Each is a separate, fresh process:

| Arm | Setup | Role |
| --- | --- | --- |
| **A0 — no fault** | Unpatched Breakout, functional Gaia, the same steps as A1 | Negative control: no exception and no recovery message, so the fault patch, not the environment, causes A1's outcome |
| **A1 — recovery** | Fault-patched Breakout, functional Gaia (the default) | The main observation |
| **A2 — imperative** | Fault-patched Breakout, Gaia in imperative mode (the ordinary opt-in checkbox setting) | Contrast: the same fault with undo off. Predicted: "Could not rewind world", and Gaia exits with code 1. |
| **A3 — standalone (diagnostic)** | Fault-patched standalone Breakout, unchanged engine, reaching gameplay with one real click on Play (the 2 November input-check method) | Contrast with no editor. Predicted: the error is logged and the game exits with code 1. A3 does not gate A1. |

### 4.2 Fixed inputs and environment

- The Nu archive above (hash-checked before extraction), extracted to scratch outside the repo. The only source changes:
  - the two fault lines above (A1–A3), recorded as a diff with before/after SHA-256 of `Gameplay.fs`;
  - an observer bridge in Gaia, written fresh in the style of `experiments/nu-history-b0/prepare.py`.
- **What the bridge may do:**
  - call Gaia's own private `toggleAdvancing`, which is the ordinary F5 route;
  - expose **read-only** values: the `Pasts` count and the type and object identity of its head, the `Futures` count, and `MessageBoxOpt`;
  - add a post-ImGui hook, as B0 did.
- **What the bridge must not do:** change the body of `runWithCleanUpAndErrorProtection`, `tryUndo`, `World.switch` or any update logic. The bridge diff and its hash go in the receipt.
- **Environment:**
  - SDK 10.0.302 and a private copy of `.artifacts/nuget-packages/`;
  - Xvfb plus Mesa with the OpenGL 4.6 override, on the lane's own display number (`:94` or higher, not one in use);
  - `nice -n 10`;
  - static 60-update timing and Gameplay edit mode, as in R03 B0.
- **No** reload, no real input to Gaia, and nothing from the returned R02/R10/R12 drafts or R03 native-001.

### 4.3 Steps and observations (A0, A1, A2)

1. **Settle.** Start Gaia and wait for the Gameplay screen to be selected and `StartPlaying` to finish, halted. Record:
   - the full gameplay model, serialized, as S0;
   - the projected scene: entity names and the selected properties B0 used;
   - the `Pasts` count P0.
2. **Advance** through the bridge's `toggleAdvancing`. Require:
   - `Pasts` count = P0 + 1, with head type `Advance`;
   - the head's model equals S0 (this head is K).
3. **Run.** Each frame, at the post-ImGui hook, record the gameplay clock and the Update and TimeUpdate counts, keeping the last good model before the fault (G). Require the clock to rise by exactly 1 per advancing frame. If it skips 30, the attempt is **invalid** (trigger not reached), not adverse.
4. **First observation after the fault.** At the first hook call after the exception, record:
   - whether the process is alive and the hook fires;
   - halted or advancing;
   - the `Pasts` and `Futures` counts and `MessageBoxOpt` text;
   - the full model;
   - whether the live state is the same object as K (**predicted: no**, claim 13);
   - the log's error text and stack.
5. **Settled halted boundary.** At least 10 halted frames later, record the model and the projected scene again.
6. **Repeat.** Call `toggleAdvancing` again. Record the new snapshot K2, the second fault, and the same observations as steps 4 and 5.
7. **Exit.** Request `World.exit`. Record the process exit code.

The external deadline is 600 s per process; the caps are 600 Update events and 1,200 hook calls. If the fault has not fired by the cap, the attempt is invalid (trigger not reached).

**A3:**
- Use the 2 November keyboard-input harness method: one real click on Play.
- Then wait up to 600 s.
- Record the log and the exit code.

### 4.4 Pass and failure conditions

**A1 passes only if all of these hold:**
- (a) exactly one `DivideByZeroException` per pass, logged with a `Gameplay` frame in its stack;
- (b) the process survives, and the hook keeps firing after each fault;
- (c) the state right after recovery is halted, `Futures` = 0, `Pasts` = P0 after the first recovery, and `MessageBoxOpt` starts with "Unexpected exception!\nRewound to previous world.\nError due to:";
- (d) the full model equals S0, both right after recovery and at the settled halted boundary;
- (e) the projected scene equals S0's at the settled boundary;
- (f) the second pass gives the same results (with K2 in place of K);
- (g) exit code 0.

**Recorded, not pass/fail:**
- lost progress: G's gameplay clock minus K's;
- whether the "and halted" variant appears;
- the stale `UpdatingSimulants` flag, if it can be observed;
- sound and random-number limits, which are stated, not measured.

**Adverse results** are valid findings. They are recorded and not rerun:
- the exception escapes Gaia (process crash, or a non-zero exit without the "Rewound" log);
- recovery is reached but the model or scene does not equal K;
- the hook stops after recovery;
- `tryUndo` itself throws;
- the second pass behaves differently.

**Controls:**
- A0 passes if there is no exception, no message box and `Pasts` = P0 + 1 through 60 advancing updates.
- A2 passes if the log says "Could not rewind world" and the exit code is 1.
- If a control fails, A1 cannot be interpreted.

**Stop rule:**
- Five unresolved failures at one unchanged step means stop that step and report it.
- Fixes to the environment alone (display, library path, SDK) are allowed. Each one counts as a separate, logged attempt.
- Changing the fault, the bridge's observation logic or a pass condition needs a new written amendment committed first.
- Never rerun to get a nicer result.

### 4.5 What this cannot show

- How often such faults happen.
- Whether a person or agent finds recovery useful.
- Recovery of G or F.
- Native physics, contacts, sound or framebuffer equality (Breakout has no physics bodies).
- Repair: the code stays broken.
- Any benefit over saving and reloading the screen (branch B) or rebuilding from model files.
- Real input to Gaia.

Rendering is software (Mesa), so timings carry no meaning.

### 4.6 Where things go

- Package: `experiments/nu-daybreak-recovery-trigger/` (scripts, bridge installer, fault patch, receipts; added to the sparse-checkout patterns first).
- Raw evidence: `.artifacts/daybreak-recovery-trigger-YYYYMMDD/`.
- Results: appended here.
- Builds: in scratch, deleted afterwards and logged.
