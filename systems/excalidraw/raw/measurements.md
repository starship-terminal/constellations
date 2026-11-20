# Excalidraw component measurements

Computed styles read from excalidraw.com on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the public editor's surfaces — the welcome screen, the toolbar Islands, the main menu and its dropdowns, the properties sidebar, the library panel, the export/shortcuts/command-palette dialogs, the dark theme and the mobile layout — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Welcome screen (first run)

#### welcome-panel

Welcome screen. The first-run overlay centred on the blank canvas: the excalifont logo, a storage note and a vertical menu.

Page: welcome. Selector: `.welcome-screen-center`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1408 x 868 |
| Padding | 0px |
| Gap | 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Text node | div.welcome-screen-center__heading.welcome-screen-decor: Excalifont 18px/21.6px 400, #b8b8b8 |
| Transition | none |
| Icon | 40 x 40, colour #6965db |
| Painted layers | button.welcome-screen-menu-item 300.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px; button.welcome-screen-menu-item 300.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px; button.welcome-screen-menu-item 300.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px; a.welcome-screen-menu-item 300.0x44.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px |
| How | at rest |

Crops: `welcome-panel-default.png`.

#### welcome-logo

Welcome logo. The hand-drawn "Excalidraw" wordmark in Excalifont.

Page: welcome. Selector: `.welcome-screen-center__logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 281.08 x 40 |
| Padding | 0px |
| Gap | normal 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Excalifont 36px/normal 400 |
| Letter spacing | normal |
| Colour | #b8b8b8 |
| Transition | none |
| Icon | 40 x 40, colour #6965db |
| How | at rest |

Crops: `welcome-logo-default.png`.

#### welcome-heading

Welcome heading. "Your drawings are saved in your browser's storage." — the privacy note under the logo.

Page: welcome. Selector: `welcome heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 453 x 64.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Excalifont 18px/21.6px 400 |
| Letter spacing | normal |
| Colour | #b8b8b8 |
| Transition | none |
| How | at rest |

Crops: `welcome-heading-default.png`.

#### welcome-menu

Welcome menu. The stacked menu inside the welcome card (Open, Help, Live collaboration…, Sign up).

Page: welcome. Selector: `welcome menu column`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1408 x 868 |
| Padding | 0px |
| Gap | 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Text node | div.welcome-screen-center__heading.welcome-screen-decor: Excalifont 18px/21.6px 400, #b8b8b8 |
| Transition | none |
| Icon | 40 x 40, colour #6965db |
| Painted layers | button.welcome-screen-menu-item 300.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px; button.welcome-screen-menu-item 300.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px; button.welcome-screen-menu-item 300.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px; a.welcome-screen-menu-item 300.0x44.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px |
| How | at rest |

Crops: `welcome-menu-default.png`.

#### welcome-item

Welcome menu item. The "Help" welcome item — a plain row with an icon; measured, its action never used.

Page: welcome. Selector: `welcome item Help`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 300 x 42 | = | = | = |
| Padding | 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | 1px solid #4440bf |
| Radius | 6px | = | = | = |
| Background | transparent | #f1f0ff | = | #f1f0ff |
| Box shadow | none | = | #5753d0 0px 0px 0px 1px | = |
| Outline | none | = | = | = |
| Font | Arial 14px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #999999 | = | = | = |
| Text node | div.welcome-screen-menu-item__text: Arial 14px/normal 400, #999999 | div.welcome-screen-menu-item__text: Arial 14px/normal 400, #121212 | = | div.welcome-screen-menu-item__text: Arial 14px/normal 400, #121212 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #999999 | 16 x 16, colour #121212 | = | 16 x 16, colour #121212 |
| Painted layers | button.welcome-screen-menu-item 300.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px | button.welcome-screen-menu-item 300.0x42.0 bg #f1f0ff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px | button.welcome-screen-menu-item 300.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px shadow #5753d0 0px 0px 0px 1px | button.welcome-screen-menu-item 300.0x42.0 bg #f1f0ff border T:1px solid #4440bf / R:1px solid #4440bf / B:1px solid #4440bf / L:1px solid #4440bf r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `welcome-item-default.png`, `welcome-item-hover.png`, `welcome-item-focus-visible.png`, `welcome-item-pressed.png`.

#### welcome-item-signup

Welcome Sign-up item. The "Sign up" welcome item — links to Excalidraw+ signup; measured never followed.

Page: welcome. Selector: `welcome item Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 300 x 44 | = | = | = |
| Padding | 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | 1px solid #4440bf |
| Radius | 6px | = | = | = |
| Background | transparent | #f1f0ff | = | #f1f0ff |
| Box shadow | none | = | #5753d0 0px 0px 0px 1px | = |
| Outline | none | = | = | = |
| Font | Assistant 14px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #999999 | = | = | = |
| Text node | div.welcome-screen-menu-item__text: Assistant 14px/normal 500, #999999 | div.welcome-screen-menu-item__text: Assistant 14px/normal 500, #121212 | = | div.welcome-screen-menu-item__text: Assistant 14px/normal 500, #121212 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #999999 | 16 x 16, colour #121212 | = | 16 x 16, colour #121212 |
| Painted layers | a.welcome-screen-menu-item 300.0x44.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px | a.welcome-screen-menu-item 300.0x44.0 bg #f1f0ff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px | a.welcome-screen-menu-item 300.0x44.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px shadow #5753d0 0px 0px 0px 1px | a.welcome-screen-menu-item 300.0x44.0 bg #f1f0ff border T:1px solid #4440bf / R:1px solid #4440bf / B:1px solid #4440bf / L:1px solid #4440bf r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `welcome-item-signup-default.png`, `welcome-item-signup-hover.png`, `welcome-item-signup-focus-visible.png`, `welcome-item-signup-pressed.png`.

### Toolbar Islands

#### tool-island

Tool island. The floating toolbar Island: a rounded shadowed card holding the tool buttons in a row.

Page: editor. Selector: `.Island.App-toolbar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 542 x 44 |
| Padding | 4px |
| Border | none |
| Radius | 8px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Text node | span.ToolIcon__keybinding: Assistant 10px/normal 400, #b8b8b8 |
| Transition | none |
| Cursor | default |
| Icon | 16 x 16, colour #1b1b1f |
| Painted layers | div.Island.App-toolbar 542.0x44.0 bg #ffffff r 8px shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px; div.App-toolbar__divider 1.0x24.0 bg #f1f0ff; div.App-toolbar__divider 1.0x24.0 bg #f1f0ff; button.dropdown-menu-button.App-toolbar__extra-tools-trigger 36.0x36.0 bg #e0dfff r 8px |
| How | at rest |

Crops: `tool-island-default.png`.

#### menu-trigger

Hamburger trigger. The main-menu icon button at the toolbar head.

Page: editor. Selector: `button.main-menu-trigger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ececf4 | #f1f0ff | = | #f1f0ff |
| Box shadow | #ffffff 0px 0px 0px 1px | = | #5753d0 0px 0px 0px 1px | #4440bf 0px 0px 0px 1px |
| Outline | none | = | = | = |
| Font | Assistant 13.3328px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1f | = | = | = |
| Transition | opacity, visibility 0.25s, 0.25s ease-in-out, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #1b1b1f | = | = | = |
| Painted layers | button.dropdown-menu-button.main-menu-trigger 36.0x36.0 bg #ececf4 r 8px shadow #ffffff 0px 0px 0px 1px | button.dropdown-menu-button.main-menu-trigger 36.0x36.0 bg #f1f0ff r 8px shadow #ffffff 0px 0px 0px 1px | button.dropdown-menu-button.main-menu-trigger 36.0x36.0 bg #ececf4 r 8px shadow #5753d0 0px 0px 0px 1px | button.dropdown-menu-button.main-menu-trigger 36.0x36.0 bg #f1f0ff r 8px shadow #4440bf 0px 0px 0px 1px |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `menu-trigger-default.png`, `menu-trigger-hover.png`, `menu-trigger-focus-visible.png`, `menu-trigger-pressed.png`.

#### tool-lock

Tool lock. The "Keep selected tool active" lock checkbox at the toolbar head.

Page: editor. Selector: `toolbar lock toggle`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | #a5d8ff 0px 0px 0px 2px |
| Outline | none | = | = |
| Font | Assistant 16px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1b1b1f | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #1b1b1f | = | = |
| Ancestor paint | 2 up div.Island.App-toolbar bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | div.ToolIcon__icon 36.0x36.0 bg #f1f0ff r 8px | button.ToolIcon.ToolIcon_type_toggle 36.0x36.0 r 8px shadow #a5d8ff 0px 0px 0px 2px |

Crops: `tool-lock-default.png`, `tool-lock-hover.png`, `tool-lock-focus-visible.png`.

#### tool-selection

Selection tool. The Selection tool button — the active tool after entering the editor, so its selected state is the resting one.

Page: editor. Selector: `button[aria-label="Selection"]`. States: default, hover, focus-visible, pressed, selected.

| Property | default | hover | focus-visible | pressed | selected |
|---|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 8px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | #a5d8ff 0px 0px 0px 2px | = | = |
| Outline | none | = | = | = | = |
| Font | Assistant 16px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #1b1b1f | = | = | = | = |
| Text node | span.ToolIcon__keybinding: Assistant 10px/normal 400, #b8b8b8 | = | = | = | span.ToolIcon__keybinding: Assistant 10px/normal 400, #030064 |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 16 x 16, colour #1b1b1f | = | = | = | 16 x 16, colour #030064 |
| Ancestor paint | 2 up div.Island.App-toolbar bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | clicked the tool once (a local selection) |
| Painted layers | - | div.ToolIcon__icon 36.0x36.0 bg #f1f0ff r 8px | button.ToolIcon.ToolIcon_type_toggle 36.0x36.0 r 8px shadow #a5d8ff 0px 0px 0px 2px | = | div.ToolIcon__icon 36.0x36.0 bg #e0dfff r 8px |

Crops: `tool-selection-default.png`, `tool-selection-hover.png`, `tool-selection-focus-visible.png`, `tool-selection-pressed.png`, `tool-selection-selected.png`.

#### tool-rect

Rectangle tool. A shape tool button; selecting it also summons the properties sidebar (a local selection, nothing drawn).

Page: editor. Selector: `button[aria-label=Rectangle]`. States: default, hover, focus-visible, pressed, selected.

| Property | default | hover | focus-visible | pressed | selected |
|---|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 8px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | #a5d8ff 0px 0px 0px 2px | = | = |
| Outline | none | = | = | = | = |
| Font | Assistant 16px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #1b1b1f | = | = | = | = |
| Text node | span.ToolIcon__keybinding: Assistant 10px/normal 400, #b8b8b8 | = | = | = | span.ToolIcon__keybinding: Assistant 10px/normal 400, #030064 |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 16 x 16, colour #1b1b1f | = | = | = | 16 x 16, colour #030064 |
| Ancestor paint | 2 up div.Island.App-toolbar bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | clicked the tool once (a local selection) |
| Painted layers | - | div.ToolIcon__icon 36.0x36.0 bg #f1f0ff r 8px | button.ToolIcon.ToolIcon_type_toggle 36.0x36.0 r 8px shadow #a5d8ff 0px 0px 0px 2px | = | div.ToolIcon__icon 36.0x36.0 bg #e0dfff r 8px |

Crops: `tool-rect-default.png`, `tool-rect-hover.png`, `tool-rect-focus-visible.png`, `tool-rect-pressed.png`, `tool-rect-selected.png`.

#### tool-draw

Draw tool. The freedraw pen tool button.

Page: editor. Selector: `button[aria-label=Draw]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #a5d8ff 0px 0px 0px 2px | = |
| Outline | none | = | = | = |
| Font | Assistant 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1f | = | = | = |
| Text node | span.ToolIcon__keybinding: Assistant 10px/normal 400, #b8b8b8 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #1b1b1f | = | = | = |
| Ancestor paint | 2 up div.Island.App-toolbar bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | div.ToolIcon__icon 36.0x36.0 bg #f1f0ff r 8px | button.ToolIcon.ToolIcon_type_toggle 36.0x36.0 r 8px shadow #a5d8ff 0px 0px 0px 2px | = |

