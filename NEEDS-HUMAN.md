# Questions for the user / orchestrator — nu-value-research

Newest first. Each item lists the options, my recommendation and what it blocks. Background is in [STATUS.md](STATUS.md) (section dated 1 November 2026).

## 2026-11-10 — item 11 ANSWERED (user decision D9, 10 November): all four directions approved — Claude Opus

- **Decision:** all four practical comparisons are approved, with included Claude/Opus quota allowed for direction 4 (coding agents). Scope and limits: `.orchestration/TASK-D9-20261110.txt`.
- **Order of work:** recovery first, as the shortest path to a useful result; then the others as far as they are unblocked.
- **Reports:** `.orchestration/d9-all-directions-20261110/`.
- **Done, 11 Nov 03:47:57 HKT (commit `1ed602b`):** all four directions have scored results (directions 3 and 4 ran in the second allocation). Integrated results: [R-series report, section 4](docs/nu-r-series-results-and-next-comparisons-2026-11-03.md).
  - **No decision is needed to finish D9.**
  - Optional choices for later, each a new experiment with its own budget: direction 4 with a harder task; direction 3 with a per-field-merge prototype; whether to report the two Nu master defects (F7 halts play; code reload of the bundled samples breaks on a stock checkout) upstream. I recommend the upstream reports first: small, factual and reproducible. Nothing waits on these.
- **Checkpoint, 11 Nov ~00:40 HKT:** directions 1 and 2 are done. Direction 2: live reload alone gives a new field 0, correct in 3/9 runs; explicit migration and restart are correct in 9/9 each.
  - Directions 3 and 4 have frozen packets. **They need a fresh time/quota allocation** (roughly 2 h for direction 4, 2–3 h for direction 3; weekly use is now 90 %).
  - No other decision is needed.
- **Progress, 11 Nov ~00:15 HKT:** direction 1 is done (history, F7 and checkpoint-file recovery all reach the common outcome (15/15 scored runs). History loses everything since Advance (30 updates here), but is ready in about 46 ms. F7 or a screen file loses only the 10 updates since the checkpoint. F7 is ready in about 46 ms; the file route needs a crash and a fresh editor, about 5.7 s. At Gaia master, F7 during play halts the game. [Record](docs/nu-d9-recovery-routes-2026-11-10.md).) Directions 2–4 have frozen protocol packets. No decision is needed.

## 2026-11-03 ~21:00 HKT — item 11: which practical comparison should the next R-series experiments serve? — Claude Opus (answered above)

- **The user asked for results first, with recommendations.** The report is ready: [docs/nu-r-series-results-and-next-comparisons-2026-11-03.md](docs/nu-r-series-results-and-next-comparisons-2026-11-03.md).
- **Short version:** the mechanisms work as their source says, but there is no demonstrated practical benefit yet, and there are several limits. The four candidate comparisons:
  1. **Getting back to work after a game-code fault in the editor:** Gaia history vs F7 vs a screen checkpoint file. Cheap, and builds on finished work.
  2. **Live editing with a schema change.** High cost; it reopens a stopped construction.
  3. **Content revision vs ordinary prefab helpers.** High cost; a negative answer is likely.
  4. **Coding agents with explicit case enumeration.** Needs a paid allocation.
- **Recommendation: option 1,** on Vulkan-era master with this server as the reference.
- **Blocks:** the choice of the next R-series experiment only. The D11 timing re-runs continue meanwhile.

## 2026-11-03 ~20:35 HKT — item 10 ANSWERED (user decision D11) — Claude Opus

- **Decision:** "a combination of a and b as discussed: timing measurements need rerunning, but data-only comparisons can be retained." The orchestrator's reading:
  - **Data-only results** stay as recorded at `064f7ae`, with no re-runs.
  - **The timing measurements** (R06 recovery cost, keyboard input check, key-release check) are re-run as **new, declared experiments ported to Vulkan-era Nu**: current master `47ef39e`, on the NVIDIA GPU with Vulkan, on our own Xvfb, with no software rendering.
  - **This server is the reference machine.** Home timings stay recorded, marked provisional.
- **DONE, 3 Nov ~21:10 HKT:** both timing re-runs ran and are the reference timings ([record](docs/nu-vulkan-timing-reference-2026-11-03.md)).
  - R06: the history route was faster in 20/20, 19/20 and 16/20 pairs.
  - Keyboard: about 60 updates/s, movement within about 71 ms, stop within about 59 ms, 3-update overshoot.
  - One amendment (restart the board on game over) was committed before any scored keyboard repeat.
- **Done before the runs:**
  - The NVIDIA Vulkan + Xvfb route works here with master: Nu logs "Selected Vulkan Device NVIDIA GeForce RTX 4090 D", and the window shows the image.
  - Wrapper: `scripts/linux_nu_vulkan_env.sh`.
  - The ports and protocols follow; see STATUS.

