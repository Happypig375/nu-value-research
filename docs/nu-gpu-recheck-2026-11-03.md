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
EOF
cd /home/happypig375/workspace/nu-value-research && printf '%s\n' /scripts/linux_nu_gpu_env.sh | git sparse-checkout add --stdin && bash scripts/linux_smoke.sh > /dev/null 2>&1; echo smoke=$?; git add --sparse scripts/linux_nu_gpu_env.sh docs/nu-gpu-recheck-2026-11-03.md && git commit -q -m "GPU re-check protocol (branch A A1, R12) and GPU wrapper: unchanged Nu on the RTX 4090 D via VirtualGL EGL, before any re-check run

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" -- scripts/linux_nu_gpu_env.sh docs/nu-gpu-recheck-2026-11-03.md 2>&1 | grep -v "CRLF\|original line"; git log --oneline -1