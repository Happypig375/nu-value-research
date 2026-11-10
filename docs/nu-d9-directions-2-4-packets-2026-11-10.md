# D9 directions 2–4: protocol packets, fixed before any outcome (10 November 2026)

**Status:** protocol packets only. Nothing in this file has been built or run.
- Each packet fixes the question, conditions, attempt budget and scoring before any candidate or native outcome exists.
- A packet may be refined by a dated amendment before its first run, never after.
- Authority: user decision D9 (10 November 2026), `.orchestration/TASK-D9-20261110.txt`.
- Direction 1 (recovery) has its own [protocol and results](nu-d9-recovery-routes-2026-11-10.md).

**Shared rules for all three directions:**
- **Engine:** Nu master `47ef39e` (`.artifacts/vulkan-timing-20261103/nu-47ef39e.tar`, SHA-256 `3dcae8b0…faac`).
- **Renderer:** NVIDIA Vulkan on our own Xvfb (`scripts/linux_nu_vulkan_env.sh`), with the same run discipline as direction 1, including its idle-GPU rule (amendment 1).
- **Stopped work stays final:** the R10 schema-migration and R12 material-intent drafts are not opened, reused or relabelled. Their recorded failures stay theirs, and new attempts get new budgets.
- **Attempts:** every attempt is kept. Five unresolved failures at one unchanged step stops that step. An adverse or null result is a result.

## Direction 2: live editing with a schema change (R10 family)

**Question:** when a developer adds a field to a live game's model and reloads code in Gaia, which route gives the correct state with less loss?
- **L, live reload, no migration:** today's behaviour. On 16 October at `064f7ae`, live reload gave a new field 0 instead of its initializer 200.
- **M, live reload with an explicit migration function:** a user-written function from the old record to the new one, applied by the probe after reload.
- **R, restart and reconstruct:** save the model before the edit, start a fresh process with the new code, and set the model with the new field filled.

**Cases for the new field:**
- **A, absent:** the field must take its declared default, 200.
- **Z, zero:** the field must be 0 because the design says so.
- **N, nondefault:** the field must take a value computed from old state (75).

**Outcome (common):**
- the complete old fields are preserved;
- the new field equals the case's required value;
- the scene projection matches;
- one declared post-edit gameplay event (a brick hit) scores with the new field.

**Port and attempt budget:**
- Start from the tracked, completed `experiments/nu-r10-schema-reload/` package (initializer-only reload), ported to master like the R06 port.
- **Construction budget:** 5 failed builds or controls at one unchanged step, then stop and report. This is a new budget. The October migration attempts stay final and are not counted or continued.
- **Runs:** 1 unscored feasibility per route, then 3 scored runs per route × case: 3 routes × 3 cases × 3 = 27 processes.

**Measures:** correctness per route × case; declared steps; machine time for reload or restart (this server only).

**What it cannot show:** developer effort, or other schema changes (field removal, renames, union cases).

**Start condition:** direction 1 complete; a quota/time check passes for a port of about 1–2 hours.

## Direction 3: content revision versus ordinary prefab/material helpers (R12 family)

**Question:** for matched revision tasks on a real scene, does Nu's entity propagation deliver the required edits with fewer misses or less total work than an ordinary helper?
- The ordinary helper is a small, fair script that sets the shared material or tint on all instances and the per-instance overrides from an explicit list.
- The October [status-quo audit](nu-status-quo-and-transfer-audit-2026-10-23.md) found such helpers credible and common in other engines.

**Conditions:**
- **P:** Nu's `World.propagateEntityStructure` from an edited source entity.
- **O:** the ordinary helper, with the same intent information (which instances keep local overrides).

**Tasks** (Terra Firma scene, which on 3 November reproduced identically on Linux):
- **T1:** a shared tint change on all 32 palms.
- **T2:** a shared change on 31 palms, with one palm keeping its local tint (the October P-local case, where propagation missed the local palm).
- **T3:** a shared roughness change plus a local tint on one palm (the October B-local case).

**Outcome:**
- every required property on every instance;
- no unrequested change;
- the state persists after save and fresh reopen.

**Measures:** missed and extra edits; declared steps; machine time.

**Budget:**
- Construction: 5 failures at one unchanged step.
- Runs: 1 unscored feasibility, then 3 scored runs per condition × task, 18 pairs of save/reopen processes.

**Fairness rule:** the helper gets the same intent list that propagation needs. A baseline denied that information is invalid. A result where O matches or beats P is a valid and likely result.

**What it cannot show:** designer effort, collaboration, or engines other than Nu.

**Start condition:** after direction 2, or in parallel only if the single-experiment slot is free.

## Direction 4: coding agents with and without explicit case enumeration (R04/D1 + R08)

**Question:** when an AI coding agent must add a new case to a game's state type, does code that lists cases explicitly (so the compiler warns about the missing case) lead to fewer missed-behaviour bugs than equivalent code with catch-all branches?

