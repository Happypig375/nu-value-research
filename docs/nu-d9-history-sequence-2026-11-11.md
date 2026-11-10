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
