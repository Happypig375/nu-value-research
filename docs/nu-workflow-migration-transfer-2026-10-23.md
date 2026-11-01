# A concrete non-game migration case

Camunda process-instance migration supplies a practical state-evolution case
with an explicit preservation requirement. The earlier
[Showtime and Harny investigation](nu-xstate-practice-case-2026-10-23.md)
found legitimate reset/compatibility-cutoff policies instead. This new case
selects a problem and ordinary capabilities; it establishes no Nu transfer,
runtime result or improved intervention.

## Demand and exact edition

A production user in [forum thread 44521](https://forum.camunda.io/t/migrate-instances-from-one-version-to-another-in-camunda-8/44521/3)
reported in May 2023 that canceling and recreating running instances was
unsuitable and that migration availability affected their deployment decision.
The organization and eventual outcome are unknown. Camunda's
[implementation epic #14907](https://github.com/camunda/camunda/issues/14907)
separately records the design choice to change existing instances while
retaining process and job keys. These are user demand and maintainer rationale,
not an independent comparative evaluation.

The selected documentation is Camunda **8.8**, archived at docs commit
[`e8df96583378d22fac284db94fecb6cb4942d5fe`](https://github.com/camunda/camunda-docs/commit/e8df96583378d22fac284db94fecb6cb4942d5fe).
Its ordinary default lets existing instances finish on their original model
while new instances use the newer definition. Explicit migration is available
through Operate/API when current instances must change. Both policies entail
operational work; the documentation calls for testing against realistic data.
[Versioning policy](https://github.com/camunda/camunda-docs/blob/e8df96583378d22fac284db94fecb6cb4942d5fe/versioned_docs/version-8.8/components/best-practices/operations/versioning-process-definitions.md#L8-L54).

## The state correspondence is larger than a task label

[Issue #46281](https://github.com/camunda/camunda/issues/46281) reports an 8.7.12
migration rejection after a task-name change, with one token at a user task and
another already waiting at a joining parallel gateway. The desired outcome
preserves both. It is an unreproduced report, not a demonstrated current defect.

The [8.8 release notes](https://github.com/camunda/camunda-docs/blob/e8df96583378d22fac284db94fecb6cb4942d5fe/versioned_docs/version-8.8/reference/announcements-release-notes/880/880-release-notes.md#L568-L575)
introduce taken-flow migration. The selected contract requires mappings for
the active task, joining gateway and already-taken incoming flow. Thus task
names alone omit consequential execution state. The same contract preserves
existing jobs/values rather than rerunning their initialization, distinguishes
preserved from reset event subscriptions, and rejects invalid plans
transactionally. It also warns that accepted mappings can strand an instance
or leave needed variables unavailable. These rules do not guarantee arbitrary
external effects. [Migration contract](https://github.com/camunda/camunda-docs/blob/e8df96583378d22fac284db94fecb6cb4942d5fe/versioned_docs/version-8.8/components/concepts/process-instance-migration.md).

The issue remains open in the inspected snapshot, with no linked fix/backport.
Its 8.7 report and 8.8's documented addition must remain distinct. No exact 8.7
internal cause, current reproduction or service deployment is claimed.

## Two different research decisions

First decide whether current instances may retain their old behavior. When
they may, parallel versions and explicit migration are valid policy alternatives
with different operational costs. If a required bug fix or business change
must affect running instances, finishing on the old definition cannot satisfy
the same requirement.

For that second question, **Camunda's existing manual migration plan and
validation are the status quo**. A proposed correspondence/checking aid would
need to improve completed migration or reduce complete work beyond those
facilities. Explicit mappings alone are already shipped functionality. No
distinct improved treatment or novelty is established here.

A useful later comparison would freeze the intended current-instance change
and observe identity, active/taken-flow state, pending jobs/events, intended
preserve/reset choices and a subsequent continuation. Count plan authoring,
testing, rejection, repair, verification and operational cleanup. Valid rejection,
deliberate reset and semantically wrong acceptance are separate outcomes.
Novelty would require the closest workflow-migration methods before proposing
a stronger checker; the present source selection does not reopen Nu's returned
R10 implementation.

## Coverage and next action

The bounded search inspected versioning and migration documentation, the 8.8
release notes, epic #14907, reports #46281/#47204 and two forum threads. Temporal
versioning was a credible alternative, not an excluded technology. The next
useful step is to choose a consequential migration requirement and compare any
proposed assistance against the supported manual plan, rather than build a
cosmetic non-game port.

Private sources are in
`A:/nu-value-execution/20261023-material-intent/value-preparation/workflow-transfer-next/`.
Its 21-file manifest hashes to
`8907361b8179213c29d2ead022dfd340e68b7caf90b995d79187b1f12609e67a`.
Parent checked the decisive demand, version-policy, joining-flow, validation
and semantic-limitation passages. No new scholarly body, Zotero operation,
application execution or participant evidence is credited by this source audit.
