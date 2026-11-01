# R12 Terra Firma: shared material revision with a local override

Prospective protocol draft, 2026-10-18. Independent and parent acceptance of
this contract, then source/checker controls, compiled-source/host verification
and native acceptance are required before execution. No revision has run.
The user authorized confident local construction and experiments. R02 input
and R10 migration remain stopped; no task-solving candidates or participants
are allocated here.

## Decision and common requirement

Does one ordinary source propagation deliver a shared palm tint while keeping
an independent local roughness choice, compared with a batch field update on
the same existing family? Observe collateral configuration changes and actual
entity reconstruction as well as delivery. This is an authored maintenance
requirement on a real existing asset, not a mined request, a prevalence claim,
a human/agent productivity experiment or an alternative-engine comparison.

All 32 existing palms must have `AlbedoOpt = ValueSome (0.25, 0.5, 0.75, 1.0)`
in RGBA single-precision components. Preserve their other material fields,
transforms, shape/asset configuration and the declared unrelated scene state.
Two conditions are assigned independently from the same original scene:

| Condition | Common preparation before either operator | Required final result |
| --- | --- | --- |
| shared | No local material edit. | All 32 receive the tint; their other material fields remain at the observed baseline. |
| local | Set only `RoughnessOpt = ValueSome 0.75f` on `Game/Gameplay/Scene/Villa-0002/Palm-0009`, using its current record. | All 32 receive the same tint; that target alone retains the roughness override. |

The selected local target is inside a copied Villa, so it lies on both the
direct palm propagation route and the indirectly reconstructed ancestor tree.
The values are fixed, exactly representable probes of the required field
mapping; no visible color/roughness or rendering-quality claim is assigned.

## Starting artifact and supplied setup

Use Nu `064f7ae92a8506689cd91aff5e6804a375d6ef3d`, the original Terra Firma
Scene.nugroup SHA-256
`1dff90c5679233f6b282e03bcb2f2fd7524a6e6e93a7df814a72f5260d3a421a`,
and the accepted asset preparation and application host from the
[load/save/reopen prerequisite](../../docs/nu-terra-firma-reopen-feasibility-2026-10-18.md).
Reuse the verified published assets; no new pipeline invocation or engine
rebuild is needed. The actual runtime host Nu.dll must remain SHA-256
`e96cd61d188c689f7e39e2670b4d8582e26b9ea2dc95e1a15056891b7c99cd68`.
Keep all eight original application units unchanged. Adapt only the external
Program observer/operator, with SDK 10.0.302, original App.config,
ServerGC/TieredPGO settings, real TerraFirmaPlugin and the same isolated
functional, accompanied, halted hidden SDL/OpenGL setup. This remains an
assembly-reference adaptation with the earlier native provenance limits.

The original tree has 197 named entities, 19 roots, 166 explicit links and
11 saved source histories. The four Villa names are `Villa`, `Villa-0002`,
`Villa-0003`, `Villa-0004`. Each has eight palms named `Palm`, `Palm-0009`,
`Palm-0010`, `Palm-0011`, `Palm-0012`, `Palm-0013`, `Palm-0014`, `Palm-0016`.
The sole palm source is `Game/Gameplay/Scene/Villa/Palm`; all other 31 palms
link directly to it. The three copied Villas link directly to `Villa`.

The corrected prerequisite observes all 32 palms' effective MaterialProperties
as the same 16-field all-ValueNone record. None of their original property maps
or the palm source's old history contains a MaterialProperties entry. The
Villa source history has 44 descriptors, including 21 non-palm material records
in the older ten-field layout. Preserve these actual histories; do not refresh,
normalize, replace or pre-propagate them to produce a cleaner starting state.

The private baseline inventory binds corrected L0 A/B and original-expectation
hashes; its JSON SHA-256 is
`b8e73df8ccca375fbf3a95d879057637b25374c621fb065f9672fc9c757cd6e6`.
All 2,351 original explicit properties were observed without errors or A/B
differences. This informs the prospective preservation oracle; the new runs
must still observe their own starting values and establish the preconditions.
Baseline entity IDs are not assigned to a new process.

Existing links/history are supplied setup in both treatments. The batch
operator may use those links for family selection: source plus its current
public `GetPropagationTargets`, materialized and sorted by full address.
This must equal the 32-address family before either treatment. That choice
isolates the update operation given existing family metadata. It does not
compare the cost of creating metadata, discovery in an unstructured scene,
or an independent selection tool. Record the inventory/selector construction
as maintainer preparation; no roster or custom helper is treated as free
authoring work or a previously available end-user feature.

## Assigned operators and sequence

| Operator | One assigned edit action after common preparation |
| --- | --- |
| P: public propagation | Read the source palm's current material record, replace only AlbedoOpt, write it once, then call `World.propagateEntityStructure source world` once. Do not suppress its ancestor propagation or repair any target. |
| B: ordinary batch | For each of the same 32 addresses in ordinal address order, read its current material record, replace only AlbedoOpt and write it once with the public setter. Do not call propagation or write saved histories. |

