# A public XState persistence decision: Showtime

The transfer search now binds a public application, a reported failure and a
specific persistence-policy change. It does **not** yet bind a demonstrated
machine-evolution failure or independent demand for cross-version preservation.
Retain this as a conditional case for the
[non-game transfer agenda](nu-status-quo-and-transfer-audit-2026-10-23.md#non-game-transfer),
alongside the stronger existing-application but different-scope alternatives
below. No application was installed, built or run.

## What is actually bound

In [Showtime issue #150](https://github.com/vishnujayvel/showtime/issues/150),
the owner reports losing an in-progress show's locked beats, lineup and current
act after relaunch. Machine changes, a date check and Electron storage scope
are proposed causes. These are hypotheses in a self-report, not our diagnosis.
The [repair PR #152](https://github.com/vishnujayvel/showtime/pull/152) adds
versioning and state-value validation. It identifies Claude Code generation,
and its manual same-day and next-day relaunch checks remain unchecked. Reported
passing tests are upstream claims; we did not execute them.

The pre-fix source is `74474089be9f4a8487cd3034c5d4c6a087765499`, and the
selected fix head is `5a4e415733e8048a146c84600f90d94fc7134c5d`. The intermediate
`ce92cba382e8fc6a0ea95532eb247289b9c6d05a` has the exact pre-fix parent.
The two persistence commits change the actor/loader and its tests, while
`showMachine.ts` is byte-identical across the selected endpoints. The package
declares XState `^5.30.0`; that range is not an exact resolved dependency pin.

| Boundary | Exact source policy |
| --- | --- |
| Old saved record | Stores `{stateValue, context, savedAt}` without a version. It is an application-defined partial record, not `actor.getPersistedSnapshot()`. |
| New loader, missing or unequal version | Deletes the saved record and initializes afresh. This includes every old unversioned record. |
| New loader, matching version but invalid state value | Resolves `no_show`/`idle` with saved context merged over initial context. The PR prose's `writers_room` fallback disagrees with the inspected code. |
| Known valid same-day record | Resolves the saved state value and merged context. A different UTC day is discarded. |

These policies follow the [pre-fix loader](https://github.com/vishnujayvel/showtime/blob/74474089be9f4a8487cd3034c5d4c6a087765499/src/renderer/machines/showActor.ts#L18-L57),
[selected new loader](https://github.com/vishnujayvel/showtime/blob/5a4e415733e8048a146c84600f90d94fc7134c5d/src/renderer/machines/showActor.ts#L18-L122)
and [unversioned-record rejection test](https://github.com/vishnujayvel/showtime/blob/5a4e415733e8048a146c84600f90d94fc7134c5d/src/__tests__/statePersistence.test.ts#L309-L327).
The parent inspected the issue/PR bodies, these decision-critical source ranges
and the identical machine hashes. The repair is a concrete **persistence-schema
and reset-policy change**. It cannot alone be called a changed-machine migration.

## A fair comparison, if preservation is useful

If maintaining an active show across the selected deployment is a real
requirement, the first rival is an ordinary application-owned transformation
from the old record to the new envelope, followed by `resolveState`. A schema
tag or explicit mapping is already ordinary machinery. Extra validation must
justify its construction and use against that baseline; a fresh show is a
matched outcome only if its required progress and recovery work also match.

The [machine and context](https://github.com/vishnujayvel/showtime/blob/5a4e415733e8048a146c84600f90d94fc7134c5d/src/renderer/machines/showMachine.ts)
include parallel phase/animation state, nested live/writers-room substates,
lineup/current-act data and timer values. The
[actor integration](https://github.com/vishnujayvel/showtime/blob/5a4e415733e8048a146c84600f90d94fc7134c5d/src/renderer/machines/showActor.ts#L171-L320)
adds an external celebration timeout, timeline/SQLite updates and notifications.
Some transient context flags are deliberately omitted from persistence. A
later contract must specify timer and transient meaning, observe the immediate
restored state and one meaningful continuation, and inspect omitted/duplicate
effects. A serializable record or successful start is insufficient. No durable
event log was found in this path, so replay is not a mandatory baseline here.

The case remains conditional. The repository and report are owner-maintained;
at retrieval it had no stars or forks, which limits demonstrated independent
adoption rather than proving non-use. The source explicitly invalidates old
versions, and no inspected statement establishes that preserving an active show
across deployments is the desired policy. A cross-version requirement would
currently be authored. For a **machine**-evolution claim, separately pin an
actual shape change and its correspondence. For the already-bound persistence
upgrade, do not add a cosmetic machine change merely to fit a preferred label.

## Alternatives retained by the search

| Evidence | Disposition |
| --- | --- |
| [Aipictors #165](https://github.com/aipictors/aipictors/issues/165), [#357](https://github.com/aipictors/aipictors/issues/357) and [PR #358](https://github.com/aipictors/aipictors/pull/358) | #165 reports a settings-restoration defect; #357 reports manual persistence-maintenance burden, and #358 switches to storing an XState persisted snapshot. Subsequent context fields changed under the same application storage key without an inspected application schema version/migration. This is a concrete evolution exposure, but no inspected report establishes a resulting old-snapshot failure. Retain as a configuration-restoration case. |
| [Node-RED XState node #108](https://github.com/sonntam/node-red-contrib-xstate-machine/issues/108) | A maintainer describes V4/V5 chart/tool migration burden. The inspected node recreates the interpreter; no durable runtime snapshot-transfer route was found. Definition migration and active-state migration remain different tasks. |
| [XState #941](https://github.com/statelyai/xstate/issues/941) | Reports an actual 4.6-to-4.7 persistence-format break and application-owned transformation work. All 20 comments were read. The affected applications are not bound public artifacts, and a later V5 resolution claim does not establish arbitrary machine-schema safety. |
| [Lineup prototype #13](https://github.com/nopivnick/lineup-prototype-03/issues/13) | Excluded from an existing-workflow case: the issue states the feature is unbuilt. Its apparent migration match is not an observed maintenance task. |

## Coverage and next action

The [search ledger](literature/nu-background-searches-2026-09-30.md#2026-10-23-xstate-application-and-material-policy-follow-up)
records returned ranges, narrowing, alternatives and the one-time 14-source
decision audit. This is public-software evidence, not a paper-reading segment
or a systematic prevalence sample. No new PDF, Zotero record or completed
primary-paper reading is claimed.

Private evidence is in `r12-intent-policy-20261023/xstate-practice/` under the C:
recovery root. The final source/search handoff has SHA-256
`12fd51fc844511004003f81ed494ef210bc78558866a78a05c1ad181232f5368`.
Pre/post machine bytes both hash to
`6cbf763b94d057d3a58027b3de8d887f44c63f527a992df4cd319c92d375fb50`.
The new actor source hashes to
`074936dde34eb8dbac7776fb4a2f6fb7c5eb571fa5b718041fac1f84bf9c6bd4`.

Next resolve the practical preservation requirement and, only for a
changed-machine claim, the actual machine-change lineage. Retain current reset
as a valid policy under its own requirements. This case supplies neither a Nu
advantage nor an executed transfer result, and it does not reopen stopped R10.

## Actual runtime evolution with an explicit compatibility cutoff

A subsequent bounded search found **Harny**, a public human/agent workflow
application with a real runtime/schema change. It still does not supply an
obligation to retain pre-change progress. Its [human-review issue #20](https://github.com/lfnovo/harny/issues/20)
asks for parking and later resuming work; the maintainer subsequently recorded
that production engine resume was not implemented. The inspected pre-change
[runner](https://github.com/lfnovo/harny/blob/86cb779dd1eb56b6274cbab8f090ce6ad727ad10/src/harness/engine/runtime/runEngineWorkflow.ts#L38-L70)
creates an actor with input, without a persisted snapshot. Same-version future
pause/resume demand is distinct from preserving already-supported XState
progress across an incompatible deployment.

The transition from parent `86cb779d` to
[`0347e0bd`](https://github.com/lfnovo/harny/commit/0347e0bd1f338776e16da357d640175c834ed042)
introduces a declarative scheduler and v3 run state. Its [historical reader](https://github.com/lfnovo/harny/blob/0347e0bd1f338776e16da357d640175c834ed042/src/harness/state/v3/reader.ts#L4-L12)
marks v2 readable but non-resumable. The subsequent
[`8e732811`](https://github.com/lfnovo/harny/commit/8e7328110a7109c3884af002908724975053c45b)
removes XState and older readers in favor of exclusive v4 state. Its
[architecture decision](https://github.com/lfnovo/harny/blob/8e7328110a7109c3884af002908724975053c45b/docs/decisions/0002-authoritative-run-snapshot.md#L22-L35)
explicitly excludes historical-schema resume, and a [test](https://github.com/lfnovo/harny/blob/8e7328110a7109c3884af002908724975053c45b/src/harness/state/runStore.test.ts#L13)
expects older schema rejection. No application or upstream test was run here.
These are exact commit boundaries; unchanged package version 0.4.0 and the
absence of observed Git tags do not establish a released compatibility contract.

This is useful adverse evidence against treating every old-state rejection as
a defect. Harny chose a compatibility cutoff. A migration task would require an
additional practical retention requirement, or an explicitly authored hypothetical
with that limitation stated. Direct XState snapshot transformation alone would
also not establish migration into Harny's different declarative scheduler:
that would need a correspondence between two runtimes and their effects.

Other new leads did not resolve the selection: [XState #3092](https://github.com/statelyai/xstate/discussions/3092)
reports a state-node rename but accepts incompatibility detection and reset,
without a public affected application; [#5178](https://github.com/statelyai/xstate/issues/5178)
is a same-machine history-restoration reproduction. The [search ledger](literature/nu-background-searches-2026-09-30.md#2026-10-23-non-game-evolution-and-compatibility-cutoff-screen)
records all six focused queries, returned coverage and source decisions.
No eligible case was found in that screen; this is not absence across the field.
Follow a concrete request where reset is unacceptable before binding a practical
cross-version comparison. This adds neither a Nu transfer result nor evidence
that migration is required for all stateful applications.
