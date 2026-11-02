# Real keyboard input to the unchanged standalone game: a new check (2 November 2026)

**Status: protocol fixed before any build or run.** Results are added afterwards in their own section and do not change this protocol.

## This is new work, not the R02 input gate

**Authority.** NEEDS-HUMAN item 7, approved by the user on 2 November, about 20:00 HKT, relayed by the orchestrator. The user left the new-versus-continued question to the orchestrator, who chose **option (a): new work**.

This check is **separate from the stopped R02 input-construction gate** ([PLAN's return](../PLAN.md#where-current-information-lives)). That gate stays stopped:
- the returned draft `experiments/nu-r02-input-feasibility/` stays untracked, **unread** and untouched;
- nothing here is copied from it, and nothing here resumes, corrects or replaces it;
- a pass or a failure here is not an R02 gate result.

The package is written from scratch, using only the pinned Nu source and the facts in STATUS ("Groundwork for the next step").

## Question

Does a key press sent through the X server reach the **unchanged** standalone MMCC Breakout game, so that the effect can be seen **from outside the process**, in screenshots only?

Earlier Nu checks published the game's own events from inside the process. This one does not touch the process at all. It sends ordinary X input events, which SDL's X11 backend reads exactly as it reads a physical keyboard. Then it looks at the screen.

## What runs

- **Game:** pinned Nu `064f7ae` (archive `.artifacts/r03-feasibility-20261015/nu-064f7ae.tar`, SHA-256 `eb0aa771…f92b`), `Projects/Breakout Mmcc`, unchanged.
  - No research bridge, no patch, no probe assembly.
  - It is started the ordinary way, with `dotnet "Breakout Mmcc.dll"` from its build folder. `Program.fs` calls `World.run`.
  - The window is 1280×720: the 640×360 virtual resolution times `DisplayScalar 2` from `App.config`.
- **Package** `experiments/nu-keyboard-input-check/`:
  - `prepare.py` extracts the archive unchanged after checking its hash;
  - `build.py` runs `dotnet build "Projects/Breakout Mmcc/Breakout Mmcc.fsproj" -c Release`;
  - `input_check.py` is the check itself.
- **Environment:** `scripts/linux_nu_env.sh` on a new Xvfb display `:95` (1920×1080×24, no window manager), Mesa llvmpipe with the OpenGL 4.6 override. `NUGET_PACKAGES` points at a private copy of `.artifacts/nuget-packages/`. There is a 600-second deadline per run.

## How input is sent

All input goes through the X server's **XTEST extension** (`libXtst.so.6`, called from Python with `ctypes`). This is the X server's standard way to inject device events. The server delivers them as ordinary `KeyPress`/`KeyRelease` and `ButtonPress`/`ButtonRelease` events. Nothing is written into the game's memory, files or events.

- **Keys:** the **Right arrow** (keysym `0xFF53`) and the **Left arrow** (`0xFF51`), mapped to keycodes with `XKeysymToKeycode`. Each key is held down, then released (`XTestFakeKeyEvent`). The game moves the paddle 4 units per update while `World.isKeyboardKeyDown` reports the key, clamped to ±128 (`Gameplay.fs`).
- **Mouse:** the pointer moves to a button's centre (`XTestFakeMotionEvent`), then presses and releases button 1. Buttons:
  - Title: Play at (0, 0) and Exit at (0, −96);
  - Gameplay: Quit at (232, −144).

  These are virtual coordinates from `Title.nugroup` and `Gameplay.fs`, converted to window pixels by the 2× scale.
- **Focus:** there is no window manager, so the harness gives the game window keyboard focus once with `XSetInputFocus`, as a window manager does when a window is clicked. This is declared now, not added after a failure.
- The window is found by its X name, `Breakout Mmcc`. It must be 1280×720; otherwise the run is invalid.

## How the screen is observed

Screenshots come from `xwd -root` and are cropped to the window. Points are read at virtual coordinates (x right, y up, origin at the window centre). These rules are fixed now:

- **Title is stable:** at least 10 s after the window appears, three screenshots 1 s apart are identical over the central region (x from −100 to 100, y from −40 to 40, sampled every 10 units), and the gameplay signature below is absent.
- **Gameplay signature:** all of these hold:
  - the left and right walls (x = ±164, sampled every 10 units in y from −170 to 170) are dark (every channel ≤ 48) in at least 32 of 35 samples;
  - the top wall (y = 176) is dark in at least 28 of 31 samples;
  - at least 25 of the 30 brick centres are lit (brightest channel ≥ 96);
  - at least 8 of the 10 brick centres in the top two rows (y = 128 and 144) are lit. The Title label covers the lower brick rows, so these two rows tell the screens apart.
- **Paddle colour:** taken from the first gameplay screenshot, at the paddle's known start (x = 0, y = −160). It is the median colour of 7 samples at x = −24 … 24, and at least 6 samples must lie within 40 per channel of it.
- **Paddle position:** on rows y = −157, −160 and −163, between the walls (x from −160 to 160), find the longest run of pixels within 40 per channel of the paddle colour. A row counts if its run is 48 to 80 units wide (the paddle is 64). The paddle centre is the median of the counted rows' run midpoints, and at least 2 rows must count.
- **Lives (recorded only):** the number of the 5 life sprites at (−240, −16·(i+1)) that show the paddle colour.

## Sequence and pass conditions

1. **Harness self-test (attempt 00, no game):** on an empty Xvfb display, the script opens the display, finds XTEST and parses one screenshot. This tests tools only and is recorded.
2. **Prepare and build:** both exit 0.
3. **Launch, find the window, wait for a stable Title.**
4. **Play by real click.** Up to 3 clicks, 10 s apart, each followed by up to 30 s of waiting for the gameplay signature. Clicks that land during the splash are ignored by the game, which is why more than one is allowed. The click count is recorded.
5. **No-input control:** the paddle is found at x = 0 (within ±4) in the first gameplay screenshot. Otherwise the run is **invalid**: the observation, not the input, failed. 0.5 s later, with no input, it is still within ±4 of the first position.
6. **Right:** hold Right, taking screenshots continuously, until the paddle centre is ≥ +64 or 20 s pass; release; screenshot 0.3 s later.
7. **Left:** the same with Left, until ≤ −64.
8. **Release check:** 1 s after releasing Left, the paddle is still within ±4 of its post-Left position, so no key is stuck.

**PRIMARY PASS** means all of the following:
- gameplay was reached by a real click;
- the no-input control stayed still;
- after Right, the centre is ≥ +64;
- after Left, the centre is ≤ −64;
- the paddle stopped after release.

**PRIMARY FAIL** means any of those failed while the observation was valid.

**INVALID** means one of these:
- the window was not found or had the wrong size;
- the Title never stabilised;
- the paddle colour or start position could not be located.

**Known risk, declared now:** the ball keeps moving and the board has 5 lives. If all lives are lost before step 7, the game stops moving the paddle, and the Left step would fail. Lives are recorded on every judged screenshot so such a failure can be told apart.

**Secondary results (reported separately; they do not change the primary result):**
- click Quit, reaching a stable Title;
- click Play again, giving a **fresh** board: paddle within ±4 of 0, and 5 lives shown;
- click Quit, then Exit: the game exits with code 0 within 30 s.

## Rules

- Every attempt is kept in `.artifacts/keyboard-input-check-20261102/`, with:
  - the trace;
  - the judged screenshots as PNG;
  - game stdout and stderr;
  - `result.json`.
- Environment-only fixes are allowed, such as display or library settings. Each is logged as a new attempt.
- **The judging rules above may not be tuned after seeing a result.** If a rule proves wrong (for example, a brightness threshold), the failed attempt is kept. Any correction goes in a dated amendment committed before the next attempt, and the failed attempt counts toward the stop rule.
- **Stop rule:** five unresolved failures (fail or invalid) at one unchanged step means stop and report.

## What this check cannot show

- Only the paddle keys and three buttons in one game; no other input, text entry or controller.
- Under Xvfb with software OpenGL, with no window manager and no physical device. Desktop focus handling and real keyboard hardware are not covered.
- No timing claim: the frame rate under llvmpipe means nothing.
- No pause, audio, gameplay-correctness or rendering-parity claim, no agent access, and no benefit.
- It says nothing about whether the stopped R02 draft would have worked.

## Amendment 1 (2 November 2026, ~20:15 HKT, before attempt 02): how the window name is read

**What happened in attempt 01.** The game started normally: SDL 3.5.0 and OpenGL 4.6 under Mesa initialised. But the script did not find the window within 120 s, so the run was **invalid**. It is kept, and it counts toward the stop rule.

A passive diagnostic (`diag-01`: `xwininfo` and `xprop` only, no input sent, game stopped after 30 s) showed why:
- the window exists, named `Breakout Mmcc`, at 1280×720, position +320+180;
- SDL3 stores its `WM_NAME` with type `UTF8_STRING`, and the Xlib call `XFetchName` returns only names of type STRING.

**Change.** The window name is now read with `XGetWMName`, which returns the raw bytes of `WM_NAME` whatever its type. The rule itself is unchanged: the window must be named exactly `Breakout Mmcc` and be 1280×720. No judging rule, threshold or step changes.

## Amendment 2 (2 November 2026, ~20:30 HKT, before attempt 03): how screenshots are captured

**What happened in attempt 02.** The window was found at 2 s: 1280×720 at +320+180. Then the first screenshot was rejected as an "unexpected xwd format" (24 bits per pixel), and the harness stopped. The run is **invalid**, kept, and it counts toward the stop rule. The game process outlived the harness, and I stopped it by hand.

A passive diagnostic (`diag-02`: `xwd` headers only, no input) showed why:
- the game window uses a **DirectColor** visual, while the root window uses TrueColor;
- with both on screen, `xwd -root` switches to a mixed-visual layout: 24 bits per pixel, 8-bit padding, 32-bit row stride;
- `xwd -id <game window>` gives an ordinary 32-bit image of the window alone.

**Changes:**
- Screenshots are taken with `xwd -id <game window>` instead of `-root`, so no cropping is needed.
- For a DirectColor window, each colour channel is mapped through the colour map that `xwd` stores in the file.
- The harness now always stops the game process if it fails itself.

No judging rule, threshold or step changes.

**Capture self-test before attempt 03 (passive, no input, kept as `capture-selftest`).** The game was launched and screenshots taken at 12 s and 20 s:
- at 12 s the window is black (still loading);
- at 20 s it shows the Title (label, Play, Credits, Exit) with correct colours;
- the unchanged gameplay signature correctly reports **not gameplay** on the Title: 0 of 10 upper brick spots lit. The Title label lights the 20 lower spots, as the protocol anticipated.

This checks the tools only and is not a judged result.

## Amendment 3 (2 November 2026, ~20:50 HKT, before attempt 04): brick sample point, and waiting for the fade-in

**What happened in attempt 03 (a recorded FAIL, counted toward the stop rule).**
- The window and capture worked.
- The "stable Title" rule fired at 12.3 s on the **black loading screen**, so Play click 1 was ignored.
- Play click 2 (52.8 s), on the visible Title, **did** start gameplay: the Title label vanished from the screen.
- The gameplay signature never matched, so the run ended with "gameplay not reached after 3 Play clicks". No key was sent.

**Diagnostic `diag-03` (not judged; one Play click on the visible Title, screenshots every 2.5 s, no keys).** It showed the gameplay screen correctly: walls, 30 bricks, the white paddle at the bottom centre, 5 lives and Quit. It also showed two rule problems:
1. Each brick image has a **black line exactly at its centre**, where the signature sampled, so all 30 bricks read as unlit.
2. Gameplay **fades in** over about 6 s at this frame rate. The paddle reads grey 153, then 212, then 255 in successive screenshots. A paddle colour taken mid-fade would not match later frames.

The unchanged paddle rule, applied to the settled diagnostic frame, found the paddle at x = −0.25 and counted 5 lives.

**Changes:**
- The brick sample point moves to **4 units above each brick centre**, in the brick's upper half. Thresholds are unchanged. Checked against every saved image: the Title, the loading black and the early fade frames all read as "not gameplay", and the settled gameplay frames read as gameplay with 30/30 bricks lit.
- **Settling:** after the signature first matches, the harness takes screenshots 0.5 s apart until the paddle colour at its start position agrees within 8 per channel in two of them (up to 10 s). The first gameplay screenshot used for the paddle colour and the no-input control is the settled one.

Nothing else changes. Known waste that is not fixed: the Title rule can fire on the black loading screen. The 3-click allowance already covers that. Attempts so far: 01 invalid, 02 invalid, 03 fail. **Two more unresolved failures would trigger the stop rule.**

## Amendment 4 (2 November 2026, ~21:05 HKT, before attempt 05): a stricter "settled" test

**What happened in attempt 04 (INVALID, counted toward the stop rule).**
- Play click 1 again landed on the black loading screen.
- Click 2 started gameplay, and the corrected signature matched at 72.6 s (27 lit bricks, 8 in the top rows).
- The amendment-3 settle test passed at once: the paddle read grey 127 in two screenshots 0.5 s apart. At this frame rate **the screen had not changed between them**, so the fade was still under way.
- At that grey the paddle could not be told from the darkened background. The paddle was not found at x = 0, so the run was invalid before any key was sent.

**Change.** "Settled" now means:
- the gameplay signature holds;
- **every channel of all 7 paddle start samples is ≥ 240**. The paddle image is white: the settled diagnostic frame reads (255, 255, 255), as do the life sprites.

The check repeats every 0.5 s for up to 30 s.

**Checked against all 17 saved screenshots** (diag-03, the capture self-test, attempts 03 and 04): only the fully faded-in diagnostic frame counts as settled. On it the unchanged paddle rule finds x = −0.25 and 5 lives. Every fade frame (59 … 212 grey) and both attempt-04 frames are rejected.

Nothing else changes. Attempts so far: 01 invalid, 02 invalid, 03 fail, 04 invalid. **Attempt 05 is the last one before the stop rule applies.** If it fails, I stop and report.

## Results (added 2 November 2026, ~21:20 HKT, after attempt 05)

**Conclusion: real keyboard and mouse input sent through the X server reaches the unchanged standalone game, and its effect is visible from outside. But by the protocol's own rule, attempt 05 is a PRIMARY FAIL, on the release check alone.** It was the fifth unresolved attempt, so the stop rule applies. I stopped and did not rerun.

**Attempt 05, in detail** (evidence `run-05/`):

| Check | Result |
| --- | --- |
| Gameplay reached by a real click | **Yes.** Click 1 landed on the black loading screen again and was ignored; click 2 worked. |
| No-input control | **Still:** −0.25, then −0.25 again 0.5 s later. |
| Right held | **Moved:** from −0.25 to **+67.75**. The first visible movement came 1.16 s after key-down; the target was reached about 7.6 s after key-down. |
| Left held | **Moved:** from +67.75 to **−64.25**. |
| Stopped after release | **No, by the rule:** −64.25 at 0.3 s after release, −72.25 at 1.3 s. That is 8 units, 2 game updates, against an allowance of 4. |
| Lives | 5 throughout. |

**Secondary results (all passed, all by real clicks):**
- Quit reached a stable Title.
- Play again gave a **fresh board**: paddle at −0.25 and 5 lives.
- Quit, then **Exit**: the game exited with **code 0** after 0.27 s.

**What the release failure probably is, and what is not shown.** The game ran at about **2.5 updates per second** under software rendering: 16 updates took about 6.4 s. What is on screen trails the key state by about 2 updates:
- after Right went down, nothing moved on screen for 1.16 s;
- after Right was released and Left pressed, the screen still moved the paddle right by 8 units (67.75 → 71.75 → 75.75) before it reversed.

The 8 units of drift after Left was released are the same 2 updates. So the most likely reading is **display lag, not a stuck key**. But the run ended before a later screenshot could show the paddle at rest. The protocol's 1-second allowance assumed a much higher frame rate. This interpretation was made after the result and is not a pass.

**All attempts** (kept in `.artifacts/keyboard-input-check-20261102/`):

| Attempt | Outcome | Cause | Fix (amendment, committed before the next attempt) |
| --- | --- | --- | --- |
| 00 | harness self-test passed | — | — |
| 01 | invalid | window name stored as UTF-8 | 1: read `WM_NAME` with `XGetWMName` |
| 02 | invalid | mixed-visual `xwd -root` image | 2: capture the window with `xwd -id`, apply its colour map |
| 03 | fail | brick sample point on a black line | 3: sample above centre; wait for the fade-in |
| 04 | invalid | settle test passed mid-fade | 4: settled means a white paddle |
| 05 | **fail** | release check: 8-unit drift | none: stop rule |

Diagnostics that sent no keys (`diag-01`, `diag-02`, `diag-03`, `capture-selftest`) are kept too. Only `diag-03` sent input: one Play click.

**What this establishes:**
- On this server, **XTEST input reaches unchanged standalone MMCC Breakout through SDL's X11 backend**: two keys and three buttons. The effects can be judged from outside, from screenshots alone.
- No in-process event publishing or probe was used.
- This is **new work**. It is not the R02 input gate, which stays stopped, with its returned draft unread.

**What it does not establish:**
- a clean pass of the frozen protocol;
- release timing;
- anything under a real window manager or with real hardware;
- frame-rate-independent timing;
- other keys or games, pause, audio, agent access or benefit.

**What would settle the release question (not done; it needs a new written protocol):** a check whose release window is measured in game updates, judged from screenshots over several seconds after release. For example: "no further movement over 5 s once motion has stopped". It could also use a lighter scene or a faster renderer.

**Cleanup (logged).** I deleted this check's scratch source tree (2.4 GB), the build outputs inside it and the NuGet copy (1.0 GB). All of it can be rebuilt with `prepare.py` and `build.py`. I stopped my Xvfb displays `:93`, started by the build wrapper, and `:95`.
