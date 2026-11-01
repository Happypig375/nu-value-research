# R04 historical-task eligibility audit, 2026-10-26

The inspected history strengthens the negative and neutral boundaries of the
explicit-enumeration question. It does **not** turn the proposed serve,
projectile-renewal or cancellation requirements into mined feature requests.
An engine API rename also does not automatically require renaming an
application-local message. That distinction qualifies the earlier rename
example and matters before measuring a convention's maintenance burden.

This is documentary source evidence. No variant, compiler probe, runtime,
candidate or participant experiment was constructed or run. The
[Daybreak-only branches](unfinished-daybreak-only-work-2026-10-25.md), returned
constructions and [A: storage stop](workspace-integrity-return-2026-10-26.md)
remain untouched.

## Decision and inclusion boundary

R04 asks whether explicit current-case enumeration earns its maintenance work
relative to an equivalent catch-all, with the same useful requirement, tools
and resources. Source history can establish what was changed, its available
rationale and relevant alternatives. It cannot establish a representative task
mix, successful delivery, compiler exposure or a causal effect on work.

The selected cases are Nu's Breakout gameplay and Blaze Vector projectile
sites at `064f7ae92a8506689cd91aff5e6804a375d6ef3d`. The already-recorded
post-pin time-advance rename is rechecked only for its task-eligibility claim.
Both demos and their maintainer history share a lineage; they are not
independent adopter accounts. Ordinary valid local names, catch-alls and safe
reorganization remain admissible unless the practical contract actually
requires otherwise.

## Rename burden depends on the local requirement

