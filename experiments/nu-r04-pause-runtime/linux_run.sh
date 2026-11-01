#!/usr/bin/env bash
# Run one prepared R04 arm on Linux under a private Xvfb display with software OpenGL.
# Environment-only wrapper around the unchanged run.py (see docs/nu-r04-linux-reproduction-2026-11-02.md).
# Usage: linux_run.sh PREPARED_ROOT ARM ATTEMPT_NN RUNS_ROOT
set -euo pipefail
prepared="$1"; arm="$2"; attempt="$3"; runs="$4"
repo="$(cd "$(dirname "$0")/../.." && pwd)"
out="$runs/run-$arm-$attempt"
[ -e "$out" ] && { echo "output exists: $out" >&2; exit 2; }

export DOTNET_ROOT="$HOME/.local/share/dotnet-sdk-10.0.302"
export PATH="$DOTNET_ROOT:$PATH" DOTNET_MULTILEVEL_LOOKUP=0 DOTNET_CLI_TELEMETRY_OPTOUT=1 DOTNET_NOLOGO=1
export LIBGL_ALWAYS_SOFTWARE=1 GALLIUM_DRIVER=llvmpipe LP_NUM_THREADS="${LP_NUM_THREADS:-4}"
export SDL_VIDEO_DRIVER=x11
[ -n "${R04_LD_LIBRARY_PATH:-}" ] && export LD_LIBRARY_PATH="$R04_LD_LIBRARY_PATH${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"

display="${R04_DISPLAY:-:93}"; n="${display#:}"
xdir="$runs/.x11"; mkdir -p -m 700 "$xdir"
export DISPLAY="$display" XAUTHORITY="$xdir/xauth"
if ! pgrep -u "$(id -u)" -f "^Xvfb $display " >/dev/null; then
  [ -S "/tmp/.X11-unix/X$n" ] && { echo "display $display is in use by someone else" >&2; exit 3; }
  rm -f "$XAUTHORITY"; ( umask 077; xauth -q -f "$XAUTHORITY" add "$display" . "$(mcookie)" )
  nohup Xvfb "$display" -screen 0 1920x1080x24 -nolisten tcp -auth "$XAUTHORITY" </dev/null >"$xdir/xvfb.log" 2>&1 &
  for _ in $(seq 50); do [ -S "/tmp/.X11-unix/X$n" ] && break; sleep 0.1; done
fi

mkdir -p "$runs"
{ echo "arm=$arm attempt=$attempt display=$DISPLAY"; env | grep -E '^(DOTNET_ROOT|LIBGL|GALLIUM|LP_NUM|SDL_|MESA_|LD_LIBRARY_PATH)=' | sort; dotnet --version; } > "$runs/run-$arm-$attempt.env.txt"
cd "$repo"
nice -n 10 .venv/bin/python -I experiments/nu-r04-pause-runtime/run.py "$prepared" "$arm" \
  experiments/nu-history-b1/checkpoint/gameplay.symbol "$out" --timeout 600
