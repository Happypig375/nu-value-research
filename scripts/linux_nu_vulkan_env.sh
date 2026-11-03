#!/usr/bin/env bash
# Run one command for Vulkan-era Nu (e.g. master 47ef39e) on the NVIDIA GPU with Vulkan, on our own Xvfb.
# The NVIDIA Vulkan driver presents to Xvfb (route confirmed by nu-gaia-agentic, 3 Nov 2026). Mesa software
# rendering is switched off. Logs the environment, nvidia-smi before the run and nvidia-smi process samples
# every 0.5 s during it. See docs/nu-vulkan-timing-reference-2026-11-03.md.
# Usage: linux_nu_vulkan_env.sh RUNS_ROOT LOG_NAME -- COMMAND [ARGS...]
#   NU_DISPLAY (default :94), NU_DOTNET_ROOT (default ~/.dotnet, SDK 10.0.403), NUGET_PACKAGES as usual.
set -euo pipefail
runs="$1"; log="$2"; shift 2
[ "${1:-}" = "--" ] && shift
[ $# -gt 0 ] || { echo "no command given" >&2; exit 2; }

export DOTNET_ROOT="${NU_DOTNET_ROOT:-$HOME/.dotnet}"
export PATH="$DOTNET_ROOT:$PATH" DOTNET_MULTILEVEL_LOOKUP=0 DOTNET_CLI_TELEMETRY_OPTOUT=1 DOTNET_NOLOGO=1
export VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/nvidia_icd.json VK_DRIVER_FILES=/usr/share/vulkan/icd.d/nvidia_icd.json
export SDL_VIDEO_DRIVER=x11
unset LIBGL_ALWAYS_SOFTWARE GALLIUM_DRIVER LP_NUM_THREADS MESA_GL_VERSION_OVERRIDE MESA_GLSL_VERSION_OVERRIDE LD_PRELOAD

display="${NU_DISPLAY:-:94}"; n="${display#:}"
mkdir -p "$runs"
xdir="$runs/.x11"; mkdir -p -m 700 "$xdir"
export DISPLAY="$display" XAUTHORITY="$xdir/xauth"
existing="$(pgrep -u "$(id -u)" -a -f "^Xvfb $display " | head -1 || true)"
if [ -n "$existing" ]; then
  auth="$(sed -n 's/.* -auth \([^ ]*\).*/\1/p' <<<"$existing")"
  [ -n "$auth" ] && [ -r "$auth" ] || { echo "cannot find auth file of running Xvfb $display" >&2; exit 3; }
  export XAUTHORITY="$auth"
else
  [ -S "/tmp/.X11-unix/X$n" ] && { echo "display $display is in use by someone else" >&2; exit 3; }
  rm -f "$XAUTHORITY"; ( umask 077; xauth -q -f "$XAUTHORITY" add "$display" . "$(mcookie)" )
  nohup Xvfb "$display" -screen 0 1920x1080x24 -nolisten tcp -auth "$XAUTHORITY" </dev/null >"$xdir/xvfb.log" 2>&1 &
  for _ in $(seq 50); do [ -S "/tmp/.X11-unix/X$n" ] && break; sleep 0.1; done
fi

{ echo "command: $*"; echo "display=$DISPLAY started=$(date -Is)"
  env | grep -E '^(DOTNET_ROOT|NUGET_PACKAGES|XAUTHORITY|VK_|SDL_|LD_LIBRARY_PATH)=' | sort
  dotnet --version
  echo "loadavg: $(cat /proc/loadavg)"; grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
  nvidia-smi --query-gpu=name,driver_version,utilization.gpu,memory.used,memory.total --format=csv
  nvidia-smi | sed -n '/Processes:/,$p' | grep -E '^\|  +[0-9]' || true; } > "$runs/$log.env.txt"
( while :; do echo "--- $(date +%s.%N)"; nvidia-smi | sed -n '/Processes:/,$p' | grep -E '^\|  +[0-9]' || true; sleep 0.5; done ) \
  > "$runs/$log.gpu-samples.txt" 2>&1 &
sampler=$!
trap 'kill $sampler 2>/dev/null || true' EXIT
nice -n 10 "$@"
