# ResearchRabbit design reference

ResearchRabbit is a literature tool built around an interactive citation
graph: a search returns papers as a list beside a map of how they cite each
other. It was read on 2026-10-04, signed in, as the model for the `/learn`
map of concepts. The graph is the point of this reference, and
[graph.md](graph.md) is the document to read first: layout, drawing,
interaction and motion, with every value traced to the app or its code, and a
comparison with the `/learn` map as it is built today.

Pages read on 2026-10-04: Home, a search's results in split, list and map views
(hover on a node, a list card and each legend chip; a selected node with its
detail panel; zoomed in; every tab of the layout settings; the keyword filter),
and a library collection in list and map views (hover, a dragged node with the
"Positions moved" pill and its Reset menu).

Refreshed on 2026-10-17 against the library's scorecard, same free account,
light theme (the only one), 1440 x 900 and 390 x 844: the workspace and
account menus; Account Settings (Profile, Preferences, an empty Subscription
tab), the Update profile dialog stacked on it, and the Delete Account
confirmation, opened and cancelled; a keyword search with its results, the
next page loading, the "Updating search..." dialog, one article selected, and
the Search Settings drawer open with its select open and a filter checked; the
library's All Articles list, table view, one article selected, an article's
empty Notes tab, and the empty Reading List; the Search start page; and the
Screen too small notice at phone width. [patterns.md](patterns.md) is new and
writes up the patterns those screens show.