Crops: `tool-draw-default.png`, `tool-draw-hover.png`, `tool-draw-focus-visible.png`, `tool-draw-pressed.png`.

#### tool-text

Text tool. The text tool button.

Page: editor. Selector: `button[aria-label=Text]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #a5d8ff 0px 0px 0px 2px | = |
| Outline | none | = | = | = |
| Font | Assistant 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1f | = | = | = |
| Text node | span.ToolIcon__keybinding: Assistant 10px/normal 400, #b8b8b8 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #1b1b1f | = | = | = |
| Ancestor paint | 2 up div.Island.App-toolbar bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | div.ToolIcon__icon 36.0x36.0 bg #f1f0ff r 8px | button.ToolIcon.ToolIcon_type_toggle 36.0x36.0 r 8px shadow #a5d8ff 0px 0px 0px 2px | = |

Crops: `tool-text-default.png`, `tool-text-hover.png`, `tool-text-focus-visible.png`, `tool-text-pressed.png`.

#### tool-eraser

Eraser tool. The eraser tool button.

Page: editor. Selector: `button[aria-label=Eraser]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #a5d8ff 0px 0px 0px 2px | = |
| Outline | none | = | = | = |
| Font | Assistant 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1f | = | = | = |
| Text node | span.ToolIcon__keybinding: Assistant 10px/normal 400, #b8b8b8 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #1b1b1f | = | = | = |
| Ancestor paint | 2 up div.Island.App-toolbar bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | div.ToolIcon__icon 36.0x36.0 bg #f1f0ff r 8px | button.ToolIcon.ToolIcon_type_toggle 36.0x36.0 r 8px shadow #a5d8ff 0px 0px 0px 2px | = |

Crops: `tool-eraser-default.png`, `tool-eraser-hover.png`, `tool-eraser-focus-visible.png`, `tool-eraser-pressed.png`.

#### tool-more

Extra tools trigger. The "Extra tools" overflow button at the toolbar tail — a local dropdown toggle.

Page: editor. Selector: `button.App-toolbar__extra-tools-trigger`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = | = |
| Padding | 10px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 8px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | #5753d0 0px 0px 0px 1px | #4440bf 0px 0px 0px 1px inset | = |
| Outline | none | = | = | = | = |
| Font | Assistant 13.3328px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #1b1b1f | = | = | = | = |
| Transition | opacity, visibility 0.25s, 0.25s ease-in-out, ease delay 0s, 0s | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 16 x 16, colour #1b1b1f | = | = | = | = |
| Ancestor paint | 3 up div.Island.App-toolbar bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | button.dropdown-menu-button.App-toolbar__extra-tools-trigger 36.0x36.0 r 8px shadow #5753d0 0px 0px 0px 1px | button.dropdown-menu-button.App-toolbar__extra-tools-trigger 36.0x36.0 r 8px shadow #4440bf 0px 0px 0px 1px inset | = |

Crops: `tool-more-default.png`, `tool-more-hover.png`, `tool-more-focus-visible.png`, `tool-more-pressed.png`, `tool-more-opened.png`.

#### lib-trigger

Library trigger. The "Library" sidebar button top-right — a local panel toggle.

Page: editor. Selector: `button.sidebar-trigger__label-element`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | #5753d0 0px 0px 0px 1px | = | = |
| Outline | none | = | = | = | = |
| Font | Assistant 16px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #1b1b1f | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 16 x 16, colour #1b1b1f | = | = | = | = |
| Painted layers | div.sidebar-trigger.default-sidebar-trigger 36.0x36.0 bg #ececf4 r 8px shadow #ffffff 0px 0px 0px 1px | div.sidebar-trigger.default-sidebar-trigger 36.0x36.0 bg #f1f0ff r 8px shadow #ffffff 0px 0px 0px 1px | button.sidebar-trigger__label-element 36.0x36.0 shadow #5753d0 0px 0px 0px 1px; div.sidebar-trigger.default-sidebar-trigger 36.0x36.0 bg #ececf4 r 8px shadow #ffffff 0px 0px 0px 1px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `lib-trigger-default.png`, `lib-trigger-hover.png`, `lib-trigger-focus-visible.png`, `lib-trigger-pressed.png`, `lib-trigger-opened.png`.

### Main menu and dropdowns

#### extra-menu

Extra tools menu. The extra-tools dropdown (Insert image, Frame, Web Embed, Draw to shape, Laser, plus the AI entries); its items were measured never pressed.

Page: editor. Selector: `extra tools dropdown`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 197 x 376 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Text node | span: Assistant 14px/normal 400, #1b1b1f |
| Transition | none |
| Cursor | default |
| Icon | 16 x 16, colour #1b1b1f |
| Painted layers | div.Island.dropdown-menu-container 197.0x376.0 bg #ffffff r 8px shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px; div.DropDownMenuItemBadge 20.0x16.0 bg #6965db border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 6px; div.DropDownMenuItemBadge 20.0x16.0 bg #6965db border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 6px |
| How | at rest |

Crops: `extra-menu-default.png`.

#### extra-menu-item

Extra menu item. A row inside the extra-tools dropdown (Lasso selection); measured, never pressed.

Page: editor. Selector: `extra menu item`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 181 x 32 | = | = |
| Padding | 0px 8px | = | = |
| Gap | normal 10px | = | = |
| Border | none | = | = |
| Radius | 6px | = | = |
| Background | transparent | #f1f0ff | #f1f0ff |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Assistant 14px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1b1b1f | = | = |
| Text node | span: Assistant 14px/normal 400, #1b1b1f | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #1b1b1f | = | = |
| Ancestor paint | 1 up div.Island.dropdown-menu-container bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | button.radix-menu-item.dropdown-menu-item 181.0x32.0 bg #f1f0ff r 6px | button.radix-menu-item.dropdown-menu-item 181.0x32.0 bg #f1f0ff r 6px |

Crops: `extra-menu-item-default.png`, `extra-menu-item-hover.png`, `extra-menu-item-focus-visible.png`.

#### menu-panel

Main menu. The hamburger dropdown: Open / Save to disk / Export image… / Live collaboration / Command palette / Help, then Preferences, Theme, Language and the canvas-background swatches.

