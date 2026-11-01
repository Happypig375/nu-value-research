# Study designs for Nu mechanisms, costs and bounded agent maintenance

**Design packet, 2026-10-08.** Implements the [continuation plan](nu-research-continuation-plan-2026-10-08.md) and the leading R01–R06 directions in the [agenda](nu-research-agenda-2026-10-08.md). These were proposed comparisons and observation specifications at the October 8 preparation checkpoint. [PLAN](../PLAN.md) owns the subsequent authority changes.

**Current status, 2026-10-15:** the user has since authorized confident local construction and experiments. The [agenda's current readiness table](nu-research-agenda-2026-10-08.md#readiness-and-next-actions-for-all-directions) links the completed bounded mechanism, lifecycle, diagnostic, oracle and cost evidence and supplies its consequences for the next actions. It supersedes this packet's October 8/11 statements that those particular checks are unexecuted or held. The comparisons and accounting below remain proposed research designs; no candidate maintenance or human benefit study has been completed or newly allocated.

Human-steered development is the intended eventual use context. Near-term claims concern inspected mechanisms, their behavior/costs, and specified agent tasks. Steering effectiveness is deferred as R21; human-only and agent-only extremes are optional reference cases when they answer a concrete question. This packet does not introduce equal human/agent/team arms or assume a 2027 market distribution.

**2026-10-19 comparison objective:** apply the [updated agenda](nu-research-agenda-2026-10-08.md#2026-10-19-objective-improve-evolution-of-stateful-software)
when turning these designs into a practical intervention study. Establish the
relevant status quo and intended improvement; trace consequential development
history alongside literature methods. Nu-specific feasibility, comparative
benefit and transfer to non-game stateful systems remain separate claims.
This update changes no frozen protocol, observation or resource allocation.

## Evidence and source basis

The reused Nu source basis is **064f7ae92a8506689cd91aff5e6804a375d6ef3d**, as inspected in the [source ledger](nu-grounded-maintenance-sources-2026-09-14.md) and [methodology](nu-grounded-maintenance-methodology-2026-09-14.md). The original design pass reused those records. The [2026-10-11 source audit](nu-source-contracts-and-scenarios-2026-10-11.md) now directly traces selected pinned code and public maintenance history; it does not refresh current Nu HEAD, run code or add primary-paper readings. Its narrower contracts below supersede the earlier unresolved source leads.

| Source-supported starting point | Consequence for the proposed comparison | Still to establish before execution |
| --- | --- | --- |
| MMCC and ImSim empty templates and Breakout examples exist at the pin. | Use legitimate within-Nu organizations as R02 candidates. | Initial observations, supported requirements and a credible comparison boundary; the empty templates are not matched games. |
| ImSim Breakout uses physics-body/collision results; MMCC updates coordinates and tests intersections explicitly. | Primary R02 attribution is to the selected packages. | Whether a narrower responsibility contrast can be isolated without destroying either idiom; intended gameplay parity is not a test result. |
| Gaia retains world roots; functional/imperative update paths and shared subsystem references are inspected. | Separate root retention, native reconstruction and user-owned mutable data in R03/R06. | Snapshot-safe application data, closure contents, native continuation and measured costs for the selected task. |
| Gaia snapshots editor operations and advance/halt/step; undo/redo require functional mode. | Represented gameplay recovery is a concrete R03 capability. | Supported same-code continuation and actual agent access; arbitrary external-effect rollback and code migration are not established. |
| Event publication, result consumption, monitors, ImSim sweeping and frame ordering are inspected. | R02/R05 specify actual delivery/lifetime/phase boundaries. | Exercised observations, identity reuse and task-specific multiplicity; event organization alone does not establish event sourcing. |
| Nu #1145 and commit d3b4824 link a transition/pause defect to the existing ImSim Breakout quit guard. | Use verified practice lineage for an adapted coordinated-change requirement. | A fresh assigned change and comparable initial behavior; the historical guard is already present at this pin. |
| A stub-world test initializes a world and a one-frame run. | There is a source lead for later observation feasibility. | A working environment and a sufficient observation interface; no headless candidate sandbox has been validated here. |

The linked ledger supplies exact pinned source locations. Reinspect those locations for a specific unresolved contract rather than treating a generated account or old description as current implementation truth. Record a new pin and its relevant differences before transferring this design to another revision.

## Shared design and accounting contract

### Units, comparison and initial information

An **obligation** is a required observable behavior; a **task** is one assigned change; a **family** groups tasks with the same substantive demand; an **application** supplies a starting program. An **attempt** is one independently initialized agent execution on a task/arm. Cosmetic variants and repeated calls do not create new families or applications.

For R02/R04 and any promoted R03 agent comparison, propose paired tasks on the two eligible arms, independently fresh workspaces/contexts and randomized or interleaved execution order. Keep source revision, model identity/configuration, environment, intended requirements, feedback and resource rules explicit. Do not supply the other arm, comparative predictions, reference solutions or final scores. This is a future policy specification; it does not modify or execute historical no-tools/no-repair protocols.

The default proposed agent policy permits ordinary source navigation, existing documentation and declared build/development-test feedback within a common fixed resource allowance. R03 additionally needs the exact history/inspection interface that defines its treatment. A source-only agent condition cannot silently inherit GUI access or a task-solving helper. Current runner/backend decisions are retained; compatibility and observation access are later feasibility dependencies, not reasons to create a new adapter now.

The [R08 information/feedback contract](nu-agent-information-and-feedback-contract-2026-10-11.md) now audits that compatibility boundary. The retained E3a controller uses inline source, no candidate tools, restricted full-file replacements and visible replay; it does not implement this proposed ordinary-tool workflow. Its diagnostic sorting/deduplication is not an established temporal-trace format, and its post-controller scores share the remaining trajectory deadline. The proposed Nu studies must preserve ordered behavioral observations and give independent final scoring a separate resource boundary. Actual tool/edit/observation authority needs a separate workflow/feasibility decision; no frozen protocol or backend is changed.

Requirements must precede candidate outcomes. Keep the desired behavior independent of a preferred patch and permit valid reorganization, helper extraction and catch-alls. Record initial information, including whether a failing entity/event is identified. Subsequent diagnostics, edits and tool usage can explain an outcome; do not adjust them away to label the remaining difference a pure source effect.

### Task provenance and convergence risk

The [R14 practice/task record](nu-practice-and-task-provenance-2026-10-11.md) now maps these and later cases to their source lineage, beneficiary, omitted work and eligibility requirements. Preserve corrected reports and the distinction between public need, current implementation and authored task. The current frame is purposive; many issues share one maintainer and do not establish independent user demand. Existing default-asset automation and customization/derived-asset work supply a conditional total-work extension. They do not add an experimental arm or validate a new task.

The following are **requirement sketches**, not mined issues, authored successors, approved benchmark tasks or a claim of current Nu support for every operation.

| Family | Proposed requirement and old behavior to retain | Contrast or counterexample it can expose | Provenance and limit |
| --- | --- | --- | --- |
| F-local | Change a local control's condition/response while keeping unrelated controls and screen transitions correct. | Locality may help; implicit evaluation order or identity may hurt. | Pinned control sites and S67's trade-off; L-control remains authored, while verified #785 is a separate editor focus case. |
| F-lifecycle | Change pause/resume or parent/child creation/removal while preserving ownership, pending actions and repeated transition behavior. | Explicit coordination may help; extra propagation may omit a required transition. | Nu #1145 grounds the adapted C-exit requirement. Its pause/exit policy is now specified; task eligibility, input/observation access and proposed deadline validation remain outstanding. Other sketches and S291–S299 retain their scope. |
| F-burst | Apply multiple eligible events under a stated rule for ordering, multiplicity and side effects. | Coherent processing versus fan-out/duplicate work; the requirement must decide what is permitted. | Event-graph and fan-out accounts; do not invent a universal exactly-once contract. |
| F-domain-distinct | Add a domain case that needs distinct behavior, retaining old-case semantics. | Useful diagnostic opportunity versus compiler-silent wrong behavior. | D1 and the type-evolution readings; not a favorable-agent-outcome filter. |
| F-domain-default | Add a case legitimately covered by the existing fallback, plus a change that does not extend the case set. | Enumeration can add work without behavioral benefit; correct defaults remain successes. | D1's adverse/control cases and S72's convention evidence. |
| F-history | Revisit a reproducible failure and repair it, with the failing entity either identified or initially unknown. | History can expose causes or add setup/navigation cost. | S42's information-dependent reversal and S66/S296/S297; no Nu effect inferred. |
| F-effect | Recover represented state around a permitted reversible operation and around an operation whose effect cannot be undone. | Stored values may be insufficient for correct continuation. | S235's restricted compensation and S107/S296/S297 contracts; unsupported operations define a boundary, not automatically a Nu bug. |

These families guide coverage and do not impose an all-factor experiment. Before execution, each selected task needs an exact requirement source, application/pin, initial contract, exercise conditions, observation map, strongest rival and reason for inclusion. The [source audit](nu-source-contracts-and-scenarios-2026-10-11.md#verified-practice-lineage-and-proposed-requirements) distinguishes L-control (source-grounded authored), C-exit (practice-grounded adapted) and the historical #1145 repair lineage. A verified issue/patch is not automatically an eligible task: the current pin contains its workaround. Other sketches remain illustrative; no matched task pair is validated.

The maintainer should challenge redundant families and include cases favorable to either alternative before observing candidate results. Record actual user/practitioner input separately from AI synthesis. Another agent response or a request for diverse ideas is not independent review or evidence of coverage. Characterize repeated solution patterns only from observable edits/trajectories under a declared coding scheme; do not infer hidden reasoning. Broad transfer requires additional applications/families or later executor replication, not simply more calls on one puzzle.

### Outcome, missingness and costs

The main agent endpoint is **all required old and new obligations satisfied within the declared allowance**, relative to a validated observation contract. Report new/retained obligations separately as secondary outcomes. Successful compilation, a supplied test pass or a matching screenshot is insufficient by itself. Finite observations warrant only their declared scope.

Record eligible assigned attempts, valid completions, demonstrated failures, budget exhaustion, infrastructure-blocked/inconclusive observations, policy deviations and unexecuted planned slots separately. All assigned attempts stay in the disposition table. For the decision endpoint, an assigned attempt without established success receives no completion credit; distinguish its reason and bound conclusions when infrastructure missingness could change the contrast. Do not label an unevaluated attempt semantically incorrect. Never select the main timing sample using only successes.

Human operational intervention and rescue must be logged if later execution encounters them. Keep the original assigned outcome; a rescued patch cannot replace it. A separate assisted follow-up requires its own declared scope. Test authors and any actual reviewers must be identified honestly; a specification written by this maintainer is not human sign-off.

For a later sequence extension, the [R09 contract](nu-change-sequence-contract-2026-10-11.md) deliberately inherits each stage's submitted workspace, unlike the independently initialized single-change design. It fixes conversation/environment and feedback policies separately, versions active/retired obligations, and distinguishes inherited failure, new regression, recovery and unknown observations. Intermediate delivery and final cumulative correctness are different endpoints. This is a proposed extension with its own feasibility/allocation gate, not a change to historical protocols or current execution authority.

| Quantity | Accounting rule |
| --- | --- |
| Agent resources | All attempted model/tool work under the pinned accounting rule, including failed repairs; keep tokens, tool time and priced expenditure distinct. |
| Elapsed time | Assigned start through stop, including execution and permitted feedback; distinguish infrastructure waiting. |
| Preparation/integration | Record one-time source, instrument, oracle and tool setup separately from per-task work; do not hide it in an adapter. |
| Runtime cost | Matched workload, environment and useful work; include retention, disposal/rebuild and relevant host/native work. |
| Human effort | Only actual observed preparation/review/rescue time if collected under an approved method; no productivity estimate from patch size or agent elapsed time. |

For paired agent outcomes, prespecify the task-level success contrast, within-family aggregation, family weighting and planned family interaction before execution. The default descriptive target is the declared task portfolio with equal weight per substantive family and equal weight per selected task within family; repetitions estimate each task/arm's stochastic performance. This is not an industry frequency estimate. A single Breakout pair remains a local case. An inferential extension must justify independent clusters, an uncertainty procedure and precision; repeated frames or calls cannot supply missing applications. No interval, sample size, worthwhile effect or allocation is invented here.

Readiness requires the intended maintainer's practical decision threshold, an acceptable resource boundary, and a model-free sensitivity/precision justification at the actual unit. If the feasible units cannot support that claim, publish descriptive feasibility or narrow the claim. Preserve all E/H results; no historical result is rescored by these endpoints.

## R01 — Whole workflow value

**Question and beneficiary.** For a maintainer considering Nu for interactive software, which verified development capabilities and costs could justify adoption, and what evidence would establish net value? Human-steered work is the future practical target; this phase prepares the package comparison and its missing evidence.

**Candidate comparison.** Nu's documented workflow versus ordinary Godot remains the leading package candidate, informed by [S67](literature/full-reading/S67-pronto-game-prototyping.md) and [S296/S297](literature/full-reading/S296-S297-state-exploration-and-live-replay.md). The [2026-10-11 comparator inventory](nu-comparator-and-convention-audit-2026-10-11.md#r01-version-and-package-boundary) provisionally pins Godot 4.7.2-stable and its GDScript desktop workflow, with a separately pinned documentation snapshot. Include its ordinary debugger/evaluator, remote inspection, scene/script synchronization, profiling and programmable undo/copying facilities. C# has a different build/tool/state-preservation boundary and needs a separate inventory if selected. Neither current research-plugin compatibility nor runtime/agent access is verified. A mature Unity workflow remains conditional on a better task fit and a reason recorded before outcomes.

**Tasks and information.** Start from F-local/F-lifecycle and, if both packages support it, F-history, using independently stated requirements and native idiomatic facilities. Match intended behavior and accessible documentation/resources, not source layout or forced transliteration. Account for setup, learning, integration, support and recovery. Do not assemble a whole-workflow score by combining unrelated papers or agent-only tasks.

**Outcomes and rivals.** Verified completed changes, total work and relevant runtime cost; favorable Nu mechanisms can be outweighed by unfamiliarity, missing integration or expensive retention. Package differences include language, tools and ecosystem support, so a package result does not isolate immutability. Human-active effort and steering quality remain unmeasured until an appropriate participant/observation design exists.

**Evidence consequence.** S67 supports useful interface trade-offs with limited human evidence; S296 supplies state-navigation benefits and significant isolation costs; S42 supplies an initial-information crossover. [S229](literature/full-reading/S229-picoscenes-expert-ai.md) supplies a favorable expert–AI workflow with allocation/accounting limits. Preserve these positives without importing their effect sizes into Nu or treating their task/sample definitions as interchangeable.

**Disposition and next action.** Conditional package proposal; human net-value estimation deferred. The [task/common-requirement audit](nu-task-diversity-and-common-requirements-2026-10-11.md#r01-common-package-requirements-and-an-ordinary-alternative) grounds a bounded platform interaction in Nu #1020 and credits ordinary Godot character/platform facilities. The [platform contract](nu-platform-contract-2026-10-11.md) now selects an ordinary dynamic/kinematic Nu route for review and states fixed-gravity carrying, jump/departure, pause, removal and cue semantics, with proposed scale/timing parameters. Dedicated character modes require explicit capsule/pogo configuration; existing gravity-relative code prevents an absence claim based on old issue status. Actual carrying, phase-correct observations and tool access await separate feasibility authority. Count each package's integration/setup work. F-history remains conditional on its own state/effect boundary. Redirect if matching needs an artificial weak baseline or an unavailable engine facility; neither source capability nor agent outcomes establish human productivity. A stronger novelty/comparator check remains necessary before a publication-priority claim.

## R02 — Ownership and temporal coordination

**Question and contrast.** Under a fixed agent policy and allowance, do the pinned Nu MMCC and ImSim packages differ in verified completion of local and coordinated changes? Compare the existing credible styles; sharing F# and Nu does not isolate responsibility organization because physics/collision and API use also differ.

**Source and task contract.** Use F-local and F-lifecycle as the initial planned strata; F-burst is promoted only when its event rule and common observations are source-bound. For each task specify the state owner, identity creation/destruction, order of reads/updates, event delivery, pending work, cancellation and external effects. Name initial observations required in both arms. Numeric motion/collision equality cannot be assumed; if the desired common contract depends on it, validate that contract later or narrow the selected behavior without hiding the package difference.

The [C-exit/Q2 contract](nu-pause-exit-contract-2026-10-11.md) supplies the first coordinated case's input, deferred-pause boundary, allowed UI/effects, quit precedence and fresh-play policy. It selects standalone imperative/static timing and permits local pause mechanisms. Preserve the existing ImSim quit guard as a package difference. Common initial behavior, actual input/phase access and the proposed deadline/watchdog still need feasibility evidence; editor quick-cut success would not validate this standalone case.

**Two-sided predictions.** Explicit transitions may help coordinated obligations and create extra propagation failures. Nearby interaction processing may help local edits and increase ordering/identity sensitivity. Prespecify this local/coordinated contrast before outcomes. Patch spread, messages added and architectural drift are explanatory observations; a safe implementation in either style passes.

**Evidence and outcomes.** [S39](literature/full-reading/S39-reactive-comprehension.md), [S40](literature/full-reading/S40-reactive-api-usability.md), [Ceptre](literature/full-reading/S291-S293-ceptre-resources-and-editor.md), [S298](literature/full-reading/S298-interaction-typing.md) and [S299](literature/full-reading/S299-modular-reactive-verification.md) motivate explicit interaction boundaries without proving a Nu benefit. Use the shared all-obligation endpoint and resource accounting, with the predeclared family contrast. Unknown initial equivalence and physics/API differences bound causal interpretation.

**Feasibility requirements.** An exact two-arm initial-contract sheet; source-grounded task provenance; exercised independent old/new observations; reachable environments; fixed warnings/tools; and a precision/resource rationale. Later validation must accept multiple correct implementations, detect ownership/order faults and expose missing/blocked observations. No such tests or baselines are built by this packet.

**Disposition and next action.** Ready for bounded feasibility review at package scope, with execution conditions outstanding. The original audit binds Breakout controls/exit to owners and a public lineage. The [Blaze Vector audit](nu-task-diversity-and-common-requirements-2026-10-11.md#what-the-second-pair-actually-shares-and-changes) adds a second application candidate and explicit input, timestamp, gravity, hit-count and lifecycle differences. It is not yet an equivalent pair. Public platform/gravity requests and authored contact/lifetime requirements broaden provenance; they are not independent samples or an allocation. Decide preserved versus changed common behavior before assigning tasks, and record any alignment cost. The platform contract is provisionally an R01 case; substituting the sandbox avatar for Blaze Vector would require its own R02 adaptation rationale. Retain package attribution; defer a pair if matching requires rebuilding one style into the other.

## R03 — History-assisted debugging and recovery

**Question and contrast.** What can an actual Nu history/inspection facility preserve and expose, at what cost, and can a fixed agent use it to complete a reproducible repair? The primary technical comparison is a selected supported retention/restoration workflow versus fresh initialization and reconstruction of the same declared state boundary. An agent repair extension compares access to that facility against ordinary declared debugging access within Nu.

**Facility boundary.** The [pinned operation audit](nu-source-contracts-and-scenarios-2026-10-11.md#r03-what-gaia-restores) establishes functional-mode undo of represented gameplay/editor state, plus selected-screen spatial/physics reconstruction. The [selected application contract](nu-history-application-contract-2026-10-11.md) chooses same-code MMCC Breakout in functional Gaia: immediate model restoration at B0, then separately specified continuation at B1. The standalone program uses an imperative default and is not an automatic same-mode comparator. Saved values/brick keys are included; arbitrary closures/native state, input/RNG replay, host clocks, reload and irreversible-effect rollback are not established. Editor camera/selection and exception recovery retain separate policies.

**Scenarios and information.** Prepare F-history with known versus unknown failing entity/event as a prespecified initial-information distinction, using separate task instances to avoid solution carryover. Separate reaching the relevant state, fault localization, a proposed correction, an executed verified repair and resumed behavior. Before constructing an unknown-cause case, map its actual symptom/question to available historical evidence and the ordinary declared tool that exposes it. Record what the executor must infer and what is supplied. Extra causal instrumentation, a supplied fault location or an observer that answers the question changes the treatment and must have its construction/use counted. Add F-effect boundary cases only when the facility claims the relevant continuation. For an excluded irreversible effect, the useful result may be an explicit unsupported boundary rather than a failed promised rollback.

**Outcomes.** Technical restoration/continuation obligations, repair correctness, all-attempt elapsed/model cost, recording/instrumentation work, retained memory and replay/rebuild latency. The agent extension uses the shared endpoint. One known failure may be faster to fix without history; long retention or recording may dominate any diagnostic benefit.

**Evidence consequence.** [S42](literature/full-reading/S42-stream-debugger-comparison.md) supplies the information-dependent package reversal; [S66](literature/full-reading/S66-omniscient-debugging-behavior.md) distinguishes reruns from diagnosis success. The complete [S310 Java Whyline reading](literature/full-reading/S310-java-whyline-diagnosis.md) adds favorable, task-dependent diagnosis/recommendation results in a custom interface that did not permit code edits. Its output-to-code dependency interface is a substantive treatment component; a retained state alone does not supply it. S296/S297 distinguish represented-state exploration from replay under changed code. [S235](literature/full-reading/S235-mio-reversible-io.md) and [S107](literature/full-reading/S107-remote-concolic-debugging.md) supply restricted compensation/replay alternatives. None establishes the chosen Nu effect contract or a verified-repair benefit.

**Disposition and next action, updated 2026-10-18.** The [B0 reconstruction pair](nu-history-feasibility-2026-10-15.md), [B1 continuation](nu-history-continuation-2026-10-15.md) and [R06 cost series](nu-recovery-cost-feasibility-2026-10-15.md) resolve their selected feasibility questions. The [concrete symptom/evidence/tool map](nu-history-question-access-2026-10-18.md) now binds R04's stale-position episode, but its missing original scene names prevent treating the inferred collision as confirmed unknown-cause ground truth. It also finds that Gaia Interactive evaluation snapshots a getter expression and clears redo history. Next validate the chosen ordinary inspection route and branch/halt policy for a consequential case with its actual predecessor evidence. Fresh reconstruction must reach the same declared values and identities, counting setup and synchronization; a cheap restart is not matched recovery work. In-process getters and Gaia's console do not verify ordinary agent transport. Keep the agent extension deferred if it needs unallocated candidate execution or an observer that solves the task. The separate [R10 migration return](nu-schema-migration-feasibility-2026-10-16.md) remains stopped, as does R02 input construction. Neither reading nor another B0 repetition establishes practical value or resumes those gates.

## R04 — Domain modeling and evolution

**Question and contrast.** The immediate bounded study retains [D1](fsharp-domain-evolution-research-proposal-2026-09-16.md): explicit enumeration of current cases versus an initially behaviorally equivalent catch-all in the same pinned implementation, for one fixed coding-agent policy. Both arms can be compiler-exhaustive. Richer domain modeling remains a separate broader question because it can change APIs, names and modeling work.

**Tasks.** Use F-domain-distinct, F-domain-default and changes without a case-set extension. Include temporal/lifecycle requirements that exhaustiveness cannot entail. Bind each targeted source site to its actual cases, payloads, guards, branch behavior and frozen compiler/warning policy. Keep the diagnostic-opportunity record separate from the requirement-to-observation record; neither site count nor warning count measures satisfied obligations.

**Controls and outcomes.** Keep engine, APIs, dependencies, names/comments and helper organization shared as far as the convention allows, recording unavoidable branch/token differences. Never insert a present-day bug into the fallback arm or force token equality. Use the common all-obligation endpoint and all-attempt resource accounting. A correct catch-all or safe reorganization is valid; a compiling explicit branch with incorrect behavior fails.

**Evidence and rival.** P08, S34–S37, S72 and the completed type-evolution readings in the [index](literature/full-reading/INDEX.md) constrain novelty and diagnostic claims. Additional source/diagnostic information might help, add redundant work or still miss temporal obligations. The total source-convention effect includes those consequences; do not adjust on successful compilation/diagnostic exposure to claim a pure type mechanism.

**Disposition and next action, reconciled 2026-10-25.** The [Breakout site/policy sheet](nu-comparator-and-convention-audit-2026-10-11.md#r04-an-authentic-existing-source-site) is joined by [Blaze Vector's projectile command site](nu-task-diversity-and-common-requirements-2026-10-11.md#r04-an-additional-authentic-convention-site), with lifetime renewal, legitimate cancellation and no-case-extension sketches. Subsequent [actual-project builds](nu-application-diagnostic-feasibility-2026-10-15.md) establish the selected warning-only contrast, and the [pause references](nu-pause-runtime-feasibility-2026-10-15.md) establish matched fixed observations for valid explicit and catch-all implementations plus sensitivity to five declared source faults. Those observations resolve the corresponding earlier unprobed dependencies; they do not establish general equivalence, physical input delivery or diagnostic use by a candidate. Two Nu demos do not establish representative task coverage, and related sketches are not independent families. The remaining comparison needs ordinary candidate access, grounded task coverage and an allocated agent study. Preserve D1's within-implementation contrast, all allocation conditions and valid catch-alls.

### Diagnostic evidence and the maintainer's decision

The practical decision is whether a maintainer should require explicit current
cases in agent-maintained state-machine code, accepting its additional named
edits, or permit an appropriate catch-all. The target is correct completed
change and total work under the same ordinary tool/resource policy. It is not
a ranking by warnings removed, and no candidate experiment is allocated here.

The existing primary reconstructions provide a useful but conditional bridge.
[P08](literature/full-reading/P08-type-error-ablation.md#outcomes-contrary-evidence-and-arithmetic)
reports favorable aggregate agent-repair results with more detailed current
type feedback, alongside per-fault reversals and a nonmonotonic condition.
[S72](literature/full-reading/S72-functional-programmer-authoring.md#direct-relation-to-nu-and-d1)
documents both silent catch-all evolution risk and productive use of catch-alls;
its human practice observations are not a causal convention comparison.
[S231](literature/full-reading/S231-harmonyos-compiler-feedback.md#reported-positive-null-and-adverse-outcomes)
reports substantial iterative compilation gains with residual semantic failures,
without a matched multi-attempt no-diagnostic control or baseline semantic
comparison. Reusing these readings adds no new full-reading credit.

| Substantive demand | Decision-relevant contrast | Evidence still required |
| --- | --- | --- |
| A new case needs distinct behavior | A diagnostic may expose an omitted site; independent behavior still determines success. | Eligible successor tasks and observed candidate outcomes. |
| A new case legitimately uses the old fallback | Enumeration may add an edit while both completed implementations remain valid. | Task coverage and complete edit/checking work; the matched pause references establish only their bounded feasibility. |
| No case-set extension | There may be no exhaustiveness opportunity; source cues or unrelated behavior can still matter. | Distinct task provenance and retained-obligation observations. |
| An authentic case/API rename | The [time-advance rename](nu-practice-and-task-provenance-2026-10-11.md#2026-10-23-a-real-api-rename-and-a-qualified-lifetime-case) adds a named consumer edit under enumeration **conditional on requiring the local case rename**, while the appropriate catch-all remains valid. An engine-event upgrade alone can retain the local name. | Historical/adapted status, eligible initial behavior and observed maintenance work; no effect is inferred from the patch alone. |

These are coverage distinctions, not an equal-frequency industry sample or a
mandatory new factorial. Their prevalence and useful weighting remain unknown.
Diagnostic exposure is a consequence of the assigned convention: conditioning
the main result on receiving or clearing a warning would change the estimand.
A pure diagnostic-information question would require a separately justified
intervention; it is not silently added as another arm. The current missing
evidence is the direct maintenance effect and task population, not another
description of an already understood diagnostic method. Follow a further paper
only when its method, comparator or adverse evidence can change that decision.

### Historical-task eligibility, 2026-10-26

The [two-site history audit](nu-r04-history-task-audit-2026-10-26.md) now binds
an additional conditional command rename, genuine no-extension maintenance,
and a historical feature patch with a later state-scrutinee correction. It
finds no post-introduction projectile case addition/removal in the inspected
lineage; authored renewal/cancellation requirements remain authored.

For a historical task, specify which external and application-local changes
are actually required. Do not equate the maintainer's chosen diff with the
only acceptable implementation, require a local rename merely to force an
edit contrast, or treat a historical successor as a validated oracle. Allow
retained local names and other correct organizations where the contract permits
them. State whether the claim concerns an authored domain-evolution scenario
or practically required maintenance; source history does not supply its task
frequency or missing candidate effect. No new arm or execution is allocated.

**Current preparation scope and evaluator dependency, 2026-10-26:** retain the
authored behavioral question, with the existing pause/lifecycle family as its
preparation basis. The [oracle eligibility audit](nu-r04-oracle-eligibility-audit-2026-10-26.md)
finds that the completed probe binds the reference's `Paused` case, typed model,
entity/control organization and advancing-engine schedule. Those bindings are
legitimate for the frozen mechanism check, but cannot silently restrict the
future study's promised correct alternatives. A behaviorally correct successor
need not extend the union unless an explicit owned compatibility contract
requires it. Keep every attempt in its assigned arm; do not select only runs
that generate the predicted diagnostic. The next evaluator feasibility must
separate required interfaces from incidental representation and validate an
appropriate different organization. No candidate access or allocation is added,
and the completed references, results and failures remain unchanged.

## R05 — Correctness of interactive change

**Question and contrast.** Which declared observations warrant an all-obligation pass, and where do weaker observations miss relevant behavior? This is the shared evaluation specification. A separate methods contribution would compare observation policies on independently justified behavior/fault cases, including the cost of specifying and observing them.

**Proposed policy comparison.** Treat compilation plus ordinary development-test agreement as a restricted observation policy, and the explicit obligation contract as a stronger candidate. Keep their exact included predicates visible; do not assume that a richer monitor is automatically correct or complete. Reference behavior is justified independently through requirements, source reasoning and diverse valid/invalid traces, not solely by the same monitor or candidate logic being assessed.

| Obligation class | Required observation specification | Adverse or inconclusive case to preserve |
| --- | --- | --- |
| State/output | Required values/relations and allowed alternatives at a named boundary. | Correct compilation with a wrong state update; representation changes that preserve behavior. |
| Identity/lifecycle | Creation, deletion, ownership and permitted reuse; observer/subscription lifetime. | A stale event reaches a replaced entity, or valid identity behavior differs from the reference's implementation. |
| Temporal response | Trigger, clock/event-order convention, permitted order and justified deadline/horizon. | Wrong order, cancelled action, absent trigger or a bounded trace that cannot establish eventual progress. |
| History/recovery | Start/checkpoint state, pending obligations, retained observations and restored external boundary. | Present values match but a pending obligation is lost; replay repeats an irreversible effect. |
| Effects | Permitted multiplicity/ordering and observable host boundary. | Duplicate or omitted effects; an unobserved environment makes the result inconclusive. |

**Endpoints and validity.** For later labeled cases, report false passes, false failures, inconclusive rates and per-class sensitivity alongside construction/observation cost. Establish a meaningful case denominator and lineage; generated variations of one fault are not independent external validation. Exercise evidence is needed for success obligations: a missing trigger is not automatic completion. Program failure to reach a required trigger differs from evaluator inability to observe it. Unknown observations do not become passes. The [R10 converter continuation](nu-live-edit-contract-2026-10-11.md#exact-dependency-and-schema-conversion-contract) adds concrete source-derived distinctions: successful conversion with an unwanted field default or positional remapping, versus an exception-driven whole-model fallback. Test the intended state/meaning separately from conversion status; the later [Prime probe](nu-conversion-feasibility-2026-10-15.md) now executes selected default/positional hazards and an explicit mapping, without establishing in-application schema installation.

The [R13 interaction contract](nu-interaction-preservation-contract-2026-10-11.md) separately binds local input replacement/extension: capture, alias priority, one-step movement and preserved fields/effects at the control-block boundary. Host input must be observed at the intended phase; equal World values do not fix it. A legitimate downstream collision must not be confused with the control block directly mutating unrelated state. The ordinary signatures do not establish these predicates, and no executable checker is supplied.

The [pause/exit contract](nu-pause-exit-contract-2026-10-11.md#transition-horizon-and-observation-phases) adds another concrete distinction: input acceptance, effective pause and observable transition completion occur at different phases. A halted game clock cannot establish a stuck-exit timeout; the proposed outer-loop horizon also needs a wall-clock watchdog. A Title image alone does not establish idling or working input, and an already queued sound is not necessarily forbidden paused progress. Validate the proposed bounds and actual observer access before assignment; none is an executed test.

**Evidence consequence.** [S294](literature/full-reading/S294-industrial-game-regression-testing.md) supplies industrial observation/recovery constraints; [S281](literature/full-reading/S281-game-monitoring-thesis.md), S47/S53 and S220/S222 supply temporal and testing boundaries; S298 records configured/excluded checks; S299's preservation theorem depends on valid models and relevant boundary exits. These are tools for specifying coverage, not a theorem that the new evaluator is sound. S42's generated agreement is narrower than an independent repair oracle.

**Disposition and next action.** Ready for observation-specification review; the [source audit](nu-source-contracts-and-scenarios-2026-10-11.md#observation-access-and-r05-trace-specifications) now supplies satisfying, violating and inconclusive traces. Bind their selected requirements, observation phase, horizon and tolerances before construction. Later checks must accept an alternative correct implementation and detect plausible order/history/effect faults. No tests, mutants or executable monitor are constructed. Demote a standalone methods-paper claim if it only instantiates an established technique without a consequential new result.

## R06 — Runtime and state-retention costs

**Question and contrast.** At matched useful work, how much do a selected Nu retention/coordination policy and its observation facilities cost? The first candidate is the same supported workflow with current-state operation versus a declared bounded retention history. It is eligible only if the source supports both policies without inventing a facility. A copying/imperative or cross-engine comparison has a different contract and must be labeled separately.

**Workload specification.** Reuse the concrete R02/R03 behavior, including the [selected B0/B1 recovery boundary](nu-history-application-contract-2026-10-11.md#checkpoint-and-observation-contract). Declare world size, changed-state fraction/rate, event fan-out, retained-history horizon, inspected/restored checkpoints and host/native resources. Choose boundaries that expose both low-change structural sharing and costly high-change/long-retention conditions, as source-grounded hypotheses. They are workload dimensions to justify, not an arbitrary large Cartesian product or a prediction that sharing always wins.

**Measurement plan.** Bind hardware, OS/runtime, build, dependencies, warm-up and useful-work count before later measurement. Report frame-time distributions/tails, allocation per useful update, managed and relevant native working set, retained memory, throughput and restore/rebuild latency. Use complete runs as the repeated measurement unit; frames within a run are correlated. Count observation overhead and record warm-up/steady-state separately under a rule fixed before outcomes. Record stalls and failed/unfinished work rather than presenting successful fast frames alone.

**Cost boundaries.** Include snapshot/root creation, referenced objects, history indexing, retention/disposal, GC and host/native work where relevant. Freeing managed references is not proof that native resources were released. A memory reduction can coexist with worse tail latency; a fast replay may require expensive input capture. Keep one-time integration and per-run resource cost distinct. Do not equate equal wall-clock duration, average FPS or source size with equal useful work.

For the pause/exit candidate, halted gameplay can coexist with input, rendering, audio and tasklet work. Count steady paused activity, transition/resume work, state/guard storage and observation/input preparation separately from advancing gameplay updates. An advancing flag or fewer physics steps is not evidence of lower total cost; no pause saving has been measured.

**Evidence and scope.** [S238](literature/full-reading/S238-attribute-grammar-rendering.md) and [S239](literature/full-reading/S239-unity-mobile-optimization.md) supply workload/measurement trade-offs; [S248](literature/full-reading/S248-snowflake-manual-memory.md) has a distinct lifetime contract; S138–S151/S211–S214 and S237–S247 in the index cover representation/runtime alternatives. [S260](literature/full-reading/S260-unreal-energy.md) and [S261](literature/full-reading/S261-unity-unreal-energy.md) preserve workload-dependent power/engine findings. Those results do not calibrate Nu sample sizes or current performance.

**Disposition and next action.** The [source cost boundary](nu-source-contracts-and-scenarios-2026-10-11.md#r06-costs-and-a-useful-comparison-boundary) separates checkpoint creation, retained roots, native rebuilding and resumed frames. The [Nu/Jolt dependency audit](nu-jolt-dependency-audit-2026-10-11.md) adds cumulative creation, maintenance threshold and positive-time integration policy; package-to-binary identity is verified, exact native build/loaded behavior is not. The [2D platform audit](nu-platform-contract-2026-10-11.md#observation-identity-and-cost-limits) distinguishes managed Box2D.NET world rebuilding from native Jolt and identifies the pre-application integration-event boundary. Do not count all physics rebuilding as native work or assume retained roots preserve solver/contact state. Compare retention policies within the same functional mode; an imperative/functional contrast changes more than retention. Gaia has no inspected bounded-history eviction policy or ready history-off comparison switch. Select matched useful work before later authorized instrumentation, repeatability and overhead checks; no run count is inferred. When services differ, compare total cost to obtain the same required result or narrow the claim explicitly.

## Shared feasibility dependencies and falsification review

| Dependency | Affected claim | Next executable desk action | Later evidence required |
| --- | --- | --- | --- |
| D-source | Actual Nu capability and common initial behavior | Use the audited ownership/history paths; bind selected application data and requirements, recording any new pin/differences. | Supported environment and independent initial-behavior checks. |
| D-task | Relevance/diversity of maintenance tasks | Extend the audited authored/adapted/historical distinctions with eligible changes and credible diversity; remove redundancy before outcomes. | Feasible independent tasks/applications; claim restricted if only a local case exists. |
| D-oracle | Correct change and recovery | Bind the source audit's trace specifications to independent requirements, valid alternatives, phases and justified horizons. | Sensitivity, exercise and false-pass/false-failure checks under approved construction. |
| D-access | Agent use of relevant tools | Apply the in-process/editor interface inventory to the permitted agent policy; access remains unverified without a live probe. | Separately approved compatibility/observation validation. |
| D-cost | Resource trade-off | Select equivalent useful work within one mode; use the audit's separate checkpoint, retention, native rebuild and resumed-frame boundaries. | Repeatability, overhead and measurement resolution. |
| D-precision | Useful uncertainty and resource allowance | State the decision threshold needed, actual independent units and proposed paired/family estimand for review. | Justified sensitivity/precision and a separately authorized budget; no old allowance reused. |
| D-human | Human productivity or steering benefit | Retain R21 policies and source-grounded measurement candidates; distinguish actual review from AI synthesis. | Measurement reliability, task/person variability, participant design and separate authorization. |
| D-literature | A particular comparator/method or stronger novelty claim | Follow the exact primary/edition dependency in the continuation plan when it can change the design. | Actual required reading/coverage; access denial remains a gap rather than an exclusion on merit. |

Before later execution, the design must explain how it would report these outcomes: a correct fallback beating explicit cases; a local/coordinated crossover; known-fault history overhead; successful visible recovery with lost pending work; a valid reorganization unlike the reference patch; infrastructure missingness reversing a naive ranking; human rescue producing an otherwise successful artifact; and memory savings with worse frame stalls. These are specification-review cases, not executed tests or predetermined results.

The six proposals and original agenda dispositions completed the October 8 preparation artifact. They did not complete the literature field or demonstrate feasibility; the subsequent linked execution records own the bounded results. The 2026-10-11 source and comparator/convention audits advance D-source/D-task/D-cost and supply prose observations. The selected history contract binds R03's first application/state subset. Use the [current agenda dispositions](nu-research-agenda-2026-10-08.md#readiness-and-next-actions-for-all-directions) for resolved dependencies and remaining work instead of repeating these desk-stage inventories. Follow primary reading when it can change a decision. This design packet is not an allocation: PLAN records the user's local-construction authorization and the remaining candidate, participant, account, OAuth and H boundaries.
