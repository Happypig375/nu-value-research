#!/usr/bin/env bash
# Run one command in the Linux environment used for the pinned Nu (064f7ae) reproductions:
# per-user .NET SDK 10.0.302, a private Xvfb display and Mesa llvmpipe software OpenGL
# (reporting 4.6, which Nu at this revision requests). Environment only: no package byte changes.
# See docs/nu-r04-linux-reproduction-2026-11-02.md and docs/nu-r03-linux-reproduction-2026-11-02.md.
# Usage: linux_nu_env.sh RUNS_ROOT ENV_LOG_NAME -- COMMAND [ARGS...]
set -euo pipefail
runs="$1"; log="$2"; shift 2
[ "${1:-}" = "--" ] && shift
[ $# -gt 0 ] || { echo "no command given" >&2; exit 2; }

export DOTNET_ROOT="$HOME/.local/share/dotnet-sdk-10.0.302"
export PATH="$DOTNET_ROOT:$PATH" DOTNET_MULTILEVEL_LOOKUP=0 DOTNET_CLI_TELEMETRY_OPTOUT=1 DOTNET_NOLOGO=1
export LIBGL_ALWAYS_SOFTWARE=1 GALLIUM_DRIVER=llvmpipe LP_NUM_THREADS="${LP_NUM_THREADS:-4}"
export MESA_GL_VERSION_OVERRIDE=4.6 MESA_GLSL_VERSION_OVERRIDE=460
export SDL_VIDEO_DRIVER=x11
[ -n "${NU_LD_LIBRARY_PATH:-}" ] && export LD_LIBRARY_PATH="$NU_LD_LIBRARY_PATH${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"

display="${NU_DISPLAY:-:93}"; n="${display#:}"
mkdir -p "$runs"
xdir="$runs/.x11"; mkdir -p -m 700 "$xdir"
export DISPLAY="$display" XAUTHORITY="$xdir/xauth"
existing="$(pgrep -u "$(id -u)" -a -f "^Xvfb $display " | head -1 || true)"
if [ -n "$existing" ]; then
  # Reuse our own running display with the cookie file it was started with.
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
  env | grep -E '^(DOTNET_ROOT|NUGET_PACKAGES|XAUTHORITY|LIBGL|GALLIUM|LP_NUM|SDL_|MESA_|LD_LIBRARY_PATH)=' | sort
  dotnet --version; } > "$runs/$log.env.txt"
exec nice -n 10 "$@"