In [Blaze Vector commit 25851cf](https://github.com/bryanedds/Nu/commit/25851cf7adf4d8dedefa71d55d5deef32fb83fa7),
the maintainer changes the engine event, local command case and terminal match
pattern from collision to penetration terminology, explaining that the change
makes room for frame-based collision events. The
[parent source](https://github.com/bryanedds/Nu/blob/562dcd1b8a151850cf278776ec50537ee06faa52/Projects/Blaze%20Vector/Bullet.fs#L7)
has exactly `Update | Collision`; its final `Collision` arm destroys the
entity. The successor keeps that destruction body.

Replacing only the parent's final pattern by `_` has an equivalence argument
for ordinary values of those two declared cases. Null/invalid CLR values,
compilation and runtime equivalence were not checked. Under the **actual local
vocabulary migration**, the explicit handler needs one renamed pattern while
the catch-all does not. Both conditions still incur the declared type and
event-mapping edits. These are source edits, not measured work or benefit.

If the actual requirement is only to consume the renamed engine event,
keeping the local `Collision` name and mapping the new event to it is a valid
source-level alternative to investigate. Then neither convention requires
that handler-pattern change. A study must not reject this alternative solely
because it differs from the maintainer's patch. If adopting the new local
vocabulary is genuinely required, state its beneficiary and reason in the
contract before execution; do not add that requirement to manufacture a
convention effect.

The same qualification applies to the earlier
[Breakout time-advance commit](https://github.com/bryanedds/Nu/commit/89e4dc7969c523c324109c9fb78e6989eb56d069).
Its three scoped changes rename the local `TimeUpdate` case to `AdvanceTime`,
the engine event subscription, and the final handler pattern. The engine-event
migration alone does not establish that the local case must change. Retaining
`TimeUpdate` with the new event subscription leaves both handler forms
available. This corrects an overly broad practical interpretation of the
historical diff; the previously recorded source counterfactual **conditional
on the local rename** still holds. Neither alternative has been compiled or
observed under a successor task here.

## Genuine maintenance without a case-extension opportunity

| Historical observation | What it supplies for R04 | What it does not establish |
| --- | --- | --- |
| [Projectile lifetime constant relocation](https://github.com/bryanedds/Nu/commit/0dd5d1f6ac492e7e3dee0fece6d095e5282ef852) leaves both command cases intact. | A real maintenance change with no new case-coverage opportunity at this match. | A request to renew a live projectile, or equal total effort under both conventions. |
| [Adding visibility suppression](https://github.com/bryanedds/Nu/commit/1ca9cbef996219e5f4b53d083a3257d2328e5048) and [removing it](https://github.com/bryanedds/Nu/commit/30738ff4c6001c3536cf87083021a27cce892cfc) change the same terminal body. | Both conventions retain a body that can need semantic maintenance. | Independent tasks, a causal reason for the reversion, or a convention-specific diagnostic. |
| The [bullet gravity repair](https://github.com/bryanedds/Nu/commit/1defc61182c77f2d52f3a74a102641b75b0246fc) changes `GravityWorld` to `GravityIgnore`; the command union/match is unchanged. | A maintainer-described bug repair outside the targeted match. | Reproduced faulty/fixed behavior or measured repair difficulty. |
| Breakout [removes a scene-state guard](https://github.com/bryanedds/Nu/commit/08d473b4854a0559b2ab5178595866dfd4545436) and later [restores it](https://github.com/bryanedds/Nu/commit/39d5dc97321c7b7af75f05b5fb11c2fe7b40a0b7) without changing the union. | Real content-policy evolution that is distinct from adding a state. | A validated visual outcome, independent user request or causal convention effect. |

The projectile command first appears during the
[October 2023 MMCC conversion](https://github.com/bryanedds/Nu/commit/32b94f7687594c6958095ed68b14831d5b90fc1f),
nested in `Gameplay.fs`. Subsequent naming changes and the move to `Bullet.fs`
retain two cases. No addition/removal after that introduction was found in the
inspected projectile history through the pin. The earlier shift from an age
counter to scheduled destruction is real lifecycle maintenance, but precedes
the selected command match and supplies no renewal/cancellation request.
The authored sketches remain legitimate conditional mechanism questions;
the history does not establish their frequency or convert them into mined cases.

## Breakout state history and a reference-solution caution

Breakout's history is not uniformly two-state. The initial April 2024 code has
`Commencing`, `Commence`, `Quitting` and `Quit`. A
[conversion](https://github.com/bryanedds/Nu/commit/fcb9abdcf28a3f1d8ce7c1c02b6acc0b66747095)
replaces these with `Empty | Playing` and moves quitting from a message to a
command. Another
[shared conversion commit](https://github.com/bryanedds/Nu/commit/48a85cb18ee53849eca7a8397d9d2535524fed74)
introduces `Playing | Quitting | Quit` and changes content matching. The later
[retirement](https://github.com/bryanedds/Nu/commit/a8e5c1aa73b44b618367feb80fea851006985799)
removes `Quitting`. That commit also changes OmniBlade and other examples;
its message alone is not evidence of a Breakout-specific requested feature
or runtime repair. These are actual representation/lifecycle changes, not an
established new gameplay requirement for the current two-state baseline.

The [score addition](https://github.com/bryanedds/Nu/commit/c9d8c4a7848c550e06d17f94161bc69238374224)
is a concrete maintainer feature: it adds score storage, brick-hit accumulation
and score display while retaining `Playing | Quit`. However, that patch also
matches the **constant** `GameplayState.Playing` in `Gameplay.update`.
The [June 7 update](https://github.com/bryanedds/Nu/commit/42458461bb1829362b6620b891c8175e1b3e6536)
changes the scrutinee to the model's `gameplay.GameplayState` and changes the
empty/initial lives assignment. This follow-up is bound to actual source,
not inferred from its generic commit title.

The narrower finding is that a selected historical patch is not automatically
a correct reference solution. We have not established whether callers made
the earlier scrutinee distinction observable, what its compiler emitted, or
whether an actual run failed. A later task must independently bind its active
and inactive-state requirements and observe them. Preserve the intermediate
source and later correction; do not silently use the revised successor as
proof that the earlier feature patch delivered every retained obligation.
This source history adds no runtime result or failure-trigger construction.

## Consequence for the active proposal

For each historical or adapted task, record separately:

1. The practical requested outcome and whose decision it serves.
2. The external contract that must change, including who owns its vocabulary.
3. Any required application-local naming or structural change, with its reason.
4. The maintainer's chosen patch, legitimate alternatives and later revisions.
5. Independent new/retained observations and complete work needed to establish delivery.

A domain change can be a controlled, authored intervention without being a
representative maintenance task. Conversely, a real maintenance change may
leave the target domain unchanged. Keep these categories and their frequencies
separate; do not force them into equally weighted arms or remove neutral and
adverse cases after seeing outcomes. No candidate allocation is added.

The next R04 decision is whether to evaluate a clearly bounded authored
case-evolution question or a practically required historical contract change.
For the latter, establish the required local/external boundary and allow valid
alternatives before building the task. Repeating these same two demo histories
will not supply an independent adopter population. Neither source counts nor
another compiler demonstration can establish the missing maintenance effect,
and a convention result alone would not establish whole-engine adoption value.

## Coverage and review

All source retrieval used public GitHub API routes; an initial web-page open
failed with a cache miss. No access purchase, new account or library write was
needed. Counts below are path-query occurrences, not independent changes or
scientific studies. Each query requested 100 results; each page 2 returned zero.

| Bounded path history | Page 1 | Actual body coverage |
| --- | ---: | --- |
| `Projects/Breakout Mmcc/Gameplay.fs` through the study pin | 15 | Fourteen scoped textual patches and the pure rename metadata; domain declarations at all 15 revisions. |
| `Projects/Breakout/Gameplay.fs` through `c1e5957` | 39 | Domain declarations at all revisions; selected state, score and subsequent correction patches/ranges. Other older bodies were not fully read. |
| `Projects/Breakout/GameplayDispatcher.fs` through `c1e5957` | 4 | Declaration history plus four existent snapshots, including the factored period; no fallback/conversion implementation audit. |
| `Projects/Blaze Vector Mmcc/Bullet.fs` through the study pin | 15 | All scoped patches. |
| `Projects/Blaze Vector/Bullet.fs` through `f988d75` | 5 | All scoped patches. |
| `Projects/BlazeVector/Bullet.fs` through `e780b2e` | 13 | All scoped patches. |
| `Projects/BlazeVector/Gameplay.fs` through `4e40438` | 34 | Metadata for all; projectile-related hunks in 20 commits. |
| `Projects/BlazeVector/BlazeGameplay.fs` through `58fe46c` | 59 | Metadata for all; projectile-related hunks in 31 commits. |
| `Projects/BlazeVector/BlazeDispatchers.fs` through `39c1bf1` | 81 | Metadata only; its older `Games/` predecessor was not followed. |

Breakout's 58 path-query occurrences represent 56 distinct commit IDs. The 54
main-file declaration snapshots required correction for indented module types
and a temporarily separate dispatcher; the first extraction was retained and
was not treated as proof of missing types. The pinned file matches the last
returned path revision by source hash. These checks establish the stated
source lineage, not whole-repository coverage or runtime correctness.

A Sol High worker owned the projectile audit; the parent verified the decisive
rename patch and complete parent/successor projectile source, the gravity
patch and the earlier time-rename patch. Parent review narrowed equivalence to
ordinary declared values. The parent owned the Breakout audit and integration.
This is AI maintainer review, not human approval or independent replication.
The private `r04-breakout-history-20261026/` and
`r04-projectile-history-20261026/` packets retain exact query URLs, revisions,
coverage, corrections, hashes and limitations. Metadata-only item granularity
is stated separately from direct patch/hunk records. Five associated-PR checks
and three exact issue searches in the projectile audit returned zero; no
absence claim is made about discussions outside those queries.