Both are within-Nu public-API operations under identical observation access.
The batch may preserve independent fields explicitly; it is not restricted to
32 manual UI edits or a whole-record overwrite. A bespoke batch is still
construction work. The public propagation wrapper remains unchanged; copying
its algorithm or silently adding field reconciliation would be a new treatment.

Assign the fixed order `P-shared`, `B-shared`, `P-local`, `B-local`. Each has
one revise process and, when eligible, one fresh reopen process immediately
after it: at most eight initially assigned native processes. Every revise
starts from the original scene in its own application copy; cases do not
inherit a successful reference or another condition's history. The order is
not randomized and the runs are not independent statistical replications.

Use the same compiled observer/operator for all four cases and their reopens.
Bind role, condition, operator, exact source/build/host, input scene and
predecessor receipt in every attempt. Reopen uses the exact actual save of
its own completed predecessor, including an adverse one. No source edit,
local override, propagation, batch action or repair occurs in a reopen.
Do not replace a failed predecessor with a reference output.

## Fixed phases and observation

On the first external preProcess, subscribe a Game-owned, cascading observer
to the public Entity lifecycle stream, then set GameState to Gameplay once.
This bypasses Play/Gaia input as before. The observer records events without
altering the world or resolving them. Keep requested and observed runtime,
GC, window, selection, mode and clock fields separate.

For each revise process:

1. Capture **Loaded** at the first postProcess where Scene exists, regardless
   of counts or desired values. Keep every earlier phase record.
2. At the immediately following postProcess, capture **Ready**. Verify the
   fixed original correspondence, graph, histories, selected configuration,
   functional/accompanied/halted Gameplay mode and the all-None palm records.
   Missing/incorrect setup prevents the assigned operator; retain the attempt.
3. Perform the condition's one declared local roughness write, or no write in
   shared. Capture **Prepared** in that same callback. Require precisely the
   declared preparation difference, with all links and old histories intact.
4. Invoke the assigned operator once; capture **Applied** immediately on its
   return, even if the required output is wrong. No final scoring or desired
   result chooses a retry, repair or later observation phase.
5. At the next postProcess, capture **Settled**, save once through
   `World.writeGroupToFile`, reparse it and compare its canonical descriptor
   to the Settled in-memory descriptor. Exit normally and retain cleanup.

Capture any partial phase and exception. The observation callbacks are fixed;
there is no wait for the scene to become favorable. Use the same 120-callback
and 180-second native limits as the prerequisite. A timeout or failed cleanup
is not complete delivery. An invalid common observer/setup gate stops further
use of that harness pending a bounded diagnosis; no automatic replacement
fixture or enlarged deadline is allowed.

For each eligible reopen, capture **ReopenA** at first Scene-exists and
**ReopenB** at the next postProcess, then save once and exit. Compare those
captures to their actual predecessor's Settled values and the common required
outcome separately. Reopening an adverse save faithfully is not successful
delivery of the tint requirement. A complete parseable save and required
observations make an adverse predecessor eligible; incomplete observations,
no usable save or failed process leave the reopen unrun and accounted for.

## Configuration and history oracle

The independent checker must reconstruct the fixed named tree using descriptor
child lists only; nested history never adds live entities. Preserve all raw
descriptors and property symbols privately. Use the accepted raw Symbol
formatter; never convert historical records to the current material type for
equality. The operator's chosen target list is not the final oracle's source
of truth: the oracle derives the fixed family from the original descriptor
tree and checks the exact 32 addresses independently.

At Applied and Settled, and again at both reopen captures, require:

- The original 197 names, parents and dispatchers, original named child
  membership, persistence and protection. Record all generated children
  separately, including their actual appearance/disappearance.
- All 32 palms' required albedo; the prepared roughness choice and every other
  material field unchanged. Check fields by name with the fixed 16-field
  layout, including absent versus ValueNone versus ValueSome distinction.
- Every other original explicit property and the prerequisite observer's
  selected effective property set on every original entity preserved from
  Prepared, except the assigned palm AlbedoOpt and allowed history changes
  below. Retain expected missing optional properties as missing, and report
  new/missing/error observations explicitly. These are declared observed
  configuration obligations, not every possible engine property or behavior.
- For Position, PositionLocal, Rotation, RotationLocal, Scale and ScaleLocal
  only: finite components and absolute tolerance 0.0001. Size, Offset and all
  other declared fields use structural equality; the material values have
  exact specified components. IDs are descriptive and need not survive a
  revision or fresh process. No native identity is inferred from an ID.
- The same 166 links, all resolving to their original source addresses;
  no newly linked original entity. The saved named tree contains exactly the
  197 originals and each saved descriptor matches its in-memory endpoint.

