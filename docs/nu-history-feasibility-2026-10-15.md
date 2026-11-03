# R03 history feasibility: execution record

> **Note, 3 November 2026 (user decision):**
> - The two early **deadline failures** happened on the memory-constrained Home PC and may reflect memory pressure, not the probe.
> - The B0 verdict is data-only, and it reproduced on the Linux server on 2 November (NEEDS-HUMAN item 10).

**Observed result, 2026-10-15:** one real functional Gaia/MMCC Breakout checkpoint passed complete declared B0 model/property recovery through Gaia undo, and a fresh process reconstructed the same checkpoint. Both fresh-initial and omitted-score negative controls were rejected. Two deadline failures and one premature-snapshot instrumentation failure remain in the attempt ledger. This establishes bounded feasibility with an instrumented bridge, not ordinary agent access, B1 continuation, comparative costs or debugging benefit.

The user's 2026-10-15 instruction, “meanwhile, do constructions and experiments that you are confident in,” authorizes this local construction and experiment. It supersedes the earlier construction hold. The subsequent “parallelize your work with subagents” authorizes bounded maintainer assistance: a separate PDF audit and a source-boundary analysis support the main agent's construction and integration. These assistants are not experimental task-solving candidates or human participants. The [selected application contract](nu-history-application-contract-2026-10-11.md) owns the scientific boundary; this record owns actual execution and its limits.

## Comparison declared before execution

Use Nu `064f7ae92a8506689cd91aff5e6804a375d6ef3d`, unchanged MMCC Breakout application code, functional accompanied execution, settled Gameplay selection and a halted, reachable noninitial checkpoint. First verify supported construction and access. Then observe the complete declared B0 gameplay values and content projection after history restoration and after fresh functional initialization plus explicit reconstruction of the same checkpoint. Record actual flags and the observation phase. A cheap fresh restart is not a successful comparator. A harness-only construction is not proof of ordinary agent access.

Pass conditions are equality of the declared application values, brick keys and projected entity/HUD properties at the stated boundary, with no intervening advancing update. Negative controls must distinguish a fresh initial state and a deliberately incomplete reconstruction. B1 controlled continuation, cost distributions, debugging benefit and human effectiveness require their additional contracts; they are not inferred from B0 success. Retain failures and instrument changes, and stop an unchanged gate after five unresolved failures.

Build and runtime artifacts stay on A: under ignored `.artifacts/r03-feasibility-20261015/`. The existing `A:/Nu` checkout has unrelated local changes and is not modified. Source isolation, build, launch, observation and reconstruction are separate gates. A missing build dependency or invalid phase is recorded as a feasibility/access failure, not a failed Nu restoration.

## Attempt ledger

| Attempt | Operation | Outcome and implication |
| --- | --- | --- |
| P01 | Local Git clone with object hardlinks | Failed with `Improper link` before checkout. No source/runtime observation. Use a Git archive of the exact pin instead; the dirty source checkout remains untouched. |

| P02 | Export exact source archive and verify extracted bytes | All 3,240 files match the archive; zero mismatches. Archive SHA-256 `eb0aa77197de1971d79aa0657c2af5cf33b99ba8302a24ba44f3306cca4bf92b`. |
| B01/B02 | Build unmodified Gaia and MMCC Breakout Release | Both succeed; 212 and 210 warnings respectively, zero errors. Existing dependency warnings are retained; no package upgrade. |
| B03 | First instrumented probe build | Fails at the bridge's inferred WorldConfig/World type. Corrected explicit World annotations. |
| B04 | Rebuild with explicit Nu revision metadata | Gaia/Breakout/Nu build; probe fails for missing explicit vendored TiledSharp reference. Added vendored references to the external probe. |
| B05/B06 | Compile complete probe and checkpoint-output guard | Both succeed. The final guard build reports 122 warnings, zero errors. |
| H01 | Actual history arm, 180-second deadline | Launch reaches functional, accompanied, halted Gameplay with correct initial model/projection. No checkpoint before deadline; process tree terminated. No restoration observation. |
| B07/H02 | Add callback heartbeat; history arm with same deadline | Build succeeds. Runtime heartbeat establishes ordinary advancing Update/TimeUpdate and life loss; deadline still expires before a checkpoint. Both failed attempts are retained. |
| H03 | History arm with 600-second deadline | Reaches an eligible hit at 232 Updates/232 TimeUpdates, then the bridge rejects an advancing snapshot. Exit 1 after 133.547 seconds; no timeout and no restoration observation. The observer wrongly assumed synchronous halt. |
| B08/H04 | Build corrected deferred-halt phases; execute history arm | Build succeeds with 122 warnings/zero errors. Hit observed at Update 148, effective halted checkpoint at 149. Drift reaches 160; complete immediate and next-halted B0 checks pass without additional Update/TimeUpdate. Exit 0, no timeout. |
| F01 | Fresh process reconstructs H04 checkpoint | Fresh initialization and omitted-score controls both fail complete equality as intended; full setter and next halted boundary match complete checkpoint model/projection. Zero Update/TimeUpdate throughout. Exit 0, no timeout. |

Before H03, extend only the external process deadline to 600 seconds because H02 demonstrates progression in a slow rendered environment. The 600 actual Update reachability cap, 1,200-callback cap, first eligible checkpoint, ten-update drift and complete equality criteria remain unchanged. No state or input is fabricated to reach a checkpoint. This is feasibility instrumentation, not a timing comparison or candidate stopping rule.

