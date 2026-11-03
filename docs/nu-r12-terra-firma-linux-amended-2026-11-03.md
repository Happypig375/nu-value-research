# R12 Terra Firma reopen pair on Linux, under a declared amendment (3 November 2026)

**Status: protocol fixed before any build or run.** Results are added afterwards in their own section and do not change this protocol.

## Why

On 2 November the unchanged Terra Firma package stopped at its asset stage on Linux ([record](nu-r12-terra-firma-linux-reproduction-2026-11-02.md)). Its asset check tests a Windows-only read-only file flag, which Linux files never have, so all 248 assets failed that one check. The asset bytes themselves were identical to Windows.

On 3 November the user decided (decision D9, item 8a in NEEDS-HUMAN) that this package should be reproduced on Linux through a declared, dated amendment, for example by treating file mode as the read-only signal, so that all results are consistently Linux.

The package ([record](nu-terra-firma-reopen-feasibility-2026-10-18.md), `experiments/nu-r12-terra-firma/`) loads Nu's existing 3D Terra Firma scene in a hidden real SDL/OpenGL world (L0), observes it, saves it, and reopens the saved bytes in a fresh process (L1). On Windows the pair passed the declared checks:
- the 197-entity correspondence;
- 166 explicit links;
- 11 saved source histories;
- selected properties of 32 palms and 4 villas;
- 0 invalid and 0 adverse findings;
- all 17 synthetic checker controls.

The question is: **does this pair pass on Linux, with only the declared amendment?**

Authority: user decision D9 (3 November 2026). This is the completed reopen pair, not the later Terra Firma revision series and not the stopped R12 material-intent draft (untracked, unopened). No new arm, no candidate or model call, nothing Daybreak-only.

## The amendment (the only change to the package)

`experiments/nu-r12-terra-firma-linux/linux_amendment.py` copies the committed package into a new scratch folder, checks every original file hash, and changes exactly these lines of `run.py` in the copy. The committed package is not touched.

| Line(s) | Windows original | Linux amendment | Why |
| --- | --- | --- | --- |
| 216 | an asset fails unless the Windows `FILE_ATTRIBUTE_READONLY` flag is set | an asset fails if its file mode has **any** write bit (owner, group or other) | On Linux, .NET's read-only attribute is the absence of write bits. This is the same check the Windows run made, expressed in the Linux signal. |
| 338 and 344 | records `st_file_attributes` of the L1 scene before and after replacing it | records it with `getattr(…, None)` | That attribute does not exist on Linux, so the L1 stage would crash before launching. The value is only recorded, never checked. |

## Two more Windows-bound steps, replaced without changing the package

- **Build acceptance.** `run.py run` requires `source-binary-seal.json` and `native-acceptance.json` in the build folder. On Windows these came from the parent's review scripts in `.artifacts/r12-propagation-20261018/`.
  - The seal is made with the same two scripts, run on copies: `inspect-terra-build.fsx` reads the PE/PDB metadata without loading the assembly, then `seal-terra-build.py` checks that all 8 original source units and the observer `Program.fs` match their recorded hashes.
  - The Windows acceptance script hard-codes the Windows DLL and PDB hashes, which differ on Linux because builds embed paths. It is replaced by `experiments/nu-r12-terra-firma-linux/accept_linux_build.py`. That script checks the same facts (ready flags, exit 0, PE/PDB seal 8+1, seal matches binary, Server GC and TieredPGO in the runtime config, package inputs unchanged, observer and protocol hashes) and writes the acceptance with my name on it. There is **no second reviewer**.
- **Output location.** `run.py` writes only inside `.artifacts/r12-propagation-20261018/` under its own repository root. As on 2 November, the scratch tree gets copies of the three authority files that `run.py` reads from there (hash-checked by `run.py`), so the preserved Windows folder is never written.

## What stays fixed

- Every other package byte: `Program.fs` (observer), the project file, `compare.py`, `check_controls.py`, `PROTOCOL.md`, `global.json`.
- The private prerequisites, read only and hash-checked by `run.py`:
  - the Nu archive `.artifacts/r03-feasibility-20261015/nu-064f7ae.tar`;
  - the existing Windows-built pipeline host (`.artifacts/r03-feasibility-20261015/source/Nu/Nu.Pipe/bin/Release/net10.0`);
  - the accepted Windows-built R05 runtime host (`.artifacts/r05-events-20261015/bin/Release/net10.0`).
- The stage order: `assets`, `build`, seal and acceptance, `run` L0, `run` L1 with L0 as predecessor, `compare.py`, then `check_controls.py` on the original scene.
- The 180-second deadline for each native run.

## What differs from Windows (environment only)

- `scripts/linux_nu_env.sh`: Xvfb on display `:96` with a private cookie and no TCP, Mesa llvmpipe with the OpenGL 4.6 override.
- A scratch NuGet cache seeded from `.artifacts/nuget-packages/`.
- **Assimp.** Terra Firma loads 3D models through Assimp. The R05 host was built on Windows and holds only `assimp.dll`; Nu at this revision looks for `libassimp.so` on Linux. The pinned archive itself ships `Nu/Nu/libassimp.so`. I put that one file, extracted from the hash-checked archive into a separate scratch folder, on `LD_LIBRARY_PATH` for the native runs, and record its hash. It is not copied into the application folder, so the protected application files stay as they are.
- Software rendering, so timing means nothing.

## Steps and pass conditions

1. **Assets:** exit 0 and `ready_for_parent_review` true, with all 248 expected outputs accounted for, including 120 transformed images. The published files must again be byte-identical to Windows `terra-assets-01` (they were on 2 November). If Nu.Pipe leaves write bits on Linux, the amended check fails; that is a Linux difference, not a reason to loosen the check.
2. **Build:** exit 0 with `ready_for_parent_review` true. Warning counts are recorded (Windows: 72 warnings, 0 errors).
3. **Seal and acceptance:** the seal finds 8 original units and 1 observer with matching PE/PDB identity, and `accept_linux_build.py` accepts.
4. **L0, then L1:** each exits 0 within 180 s with `complete_observation_and_save` true.
5. **`compare.py`:** disposition `passed_declared_checks` with scope `pair`, 0 invalid and 0 adverse, as on Windows.
6. **`check_controls.py`:** all 17 synthetic controls pass, as on Windows.
7. **Also recorded** (not pass/fail):
   - the L0 and L1 saved-scene hashes against Windows (both `0bdb814d…`);
   - the live-entity counts per observation (Windows: 233, with 36 generated protected entities);
   - the Linux findings and descriptive output against Windows `terra-comparison-01.json`.

   Nu's entity `Order` numbers come from a clock that runs differently on Linux, so byte differences in saved scenes are expected and are not failures by themselves.

## What counts as a different result

Any of these is a **Linux difference**. It is recorded as found, not fixed and rerun:
- a stage failure, crash or timeout;
- an invalid or adverse comparison;
- a control failure;
- a correspondence count different from Windows.

The stop rule applies: five unresolved failures at one unchanged step means stop that step. Environment-only fixes (display, library path, exact SDK) are allowed, and each is logged as its own attempt. A change to any package byte beyond the declared amendment would need a new written amendment first.

## What this check cannot show

The original limits stay: no decoded visual appearance or framebuffer check; no input; no native resource restoration; no propagation or revision; no authoring benefit. The asset check covers presence, container signatures, exact untransformed bytes and the read-only signal, not how textures look.
