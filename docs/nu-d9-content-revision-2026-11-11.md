# Content revision: Nu's entity propagation versus an ordinary helper (D9 direction 3, 11 November 2026)

**Status: protocol fixed before any probe run.** This is the run-level protocol for direction 3 of [the D9 packets](nu-d9-directions-2-4-packets-2026-11-10.md) (question, conditions P and O, tasks T1–T3, outcome, fairness rule, budget). Results go in later sections without changing sections 1–6.
- The October R12 Terra Firma packages (pinned `064f7ae`, OpenGL) and the stopped R12 material-intent draft are not reused, opened or relabelled.
- This is a new port to Nu master with its own attempt budget.

## 1. Question

**For matched revision tasks on a real scene, does Nu's entity propagation deliver the required edits with fewer misses, or fewer unrequested changes, than an ordinary helper given the same intent list?**
- **P (Nu):** edit the source entity, then call `World.propagateEntityStructure` on it, which is the operation behind Gaia's "Propagate" command.
- **O (ordinary helper):** a small loop that sets the one field on every family member and skips the declared local keeps.

A result where O matches or beats P is valid and expected to be likely.

## 2. Fixed setup

- **Engine:** Nu master `47ef39e` (pinned tar, SHA-256 `3dcae8b0…faac`).
- **Scene:** Terra Firma, `Projects/Terra Firma/Assets/Gameplay/Scene.nugroup` (SHA-256 `95988f8c…4665`), as copied to the Release build output.
  - Master's scene differs from October's `064f7ae` scene: the palms are rigid-model entities, and 38 entities name `Villa/Palm` as their source.
- **Probe:** `experiments/nu-d9-content-revision/TerraProbe.fs` replaces Terra Firma's `Program.fs` in a scratch tree; the other Terra Firma sources are unchanged.
  - It runs a plain `NuPlugin` from the same assembly, so Terra Firma's dispatchers are available but its screen flow does not run.
  - It creates the screen `Gameplay` and loads the scene as group `Scene`, so entity addresses match the scene's links.
  - **Everything happens inside one frame callback**, so no game time or physics step passes between the observations.
- **Renderer:** NVIDIA Vulkan on our own Xvfb (`scripts/linux_nu_vulkan_env.sh`). There is an idle-GPU check before each process, and every process must log "Selected Vulkan Device NVIDIA GeForce RTX 4090 D". SDK 10.0.403, Release.
- **Family and local palm**, defined by rule and recorded by the probe at load:
  - the **family** is the source `Game/Gameplay/Scene/Villa/Palm` plus every entity whose `PropagationSourceOpt` is that source;
  - the **local palm L** is the first family member, in address order, whose address contains `/Villa-0002/`. It sits inside a copied villa, so it is reached both directly and through the villa's own propagation.
- **Values** (exactly representable): shared tint `AlbedoOpt = (0.25, 0.5, 0.75, 1)`, local tint `(1, 0, 0, 1)`, shared roughness `RoughnessOpt = 0.75`.

## 3. Tasks and routes

**Preparation** (identical in both conditions, before the route acts): in T2 and T3, L gets the local tint (only its `AlbedoOpt` changes).

| Task | P: Nu propagation | O: ordinary helper (same intent list) | Required for every family member afterwards |
| --- | --- | --- | --- |
| **T1:** shared tint | set the source's `AlbedoOpt` to the tint, then propagate | set `AlbedoOpt` to the tint on every family member | `AlbedoOpt` = tint |
| **T2:** shared tint, L keeps its local tint | the same as T1 | the same, skipping L (intent list: "L keeps its tint") | L: local tint; all others: tint |
| **T3:** shared roughness, L keeps its local tint | set the source's `RoughnessOpt` to 0.75, then propagate | set `RoughnessOpt` on every family member | all: roughness 0.75; L also keeps the local tint |

- In every task, the other fields of each member's `MaterialProperties` must stay as loaded.
- **Control N** (no task, no route): load, save, reopen. It shows whether saving and reopening alone produce differences.

## 4. Observations and pass conditions

The probe writes JSON snapshots of every entity in the group: the dispatcher, the propagation source, the material fields, and every saved property (`World.writeEntity` without order and propagation history).
- **Op process:** `before.json` (as loaded), `prepared.json`, `after.json`, then saves `saved.nugroup`.
- **Reopen process** (fresh): loads `saved.nugroup` and writes `reopen.json`.

`check.py` scores each run:
- **Missed edits:** family members whose material fields do not meet the requirement, counted separately after the op and after reopen. It covers albedo and roughness, plus the rest of the material record compared with `before.json`.
- **Unrequested changes:** each `(entity, property)` pair in `after.json` that differs from `before.json`, other than the family members' `MaterialProperties`, plus any entity added or removed.
- **Persistence:** every entity and property in `reopen.json` equals `after.json`.
- **Pass:**
  - 0 missed after the op and after reopen;
  - 0 unrequested changes;
  - persistence holds;
  - both processes exit 0 with the Vulkan device line.
- **Control N passes** when `after.json` equals `before.json` and `reopen.json` equals `after.json`. **If a control fails, that round's comparison is invalid.** It is recorded, and the cause is found before any scored round continues.
- **Measures:**
  - missed and unrequested counts;
  - operation time (ms), save time and load time;
  - declared steps:
    - P: 2, edit the source field and propagate;
    - O: 1 invocation of the helper with field, value and keep list. Writing the helper itself is a one-time cost; it is the 10-line loop in `TerraProbe.fs`, and its line count is reported.

## 5. Runs, attempts and stop rule

