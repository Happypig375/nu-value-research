# Ordinary material-field intent helper: component contract v1.1

Frozen for component construction on 2026-10-23, before implementation or
execution. This is an ordinary application helper, not a distinct Nu treatment
or a novel merge algorithm. It strengthens the baseline that already delivered
the shared tint while retaining independent roughness. A later integration must
beat this capability or reduce complete observed work under a practical task.

This contract assigns a dependency-free F# component and deterministic controls.
It does **not** assign a new Nu process, editor workflow, participant or model
candidate. Actual native integration needs a separately sealed package and
prospective process acceptance. The R02/R10 returns remain in force.

## Meaning and boundary

The helper manages only `AlbedoOpt` and `RoughnessOpt` on a fixed, supplied
family with one source and distinct targets. Values use the same meanings as
Nu's material options: an absent option requests the imported asset's value;
an explicit option supplies a renderer override. An absent option is **not**
source inheritance. For each target and each managed field, explicit `inherit`
or `pin` metadata records whether later source edits should replace that field.
The pinned value remains in the scene. There is no duplicated value in metadata,
historical merge base, inferred intent, conflict solver or transaction layer.

A target pinned at a value equal to its source remains pinned. `Pin(ValueNone)`
is valid and differs from inheritance. Releasing a pin adopts the source's
current option immediately and follows its future revisions. This is an
authored policy. It does not claim to describe Nu's existing public propagation.
No albedo/roughness domain invariant has been established or is imposed.

The component consumes the complete family material map for the two fields,
including its source. Its output specifies updated two-field values and modes;
a later Nu adapter must preserve the other fourteen material fields by reading
and updating the existing record. This component neither parses `.nugroup`
symbols nor verifies that supplied values came from a live Nu world. Those are
adapter and independent observation obligations.

## Persistent representation and inputs

Use an application-owned UTF-8 JSON companion document, with these required keys:

```json
{
  "schema": "r12-material-intent/v1",
  "sequence": "a nonempty sequence identity",
  "generation": 0,
  "scene_sha256": "64 lower-case hexadecimal characters",
  "source": "the full logical source address",
  "members": {
    "a full logical target address": {
      "AlbedoOpt": "inherit",
      "RoughnessOpt": "inherit"
    }
  }
}
```

The target key set must exactly equal the supplied family minus the source;
the source must occur exactly once in a nonempty, unique family. Each target
must have both known mode keys. Reject duplicates anywhere in JSON, wrong
required types, unsupported schema/modes, missing or extra target addresses,
empty identities, negative/nonintegral generations, and nonfinite supplied
material numbers. Do not silently default missing metadata or infer it from
current values. Unknown top-level JSON properties and extra properties within
a known member entry are opaque extensions and must survive parse, operations
and serialization semantically,
including nested arrays, numbers and objects. Formatting need not be identical.

Explicit initialization creates generation zero with all targets inheriting.
It is a separate operation, never a fallback for failed loading. Loading
computes SHA-256 from the supplied exact scene bytes and checks the document's
hash, expected sequence, generation, source and family **before** any operation.
The caller must supply actual scene bytes and observe their material values;
passing this component check alone does not validate a full staged application.

An operation produces a new draft without mutating its input policy, material
map or unknown extensions. Binding a completed scene save computes its hash
from exact saved bytes, advances generation by exactly one, and preserves the
draft modes/extensions. It returns the companion JSON; it does not write scene
or policy files, call Nu, advance an external receipt, or claim atomicity.
Initialization, loading, operation and binding must therefore be separable.
An unknown property inside a member remains opaque even if its value is the
string `inherit` or `pin`; only the two named fields are managed. Extra address
keys in the `members` roster or in the supplied material map remain invalid.
This distinction was clarified before the first component build in v1.1;
the original submitted v1 and its review remain in the private attempt record.

## Operations

- `ReviseAlbedo(value)` changes the source albedo and every target whose albedo
  mode is `inherit`; all pinned albedos and all roughness values/modes remain.
- `ReviseRoughness(value)` has the symmetric meaning.
- `PinAlbedo(target, value)` sets only that target's albedo value and mode,
  even when its value equals the source. `PinRoughness` is symmetric.
- `InheritAlbedo(target)` changes only that mode to `inherit` and immediately
  copies the current source albedo. `InheritRoughness` is symmetric.
