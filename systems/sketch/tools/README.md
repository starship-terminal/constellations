# Capture kit

The starting scripts for capturing a new product into `systems/<slug>/`. Copy
the kit into the package, then adapt the marked parts. A package keeps its own
adapted copy under `systems/<slug>/tools/`, because that copy is the record of
how its values were read; this folder is only the starting point.

```bash
mkdir -p systems/<slug>/tools
cp -R tools/kit/capture systems/<slug>/tools/capture
cp tools/kit/build/* systems/<slug>/tools/
```

A native iOS app uses `native/` in place of `build/`, from Grok Bot, the first
package built with this native pipeline:

```bash
mkdir -p systems/<slug>/tools/capture
cp -R tools/kit/capture/native systems/<slug>/tools/capture/native
cp tools/kit/native/quantize.py systems/<slug>/tools/capture/quantize.py
cp tools/kit/native/*.py tools/kit/native/crops.json systems/<slug>/tools/
rm systems/<slug>/tools/quantize.py
```

The process, the coverage checklist and the traps are in
[docs/CAPTURE.md](../../docs/CAPTURE.md). What a package must contain is in
[docs/PACKAGE.md](../../docs/PACKAGE.md).

Python deps (Pillow for `quantize.py` and the inline PIL calls in the `.mjs`
scripts, and whatever a route adds) are in
[tools/requirements-capture.txt](../requirements-capture.txt), installed by
`make setup`; the `.mjs` scripts call `process.env.PYTHON || 'python3'`.
See [docs/CAPTURE.md](../../docs/CAPTURE.md#dependencies) for the full table.

## Which route

| Product | Route | Scripts |
|---|---|---|
| Public web pages | Headless Playwright straight from the URL | `capture/public/` (from gauth), with its own `build-measurements.mjs`; use `build/build_components_md.public.py` as the package's `build_components_md.py` |
| Signed-in web app | The owner signs in to a real browser; `snapshot.js` copies each state to disk, then everything is rendered and measured headless from the copies | `capture/signed-in/` (from claude, with chatgpt's measurement builder) |
| Signed-in web app, live evidence | Use the owner's selected visible browser and the current harness's supported screenshot and read-only DOM tools when copies lose behaviour or layout | Record the same viewport fields below; these Playwright scripts still render copies and do not attach to that browser |
| Native iOS app | iPhone Mirroring on the Mac; values are sampled from window screenshots | `capture/native/` to capture, `native/` to measure and build (from grokbot) |
| Electron desktop app | The owner opens the app with `--remote-debugging-port`; screenshots and CSS variables are read live from the running app | `capture/electron/shot.mjs` ([docs/CAPTURE.md](../../docs/CAPTURE.md#desktop-apps)) |
| Native desktop app | As the iOS route, with the app's own window | `capture/native/winid.swift`, `sample.py`, `native/` |

`vars.mjs`, `layout.mjs`, `icons.mjs`, `motion-probe.mjs` and `quantize.py` serve both web routes.
The `build/` scripts serve every route.

## Screenshot dimensions and acceptance

The public, signed-in render and Electron routes use
[`capture/screenshot.mjs`](capture/screenshot.mjs). Each PNG gets a neighbouring
`<name>.png.capture.json` with its capture time, requested size and pixel ratio,
configured viewport, actual `innerWidth` / `innerHeight`, visual viewport
(including scale and offsets), actual device pixel ratio, safe root theme
classes/attributes, document size and PNG dimensions. The helper does not read
the page URL; a caller may explicitly supply `sanitizedSourceUrl` after removing
credentials, signed query parameters and banned personal data.

The existing commands and arguments stay the same. Copy the whole capture tree
as shown above: [`render.mjs`](capture/signed-in/render.mjs),
[`public.mjs`](capture/public/public.mjs) and
[`shot.mjs`](capture/electron/shot.mjs) now import the shared helper one directory
above their own folder. When updating an older package's individual script,
copy that helper into its corresponding capture folder too.

The helper checks the PNG header dimensions against the capture region and
scale, allowing one physical pixel for rounding. Viewport, full-page and clipped
tile captures record their different size bases. A mismatch throws and leaves a
failed sidecar in scratch so the operator can diagnose it. A passed dimension
check still leaves visual review pending and crop-coordinate alignment
unverified. Keep sanitized metadata with the retained evidence; preserve each
tile's sidecar when stitching and record the stitched image's final dimensions.

Inspect each final screenshot before accepting coverage. Reject blank, clipped,
unsettled or unintended states, recapture them, and keep rejected attempts outside
the package. Requested dimensions describe intent. Label evidence with the
measured CSS viewport, and choose crop/masking boxes against the saved PNG;
neither a DOM rectangle nor a viewport-to-PNG ratio proves that the layouts align.
Use the same checks for screenshots from a live browser, recording unsupported
metadata as unavailable rather than guessing it.

Record themes and states actually observed in the live product. Rendering a
static copy with alternate theme classes is a reconstruction; label it separately
and do not count it as live theme evidence or infer matching state coverage.
Theme changes in the owner's account need approval, followed by restoration and
verification. Keep public marketing demos separate from signed-in app coverage.

Run the browser-free contract tests with
`node --test tools/kit/capture/test_screenshot.mjs` (also included in `make test`). The motion
readings have their own: `node --test tools/kit/capture/test_motion.mjs` (the probe test needs the
capture Playwright and is skipped without it).

## Generic: use as they are

| File | Does |
|---|---|
| `capture/quantize.py` | Converts screenshots to sRGB 256-colour PNGs |
| `capture/screenshot.mjs` | Saves a Playwright PNG plus viewport/theme metadata and validates PNG dimensions; visual acceptance and crop alignment still need review |
| `capture/signed-in/snapshot.js` | Pasted into the signed-in page; copies one state with stylesheets inlined, scripts removed, configured banned text redacted and signed URLs cut |
| `capture/signed-in/unsnap.py` | Writes a snapshot to disk; refuses it if a redacted string or a signing parameter survived. Needs `SNAP_REDACT` |
| `capture/signed-in/redact.example.json` | The shape of the redaction file, which lives in `~/.design-systems/<slug>-redact.json` |
| `capture/signed-in/render-all.sh` | Renders every row of `shots.tsv`: a copy taken in dark (`-dark` in its label) in both themes, any other once |
| `capture/motion.mjs` | The motion probe's library: normalises durations and easings, zips transition and animation lists, diffs a normal read against a reduced-motion one, and carries the two page readers. Tested in `capture/test_motion.mjs` |
| `capture/motion-probe.mjs` | Reads every element's transitions and animations, the `@keyframes`, the authored `prefers-reduced-motion` rules and the motion custom properties, then reads the same elements again under `page.emulateMedia({ reducedMotion: 'reduce' })`. Writes `raw/motion.json`. `SNAPS=<dir>` for signed-in copies, `--urls` for public pages ([docs/CAPTURE.md](../../docs/CAPTURE.md#motion)) |
| `build/motion.py` | Turns `raw/motion.json` into the `core.motion` token group with evidence labels. Product-free; `build_tokens.py` imports it when the file exists. Copied with the rest of `build/` |
| `capture/native/shot.sh` | `shot.sh <slug> <theme> <name>`: the mirroring window alone, in sRGB, to `~/.design-systems/<slug>/raw-shots/<theme>/` |
| `native/quantize.py` | The native `quantize.py`: keeps the window's transparent corners |
| `native/crops.py` | Cuts `components/crops/` from `screenshots/` by `crops.json` |
| `capture/native/winid.swift` | The iPhone Mirroring window id, for `screencapture -l` |
| `capture/native/sample.py` | Flat fills, text colours and edge positions from a screenshot (tested in `tools/test_sample.py`) |

## Adapt: the marked parts

Search each file for `PRODUCT (adapt)` first, then work down this list.

| File | Change |
|---|---|
| `capture/signed-in/shots.tsv` | One row per page copy: `<page>-<theme>-<state>`, plus `full` and `scroll=` flags |
| `capture/signed-in/lib.mjs` | The `CDN` pattern, how to switch the copy to light (`setLight`), the stylesheet count that proves a copy came up styled |
| `capture/signed-in/render.mjs` | The light-theme switch, if it differs from `lib.mjs` |
| `capture/signed-in/measure.mjs` | `SPECS`: one entry per checklist component the product has, found by role or structure, never by account text; `M()` and `S()` helpers; the attribute list; the `_meta` source strings |
| `capture/signed-in/build-measurements.mjs` | The heading (`PRODUCT`, or the `PRODUCT` env var; the kit's copy says ChatGPT) and the intro and States paragraph of `measurements.md` |
| `capture/vars.mjs` | The probe `shell` (the kit's copy carries Claude's `data-theme="claude"` root and `.dframe` sidebar), which selectors carry the theme, how names are binned, the source string. If stylesheets are cross-origin, swap in manus's CDN-chunk reader or gauth's network-response reader |
| `capture/motion-probe.mjs` | `prepare()`: what a public page needs before it shows its real UI (a promo or cookie dialog). Read the pages and states where the product moves, not only the landing page |
| `capture/layout.mjs` | The product block naming the shell's regions; keep the generic part (widths, grids, fixed bars, dialogs, menus) |
| `capture/icons.mjs` | Ships the inline-SVG strategy. For an icon font use `systems/claude/tools/capture/icons.mjs`; for SVG sprites, `systems/chatgpt/tools/capture/icons.mjs`. Fill `icon-names.tsv` |
| `capture/public/*.mjs` | `BASE`, `PAGES`, the promo and dialog dismissers, `M()`, and the two prose blocks in `build-measurements.mjs`. `public.mjs` writes full-colour shots to `~/.design-systems/<slug>/raw-shots` unless `RAW` names another scratch folder |
| `build/build_tokens.py` | The header constants and the whole mapping from readings to `core`, `light` and `dark`; keep the helpers, build and checks, and the `motion.json` hook that adds `core.motion` |
| `build/build_components_md.py` (signed-in) or `build_components_md.public.py` (public) | `PREFER`, `ORDER_GROUPS`, group and page descriptions, the intro and the Gaps section. The two read different measurement files, so use the one that matches the route |
| `build/style-guide.template.html` | The theme attribute (`data-mode` or a `.dark` class), the token group names, and the whole Components section |
| `native/measure.py` | `NAME` and the reading table `R`: one box per value, in capture pixels on this product's screens. It writes `raw/readings.json` and `raw/<slug>-measured.md` |
| `native/build_tokens.py` | `core()` and `semantic()`: the mapping from readings to tokens. Keep the helpers, `check()` and `build()` |
| `native/build_style_guide.py` | `NAME`, `OWNER`, `LEDE`, the specimen text and the Components specimens, drawn from tokens only |
| `native/build_components_md.py` | `NAME`, `INVENTORY` (one row per checklist component, with its crops) and `GAPS` |
| `native/test_build_tokens.py` | Nothing: its fixture is product-free, and it also checks the package's own `tokens.json` once one exists |
| `native/crops.json` | One box per component state, in capture pixels; Grok Bot's boxes are the example |
| `build/build_style_guide.py` | Usually nothing; it renders a light-only package too, and the template then starts in light with the theme toggle hidden |

## Never commit

Follow the current repository privacy policy in [AGENTS.md](../../AGENTS.md).
Mask credentials (passwords, one-time/recovery codes, API keys, tokens, session
cookies and signed URLs) and banned personal data (phone numbers, street
addresses, precise locations, dates of birth, government/payment/bank numbers,
and other people's email or contact details).

The private library permits the owner's profile, including their email, their
chat/document/project text and time zone; other people's names, handles and
profile pictures as the app displays them; and published product content.
Do not build broader redaction lists for permitted names or titles. Derive
redaction rules from the current policy, and run the repository image checker
on signed-in screenshots and crops before committing them.

Keep raw page copies, redaction files and proprietary fonts outside the repo.
Specs should identify elements by role, stable structure or position so capture
scripts do not depend on account text. Sanitize retained readings and screenshot
metadata too; they are evidence, not an exemption from the privacy rules.

## Known gaps in the kit

- The signed-in and public measuring engines differ (the public one can force
  `pressed` and `filled` states through CDP). Merging them is open.
- The oklab and lab to sRGB conversion is repeated in `vars.mjs`,
  `build-measurements.mjs`, `build_tokens.py` and `build_components_md.py`.
- `build_tokens.py` still mixes generic helpers and the product mapping in one
  file; the mapping region is the part to rewrite.