**Conditions** (the same game, the same task, two source variants):
- **E, explicit:** the shipped Breakout code, where the gameplay update matches `| Playing | Quit -> gameplay`.
- **W, catch-all:** the same match sites rewritten with `| _ -> gameplay`. This is behaviourally identical before the task, and checked by the R04 compiler probe method.

**Candidate task** (one, fixed): *"Add a `Paused` gameplay state. Pressing P toggles pause during play. While paused, nothing moves and the message reads 'Paused'. Quitting while paused works as before."* The task text is identical in both conditions and does not mention warnings.

**Candidates:**
- Claude Opus subagents, using included quota only.
- Each starts with a fresh context containing only the task text and a private copy of the Breakout source in its condition. They have no access to this repository, other candidates' work, oracles or answers.
- One candidate runs at a time (the single experiment slot). Candidates may build, but they may not run the oracle.
- **Model family:** included Opus only. A fair comparison across model families would need families with no allocation; that packet is written here but **not substituted**. Results are labelled "one model family".

**Budget:** 6 candidates per condition (12 runs), in alternating order E W W E …; one attempt each; no reruns. Before each candidate, read quota and forecast. Stop and checkpoint if the next candidate cannot fit.

**Scoring** (fixed before any candidate output; applied after all candidates finish, by a scorer that never edits candidate code):
1. The candidate's code builds (SDK 10.0.403).
2. **A behavioural oracle on master,** run with Vulkan on the GPU and XTEST keys (the direction-1 and keyboard-timing harness methods):
   - (a) pause stops paddle and ball;
   - (b) the message reads "Paused";
   - (c) resume continues from the same state;
   - (d) Quit while paused returns to the title;
   - (e) no change to normal play (paddle moves, ball moves).
3. **Missed-case count:** match sites where `Paused` falls into wrong behaviour, read from the diff by a fixed checklist written before any candidate runs.
4. Whether the compiler warned in condition E, and whether the candidate acted on it (from its build log).

**Outcomes:** the pass count per condition, and missed-case counts. Descriptive only; 6 per condition cannot establish an effect size.

**What it cannot show:** human developers, other model families, other tasks or larger codebases, and long-term maintenance.

**Start condition:**
- the oracle is built and validated on hand-written reference solutions (one correct, two with planted misses) before any candidate runs;
- a quota forecast for 12 candidate runs is recorded first.

## Direction 4: missed-case checklist (fixed 11 November 2026 HKT, before any candidate exists)

Taken from master's `Projects/Breakout Mmcc/Gameplay.fs` (`47ef39e`). A candidate's diff is scored against these sites:

| Site | Where | What a correct `Paused` change needs | Does the compiler warn? |
| --- | --- | --- | --- |
| S1 | `Gameplay.update`, `match gameplay.GameplayState with … \| Playing \| Quit -> gameplay` (lines 89–168) | Paused must not move the paddle or the ball | **E: yes** (incomplete match, FS0025). **W: no.** The catch-all already treats `Paused` as "no update", which is correct here |
| S2 | `Content`: `if gameplay.GameplayState = Playing then` (line 240) | The scene must stay visible while paused; otherwise the board **and the Quit button** disappear | No, in either condition (an equality test) |
| S3 | Input: a P key toggle (new message or command, plus `Definitions` or keyboard handling) | P toggles Playing ↔ Paused only during play | No |
| S4 | The message text entity | It reads "Paused" while paused, and its normal text otherwise | No |
| S5 | Quit while paused (the Quit button and the `StartQuitting` command) | It returns to the title as before | No; it depends on S2 |

**What this means for interpreting direction 4:**
- The explicit-enumeration warning covers S1 only, where the catch-all happens to be harmless.
- The likely missed case is S2, which neither condition flags.
- So **a null or reversed result is plausible.** The packet's outcome measure stays as declared: the behavioural oracle (a)–(e) plus the per-site missed-case count.

## Direction 2: amendment 1 (11 November 2026 HKT, before any direction-2 run)

- **Order of work:** before building all three routes, run **one unscored feasibility of route L, case A** (package `experiments/nu-d9-schema-reload/`). Its purpose is to check that Gaia master's code reload works on this server at all, and to observe the new field's value.
- **Procedure:**
  1. Functional Gaia, Gameplay edit mode. Advance 10 updates and halt.
  2. Apply the October R10 schema edit to the scratch tree's `Gameplay.fs`: add `BrickReward : int`, initialize it to 200 in `empty`, and use it in scoring.
  3. Call Gaia's own `tryReloadCode`.
  4. After 10 halted frames, read the live model by reflection.
- **Recorded:**
  - whether reload compiled and installed the project code, with the reload time;
  - whether the seven old fields are unchanged;
  - the value of `BrickReward` (required: 200).
- **No migration** is tried in this step. This is the first construction attempt under the direction-2 budget (5 failures at one unchanged step). The October R10 attempts are not counted.

