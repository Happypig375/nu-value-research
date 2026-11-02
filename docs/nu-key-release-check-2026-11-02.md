# Key release, counted in game updates: display lag or stuck key? (2 November 2026)

**Status: protocol fixed before any build or run.** Results are added afterwards in their own section and do not change this protocol.

## Why

The [keyboard input check](nu-keyboard-input-check-2026-11-02.md) showed that real X key and mouse input reaches the unchanged standalone MMCC Breakout game. But it failed its release rule: the paddle drifted 8 units, 2 game updates, within 1 s after Left was released. The game ran at only about 2.5 updates per second, and the screen visibly trailed key changes. That rule was written in seconds, and it could not tell **display lag**, a few late frames, from a **stuck key**, where movement never stops.

**Question:** after a real key release, does the paddle stop within a few game updates and then stay still, or does it keep moving?

**Authority:** development work pre-approved by the user. The orchestrator asked for this follow-up on 2 November, ~21:30 HKT. It is **new work**, separate from the stopped R02 input gate. The returned draft `experiments/nu-r02-input-feasibility/` stays unread and untouched.

## The clock: one new frame = one game update

The check never looks inside the process, so it needs an outside clock. It counts **distinct rendered frames**:
- Nu's loop renders once per update;
- the 3D cube's rotation is set from `GameplayTime`, which grows every update, so every update changes the picture.

The harness takes window screenshots far faster than the game draws (about every 25 ms, against about 400 ms per frame). It counts a frame each time the screenshot differs from the previous one.

**The run checks this assumption itself:** while a key is held, the paddle moves exactly 4 units per update (`Gameplay.fs`). So in each held phase, at least **80 % of the frame-to-frame steps after the first movement must be 4 ± 1 units**. If not, for example because partial frames are counted, the clock is not validated and the run is **invalid**.

## What runs

- **Game:** the same unchanged pinned build as the input check. `experiments/nu-keyboard-input-check/prepare.py` and `build.py` run unchanged: pinned Nu `064f7ae`, `Projects/Breakout Mmcc`, started with `dotnet "Breakout Mmcc.dll"`.
- **Harness:** new `experiments/nu-key-release-check/release_check.py`. It imports these unchanged from `input_check.py` (commit `4be9c8f`):
  - XTEST input;
  - window capture with `xwd -id` and the colour map;
  - the gameplay signature;
  - the paddle colour and position rules;
  - the lives count.
- **Environment:** the same as the input check: `scripts/linux_nu_env.sh`, Xvfb `:95` with no window manager, one `XSetInputFocus`, Mesa llvmpipe with the OpenGL 4.6 override, and a private NuGet copy. Overall deadline 900 s.
- **Keys:** Right (keysym `0xFF53`) and Left (`0xFF51`), held and released with `XTestFakeKeyEvent`. **Mouse:** Play, Quit and Exit, by real clicks, as before.

## Sequence

1. **Title visible (new rule):** the Play, Credits and Exit buttons all read green at virtual (−50, 0), (−50, −48) and (−50, −96), in two screenshots 1 s apart. "Green" means green ≥ 64 with red and blue ≤ 32.
   - On saved screenshots, the visible Title reads (0, 97, 2).
   - The black loading screen and gameplay frames do not match.

   This replaces the old "stable screen" rule, which fired on the black loading screen.
2. **Play by a real click.** Up to 3 clicks, each followed by up to 60 s to reach the gameplay signature. Then wait until the paddle is fully white: all 7 start samples have every channel ≥ 240. These are the input check's amendment-4 rules.
3. **No-input control:** the paddle starts at x = 0 (within ±4), and stays within 2 units over the next **10 frames** with no key. Otherwise the run is **invalid**.
4. **Right:**
   - hold Right, counting frames, until a frame shows the paddle centre ≥ +64;
   - release;
   - then observe **30 more frames**.
5. **Left:** the same with Left, until ≤ −64, then 30 frames.
6. **Leave (secondary):** click Quit, wait for the Title, click Exit, and record the exit code.

For each key, the harness records:
- the press lag: frames from key-down to the first visible movement;
- every held step;
- each release-window frame's paddle centre and life count.

A frame "moved" if its centre differs from the previous located centre by more than 2 units.

## Verdict, fixed now

- **RELEASE WORKS:** in both release windows,
  - the last moving frame is within **5 frames** after key-up, and the remaining 25 or more frames are still;
  - the paddle does not end at the ±128 clamp.

  A stuck key would move the paddle 4 units on every frame, reaching the clamp in about 16 frames. So 25 still frames cannot occur with the key held. The earlier input check saw about 2 frames of lag.
- **STUCK KEY:** in either window, movement continues past 5 frames, or the paddle ends at the clamp.
- **KEY NOT DELIVERED:** no visible movement within 60 frames of a key-down.
- **INVALID:**
  - the window, Title, gameplay or paddle could not be set up;
  - the paddle moved during the no-input control;
  - the clock was not validated;
  - no new frame came for 20 s;
  - the paddle was not located on more than 5 frames of a release window;
  - all lives were lost before a window ended. With no lives left the paddle freezes, which would fake a clean release.

Also recorded but not used in the verdict:
- the press lag against the release lag. Similar numbers support a pipeline delay of a few frames;
- the secondary exit.

## Rules

- Attempts are kept in `.artifacts/key-release-check-20261102/`. Each holds:
  - `trace.jsonl` and `frames.jsonl` (every counted frame);
  - `result.json`;
  - judged screenshots as PNG;
  - game logs.
- Environment-only fixes are allowed, each as a new attempt.
- The rules above are not tuned after a result. A rule correction needs a dated amendment committed before the next attempt, and the failed attempt counts toward the stop rule.
- **Stop rule:** five unresolved failures (stuck-key, not-delivered or invalid) at one unchanged step means stop and report.
- If the first valid attempt gives a verdict, I stop there. I do not repeat a run to get a different verdict.

## What this check cannot show

- One game, two keys, under Xvfb with software OpenGL, no window manager and no physical keyboard.
- Lag is counted in frames, not in milliseconds of real hardware latency.
- It cannot locate where the delay comes from: the X server, SDL's event queue, Nu's input polling or presentation.
- No pause, audio, agent access, gameplay-correctness or benefit claim. Nothing about the stopped R02 draft.
