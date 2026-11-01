# R04 oracle eligibility and authored scope, 2026-10-26

**Decision:** retain the completed pause probe as evidence for its fixed reference
implementations. It is not yet a final evaluator for all the correct source
organizations permitted by [D1](fsharp-domain-evolution-research-proposal-2026-09-16.md).
Continue R04 preparation as an explicitly authored, within-implementation
maintenance question. The inspected histories do not establish a representative
population of case-extension requests. This decision changes the proposal's
scope and next dependency; it creates no candidate task, run allocation or
replacement for the frozen probe.

## What the existing checks establish

The [actual-project diagnostic record](nu-application-diagnostic-feasibility-2026-10-15.md)
establishes the selected warning-only contrast after an evaluator-authored
`Paused` extension. The [pause runtime record](nu-pause-runtime-feasibility-2026-10-15.md)
establishes matching fixed observations for two baseline references and two
completed pause references, plus detection of five declared faults. Both pause
references use the same new case, controls, model layout and local-pause policy.
They differ at the selected explicit-versus-wildcard clause. Their success
does not validate every implementation that could meet a behavioral request.

This distinction matters because D1 permits safe reorganization and correct
catch-alls. A feature request to pause gameplay does not, by itself, require a
particular union extension, model field or private entity name. A required
public interface can legitimately constrain those choices, but it must be an
explicit part of the task contract, with an owner and reason, before outcomes.
The [history audit](nu-r04-history-task-audit-2026-10-26.md) establishes the same
distinction for external event changes and optional local renames.

## Source-bound observations

The following are static observations of this repository at
`782be65a0ca319683a303908e372c5f86a8a7868`. They are not new executions or observed
candidate failures.

