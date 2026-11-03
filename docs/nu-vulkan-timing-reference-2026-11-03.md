# Timing reference re-runs on Vulkan-era Nu: R06 recovery cost and keyboard timing (3 November 2026)

**Status: protocol fixed before any run.** The packages are committed with this file. Results go in a later section, without changing parts 0–2.

## 0. Why, authority and the shared configuration

**Decision D11** (user, 3 November 2026, item 10; the orchestrator's reading):
- Data-only results stay as recorded at Nu `064f7ae`.
- **Timing measurements are re-run as new, declared experiments on Vulkan-era Nu, on this server, which is now the reference machine.**
- The October Home/Windows timings stay recorded, marked provisional: Home was memory-constrained.
- The 2 November Linux timings (Mesa software rendering) are also not the reference.

This file covers the three timing measurements: R06 recovery cost (part 1), and the keyboard input and key-release checks, combined into one port (part 2). These are **new experiments**. Their timings must not be compared with any earlier timing, on any machine or renderer (3 November timing rule).

**Shared configuration** (the same for every process in both parts):
- **Nu master `47ef39e176424675f067c378c3a5f86f9c5ec3be`** (3 November 2026, 07:25 UTC):
  - pinned input `.artifacts/vulkan-timing-20261103/nu-47ef39e.tar`, SHA-256 `3dcae8b0c61103b12b215b631bcca96fc219bfced876e1d35753db348581faac`, made with `git archive` (git 2.34.1);
  - the tar header names the commit, and the package scripts check both the hash and the commit.
- **Why master:** it is current upstream. The orchestrator suggested it, and nu-gaia-agentic works from this line and confirmed the Vulkan route on it. It also includes the upstream screen-import fix. No reason was found to prefer another Vulkan-era revision.
- **Build:** .NET SDK 10.0.403 (user-level, `~/.dotnet`; master has no `global.json`), Release, with a private copy of the NuGet cache.
- **GPU:** NVIDIA RTX 4090 D (driver 580.178.04), Vulkan through the NVIDIA driver (`VK_ICD_FILENAMES` / `VK_DRIVER_FILES` = `nvidia_icd.json`), on our own Xvfb display `:94`, via `scripts/linux_nu_vulkan_env.sh`.
  - **No software rendering for Nu.** Every process must log "Selected Vulkan Device NVIDIA GeForce RTX 4090 D"; otherwise that process is invalid.
  - The environment check on 3 November showed this line, and the window shows the game image.
- **Run discipline:**
  - one process at a time, `nice -n 10`;
  - before each process, wait until the GPU is idle (no process on it except root's Xorg, utilization < 10 %), polling every 15 s for up to 30 min, and record the wait;
  - the wrapper records load average, free memory and swap, `nvidia-smi` before the run, and GPU process samples every 0.5 s.
- **Shared GPU:** another workspace's `dotnet` process was seen on the GPU on 3 November. Hence the idle check.

## 1. R06 recovery cost, ported (package `experiments/nu-vulkan-r06-recovery-cost/`)

**Question (unchanged in kind from the [original contract](../experiments/nu-r06-recovery-cost/pre-execution-contract.md)):** for one declared B0 checkpoint, what does each supported route cost in component time?
- **History (H):** Gaia snapshot, then Gaia undo.
- **Reconstruction (R):** serialize the gameplay model, then deserialize and set it.

**Kept from the original:**
- the seed (the fixed B0 model `experiments/nu-history-b1/checkpoint/gameplay.symbol`, after the same content-clear step);
- functional, accompanied Gaia in Gameplay edit mode, with the static 60-update clock;
- the 10-step drift with its source-predicted model;
- both routes and their timers (`Stopwatch` ticks: acquisition, direct recovery, request-to-ready, with the readiness timestamp as the first operation of the next callback);
- the readiness oracle (complete model and projection equal to B0, halted, no events during recovery);
- the GC/memory samples outside the timers, the 600 s deadline and the 1,200-callback watchdog.

**Ported (each item changes what is measured, as stated):**

| Change | Why | Effect on what is measured |
| --- | --- | --- |
| Engine: `064f7ae` → `47ef39e` (1,938 commits), OpenGL → Vulkan on the GPU | D11 | All timings are new. Any engine change on the snapshot/undo/serialize paths is part of the result. |
| Names: `Advancing` → `TimeAdvancing`, `TimeUpdateEvent` → `TimeAdvanceEvent` | Master renamed them; the meaning is unchanged (checked in source) | None |
| The Breakout scene no longer has the rotating `StaticModel` cube or the `Light3d` entity | Master's sample changed | Less content to rebuild after recovery. The projection drops the cube rotation, and the recorded B0 projection is compared **with `StaticModel`, `Light3d` and the rotation removed** |
| Projections are compared as JSON trees (`JsonNode.DeepEquals`), not exact strings | Robust to serializer formatting | None on equality; the comparison work sits outside the timers |
| The bridge is installed at master's anchors (`firstFrameCallbackOpt`) | Master renamed the parameter | None. The bridge is the same B0 bridge with R06's weak identity witness. |

**Attempts, fixed in advance** (`series.py`):
1. One unscored feasibility process per route: F-H, then F-R. A feasibility failure allows a documented correction under a dated amendment, committed before the next attempt.
2. Then **20 measured pairs, 40 processes**, in alternating balanced order: `H01 R01 R02 H02 H03 R03 R04 H04 …` (the order within each pair flips every pair).
3. Every process starts fresh, with no hidden warm-up.
4. **A failed measured process stops the series.** It is kept. Continuing needs a dated amendment.
5. Five unresolved failures at one unchanged step stops that step.
6. No outlier filtering, replacement or extension.

**Pass, per process:** the same requirements as the original (seed, drift order and model, readiness oracle, exit code 0), plus the Vulkan device line.

**Outcomes** (`summarize.py`, descriptive only, for passing measured processes, with every attempt listed):
- for each route and component: the median, quartiles and range in ms;
- the paired difference history − reconstruction for each component, with counts of pairs where history was slower or faster, and ties.

No significance test or benefit claim.

**What this cannot show:** the same limits as the original. It doesn't measure debugging or repair benefit, native contacts or the framebuffer, retention or eviction policy, or editor workflow. The serialized payload is narrower than a Gaia world snapshot.

## 2. Keyboard input and release timing, ported (package `experiments/nu-vulkan-keyboard-timing/`)

**Question:**
- Does real X keyboard input (XTEST) reach unchanged standalone MMCC Breakout at master, judged from screenshots only?
- How long after a key press does movement appear, and how long after release does the paddle stop?
- How far does it overshoot after release, and at what update rate does the game run?

This combines the [keyboard input check](nu-keyboard-input-check-2026-11-02.md) and the [key-release check](nu-key-release-check-2026-11-02.md).

**Kept:**
- XTEST input, window discovery and focus;
- `xwd` window screenshots decoded with their colour map;
- the paddle/brick/wall detection rules, thresholds and title/gameplay/settle logic, copied unchanged from `input_check.py` (lines 73–251);
- the no-input control (±4 units over 0.5 s);
- the secondary click path: Quit → title → Play (fresh board, 5 lives) → Quit → Exit (exit code 0).

Master did not change the window size, the title or Gameplay button positions, or the sprite images (checked by diff).

**Changed, and why** (each item changes what is measured):
- **Master runs on the GPU at roughly the display rate, faster than screenshots can be taken.** The originals ran at about 2.5 updates per second, so the key-release check could count each distinct frame as one update. That is impossible here.
- **The rotating cube is gone,** so frames no longer differ on every update anyway.
- **So the port measures, per trial:**
  - press latency in ms, with lower and upper bounds set by the screenshots around the first movement;
  - release-to-stop time in ms, with lower and upper bounds;
  - **overshoot after release, in units and in updates** (units ÷ 4, because `Gameplay.update` moves the paddle 4 units per update). This is the same quantity the original reported as "moved on exactly 2 more updates";
  - the update rate, from the paddle speed (units per second ÷ 4);
  - the screenshot interval.
- **Trials:** release once a screenshot shows the paddle 32 units from the trial start. That keeps it clear of the ±128 clamp. (The original held until 64 units, with a 1 s rule in seconds.) "Stopped" means unchanged within 0.5 units for 0.5 s. There are 3 Right and 3 Left trials per process, alternating.

**Attempts, fixed in advance** (`series.py`):
1. One unscored feasibility repeat (KF). Its failure allows a documented correction under a dated amendment; for example, the detection thresholds might not suit Vulkan rendering.
2. Then **10 repeats (K01–K10)**: fresh processes, 60 trials in total.
3. Invalid repeats (window, title or settle problems) are kept and not replaced.
4. The five-failure rule applies per step.
5. There are no paired arms: this is a single-arm measurement, repeated.

**Validity, per repeat (data checks):**
- gameplay is reached by a real click;
- the no-input control stays still;
- every trial travels 32 units and then stops.

The secondary click path is recorded.

**Outcomes** (`summarize.py`): the median, quartiles and range of each measure, for Right, Left and all trials together. Descriptive only, and valid only on this server and configuration.

**What this cannot show:** real hardware, a window manager, other keys or games, pause, audio, agent access, Gaia input, or benefit.

## 3. Order of work

1. Commit this file and both packages.
2. Build in scratch: the R06 probe against the bridged tree, and the standalone game from an unbridged tree (`prepare.py --no-bridge`).
3. Run R06 F-H and F-R, then the 40 measured processes.
4. Run keyboard KF, then K01–K10.
5. Append the results here, then update STATUS and NEEDS-HUMAN.
6. Delete the scratch builds and log the deletions.

## Amendment 1 (3 November 2026, after keyboard feasibility repeat KF, before any scored keyboard repeat)

- **What KF found:**
  - Five of six trials were valid, and the control and click path passed.
  - The sixth trial (Left 3) showed no movement for 8 s, because the screen read **"Game over!"**. At about 60 updates per second, the ball loses all five lives within seconds, and Breakout then freezes the paddle. At 2.5 updates per second (the 2 November runs) this could not happen in time.
  - KF is kept as recorded (`.artifacts/vulkan-timing-20261103/keyboard/runs/KF/`).
- **Change** (`keyboard_timing.py`; nothing else changes):
  - Before each trial, if no life icon is left, start a fresh board with the ordinary Quit → Play clicks.
  - Any trial that ends with no lives left is kept, labelled `interrupted_by_game_over`, excluded from the summaries, and redone once on a fresh board. Such a trial is excluded even when it looked valid, because a game-over freeze could fake the "stopped" reading.
  - A repeat is valid only if all 6 counted trials are valid.
- **Verification:** one more unscored feasibility repeat, **KF2**, then K01–K10 as planned.
- **R06 is not affected.** Its feasibility processes and all 40 measured processes passed under the original protocol.

## Results, part 1: R06 recovery cost (3 November 2026, 20:44–20:51 HKT)

**Conclusion:**
- On the reference configuration (Nu master `47ef39e`, Vulkan on the RTX 4090 D, this server), **Gaia's history route is faster than reconstruction for both taking and using the recovery point.**
  - Taking the snapshot is faster in **20 of 20 pairs**.
  - The undo call itself is faster in **19 of 20**.
  - Request-to-ready is faster in **16 of 20**.
- This is a **new reference result.** It must not be compared with the October Windows/Home series (where undo was slower in 6/6 pairs) or the 2 November Linux software-rendering series (5/6). Those used a different engine revision, renderer and machine, and the Home timings are marked provisional.
- Both routes always reached the declared B0 output.

**Attempts:** all 42 processes passed at their first attempt: F-H and F-R (unscored feasibility), then the 40 measured processes in the declared order.
- Every process logged "Selected Vulkan Device NVIDIA GeForce RTX 4090 D".
- Each took 4.5–6.8 s in total, with peak GPU memory about 1.2 GB.
- No other process appeared on the GPU during the series; the idle check waited 15 s before some processes while our own previous process wound down.
- Load average was 2.5–6.5 and free memory about 470 GB; no swap was used.
- One launch command failed before any process ran: the runner was started from a scratch copy, so it could not find the wrapper. That is logged in `OPERATOR-NOTES.log`; it was not an attempt.

**Component times (ms; 20 passing measured processes per route):**

| Component | History (H): median [quartiles; range] | Reconstruction (R): median [quartiles; range] | Paired H − R: median; H faster / slower |
| --- | --- | --- | --- |
| Take the recovery point | 0.70 [0.44–0.75; 0.40–0.77] | 4.47 [4.01–6.09; 2.40–6.53] | −3.79; **20 / 0** |
| Recover (direct call) | 10.26 [5.95–10.38; 5.69–11.73] | 19.27 [13.76–23.93; 8.54–25.33] | −9.72; **19 / 1** |
| Request to ready (next callback) | 13.48 [7.69–13.86; 7.31–15.46] | 21.08 [15.28–26.03; 9.46–27.88] | −8.90; **16 / 4** |

**Observed, not explained:**
- History recovery times fall into two clusters (about 5.9 ms and about 10.3 ms), interleaved across the series. They do not follow run order or position within a pair.
- Reconstruction times are spread more widely (8.5–25 ms).
- Possible causes, none tested: CPU core placement or frequency, or GC timing. The per-process GC and memory samples are in each trace.

**What this does and does not show:** the same limits as the original contract.
- The history route keeps a whole world state; the reconstruction payload is only the gameplay model.
- The timings are machine time for one checkpoint, not repair effort or a benefit.
- They are valid only on this server and configuration.

**Evidence:**
- `.artifacts/vulkan-timing-20261103/r06/`: prepare and build receipts, `runs/` with the ledger, each process's trace, `result.json`, environment and GPU samples, and `summary.json`.
- `experiments/nu-vulkan-r06-recovery-cost/result-receipt.json` is the committed copy of the summary.

## Results, part 2: keyboard input and release timing (3 November 2026, 20:53–21:01 HKT)

**Conclusion:**
- On the reference configuration, real X keyboard input reaches standalone MMCC Breakout at Nu master in every trial.
- The game runs at about **60 updates per second** (median 60.2).
- Movement appears **within about 71 ms** of a key press (median upper bound), and the paddle stops **within about 59 ms** of release (median upper bound).
- **It overshoots by 3 updates after release** (median; range 2–4), that is 12 units.
- These are **new reference values for this server and configuration.** They must not be compared with the 2 November software-rendering checks (2.5 updates per second, 2-update overshoot), which used a different engine revision and renderer.

**Attempts:**
- KF (unscored) found the game-over freeze, which led to amendment 1. KF2 (unscored) then passed.
- **K01–K10 all passed at their first attempt:** 60 counted trials, all valid.
- In K06 one trial ended on game over. Under amendment 1 it was kept, excluded, and redone on a fresh board.
- Every repeat: gameplay was reached by one real click, the no-input control stayed still, and Quit → title → Play gave a fresh board (5 lives, paddle at the start). Exit by click returned code 0.
- Every repeat logged "Selected Vulkan Device NVIDIA GeForce RTX 4090 D". No other process appeared on the GPU.

**Measures (60 trials: 30 Right, 30 Left; Right and Left agree closely):**

| Measure | Median [quartiles; range] |
| --- | --- |
| Press → first screenshot showing movement (upper bound of press latency) | 71.1 ms [66.4–80.5; 52.9–94.8] |
| Release → first screenshot of the final position (upper bound of stop time) | 58.9 ms [52.5–64.4; 41.8–76.6] |
| Overshoot after release | 3.0 updates [3–3; 2–4] |
| Update rate (paddle speed ÷ 4) | 60.2 per s [57.7–63.0; 53.7–71.0] |
| Screenshot duration (per-trial median) | 24.9 ms [23.6–28.8; 22.3–36.9] |

**Limits of these numbers:**
- The **lower** bounds of press latency and stop time are 0 ms in every trial: the first screenshot starts as the key event is sent. So only the upper bounds are informative, and they include one screenshot's capture time (about 25 ms).
- Overshoot in updates rests on the source fact of 4 units per update.
- Valid only on this server and configuration. No real hardware, window manager, other games or Gaia.

**Evidence:**
- `.artifacts/vulkan-timing-20261103/keyboard/`: prepare and build receipts, and `runs/` with KF, KF2, K01–K10, each with its trace (every poll), screenshots, game logs, environment and GPU samples, plus `summary.json`.
- `experiments/nu-vulkan-keyboard-timing/result-receipt.json` is the committed copy of the summary.

## Status of D11

- Both timing re-runs are done. They are the reference timings for this server.
- The October and 2 November timings stay recorded as provisional and are not compared with these.
- Data-only results are unchanged.