Saved histories are treatment-specific consequences, not a forced equality
between unlike operations. Batch must preserve all 11 original raw histories.
Propagation may advance only the Palm and Villa source histories; the other
nine must remain unchanged. Record their full structures and correspondence
to current source trees, excluding only the top-level self-history field
when comparing a source's saved descriptor to its current serialization.
Do not strip nested history or material fields. Preserve actual histories
unchanged through that case's save/reopen. Any unexpected history-source set,
nonselected history change or failed correspondence is reported separately
from the common tint/configuration outcome. These runs do not test the later
maintenance consequences of the two operators' different history states.

## Reconstruction observations and work boundary

Use `Game.LifeCycleEvent (nameof Entity)`, whose RegisterData and
UnregisteringData carry the affected Simulant. Increment a callback-side
monotonic counter before any kind/address classification and assign that
ordinal to every recorded callback, including other kinds and out-of-scene
events. Record phase, kind, address and entity ID while available. The Game
subscription survives target reconstruction. Preserve all events and delimit
load, preparation, operator, settling, save and cleanup; only the declared
operator interval supplies its immediate observed lifecycle count. Save the
final callback counter separately from the record array, never deriving it
from the retained array's length. Require the full serialized stream's ordinals
to be exactly 1 through that counter, including callbacks during cleanup.

Reconcile the event stream against before/after identity maps: registration
adds a live address/ID, unregistering removes that same address/ID, and the
result must match the captured live map. Endpoint conservation alone cannot
detect a lost balanced intermediate register/unregister pair at an address
rebuilt twice. The separate callback count and contiguous ordinals check
recorder omissions, including that balanced case; endpoint maps check local
identity transitions. Keep generated entities and original entities separate.
Changed final IDs alone cannot count multiple rebuilds. Trace-conformance
failures leave the affected lifecycle measure unestablished; do not relabel
them as Nu configuration failures or discard otherwise observable adverse
configuration. These checks do not independently prove that an internal action
emitted an event or that another subscriber did not prevent its delivery.

Source and graph predict 31 direct palm reconstructions plus three complete
44-entity Villa trees: 163 original-entity reconstruction occurrences, with
24 copied palms reconstructed twice and 139 distinct original addresses
affected. The per-original-address prediction is 24 copied palms with two
unregister/register pairs, 115 other addresses with one pair, and 58 with none.
Batch predicts zero pairs at every address. These are falsifiable predictions,
not required success/validity counts or permission to stop observing early.
A coherent recorded multiplicity that differs is prediction divergence;
report it and resolve any remaining emission/delivery uncertainty before
asserting a complete internal reconstruction total. Never repair or filter the
trace to match the prediction. Record observed registration/unregistration,
ID changes, extra entities and exceptions. These are public managed lifecycle
observations, not native allocations, body/contact preservation, frame
completion or total CPU/authoring work.

Retain all asset reuse, source changes, builds, controls, reviews, failed
attempts, preparation and integration. Record operator/property-write counts
and process/phase times as descriptive instrumented observations. The common
observer imposes unequal event-recording work when one action emits more
events. No speed, complete-work or productivity advantage is estimated from
these single fixed-order cases. An eventual practical comparison must include
selection/helper construction, verification, failure and any explicit repair;
repair is not assigned inside these first operations.

## Falsifiers, controls and disposition

The source-derived prediction is that P-shared delivers all tints, while
P-local retains the local target's whole differing material record and leaves
its old albedo. Both batch cases are predicted to deliver the field-wise
requirement. A contrary complete observation revises that prediction; a
predicted tint failure remains **adverse delivery**, never a passing task.
Unexpected collateral changes are adverse even if all palms receive the tint.

Before native acceptance, synthetic checker controls must demonstrate: a
missed tint is adverse in either condition; lost roughness is adverse; an
unrelated property or history change is adverse; transform tolerance does not
apply to Size/Offset; missing original entities and added saved entities are
detected; wrong input/predecessor, phase/order, observer/host, outcome-filtered
capture and changed sealed bytes are invalid; an adverse complete predecessor
remains eligible; unbalanced lifecycle changes fail identity conservation;
and dropping a balanced intermediate register/unregister pair fails the
callback-count/ordinal check even though its endpoint map still agrees. Check
duplicate and trailing record losses against the same independent counter.
A complete self-consistent synthetic stream with different multiplicities
must be reported as prediction divergence rather than forced to 163. Mark
synthetic data explicitly. Reuse unchanged provenance controls where applicable
and record the new cases and exact source tested.

Wrong source/setup/mode, a missing required observation, observer failure,
exception, failed cleanup or deadline leaves the affected comparison invalid
or incomplete. Correctly observed violations after the assigned operation
are valid adverse evidence. Keep semantic, history and lifecycle dispositions
separate and preserve all assigned work. No favorable-only selection or
post-result policy change is allowed. Five unresolved failures at one
unchanged construction gate require return; success does not erase failures.

The result can support the selected within-engine update-policy and
reconstruction comparison only. Visuals, interaction, native lifetime,
physics continuation, ordinary Gaia/agent access, task demand, general reuse
effort, human steering and benefit require separate evidence.
