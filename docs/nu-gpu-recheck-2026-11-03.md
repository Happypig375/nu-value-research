# GPU re-check of branch A (A1) and R12 Terra Firma (3 November 2026)

**Status: protocol fixed before either re-check ran.** Results are added afterwards in their own section.

## Why

The user said Gaia may use the server's GPU ("You can use the GPU resources to run Gaia properly", relayed by the orchestrator on 3 November). Until now every Linux run used Mesa's software OpenGL (llvmpipe) on Xvfb. The [GPU recipe](nu-gpu-headless-recipe-2026-11-03.md) found a way, without admin rights, to run unchanged pinned Nu with OpenGL on the NVIDIA RTX 4090 D: VirtualGL's EGL back end, on our own Xvfb.

This re-check asks one question. **Do two results already obtained with software rendering come out the same when rendering runs on the GPU?** It also records timings. It is an environment change only.

## What is re-run, once each

1. **Branch A, arm A1** ([record](nu-daybreak-recovery-trigger-2026-11-03.md), section 6). Same package (`experiments/nu-daybreak-recovery-trigger/`). The fault tree is prepared again from the same archive, with the same source hashes as on 3 November: `Gaia.fs` bridged `adcd0587…`, `Gameplay.fs` with the fault `cded97cd…`.
2. **R12 Terra Firma reopen pair** ([record](nu-r12-terra-firma-linux-amended-2026-11-03.md)), with all amendment-3 settings unchanged, including the 1,800 s per-process deadline. The steps are those the package requires: assets, build, seal and acceptance as before, then L0, L1 (with L0 as predecessor), `compare.py` and `check_controls.py`.

## What changes, and nothing else

- **Wrapper:** `scripts/linux_nu_gpu_env.sh` replaces `scripts/linux_nu_env.sh`. It uses the same SDK and our own Xvfb display, with Mesa software rendering switched off. The app runs under VirtualGL 3.1.5 (`vglrun`, `VGL_DISPLAY=egl`): its GLX/OpenGL calls run on the NVIDIA GPU through NVIDIA's EGL. VirtualGL comes from the official GitHub release, SHA-256 `df3f7788…485e`, matching GitHub's digest, unpacked into `~/.local/share/virtualgl-3.1.5`.
- **Device evidence:** Nu's own startup line must read "Initialized OpenGL 4.6.0 NVIDIA …". The wrapper's `nvidia-smi` samples must show the app process on the GPU.
- **Shared GPU:** check `nvidia-smi` before each run. Runs are `nice -n 10`, one process at a time.

## Pass conditions (the results must match the software-rendering runs)

**Branch A A1 must give the same verdicts and the same recorded behaviour:**
- `check.py` A1 verdict **PASS**, with all 17 checks true;
- the last hook before each fault at gameplay clock 29;
- no "and halted" log variant;
- the live state not the same object as K, in both passes;
- exit code 0.

The settled model values themselves (ball direction, brick colours) are random per process, as before, so they are compared with this run's own S0, not with the earlier run's.

**R12 must give the same results:**
- pair verdict `passed_declared_checks` with 0 invalid and 0 adverse findings;
- a comparison equal to Windows `terra-comparison-01.json` and to the amendment-3 Linux result;
- L0/L1 captures and saved scene byte-identical to Windows (`10ab23a3…`, `0bdb814d…`), with 233 entities;
- 17/17 checker controls.

**Recorded:** wall-clock time per process, against the software-rendering runs (A1 47 s; R12 L0 749 s, L1 747 s) and Windows (R12 34–37 s), plus GPU memory used.

**What counts as a difference:** any verdict, check, count or byte that differs is a **GPU difference**. It is recorded, not fixed and rerun. Environment-only fixes (library path, display) are allowed and logged as separate attempts. The five-failure rule applies per step.

## What this cannot show

- Rendered images: no framebuffer or screenshot comparison is made, so this does not show that GPU and software images are equal.
- Real-hardware display or input.
- Timing as a performance result: the GPU is shared, and VirtualGL copies frames back to Xvfb.

*Correction, 3 November (after the runs): three lines of stray shell text (a heredoc terminator and a `git commit` command) were accidentally committed here at `6dde89a`. They have been removed. They were never part of the protocol, and no protocol content changed.*

## Results (added after the runs)

### R12 results (GPU)

Added 3 November 2026, ~19:25 HKT, after the runs. Done by the Claude Opus fork that ran the amendment-3 software runs.

**Conclusion: on the GPU, the R12 Terra Firma pair gives exactly the same results as the software-rendering run (amendment 3) and as Windows. It is now fast: each native process takes about 9–11 s, against about 12.5 minutes with software rendering and 34–37 s on Windows.** No GPU difference was found.

