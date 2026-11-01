# Do explicit domain-case matches improve Codex maintenance of evolving F# state machines?

**Recommendation, 2026-09-16:** select this narrower question for human review; **defer experimental construction and live runs** until the feasibility requirements below are met and separately authorized. The literature supports investigating a consequential convention, not asserting its benefit or firstness. [PLAN](../PLAN.md) owns authority. The [candidate comparison](research-question-discovery-2026-09-16.md), [search and source ledger](literature/question-discovery-sources-2026-09-16.md) and [full-reading index](literature/full-reading/INDEX.md) expose the evidence and its limits.

**Supervisory amendment, 2026-09-30:** retain D1 as a candidate, not the completion criterion for the reopened whole-background survey. The [review](supervisor-review-2026-09-30.md) corrects the treatment terminology, separates diagnostic opportunity from semantic coverage, carries temporal-oracle limits into this proposal, and distinguishes design blockers from legitimate negative outcomes. No construction, compiler probe, candidate run or new allocation occurred in this amendment. The original text is preserved at `f00d98d2e6f8bbe1eda96ffc72d8d3999084f959`.

**Current preparation decision, 2026-10-26:** continue the bounded authored
maintenance question, without claiming a representative population of domain
extensions. The [oracle eligibility audit](nu-r04-oracle-eligibility-audit-2026-10-26.md)
reconciles the completed October 15 compiler and fixed-reference runtime
checks with the remaining evaluator/access dependencies. Those observations
supersede the dated unexecuted descriptions below at their exact scope. The
existing oracle assumes the reference's case, model and control organization;
it is not yet a final scorer for every correct reorganization this proposal
permits. The subsequent [behavioral/compatibility decision](nu-r04-behavioral-contract-2026-10-26.md)
selects ordinary standalone MMCC and the authored pause/progress/lifecycle
requirements, with independent effect observations. It permits different
private state organizations and separates Q2's stronger phase/race requirements.
It also preserves unresolved measurements separately from observed failures.
Ordinary access and evaluator calibration remain unverified. No candidate
experiment, new construction or allocation follows.

## Introduction and practical problem

F# discriminated unions let a program name its domain states. Explicitly enumerating the current cases can make a later added case expose an incomplete match. A catch-all can cover existing and newly added cases without that diagnostic. **Both initial variants may be exhaustive:** the treatment is explicit case enumeration versus catch-all coverage, not exhaustive versus non-exhaustive, typed versus untyped, or correct versus initially defective code. Microsoft's [FS0025 documentation](https://learn.microsoft.com/en-us/dotnet/fsharp/language-reference/compiler-messages/fs0025) gives explicit coverage and a wildcard as alternative repairs; its [pattern reference](https://learn.microsoft.com/en-us/dotnet/fsharp/language-reference/pattern-matching) describes a wildcard as matching any input. These primary semantics were rechecked on 2026-09-30. Neither coverage strategy establishes whether the newly required behavior is correct.

For a maintainer delegating changes to a coding agent, the consequential choice is whether to preserve explicit case handling at domain boundaries, accepting the associated editing and review work, or permit a shared fallback. A new gameplay state can require coordinated changes to movement, time, rendering, input and lifecycle. Some obligations occur in pattern matches; others occur in equality tests, guards or effects that remain type-correct. The useful answer is whether the convention improves complete behavior under ordinary source/tool access, at an acceptable cost, and which obligations it leaves unprotected.

Nu supplies a concrete F# motivation. Its pinned [coding standard](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Standard.md) favors domain types and exhaustiveness where appropriate. In the same revision's [Breakout MMCC gameplay](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Projects/Breakout%20Mmcc/Gameplay.fs), `GameplayState` is explicitly matched during updating, while content uses equality with `Playing` and time is advanced through a separate message. This source combination makes the question concrete; no new state was implemented and no agent failure was observed here. MMCC also performs sound effects during updating, so it must not be described as an entirely pure effect-free boundary.

