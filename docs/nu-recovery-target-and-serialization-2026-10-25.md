# R03/R06: recovery target and serialization boundary

**Latest user restriction, 2026-10-25:** the later deliberate fault-trigger
investigation and ordinary screen serializer/runtime persistence investigation
are **unfinished, Daybreak-only work**. Non-Daybreak ChatGPT models must not
continue or delegate either branch. The [handoff](unfinished-daybreak-only-work-2026-10-25.md)
records their preserved, unaccepted preparation. All prospective source,
construction and execution steps below are subject to that restriction and
the existing returned gates; they are not current instructions to an
ineligible model. The earlier reviewed analysis retains its stated scope.

Integrated 2026-10-25 from the reviewed October 23 desk analysis. The practical
question is recovery of useful editing-session state after a user-code
exception. Nu #151 supplies the maintainer rationale; the
[history-demand record](nu-history-question-access-2026-10-18.md#2026-10-23-recovery-demand-and-the-next-comparison)
preserves its historical trigger and current-task limits. This is source
preparation, not a new execution, repair result or accepted experimental
protocol. The [terminal native-001](nu-passive-access-observation-2026-10-23.md)
and returned R02/R10/R12 constructions remain unchanged.

## Select the target before selecting the recovery route

The ordinary pinned Gaia workflow already provides snapshots, Undo and an
explicit restore point. Showing that history can restore a represented
checkpoint would establish feasibility. A useful improvement over that
workflow must preserve required work or improve recovery reliability/effort,
including the additional checkpoint, inspection and integration work.

Keep three roots separate: **K**, the last actual editor snapshot; **G**, the
last good simulation state before the fault; and **F**, the handler-entry
represented root before any recovery switch. These names do not recover the
missing roots of the old stale-position episode, and this desk pass creates
no new roots.

All source statements below concern Nu
`064f7ae92a8506689cd91aff5e6804a375d6ef3d`.

| Existing route | State and history behavior | Consequence for a comparison |
| --- | --- | --- |
| Editor snapshot | Stores `world.CurrentState` in `Pasts` and clears `Futures`. | Editor operation boundaries are not an every-tick execution trace. |
| Advance/Halt | Snapshots before toggling advancement. | Recovery may lose progress since advancement began. K need not equal G. |
| F7/menu restore point | While advancing, halts, snapshots and advances again; the source also plays a sound before snapshotting. | This is an existing ordinary alternative with capture, effects and work to count. |
| Outer exception recovery | `tryUndo` switches to the head of `Pasts`, temporarily puts F in futures, then the handler clears futures and halts the switched world if advancing. | It targets K and removes ordinary redo access to F. `wasAdvancing` describes the switched root, not an independent observation of F. |
| Dialog Hard Rewind | Calls `tryUndo`, ignores its Boolean result and dismisses the exception flag; a successful undo retains F as a redo future. | Dismissal does not prove that a past root existed or restoration succeeded. |

The source boundaries are [snapshot](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L505-L508),
[Undo](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L617-L640),
[restore point](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L889-L895),
[Advance/Halt](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L1395-L1398),
[dialog](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L4260-L4279)
and [outer handler](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L4517-L4537).

With no past root, including the imperative-mode path, the outer handler logs
and returns failure; the inspected branch does not establish editor reentry
or normal cleanup. Failure during state switching or recovery is also not
covered by a guarantee. Capture F before the handler discards it if the
question requires it. Do not infer it from a post-recovery log.

Restoring a usable halted K does not repair the code. The same trigger can
fail again. Session recovery may require K plus a declared safe continuation;
a repair endpoint additionally requires a correct code change and continuation
through the failing behavior. Lost progress, recovery, diagnosis and repair
must retain separate outcomes.

## Soft Rewind is a source prediction needing a reachable case

Each `imGuiProcess` invocation binds a fresh local `worldStateOld` from
`world.CurrentState`. Its UI-work catch stores only the exception; the dialog
runs on a later invocation and receives that invocation's entry root. Soft
Rewind switches to the passed root. The inspected implementation therefore
does not establish retention of the faulting invocation's entry root.
[Entry and catch/dispatch source](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L4282-L4402).

This predicts a possible distinction if UI work changes represented state
before throwing. It does not prove that an ordinary reachable operation commits
such a change to the caller before the exception, or that no intervening state
switch occurs. In functional code, a successor computed inside a throwing
callee need not have been assigned to the caller's mutable world. A source
call-chain check must settle that boundary before a concrete fault comparison.
Native/shared effects and later eye-state processing are separate. No runtime
bug, universal failure or successful competing rollback is inferred here.

## The reconstruction comparator must include the screen model

Save Group calls `World.writeGroupToFile`. It serializes the group's properties
and eligible entities, not its parent screen. Breakout's seven-field Gameplay
value lives in `Screen.Model`, including game time/state, paddle, ball, bricks,
score and lives. Thus a group-only save is not a complete checkpoint of that
Gameplay value. Group loading also rejects a protected existing group; this
source fact does not establish the actual protection value in a later task.
[Group serializer](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/World/WorldGroup.fs#L228-L256),
[Gameplay model](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Projects/Breakout%20Mmcc/Gameplay.fs#L183-L215)
and [load wrapper](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L1183-L1222).

The existing `writeScreenToFile`/`readScreenFromFile` APIs are a stronger
candidate: they include screen properties and eligible groups. The default
nonpersistent-name set does not exclude Model, but dynamic persistence filters,
symbolic conversion and actual model roundtrip remain to be checked.
`readScreen` calls `World.addScreen true`: the Boolean means `mayReplace`, so
an existing-address ScreenState can be replaced. Only a newly added screen is
registered. The original independent review's contrary replacement claim was
incorrect; its retained addendum corrects it.
[Screen serialization](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/World/WorldScreen.fs#L257-L331),
[replacement implementation](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/World/WorldModuleScreen.fs#L462-L481)
and [default persistence exclusions](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/Core/Constants.fs#L114-L163).

Replacement is not complete restoration. The comparator must bind destination
identity, replacement versus destruction/fresh-world policy, registration,
children absent from the descriptor, selection, zero-processing and failure
rollback. `readScreen` contains no local transaction restoring the pre-import
root on failure. Breakout selection can initialize new gameplay and generated
brick names/colors, so import/selection order matters. The inspected screen
menu has no screen-save command; this is a scoped menu observation, not an
exhaustive search of editor/API routes.

The demonstrated B0/B1 model-symbol reconstruction is another, narrower
candidate. Count its helper installation, common clear/content alignment and
verification, retaining its native/effect limits. Ordinary Interactive
evaluation itself snapshots, including serializer calls. Using serialization
there does not establish a history-free-memory arm; both arms must account
for implicit retention.

## Eligibility and falsification

A distinct comparison must name the exception domain and actual checkpoint,
state the permitted lost-work policy, give both routes eligible ordinary inputs
and tools, and verify recovery plus continuation against that policy. Capture
G/F only if required, but do not silently substitute K for them. Preserve
no-past, repeated-fault, partial import, lost progress and invalid-environment
outcomes. Count setup, checkpoint capture, retention, access, restart,
reconstruction, verification and failures; keep overlapping wall time, machine,
AI/tool and active-human work separate.

If ordinary recovery meets the same required outcome with equal or lower total
work, the proposed addition has no demonstrated practical advantage on that
task. If a faster route drops required progress, it fails the common outcome.
An allowed reset remains valid. A new checkpoint policy cannot be compared only
against an artificially weakened baseline that withholds Gaia's existing F7
facility.

No exact current trigger, captured root pair, complete screen-file procedure
or common final oracle is accepted by this note. A subsequent private source
candidate remains unaccepted. In response to the user's direction to avoid
flagged work, the parent stopped the deliberate fault-trigger investigation.
The subsequent ordinary checkpoint-persistence branch is also stopped and
unfinished under the user's Daybreak-only restriction. Its delegated source
candidate and historical input preparation remain private and unaccepted;
neither supplies a new export/import or runtime result. No consumed assignment
or returned construction gate is reset.

### Current preparation: ordinary checkpoint persistence

**Preserved unfinished brief; continuation is Daybreak-only.** The following
dependencies describe remaining work, not work authorized for a non-Daybreak
ChatGPT model.

The practical decision is which available route can retain a required
noninitial checkpoint for later continuation, and what complete work it needs.
Use the already specified B0 represented-state contract, under unchanged code
and functional mode. Its recorded witness has GameplayTime 149, score 100,
29 bricks and five lives; the actual oracle covers every declared model field,
logical key and projected property, not those summary numbers alone.
[B0 observations](nu-history-feasibility-2026-10-15.md#observed-b0-comparison).
The old process is closed, so a later fresh reconstruction must be labelled
as such; it cannot be a resumed old root.

| Available route | What is already supported | Remaining eligibility/work boundary |
| --- | --- | --- |
| Gaia history/F7 | Ordinary facility; bounded B0 recovery and B1 represented continuation observed in prior instrumented processes. | A new live checkpoint and ordinary access still need their own evidence. Count capture, retained payload, navigation and readiness. |
| Model-symbol reconstruction | Prior complete model/selected-projection reconstruction, with an explicit common absent-content setup when required. | Count acquisition, helper installation, initialization/selection ordering, content alignment and verification. Preserve the prior stale-initialization observation. |
| Screen-file API | Source writes screen properties and eligible groups; read can replace an existing-address ScreenState. | Actual model serialization, dispatch registration, children, selection and settled projection remain unverified. API availability is not a demonstrated ordinary UI workflow. |
| Group file | Existing scene/group persistence. | Eligible for a group-only requirement, but insufficient for this B0 outcome because it omits the parent gameplay model. Do not relabel a narrower valid use as a complete gameplay checkpoint. |

Before constructing the screen-file comparison, define the serialized scope
from an actual ordinary export and inspect it as data. Choose either a fresh
destination or an existing-address replacement explicitly; their registration
and child-cleanup obligations differ. Specify the screen-selection order so
`StartPlaying` does not silently replace the required model. Verification must
compare model and settled content at a halted boundary, then a declared normal
continuation with common input/time assumptions. Shared input or native/effect
state outside the file must remain outside the preservation claim unless
observed independently.

This is baseline eligibility work, not a new runtime protocol or an effect
estimate. An export that parses is not yet restoration, and restored model
values alone do not prove projected or native-state equality. Reuse the prior
[R06 scope/cost distinction](nu-recovery-cost-feasibility-2026-10-15.md#comparison-and-interpretation):
history and model files retain different payloads, and component timings omit
substantial setup work. Once a credible ordinary route meets the common
outcome, specify any useful improvement over it and evaluate its full added
work. Do not count another equivalent restoration witness as demonstrated
maintenance benefit.

## Provenance and review

Private `value-preparation/recovery-target-next/` retains eight source copies,
selected ranges, original draft/review, correction addendum and parent
acceptance. Seven copies matched prior PDB document hashes; original Gaia raw
source is distinguished from the modified research bridge. Corrected evidence
SHA-256 is `608d043d802533eaa821bbcbef1b4ad79687a8f569de947a6165ec1e8ed55bd1`;
parent acceptance is `e8ae7c43c8354c40d798144420d46c4bcaa22fdcb2b7c4016c8eaa8e39f8dc8d`.
This integration reuses that selected static-source coverage and historical
#151 evidence; it credits no new paper reading or runtime observation.
