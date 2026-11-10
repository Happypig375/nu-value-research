# Getting back to work after a game-code fault in the editor: three routes compared (D9 direction 1, 10 November 2026)

**Status: protocol fixed before any run.** The package is committed with this file. Results go in a later section, without changing sections 1–5.

## 1. Question and who uses the answer

**Question:** after a game-code exception while the game runs in Gaia (Nu's editor), which ordinary route gets the user back to a working, correct session?
- **H, history:** Gaia's automatic rewind to the snapshot taken at Advance.
- **F, restore point:** the user pressed F7 (restore point) during play; Gaia's automatic rewind then targets that point.
- **C, checkpoint file:** the user saved the gameplay screen to a file during play, in imperative mode (faster, no undo), where the fault ends the editor. A fresh editor process then loads the file.

The comparison is how much progress survives, whether the result is correct, how many declared steps each route needs, and how much machine time each takes.

**Who uses the answer:** Nu users and the Gaia maintainer. It tells them whether to keep functional mode (history) on while editing, whether F7 is worth pressing, and whether screen checkpoint files are a credible alternative or addition. User decision D9 (10 November 2026) approves this direction.

## 2. Fixed setup (all routes)

- **Nu and application:**
  - Nu master `47ef39e` (pinned tar `.artifacts/vulkan-timing-20261103/nu-47ef39e.tar`, SHA-256 `3dcae8b0…faac`; the commit is checked from the tar header).
  - MMCC Breakout, Gaia in Gameplay edit mode, the static 60-update clock.
  - SDK 10.0.403, Release.
- **Renderer:** NVIDIA RTX 4090 D with Vulkan on our own Xvfb (`scripts/linux_nu_vulkan_env.sh`; `nice -n 10`). There is an idle-GPU check before each process, and load, memory and GPU samples are recorded. Every process must log "Selected Vulkan Device NVIDIA GeForce RTX 4090 D".
- **The fault (authored, the same in every route):** the branch A test fault, ported to master. Two lines in Breakout's `Update` handler divide by `30 − gameplay clock`, so `DivideByZeroException` fires on the update where the clock reads 30 ([branch A record](nu-daybreak-recovery-trigger-2026-11-03.md)).
- **The only Gaia change:** a read-only observer bridge. It adds Gaia's own Advance (F5) and restore-point (F7) functions plus read-only accessors. `prepare.py` prints the before/after hashes: Gaia `8e26778f…` → `cf418d65…`, `Gameplay.fs` `09e48445…` → `c2ce60b3…`.
- **Checkpoint moment:** routes F and C take their checkpoint at the observer hook where the clock reads 20, so their recovery point is clock 20. Route H's recovery point is the Advance snapshot at clock 0.
- **The checkpoint-file route uses the public API.** Master's Gaia has no menu command to save or load a screen. The probe therefore calls `World.writeScreenToFile` and, in the fresh process, the branch B procedure: destroy the screen's groups, `World.readScreenFromFile`, then `World.notifyScreenModelChange`. In ordinary use this would be an F# evaluation in Gaia's Interactive window, and it is counted as a declared step.

## 3. Procedure per route

- **H:**
  1. Settle at clock 0.
  2. Advance (Gaia's F5 function), which takes the snapshot K.
  3. The fault fires at clock 30, and Gaia's outer handler rewinds to K.
  4. Settle for 10 halted frames.
  5. Advance again, and halt after 5 updates.
- **F:** the same as H, except that F7 is called at clock 20, so the rewind targets the restore point.
- **C1 (session):**
  1. Gaia in imperative mode (its ordinary checkbox option). Settle at clock 0, then Advance.
  2. At clock 20, write the screen file, and also save the model, the scene projection and the per-clock model trace to the transfer folder as references.
  3. The fault at clock 30 ends Gaia: "Could not rewind world", exit code 1.
- **C2 (restart):**
  1. A fresh imperative Gaia process.
  2. At the first settled hook, import the file.
  3. Settle for 10 halted frames.
  4. Advance, and halt after 5 updates.

## 4. Common outcome, measures and pass conditions

**Common outcome (every route must reach it to pass):**
- **(a) Recovery:** H/F: the fault is caught and rewound, with the message "Unexpected exception! Rewound to previous world. Error due to: Attempted to divide by zero.", halted, with no redo entries. C: the session ended by the fault, the file was written, and the fresh process imported it.
- **(b) Correct state:** the complete gameplay model and the scene projection (B0 serializers, exact float bits) equal the route's recovery point, both at the first hook after recovery and after 10 halted frames.
- **(c) Continuation:** after 5 more updates, the model equals the original run's recorded model at the same clock. Ball motion is deterministic until the first ball loss, which cannot happen before clock 30.
- **(d) Clean exit:** H/F exit code 0; C2 exit code 0.

**Measures:**

| Measure | How |
| --- | --- |
| Progress lost | 30 − the clock of the recovered state |
| Declared steps to get back | Fixed by design: H 1 (Advance) + 1 (dismiss message); F 1 + 1 (F7) + 1; C 1 + 1 (save file) + 1 (restart editor) + 1 (load file through Interactive) |
| Checkpoint time | ms of the F7 call or the file write |
| Fault to ready | H/F: last hook before the fault → first hook after recovery (an upper bound that includes the faulting frame). C: C1's last hook → C2's first hook after import (wall clock, including process restart) |
| Import time | C only: ms of destroy + read + notify |

Times are valid only on this server and configuration. They must not be compared with Home timings.

**Pass:** (a)–(d) all hold for the run. A route that fails is an **adverse result**: it is recorded and not rerun.

## 5. Attempts, stop rule and limits

- **Feasibility round Z:** one each of H, F and C, unscored. A failure allows a documented correction under a dated amendment, committed before scored runs.
- **Scored rounds 1–5,** in rotating order: H F C, F C H, C H F, H F C, F C H. That is 5 runs per route.
- **Stop rule:**
  - Adverse outcomes do not stop the series.
  - Infrastructure failures do: a timeout (300 s), a launch exception, or a missing Vulkan device line.
  - Five unresolved failures at one unchanged step means stop that step.
  - Every attempt is kept.
- **Limits:**
  - Authored faults at a fixed clock, in one game.
  - Declared steps are not human effort, and nothing here measures human or agent work.
  - The checkpoint route depends on an API call with no menu command.
  - Sound and random-number state are not compared.
  - No real-world fault frequency, no other game or engine, and no benefit claim beyond what survives and the machine time.

## Amendment 1 (10 November 2026, before any run)

- **Problem:** the first launch of round Z never started a process. A labmate's long-running service (`buildinggpt-rag`, resident on the GPU for nearly 3 days, 4.6 GB, 0 % utilization) means "no process on the GPU except Xorg" can never hold, so the idle check would only time out.
- **Change** (`series.py` only): **idle means GPU utilization < 10 % on two polls 2 s apart.** The processes present are recorded with each attempt. Nothing else changes, and no Nu process ran before this amendment.
