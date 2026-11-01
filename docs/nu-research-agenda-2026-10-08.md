# Prioritized agenda for investigating Nu value

**Assignment, 2026-10-08:** prepare the plausible research directions together, prioritize them by research value, and continue literature work when it can change a question, comparison or interpretation. This replaces the immediate requirement to choose only one direction before further preparation. It does not select a favorable answer or reopen experimental execution.

The central question is **how to improve the correctness and total work of evolving stateful interactive software, starting from Nu's representations, coordination, history and development tools**. The intended result is an evaluated improvement with useful conditions of benefit and explicit costs, including conditions where a credible alternative works better. Whole-package value, the MMCC/ImSim choice and a source convention such as D1 answer different questions. They belong in one agenda with separate comparisons.

This agenda covers **21 currently plausible directions**, including less mature extensions and the user-added R21 steering question. It is a revisable map, not a claim that every possible idea has been enumerated or a commitment to run 21 studies. [PLAN](../PLAN.md) owns authority. The [B01–B12 survey](literature/nu-background-survey-2026-09-30.md), [reading index](literature/full-reading/INDEX.md) and [search ledger](literature/nu-background-searches-2026-09-30.md) retain source coverage and gaps.

**Implemented continuation:** the [saved plan](nu-research-continuation-plan-2026-10-08.md) and [six detailed designs](nu-research-study-designs-2026-10-08.md) prioritize **mechanisms/costs plus bounded agent maintenance**. Human-steered development is the intended practical context; its anticipated 2027 importance is a planning assumption, not a measured forecast. Steering effectiveness is deferred pending measurement and participant-design work. Human-only and agent-only extremes remain optional reference cases; the near-term packet does not require three equal workflow arms. Source-grounded task diversity and counterexamples address the user's convergence concern without claiming that prompts or repeated AI outputs establish independent thinking.

