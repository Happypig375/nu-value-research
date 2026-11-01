# R04 behavioral and compatibility boundary, 2026-10-26

**Decision:** prepare an authored **standalone MMCC Breakout pause task** whose
requirements concern the player's controls, retained progress, resumed play,
quit and new play. Assign the initial explicit-case or equivalent catch-all
convention; permit the successor to change application-owned representation.
There is no requirement to add `Paused`, retain a particular `Gameplay` record,
or keep the engine advancing. This resolves the scope choice left by the
[oracle eligibility audit](nu-r04-oracle-eligibility-audit-2026-10-26.md).
It does not supply a validated evaluator or an assignable benchmark prompt.

The practical decision remains whether an F# maintainer should prefer explicit
case handling for this bounded kind of agent-assisted change, considering
complete observed behavior and total work. The request is researcher-authored;
neither its frequency nor a worthwhile effect is established. A positive,
null or adverse convention result would be interpretable only within the
eventual task, model, access and resource policy. This is not a Nu-versus-Godot
comparison or a measure of human steering.

## Application and compatibility choices

Use the same pinned Nu/MMCC application in both initial conditions, rather than
MMCC versus ImSim. The selected source remains Nu
`064f7ae92a8506689cd91aff5e6804a375d6ef3d`. Prepare for ordinary **standalone,
unaccompanied, default imperative mode**, with the same fixed configuration in
both arms. This choice serves the ordinary player workflow. It differs from
the functional accompanied Gaia environment of the
[completed R04 probe](nu-pause-runtime-feasibility-2026-10-15.md); that result
does not validate this environment. Effective configuration, original behavior
and source-convention equivalence still need observation before assignment.

| Boundary owned by the authored task | Required compatibility | Permitted alternatives |
| --- | --- | --- |
| Delivery and hosting | Preserve the assigned application's declared build/launch route, engine/plugin entry points and supported dependency versions. Maintain the application rather than change Nu or the evaluator. | Reorganize application files, helpers and state within the eventual edit policy. The concrete launch command and owned edit surface must be recorded before assignment. |
| Existing player interface | Retain the existing board, assets, score/lives information, movement controls and Title/Play/Quit actions at their declared meanings. This is a pause addition, not an interface redesign. | Internal entity names, helper entities, fields, cases and control implementation may change. Required visible layout/appearance constraints must be stated to candidates; a private scene-tree equality check is not such a constraint. |
| New pause interface | A nonrepeated P key-down toggles pause during playable Gameplay; holding the key does not repeatedly toggle. Show an unambiguous paused indicator while keeping the board and progress readable. Resume uses P; existing Quit remains usable. | A separate pause flag, another state organization, local suspension or global advancement control is eligible if it satisfies the common behavior. No exact indicator text or private control address is required by this decision. |
| State continuity | Retain current gameplay progress through pause/resume and provide a fresh unpaused game after Quit followed by Play. | Storage location and record shape are not scored. This task begins from ordinary fresh launch and play; it does not import a checkpoint, perform live migration or require an old native world to survive. |

The hosting interface is a real compatibility obligation. The historical
probe's access to typed getters is an evaluator dependency, not automatically
a public product interface. Any additional externally owned API requirement
must be justified and disclosed before assignment. Do not invent one after a
candidate chooses a valid representation. The candidate also does not have to
preserve the assigned convention in its successor: analyze by **initial
assignment**, including solutions that avoid a new union case or replace the
selected match. Diagnostic exposure is a secondary observation, not eligibility.

## Required behavior and evidence

These are proposed obligations for the selected authored task. They are not
observed successes, hidden final tests or a frozen input sequence. All behavioral
requirements belong in the eventual candidate specification; withheld scoring
cases must exercise those requirements rather than introduce new ones.