Page: menus. Selector: `.dropdown-menu.main-menu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 225 x 648 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Text node | span: Assistant 14px/normal 400, #1b1b1f |
| Transition | none |
| Cursor | default |
| Icon | 16 x 16, colour #1b1b1f |
| Painted layers | div.Island.dropdown-menu-container 225.0x648.0 bg #ffffff r 8px shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px; div 209.0x1.0 bg #f1f0ff; div 209.0x1.0 bg #f1f0ff; div.RadioGroup 108.0x32.0 bg #ffffff border T:1px solid #f1f0ff / R:1px solid #f1f0ff / B:1px solid #f1f0ff / L:1px solid #f1f0ff r 10px; div.RadioGroup__choice.active 32.0x24.0 bg #6965db r 8px; div.RadioGroup__choice 32.0x24.0 bg #ffffff r 8px |
| How | at rest |

Crops: `menu-panel-default.png`.

#### menu-item

Menu item. The "Open" menu row (icon + label); measured, never pressed.

Page: menus. Selector: `menu item Open`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 209 x 32 | = | = |
| Padding | 0px 8px | = | = |
| Gap | normal 10px | = | = |
| Border | none | = | = |
| Radius | 6px | = | = |
| Background | transparent | #f1f0ff | #f1f0ff |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Assistant 14px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1b1b1f | = | = |
| Text node | span: Assistant 14px/normal 400, #1b1b1f | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #1b1b1f | = | = |
| Ancestor paint | 1 up div.Island.dropdown-menu-container bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | button.radix-menu-item.dropdown-menu-item 209.0x32.0 bg #f1f0ff r 6px | button.radix-menu-item.dropdown-menu-item 209.0x32.0 bg #f1f0ff r 6px |

Crops: `menu-item-default.png`, `menu-item-hover.png`, `menu-item-focus-visible.png`.

#### menu-item-collab

Collaboration item. "Live collaboration…" — would start a session; measured never pressed.

Page: menus. Selector: `menu item Live collaboration`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 209 x 32 | = | = |
| Padding | 0px 8px | = | = |
| Gap | normal 10px | = | = |
| Border | none | = | = |
| Radius | 6px | = | = |
| Background | transparent | #f1f0ff | #f1f0ff |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Assistant 14px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1b1b1f | = | = |
| Text node | span: Assistant 14px/normal 400, #1b1b1f | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #1b1b1f | = | = |
| Ancestor paint | 1 up div.Island.dropdown-menu-container bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | button.radix-menu-item.dropdown-menu-item 209.0x32.0 bg #f1f0ff r 6px | button.radix-menu-item.dropdown-menu-item 209.0x32.0 bg #f1f0ff r 6px |

Crops: `menu-item-collab-default.png`, `menu-item-collab-hover.png`, `menu-item-collab-focus-visible.png`.

#### menu-sep

Menu separator. The hairline divider between menu groups.

Page: menus. Selector: `menu separator`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 209 x 1 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #f1f0ff |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Transition | none |
| Cursor | default |
| Painted layers | div 209.0x1.0 bg #f1f0ff |
| Ancestor paint | 1 up div.Island.dropdown-menu-container bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px |
| How | at rest |

Crops: `menu-sep-default.png`.

#### theme-radios

Theme radio group. The Light/Dark/System radio row inside the menu — the real theme control (Dark is set for the dark page, never left on).

Page: menus. Selector: `main menu .RadioGroup`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 108 x 32 |
| Padding | 3px |
| Gap | 2px |
| Border | 1px solid #f1f0ff |
| Radius | 10px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Assistant 14px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Transition | none |
| Cursor | default |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | div.RadioGroup 108.0x32.0 bg #ffffff border T:1px solid #f1f0ff / R:1px solid #f1f0ff / B:1px solid #f1f0ff / L:1px solid #f1f0ff r 10px; div.RadioGroup__choice.active 32.0x24.0 bg #6965db r 8px; div.RadioGroup__choice 32.0x24.0 bg #ffffff r 8px; div.RadioGroup__choice 32.0x24.0 bg #ffffff r 8px |
| Ancestor paint | 2 up div.Island.dropdown-menu-container bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px |
| How | at rest |

Crops: `theme-radios-default.png`.

#### theme-choice

Theme radio choice. A choice in the Theme radio group (Dark); measured at rest.

Page: menus. Selector: `.RadioGroup__choice Dark`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 32 x 24 | = | - |
| Padding | 0px 6px | = | - |
| Border | none | = | - |
| Radius | 8px | = | - |
| Background | #ffffff | = | - |
| Box shadow | none | = | - |
| Outline | none | = | - |
| Font | Assistant 12px/12px 600 | = | - |
| Letter spacing | 0.4px | = | - |
| Colour | #6965db | #5753d0 | - |
| Transition | none | = | - |
| Cursor | default | = | - |
| Icon | 16 x 16, colour #6965db | 16 x 16, colour #5753d0 | - |
| Painted layers | div.RadioGroup__choice 32.0x24.0 bg #ffffff r 8px | = | - |
| Ancestor paint | 1 up div.RadioGroup bg #ffffff; 3 up div.Island.dropdown-menu-container bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px | = | - |
| How | at rest | mouse hover | - |
| Skipped | - | = | focus failed: keyboard focus did not reach the element |

Crops: `theme-choice-default.png`, `theme-choice-hover.png`.

#### canvas-swatches

Canvas background picker. The canvas-background colour row at the menu foot — a strip of preset swatches.

Page: menus. Selector: `menu canvas colour picker`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 189 x 34 |
| Padding | 4px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Transition | none |
| Cursor | default |
| Painted layers | button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #ffffff r 4px shadow #ebebeb 0px 0px 0px 1px; div.color-picker__button-outline 24.0x24.0 r 4px shadow #4a47b1 0px 0px 0px 1px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #f8f9fa r 4px shadow #ebebeb 0px 0px 0px 1px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #f5faff r 4px shadow #ebebeb 0px 0px 0px 1px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #fffce8 r 4px shadow #ebebeb 0px 0px 0px 1px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #fdf8f6 r 4px shadow #ebebeb 0px 0px 0px 1px |
| Ancestor paint | 3 up div.Island.dropdown-menu-container bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px |
| How | at rest |

Crops: `canvas-swatches-default.png`.

#### canvas-swatch

Canvas swatch. One preset swatch in the canvas-background picker; measured, never set.

Page: menus. Selector: `canvas swatch`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 22 x 22 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 4px | = | = |
| Background | #ffffff | = | = |
| Box shadow | #ebebeb 0px 0px 0px 1px | = | = |
| Outline | none | = | = |
| Font | Assistant 13.3328px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #ffffff r 4px shadow #ebebeb 0px 0px 0px 1px; div.color-picker__button-outline 24.0x24.0 r 4px shadow #4a47b1 0px 0px 0px 1px | = | button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #ffffff r 4px shadow #ebebeb 0px 0px 0px 1px; button::after.color-picker__button.top-picks-dnd__pick 24pxx24px border T:3px solid #a5d8ff / R:3px solid #a5d8ff / B:3px solid #a5d8ff / L:3px solid #a5d8ff r 5px; div.color-picker__button-outline 0.0x0.0 r 4px shadow #4a47b1 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab |
| ::after | - | = | 24px x 24px, absolute, bg #000000 @ 0, radius 5px |

Crops: `canvas-swatch-default.png`, `canvas-swatch-hover.png`, `canvas-swatch-focus-visible.png`.

#### pref-submenu

Preferences submenu. The Preferences submenu (Zen mode, View mode, Grid mode, snapping, stats); toggles measured never set.

Page: menus. Selector: `preferences submenu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 255 x 411 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Text node | span: Assistant 14px/normal 400, #1b1b1f |
| Transition | none |
| Cursor | default |
| Icon | 16 x 16, colour #1b1b1f, fill #000000 |
| Painted layers | div.Island.dropdown-menu-container 255.0x411.0 bg #ffffff r 8px shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px; div.RadioGroup 105.4x32.0 bg #ffffff border T:1px solid #f1f0ff / R:1px solid #f1f0ff / B:1px solid #f1f0ff / L:1px solid #f1f0ff r 10px; div.RadioGroup__choice.active 40.6x24.0 bg #6965db r 8px; div.RadioGroup__choice 54.8x24.0 bg #ffffff r 8px; div.RadioGroup 121.2x32.0 bg #ffffff border T:1px solid #f1f0ff / R:1px solid #f1f0ff / B:1px solid #f1f0ff / L:1px solid #f1f0ff r 10px; div.RadioGroup__choice.active 63.2x24.0 bg #6965db r 8px |
| Ancestor paint | 2 up div.Island.dropdown-menu-container bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px |
| How | at rest |

Crops: `pref-submenu-default.png`.

#### pref-item

Preference item. A togglable submenu row (Zen mode); measured, never set.

Page: menus. Selector: `preferences item Zen mode`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 239 x 32 | = | = |
| Padding | 0px 8px | = | = |
| Gap | normal 10px | = | = |
| Border | none | = | = |
| Radius | 6px | = | = |
| Background | transparent | #f1f0ff | #f1f0ff |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Assistant 14px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1b1b1f | = | = |
| Text node | span: Assistant 14px/normal 400, #1b1b1f | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Ancestor paint | 1 up div.Island.dropdown-menu-container bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | button.radix-menu-item.dropdown-menu-item 239.0x32.0 bg #f1f0ff r 6px | button.radix-menu-item.dropdown-menu-item 239.0x32.0 bg #f1f0ff r 6px |

Crops: `pref-item-default.png`, `pref-item-hover.png`, `pref-item-focus-visible.png`.

### Footer bar

#### undo-btn

Undo button. The Undo footer button — disabled on a blank canvas, which is its resting reading.

Page: editor. Selector: `button[aria-label=Undo]`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 36 x 36 | - |
| Padding | 0px | - |
| Border | none | - |
| Radius | 8px 0px 0px 8px | - |
| Background | transparent | - |
| Box shadow | none | - |
| Outline | none | - |
| Font | Arial 14px/normal 400 | - |
| Letter spacing | normal | - |
| Colour | #101010 @ 0.3 | - |
| Transition | none | - |
| Cursor | default | - |
| Icon | 16 x 16, colour #b8b8b8 | - |
| Ancestor paint | 3 up div.undo-redo-buttons.zen-mode-transition bg #ececf4 shadow #ffffff 0px 0px 0px 1px | - |
| How | at rest | - |
| Skipped | - | focus failed: keyboard focus did not reach the element |