Before H04, correct the observed pause-phase error: `World.setAdvancing` schedules an end-frame tasklet, after the next update work. Record the eligible-hit/request state and capture only at the next observed halted boundary. After at least ten drift Updates, request halt and wait again, retaining actual counts. Snapshot and immediate/next-boundary equality still require a halted world and zero advancing events across restore. This is an explicit protocol correction, not evidence that H03 tested restoration. The pinned routes are `WorldModule2.fs:50-58`, tasklet processing at 2034 and current-Advancing TimeUpdate gating at 2140-2148.

The verified export initially inherited the outer research repository's revision in MSBuild ProductVersion, although its source bytes were exact. Explicit `SourceRevisionId=064f7ae92a8506689cd91aff5e6804a375d6ef3d` fixes that metadata. The current Nu.dll has SHA-256 `e96cd61d188c689f7e39e2670b4d8582e26b9ea2dc95e1a15056891b7c99cd68`. Earlier build records and hashes remain preserved; the first build is not relabeled as different source.

The final bridge installer reproduces the executed Gaia text after line-ending normalization. Executed Gaia SHA-256 is `98e8c470c2795472f13a9ccf8f2c002b56be8235db40ca95c4a9fd3b07462012`; generated text is `19964b823feee68730572f031156440c4c52ded79a7336d1805d17c5516cdfc5`. Two corrected signature lines and the final newline use CRLF in the executed copy and LF in the generated copy. The initial missing-final-newline check and subsequent exact-byte mismatch are retained; no exact byte reproduction is claimed. All code is identical after that normalization. See the private `instrumentation-reproduction-final.json` receipt.

The [reviewable probe](../experiments/nu-history-b0/README.md) instruments only an isolated Gaia export. MMCC application and Nu core source are unchanged. The actual launch used .NET 10.0.10, SDL 3.5.0 and Intel OpenGL 4.6. Build warnings include the pinned Magick.NET vulnerability notices and Gaia's FSharp.Compiler.Service/FSharp.Core version constraint. Successful launch does not establish reload compatibility or dependency safety.

## Observed B0 comparison

H04's first eligible hit occurred at GameplayTime 148. The halt request took effect after one further actual Update; the retained checkpoint has GameplayTime **149**, score **100**, **29** bricks, **5** lives and **46** scene entities. These summaries locate the witness; equality compares every declared field, nested value, brick key and projected property, using float bit encodings. Serialization also passed exact represented-value round-trip equality.

After the resume request, ten additional Updates triggered another halt request. The effective halt occurred after **11** actual drift Updates, at GameplayTime 160. Gaia's real undo restored GameplayTime 149 and every declared model/projection value. The immediate and next halted observations both matched. Observer counts remained **160 Updates / 160 TimeUpdates** across restoration and the subsequent boundary. No Left/Right key-down update was observed. Mutable observer counters intentionally lie outside the B0 state.

F01 used a new Gaia process and the same application. Fresh initialization had score 0, 30 bricks and 47 entities, and was rejected. Reconstructing the target while omitting its score had the target geometry/brick set but score 0 and corresponding HUD; it too was rejected, including the score-specific target check. Applying the complete target matched the model and projection immediately and at the next halted boundary, with **zero** advancing Updates/TimeUpdates. In this run the full setter's immediate projection also matched; the protocol requires the later settled observation.

The compact [result receipt](../experiments/nu-history-b0/result-receipt.json) records all five runtime attempts, probe/trace/checkpoint hashes and observation summaries. Parent verification parsed the independent history and fresh trace files, compared their complete model/projection dictionaries and confirmed both negative differences. A negative control can agree with its own internally consistent model while differing from the target; its empty self-projection-error list is therefore not target acceptance. Full traces and checkpoint bytes remain in the ignored artifact directory.

The two successful processes took 84.906 and 24.688 seconds respectively. These totals include different work—checkpoint reachability and drift versus loading an already serialized target—so they are **not a history-versus-reconstruction cost comparison**. One checkpoint pair does not estimate reliability, scale, total effort or benefit. No framebuffer was captured; actual rendered-image equality, native trajectories, audio/input/RNG rollback and external effects are untested. B1 next needs its own controlled input/time/effect boundary and sensitivity checks. Ordinary agent transport remains separate from this internal instrumentation.

## B1 continuation follow-up

The [subsequent seeded B1 pair](nu-history-continuation-2026-10-15.md) now compares twenty resumed steps after a newly retained/undone Gaia world with fresh reconstruction of the fixed `history-04` model values. Complete models and selected projections agree, including a source-predicted wall bounce. The old `history-04` process was already closed; no old live root or native state was resumed. Audio, native contact, framebuffer, randomness/input replay, ordinary agent access and comparative costs remain outside that observation.

## Later reconstruction limitation observed in R04

An observation-only diagnostic of the
[R04 pause setup](nu-pause-runtime-feasibility-2026-10-15.md) subsequently
recorded the exact fixed B0 model while two projected brick entities retained incorrect
positions. The scene's entity-name set, brick sizes and dynamically updated
colors matched. Pinned source matches children by name and dispatcher; brick
positions use the reinitializing `==` property form, while colors use dynamic
`:=`. The observed stale positions are the first two fresh grid positions.
This supports an identity-collision explanation, although the initial keys
were not directly logged. The preceding failed run stopped at the same gate
but did not record those actual projected positions.

The earlier F01/B1 successes retain their complete observed comparisons. They
do not establish that direct `SetGameplay` generally reconstructs a fixed
checkpoint over existing same-name entities with different initialization
values. R04 and the prospective recovery-cost probe now require a common
halted, verified absent-scene boundary before first installing B0. That setup
is explicit alignment work; it does not demonstrate preservation of live
entity lifetimes or arbitrary native state. The original failures and their
unchanged projection oracles remain part of the evidence.
