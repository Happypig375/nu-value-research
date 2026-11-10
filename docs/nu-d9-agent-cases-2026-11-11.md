# Coding agents with and without explicit case lists: oracle, candidates and scoring (D9 direction 4, 11 November 2026)

**Status: protocol fixed before any oracle run or candidate.** This is amendment 2 to the direction 4 packet in [the D9 packets](nu-d9-directions-2-4-packets-2026-11-10.md) (question, conditions, task, missed-case checklist S1–S5, amendment 1 on isolation). It fills in the details those left open. Results go in later sections without changing sections 1–6.

## 1. What stays as declared

- **Question:** when an AI coding agent adds a new case to a game's state type, do fewer missed-behaviour bugs follow when the code lists cases explicitly (so the compiler warns about the missing case) than when the same code uses a catch-all branch?
- **Conditions:**
  - **E:** shipped Breakout Mmcc (Nu master `47ef39e`).
  - **W:** the same, with the single gameplay-state arm `| Playing | Quit -> gameplay` replaced by `| _ -> gameplay`.
- **Task text:** identical in both conditions, and it does not mention warnings. It is in `experiments/nu-d9-agent-cases/prepare.py` (`TASK`, SHA-256 `c5643d08…`).
- **Budget:** 12 candidates, 6 per condition, in the order E W W E E W W E E W W E. One attempt each, no reruns.
- **Scoring:** oracle checks (a)–(e), the S1–S5 missed-case count, and the compiler-warning record. It is descriptive only.
- **Limits:** one model family, one task, one game.

## 2. Candidate setup (fixed)

- **Folder:** a fresh folder outside this repository: `.../scratchpad/d4/cand-NN-<E|W>/`. It is made by `prepare.py tree … --variant E|W --candidate` and holds only:
  - `Nu/` (the engine, needed to build);
  - `Projects/Breakout Mmcc/` in the candidate's condition;
  - `License.md`, `ReadMe.md` and `TASK.md`.
  - **Change from amendment 1:** amendment 1 said "only the task text and a private copy of `Projects/Breakout Mmcc/`". The engine folder is added because the game cannot be built without it. It is unmodified master, and the same in both conditions.
  - Before the candidate starts, the folder is built once (`dotnet build`, Debug), so the candidate's builds are incremental.
- **Agent:**
  - `claude -p` (Claude Code CLI, the included account, model `claude-opus-5-5`, `--effort medium`), started in the candidate folder.
  - **Tools:** `--tools "Bash,Read,Edit,Write,Glob,Grep"` only. There are no helpers, no web access and no scheduling tools.
  - **No MCP servers:** `--strict-mcp-config --mcp-config '{"mcpServers":{}}'`. Without this, the account's claude.ai connectors (Linear, Todoist, calendar and others) would be exposed to the candidate.
  - **No user settings:** `--setting-sources project,local`, so no user hooks or plugins.
  - Permissions are skipped (`--dangerously-skip-permissions`), so it can build without prompts.
  - The output format is `stream-json --verbose`, and the full tool log is saved outside the folder. The session is not persisted.
  - The prompt is the content of `TASK.md`.
  - Environment: `PATH` with SDK 10.0.403; `NUGET_PACKAGES` points at the shared package cache used for all builds here; MSBuild node reuse is off.
- **Context it sees, checked by two probe calls** (11 Nov, 18:3x UTC, `.artifacts/d9-agent-cases-20261111/ctxprobe*.jsonl`):
  - with these flags, the tool list is exactly the six tools, and there are no MCP servers;
  - asked to name any CLAUDE.md or AGENTS.md in its context, the model answered "NONE";
  - the starting prompt is 7,828 tokens.

  This repository's instructions and memory are not loaded, because the folder is outside the repository.
