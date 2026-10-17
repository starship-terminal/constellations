# What a package contains

A package is one folder under `systems/<slug>/` that describes one product's
visual system well enough to build a screen that matches it. It stands alone:
it holds its own evidence and the tools that rebuild it, and nothing in it
points at a path outside the folder.

## Layout

Every package aims at the same layout, so an agent can open any of them
without learning a new one. `make check` fails when a package lacks one of the
four parts marked required. The rest are standard: the package's
[Health](#health) section names each standard part it lacks, and the root
README's catalog table shows the same gaps beside every package.

| Path | Required | What it is |
|---|---|---|
| `README.md` | yes | The entry file. Read it in full before using anything else. [The README](#the-readme) lists its sections |
| `DESIGN.md` | yes | A generated, read-only copy of the tokens in Google's DESIGN.md format, for tools that read that format. Never edit it by hand; see [DESIGN.md](#designmd) below |
| `tokens.json` | | W3C DTCG tokens in Tokens Studio's multi-set layout: a `core` set of scales, a `light` and usually a `dark` semantic set, and `$themes`. Every token carries `$extensions.source`. [catalog.json](../catalog.json) names the tokens file for each package, so a package that keeps it elsewhere still works |
| `style-guide.html` | yes | One page that renders every token and the main components with the real values, with a theme toggle |
| `components.md` | | The component inventory: one entry per component with crops of the real product and its values as token names, the shared values, and a Gaps section |
| `patterns.md` | | Page-level patterns: how components combine into the product's main screens, with the screenshots that show them |
| `components/` | | `crops/`, element screenshots named `{component}-{state}.png` at 2x |
| `icons/` | | The product's icons as SVG, with an `INDEX.tsv` naming each by role |
| `screenshots/` | | Whole-page captures named `{page}-{theme}-{state}.png` |
| `raw/` | | The unprocessed readings every token traces back to |
| `tools/` | yes | Every script that rebuilds a generated file in the package, and the capture scripts |

A package may add files for what is unusual about its product, such as
researchrabbit's `graph.md`. Every top-level file and folder, standard or
not, gets a row in the README's file table; Health lists any that do not.

## The README

The README is the one file an agent must read, so every package's README has
the same outline, in this order:

| Section | What it holds |
|---|---|
| Title and intro | What the product is, which surfaces were captured, when, from which account, in which themes and widths |
| File table | One row per top-level file and folder, linking it, with what it holds and how many |
| `## Health` | Generated. See [Health](#health) |
| `## How the values were read` | Where every value came from: which stylesheets, which pages, which tools, and what was changed or neutralised before reading |
| `## What to distrust` | Values that look measured but are not, readings that came out wrong, and what the images no longer show |
| `## Fonts` | The families, their licences, and the fallbacks the tokens use |
| `## Coverage` | Which pages and states were captured and which were not |
| `## Do and don't` | Rules for using the style, each linking the screenshot or crop that shows it |
| `## Rebuild` | The commands that regenerate the package's files from its readings |

A section about one product (its surfaces compared with the app it was
captured for, a layout worth calling out) goes after these.

## Health

Each package's README opens with a `## Health` section, right after the file
table. [tools/health.py](../tools/health.py) writes it from the newest
scorecard snapshot in [scorecard/audits/](../scorecard/audits) and the
package's folder, between the `health:start` and `health:end` markers. It
says:

- how many scorecard criteria the package meets, partly meets and misses,
  leaving out the ones a capture cannot meet (C5, V1 and V2);
- every criterion it partly meets or misses, missing first, with the
  reviewer's evidence, which is the to-do list for its next capture;
- when its grades were last reviewed and when it was captured, flagging a
  capture newer than the review as a re-review due;
- the standard parts of the [layout](#layout) it lacks, and any top-level
  entry the file table does not list.

`make grade` rewrites every Health section after it writes a snapshot, and
`make check` fails when one differs from a fresh write, so a README never
shows grades the scorecard has moved past. Never edit the section by hand:
change the package or its grades, then run `make grade`. It never reaches the
package's `DESIGN.md`, which copies README sections by heading and has no
home for this one. The root README's catalog table comes from the same script
and the same data.

## Builders

The packages built in self-learn share three deterministic builders, run
from the package folder with plain `python3`, so a rebuild that changes
nothing proves the outputs still match their inputs:

```bash
cd systems/claude && python3 tools/build_tokens.py && python3 tools/build_style_guide.py && python3 tools/build_components_md.py && git status --short .
```

Duolingo has no `build_tokens.py`: its `tokens.json` came out of the capture
dumps, and `tokens-notes.md` explains how it is organised. Brilliant's icons
sit in `icons/app/` and `icons/public/` with no `INDEX.tsv`.

## Linear and Polaris

These two came from a work project, with their own builders. Linear now
follows the layout: its DTCG tokens are `tokens.json`, its readings (the
public site's included) are in `raw/`, and `components.md` holds its
component inventory; it has no `patterns.md`. Polaris does not yet: its
tokens sit under `tokens/`, its readings under `evidence/`, and it has no
`components.md`. Their Health sections list the gaps. Beyond the layout, this
is what they hold:

| Path | What it is |
|---|---|
| `README.md` | The entry file: scope, evidence labels, colours, type, geometry, components, and the limits of the capture |
| `style-guide.html` | A browsable guide over everything in the package. Polaris's fetches its data, so open it through `make serve` |
| `tokens/` | Linear: the tokens of `tokens.json` again as Tokens Studio (`tokens-studio.json`) and CSS custom properties (`linear.css`). Polaris: Tokens Studio (`*.tokens-studio.json`) and CSS custom properties (`light.css`) |
| `components/` | One SVG redraw per component and state, with `manifest.json` (linear). These are reconstructions, labelled as such |
| `boards/` | SVG sheets of colours, type, geometry, controls, components and icons, for dragging into Figma |
| `screenshots/` | Linear: full-page public captures, `app-2026-10/` renders of the redacted app copies, and `app/` anonymised accessibility snapshots from the first capture. Polaris: the local reference gallery |
| `previews/`, `thumbnails/`, `icons/` | Rendered previews of the boards, page thumbnails, reference icons |
| `raw/` | Linear: the app's readings (`css-vars.json`, `components-computed.json`, `measurements.md`), `pages/<page>-page.txt` and `styles/<page>-styles.json` per public page, plus `coverage.json`, `validation.json`, `capture-manifest.json`, `icon-evidence.json`, `public-navigation.json`, `settings-inventory.json` |
| `evidence/` | Polaris: `token-parity.json`, `provenance.json`, `vector-manifest.json`, findings and verification notes. Polaris also keeps `licenses/` |
| `tools/` | Linear: `build_tokens.py` (`tokens.json` and `tokens/`), `build_library.py` (boards, components) and `build_guide.py` (the style guide, thumbnails, `raw/coverage.json` and `raw/validation.json`); the last two need Pillow and Markdown. Polaris: `build.mjs` with its `package.json` (`cd tools && npm ci --ignore-scripts && npm run build`), `gallery.jsx` (bundled into `assets/gallery.js`) and `build_vectors.py` |
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

1. Capture into `systems/<slug>/` in the [layout](#layout), following
   [CAPTURE.md](CAPTURE.md). Copy the shared kit from
   [tools/kit/](../tools/kit) into the package's `tools/` and adapt the parts
   its README marks.
2. Label every value ([EVIDENCE.md](EVIDENCE.md)) and fill the Gaps section.
3. Run the three builders and open `style-guide.html` in both themes. Write
   the README in the [outline above](#the-readme), with a row in its file
   table for every top-level entry.
4. Add an entry to [catalog.json](../catalog.json). The entry needs `tags` and a `preview`:
   a cover screenshot and the token paths for its swatches (`page`,
   `surface`, `text`, `muted`, `accent`, `border` per theme) and fonts. Copy
   an existing entry, then run `make design-md` and `make check`, which
   resolves every token path, fails on one that does not exist, and fails if
   the package's `DESIGN.md` is missing or stale.
5. Review the package against [scorecard/criteria.json](../scorecard/criteria.json)
   and merge the grades with `python3 tools/grade.py --write --review
   <slug>=<grades.json>`. That writes its Health section and its row in the
   root README's catalog table.
6. Keep anything private out of the folder: account names, chat titles,
   signed URLs, raw DOM copies ([RIGHTS.md](RIGHTS.md)).