**Setup.**
- `nvidia-smi` before the native runs: no compute process, 16 MiB in use.
- Assets, build, seal and acceptance used the **software wrapper** (`scripts/linux_nu_env.sh`), as in amendment 3, because they don't render.
- L0 and L1 used the **GPU wrapper** (`scripts/linux_nu_gpu_env.sh`) on display `:96`. `libassimp.so` and `libbulletc.so` from the pinned archive went through `NU_LD_LIBRARY_PATH`. `LP_NUM_THREADS=32` stayed exported as in amendment 3; it has no effect on the GPU.
- The amendment-3 package copy was made again with the same script (`run.py` `cf8ffd38…`, deadline 1,800 s).

| Step | Result | Compared with |
| --- | --- | --- |
| Assets | Ready, 0 closure failures; all 251 published files byte-identical to Windows. | Same as amendment 3 |
| Build, seal, acceptance | Ready, 72 warnings, 0 errors; 8+1 PE/PDB seal; accepted, no failed check. | Same as amendment 3 |
| **L0** | Exit 0, complete, **11.2 s**. Nu logged "Initialized OpenGL 4.6.0 NVIDIA 580.178.04 (NVIDIA Corporation)". `nvidia-smi` samples show the run's own `dotnet` PID 302669 on the GPU; peak **1,071 MiB**. New files: the same four as Windows. | Software 749 s; Windows 34 s |
| **L1** (predecessor L0) | Exit 0, complete, **8.8 s**. Same NVIDIA line; PID 303540 on the GPU; peak **1,190 MiB**. | Software 747 s; Windows 37 s |
| `compare.py` | `passed_declared_checks`, pair, **0 invalid, 0 adverse**, no findings, inputs unchanged. Disposition, scope, counts, `L1_assigned_observed`, findings and descriptive records are **equal to both Windows `terra-comparison-01.json` and the amendment-3 Linux comparison**. | Same |
| Captures and saves | L0 and L1 `A.nugroup`/`B.nugroup` `10ab23a3…`, `saved-Scene.nugroup` `0bdb814d…`: byte-identical to Windows. A and B: 233 entities, 36 generated. | Same |
| `check_controls.py` | 17 of 17 pass. | Same |

**Attempts:** one of each step, all passed, nothing repeated.

**Timing and memory caveats:** the peaks are 2-second samples on a shared GPU. The timings are not a performance result (shared GPU; VirtualGL copies frames back to Xvfb). But the size of the change confirms the attempt-03 diagnosis: on the software renderer, nearly all the time was one shutdown frame.

Evidence is in `.artifacts/gpu-recheck-20261103/r12/`:
- the runner scripts;
- the assets/build/seal/acceptance records;
- both native runs' receipts, observations, logs, `*.gpu-env.txt` and `*.gpu-samples.txt`;
- the comparison and the controls receipt.

I deleted the scratch and logged it in `DELETIONS.log`, and stopped Xvfb `:96`.

### Branch A A1 results (GPU)

- **Result: the same verdict and the same recorded behaviour as the software run.**
  - `check.py` A1 verdict **PASS**, with all 17 checks true.
  - The last hook before each fault was at gameplay clock 29. 30 TimeUpdates had completed when the first recovery came (60 by the second).
  - No "and halted" variant appeared. The live state was not the same object as K, in both passes.
  - Exit code 0.
- **Device:** Nu logged "Initialized OpenGL 4.6.0 NVIDIA 580.178.04 (NVIDIA Corporation)". `nvidia-smi` showed the run's `dotnet` process (PID 295276) on the GPU with about 1,059 MiB.
- **Time:** 6.4 s, against 47 s with software rendering.
- **Attempts:** one, which passed. The GPU was idle beforehand (0 %, 16 MiB).
- **Environment checks before the re-check** (not attempts):
  - an SDL-offscreen start, which failed in Nu's renderer thread for the EGL reason in the [recipe](nu-gpu-headless-recipe-2026-11-03.md);
  - two A0 starts under VirtualGL, which passed in 8.4 s and 7.2 s;
  - screenshot tests that found the black-window limit.

  All are in `.artifacts/gpu-recheck-20261103/runs/` (`smoke-*`, `shot-*`, `standalone-*`).
- **Evidence:** `.artifacts/gpu-recheck-20261103/runs/a1-gpu-01/` and `a1-gpu-verdict.json`. The trees were prepared again from the same archive with the same source hashes (`prepare-*.json`, `build-*.log`).

### Conclusion of the re-check

Both re-checked results are unchanged on the GPU:
- branch A A1: same verdict and behaviour;
- R12 Terra Firma: the same comparison, byte-identical captures and saves, and 17/17 controls.

Run times drop from about 47 s to 6.4 s (A1), and from about 750 s to about 10 s per process (R12). No rendered images were compared.

