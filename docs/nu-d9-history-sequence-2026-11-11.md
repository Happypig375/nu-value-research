# Content revision follow-up: does an ordinary helper edit change what a later Nu propagation delivers? (D9 direction 3 supplement, 10–11 November 2026)

**Status: protocol fixed before any engine outcome** (committed before the first probe run). Results go in later sections.
- Scope: a scoped supplement to [direction 3](nu-d9-content-revision-2026-11-11.md). The original direction 3 series, its scores and its artifacts are not changed.
- October R12 packages and the stopped R02/R10/R12 constructions are not touched.
- Goal: `.orchestration/GOAL-D9-history-sequence-20261111.txt`.

## 1. Question

The D9 evidence audit predicted, from the engine code, that the ordinary helper's direct edits would make a later Nu propagation treat every family member as locally overridden, and so skip them. **Does that happen?**
- If it does not, the null result is reported.
- The prediction rests on `propagateEntityDescriptor`: the source's propagation history has no `MaterialProperties` entry, and the helper's targets then carry a non-default value.

## 2. Fixed setup (the same as direction 3)

- **Engine and scene:**
  - Nu master `47ef39e` (pinned tar, SHA-256 `3dcae8b0…faac`), SDK 10.0.403, Release.
  - Terra Firma `Assets/Gameplay/Scene.nugroup` (SHA-256 `95988f8c…4665`).
  - NVIDIA Vulkan on a private Xvfb (`scripts/linux_nu_vulkan_env.sh`), with the idle-GPU rule and the device-line check.
- **Fresh scratch tree and a new probe:** `experiments/nu-d9-history-sequence/HistoryProbe.fs` replaces Terra Firma's `Program.fs`. It works like direction 3's probe (amendment 1 included): a plain plugin, the existing `Gameplay` screen reused, and the scene loaded as group `Scene`.
- **Family and values:**
  - the family is the source `Game/Gameplay/Scene/Villa/Palm` plus every entity whose `PropagationSourceOpt` is that source (32 in direction 3);
  - tint `AlbedoOpt = (0.25, 0.5, 0.75, 1)`, roughness `RoughnessOpt = 0.75`.
  - There is no local keep.

## 3. Sequences (identical intended edits; only the route differs)

- **Step 1:** shared tint on all 32.
- **Step 2:** shared roughness 0.75 on all 32, keeping the tint.

| Sequence | Step 1 | Step 2 |
| --- | --- | --- |
| **PP** | set the source's `AlbedoOpt`, then `World.propagateEntityStructure source` | set the source's `RoughnessOpt` (from its current record, so the tint is kept), then propagate |
| **HP** | helper: set `AlbedoOpt` on every family member | Nu propagation, as in PP step 2 |
| **HH** | helper, as in HP step 1 | helper: set `RoughnessOpt` on every family member |
| **N** (control) | none | none |

- **Required after step 1:** every family member has albedo = tint, roughness as loaded, and every other material field as loaded.
- **Required after step 2:** every member has albedo = tint, roughness = 0.75, and every other material field as loaded.

## 4. Processes and observations

- **Op process:** loads the scene, then snapshots `before`; runs step 1, snapshots `after1` and saves `saved1.nugroup`; runs step 2, snapshots `after2` and saves `saved2.nugroup`. Everything runs in one frame callback.
- **Reopen processes** (fresh, one per file): `reopen1` from `saved1`, and `reopen2` from `saved2`.
- **Control N:** an op process with no steps (snapshots `before` and `after2`, saves `saved2`), plus `reopen2`.
- **Each snapshot records, for every entity:**
  - the core saved properties (`writeEntity false false`, as in direction 3);
  - **`Order`** and the **propagation history** (`PropagatedDescriptorOpt`), from `writeEntity true true`, kept as separate fields;
  - the raw `MaterialProperties` string;
  - the probe's material summary (albedo, roughness).
- **The checker also derives albedo and roughness independently** from the raw `MaterialProperties` string, and reports any disagreement with the probe's summary.

## 5. Measures (fixed now)

- **Live-field success, per stage** (after1, reopen1, after2, reopen2): the number of family members missing the requirement.
  - The primary outcome is **missed members after step 2 and after reopen2**.
  - Misses are also checked with the independently derived values.
- **Unrequested live changes:** core properties of non-family entities, and non-material core properties of family members, compared with `before`; plus entities added or removed.
- **Persistence:** core properties in each reopen equal the matching after-snapshot.
- **Metadata (observations, not defects):**
  - the number of entities whose `Order` changed at each step;
  - whether each family member's and the source's history contains a `MaterialProperties` entry after each step;
  - the number of history strings changed.
- **Machine time:** step 1, step 2 and save, in ms.
- **Pass per sequence run:** 0 missed at all four stages, 0 unrequested, persistence at both reopens, every process exit 0 with the device line.
- **Control N passes** with no core differences and persistence.
- **Prediction to test:** HP misses the 31 non-source members' roughness after step 2. PP and HH pass.

## 6. Runs, budget and stop rule

- **Feasibility round F (unscored):** N, PP, HP, HH.
  - Only an apparatus failure (crash, missing device line, a control with differences, a probe error) allows a dated amendment before the scored rounds. **An adverse or null scientific result does not.**
