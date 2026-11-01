#!/usr/bin/env bash
# Run one screen-persistence arm on Linux under a private Xvfb display with software OpenGL.
# Environment-only wrapper around run.py (see docs/nu-daybreak-screen-persistence-2026-11-02.md).
# Usage: linux_run.sh PREPARED_SOURCE MODE ATTEMPT_NN RUNS_ROOT
set -euo pipefail
prepared="$1"; mode="$2"; attempt="$3"; runs="$4"
repo="$(cd "$(dirname "$0")/../.." && pwd)"
out="$runs/run-$mode-$attempt"
[ -e "$out" ] && { echo "output exists: $out" >&2; exit 2; }
transfer="$runs/transfer"

export DOTNET_ROOT="$HOME/.local/share/dotnet-sdk-10.0.302"
export PATH="$DOTNET_ROOT:$PATH" DOTNET_MULTILEVEL_LOOKUP=0 DOTNET_CLI_TELEMETRY_OPTOUT=1 DOTNET_NOLOGO=1
export LIBGL_ALWAYS_SOFTWARE=1 GALLIUM_DRIVER=llvmpipe LP_NUM_THREADS="${LP_NUM_THREADS:-4}"
export MESA_GL_VERSION_OVERRIDE=4.6 MESA_GLSL_VERSION_OVERRIDE=460
export SDL_VIDEO_DRIVER=x11

display="${DAYBREAK_DISPLAY:-:94}"; n="${display#:}"
xdir="$runs/.x11"; mkdir -p -m 700 "$xdir"
export DISPLAY="$display" XAUTHORITY="$xdir/xauth"
if ! pgrep -u "$(id -u)" -f "^Xvfb $display " >/dev/null; then
  [ -S "/tmp/.X11-unix/X$n" ] && { echo "display $display is in use by someone else" >&2; exit 3; }
  rm -f "$XAUTHORITY"; ( umask 077; xauth -q -f "$XAUTHORITY" add "$display" . "$(mcookie)" )
  nohup Xvfb "$display" -screen 0 1920x1080x24 -nolisten tcp -auth "$XAUTHORITY" </dev/null >"$xdir/xvfb.log" 2>&1 &
  for _ in $(seq 50); do [ -S "/tmp/.X11-unix/X$n" ] && break; sleep 0.1; done
fi

mkdir -p "$runs"
{ echo "mode=$mode attempt=$attempt display=$DISPLAY"; env | grep -E '^(DOTNET_ROOT|LIBGL|GALLIUM|LP_NUM|SDL_|MESA_)=' | sort; dotnet --version; } > "$runs/run-$mode-$attempt.env.txt"
cd "$repo"
probe="$runs/build/probe/bin/Release/net10.0/Probe.dll"
nice -n 10 python3 -I experiments/nu-daybreak-screen-persistence/run.py "$mode" \
  "$prepared/Projects/Breakout Mmcc/bin/Release/net10.0/Breakout Mmcc.dll" \
  experiments/nu-history-b1/checkpoint "$transfer" "$out" --timeout 600 --probe "$probe"
