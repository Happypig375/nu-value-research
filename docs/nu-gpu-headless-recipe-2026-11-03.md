# Running OpenGL Nu/Gaia on the server's NVIDIA GPU without admin rights (3 November 2026)

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