- Pin/release requires a known target, never the source. An unknown target,
  incomplete/extra material map or invalid field value rejects without a
  partially returned result or mutation. No automatic reconciliation of an
  unrelated field is authorized by an operation.

Operations may compose in one declared stage before a single binding. Equal
value writes may be omitted by the eventual adapter; mode changes must remain.
Returned values, not attempted setter counts, determine the material outcome.

## Required component controls

Use the existing 32-palm Terra Firma address roster (four Villa paths, eight
named palms each), source `Game/Gameplay/Scene/Villa/Palm`, and local target
`Game/Gameplay/Scene/Villa-0002/Palm-0009`. The native asset/version identities
remain in the accepted [revision protocol](../nu-r12-terra-revision/PROTOCOL.md).
Component fixture scene bytes are explicitly synthetic binding inputs, not
native saves, and cannot establish Nu persistence.

The expected sequence is declared before running the component:

1. Start with all material options absent and all target modes inherited.
   Revise family albedo to A = `(0.25, 0.5, 0.75, 1)`. All 32 take A.
2. Explicitly pin local albedo at A and local roughness at `0.75`. All albedos
   still equal A, while both local modes are pinned. Persist/reload the policy
   and exact paired synthetic scene bytes between every numbered stage.
3. Revise family albedo to B = `(0.75, 0.5, 0.25, 1)`. The local target retains
   A and roughness `0.75`; the other 31 albedos take B.
4. Release only local albedo. It immediately becomes B and inherited; its
   roughness remains pinned at `0.75`.
5. Revise family albedo to C = `(0.5, 0.25, 0.75, 1)`. All 32 take C, while
   local roughness remains `0.75`. Reload and verify the final modes/values.

These exact later values are known to the maintainer during construction.
This is a prospective authored conformance discriminator, not evidence that
an independent author committed an unforeseen future exception or that the
requirement is prevalent. Do not turn temporal fixture order into such a claim.

Additional controls must establish:

- a pinned absent option survives a distinct source revision while an inherited
  absent option follows it; explicit release adopts an absent source option;
- roughness revision/release obey the symmetric rule and do not change albedo;
- equal-value mode changes survive serialization, and losing/flipping that mode
  is detected independently of values;
- missing metadata, wrong paired scene bytes, wrong sequence/generation/source,
  duplicate JSON keys, malformed modes, and missing/extra target/material keys
  reject before producing a successor; initialization is never an error rescue;
- an opaque extension with nested data survives all operations and bindings;
- inputs remain unchanged on accepted operations and rejection; successive
  drafts can be used independently, without shared mutable JSON aliasing.

The controls must make observable assertions against these fixed outcomes,
not merely reproduce the implementation's update loop. Preserve all failed
builds/checks and submitted review findings. Five unresolved failures at one
unchanged construction gate require return; errors of different classes do not
restart that count. A successful gate resets its counter.

## Native continuation and work boundary

The next native package should reuse the original Nu pin, eight unchanged
application source units, 189-file host and 251 published assets, revalidated for
the new C: composition. It should execute one of the five declared stages per
fresh process, from the **actual** immediately preceding saved scene and
companion, followed by a final no-edit reopen. Before assigning it, freeze its
observer phases, complete provenance/eligibility rules, sibling-order channel,
controls, source/PDB/build seal and per-attempt input/time/callback limits.
This paragraph is preparation, not acceptance of a runnable package.

The intended native scope is incremental revision of the supplied family.
Existing family creation and asset import are supplied costs, not zero adoption
costs. Record construction, metadata, selection, operations, validation, failed
work and repair, save/reopen and environment work. Retrospective active human
time is unavailable; machine elapsed and property-write counts are descriptive.
No productivity or comparative savings claim follows from this component.

A complete adverse saved scene and its actual companion remain evidence and
the actual predecessor for a declared continuation. Semantic failure must not
be replaced by a favorable reference. An incomplete or unbound pair is
ineligible; retain any partial files and do not advance by substituting intent
from requested values. The helper provides no crash consistency or rollback.

Native integration, ordinary editor use, copy/rename/export behavior, visual
rendering, practical demand, complete-work advantage and non-game transfer
remain unestablished. A sidecar helper must not be relabeled as a new treatment
while the comparator is denied the same information or ordinary machinery.