Crops: `undo-btn-default.png`.

#### redo-btn

Redo button. The Redo footer button — disabled at rest like Undo.

Page: editor. Selector: `button[aria-label=Redo]`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 36 x 36 | - |
| Padding | 0px | - |
| Border | none | - |
| Radius | 0px 8px 8px 0px | - |
| Background | transparent | - |
| Box shadow | none | - |
| Outline | none | - |
| Font | Arial 14px/normal 400 | - |
| Letter spacing | normal | - |
| Colour | #101010 @ 0.3 | - |
| Transition | none | - |
| Cursor | default | - |
| Icon | 16 x 16, colour #b8b8b8 | - |
| Ancestor paint | 3 up div.undo-redo-buttons.zen-mode-transition bg #ececf4 shadow #ffffff 0px 0px 0px 1px | - |
| How | at rest | - |
| Skipped | - | focus failed: keyboard focus did not reach the element |

Crops: `redo-btn-default.png`.

#### zoom-btn

Zoom control. The "− 100% +" zoom pill bottom-left; the opened state is its dropdown (Zen/grid/snap toggles), measured never set.

Page: editor. Selector: `.zoom-button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 60 x 36 | = | = | = | = |
| Padding | 0px 10px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 8px 0px 0px 8px | = | = | = | = |
| Background | transparent | #f1f0ff | = | #f1f0ff | #f1f0ff |
| Box shadow | none | = | #5753d0 0px 0px 0px 1px inset | #6965db 0px 0px 0px 1px inset | = |
| Outline | none | = | = | = | = |
| Font | Assistant 14px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #1b1b1f | = | = | = | = |
| Transition | opacity, visibility 0.25s, 0.25s ease-in-out, ease delay 0s, 0s | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Ancestor paint | 2 up div.zoom-actions bg #ececf4 shadow #ffffff 0px 0px 0px 1px | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | button.dropdown-menu-button.zoom-menu-trigger 60.0x36.0 bg #f1f0ff r 8px 0px 0px 8px | button.dropdown-menu-button.zoom-menu-trigger 60.0x36.0 r 8px 0px 0px 8px shadow #5753d0 0px 0px 0px 1px inset | button.dropdown-menu-button.zoom-menu-trigger 60.0x36.0 bg #f1f0ff r 8px 0px 0px 8px shadow #6965db 0px 0px 0px 1px inset | button.dropdown-menu-button.zoom-menu-trigger 60.0x36.0 bg #f1f0ff r 8px 0px 0px 8px |

Crops: `zoom-btn-default.png`, `zoom-btn-hover.png`, `zoom-btn-focus-visible.png`, `zoom-btn-pressed.png`, `zoom-btn-opened.png`.

#### zoom-menu

Zoom menu. The zoom footer dropdown (Zoom in/out, Zen mode, Grid, snapping); opened by its own trigger, toggles never set.

Page: editor. Selector: `zoom dropdown`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 218 x 194 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Text node | span: Assistant 14px/normal 400, #1b1b1f |
| Transition | none |
| Cursor | default |
| Icon | 16 x 16, colour #1b1b1f |
| Painted layers | div.Island.dropdown-menu-container 218.0x194.0 bg #ffffff r 8px shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px; div 202.0x1.0 bg #f1f0ff |
| Ancestor paint | 3 up div.zoom-actions bg #ececf4 shadow #ffffff 0px 0px 0px 1px |
| How | at rest |

Crops: `zoom-menu-default.png`.

#### help-btn

Help button. The "?" help icon button bottom-right.

Page: editor. Selector: `button.help-icon`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ececf4 | #f1f0ff | = | #f1f0ff |
| Box shadow | #ffffff 0px 0px 0px 1px | = | #5753d0 0px 0px 0px 1px | #4440bf 0px 0px 0px 1px |
| Outline | none | = | = | = |
| Font | Assistant 13.3328px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #1b1b1f | = | = | = |
| Painted layers | button.help-icon 36.0x36.0 bg #ececf4 r 8px shadow #ffffff 0px 0px 0px 1px | button.help-icon 36.0x36.0 bg #f1f0ff r 8px shadow #ffffff 0px 0px 0px 1px | button.help-icon 36.0x36.0 bg #ececf4 r 8px shadow #5753d0 0px 0px 0px 1px | button.help-icon 36.0x36.0 bg #f1f0ff r 8px shadow #4440bf 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `help-btn-default.png`, `help-btn-hover.png`, `help-btn-focus-visible.png`, `help-btn-pressed.png`.

#### collab-btn

Share button. The purple "Share"/collaboration button — opens a session dialog, never pressed.

Page: editor. Selector: `Share/collab button`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 55 x 36 | = | = |
| Padding | 10px | = | = |
| Border | 1px solid #6965db | 1px solid #5b57d1 | = |
| Radius | 8px | = | = |
| Background | #6965db | #5b57d1 | = |
| Box shadow | #ffffff 0px 0px 0px 1px | = | #5753d0 0px 0px 0px 1px |
| Outline | none | = | = |
| Font | Assistant 13.3328px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.excalidraw-button.collab-button 55.0x36.0 bg #6965db border T:1px solid #6965db / R:1px solid #6965db / B:1px solid #6965db / L:1px solid #6965db r 8px shadow #ffffff 0px 0px 0px 1px | button.excalidraw-button.collab-button 55.0x36.0 bg #5b57d1 border T:1px solid #5b57d1 / R:1px solid #5b57d1 / B:1px solid #5b57d1 / L:1px solid #5b57d1 r 8px shadow #ffffff 0px 0px 0px 1px | button.excalidraw-button.collab-button 55.0x36.0 bg #6965db border T:1px solid #6965db / R:1px solid #6965db / B:1px solid #6965db / L:1px solid #6965db r 8px shadow #5753d0 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `collab-btn-default.png`, `collab-btn-hover.png`, `collab-btn-focus-visible.png`.

#### plus-btn

Excalidraw+ promo. The Excalidraw+ upsell action; measured never followed.

Page: editor. Selector: `Excalidraw+ promo`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 148 x 36 | = | = |
| Padding | 0px 14px 0px 10px | = | = |
| Gap | 8px | = | = |
| Border | 1px solid #d7d5ff | 1px solid #e3e2fe | = |
| Radius | 8px | = | = |
| Background | #f0efff | #e3e2fe | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | Assistant 16px/normal 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #6965db | = | = |
| Text node | span.plus-banner__title: Assistant 14px/16.1px 600, #6965db | = | = |
| Transition | background-color, border-color 0.15s, 0.15s ease, ease delay 0s, 0s | = | = |
| Cursor | pointer | = | = |
| Icon | 20 x 20, colour #6965db | = | = |
| Painted layers | a.plus-banner 148.0x36.0 bg #f0efff border T:1px solid #d7d5ff / R:1px solid #d7d5ff / B:1px solid #d7d5ff / L:1px solid #d7d5ff r 8px | a.plus-banner 148.0x36.0 bg #e3e2fe border T:1px solid #e3e2fe / R:1px solid #e3e2fe / B:1px solid #e3e2fe / L:1px solid #e3e2fe r 8px | a.plus-banner 148.0x36.0 bg #f0efff border T:1px solid #d7d5ff / R:1px solid #d7d5ff / B:1px solid #d7d5ff / L:1px solid #d7d5ff r 8px outline 1px auto #101010 offset 1px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `plus-btn-default.png`, `plus-btn-hover.png`, `plus-btn-focus-visible.png`.

### Properties sidebar

#### props-panel

Properties panel. The left sidebar summoned by picking a shape tool: Stroke and Background pickers, Stroke width/style, Sloppiness, Edges, Opacity, Layers.

Page: sidebar. Selector: `.App-menu__left`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 195 x 543 |
| Padding | 12px |
| Border | none |
| Radius | 8px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Text node | h3: Assistant 12px/normal 400, #1b1b1f |
| Transition | none |
| Cursor | default |
| Icon | 16 x 16, colour #1b1b1f |
| Painted layers | div.Island.App-menu__left 195.0x543.0 bg #ffffff r 8px shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #1e1e1e r 4px; div.color-picker__button-outline 24.0x24.0 r 4px shadow #4a47b1 0px 0px 0px 1px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #e03131 r 4px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #2f9e44 r 4px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #1971c2 r 4px |
| How | at rest |

Crops: `props-panel-default.png`.

#### prop-label

Property label. A section label ("Stroke") inside the properties panel.

Page: sidebar. Selector: `props label Stroke`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 63 x 15 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 12px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Transition | none |
| Cursor | default |
| Ancestor paint | 3 up div.Island.App-menu__left bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px |
| How | at rest |

Crops: `prop-label-default.png`.

#### stroke-picker

Stroke colour picker. The Stroke top-picks row: five preset swatches plus the custom picker button.

Page: sidebar. Selector: `stroke colour picker`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 171 x 34 |
| Padding | 4px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Transition | none |
| Cursor | default |
| Painted layers | button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #1e1e1e r 4px; div.color-picker__button-outline 24.0x24.0 r 4px shadow #4a47b1 0px 0px 0px 1px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #e03131 r 4px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #2f9e44 r 4px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #1971c2 r 4px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #f08c00 r 4px |
| Ancestor paint | 3 up div.Island.App-menu__left bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px |
| How | at rest |

Crops: `stroke-picker-default.png`.

#### stroke-swatch

Stroke swatch. A preset colour swatch in the Stroke picker — the selected one carries the accent ring.

Page: sidebar. Selector: `stroke swatch`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 22 x 22 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 4px | = | = |
| Background | #1e1e1e | = | = |
| Box shadow | none | = | #5753d0 0px 0px 0px 1px |
| Outline | none | = | = |
| Font | Assistant 13.3328px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #1e1e1e r 4px; div.color-picker__button-outline 24.0x24.0 r 4px shadow #4a47b1 0px 0px 0px 1px | = | button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #1e1e1e r 4px shadow #5753d0 0px 0px 0px 1px; button::after.color-picker__button.top-picks-dnd__pick 24pxx24px border T:3px solid #a5d8ff / R:3px solid #a5d8ff / B:3px solid #a5d8ff / L:3px solid #a5d8ff r 5px; div.color-picker__button-outline 0.0x0.0 r 4px shadow #4a47b1 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab |
| ::after | - | = | 24px x 24px, absolute, bg #000000 @ 0, radius 5px |

Crops: `stroke-swatch-default.png`, `stroke-swatch-hover.png`, `stroke-swatch-focus-visible.png`.

#### stroke-width-group

Stroke width radio. The Stroke-width segmented control (thin/bold/extra-bold icons).

Page: sidebar. Selector: `stroke width RadioGroup`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 171 x 59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Text node | legend: Assistant 12px/normal 400, #1b1b1f |
| Transition | none |
| Cursor | default |
| Icon | 16 x 16, colour #1b1b1f |
| Painted layers | label 32.0x32.0 bg #f6f6f9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; label.active 32.0x32.0 bg #e0dfff border T:1px solid #e0dfff / R:1px solid #e0dfff / B:1px solid #e0dfff / L:1px solid #e0dfff r 8px; label 32.0x32.0 bg #f6f6f9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| Ancestor paint | 2 up div.Island.App-menu__left bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px |
| How | at rest |

Crops: `stroke-width-group-default.png`.

#### stroke-choice

Stroke width choice. A choice inside a properties RadioGroup — the active choice paints the accent background.

Page: sidebar. Selector: `stroke RadioGroup choice`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = |
| Padding | 0px | = | = |
| Border | 1px solid #e0dfff | = | = |
| Radius | 8px | = | = |
| Background | #e0dfff | = | = |
| Box shadow | none | = | #5753d0 0px 0px 0px 1px |
| Outline | none | = | = |
| Font | Assistant 12px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1b1b1f | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #030064 | = | = |
| Painted layers | label.active 32.0x32.0 bg #e0dfff border T:1px solid #e0dfff / R:1px solid #e0dfff / B:1px solid #e0dfff / L:1px solid #e0dfff r 8px | = | label.active 32.0x32.0 bg #e0dfff border T:1px solid #e0dfff / R:1px solid #e0dfff / B:1px solid #e0dfff / L:1px solid #e0dfff r 8px shadow #5753d0 0px 0px 0px 1px; input 13.0x13.0 shadow #5753d0 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `stroke-choice-default.png`, `stroke-choice-hover.png`, `stroke-choice-focus-visible.png`.

#### opacity-row

Opacity control. The Opacity row: a range slider and a numeric input.

Page: sidebar. Selector: `opacity control`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 171 x 58 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 12px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Transition | none |
| Cursor | default |
| Painted layers | input.range-input 171.0x4.0 image linear-gradient(to right, #ccccff calc(100%), #f6f6f9 calc(100%)) r 2px |
| Ancestor paint | 2 up div.Island.App-menu__left bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px |
| How | at rest |

Crops: `opacity-row-default.png`.

#### opacity-slider

Opacity slider. The range input inside the Opacity control.

Page: sidebar. Selector: `opacity input[type=range]`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 171 x 4 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 2px | = |
| Background | transparent | = |
| Background image | linear-gradient(to right, #ccccff calc(100%), #f6f6f9 calc(100%)) | = |
| Box shadow | none | #5753d0 0px 0px 0px 1px |
| Outline | none | = |
| Font | Arial 13.3333px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #9d968e | = |
| Transition | none | = |
| Cursor | default | = |
| Placeholder | #9d968e, opacity 1 | = |
| Painted layers | input.range-input 171.0x4.0 image linear-gradient(to right, #ccccff calc(100%), #f6f6f9 calc(100%)) r 2px | input.range-input 171.0x4.0 image linear-gradient(to right, #ccccff calc(100%), #f6f6f9 calc(100%)) r 2px shadow #5753d0 0px 0px 0px 1px |
| How | at rest | Shift+Tab, Tab |

Crops: `opacity-slider-default.png`, `opacity-slider-focus-visible.png`.

#### layers-row

Layers row. The Layers section: bring-forward/send-backward icon buttons.

Page: sidebar. Selector: `layers section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 171 x 59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Text node | legend: Assistant 12px/normal 400, #1b1b1f |
| Transition | none |
| Cursor | default |
| Icon | 16 x 16, colour #1b1b1f |
| Painted layers | button.zIndexButton 32.0x32.0 bg #f6f6f9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; button.zIndexButton 32.0x32.0 bg #f6f6f9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; button.zIndexButton 32.0x32.0 bg #f6f6f9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; button.zIndexButton 32.0x32.0 bg #f6f6f9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| Ancestor paint | 2 up div.Island.App-menu__left bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px |
| How | at rest |