| File | What it is |
|---|---|
| [graph.md](graph.md) | How the graph is laid out, drawn and driven, what each pointer and key does, the motion table, and what the `/learn` map can take from it |
| [patterns.md](patterns.md) | The app shell, forms, empty and loading states, the destructive confirmation, feedback, search and filtering, data display and onboarding, as the product does them |
| [style-guide.html](style-guide.html) | One self-contained page rendering every token and the chrome components, with a live canvas graph that reproduces the engine's grammar on sample learning topics, written to be ported |
| [tokens.json](tokens.json) | W3C DTCG tokens in Tokens Studio's multi-set layout (`core`, `light`, `$themes`): the palette, type, spacing, radius, border widths, sizes (controls, icons, focus ring, dialog and menu widths), the 640px breakpoint, z-index, motion, the semantic colour roles (backgrounds, text, borders, actions, status) and elevation, plus a `graph` group with the engine's node, edge, label, interaction, motion and layout constants. Every token carries `$extensions.source` |
| [components.md](components.md) | Every page and component with crops and measured values (each colour, shadow and radius named by its token), the shared values, the icon index, and the gaps |
| [components/crops/](components/crops) | Element screenshots, `{component}-{state}.png`, at 2x |
| [icons/](icons) | SVGs lifted from the pages, plus the graph's own canvas glyphs (`graph-*.svg`), named in [icons/INDEX.tsv](icons/INDEX.tsv). ResearchRabbit's property, kept for reference only |
| [screenshots/](screenshots) | `{page}-light-{state}.png`, 2880 x 1800 renders (1440 x 900 at 2x) of each captured state; the two `library-mobile` ones are 390 x 844 at 2x |
| [raw/](raw) | The unprocessed readings: [graph-code-notes.md](raw/graph-code-notes.md) (the engine, read from the production bundle, with identifiers and byte offsets), [css-vars.json](raw/css-vars.json) (the `:root` properties, every styled-component's rules, the rules on bare elements, the @media conditions and keyframes), [components-computed.json](raw/components-computed.json) (computed styles per component and state, with the date each page was read) |
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
The workspace, account and collection names and the email were redacted
before a copy left the browser ("My workspace", "Researcher", "my-collection",
"Email hidden"). The redaction file lives in
`~/.design-systems/researchrabbit-redact.json`, never in the repository. The
2026-10-04 snapshots were deleted in the library's 2026-10-11 cleanup; the
2026-10-17 ones are gzipped in `~/.design-systems/snaps/researchrabbit/`.

The refresh read the new snapshots into the same files without discarding the
older readings: [vars.py](tools/capture/vars.py) merges each capture into
`raw/css-vars.json`, and [measure.mjs](tools/capture/measure.mjs) merges by
page, so `components-computed.json` holds the 2026-10-04 states as they were
read and adds the 2026-10-17 ones (each page records its date). The refresh
also measures a pressed state (the mouse held down) and reads each page at
the size it was captured. Loading states last a fraction of a second, so the
spinner and the loading dialog were copied by a script the moment they
mounted, before any screenshot.

Two traps cost time. The built-in browser delivers a hover to the page only
with its next action, so each state was followed by a throwaway screenshot
before the snapshot, or the canvas showed the state before. And the engine
animates only while the page paints, so the entrance animation could not be
sampled frame by frame; its timing comes from the code, and one mid-entrance
frame was seen live (nodes as dots growing into circles).

Actions taken in the app on 2026-10-04: one "Similar articles" search from the
existing collection, hovers, clicks on nodes (which open a detail panel), the
layout settings tabs (opened, not changed), a keyword filter typed and
cleared, the view toggle, toolbar zoom and recenter, and one node drag in the
library map, reset afterwards. On 2026-10-17: one keyword search ("citation
graph") and two pages of its results; the menus and Account Settings opened;
Update profile and Delete Account opened and cancelled with nothing typed; an
article selected and cleared in search and in the library; Open Access
checked and unchecked; a select opened and closed; the library view switched
to the table and back to the list. Nothing was saved, shared, exported or
deleted, and no account field was changed.

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

Every text line read computes to a line height of 1.5 times its size (14/21,
16/24, 24/36, 32/48), the html default; only bare spans drop to 1em. The
element defaults give the heading scale: h1 32px 600, h2 28px, h3 24px (also
the dialog title), h4 16px 500, h5 14px 600, and labels 14px 500. There is no
code or monospace text anywhere in the captured pages; Tailwind's default
`--font-mono` stack is declared but nothing uses it, so `core.typography` has
no code role.

## Foundations at a glance

| Group | What the tokens hold | Where it came from |
|---|---|---|
| Colour ramps | `core.palette`: a nine-step grey, three to four steps of turquoise, green, lavender and peach, three of the selection blue, nine collection colours, the status trios, and the alphas the rules use | The 80 `:root` properties; the product defines no longer ramps |
| Backgrounds | `light.background`: page (body), surface, raised (dialogs), overlay (menus), scrim, plus the glass panel, section and hint fills | Rules on `body`, `Modal__Content`, `Dropdown__Content`, `Modal__Overlay` |
| Text | primary, secondary, tertiary, disabled, inverse, on-accent, link, link-hover | Rules and the computed link colour |
| Borders | default, strong, rule, field, line, focus, drawer; widths in `core.borderWidth` (1px everywhere, a 2px select ring, a 4px slider ring) | Rules |
| Actions | primary black with hover and pressed `#333333`, the lavender accent, quiet fills, the focus ring colour, the peach danger fill | Rules and computed pressed states |
| Status | success, warning, danger and info, each with fill, text and border | The `--activity-*` properties, the typed-phrase box and the notice banner |
| Sizing | controls 24, 32, 40 and 56px, the 37px field, icons 14, 16, 18 and 24px, a 1px focus ring at offset 0 | Rules and computed heights |
| Elevation | `light.elevation`: menu, popup (popovers, tooltips) and dialog shadows; the declared `--shadow-s/m/l` are unused | Rules |
| Motion | 150 to 500ms transitions, 400ms dialog and popover entrances on `cubic-bezier(0.16, 1, 0.3, 1)`, a 1.1s spinner | Rules |
| Layout | the 640px Screen too small breakpoint, 1400px home column, 650px Account Settings, 500 to 800px dialogs, 220 to 500px menus, 290 to 390px right panel, z-index 1 to 3 | Rules and `@media` |

**Reduced motion.** No captured stylesheet has a `prefers-reduced-motion` rule
(the `@media` list is in [raw/css-vars.json](raw/css-vars.json)), so nothing
changes when a visitor asks for less motion: dialogs still slide in over
400ms, the spinner still turns and the graph still animates its entrance.

**Breakpoints and grid.** The app's one breakpoint is `max-width: 640px`,
where every page is covered by the Screen too small notice. Tailwind's
`.container` steps (40, 48, 64, 80, 96rem) are declared in the CSS but no
captured element uses them. Layouts are flex rows, not a column grid: the
home page puts three equal cards in a 1400px row, and search pages split a
main card from the 290 to 390px right panel.

## What to distrust

- **Two capture dates.** The search, graph and library-collection entries are
  from 2026-10-04 and the dialogs, menus, forms, table, empty and loading
  states from 2026-10-17. The `:root` properties were identical on both dates,
  so the palette is the same, but a component read only on the first date
  may have changed since.
- **Pressed is the hover fill.** No captured rule styles `:active`, so the
  pressed tokens repeat the hover colours. A pressed state was read only on
  the 2026-10-17 pages.
- **Status roles are a mapping.** The `--activity-*` colours are measured;
  which one is a fill, a text or a border colour is this package's reading of
  where the product uses them. No captured status surface draws a border.
- **The danger button was seen only disabled**, at the opacity a disabled
  button gets, so its enabled fill and text are not captured.
- **Six colours are still screenshot samples** (the corner glows, the
  drawer's idle Search button, the search summary's white half, the card
  rule); their tokens say so.
- **The graph is a canvas.** Its values come from the production bundle, not
  from styles; see [graph.md](graph.md).

## Coverage

Against the checklist in the library's `docs/DESIGN-SYSTEM.md`. Captured rows
name the file that shows them; the rest say why not.

| Item | Status | Where, or why not |
|---|---|---|
| Colour ramps | Captured, short | `core.palette`; the product's own ramps stop at three to four steps per hue (nine for grey), and no longer ramp exists to read |
| Background roles | Captured | `light.background` page, surface, raised, overlay, scrim |
| Text roles | Captured | `light.text` primary, secondary, disabled, on-accent, link |
| Border roles | Captured | `light.border` default, strong, focus |
| Accent states | Captured | `light.action.primary`, `primary-hover`, `primary-pressed` |
| Status colours | Captured | `light.status` success, warning, danger, info with fill, text, border |
| Theme parity | Not present | One light theme; no dark theme exists |
| Type | Captured, no code role | `core.typography` (19 roles, 8 sizes, line heights measured); the product sets no code text |
| Spacing | Captured | `core.spacing`, a 4px step |
| Shape | Captured | `core.radius`, `core.borderWidth` |
| Sizing | Captured | `core.size` control-sm to control-xl, icon sizes, focus-ring-width and offset |
| Elevation | Captured | `light.elevation` menu, popup, dialog |
| Motion | Captured | `core.duration`, `core.easing`; reduced motion: nothing changes (above) |
| Layout | Captured | `core.breakpoint`, `core.size` widths, `core.zIndex`; no column grid (above) |
| Button | Captured | [components.md](components.md#primary-button): primary, secondary, danger, disabled, text |
| Icon button | Captured | [dialog close](components.md#dialog-close-button), [graph toolbar](components.md#graph-toolbar-button) |
| Link | Captured | [Find out how it works](components.md#find-out-how-it-works-link), [Clear](components.md#clear-link) |
| Text field | Captured | [text field](components.md#text-field), [home search field](components.md#home-search-field), [drawer inputs](components.md#drawer-inputs) |
| Text area | Captured as a rich-text box | [note composer](components.md#note-composer), a contenteditable box; there is no `<textarea>` |
| Select | Captured | [select in the drawer](components.md#select-in-the-drawer), [layout select](components.md#layout-select) |
| Checkbox | Captured | [checkbox](components.md#checkbox), light and dark, unchecked and checked |
| Radio | Not present | Single choices are [pills](components.md#single-choice-pills), not radio buttons |
| Switch | Not present | On and off options are [checkbox-like toggles](components.md#layout-toggle) |
| Tabs | Captured | [vertical tab](components.md#vertical-tab), [layout tab](components.md#layout-tab), [filter pills](components.md#filter-toggle-pills) |
| Menu | Captured | [menu](components.md#menu), [account menu](components.md#account-menu) |
| Tooltip | Captured | [legend tooltip](components.md#legend-tooltip) |
| Dialog | Captured | [dialog](components.md#dialog), [scrim](components.md#dialog-scrim), [destructive confirmation](components.md#destructive-confirmation) |
| Toast | Not captured | The toast container is mounted empty; no action taken raised a toast |
| Card | Captured | [result card](components.md#result-card), [home section card](components.md#home-section-card) |
| List row | Captured | [library list row](components.md#library-list-row), [recent search row](components.md#recent-search-row) |
| Table | Captured | [article table](components.md#article-table), [header cell](components.md#table-header-cell), [row](components.md#table-row) |
| Avatar | Captured | [avatar](components.md#avatar), the placeholder glyph; no photo is set |
| Badge | Captured | [Upgrade badge](components.md#upgrade-badge), [count badge](components.md#library-list-row) |
| States | Captured except error | hover, focus-visible, pressed, selected, disabled, loading in [components.md](components.md); no error state was reached |
| App shell | Captured | [patterns.md](patterns.md#app-shell-and-navigation) |
| Form with a validation error | Not captured | The only forms edit the account; they were not emptied or submitted ([patterns.md](patterns.md#forms-and-validation)) |
| Empty, loading, error | Empty and loading captured; error not captured | [patterns.md](patterns.md#empty-loading-and-error-states); nothing failed during the capture |
| Destructive confirmation | Captured | [patterns.md](patterns.md#destructive-confirmation) |
| Feedback after an action | Captured inline; toast not captured | [patterns.md](patterns.md#feedback-after-an-action) |
| Search and filtering | Captured | [patterns.md](patterns.md#search-and-filtering) |
| List or table | Captured | [patterns.md](patterns.md#data-display) |
| Onboarding | Not captured | The account is not new and Reset Tutorials is disabled ([patterns.md](patterns.md#onboarding-and-first-run)) |
| Light and dark | Light only | The product has no dark theme |
| Desktop and phone widths | Captured | 1440 x 900 throughout; 390 x 844 shows the Screen too small notice, the product's only phone state |

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

`measure.mjs` takes about two minutes for the 2026-10-17 pages and reads the
snapshots from `$RR_SNAPSHOTS` (default `~/.design-systems/snaps/researchrabbit`);
pass page keys to run only those pages, and `--only` to run only some
components. The 2026-10-04 pages need their snapshots back before they can be
measured again. `icons.mjs` lifts the
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
