# R-series results so far, and which practical comparison to serve next (3 November 2026)

**Conclusion.**
- **What the experiments show:** Nu's distinctive mechanisms mostly work as their source code says. Gaia's undo history, its built-in crash recovery, screen save/load (after a one-line fix) and save/reopen of a large scene all restore the declared state exactly.
- **But no experiment yet shows a practical benefit over an ordinary workflow,** and several show limits:
  - a schema change through live reload loses the new field's value;
  - one local content revision is missed;
  - stock screen import is broken at the pinned revision.
- **My recommendation for the next R-series experiments: serve one decision, "after a game-code fault in the editor, what is the cheapest reliable way back to work: Gaia's history, or a saved checkpoint file?"** It builds directly on finished work and needs no paid runs or participants. Its result would tell Nu users and the Gaia maintainer whether to rely on functional-mode history or on checkpoint files.

**Terms used here:**
- **Nu:** an F# game engine.
- **Gaia:** Nu's editor.
- **MMCC Breakout:** a small sample game used as the test application.
- **Functional mode:** the world is kept as immutable states, so old states can be kept for undo.
- **Imperative mode:** the world changes in place; Gaia's undo is off.
- **Pinned revision:** Nu commit `064f7ae` (July 2026), used by every experiment so far.
- **Data-only result:** judged from program state, traces or saved files, not from timings.
- **"Rn":** one of the 21 numbered research directions in the [agenda](nu-research-agenda-2026-10-08.md).

## 1. What each finished package found

**How strong the evidence is, overall:**
- Almost every experiment is a **single, instrumented feasibility witness**: one run per arm, with an added observer, on an authored task in one sample game. Each shows that a mechanism can do something under declared conditions. None estimates how often, how much, or for whom.
- **Every data-only result reproduced on this Linux server** (2–3 November), and several were byte-identical to Windows. So the results are robust to the machine and the platform, not just one-off runs.
- **Timing results are provisional:** the Windows/Home machine was memory-constrained. They are being re-run on this server as the new reference (see "Timing" below).

