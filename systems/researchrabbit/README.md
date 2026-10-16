# ResearchRabbit design reference

ResearchRabbit is a literature tool built around an interactive citation
graph: a search returns papers as a list beside a map of how they cite each
other. It was read on 2026-10-04, signed in, as the model for the `/learn`
map of concepts. The graph is the point of this reference, and
[graph.md](graph.md) is the document to read first: layout, drawing,
interaction and motion, with every value traced to the app or its code, and a
comparison with the `/learn` map as it is built today.

Pages read: Home, a search's results in split, list and map views (hover on a
node, a list card and each legend chip; a selected node with its detail
panel; zoomed in; every tab of the layout settings; the keyword filter), and a
library collection in list and map views (hover, a dragged node with the
"Positions moved" pill and its Reset menu).

| File | What it is |
|---|---|
| [graph.md](graph.md) | How the graph is laid out, drawn and driven, what each pointer and key does, the motion table, and what the `/learn` map can take from it |
| [style-guide.html](style-guide.html) | One self-contained page rendering every token and the chrome components, with a live canvas graph that reproduces the engine's grammar on sample learning topics, written to be ported |
| [tokens.json](tokens.json) | W3C DTCG tokens in Tokens Studio's multi-set layout (`core`, `light`, `$themes`), including a `graph` group with the engine's node, edge, label, interaction, motion and layout constants. Every token carries `$extensions.source` |
| [components.md](components.md) | Every page and component with crops and measured values, the shared values, the icon index, and the gaps |
| [components/crops/](components/crops) | Element screenshots, `{component}-{state}.png`, at 2x |
| [icons/](icons) | SVGs lifted from the pages, plus the graph's own canvas glyphs (`graph-*.svg`), named in [icons/INDEX.tsv](icons/INDEX.tsv). ResearchRabbit's property, kept for reference only |
| [screenshots/](screenshots) | `{page}-light-{state}.png`, 2880 x 1800 renders (1440 x 900 at 2x) of each captured state |
| [raw/](raw) | The unprocessed readings: [graph-code-notes.md](raw/graph-code-notes.md) (the engine, read from the production bundle, with identifiers and byte offsets), [css-vars.json](raw/css-vars.json) (the `:root` properties and every styled-component's rules), [components-computed.json](raw/components-computed.json) (computed styles per component and state) |
| [tools/](tools) | The builders and the capture kit. See Rebuild |

## How the values were read

ResearchRabbit is a Vite and React app styled with styled-components, so every
element carries a readable `File__Name-sc-hash` class next to its generated
one, and [vars.py](tools/capture/vars.py) maps each display name to its rules.
The palette, spacing and shadows are 80 custom properties on `:root`. There is
no dark theme: no `[data-theme]`, `.dark` or `prefers-color-scheme` rule exists
in the page CSS, though the graph engine carries dark edge colours that no
page uses (kept as `$extensions` in the tokens).

The graph is one `<canvas>` drawn in plain Canvas 2D by Litmaps' engine, with
an input layer on top; there is no DOM for nodes, so its values cannot be
measured from styles. They were read from the production bundle instead, which
the minifier left with readable names (`GraphEngine`, `GraphArticle`,
`GraphEdge`, `GraphLabel`, `DEFAULT_LAYOUT_SETTINGS`). The notes quote only
short formula excerpts; no bundle code is committed.

Screens were captured from the built-in browser at a 1440 x 900 viewport with
[snapshot.js](tools/capture/snapshot.js): a static copy of the DOM with the
CSSOM inlined and the canvas swapped for its own 2x bitmap, so each graph
state is kept exactly as drawn. [unsnap.py](tools/capture/unsnap.py) writes the
copies out and refuses one that still holds a redacted string or a signed URL,
[render.mjs](tools/capture/render.mjs) renders them headless at 2x, and
[store.py](tools/capture/store.py) names them and keeps 256-colour PNGs here.
The workspace name was redacted to "My workspace"; the redaction file lives in
`~/.self-learn/researchrabbit-redact.json`, never in the repository, and the
snapshots themselves are gzipped in `~/.self-learn/researchrabbit-snapshots/`.

Two traps cost time. The built-in browser delivers a hover to the page only
with its next action, so each state was followed by a throwaway screenshot
before the snapshot, or the canvas showed the state before. And the engine
animates only while the page paints, so the entrance animation could not be
sampled frame by frame; its timing comes from the code, and one mid-entrance
frame was seen live (nodes as dots growing into circles).

Actions taken in the app: one "Similar articles" search from the existing
collection, hovers, clicks on nodes (which open a detail panel), the layout
settings tabs (opened, not changed), a keyword filter typed and cleared, the
view toggle, toolbar zoom and recenter, and one node drag in the library map,
reset afterwards. Nothing was saved, shared, exported or deleted.

Screenshots are 256-colour PNGs. Flat colours are exact; read values from the
tokens, not the images.

## Fonts

| Family | Weights | Used for |
|---|---|---|
| Plus Jakarta Sans | 200 to 800 | Everything: the interface and the canvas labels (12px, 600 for emphasis, 600 14px selected) |
| IBM Plex Sans | 300, roman and italic | Requested by the page's font link, but no captured rule names it, so nothing on these pages renders in it |

The italic used for journal names and the list total is Plus Jakarta Sans
italic. Both families are open source on
Google Fonts, which the style guide links.

## Do and don't

1. **Do use black for the current choice and the main action.** The current view button, the current layout tab, Auto-save, Search from Collection, the Collection and Reading List buttons, the home search field and both drawers are black with white text; hover lightens the view button and Search from Collection to `#333333`. Other controls are a light grey or white pill, or bare. See [search-split-light-default](screenshots/search-split-light-default.png), [library-list-light-default](screenshots/library-list-light-default.png) and [inspector-library-row-default](components/crops/inspector-library-row-default.png).
2. **Do keep hue for the user's collections.** The collection colour (here `#f07d59`, one of eight collection colours) fills search-input and saved nodes, folder icons and the collection tile, and at 20% tints the Share, settings and add buttons and the folder chip. The chrome is black, white and pastel washes; green appears only on the Upgrade pill and the 8px evaluation dot in the inspector's author row. See [library-list-light-default](screenshots/library-list-light-default.png), [search-map-light-default](screenshots/search-map-light-default.png) and [inspector-folder-chip-default](components/crops/inspector-folder-chip-default.png).
3. **Do keep blue for what is in focus, and fade the rest.** A hovered card gets a `#a7d4ff` inset line and a `#f0f6ff` tint, a selected node gets a pale blue disc and `#2782F7` 2px edges, and the chosen layout option is `#e9f5fe`; nodes outside the focus drop to a tenth. No other control or surface in the chrome is blue. See [search-split-light-hover-list-card](screenshots/search-split-light-hover-list-card.png), [search-map-light-inspect-node](screenshots/search-map-light-inspect-node.png), [library-map-light-hover](screenshots/library-map-light-hover.png) and [layout-option-chosen](components/crops/layout-option-chosen.png).
4. **Do separate surfaces with fill alone.** White cards sit on the half-white main card, which sits on the pastel ground, and no card or panel has a drop shadow. Only things that float get one: the filter popover, the legend tooltip and the Reset menu. See [home-light-default](screenshots/home-light-default.png), [search-list-light-default](screenshots/search-list-light-default.png) and [search-map-light-filter-popover](screenshots/search-map-light-filter-popover.png).
5. **Do leave the graph's chrome unboxed.** The legend, the axis captions and the five toolbar buttons sit straight on the canvas with no container; legend and captions are 12px, the captions in `#686d79`. A chip or button gains a white or 5% black fill only on hover. See [search-map-light-default](screenshots/search-map-light-default.png), [graph-controls-default](components/crops/graph-controls-default.png) and [graph-legend-item-results-hover](components/crops/graph-legend-item-results-hover.png).
6. **Don't copy the faint focus ring.** Most controls show keyboard focus as a 1px `#b0edf0` outline that barely shows on white or grey, and links fall back to the browser's `#005fcc`. Use one visible 2px ring. See [view-toggle-button-other-focus-visible](components/crops/view-toggle-button-other-focus-visible.png) and [autosave-button-focus-visible](components/crops/autosave-button-focus-visible.png).

## Rebuild

```bash
python3 tools/build_tokens.py
```

```bash
python3 tools/build_style_guide.py
```

```bash
python3 tools/build_components_md.py
```

All three are deterministic: re-running them on this commit reproduces their
files byte for byte. Edit the raw inputs or the builders, never the generated
files.

The capture kit needs a signed-in browser. Paste
[snapshot.js](tools/capture/snapshot.js) into the page, call
`__snap('<label>', REDACT)` for each state, save each result to a file, then:

```bash
python3 tools/capture/unsnap.py <result file> <scratch dir>
```

```bash
PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/render.mjs <scratch dir> <label>
```

```bash
python3 tools/capture/store.py <scratch dir>
```

```bash
python3 tools/capture/vars.py
```

```bash
PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/measure.mjs
```

```bash
RR_BUNDLE=/path/to/prettified-bundle.js PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/icons.mjs
```

`measure.mjs` takes about seven minutes and reads the snapshots from
`$RR_SNAPSHOTS`; `--only` takes component or page keys. `icons.mjs` lifts the
page icons from the same snapshots, and the graph's canvas glyphs from a
prettified copy of the production bundle named by `RR_BUNDLE`, which is never
kept in the repository; without it the graph icons are left as they are.

## ResearchRabbit's surfaces and self-learn's

| ResearchRabbit | Layout | self-learn |
| --- | --- | --- |
| Search results, map view | Full-width graph with legend top right, axis captions bottom left, toolbar bottom right, and a right panel for next search, settings or the selected paper | The `/learn` map |
| Search results, split view | A list of papers beside the graph, hover synced both ways | The `/learn` table beside the map, if they ever share a screen |
| Paper detail panel | Title, authors, collections, abstract, and a black "Dive deeper" bar with Similar, Refs and Cited by | The `/learn` map's side panel with "Start a session" and "Open in workspace" |
| Layout settings | One tab per axis plus size and advanced, each option a card with a sentence on what it is for | An optional axes view of the map |
| Library collection map | Saved papers as plain discs in the collection colour | Concepts filled by mastery bucket |
