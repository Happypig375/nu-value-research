# Running OpenGL Nu/Gaia on the server's NVIDIA GPU without admin rights (3 November 2026)

> **Update, 3 November 2026 (user rule: "All Nu runs should be on Vulkan").**
> - **The default for Vulkan-era Nu will be NVIDIA Vulkan on Xvfb,** once nu-gaia-agentic confirms that route.
> - **This OpenGL/VirtualGL route is the fallback.** It is also the only GPU route for the research's pinned Nu `064f7ae`, which has **no Vulkan renderer** (see "Vulkan and the pinned revision" below).
> - Switching the pinned packages to Vulkan would mean re-pinning to a much newer Nu, which is a user decision (NEEDS-HUMAN item 10).

**Short answer:**
- **It works:** run the app on your own Xvfb display under **VirtualGL's EGL back end**. Its OpenGL then runs on the RTX 4090 D. Unchanged Gaia (pinned Nu `064f7ae`) runs about 7 times faster than with Mesa software rendering. Heavy 3D scenes run about 70 times faster, and faster than our earlier Windows runs.
- **Limit:** Nu's frames do **not** reach the Xvfb window (it stays black). So use this route for runs judged from the program's own data, and keep software rendering for screenshot-based checks.

Scope: Nu at `064f7ae` renders with **OpenGL 4.6**, not Vulkan. Current Nu master uses Vulkan; see "Vulkan" below.

## Recipe

1. **VirtualGL, user-level, once:** download the official release `virtualgl_3.1.5_amd64.deb` from GitHub (`gh release download 3.1.5 -R VirtualGL/virtualgl -p 'virtualgl_3.1.5_amd64.deb'`). Check SHA-256 `df3f7788ce41b182a47c0d298e5cd6d2d63579522cb41825970b7726e825485e`, which matches GitHub's published digest. Unpack without installing: `dpkg-deb -x virtualgl_3.1.5_amd64.deb ~/.local/share/virtualgl-3.1.5`. It is already unpacked there on this server.
2. **Run** with our own Xvfb (any free display you own, with an Xauthority cookie and `-nolisten tcp`). Mesa's software settings must be **off**:

   ```bash
   V=~/.local/share/virtualgl-3.1.5
   export DISPLAY=:94 XAUTHORITY=/path/to/your/xauth          # your own Xvfb
   unset LIBGL_ALWAYS_SOFTWARE GALLIUM_DRIVER MESA_GL_VERSION_OVERRIDE MESA_GLSL_VERSION_OVERRIDE
   export LD_LIBRARY_PATH="$V/usr/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
   VGL_DISPLAY=egl nice -n 10 "$V/opt/VirtualGL/bin/vglrun" dotnet YourApp.dll
   ```

   In this repo, `scripts/linux_nu_gpu_env.sh RUNS LOG -- COMMAND…` does all of this. It reuses `scripts/linux_nu_env.sh` for Xvfb and the SDK, and logs `nvidia-smi` samples during the run.
3. **Verify the device every time:**
   - Nu's log line must read `Initialized OpenGL 4.6.0 NVIDIA 580.178.04 (NVIDIA Corporation).` With software rendering it reads `… Mesa …`.
   - `nvidia-smi` during the run must show the `dotnet` process; Gaia uses about 1 GB of GPU memory.
   - A quick standalone check: `vglrun $V/opt/VirtualGL/bin/glxinfo -B` should print `OpenGL renderer string: NVIDIA GeForce RTX 4090 D/PCIe/SSE2`.

## Measured here (3 November)

| Run (pinned Nu, unchanged) | Software (Mesa llvmpipe) | GPU (VirtualGL EGL) |
| --- | --- | --- |
| Gaia + Breakout, branch A A1 (two fault/recovery passes) | 47 s | 6.4 s, the same verdict and behaviour ([re-check](nu-gpu-recheck-2026-11-03.md)) |
| Gaia + Breakout, 60-update control (A0) | 45 s | 7.2 s |
| R12 Terra Firma 3D scene, per process | about 750 s (Windows: 34–37 s) | L0 11.2 s, L1 8.8 s, about 1.1–1.2 GB GPU memory; the same comparison, byte-identical captures and saves |

These timings are not performance results: the GPU is shared, and VirtualGL copies frames back to X.

## Caveats