## 2026-11-03 ~20:00 HKT — item 10: "All Nu runs on Vulkan" vs the OpenGL-only pinned revision — Claude Opus (answered above)

### 10. The research's pinned Nu has no Vulkan renderer. Re-pin, or keep it as an exception?
- **Facts** (source reading and GitHub API only; nothing run; details in `docs/nu-gpu-headless-recipe-2026-11-03.md`, "Vulkan and the pinned revision"):
  - Every retained package that runs Nu pins Nu `064f7ae` (23 July 2026), and that revision is **OpenGL-only**. It has no Vulkan code and no renderer switch.
  - Current Nu master is **Vulkan-only**. The two lines diverged: OpenGL was removed on a Vulkan branch that master merged after our pin. Master is 1,938 commits ahead.
  - So "on Vulkan" for these packages means **moving the research to a much newer Nu**, not flipping a setting.
- **What a move would change:**
  - Every probe, bridge and protocol needs porting, and every result becomes a new observation, not a reproduction of the October Windows and 2–3 November Linux records.
  - The engine changes matter more than the renderer. Example: stock screen import works on master (upstream `7d6389bea`) but not at `064f7ae`.
  - Data-only results (model values, properties, traces, saved files) would not depend on the renderer itself. Screenshot- and timing-based ones would (keyboard/key-release checks, R06 timings, wall-clock times).
- **Options:**
  - **(a)** Keep the pinned `064f7ae` packages on OpenGL, their only renderer, as a declared exception to the Vulkan rule. Use the NVIDIA GPU via VirtualGL for data-only runs, and Mesa software rendering for screenshot checks. **All new Nu work** uses a Vulkan-era revision on NVIDIA Vulkan, once nu-gaia-agentic confirms the Vulkan + Xvfb route.
  - **(b)** Re-pin the research to a Vulkan-era revision (for example current master), port the packages and re-run them as new, declared experiments. Large: about 20 packages, each with its own protocol. The October records stay as the `064f7ae` evidence.
  - **(c)** Stop running the pinned packages at all, and use only new Vulkan-era work from now on.
- **Recommendation: (a).** The pinned packages exist to reproduce recorded results, and they can only do that on the revision they pin. Re-pinning is a research-design choice, closer to starting new experiments, and fits better with the open R-series comparison choice.
- **Blocks:** only the question of which renderer re-runs of the pinned packages use. Nothing is running now.

#### 10, follow-up (user question, 3 Nov): what the packages are, and whether they need OpenGL-specific comparators

**Short answer: no package needs an OpenGL-specific comparator.**
- 15 of the 18 rows below judge only data (model values, entity properties, event traces, saved files, compiler output). Those comparators would work the same on Vulkan.
- 6 of those 15 never render at all: R01, the two R04 compiler/build probes, R05, R10 conversion, and R12 propagation.
- Only three rows are environment-specific:
  - **R06** reads milliseconds, which are already not comparable between Windows and Linux. They are only compared within one run.
  - **The two keyboard checks** read screenshots, so a Vulkan run would need re-tuned sample points under its own protocol, not a comparison against the OpenGL images.
- Moving to Vulkan matters because of the engine version (1,938 commits of changes), not because of the comparators.

