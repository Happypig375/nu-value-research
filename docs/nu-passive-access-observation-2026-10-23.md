# R03 passive access: one native attempt, fixture not established

The single frozen Gaia attempt **did not establish the two-state fixture**.
The submitted Position.X drag left LeftWall at `(-164.000, 0.000, 0.000)` with
only `<Present>` in the Timeline. A later capture is byte-identical to the
immediate post-drag capture. No distinct F or new `Change Property Position`
entry was observed, so C0-C3 and Undo/Redo were not attempted. The post-run
manifest also found an undeclared new `gaia/imgui.ini`. The complete protocol
does not pass; no replacement process or post-hoc allowlist change was made.

This is a setup failure and a separate output-boundary failure. It is not a
demonstrated Undo/Redo defect, successful history-preserving access, repair
result or benefit estimate. The source of the ineffective drag remains
unresolved between the submitted interaction, transport and application.

## Preparation and assignment

The [accepted preparation](nu-passive-access-preparation-2026-10-23.md)
was completed in one registered operation with a 600-second limit and 8-GiB
free-space threshold. All 691 copied files / 1,441,875,801 bytes matched the
two previous manifests. The operation removed only the archived copies of
Breakout's log and imgui file, then installed the accepted 535-byte state.
The resulting 690 files / 1,441,869,206 bytes match the exact expected map:
689 shared entries unchanged, two removed, one added. The operation took
20.156 seconds; its outer process took 20.297 seconds. These nested times
are not additive.

Parent acceptance of the fresh manifest preceded the sole durable assignment.
An acceptance-receipt count typo, 688 rather than 689 unchanged shared entries,
was corrected in a retained erratum before launch; the full map comparisons,
manifest and assignment were unchanged. Four earlier construction failures
remain retained. The complete preparation gate passed before native execution;
this does not convert the later native outcome into a success.

The launcher verified the complete fresh package again and atomically consumed
`native-001`. A pre-launch OS query found no exact-path Gaia process. The later
OS record bound PID 30168 and its launcher parent, matching the final launcher
result. The process ran from 11:29:50.028 to 11:33:31.733 UTC on 23 October
2026: 221.704 seconds, exit code 0, without timeout or external termination.
Normal close included the application's exit-confirmation dialog.

## Actual observation coverage

Seven archived operations comprise window enumeration, initial observation,
LeftWall selection, one drag, one stability observation, close and confirmation.
Six screenshots were retained. The selected window was 1302 by 776 at reported
scale 1; its accessibility tree exposed only the window, so pixels supplied
the property/history observations. Provider action results explicitly label
synthetic input as unverified; the visible effects are judged separately.

| Stage | Observed evidence |
| --- | --- |
| Initial window | Scene hierarchy and Breakout presentation; `Advance (F5)` control and Timeline containing only `<Present>`. The sealed and rewritten state selects Gameplay with imperative execution false. |
| LeftWall selection | LeftWall highlighted; entity name LeftWall and visible ID 253; Position `-164.000`, `0.000`, `0.000`; Timeline remains `<Present>` only. |
| Single declared drag | One submitted window-local drag from (1018, 275) to (1058, 275), with no modifier or second edit. Position remains K; the property editor displays `[-164 0 0]`; no new history label appears. |
| Stability | Capture roughly 55 seconds after the immediate post-drag capture has the identical PNG hash and the same displayed state. |
| Termination | Window-close request opens the ordinary confirmation; confirmation is followed by normal process exit. No RightWall setup selection, distinct F, C0-C3 traversal or rescue run occurred. |

This supports partial ordinary selection and visible property access in one
launch. It does not independently observe the physical button trajectory,
underlying float bits, complete World state or callback value. Initial halt is
inferred from the source-bound `Advance (F5)` display, not an in-process query.
The clipped mode text is not promoted to a complete runtime mode observation.

## Runtime and output boundary

External module sampling recorded 171 module paths without a reported sampling
error. Observed Nu.Gaia, Nu, hostfxr, hostpolicy and coreclr file identities
match the bound package/runtime; 10.0.10 was the observed .NET host patch.
The Breakout managed DLL is absent from that external module record, so it
does not independently certify every loaded managed assembly. Conditional
reuse of the default-inert research bridge retains its previous limits.

