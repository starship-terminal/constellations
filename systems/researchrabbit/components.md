# ResearchRabbit components

The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Read on 2026-10-04 and again on 2026-10-17 (the dialogs, menus, forms, table, empty, loading and error states, the toast, pressed states, and the tablet and phone widths) from static, redacted snapshots of signed-in pages on app.researchrabbit.ai, rendered in headless Chromium at 1440 x 900 (2x; the narrow pages at 1000 x 800, 800 x 900 and 390 x 844), with computed styles read from the rendered page. The workspace, account and collection names in the snapshots are redacted. Nothing was created, sent or changed; one keyword search was run, an article was selected and cleared, a filter was checked and unchecked, and a citation was copied to the clipboard.

The machine-readable copy is [raw/components-computed.json](raw/components-computed.json) (132 components, 530 states). Custom properties and per-component CSS rules are in [raw/css-vars.json](raw/css-vars.json); how the graph engine draws is in [raw/graph-code-notes.md](raw/graph-code-notes.md).

How to read an entry:

- A component is found by its styled-components display name (`GraphControls__StyledButton`), so `generateVariantComponent__default`, which many unrelated buttons share, is found by text or position instead. The entry's heading is the product's name for the part, and the key in backticks is the key in the JSON.
- A colour, shadow, radius, padding, gap or control height is its value followed by the [tokens.json](tokens.json) token with the same value (`{palette.grey.primary}`, `{elevation.menu}`, `{radius.lg}`, `{spacing.2}`, `{size.control-md}`), when there is one; a colour names the light-set role for what it paints (`{background.surface}` for a fill, `{text.default}` for text, `{border.default}` for a border; these live in the light set) and falls back to the palette token when no role has that value; an entry's own `component.*` token (by name: `component.toast` for the toast, `component.tooltip` for the graph tooltip, `component.menu-separator` for a menu's rule) is named first for its fill, so a token is only chosen by value when the component has none of its own. Collection colours (`palette.ugc.*`) stay palette tokens because the user picks them per collection. Text is written family size/line-height weight, then its colour, for example `Plus Jakarta Sans 14/21 400, #000000 {palette.base.black}`, and is read from the first text node inside the component.
- The state table has one row per element or snapshot state read at rest. A hover, focus-visible or pressed row lists only what changes from the row above it; a state with the same values is named in the row's label, for example "default (same: hover)". Hover is a real mouse hover, focus-visible a real keyboard focus and pressed the mouse held down (2026-10-17 pages only); where a snapshot state could not be reached it says so.
- "Parts" lists the pieces inside the component, with sizes and offsets measured from the component's corner.
- Crops are images of the component read from the rendered snapshot, in [components/crops/](components/crops) (438 files, named `{component}-{state}.png`, at 2x, 256 colours). A crop wider than 1600px was halved. A state that paints the same pixels as its default has no file of its own. Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (the captured theme is light; the product has no dark theme). They are 1440 x 900 at 2x (the two `library-mobile` ones 390 x 844), 256 colours. The graph canvas in every one of them is a bitmap, frozen exactly as captured.

