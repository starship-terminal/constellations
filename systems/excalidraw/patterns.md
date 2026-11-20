# Excalidraw patterns

How the measured components combine into the signed-out editor. Values are tokens from [tokens.json](tokens.json); the components behind them are in [components.md](components.md).

## One canvas, floating chrome

excalidraw.com serves a single surface: `/` is the editor itself, public and fully usable signed out. The canvas fills the viewport edge to edge (`color.canvas.default-bg`, `#ffffff` light / `#121212` dark, inset 16px by `core.space.editor-pad`); nothing scrolls. Every piece of UI is a floating **Island** — a `control.island.bg` card at `core.radius.lg` (8px) carrying `core.shadow.island`: a hairline, a 3px blur and a soft 14px drop, theme-invariant.

- **Top-centre:** the tool island, `component.toolbar.island-h` 44px of `component.toolbar.button` 36px tools at `core.radius.md` (6px) — Selection, Rectangle, Diamond, Ellipse, Arrow, Line, Draw, Text, Image, Eraser and the extra-tools `…`. The active tool takes `color.brand.light` (the violet wash) with `color.brand.darker` ink; hover is `control.button.hover-bg` (declared = `color.surface.high`). See [tool-island](components/crops/tool-island-default.png), [tool-rect](components/crops/tool-rect-default.png).
- **Top-left:** the hamburger `menu-trigger`, a standalone 36px island. **Top-right:** the Try-Excalidraw+ promo button (`color.brand.promo`, declared = primary), the `color.brand.default` Share button and the library trigger. **Bottom-left:** the zoom pill (`component.footer.zoom-h` 36px) and undo/redo; **bottom-right:** the `?` help button. See [menu-trigger](components/crops/menu-trigger-default.png), [zoom-btn](components/crops/zoom-btn-default.png).

## The main menu

The hamburger opens a 225px dropdown on the same island surface: `component.menu.item-h` 32px rows at `component.menu.item-radius` 6px, hairline separators (`color.border.subtle`), `color.keybinding` gray shortcut hints right-aligned, and violet `color.brand.default` promo rows (Excalidraw+, Sign up). Its foot carries two widgets: the Theme `control.radio.*` trio (sun/moon/system, the selected segment filled `control.radio.choice-on-bg` = primary) and a `canvas-swatches` row of 22px background wells. Preferences flies a 255px submenu of toggles to the right. See [menu-panel](components/crops/menu-panel-default.png), [menu-item](components/crops/menu-item-default.png), [theme-radios](components/crops/theme-radios-default.png), [pref-submenu](components/crops/pref-submenu-default.png).

## The properties sidebar

Picking a shape tool slides in the left properties panel — 195px (`component.props.width`) of sectioned controls on the island surface: labelled rows of 22px `stroke-swatch` and background wells (the checked swatch ringed `color.brand.default`), `stroke-width-group` and stroke-style option trios where the chosen option gets `color.brand.light`, a sloppiness row, an edges pair, the `opacity-slider` (`color.slider.track` hairline, `color.slider.thumb` 20px knob) and the layers row. See [props-panel](components/crops/props-panel-default.png), [stroke-picker](components/crops/stroke-picker-default.png), [opacity-slider](components/crops/opacity-slider-default.png).

## The library panel

The right sidebar is a 294px `control.sidebar.bg` sheet (`component.library.width`) pinned to the viewport edge, `control.sidebar.border` hairline down the left. Its head is a `sidebar-tab-trigger` icon strip — the magnifier tab reveals the `lib-search` field — above the `lib-empty` "No items added yet" state (violet heading over `color.keybinding` gray) and the full-width `color.brand.default` Browse-libraries action. See [lib-panel](components/crops/lib-panel-default.png), [lib-search](components/crops/lib-search-default.png), [lib-browse-btn](components/crops/lib-browse-btn-default.png).

## Dialogs on the scrim

Modals centre a `control.island.bg` card under `core.shadow.modal` over the `color.overlay-bg` scrim (35% ink light, 65% dark).

- **Export image** (~920px): the checkered `control.export.preview-border` preview pane beside a column of `control.switch.*` toggles (Background, Dark mode, Embed scene), a `radiog` scale picker (1×/2×/3×) and a row of `color.brand.default` actions (PNG, SVG, Copy to clipboard) — measured, never pressed. See [export-dialog](components/crops/export-dialog-default.png), [export-switch](components/crops/export-switch-default.png), [export-copy](components/crops/export-copy-default.png).
- **Help / keyboard shortcuts** (~945px): a `color.text-primary` "Help" title row of link pills, then two `shortcut-row` islands listing actions with `kbdpill` keycaps — the same sheet `?` opens. See [shortcuts-dialog](components/crops/shortcuts-dialog-default.png), [keycap](components/crops/keycap-default.png).
- **Command palette** (~718px): a `cmdk-input` field over grouped `cmdk-item` rows (App / Export / Editor), each with its keycap hints — opened by Ctrl+/, never ran a command. See [cmdk-dialog](components/crops/cmdk-dialog-default.png), [cmdk-item](components/crops/cmdk-item-default.png).
- **Find on canvas** (Ctrl+F): a small `control.field.*` search box pinned into the top-right island strip. See [editor-light-find](screenshots/editor-light-find.png).

## The dark theme

The Theme radio flips `.theme--dark` on the app root — a real user theme, persisted to localStorage. ~80 of the ~191 vars rebind: the canvas to near-black `#121212`, the gray roles invert direction, the primary goes `#6965db` → `#a8a5ff` (lighter for contrast), `color.icon.white` goes white → near-black. Same geometry, same shadows; the "Dark theme" component group re-measures the island, menu and sidebar under it. See [editor-dark-editor](screenshots/editor-dark-editor.png), [editor-dark-menu](screenshots/editor-dark-menu.png), [editor-dark-export](screenshots/editor-dark-export.png).

## The mobile fold

At 390 × 844 the chrome collapses to edges: the tool island becomes a 362px `component.mobile.toolbar-h` bottom bar (hand, selection, pen, diamond, rect, arrow, text, `…`), the hamburger a top-left square and the library trigger top-right; the zoom/help row disappears. Picking a shape swaps the bottom bar to `m-shape-actions` (compact stroke/background wells plus a shape sub-row, `component.mobile.actions-h` ~43px). The welcome sheet keeps the Excalifont wordmark and vertical menu. See [mobile-editor-light-default](screenshots/mobile-editor-light-default.png), [mobile-editor-light-shape-actions](screenshots/mobile-editor-light-shape-actions.png), [m-toolbar](components/crops/m-toolbar-default.png).