| Package (all at Nu `064f7ae`) | What it measures | Its pass condition reads | Renderer-specific? | Recommendation |
| --- | --- | --- | --- | --- |
| R01 platform | Whether a moving platform carries a rider (Box2D.NET mirror of Nu's physics settings) | Physics traces | No; it runs neither Nu nor a renderer | Keep; the Vulkan rule doesn't apply |
| R02 standalone lifecycle | Both Breakout games go title → play → quit → exit with the expected lifecycle events | Event sequences and callback counts (game updates, not ms) | No | Keep on 064f7ae |
| R03 B0/B1 history | Gaia undo restores a checkpoint; a 20-step continuation matches | Model values and scene properties | No | Keep on 064f7ae |
| R04 compiler diagnostics | Compiler warning for explicit cases vs a catch-all | Compiler output only | No; nothing runs | Keep |
| R04 application diagnostics | The same warning inside the full Breakout build | Compiler output only | No; nothing runs | Keep |
| R04 pause/lifecycle runtime | Pause/quit behaviour of four references; five planted faults caught | Model and property traces per game update | No | Keep on 064f7ae |
| R05 events | Event delivery order in a stub world | Event traces | No; the stub world has no renderer | Keep |
| R06 recovery cost | Gaia snapshot/undo vs serialize/restore: correct state, plus component times | Timing (ms) plus state equality | **Timing is machine- and configuration-specific.** No OpenGL baseline is needed, but the Home timings are provisional (memory pressure). | Keep on 064f7ae. **Paired, repeated reference re-run of both arms on this server** (plan below). |
| R10 conversion | How Prime converts changed record types | Converted values | No; Prime only, no Nu run | Keep |
| R10 live reload | Game state survives a code reload | Model fields | No | Keep on 064f7ae |
| R10 schema reload | A new field after reload gets 0 instead of 200 | Model fields | No | Keep on 064f7ae |
| R12 propagation | Entity-template propagation in a stub world | Serialized entity values | No; no renderer | Keep |
| R12 Terra Firma reopen | A big 3D scene keeps its entities, links and histories across save and reopen | Entity properties and saved files | No; identical on Windows, Linux software and Linux GPU | Keep on 064f7ae |
| R12 Terra Firma revisions | Template revisions (palm tints and others) delivered and kept after reopen | Entity properties and histories | No | Keep (not re-run on Linux) |
| Branch A recovery fault | Gaia rewinds to the last snapshot after a game-code exception | Model and scene values, log text, exit codes | No | Keep. Port only if recovery on current Nu becomes a question. |
| Branch B screen save/reload | Screen export and import round-trip the gameplay model | Saved file, model values | No | Keep. **Porting is worth it as a new question:** stock import is broken at 064f7ae but fixed on current Nu (upstream `7d6389bea`). |
| Keyboard input check | Real X key and mouse input reaches the game | **Screenshots** (paddle and brick pixels) | **Yes.** Sample points were tuned on Mesa images, and they need software rendering (black window under VirtualGL). | Keep as the record. Its timing parts (release drift in seconds, about 2.5 updates/s) are valid only for that configuration. **Repeated reference re-run on this server** (plan below). Redo on Vulkan-era Nu with a re-tuned protocol only if input work needs it. |
| Key-release check | Release stops the paddle within 2 game updates | **Screenshots** (one distinct frame = one update) | **Yes**, as above, plus display-lag dependence | Same as the keyboard input check, including the **repeated reference re-run** |

The stopped drafts (R02 input, R10 schema migration, R12 material intent) are not runnable, and nothing here changes their status.

#### 10, follow-up 2 (user, 3 Nov): timing is machine-dependent; this server becomes the reference machine

**Rule:**
- Any timing result (milliseconds, wall-clock, frame pacing, deadlines met or missed) is valid only within one machine and one configuration.
- The October Home/Windows timings are **provisional and possibly distorted**: Home was memory-constrained. They are now marked so in PLAN and the package docs, with their values unchanged.
- **This server is the reference machine.** Data-only results can still be compared across machines.

**Timing-sensitive packages: paired or repeated reference re-runs on this server**

| Package | Timing result | Arms to re-run | Planned configuration |
| --- | --- | --- | --- |
| **R06 recovery cost** | ms to take a recovery point; ms to recover; request-to-ready | Both arms: Gaia snapshot/undo (history) and serialize/restore (reconstruction) | **20 pairs** (instead of 6), alternating order (H R R H …); one build; `nice -n 10`; one process at a time; before each process, check that the GPU is idle and record the load average and free memory |
| **Keyboard input check** | Release drift within 1 s; update rate | One arm (press, then release); repeats only | **10 repeats**; Mesa software rendering on Xvfb (screenshots need it); same nice level and checks |
| **Key-release check** | Press lag and release lag, in updates counted from screenshots | One arm; repeats only | **10 repeats**, same configuration as the keyboard check |
| GPU vs software speed (recipe doc; not a package) | Seconds per process | Optional: both configurations, alternating, 5 repeats each (A1 and R12 L0) | Only if a speed figure is ever cited; today's figures are single runs |

- **Timing recorded only as description, no re-run planned:** the R12 Terra Firma and revision wall times, branch A/B run times, and R03/R04/R10 process times. No result rests on them.
- **R02's callback counts** are game-update counts under a fixed 60-update clock, not wall-clock. They were identical on Windows and Linux, so they are treated as data.
- **Each re-run gets a dated protocol committed first,** and its results replace the provisional timings as the reference.
- **The configuration for R06 depends on this item:** at `064f7ae` it can only be OpenGL. My proposal is the NVIDIA GPU via VirtualGL (data-only, less CPU noise). The keyboard checks need Mesa software rendering either way.

**Data-only results that Home's memory pressure might have affected** (outcomes stand; listed so nobody reads more into them):
- **R03 B0:** the first two runs hit a 180 s deadline before the 600 s run passed. The B0 verdict reproduced on the server.
- **R06:** the reconstruction feasibility run timed out on Windows (unexplained) and **passed on the server**. This is the most likely memory-pressure case.
- **R12 Terra Firma reopen:** one expanded attempt was interrupted by a restart. The final pair reproduced on the server, identically.
- **R10 schema reload:** build 01 ended "interrupted, completion unknown". The final verdicts reproduced on the server.
- **R03 native-001 preparation:** one construction failure was an "SDK first-use timeout". R03 native-001 stays final; this is listed only as a possible memory effect.
- **Not memory:** R12 revision's B-local input-integrity failure was attributed to the A: storage problem. The stopped R02/R10/R12 drafts failed on compile, control and fixture errors.

**Updated recommendation for item 10: (a), plus the timing rule.**
- Keep the pinned packages on `064f7ae` with OpenGL.
- Make this server the reference machine.
- Run the three timing re-runs above under declared protocols.
- **All three wait on this item:** every run at `064f7ae` is an OpenGL run, so each needs the exception in option (a) to the "all Nu runs on Vulkan" rule. With (a), R06 would use OpenGL on the GPU via VirtualGL, and the keyboard checks Mesa software rendering.
- Run all new Nu work on Vulkan.

Server time is cheap. In total: about 40 R06 processes and 20 short keyboard runs.

## 2026-11-03 ~18:45 HKT — branch A finished — Claude Opus

- **No decision needed.** The orchestrator reassigned the branch A build/run step from Kimi K3 to me, and it is done. All three arms passed at the first attempt:
  - Gaia recovers from a deliberate game-code exception by restoring the Advance snapshot exactly;
  - it loses the progress since that snapshot, and the fault repeats;
  - with undo off, Gaia exits.
- Record: `docs/nu-daybreak-recovery-trigger-2026-11-03.md` section 6 (`727eaed`).
- **Both Daybreak-only branches are now complete.** Nothing is left for the Kimi lane from this workspace.

## 2026-11-03 — user decisions D9 applied (items 8 and K1) — Claude Opus

- **K1: ANSWERED (option b), steps 1–2 DONE.**
  - The private draft is still not on the server, so I verified the branch A sources myself from the pinned Nu archive (hash checked).
  - **Decision: eligible.** A deliberate division by zero in Breakout's own `Update` handler reaches Gaia's outer recovery in Gaia's default functional mode. All 22 decisive source claims are verified, except one side route (a fault after a code reload) that is unresolved and avoided.
  - The run protocol is written (section 4 of the record). I built and ran nothing.
  - **Next step (orchestrator):** give the build/run step to the Kimi K3 lane, with a credit ceiling.
  - Record: [docs/nu-daybreak-recovery-trigger-2026-11-03.md](docs/nu-daybreak-recovery-trigger-2026-11-03.md), commit `7cd5301`.
  - If the draft arrives later, comparing it with my note is a separate optional pass.
- **8(a): ANSWERED, now option (ii)** (this reverses the 2 November choice of (i)), **and done, except as item 9 below.**
  - R10 initializer-only schema reload reproduces on Linux, with the same verdicts as Windows.
  - R12 Terra Firma reproduces through its first run (L0), byte for byte, but cannot finish within its 180-second deadline here.
  - Details are in STATUS.
- **8(b): ANSWERED, option (ii) extended, and done.** PLAN states the platform for every reproduced result: a dated update at the top, a platform note after the October evidence, and inline notes.

### 9. ANSWERED (user: yes) and DONE — R12 Terra Firma on Linux with a longer deadline
- Amendment 3 (`4b4249f`, committed before any run) raised the per-process deadline to 1,800 s.
- The pair now passes exactly as on Windows (0 invalid, 0 adverse, byte-identical captures and saves). Each process takes about 12.5 minutes on the software renderer. Results: `ffe493b`.

Original question, kept for the record:
- **Facts:** under the declared amendment, the assets, the build and L0's observations and saved scene all match Windows byte for byte. But L0 can't exit within the package's fixed 180-second deadline. Its shutdown waits for one very slow software-rendered 3D frame, confirmed by thread stacks: it is not a deadlock. More renderer threads didn't help. The fresh-process reopen (L1) and the pair verdict were therefore not reached. Record: `docs/nu-r12-terra-firma-linux-amended-2026-11-03.md`.
- **Options:**
  - (a) Approve a third dated amendment that raises the process deadline (for example to 900 s), keeping everything else fixed. Rerun L0, then L1 and the comparison once.
  - (b) Leave the reopen verdict Windows-only, as PLAN now says.
- **Recommendation:** (b). L0 already matches Windows byte for byte, so the reopen adds little. Also, a longer deadline means a package change made only to rescue a slow environment, which the stop rule discourages. Choose (a) if a fully Linux-only record matters to you. It costs about 30–60 minutes of server time.
- **Blocks:** only the last part of the R12 Linux reproduction.

## 2026-11-02 ~21:20 HKT, item 7 ANSWERED and done — Claude Opus

- **Decision (user approval, orchestrator's choice, ~20:00 HKT):** option (a). The check is **new work**, not a resumption of the stopped R02 input gate. The returned R02 draft stayed unread.
- **Done:**
  - Protocol `06ab165`, committed before any run, with four amendments, each committed before the next attempt.
  - **Result: real X keyboard and mouse input reaches the unchanged standalone game.** Right moved the paddle −0.25 → +67.75, Left moved it to −64.25, and Play, Quit, Play again (a fresh board) and Exit all worked by real clicks.
  - Attempt 05 is still a **protocol FAIL** on the release check: 8 units of drift within 1 s of releasing Left. That is probably display lag at about 2.5 game updates per second, but it is not proven.
  - The five-attempt stop rule applied, and I stopped.
- **Details:** `docs/nu-keyboard-input-check-2026-11-02.md`, STATUS.md, `.artifacts/keyboard-input-check-20261102/`.
- **No decision needed now.** A follow-up check whose release window is measured in game updates would need its own new protocol. I have not started one.

## 2026-11-02 ~05:20 HKT, items 7 and 8 applied — Claude Opus

The orchestrator approved "7(a), 8(a) and 8(b) (the recommended options)".
- **Item 8(a): DONE, option (i).** The R10 initializer-only schema reload and the R12 Terra Firma reopen pair stay Windows-only. No amendment.
- **Item 8(b): DONE, option (ii).** PLAN's R06 sentence now reads "direct history recovery is slower in every pair on Windows (5 of 6 pairs, with one 0.02 ms tie, in the 2 November Linux reproduction)", with a link to the Linux record.
- **Item 7 (answered later, ~20:00 HKT; see the newer entry above). Earlier status: STILL OPEN; the approval contradicts itself.** Item 7 has no parts, so "7(a)" means option (a): run a fresh input check. But my recommended option for item 7 was **(b)**: wait for an explicit user decision, because the check may count as reopening the stopped R02 input gate. The orchestrator's own notes call this "my approval" of the recommended options. Option (b) asks for the user's own decision, which an orchestrator approval of "the recommended option" does not give. So I have **not** run the input check.
  - **To unblock:** the user says either "item 7: run the fresh check (a)" or "item 7: skip (c)". With (a), I commit a protocol first, leave the returned R02 draft unread and label the check as new work, not the R02 gate.

## 2026-11-02 item 8 — Claude Opus

### 8. Two small decisions from the Linux reproductions (neither blocks anyone)
- **(a) Windows-bound packages.** Two retained packages cannot run unchanged here, because their own code checks for Windows:
  - R10 initializer-only schema reload: its build sealer says "frozen probe requires Windows".
  - R12 Terra Firma reopen: its asset check tests a Windows-only read-only file attribute. The assets themselves came out byte-identical to Windows.

  Options:
  - (i) leave them Windows-only;
  - (ii) allow a declared, dated amendment for each (for example, treating file mode as the read-only signal), with a new protocol, and then reproduce them.

  **Recommendation: (i)** for now. Every other package already reproduces, and these two add little unless a later experiment needs them on Linux.
- **(b) One sentence in PLAN.** PLAN says R06's "direct history recovery is slower in every pair". On Linux this held in 5 of 6 pairs (one was a 0.02 ms tie; see `docs/nu-r06-linux-reproduction-2026-11-02.md`). Options:
  - (i) leave PLAN as the Windows record;
  - (ii) let me add "on Windows; 5 of 6 on the Linux reproduction".

  **Recommendation: (ii).** It is a claim change, which AGENTS says is a reason to edit PLAN, but I'd rather the user approve edits to PLAN.

## 2026-11-02 item 7 — Claude Opus

### 7. May I run a fresh "real keyboard input" check, given that the R02 input gate is stopped?
- **Facts:** In STATUS ("Groundwork for the next step") I proposed checking that a real key press, sent to the virtual display through the X server, reaches the unchanged standalone game, and that the result can be seen from outside by screenshot. PLAN names this kind of check ("establish supported input … observations") as the next step after R02's lifecycle pair. But PLAN's **R02 input-construction return** (15 October, five-failure rule) stopped exactly that line of work. It says that resuming requires binding the returned draft and getting independent and parent acceptance first. A fresh check that doesn't reuse the draft could still count as resuming that gate under another name.
- **Options:**
  - (a) Treat the 2 November pre-approval as covering a fresh, independently written input check, with a protocol committed first and the returned draft left unread. State clearly that it is new work, not the R02 gate.
  - (b) Treat it as resuming the R02 gate. Wait for an explicit user decision and follow PLAN's resumption conditions.
  - (c) Skip it.
- **Recommendation:** (b). The project's rules are strict about returned gates, and this is a judgment the user should make. I'm continuing with the Linux reproductions meanwhile.
- **Blocks:** only this input check.

## 2026-11-02 — Kimi K3 (Daybreak branches)

### K2. DONE (no decision needed): branch B finished — export works, stock import API broken at pinned revision
- **Facts:** All three arms ran. Export passed (file contains the complete model and declared screen properties, no entity content, as source-verified). Both import arms crashed identically inside `World.readScreenFromFile`: it addresses the imported screen with one name instead of the game-rooted two, a reproducible engine defect in a callerless code path at pinned Nu `064f7ae`. Results are in `docs/nu-daybreak-screen-persistence-2026-11-02.md` and STATUS.md. Evidence in `.artifacts/daybreak-screen-persistence-20261102/`. Scratch `/tmp/kimi-daybreak-20261102/` (~3 GB, rebuildable) can be deleted.
- **Open follow-up (for a future decision, not blocking):** whether to amend the protocol to test a corrected import (engine patch or new API) is a separate question; documented as "next step" in the results doc.
- **Update, 2 Nov ~19:50 HKT (Claude Opus, user decision D41): corrected import DONE, it passes.** The protocol amendment was committed first (`9c06f41`). I rebuilt 064f7ae with only the one-line fix (`WorldScreen.fs:309`, the same as upstream bryanedds/Nu#1466) and reran the three arms once each.
  - Export passed, with the same file hash as before (`a1827a05…`).
  - **Import passed:** the model and the projected scene both equal B0 in a fresh process, and both negative controls rejected the fresh board.
  - The diagnostic replace-without-destroy arm passed, but its frozen "59 bricks" prediction is falsified. There were 30 brick entities: the 29 model bricks, updated in place because they share names with the fresh board, plus one stale brick (`@449`).
  - This is adapted engine source; stock import at 064f7ae is still broken.
  - Details are in the results doc's "Corrected-import results" section, and evidence is in `.artifacts/daybreak-screen-persistence-20261102/corrected-import/`.
  - **No decision needed.**

### K1. The two private source drafts for the Daybreak branches are still not on the server
- **Facts:** The brief (`.orchestration/TASK-daybreak-kimi.md`) expects two private, unaccepted source candidates under `~/workspace/home-port/.orchestration/rescued/nu-value-recovery/20261025-s180-integrity-stop-01/value-preparation/`:
  - `recovery-reachability-20261025/` (branch A: deliberate recovery fault-trigger). Expected evidence hash `e137ca45b2c97f378b3fbc03b28f3dbe92ca2c14573cb10de7d34949eb9bf7f3`, source coverage `713082c71c7f218ad5d91bd1d958b0995ffe6efa0ba95fc31082b905894e235e`.
  - `screen-persistence-source-20261025/` (branch B: ordinary screen serializer / runtime persistence). Expected evidence hash `abe47eacf194768a31bd37393e8cbc4cba37f079669a6aa2d1f805bf16352e18`, source coverage `0b5f94683a8c066124e9864f45007aeb285921e30fd54f3d8b906e65f11a40ad`.
  - On 2 November only `r14-external-accounts-20261026/` has arrived. I checked both `rescued/nu-value-recovery/` and `rescued/nu-value-recovery-remainder/`; neither candidate is there. The home-port copy from Home `C:/Users/hadri/nu-value-recovery/` is still in progress or missed these two folders.
- **Options:** (a) home-port finishes copying `value-preparation/recovery-reachability-20261025/` and `value-preparation/screen-persistence-source-20261025/` from Home `C:`, so I can verify the candidates' claims against the pinned Nu source, as the brief's step 1 asks. (b) I skip the candidate-check step and do my own independent source reading of the pinned Nu revision for both branches, treating the candidates as unavailable rather than as something to check. The brief explicitly allows this: "the candidates are prior drafts to check, not required inputs."
- **Recommendation:** (b) now, with (a) as a later addition. I will do my own source verification directly from the pinned Nu archive (hash-checked). If the candidates arrive later, I can compare my verified notes against them as a separate pass.
- **Blocks:** only the "check the candidate against source" step for branch A. Branch B has all its required inputs on the server (six files, all SHA-256 verified on 2 Nov) and is proceeding without either candidate.

## 2026-11-02 items 2 and 4 — Claude Opus

- **Item 2: DONE (option a).** home-port's copy of the Home C: folder brought the saved R14 audit input (`citation-input.json`, SHA-256 `152b181e…1966`). I submitted the 81 unchanged decisions once to Scite under the new ID `r14_public_request_frame_20261026_resubmit_20261102`. Scite recorded 13 cited, 68 excluded and 0 skipped. Reading the report back showed 81 screened, no decision missing a reason, not truncated. The old ID stays unverifiable (Scite reports are per session). Receipt: `.artifacts/r14-citation-resubmission-20261102/receipt.json`.
- **Item 4: handed to Kimi K3** (user decision, 2 Nov). The self-contained brief is `.orchestration/TASK-daybreak-kimi.md`. I did none of the work. The brief notes that the two private source drafts for these branches (`recovery-reachability-20261025/`, `screen-persistence-source-20261025/`) are **not yet on the server**: only `r14-external-accounts-20261026/` had arrived in home-port's `rescued/nu-value-recovery/`. The historical inputs for the screen-persistence branch are on the server.

## 2026-11-02 item 3 done — Claude Opus

- **Item 3: DONE** (the user approved it as development work). R04 reproduces on Linux: 4/4 references pass, 5/5 faults caught at their predicted gates, reference records identical to Windows. One environment fix was needed (Mesa OpenGL 4.6 override). Details are in STATUS.md and `docs/nu-r04-linux-reproduction-2026-11-02.md`. Nothing is waiting on the user for this.
- **Item 4 (Daybreak-only):** still parked. The user's restriction names Daybreak models specifically, so the "development is pre-approved" rule doesn't make me eligible. Only the user can change that.

## 2026-11-02 orchestrator decisions — Claude Opus

- **Item 6: DONE** with option (a). Added the 149 restored paths **plus `STATUS.md` and `NEEDS-HUMAN.md`** to the sparse patterns. Those two are also committed files outside the old patterns, and re-applying the patterns would otherwise have deleted them from disk. Nothing new on disk; details are in STATUS.md.
- **Item 2: WAITING** for home-port to copy `C:/Users/hadri/nu-value-recovery/` to the server. If the R14 input (`value-preparation/r14-external-accounts-20261026/`) is there: re-submit the 81 decisions once under a new, dated audit ID and read the report back. If it can't be found: option (b), close the remote check as unverifiable and keep the local decisions as the record.
- **Items 3 and 4:** passed to the user by the orchestrator. Still open.

## 2026-11-02 merge done — Claude Opus

- **Item 1: DONE** (user-approved). `ebe4418` → merge commit `6894668`, not pushed. Details are in STATUS.md.
- **New item 6, sparse-checkout patterns (decision needed):** this folder uses a sparse checkout that lists only a few top-level files, `docs/`, `reports/`, `protocols/`, `scripts/ci_scope.py`, `tests/test_ci_scope.py` and the CI workflow. Home nevertheless had 149 committed files on disk outside those patterns: experiment packages, `.codex/config.toml` and `scripts/linux_smoke.sh`. The merge deleted them from disk. I restored all of them, each hash-verified. **Any future checkout, merge or `git sparse-checkout reapply` can delete them again.**
  - **Options:** (a) Add those 149 paths (or `experiments/`, `.codex/` and `scripts/linux_smoke.sh`) to the sparse patterns. Small change, files stay as they are. (b) Turn sparse checkout off. Git would then write roughly 294 more tracked files that Home never had on disk. (c) Leave it and be careful.
  - **Recommendation:** (a), listing the exact 149 paths so nothing new appears on disk.
  - **Blocks:** nothing now, but it is a trap for the next git operation.
- **For home-port:** the merge changed 61 files on disk; the list is in `.orchestration/evidence/pre-merge-untracked-20261102/merge-ondisk-changes.txt`. The 149 restored files have their original bytes, but new modification times.

## 2026-11-02 update — Claude Opus

- **Item 1:** (superseded: merged, see above). The orchestrator approved (a) in principle and first held it until home-port confirmed.
- **Item 2:** the R14 input is **still missing**. I searched home-port's rescued folders (`nu-value-execution`, `nu-value-execution-remainder` and the others under `~/workspace/home-port/.orchestration/rescued/`) by folder name and by audit ID. They hold A: rescues; this folder lived on Home **C:** (`C:/Users/hadri/nu-value-recovery/20261025-s180-integrity-stop-01/value-preparation/r14-external-accounts-20261026/`). Small (a few JSON files). Still needs a user/home-port decision: copy it from C:, or close the audit as unverifiable.
- **Item 3:** desk check done, nothing built. Facts added under item 3 below. Still waiting for the user's yes or no.
- **Items 4 and 5:** unchanged.

## 2026-11-01 23:55 HKT — Claude Opus (fresh session)

### 1. Move this checkout up to GitHub `main`?
- **Facts:** GitHub `main` `2346751` (26 Oct) descends directly from this checkout's Home HEAD `fca2547` (18 Oct) and adds 25 research commits. Home's uncommitted edits to four tracked files already appear word for word on GitHub. The only exception is one `.gitattributes` line for a stopped draft folder. The untracked file `docs/nu-terra-firma-revision-feasibility-2026-10-18.md` is an older draft of the GitHub version. Ten files in `experiments/nu-r12-terra-revision/` are byte-identical.
- **Options:** (a) Merge `origin/main` into `port/linux-2026-10-30`. Copy the old draft and the identical files into `.orchestration/evidence/` first. Leave the stopped R02/R10/R12 drafts untracked and untouched. (b) Keep this checkout at Home's state and read GitHub only for reference.
- **Recommendation:** (a). Timing is the orchestrator's call, because it changes files and `.git` that home-port's Home-deletion check compares (see item 5).
- **Blocks:** working from the current October 26 rules and records in this folder. Nothing else is waiting on it.

### 2. Old R14 Scite citation audit
- **Facts:** The old blocker was an expired login. This session's Scite works, but `citation_report` for `r14_public_request_frame_20261026` says "no decisions recorded for this session": reports are per session, so the old record can't be checked from a new one. The saved input (81 decisions: 13 credited, 68 not) is in `C:/Users/hadri/nu-value-recovery/20261025-s180-integrity-stop-01/value-preparation/r14-external-accounts-20261026/`. **That folder is missing on this server.** Of that recovery root, only `CURRENT-HANDOFF*`, `CONTINUATION-PROMPT*`, two JSON files, a partial `publication/` folder and three `value-preparation/` subfolders (plus two readiness notes) were copied; `publication-review/` is also absent, though its content is on GitHub.
- **Options:** (a) Recover that folder from Home C:, then re-submit the 81 decisions once under a new, dated audit ID and read the report back. (b) Close the remote check as unverifiable and keep the local decisions (already reflected in GitHub docs) as the record.
- **Recommendation:** (a) if the folder can be copied cheaply; otherwise (b). The published conclusions don't change either way.
- **Blocks:** only this audit record.

### 3. Lift the migration "no native build" hold for one bounded environment check?
- **Facts:** nu-gaia-agentic built current Nu master and ran it headless here on 1 Nov (no GPU, no sudo; recipe `~/workspace/nu-gaia-agentic/docs/agentic-gaia/prototype/run_gaia_headless.sh`). The research's last-stated blocker for R04 (pause/lifecycle behaviour) was "no suitable native environment".
- **Proposal:** Build the research's pinned Nu revision on Linux. Rerun the four existing R04 reference applications and the frozen oracle headless, and compare the results with the recorded Windows results. Stop after five failures at one step. There would be no new arms, no candidate/model/paid runs, and no restart of R02/R10/R12 or the Daybreak-only work. It would finish before the 2 December outage.
- **Desk check, 2 Nov (read-only; nothing built or downloaded):**
  - The pinned Nu revision `064f7ae` (23 Jul 2026) is 1,915 commits behind current master. It uses **OpenGL**, not Vulkan, and officially supports Linux (`Configure.Linux.Development.sh`). Headless OpenGL would use Mesa's software renderer under Xvfb. Mesa and Xvfb are installed; the renderer has not been tried with Nu.
  - The R04 inputs are on the server: `.artifacts/r04-pause-runtime-20261015/` (102 GB, all eight preflights and every runtime folder). The package cache `.artifacts/nuget-packages/` includes Linux x64 native builds of SDL3, SDL3_image/ttf/mixer and Jolt.
  - **Gap 1, .NET SDK:** R04's `global.json` pins SDK **10.0.302** with roll-forward disabled; the server has only 10.0.403. Option: a user-level install of 10.0.302 (about 200 MB over the tunnel, no sudo). Using 10.0.403 instead would change the compiler, so warning counts and outputs would no longer be directly comparable.
  - **Gap 2, Assimp:** the pinned revision expects a system `libassimp` on Linux (apt, needs sudo); none is installed system-wide. nu-gaia-agentic has a user-provided `libassimp.so` in its own tree; another option is a user-level build. It's unknown whether 2D Breakout loads Assimp at startup.
  - The runner scripts (`run.py`, `build.py`, `prepare.py`) look portable (Windows branches are guarded by `os.name`). The preserved arm trees contain Windows build outputs, so a Linux check would build from copies **outside** the workspace and leave the preserved trees untouched.
- **Options:** (a) Approve this check. (b) Keep native work on hold.
- **Recommendation:** (a), including a user-level install of SDK 10.0.302 so the compiler matches. It is the only step I can see that could unblock research, and a failure (for example, the pinned revision won't run on Linux) is still useful. If approved, I would work from copies in a scratch folder outside this workspace, so home-port's check is unaffected.
- **Blocks:** any further R04/R03 evidence. Desk work is not blocked.

### 4. Daybreak-only work
- **Facts:** The deliberate recovery-fault and screen save/reload branches are reserved for verified "Daybreak" ChatGPT models. I (Claude) am not eligible and have not touched them.
- **Question:** Leave them parked, or assign a Daybreak session? Codex is reserved for other work right now, so my default is to leave them parked.

### 5. For home-port / orchestrator: files I changed in this workspace
- `STATUS.md`: new section prepended (the migration record below it is unchanged; the earlier session-recovery paragraph was already an uncommitted change).
- `NEEDS-HUMAN.md`: new file.
- Outside the repo: appended to `~/workspace/exchange/nu-value-research--to--nu-gaia-agentic.md` and `~/workspace/exchange/literature-quota.tsv`.
- **No git operations** (no fetch, commit, branch or merge). **Question:** may I commit these two files on `port/linux-2026-10-30` now, or should I wait until the Nu Home-deletion lane is finished?
- **2 Nov:** resolved by the user's merge approval. STATUS.md and NEEDS-HUMAN.md are committed right after the merge commit.
