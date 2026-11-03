#!/usr/bin/env bash
# Run one command for pinned Nu (064f7ae) with OpenGL rendered on the NVIDIA GPU, without admin rights.
# How: our own Xvfb display (via scripts/linux_nu_env.sh) for windows and input, plus VirtualGL's EGL
# back end (user-level copy, VGL_DISPLAY=egl), which runs the app's GLX/OpenGL calls on the GPU through
# NVIDIA's EGL. Mesa software rendering is switched off. Logs the environment, an nvidia-smi snapshot,
# and nvidia-smi process samples every 2 s during the run (proof of the device; footprint on a shared GPU).
# See docs/nu-gpu-headless-recipe-2026-11-03.md.
# Usage: linux_nu_gpu_env.sh RUNS_ROOT LOG_NAME -- COMMAND [ARGS...]
#   NU_DISPLAY (default :94), VGL_ROOT (default ~/.local/share/virtualgl-3.1.5), NUGET_PACKAGES as usual.
set -euo pipefail
runs="$1"; log="$2"; shift 2
[ "${1:-}" = "--" ] && shift
[ $# -gt 0 ] || { echo "no command given" >&2; exit 2; }
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
vgl="${VGL_ROOT:-$HOME/.local/share/virtualgl-3.1.5}"
[ -x "$vgl/opt/VirtualGL/bin/vglrun" ] || { echo "VirtualGL not found at $vgl" >&2; exit 3; }
mkdir -p "$runs"

{ echo "gpu wrapper: VirtualGL $vgl, VGL_DISPLAY=egl"
  nvidia-smi --query-gpu=name,driver_version,utilization.gpu,memory.used,memory.total --format=csv; } > "$runs/$log.gpu-env.txt"
( while :; do echo "--- $(date -Is)"; nvidia-smi | sed -n '/Processes:/,$p' | grep -E '^\|  +[0-9]' || true; sleep 2; done ) \
  > "$runs/$log.gpu-samples.txt" 2>&1 &
sampler=$!
trap 'kill $sampler 2>/dev/null || true' EXIT

export NU_LD_LIBRARY_PATH="$vgl/usr/lib${NU_LD_LIBRARY_PATH:+:$NU_LD_LIBRARY_PATH}"
NU_DISPLAY="${NU_DISPLAY:-:94}" bash "$here/linux_nu_env.sh" "$runs" "$log" -- \
  env -u LIBGL_ALWAYS_SOFTWARE -u GALLIUM_DRIVER -u MESA_GL_VERSION_OVERRIDE -u MESA_GLSL_VERSION_OVERRIDE \
      VGL_DISPLAY=egl \
      "$vgl/opt/VirtualGL/bin/vglrun" "$@"