- **Black window:** under VirtualGL, Nu's Xvfb window stays black, so `xwd -id` captures show nothing. Software rendering shows the image, and VirtualGL's own `glxspheres64` displays fine. So rendering happens, but Nu's frames are not delivered to X. `VGL_READBACK=sync VGL_SPOIL=0` and `VGL_SYNC=1` did not help.
  - **Use the GPU route only when results come from the program itself:** probes, traces, saved files.
  - Keep `scripts/linux_nu_env.sh` (software) for checks that read screenshots, such as the 2 November keyboard and key-release checks.
- **What does not work: SDL3's `offscreen` driver with NVIDIA EGL** (`SDL_VIDEO_DRIVER=offscreen`, no X at all). It does give a real NVIDIA OpenGL 4.6 context; a plain SDL test prints the RTX 4090 D. But Nu at `064f7ae` then fails with "Could not make OpenGL context current when required". Nu's texture-loading thread makes its own shared context current on the **same window** as the renderer thread. GLX allows that; EGL forbids one surface being current on two threads. Using this route would mean changing engine code.
- **No usable NVIDIA X server:** `:0` is root's Xorg on the GPU and not ours to use. Xvfb cannot load NVIDIA's GLX. Hence VirtualGL.
- **Device evidence also in `Log.txt`:** the NVIDIA "Initialized OpenGL" line appears in both stdout and the app's `Log.txt`. The wrapper samples `nvidia-smi` every 2 s, which is coarse for short runs.
- **Shared GPU:** check `nvidia-smi` first, run one GPU process at a time, use `nice -n 10`, and keep runs bounded.
- **Vulkan (current Nu master, e.g. nu-gaia-agentic):** VirtualGL does not cover Vulkan. Pointing `VK_ICD_FILENAMES` at `/usr/share/vulkan/icd.d/nvidia_icd.json` selects the NVIDIA Vulkan driver. Whether it can present to a non-NVIDIA X server like Xvfb was **not tested here**: no Vulkan test tool is installed, and this repo's Nu is OpenGL. nu-gaia-agentic's launcher already has a `GAIA_VULKAN=nvidia` switch to try.
- **Line endings:** this checkout has `core.autocrlf=true`. The repository stores the scripts with LF, but a fresh checkout here would write CRLF, which breaks bash. Use the working copy, or `git show HEAD:scripts/linux_nu_gpu_env.sh`.

## Vulkan and the pinned revision (checked 3 November, source and GitHub API only; nothing run)

- **Every retained package that runs Nu pins `064f7ae`** (23 July 2026). That covers R02–R06, R10, R12, B0/B1, branches A/B and the input checks. R10 conversion uses Prime only, and R01's traces use Box2D.NET.
- **`064f7ae` is OpenGL-only:**
  - no file or line in the engine or Gaia source mentions Vulkan;
  - the renderer is OpenGL.Net, and SDL windows are created with the OpenGL flag (`Nu/Nu/Sdl/Sdl.fs:28`);
  - there is no switch to choose a renderer.
- **Current Nu master** (`47ef39e17`, 3 November) is **Vulkan-only**: it has `Nu/Nu/Vulkan/` and no OpenGL folder.
  - OpenGL was removed on a separate Vulkan branch (`aab38e2f9`, "Ripped out OpenGL dependency and code", 12 July 2026). That branch had diverged from our pin's line and was merged into master later.
  - Master is 1,938 commits ahead of `064f7ae`.
  - So the renderer is fixed by the Nu revision. Neither revision can switch at run time.
- **Comparability if the research moved to a Vulkan-era revision:**
  - **The main change would be the engine revision, not the renderer.** 1,938 commits change engine behaviour and APIs. That includes the screen-import fix (upstream `7d6389bea`), which would make stock import work. Every probe and the Gaia bridge anchors would need porting under new protocols. The results would be new observations, not reproductions of the October records.
  - **Mostly data-only observations** (model values, entity properties, event and callback traces, saved files, verdicts) would not depend on the renderer, but would still depend on the revision. This covers R03 B0/B1, R04, R10, R12, branch A and branch B.
  - **Rendering- or timing-dependent observations** would also change with the renderer and hardware:
    - the screenshot-judged keyboard and key-release checks;
    - R06's millisecond component timings;
    - wall-clock times;
    - anything tied to frame pacing, such as R02's callback counts.

