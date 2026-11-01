# R03: a concrete debugging question and its information boundary

The retained R04 reconstruction failure is useful for checking what a history
workflow would need to expose. It is **not yet an eligible unknown-cause repair
task**: the original fresh scene's names were not recorded, no corresponding
pre-installation history root is retained for this attempt, and ordinary agent
access has not been demonstrated. A further source finding changes the proposed
workflow: Gaia's Interactive evaluation snapshots even a getter expression and
clears redo history. Inspection through that route must be counted as a history
operation.

This is a retained-evidence and pinned-source check, following the completed
[S310 reading](literature/full-reading/S310-java-whyline-diagnosis.md). It adds
no native run, candidate, participant, full-paper reading or favorable repair
result. R02 input and R10 migration remain stopped.

## Selected symptom and what was actually observed

The [R04 execution record](nu-pause-runtime-feasibility-2026-10-15.md#reconstruction-limitation)
preserves the initial failed projection check and its separate observation-only
rerun. In that rerun, after installing the unchanged time-149 B0 model into a
fresh populated scene, the halted world had zero Gameplay Update/TimeUpdate
events and these values:

| Brick | Model position | Entity position | Other recorded agreement |
| --- | --- | --- | --- |
| `@477` | `(128,128,0)` | `(-128,64,0)` | Exact size and color |
| `@478` | `(128,144,0)` | `(-128,80,0)` | Exact size and color |

The two position errors are the complete reported projection-error list at
this boundary. This is a property observation, not a recorded screenshot of
the rendered framebuffer. The initial failure lacked that detail; the rerun's
extra observation was constructed by the research maintainer.

The practical question is: **after restoring saved gameplay values, why do
these two entity positions disagree, and what reconstruction procedure makes
the complete declared state agree?** The immediate beneficiary is someone
returning a scene to a saved debugging state. This episode arose in our
research setup, rather than an independently sampled developer report. Its
frequency and avoided real-world work are unknown.

The pinned application assigns brick position with the reinitialization
operator and color dynamically in [Gameplay.fs](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Projects/Breakout%20Mmcc/Gameplay.fs#L274).
[Content reconciliation](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/World/WorldContent.fs#L137)
distinguishes initialization/reinitialization from dynamic assignment, and
matches existing children by key and dispatcher. This is consistent with the
recorded mixed old-position/new-color outcome. It does not establish that a
generated-name collision actually occurred: the necessary original name/value
correspondence was not logged.

## Question, evidence and ordinary tool

| Question | Evidence needed and available here | Existing route and remaining inference |
| --- | --- | --- |
| Which values disagree now? | Saved B0, current model and current entity properties. The diagnostic rerun supplies these numerically. | Gaia has screen/entity property panels and an Interactive expression window. Complete display of these specific values and ordinary agent control remain unexercised; the diagnostic JSON is extra research observation, not evidence of that access. |
| Did installing B0 reuse these particular earlier entities? | Both the original fresh tree and the post-installation tree, with names, dispatchers and positions at the actual boundaries. The original tree is missing. | A previously captured appropriate world root could expose represented predecessor values through undo and inspection. The Timeline's operation labels do not reconstruct an absent root or a per-property causal trace. The B0 symbol from another run is not this predecessor. |
| Why can position remain while color changes? | The application property declarations and actual content-matching/update policy. These pinned source bodies are available. | Ordinary source search/inspection supplies a mechanism explanation. A solver still has to connect that policy to the particular predecessor evidence; giving the exact explanation in the prompt would supply part of the diagnosis. |
| Does a correction work? | Complete model/projection checks after the declared reconstruction and continuation. | The common clear-then-install amendment passed the later declared R04 checks. That establishes the maintainer's setup correction at its scope, not an independently executed repair by a candidate or an estimate of diagnosis time. |
| Can history avoid rebuilding the debugging state? | A usable retained root from the actual workflow, a matched fresh reconstruction, verified inspection access and all acquisition/retention/recovery work. | B0/B1 and R06 establish narrower restoration and component-cost observations. This failed fresh-process attempt supplies no matched history workflow or total-work comparison. |

The public [property panels](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L2936)
and [Interactive window](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L3242)
are source-supported interfaces. Their existence does not imply an external
command inbox. Interactive input is written **from** the UI to its source file
before FSI evaluation; the inspected path does not watch that file for agent
commands. Event tracing is separately enabled and filtered; no event log or
output-to-source dependency history for this failed attempt was recovered.

## Inspection changes the history when Interactive is used

[Interactive evaluation](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L3256)
calls `snapshot` before initializing/evaluating the expression. The
[snapshot implementation](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L505)
pushes the current world state onto `Pasts` and clears `Futures`. It does not
first decide whether the expression mutates gameplay. Even a getter such as
`world.Halted` follows this path. The [Timeline](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L2912)
prints snapshot labels; it does not supply a value-difference or dependency
query interface.

For a halted functional world, consider a current state F with an older
checkpoint K. A getter evaluation at F adds another F entry. The next undo
therefore restores that pre-evaluation F entry before an older checkpoint
can be reached. After undoing to K, another Interactive evaluation clears the
then-retained redo branch. This is a source-derived consequence, **not a newly
executed GUI observation**. Arbitrary expressions and advancing worlds have
additional effects outside this example.

A later comparison must specify how inspection is performed and record actual
history operations and branch loss. Property-panel reading is a candidate
alternative with a different access/coverage question; do not infer that all
inspection APIs have this side effect. Adding a query adapter that bypasses
the UI would be a new tool treatment with construction/access costs. It cannot
be hidden in the final observer or presented as an already available ordinary
agent workflow.

## Decision and executable next work

Retain this episode as an **observed reconstruction/access counterexample**,
not a clean unknown-cause task with a confirmed collision ground truth. Do not
score that inferred cause as the only correct diagnosis or count the successful
clear-then-install procedure as an independent task-solving result. Correct
alternatives meeting the model/projection/continuation contract remain valid.

For a later history-assisted repair comparison, select a consequential case
with the actual symptom, needed predecessor information and permitted tool
route available before assignment. If this mechanism is used to construct a
new deterministic name-reuse case, freeze its names, predecessor evidence,
information policy and behavioral oracle prospectively and label it authored;
it would not repair the missing evidence in the original run. Separate state
reach, fault localization, proposed correction, executed repair and continuation.
Candidate allocation remains zero.

The immediate technical access question is whether the chosen ordinary
inspection route can expose the required model/entity values while preserving
the intended branch and halt boundary. Do not repeat a B0 switch merely to
claim that this workflow question is resolved. Independently, the public R12
propagation route can now be exercised under its own bounded protocol without
resuming either stopped construction gate.

## Evidence identity

The original archive was rechecked at SHA-256
`eb0aa77197de1971d79aa0657c2af5cf33b99ba8302a24ba44f3306cca4bf92b`.
Selected original Gaia, WorldContent, Gameplay and WorldEntity files were read
directly from it; instrumented Gaia was not substituted. The retained R04
diagnostic trace SHA-256 is
`e900414dd1360bc61b28cbb2ca8f44e657ecbf4cbba6af29d62f08a9feaa1915`,
and process receipt SHA-256 is
`40cccce6e84c375041fc7e26857a289a0b1ab4fff667994c24b85c0da4e0dfa1`.
Both match the [published R04 receipt](../experiments/nu-r04-pause-runtime/result-receipt.json).
The read-only extraction/check script, exact source identities and decoded
observations are private under `.artifacts/r03-question-access-20261018/`.
No new source retrieval or unchanged Scite screening is credited.

## 2026-10-23 ordinary inspection and history lineage

The [development-history audit](nu-development-history-audit-2026-10-23.md#r03-ordinary-inspection-can-preserve-the-history-branch)
now checks the pinned property panel directly. It reads a selected entity's
property and invokes the snapshotting setter only when the widget reports a
promotion or edit. Plain hierarchy selection likewise has no snapshot in the
inspected path. Passive inspection of a halted functional world is therefore
source-supported as an ordinary alternative to Interactive evaluation.
Position remains an editable widget; accidental editing, displayed precision,
runtime branch preservation and ordinary agent transport are not validated.

The #629 report and contemporaneous same-topic snapshot corrections, #592
selection repair and #639 Interactive introduction clarify this distinction.
An exact #629 issue-to-commit link remains unestablished. They are maintainer
accounts and source lineage, not independent demand or a new native result.
The Timeline still exposes labels, and the original episode's missing
predecessor/root remains missing.

If this route is selected for later feasibility, bind a real two-root halted
state and verify property reading, selection, undo/redo and no-edit controls
before assigning a debugging task. Treat Interactive getter evaluation as a
separate history-affecting control. The [Redux reference](nu-status-quo-and-transfer-audit-2026-10-23.md#redux-changed-code-replay-and-ordinary-inspection)
similarly separates monitor selection from history changes while retaining
subscriber/effect limits. Allow each workflow its ordinary sufficient route;
a forced query adapter or arbitrary expression would change the comparison.

## 2026-10-23 predecessor audit and passive-access preparation

A further audit of twenty exact retained files/ranges confirms that the
inspected evidence cannot supply this episode's same-process predecessor.
The first failed trace contains no model/projection roster. The diagnostic
calls `SetGameplay` before its first state capture, so its `@450`–`@478`
roster describes the installed state. A separate R03 `history-04` run records
fresh names `@449`–`@478`, but uses another process and application binary;
its last two positions already match B0. Those observations cannot substitute
for the missing R04 predecessor. The collision explanation remains an
inference, and another known-good run cannot make it diagnosis ground truth.

If an authored version is selected, capture the actual halted pre-install and
post-install roots in one process, including complete addresses, dispatchers,
positions and relevant dynamic properties. Bind the B0 input, application and
observation phase before the operation. Deliberate name reuse would be a new
authored fact, not recovery of the old run's missing evidence.

The ordinary-access proposal now has a minimal four-boundary sequence. Bind
functional Gaia, immediate past K and current F, both halted, no future at F,
and an unmounted entity E at the same full address/group in both roots. Give
E distinct, exactly displayable positions at K and F. A mounted entity exposes
`PositionLocal` and is a different case. The source basis is the pinned
[selection and undo/redo code](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L579-L667)
and [property enumeration](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L2131-L2164).

| Boundary | Ordinary action and required observation |
| --- | --- |
| C0 | At F before selection, record the halt indicator, selected screen/group, E's full hierarchy path and visible Timeline. |
| C1 | Select E through the hierarchy and passively view its position; Timeline must remain unchanged. |
| C2 | Use Game > Undo once; record K's position and the expected future. Reselect E only if selection reconciliation clears it, counting that action and checking history again. |
| C3 | Use Game > Redo once; record F's restored position, consumed future, unchanged halt state and Timeline matching C1. |

Keep pointers/focus outside editable properties during observations. Runtime
IDs are recorded; address identity defines E across roots. An accidental edit,
unreadable position or observed branch loss is retained as adverse access
evidence when the fixture and observations are intact. Wrong mode/root,
Interactive evaluation, undeclared advance/step/edit actions or missing
captures do not establish passive branch preservation. Gaia's outer exception
handler can itself undo and clear futures, so exception-caused branch loss
must not be attributed to passive display.

This prepares one ordinary-access check; no UI or native process was run and
no package is yet accepted for it. Even a pass would establish only the
declared position/history observations in this authored case, not complete
world equivalence, diagnosis benefit or ordinary agent transport. The private
episode and access notes are under
`A:/nu-value-execution/20261023-material-intent/value-preparation/`, with
SHA-256 `9961625053c53248624011bf11b7098fc1fc81be085434196246ce8a27d2113b`
and `378056531584e7ef9f003a7b341a2e46b97560a2d2263b0e8bc2ffb3ff9469b1`.

## 2026-10-23 recovery demand and the next comparison

The complete body and linked history of [Nu #151](https://github.com/bryanedds/Nu/issues/151)
now supply a concrete recovery rationale: undo after a user-code exception may
preserve the editing session. This promotes an earlier title-only lead. It is
maintainer demand for recovery, not independent adopter evidence or diagnosis
ground truth for the stale-position episode above.

The February 2017 lineage is explicit. [53a50bf](https://github.com/bryanedds/Nu/commit/53a50bfacb7d5ec8c90267ba404b726e38a6a017)
introduces exception recovery; its child
[59c83bd](https://github.com/bryanedds/Nu/commit/59c83bdc9902dcdfcc9e0ff97583c43f082d824e)
changes initialization; the next child
[a4a3de4](https://github.com/bryanedds/Nu/commit/a4a3de4e339fcee9f1bb5858281e0b68e484286c)
corrects recovery and deliberately inserts a division-by-zero after Blaze
Vector bullet creation. [c4f76ed](https://github.com/bryanedds/Nu/commit/c4f76ed33b8eb61b034bae734fd66fee9f9419c5)
removes that test fault and closes the issue. The insertion/removal documents
a maintainer-authored trigger; it is not a retained runtime result. The
functional-only undo and exception-rewind routes survive at the research pin.

A later recovery comparison can ask whether retaining the prior world makes
a failed editing session recoverable with less work than an ordinary saved-state
reconstruction. It must capture actual named roots in one process, specify the
exception and recovery route, and verify a declared continuation. Merely
catching and halting the exception is a rival explanation. Give the comparator
the same saved project, trigger, logs and sufficient ordinary tools. Neither
the historical patches nor the existing B0/B1 observations supply this complete
comparison; no crash fixture is executed by this source audit.

### Methods that change the design

Existing complete readings already constrain that comparison:

- [S42](literature/full-reading/S42-stream-debugger-comparison.md) finds that
  supplying the relevant object changes which debugging package is faster.
  Freeze fault-location information and permitted access before assignment.
- [S66](literature/full-reading/S66-omniscient-debugging-behavior.md) observes
  fewer reruns with Replay without greater diagnosis success. Rerun counts and
  restoration alone cannot be the repair endpoint.
- [S310](literature/full-reading/S310-java-whyline-diagnosis.md) evaluates a
  causal output-to-source question interface and diagnosis recommendations,
  with no code edits. Its positive results cannot be attributed to bare history
  retention or transferred to completed Nu repairs.
- [S43](literature/full-reading/S43-reactive-debugging.md) and
  [S49](literature/full-reading/S49-rxfiddle.md) make supervision, answer checking,
  attrition and success-only timing consequential. Preserve every assigned
  outcome and verify delivered behavior independently.

These are reused readings, not new paper-reading credit. The immediate gap is
an eligible task and ordinary access, rather than another generic debugging
literature inventory. A new causal-query interface would be another
intervention with its own construction and use costs.

### Common outcome and work boundary

A practical repair must deliver the required model, logical identities and
selected projection, pass its declared continuation, and retain any required
halt/branch behavior. Distinguish reaching the symptom, localizing a cause,
proposing a repair, applying it and verifying it. Correct alternative repairs
remain valid. An authored feasibility case cannot establish practical frequency.

Keep assignment-to-delivery elapsed time, machine/facility components, AI/tool
work and active human work separate. Include route setup, capture/retention,
navigation, reconstruction, failures and verification; leave unobserved work
unknown. Do not sum overlapping intervals or amortize preparation over
hypothetical future tasks.

The [R06 measurements](nu-recovery-cost-feasibility-2026-10-15.md#comparison-and-interpretation)
remain local component observations. History retains a broader World than the
reconstruction arm's Gameplay value, while clear/install alignment and much
integration work sit outside the timers. Reuse the observation definitions,
not those milliseconds as a price for repair. For a common verified outcome,
ordinary-workflow dominance after counted preparation and failures would defeat
a history-benefit claim for that task; mixed costs establish a trade-off until
the practical decision supplies a defensible valuation.

Private evidence is under `value-preparation/history-demand-next/`,
`r03-methods-next/` and `history-work-next/` in the current A: execution root.
The source manifest is SHA-256
`db114a9109aa4b7ca326de3672a4a74728aa8a73b58f59e4063ae5671259fbba`;
the methods and cost notes are respectively
`b7a640bc5c4e21ce68983cbebdefd2a658b8becc1766c690bc9a32f3d7d7dfb8`
and `e16922457be37fa41e68dfca9c5c41abe733885c0d84ac31d070d1bbd3401ddf`.
This preparation allocates no participant or experimental candidate runs and
does not reopen R02, R10 or the returned R12 construction.

## 2026-10-23 native passive-access disposition

The [one native observation](nu-passive-access-observation-2026-10-23.md)
followed accepted copied-package configuration and a fresh exact manifest.
Ordinary hierarchy selection exposed LeftWall and its displayed Position K.
The sole submitted drag left K unchanged with no new history entry; the later
capture was byte-identical. No distinct F was established, so C0-C3 and
Undo/Redo were not attempted. This is a fixture setup failure, not evidence
that passive observation destroys an established branch or that Undo/Redo is
defective. The unexpected new `gaia/imgui.ini` separately fails the frozen
output boundary.

Independent review and parent disposition retain the complete attempt and
its narrower property-access evidence. The assignment is consumed. Do not
reset the package, retune the gesture or repeat the process. Source-only
inspection may clarify the interaction/output paths before a distinct future
question; it cannot supply missing observations retroactively. The practical
recovery comparison above remains unresolved, including actual named roots,
ordinary access, verified continuation and complete work. R02/R10/R12 remain
returned, and the [current prompt](continuation-prompt-2026-10-23.md) owns the
next handoff.

## 2026-10-25: specify useful recovery before a repair comparison

The [reviewed recovery-target analysis](nu-recovery-target-and-serialization-2026-10-25.md)
now distinguishes last editor snapshot K, last good simulation state G and
handler-entry F. Ordinary Gaia already supplies recovery and explicit F7
restore points. A new benefit claim must improve on that workflow and count
lost progress and complete work. Outer exception recovery discards redo F;
dialog Hard Rewind differs. Soft Rewind's later-entry root is a source
prediction requiring a reachable state-changing exception, not a runtime bug
result. Group serialization omits Screen.Model; screen-file replacement is a
stronger unverified comparator with lifecycle/content/transaction obligations.
Recovery, diagnosis, code repair and verified continuation remain separate.

This integrates the completed static review and its correction, including
existing-address ScreenState replacement. It supplies no new actual roots or
native observation and does not reopen native-001 or R02/R10/R12. A later
source candidate remains private and unaccepted. Both that deliberate
fault-trigger branch and the later ordinary screen serializer/runtime
persistence branch are now **unfinished, Daybreak-only work** under the
[user's restriction](unfinished-daybreak-only-work-2026-10-25.md). Non-Daybreak
ChatGPT models must not continue or delegate them. The
[ordinary checkpoint-persistence brief](nu-recovery-target-and-serialization-2026-10-25.md#current-preparation-ordinary-checkpoint-persistence)
preserves outstanding scope and destination/selection/content dependencies;
it is not a current assignment for an ineligible model. Separate literature
and synthesis remain authorized.
