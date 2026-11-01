# Nu agent information, feedback and execution boundaries

**Prepared 2026-10-11.** This supplies R08's information/accounting contract as support for R02/R04 and any later agent extension of R03. It follows the [study packet](nu-research-study-designs-2026-10-08.md), [R05/R06 observations and costs](nu-source-contracts-and-scenarios-2026-10-11.md), and [R09 sequence policy](nu-change-sequence-contract-2026-10-11.md). It specifies a proposed workflow; no candidate, fixture, runtime observer or adapter is constructed. [PLAN](../PLAN.md) retains all holds and zero new allocation.

## What the retained controller actually supports

The retained E3a controller is useful evidence about an existing implementation, but it does **not** implement the packet's proposed ordinary source-navigation/build/test agent workflow. Inspection uses repository pin `065e3f931400300f24216e72164c2e8e7a90a7f7`, through Git objects without restoring or running the sparse-checkout engineering tree. This is not a current provider/client capability test.

| Inspected source | Established boundary and consequence |
| --- | --- |
| [Candidate instructions](https://github.com/Happypig375/interactive-software-evolution/blob/065e3f931400300f24216e72164c2e8e7a90a7f7/protocols/workstream-e3a-v1/candidate-instructions.md) and [specification](https://github.com/Happypig375/interactive-software-evolution/blob/065e3f931400300f24216e72164c2e8e7a90a7f7/protocols/workstream-e3a-v1/specification.json) | E3a gives inline approved source/contracts and no shell, build, test, network or other candidate tools. It accepts full-file JSON replacements, root-level language-specific names, at most eight source files and restricted project changes; deletion/rename is unsupported. These are historical OrderFlow choices, not a validated Nu workspace/edit contract or generic language restrictions. |
| [Replay and parser](https://github.com/Happypig375/interactive-software-evolution/blob/065e3f931400300f24216e72164c2e8e7a90a7f7/src/ise/e3a_codex.py#L59) and [generation boundary](https://github.com/Happypig375/interactive-software-evolution/blob/065e3f931400300f24216e72164c2e8e7a90a7f7/src/ise/e3a_codex.py#L105) | The adapter ignores a previous response ID and serializes visible replay for a fresh launch. The parser requires one started/completed turn and accepts reasoning/agent-message items, rejecting other item types. It is not an implemented tool loop; deleting a parser check would not establish tool authority, isolation or accounting. |
| [Submission and feedback](https://github.com/Happypig375/interactive-software-evolution/blob/065e3f931400300f24216e72164c2e8e7a90a7f7/src/ise/workstream_e3a.py#L211) | Replacement/project checks enforce the OrderFlow envelope. The [formatter](https://github.com/Happypig375/interactive-software-evolution/blob/065e3f931400300f24216e72164c2e8e7a90a7f7/src/ise/workstream_e3a.py#L284) groups diagnostic lines, deduplicates exact blocks and sorts errors first with lexical ordering. It preserves multiline block context and marks omissions, but this is not a general order/multiplicity-preserving trace format. |
| [Trajectory controller](https://github.com/Happypig375/interactive-software-evolution/blob/065e3f931400300f24216e72164c2e8e7a90a7f7/src/ise/workstream_e3a.py#L371) | Up to two repairs follow the initial submission; stopping depends on development results, resources and protocol/accounting conditions. No hidden score enters this loop. Failed or ambiguous responses remain in the trajectory. These useful boundaries do not authorize their reuse with new tasks or allowances. |
| [Batch scoring](https://github.com/Happypig375/interactive-software-evolution/blob/065e3f931400300f24216e72164c2e8e7a90a7f7/src/ise/e3a_runner.py#L147) | Holdouts are evaluated after the controller returns, first submission before terminal submission, only while the same trajectory deadline remains. Thus a source may lack a final observation because time is exhausted; scoring the first endpoint can consume time available for the terminal one. This is a source-supported possibility, not a new claim that a historical result was affected. Reported slot elapsed time includes scoring. |

The specification retains historical authorization flags and five/72 ceilings. **Current PLAN authority overrides them for this assignment: allocation is zero.** Do not activate an old JSON flag, reuse an unused balance, reinterpret old results or weaken the preserved backend/transport/security choices.

Current [official OpenAI documentation](https://learn.chatgpt.com/docs/non-interactive-mode) describes JSONL item types including commands, file changes and tool calls; it describes ephemeral mode as avoiding persisted rollout files. These are distinct facilities. They do not establish no-tools enforcement, absence of other supplied context or compatibility with this pinned customized client. No current catalog, CLI, model, authentication or count probe was run, and no model/backend migration is proposed.

## The proposed candidate information contract

Keep R08 as support for the leading mechanism/maintenance questions unless an actual tool/information treatment justifies a separate study. Within R02/R04, the intended source/package comparison should receive the same declared access policy; different chosen actions and consequent observations remain possible. Equal access does not mean forcing identical token counts, file visits or returned diagnostics.

| Information or operation | Proposed candidate access | Research/evaluation boundary |
| --- | --- | --- |
| Initial program and requirement | Assigned predecessor revision, exact current request, active retained requirements, ordinary documentation and declared development examples. Record file/version identity and whether the failing entity/event is identified. | Exclude successor solutions, the other arm, comparative predictions, final scoring implementation/results and this research workspace's governance/evidence. A normal upstream coding instruction is a declared input, not silently equated with research instructions. |
| Source navigation and editing | Ordinary declared reads/searches and legitimate changes within the selected application boundary. Preserve safe helper extraction, reorganization and correct catch-alls where behavior permits them. | Specify directories, project/asset changes and valid deletion/rename behavior for the actual Nu task. Do not silently import E3a's root-only replacement envelope or reward similarity to a reference patch. Actual supported access is unverified. |
| Compiler/build output | Current output from the submitted source and fixed build/warning policy, including useful locations and context within the declared feedback policy. | Record source, compiler/configuration identity, produced output, delivered output and any omission separately. A potential FS0025 site, an emitted warning, its delivery, its use and correct behavior are different observations. |
| Development tests | Declared examples and candidate-created checks under the common resource policy. Candidate-created tests are ordinary work whose editing/execution cost is counted. | They are fallible development aids. They cannot replace independent final behavior obligations, mutate final scoring or serve as their own authoritative oracle. |
| Runtime observation and input | Only predeclared, supported operations with source/instance, input sequence, phase and scope recorded. Use the selected task's R05 contract. | An API in Nu source or a maintainer's privileged local access is not verified candidate transport. An observer must expose observations, not a hidden-reference diagnosis or solution. GUI/history access remains conditional. |
| Failure report and assistance | Freeze whether the starting report supplies an entity, event, location or expected/actual example. Operational intervention is logged with content, contributor and cost. | Extra localization changes the task. Unplanned human repair is a separate assisted outcome; preserve the original attempt. R21 steering effectiveness remains deferred. |
| Final evaluation | No candidate access and no feedback into its stopping, repair, later assigned tasks or sample selection. | Score the frozen submission independently after the candidate stops, with a separate declared evaluation resource boundary and observation missingness. |

The initial packet and subsequent visible observations must be recoverable by version/hash and sequence. Record any truncation, search ranking, image scaling, data projection, automatically loaded instructions or summaries that can change delivered information. Do not infer receipt from a file merely being present, or understanding from a tool call being logged. Deliberate context/summary/tool changes are treatments needing their own comparison, not harmless measurement plumbing.

For D1, the source treatment can itself change compiler output after a new domain case. Keep the effective warning policy and opportunity for build feedback common; do not suppress that consequence to manufacture equal outputs. Conversely, do not add a warning or diagnostic to one arm unless it is part of the declared source/tool treatment. Preserve the no-new-case task and valid-default cases, where enumeration may add work without behavioral benefit. Conditioning the main contrast on receiving a warning, successful compilation or retaining the assigned style would change the estimand.

## Temporal feedback needs a different preservation rule

The current E3a formatter is suitable only within its validated diagnostic scope. If Nu events are encoded as repeated diagnostic-like blocks, sorting or deduplication can remove the very order or multiplicity the task requires. If the entire trace is one block it may retain order; **not every trace is necessarily altered**. The relevant gap is absence of an established temporal-preservation contract, not an executed formatter failure.

For eventual Nu development observations, preserve event sequence, occurrence count, entity/lifetime identity, phase/time basis, input provenance, observation window and explicit omitted ranges. Separate compiler diagnostics from structured behavioral observations. A count can help summarize a burst, but cannot establish which event occurred first; one unique event description cannot establish that an effect happened exactly once. Do not silently turn an ordered log into a set or use a sorted diagnostic packet as a temporal oracle.

The [pause/exit contract](nu-pause-exit-contract-2026-10-11.md) provides a concrete boundary: a pause request, its later effective phase, quit/navigation and fresh play are different observations. Development feedback may expose declared examples, while final independently specified obligations also test retained behavior. A final-test-selected counterexample must not become a repair hint. Phase-correct input and observation remain separately held feasibility work; this document creates no trace schema implementation or test cases.

## Stopping, evaluation and resource accounting

Declare candidate stopping by the resource allowance, its explicit submission/stop decision, allowed development conditions and existing safety/accounting stops. A development pass may be a predeclared stop condition; it does not imply final correctness. Preserve the last submitted artifact and the exact accepted workspace, distinguishing invalid submission, unapplied changes and any earlier correct state. No hidden score chooses the submitted endpoint or a favorable retry.

For the proposed studies, allocate **final evaluation resources separately from candidate repair resources**. This prevents candidate budget exhaustion from automatically suppressing observation and prevents evaluation of an earlier endpoint from consuming the terminal endpoint's allowance. Evaluation may still time out or fail; retain unknown obligations and their cause without awarding success or labeling unobserved behavior incorrect. Evaluation spending and delay remain real costs, reported separately and in any declared total. This is a future design rule, not a modification or rescoring of E3a.

Report authored source/packet bytes, delivered context and cumulative model traffic as different quantities. Count tool attempts, build/development execution, input/observation work, replay/summarization if allowed, failed requests, retries if later explicitly allowed, and all known model usage. Keep generation requests, client launches and tool operations distinct. Cached/reasoning subsets must not be added twice; unknown subscription expenditure remains unknown rather than converted to API dollars or zero. Old post-turn alarms are not hard provider caps. Numerical limits and allocation require later explicit decisions; this contract borrows none from E/H.

Preserve assignment and all attempted outcomes, including blocked infrastructure, unsupported observations, ambiguity and rescue. Paired tasks share substantive difficulty; repeated calls do not supply independent applications. Distinguish information assigned before work from behavior observed during it. Resource use, edits and feedback can explain a result without being post-treatment covariates used to manufacture a pure mechanism effect.

## Closest reconstructed methods and readiness

[P08](literature/full-reading/P08-type-error-ablation.md) supplies favorable richer-current-diagnostic results alongside task reversals, and separates feedback content from type checking. Its shared feedback/evaluation tests do not establish an independent final oracle; its retry accounting motivates recording every attempt. [P12](literature/full-reading/P12-tocs.md) shows that elicited architecture maps/probes can change the agent's work and that replay/full-information comparisons alter several inputs. Do not inject research questions into candidate context to measure supposed understanding. [S42](literature/full-reading/S42-stream-debugger-comparison.md) supplies the human package-by-initial-information reversal; it motivates an explicit information boundary without predicting the same agent effect. These completed notes are reused, not reread publications or new empirical results.

R08 now has an explicit information, temporal-feedback, stopping and accounting specification. The remaining execution dependency is concrete: reconcile the intended tool/edit/observation authority with the retained no-tools controller and actual Nu access while preserving the required backend, transport and security decisions. A constrained no-tools Nu question would be a different study and must be named as such; silently imposing it is not completion of the proposed workflow. No new adapter, proxy, model worker, OAuth staging or live probe is authorized.

The next action for this contract is a **separate workflow/feasibility decision**, followed only under later authority by minimal necessary validation of source/edit access, common diagnostics, phase-correct observations, information isolation and independent scoring. S227 v2 becomes necessary if its updated GUI-agent/playtesting method is selected; nothing here adopts that method. Continue other consequential literature or task-practice dependencies while these execution gates remain held. Documentation and existing engineering checks do not establish a Nu agent effect or complete the broad survey.

## 2026-10-15: revised GUI-playtesting method

The [complete S227 v2 reading](literature/full-reading/S227-continual-gui-playtesting-v2.md)
resolves the preceding edition-reading dependency. It retains favorable
Play2Code rubric results and adds full-benchmark human agreement and two
alternative judges for one generation backbone. Its development GUI playtester
receives a generated guide, screenshots and memory without the final rubric;
the final rubric judge is a separate role after stopping. This supports the
information separation above as a reported method. The unreleased scaffold,
prompts, parser and traces prevent independent verification of that isolation.

Retain complete ordered observations even if a summary and fix list are useful
candidate feedback. Cross-task memory requires a declared task order/reset
policy. The approximate $5/$12/$17 inference-cost sample does not cover total
work or establish equal resources. Gain-group trajectories and the human plot
remain inconsistent with parts of the text; early-stop later-round populations
remain unspecified. Those comparisons cannot set a Nu effect prediction.

Screenshot/browser interaction is useful complementary evidence, but does not
establish fixed-tick observation, entity identity, event multiplicity, audio or
world-history access. Continue actual Nu tool/phase-access and independent-score
feasibility under PLAN's current local-work authority. Candidate/model
allocation, backend, transport and security decisions remain separate. This
reading neither executes a GUI agent nor validates the proposed Nu workflow.

## 2026-10-25: an agent-repair method with a replay boundary

[S312 ADI](literature/full-reading/S312-adi-agent-repair.md) now supplies a
completed selected method: ordinary file/shell, low-level PDB and function-trace
configurations under common paper-reported benchmark/model/budget conditions.
Their deposited prompts differ materially; this is a bundled workflow comparison.
Reported
held-out patch resolution favors ADI in all four models; PDB is mixed. Agent
self-reported success is a different, more favorable endpoint in the deposit.
The independent final score must therefore remain separate from development
feedback and stopping, as required above.

The added condition includes rerunning an authored reproducer, tool prompts
and navigation as well as trace information. It is not passive retained-history
access. Future comparison must count reproduction failures, reruns, interface
construction and verification and retain full task denominators. The artifact
cannot reconstruct missing comparator trajectories or resolve the temperature
setting used in each run. This paper supports a method and a bounded result;
it neither validates Nu tool access nor allocates any candidate/model run.