**Current evidence and authority, 2026-10-15:** the user has authorized confident local construction and experiments, as recorded in [PLAN](../PLAN.md). The [current readiness table](#readiness-and-next-actions-for-all-directions) below now incorporates the completed bounded probes and owns the next actions. It supersedes earlier held/unverified wording in the direction cards for the linked executed cases and completed selected readings; exact residual edition/artifact gaps remain in the reading index. Those cards preserve the comparisons and their design rationale. Mechanism feasibility does not establish agent maintenance, human productivity or net adoption value; the priority ranking remains unchanged. Candidate/model experiments, recruitment, new accounts, OAuth staging and H execution remain unallocated.

## 2026-10-19 objective: improve evolution of stateful software

The user's refinement changes the intended endpoint: develop and evaluate a
useful improvement over a credible existing workflow for evolving stateful
interactive software. Nu supplies concrete mechanisms, artifacts and hypotheses.
The eventual contribution may improve Nu, another implementation, or a portable
method. Demonstrating features and documenting tradeoffs are foundations; the
research programme should pursue a better capability, more reliable completed
change, or lower total work under stated constraints.

A positive effect is an objective to test, never an acceptance rule for data.
Retain failed interventions, nulls, adverse findings and cases where an ordinary
alternative wins. If a proposed improvement fails, use the result to revise or
redirect the design without rewriting its original requirement or outcome.
Novelty and useful effect need separate evidence; neither follows from a Nu
implementation or from using a different application domain.

### Establish the status quo for the decision

There is no single status quo across all 21 directions. Identify the beneficiary,
practical change, existing tools and relevant costs before selecting a comparator.

| Comparison level | Candidate status quo | Evidence needed before selection |
| --- | --- | --- |
| Game-development workflow | Relevant Unity, Unreal, Godot or existing project workflow | Match the target task, assets, deployment needs, ordinary tools and allowed assistance. Credit idiomatic solutions and shipped facilities. These engines are candidates, not an established ranking or a requirement to build three ports. |
| Mechanism within a workflow | A credible batch/helper, reconstruction, replay, undo or explicit migration policy | Require the same intended outcomes and count construction, integration, verification, failure and repair. Select the relevant ordinary alternative; do not manufacture a weaker baseline by removing useful tooling. |
| Improved intervention | The supported existing workflow plus the proposed change, with a credible alternative where needed | Separate the contribution of the intervention from language, engine, tooling and familiarity differences. Use an ablation when necessary for a component claim; a package comparison estimates the package. |
| Transfer beyond games | An ordinary implementation of the selected non-game stateful task | Verify its actual state, event, identity, scheduling and effect contracts. A framework name or the observation that games have states does not establish an equivalent baseline. |

The [existing Godot audit](nu-comparator-and-convention-audit-2026-10-11.md)
provides inspected facilities at its recorded pin, not universal status-quo
selection. Unity/Unreal or non-game alternatives require their own relevant
primary-source/tooling investigation when the task makes them consequential.

### Use development history as supplementary evidence

Extend the [practice and task record](nu-practice-and-task-provenance-2026-10-11.md)
with linked issues, discussions, pull requests, parent/child commits, tests and
release history. Trace the actual need and beneficiary, proposed alternatives,
implementation decision, later repairs or reversals, and the behavior present
at the research pin. A commit message or closed issue alone establishes neither
successful behavior nor saved work. Maintainer rationale remains distinct from
independent adopter demand. Preserve withdrawn reports and adverse designs.

For a historical change, bind the relevant predecessor and successor before
calling it a reconstructed task. If its workaround is already present, label
the research task as an adaptation rather than replaying a supposed current
defect. Keep any reference solution or fixing patch outside experimental
candidate information when the later protocol requires that separation.

### Generalize a mechanism through tested contracts

The broader candidate problem is changing state representations, transitions
or configuration while preserving intended ongoing behavior at acceptable cost.
Possible transfer settings include a stateful UI, workflow tool or simulation;
none is selected or claimed equivalent yet. Map the state, identities, queued
work, scheduling and external effects explicitly. An abstract state machine can
omit precisely the integration costs and irreversible effects that matter.

First explain a mechanism and its conditions in the Nu case. Then formulate a
portable intervention or prediction and test it on a consequential non-game
case with its ordinary comparator. Report which assumptions transfer and which
require application-specific work. A renamed game fixture or a second cosmetic
variant is not evidence of generality.

### Next consequential preparation

1. Trace the issue/commit lineage behind one practical need among the current
   R12 revision and R03/R10 recovery/evolution cases, including contrary accounts
   and the state of the feature at the pin. Prioritize a gap that can change
   the task or intervention, not another description of an understood branch.
2. Select the beneficiary's decision and credible baseline; use literature to
   specify correctness, total work, meaningful improvement and rival explanations.
3. Design the proposed improvement and its falsifiers. Existing mechanisms,
   an adaptation, a hybrid workflow or a new method are eligible; none is presumed
   better. Preserve ordinary tool access and all assigned work in the comparison.
4. Select a non-game transfer case only when the proposed mechanism has a
   clear portable contract worth testing. Continue literature and development
   history where they can change these choices.

This refinement retains the 21 direction IDs and their evidence. It adds no
candidate/model or participant allocation, new account or purchase. Confident
local work retains PLAN's existing authority and prospective checks; the R02
input and R10 migration returns remain stopped. Human steering stays a future
measurement question. No new search, source-lineage reconstruction, baseline
validation or experiment is claimed by this planning update.

## 2026-10-23 evidence-led continuation

The [development-history audit](nu-development-history-audit-2026-10-23.md)
resolves the selected R12/R03/R10 source questions. Nu's whole-property
override is a documented abstraction; the specific record-field requirement
remains authored. Historical repairs already present at the pin are not new
unfixed tasks. Ordinary property inspection has a source-supported path that
avoids Interactive's snapshot, while actual UI/access still needs validation.
Live-model evolution is an intended use, but the reward-200 mapping is not a
public initializer guarantee.

The [ordinary-workflow audit](nu-status-quo-and-transfer-audit-2026-10-23.md)
changes the comparison. Unity and Unreal already express selective material
inheritance; Godot supports both a shared-plus-unique workflow and a shared
shader with per-instance values. Known merge literature supplies relevant
methods. The [material-intent follow-up](nu-material-intent-baseline-2026-10-23.md)
finds that the proposed mode table and field update are themselves a credible
ordinary helper. Its [pure reference component](../experiments/nu-r12-material-intent/RESULTS.md)
now passes the declared explicit-intent, immediate-release and JSON-pairing
controls; supplied material maps have not undergone native serialization. A later Nu
integration must improve capability or complete work beyond it; a baseline
denied the same helper or intent information is invalid. Charge representation,
metadata, verification, failed work and conversion. Actual Nu continuation is a
separate acceptance gate. This does not rank R12 above every Band A question
or establish a new algorithm.

Redux and XState supply two concrete non-game mechanism references, with
different reconstruction/effect boundaries. Ordinary XState snapshot
transformation must be credited before testing any additional migration
checks; event sourcing is an alternative when usable history exists. The
proposed ticket/approval scenarios remain authored shapes. The
[Showtime follow-up](nu-xstate-practice-case-2026-10-23.md) now binds a real
partial-record persistence change and self-reported relaunch failure; it
leaves machine-change causality and useful cross-version preservation intent
unresolved. These are preparation results,
not transfer experiments or reopened R10 construction. Human steering remains
future work; all 21 direction IDs and the existing allocations/returns remain.

### Preparation priority after the material construction return

The [material construction return](nu-material-intent-baseline-2026-10-23.md#native-construction-return-at-gate-008)
stops the native helper at five failures; no native sequence ran. Ordinary
continuation does not reopen it. Prioritize the following independent
comparisons for preparation. This orders current research value and readiness,
not predicted effect sizes, and does not change the 21 direction IDs or
candidate/participant allocation.

| Preparation order | Practical decision and credible alternative | Consequential next dependency and falsifier |
| --- | --- | --- |
| 1: R03 with R06 | Whether a recovery procedure preserves required editing-session work and supports verified continuation more reliably or with less total work than ordinary Gaia recovery/F7 checkpoints or an eligible reconstruction route. Diagnosis and code repair are separate possible endpoints. | Name the actual exception boundary and required K/G/F target before construction. Establish caller-visible state changes, ordinary access and common outcome; count capture, retention, integration, failures and verification. If ordinary recovery meets that outcome with equal or less complete work, an added mechanism has no demonstrated advantage on that task. |
| 2: R04 | Whether explicit current-case enumeration earns its warning/edit burden relative to a valid exhaustive catch-all with the same ordinary compiler, context and tests. | Bind a practical successor requirement and ordinary information policy. Later all-assigned completion and work, not another compiler probe, must discriminate the conventions. Equal/better catch-all completion, ignored warnings or mechanically compiling but wrong repairs narrow the claim to diagnostic availability. Candidate execution remains unallocated. |
| 3: conditional R01 informed by R12 | Whether a developer should adopt or retain Nu's selective-material workflow over the ordinary workflow in that developer's actual engine/project. | Bind a beneficiary, consequential workflow choice and incremental revision history before selecting one comparator. Count setup, asset/selection/helper work, editing, repair and verification. An ordinary engine providing the same saved/rendered result with equal or less complete work defeats the proposed advantage. Do not build three ports merely because three engines were surveyed. |

The [history access record](nu-history-question-access-2026-10-18.md#2026-10-23-ordinary-inspection-and-history-lineage)
supports the passive route at source level; the retained stale-position episode
still lacks its original predecessor names and is not confirmed diagnosis
ground truth. The [cost series](nu-recovery-cost-feasibility-2026-10-15.md#comparison-and-interpretation)
has mixed readiness results and unequal payload scopes. These make complete
repair work consequential without supplying a benefit estimate. R04 already
has [compiler evidence](nu-application-diagnostic-feasibility-2026-10-15.md)
and a [bounded behavioral oracle](nu-pause-runtime-feasibility-2026-10-15.md);
repeat demonstrations would not resolve task/solver validity.

R01 retains the greatest direct adoption potential and the largest unresolved
workload burden. The [ordinary engine alternatives](nu-status-quo-and-transfer-audit-2026-10-23.md#a-credible-status-quo-for-the-material-task)
must receive their sufficient native facilities. Further baseline repetitions
or mode-table variants are not the next research contribution. The
[Showtime/Harny cases](nu-xstate-practice-case-2026-10-23.md) do not establish a
cross-version preservation obligation, so they do not yet select a non-game
migration experiment. R02/R10/R12 returns remain in force. New consequential
primary evidence can change this order; no broad-survey completion is implied.

The completed parallel follow-up sharpens these priorities. The
[R03 passive-access attempt](nu-passive-access-observation-2026-10-23.md)
completed accepted package preparation and one native launch. Its single
submitted drag left the required second state absent; no C0-C3 or Undo/Redo
observation followed. An unexpected Gaia imgui file separately failed the
frozen output boundary. Ordinary property selection/viewing has partial
evidence, while access around an actual history branch remains unresolved.
The assignment is consumed; source-only clarification may inform a distinct
future question, not a retry or retrospective protocol change. Nu
[#151's recovery lineage](nu-history-question-access-2026-10-18.md#2026-10-23-recovery-demand-and-the-next-comparison)
supplies a concrete maintainer rationale, but no eligible actual-root repair
trial or independent adopter evidence. [S311](literature/full-reading/S311-partial-trace-dependency-estimation.md)
adds a useful adverse boundary: inferred dependencies may aid localization
but cannot replace missing actual predecessor evidence.
[S312 ADI](literature/full-reading/S312-adi-agent-repair.md) now supplies reported
agent-repair comparisons under common benchmark/model/budget conditions.
Deposited prompts differ materially; interface, prompt/workflow and rerun
changes form a bundle. Its traces come from re-execution, so the favorable
reported counts do not resolve this attempt's missing fixture evidence.

The [recovery-target analysis](nu-recovery-target-and-serialization-2026-10-25.md)
now separates editing-session recovery from diagnosis/repair and distinguishes
last editor snapshot K, last good simulation G and handler-entry F. Gaia's
ordinary history/F7 facility is part of the status quo. Group files omit the
screen model; screen-file replacement is a stronger unverified comparator.
The subsequent deliberate fault-trigger branch and ordinary screen
serializer/runtime persistence branch are both **unfinished, Daybreak-only
work** under the [latest user restriction](unfinished-daybreak-only-work-2026-10-25.md).
Their private candidates remain unaccepted. Non-Daybreak ChatGPT models must
not continue or delegate either branch. Ordinary persistence scope and
destination/selection/content policy remain future dependencies for an eligible
model; they are not demonstrated baseline capabilities. Separate literature
and synthesis remain authorized, without changing the scientific ranking.
The [UI/output source follow-up](nu-passive-access-source-followup-2026-10-25.md)
clarifies focus versus edit and conditional ini saving while preserving the
failed attempt and its unobserved gesture/writer.

The [authentic R04 API rename](nu-practice-and-task-provenance-2026-10-11.md#2026-10-23-a-real-api-rename-and-a-qualified-lifetime-case)
is a source-maintenance burden case where a valid catch-all can avoid a named
consumer edit **if the local case rename is required**; engine-event adaptation
alone may retain the local name. It adds no new gameplay requirement. Preserve it as a boundary
case rather than recasting it as a favorable semantic diagnostic task. The
qualified R05 event-lifetime report remains a source hypothesis requiring
actual roots, disposal and live-contact evidence.

The [October 26 R04 history audit](nu-r04-history-task-audit-2026-10-26.md)
and [oracle eligibility audit](nu-r04-oracle-eligibility-audit-2026-10-26.md)
now select an explicitly authored behavioral question for current preparation.
The completed pause references validate their clause contrast under shared
case/model/control/schedule choices. A future maintenance evaluator must also
admit the correct organizations promised by D1, including a successor that
meets the task without a union extension when no public contract requires one.
That evaluator/access dependency, task coverage and allocation remain; another
compiler demonstration or equal weighting of invented cases cannot resolve them.

For non-game transfer, [Camunda](nu-workflow-migration-transfer-2026-10-23.md)
now supplies explicit running-instance preservation demand. When running
instances must change, its supported manual migration/validation is the
ordinary baseline; old-version completion is valid only when that policy
meets the requirement. A novel, useful improvement beyond existing facilities
is still to be specified. This strengthens task selection without raising
transfer above the immediate R03/R06 access dependency or reopening R10.

## How the priorities are chosen

Priority is an ordinal research judgment, not an estimated effect size or a computed score. It considers:

- **Decision value:** who could make a consequential development, tooling or adoption decision from the answer?
- **Mechanism grounding and transfer:** does an inspected Nu capability or credible alternative motivate the intervention, what new capability needs validation, and which assumptions could transfer beyond the initial application?
- **Unresolved knowledge:** what would be learned beyond the closest existing method or comparison? A Nu port or a low publication count alone is insufficient.
- **Discrimination:** can credible alternatives, meaningful outcomes and rival explanations be distinguished? Useful nulls, adverse findings and crossovers count as valuable answers.
- **Evidence cost and transfer:** what preparation, source access, participants, engineering and replication would be needed, and how narrowly would the answer apply?

Research value and order of execution are different. R01 has the greatest direct adoption value but depends on a defensible workload and measurement boundary. R02/R03 may offer a smaller first comparison after separately authorized feasibility. R05/R06 and R14 supply measurement and practice foundations early, even when their standalone contribution is less distinctive. Order within a band is provisional; a missing comparator, a close duplicate or a real stakeholder decision can change it.

## Ranked directions

| Rank / ID | Priority | Question | Decision or knowledge gained |
| --- | --- | --- | --- |
| 1 / R01 | A | Does the complete Nu development workflow provide net value against a credible alternative? | Whether and for which work a developer should adopt the package. |
| 2 / R02 | A | How do ownership and coordination choices affect local versus coordinated changes? | When to choose MMCC, ImSim or another justified organization within Nu. |
| 3 / R03 | A | When do retained history and state inspection improve debugging and recovery? | Which failure situations justify the tooling and retention cost. |
| 4 / R04 | A | Do explicit domain representations help complete evolving behavior? | When type/domain modeling or explicit-case conventions repay their cost. |
| 5 / R05 | A, enabling | What evidence warrants a claim of correct interactive-software change? | A defensible outcome/oracle for the other directions; possibly a reusable evaluation method. |
| 6 / R06 | A, enabling | What runtime and development costs accompany Nu's state/coordination choices? | The workload boundary at which an otherwise useful workflow becomes too expensive. |
| 7 / R07 | B | How do learning, comprehension and prior experience affect productive use? | Training and onboarding decisions, with performance separated from preference. |
| 8 / R08 | B | Which Nu representations and tools help coding agents, and under what information policy? | A concrete agent maintenance workflow, without inferring an effect from human results. |
| 9 / R09 | B | Do benefits survive sequences of changes and accumulated requirements? | Whether a short-task gain persists through maintenance and handoff. |
| 10 / R10 | B | Which live edits and schema changes can preserve useful state and continuation? | When live development saves restart/reconstruction work safely. |
| 11 / R11 | B | How does the workflow affect collaborative editing, merging and cross-role handoff? | Team-level value and where work moves between participants. |
| 12 / R12 | B | Does domain-specific reuse or content authoring reduce total change effort? | When reusable mechanics/assets/models help and when their extension cost dominates. |
| 13 / R13 | B | Can interaction contracts make extension and replacement more compositional? | What guarantees and verification effort accompany modular game behavior. |
| 14 / R14 | B, enabling | Which actual development problems and adoption constraints should the agenda target? | Relevant populations, change families and cost boundaries. |
| 15 / R15 | C | Can prospective analysis predict the better architectural choice? | Whether analysis improves adoption advice enough to justify its own effort. |
| 16 / R16 | C | Which effects transfer across F#, other languages and source/context representations? | The boundary between Nu/package effects, language effects and information cost. |
| 17 / R17 | C | How costly are interoperability, dependency upgrades and engine/application coevolution? | Whether local application gains survive ecosystem and integration work. |
| 18 / R18 | C | Can explicit state/history help distributed play, rollback or concurrent simulation? | A possible extension beyond local development, conditional on a real Nu capability and workload. |
| 19 / R19 | C | How do deployment targets, power and energy change the value assessment? | Resource costs at equivalent useful work on relevant platforms. |
| 20 / R20 | C | What expressive and collaborative work becomes possible for designers or less specialized users? | Whether tooling broadens useful authoring without shifting hidden work to programmers. |
| Future / R21 | B, deferred human study | Which representations and intervention policies help humans steer agents toward correct changes? | Whether specification, review, redirection and takeover costs justify a workflow under reliable measures. |

Band A deserves the most preparation now. Band B receives actionable designs and consequential reading alongside it; R21's future label separates human-study feasibility from eventual research value and does not renumber the existing IDs. Band C remains an active set of conditional questions. No band implies a positive effect or established feasibility. R01–R06 now have detailed specifications; the dispositions below govern their next preparation.

## Band A study preparation

### R01 Whole workflow value

**Question and comparison.** For stated developers and change families, compare an authentic Nu workflow with an independently credible alternative workflow. Match required behavior and available resources; allow each package its normal useful facilities when estimating package value. An ordinary workflow and a feature-ablation contrast estimate different things and need separate interpretations.

**Outcome.** New and retained behavior satisfied across all assigned changes, with total setup, learning, integration, change, review and recovery work. Runtime costs accompany the development outcome. Report failures and unfinished changes rather than comparing only successful attempts.

**Evidence and rival.** The [pinned Nu account](nu-grounded-maintenance-methodology-2026-09-14.md) and survey characterize capabilities; S255–S259 and S269–S271 offer prepared-tool/package comparisons. S42 shows why package rankings can reverse with the information supplied. Familiarity, task fit and tooling maturity may explain a difference; that remains part of a practical package contrast but prevents attribution to immutability or language alone.

**Next preparation and redirect condition.** The [2026-10-11 inventory](nu-comparator-and-convention-audit-2026-10-11.md#r01-version-and-package-boundary) now pins a provisional Godot/GDScript edition and its ordinary facilities, including live inspection, programmable undo and diagnostic snapshots. The [task/common-requirement audit](nu-task-diversity-and-common-requirements-2026-10-11.md) now grounds a platform interaction in #1020 and credits ordinary Godot character/platform APIs. The [platform contract](nu-platform-contract-2026-10-11.md) resolves ordinary/dedicated character routes and proposes fixed-gravity carrying/jump/pause/removal semantics. It next needs a separate feasibility/construction decision on actual carrying, phase-correct observation and tool access; account for each package's required integration. Narrow or redirect if equivalent requirements cannot be supported credibly, the comparison is merely a deliberately weak baseline, or no consequential adoption decision remains. A scoped adverse Nu result is still informative.

### R02 Ownership and temporal coordination

**Question and comparison.** Compare credible Nu organizations for local interaction edits versus changes that coordinate entity lifecycle, parent/child state, events and effects. MMCC/ImSim is a candidate package comparison within one language/engine. The existing Breakout examples differ in physics and collision implementation; intended parity does not establish controlled equivalence.

**Outcome and rival.** Correct completed changes, retained temporal obligations and total work. Explicit transitions may reduce omissions while adding propagation/plumbing; nearby immediate-mode code may simplify local edits while increasing order or identity sensitivity. These are two-sided, prespecified predictions. Patch spread, messages added and architecture conformity are explanatory observations, not success definitions.

**Evidence and next action.** Reuse the source distinctions, S39/S40, S298 interaction typing, S299 modular preservation and the Ceptre/SGL alternatives. Use the [Blaze Vector mismatch register and requirement families](nu-task-diversity-and-common-requirements-2026-10-11.md): a second named pair has real input, gravity, hit-count and lifecycle differences, not established baseline equivalence. Fix intended common behavior and record any alignment work before assigning tasks. Redirect the causal claim to a package claim if differences cannot be isolated without rebuilding one style into the other. No adapter or baseline construction is authorized by this card.

### R03 History assisted debugging and recovery

**Question and comparison.** Compare an available Nu history/inspection workflow with a credible ordinary debugging/recovery workflow on reproducible failures. A within-Nu feature comparison may estimate an incremental workflow benefit; a comparison to another engine estimates a package difference. First identify exactly which state, inputs, pending work and effects each workflow retains.

**Outcome and rival.** Independently verified repair and successful continuation/recovery, elapsed and active work, retention/instrumentation costs and unresolved failures. A history view may help locate an unknown event but add overhead when the offending entity or event is already known. The [completed S42 study](literature/full-reading/S42-stream-debugger-comparison.md) gives a concrete predecessor for such a reversal; it does not estimate a Nu effect. S66 and [State Explorer/live replay](literature/full-reading/S296-S297-state-exploration-and-live-replay.md) provide closer debugging/history alternatives.

**Next action.** The [selected application contract](nu-history-application-contract-2026-10-11.md) specifies functional Gaia/MMCC Breakout, a halted checkpoint, B0 values and separate B1 continuation. Its launch, observation phase, controlled input and same-state fresh reconstruction remain feasibility dependencies. Prepare actual repair tasks only after the technical/access boundary is supported, preserving known versus unknown fault information. Redirect if instrumentation solves the fault or requires an unavailable facility; in-process getters do not verify agent access. A model restoration check alone does not establish debugging benefit.

### R04 Domain modeling and evolution

**Question and comparison.** Distinguish richer domain representation from the narrower [D1 explicit-case versus equivalent catch-all convention](fsharp-domain-evolution-research-proposal-2026-09-16.md). The first can change API and modeling effort; the second can potentially retain language, engine and initial behavior. Both D1 baselines can be exhaustive, and a correct catch-all remains valid.

**Outcome and rival.** Correct new and retained behavior, including compiler-silent semantic/temporal obligations, under a common allowance. Record diagnostic opportunities separately from obligations. Explicit cases may expose edit sites but also create noisy work or encourage mechanically compiling repairs. Static types, informative names, documentation, compiler feedback and source size are distinct interventions.

**Evidence and next action.** P08, S34–S37, S127/S129 and the completed type-evolution readings constrain the design. The [existing-site audit](nu-comparator-and-convention-audit-2026-10-11.md#r04-an-authentic-existing-source-site) now specifies the guarded MMCC update/fallback, checked-in warning policy and contrasting authored requirements. FS0025 is not explicitly promoted to an error; exact effective policy and diagnostics await authorized validation. The [Blaze Vector projectile site](nu-task-diversity-and-common-requirements-2026-10-11.md#r04-an-additional-authentic-convention-site) now adds lifetime/identity obligations and valid default behavior. These two demos broaden source coverage within one Nu lineage; they do not establish representative tasks. Keep D1 as one convention study; it cannot establish whole-Nu or F#/C# superiority. Redirect if the contrast is practically immaterial or already resolved by a close comparison.

### R05 Interactive correctness and evaluation

**Question and comparison.** Define what counts as successful change under state, time, identity, input and external-effect obligations. A separate methods study would compare observation strategies against independently justified fault/behavior cases; simply building a benchmark is not yet a research contribution.

**Outcome and rival.** False passes, false failures, inconclusive results, fault sensitivity and specification/observation cost. Compiler acceptance, screenshots, sampled traces, development-test agreement and final behavior are distinct. S42's supplied-test completion is useful evidence within its generated repair setting; it is not an independent general semantic oracle.

**Evidence and next action.** Reuse [industrial regression testing](literature/full-reading/S294-industrial-game-regression-testing.md), [temporal monitoring](literature/full-reading/S281-game-monitoring-thesis.md), S220/S222 and agent/game judge reconstructions. Draft an obligation-to-observation table covering triggers, clocks, horizons, resets, identity, pending events and inconclusive cases. Resolve an exact missing formula or release when the chosen contract depends on it. Development feedback must be separated from final scoring; no final-test-driven repair or stopping.

### R06 Runtime and state retention costs

**Question and comparison.** Determine how chosen representation, retention and coordination policies change frame-time tails, allocation, working set, throughput and edit/recovery latency under equivalent useful work. Compare identifiable policies or complete runtime packages, with the corresponding attribution boundary.

**Outcome and rival.** A workflow can reduce debugging effort while increasing retained memory or frame stalls. Charge snapshot creation, retention, disposal, host work and rebuilding to the correct boundary. Average FPS and source size cannot stand in for that trade-off.

**Evidence and next action.** S138–S151, S211–S214, S237–S248 and S260/S261 supply mechanisms and workload-specific positive/adverse results. Prepare workload dimensions—world size, mutation rate, retention horizon, event fan-out and external/native resources—and identify the exact Nu policy each comparison would vary. Use a workload grounded in R01/R03 before proposing unrelated allocator measurements. A cost result can refine useful scope without refuting every development benefit.

## Band B study preparation

### R07 Learning and comprehension

Compare newcomers and experienced users within separately defined populations, with an authentic onboarding/support policy. Measure learning effort, correct changes, delayed retention and transfer to a new task; keep preferences and comprehension questions secondary. S300/S301 show why understanding, structure-conformity scores and partial progress cannot be substituted for completed change. S39/S40 and S255–S259 preserve positive and contrary representation results.

The [2026-10-11 learning and role contract](nu-learning-and-role-contract-2026-10-11.md) now specifies prerequisites, preparation, assistance, all-assigned outcomes and the distinction between onboarding and trained productivity. [S38](literature/full-reading/S38-cognitive-dimensions.md) is fully read: use its dimensions as qualitative, task-specific mechanisms, not a validated learning score. Its supplied-target editing result has a narrower scope than independent maintenance solving. [S307](literature/full-reading/S307-programming-walkthrough-draft.md) now reconstructs the qualitative procedure in an explicitly marked archived draft and supplies a candidate decision/knowledge/assistance inventory for the existing R11/R12 roles. The [completed S304/S305-report/S306 readings](literature/full-reading/S304-S306-walkthrough-edition-access.md) now resolve the selected user-protocol and final-method gaps, preserving overlapping accounts and assistance. The [S305 journal reconciliation](literature/full-reading/S305-problem-centered-design-journal-reading-2026-10-18.md) now adds the same S304 user check and explicit walkthrough-prediction limits, with no independent-study increment. Neither the draft nor final method validates readiness; select the practical role/task before later measurement work. The human comparison remains deferred pending a practical beneficiary, task/access validity and reliable outcomes. The [S308 engine-API study](literature/full-reading/S308-engine-api-metrics-access.md) and its [S309 metric origin](literature/full-reading/S309-structural-api-usability.md) are now completely read. S308's historical C++ file scores and S309's Java structural/face checks supply no observed developer outcomes. Changed AESI/documentation definitions and unresolved formula/calculator/aggregate correspondences preclude treating shared metric names as cross-language validation. Specify the task-facing interface and language/tool mapping before using a structural descriptor; this evidence does not validate a Nu usability or learning score. Redirect if a supposed language effect is only unequal preparation or the claimed outcome is a preference score.

### R08 Coding agents and tool support

Compare concrete agent workflows using Nu representations, typed/source context or inspection tools while fixing the intended model/policy and documenting available information and cost. Human and agent results require separate estimates. Valid repairs may reorganize code; conformity to the assigned starting style is not an outcome filter.

Measure new/retained behavior across every assigned attempt, resource use, failure classes and recovery burden. P03–P13, S35/S36 and the game-agent readings already overlap strongly with generic context/planning claims. The [information/feedback contract](nu-agent-information-and-feedback-contract-2026-10-11.md) now specifies candidate inputs, current diagnostics, ordered development observations, stopping and separate final-evaluation resources. P08/P12/S42 supply the close feedback/probe/information boundaries. The retained controller's no-tools/full-file protocol does not implement the proposed ordinary-tool workflow; generic JSONL or ephemeral mode does not establish compatibility. Next make a separate workflow/feasibility decision about actual tool/edit/observation access, preserving the backend/transport/security boundary and zero allocation. The [completed S227 v2 reading](literature/full-reading/S227-continual-gui-playtesting-v2.md) now supplies clarified rubric-blind development feedback and a separate final judge, expanded judge validation and partial inference costs. Preserve its unresolved gain-plot correspondence, early-stop population, human-comparison conflict and unavailable scaffold; actual Nu tool/phase access and independent scoring remain the consequential feasibility gap. Redirect if the contribution is just another model leaderboard, F# port, or unpriced tool advantage. New model calls and workers remain unallocated.

The current packet proposes bounded agents as executors of independently specified changes, while treating task convergence as a coverage risk. Source/history/practice provenance, adverse families and valid alternative solutions matter more than repeated prompts on one puzzle. Agent-only observations do not estimate human-steered productivity; R21 retains that future transfer question.

### R09 Sequences of change and retained obligations

Compare the durability of a selected representation/workflow across ordered changes with an explicit dependency structure. Preserve the submitted predecessor state and record what happens after a failed change. A clean reference predecessor, a repaired predecessor and the actual inherited state define different questions.

Measure retained and new obligations, cumulative effort, recovery and missingness for the assigned sequence. P04–P06/P09 and the long-horizon agent readings are close prior art; sequence length alone adds little novelty. The [2026-10-11 sequence contract](nu-change-sequence-contract-2026-10-11.md) now specifies an authored/adapted control–lifecycle–policy-revision chain, active/retired obligation versions, actual inherited workspace with fresh conversation/environment, and independent hidden scoring. Actual inherited, clean-reference and repaired predecessors remain different policies. Preserve failed intermediate delivery even if the final product recovers; an intentionally retired rule is not a regression. [Q2's pause/exit policy](nu-pause-exit-contract-2026-10-11.md) now specifies phase, clocks, effects and quit precedence while permitting local pause implementations. Next resolve practical task value and held common-behavior, input/observation and deadline/watchdog feasibility before any allocation. Redirect if a longer sequence adds no useful durability question or merely repeats an established benchmark contrast.

### R10 Live editing and state migration

Compare restart/reconstruction, replay and migration workflows for a specified class of edits. State the identities, defaults, pending events, observers and external effects that must survive; a type-correct migrated object does not establish valid continuation.

Measure correctly preserved behavior, recovery/reconstruction work and unsupported edits, with S71/S86 and [S295](literature/full-reading/S295-persistent-object-evolution.md) as distinct change contracts. The [2026-10-11 live-edit audit](nu-live-edit-contract-2026-10-11.md) now binds the F# reload/late-binding path, model conversion/fallback, initialization choices and declared-content reconciliation. Its first authored case changes future brick rewards while preserving existing progress, compared with matched restart/reconstruction. A reload event can follow a compilation failure; a conversion fallback can reset the game. The [2026-10-15 behavior-only construction](nu-live-reload-feasibility-2026-10-15.md) now passes actual core reload, FSI model/dispatcher installation, complete checkpoint preservation and one prescribed future hit against matched fresh reconstruction. F9/menu, native input and external effects remain unobserved; this establishes no work saving. The dependency continuation now binds the selected Prime converter/default paths to the package: successful conversion can default a new field or remap positional values without an exception. The [initializer-only schema observation](nu-schema-reload-feasibility-2026-10-16.md) now preserves the inherited state but fails the required new-field mapping: live reward 0 versus fresh initial reward 200, with separately correct next-hit scores 100 and 300. The [explicit-migration treatment](nu-schema-migration-feasibility-2026-10-16.md) freezes absent, deliberate-zero and nondefault-value cases, repeat reloads and a failed-compilation control. Its application compiles, but four harness/conformance failures remain unresolved. Subsequent objective attempts 11–18 failed consecutively, crossing the five-failure return at 15; passing controls 19/20 do not authorize that overrun. Construction is stopped with the current draft uncompiled and unaccepted. No native migration result is established. Preserve the exact draft and return; ordinary continuation does not resume this gate. Count application adaptation, verification and reconstruction work separately; other schema changes need their own correspondence. S218/S219 originals are now fully read, separating quiescence from controlled object/GUI transfer; their exact implementations and any other edition gaps matter when the selected comparator depends on them. Redirect or narrow if the proposal assumes arbitrary code/state migration or reversal of irreversible effects. Demonstrating more edit kinds alone does not establish developer value.

### R11 Collaboration and handoff

Compare team workflows for concurrent edits, merge conflicts and designer/programmer handoff. Establish whether Nu changes shared representation, coordination or tooling; personal debugging history and a collaborative document history are different facilities.

Measure correct integrated outcomes, unresolved conflicts, total team effort and work shifted between roles. [S283](literature/full-reading/S283-nccollab-collaboration-history.md), [S284](literature/full-reading/S284-levelmerge-scene-merge.md), S286–S288 supply selected correspondence, collaboration/history and practice methods. The [2026-10-11 collaboration contract](nu-collaboration-and-handoff-contract-2026-10-11.md) now binds the serialized title scene to its F# event handles and proposes a rename/presentation integration case with contrasting independent, conflicting and deletion requirements. Preserve the source's whole-file save, runtime identity and explicit-load boundaries; textual success does not establish references, behavior or safe stale-editor reuse. Role responsibilities, handoff information and complete work accounting are specified, but a dedicated Nu merge treatment is not established. Next identify a practical decision and actual treatment/comparator before separately authorized feasibility or participant design. [SceneGit's primary method is now read](literature/full-reading/S285-scenegit-reading-2026-10-15.md); its snapshot correspondence/merge and reported scale/subjective results leave workflow comparison, conflict-study outcomes and total-team work unresolved. Account for team-level assignment and repeated tasks. Redirect if the apparent gain is one role's time saved by undocumented assistance from another, or a nonexistent merge facility is required. Recruitment remains separate from this preparation.

### R12 Reuse and content authoring

Compare reusable mechanics, asset/configuration families or domain-specific authoring with a credible ordinary implementation. Separate creating a supported variant from extending the representation to express a new requirement.

Measure behavioral validity, authoring/change effort and amortized construction/integration/extension cost. S255–S259 show prepared-tool gains, nulls and overlap between datasets; [S263/S264's published generation methods](literature/full-reading/S263-S264-phylogenetic-generation-reading-2026-10-15.md) are now read, with bundled guidance/manual integration, a nearly null seed-selection-only contrast and overlapping conference/journal data. The [reuse contract](nu-reuse-and-authoring-contract-2026-10-11.md) separates configuration, family revision and vocabulary extension. Its [Terra Firma revision series](nu-terra-firma-revision-feasibility-2026-10-18.md) now observes both shared operators delivering the tint and propagation missing one target's tint while preserving its local roughness. Recorded reconstruction and exact history-correspondence limits are separate from native lifetime and authoring benefit. The first batch/local attempt failed input integrity before editing. Its later revalidated continuation and actual-save reopen deliver all 32 tints while preserving local roughness and the declared old histories, with no operator lifecycle callbacks. All four pairs are now observed; the invalid startup remains retained. Later revision and complete-work consequences remain untested. Preserve ordinary batch/helpers/composition as valid alternatives, with selection, construction, verification and any repair counted. Follow generation methods only if that different comparator becomes consequential. Redirect if only visual appeal, generated volume or family similarity is observed. Distinct editions of one dataset are not replications.

The [practice continuation](nu-practice-and-task-provenance-2026-10-11.md#2026-10-18-continuation-material-revision-rationale-and-observed-limits) now supplies a specific maintainer rationale for shared material revision and local choices. The exact tint/roughness field policy remains authored: the sources do not promise field-wise merging within a material record. Preserve that distinction when interpreting the adverse delivery and selecting a practical repair comparison; independent demand and total benefit remain unresolved. The [retained-history audit](nu-reuse-and-authoring-contract-2026-10-11.md#2026-10-18-retained-history-audit-a-conditional-switching-prediction) now predicts a specific B-to-P switching limitation from the actual saves; it does not make continued batching fail. Separate continued-use, repair and switching policies in the next comparison.

### R13 Interaction composition and guarantees

Compare an explicit interaction/behavior contract with a credible less-formal development method for extension or replacement. The research can concern what is provable, what faults are detected, or what verification effort is saved; these are separate outcomes.

S298 provides data-compatible interaction substitution with configured runtime checks. [S299](literature/full-reading/S299-modular-reactive-verification.md) provides property preservation under model and exit assumptions; Ceptre distinguishes local existential composition from whole staged behavior. The [2026-10-11 interaction contract](nu-interaction-preservation-contract-2026-10-11.md) now binds a Breakout control replacement/alias extension to input capture, priority, phase, retained state and effect obligations. Host input is not a world snapshot, and the actual MMCC update emits effects; its type signature does not establish purity or these behavioral predicates. Keep this contract as support for R02/R05 unless a consequential guarantee or total verification-effort question justifies a standalone R13 study. No S299 theorem transfer to the Nu frame loop is established. Formalization, instrumentation and execution remain later authorization decisions.

### R14 Practice and adoption relevance

Use existing primary studies and passive repository/source inspection to identify recurring changes, constraints, support needs and reasons to adopt or abandon a workflow. A later empirical study would need a justified sample and its own authorization; observations/interviews remain held. This direction supplies sampling and cost boundaries for R01–R13; another list of reported complaints is not automatically a standalone contribution.

The [2026-10-26 public-request continuation](nu-public-request-provenance-2026-10-26.md)
expands the initial account frame and checks concrete UI/deployment/text needs.
The fill-direction request is a conditional whole-workflow extension/configuration
case: the inspected Nu path fixes direction, while pinned Godot exposes ordinary
configuration. It is not a mined extension of an existing Nu direction union,
a new standalone research contribution or a replacement for R04. Camera demand
changes within its thread; a reported historical CJK repair remains positive
evidence while Gaia text entry is a distinct reported concern. R01 remains a
broad conditional adoption question, not a fixed moving-platform-only task.
Promote a new case only when a consequential workflow decision and common outcome
justify it; do not infer prevalence or implementation from account counts or
issue status. The review authorizes no port, observer, candidate or returned work.

S250–S252, S267–S271 and S288–S290 supply situated practice evidence. The [R14 provenance record](nu-practice-and-task-provenance-2026-10-11.md) now links the proposed families to public requests, source and those methods, with beneficiaries and omitted work explicit. Corrected issue reports prevent two false bug-task selections; mixed history accounts challenge assumed demand, and existing scripts qualify an automation-absent asset comparison. Keep the set purposive and distinguish authored/adapted requirements from current defects. Next choose a practical decision before separately authorized feasibility; asset/engine-upgrade work is a conditional total-work case. [S266's completed preprint reading](literature/full-reading/S266-game-development-problems-reading-2026-10-15.md) now supplies source-conditioned task discovery and the shared-corpus lineage. Exact longitudinal magnitudes still require the promised row-level release, denominator reconciliation and document-level/source-balanced analysis; the paper reading does not establish prevalence. Continue the retained practice search from offset 100 when an independent coverage gap needs it. No participant contact or recruitment occurs under this agenda.

## Band C study preparation

### R15 Prospective architecture choice

This retains D2 as a future decision question: does analysis performed before seeing successor outcomes improve architecture/package choice against equally informed ordinary review, defaults or simpler predictors? Measure decision quality and the cost of producing advice. The earlier [D2 proposal](architecture-maintenance-research-proposal-2026-09-15.md) and completed selection literature already establish much of the method.

Prepare this only around a real choice with credible alternatives and change profiles. Advice and predictions must precede outcome observation. Promote it when R01/R02 identify meaningful, predictable trade-offs; demote it if one option dominates or the analysis costs more than the decision is worth. Preparing the question does not reopen D2/A0 selection or construction.

### R16 Language and information representation transfer

Ask whether a specified result survives a change of language, library or source/context representation. A natural F#/C# package comparison and an isolated source-information manipulation have different interpretations. Match intended behavior and accessible support; do not force an unnatural transliteration to manufacture equivalence.

Measure correct change and total work/information cost. Existing E/H negative compactness observations remain valid; authored source size, cumulative model traffic and retained/peak context are distinct. S34–S37 and the type/agent evidence defeat a generic “F# is understudied” rationale. First identify a result or practical choice worth testing for transfer. Redirect if training familiarity, APIs and tooling cannot support the intended attribution. A universal language ranking is outside this agenda's defensible scope.

### R17 Ecosystem integration and coevolution

Compare supported approaches to dependency/API upgrades, native-resource integration or engine/application boundary changes. Measure all affected behavior, integration/recovery effort and ongoing compatibility work. S267's operational migration and S204's industrial change propagation motivate costs beyond the local edit.

The [Nu/Jolt dependency audit](nu-jolt-dependency-audit-2026-10-11.md) now supplies an actual cross-layer case: history rebuilding, native maintenance/callback semantics, binding coverage and package provenance. It verifies package-to-vendored-binary identity and the upstream zero-time fix, while exact native source/build correspondence and actual Nu behavior remain open. Nu's positive-time guard and periodic optimization persist; upstream batch advice is not an established managed API at the inspected pin. Use this case to refine R03/R06 first. Promote R17 when integration demonstrably dominates the target workflow; a provenance mismatch alone is not a standalone research contribution. Existing backend, transport and security decisions remain fixed.

### R18 Distributed state and concurrency

Explore whether explicit state, identity and history could help deterministic replay, rollback, synchronization or concurrent simulation. No inspected Nu capability is being newly asserted to implement these distributed guarantees. Networking delay, nondeterminism, ownership and externally visible effects require their own contracts.

Possible outcomes include divergence, recovery correctness, responsiveness and computation/bandwidth cost at equivalent work. The new search locates *Hybrid Prediction for Games' Rollback Netcode* (DOI 10.1145/3532719.3543199) and CRDT-based game-state synchronization (conference DOI 10.1145/3721473.3722144; same-title arXiv 2503.17826). These are title/metadata leads; their methods and exact edition relationship remain unverified. Next, establish a real Nu use case/capability before promoting a primary reading. Keep this exploratory if it requires creating a networking subsystem; immutability alone does not establish determinism or network consistency.

### R19 Deployment power and energy

Compare relevant deployment/runtime configurations at matched useful work, quality and behavior. Measure power, total energy, frame-time distribution and any developer/runtime trade-off separately. [S260](literature/full-reading/S260-unreal-energy.md) and [S261](literature/full-reading/S261-unity-unreal-energy.md) show workload-dependent engine ordering; S265's selected source/data and missing visuals retain their limits.

Next, connect a target platform and workload to R06, then identify necessary build and measurement correspondence. Promote when energy or constrained hardware is a real adoption boundary. Redirect an independent engine-ranking study if it repeats hardware-specific FPS/power comparisons without an unresolved Nu decision. Equal wall-clock duration alone does not establish equal completed work.

### R20 Expressive reach and designer collaboration

Ask whether Nu's actual authoring workflow lets designers or less specialized developers express and revise useful interactive behavior with less dependence on specialist intervention. Compare authentic workflows and separately account for preparation by tool builders or programmers.

Measure successfully expressed behavior, revision work, learning and assistance; creative quality requires a justified independent assessment rather than screenshot preference as a substitute for behavior. S67, S253, S288 and S291–S293 motivate expressive and cross-role questions. The [learning and role contract](nu-learning-and-role-contract-2026-10-11.md) now maps presentation, family-maintenance and behavior/integration responsibilities onto the R11/R12 source cases, with prerequisites and specialist assistance visible. These are authored cases, not validated designer tasks. Next establish an actual beneficiary and practical unsupported-change requirement, then follow the exact usability/expressiveness method needed. Promote when that role and facility exist in the intended setting. Redirect if the proposed benefit depends on inventing a new editor or on excluding all requests outside a prepared vocabulary.

## R21 Human steering and intervention — future direction

Ask whether Nu's representations, state visibility and contracts help people specify work, delegate, inspect evidence, redirect an agent and accept correct changes. This is distinct from R08's fixed agent/tool policy and R11's multi-person editing. It remains valuable for the user's intended 2027 setting, while direct steering effectiveness is deferred because construct reliability, task/person variation and participant feasibility are unresolved.

Preserve two future policies: **steering-only**, where people specify/inspect/diagnose/redirect and agents implement, and **unrestricted intervention**, which also permits direct editing and takeover. Human-authored replacement code or patches supplied through prompts count as human coding. Count specification, context gathering, review, redirection, rescue and rework alongside agent cost and verified outcomes. A successful artifact does not reveal how much expert work produced it.

[S229](literature/full-reading/S229-picoscenes-expert-ai.md) supplies favorable expert–AI practice with explicit allocation/accounting limits. The [2026-10-11 measurement contract](nu-steering-measurement-contract-2026-10-11.md) now applies S302's adverse AI-permission result and S303's qualitative interaction method to observable actions, intent evidence, independently checked outcomes and overlapping work. It specifies candidate categories and reliability questions without claiming a validated instrument. A larger sample cannot by itself define the construct. Next establish a practical steering comparison before separately authorized instrument/participant feasibility; small descriptive work is only a future option. Retain human-only/agent-only cases when they clarify a specific question, rather than requiring three equally funded arms or a universal autonomy ranking. Do not retrofit this direction into D1 or add a steering-policy factorial to R02.

## Readiness and next actions for all directions

**Updated through 2026-10-18.** These dispositions separate observed mechanism evidence, remaining research dependencies and execution authority. The linked execution records own exact scope, all attempts and adverse results; a passed probe is not a completed direction. **Conditional** identifies a consequential dependency; **deferred** preserves a future question or existing hold. The [study packet](nu-research-study-designs-2026-10-08.md) owns the proposed comparisons and shared accounting, while [PLAN](../PLAN.md) owns authority.

**Execution prerequisite:** the [October 18 storage-integrity return](workspace-integrity-return-2026-10-18.md) takes precedence over the native next actions below. Establish reliable execution storage and revalidate exact inputs before a prospectively bound continuation. Work on the verified C: publication copy can continue; neither documentation nor a healthy volume status clears that runtime boundary. The separate R02/R10 five-failure returns remain in force.

| ID | Disposition | Consequential dependency | Next action / promotion condition |
| --- | --- | --- | --- |
| R01 | [Dependency probe executed](nu-platform-feasibility-2026-10-15.md); whole-workflow comparison conditional | Ordinary contact maintained support but missed the frozen positional carrying tolerance; no Nu scene or Godot comparison was run | Decide whether a practical requirement warrants a new, prospectively specified motion profile or explicit carrying logic. Preserve the failed condition and count integration work; jump/pause/removal and adoption value remain unmeasured. |
| R02 | [Unchanged standalone lifecycle pair passed](nu-standalone-lifecycle-feasibility-2026-10-15.md); subsequent input construction stopped under [PLAN's return record](../PLAN.md#where-current-information-lives) | Synthetic ClickEvents validate selected lifecycle/cleanup predicates, not SDL/ButtonFacet input, held-key polling or pause behavior. The new input draft crossed the five-failure compilation threshold and has no native run or accepted final source/build review | Preserve the return and unfinished draft; ordinary continuation does not resume that gate. If separately resumed, bind the exact source/unchanged hosts/runner and accept independent plus parent review before native input execution. Keep both imperative applications, package attribution and distinct cleanup obligations explicit; Blaze Vector remains unvalidated. |
| R03 | [Functional Gaia B0 pair](nu-history-feasibility-2026-10-15.md) and [twenty-step B1 prefix](nu-history-continuation-2026-10-15.md) passed; [symptom/access map](nu-history-question-access-2026-10-18.md) bound | The stale-position episode lacks original predecessor names; Interactive getter evaluation changes history and clears redo; ordinary agent access and repair benefit remain unmeasured | Validate the chosen inspection route and branch/halt policy on a case with actual predecessor evidence. Keep the inferred collision out of confirmed diagnosis scoring. Count inspection, reconstruction and added instrumentation; separate state reach, localization, proposed correction, verified repair and continuation. Another B0 witness is not benefit evidence. |
| R04 | [Actual compiler contrast](nu-application-diagnostic-feasibility-2026-10-15.md) and [bounded pause/lifecycle oracle](nu-pause-runtime-feasibility-2026-10-15.md) exercised | The added explicit case emits warning-only FS0025; four references pass and five frozen faults are detected under the functional accompanied harness, not an ordinary agent workflow | Carry the demonstrated semantic/temporal obligations into supported input and standalone references. Preserve valid catch-alls, warning-free behavioral failure and the retained reconstruction/setup failure; diagnostic exposure and D1 maintenance benefit remain unmeasured. |
| R05 | [Stub-world delivery](nu-event-feasibility-2026-10-15.md) and the R04 executable oracle provide bounded evidence | Selected priority/Resolve/unsubscribe traces and frozen-fault detections do not establish general oracle sensitivity, input delivery or independent external validity | Validate the actual trigger and observation phase for the next selected requirement. Preserve event order, exercise evidence, source-fault lineage and missingness; count observer construction and its overhead. |
| R06 | [Twelve-process component series completed](nu-recovery-cost-feasibility-2026-10-15.md); practical cost-benefit conditional | History acquisition is faster in all six pairs, direct history recovery slower in all six, and readiness differences have both signs; retained payload scopes differ | Preserve the original unexplained reconstruction timeout and separate later diagnostic. A further cost study needs a consequential workload boundary and matched useful work; these timings do not estimate a pure persistence effect, retained/native memory or developer savings. |
| R07 | Preparation/outcome and candidate knowledge inventory specified; human comparison deferred | Practical role/task, supported access and validated measurement; S305 final edition resolved, supplement/raw materials conditional | Use the [completed S304/S305-report/S306 readings](literature/full-reading/S304-S306-walkthrough-edition-access.md) with their shared lineage and assistance limits. Select the consequential role/task; neither the qualitative final method nor an analyst inventory validates a readiness score. |
| R08 | Information/feedback/accounting contract prepared; execution held | Reconcile intended tool/edit/observation authority with the retained no-tools controller | Use ordered behavioral observations and separately resourced final scoring. A workflow/feasibility decision precedes any implementation; S227 v2 is conditional on selecting its GUI method. |
| R09 | Sequence/lineage and Q2 behavior policies specified; execution conditional | Practical durability question, common baseline, input/observation access and deadline/watchdog validity | Use actual inherited histories with explicit active/retired obligations and failure/missingness accounting. Validate Q2's phase/clock/effect contract separately; keep reference/rescue branches distinct. Promote for a meaningful durability decision. |
| R10 | [Unchanged-schema preservation](nu-live-reload-feasibility-2026-10-15.md) passed; [initializer-only schema reload](nu-schema-reload-feasibility-2026-10-16.md) preserved old state but failed the required new-field mapping | Actual FSI conversion installed reward 0 despite initializer 200; live/fresh scores were 100/300 after the declared hit. Both reward-specific continuations passed. Explicit migration, effects and practical savings remain unmeasured | The separate [explicit-migration comparison](nu-schema-migration-feasibility-2026-10-16.md) has stopped after the objective-control return threshold was exceeded. Preserve its uncompiled current draft; ordinary continuation does not resume that gate. Preserve fully observed failures, actual inherited values, exact live/fresh checkpoint provenance and all construction/verification/reconstruction work. Do not repair or relabel the initializer-only result. |
| R11 | Artifact/role contract specified; team comparison deferred | Practical collaboration decision, actual treatment/comparator and save/load/observation feasibility | Use the scene-name/F# handle case and total-team accounting; distinguish textual, reference, behavioral and stale-editor outcomes. No dedicated Nu merge treatment or human effect is established. |
| R12 | [Terra Firma preservation prerequisite](nu-terra-firma-reopen-feasibility-2026-10-18.md) and [four revision/reopen pairs](nu-terra-firma-revision-feasibility-2026-10-18.md) completed across nine processes, including the retained invalid startup | Both batch cases and P-shared deliver all 32 tints; P-local retains roughness but misses one tint. Propagation records 160 managed reconstruction pairs versus predicted 163 and separate Order-only fresh history findings. Ordinary Gaia editing access, complete work and practical benefit remain unmeasured | The [revalidated continuation](nu-terra-firma-revision-continuation-2026-10-18.md) resolves the missing B-local outcome. For a practical comparison, specify completion/repair and history consequences and count selector/helper construction, verification and all failures. Preserve all nine attempts and actual adverse reopens; another passing cosmetic variant cannot establish authoring value. |
| R13 | Local interaction contract specified; standalone study conditional | Coherent host input, scheduling/effect assumptions and consequential verification value | Use the paddle replacement/alias contract for R02/R05. Promote only if preservation or total verification effort warrants a richer boundary; no checker or theorem transfer is established. |
| R14 | Provenance frame prepared; broader adoption coverage conditional | Practical beneficiary, eligible task and population scope | Apply the family/evidence map and corrected issue histories to the selected case. Asset upkeep is a conditional total-work extension; preserve missing roles and source dependence. Use S266's completed source-conditioned reading; exact expanded-corpus claims still need released rows and reconciled denominators. |
| R15 | Deferred D2 | Meaningful prospective choice and pre-outcome information | Retain the selector history; promote only after R01/R02 expose a practical predictable trade-off and D2 is explicitly reopened. |
| R16 | Conditional later transfer | A bounded result worth transferring | State the changed language/context/package dimension and credible equivalent behavior; preserve E/H adverse compactness evidence. |
| R17 | Conditional; cross-layer case inspected | Exact native build provenance, actual loaded artifacts and affected obligations | Use the package/blob/fix audit to refine R03/R06; preserve Nu's positive-time/optimization policy and unverified batch-binding route. No current defect or cost advantage is established. |
| R18 | Deferred exploratory extension | Verified distributed Nu capability and real workload | Establish a concrete use case before reading netcode/CRDT methods as treatment evidence or proposing new infrastructure. |
| R19 | Conditional extension of R06 | Target platform and matched useful work | Identify an energy-relevant adoption boundary, then bind build/sampling/measurement correspondence; promote only if it changes the value decision. |
| R20 | Deferred human-role comparison | Existing authoring facility and intended non-specialist role | Identify a representative supported/unsupported revision and assistance boundary before expressive-reach claims. |
| R21 | Observation/cost vocabulary prepared; steering effectiveness deferred | Reliable constructs, practical comparison, task/person variation and participant feasibility | Use the S229/S302/S303 measurement contract; establish a consequential comparison before instrument validation and participant design. Preserve both policies, unknown intervals, all assigned work and contribution provenance; no sample size or pilot is authorized. |

## Shared study requirements

Each later protocol needs a claim-to-source-to-comparison record: the actual Nu revision/capability, intended users and changes, closest methods and adverse evidence, assigned treatment, initial information, permitted development feedback, final observation, total cost, and the inference it supports. The current source basis remains revision `064f7ae92a8506689cd91aff5e6804a375d6ef3d`; this preparation does not certify current-head source correspondence. A later source refresh must record what changed.

Separate package effects from mechanism effects. Use credible alternatives and give a reason for their information/tool policy. Initial behavior equivalence is an obligation to validate, not a consequence of naming the same game. Do not implement the requested change in an adapter, hide extra work in setup or require the preferred internal organization as the behavioral answer.

Choose outcomes appropriate to the question. For maintenance, retain all assigned attempts, new/old behavior, incomplete outcomes and missingness. Do not average time only over successful repairs and call it the overall treatment effect. Model repeated developers, applications, tasks and sequences at their actual units; repeated frames and publications are not independent participants. Specify practically meaningful effects, uncertainty analysis and resource allowances only after the population, outcome and feasible design are known. No sample size or allocation is invented here.

Record intermediate observations—diagnostic exposure, comprehension, navigation, patch spread, tool use and source size—without turning them into proof of correct change or adjusting away post-treatment consequences to claim a pure mechanism. Information probes can themselves change behavior and cost. S42 makes initial failing-entity knowledge a concrete candidate moderator; it does not justify a huge factorial crossing every possible factor.

Preserve favorable, null, adverse and interaction results. Existing E/H results are not rescored or discarded. Stop or redirect a proposed study when its decision is immaterial, its closest predecessor already answers it, its comparison is not credible, its outcome cannot test the claim or its required resources are unavailable. An adequately measured negative result is not a reason to replace cases until Nu wins.

## Preparation order and literature continuation

1. **Use the completed R01–R06 design packet.** The current emphasis is mechanisms/costs plus bounded agent maintenance, with R14 supplying practice/task provenance. R01 retains eventual adoption value; human steering is a future R21 question. No mandatory human/agent/team factorial follows.
2. **Use the resolved source boundaries before any build.** The [2026-10-11 audit](nu-source-contracts-and-scenarios-2026-10-11.md) supplies R02 ownership/order/identity/effects, a verified historical issue/patch, R03's real history/reference/access boundary and R05/R06 trace/cost specifications. The [history application contract](nu-history-application-contract-2026-10-11.md) now selects R03's functional MMCC/Gaia subset and B0/B1 observations. The task-diversity audit adds common platform requirements and a second application/site. The platform contract now resolves Nu route/configuration and common semantics, with phase/identity/cost limits. The linked October 15 execution records and current table above now resolve selected carrying, history, diagnostic, oracle and cost questions. Use their remaining boundaries for the next confident construction, especially supported input before standalone pause/exit references. Source sketches, measured subcontracts and historical fixes do not establish full baseline equivalence or candidate allocation.
3. **Maintain all other dispositions above.** Use their cards to identify beneficiaries, outcomes and conditions for promotion. Resolve consequential accessible gaps without waiting for every human/access-limited direction. A newly found close or adverse source can reorder the agenda.
4. **Read where the answer can change the design.** S42's previously queued publication and selected artifact are now reconstructed. S38 now supplies a complete framework/edition reading and R07 has preparation/role/outcome boundaries. S304, both S305 report/journal editions and S306 now supply the selected original/final methods; S305's journal adds the same S304 prototype check and no independent cohort. S227 v2, S263/S264 and S266 have also been read; use the [reading index](literature/full-reading/INDEX.md) for exact coverage, shared datasets and remaining artifacts/edition limits. R08's information/feedback contract remains specified while ordinary tool/edit/observation compatibility is unverified. Completed reading does not validate an instrument, establish independent replications or remove source/time confounding from a prevalence claim. Exact temporal, live-state and comparator gaps remain attached to the directions that need them. Resolve accessible consequential gaps without waiting for a fixed batch to finish or for denied sources to become available.
5. **Promote C directions by evidence.** A verified capability, an actual stakeholder/workload need, or a close method that exposes an important unanswered question can raise their priority. Generic novelty claims, attractive feature names and raw citation counts cannot.

Searches are targeted to missing mechanisms, comparators, methods, contrary results and edition changes. Use aliases across relevant communities and follow primary sources. Scite requests remain `limit:20`; native Consensus requests remain `page_size:100` when used. Continue useful pages by actual returns and reformulate noisy queries; log unopened continuations and denied routes. Abstract/title screens locate reading candidates and do not establish effect, absence or full understanding. Create/reuse Zotero records before selected reading, preserve preprint types and edition lineage, and report considered decisions once after historical deduplication.

The preceding discovery pass inspected engine-usability/adoption and distributed-state leads and extended the retained practice query through positions 81–100. Broad prefixes were noisy and were reformulated; later pages remain open. The current design pass reuses that evidence and completed reconstructions; it adds no new retrieval/full-reading credit or citation-screen decisions. Neither pass certifies novelty across the agenda. Reopen the closest-source/edition check before a stronger novelty or publication claim.

The October 15 user authorization permits confident local constructions and experiments plus the requested bounded maintainer delegation. Define comparisons, observations and falsifiers before execution and preserve all attempts. Candidate/model experiments, recruitment, new accounts, OAuth staging and H execution remain unallocated; no historical run allowance is reused. Continue consequential literature alongside construction when an exact method, comparator or adverse result can change the design. These updates add no new search or full-reading credit.

## Coverage against the broad survey

| Survey theme | Agenda directions |
| --- | --- |
| B01 Foundations and comprehension | R01, R02, R07, R20, R21 |
| B02 Domain types and evolution | R04, R10, R13, R16 |
| B03 Reactive coordination and lifecycle | R02, R05, R13, R18 |
| B04 Persistent state, effects and history | R03, R06, R09–R11, R18 |
| B05 Game architecture alternatives | R01, R02, R12, R15, R17 |
| B06 Runtime and resource costs | R06, R18, R19 |
| B07 Specification, testing and oracles | R05 and the outcome contract of every empirical direction |
| B08 Debugging and live development | R03, R08, R10, R20, R21 |
| B09 Coding agents and language effects | R04, R08, R09, R16, R21 |
| B10 Maintenance and adoption in practice | R01, R07, R11, R12, R14, R17, R20, R21 |
| B11 Architecture choice and assessment | R01, R02, R06, R15 |
| B12 Empirical and synthesis methods | R05, R14, R21 and the shared study requirements |

Player enjoyment, accessibility, security and resilience may be important requirements or costs within a chosen game/workflow, but no inspected Nu-specific causal mechanism currently justifies standalone superiority studies for them. Promote such a direction when an actual capability, beneficiary and comparison are established. Generic AI game generation, universal language rankings and unrelated hardware leaderboards likewise need a concrete connection to this agenda before they displace its leading questions.
