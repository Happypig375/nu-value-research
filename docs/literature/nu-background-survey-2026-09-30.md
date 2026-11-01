# Wider Nu research background survey

**Status: bounded background assessment available; broad prioritized research preparation active, 2026-10-08 HKT.** The user's latest instruction is to prepare the plausible directions together, prioritized by research value, while searching literature as needed. The [research agenda](../nu-research-agenda-2026-10-08.md) records those questions, comparisons and preparation order. The wider survey remains the evidence base, with access and coverage limits explicit. The [preceding assessment](nu-literature-assessment-2026-09-30.md) completed an earlier decision-specific task; its 62 full readings and controls do not establish whole-background completion.

**Implemented continuation:** the [saved plan](../nu-research-continuation-plan-2026-10-08.md) and [six study designs](../nu-research-study-designs-2026-10-08.md) prioritize mechanisms/costs plus bounded agent maintenance. R21 preserves future human-steering effectiveness, including steering-only and unrestricted intervention, with measurement and participant feasibility unresolved. Task provenance and contrasting requirements address the user's convergence concern; repeated AI outputs are not independent coverage. This design segment reuses completed evidence and adds no new primary reading or retrieval credit.

**Source continuation, 2026-10-11:** the [ownership/history and scenario audit](../nu-source-contracts-and-scenarios-2026-10-11.md) inspects pinned Nu implementation and public maintenance history directly. It establishes a transition/pause issue-to-patch lineage and functional-mode represented-gameplay undo with native reconstruction. The subsequent [comparator/convention audit](../nu-comparator-and-convention-audit-2026-10-11.md) adds ordinary Godot facilities and D1's existing match/warning-policy sheet. Task eligibility, application-specific snapshot safety, agent access and measured benefit remain separate. The dated coverage refinements add source/practice understanding, not publication-reading credit or experimental results.

**2026-10-15 continuation:** existing attachments now close the selected practice, generation, scene-merge and walkthrough reading gaps at the editions in the [index](full-reading/INDEX.md). At that checkpoint S305 was complete at its 1990 report only. The [October 18 journal reconciliation](full-reading/S305-problem-centered-design-journal-reading-2026-10-18.md) now closes the final-edition gap and distinguishes the added, overlapping six-person prototype check. The [PDF audit](pdf-acquisition-audit-2026-10-15.md) corrects the false human-verification classification. Confident local experiments are authorized; the dated continuation below integrates bounded probes without claiming comparative benefit. Historical hold/access statements below retain their checkpoint scope.

## Question and scope

The starting point is characterizing **Nu's claimed innovations** against prior work. Interactive Software Evolution is an internal codename, not a replacement research claim. The background question is how domain and state representation, ownership, coordination and tools affect the cost and correctness of evolving interactive software, particularly Nu/F# games and maintenance by humans or coding agents. The survey includes foundational mechanisms, engineering alternatives, empirical benefits and costs, practice/adoption, and methods needed to distinguish those effects. D1's exhaustive-match candidate is one part of this background. D2's selector apparatus remains deferred; evidence about architecture evaluation and adoption can still be relevant to the broader survey without authorizing D2 construction.

The strongest rival is that apparent benefits come from tool access, experience, training exposure, task selection, API/implementation differences, hidden mutable or external state, or shifted runtime and coordination costs. Evidence can change which mechanism is plausible, which claim is unsupported, which comparison is necessary, or whether a research question should be redirected. Include empirical null/adverse findings and nonfunctional alternatives. Separate theory, practitioner accounts, demonstrations, measurements and independent comparisons. Public Nu source, Vsynchronicity hypotheses and derived sibling technical analysis retain their separate evidence classes; no private transcripts enter searches or Git.

## Live evolution: what the mechanisms preserve

**Consolidated 2026-10-03 from completed readings.** The strongest supported comparison is between explicit contracts for change, state, history and effects. Persistent data, a consistent update phase, a successful migration, a replayed trace and a checked temporal property are different capabilities. The following synthesis reuses the recorded publication/source scopes; it adds no full-reading credit, new experiment or claim of field completeness.

Nu's inspected source remains revision `064f7ae92a8506689cd91aff5e6804a375d6ef3d`. Its [MMCC and ImSim templates, World wrapper, snapshot/restoration and event graph](../nu-grounded-maintenance-methodology-2026-09-14.md#a-potentially-simpler-contrast-already-exists-inside-nu) establish concrete design mechanisms. The [source and practitioner account](../nu-form-factors-and-research-leads-2026-09-14.md) motivates domain modeling, ownership and locality, while explicitly recognizing coordination and temporal coupling. These are the claims to characterize. The derived sibling analysis is hypothesis material, not a second independent observation of benefit. No new whole-Nu source audit or engine execution is claimed here.

### Change and continuation contracts

| Method and permitted change | What is retained or reconstructed | Pending work, history and external boundary |
| --- | --- | --- |
| [S71 live coding](full-reading/S71-live-state-migration.md): replace a step function and migrate explicitly represented typed state | Structural correspondence retains compatible fields, initializes new structure and permits custom conversions. | Well-typed state need not satisfy the new program's semantic invariants. Functions cannot be retained through the `Data` representation; clocks, foreign storage and effects need their own policy. The demonstrations and finite migration tests do not establish arbitrary safe continuation. |
| [S85 Nextep](full-reading/S85-constraint-state-migration.md): edit a model and solve for its new runtime state | New-model invariants and a separately chosen old/new migration relation constrain a solution; a distance objective prefers selected small changes. | Modeled queues can be constrained, but unrepresented history is unavailable. Deleted-active-state handling is a policy choice. The paper leaves integration of actual resumed execution to future work; satisfiability and a small structural distance are not observed behavioral preservation. |
| [S86 Baseline](full-reading/S86-operation-based-data-evolution.md): selected schema and data operations across divergent documents | Stable field/element identity and recorded operations support directional transfer, compensation and partial query rewriting. | Conflict direction is explicit; failed transfers and a dropped update are retained adverse examples. It does not implement arbitrary live program-state type evolution. Undoing represented data is not reversing external I/O. |
| [S87 Denicek](full-reading/S87-denicek-document-computation.md): evolve structured documents and computations through edit history | Rebase-style merging rewrites explicit references and specializes transformations for added/copied nodes. Evaluated results are separate edits whose dependencies support invalidation. | Converges variants into one structure; conflicts and conditional actions require policy. Positive qualitative notebook construction coexists with scaling limits. The paper expressly excludes arbitrary evaluation-state-preserving source edits; implicit-format logic and external effects are not repaired automatically. |
| [S102 Cambria](full-reading/S102-cambria-document-evolution.md): translate document schemas and supported patches between application versions | Explicit directional maps, defaults and generated types/schemas define compatibility. Its Automerge adapter retains original writer-schema operations and translates on read, reconstructing identity/path state. | Positive demonstrations and author workflow experience coexist with an acknowledged scalar/list deletion inconsistency. CRDT/lens interaction remains open; valid data shapes do not establish user intent, arbitrary concurrent consistency or external-effect rollback. |
| [S103](full-reading/S103-bidirectional-schema-versions.md) / [S236 BiDEL/InVerDa](full-reading/S236-multischema-placement-advisor.md): maintain several writable relational schemas over shared data | Declared bidirectional operations, stable tuple identity, defaults, preferred-replica rules and hidden auxiliary data reconstruct each logical view across physical placements; S236 adds redundant copies and calibrated placement advice. | Round trips preserve a view’s admissible data; cross-view propagation is best effort. The advisor improves tested workload costs without proving global optimality, zero-downtime service, live-code preservation or developer effort. |
| [S99 generated-code live modeling](full-reading/S99-generated-code-live-modeling.md): supported state/transition edits and action replacement | Runtime tables change while initial actions remain compiled and edited actions are interpreted. A capsule pauses at a run-to-completion boundary; an active deleted state requires a chosen replacement. | Other capsules may keep queuing work. Replay uses the latest exit record per basic state, restores one capsule and temporarily defers messages; it does not rewind peers or physical effects. Capsule/port/protocol changes are outside the demonstrated editable scope. |
| [S101](full-reading/S101-operation-based-live-models.md), using the [S108](full-reading/S108-blended-model-versioning.md) versioning core: reconcile represented design edits and interpreted execution | Dependency-closed, nonconflicting operations can merge. Recorded-event reconciliation preserves compatibility with the recorded computation; the alternative current-state policy can continue after invalidating its old replay history. | Read dependencies currently need manual annotations. A conflict-free graph is conditional on complete represented causes; user runtime interventions can create unreachable states. Graph operations do not automatically capture clocks, native handles or external effects. S108 alone supplies no execution semantics. |
| [S100 current-state checking](full-reading/S100-live-model-checking.md) and [S105 temporal breakpoints](full-reading/S105-temporal-breakpoints.md): explore possible futures under declared properties | Subject/monitor products retain property progress within a search and return useful state or cycle witnesses. | A fresh lookup does not automatically inherit obligations begun before its checkpoint. Current-state exploration is not all initial-state exploration. State equality, reductions, environment assumptions and observation points determine what a pass means. Neither paper supplies a universal code-edit migration policy. |
| [S106 verification and monitoring](full-reading/S106-unified-verification-monitoring.md): reuse a property representation across abstract exploration and concrete execution | A shared interpreter/observer framework supports verification and monitoring of the scheduled runtime trace. | Abstract environment coverage and actual runtime scheduling differ. Queue presence/oldest-event predicates do not necessarily observe consumption or physical response. Shared atoms can share mistakes; monitoring is not independent validation of the specification or a migration guarantee. |
| [S107 remote concolic debugging](full-reading/S107-remote-concolic-debugging.md): explore executions of a loaded program with concrete or mocked inputs | Logged input values and instruction counts support reset/root replay; an on-demand VM snapshot starts bounded concolic exploration. | Outputs are not compensated. Formal reachability relies on feasible manual mocks; automatic suggestions are bounded by instructions, symbolic inputs and iterations. One representative control path does not cover every output-relevant value. This is not a general cross-version code/state migration contract. |
| [S296 State Explorer](full-reading/S296-S297-state-exploration-and-live-replay.md): explore reachable relevant states inside a Godot game | Copies of represented state, supplied actions and a relevance predicate define a search frontier. Selecting a result makes it current; examples supply useful flaw finding and undo. | Relevant states are retained but not expanded in that search. Restricted variables/actions bound coverage; mechanics isolation, integration, copying and interpretation remain costs. It supplies no arbitrary host-effect rollback or complete game oracle. |
| [S297 live replay](full-reading/S296-S297-state-exploration-and-live-replay.md): change game code, reinitialize and replay the recorded event log | The implemented prototype retains inputs/ticks and rebuilds game state from initialization under the new code. | It discards the old component; this is not arbitrary old-state/continuation migration. Even rendering-only edits replay the whole log. The proposed node graph and borrowing discipline are unfinished; unlogged inputs/effects and semantic intent need separate treatment. |
| [S235 MIO](full-reading/S235-mio-reversible-io.md): navigate one program’s executions with reversible I/O | Snapshots after I/O and deterministic, invocation-specific compensation support backward/branch travel; feasible mocks select inputs. | Atomic synchronous outputs, reversible selected effects and the formal independent-input model are premises. The dial demonstrates a supported motor case; asynchronous/irreversible outputs and arbitrary physical-world restoration are excluded. It supplies no general edit-migration or developer-benefit guarantee. |
| [S225 Micro-Machinations](full-reading/S225-micro-machinations-adaptation.md): apply explicit named game-mechanics deltas between evaluation steps | Same-kind nodes can retain identity, while redefining a pool sets its quantity to the new declared initial value in the inspected later source. | C# host bindings, instance/value notifications and two-step converters are part of the contract. Physics, timing and other host behavior lie outside the economy model; node survival alone does not establish preserved quantities, atomic host updates or external rollback. |
| [S269–S271 Rulebook](full-reading/S271-rulebook-thesis-and-methods.md): activate or replace authored game-mechanics rules; later pattern permits dynamic rule addition/removal | Current simulation state and effect data guide rule applicability. ARC separates amendment, resolution and chaining; selected implementations preview amendments. This is an active-mechanics contract, not a general source-edit migration policy. | Reference and jam implementations have different linked-effect, synchronous dispatch and timer paths. Preview may mutate the supplied effect and reads current mutable state; a later click creates a new effect. The thesis’s stable save checkpoint is a persistence boundary; Direct Access may bypass amendments. No immutable history, pending-work migration or host-effect rollback is established. |
| [S277/S278](full-reading/S277-S278-mayet-runtime-repair.md) Mayet/Lakitu: detect selected bad states/sequences and ask the host to repair them during play | Manually emitted event payloads enter Drools memory; human rules request authored host operations. Examples restore selected jump/gap behavior. | Asynchronous repair requests can describe an earlier state; the host may defer or ignore them. Restart clears monitor memory. No source/schema migration, universal preservation or termination guarantee is supplied; harmful repairs/cascades remain acknowledged risks. |
| [S279/S280](full-reading/S279-S280-game-runtime-monitoring.md): observe selected game-loop snapshots with an external temporal monitor | XML templates and identity-linked formulas separate the exported trace from the game implementation. Both publications and their original visuals are now fully read, including inconclusive verdicts and the fuller journal formulas. | Selected-fault detection and bounded cost results are favorable. Exported snapshots can miss transients; absent objects can vacuously satisfy a property, and finite-ending/reset policy remains unspecified. Exact measured-build correspondence is unbound. Observation supplies neither state repair nor arbitrary edit preservation. |
| [S286 NodeGit](full-reading/S286-nodegit-source-and-access.md): integrate edits to serialized procedural graphs | Greedy type/property/reference matching infers correspondence despite fresh import IDs; diffs map matched references to ancestor IDs and combine nonconflicting property edits. The complete paper adds favorable curated and randomized matching results. | The Blender path imports/exports graph documents. Same-object overlap checks do not establish cross-object validity or preserve stacks, events/timers and external effects. The inspected public graph-cost denominator differs from the paper; exact measured-build identity, conflict repair and total workflow cost remain unresolved. |
| [S287 VRGit](full-reading/S287-vrgit-history-and-collaboration.md): navigate recorded edits and selectively reuse objects from alternate scene versions | An operation DAG records edits; a summarized miniature history shows versions and collaborator locations. Selected furniture is reused with its transform. | Automatic history recording and visual comparison support collaborative authoring. The merge label is qualified as selective reuse; code/schema migration, ongoing-game state and external-effect preservation are not established. |

The decisive distinction is the **chosen meaning of continuation**. A designer may want to retain current play state, replay an old input history under new code, or find a new state satisfying revised constraints. These can require different outcomes after the same edit. S101 makes that choice explicit; S71, S85, S99 and S225 implement other correspondence/default/reset policies. A snapshot cannot select the intended policy by itself. Likewise, replaying an input or graph operation does not by itself restore a peer, physical device or pending response obligation.

### Game alternatives and observed costs

| Alternative | Closest Nu-relevant mechanism | Evidence and consequence |
| --- | --- | --- |
| [S69/S70 Casanova](full-reading/S70-casanova-encapsulation-networking.md) | Typed world rules, current/next buffers, scripts spanning ticks, generated indexes and lifecycle notifications | Concrete F#/C# predecessors for declarative updates and generated coordination. Selected query/update workloads improve substantially, but effects and network ownership remain explicit, and the networking example permits stale replicas and missed collisions. Generated machinery grows while authored source shrinks; no maintenance-effort effect is measured. |
| [S223/S224 SGL](full-reading/S224-sgl-state-effect-pattern.md) | Common-state reads, declared effect combination and separate application of effects; shared query work across entities | Strong scan/index throughput evidence includes index rebuilding in its 500-tick workload. This is within-tick coordination, not retained history or edit migration. Multiplicity, nonstacking selection and host postprocessing still need intended rules. The healer crossover and disputed legend qualify unconditional indexing claims. |
| [S76 ECS references](full-reading/S76-ecs-entity-references.md), [S77 DOTS migration](full-reading/S77-dots-migration.md), [S112 ECS storage](full-reading/S112-ecs-storage-comparison.md) | Entity identity/validity, storage/query organization, jobs, command buffers and host synchronization | Packed iteration, reference access, initialization and host rendering have different winners. S77 reports faster occupation but slower rendering and declines a full product migration. These are useful alternative mechanisms and adverse workloads; the papers do not establish live-edit/history contracts or a universal architecture ranking. |
| [S225 game adaptation](full-reading/S225-micro-machinations-adaptation.md) | An executable mechanics model shared between simulation and a running .NET game | About fifteen-minute author design/modeling iterations are favorable experience. They exclude a controlled comparator and measured total DSL/host-integration budget. This is direct game-specific prior art without requiring a wholly functional world. |
| [S291–S293 Ceptre](full-reading/S291-S293-ceptre-resources-and-editor.md) | Typed multiset resource rewrites, unordered rules within a stage, quiescence handoff and explicit external choices | A concrete coordination alternative. The local frame property preserves the existence of an old trace, while staged programs give up that composition guarantee. One eight-person editor study has favorable model-change observations; its editor lacks stages. No Nu effect, whole-system migration or host-I/O preservation follows. |
| [S269–S271 Rulebook](full-reading/S271-rulebook-thesis-and-methods.md) | Predicate dispatch and effect amendment localize cross-cutting mechanics; partial ARC supports action-cost previews | Course effort/usefulness is inconclusive, with slightly fewer reported architecture changes and strong reuse preference. Three jam cases add favorable local extensions and previews alongside learning, duplication and state-access costs. S271 adds original self-report instruments and Grimoire’s useful property/rule reuse, editor propagation, dispatch performance problems and preview recursion. Short dispatch bodies exclude the complete adoption/integration budget; no universal performance or maintenance effect is measured. |

The live tools also preserve real favorable outcomes. S99 reports **1.3–2.1 ms** single edits against **608 ms** in its selected large model, alongside about **25% higher peak memory** and a **70% slower selected interpreted action**. S106 finds and repairs a model interleaving defect, with **50.8% runtime monitoring overhead** and **8.2% executable-size overhead** in its CCI case. S107 reports about **2 seconds traced versus 5 minutes checkpointed** for 50,000 instructions in an I/O-heavy game, but changes the external-effect guarantee; its difficult capped calibration analysis takes **219.613 seconds**. These are different units and workloads. They cannot be averaged into a maintenance saving, and the remote comparison does not establish dominance at equivalent reversibility.

For Nu, the retained empirical questions are therefore specific: whether its ownership and representation make consequential changes easier; whether its history/tool support reduces diagnosis or repair work under the intended effect contract; and whether those benefits exceed setup, review, runtime, integration and recovery costs. The inspected MMCC/ImSim Breakout pair differs in movement/collision implementation and engine-physics use, so it is not an isolated source-organization treatment. Shared engine facilities do not explain an effect between styles without a corresponding difference in use. Neither source length nor an immediately visible edit answers these questions. Existing adverse E/H compactness observations remain evidence.

### Evidence disposition and the next dependency

Generic claims to invent persistent history, coordinated world updates, live rule editing, typed migration or temporal debugging have close predecessors. This establishes overlap, not the absence of any distinctive Nu combination. The source-grounded Nu package and its intended change/effect boundaries still need to define any narrower claim; no firstness or measured Nu advantage follows from the codename.

The former compensation dependency is now primary-read as [S235 MIO](full-reading/S235-mio-reversible-io.md). It supplies useful device-specific compensation and reduces full-snapshot overhead substantially, while requiring atomic synchronous, deterministically reversible effects. Its no-I/O timing workload and single dial demonstration do not certify every environment or a net maintenance saving. S107’s cheaper trace/replay changes that effect contract. [S83’s completed program-structure study](full-reading/S83-program-structure-maintenance.md) now supplies actual change-task evidence: favorable functional decomposition for complex student tasks, professional uncertainty at .05 and study/edit time that omits compilation and checking. This strengthens the task-dependent factoring rationale without establishing a Nu or functional-language advantage. [S229’s complete professional workflow](full-reading/S229-picoscenes-expert-ai.md) adds reported feature effort of 133 → 42 active engineer-hours, lower normalized defects and hardware costs. Its expert/context/feedback bundle and incompletely specified historical/rotated allocation do not isolate a Nu source effect. The PlotService illustration also changes an x-axis cutoff into a fixed sample capacity, making preserved behavior a concrete condition on its speed claim. Net professional/agent benefit in Nu is an empirical residual; more unrelated abstracts cannot settle it. S102 now supplies a document/patch contract with positive author experience and an acknowledged deletion inconsistency. S87 now adds document computations and their dependency/representation limits, with positive qualitative construction evidence. The completed S218/S219 originals now resolve the quiescence and GUI/state-transfer methods; their exact implementation, complete migration policy and modern Nu cost remain distinct gaps. S229 allocation/artifact reconstruction remains open. This consolidation closes none of those themes; PLAN separately authorizes confident local construction.

## Coverage map

**Reconciled 2026-10-15 with supplied-publication readings and bounded local feasibility.** The [supervisory review](../supervisor-review-2026-09-30.md) requires discovery coverage, primary understanding, evidence disposition and the next consequential action to remain separate. This map separates those decisions and points to the full reconstructions instead of repeating every per-paper result. Detailed results, contradictory endpoints and edition limits remain in the linked reading notes, the refinements below and the [search ledger](nu-background-searches-2026-09-30.md). Earlier map states remain in Git. The map credits only the linked actual readings. The dated assessment below is a maintainer coverage judgment for characterizing the present Nu claims, not field completeness or human scientific sign-off.

Discovery is bounded: thirteen native Consensus calls returned 1,295 occurrences; title coverage does not imply full-abstract or primary-method coverage. C02's two pages now have dispositions for all 199 records (195 scientific passages, one boilerplate, three missing abstracts). C05 now has [100 supplied-text dispositions](nu-background-agents-search-2026-10-02.md), with94 newly consumed passages; this closes only the retrieved-page screen. Other C01–C11 continuations, bounded citation graphs and exact-primary routes retain their recorded limits. Neither a complete result page nor a sparse graph establishes field-wide absence. Benefit in Nu can remain unmeasured even where an alternative's method is understood; an acquired unread paper remains a reading gap.

**Retained-route audit, 2026-10-08:** C03/C04/C06/C07/C09/C10/C11 cached titles are revisited, with C08's existing 98-record table reused; the previous pass revisited C01, and C02/C05 supplied-text dispositions remain available. Thirty-one selected passages are consumed or reused at the exact positions in the ledger, with no new Consensus call or claim of newly screening every title. This promotes the interaction-typing method S298, modular verification S299 and cognitive-fit maintenance S300; S301 initially retains a positive experiment with unavailable primary methods. S298–S300 are now reconstructed below, and the subsequently supplied S301 PDF resolves its original methods. S300 separates measured comprehension gain from partially completed modification; it does not measure time to verified completion. Other retained leads are conditional on a missing comparator, contract or cost boundary.

| Theme and question | Discovery coverage | Primary understanding and gaps | Evidence disposition | Next consequential action |
| --- | --- | --- | --- | --- |
| **B01 Design foundations and comprehension:** what makes understanding and change easier? | C04/C08/C09 and G23–26/G31/G33 cover foundations, contrary comparisons and selected professional work. S83 and the S288–S290 routes add primary methods; this is not current-population coverage. S38 adds an exact-DOI framework lookup and bounded walkthrough recall; S304–S307 add three bounded Scite lookups plus primary publisher/archive and bibliographic routes, not instrument validation or thematic saturation. | Information hiding, control distribution, modularity and concern measures are reconstructed. S83, S155/S156 and professional studies retain task/sample limits; S152/S153 fuller accounts remain partial. S288 is complete; [S289/S290](full-reading/S289-S290-game-practice-methods-partial.md) now has complete supplied-publication coverage, including all figures/tables; instruments and participant overlap remain unresolved. [S300](full-reading/S300-cognitive-fit-and-modification.md) reconstructs 24 professionals, two repeated tasks per person and task-dependent comprehension-gain/modification-progress associations; S301 reconstructs two student experiments on grouped rule documentation/interfaces, with favorable graduate elapsed time and novice correctness/structure scores. S42 now reconstructs a twenty-professional loop/stream debugger-package comparison with known/unknown failing-object conditions. [S38](full-reading/S38-cognitive-dimensions.md) now has complete 44-page publisher coverage and all main/appendix figures; [S307](full-reading/S307-programming-walkthrough-draft.md) now reconstructs the complete archived-draft walkthrough procedure and four author experience accounts. [S304](full-reading/S304-usability-testing-reading-2026-10-15.md) now supplies the original six-volunteer protocol; [S306](full-reading/S306-programming-walkthrough-final-reading-2026-10-15.md) supplies the final method. [S305](full-reading/S305-problem-centered-design-reading-2026-10-15.md) is complete at its 1990 report edition; its 1991 journal body remains unread. | There are favorable task-time, locality and guideline results, centralized-control advantages, nulls and adverse rework. Source metrics and self-reported process adherence do not identify lifetime effort. The S308/S309 continuation below now binds the API-metric derivation and its unvalidated developer-outcome boundary. Representation accessibility and cross-role handoffs are part of the value question. S42 reverses the overall stream benefit when the failing object is known. S38 supplies task-specific qualitative trade-offs and a supplied-target editing contrast, not a validated learning scale or onboarding effect. S307 supports useful prerequisite/design/documentation hypotheses and preserves missed knowledge and alternatives; no calibrated readiness or prediction-accuracy result follows. | Reuse these results in the Nu claim-to-outcome assessment below. Follow another design/practice study only if it can change a named mechanism, comparator or cost boundary; another process label cannot settle Nu value. S300’s original allocation and progress rubric are now reconstructed: preserve its favorable and adverse associations without treating measured comprehension gain as an assigned intervention or partial progress as verified completion. Retain S301’s positive documentation result without treating its structure-conformity score as general correctness or its elapsed-time mean as time to verified completion. Apply the [R07/R20 learning and role contract](../nu-learning-and-role-contract-2026-10-11.md); use the candidate knowledge/assistance inventory at its qualitative scope, then select a practical role/task before later measurement. Use the completed protocols with their shared ChemTrains lineage. Follow S305’s final journal or design supplement when exact edition or problem-material correspondence matters. Human comparison stays deferred. |
| **B02 Domain modeling, types and evolution:** what guidance survives new cases? | C02 screens all supplied material from two retrieved pages; later pages and missing abstracts remain unexamined. Exact schema, typed-method and versioned Blueprint routes recover methods missed by broad prefixes. | Coverage checking, extension/composition, S87/S101/S102/S103/S108/S236 and selected translation methods are reconstructed. [S221 original LOFT](full-reading/S221-formal-statistical-testing-access.md) remains an access gap; [S295](full-reading/S295-persistent-object-evolution.md) now reconstructs persistent-object/class evolution and JPA/time-series mappings. Blueprint shipped-source correspondence and selected typed-editor leads remain conditional. S298 now reconstructs typed interaction substitution/composition and the distinction between host data typing and configured runtime conflict checks. | Coverage diagnostics, shape compatibility and round trips are useful under explicit assumptions. They do not supply intended successor behavior. Correct catch-alls remain valid alternatives; human/type-context benefits and construction costs do not estimate D1 or a Nu effect. | Bind any retained Nu type-evolution claim to its represented values, identity/default policy and independent behavior obligation. Reuse S295’s operation/mapping/repair distinction; reopen another exact typed-editor or persistent-object method only if the claim exceeds the reconstructed contracts; keep missing primary access separate from unknown empirical transfer. Reuse S298’s concrete substitution and predicate-exclusion boundaries; its selected companion release does not establish every manuscript conflict-analysis claim. |
| **B03 Reactive coordination and lifecycle:** who orders work and owns effects? | Reactive bibliographies, G15/G17 and S68 cover joins, plans, logical resources and staged execution. Casanova, Join Token, SGL, Micro-Machinations and monitoring/repair lineages have primary follow-up; Ceptre now has primary reconstruction; ABL remains conditional. SC232-SC234 and W741-W746 add the exact Ceptre language/editor lineage. | S57–S62, S121/S122, S142, S223–S225 and S277/S278 supply ordering, matching, effects and host-repair contracts. [S205](full-reading/S205-jescala-dissertation-access.md) now supplies the complete fuller JEScala dissertation: occurrence-dependent blocking, specialized FSMs and actor-backed event monitors, with S142 dataset overlap and unavailable artifacts explicit. S105–S107/S235 locate monitor history, replay and restricted compensation. S297 separates its implemented event replay from proposed mutable-node ownership and borrowing. [S291/S292](full-reading/S291-S293-ceptre-resources-and-editor.md) now reconstruct multiset rewriting, resource competition, quiescence handoff and the distinction between local and whole-stage composition. S298 adds interaction families and conditional conflict diagnostics. [S299](full-reading/S299-modular-reactive-verification.md) now supplies formal module contraction and property-preserving replacement under valid behavioral models and matching relevant exit conditions. | Useful coordination has multiple implementations. Common-state reads, exclusive resource consumption, delayed repair and external-effect compensation are different contracts. Explicit event selection and a deadline do not establish complete lifecycle correctness. | Apply the reconstructed Ceptre contract to Nu’s represented state, order and external effects. Review retained discovery paths for a consequential missing coordination mechanism; a second description of resource rewriting alone would not resolve Nu benefit. The [R05 stub-world probe](../nu-event-feasibility-2026-10-15.md) observes bounded actual event order, Resolve and explicit unsubscription, with application lifecycle untested. S205’s fuller method is now read; use its queue/thread/completion boundaries only for a comparison that promises them, rather than treating every event system as a Join or monitor implementation. Reuse S299’s model-relative preservation contract alongside Ceptre’s local/staged distinction; memoryless selection, world assumptions and boundary predicates define its transfer. Use the 2026-10-11 source audit for Nu publication/consumption order, monitored versus plain subscription lifetime and #1145 transition/pause lineage; next settle eligible adapted changes and initial observations. |
| **B04 Persistent state, effects and history:** what can be retained or restored? | C01/C03/C11, G18–22 and exact collection, snapshot, live-state and authoring routes separate functional persistence from nonvolatile-memory noise. Selected C01 state-exploration/replay passages now lead to S296/S297; later broad pages remain open at their recorded scopes. | Persistence, migration, replay, Tardis, HistOOry, MIO and document histories are reconstructed; S295 adds stored-object evolution while explicitly excluding live-process/class-version updating. S296 reconstructs copied-state navigation; S297 rebuilds state from logged inputs after an edit. S218/S219 now have complete original-PDF and visual readings, separating quiescence, controlled object-graph migration and GUI/native routing. [SceneGit S285](full-reading/S285-scenegit-reading-2026-10-15.md) now has complete primary-method coverage; its supplement/raw conflict cases remain unexamined. [NodeGit S286](full-reading/S286-nodegit-source-and-access.md) now has a complete twelve-page primary reading alongside the bounded public-source packet. Its snapshot matching/merge evaluation does not establish undo or live-state retention; paper/source graph-cost normalization remains different. LevelMerge’s final edition and selected supplements remain unbound. | Retaining values, restoring a document, replaying inputs, merging edits and continuing a running world are established but distinct capabilities. Pending work, identity, observers, retention policy and external effects determine what survives. None alone guarantees arbitrary successor behavior. | Use the consolidated continuation-contract table to state exactly which Nu capability is claimed. Retain the named access/version gaps; do not restart failed routes without a new source or a claim whose conclusion needs that missing material. The 2026-10-11 audits establish functional-mode gameplay roots plus native reconstruction and select MMCC/Gaia B0 model recovery with separate B1 continuation. Local feasibility is now authorized; the [R03 execution record](../nu-history-feasibility-2026-10-15.md) owns actual launch, phase and same-state reconstruction evidence. The [seeded B1 pair](../nu-history-continuation-2026-10-15.md) now agrees for twenty logical steps with one predicted managed wall bounce. Native contact, audio, input/RNG and host rollback remain unestablished. |
| **B05 Game architecture alternatives:** which mechanisms actually differ? | S68’s dated 108-language map, S268’s industry review, exact engine/rule/monitoring routes and bounded forward graphs broaden the comparison beyond functional worlds versus ECS. Short-name noise and graph caps remain explicit. | Casanova, Join Token, ECS/DOTS, SGL, Micro-Machinations, Rulebook, managed rendering and selected authoring tools have primary reconstructions. S296 adds state exploration in Godot; S297 adds an implemented imperative replay prototype and a proposed ownership alternative. [S272/S273](full-reading/S272-S273-mvc-conformance-access.md) now reconstruct MVC separation and structural conformance, including retrospective refactoring and a small student comparison. Their quality metrics are not behavioral maintenance outcomes; S273’s registered thesis identity is supported by catalog/deposit and internal lineage while its title leaf remains absent. [SuBViS/BPAlt](full-reading/S275-bpalt-partial-method.md), [NCAlt](full-reading/S282-ncalt-access.md) and NodeGit now have complete primary methods, with distinct graph, class, snapshot and runtime boundaries. SceneGit’s method and reported evaluation are now fully reconstructed. Ceptre’s resource/stage method and original editor study are now reconstructed in S291–S293; the editor-image supplement and study-reporting differences remain explicit. | Declarative rules, coordinated updates, editable mechanics and history tools have predecessors. Runtime, usability and selected task benefits coexist with integration, learning and adverse-workload costs. A distinctive combination is possible; general invention or superiority is not established. | Reuse the completed Ceptre and architecture/alternative-authoring comparisons. Keep conformance-rule correctness, structural conformity and accepted behavior separate, and do not pool the repeated MVC case or the monitor/alternative-tool lineages. Reopen a generation/authoring or other discovery gap when the chosen claim needs its missing method. Preserve specific access gaps and scoped positive results; another engine benchmark needs a comparable workload or missing mechanism. |
| **B06 Runtime and resource costs:** where do costs move? | C03/C06/C07/C11 and the runtime, managed-rendering and CoreCLR screens cover selected collection, lifetime, rendering, build and monitoring workloads. Noisy prefixes and exact-query exhaustion are not global coverage. | S138–S151/S211–S214, S237–S248, S260/S261 and S281 reconstruct important mechanisms and tradeoffs. [S240](full-reading/S240-endless-runner-pooling-partial.md) and [S265](full-reading/S265-unity-build-energy-partial.md) now have complete publisher/visual readings. S240 reuses the same Task Manager image for both conditions and supplies uncontrolled profiler snapshots; S265 measures CPU+GPU power and throughput, with one figure/classification disagreement and incomplete raw/replay access. S279/S280’s complete readings reconstruct monitor/producer boundaries but leave exact measured-build and finite-ending policy gaps. | There are real workload-specific gains and adverse cases. FPS, frame tails, working-set quantiles, power, total energy, edit latency and total labor are different outcomes. Retention, tracing, preparation and host work must be charged to the appropriate boundary. Nu-specific cost remains unmeasured. | Use existing costs to define the boundary of a Nu value claim. Match work and observation windows; separate total energy from average component power, derived energy per frame, live counts and cumulative allocation. Count producer export, monitor computation, backpressure and tail latency separately. Seek another runtime source only for a missing mechanism or comparable workload; keep exact-build/raw gaps explicit rather than treating an unrelated allocator result as a Nu estimate. Use the 2026-10-11 same-mode retention/rebuild cost boundary and native-integration issue chain; runtime magnitude, release and resumed-frame effects remain unmeasured. |
| **B07 Specification, testing and oracles:** what warrants a pass? | C10 covers 100 titles/31 abstracts with continuation open; exact oracle, temporal, fault-sensitivity and game-practice routes add primary methods. Missing abstracts and later pages retain their recorded scope. | Temporal checking, contracts, mutation/guided testing, S220/S222, S252, S277–S281 and [S294](full-reading/S294-industrial-game-regression-testing.md) supply concrete observation methods; S296 adds a relevance frontier whose supplied actions and represented variables determine coverage; S294 adds industrial hybrid regression-test scheduling, event counts, interface identity and recovery. Original LOFT remains access-limited. [S279/S280](full-reading/S279-S280-game-runtime-monitoring.md) are now fully read, including the journal formulas and original visuals. Missing finite-ending/reset policy, empty-domain vacuity, exported-snapshot coverage and exact experimental builds remain explicit limits rather than unread-method claims. S273’s day-level conformance counts and S286’s matching oracle check represented structure, not delivered behavior. S298 supplies a concrete example of disabled/excluded diagnostic opportunities and a narrower released checker than the paper’s broader discussion. | Selected fault detection and tolerances are positive findings. Compiler acceptance, replay, coverage and visible changes are incomplete evidence for intended behavior. Trigger coverage, clocks, resets, identity, unfinished obligations and inconclusive observations require explicit treatment. | Apply those observation obligations to each retained continuation claim, including Ceptre’s now-reconstructed model/host boundary and existence-versus-all-traces distinction. Follow the exact missing formula/version only when it changes that claim; another generic monitor cannot certify an unobserved Nu outcome. Preserve diagnostic configuration and omitted predicates as coverage boundaries. S299 now resolves the selected formal-composition dependency: new behavior entails old guarantees and relevant exit predicates match. Its reported example is not independently executed. Apply the 2026-10-11 satisfying/violating/inconclusive source traces; require a witnessed trigger/domain, phase and explicit trace-ending/reset policy before interpreting a finite pass. Selected requirements, tolerances and later sensitivity validation remain necessary; runtime fault-control results belong in their separate execution record. |
| **B08 Debugging and live development:** does visibility improve iteration? | Tool/practice lineages, C01/C02, live-model citations and versioned Blueprint routes cover several debugging, adaptation and collaborative-authoring approaches. C01 now supplies selected state-exploration/live-replay methods through S296/S297; bounded search and edition limits remain. The S42 exact primary/artifact route is now complete at its recorded scope. | Live state/model/document methods and S199/S202/S203 are reconstructed. S283/S284/S287 provide selected authoring outcomes; S293 adds successful editor-supported model changes after training, with assistance and prerequisite limits. S288 and S289/S290 add practice context. S296 reports useful flaw finding, undo and commercial-game queries; S297 demonstrates replay after edits but leaves its full graph/interface and comparison to future work. S218/S219 are now complete primary readings. SuBViS/BPAlt/NCAlt now supply complete alternative-authoring methods and preliminary favorable ratings, with assistance, order effects and null efficiency/ease contrasts explicit. NodeGit adds favorable generated matching and curated merge results without user or conflict-repair evaluation. Class replacement, copied graph alternatives and offline document merges do not retain arbitrary running state; selected videos and evaluation data remain unexamined. SceneGit supplies favorable fixture/acceptance results, but no observed user conflicts or comparative total-work outcome. S298 demonstrates data-compatible interaction substitutions without a developer comparison; its exact demonstration-build correspondence remains unresolved. [S42](full-reading/S42-stream-debugger-comparison.md) adds all thirteen publication pages and nine selected artifact files; raw statistics and exact executed-build correspondence remain unverified. | Useful localization, collaboration and instructed history use coexist with nulls, navigation friction and preparation/coordination costs, including S296’s substantial mechanics-isolation work. Stored or visible history does not establish valid merging or running-state preservation. A tool bundle’s effect cannot be attributed to one feature. Initial failing-object knowledge reverses S42's package ranking. | Separate Nu’s available capability, intended workflow and measured outcome in synthesis. Preserve source/visual access gaps; pursue them when they could change the particular comparison, rather than repeating the now-completed McKenzie method assignment. Prepare R03's initial-information, repair and recovery contract; the generated test agreement in S42 is distinct from an independent behavioral oracle. Gaia history and in-process access are source-located, and the selected MMCC application contract binds immediate recovery versus continuation. Ordinary agent transport remains unverified. The seeded B1 pair now agrees for twenty declared steps; the new R10 pair preserves a halted checkpoint across one reward-rule reload and matches fresh reconstruction. Their limited model/projection and phase observations do not establish native-state preservation or benefit. |
| **B09 Coding agents and language effects:** what transfers from conventions and feedback? | P/S discovery, C05/X01 and exact type/context, API-evolution, translation and game-agent routes cover selected close methods. C05’s 100 supplied records are screened; later pages remain open. R21 adds exact-title/arXiv retrieval for S302/S303 and a bounded instrument-repository check; broad AI-method coverage is not claimed. | Agent/game methods, S229–S244 and bounded artifacts are reconstructed. Final-edition correspondence, functional-judge/raw-execution records and exact implementation/budget packets remain missing for specified studies. The [R08 controller audit](../nu-agent-information-and-feedback-contract-2026-10-11.md) now reconstructs retained candidate authority, visible replay, diagnostic formatting and post-stop scoring from pinned source. S302/S303 are complete in their selected preprint editions. Permission, human contribution, observed interaction and measured agent behavior are distinct. | Useful test/feedback/type-context results coexist with adverse cells, regressions and unequal budgets. Human effects, source size, traffic and retained context do not establish a fixed-agent language effect. Preserve E/H adverse evidence. D1’s explicit-case versus equivalent catch-all effect remains unknown. Those implemented no-tools/full-file semantics do not establish the proposed ordinary-tool Nu workflow; current diagnostics, ordered observations and final scores have separate roles. Repeated suggestions can influence confidence without providing independent coverage; qualitative modes are not a language or productivity effect. | Reuse the source/diagnostic/behavior/budget distinctions. Follow a missing edition or raw record only for a material inference. Local mechanism construction is now authorized: [R04](../nu-diagnostic-feasibility-2026-10-15.md) supplies bounded authored cases. Actual Nu source equivalence and candidate execution remain separate gates; unknown transfer does not require a generic agent search. R08 now needs a separate workflow/feasibility decision on actual tool/edit/observation authority, with final scoring resourced independently and historical/backend constraints preserved. Use the [R21 measurement contract](../nu-steering-measurement-contract-2026-10-11.md) for a future practical steering comparison; instrument/participant validation remains deferred. |
| **B10 Maintenance and adoption in practice:** what work do practitioners face? | SC167–180, SC189 and exact tool, reuse, model/code, studio and AR/VR routes cover selected professional accounts and interventions. SC189/SC235/SC239/SC250 extend the retained query through position 100 of 179; later coverage remains open. W725–W740 and SC229–SC231 add the McKenzie lineage. R14 adds three narrow public Nu issue queries, all 71 distinct titles and fourteen complete discussions, plus selected wiki/script evidence. S302 adds a selected OSS field intervention; S303 adds laboratory interaction methods, with different task and population boundaries. | Professional maintenance, S249–S259, S267/S271/S288, the complete supplied-PDF S289/S290 methods and S294’s reported production-test deployment are reconstructed. [S253](full-reading/S253-tools-expectations-reading-2026-10-15.md) and [S254](full-reading/S254-game-reuse-reading-2026-10-15.md) now have complete final-publication/main-visual coverage. [S263/S264](full-reading/S263-S264-phylogenetic-generation-reading-2026-10-15.md) reconstruct the generation methods and shared dataset; [S266](full-reading/S266-game-development-problems-reading-2026-10-15.md) reconstructs the extended preprint corpus, source shift and denominator inconsistencies. Instruments, released rows and selected artifact correspondence remain gaps. S180/S182 are acquired but unread, not automatically required. S295 adds selected JPA-history vocabulary coverage, not observed migration success or maintenance savings. S296 adds one commercial-game developer’s useful queries and integration burden. S300 supplies professional comprehension/modification evidence with prepared COBOL tasks, a fixed 35-minute modification period and partial-credit scoring; S301 adds a positive documented-interface intervention in two student samples, with distinct time and correctness/structure endpoints. Their native editions, instruments and selected artifact checks are reconstructed; final-edition/data correspondence and numerical reconstruction gaps remain in the notes. | Preserve favorable prepared-tool/feature outcomes, useful adaptations and reuse, with testing, skill, merge, prototype and operational costs. Labels, preferences and retrospective reports have their own value but do not establish net causal savings or present population prevalence. Publication/sample overlap remains explicit. Corrected public reports, mixed history-value accounts and existing asset automation constrain task/adoption claims; issue counts do not supply independent beneficiaries. Favorable S229 expert work and adverse S302 timing coexist at different scopes; they do not identify net Nu adoption value. | Apply the [R14 provenance/eligibility record](../nu-practice-and-task-provenance-2026-10-11.md) to a concrete practical case, preserving authored/adapted status, missing roles and total work. Asset upkeep is conditional; broader independent adoption coverage remains open. Resume the practice query at offset100 for a consequential population/mechanism gap. The selected generation/corpus methods are now reconstructed; follow missing raw records when an exact inference needs them. S294’s selected testing method is already reconstructed. Preserve context, review, rescue and concurrent-work accounting when a concrete beneficiary justifies future steering feasibility. |
| **B11 Architecture choice and assessment:** when is information worth its cost? | Earlier D2 audits, design comparisons, metric routes and professional practice provide decision foundations. Their coverage is bounded and does not reopen selection construction. | P02/A01/S01–S30, S83/S154–S156/S185 and professional workflow/operational studies are understood at their scopes. Conditional selection methods remain deferred. S288–S290 make representation access and adaptation costs concrete. | Architecture value depends on change families, available information, setup, coordination and recovery. Within-system correlations and prepared-task gains do not calibrate early choices or net lifecycle benefit. Transition can move cost across components and roles. | Use the consolidated claim-to-outcome assessment for scientific disposition, with explicit change and cost boundaries. Keep any Nu recommendation conditional on its population and workload; A0/D2 construction remains deferred. |
| **B12 Empirical and synthesis methods:** what is the unit and conclusion? | Primary bibliographies, dependency/context checks and answer-scoped audits account for considered decisions. Exact query/page/graph limits remain in the ledger; there is no field-completeness claim from accepted citation counts. R21 exact primary/instrument retrieval is recorded separately from six failed paper-search connectors. The walkthrough continuation records exact lookup/recall and draft/final access separately. | Allocation, missingness, outcome definitions, editions, reused datasets and passive reconstruction are recorded in the linked notes. S268/S276 resolve the review/classification methods. S289/S290 add two linked publications without establishing independent participants; both now have original publication/visual coverage, while instruments and participant overlap remain unresolved. S292 explicitly summarizes S293’s one eight-person study, with unresolved logic-background and timing-description differences. S295’s multi-label histories and artifact arithmetic preserve the difference between category coverage, safe changes and independent empirical cases. S296’s three demonstrations and one development account are not controlled replications; S297’s implemented prototype and hypothetical interface remain distinct. S298’s implementation/examples and selected release are distinct from formal soundness, diagnostic accuracy and a comparative change outcome. S299 supplies a model-relative preservation theorem and illustrative checks; S300 supplies one 24-person repeated-measures experiment, with measured comprehension change and partial modification progress rather than an assigned comprehension treatment or independently verified completed-change endpoint. S301 separates elapsed time, correctness and structure conformity; its printed quality-score inconsistency and unacquired raw packet remain explicit. S42 has twenty developers with sixteen repeated conditions each, not 320 independent participants; its selected source bounds timing and test-based completion without reproducing raw results. S302/S303 supply codebooks and coding procedures without reported independent agreement statistics; S303 released duration/event code has concrete qualifications. S304/S306 now resolve the original/final walkthrough protocols with shared ChemTrains lineage. S305’s 30 analytical walkthroughs are read at the report edition, with no observed users. S309 now supplies seven-system structural/face checks without developer outcomes; S308's method remains access-limited, as specified below. S264 extends S263’s dataset; S266 merges 67 new documents with the reused 200-document S250/S251 corpus. Publications, editions and merged rows do not establish independent replication. | Keep positive, null and adverse results at their actual scope. Nonsignificance is not equivalence; selected-success measures are not all-assignment effects. Reused participants, frames, model outputs and publication editions are not independent replications. Public issues, corrected reports and tasks derived from them retain their thread/beneficiary lineage; issue closure is not patch or runtime validation. Static reconstruction and documentation checks do not validate execution. Observable actions, reported intent, retained output and checked correctness are distinct. Descriptive interaction modes and a codebook do not validate a steering scale. A qualitative prerequisite inventory and useful design changes do not validate readiness or predictive accuracy. | Apply these distinctions to the Nu assessment and any later proposed measurement. Preserve exact source/version gaps in the reading index rather than duplicating every paper’s defect list in this map; report new considered decisions once. Apply the R21 observation/reliability and R07 knowledge/assistance contracts; select the practical estimand and resolve instrument/task/person variation before choosing participant numbers. Resolve exact original protocols when their validation claims are needed. |

**Priority reconciliation, 2026-10-08:** the earlier SceneGit and repeated McKenzie instructions are superseded. S285 records SceneGit’s access boundary; S286 reconstructs available NodeGit source; S287/S288 and the completed supplied S289/S290 publications now supply the selected authoring/practice methods. S289/S290’s former visual/file gaps are resolved; instrument, participant-lineage and accepted/publisher byte-equivalence limits remain distinct.

**Ceptre priority resolved, 2026-10-08:** [S291–S293](full-reading/S291-S293-ceptre-resources-and-editor.md) supplies the resource/stage semantics, external-input boundary and original editor study. The local frame property does not preserve every possible trace, and staged programs lose the composition guarantee. The stage-less editor supports real successful model changes in one eight-person study; later publication does not add an independent replication. Original supplement, publisher editions and unreconciled prerequisite/time descriptions remain explicit.

**Claim-directed gap disposition after S295–S297, 2026-10-08:** these passes reuse existing gaps and resolve selected persistent-object, state-exploration and live-replay methods. It is not a new access retry or a declaration that all discovery paths are covered.

| Remaining frontier | Consequence for the Nu assessment | Current disposition and executable next action |
| --- | --- | --- |
| S263/S264 generation methods | Generation validity, reusable assets and setup/maintenance work can change the game-authoring comparator and cost boundary. | Their selected full publisher methods are now read. Preserve heuristic validity, expert assistance, reused cases and setup costs; exact build/raw-data and edition correspondence remain claim-specific dependencies. |
| S266 expanded postmortem corpus | Source selection, reused reports and problem coding can change practice coverage and transfer claims. | The complete selected 33-page preprint is now read. Source/time confounding, unreconciled denominators and source/coding lineage limit its profiles; it is not an independent benefit estimate. |
| Type and stored-state evolution | A class edit, stored-data correspondence and live continuation need different contracts. | S295 now supplies the retained abstract/concrete persistent-object method, explicit defaults, exclusions and selected-history evidence. Reuse it with S71/S86/S87/S102/S103/S108/S236. Signal Classes, ESCHER and typed-editor leads are conditional on a claim needing their original mechanism, not an automatic reading chain. |
| Temporal and live-state primary editions | Exact event order, observation horizon, reset, identity and unfinished obligations can change what a pass warrants. | S218/S219 originals now resolve their earlier text/visual gaps. S279/S280 exact PDFs are local and their readings await integration. Original S221, exact builds, reset/finalization semantics and selected supplements remain separate; follow the missing definition that can change a Nu claim. |
| Remaining discovery coverage | An unexamined route can still hide a consequential alternative or adverse outcome. | The retained C01–C11 audit now identifies selected primary gaps instead of treating 1,295 occurrences as full understanding. S298–S300 now resolve the selected interaction, preservation and comprehension/modification methods; S301 now supplies its original documentation-treatment methods and outcomes. The ledger preserves thirty-one selected passage dispositions and conditional alternatives. Further practice retrieval starts at offset100 only when it can change a named claim; later pages remain unexamined. |
| Nu-specific empirical value | Whether the available mechanism/tool combination improves a stated change and workflow at acceptable total cost. | This remains empirical after literature synthesis. Confident local construction is authorized and bounded feasibility results are recorded; comparative cost/benefit, paid candidate/model runs, recruitment and future steering remain separate. Missing Nu measurements alone do not justify endless retrieval. |

**State-exploration/replay priority resolved, 2026-10-08:** [S296/S297](full-reading/S296-S297-state-exploration-and-live-replay.md) supplies two retained C01 alternatives. State Explorer reports useful flaw finding, undo and level checks, with substantial work to isolate mechanics from animation and host dependencies. The liveness prototype reconstructs play from a recorded event log after reinitialization; its graph/interface and comparative evaluation are unfinished. These methods make the integration and observation cost concrete without estimating Nu’s benefit. The cached screen and SC239 continuation are recorded with their exact retrieval scopes in the ledger.

**Coverage disposition after the selected readings:** S300’s comprehension/modification experiment and S299’s modular replacement contract are reconstructed and integrated in the Nu claim-to-outcome recommendation. S301’s newly supplied PDF resolves its original modular-rule experiment; S289/S290’s supplied editions resolve their visual/file gaps. Keep S263/S264 and S266 as specific primary-access gaps. S298’s interaction substitution/checking method is resolved at the manuscript and selected-source scopes. Additional retrieval needs a consequential missing comparator, contract or outcome; Finnish/Musil practice, XRSpotlight, ABL, formal Micro-Machinations, persistent-state testing theory and Praxish remain conditional, not discarded or mandatory batches.

This coverage reconciliation does not certify field completeness; completed main-paper readings and their limits are recorded in the index. It separates remaining discovery/primary-understanding work, specific access/version/observation gaps, and Nu-specific empirical benefit that the inspected literature does not measure. The last category alone is not a reason for endless adjacent retrieval. A bounded coverage conclusion still needs the relevant search paths and consequential alternatives accounted for; all experimental and worker holds remain.

### Current claim-to-outcome assessment

The source boundary remains Nu revision`064f7ae92a8506689cd91aff5e6804a375d6ef3d`, with the [pinned source account](../nu-grounded-maintenance-methodology-2026-09-14.md#a-potentially-simpler-contrast-already-exists-inside-nu) and separately dated [practitioner claims](../nu-form-factors-and-research-leads-2026-09-14.md#1-what-the-nu-sources-actually-motivate). The following is synthesis of inspected evidence, not a new Nu source audit or an executed comparison.

| Nu value question | What the evidence supports | What remains to establish |
| --- | --- | --- |
| Do explicit domain representations and ownership make consequential changes easier? | The source offers concrete organization choices; information hiding, type guidance and task-dependent organization benefits have predecessors. S83/S155/S156 and professional studies preserve favorable outcomes and counterexamples. S300 supplies positive comprehension-gain/progress associations under predicted cognitive fit and negative associations under mismatch. S301 adds favorable outcomes for explicit rule grouping/interface documentation in two student experiments. | The relevant change families, information obligations and total cost in Nu. A correct catch-all and other valid organizations remain admissible; a diagnostic is not the required behavior. S298 additionally separates data-compatible substitution, enabled runtime checks and intended interaction semantics. S300’s partial progress and measured comprehension change do not identify verified-completion time or a causal comprehension effect. S301’s documentation contrast does not identify software-enforced encapsulation; its elapsed time and structure-conformity score require separate interpretation. |
| Do coordinated world/rule updates reduce conflicting interactions? | SGL, Casanova, Join Token, Micro-Machinations and Ceptre establish alternative coordination mechanisms with explicit order, reset, resource and host boundaries. S299 supplies a formal preservation alternative under modeled behavior, world assumptions and compatible module exits. | A precise Nu contract and comparison at equivalent behavior. Ceptre’s local composition property and whole-stage limitation are explicit. S299 shows what a stronger model-relative guarantee requires, without measuring its specification/verification effort. No universal uniqueness or whole-system preservation follows from a functional-world label. |
| Does history support useful recovery or continued development? | Persistence, document histories, snapshots, replay, migration and restricted compensation are established capabilities with different guarantees. Authoring studies supply useful selected collaboration/history outcomes. S296 supplies state exploration/undo; S297 supplies edit/reinitialize/replay, with different retention and input boundaries. | Which values, pending work and effects a Nu workflow needs to retain; its diagnostic/repair benefit and retention/recovery costs. Stored history alone does not settle those questions. |
| Does locality or interactive feedback improve iteration? | Tool-assisted localization, prepared workflows, collaborative authoring and S293’s editor-supported model changes have favorable scoped evidence alongside nulls and friction. S296 reports useful queries and a substantial mechanics-isolation burden; S297 separates its implemented replay prototype from a planned interface. S288–S290 make skill, handoff and adaptation boundaries explicit; S292/S293 expose prerequisite, assistance and study-lineage limits. | Benefit attributable to the available Nu representation/tool combination in its intended workflow. Shared engine capabilities cannot explain an MMCC–ImSim difference without differing use. |
| Does the package offer net value, including for coding agents? | Runtime and development evidence identifies credible tradeoffs and useful capabilities. Existing E/H compactness counterevidence remains valid; measured task outcomes and practitioner accounts retain separate scopes. | Setup, integration, learning, change correctness, runtime and recovery costs within one stated comparison. Literature supplies mechanisms and comparators; it does not provide the missing Nu-specific effect estimate. |

The defensible current claim is an **available combination of mechanisms whose value depends on the change and workflow**. Nu offers domain representations, ownership/programming-model choices, coordinated engine facilities and explicit world/history mechanisms in an integrated game-development setting. The inspected prior art supplies concrete alternatives for each broad capability; this does not make the package valueless. Its useful differentiation could be a combination that reduces real change or recovery work under stated conditions. Neither general invention nor comparative Nu advantage is established, and absence of a Nu effect estimate is not a null result.

### Scientific disposition and remaining work

**Coverage judgment, 2026-10-08:** the current characterization is ready for scientific disposition. B01–B12 now have accounted discovery routes, primary mechanisms and consequential alternatives, positive/null/adverse outcomes, transfer boundaries and executable residual actions. The retained-route pass selected S298–S300 because they could change the substitution, preservation and comprehension-to-change claims; their original methods are now reconstructed. The conclusion rests on those source-to-claim links, not the reading count, an empty queue or D1 sufficiency. This is the maintainer agent’s bounded assessment, not a supervisor’s certification, exhaustive search or human approval.

The conclusion is deliberately limited to the pinned Nu source and the literature/editions actually inspected. Unexamined search continuations remain in the ledger. The supplied S301 and S289/S290 publications now resolve their original body/visual gaps. S263/S264’s generation methods and S266’s larger corpus retain specific primary-access gaps; the table above also retains missing visuals, exact experimental builds, supplements and edition bindings. These prevent stronger claims about those methods, general priority and population-wide superiority. They do not turn unknown Nu benefit into negative evidence. Reopen the exact dependency when a new accessible source appears or the chosen claim needs it; do not relabel it resolved or repeatedly retry the same denied route.

The user's follow-up directs **preparation of the plausible research directions together, prioritized by research value**. The [ranked agenda](../nu-research-agenda-2026-10-08.md) now carries 21 direction cards and their dependencies, with detailed R01–R06 designs and future R21 steering research. The immediate emphasis is mechanisms/costs and bounded agent changes; human-steered development remains the intended eventual context rather than an effect already measured by agent tasks. A Nu workflow/package comparison includes integration, tooling and learning differences. The existing MMCC/ImSim pair shares the language and engine but differs in movement/collision implementations; it is not a validated equivalent maintenance baseline. D1 addresses explicit-case enumeration versus an equivalent catch-all for a fixed coding agent. Both can be exhaustive. These questions retain distinct interpretations and do not establish whole-Nu or F#/C# superiority.

For a later approved comparison, retain new and old behavior obligations, temporal/identity/effect boundaries, all assigned attempts and missingness, and complete setup/integration/learning/change/recovery costs. Useful intermediate observations—diagnostic exposure, source size, understanding, partial progress or one successful trace—must remain distinct from correctly completed changes and net cost. The strongest rival is displaced work or a tool/task/experience difference, so source equivalence and the outcome boundary need separately authorized feasibility evidence before candidate runs.

**Remaining work:** the [comparison/outcome packet](../nu-research-study-designs-2026-10-08.md) is prepared. Use the completed source/comparator/native audits and selected MMCC/Gaia history contract. Apply the task-diversity audit's second application/site, baseline mismatch register and public platform/gravity requirements. The [platform contract](../nu-platform-contract-2026-10-11.md) now resolves the source route and common carrying/jump/pause/removal semantics, using R05/R06's phase/identity/cost specifications. Actual carrying and observation access require separately authorized feasibility; two related demos are not representative coverage. R03's selected B0 launch/phase/access and B1 continuation now require later authorized feasibility, not another generic history inventory. Current source-inspired task sketches are not verified mined issues or tested successors. Follow literature dependencies when they can change these designs; retain R01's broader adoption question and R21's deferred human-effect claims. Execution requires a separate decision on a reviewable study, its feasibility and allocation. No A0/A1/D1 construction, recruitment, added worker, model probe, candidate run or H execution follows from this preparation. Existing E/H results and adverse compactness evidence remain unchanged. An absent Nu measurement cannot be supplied by adjacent literature.

**Reading priorities during agenda preparation, 2026-10-08:** prepare the distinct proposals with an identified Nu capability, intended users/change families, comparator and outcome. Existing evidence supports that work. Further reading resolves each design's dependencies before methods and stronger claims are fixed; the following sources are not a mandatory batch for every direction.

| Proposed claim or method | Consequential remaining reading | Gate it can resolve |
| --- | --- | --- |
| The expanded postmortem corpus supports contemporary task priorities or prevalence claims | [S266's expanded postmortem corpus](full-reading/S266-postmortem-extension-access.md): full paper and source/coding lineage. A newly found SSRN delivery URL still returns 403; only its abstract is available here. | Source/time mix, reused reports, coding and denominators must be understood before treating the expanded corpus as evidence of changed prevalence or representative task selection. Existing practice evidence can support a narrower motivation meanwhile. |
| Nu improves content authoring, asset reuse or generation | [S263/S264](full-reading/S263-S264-content-generation-access.md): original representations, generation/validity checks, comparator and evaluation units. | These could change the relevant alternative and the cost boundary. The newly located JISBD summary deposit is a lead, not the full SPLC paper or an independent study. They need not block a maintenance-only proposal. |
| GUI agents or playtesting supply the development baseline or final evaluation | [S227 v2 is fully read](full-reading/S227-continual-gui-playtesting-v2.md), with separate edition identity and the v1 comparison. The current primary release still matches the inspected static gallery. | Use the expanded judge validation and clarified feedback/final-scoring separation. Gain-plot correspondence, human plot/prose direction, early-stop population, complete resources and the unreleased scaffold remain unresolved; validate actual Nu observation/transport separately. |
| A specific competing history, temporal-checking or type-evolution mechanism is central to the treatment | Its exact primary method/edition, if still partial in B02/B04/B07/B08 above. | Reconstruct the comparator's state, effect, observation and change contract. The existing S71/S86/S295–S299 methods already support substantial comparisons; another generic paper is not an automatic prerequisite. |

For a Nu maintenance/iteration proposal, the immediate work is to apply the already read outcome and comparison methods, including S300/S301's distinction between understanding, partial progress and completed correct change. Selecting the exact comparator can promote a currently conditional source. Reopen the focused novelty/edition check before stronger priority or publication claims, rather than asserting that every relevant work has been exhausted.

Results require evidence from the stated Nu comparison. More literature can improve its design and interpretation but cannot supply a missing Nu effect estimate. A favorable result, a null or an adverse result must all remain admissible. The proposal can advance while explicitly carrying a nonessential access gap; an unread dependency essential to its method must instead be resolved or the claim narrowed. Existing execution holds remain as recorded in PLAN.

## Progress and evidence rules

The [search ledger](nu-background-searches-2026-09-30.md) records query ranges and screening states. Thirteen native Consensus calls requesting 100 records per page have returned **1,295 occurrences**. All titles were inspected; selected supplied abstracts/index text were consumed as enumerated in the ledger. These are retrieved occurrences, not full readings or independent studies. The old twenty-result app interface and the new native interface have different pagination affordances. No year, citation, venue-quality or publication-type filters were applied to the native searches.

Maintain stable P/A/S reading identities. New broad-search occurrences have query/position identities until editions and existing Zotero holdings are verified. A result receives no methods/effect credit from a title or abstract alone. Preserve full primary PDFs outside Git and attach relevant records through the existing native Zotero API authorization. Organizing a record never automatically marks it read.

Completion requires an inspected source-to-theme map across this full background, accounted search/citation paths, primary examination of consequential leads, credible opposing mechanisms, and explicit residual empirical/access uncertainty. Missing coverage is not completion. A broad search prefix, citation count, the existing 62 readings, or narrowing a proposal cannot alone certify that the background has been surveyed. Global proof that no further paper exists is not available from these services.

## New primary claim coverage

| Claim / theme | Evidence read | Disposition and unresolved comparison |
| --- | --- | --- |
| B04/B08: explicit functional state enables live program replacement | [S71](full-reading/S71-live-state-migration.md), all main/appendix pages | Prior type-directed live-state migration is established; Nu-specific distinctions require actual correspondence, defaults, control-state and external-effect boundaries. |
| B02/B07: types or retained state ensure valid behavior after an edit | S71 main §7 and control-flow examples; appendix restrictions | The general inference fails: migration preserves required types, not invariants absent from them. Independent old/new obligations remain necessary. |
| B06/B10: live migration yields net maintenance/runtime benefit | S71 demonstrations, limitations and proposed testing | No comparative effort, runtime or retention estimate is supplied. Value and cost remain unmeasured. |
| B02/B04/B08: schema evolution is solved by preserving well-typed state | S73 challenges 1–8; completed S71/S85/S86/S99/S102/S103/S108/S236 methods | Code, data, intent and version compatibility impose separate duties. S71/S85 require explicit migration policy; S86 retains partial/failed transfers. S99 has bounded editable scope and local replay. S102 acknowledges scalar/list inconsistency; S103/S236 retain hidden information and best-effort cross-view policy. S108 supplies correspondence/merge rules. S87 now adds reference-aware document/computation evolution and dependency invalidation, explicitly distinct from preserving arbitrary live evaluation state. |
| B01/B10/B11/B12: experience identifies the better maintenance design | S81 Tables 4–7; all fourteen pages | Centralized control has higher complete-chain success. Planned experience interaction p = .133; post hoc regrouping p = .028. Correct-only timing does not establish all-assignment benefit. S88 is a different-protocol replication of the 2001 predecessor; its RD-favoring score at alpha .10 and missing effort data do not yield commensurate pooled success rates. |
| B01/B10/B12: parameters or lower coupling guarantee faster changes | S82 three cohorts and Tables 1–3, all eight pages | No consistent effect for one PL/I simulator; initial favorable timing did not replicate. One interface dimension does not dispose of broader information-hiding interventions; S92 now adds distinct structural and effort outcomes, while the S90/S193 continuation below now preserves task-specific positive results and a smaller inconclusive external replication. |
| B01/B02/B06/B11: change-locality and logical/physical separation are novel mechanisms | S89 complete 1972 journal | Both mechanisms have explicit prior art; anticipated-change selection, semantic interface obligations and implementation overhead remain separate. No Nu/agent effect follows. |
| B01/B02/B10/B12: inheritance uniformly improves maintenance, or a null comparison proves equivalence | S84 all twelve pages, Tables 1–5 and both figures | Shared-report changes favor inheritance; a single inherited-behavior change favors flat correctness. Different cohorts/tasks, deterministic assignment and partial-credit scoring limit transfer. Five-per-group nonsignificance does not establish equivalence. |
| B01/B11/B12: design metrics demonstrate maintenance benefit or validated prediction | S91 all eight pages and Tables 1–4 | Same-project stepwise fits explain variation in integration-period modification counts; causes are unclassified and no held-out prediction or maintenance-time benefit is tested. Static scores and observed outcomes stay distinct. |
| B01/B02/B10/B12: information hiding guarantees retained structure or lower effort | S92 all seven pages and detailed outcome prose | Positive preservation/reorganization observations coexist with an unquantified effort null, eight missing participants and inconsistent aggregate counts. Site assignment, task asymmetry and valid alternative edits require explicit treatment. |
| B02/B03/B04/B06/B07/B08: a solver supplies intended state and seamless live continuation | S85 all thirteen pages, explicit migration examples, Figure 2 and selected 2018 source/data | Designer-specified constraints and policies guide a bounded solve; distance is a heuristic, pending work needs rules, and timeouts/resumption/effects remain distinct. Released aggregate labels and publication/source correspondence require caution. S99/S100 expose later alternative mechanisms. |
| B02/B03/B04/B07/B08: operation histories automatically preserve intended evolution | S86 all 34 v2 pages, eleven figures and Appendices A–E | Stable identities and directional rules enable selected transfers, while deletion/deduplication cases fail or decouple. Query evolution is partial; general programming-language cases, complete rules and benefit/cost evidence remain open. |
| B03/B04/B07/B08: checking retained current state establishes complete evolving behavior | S100 all six pages, property automata and selected dated checker-library files | Separate current-state from initial-state coverage, safety from liveness/fairness, and shared semantics from an independent oracle. One author scenario has no measured user/cost benefit; dependency, monitor-history and equality reductions need explicit conditions. |
| B02/B03/B04/B08: a generic graph merge supplies correct live migration without integration cost | S101 all nineteen pages, two listings and explicit limitations | Complete read/write capture is required; read annotations remain manual. Overrides permit continuation without old-trace reachability, and existing-interpreter porting can resemble rewriting. S108 now reconstructs dependency closure and correspondence overrides; its later deployed build checks prerequisites and hashes the updated target. The 2023 prototype simulates concurrency, with no comparative benefit/cost measurement. |
| B03/B05/B06: efficient bulk iteration guarantees cheap references or lifecycle safety | S76 all 34 pages, ten figures/eight tables and pseudocode | EnTT leads the largest linear workloads; the object baseline leads target access. Explicit version checks have low observed timing cost, while dead-target/component-removal behavior is not tested. Cache explanations and general maintenance benefits remain unmeasured. |
| B05/B06/B12: faster archetype frame updates imply lower tails, cheap ongoing changes or an intrinsic storage effect | S112 all nine pages, three CSVs and fifteen pinned source/config files | Released data support lower large-scale archetype frame centers and lower sparse-set creation costs. Archetype's high-scale maximum/SD are larger; ongoing component changes are not separately measured. Consecutive rows and demo/measurement differences limit inference. |
| B05/B06/B10: a faster data-oriented subsystem makes production migration worthwhile | S77 all 46 thesis pages, two timing tables and profiler appendix | Occupation is faster and hybrid rendering slower in a simplified editor-only test. The developer declines production migration on qualitative integration/learning grounds. This is a scoped decision with unmeasured total effort, not a general negative ROI or language effect. |
| B02/B07/B12: generation, compilation or retained old tests supply a complete evolution oracle | S104 all nineteen publisher pages; S46/S47/S53/S100 temporal methods | Specified, derived, implicit and human judgments have different assumptions. Undefined observations are not passes; changed requirements may replace old verdicts. Independent validity, state/reset conditions and judgment costs remain necessary. |
| B02/B10/B12: a favorable typing average benefits every maintainer and isolates compiler feedback | S117 all ten pages and 33 printed participant rows | Preserve Java-favorable type repairs, five Java-slower overall completers and semantic-task order reversals. Declarations/checks, domain cues and tool opportunity are bundled. S126 confirms identical timing data and favorable launch/file-open results, but its file-switch table and new figure labels require reconciliation. S127 now establishes bounded gains from correct information alone and a wrong-information cost; its selected tasks and absent checking arm leave the checker increment unresolved. S128 now preserves the benefit in a richer combined environment, without isolating tooling/checking or navigation causality. S129 now separates observed total/component time from unobserved prior comprehension; its interaction remains nonsignificant. S130 now narrows the checker mechanism with common information, while attempted work, delivered defects and time remain separate outcomes. |
| B02/B07/B10: a partial match must be unsafe, or checker success proves intended behavior | S114 all twelve pages, four pinned files; S133 selected proof/translation passages | Program-context preconditions can verify partial matches; reported concrete crash repairs are useful. Changes that add defaults need separate behavioral justification. The normal-form proof premise, bounded-tested MP2 and first-order transformation limits prevent universal guarantees. |
| B02/B08: prior hot reloading never migrates through type changes | S73 p. 24 compared with S71 §§2–3 | The blanket characterization is inaccurate for its cited S71. Retain S71's actual type-directed capability and its semantic-invariant limits. |

S69–S74, S76–S82, S84–S86, S88/S89 and S91/S92 and S68/S100/S101/S104/S108/S112/S113/S114/S117/S123/S124/S125/S126/S127/S128/S129/S130/S131/S119/S135/S136/S115/S137/S138/S139 raise complete publication coverage to **107 works**. [S69](full-reading/S69-casanova-formal.md) establishes a game-world/rules/coroutine predecessor with generated optimization, not an isolated functional-language or maintenance effect. [S68's full author-edition survey](full-reading/S68-game-language-mapping.md) is complete, with the publisher-edition relation limited; S69's six-page Casanova paper and its two copies are fully examined; [S70's networking/encapsulation reading](full-reading/S70-casanova-encapsulation-networking.md) is complete, retaining generated-bookkeeping, external-state and unreliable-replica boundaries. [S72 type-authoring](full-reading/S72-functional-programmer-authoring.md) is fully read, including all figures and tables; [S73 schema evolution](full-reading/S73-schema-evolution-challenges.md) is fully read: eight challenges, no new solution or empirical effect, with an explicit correction of its S71 characterization. S72 documents wildcard/evolution risks and purposeful failing compilation. Its small pattern/combinator comparison did not reject the null for subjective workload (p = .083); the observed time difference is task-specific, and the causal mechanism remains unresolved. [S74 typed patterns](full-reading/S74-typed-design-patterns.md) are now fully read; S75 game bad smells remains incomplete; [S76 ECS references](full-reading/S76-ecs-entity-references.md) is now fully read; [S77 released-game DOTS migration](full-reading/S77-dots-migration.md) is now fully read. These were promoted with explicit claim/contrary-evidence roles and Zotero records. All six PDFs are now attached across S72–S77. The ledger preserves S75's placeholder-DOI/page-count edition discrepancy and S76's direct-download failure. Current holdings are 156 literature records, three public sources and 169 PDFs, plus four separate ZIP supplements, one corrected XLSX and one unread PostScript; acquisition alone does not increase full-reading credit. User-library attachments close the S76/S78/S79/S80 PDF gaps. [S79](full-reading/S79-maintainability-performance-case.md) and [S80](full-reading/S80-maintainability-performance-lineage.md) are fully read publications of the same parser case; [S78](full-reading/S78-structure-maintenance-outcomes.md) is also fully read, with its competing maintenance outcomes and aggregate discrepancies preserved. S81–S84 are selected foundation records, all with PDFs; S85–S87 add schema-evolution follow-ups, also with PDFs. The six newly present S82–S87 attachments have first-page identity/abstract coverage, with S82/S84/S85/S86 now fully read and S83/S87 bodies still pending, with S86 demo/video coverage separately open. [S81](full-reading/S81-control-style-experience.md) is fully read; [S88](full-reading/S88-control-style-replication.md) is fully read: it replicates the 2001 predecessor, with a different correctness score favoring RD at alpha .10 and unexplained effort exclusions. [S82](full-reading/S82-global-parameter-coupling.md) and [S89](full-reading/S89-information-hiding-decomposition.md) are complete. The [C09 screen](nu-background-information-hiding-search-2026-09-30.md) preserves 100 more discovery records and the new S89–S94 acquisition/reading roles. [S84](full-reading/S84-task-dependent-inheritance.md) is complete. Four more user-library PDFs close S91–S94 access gaps; [S91](full-reading/S91-structured-design-quality.md) and [S92](full-reading/S92-information-hiding-maintenance.md) are now fully read. S93/S94 remain pending, with S94 Poppler extraction partly repaired. S95–S98 extend the inheritance, industrial and encapsulation/distributed-language frontier; newly present S96–S98 PDFs have first-page coverage only. [S85](full-reading/S85-constraint-state-migration.md) is now complete, with a bounded dated-artifact check. S99 retains first-page coverage; [S100](full-reading/S100-live-model-checking.md) is fully read, with all figures and a bounded dated checker-library inspection. Its application source/demo are currently inaccessible. S105–S107 add temporal breakpoints, unified verification/monitoring and remote concolic debugging; S107 is acquired at first-page coverage, while S105/S106 now have user-library PDFs at opening-only coverage. S101–S104 add operation-based versioning, Cambria, BiDEL and the oracle survey. [S101](full-reading/S101-operation-based-live-models.md) is now complete; S102/S103 remain incomplete. [S104](full-reading/S104-test-oracle-survey.md) is also fully read in its nineteen-page publisher edition; its author edition remains separate. The eighteen-page core method [S108](full-reading/S108-blended-model-versioning.md) is now fully read, including twenty figures, Table 1 and 44 references. A bounded static check of two later deployed core modules closes hash/closure interpretation questions without executing or certifying the historical implementation. S101/S103/S104 have PDFs; S103/S104 publisher and author editions are retained separately. The [C10 screen](nu-background-oracles-search-2026-09-30.md) records 100 oracle/testing results and specific recall, edition and observation gaps. S111 adds a nineteen-page mobile crowd/variation thesis at verified cover/indexed-abstract coverage. [S112](full-reading/S112-ecs-storage-comparison.md) is now complete, with all three CSVs reconstructed and fifteen pinned source/config files inspected; its ZIP supplement is also attached in Zotero. Runtime experiments were not reproduced. S109 adds an eleven-page acquired human-oracle study at opening-page coverage; S110 adds an acquired model-steering record at opening-only coverage. The [C11 runtime screen](nu-background-runtime-search-2026-09-30.md) preserves another 100 records and 31 supplied abstracts. [S117](full-reading/S117-static-types-maintainability.md) is fully read with its 33-row table reconstructed; [S126](full-reading/S126-static-types-maintainability-journal.md) is now fully read in the publisher edition, confirming one shared timing experiment and reconstructing additional measurements; [S127](full-reading/S127-type-names-without-checking.md) is fully read, preserving information benefits, wrong-information costs and capped/absent attempts; [S128](full-reading/S128-typing-with-eclipse.md) is fully read with both 23-row tables reconstructed; [S129](full-reading/S129-documentation-and-typing.md) is fully read with all 25 columns reconstructed, retaining documentation use, favorable outcomes, exclusions/caps and cost/interaction limits. [S130](full-reading/S130-procedure-argument-checking.md) is fully read in its fifteen-page author edition, with bounded data-package reconstruction. [S113](full-reading/S113-gadt-pattern-coverage.md) now has full extended-version coverage and four pinned source/config files inspected; its diagnostic mechanism and selected-corpus improvement do not estimate maintenance benefit. [S114](full-reading/S114-partial-sufficient-matching.md) now has complete paper coverage and four pinned files inspected, with [S133](full-reading/S133-catch-proof-and-translation-partial.md) supplying selected proof/translation passages without full-thesis credit. [S131](full-reading/S131-deliberately-dynamic-typing.md) now has full publisher coverage, preserving mixed task benefits and source-data limits. [S119](full-reading/S119-compositional-pattern-coverage.md) is fully read in its updated author edition; [S134](full-reading/S134-lyg-proof-scope-partial.md) is a partial proof dependency, and [S135](full-reading/S135-pattern-analyzer-validation.md) is fully read with a bounded archive/issue reconstruction; [S136](full-reading/S136-intensional-datatype-refinement.md) now has complete publisher/v3-appendix coverage and a bounded public-source reconstruction; S132 has a fourteen-page university copy at opening-only coverage. S120/S121/S122 PDFs are now present, with S122 a chapter inside a whole proceedings attachment. Their full methods remain pending. Neither retrieval counts nor these acquisitions close any whole-background theme.

Casanova adds two consequential distinctions: source-level organization can be implemented by generated indexes, notifications and mutable buffers, so runtime algorithms are a rival explanation; local state consistency does not guarantee correct gameplay across delayed or lost network updates. S70's selected source-count and synthetic timing comparisons do not measure net maintenance benefit. Bibliography and broader ECS/data-oriented alternatives remain open.

The S79/S80 comparison is evidence of a concrete runtime difference between combined implementation choices, not observed future maintenance benefit. Its prediction uses source volume and imported productivity rates; a specialized generated parser also replaces threads with processes and receives limited verification. Component exchangeability, allocator choice, generated code, workload and production readiness are consequential rival mechanisms for B01/B05/B06/B10/B11. S78 supplies a direct controlled maintenance-outcome comparison: lower time and fewer serious ripple errors coexist with more primary failures and fewer completely correct submissions. Its paper-only workflow and selected timing subset require explicit boundaries; no Nu or agent effect follows. The [C08 discovery screen](nu-background-foundations-search-2026-09-30.md) expands the related empirical and methodological frontier.

## What the type and information comparisons establish

The completed human API lineage now resolves several alternative explanations without establishing a Nu or agent effect. These are related research programs and task families; publication counts do not represent independent broad replications.

| Comparison | Measured capability or outcome | Remaining boundary / consequential next source |
| --- | --- | --- |
| S117/S126: Java versus Java-like Groovy in a basic editor | Selected type repairs and API tasks favor Java; launch/viewed-file results preserve some benefits. | One shared timing experiment; declarations/checking and language cues are bundled, semantic results depend on order, file-switch labels are unresolved. |
| S127: correct or incorrect names without automatic checking | Correct names help two selected API tasks; wrong names slow one repair. | No checker-enabled arm; responsive predecessor tasks and caps/carryover limit generalization. S130 now reconstructs the checking-with-information comparator under a different compiler/wrapper/task setting. |
| S128: Java/Groovy with Eclipse, JavaDocs and ordinary names | Large favorable Java timing differences persist in a richer environment. | IDE maturity differs and changes are bundled; completion-count inference conflicts with the printed table. This does not make tool opportunity irrelevant. |
| S129: Dart typing × external documentation | Total time favors typing on one selected task; all documented attempts complete, while three retained undocumented attempts are capped. | Total documentation effect is uncertain and interactions nonsignificant. Subtracted viewing time is an observed component, not a prior-knowledge or amortized-cost experiment. |
| S130: argument checking with signatures/documentation retained | Fewer detectable residual defects; faster second-task delivery in the selected GUI-call setting. | Two compiler implementations, a checkable wrapper, learning and exclusions limit transfer. FU rate counts attempted units; correctness is a separate selected defect endpoint. Package/group correspondence is partly unresolved. |
| S132: scanner/parser development in a new language | Dynamic scanner time is lower among42completers;49-person parser scores show no detected difference, and full-project debugging intervals favor dynamic typing. | Interview-balanced groups, different training, completion selection and distinct endpoints; neither general dynamic superiority nor no static benefit follows. S206 is related partial-report lineage. |

S131 now supplies the dynamically favorable task-design counterweight, with results in both directions and no joint lifecycle estimate. S113 now resolves the first semantic dependency: coverage, redundancy and divergence differ, and error fallbacks can conceal added constructors. S114 now reconstructs sufficient reachable inputs and their proof/translation limits. S119 and its selected S134 dependency now resolve compositional coverage/proof scope. S135 now supplies implementation-validation evidence. S136 now resolves the constrained-refinement safety method. The next semantic dependencies are C02's extensibility/practice methods: diagnostic reachability, sufficient partial matches and future-case obligations differ from these API-construction tasks. Practical task prevalence, exact source/tool equivalence and agent transfer remain unmeasured; those empirical residuals do not excuse unread primary methods or unexamined search continuations.

## What the coverage-checking evidence establishes

[S113](full-reading/S113-gadt-pattern-coverage.md) supplies a direct predecessor for future-case warning loss through catch-alls. Its algorithm tracks successful matching, nondiverging failure and divergence separately; an inaccessible right-hand side can still affect lazy evaluation. Conservative constraint reasoning permits residual false warnings. The historical implementation’s weak term oracle and type-only enclosing constraints limit the richer formal framework.

The selected twelve-program corpus reports missing-case warnings falling from51 to24 relative to the old GADT workaround, with38 new redundancy reports. That is useful diagnostic evidence under a problem-enriched selection, not measured developer time, avoided behavioral defects or a Nu/agent effect. Four pinned files corroborate catch-all examples and identify one corpus member as a tutorial. Exact historical compiler/package binding remains unresolved. S114’s now-reconstructed method proves selected partial matches safe for sufficient inputs and reports concrete crash fixes. Its finite constraints, conservative laziness handling and preparation edits limit applicability. Selected S133 passages expose a normal-form theorem premise and an unproved bounded-tested lemma; the later repository does not certify behavior-preserving versions. S119’s compositional successor is now fully read in its later author edition. Its selected stress improvements, adverse case, trusted completeness declarations and conditional proof do not establish unconditional implementation safety. S134 resolves the oracle premise and scoping correction; S135 now supplies concrete implementation checks, with real defects/fixes, no GHC discoveries, conditional oracles and report/data limits. S136 now adds automatically inferred constructor refinements and a bounded-interface complexity argument, preserving the omitted generated module, conservative warnings and unresolved exact timing-artifact correspondence. Baseline exhaustiveness, warning opportunity after change, branch removability, sufficient inputs and correct behavior remain separate.

## What the temporal-oracle evidence requires

This is a literature synthesis for comparing approaches, not an implemented evaluator or permission to build one. It carries useful capabilities forward along with their limits.

| Decision | Source-grounded capability and condition | Consequence for interpreting an evaluation |
| --- | --- | --- |
| What is observed? | S46/S47/S53 express event/signal properties; S104 includes environment, resets and timing in the observation domain. | State the trigger, event order, clock, observed outputs and allowed alternatives. A final-state check need not see transient failures. |
| What does a finite run establish? | S47/S50/S53 supply explicit finite/partial-trace interpretations; S100 separates safety from progress/fairness. | Distinguish a witnessed violation, a bounded obligation satisfied within its stated horizon, and insufficient observation. An arbitrary timeout cannot redefine unbounded liveness. |
| Which trace population supports the claim? | S123 supplies recorded-trace matching, post-solution checking and an outlined automata/model route; its dated analyzer has configurable search limits and first-solution policy. | Name observation projection, initial-state treatment, search policy and model correspondence. A property of found winning traces does not certify every path, and a finite trace cannot establish an infinite-repeat match. |
| How can an industrial test survive routine changes? | [S294](full-reading/S294-industrial-game-regression-testing.md) uses named UI objects, shared test components and event-driven recovery around real game instances. | Host instrumentation and authored conditions remain required. Estimated command delays, counter resets and optional recovery do not themselves establish post-trigger behavior, an absence horizon or restored game state. Preserve its useful reported deployment without importing a net-cost estimate. |
| Was the obligation exercised? | Temporal implications can hold without their antecedent; the reviewed methods' generation/monitor semantics do not establish application-level trigger coverage automatically. | Track trigger/reachability evidence. A program violating required reachability is a failure; an evaluator that never observes the needed case has a coverage gap. |
| What survives a checkpoint or edit? | S100 checks futures from the reached state; S101 supplies distinct replay and retained-state policies; S104 explains revised versus retained oracle judgments. | Preserve outstanding obligations through adequate monitor history/state, and replace superseded expectations while retaining applicable ones. Current values and replay compatibility are not the complete intended contract. |
| Which effects can be replayed? | S46/S47/S48/S53 bound sampling, asynchronous inputs and external reset; S65 demonstrates useful ECS state inspection with transient-event limits. | Define the environment/effect boundary and reset fidelity. Replay equality within recorded state does not show that irreversible external actions were undone. |
| Why trust the verdict? | S104 separates oracle sources and labels; S100's shared semantics make an additional independent interpretation consequential. S124 records flawed contracts, a design-conforming pathfinder that missed intended behavior, and an unenforced synchronization boundary. S125 supplies positive mutant-guided criterion repair and temporal/scenario ablations, with unreleased calibration and finite-observation limits. | Check intended behavior, abstraction mapping, positive/negative/vacuity witnesses and plausible faults; count construction and judgment effort. A typed wrong branch and a valid fallback must be distinguishable by behavior. |

These controls also explain the supervisory D1 amendment: **diagnostic sites and behavioral obligations are separate maps**, often many-to-many. Both initial source variants can cover all inputs. The literature motivates checking later behavior and total work; it does not validate source equivalence or a future experimental oracle. A well-measured adverse convention result would be useful evidence, while an unread method remains a survey gap.

## Three-criterion status and next work

**Unique:** unconfirmed; newly surfaced predecessors require examination. **Valuable:** plausible beneficiary decisions remain concrete, but effect, prevalence and net cost are unmeasured. **Scientifically valid:** the existing candidate designs retain unvalidated equivalence, oracle, task-diversity and accounting assumptions; this expanded review is not an experiment or validation.

Continue the source-specific priorities in the reconciled coverage map. Completed S108/S104, type/coverage, game/runtime and empirical-method dependencies no longer appear as unread next steps. The remaining game-adaptation, comparative-maintenance and agent-evaluation routes address distinct uncertainties. Further searching follows the claim it can change, not an expectation that a positive Nu effect must eventually appear. This is continued literature work, with all experimental holds in PLAN preserved.

## Refined safety and analysis costs: S136

[S136](full-reading/S136-intensional-datatype-refinement.md) establishes a useful intermediate claim: partial functions can be safe for a program whose callers respect inferred constructor subsets. It builds those subsets automatically from declared datatypes and carries conditional summaries across functions/modules. This supports a concrete prior mechanism beyond local coverage, while constructor erasure cannot express arbitrary invariants such as finite non-empty lists. Neither its inference theorem nor local exhaustive syntax specifies the behavior required after a new case is added.

The printed performance evidence is positive within scope: ten retained package sets have short reported analysis times, and334 appendix rows reproduce every structural aggregate. The generated Data.Sequence module is excluded after failing to finish promptly; unsupported language/dependency features cause conservative warnings, with no true bugs identified in this sample. The complexity theorem is linear only with type/slice/nesting and function sizes bounded. The public August source uses a CPU-time formatter with an inconsistent unit label; correspondence to the later5.211 GB evaluation VM is unresolved, so the paper's timings remain reported values. No runtime or maintenance effect has been reproduced.

**Discovery:** G09 and SC55–57 provide a sparse incoming neighborhood, four backward metadata lookups and an exhausted exact-title phrase, not field coverage. **Primary understanding:** S136 publisher and v3 appendices are read; the exact VM/raw measurements remain available but unacquired. **Evidence disposition:** established restricted mechanism, conditional positive analysis results, explicit adverse/precision/version limits; Nu/agent transfer unmeasured. **Next action:** acquired S115/S118 extension rules and S116 practice, with refinement alternatives and the wider Join Token/persistence/oracle frontiers retained. No theme is closed.

## Extending constructors and operations: S115

[S115](full-reading/S115-open-data-functions.md) provides a concrete positive mechanism: definitions in separate modules contribute constructors and function cases, and best-fit dispatch lets a new specific case outrank an old default. Recursive calls use the final assembled function. Global meaning, duplicate-pattern rejection and import-derived constructor ordering are integration obligations; ordinary typing does not rule out incomplete matching or specify a new case's behavior. The proposed separate-compilation translation still requires additional compiler-interface support, and exhaustiveness is checked globally. No effort or performance result was measured.

**Discovery:** all 49 DOI records in G10's incoming set were retrieved at effective offsets 0/20/40; the set contains edition notices and four open-data/open-science entries. This does not certify the field or actual citation context for every edge. **Primary understanding:** all S115 pages/figures are read; EML and selectable datatype composition have metadata/citation coverage only. **Evidence disposition:** established extensibility semantics and explicit design costs, unmeasured practical benefit. **Next action:** resolve selectable component composition, then acquired S118 pattern views and S116 extension practice; keep EML's modular-checking question and the wider background frontiers open.

## Selectable composition and effect descriptions: S137

[S137](full-reading/S137-data-types-a-la-carte.md) resolves a consequential S115 contrast. Explicit signature sums select which constructors belong to a particular datatype; component algebras support reused operations. Smart constructors hide injection syntax, but annotations, overlapping instances and a right-spine search restriction remain. The free-monad extension permits modular effect descriptions with separate interpreters. Operation-category types do not specify exact behavior, complete external effects or serializable continuations.

**Discovery:** the initial 200-edge graph was truncated, so G12 expanded the cap and returned 287 edges without truncation. The [composition screen](nu-background-composition-screen-2026-10-01.md) distinguishes title-only records, eight targeted metadata lookups, selective snippets, editions and eleven unchanged S115 decisions. **Primary understanding:** all S137 pages are read; S138/S139 practical/cost methods are acquired but unread. **Evidence disposition:** established reuse and effect-description mechanisms, explicit integration costs, no original measured benefit. **Next action:** inspect S138/S139's actual runtime/representation comparisons, then S118 views and S116 practice. This follows a material cost question, not every neighboring theory paper. EML, Join Token, persistence and other B01–B12 frontiers remain open.

## Composition performance without assuming zero cost: S139

[S139](full-reading/S139-composition-representation-cost.md) reports a useful positive result: generating one flat signature for a selected sum removes the growing composition-depth cost in its expression evaluator. Original polymorphic component code can be reused through generated injections and algebra instances. In the displayed normalized comparison, however, the generated version remains roughly 1.3–1.5× the plain datatype over much of the range. Balanced composition is slower again. Preserve both the improvement and the residual overhead; the abstract's broad equal-efficiency wording is stronger than the graph warrants.

**Discovery:** G13 is sparse and explicitly low coverage; a keyword fallback returns five records against a reported total of eight, then zero at effective offset five. The discrepancy remains visible. **Primary understanding:** all five pages/nine figures are read, with a bounded standard-API check; exact benchmark source/data are unlocated after primary-page and targeted public searches. **Evidence disposition:** positive reported runtime trend under one synthetic fixed-height workload, unresolved uncertainty/version/forcing details and no maintenance or compilation measurement. **Next action:** S138's practical/fusion comparison, then S118/S116; retain the 2014 composition implementation and worker/wrapper foundation as conditional dependencies. No theme closes, and all experimental holds remain.

## Composition benefits after a published benchmark correction: S138

[S138](full-reading/S138-compositional-data-types.md) supplies useful phase-specific syntax, annotation propagation and generic transformations. Its largest reported performance advantage is invalid: the author identifies a deep-evaluation generator bug in 2013 and releases corrected results. Those later measurements show desugaring slower than ordinary recursive datatypes, alongside substantial improvements from fusion within the compositional implementation. The corrected data are now in Zotero; all 88 stored ratios were checked. They do not estimate maintenance effort or isolate a Nu mechanism.

**Discovery:** G14's 38 incoming titles include 35 already screened sources and three new titles; SC69/70 return one exact S138 record and zero exact S140 records. The repository correction is consequential evidence absent from the returned Scite metadata. **Primary understanding:** all twelve article pages and selected source are examined; the corrected workbook is reconstructed, while the older ODS variants do not recover the precise published table. **Evidence disposition:** preserve generic reuse and favorable fusion, exclude the invalid original desugaring advantage, and retain corrected baseline overhead. Symbolic duplication/deletion examples narrow the stated monadic fusion premise; exact Fokkinga hypotheses remain an unread dependency. **Next action:** follow S140’s lawful author copy while continuing S118/S116 and the other background themes. No experimental work or new workers are authorized.

## Pattern abstraction after S118

[S118](full-reading/S118-active-patterns.md) supplies a concrete way to evolve representation behind a public pattern interface. Its declared case family can be covered while its recognizer still raises an exception or maps a new case incorrectly. Stable views therefore relocate integration work; they do not eliminate behavioral obligations. The historical compiler’s effect assumptions and the non-equivalent reflection appendix further limit claims from the examples.

**Discovery:** G15 covers 53 incoming titles, with selected contexts and 47 new dispositions; SC71/72 and primary foundation routes have explicit bounded returns. C02’s unexamined abstracts/pages remain separate gaps. **Primary understanding:** all twelve pages, figures/table and appendix are reconstructed; historical compiler source and later follow-up methods are not. **Evidence disposition:** established abstraction/composition mechanism, unmeasured maintenance benefit, and distinct proposed-versus-implemented semantics. **Next action:** S116’s practice study can establish what its observed extensions actually represent; joins/Joinads remain conditional coordination methods alongside acquired S121/S122. This closes a method dependency without closing B02 or the whole survey.

## Extension practice after S116 and the S141 comparison

[S116](full-reading/S116-extension-practice.md) supplies a practical reason to support both extension directions: neither is rare in its selected Smalltalk histories, and open-class additions coexist with substantial conventional subclassing. The favorable stability observations also matter. The study’s method counts, change entropy and extension frequency do not establish net maintenance effort, intended behavior or a Nu/agent effect.

**Discovery:** the complete bibliography, G16’s fourteen edges and exact DOI lookups are accounted, with conditional work-fragmentation, type-predicate and contrary Visitor leads. C02’s unexamined continuation remains a separate frontier. **Primary understanding:** all 38 pages/21 figures are reconstructed; the final issue has bounded text/visual correspondence and S141 a nine-page comparison. Advertised CSV/R data are unacquired after the resolved route returns 404. **Evidence disposition:** concrete ecosystem prevalence and scoped favorable stability; no causal language/tool benefit; selection, counting-unit and reporting conflicts qualify exact estimates. **Next action:** move back to the acquired S121/S122 coordination methods and selected persistent-structure/runtime methods. The empirical residual does not require an endless search for a positive effect; missing primary coverage elsewhere still requires work. All experimental holds remain.

## Join-token alternatives after S121/S122

The mechanism-to-benefit chain is now explicit: named object participation and ordered joins relocate candidate selection; programmers maintain token roles, ignition order, guards and disposal; small game demonstrations and a 357/436 physical-line comparison support expressiveness and scoped size observations; different host support and game behavior prevent a net maintenance or runtime transfer claim.

**Discovery:** the complete two bibliographies, G17 and targeted web/author follow-up expose a related JEScala method and an earlier 2006 publication, with sparse graph coverage explicitly insufficient. **Primary understanding:** S121's seven pages and S122's twenty-page chapter are complete; selected dated runtime and game sources clarify snapshot, cleanup and comparison boundaries. **Evidence disposition:** constructive positive capabilities and bounded author experience; no controlled maintenance effect, general latency bound or verified lifecycle property. **Next action:** resume C11 functional-persistence/runtime primary methods to balance cost coverage; retain acquired S142 for its event/join comparison and C02's unexamined continuation. No theme or experimental hold is closed.

## Persistent-collection benefits and measurement context: S143/S146

[S143](full-reading/S143-champ-immutable-collections.md) supplies concrete positive cost evidence within immutable JVM collections. Cached-data arithmetic reproduces its large iteration/equality and selected dominator-analysis gains, as well as slower lookup/update cases. Equalizing collection-hash policy reduces application gains substantially while preserving a scoped advantage. Single-root structure overhead, repeated updates from a fixed root and nominal graph counts are distinct from retained histories, peak allocation and interactive latency. Pinned source exposes version/accounting questions without constituting executed defect confirmation.

[S146](full-reading/S146-jvm-benchmark-context.md) provides a constructive counterexample to assuming isolated throughput rankings transfer: diverse prior inputs reverse a hash optimization’s aggregate ranking. Its stream and standard-class-clone cases show further profile sensitivity. It does not rerun CHAMP, whose principal comparators are Scala/Clojure immutable collections. The [partial S147 check](full-reading/S147-benchmark-practices-partial.md) likewise does not refute CHAMP timings: the authors excluded that artifact from impact testing, and released static counts substantially include JMH’s own examples/internal benchmarks.

**Discovery:** G18, SC77–81 and the [runtime screen](nu-background-runtime-screen-2026-10-01.md) account returned identities, editions, metadata/selected contexts and open continuations. **Primary understanding:** S143/S146 complete, S147 partial with access limits, S144/S145 now complete below; S148 acquired/body-unread. **Evidence disposition:** measured representation gains and adverse cases, demonstrated context sensitivity, unmeasured history/latency/Nu transfer. **Next action:** read the collector and reuse methods before treating those unresolved empirical outcomes as literature-completion blockers. Retention/trace-method leads and the other B01–B12 frontiers remain. All experimental holds remain.

## Runtime latency after S144

[S144](full-reading/S144-alligator-collector.md) connects runtime mechanism to measured outcomes: retain moving nursery allocation, collect old objects concurrently, pay barriers/synchronization/fragmentation costs, and obtain substantially shorter major pauses in selected GHC workloads. The favorable HTTP tail and15-second game account coexist with longer minor pauses, increased CPU and some slower executions. Runtime choice is therefore a concrete explanatory dimension beside source-state convention. No universal pause bound or Nu/.NET maintenance benefit follows.

**Discovery:** G19's five incoming edges, SC82/83's exact identity sets, the full bibliography and the pinned author repository are accounted in the runtime screen; broader C11/.NET/game continuation remains open. **Primary understanding:** all thirteen paper pages/figures/tables are complete; ten source/config/doc files,33 notebook cells and eleven of31 design pages are reconstructed. **Evidence disposition:** scoped major-pause/response benefits and adverse costs; proposal-level finalization/retention differences; unresolved raw-data/launcher and published-versus-saved-output correspondence. **Next action:** S145 now distinguishes reference-counted reuse from tracing collection below; continue S148 and reconcile consequential retention/workload and other theme frontiers. Unmeasured transfer remains an empirical question; it does not erase demonstrated benefits or complete the background survey.

## Reuse, borrowing and history retention after S145

[S145](full-reading/S145-counting-immutable-beans.md) adds a positive mechanism-to-outcome chain: source transformations expose uniquely owned cells, reset/reuse recycles their allocations, borrow inference reduces counter work, and selected compiler ablations show substantial throughput gains. Retained map roots reduce those gains and increase runtime; the fully retained case still benefits from some reuse. Acyclic values, lifetime ownership, tail calls, representation size and thread-sharing transitions are integration assumptions. This is broader evidence than an unconditional claim that functional updates allocate or cost more.

**Discovery:** G20 supplies22 incoming edges, SC84 six exact metadata records and W161/162 primary edition/artifact routes; all titles/supplied passages are accounted. One parkour DOI with unrelated formalization text is rejected as an unreliable identity. C11 and .NET/game continuation remain open. **Primary understanding:** all twelve S145 pages/seven figures, thirteen complete files and selected configuration are reconstructed; raw trial data are not present in the pinned tree. S148's forty-page extended report is acquired but unread. **Evidence disposition:** scoped compiler-ablation and retained-history benefits/costs; unfinished compiler proof, asymmetric GC accounting and bundled cross-language comparisons. **Next action:** reconstruct Perceus's precise-reclamation/proof assumptions, then reconcile consequential retention/latency and other thematic frontiers. Nu maintenance benefit remains an empirical residual, not a reason to discard these positive results or declare coverage complete.


## What precise reclamation adds to the runtime account

[S148 Perceus](full-reading/S148-perceus-precise-reclamation.md) now reconstructs the full forty-page extended edition, selected published correspondence and eleven pinned files. Functional source can support physical in-place updates when ownership, shape and compiler conditions hold. Its core theorem concerns reachability after reference-count operations in an acyclic calculus; it does not cover every subsequent optimization or imply minimal RSS. The paper itself reports a case where reuse retains storage longer. Favorable timings remain meaningful within the selected implementations, alongside shared-workload dependence, adverse cases and unequal C++ persistence/reclamation obligations.

The named source release uses 4.2 million insertions where both paper editions say 42 million, and a trimmed mean where the paper reports ten-run medians. These are unresolved source/result correspondences, not reproduced failures. The two paper editions and S145-derived workloads are not independent replications. S149 has now resolved the immediate frame-limited reuse dependency below; S150 now supplies the fully reconstructed imperative capture/restore rival below. This advances B04/B06 understanding without declaring either theme surveyed. Nu transfer and net maintenance value remain empirical residuals; C11, .NET/game discovery and the other theme frontiers remain coverage work.

## B04/B06 refinement — bounded reuse, 2026-10-01

**Discovery:** S149 follows G21/SC85's already identified direct method dependency; W166/W167 resolve the extended edition and named sources. The existing citation neighborhood and conditional static-allocation leads are retained without another unchanged graph screen. **Primary understanding:** [all24 published pages](full-reading/S149-frame-limited-reuse.md), eight figures, ten selected extended pages and fourteen source/configuration files are reconstructed; other proof dependencies and exact run binding remain unresolved. **Evidence disposition:** drop-guided reuse has an evaluation-depth-dependent extra-heap bound, with concrete tree gains and null/adverse results elsewhere. The old comparator also changes borrowing. No constant total-memory, frame-latency or Nu benefit follows. **Next action:** S150's acquired imperative capture/restore method can change the alternatives and cost synthesis. Broader runtime/discovery and other thematic gaps remain; unmeasured Nu benefit is an empirical residual, not by itself a reason to prolong this proof branch.

## B04/B06/B07 refinement — imperative capture and restore, 2026-10-01

**Discovery:** W168 recovers the pinned Store/proof artifacts, and W169 screens eighteen web records for later work. Scite G22 failed at the monthly quota; no citation-coverage conclusion follows. **Primary understanding:** [S150](full-reading/S150-snapshottable-stores.md) is fully read in its 39-page extended edition, including seven figures and all 114 detailed table rows; eleven source files and selected mechanized-core definitions/specifications are inspected. **Evidence disposition:** explicit capture points enable cheap repeated writes, with observed type-checking gains and copying-favorable cases. Restore distance, recording/retention, invalidation and complete mutation capture remain integration obligations. The persistent core proof and finite transaction tests do not certify external effects or the whole compiled library. **Next action:** S151's acquired 17-page custom-type successor addresses the original reference-only boundary. Then return to S97/S98 and B01/B10's weaker design/practice coverage rather than following every runtime citation automatically. C11/.NET/game transfer and citation follow-up remain open; Nu benefit is an empirical residual.

## B04/B06/B10 refinement — custom snapshot integration, 2026-10-01

**Discovery:** W170 pins the named prototype; W171 screens thirteen returned title/context records, mostly alternate routes and unrelated meanings of “storable.” Four cited solver files supply a bounded practice check; citation coverage is not exhausted. **Primary understanding:** [S151](full-reading/S151-custom-storable-types.md) is fully read, with eleven full source files and three partial ones. **Evidence disposition:** custom operations can restore logical contents while retaining capacity or internal optimizations, reducing the need to rebuild every field around stored references. The cost moves to undo/redo/trail contracts, generic dispatch and retained history; no new benchmark or generalized proof is supplied. The prototype's exported API and active fuzzer are narrower than the paper's design. The cited Z3 source has generic undo extensibility, so a broad absence claim is rejected. **Next action:** the immediate reference-only dependency is resolved; return to S97/S98's human design/maintenance evidence. Solver-wide review, later release status, C11/.NET/game transfer and citation follow-up remain distinct conditional or unsurveyed paths. Nu benefit remains an empirical residual.

## B01/B10 refinement — structural choices versus observed benefit, 2026-10-01

**Discovery:** W172–W174 screen 42 returned occurrences (40 distinct URLs) for S97's thesis and related routes; W175 and ordinary public HTTP reach the author's site but recover no dissertation. **Primary understanding:** [S97](full-reading/S97-encapsulation-guidelines.md) is fully read, including all page images and printed counts. The selected fuller S152 account remains unavailable, with unresolved edition date. **Evidence disposition:** the 27-person, three-program study reports inconclusive immediate timing and substantial differences in author-classified structural shortcuts. Those shortcuts can be behaviorally correct; five boundary opportunities include one adverse cell and dependent repeated observations. Only one maintenance round per program was observed, leaving subsequent cost a prediction. **Next action:** read S98's accessible distributed-language study, preserving S90's favorable but blocked result and S152's specific allocation/outcome/data gaps. These are coverage limits distinct from unmeasured Nu transfer.

## B01/B10/B12 refinement — useful isolation, mixed total costs, 2026-10-01

**Discovery:** W176/W177/W179 examine 46 search occurrences / 45 distinct URLs; W178/W180 and ordinary primary HTTPS resolve NASA and DNB acquisition routes. **Primary understanding:** [S98](full-reading/S98-language-structure-maintenance.md) is fully read, all eleven pages and seven tables visually checked. S153 has two contents pages only; S154’s earlier metric-method account is acquired for continued reading. **Evidence disposition:** LADY reduces isolation effort and changed-module counts on selected systems, while correction effort has no significant advantage and overall rework is higher. The language/support bundle, six-person allocation and missing inferential detail limit attribution. Best within-study rank correlations do not establish prospective effort prediction. **Next action:** reconstruct S154’s actual metric method, then S96’s professional maintenance comparison; preserve the blocked S90/S152/S153 paths and unmeasured Nu transfer as different kinds of gaps.

Scite’s stated UTC reset has occurred: S150, S151 and S97 decisions were submitted and their reports inspected, with zero skips/missing reasons or unlinked/truncation flags. G22 now returns a small incoming graph; its seven links do not establish field completeness. The [runtime screen](nu-background-runtime-screen-2026-10-01.md) records exact editions, conditional leads and audit units. No theme is declared surveyed and no experimental hold changes.

## B01/B11/B12 refinement — measured structure and prediction time, 2026-10-01

**Discovery:** S98 reference 23 and W177/W178 already locate the primary NASA report; no new search is counted. **Primary understanding:** [S154](full-reading/S154-design-metrics-maintenance.md) now covers the complete paper and presentation. Its six C-TIP systems are related to S98’s project, with exact data/participant correspondence unresolved. **Evidence disposition:** useful within-system rank associations distinguish ripple work from internal modification. Structural measurements come from the final development design, and no satisfactory linear effort model or held-out prediction is reported. Formal documentation and implicit-dependency analysis impose measurement obligations. **Next action:** S96’s acquired industrial comparison can address professional work and lifecycle tradeoffs. S153’s specific data/validation sections remain inaccessible; missing Nu benefit is a separate empirical residual. No theme closes and no experiment is authorized.

## B01/B06/B10/B11/B12 refinement — professional maintenance and lifecycle tradeoffs, 2026-10-01

**Discovery:** G23 returns eleven incoming edges/twelve nodes; SC87 resolves ten of eleven requested DOIs. W182/W184 inspect 35 search occurrences/34 URLs and W183 checks four primary routes. Incomplete abstracts, related editions and conditional leads remain explicit. **Primary understanding:** [S96](full-reading/S96-industrial-credit-maintenance.md) now covers all eight journal pages and four tables, with every page visually checked. **Evidence disposition:** one professional OO team spends substantially less technical effort than the legacy team on one integration change, despite greater requirements effort, more changed code/files and adverse runtime/resource cost. Documentation, testing, team and organization are bundled; future payback is unmeasured. **Next action:** S94’s existing 47-page journal can resolve the changeability pilot/main and later-replication lineage. S95’s cost model and prior Briand/Bunse design-document/guideline leads remain consequential. Nu-specific benefit is a separate empirical residual; no theme closes and no experiment is authorized.

## B01/B10/B11/B12 refinement — original coffee-study method and favorable rivals, 2026-10-01

**Discovery:** the original S94 journal/appendices are now complete; W185–W191 examine positive guideline/document evidence previously screened in SC13. **Primary understanding:** [S94](full-reading/S94-changeability-design-alternatives.md) separates its pilot, randomized 17/19-person main assignment, ordered paper tasks, endpoint-specific missingness and selected structural measures. S81/S88 lineage is resolved at the original publication level. **Evidence disposition:** distributed design takes longer to understand here, while selected correct solutions have smaller later change sizes. Graded correctness, manual example checks and task completion are distinct, and the structural five-case eligibility rule cannot be reconstructed from the observed RD grades. These limitations do not erase either observed direction or establish a lifetime effect. **Next action:** the acquired S155 report supplies accessible favorable guideline methods; S156's document comparison and report/journal/conference relationships remain acquisition/method gaps. Nu benefit and transfer are empirical residuals. No theme closes or experiment starts.

## B01/B05/B10/B11/B12 refinement — favorable guidelines and the practice frontier, 2026-10-01

**Discovery:** [G24 and its targeted follow-up](nu-background-design-practice-screen-2026-10-01.md) account for 181 incoming DOI sources, 57 web search occurrences and fourteen resolved metadata records, with old decisions reused and four graph identity gaps explicit. **Primary understanding:** [S155’s complete May 1999 report](full-reading/S155-quality-guidelines-design-documents.md) reconstructs seven understanding questions, two impact tasks, counterbalanced order, phase-time missingness and positive accuracy/completeness/rate. **Evidence disposition:** these are document-task benefits under a time allowance, with domain/guideline confounding and no implementation or net QA-cost outcome. Aggregate and final-edition discrepancies remain unresolved. **Next action:** S157’s acquired game-engine recovery study and S158’s acquired practitioner survey directly address weaker game/practice coverage. S156’s full methods and S155’s package/journal remain access gaps, while Nu transfer and lifetime benefit are empirical residuals. No theme closes or experiment begins.

## B01/B05/B07/B10/B11/B12 refinement — recovery support and observation cost, 2026-10-01

**Discovery:** G25’s seven incoming edges, fourteen exact Scite records and W200–W207 primary routes distinguish recovered architecture, engine-quality proxies, build access and selective instrumentation. **Primary understanding:** [S157](full-reading/S157-sydra-game-engine-understanding.md) is complete in arXiv v2, with nineteen package files and descriptive arithmetic; journal methods/results have targeted extraction only. **Evidence disposition:** subsystem/include recovery is a concrete support mechanism with substantial manual preparation. Favorable understanding/precision directions coexist with greater impact time, score inconsistencies and unverified significance. No implemented change, net benefit or Nu transfer is observed. **Next action:** S158’s acquired practitioner survey and S159’s acquired industrial instrumentation method address practice and observation cost; original representation/engine-build methods remain conditional. Reporting gaps require correction/materials, while unmeasured Nu effects remain empirical residuals. All experimental holds remain.

## B01/B07/B10/B11/B12 refinement — practitioner judgment and observed benefit, 2026-10-01

**Discovery:** G26 screens 24 incoming edges/25 nodes; SC92–93 resolve seventeen exact records, with primary institutional follow-up in W208–W212. **Primary understanding:** [S158](full-reading/S158-practitioner-design-quality.md) is complete in its 45-page online-first edition, including the questionnaire; its raw data files are blocked. **Evidence disposition:** respondents value experience, review and qualified design rules, while describing overuse, essential complexity and time pressure. This is useful reported practice under convenience/snowball sampling, not observed maintenance benefit, calibrated expertise or population prevalence. The authors themselves distinguish indicators from validated effects. **Next action:** S159’s acquired game-engine instrumentation, S160’s belief/evidence comparison, S161’s metric/judgment study and S162’s extended industry hot-fixing method address distinct observation and practice gaps. S162 shares predecessor survey data. Material access/edition gaps remain separate from empirical residuals; no theme closes or experiment starts.

## B05/B07/B10/B11/B12 refinement — observing an interactive system has costs, 2026-10-01

**Discovery:** S159’s empty/low-coverage G27 is supplemented by SC94’s five exact records and versioned compiler/primary coverage routes in W213–W217. **Primary understanding:** [S159](full-reading/S159-selective-game-instrumentation.md) is complete in v1; private source/data/absolute timings remain unavailable. **Evidence disposition:** selected commit instrumentation preserves substantially more average FPS than full instrumentation in the chosen workload and avoids the reported full-FE failures in two fixed industrial suites. Full IR also passes, with coarser information. Extraction latency is separate from CPU compilation cost; the 2,000-commit estimate is extrapolated, and plotted observations defeat universal headline FPS bounds. Changed-function coverage neither establishes fault sensitivity nor covers every relevant path or failed capture. **Next action:** S164’s acquired industrial coverage method and S163’s access-limited game-metric taxonomy address actual use and coverage validity, alongside the retained practice/oracle methods. These are material reading/access gaps, while Nu benefit remains an empirical residual. No theme closes or experiment starts.

## B07/B10/B11/B12 refinement — operational adoption and behavioral adequacy, 2026-10-01

**Discovery:** [G28 and its follow-up](nu-background-coverage-practice-screen-2026-10-01.md) account for 107 incoming DOI entries, 24 exact Scite returns and 37 web search occurrences. Edition aliases, a missing-title source and an implausible 2017-to-2019 citation with an unrelated abstract remain explicit. **Primary understanding:** [S164](full-reading/S164-google-coverage-practice.md) is complete, including all figures/tables and the survey instrument. **Evidence disposition:** automatic coverage integration is a concrete prior workflow with substantial adoption and perceived usefulness. It incurs maintenance and observation costs; successful computation, increasing aggregate coverage and self-reported usefulness do not measure defect reduction, faster reviews or net budget benefit. The authors explicitly leave those effects open. **Next action:** acquired S165 reconciles test-size/adequacy comparisons; S166 tests mutant/real-fault validity; S167 challenges universal instrumentation-harm claims with mixed Java evidence. The 2026 causal study is a registered plan without an effect estimate. Those are primary-method gaps, distinct from unmeasured Nu effects; S163’s access gap and S160–S162’s practice methods remain. No theme closes or experiment starts.

## B07/B11/B12 refinement — selection goals, cost measures and adjustment assumptions, 2026-10-01

**Discovery:** [G29/SC98–99/W222–W228](nu-background-adequacy-method-screen-2026-10-01.md) account for 61 citer titles, 29 snippets, ten exact metadata returns and 89 web search occurrences. A direct later size-adjustment claim is retained, with its inaccessible body distinct from the newer registered report. **Primary understanding:** [S165](full-reading/S165-adequacy-size-methodology.md) is complete in its thirteen-page author edition. **Evidence disposition:** its simulations favor goal-directed over random selection, coverage early and coverage-then-mutation later. Equal method counts do not mean equal time/cost. Normality is required for the plotted correlation ceiling; zero-filled undefined correlations and observational conditioning cannot establish a universal causal rule. Section 7 explicitly allows several causal explanations. **Next action:** S166/S170 reconstruct the original favorable/critical real-fault accounts, S169 supplies an acquired earlier evaluation framework, and S168 remains a material access gap. S167 and the practice/type/runtime frontiers remain independently actionable. Missing Nu effects are empirical residuals; missing methods and edition binding are coverage deficits. No theme closes or experiment starts.

## B07/B10/B12 refinement — instrumentation effects and report identity, 2026-10-01

**Discovery:** G30/SC100–102/W229–W230 account for seven incoming entries, eleven exact Scite returns and sixteen web search occurrences, with primary selected abstracts/appendices and edition aliases retained. **Primary understanding:** [S167](full-reading/S167-instrumentation-flakiness.md) is complete in its five-page v1; the [pinned release check](full-reading/S167-instrumentation-artifact-check.md) inventories all 1,080 names and inspects selected fields in 47 ZIPs before HTTP 429 stopped downloads. **Evidence disposition:** instrumentation's observed directions vary by Java project/tool. This preserves contrary evidence to a universal harm claim alongside concrete interference examples. Within-configuration variability, deterministic resource conflict, source/bytecode mapping, missingness and causal attribution are distinct. Raw Exhibitor averages agree with the paper, but duplicate reports/conflicting outcomes and a .100 formula bound versus printed .200 remain unresolved. These issues do not invalidate every observation or establish harmlessness. **Next action:** acquired S171/S172 can resolve mapping and industrial diagnostic value; S166/S170/S169 address the remaining adequacy-method dependencies. S168 remains access-limited and the practice/type/runtime frontier continues. Nu effect sizes remain empirical residuals, while unread methods and incomplete editions remain coverage gaps. No theme or experimental hold changes.

## B04/B07/B12 refinement — mutation sensitivity is conditional evidence, 2026-10-01

**Discovery:** the [mutation-validity screen](nu-background-mutation-validity-screen-2026-10-01.md) records sixty ranked title/available-abstract records, a failed contrasting-label query followed by content discovery, and focused primary follow-up. Offset 60 onward remains unexamined; application-heavy results were reformulated around concrete method gaps. **Primary understanding:** [S166](full-reading/S166-mutants-real-faults.md) is complete in its twelve-page author edition. **Evidence disposition:** 153/258 developer trigger pairs improve mutation score without increasing statement coverage, a positive additional-sensitivity result. Known fix locations, selected reproducible/isolated faults, stability filtering and changed pairwise score denominators delimit transfer. The paper explicitly does not calculate one global coverage-independent correlation, and preserving mutation score can still lose real-fault detection. Its operator-specific difficult cases do not prove that all future mutants fail to represent them. **Next action:** S170 and S169 remain acquired original/comparison-framework dependencies; S173 reopens later coupling but is access-limited, while S174/S175 are acquired weighting/change-relevance methods. Source location alone is not a complete behavioral-obligation boundary. Broader practice/type/runtime and temporal-oracle continuations remain, separately from unmeasured Nu benefits. No experimental authority changes.

## B07/B12 refinement — weak correlation does not erase selection value, 2026-10-01

**Discovery:** W236–W238 and SC109 follow the original method, earlier bibliography and a new contrary replication; four bounded original-title/artifact queries did not locate S170’s original analysis release. The found 2026 package belongs to S176. **Primary understanding:** [S170](full-reading/S170-mutant-correlation.md) is complete in its twelve-page institutional edition. **Evidence disposition:** correlations weaken after fixing suite size under its random-pool sampling, yet top-ranked suites have positive real-fault detection gains. The reported averages sit within a selected-significant-case discussion, the high-score subset overlaps its all-suite comparator, and exact analysis implementation remains unresolved. S166/S165/S170 use different populations and selection processes; favorable trigger sensitivity, weak correlation and useful score-guided selection can coexist. Equal counts do not establish equal cost. **Next action:** S176 is now acquired as arXiv v1 after native record creation, with abstract/history/opening-only coverage. Its claimed clean-versus-buggy-input difference and lack of dominant size confounding challenge transfer to LLM tests and require full methods. S169/S174/S175 and the practice/type/runtime frontier remain consequential. An incomplete coverage route is not relabeled an unanswerable empirical question; none of these results validates Nu or closes a theme.

## B07/B12 refinement — positive model comparisons need their actual selection rule, 2026-10-01

**Discovery:** SC110 and W239–W242 trace the original coverage comparison, incorrect-code intervention, documentation-oracle alternative and released S176 package; wider query/citer continuations remain open. **Primary understanding:** [S176](full-reading/S176-llm-proxy-replication.md) is complete in its twenty-four-page v1; the [artifact check](full-reading/S176-proxy-artifact-check.md) separately inspects pinned source and 105 CSVs. **Evidence disposition:** fixed-input model-level branch and raw-mutation associations reproduce at .861/.863 using the supplied count target. They are useful positive evidence under this workflow. Detection per each model’s retained population asks another question and yields .650/.694; neither is automatically the corrected estimand. Many suites in nominal fixed-size data contain fewer than k tests, and some flagged-compiled rows contain zero tests. The study cannot establish exact size independence using those filters. Thirteen configurations share families/tasks; 318 method rows share 233 bug IDs. The buggy-input arm measures coverage, not mutation. **Next action:** reconstruct acquired S177/S178/S179 for direct input, positive documentation and original coverage methods, alongside S169 and the weaker practice/type/runtime frontier. These are specific understanding gaps, separate from unmeasured Nu effects. No theme or experimental hold changes.

## B01/B10/B12 refinement — belief, experience and a measured outcome, 2026-10-01

**Discovery:** [G31 and its selective follow-up](nu-background-belief-practice-screen-2026-10-01.md) account for 154 incoming titles, seventeen exact metadata records and primary edition/artifact paths; most bodies remain unread. **Primary understanding:** [S160](full-reading/S160-belief-and-evidence.md) is complete in the twelve-page author edition. **Evidence disposition:** personal experience leads reported influences on two selected strong opinions per respondent. Two purposively selected projects show small additional localization variance and mixed conditional directions for file repair counts. This is useful, bounded counterevidence to a simple universal distribution/defect claim; it does not exclude coordination burden, other quality outcomes or indirect effects. The proposed bias explanation and dissemination remedy are not tested. **Next action:** S161's metric/judgment comparison, S181's direct metric display intervention, S180/S182's distinct belief comparisons and S162's hot-fixing workflow resolve specific practice methods. Their acquisition/edition/reading gaps are separate from the empirical absence of a Nu benefit estimate. No theme closes or experimental authority changes.

## B01/B10/B12 refinement — judgment needs context and an outcome, 2026-10-01

**Discovery:** SC113–115 and W249–253 resolve five exact Scite records, primary bibliography routes and the archived S161 supplement index; full primary methods of conditional predecessors remain unread. **Primary understanding:** [S161](full-reading/S161-metrics-and-judgment.md) is complete in its sixteen-page accepted manuscript. The archive confirms intended material types, but six correct child requests return 404 and three availability checks find no snapshot; the retained dataset, formulas and questionnaire are unreconstructed. **Evidence disposition:** five individual metrics weakly track selected ratings of ten adjusted educational diagrams. Respondents request behavior, purpose and domain context; these are useful requirements for judgment, not measured gains from adding context or involving humans. No refactoring intervention or maintenance performance is tested. **Next action:** acquired S183 compares metrics with observed professional maintenance across four systems sharing requirements; S181 separately tests a displayed-metric intervention. Preserve S162’s industry workflow, conditional method lineage and the type/runtime/oracle frontiers. Missing method evidence remains distinct from unmeasured Nu benefit; no theme closes or experiment starts.

## B01/B10/B12 refinement — preserve the measured maintenance advantage, 2026-10-01

**Discovery:** SC116 resolves four exact predecessor/shared-case records; W254–262 trace institutional, author and repository access, with a narrow unsuccessful original-data/correction search. **Primary understanding:** [S183](full-reading/S183-maintenance-metrics.md) is complete, all four pages and both tables. Own descriptive arithmetic reproduces LOC/effort rank correlation 1.0 from the printed values; exact allocation, round correction, raw times and inverse-zero handling remain unresolved. **Evidence disposition:** the smallest of four systems implementing common requirements has the lowest observed effort and revision count. Several specialized metrics prefer another system, providing a concrete indicator mismatch. This positive result remains useful without claiming a randomized size effect, validated revision-quality proxy, or lifetime/Nu/agent transfer. **Next action:** S184's fuller shared-case file-level paper remains access-limited despite a native record and primary repository metadata; acquired S181 can now separate metric-induced ratings from task performance. Continue S162 and the type/runtime/oracle frontiers independently. No theme closes or experimental authority changes.

## B01/B10/B12 refinement — display effects and independent outcomes, 2026-10-01

**Discovery:** SC117 returns eight exact-title records with selected outgoing contexts; W263–264 resolve the released package and positive validation/reanalysis alternatives. The bounded replication query establishes no global absence. **Primary understanding:** [S181](full-reading/S181-displayed-metric-anchoring.md) is complete, with [all 45 released data rows and a bounded material check](full-reading/S181-displayed-metric-artifact-check.md). **Evidence disposition:** identical code with a higher displayed metric receives substantially higher difficulty ratings. Own arithmetic reproduces the effect and preserves it when both task-complete excluded rows are retained. A wide interval around the combined time/accuracy contrast leaves performance effects unresolved; a null is not equivalence. Slot assignment, sample-dependent scoring and absent individual answers bound the reconstruction. **Next action:** return to S162’s industry hotfix workflows to balance runtime/practice coverage. S185’s positive Cognitive Complexity validation is now acquired at opening coverage; its method and the later favorable/qualified prediction literature remain live dependencies, not assumed refutations. S184 remains access-limited. No theme or empirical benefit question closes, and no construction authority changes.

## B02/B07/B10/B11/B12 refinement — urgent changes carry deployment and recovery obligations, 2026-10-01

**Discovery:** SC118/W265–268 trace the reused survey, independent runtime-monitoring practice, expanded hotfix review and benchmark lineage; a later empirical APR artifact and thesis are conditional leads. **Primary understanding:** [S162](full-reading/S162-industry-hotfix-workflows.md) is fully reconstructed, including nine case accounts, all figures/tables and a [bounded pinned-release check](full-reading/S162-hotfix-artifact-check.md). **Evidence disposition:** practitioner reports preserve rapid releases, later-stage automation, defensive containment and costly failures. Cross-service and serverless-path incidents show how application tests can miss operational obligations; accepted downtime/data loss expose competing recovery endpoints. Survey/interview descriptions do not identify causal architectural benefit or historical abandonment of live patching. **Next action:** read S186’s independent runtime-anomaly method; then S187’s expanded review and S188’s time-critical case construction as consequential coverage/validation dependencies. S185 and broader type/runtime/oracle queues remain open. No experiment or construction is authorized.

## B06/B07/B10/B11/B12 refinement — useful monitoring has conditional coverage and costs, 2026-10-01

**Discovery:** SC119/W269–270 resolve S186's released methods and version lineage, plus conditional seed-review and positive industrial-deployment leads. **Primary understanding:** [S186](full-reading/S186-runtime-anomaly-practice.md) is fully read, with all five supplement PDFs and a [bounded spreadsheet check](full-reading/S186-runtime-anomaly-artifact-check.md). **Evidence disposition:** reported fast rule-based detection, useful query diagnosis and AI-assisted debugging coexist with false alarms, maintenance, aggregation loss and an instrumentation-induced outage. Delayed leaks, accumulated work and startup/health-check behavior show why an observable anomaly, its cause and retained obligations need separate claims. The review's 80% AI figure is reproduced within its recent-paper coding; it is not industrial prevalence or a comparative benefit estimate. **Next action:** return to acquired S93's original structured-design method to resolve the decomposition/coupling foundation behind architectural claims. S187/S188, S95/S185 and the wider type/oracle/frontier remain consequential; the newest monitoring citations do not automatically outrank them. No theme closes or experimental permission changes.

## B01/B02/B06/B07/B09/B11/B12 refinement — original structured-design mechanisms, 2026-10-01

**Discovery:** SC120's broad title/author retrieval was noisy and was replaced by SC121's three known DOI identities; W271–272 check editions and the conditional sequence/parallelism dependency. **Primary understanding:** [S93](full-reading/S93-structured-design.md) is fully reconstructed in its original 1974 edition, including all 22 figures, the worked redesign and explicit testing/theory limits. **Evidence disposition:** coupling, functional grouping, predictable interfaces, observability, transformation structure and conditional locality have detailed antecedents. The method separates sharing functions from incidental repeated code and acknowledges call/resource costs. It supplies design reasoning, not a calibrated maintenance, compactness or agent effect. Its criterion overlaps with S89's information hiding while assigning different emphasis to functions and anticipated decisions. **Next action:** read acquired S95's inheritance-depth experiments to reconstruct task-dependent navigation/reuse costs and contrary findings. The map's action column is reconciled to remove already completed readings and repeated outcome summaries; those results remain in the primary/evidence columns and notes. The wider type, game, runtime, oracle and review frontiers remain open.

## S95 and S189 — task-dependent navigation/reuse and refreshed access

**Discovery:** SC122/W273–276 resolve the detailed report/package, edition discrepancy and conditional favorable/adverse inheritance predecessors. **Primary understanding:** [S95](full-reading/S95-inheritance-depth-maintenance.md) is fully reconstructed; [S189/material checking](full-reading/S95-S189-inheritance-material-check.md) covers selected report pages, instructions and released aggregates. **Evidence disposition:** duplicated flat code is faster for several understanding-heavy changes, while a deeper hierarchy supports a faster follow-on reuse task among observed participants. Correctness grades, complete solutions, elapsed time, navigation assumptions and missingness are different quantities. Older report/data discrepancies prevent an unchanged reproduction of the later sixteen-row model; they do not erase the observed mixed outcomes. **Next action:** new PDFs reopen eight recorded access gaps. Read S163 for game-specific coverage/oracle alternatives next, then select among S140’s laws, S90’s modularity method, S184’s same-case effort model, S185 and the type/oracle frontier. Access is no longer the barrier for those eight; method understanding still is. No theme closes or experiment starts.

## B05/B07/B12 refinement — coverage vocabulary and an actual output verdict, 2026-10-01

**Discovery:** SC123/W277–278 resolve S163 and two related university theses, with fifteen search occurrences and explicit partial-primary coverage. **Primary understanding:** [S163](full-reading/S163-game-coverage-taxonomy.md) is fully read; [S190/S191 dependencies](full-reading/S163-S190-S191-game-testing-dependencies.md) reconstruct selected review/taxonomy sections and S190’s audio chapter. **Evidence disposition:** 26 definitions distinguish exercised game opportunities, UX, resources and observed failures. They do not form one validated quality score. S190 implements recognition of expected sounds near observed events, a useful explicit verdict beyond sound-play coverage; one-game calibration, environmental recording, event windows and unverified chunk order bound it. S123/S124 already refute a universal absence of explicit game specifications. Shared review lineage supplies no independent replication or coverage-to-fault benefit estimate. **Next action:** return to readable S140 for composition/effect laws, retaining S191’s unread implementation, primary audio comparisons, S90/S184/S185, C02 and independent oracle methods as consequential alternatives. No theme closes or construction starts.

## B02/B04/B06/B07/B12 refinement — a lawful traversal still needs the intended effects, 2026-10-01

**Discovery:** SC124 and W279–282 screen a broad twenty-result prefix, then follow the exact theorem/edition question through primary sources. **Primary understanding:** [S140](full-reading/S140-monadic-maps-folds.md) is complete, with every mathematical page visually read; [S192](full-reading/S192-monadic-fold-dependency-partial.md) is a bounded author/final comparison. **Evidence disposition:** S140 establishes useful conditional monadic-fold/map laws. Its general product premise fails for ordinary state, but a particular datatype may have a valid distribution. Fusion additionally requires the actual homomorphism/naturality equation; S138’s earlier symbolic cases do not refute that theorem. S192 provides the fixed-signature construction while its printed example changes head/tail execution order in both inspected editions. Equal returned lists can conceal different effect logs. This is a narrow symbolic discrepancy, not an executed defect or a refutation of the unification theory. **Next action:** return to S90’s newly readable modularity/change-task method, retaining S184/S185, C02 and oracle/runtime alternatives. The S138/S140 unread-theorem dependency is closed; no theme or empirical benefit question closes.

## S90 / S193 — substantial task benefits with a qualified replication

**Discovery:** SC125–127 and W283–289 trace the original modularity chapter, later investigator account and 1994 conference/report/thesis lineage. Exact Scite lookup misses S90; a broader surname query is noisy and remains a prefix, not evidence of absence. **Primary understanding:** [S90](full-reading/S90-modularity-program-modifiability.md) is complete in nineteen chapter pages; [S193](full-reading/S193-replication-modularity-account.md) is complete in fifteen chapter pages, not its whole book. The original S194 publication and source-material/dissertation details remain unacquired. **Evidence disposition:** S90’s measured phase totals strongly favor modularity on three selected changes, with a near-zero fourth comparison. Excluding typing and half-weighting four later sittings changes the endpoint, but restoring the omitted half strengthens the positive gaps. S193 reports a smaller favorable, nonsignificant first-task replication, with post hoc ability and strategy explanations. Neither null establishes equivalence; neither report identifies broad comprehension as the sole causal route. **Next action:** return to S147’s newly acquired full benchmarking method to strengthen runtime/resource comparison, retaining S194’s exact access gap, S184/S185, C02 and the oracle frontier. No theme closes or experiment starts.

## S147 — consequential measurement repairs without a universal fault label

**Discovery and coverage:** the [complete final-journal note](full-reading/S147-benchmark-practices.md) supersedes the earlier partial-paper status. W290–291 record failed web opens; pinned raw GitHub files supply fourteen bounded artifact inspections, including all343 summary rows and six complete source files. Prior RQ1/CHAMP decisions are reused. No new Scite search page or author experiment was run.

**Disposition for B06/B12:** selected repairs materially change timings, including slowdowns when intended work is retained. Intentional accumulation, necessary per-invocation setup and debugging configurations qualify the static rules. The six-project selection, parameter-level any-instance criterion and separate intrusive setup comparison constrain transfer. The final tables give71 impacted methods, the introduction73, and the older release72 under a different setup grouping; exact aggregate incidence remains unresolved. The released code removes warm-ups but has an outlier filter and alpha.001 instead of the final article’s.01. These discrepancies do not erase observed changes or establish that CHAMP was invalidated: that artifact was explicitly excluded from impact testing.

**Next consequential action:** resume C02’s uncompleted type/extensibility abstracts and primary alternatives. Keep S194’s original replication access action, S184/S185 and the temporal-oracle methods open. Final S147 analysis/data correspondence is a specific remaining method gap, not a reason to halt independent background work or to run a benchmark. No theme, protocol or empirical benefit is declared complete.

## S120 / C02 — mechanism, lexical proxy and maintenance effect

**Discovery:** twelve additional C02 supplied passages reach95/199;104 and later pages remain unexamined. SC128 and W292–295 resolve a topic-modeling foundation, an original Mozilla patch-history comparison and specific access/source boundaries. Neither a finite lookup nor this passage screen is field completion.

**Primary evidence and disposition:** [S120](full-reading/S120-functional-modularity-critique.md) is complete. It offers a reasonable distinction between constructive examples and broad empirical claims, plus a preliminary topic analysis of one GHC snapshot. Its high scattering curves coexist with text/topic-count sensitivity. The surviving parser selects a narrower vocabulary than an all-used-identifiers account and also handles imported scope; the complete fitted-analysis package is unavailable. No comparative maintenance disadvantage follows, and favorable mechanisms/task outcomes elsewhere remain intact.

**Next action:** S195’s acquired twenty-page method can clarify how topic/entropy measurements were validated; S196’s abstract-reported patch findings require the original body, currently unacquired after a publisher403. Records already exist for both. Continue independent C02/type, oracle, runtime and practice work across that specific access boundary. No new worker or experiment is authorized.

## S110 — useful tolerant oracles need separate reference labels

**Discovery:** W305 and exact-title SC129 locate author copies, registered page-range disagreement and the journal/dissertation lineage. **Primary understanding:** [S110](full-reading/S110-model-oracle-steering.md) is complete in eleven pages; extracted author-copy text differs only by page footers. **Evidence disposition:** reachable-state steering has a favorable false-alarm/fault-origin tradeoff against the specified filter in one model-derived example. The15,300 table total conflicts with15,200 declared; cumulative-volume observations change initial category counts, and unsteered recall is conditional on the initial oracle. Offline prioritization, final judgment and unmeasured developer cost remain separate. **Next action:** inspect S197’s acquired expanded method for case diversity, mutant-level complete masking, computation costs and data access. Preserve S111, C02 and broader runtime/independent-oracle work; neither the case nor its continuation closes a theme.


## C02 cached-text screen complete; primary reading priorities change

**Discovery:** all199 cached records now have supplied-text dispositions:195 scientific passages, one boilerplate and three missing abstracts. SC131/W312 add exact identities and primary locators; later native pages remain unexamined. **Primary understanding:** no additional paper is fully read. S198’s object-algebra PDF is acquired after its native record; S199’s positive live-documentation method is still abstract-only. The user’s new S196 PDF closes its specific access barrier, with first-page identity verified. **Evidence disposition:** alternative extension mechanisms, finite-test hypotheses, checker-correction lineage and activity-based change measures deserve primary reconstruction. Mixed book/chapter text, correction metadata, reported associations and an abstract’s positive tool result retain their actual scope. **Next action:** read S196’s original Mozilla patch-history method to resolve the S120/S195 concern-to-consequence dependency, then S198’s object-algebra alternative. S199 and the independent oracle/runtime frontiers remain consequential. Completing these cached passages is neither field saturation nor an empirical benefit estimate.


## S196 — change extent, revision and effort remain different outcomes

**Discovery:** SC132/W313–315 follow positive defect and direct-maintenance counterpoints, with exact title/edition checks and bounded original-data searching. **Primary understanding:** [S196](full-reading/S196-crosscutting-patch-history.md) is complete in eleven pages; all printed tables and formulas were checked. S194/S199 user PDFs and S200’s final journal copy are newly verified at opening scope. **Evidence disposition:** most patches affect few files, greater scattering correlates positively with revision counts, and later mean scattering rises. Among changed revised issues53.90% increase in extent, despite the overall revised-group mean falling7.09→6.58. These are coherent frequency/magnitude distinctions; they do not measure an absence of effort cost or identify a review/architecture effect. The paper’s challenge to universal AOP claims remains useful without discarding its adverse observations. **Next action:** acquired S198’s object-algebra method restores the type/alternative balance; S194, S199, S200, S184/S185 and independent oracle/runtime methods remain consequential. Specific access gaps have closed, not all method gaps or the survey.

## S198: a concrete extension mechanism with explicit integration work

[S198](full-reading/S198-object-algebras.md) places the selected constructor set in a generic factory interface. Clients built against that interface can reuse multiple interpretations and accept richer factories; an insufficient interpreter cannot satisfy a richer builder. This supplies a prior alternative to a globally fixed datatype or visitor interface. It requires factory-based client construction, implementations of new cases and deliberate composition. The imperative example owns mutable state; neither factory typing nor paired interpretations guarantees future behavior, migration or preserved effects.

The Batches application gives useful evidence of use beyond arithmetic expressions, with five interpretations and mutually recursive operations. The paper does not estimate lower maintenance effort, runtime overhead or adoption. All 25 author-manuscript pages are read; the registered 26-page final edition is not compared. Three author-index code downloads fail, leaving their exact implementations unread. Existing Zotero records are preserved and the temporary native API interruption is resolved; S198’s completed note/tag are synchronized. S199’s live-tool comparison is now reconstructed below. S194/S200 and broader primary/discovery gaps stay open.

## S199: preserve the favorable tool result and its comparison boundary

[S199](full-reading/S199-live-pattern-documentation.md) supplies a useful positive comparison: twenty-one students use either a preconfigured live-pattern plugin or IntelliJ with equivalent prepared PDF information/manual diagrams. Five timing subtasks favor the plugin; implementation-only T22 is null/slightly slower. Released task means reproduce approximately62% less comprehension time and53% less total task time. Researcher correctness checking occurred, while the submitted code/diagrams were later lost. This is evidence for that prepared tool bundle, whose detection, diagram generation, editor location and feedback are not separately estimated.

The [artifact check](full-reading/S199-live-pattern-artifact-check.md) locates several reporting discrepancies without reversing those results: a T31/T32 prose swap, an89% external-access claim based on only one subtask, standard-error columns and squared rank-effect values. Counts of internal/external accesses have different meanings and do not establish equal-cost cognitive switching. The six-task comparison does not measure installation, professional adoption, long-term documentation maintenance or future semantic correctness.

G32 returns three other citing works plus a self-loop, not four independent replications; requested contexts are absent. Primary abstracts distinguish DP-LARA’s detector evaluation from S202 Infragenie’s maintainer ratings. S202 now has a native record before reading;36responses after378contacts is a method follow-up, not a reconstructed representative sample. Next read acquired S194’s original replication, retaining S200/S202 and independent type/runtime/oracle paths. No theme or experimental gate is closed.

## S194: original methods qualify the replicated maintenance outcome

[S194](full-reading/S194-original-modularity-replication.md) now resolves the original-paper gap behind the later S193 account. Reported random assignment produces seventeen timed completers from twenty-three volunteers; six fail to finish within four hours. The modular mean remains faster,48.0 versus59.1minutes, with an inconclusive test. Those times exclude editing, and semantic work sometimes moves across the imposed syntax/logic phase boundary. Neither result is a total wall-time effect for everyone assigned.

Exploratory pretest rankings, strategy reports and saved-program comparisons explain possible sources of variation without proving a corrected modularity effect. A hypothetical one-minute testing-time substitution is not a separately observed protocol. These limits preserve the original positive result and the smaller replication rather than turning inconclusiveness into equivalence or filtering away inconvenient behavior. S193/S194 remain one replication lineage. The next method is acquired S200’s positive concern/defect study, alongside S202 and independent runtime/oracle/type frontiers; fuller report/source/test dependencies remain explicit.


### S200 positive concern/defect evidence,2026-10-02

**Discovery coverage:** G33 returns20 incoming edges with20 snippets across12 edges, explicitly truncated. SC135's four exact DOI hits have truncated abstracts; W326–329 supply author archives, primary abstract/locator routes and reader documentation. S203/S204 now have native records before body reading; most graph neighbors remain conditional leads. **Primary understanding:** [S200](full-reading/S200-concern-scattering-defects.md) is fully reconstructed in19 pages, every page visual. The [three-package check](full-reading/S200-concern-scattering-artifacts.md) covers selected requirements, all357 Rhino CSV rows, Mylyn's28 numeric rows and bounded workbook/source identity metadata. **Evidence disposition:** positive correlations and explicit size analyses are retained; own rank arithmetic supports their approximate magnitude. Shared bug assignments, in-sample fitting, unspecified log-zero handling and paper1.5R6/archive1.6R5 correspondence constrain causal/reproduction claims. Manual mapping hours are preparation effort, not a total adoption cost. Different concern definitions and outcomes reconcile this positive evidence with S120/S195/S196 without erasing either. **Next action:** reconstruct S203's feature-comprehension user-study method to connect visibility with observed developer outcomes; retain S204's industrial population and S202's maintainer costs, plus independent type/runtime/oracle methods. An unanswered intervention benefit remains an empirical question; unread methods remain reading gaps. No theme or experiment is closed/opened by this checkpoint.


### S203 earlier manuscript checkpoint,2026-10-02

**Historical access state:** the final-edition checkpoint below supersedes this paragraph’s publication-access and immediate-next-action state.

**Discovery/access:** W330–335 and public tool/repository metadata recover S203’s institutional manuscript text and distinguish the later2019 tool lineage. Original downloads and figure/package routes remain unavailable; S204’s final19-page journal PDF is acquired and first-page verified. **Primary understanding:** [S203](full-reading/S203-feature-comprehension-partial.md) covers all1,171 returned lines but no visual pages or final-edition comparison, so no full-publication credit is added. **Evidence disposition:**54student pairs show faster localization, more exclusive-code detections and fewer false positives with PANGOLIN; EclEmma users identify more shared code. Both receive the author-selected feature tests. PFD separately replaces tests with labeled manual interactions in an author-operated JHotDraw case. Similarity to recorded behavior and its nonzero-report accuracy measure do not prove complete change obligations or repair correctness. **Next action:** read acquired S204’s industrial coupling method while retaining S203’s renderable edition/scoring/run-data gaps, S202’s maintainer practice and independent runtime/type/oracle alternatives. Do not relabel an access limit as absent evidence or an unmeasured repair effect as a failed localization benefit.


### S203 final-edition resolution and professional comparison,2026-10-02

**Discovery coverage:** native attachment refresh closes S203 publication access and supplies S201/S202; exact uppercase package routes remain unavailable. Three pinned later source files confirm Ochiai/count storage but not the historical PFD analysis. **Primary understanding:** [S203](full-reading/S203-spectrum-feature-comprehension.md) is fully read in its23-page final edition, with16 visual pages covering all structured material. **Evidence disposition:** preserve faster/more selective localization and the control’s better shared-code detection. Final TableI differs from the manuscript in one mean. Under the printed PFD formula and one-fixed-positive-trace procedure, its initial accuracy implies an upper bound near.15, incompatible with the plotted rise above.8 without some additional operation or different definition. This is an unresolved analysis correspondence, not grounds to erase the separate student outcome. **Next consequential action:** read S201’s now-accessible professional maintenance experiment, because its population and task can qualify the benefit account directly. S202/S204 and independent runtime/type/oracle methods remain open; neither acquisition nor this checkpoint completes a theme.


### S201 professional evidence and the next practice gap,2026-10-02

**Discovery:** W338/SC136 cover exact archive/correction queries and the two selected DOI identities; these searches do not certify absence of a correction. **Primary understanding:** [S201](full-reading/S201-professional-aspect-maintainability.md) is fully read, including AppendixA and all structured material. The11professionals are randomly assigned after five AspectJ tutorial sessions, but answer on paper/email without tools; detailed pseudocode can receive full modification marks. **Evidence disposition:** retain the null tests and Java-favoring timing pattern, distinguishing outcome-dependent OO time omissions from the unchanged assigned cohort. The printed timing data reproduce its reported descriptives; the changed-line observations conflict with the summaries. This narrows the outcome to a professional cognitive exercise, without erasing its contrary evidence or claiming equivalence. **Next action:** S202’s maintainer evaluation and released package can distinguish useful living documentation from measured savings and ongoing upkeep. S204 and independent runtime/type/oracle methods remain active; residual S201 raw-material access does not block them.


### S202 documentation value, weaker change expectations and data correspondence,2026-10-02

**Discovery/primary understanding:** W339 and the native v1.2 package supply the final nine-page chapter, questionnaire and released data. [S202](full-reading/S202-infragenie-maintainer-evidence.md) now covers all six publication figures, the complete nine-page instrument and bounded passive CSV/notebook reconstruction. **Evidence disposition:** documentation ratings are favorable, including33/36 agreeing that relevant architecture elements are shown; only7/36 expect faster changes and3/36 express the specified planning-use intention. These are separate perceived outcomes, not a measured productivity effect. The prior-diagram subset gives9/12=75%; the notebook’s14-answer unconditioned comparison produces the vicinity of the printed78%. PR counts reproduce as rows, but373unique URLs/366repository paths qualify the claimed378-repository sample. Some accepted contributions and useful detail coexist with missing connections/infrastructure, editor limits and manual update burden. **Next consequence:** S204’s industrial history can change the account of temporal association, size/activity and defect-type variation. Independent runtime/type/oracle frontiers and S202’s unmeasured fidelity/longitudinal benefit remain open; no construction follows.


### S204 industrial associations, temporal units and conditional effects, 2026-10-02

**Discovery/primary understanding:** W340 checks institutional and publisher supporting-material routes. [S204](full-reading/S204-industrial-evolutionary-coupling.md) is fully read in nineteen final pages, including Appendix A; fourteen visual pages cover all figures/tables. **Evidence disposition:** two industrial histories show significant coupling/defect associations in 161/274 financial and 6/11 telecommunications modules, with within-system and defect-type variation. This preserves useful positive evidence for investigating co-change obligations. Histograms select significant modules, fixes contribute to shared historical measures, and no prospective cutoff or coupling-reduction intervention is established. The fitted interaction makes the per-coupling odds ratio `exp(.0747 − .0184 × developers)`, rather than a universal eight-percent probability increase; the outcome is file-level. Type-specific coefficients remain numerically low/trivial under the paper’s thresholds. **Next action:** return to acquired S142 for object-level event/join semantics and explicit comparator costs, strengthening the less developed B03 route. Raw industrial data/external supporting material and independent type/runtime/oracle methods remain separate gaps; no theme or experiment is closed/opened.


### S142 object-level coordination and scoped runtime costs, 2026-10-02

**Discovery/primary understanding:** W341–345 recover historical archive links and the fuller S205 dissertation identity. [S142](full-reading/S142-jescala-coordination.md) is fully read in twelve pages; ten visual pages cover all thirteen figures. All34 printed metric rows are checked passively. Exact archive links now redirect to a homepage, and S205’s primary file routes return HTML despite accessible HAL metadata. **Evidence disposition:** composing events with explicit join groups reduces imperative emissions in every row and source lines in31, while event/handler counts retain exceptions. Object-level queues, dynamic bindings, occurrence-dependent synchronicity and nondeterministic pattern selection differ from Mogemoge’s global ordered pool. Thread pooling materially improves the reported prototype; compiler/parameter/workload choices also preserve unfavorable comparisons, and Figure9 contradicts the small claimed Scala Joins advantage. No measured maintenance benefit, general fairness/deadlock theorem, retained-world migration or author-code reproduction follows. **Next action:** acquired S188’s time-critical repair/oracle method, with S205/source-access and independent type/persistence/fault-sensitivity paths retained. This closes a selected reading gap without closing B03 or the survey.


### S188 urgent repair is a task population, not a temporal guarantee, 2026-10-02

**Discovery/primary understanding:** W346–348 follow the five-page arXiv v1, primary repository/project, all679 workbook classification records and one pinned Flink case. [S188](full-reading/S188-hotbugs-urgent-repair.md) is fully reconstructed; the public artifact inspection is bounded and passive. **Evidence disposition:** useful issue curation and test/setup information support urgent-repair scenarios.109 new integrations plus one inherited Bugs.jar case reconcile the reported110. Workbook labels reverse the paper’s user-facing columns; exact publication-snapshot equivalence is unestablished. FLINK-18425 combines pre-fix production with the developer fix’s regression test, while its branch suffix identifies the pre-fix parent. A recorded functional conversion failure and a short repair interval establish neither temporal-behavior checking nor live deployment. Final-test independence and candidate information require explicit source/test lineage. **Next action:** acquired S173’s real-fault/mutant coupling method can change the fault-sensitivity account. S187’s fuller hot-fix review, S168/S177/S178 and independent type/runtime/migration alternatives remain consequential gaps, not completed by this reading.


### S173 observed coupling and the meaning of a proxy, 2026-10-02

**Discovery/primary understanding:** W349/350 resolve the relocated, pinned S173 artifact. [The ten-page publication](full-reading/S173-mutant-real-fault-coupling.md) is fully read; [four summary tables,337suite lists and two raw cases](full-reading/S173-coupling-artifact-check.md) are reconstructed passively. **Evidence disposition:**272/337selected faults have an observed mutant witness, and each tool contributes cases missed by the other. That positive result,2,828suite IDs and the conditional summary statistics reproduce. Coupling is a finite test-set implication, distinct from mutation-score prediction, generation success or repair benefit. The intermediate suite threshold, one Major operator count and plotted denominators need qualification. Raw Chart-2f observations include non-trigger-list suites, so the printed exclusion rule cannot simply be assumed when criticizing the rate. **Next action:** acquired S132’s longer scanner/parser development experiment can balance type evidence beyond small API tasks. Remaining oracle methods, S187 and the game/runtime/persistence paths stay open; no experiment is started.


### Longer type/development evidence and study lineage, 2026-10-02

**Discovery/primary understanding:** W351–355close S132’s readable-body gap through14rendered pages and check the earlier S206report through its two-page publisher preview. [S132](full-reading/S132-scanner-parser-types.md) includes a27hour new-program task; its scanner/parser measurements and feedback bundle differ from the already reconstructed small API and maintenance experiments. **Evidence disposition:**42printed completion times reproduce lower dynamic scanner time and the reported rank sums/interval; all49participants enter the parser-score null comparison. A wrong mean-difference cell and secondary subgroup count qualify exact reporting without overturning the main observations. Outcome-defined quantiles do not verify skill balance, and a fixed-time quality null is not proof of equal completion time. [S206](full-reading/S206-ecoop-type-study-partial.md) is likely shared-study lineage, not independent confirmation. **Next action:** acquired S184can settle S183’s allocation, logged effort and conditional smell/size model. Original S132logs and S206pp.302–303remain unresolved access dependencies; independent runtime/persistence/oracle work continues. No theme closes or experiment starts.


### Professional effort, conditional models and game-practice transfer, 2026-10-02

**Discovery/primary understanding:** W356–358 accompany [S184’s complete publisher reconstruction](full-reading/S184-smells-maintenance-effort.md), all nine tables and selected published arithmetic. It resolves S183’s eleven analyzed assignments and confirms their shared case. **Evidence disposition:** positive size/churn associations, lower system-C effort and negligible incremental conditional smell fit are preserved. Revisions arise during maintenance; treating them as a quality control does not identify a total architectural/refactoring effect. One unfinished assignment is excluded, and file occurrences are not independent developers. Exact raw-data/log-transform/round-adjustment correspondence remains unresolved. **Next action:** acquired S75 can test how game-specific smell mechanisms and practitioner evidence relate to this general model. The qualitative/inter-smell/problem-endpoint family remains a consequential lead, without being counted as independent corroboration; S185 and runtime/persistence/oracle work stay open. No Nu benefit, theme completion or experimental authorization follows.


### Game practice, instrument meaning and favorable design alternatives, 2026-10-02

**Discovery/primary understanding:** W359–361 close [S75’s author-version reading](full-reading/S75-game-smells-perception.md), with full questionnaire/catalog text and a [bounded data reconstruction](full-reading/S75-game-smells-artifact-check.md). Its final 35-page publication and exact sampling/instrument-stage mapping remain unresolved. **Evidence disposition:** all 28 plotted denominators and 84 percentages reproduce; respondents often endorse concerns with visible runtime/gameplay effects, while coupling, state-pattern and prototyping choices receive contextual defenses. Ratings of descriptions are not measured refactoring benefit. The client-state and dependency labels are broader than their actual vignettes, so their percentages cannot decide an entire architecture. This complements S184’s different effort endpoint without erasing either result. **Next consequential action:** primary routes and pre-reading Zotero records now exist for S207’s reported positive game-development comparison and S208’s game-version/structural-metric analysis. Read their actual interventions, outcomes and denominators before using them as favorable or adverse evidence. S75’s detector and defect-association predecessors remain conditional method leads; independent type, persistence, runtime and oracle frontiers stay open. No construction or additional worker is authorized.


### Suite-size evidence and causal interpretation,2026-10-02

**Discovery/primary understanding:** SC137 retrieves two exact statistical dependencies at requested20; W367–W371 verify the Figsharev5 package, S209 publisher PDF and bounded S210 access attempts. [S168](full-reading/S168-suite-size-confounding.md) is fully read in54final pages, with its seven-page supplement and [passive155CSV/selected-source reconstruction](full-reading/S168-artifact-check.md). [S209](full-reading/S209-logistic-mediation.md) is fully read; [S210](full-reading/S210-mediation-confounding-access.md) remains selected-passage/abstract coverage. **Evidence disposition:** lower reduction loss comes with greater retained size; coverage prioritization improves slightly while mutation prioritization worsens. Those observed tradeoffs survive limitations of the deconfounding explanation. Inverting a regression is not fitting its reverse, logistic coefficients need explicit scales/estimands, and residual orthogonality is not causal removal. Significance-selected project sets and repeated suites constrain transfer. **Next action:** acquired S169’s ground-truth/agreement framework can change how proxy evidence is assessed; check its2022v1 against the2024journal identity before reading. S210 full equations, S168 analysis/source correspondence and independent type/runtime/persistence/oracle paths remain explicit gaps. An unmeasured Nu/D1 effect remains an empirical question; no experiment or theme completion follows.

## B07/B09/B12 refinement — useful proxy agreement has an explicit target, 2026-10-02

**Discovery/primary understanding:** W372–W374 close [S169's final-journal reading](full-reading/S169-assent-proxy-evaluation.md), preserving its earlier partial preprint. All 32 pages and a [bounded pinned-artifact reconstruction](full-reading/S169-assent-artifact-check.md) are complete at the stated coverage. **Evidence disposition:** separating ground truth, compared suites and agreement is useful; mutation's conditional sensitivity, coverage complementarity and automatic-pool means remain positive evidence. Perfect order preservation by test count shows why this particular comparison cannot establish practical value. Own derivation qualifies the claimed tau-A/tau-C equivalence; released population, BC missingness and alternate-analysis correspondence remain explicit. Matching PC/automatic means do not erase those limits. **Next action:** return to B04/B06's persistent-vector, iterator and transient-update frontier to resolve actual workload, sharing and ownership costs. The selected adequacy-method chain is sufficiently reconstructed to inform the survey; unread conditional predecessors are not a command to expand it indefinitely. S210 access and exact artifact gaps remain separate from unmeasured Nu effects. No theme or experimental hold changes.

## B07/B09/B12 refinement — the statistical dependency is now primary-read, 2026-10-02

**Discovery/primary understanding:** native refresh finds S210’s existing supplied PDF and supersedes the preceding access label; [all nine original-journal pages](full-reading/S210-mediation-confounding-access.md) are now read, including displayed equations and examples. **Evidence disposition:** its OLS product/difference identity requires fitting the third variable on the predictor. Own example arithmetic reproduces a beneficial total direction coexisting with an adverse component. Equivalent coefficient calculations cannot choose the causal interpretation; intervention assignment does not automatically identify mediator effects. The external simulation supplement remains unread, separately from the now-closed publication-method gap. **Next action:** resume B04/B06’s persistent-collection costs; this bounded dependency adds no experimental permission or need to expand the statistical citation chain.

## B04/B06 refinement — persistence has an ownership and workload boundary, 2026-10-02

**Discovery/primary understanding:** [S211](full-reading/S211-rrb-systems-persistence.md) now has a complete28page publication reconstruction and a [bounded2017source inspection](full-reading/S211-rrb-artifact-check.md). W375–378 resolve S212/S213 acquisition and identify the public report/source routes; exact published-run correspondence remains unresolved. Their bodies remain pending, with an explicit S213 edition/complexity discrepancy.

**Evidence disposition:** S211 supplies a concrete predecessor for persistent state with unboxed trees, configurable reclamation and conditional mutation. Its transient batches improve many measured operations; large ordered updates remain8×slower than the listed mutable array, and general transient concat adds little. The source keeps one starting root while dropping intermediate versions and prepares mutable-array copies outside timing. This is useful feasibility/cost evidence under stated semantics, not a growing-history or development-benefit experiment. The paper itself leaves the dynamic-aliasing workload hypothesis untested. Its proposed game/database application is future work.

**Next consequential action:** read S213’s transient ownership, complexity guarantees and measurements, reconciling the acquired author edition with final metadata; follow S212’s iterator semantics where needed. Preserve independent retained-history, .NET/game, practice and type routes. The remaining Nu-specific empirical uncertainty is distinct from these still-unread methods, and no experimental hold changes.

## B04/B06/B07 refinement — conversions and guarantees have operational conditions, 2026-10-02

**Discovery/primary understanding:** [S213](full-reading/S213-transient-sequence.md) now has all33author-edition pages,19figures and both appendices read. W379–380 resolve official abstract/source routes; [eleven full release files plus selected ranges](full-reading/S213-sek-artifact-check.md) establish bounded correspondence. The34page final PDF remains403. Its abstract’s looser complexity bound is compatible with the author PDF, so an edition boundary is preserved without manufacturing a theorem contradiction.

**Evidence disposition:** ownership, packed chunks, compaction and buffering provide a concrete general sequence alternative. O(log_K N) amortized end operations require O(K log_K N) edit credit; the preserving release snapshot costs O(K), while the cheaper conversion clears its input. Positive large-stack results coexist with small-size penalties. The linear benchmark retains no history; a source denominator discrepancy affects absolute ns/operation but leaves ratios at fixed size unchanged. Model-based nonlinear testing and single-sequence space bounds answer different questions from proof, concurrent safety, retained-history memory and temporal correctness. Hidden monotonic writes have an explicit concurrent-push limitation.

**Next consequential action:** S212’s persistent iterators directly challenge the traversal/update interface used by S211/S213. Its acquired edition is still partial and will be read next. Retained-history, MapReplay/.NET, game/practice and type frontiers remain; unknown Nu-specific empirical benefit is not relabeled as an unread-method gap or settled by another search page. No experimental hold changes.

## B01/B04/B06/B07/B12 refinement — cursor values and measured outputs, 2026-10-02

**Discovery/primary understanding:** [S212](full-reading/S212-persistent-iterators.md) is complete in22page arXivv1, with all9figures/2tables. W381–383 follow its cited AEC-v2 artifact and three primary C++ semantic clauses. [Eight complete files plus selected ranges](full-reading/S212-libfpp-artifact-check.md) resolve version extraction, workload setup and allocation accounting; exact final-edition/run correspondence remains open.

**Evidence disposition:** zipper-local updates defer full-container reconstruction and preserve independent cursor values, supplying a concrete imperative interface alternative. The paper reports positive concat and selected set-erase costs with large vector penalties. In the release, iterator append discards each edited cursor and update does not extract its changed output; cumulative allocation is mislabeled if interpreted as live memory. The unopt recipe does not isolate allocator choice. These findings qualify specific measurements while preserving the design and unaffected reported results. Editor convenience and invalidation avoidance are semantic/design evidence, not measured maintenance productivity or all-memory-safety guarantees.

**Next consequential action:** return to the [screened MapReplay method](nu-background-runtime-screen-2026-10-01.md), whose application traces may change representativeness judgments for these synthetic workloads. .NET/game transfer and type/evolution/practice frontiers remain independent. Retaining more unexplored citations is not itself a reason to postpone synthesis indefinitely; material reading gaps remain distinct from empirical benefits the literature cannot establish. All construction holds remain.

## B04/B06/B07/B12 refinement — realistic traces and conditional prediction, 2026-10-02

**Discovery/primary understanding:** [S214](full-reading/S214-mapreplay.md) upgrades the existing SC81/W154 MapReplay lead to all 14 pages and all figures/tables. W384–387 resolve a pinned source and a 46-trace public release; [bounded inspection](full-reading/S214-mapreplay-artifact-check.md) separates acquired source, small release members, trace metadata and unacquired executable/full dataset. It is no longer an unread method or an absent-data claim.

**Evidence disposition:** application-derived operation distributions are a constructive alternative to isolated collection microbenchmarks. Preserve 18/21 directional agreement, three weak disagreements and reported eight-hour versus 72-hour schedules in one capacity-change family. Source canonicalization and omitted operations qualify general fidelity; one released trace differs from the paper’s reported inputs. Correlation is not an independent correctness oracle, and library sensitivity is not whole-application benefit. These qualifications refine transfer without erasing the observed positive relationship.

**Next consequential action:** after the selected S211–S214 state/runtime methods, return to acquired **S185**, *An Empirical Validation of Cognitive Complexity as a Measure of Source Code Understandability* (DOI10.1145/3382494.3410636). Its positive validation could change B01/B11/B12’s interpretation of understandability proxies after S181/S183. It is a known primary-reading gap, unlike an unmeasured Nu benefit. B02’s GATlab/typed-default/dependent-matching methods, B08’s expanded S187 review and .NET/game representativeness remain independent frontiers, prioritized by claim consequence. No construction hold changes.

## B01/B11/B12 refinement — positive metric evidence and its construct, 2026-10-02

**Discovery/primary understanding:** [S185](full-reading/S185-cognitive-complexity-validation.md) now closes the selected validation-method reading gap: all twelve pages, all figures/tables and [bounded released analysis](full-reading/S185-cognitive-complexity-artifact-check.md). W388–390 distinguish the selected arXiv edition, publisher access and versioned Zenodo package. Nine studies/327 snippet entries is the time subset of ten/427, rather than conflicting editions.

**Evidence disposition:** preserve positive average time association (.54), negative ease-rating association (−.29), mixed correctness (−.13) and a positive derived time/correctness score (.40). Repeated samples/outcomes and substantial heterogeneity bound generalization. Study 8’s first-seen identifier filter explains its printed descriptive range; no effect size is recalculated. A construct can have scoped validation while remaining unsuitable as a complete behavioral oracle or causal architecture-benefit estimate. S181’s equal-score tasks are not thereby known to be equally difficult.

**Next consequential action:** return to **B02/B04’s GATlab**, *Modeling and Programming with Generalized Algebraic Theories*, DOI10.46298/entics.14666, already screened at C02 2-12. The primary publication resolves a concrete theory-map/model-migration alternative. Reconstruct which types, equations and executable mappings are enforced and whether migration means representation reinterpretation, data transformation or live-state transition. This can change the novelty boundary around Nu without requiring a new experiment. Typed defaults, dependent matching, S187 and temporal/runtime transfer remain independent frontiers; the whole survey remains active.

## B02/B04/B07 refinement — algebraic maps and preservation premises, 2026-10-02

**Discovery/primary understanding:** [S215](full-reading/S215-gatlab-model-migration.md) closes C02 2-12’s primary-method gap at the19-page publisher edition. W391–394 and the [bounded source check](full-reading/S215-gatlab-artifact-check.md) distinguish publication, preprints and a dated0.1.3 implementation. The source pin is not proven to be the exact manuscript code.

**Evidence disposition:** a theory map A→B provides a reusable interpretation and derives A-model behavior from an existing B-model. Explicit model values, generated delegation and dependent membership checks are concrete design alternatives. Law preservation requires valid mappings and lawful implementations; method registration and sort checks do not establish those premises. The inspected code explicitly leaves axiom-proof checking unfinished. This supports a useful mechanism while limiting “migration” to its actual model/interface role; heap transitions, pending work and external-effect preservation remain separate obligations. The paper supplies no comparative Nu or maintenance estimate.

**Next consequential action:** reconstruct **C02 2-71, *Inductive types deconstructed: the calculus of united constructions***. Its typed default branches bear directly on future-case handling and can challenge an overly broad reading of catch-all weakness. Follow dependent matching and algebraic testing where they change enforcement/semantics claims; retain the expanded S187 practice review and runtime/oracle transfer. No construction hold changes.

## B02/B06/B07 refinement — default refinement and behavior, 2026-10-02

**Discovery/primary understanding:** [S216](full-reading/S216-united-constructions.md) upgrades C02 2-71 to all12 author-copy pages and visual coverage of every rule/proof sketch. W395–399 distinguish final-publication metadata, successful exact-PDF access, denied publisher/homepage routes and a different Typer theory document. The latter is not a recovered CUC proof package.

**Evidence disposition:** a failed tag test can leave a default branch with a precise residual union and equality evidence. This is constructive prior art against universally equating catch-alls with erased case information. Formal cast erasure and a sketched translation/relative-consistency argument have their stated calculus scope. They neither implement proposed extensible-union features nor establish correct new application behavior or a practical speedup. The D1 proposal now cites this boundary while preserving its fixed-toolchain, initially equivalent and potentially exhaustive arms.

**Next consequential action:** resolve the edition relationship and read C02 1-78/2-91, *Elaborating dependent (co)pattern matching: No pattern left behind*. Its source-clause/core-elaboration relation can change claims about what checker feedback guarantees. Algebraic testing, S187 and independent runtime/temporal frontiers remain prioritized by consequence, with all holds intact.

## B02/B07/B08 refinement — elaboration, branch coverage and editing, 2026-10-02

**Discovery/primary understanding:** [S217](full-reading/S217-dependent-copattern-elaboration.md) closes the recorded dependent-(co)pattern edition/method gap through all43 journal pages,20 figures,2 tables and displayed proofs. W400–403 distinguish the2018 precursor, final2020 body and bounded implementation evidence. No extra C02 page is fetched; its unchanged passage screening is reused.

**Evidence disposition:** well-typed, covering case trees and faithful source-clause translation are separately justified. The source guarantee uses conservative matching: an earlier blocked component cannot be bypassed simply because another component mismatches. The formal catch-all construction compresses source clauses while expanding generated branches; the reported Agda implementation retains individual-clause checking because interactive holes can otherwise acquire incompatible branch types. Two public issues substantiate concrete implementation problems and author-reported correction work, without an independent execution or comparative maintenance estimate. Closed-signature extension preserves checking only under restrictions that exclude adding cases to completed datatypes.

**Next consequential action:** read S187’s already acquired58-page expanded hot-fixing review. Its revised140-article corpus could change B04/B08/B10/B12’s update/state/recovery alternatives and discovery coverage. The B01–B12 map’s next actions now retain each theme’s own remaining question instead of repeating the completed type-paper route. Algebraic testing and .NET/game/temporal transfer remain separate live frontiers; unknown benefit is not mislabeled an unread method or proof of absence.


## B04/B08/B10/B12 refinement — urgent fixes, live updates and evidence units, 2026-10-02

**Discovery/primary understanding:** [S187](full-reading/S187-hotfix-review.md) is now fully reconstructed at its58-page ACM Just Accepted edition. Its primary keyword search, five backward-snowball rounds, feedback additions and thematic coding produce the stated140-paper review. A pinned public roster has140 distinct titles,1986–2024. W404–405 record exact coverage, identity and passive tag counts. Most listed primary methods remain review-level evidence, not newly completed readings.

**Evidence disposition:** urgent production intervention and no-restart updating are different dimensions. The review preserves successful patching, diagnostic and deployment cases alongside incomplete repair, lost functionality and recovery failures. Configuration, containment, selective updates, VM migration and component restarts are relevant alternatives. Its tables/narrative/roster disagree on some counts; it excludes much general runtime updating and independent post-deployment monitoring. Consequently it supports a scoped mechanism/practice map, not proof of absent methods, a pooled success rate or measured Nu benefit. Later [S162](full-reading/S162-industry-hotfix-workflows.md) and [S188](full-reading/S188-hotbugs-urgent-repair.md) refine the review’s dated developer-practice/benchmark gaps. Publication attention and reported workplace automation are different measurements.

**Next consequential action:** resolve/read ReDAC, Rasche/Polze2008(ref115/roster61), before crediting the review’s Paint.NET/no-overhead summary. Its cyclic distributed-component reconfiguration can change the still-open .NET/interactive-state assumptions and cost account. Algebraic testing and independent temporal/game evidence remain live; this is a source-located next method, not a construction or experiment.

## B04/B06/B08/B10 refinement — cyclic-call quiescence and cost units, 2026-10-02

[S218](full-reading/S218-redac-cyclic-reconfiguration.md) reconstructs all available author-uploaded ReDAC text, while retaining the inaccessible PDF/diagram/code/plot check as a primary-coverage gap. The method drains guarded synchronous calls selectively so that cyclic reentry can finish, with logical thread IDs, per-capsule counters and an expanded dependency set for shared resources. It establishes an update point; it delegates representation conversion and does not discharge every application or temporal obligation.

Preserve the favorable reported synchronization comparison: 151.68 versus 324.19 microseconds per 1,000 calls. Relative to the 5.96-microsecond interface baseline, own arithmetic gives 145.72 nanoseconds additional time per guarded call. Neither the small absolute cost nor the roughly 53% reduction versus locks implies zero overhead. Generated blackout measurements and the PaintDotNet report have different workloads and evidential force. This qualifies S187’s compressed no-overhead wording without discarding the successful application account. The direct GUI/state-transfer predecessor is the next method dependency where accessible; algebraic-testing and temporal/game work continue independently.


**Access disposition:** [S219](full-reading/S219-gui-updates-access.md), the direct graphical-state dependency, has a native record but no acquired PDF. Its advertised public routes fail; metadata/one extracted passage cannot settle its migration or cost method. Keep S218’s visual gap and S219’s body gap distinct from unmeasured empirical benefit. Continue the already-recorded C02 1-83 algebraic-testing foundation for B02/B07/B12, with independent temporal/game alternatives still open.

## B02/B07/B12 refinement — finite tests and their premises, 2026-10-02

**Discovery/primary understanding:** [S220](full-reading/S220-algebraic-specification-testing.md) closes C02 1-83’s selected-edition method gap through all 32 arXiv v1 pages, 21 visual pages and the complete bibliography. W413–414 distinguish the earlier report, selected manuscript and unacquired publisher body. A chapter reference is a follow-up route, not an independently read primary experiment.

**Evidence disposition:** algebraic testing supplies constructive specification-based suites and an explicit conformance argument. Reachable deterministic implementation models, reliable observations, representative subdomains and finite bounds are material premises. Abstract observations may legitimately ignore internal representations, but replacing a nonobservable conditional premise with finite observed agreement can bias the verdict. The chapter reports a useful subway coverage discovery, a hidden-state/large-instance miss, a specification anomaly and a null data-type result. Preserve these separate outcomes while seeking their primary methods; no pooled Nu benefit or universal adequacy follows.

**Next consequential action:** resolve/read reference 52, Marre et al.’s 1992 formal-versus-statistical testing experiment, for its actual fault population, selected suites, budgets and missed case. That can change the evidence account beyond the chapter’s summary. S218’s visuals and S219’s full body remain explicit access tasks; game/runtime and temporal alternatives remain independent open frontiers. This checkpoint authorizes no construction or execution.

## B04/B07/B08/B12 refinement — controlled state and initialization, 2026-10-02

**Discovery/primary understanding:** [S221](full-reading/S221-formal-statistical-testing-access.md) resolves S220 reference52 and its revised chapter, with only two preview pages read. The coauthor’s [S222 thesis](full-reading/S222-statistical-testing-thesis.md) supplies a bounded107/187-page reconstruction, including complete unit/integration chapters and43visual pages. SC139 returns1/1 exact-DOI metadata at requestedlimit20; W415–419 record the failed original-body routes, preview and accessible thesis. The full-publication count stays184; primary understanding advances without falsely completing either work.

**Evidence disposition:** the formal-testing case’s1345 eligible cases are mutants. Closed-loop control, additional state observation and the statistical comparator’s direct control produce different detection/eligibility conditions and suite budgets. Preserve the nearly complete algebraic result. In the same component’s integration study, functional441-input suites outperform the recorded structural500/uniform5300 suites on diagnosed faults. Refining initialization interactions reveals a further real defect missed by prior suites. These favorable results coexist with dependent repairs, same-case adaptation and unmeasured engineering cost. They do not establish industrial defect prevalence or a Nu effect. Steady-state activation counts and finite-run temporal hit guarantees require separate arguments.

**Next consequential action:** return to **SC06/S68 L85, Scaling Games to Epic Proportions**, DOI10.1145/1247480.1247486. It is an already-discovered primary gap: declarative game-state/effect processing, restricted iteration and batched query execution can challenge an overly narrow functional-world/ECS comparison. Resolve language/publication lineage and native holdings before selected body reading, then reconstruct semantics, comparator workload and measured costs. This advances B03/B05/B06 independently of the S218 visual, S219 body and original S221 body access tasks. The unmeasured transfer to Nu remains an empirical question, not a reason for indiscriminate acquisition. All holds remain.

## B03/B05/B06 refinement — common-state decisions and shared query work, 2026-10-02

[S223](full-reading/S223-sgl-game-scaling.md) now reconstructs the original SGL scaling paper in all12author-copy pages. A tick reads common state, computes per-unit effects, combines supported effects and applies game mechanics afterward. Restricted query forms expose overlapping work to bag-algebra rewrites and shared spatial/aggregate indexes. That is a concrete game-runtime alternative to immediate shared mutation; it does not implement retained-world history or arbitrary external-effect replay.

Preserve the positive2007experiment: a tailored C++ combat simulator with rebuilt indexes supports over12,000units under an average10ticks/s requirement, versus fewer than1,100with repeated scans. Its500-tick elapsed-time endpoint is not a rendered-frame or worst-case-latency measure. Automatic general-language compilation, raw results, engineering effort and Nu transfer remain separate gaps. The author identifies a later Sandbox2008 language paper as the more definitive SGL account; reconstruct that next before transferring early syntax or describing repeated timings as an independent study.

## B03/B05/B06/B08 refinement — effect constraints and changing workloads, 2026-10-02

[S224](full-reading/S224-sgl-state-effect-pattern.md) completes the eight-page later SGL account in text and visually. Write-only effects, immutable locals, two-phase accumulation and explicit update rules enable shared query processing. The loot example locates ownership on the uniquely owned object; arbitrary host postprocessing and asynchronous pathfinding retain separate obligations. These are concrete design alternatives and integration costs, not measured maintenance effects.

Figure5 repeats S223's favorable simulator result. The new healer-only comparison shows crossing strategy costs, but Figure6's legend conflicts with the prose about which curve is indexing versus pruning. Keep the workload-dependent argument and uncertainty together. Dynamic switching is discussed rather than measured; the paper explicitly leaves pipelining and parallelization unapplied to SGL. The completed lineage now informs synthesis instead of remaining the next unread source.

## B03/B04/B05/B08/B10 refinement — live mechanics and explicit reset policy, 2026-10-02

[S225](full-reading/S225-micro-machinations-adaptation.md) reconstructs the complete Micro-Machinations adaptation account and bounded pinned source. A C# tower-defense host embeds a C++ library, supplies collision/time/UI activations and receives state/type notifications. Named model deltas can add or change mechanics between steps; a generic host convention exposes new interactive nodes. The inspected pool-change path resets its stored quantity to the new declared initial value. Retained identity, intended migration and whole-game state preservation are therefore distinct.

The authors’ roughly15-minute design/modeling iterations and brief favorable playtests remain useful prototype experience. There is no controlled effort comparison or measured total library/integration budget. The code snapshot postdates the conference, and combined versus separate scripts differ materially; no exact historical execution or whole-game equivalence is claimed. This closes the selected game-adaptation reading and moves the next primary action to acquired S156’s empirical comparison, while broader agent and live-method frontiers remain open.

## B01/B10/B11/B12 refinement — favorable guidelines and inconclusive paradigm ranking, 2026-10-02

[S156](full-reading/S156-oo-structured-design-maintainability.md) now has a complete22-page journal reconstruction. Thirteen attending students worked on four different application/condition packets; they identified change locations without implementing changes. Conforming OO shows better understanding and location rate than degraded OO, while its comparison with conforming structured design is inconclusive. Structured-versus-OO impact results, reversed structured understanding means and nonsignificant endpoints remain visible. Fixed domains, unequal attendance, missing pairs and exploratory alpha limit attribution; significance in one contrast but not another is not a direct interaction estimate.

S155 is a later, larger internal replication of the OO comparison with revised materials. It supplies further favorable document-task evidence without becoming an independent research-group/application-family replication or measuring net implementation benefit. S156's body-access gap is resolved; other editions, task packets and participant data remain distinct gaps. The survey now returns to the retained game-agent evaluation frontier, preserving the positive human evidence and all experimental holds.


## B07/B09/B12 refinement — visual feedback and actual behavioral observation, 2026-10-02

[S226](full-reading/S226-gamedevbench.md) reconstructs the full29-page GameDevBench publication and bounded source at July/October pins. Its333 tutorial-derived tasks include179 variants. GPT-5.4 improves41.1%→52.0% with both feedback tools/guidance while median cost rises$0.156→$0.522; smaller-model declines and video-only advantages remain. The baseline already permits images/videos. Scene-file edits dominate the reported gold patch, so edited lines are not a language or context-efficiency effect.

Deterministic tests provide useful scene/state evidence. One inspected projectile task directly invokes callbacks and checks a counter/deletion/UI, without driving real collision timing. Filtered workspaces and post-solver tests exist in July source; stronger confinement arrives in September. Original run binding and the28-configuration per-task result packet remain unresolved within inspected routes. Passing assertions, trusted score emission, permitted development feedback and independent temporal obligations are separate requirements.

Read acquired S227 next to compare GUI-driven playtesting and shared repair memory, then S228's industrial edit/play route. C05 discovery, S125 calibration artifacts and Nu/D1 benefit remain distinct unresolved questions. No experiment is authorized and no background theme is declared complete.


## B07/B09/B12 refinement — playtesting, memory and judge correspondence, 2026-10-02

[S227](full-reading/S227-continual-gui-playtesting.md) reconstructs all19 pages of PlaytestArena/Play2Code. The reported rubric means improve29.7%→52.2%→66.8% across direct, agentic and GUI-playtesting pipelines. Nested memory scores and the no-GUI contrast provide closer positive component evidence. Three blinded human judges agree with the GUI scorer on84.2% of criteria in32 builds, withκ=.64; this is useful alignment evidence despite an unresolved rubric-count/version discrepancy.

Development playtesting lacks the final rubric and can end repair on its own confidence; the scoring role receives the rubric. Common five-round caps do not establish equal cost or exposure. Complexity tiers are defined using observed gains, and the printed thresholds, trajectory plot and human-comparison direction conflict. Group averages and post-outcome groups cannot demonstrate individual retained behavior or a pure complexity mechanism. The pinned/live-matching public artifact is an eight-demo gallery; complete task/rubric/scaffold/raw-result correspondence remains unresolved.

These are prior coding/playtesting/memory mechanisms with favorable scoped outcomes, not a Nu architecture or D1 source-convention estimate. Continue S228's industrial edit/play client/server route; keep C05 discovery and conditional OpenGame/incremental-playtesting dependencies separate from missing artifacts and unmeasured empirical transfer. All holds persist.


## B07/B09/B12 refinement — native runtime tests have specific obligations, 2026-10-02

[S228](full-reading/S228-opengameeval.md) adds a complete primary Roblox article and bounded source comparison, without increasing full-paper coverage. Prepared native-engine tasks already vary context and support edit/server/client assertions. Historical pass-rate/reliability metrics and the reported difficulty of contextual work remain useful scoped evidence. The same four example test bodies are present in article-date/current snapshots.

The health case samples client values after server-triggered damage, with no server-healing assertion and exact endpoints that favor a particular update schedule. Baseplate traffic counts repeated observations of a switched state; suburban cases collect shared color-change flags. These tests observe behavior but do not establish a complete safe cycle, all delay instants, authoritative healing or preservation of pedestrian behavior. This does not reproduce an exploit, reject a reported run or erase the benchmark's contribution.

Together, S125/S226/S227/S228 resolve several concrete game-evaluation alternatives. Continue C05 discovery by consequence, retaining specific baseline/incremental-playtesting dependencies and existing live/type/runtime gaps. Source coverage, oracle validation, representative maintenance value and the unmeasured Nu/D1 effect remain separate. No construction or experiment follows from this synthesis.


## C05 continuation: typed UI generation and professional-workflow leads

The [completed C05 supplied-text screen](nu-background-agents-search-2026-10-02.md) adds94 passages without another search page or a field-completeness claim. It retains both favorable generalization/professional-benefit leads and adverse robustness/evolution leads. Primary methods, not abstract rankings, determine their eventual evidential role.

[S230](full-reading/S230-arkts-code-generation.md) separates compilation from behavior and reports a favorable30-task progression from7 to11 solves using examples and compiler repair. Preserve those counts while keeping the two-example/two-call bundle distinct from a causal type-system effect. Its main rankings condition on returned responses, its judge distribution is explicitly reconstructed from code features, and figure/table/denominator conflicts plus request-only data limit quantitative use. Native UI labels do not supply inspected lifecycle or temporal assertions.

[S229](full-reading/S229-picoscenes-expert-ai.md) could add direct professional architecture/implementation effort and runtime evidence; its full methods remain inaccessible through the tried routes. A different HarmonyOS paper, S231, has a public compiler-feedback implementation and an explicitly linked Research Square/final lineage. Read that method next; do not merge its data with S230 or replace the missing PicoScenes comparison with more benchmark summaries. No experiment or new worker is authorized.


## B02/B07/B09/B12 refinement — native UI repair and semantic preservation, 2026-10-03

[S231](full-reading/S231-harmonyos-compiler-feedback.md) reports strong compilation gains from carrying current source and compiler errors into repeated generation. Its separate manual checks yield 88/91, 76/83 and 74/82 successes among the three selected models’ compilable outputs: respectively 88, 76 and 74 confirmed successes per 100 tasks. These favorable results coexist with flat/small gains in several smaller models and specific state, gesture, animation and appearance failures. The study supplies evidence beyond compilation alone, while lacking a matched-budget diagnostic ablation and baseline semantic comparison.

The inspected native UI release makes the repair mechanism concrete. It supplies a three-attempt helper and 100 test prompts, but no test references/metadata or original ten-attempt outcome packet; its two inspected test files are generic examples. The selected preprint is fully read, while the final journal edition remains a separate body-access gap. Reported human assessment, source reconstruction and reproduction stay distinct.

For Nu’s claimed innovations, useful diagnostics and native declarative state are established alternatives, not sufficient proof of preserving intended interaction during change. Compiler success can coexist with removing text that should be replaced. Conversely, those residual failures do not erase substantial reported successes. Next reconstruct the retained modular translation study’s local type-compatibility and I/O checks; its project-level scope can change the preservation argument more than another isolated code-generation ranking. D1 and all construction remain held.

## B02/B07/B09/B12 refinement — modular translation has several preservation gates, 2026-10-03

[S232](full-reading/S232-modular-validated-translation.md) reconstructs all 26 final-publication pages and bounded artifact methods. Feature rules, dependency-local translation, observed-value type compatibility and source-backed callee mocks are concrete predecessors. The paper reports 98% average compilable functions and 73% validated functions; compatibility checks improve six of eight project rows. Preserve those positive results alongside the five unchanged semantic-repair cases and the nested no-feature/no-type ablation. Different historical comparison sets do not isolate a language or architecture effect.

Compatibility is relative to test-derived representations, and semantic repair reuses those snapshots. Successful-call outputs and selected state changes, coarse failure outcomes and whole-system temporal behavior are different contracts. The released default route ends before the paper's semantic repair phase, advertises six replay cases with different rates, and reports compilation over all declaration items versus equivalence over available unit tests. These are specific correspondence limits, not newly executed adverse outcomes or grounds to discard the reported gains.

For Nu, modular decomposition and useful type feedback cannot be treated as new mechanisms or sufficient preservation evidence. Net developer benefit remains a separate question. S232 borrows that benefit claim from its reference 29, *Repository-Level Compositional Code Translation and Validation*, arXiv2410.24117. Read that primary comparator/user-study method next after native identity checks, while retaining S229's exact access gap and the independent live/temporal/type frontiers. No experiment or worker is authorized.

## B02/B07/B09/B10/B12 refinement — translation completion and verdict validity, 2026-10-03

[S233](full-reading/S233-alphatrans-compositional-validation.md) resolves S232’s borrowed developer-effort dependency. AlphaTrans combines source transformation, manually completed type mappings, skeletons, dependency-local translation and source-backed Graal/translated-test execution. Its final paper reports25.14% functional validation; two participants finish four partial translations in5.5,11,30and34hours, averaging20.1. Preserve that useful feasibility evidence. No unaided comparison measures time saved, and the completed test suites also change: a selected empty test gains assertions. Test repair is useful work, while all-passing completion is not an independent unchanged oracle.

Bounded primary-source inspection and stored-status arithmetic locate a material reporting error. All20 project rows’ GS/M1 counts match, but38of118 DeepSeek and9of34 GPT M1 Some fragments have zero passing tests. The release labels multiple all-failed tests `some-all` and includes them in Some. Positive Graal-success and M1 All counts remain intact; pending/status-policy and all-fragment syntax differences preclude declaring a wholly recovered final result packet. No model, compiler or author test was run.

This narrows benefit and preservation claims without turning the survey into a catalogue of defects. The next consequential method is MatchFixAgent, surfaced through the primary author’s page, because it directly investigates translation-validation verdicts and human comparison. Its abstract is a lead, not accepted evidence; resolve edition and native record before reading. ReCodeAgent/TRAM/skeleton-guided translation, S229’s access-limited professional comparison and the independent live/temporal/type frontiers retain separate priorities. All holds persist.

## B02/B07/B09/B10/B12 refinement — useful repair needs a common contract, 2026-10-03

[S234](full-reading/S234-matchfixagent-validation-repair.md) completes MatchFixAgent’s final publication and a bounded released-data reconstruction. Its 99.2% is availability of a verdict. Authors favor its verdict in 88/145 retained sampled disagreements; the result is strong against Oxidizer (37/44) and AlphaTrans (25/34), near even against SKEL (23/43), and adverse against RustRepoTrans (3/24). The 134/265 versus 49/265 accepted repairs are useful conditional improvement evidence. Preserve these outcomes without converting fixed per-project/per-direction review, changed validation routes or shared datasets into overall accuracy or independent replications.

The annotations make the contract consequential: accepted language idioms and valid calling contexts can differ from the prompt’s strict state/output agreement, and some favorable labels concern unused variables or allocation quality. One annotation conflates a repaired function with its original. Agreement also contains four jointly wrong judgments in 110 reviewed cases. The workbook reconstructs the main counts and locates an initial-rater agreement discrepancy; the later reporter prefers test/repair verdicts and counts newly covered fragments from status transitions. Those findings sharpen the distinction between diagnostic exposure, generated execution, observations and intended behavior. No author code or model was run.

For Nu, retain an explicit input/state correspondence, effects and version boundary before making preservation or iteration claims. Unknown net maintenance benefit remains an empirical question, while unread temporal-breakpoint/monitor methods remain primary-reading gaps. The next action is acquired S105, to reconstruct alternate histories and pending temporal observations; S106/S99/S107 retain their own scopes. Other translation neighbors are conditional, not automatic additions. All holds persist.

## B03/B04/B07/B08/B12 refinement — temporal history has a starting boundary, 2026-10-03

[S105](full-reading/S105-temporal-breakpoints.md) supplies a concrete positive mechanism: compose an unmodified subject-language model with a branch-specific temporal monitor, then search for an accepting witness. Regular-expression/statechart reachability and Büchi accepting cycles answer different questions; a stored execution trace alone is not the latter. The mutual-exclusion demonstrations establish capability without a comparative debugging-time or adoption-cost estimate.

Primary formal/prototype reading locates the boundary relevant to Nu: a lookup starts at selected current subject state and constructs fresh breakpoint state, then projects the witness back into subject history. Earlier pending monitor obligations are not automatically retained. Deadlock stuttering, step visibility, acceptance/fairness assumptions and property-preserving reductions need explicit treatment. The literal formal set definitions differ from the described product/union, while the JavaScript uses enumeration; source/exposition and sample-version gaps prevent claiming inspected proof or reproduction. These limits leave the useful mechanism intact.

S100’s temporal-witness dependency is now primary-read. The next consequential source is acquired S106, to distinguish abstract environment exploration from monitored execution and determine the observation relation. S99/S107 remain separate live/remote routes. Unmeasured Nu benefit is an empirical gap; these unread methods are coverage gaps. All holds remain.

## B03/B04/B06/B07/B08/B10/B12 refinement — shared observation and measured cost, 2026-10-03

[S106](full-reading/S106-unified-verification-monitoring.md) resolves the complete verification/monitoring method. Reusing the same deterministic observer across a model checker and device execution removes a property-translation boundary. It still leaves different environments and schedulers: offline exploration uses abstractions, while monitoring follows the actual trace. The appendix locates event-pool presence and oldest-event predicates, so queued, consumed and externally effected events cannot be equated.

Preserve the positive interleaving-defect discovery and repair, matching LTL/PUSM verdicts, and average 6.7% memory/7.4% time advantage for the latter checking route in one example. Those routes share atoms and system semantics, and implementation languages differ. Monitoring costs 50.8% execution time for the measured CCI and 8.2% executable size; the stated scope excludes real-time constraints. No-failure observations and a conditional claim about detecting the old defect are not a measured runtime sensitivity result. The small formalization release supplies definitions with located correspondence limits, not a reproduced C runtime or result packet.

For research value, the architecture question is now more specific: does shared state/observation improve correct completed changes or diagnosis enough to justify setup, monitoring and deployment costs in the relevant workload? Generic integrated verification is already a prior capability. A Nu benefit remains unmeasured, while the next coverage gap is acquired S99’s generated-code live-update method. S107, professional S229 access and .NET/game transfer remain distinct; another verification neighbor is not automatically the next paper. All holds persist.

## B03/B04/B05/B06/B08/B10/B12 refinement — live editing moves costs and obligations, 2026-10-03

[S99](full-reading/S99-generated-code-live-modeling.md) supplies a generated-code rival: compiled control code and mutable runtime tables, with edited actions redirected to an interpreter. In the largest model, seven single-edit rows take 1.3–2.1 ms versus 608 ms for regeneration/build/hot-patching; ten edits take 9.9–18.1 ms versus 1,192 ms. Preserve this substantial latency advantage alongside about 25% greater peak memory and 70% slower execution of one selected interpreted action. Human change success, total integration effort and game-frame latency are unmeasured. The printed 510/514 ms CPU values contradict the claimed slowdown; a row-ratio error does not reverse the edit advantage.

The state contract is explicit: one capsule pauses at a run-to-completion boundary; active-state deletion requires user selection; only the latest exit per state is retained. Replay restores that capsule and injects messages while its peers and external effects are not rewound. The paper acknowledges unexpected peer reactions. The public release matches all twelve generation timings and both hot-patching component sums, but those sums exclude detection delay and the snapshot does not recover the complete final replay/timing packet.

For funder-facing value, compare the actual edit/state/effect boundaries and total cost of successful changes. Compiled execution, mutable tables and local replay already offer useful live development, so merely reproducing such capability would be a weak Nu contribution. Next acquired S107 can resolve a distinct remote/device-state question; then consolidate the selected architecture alternatives. Other theme coverage and access gaps remain explicit, and no new experiment follows.

## Remote replay and the limits of path coverage

[S107](full-reading/S107-remote-concolic-debugging.md) supplies a concrete remote/game alternative. It records inputs and instruction counts, transfers a snapshot for analysis, and resets/replays when changing past choices. This lowers forward-execution costs while relinquishing reversible I/O. The formal reachability argument concerns represented VM state and manual feasible-input mocks; bounded concolic suggestions and control-flow representatives do not prove all application behaviors. The motor-speed example makes this value/branch distinction explicit.

Preserve the useful results: most selected analyses finish below one second; the game produces three paths at its chosen horizon; trace execution is much cheaper than frequent snapshots. Preserve the 219.613-second calibration case and the cost of conditioning analysis on a fixed state. Hardware, emulator and later modified-source results remain separate. Together with S99/S105/S106, these methods support a comparison by state, history, effects, coverage and costs. Their availability neither establishes a Nu advantage nor removes the primary MIO compensation-method dependency or other B01–B12 gaps.

## B02/B06/B08/B10/B12 refinement — coexisting views require retained information, 2026-10-03

[S103](full-reading/S103-bidirectional-schema-versions.md) adds a preservation contract distinct from the earlier debugger and migration methods: several writable schemas can coexist while data moves between physical representations. Bidirectional SMOs retain invisible columns, unmatched rows, tuple identity, deleted-copy markers and conflicting replica values. Developer-supplied defaults and a preferred replica remain policy choices. The worked split round trips and appendix mappings are substantive formal evidence; the printed padding rules still need explicit admissible-state premises before a universal implementation claim. Logical schema preservation supplies no oracle for new application behavior or external effects.

The evaluation preserves positive results: **359 versus three** authored evolution lines, **182 versus one** migration line, subsecond example code generation and substantially faster access from suitable physical placements. The repeated 359-fold prose is inconsistent with the table’s three-line denominator. Adaptive-placement results include migration cost, but the switch is instructed when another placement is faster; the comparator stays fixed. The 171-version Wikimedia history and synthetic pairs establish representation/performance cases, not 171 independent maintenance trials. Source compactness, generated-code overhead, physical optimization and net developer benefit remain different endpoints.

W451–W453 identify matching normalized conference/v2 body text and a **2018 journal extension, S236**, whose institutional abstract adds an advisor. Its native record exists before body reading. That extension is the strongest immediate gap: reconstruct its selection inputs, added experiments, state premises and conference lineage before treating advisor support as absent. S102 and the independent game/type/practice frontiers remain; this checkpoint closes no B theme and changes no construction/model/worker hold.

## B02/B06/B08/B10/B12 refinement — redundancy and workload advice, 2026-10-03

[S236’s accepted manuscript](full-reading/S236-multischema-placement-advisor.md) is now fully read: two covers and 25 article pages, including the new physical-design advisor. It explicitly reuses S103/CoDEL/thesis formal results and much of the TasKy/Wikimedia evaluation. The extension adds redundant placements, hardware/DBMS-specific calibration and a bounded evolutionary search over valid storage configurations. Own-view read-back and best-effort cross-view propagation remain different contracts; the referenced formal/domain premises and zero-downtime service are not newly proved here.

Preserve the added favorable evidence. In 21 TasKy workload conditions, the proposal is at most 10% above the measured best among 59 placements. A larger illustrated run takes 828 ms for 429 evolved members and improves a physically applied workload from 2.35 to 0.26 seconds (9.04-fold measured; tenfold estimated), with unknown global optimum. Cost-model calibration, prediction, migration, advisor search and DBA review have separate denominators. Redundancy can reduce auxiliary writes, so a simple read-benefit/write-penalty rule would misrepresent the mechanism. The journal’s 209 versus conference’s 211 historical SMOs is a version/accounting difference, not independent replication.

SC153 and W454–W459 resolve accepted-body access and record partial Scite coverage, three outgoing citation contexts and remaining artifact/final-edition limits. The next material gap is **S102 Cambria**: reconstruct its document and patch contract before extending relational conclusions to heterogeneous or concurrent documents. Denicek, persistent objects, concurrent DDL and source/schema practice are retained leads with their actual reading limits. This closes neither a B theme nor the wider survey and changes no construction, model or worker hold.

## B02/B04/B08/B10/B12 refinement — document edits, history and intent, 2026-10-03

[S102 Cambria](full-reading/S102-cambria-document-evolution.md) now has complete report/appendix/static-figure coverage. Explicit lenses translate supported document edits and derive related schemas/types. The authors’ positive multi-month workflow experience is retained alongside prototype instability, an acknowledged scalar/list deletion inconsistency and the absence of formal performance measurement. Neither a valid new schema nor a cleared diagnostic selects the correct policy for information hidden from an older client.

Its Automerge integration preserves original writer-schema changes and translates on read, reconstructing identity/path state and intermediate views. This supports later interpretation without proving every cross-schema concurrent schedule or user-intent property. Fifteen complete source files, two bounded ranges and six locked-version comparisons corroborate the mechanism and distinguish later core behavior from the adapter’s dependency. Four embedded clips are sampled at six timestamps each; no dynamic output, author program or test suite is run.

SC154 requests20 and returns no exact-title records; W460–W461 supply the direct primary report, media and pinned code. This retrieval limit is not scientific absence. **S87 Denicek** is next for computations and dependency evolution in the document substrate, with its S73/S86 lineage retained. Modern .NET/game, type/context/multi-turn and other stated frontiers remain independent. This closes no theme and changes no experimental hold.

## B02/B04/B06/B08/B10/B12 refinement — document computation and live-state boundaries, 2026-10-03

[S87 Denicek](full-reading/S87-denicek-document-computation.md) now has complete 19-page publisher coverage, all18 figures and both appendices read. Rebase-style history merging, explicit references and separate evaluated edits jointly support replayed interactions, schema/code evolution and invalidation. The convergence model differs from retaining distinct document schemas; the substrate cannot rewrite arbitrary formula logic depending on an implicit string format. The paper explicitly excludes preserving arbitrary evaluation state during source edits.

Preserve the successful author-built notebook and reported implementation ease as qualitative construction evidence. Six formative examples, a later aligned same-team system and heuristic evaluation do not constitute independent replications or measured developer-effort savings. Cumbersome use at thousands of rows, conflict over-approximation and integration/UI limits are reported adverse observations, without a calibrated runtime estimate.

W462–W463 follow the verified author/source routes. Eleven complete files and three bounded ranges at the September2025 pin show broader conflict checking than the earlier same-kind rule, whole-formula dependencies and separate merge/invalidation policies. Visible test/source signature mismatches limit runnable-artifact claims; no compiler or author test is executed. Supplementary video access remains uncompleted. The next independent discovery priority is modern .NET/game cost and integration evidence through focused C06/C07 reformulation; C05 and other material frontiers remain. No theme or experimental hold closes.


## Selected object history is a different contract — S247, 2026-10-04

**Discovery/primary understanding:** W515–519 recover and distinguish HistOOry's full-work aliases, two-page companion,17-page author copy and conflicting institutional page metadata. All17 acquired pages are text/visually read, with14 figures and28 references; native attachment/hash and exact note are verified. The primary mechanism is reconstructed; an implementation/raw packet, final18-page equivalence and the discovered talk remain separate gaps.

**Evidence disposition:** [S247](full-reading/S247-histoory-object-history.md) supplies selected field histories with explicit capture points, process-local observation and propagation into referenced/replacement objects. Unversioned fields expose present values, and writes to them from a historical query affect the present. Reachability-based collection does not establish a bounded retention window. These conditions differ from immutable world roots and Tardis checkpoint/replay, so neither the old3× secondary account nor a cheap snapshot primitive estimates Nu costs.

The primary retains real gains: repeated singleton checks and larger swap collections can avoid growing copy costs, and a one-entry historical cache improves repeated queries. It also retains substantial assignment instrumentation costs, copying-favorable small swaps, and copying below HistOOry throughout the plotted bulk-insertion range. The1.3× tracing ratio uses an already expensive stateless tracer as denominator. The printed swap predicates differ in identity/equality, with no acquired artifact proving their measured equivalence. Preserve results, comparator scope and static correspondence limits separately.

**Next consequential action:** Follow SC161's already retained Snowflake primary, DOI10.1145/3141879, for the .NET allocation/reclamation boundary and latency evidence. The older Smalltalk/modified-CLR mechanisms are now understood at their selected editions; another mechanism paper does not resolve unknown Nu benefit. Game-change/adoption, historical-obligation methods and explicit access/visual gaps remain independent. No construction or experiment follows from this checkpoint.


## Reclamation is not history or uniformly lower latency — S248, 2026-10-04

**Discovery/primary understanding:** SC166 returns1/1 exact record with requested limit20; W520–523 resolve the primary, linked earlier report and bounded artifact routes. [S248 Snowflake](full-reading/S248-snowflake-manual-memory.md) now has complete25-page primary text/visual coverage and complete AppendixA pp25–40 of the40-page report. The manual-heap/GC boundary, unique owners, stack-only guards, deferred epochs, thread ejection and card/trie scanning are reconstructed. The exact implementation/raw packet remains unlocated; no runtime is executed. This closes an unread-method gap without closing B04/B06 or certifying final-publisher bytes.

**Evidence disposition:** Manual allocation provides substantial cache and memory gains under explicit API/frontend/runtime changes. It also transfers costs: guard operations, slower allocation, retained guards, GC scanning of manual roots and synchronous work. Infer.NET saves memory while running slightly slower. Havlak’s fast loop phase coexists with slower important end-to-end cases and more memory; its one-thread large-case Gen2 maximum grows6.8→149.4ms despite fewer collections. These are scoped positive/adverse observations, not a universal ranking, independent Nu experiment or game-frame tail estimate.

The comparison now distinguishes five levers: retained immutable world roots, selected historical fields, checkpoint-plus-input replay, explicit manual lifetimes and ordinary GC policy. They control different state and cost boundaries. A safe pointer does not encode an old world; a retained world does not reverse an external effect; fewer GC events do not ensure smaller pauses. This is the actionable mechanism synthesis for Nu, whose pinned source revision remains unchanged.

**Next consequential action:** Follow primary game-change/adoption evidence to establish the workload and integration decisions these mechanisms would serve. Reuse S75/S207/S208 and the professional workflow findings; do not interpret another runtime-method reading as a measurement of maintenance value. Preserve the unresolved Nu benefit, source/raw/edition limits and historical-instruction frontier separately. No construction, model, benchmark, candidate run or additional worker follows from this reading.


## Game changes cross source, assets and workflow — S249–S251, 2026-10-04

**Discovery/primary understanding:** [S249](full-reading/S249-game-postmortems-155.md) supplies all10 primary pages, [S250](full-reading/S250-game-industry-problems.md) all18 preprint pages and complete appendix, and [S251](full-reading/S251-game-problem-dataset.md) all5 dataset-paper pages. The [bounded release check](full-reading/game-postmortem-data-check-2026-10-04.md) reconciles the older1,035-row and later927-row type distributions with a shared200-title corpus. These are three publications, not555 independent game cases. S249’s raw appendix, exact final editions and S250’s final subtype correspondence remain explicit reconstruction gaps. The search roster records actual ranges and noisy reformulation; no industrial-practice frontier is declared exhaustive.

**Evidence disposition:** Retrospective accounts identify real kinds of work and useful solutions. S249 preserves fast iteration, effective reuse and productive preparation alongside documentation/learning burdens. S250’s selected coded passages show why a source-only benefit claim is incomplete. Dead Head Fred’s engine reuse coexists with animation, dialogue, levels and balancing work as mechanics change. Draconus’s shipped loading improves while developer loading stays slow and implementation takes substantial effort. Outrealm’s engine helps early prototyping but later requirements exceed the developer’s available time/skill; its quoted author explicitly distinguishes that from engine incapability.

For Nu, connect each claimed mechanism to an outcome it could actually change:

| Claim-relevant boundary | Consequential outcome | What this evidence leaves unresolved |
| --- | --- | --- |
| Source organization, typed cases and change location | Correct integrated successor behavior and retained obligations | Diagnostic exposure does not establish asset, animation, balancing or temporal correctness. |
| Live editing, retained state and faster loads | Time from an edit to informative feedback, including preparation/recovery | Fast shipped runtime or a fast restore primitive does not establish a shorter development loop. |
| Engine reuse and tool integration | Completed change plus learning, adapter, asset-pipeline and validation work | Available functionality and favorable author experience do not identify total adoption savings. |
| Testing and automation | Adequate behavioral observation and reliable execution of the pipeline | The released MotoGP07 quotation contains automation but costly infrastructure failures; Casey’s Contraptions reports framework-boundary testability costs. |
| Iteration toward a better game | Improved player experience with explicitly changed requirements | Beneficial redesign can increase work; it is not an equal-behavior implementation comparison. |

The supported near-balance of production and management problem entries remains useful despite inconsistent type percentages and subtype packets. Mention frequencies, chosen quotations and coded root-cause labels are not measured severity, prevalence or causal intervention effects. Absence of a testing mention cannot prove absence of testing. This reading narrows unsupported transfer while preserving favorable practitioner outcomes.

**Next consequential action:** reconstruct the professional-method evidence in Cowboys, already retained by S51 and the earlier assessment. It can challenge the interpretation using a different evidence source; automatically adding another postmortem catalogue would not do that. Newer engine/adoption routes, the2026 extension and SC168 offset20 remain open, prioritized by claim consequence. No construction, recruitment, compiler/model/author-code execution, benchmark or additional worker is authorized.

## Practitioner comparison sharpens the game-change claim — S252, 2026-10-04

[S252](full-reading/S252-game-practitioner-comparison.md) reconstructs all11 author-copy pages, both demographic tables,28 survey items and40 references. It adds an independent source of practice evidence to the retrospective postmortem lineage:14 interviews, followed by145 Games,100 Office and119 Other respondents within Microsoft. The authors select28 of84 proposed agreement items; their role mix, response rates and organizational setting constrain generalization. This is a perceived-practice comparison, not a language or tool intervention.

Useful differences survive that scope. Requirement clarity is lower, creativity and skill diversity more valued, and communication with non-engineers substantially more valued in Games against both comparators. Reuse ease, technical debt, architecture evolution and several other prominent interview themes are inconclusive in the survey. Unit testing and automation-complexity differences hold against Other but not Office; scripted simulation is lower against Office, contrary to the interview prediction. Own arithmetic checks all56 rounded p-values and recovers the18 reported discoveries; it does not reconstruct raw ratings or rank-sum tests.

For Nu, these findings motivate observing whether an explicit state/tool structure helps people communicate, preserve intended behavior and integrate content while requirements evolve. They do not imply that game development lacks automation, that all games share one maintenance model, or that a type/runtime mechanism improves creative discovery. Requirements clarity and subjective enjoyment are distinct; the latter need not be determined by the same oracle as regression correctness. Artists, assets, engine reuse and internal tool pipelines belong in the work boundary alongside source changes.

The linked study-materials PDF remains unavailable after DNS/web failure, targeted searches and a rate-limited archive request. This access gap is distinct from empirical Nu uncertainty. Next resolve the cited EASE2013 tool-expectations primary, which can change the adoption and integration account. Modern engine evidence, the2026 postmortem extension and retained search continuations remain open. No construction, author-code/compiler/model execution, recruitment or worker is authorized.

## Existing-tool fit is part of research value — S253, 2026-10-04

[S253](full-reading/S253-game-tool-expectations-partial.md) now reconstructs all accessible indexed primary text, including four tables textually and15 references. It remains a partial publication reading: publisher/ResearchGate downloads are denied, the old author PDF is missing, CiteSeer retrieval fails, and the questionnaire site is unavailable. No visual, raw-data or publisher-edition equivalence is inferred. Full-work coverage remains221.

The seven selected Finnish organizations contribute27 interview sessions during2012, not a demonstrated sample of27 distinct developers. Their generally favorable view of current infrastructure survives the study’s limits. Five currently use third-party engines, one more plans a switch, and three of the current users modify the engine locally. Reuse, rapid prototyping, recycled/purchased assets and familiar tools support reported work; crashes, editor restrictions, portability and compatibility remain concrete needs. Satisfaction does not identify its cause, and a small qualitative sample does not establish present-day prevalence or a controlled adoption effect.

For Nu, a meaningful claim must connect a mechanism to a specific obligation or cost in an existing workflow. Replacing a whole toolchain is not automatically valuable when developers report effective engines and pipelines. Preserve integration with asset formats, teammates, platforms and version control in the value account. The separate evidence for developer feedback, creative requirement discovery, behavior preservation and runtime performance should remain separate.

Next follow the retained newer multiple-case reuse study, resolving its edition and case/comparator before crediting an independent effect. Generative-asset/tool-integration preferences and contemporary practice are consequential further leads. The S253 access gaps stay executable follow-ups, while the survey continues independent accessible work. No construction, author-code execution, model, recruitment or additional worker occurs.

## Prefab reuse broadens the change boundary — S254,2026-10-04

[S254](full-reading/S254-game-reuse-cases-partial.md) reconstructs the indexed March2025 preprint and its acquired January2025 replication materials. Main-PDF images, dense figure labels and final/SSRN body correspondence remain unavailable, so complete-work coverage stays221. The two studios and five games add situated evidence of useful reuse through configured objects, shared scripts, assets and design tools, alongside setup effort, propagated errors, redundancy and abandoned objects.

The package materially sharpens interpretation. Its instruments ask about initial effort and whether savings were actually measured, and distinguish engine/editor work from IDE work. Follow-up prompts preserve conflicting5%/65% and40%/80% estimates without the resolving answers. The published2–5% cross-project summary therefore remains an author-reported account with unresolved denominators. Five released trees contain86/2,036/1,481/158/84 named leaves; the preprint’s NeonHAT/VTM counts are1,318/85. These are source/version discrepancies, not new failed experiments. Selected answer images still preserve positive, concrete accounts of sharing dialogue, interactables and menu functionality.

The consequential distinction is **configured-object reuse, inferred similarity, change history and completed maintenance**. A tree can reveal relationships developers find useful without recording chronological ancestry or proving a bug fix. For Nu, source-level obligations must connect to the asset/configuration/dependency work that surrounds a successful change. Existing engine support, beneficial reuse and the cost of integrating or learning a new approach all belong in the comparison.

Next read the direct2023 SPL/clone-and-own comparison and resolve its2022 lineage before crediting its reported model/code-dependent correctness, efficiency and satisfaction effects. Phylogenix’s encoding/inference method and the2025 Unreal model/code experiment remain concrete further dependencies. No construction, compiler/model/author-code execution, recruitment or extra worker occurs.

## Prepared representations have measured task benefits — S255,2026-10-04

[S255](full-reading/S255-game-product-lines-comparison-partial.md) adds a direct game-content reuse comparison. Its supplied product-line configurations improve correction-template scores in both MDD and CDD tasks. CDD also has higher correctness per minute and satisfaction; MDD efficiency/satisfaction differences remain inconclusive. These are useful positive and null results. At this initial checkpoint, indexed text and bounded materials were reconstructed. The later S256 continuation acquires the19-page author PDF and closes its visual gap; publisher-final correspondence remains unverified.

The released instructions show what the benefit covers: handwritten C++ or feature selections, and complete SDML drawings versus named-fragment assignments. Choices differ in granularity and documentation as well as reuse organization. Participants report that the constrained overview helps them see options and avoid omissions, while code/models offer more freedom and precise detail. This suggests distinct questions about supported variants and extending the representation to meet new requirements. The experiment does not measure compiler execution, retained runtime behavior, tool construction or total maintenance cost.

Own descriptive checks retain50 CDD correctness/efficiency values per method,51 time/satisfaction values and28 per MDD method. The headline51% efficiency gain accompanies about9% shorter CDD mean task time; the score/time ratio is a different outcome. Table6 and the released summary both give p=.45 for the correctness interaction, contrary to the prose; the favorable within-paradigm differences remain. Ten CDD respondents report prior boss-modeling experiments, with cross-study person linkage unresolved. Reused2022 MDD observations are not a new replication.

For Nu, preserve the plausible benefit of explicit domain choices, together with requirements discovery, expressive limits, library evolution and integration cost. None establishes D1’s equivalent-catch-all treatment effect. The predecessor edition and released-file lineage are now reconstructed in S256; next inspect the retained contemporary Unreal comparison. No new execution or worker follows from this evidence.


## Reuse benefits retain their experiment identity — S255/S256, 2026-10-04

[S256](full-reading/S256-game-product-line-predecessor.md) completes the original MDD comparison and [S255](full-reading/S255-game-product-lines-comparison-partial.md) closes its main-PDF visual gap. The 28-person study is reused, with 78 identical files across the released packages. This strengthens the bound positive correctness result and inconclusive efficiency/satisfaction contrasts without adding independent evidence. Main publication coverage reaches223 works; no B theme or survey-completion claim follows.

The original recruitment account identifies one noncompleting student; the shared analysis rows cover the28 completers. Repeated sequence-table cells and a code-based training deck in the later-uploaded nominal2022 archive qualify report/material correspondence, while the shared MDD forms and data remain useful. These findings distinguish a known task effect, a historical artifact question and an unmeasured Nu benefit. Preserve that separation when reading the2025 Unreal comparison and assessing research value from tool integration, requirement discovery, expressive scope and total maintenance work.


## Contemporary integrated task evidence — S257, 2026-10-04

[S257](full-reading/S257-unreal-model-code-comparison.md) completes the2025 Unreal comparison and changes the integration account: this is work in Unreal/Visual Studio, with supplied movement and damage functions, rather than the earlier handwritten product-line submissions. Blueprint correctness averages49.585 versus24.894 on the study rubric; the selected model gives p=.036. Efficiency and satisfaction remain inconclusive. Positive effects therefore deserve a place in the Nu background alongside adverse and null evidence.

The comparison bundles representation, editor support, prepared code/assets and participants' prior skills. The rubric averages expected operations with a Works item; it does not expose a complete temporal oracle. Warmup/configuration is outside the measured tasks. Participant accounts favor quick iteration and hybrid code/model use while reporting testing, merging and modularity costs. These findings make preserving rapid feedback across stateful changes a concrete research-value question; they do not prove either the older coexistence explanation or the later visual-constraint explanation, much less a Nu benefit.

Reading the cited bug-localization counterevidence can establish whether outcomes change with the activity. Resolving the newer author-listed Modeling Paradox work can establish extension/sample lineage. These are primary-understanding gaps, separate from the still-unmeasured benefit of Nu's particular architecture. Selected-author publication coverage is224; no B theme or broad-survey completion follows, and no experiment is authorized.


## Representation benefits depend on the activity — S258, 2026-10-04

[S258](full-reading/S258-model-code-bug-localization.md) supplies the missing bug-localization comparison behind S257's counterevidence. A static diagram/code task produces no significant pooled performance/productivity difference, but ten professionals achieve higher code F1; model satisfaction is favorable across cohorts. Released means reproduce. This is a meaningful adverse contrast for a blanket model-superiority claim, without overturning S257's favorable prepared Unreal implementation result.

The distinctions are observable in the materials: lists of suspected locations versus implementation and behavioral checking; static files versus integrated editors; unfamiliar domain rules versus prepared scaffolding. Source-value/link discrepancies, timing overruns and selected statistical warnings qualify exact effect interpretation. Preference, completion, location accuracy and preserved behavior must stay separate. The newer Unreal title's sample/edition lineage and runtime/energy costs remain primary-understanding gaps; Nu's own comparative benefit remains an empirical question. Selected-author publication coverage is225; no theme or broad-survey completion follows.


## A new comparator with shared Unreal evidence — S259, 2026-10-04

[S259](full-reading/S259-blueprints-unity-visual-scripting.md) strengthens the case for taking tool integration and task fit seriously: its released BP/UVS movement-task comparison favors BP in scores, efficiency and satisfaction. The qualitative material explains useful domain operations and hybrid collaboration while retaining BP testing/merge costs and possible UVS orchestration/state-machine uses. This is valuable evidence at its observed scope.

All16 BP records match S257's BP movement subset, and the BP interview themes recur. It therefore adds a comparator rather than an independent replication of Unreal benefits. Engine familiarity and task requirements are bundled; a numerical error in the discussion, inconsistent time policy and subjective-label disagreement narrow precise claims without erasing the observed gains. A node-based interface alone neither explains adoption nor guarantees good abstraction, debugging or temporal correctness.

For Nu, the research proposition needs a traceable connection from domain/state operations and diagnostic feedback to completed work, followed by an account of integration, testing, merging and runtime cost. The2024 energy/task predecessor is the immediate primary-reading gap; API/documentation checks can separately test the claimed diagnostic mechanism. Nu's actual comparative benefit remains empirical and unknown. Selected-author coverage is226; no theme or broad survey closes.


## Development benefit and runtime cost use different units — S260, 2026-10-04

[S260](full-reading/S260-unreal-energy.md) adds useful workload-specific runtime evidence from three UE5.3.2 BP/C++ pairs. Its reported power is similar over equal elapsed time; frame-normalized results favor C++ for health/inventory and BP for input. The inventory headline confuses48% higher BP with48% lower C++; printed values imply about32% lower C++. The conversion between watts, frame duration and reported frame values remains unresolved, so a corrected headline alone does not validate an energy estimate.

These results complement the development-task gains in S257/S259 and the localization counterweight in S258. They do not measure a joint lifecycle benefit, verify exact inherited task/project identity or identify the compiler mechanism. The global household-savings extrapolation lacks the required workload and equal-service transfer. For Nu, source organization, completed changes, frame latency and memory/state cost need their own observations under an explicit runtime target.

The primary author edition is complete; the Zenodo link/API and inferred DOI lookup did not yield the artifact. Retain run inclusion, conversion and project-equivalence gaps without treating them as absence of data. The related published Unity/Unreal comparison and independent Unity-build follow-on can change the runtime interpretation; neither is primary-read yet. Broader tool, practice and temporal/state questions remain open. No runtime or candidate experiment is authorized by this reading.


## Runtime tradeoffs depend on the scene — S261, 2026-10-04

[S261](full-reading/S261-unity-unreal-energy.md) reports lower DUT power for Unity in static-mesh/physics scenes and for Unreal in animated meshes. Preserve that observed change in ordering and the reported significance; it is evidence against a universal engine ranking. The experiment compares equal-duration runs, while useful work, image quality, simulation trajectories and target frame rates remain unverified. Its 38 excluded and 142 retained tabulated runs improve the inclusion account but do not resolve the allocation between two execution orders.

The complete current author edition and partial older arXiv check share 192 numerical table cells. They form one empirical lineage, despite a changed global-energy illustration. The physics difference is 350.78% higher Unreal or 77.82% lower Unity; neither the erroneous “351% lower” wording nor the hypothetical best-of-engines combination measures global savings. Baseline/table presentation and a dynamic figure labeled with Physics data remain unresolved. Six declared artifact archives were inventoried only at the public metadata level; no file contents were acquired.

Together with S257–S260, this supports investigating concrete development and runtime tradeoffs. It does not establish Nu’s net benefit, identify the compiler explanation or imply that easier construction is cost-free. The compiler/debugger contract is now a more consequential next method check than extending the global extrapolation. Independent build configurations, practical integration, assets and temporal/state obligations remain live alternatives under the existing construction hold.


## Tool support makes the preservation question more specific — 2026-10-04

[Unreal’s documented Blueprint contracts](full-reading/unreal-blueprint-contracts-2026-10-04.md) connect the development/runtime studies to actual described tool mechanisms: compilation to VM operations, object reconstruction, execution-sensitive watches and some automatic type-change conversions. These are positive capabilities to include when characterizing Nu, rather than treating game engines as an absence-of-support baseline. Four original illustrations and bounded indexed documentation are preserved in Zotero; no exact shipped source or running system is validated.

The release illustration's inserted Truncate node sharpens the research distinction: maintaining a valid graph after a type change and preserving the application's intended values are separate obligations. Likewise, copied properties do not establish the fate of pending effects, and a watched last-executed pin is not a temporal oracle. The documentation can ground a proposed mechanism, while S257/S259's bundled task evidence and S260's unexplained runtime difference retain their original inferential limits.

The next priority returns to integration work around interactive content through Phylogenix. More general debugger documentation cannot answer unknown Nu benefit; exact-version coverage gaps and empirical questions remain explicitly different. Full-paper coverage stays at228, and no experiment or worker is authorized.


## Asset relationships and integration are distinct claims — S262,2026-10-04

[S262](full-reading/S262-phylogenix-integration-partial.md) narrows the Phylogenix method gap using all available primary text, the complete guide and selected source. Four commercial applications and an organized view of prefab relationships are useful prior capabilities. The acquired S254 package, however, counts components, measures count mismatches and merges closest pairs by average distance; the manuscript describes binary encoding, Manhattan distance and neighbor joining. Source-version and execution correspondence remain explicit rather than silently reconciling these accounts.

For Nu, asset identity, serialized structure, generated artifacts, cross-tool handoff and hosted-service assumptions belong in the work boundary. A tree can help developers inspect relationships without establishing chronological ancestry, behavior preservation or completed maintenance benefit. The four Unity games recur in S254; printed/released prefab counts differ for VTM and NeonHAT. Preserve S254’s favorable situated reuse accounts without treating another publication as independent game evidence.

B03/B04/B10/B12 now reflect those mechanisms and limits. Paper figures/final edition and remaining pinned source are coverage gaps; unknown Nu benefit is a different residual. Follow the primary latent-content claim, with modern practice and independent runtime/temporal alternatives still open. Full-paper count remains228 and no theme or experiment is closed/opened by this checkpoint.

## Content-generation extension and the remaining access boundary — S263/S264,2026-10-04

[The partial readings](full-reading/S263-S264-content-generation-access.md) establish that the journal approach extends the2024 conference work and adds feature injection. Its introduction reports favorable family-fit outcomes; full metrics/results and replication material remain inaccessible. Preserve those reported positives while keeping generation validity, empirical independence and developer benefit unresolved. The native indexed-text attachments are labeled partial, and no complete reading or field-absence claim follows from the failed access routes.

B10/B12 now retain that distinction. Continue S265's accessible independent Unity-build primary/artifact for the cost and workload boundary, with generation access, temporal/type, newer practice and the conditional scoping package22692269 remaining separate continuations. No theme or experiment is closed/opened.

## Build settings refine the cost comparison — S265,2026-10-05 HKT

[S265](full-reading/S265-unity-build-energy-partial.md) preserves a favorable production-configuration result without a universal backend ranking. Its author classification tables reproduce34lower-power alternatives among65. Four matrices match420FantasyKingdom runs; Faster Runtime/Release has5.15% lower CPU+GPU power and0.068% higher mean recorded FPS than development Mono. These descriptive differences clarify magnitude and measurement boundary without rerunning inference or the engine.

For Nu, runtime service, build settings, configured assets and integration must accompany the source-organization account. Net change benefit is still empirical; missing monitor/replay source, four-game raw CSVs and primary visuals/supplement are concrete coverage gaps. The next stronger independent route is contemporary change/adoption practice, using retained SC168 offset20 and the2026 postmortem extension10.2139/ssrn.7124688. Reuse the completed professional/runtime methods and preserve other temporal/type frontiers. No full-paper increment, theme closure or experiment follows.

## Operational change includes the support needed to keep working — S266/S267,2026-10-05 HKT

[S267](full-reading/S267-ubisoft-change-propagation.md) connects architecture to a real change in infrastructure serving game production. Its reported replication slowdown/recovery and unexpected backup improvement are useful adverse and positive evidence. The intervention also includes spare capacity, temporarily retained infrastructure, traffic diversion and an agreement about who absorbs cost discrepancies. For Nu, a credible benefit account should therefore include integration, retained service and recovery work alongside source edits and frame costs. This is a scope implication from one situated case, not a general causal benefit estimate.

The complete author edition closes that selected method/figure gap. The final published PDF and underlying case packet remain unverified. [S266](full-reading/S266-postmortem-extension-access.md) is a different residual: its abstract reports a larger postmortem corpus and shifted problem distributions, but the new source mix and coding/AI-curation methods are unread. It cannot yet revise the established S250/S251 release account or establish changed industry prevalence.

SC189 covers the retained search’s positions21–40; the remaining179-result set is not exhausted. The next consequential discovery check is W633’s *The Consolidation of Game Software Engineering: A Systematic Literature Review of Software Engineering for Industry-scale Computer Games*, followed by relevant original methods. Team-premortem and studio-ethnography leads, S266 access, temporal/type obligations and generation access remain independent continuations. Current full-work coverage229does not close a theme or authorize an experiment.

## Industry-scale coverage identifies a closer architectural comparison — S268,2026-10-05 HKT

[S268](full-reading/S268-industry-scale-game-software-review.md) supplies a reconstructible98-study review with broad architectural and empirical coverage. Its original workbook confirms the principal selection flow and68empirical/29descriptive/1exploratory coding, with38case studies,19surveys and11experiments inside the empirical group. This is useful positive evidence of a substantial research base. The commercial/industry-scale screen,2009–2021window and exclusions for academic prototypes and selected neighboring domains also explain why this review cannot delimit all Nu-relevant prior art.

| Affected theme | Discovery and primary understanding | Evidence disposition and next action |
| --- | --- | --- |
| B05 game alternatives; B11 architectural choice | Complete review/appendix and original coding now locate economy architectures, conformance/MVC evolution, cross-engine reuse and consistency methods. Their underlying bodies are not newly read. | Follow Unlimited Rulebook's original claimed implementation/maintenance comparison. Compare its task/outcome/integration boundary with Nu and S225; do not import an effect from a review label. |
| B10 practice |98selected publication identities and24older selected coding records are screened. SC194adds a capped forward-citation map; current practice remains partly outside the review's dates. | Retain the positive breadth of situated evidence. More case-study publications do not directly measure adoption or a shrinking industry-academia gap. Continue consequential team/studio/indie leads where they can change the practice account. |
| B12 methods | All25pages/eight figures/seven tables read;98quality totals and selected aggregate arithmetic reconstructed from the released workbook. | Preserve main counts and mean/SD alongside percentage, Q5/Q6and edition differences. Reporting quality, industrial relevance, method labels and causal benefit are separate. The older/newer comparison overlaps in2009and at least one publication. |

B01–B04andB06–B09retain the source-located dispositions and primary/access gaps in the map above. The review's requirements, testing, runtime and live-development neighbors are discovery leads; this pass adds no direct type-feedback, temporal-preservation, agent or Nu effect. Its sparse maintenance category does not establish scientific absence. SC194's *Use and misuse of case studies and experiments in Game Software Engineering* is a retained title-only method lead, while W639's BDD study is a retained testing lead. Neither supersedes the stronger immediate architectural comparison merely by being newer.


## Rulebook localizes economy changes, with mixed preliminary effort evidence — S269, 2026-10-05 HKT

[S269](full-reading/S269-unlimited-rulebook-architecture.md) supplies a close game-architecture alternative: economy state sits behind rule dispatch, while feature patches add or override behavior through predicates, precedence and composition. The complete author edition and selected public code support this mechanism. Its card examples show useful local extensions, and the course report preserves slightly fewer architecture changes and strong willingness to reuse the approach.

The same primary report finds implementation effort and perceived usefulness inconclusive. Genre order is split, but all teams use free design first and Rulebook second; period, deadlines and architecture are therefore not separated. Initial implementation effort is excluded because the substrate is supplied. The authors also identify nested conflict resolution as a runtime concern. These are concrete limits on a net-cost inference, not grounds to discard the positive experience or treat inconclusiveness as equivalence.

Source inspection separates a design contract from enforcement: mutable property tables, publicly accessible records and shared predicate/implementation closures do not guarantee read-only predicates or safe migration. The example’s pinned older prototype differs from the current inspected Lua code only in comments within the changed Lua files; the full course binary remains unbound. The paper’s simplified damage update and released accumulating rule remain separate examples. No author code is executed.

For B03–B05/B11–B12, compare this mechanism with S225’s explicit live deltas and pool resets, and with Nu’s actual host/state obligations. General novelty in separated economy rules is narrowed; Nu’s net maintenance value and preservation behavior remain unresolved empirical questions. The later Rulebook publication and thesis are now consequential primary-reading gaps because they may change the mechanism and evaluation account. S268’s industry-scale eligibility label does not convert these student courses into industrial comparisons. No theme or whole-survey completion follows.


## Effects, previews and observed adoption costs — S270, 2026-10-05 HKT

[S270](full-reading/S270-rulebook-effects-and-jam-games.md) refines the earlier Rulebook into effect objects processed by active rules. Its Amend–Resolve–Chain convention can expose an amended effect for preview before state resolution. The three jam games demonstrate useful variants: per-entity component dispatch, centralized type-based dispatch and a modifier/application split used to display action costs. This strengthens the Nu-relevant precedent for separating requested operations, current-rule interpretation and committed state changes.

The reported experience preserves both gains and costs. Legend of Slime delivers varied puzzle mechanics with duplicated pairwise power rules; Dungeon Architect supports cross-room interactions and reported time for polish; Honey BZZZness gains useful previews while learning and state access contribute to delays and omitted features. Selection among sufficiently finished author-participated games, one engine family and absent controlled time data bound these observations. The paper's 4–15 central implementation lines are a narrow code boundary, not a total adoption-cost estimate or reversal of prior E/H compactness evidence.

Bounded source reading verifies the preview and dispatch mechanisms without extending their contract. Grimoire preview processes linked effects without its resolution phase; Honey preview shares amendment rules with execution, but click handling creates a fresh effect under then-current state. Within-phase dependencies and pending timers remain explicit obligations. The three jam cases do not implement the complete proposed effect-stream/chaining mechanism. Neither a phase diagram nor a successful local extension proves preserved history, arbitrary migration or external-effect rollback.

The consolidated mechanism/cost comparison now includes S269/S270 alongside S225, Casanova, SGL and ECS. Read the original thesis next for the still-unread detailed course evidence, interviews and requirement/iteration account. This is a source-located primary gap; another search page cannot resolve unknown Nu-specific empirical value. All construction and execution holds remain.

## Original Rulebook evidence and the comparison boundary — S271, 2026-10-05 HKT

[S271](full-reading/S271-rulebook-thesis-and-methods.md) closes the original-method gap behind S269/S270. Its three iterations show a substantive design response to adoption friction: the later architecture permits Direct Access and effect/entity-based Rule Fields. The course’s randomized teams and genre allocation coexist with a fixed ad hoc-then-Rulebook treatment order. Difficulty, helpfulness and change frequency are self-reports; slightly lower reported change burden and useful predicate/rule reuse remain favorable evidence, while net effort is unresolved.

The four professional interviews concern existing games, rather than Rulebook deployment. The 33 requirements provide a broad comparison of mechanics, runtime lifecycle, communication, tooling and evolution, with interpretive provenance. Grimoire supplies implemented reusable properties/rules and previews alongside editor/UI propagation, author-reported dispatch performance problems and recursive preview failure. These concrete costs are part of the architectural account, not reasons to discard its successful changes.

For Nu, compare the actual change boundary, extension vocabulary, current-state/pending-work contract and whole integration burden. A stable save checkpoint does not establish arbitrary live schema migration; a preview does not reserve future state. The conference, thesis and journal reuse some empirical cases, so publication count must not become replication count. Next read the independent MVC architecture-evolution/evaluation route; retained method/practice/access and temporal/type frontiers remain open. No construction or execution is authorized.

## Architecture and exploration access boundary — S272–S274, 2026-10-05 HKT

The independent MVC/conformance route remains consequential, but its checked primary routes do not yet supply the methods. S272’s five-project refactoring/quality account and S273’s violation-reduction account therefore remain abstract/prefix evidence. SuBViS locates graph/node alternatives in Unreal Blueprints, while its study and state/copy/merge semantics remain unread. These are specific primary-understanding gaps; they do not weaken the existence of these predecessors or establish an empirical null.

The related BPAlt paper reports a ten-participant comparison in its publisher abstract. Reading its primary method can clarify whether the outcome concerns perceived support, exploration behavior, completed changes or total effort, and what managing alternatives does to live state and host integration. It remains distinct from SuBViS until primary lineage is established. Continue that accessible route or an independent architecture/method frontier; no experiment follows from acquisition.

## Blueprint alternatives: situated positive evidence, unresolved primary method — S275

[BPAlt’s publisher preview](full-reading/S275-bpalt-partial-method.md) reports a higher creativity-support score and unanimous preference in a ten-person comparison. This is useful positive evidence for managing exploratory alternatives. Complete tasks/allocation, state/copy/merge semantics, outcome tables and integration costs remain unread; the reported score does not establish a maintenance-effort or live-migration effect. The preview’s F/df and partial-effect-size values are inconsistent, without determining which is wrong.

Continue the already retained evaluation-method review through its OA route to inspect how it classifies studies and uses their evidence. Exact MVC/conformance, SuBViS and BPAlt access gaps remain; shifting to accessible consequential work does not close them or resolve Nu-specific value.

## Empirical method names do not measure architecture value — S276

[S276](full-reading/S276-game-software-evaluation-methods.md) distinguishes real-context observation, researcher-led change, archived evidence and constructed evaluations. These can all support useful claims when the unit, intervention and outcome are explicit. Its own stated experiment definition separates manipulation/control/allocation from additional reporting and replication attributes. Four displayed studies meet the first three, while two meet all seven. A checklist-completeness rate is not a field-wide rate of valid experiments or a benefit estimate.

The manuscript’s coding pilot and split remainder, missing case-table rows, reference mismatch and unexplained omission from S268’s workbook constrain its headline percentages. Its adverse screening result remains informative: the interview-word indicator misses the sole reported case and has zero recall. Preserve that result and practical guidance without erasing the earlier studies’ favorable, null or adverse outcomes. The complete selected author method is read; original coding notes and final-body correspondence remain separate gaps.

For Nu, the comparison still needs an explicit change/preservation contract, independent outcome/oracle and complete integration-cost boundary. A live demonstration can establish a mechanism without establishing a professional maintenance effect. The omitted runtime-repair source (10.1109/MS.2011.87) is a consequential independent continuation, not a replacement selected to obtain a favorable result.

## Runtime recovery needs an observation and repair contract — S277/S278

[S277/S278](full-reading/S277-S278-mayet-runtime-repair.md) now resolves the selected primary method after ordinary author-route recovery. The event monitor, temporal rule and host repair operation are distinct. The same game demonstrates selected recovery with seeded faults and on/off controls; the rule engine does not directly mutate game state. That is useful mechanism evidence across a shared publication lineage.

The repair can arrive after the observed state has changed. Choosing whether to apply, delay or ignore it is host policy; a successful local correction does not prove other behavior is preserved. The authors acknowledge possible repair loops and harmful repairs, and report no commercial-scale evaluation. Their short rule examples, qualitative frame lag and presentation claims do not measure total engineering benefit. Preserve this positive mechanism with its actual obligations.

For Nu, compare the observation vocabulary, pending temporal facts, application point, stale-message policy and whole integration cost. A new paper count does not create independent cases. Follow the retained later game-monitoring lineage for its fault population, real temporal checks and measured overhead, while preserving the other thematic/access frontiers. No construction, recruitment, author-code/model execution or new worker is authorized.

## A visible snapshot is a specified observation — S279/S280

[S279/S280](full-reading/S279-S280-game-runtime-monitoring.md) adds a useful game-monitoring alternative: separate selected-state export, temporal checking and tester action. The conference evaluation reports successful detection in seeded games and three historical Bos Wars cases with low measured processing costs. It does not compare tester time or whole maintenance effort. The later six-game journal body is still unread, so it adds neither validated method detail nor independent cases.

The inspected public revision illustrates why the observation contract matters to Nu: it suppresses empty-state messages, loses velocity sign in exported magnitudes, and retains inconclusive temporal verdicts. Its hard-coded template, CPU counters and GUI fields also differ from the paper’s described setup. These are bounded source/version findings; they do not erase the reported feasibility results or reproduce their measurements. Omitted temporal formulas and end-of-level treatment make the linked thesis a consequential next source. Original visuals, final journal understanding and unknown empirical transfer remain distinct gaps.


## Monitoring feasibility includes a commercial case — S281

[The complete thesis](full-reading/S281-game-monitoring-thesis.md) establishes a stronger applicability account than the conference roster alone: BlooBuzz’s commercial Unity game is included, with fixed historical bugs deliberately reintroduced. Mario/Pyramid embed the monitor and emit action events; Pingus/Bos Wars export snapshots to an external process. Three games overlap the conference. Preserve successful selected checking and modest reported overhead as scoped positive evidence.

The thesis explicitly allows inconclusive verdicts, while exact end-of-level policy for the conference’s omitted eventual property remains unknown. Printed identity/Until qualifications and the unresolved Bos Wars tracker number prevent silently equating intent, formula, executable and historical fault. Embedded-case overhead includes monitoring; external-case overhead excludes it. Neither the table nor the number of demonstrations measures net maintenance benefit or a language effect.

This closes a consequential primary-reading gap without closing an empirical Nu question. NCAlt now offers a stronger independent continuation for alternative comparison and state/evaluation semantics. The2013 predecessor remains conditional on a specific missing method claim; journal/visual/version, practice, architecture and type-evolution gaps remain open. No experiment or worker is authorized.


## Alternatives access and an accessible collaboration method — S282

[NCAlt](full-reading/S282-ncalt-access.md) is directly relevant to comparing design alternatives. Its positive abstract reports higher SUS and favorable qualitative follow-up; the31-page primary method remains unavailable through publisher, supplied institutional, author and public-code routes. That access result neither refutes its benefits nor establishes the switch/reset semantics. A misassigned mechanical Bolt DOI is removed from the software lineage. Broad acronym noise is recorded as a retrieval limitation.

NCCollab is the strongest accessible adjacent continuation because its collaboration/history and logged task-time methods can connect an implemented editing mechanism to an observed outcome. Its native record predates reading, and PMC's public dataset supplies the38-page published PDF and video. Treat the shared author/tool lineage explicitly and preserve the distinct alternatives and collaboration treatments. This does not close a theme or reopen experiments.


## Collaborative authoring has a scoped measured benefit — S283

[NCCollab's complete paper](full-reading/S283-nccollab-collaboration-history.md) strengthens the connection from an interactive editing mechanism to an observed outcome. In twelve participants arranged as six pairs, collaborative task completion averages16.25/17.57minutes versus21.32alone. This is positive elapsed-time evidence for an implemented collaboration bundle. It is not an isolated history/preview effect or total-labor saving. Overall CSI rises, while its non-collaboration factor tests and the Async–Sync time/CSI contrasts are null. Preserve the authors' collaboration-based interpretation and reported coordination/interface difficulties.

The method saves and restores BT documents; it does not specify migration of ongoing game-world state. Live preview concerns another editor's tree while the local scene runs local behavior. Removing a conflict notification can hide an unresolved underlying difference. These findings narrow what a Nu comparison must identify, without denying the demonstrated workflow value. NCAlt's separate alternatives evaluation remains access-limited. LevelMerge is the next primary route for actual graph merge and identity obligations; its evaluation should be read directly rather than inferred from NCCollab's characterization.

The B01–B12 map now reuses the completed monitoring thesis in B06/B08/B09 instead of leaving stale read-the-thesis actions, and places document history with B04/B08. Remaining empirical uncertainty is kept separate from precise raw-data, edition, visual and body-access gaps. Neither this reconciliation nor238full readings certifies the entire survey or authorizes experiments.


## Dependency-aware scene merging is an evaluated alternative — S284

[LevelMerge’s complete selected preprint](full-reading/S284-levelmerge-scene-merge.md) connects a graph representation to an integration operation and an observed outcome. Unique IDs and direct/indirect dependencies support three-way merging, conflict handling and cycle removal. Four selected scenes remain playable after merging; a small comparative study reports favorable failure-sensitive difficulty ratings against Git text merging. Keep this evidence, including deliberately conflict-prone tasks, participant-count discrepancies and missing raw denominators. “No formal evaluation” in NCCollab is not a sound basis for erasing the primary comparison.

The integration boundary is concrete: serialized scenes are rewritten/reloaded; synchronization stops during play. Preferred-branch choices or cycle removal can discard edits/dependencies. Compilation and graph consistency are useful checks, but do not establish preservation of an ongoing runtime or every gameplay obligation. The 2016 preprint is complete, while the final 2018 edition and video remain unacquired; DOI-indexed text is not sufficient to erase that version gap. SceneGit is the next primary method for practical matching and merge policy, with NodeGit conditional. Unknown Nu-specific benefit remains an empirical question, not something additional citation pages can settle. No theme or experiment is closed/opened merely by this checkpoint.

## SceneGit access and the next available graph method — S285,2026-10-08 HKT

[SceneGit](full-reading/S285-scenegit-access.md) reports favorable large-scene speed/robustness and collaboration outcomes, but only its1100-character abstract is available through the checked routes. Preserve those claims without inventing the matching algorithm, merge policy or comparative procedure. Scite/OpenAlex access flags do not override the actual abstract-only response, restricted institutional file or repository with no files. The gap is unread primary evidence, not an established null result.

The author-linked NodeGit repository supplies an available next method route: after native registration, bind a commit and reconstruct graph matching, diff and merge by static inspection while seeking the paper/evaluation. Code availability alone does not establish its experimental results. VRGit’s author PDF is a conditional next route for collaborative change outcomes. B04/B05/B08 now distinguish these actions from blocked SceneGit acquisition; the other thematic frontiers and unknown Nu-specific empirical value remain. The complete-reading total stays239 and all experimental holds remain.

## Inferred identity makes integration policy consequential — S286, 2026-10-08 HKT

[NodeGit’s selected source](full-reading/S286-nodegit-source-and-access.md) closes a concrete mechanism gap despite unavailable paper text. The Blender importer generates fresh IDs; greedy matching uses type counts, property changes and already inferred references. Diffs translate correspondence back to ancestor IDs. This supplies an alternative to requiring stable imported IDs, with an explicit fixed-property-set premise and domain-specific adapter.

The merge core combines nonoverlapping edits and equal changes, reports local delete/edit or competing-value conflicts, and otherwise applies both diffs to the ancestor. It does not provide a cross-object behavior or running-state oracle. The documented dangling-reference case is a static control-flow inference, not an executed failure or an estimate of real-world frequency. Preserve the paper’s favorable manual/randomized-edit reliability claim at abstract scope; exact metrics and comparative results remain an access gap.

The B02/B04/B05/B08 map now distinguishes reconstructed source contracts from unread evaluation. VRGit’s available author paper is the next route for how version/history/merge tools affect collaborative outcomes. Nu-specific net value, broader practice and temporal/type questions remain open; full-reading credit stays239 and no experiment is authorized.

## VRGit: useful history interaction and the professional-practice gap

[S287 VRGit](full-reading/S287-vrgit-history-and-collaboration.md) completes the author paper and original visuals. Its operation DAG, summarized miniature history and selective object reuse support an editor workflow different from whole-branch graph merging. Fourteen participants completed instructed individual/collaborative tasks, with high usefulness ratings and reported controller, long-history and sharing-control difficulties. Preserve those findings as exploratory usability evidence: the study does not assign a control condition, measure net maintenance savings or certify concurrent correctness. The video remains unread.

The professional workflow gap selected from VRGit’s references is now reconstructed as [S288](full-reading/S288-collaborative-arvr-practice.md). Its26 interviews supply the role/tool handoff account below; they do not turn VRGit’s usability findings into a professional maintenance-effect estimate. Ashtari’s earlier practice study, modern CAD version-control practice, Spacetime and FlowMatic retain conditional relevance. This reorders the accessible continuation without closing any B01–B12 theme or reopening an experiment.

## Professional practice: the change crosses people and tools

[S288](full-reading/S288-collaborative-arvr-practice.md) reconstructs professional collaborative AR/VR development through26 interviews. Participants describe useful shared prototypes, early feasibility discussion and mutual training, alongside tool/skill translation, limited device access and maintenance burdens when rushed prototypes become products. Coding a layout can make it harder for a non-programming designer to edit; a fast local implementation can therefore move work elsewhere. The evidence is qualitative and situated, without an assigned comparison or measured Nu effect.

For Nu, connect the mechanism to a change completed across the relevant roles and tools. Include who can inspect and edit a representation, the intended spatial/temporal behavior, learning and integration work, and later refactoring. Shared understanding and visible prototypes do not certify behavioral obligations. The immediate continuation is McKenzie et al.’s2019 game-industry practice method, with its later2021 lineage checked if consequential; this directly tests the transfer of the practice account to game teams. DART’s ten-year adoption account and Ashtari/Musil remain conditional. Access/version gaps and B01–B12 coverage remain open; no experiment follows.

## Reported practices, useful adaptations and the value boundary

[S289/S290](full-reading/S289-S290-game-practice-methods-partial.md) reconstructs the selected game-studio survey and interview methods from complete returned indexed text. At that indexed-reading checkpoint, original figures/PDF bytes were unavailable and neither received a complete-publication increment. The supplied-PDF completions below now resolve those gaps. The studies distinguish claimed frameworks from reported activities and document adaptations for different kinds of work. Preserve those useful accounts and continuing difficulties without treating adherence, a framework name or linked publications as a causal benefit or independent replication. The map above now prioritizes the remaining resource/stage method rather than another automatic practice citation.

## Interaction types provide reuse with a specific diagnostic boundary — 2026-10-08

[S298](full-reading/S298-interaction-typing.md) supplies complete HAL-v2 manuscript/visual coverage and ten pinned companion/source files. Separating interaction behavior from exposed data permits useful substitution and composition in a TypeScript API. The same interaction-data object is updated during execution and cleared afterward; this is a different contract from immutable world history or live-state migration. No controlled completed-change benefit or total integration-cost estimate is reported.

Data typing uses the host compiler, while the described conflict checks run dynamically and omit binders with custom predicates. The companion points to v8.0.0; that selected release defaults all checks to ignore, uses exact widget-set intersection and a fixed name-based inclusion map. It does not establish the paper’s broader ancestor/bubbling and timing analysis. These are version-specific static findings, not executed failures or a verdict on the current library. The positive substitution mechanism and narrower diagnostic coverage both belong in the Nu comparison.

The retained-route audit now selects S299 for modular replacement/whole-system correctness and S300 for the distinction between comprehension and modification performance. At that selection checkpoint, both had verified native PDFs but unread methods, and [S301](full-reading/S301-modularity-rule-maintenance-access.md) was abstract-only behind a precise access gap. Subsequent readings below resolve all three selected primary bodies. This moves the work toward a claim-based synthesis without treating another acquisition, page or paper count as completion. Experimental and worker holds remain.

## A local replacement requires an explicit preservation contract — S299, 2026-10-08

[S299](full-reading/S299-modular-reactive-verification.md) supplies a positive formal alternative: contract a module to its derived action, then verify a replacement whose behavioral model entails the old one and whose relevant exit conditions agree. The selected controller is memoryless during each decision, with stable current input while selection is computed. LTL guarantees depend on valid action/world models; the illustrative drone also assumes eventual permanently favorable conditions. Reported counterexamples reject two plausible designs before successful whole-controller and local-replacement checks.

This resolves the selected formal-composition method without measuring developer benefit. A changed module can encompass the entire controller; no scaling/time comparison is reported. Unreachable return arcs can lower structural complexity without changing actual behavior. Exact example encoding and final publisher correspondence remain unbound. For Nu, compare explicit preservation obligations with Ceptre’s resource/stage semantics and S298’s data/diagnostic boundary. S300 below resolves the selected empirical dependency. All experimental holds remain.

## Comprehension is a task-dependent intermediate outcome — S300, 2026-10-08

[S300](full-reading/S300-cognitive-fit-and-modification.md) supplies professional evidence for both sides of the proposed comprehension-to-change link. Twenty-four COBOL maintainers perform one enhancement in each of two programs, with function versus control-flow task type randomly assigned and domain/order controls recorded. In the two predicted cognitive-fit conditions, comprehension gain correlates positively with modification progress (+.52, +.49); in the two mismatch conditions it correlates negatively (−.35, −.30). The reported three-way interaction is significant (p = .007), with a consistent rank-based analysis. These are task-dependent associations, not four separately established treatment effects or a uniform mean advantage for fit.

The modification period is fixed at 35 minutes. Progress earns partial credit, including up to 75% of a subtask's points for handwritten work not entered into the program; some record-format changes are supplied in advance. This is useful measured progress, distinct from time to independently verified completion. Comprehension gain occurs during the same modification activity and is measured, not randomized. For Nu, keep representation, understanding, progress, retained/new behavior and total effort separate. A later comparison must retain all assigned attempts and cannot identify a pure mechanism effect merely by adjusting for achieved comprehension. No experiment is started.

## Supplied primary evidence resolves the rule-maintenance experiment — S301, 2026-10-08

[S301](full-reading/S301-modularity-rule-maintenance-access.md) now supplies complete original methods and outcomes. Grouped rule documentation and explicit produced/used interfaces improve elapsed time in one graduate-student experiment and correctness/structure scores in a second novice experiment. This is positive evidence about a concrete information/organization intervention, distinct from software-enforced encapsulation. The two samples do not supply one combined verified-completion-time result or a Nu benefit estimate. The access gap is resolved; raw records and the printed quality-score discrepancy remain explicit. The accompanying S289/S290 supplied-PDF completions and the current coverage map incorporate the new visual and method evidence.

## Practice labels, reported actions and outcomes — S289 PDF completion, 2026-10-08

[S289](full-reading/S289-S290-game-practice-methods-partial.md) now has full publication and figure coverage. The ten plotted perception scores exceed questionnaire-derived Scrum adherence, while the response matrices expose ambiguous blanks and a difference between reporting a review and supplying its details. Effort categories are estimates; reported use of an on-time-shipping metric is not an on-time delivery rate. This strengthens the source basis for separating declared methods, available information, actual practice and outcomes. It does not establish that conformity causes better game development or that a Nu workflow saves effort.

## Adaptation, collaboration and the outcome boundary — S290 PDF completion, 2026-10-08

[S290](full-reading/S289-S290-game-practice-methods-partial.md) now has complete publisher-edition coverage: twelve pages, Figure 1, Table I and fifty references. Eight leaders describe useful combinations of iterative feature work, continuous assets/fixes, milestones and hybrid roles. The figure is a synthesis with illustrative milestones, not a measured delivery schedule. Table I preserves countercases: studios with retrospectives, action on issues and Scrum Masters still report knowledge silos/shared-understanding problems; a Scrumban studio reports solving communication problems through colocation and chat. The qualitative checks strengthen the account without establishing a causal training or adherence effect.

For Nu, useful differentiation should be connected to the work enabled for particular roles and phases, and to total change, integration and coordination costs. S289’s labels/adherence/metric-use distinctions and S290’s adaptations support that boundary; neither supplies a Nu benefit estimate. Their former original-visual/file gaps are resolved, while raw instruments, participant overlap and accepted/publisher byte equivalence remain explicit. This updates B01/B08/B10/B11/B12 without changing the scientific-choice or experimental holds.

## Broad research preparation and information-dependent debugging — 2026-10-08

The user requests preparation across plausible directions, prioritized by research value, with literature continuing where needed. The [agenda](../nu-research-agenda-2026-10-08.md) provides twenty direction cards, each with a comparison, outcome, rival explanation or inference boundary, next preparation and condition for redirecting. Whole-workflow value ranks highest for the adoption decision. Coordination and debugging offer more concrete smaller comparisons; correctness, runtime cost and situated practice evidence support their interpretation. Learning, agents, sequences, live editing, collaboration, reuse and composition remain substantial directions. Prospective selection, language transfer, integration, distributed state, energy and expressive reach have explicit promotion conditions. These rankings are maintainer judgments, not estimated effects or experimental allocations.

The completed [S42](full-reading/S42-stream-debugger-comparison.md) resolves a consequential queued method. Its twenty-professional repeated-measures comparison favors the stream-plus-debugger package overall, while loops with stepwise debugging are faster when the failing object is known. All thirteen publication pages and nine selected artifact files are read. Generated test agreement, timing callbacks, remaining raw-data/build gaps and printed statistical inconsistencies are reconstructed without erasing the positive result or reversal. B01/B08/B12 now retain initial information as a concrete condition of benefit, package attribution and the distinction between supplied-test completion and independent behavioral correctness.

SC245–SC250 broaden selected adoption/usability and distributed-state discovery and extend the practice query through positions 81–100; one request fails and five return twenty records each. All returned titles and available abstract prefixes are screened, with primary-method credit only where separately recorded. The engine-API usability abstract (DOI 10.1002/spe.2985) describes structural metrics, so human productivity remains a separate outcome. Rollback/CRDT leads remain conditional on a real Nu distributed-state capability and use case; matching preprint/conference titles do not establish independent studies or exact edition equivalence. Later pages remain open. The [ledger](nu-background-searches-2026-09-30.md) owns exact routes and considered-source decisions.

Continue with source-grounded comparison and outcome specifications for the leading directions, retaining the whole agenda and its B01–B12 mapping. S38's acquired usability framework becomes consequential if adopted as a measure; S227 v2, S263/S264 and S266 remain dependencies of the specific methods/claims that need them. This prepares concrete scientific decisions without requiring a single-direction choice first or starting an experiment.


## Nu source and practice contracts refine the leading designs ? 2026-10-11

The [source audit](../nu-source-contracts-and-scenarios-2026-10-11.md) separates a useful implemented capability from correct continuation and measured maintenance value. Public #1145 history supplies a concrete transition/pause failure and a traced workaround inherited by ImSim Breakout. Gaia snapshots represented gameplay as well as editor operations in functional mode; restoring the root rebuilds selected-screen spatial/physics state. This improves source understanding without claiming universal immutability, arbitrary process rollback, a new empirical result or novelty.

| Themes | Discovery coverage | Primary/source understanding and gap | Evidence disposition | Next consequential action |
| --- | --- | --- | --- | --- |
| B03/B07/B10: ownership and coordination | Five bounded GitHub issue searches, 47 positions / 45 unique issues; #1145 patch lineage followed. These do not estimate task prevalence. | Selected owners, frame phases, message/result consumption and subscription lifetime traced. Required initial parity and a diverse task portfolio remain unvalidated. | Real practice motivation and source semantics; local control is an authored task and pause/exit an adaptation. A fixed historical issue is not an eligible new repair at this pin. | Select legitimate assigned changes and required old/new observations; keep package attribution and broader task provenance. |
| B04/B08/B09: history and access | Pinned code plus selected public mutable-state/undo reports; no new paper or agent-interface probe. | Root retention, shared objects, pending callbacks, physics rebuild and editor access paths inspected. User-data safety, exact native continuation and agent transport remain conditional. | Source-supported represented-gameplay recovery, not arbitrary host-effect rollback or demonstrated agent productivity. S42/S296/S297 remain useful scoped methods. | Select a snapshot-safe same-code state/effect boundary and actual permitted access; retain source reload as a separate R10 question. |
| B06/B11/B12: cost and interpretation | Nu/Jolt restore/broad-phase chain and historical allocation/regression reports followed; screenshots uninspected. | Checkpoint/root cost differs from native reconstruction, release and resumed-frame behavior. Upstream fix/dependency-version correspondence remains unaudited. | Concrete cost/obligation hypotheses, including adverse outcomes; no measured current Nu cost, leak or runtime failure. | Keep execution mode fixed for a retention comparison; bind matched useful work and later overhead/resolution checks. R17 can follow the exact native-version dependency if selected. |

The ledger records 75 new source decisions (30 credited, 35 deferred, 10 unused) and the inspected report. No primary-paper reading was added; the 255-work checkpoint remains unchanged. R01 ordinary-engine capability comparison and R04 authentic fallback sites remain independent preparation. The current strongest gaps concern eligible requirements, observation boundaries and later feasibility; adding adjacent papers without changing those decisions would not supply missing Nu measurements. All construction, worker, participant and experiment holds remain in force.

## Comparator and source-convention refinement, 2026-10-11

The subsequent [R01/R04 audit](../nu-comparator-and-convention-audit-2026-10-11.md) resolves those independent source-preparation steps at a bounded scope. The [ledger](nu-background-searches-2026-09-30.md#2026-10-11--ordinary-godot-and-the-d1-source-convention) preserves two web queries, all 13 displayed search hits, exact code/documentation pins, selected reading ranges and source dispositions. It adds no full-paper credit, Zotero change, empirical Nu result or execution authority.

| Theme and decision | Discovery coverage | Primary understanding and gaps | Evidence disposition | Next consequential action |
| --- | --- | --- | --- | --- |
| B01/B04/B08/B11: credible ordinary workflow | Official stable-release metadata plus independently pinned Godot 4.7 tutorial and engine class/source routes. Release-heavy search output was replaced by exact primary retrieval. | Inspection, live synchronization, programmable undo, copying and diagnostic snapshots are documented. Images/demos, C# reload implementation and current research-plugin compatibility remain uninspected. | A capable ordinary Godot/GDScript package is a credible R01 candidate. Its tools do not by themselves establish full gameplay restoration, just as Nu roots do not establish arbitrary process rollback. | Select an authentic application and common promised outcome; include ordinary tools and total integration/recovery work. Follow C#/plugin dependencies only if selected. |
| B03/B07: pause and lifecycle | Selected Node/Object/SceneTree entries and full pause-tutorial text inspected at declared pins. | Signal delivery, timer defaults, deferred calls and scene replacement need distinct observation boundaries. No engine session exercised them. | Native facilities can express a credible coordinated alternative; source timing rules do not prove a completed task correct. | Bind common requirements to each engine's allowed schedule and validate under separate construction authority. |
| B02/B07/B09/B12: source convention and diagnostics | Existing D1 match revisited for a material policy/task question; new project/CI records read. All tracked Nu paths screened for SDK/parent-build configuration names. | Shared fallback has a source-equivalence argument; FS0025 is not explicitly an error in checked-in settings. Effective inherited properties, compiler version and actual output remain unprobed. | A legitimate proposed convention contrast and three authored requirement sketches, not an observed warning, behavioral effect or representative task set. | Extend task provenance; freeze and later validate common toolchain/equivalence/diagnostic/observation contracts. Keep default-correct and compiler-silent obligations. |
| B06/B11/B12: cost and measurement | Selected UndoRedo implementation plus ordinary timing and ObjectDB documentation read. | Action eviction and retained values/targets differ from Nu root retention and native reconstruction; profiler overhead and partial native-memory coverage are explicit. | Concrete competing mechanisms and accounting boundaries; no measured ranking or total-cost advantage. | Apply R06's matched-useful-work and full managed/native boundary to the selected outcome, preserving adverse cases. |

The source segment records 37 new decisions (22 credited, 3 deferred, 12 unused) with an inspected, untruncated citation report and no missing reasons. Unchanged historical sources were not screened again. Current passive priorities are eligible applications/common requirements, credible task diversity, R03's selected snapshot-safe subset and the independent R17 dependency-version audit. Actual agent access, runtime/oracle validation and all experiments remain held. The broad survey's named source/edition/access gaps and future steering question remain as recorded; this comparator inventory does not close them.

## Native dependency and recovery refinement, 2026-10-11

The subsequent [Nu/Jolt dependency audit](../nu-jolt-dependency-audit-2026-10-11.md) follows the R17 lead through actual package metadata, archived bytes, wrapper source and upstream fix history. The [ledger](nu-background-searches-2026-09-30.md#2026-10-11--nu-jolt-package-and-upstream-fix-lineage) records all 25 new/material decisions and the exact remaining boundary. This is passive artifact/source understanding, with no new paper reading, library mutation or runtime execution.

| Theme and decision | Discovery coverage | Primary understanding and gaps | Evidence disposition | Next consequential action |
| --- | --- | --- | --- | --- |
| B04/B06/B11: recovery across a native dependency | Nu declaration, managed/native nuspecs, native package, 253-path wrapper tree, five-entry binary-history prefix and Jolt #1525's four-file patch followed. Earlier history and native build attestations remain outside inspected coverage. | All ten packaged binaries match vendored wrapper objects. The native repository/commit pair fails to resolve; exact joltc/Jolt compilation provenance and actual loaded artifacts remain unverified. | Verified package-content identity and upstream fix/source ancestry. Inclusion in packaged C++ code is a qualified inference, not a current-runtime verdict. | Preserve the exact build gap if native semantics become central; independently select R03's application/state/effect subset. |
| B03/B06/B07/B12: native maintenance and resumed behavior | Selected positive-time integration, clear/counter and binding paths inspected; whole-file batch-name searches recorded. | Nu does not call native Update at zero time, retains thresholded optimization and keeps the counter across the inspected clear operation. Searched batch-add declarations are absent in the pinned binding files. | A concrete cross-layer integration case; cumulative creation differs from live population. No current bug, measurable stall or useful-effect estimate follows. | Apply R03/R06's correctness/cost contract to the selected application; verify actual binding route before proposing batching as an available control. Later behavior/overhead checks remain held. |

The inspected report confirms 18 credited / 4 deferred / 3 unused decisions, zero malformed entries or missing reasons and no truncation. Reused issue/literature findings were not given new reading credit. R17 remains conditional on a consequential integration outcome; its source complexity does not itself justify promotion above the leading studies. Accessible independent work continues on eligible applications, credible requirements and snapshot-safe state/effect boundaries. The broad survey and future steering design retain their existing limits and authority.

## Selected history application, 2026-10-11

The [MMCC/Gaia contract](../nu-history-application-contract-2026-10-11.md) selects a first R03 technical application and distinguishes immediate B0 model recovery from B1 continued behavior. The inspected model records/maps, content projection and in-process accessors make the subset concrete; the standalone imperative default, selection-triggered initialization and pre-toggle history mode narrow eligibility. Fresh functional reconstruction must reach the same saved state before cost comparison. Timing configuration, input/focus, future random draws and external effects are separate conditions, not implied rollback capabilities.

B04/B08 now have an application-specific source boundary rather than an unspecified snapshot promise; B06 retains same-mode, full-recovery accounting. Launch, observation phase, input control, model/content correspondence and agent transport remain unverified. Continue credible R02/R04 task diversity and R01 common requirements; this R03 contract next needs separately authorized feasibility. No new publication reading, field-completion judgment, Nu benefit measurement or experimental allocation follows.

## Task provenance and common application requirements, 2026-10-11

The [task-diversity audit](../nu-task-diversity-and-common-requirements-2026-10-11.md) adds Blaze Vector's MMCC/ImSim pair and an authentic projectile-command D1 site. Complete selected application files expose material input, initial-state, gravity, hit-count and lifecycle differences; no equivalent baseline or observed defect is asserted. Three issue-query ranges yield public platform/gravity requests plus qualified character, documentation, mode-switch and historical Elm-interface accounts. These extend B01/B05/B09 practice and source coverage, not representative sampling or publication-reading counts.

R01's ordinary Godot comparator includes shipped character/platform support and explicit departure policies. R02/R04 now have broader source candidates with authored/adapted provenance and a mismatch register. The subsequent platform continuation below resolves the route and common semantics while retaining the need for actual carrying observations; make alignment/setup costs visible. The B04/B08 R03 application boundary and all empirical/access gaps remain. No execution, allocation, human-productivity evidence or field-completion judgment follows.

## 2026-10-11 continuation: platform configuration and observation boundary

The [2D platform contract](../nu-platform-contract-2026-10-11.md) resolves a material R01 source dependency without constructing the comparison. Nu's default 2D route is the managed Box2D.NET port. Character2dDispatcher selects an ordinary dynamic capsule; dedicated character modes need explicit pogo configuration and do not implement the inspected stair-stepping branch. Existing gravity-relative jump/sample code qualifies the old open request. Neither these sources nor a physics API name demonstrates rider carrying.

| Themes | Discovery coverage | Primary understanding | Evidence disposition | Next consequential action |
| --- | --- | --- | --- | --- |
| B01/B05/B09: capability, alternative and practice | Thirteen pinned Nu files plus exact package metadata and selected dependency definitions followed from the public platform/gravity requests; no new literature search or issue sample. | Default backend, ordinary versus dedicated character configuration, gravity/jump routes and existing kinematic motion are source-bound. Exact resolved/loaded package and carrying remain unobserved. | Credible R01 package candidate with authored fixed-gravity carrying/jump/pause/removal semantics and ordinary Godot support. Neither missing Nu capability nor runtime success is established. | Separate feasibility/construction decision on the common scene, behavior and actual tool access. Keep R02's existing pair and alignment cost distinct; a sandbox replacement is not a neutral baseline change. |
| B03/B04/B06/B08/B11/B12: order, state, cost and validation | Selected integration, message, identity, solver, removal and clearing code read; earlier Jolt/history evidence reused without unchanged re-screening. | Integration batch precedes entity-message application; body address/index is not an uninterrupted lifetime certificate. Box2D.NET rebuilds managed physics state; Jolt has a different native boundary. Private support state and prospective observer access remain limits. | Concrete phase/removal hypotheses and cost boundaries, not a demonstrated stale-handle failure, state-replay guarantee or performance result. R03's selected Breakout recovery claim is not expanded. | Later observations must distinguish raw physics, applied state and completed gameplay, preserve missingness and count all integration/rebuild work. No monitor, baseline, candidate or timing run is authorized. |

The upstream mover example at the source-comment revision remains an unread lineage lead; exact algorithm ancestry is not needed for the first ordinary-body contract. Further generic platform searches would not establish Nu's current behavior. Continue a different direction's consequential accessible dependency while the concrete execution decisions remain held. This source continuation changes no paper count, P/A/S identity, B01–B12 overall completion claim, E/H result or human-steering disposition.

## 2026-10-11 continuation: changed-code state preservation

The [R10 source/contract audit](../nu-live-edit-contract-2026-10-11.md) resolves another accessible mechanism dependency. Gaia generates an F# script, replaces its FSI session, updates late bindings and reconciles declared content. This is a real source route, distinct from R03's unchanged-code history and from generic arbitrary state migration. Successful compilation, a reload event and a running scene each remain insufficient to establish retained progress and correct new behavior.

| Themes | Discovery coverage | Primary understanding | Evidence disposition | Next consequential action |
| --- | --- | --- | --- | --- |
| B02/B04/B08: types, state and live tools | Twelve pinned Nu files acquired; eleven have selected/completed text coverage, one unused dispatcher lead has identity-only coverage. Completed S71/S86/S295 notes reused; no new paper/search or full-PDF claim. | Generated-script/FSI boundary, application permission, late-binding names, symbolic model/signal conversion, fallback and initialization gates are source-bound. The full converter schema semantics and actual reload remain unverified. | An existing changed-code workflow and a concrete authored behavior-edit candidate. Conversion fallback can produce a reset model; the reload event also follows the returned compilation-failure branch. No measured preservation, usability or cost result follows. | Separate feasibility/construction decision for a future-brick-reward edit with unchanged model shape, observed progress and matched restart/reconstruction. A schema-changing variant requires its exact mapping/default/converter contract before promotion. |
| B03/B06/B11/B12: reconciliation, costs and validity | Selected subscription, child-matching, plugin/session and failure paths inspected; prior effect/history limits retained. | Declared handlers/children have explicit reconciliation and initialization rules. These do not establish conversion of all captured callbacks, pending work, external effects or cross-version history. | Concrete preservation/failure observations and full-work cost boundary, not a universal transaction or arbitrary hot-reload guarantee. Existing generic migration/schema prior art remains consequential. | Observe installed code and before/after state/effects at named phases; retain failed/partial attempts and session/GC/reconstruction cost. Keep R03, R10 and future R21 claims separate. |

The favorable capability is an implemented source path for changing code and reconciling represented state. The limitations define its useful question rather than erasing that capability or importing another system's effect sizes. Unknown Nu benefit remains empirical; additional generic schema papers cannot substitute for the held observation. No execution, worker, participant, P/A/S identity or E/H result changes.

## 2026-10-11 continuation: package-bound schema correspondence

The [R10 converter continuation](../nu-live-edit-contract-2026-10-11.md#exact-dependency-and-schema-conversion-contract) closes the selected dependency-source gap. Prime 11.5.1's published package matches the local cache; DLL/PDB identities, the specified portable-PDB checksum and six CRLF-normalized source-document hashes bind the inspected commit. No runtime assembly or migration was executed. The package provenance does not close the separate Jolt native-build gap.

| Themes | Discovery coverage | Primary understanding | Evidence disposition | Next consequential action |
| --- | --- | --- | --- | --- |
| B02/B04/B08: schema, identity and live tools | Exact NuGet/package/PDB route to Prime source; selected record/union/default paths and wrapper helpers. Completed S71/S86/S295 reused. Format-spec searches are technical provenance lookups, not new literature coverage. | Gameplay uses named expanded fields; nested Paddle/Ball/Brick records are positional. Missing fields use type defaults; case names and payload positions have different correspondence rules. Application fallback follows deserialization failure, not every semantically wrong conversion. | Positive preservation paths and concrete default/remapping/fallback predictions, with custom-converter and loaded-runtime limits. No observed migration success/failure or productivity effect. | For a schema extension, state the required old/new value mapping and default independently. Then seek separately authorized invariant/phase observations, preserving valid deletion/reset policies as well as failures. |
| B06/B11/B12: costs and claims | Matching package members, PDB records and source hashes inspected passively; current-head/tag discovery was not substituted for the distributed edition. | Converter success, retained meaningful values and application recovery are distinct. Explicit mappings/custom conversion, checks and reconstruction impose work beyond a reload call. | A better bounded correctness/cost question, not generic migration novelty, a reproduced build or a runtime result. | Keep the unchanged-shape R10 case first; promote a schema variant only for a consequential practical decision. R05 must distinguish silent default/remapping from thrown failure and lost observations. |

This continuation resolves selected source understanding rather than replacing missing Nu measurements with more citations. Custom value/resource conversions and any stronger edit class retain their own dependencies. All 21 direction dispositions, execution holds, P/A/S identities and historical E/H evidence remain.

## 2026-10-11 continuation: interaction preservation has a host boundary

The [R13 interaction contract](../nu-interaction-preservation-contract-2026-10-11.md) connects the reconstructed S298/S299 distinctions to the actual Breakout control block. It specifies replacement under an input mapping and extension over a retained legacy subset, with explicit alias priority, capture, clamp and preserved-state/effect requirements. These are authored adaptations, not newly mined requests or independent tasks.

| Themes | Discovery coverage | Primary understanding | Evidence disposition | Next consequential action |
| --- | --- | --- | --- | --- |
| B02/B03/B07: typing and composition | Five pinned Nu source files, selected text; completed S298/S299 reconstructions reused. No new literature search or PDF credit. | The typed MMCC boundary organizes data/callbacks but supplies no clamp, priority or effect predicates. A control block exists; no pluggable input-policy seam or formal module mapping is established. | Useful local structure and explicit preservation obligations. Interacto's data substitution and S299's modeled controller theorem remain distinct prior mechanisms, not automatically provided Nu guarantees. | Use the contract for R02/R05. Promote standalone R13 only for a consequential guarantee or total verification-effort question beyond generic key remapping. |
| B04/B08/B11/B12: host state and claims | Input wrapper, scheduler, screen event and actual update/effect paths inspected at the same source pin. | Keyboard queries ignore World and consult capture/host input. Scheduler flags are captured before later callbacks; the complete MMCC update emits sound and can obtain randomness. | Immutable model return does not establish a pure handler, input snapshot or whole-trace preservation. Local movement correspondence does not erase the MMCC/ImSim package differences. | Specify coherent input, eligibility/phase and permitted effects before later observations. Separate local unchanged-state obligations from legitimate downstream gameplay changes, and count model/observer construction. |

No executable verifier, input sampler, formal model, variant, runtime check or worker was created. The source contract is prepared; its validity in execution and practical benefit remain separate feasibility questions. Keep R03 history, R10 reload and future R21 steering within their existing boundaries.

## 2026-10-11 continuation: requirement lineage and actual inherited histories

The [R09 sequence contract](../nu-change-sequence-contract-2026-10-11.md) resolves its requirement-lineage and failed-predecessor desk dependency. It combines an authored control extension, practice-grounded pause/exit adaptation and authored priority revision. The third stage intentionally supersedes one earlier rule, while the others remain active. This is a reviewable candidate dependency structure, not three mined issues, independent applications or validated tasks.

| Themes | Discovery coverage | Primary understanding | Evidence disposition | Next consequential action |
| --- | --- | --- | --- | --- |
| B09/B11/B12: sequence methods and inference | Completed P04/P05/P06/P09 and existing Nu contracts reused. The linked ChainSWE web/API route was rechecked and still returns 404; no new code or paper body acquired. | Actual inherited, clean-reference and repaired predecessors answer different questions. Source/workspace, installed state, conversation, durable notes and test exposure require separate policies. | These are established comparison patterns with observed scoped benefits/costs and adverse outcomes; a longer Nu sequence alone supplies no novelty or measured durability. Exact ChainSWE implementation/exposure remains an access gap. | Use the specified inheritance/feedback/accounting contract only for a practical durability decision; preserve publication/implementation uncertainty and all assigned histories. |
| B02/B03/B07/B10: obligations and practice | L-control/R13 and C-exit/#1145 lineage reused; Q1/Q3 authored, Q2 adapted, with the historical workaround retained. | A revised requirement retires its old predicate without erasing historical outcomes. New exercise conditions do not inherit old coverage automatically. Regression, persistent failure, recovery and missing observations differ. | Concrete active/retired obligation and observation rules, plus a source-grounded candidate sequence. No completed changes, runtime equivalence or prevalence estimate. | Resolve Q2's complete phase/clock/effect specification and common-baseline/observation feasibility under the appropriate authority. Promote R09 only when a meaningful result or maintenance decision needs durability evidence. |

The main proposed policy inherits actual workspaces with fresh conversation/environment and fixed public feedback. Hidden evaluation cannot select predecessors, supply later repair feedback or erase failed intermediate delivery. Final recovery remains a useful separate endpoint with its full cost. Reference/rescue branches are optional diagnostics; they neither replace the main history nor create human-steering evidence. Construction, model/worker, recruitment and allocation holds remain unchanged.

## 2026-10-11 continuation: pause requests, clock domains and exit progress

The [C-exit/Q2 contract](../nu-pause-exit-contract-2026-10-11.md) resolves the preceding entry's phase/clock/effect specification through selected pinned Nu source. It defines an authored pause interface and an adapted quit requirement, retaining #1145's existing ImSim workaround. It does not supply a new paper reading, mined feature request, executed fix or validated observation route.

| Themes | Discovery coverage | Primary understanding | Evidence disposition | Next consequential action |
| --- | --- | --- | --- | --- |
| B03/B07/B08: coordination and observation | Selected tasklet, input, transition, time, physics and application paths in 18 pinned files; exact text ranges and hashes retained. No new literature search or PDF reading. | setAdvancing schedules its change; input/rendering and selected processing continue. Static game time and host/outer-loop time differ. Transition input swallowing and Gaia's quick-cut path constrain observation. | Source-supported mechanisms, with an explicit proposed response/precedence contract. No exercised pause, exit, race, defect or latency result. Global halt is one valid implementation strategy, not the required observable outcome. | Separately validate common behavior, input/phase access and the proposed exit horizon/watchdog. Preserve valid local-pause alternatives and legitimate queued effects. |
| B10/B11/B12: practice, costs and inference | Existing #1145 lineage reused; both standalone entry points/plugins and default clock/physics routes checked. | The historical guard is already present in ImSim. Pause can stop gameplay while host work continues. A frozen game clock can conceal a timeout failure; a Title image need not mean working interaction. | A reviewable adaptation and measurement boundary, not representative demand, a pure architecture effect or measured cost saving. A proposed 100-loop bound is unvalidated and not elapsed-time evidence. | Establish practical task value and deadline/observer suitability before assignment. Count synchronization, pause storage, UI/transition work and observation preparation; retain all failures and missing observations. |

Q2's policy is now specified. Runtime correspondence, common baseline and observer/deadline feasibility remain separate held work; another static source inventory cannot establish their success. No construction, model call, worker, recruitment or allocation occurred, and the reading index/assets and historical E/H evidence remain unchanged.

## 2026-10-11 continuation: reuse units, family revision and expressive limits

The [R12 authoring contract](../nu-reuse-and-authoring-contract-2026-10-11.md) binds the previously open reuse-unit question to existing Gaia/entity-structure propagation. A proposed ordinary button family separates supported configuration from structural revision and a hold-to-confirm extension. This is an authored review case, not a mined feature request, new editor or observed non-specialist workflow.

| Themes | Discovery coverage | Primary understanding | Evidence disposition | Next consequential action |
| --- | --- | --- | --- | --- |
| B03/B05/B08: composition and authoring | Pinned overlay, descriptor, propagation and Gaia paths inspected, including five empty external overlay files. S255/S256/S257 reconstructions reused; no new publication search/reading. | Intrinsic defaults exist despite empty external files. Propagation uses previous/current source and target values plus child names, then reconstructs target entities. Configuration, family revision and vocabulary extension differ. | Existing bounded mechanisms, not a universal override-intent, live-lifetime or concurrent-merge guarantee. Local child deletion can persist in the inspected ordinary revision branch; source deletion/reintroduction takes a different branch. | Validate the selected quiescent family, ordinary composition/helper comparator, property/identity semantics, supported input and saved-history access before assignment. |
| B04/B06/B07/B10/B11/B12: outcomes and total work | Selected destroy/read/write and editor routes, plus completed positive/null product-line and Unreal evidence. No current Nu runtime or human observation. | Entity addresses can be reused after unregister/tasklet removal and reconstruction. Prepared-vocabulary gains can shift work into construction, assistance and extensions; shared paper datasets do not multiply evidence. | A concrete candidate boundary and source-derived costs, with empirical benefit and role independence unresolved. Generation-method access gaps remain scoped to a different comparator. | Count setup, supported variants, family revisions, extensions, integration/verification and repair across the actual workload. Promote only for a consequential authoring decision; R20 human outcomes remain future work. |

No variant, component, new authoring interface, observer, runtime, worker, model call or participant study was constructed or executed. Keep the reuse/propagation question distinct from R03 history, R10 migration, R11 team merge and R21 steering effectiveness; none inherits a result from source inspection.

## 2026-10-11 continuation: collaboration artifacts and handoff

The [R11 contract](../nu-collaboration-and-handoff-contract-2026-10-11.md) now gives collaboration preparation a concrete artifact boundary: MMCC Breakout's title group, names and external F# event handles. The first authored case combines a rename/reference change with a presentation change. Independent-property, incompatible-property and conditional deletion/reference cases distinguish integration requirements without treating impossible preservation of contradictory values as correctness.

| Themes | Discovery coverage | Primary understanding | Evidence disposition | Next consequential action |
| --- | --- | --- | --- | --- |
| B03/B04/B05/B08: shared representation and history | Nine pinned source files, four complete and five selected; actual ranges/hashes in the ledger. Completed S283/S284/S286/S287 methods reused. | Group save replaces serialized content; names participate in addresses and external code handles; runtime rename assigns a fresh Id and repairs a specific reference class. Explicit load and unchanged file-path reconciliation have bounded source contracts. | Source-supported integration obligations and an authored task, not an observed merge failure or dedicated Nu collaboration facility. Textual, structural, behavioral and stale-editor success differ. | Identify a meaningful actual treatment/comparator; then separately validate save/load, correspondence, fresh behavior and observation. Keep ordinary communication/manual repair available and live runtime state outside this first case. |
| B01/B10/B11/B12: roles and value | S283/S284's positive comparisons and S287/S288's usability/practice accounts reused with their populations and outcome boundaries. No new participant observations. | Role access, assistance, translation, negotiation and final reconciliation can move work outside individual editing or task-completion timers. A clean artifact does not reveal its total production cost. | An explicit role/handoff and full-work contract. Team value and role independence remain empirical questions, with team comparison deferred. | Establish practical demand and a verified treatment before participant design. Preserve every attempt, team/task dependence, elapsed time, person-work, unresolved conflicts and missing evidence. |
| B04/B08/B10: close scene-merge method access | Nine exact/reformulated web queries returned 49 search panels; five opens and one find returned six more panels. Author/thesis/publisher and public site-tree routes checked; no new paper body. | SceneGit's existing native record is verified, but its matching, conflict policy and comparative method remain unread. Only metadata/selected locator entries and an untruncated filename tree were inspected. | Access-limited method, not absence of useful results. Existing favorable abstract claims remain credited at their original scope. New public-tree access evidence does not close the paper gap. | Resume from the exact lawful full edition when available and consequential. Do not repeat noisy generic queries or substitute secondary citation fragments; continue independent desk dependencies. |

The reading index/assets and Zotero objects are unchanged. No Nu runtime, merge fixture, source variant, adapter, agent/model worker, steering study or recruitment occurred. This contract supports the leading task/cost designs while preserving R11's deferred team comparison and the complete set of experimental holds.

## 2026-10-11 continuation: schema mapping and observation before conversion

R10's [added-reward mapping](../nu-live-edit-contract-2026-10-11.md#application-mapping-for-the-conditional-schema-extension) now specifies the previously open application correspondence. First installation adds reward 200 while preserving the existing seven-field progress; later reloads retain deliberate zero/nondefault rewards, and an explicit new round uses the new default. These are authored requirements, not constructed variants or measured capabilities.

| Themes | Discovery coverage | Primary understanding | Evidence disposition | Next consequential action |
| --- | --- | --- | --- | --- |
| B02/B04/B08: schema and live state | Complete pinned Gameplay text and selected screen getter; prior package-bound Prime reconstruction and S71/S86/S295 notes reused. No new paper search/reading. | Successful missing-field defaulting can erase the distinction between absent reward and legitimate zero. The typed getter can replace the stored model while reading it. Preserved progress includes key/value identity and nested geometry, not only counts or final score. | Explicit first-installation, retained-configuration, repeat and fresh-round mappings; source-supported observation hazard. No executed conversion or universal migration guarantee. | Validate a supported mapping point and pre-installation witness/phase access under separate construction authority. Other schema edits still require their own correspondence. |
| B03/B07/B10/B11/B12: correctness and useful work | Actual hit/removal, cue/direction, time and lifecycle source; existing invariant/cost methods reused. | Zero reward must still remove hit bricks and preserve the existing collision effects. Replay under the new scoring rule need not reconstruct the old score; a restart comparator must reach the same declared mapped state. | A more discriminating correctness/cost specification, with state reachability, observation sensitivity, practical value and effort unresolved. | Establish feasible independent observations and same-state reconstruction before assignment; retain every attempted outcome and account for mapping, capture, repair and verification work. |

Keep the unchanged-shape edit first, the schema extension conditional, R03's same-code boundary intact and R21 deferred. No fixture, converter, observer, source edit, reload, worker, model call or participant study was executed. Source understanding resolves this desk dependency without authorizing feasibility or claiming Nu benefit.

## 2026-10-11 continuation: preparation, learning and role-dependent work

[S38's complete reading](full-reading/S38-cognitive-dimensions.md) closes the acquired-framework gap. Its qualitative trade-offs and bounded editing-time comparison remain useful: abstraction can save repeated work while increasing entry knowledge or navigation, and editing a supplied target can differ greatly across environments. Its framework is not a validated learning scale; its editing exercise deliberately removes solution discovery. Neither observation estimates Nu adoption, maintenance productivity or an agent effect.

The [R07/R20 contract](../nu-learning-and-role-contract-2026-10-11.md) now separates onboarding from trained productivity, preserves all assigned preparation/task outcomes, and counts specialist assistance and tool-family preparation. Existing title-scene and reusable-button contracts supply candidate role boundaries without establishing representative designer work. S39/S40/S42 and S300/S301 retain their scoped positive, null and adverse findings; comprehension, preferences and partial progress remain distinct from complete new/retained behavior.

Discovery, primary understanding and empirical uncertainty remain separate. Three Scite lookups and one bounded web recall query locate conditional programming-walkthrough methods; they do not validate an instrument. The original primary comparison is the next consequential source if that method is adopted. Otherwise continue R08's information/feedback contract and selected edition dependencies. The human comparison, recruitment, construction and all candidate execution remain held, with no new allocation.

## 2026-10-11 continuation: agent-visible evidence and controller compatibility

The [R08 contract](../nu-agent-information-and-feedback-contract-2026-10-11.md) turns the study packet's proposed tool/feedback policy into an explicit information boundary and audits the retained E3a controller. That implementation uses inline source and full-file responses with no candidate tools; its parser/replay and OrderFlow edit rules do not establish ordinary Nu workspace access. Backend continuity is not scientific or technical compatibility. Historical authorization fields and allowances do not override current zero allocation.

Two source findings change the proposed Nu method. Error-first sorting and exact-block deduplication preserve a compiler-diagnostic policy, not arbitrary temporal order/multiplicity. Preserve behavioral sequences and omitted ranges explicitly. Post-controller scoring is correctly separate from repair information, but E3a's first/terminal observations share the remaining trajectory deadline; the proposed studies need independently resourced final evaluation and explicit missingness. No historical outcome is newly classified or rescored.

P08's useful-diagnostic result, P12's probe/intervention limits and S42's initial-information reversal remain credited at their existing scopes. The new contract preserves all assigned work, valid alternative repairs, feedback delivery versus use, and total resource costs. No paper reading, Nu runtime, model/count probe, new adapter or worker was added. The specific next step is a separate workflow/feasibility decision about supported tool/edit/observation authority; continue other consequential desk dependencies while that execution gate remains held.

## 2026-10-11 continuation: predicted knowledge and actual use

[S307](full-reading/S307-programming-walkthrough-draft.md) now supplies a complete 36-page archived-draft reconstruction. Its CMPL, MFD, ChemTrains and DINO accounts describe useful design/documentation changes, including simpler valid alternatives, poorly motivated mechanisms and omitted knowledge. Predicted difficulty sometimes increases despite shorter programs. Preserve those positive and adverse accounts without turning designer judgments, thirty problem/design walkthroughs or overlapping publications into independent participant comparisons.

The [R07/R20 contract](../nu-learning-and-role-contract-2026-10-11.md#candidate-knowledge-and-assistance-inventory) now links existing presentation, rename/integration and family-revision decisions to proposed guiding knowledge, acceptable alternatives, counted assistance and later observations. This resolves the immediate qualitative procedure gap. It is maintainer analysis, not a completed Nu user session or validated readiness gate. The source's summarized user check reports missed prerequisites and insufficient explanations but does not supply the original sample, complete coding or prediction accuracy.

Discovery used exact Scite lookups, bounded web recall and primary archive/publisher routes. The selected PDF is explicitly a draft; native type is corrected to preprint and its complete reading remains separate from unread S304–S306 originals/final bodies. Current/legacy publisher denials, a resolver application shell and a failed manuscript locator are recorded at their actual scope. Follow a newly available exact original when it can change the chosen claim; unknown Nu benefit is not an access gap, and another general walkthrough description would not validate the instrument. Human work and construction remain held.

## 2026-10-15 continuation: completed methods and bounded mechanism evidence

The [reading index](full-reading/INDEX.md) distinguishes completed works, editions and unexamined supplements. The [remote acquisition audit](pdf-acquisition-audit-2026-10-15.md) found existing PDFs and retrieved no new file. The visible S305 DOI page said “DOI Not Found”; the subsequent direct publisher route showed Get Access. The complete predecessor report does not establish journal-edition correspondence.

| Themes | Newly reconstructed evidence | Consequence and next consequential action |
| --- | --- | --- |
| B01/B10/B12: preparation and walkthroughs | S304 supplies six volunteers, sequential preparation/interface changes and four assistance fallbacks. S305 supplies 30 analytical walkthroughs, favorable expressive-power comparisons and reserve problems exposing missed requirements. S306 is the final method; S307 is an overlapping draft. | Count doctrine, explanation and operation assistance as inputs and costs. Retain useful qualitative design guidance without calling it validated readiness or prediction accuracy. Select a consequential role/task before human validation; follow S305’s journal/supplement for an exact edition or materials claim. |
| B05/B08/B10/B11: ordinary tools and reuse | S253 reports acceptable tools alongside fit, instability and migration needs. S254 supplies prefab/configuration reuse and useful relationship inspection, with expertise, propagated errors, redundancy and dead prefabs. S263’s favorable generation package includes expert selection/manual reconstruction; seed selection alone is nearly null. S264 reuses the dataset and adds feature injection with a negligible overall increment over LCG. | Credit ordinary engines, assets and authoring facilities. Generation does not measure propagation or maintenance. Count encoding, selection, construction, integration, extension and repair across actual reuse. The [R12 contract](../nu-reuse-and-authoring-contract-2026-10-11.md) preserves these boundaries; exact quantitative reuse requires the missing code/data or pure expert comparator. |
| B04/B08/B10/B12: scene collaboration | S285 supplies representation, heuristic correspondence, three-way merge and conflict copies. Fixture results and user acceptance are favorable within scope; its 16-user exercise observed no conflicts and had no comparative completion/work outcome. | External F# handles and stale-editor obligations remain outside scene-only merging. Follow supplement/raw conflict cases for an actual comparator need; no general Nu collaboration benefit follows. |
| B10/B12: task populations | S266 adds 67 documents to the reused 200-document corpus. Source-conditioned profiles are useful; period and source change together. Baseline 927/1,000, extension 297/300 and AI-confirmation totals disagree. | Use source-aware task discovery and explicit beneficiaries rather than pooled prevalence, causal trends or unreconciled effect sizes. Exact reuse requires released rows and document-level/source-balanced analysis. The [R14 record](../nu-practice-and-task-provenance-2026-10-11.md) retains the positive scope and limits. |

The local probes are maintainer constructions, not experimental task-solving candidates. [R04](../nu-diagnostic-feasibility-2026-10-15.md) observes warning-only FS0025 and compiler-clean behavioral failure in authored adaptations; a catch-all is correct at the selected simulation-update site for the contrasting pause requirement. The [actual-project continuation](../nu-application-diagnostic-feasibility-2026-10-15.md) confirms warning-only FS0025 in four complete project builds; the pause application remains unimplemented and its content/time/lifecycle obligations untested. [R10](../nu-conversion-feasibility-2026-10-15.md) observes actual Prime conversion preserving an unintended zero and a positional swap; edition-aware mapping fixes the selected added field without validating live Gaia installation. [R05](../nu-event-feasibility-2026-10-15.md) observes actual Nu stub-world ordering, Resolve and explicit unsubscribe, retaining the initially wrong expected order. [R01](../nu-platform-feasibility-2026-10-15.md) observes continuous support and matching final velocity in the direct Box2D case, but about 0.0999H lag misses the predeclared 0.05H tolerance. That tolerance is authored, not a validated definition of useful carrying.

These results separate diagnostic exposure from behavior, type-compatible conversion from intended mapping, a stub event graph from application lifecycle, and contact from complete carrying obligations. The [R03 execution record](../nu-history-feasibility-2026-10-15.md) now supplies one actual functional Gaia B0 history/fresh reconstruction pair: complete declared values/properties match and both negative controls are rejected. The [seeded B1 continuation](../nu-history-continuation-2026-10-15.md) subsequently agrees across twenty complete model/projection observations, within its no-RNG, monitored-no-input prefix. Ordinary agent access remains separate. No probe estimates Nu productivity, agent improvement, steering effectiveness or comparative runtime cost. The broad agenda remains open with specific access, source-to-runtime and empirical questions; a fixed paper count does not close it.

### S205 fuller coordination methods, 2026-10-15

**Discovery:** the existing native attachment resolves a previously retained access gap; no new broad search or artifact acquisition is credited. Two material source decisions record this reading and the S142 table revisit; unchanged historical screens are not resubmitted. **Primary understanding:** [S205](full-reading/S205-jescala-dissertation-access.md) is complete across233 PDF pages and43 consequential visual pages, including summaries, appendices and129 references. **Evidence disposition:** fuller propagation/blocking, specialized FSM and actor-backed monitor mechanisms support positive scoped compactness, extension and performance claims. The34-row static set is numerically identical to S142, not replication. French summary percentages do not completely reconcile with that table. Formal semantics, artifact correspondence, exceptional/blocking-dependent monitor behavior and independent maintenance effects remain unestablished. **Next consequential action:** bind any richer R05/R13 comparison to a practical occurrence/queue/thread/completion obligation and count synchronization and verification work; follow an artifact or formal method only if that chosen obligation requires it. Generic event coordination is no longer an unread-method gap, and unknown Nu benefit remains empirical.

### S227 revised GUI-feedback evidence, 2026-10-15

**Discovery:** exact arXiv v2 acquisition and bounded primary release recheck;
no new broad search or independent work. **Primary understanding:** the
[complete 19-page v2 reading](full-reading/S227-continual-gui-playtesting-v2.md)
compares all methods and appendices with v1. Full-200-game judge validation
reports 87.9% machine–human agreement and κ=.66; two alternative judges retain
the method ordering for GPT-5.4 artifacts. The development playtester and final
rubric judge are more clearly separated. Approximate inference costs are now
reported on a random 10% subset. **Evidence disposition:** the favorable
generation/playtesting result remains, with stronger calibration evidence and
visible additional resources. Corrected gain terminology does not resolve the
plot/threshold correspondence; the human plot/prose and early-stop population
gaps also remain. These are the same S227 work and dataset lineage. The current
website and repository still match the inspected static gallery, not a full
scaffold or run-level release. **Next consequential action:** for B07/B09/B12
and R05/R08, validate actual Nu tool/phase access, preserve ordered observations
and separate development from final-scoring resources. Follow missing raw
trajectory or scaffold evidence when the adopted method requires it; another
generic GUI-paper inventory cannot validate that boundary or establish Nu
maintenance benefit.

## 2026-10-15 continuation: .NET originals and one actual reload

The full original readings of [S218 ReDAC](full-reading/S218-redac-cyclic-reconfiguration.md) and [S219 GUI-component updates](full-reading/S219-gui-updates-access.md) close their former primary-text/visual access gaps. ReDAC supplies guarded cyclic-call quiescence and measured wrapper overhead. Its original distinguishes evaluated progress from the narrower displayed invariant argument; the earlier extracted proof wording is not retained as the publisher’s claim. S219 supplies a controlled object-graph transfer and GUI-routing method, including alias/cycle and delegate handling. It leaves important field policies, rollback and performance evaluation unspecified. Safe entry to an update, valid transferred state and valid later behavior are separate obligations.

| Theme | Discovery and primary understanding | Evidence disposition | Next consequential action |
| --- | --- | --- | --- |
| B04/B08 state and live development | Two already selected native Zotero originals are now fully read; no new discovery search or independent replication is added. | There are close .NET predecessors for quiescence and object/GUI transfer. Neither supplies arbitrary migration, complete external-effect retention or a Nu value estimate. | Use their explicit graph, callback, GUI/native and timing boundaries when a comparison requires those capabilities; obtain exact implementation only for a consequential unresolved mechanism. |
| B06 costs | S218’s guarded-call timings and bounded reconfiguration workload are reconstructed; S219 contains no performance experiment. | Useful low-overhead results coexist with a measurable multiplier on a tiny direct-call baseline. Application anecdotes are not zero-cost measurements. | Measure the selected Nu boundary, including preparation, reconstruction, verification and failures; do not transfer an old wrapper microbenchmark as a modern game cost. |
| B07/B08 actual Nu observation | The [R10 runtime record](../nu-live-reload-feasibility-2026-10-15.md) fixes one halted unchanged-schema reward edit and matched fresh reconstruction before execution. | Both arms preserve the full declared checkpoint and yield the same one-step model/projection: score100→300, one named brick removed. Actual FSI model/dispatcher identity is checked. This is feasibility, not benefit. | Resolve a consequential remaining effect, schema or workflow boundary; retain FSI-versus-Release compile modes, synthetic bridge, sampled-key and native-state limits. The prepared R04 pause/lifecycle comparison is an independent next application gap. |

The [expanded acquisition audit](pdf-acquisition-audit-2026-10-15.md#second-native-attachment-reconciliation) verifies ten more existing PDFs that older notes had treated as unavailable or partial. Their readings were subsequently accepted in the ten-publication continuation below; the 271-work checkpoint remains the historical state of this .NET segment. S305’s final journal edition and the other named originals remain exact access gaps; acquisition and completed reading are separate records.

## 2026-10-15 continuation: ten attached originals and the comparison boundary

The [reading index](full-reading/INDEX.md) now credits the completed selected
bodies for S240, S265, S272–S275, S279/S280, S282 and S286: **281 works =
13 P + 3 A + 265 S**. Each registered parent and exact attachment was checked
before reading; all consequential figures/tables are covered. S273's 98-page
inner body lacks its outer title leaf. Its thesis identity is supported by
the prior registered catalog record, author-deposit abstract/contents and
internal publication lineage; no byte-identical institutional edition is
claimed. S286 is the ACM TOG journal edition. Prior denied routes, partial
readings and historical counts remain dated evidence.

| Theme | Discovery coverage | Primary understanding and evidence disposition | Next consequential action |
| --- | --- | --- | --- |
| B04/B05/B08: state, architecture and authoring | Ten already selected local bodies were read; there was no new broad literature search. S273 alone needed twelve identity/extent queries and eight direct route attempts. | S272/S273 supply structural conformance methods; SuBViS/BPAlt/NCAlt supply graph/class alternatives and preliminary favorable authoring ratings; NodeGit supplies favorable snapshot-matching and curated merge results. Structural conformity, subjective support and running-state preservation are distinct. Reused cases and related tool lineages do not add independent replications. | Credit ordinary composition, class duplication, graph alternatives and semantic matching. For R11/R12/R20, specify identity and replacement semantics, assistance, adapter/repair work and independent behavior checks before selecting a comparison. Keep human outcomes deferred. |
| B06: costs | Original S240/S265 visuals and S279/S280 cost reports now replace partial or abstract-only coverage. Prior raw/source packets retain their exact extent. | S240 cannot isolate pooling from unequal snapshots and a repeated Task Manager image. S265 has repeated favorable/adverse configuration results but measures component power/throughput, not whole-run energy. Monitor cost separates producer export, pipe backpressure and checking; arithmetic and exact-build limits remain. | For R06, match useful work and observation windows, include construction/reconstruction/verification and failures, and retain frame tails, live counts, cumulative creation and retention as distinct quantities. Follow raw/build gaps only for the inference they can change. |
| B07: observations and valid passes | The complete S279 journal and S280 conference publications close the formula/visual gap; original LOFT and named supplements remain unresolved. | Selected fault detection is positive evidence. Snapshot export, quantified-domain vacuity, finite trace endings/resets and unbound measured code limit a pass. S273 conformance and S286 matching check different represented structures. | Apply phase, ordered-event, trigger/domain and failure-state requirements to the prepared R04 application probe and R05. Freeze comparison and falsifiers before runtime; a clean build or structural merge is insufficient. |

The [synthesis](full-reading/synthesis.md#2026-10-15-continuation-structure-running-behavior-and-complete-work)
connects these findings to the active directions. Full reading closes those
method dependencies; it does not finish the broad survey, validate human
steering, establish a Nu effect or turn ten publications into ten independent
studies. The selected pause/lifecycle check remains the immediate application
gap while exact raw/supplement/edition dependencies stay visible.

### S262 final-edition continuation: structural analysis and useful work

**Discovery and primary understanding:** the requested remote Zotero integration
retrieved the exact four-page ACM [Phylogenix paper](full-reading/S262-phylogenix-integration-partial.md).
All text, three figures, Table 1 and 32 references are now read. This closes
its original-body/figure gap; it does not repeat or expand the earlier selected
guide/package inspection. The final edition changes NeonHAT's count from
1,319 to 1,318 and omits the manuscript's demonstration appendix. The four
projects overlap S254's later study and are not independent replications.

**Evidence disposition:** for B03/B05/B08, the paper supplies a useful
configured-object overview and a displayed Canvas cluster. It measures no
completed revision, retained instance variation or authoring savings. Its
schematic distance matrix conflicts with the stated metric, and the previously
inspected package differs from the paper's method description; the exact
reported build remains unbound. For B06, four single analysis times of 1–25
minutes lack matched work, hardware, repetition and phase accounting. They
cannot estimate a runtime or maintenance advantage.

**Next consequential action:** R12 should credit ordinary prefab relationship
inspection when a selected task needs it, then compare actual edits, retained
values/identity, behavior and repair. R06 keeps extraction, inference, file
I/O, viewer handoff and inspection distinct if those operations enter its
workload. Follow the remaining source/build, viewer, video or timing evidence
only for a comparison that depends on it; the current recovery-cost case does
not require another Phylogenix source crawl.

### S206 original completion: adverse results and shared study lineage

**Discovery and primary understanding:** the requested remote Zotero route
retrieved the publisher volume and registered its exact four-page
[ECOOP article](full-reading/S206-ecoop-type-study-partial.md) before reading.
All text, both Figure 1 plots and nine references are now read. A targeted
text/visual return to S132's PDF page 7 / printed p.28 resolves what its scanner
test-count passage actually says; it is not a second full reading.

**Evidence disposition:** for B02/B10/B12, the report preserves a dynamic-group
scanner-time advantage (p=.04) and an inconclusive parser comparison (p=.40),
under bundled language/checker/annotation treatments. S132's fuller methods
make the timing result conditional on 21 completers in each group, excluding
four dynamic and three static participants; parser outcomes retain all 49.
Unequal 16/18-hour training is outside those endpoints. The matching designs
strongly support one experiment lineage, without verified participant/log/test
identity. S206's 25 hidden scanner tests conflict with S132's 23; its reference
4 names an unlocated June 2010 technical report, not the final OOPSLA paper.

**Next consequential action:** R04/D1 must keep compiler feedback, observed
behavior and training/adaptation work distinct. The original-body gap is
closed; follow the technical report, tests or logs if exact endpoint
reconstruction becomes necessary. No current Nu/D1 prediction depends on
resolving that historical discrepancy. The prepared pause and recovery checks
can proceed under their own contracts, preserving failures and complete work.

### Bounded application and recovery observations, 2026-10-15

This continuation adds local construction evidence, not publication readings
or independent field coverage. The [R04 pause/lifecycle comparison](../nu-pause-runtime-feasibility-2026-10-15.md)
passes both current baselines and both completed successors. Five frozen
source faults reach their declared first failing checks. The wildcard remains
a valid implementation of this selected update clause; no diagnostic-attention
or maintenance advantage has been measured.

For **B04/B08 state and live development**, a retained setup failure and its
observation-only diagnostic show why model equality is insufficient: two bricks
had correct model/color values but stale projected positions. Pinned keyed
reconciliation and initialization-only positions support an identity-collision
explanation, with the unrecorded initial key set explicitly limiting that
inference. Clearing content before installing the fixed checkpoint is visible
alignment work. Earlier successful B0/B1 reconstructions remain valid at their
observed scope; they do not supply a general replacement guarantee.

For **B07 observation**, positive advancing-event evidence, complete represented
state/projection, counted event triggers, lifecycle checks and actual fault
detections now establish a bounded application oracle. Synthetic entity clicks,
sampled Left/Right states and request-level audio remain narrower than physical
input, native playback or whole-game behavior. The next consequential step is
to bind that oracle to a useful change and complete work accounting; another
generic monitoring-method inventory would not establish maintenance value.

For **B06 costs**, the [R06 component comparison](../nu-recovery-cost-feasibility-2026-10-15.md)
separates acquisition, direct recovery, next-callback readiness and verification.
The original reconstruction feasibility process timed out before its first
setup observation. A separately assigned diagnostic subsequently passed without
a stack attachment; its complete represented output matched the history route.
The prospective release then retained the original failure and admitted exactly
the twelve previously assigned measured processes, all of which passed. History
acquisition was faster in all six pairs, while its direct recovery call was
slower in all six. Request-to-ready differences ranged across both signs. These
are local first-use component observations with unequal retained payload scopes,
not an isolated persistence effect or a maintenance-benefit estimate. The startup
timeout remains unexplained; no feasibility/diagnostic time enters the measured
summaries. Construction, workflow access, diagnosis and useful repair costs
remain unmeasured. R02's standalone continuation below now supplies its bounded
unchanged-application lifecycle prerequisite; another identical timing series
would not establish practical value.

### Standalone lifecycle and initializer observations, 2026-10-15

**Discovery and primary understanding:** no new publication search or reading
is claimed. The [R02 standalone pair](../nu-standalone-lifecycle-feasibility-2026-10-15.md)
executes the previously source-bound MMCC/ImSim lifecycle, preserving the
existing quit workaround, different state owners, and source/physics packages.
Both unchanged applications pass their single assigned run, with all earlier
preparation/build failures retained.

**Evidence disposition:** for B03/B07/B08, ordinary standalone mode and the
public event/observation boundary now have executed support. Both runs reach
Title, Gameplay, Quit, and a fresh second session within fixed callback and
wall bounds. MMCC clears its model; ImSim retains unselected screen properties
while removing its old scene and descendants. Separate exact scalar captures
observe two initialized generations in each arm; ImSim's scene IDs differ.
Its Play transition is one callback faster than the frozen nominal prediction
(95 rather than 96), without changing the common bound or pass definition.
These findings validate the declared lifecycle scope, not package equivalence
or an isolated ownership effect.

**Next consequential action:** establish the input and effective-pause boundary
for the prepared pause/exit references. Synthetic ClickEvents do not exercise
SDL, ButtonFacet hit testing, capture, or physical input. Programmatically
queued keyboard events also do not change held-key polling state, so a later
reference's convenient event route must not silently exclude valid alternatives.
Retain construction, observation, synchronization and recovery work separately
from any future maintenance-benefit outcome. The historical issue motivates an
adaptation; task prevalence and practical benefit remain unmeasured.

### S308/S309 continuation: API structure is a candidate mechanism

**Discovery coverage:** exact Scite lookups and an outgoing 40-edge graph
trace the previously retained engine-API lead to its primary metric origin.
The [search ledger](nu-background-searches-2026-09-30.md#s308s309-api-metric-origin-and-artifact-boundary-2026-10-15)
records actual queries, returned ranges, access failures, provenance limits
and deferred method leads; this is not a new field-completeness claim.

**Primary understanding:** [S309](full-reading/S309-structural-api-usability.md)
is complete in its 36-page author-hosted early-view edition. It defines eight
metrics for nine structural issues and applies them to seven Java systems.
The evaluation uses corresponding structural counts, manual examples and some
community-belief/version comparisons. It explicitly does not measure whether
programmers find low-scoring APIs harder to use. The AMNCI formula,
pseudocode and reported aggregate scores also have an unresolved mismatch.
[S308](full-reading/S308-engine-api-metrics-access.md) remains abstract/context
and bounded artifact coverage: the actual journal method, 95-engine selection,
thresholds, implementation and validation remain unread.

**Evidence disposition, B01/B10/B12:** useful operational structural descriptors
are distinct from a validated developer outcome. S309 supplies neither a
cross-language validation nor a Nu benefit estimate. The likely author S308
workbook supports a bounded results-release attribution, with an unresolved
paper-to-repository link, a sum/average disagreement and no exact source
snapshots or measurement code in its three-file tree. A related 526-engine
corpus cannot be substituted for those 95 rows. These limits do not invalidate
every structural hypothesis or establish absence of other validation work.

**Next consequential action:** R01/R07/R20 should retain task behavior and total
work as outcomes and name the actual interface before selecting a structural
descriptor. If the descriptor will support a usability prediction, resolve
its relevant outcome validation and language/extraction mapping. S308's exact
body remains the executable acquisition target when its corpus or method
claim matters; S309's reading does not fill it. A further generic API catalogue
cannot settle Nu's benefit or readiness. Human learning and steering
comparisons remain future work under their existing allocation boundaries.

## 2026-10-16 continuation: application schema defaulting and preservation

**Discovery and primary understanding:** no new paper search or reading is credited. The completed S71/S86/S295 and S218/S219 mechanisms remain distinct predecessors. A pinned [Nu source audit](../nu-live-edit-contract-2026-10-11.md#2026-10-16-source-boundary-for-an-explicit-migration) binds raw pre-conversion observation, typed conversion, content synchronization and event/setter ordering; it does not construct an atomic application migration.

**Evidence disposition for B02/B04/B08:** the [R10 initializer-only live/fresh case](../nu-schema-reload-feasibility-2026-10-16.md) now preserves the old seven-field checkpoint and selected projection while actual FSI conversion gives the added reward field zero despite its initializer of 200. The declared next hit yields score 100; the fresh application observes initial reward 200 and its explicit required-state reconstruction yields 300. Both complete reward-specific continuation oracles pass. This is a valid failed live mapping, not a matched successful preservation pair or a general schema result. The frozen contract, complete selected observations, full attempt ledger, build/runner identities and narrow Nu.Spine exact-path timing limit are retained.

**Next consequential action for B08/B11/B12:** the separate [explicit-migration treatment](../nu-schema-migration-feasibility-2026-10-16.md) now freezes first installation, legitimate zero/nondefault retained configuration, repeated reload and failed-compilation observations. Its application compiles, but four harness/conformance failures remain unresolved. Subsequent objective attempts 11–18 failed consecutively, crossing the five-failure return at 15; passing controls 19/20 do not authorize that overrun. Construction is stopped with the current draft uncompiled and unaccepted. Preserve the return and exact draft; ordinary continuation does not resume this gate. No native migration process ran and no migration success follows from these construction checks. Preserve intermediate content/effects and account for all mapping, verification and reconstruction work. The unchanged-schema success remains valid at its narrower boundary; this adverse schema result neither erases it nor establishes a net benefit. Ordinary agent access, native/external effects and human steering remain separate questions. R02 input construction remains stopped under PLAN's return.

## 2026-10-18 continuation: structural metrics and diagnosis endpoints

**Discovery coverage:** an exact four-DOI lookup follows known S66 method leads,
requesting Scite `limit:20` and receiving all four matches. Selected author
routes resolve Java Whyline as S310. The existing remote Zotero integration
also acquires S308's exact publisher PDF. The [ledger](nu-background-searches-2026-09-30.md)
records the routes and actual source decisions; this is a targeted continuation,
not a new field-wide search or a completeness claim.

**Primary understanding:** [S308](full-reading/S308-engine-api-metrics-access.md)
now has complete 17-page text/visual coverage. It selects 95 C++ repositories
from a top-starred May 2020 collection, averages `.cpp` file scores, and assigns
usability labels to metric ranges. Its explicit companion link resolves the
earlier attribution uncertainty. Its AESI construct and documentation threshold
differ from S309; calculator/source provenance, missing-case treatment and the
workbook sum versus paper mean remain unresolved. It reports no developer task
validation. [S310](full-reading/S310-java-whyline-diagnosis.md) has complete
ten-page author-edition coverage. Its favorable, task-dependent diagnosis and
change-recommendation comparison uses a custom interface without code edits;
the later author-file date and shared Whyline publication lineage are retained.

**Evidence disposition, B01/B04/B08/B10/B12:** structural descriptions,
recovery access, diagnosis and verified maintenance are different outcomes.
S308's distributions retain their descriptive value but do not validate Nu
usability. S310's positive recommendations do not establish executed repair,
and its output-to-source dependency interface cannot be inferred from Nu's
history roots. These results refine R01/R03/R07/R20 without importing an
effect size, treating publications as independent replications, or erasing
the completed R03/R06 feasibility/cost results.

**Next consequential action:** R03 should bind a practical symptom/question to
actual retained evidence and an ordinary supported tool before constructing a
debugging-benefit comparison. Separate reaching a state, locating the fault,
proposing a correction and delivering a verified repair/continuation; identify
supplied causal information and count added instrumentation. R01/R07/R20
should select the actual task-facing interface and outcome before seeking
predictive validation of a structural score. The selected body gap is now
closed; exact calculators and developer validation remain conditional
dependencies, not evidence of absence. R02/R10 remain stopped and experimental
candidate, participant and human-steering allocations remain unchanged.

## 2026-10-18 continuation: a debugging symptom and inspection's effects

**Discovery and primary understanding:** the [R03 question/access map](../nu-history-question-access-2026-10-18.md)
reuses S310 and the retained R04 reconstruction failure, with no new paper
search or reading credit. Exact retained hashes and selected original source
bodies were rechecked. The actual symptom is a model/entity position mismatch;
the missing original fresh scene names still prevent confirming the proposed
name-collision explanation.

**Evidence disposition, B04/B08/B12:** a stored state, a causal trace, an
available inspection interface and a verified repair remain different things.
Pinned Gaia Interactive evaluation snapshots even a getter and clears redo
history. This source-derived observation changes the tool/cost policy of a
future comparison; it does not establish a GUI run or show that every way of
inspecting Nu state has the same effect. The R04 maintainer's successful
reconstruction amendment remains a scoped setup correction, not independent
task-solving or evidence of diagnostic benefit.

**Next consequential action:** validate the selected ordinary inspection route
and its branch/halt boundary for a practical case with its actual predecessor
evidence. Preserve the original episode as an incomplete causal record; a new
deterministic mechanism case would be authored and would not fill that history.
Continue independent authorized mechanisms while candidate execution, human
steering and the R02/R10 returned gates remain unchanged.

## 2026-10-18 continuation: R12 public propagation

**Discovery and primary understanding:** no new paper search, full reading or
independent study is credited. Targeted original source checks resolve a
public `World.propagateEntityStructure` route through an actual stub world,
rather than a copied or reflection-invoked descriptor algorithm. Existing
R12 reuse, Cognitive Dimensions and generation readings retain their scopes.

**Evidence disposition, B04/B05/B08/B10/B12:** the
[executed fixture](../nu-propagation-feasibility-2026-10-18.md) passes one frozen
Button/Text family revision. It preserves divergent target values and local
deletions, updates matching values, introduces new source children and retains
target-only children. Source deletion removes a locally edited child; an
equal-valued return follows the source. The recreated target has a new root
ID. These are useful policy observations, including limits, not an authoring
or productivity advantage. One source-review rejection, the accepted first
build and one runtime attempt are preserved with complete identities.

**Next consequential action:** choose a practical family revision with explicit
override/deletion intent, an ordinary helper/composition comparator and total
construction/configuration/revision/verification work. Gaia menu/undo,
save/reopen, interaction and runtime lifetime remain separate. Another passing
supported variant does not by itself establish the benefit needed to promote
R12 or validate R20/R21 human outcomes.

## 2026-10-18 continuation: an existing propagated family

**Discovery and primary understanding:** a targeted pinned-project source
search finds Terra Firma's saved scene as an actual use of entity propagation.
The [R12 case preparation](../nu-reuse-and-authoring-contract-2026-10-11.md#2026-10-18-existing-terra-firma-family-and-next-revision-case)
distinguishes its 197 actual serialized descriptors and 166 links from nested
historical descriptors. The selected family has 32 placed palms across four
Villa trees. This expands the earlier bounded empty-overlay sample with a
different existing facility; it is one project artifact, not independent
beneficiary evidence or a new publication reading.

**Evidence disposition, B04/B05/B08/B10/B12:** source inspection binds the
gameplay load route, its first-creation boundary and an ordinary F# composition
precedent. The proposed shared tint/local roughness contrast exposes a possible
whole-property versus field-level requirement mismatch. Nested propagation
also reaches a Villa ancestor with three complete tree targets. These are
consequential source-derived predictions, not new observed failures, rendering
results or measured work. A batch field update is a valid incremental-edit
alternative; a constructed parameterized family has separate setup and
integration costs. Existing practice readings motivate those costs without
establishing demand for this authored change or a Nu advantage.

**Next consequential action:** observe the unchanged scene's loaded values,
links/history and save/reopen correspondence before accepting the common
revision protocol and comparator. Retain older saved descriptor layouts,
unrelated configuration and actual reconstruction work. Keep incremental
maintenance separate from full family construction, property outcomes from
visual/physics behavior, and maintainer feasibility from R20/R21 human effects.
The R02/R10 returns and experimental allocations are unchanged.

## 2026-10-18 continuation: Terra Firma preservation prerequisite

**Discovery and primary understanding:** the targeted pipeline, application
loop/save and pinned Prime symbol-formatting checks support the
[executed load/save/fresh-reopen record](../nu-terra-firma-reopen-feasibility-2026-10-18.md).
They are source and maintainer-construction evidence, not a new publication
reading, Zotero addition or independent study. The actual runtime supplies
the previously missing baseline observation for the selected existing family.

**Evidence disposition, B04/B05/B08/B10/B12:** one corrected native pair passes
the declared 197-entity correspondence, all 166 links, 11 raw saved history
structures and selected configuration of four Villas and 32 palms. L1 uses
L0's actual save in a fresh process; 36 generated protected children remain
separate from the 197 saved entities. The first process/save succeeded with an
invalid observer representation and remains unscored. Its formatter correction,
failed build/proof, rejected reviews and restart-interrupted work are retained.
This distinction matters: process success and a save file did not by themselves
establish the required observation or preservation.

**Next consequential action:** accept the common tint/local-roughness revision
and ordinary batch alternative using the observed baseline, preserving
indirect reconstruction, unrelated configuration and complete work. The result
does not execute propagation, measure visual/physics preservation, validate
ordinary Gaia/agent access, establish practical demand or estimate authoring
benefit. Existing literature and the deferred human steering question retain
their separate scopes. R02/R10 and candidate/participant allocations are unchanged.

## 2026-10-18 continuation: field intent and reconstruction measurement

**Discovery and primary understanding:** selected pinned lifecycle, entity
serialization and RGBA constructor bodies support the
[accepted Terra Firma revision protocol](../nu-terra-firma-revision-feasibility-2026-10-18.md).
This extends the existing source/practice-grounded case without adding a paper
reading or independent study. Both operators receive the existing family
metadata; the ordinary batch reads each current material record and changes
only the requested field.

**Evidence disposition, B04/B05/B08/B10/B12:** the shared tint and local
roughness condition now separates field-level intent from whole-property
propagation. The predicted material conflict and indirect Villa reconstruction
remain hypotheses for this artifact. A rejected recorder design showed why
endpoint IDs alone cannot establish repeated reconstruction counts: a missing
balanced intermediate pair can leave the same endpoint. The accepted protocol
requires independent callback counts and ordinals, while retaining coherent
count divergence as evidence. Callback integrity does not prove complete
internal/native event emission or delivery.

**Next consequential action:** complete source/checker/compile acceptance and
observe the fixed four revision cases and eligible actual-save reopens. Retain
adverse delivery, treatment-specific histories, all declared collateral
configuration and maintainer preparation work. Faithful reopening of an adverse
save is not successful delivery. Visuals, native lifetime, ordinary editing
access, practical demand and authoring/steering benefit remain separate gaps.
Neither construction nor this source synthesis changes the R02/R10 returns
or experimental candidate/participant allocations.

## 2026-10-18 continuation: observed field-intent limit and integrity return

**Discovery and primary understanding:** the existing Terra Firma family now
has [three completed revision/reopen pairs](../nu-terra-firma-revision-feasibility-2026-10-18.md).
New selected address/filter and save/read Order bodies explain coherent
prediction divergence and strict history correspondence findings. This is
maintainer mechanism evidence on one artifact, not a new publication, an
independent empirical population or a broader task-prevalence result.

**Evidence disposition, B04/B05/B08/B10/B12:** both shared propagation and
shared batch deliver the tint to all 32 palms. With an independent local
roughness choice, propagation tints 31 and retains both the target's desired
roughness and undesired old albedo. It faithfully saves/reopens that adverse
state. This observes a whole-property/field-intent boundary without assuming
every override should be overwritten. Other declared configuration, links
and raw histories preserve. The two propagation histories separately fail
exact fresh current-source correspondence because Order values regenerate;
this is not established rendering damage or a future maintenance defect.

Both propagation operators record 160 original reconstruction pairs instead
of the frozen 163 prediction; exactly three same-name copied palms account
for the difference. B-shared records zero operator pairs. Preserved callback
counts, ordinals and address/ID transitions support the managed observations,
subject to internal event-emission/delivery limits. The missed local target
is rebuilt twice, so that failure is separate from the count divergence.
Fixed order, unequal instrumentation and missing complete work prevent a
speed or productivity conclusion.

**Next consequential action:** B-local stops before editing after its staged
input bytes change; it supplies no local batch outcome and no eligible reopen.
The [storage-integrity return](../workspace-integrity-return-2026-10-18.md)
preserves a verified C: recovery copy and stops native execution. Establish
reliable execution storage and revalidate the exact inputs before any
prospectively bound continuation. Preserve all seven processes and the
original chronology. A subsequent practical repair/completion comparison must
count selection/helper construction, verification, failure, repair and history
consequences. Visuals, native lifetime, ordinary editing access, demand and
authoring/steering benefit remain separate questions. The R02/R10 returns,
candidate/participant allocations and broad survey boundaries are unchanged.

## 2026-10-18 continuation: practical rationale without a field-merge promise

**Discovery and primary understanding, B05/B10/B12:** the
[new propagation-practice check](../nu-practice-and-task-provenance-2026-10-11.md#2026-10-18-continuation-material-revision-rationale-and-observed-limits)
examines a distinct issue/discussion vocabulary rather than repeating the
earlier reload/undo/default-asset frame. The maintainer's shared-material
proposal and local-delta discussions ground the selected family-maintenance
question. Complete historical defect accounts preserve separate dispatcher,
link, history and child-order obligations. The exact search ranges and
uninspected continuations remain in the ledger; no new paper reading or
independent empirical population is claimed.

**Evidence disposition:** R12 is an authored task on a real artifact with a
specific maintainer rationale. The sources do not promise field-wise merging
inside a material record, and all credited accounts come from the maintainer.
Thus the observed local-condition failure concerns the frozen authored
requirement; it does not establish a violation of documented Nu semantics,
external demand or measured benefit. The related historical child-order
report does not diagnose the experiment's fresh timestamp-Order findings.

**Next consequential action:** preserve shared versus local intent explicitly
in any practical completion/repair comparison, including valid whole-material
policies and the work of translating the requirement into supported edits.
Reliable execution storage remains prerequisite to the missing batch/local
condition. Ordinary editing access, complete work and broader beneficiary
coverage remain separate dependencies; another broad issue search would not
resolve them. Existing allocations and R02/R10 returns are unchanged.

## 2026-10-18 continuation: batch/local result after exact input recovery

**Discovery and primary understanding, B04/B05/B08/B10/B12:** the
[revalidated Terra Firma continuation](../nu-terra-firma-revision-feasibility-2026-10-18.md#revalidated-continuation-and-next-consequential-action)
resolves the previously missing local batch outcome. This is two more processes
on the same artifact under the original build and oracle, not an independent
study or a new prevalence source. The original integrity failure remains.

**Evidence disposition:** batch now delivers all 32 tints while preserving the
local roughness, other declared configuration, links and eleven old histories;
its actual save reopens with those values. Zero operator lifecycle callbacks
and unchanged original IDs contrast with propagation's 160 reconstruction
pairs. The recorded 447-file pre-launch composition and protected post-run
checks pass for both processes. This supports the authored field-intent
comparison, while propagation's adverse local result and fresh Order/history
findings remain unchanged. Different history obligations and the interruption
prevent treating the pair as an equal-future-state or speed comparison.

**Next consequential action:** specify practical completion/repair and later
history obligations before another execution assignment, counting selection,
helper construction, verification, failed work and recovery. The current series
contains four complete pairs and one invalid startup across nine processes.
Ordinary editing access, native lifetime, demand, complete authoring cost and
steering benefit remain separate; the broad survey and R02/R10 returns retain
their existing boundaries.

## 2026-10-18 continuation: S305 journal edition reconciled

**Discovery and primary reading, B01/B10/B12:** the user supplied the final
journal PDF and updated its existing Zotero DOI. The [complete journal reading](full-reading/S305-problem-centered-design-journal-reading-2026-10-18.md)
covers all 39 PDF pages, printed pp.319-355, all 11 figures and the full method,
results, limitations and reference tail. Publisher/PDF and legacy Crossref
metadata support the same article identity under the two DOI forms; a formal
registry alias and unavailable legacy-file byte identity are not established.
The report and journal remain separate editions of one credited S305 work.

**Evidence disposition:** the final retains three designs, six development and
four reserve problems, 30 analytical walkthroughs and the favorable OpsTrains
ranking. It adds one minimal prototype and the same six-person assisted
Bunsen check reported in S304. Users' omitted basic assumptions, compelling
alternative interpretations and need to understand action effects qualify the
analytic prediction. The journal explicitly treats walkthroughs as fallible
preparation for, or partial substitutes for, empirical evaluation; it supplies
no calibrated readiness/accuracy score or three-design user comparison. The
report's full Bunsen appendix is absent from the journal and remains useful.

**Next consequential action:** use this final-edition account in R07/R20's
knowledge/assistance inventory, preserving chosen representation, operation,
understanding of effects and independently verified outcome as separate
observations. Select the practical task before human validation. Follow
CU-CS-480-90 or underlying protocols only when a selected claim requires them;
the journal body is no longer an access gap. The 286-work checkpoint is
unchanged, and shared ChemTrains reports are not independent replications.

## 2026-10-18 continuation: R12 history consequences and comparator policy

**Discovery and understanding:** no new search or publication reading was
needed for this source-level question. The [retained-history audit](../nu-reuse-and-authoring-contract-2026-10-11.md#2026-10-18-retained-history-audit-a-conditional-switching-prediction)
now binds all four actual saved endpoints to the pinned whole-property and
default-comparison branches, including nested Villa propagation.

**Evidence disposition:** both completed batch cases deliver the specified
tint and retain their old histories. A later switch to source propagation is
predicted to change only the edited source palm: the other batch-tinted
records differ from the default used when old history lacks that property.
The corresponding propagation-predecessor predictions are 32/32 for shared
and 31/32 for local, preserving its whole-material override. These are
conditional source predictions, not later native observations. The original
invalid startup, local tint failure and Order-history findings are unchanged.

**Next consequential action:** distinguish continued batch use from switching
to propagation, and declare repair/history conversion as explicit work. A
second batch update need not depend on propagation history. Bind intermediate
delivery, actual inherited state and cumulative construction/verification/
repair costs for the practical comparison. The source result narrows that
design; it does not establish authoring savings, independent demand, a general
reuse advantage or whole-background survey completion.

## 2026-10-23 continuation: development history and credible status quo

**Discovery and primary understanding, B02/B04/B05/B08/B10/B12:** ten bounded
maintainer assistants traced Nu's propagation, history-access and live-model
lineages; inspected ordinary Godot, Unity and Unreal material workflows; bound
Redux and stable/alpha XState mechanisms; and recalled structured-merge and
correspondence literature. The [search ledger](nu-background-searches-2026-09-30.md#2026-10-23-development-history-comparators-and-merge-methods)
separates exact source editions, selected reading, noisy discovery, failed
routes and decisions. Seven completed primary reconstructions were reused;
no new paper body, PDF reading or native application run is credited.

**Evidence disposition:** the [development-history audit](../nu-development-history-audit-2026-10-23.md)
shows that Nu's public override policy operates at its property boundary. The
authored material-field requirement is stronger; its missed tint remains
adverse to that requirement. Relevant historical repairs are present at the
pin, with an abandoned sibling and unverified issue/commit associations
kept distinct. Group save, entity export, raw Order/history and effective child
sequence are different obligations. Ordinary property-panel inspection is
source-supported without Interactive's unconditional snapshot; UI precision,
branch behavior and agent transport remain unobserved. Live-model evolution
has practical maintainer rationale, while successful type-default conversion
does not promise an application's new-field initializer.

The [status-quo audit](../nu-status-quo-and-transfer-audit-2026-10-23.md) credits
Unity/Unreal selective material inheritance and Godot's ordinary copied-material
and parameterized-shader alternatives. The known merge/correspondence methods
are predecessors, not grounds for a new-algorithm claim. Redux's retained-action
recomputation and XState's application-owned snapshot transformation are
existing non-game mechanisms with separate history, pending-work and effect
boundaries. Their documented/source-supported capability is not executed
save/reopen, semantic migration, developer benefit or independent demand.

**Next consequential action:** the [material-intent follow-up](../nu-material-intent-baseline-2026-10-23.md)
identifies the explicit mode table plus field update as an ordinary helper,
so construct that stronger reference baseline first. The prospective component
separates imported-asset fallback, source inheritance and equal-value pins;
its synthetic pairing controls do not establish Nu persistence. A later
integration must improve capability or complete work beyond this baseline,
with actual saved predecessors and metadata/setup/verification/repair counted.
For non-game transfer, the [Showtime follow-up](../nu-xstate-practice-case-2026-10-23.md)
now binds a public persistence-schema/reset change and relaunch report, with
machine-change causality and cross-version preservation intent still unresolved.
Do not treat that source evidence as a runtime or benefit result, or add a
cosmetic machine change solely to fit a preferred task label. Follow the deferred merge/lens
originals if a stronger general resolution or correspondence-law claim makes
them consequential. The broad survey stays open and the R02/R10 returns stay
stopped; these findings do not allocate candidates or participants.

## 2026-10-23 follow-up: a stronger ordinary baseline and valid reset policies

The [material-intent component](../nu-material-intent-baseline-2026-10-23.md)
now has an accepted pure implementation and Linux/Windows control results.
The saved Nu sequence is prepared at the architecture level, with actual-state
continuation, relative-order observations and all work retained; no new native
result is established. A passing supplied-map component is neither actual
material persistence nor comparative benefit. Once the ordinary native baseline
is accepted, further repetitions need a practical comparison that can change a
decision.

The [Harny follow-up](../nu-xstate-practice-case-2026-10-23.md#actual-runtime-evolution-with-an-explicit-compatibility-cutoff)
binds real XState-to-declarative runtime evolution and same-version pause/resume
demand, while its source deliberately excludes old-schema resume. Together
with Showtime's reset policy, this narrows the proposed transfer task: find an
actual retention requirement rather than declaring rejection a defect. Six
focused queries and their selected primary sources leave that application
selection unresolved; no new paper body was read and no field-completeness or
lack-of-demand inference follows. Mechanism findings, practical demand and
empirical advantage remain separate.

## 2026-10-23 completed parallel follow-up and handoff

The [R03 passive-access preparation](../nu-passive-access-preparation-2026-10-23.md)
produced reviewed configuration, launch and capture artifacts, preserving four
construction failures. Its then-pending native check is now terminal, as
recorded below. The [continuation prompt](../continuation-prompt-2026-10-23.md)
contains the current handoff. The separate R02/R10/R12 returns remain stopped;
accepted preparation is not native or benefit evidence.

The new source work improves task selection. [Nu #151's exact recovery
lineage](../nu-history-question-access-2026-10-18.md#2026-10-23-recovery-demand-and-the-next-comparison)
supports preserving an editing session after user-code failure, with a
maintainer-authored historical trigger. It does not recover the missing roots
of our stale-position episode or establish independent adopter demand. R03/R06
still need a common verified recovery/repair and continuation outcome, with
capture, navigation, reconstruction, failures and verification included in
separate work ledgers. Reused S42/S66/S310 evidence makes initial information
and the difference between localization and repair decisive.

[S311](full-reading/S311-partial-trace-dependency-estimation.md) is a newly
completed 15-page preprint reading. Estimated missing dependency edges improve
one reported automatic regression-localization pipeline on 489 selected bugs.
They remain estimates with false/missed-edge risk, not actual retained state
or completed repair. A rescue estimator would be a separately named treatment;
it cannot fill missing R03 provenance retroactively. Acquisition, full reading
and reproduction remain distinct; the linked implementation is access-limited.

Two additional source cases preserve useful adverse possibilities. The
[authentic API rename](../nu-practice-and-task-provenance-2026-10-11.md#2026-10-23-a-real-api-rename-and-a-qualified-lifetime-case)
creates consumer editing work that a valid equivalent catch-all may avoid,
without adding gameplay behavior. R04 should retain that boundary rather than
select only favorable new-case warnings. The R05 event-retention report is
qualified, with actual disposal/collection and live-contact behavior still
unmeasured; an observed treatment-induced behavior regression would be adverse
evidence, not an invalid run.

For transfer, [Camunda's current-instance migration](../nu-workflow-migration-transfer-2026-10-23.md)
has explicit user preservation demand and an existing manual-plan/validation
baseline. Finishing old instances under old behavior is only a valid option
when it meets the requirement. A new assistance method must improve on those
ordinary facilities. [NgRx replay](../nu-status-quo-and-transfer-audit-2026-10-23.md#a-concrete-replay-failure-and-a-migration-obligation)
similarly makes reducer availability and external-effect boundaries concrete,
but no eligible exact historical artifact has been recovered. A missing
artifact is an eligibility limit, not proof that replay failed.

The [search ledger](nu-background-searches-2026-09-30.md#2026-10-23-parallel-recovery-evolution-and-transfer-source-audit)
records the once-only 74-source audit and separate nine-decision scholarly
segment, with query/edition/coverage gaps. These deepen B02/B03/B04/B06/B08/B10
and B12 without closing the other themes or the broad survey. The next
consequential scholarly lead is ADI if ordinary coding-agent repair is selected;
no title-only screen is treated as a read method or a novelty verdict.

## 2026-10-23 native access disposition

The [single R03 attempt](../nu-passive-access-observation-2026-10-23.md)
supports ordinary LeftWall selection and reading its displayed position. The
submitted drag did not create the required distinct state or history entry,
so the proposed passive history traversal was not tested. A new `gaia/imgui.ini`
also violated the frozen output boundary. Independent and parent review retain
both failures and the partial observations; normal process exit is not a
passing protocol or evidence of repair value.

This changes readiness for B04/B08's history-access comparison, without
changing the literature's reported findings. The cause of the ineffective
interaction remains unresolved. The consumed assignment has no retry; any
source-only clarification informs a distinct future question. R03/R06 still
need an eligible practical task, demonstrated access, a common verified
recovery/repair outcome and complete work accounting. No new search, paper
reading or candidate/participant evidence is credited by this local attempt.

## 2026-10-25: resumed integration and a recovery target

The user reactivated the goal after the October 23 handoff. The completed
[S312 ADI reading](full-reading/S312-adi-agent-repair.md) is now integrated at
arXiv v1; the checkpoint is **288 fully read works**, not field completion.
The selected edition's 22 pages and visuals were read by the earlier worker.
Substantive review verified the paper's counts and exact artifact summaries,
and corrected the clean-matching claim: deposited prompts differ materially.

ADI-enabled configurations have higher reported held-out repair counts in all
four model comparisons; PDB is mixed and adverse for two. The comparison has
common paper-reported benchmark/model/budget conditions but bundles dynamic
information, tools, prompts/workflow and reruns. Final patch resolution is
stronger than localization or agent self-report. Those useful results coexist
with curated Python-task coverage, missing comparator trajectories/results,
submitted-ID inconsistencies and unresolved temperature/source-to-run binding.
API spend and selected runtime omit complete setup/integration/maintenance work.

For B04/B08 and R03/R08, ADI reconstructs selected traces by rerunning a
reproducer. It does not recover missing actual historical roots or establish
native/GUI state preservation. The [reviewed recovery-target analysis](../nu-recovery-target-and-serialization-2026-10-25.md)
selects session recovery as a distinct practical question: ordinary Gaia
already provides history/F7 checkpoints. K, G and handler-entry F can differ,
and group-file persistence omits Breakout's screen model. A new procedure must
improve useful preservation or complete work over that credible status quo.
Screen-file replacement is a stronger existing comparator candidate with
unverified lifecycle, content, transaction and continuation obligations.

The [source clarification](../nu-passive-access-source-followup-2026-10-25.md)
explains how property focus can occur without an accepted edit and supplies
version-matched conditional ini-save semantics. The actual gesture, writer and
Twizzle native source/build correspondence remain unobserved. Native-001's
terminal failures stand; source explanations cannot fill its missing fixture.

**Current handoff, updated after user steering:** the deliberate recovery
fault-trigger branch and ordinary screen serializer/runtime persistence branch
are **unfinished, Daybreak-only work**. Their private source candidates remain
unaccepted; no new persistence runtime result is established. Non-Daybreak
ChatGPT models must not continue or delegate either branch. Follow the
[restriction record](../unfinished-daybreak-only-work-2026-10-25.md); separate
consequential literature and synthesis remain authorized. This changes who
may continue the unfinished work, not its scientific evidence or ranking.
Keep recovery, diagnosis, applied
repair and verified continuation separate, with complete R06 work accounting.
The [search ledger](nu-background-searches-2026-09-30.md#2026-10-25-integration-s312-replay-based-debugging-and-repair)
records the reused once-only ADI audit and the separate bounded ImGui audit.
No new candidate, participant or native execution occurred; other B01–B12
coverage gaps and R02/R10/R12 returns remain in force. These findings improve
the comparison's definition without establishing Nu's empirical advantage.

## 2026-10-26: Practitioner evidence and diagnostic value

The [S180 complete selected reading](full-reading/S180-practitioner-beliefs.md)
closes an accessible primary-method gap for R14/R15. It retains favorable
retrospective associations and conditional contrasts while distinguishing
handbook-selected propositions from beliefs actually elicited from participants.
Training-task observations do not establish current Nu demand, causal language
advantage or prospective guidance. The selected paper is fully read; publisher
body, handbook originals and actual artifact-to-publication run correspondence
remain unresolved. Its separate independent arithmetic check failed before
reading data and remains unfinished; do not count it as reproduction.

The [R14 evidence table](../nu-practice-and-task-provenance-2026-10-11.md#match-the-evidence-to-the-kind-of-claim)
now distinguishes requests/preferences, demonstrated capability, comparative
benefit and population prevalence. The [R04 diagnostic reconciliation](../nu-research-study-designs-2026-10-08.md#diagnostic-evidence-and-the-maintainers-decision)
uses completed P08/S72/S231 evidence to specify the practical convention
question and valid countercases. These are documentation and literature
contributions, not new engine results or benefit estimates.

The strongest remaining work is still a consequential practical comparison
and its actual access, outcome and total-work evidence. S182 is a conditional
unread follow-up, not an automatic quota. Broader discovery and named access
gaps remain open. Current [storage](../workspace-integrity-return-2026-10-26.md)
and [Daybreak eligibility](../unfinished-daybreak-only-work-2026-10-25.md)
restrictions apply independently; neither turns unavailable evidence into an
adverse scientific result or resumes returned construction.


## 2026-10-26: R04 historical-task and reference boundaries

The [two-site source-history audit](../nu-r04-history-task-audit-2026-10-26.md)
changes R04/R14's task-eligibility rule: separate an external API change from
a required application-local rename and from the maintainer's chosen patch.
Retaining a local name can satisfy event adaptation, so extra enumeration edits
cannot be assumed from a historical diff alone. Neutral body/lifetime changes
and an out-of-match gravity repair remain real maintenance evidence. The
inspected projectile lineage supplies no case addition after the command's
introduction; authored positive extensions retain their authored status.

Breakout's score addition and later change from a constant to the actual state
scrutinee further require independent reference/retained-behavior validation.
No failure was reproduced, compiler diagnostic observed or candidate effect
estimated. This updates the [D1 proposal](../fsharp-domain-evolution-research-proposal-2026-09-16.md)
and study designs without another full-paper credit or representative-workload
claim. The literature checkpoint remains 289; broader research, Daybreak-only
work and returned constructions remain unfinished under their separate limits.

## 2026-10-26: R04 evaluator eligibility and authored scope

The [oracle audit](../nu-r04-oracle-eligibility-audit-2026-10-26.md) identifies a
specific B02/B12 measurement dependency. The successful pause references share
the same case/model/control organization and local-pause schedule; their probe
checks those choices directly. That fixed-source evidence is preserved, but it
does not validate a final evaluator for every correct reorganization D1 allows.
A future behavioral task must distinguish actual compatibility obligations from
incidental reference structure. A successor that needs no union extension
remains eligible unless a declared public contract requires one; missing the
predicted diagnostic is not grounds for removing the assigned attempt.

Current preparation therefore retains the authored pause/lifecycle question,
with bounded transfer and no representative-workload claim. The next dependency
is an evaluator/ordinary-access boundary that admits the promised alternatives,
not another warning demonstration. No candidate or runtime ran. A separate
bounded review selected no additional primary reading among the named gaps
inspected for current decisions; S182 remains conditional and opening-only.
Neither this disposition nor the unchanged 289-work reading count completes
the whole-background survey. Model, storage and returned-gate restrictions hold.

## 2026-10-26: S180 bounded numerical reconstruction

The [independent correlation check](full-reading/S180-correlation-reconstruction.md)
now completes its declared 150-cell disposition: 146 computed and four
uncomputable coding-time cells, with no row deletion. For the declared broader
`ActMin` metric, the significance-to-zero operation replaces 35/50 coefficients
and yields exact-zero medians in four of five language groups. The B3 positive
associations remain; none of its 50 coefficients is replaced by the rule.
The arithmetic therefore substantiates the earlier static measurement concern
while retaining favorable associations and the incomplete sensitivity groups.

This new environment is identified and independently reviewed at its bounded
scope. Its B4 operation order is algebraically, not necessarily bitwise,
equivalent to the archived expression; possible tie effects remain unquantified.
The actual publication run, full Scott-Knott reproduction, journal edition and
causal practice recommendations remain unresolved. R14 can use this as a
checked example of why metric definitions and reporting operations belong in
the evidence contract. It does not supply Nu benefit or another independent
study. The reading count stays 289; both earlier setup failures and the A:
stop remain preserved, and no restricted/returned native branch was reopened.

## 2026-10-26: R04 behavior, compatibility and unknown outcomes

The [authored behavioral contract](../nu-r04-behavioral-contract-2026-10-26.md)
now chooses ordinary standalone MMCC, a declared P pause/resume interface,
retained progress, sequential quit/fresh play and independent effect evidence.
Private state cases, records, entity names and local/global pause scheduling
may differ. The initial source convention remains the treatment even when a
successor avoids a new union case. Q2's stronger next-loop/same-pass requirements
remain separate rather than hidden final requirements. The accompanied probe
does not validate this standalone environment or ordinary access.

Completed S226/S227 readings support visual feedback and separately scoped
final judging while delimiting private-state, phase, audio and event coverage.
Their useful results motivate complementary observations, not a screenshot-only
claim of complete pause correctness. The contract now distinguishes verified
completion, observed failure and unresolved measurement. Logical all-assigned
outcome bounds expose the consequence of missing observations without calling
them candidate defects or confidence intervals.

This resolves a desk-level task/evaluator boundary. Actual ordinary input,
independent effect/timing observations, comparison across a differently
organized correct implementation, resources and candidate allocation remain.
No paper body, runtime, candidate or restricted branch was opened. The 289-work
reading count is unchanged; the broad survey and practical value question are
unfinished. Another repetition of the fixed compiler probe or this contract
would not resolve the remaining observation dependency.

## 2026-10-26: public requests and ordinary configuration before mechanism value

The [expanded R14 source frame](../nu-public-request-provenance-2026-10-26.md)
adds requests by accounts outside the two dominating the earlier issue queries.
The observed unit is an issue/account, not an independent adopter or game.
Eight selected textual threads expose concrete fill-direction, camera,
deployment and game/editor text needs. They include a project idea set aside,
a deprioritized port and a reported successful Unicode render/measurement
repair. These dispositions matter more for task eligibility than open/closed
labels or another count of requests.

At the inspected source revisions, Nu's built-in fill-bar path fixes the fill
to the left edge; the pinned Godot control provides direction configuration,
including a layout-dependent horizontal convention. A whole-workflow comparison
must allow that ordinary facility and count any necessary Nu extension and
both packages' setup/integration/verification. No rendering equivalence or
measured work advantage follows from the source. The feature request does not
itself supply an existing direction union for the D1 treatment; a newly authored
representation or follow-on extension must keep that provenance.

This is new bounded practice/source evidence, not another paper reading,
population survey or automatic new study. R01's practical workflow and common
outcome still govern promotion. Deployment and localization are conditional
requirements, while game text, editor entry and advanced typography remain
different outcomes. Native validation and actual value remain unresolved;
storage/model restrictions, returned gates and the 289-work count are unchanged.
