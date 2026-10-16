# What a package contains

A package is one folder under `systems/<slug>/` that describes one product's
visual system well enough to build a screen that matches it. It stands alone:
it holds its own evidence and the tools that rebuild it, and nothing in it
points at a path outside the folder.

Every package, whatever its shape, has the same four things at its top level,
so an agent can open any package without knowing which shape it is:

| Path | What it is |
|---|---|
| `README.md` | The entry file. Read it in full before using anything else |
| `style-guide.html` | One page that renders the tokens and components with the real values |
| `tools/` | Every script that rebuilds a generated file in the package |
| `DESIGN.md` | A generated, read-only copy of the tokens in Google's DESIGN.md format, for tools that read that format. Never edit it by hand; see [DESIGN.md](#designmd) below |

The tokens file is `tokens.json` in the reference shape and under `tokens/` in
the audit shape; [catalog.json](../catalog.json) names it for each package.
`make check` fails if any package is missing one of these.

Below that there are two shapes, because the packages came from two projects.
New packages use the reference shape.

## The reference shape

Used by duolingo, brilliant, notebooklm, coursera, gauth, researchrabbit,
manus, chatgpt, claude and hevy.

| Path | What it is |
|---|---|
| `README.md` | The entry file. A table of the files, how the values were read (where, when, which account, which themes and widths), what to distrust, the fonts, and the rebuild commands |
| `tokens.json` | W3C DTCG tokens in Tokens Studio's multi-set layout: a `core` set (palette, type, spacing, radii, borders, shadows, opacity, motion, breakpoints, layout, z-index), a `light` and usually a `dark` semantic set, and `$themes`. Every token carries `$extensions.source`; a value DTCG cannot hold is listed under the set's `$extensions.notTokenised` |
| `style-guide.html` | One self-contained page, generated from `tokens.json`, that renders every token and the main components with the real values and a theme toggle. Open it straight from disk |
| `components.md` | The component inventory: one entry per component with crops of the real product, the shared values (hover washes, radii, focus ring, motion), the icon index, and a Gaps section saying what was not captured |
| `components/` | `crops/` (element screenshots named `{component}-{state}.png` at 2x). Duolingo also has `core.md` and `product.md` with JSON twins |
| `icons/` | The product's icons as SVG, with an `INDEX.tsv` naming each by role |
| `screenshots/` | Whole-page captures named `{page}-{theme}-{state}.png`, phone widths prefixed or suffixed `mobile`. 2x, stored as sRGB 256-colour PNGs |
| `raw/` | The unprocessed readings every token traces back to: custom properties by selector (`css-vars.json`), per-component computed styles (`components-computed.json`, `measurements.md`), measured values the token builder reads (`component-tokens.json`), page geometry (`layout.json`, `pages.md`) |
| `tools/` | `build_tokens.py`, `build_style_guide.py`, `build_components_md.py`, `style-guide.template.html`, and `capture/` (the scripts the readings came from) |

Some packages add a file for what is unusual about the product:
researchrabbit's `graph.md` (its citation graph, with `raw/graph-tokens.json`),
duolingo's `tokens-notes.md`, `style-guide-notes.md` and `icons.md`.

The three builders are deterministic and run from the package folder with
plain `python3`, so a rebuild that changes nothing proves the outputs still
match their inputs:

```bash
cd systems/claude && python3 tools/build_tokens.py && python3 tools/build_style_guide.py && python3 tools/build_components_md.py && git status --short .
```

The earliest packages differ in small ways. Duolingo has no
`build_tokens.py`: its `tokens.json` came out of the capture dumps, and
`tokens-notes.md` explains how it is organised and how to import it. Its
icons are indexed in `icons.md`. Brilliant's icons sit in `icons/app/` and
`icons/public/` with no `INDEX.tsv`, and NotebookLM has no `icons/` or
`components/` folder, only `components.md`.

## The audit shape

Used by linear and polaris. Same purpose, different files.

| Path | What it is |
|---|---|
| `README.md` | The entry file: scope, evidence labels, colours, type, geometry, components, and the limits of the capture |
| `style-guide.html` | A browsable guide over everything in the package. Polaris's fetches its data, so open it through `make serve` |
| `tokens/` | Tokens as DTCG (`linear.tokens.json`), Tokens Studio (`*.tokens-studio.json`) and CSS custom properties (`linear.css`, `light.css`) |
| `components/` | One SVG redraw per component and state, with `manifest.json` (linear). These are reconstructions, labelled as such |
| `boards/` | SVG sheets of colours, type, geometry, controls, components and icons, for dragging into Figma |
| `screenshots/` | Linear: full-page public captures plus `app/` anonymised accessibility snapshots of the signed-in app (no app images). Polaris: the local reference gallery |
| `previews/`, `thumbnails/`, `icons/` | Rendered previews of the boards, page thumbnails, reference icons |
| `evidence/` | Linear: `pages/<page>-page.txt` and `styles/<page>-styles.json` per public page, plus `coverage.json`, `validation.json`, `capture-manifest.json`, `icon-evidence.json`, `public-navigation.json`, `settings-inventory.json`. Polaris: `token-parity.json`, `provenance.json`, `vector-manifest.json`, findings and verification notes. Polaris also keeps `licenses/` |
| `tools/` | Linear: `build_library.py` (tokens, boards, components) and `build_guide.py` (the style guide, thumbnails, coverage and validation), both needing Pillow and Markdown. Polaris: `build.mjs` with its `package.json` (`cd tools && npm ci --ignore-scripts && npm run build`), `gallery.jsx` (bundled into `assets/gallery.js`) and `build_vectors.py` |
| `assets/` | Polaris: the style guide's bundled script, CSS, font and data |