| Obligation | Required finite evidence | What is not sufficient |
| --- | --- | --- |
| Reach and operate pause | Reach noninitial ordinary play, deliver the declared key action through the supported input route, observe a paused indicator within the fixed response bound, and exercise the held/repeated-key policy. | Directly publishing a dispatcher event, setting `Paused`, or a candidate's claim that it accepted the key. If a validated ordinary input is ignored, that is a response failure; inability of the evaluator to establish input delivery is different. |
| Keep progress while paused | Across the declared observation interval, retain the visible paddle/ball configuration, remaining bricks, score and lives, with the board still readable. The declared P resume action and existing Quit action must remain usable. No gameplay progression or gameplay effect may accrue and later appear on resume. | A single still image, an advancement flag, or equality with the candidate's own record. Position tolerances and observation coverage must be established independently; sampled stability is not proof about every unobserved instant. |
| Resume the interrupted play | After P, continue from the retained progress under the ordinary movement rules, with no fresh-game reset, delayed catch-up jump, repeated-toggle response, or loss or duplication of the declared externally observable score/life consequence. Exercise a declared subsequent gameplay scenario and independently check its external result, not only disappearance of the indicator. | A resumed label, a running process, or one changing image. A finite independently checked continuation is needed. It need not use the reference's `Playing` constructor, game-time field or update count. |
| Quit from steady pause | Through the existing usable Quit action, reach interactive Title within the declared bound. A subsequent ordinary Title action must work; stale pause work must not interfere with the exercised transition or new game. | A Title screenshot, selected-screen name, or a deadline measured only by a game clock that can stop. |
| Start fresh play and retain original behavior | Ordinary Play reaches an unpaused fresh game with the declared initial progress and functioning movement, scoring/life and return-to-Title behavior in the selected scenarios. | Equality to B0, the old session's private identity, or a first-frame comparison that assumes no gameplay has occurred before rendering. The evaluator must know what its observation phase permits. |
| Respect gameplay effects | No new gameplay effect attributable to forbidden paused progress; no duplicate effect on the exercised resumed event. Already caused effects may finish, and ordinary UI feedback remains allowed. | Silence inferred from screenshots or absence of a candidate log line. Audio/effect claims require an independent supported observation route and trigger/time attribution. Existing R04 enqueue-helper evidence is not native playback coverage. |

The contract concerns behavior, including its timed continuity and effects. It
does **not** require physical object-address continuity, an exact number of
private callbacks, unchanged hidden counters, or a particular subscription
structure if the required behavior is preserved. Conversely, representation
freedom does not excuse a visible reset, extra score/life event or lost motion.
Private inspection can explain a result; it must not silently expand success
criteria to match the reference implementation.

The earlier [Q2 pause/exit contract](nu-pause-exit-contract-2026-10-11.md)
also proposes next-outer-loop effectiveness, same-input-pass quit precedence,
exact phase observations and a 100-iteration transition allowance. Those
remain a separate, stronger coordination question. They are **not imported
as hidden R04 requirements**, and the new R04 task cannot claim to validate
them. R04 exercises sequential pause, resume, pause, quit and fresh-play
actions with established preconditions. Its bounded effect and retention
requirements remain; excluding a same-pass race is an explicit scope choice,
not evidence that the race is correct. Existing probes and Q2 are unchanged.

## Observation policy before an assignment

Use a monotonic host-time basis for response and watchdog deadlines; an
application game clock is not a common deadline when global halt is eligible.
Preserve chronological inputs, visible observations, applicable event evidence
and their timing/phase uncertainty. Rendering cadence alone does not identify
an engine-loop boundary. No numerical latency, sample interval, position
tolerance or watchdog is validated by this document.

Before assignment, record the concrete display/input configuration, how normal
play reaches each precondition, finite response/steady-pause/continuation
windows, independent effect observations, and treatment of stalls and dropped
observations. Calibrate those choices using independently reviewed correct
behavior and declared failures, including **at least one correct organization
that differs materially from the reference's pause case/model**. This is
maintainer preparation cost. It is not a candidate pilot, an authorization to
construct that alternative now, or proof that every possible correct program
will be observable. The current two reference clauses do not supply this check.

An evaluator may use multiple independently justified observation routes.
Screenshots or a GUI judge can assess visible criteria without depending on
private names. Structured observations may be necessary for timed effects and
progress that sparse images miss. A representation-specific mapping must be
declared, reviewed and costed under a frozen policy before candidate outcomes;
it cannot be an unrecorded repair of the final evaluator after a score appears.
If the admitted strategies cannot be measured comparably, defer allocation or
explicitly narrow the task **before** outcomes. Do not make adherence to the
reference layout an implicit shortcut.

Development access and final evaluation remain separate. Candidates may receive
declared current source, ordinary tools, compiler messages and development
observations under the [R08 policy](nu-agent-information-and-feedback-contract-2026-10-11.md).
Final test cases, reference implementations and scoring results do not enter
repair or stopping. A candidate's own completion report is not correctness
evidence. Ordinary candidate access is still unverified; this contract adds no
tool adapter, model call or transport change.

## Completion and missing observations

Keep all assigned attempts in their original source condition. For the finite
contract, report mutually exclusive dispositions:

- **Verified completion:** delivery satisfies the declared resource policy and
  every required administered criterion has independent supporting evidence.
- **Observed failure:** at least one required behavior is violated, or there is
  an independently established candidate-caused failure of a prespecified
  delivery, build, launch or candidate-resource obligation under a working
  validated administration route. Preserve which obligation failed; this is
  not a claim that all other behavior is defective.