The [Vsynchronicity essay](https://vsynchronicity.wordpress.com/2026/09/07/simplicity-aware-programming/) and the sibling `nu chat analysis` technical synthesis prompted attention to domain distinctions, state transitions and coordination over time. They are practitioner/derived hypothesis inputs, not controlled evidence of agent performance. Private transcripts are not study data or public exhibits. Public pinned Nu source is sufficient to inspect the motivation.

## Research gap and closest work

The broad claims are already occupied. Type feedback, typed context, functional-language repair, code-organization experiments and multi-file propagation have substantial prior work. The proposed residual contribution is **a controlled estimate of the behavioral and resource consequences of one existing source convention during later domain changes**, including cases where its additional diagnostics are unhelpful. A different language or model alone would not justify the study.

| Closest evidence | Purpose/mechanism/evaluation | Consequence for this proposal |
| --- | --- | --- |
| [P08, Type-Error Ablation](literature/full-reading/P08-type-error-ablation.md), arXiv 2606.01522v2 | Agent repair of selected single type faults in ten Shplait programs; diagnostic-detail interventions, dynamic test feedback and substantial conditional reversals | Do not claim first type-feedback benefit or universal improvement. New obligations and independently withheld final behavior are needed; its effect sizes do not calibrate this study |
| [S35, Typed Holes](literature/full-reading/S35-typed-holes.md), DOI 10.1145/3689728 | Types, relevant headers and error rounds for missing update functions in five MVU applications; behavioral tests, competitive exhaustive context and adverse header cases | MVU, sum types and behavior-tested type context already coexist. The comparison here concerns assigned source conventions during changes, with full source available to both arms |
| [P03, Code Cleanliness](literature/full-reading/P03-code-cleanliness.md), arXiv 2605.20049v1 | Behaviorally checked source transformations followed by coding-agent tasks; bundled organization changes, partial test scores, heterogeneous costs | Source-convention experiments are established. Isolate the declared contrast, retain regressions and adverse cases, and avoid resource-outlier or success filtering |
| [S34, FPEval](literature/full-reading/S34-functional-programming.md), arXiv 2601.02060v1 | Functional-language initial generation and repair; tests plus static style metrics; repair advice permits missing cases or a catch-all | First functional repair and lint-based maintainability claims are unavailable. Catch-alls are a possible valid repair, not a failure label |
| [S36, TRACE](literature/full-reading/S36-trace-subsequent-edits.md), DOI 10.1109/ASE63991.2025.00117 | Learned/LSP subsequent-edit propagation, reference-edit simulation, and a separate human study with task-dependent winners | Static location support does not settle semantic edits. Evaluate actual autonomous outcomes, retain failed patches, and do not insert reference edits into candidate runs |
| [S37, Haskell Refactoring](literature/full-reading/S37-haskell-refactoring.md), DOI 10.1007/978-3-032-12089-2_26 | Bundled agent refactoring already recommends exhaustive cases; before/after static/runtime metrics, with incomplete released verification provenance | The convention is prior advice. Its incremental value for later behavior remains a question; aggregate quality improvements are not a maintenance effect estimate |

The repository records all six papers as fully read at their stated edition/coverage; the supervisory amendment reuses those records, not a new full-PDF recertification or experimental reproduction. The discovery ledger also records abstract-only constrained-decoding and dependency-repair leads. Those different mechanisms prevent claiming first type-related semantic reliability; they are not established replications of the proposed contrast. Scite's useful functional-programming branch was paginated, and direct/citing methods were checked, but large noisy result sets and sparse citation graphs leave priority uncertain.

The later [S72 reconstruction](literature/full-reading/S72-functional-programmer-authoring.md), DOI `10.1145/3485532`, supplies direct human reports of wildcard conventions and new variants taking old fallback paths. It also distinguishes deliberately eliciting compiler guidance from accidental failures. Its quantitative comparison is pattern matching versus combinators, not this source treatment; it does not establish an F# coding-agent effect or convention prevalence. This strengthens the practice motivation while narrowing novelty, and failed build counts alone must not be called wasted work.

The [S216 reconstruction](literature/full-reading/S216-united-constructions.md), DOI `10.1145/3331554.3342607`, supplies a further type-system boundary: its core calculus gives a default branch the residual union type and equality evidence after a failed tag test. Catch-all syntax therefore does not universally imply loss of type information. This is a language/semantics construction, with formal cast erasure and a sketched relative-consistency argument, rather than an F# maintenance comparison. It neither determines the required behavior of a future case nor changes this proposal's fixed-toolchain contrast; both D1 baselines may remain exhaustive and a correct default remains valid.

The [S217 reconstruction](literature/full-reading/S217-dependent-copattern-elaboration.md), DOI `10.1017/S0956796819000182`, further separates coverage and core typing from preservation of ordered source-clause semantics. Its dependent-language construction can expand a compact catch-all into many correctly typed branches, while the reported implementation retains extra checks for interactive holes. These are elaboration and editing mechanisms, not evidence of an F# defect or a measured convention effect; source-clause count, generated branches, diagnostics and behavioral obligations remain different quantities.

## Question, scope and useful implications

**For bounded domain-state changes in existing F# applications, does starting from explicit enumeration of current domain cases, compared with an initially behaviorally equivalent catch-all convention, increase the probability that a fixed Codex coding-agent policy satisfies every new and retained behavioral obligation within the same resource allowance? Where do obligations outside those matches remain unsatisfied?**

The first target is a Nu-grounded feasibility case, not a comparison of Nu architectures or a language leaderboard. A contribution would be conditional practice guidance: when explicit case handling earns its maintenance cost, when a valid default suffices, and where independent behavioral verification remains necessary. A precise null or adverse result would also change that decision. It would not show that F# is intrinsically superior, that the model understands a state machine, or that compilation proves correctness.

The beneficiary is an F# maintainer setting a source/review convention for agent-assisted changes. Importance is supported by an existing public convention, concrete state-dependent responsibilities in Nu, and the closest studies' conditional outcomes. Frequency across industrial F# projects, willingness to pay the extra review cost, and the magnitude of any benefit are **not yet established**. Do not promise adoption or positive return on effort from this literature review.

## Proposed methodology

### Units, source contrast and tasks

Use two initial variants of the **same** pinned F# implementation. Preserve APIs, engine, dependencies, initial behavior, names, comments, helper organization and runtime facilities as far as the convention permits. In one variant, enumerate the existing domain cases at specified match sites; in the other, use a semantically appropriate fallback for the corresponding existing cases. Verify initial observational equivalence with common tests and source review. Record unavoidable token/branch differences. The primary estimand is the **total effect of that source convention**, including its information and diagnostic consequences; it does not isolate a pure compiler-information effect.

Do not use existing MMCC versus ImSim as these two arms. The fully inspected Breakout gameplay files differ in manual versus engine physics, lifecycle/API use and other implementation choices. Sharing F# and Nu does not control those differences.

Define change families from requirements before candidate outcomes. Include added domain cases requiring distinct behavior, cases for which an existing default remains correct, and matched changes that do not alter the union. Include coordinated temporal/lifecycle obligations not entailed by case coverage. Do not select final tasks because a preliminary model run showed an advantage. Separate development examples from evaluation families; cosmetic variations of one task are not independent evidence. If only one application/family is feasible, label the result a local case, not a general convention recommendation.

### Diagnostic opportunity is not semantic coverage

Establish the treatment at the **source-site** level, separately from the **behavioral-obligation** level. The selected source site now has actual-project compiler evidence and fixed-reference runtime observations. Other sites, ordinary candidate delivery and broader valid implementations still need their own evidence; the completed checks do not authorize new probes.

For each targeted site, record the original cases/payloads/guards, equivalent branches, why a fallback is legitimate in the original domain, and the fixed compiler/warning policy. Both variants must satisfy the original contract; do not insert a present-day bug into the fallback arm. Prefer minimal source transformations and shared branch bodies where appropriate rather than gratuitously duplicating implementation. Record unavoidable source-size differences; do not force token equality.

An evaluator-side type-extension probe, when separately authorized, can establish whether an otherwise unhandled added case produces a diagnostic at a particular site under that pinned toolchain. It is not the candidate task, a reference patch to inject into candidate runs, or a way to retain only tasks whose measured agent outcomes favor enumeration. Record warning versus build failure accurately. Do not silently suppress warnings in one arm or promote them to errors in another.

Maintain an independent requirement-to-observation map for movement, rendering, time, lifecycle or other actual obligations. A diagnostic may identify a place to inspect, but it does not specify the correct transition, side effect or deadline. A correctly typed exhaustive branch with the wrong behavior is an important oracle fault; a correct catch-all is an important valid alternative. One site can affect multiple obligations, and one obligation can depend on several sites. Do not equate diagnostic count with requirement count.

Report separately what the controlled probe predicts, which diagnostics the actual agent generated, and which tool output was actually returned to it when observable. Unobserved attention or comprehension remains unobserved. Conditional analyses of diagnostic-receiving runs are descriptive, not the randomized source-treatment estimate. A later pure diagnostic-information intervention would be a separate study, not an automatic extra arm here.

### Source preparation addendum, 2026-10-11

The [existing-site and policy audit](nu-comparator-and-convention-audit-2026-10-11.md#r04-an-authentic-existing-source-site) makes the original Breakout motivation reviewable at one exact match. Its final shared `Playing`/`Quit` identity branch has a source-level argument for a currently equivalent wildcard; neither arm was constructed. The checked-in Debug/Release policy does not suppress FS0025 or explicitly promote it to an error, while inherited properties remain possible. Floating `10.x` CI and an FSharp.Core package version do not freeze the compiler. Carry the warning-only expectation forward provisionally; any common change to severity must be declared before outcomes and validated under separate authorization.

The addendum supplies researcher-authored serve preparation, pause/resume and alternative-control sketches. Serving needs distinct update behavior; paused simulation can correctly use the identity default while content, clock and lifecycle obligations remain elsewhere; alternative controls leave the union unchanged. They are source-grounded options, not mined requests or three independent applications. Their diagnostic and behavioral records stay separate. Broader task provenance, initial equivalence, actual warning delivery, oracle sensitivity and every allocation condition below remain outstanding.

The [task-diversity continuation](nu-task-diversity-and-common-requirements-2026-10-11.md#r04-an-additional-authentic-convention-site) adds Blaze Vector MMCC's existing BulletCommand match. Its final Penetration/destruction arm has a source argument for an initially equivalent catch-all; no variant was constructed. Authored lifetime-renewal, cancellation and unchanged-case-set alternatives expose distinct versus valid default behavior and temporal/identity obligations. The checked-in warning policy matches the Breakout sheet. This broadens source/application coverage within Nu's demo lineage, not representative sampling or independent evidence; the MMCC/ImSim pair is not substituted for D1's arms. All feasibility, provenance, practical-value and allocation conditions remain.

### Historical requirements and valid alternatives, 2026-10-26

The [R04 source-history audit](nu-r04-history-task-audit-2026-10-26.md) qualifies
both real API-rename examples: the extra named-handler edit follows only when
the application-local case must also be renamed. Updating an external event
subscription can retain the old local case name. Record the actual contract,
ownership and reason for any naming requirement before task construction;
do not reject a behaviorally correct alternative because it differs from the
historical patch. Source edit counts alone are not maintenance work estimates.

The same audit retains genuine no-extension changes, no authenticated
projectile case-extension request in the inspected history, and a score
feature patch whose state scrutinee changes in a later revision. Serve,
renewal and cancellation remain authored questions. Preserve that status,
intermediate source and follow-up corrections; independently validate any
reference solution and retained obligations. A bounded authored experiment can
still answer its conditional question, but neither demo history nor a successful
compiler probe makes its workload representative. Candidate execution remains
unallocated and existing model/storage/returned-gate restrictions remain.

### Candidate policy and information

Pin the Codex CLI, returned model identity, settings, source snapshot, .NET/F# toolchain, dependencies and environment. Give each run a fresh isolated workspace/context, the same behavioral request, available current source, documentation and existing public tests. Allow the same ordinary source navigation, build/test feedback and bounded repair opportunities in both arms. Freeze compiler flags, including warning severity; do not turn warnings into errors after seeing results. An agent may use another correct organization or a catch-all. Preserve the assigned arm in analysis and record resulting changes descriptively.

Agents must not see the alternate arm, research predictions, reference patches, hidden evaluation cases or comparative outcomes. Within-run public test feedback is allowed by the proposed policy; held-out final scores never feed repair, stopping or sample extension. This proposed tool/repair policy differs from some historical ISE no-tools/no-repair packets and therefore needs its own approval. It is not retroactively applied to old data.

### Reference standard and outcomes

Before model evaluation, establish a common behavioral contract and an independent final oracle. Cover initial regressions, new behavior, relevant event ordering, repeated transitions and forbidden side effects where the requirement demands them. Validate the oracle against reviewed reference implementations, plausible faults and at least one alternative correct implementation. Count no extra credit for matching a reference patch. Faults must test obligations, not enforce source style. Keep test-author access and development/evaluation boundaries explicit.

The [current eligibility audit](nu-r04-oracle-eligibility-audit-2026-10-26.md)
identifies an additional acceptance requirement: the published explicit/wildcard
pause references share the same `Paused` case, typed model, controls and local
pause schedule. They establish the clause comparison's fixed observations,
not compatibility with all admitted source organizations. For the authored
behavioral request, allow a correct strategy that does not add a union case;
do not filter out that assigned attempt because it lacks a diagnostic. If a
public type/interface extension is itself required, state its owner and
compatibility reason before outcomes. A future evaluator must validate an
appropriate alternative organization and distinguish an interface mismatch
from a demonstrated behavioral failure. Keep the frozen probe unchanged.

The primary outcome is **all-obligation success for the assigned change within budget**, requiring the applicable old and new checks under the declared observation contract. This is oracle-relative success, not proof of all possible executions. Report partial obligation coverage separately. Also report compilation/diagnostic status, new failures versus retained failures, elapsed time, every attempted token debit and review-relevant patch size. A correct fallback is a success; clearing a warning is not automatically one. Infrastructure-blocked observations, time-budget exhaustion and unrun slots are distinct, under rules frozen before evaluation. Do not exclude slow or noncompiling candidates after assignment.

For the current authored R04 preparation, follow the
[completion and missing-observation rule](nu-r04-behavioral-contract-2026-10-26.md#completion-and-missing-observations).
Verified completion, an observed required failure and an unresolved outcome
are distinct. Keep all assigned attempts; an unsupported evaluator interface
is neither completion nor a demonstrated semantic defect. Report logical
missing-outcome bounds separately from eventual sampling uncertainty. These
rules do not make an ineligible or systematically biased evaluator acceptable.

Classify diagnostic opportunities at source sites and behavioral obligations independently, as above, before model results. Do not call an obligation "compiler-verified" because an associated site emits FS0025. Their association is explanatory evidence; do not condition the primary effect on successful compilation or adjust it for post-assignment diagnostics, edits or repair counts. Those may be mechanisms through which the source convention acts.

### Temporal observation and vacuity controls

The full-reading records for [S47](literature/full-reading/S47-frp-runtime-verification.md), [S53](literature/full-reading/S53-asynchronous-frp-testing.md) and [S100](literature/full-reading/S100-live-model-checking.md) motivate explicit temporal boundaries. Carry their lessons into the future oracle rather than merely accumulating related citations.

For every temporal obligation specify its trigger, permitted observations, clock/event-order convention, finite horizon or deadline when applicable, environment/reset assumptions and pending work at the start. A bounded response deadline is a particular requirement, not an arbitrary timeout substituted for unbounded eventual progress. A finite run without a counterexample is not a general liveness proof. Unknown/inapplicable/blocked observations stay distinct from a demonstrated pass.

Test the monitor itself with reviewed satisfying and violating traces, including an absent trigger, a wrong event order, a delayed or cancelled action and a pending pre-checkpoint obligation where relevant. Require trigger/exercise evidence for obligations used in the success endpoint. If the program violates a required transition or reachability condition, score that failure; if the evaluator simply never establishes the applicable observation, do not grant vacuous completion credit. Failure-sensitive checks should not require a single reference implementation or reuse the candidate's own logic as the only oracle.

D1's proposed fresh-workspace tasks do not perform live migration. Do not import a live checker, graph-history engine or arbitrary snapshot state merely because S100/S101 describe one. If a later protocol starts from a runtime checkpoint, it must explicitly initialize the required monitor history or use a justified sufficient state; observing only the present values does not preserve every outstanding obligation.

### Uncertainty, cost and interpretation

Run both source conditions on each evaluation task, with randomized/interleaved dispatch order and independently fresh agent runs. Task-family/application clustering, not the number of API calls or test assertions, determines generalization. Prespecify the paired task-level success difference, task/family weighting, interval procedure, handling of missing observations and limited secondary comparisons. Repetitions estimate executor variability; they do not create new change families. Do not use unpaired participant tests from TRACE or prior studies' selected effect sizes as a power calculation.

Choose a smallest worthwhile improvement and acceptable cost with the intended maintainer before allocating runs. Model-free precision/sensitivity calculations should then determine how many independent families and repeats the intended claim needs. If feasible family counts cannot support useful uncertainty bounds, reduce the claim to descriptive feasibility or defer it. There is no sample allocation in this proposal, and the historical 192+5 cannot supply one.

Measure one-time source preparation/review separately from per-change execution cost. A fixed agent-budget comparison estimates quality under that budget; it does not establish overall budget superiority. Any claim that saved review effort is better spent on additional tests would require an explicitly designed comparison, not an assumed benefit.

## Feasibility, validation requirements and stopping decision

The existing `src/ise/agents/codex.py` integration is the intended reuse path, not a newly validated runtime in this supervisory pass. Before any separately approved experiment, reconcile the pinned CLI's actual event schema, warning/output delivery and usage fields using the approved model-free and integration boundaries. This review ran no adapter, compiler or live model request and establishes no current backend compatibility. Do not change OAuth/backend choices or quietly launch a diagnostic call.

The completed [application builds](nu-application-diagnostic-feasibility-2026-10-15.md)
establish warning-only FS0025 at the selected site. The
[pause runtime record](nu-pause-runtime-feasibility-2026-10-15.md) establishes
matching bounded baseline/successor observations and sensitivity to five
declared faults under functional accompanied Gaia. Preserve all preparation
and reconstruction failures. These resolve the corresponding earlier probe
questions, not ordinary physical input, standalone transitions, candidate
access, general equivalence or maintenance benefit.

The [common behavioral/compatibility boundary](nu-r04-behavioral-contract-2026-10-26.md)
now selects standalone MMCC, ordinary input and the authored pause/resume,
retained-progress, quit and fresh-play family, including independently observed
effects. It is not an authenticated request or a frozen candidate prompt. Next
establish an evaluator that admits the permitted alternatives under actual
ordinary access; the accompanied probe does not validate the selected
standalone environment. Source-convention assignment remains the treatment
even when the candidate reorganizes the successor. Enough independent changes for a broader
claim, actual tool/observation access and credible effort/precision requirements
remain unresolved. If those conditions require a substitute engine or a
task-solving observation seam, defer the Nu case rather than mislabeling the
fixed probe as an ordinary maintenance study. Current storage/model restrictions
and returned construction gates remain in force.

Separate design feasibility from what a completed experiment finds.

**Before a confirmatory run, narrow, adapt as an explicit replication, defer or redirect when:** closer methods occupy the same estimand; source equivalence requires material unrelated changes; the sampling frame cannot support a relevant convention decision; or adequate temporal observation, valid alternatives, task diversity and accounting cannot be established within justified resources. A non-counting development pilot may inform a later preregistered design; preserve it and label resulting changes. Do not select evaluation tasks for favorable observed effects.

**After an authorized frozen study, retain and report its outcomes:** additional diagnostic/editing work without worthwhile behavioral improvement, a precise adverse effect, or evidence that a default remains sufficient are legitimate results. They may justify not investing in the convention under that ecology, but not discarding the study, replacing tasks until enumeration wins, or retrospectively changing its endpoint. An imprecise null is inconclusive, not equivalence. Saturated correctness limits that endpoint; any cost comparison must keep its predeclared role, not become the primary result opportunistically.

A local effect remains conditional on the implementation, task families, model and tool policy. The original language/context or Nu-wide benefit hypothesis is neither validated nor refuted by this one convention contrast.

## Three-criterion judgement

| Criterion | Answer at this handoff | Condition still required |
| --- | --- | --- |
| **Unique — Scite** | **Unconfirmed.** No exact duplicate was identified in the recorded screen; closest full methods leave a narrower empirical contrast. Exhaustiveness, type feedback and source-organization evaluation are established | Bound priority to this search. Follow any newly consequential duplicate; do not interpret unexamined records or low graph coverage as absence |
| **Valuable** | **Plausible, concretely motivated.** The result could change an F# maintainer's convention and verification effort, including a useful negative answer | Validate task prevalence, worthwhile effect and effort with the actual use case; no benefit or return is yet measured |
| **Scientifically valid** | **Proposed design with bounded feasibility evidence.** The selected warning contrast and fixed-reference observations/fault detections are established; no candidate maintenance study is validated | General equivalence, an evaluator compatible with admitted alternatives, ordinary access, accounting, task diversity and allocation remain unresolved |

**Disposition: retain D1 as a bounded authored maintenance question; candidate
execution remains unallocated.** The completed mechanism checks are evidence
at their stated scope, not human approval, maintenance benefit or representative
workload coverage. Follow PLAN for current local-construction authority,
storage/model restrictions and returned gates; the historical blanket worker
hold does not override authorized maintainer assistance. New candidate,
participant, paid and H allocation is zero.