| Package | What it found | Strength | What it does NOT show |
| --- | --- | --- | --- |
| **R01** moving platform (Box2D.NET physics, Nu's settings mirrored) | Ordinary friction keeps a rider on a moving platform, but the rider lags outside the authored tolerance. | One fixture; byte-identical across platforms. | Nu application behaviour, any benefit. |
| **R02** standalone lifecycle (both Breakout versions) | Both games go title → play → quit → exit with the predicted lifecycle events. The ImSim version takes 95 callbacks, not the predicted 96, inside the allowed bound. | One pass each; identical counts on Linux. | Input or pause behaviour (the R02 input construction was stopped after five failures). |
| **Keyboard / key-release checks** (new work, Linux) | Real X keyboard and mouse input reaches the unchanged game. The paddle stops 2 updates after a key is released. | One run each, judged from screenshots only. The Vulkan reference re-run (10 repeats, 60 trials): about 60 updates/s, movement within about 71 ms, stop within about 59 ms, 3-update overshoot. | Real hardware, Gaia input, agent access. |
| **R03 B0/B1** history in Gaia | Gaia's undo restores a represented checkpoint exactly, and both negative controls were rejected (B0). A fresh reconstruction continues 20 steps identically (B1). | One witness each; the B1 steps are bit-identical across platforms. | Resuming the old native world; ordinary editor access (the one ordinary-access attempt, R03 native-001, failed and is final); debugging benefit. |
| **R04** case enumeration (D1) and pause/lifecycle | Listing cases explicitly makes the compiler warn about an added case, where a catch-all stays silent. The warning is one among 210 existing ones. Four pause/exit references pass, and five planted faults are caught at their predicted points. | Compile-level contrast; one runtime series; reproduced. | Whether developers or agents notice the warning; any maintenance benefit. |
| **R05** events (stub world) | Event delivery order, stop-propagation and unsubscribe behave as the source says. | Small stub-world probe. | Behaviour in a real application. |
| **R06** recovery cost | Taking a history snapshot is faster than serializing the model. Applying undo is slower than restoring from the serialized model (6/6 pairs on Windows, 5/6 on Linux with one tie). Time until ready again goes both ways. | 6 pairs; **timings provisional**. **The reference re-run on Vulkan-era Nu (20 pairs, 3 Nov) found history faster in all three components** (20/20, 19/20, 16/20): a new result on a different engine and configuration ([record](nu-vulkan-timing-reference-2026-11-03.md)). | Total repair work; memory policy; the two routes keep different amounts of state. |
| **R10** live code reload | An unchanged-schema game state survives a code reload. When a field is **added** (with initializer 200), live reload gives it 0, so the intended mapping fails. A fresh start gives 200. Prime's converter has defaulting and positional hazards. | One witness each; identical on Linux. | A working migration (that construction was stopped after five failures); benefit. |
| **R12** content propagation and scene save/reopen | A large 3D scene (Terra Firma, 197 entities, 166 links) keeps everything across save and fresh reopen. Shared revisions reach all 32 palms, **one local revision misses its palm**, and a batch/local edit succeeds. Propagation creates 160 pairs, not the predicted 163. | Four revision/reopen pairs plus the reopen prerequisite; the reopen is identical on Linux (software and GPU). | Authoring effort, collaboration, or an advantage over ordinary prefab/material workflows (an audit found Unity, Unreal and Godot already do selective inheritance). The material-intent construction was stopped after five failures. |
| **Daybreak B:** screen save/reload | Saving a running screen through Nu's ordinary serializer keeps the complete gameplay model. **Stock import is broken at `064f7ae`** (wrong internal address). With a one-line fix, now upstream, import reproduces the B0 model and scene in a fresh process. Importing without first clearing leaves one stale entity. | One run per arm; engine fix applied by us. | Native or physics state, audio, editor workflow, benefit. |
| **Daybreak A:** crash recovery | A deliberate division by zero in the game's own code is caught by Gaia. Gaia rewinds exactly to the last Advance snapshot and keeps the editor running through a repeated fault. Progress since the snapshot is lost. With undo off, Gaia exits. | One run per arm, with controls; identical on the GPU. | Sound or random-number rewinding, repair, real faults' frequency, benefit. |

- **Desk-only directions** (contracts and literature, no experiments): R07 learning, R08 coding agents, R09 change sequences, R11 collaboration, R13 interaction guarantees, R14 practice and adoption, R20 designer roles and R21 human steering. R15–R19 stay deferred.
- **Timing:** the October timings are provisional. **New reference re-runs on Vulkan-era Nu (master `47ef39e`, NVIDIA GPU)** for R06 and the keyboard checks are done ([record](nu-vulkan-timing-reference-2026-11-03.md)). They are the reference timings.

## 2. Practical comparisons the next experiments could serve

Each option names who would use the answer, what it would change, the experiments it needs, and its cost and risk. "Cheap" means server time only, with no paid model calls and no participants.

### Option 1: getting back to work after a game-code fault in the editor (R03 + R06 + Daybreak A/B)

- **Who and what changes:** Nu users and the Gaia maintainer.
  - If history recovery is as reliable as a checkpoint file and costs less, users keep functional mode on while editing.
  - If checkpoint files are needed anyway (for example to survive a crash without a usable snapshot, or to recover a later state), Gaia could add automatic screen checkpoints.
- **Experiments:**
  - port Daybreak A (crash recovery) and B (screen save/load, which works stock on master) to Vulkan-era master;
  - define one common outcome: the required gameplay model and scene, plus a declared continuation;
  - compare three routes on the same authored faults: (a) Gaia's automatic rewind or undo, (b) F7 restore point, (c) a screen checkpoint file plus fresh restart;
  - measure what each preserves and loses, plus machine time and steps, using the R06 timers, on this server as the reference.
- **Cost:** low to moderate, about one to two sessions; all the pieces exist.
- **Risk:**
  - authored faults, not observed ones;
  - one sample game;
  - "steps" is not human effort, and human or agent effort would need allocations not yet made;
  - ordinary F7 may simply win, which is a valid answer.

### Option 2: live editing with a schema change (R10)

- **Who and what changes:** developers iterating on game state. Should Nu offer explicit migration on reload, or is restart-and-rebuild cheaper and safer?
- **Experiments:** an explicit migration on reload, compared with restart plus model-file reconstruction, for absent, zero and nondefault new fields.
- **Cost:** high. The October construction failed more than five times and is stopped; resuming it needs your explicit decision, or a fresh port to master.
- **Risk:** high construction risk. The current finding (the new field gets 0) may already be enough to decide.

### Option 3: content revision and reuse (R12)

- **Who and what changes:** designers. Is Nu's entity propagation better than an ordinary prefab or material helper?
- **Experiments:** a matched revision task with an ordinary helper as the baseline (the audit found it credible), counting total work and missed edits.
- **Cost:** high. It needs a fair helper baseline, and the material-intent construction is stopped.
- **Risk:** the ordinary-workflow audit suggests no Nu advantage is likely. The useful answer may be a negative one.

### Option 4: coding agents maintaining stateful game code (R04/D1 + R08)

- **Who and what changes:** people using AI agents on Nu projects. Does explicit case enumeration (the compiler warning) help agents avoid missed-case bugs? It overlaps with nu-gaia-agentic.
- **Experiments:** agent runs on matched change tasks with and without enumeration, scored on behaviour.
- **Cost:** needs candidate model runs, which have **no allocation** (paid or quota). The scoring oracle (R04) exists.
- **Risk:** agent variability and convergence, and the warning is buried among 210 others. It needs your allocation decision first.

## 3. Recommendation

*(Update, 11 November 2026: the user approved all four options (decision D9, 10 November). Option 1 is done: history, F7 and checkpoint-file recovery all reach the common outcome (15/15 scored runs). History loses everything since Advance (30 updates here), but is ready in about 46 ms. F7 or a screen file loses only the 10 updates since the checkpoint. F7 is ready in about 46 ms; the file route needs a crash and a fresh editor, about 5.7 s. At Gaia master, F7 during play halts the game. [Record](nu-d9-recovery-routes-2026-11-10.md).)*

**Choose option 1** (recovery after a fault), on Vulkan-era master, with this server as the reference machine. Why:
- It turns three finished pieces (history recovery, crash recovery, screen save/load) into **one practical comparison with a common outcome**. That is the step the project's rules say is missing before any benefit claim.
- It is cheap: server time only, with no paid runs, participants or stopped gates to reopen. Stock import works on master, so no engine patch is needed.
- Every outcome is informative. "F7 or a checkpoint file is as good" is a real answer for users, as is "history loses work the file keeps", or the opposite.

Options 2 and 3 need reopening stopped constructions and face likely negative answers. Option 4 needs a paid allocation. They can follow if option 1 shows a gap worth pursuing.

**What option 1 would still not show:** human or agent effort, real-world fault frequency, other games or engines, and native or audio state.