- **Unresolved outcome:** no decisive required failure is established, but at
  least one required observation is missing or unsupported, including an
  evaluator-interface mismatch. It receives no completion credit and is not
  relabeled a demonstrated semantic failure.

Failure of the evaluator, host, input route or observation route to administer
a criterion is unresolved, not an observed candidate failure. Candidate budget
exhaustion is an observed failure only when the budget and stopping rule were
prespecified candidate obligations and the validated administration route
establishes that the candidate exhausted them; otherwise retain the appropriate
unresolved infrastructure/nonexecution reason.

Partial coverage, nonexecution, infrastructure failures and candidate budget
exhaustion retain separate reasons. A failure to reach a required state under
a working validated input/observation route is not an excuse to call that
criterion unobserved. Equally, a broken observation route is not a candidate
defect. A run with one proven violation is an observed failure even if other
criteria remain unobserved. No failure or expensive attempt is discarded.

For an assigned arm, partition all `N > 0` attempts into `P` verified
completions, `F` observed failures and `U` unresolved outcomes, so
`N = P + F + U`. The verified-completion proportion is `P/N`. The finite
assigned set's possible all-criteria completion proportion is bounded by
`[P/N, (P+U)/N]`: the lower endpoint treats all unresolved attempts as
noncompletions and the upper treats all as completions. No assigned attempt may
remain uncategorized. For explicit (`E`) minus wildcard (`W`), the corresponding
difference bounds are:

```text
lower = P_E/N_E - (P_W + U_W)/N_W
upper = (P_E + U_E)/N_E - P_W/N_W
```

These are logical missing-outcome bounds, not confidence intervals, a sampling
plan or a way to repair a biased evaluator. They apply to the same prespecified
all-assigned target with nonzero arm denominators. A useful maintenance-effect
claim still needs credible measurement, task coverage, uncertainty and cost
analysis. No attempts or outcome counts are supplied here.

## Literature reused and what changed

The completed [S226 GameDevBench reading](literature/full-reading/S226-gamedevbench.md)
supports combining game-engine assertions with visual development feedback.
Its passing-reference/failing-starter construction and selected callback-based
validator do not supply independent valid-implementation/mutant calibration,
an evaluator for every correct organization, or actual ordered native delivery.
This leads to the explicit compatibility boundary and the requirement
for a differently organized correct implementation, rather than reuse of the
fixed R04 typed oracle.

The completed [S227 v2 GUI-playtesting reading](literature/full-reading/S227-continual-gui-playtesting-v2.md)
supports separating development playtesting from final criterion judging, with
reported human-agreement validation at its stated scope. Its visually grounded
criteria do not establish hidden-state, exact phase, native audio or event-order
coverage; forced binary verdicts also leave observation failures ambiguous.
This leads to the narrower external R04 contract, separate effect/timing
requirements and an unresolved-outcome disposition. Favorable published GUI
results are retained; they are not a validated Nu observation interface.

One separate Sol High AI maintainer reviewed those existing method notes and
their relation to R04. The parent verified the decisive note sections and owns
the behavioral, compatibility and outcome decisions above. This is reuse of
completed readings, not a new full-paper reading, current artifact recheck,
reproduction or human sign-off. No new literature search or Zotero operation
was needed for this decision; the broad survey remains open.

## Next boundary and saved state

The remaining R04 dependency is now concrete: verify ordinary standalone
input/access and common observation of this contract, including the different
correct organization and effect/timing requirements, before an allocation.
A source inventory, another compiler probe, another GUI benchmark citation or
the existing fixed-reference success cannot supply that observation.
The current C: checkout remains documentation/source synthesis only; no Nu
execution environment was established in this pass.

All A: writes/execution remain stopped. R03 native-001 is terminal, R02/R10/R12
construction returns remain in force, and the two
[unfinished Daybreak-only branches](unfinished-daybreak-only-work-2026-10-25.md)
were not investigated, implemented, tested, executed or delegated. This
document resumes none of them and allocates no candidate, participant, paid
or H work. Private decision/review/acceptance records are under
`value-preparation/r04-behavioral-contract-20261026/` in the current C:
preservation root. Frozen probes and their adverse results are unchanged.

The once-only source segment `r04_behavioral_contract_20261026` records eight
reused repository-note decisions: seven credits and one historical-v1 release
provenance noncredit, with no skipped entries, missing reasons or truncation.
The report has retrieval_unlinked=false and retrieved=null. These are note
decisions at the stated coverage, not eight new papers or repeated primary
screens. The full-reading count remains 289.