stdout contains 325 bytes of SDL/OpenGL initialization messages; stderr is
empty. Both streams were retained without truncation. File changes are:

| Path | Frozen boundary | Actual result |
| --- | --- | --- |
| `breakout-mmcc/imgui.ini` | Allowed | Created, 4,855 bytes; matches the archived default bytes. |
| `breakout-mmcc/Log.txt` | Allowed | Created, 325 bytes; matches captured stdout. |
| `gaia/Nu.Gaia.State.txt` | Allowed | 535 to 536 bytes; exactly `ProjectFreshlyLoaded True` to `False`. |
| `gaia/imgui.ini` | **Not allowed** | New 4,855-byte file; retained as an unexpected change. |

All other pre-existing entries remain unchanged. No Gaia log was created.
The unexpected file's timestamp is near shutdown, but that is not a causal
source reconstruction. Its appearance is not retroactively added to the
normal-write list. The output violation prevents a fully conforming access
claim while the trustworthy partial visual observations remain retained.

## Disposition and next work

The assignment is consumed and this case is terminal. Do not reset the package
or rerun the gesture. Source-only investigation of input delivery/property
editing and the extra output may inform a distinct prospective question, with
new limits and acceptance; it cannot replace this result. R02/R10/R12 remain
returned. The [continuation prompt](continuation-prompt-2026-10-23.md) preserves
the next desk work and the unresolved practical R03/R06 comparison.

Count all setup, capture and verification work. Operation intervals overlap
the native lifetime; they are not summed as human effort. No participant,
experimental coding-agent run or measured active-human time is supplied by
this maintainer-operated feasibility observation.

## Retained evidence

Private root: `A:/nu-value-execution/20261023-material-intent/r03-passive-access/`.

| Artifact | SHA-256 |
| --- | --- |
| `configured-package/attempt-001-preregister.json` | `990719a4424cc08ba1fc2b9378d995376a721075ca1d93fa4299f8c50ac3103c` |
| `configured-package/attempt-001/result.json` | `b7dee724df999ea337d381d18252f77f945f2762fe27066b350a375940ef8c1f` |
| `configured-package/attempt-001/fresh-package-manifest.json` | `5a396b1223a24a6e5efd8dbce8ff4161e97f2f729c74508e537e5e28c637ea0c` |
| `launcher/runs/native-001/result.json` | `264da1df7fdca9069ac19fcd97db024bf42b21718c6842b35ee6e9cb13fc0152` |
| `observations/setup-004-drag-x/screenshot.png`, identical stability capture | `0169481d7a39d1d10b97a4a439e94c733a78ddb7bfdd8bfa6d33351b3f496200` |
| Unexpected `package/gaia/imgui.ini` | `f431666fed344cd1596ff44f72000372c35ceb67e1c8973ae641628cff04a5a8` |
| `reviews/native-001/review.md` | `638164d89d9692ac6e4ce52163354b70a0cacf8936f33785ebedff7a800ccad2` |
| `reviews/native-001/coverage.json` | `52c226c21fc676bddcd0648c2c3b2a481736e4de1453bbab79c11ce6fffaa203` |
| `reviews/native-001/parent-acceptance.json` | `113852faa8189ada253deaa418a9c54f4a0e82ad20ee1394d52fd3442dccac14` |

Raw commands, responses, screenshots, preflight, consumed assignment, complete
pre/post manifests and all earlier attempts remain private. Independent Sol
review and parent disposition are complete. They accept the retained setup
failure and separate output nonconformance, not a passing access result.
The parent receipt qualifies two statements in the preserved review table:
the clipped mode label is not a full runtime mode readout, and the submitted
drag command does not independently observe an uninterrupted physical gesture.
The original review and provisional assessment remain unchanged. These are
AI maintainer reviews, not human scientific approval.

## 2026-10-25 source clarification, without changing the attempt

The [pinned-source follow-up](nu-passive-access-source-followup-2026-10-25.md)
separates property focus from an accepted numeric edit and explains why the
lower Position editor can appear without a new value or snapshot. It leaves
the actual delivered gesture unresolved. The ordinary exit route changes cwd
to Gaia before ImGui cleanup; version-matched upstream source saves default
cwd-relative settings at context destruction under stated conditions. Exact
Twizzle native build correspondence and the actual writer remain unobserved.
Both terminal findings stand, with no retry or retrospective output amendment.