## Direction 2: route L feasibility results, and amendment 2 (11 November 2026 HKT)

**Route L, case A feasibility** (`.artifacts/d9-schema-reload-20261110/`):
- **Attempt 01 failed.** Gaia master's code reload did not compile: "Unable to find the file '../../../../Nu.Dependencies/AssimpNet/…'".
  - **Cause (upstream, source-confirmed):** since Nu commit `d51f628d9a` (11 August 2026), the reload script hard-codes `../Nu.Dependencies/…` relative to the project folder. For the bundled samples under `Projects/`, that points to a folder that doesn't exist. At `064f7ae` the paths came from the project's HintPaths.
  - **So at master, code reload of the bundled sample games fails on a stock checkout.**
- **Attempt 02, environment-only fix:** a symlink `Projects/Nu.Dependencies` → `../Nu/Nu.Dependencies` in the scratch tree, with no source change. **Reload then compiled and installed in 5.9 s.**
  - The live model became `FSI_0005.Breakout.Gameplay`, and all seven old fields were preserved.
  - **`BrickReward` was 0, not the required 200.** This is the October `064f7ae` finding (the new field gets its type default, not its initializer), reproduced at master on Vulkan.

**Amendment 2** (before any route-M run):
- `Probe.fs` takes a route argument, L or M.
- **Route M**, after the same reload, builds a migrated record of the reloaded type by reflection, with `BrickReward` = 200 for case A. It sets the record through the reloaded code's own `Screen.SetGameplay` (in the F# Interactive assembly), settles for 10 halted frames, and then records the new field, the old fields and the scene's entity names.
- **One unscored feasibility run (M-A).** The environment fix stays in place.
- Builds: build 02 accidentally compiled Breakout from the edited source left by attempt 02. It was not used for any run. The source was restored and rebuilt as build 03 (logged).

## Direction 2: route M feasibility result, and amendment 3 (11 November 2026 HKT)

- **Route M, case A feasibility (M-A-feasibility-01): passed.**
  - After the reload (6.9 s), the migration through the reloaded code's own setter took 1.6 ms.
  - `BrickReward` became 200, the old fields were preserved, and the scene's entity names were unchanged.
- **Amendment 3 (route R, before any route-R run):** two processes.
  - **R1**, the old code (`src2`): advance 10 updates, halt, save the model as a Prime symbol and its field values, exit.
  - **R2**, a fresh process built from the schema-edited source (`src3`, the same three edits applied before the build): convert the symbol into the new record type, record what `BrickReward` became after conversion, then set it to 200 explicitly. Settle for 10 halted frames and record the new field and the old fields.
  - **One unscored feasibility run (R-A).** Build 04 (old and new) passed.

## Direction 2: route R feasibility result, and amendment 4 — the scored series (11 November 2026 HKT, before any scored run)

**Route R, case A feasibility: passed.**
- The old fields were preserved and `BrickReward` was 200 after the explicit set. Both processes took 6.2 s and 11.6 s of wall time.
- **Observation:** converting the saved Prime symbol into the newly compiled type already gave `BrickReward` = 200 before the explicit set. Live reload's conversion gave 0 (route L). Two of Nu's conversion paths disagree about a new field.

**Amendment 4, the declared scored series** (package `experiments/nu-d9-schema-reload/`: `series.py`, `check.py`; probe build 06):
- **Seed (replaces "advance 10 updates"):** the fixed B0 model (`experiments/nu-history-b1/checkpoint/gameplay.symbol`, time 149, score 100, 29 bricks), with the ball placed under the existing bottom-row brick nearest x = −64, at y = 52, moving straight up. The next update must hit that brick.
- **Cases and required values:** A (absent: declared default 200), Z (deliberate zero: 0), N (nondefault: 75). The code edit is the same in all cases (initializer 200). Only the requirement changes, and M and R set the required value.
- **Common outcome (pass only if all three hold):**
  1. the old fields are preserved;
  2. the new field equals the required value;
  3. after one update, the seeded brick is gone and the score is 100 + the required value.
- **Order:**
  - unscored feasibility round F4 (L-A, M-A, R-A);
  - then 3 scored repeats, each with all 9 route × case runs, routes rotating (L M R, M R L, R L M) and cases A Z N within each route: **27 scored runs** (R uses two processes).
- **Discipline:**
  - Before each L/M run, `Gameplay.fs` is restored from the pinned tar; the probe then applies the edit itself.
  - The environment symlink from attempt 02 stays.
  - The idle-GPU rule is direction 1's amendment 1. 300 s deadline per process.
  - Adverse outcomes do not stop the series; infrastructure failures do.
- **Construction record:** build 05 failed to compile (a missing helper and an out-of-order reference); build 06 passed. That is 1 failed build at this step, within the budget of 5.
- **Limits:** this measures correctness per route and case, not developer effort. The October R10 attempts stay final and separate.
