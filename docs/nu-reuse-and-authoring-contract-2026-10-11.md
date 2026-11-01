# Nu reuse: authoring a variant versus extending its vocabulary

**Decision, 2026-10-11:** R12's first candidate reuse unit is a persistent, explicitly named entity tree authored in Gaia with existing dispatchers/facets and a declared propagation source. This is an existing source-supported facility, not a proposed new editor. Separate configuring an instance, propagating a family revision and adding behavior outside the prepared vocabulary. The case supports R01/R05/R06 and a future R20 role study; no reuse benefit, designer independence or execution is established. [PLAN](../PLAN.md) retains all construction and experimental holds.

## Existing mechanism and its boundary

All Nu references use **`064f7ae92a8506689cd91aff5e6804a375d6ef3d`**. The [README](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/ReadMe.md#L93) advertises recursive prefab-like entity-structure propagation. This is a maintainer capability claim, not a comparative result; its linked image was not inspected. Selected implementation and editor paths supply the following narrower account.

| Source mechanism | Consequence for the proposed reuse unit |
| --- | --- |
| [Overlays](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/Overlayer/Overlayer.fs#L38) derive intrinsic property defaults from dispatcher/facet definitions, with inheritance and optional external property sets. Variable/computed expressions are not converted into those intrinsic default symbols. | An empty external overlay file does not mean that no overlay/default machinery exists. The inspected Gaia, Sand Box 2d, Terra Firma and both Breakout external files are empty; they do not supply an existing nonempty configuration family for this case. This is a bounded sample, not a repository-wide absence claim. |
| [Overlay classification](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/Overlayer/Overlayer.fs#L120) compares a current property value with its converted default. Matching values are classified Overlaid; altered/bare values may serialize, while overlaid/nonpersistent ones do not. | The inspected mechanism records values/default correspondence, not a separate author's intent to pin an equal-valued override. A request to retain a value even when it equals the old default needs an explicit supported representation or extra work. No observed data loss is claimed. |
| [Descriptor writing](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/World/WorldModuleEntity.fs#L2423) uses that serialization policy, with separate order/history options. Child traversal includes persistent entities except DeclarativeProtection. | Use unprotected, persistent editor-authored trees with unique explicit sibling names for the first case. Code-declared MMCC/ImSim content is not automatically the same authoring unit. A saved descriptor is not a snapshot of every reachable runtime value. |
| [Property propagation](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/World/WorldModule2.fs#L548) compares previous source, current source and target descriptors. A target symbol matching the previous source follows the current source; a differing target can remain. Missing symbols use additional overlay/default branches. | A useful family-change mechanism exists. Its value comparison is not a guarantee of semantic conflict resolution or preserved user intent. Before claiming an override survives, identify which serialized/default branch actually represents it. |
| The property loop explicitly excludes Name, Position, Rotation, Elevation, PropagationSourceOpt and PropagatedDescriptorOpt. [Children](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/World/WorldModule2.fs#L656) are matched by name. A source-deleted prior child is dropped even if a target version exists; a target-only child is retained. For a previously known nonempty-dispatcher child still in the source but absent in the target, recursion starts with an [empty descriptor](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/World/WorldTypes.fs#L1813), retains its different empty dispatcher and the final filter omits it. | Local deletion can survive this ordinary revision; source presence alone does not imply resurrection. A later source deletion and reintroduction instead takes a new-child path. Renaming changes name-based matching, not an inspected stable-identity mapping. Position/rotation exclusions are not a theorem about all local/world transforms. These are source-derived policies, not exercised outcomes. |
| [Applying propagation](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/World/WorldModule2.fs#L722) serializes targets, destroys/recreates each existing eligible target, updates the source's saved descriptor and can recurse through sourced ancestors. [Destruction](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/World/WorldModuleEntity.fs#L2235) unregisters, removes entity-owned tasklets and recursively destroys children. | Reusing the same address does not preserve runtime lifetime, pending work or arbitrary external effects. Select quiescent authoring for the first case; live gameplay propagation would need its own continuation/effect contract. Include rebuilding and affected ancestors in costs. |
| Gaia's [duplicate path](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L1613) can establish or remove a propagation source. [Push/Wipe](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L1991) and the [Propagation Sources panel](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L2966) expose actual controls; the propagation wrapper snapshots first. | The inspected facility has an editor route. Its existence does not establish agent transport, trained-user success or reliable undo of all effects. Wiping targets/history changes the future update policy and is not cost-free preservation. |

This propagation mechanism is distinct from R03's same-code history, R10's model conversion and an R11 multi-person merge facility. It has a saved source descriptor and reconciliation rules; that alone does not establish version control, concurrent-edit conflict reporting or a CRDT. No new guarantee of those kinds is attributed to Nu.

## Proposed authoring and change contract

Use a prepared family of ordinary GUI button assemblies as the first reviewable candidate: a root with the existing button behavior and explicitly named persistent decorative children. The [existing input audit](nu-pause-exit-contract-2026-10-11.md) binds the normal button click path; this family is newly authored, not a mined feature request or an observed project template. Pin the allowed properties, assets, component types and behavior before assignment. Verify that the chosen editor-created assembly and ordinary click route are supported; no assembly has been constructed here.

1. **Create a supported variant.** Change the label, selected exposed properties and declared placement using the supplied vocabulary. Preserve enabled/disabled click behavior and unrelated instances. Correct rendering alone is insufficient: the chosen ordinary interaction must still occur under its declared input policy. Give every workflow equivalent assets, requirements and ordinary documentation.
2. **Revise a family.** Change a shared property and add or remove a named decorative child across linked instances while preserving nominated instance-specific differences. Declare source-authoritative deletion and target-only additions when those are intended. Exercise local deletion under ordinary source revision separately from source deletion/reintroduction. If an equal-valued pinned override or rename preserving a child's logical identity is required, state it explicitly rather than assuming propagation records that intent. Do not hide a difficult instance by deleting it from the outcome set.
3. **Extend the vocabulary.** A later hold-to-confirm control with cancellation on early release changes the ordinary click contract; label this an authored extension of the prepared button family, not another label/configuration choice. First check whether the frozen set of available components already expresses it. If so, it is configuration; otherwise count the necessary component/code, authoring-interface, documentation, integration and verification changes. No claim that all of Nu lacks such a facility follows from inspecting one button path.

These are separate task classes, not three mandatory arms or a sample-size justification. Keep task provenance and all assigned outcomes visible. A mechanism comparison may use bounded agents only under later authority; its outcomes cannot estimate designer productivity. For R20, a possible division is a programmer preparing the family and another role configuring it, with explicit escalation for unsupported behavior. That division is proposed, not observed human work or a verified non-specialist workflow.

The first propagation comparison concerns a quiescent editor-authored artifact, not preservation of an in-flight game. Before a family revision, record the prior source descriptor and eligible targets; initial duplication and the first propagation belong in setup work. With no prior descriptor the source path uses an empty one, so bootstrap and later revision are different conditions. Observe the resulting declared values, structure, nominated instance differences and working interaction after reconstruction; saving/reopening must preserve the declared family/instance policy if that is part of the task. Record whether propagation history is actually saved and restored. A correct alternative may recreate entities; do not score runtime object identity as preserved unless the requirement promises it. Missing input or property observations remain inconclusive rather than successes.

## Credible alternatives, evidence and total work

A credible ordinary comparator may use Nu's existing entity composition, duplication, named reusable F# helpers and parameter data as appropriate; it is not restricted to manually editing every copy. The exact supported implementation remains a later preparation/construction decision. A cross-engine claim would additionally require the other engine's ordinary prefab/inheritance facilities and matched semantics. This audit does not establish an engine ranking or novel reuse mechanism.

Completed [S255](literature/full-reading/S255-game-product-lines-comparison-partial.md) and [S256](literature/full-reading/S256-game-product-line-predecessor.md) supply favorable prepared product-line results and inconclusive MDD efficiency differences, with shared study lineage. Supported feature selections, handwritten code/models and their rubrics do not measure the cost of extending the generator or integrated runtime correctness. [S257](literature/full-reading/S257-unreal-model-code-comparison.md) adds favorable correctness on prepared Unreal tasks, no significant selected efficiency contrast and practitioner support for mixed code/visual workflows. Its scaffolding, integration and role assistance are part of the comparison; it supplies no pure syntax effect or measured Nu advantage. These completed reconstructions are reused, not new paper readings.

### 2026-10-15 practice and generation continuation

[S253's complete seven-organization study](literature/full-reading/S253-tools-expectations-reading-2026-10-15.md) reports generally acceptable existing infrastructure alongside bugs, occasional lost work, unstable or restrictive editors, usability, extensions and migration concerns. Across 27 role-structured sessions, the cases emphasize compatibility, platform and asset integration, rapid prototyping and change during production. Five organizations used third-party engines, often with local modification, while mature tools and bought assets were ordinary alternatives. These are purposively selected interview accounts without observed task outcomes or saved-work estimates. R12 must therefore credit an ordinary package of engine/editor reuse, duplication, composition, scripts/helpers and asset workflows rather than treating local mechanism construction or a manual-every-copy baseline as free.

[S254's complete final-edition reading](literature/full-reading/S254-game-reuse-reading-2026-10-15.md) supplies two studios, five projects and four developers from the same work lineage as the earlier preprint and replication package. It identifies prefabs as configured trees containing properties, components, children, scripts and assets, and reports a bespoke level editor that let a designer author content with fewer mistakes. It also reports upfront construction and expertise costs, redundancy, propagated errors, technical debt, misunderstood relations and dead prefabs. Cross-project reuse was estimated at only 2–5 percent with no resolved denominator. The favorable and adverse accounts strengthen the configuration/family-revision/vocabulary-extension split and require credible prefab, scene, Blueprint and helper/composition comparators, but they do not measure task completion, savings, break-even reuse or Nu's ability to preserve intent.

[S263/S264's completed paired reading](literature/full-reading/S263-S264-phylogenetic-generation-reading-2026-10-15.md) now closes the main-text and visual gap for a different comparison: hybrid content generation from the same 48-member Kromaia family. S263's LCG arm is favorable against its two evolutionary PCG baselines, but it bundles phylogenetic guidance with expert domain rules, manual ancestor reconstruction and integration. Selecting phylogenetically related seeds alone has a near-null Overall advantage over random seeds (Cliff's delta -0.04898). S264 reuses the same source family and S263 rows rather than independently replicating them; its new FICG arm has a statistically different but negligible Overall effect against LCG (Cliff's delta -0.021912), with the large gain confined to one metric. There is no pure expert-authoring baseline or productivity outcome. If a selected comparison uses generation, count encoding, rules, tree machinery, expert selection, manual reconstruction/injection, integration, repair and the actual reuse count. These results do not transfer to Nu's source propagation, instance-value retention or authoring benefit.

Separate total work into initial family/tool construction, onboarding/support, each supported variant, family revisions, vocabulary extensions, integration/verification and repair. Report the full assigned workload and the reuse count at which costs are incurred; do not presume a break-even point or amortize setup over hypothetical future variants. Count saved-source/history storage, serialization/default resolution, target destruction/recreation, ancestor propagation and observation overhead where relevant. An inexpensive configuration task can coexist with expensive extension or integration.

R12 now has a concrete reuse unit and a configuration/revision/extension boundary. Promote it only if an actual authoring or maintenance decision makes those trade-offs consequential. Before execution, establish the ordinary comparator, exact property/identity policy, supported editor/input access, saved-history behavior, valid alternative outcomes and total-work accounting. At the 2026-10-11 checkpoint, S263/S264's generation methods were access-limited; the 2026-10-15 continuation now supplies their bounded comparator evidence. They become relevant only if a selected comparison uses generation and do not block this distinct scene-family question. No editor operation, runtime, source variant, observer, human study, worker or model run was performed.

### 2026-10-15 alternative-authoring continuation

The complete [SuBViS](literature/full-reading/S274-subvis-access.md),
[BPAlt](literature/full-reading/S275-bpalt-partial-method.md) and
[NCAlt](literature/full-reading/S282-ncalt-access.md) readings close the selected
graph/class-alternative method gaps. They supply three different reuse units:
node/graph states, whole Blueprint classes with placed-actor choices, and
copied behavior-tree graphs with selected-node transfer. BPAlt replaces the
placed actor before play; its level scenario records class choices, not
arbitrary running state. NCAlt can paste disconnected nodes when a needed
parent is absent. These are useful supported policies, not evidence of Nu's
family-revision or live-continuation semantics.

The studies retain favorable subjective evidence with material bounds:
SuBViS has four assisted students and a recompile defect; BPAlt has ten paid
students, prepared templates and substantial tutorials; NCAlt has sixteen
paid students and a strong order interaction in its usability score.
BPAlt's selective merge/scenarios and later all-instance Play option were
outside its study, while NCAlt's efficiency/ease and selective-merge ratings
did not establish an advantage. No study measures complete construction,
extension, repair and verification work. Shared authorship is a lineage,
not independent replication or proof of person-level overlap.

For the prepared button-family comparison, allow ordinary duplication,
parameterized helpers, class/graph alternatives and explicit reconstruction
where applicable. Score the nominated values, structure and interaction after
reconstruction; do not add runtime-identity retention as an unstated
requirement. Charge setup, supplied solutions, assistance, missing-vocabulary
implementation, repair and verification to the proper role. Selective-copy
success and favorable ratings remain distinct from R20 productivity and R21
steering effectiveness, which are still unmeasured.

### 2026-10-15 Phylogenix final-edition continuation

The full [S262 original](literature/full-reading/S262-phylogenix-integration-partial.md)
now establishes its three figure and final-edition contents. It demonstrates
project-wide prefab relationship analysis and displays a Canvas cluster,
with four reported analysis times. This supports a diagnostic/organization
alternative when a task requires finding related objects. It does not test
source propagation, retained instance values, vocabulary extension, runtime
lifetime or authoring savings. Its four games overlap S254, while its exact
reported build and the paper/package method correspondence remain unresolved.

For a selected family revision, allow ordinary structural inspection alongside
prefabs, duplication and helpers. Observe the actual edit, child/target identity,
retained variation, behavior and repair; do not score the tree itself as a
completed revision. Charge extraction, viewer handoff, inspection and manual
reconciliation when they are used. The four single times with differing
project sizes and no hardware/repetition protocol do not supply a cost model
for this comparison. Further viewer or algorithm reconstruction is conditional
on selecting that operation, rather than a prerequisite for the prepared Nu
button-family question.

### 2026-10-18 public propagation observation

The [first public-wrapper exercise](nu-propagation-feasibility-2026-10-18.md)
now passes one frozen Button/Text revision in a real functional, accompanied,
halted stub world. It uses ordinary creation, serialization, duplication and
linking, then calls `World.propagateEntityStructure` once. Matching values
follow the source; differing local values and local deletions survive; source
deletion removes even a locally edited child; target-only children survive.
A target value changed and then returned to the previous source value follows
the later source revision. The target's root ID changes on reconstruction.

This resolves the public API execution route for that mechanism fixture,
including its declared limits. It does not establish Gaia access, save/reopen,
interaction, runtime lifetime or authoring benefit. Next select a consequential
family revision and a credible helper/composition comparator with the same
required override/deletion behavior, counting all construction, configuration,
revision and verification work. Preserve differing user-intent requirements
rather than treating equal values as proof of an intended override policy.

### 2026-10-18 existing Terra Firma family and next revision case

The next R12 case is grounded in the pinned Terra Firma gameplay scene, rather
than another newly invented family. This establishes an existing reusable
artifact; the proposed revision below remains **authored**, without an observed
designer request, task frequency or measured benefit. It does not change the
earlier finding that the sampled external overlay files are empty: entity
propagation and external overlays are different facilities.

#### Existing artifact and loading boundary

The [actual scene](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Projects/Terra%20Firma/Assets/Gameplay/Scene.nugroup)
has 19 top-level entity descriptors and 197 including descendants, with 166
explicit propagation links to 11 source addresses. All link addresses resolve
within that serialized tree. These are structural extraction results, not
runtime-created entity counts or independent empirical cases. The traversal
follows each descriptor's children; it does **not** count the descriptors
nested inside `PropagatedDescriptorOpt` as additional live instances.

| Existing source, relative to `Game/Gameplay/Scene` | Direct linked targets | Interpretation |
| --- | ---: | --- |
| `Villa` | 3 | Four Villa trees including the source; each has 43 direct children. |
| `Villa/Palm` | 31 | Eight palms in each Villa, 32 including the source. |
| `Villa/Barrel`, `Villa/Barrier`, `Villa/Crate`, `Villa/Generator` | 19, 35, 27, 11 | Repeated static props, with links spanning the Villa trees. |
| `Villa/House`, `Villa/House2`, `Villa/Tires`, `Villa/Well` | 7 each | Additional prop families within the same scene. |
| `Enemy-0001` | 12 | A separate character family; exclude its active behavior from the first static-authoring case. |

Terra Firma's [selected gameplay path](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Projects/Terra%20Firma/Gameplay.fs#L34)
loads `Assets/Gameplay/Scene.nugroup` using `World.beginGroupFromFile` at line
49, under the [declared scene handle](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Projects/Terra%20Firma/Simulants.fs#L20).
The [loader](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/World/WorldImSim.fs#L259)
reads and parses the file only on group creation without an existing journal;
changing its path or contents does not reload an existing group on the next
Process pass. [Group reconstruction](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/World/WorldGroup.fs#L258)
then reads the entity descriptors. This is a source-supported game-loading
route, not a new successful Terra Firma launch, asset publication or rendering
observation. Prefer a fresh process for the initial unchanged-scene check;
explicit recreation would also need its journal/lifecycle boundary verified.

The [source palm and its seven siblings](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Projects/Terra%20Firma/Assets/Gameplay/Scene.nugroup#L2381)
use `RigidModelDispatcher`, `Gameplay/PalmTree`, a static concave surface
shape, clipping and mounting. The four Villa instances preserve different
local placements; explicit scale variations include 1.2 and approximately
1.1, as well as near-unit values. Missing scale symbols are not measured
runtime defaults. All 32 palm descriptors omit `MaterialProperties` in the
current saved scene. Their asset, placement and shape values supply actual
variation to preserve, not demonstrated intent about a future color change.

The file also preserves older source layouts. For example, the [Barrel's
current material record](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Projects/Terra%20Firma/Assets/Gameplay/Scene.nugroup#L1653)
contains fields absent from its saved propagation descriptor at lines
1681–1709. Do not silently regenerate that history and call the result an
unchanged source artifact. Its effective loading and save/reopen correspondence
remain an observation obligation. This is distinct from the stopped R10 live
application-schema construction and does not resume that gate.

#### A consequential, falsifiable comparison to prepare

Use a quiescent **shared foliage tint revision**: apply one declared new
`AlbedoOpt` value to the 32 existing palms while preserving their placements,
scales, shape/asset choices and unrelated scene configuration. The beneficiary
is a level author maintaining a placed prop family. This is a plausible task
derived from an existing artifact and the completed S254 practice reading,
not a mined outstanding issue or evidence of its prevalence.

Prepare two requirement conditions before execution. First, all palms should
follow the shared tint. Second, introduce one explicitly authored local
roughness override on a named target and require the same shared tint change
while retaining that independent roughness choice. Both conditions must retain
the other 165 serialized entities' declared configuration, including objects
reconstructed indirectly. Fix the exact target, values, property/transform
tolerances, initial history, observation phases and controls in a later
reviewable execution protocol; none is an executed result here.

This second condition can distinguish an intended **field-level** update from
the engine's existing **whole-property** rule. `MaterialProperties` is one
[record-valued entity property](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/Render/Renderer3d.fs#L77)
containing albedo and roughness among other fields. Its ordinary
[getter/setter and static-model default](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/World/WorldFacets.fs#L2778)
operate on that record; `StaticModelFacet` uses `MaterialProperties.empty`
at line 3212, and the [actual palm dispatcher includes that facet](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/World/WorldDispatchers.fs#L588).
The propagation loop compares entire property symbols at
`WorldModule2.fs:614–651`, with separate missing/default branches. It does not
recursively merge record fields. Thus a differing roughness record **may also
retain its old albedo** under the inspected branch. That is a source-derived
prediction to test with actual serialized/effective values, not a material
result from the earlier Button/Text fixture. If a plain push fails the authored
requirement, retain that mechanism result and count any explicit reconciliation
needed to deliver the revision.

The existing graph adds a second cost boundary. After updating direct targets,
the public wrapper examines their ancestors and propagates those with their
own targets (`WorldModule2.fs:752–777`). Seven palm targets sit under the source
Villa, which itself has three targets with 43 children each. The inspected
route can therefore rebuild whole Villa trees as well as individual palms.
This is a prediction from the saved graph and implementation, not an observed
reconstruction count, elapsed time or native-effect result. Observe the actual
affected set and total reconstruction work; do not charge only 31 leaf updates.

For this existing-scene revision, permit an ordinary batch helper that reads
each declared target's material record, changes only the required field and
writes it back, followed by the same save/reopen and outcome checks. An explicit
roster, ordinary selection or parameter table is valid if its construction and
maintenance are counted. Do not handicap this alternative to manual editing
of every copy, or give it the target roster and resolved defaults for free.
Likewise, existing propagation links/history are supplied setup in the Nu
condition; an incremental edit comparison does not measure their creation cost.

For the broader construct-and-revise question, the ordinary F# precedent is
[Twenty 48's tile comprehension](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Projects/Twenty%2048/GameplayDispatcher.fs#L84):
stable instance names, shared properties and instance-dependent placement,
text and images. `Content.composite` supplies named child composition. A
parameterized family with explicit overrides is therefore a credible proposed
alternative, but the existing precedent is MMCC while Terra Firma loads the
scene through ImSim. Translation, integration, correct initializer/update
policy and behavioral equivalence are real work, not an established drop-in
substitution. Keep that total-work comparison separate from a single batch edit.

**Next:** first observe the unchanged scene's actual loaded tree, effective
properties, links/history and save/reopen correspondence under a pinned host.
Then accept the common revision protocol and ordinary batch route before
comparing delivery, failure/repair and complete work. A failure to load or
preserve the required starting artifact is a feasibility result, not a reason
to silently replace it with a cleaner successful fixture. Visual tint, physics,
Gaia/agent access and human authoring effort each need their actual observations;
property equality alone proves none of them. Candidate/participant allocations
and the R02/R10 returns remain unchanged.

The scene is 218,933 bytes and 6,261 lines, SHA-256
`1dff90c5679233f6b282e03bcb2f2fd7524a6e6e93a7df814a72f5260d3a421a`.
It matches the retained original Nu archive byte for byte. Private structural
extraction, selected source spans, identities and the bounded assistant's
loading/composition handoff are under `.artifacts/r12-propagation-20261018/`.
The parent checked the consequential loader, composition, property and ancestor
branches. This pass parsed the whole descriptor structure and read selected
source bodies; it is not a complete semantic reading of all scene properties,
a new publication reading, or an additional runtime trial.

#### 2026-10-18 executed load/save/reopen prerequisite

The [native feasibility record](nu-terra-firma-reopen-feasibility-2026-10-18.md)
now observes one corrected original-scene L0 and actual-save fresh-process L1
under functional, accompanied, halted execution. All 197 original named
entities, 166 explicit links, 11 source-bound saved histories and the declared
configuration of four Villas/32 palms pass. The 36 generated declaratively
protected children remain separate, and the saved tree contains the original
197 names. L1 consumes L0's exact save; byte equality to the original file is
not the tested property.

The first native process completed but emitted invalid Symbol wrappers/origin
metadata. It remains retained and unscored; only the reviewed three-call
formatter correction and recompiled observer supply the passing pair. The
failed build, rejected reviews, failed small proof and restart-interrupted
work also remain. This is one corrected feasibility pair, not independent
replication or a complete-work advantage.

**Updated next action:** bind the common shared-tint/local-roughness revision
and ordinary batch protocol against this observed baseline. Keep all other
declared configuration, the indirect Villa reconstruction boundary, actual
save/reopen, repair and complete work explicit. Source propagation under that
change, visible appearance, practical demand and ordinary editing access remain
unobserved; the preservation prerequisite does not establish them.

#### 2026-10-18 accepted revision comparison

The [revision construction record](nu-terra-firma-revision-feasibility-2026-10-18.md)
now binds the common shared-tint/local-roughness requirement and ordinary
batch operation in an accepted prospective protocol. Each operation receives
the same existing family metadata and must preserve all declared configuration
on every original entity. Propagation and batch have different allowed saved
history consequences; those are reported separately from the common required
material outcome. Every eligible reopen consumes its own actual save,
including an adverse one.

The lifecycle recorder has a separate callback counter and contiguous
ordinals, plus address/ID transition checks; final IDs alone cannot count
intermediate repeated reconstruction. The predicted 163 original-entity
occurrences are a falsifiable expectation, not a run-validity requirement.
The construction record owns current review, compile and execution gates.
No native revision outcome or complete-work advantage follows from the
accepted protocol or synthetic controls.

#### 2026-10-18 revision observations and integrity return

The [execution record](nu-terra-firma-revision-feasibility-2026-10-18.md) first
completed P-shared, B-shared and P-local revise/actual-save reopen pairs.
Both shared cases deliver all 32 tints. P-local retains the selected palm's
roughness but also its old albedo, so only 31 receive the tint; faithful
reopening does not cure this authored requirement failure. Other declared
configuration, links and raw-history preservation pass. Propagation's exact
current-source/history check separately finds regenerated Order differences
after fresh reopen. Batch retains its old histories, whose later maintenance
consequences remain untested.

Propagation records 160 original reconstruction pairs over 139 changed IDs,
versus the frozen prediction of 163. Three same-name copied palms have one
pair rather than two; pinned address/filter behavior explains that pattern
without changing the prediction or claiming total native work. B-shared has
no operator lifecycle events or original ID changes. The missed P-local target
itself is rebuilt twice, keeping the field-intent failure separate from the
three-address prediction divergence.

The first B-local attempt fails the original-scene integrity guard before any
edit. Its three changed staged inputs make that attempt invalid/incomplete,
and its reopen remains ineligible. The
[storage return](workspace-integrity-return-2026-10-18.md) preserved the failed
attempt and a verified C: recovery copy. After clean CHKDSK snapshots, exact
input revalidation and prospective acceptance, the separate
[two-process continuation](nu-terra-firma-revision-continuation-2026-10-18.md)
now completes B-local and its own actual-save reopen. All 32 tints, selected
roughness, other declared configuration, links and old histories pass, with
zero operator lifecycle callbacks or changed original IDs.

Four revision/reopen pairs are complete across nine processes, including the
invalid startup. Batch's retained histories and propagation's advanced
histories remain different endpoints; their later maintenance consequences
have not been executed. A practical comparison must count helper construction,
verification, failed work, repair and history consequences. These observations
do not establish a general reuse, authoring or steering advantage; the separate
R02/R10 returns remain stopped.

#### 2026-10-18 next comparison: continued use and workflow switching

The practical decision is whether a level author maintaining these placed
props should use public source propagation, a reusable field-update helper,
or a declared combination when shared revisions must retain independent local
fields. The existing maintainer rationale and S254's reuse accounts support
that decision frame; they do not establish its frequency, independent demand
or a productivity effect. Existing family links remain supplied setup, with
the selection/helper and verification work recorded separately.

The next maintenance question concerns a second shared albedo revision from
each workflow's **actual saved endpoint**, retaining the specified roughness
and unrelated configuration. The first stage keeps its original result:
P-local's missed tint remains failed delivery even if a later operation fixes
it. Saved histories are inputs to the next operation, not metadata to normalize
into a preferred reference before comparison. The invalid B-local startup has
no successor; the accepted L0-02 save is the eligible batch/local endpoint.

| Question | Eligible continuation | Interpretation |
| --- | --- | --- |
| Continued batch use | B-shared/B-local followed by the same field-update policy | Leaving propagation history unchanged is not a failure by itself. Test the new and retained material/configuration obligations. |
| Continued propagation | P-shared/P-local followed by public propagation, with any repair policy prospectively separate and explicit | Count failed delivery, reconstruction and any subsequent selection, repair and verification. A repair may use an ordinary helper; its work is not free. |
| Switching from batch to propagation | B-shared/B-local followed by public propagation | This is a compatibility diagnostic for choosing that switch. It is not the main batch policy and cannot alone establish that continued batching is worse. |

A history-source difference is consequential only through a stated future
operation or guarantee. Do not impose equal serialized histories as a common
success rule when the workflows legitimately use different policies. Conversely,
retaining a link does not establish that every later propagation will express
the author's field-level intent. The pinned reconciliation branches and actual
saved descriptors must determine the next prediction; then native observation,
if assigned, must test it independently. Source inference is not execution.

The comparison must separate one-time selection/helper construction from each
revision's editing, verification, failed work and repair. Charge any history
refresh or workflow conversion explicitly and preserve its pre-refresh input.
Report intermediate delivery and final recovery separately, following the
[R09 actual-history contract](nu-change-sequence-contract-2026-10-11.md).
Repeated edits to these same props do not add independent applications or
participants. Instrumented process time and property-write counts remain
mechanism observations until ordinary editing access and complete work can be
measured under a declared policy.

This selects the next decision and valid comparator policies; it assigns no
additional native process or candidate and changes no frozen package. A later
execution protocol still needs exact revised values, actual predecessor hashes,
operator/repair order, observations, controls and limits before acceptance.

#### 2026-10-18 retained-history audit: a conditional switching prediction

A read-only audit now binds the four actual saved L0 endpoints to their
receipts and inspects the next material-comparison branch at the existing
Nu pin. Propagation stores the first tint in its Palm source history and all
eight nested Palm histories in the source Villa. Batch preserves the older
histories, where those material properties are absent. All 32 current palm
descriptors explicitly contain the edited material in both batch cases.

The [property branch](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/World/WorldModule2.fs#L614)
compares the whole material symbol with the previous source value when one is
present. With no previous value, it instead compares the target with its
[dispatcher/facet default](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/World/WorldFacets.fs#L3212).
For these RigidModel entities the material default has sixteen unset fields.
A batch-tinted record differs from that default and is preserved as a local
whole-property change; missing history does not make it adopt the new source.

**Conditional source prediction, not a new execution:** change only the source
Palm's albedo to a distinct value, then invoke the unchanged public propagation
wrapper from each retained endpoint, without refreshing histories or changing
dispatchers, overlays or links.

| Actual saved predecessor | Palm / nested Villa histories contain first tint | Predicted palms receiving the later albedo, including edited source |
| --- | --- | --- |
| P-shared | Present / 8 of 8 | 32 of 32 |
| P-local | Present / 8 of 8 | 31 of 32; selected roughness target retains its prior material |
| B-shared | Absent / 0 of 8 | 1 of 32; only the edited source |
| B-local L0-02 | Absent / 0 of 8 | 1 of 32; only the edited source |

The same-name address filter does not supply an exception: 28 targets have a
direct route, 24 copied-Villa palms have an ancestor route, and 21 have both.
The three copied palms named exactly `Palm` use only the ancestor route.
The batch Villa history also lacks their material property, so its default
comparison preserves the old tint. After a direct propagation update in P,
an ancestor comparison may preserve the already-new value rather than replace
it again. These route consequences are source inference; no second-revision
callback or native outcome has been observed.

The parent checked the material/default and direct/ancestor source branches,
four source-file identities, twenty receipt/capture/save identities, and the
critical saved-versus-Settled material, overlay, facet, link and history fields
for all 32 palms plus Villa in each case. The retained original result checks
supply the save/reopen preservation evidence; this audit does not repeat those
native processes. P's Order-only correspondence findings remain separate and
unchanged.

Private evidence is under the C: recovery root's
`r12-history-followup-20261018/`: `r12-history-followup-evidence-01.md`
(SHA-256 `596b4d3ed467331bd7344305ac575e925e25d779332213f79bd595fe0619caf5`),
`history-branch-derivation-01.json`
(`7b8b29e56d337b2c3397ae37e8634d25411efa6a066036e7b02ce5d4c0124def`),
and the script, parent acceptance and three retained parser-only failures.
No frozen input, operator, oracle or native result changed.

This resolves the source-level reason to distinguish continued use from a
switch. It neither makes the original batch result adverse nor estimates
future maintenance effort. A continued field-wise batch, explicit history
refresh, changed overlay or a target returned to the all-unset default is a
different case. Any practical execution must now choose its policy and charge
conversion/repair work explicitly; the source prediction alone does not
justify adding more cosmetic revisions.

### 2026-10-23 next construction: explicit field policy and credible rivals

The [development-history audit](nu-development-history-audit-2026-10-23.md)
establishes whole-Nu-property override preservation as the public abstraction.
Material-field independence is our authored requirement. It also separates
the accepted #946 repair from an abandoned sibling and distinguishes group
save/reopen from standalone export. Preserve the original strict Order/history
findings; a future contract should observe effective child sequence and raw
provenance separately, with no retrospective oracle relaxation.

The [status-quo audit](nu-status-quo-and-transfer-audit-2026-10-23.md)
credits ordinary Unity/Unreal selective inheritance and Godot's two valid
material workflows. Existing merge and correspondence literature supplies
relevant methods. The next local construction candidate is the least invasive
explicit material-field policy that can retain declared local choices across
family revisions. Compare it with the already-successful field-update helper
and unchanged public propagation with a declared repair policy. This is an
integration/value question, not a claim that three-way merging is new.

Before construction, bind initial family/target state, the selected field
meanings, same-field and equal-to-base local intent, reset/absence semantics,
eligible coupled-field constraints, conflict/rejection policy and actual saved
predecessors. State whether provenance advances after success, partial delivery
or rejection. Count setup, representation and metadata, selection/editing,
validation, unsuccessful work, repair, save/reopen and later conversion. The
information boundary and falsifiers are in the audit; they are prospective
discriminators, not a compulsory new matrix or completed protocol.

The initial P-local missed tint, valid batch outcomes and later-switch source
prediction remain unchanged. Any new comparison must show a useful outcome
beyond merely reproducing the successful batch and must accept equal/better
ordinary alternatives. No new native process, helper, shader, engine port or
candidate run is added by this continuation.

### 2026-10-23 construction correction: credit the intent-aware helper

The [follow-up decision](nu-material-intent-baseline-2026-10-23.md) identifies
the least-invasive mode table plus field update as the strengthened ordinary
baseline itself. A separate treatment label does not create a comparison.
The accepted [component contract](../experiments/nu-r12-material-intent/CONTRACT.md)
uses a paired companion document, explicit equal-valued pins and immediate
return to source inheritance. `ValueNone` means imported material fallback,
not source inheritance. No historical merge base or invented coupled-field
invariant is needed for this bounded policy.

The construction first checks the component on synthetic paired inputs.
Actual Nu save/reopen, editor integration and complete-work benefit remain
separate. A future observer must sort sibling identities by `GetOrder`, not
by names or raw set enumeration; fresh numeric Orders are not portable state.
The old runtime outcomes and strict history findings remain unchanged.