Crops: `layers-row-default.png`.

#### layer-btn

Layer action. A z-order icon button in the Layers row.

Page: sidebar. Selector: `layer action button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | 1px solid #4440bf |
| Radius | 8px | = | = | = |
| Background | #f6f6f9 | #f1f0ff | = | #f1f0ff |
| Box shadow | none | = | #5753d0 0px 0px 0px 1px | = |
| Outline | none | = | = | = |
| Font | Assistant 13.3328px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #1b1b1f | = | = | = |
| Painted layers | button.zIndexButton 32.0x32.0 bg #f6f6f9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.zIndexButton 32.0x32.0 bg #f1f0ff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.zIndexButton 32.0x32.0 bg #f6f6f9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #5753d0 0px 0px 0px 1px | button.zIndexButton 32.0x32.0 bg #f1f0ff border T:1px solid #4440bf / R:1px solid #4440bf / B:1px solid #4440bf / L:1px solid #4440bf r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `layer-btn-default.png`, `layer-btn-hover.png`, `layer-btn-focus-visible.png`, `layer-btn-pressed.png`.

### Library panel

#### lib-panel

Library panel. The right sidebar holding the shape library: a search field, the empty state and "Browse libraries" — nothing was installed.

Page: library. Selector: `.sidebar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 294 x 900 |
| Padding | 0px |
| Border | T: none; R: none; B: none; L: 1px solid #f1f0ff |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.07 0px 100px 80px 0px, #000000 @ 0.05 0px 41.7776px 33.4221px 0px, #000000 @ 0.043 0px 22.3363px 17.869px 0px, #000000 @ 0.035 0px 12.5216px 10.0172px 0px, #000000 @ 0.027 0px 6.6501px 5.32008px 0px, #000000 @ 0.02 0px 2.76726px 2.21381px 0px |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Text node | div.library-menu-items__no-items__label: Assistant 18px/27px 700, #6965db |
| Transition | none |
| Icon | 16 x 16, colour #1b1b1f |
| Painted layers | div.Island.sidebar 294.0x900.0 bg #ffffff border L:1px solid #f1f0ff shadow #000000 @ 0.07 0px 100px 80px 0px, #000000 @ 0.05 0px 41.7776px 33.4221px 0px, #000000 @ 0.043 0px 22.3363px 17.869px 0px, #000000 @ 0.035 0px 12.5216px 10.0172px 0px, #000000 @ 0.027 0px 6.6501px 5.32008px 0px, #000000 @ 0.02 0px 2.76726px 2.21381px 0px; div::after.sidebar__header 269pxx1px bg #f1f0ff; div.sidebar-triggers 150.0x42.0 bg #ffffff border T:1px solid #f1f0ff / R:1px solid #f1f0ff / B:1px solid #f1f0ff / L:1px solid #f1f0ff r 10px; button.excalidraw-button.sidebar-tab-trigger 36.0x36.0 bg #6965db r 8px; button.excalidraw-button.sidebar__close 36.0x36.0 bg #f1f0ff r 8px; button.dropdown-menu-button.zen-mode-transition 36.0x36.0 bg #f6f6f9 border T:1px solid #f1f0ff / R:1px solid #f1f0ff / B:1px solid #f1f0ff / L:1px solid #f1f0ff r 8px |
| How | at rest |

Crops: `lib-panel-default.png`.

#### lib-search

Library search. The search field revealed by the first tab button at the library head; focused, never submitted.

Page: library. Selector: `library search input`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 217 x 24 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Assistant 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1b1f | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #757575, opacity 1 | = |
| Ancestor paint | 1 up div.ExcTextField__input bg #f5f5f9 | = |
| How | at rest | Shift+Tab, Tab |

Crops: `lib-search-default.png`, `lib-search-focus-visible.png`.

#### lib-empty

Library empty state. The "no shapes yet" empty-state text inside the panel.

Page: library. Selector: `library empty state`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 265 x 68 |
| Padding | 16px 0px |
| Gap | 10px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Text node | a.library-menu-browse-button: Assistant 12px/normal 600, #ffffff |
| Transition | none |
| Painted layers | a.library-menu-browse-button 265.0x36.0 bg #6965db r 8px |
| How | at rest |

Crops: `lib-empty-default.png`.

#### lib-browse-btn

Browse libraries button. The "Browse libraries" action — opens the community libraries list; measured never followed.