- **Scored rounds 1–3:** N first in each, then the sequences in a rotating order: round 1 PP HP HH; round 2 HP HH PP; round 3 HH PP HP. That gives 3 replicates per sequence, 3 controls, and 9 × 3 + 3 × 2 = 33 processes.
- **Construction budget:** 5 failures at one unchanged step. Infrastructure failures (a 300 s timeout, a launch error, a missing device line) stop the series. Every attempt is kept.
- **Allocation:** checkpoint at 21:22 UTC on 10 Nov at the latest. If the scored rounds cannot finish, the completed ones are reported and the rest stay unrun.

## 7. What it cannot show

- Gaia's interactive path: the probe calls the same world functions.
- Other properties or families; designer effort; other engines.
- One scene revision only.
- Whole-property merge is a design choice. Whatever the result, it is reported as engine behaviour, not an upstream bug.

## Results (feasibility 20:25:16–20:27:00 UTC; scored rounds 20:27:38–20:33:16 UTC, 10 Nov 2026, ledger times)

**Conclusion: the audit's code-based prediction is confirmed by measurement.**
- **After an ordinary helper edit, a later Nu propagation does not deliver the next shared change to the 31 linked palms.** In HP, 0/3 runs pass: after step 2 and after fresh reopen, all 31 non-source members kept the tint but had no roughness. Only the source received 0.75.
- **Propagation twice (PP) and the helper twice (HH) both deliver both steps,** 3/3 each.
- No sequence made an unrequested live change, and every stage persisted after reopen.

| Sequence | Pass | Missed after step 1 / reopen 1 | Missed after step 2 / reopen 2 | Unrequested | Persistence differences | Step 1 / step 2 time, median |
| --- | --- | --- | --- | --- | --- | --- |
| **PP:** propagate, propagate | 3/3 | 0 / 0 | 0 / 0 | 0 | 0 | 571 ms / 504 ms |
| **HP:** helper, then propagate | **0/3** | 0 / 0 | **31 / 31** in every run (roughness unset; the source is fine) | 0 | 0 | 4.7 ms / 446 ms |
| **HH:** helper, helper | 3/3 | 0 / 0 | 0 / 0 | 0 | 0 | 3.0 ms / 1.3 ms |
| **N:** load, save, reopen | 3/3, no differences | | | | | |

- **The independently derived values agree with the probe's summary everywhere** (0 disagreements).
- **Raw check** (round-1 HP, `Villa-0002/Palm`): its `MaterialProperties` string after step 2 reads `AlbedoOpt [Some [0.25 0.5 0.75 1]]`, `RoughnessOpt None`, and reopen2 also reads `RoughnessOpt None`. The source reads `RoughnessOpt [Some 0.75]`.
- **All 44 processes** (11 feasibility, 33 scored) exited 0 and logged "Selected Vulkan Device NVIDIA GeForce RTX 4090 D". The feasibility round needed no amendment.

**Metadata (observations, not defects):**
- **Propagation history:**
  - After a propagation step, the source's history contains `MaterialProperties`, and 2 history strings change: the source's and its villa's.
  - After helper steps, no history changes, and the source's history still has no `MaterialProperties`.
  - This matches the mechanism: in HP, the helper made all 32 members' values non-default while the history held no previous value. At step 2, propagation therefore kept each target's own record.
- **`Order`** (corrected at 20:39:34 UTC after the independent review, and checked by the parent): **no entity's live `Order` changed at any step.**
  - Saved group files do not contain entities' own `Order`: the group writer uses `writeEntities false true`, `WorldGroup.fs:247`. All 63 `[Order n]` tokens in a saved file sit inside the propagation-history fields of the 11 entities that have one.
  - The 46 tokens that change after a propagation step are the two history rewrites already counted above, the Villa's and the source palm's. Propagation copies the current process's clock-based `Order` values into the rewritten history.
  - The first version of this section said the probe's `order` field "did not capture" a propagation `Order` change, and that this confirmed the audit's F3. **Both statements were wrong, and they are withdrawn here.**

**How to read this:**
- Mixing routes is the risk: a scene edited with an ordinary field-level helper silently stops receiving later propagated changes for that property, and nothing warns. Using one route consistently (PP or HH) delivers both steps.
- This is engine behaviour following from whole-property merging with propagation history, a design choice, **not an upstream bug.**
- **Cause, more precisely (review F3):**
  - After the helper, each target's record is non-default, and the source's history had no previous `MaterialProperties`, so the engine kept the target's record.
  - Had the history held a previous record, the target would also have been kept, because it differs from that record. **The miss does not depend on the history lacking a value.**
- **Timing note (review F2):** propagating the palm also re-propagates the whole Villa to its 3 copies, because an ancestor with its own targets is propagated too. So P's 446–571 ms include that pass. It changed no core property and no entity set.
- **Checker note (review F4):** the independent raw-string cross-check covered after1, after2 and reopen2, not reopen1. The reviewer's own raw scoring of all 4 stages in all 16 runs gave the same counts.
- Limited to one property, one family, one scene revision, and direct world calls rather than Gaia's interface. Three replicates of a deterministic operation show it repeats; they are not a sampling estimate.

**Evidence:**
- `.artifacts/d9-history-sequence-20261111/`: `builds/`, `series/` (ledger, every snapshot and saved file, `score.json` per run, environment and GPU samples), `summary.json`.
- Committed copy: `experiments/nu-d9-history-sequence/result-receipt.json`.
