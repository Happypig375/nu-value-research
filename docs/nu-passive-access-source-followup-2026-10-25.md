# R03 native-001: property focus and ini-output source follow-up

Integrated 2026-10-25. The [native observation](nu-passive-access-observation-2026-10-23.md)
remains terminal: its sole drag left Position K unchanged, produced no history
entry, and never reached C0-C3 or Undo/Redo. The new Gaia-root ini file remains
outside the frozen output boundary. This note supplies source explanations
with causal limits; it changes neither outcome and authorizes no retry.

## Property focus is separate from an accepted edit

At Nu pin `064f7ae92a8506689cd91aff5e6804a375d6ef3d`, a Vector3 property uses
`ImGui.DragFloat3` with the editor's `SnapDrag` value. The helper calls
`FocusProperty` when the item is focused even if the widget reports no edit.
Gaia's lower Edit Property window then displays the focused descriptor.
Consequently, its appearance after the submitted action is compatible with
focus without an accepted numeric change.
[Property helper](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/World/WorldImGui.fs#L579-L598),
[property edit route](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L2034-L2064)
and [focused editor](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L3086-L3153).

The ordinary setter runs on reported editing or promotion and snapshots before
the first accepted change. Subsequent frames sharing one `MouseLeftId` can
deduplicate that snapshot; focus alone does not create one. The inspected
route therefore does not support the claim that deduplication erased a first
successful edit. [Setter/snapshot source](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L505-L544).

The receipt's coordinates and speed parameter make a change plausible if an
active held drag reached the widget. They do not prove the delivered
button-down/motion/up trajectory, docking geometry, or acceptance conditions.
The provider marked synthetic input unverified. The ineffective action's
physical cause remains unresolved; no engine defect is localized.

## A cwd-dependent ini save is source-consistent

Gaia creates the initial layout under the loaded project's target directory.
The ordinary exit-confirmation path then writes editor state by an absolute
Gaia path, changes process cwd back to Gaia and exits. Normal cleanup destroys
the ImGui context. The executed research bridge changes a later callback, not
these inspected property/cwd/cleanup paths; the prior PDB/source comparison
and seven-source audit retain that narrower correspondence.
[Exit-confirmation source](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu.Gaia/Gaia.fs#L4076-L4090),
[ImGui cleanup](https://github.com/bryanedds/Nu/blob/064f7ae92a8506689cd91aff5e6804a375d6ef3d/Nu/Nu/ImGui/ImGui.fs#L119-L122).

Nu's dependency is `Twizzle.ImGui-Bundle.NET` 1.91.5.2. The matching upstream
Dear ImGui `v1.91.5-docking` tag resolves through its annotated tag object to
commit `368123ab06b2b573d585e52f84cd782c5c006697`. At that source edition:

- `ImGuiIO` defaults to cwd-relative `imgui.ini`.
- `NewFrame` invokes the settings update; its initial load attempt marks
  settings loaded even when a file is absent.
- `DestroyContext` calls `Shutdown`. Once initialized, shutdown saves settings
  if they have been loaded and the filename is non-null.
- Saving opens the supplied path in text-write mode. A delayed dirty save is
  also possible before teardown, using the cwd then in force.

These facts are bound by the upstream [default filename](https://github.com/ocornut/imgui/blob/368123ab06b2b573d585e52f84cd782c5c006697/imgui.cpp#L1425-L1431),
[context destruction](https://github.com/ocornut/imgui/blob/368123ab06b2b573d585e52f84cd782c5c006697/imgui.cpp#L3866-L3875),
[shutdown conditions](https://github.com/ocornut/imgui/blob/368123ab06b2b573d585e52f84cd782c5c006697/imgui.cpp#L4177-L4200),
[settings update](https://github.com/ocornut/imgui/blob/368123ab06b2b573d585e52f84cd782c5c006697/imgui.cpp#L15070-L15094)
and [save implementation](https://github.com/ocornut/imgui/blob/368123ab06b2b573d585e52f84cd782c5c006697/imgui.cpp#L15230-L15244).

This is a version-matched upstream mechanism consistent with a Gaia-root write
at cleanup. The nuspec identifies a wrapper repository commit but does not
bind the executed native DLL to these exact C++ bodies, patches or build flags.
The runtime filename and file-function configuration were not observed, and
there is no file-write trace identifying the actual writer. File timestamps
and similar contents support the hypothesis but do not close these gaps.
Normal exit and an explanatory mechanism do not make an undeclared output
conformant retroactively.

## Consequence and evidence coverage

A distinct future access protocol must observe an accepted state change rather
than infer it from focus or submitted coordinates. Its output boundary must
prospectively account for cwd-dependent persistence or explicitly bind the
settings path. These are design implications, not a new assignment, reset or
replacement for native-001.

Private `value-preparation/r03-ui-source-followup/` retains the Nu audit and
seven-source coverage. `imgui-upstream-followup/` retains exact tag metadata,
header/implementation and nuspec. `imgui-source-audit-20261025/` records the
selected ranges, eight bound inputs and once-only source-decision receipts.
No whole-file C++/header reading or native execution is claimed. Parent checked
the decisive Vector3, filename, settings-load, destruction and save ranges.

The audit `imgui_source_audit_20261025` includes five directly considered
source units with no exclusions/skips or report warnings. The tag responses
are one identity chain, and the header/implementation one upstream edition;
this is not five independent works. Wider historical web-screen coverage was
not preserved in the acquisition manifest and is not reconstructed as complete.
Evidence SHA-256: `a6785688bc4e8c3a169f109f72fc927c7503d4c38ebcfc496f362c031f498334`.