Page: library. Selector: `library Browse button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 265 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #6965db | #5753d0 | #5753d0 | #4440bf |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | 1px auto #101010 offset 1px |
| Font | Assistant 12px/normal 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.library-menu-browse-button 265.0x36.0 bg #6965db r 8px | a.library-menu-browse-button 265.0x36.0 bg #5753d0 r 8px | a.library-menu-browse-button 265.0x36.0 bg #5753d0 r 8px outline 1px auto #101010 offset 1px | a.library-menu-browse-button 265.0x36.0 bg #4440bf r 8px outline 1px auto #101010 offset 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `lib-browse-btn-default.png`, `lib-browse-btn-hover.png`, `lib-browse-btn-focus-visible.png`, `lib-browse-btn-pressed.png`.

#### lib-overflow

Library overflow. The "…" overflow menu button at the library head (Reset library, import); measured never pressed.

Page: library. Selector: `library overflow button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 10px | = | = | = |
| Border | 1px solid #f1f0ff | = | = | 1px solid #4440bf |
| Radius | 8px | = | = | = |
| Background | #f6f6f9 | #f1f0ff | #f1f0ff | #f1f0ff |
| Box shadow | none | = | #5753d0 0px 0px 0px 1px | #6965db 0px 0px 0px 1px |
| Outline | none | = | = | = |
| Font | Assistant 13.3328px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 16, colour #1b1b1f | = | = | = |
| Painted layers | button.dropdown-menu-button.zen-mode-transition 36.0x36.0 bg #f6f6f9 border T:1px solid #f1f0ff / R:1px solid #f1f0ff / B:1px solid #f1f0ff / L:1px solid #f1f0ff r 8px | button.dropdown-menu-button.zen-mode-transition 36.0x36.0 bg #f1f0ff border T:1px solid #f1f0ff / R:1px solid #f1f0ff / B:1px solid #f1f0ff / L:1px solid #f1f0ff r 8px | button.dropdown-menu-button.zen-mode-transition 36.0x36.0 bg #f1f0ff border T:1px solid #f1f0ff / R:1px solid #f1f0ff / B:1px solid #f1f0ff / L:1px solid #f1f0ff r 8px shadow #5753d0 0px 0px 0px 1px | button.dropdown-menu-button.zen-mode-transition 36.0x36.0 bg #f1f0ff border T:1px solid #4440bf / R:1px solid #4440bf / B:1px solid #4440bf / L:1px solid #4440bf r 8px shadow #6965db 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `lib-overflow-default.png`, `lib-overflow-hover.png`, `lib-overflow-focus-visible.png`, `lib-overflow-pressed.png`.

### Dialogs

#### export-dialog

Export dialog. The "Export image" modal: checkerboard preview, Background/Dark-mode/Embed switches, the 1×/2×/3× scale radio and PNG/SVG/copy actions — none pressed.

Page: dialogs. Selector: `.Dialog Export image`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 919.8 x 396 |
| Padding | 40px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Text node | h3: Assistant 21.008px/27.3104px 700, #1b1b1f |
| Transition | none |
| Icon | 18 x 18, colour #1b1b1f |
| Painted layers | div.Island 919.8x396.0 bg #ffffff; div.ImageExportModal__preview__canvas 466.3x324.0 image url(data:…) border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 12px; div.Switch.toggled 36.0x18.0 bg #6965db border T:1px solid #6965db / R:1px solid #6965db / B:1px solid #6965db / L:1px solid #6965db r 12px; div::before.Switch.toggled 14pxx14px bg #ffffff r 100%; div.Switch 36.0x18.0 bg #ffffff border T:1px solid #767680 / R:1px solid #767680 / B:1px solid #767680 / L:1px solid #767680 r 12px; div::before.Switch 10pxx10px bg #1b1b1f r 100% |
| Ancestor paint | 1 up div.Modal__content bg #ffffff shadow #000000 @ 0.07 0px 100px 80px 0px, #000000 @ 0.05 0px 41.7776px 33.4221px 0px, #000000 @ 0.043 0px 22.3363px 17.869px 0px, #000000 @ 0.035 0px 12.5216px 10.0172px 0px, #000000 @ 0.027 0px 6.6501px 5.32008px 0px, #000000 @ 0.02 0px 2.76726px 2.21381px 0px |
| How | at rest |

Crops: `export-dialog-default.png`.

#### export-preview

Export preview. The checkerboard transparency preview pane inside the export dialog.

Page: dialogs. Selector: `export preview pane`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 518.09 x 360 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Transition | none |
| Painted layers | div.ImageExportModal__preview__canvas 518.1x360.0 image url(data:…) border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 12px |
| How | at rest |

Crops: `export-preview-default.png`.

#### export-switch

Export switch. A labelled toggle in the dialog (Background/Dark mode/Embed scene); measured never flipped.

Page: dialogs. Selector: `export Switch`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 40 x 20 | = | - |
| Padding | 0px | = | - |
| Border | 1px solid #6965db | 1px solid #5b57d1 | - |
| Radius | 12px | = | - |
| Background | #6965db | #5b57d1 | - |
| Box shadow | none | = | - |
| Outline | none | = | - |
| Font | Assistant 16px/normal 400 | = | - |
| Letter spacing | normal | = | - |
| Colour | #1b1b1f | = | - |
| Transition | background, border 0.15s ease-out | = | - |
| ::before | 14px x 14px, absolute, bg #ffffff, radius 100% | = | - |
| Painted layers | div.Switch.toggled 40.0x20.0 bg #6965db border T:1px solid #6965db / R:1px solid #6965db / B:1px solid #6965db / L:1px solid #6965db r 12px; div::before.Switch.toggled 14pxx14px bg #ffffff r 100% | div.Switch.toggled 40.0x20.0 bg #5b57d1 border T:1px solid #5b57d1 / R:1px solid #5b57d1 / B:1px solid #5b57d1 / L:1px solid #5b57d1 r 12px; div::before.Switch.toggled 14pxx14px bg #ffffff r 100% | - |
| How | at rest | mouse hover | - |
| Skipped | - | = | focus failed: keyboard focus did not reach the element |

Crops: `export-switch-default.png`, `export-switch-hover.png`.

#### export-scale

Scale radio. The 1×/2×/3× scale segmented control.

Page: dialogs. Selector: `export scale RadioGroup`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 108 x 32 |
| Padding | 3px |
| Gap | 2px |
| Border | 1px solid #f1f0ff |
| Radius | 10px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Text node | div.RadioGroup__choice: Assistant 12px/12px 600, #6965db, ls 0.4px |
| Transition | none |
| Painted layers | div.RadioGroup 108.0x32.0 bg #ffffff border T:1px solid #f1f0ff / R:1px solid #f1f0ff / B:1px solid #f1f0ff / L:1px solid #f1f0ff r 10px; div.RadioGroup__choice 32.0x24.0 bg #ffffff r 8px; div.RadioGroup__choice.active 32.0x24.0 bg #6965db r 8px; div.RadioGroup__choice 32.0x24.0 bg #ffffff r 8px |
| How | at rest |

Crops: `export-scale-default.png`.

#### export-png

PNG button. The accent "PNG" export action; measured never pressed (no file was produced).

Page: dialogs. Selector: `export PNG`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 84 x 40 | = | = |
| Padding | 8px 16px | = | = |
| Border | 1px solid #000000 @ 0 | = | = |
| Radius | 8px | = | = |
| Background | #6965db | #5753d0 | #5753d0 |
| Box shadow | none | = | #5753d0 0px 0px 0px 1px |
| Outline | none | = | = |
| Font | Assistant 12px/normal 600 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Text node | div.ExcButton__contents: Assistant 12px/normal 600, #ffffff | = | = |
| Transition | none | all 0.15s ease-out | all 0.15s ease-out |
| Cursor | pointer | = | = |
| Icon | 20 x 20, colour #ffffff | = | = |
| Painted layers | button.ExcButton.ExcButton--color-primary 84.0x40.0 bg #6965db border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.ExcButton.ExcButton--color-primary 84.0x40.0 bg #5753d0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.ExcButton.ExcButton--color-primary 84.0x40.0 bg #5753d0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #5753d0 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `export-png-default.png`, `export-png-hover.png`, `export-png-focus-visible.png`.

#### export-svg

SVG button. The "SVG" export action beside PNG; measured never pressed.

Page: dialogs. Selector: `export SVG`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 81 x 40 | = | = |
| Padding | 8px 16px | = | = |
| Border | 1px solid #000000 @ 0 | = | = |
| Radius | 8px | = | = |
| Background | #6965db | #5753d0 | #5753d0 |
| Box shadow | none | = | #5753d0 0px 0px 0px 1px |
| Outline | none | = | = |
| Font | Assistant 12px/normal 600 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Text node | div.ExcButton__contents: Assistant 12px/normal 600, #ffffff | = | = |
| Transition | none | all 0.15s ease-out | all 0.15s ease-out |
| Cursor | pointer | = | = |
| Icon | 20 x 20, colour #ffffff | = | = |
| Painted layers | button.ExcButton.ExcButton--color-primary 81.0x40.0 bg #6965db border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.ExcButton.ExcButton--color-primary 81.0x40.0 bg #5753d0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.ExcButton.ExcButton--color-primary 81.0x40.0 bg #5753d0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #5753d0 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `export-svg-default.png`, `export-svg-hover.png`, `export-svg-focus-visible.png`.

#### shortcuts-dialog

Shortcuts dialog. The keyboard-shortcuts sheet opened by ? — a column of actions and their keycaps.

