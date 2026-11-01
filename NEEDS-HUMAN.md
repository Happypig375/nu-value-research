# Questions for the user / orchestrator — nu-value-research

Newest first. Each item lists the options, my recommendation and what it blocks. Background is in [STATUS.md](STATUS.md) (section dated 1 November 2026).

## 2026-11-02 — Kimi K3 (Daybreak branches)

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
