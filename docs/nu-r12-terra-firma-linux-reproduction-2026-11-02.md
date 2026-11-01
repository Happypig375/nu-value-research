# R12 Terra Firma reopen pair: Linux reproduction check (2 November 2026)

**Status: protocol fixed before any build or run.** Results are added afterwards in their own section and do not change this protocol.

## Why

Eleven October packages now reproduce unchanged on this server ([STATUS](../STATUS.md)). R10's initializer-only schema reload cannot be reproduced unchanged: its sealer refuses any OS but Windows, and its comparator requires a Windows OS string. It is left as it is. The remaining executed native package that has no such lock is the R12 Terra Firma load/save/reopen pair ([record](nu-terra-firma-reopen-feasibility-2026-10-18.md)).

That pair loads Nu's existing 3D Terra Firma scene in a hidden real SDL/OpenGL world (L0), observes it, saves it, and reopens the saved bytes in a fresh process (L1). The checks:
- the declared 197-entity correspondence;
- 166 explicit links;
- 11 saved source histories;
- selected properties of 32 palms and 4 villas.

The question is: **does this pair reproduce on this server, unchanged?** This is the heaviest rendering load so far, on a software renderer.

Authority: user pre-approval of autonomous development (2 November). This is the completed reopen pair (15 to 18 October), not the later Terra Firma revision series and not the stopped R12 material-intent draft (untracked, untouched). No new arm, no candidate or model call, nothing Daybreak-only.

## What stays fixed

- Package `experiments/nu-r12-terra-firma/` exactly as committed (`run.py`, `Program.fs`, project, `compare.py`, `check_controls.py`). It is copied byte for byte to scratch.
- The private prerequisites, read only and hash-checked by `run.py`:
  - the Nu archive (`.artifacts/r03-feasibility-20261015/nu-064f7ae.tar`);
  - the existing **Windows-built** pipeline host (`.artifacts/r03-feasibility-20261015/source/Nu/Nu.Pipe/bin/Release/net10.0`, which also contains linux-x64 native libraries);
  - the accepted **Windows-built** R05 runtime host (`.artifacts/r05-events-20261015/bin/Release/net10.0`).
- The stage order: `assets`, `build`, `run` L0, `run` L1 with L0 as predecessor, `compare.py`, then `check_controls.py` on the original scene.

## What differs from Windows

- Linux, through `scripts/linux_nu_env.sh`: Xvfb and Mesa llvmpipe with the OpenGL 4.6 override.
- The NuGet cache is seeded from the preserved Windows cache (`.artifacts/nuget-packages/`), as in the other Linux checks. This avoids the FSharp.Core package difference found in the small-probe check.
- **Acceptance.** On Windows, a review of preparation diagnostics and source/PDB identity came between `build` and `run`. Here I check the build receipt's own readiness flag and its source/PDB identity fields, and record the receipt hash. There is no second reviewer.

## Steps and pass conditions

1. **Assets:** exit 0, accounting for all 248 outputs, including 120 transformed images. Output hashes are compared with the Windows `terra-assets-01`. Transformed images are made by the pipeline's encoders on a different OS, so a difference there is recorded, not failed. Copied files must be identical.
2. **Build:** exit 0, with `ready_for_parent_review` true. The compiled DLL hash will differ from Windows `ade20c65…`, because builds embed paths.
3. **L0, then L1:** each exits 0 without timeout, with the required observations A and B present.
4. **`compare.py`:** completed pair with 0 invalid and 0 adverse, preserving 197 original entities, 19 roots, 166 explicit links, 11 saved source histories, 32 palms and 4 villas, as on Windows.
5. **`check_controls.py`:** all 17 synthetic controls pass, as on Windows.
6. **Across platforms** (recorded): live-entity counts per observation (Windows: 233, with 36 generated protected entities), and the Linux comparison's counts and dispositions against Windows `terra-comparison-01.json`.

## What counts as a different result

Any of these is a **Linux difference**. It is recorded as found, not fixed and rerun:
- a stage failure, crash or timeout;
- an invalid or adverse comparison;
- a control failure;
- a correspondence count different from Windows.

The stop rule applies: five unresolved failures at one unchanged step means stop. Environment-only fixes are allowed and logged as attempts. No package byte changes.

## What this check cannot show

The original limits stay:
- no decoded visual appearance or framebuffer check;
- no input;
- no native resource restoration;
- no propagation or revision;
- no authoring benefit.

Software rendering makes timing meaningless.