Page: dialogs. Selector: `shortcuts dialog`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 945.11 x 807.28 |
| Padding | 0px |
| Border | 1px solid #ebebeb |
| Radius | 12px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.07 0px 100px 80px 0px, #000000 @ 0.05 0px 41.7776px 33.4221px 0px, #000000 @ 0.043 0px 22.3363px 17.869px 0px, #000000 @ 0.035 0px 12.5216px 10.0172px 0px, #000000 @ 0.027 0px 6.6501px 5.32008px 0px, #000000 @ 0.02 0px 2.76726px 2.21381px 0px |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Text node | span.Dialog__titleContent: Assistant 20px/normal 700, #1b1b1f |
| Transition | none |
| Transform | matrix(0.98449, 0, 0, 0.98449, 0, 0) |
| Opacity | 0.844903 |
| Icon | 15.75 x 15.75, colour #1b1b1f |
| Painted layers | div.Modal__content 945.1x807.3 bg #ffffff border T:1px solid #ebebeb / R:1px solid #ebebeb / B:1px solid #ebebeb / L:1px solid #ebebeb r 12px shadow #000000 @ 0.07 0px 100px 80px 0px, #000000 @ 0.05 0px 41.7776px 33.4221px 0px, #000000 @ 0.043 0px 22.3363px 17.869px 0px, #000000 @ 0.035 0px 12.5216px 10.0172px 0px, #000000 @ 0.027 0px 6.6501px 5.32008px 0px, #000000 @ 0.02 0px 2.76726px 2.21381px 0px; div.Island 943.1x1993.6 bg #ffffff; h2.Dialog__title 864.4x38.4 border B:1px solid #ebebeb; a.HelpDialog__btn 142.0x37.4 bg #f6f6f9 border T:1px solid #f6f6f9 / R:1px solid #f6f6f9 / B:1px solid #f6f6f9 / L:1px solid #f6f6f9 r 8px; a.HelpDialog__btn 132.1x37.4 bg #f6f6f9 border T:1px solid #f6f6f9 / R:1px solid #f6f6f9 / B:1px solid #f6f6f9 / L:1px solid #f6f6f9 r 8px outline 1px auto #101010 offset 1px; a.HelpDialog__btn 184.9x37.4 bg #f6f6f9 border T:1px solid #f6f6f9 / R:1px solid #f6f6f9 / B:1px solid #f6f6f9 / L:1px solid #f6f6f9 r 8px |
| How | at rest |

Crops: `shortcuts-dialog-default.png`.

#### shortcut-row

Shortcut row. A row in the shortcuts sheet (action name + keycap).