- **Feasibility round F (unscored):** N, then T1-P, T1-O, T2-P, T2-O, T3-P, T3-O. Each is an op process followed by a reopen process.
  - A failure of the apparatus (crash, missing device line, a control with differences, a probe error) allows a correction under a dated amendment, committed before scored rounds.
  - **An adverse result of P or O is a result, not a reason to amend.**
- **Scored rounds 1–3:** each has N first, then the six task × route runs in a rotating order:
  - round 1: T1 T2 T3, with P before O;
  - round 2: T2 T3 T1, with O before P;
  - round 3: T3 T1 T2, with P before O.

  That makes 3 scored runs per condition × task, 18 op/reopen pairs plus 3 controls.
- **Stop rule:**
  - Five unresolved failures at one unchanged step stop it.
  - Infrastructure failures (a 300 s timeout, a launch exception, a missing device line) stop the series.
  - Every attempt is kept.

## 6. What it cannot show

- Designer effort or skill.
- Collaboration or merges.
- Other scenes, families or properties.
- Gaia's interactive editing path; the probe calls the same world functions directly.
- Engines other than Nu.

Steps are declared counts, not measured human work. The helper is fair only in that it receives the same intent list. A helper denied the list would be invalid.

## Amendment 1 (11 November 2026, 03:3x HKT): after feasibility attempt 1, before any scored round

- **Feasibility attempt 1 stopped at control N:** the probe raised "Screen 'Game/Gameplay' already exists and cannot be created". The engine had already made that screen by frame 3, even with the plain plugin. Kept in `.artifacts/d9-content-revision-20261111/series/round-F.attempt1/`.
- **Correction (`TerraProbe.fs` only):** reuse an existing `Gameplay` screen, and destroy any existing `Scene` group before loading the file, inside the same callback. The probe records which of the two existed in `setup.json`: here the screen existed, and the group did not. Probe build 03 passed.
- **Feasibility attempt 2 (unscored)** ran all seven runs. Every process exited 0 with the NVIDIA Vulkan device line.
  - Control N: no difference after save and reopen.
  - The family has 32 members; the local palm L is `Game/Gameplay/Scene/Villa-0002/Palm`.
  - T1 and T2 passed on both routes, and T3-O passed. **T3-P missed L's roughness**, which stayed unset, both after the operation and after reopen. This is an adverse result for P, not an apparatus failure, so it does not change the protocol.
- **Construction record:** probe build 01 failed (a missing namespace); builds 02 and 03 passed. Feasibility failures at the run step: 1.
- **Scored rounds 1–3 follow unchanged.**

## Results (11 November 2026, 03:37–03:45 HKT; scored rounds 1–3)

**Conclusion:**
- **For a shared change with no conflicting local edit (T1), or a shared tint where the local palm keeps its own tint (T2), Nu's propagation and the ordinary helper both deliver every required edit:** 3/3 each, with no unrequested change, and the result survives save and fresh reopen.
- **When the shared change is to a different field than the local override (T3), propagation misses it on the overridden palm in every run (0/3).** The helper delivers it (3/3).
- **Cause:** propagation merges whole properties. The local palm's `MaterialProperties` differed from the source's last propagated value, so the whole record counted as a local override and was kept as it was. The palm kept its local tint, but its roughness stayed unset instead of 0.75. The helper sets one field at a time, so the local tint and the new roughness coexist.
- **Machine time:** propagation took about 0.53 s per operation (it rebuilds the 31 targets and the copied villas). The helper took 1–6 ms. Saving took about 0.5–0.7 s for both.

| Task | P: Nu propagation | O: ordinary helper | Missed edits (P / O) | Unrequested changes | Persists after reopen |
| --- | --- | --- | --- | --- | --- |
| **T1:** shared tint, 32 palms | 3/3 | 3/3 | 0 / 0 | 0 | yes |
| **T2:** shared tint, L keeps its local tint | 3/3 | 3/3 | 0 / 0 | 0 | yes |
| **T3:** shared roughness, L keeps its local tint | **0/3** | 3/3 | **1** (L's roughness) / 0 | 0 | yes, the miss persists too |
| **Control N:** load, save, reopen | 3/3 with no differences | | | | |

**Operation time, median:** P 525–612 ms; O 1.0–5.8 ms. **Declared steps:** P 2 (edit the source, propagate); O 1 helper invocation with the field, the value and the keep list, after a one-time 10-line helper.

**How to read this:**
- The helper wins on T3 only because it was given the same intent list ("L keeps its tint") and works field by field.
- Propagation needs no list of family members: it found all 32 by itself. The helper's family list came from the same source links, so building it is not counted here.
- In a real editor, P is the Gaia "Propagate" command, while O is a script the user must write and keep.
- Propagation's whole-property merge is a design choice, not a defect. But it means **a field-level local override silently blocks every later shared change to any other field of the same property.** Nothing warns about it.

**What this does not show:** designer effort, other properties or families, collaboration, Gaia's interactive path, or other engines. The October `064f7ae` Terra Firma results used a different scene revision and observer, so they are not directly comparable.

**Attempts (all kept):**
- Probe build 01 failed (a missing namespace).
- Feasibility attempt 1 stopped on the existing screen (amendment 1); attempt 2 passed the apparatus checks.
- All 42 scored processes exited 0 and logged "Selected Vulkan Device NVIDIA GeForce RTX 4090 D", with no timeouts.

**Evidence:**
- `.artifacts/d9-content-revision-20261111/`: `builds/`, and `series/` with the ledger, every snapshot (`before`, `prepared`, `after`, `reopen`), the saved scenes, `score.json` per run, and environment and GPU samples; `summary.json`; `OPERATOR-NOTES.log`.
- Committed copy: `experiments/nu-d9-content-revision/result-receipt.json`.