| Binding in the published probe | Evidence | Consequence for a later maintenance evaluator |
| --- | --- | --- |
| The probe compiles against the application and reads typed `Gameplay` values. | [Probe.fsproj, lines 8-15](https://github.com/Happypig375/interactive-software-evolution/blob/782be65a0ca319683a303908e372c5f86a8a7868/experiments/nu-r04-pause-runtime/Probe.fsproj#L8); [Common.fs, lines 21-39](https://github.com/Happypig375/interactive-software-evolution/blob/782be65a0ca319683a303908e372c5f86a8a7868/experiments/nu-r04-pause-runtime/Common.fs#L21). | `equalModel` compares a listed observation projection, including the named state and selected model fields. It is not structural equality of every possible successor record, nor an implementation-independent state interface. |
| Pause and resume require the particular `Paused` and `Playing` cases. | [PauseProbe.fs, lines 156-190](https://github.com/Happypig375/interactive-software-evolution/blob/782be65a0ca319683a303908e372c5f86a8a7868/experiments/nu-r04-pause-runtime/PauseProbe.fs#L156). | An implementation using a separate pause flag cannot simply be passed to this unchanged oracle: its source/type interface and state assertions must be compatible. Even if the old cases remain available, a paused implementation retaining `Playing` would fail the stated equality predicate. This is a conditional source consequence, not an implemented or validated alternative. |
| Control delivery and projection checks depend on fixed handles, names, layout and text. | [PauseProbe.fs, lines 63-65](https://github.com/Happypig375/interactive-software-evolution/blob/782be65a0ca319683a303908e372c5f86a8a7868/experiments/nu-r04-pause-runtime/PauseProbe.fs#L63); [Common.fs, lines 129-184](https://github.com/Happypig375/interactive-software-evolution/blob/782be65a0ca319683a303908e372c5f86a8a7868/experiments/nu-r04-pause-runtime/Common.fs#L129). | The exact entity-name set can reject additional or differently organized entities even when those differences are allowed by a future task. Fixed UI requirements may remain, but private names and helper structure must not become hidden obligations. |
| The paused interval requires ten positive Update/TimeUpdate pairs and twenty advancing handlers. | [PauseProbe.fs, lines 88-105 and 166-179](https://github.com/Happypig375/interactive-software-evolution/blob/782be65a0ca319683a303908e372c5f86a8a7868/experiments/nu-r04-pause-runtime/PauseProbe.fs#L88). | This is evidence for local application pause under an advancing engine. It cannot silently become a mechanism-independent pause requirement. A future task must declare whether engine advancement is a justified common constraint or whether other correct scheduling policies are eligible. |
| Preparation constructs the specific case, transition, TimeUpdate guard, content condition and control. Baseline fixtures also use typed model setters. | [prepare.py, lines 132-188](https://github.com/Happypig375/interactive-software-evolution/blob/782be65a0ca319683a303908e372c5f86a8a7868/experiments/nu-r04-pause-runtime/prepare.py#L132); [BaselineProbe.fs, lines 32-53 and 96-112](https://github.com/Happypig375/interactive-software-evolution/blob/782be65a0ca319683a303908e372c5f86a8a7868/experiments/nu-r04-pause-runtime/BaselineProbe.fs#L32). | Reference construction and fixture injection are controlled preparation work. They are not ordinary candidate behavior, independent evidence of task demand, or a ready interface for arbitrary successor schemas. |

These bindings are appropriate to the original fixed-source mechanism check.
The issue is reuse under a broader admissibility rule, not a retrospective
failure of that check. Its observed faults, setup amendment, failed attempts,
audio boundary and input limitations remain unchanged. No test is removed or
weakened by this audit.

## Selected preparation scope

The next R04 preparation concerns an **authored behavioral change**, using the
already specified pause/resume, retained progress, quit and fresh-play
obligations as its starting family. It is not yet a benchmark prompt or an
accepted ordinary-input protocol. The narrower accompanied probe and the
separate standalone [pause/exit contract](nu-pause-exit-contract-2026-10-11.md)
have different input and transition boundaries; neither silently validates the
other. Broader task families remain in the agenda, with their existing
provenance and feasibility limits.

Keep the treatment at the assigned initial source convention. If a candidate
can satisfy the eventual behavioral and compatibility contract without adding
a union case, that is an eligible strategy. Preserve its original assignment;
do not exclude it for failing to generate the predicted diagnostic. Conversely,
if a future task genuinely requires a new public case, record that owned
interface obligation separately from the behavioral obligations. Requiring a
case solely to elicit FS0025 would answer a constrained authored question and
must be labeled that way.

This scope can eventually estimate a conditional maintenance effect for the
declared tasks, model and tool policy. It cannot establish industry task
frequency, Nu-wide adoption value, or the effectiveness of human steering.
Repeated agent calls cannot supply the missing task population. The current
positive evidence remains mechanism feasibility; no maintenance effect is
measured here.

## Remaining evaluator dependency

Before any candidate allocation, a future feasibility packet must:

1. Distinguish required behavior and actual compatibility interfaces from
   incidental reference fields, constructors, names and scheduling choices.
2. Establish common, independently checked observations for every admitted
   implementation strategy. A candidate-provided success flag or comparison
   with its own model is not sufficient independent evidence. Any necessary
   fixture/observation mapping is preparation work with an explicit cost and
   review boundary, not an unrecorded repair after seeing final scores.
3. Validate at least one correct implementation that changes a relevant
   representation or organization, alongside failures of the required
   behavior. The existing explicit/wildcard pair validates the clause contrast;
   it does not alone validate this broader admissibility promise.
4. Distinguish a demonstrated behavioral failure from an evaluator-interface
   mismatch or an unobserved obligation. Neither gets completion credit without
   evidence, but an unsupported measurement must not be reported as a semantic
   defect. Freeze the disposition and feedback rules before candidate outcomes.

The public input route, ordinary candidate access, complete oracle coverage,
resource limits and study allocation remain unresolved. This is a desk-level
acceptance boundary, not authority to build an adapter, alter the frozen
references or run a candidate. A: remains stopped; R02/R10/R12 remain returned;
R03 native-001 remains terminal. The unfinished
[Daybreak-only branches](unfinished-daybreak-only-work-2026-10-25.md) were not
investigated or delegated.

## Coverage and records

The parent inspected Common.fs lines 1-90 and 129-185; PauseProbe.fs lines 1-110
and 145-214; BaselineProbe.fs lines 32-55 and 96-112; prepare.py lines 132-188;
and all 23 lines of Probe.fsproj. Filename and identifier searches preceded
these reads. This is selected source coverage, not a review of every probe,
host, build or runtime path. Exact Git objects, SHA-256 hashes, prospective
scope and read ranges are retained privately in the current C: preservation
root under `value-preparation/r04-oracle-eligibility-20261026/`.

The audit reuses completed paper readings and published observations; it adds
no full-paper credit or reproduction. A parallel bounded review of named
remaining literature gaps selected no additional reading for the decisions
it inspected. S182 remains conditional and opening-only; this is not a claim
that the broad literature survey is complete or that no other consequential
source exists.

The once-only source-decision segment is `r04_oracle_eligibility_20261026`:
five included repository files, no excluded/skipped decisions or missing
reasons, and an untruncated report with retrieval_unlinked=false. The
answer-scoped retrieved count is null. These counts describe the source audit,
not scientific papers or independent studies.