Page: dialogs. Selector: `shortcut row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 427 x 1093 |
| Padding | 0px |
| Border | 1px solid #ebebeb |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Text node | div: Assistant 14px/normal 400, #1b1b1f |
| Transition | none |
| Painted layers | div.HelpDialog__island-content 427.0x1093.0 border T:1px solid #ebebeb / R:1px solid #ebebeb / B:1px solid #ebebeb / L:1px solid #ebebeb r 8px; div.HelpDialog__shortcut 425.0x39.0 border B:1px solid #ebebeb; kbd.HelpDialog__key 22.0x26.0 bg #e3e2fe r 6px; div.HelpDialog__shortcut 425.0x39.0 border B:1px solid #ebebeb; kbd.HelpDialog__key 21.0x26.0 bg #e3e2fe r 6px; kbd.HelpDialog__key 21.0x26.0 bg #e3e2fe r 6px |
| How | at rest |

Crops: `shortcut-row-default.png`.

#### keycap

Keycap. A rendered key chip (e.g. "Ctrl") inside the shortcuts sheet.

Page: dialogs. Selector: `kbd keycap`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 22 x 26 |
| Padding | 0px |
| Gap | normal 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 14px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Text node | kbd.HelpDialog__key: Assistant 10px/10px 400, #1b1b1f |
| Transition | none |
| Painted layers | kbd.HelpDialog__key 22.0x26.0 bg #e3e2fe r 6px |
| How | at rest |

Crops: `keycap-default.png`.

#### cmdk-dialog

Command palette. The Ctrl+/ launcher: a search field over grouped commands (App / Editor); nothing was invoked.

Page: dialogs. Selector: `.command-palette-dialog`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 718 x 748 |
| Padding | 24px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Text node | div.shortcut-key: Assistant 10px/normal 400, #1b1b1f |
| Transition | none |
| Icon | 16 x 16, colour #000000 |
| Painted layers | div.Island 718.0x748.0 bg #ffffff; div.ExcTextField__input 670.0x48.0 bg #ececf4 border T:1px solid #4440bf / R:1px solid #4440bf / B:1px solid #4440bf / L:1px solid #4440bf r 8px; div.shortcut-key 18.0x16.0 bg #e3e2fe r 4px; div.shortcut-key 14.0x16.0 bg #e3e2fe r 4px; div.shortcut-key 22.0x16.0 bg #e3e2fe r 4px; div.command-item.item-selected 666.0x40.0 bg #f6f6f9 r 8px |
| Ancestor paint | 1 up div.Modal__content bg #ffffff shadow #000000 @ 0.07 0px 100px 80px 0px, #000000 @ 0.05 0px 41.7776px 33.4221px 0px, #000000 @ 0.043 0px 22.3363px 17.869px 0px, #000000 @ 0.035 0px 12.5216px 10.0172px 0px, #000000 @ 0.027 0px 6.6501px 5.32008px 0px, #000000 @ 0.02 0px 2.76726px 2.21381px 0px |
| How | at rest |

Crops: `cmdk-dialog-default.png`.

#### cmdk-input

Palette input. The search field at the palette head.

Page: dialogs. Selector: `palette input`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 644 x 24 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Assistant 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1b1f | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #757575, opacity 1 | = |
| Ancestor paint | 1 up div.ExcTextField__input bg #ececf4 | = |
| How | at rest | Shift+Tab, Tab |

Crops: `cmdk-input-default.png`, `cmdk-input-focus-visible.png`.

#### cmdk-item

Palette item. A command row inside the palette (with its shortcut hint); measured, never invoked.

Page: dialogs. Selector: `palette item`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 666 x 40 | = |
| Padding | 0px 8px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #f6f6f9 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Assistant 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span: Assistant 16px/normal 400, #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #000000 | = |
| Painted layers | div.command-item.item-selected 666.0x40.0 bg #f6f6f9 r 8px; div.shortcut-key 26.0x16.0 bg #e3e2fe r 4px; div.shortcut-key 19.0x16.0 bg #e3e2fe r 4px; div.shortcut-key 14.0x16.0 bg #e3e2fe r 4px | = |
| How | at rest | mouse hover |

Crops: `cmdk-item-default.png`, `cmdk-item-hover.png`.

#### export-copy

Copy-to-clipboard button. The "Copy to clipboard" ExcButton in the export dialog (a filled primary variant); measured never pressed.

Page: dialogs. Selector: `.ExcButton Copy to clipboard`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 154 x 40 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #6965db | #5753d0 | #5753d0 | #4440bf |
| Box shadow | none | = | #5753d0 0px 0px 0px 1px | #5753d0 0px 0px 0px 1px |
| Outline | none | = | = | = |
| Font | Assistant 12px/normal 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.ExcButton__contents: Assistant 12px/normal 600, #ffffff | = | = | = |
| Transition | none | all 0.15s ease-out | all 0.15s ease-out | all 0.15s ease-out |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = |
| Painted layers | button.ExcButton.ExcButton--color-primary 154.0x40.0 bg #6965db border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.ExcButton.ExcButton--color-primary 154.0x40.0 bg #5753d0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.ExcButton.ExcButton--color-primary 154.0x40.0 bg #5753d0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #5753d0 0px 0px 0px 1px | button.ExcButton.ExcButton--color-primary 154.0x40.0 bg #4440bf border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #5753d0 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `export-copy-default.png`, `export-copy-hover.png`, `export-copy-focus-visible.png`, `export-copy-pressed.png`.

### Dark theme

#### d-island

Tool island (dark). The same toolbar Island in dark theme — near-black surface, light icons.

Page: dark. Selector: `.Island.App-toolbar (theme--dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 542 x 44 |
| Padding | 4px |
| Border | none |
| Radius | 8px |
| Background | #232329 |
| Box shadow | #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #e3e3e8 |
| Text node | span.ToolIcon__keybinding: Assistant 10px/normal 400, #7a7a7a |
| Transition | none |
| Cursor | default |
| Icon | 16 x 16, colour #e3e3e8 |
| Painted layers | div.Island.App-toolbar 542.0x44.0 bg #232329 r 8px shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px; div.App-toolbar__divider 1.0x24.0 bg #2e2d39; div.App-toolbar__divider 1.0x24.0 bg #2e2d39; button.dropdown-menu-button.App-toolbar__extra-tools-trigger 36.0x36.0 bg #403e6a r 8px |
| How | at rest |

Crops: `d-island-default.png`.

#### d-tool

Tool button (dark). A tool button in dark theme.

Page: dark. Selector: `tool button (dark)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #228be6 0px 0px 0px 2px | = |
| Outline | none | = | = | = |
| Font | Assistant 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #e3e3e8 | = | = | = |
| Text node | span.ToolIcon__keybinding: Assistant 10px/normal 400, #7a7a7a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #e3e3e8 | = | = | = |
| Ancestor paint | 2 up div.Island.App-toolbar bg #232329 shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | div.ToolIcon__icon 36.0x36.0 bg #2e2d39 r 8px | button.ToolIcon.ToolIcon_type_toggle 36.0x36.0 r 8px shadow #228be6 0px 0px 0px 2px | = |

Crops: `d-tool-default.png`, `d-tool-hover.png`, `d-tool-focus-visible.png`, `d-tool-pressed.png`.

#### d-menu-panel

Main menu (dark). The hamburger dropdown in dark theme.

Page: dark. Selector: `.dropdown-menu.main-menu (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 225 x 648 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #e3e3e8 |
| Text node | span: Assistant 14px/normal 400, #e3e3e8 |
| Transition | none |
| Cursor | default |
| Icon | 16 x 16, colour #e3e3e8 |
| Painted layers | div.Island.dropdown-menu-container 225.0x648.0 bg #232329 r 8px shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px, #000000 @ 0.15 0px 0px 0px 1px; div 209.0x1.0 bg #2e2d39; div 209.0x1.0 bg #2e2d39; div.RadioGroup 108.0x32.0 bg #232329 border T:1px solid #2e2d39 / R:1px solid #2e2d39 / B:1px solid #2e2d39 / L:1px solid #2e2d39 r 10px; div.RadioGroup__choice 32.0x24.0 bg #232329 r 8px; div.RadioGroup__choice.active 32.0x24.0 bg #a8a5ff r 8px |
| How | at rest |

Crops: `d-menu-panel-default.png`.

#### d-menu-item

Menu item (dark). A menu row in dark theme.

Page: dark. Selector: `menu item (dark)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 119 x 18 | = |
| Padding | 0px | = |
| Gap | 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Assistant 14px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #e3e3e8 | = |
| Text node | span: Assistant 14px/normal 400, #e3e3e8 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Ancestor paint | 2 up div.Island.dropdown-menu-container bg #232329 shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px, #000000 @ 0.15 0px 0px 0px 1px | 1 up button.radix-menu-item.dropdown-menu-item bg #2e2d39; 2 up div.Island.dropdown-menu-container bg #232329 shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px, #000000 @ 0.15 0px 0px 0px 1px |
| How | at rest | mouse hover |

Crops: `d-menu-item-default.png`, `d-menu-item-hover.png`.

#### d-props

Properties panel (dark). The properties sidebar in dark theme.

Page: dark. Selector: `.App-menu__left (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 195 x 543 |
| Padding | 12px |
| Border | none |
| Radius | 8px |
| Background | #232329 |
| Box shadow | #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #e3e3e8 |
| Text node | h3: Assistant 12px/normal 400, #e3e3e8 |
| Transition | none |
| Cursor | default |
| Icon | 16 x 16, colour #e3e3e8 |
| Painted layers | div.Island.App-menu__left 195.0x543.0 bg #232329 r 8px shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #d3d3d3 r 4px; div.color-picker__button-outline 24.0x24.0 r 4px shadow #beb9ff 0px 0px 0px 1px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #ff8383 r 4px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #39994b r 4px; button.color-picker__button.top-picks-dnd__pick 22.0x22.0 bg #56a2e8 r 4px |
| How | at rest |

Crops: `d-props-default.png`.

### Mobile (390 wide)

#### m-welcome

Welcome screen (mobile). The first-run overlay at 390 wide: logo, note and menu fill the sheet.

Page: mobile. Selector: `.welcome-screen-center (mobile)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 780 |
| Padding | 0px |
| Gap | 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Text node | div.welcome-screen-center__heading.welcome-screen-decor: Excalifont 18px/21.6px 400, #b8b8b8 |
| Transition | none |
| Icon | 40 x 40, colour #6965db |
| Painted layers | button.welcome-screen-menu-item 300.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px; button.welcome-screen-menu-item 300.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px; button.welcome-screen-menu-item 300.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px; a.welcome-screen-menu-item 300.0x44.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px |
| How | at rest |

Crops: `m-welcome-default.png`.

#### m-welcome-item

Welcome item (mobile). A welcome menu row on the phone layout.

Page: mobile. Selector: `welcome item (mobile)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 300 x 42 |
| Padding | 12px |
| Border | 1px solid #000000 @ 0 |
| Radius | 6px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 14px/normal 400 |
| Letter spacing | normal |
| Colour | #999999 |
| Text node | div.welcome-screen-menu-item__text: Arial 14px/normal 400, #999999 |
| Transition | none |
| Cursor | pointer |
| Icon | 16 x 16, colour #999999 |
| Painted layers | button.welcome-screen-menu-item 300.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px |
| How | at rest |

Crops: `m-welcome-item-default.png`.

#### m-toolbar

Mobile toolbar. The bottom tool bar at 390 wide: a single row of tools plus the overflow trigger.

Page: mobile. Selector: `.mobile-toolbar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 362 x 44 |
| Padding | 4px |
| Border | none |
| Radius | 8px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Transition | none |
| Icon | 16 x 16, colour #1b1b1f |
| Painted layers | div.Island.App-toolbar 362.0x44.0 bg #ffffff r 8px shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px; div.ToolIcon__icon 36.0x36.0 bg #e0dfff r 8px; div.tool-popover-content 92.0x52.0 bg #ffffff r 8px shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px; div.ToolIcon__icon 36.0x36.0 bg #e0dfff r 8px |
| How | at rest |

Crops: `m-toolbar-default.png`.

#### m-tool

Tool button (mobile). A tool button in the phone toolbar.

Page: mobile. Selector: `tool button (mobile)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 36 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 4px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Transition | none |
| Cursor | pointer |
| Icon | 16 x 16, colour #030064 |
| Painted layers | div.ToolIcon__icon 36.0x36.0 bg #e0dfff r 8px |
| Ancestor paint | 2 up div.Island.App-toolbar bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px |
| How | at rest |

Crops: `m-tool-default.png`.

#### m-extra-trigger

Extra tools (mobile). The overflow trigger at the phone toolbar tail.

Page: mobile. Selector: `extra trigger (mobile)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 36 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 13.3328px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Transition | none |
| Cursor | pointer |
| Icon | 16 x 16, colour #1b1b1f |
| Ancestor paint | 3 up div.Island.App-toolbar bg #ffffff shadow #000000 @ 0.17 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 3px 0px, #000000 @ 0.05 0px 7px 14px 0px |
| How | at rest |

Crops: `m-extra-trigger-default.png`.

#### m-menu-trigger

Hamburger (mobile). The floating menu button top-left.

Page: mobile. Selector: `menu trigger (mobile)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 32 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | #ececf4 |
| Box shadow | #ffffff 0px 0px 0px 1px |
| Outline | none |
| Font | Assistant 13.3328px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Transition | none |
| Cursor | pointer |
| Icon | 16 x 16, colour #1b1b1f |
| Painted layers | button.dropdown-menu-button.main-menu-trigger 32.0x32.0 bg #ececf4 r 8px shadow #ffffff 0px 0px 0px 1px |
| How | at rest |

Crops: `m-menu-trigger-default.png`.

#### m-lib-trigger

Library trigger (mobile). The floating library button top-right.

Page: mobile. Selector: `lib trigger (mobile)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 32 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Transition | none |
| Cursor | pointer |
| Icon | 16 x 16, colour #1b1b1f |
| Painted layers | div.sidebar-trigger.default-sidebar-trigger 32.0x32.0 bg #ececf4 r 8px shadow #ffffff 0px 0px 0px 1px |
| How | at rest |

Crops: `m-lib-trigger-default.png`.

#### m-shape-actions

Shape actions (mobile). The compact-shape-actions bar that appears above the toolbar when a shape tool is picked on the phone.

Page: mobile. Selector: `.compact-shape-actions`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 362 x 43.19 |
| Padding | 0px |
| Gap | 6px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Assistant 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1f |
| Transition | none |
| Icon | 30 x 30, colour #ffffff |
| Painted layers | button.color-picker__button.active-color 32.0x32.0 bg #1e1e1e border T:1px solid #f1f0ff / R:1px solid #f1f0ff / B:1px solid #f1f0ff / L:1px solid #f1f0ff r 5px; button.color-picker__button.active-color 32.0x32.0 image url(data:…) border T:1px solid #f1f0ff / R:1px solid #f1f0ff / B:1px solid #f1f0ff / L:1px solid #f1f0ff r 5px shadow #ebebeb 0px 0px 0px 1px; button.compact-action-button.properties-trigger 32.0x32.0 bg #ffffff @ 0.35 r 8px; button.ToolIcon_type_button.ToolIcon_size_medium 32.0x32.0 bg #ffffff @ 0.35 r 8px; button.ToolIcon_type_button.ToolIcon_size_medium 32.0x32.0 bg #ffffff @ 0.35 r 8px |
| How | at rest |

Crops: `m-shape-actions-default.png`.

## Transitions declared in the readable stylesheets

excalidraw.com serves its CSS bundles same-origin, so this list holds the transitions the readable sheets declare; the per-state Transition rows above are computed values and cover every rule the page paints.

- editor: `transform 0.14s, opacity 0.14s, box-shadow 0.14s`, `width 0.15s, height 0.15s`, `transform 0.15s, opacity 0.15s, box-shadow 0.15s`, `transform 0.18s cubic-bezier(0.2, 0.8, 0.3, 1), width 0.18s, height 0.18s`, `box-shadow 0.5s ease-in-out`, `0.2s`, `unset`, `transform 0.12s, background-color 0.12s, color 0.12s`, `0.15s ease-out`, `border-color 0.2s`, `color 0.2s`, `width 0.1s ease-in-out`

- welcome: `transform 0.14s, opacity 0.14s, box-shadow 0.14s`, `width 0.15s, height 0.15s`, `transform 0.15s, opacity 0.15s, box-shadow 0.15s`, `transform 0.18s cubic-bezier(0.2, 0.8, 0.3, 1), width 0.18s, height 0.18s`, `box-shadow 0.5s ease-in-out`, `0.2s`, `unset`, `transform 0.12s, background-color 0.12s, color 0.12s`, `0.15s ease-out`, `border-color 0.2s`, `color 0.2s`, `width 0.1s ease-in-out`