## DESIGN.md

Each package's `DESIGN.md` follows Google's
[DESIGN.md spec](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md),
version `alpha`, the format Google Stitch, the `impeccable` skill and many
coding agents read. [tools/catalog.py](../tools/catalog.py) writes it from the
package's tokens file and `README.md`; nothing else does, and nobody edits it
by hand. The tokens file stays the source of truth, because DESIGN.md has no
themes, no per-value provenance, and only px, em and rem units.

| DESIGN.md | Comes from |
|---|---|
| `colors.primary`, `neutral`, `surface`, `on-surface`, `on-surface-variant`, `outline` | The catalog's swatches for the first light theme (`accent`, `page`, `surface`, `text`, `muted`, `border`), or the first theme when there is no light one |
| The other `colors` | Every colour token in that theme's semantic set, aliases resolved, named by path with dots as hyphens (`light.text.primary` is `text-primary`). Gradients and shadows are left out |
| `typography` | `core.typography`, one style per composite token. `fontFamily` is the first family of the stack; percentages become unitless line heights and em letter spacing; text case and decoration are dropped |
| `rounded`, `spacing` | `core.radius`, and `core.spacing` or `core.space`, in px, rem or em. A value with no such form (`50%`) is left out |
| `components` | The semantic set's `component` group, where a token's last word names a DESIGN.md property: `bg`, `background`, `face` or `surface` for `backgroundColor`, `text`, `fg` or `foreground` for `textColor`, and `radius`, `padding`, `height`, `width`, `size`. Other words (hover, lip, fill, label) are left out rather than guessed |
| `omitted` | Each of `typography`, `rounded`, `spacing` and `components` that came out empty, with the reason |
| Body | The spec's eight sections in order. Each opens with generated text (the roles and the tokens they came from, the scales, the shadows as CSS), then copies the README's sections whose headings match (Fonts into Typography, What to distrust into Do's and Don'ts), headings pushed down a level |

A package whose tokens do not sit where the defaults look names its own token
path prefixes in its catalog entry under `designMd`, for `colors`,
`typography`, `rounded` or `spacing`. Linear reads `app.` and `semantic.`,
Polaris reads its flat `light.text.text-*-font-size` tokens as type styles,
and Claude reads its density scale's `pad-` and `gap-` steps as spacing.
`make check` fails when a prefix matches nothing.

```bash
make design-md          # rewrite every package's DESIGN.md
make check              # fails if a committed DESIGN.md differs from a fresh generation
make lint-design-md     # Google's linter, pinned, run through npx in a temp directory
```

`make lint-design-md` passes when no file has an error and every warning comes
from one of two rules the export cannot satisfy without inventing data:

| Rule | Why it cannot pass |
|---|---|
| `orphaned-tokens` | It wants every colour referenced by a component. The colours are the product's whole semantic set (text, border, status, chart roles), used across many components, and the tokens file does not record which component uses which. Only packages with component tokens trigger it, since the rule is silent when there are no components |
| `contrast-ratio` | It flags a component whose text and background fall under 4.5:1. These are the product's measured values (Brilliant's disabled 3D button); changing them would misreport the product |

## Adding a package

1. Capture into `systems/<slug>/` in the reference shape, following
   [CAPTURE.md](CAPTURE.md). Copy the shared kit from
   [tools/kit/](../tools/kit) into the package's `tools/` and adapt the parts
   its README marks.
2. Label every value ([EVIDENCE.md](EVIDENCE.md)) and fill the Gaps section.
3. Run the three builders and open `style-guide.html` in both themes.
4. Add an entry to [catalog.json](../catalog.json) and a row to the catalog
   table in [README.md](https://github.com/c-wenlong/design-systems/blob/main/README.md). The entry needs `tags` and a `preview`:
   a cover screenshot and the token paths for its swatches (`page`,
   `surface`, `text`, `muted`, `accent`, `border` per theme) and fonts. Copy
   an existing entry, then run `make design-md` and `make check`, which
   resolves every token path, fails on one that does not exist, and fails if
   the package's `DESIGN.md` is missing or stale.
5. Keep anything private out of the folder: account names, chat titles,
   signed URLs, raw DOM copies ([RIGHTS.md](RIGHTS.md)).
