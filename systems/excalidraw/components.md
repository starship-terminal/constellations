# Excalidraw components

The discovery list of every view captured, then one entry per component with crops of the real product, and the Gaps. Captured from excalidraw.com on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. excalidraw.com is one public signed-out surface — the drawing editor itself. Nothing was drawn, opened from disk, saved, shared, exported, generated or signed into; Open, Save to, Export actions, Live collaboration, Share, the AI generators, Reset the canvas and every Sign up were measured, never pressed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (76 components, 167 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (163 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `editor-{theme}-{state}.png` — excalidraw.com is a single fixed-height canvas app, nothing scrolls, so there are no `-full` captures. Desktop shots are 1440 x 900 at 1x; mobile shots are `mobile-editor-light-{state}.png`, 780 wide (390 at 2x). `light`/`dark` are the app's own Theme radio states.

| Surface | URL | Screenshots |
|---|---|---|
| Editor | `/` | [editor](screenshots/editor-dark-editor.png), [export](screenshots/editor-dark-export.png), [library](screenshots/editor-dark-library.png), [menu](screenshots/editor-dark-menu.png), [sidebar](screenshots/editor-dark-sidebar.png), [welcome](screenshots/editor-dark-welcome.png), [cmdk](screenshots/editor-light-cmdk.png), [default](screenshots/editor-light-default.png), [editor](screenshots/editor-light-editor.png), [export](screenshots/editor-light-export.png), [find](screenshots/editor-light-find.png), [library](screenshots/editor-light-library.png), [menu-preferences](screenshots/editor-light-menu-preferences.png), [menu](screenshots/editor-light-menu.png), [moretools](screenshots/editor-light-moretools.png), [shortcuts](screenshots/editor-light-shortcuts.png), [sidebar](screenshots/editor-light-sidebar.png), [zoommenu](screenshots/editor-light-zoommenu.png) |
| Editor, phone | `/` | [default](screenshots/mobile-editor-light-default.png), [editor](screenshots/mobile-editor-light-editor.png), [menu](screenshots/mobile-editor-light-menu.png), [shape-actions](screenshots/mobile-editor-light-shape-actions.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Welcome screen | the editor on first run | shown on load; dismissed by picking a tool | [default](screenshots/editor-light-default.png), [welcome](#welcome-screen) |
| Main menu + Preferences submenu | the editor | the hamburger's own toggle; the Preferences item's own submenu | [menu](screenshots/editor-light-menu.png), [menu-preferences](screenshots/editor-light-menu-preferences.png) |
| Extra-tools dropdown | the toolbar | the '…' extra-tools trigger's own toggle | [moretools](screenshots/editor-light-moretools.png), [extra-menu](#extra-tools-menu) |
| Zoom dropdown | the footer | the zoom pill's own toggle | [zoommenu](screenshots/editor-light-zoommenu.png), [zoom-menu](#zoom-menu) |
| Properties sidebar | the editor | selecting the Rectangle tool summons it | [sidebar](screenshots/editor-light-sidebar.png), [props-panel](#properties-panel) |
| Library panel | the editor | the sidebar trigger's own toggle; nothing installed | [library](screenshots/editor-light-library.png), [lib-panel](#library-panel) |
| Export image dialog | menu → Export image… | the menu item opens the local dialog; PNG/SVG/Copy never pressed | [export](screenshots/editor-light-export.png), [export-dialog](#export-dialog) |
| Keyboard shortcuts | menu → Help | the Help item opens the local sheet | [shortcuts](screenshots/editor-light-shortcuts.png), [shortcuts-dialog](#shortcuts-dialog) |
| Command palette | Ctrl+/ | the local launcher dialog; never ran a command | [cmdk](screenshots/editor-light-cmdk.png), [cmdk-dialog](#command-palette) |
| Find on canvas | Ctrl+F | the local search panel; never typed a query | [find](screenshots/editor-light-find.png) |
| Dark theme | the whole editor | the Theme radio's dark choice (localStorage only) | [dark captures](screenshots/editor-dark-editor.png), [Dark theme group](#dark-theme) |
| Excalidraw+ / collaboration | account surfaces | needs an account or a shared session | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 32 components were given a real keyboard focus. 2 draw an outline ring: `plus-btn` (1px auto #101010, offset 1px), `lib-browse-btn` (1px auto #101010, offset 1px). 23 draw a focus ring as a shadow instead: `welcome-item`, `welcome-item-signup`, `menu-trigger`, `tool-lock`, `tool-selection`, `tool-rect`, `tool-draw`, `tool-text`, `tool-eraser`, `tool-more`, `zoom-btn`, `help-btn`, `collab-btn`, `lib-trigger`, `stroke-swatch`, `stroke-choice`, `opacity-slider`, `layer-btn`, `lib-overflow`, `export-png`, `export-svg`, `d-tool`, `export-copy`. The other 7 show no measured change: `extra-menu-item`, `menu-item`, `menu-item-collab`, `canvas-swatch`, `pref-item`, `lib-search`, `cmdk-input`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `ease` | background-color, border-color | plus-btn |
| 0.15s | `ease-out` | all, background, border | export-copy, export-png, export-svg, export-switch |
| 0.25s | `ease` | visibility | menu-trigger, tool-more, zoom-btn |
| 0.25s | `ease-in-out` | opacity | menu-trigger, tool-more, zoom-btn |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Tool island](#tool-island) | 542 x 44 | - | 8px | #ffffff | rgba(0, 0, 0, 0.17) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 3px 0px, rgba(0, 0, 0, 0.05) 0px 7px 14px 0px | 4px |
| [Properties panel](#properties-panel) | 195 x 543 | - | 8px | #ffffff | rgba(0, 0, 0, 0.17) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 3px 0px, rgba(0, 0, 0, 0.05) 0px 7px 14px 0px | 12px |
| [Library panel](#library-panel) | 294 x 900 | L: 1px solid #f1f0ff | - | #ffffff | rgba(0, 0, 0, 0.07) 0px 100px 80px 0px, rgba(0, 0, 0, 0.05) 0px 41.7776px 33.4221px 0px, rgba(0, 0, 0, 0.043) 0px 22.3363px 17.869px 0px, rgba(0, 0, 0, 0.035) 0px 12.5216px 10.0172px 0px, rgba(0, 0, 0, 0.027) 0px 6.6501px 5.32008px 0px, rgba(0, 0, 0, 0.02) 0px 2.76726px 2.21381px 0px | 0 |
| [Main menu](#main-menu) | 225 x 648 | - | - | transparent | none | 0 |
| [Extra tools menu](#extra-tools-menu) | 197 x 376 | - | - | transparent | none | 0 |
| [Preferences submenu](#preferences-submenu) | 255 x 411 | - | - | transparent | none | 0 |
| [Export dialog](#export-dialog) | 919.8 x 396 | - | - | #ffffff | none | 40px |
| [Shortcuts dialog](#shortcuts-dialog) | 945.11 x 807.28 | 1px solid #ebebeb `color.gray.20` | 12px | #ffffff | rgba(0, 0, 0, 0.07) 0px 100px 80px 0px, rgba(0, 0, 0, 0.05) 0px 41.7776px 33.4221px 0px, rgba(0, 0, 0, 0.043) 0px 22.3363px 17.869px 0px, rgba(0, 0, 0, 0.035) 0px 12.5216px 10.0172px 0px, rgba(0, 0, 0, 0.027) 0px 6.6501px 5.32008px 0px, rgba(0, 0, 0, 0.02) 0px 2.76726px 2.21381px 0px | 0 |
| [Command palette](#command-palette) | 718 x 748 | - | - | #ffffff | none | 24px |
| [Welcome screen](#welcome-screen) | 1408 x 868 | - | - | transparent | none | 0 |

## Components

### Welcome screen (first run)

The first-run overlay centred on the blank canvas: the Excalifont wordmark logo, the browser-storage note and the vertical Open/Help/Live-collaboration/Sign-up menu — its actions were never pressed.

#### Welcome screen
The first-run overlay centred on the blank canvas: the excalifont logo, a storage note and a vertical menu. Read as `welcome-panel` on the welcome page.

**Values (default).** size 1408 x 868; background transparent; text Excalifont 18/21.6 400, #b8b8b8 `color.gray.40`; icon 40 x 40, #6965db; layers button.welcome-screen-menu-item 300.0x42.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 6px; button.welcome-screen-menu-item 300.0x42.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 6px; button.welcome-screen-menu-item 300.0x42.0 T:1px solid rgba(.

Child layers that carry the look: button 300x42 border 1px solid transparent radius 6px; button 300x42 border 1px solid transparent radius 6px; button 300x42 border 1px solid transparent radius 6px.

![Welcome screen default](components/crops/welcome-panel-default.png)

#### Welcome logo
The hand-drawn "Excalidraw" wordmark in Excalifont. Read as `welcome-logo` on the welcome page.

**Values (default).** size 281.08 x 40; background transparent; text Excalifont 36/normal 400, #b8b8b8 `color.gray.40`; icon 40 x 40, #6965db.

![Welcome logo default](components/crops/welcome-logo-default.png)

#### Welcome heading
"Your drawings are saved in your browser's storage." — the privacy note under the logo. Read as `welcome-heading` on the welcome page.

**Values (default).** size 453 x 64.78; background transparent; text Excalifont 18/21.6 400, #b8b8b8 `color.gray.40`.

![Welcome heading default](components/crops/welcome-heading-default.png)

#### Welcome menu
The stacked menu inside the welcome card (Open, Help, Live collaboration…, Sign up). Read as `welcome-menu` on the welcome page.

**Values (default).** size 1408 x 868; background transparent; text Excalifont 18/21.6 400, #b8b8b8 `color.gray.40`; icon 40 x 40, #6965db; layers button.welcome-screen-menu-item 300.0x42.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 6px; button.welcome-screen-menu-item 300.0x42.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 6px; button.welcome-screen-menu-item 300.0x42.0 T:1px solid rgba(.

Child layers that carry the look: button 300x42 border 1px solid transparent radius 6px; button 300x42 border 1px solid transparent radius 6px; button 300x42 border 1px solid transparent radius 6px.

![Welcome menu default](components/crops/welcome-menu-default.png)

#### Welcome menu item
The "Help" welcome item — a plain row with an icon; measured, its action never used. Read as `welcome-item` on the welcome page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 300 x 42; padding 12px; border 1px solid transparent; radius 6px; background transparent; text Arial 14/normal 400, #999999 `color.gray.50`; icon 16 x 16, #999999 `color.gray.50` |
| hover | background #f1f0ff; text Arial 14/normal 400, #121212 `color.gray.100`; icon 16 x 16, #121212 `color.gray.100` |
| focus-visible | shadow #5753d0 0px 0px 0px 1px |
| pressed | border 1px solid #4440bf; background #f1f0ff; text Arial 14/normal 400, #121212 `color.gray.100`; icon 16 x 16, #121212 `color.gray.100` |

![Welcome menu item default](components/crops/welcome-item-default.png) ![Welcome menu item hover](components/crops/welcome-item-hover.png) ![Welcome menu item focus-visible](components/crops/welcome-item-focus-visible.png) ![Welcome menu item pressed](components/crops/welcome-item-pressed.png)

#### Welcome Sign-up item
The "Sign up" welcome item — links to Excalidraw+ signup; measured never followed. Read as `welcome-item-signup` on the welcome page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 300 x 44; padding 12px; border 1px solid transparent; radius 6px; background transparent; text Assistant 14/normal 500, #999999 `color.gray.50`; icon 16 x 16, #999999 `color.gray.50` |
| hover | background #f1f0ff; text Assistant 14/normal 500, #121212 `color.gray.100`; icon 16 x 16, #121212 `color.gray.100` |
| focus-visible | shadow #5753d0 0px 0px 0px 1px |
| pressed | border 1px solid #4440bf; background #f1f0ff; text Assistant 14/normal 500, #121212 `color.gray.100`; icon 16 x 16, #121212 `color.gray.100` |

![Welcome Sign-up item default](components/crops/welcome-item-signup-default.png) ![Welcome Sign-up item hover](components/crops/welcome-item-signup-hover.png) ![Welcome Sign-up item focus-visible](components/crops/welcome-item-signup-focus-visible.png) ![Welcome Sign-up item pressed](components/crops/welcome-item-signup-pressed.png)

### Toolbar Islands

The floating Islands chrome: the 44px tool island with its 36px tool buttons (Selection through Eraser plus the extra-tools trigger), the hamburger and the library trigger.

#### Tool island
The floating toolbar Island: a rounded shadowed card holding the tool buttons in a row. Read as `tool-island` on the editor page.

**Values (default).** size 542 x 44; padding 4px; radius 8px; background #ffffff; shadow rgba(0, 0, 0, 0.17) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 3px 0px, rgba(0, 0, 0, 0.05) 0px 7px 14px 0px; text Assistant 10/normal 400, #b8b8b8 `color.gray.40`; icon 16 x 16, #1b1b1f.

![Tool island default](components/crops/tool-island-default.png)

#### Hamburger trigger
The main-menu icon button at the toolbar head. Read as `menu-trigger` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; padding 10px; radius 8px; background #ececf4; shadow #ffffff 0px 0px 0px 1px; text Assistant 13.33/normal 400, #1b1b1f; transition opacity 0.25s ease-in-out, visibility 0.25s ease; icon 16 x 16, #1b1b1f |
| hover | background #f1f0ff |
| focus-visible | shadow #5753d0 0px 0px 0px 1px |
| pressed | background #f1f0ff; shadow #4440bf 0px 0px 0px 1px |

![Hamburger trigger default](components/crops/menu-trigger-default.png) ![Hamburger trigger hover](components/crops/menu-trigger-hover.png) ![Hamburger trigger focus-visible](components/crops/menu-trigger-focus-visible.png) ![Hamburger trigger pressed](components/crops/menu-trigger-pressed.png)

#### Tool lock
The "Keep selected tool active" lock checkbox at the toolbar head. Read as `tool-lock` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; radius 8px; background transparent; text Assistant 16/normal 400, #1b1b1f; icon 16 x 16, #1b1b1f |
| hover | layers div.ToolIcon__icon 36.0x36.0 rgb(241, 240, 255) 8px |
| focus-visible | shadow #a5d8ff 0px 0px 0px 2px; layers button.ToolIcon.ToolIcon_type_toggle 36.0x36.0 rgb(165, 216, 255) 0px 0px 0px 2px 8px |

![Tool lock default](components/crops/tool-lock-default.png) ![Tool lock hover](components/crops/tool-lock-hover.png) ![Tool lock focus-visible](components/crops/tool-lock-focus-visible.png)

#### Selection tool
The Selection tool button — the active tool after entering the editor, so its selected state is the resting one. Read as `tool-selection` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 36 x 36; radius 8px; background transparent; text Assistant 10/normal 400, #b8b8b8 `color.gray.40`; icon 16 x 16, #1b1b1f |
| hover | layers div.ToolIcon__icon 36.0x36.0 rgb(241, 240, 255) 8px |
| focus-visible | shadow #a5d8ff 0px 0px 0px 2px; layers button.ToolIcon.ToolIcon_type_toggle 36.0x36.0 rgb(165, 216, 255) 0px 0px 0px 2px 8px |
| selected | text Assistant 10/normal 400, #030064; icon 16 x 16, #030064; layers div.ToolIcon__icon 36.0x36.0 rgb(224, 223, 255) 8px |

![Selection tool default](components/crops/tool-selection-default.png) ![Selection tool hover](components/crops/tool-selection-hover.png) ![Selection tool focus-visible](components/crops/tool-selection-focus-visible.png) ![Selection tool pressed](components/crops/tool-selection-pressed.png) ![Selection tool selected](components/crops/tool-selection-selected.png)

#### Rectangle tool
A shape tool button; selecting it also summons the properties sidebar (a local selection, nothing drawn). Read as `tool-rect` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 36 x 36; radius 8px; background transparent; text Assistant 10/normal 400, #b8b8b8 `color.gray.40`; icon 16 x 16, #1b1b1f |
| hover | layers div.ToolIcon__icon 36.0x36.0 rgb(241, 240, 255) 8px |
| focus-visible | shadow #a5d8ff 0px 0px 0px 2px; layers button.ToolIcon.ToolIcon_type_toggle 36.0x36.0 rgb(165, 216, 255) 0px 0px 0px 2px 8px |
| selected | text Assistant 10/normal 400, #030064; icon 16 x 16, #030064; layers div.ToolIcon__icon 36.0x36.0 rgb(224, 223, 255) 8px |

![Rectangle tool default](components/crops/tool-rect-default.png) ![Rectangle tool hover](components/crops/tool-rect-hover.png) ![Rectangle tool focus-visible](components/crops/tool-rect-focus-visible.png) ![Rectangle tool pressed](components/crops/tool-rect-pressed.png) ![Rectangle tool selected](components/crops/tool-rect-selected.png)

#### Draw tool
The freedraw pen tool button. Read as `tool-draw` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 36 x 36; radius 8px; background transparent; text Assistant 10/normal 400, #b8b8b8 `color.gray.40`; icon 16 x 16, #1b1b1f |
| hover | layers div.ToolIcon__icon 36.0x36.0 rgb(241, 240, 255) 8px |
| focus-visible | shadow #a5d8ff 0px 0px 0px 2px; layers button.ToolIcon.ToolIcon_type_toggle 36.0x36.0 rgb(165, 216, 255) 0px 0px 0px 2px 8px |

![Draw tool default](components/crops/tool-draw-default.png) ![Draw tool hover](components/crops/tool-draw-hover.png) ![Draw tool focus-visible](components/crops/tool-draw-focus-visible.png) ![Draw tool pressed](components/crops/tool-draw-pressed.png)

#### Text tool
The text tool button. Read as `tool-text` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 36 x 36; radius 8px; background transparent; text Assistant 10/normal 400, #b8b8b8 `color.gray.40`; icon 16 x 16, #1b1b1f |
| hover | layers div.ToolIcon__icon 36.0x36.0 rgb(241, 240, 255) 8px |
| focus-visible | shadow #a5d8ff 0px 0px 0px 2px; layers button.ToolIcon.ToolIcon_type_toggle 36.0x36.0 rgb(165, 216, 255) 0px 0px 0px 2px 8px |

![Text tool default](components/crops/tool-text-default.png) ![Text tool hover](components/crops/tool-text-hover.png) ![Text tool focus-visible](components/crops/tool-text-focus-visible.png) ![Text tool pressed](components/crops/tool-text-pressed.png)

#### Eraser tool
The eraser tool button. Read as `tool-eraser` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 36 x 36; radius 8px; background transparent; text Assistant 10/normal 400, #b8b8b8 `color.gray.40`; icon 16 x 16, #1b1b1f |
| hover | layers div.ToolIcon__icon 36.0x36.0 rgb(241, 240, 255) 8px |
| focus-visible | shadow #a5d8ff 0px 0px 0px 2px; layers button.ToolIcon.ToolIcon_type_toggle 36.0x36.0 rgb(165, 216, 255) 0px 0px 0px 2px 8px |

![Eraser tool default](components/crops/tool-eraser-default.png) ![Eraser tool hover](components/crops/tool-eraser-hover.png) ![Eraser tool focus-visible](components/crops/tool-eraser-focus-visible.png) ![Eraser tool pressed](components/crops/tool-eraser-pressed.png)

#### Extra tools trigger
The "Extra tools" overflow button at the toolbar tail — a local dropdown toggle. Read as `tool-more` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, opened) | size 36 x 36; padding 10px; radius 8px; background transparent; text Assistant 13.33/normal 400, #1b1b1f; transition opacity 0.25s ease-in-out, visibility 0.25s ease; icon 16 x 16, #1b1b1f |
| focus-visible | shadow #5753d0 0px 0px 0px 1px; layers button.dropdown-menu-button.App-toolbar__extra-tools-trigger 36.0x36.0 rgb(87, 83, 208) 0px 0px 0px 1px 8px |
| pressed | shadow #4440bf 0px 0px 0px 1px inset; layers button.dropdown-menu-button.App-toolbar__extra-tools-trigger 36.0x36.0 rgb(68, 64, 191) 0px 0px 0px 1px inset 8px |

![Extra tools trigger default](components/crops/tool-more-default.png) ![Extra tools trigger hover](components/crops/tool-more-hover.png) ![Extra tools trigger focus-visible](components/crops/tool-more-focus-visible.png) ![Extra tools trigger pressed](components/crops/tool-more-pressed.png) ![Extra tools trigger opened](components/crops/tool-more-opened.png)

#### Library trigger
The "Library" sidebar button top-right — a local panel toggle. Read as `lib-trigger` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed, opened) | size 36 x 36; background transparent; text Assistant 16/normal 400, #1b1b1f; icon 16 x 16, #1b1b1f; layers div.sidebar-trigger.default-sidebar-trigger 36.0x36.0 rgb(236, 236, 244) rgb(255, 255, 255) 0px 0px 0px 1px 8px |
| hover | layers div.sidebar-trigger.default-sidebar-trigger 36.0x36.0 rgb(241, 240, 255) rgb(255, 255, 255) 0px 0px 0px 1px 8px |
| focus-visible | shadow #5753d0 0px 0px 0px 1px; layers button.sidebar-trigger__label-element 36.0x36.0 rgb(87, 83, 208) 0px 0px 0px 1px; div.sidebar-trigger.default-sidebar-trigger 36.0x36.0 rgb(236, 236, 244) rgb(255, 255, 255) 0px 0px 0px 1px 8px |

Child layers that carry the look: div 36x36 background #ececf4 radius 8px shadow #ffffff 0px 0px 0px 1px.

![Library trigger default](components/crops/lib-trigger-default.png) ![Library trigger hover](components/crops/lib-trigger-hover.png) ![Library trigger focus-visible](components/crops/lib-trigger-focus-visible.png) ![Library trigger pressed](components/crops/lib-trigger-pressed.png) ![Library trigger opened](components/crops/lib-trigger-opened.png)

### Main menu and dropdowns

The hamburger dropdown and what hangs off it: the Open/Save/Export/Collaborate items (measured never pressed), the Preferences submenu, the Theme radio trio and the Canvas-background swatches; also the toolbar's extra-tools and zoom dropdowns.

#### Extra tools menu
The extra-tools dropdown (Insert image, Frame, Web Embed, Draw to shape, Laser, plus the AI entries); its items were measured never pressed. Read as `extra-menu` on the editor page.

**Values (default).** size 197 x 376; background transparent; text Assistant 14/normal 400, #1b1b1f; icon 16 x 16, #1b1b1f; layers div.Island.dropdown-menu-container 197.0x376.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.17) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 3px 0px, rgba(0, 0, 0, 0.05) 0px 7px 14px 0px 8px; div.DropDownMenuItemBadge 20.0x16.0 rgb(105, 101, 219) T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, 255, 255) 6px; div.DropDownMenuItemBadge 20.

Child layers that carry the look: div 197x376 background #ffffff radius 8px shadow rgba(0, 0, 0, 0.17) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 3px 0px, rgba(0, 0, 0, 0.05) 0px 7px 14px 0px; div 20x16 background #6965db border 1px solid #ffffff radius 6px; div 20x16 background #6965db border 1px solid #ffffff radius 6px.

![Extra tools menu default](components/crops/extra-menu-default.png)

#### Extra menu item
A row inside the extra-tools dropdown (Lasso selection); measured, never pressed. Read as `extra-menu-item` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 181 x 32; padding 0px 8px; radius 6px; background transparent; text Assistant 14/normal 400, #1b1b1f; icon 16 x 16, #1b1b1f |
| hover, focus-visible | background #f1f0ff |

![Extra menu item default](components/crops/extra-menu-item-default.png) ![Extra menu item hover](components/crops/extra-menu-item-hover.png) ![Extra menu item focus-visible](components/crops/extra-menu-item-focus-visible.png)

#### Main menu
The hamburger dropdown: Open / Save to disk / Export image… / Live collaboration / Command palette / Help, then Preferences, Theme, Language and the canvas-background swatches. Read as `menu-panel` on the editor page.

**Values (default).** size 225 x 648; background transparent; text Assistant 14/normal 400, #1b1b1f; icon 16 x 16, #1b1b1f; layers div.Island.dropdown-menu-container 225.0x648.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.17) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 3px 0px, rgba(0, 0, 0, 0.05) 0px 7px 14px 0px 8px; div 209.0x1.0 rgb(241, 240, 255); div 209.0x1.0 rgb(241, 240, 255); div.RadioGroup 108.0x32.0 rgb(255, 255, 255) T:1px solid rgb(241, 240, 255) / R:1px solid rgb(241, 240, 255) / B:1px solid rgb(241, 240, 255) / L:1px .

Child layers that carry the look: div 225x648 background #ffffff radius 8px shadow rgba(0, 0, 0, 0.17) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 3px 0px, rgba(0, 0, 0, 0.05) 0px 7px 14px 0px; div 209x1 background #f1f0ff; div 209x1 background #f1f0ff.

![Main menu default](components/crops/menu-panel-default.png)

#### Menu item
The "Open" menu row (icon + label); measured, never pressed. Read as `menu-item` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 209 x 32; padding 0px 8px; radius 6px; background transparent; text Assistant 14/normal 400, #1b1b1f; icon 16 x 16, #1b1b1f |
| hover, focus-visible | background #f1f0ff |

![Menu item default](components/crops/menu-item-default.png) ![Menu item hover](components/crops/menu-item-hover.png) ![Menu item focus-visible](components/crops/menu-item-focus-visible.png)

#### Collaboration item
"Live collaboration…" — would start a session; measured never pressed. Read as `menu-item-collab` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 209 x 32; padding 0px 8px; radius 6px; background transparent; text Assistant 14/normal 400, #1b1b1f; icon 16 x 16, #1b1b1f |
| hover, focus-visible | background #f1f0ff |

![Collaboration item default](components/crops/menu-item-collab-default.png) ![Collaboration item hover](components/crops/menu-item-collab-hover.png) ![Collaboration item focus-visible](components/crops/menu-item-collab-focus-visible.png)

#### Menu separator
The hairline divider between menu groups. Read as `menu-sep` on the editor page.

**Values (default).** size 209 x 1; background #f1f0ff; text Assistant 16/normal 400, #1b1b1f.

![Menu separator default](components/crops/menu-sep-default.png)

#### Theme radio group
The Light/Dark/System radio row inside the menu — the real theme control (Dark is set for the dark page, never left on). Read as `theme-radios` on the editor page.

**Values (default).** size 108 x 32; padding 3px; border 1px solid #f1f0ff; radius 10px; background #ffffff; text Assistant 14/normal 400, #1b1b1f; icon 16 x 16, #ffffff.

![Theme radio group default](components/crops/theme-radios-default.png)

#### Theme radio choice
A choice in the Theme radio group (Dark); measured at rest. Read as `theme-choice` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 24; padding 0px 6px; radius 8px; background #ffffff; text Assistant 12/12 600, #6965db; icon 16 x 16, #6965db |
| hover | text Assistant 12/12 600, #5753d0; icon 16 x 16, #5753d0 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Theme radio choice default](components/crops/theme-choice-default.png) ![Theme radio choice hover](components/crops/theme-choice-hover.png)

#### Canvas background picker
The canvas-background colour row at the menu foot — a strip of preset swatches. Read as `canvas-swatches` on the editor page.

**Values (default).** size 189 x 34; padding 4px 0px; background transparent; text Assistant 16/normal 400, #1b1b1f; layers button.color-picker__button.top-picks-dnd__pick 22.0x22.0 rgb(255, 255, 255) rgb(235, 235, 235) 0px 0px 0px 1px 4px; div.color-picker__button-outline 24.0x24.0 rgb(74, 71, 177) 0px 0px 0px 1px 4px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 rgb(248, 249, 250) rgb(235, 235, 235) 0px 0px 0px 1px 4px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 rgb(245, 250, 255) rgb(235,.

Child layers that carry the look: button 22x22 background #ffffff radius 4px shadow #ebebeb `color.gray.20` 0px 0px 0px 1px; div 24x24 radius 4px shadow #4a47b1 0px 0px 0px 1px; button 22x22 background #f8f9fa radius 4px shadow #ebebeb `color.gray.20` 0px 0px 0px 1px.

![Canvas background picker default](components/crops/canvas-swatches-default.png)

#### Canvas swatch
One preset swatch in the canvas-background picker; measured, never set. Read as `canvas-swatch` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 22 x 22; radius 4px; background #ffffff; shadow #ebebeb 0px 0px 0px 1px; text Assistant 13.33/normal 400, #000000 |
| focus-visible | layers ::after rgba(0, 0, 0, 0) 3px none 1 |

![Canvas swatch default](components/crops/canvas-swatch-default.png) ![Canvas swatch hover](components/crops/canvas-swatch-hover.png) ![Canvas swatch focus-visible](components/crops/canvas-swatch-focus-visible.png)

#### Preferences submenu
The Preferences submenu (Zen mode, View mode, Grid mode, snapping, stats); toggles measured never set. Read as `pref-submenu` on the editor page.

**Values (default).** size 255 x 411; background transparent; text Assistant 14/normal 400, #1b1b1f; icon 16 x 16, #1b1b1f; layers div.Island.dropdown-menu-container 255.0x411.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.17) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 3px 0px, rgba(0, 0, 0, 0.05) 0px 7px 14px 0px 8px; div.RadioGroup 105.4x32.0 rgb(255, 255, 255) T:1px solid rgb(241, 240, 255) / R:1px solid rgb(241, 240, 255) / B:1px solid rgb(241, 240, 255) / L:1px solid rgb(241, 240, 255) 10px; div.RadioGroup__choice.active 40.6x24.

Child layers that carry the look: div 255x411 background #ffffff radius 8px shadow rgba(0, 0, 0, 0.17) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 3px 0px, rgba(0, 0, 0, 0.05) 0px 7px 14px 0px; div 105.4x32 background #ffffff border 1px solid #f1f0ff radius 10px; div 40.6x24 background #6965db radius 8px.

![Preferences submenu default](components/crops/pref-submenu-default.png)

#### Preference item
A togglable submenu row (Zen mode); measured, never set. Read as `pref-item` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 239 x 32; padding 0px 8px; radius 6px; background transparent; text Assistant 14/normal 400, #1b1b1f |
| hover, focus-visible | background #f1f0ff |

![Preference item default](components/crops/pref-item-default.png) ![Preference item hover](components/crops/pref-item-hover.png) ![Preference item focus-visible](components/crops/pref-item-focus-visible.png)

### Footer bar

The bottom chrome: the zoom pill and its dropdown, undo/redo, the '?' help button, the Share and Try-Excalidraw+ buttons — pressed states forced, never triggered.

#### Undo button
The Undo footer button — disabled on a blank canvas, which is its resting reading. Read as `undo-btn` on the editor page.

**Values (default).** size 36 x 36; radius 8px 0px 0px 8px; background transparent; text Arial 14/normal 400, rgba(16, 16, 16, 0.3); icon 16 x 16, #b8b8b8 `color.gray.40`.

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Undo button default](components/crops/undo-btn-default.png)

#### Redo button
The Redo footer button — disabled at rest like Undo. Read as `redo-btn` on the editor page.

**Values (default).** size 36 x 36; radius 0px 8px 8px 0px; background transparent; text Arial 14/normal 400, rgba(16, 16, 16, 0.3); icon 16 x 16, #b8b8b8 `color.gray.40`.

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Redo button default](components/crops/redo-btn-default.png)

#### Zoom control
The "− 100% +" zoom pill bottom-left; the opened state is its dropdown (Zen/grid/snap toggles), measured never set. Read as `zoom-btn` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 60 x 36; padding 0px 10px; radius 8px 0px 0px 8px; background transparent; text Assistant 14/normal 400, #1b1b1f; transition opacity 0.25s ease-in-out, visibility 0.25s ease |
| hover | background #f1f0ff |
| focus-visible | shadow #5753d0 0px 0px 0px 1px inset; layers button.dropdown-menu-button.zoom-menu-trigger 60.0x36.0 rgb(87, 83, 208) 0px 0px 0px 1px inset 8px 0px 0px 8px |
| pressed | background #f1f0ff; shadow #6965db 0px 0px 0px 1px inset |
| opened | background #f1f0ff |

![Zoom control default](components/crops/zoom-btn-default.png) ![Zoom control hover](components/crops/zoom-btn-hover.png) ![Zoom control focus-visible](components/crops/zoom-btn-focus-visible.png) ![Zoom control pressed](components/crops/zoom-btn-pressed.png) ![Zoom control opened](components/crops/zoom-btn-opened.png)

#### Zoom menu
The zoom footer dropdown (Zoom in/out, Zen mode, Grid, snapping); opened by its own trigger, toggles never set. Read as `zoom-menu` on the editor page.

**Values (default).** size 218 x 194; background transparent; text Assistant 14/normal 400, #1b1b1f; icon 16 x 16, #1b1b1f; layers div.Island.dropdown-menu-container 218.0x194.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.17) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 3px 0px, rgba(0, 0, 0, 0.05) 0px 7px 14px 0px 8px; div 202.0x1.0 rgb(241, 240, 255).

Child layers that carry the look: div 218x194 background #ffffff radius 8px shadow rgba(0, 0, 0, 0.17) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 3px 0px, rgba(0, 0, 0, 0.05) 0px 7px 14px 0px; div 202x1 background #f1f0ff.

![Zoom menu default](components/crops/zoom-menu-default.png)

#### Help button
The "?" help icon button bottom-right. Read as `help-btn` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; padding 10px; radius 8px; background #ececf4; shadow #ffffff 0px 0px 0px 1px; text Assistant 13.33/normal 400, #1b1b1f; icon 16 x 16, #1b1b1f |
| hover | background #f1f0ff |
| focus-visible | shadow #5753d0 0px 0px 0px 1px |
| pressed | background #f1f0ff; shadow #4440bf 0px 0px 0px 1px |

![Help button default](components/crops/help-btn-default.png) ![Help button hover](components/crops/help-btn-hover.png) ![Help button focus-visible](components/crops/help-btn-focus-visible.png) ![Help button pressed](components/crops/help-btn-pressed.png)

#### Share button
The purple "Share"/collaboration button — opens a session dialog, never pressed. Read as `collab-btn` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 55 x 36; padding 10px; border 1px solid #6965db; radius 8px; background #6965db; shadow #ffffff 0px 0px 0px 1px; text Assistant 13.33/normal 400, #ffffff |
| hover | border 1px solid #5b57d1; background #5b57d1 |
| focus-visible | shadow #5753d0 0px 0px 0px 1px |

![Share button default](components/crops/collab-btn-default.png) ![Share button hover](components/crops/collab-btn-hover.png) ![Share button focus-visible](components/crops/collab-btn-focus-visible.png)

#### Excalidraw+ promo
The Excalidraw+ upsell action; measured never followed. Read as `plus-btn` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 148 x 36; padding 0px 14px 0px 10px; border 1px solid #d7d5ff; radius 8px; background #f0efff; text Assistant 14/16.1 600, #6965db; transition background-color 0.15s ease, border-color 0.15s ease; icon 20 x 20, #6965db |
| hover | border 1px solid #e3e2fe; background #e3e2fe |
| focus-visible | outline 1px auto #101010, offset 1px |

![Excalidraw+ promo default](components/crops/plus-btn-default.png) ![Excalidraw+ promo hover](components/crops/plus-btn-hover.png) ![Excalidraw+ promo focus-visible](components/crops/plus-btn-focus-visible.png)

### Properties sidebar

The left shape-properties panel a shape tool summons: stroke and background swatches, stroke width/style, sloppiness, edges, opacity slider and the layers row.

#### Properties panel
The left sidebar summoned by picking a shape tool: Stroke and Background pickers, Stroke width/style, Sloppiness, Edges, Opacity, Layers. Read as `props-panel` on the editor page.

**Values (default).** size 195 x 543; padding 12px; radius 8px; background #ffffff; shadow rgba(0, 0, 0, 0.17) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 3px 0px, rgba(0, 0, 0, 0.05) 0px 7px 14px 0px; text Assistant 12/normal 400, #1b1b1f; icon 16 x 16, #1b1b1f.

![Properties panel default](components/crops/props-panel-default.png)

#### Property label
A section label ("Stroke") inside the properties panel. Read as `prop-label` on the editor page.

**Values (default).** size 63 x 15; background transparent; text Assistant 12/normal 400, #1b1b1f.

![Property label default](components/crops/prop-label-default.png)

#### Stroke colour picker
The Stroke top-picks row: five preset swatches plus the custom picker button. Read as `stroke-picker` on the editor page.

**Values (default).** size 171 x 34; padding 4px 0px; background transparent; text Assistant 16/normal 400, #1b1b1f; layers button.color-picker__button.top-picks-dnd__pick 22.0x22.0 rgb(30, 30, 30) 4px; div.color-picker__button-outline 24.0x24.0 rgb(74, 71, 177) 0px 0px 0px 1px 4px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 rgb(224, 49, 49) 4px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 rgb(47, 158, 68) 4px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 rgb(25, 113, 194) 4px;.

Child layers that carry the look: button 22x22 background #1e1e1e `color.gray.90` radius 4px; div 24x24 radius 4px shadow #4a47b1 0px 0px 0px 1px; button 22x22 background #e03131 radius 4px.

![Stroke colour picker default](components/crops/stroke-picker-default.png)

#### Stroke swatch
A preset colour swatch in the Stroke picker — the selected one carries the accent ring. Read as `stroke-swatch` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 22 x 22; radius 4px; background #1e1e1e `color.gray.90`; text Assistant 13.33/normal 400, #000000 |
| focus-visible | shadow #5753d0 0px 0px 0px 1px; layers ::after rgba(0, 0, 0, 0) 3px none 1 |

![Stroke swatch default](components/crops/stroke-swatch-default.png) ![Stroke swatch hover](components/crops/stroke-swatch-hover.png) ![Stroke swatch focus-visible](components/crops/stroke-swatch-focus-visible.png)

#### Stroke width radio
The Stroke-width segmented control (thin/bold/extra-bold icons). Read as `stroke-width-group` on the editor page.

**Values (default).** size 171 x 59; background transparent; text Assistant 12/normal 400, #1b1b1f; icon 16 x 16, #1b1b1f; layers label 32.0x32.0 rgb(246, 246, 249) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 8px; label.active 32.0x32.0 rgb(224, 223, 255) T:1px solid rgb(224, 223, 255) / R:1px solid rgb(224, 223, 255) / B:1px solid rgb(224, 223, 255) / L:1px solid rgb(224, 223, 255) 8px; label 32.0x32.0 rgb(246, 246, 249) T:1px solid rgba(0, 0, 0, .

Child layers that carry the look: label 32x32 background #f6f6f9 border 1px solid transparent radius 8px; label 32x32 background #e0dfff border 1px solid #e0dfff radius 8px; label 32x32 background #f6f6f9 border 1px solid transparent radius 8px.

![Stroke width radio default](components/crops/stroke-width-group-default.png)

#### Stroke width choice
A choice inside a properties RadioGroup — the active choice paints the accent background. Read as `stroke-choice` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 32 x 32; border 1px solid #e0dfff; radius 8px; background #e0dfff; text Assistant 12/normal 400, #1b1b1f; icon 16 x 16, #030064 |
| focus-visible | shadow #5753d0 0px 0px 0px 1px |

![Stroke width choice default](components/crops/stroke-choice-default.png) ![Stroke width choice hover](components/crops/stroke-choice-hover.png) ![Stroke width choice focus-visible](components/crops/stroke-choice-focus-visible.png)

#### Opacity control
The Opacity row: a range slider and a numeric input. Read as `opacity-row` on the editor page.

**Values (default).** size 171 x 58; background transparent; text Assistant 12/normal 400, #1b1b1f; layers input.range-input 171.0x4.0 2px.

Child layers that carry the look: input 171x4 image linear-gradient(to right, #ccccff calc(100%), #f6f6f9 calc(100%)) radius 2px.

![Opacity control default](components/crops/opacity-row-default.png)

#### Opacity slider
The range input inside the Opacity control. Read as `opacity-slider` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 171 x 4; radius 2px; background transparent; image linear-gradient(to right, #ccccff calc(100%), #f6f6f9 calc(100%)); text Arial 13.33/normal 400, #9d968e; placeholder #9d968e |
| focus-visible | shadow #5753d0 0px 0px 0px 1px |

![Opacity slider default](components/crops/opacity-slider-default.png) ![Opacity slider focus-visible](components/crops/opacity-slider-focus-visible.png)

#### Layers row
The Layers section: bring-forward/send-backward icon buttons. Read as `layers-row` on the editor page.

**Values (default).** size 171 x 59; background transparent; text Assistant 12/normal 400, #1b1b1f; icon 16 x 16, #1b1b1f; layers button.zIndexButton 32.0x32.0 rgb(246, 246, 249) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 8px; button.zIndexButton 32.0x32.0 rgb(246, 246, 249) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 8px; button.zIndexButton 32.0x32.0 rgb(246, 246, 249).

Child layers that carry the look: button 32x32 background #f6f6f9 border 1px solid transparent radius 8px; button 32x32 background #f6f6f9 border 1px solid transparent radius 8px; button 32x32 background #f6f6f9 border 1px solid transparent radius 8px.

![Layers row default](components/crops/layers-row-default.png)

#### Layer action
A z-order icon button in the Layers row. Read as `layer-btn` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; border 1px solid transparent; radius 8px; background #f6f6f9; text Assistant 13.33/normal 400, #1b1b1f; icon 16 x 16, #1b1b1f |
| hover | background #f1f0ff |
| focus-visible | shadow #5753d0 0px 0px 0px 1px |
| pressed | border 1px solid #4440bf; background #f1f0ff |

![Layer action default](components/crops/layer-btn-default.png) ![Layer action hover](components/crops/layer-btn-hover.png) ![Layer action focus-visible](components/crops/layer-btn-focus-visible.png) ![Layer action pressed](components/crops/layer-btn-pressed.png)

### Library panel

The right-hand library sidebar: the tab strip with the search field it reveals, the 'No items added yet' empty state, Browse libraries and the overflow menu — nothing installed.

#### Library panel
The right sidebar holding the shape library: a search field, the empty state and "Browse libraries" — nothing was installed. Read as `lib-panel` on the editor page.

**Values (default).** size 294 x 900; border L: 1px solid #f1f0ff; background #ffffff; shadow rgba(0, 0, 0, 0.07) 0px 100px 80px 0px, rgba(0, 0, 0, 0.05) 0px 41.7776px 33.4221px 0px, rgba(0, 0, 0, 0.043) 0px 22.3363px 17.869px 0px, rgba(0, 0, 0, 0.035) 0px 12.5216px 10.0172px 0px, rgba(0, 0, 0, 0.027) 0px 6.6501px 5.32008px 0px, rgba(0, 0, 0, 0.02) 0px 2.76726px 2.21381px 0px; text Assistant 18/27 700, #6965db; icon 16 x 16, #1b1b1f.

![Library panel default](components/crops/lib-panel-default.png)

#### Library search
The search field revealed by the first tab button at the library head; focused, never submitted. Read as `lib-search` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 217 x 24; background transparent; text Assistant 16/24 400, #1b1b1f; placeholder #757575 |

![Library search default](components/crops/lib-search-default.png) ![Library search focus-visible](components/crops/lib-search-focus-visible.png)

#### Library empty state
The "no shapes yet" empty-state text inside the panel. Read as `lib-empty` on the editor page.

**Values (default).** size 265 x 68; padding 16px 0px; background transparent; text Assistant 12/normal 600, #ffffff; layers a.library-menu-browse-button 265.0x36.0 rgb(105, 101, 219) 8px.

Child layers that carry the look: a 265x36 background #6965db radius 8px.

![Library empty state default](components/crops/lib-empty-default.png)

#### Browse libraries button
The "Browse libraries" action — opens the community libraries list; measured never followed. Read as `lib-browse-btn` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 265 x 36; radius 8px; background #6965db; text Assistant 12/normal 600, #ffffff |
| hover | background #5753d0 |
| focus-visible | background #5753d0; outline 1px auto #101010, offset 1px |
| pressed | background #4440bf; outline 1px auto #101010, offset 1px |

![Browse libraries button default](components/crops/lib-browse-btn-default.png) ![Browse libraries button hover](components/crops/lib-browse-btn-hover.png) ![Browse libraries button focus-visible](components/crops/lib-browse-btn-focus-visible.png) ![Browse libraries button pressed](components/crops/lib-browse-btn-pressed.png)

#### Library overflow
The "…" overflow menu button at the library head (Reset library, import); measured never pressed. Read as `lib-overflow` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; padding 10px; border 1px solid #f1f0ff; radius 8px; background #f6f6f9; text Assistant 13.33/normal 400, #1b1b1f; icon 14 x 16, #1b1b1f |
| hover | background #f1f0ff |
| focus-visible | background #f1f0ff; shadow #5753d0 0px 0px 0px 1px |
| pressed | border 1px solid #4440bf; background #f1f0ff; shadow #6965db 0px 0px 0px 1px |

![Library overflow default](components/crops/lib-overflow-default.png) ![Library overflow hover](components/crops/lib-overflow-hover.png) ![Library overflow focus-visible](components/crops/lib-overflow-focus-visible.png) ![Library overflow pressed](components/crops/lib-overflow-pressed.png)

### Dialogs

The modal layer: the Export-image dialog (toggles, scale radios, PNG/SVG/Copy actions measured never pressed), the keyboard-shortcuts Help sheet and the command palette.

#### Export dialog
The "Export image" modal: checkerboard preview, Background/Dark-mode/Embed switches, the 1×/2×/3× scale radio and PNG/SVG/copy actions — none pressed. Read as `export-dialog` on the editor page.

**Values (default).** size 919.8 x 396; padding 40px; background #ffffff; text Assistant 21.00/27.31 700, #1b1b1f; icon 18 x 18, #1b1b1f.

![Export dialog default](components/crops/export-dialog-default.png)

#### Export preview
The checkerboard transparency preview pane inside the export dialog. Read as `export-preview` on the editor page.

**Values (default).** size 518.09 x 360; background transparent; text Assistant 16/normal 400, #1b1b1f; layers div.ImageExportModal__preview__canvas 518.1x360.0 T:1px solid rgb(214, 214, 214) / R:1px solid rgb(214, 214, 214) / B:1px solid rgb(214, 214, 214) / L:1px solid rgb(214, 214, 214) 12px.

Child layers that carry the look: div 518.1x360 image url(data:…) border 1px solid #d6d6d6 `color.gray.30` radius 12px.

![Export preview default](components/crops/export-preview-default.png)

#### Export switch
A labelled toggle in the dialog (Background/Dark mode/Embed scene); measured never flipped. Read as `export-switch` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 20; border 1px solid #6965db; radius 12px; background #6965db; text Assistant 16/normal 400, #1b1b1f; transition background 0.15s ease-out, border 0.15s ease-out; layers ::before rgb(255, 255, 255) 0px none 1 |
| hover | border 1px solid #5b57d1; background #5b57d1 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Export switch default](components/crops/export-switch-default.png) ![Export switch hover](components/crops/export-switch-hover.png)

#### Scale radio
The 1×/2×/3× scale segmented control. Read as `export-scale` on the editor page.

**Values (default).** size 108 x 32; padding 3px; border 1px solid #f1f0ff; radius 10px; background #ffffff; text Assistant 12/12 600, #6965db.

![Scale radio default](components/crops/export-scale-default.png)

#### PNG button
The accent "PNG" export action; measured never pressed (no file was produced). Read as `export-png` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 84 x 40; padding 8px 16px; border 1px solid transparent; radius 8px; background #6965db; text Assistant 12/normal 600, #ffffff; icon 20 x 20, #ffffff |
| hover | background #5753d0; transition all 0.15s ease-out |
| focus-visible | background #5753d0; shadow #5753d0 0px 0px 0px 1px; transition all 0.15s ease-out |

![PNG button default](components/crops/export-png-default.png) ![PNG button hover](components/crops/export-png-hover.png) ![PNG button focus-visible](components/crops/export-png-focus-visible.png)

#### SVG button
The "SVG" export action beside PNG; measured never pressed. Read as `export-svg` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 81 x 40; padding 8px 16px; border 1px solid transparent; radius 8px; background #6965db; text Assistant 12/normal 600, #ffffff; icon 20 x 20, #ffffff |
| hover | background #5753d0; transition all 0.15s ease-out |
| focus-visible | background #5753d0; shadow #5753d0 0px 0px 0px 1px; transition all 0.15s ease-out |

![SVG button default](components/crops/export-svg-default.png) ![SVG button hover](components/crops/export-svg-hover.png) ![SVG button focus-visible](components/crops/export-svg-focus-visible.png)

#### Shortcuts dialog
The keyboard-shortcuts sheet opened by ? — a column of actions and their keycaps. Read as `shortcuts-dialog` on the editor page.

**Values (default).** size 945.11 x 807.28; border 1px solid #ebebeb `color.gray.20`; radius 12px; background #ffffff; shadow rgba(0, 0, 0, 0.07) 0px 100px 80px 0px, rgba(0, 0, 0, 0.05) 0px 41.7776px 33.4221px 0px, rgba(0, 0, 0, 0.043) 0px 22.3363px 17.869px 0px, rgba(0, 0, 0, 0.035) 0px 12.5216px 10.0172px 0px, rgba(0, 0, 0, 0.027) 0px 6.6501px 5.32008px 0px, rgba(0, 0, 0, 0.02) 0px 2.76726px 2.21381px 0px; text Assistant 20/normal 700, #1b1b1f; transform scale(0.98449); opacity 0.844903; icon 15.75 x 15.75, #1b1b1f.

![Shortcuts dialog default](components/crops/shortcuts-dialog-default.png)

#### Shortcut row
A row in the shortcuts sheet (action name + keycap). Read as `shortcut-row` on the editor page.

**Values (default).** size 427 x 1093; border 1px solid #ebebeb `color.gray.20`; radius 8px; background transparent; text Assistant 14/normal 400, #1b1b1f.

![Shortcut row default](components/crops/shortcut-row-default.png)

#### Keycap
A rendered key chip (e.g. "Ctrl") inside the shortcuts sheet. Read as `keycap` on the editor page.

**Values (default).** size 22 x 26; background transparent; text Assistant 10/10 400, #1b1b1f; layers kbd.HelpDialog__key 22.0x26.0 rgb(227, 226, 254) 6px.

Child layers that carry the look: kbd 22x26 background #e3e2fe radius 6px.

![Keycap default](components/crops/keycap-default.png)

#### Command palette
The Ctrl+/ launcher: a search field over grouped commands (App / Editor); nothing was invoked. Read as `cmdk-dialog` on the editor page.

**Values (default).** size 718 x 748; padding 24px; background #ffffff; text Assistant 10/normal 400, #1b1b1f; icon 16 x 16, #000000.

![Command palette default](components/crops/cmdk-dialog-default.png)

#### Palette input
The search field at the palette head. Read as `cmdk-input` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 644 x 24; background transparent; text Assistant 16/24 400, #1b1b1f; placeholder #757575 |

![Palette input default](components/crops/cmdk-input-default.png) ![Palette input focus-visible](components/crops/cmdk-input-focus-visible.png)

#### Palette item
A command row inside the palette (with its shortcut hint); measured, never invoked. Read as `cmdk-item` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 666 x 40; padding 0px 8px; radius 8px; background #f6f6f9; text Assistant 16/normal 400, #000000; icon 16 x 16, #000000 |

![Palette item default](components/crops/cmdk-item-default.png) ![Palette item hover](components/crops/cmdk-item-hover.png)

#### Copy-to-clipboard button
The "Copy to clipboard" ExcButton in the export dialog (a filled primary variant); measured never pressed. Read as `export-copy` on the editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 154 x 40; padding 8px 16px; border 1px solid transparent; radius 8px; background #6965db; text Assistant 12/normal 600, #ffffff; icon 20 x 20, #ffffff |
| hover | background #5753d0; transition all 0.15s ease-out |
| focus-visible | background #5753d0; shadow #5753d0 0px 0px 0px 1px; transition all 0.15s ease-out |
| pressed | background #4440bf; shadow #5753d0 0px 0px 0px 1px; transition all 0.15s ease-out |

![Copy-to-clipboard button default](components/crops/export-copy-default.png) ![Copy-to-clipboard button hover](components/crops/export-copy-hover.png) ![Copy-to-clipboard button focus-visible](components/crops/export-copy-focus-visible.png) ![Copy-to-clipboard button pressed](components/crops/export-copy-pressed.png)

### Dark theme

The same chrome under `.theme--dark`: the tool island, a tool button, the main menu and the properties panel, measured in dark for the dark token set.

#### Tool island (dark)
The same toolbar Island in dark theme — near-black surface, light icons. Read as `d-island` on the editor (dark) page.

**Values (default).** size 542 x 44; padding 4px; radius 8px; background #232329; shadow rgba(0, 0, 0, 0.17) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 3px 0px, rgba(0, 0, 0, 0.05) 0px 7px 14px 0px; text Assistant 10/normal 400, #7a7a7a `color.gray.60`; icon 16 x 16, #e3e3e8.

![Tool island (dark) default](components/crops/d-island-default.png)

#### Tool button (dark)
A tool button in dark theme. Read as `d-tool` on the editor (dark) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 36 x 36; radius 8px; background transparent; text Assistant 10/normal 400, #7a7a7a `color.gray.60`; icon 16 x 16, #e3e3e8 |
| hover | layers div.ToolIcon__icon 36.0x36.0 rgb(46, 45, 57) 8px |
| focus-visible | shadow #228be6 0px 0px 0px 2px; layers button.ToolIcon.ToolIcon_type_toggle 36.0x36.0 rgb(34, 139, 230) 0px 0px 0px 2px 8px |

![Tool button (dark) default](components/crops/d-tool-default.png) ![Tool button (dark) hover](components/crops/d-tool-hover.png) ![Tool button (dark) focus-visible](components/crops/d-tool-focus-visible.png) ![Tool button (dark) pressed](components/crops/d-tool-pressed.png)

#### Main menu (dark)
The hamburger dropdown in dark theme. Read as `d-menu-panel` on the editor (dark) page.

**Values (default).** size 225 x 648; background transparent; text Assistant 14/normal 400, #e3e3e8; icon 16 x 16, #e3e3e8; layers div.Island.dropdown-menu-container 225.0x648.0 rgb(35, 35, 41) rgba(0, 0, 0, 0.17) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 3px 0px, rgba(0, 0, 0, 0.05) 0px 7px 14px 0px, rgba(0, 0, 0, 0.15) 0px 0px 0px 1px 8px; div 209.0x1.0 rgb(46, 45, 57); div 209.0x1.0 rgb(46, 45, 57); div.RadioGroup 108.0x32.0 rgb(35, 35, 41) T:1px solid rgb(46, 45, 57) / R:1px solid rgb(46, 45, 57) / B:1px solid rgb(46, .

Child layers that carry the look: div 225x648 background #232329 radius 8px shadow rgba(0, 0, 0, 0.17) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 3px 0px, rgba(0, 0, 0, 0.05) 0px 7px 14px 0px, rgba(0, 0, 0, 0.15) 0px 0px 0px 1px; div 209x1 background #2e2d39; div 209x1 background #2e2d39.

![Main menu (dark) default](components/crops/d-menu-panel-default.png)

#### Menu item (dark)
A menu row in dark theme. Read as `d-menu-item` on the editor (dark) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 119 x 18; background transparent; text Assistant 14/normal 400, #e3e3e8 |

![Menu item (dark) default](components/crops/d-menu-item-default.png) ![Menu item (dark) hover](components/crops/d-menu-item-hover.png)

#### Properties panel (dark)
The properties sidebar in dark theme. Read as `d-props` on the editor (dark) page.

**Values (default).** size 195 x 543; padding 12px; radius 8px; background #232329; shadow rgba(0, 0, 0, 0.17) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 3px 0px, rgba(0, 0, 0, 0.05) 0px 7px 14px 0px; text Assistant 12/normal 400, #e3e3e8; icon 16 x 16, #e3e3e8.

![Properties panel (dark) default](components/crops/d-props-default.png)

### Mobile (390 wide)

The phone surface at 390 wide: the welcome sheet, the bottom tool bar and the compact shape-actions row a shape tool swaps in.

#### Welcome screen (mobile)
The first-run overlay at 390 wide: logo, note and menu fill the sheet. Read as `m-welcome` on the mobile editor page at 390 wide.

**Values (default).** size 358 x 780; background transparent; text Excalifont 18/21.6 400, #b8b8b8 `color.gray.40`; icon 40 x 40, #6965db; layers button.welcome-screen-menu-item 300.0x42.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 6px; button.welcome-screen-menu-item 300.0x42.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 6px; button.welcome-screen-menu-item 300.0x42.0 T:1px solid rgba(.

Child layers that carry the look: button 300x42 border 1px solid transparent radius 6px; button 300x42 border 1px solid transparent radius 6px; button 300x42 border 1px solid transparent radius 6px.

![Welcome screen (mobile) default](components/crops/m-welcome-default.png)

#### Welcome item (mobile)
A welcome menu row on the phone layout. Read as `m-welcome-item` on the mobile editor page at 390 wide.

**Values (default).** size 300 x 42; padding 12px; border 1px solid transparent; radius 6px; background transparent; text Arial 14/normal 400, #999999 `color.gray.50`; icon 16 x 16, #999999 `color.gray.50`.

![Welcome item (mobile) default](components/crops/m-welcome-item-default.png)

#### Mobile toolbar
The bottom tool bar at 390 wide: a single row of tools plus the overflow trigger. Read as `m-toolbar` on the mobile editor page at 390 wide.

**Values (default).** size 362 x 44; padding 4px; radius 8px; background #ffffff; shadow rgba(0, 0, 0, 0.17) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 3px 0px, rgba(0, 0, 0, 0.05) 0px 7px 14px 0px; text Assistant 16/normal 400, #1b1b1f; icon 16 x 16, #1b1b1f.

![Mobile toolbar default](components/crops/m-toolbar-default.png)

#### Tool button (mobile)
A tool button in the phone toolbar. Read as `m-tool` on the mobile editor page at 390 wide.

**Values (default).** size 36 x 36; radius 4px; background transparent; text Assistant 16/normal 400, #1b1b1f; icon 16 x 16, #030064; layers div.ToolIcon__icon 36.0x36.0 rgb(224, 223, 255) 8px.

Child layers that carry the look: div 36x36 background #e0dfff radius 8px.

![Tool button (mobile) default](components/crops/m-tool-default.png)

#### Extra tools (mobile)
The overflow trigger at the phone toolbar tail. Read as `m-extra-trigger` on the mobile editor page at 390 wide.

**Values (default).** size 36 x 36; radius 8px; background transparent; text Assistant 13.33/normal 400, #1b1b1f; icon 16 x 16, #1b1b1f.

![Extra tools (mobile) default](components/crops/m-extra-trigger-default.png)

#### Hamburger (mobile)
The floating menu button top-left. Read as `m-menu-trigger` on the mobile editor page at 390 wide.

**Values (default).** size 32 x 32; radius 8px; background #ececf4; shadow #ffffff 0px 0px 0px 1px; text Assistant 13.33/normal 400, #1b1b1f; icon 16 x 16, #1b1b1f.

![Hamburger (mobile) default](components/crops/m-menu-trigger-default.png)

#### Library trigger (mobile)
The floating library button top-right. Read as `m-lib-trigger` on the mobile editor page at 390 wide.

**Values (default).** size 32 x 32; background transparent; text Assistant 16/normal 400, #1b1b1f; icon 16 x 16, #1b1b1f; layers div.sidebar-trigger.default-sidebar-trigger 32.0x32.0 rgb(236, 236, 244) rgb(255, 255, 255) 0px 0px 0px 1px 8px.

Child layers that carry the look: div 32x32 background #ececf4 radius 8px shadow #ffffff 0px 0px 0px 1px.

![Library trigger (mobile) default](components/crops/m-lib-trigger-default.png)

#### Shape actions (mobile)
The compact-shape-actions bar that appears above the toolbar when a shape tool is picked on the phone. Read as `m-shape-actions` on the mobile editor page at 390 wide.

**Values (default).** size 362 x 43.19; radius 8px; background transparent; text Assistant 16/normal 400, #1b1b1f; icon 30 x 30, #ffffff; layers button.color-picker__button.active-color 32.0x32.0 rgb(30, 30, 30) T:1px solid rgb(241, 240, 255) / R:1px solid rgb(241, 240, 255) / B:1px solid rgb(241, 240, 255) / L:1px solid rgb(241, 240, 255) 5px; button.color-picker__button.active-color 32.0x32.0 T:1px solid rgb(241, 240, 255) / R:1px solid rgb(241, 240, 255) / B:1px solid rgb(241, 240, 255) / L:1px solid rgb(241, 240, 255) rgb(235, 235, 235.

Child layers that carry the look: button 32x32 background #1e1e1e `color.gray.90` border 1px solid #f1f0ff radius 5px; button 32x32 image url(data:…) border 1px solid #f1f0ff radius 5px shadow #ebebeb `color.gray.20` 0px 0px 0px 1px; button 32x32 background rgba(255, 255, 255, 0.35) radius 8px.

![Shape actions (mobile) default](components/crops/m-shape-actions-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Excalifont wordmark, the tool glyphs, the menu and dialog iconography) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Excalidraw is fully usable signed out — the whole captured surface works without an account. What an account adds (Excalidraw+: saved workspaces, the library synced to the cloud, collaboration management, billing) was never reached: no Sign up, log-in or 'Try Excalidraw+' path was followed.

### Pages

- **One surface.** excalidraw.com serves only the editor; there is no marketing site, docs or blog on the domain to capture. Every measured view lives on `/`.
- **Collaboration and sharing.** Live collaboration and Share open a session and send the scene over the network — never started; the session UI is uncaptured.
- **File actions.** Open, Save to…, Save to disk and Export (PNG/SVG/Copy) write files or the clipboard — never pressed; only the Export dialog's frame and controls are measured.
- **AI generators and installs.** Text to diagram, Mermaid to Excalidraw, Wireframe to code and 'Browse libraries' call external services — never invoked.
- **The canvas.** Nothing was drawn and no scene was loaded, so element rendering, selection chrome, context menus and the wysiwyg text editor are uncaptured — only the empty-canvas chrome.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the empty-canvas surface (e.g. the disabled export scale states).
- **The library was empty** — its item list, per-item actions and the browse-libraries listing were never reached.

### Themes

Excalidraw ships a real user theme toggle — the Theme radio in the main menu flips `.theme--dark` on the app root and persists to localStorage. The stylesheet overrides ~80 of its ~191 custom properties under that class, so tokens.json keeps real light and dark sets.

### Fonts

- **Assistant** (all UI text), **Excalifont** (the hand-drawn logo and default canvas handwriting) and **Cascadia** (canvas code text) are the served faces, hosted on Excalidraw's DigitalOcean CDN; the style guide falls back to system sans.

### Screenshots

- The Excalifont wordmark and the hand-drawn hint annotations in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- No drawings, library items or user content exist in the capture — only the empty-canvas chrome was measured.