- **Limit per candidate:** 30 minutes of wall time; if it runs longer, it is stopped and scored as it stands. There is no turn limit.
- **Quota:**
  - Read `read_quota.py --main` before each candidate. Start it only if the forecast fits this project's share (weekly ≤ 96 %).
  - The forecast is the measured cost of earlier candidates, or 1.5 weekly points for the first one.
  - When the next candidate does not fit, the series stops at that point. **Unrun candidates are reported as not run, never replaced by another model.**
  - The series may also stop at the allocation's end. If it stops after an odd number, the conditions are unbalanced, and the report says so.
- **One at a time:** one candidate process at a time, and no GPU use by candidates (they are told not to run the game).

## 3. The behavioural oracle (fixed)

**Build:** the candidate's `Projects/Breakout Mmcc/` source files are copied into a separate master tree (`otree`). Their `Program.fs` is replaced by the oracle's `OracleProgram.fs`. That file runs the game exactly as `World.run` does, plus a read-only per-frame observer (the run loop's `postProcess` callback). The observer writes JSON lines with:
- the selected screen;
- the position of the Paddle and Ball entities;
- the texts of the Message and Score entities;
- the position of the Quit button;
- the number of Life+ icons and of entities.

Entities are found by name in any group of the Gameplay screen. The project builds in Release with SDK 10.0.403. **A candidate whose source does not build fails every check**, and that is recorded as "does not build".

**Run** (`oracle.py`): on our own Xvfb with NVIDIA Vulkan (`scripts/linux_nu_vulkan_env.sh`), with real XTEST keys and clicks:
1. Wait for a stable Title screen, then click Play, and wait until the ball moves.
2. **(e) Normal play:** the ball moves, and holding Right for 0.25 s moves the paddle at least 8 units.
3. Tap P (80 ms). Wait 0.4 s, then observe for 1.0 s, holding Right from 0.2 s to 0.7 s.
   - **(a) Pause stops paddle and ball:** the screen stays on Gameplay throughout, there are at least 10 frames, both entities exist, and neither moves by more than 0.01 units.
   - **(b) The message reads "Paused":** the Message text in every frame of that window, trimmed, with trailing "!" or "." removed, and ignoring case, equals "paused".
4. Tap P again.
   - **(c) Resume continues from the same state.** Within 1.0 s, the ball moves, and its first moved position is within 6.5 units (about 2 updates) of the paused position. The score text and life count at that frame equal those of the paused state. The message is not "Paused" from 0.5 s after resuming. Holding Right for 0.25 s then moves the paddle at least 8 units.
5. Tap P, wait 0.4 s, then click the Quit button where its entity is.
   - **(d) Quit while paused returns to the title:** a Quit entity exists while paused, the Title screen is reached within 8 s, and a new Play gives a moving ball with 5 lives and no "Paused" message.
6. The game is then stopped.

**A run passes when (a)–(e) all hold.**
- **Invalid runs** are not scored as candidate failures: the window is not found, the title is never stable, the "Selected Vulkan Device NVIDIA GeForce RTX 4090 D" line is missing, or the oracle itself errors. An invalid run may be repeated once, and both are kept.
- **A game that crashes or never reaches play fails** the checks it cannot pass.

**Validation, before any candidate:** each of the following is run once.

| Reference (`.artifacts/d9-agent-cases-20261111/oracle-refs/`, never shown to candidates) | Required oracle result |
| --- | --- |
| **R0:** correct (Paused case, a P toggle in `update`, the explicit arm extended, the scene shown while Playing or Paused, the message "Paused") | passes (a)–(e) |
| **M2:** R0 without the scene change, so the scene and Quit button are hidden while paused (the S2 miss) | fails (b) and (d) |
| **M3:** R0 without the P toggle, so pause is never entered (the S3 miss) | fails (a) |
| **E0:** unmodified shipped source (control) | fails (a) and (b) |

- If any reference gives a different result, the oracle is corrected under a dated amendment and all four are re-run.
- Five unresolved validation failures stop direction 4.
- Every attempt is kept.

## 4. Missed-case count and warning record (fixed)

- **Missed-case count:** for each candidate, sites S1–S5 (packet checklist) are marked "handled" or "missed".
  - The marking comes from the diff against the condition's starting source, and from the oracle where a site has a direct check: S2 by (b) and (d), S3 by (a), S4 by (b), S5 by (d).
  - S1 is "missed" if `Paused` reaches the moving update branch, which oracle check (a) shows.
- **Warning record**, from the candidate's tool log:
  - whether any build output showed FS0025 (incomplete match) in Gameplay.fs;
  - whether a later build no longer showed it;
  - whether the final source extends the S1 match arm explicitly.
- **Isolation check:** every tool call's paths are listed. Any read or write outside the candidate folder makes the candidate **invalid**; it is kept and reported, not replaced. Allowed outside paths: the SDK, the package cache, `/tmp`, and system binaries.

## 5. Reporting

- **Per candidate:** condition, build, (a)–(e), S1–S5, warning record, isolation, wall time, turns, quota before and after.
- **Per condition:** pass count and missed-case counts.
- **No claim about effect size**, human developers, other models, tasks or codebases.

## 6. Order of work and the GPU

- The oracle and references are built on the CPU first.
- The GPU validation waits until Nu-Gaia's current GPU trial has stopped (its process gone from `nvidia-smi` and from the process list).
- Candidates need no GPU. They start only after validation passes.
- Candidates' oracle runs happen after all of them finish, or at the checkpoint for those that ran, one at a time.

## Amendment 3 (11 November 2026, 02:4x HKT; before any oracle run and before any candidate)

- **Why:** Nu-Gaia holds the next GPU slot. Its pilot runs agents with Gaia on the GPU for up to 20 minutes each, within a 90-minute allocation. So the GPU validation in section 3 may not be possible for over an hour. Candidates need no GPU.
- **Change: candidates may start before the GPU validation.** This keeps blindness because:
  - the oracle code (`OracleProgram.fs`, `oracle.py`, `build_for_oracle.py`) and the four references were fixed and committed (`be3b97a`) before any candidate existed;
  - **no candidate's output is opened, built for the oracle, or scored until validation has passed;**
  - if validation needs an oracle correction, it is made under a dated amendment from the reference results alone, and the oracle then runs unchanged on every candidate.
- **Construction record so far:**
  - oracle build 01 failed (a missing `open Prime`), which is 1 failure at the oracle-build step;
  - reference build run 02 never reached `dotnet`, because of a script error;
  - reference build run 03 passed for E0, R0, M2 and M3.

  Both are logged in `.artifacts/d9-agent-cases-20261111/OPERATOR-NOTES.log`.

## Amendment 4 (11 November 2026, 03:2x HKT): oracle correction after validation attempt 1, before any candidate output is opened

- **Nu-Gaia's GPU trial ended first:** their verdict read CLEAN at 03:22 HKT, and no Gaia process ran for 60 s. All 12 candidates had finished on the CPU by then (weekly usage 91 % throughout). None of their outputs has been opened.
- **Validation attempt 1** (`.artifacts/d9-agent-cases-20261111/validation/*-01/`):
  - M2 failed (b) and (d); M3 failed (a); E0 failed (a) and (b), all as required.
  - **R0 (correct) failed (c).** Its first moved ball position was 18 units from the paused one, against the limit of 6.5.
- **Cause, an oracle bug:** the trace shows R0 resuming exactly. The first frame after resume moved 3 units, one update, with the message cleared. But the oracle began collecting the resume window only after its 80 ms P tap had ended, while the game resumes on key-down. So the oracle missed the first moved frames.
- **Correction (`oracle.py` only):** the resume window now starts at the frame before the tap and lasts 1.0 s in total. No threshold or other check changes.
- **Next:** all four references are re-run (validation attempt 2). This is validation failure 1 of 5.
