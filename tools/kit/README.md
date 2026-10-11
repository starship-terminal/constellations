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

The process, the coverage checklist and the traps are in
[docs/CAPTURE.md](../../docs/CAPTURE.md). What a package must contain is in
[docs/PACKAGE.md](../../docs/PACKAGE.md).

## Which route

| Product | Route | Scripts |
|---|---|---|
| Public web pages | Headless Playwright straight from the URL | `capture/public/` (from gauth), with its own `build-measurements.mjs`; use `build/build_components_md.public.py` as the package's `build_components_md.py` |
| Signed-in web app | The owner signs in to a real browser; `snapshot.js` copies each state to disk, then everything is rendered and measured headless from the copies | `capture/signed-in/` (from claude, with chatgpt's measurement builder) |
| Native iOS app | iPhone Mirroring on the Mac; values are sampled from window screenshots | `capture/native/` |

`vars.mjs`, `layout.mjs`, `icons.mjs` and `quantize.py` serve both web routes.
The `build/` scripts serve every route.

## Generic: use as they are

| File | Does |
|---|---|
| `capture/quantize.py` | Converts screenshots to sRGB 256-colour PNGs |
| `capture/signed-in/snapshot.js` | Pasted into the signed-in page; copies one state with stylesheets inlined, scripts removed, names redacted, signed URLs cut |
| `capture/signed-in/unsnap.py` | Writes a snapshot to disk; refuses it if a redacted string or a signing parameter survived. Needs `SNAP_REDACT` |
| `capture/signed-in/redact.example.json` | The shape of the redaction file, which lives in `~/.design-systems/<slug>-redact.json` |
| `capture/signed-in/render-all.sh` | Renders every row of `shots.tsv`: a copy taken in dark (`-dark` in its label) in both themes, any other once |
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
| `capture/signed-in/build-measurements.mjs` | The heading and intro of `measurements.md` |
| `capture/vars.mjs` | Which selectors carry the theme, how names are binned, the source string. If stylesheets are cross-origin, swap in manus's CDN-chunk reader or gauth's network-response reader |
| `capture/layout.mjs` | The product block naming the shell's regions; keep the generic part (widths, grids, fixed bars, dialogs, menus) |
| `capture/icons.mjs` | Ships the inline-SVG strategy. For an icon font use `systems/claude/tools/capture/icons.mjs`; for SVG sprites, `systems/chatgpt/tools/capture/icons.mjs`. Fill `icon-names.tsv` |
| `capture/public/*.mjs` | `BASE`, `PAGES`, the promo and dialog dismissers, `M()`, and the two prose blocks in `build-measurements.mjs` |
| `build/build_tokens.py` | The header constants and the whole mapping from readings to `core`, `light` and `dark`; keep the helpers, build and checks |
| `build/build_components_md.py` (signed-in) or `build_components_md.public.py` (public) | `PREFER`, `ORDER_GROUPS`, group and page descriptions, the intro and the Gaps section. The two read different measurement files, so use the one that matches the route |
| `build/style-guide.template.html` | The theme attribute (`data-mode` or a `.dark` class), the token group names, and the whole Components section |
| `build/build_style_guide.py` | Usually nothing; it renders a light-only package too, and the template then starts in light with the theme toggle hidden |

## Never commit

Account names, conversation or file titles, task and project ids, raw page
copies, redaction files and proprietary fonts. Specs find elements by role,
label or position, so a kit copy holds no account text at all.

## Known gaps in the kit

- The signed-in and public measuring engines differ (the public one can force
  `pressed` and `filled` states through CDP). Merging them is open.
- The oklab and lab to sRGB conversion is repeated in `vars.mjs`,
  `build-measurements.mjs`, `build_tokens.py` and `build_components_md.py`.
- `build_tokens.py` still mixes generic helpers and the product mapping in one
  file; the mapping region is the part to rewrite.
