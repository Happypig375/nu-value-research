# Ordinary workflows and candidate improvements, 2026-10-23

The source comparison changes the next research decision. **Selective material inheritance is already an ordinary capability in relevant engines.** A useful Nu intervention must therefore establish correct integration or lower complete work for a declared task, rather than claim that combining independent property edits is new. The [development-history audit](nu-development-history-audit-2026-10-23.md) separately binds Nu's intended policy and the historical repairs already present at the research pin.

This implements the [October 19 objective](nu-research-agenda-2026-10-08.md#2026-10-19-objective-improve-evolution-of-stateful-software). The evidence here is official documentation, pinned source, existing primary-paper reconstructions and explicit design reasoning. No new engine, browser application, participant or experimental candidate ran. Source-supported predictions below are not native save/reopen, performance or benefit observations. The earlier [R12 observations](nu-terra-firma-revision-feasibility-2026-10-18.md) remain unchanged.

## A credible status quo for the material task

The common task is to change a family's tint while retaining one instance's independent roughness choice, then continue through another revision from the actual saved result. Material inheritance, scene/prefab inheritance, runtime lifetime and live-state migration are different facilities.

| Workflow and inspected edition | Ordinary policy for the task | Cost and observation boundary |
| --- | --- | --- |
| Nu at `064f7ae92a8506689cd91aff5e6804a375d6ef3d` | Public entity-structure propagation preserves overrides at the complete Nu-property symbol. `MaterialProperties` is one such property; the retained local roughness therefore also retains the old tint. The accepted ordinary field-update helper delivers both fields. | Existing links/history were supplied. Propagation's reconstruction and batch's older saved histories have different consequences. Keep both outcomes, helper construction and any later repair/conversion. |
| Godot 4.7.2, ordinary materials | Share one external material and make the exceptional instance's material unique. Edit albedo on both materials for each shared revision. | A unique material is a whole-resource copy. Two-point continued editing is valid; a source-only later edit is a detachment diagnostic, not failure of that valid policy. Selection, saving both resources and verification remain work. |
| Godot 4.7.2, parameterized shader | Use one shared `ShaderMaterial` for tint and a per-instance roughness uniform. | This can express independent variation without duplicating the shared material. Shader translation, textures, parameter bindings, renderer equivalence and maintenance must be counted. It is not free setup or an executed result. |
| Unity 6.0, Material Variant | Give the exceptional renderer a child material that overrides only the microsurface property; keep tint inherited from its parent. | A saved scene-level material-slot override selects the child. Material properties inherit separately; prefab reference changes are a different operation. Pin shader/pipeline and validate roughness versus smoothness mapping. |
| Unreal Engine 5.6, Material Instance Constant | Parameterize tint and roughness. A child of the family material instance overrides roughness and leaves tint inherited. | Parameterizing the shader, creating/assigning assets and saving the level count. A Blueprint adapter is optional. Runtime Dynamic Material Instances require another persistence contract. |

### Godot: two valid policies, with different setup

The exact `4.7.2-stable` tag resolves to `ed1daf0bf001b61586d9930840f2f1394092c079`; the separate 4.7 documentation snapshot is `9adca4c1c72917bfe1b7be3108abed5ce26696a6`. The latter postdates the release. The [scene-instancing documentation](https://github.com/godotengine/godot-docs/blob/9adca4c1c72917bfe1b7be3108abed5ce26696a6/getting_started/step_by_step/instancing.rst) and [Make Unique implementation](https://github.com/godotengine/godot/blob/ed1daf0bf001b61586d9930840f2f1394092c079/editor/inspector/editor_resource_picker.cpp#L497-L505) support the shared-plus-unique workflow. Duplicating a material detaches its other properties too; a later shared tint must also be applied to the unique resource.

The alternative is supported by the exact release's [ShaderMaterial contract](https://github.com/godotengine/godot/blob/ed1daf0bf001b61586d9930840f2f1394092c079/doc/classes/ShaderMaterial.xml) and [per-instance parameter API](https://github.com/godotengine/godot/blob/ed1daf0bf001b61586d9930840f2f1394092c079/doc/classes/GeometryInstance3D.xml#L13-L28). The [versioned shader documentation](https://github.com/godotengine/godot-docs/blob/9adca4c1c72917bfe1b7be3108abed5ce26696a6/tutorials/shaders/shader_reference/shading_language.rst#L1068-L1161) even uses varied trees as a motivating example. A shared tint plus an instance roughness is a plausible application of that documented facility, not a shader constructed or rendered in this pass. `resource_local_to_scene` duplicates resources per instance; it is not a substitute for selective field inheritance.

### Unity and Unreal: existing selective inheritance

Unity's [6.0 Material.parent API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-parent.html) explicitly supports per-property overrides and inherited parent changes. The matching [6000.0.65f1 editor source](https://github.com/Unity-Technologies/UnityCsReference/blob/9674e068b1822a55486fa0467a77f9a2e7577d92/Editor/Mono/Inspector/MaterialEditor.cs#L3138-L3174) creates a Material Variant for a selected renderer and replaces the matching shared-material slot. This is an ordinary editor route. It predicts that a child overriding only roughness-equivalent behavior will inherit successive parent tint edits. The shader mapping still needs independent validation; equating Unity smoothness numerically with Nu roughness would be an invalid alignment shortcut. The hierarchy is editor-only and flattened in builds, so it supplies no running-state migration guarantee.

Epic's [UE 5.6 Material Instance Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui?application_version=5.6) documents nested material parents, checked parameter overrides and unchecked inheritance. Its [material-instance guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-and-using-material-instances-in-unreal-engine?application_version=5.6) supplies the required parameterization and asset workflow. A child overriding only roughness is therefore a credible ordinary comparator. A material parameter edit is not a whole-actor reconstruction or merge guarantee.

The distinct Blueprint policy supplies useful adverse context. [UE-88414](https://issues.unrealengine.com/issue/UE-88414) explains that instance values are delta-serialized against their archetype; an equal-value default change can remove the distinction and relink future changes. This historical 4.23/4.24 account is not a reproduced UE 5.6 failure. It demonstrates why an explicit material override flag and value-difference inference must not be conflated. Further component/default-propagation issue screens remain in the private ledger; they do not establish a current failure of the proposed material workflow.

A fair comparison can supply both workflows' existing family relationships for an incremental question, or charge their construction for an adoption/authoring question. It cannot give Nu a ready-made family while silently charging a full asset port only to its comparator. Nor may it assume zero Unity/Unreal/Godot lifecycle work from the absence of a Nu-style destroy/recreate call. Observe the relevant import, reference, component, renderer and reopen consequences in each workflow.

## What the literature already provides

The completed [SceneGit S285](literature/full-reading/S285-scenegit-reading-2026-10-15.md), [NodeGit S286](literature/full-reading/S286-nodegit-source-and-access.md) and [LevelMerge S284](literature/full-reading/S284-levelmerge-scene-merge.md) reconstructions already supply common-ancestor merging of represented property changes, conflicts and relevant identity/dependency limits. [Denicek S87](literature/full-reading/S87-denicek-document-computation.md) and [blended-model versioning S108](literature/full-reading/S108-blended-model-versioning.md) supply retained-history/dependency machinery; [Cambria S102](literature/full-reading/S102-cambria-document-evolution.md) and [BiDEL S103](literature/full-reading/S103-bidirectional-schema-versions.md) show that hidden information, defaults and correspondence need explicit policies and retained state. These are reused readings, not new body-reading credit.

A new targeted recall check does not expose a missing elementary method that blocks this bounded design. XML three-way merging is credited at abstract level; Edit Lenses and later domain/model-merge leads remain conditional for stronger correspondence-law or general conflict-resolution claims. The [search ledger](literature/nu-background-searches-2026-09-30.md#2026-10-23-development-history-comparators-and-merge-methods) records the actual retrieval, screening and deferrals. This is not a complete novelty assessment.

Applying a change atomically prevents some intermediate states; it does not establish that the combined final values satisfy application invariants. A conflict marker is a diagnosis requiring resolution, not completed maintenance. Known methods should be credited and adapted only where their integration can improve a practical outcome.

## The intervention to prepare next

**Subsequent construction correction:** the
[material-intent follow-up](nu-material-intent-baseline-2026-10-23.md) finds that
the least-invasive mode table plus field helper is itself the ordinary baseline.
The first construction therefore strengthens that reference, rather than
presenting an equivalent helper as a distinct treatment. The discriminators
below record the design questions that led to this correction. No coupled-field
invariant was found in the selected material path, and a historical merge base
or native failure-injection framework is unnecessary for the selected explicit
operations. A later integration/work comparison must earn its distinction.

Prioritize an **explicit material-field revision policy within Nu** as the next local construction candidate. This advances R12's practical repair/completion question without replacing the broader agenda or promoting it to a proven engine advantage. The first implementation should use the least invasive application/helper representation that can express the required inheritance and local choices. A general engine merge framework is not justified merely by the first missed tint.

Compare that policy with the accepted ordinary field-update helper and unchanged public propagation with an explicit repair policy. Credit the existing engine facilities above when interpreting any result. Keep the original P-local failed delivery, each workflow's actual saved predecessor, the separate history-switch prediction and all setup/repair work. A helper that merely repeats the already-successful batch result supplies no new value claim.

The prospective contract must distinguish:

1. A shared change without local variation, where ordinary facilities should already succeed.
2. A shared field change plus a retained independent local field, as in the existing authored material case.
3. A retained local choice on the same field, including a deliberate choice equal to the previous source value.
4. Explicit return to inheritance, missing values and reset/default operations when their meanings differ.
5. A source-supported coupled-field requirement, with conflict or atomic resolution rather than blind recursive merging.
6. Conflicted/failed application and two later revisions through actual saved state, including whether the stored base advances and what work restores consistency.

These are discriminators, not a mandatory count of new experiments. Select the consequential cases and freeze intended outcomes, eligible initial states, group/identity rules, repair order, observations, controls and limits before execution. Construction, selection, shader/representation changes, metadata storage, editing, checking, failed work, repair and conversion belong in complete work. More fields, a smaller patch or a faster instrumented process do not by themselves measure that work or establish productivity.

A minimal information argument explains one required boundary. The same old-source/current-target/new-source values `(red, red, blue)` can mean either inherited red, which should become blue, or explicitly pinned red, which should stay red. A function receiving only those values cannot guarantee both outcomes. Additional intent/provenance or a deliberately restricted policy is necessary. This elementary argument is not a novel theorem or proof that value-based inheritance is wrong under its own contract.

The proposed improvement is falsified or narrowed if it loses required values or identities, silently resolves a declared conflict, changes explicit override/reset meaning, advances provenance after rejected application, fails actual reopen/continuation, or adds more complete work without a useful correctness/capability gain. Equal or better ordinary workflows are valid outcomes. Novelty and useful effect remain unestablished.

## Non-game transfer

### Redux: changed-code replay and ordinary inspection

Redux DevTools extension 3.2.12 is pinned at `a857d4a44fe170e68508ecc66ffca6d6ad9a4524`, with Redux core 5.0.1 at `50b010210df25c470386f7e39a9389a4a77b3842`. The selected Inspector's row/path selection changes monitor metadata while leaving application history and its selected state unchanged. It still dispatches through the lifted store and can notify raw subscribers. This supports a history-preserving inspection route, not a globally effect-free action. [Instrument source](https://github.com/reduxjs/redux-devtools/blob/a857d4a44fe170e68508ecc66ffca6d6ad9a4524/packages/redux-devtools-instrument/src/instrument.ts#L811-L840), [Redux subscriber dispatch](https://github.com/reduxjs/redux/blob/50b010210df25c470386f7e39a9389a4a77b3842/src/createStore.ts#L294-L309).

Time travel moves a pointer within one retained sequence. An application action issued while viewing the past appends after the retained future; jumping and committing instead makes the selected state the base and discards staged history. Default DevTools hot-reducer replacement recomputes retained actions under changed code, whereas core Redux replacement invokes the new reducer once against current state. Replay calls reducers directly, bypassing application middleware. DOM/component-local state, browser focus, network/storage effects and external resources therefore need separate representation and observation. These are pinned source inferences, not an executed browser recovery. [History and replay implementation](https://github.com/reduxjs/redux-devtools/blob/a857d4a44fe170e68508ecc66ffca6d6ad9a4524/packages/redux-devtools-instrument/src/instrument.ts), [core replacement](https://github.com/reduxjs/redux/blob/50b010210df25c470386f7e39a9389a4a77b3842/src/createStore.ts#L330-L336).

A possible later task is to recover a support-ticket editor after a same-shape reducer correction, comparing retained action/state inspection and replay with ordinary browser tools, existing logs/tests and reconstruction using the same fixed server-response fixture. **No existing ticket application or actual issue is bound yet**; this is an authored scenario shape. Before promoting it, select the real artifact and practical failure, freeze state/projection/effect/continuation observations, and count configuration, retention, diagnosis, repair, verification and recovery. Do not invent a slow manual baseline when the application already has replay fixtures or persistence. Nor should Nu be forced to evaluate Interactive getters when its ordinary property panel supplies the required evidence.

### XState: existing application-owned migration

Stable XState 5.33.3 is pinned at `6a85c4057dc7c0906381664249e0b1bac300cd92`. Its persisted machine state includes context, state/history information and children; `createActor` can restore a supplied snapshot against the current machine. An application-owned transformation of that snapshot is therefore the first ordinary migration comparator. Explicit mapping is not a new Nu-derived method. The developer must account for version dispatch, state/history identifiers, child representations, validation, pending work and effects. [Snapshot input](https://github.com/statelyai/xstate/blob/6a85c4057dc7c0906381664249e0b1bac300cd92/packages/core/src/createActor.ts#L257-L270), [restore implementation](https://github.com/statelyai/xstate/blob/6a85c4057dc7c0906381664249e0b1bac300cd92/packages/core/src/StateMachine.ts#L566-L700).

The stable persisted envelope does not itself preserve the actor mailbox or delayed-event schedule. The [delayed-restoration issue #5331](https://github.com/statelyai/xstate/issues/5331) and [official persistence guidance](https://stately.ai/docs/persistence) distinguish snapshot restoration from event sourcing and warn about incompatible machine changes. Event sourcing is another ordinary rival when the required events actually exist; its capture, adapters, replay and effect-idempotency work count. Reset is a matched alternative only when it reaches the same useful outcome, including any compensation or operator work. A newly initialized order is not automatically equivalent to an already charged order awaiting approval.

The separately inspected 6.0.0-alpha.70 snapshot at `c628b91f5f48b022c7ccf9dde1bd408764dd8add` supplies explicit versioned migration and timer records. It is a future reference, not the stable baseline or a claim of queued-mailbox persistence. [Alpha persistence contract](https://github.com/statelyai/xstate/blob/c628b91f5f48b022c7ccf9dde1bd408764dd8add/docs/persistence.md). Restoration and child restart also differ from Nu's same-process FSI/content-reconciliation route.

A prospective charged-order/approval case could compare ordinary direct transformation with additional source-version rejection and whole-envelope checks, plus event replay where available. State/context meaning, child identity, original-versus-restarted deadline policy, accepted events, duplicate/omitted effects and the first subsequent decision must be declared independently. The extra checks must justify their own work against ordinary migration. The vendor's workflow example is practical motivation, not independent adoption evidence, and the particular schema change remains authored. No migration, actor process, external service or effect replay was executed here; this preparation does not reopen Nu's stopped R10 gate.

These two references support portable questions about represented state, inspection, reconstruction and pending/effect obligations. Configuration inheritance, changed-code replay and migration of active state remain distinct questions. Useful transfer requires a tested outcome and complete-work comparison in the selected non-game artifact.

### A concrete replay failure and a migration obligation

[NgRx #919](https://github.com/ngrx/platform/issues/919) now supplies an actual
replay task in place of the authored ticket-editor shape: a book disappears
after export/reload/import when its lazy reducer is unavailable during replay.
The 2018 report names NgRx 5.2.0 and was closed through #955. The historical
export and fixed application revision are not recovered; this is a practical
source case, not a runnable or reproduced current defect.

The pinned Redux DevTools import implementation recomputes retained actions
under the active reducer unless its explicit no-recompute route is used.
Therefore a usable export needs the relevant base/payload and corresponding
reducer registry/semantics. It is not automatically an independent endpoint
oracle after a repair. Ordinary Action/State/Diff inspection, registration
correction, reimport of an unchanged export and an independently verified
continuation form a possible workflow; source evidence alone does not show it
succeeds. [Import implementation](https://github.com/reduxjs/redux-devtools/blob/a857d4a44fe170e68508ecc66ffca6d6ad9a4524/packages/redux-devtools-instrument/src/instrument.ts#L751-L829).

[NgRx #229](https://github.com/ngrx/platform/issues/229) and
[DevTools extension #281](https://github.com/zalmoxisus/redux-devtools-extension/issues/281)
also report subscription/component effects around replay. Bypassing middleware
does not imply an effect-free operation. The earlier
[Redux #378](https://github.com/reduxjs/redux-devtools/issues/378) and
[#559](https://github.com/reduxjs/redux-devtools/issues/559) discussions distinguish
visible action labels from preserved past transitions and debate changed-reducer
replay. These are related historical reports, not independent Nu replications.
An unpinned artifact makes the proposed task ineligible; a frozen eligible
export that actually lacks necessary evidence can demonstrate insufficiency.

Separately, the [Camunda migration case](nu-workflow-migration-transfer-2026-10-23.md)
provides explicit current-instance preservation demand. Ordinary parallel
versions are valid when old behavior may finish; when current instances must
change, the existing manual migration facility is the appropriate status quo.
This resolves the earlier lack of a concrete retention obligation without
claiming that a distinct improvement has been designed or validated.

The [subsequent application search](nu-xstate-practice-case-2026-10-23.md)
binds Showtime's public relaunch report and its later rejection of unversioned
records. Its machine is unchanged across that persistence repair, so this is
a concrete record-schema/reset decision, not a demonstrated machine-evolution
failure. Cross-version preservation intent remains unresolved. Aipictors,
Node-RED and XState #941 retain distinct configuration, definition-migration and
unbound application boundaries; none is silently upgraded to a transfer result.

## Evidence and continuation

The private evidence root is `C:/Users/hadri/nu-value-recovery/20261018-205753-integrity-stop/source-comparisons-20261023/`. The engine assistants retained exact source snapshots, revision identities, inspected ranges and failures in `godot-baseline/`, `unity-baseline/` and `unreal-baseline/`; the literature assistant retained its decisions and search/audit outputs in `merge-literature/`. The parent checked decision-critical documentation and the per-instance/variant interfaces, retained adverse scope and corrected an archive boundary: Epic issue HTML responses were application shells, while readable issue-extractor text supports the historical issue account. A shell hash is not a hash of that claim body.

Ten assistants divide maintainer work; their agreement is not independent user evidence or a measured effect. No native application, shader, participant or candidate execution occurred in this source audit. The broad survey remains open. R02 input construction, R10 explicit migration and the subsequent R12 native material-intent construction remain stopped; ordinary source investigation and transfer preparation do not resume them. The newer replay/Camunda evidence is under `A:/nu-value-execution/20261023-material-intent/value-preparation/replay-comparator-next/` and `workflow-transfer-next/`, with coverage in the [search ledger](literature/nu-background-searches-2026-09-30.md#2026-10-23-parallel-recovery-evolution-and-transfer-source-audit).
