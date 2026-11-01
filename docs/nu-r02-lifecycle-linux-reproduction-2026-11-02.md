# R02 standalone lifecycle pair: Linux reproduction check (2 November 2026)

**Status: protocol fixed before any build or run.** Results are added afterwards in their own section and do not change this protocol.

## Why

R04, the R03 history pair and the R10 live-reload pair now reproduce unchanged on this server ([R04](nu-r04-linux-reproduction-2026-11-02.md), [R03](nu-r03-linux-reproduction-2026-11-02.md), [R10](nu-r10-live-reload-linux-reproduction-2026-11-02.md)). All three ran inside Gaia (Nu's editor) or a Gaia-like host.

The R02 standalone lifecycle pair from 15 October ([record](nu-standalone-lifecycle-feasibility-2026-10-15.md)) runs the two **unchanged standalone games** instead: MMCC Breakout and ImSim Breakout. Each uses the ordinary `World.runPlus`, and the probe publishes the games' own Play and Quit click events. The sequence is Title → Play → Gameplay → Quit → Title → Play again, which must give a fresh game.

The question is: **does this pair reproduce on this server, unchanged?**

Authority: user pre-approval of autonomous development (2 November). This is the **completed lifecycle package**. It is not the stopped R02 input-construction draft (`experiments/nu-r02-input-feasibility/`), which stays untracked, unread and untouched. No new arm, no physical input, no candidate or model call, nothing Daybreak-only.

## What stays fixed

- Package `experiments/nu-r02-standalone-lifecycle/` exactly as committed: `prepare.py`, `build.py`, `run.py`, the probe sources, the contract and the addendum. It is copied byte for byte to scratch. `prepare.py` records each public input's hash, and `run.py` refuses to run if its own bytes differ from the prepared identity.
- Nu archive `.artifacts/r03-feasibility-20261015/nu-064f7ae.tar`, whose hash `prepare.py` checks, and both unchanged application manifests (also checked by `prepare.py`).
- .NET SDK 10.0.302 (checked by `build.py`) and the exact 600-second deadline (enforced by `run.py`). Run order: `mmcc`, then `imsim`, once each.

## What differs from Windows

- The same display/OpenGL environment as the earlier Linux checks: `scripts/linux_nu_env.sh` with Xvfb and Mesa llvmpipe with the 4.6 override.
- **PowerShell.** `build.py` reads each built assembly's name by calling `powershell` with .NET's `[Reflection.AssemblyName]::GetAssemblyName`, and `run.py` refuses a build without those names. This server has no Windows PowerShell. For the build command only, PATH gets a folder whose `powershell` points to PowerShell 7.4.6 for Linux. That is the official release tarball, SHA-256 `6f601520…e157561` (matching the release's published hash), installed per-user in `~/.local/share/powershell-7.4.6`. It calls the same .NET method. No package byte changes.
- **Acceptance.** On Windows, the build receipt was accepted after an independent review and a parent review before the runs (`--accept-build-sha256`). Here no second reviewer exists. I accept the Linux build receipt only after checking that:
  - both arms exit 0;
  - no original source input changed;
  - assembly names are complete;
  - each host has the same 349-file count as Windows.

  The receipt hash I accept is recorded. This acceptance is weaker than the original and is stated as such.

## Steps and pass conditions

1. **Prepare** (new folder): exit 0. Archive and both application manifest hashes are accepted by `prepare.py` itself. The 3,240-file source manifest identity must equal Windows (`bcdac43e…9ac08`).
2. **Build:** `build.py` exits 0:
   - both arms compile;
   - zero source-input mismatches across the 3,240 files;
   - assembly names complete.

   Compared with Windows (270 warnings per arm, NU1901/NU1902 only, 349 host files), any difference is recorded, not a failure. One exception: a different host file count is a Linux difference.
3. **Runs:** `run.py … mmcc`, then `run.py … imsim`, with the accepted receipt hash. Each must pass:
   - the frozen primary lifecycle oracle, with engine exit 0, no timeout and the owned process terminal;
   - the separately frozen fresh-initializer diagnostic.
4. **Comparison with Windows** (recorded; differences are not failures unless an oracle fails):
   - callback counts (Windows: MMCC 485, ImSim 487);
   - Play/Quit/Play action-to-idle increments (Windows: MMCC 95/95/95, ImSim 95/97/95);
   - the initializer-seam scalars (Playing, time 0, score 0, 5 lives, 30 bricks);
   - ImSim's distinct Scene IDs (Windows: 270 and 1171).

## What counts as a different result

Any of these is a **Linux difference**. It is recorded as found, not fixed and rerun:
- a build failure, missing native library, crash or timeout;
- a primary or initializer oracle failure;
- a host closure different from 349 files.

The stop rule applies: five unresolved failures at one unchanged step means stop. Environment-only fixes are allowed, each logged as its own attempt. No package byte may change.

## What this check cannot show

The original limits stay:
- the Play and Quit clicks are synthetic, published events, not physical pointer input or SDL delivery;
- no audio, framebuffer or pause behaviour;
- no equivalence between the two packages;
- no claim about practical value or agent access.

A pass shows only that this bounded lifecycle observation reproduces on this server.
