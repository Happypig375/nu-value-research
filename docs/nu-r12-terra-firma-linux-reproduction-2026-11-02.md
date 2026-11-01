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

## Results (added 2 November 2026, after the attempts)

**Conclusion: the Terra Firma pair cannot be reproduced unchanged on Linux. Its asset stage checks a Windows-only file attribute. The assets themselves are byte-identical to Windows.** I stopped before the build stage, because continuing would require changing the package.

**Attempts, all retained** (`.artifacts/r12-terra-linux-20261102/`):

1. **Assets attempt 01:** `run.py` refused the output location. It only writes inside `.artifacts/r12-propagation-20261018/` under its own repository root, and it reads three authority files from there.
2. **Assets attempt 02:** I copied those three authority files into the same relative path inside the scratch copy, so the preserved Windows folder was not written to. `run.py` checks their hashes (`fd945db4…`, `07458874…`, `29529d5f…`), and they were accepted. Results:
   - The **pipeline ran and exited 0** in 46 s.
   - The source and the Windows-built pipeline host were unchanged.
   - The **asset-closure check failed for all 248 assets, with one reason: `not_read_only`.** The runner tests the Windows `FILE_ATTRIBUTE_READONLY` flag (`st_file_attributes`), which Linux files never have.
   - The extra `AssetGraph.tracker` was also reported on Windows; it is not a difference.
   - `ready_for_parent_review` is false, so the build stage cannot follow unchanged.

**Asset content across platforms:** all **251 published files are byte-identical to Windows `terra-assets-01`**. That covers the 120 images transformed by the pipeline's encoders and the empty `AssetGraph.tracker`. Hash lists are in the evidence folder. The Windows-built Nu asset pipeline therefore produces the same bytes on Linux.

**Disposition:** like R10's initializer-only schema reload (whose build sealer refuses any OS but Windows), this package is Windows-bound as written. Running it here would need a declared amendment, such as treating file mode as the read-only signal. That is a package change, outside these unchanged-reproduction checks. I have not made it. The L0/L1 native pair was not run.
