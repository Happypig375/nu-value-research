# Ordinary material intent reference component

This small F# component implements an ordinary field-update helper with explicit
per-target inheritance/pin metadata. It is the strengthened baseline for the
[R12 material question](../../docs/nu-material-intent-baseline-2026-10-23.md),
not a new merge algorithm or demonstrated Nu advantage.

The [prospective contract](CONTRACT.md) defines its input validation, exact
operations, five-stage example and negative controls. It has no Nu, graphics,
filesystem-save or network dependency. The executable is a deterministic
component control suite, not an engine experiment.

## Run the controls

With the pinned .NET SDK 10.0.302, from the repository root:

```text
dotnet run --project experiments/nu-r12-material-intent/R12MaterialIntent.fsproj -c Release --no-launch-profile --artifacts-path .artifacts/r12-material-intent-check
```

Exit zero means all asserted component outcomes and expected rejections passed.
The console prints their names and a final summary. The full Linux and Windows
CI jobs run this same component with build outputs in runner temporary storage.
No engine assets or credentials are needed.

## API and responsibility boundary

[MaterialIntent.fs](MaterialIntent.fs) provides immutable material fields,
modes, opaque policy/draft values, and these operations:

1. `initialize` explicitly creates all-inherit metadata at generation zero.
2. `load` validates the document and checks its sequence, generation, source,
   family and SHA-256 against supplied exact scene bytes.
3. `prepare` receives the caller's actual two-field material map.
4. `apply` / `applyMany` revise a family field, pin a target field or release
   it to the current source value. The original policy/map remain unchanged.
5. `bind` pairs the draft modes with exact saved bytes, advances one generation
   and returns companion JSON. `serializeUtf8` serializes an existing policy.

The component uses F# `option`; a Nu adapter must explicitly map Nu's `voption`.
Absent options mean imported-asset fallback, while the separate modes determine
source following. The adapter must preserve the other fourteen Nu material
fields, observe the actual saved state and retain complete adverse outcomes.

The helper does not parse a scene, recover its material map, prove that the map
matches those bytes, write either file, or commit a receipt. `bind` can therefore
hash a scene whose contents fail the intended change; the native observer must
detect that rather than promote successful binding to semantic success. There
is no transaction, crash recovery, historical base or out-of-band edit detector.
Copy/rename/export of a scene/companion pair and ordinary editor access remain
integration work.

## Exact control scope

[Controls.fs](Controls.fs) checks the 32-member five-stage sequence, equal-value
pins, release, independent fields, absent options, immutable drafts, malformed
or mismatched inputs and opaque JSON extensions. Its scene bytes are synthetic
stage labels. Companion modes and hashes round-trip through JSON; the material
maps are carried as supplied immutable values, not decoded from those labels.
This tests component semantics and pairing, **not** material serialization or
actual Nu save/reopen. The latter needs the separately accepted native package
described in the contract.

The construction history and exact accepted checks are recorded in
[RESULTS.md](RESULTS.md). Runtime duration and assertion counts are implementation
observations, not authoring productivity or independent research replications.
