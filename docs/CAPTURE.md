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
   themselves.
3. **Copy each state as a static page.** `tools/capture/signed-in/snapshot.js`
   copies the DOM with every stylesheet inlined from the CSSOM, redacts names
   and emails, strips signing parameters from URLs, and marks scrolled
   elements. One copy per state (a menu open, a dialog, the phone layout).
4. **Render and measure headless from the copies.** `render.mjs` at 2x in
   both themes, `measure.mjs` for computed styles per state (hover with the
   pointer, focus-visible with real keyboard focus), `layout.mjs` for page
   geometry, `icons.mjs` for the icon set.
5. **Shrink the screenshots.** `quantize.py` converts to sRGB 256-colour
   PNGs (61 MB became 15 MB on Duolingo). Flat UI colours survive exactly.
6. **Build.** `build_tokens.py`, `build_style_guide.py`,
   `build_components_md.py`, then open the style guide in both themes.

The Playwright scripts take `PLAYWRIGHT` as the path to any Playwright
install's `index.mjs`. The package READMEs show a path inside self-learn;
any install works. The signed-in scripts take `SNAPS` as the folder of page
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
| Pillow (`pillow`) | `capture/quantize.py` and its per-package copies, `crops.py`, `srgb.py`, `shot.py`, `store.py`, the inline `python3 -c "from PIL import …"` quantize calls in the `.mjs` scripts, `tools/make_icons.py`, `tools/redact_images.py`, linear's `build_guide.py`/`build_library.py`, polaris's `build_vectors.py`, and `tools/catalog.py` gallery thumbnails (macOS `sips` is used instead when present; with neither, thumbs fall back to the full-size screenshot and `build` warns once) |
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

The package README ends with a coverage table: one row per checklist item,
marked captured (with the file that shows it), not present in the product,
or not captured (with the reason, such as "behind a paid plan"). A blank
row is never acceptable; "not captured" with a reason is.

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
   the package.** The owner's own name, email and chat text may stay; a
   password, a code, a phone number, an address or another person's name or
   face may not. A native capture is pixels, so `scan` cannot see any of it.
   Look at every capture and paint those regions over with `sample.py mask
   shot.png X,Y,W,H ...`, which fills each box with the surface colour
   around it. Sample values first, mask second, then quantise.
6. **Do not break the mirror.** Turning off the phone's network or locking
   it ends the session, so offline and lock-screen states cannot be
   captured this way.

## What stays outside the repo

| Thing | Why | Where it lives |
|---|---|---|
| Raw page copies | They hold the account's own chats, files and names | `~/.design-systems/snaps/<slug>/`. The older packages' copies (from self-learn) were deleted on 2026-10-11, so re-rendering one of those packages starts with a fresh capture |
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

Two things the duolingo and coursera runs showed. Names of people other than the
owner are not in the shared pattern file; put them in a second local file and
pass `--patterns` twice, and leave out anything that is also a UI word or a number
(a gem total, the product's own name), or the net paints it everywhere. Text typed
into a focused input is not read by OCR, so give it a rectangle. A `rows` rectangle
whose right edge touches a coloured button smears that colour across the fill; end
it a few pixels short. A pattern that matches a logo word next to a heading is
reported as spanning lines; if it is a false positive, list the image under
`ocr.wrap_ignore` and `check --rules` stops flagging it.

## Traps that cost time before

Browser and capture:

- The Claude in Chrome JS tool truncates results at about 1000 characters.
  A loopback sink (`sink.py` on 127.0.0.1) or a hidden `<article>` read back
  with `get_page_text` gets data out. Output containing `=` or `;` can be
  blocked as cookie data; swap those characters first.
- In the built-in browser pane, a `javascript_tool` result over the size
  limit spills to a file. That spill is a clean data channel: one
  `__snap()` call per state. A spill is reported as an error, so never put
  it in the same `browser_batch` as anything else.
- When the pane or window is hidden it does not paint, so
  `requestAnimationFrame` stalls: menus still mount, but entrance and exit
  animations freeze, virtualised lists never fill and drawers stay off
  screen. A hover reaches the page only with the next action; take a tiny
  screenshot before snapshotting.
- `screencapture -l <windowid>` gives crisp 2x shots only while the window
  is uncovered, and they are Display P3. Convert to sRGB.
- Some sites block `eval` on fresh loads (CSP). Paste the kit inline after
  every hard navigation and prefer in-app link clicks.
- A MutationObserver that redacts names must assign only when the text
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
- Redact health, money and other personal titles in chat lists even after
  the name is gone.

## A quicker, shallower path

When a full capture is more than a job needs,
[dembrandt](https://github.com/dembrandt/dembrandt) reads computed styles
from a public URL and writes DTCG tokens or a DESIGN.md
(`npx dembrandt <url> --dtcg`, `--design-md`). It reads public pages only,
so it misses everything behind a sign-in, and its output does not follow
this repo's evidence labels. Keep its output out of `systems/` until each
value has been checked and labelled.
