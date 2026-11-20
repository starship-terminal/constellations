# Capturing a product

How the reference packages were made, so the next one takes an afternoon
instead of rediscovering the traps. Start from the shared kit in
[tools/kit/](../tools/kit): copy it into the new package and adapt the parts
its README marks. Each package keeps its own adapted copy as the record of
how it was captured. The `extract-style` skill in the quiver-hub
`design-systems` plugin runs this whole process.

## The order

1. **Find the CSS first.** Open the product and list its custom properties
   on `:root` and on whatever switches the theme (`[data-theme="dark"]`,
   `.dark`, `[data-mode]`). Most products are built on a token system
   (Coursera's `--cds-*`, Brilliant's `--panda-*`, Claude's cds) and nearly
   every value traces to one. `tools/capture/vars.mjs` parses the
   stylesheets and resolves each name the way the browser does.
2. **Decide how to get in.** Public pages load in headless Playwright.
   Signed-in pages are captured in a real browser the owner is signed in to;
   never hand an account to a headless browser. The owner signs in
   themselves. Before handing off sign-in, confirm the browser host, tab
   URL and visible window, and take a screenshot. Name that browser and
   window to the owner; a connected browser may have no visible window.
3. **Capture each state through supported APIs.** Prefer live read-only DOM
   measurements and screenshots when the harness provides them. If it supports
   the static-copy route, `tools/capture/signed-in/snapshot.js` copies the DOM
   with stylesheets inlined, applies configured redaction literals, strips
   signing parameters and marks scrolled elements. Keep copies outside git.
   Configure only what [AGENTS.md](../AGENTS.md) bans. Do not inject the helper
   where the browser API permits only read-only evaluation.
4. **Measure the captured state.** For live captures, save custom properties,
   computed component styles and layout readings with their screenshot. For
   static copies, use `render.mjs`, `measure.mjs` and `layout.mjs`. Label an
   alternate theme or interaction rendered from a copy as a reconstruction;
   its filename does not prove the live app displayed it. Record approval for
   account appearance changes, reuse approval already given, and restore and
   verify the original theme after capture. Read the product's motion with
   `tools/capture/motion-probe.mjs` ([Motion](#motion)).
5. **Shrink the screenshots.** `quantize.py` converts to sRGB 256-colour
   PNGs (61 MB became 15 MB on Duolingo). Flat UI colours survive exactly.
6. **Build.** `build_tokens.py`, `build_style_guide.py`,
   `build_components_md.py`, then open the style guide in both themes.
7. **Record the capture.** The catalog entry's `capture` block says how the
   extraction ran: `harness` and `model` (the agent and model that did the
   work), `version` (the product version captured), `route` (which path
   above was taken), `pr` (the pull request that added the package) and
   `durationMin` (how long the capture took in minutes, summed across
   sessions). Fill it when the entry is created; a number not recorded is
   lost for good.
8. **Generate before checking.** After writing the package and registering
   it in [catalog.json](../catalog.json), run `make design-md`, then
   `make grade`, then `make check` and `make test`. The first two update
   generated Brief, DESIGN.md and Health content; `make grade` also updates
   the root README catalog table. Never add that table's row by hand. Set
   reviewed grades against the platform rubric as described in [AGENTS.md](../AGENTS.md),
   then rerun the checks after writing those grades. This review is not
   optional: the package is not done until `tools/grade.py --write --review`
   has written its grades, and every criterion that cannot grade `meets`
   carries a written justification in the grades file.
9. **Clean up when it merges.** `git worktree remove` the capture worktree,
   delete `~/.design-systems/<slug>/`, and delete the merged branch.

The Playwright scripts take `PLAYWRIGHT` as the path to any Playwright
install's `index.mjs`. The package READMEs show the `~/.design-systems/pw`
install; any install works. The signed-in scripts take `SNAPS` as the folder of page
copies. The `.mjs` scripts run their inline Pillow calls through `python3`;
set `PYTHON` when the interpreter with the dependencies below lives
elsewhere (an activated `.venv` resolves bare `python3` to itself).

## Dependencies

`make setup` installs
[tools/requirements-capture.txt](../tools/requirements-capture.txt) into
`.venv` along with the site builder's requirements. On a capture host
without it, run `pip install -r tools/requirements-capture.txt` into the
interpreter `PYTHON`/`python3` resolves to.

| Dependency | Needed by |
|---|---|
| Pillow (`pillow`) | `capture/quantize.py` and its per-package copies, `crops.py`, the package-only `srgb.py` (brilliant), `shot.py` (duolingo) and `store.py` (researchrabbit), the inline `python3 -c "from PIL import …"` quantize calls in the `.mjs` scripts, `tools/make_icons.py`, `tools/redact_images.py`, linear's `build_guide.py`/`build_library.py`, polaris's `build_vectors.py`, and `tools/catalog.py` gallery thumbnails (macOS `sips` is used instead when present; with neither, thumbs fall back to the full-size screenshot and `build` warns once) |
| numpy (`numpy`) | `tools/redact_images.py` (also needs `tesseract` on PATH) |
| markdown (`markdown`) | `tools/site.py`, linear's `build_guide.py` |
| fontTools + Brotli (`fonttools[woff]`) | polaris's `build_vectors.py` (text measurement; widths drift across versions; Brotli decodes `inter.woff2` to TTF) |
| ffmpeg | `tools/refero/mirror_media.py --compress-videos`; a binary on PATH, not pip (`~/.nix-profile/bin/ffmpeg` is a fallback) |
| `sips` | gallery thumbnails on macOS; optional, Pillow covers Linux |
| Node.js + Playwright | every `*.mjs` capture script |

## What to capture: the coverage checklist

A capture is graded against [DESIGN-SYSTEM.md](DESIGN-SYSTEM.md), the same
list an app's own design system is built to. Plan the shot list from it
before opening the product, so every page you visit is there for a reason.

- **Foundations.** Every group in its foundations table: colour roles in
  each theme, type roles, spacing, radii, borders, elevation, motion,
  sizing, layout.
- **Components.** Button, icon button, link, text field, text area, select,
  checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, card, list
  row, table, avatar, badge. For each one the product has, capture default
  plus every state it shows: hover, focus-visible, pressed, selected,
  disabled, loading, error.
- **Patterns.** App shell and navigation, a form with a validation error,
  empty, loading and error states, a destructive confirmation, feedback
  after an action, search and filtering, a list or table, onboarding.
- **Themes and widths.** Light and dark where the product has both; desktop
  (1440) and phone (390) widths for a web product.

**Screenshots are the shot list; CSS is the values.** Every route captures
every screen and state on the checklist as a full screenshot, in each
theme the product has. Reading CSS adds exact values on top of those
screenshots and never replaces one. A package whose values are all exact
but whose screens are missing cannot show how the product is laid out.

The package README ends with a coverage table: one row per checklist item,
marked captured (with the file that shows it), not present in the product,
or not captured (with the reason, such as "behind a paid plan"). A blank
row is never acceptable; "not captured" with a reason is.

### Browser dimensions and screenshot checks

Record the measured `window.innerWidth`, `window.innerHeight`,
`window.devicePixelRatio` and `window.visualViewport` width, height and
scale with each capture, plus the PNG's pixel dimensions. A requested
browser size is not proof of the CSS viewport: browser zoom and screenshot
scaling can produce different values. If the measured width differs from
the plan, correct it and recapture or label the evidence with its actual
width; do not call it a 1440 or 390 capture from the request alone.

The kit's [screenshot wrapper](../tools/kit/capture/screenshot.mjs) writes
these dimensions to a `.png.capture.json` sidecar and checks the PNG against
the capture mode and scale. Live-browser captures should record the same
fields through their supported APIs. A passing dimension check leaves visual
review pending and does not establish a CSS-to-PNG crop transform.

A signed-in pass is not finished when the first post-login page loads.
Before the last screenshot, write `login-review.offered` from the
signed-in navigation, the settings area, and the create or empty-state
flow. Open every item those three areas show. Record each opened screen
in `login-review.screens`, with the file that shows it, before setting
`login-extracted` to `done`. A review of one screenshot fails the check,
and so does a package screenshot the review never names. The check is
`python3 tools/login_extracted.py --check`, and the states are in
[HANDOVER.md](HANDOVER.md).

Open every final screenshot before ticking its coverage row. For a popup,
confirm the whole popup is inside the image and its entrance animation has
finished; recapture blank or clipped images. Keep the screenshot and CSS
readings tied to the same visible state.

Public marketing pages may contain animated dashboard demonstrations.
Label those as public demos, with their URL and capture time. Use the real
signed-in dashboard for dashboard component and state coverage; a demo only
covers the public page and the demo state actually shown.

### Motion

A package records how the product moves as tokens, and whether it honours
`prefers-reduced-motion` ([decision](decisions/0001-motion-tokens.md)). Screenshots
cannot show either, so this is a reading, not a shot. Run
`tools/capture/motion-probe.mjs` on the same pages the other readings use:

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs SNAPS=<dir of page copies> node tools/capture/motion-probe.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/motion-probe.mjs --urls <url>[,<url>...]
```

It writes `raw/motion.json`. Per page it records:

| Reading | What it holds |
|---|---|
| Motion per element | Every element and `::before`/`::after` that transitions or animates, read from computed `transition-property`, `-duration`, `-timing-function`, `-delay` and `animation-name`, `-duration`, `-timing-function`, `-delay`, `-iteration-count`, `-direction`, `-fill-mode`, plus `scroll-behavior: smooth`. Durations are in ms, easings in one spelling (`cubic-bezier(0.4, 0, 0.2, 1)`), and elements with the same motion share one group with up to three example nodes |
| Reduced-motion pass | The same elements read again after `page.emulateMedia({ reducedMotion: 'reduce' })`. Each transition and animation is `removed` (at or under 1 ms, the usual `0.01ms` reset), `shortened`, `kept` or `changed`; each element is `removed`, `reduced`, `kept` or `partial`. The page verdict is `honours`, `partial`, `ignores` or `no-motion`, and `loops` names the animations that still run forever under reduce. The page's own `matchMedia('(prefers-reduced-motion: reduce)')` answer is stored for both passes: a `false` under reduce means the emulation did not take, so discard the reading |
| Declared motion | The transitions and animations the stylesheets declare, by selector and `@media`/`@supports` context. This is where a `:hover` or state rule shows, which a computed read at rest cannot see; a value still holding `var()` is flagged |
| `@keyframes` | Each name, its steps, and the properties each step sets |
| Authored reduce rules | Every rule under a `prefers-reduced-motion` media query (`reduce` and `no-preference` alike; the media text says which), with its declarations. `@import`ed sheets and a sheet's own `media` attribute are followed. Selectors and conditions are cleaned of URLs and query strings |
| Motion custom properties | Each custom property whose name says duration, easing, motion, transition, animation, delay and so on, or whose value is a time or an easing, with its declared and resolved value on the root |

Then `build_tokens.py` calls `motion.py`, which writes the `core.motion` group
into `tokens.json`: `duration`, `easing`, `transition`, `animation`, and
`$extensions` for the reduce verdict, which properties transition, and keyframes
nothing used. Durations and easings are named after the product's own custom
properties when it has them, else by value (`200ms`, `ease-out`,
`bezier-0_4-0-0_2-1`). Every token carries an evidence label
([EVIDENCE.md](EVIDENCE.md)): Measured for a computed value, a rule or a custom
property; Derived for a keyword expanded to its control points. An easing that
`cubicBezier` cannot hold (`steps()`, a `linear()` spring) goes to
`notTokenised`.

Rules for the reading:

- Run it on the pages where the product has its motion (the app shell, a dialog
  open, a list with rows), not only the landing page. It reads what is in the
  DOM at that moment; an element that is not rendered is not read. For a state
  that only exists after a click, take a copy in that state (signed-in route) or
  run the probe again from a script that opens it.
- A computed read sees the state at rest. Read the sheets' own rules too (the probe
  does) before saying a product has no hover motion.
- JavaScript-driven motion (a spring library, `element.animate`, canvas) leaves no
  computed transition. Say so in the README's coverage table as Not captured, with
  the reason; do not infer a duration from a video or a screenshot.
- A page's reading says when it is incomplete: `capped` (more moving elements than the cap, 6000; the
  rest were read in neither pass, so none is taken for stopped) and `sheetsTruncated` (a rule or custom
  property list cut at 400). Both reach `core.motion.$extensions.incomplete`. Only a real reduction
  counts as honouring: a longer duration, a replacement animation or smooth scrolling that appears under
  reduce is `increased`, and an animation set to `paused` counts as stopped. Pages are keyed `page-1`,
  `page-2`... in `--urls` order (the sanitised URL is inside each record); a run that captures no page
  exits 1 and leaves the earlier `raw/motion.json` alone.
- A reduce verdict of `ignores` is a finding, not a failed capture: the product does
  not honour the setting. Record it; do not tidy it away.
- Raw values pass through `noUrl` before they are written, like every other
  computed value: an animation name or custom property can hold a `url()`.
- Native iOS and desktop routes read screenshots and have no computed styles: record
  motion as Not captured, unless the app is an Electron one the probe can open.

## Native iOS apps (iPhone Mirroring)

A native app has no CSS, so every value comes from screenshots. The hevy
package was made this way and its README shows the evidence labels to use.

1. **Open the app in iPhone Mirroring** on the Mac. The phone must be
   locked, nearby and signed in to the same Apple Account; the Mac asks
   for its own password or Touch ID. Only the owner can do either. The app
   must already be installed on the phone.
2. **Drive it from the Mac.** Clicks and scrolls go through the mirroring
   window; typing comes from the Mac keyboard, which hides the software
   keyboard (so no capture shows it). Scrolling moves a few points at a
   time, so long pages are captured from the top.
3. **Capture the window alone**, uncovered, light and dark:

   ```bash
   screencapture -o -x -l "$(swift tools/kit/capture/native/winid.swift 'iPhone Mirroring')" shot.png
   ```

   Record the scale (1 px = 1 pt, or 2 px) and where the screen sits inside
   the PNG, as the hevy README does. Convert Display P3 captures to sRGB
   before reading values.
4. **Read values with `tools/kit/capture/native/sample.py`.** `fill` gives a
   flat surface (Sampled), `text` the darkest anti-aliased pixel of a label
   (Sampled (text)), `edges` the pixel positions where colour changes, for
   sizes, padding and radii (exact for sizes, Derived for radii). Font
   family is usually not determinable; mark it Not captured.
5. **Mask what [AGENTS.md](../AGENTS.md) still bans before anything enters
   the package.** The owner's own profile and chat text and the content
   the product publishes may stay; another user's name, username or
   avatar, a password, a code, a phone number, an address or another
   person's email may not. A native capture is pixels, so `scan` cannot see any of it.
   Look at every capture and paint those regions over with `sample.py mask
   shot.png X,Y,W,H ...`, which fills each box with the surface colour
   around it. Sample values first, mask second, then quantise.
   - Mask the smallest span that holds the private value: the digits of a
     phone number, not the line that also carries a handle; the street, not
     the whole list row. Neighbouring text of the same style then stays in
     the screenshot, so the layout still reads.
   - Keep the unmasked `.raw.png` outside the repo, beside the capture. It
     is what the values were sampled from, and the only place a masked
     region can be measured again.
   - If a masked string is the only example of its text style in the app,
     say so in the package README and name the `.raw.png` it was sampled
     from. Never draw substitute text over a masked region; the font is
     usually Not captured, so the overlay would be a guess that looks like
     evidence.
   - `redact_images.py check` finds configured patterns and, by default,
     email addresses. The shared `cleanup-redact.json` holds no addresses
     or phone numbers, and the tool does not detect them on its own, so a
     clean result does not clear a native capture. Looking at every
     capture is the check.
6. **Do not break the mirror.** Turning off the phone's network or locking
   it ends the session, so offline and lock-screen states cannot be
   captured this way.

## Desktop apps

First find out what the app is built with. Many desktop apps are a web app
in a native shell, and those have CSS to read.

| In `<App>.app/Contents` | Built with | Route |
|---|---|---|
| `Frameworks/Electron Framework.framework` | Electron (Linear, Notion, Slack, Cursor) | Electron, below |
| `Frameworks/Chromium Embedded Framework.framework` | Chromium in a native shell (Spotify) | Native |
| The binary (`otool -L Contents/MacOS/<exe>`) links `UIKit` or `iOSSupport` | The iPad app on the Mac (Catalyst) | Native |
| None of these | AppKit or SwiftUI (Raycast, Things) | Native |

An app installed from Chrome as a web app is a small launcher that opens
Chrome, so it shows none of these; capture it as a web app.

**When the product also has a web version**, the desktop app shows the
same screens. Capture the web version for those and use the desktop app
only for what exists there alone: the window frame and title bar, native
menus, settings windows, menu-bar popovers.

**Electron.** Quit the app and open it with Chromium's debugging switch;
the owner signs in inside the app itself:

```bash
osascript -e 'tell application "Linear" to quit'
open -a Linear --args --remote-debugging-port=9333
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node tools/kit/capture/electron/shot.mjs <out-dir> <name> https://linear.app
```

`shot.mjs` connects to the running app, screenshots the window's page at
its own size and pixel ratio, and writes beside it every custom property
declared on `:root`, `html` or `body`, with the value it computes to in the
theme on screen. `--hover=<selector>` forces `:hover` through
the DevTools protocol, so no pointer moves. It only reads: navigating,
opening menus and switching themes stay with the person driving the app.
Quit the app and open it normally when done, because any local process can
drive an app whose port is open. Linear 1.32.4 accepted the switch on
2026-10-25 and kept its session across relaunches (the first relaunch came
back signed out, and after one sign-in the session held); an app may
ignore the switch, and then the native route below is the fallback.

**Native and Catalyst.** As for iOS, every value comes from the window's
pixels: `screencapture -o -x -l "$(swift
tools/kit/capture/native/winid.swift '<App>')" shot.png`, converted from Display P3
to sRGB, read with `sample.py`. Hover exists on the desktop, so each hover
state is one more capture with the pointer really over the control.

### The scratch folder for test prompts

A coding harness only shows its running states (streaming output, a tool
call in progress, an approval prompt, the finished result) when an agent
actually runs. The owner allowed test prompts on 2026-10-25, on one
condition: the agent works only in `~/.design-systems/harness-scratch`, a
folder that holds nothing of the owner's.

- **One subfolder per app**, named after the package without `-desktop`
  (`codex/`, `devin/`, `orca/`), so two captures never touch each other's
  files. Create the subfolder, and `git init` it when the app only opens
  repositories. Two packages differ: Cursor, the pilot, used the folder's
  root (its `hello.txt` and `.cursor/`), and Superset's capture script
  names the root as `SCRATCH_DIR` because Superset itself creates the
  `superset/` project folder inside it. Give a new capture its own
  subfolder rather than copying either.
- **Open it as a new project or workspace, in a fresh agent or thread.**
  Never point an agent at the owner's projects, and never open the owner's
  existing sessions: on 2026-10-25 opening a sleeping Devin cloud session
  woke its agent, which posted a message.
- **Apps that copy the project elsewhere.** Conductor turns every project
  into git worktrees under `~/conductor/workspaces/<project>/`, so its
  agent writes there, not in the scratch folder. That copy holds only the
  scratch repository, so it is allowed, but the README must name the
  worktree path and the capture must not let the agent act outside it.
  Check for this before the first prompt in any app that makes worktrees.
- **Harmless prompts only:** "List the files in this folder", "Create
  hello.txt here with one line". Approve an action only when it stays
  inside the subfolder; deny anything else. The owner's harnesses often
  auto-approve (Cursor's auto-run, Superset's and Orca's skip-permissions
  modes, Devin's Bypass Permissions), so an approval prompt often never
  appears; record that in the coverage table rather than changing the
  setting.
- **Keep the folder and what the agents wrote.** It is small, and the
  package READMEs of `cursor-desktop`, `devin-desktop`, `grokbot-desktop`,
  `codex-desktop`, `superset-desktop`, `orca-desktop`, `opencode-desktop`,
  `conductor-desktop` and `capy-desktop` name it in their re-capture steps: some scripts
  reopen the test chat or the `hello.txt` an earlier run wrote. Delete an
  app's subfolder only when its package no longer needs it (Zed's was
  removed on 2026-10-25), and say so in that package's README.
- **It stays outside the repository**, like the raw captures. Nothing in it
  is ever committed; the screenshots that show it are the record.
- **List what each capture created** in the app (test projects, chats,
  bots, workspaces) in the package README, so the owner can delete them.

## What stays outside the repo

| Thing | Why | Where it lives |
|---|---|---|
| Raw page copies | They may retain credentials, signed URLs or other banned data beyond the visible page | `~/.design-systems/snaps/<slug>/`. The older packages' copies (from self-learn) were deleted on 2026-10-11, so re-rendering one of those packages starts with a fresh capture |
| Redaction lists | The literals being redacted are the private data | `~/.design-systems/<slug>-redact.json`, shaped like the package's `redact.example.json`. The older packages' rules are merged into `~/.design-systems/cleanup-redact.json`, the list every package is scanned against |
| CDN caches | Large, and the product's property | Beside the copies, as `<SNAPS>-cdn-cache` |
| Proprietary fonts | Not ours to commit | `systems/<slug>/fonts/`, gitignored |

`unsnap.py` refuses a copy in which a redacted string or a signing parameter
survived. Run it before rendering anything. Before committing, run
`python3 tools/catalog.py scan systems/<slug> --redact ~/.design-systems/<slug>-redact.json`
over the whole package; it must find nothing.

`catalog.py scan` reads text files only. Screenshots and crops are checked by
OCR, as below. Rendering from redacted page copies gives clean images; use the
tool below only when the copies are gone.

## Private text already in the images

When the page copies are gone, or a package was captured before its content was
redacted, paint the regions out of the finished PNGs with
[tools/redact_images.py](../tools/redact_images.py). It needs Pillow, numpy and
`tesseract`, and reads the same pattern file as `catalog.py scan`.

```bash
python3 -m venv /tmp/redact-venv && /tmp/redact-venv/bin/pip install pillow numpy
/tmp/redact-venv/bin/python tools/redact_images.py apply systems/<slug> --rules tools/redact-rules/<slug>.json --patterns ~/.design-systems/cleanup-redact.json
/tmp/redact-venv/bin/python tools/redact_images.py check systems/<slug> --patterns ~/.design-systems/cleanup-redact.json
```

`check` loads `tools/redact-rules/<slug>.json` for the package by itself when
the file exists, and prints a `rules:` line saying so. That file's `ocr` block
allows a product's own published addresses and sets `wrap_ignore`, so a
package with a rules file needs no `--rules` to pass. `--rules <file>` loads
that file instead. `apply` always needs `--rules`, because it edits images in
place.

`apply` changes only the pixels inside the regions it paints, so the image
stays the evidence it was apart from the mask. A file with nothing to paint is
not rewritten. An edited PNG keeps its mode, its palette and tRNS, and every
other chunk (colour profile, pHYs, text) byte for byte. A palette image keeps
every untouched pixel's index and paints with the nearest existing palette
entry, alpha included. The palette is never grown or reordered, so when it has
no entry close to a fill colour, `apply` uses the nearest one and prints how
many pixels that hit; look at those images. RGB, RGBA and grey images are
painted in their own mode, and alpha inside a region is filled like the
colour. Before replacing a file, `apply` decodes the written copy and stops
with the file unchanged if any pixel or alpha value outside the painted
regions differs. It will not edit a JPEG (lossy), a 16-bit PNG or an animated
PNG: it names each one, writes nothing to it and exits 1.

A rules file (see [manus.json](../tools/redact-rules/manus.json) and
[notebooklm.json](../tools/redact-rules/notebooklm.json); duolingo.json and
coursera.json show the net-first style) lists pixel
rectangles per screenshot family and the UI words to keep. Author it with
`redact_images.py lines <image>`, which prints every OCR text line with its
box. Rules hold coordinates and generic UI words only; the private strings stay
in the pattern file. Crops that are only a title are deleted by component name
(`delete_stems`); rebuild `components.md` afterwards, and it drops the missing
images. Look at a contact sheet of every family after an `apply`: OCR does not
read text that is dimmed behind a modal unless the rules say to boost it, and a
pattern file only knows the strings it was given.

Follow the current policy in [AGENTS.md](../AGENTS.md): other people's names,
usernames and avatars are masked, and so are their email and other contact
details. OCR finds a name only when a pattern file lists it and never sees an
avatar, so give each one a rectangle. Add only banned literals to a local pattern file; leave out anything
that is also a UI word or a number (a gem total, the product's own name), or
the net paints it everywhere. Text typed
into a focused input is not read by OCR, so give it a rectangle. A `rows` rectangle
whose right edge touches a coloured button smears that colour across the fill; end
it a few pixels short. A pattern that matches a logo word next to a heading is
reported as spanning lines; if it is a false positive, list the image under
`ocr.wrap_ignore` and `check --rules` stops flagging it. `check` and `apply`
refuse a rules file holding a key at a level that never reads it (a top-level
`wrap_ignore`, an `ocr.families`) or a key they do not know; start a note's
key with `_`.

## Traps that cost time before

Browser and capture:

- Browser APIs and output limits vary by harness. Read the current tool
  documentation and use its supported screenshot, read-only DOM and file-export
  APIs. Older `javascript_tool` spill files and `browser_batch` recipes apply
  only where those APIs exist. Do not encode around a privacy or export block;
  narrow the reading or use an approved route.
- When the pane or window is hidden it does not paint, so
  `requestAnimationFrame` stalls: menus still mount, but entrance and exit
  animations freeze, virtualised lists never fill and drawers stay off
  screen. A hover reaches the page only with the next action; take a tiny
  screenshot before snapshotting.
- `screencapture -l <windowid>` gives crisp 2x shots only while the window
  is uncovered, and they are Display P3. Convert to sRGB.
- Some sites or browser APIs block script evaluation or injection. Use the
  supported reader or screenshot route; record an unavailable reading as a gap.
- A MutationObserver that redacts banned text must assign only when the text
  changes, or it re-triggers itself and freezes the tab.
- Cross-origin stylesheets are invisible to the CSSOM (Manus). Fetch the
  chunks with curl and parse them headless.

Product-specific:

- Theme switches differ. Brilliant's is page-only (`data-theme` on
  `<html>`); Claude's is every `[data-mode]` element; ChatGPT's is the
  `dark` class on every element, the markdown body included; Duolingo's is
  an account setting, so ask before flipping it and restore it afterwards.
- Base UI (Claude) leaves closed popups mounted with `data-closed` and
  `data-ending-style`. Drop them from the copy.
- Virtualised threads (Manus) render blank from a static copy unless the
  inner scroll positions are recorded in the snapshot.
- Canvas content (ResearchRabbit's graph) does not survive a DOM copy. Swap
  the canvas for its own `toDataURL()` image in the copy.
- `networkidle` never settles on some sites (Gauth); wait for a selector.

Hygiene:

- Strip presigned URLs (S3 and CDN signing parameters) from every copy.
- Keep redaction literals out of committed scripts.
- Real DTCG types: a `dimension` is one px or rem length.
- Write new captures first and prune old outputs only after a complete run.
- Follow [AGENTS.md](../AGENTS.md) when deciding what to mask. The owner's
  own profile, chat and document titles may stay; mask other people's
  names, usernames and avatars, credentials, and the personally
  identifiable data listed there, including other people's contact
  details. Keep raw page copies and redaction lists outside git.

## A quicker, shallower path

When a full capture is more than a job needs,
[dembrandt](https://github.com/dembrandt/dembrandt) reads computed styles
from a public URL and writes DTCG tokens or a DESIGN.md
(`npx dembrandt <url> --dtcg`, `--design-md`). It reads public pages only,
so it misses everything behind a sign-in, and its output does not follow
this repo's evidence labels. Keep its output out of `systems/` until each
value has been checked and labelled.