| Surface | URL | Screenshots |
|---|---|---|
| Search, split view. The list of result cards beside the graph, Next Search at the right. Default, a search input node hovered, a result node hovered, a list card hovered (it stays tinted), the two legend chips hovered, and a node inspected. | `/search/<id>/0` | [default](screenshots/search-split-light-default.png), [hover-input](screenshots/search-split-light-hover-input.png), [hover-legend-inputs](screenshots/search-split-light-hover-legend-inputs.png), [hover-legend-results](screenshots/search-split-light-hover-legend-results.png), [hover-list-card](screenshots/search-split-light-hover-list-card.png), [hover-result](screenshots/search-split-light-hover-result.png), [inspect-node](screenshots/search-split-light-inspect-node.png) |
| Search, map view. The graph fills the main card. Default, zoomed in, a node inspected, the four layout settings tabs, and the filter popover. | `/search/<id>/0` | [default](screenshots/search-map-light-default.png), [filter-popover](screenshots/search-map-light-filter-popover.png), [inspect-node](screenshots/search-map-light-inspect-node.png), [settings-advanced](screenshots/search-map-light-settings-advanced.png), [settings-size](screenshots/search-map-light-settings-size.png), [settings-x-axis](screenshots/search-map-light-settings-x-axis.png), [settings-y-axis](screenshots/search-map-light-settings-y-axis.png), [zoomed-in](screenshots/search-map-light-zoomed-in.png) |
| Search, list view. The result cards at full width; on 2026-10-17 a keyword search: results, the next page loading, the updating dialog, one article selected, an article with no citation data (the inline error), and the Search Settings drawer open, with its select open and a checkbox checked. | `/search/<id>/0` | [citation-missing](screenshots/search-list-light-citation-missing.png), [default](screenshots/search-list-light-default.png), [keyword-results](screenshots/search-list-light-keyword-results.png), [loading](screenshots/search-list-light-loading.png), [selected](screenshots/search-list-light-selected.png), [settings-checked](screenshots/search-list-light-settings-checked.png), [settings-drawer](screenshots/search-list-light-settings-drawer.png), [settings-select-open](screenshots/search-list-light-settings-select-open.png), [updating-dialog](screenshots/search-list-light-updating-dialog.png) |
| Search start page (2026-10-17): the search field, the BibTeX drop zone and the recent searches. | `/search` | [recent](screenshots/search-start-light-recent.png) |
| Library, map view of one collection. Default, hovering, after a node was dragged (Positions moved), and the Reset menu open. | `/library/<id>` | [default](screenshots/library-map-light-default.png), [hover](screenshots/library-map-light-hover.png), [positions-moved](screenshots/library-map-light-positions-moved.png), [positions-reset-menu](screenshots/library-map-light-positions-reset-menu.png) |
| Library, list view of one collection, with the sidebar and the collection header. | `/library/<id>` | [default](screenshots/library-list-light-default.png) |
| Home. Hero with the search field, recent articles, collections and guides; on 2026-10-17 again, with a query typed and the workspace and account menus open. | `/` | [account-menu](screenshots/home-light-account-menu.png), [default](screenshots/home-light-default.png), [refresh](screenshots/home-light-refresh.png), [search-typed](screenshots/home-light-search-typed.png), [workspace-menu](screenshots/home-light-workspace-menu.png) |
| Account Settings dialog (2026-10-17), opened from the account menu: Profile, Preferences, an empty Subscription tab, the Update profile dialog stacked on it, and the Delete Account confirmation (cancelled). | `/?account=<tab>` | [delete-confirm](screenshots/account-light-delete-confirm.png), [edit-profile-dialog](screenshots/account-light-edit-profile-dialog.png), [preferences](screenshots/account-light-preferences.png), [profile](screenshots/account-light-profile.png), [subscription-empty](screenshots/account-light-subscription-empty.png) |
| Library, All Articles (2026-10-17): the list, one article selected, an article's empty Notes tab, the Cite Article dialog, and the toast after copying a citation. | `/library` | [cite-dialog](screenshots/library-all-light-cite-dialog.png), [default](screenshots/library-all-light-default.png), [notes-empty](screenshots/library-all-light-notes-empty.png), [selected](screenshots/library-all-light-selected.png), [toast](screenshots/library-all-light-toast.png) |
| Library, All Articles in the table view (2026-10-17). | `/library` | [default](screenshots/library-table-light-default.png) |
| Library, the empty Reading List (2026-10-17). | `/library/reading` | [empty](screenshots/library-reading-light-empty.png) |
| Search list view at 1000 x 800 (2026-10-17), an article inspected: the right panel shrinks toward its 290px minimum (314.67px here) and the list narrows. | `/search/<id>/0` | [inspect](screenshots/search-tablet-light-inspect.png) |
| Home at 800 x 900 (2026-10-17): below 896px the three cards stack in one column. | `/` | [stacked](screenshots/home-narrow-light-stacked.png) |
| Library at 390 x 844 (2026-10-17): the Screen too small notice, and the clipped desktop layout after Continue anyway. | `/library` | [continue](screenshots/library-mobile-light-continue.png), [screen-too-small](screenshots/library-mobile-light-screen-too-small.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Legend tooltip | search split view | pointer over a legend chip when the snapshot was taken | [search-split-light-hover-legend-inputs](screenshots/search-split-light-hover-legend-inputs.png), [search-split-light-hover-legend-results](screenshots/search-split-light-hover-legend-results.png), [graph-tooltip](#legend-tooltip) |
| Node hover title | search split view | pointer over a node; the white title box is drawn on the canvas, so it is only in the crop | [search-split-light-hover-result](screenshots/search-split-light-hover-result.png), [search-split-light-hover-input](screenshots/search-split-light-hover-input.png) |
| Tinted list card | search split view | pointer over a card when the snapshot was taken; its node is highlighted in the graph | [search-split-light-hover-list-card](screenshots/search-split-light-hover-list-card.png), [result card](#result-card) |
| Article detail panel | search split and map views | a node clicked | [search-split-light-inspect-node](screenshots/search-split-light-inspect-node.png), [search-map-light-inspect-node](screenshots/search-map-light-inspect-node.png), [article detail panel](#article-detail-panel) |
| Layout settings, four tabs | search map view | the settings button in the graph toolbar, then each tab | [x-axis](screenshots/search-map-light-settings-x-axis.png), [y-axis](screenshots/search-map-light-settings-y-axis.png), [size](screenshots/search-map-light-settings-size.png), [advanced](screenshots/search-map-light-settings-advanced.png), [layout settings panel](#layout-settings-panel) |
| Filter popover | search map view | the filter button | [search-map-light-filter-popover](screenshots/search-map-light-filter-popover.png), [filter popover](#filter-popover) |
| Positions moved and Reset menu | library map view | a node dragged, then the pill pressed | [library-map-light-positions-moved](screenshots/library-map-light-positions-moved.png), [library-map-light-positions-reset-menu](screenshots/library-map-light-positions-reset-menu.png), [positions moved pill](#positions-moved-pill) |
| Zoomed graph | search map view | scroll or zoom button; the canvas is redrawn at a larger scale | [search-map-light-zoomed-in](screenshots/search-map-light-zoomed-in.png) |
| Workspace and account menus | home page | the top-bar buttons, one item under the pointer | [home-light-workspace-menu](screenshots/home-light-workspace-menu.png), [home-light-account-menu](screenshots/home-light-account-menu.png), [menu](#menu), [account menu](#account-menu) |
| Dialogs, stacked | Account Settings | account menu, then Preferences or Profile, then Update Profile | [account-light-profile](screenshots/account-light-profile.png), [account-light-edit-profile-dialog](screenshots/account-light-edit-profile-dialog.png), [dialog](#dialog) |
| Destructive confirmation | Account Settings, Profile | Delete Account, then Cancel; nothing typed | [account-light-delete-confirm](screenshots/account-light-delete-confirm.png), [destructive confirmation](#destructive-confirmation) |
| Loading | keyword search results | the copy was taken by a script the moment the spinner or loading dialog mounted | [search-list-light-loading](screenshots/search-list-light-loading.png), [search-list-light-updating-dialog](screenshots/search-list-light-updating-dialog.png), [spinner](#spinner) |
| Selected article | keyword search results, All Articles | the selection circle clicked, then Clear | [search-list-light-selected](screenshots/search-list-light-selected.png), [library-all-light-selected](screenshots/library-all-light-selected.png), [selection circle](#selection-circle) |
| Toast | library, All Articles | an article's Cite button, then the citation box clicked (copies to the clipboard); the copy was taken the moment the toast mounted | [library-all-light-cite-dialog](screenshots/library-all-light-cite-dialog.png), [library-all-light-toast](screenshots/library-all-light-toast.png), [toast](#toast) |
| Inline error | keyword search results | an article with no references and no citations inspected; the drawer shows Cannot search | [search-list-light-citation-missing](screenshots/search-list-light-citation-missing.png), [inline error](#inline-error), [incomplete data warning](#incomplete-data-warning) |
| Select list, checked checkbox | Search Settings drawer | the Retractions select opened; Open Access checked, then unchecked | [search-list-light-settings-select-open](screenshots/search-list-light-settings-select-open.png), [search-list-light-settings-checked](screenshots/search-list-light-settings-checked.png) |

## Shared values

Values that apply across entries, from the measurement file. Counts are components whose first state has the value.

**Type.** Two faces are loaded from Google Fonts: IBM Plex Sans, Plus Jakarta Sans. First-state text is set in Plus Jakarta Sans (131 components), monospace (1 components). No measured component renders in IBM Plex Sans, which is requested in a light weight only.

| Type | Components using it |
|---|---|
| Plus Jakarta Sans 14/21 400 | 24: `avatar`, `button-disabled`, `clear-link`, `collection-icon-button`, `confirm-safeguard`, `dialog-scrim` and more |
| Plus Jakarta Sans 14/21 600 | 16: `button-text`, `empty-state-link`, `home-article-row`, `home-guide-card`, `home-search-button`, `inspector-library-row` and more |
| Plus Jakarta Sans 16/24 500 | 14: `account-menu`, `button-danger`, `button-primary`, `button-secondary`, `empty-notes`, `empty-reading` and more |
| Plus Jakarta Sans 14/14 400 | 11: `filter-bar-button`, `inspector`, `inspector-authors`, `inspector-chips`, `inspector-nav`, `layout-select` and more |
| Plus Jakarta Sans 12/12 400 | 8: `collection-share`, `graph-axis-x`, `graph-axis-y`, `graph-canvas`, `graph-legend`, `graph-legend-item` and more |
| Plus Jakarta Sans 14/14 600 | 7: `drawer-search-button`, `home-browse-library`, `layout-panel`, `layout-tab`, `layout-tabs`, `table` and more |
| Plus Jakarta Sans 12/18 400 | 6: `drawer-input`, `filter-toggle`, `inspector-folder-chip`, `list-state-chip`, `quartile-chip`, `segmented` |
| Plus Jakarta Sans 14/14 500 | 6: `button-link`, `drop-zone`, `library-footer-button`, `nav-workspace`, `positions-moved`, `toast` |
| Plus Jakarta Sans 14/21 500 | 5: `filter-go`, `layout-close`, `layout-reset`, `list-pager`, `table-row` |
| Plus Jakarta Sans 16/24 600 | 5: `drawer`, `drawer-head`, `home-columns`, `home-section`, `library-collections-title` |
| Plus Jakarta Sans 18/27 400 | 4: `checkbox`, `graph-control-button`, `inspector-close`, `layout-toggle` |
| Plus Jakarta Sans 24/36 400 | 4: `confirm-destructive`, `dialog`, `dialog-close`, `empty-state` |
| Plus Jakarta Sans 16/24 400 | 3: `filter-button`, `graph-controls`, `view-toggle-button` |
| Plus Jakarta Sans 12/12 600 | 2: `notice`, `paywall-badge` |
| Plus Jakarta Sans 12/18 600 | 2: `collection-search-button`, `inspector-icon-button` |
| Plus Jakarta Sans 14/21 700 | 2: `nav-bar`, `nav-tab` |

**Radii.**

| Radius | Count | Components |
|---|---|---|
| 48px | 31 | `autosave-button`, `collection-icon-button`, `collection-search-button`, `collection-share`, `drawer-input`, `drawer-search-button`, `filter-bar-button` and more |
| 36px | 1 | `inspector-close` |
| 32px 32px 16px 16px | 1 | `drawer` |
| 24px | 2 | `graph-legend-item`, `quartile-chip` |
| 16px | 7 | `confirm-destructive`, `dialog`, `drop-zone`, `empty-notes`, `filter-popover`, `home-guide-card`, `inspector` |
| 16px 16px 0px 0px | 1 | `main-card` |
| 12px | 1 | `next-search` |
| 12px 12px 0px 0px | 1 | `next-search-header` |
| 8px | 24 | `account-menu`, `button-danger`, `button-disabled`, `button-primary`, `button-secondary`, `citation-box`, `collection-header` and more |
| 6px | 3 | `layout-option`, `menu`, `reset-menu` |
| 4px | 14 | `button-link`, `button-text`, `checkbox`, `filter-go`, `graph-axis-x`, `graph-axis-y`, `graph-control-button` and more |
| 3px | 1 | `layout-tab` |
| 0px 8px 8px 0px | 1 | `list-card-side` |
| 100% | 1 | `dialog-close` |
| 50% | 1 | `avatar` |

**Pill shape.** A component is a pill when its radius is at least half its height. 34 are: `autosave-button`, `collection-icon-button`, `collection-search-button`, `collection-share`, `drawer-input`, `drawer-search-button`, `filter-bar-button`, `filter-button`, `filter-toggle`, `graph-legend-item`, `home-browse-library`, `home-search-button`, `home-search-field`, `incomplete-warning`, `inspector-chips`, `inspector-close`, `inspector-icon-button`, `inspector-nav`, `inspector-sticker`, `library-footer-button`, `nav-avatar`, `nav-tab`, `nav-upgrade`, `nav-workspace`, `paywall-badge`, `positions-moved`, `quartile-chip`, `search-summary`, `search-summary-inputs`, `search-summary-type`, `segmented`, `session-bar`, `session-bar-button`, `view-toggle`. 31 of them use `48px` whatever their height (22 to 53px), so `48px` reads as fully round. Cards, panels and menus use `6px` to `16px`; the drawer's top corners are `32px`.

**Shadows.** Every box shadow read on a component, with the token it equals where there is one. 

| Shadow | Where |
|---|---|
| #000000 0px 0px 0px 1px inset (`{elevation.ring-strong}`) | `filter-toggle`, `library-list-row`, `list-card`, `recent-search-row` |
| #000000 0px 0px 0px 2px | `filter-bar-button`, `layout-select`, `select-dark` |
| #c9cdd3 0px 0px 0px 1px inset (`{elevation.ring-field}`) | `button-disabled`, `filter-input`, `text-field` |
| rgba(14, 18, 22, 0.35) 0px 10px 38px -10px, rgba(14, 18, 22, 0.2) 0px 10px 20px -15px (`{elevation.popup}`) | `account-menu`, `filter-popover`, `graph-tooltip` |
| rgba(22, 23, 24, 0.35) 0px 10px 38px -10px, rgba(22, 23, 24, 0.2) 0px 10px 20px -15px (`{elevation.menu}`) | `menu`, `reset-menu`, `select-dark` |
| #a7d4ff 0px 0px 0px 1px inset (`{elevation.ring-highlight}`) | `inspector`, `list-card` |
| rgba(0, 0, 0, 0.5) 3px 3px 12px 0px (`{elevation.dialog}`) | `confirm-destructive`, `dialog` |
| #000000 0px 0px 0px 1px | `home-guide-card` |
| #686d79 0px 0px 0px 1px (`{elevation.ring-composer}`) | `note-composer` |
| #a49edb 0px 0px 0px 4px (`{elevation.slider-thumb}`) | `slider` |
| #a49edb 0px 0px 0px 5px (`{elevation.slider-thumb-active}`) | `slider` |
| #dde0e4 0px 0px 0px 1px inset (`{elevation.ring-field-dark}`) | `drawer-input` |
| rgba(0, 0, 0, 0.3) 3px 3px 12px 0px (`{elevation.toast}`) | `toast` |

**Colours in use.** Background and text colours of the first state of each component, most used first.

| Use | Colour | Components |
|---|---|---|
| text | #000000 `{text.default}` | 108 |
| background | #ffffff `{background.surface}` | 21 |
| text | #ffffff `{text.inverse}` | 14 |
| background | #000000 `{action.primary}` | 7 |
| text | #201d1d `{text.primary}` | 5 |
| background | rgba(0, 0, 0, 0.05) `{action.quiet}` | 4 |
| background | #e8e7f6 `{action.accent-soft}` | 3 |
| background | rgba(240, 125, 89, 0.2) `{component.folder-tint}` | 3 |
| background | rgba(255, 255, 255, 0.5) `{background.panel-glass}` | 3 |
| text | #686d79 `{text.secondary}` | 3 |
| background | #333333 `{action.primary-hover}` | 2 |
| background | #8add8a `{action.upgrade}` | 2 |
| background | #d1ceed `{action.accent}` | 2 |
| background | #eef0f1 `{background.page}` | 2 |
| background | #f2f2f2 `{action.control}` | 2 |
| background | #fcebe5 `{status.danger.fill}` | 2 |
| background | rgba(0, 0, 0, 0.1) `{action.quiet-hover}` | 2 |
| background | #61dce2 `{action.go}` | 1 |
| background | #d7f6f8 `{background.hint}` | 1 |
| background | #e2f6e2 `{status.info.fill}` | 1 |
| background | #e9f5fe `{component.option-selected}` | 1 |
| background | #f2af97 `{action.danger}` | 1 |
| background | #f5c751 `{component.positions-moved}` | 1 |
| background | #fef1c5 `{status.warning.fill}` | 1 |
| background | rgba(221, 204, 255, 0.2) `{background.panel-tint}` | 1 |
| background | rgba(255, 255, 255, 0.3) `{background.drop-zone}` | 1 |
| background | rgba(255, 255, 255, 0.4) `{background.section}` | 1 |
| background | rgba(255, 255, 255, 0.9) `{action.glass-hover}` | 1 |

**Motion.** Transitions in the page's CSS (every styled component's rules, in [raw/css-vars.json](raw/css-vars.json)) and on the measured elements. The CSS defines no transition on a hover or focus colour except the scrollbar thumb; the rest are opacity, transform and width changes on panels, the drawer and overlays.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 150ms | `ease` | opacity, transform | AnimatedContainer__Container, Commander__Container, Commander__CopiedContainer |
| 160ms | `ease-out` | background-color | ScrollContainer__Scrollbar, `list-scrollbar` |
| 200ms | `ease` | opacity, transform | AnimatedContainer__Container, ArticleAuthors__SlideHint |
| 300ms | `ease` | background-color, box-shadow, min-height, opacity, transform | AnimatedContainer__Container, ArticleNotesCreate__StyledRichInput, DashboardFolders__StyledArrowRight, GraphScreenshotFrame__HandlesContainer, GraphScreenshotFrame__ShotFrame, LoadLine__Container and more |
| 350ms | `ease` | opacity, transform | AnimatedContainer__Container |
| 500ms | `ease` | max-height, transform, width | FilterableSearchActions__Chevron, Navigation__AnimatedWidth, `drawer` |

**Focus.** Real keyboard focus was given to every component that could take it. 62 draw an outline ring, in 3 styles: 1px auto #b0edf0 `{action.focus-ring}`, offset 0px on `account-menu`, `autosave-button`, `button-link`, `button-primary`, `button-secondary` and more; 1px auto #005fcc `{border.focus-browser}`, offset 1px on `empty-state-link`, `home-guide-card`, `inspector-title`, `nav-logo`, `nav-tab`; 1px auto #005fcc `{border.focus-browser}`, offset 0px on `note-composer`. 1 change something other than an outline: `slider`. Focus could not be captured on 14 more (not focusable, or focused without matching :focus-visible), left out of the tally: `citation-box`, `drawer-search-button`, `graph-legend-item`, `inspector-authors`, `inspector-nav`, `layout-reset`, `layout-tab`, `library-list-row`, `list-pager`, `recent-search-row`, `selection-bar`, `selection-tick`, `table-header`, `table-row`.

**Hover.** 71 hovered states differ from their rest state in computed style and 60 do not (they change something drawn on the canvas, or nothing). Background changes on hover, most common first:

| From | To | Count |
|---|---|---|
| transparent | rgba(0, 0, 0, 0.05) `{action.quiet}` | 23 |
| #000000 `{action.primary}` | #333333 `{action.primary-hover}` | 6 |
| rgba(0, 0, 0, 0.05) `{action.quiet}` | rgba(0, 0, 0, 0.07) `{action.select-hover}` | 5 |
| transparent | #ffffff `{background.surface}` | 3 |
| rgba(0, 0, 0, 0.05) `{action.quiet}` | rgba(0, 0, 0, 0.08) `{action.quiet-hover-soft}` | 2 |
| rgba(0, 0, 0, 0.05) `{action.quiet}` | rgba(0, 0, 0, 0.1) `{action.quiet-hover}` | 2 |
| transparent | rgba(255, 255, 255, 0.1) `{action.quiet-hover-inverse}` | 2 |
| #8add8a `{action.upgrade}` | #c4eec4 `{action.upgrade-hover}` | 1 |
| #f2f2f2 `{action.control}` | #e8e8e8 `{action.control-hover}` | 1 |
| #ffffff `{background.surface}` | #e9f5fe `{component.option-selected}` | 1 |
| #ffffff `{background.surface}` | #eef0f1 `{background.page}` | 1 |
| #ffffff `{background.surface}` | rgba(255, 255, 255, 0.5) `{background.panel-glass}` | 1 |

**Layout regions.** The page's main regions at the captured size, from the DOM ([raw/components-computed.json](raw/components-computed.json), `pages`). Pages with the same region are listed together.

| Region | x | y | width | height | Background | Radius | Pages |
|---|---|---|---|---|---|---|---|
| DashboardSearch__Container | 322 | 120 | 1042 | 171 | - | - | home and 9 more |
| DashboardSearch__Container | 56 | 120 | 688 | 171 | - | - | home-narrow |
| DashboardSearch__Container | 76 | 169.5 | 1288 | 137 | - | - | search-start |
| ExploreGraph__Container | 24 | 166 | 994 | 726 | - | - | sm and 7 more |
| ExploreGraph__Container | 424 | 166 | 594 | 726 | - | - | sp and 6 more |
| ExploreStep__ListContainer | 24 | 166 | 994 | 726 | - | - | sl and 7 more |
| ExploreStep__ListContainer | 24 | 166 | 400 | 726 | - | - | sp and 6 more |
| ExploreStep__ListContainer | 24 | 166 | 629.33 | 626 | - | - | tablet |
| Graph__Container | 282 | 250 | 1126 | 634 | - | - | lm, lm-hover, lm-moved, lm-reset |
| Graph__Container | 24 | 166 | 994 | 726 | - | - | sm and 7 more |
| Graph__Container | 424 | 166 | 594 | 726 | - | - | sp and 6 more |
| LibraryFolder__Container | 274 | 80 | 1142 | 812 | - | - | lm and 4 more |
| Library__SidebarContainer | 24 | 80 | 250 | 812 | - | - | lm and 11 more |
| Library__SidebarContainer | 0 | 0 | 0 | 0 | - | - | mobile-warn |
| Navigation__Container | 0 | 0 | 800 | 64 | - | - | home-narrow |
| Navigation__Container | 0 | 0 | 0 | 0 | - | - | mobile-warn |
| Navigation__Container | 0 | 0 | 1440 | 64 | - | - | sp and 46 more |
| Navigation__Container | 0 | 0 | 1000 | 64 | - | - | tablet |
| Scaffold__Actions | 1026 | 120 | 390 | 772 | - | - | sp and 23 more |
| Scaffold__Actions | 661.3 | 120 | 314.67 | 672 | - | - | tablet |
| Scaffold__Body | 24 | 80 | 1392 | 812 | - | - | lm and 11 more |
| Scaffold__Body | 0 | 0 | 0 | 0 | - | - | mobile-warn |
| Scaffold__Body | 44 | 80 | 1352 | 812 | - | - | search-start |
| Scaffold__Body | 24 | 166 | 994 | 726 | - | - | sp and 23 more |
| Scaffold__Body | 24 | 166 | 629.33 | 626 | - | - | tablet |
| Scaffold__Header | 24 | 120 | 994 | 46 | #ffffff `{background.surface}` | - | sp and 23 more |
| Scaffold__Header | 24 | 120 | 629.33 | 46 | #ffffff `{background.surface}` | - | tablet |
| Scaffold__Main | 24 | 80 | 1392 | 812 | - | - | lm and 11 more |
| Scaffold__Main | 0 | 0 | 0 | 0 | - | - | mobile-warn |
| Scaffold__Main | 44 | 80 | 1352 | 812 | - | - | search-start |
| Scaffold__Main | 24 | 120 | 994 | 772 | rgba(255, 255, 255, 0.5) `{background.panel-glass}` | 16px 16px 0px 0px | sp and 23 more |
| Scaffold__Main | 24 | 120 | 629.33 | 672 | rgba(255, 255, 255, 0.5) `{background.panel-glass}` | 16px 16px 0px 0px | tablet |

**Surface shapes.** Values from the first state of each; the entries hold the others.

| Surface | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Main card](#main-card) | 994 x 772 | - | 16px 16px 0px 0px | rgba(255, 255, 255, 0.5) `{background.panel-glass}` | none | 0 |
| [Right panel](#right-panel) | 390 x 772 | - | 12px | rgba(221, 204, 255, 0.2) `{background.panel-tint}` | none | 0 |
| [Result card](#result-card) | 372 x 204 | - | 8px `{radius.lg}` | #ffffff `{background.surface}` | none | 0 |
| [Search summary pill](#search-summary-pill) | 248.64 x 37 (height `{size.field}`) | - | 48px `{radius.pill}` | #d1ceed `{action.accent}` | none | 4px `{spacing.1}` |
| [View toggle](#view-toggle) | 96 x 32 (height `{size.control-md}`) | - | - | #000000 `{action.primary}` | none | 0 |
| [Filter popover](#filter-popover) | 356 x 148 | - | 16px `{radius.2xl}` | #ffffff `{background.surface}` | rgba(14, 18, 22, 0.35) 0px 10px 38px -10px, rgba(14, 18, 22, 0.2) 0px 10px 20px -15px (`{elevation.popup}`) | 8px `{spacing.2}` |
| [Legend tooltip](#legend-tooltip) | 162.41 x 28 | - | 8px `{radius.lg}` | #333333 `{action.primary-hover}` | rgba(14, 18, 22, 0.35) 0px 10px 38px -10px, rgba(14, 18, 22, 0.2) 0px 10px 20px -15px (`{elevation.popup}`) | 8px 12px `{spacing.2} {spacing.3}` |
| [Tip banner](#tip-banner) | 374 x 44 | - | 8px `{radius.lg}` | #d7f6f8 `{background.hint}` | none | 0 |
| [Search Settings drawer](#search-settings-drawer) | 390 x 110 | - | 32px 32px 16px 16px | #000000 `{action.primary}` | none | 0 |
| [Article detail panel](#article-detail-panel) | 390 x 772 | - | 16px `{radius.2xl}` | #ffffff `{background.surface}` | #a7d4ff 0px 0px 0px 1px inset (`{elevation.ring-highlight}`) | 0 |
| [Layout option card](#layout-option-card) | 374 x 190 | 1px solid #8a92a1 `{border.line}` | 6px `{radius.md}` | #e9f5fe `{component.option-selected}` | none | 12px `{spacing.3}` |
| [Layout select](#layout-select) | 119.59 x 29 | - | 4px `{radius.sm}` | rgba(0, 0, 0, 0.05) `{action.quiet}` | none | 4px 8px `{spacing.1} {spacing.2}` |
| [Positions moved pill](#positions-moved-pill) | 150.33 x 24 (height `{size.control-sm}`) | - | 48px `{radius.pill}` | #f5c751 `{component.positions-moved}` | none | 4px 8px `{spacing.1} {spacing.2}` |
| [Reset positions menu](#reset-positions-menu) | 220 x 38 | - | 6px `{radius.md}` | #ffffff `{background.surface}` | rgba(22, 23, 24, 0.35) 0px 10px 38px -10px, rgba(22, 23, 24, 0.2) 0px 10px 20px -15px (`{elevation.menu}`) | 4px `{spacing.1}` |
| [Library sidebar](#library-sidebar) | 250 x 812 | - | 8px | #ffffff `{background.surface}` | none | 0px 16px 0px 0px `{spacing.0} {spacing.4} {spacing.0} {spacing.0}` |
| [Collection header](#collection-header) | 1142 x 92 | - | 8px `{radius.lg}` | #ffffff `{background.surface}` | none | 0 |
| [Home section card](#home-section-card) | 440 x 500 | - | 8px `{radius.lg}` | rgba(255, 255, 255, 0.4) `{background.section}` | none | 12px `{spacing.3}` |
| [Guide card](#guide-card) | 416 x 275 | - | 16px `{radius.2xl}` | #ffffff `{background.surface}` | none | 0 |

## Components

### Shell and navigation

The frame shared by every signed-in page: a pastel gradient ground, a 64px top bar that paints nothing, a half-white main card with a solid white header strip, and a 390px right panel. Search pages add a translucent grey session bar under the top bar.

#### Page ground
The pastel ground behind every signed-in page: a transparent full-page container holding three 1080px radial gradients (lavender fading through turquoise, lavender, peach), each anchored to a different corner. The colour under them is the body background. Read as `page-ground` on the search split view, home page.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 1440 x 900; background transparent; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}` |
| home (same as the first row) | same values |

Child layers that carry the look: div 1080x1080; div 1080x1080; div 1080x1080.

Parts:

- body: 1440 x 900; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; background #eef0f1 `{background.page}`; text "Search Library Upgrade My work"
- blobs 1: 1080 x 1080; padding 0px 0px 1080px; image radial-gradient(farthest-side at 100% 0%, #e8e7f6 `{gradient.glow-left}`, rgba(215, 246, 248, 0.5), transparen
- blobs 2: 1080 x 1080; padding 0px 0px 1080px; image radial-gradient(farthest-side at 0% 100%, #e8e7f6 `{gradient.glow-left}`, transparent)
- blobs 3: 1080 x 1080; padding 0px 0px 1080px; image radial-gradient(farthest-side at 100% 100%, #fcebe5 `{gradient.glow-bottom-right}`, transparent)

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Top bar
The 64px bar over every signed-in page: wordmark at the left, Search and Library tabs, then the Upgrade pill, the workspace menu and the account button at the right. It paints nothing of its own; the page gradient shows through. Read as `nav-bar` on the search split view, library map view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 1440 x 64; padding 16px 24px 0px 24px `{spacing.4} {spacing.6} {spacing.0} {spacing.6}`; gap 16px `{spacing.4}`; background transparent; text Plus Jakarta Sans 14/21 700, #000000 `{text.default}`; icon 48 x 48, #000000 `{text.default}` |
| library (same as the first row) | same values |

Child layers that carry the look: a 71.8x37 background #ffffff `{background.surface}` radius 48px; button 83.6x29 background #8add8a `{action.upgrade}` radius 48px; button 137x32 background rgba(255, 255, 255, 0.5) `{background.panel-glass}` radius 48px.

Parts:

- container: 1440 x 64; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; padding 16px 24px 0px `{spacing.4} {spacing.6} {spacing.0}`; gap 16px `{spacing.4}`; text "Search Library Upgrade My work"
  - child a: 208 x 48; at 24, 16; Plus Jakarta Sans 14/21 600, #000000 `{text.default}`
  - child svg: 48 x 48; at 24, 12
  - child svg: 208 x 42; at 24, 16
  - child Search: 71.77 x 37; at 248, 21.5; Plus Jakarta Sans 14/21 700, #000000 `{text.default}`; background #ffffff `{background.surface}`; radius 48px `{radius.pill}`; padding 8px 12px `{spacing.2} {spacing.3}`; text "Search"
  - child Library: 71.33 x 37; at 335.8, 21.5; Plus Jakarta Sans 14/21 700, #000000 `{text.default}`; radius 48px `{radius.pill}`; padding 8px 12px `{spacing.2} {spacing.3}`; text "Library"
  - child Upgrade: 83.64 x 29; at 1147.4, 25.5; Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; background #8add8a `{action.upgrade}`; radius 48px `{radius.pill}`; padding 4px 12px `{spacing.1} {spacing.3}`; gap 8px `{spacing.2}`; text "Upgrade"
  - child My workspace: 137 x 32; at 1243, 24; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; background rgba(255, 255, 255, 0.5) `{background.panel-glass}`; radius 48px `{radius.pill}`; padding 8px `{spacing.2}`; gap 8px `{spacing.2}`; text "My workspace"
  - child svg: 16 x 16; at 1356, 32
  - child button: 32 x 32; at 1384, 24; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; background rgba(255, 255, 255, 0.5) `{background.panel-glass}`; radius 48px `{radius.pill}`; padding 8px `{spacing.2}`
  - child svg: 16 x 16; at 1392, 32

![Top bar default](components/crops/nav-bar-default.png) ![Top bar library](components/crops/nav-bar-library.png)

#### Wordmark link
ResearchRabbit wordmark. The rabbit mark beside it only shows on the Library and Home pages (the width animates). Read as `nav-logo` on the search split view, library map view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 208 x 48; background transparent; text Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; cursor pointer; icon 48 x 48, #000000 `{text.default}` |
| hover | text Plus Jakarta Sans 14/21 600, #000000 `{text.default}`, underline |
| focus-visible | outline 1px auto #005fcc `{border.focus-browser}`, offset 1px |
| with-mark (as the first row, except) | size 256 x 48 |

Parts:

- wordmark: 208 x 42

Authored state rules (from the page's CSS): `a:hover { text-decoration: underline; }`.

![Wordmark link default](components/crops/nav-logo-default.png) ![Wordmark link focus-visible](components/crops/nav-logo-focus-visible.png) ![Wordmark link with-mark](components/crops/nav-logo-with-mark.png)

#### Search and Library tabs
Two text tabs. The current one sits in a white pill; the other is plain text. Read as `nav-tab` on the search split view, keyword search results (list view).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| current | size 71.77 x 37 (height `{size.field}`); padding 8px 12px `{spacing.2} {spacing.3}`; radius 48px `{radius.pill}`; background #ffffff `{background.surface}`; text Plus Jakarta Sans 14/21 700, #000000 `{text.default}`; cursor pointer |
| current, hover | text Plus Jakarta Sans 14/21 700, #000000 `{text.default}`, underline |
| current, focus-visible | outline 1px auto #005fcc `{border.focus-browser}`, offset 1px |
| current, pressed | text Plus Jakarta Sans 14/21 700, #000000 `{text.default}`, underline |
| other (as the first row, except) | size 71.33 x 37 (height `{size.field}`); background transparent |
| other, hover | text Plus Jakarta Sans 14/21 700, #000000 `{text.default}`, underline |
| other, focus-visible | outline 1px auto #005fcc `{border.focus-browser}`, offset 1px |
| other, pressed | text Plus Jakarta Sans 14/21 700, #000000 `{text.default}`, underline |

Authored state rules (from the page's CSS): `a:hover { text-decoration: underline; }`.

![Search and Library tabs current](components/crops/nav-tab-current.png) ![Search and Library tabs current-hover](components/crops/nav-tab-current-hover.png) ![Search and Library tabs current-focus-visible](components/crops/nav-tab-current-focus-visible.png) ![Search and Library tabs other](components/crops/nav-tab-other.png) ![Search and Library tabs other-hover](components/crops/nav-tab-other-hover.png) ![Search and Library tabs other-focus-visible](components/crops/nav-tab-other-focus-visible.png) ![Search and Library tabs current-pressed](components/crops/nav-tab-current-pressed.png) ![Search and Library tabs other-pressed](components/crops/nav-tab-other-pressed.png)

#### Upgrade pill
Green pill button in the top bar. Read as `nav-upgrade` on the search split view, keyword search results (list view).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 83.64 x 29; padding 4px 12px `{spacing.1} {spacing.3}`; gap 8px `{spacing.2}`; radius 48px `{radius.pill}`; background #8add8a `{action.upgrade}`; text Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; cursor pointer |
| hover | background #c4eec4 `{action.upgrade-hover}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| pressed | background #c4eec4 `{action.upgrade-hover}` |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(0, 0, 0, 0.05); }`; `.x:hover { background-color: var(--green-50); }`.

![Upgrade pill default](components/crops/nav-upgrade-default.png) ![Upgrade pill hover](components/crops/nav-upgrade-hover.png) ![Upgrade pill focus-visible](components/crops/nav-upgrade-focus-visible.png) ![Upgrade pill pressed](components/crops/nav-upgrade-pressed.png)

#### Workspace menu button
Pill with the workspace name (redacted to "My workspace") and a chevron. The menu itself is not in the snapshots. Read as `nav-workspace` on the search split view, home page (workspace menu open), keyword search results (list view).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 137 x 32 (height `{size.control-md}`); padding 8px `{spacing.2}`; gap 8px `{spacing.2}`; radius 48px `{radius.pill}`; background rgba(255, 255, 255, 0.5) `{background.panel-glass}`; text Plus Jakarta Sans 14/14 500, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| hover | background #ffffff `{background.surface}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| pressed | background #ffffff `{background.surface}` |
| open (same as the first row) | same values |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: #ffffff; }`.

![Workspace menu button default](components/crops/nav-workspace-default.png) ![Workspace menu button hover](components/crops/nav-workspace-hover.png) ![Workspace menu button focus-visible](components/crops/nav-workspace-focus-visible.png) ![Workspace menu button pressed](components/crops/nav-workspace-pressed.png) ![Workspace menu button open](components/crops/nav-workspace-open.png)

#### Account button
Round 32px button with a person icon. Read as `nav-avatar` on the search split view, keyword search results (list view).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default (same: hover, pressed) | size 32 x 32 (height `{size.control-md}`); padding 8px `{spacing.2}`; radius 48px `{radius.pill}`; background rgba(255, 255, 255, 0.5) `{background.panel-glass}`; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(255, 255, 255, 0.5); }`.

![Account button default](components/crops/nav-avatar-default.png) ![Account button focus-visible](components/crops/nav-avatar-focus-visible.png) ![Account button pressed](components/crops/nav-avatar-pressed.png)

#### Search session bar
Grey pill under the top bar with close, back, forward and the rabbit trail button. Read as `session-bar` on the search split view.

**Values (default).** size 112 x 40 (height `{size.control-lg}`); padding 4px `{spacing.1}`; radius 48px `{radius.pill}`; background rgba(0, 0, 0, 0.1) `{action.quiet-hover}`; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; icon 16 x 16, #000000 `{text.default}`.

Parts:

- container: 112 x 40; background rgba(0, 0, 0, 0.1) `{action.quiet-hover}`; radius 48px `{radius.pill}`; padding 4px `{spacing.1}`
  - child button: 24 x 32; at 4, 4; Plus Jakarta Sans 20/30 400, #000000 `{text.default}`; radius 48px `{radius.pill}`; padding 4px `{spacing.1}`
  - child button: 24 x 32; at 28, 4; Plus Jakarta Sans 20/30 400, #000000 `{text.default}`; radius 48px `{radius.pill}`; padding 4px `{spacing.1}`; opacity 0.5
  - child button: 24 x 32; at 52, 4; Plus Jakarta Sans 20/30 400, #000000 `{text.default}`; radius 48px `{radius.pill}`; padding 4px `{spacing.1}`; opacity 0.5
  - child button: 32 x 32; at 76, 4; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; radius 48px `{radius.pill}`

![Search session bar default](components/crops/session-bar-default.png)

#### Search session bar button
Close, back and forward buttons in the session bar. Read as `session-bar-button` on the search split view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| close | size 24 x 32 (height `{size.control-md}`); padding 4px `{spacing.1}`; radius 48px `{radius.pill}`; background transparent; text Plus Jakarta Sans 20/30 400, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| close, hover | background rgba(0, 0, 0, 0.1) `{action.quiet-hover}` |
| close, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| back (same: hover) (as the first row, except) | opacity 0.5; cursor none |
| rabbit | size 32 x 32 (height `{size.control-md}`); radius 48px `{radius.pill}`; background transparent; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; cursor pointer; icon 32 x 32, #000000 `{text.default}` |
| rabbit, hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| rabbit, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(0, 0, 0, 0.1); }`.

![Search session bar button close](components/crops/session-bar-button-close.png) ![Search session bar button close-hover](components/crops/session-bar-button-close-hover.png) ![Search session bar button close-focus-visible](components/crops/session-bar-button-close-focus-visible.png) ![Search session bar button back](components/crops/session-bar-button-back.png) ![Search session bar button rabbit](components/crops/session-bar-button-rabbit.png) ![Search session bar button rabbit-hover](components/crops/session-bar-button-rabbit-hover.png) ![Search session bar button rabbit-focus-visible](components/crops/session-bar-button-rabbit-focus-visible.png)

#### Main card
The 50% white card, rounded at the top corners only, that holds a solid white header strip and the list or graph, left of the right-hand panel. Read as `main-card` on the search split view.

**Values (default).** size 994 x 772; radius 16px 16px 0px 0px; background rgba(255, 255, 255, 0.5) `{background.panel-glass}`; text Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; icon 14 x 14, #ffffff `{text.inverse}`.

Parts:

- header: 994 x 46; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; background #ffffff `{background.surface}`; padding 0px 12px `{spacing.0} {spacing.3}`; gap 16px `{spacing.4}`; text "Similar articles to 9 Articles"
- body: 994 x 726; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; text "Jimenez, 2023 SWE-bench: Can L"
- actions: 390 x 772; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; text "Next Search Auto-save to... Se"
- root: 1440 x 836; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; padding 0px 24px 8px `{spacing.0} {spacing.6} {spacing.2}`; gap 8px `{spacing.2}`; text "Similar articles to 9 Articles"
- content: 1392 x 772; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; gap 8px `{spacing.2}`; text "Similar articles to 9 Articles"

![Main card default](components/crops/main-card-default.png)

#### Right panel
The 390px column at the right: Next Search, the article detail or the layout settings take turns in it. Read as `side-panel` on the search split view, search map view (a node inspected), search map view (layout settings, X Axis) and 1 more.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| next-search | size 390 x 772; background transparent; text Plus Jakarta Sans 16/24 500, #000000 `{text.default}`; icon 16 x 16, #ffffff `{text.inverse}` |
| article (as the first row, except) | text Plus Jakarta Sans 14/14 400, #000000 `{text.default}`; icon 16 x 16, #000000 `{text.default}` |
| layout (same as the first row) | same values |
| width-1000 | size 314.67 x 672; background transparent; text Plus Jakarta Sans 14/14 400, #000000 `{text.default}`; icon 16 x 16, #000000 `{text.default}` |

Child layers that carry the look: div 390x772 background rgba(221, 204, 255, 0.2) `{background.panel-tint}` radius 12px; button 126.2x32 background #000000 `{action.primary}` radius 48px; div 374x44 background #d7f6f8 `{background.hint}` radius 8px.

![Right panel next-search](components/crops/side-panel-next-search.png) ![Right panel article](components/crops/side-panel-article.png) ![Right panel layout](components/crops/side-panel-layout.png)

### Search header

The row at the top of the main card: the "Similar articles to 9 Articles" summary capsule at the left, then the filter button and the three-way view toggle at the right.

#### Search summary pill
The search header: "Similar articles" in a light pill, "to", then the black "9 Articles" pill, all inside a lavender capsule. Read as `search-summary` on the search split view.

**Values (default).** size 248.64 x 37 (height `{size.field}`); padding 4px `{spacing.1}`; gap 8px `{spacing.2}`; radius 48px `{radius.pill}`; background #d1ceed `{component.search-summary}`; text Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; cursor pointer; icon 14 x 14, #ffffff `{text.inverse}`.

Parts:

- left: 113.81 x 29; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; background #ffffff `{component.search-summary-label}`; radius 48px `{radius.pill}`; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; text "Similar articles"
- label: 97.81 x 21; Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; text "Similar articles"
- to: 14.33 x 14; Plus Jakarta Sans 14/14 400, #000000 `{text.default}`; text "to"

Authored state rules (from the page's CSS): `.x:hover { opacity: 0.7; }`.

![Search summary pill default](components/crops/search-summary-default.png)

#### Search type pill
The light pill that names the kind of search ("Similar articles"). Read as `search-summary-type` on the search split view.

**Values (default).** size 113.81 x 29; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; radius 48px `{radius.pill}`; background #ffffff `{background.surface}`; text Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; cursor pointer.

![Search type pill default](components/crops/search-summary-type-default.png) ![Search type pill hover](components/crops/search-summary-type-hover.png)

#### Search inputs pill
The black pill that names the inputs ("9 Articles") with the seed icon. Read as `search-summary-inputs` on the search split view.

**Values (default).** size 96.5 x 29; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; radius 48px `{radius.pill}`; background #000000 `{action.primary}`; text Plus Jakarta Sans 14/21 600, #ffffff `{text.inverse}`; cursor pointer; icon 14 x 14, #ffffff `{text.inverse}`.

![Search inputs pill default](components/crops/search-summary-inputs-default.png) ![Search inputs pill hover](components/crops/search-summary-inputs-hover.png)

#### View toggle
Three icon buttons in one capsule: split, list and map. The current one is filled black. Read as `view-toggle` on the search split view, search map view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 96 x 32 (height `{size.control-md}`); radius 48px `{radius.pill}`; background transparent; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; icon 16 x 16, #ffffff `{text.inverse}` |
| map (as the first row, except) | icon 16 x 16, #000000 `{text.default}` |

Child layers that carry the look: button 32x32 background #000000 `{action.primary}`; button 32x32 background rgba(0, 0, 0, 0.05) `{action.quiet}`; button 32x32 background rgba(0, 0, 0, 0.05) `{action.quiet}`.

Parts:

- container: 96 x 32; radius 48px `{radius.pill}`
  - child button: 32 x 32; at 0, 0; Plus Jakarta Sans 16/24 400, #ffffff `{text.inverse}`; background #000000 `{action.primary}`; padding 8px `{spacing.2}`
  - child button: 32 x 32; at 32, 0; Plus Jakarta Sans 16/24 400, #000000 `{text.default}`; background rgba(0, 0, 0, 0.05) `{action.quiet}`; padding 8px `{spacing.2}`
  - child button: 32 x 32; at 64, 0; Plus Jakarta Sans 16/24 400, #000000 `{text.default}`; background rgba(0, 0, 0, 0.05) `{action.quiet}`; padding 8px `{spacing.2}`

![View toggle default](components/crops/view-toggle-default.png) ![View toggle map](components/crops/view-toggle-map.png)

#### View toggle button
One of the three view buttons, current and not current. Read as `view-toggle-button` on the search split view, keyword search results (list view).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| current | size 32 x 32 (height `{size.control-md}`); padding 8px `{spacing.2}`; background #000000 `{action.primary}`; text Plus Jakarta Sans 16/24 400, #ffffff `{text.inverse}`; cursor pointer; icon 16 x 16, #ffffff `{text.inverse}` |
| current, hover | background #333333 `{action.primary-hover}` |
| current, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| current, pressed | background #333333 `{action.primary-hover}` |
| other (as the first row, except) | background rgba(0, 0, 0, 0.05) `{action.quiet}`; text Plus Jakarta Sans 16/24 400, #000000 `{text.default}`; icon 16 x 16, #000000 `{text.default}` |
| other, hover | background rgba(0, 0, 0, 0.1) `{action.quiet-hover}` |
| other, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| other, pressed | background rgba(0, 0, 0, 0.1) `{action.quiet-hover}` |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(0, 0, 0, 0.1); }`; `.x:hover { background-color: #333333; }`.

![View toggle button current](components/crops/view-toggle-button-current.png) ![View toggle button current-hover](components/crops/view-toggle-button-current-hover.png) ![View toggle button current-focus-visible](components/crops/view-toggle-button-current-focus-visible.png) ![View toggle button other](components/crops/view-toggle-button-other.png) ![View toggle button other-hover](components/crops/view-toggle-button-other-hover.png) ![View toggle button other-focus-visible](components/crops/view-toggle-button-other-focus-visible.png) ![View toggle button current-pressed](components/crops/view-toggle-button-current-pressed.png) ![View toggle button other-pressed](components/crops/view-toggle-button-other-pressed.png)

#### Filter button
Round funnel button left of the view toggle; it opens the filter popover. Read as `filter-button` on the search split view, search map view (filter popover open).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default (same: hover) | size 32 x 32 (height `{size.control-md}`); padding 8px `{spacing.2}`; gap 8px `{spacing.2}`; radius 48px `{radius.pill}`; background #eef0f1 `{component.filter-button}`; text Plus Jakarta Sans 16/24 400, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| open (as the first row, except) | outline 1px solid #000000 `{border.strong}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Filter button default](components/crops/filter-button-default.png) ![Filter button focus-visible](components/crops/filter-button-focus-visible.png) ![Filter button open](components/crops/filter-button-open.png)

#### Filter popover
A small card under the filter button: a text field with a Go button and a line of help. Read as `filter-popover` on the search map view (filter popover open).

**Values (default).** size 356 x 148; padding 8px `{spacing.2}`; radius 16px `{radius.2xl}`; background #ffffff `{background.surface}`; shadow rgba(14, 18, 22, 0.35) 0px 10px 38px -10px, rgba(14, 18, 22, 0.2) 0px 10px 20px -15px (`{elevation.popup}`); text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`.

Parts:

- input: 340 x 37; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; radius 8px `{radius.lg}`; padding 8px 32px 8px 12px `{spacing.2} {spacing.8} {spacing.2} {spacing.3}`; shadow #c9cdd3 0px 0px 0px 1px inset (`{elevation.ring-field}`)
- info: 340 x 58; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; background #e8e7f6 `{action.accent-soft}`; radius 8px `{radius.lg}`; padding 8px 12px `{spacing.2} {spacing.3}`; gap 8px `{spacing.2}`; text "Find a broader set of results "

Authored state rules (from the page's CSS): `.x:focus { box-shadow: rgba(14, 18, 22, 0.35) 0px 10px 38px -10px, rgba(14, 18, 22, 0.2) 0px 10px 20px -15px, rgba(0, 0, 0, 0.2) 0px 0px 0px 2px; }`; `.x[data-state="open"][data-side="bottom"] { animation-name: fSMqcH; }`.

![Filter popover default](components/crops/filter-popover-default.png)

#### Filter field
Text input inside the filter popover. Read as `filter-input` on the search map view (filter popover open).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default (same: hover) | size 340 x 37 (height `{size.field}`); padding 8px 32px 8px 12px `{spacing.2} {spacing.8} {spacing.2} {spacing.3}`; radius 8px `{radius.lg}`; background transparent; shadow #c9cdd3 0px 0px 0px 1px inset (`{elevation.ring-field}`); text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; cursor text; placeholder oklab(0 0 0 / 0.5) |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Filter field default](components/crops/filter-input-default.png) ![Filter field focus-visible](components/crops/filter-input-focus-visible.png)

#### Filter Go button
Small button at the right end of the filter field. Read as `filter-go` on the search map view (filter popover open).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default (same: hover) | size 38.59 x 27; padding 3px 9px; radius 4px `{radius.sm}`; background #61dce2 `{action.go}`; text Plus Jakarta Sans 14/21 500, #ffffff `{text.inverse}`; cursor pointer |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Filter Go button default](components/crops/filter-go-default.png)

### Graph

The graph area. Everything drawn on the canvas (nodes, edges, labels, the hover title box) is a bitmap in the snapshots; this group measures the DOM around it: the legend, the axis captions, the toolbar, the Positions moved pill and the legend tooltip. The canvas crops are the only record of node drawing, so read node colours and sizes from graph.md and raw/graph-code-notes.md.

#### Graph canvas region
The graph area of each captured state: the canvas bitmap with its axes captions, legend, toolbar and any hover label drawn on top. The canvas is a bitmap in the snapshots, so these crops are the only record of node, edge and label drawing; read the colours from graph.md and raw/graph-code-notes.md. Read as `graph-canvas` on the search split view, search split view (hovering a search input node), search split view (hovering a result node) and 16 more.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| split-default | size 594 x 726; background transparent; text Plus Jakarta Sans 12/12 400, #686d79 `{text.secondary}`; icon 14 x 14, #8a92a1 `{text.tertiary}` |
| split-hover-input (same as the first row) | same values |
| split-hover-result (same as the first row) | same values |
| split-hover-list-card (same as the first row) | same values |
| split-hover-legend-inputs (same as the first row) | same values |
| split-hover-legend-results (same as the first row) | same values |
| split-inspect-node (same as the first row) | same values |
| map-default (as the first row, except) | size 994 x 726 |
| map-zoomed-in (as the first row, except) | size 994 x 726 |
| map-inspect-node (as the first row, except) | size 994 x 726 |
| map-settings-x-axis (as the first row, except) | size 994 x 726 |
| map-settings-y-axis (as the first row, except) | size 994 x 726 |
| map-settings-size (as the first row, except) | size 994 x 726 |
| map-settings-advanced (as the first row, except) | size 994 x 726 |
| map-filter-popover (as the first row, except) | size 994 x 726 |
| library-default (as the first row, except) | size 1126 x 634 |
| library-hover (as the first row, except) | size 1126 x 634 |
| library-positions-moved | size 1126 x 634; background transparent; text Plus Jakarta Sans 14/14 500, #201d1d `{text.primary}`; icon 16 x 16, #201d1d `{text.primary}` |
| library-positions-reset-menu | size 1126 x 634; background transparent; text Plus Jakarta Sans 14/14 500, #201d1d `{text.primary}`; icon 16 x 16, #201d1d `{text.primary}` |

Child layers that carry the look: div 594x726 radius 6px shadow transparent 0px 0px 0px 1440px; div 1x16 background #8a92a1 `{component.axis-line}`; div 1x32 background #8a92a1 `{component.axis-line}`.

![Graph canvas region split-default](components/crops/graph-canvas-split-default.png) ![Graph canvas region split-hover-input](components/crops/graph-canvas-split-hover-input.png) ![Graph canvas region split-hover-result](components/crops/graph-canvas-split-hover-result.png) ![Graph canvas region split-hover-list-card](components/crops/graph-canvas-split-hover-list-card.png) ![Graph canvas region split-hover-legend-inputs](components/crops/graph-canvas-split-hover-legend-inputs.png) ![Graph canvas region split-hover-legend-results](components/crops/graph-canvas-split-hover-legend-results.png) ![Graph canvas region split-inspect-node](components/crops/graph-canvas-split-inspect-node.png) ![Graph canvas region map-default](components/crops/graph-canvas-map-default.png) ![Graph canvas region map-zoomed-in](components/crops/graph-canvas-map-zoomed-in.png) ![Graph canvas region map-inspect-node](components/crops/graph-canvas-map-inspect-node.png) ![Graph canvas region map-settings-x-axis](components/crops/graph-canvas-map-settings-x-axis.png) ![Graph canvas region map-settings-y-axis](components/crops/graph-canvas-map-settings-y-axis.png) ![Graph canvas region map-settings-size](components/crops/graph-canvas-map-settings-size.png) ![Graph canvas region map-settings-advanced](components/crops/graph-canvas-map-settings-advanced.png) ![Graph canvas region map-filter-popover](components/crops/graph-canvas-map-filter-popover.png) ![Graph canvas region library-default](components/crops/graph-canvas-library-default.png) ![Graph canvas region library-hover](components/crops/graph-canvas-library-hover.png) ![Graph canvas region library-positions-moved](components/crops/graph-canvas-library-positions-moved.png) ![Graph canvas region library-positions-reset-menu](components/crops/graph-canvas-library-positions-reset-menu.png)

#### Graph legend
Three chips at the top right of the graph: References (arrow), Search inputs (seed icon), Results (open circle). Hovering a chip shows a tooltip and highlights those nodes. Read as `graph-legend` on the search split view.

**Values (default).** size 288 x 20; gap 4px `{spacing.1}`; background transparent; text Plus Jakarta Sans 12/12 400, #201d1d `{text.primary}`; icon 12 x 12, #201d1d `{text.primary}`.

Parts:

- container: 288 x 20; Plus Jakarta Sans 12/18 400, #201d1d `{text.primary}`; gap 4px `{spacing.1}`; text "References Search inputs Resul"
  - child References: 97.45 x 20; at 0, 0; Plus Jakarta Sans 12/18 400, #201d1d `{text.primary}`; radius 24px `{radius.chip}`; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; text "References"
  - child svg: 12 x 12; at 8, 4
  - child References: 65.45 x 12; at 24, 4; Plus Jakarta Sans 12/12 400, #201d1d `{text.primary}`; text "References"
  - child Search inputs: 109.33 x 20; at 101.5, 0; Plus Jakarta Sans 12/18 400, #201d1d `{text.primary}`; radius 24px `{radius.chip}`; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; text "Search inputs"
  - child svg: 12 x 12; at 109.5, 4
  - child Search inputs: 77.33 x 12; at 125.5, 4; Plus Jakarta Sans 12/12 400, #201d1d `{text.primary}`; text "Search inputs"
  - child Results: 73.22 x 20; at 214.8, 0; Plus Jakarta Sans 12/18 400, #201d1d `{text.primary}`; radius 24px `{radius.chip}`; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; text "Results"
  - child svg: 12 x 12; at 222.8, 4
  - child Results: 41.22 x 12; at 238.8, 4; Plus Jakarta Sans 12/12 400, #201d1d `{text.primary}`; text "Results"

![Graph legend default](components/crops/graph-legend-default.png)

#### Graph legend chip
One legend chip. Hovering shows a help cursor and a white fill; the tooltip itself comes from script and is only present in three of the snapshots. Read as `graph-legend-item` on the search split view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| references | size 97.45 x 20; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; radius 24px `{radius.chip}`; background transparent; text Plus Jakarta Sans 12/12 400, #201d1d `{text.primary}`; cursor help; icon 12 x 12, #201d1d `{text.primary}` |
| references, hover | background #ffffff `{background.surface}` |
| inputs (as the first row, except) | size 109.33 x 20 |
| inputs, hover | background #ffffff `{background.surface}` |
| results (as the first row, except) | size 73.22 x 20 |
| results, hover | background #ffffff `{background.surface}` |

- Not measured: focus could not be captured on references (not focusable, or focused without matching :focus-visible).

Authored state rules (from the page's CSS): `.x:hover { background-color: white; }`.

![Graph legend chip references](components/crops/graph-legend-item-references.png) ![Graph legend chip references-hover](components/crops/graph-legend-item-references-hover.png) ![Graph legend chip inputs](components/crops/graph-legend-item-inputs.png) ![Graph legend chip inputs-hover](components/crops/graph-legend-item-inputs-hover.png) ![Graph legend chip results](components/crops/graph-legend-item-results.png) ![Graph legend chip results-hover](components/crops/graph-legend-item-results-hover.png)

#### Legend tooltip
Dark tooltip with an arrow, shown above a legend chip. Read as `graph-tooltip` on the search split view (hovering a result node), search split view (hovering the Search inputs legend chip), search split view (hovering the Results legend chip).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| search-inputs | size 162.41 x 28; padding 8px 12px `{spacing.2} {spacing.3}`; radius 8px `{radius.lg}`; background #333333 `{component.tooltip}`; shadow rgba(14, 18, 22, 0.35) 0px 10px 38px -10px, rgba(14, 18, 22, 0.2) 0px 10px 20px -15px (`{elevation.popup}`); text Plus Jakarta Sans 12/12 400, #ffffff `{text.inverse}`; icon 10 x 5, #ffffff `{text.inverse}` |
| results (as the first row, except) | size 232.84 x 28 |
| result-hover (same as the first row) | same values |

Parts:

- arrow: 10 x 5

![Legend tooltip search-inputs](components/crops/graph-tooltip-search-inputs.png) ![Legend tooltip results](components/crops/graph-tooltip-results.png) ![Legend tooltip result-hover](components/crops/graph-tooltip-result-hover.png)

#### Graph axis caption, vertical
Rotated caption with an arrow icon and two rules, at the bottom left of the graph ("More citations"). Read as `graph-axis-y` on the search map view.

**Values (default).** size 20 x 166.86; padding 0px 0px 0px 8px `{spacing.0} {spacing.0} {spacing.0} {spacing.2}`; radius 4px `{radius.sm}`; background transparent; text Plus Jakarta Sans 12/12 400, #686d79 `{text.secondary}`; transform matrix(0, -1, 1, 0, 0, 0); cursor pointer; icon 14 x 14, #8a92a1 `{text.tertiary}`.

Child layers that carry the look: div 1x16 background #8a92a1 `{component.axis-line}`; div 1x32 background #8a92a1 `{component.axis-line}`.

Parts:

- label: 12 x 80.86; Plus Jakarta Sans 12/12 400, #686d79 `{text.secondary}`; margin 4px 8px `{spacing.1} {spacing.2}`; text "More citations"
- icon: 14 x 14
- line: 1 x 16; background #8a92a1 `{component.axis-line}`

Authored state rules (from the page's CSS): `.x:hover { background-color: white; }`.

![Graph axis caption, vertical default](components/crops/graph-axis-y-default.png)

#### Graph axis caption, horizontal
The horizontal caption along the bottom edge ("More recently published"). Read as `graph-axis-x` on the search map view.

**Values (default).** size 222.89 x 20; padding 0px 0px 0px 8px `{spacing.0} {spacing.0} {spacing.0} {spacing.2}`; radius 4px `{radius.sm}`; background transparent; text Plus Jakarta Sans 12/12 400, #686d79 `{text.secondary}`; cursor pointer; icon 14 x 14, #8a92a1 `{text.tertiary}`.

Child layers that carry the look: div 16x1 background #8a92a1 `{component.axis-line}`; div 32x1 background #8a92a1 `{component.axis-line}`.

Parts:

- label: 136.89 x 12; Plus Jakarta Sans 12/12 400, #686d79 `{text.secondary}`; margin 4px 8px `{spacing.1} {spacing.2}`; text "More recently published"
- icon: 14 x 14
- line: 16 x 1; background #8a92a1 `{component.axis-line}`

Authored state rules (from the page's CSS): `.x:hover { background-color: white; }`.

![Graph axis caption, horizontal default](components/crops/graph-axis-x-default.png)

#### Graph toolbar
Five 32px icon buttons stacked at the bottom right of the graph: pointer, recentre, zoom in, zoom out and layout settings. Read as `graph-controls` on the search split view, search map view, library map view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 32 x 176; gap 4px `{spacing.1}`; radius 8px `{radius.lg}`; background transparent; text Plus Jakarta Sans 16/24 400, #000000 `{text.default}`; icon 16 x 16, #000000 `{text.default}` |
| split (same as the first row) | same values |
| library (same as the first row) | same values |

Parts:

- container: 32 x 176; radius 8px `{radius.lg}`; gap 4px `{spacing.1}`
  - child button: 32 x 32; at 0, 0; Plus Jakarta Sans 18/27 400, #000000 `{text.default}`; radius 4px `{radius.sm}`; padding 8px `{spacing.2}`
  - child button: 32 x 32; at 0, 36; Plus Jakarta Sans 18/27 400, #000000 `{text.default}`; radius 4px `{radius.sm}`; padding 8px `{spacing.2}`
  - child button: 32 x 32; at 0, 72; Plus Jakarta Sans 18/27 400, #000000 `{text.default}`; radius 4px `{radius.sm}`; padding 8px `{spacing.2}`
  - child button: 32 x 32; at 0, 108; Plus Jakarta Sans 18/27 400, #000000 `{text.default}`; radius 4px `{radius.sm}`; padding 8px `{spacing.2}`
  - child button: 32 x 32; at 0, 144; Plus Jakarta Sans 18/27 400, #000000 `{text.default}`; radius 4px `{radius.sm}`; padding 8px `{spacing.2}`

![Graph toolbar default](components/crops/graph-controls-default.png) ![Graph toolbar split](components/crops/graph-controls-split.png) ![Graph toolbar library](components/crops/graph-controls-library.png)

#### Graph toolbar button
One toolbar button. The first (pointer) is the active tool. Read as `graph-control-button` on the search map view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| pointer | size 32 x 32 (height `{size.control-md}`); padding 8px `{spacing.2}`; radius 4px `{radius.sm}`; background transparent; text Plus Jakarta Sans 18/27 400, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| pointer, hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| pointer, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| recentre (same as the first row) | same values |
| recentre, hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| recentre, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| zoom-in (same as the first row) | same values |
| zoom-in, hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| settings (same as the first row) | same values |
| settings, hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| settings, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(0, 0, 0, 0.05); }`.

![Graph toolbar button pointer](components/crops/graph-control-button-pointer.png) ![Graph toolbar button pointer-hover](components/crops/graph-control-button-pointer-hover.png) ![Graph toolbar button pointer-focus-visible](components/crops/graph-control-button-pointer-focus-visible.png) ![Graph toolbar button recentre](components/crops/graph-control-button-recentre.png) ![Graph toolbar button recentre-hover](components/crops/graph-control-button-recentre-hover.png) ![Graph toolbar button recentre-focus-visible](components/crops/graph-control-button-recentre-focus-visible.png) ![Graph toolbar button zoom-in](components/crops/graph-control-button-zoom-in.png) ![Graph toolbar button zoom-in-hover](components/crops/graph-control-button-zoom-in-hover.png) ![Graph toolbar button settings](components/crops/graph-control-button-settings.png) ![Graph toolbar button settings-hover](components/crops/graph-control-button-settings-hover.png) ![Graph toolbar button settings-focus-visible](components/crops/graph-control-button-settings-focus-visible.png)

#### Panel resize handle
Invisible 8px strip at the edge of the graph with a 4px display bar; drag resizes the list or the panel. Read as `graph-resize-handle` on the search split view.

**Values (default).** size 8 x 200; background transparent; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; transform matrix(1, 0, 0, 1, -4, 0); cursor col-resize.

Child layers that carry the look: div 4x200 background #8a92a1 `{component.axis-line}` radius 1px.

Parts:

- display: 4 x 200; background #8a92a1 `{component.axis-line}`; radius 1px; margin 2px 0px

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Positions moved pill
Replaces the axes captions once a node has been dragged: a peach pill with an icon, in the bottom left of the graph. It opens a one-item menu. Read as `positions-moved` on the library map view (positions moved), library map view (reset menu open).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default (same: hover) | size 150.33 x 24 (height `{size.control-sm}`); padding 4px 8px `{spacing.1} {spacing.2}`; gap 8px `{spacing.2}`; radius 48px `{radius.pill}`; background #f5c751 `{component.positions-moved}`; text Plus Jakarta Sans 14/14 500, #201d1d `{text.primary}`; cursor pointer; icon 16 x 16, #201d1d `{text.primary}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| open (same as the first row) | same values |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Positions moved pill default](components/crops/positions-moved-default.png) ![Positions moved pill focus-visible](components/crops/positions-moved-focus-visible.png) ![Positions moved pill open](components/crops/positions-moved-open.png)

#### Reset positions menu
White menu card above the Positions moved pill with one row, Reset. Read as `reset-menu` on the library map view (reset menu open).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 220 x 38; padding 4px `{spacing.1}`; radius 6px `{radius.md}`; background #ffffff `{background.surface}`; shadow rgba(22, 23, 24, 0.35) 0px 10px 38px -10px, rgba(22, 23, 24, 0.2) 0px 10px 20px -15px (`{elevation.menu}`); text Plus Jakarta Sans 14/21 400, #201d1d `{text.primary}`; icon 18 x 18, #201d1d `{text.primary}` |
| item (same: hover) | size 212 x 30; padding 8px 8px 8px 32px `{spacing.2} {spacing.2} {spacing.2} {spacing.8}`; radius 3px `{radius.xs}`; background transparent; text Plus Jakarta Sans 14/21 400, #201d1d `{text.primary}`; icon 18 x 18, #201d1d `{text.primary}` |

Parts:

- item: 212 x 30; Plus Jakarta Sans 14/21 400, #201d1d `{text.primary}`; radius 3px `{radius.xs}`; padding 8px 8px 8px 32px `{spacing.2} {spacing.2} {spacing.2} {spacing.8}`; text "Reset"
- icon: 20 x 20

Authored state rules (from the page's CSS): `.x[data-state="checked"] { font-weight: 600; }`.

![Reset positions menu default](components/crops/reset-menu-default.png) ![Reset positions menu item](components/crops/reset-menu-item.png)

### Article list

The 400px column of result cards in the split view, and the same cards at full width in the list view and in the library.

#### Result list column
The 400px column of result cards at the left of the split view, with a thin loading line on top and a pager at the bottom. Read as `list-column` on the search split view.

**Values (default).** size 400 x 726; padding 8px `{spacing.2}`; background transparent; text Plus Jakarta Sans 16/24 500, #000000 `{text.default}`; icon 18 x 18, #000000 `{text.default}`.

Child layers that carry the look: div 372x2 background #0000ff `{component.result-card-loadline}`; div 372x2; div 372x204 background #ffffff `{background.surface}` radius 8px.

Parts:

- viewport: 372 x 686; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; radius 4px `{radius.sm}`; text "Jimenez, 2023 SWE-bench: Can L"
- loadline: 372 x 2; background #0000ff `{component.result-card-loadline}`; opacity 0

![Result list column default](components/crops/list-column-default.png)

#### Result card
A white card per article: author and year, title, journal in italics, a selection circle at the top right, then a rule and the abstract. The tinted variant is the card the pointer was over when its snapshot was taken (it stays tinted and its node is highlighted in the graph). Read as `list-card` on the search split view, search split view (hovering a list card), search list view and 2 more.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 372 x 204; radius 8px `{radius.lg}`; background #ffffff `{background.surface}`; text Plus Jakarta Sans 16/24 500, #000000 `{text.default}`; icon 18 x 18, #000000 `{text.default}` |
| hover | shadow #a7d4ff 0px 0px 0px 1px inset (`{elevation.ring-highlight}`) |
| second (as the first row, except) | size 372 x 225 |
| tinted (as the first row, except) | size 372 x 225; background #f0f6ff `{component.list-card-tinted}`; shadow #a7d4ff 0px 0px 0px 1px inset (`{elevation.ring-highlight}`) |
| list-view (as the first row, except) | size 966 x 183 |
| list-view, hover | shadow #a7d4ff 0px 0px 0px 1px inset (`{elevation.ring-highlight}`) |
| library (as the first row, except) | size 1114 x 217; icon 16 x 16, #f07d59 `{palette.ugc.amber}` |
| library, hover | shadow #a7d4ff 0px 0px 0px 1px inset (`{elevation.ring-highlight}`) |
| selected (as the first row, except) | size 966 x 183; shadow #000000 0px 0px 0px 1px inset (`{elevation.ring-strong}`) |

Parts:

- details: 336 x 123; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; padding 12px `{spacing.3}`; gap 8px `{spacing.2}`; text "Jimenez, 2023 SWE-bench: Can L"
- nickname: 108.92 x 24; Plus Jakarta Sans 16/24 500, #000000 `{text.default}`; text "Jimenez, 2023"
- title: 312 x 42; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; text "SWE-bench: Can Language Models"
- journal: 58.27 x 21; Plus Jakarta Sans 14/21 400 italic, #000000 `{text.default}`; text "arXiv.org"
- rule: 370 x 1; margin 0px 1px; border T:1px solid #dde0e4 `{border.rule}`
- abstract: 348 x 56; Plus Jakarta Sans 12/18 400, #201d1d `{text.primary}`; text "Language models have outpaced "
- side: 36 x 123; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; radius 0px 8px 8px 0px; padding 8px `{spacing.2}`
- tick: 20 x 20

Authored state rules (from the page's CSS): `.x:hover { box-shadow: inset 0 0 0 1px var(--selection); }`.

![Result card default](components/crops/list-card-default.png) ![Result card hover](components/crops/list-card-hover.png) ![Result card second](components/crops/list-card-second.png) ![Result card tinted](components/crops/list-card-tinted.png) ![Result card list-view](components/crops/list-card-list-view.png) ![Result card list-view-hover](components/crops/list-card-list-view-hover.png) ![Result card library](components/crops/list-card-library.png) ![Result card library-hover](components/crops/list-card-library-hover.png) ![Result card selected](components/crops/list-card-selected.png)

#### Result card, focus ring
The card body is a button; this is its keyboard focus ring, measured on the button itself. Read as `list-card-focus` on the search split view.

Not on the page when it was captured.

#### Result card side button
Full-height 36px strip at the right of a card; holds the selection circle. Read as `list-card-side` on the search split view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default (same: hover) | size 36 x 123; padding 8px `{spacing.2}`; radius 0px 8px 8px 0px; background transparent; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; cursor pointer; icon 18 x 18, #000000 `{text.default}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Parts:

- tick: 20 x 20
- icon: 18 x 18; opacity 0

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Result card side button default](components/crops/list-card-side-default.png) ![Result card side button hover](components/crops/list-card-side-hover.png) ![Result card side button focus-visible](components/crops/list-card-side-focus-visible.png)

#### List pager
Previous and next chevrons around a "1 - 20 of 686" label at the foot of the list. Read as `list-pager` on the search split view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| prev | size 32 x 24 (height `{size.control-sm}`); padding 4px 8px `{spacing.1} {spacing.2}`; radius 4px `{radius.sm}`; background transparent; text Plus Jakarta Sans 14/21 500, #000000 `{text.default}`; opacity 0.4; icon 16 x 16, #000000 `{text.default}` |
| prev, hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| next (as the first row, except) | opacity none; cursor pointer |
| next, hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| next, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

- Not measured: focus could not be captured on prev (not focusable, or focused without matching :focus-visible).

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(0, 0, 0, 0.05); }`.

![List pager prev](components/crops/list-pager-prev.png) ![List pager prev-hover](components/crops/list-pager-prev-hover.png) ![List pager next](components/crops/list-pager-next.png) ![List pager next-hover](components/crops/list-pager-next-hover.png) ![List pager next-focus-visible](components/crops/list-pager-next-focus-visible.png)

#### List scrollbar
Custom 12px scrollbar track with a thumb; visible on hover in the list. Read as `list-scrollbar` on the search split view (hovering a list card).

**Values (default).** size 12 x 686; padding 1px; background rgba(0, 0, 0, 0.1) `{action.quiet-hover}`; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; transition background-color 0.16s ease-out.

Parts:

- thumb: 10 x 112.08; background #ffffff `{background.surface}`; radius 12px `{radius.xl}`

Authored state rules (from the page's CSS): `.x:hover { background-color: rgba(0, 0, 0, 0.15); }`.

![List scrollbar default](components/crops/list-scrollbar-default.png)

#### Library folder chip
Outlined chip under a library card title naming the collection the article is in. Read as `list-state-chip` on the library list view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 1054 x 26; gap 4px `{spacing.1}`; background transparent; text Plus Jakarta Sans 12/18 400, #000000 `{text.default}`; icon 16 x 16, #f07d59 `{palette.ugc.amber}` |
| hover | cursor pointer |

Child layers that carry the look: div 124.5x26 radius 4px shadow #dde0e4 0px 0px 0px 1px inset (`{elevation.ring-field-dark}`).

Parts:

- container: 1054 x 26; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; gap 4px `{spacing.1}`; text "my-collection"
  - child svg: 16 x 16; at 8, 5
  - child my-collection: 80.47 x 18; at 32, 4; Plus Jakarta Sans 12/18 400, #000000 `{text.default}`; text "my-collection"

![Library folder chip default](components/crops/list-state-chip-default.png)

### Next Search panel

The right panel when nothing is selected: a header, a dismissible tip, an empty state, and the black Search Settings drawer.

#### Next Search panel
The right-hand column when nothing is selected: header, a dismissible tip, an empty state with art, and the black Search Settings drawer at the foot. Read as `next-search` on the search split view.

**Values (default).** size 390 x 772; radius 12px `{radius.xl}`; background rgba(221, 204, 255, 0.2) `{background.panel-tint}`; text Plus Jakarta Sans 16/24 500, #000000 `{text.default}`; icon 16 x 16, #ffffff `{text.inverse}`.

![Next Search panel default](components/crops/next-search-default.png)

#### Next Search header
Title at the left, the black "Auto-save to..." pill at the right. Read as `next-search-header` on the search split view.

**Values (default).** size 390 x 46; padding 16px `{spacing.4}`; radius 12px 12px 0px 0px; background transparent; text Plus Jakarta Sans 16/24 500, #000000 `{text.default}`; icon 16 x 16, #ffffff `{text.inverse}`.

Child layers that carry the look: button 126.2x32 background #000000 `{action.primary}` radius 48px.

Parts:

- container: 390 x 46; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; radius 12px 12px 0px 0px; padding 16px `{spacing.4}`; text "Next Search Auto-save to..."
  - child Next Search: 92.5 x 24; at 16, 11; Plus Jakarta Sans 16/24 500, #000000 `{text.default}`; text "Next Search"
  - child Auto-save to...: 126.16 x 32; at 247.8, 7; Plus Jakarta Sans 14/21 500, #ffffff `{text.inverse}`; background #000000 `{action.primary}`; radius 48px `{radius.pill}`; padding 8px `{spacing.2}`; gap 8px `{spacing.2}`; text "Auto-save to..."
  - child Auto-save to...: 86.16 x 12; at 255.8, 17; Plus Jakarta Sans 12/12 500, #ffffff `{text.inverse}`; text "Auto-save to..."

![Next Search header default](components/crops/next-search-header-default.png)

#### Auto-save button
Black pill with a disk icon. Read as `autosave-button` on the search split view, keyword search results (list view).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default (same: hover, pressed) | size 126.16 x 32 (height `{size.control-md}`); padding 8px `{spacing.2}`; gap 8px `{spacing.2}`; radius 48px `{radius.pill}`; background #000000 `{action.primary}`; text Plus Jakarta Sans 12/12 500, #ffffff `{text.inverse}`; cursor pointer; icon 16 x 16, #ffffff `{text.inverse}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Auto-save button default](components/crops/autosave-button-default.png) ![Auto-save button focus-visible](components/crops/autosave-button-focus-visible.png) ![Auto-save button pressed](components/crops/autosave-button-pressed.png)

#### Tip banner
Turquoise strip with the rabbit, a line of help and a close button. Read as `tip-banner` on the search split view.

**Values (default).** size 374 x 44; radius 8px `{radius.lg}`; background #d7f6f8 `{background.hint}`; text Plus Jakarta Sans 12/14 400, #000000 `{text.default}`; icon 30 x 30, #000000 `{text.default}`.

Parts:

- container: 374 x 44; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; background #d7f6f8 `{background.hint}`; radius 8px `{radius.lg}`; margin 0px 8px 8px `{spacing.0} {spacing.2} {spacing.2}`; text "Select articles to help your n"
  - child svg: 30 x 30; at 8, 7
  - child Select articles to help : 288 x 28; at 50, 8; Plus Jakarta Sans 12/14 400, #000000 `{text.default}`; text "Select articles to help your n"
  - child button: 32 x 44; at 342, 0; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; padding 0px 8px `{spacing.0} {spacing.2}`
  - child svg: 16 x 16; at 350, 14

![Tip banner default](components/crops/tip-banner-default.png)

#### Tip close button
32px icon button that dismisses the tip. Read as `tip-close` on the search split view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 32 x 44; padding 0px 8px `{spacing.0} {spacing.2}`; background transparent; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(0, 0, 0, 0.05); }`.

![Tip close button default](components/crops/tip-close-default.png) ![Tip close button hover](components/crops/tip-close-hover.png) ![Tip close button focus-visible](components/crops/tip-close-focus-visible.png)

#### Next Search empty state
Centred heading "Grow and go!", an italic line, the illustration and a "Find out how it works" link. Read as `empty-state` on the search split view.

**Values (default).** size 390 x 673; padding 8px 24px 24px 24px `{spacing.2} {spacing.6} {spacing.6} {spacing.6}`; gap 8px `{spacing.2}`; background transparent; text Plus Jakarta Sans 24/36 400, #000000 `{text.default}`.

Parts:

- container: 390 x 673; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; padding 8px 24px 24px `{spacing.2} {spacing.6} {spacing.6}`; gap 8px `{spacing.2}`; text "Grow and go! Improve your resu"
  - child Grow and go!: 152.45 x 36; at 118.8, 141.9; Plus Jakarta Sans 24/36 400, #000000 `{text.default}`; text "Grow and go!"
  - child Improve your results by : 342 x 42; at 24, 185.9; Plus Jakarta Sans 14/21 400 italic, #000000 `{text.default}`; text "Improve your results by select"
  - child img: 249.98 x 178.22; at 70, 243.9; margin 8px 0px `{spacing.2} {spacing.0}`
  - child Find out how it works: 141.39 x 21; at 124.3, 438.1; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; text "Find out how it works"
  - child Find out how it works: 141.39 x 18; at 124.3, 439.1; Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; text "Find out how it works"

![Next Search empty state default](components/crops/empty-state-default.png)

#### Find out how it works link
Underlined link under the illustration. Read as `empty-state-link` on the search split view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default (same: hover) | size 141.39 x 18; background transparent; text Plus Jakarta Sans 14/21 600, #000000 `{text.default}`, underline; cursor pointer |
| focus-visible | outline 1px auto #005fcc `{border.focus-browser}`, offset 1px |

Authored state rules (from the page's CSS): `a:hover { text-decoration: underline; }`.

![Find out how it works link default](components/crops/empty-state-link-default.png) ![Find out how it works link focus-visible](components/crops/empty-state-link-focus-visible.png)

#### Search Settings drawer
Black rounded sheet pinned to the foot of the right panel: a head row with a chevron, a rule, then a summary line and the grey Search button. The article panel reuses it as "Dive deeper on this article". Read as `drawer` on the search split view, search map view (a node inspected), Search Settings drawer (open).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| search-settings | size 390 x 110; radius 32px 32px 16px 16px; background #000000 `{component.drawer}`; text Plus Jakarta Sans 16/24 600, #ffffff `{text.inverse}`; transition max-height 0.5s ease; icon 20 x 20, #ffffff `{text.inverse}` |
| dive-deeper (same as the first row) | same values |
| open (as the first row, except) | size 390 x 772 |

Parts:

- head: 390 x 57; Plus Jakarta Sans 14/21 400, #ffffff `{text.inverse}`; padding 16px `{spacing.4}`; gap 8px `{spacing.2}`; border B:1px solid #686d79 `{border.drawer}`; text "Search Settings"
- title: 122.03 x 24; Plus Jakarta Sans 16/24 600, #ffffff `{text.inverse}`; text "Search Settings"
- chevron: 20 x 20
- summary: 211.91 x 18; Plus Jakarta Sans 14/18 400, #ffffff `{text.inverse}`; text "Find related articles of 9 art"
- emph: 100.98 x 18; Plus Jakarta Sans 14/14 600, #ffffff `{text.inverse}`; text "related articles"

![Search Settings drawer search-settings](components/crops/drawer-search-settings.png) ![Search Settings drawer dive-deeper](components/crops/drawer-dive-deeper.png) ![Search Settings drawer open](components/crops/drawer-open.png)

#### Drawer head button
The title row of the drawer; pressing it opens and closes the sheet. Read as `drawer-head` on the search split view, search map view (a node inspected).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| search-settings (same: hover) | size 390 x 57; padding 16px `{spacing.4}`; gap 8px `{spacing.2}`; border B: 1px solid #686d79 `{border.drawer}`; background transparent; text Plus Jakarta Sans 16/24 600, #ffffff `{text.inverse}`; cursor pointer; icon 20 x 20, #ffffff `{text.inverse}` |
| search-settings, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| dive-deeper (same: hover) (same as the first row) | same values |

Child layers that carry the look: button 390x57 border 1px solid #686d79 `{border.drawer}`.

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Drawer head button search-settings](components/crops/drawer-head-search-settings.png) ![Drawer head button search-settings-focus-visible](components/crops/drawer-head-search-settings-focus-visible.png) ![Drawer head button dive-deeper](components/crops/drawer-head-dive-deeper.png)

#### Drawer Search button
Grey pill button at the right of the drawer summary. Read as `drawer-search-button` on the search split view.

**Values (default).** size 71.41 x 37 (height `{size.field}`); padding 8px 12px `{spacing.2} {spacing.3}`; radius 48px `{radius.pill}`; background #e8e7f6 `{action.accent-soft}`; text Plus Jakarta Sans 14/14 600, #000000 `{text.default}`; opacity 0.6.

- Not measured: focus could not be captured on the component (not focusable, or focused without matching :focus-visible).

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Drawer Search button default](components/crops/drawer-search-button-default.png)

### Article detail panel

The right panel when an article is selected, from the graph or from the list. It reuses the black drawer as "Dive deeper on this article".

#### Article detail panel
The right column when a node or card is selected: a header (counts, close, sticker and nickname, action icons), the title, journal, authors, library buttons, folder chip and abstract, with the "Dive deeper" drawer at the foot. Read as `inspector` on the search split view (a node inspected), search map view (a node inspected).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 390 x 772; radius 16px `{radius.2xl}`; background #ffffff `{background.surface}`; shadow #a7d4ff 0px 0px 0px 1px inset (`{elevation.ring-highlight}`); text Plus Jakarta Sans 14/14 400, #000000 `{text.default}`; icon 16 x 16, #000000 `{text.default}` |
| split (same as the first row) | same values |

Parts:

- header: 390 x 108; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; padding 12px `{spacing.3}`; gap 16px `{spacing.4}`; border B:1px solid #dde0e4 `{border.rule}`; text "Article Notes 0 Raghavendra, 2"
- body: 390 x 662; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; radius 8px `{radius.lg}`; text "SWE Atlas: Benchmarking Coding"
- nav: 145.2 x 33; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; background #f2f2f2 `{action.control}`; radius 48px `{radius.pill}`; padding 2px; gap 4px `{spacing.1}`; text "Article Notes 0"
- nickname: 149.25 x 24; Plus Jakarta Sans 16/24 500, #000000 `{text.default}`; text "Raghavendra, 2026"
- title: 366 x 42; Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; text "SWE Atlas: Benchmarking Coding"
- journal: 366 x 21; Plus Jakarta Sans 14/21 400 italic, #000000 `{text.default}`; text "arXiv (Cornell University)"
- authors: 366 x 29; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; text "Mohit Raghavendra ... +13 Yunz"
- abstract: 366 x 414; Plus Jakarta Sans 12/18 300, #000000 `{text.default}`; text "We introduce SWE Atlas, a benc"

![Article detail panel default](components/crops/inspector-default.png) ![Article detail panel split](components/crops/inspector-split.png)

#### Article navigation
Previous and next article arrows with a count. Read as `inspector-nav` on the search map view (a node inspected).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 145.2 x 33; padding 2px; gap 4px `{spacing.1}`; radius 48px `{radius.pill}`; background #f2f2f2 `{action.control}`; text Plus Jakarta Sans 14/14 400, #000000 `{text.default}` |
| item (same: hover) | size 58.72 x 29; padding 4px 8px `{spacing.1} {spacing.2}`; radius 48px `{radius.pill}`; background #ffffff `{background.surface}`; text Plus Jakarta Sans 14/14 400, #000000 `{text.default}`; cursor pointer |

- Not measured: focus could not be captured on item (not focusable, or focused without matching :focus-visible).

Parts:

- container: 145.2 x 33; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; background #f2f2f2 `{action.control}`; radius 48px `{radius.pill}`; padding 2px; gap 4px `{spacing.1}`; text "Article Notes 0"
  - child Article: 58.72 x 29; at 2, 2; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; background #ffffff `{background.surface}`; radius 48px `{radius.pill}`; padding 4px 8px `{spacing.1} {spacing.2}`; text "Article"
  - child Notes 0: 78.48 x 29; at 64.7, 2; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; radius 48px `{radius.pill}`; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; text "Notes 0"
  - child 0: 18.25 x 21; at 117, 6; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; background rgba(0, 0, 0, 0.05) `{action.quiet}`; radius 48px `{radius.pill}`; padding 0px 4px `{spacing.0} {spacing.1}`; text "0"

Authored state rules (from the page's CSS): `.x:hover { background-color: white; }`.

![Article navigation default](components/crops/inspector-nav-default.png) ![Article navigation item](components/crops/inspector-nav-item.png)

#### Article panel close button
24px X at the top right of the panel. Read as `inspector-close` on the search map view (a node inspected).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 24 x 24 (height `{size.control-sm}`); padding 4px `{spacing.1}`; radius 36px `{radius.search}`; background #f2f2f2 `{action.control}`; text Plus Jakarta Sans 18/27 400, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| hover | background #e8e8e8 `{action.control-hover}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: var(--ui-bg-hover); }`.

![Article panel close button default](components/crops/inspector-close-default.png) ![Article panel close button hover](components/crops/inspector-close-hover.png) ![Article panel close button focus-visible](components/crops/inspector-close-focus-visible.png)

#### Sticker button
34px square button at the left of the nickname (the sticker icon). Read as `inspector-sticker` on the search map view (a node inspected).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default (same: hover) | size 34 x 34; border 1px solid #dde0e4 `{border.rule}`; radius 48px `{radius.pill}`; background rgba(255, 255, 255, 0.9) `{action.glass-hover}`; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; cursor pointer; icon 18 x 18, #000000 `{text.default}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Parts:

- emoji: 32 x 32
- icon: 18 x 18

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Sticker button default](components/crops/inspector-sticker-default.png) ![Sticker button focus-visible](components/crops/inspector-sticker-focus-visible.png)

#### Nickname row
Author and year heading ("Raghavendra, 2026") with the evaluation dot and action icons. Read as `inspector-nickname-row` on the search map view (a node inspected).

**Values (default).** size 366 x 34; background transparent; text Plus Jakarta Sans 16/24 500, #000000 `{text.default}`; icon 18 x 18, #000000 `{text.default}`.

Child layers that carry the look: button 34x34 background rgba(255, 255, 255, 0.9) `{action.glass-hover}` border 1px solid #dde0e4 `{border.rule}` radius 48px; div 8x8 background #8add8a `{action.upgrade}` radius 50%.

Parts:

- nickname: 149.25 x 24; Plus Jakarta Sans 16/24 500, #000000 `{text.default}`; text "Raghavendra, 2026"
- dot: 8 x 8; background #8add8a `{action.upgrade}`; radius 50%
- tick: 20 x 20

![Nickname row default](components/crops/inspector-nickname-row-default.png)

#### Article action icon button
24px icon buttons in the nickname row. Read as `inspector-icon-button` on the search map view (a node inspected).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| first | size 24 x 24 (height `{size.control-sm}`); padding 4px `{spacing.1}`; gap 4px `{spacing.1}`; radius 48px `{radius.pill}`; background transparent; text Plus Jakarta Sans 12/18 600, #333333 `{text.icon-strong}`; cursor pointer; icon 16 x 16, #333333 `{text.icon-strong}` |
| first, hover | background #e8e8e8 `{action.control-hover}` |
| first, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| second | size 24 x 24 (height `{size.control-sm}`); padding 4px `{spacing.1}`; radius 24px `{radius.chip}`; background transparent; text Plus Jakarta Sans 16/24 400, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| second, hover | background rgba(0, 0, 0, 0.08) `{action.quiet-hover-soft}` |
| second, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Child layers that carry the look: div 8x8 background #8add8a `{action.upgrade}` radius 50%.

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: var(--ui-bg-hover); }`.

![Article action icon button first](components/crops/inspector-icon-button-first.png) ![Article action icon button first-hover](components/crops/inspector-icon-button-first-hover.png) ![Article action icon button first-focus-visible](components/crops/inspector-icon-button-first-focus-visible.png) ![Article action icon button second](components/crops/inspector-icon-button-second.png) ![Article action icon button second-hover](components/crops/inspector-icon-button-second-hover.png) ![Article action icon button second-focus-visible](components/crops/inspector-icon-button-second-focus-visible.png)

#### Article title
The paper title, a link to the source. Read as `inspector-title` on the search map view (a node inspected).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 331.11 x 39; background transparent; text Plus Jakarta Sans 14/21 600, #000000 `{text.default}`, underline; cursor pointer |
| hover | text Plus Jakarta Sans 14/21 600, #746fa3 `{text.link-hover}`, underline |
| focus-visible | outline 1px auto #005fcc `{border.focus-browser}`, offset 1px |

Parts:

- heading: 366 x 42; Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; text "SWE Atlas: Benchmarking Coding"

Authored state rules (from the page's CSS): `a:hover { text-decoration: underline; }`; `.x:hover a { text-decoration: underline; color: #746fa3; }`.

![Article title default](components/crops/inspector-title-default.png) ![Article title hover](components/crops/inspector-title-hover.png) ![Article title focus-visible](components/crops/inspector-title-focus-visible.png)

#### Author chips
Authors as inline buttons; the rest collapse into a "+13" button. Read as `inspector-authors` on the search map view (a node inspected).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 366 x 29; background transparent; text Plus Jakarta Sans 14/14 400, #686d79 `{text.secondary}` |
| author | size 143.88 x 29; padding 4px 8px `{spacing.1} {spacing.2}`; radius 48px `{radius.pill}`; background transparent; text Plus Jakarta Sans 14/14 400, #686d79 `{text.secondary}` |
| author, hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| more (same: hover) | size 39.38 x 26; padding 4px `{spacing.1}`; radius 4px `{radius.sm}`; background rgba(0, 0, 0, 0.05) `{action.quiet}`; text Plus Jakarta Sans 12/18 400, #201d1d `{text.primary}`; cursor pointer |
| more, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

- Not measured: focus could not be captured on author (not focusable, or focused without matching :focus-visible).

Child layers that carry the look: button 39.4x26 background rgba(0, 0, 0, 0.05) `{action.quiet}` radius 4px.

Parts:

- container: 366 x 29; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; text "Mohit Raghavendra ... +13 Yunz"
  - child Mohit Raghavendra: 143.88 x 29; at -4, 0; Plus Jakarta Sans 14/21 400, #686d79 `{text.secondary}`; radius 48px `{radius.pill}`; padding 4px 8px `{spacing.1} {spacing.2}`; margin 0px -4px; text "Mohit Raghavendra"
  - child ... +13: 39.38 x 26; at 139.9, 1.5; Plus Jakarta Sans 12/18 400, #201d1d `{text.primary}`; background rgba(0, 0, 0, 0.05) `{action.quiet}`; radius 4px `{radius.sm}`; padding 4px `{spacing.1}`; text "... +13"
  - child Yunzhong He: 102.14 x 29; at 179.3, 0; Plus Jakarta Sans 14/21 400, #686d79 `{text.secondary}`; radius 48px `{radius.pill}`; padding 4px 8px `{spacing.1} {spacing.2}`; margin 0px -4px; text "Yunzhong He"

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: var(--lavender-25); z-index: 1; }`; `.x:disabled:hover { border-color: transparent; background-color: rgba(0, 0, 0, 0.05); }`.

![Author chips default](components/crops/inspector-authors-default.png) ![Author chips author](components/crops/inspector-authors-author.png) ![Author chips author-hover](components/crops/inspector-authors-author-hover.png) ![Author chips more](components/crops/inspector-authors-more.png) ![Author chips more-focus-visible](components/crops/inspector-authors-more-focus-visible.png)

#### Add to library row
A "Library" label with the Collection and Reading List buttons. Read as `inspector-library-row` on the search map view (a node inspected).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 366 x 28; background transparent; text Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; icon 12 x 12, #ffffff `{text.inverse}` |
| collection (same: hover) | size 94.19 x 28; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; border 1px solid transparent; radius 48px `{radius.pill}`; background #000000 `{action.primary}`; text Plus Jakarta Sans 12/18 600, #ffffff `{text.inverse}`; cursor pointer; icon 12 x 12, #ffffff `{text.inverse}` |
| collection, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| reading-list (same: hover) | size 104.09 x 28; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; border 1px solid transparent; radius 48px `{radius.pill}`; background #000000 `{action.primary}`; text Plus Jakarta Sans 12/18 600, #ffffff `{text.inverse}`; cursor pointer; icon 12 x 12, #ffffff `{text.inverse}` |
| reading-list, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Child layers that carry the look: button 94.2x28 background #000000 `{action.primary}` border 1px solid transparent radius 48px; button 104.1x28 background #000000 `{action.primary}` border 1px solid transparent radius 48px.

Parts:

- container: 366 x 28; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; text "Your Library Collection Readin"
  - child Your Library: 79.14 x 21; at 0, 3.5; Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; text "Your Library"
  - child Collection: 94.19 x 28; at 159.7, 0; Plus Jakarta Sans 12/18 600, #ffffff `{text.inverse}`; background #000000 `{action.primary}`; radius 48px `{radius.pill}`; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; border T:1px solid transparent / R:1px solid transparent / B:1px solid transparent / L:1px solid transparent; text "Collection"
  - child svg: 12 x 12; at 232.9, 8
  - child Reading List: 104.09 x 28; at 261.9, 0; Plus Jakarta Sans 12/18 600, #ffffff `{text.inverse}`; background #000000 `{action.primary}`; radius 48px `{radius.pill}`; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; border T:1px solid transparent / R:1px solid transparent / B:1px solid transparent / L:1px solid transparent; text "Reading List"
  - child svg: 12 x 12; at 345, 8

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Add to library row default](components/crops/inspector-library-row-default.png) ![Add to library row collection](components/crops/inspector-library-row-collection.png) ![Add to library row collection-focus-visible](components/crops/inspector-library-row-collection-focus-visible.png) ![Add to library row reading-list](components/crops/inspector-library-row-reading-list.png) ![Add to library row reading-list-focus-visible](components/crops/inspector-library-row-reading-list-focus-visible.png)

#### Folder chip
The collection the article is already in, with a remove button. Read as `inspector-folder-chip` on the search map view (a node inspected).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default (same: hover) | size 144.47 x 26; padding 4px 0px 4px 8px `{spacing.1} {spacing.0} {spacing.1} {spacing.2}`; gap 8px `{spacing.2}`; radius 4px `{radius.sm}`; background rgba(240, 125, 89, 0.2) `{component.folder-tint}`; text Plus Jakarta Sans 12/18 400, #000000 `{text.default}`; icon 16 x 16, #f07d59 `{palette.ugc.amber}` |
| remove | size 24 x 24 (height `{size.control-sm}`); padding 4px `{spacing.1}`; background transparent; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| remove, hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| remove, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Parts:

- icon: 16 x 16
- label: 80.47 x 18; Plus Jakarta Sans 12/18 400, #000000 `{text.default}`; text "my-collection"
- remove: 24 x 24; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; padding 4px `{spacing.1}`; margin -4px 0px

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(0, 0, 0, 0.05); }`.

![Folder chip default](components/crops/inspector-folder-chip-default.png) ![Folder chip remove](components/crops/inspector-folder-chip-remove.png) ![Folder chip remove-hover](components/crops/inspector-folder-chip-remove-hover.png) ![Folder chip remove-focus-visible](components/crops/inspector-folder-chip-remove-focus-visible.png)

#### Abstract text
Abstract paragraphs in the scrolling body of the panel. Read as `inspector-abstract` on the search map view (a node inspected).

**Values (default).** size 366 x 414; background transparent; text Plus Jakarta Sans 12/18 300, #000000 `{text.default}`.

![Abstract text default](components/crops/inspector-abstract-default.png)

#### Dive deeper chips
Three outlined chips in the drawer: Similar, Refs and Cited By, each with a count. The drawer is always shown on this panel; the "Dive deeper on this article" title above them is the drawer head. Read as `inspector-chips` on the search map view (a node inspected).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| similar (same: hover) | size 185.08 x 30; padding 8px `{spacing.2}`; radius 48px `{radius.pill}`; background #e8e7f6 `{action.accent-soft}`; text Plus Jakarta Sans 14/14 400, #000000 `{text.default}`; cursor pointer |
| similar, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| refs (same: hover) (as the first row, except) | size 68.34 x 30 |
| cited-by (same: hover) (as the first row, except) | size 88.58 x 30 |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Dive deeper chips similar](components/crops/inspector-chips-similar.png) ![Dive deeper chips similar-focus-visible](components/crops/inspector-chips-similar-focus-visible.png) ![Dive deeper chips refs](components/crops/inspector-chips-refs.png) ![Dive deeper chips cited-by](components/crops/inspector-chips-cited-by.png)

### Layout settings

The right panel the graph toolbar opens: four tabs for how the map is laid out (X Axis, Y Axis, Size, Advanced).

#### Layout settings panel
The right column opened by the graph toolbar: four tabs (X Axis, Y Axis, Size, Advanced) with a close button, then option cards, and Reset to defaults at the foot. Read as `layout-panel` on the search map view (layout settings, X Axis), search map view (layout settings, Y Axis), search map view (layout settings, Size) and 1 more.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| x-axis | size 390 x 772; padding 8px `{spacing.2}`; background transparent; text Plus Jakarta Sans 14/14 600, #ffffff `{text.inverse}`; icon 16 x 16, #000000 `{text.default}` |
| y-axis (as the first row, except) | text Plus Jakarta Sans 14/14 400, #000000 `{text.default}` |
| size (as the first row, except) | text Plus Jakarta Sans 14/14 400, #000000 `{text.default}` |
| advanced (as the first row, except) | text Plus Jakarta Sans 14/14 400, #000000 `{text.default}` |

Child layers that carry the look: div 51.2x27 background #000000 `{action.primary}` radius 3px; div 374x91 border 1px solid #8a92a1 `{border.line}` radius 6px; div 374x91 border 1px solid #8a92a1 `{border.line}` radius 6px.

Parts:

- tabs: 342 x 30; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; gap 4px `{spacing.1}`; text "X Axis Y Axis Size Advanced"

![Layout settings panel x-axis](components/crops/layout-panel-x-axis.png) ![Layout settings panel y-axis](components/crops/layout-panel-y-axis.png) ![Layout settings panel size](components/crops/layout-panel-size.png) ![Layout settings panel advanced](components/crops/layout-panel-advanced.png)

#### Layout tabs
Text tabs across the top of the panel; the current tab is a black pill with white text. Read as `layout-tabs` on the search map view (layout settings, X Axis), search map view (layout settings, Y Axis).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 342 x 30; gap 4px `{spacing.1}`; background transparent; text Plus Jakarta Sans 14/14 600, #ffffff `{text.inverse}` |
| y-axis (as the first row, except) | text Plus Jakarta Sans 14/14 400, #000000 `{text.default}` |

Child layers that carry the look: div 51.2x27 background #000000 `{action.primary}` radius 3px.

Parts:

- container: 342 x 30; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; gap 4px `{spacing.1}`; text "X Axis Y Axis Size Advanced"
  - child X Axis: 51.17 x 27; at 0, 0; Plus Jakarta Sans 14/21 400, #ffffff `{text.inverse}`; background #000000 `{action.primary}`; radius 3px `{radius.xs}`; padding 3px 6px; margin 0px 3px 3px 0px; text "X Axis"
  - child X Axis: 39.17 x 18; at 6, 4; Plus Jakarta Sans 14/14 600, #ffffff `{text.inverse}`; text "X Axis"
  - child Y Axis: 49.39 x 27; at 58.2, 0; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; radius 3px `{radius.xs}`; padding 3px 6px; margin 0px 3px 3px 0px; text "Y Axis"
  - child Y Axis: 37.39 x 18; at 64.2, 4; Plus Jakarta Sans 14/14 400, #000000 `{text.default}`; text "Y Axis"
  - child Size: 39.16 x 27; at 114.6, 0; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; radius 3px `{radius.xs}`; padding 3px 6px; margin 0px 3px 3px 0px; text "Size"
  - child Size: 27.16 x 18; at 120.6, 4; Plus Jakarta Sans 14/14 400, #000000 `{text.default}`; text "Size"
  - child Advanced: 79.53 x 27; at 160.7, 0; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; radius 3px `{radius.xs}`; padding 3px 6px; margin 0px 3px 3px 0px; text "Advanced"
  - child Advanced: 67.53 x 18; at 166.7, 4; Plus Jakarta Sans 14/14 400, #000000 `{text.default}`; text "Advanced"

![Layout tabs default](components/crops/layout-tabs-default.png) ![Layout tabs y-axis](components/crops/layout-tabs-y-axis.png)

#### Layout tab
One tab, current and not current. Read as `layout-tab` on the search map view (layout settings, X Axis).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| current | size 51.17 x 27; padding 3px 6px; radius 3px `{radius.xs}`; background #000000 `{action.primary}`; text Plus Jakarta Sans 14/14 600, #ffffff `{text.inverse}`; cursor pointer |
| current, hover | opacity 0.8 |
| other (as the first row, except) | size 49.39 x 27; background transparent; text Plus Jakarta Sans 14/14 400, #000000 `{text.default}` |
| other, hover | opacity 0.8 |

- Not measured: focus could not be captured on current (not focusable, or focused without matching :focus-visible).
- Not measured: focus could not be captured on other (not focusable, or focused without matching :focus-visible).

Parts:

- label: 39.17 x 18; Plus Jakarta Sans 14/14 600, #ffffff `{text.inverse}`; text "X Axis"

Authored state rules (from the page's CSS): `.x:hover { opacity: 0.8; }`.

![Layout tab current](components/crops/layout-tab-current.png) ![Layout tab current-hover](components/crops/layout-tab-current-hover.png) ![Layout tab other](components/crops/layout-tab-other.png) ![Layout tab other-hover](components/crops/layout-tab-other-hover.png)

#### Layout panel close button
X at the top right of the panel. Read as `layout-close` on the search map view (layout settings, X Axis).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 32 x 24 (height `{size.control-sm}`); padding 4px 8px `{spacing.1} {spacing.2}`; radius 4px `{radius.sm}`; background transparent; text Plus Jakarta Sans 14/21 500, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(0, 0, 0, 0.05); }`.

![Layout panel close button default](components/crops/layout-close-default.png) ![Layout panel close button hover](components/crops/layout-close-hover.png) ![Layout panel close button focus-visible](components/crops/layout-close-focus-visible.png)

#### Layout option card
A bordered card per choice (for the Y axis: Cite Count, Ref Count, Publication Date). The chosen card is tinted blue, shows a tick and opens its sub-settings; the others are white with a hint line. Read as `layout-option` on the search map view (layout settings, X Axis), search map view (layout settings, Y Axis), search map view (layout settings, Size).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| chosen | size 374 x 190; padding 12px `{spacing.3}`; border 1px solid #8a92a1 `{border.line}`; radius 6px `{radius.md}`; background #e9f5fe `{component.option-selected}`; text Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; icon 14 x 14, #000000 `{text.default}` |
| other | size 374 x 91; padding 12px `{spacing.3}`; border 1px solid #8a92a1 `{border.line}`; radius 6px `{radius.md}`; background transparent; text Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; cursor pointer |
| other, hover | background #e9f5fe `{component.option-selected}` |
| x-chosen (as the first row, except) | size 374 x 140 |
| size-chosen (same as the first row) | same values |

Parts:

- header: 348 x 21; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; text "Cite Count"
- hint: 348 x 36; Plus Jakarta Sans 12/18 400 italic, #000000 `{text.default}`; text "Articles with a high citation "
- label: 85.52 x 21; Plus Jakarta Sans 14/21 400, #686d79 `{text.secondary}`; margin 8px 0px `{spacing.2} {spacing.0}`; text "Interpolation"

Authored state rules (from the page's CSS): `.x:hover { background-color: var(--selection-light); }`; `.x:hover { background-color: var(--selection); }`.

![Layout option card chosen](components/crops/layout-option-chosen.png) ![Layout option card other](components/crops/layout-option-other.png) ![Layout option card other-hover](components/crops/layout-option-other-hover.png) ![Layout option card x-chosen](components/crops/layout-option-x-chosen.png) ![Layout option card size-chosen](components/crops/layout-option-size-chosen.png)

#### Layout select
Grey rounded select with a chevron ("Logarithmic", "4"). Read as `layout-select` on the search map view (layout settings, Y Axis), search map view (layout settings, Advanced).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 119.59 x 29; padding 4px 8px `{spacing.1} {spacing.2}`; gap 8px `{spacing.2}`; radius 4px `{radius.sm}`; background rgba(0, 0, 0, 0.05) `{action.quiet}`; text Plus Jakarta Sans 14/14 400, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| hover | background rgba(0, 0, 0, 0.07) `{action.select-hover}` |
| focus-visible | shadow #000000 0px 0px 0px 2px; outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| small (as the first row, except) | size 48.83 x 29 |
| small, hover | background rgba(0, 0, 0, 0.07) `{action.select-hover}` |
| advanced (as the first row, except) | size 85.86 x 29 |
| advanced, hover | background rgba(0, 0, 0, 0.07) `{action.select-hover}` |

Parts:

- value: 79.59 x 21; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; text "Logarithmic"

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(0, 0, 0, 0.07); }`; `.x:focus { box-shadow: black 0px 0px 0px 2px; }`.

![Layout select default](components/crops/layout-select-default.png) ![Layout select hover](components/crops/layout-select-hover.png) ![Layout select focus-visible](components/crops/layout-select-focus-visible.png) ![Layout select small](components/crops/layout-select-small.png) ![Layout select small-hover](components/crops/layout-select-small-hover.png) ![Layout select advanced](components/crops/layout-select-advanced.png) ![Layout select advanced-hover](components/crops/layout-select-advanced-hover.png)

#### Layout toggle
Checkbox-like 20px button for the on and off options (Compact, Reverse). Read as `layout-toggle` on the search map view (layout settings, X Axis).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| checked (same: hover) | size 20 x 20; border 1px solid #686d79 `{border.drawer}`; radius 4px `{radius.sm}`; background transparent; text Plus Jakarta Sans 18/27 400, #000000 `{text.default}`; cursor pointer; icon 18 x 18, #000000 `{text.default}` |
| checked, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| unchecked (same: hover) (as the first row, except) | icon none |
| unchecked, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Layout toggle checked](components/crops/layout-toggle-checked.png) ![Layout toggle checked-hover](components/crops/layout-toggle-checked-hover.png) ![Layout toggle checked-focus-visible](components/crops/layout-toggle-checked-focus-visible.png) ![Layout toggle unchecked](components/crops/layout-toggle-unchecked.png) ![Layout toggle unchecked-hover](components/crops/layout-toggle-unchecked-hover.png) ![Layout toggle unchecked-focus-visible](components/crops/layout-toggle-unchecked-focus-visible.png)

#### Setting help icon
Small question-mark icon beside a setting label. Read as `layout-help` on the search map view (layout settings, Y Axis).

**Values (default).** size 14 x 14; background transparent; text Plus Jakarta Sans 14/21 400, #686d79 `{text.secondary}`; icon 14 x 14, #686d79 `{text.secondary}`.

![Setting help icon default](components/crops/layout-help-default.png) ![Setting help icon hover](components/crops/layout-help-hover.png)

#### Reset to defaults button
Plain text button at the foot of the layout panel. Read as `layout-reset` on the search map view (layout settings, X Axis).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 129.23 x 29; padding 4px 8px `{spacing.1} {spacing.2}`; radius 4px `{radius.sm}`; background transparent; text Plus Jakarta Sans 14/21 500, #000000 `{text.default}`; opacity 0.4 |
| hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |

- Not measured: focus could not be captured on the component (not focusable, or focused without matching :focus-visible).

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(0, 0, 0, 0.05); }`.

![Reset to defaults button default](components/crops/layout-reset-default.png) ![Reset to defaults button hover](components/crops/layout-reset-hover.png)

### Library

The Library page: a sidebar of lists and collections, a collection header, a selection bar, and the same list, split and map views as search.

#### Library sidebar
A 250px column of white cards: three fixed lists (Recently Found, All Articles, Reading List) with counts, then Collections with its tools and the folder list, then BibTeX and Zotero at the foot. Read as `library-sidebar` on the library map view.

**Values (default).** size 250 x 812; padding 0px 16px 0px 0px `{spacing.0} {spacing.4} {spacing.0} {spacing.0}`; background transparent; text Plus Jakarta Sans 14/14 400, #000000 `{text.default}`; icon 16 x 16, #000000 `{text.default}`.

Child layers that carry the look: div 234x34 background #ffffff `{background.surface}` radius 8px; div 24.7x18 background rgba(0, 0, 0, 0.05) `{action.quiet}` radius 48px; div 234x34 background #ffffff `{background.surface}` radius 8px.

![Library sidebar default](components/crops/library-sidebar-default.png)

#### Library list row
A fixed list entry with an icon, a name and a count badge. Read as `library-list-row` on the library map view, library, All Articles.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| recently-found (same: hover) | size 234 x 34; padding 8px `{spacing.2}`; radius 8px `{radius.lg}`; background #ffffff `{background.surface}`; text Plus Jakarta Sans 14/14 400, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| all-articles (same: hover) (same as the first row) | same values |
| reading-list (same: hover) (same as the first row) | same values |
| all-articles-current (same: pressed) (as the first row, except) | shadow #000000 0px 0px 0px 1px inset (`{elevation.ring-strong}`); text Plus Jakarta Sans 14/14 600, #000000 `{text.default}` |

- Not measured: focus could not be captured on recently-found (not focusable, or focused without matching :focus-visible).

Parts:

- title: 103.13 x 14; Plus Jakarta Sans 14/14 400, #000000 `{text.default}`; text "Recently Found"
- count: 24.7 x 18; Plus Jakarta Sans 12/18 500, #000000 `{text.default}`; background rgba(0, 0, 0, 0.05) `{action.quiet}`; radius 48px `{radius.pill}`; padding 0px 8px `{spacing.0} {spacing.2}`; text "0"

![Library list row recently-found](components/crops/library-list-row-recently-found.png) ![Library list row all-articles](components/crops/library-list-row-all-articles.png) ![Library list row reading-list](components/crops/library-list-row-reading-list.png) ![Library list row all-articles-current](components/crops/library-list-row-all-articles-current.png)

#### Collections heading
The "Collections" heading with three 24px tool buttons (sort, filter, add). Read as `library-collections-title` on the library map view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 88.44 x 24 (height `{size.control-sm}`); background transparent; text Plus Jakarta Sans 16/24 600, #000000 `{text.default}` |
| tool-sort | size 24 x 24 (height `{size.control-sm}`); padding 4px `{spacing.1}`; radius 24px `{radius.chip}`; background rgba(0, 0, 0, 0.05) `{action.quiet}`; text Plus Jakarta Sans 16/24 400, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| tool-sort, hover | background rgba(0, 0, 0, 0.08) `{action.quiet-hover-soft}` |
| tool-sort, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| tool-add | size 24 x 24 (height `{size.control-sm}`); padding 4px `{spacing.1}`; radius 24px `{radius.chip}`; background rgba(0, 0, 0, 0.05) `{action.quiet}`; text Plus Jakarta Sans 16/24 400, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| tool-add, hover | background rgba(0, 0, 0, 0.08) `{action.quiet-hover-soft}` |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(0, 0, 0, 0.08); }`.

![Collections heading default](components/crops/library-collections-title-default.png) ![Collections heading tool-sort](components/crops/library-collections-title-tool-sort.png) ![Collections heading tool-sort-hover](components/crops/library-collections-title-tool-sort-hover.png) ![Collections heading tool-sort-focus-visible](components/crops/library-collections-title-tool-sort-focus-visible.png) ![Collections heading tool-add](components/crops/library-collections-title-tool-add.png) ![Collections heading tool-add-hover](components/crops/library-collections-title-tool-add-hover.png)

#### Collection row
A collection in the sidebar: folder icon in the collection colour, name, and a hover chevron. The current collection has a black outline. Read as `library-folder` on the library map view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default (same: hover) | size 218 x 38; background transparent; text Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; icon 18 x 18, #f07d59 `{palette.ugc.amber}` |
| chevron | size 32 x 32 (height `{size.control-md}`); padding 8px `{spacing.2}`; radius 4px `{radius.sm}`; background transparent; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; opacity 0; transform matrix(1, 0, 0, 1, 0, -16); cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| chevron, hover | background rgba(0, 0, 0, 0.05) `{action.quiet}`; opacity none |
| chevron, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Child layers that carry the look: div 218x37 background #ffffff `{background.surface}` radius 4px; button 32x32 background #ffffff `{background.surface}` radius 4px; hr 218x1 border 1px solid #dde0e4 `{border.rule}`.

Parts:

- icon: 18 x 18
- label: 96.58 x 21; Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; margin 4px 0px `{spacing.1} {spacing.0}`; text "my-collection"
- overlay: 218 x 38; radius 8px `{radius.lg}`; shadow #000000 0px 0px 0px 1px inset (`{elevation.ring-strong}`)
- chevron: 16 x 16

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover .x { opacity: 1; }`; `.x:hover { background-color: rgba(0, 0, 0, 0.05); }`.

![Collection row default](components/crops/library-folder-default.png) ![Collection row hover](components/crops/library-folder-hover.png) ![Collection row chevron](components/crops/library-folder-chevron.png) ![Collection row chevron-hover](components/crops/library-folder-chevron-hover.png)

#### BibTeX and Zotero buttons
Two text buttons with icons at the foot of the sidebar (import). Read as `library-footer-button` on the library map view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| bibtex | size 93.95 x 32 (height `{size.control-md}`); padding 8px 12px `{spacing.2} {spacing.3}`; gap 8px `{spacing.2}`; radius 48px `{radius.pill}`; background transparent; text Plus Jakarta Sans 14/14 500, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| bibtex, hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| bibtex, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| zotero (as the first row, except) | size 93.13 x 32 (height `{size.control-md}`) |
| zotero, hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(0, 0, 0, 0.05); }`.

![BibTeX and Zotero buttons bibtex](components/crops/library-footer-button-bibtex.png) ![BibTeX and Zotero buttons bibtex-hover](components/crops/library-footer-button-bibtex-hover.png) ![BibTeX and Zotero buttons bibtex-focus-visible](components/crops/library-footer-button-bibtex-focus-visible.png) ![BibTeX and Zotero buttons zotero](components/crops/library-footer-button-zotero.png) ![BibTeX and Zotero buttons zotero-hover](components/crops/library-footer-button-zotero-hover.png)

#### Collection header
White banner: a 64px tile in the collection colour with a folder icon, the name, the article count, then Share, settings, add and Search from Collection at the right. Read as `collection-header` on the library map view.

**Values (default).** size 1142 x 92; radius 8px `{radius.lg}`; background #ffffff `{background.surface}`; text Plus Jakarta Sans 20/30 600, #000000 `{text.default}`; icon 32 x 32, #ffffff `{text.inverse}`.

Parts:

- tile: 64 x 92; background #f07d59 `{palette.ugc.amber}`; padding 16px `{spacing.4}`
- name: 137.95 x 30; Plus Jakarta Sans 20/30 600, #000000 `{text.default}`; text "my-collection"
- info: 69.95 x 12; Plus Jakarta Sans 12/18 400, #000000 `{text.default}`; gap 4px `{spacing.1}`; text "9 Articles"
- children: 1078 x 92; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; padding 16px 12px `{spacing.4} {spacing.3}`; gap 4px `{spacing.1}`; text "my-collection Share 9 Articles"

![Collection header default](components/crops/collection-header-default.png)

#### Share button
Peach pill button with a people icon. Read as `collection-share` on the library map view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default (same: hover) | size 72.94 x 24 (height `{size.control-sm}`); padding 4px 8px `{spacing.1} {spacing.2}`; gap 8px `{spacing.2}`; radius 48px `{radius.pill}`; background rgba(240, 125, 89, 0.2) `{component.folder-tint}`; text Plus Jakarta Sans 12/12 400, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Share button default](components/crops/collection-share-default.png) ![Share button focus-visible](components/crops/collection-share-focus-visible.png)

#### Collection icon button
24px round icon buttons beside Share: settings and add. Read as `collection-icon-button` on the library map view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| settings (same: hover) | size 24 x 24 (height `{size.control-sm}`); padding 4px `{spacing.1}`; radius 48px `{radius.pill}`; background rgba(240, 125, 89, 0.2) `{component.folder-tint}`; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| settings, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| add (same: hover) (same as the first row) | same values |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Collection icon button settings](components/crops/collection-icon-button-settings.png) ![Collection icon button settings-focus-visible](components/crops/collection-icon-button-settings-focus-visible.png) ![Collection icon button add](components/crops/collection-icon-button-add.png)

#### Search from Collection button
Black pill under the header buttons. Read as `collection-search-button` on the library map view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 156.97 x 26; padding 4px 12px `{spacing.1} {spacing.3}`; radius 48px `{radius.pill}`; background #000000 `{action.primary}`; text Plus Jakarta Sans 12/18 600, #ffffff `{text.inverse}`; cursor pointer |
| hover | background #333333 `{action.primary-hover}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: #333333; }`.

![Search from Collection button default](components/crops/collection-search-button-default.png) ![Search from Collection button hover](components/crops/collection-search-button-hover.png) ![Search from Collection button focus-visible](components/crops/collection-search-button-focus-visible.png)

#### Selection bar
A row under the header: Select all at the left, then Reading, Delete, Save, Export and Search, greyed until something is selected. Read as `selection-bar` on the library map view, library, All Articles, library, All Articles (one selected).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 1142 x 42; padding 8px 0px `{spacing.2} {spacing.0}`; background transparent; text Plus Jakarta Sans 12/12 400, #000000 `{text.default}`; icon 16 x 16, #000000 `{text.default}` |
| select-all | size 67.53 x 20; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; radius 24px `{radius.chip}`; background transparent; text Plus Jakarta Sans 12/12 400, #000000 `{text.default}`; cursor pointer |
| select-all, hover | background rgba(255, 255, 255, 0.5) `{background.panel-glass}` |
| select-all, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| select-all, pressed | background rgba(255, 255, 255, 0.5) `{background.panel-glass}` |
| action (same: hover) | size 83.31 x 26; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; radius 24px `{radius.chip}`; background transparent; text Plus Jakarta Sans 12/18 500, #000000 `{text.default}`; opacity 0.4; icon 16 x 16, #000000 `{text.default}` |
| one-selected (as the first row, except) | text Plus Jakarta Sans 12/12 600, #000000 `{text.default}` |
| action-enabled (same: hover, pressed) | size 74.42 x 26; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; radius 24px `{radius.chip}`; background transparent; text Plus Jakarta Sans 12/18 500, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| action-enabled, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

- Not measured: focus could not be captured on action (not focusable, or focused without matching :focus-visible).

Parts:

- container: 1142 x 42; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; padding 8px 0px `{spacing.2} {spacing.0}`; text "Select all Reading Delete Save"
  - child Select all: 67.53 x 20; at 0, 11; Plus Jakarta Sans 12/18 400, #000000 `{text.default}`; radius 24px `{radius.chip}`; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; text "Select all"
  - child Reading: 83.31 x 26; at 757.6, 8; Plus Jakarta Sans 12/18 500, #000000 `{text.default}`; radius 24px `{radius.chip}`; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; opacity 0.4; text "Reading"
  - child Delete: 74.42 x 26; at 849, 8; Plus Jakarta Sans 12/18 500, #000000 `{text.default}`; radius 24px `{radius.chip}`; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; opacity 0.4; text "Delete"
  - child Save: 64 x 26; at 931.4, 8; Plus Jakarta Sans 12/18 500, #000000 `{text.default}`; radius 24px `{radius.chip}`; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; opacity 0.4; text "Save"
  - child Export: 74.3 x 26; at 1003.4, 8; Plus Jakarta Sans 12/18 500, #000000 `{text.default}`; radius 24px `{radius.chip}`; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; opacity 0.4; text "Export"
  - child Search: 56.33 x 26; at 1085.7, 8; Plus Jakarta Sans 12/18 500, #000000 `{text.default}`; radius 24px `{radius.chip}`; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; opacity 0.4; text "Search"

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(255, 255, 255, 0.5); }`.

![Selection bar default](components/crops/selection-bar-default.png) ![Selection bar select-all](components/crops/selection-bar-select-all.png) ![Selection bar select-all-hover](components/crops/selection-bar-select-all-hover.png) ![Selection bar select-all-focus-visible](components/crops/selection-bar-select-all-focus-visible.png) ![Selection bar action](components/crops/selection-bar-action.png) ![Selection bar select-all-pressed](components/crops/selection-bar-select-all-pressed.png) ![Selection bar one-selected](components/crops/selection-bar-one-selected.png) ![Selection bar action-enabled](components/crops/selection-bar-action-enabled.png)

#### Library filter bar
Grey row inside the list card: "Showing 9 Articles" at the left, then sort, filter, search and the four view buttons at the right. Read as `filter-bar` on the library map view, library list view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 1126 x 24 (height `{size.control-sm}`); gap 8px `{spacing.2}`; background transparent; text Plus Jakarta Sans 12/18 400 italic, #686d79 `{text.secondary}`; icon 16 x 16, #000000 `{text.default}` |
| map (same as the first row) | same values |

Child layers that carry the look: button 24x24 background rgba(0, 0, 0, 0.05) `{action.quiet}` radius 48px; button 24x24 background rgba(0, 0, 0, 0.05) `{action.quiet}` radius 48px; input 24x24 background rgba(0, 0, 0, 0.05) `{action.quiet}` radius 48px.

Parts:

- container: 1126 x 24; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; gap 8px `{spacing.2}`; text "Showing 9 Articles Label"
  - child Showing 9 Articles: 103.73 x 18; at 0, 3; Plus Jakarta Sans 12/18 400 italic, #686d79 `{text.secondary}`; text "Showing 9 Articles"
  - child Label: 24 x 24; at 934, 0; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; background rgba(0, 0, 0, 0.05) `{action.quiet}`; radius 48px `{radius.pill}`; padding 4px `{spacing.1}`; gap 8px `{spacing.2}`; text "Label"
  - child svg: 16 x 16; at 938, 4
  - child svg: 16 x 16; at 945.5, 25.5
  - child button: 24 x 24; at 962, 0; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; background rgba(0, 0, 0, 0.05) `{action.quiet}`; radius 48px `{radius.pill}`; padding 4px `{spacing.1}`
  - child svg: 16 x 16; at 966, 4
  - child input: 24 x 24; at 990, 0; Plus Jakarta Sans 14/14 400, #000000 `{text.default}`; background rgba(0, 0, 0, 0.05) `{action.quiet}`; radius 48px `{radius.pill}`; padding 4px 12px `{spacing.1} {spacing.3}`
  - child svg: 16 x 16; at 994, 4
  - child button: 24 x 24; at 1030, 0; Plus Jakarta Sans 16/24 400, #ffffff `{text.inverse}`; background #000000 `{action.primary}`; padding 4px `{spacing.1}`
  - child svg: 16 x 16; at 1034, 4

![Library filter bar default](components/crops/filter-bar-default.png) ![Library filter bar map](components/crops/filter-bar-map.png)

#### Library filter bar controls
The sort select, the filter button, the search field and the view buttons (current and not). Read as `filter-bar-button` on the library list view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| sort | size 24 x 24 (height `{size.control-sm}`); padding 4px `{spacing.1}`; gap 8px `{spacing.2}`; radius 48px `{radius.pill}`; background rgba(0, 0, 0, 0.05) `{action.quiet}`; text Plus Jakarta Sans 14/14 400, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| sort, hover | background rgba(0, 0, 0, 0.07) `{action.select-hover}` |
| sort, focus-visible | shadow #000000 0px 0px 0px 2px; outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| filter | size 156.97 x 26; padding 4px 12px `{spacing.1} {spacing.3}`; radius 48px `{radius.pill}`; background #000000 `{action.primary}`; text Plus Jakarta Sans 12/18 600, #ffffff `{text.inverse}`; cursor pointer |
| filter, hover | background #333333 `{action.primary-hover}` |
| filter, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| search (same: hover) | size 24 x 24 (height `{size.control-sm}`); padding 4px 12px `{spacing.1} {spacing.3}`; radius 48px `{radius.pill}`; background rgba(0, 0, 0, 0.05) `{action.quiet}`; text Plus Jakarta Sans 14/14 400, #000000 `{text.default}`; cursor text; placeholder oklab(0 0 0 / 0.5) |
| search, focus-visible | size 200 x 24 (height `{size.control-sm}`); padding 4px 12px 4px 24px `{spacing.1} {spacing.3} {spacing.1} {spacing.6}`; outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| view-current | size 24 x 24 (height `{size.control-sm}`); padding 4px `{spacing.1}`; background #000000 `{action.primary}`; text Plus Jakarta Sans 16/24 400, #ffffff `{text.inverse}`; cursor pointer; icon 16 x 16, #ffffff `{text.inverse}` |
| view-current, hover | background #333333 `{action.primary-hover}` |
| view-current, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| view-other (as the first row, except) | gap none; radius none; text Plus Jakarta Sans 16/24 400, #000000 `{text.default}` |
| view-other, hover | background rgba(0, 0, 0, 0.1) `{action.quiet-hover}` |
| view-other, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(0, 0, 0, 0.07); }`; `.x:focus { box-shadow: black 0px 0px 0px 2px; }`.

![Library filter bar controls sort](components/crops/filter-bar-button-sort.png) ![Library filter bar controls sort-hover](components/crops/filter-bar-button-sort-hover.png) ![Library filter bar controls sort-focus-visible](components/crops/filter-bar-button-sort-focus-visible.png) ![Library filter bar controls filter](components/crops/filter-bar-button-filter.png) ![Library filter bar controls search](components/crops/filter-bar-button-search.png) ![Library filter bar controls search-focus-visible](components/crops/filter-bar-button-search-focus-visible.png) ![Library filter bar controls view-current](components/crops/filter-bar-button-view-current.png) ![Library filter bar controls view-current-hover](components/crops/filter-bar-button-view-current-hover.png) ![Library filter bar controls view-current-focus-visible](components/crops/filter-bar-button-view-current-focus-visible.png) ![Library filter bar controls view-other](components/crops/filter-bar-button-view-other.png) ![Library filter bar controls view-other-hover](components/crops/filter-bar-button-view-other-hover.png) ![Library filter bar controls view-other-focus-visible](components/crops/filter-bar-button-view-other-focus-visible.png)

### Home

The home page: a hero with a search field, then three white cards (recent articles, collections, getting started).

#### Home hero
An illustration at the left, then a heading, a subtitle, a wide search field with its Search button, a tip line and Browse Library. Read as `home-hero` on the home page.

**Values (default).** size 1042 x 171; gap 4px `{spacing.1}`; background transparent; text Plus Jakarta Sans 32/48 600, #000000 `{text.default}`; icon 20 x 20, #ffffff `{text.inverse}`.

Child layers that carry the look: form 853.5x53 background #000000 `{action.primary}` radius 36px; button 71.4x37 background #d1ceed `{action.accent}` radius 48px; button 142.5x34 background #ffffff `{background.surface}` border 1px solid #686d79 `{border.drawer}` radius 48px.

Parts:

- title: 1042 x 48; Plus Jakarta Sans 32/48 600, #000000 `{text.default}`; text "Follow your curiosity"
- subtitle: 1042 x 30; Plus Jakarta Sans 20/30 500, #000000 `{text.default}`; text "Jump from what you know, to wh"
- bar: 853.48 x 53; Plus Jakarta Sans 14/21 400, #ffffff `{text.inverse}`; background #000000 `{action.primary}`; radius 36px `{radius.search}`; text "Search"
- tip: 853.48 x 12; Plus Jakarta Sans 12/12 400, #000000 `{text.default}`; text "Search for new articles using "
- or: 14.06 x 14; Plus Jakarta Sans 14/14 500, #000000 `{text.default}`; text "or"

![Home hero default](components/crops/home-hero-default.png)

#### Home search field
The 53px search input with a magnifier icon. Read as `home-search-field` on the home page, home page (a query typed, not sent).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default (same: hover) | size 853.48 x 53; padding 16px 72px 16px 48px; radius 48px `{radius.pill}`; background transparent; text Plus Jakarta Sans 14/21 400, #ffffff `{text.inverse}`; cursor text; placeholder #ffffff `{text.inverse}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| typed (same as the first row) | same values |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Home search field default](components/crops/home-search-field-default.png) ![Home search field focus-visible](components/crops/home-search-field-focus-visible.png) ![Home search field typed](components/crops/home-search-field-typed.png)

#### Home Search button
Black pill inside the right end of the field. Read as `home-search-button` on the home page, home page (2026-10-17).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default (same: hover, pressed) | size 71.41 x 37 (height `{size.field}`); padding 8px 12px `{spacing.2} {spacing.3}`; radius 48px `{radius.pill}`; background #d1ceed `{action.accent}`; text Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; cursor pointer |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Home Search button default](components/crops/home-search-button-default.png) ![Home Search button focus-visible](components/crops/home-search-button-focus-visible.png) ![Home Search button pressed](components/crops/home-search-button-pressed.png)

#### Browse Library button
Light pill with a library icon next to the field. Read as `home-browse-library` on the home page, home page (2026-10-17).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 142.45 x 34; padding 8px `{spacing.2}`; gap 12px `{spacing.3}`; border 1px solid #686d79 `{border.drawer}`; radius 48px `{radius.pill}`; background #ffffff `{background.surface}`; text Plus Jakarta Sans 14/14 600, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| hover | background rgba(255, 255, 255, 0.9) `{action.glass-hover}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| pressed | background rgba(255, 255, 255, 0.9) `{action.glass-hover}` |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(255, 255, 255, 0.9); }`.

![Browse Library button default](components/crops/home-browse-library-default.png) ![Browse Library button hover](components/crops/home-browse-library-hover.png) ![Browse Library button focus-visible](components/crops/home-browse-library-focus-visible.png) ![Browse Library button pressed](components/crops/home-browse-library-pressed.png)

#### Home section card
Three white cards: recent articles, your collections and getting started. Each has a header with title and description. Read as `home-section` on the home page.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| recent | size 440 x 500; padding 12px `{spacing.3}`; gap 4px `{spacing.1}`; radius 8px `{radius.lg}`; background rgba(255, 255, 255, 0.4) `{background.section}`; text Plus Jakarta Sans 16/24 600, #000000 `{text.default}`; icon 16 x 16, #f07d59 `{palette.ugc.amber}` |
| collections (same as the first row) | same values |
| guides (as the first row, except) | size 440 x 901; icon 14 x 14, #000000 `{text.default}` |

Parts:

- header: 416 x 53; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; padding 4px 8px `{spacing.1} {spacing.2}`; text "Recently saved Dive deeper on "
- title: 400 x 24; Plus Jakarta Sans 16/24 600, #000000 `{text.default}`; text "Recently saved"
- desc: 400 x 21; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; text "Dive deeper on your new finds"

![Home section card recent](components/crops/home-section-recent.png) ![Home section card collections](components/crops/home-section-collections.png) ![Home section card guides](components/crops/home-section-guides.png)

#### Compact article row
A row in the recent lists: author and year, folder icon, a one-line title and two 36px buttons at the right (search from this article, open). Read as `home-article-row` on the home page.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 332 x 47; padding 4px 8px `{spacing.1} {spacing.2}`; background transparent; text Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; icon 16 x 16, #f07d59 `{palette.ugc.amber}` |
| hover | cursor pointer |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| side-button (same: hover) | size 36 x 47; padding 8px `{spacing.2}`; background transparent; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; cursor pointer; icon 18 x 18, #000000 `{text.default}` |
| side-button, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Parts:

- nickname: 76.14 x 21; Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; text "Feng, 2026"
- folders: 16 x 16; gap 4px `{spacing.1}`
- title: 316 x 18; Plus Jakarta Sans 12/18 400, #000000 `{text.default}`; text "LongCLI-Bench: A Preliminary B"

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { cursor: pointer; }`.

![Compact article row default](components/crops/home-article-row-default.png) ![Compact article row hover](components/crops/home-article-row-hover.png) ![Compact article row focus-visible](components/crops/home-article-row-focus-visible.png) ![Compact article row side-button](components/crops/home-article-row-side-button.png) ![Compact article row side-button-hover](components/crops/home-article-row-side-button-hover.png) ![Compact article row side-button-focus-visible](components/crops/home-article-row-side-button-focus-visible.png)

#### Home collection row
A collection link with a folder icon in its colour and an arrow. Read as `home-folder-row` on the home page.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 416 x 40 (height `{size.control-lg}`); padding 8px `{spacing.2}`; gap 12px `{spacing.3}`; radius 8px `{radius.lg}`; background #ffffff `{background.surface}`; text Plus Jakarta Sans 16/24 500, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #f07d59 `{palette.ugc.amber}` |
| hover | background rgba(255, 255, 255, 0.5) `{background.panel-glass}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Parts:

- icon: 16 x 16
- label: 108.83 x 24; Plus Jakarta Sans 16/24 500, #000000 `{text.default}`; text "my-collection"
- arrow: 16 x 16; opacity 0

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { text-decoration: none; background-color: rgba(255, 255, 255, 0.5); }`.

![Home collection row default](components/crops/home-folder-row-default.png) ![Home collection row hover](components/crops/home-folder-row-hover.png) ![Home collection row focus-visible](components/crops/home-folder-row-focus-visible.png)

#### Guide card
A linked card with a 180px image over a title and a short description. Read as `home-guide-card` on the home page.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 416 x 275; radius 16px `{radius.2xl}`; background #ffffff `{background.surface}`; text Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; cursor pointer; icon 14 x 14, #000000 `{text.default}` |
| hover | shadow #000000 0px 0px 0px 1px |
| focus-visible | outline 1px auto #005fcc `{border.focus-browser}`, offset 1px |

Parts:

- image: 416 x 180; background #e8e7f6 `{action.accent-soft}`
- body: 416 x 95; Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; padding 16px `{spacing.4}`; text "Get started in 2 minutes Learn"
- title: 158.92 x 21; Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; text "Get started in 2 minutes"
- desc: 384 x 42; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; text "Learn about how ResearchRabbit"

Authored state rules (from the page's CSS): `a:hover { text-decoration: underline; }`; `.x:hover { box-shadow: black 0px 0px 0px 1px; }`.

![Guide card default](components/crops/home-guide-card-default.png) ![Guide card hover](components/crops/home-guide-card-hover.png) ![Guide card focus-visible](components/crops/home-guide-card-focus-visible.png)

### Dialogs

Read on 2026-10-17. Account Settings, a form dialog stacked on it, the destructive confirmation and the loading dialog all use one modal: a white sheet over a teal-grey scrim.

#### Dialog
Every dialog is one white sheet centred over a teal-grey scrim: 16px corners, a 1px rule under a 24px title, and a close button at the top right. Account Settings is 650 x 600 with a 180px tab column; Update profile opens a second dialog over the first; the loader is the same sheet with only a message and a spinner. Read as `dialog` on the Account Settings dialog (Profile), Update profile dialog, keyword search results (updating dialog) and 1 more.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| account-settings | size 650 x 600; radius 16px `{radius.2xl}`; background #ffffff `{background.surface}`; shadow rgba(0, 0, 0, 0.5) 3px 3px 12px 0px (`{elevation.dialog}`); text Plus Jakarta Sans 24/36 400, #000000 `{text.default}`; transform matrix(1, 0, 0, 1, -325, -300); icon 16 x 16, #000000 `{text.default}` |
| form (as the first row, except) | size 500 x 329; transform matrix(1, 0, 0, 1, -250, -164.5) |
| loading (as the first row, except) | size 272.16 x 130; padding 32px `{spacing.8}`; transform matrix(1, 0, 0, 1, -136.078, -65); icon 16.91 x 16.91, #000000 `{text.default}` |
| cite (as the first row, except) | size 550 x 374; transform matrix(1, 0, 0, 1, -275, -187) |

Parts:

- head: 650 x 77; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; padding 20px `{spacing.5}`; border B:1px solid #c9cdd3 `{border.default}`; text "Account Settings"
- title: 578 x 36; Plus Jakarta Sans 24/36 400, #000000 `{text.default}`; text "Account Settings"
- body: 650 x 523; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; text "Profile Preferences Subscripti"

![Dialog account-settings](components/crops/dialog-account-settings.png) ![Dialog form](components/crops/dialog-form.png) ![Dialog loading](components/crops/dialog-loading.png) ![Dialog cite](components/crops/dialog-cite.png)

#### Dialog scrim
The full-screen overlay behind every dialog. A second dialog adds a second overlay, so the page darkens twice. Read as `dialog-scrim` on the Account Settings dialog (Profile), Update profile dialog.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 1440 x 900; background rgba(48, 85, 94, 0.3) `{background.scrim}`; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}` |
| stacked (same as the first row) | same values |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Dialog close button
Round 32px button with a 24px cross. Read as `dialog-close` on the Account Settings dialog (Profile).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 32 x 32 (height `{size.control-md}`); padding 8px `{spacing.2}`; radius 100%; background transparent; text Plus Jakarta Sans 24/36 400, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| pressed | background rgba(0, 0, 0, 0.05) `{action.quiet}` |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(0, 0, 0, 0.05); }`.

![Dialog close button default](components/crops/dialog-close-default.png) ![Dialog close button hover](components/crops/dialog-close-hover.png) ![Dialog close button focus-visible](components/crops/dialog-close-focus-visible.png) ![Dialog close button pressed](components/crops/dialog-close-pressed.png)

#### Destructive confirmation
Delete Account: a sentence of warning, then a pale yellow box asking for a typed phrase, then a pale red "Permanently Delete My Account" button that stays disabled until the phrase matches, and a plain Cancel. Opened and cancelled; nothing was typed. Read as `confirm-destructive` on the Delete Account confirmation.

**Values (default).** size 500 x 340; radius 16px `{radius.2xl}`; background #ffffff `{background.surface}`; shadow rgba(0, 0, 0, 0.5) 3px 3px 12px 0px (`{elevation.dialog}`); text Plus Jakarta Sans 24/36 400, #000000 `{text.default}`; transform matrix(1, 0, 0, 1, -250, -170); icon 16 x 16, #000000 `{text.default}`.

Parts:

- content: 500 x 263; Plus Jakarta Sans 16/24 400, #000000 `{text.default}`; padding 16px `{spacing.4}`; gap 8px `{spacing.2}`; text "Are you really, really sure? T"
- safeguard: 468 x 93; Plus Jakarta Sans 16/24 400, #000000 `{text.default}`; background #fef1c5 `{status.warning.fill}`; radius 8px `{radius.lg}`; padding 12px `{spacing.3}`; gap 8px `{spacing.2}`; text "Type Delete my account below t"

![Destructive confirmation default](components/crops/confirm-destructive-default.png)

#### Typed-phrase box
The yellow box in the destructive confirmation, with the phrase in bold and an empty 5% black input. Read as `confirm-safeguard` on the Delete Account confirmation.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 468 x 93; padding 12px `{spacing.3}`; gap 8px `{spacing.2}`; radius 8px `{radius.lg}`; background #fef1c5 `{status.warning.fill}`; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}` |
| input (same: hover) | size 444 x 40 (height `{size.control-lg}`); padding 8px `{spacing.2}`; radius 4px `{radius.sm}`; background rgba(0, 0, 0, 0.05) `{action.quiet}`; text Plus Jakarta Sans 16/24 400, #000000 `{text.default}`; cursor text; placeholder #000000 `{text.default}` |
| input, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Typed-phrase box default](components/crops/confirm-safeguard-default.png) ![Typed-phrase box input](components/crops/confirm-safeguard-input.png) ![Typed-phrase box input-focus-visible](components/crops/confirm-safeguard-input-focus-visible.png)

### Buttons

Read on 2026-10-17. The button kinds outside the search chrome: the black primary, the text-only secondary, the pale red destructive button, disabled buttons, and text buttons. Pressed is the mouse held down; no captured rule styles `:active` except the slider thumb's cursor, so a pressed button keeps its hover fill.

#### Primary button
Black rectangle with white text and 8px corners ("Done" in a dialog, "Search for Articles" in an empty state). Read as `button-primary` on the Update profile dialog, library, Reading List (empty).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 81.42 x 56 (height `{size.control-xl}`); padding 16px 20px `{spacing.4} {spacing.5}`; radius 8px `{radius.lg}`; background #000000 `{action.primary}`; text Plus Jakarta Sans 16/24 500, #ffffff `{text.inverse}`; cursor pointer |
| hover | background #333333 `{action.primary-hover}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| pressed | background #333333 `{action.primary-hover}` |
| empty-state (as the first row, except) | size 179.28 x 56 (height `{size.control-xl}`) |
| empty-state, hover | background #333333 `{action.primary-hover}` |
| empty-state, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| empty-state, pressed | background #333333 `{action.primary-hover}` |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: #333333; }`.

![Primary button default](components/crops/button-primary-default.png) ![Primary button hover](components/crops/button-primary-hover.png) ![Primary button focus-visible](components/crops/button-primary-focus-visible.png) ![Primary button pressed](components/crops/button-primary-pressed.png) ![Primary button empty-state](components/crops/button-primary-empty-state.png) ![Primary button empty-state-hover](components/crops/button-primary-empty-state-hover.png) ![Primary button empty-state-focus-visible](components/crops/button-primary-empty-state-focus-visible.png) ![Primary button empty-state-pressed](components/crops/button-primary-empty-state-pressed.png)

#### Secondary button
Text only, the same height as the primary beside it ("Cancel"). Read as `button-secondary` on the Update profile dialog, Delete Account confirmation.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 94.03 x 56 (height `{size.control-xl}`); padding 16px 20px `{spacing.4} {spacing.5}`; radius 8px `{radius.lg}`; background transparent; text Plus Jakarta Sans 16/24 500, #000000 `{text.default}`; cursor pointer |
| hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| pressed | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| confirm (same as the first row) | same values |
| confirm, hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| confirm, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| confirm, pressed | background rgba(0, 0, 0, 0.05) `{action.quiet}` |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(0, 0, 0, 0.05); }`.

![Secondary button default](components/crops/button-secondary-default.png) ![Secondary button hover](components/crops/button-secondary-hover.png) ![Secondary button focus-visible](components/crops/button-secondary-focus-visible.png) ![Secondary button pressed](components/crops/button-secondary-pressed.png) ![Secondary button confirm](components/crops/button-secondary-confirm.png) ![Secondary button confirm-hover](components/crops/button-secondary-confirm-hover.png) ![Secondary button confirm-focus-visible](components/crops/button-secondary-confirm-focus-visible.png) ![Secondary button confirm-pressed](components/crops/button-secondary-confirm-pressed.png)

#### Danger button
The destructive action in the confirmation. Seen only disabled: the phrase was never typed. Read as `button-danger` on the Delete Account confirmation.

**Values (disabled).** size 283.66 x 56 (height `{size.control-xl}`); padding 16px 20px `{spacing.4} {spacing.5}`; radius 8px `{radius.lg}`; background #f2af97 `{action.danger}`; text Plus Jakarta Sans 16/24 500, #000000 `{text.default}`; opacity 0.4.

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: var(--peach-50); }`.

![Danger button disabled](components/crops/button-danger-disabled.png)

#### Disabled buttons
Buttons with the disabled attribute: Reset Tutorials in Preferences, and the selection actions above an article list until something is selected. Read as `button-disabled` on the Account Settings dialog (Preferences), library, All Articles.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| reset-tutorials | size 422 x 37 (height `{size.field}`); padding 8px 12px `{spacing.2} {spacing.3}`; radius 8px `{radius.lg}`; background transparent; shadow #c9cdd3 0px 0px 0px 1px inset (`{elevation.ring-field}`); text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; opacity 0.5 |
| reset-tutorials, hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| toolbar (same: hover) | size 74.42 x 26; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; radius 24px `{radius.chip}`; background transparent; text Plus Jakarta Sans 12/18 500, #000000 `{text.default}`; opacity 0.4; icon 16 x 16, #000000 `{text.default}` |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(0, 0, 0, 0.05); }`.

![Disabled buttons reset-tutorials](components/crops/button-disabled-reset-tutorials.png) ![Disabled buttons reset-tutorials-hover](components/crops/button-disabled-reset-tutorials-hover.png) ![Disabled buttons toolbar](components/crops/button-disabled-toolbar.png)

#### Text button
Left-aligned 600 text buttons in a column (Update Profile, Change Email, Change Password, Delete Account). Read as `button-text` on the Account Settings dialog (Profile).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 422 x 29; padding 4px 8px `{spacing.1} {spacing.2}`; radius 4px `{radius.sm}`; background transparent; text Plus Jakarta Sans 14/21 600, #000000 `{text.default}`; cursor pointer |
| hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| pressed | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| delete (same as the first row) | same values |
| delete, hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(0, 0, 0, 0.05); }`.

![Text button default](components/crops/button-text-default.png) ![Text button hover](components/crops/button-text-hover.png) ![Text button focus-visible](components/crops/button-text-focus-visible.png) ![Text button pressed](components/crops/button-text-pressed.png) ![Text button delete](components/crops/button-text-delete.png) ![Text button delete-hover](components/crops/button-text-delete-hover.png)

#### Inline link button
Small text button with a leading plus ("Link Zotero"). Read as `button-link` on the Account Settings dialog (Preferences).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 114.27 x 24 (height `{size.control-sm}`); padding 4px 8px `{spacing.1} {spacing.2}`; gap 8px `{spacing.2}`; radius 4px `{radius.sm}`; background transparent; text Plus Jakarta Sans 14/14 500, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| hover | background rgba(0, 0, 0, 0.05) `{action.quiet}` |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| pressed | background rgba(0, 0, 0, 0.05) `{action.quiet}` |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(0, 0, 0, 0.05); }`.

![Inline link button default](components/crops/button-link-default.png) ![Inline link button hover](components/crops/button-link-hover.png) ![Inline link button focus-visible](components/crops/button-link-focus-visible.png) ![Inline link button pressed](components/crops/button-link-pressed.png)

### Form controls

Read on 2026-10-17. Fields, the checkbox, single- and multi-choice pills, the select, the range slider and the note composer. The light controls live in dialogs; the dark ones on the black Search Settings drawer.

#### Text field
Field with an inset 1px grey line and 8px corners under a label. Filled and empty (placeholder). Read as `text-field` on the Update profile dialog.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| filled (same: hover) | size 468 x 37 (height `{size.field}`); padding 8px 12px `{spacing.2} {spacing.3}`; radius 8px `{radius.lg}`; background transparent; shadow #c9cdd3 0px 0px 0px 1px inset (`{elevation.ring-field}`); text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; cursor text; placeholder #000000 `{text.default}` |
| filled, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| placeholder (same: hover) (same as the first row) | same values |
| placeholder, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Text field filled](components/crops/text-field-filled.png) ![Text field filled-focus-visible](components/crops/text-field-filled-focus-visible.png) ![Text field placeholder](components/crops/text-field-placeholder.png) ![Text field placeholder-focus-visible](components/crops/text-field-placeholder-focus-visible.png)

#### Checkbox
A 20px square button with role checkbox. Light in a dialog, dark in the Search Settings drawer, where checking it tints the whole row and adds a remove cross. Read as `checkbox` on the Account Settings dialog (Preferences), Search Settings drawer (open), Search Settings drawer (Open Access checked) and 1 more.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| unchecked (same: hover, pressed) | size 20 x 20; border 1px solid #686d79 `{border.drawer}`; radius 4px `{radius.sm}`; background transparent; text Plus Jakarta Sans 18/27 400, #000000 `{text.default}`; cursor pointer |
| unchecked, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| dark (same: hover) (as the first row, except) | text Plus Jakarta Sans 18/27 400, #ffffff `{text.inverse}` |
| dark, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| dark-checked (as the first row, except) | text Plus Jakarta Sans 18/27 400, #ffffff `{text.inverse}`; icon 18 x 18, #ffffff `{text.inverse}` |
| cite (same: hover, pressed) (same as the first row) | same values |
| cite, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Checkbox unchecked](components/crops/checkbox-unchecked.png) ![Checkbox unchecked-focus-visible](components/crops/checkbox-unchecked-focus-visible.png) ![Checkbox dark](components/crops/checkbox-dark.png) ![Checkbox dark-focus-visible](components/crops/checkbox-dark-focus-visible.png) ![Checkbox dark-checked](components/crops/checkbox-dark-checked.png) ![Checkbox cite](components/crops/checkbox-cite.png) ![Checkbox cite-focus-visible](components/crops/checkbox-cite-focus-visible.png)

#### Single-choice pills
The product has no radio buttons. A choice of one is a row of outlined pills where the chosen one is filled lavender (Articles or Authors; Similar, References or Citations; 10, 20 or 40). Read as `segmented` on the Search Settings drawer (open).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| selected (same: hover, pressed) | size 60.73 x 28; padding 4px 8px `{spacing.1} {spacing.2}`; border 1px solid #e8e7f6 `{border.choice-dark}`; radius 48px `{radius.pill}`; background #e8e7f6 `{action.accent-soft}`; text Plus Jakarta Sans 12/18 400, #000000 `{text.default}`; cursor pointer |
| selected, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| other (as the first row, except) | size 62.14 x 28; background transparent; text Plus Jakarta Sans 12/18 400, #e8e7f6 `{text.choice-dark}` |
| other, hover | background rgba(255, 255, 255, 0.1) `{action.quiet-hover-inverse}` |
| other, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| other, pressed | background rgba(255, 255, 255, 0.1) `{action.quiet-hover-inverse}` |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover:not(:disabled) { background-color: rgba(255, 255, 255, 0.1); }`; `.x:hover:not(:disabled) { background-color: var(--lavender-25); }`.

![Single-choice pills selected](components/crops/segmented-selected.png) ![Single-choice pills selected-focus-visible](components/crops/segmented-selected-focus-visible.png) ![Single-choice pills other](components/crops/segmented-other.png) ![Single-choice pills other-hover](components/crops/segmented-other-hover.png) ![Single-choice pills other-focus-visible](components/crops/segmented-other-focus-visible.png) ![Single-choice pills other-pressed](components/crops/segmented-other-pressed.png)

#### Select in the drawer
The Retractions select ("Not set...") and its open list: white, 6px corners, the highlighted option in the selection blue. Read as `select-dark` on the Search Settings drawer (open), Search Settings drawer (select open).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| trigger | size 100.33 x 29; padding 4px 8px `{spacing.1} {spacing.2}`; gap 8px `{spacing.2}`; radius 4px `{radius.sm}`; background rgba(0, 0, 0, 0.05) `{action.quiet}`; text Plus Jakarta Sans 14/14 400, #686d79 `{text.secondary}`; cursor pointer; icon 16 x 16, #686d79 `{text.secondary}` |
| trigger, hover | background rgba(0, 0, 0, 0.07) `{action.select-hover}` |
| trigger, focus-visible | shadow #000000 0px 0px 0px 2px; outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| list | size 189.91 x 52; radius 6px `{radius.md}`; background #ffffff `{background.surface}`; shadow rgba(22, 23, 24, 0.35) 0px 10px 38px -10px, rgba(22, 23, 24, 0.2) 0px 10px 20px -15px (`{elevation.menu}`); text Plus Jakarta Sans 14/14 400, #000000 `{text.default}` |
| option-highlighted | size 181.91 x 22; padding 4px 35px 4px 25px; radius 4px `{radius.sm}`; background #a7d4ff `{action.highlighted}`; text Plus Jakarta Sans 14/14 400, #000000 `{text.default}` |
| option | size 181.91 x 22; padding 4px 35px 4px 25px; radius 4px `{radius.sm}`; background transparent; text Plus Jakarta Sans 14/14 400, #201d1d `{text.primary}` |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(0, 0, 0, 0.07); }`; `.x:focus { box-shadow: black 0px 0px 0px 2px; }`.

![Select in the drawer trigger](components/crops/select-dark-trigger.png) ![Select in the drawer trigger-hover](components/crops/select-dark-trigger-hover.png) ![Select in the drawer trigger-focus-visible](components/crops/select-dark-trigger-focus-visible.png) ![Select in the drawer list](components/crops/select-dark-list.png) ![Select in the drawer option-highlighted](components/crops/select-dark-option-highlighted.png) ![Select in the drawer option](components/crops/select-dark-option.png)

#### Range slider
Two thumbs on a 3px track: 12px dark thumbs with a 4px lavender ring. Read as `slider` on the Search Settings drawer (open).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 293 x 20; padding 8px 12px `{spacing.2} {spacing.3}`; background transparent; text Plus Jakarta Sans 14/14 400, #ffffff `{text.inverse}` |
| thumb (same: hover) | size 12 x 12; radius 10px; background #353535 `{component.drawer-row}`; shadow #a49edb 0px 0px 0px 4px (`{elevation.slider-thumb}`); text Plus Jakarta Sans 14/14 400, #ffffff `{text.inverse}`; cursor grab |
| thumb, focus-visible | shadow #a49edb 0px 0px 0px 5px (`{elevation.slider-thumb-active}`) |
| thumb, pressed | shadow #a49edb 0px 0px 0px 5px (`{elevation.slider-thumb-active}`); cursor grabbing |

Child layers that carry the look: span 269x3 background #f2f2f2 `{action.control}` radius 48px; span 269x3 background #000000 `{action.primary}` radius 48px; span 12x12 background #353535 `{component.drawer-row}` radius 10px shadow #a49edb 0px 0px 0px 4px (`{elevation.slider-thumb}`).

Parts:

- track: 269 x 3; Plus Jakarta Sans 14/14 400, #ffffff `{text.inverse}`; background #f2f2f2 `{action.control}`; radius 48px `{radius.pill}`
- range: 269 x 3; Plus Jakarta Sans 14/14 400, #ffffff `{text.inverse}`; background #000000 `{action.primary}`; radius 48px `{radius.pill}`
- thumb: 12 x 12; Plus Jakarta Sans 14/14 400, #ffffff `{text.inverse}`; background #353535 `{component.drawer-row}`; radius 10px; shadow #a49edb 0px 0px 0px 4px (`{elevation.slider-thumb}`)

Authored state rules (from the page's CSS): `.x:focus { outline: none; box-shadow: 0 0 0 5px var(--lavender); }`; `.x:active { cursor: grabbing; }`.

![Range slider default](components/crops/slider-default.png) ![Range slider thumb](components/crops/slider-thumb.png) ![Range slider thumb-focus-visible](components/crops/slider-thumb-focus-visible.png) ![Range slider thumb-pressed](components/crops/slider-thumb-pressed.png)

#### Drawer inputs
Pill inputs on the dark drawer: the keyword field (italic placeholder) and the 60px number fields of a range. Read as `drawer-input` on the Search Settings drawer (open).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| keyword (same: hover) | size 293 x 26; padding 4px 8px `{spacing.1} {spacing.2}`; radius 48px `{radius.pill}`; background transparent; shadow #dde0e4 0px 0px 0px 1px inset (`{elevation.ring-field-dark}`); text Plus Jakarta Sans 12/18 400, #ffffff `{text.inverse}`; cursor text; placeholder #ffffff `{text.inverse}` |
| keyword, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| number (same: hover) (as the first row, except) | size 60 x 28; padding 4px 12px `{spacing.1} {spacing.3}`; border 1px solid #c9cdd3 `{border.default}`; shadow none |
| number, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Drawer inputs keyword](components/crops/drawer-input-keyword.png) ![Drawer inputs keyword-focus-visible](components/crops/drawer-input-keyword-focus-visible.png) ![Drawer inputs number](components/crops/drawer-input-number.png) ![Drawer inputs number-focus-visible](components/crops/drawer-input-number-focus-visible.png)

#### Multi-choice chips
Outlined lavender chips that toggle independently (SJR quartiles Q1 to Q4). Read as `quartile-chip` on the Search Settings drawer (open).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default (same: hover, pressed) | size 33 x 28; padding 4px 8px `{spacing.1} {spacing.2}`; border 1px solid #d1ceed `{border.chip-dark}`; radius 24px `{radius.chip}`; background transparent; text Plus Jakarta Sans 12/18 400, #d1ceed `{text.chip-dark}`; cursor pointer |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Multi-choice chips default](components/crops/quartile-chip-default.png) ![Multi-choice chips focus-visible](components/crops/quartile-chip-focus-visible.png)

#### Note composer
The multi-line field at the foot of the Notes tab: a contenteditable rich-text box, the product's only free-text area. Seen empty, never typed into. Read as `note-composer` on the library, article Notes tab (empty).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default (same: hover) | size 382 x 50; padding 4px 8px `{spacing.1} {spacing.2}`; radius 8px `{radius.lg}`; background #ffffff `{background.surface}`; shadow #686d79 0px 0px 0px 1px (`{elevation.ring-composer}`); text Plus Jakarta Sans 13/13 400 italic, #aaaaaa `{component.note-placeholder}`; transition min-height 0.3s ease |
| focus-visible | outline 1px auto #005fcc `{border.focus-browser}`, offset 0px |

![Note composer default](components/crops/note-composer-default.png) ![Note composer focus-visible](components/crops/note-composer-focus-visible.png)

#### Citation box
The click-to-copy box in Cite Article: the citation in 12px monospace on a pale blue fill with a copy icon. Clicking copies it and raises a toast. Read as `citation-box` on the library, Cite Article dialog, library, Cite Article (citation copied, toast showing).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 502 x 108; padding 4px `{spacing.1}`; border 1px solid #c9cdd3 `{border.default}`; radius 8px `{radius.lg}`; background #ffffff `{background.surface}`; text monospace 12/12 400, #000000 `{text.default}`; cursor pointer; icon 14 x 14, #000000 `{text.default}` |
| hover, pressed | background #e9f5fe `{component.citation-box}` |
| copied (as the first row, except) | background #e9f5fe `{component.citation-box}` |

- Not measured: focus could not be captured on the component (not focusable, or focused without matching :focus-visible).

Parts:

- preview: 462 x 90; monospace 12/18 400, #000000 `{text.default}`; margin 4px `{spacing.1}`; text "Ding, S., Dai, X., Xing, L., D"

Authored state rules (from the page's CSS): `.x:hover { background-color: var(--selection-light); }`.

![Citation box default](components/crops/citation-box-default.png) ![Citation box hover](components/crops/citation-box-hover.png) ![Citation box pressed](components/crops/citation-box-pressed.png) ![Citation box copied](components/crops/citation-box-copied.png)

#### BibTeX drop zone
A 30% white strip with 16px corners on the Search start page: "Drag and drop a BibTeX file to search from". Read as `drop-zone` on the Search start page (recent searches).

**Values (default).** size 1288 x 78; padding 32px `{spacing.8}`; gap 16px `{spacing.4}`; radius 16px `{radius.2xl}`; background rgba(255, 255, 255, 0.3) `{background.drop-zone}`; text Plus Jakarta Sans 14/14 500, #000000 `{text.default}`; icon 14 x 14, #000000 `{text.default}`.

![BibTeX drop zone default](components/crops/drop-zone-default.png)

### Tabs and navigation

Read on 2026-10-17. The vertical tabs of Account Settings and the filter pills above the Reading List.

#### Vertical tab
The Account Settings tab column: 40px rows with an icon, the current one on a grey fill. Read as `settings-tab` on the Account Settings dialog (Preferences).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| current (same: hover, pressed) | size 180 x 40 (height `{size.control-lg}`); padding 12px `{spacing.3}`; radius 8px `{radius.lg}`; background #eef0f1 `{background.page}`; text Plus Jakarta Sans 16/16 400, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |
| current, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| other (as the first row, except) | background transparent |
| other, hover | background #f9fafa `{component.tab-hover}` |
| other, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| other, pressed | background #f9fafa `{component.tab-hover}` |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: var(--grey-bg1); }`; `.x:hover { background-color: var(--grey-bg2); }`.

![Vertical tab current](components/crops/settings-tab-current.png) ![Vertical tab current-focus-visible](components/crops/settings-tab-current-focus-visible.png) ![Vertical tab other](components/crops/settings-tab-other.png) ![Vertical tab other-hover](components/crops/settings-tab-other-hover.png) ![Vertical tab other-focus-visible](components/crops/settings-tab-other-focus-visible.png) ![Vertical tab other-pressed](components/crops/settings-tab-other-pressed.png)

#### Filter toggle pills
All, To Read and Read above the Reading List, each with a count; the current one has a 1px black inset ring. Read as `filter-toggle` on the library, Reading List (empty).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| current (same: hover, pressed) | size 39.97 x 22; padding 2px 8px; radius 48px `{radius.pill}`; background rgba(0, 0, 0, 0.05) `{action.quiet}`; shadow #000000 0px 0px 0px 1px inset (`{elevation.ring-strong}`); text Plus Jakarta Sans 12/18 400, #000000 `{text.default}`; cursor pointer |
| current, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| other (same: hover, pressed) (as the first row, except) | size 71.31 x 22; shadow none |
| other, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Filter toggle pills current](components/crops/filter-toggle-current.png) ![Filter toggle pills current-focus-visible](components/crops/filter-toggle-current-focus-visible.png) ![Filter toggle pills other](components/crops/filter-toggle-other.png) ![Filter toggle pills other-focus-visible](components/crops/filter-toggle-other-focus-visible.png)

### Menus

Read on 2026-10-17. The workspace menu (Radix dropdown) and the account popover.

#### Menu
The workspace menu: a 220px white sheet with 6px corners and a soft two-layer shadow, a separator, and 30px items with a 32px left inset for the check. The highlighted item is the selection blue. Read as `menu` on the home page (workspace menu open).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 228.16 x 107; padding 4px `{spacing.1}`; radius 6px `{radius.md}`; background #ffffff `{background.surface}`; shadow rgba(22, 23, 24, 0.35) 0px 10px 38px -10px, rgba(22, 23, 24, 0.2) 0px 10px 20px -15px (`{elevation.menu}`); text Plus Jakarta Sans 14/21 600, #201d1d `{text.primary}`; icon 18 x 18, #201d1d `{text.primary}` |
| item-highlighted | size 220.16 x 30; padding 8px 8px 8px 32px `{spacing.2} {spacing.2} {spacing.2} {spacing.8}`; radius 3px `{radius.xs}`; background #a7d4ff `{action.highlighted}`; text Plus Jakarta Sans 14/21 400, #201d1d `{text.primary}`; icon 18 x 18, #201d1d `{text.primary}` |
| item | size 220.16 x 30; padding 8px 8px 8px 32px `{spacing.2} {spacing.2} {spacing.2} {spacing.8}`; radius 3px `{radius.xs}`; background transparent; text Plus Jakarta Sans 14/21 400, #201d1d `{text.primary}`; icon 18 x 18, #201d1d `{text.primary}` |
| separator | size 212.16 x 1; background #eef0f1 `{component.menu-separator}`; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}` |

Authored state rules (from the page's CSS): `.x[data-state="checked"] { font-weight: 600; }`.

![Menu default](components/crops/menu-default.png) ![Menu item-highlighted](components/crops/menu-item-highlighted.png) ![Menu item](components/crops/menu-item.png)

#### Account menu
A popover from the account button: name and email (redacted), then three groups of text items split by rules, Log Out centred at the foot. Read as `account-menu` on the home page (account menu open).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 220 x 290; border 1px solid #000000 `{border.strong}`; radius 8px `{radius.lg}`; background #ffffff `{background.surface}`; shadow rgba(14, 18, 22, 0.35) 0px 10px 38px -10px, rgba(14, 18, 22, 0.2) 0px 10px 20px -15px (`{elevation.popup}`); text Plus Jakarta Sans 16/24 500, #000000 `{text.default}`; icon 16 x 16, #000000 `{text.default}` |
| item | size 210 x 29; padding 4px 8px `{spacing.1} {spacing.2}`; radius 4px `{radius.sm}`; background transparent; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; cursor pointer |
| item, hover | background #eef0f1 `{background.page}` |
| item, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| item, pressed | background #eef0f1 `{background.page}` |

Parts:

- container: 220 x 290; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; background #ffffff `{background.surface}`; radius 8px `{radius.lg}`; border T:1px solid #000000 `{border.strong}` / R:1px solid #000000 `{border.strong}` / B:1px solid #000000 `{border.strong}` / L:1px solid #000000 `{border.strong}`; shadow rgba(14, 18, 22, 0.35) 0px 10px 38px -10px, rgba(14, 18, 22, 0.2) 0px 10px 20px -15px (`{elevation.popup}`); text "Researcher Email hidden Profil"
  - child Profile: 210 x 29; at 5, 64; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; radius 4px `{radius.sm}`; padding 4px 8px `{spacing.1} {spacing.2}`; text "Profile"
  - child Preferences: 210 x 29; at 5, 93; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; radius 4px `{radius.sm}`; padding 4px 8px `{spacing.1} {spacing.2}`; text "Preferences"
  - child Subscription: 210 x 29; at 5, 122; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; radius 4px `{radius.sm}`; padding 4px 8px `{spacing.1} {spacing.2}`; text "Subscription"
  - child Invites: 210 x 29; at 5, 151; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; radius 4px `{radius.sm}`; padding 4px 8px `{spacing.1} {spacing.2}`; text "Invites"
  - child Support Chat: 210 x 29; at 5, 189; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; radius 4px `{radius.sm}`; padding 4px 8px `{spacing.1} {spacing.2}`; text "Support Chat"
  - child Guides: 210 x 29; at 5, 218; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; radius 4px `{radius.sm}`; padding 4px 8px `{spacing.1} {spacing.2}`; text "Guides"
  - child Log Out: 210 x 29; at 5, 256; Plus Jakarta Sans 14/21 500, #000000 `{text.default}`; radius 4px `{radius.sm}`; padding 4px 8px `{spacing.1} {spacing.2}`; text "Log Out"

Authored state rules (from the page's CSS): `.x:focus { box-shadow: rgba(14, 18, 22, 0.35) 0px 10px 38px -10px, rgba(14, 18, 22, 0.2) 0px 10px 20px -15px, rgba(0, 0, 0, 0.2) 0px 0px 0px 2px; }`; `.x[data-state="open"][data-side="bottom"] { animation-name: fSMqcH; }`.

![Account menu default](components/crops/account-menu-default.png) ![Account menu item](components/crops/account-menu-item.png) ![Account menu item-hover](components/crops/account-menu-item-hover.png) ![Account menu item-focus-visible](components/crops/account-menu-item-focus-visible.png) ![Account menu item-pressed](components/crops/account-menu-item-pressed.png)

### Avatar and badges

Read on 2026-10-17. The placeholder avatar, the green Upgrade badge and the notice banner.

#### Avatar
No photo is set, so the avatar is a placeholder person glyph: an 80px white circle on the profile card, 16px inside the 32px account button. Read as `avatar` on the home page (account menu open), Account Settings dialog (Profile).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| profile | size 80 x 80; radius 50%; background #ffffff `{background.surface}`; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; icon 28 x 28, #686d79 `{text.secondary}` |
| button | size 16 x 16; radius 100px; background transparent; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; cursor pointer; icon 16 x 16, #000000 `{text.default}` |

![Avatar profile](components/crops/avatar-profile.png) ![Avatar button](components/crops/avatar-button.png)

#### Upgrade badge
Green 12px 600 pill marking a paid feature, in menus and drawer headings. Read as `paywall-badge` on the home page (workspace menu open), Search Settings drawer (open).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 67.13 x 26; padding 4px 8px `{spacing.1} {spacing.2}`; radius 48px `{radius.pill}`; background #8add8a `{action.upgrade}`; text Plus Jakarta Sans 12/12 600, #201d1d `{text.primary}` |
| drawer (as the first row, except) | cursor pointer |

![Upgrade badge default](components/crops/paywall-badge-default.png) ![Upgrade badge drawer](components/crops/paywall-badge-drawer.png)

#### Notice banner
Pale green box with a lock icon ("You are previewing Advanced Settings"). With the turquoise tip banner, the only informational banners seen. Read as `notice` on the Search Settings drawer (open).

**Values (default).** size 358 x 40 (height `{size.control-lg}`); padding 8px `{spacing.2}`; gap 8px `{spacing.2}`; radius 8px `{radius.lg}`; background #e2f6e2 `{status.info.fill}`; text Plus Jakarta Sans 12/12 600, #201d1d `{text.primary}`; icon 14 x 14, #201d1d `{text.primary}`.

![Notice banner default](components/crops/notice-default.png)

### Feedback and loading

Read on 2026-10-17. The spinner, the selection circle and its Clear link, the toast (raised by copying a citation), the inline error and the incomplete-data warning.

#### Spinner
16px spinning wheel, 1.1s per turn: alone in the middle of the list while a page of results loads, or under the message in the loading dialog. Read as `spinner` on the keyword search results (next page loading), keyword search results (updating dialog).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| list | size 16.91 x 16.91; background transparent; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; transform matrix(-0.236127, -0.971722, 0.971722, -0.236127, 0, 0); icon 16.91 x 16.91, #000000 `{text.default}` |
| dialog (as the first row, except) | transform matrix(0.236399, 0.971656, -0.971656, 0.236399, 0, 0) |

![Spinner list](components/crops/spinner-list.png) ![Spinner dialog](components/crops/spinner-dialog.png)

#### Selection circle
The 20px circle at the top right of a result card. Selecting it fills it black with a white tick, outlines the card and lists the paper in Next Search. Read as `selection-tick` on the keyword search results (list view), keyword search results (one article selected).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| unselected (same: hover, pressed) | size 20 x 20; background transparent; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; cursor pointer; icon 18 x 18, #000000 `{text.default}` |
| selected (same as the first row) | same values |

- Not measured: focus could not be captured on unselected (not focusable, or focused without matching :focus-visible).

![Selection circle unselected](components/crops/selection-tick-unselected.png) ![Selection circle unselected-hover](components/crops/selection-tick-unselected-hover.png) ![Selection circle unselected-pressed](components/crops/selection-tick-unselected-pressed.png) ![Selection circle selected](components/crops/selection-tick-selected.png)

#### Clear link
Underlined grey text after the selection count ("1 selected Clear"). Read as `clear-link` on the keyword search results (one article selected).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 35.36 x 21; background transparent; text Plus Jakarta Sans 14/21 400, #686d79 `{text.secondary}`, underline; cursor pointer |
| hover | text Plus Jakarta Sans 14/21 400, #201d1d `{text.primary}`, underline |
| focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| pressed | text Plus Jakarta Sans 14/21 400, #201d1d `{text.primary}`, underline |

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { color: var(--grey-primary); }`.

![Clear link default](components/crops/clear-link-default.png) ![Clear link hover](components/crops/clear-link-hover.png) ![Clear link focus-visible](components/crops/clear-link-focus-visible.png) ![Clear link pressed](components/crops/clear-link-pressed.png)

#### Toast
A 500px dark bar centred 12px above the bottom edge: an icon, a 500 message, and a close cross in a 40px square. Seen after copying a citation ("Copied to clipboard"); it stays 4 seconds, 2 more after the pointer leaves (raw/app-code-notes.md). Read as `toast` on the library, Cite Article (citation copied, toast showing).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 500 x 42; gap 8px `{spacing.2}`; border 1px solid transparent; radius 8px `{radius.lg}`; background #333333 `{component.toast}`; shadow rgba(0, 0, 0, 0.3) 3px 3px 12px 0px (`{elevation.toast}`); text Plus Jakarta Sans 14/14 500, #ffffff `{text.inverse}`; icon 14 x 14, #ffffff `{text.inverse}` |
| close | size 40 x 40 (height `{size.control-lg}`); padding 12px `{spacing.3}`; background transparent; text Plus Jakarta Sans 18/27 400, #ffffff `{text.inverse}`; cursor pointer; icon 16 x 16, #ffffff `{text.inverse}` |
| close, hover | background rgba(255, 255, 255, 0.1) `{action.quiet-hover-inverse}` |
| close, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |
| close, pressed | background rgba(255, 255, 255, 0.1) `{action.quiet-hover-inverse}` |

Parts:

- message: 135.13 x 14; Plus Jakarta Sans 14/14 500, #ffffff `{text.inverse}`; text "Copied to clipboard"
- close: 40 x 40; Plus Jakarta Sans 18/27 400, #ffffff `{text.inverse}`; padding 12px `{spacing.3}`

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`; `.x:hover { background-color: rgba(255, 255, 255, 0.1); }`.

![Toast default](components/crops/toast-default.png) ![Toast close](components/crops/toast-close.png) ![Toast close-hover](components/crops/toast-close-hover.png) ![Toast close-focus-visible](components/crops/toast-close-focus-visible.png) ![Toast close-pressed](components/crops/toast-close-pressed.png)

#### Inline error
A pale red 12px box in the article panel's drawer, "Cannot search: Citation info missing", shown when an article has no references and no citations. Read as `error-box` on the keyword search results (an article with no citation data inspected).

**Values (default).** size 358 x 29; padding 4px 8px `{spacing.1} {spacing.2}`; gap 8px `{spacing.2}`; radius 8px `{radius.lg}`; background #fcebe5 `{status.danger.fill}`; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; icon 12 x 12, #000000 `{text.default}`.

![Inline error default](components/crops/error-box-default.png)

#### Incomplete data warning
A peach chip after the author and year on a result card, and a banner with Learn More at the top of the article panel, for an article whose metadata is incomplete. Read as `incomplete-warning` on the keyword search results (an article with no citation data inspected).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| chip | size 130.77 x 26; padding 4px 8px `{spacing.1} {spacing.2}`; gap 4px `{spacing.1}`; radius 48px `{radius.pill}`; background #fcebe5 `{component.incomplete-warning}`; text Plus Jakarta Sans 12/18 500, #000000 `{text.default}`; icon 16 x 16, #686d79 `{text.secondary}` |
| banner | size 366 x 26; padding 4px 8px `{spacing.1} {spacing.2}`; gap 8px `{spacing.2}`; radius 8px `{radius.lg}`; background #fcebe5 `{component.incomplete-warning}`; text Plus Jakarta Sans 12/18 500, #000000 `{text.default}`; icon 14 x 14, #686d79 `{text.secondary}` |

![Incomplete data warning chip](components/crops/incomplete-warning-chip.png) ![Incomplete data warning banner](components/crops/incomplete-warning-banner.png)

### Data display

Read on 2026-10-17. The library table and the recent-search rows.

#### Article table
The library table view: a white panel with 8px corners, a 600 header row with a sort chevron, 29px rows split by 1px grey rules, numbers at the right and a selection circle per row. Read as `table` on the library, All Articles in table view.

**Values (default).** size 1126 x 624; radius 8px `{radius.lg}`; background #ffffff `{background.surface}`; text Plus Jakarta Sans 14/14 600, #000000 `{text.default}`; icon 14 x 14, #686d79 `{text.secondary}`.

![Article table default](components/crops/table-default.png)

#### Table header cell
A sortable column title; Label carries the up chevron. Read as `table-header` on the library, All Articles in table view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 120 x 30; padding 6px 3px; gap 4px `{spacing.1}`; background transparent; text Plus Jakarta Sans 14/14 600, #000000 `{text.default}`; cursor pointer; icon 14 x 14, #686d79 `{text.secondary}` |
| hover, pressed | background rgba(0, 0, 0, 0.05) `{action.quiet}` |

- Not measured: focus could not be captured on the component (not focusable, or focused without matching :focus-visible).

Authored state rules (from the page's CSS): `.x:hover { background-color: rgba(0, 0, 0, 0.05); }`.

![Table header cell default](components/crops/table-header-default.png) ![Table header cell hover](components/crops/table-header-hover.png) ![Table header cell pressed](components/crops/table-header-pressed.png)

#### Table row
One article per 29px row. Read as `table-row` on the library, All Articles in table view.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 1126 x 29; padding 0px 4px `{spacing.0} {spacing.1}`; background #ffffff `{background.surface}`; text Plus Jakarta Sans 14/21 500, #000000 `{text.default}`; icon 14 x 14, #000000 `{text.default}` |
| hover, pressed | background #eef0f1 `{component.table-row-hover}` |

- Not measured: focus could not be captured on the component (not focusable, or focused without matching :focus-visible).

Authored state rules (from the page's CSS): `.x:hover { background-color: var(--grey-bg2); }`.

![Table row default](components/crops/table-row-default.png) ![Table row hover](components/crops/table-row-hover.png) ![Table row pressed](components/crops/table-row-pressed.png)

#### Recent search row
One past search on the Search start page: the inputs as chips, the date in 12px grey, and a remove cross. Read as `recent-search-row` on the Search start page (recent searches).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 1316 x 92; radius 8px `{radius.lg}`; background #ffffff `{background.surface}`; text Plus Jakarta Sans 14/14 400, #000000 `{text.default}`; icon 14 x 14, #000000 `{text.default}` |
| hover, pressed | shadow #000000 0px 0px 0px 1px inset (`{elevation.ring-strong}`) |

- Not measured: focus could not be captured on the component (not focusable, or focused without matching :focus-visible).

Parts:

- main: 1260 x 92; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; padding 16px `{spacing.4}`; gap 8px `{spacing.2}`; text "1 Similar articles to 0 Inputs"
- date: 1220 x 14; Plus Jakarta Sans 14/14 400, #686d79 `{text.secondary}`; margin 0px 4px `{spacing.0} {spacing.1}`; text "Saturday, October 17, 2026 at "

Authored state rules (from the page's CSS): `.x:hover { box-shadow: black 0px 0px 0px 1px inset; }`.

![Recent search row default](components/crops/recent-search-row-default.png) ![Recent search row hover](components/crops/recent-search-row-hover.png) ![Recent search row pressed](components/crops/recent-search-row-pressed.png)

### Empty states

Read on 2026-10-17. Each empty list or tab has its own line of copy; the Reading List and Notes add an illustration or a heading.

#### Empty Reading List
A 400px line illustration, "A clean slate - enjoy!", one sentence, and a black "Search for Articles" button. Read as `empty-reading` on the library, Reading List (empty).

**Values (default).** size 1126 x 648; gap 16px `{spacing.4}`; background transparent; text Plus Jakarta Sans 16/24 500, #000000 `{text.default}`.

Child layers that carry the look: button 179.3x56 background #000000 `{action.primary}` radius 8px.

![Empty Reading List default](components/crops/empty-reading-default.png)

#### Empty tab
A tab with nothing in it shows one line of 14px text at the top left ("You have no active subscriptions"). Read as `empty-text` on the Account Settings dialog (Subscription, empty).

**Values (default).** size 214.88 x 18; background transparent; text Plus Jakarta Sans 14/21 400 italic, #000000 `{text.default}`.

![Empty tab default](components/crops/empty-text-default.png)

#### Empty Notes tab
Centred 600 heading "Turn reading into understanding" over one sentence, above the composer. Read as `empty-notes` on the library, article Notes tab (empty).

**Values (default).** size 350 x 335.86; padding 24px `{spacing.6}`; gap 4px `{spacing.1}`; radius 16px `{radius.2xl}`; background transparent; text Plus Jakarta Sans 16/24 500, #000000 `{text.default}`.

![Empty Notes tab default](components/crops/empty-notes-default.png)

### Phone width

Read on 2026-10-17 at 390 x 844, 800 x 900 and 1000 x 800. Below 641px the app has no layout and shows a notice instead; between that and desktop it keeps the desktop frame and changes only what its script breakpoints switch (raw/app-code-notes.md).

#### Screen too small
At 640px wide or less the app covers every page with this notice: the wordmark, a heading, an 18px sentence and a "Continue anyway" text button. Continuing shows the desktop layout clipped at the right edge. Read as `mobile-warning` on the library at 390px (Screen too small).

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| default | size 390 x 844; padding 24px 48px `{spacing.6} {spacing.12}`; gap 16px `{spacing.4}`; background transparent; text Plus Jakarta Sans 28/42 400, #000000 `{text.default}` |
| continue (same: hover, pressed) | size 113.45 x 21; background transparent; text Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; cursor pointer |
| continue, focus-visible | outline 1px auto #b0edf0 `{action.focus-ring}`, offset 0px |

Parts:

- logo: 250 x 50
- desc: 294 x 54; Plus Jakarta Sans 18/27 400, #000000 `{text.default}`; text "Resize your window to take ful"

Authored state rules (from the page's CSS): `button:focus, input:focus { outline-color: var(--turq-50); }`.

![Screen too small default](components/crops/mobile-warning-default.png) ![Screen too small continue](components/crops/mobile-warning-continue.png) ![Screen too small continue-focus-visible](components/crops/mobile-warning-continue-focus-visible.png)

#### Home columns
The home page lays its three cards in a row at 896px and wider, and stacks them in one column below that (the breakpoint xmd, raw/app-code-notes.md). The hero illustration drops out below 768px (md). Read as `home-columns` on the home page (2026-10-17), home page at 800 x 900.

| State | Values (a hover, focus-visible or pressed row lists only what changes) |
|---|---|
| stacked-800 | size 752 x 1522; gap 16px `{spacing.4}`; background transparent; text Plus Jakarta Sans 16/24 600, #000000 `{text.default}`; icon 16 x 16, #f07d59 `{palette.ugc.amber}` |
| row-1440 (as the first row, except) | size 1352 x 901 |

Child layers that carry the look: div 752x496.7 background rgba(255, 255, 255, 0.4) `{background.section}` radius 8px; div 728x2 background #0000ff `{component.result-card-loadline}`; div 728x2.

Parts:

- container: 752 x 1522; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; gap 16px `{spacing.4}`; text "Recently saved Dive deeper on "
  - child Recently saved Dive deep: 752 x 496.67; at 0, 0; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; background rgba(255, 255, 255, 0.4) `{background.section}`; radius 8px `{radius.lg}`; padding 12px `{spacing.3}`; gap 4px `{spacing.1}`; text "Recently saved Dive deeper on "
  - child Library Find new article: 752 x 496.67; at 0, 512.7; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; background rgba(255, 255, 255, 0.4) `{background.section}`; radius 8px `{radius.lg}`; padding 12px `{spacing.3}`; gap 4px `{spacing.1}`; text "Library Find new articles for "
  - child What’s New Learn about a: 752 x 496.67; at 0, 1025.3; Plus Jakarta Sans 14/21 400, #000000 `{text.default}`; background rgba(255, 255, 255, 0.4) `{background.section}`; radius 8px `{radius.lg}`; padding 12px `{spacing.3}`; gap 4px `{spacing.1}`; text "What’s New Learn about all thi"

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

## Icons

66 SVGs: 59 lifted from the snapshots and 7 copied as path strings from the graph engine's `graphIconPathMap` (the `graph-*` files, 24 x 24, drawn on the canvas with Path2D). They are in [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. The big Lottie rabbit and the illustration art are not included. The SVGs are ResearchRabbit's, kept for reference only.

| Icon | Rendered sizes | View box | Style | Seen on | Place |
|---|---|---|---|---|---|
| ![account](icons/account.svg) [account](icons/account.svg) | 16x16 | 0 0 24 24 | fill | 22 pages | button ActiveUserAvatar__PlaceholderContainer |
| ![wordmark](icons/wordmark.svg) [wordmark](icons/wordmark.svg) | 208x42 | 0 0 119 19 | fill | 22 pages | a Navigation__StyledWordmark |
| ![chevron-down](icons/chevron-down.svg) [chevron-down](icons/chevron-down.svg) | 12x12 16x16 20x20 | 0 0 24 24 | fill | 22 pages | button generateVariantComponent__default |
| ![view-split](icons/view-split.svg) [view-split](icons/view-split.svg) | 16x16 | 0 0 24 24 | fill | 21 pages | button ViewSelection__Button |
| ![filter](icons/filter.svg) [filter](icons/filter.svg) | 16x16 | 0 0 24 24 | fill | 21 pages | button Button__SharedStyles |
| ![view-list](icons/view-list.svg) [view-list](icons/view-list.svg) | 16x16 | 0 0 25 24 | fill | 21 pages | button ViewSelection__Button |
| ![zoom-out](icons/zoom-out.svg) [zoom-out](icons/zoom-out.svg) | 16x16 | 0 0 25 24 | fill | 19 pages | button GraphControls__StyledButton |
| ![zoom-in](icons/zoom-in.svg) [zoom-in](icons/zoom-in.svg) | 16x16 | 0 0 24 24 | fill | 19 pages | button GraphControls__StyledButton |
| ![tool-pointer](icons/tool-pointer.svg) [tool-pointer](icons/tool-pointer.svg) | 16x16 | 0 0 24 25 | fill | 19 pages | button GraphControls__StyledButton |
| ![layout-settings](icons/layout-settings.svg) [layout-settings](icons/layout-settings.svg) | 16x16 | 0 0 24 25 | fill | 19 pages | button GraphControls__StyledButton |
| ![recentre](icons/recentre.svg) [recentre](icons/recentre.svg) | 16x16 | 0 0 24 25 | fill | 19 pages | button GraphControls__StyledButton |
| ![axis-arrowhead-a](icons/axis-arrowhead-a.svg) [axis-arrowhead-a](icons/axis-arrowhead-a.svg) | 14x14 | 0 0 24 24 | fill | 17 pages | div GraphAxes__AxisIcon |
| ![axis-arrowhead](icons/axis-arrowhead.svg) [axis-arrowhead](icons/axis-arrowhead.svg) | 14x14 | 0 0 24 24 | fill | 17 pages | div GraphAxes__AxisIcon |
| ![close-small](icons/close-small.svg) [close-small](icons/close-small.svg) | 16x16 18x18 | 0 0 24 24 | fill | 17 pages | div Dropdown__LeftSpace |
| ![nav-back](icons/nav-back.svg) [nav-back](icons/nav-back.svg) | 16x16 | 0 0 24 24 | fill | 16 pages | button ExploreSession__NavButton |
| ![search-inputs-summary](icons/search-inputs-summary.svg) [search-inputs-summary](icons/search-inputs-summary.svg) | 14x14 | 0 0 24 24 | fill | 16 pages | div SearchSummary__InfoContainer |
| ![close](icons/close.svg) [close](icons/close.svg) | 16x16 | 0 0 24 24 | fill | 16 pages | button ExploreSession__NavButton |
| ![nav-forward](icons/nav-forward.svg) [nav-forward](icons/nav-forward.svg) | 16x16 | 0 0 24 24 | fill | 16 pages | button ExploreSession__NavButton |
| ![legend-references](icons/legend-references.svg) [legend-references](icons/legend-references.svg) | 12x12 | 0 0 24 24 | fill | 15 pages | div ExploreGraphLegend__ItemContainer |
| ![legend-search-inputs](icons/legend-search-inputs.svg) [legend-search-inputs](icons/legend-search-inputs.svg) | 12x12 | 0 0 24 24 | fill | 15 pages | div ExploreGraphLegend__ItemContainer |
| ![legend-results](icons/legend-results.svg) [legend-results](icons/legend-results.svg) | 12x12 | 0 0 25 24 | fill | 15 pages | div ExploreGraphLegend__ItemContainer |
| ![tick-small](icons/tick-small.svg) [tick-small](icons/tick-small.svg) | 14x14 16x16 18x18 | 0 0 24 25 | fill | 14 pages | button SelectionTick__SelectionTickIcon |
| ![auto-save](icons/auto-save.svg) [auto-save](icons/auto-save.svg) | 16x16 | 0 0 24 24 | fill | 14 pages | button generateVariantComponent__default |
| ![rabbit-tip](icons/rabbit-tip.svg) [rabbit-tip](icons/rabbit-tip.svg) | 30x30 | 0 0 24 24 | fill | 14 pages | div ExploreBuilder__Container |
| ![view-map](icons/view-map.svg) [view-map](icons/view-map.svg) | 16x16 | 0 0 24 24 | fill | 12 pages | button ViewSelection__Button |
| ![selection-circle](icons/selection-circle.svg) [selection-circle](icons/selection-circle.svg) | 16x16 18x18 | 0 0 24 24 | fill | 10 pages | button SelectionTick__Container |
| ![chevron-next](icons/chevron-next.svg) [chevron-next](icons/chevron-next.svg) | 16x16 | 0 0 24 24 | fill | 9 pages | button Button__SharedStyles |
| ![chevron-prev](icons/chevron-prev.svg) [chevron-prev](icons/chevron-prev.svg) | 16x16 | 0 0 24 24 | fill | 9 pages | button Button__SharedStyles |
| ![view-map-alt](icons/view-map-alt.svg) [view-map-alt](icons/view-map-alt.svg) | 16x16 | 0 0 24 24 | fill | 9 pages | button ViewSelection__Button |
| ![folder-collection](icons/folder-collection.svg) [folder-collection](icons/folder-collection.svg) | 16x16 18x18 | 0 0 24 24 | fill | 8 pages | button ListItemArticleDetailsCompact__FolderIcon |
| ![add-small](icons/add-small.svg) [add-small](icons/add-small.svg) | 12x12 16x16 | 0 0 24 24 | fill | 7 pages | button NestedFolders__HoverInlineButton |
| ![search](icons/search.svg) [search](icons/search.svg) | 16x16 18x18 20x20 | 0 0 24 24 | fill | 6 pages | div SearchBar__IconContainer |
| ![save](icons/save.svg) [save](icons/save.svg) | 16x16 | 0 0 24 24 | fill | 5 pages | button Button__SharedStyles |
| ![reading-list](icons/reading-list.svg) [reading-list](icons/reading-list.svg) | 16x16 | 0 0 24 24 | fill | 5 pages | button Button__SharedStyles |
| ![filter-library](icons/filter-library.svg) [filter-library](icons/filter-library.svg) | 16x16 | 0 0 24 24 | fill | 5 pages | button Button__SharedStyles |
| ![import-bibtex](icons/import-bibtex.svg) [import-bibtex](icons/import-bibtex.svg) | 16x16 | 0 0 24 24 | fill | 5 pages | button generateVariantComponent__default |
| ![zotero](icons/zotero.svg) [zotero](icons/zotero.svg) | 16x16 | 0 0 24 24 | fill | 5 pages | button generateVariantComponent__default |
| ![delete](icons/delete.svg) [delete](icons/delete.svg) | 16x16 | 0 0 24 25 | fill | 5 pages | button Button__SharedStyles |
| ![export](icons/export.svg) [export](icons/export.svg) | 16x16 | 0 0 24 24 | fill | 5 pages | button Button__SharedStyles |
| ![list-reading](icons/list-reading.svg) [list-reading](icons/list-reading.svg) | 16x16 | 0 0 24 24 | fill | 5 pages | div LibrarySidebar__ClickableSectionContainer |
| ![settings](icons/settings.svg) [settings](icons/settings.svg) | 16x16 | 0 0 24 24 | fill | 5 pages | button generateVariantComponent__default |
| ![add](icons/add.svg) [add](icons/add.svg) | 16x16 | 0 0 24 24 | fill | 5 pages | button Button__SharedStyles |
| ![list-all-articles](icons/list-all-articles.svg) [list-all-articles](icons/list-all-articles.svg) | 12x12 16x16 | 0 0 24 24 | fill | 5 pages | div LibrarySidebar__ClickableSectionContainer |
| ![folder-tile](icons/folder-tile.svg) [folder-tile](icons/folder-tile.svg) | 32x32 | 0 0 24 24 | fill | 5 pages | div LibraryStyles__IconContainer |
| ![share](icons/share.svg) [share](icons/share.svg) | 16x16 | 0 0 24 24 | fill | 5 pages | button generateVariantComponent__default |
| ![view-rows](icons/view-rows.svg) [view-rows](icons/view-rows.svg) | 16x16 | 0 0 24 24 | fill | 5 pages | button ViewSelection__Button |
| ![collections-sort](icons/collections-sort.svg) [collections-sort](icons/collections-sort.svg) | 16x16 | 0 0 24 24 | fill | 5 pages | button Button__SharedStyles |
| ![list-recently-found](icons/list-recently-found.svg) [list-recently-found](icons/list-recently-found.svg) | 16x16 | 0 0 24 24 | fill | 5 pages | div LibrarySidebar__ClickableSectionContainer |
| ![folder-expand](icons/folder-expand.svg) [folder-expand](icons/folder-expand.svg) | 16x16 | 0 0 24 24 | fill | 5 pages | button NestedFolders__TwiddleChevronRight |
| ![help-small](icons/help-small.svg) [help-small](icons/help-small.svg) | 14x14 | 0 0 24 24 | fill | search-map settings-size; search-map settings-x-axis; search-map settings-y-axis | div LayoutSettingControlHint__StyledQuestion |
| ![more-vertical](icons/more-vertical.svg) [more-vertical](icons/more-vertical.svg) | 16x16 | 0 0 24 24 | fill | search-map inspect-node; search-split inspect-node | button Button__SharedStyles |
| ![positions-moved](icons/positions-moved.svg) [positions-moved](icons/positions-moved.svg) | 16x16 | 0 0 24 24 | fill | library-map positions-moved; library-map positions-reset-menu | button GraphBrokenAxes__BrokenAxesDropdown |
| ![arrow-right-small](icons/arrow-right-small.svg) [arrow-right-small](icons/arrow-right-small.svg) | 16x16 | 0 0 25 24 | fill | home; search-split inspect-node | button DashboardFolders__StyledArrowRight |
| ![evaluation-shield](icons/evaluation-shield.svg) [evaluation-shield](icons/evaluation-shield.svg) | 16x16 | 0 0 24 24 | fill | search-map inspect-node; search-split inspect-node | button generateVariantComponent__default |
| ![sticker](icons/sticker.svg) [sticker](icons/sticker.svg) | 18x18 | 0 0 25 24 | fill | search-map inspect-node; search-split inspect-node | button StickerButton__StyledSticker |
| ![sort-arrows](icons/sort-arrows.svg) [sort-arrows](icons/sort-arrows.svg) | 16x16 | 0 0 24 24 | fill | library-list | button Select__Trigger |
| ![browse-library](icons/browse-library.svg) [browse-library](icons/browse-library.svg) | 16x16 | 0 0 24 24 | fill | home | button DashboardSearch__LibraryIcon |
| ![open-article](icons/open-article.svg) [open-article](icons/open-article.svg) | 18x18 | 0 0 24 24 | fill | home | button withGo__SearchIconContainer |
| ![external-link](icons/external-link.svg) [external-link](icons/external-link.svg) | 14x14 | 0 0 24 24 | fill | home | a DashboardNew__ContentBody |
| ![graph-author](icons/graph-author.svg) [graph-author](icons/graph-author.svg) | 24x24 | 0 0 24 24 | fill | graph canvas (graphIconPathMap) | canvas Path2D, Author |
| ![graph-evaluationalert](icons/graph-evaluationalert.svg) [graph-evaluationalert](icons/graph-evaluationalert.svg) | 24x24 | 0 0 24 24 | fill | graph canvas (graphIconPathMap) | canvas Path2D, EvaluationAlert |
| ![graph-evaluationcaution](icons/graph-evaluationcaution.svg) [graph-evaluationcaution](icons/graph-evaluationcaution.svg) | 24x24 | 0 0 24 24 | fill | graph canvas (graphIconPathMap) | canvas Path2D, EvaluationCaution |
| ![graph-seed](icons/graph-seed.svg) [graph-seed](icons/graph-seed.svg) | 24x24 | 0 0 24 24 | fill | graph canvas (graphIconPathMap) | canvas Path2D, Seed |
| ![graph-star](icons/graph-star.svg) [graph-star](icons/graph-star.svg) | 24x24 | 0 0 24 24 | fill | graph canvas (graphIconPathMap) | canvas Path2D, Star |
| ![graph-starcircle](icons/graph-starcircle.svg) [graph-starcircle](icons/graph-starcircle.svg) | 24x24 | 0 0 24 24 | fill | graph canvas (graphIconPathMap) | canvas Path2D, StarCircle |
| ![graph-tick](icons/graph-tick.svg) [graph-tick](icons/graph-tick.svg) | 24x24 | 0 0 24 24 | fill | graph canvas (graphIconPathMap) | canvas Path2D, Tick |

## Gaps

### Graph

- **Canvas states are bitmaps.** The graph is drawn on a canvas, and each snapshot holds an image of it. Node fills, rings, edge colours, label placement and the hover title box have no computed style; read them from [raw/graph-code-notes.md](raw/graph-code-notes.md) and measure them off the crops. A node's hit area and the camera are not in the snapshots at all.
- **Drag and box select are only partly captured.** The library snapshots show one state after dragging a node (Positions moved) and the Reset menu. There is no mid-drag frame, no box-select rectangle, no multi-select state and no resize drag.
- **Pan and zoom are one before and after.** Zoomed in is a single snapshot; the zoom steps and the transition between them are not.
- **The author-ring layout** (articles on the map, authors on a ring) was not captured.
- **One screenshot disagrees with a fresh render.** In [library-map-light-positions-reset-menu](screenshots/library-map-light-positions-reset-menu.png) the Positions moved pill is a salmon gradient; rendering the same snapshot file again paints it `#f5c751` (as in library-map-light-positions-moved), and the measurements here use the fresh render. If the live pill turns salmon when its menu is open, that is an animation or a state the snapshot did not keep.

### States

- **Pressed** was measured only on the 2026-10-17 pages (and the top-bar, view toggle, Auto-save and home controls read again there). No captured rule styles `:active` except the slider thumb's cursor, so every pressed state keeps the hover fill.
- **Hover states of the canvas** (a node, an edge) are only in the three hover snapshots; the DOM tooltip is measured, the title box on the canvas is not.
- **Components that did not take focus** (legend chips, the disabled pager and drawer Search button, text tabs that are divs) are named in each entry.
- **Still missing**: an error toast (only the copy toast was raised; the bundle styles an error toast with an orange border), the Sort select list, the Collection and Reading List menus, the share dialog, list scrolling, the drawer opening and closing, and every transition between panels. Only the states captured are measured.
- **Error states.** One inline error was captured: Cannot search, for an article with no citation data, with the incomplete-data chip and banner. Form validation was not reached: the only forms edit the account, and the capture did not submit or empty them. Disabled is measured on Reset Tutorials, the selection actions, the danger button and the disabled pager.

### Themes

Only the light theme was captured. The stylesheets declare dark values (the `--shadow-*-dark` variables and a few others), but no page was captured in dark, so no dark component values exist here.

### Pages and widths

- **Widths.** Pages were read at 1440 x 900, with search at 1000 x 800 and home at 800 x 900. At 640px or less the app covers every page with the Screen too small notice (captured at 390 x 844); there is no phone layout. Between 641px and desktop the frame stays and only the script breakpoints act (home cards stack below 896px, the split view gives way to the list below 1024px); 1024 to 1280 was not captured on its own.
- **Not captured:** sign-in and first-run onboarding (the account is not new, and Reset Tutorials is disabled), billing and plans (paid), the share dialog, the import (BibTeX, Zotero) flows, the authors view, the Reading List with content, and the PDF reader.

### Screenshots and crops

- Article cards show public papers; the workspace name is redacted. The graph bitmap in each crop is the app's own, so two states of the same search can differ in which nodes are labelled.
- Crops and screenshots are 256-colour PNGs; read exact colours from the tables above or from [raw/css-vars.json](raw/css-vars.json), not from the images.
- Images from the app's own `/assets/` (the home page's illustration and guide thumbnails) are allowed through while measuring so the crops show them; no other request is let through.
