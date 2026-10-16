# NotebookLM component measurements

Computed styles read on 2026-10-17 by `tools/capture/signed-in/measure.mjs` from static page copies of the signed-in app (1440x900 (the mobile-* copies 390x844), deviceScaleFactor 2), and written here by `tools/capture/signed-in/build-measurements.mjs` from [components-computed.json](components-computed.json). Every copy was taken in dark. Light is the same copy with the body class dark-theme swapped for light-theme, which is what the in-app Light mode does. Dark states have plain names; light states are `light`, `light-<state>`. Every state records `theme` and `snapshot`.

Every component has one table per theme: a column per state, a row per property. A cell that repeats the first column reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline (a hover or selection is sometimes painted on an inner layer, not the element itself); "Ancestor paint" the same for its parents. NotebookLM's Angular Material and nb-* classes name no variables in the markup, so the theme variables behind these values are in [css-vars.json](css-vars.json) instead.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab), skipped where the element cannot take focus; `pressed` is the mouse held down on the element (:active). NotebookLM draws focus rings in plain CSS (:focus-visible outlines on nb-buttons, the .mat-focus-indicator ::before box on Material controls), so they survive in the static copies. The rest (`selected`, `open`, `readonly`, `off`, `option-highlighted`) are other elements or copies captured in that state. Light states are prefixed `light` and were read from the same copies with the body class swapped to light-theme. The 390 wide copies are measured at rest only.

64 components, 336 states (336 measured, 0 skipped, 0 not found).

## Shared values

Tallied over every measured state by the build script.

- **Radius scale** (element radius, times seen): 9999px (116), 20px (22), 96px (12), 32px (12), 16px (10), 12px (10), 40px (10), 8px (10), 50% (10), 28px (6), 100px (6), 24px (2), 4px (2).
- **Transitions**: `box-shadow 0.28s cubic-bezier(0.4, 0, 0.2, 1)` (46), `color 0.2s ease` (18), `border 0.28s cubic-bezier(0.4, 0, 0.2, 1)` (14), `padding 0.15s cubic-bezier(0.4, 0, 0.2, 1)` (10), `background-color, border-color 0.2s ease-in-out` (8), `outline 0.15s ease` (8), `opacity 0.2s linear` (8), `transform 0.15s cubic-bezier(0, 0, 0.2, 1)` (6), `transform, -webkit-transform 0.2s cubic-bezier(0.05, 0.7, 0.1, 1)` (6), `inline-size, min-inline-size 0.2s ease-in-out` (4).
- **Font families**: Google Sans Flex (370), Luminous Symbols (104), Times (84), Arial (28), Google Symbols (26), Google Sans Text (4).
- **Type sizes** (size/line-height weight of the first text): 20px/20px 400 (90), 15px/20px 400 (26), 24px/24px 400 (26), 13px/17px 400 (20), 15px/normal 370 (18), 16px/20px 400 (14), 17px/24px 400 (12), 16px/normal 400 (12), 15px/40px 370 (12), 14px/20px 500 (10), 18px/18px 400 (8), 13px/16px 400 (8), 36px/36px 400 (8), 11.008px/16px 500 (8).
- **Shadows**: `#000000 @ 0.28 0px 0px 20px 0px` (24); `#000000 @ 0.04 0px 0px 20px 0px` (24); `#000000 @ 0.08 0px 0px 0px 1px inset` (18); `#000000 @ 0.2 0px 3px 1px -2px, #000000 @ 0.14 0px 2px 2px 0px, #000000 @ 0.12 0px 1px 5px 0px` (4); `#000000 @ 0.2 0px 3px 5px -1px, #000000 @ 0.14 0px 6px 10px 0px, #000000 @ 0.12 0px 1px 18px 0px` (4); `#000000 @ 0.1 0px 1px 3px 0px` (2).
- **Focus-visible, dark** (31 focused states): nothing painted on the element (14); outline 3px solid #e6e6e6 offset 2px (10); outline 1px auto #99c8ff offset 0px (3); outline 1px auto #99c8ff offset 1px (2); shadow #000000 @ 0.28 0px 0px 20px 0px (1); outline 2px solid #e6e6e6 offset 2px (1).
- **Focus-visible, light** (31 focused states): nothing painted on the element (14); outline 3px solid #000000 offset 2px (10); outline 1px auto #005fcc offset 0px (3); outline 1px auto #005fcc offset 1px (2); shadow #000000 @ 0.04 0px 0px 20px 0px (1); outline 2px solid #000000 offset 2px (1).
- **Hover changes, dark** (29 hovered components, 13 with no change on the element or its first painted layer): inner layer #e6e6e6 → #e6e6e6 (5); inner layer undefined → undefined (3); backgroundColor #000000 @ 0 → #e6e6e6 @ 0.08 (1); inner layer #ababab → #ababab (1); inner layer none → #e6e6e6 (1); backgroundColor #171717 → #000000 @ 0 (1); backgroundColor #000000 @ 0 → #171717 (1).
- **Hover changes, light** (29 hovered components, 13 with no change on the element or its first painted layer): inner layer #000000 → #000000 (5); inner layer undefined → undefined (3); backgroundColor #000000 @ 0 → #000000 @ 0.08 (1); inner layer #5e5e5e → #5e5e5e (1); inner layer none → #000000 (1); backgroundColor #f2f0f0 → #000000 @ 0 (1); backgroundColor #000000 @ 0 → #f2f0f0 (1).

### Tokens the measured components use

Every custom property a measured component's classes or inline style name, with the value it resolved to in each theme.

| Token | Dark | Light |
|---|---|---|

## Components

### Buttons

#### button-accent

Accent button (New notebook). nb-button type accent: the one filled page action.

Page copy: `home-dark`. Finder: `() => Q('nb-button.nb-button-type-accent button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 147.09 x 36 | = | = | = |
| Padding | 0px 12px 0px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #1f3b9b | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #e6e6e6 offset 2px | = |
| Font | Google Sans Flex 15px/normal 370 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #e6e6e6 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.nb-icon-size-large: Luminous Symbols 20px/20px 400, #e6e6e6 | = | = | = |
| Transition | box-shadow 0.28s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | pointer | = | pointer |
| Painted layers | button.mdc-button.mat-mdc-button-base.mat-badge 147.1x36.0 bg #1f3b9b r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 147.094pxx36px bg #e6e6e6 r 9999px opacity 0 | button.mdc-button.mat-mdc-button-base.mat-badge 147.1x36.0 bg #1f3b9b r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 147.094pxx36px bg #e6e6e6 r 9999px opacity 0.08 | button.mdc-button.mat-mdc-button-base.mat-badge 147.1x36.0 bg #1f3b9b r 9999px outline 3px solid #e6e6e6 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 147.094pxx36px bg #e6e6e6 r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #e6e6e6 / R:3px solid #e6e6e6 / B:3px solid #e6e6e6 / L:3px solid #e6e6e6 r 9999px | button.mdc-button.mat-mdc-button-base.mat-badge 147.1x36.0 bg #1f3b9b r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 147.094pxx36px bg #e6e6e6 r 9999px opacity 0.12 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 147.09 x 36 | = | = | = |
| Padding | 0px 12px 0px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #9dd2ff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #000000 offset 2px | = |
| Font | Google Sans Flex 15px/normal 370 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.nb-icon-size-large: Luminous Symbols 20px/20px 400, #000000 | = | = | = |
| Transition | box-shadow 0.28s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | pointer | = | pointer |
| Painted layers | button.mdc-button.mat-mdc-button-base.mat-badge 147.1x36.0 bg #9dd2ff r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 147.094pxx36px bg #000000 r 9999px opacity 0 | button.mdc-button.mat-mdc-button-base.mat-badge 147.1x36.0 bg #9dd2ff r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 147.094pxx36px bg #000000 r 9999px opacity 0.08 | button.mdc-button.mat-mdc-button-base.mat-badge 147.1x36.0 bg #9dd2ff r 9999px outline 3px solid #000000 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 147.094pxx36px bg #000000 r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #000000 / R:3px solid #000000 / B:3px solid #000000 / L:3px solid #000000 r 9999px | button.mdc-button.mat-mdc-button-base.mat-badge 147.1x36.0 bg #9dd2ff r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 147.094pxx36px bg #000000 r 9999px opacity 0.12 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Crops: `button-accent-default.png`, `button-accent-hover.png`, `button-accent-focus-visible.png`, `button-accent-pressed.png`, `button-accent-light.png`, `button-accent-light-hover.png`, `button-accent-light-focus-visible.png`, `button-accent-light-pressed.png`.

#### button-tonal

Tonal button (Add sources). mat-tonal-button, full panel width.

Page copy: `notebook-dark`. Finder: `() => Q('nb-button.add-source-button button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 336 x 36 | = | = | = |
| Padding | 0px 12px 0px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #171717 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #e6e6e6 offset 2px | = |
| Font | Google Sans Flex 15px/normal 370 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #e6e6e6 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.nb-icon-size-large: Luminous Symbols 20px/20px 400, #e6e6e6 | = | = | = |
| Transition | box-shadow 0.28s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | pointer | = | pointer |
| Painted layers | button.mdc-button.mat-mdc-button-base.mat-badge 336.0x36.0 bg #171717 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 336pxx36px bg #e6e6e6 r 9999px opacity 0 | button.mdc-button.mat-mdc-button-base.mat-badge 336.0x36.0 bg #171717 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 336pxx36px bg #e6e6e6 r 9999px opacity 0.08 | button.mdc-button.mat-mdc-button-base.mat-badge 336.0x36.0 bg #171717 r 9999px outline 3px solid #e6e6e6 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 336pxx36px bg #e6e6e6 r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #e6e6e6 / R:3px solid #e6e6e6 / B:3px solid #e6e6e6 / L:3px solid #e6e6e6 r 9999px | button.mdc-button.mat-mdc-button-base.mat-badge 336.0x36.0 bg #171717 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 336pxx36px bg #e6e6e6 r 9999px opacity 0.12 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 336 x 36 | = | = | = |
| Padding | 0px 12px 0px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #f2f0f0 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #000000 offset 2px | = |
| Font | Google Sans Flex 15px/normal 370 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.nb-icon-size-large: Luminous Symbols 20px/20px 400, #000000 | = | = | = |
| Transition | box-shadow 0.28s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | pointer | = | pointer |
| Painted layers | button.mdc-button.mat-mdc-button-base.mat-badge 336.0x36.0 bg #f2f0f0 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 336pxx36px bg #000000 r 9999px opacity 0 | button.mdc-button.mat-mdc-button-base.mat-badge 336.0x36.0 bg #f2f0f0 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 336pxx36px bg #000000 r 9999px opacity 0.08 | button.mdc-button.mat-mdc-button-base.mat-badge 336.0x36.0 bg #f2f0f0 r 9999px outline 3px solid #000000 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 336pxx36px bg #000000 r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #000000 / R:3px solid #000000 / B:3px solid #000000 / L:3px solid #000000 r 9999px | button.mdc-button.mat-mdc-button-base.mat-badge 336.0x36.0 bg #f2f0f0 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 336pxx36px bg #000000 r 9999px opacity 0.12 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Crops: `button-tonal-default.png`, `button-tonal-hover.png`, `button-tonal-focus-visible.png`, `button-tonal-pressed.png`, `button-tonal-light.png`, `button-tonal-light-hover.png`, `button-tonal-light-focus-visible.png`, `button-tonal-light-pressed.png`.

#### button-text

Text button (Create notebook, header).

Page copy: `notebook-dark`. Finder: `() => Q('nb-button.create-notebook-button button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 170.88 x 36 | = | = | = |
| Padding | 0px 16px 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #e6e6e6 offset 2px | = |
| Font | Google Sans Flex 15px/normal 370 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #e6e6e6 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.nb-icon-size-large: Luminous Symbols 20px/20px 400, #e6e6e6 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | pointer | = | pointer |
| Painted layers | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 170.875pxx36px bg #e6e6e6 r 9999px opacity 0 | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 170.875pxx36px bg #e6e6e6 r 9999px opacity 0.08 | button.mdc-button.mat-mdc-button-base.mat-badge 170.9x36.0 r 9999px outline 3px solid #e6e6e6 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 170.875pxx36px bg #e6e6e6 r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #e6e6e6 / R:3px solid #e6e6e6 / B:3px solid #e6e6e6 / L:3px solid #e6e6e6 r 9999px | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 170.875pxx36px bg #e6e6e6 r 9999px opacity 0.12 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 170.88 x 36 | = | = | = |
| Padding | 0px 16px 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #000000 offset 2px | = |
| Font | Google Sans Flex 15px/normal 370 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.nb-icon-size-large: Luminous Symbols 20px/20px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | pointer | = | pointer |
| Painted layers | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 170.875pxx36px bg #000000 r 9999px opacity 0 | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 170.875pxx36px bg #000000 r 9999px opacity 0.08 | button.mdc-button.mat-mdc-button-base.mat-badge 170.9x36.0 r 9999px outline 3px solid #000000 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 170.875pxx36px bg #000000 r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #000000 / R:3px solid #000000 / B:3px solid #000000 / L:3px solid #000000 r 9999px | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 170.875pxx36px bg #000000 r 9999px opacity 0.12 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Crops: `button-text-default.png`, `button-text-hover.png`, `button-text-focus-visible.png`, `button-text-pressed.png`, `button-text-light.png`, `button-text-light-hover.png`, `button-text-light-focus-visible.png`, `button-text-light-pressed.png`.

#### button-outlined

Outlined button (Upload files).

Page copy: `notebook-dark-add-sources`. Finder: `() => Q('[role=dialog] button.source-action-button.mdc-button--outlined')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140.45 x 40 | = | = | = |
| Padding | 6px 14px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #ffffff @ 0.12 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #e6e6e6 @ 0.08 | = | #e6e6e6 @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Google Sans Flex 17px/24px 370 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #e6e6e6 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.google-symbols: Luminous Symbols 18px/18px 400, #ffffff @ 0.55 | = | = | = |
| Transition | background-color, border-color 0.2s, 0.2s ease-in-out, ease-in-out delay 0s, 0s | = | = | = |
| Cursor | default | pointer | = | pointer |
| Painted layers | button.mdc-button.mat-mdc-button-base.source-action-button 140.5x40.0 border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 140.453pxx40px bg #e6e6e6 r 9999px opacity 0 | button.mdc-button.mat-mdc-button-base.source-action-button 140.5x40.0 bg #e6e6e6 @ 0.08 border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 140.453pxx40px bg #e6e6e6 r 9999px opacity 0.08 | button.mdc-button.mat-mdc-button-base.source-action-button 140.5x40.0 border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 140.453pxx40px bg #e6e6e6 r 9999px opacity 0; span.mat-focus-indicator::before 150.453pxx50px border T:3px solid #c3cafc / R:3px solid #c3cafc / B:3px solid #c3cafc / L:3px solid #c3cafc r 9999px | button.mdc-button.mat-mdc-button-base.source-action-button 140.5x40.0 bg #e6e6e6 @ 0.08 border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 140.453pxx40px bg #e6e6e6 r 9999px opacity 0.12 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 140.45 x 40 | = | = | = |
| Padding | 6px 14px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0.08 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #000000 @ 0.08 | = | #000000 @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Google Sans Flex 17px/24px 370 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.google-symbols: Luminous Symbols 18px/18px 400, #000000 @ 0.55 | = | = | = |
| Transition | background-color, border-color 0.2s, 0.2s ease-in-out, ease-in-out delay 0s, 0s | = | = | = |
| Cursor | default | pointer | = | pointer |
| Painted layers | button.mdc-button.mat-mdc-button-base.source-action-button 140.5x40.0 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 140.453pxx40px bg #000000 r 9999px opacity 0 | button.mdc-button.mat-mdc-button-base.source-action-button 140.5x40.0 bg #000000 @ 0.08 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 140.453pxx40px bg #000000 r 9999px opacity 0.08 | button.mdc-button.mat-mdc-button-base.source-action-button 140.5x40.0 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 140.453pxx40px bg #000000 r 9999px opacity 0; span.mat-focus-indicator::before 150.453pxx50px border T:3px solid #4259ff / R:3px solid #4259ff / B:3px solid #4259ff / L:3px solid #4259ff r 9999px | button.mdc-button.mat-mdc-button-base.source-action-button 140.5x40.0 bg #000000 @ 0.08 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 140.453pxx40px bg #000000 r 9999px opacity 0.12 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Crops: `button-outlined-default.png`, `button-outlined-hover.png`, `button-outlined-focus-visible.png`, `button-outlined-pressed.png`, `button-outlined-light.png`, `button-outlined-light-hover.png`, `button-outlined-light-focus-visible.png`, `button-outlined-light-pressed.png`.

#### button-dialog-primary

Dialog confirm button (Save, Configure Chat). Disabled while the Custom prompt is empty.

Page copy: `notebook-dark-configure-chat`, `notebook-dark-configure-chat-custom`. Finder: `() => Q('[role=dialog] button.submit-button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed | disabled |
|---|---|---|---|---|---|
| Size (w x h) | 80 x 40 | = | = | = | = |
| Padding | 0px 24px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 96px | = | = | = | = |
| Background | #4259ff | = | = | = | #e6e6e6 @ 0.12 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Google Sans Flex 15px/normal 370 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | = | = | = | #ababab |
| Text node | span.mdc-button__label: Google Sans Flex 15px/normal 370, #ffffff | = | = | = | span.mdc-button__label: Google Sans Flex 15px/normal 370, #ababab |
| Transition | box-shadow 0.28s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | default | pointer | = | pointer | = |
| Painted layers | button.mdc-button.mat-mdc-button-base.submit-button 80.0x40.0 bg #4259ff r 96px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 80pxx40px bg #062e6f r 96px opacity 0 | button.mdc-button.mat-mdc-button-base.submit-button 80.0x40.0 bg #4259ff r 96px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 80pxx40px bg #062e6f r 96px opacity 0.08 | button.mdc-button.mat-mdc-button-base.submit-button 80.0x40.0 bg #4259ff r 96px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 80pxx40px bg #062e6f r 96px opacity 0; span.mat-focus-indicator::before 90pxx50px border T:3px solid #c3cafc / R:3px solid #c3cafc / B:3px solid #c3cafc / L:3px solid #c3cafc r 96px | button.mdc-button.mat-mdc-button-base.submit-button 80.0x40.0 bg #4259ff r 96px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 80pxx40px bg #062e6f r 96px opacity 0.12 | button.mdc-button.mat-mdc-button-base.submit-button 80.0x40.0 bg #e6e6e6 @ 0.12 r 96px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 80pxx40px bg #ffffff @ 0.55 r 96px opacity 0 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down | at rest, captured disabled |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed | light-disabled |
|---|---|---|---|---|---|
| Size (w x h) | 80 x 40 | = | = | = | = |
| Padding | 0px 24px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 96px | = | = | = | = |
| Background | #4259ff | = | = | = | #000000 @ 0.12 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Google Sans Flex 15px/normal 370 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | = | = | = | #5e5e5e |
| Text node | span.mdc-button__label: Google Sans Flex 15px/normal 370, #ffffff | = | = | = | span.mdc-button__label: Google Sans Flex 15px/normal 370, #5e5e5e |
| Transition | box-shadow 0.28s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | default | pointer | = | pointer | = |
| Painted layers | button.mdc-button.mat-mdc-button-base.submit-button 80.0x40.0 bg #4259ff r 96px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 80pxx40px bg #ffffff r 96px opacity 0 | button.mdc-button.mat-mdc-button-base.submit-button 80.0x40.0 bg #4259ff r 96px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 80pxx40px bg #ffffff r 96px opacity 0.08 | button.mdc-button.mat-mdc-button-base.submit-button 80.0x40.0 bg #4259ff r 96px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 80pxx40px bg #ffffff r 96px opacity 0; span.mat-focus-indicator::before 90pxx50px border T:3px solid #4259ff / R:3px solid #4259ff / B:3px solid #4259ff / L:3px solid #4259ff r 96px | button.mdc-button.mat-mdc-button-base.submit-button 80.0x40.0 bg #4259ff r 96px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 80pxx40px bg #ffffff r 96px opacity 0.12 | button.mdc-button.mat-mdc-button-base.submit-button 80.0x40.0 bg #000000 @ 0.12 r 96px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 80pxx40px bg #000000 @ 0.55 r 96px opacity 0 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down | at rest, captured disabled |

Other finders: disabled: `() => Q('[role=dialog] button.submit-button')`; light-disabled: `() => Q('[role=dialog] button.submit-button')`.

Crops: `button-dialog-primary-default.png`, `button-dialog-primary-hover.png`, `button-dialog-primary-focus-visible.png`, `button-dialog-primary-pressed.png`, `button-dialog-primary-disabled.png`, `button-dialog-primary-light.png`, `button-dialog-primary-light-hover.png`, `button-dialog-primary-light-focus-visible.png`, `button-dialog-primary-light-pressed.png`, `button-dialog-primary-light-disabled.png`.

#### button-disabled

Disabled filled button (Insert). Stays disabled while the URL field is empty or invalid.

Page copy: `notebook-dark-website-dialog`. Finder: `() => Q('[role=dialog] button.mdc-button--unelevated')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 86.77 x 40 |
| Padding | 0px 24px |
| Border | none |
| Radius | 96px |
| Background | #e6e6e6 @ 0.12 |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 15px/normal 370 |
| Letter spacing | normal |
| Colour | #ababab |
| Text node | span.mdc-button__label: Google Sans Flex 15px/normal 370, #ababab |
| Transition | box-shadow 0.28s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | default |
| Painted layers | button.mdc-button.mat-mdc-button-base.mdc-button--unelevated 86.8x40.0 bg #e6e6e6 @ 0.12 r 96px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 86.7656pxx40px bg #ffffff @ 0.55 r 96px opacity 0 |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 86.77 x 40 |
| Padding | 0px 24px |
| Border | none |
| Radius | 96px |
| Background | #000000 @ 0.12 |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 15px/normal 370 |
| Letter spacing | normal |
| Colour | #5e5e5e |
| Text node | span.mdc-button__label: Google Sans Flex 15px/normal 370, #5e5e5e |
| Transition | box-shadow 0.28s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | default |
| Painted layers | button.mdc-button.mat-mdc-button-base.mdc-button--unelevated 86.8x40.0 bg #000000 @ 0.12 r 96px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 86.7656pxx40px bg #000000 @ 0.55 r 96px opacity 0 |
| How | at rest |

Crops: `button-disabled-default.png`, `button-disabled-light.png`.

#### button-confirm-delete

Delete confirmation buttons (Delete). The destructive action is a tonal button; it was never clicked.

Page copy: `home-dark-delete-confirm`. Finder: `() => Q('[role=dialog] nb-button.yes-button button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed | cancel | cancel-hover | cancel-focus-visible |
|---|---|---|---|---|---|---|---|
| Size (w x h) | 76.34 x 48 | = | = | = | 78.73 x 48 | 78.73 x 48 | 78.73 x 48 |
| Padding | 0px 16px | = | = | = | = | = | = |
| Border | none | = | = | = | = | = | = |
| Radius | 9999px | = | = | = | = | = | = |
| Background | #171717 | = | = | = | transparent | transparent | transparent |
| Box shadow | none | = | = | = | = | = | = |
| Outline | none | = | 3px solid #e6e6e6 offset 2px | = | = | = | 3px solid #e6e6e6 offset 2px |
| Font | Google Sans Flex 15px/normal 370 | = | = | = | = | = | = |
| Letter spacing | normal | = | = | = | = | = | = |
| Colour | #e6e6e6 | = | = | = | = | = | = |
| Text node | span: Google Sans Flex 15px/20px 400, #e6e6e6 | = | = | = | = | = | = |
| Transition | box-shadow 0.28s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | none | none | none |
| Cursor | default | pointer | = | pointer | = | pointer | = |
| Painted layers | button.mdc-button.mat-mdc-button-base.mat-badge 76.3x48.0 bg #171717 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 76.3438pxx48px bg #e6e6e6 r 9999px opacity 0 | = | button.mdc-button.mat-mdc-button-base.mat-badge 76.3x48.0 bg #171717 r 9999px outline 3px solid #e6e6e6 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 76.3438pxx48px bg #e6e6e6 r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #e6e6e6 / R:3px solid #e6e6e6 / B:3px solid #e6e6e6 / L:3px solid #e6e6e6 r 9999px | button.mdc-button.mat-mdc-button-base.mat-badge 76.3x48.0 bg #171717 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 76.3438pxx48px bg #e6e6e6 r 9999px opacity 0.12 | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 78.7344pxx48px bg #e6e6e6 r 9999px opacity 0 | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 78.7344pxx48px bg #e6e6e6 r 9999px opacity 0.08 | button.mdc-button.mat-mdc-button-base.mat-badge 78.7x48.0 r 9999px outline 3px solid #e6e6e6 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 78.7344pxx48px bg #e6e6e6 r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #e6e6e6 / R:3px solid #e6e6e6 / B:3px solid #e6e6e6 / L:3px solid #e6e6e6 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down | at rest, captured cancel | mouse hover | keyboard: focus(), Shift+Tab, Tab |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed | light-cancel | light-cancel-hover | light-cancel-focus-visible |
|---|---|---|---|---|---|---|---|
| Size (w x h) | 76.34 x 48 | = | = | = | 78.73 x 48 | 78.73 x 48 | 78.73 x 48 |
| Padding | 0px 16px | = | = | = | = | = | = |
| Border | none | = | = | = | = | = | = |
| Radius | 9999px | = | = | = | = | = | = |
| Background | #f2f0f0 | = | = | = | transparent | transparent | transparent |
| Box shadow | none | = | = | = | = | = | = |
| Outline | none | = | 3px solid #000000 offset 2px | = | = | = | 3px solid #000000 offset 2px |
| Font | Google Sans Flex 15px/normal 370 | = | = | = | = | = | = |
| Letter spacing | normal | = | = | = | = | = | = |
| Colour | #000000 | = | = | = | = | = | = |
| Text node | span: Google Sans Flex 15px/20px 400, #000000 | = | = | = | = | = | = |
| Transition | box-shadow 0.28s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | none | none | none |
| Cursor | default | pointer | = | pointer | = | pointer | = |
| Painted layers | button.mdc-button.mat-mdc-button-base.mat-badge 76.3x48.0 bg #f2f0f0 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 76.3438pxx48px bg #000000 r 9999px opacity 0 | = | button.mdc-button.mat-mdc-button-base.mat-badge 76.3x48.0 bg #f2f0f0 r 9999px outline 3px solid #000000 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 76.3438pxx48px bg #000000 r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #000000 / R:3px solid #000000 / B:3px solid #000000 / L:3px solid #000000 r 9999px | button.mdc-button.mat-mdc-button-base.mat-badge 76.3x48.0 bg #f2f0f0 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 76.3438pxx48px bg #000000 r 9999px opacity 0.12 | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 78.7344pxx48px bg #000000 r 9999px opacity 0 | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 78.7344pxx48px bg #000000 r 9999px opacity 0.08 | button.mdc-button.mat-mdc-button-base.mat-badge 78.7x48.0 r 9999px outline 3px solid #000000 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 78.7344pxx48px bg #000000 r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #000000 / R:3px solid #000000 / B:3px solid #000000 / L:3px solid #000000 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down | at rest, captured cancel | mouse hover | keyboard: focus(), Shift+Tab, Tab |

Other finders: cancel: `() => Q('[role=dialog] nb-button.no-button button')`; light-cancel: `() => Q('[role=dialog] nb-button.no-button button')`; cancel-hover: `() => Q('[role=dialog] nb-button.no-button button')`; light-cancel-hover: `() => Q('[role=dialog] nb-button.no-button button')`; cancel-focus-visible: `() => Q('[role=dialog] nb-button.no-button button')`; light-cancel-focus-visible: `() => Q('[role=dialog] nb-button.no-button button')`.

Crops: `button-confirm-delete-default.png`, `button-confirm-delete-hover.png`, `button-confirm-delete-focus-visible.png`, `button-confirm-delete-pressed.png`, `button-confirm-delete-cancel.png`, `button-confirm-delete-cancel-hover.png`, `button-confirm-delete-cancel-focus-visible.png`, `button-confirm-delete-light.png`, `button-confirm-delete-light-hover.png`, `button-confirm-delete-light-focus-visible.png`, `button-confirm-delete-light-pressed.png`, `button-confirm-delete-light-cancel.png`, `button-confirm-delete-light-cancel-hover.png`, `button-confirm-delete-light-cancel-focus-visible.png`.

#### icon-button

Icon button (Settings, 36px).

Page copy: `home-dark`. Finder: `() => Q('button[aria-label="Settings"]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #e6e6e6 offset 2px | = |
| Font | Arial 24px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #e6e6e6 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.nb-icon-size-large: Luminous Symbols 20px/20px 400, #e6e6e6 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #e6e6e6 r 9999px opacity 0 | span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #e6e6e6 r 9999px opacity 0.08 | button.mdc-icon-button.mat-mdc-icon-button.mat-mdc-button-base 36.0x36.0 r 9999px outline 3px solid #e6e6e6 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #e6e6e6 r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #e6e6e6 / R:3px solid #e6e6e6 / B:3px solid #e6e6e6 / L:3px solid #e6e6e6 r 9999px | span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #e6e6e6 r 9999px opacity 0.12 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #000000 offset 2px | = |
| Font | Arial 24px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.nb-icon-size-large: Luminous Symbols 20px/20px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #000000 r 9999px opacity 0 | span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #000000 r 9999px opacity 0.08 | button.mdc-icon-button.mat-mdc-icon-button.mat-mdc-button-base 36.0x36.0 r 9999px outline 3px solid #000000 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #000000 r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #000000 / R:3px solid #000000 / B:3px solid #000000 / L:3px solid #000000 r 9999px | span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #000000 r 9999px opacity 0.12 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Crops: `icon-button-default.png`, `icon-button-hover.png`, `icon-button-focus-visible.png`, `icon-button-pressed.png`, `icon-button-light.png`, `icon-button-light-hover.png`, `icon-button-light-focus-visible.png`, `icon-button-light-pressed.png`.

#### icon-button-small

Icon button, small (card actions, 28px).

Page copy: `home-dark`. Finder: `() => Q('project-button .project-button-more button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 28 x 28 | = | = | = |
| Padding | 2px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #e6e6e6 offset 2px | = |
| Font | Arial 24px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ababab | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.nb-icon-size-large: Luminous Symbols 20px/20px 400, #ababab | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 28pxx28px bg #ababab r 9999px opacity 0 | span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 28pxx28px bg #ababab r 9999px opacity 0.08 | button.mdc-icon-button.mat-mdc-icon-button.mat-mdc-button-base 28.0x28.0 r 9999px outline 3px solid #e6e6e6 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 28pxx28px bg #ababab r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #e6e6e6 / R:3px solid #e6e6e6 / B:3px solid #e6e6e6 / L:3px solid #e6e6e6 r 9999px | span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 28pxx28px bg #ababab r 9999px opacity 0.12 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 28 x 28 | = | = | = |
| Padding | 2px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #000000 offset 2px | = |
| Font | Arial 24px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #5e5e5e | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.nb-icon-size-large: Luminous Symbols 20px/20px 400, #5e5e5e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 28pxx28px bg #5e5e5e r 9999px opacity 0 | span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 28pxx28px bg #5e5e5e r 9999px opacity 0.08 | button.mdc-icon-button.mat-mdc-icon-button.mat-mdc-button-base 28.0x28.0 r 9999px outline 3px solid #000000 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 28pxx28px bg #5e5e5e r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #000000 / R:3px solid #000000 / B:3px solid #000000 / L:3px solid #000000 r 9999px | span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 28pxx28px bg #5e5e5e r 9999px opacity 0.12 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Crops: `icon-button-small-default.png`, `icon-button-small-hover.png`, `icon-button-small-focus-visible.png`, `icon-button-small-pressed.png`, `icon-button-small-light.png`, `icon-button-small-light-hover.png`, `icon-button-small-light-focus-visible.png`, `icon-button-small-light-pressed.png`.

#### search-pill

Search pill (outlined button that opens search).

Page copy: `home-dark`. Finder: `() => Q('nb-button.search-pill-button button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 256 x 36 | = | = | = |
| Padding | 0px 12px 0px 8px | = | = | = |
| Border | 1px solid #ffffff @ 0.12 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #e6e6e6 offset 2px | = |
| Font | Google Sans Flex 15px/normal 370 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #e6e6e6 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.nb-icon-size-large: Luminous Symbols 20px/20px 400, #ffffff @ 0.55 | = | = | = |
| Transition | border 0.28s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | text | = | = | = |
| Painted layers | button.mdc-button.mat-mdc-button-base.mat-badge 256.0x36.0 border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 256pxx36px bg #e6e6e6 r 9999px opacity 0 | button.mdc-button.mat-mdc-button-base.mat-badge 256.0x36.0 border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 256pxx36px bg #171717 r 9999px | button.mdc-button.mat-mdc-button-base.mat-badge 256.0x36.0 border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 9999px outline 3px solid #e6e6e6 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 256pxx36px bg #e6e6e6 r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #e6e6e6 / R:3px solid #e6e6e6 / B:3px solid #e6e6e6 / L:3px solid #e6e6e6 r 9999px | button.mdc-button.mat-mdc-button-base.mat-badge 256.0x36.0 border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 256pxx36px bg #171717 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 256 x 36 | = | = | = |
| Padding | 0px 12px 0px 8px | = | = | = |
| Border | 1px solid #000000 @ 0.08 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #000000 offset 2px | = |
| Font | Google Sans Flex 15px/normal 370 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.nb-icon-size-large: Luminous Symbols 20px/20px 400, #000000 @ 0.55 | = | = | = |
| Transition | border 0.28s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | text | = | = | = |
| Painted layers | button.mdc-button.mat-mdc-button-base.mat-badge 256.0x36.0 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 256pxx36px bg #000000 r 9999px opacity 0 | button.mdc-button.mat-mdc-button-base.mat-badge 256.0x36.0 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 256pxx36px bg #f2f0f0 r 9999px | button.mdc-button.mat-mdc-button-base.mat-badge 256.0x36.0 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 9999px outline 3px solid #000000 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 256pxx36px bg #000000 r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #000000 / R:3px solid #000000 / B:3px solid #000000 / L:3px solid #000000 r 9999px | button.mdc-button.mat-mdc-button-base.mat-badge 256.0x36.0 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 256pxx36px bg #f2f0f0 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Crops: `search-pill-default.png`, `search-pill-hover.png`, `search-pill-focus-visible.png`, `search-pill-pressed.png`, `search-pill-light.png`, `search-pill-light-hover.png`, `search-pill-light-focus-visible.png`, `search-pill-light-pressed.png`.

### Links

#### link

Link (Learn more, Notifications dialog).

Page copy: `home-dark-notifications-dialog`. Finder: `() => Q('[role=dialog] a.learn-more-link')`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 76.17 x 18 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #99c8ff offset 1px |
| Font | Google Sans Flex 14px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #4259ff | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |
| Painted layers | - | = | a.learn-more-link 76.2x18.0 outline 1px auto #99c8ff offset 1px |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 76.17 x 18 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px |
| Font | Google Sans Flex 14px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #4259ff | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |
| Painted layers | - | = | a.learn-more-link 76.2x18.0 outline 1px auto #005fcc offset 1px |

Crops: `link-default.png`, `link-hover.png`, `link-focus-visible.png`, `link-light.png`, `link-light-hover.png`, `link-light-focus-visible.png`.

#### link-inline

Inline link in help text (learn more).

Page copy: `notebook-dark-website-dialog`. Finder: `() => Q('[role=dialog] a.learn-more')`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 64.48 x 15 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #99c8ff offset 1px |
| Font | Google Sans Flex 12px/20px 400 | = | = |
| Letter spacing | 0.096px | = | = |
| Colour | #c3cafc | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |
| Painted layers | - | = | a.learn-more 64.5x15.0 outline 1px auto #99c8ff offset 1px |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 64.48 x 15 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px |
| Font | Google Sans Flex 12px/20px 400 | = | = |
| Letter spacing | 0.096px | = | = |
| Colour | #4259ff | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |
| Painted layers | - | = | a.learn-more 64.5x15.0 outline 1px auto #005fcc offset 1px |

Crops: `link-inline-default.png`, `link-inline-hover.png`, `link-inline-focus-visible.png`, `link-inline-light.png`, `link-inline-light-hover.png`, `link-inline-light-focus-visible.png`.

### Inputs

#### text-field

Text field (Add people and groups).

Page copy: `notebook-dark-share-dialog`. Finder: `() => C(Q('[role=dialog] input.mat-mdc-input-element'), 'mat-form-field')`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 386.06 x 56 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Google Sans Flex 17px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #c7c7c7 | = | = |
| Text node | mat-label: Google Sans Flex 17px/normal 400, #e6e6e6 | = | = |
| Transition | none | = | = |
| Placeholder | "" #e6e6e6, opacity 1, 17px | = | = |
| Painted layers | div.mat-mdc-notch-piece.mdc-notched-outline__leading 16.0x56.0 border T:1px solid #37383b / B:1px solid #37383b / L:1px solid #37383b r 16px 0px 0px 16px; div.mat-mdc-notch-piece.mdc-notched-outline__notch 138.8x56.0 border B:1px solid #37383b / L:1px solid #000000 @ 0; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 232.3x56.0 border T:1px solid #37383b / R:1px solid #37383b / B:1px solid #37383b r 0px 16px 16px 0px | div.mat-mdc-notch-piece.mdc-notched-outline__leading 16.0x56.0 border T:1px solid #e6e6e6 / B:1px solid #e6e6e6 / L:1px solid #e6e6e6 r 16px 0px 0px 16px; div.mat-mdc-notch-piece.mdc-notched-outline__notch 138.8x56.0 border B:1px solid #e6e6e6 / L:1px solid #000000 @ 0; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 232.3x56.0 border T:1px solid #e6e6e6 / R:1px solid #e6e6e6 / B:1px solid #e6e6e6 r 0px 16px 16px 0px | div.mat-mdc-notch-piece.mdc-notched-outline__leading 16.0x56.0 border T:2px solid #e6e6e6 / B:2px solid #e6e6e6 / L:2px solid #e6e6e6 r 16px 0px 0px 16px; div.mat-mdc-notch-piece.mdc-notched-outline__notch 138.8x56.0 border B:2px solid #e6e6e6 / L:1px solid #000000 @ 0; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 232.3x56.0 border T:2px solid #e6e6e6 / R:2px solid #e6e6e6 / B:2px solid #e6e6e6 r 0px 16px 16px 0px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 386.06 x 56 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Google Sans Flex 17px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #303030 | = | = |
| Text node | mat-label: Google Sans Flex 17px/normal 400, #000000 @ 0.92 | mat-label: Google Sans Flex 17px/normal 400, #000000 | mat-label: Google Sans Flex 17px/normal 400, #000000 |
| Transition | none | = | = |
| Placeholder | "" #000000, opacity 1, 17px | = | = |
| Painted layers | div.mat-mdc-notch-piece.mdc-notched-outline__leading 16.0x56.0 border T:1px solid #dde1eb / B:1px solid #dde1eb / L:1px solid #dde1eb r 16px 0px 0px 16px; div.mat-mdc-notch-piece.mdc-notched-outline__notch 138.8x56.0 border B:1px solid #dde1eb / L:1px solid #000000 @ 0; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 232.3x56.0 border T:1px solid #dde1eb / R:1px solid #dde1eb / B:1px solid #dde1eb r 0px 16px 16px 0px | div.mat-mdc-notch-piece.mdc-notched-outline__leading 16.0x56.0 border T:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 16px 0px 0px 16px; div.mat-mdc-notch-piece.mdc-notched-outline__notch 138.8x56.0 border B:1px solid #000000 / L:1px solid #000000 @ 0; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 232.3x56.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 r 0px 16px 16px 0px | div.mat-mdc-notch-piece.mdc-notched-outline__leading 16.0x56.0 border T:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 16px 0px 0px 16px; div.mat-mdc-notch-piece.mdc-notched-outline__notch 138.8x56.0 border B:2px solid #000000 / L:1px solid #000000 @ 0; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 232.3x56.0 border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 r 0px 16px 16px 0px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) |

Crops: `text-field-default.png`, `text-field-hover.png`, `text-field-focus-visible.png`, `text-field-light.png`, `text-field-light-hover.png`, `text-field-light-focus-visible.png`.

#### search-field

Search field (expanded header search).

Page copy: `search-dark-empty`, `home-dark-search-typed`. Finder: `() => C(Q('input[aria-label="Search notebooks"]'), 'mat-form-field') // P(Q('input[aria-label="Search notebooks"]'))`.

Dark theme.

| Property | default | hover | focus-visible | typed |
|---|---|---|---|---|
| Size (w x h) | 650 x 44 | = | = | = |
| Padding | 0px | = | = | 0px 4px 0px 8px |
| Border | none | = | = | = |
| Radius | 0px | = | = | 9999px |
| Background | transparent | = | = | #1f1f1f |
| Box shadow | none | = | = | #000000 @ 0.28 0px 0px 20px 0px |
| Outline | none | = | = | = |
| Font | Google Sans Flex 17px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #c7c7c7 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.search-icon: Luminous Symbols 20px/20px 400, #ffffff @ 0.55 | = | = | = |
| Transition | none | = | = | = |
| Placeholder | "Search notebooks by keywords or topics.." #ffffff @ 0.55, opacity 1, 17px | = | = | = |
| Painted layers | div.mat-mdc-text-field-wrapper.mdc-text-field.mdc-text-field--outlined 650.0x44.0 bg #1f1f1f r 9999px shadow #000000 @ 0.28 0px 0px 20px 0px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #ababab r 9999px opacity 0 | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) | at rest, captured typed |

Light theme.

| Property | light | light-hover | light-focus-visible | light-typed |
|---|---|---|---|---|
| Size (w x h) | 650 x 44 | = | = | = |
| Padding | 0px | = | = | 0px 4px 0px 8px |
| Border | none | = | = | = |
| Radius | 0px | = | = | 9999px |
| Background | transparent | = | = | #ffffff |
| Box shadow | none | = | = | #000000 @ 0.04 0px 0px 20px 0px |
| Outline | none | = | = | = |
| Font | Google Sans Flex 17px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #303030 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.search-icon: Luminous Symbols 20px/20px 400, #000000 @ 0.55 | = | = | = |
| Transition | none | = | = | = |
| Placeholder | "Search notebooks by keywords or topics.." #000000 @ 0.55, opacity 1, 17px | = | = | = |
| Painted layers | div.mat-mdc-text-field-wrapper.mdc-text-field.mdc-text-field--outlined 650.0x44.0 bg #ffffff r 9999px shadow #000000 @ 0.04 0px 0px 20px 0px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #5e5e5e r 9999px opacity 0 | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) | at rest, captured typed |

Other finders: typed: `() => P(Q('input[placeholder]'))`; light-typed: `() => P(Q('input[placeholder]'))`.

Crops: `search-field-default.png`, `search-field-hover.png`, `search-field-focus-visible.png`, `search-field-typed.png`, `search-field-light.png`, `search-field-light-hover.png`, `search-field-light-focus-visible.png`, `search-field-light-typed.png`.

#### text-area

Text area (chat composer). A cdk-autosize <textarea> inside the rounded composer.

Page copy: `notebook-dark`, `notebook-dark-composer-typed`. Finder: `() => P(Q('textarea.query-box-input'))`.

Dark theme.

| Property | default | hover | focus-visible | typed |
|---|---|---|---|---|
| Size (w x h) | 628 x 64 | = | = | = |
| Padding | 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | #1f1f1f | = | = | = |
| Box shadow | #000000 @ 0.28 0px 0px 20px 0px | = | = | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #c7c7c7 | = | = | = |
| Text node | div.selected-num: Google Sans Flex 13px/17px 400, #ababab | = | = | textarea.cdk-textarea-autosize.mat-mdc-autocomplete-trigger.query-box-input: Google Sans Flex 16px/24px 400, #c7c7c7 |
| Transition | outline 0.15s ease | = | = | = |
| Painted layers | div.input-group 628.0x64.0 bg #1f1f1f r 32px shadow #000000 @ 0.28 0px 0px 20px 0px; nb-icon-button.submit-button.outset-focus-ring.nb-button 36.0x36.0 bg #292929 r 50%; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #000000 @ 0.08 r 9999px opacity 0 | = | = | div.input-group 628.0x64.0 bg #1f1f1f r 32px shadow #000000 @ 0.28 0px 0px 20px 0px; nb-icon-button.submit-button.outset-focus-ring.nb-button 36.0x36.0 bg #1f3b9b r 50%; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #e6e6e6 r 9999px opacity 0 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) | at rest, captured typed |

Light theme.

| Property | light | light-hover | light-focus-visible | light-typed |
|---|---|---|---|---|
| Size (w x h) | 628 x 64 | = | = | = |
| Padding | 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0.04 0px 0px 20px 0px | = | = | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #303030 | = | = | = |
| Text node | div.selected-num: Google Sans Flex 13px/17px 400, #5e5e5e | = | = | textarea.cdk-textarea-autosize.mat-mdc-autocomplete-trigger.query-box-input: Google Sans Flex 16px/24px 400, #303030 |
| Transition | outline 0.15s ease | = | = | = |
| Painted layers | div.input-group 628.0x64.0 bg #ffffff r 32px shadow #000000 @ 0.04 0px 0px 20px 0px; nb-icon-button.submit-button.outset-focus-ring.nb-button 36.0x36.0 bg #dcdbdb r 50%; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #000000 @ 0.08 r 9999px opacity 0 | = | = | div.input-group 628.0x64.0 bg #ffffff r 32px shadow #000000 @ 0.04 0px 0px 20px 0px; nb-icon-button.submit-button.outset-focus-ring.nb-button 36.0x36.0 bg #9dd2ff r 50%; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #000000 r 9999px opacity 0 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) | at rest, captured typed |

Other finders: typed: `() => P(Q('textarea.query-box-input'))`; light-typed: `() => P(Q('textarea.query-box-input'))`.

Crops: `text-area-default.png`, `text-area-hover.png`, `text-area-focus-visible.png`, `text-area-typed.png`, `text-area-light.png`, `text-area-light-hover.png`, `text-area-light-focus-visible.png`, `text-area-light-typed.png`.

#### text-area-outlined

Text area, outlined (Website URLs).

Page copy: `notebook-dark-website-dialog`, `notebook-dark-website-dialog-typed`, `notebook-dark-website-dialog-error`. Finder: `() => C(Q('[role=dialog] textarea'), 'mat-form-field')`.

Dark theme.

| Property | default | hover | focus-visible | typed | error |
|---|---|---|---|---|---|
| Size (w x h) | 625.98 x 220 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Google Sans Flex 17px/24px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #e6e6e6 | = | = | = | = |
| Transition | none | = | = | = | = |
| Painted layers | div.mat-mdc-notch-piece.mdc-notched-outline__leading 16.0x200.0 border T:1px solid #37383b / B:1px solid #37383b / L:1px solid #37383b r 16px 0px 0px 16px; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 610.0x200.0 border T:1px solid #37383b / R:1px solid #37383b / B:1px solid #37383b r 0px 16px 16px 0px | div.mat-mdc-notch-piece.mdc-notched-outline__leading 16.0x200.0 border T:1px solid #e6e6e6 / B:1px solid #e6e6e6 / L:1px solid #e6e6e6 r 16px 0px 0px 16px; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 610.0x200.0 border T:1px solid #e6e6e6 / R:1px solid #e6e6e6 / B:1px solid #e6e6e6 r 0px 16px 16px 0px | div.mat-mdc-notch-piece.mdc-notched-outline__leading 16.0x200.0 border T:2px solid #e6e6e6 / B:2px solid #e6e6e6 / L:2px solid #e6e6e6 r 16px 0px 0px 16px; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 610.0x200.0 border T:2px solid #e6e6e6 / R:2px solid #e6e6e6 / B:2px solid #e6e6e6 r 0px 16px 16px 0px | div.mat-mdc-notch-piece.mdc-notched-outline__leading 16.0x200.0 border T:2px solid #e6e6e6 / B:2px solid #e6e6e6 / L:2px solid #e6e6e6 r 16px 0px 0px 16px; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 610.0x200.0 border T:2px solid #e6e6e6 / R:2px solid #e6e6e6 / B:2px solid #e6e6e6 r 0px 16px 16px 0px | div.mat-mdc-notch-piece.mdc-notched-outline__leading 16.0x200.0 border T:1px solid #f2b8b5 / B:1px solid #f2b8b5 / L:1px solid #f2b8b5 r 16px 0px 0px 16px; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 610.0x200.0 border T:1px solid #f2b8b5 / R:1px solid #f2b8b5 / B:1px solid #f2b8b5 r 0px 16px 16px 0px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) | at rest, captured typed | at rest, captured error |
| Text node | - | = | = | textarea.mat-mdc-input-element.mat-mdc-form-field-textarea-control.mat-mdc-form-field-input-control: Google Sans Flex 17px/24px 400, #e6e6e6 | textarea.mat-mdc-input-element.mat-mdc-form-field-textarea-control.mat-mdc-form-field-input-control: Google Sans Flex 17px/24px 400, #e6e6e6 |

Light theme.

| Property | light | light-hover | light-focus-visible | light-typed | light-error |
|---|---|---|---|---|---|
| Size (w x h) | 625.98 x 220 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Google Sans Flex 17px/24px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Transition | none | = | = | = | = |
| Painted layers | div.mat-mdc-notch-piece.mdc-notched-outline__leading 16.0x200.0 border T:1px solid #dde1eb / B:1px solid #dde1eb / L:1px solid #dde1eb r 16px 0px 0px 16px; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 610.0x200.0 border T:1px solid #dde1eb / R:1px solid #dde1eb / B:1px solid #dde1eb r 0px 16px 16px 0px | div.mat-mdc-notch-piece.mdc-notched-outline__leading 16.0x200.0 border T:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 16px 0px 0px 16px; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 610.0x200.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 r 0px 16px 16px 0px | div.mat-mdc-notch-piece.mdc-notched-outline__leading 16.0x200.0 border T:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 16px 0px 0px 16px; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 610.0x200.0 border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 r 0px 16px 16px 0px | div.mat-mdc-notch-piece.mdc-notched-outline__leading 16.0x200.0 border T:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 16px 0px 0px 16px; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 610.0x200.0 border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 r 0px 16px 16px 0px | div.mat-mdc-notch-piece.mdc-notched-outline__leading 16.0x200.0 border T:1px solid #b3261e / B:1px solid #b3261e / L:1px solid #b3261e r 16px 0px 0px 16px; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 610.0x200.0 border T:1px solid #b3261e / R:1px solid #b3261e / B:1px solid #b3261e r 0px 16px 16px 0px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) | at rest, captured typed | at rest, captured error |
| Text node | - | = | = | textarea.mat-mdc-input-element.mat-mdc-form-field-textarea-control.mat-mdc-form-field-input-control: Google Sans Flex 17px/24px 400, #000000 | textarea.mat-mdc-input-element.mat-mdc-form-field-textarea-control.mat-mdc-form-field-input-control: Google Sans Flex 17px/24px 400, #000000 |

Other finders: error: `() => C(Q('[role=dialog] textarea'), 'mat-form-field')`; light-error: `() => C(Q('[role=dialog] textarea'), 'mat-form-field')`; typed: `() => C(Q('[role=dialog] textarea'), 'mat-form-field')`; light-typed: `() => C(Q('[role=dialog] textarea'), 'mat-form-field')`.

Crops: `text-area-outlined-default.png`, `text-area-outlined-hover.png`, `text-area-outlined-focus-visible.png`, `text-area-outlined-typed.png`, `text-area-outlined-error.png`, `text-area-outlined-light.png`, `text-area-outlined-light-hover.png`, `text-area-outlined-light-focus-visible.png`, `text-area-outlined-light-typed.png`, `text-area-outlined-light-error.png`.

#### error-text

Field error message.

Page copy: `notebook-dark-website-dialog-error`. Finder: `() => Q('[role=dialog] mat-error')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 593.98 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 13px/16px 400 |
| Letter spacing | normal |
| Colour | #f2b8b5 |
| Transition | none |
| ::before | 0px x 16px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 593.98 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 13px/16px 400 |
| Letter spacing | normal |
| Colour | #b3261e |
| Transition | none |
| ::before | 0px x 16px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `error-text-default.png`, `error-text-light.png`.

#### text-area-custom

Text area with counter (Custom chat prompt).

Page copy: `notebook-dark-configure-chat-custom`. Finder: `() => C(Q('[role=dialog] textarea.custom-input-textarea'), 'mat-form-field')`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 808 x 124 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Google Sans Flex 17px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #c7c7c7 | = | = |
| Text node | span: Google Sans Flex 13px/16px 400, #c7c7c7 | = | = |
| Transition | none | = | = |
| Painted layers | div.mat-mdc-notch-piece.mdc-notched-outline__leading 12.0x104.0 border T:1px solid #37383b / B:1px solid #37383b / L:1px solid #37383b r 4px 0px 0px 4px; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 796.0x104.0 border T:1px solid #37383b / R:1px solid #37383b / B:1px solid #37383b r 0px 4px 4px 0px | div.mat-mdc-notch-piece.mdc-notched-outline__leading 12.0x104.0 border T:1px solid #e6e6e6 / B:1px solid #e6e6e6 / L:1px solid #e6e6e6 r 4px 0px 0px 4px; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 796.0x104.0 border T:1px solid #e6e6e6 / R:1px solid #e6e6e6 / B:1px solid #e6e6e6 r 0px 4px 4px 0px | div.mat-mdc-notch-piece.mdc-notched-outline__leading 12.0x104.0 border T:2px solid #e6e6e6 / B:2px solid #e6e6e6 / L:2px solid #e6e6e6 r 4px 0px 0px 4px; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 796.0x104.0 border T:2px solid #e6e6e6 / R:2px solid #e6e6e6 / B:2px solid #e6e6e6 r 0px 4px 4px 0px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 808 x 124 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Google Sans Flex 17px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #303030 | = | = |
| Text node | span: Google Sans Flex 13px/16px 400, #303030 | = | = |
| Transition | none | = | = |
| Painted layers | div.mat-mdc-notch-piece.mdc-notched-outline__leading 12.0x104.0 border T:1px solid #dde1eb / B:1px solid #dde1eb / L:1px solid #dde1eb r 4px 0px 0px 4px; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 796.0x104.0 border T:1px solid #dde1eb / R:1px solid #dde1eb / B:1px solid #dde1eb r 0px 4px 4px 0px | div.mat-mdc-notch-piece.mdc-notched-outline__leading 12.0x104.0 border T:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 4px 0px 0px 4px; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 796.0x104.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 r 0px 4px 4px 0px | div.mat-mdc-notch-piece.mdc-notched-outline__leading 12.0x104.0 border T:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 4px 0px 0px 4px; div.mat-mdc-notch-piece.mdc-notched-outline__trailing 796.0x104.0 border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 r 0px 4px 4px 0px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) |

Crops: `text-area-custom-default.png`, `text-area-custom-hover.png`, `text-area-custom-focus-visible.png`, `text-area-custom-light.png`, `text-area-custom-light-hover.png`, `text-area-custom-light-focus-visible.png`.

#### select

Select (Notebook access).

Page copy: `notebook-dark-share-dialog`, `notebook-dark-share-select-open`. Finder: `() => C(Q('[role=dialog] mat-select.general-access-select-dropdown'), 'mat-form-field') // Q('[role=dialog] mat-select.general-access-select-dropdown')`.

Dark theme.

| Property | default | hover | focus-visible | open | option | option-hover | option-selected |
|---|---|---|---|---|---|---|---|
| Size (w x h) | 212 x 24 | = | = | 212 x 160 | 212 x 48 | 212 x 48 | 212 x 48 |
| Padding | 0px | = | = | 8px 0px | 0px 16px | 0px 16px | 0px 16px |
| Border | none | = | = | = | = | = | = |
| Radius | 0px | = | = | 0px 0px 4px 4px | = | = | = |
| Background | transparent | = | = | #1f1f1f | = | #e6e6e6 @ 0.08 | #e6e6e6 @ 0.12 |
| Box shadow | none | = | = | #000000 @ 0.2 0px 3px 1px -2px, #000000 @ 0.14 0px 2px 2px 0px, #000000 @ 0.12 0px 1px 5px 0px | = | = | = |
| Outline | none | = | = | = | = | = | = |
| Font | Google Sans Flex 17px/24px 400 | = | = | Google Sans Flex 14px/24px 400 | Google Sans Flex 16px/20px 400 | Google Sans Flex 16px/20px 400 | Google Sans Flex 16px/20px 400 |
| Letter spacing | normal | = | = | = | = | = | = |
| Colour | #c7c7c7 | = | = | #e6e6e6 | #e6e6e6 | #e6e6e6 | #e6e6e6 |
| Text node | span.mat-mdc-select-min-line: Google Sans Flex 14px/24px 400, #e6e6e6 | = | = | span.mdc-list-item__primary-text: Google Sans Flex 16px/20px 400, #e6e6e6 | span.mdc-list-item__primary-text: Google Sans Flex 16px/20px 400, #e6e6e6 | span.mdc-list-item__primary-text: Google Sans Flex 16px/20px 400, #e6e6e6 | span.mdc-list-item__primary-text: Google Sans Flex 16px/20px 400, #e6e6e6 |
| Transition | none | = | = | = | = | = | = |
| Icon | 24 x 24, colour #ffffff @ 0.55 | = | 24 x 24, colour #e6e6e6 | - | - | - | - |
| Painted layers | div.mat-mdc-form-field-focus-overlay 212.0x24.0 bg #e6e6e6 opacity 0 | div.mat-mdc-form-field-focus-overlay 212.0x24.0 bg #e6e6e6 opacity 0.08 | = | div.mat-mdc-select-panel.mdc-menu-surface.mdc-menu-surface--open 212.0x160.0 bg #1f1f1f r 0px 0px 4px 4px shadow #000000 @ 0.2 0px 3px 1px -2px, #000000 @ 0.14 0px 2px 2px 0px, #000000 @ 0.12 0px 1px 5px 0px; mat-option.mat-mdc-option.mdc-list-item.mdc-list-item--selected 212.0x48.0 bg #e6e6e6 @ 0.12; mat-pseudo-checkbox.mat-pseudo-checkbox.mat-mdc-option-pseudo-checkbox.mat-pseudo-checkbox-checked::after 14pxx6px border B:2px solid #c2e7ff / L:2px solid #c2e7ff; div.mat-ripple.mat-mdc-option-ripple.mat-focus-indicator::before 212pxx48px border T:3px solid #c3cafc / R:3px solid #c3cafc / B:3px solid #c3cafc / L:3px solid #c3cafc r 4px | - | mat-option.mat-mdc-option.mdc-list-item 212.0x48.0 bg #e6e6e6 @ 0.08 | mat-option.mat-mdc-option.mdc-list-item.mdc-list-item--selected 212.0x48.0 bg #e6e6e6 @ 0.12; mat-pseudo-checkbox.mat-pseudo-checkbox.mat-mdc-option-pseudo-checkbox.mat-pseudo-checkbox-checked::after 14pxx6px border B:2px solid #c2e7ff / L:2px solid #c2e7ff; div.mat-ripple.mat-mdc-option-ripple.mat-focus-indicator::before 212pxx48px border T:3px solid #c3cafc / R:3px solid #c3cafc / B:3px solid #c3cafc / L:3px solid #c3cafc r 4px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) | at rest, captured open | at rest, captured option | mouse hover | at rest, captured option-selected |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | - | = | = | pointer | pointer | pointer | pointer |
| Ancestor paint | - | = | = | = | 1 up div.mat-mdc-select-panel.mdc-menu-surface.mdc-menu-surface--open bg #1f1f1f shadow #000000 @ 0.2 0px 3px 1px -2px, #000000 @ 0.14 0px 2px 2px 0px, #000000 @ 0.12 0px 1px 5px 0px | 1 up div.mat-mdc-select-panel.mdc-menu-surface.mdc-menu-surface--open bg #1f1f1f shadow #000000 @ 0.2 0px 3px 1px -2px, #000000 @ 0.14 0px 2px 2px 0px, #000000 @ 0.12 0px 1px 5px 0px | 1 up div.mat-mdc-select-panel.mdc-menu-surface.mdc-menu-surface--open bg #1f1f1f shadow #000000 @ 0.2 0px 3px 1px -2px, #000000 @ 0.14 0px 2px 2px 0px, #000000 @ 0.12 0px 1px 5px 0px |

Light theme.

| Property | light | light-hover | light-focus-visible | light-open | light-option | light-option-hover | light-option-selected |
|---|---|---|---|---|---|---|---|
| Size (w x h) | 212 x 24 | = | = | 212 x 160 | 212 x 48 | 212 x 48 | 212 x 48 |
| Padding | 0px | = | = | 8px 0px | 0px 16px | 0px 16px | 0px 16px |
| Border | none | = | = | = | = | = | = |
| Radius | 0px | = | = | 0px 0px 4px 4px | = | = | = |
| Background | transparent | = | = | #ffffff | = | #000000 @ 0.08 | #000000 @ 0.12 |
| Box shadow | none | = | = | #000000 @ 0.2 0px 3px 1px -2px, #000000 @ 0.14 0px 2px 2px 0px, #000000 @ 0.12 0px 1px 5px 0px | = | = | = |
| Outline | none | = | = | = | = | = | = |
| Font | Google Sans Flex 17px/24px 400 | = | = | Google Sans Flex 14px/24px 400 | Google Sans Flex 16px/20px 400 | Google Sans Flex 16px/20px 400 | Google Sans Flex 16px/20px 400 |
| Letter spacing | normal | = | = | = | = | = | = |
| Colour | #303030 | = | = | #000000 | #000000 | #000000 | #000000 |
| Text node | span.mat-mdc-select-min-line: Google Sans Flex 14px/24px 400, #000000 | = | = | span.mdc-list-item__primary-text: Google Sans Flex 16px/20px 400, #000000 | span.mdc-list-item__primary-text: Google Sans Flex 16px/20px 400, #000000 | span.mdc-list-item__primary-text: Google Sans Flex 16px/20px 400, #000000 | span.mdc-list-item__primary-text: Google Sans Flex 16px/20px 400, #000000 |
| Transition | none | = | = | = | = | = | = |
| Icon | 24 x 24, colour #000000 @ 0.55 | = | 24 x 24, colour #000000 | - | - | - | - |
| Painted layers | div.mat-mdc-form-field-focus-overlay 212.0x24.0 bg #000000 opacity 0 | div.mat-mdc-form-field-focus-overlay 212.0x24.0 bg #000000 opacity 0.08 | = | div.mat-mdc-select-panel.mdc-menu-surface.mdc-menu-surface--open 212.0x160.0 bg #ffffff r 0px 0px 4px 4px shadow #000000 @ 0.2 0px 3px 1px -2px, #000000 @ 0.14 0px 2px 2px 0px, #000000 @ 0.12 0px 1px 5px 0px; mat-option.mat-mdc-option.mdc-list-item.mdc-list-item--selected 212.0x48.0 bg #000000 @ 0.12; mat-pseudo-checkbox.mat-pseudo-checkbox.mat-mdc-option-pseudo-checkbox.mat-pseudo-checkbox-checked::after 14pxx6px border B:2px solid #004a77 / L:2px solid #004a77; div.mat-ripple.mat-mdc-option-ripple.mat-focus-indicator::before 212pxx48px border T:3px solid #4259ff / R:3px solid #4259ff / B:3px solid #4259ff / L:3px solid #4259ff r 4px | - | mat-option.mat-mdc-option.mdc-list-item 212.0x48.0 bg #000000 @ 0.08 | mat-option.mat-mdc-option.mdc-list-item.mdc-list-item--selected 212.0x48.0 bg #000000 @ 0.12; mat-pseudo-checkbox.mat-pseudo-checkbox.mat-mdc-option-pseudo-checkbox.mat-pseudo-checkbox-checked::after 14pxx6px border B:2px solid #004a77 / L:2px solid #004a77; div.mat-ripple.mat-mdc-option-ripple.mat-focus-indicator::before 212pxx48px border T:3px solid #4259ff / R:3px solid #4259ff / B:3px solid #4259ff / L:3px solid #4259ff r 4px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) | at rest, captured open | at rest, captured option | mouse hover | at rest, captured option-selected |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | - | = | = | pointer | pointer | pointer | pointer |
| Ancestor paint | - | = | = | = | 1 up div.mat-mdc-select-panel.mdc-menu-surface.mdc-menu-surface--open bg #ffffff shadow #000000 @ 0.2 0px 3px 1px -2px, #000000 @ 0.14 0px 2px 2px 0px, #000000 @ 0.12 0px 1px 5px 0px | 1 up div.mat-mdc-select-panel.mdc-menu-surface.mdc-menu-surface--open bg #ffffff shadow #000000 @ 0.2 0px 3px 1px -2px, #000000 @ 0.14 0px 2px 2px 0px, #000000 @ 0.12 0px 1px 5px 0px | 1 up div.mat-mdc-select-panel.mdc-menu-surface.mdc-menu-surface--open bg #ffffff shadow #000000 @ 0.2 0px 3px 1px -2px, #000000 @ 0.14 0px 2px 2px 0px, #000000 @ 0.12 0px 1px 5px 0px |

Other finders: open: `() => Q('.mat-mdc-select-panel')`; option: `() => Q('.mat-mdc-select-panel mat-option', 1)`; light-open: `() => Q('.mat-mdc-select-panel')`; option-hover: `() => Q('.mat-mdc-select-panel mat-option', 1)`; light-option: `() => Q('.mat-mdc-select-panel mat-option', 1)`; option-selected: `() => Q('.mat-mdc-select-panel mat-option.mdc-list-item--selected')`; light-option-hover: `() => Q('.mat-mdc-select-panel mat-option', 1)`; light-option-selected: `() => Q('.mat-mdc-select-panel mat-option.mdc-list-item--selected')`.

Crops: `select-default.png`, `select-hover.png`, `select-focus-visible.png`, `select-open.png`, `select-option.png`, `select-option-hover.png`, `select-option-selected.png`, `select-light.png`, `select-light-hover.png`, `select-light-focus-visible.png`, `select-light-open.png`, `select-light-option.png`, `select-light-option-hover.png`, `select-light-option-selected.png`.

#### menu-trigger

Menu trigger (Web source type).

Page copy: `notebook-dark`. Finder: `() => Q('nb-button.corpus-menu-trigger button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 102.45 x 36 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #1f1f1f | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #e6e6e6 offset 2px | = |
| Font | Google Sans Flex 13px/normal 370 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #e6e6e6 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.corpus-select-icon: Luminous Symbols 20px/20px 400, #e6e6e6 | = | = | = |
| Transition | box-shadow 0.28s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | pointer | = | pointer |
| Painted layers | button.mdc-button.mat-mdc-button-base.mat-badge 102.5x36.0 bg #1f1f1f r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 102.453pxx36px bg #e6e6e6 r 9999px opacity 0 | button.mdc-button.mat-mdc-button-base.mat-badge 102.5x36.0 bg #1f1f1f r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 102.453pxx36px bg #e6e6e6 r 9999px opacity 0.08 | button.mdc-button.mat-mdc-button-base.mat-badge 102.5x36.0 bg #1f1f1f r 9999px outline 3px solid #e6e6e6 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 102.453pxx36px bg #e6e6e6 r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #e6e6e6 / R:3px solid #e6e6e6 / B:3px solid #e6e6e6 / L:3px solid #e6e6e6 r 9999px | button.mdc-button.mat-mdc-button-base.mat-badge 102.5x36.0 bg #1f1f1f r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 102.453pxx36px bg #e6e6e6 r 9999px opacity 0.12 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 102.45 x 36 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #000000 offset 2px | = |
| Font | Google Sans Flex 13px/normal 370 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.corpus-select-icon: Luminous Symbols 20px/20px 400, #000000 | = | = | = |
| Transition | box-shadow 0.28s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | pointer | = | pointer |
| Painted layers | button.mdc-button.mat-mdc-button-base.mat-badge 102.5x36.0 bg #ffffff r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 102.453pxx36px bg #000000 r 9999px opacity 0 | button.mdc-button.mat-mdc-button-base.mat-badge 102.5x36.0 bg #ffffff r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 102.453pxx36px bg #000000 r 9999px opacity 0.08 | button.mdc-button.mat-mdc-button-base.mat-badge 102.5x36.0 bg #ffffff r 9999px outline 3px solid #000000 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 102.453pxx36px bg #000000 r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #000000 / R:3px solid #000000 / B:3px solid #000000 / L:3px solid #000000 r 9999px | button.mdc-button.mat-mdc-button-base.mat-badge 102.5x36.0 bg #ffffff r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 102.453pxx36px bg #000000 r 9999px opacity 0.12 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Crops: `menu-trigger-default.png`, `menu-trigger-hover.png`, `menu-trigger-focus-visible.png`, `menu-trigger-pressed.png`, `menu-trigger-light.png`, `menu-trigger-light-hover.png`, `menu-trigger-light-focus-visible.png`, `menu-trigger-light-pressed.png`.

#### checkbox

Checkbox (source row, checked).

Page copy: `notebook-dark`, `notebook-dark-share-dialog`. Finder: `() => Q('mat-checkbox.select-checkbox')`.

Dark theme.

| Property | default | hover | focus-visible | notify-checked |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | 30 x 30 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #c7c7c7 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | - |
| Placeholder | "" #ffffff, opacity 1, 13.3333px | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) | at rest, captured notify-checked |
| Painted layers | - | span.mdc-checkbox__ripple 32.0x32.0 bg #e6e6e6 r 50% opacity 0.08 | input.mdc-checkbox__native-control.mdc-checkbox--selected 32.0x32.0 outline 1px auto #99c8ff offset 2px opacity 0; span.mdc-checkbox__ripple 32.0x32.0 bg #e6e6e6 r 50% opacity 0.12; span.mat-ripple.mat-mdc-checkbox-ripple.mat-focus-indicator::before 32pxx32px border T:3px solid #c3cafc / R:3px solid #c3cafc / B:3px solid #c3cafc / L:3px solid #c3cafc r 50% | = |

Light theme.

| Property | light | light-hover | light-focus-visible | light-notify-checked |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | 30 x 30 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #303030 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | - |
| Placeholder | "" #000000, opacity 1, 13.3333px | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) | at rest, captured notify-checked |
| Painted layers | - | span.mdc-checkbox__ripple 32.0x32.0 bg #000000 r 50% opacity 0.08 | input.mdc-checkbox__native-control.mdc-checkbox--selected 32.0x32.0 outline 1px auto #005fcc offset 2px opacity 0; span.mdc-checkbox__ripple 32.0x32.0 bg #000000 r 50% opacity 0.12; span.mat-ripple.mat-mdc-checkbox-ripple.mat-focus-indicator::before 32pxx32px border T:3px solid #4259ff / R:3px solid #4259ff / B:3px solid #4259ff / L:3px solid #4259ff r 50% | = |

Other finders: notify-checked: `() => Q('[role=dialog] mat-checkbox')`; light-notify-checked: `() => Q('[role=dialog] mat-checkbox')`.

Crops: `checkbox-default.png`, `checkbox-hover.png`, `checkbox-focus-visible.png`, `checkbox-notify-checked.png`, `checkbox-light.png`, `checkbox-light-hover.png`, `checkbox-light-focus-visible.png`, `checkbox-light-notify-checked.png`.

#### radio

Radio group drawn as toggle chips (Configure Chat). mat-button-toggle-group with role radiogroup; each chip is a role=radio button. The checked chip gains a leading check.

Page copy: `notebook-dark-configure-chat`. Finder: `() => Q('[role=dialog] mat-button-toggle:not(.mat-button-toggle-checked) button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed | selected | group |
|---|---|---|---|---|---|---|
| Size (w x h) | 126.61 x 40 | = | = | = | 102.89 x 40 | 816 x 50 |
| Padding | 0px | = | = | = | 0px 0px 0px 30px | = |
| Border | none | = | = | = | = | = |
| Radius | 0px | = | = | = | = | 24px |
| Background | transparent | = | = | = | = | = |
| Box shadow | none | = | = | = | = | = |
| Outline | none | = | = | = | = | = |
| Font | Google Sans Flex 15px/20px 370 | = | = | = | = | Google Sans Flex 14px/24px 400 |
| Letter spacing | normal | = | = | = | = | = |
| Colour | #e6e6e6 | = | = | = | #ffffff | #c7c7c7 |
| Text node | span.mat-button-toggle-label-content: Google Sans Flex 15px/40px 370, #e6e6e6 | = | = | = | span.mat-button-toggle-label-content: Google Sans Flex 15px/40px 370, #ffffff | span.mat-button-toggle-label-content: Google Sans Flex 15px/40px 370, #ffffff |
| Transition | padding 0.15s cubic-bezier(0.4, 0, 0.2, 1) delay 0.045s | = | = | = | = | none |
| Cursor | pointer | = | = | = | = | - |
| Painted layers | mat-pseudo-checkbox.mat-pseudo-checkbox.mat-pseudo-checkbox-checked.mat-pseudo-checkbox-minimal::after 14pxx6px border B:2px solid #ffffff / L:2px solid #ffffff | = | button.mat-button-toggle-button.mat-focus-indicator::before 126.609pxx40px border T:3px solid #c3cafc / R:3px solid #c3cafc / B:3px solid #c3cafc / L:3px solid #c3cafc r 4px; mat-pseudo-checkbox.mat-pseudo-checkbox.mat-pseudo-checkbox-checked.mat-pseudo-checkbox-minimal::after 14pxx6px border B:2px solid #ffffff / L:2px solid #ffffff | = | = | mat-button-toggle.mat-button-toggle.mat-button-toggle-checked.mat-button-toggle-appearance-standard 104.9x42.0 bg #4259ff border T:1px solid #37383b / R:1px solid #37383b / B:1px solid #37383b / L:1px solid #37383b r 24px; mat-pseudo-checkbox.mat-pseudo-checkbox.mat-pseudo-checkbox-checked.mat-pseudo-checkbox-minimal::after 14pxx6px border B:2px solid #ffffff / L:2px solid #ffffff; span.mat-button-toggle-focus-overlay 102.9x40.0 bg #e6e6e6 r 24px opacity 0; mat-button-toggle.mat-button-toggle.mat-button-toggle-appearance-standard.mat-button-toggle-animations-enabled 128.6x42.0 border T:1px solid #37383b / R:1px solid #37383b / B:1px solid #37383b / L:1px solid #37383b r 24px; mat-pseudo-checkbox.mat-pseudo-checkbox.mat-pseudo-checkbox-checked.mat-pseudo-checkbox-minimal::after 14pxx6px border B:2px solid #ffffff / L:2px solid #ffffff; span.mat-button-toggle-focus-overlay 126.6x40.0 bg #e6e6e6 r 24px opacity 0 |
| How | at rest | mouse hover | keyboard: Shift keydown, then focus() | mouse hover, then held down | at rest, captured selected | at rest, captured group |
| ::before | - | = | 126.609px x 40px, absolute, bg #000000 @ 0, radius 4px | = | = | = |
| Ancestor paint | - | = | = | = | 1 up mat-button-toggle.mat-button-toggle.mat-button-toggle-checked.mat-button-toggle-appearance-standard bg #4259ff | = |
| Transform | - | = | = | = | = | matrix(1, 0, 0, 1, 0, 0) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed | light-selected | light-group |
|---|---|---|---|---|---|---|
| Size (w x h) | 126.61 x 40 | = | = | = | 102.89 x 40 | 816 x 50 |
| Padding | 0px | = | = | = | 0px 0px 0px 30px | = |
| Border | none | = | = | = | = | = |
| Radius | 0px | = | = | = | = | 24px |
| Background | transparent | = | = | = | = | = |
| Box shadow | none | = | = | = | = | = |
| Outline | none | = | = | = | = | = |
| Font | Google Sans Flex 15px/20px 370 | = | = | = | = | Google Sans Flex 14px/24px 400 |
| Letter spacing | normal | = | = | = | = | = |
| Colour | #000000 | = | = | = | #ffffff | #303030 |
| Text node | span.mat-button-toggle-label-content: Google Sans Flex 15px/40px 370, #000000 | = | = | = | span.mat-button-toggle-label-content: Google Sans Flex 15px/40px 370, #ffffff | span.mat-button-toggle-label-content: Google Sans Flex 15px/40px 370, #ffffff |
| Transition | padding 0.15s cubic-bezier(0.4, 0, 0.2, 1) delay 0.045s | = | = | = | = | none |
| Cursor | pointer | = | = | = | = | - |
| Painted layers | mat-pseudo-checkbox.mat-pseudo-checkbox.mat-pseudo-checkbox-checked.mat-pseudo-checkbox-minimal::after 14pxx6px border B:2px solid #ffffff / L:2px solid #ffffff | = | button.mat-button-toggle-button.mat-focus-indicator::before 126.609pxx40px border T:3px solid #4259ff / R:3px solid #4259ff / B:3px solid #4259ff / L:3px solid #4259ff r 4px; mat-pseudo-checkbox.mat-pseudo-checkbox.mat-pseudo-checkbox-checked.mat-pseudo-checkbox-minimal::after 14pxx6px border B:2px solid #ffffff / L:2px solid #ffffff | = | = | mat-button-toggle.mat-button-toggle.mat-button-toggle-checked.mat-button-toggle-appearance-standard 104.9x42.0 bg #4259ff border T:1px solid #dde1eb / R:1px solid #dde1eb / B:1px solid #dde1eb / L:1px solid #dde1eb r 24px; mat-pseudo-checkbox.mat-pseudo-checkbox.mat-pseudo-checkbox-checked.mat-pseudo-checkbox-minimal::after 14pxx6px border B:2px solid #ffffff / L:2px solid #ffffff; span.mat-button-toggle-focus-overlay 102.9x40.0 bg #000000 r 24px opacity 0; mat-button-toggle.mat-button-toggle.mat-button-toggle-appearance-standard.mat-button-toggle-animations-enabled 128.6x42.0 border T:1px solid #dde1eb / R:1px solid #dde1eb / B:1px solid #dde1eb / L:1px solid #dde1eb r 24px; mat-pseudo-checkbox.mat-pseudo-checkbox.mat-pseudo-checkbox-checked.mat-pseudo-checkbox-minimal::after 14pxx6px border B:2px solid #ffffff / L:2px solid #ffffff; span.mat-button-toggle-focus-overlay 126.6x40.0 bg #000000 r 24px opacity 0 |
| How | at rest | mouse hover | keyboard: Shift keydown, then focus() | mouse hover, then held down | at rest, captured selected | at rest, captured group |
| ::before | - | = | 126.609px x 40px, absolute, bg #000000 @ 0, radius 4px | = | = | = |
| Ancestor paint | - | = | = | = | 1 up mat-button-toggle.mat-button-toggle.mat-button-toggle-checked.mat-button-toggle-appearance-standard bg #4259ff | = |
| Transform | - | = | = | = | = | matrix(1, 0, 0, 1, 0, 0) |

Other finders: selected: `() => Q('[role=dialog] mat-button-toggle.mat-button-toggle-checked button')`; group: `() => Q('[role=dialog] mat-button-toggle-group')`; light-selected: `() => Q('[role=dialog] mat-button-toggle.mat-button-toggle-checked button')`; light-group: `() => Q('[role=dialog] mat-button-toggle-group')`.

Crops: `radio-default.png`, `radio-hover.png`, `radio-focus-visible.png`, `radio-pressed.png`, `radio-selected.png`, `radio-group.png`, `radio-light.png`, `radio-light-hover.png`, `radio-light-focus-visible.png`, `radio-light-pressed.png`, `radio-light-selected.png`, `radio-light-group.png`.

#### switch

Switch (Web notifications, off and disabled). Disabled because the browser blocks notifications; no enabled switch appeared.

Page copy: `home-dark-notifications-dialog`. Finder: `() => Q('[role=dialog] button[role=switch]')`.

Dark theme.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 52 x 32 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Arial 13.3333px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff @ 0.3 | = |
| Transition | none | = |
| Cursor | default | = |
| Icon | 16 x 16, colour #ffffff @ 0.3, fill #444746 | = |
| Painted layers | span.mdc-switch__track::before 52pxx32px bg #444746 border T:2px solid #e6e6e6 / R:2px solid #e6e6e6 / B:2px solid #e6e6e6 / L:2px solid #e6e6e6 r 9999px; span.mdc-switch__track::after 52pxx32px bg #e6e6e6 border T:2px solid #e6e6e6 / R:2px solid #e6e6e6 / B:2px solid #e6e6e6 / L:2px solid #e6e6e6 r 9999px opacity 0; span.mdc-switch__handle::before 24pxx24px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; span.mdc-switch__handle::after 24pxx24px bg #e6e6e6 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px opacity 0.38 | = |
| How | at rest | mouse hover |

Light theme.

| Property | light | light-hover |
|---|---|---|
| Size (w x h) | 52 x 32 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Arial 13.3333px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #101010 @ 0.3 | = |
| Transition | none | = |
| Cursor | default | = |
| Icon | 16 x 16, colour #101010 @ 0.3, fill #e1e3e1 | = |
| Painted layers | span.mdc-switch__track::before 52pxx32px bg #e1e3e1 border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 9999px; span.mdc-switch__track::after 52pxx32px bg #000000 border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 9999px opacity 0; span.mdc-switch__handle::before 24pxx24px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; span.mdc-switch__handle::after 24pxx24px bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px opacity 0.38 | = |
| How | at rest | mouse hover |

Crops: `switch-default.png`, `switch-hover.png`, `switch-light.png`, `switch-light-hover.png`.

#### progress

Progress bar (source limit).

Page copy: `notebook-dark-add-sources`. Finder: `() => Q('[role=dialog] mat-progress-bar')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 600.45 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | transparent |
| Box shadow | none |
| Outline | 1px solid #000000 @ 0 offset 0px |
| Font | Google Sans Flex 15px/20px 400 |
| Letter spacing | normal |
| Colour | #e6e6e6 |
| Transition | opacity 0.25s cubic-bezier(0.4, 0, 0.6, 1) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Painted layers | mat-progress-bar.mat-mdc-progress-bar.mdc-linear-progress.progress-bar 600.5x16.0 r 16px outline 1px solid #000000 @ 0 offset 0px; div.mdc-linear-progress__buffer-bar 600.5x16.0 bg #a3a3a3 @ 0.2; span.mdc-linear-progress__bar-inner 36.0x16.0 border T:16px solid #e6e6e6 |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 600.45 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | transparent |
| Box shadow | none |
| Outline | 1px solid #000000 @ 0 offset 0px |
| Font | Google Sans Flex 15px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | opacity 0.25s cubic-bezier(0.4, 0, 0.6, 1) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Painted layers | mat-progress-bar.mat-mdc-progress-bar.mdc-linear-progress.progress-bar 600.5x16.0 r 16px outline 1px solid #000000 @ 0 offset 0px; div.mdc-linear-progress__buffer-bar 600.5x16.0 bg #a3a3a3 @ 0.2; span.mdc-linear-progress__bar-inner 36.0x16.0 border T:16px solid #000000 |
| How | at rest |

Crops: `progress-default.png`, `progress-light.png`.

### Navigation

#### tab

Header tab (All, My notebooks, Discover, Collections). nb-buttons: the selected one is tonal, the rest text.

Page copy: `home-dark`. Finder: `() => Q('nb-button.nb-button-type-text-primary button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed | selected |
|---|---|---|---|---|---|
| Size (w x h) | 44 x 36 | = | = | = | 109.89 x 36 |
| Padding | 0px 12px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | transparent | = | = | = | #171717 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 3px solid #e6e6e6 offset 2px | = | = |
| Font | Google Sans Flex 15px/normal 370 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #e6e6e6 | = | = | = | = |
| Text node | span: Google Sans Flex 13px/17px 400, #e6e6e6 | = | = | = | = |
| Transition | none | = | = | = | box-shadow 0.28s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | default | pointer | = | pointer | = |
| Painted layers | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 44pxx36px bg #e6e6e6 r 9999px opacity 0 | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 44pxx36px bg #e6e6e6 r 9999px opacity 0.08 | button.mdc-button.mat-mdc-button-base.mat-badge 44.0x36.0 r 9999px outline 3px solid #e6e6e6 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 44pxx36px bg #e6e6e6 r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #e6e6e6 / R:3px solid #e6e6e6 / B:3px solid #e6e6e6 / L:3px solid #e6e6e6 r 9999px | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 44pxx36px bg #e6e6e6 r 9999px opacity 0.12 | button.mdc-button.mat-mdc-button-base.mat-badge 109.9x36.0 bg #171717 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 109.891pxx36px bg #e6e6e6 r 9999px opacity 0 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down | at rest, captured selected |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed | light-selected |
|---|---|---|---|---|---|
| Size (w x h) | 44 x 36 | = | = | = | 109.89 x 36 |
| Padding | 0px 12px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | transparent | = | = | = | #f2f0f0 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 3px solid #000000 offset 2px | = | = |
| Font | Google Sans Flex 15px/normal 370 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Text node | span: Google Sans Flex 13px/17px 400, #000000 | = | = | = | = |
| Transition | none | = | = | = | box-shadow 0.28s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | default | pointer | = | pointer | = |
| Painted layers | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 44pxx36px bg #000000 r 9999px opacity 0 | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 44pxx36px bg #000000 r 9999px opacity 0.08 | button.mdc-button.mat-mdc-button-base.mat-badge 44.0x36.0 r 9999px outline 3px solid #000000 offset 2px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 44pxx36px bg #000000 r 9999px opacity 0; span.mat-focus-indicator::before autoxauto border T:3px solid #000000 / R:3px solid #000000 / B:3px solid #000000 / L:3px solid #000000 r 9999px | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 44pxx36px bg #000000 r 9999px opacity 0.12 | button.mdc-button.mat-mdc-button-base.mat-badge 109.9x36.0 bg #f2f0f0 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 109.891pxx36px bg #000000 r 9999px opacity 0 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down | at rest, captured selected |

Other finders: selected: `() => Q('nb-button.nb-button-type-tonal button')`; light-selected: `() => Q('nb-button.nb-button-type-tonal button')`.

Crops: `tab-default.png`, `tab-hover.png`, `tab-focus-visible.png`, `tab-pressed.png`, `tab-selected.png`, `tab-light.png`, `tab-light-hover.png`, `tab-light-focus-visible.png`, `tab-light-pressed.png`, `tab-light-selected.png`.

#### segmented

Segmented control (Grid view, List view).

Page copy: `home-dark`. Finder: `() => Q('button.nb-segmented-button-action[aria-label="List view"]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed | selected | group |
|---|---|---|---|---|---|---|
| Size (w x h) | 36 x 32 | = | = | = | = | 76 x 36 |
| Padding | 1px 8px | = | = | = | = | 2px |
| Border | none | = | = | = | = | = |
| Radius | 9999px | = | = | = | = | = |
| Background | transparent | = | = | = | = | #171717 |
| Box shadow | none | = | = | = | = | = |
| Outline | none | = | 1px auto #99c8ff offset 0px | = | = | = |
| Font | Google Sans Flex 15px/20px 400 | = | = | = | = | Times 16px/normal 400 |
| Letter spacing | normal | = | = | = | = | = |
| Colour | #ffffff @ 0.55 | = | = | = | #e6e6e6 | #c7c7c7 |
| Text node | mat-icon.mat-icon.notranslate.google-symbols: Google Symbols 20px/20px 400, #ffffff @ 0.55 | = | = | = | mat-icon.mat-icon.notranslate.google-symbols: Google Symbols 20px/20px 400, #e6e6e6 | mat-icon.mat-icon.notranslate.google-symbols: Google Symbols 20px/20px 400, #e6e6e6 |
| Transition | color 0.2s ease | = | = | = | = | none |
| Cursor | pointer | = | = | = | = | - |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down | at rest, captured selected | at rest, captured group |
| Painted layers | - | = | button.nb-segmented-button-action 36.0x32.0 r 9999px outline 1px auto #99c8ff offset 0px | = | = | nb-segmented-button-row.nb-segmented-button-row.is-initialized 76.0x36.0 bg #171717 r 9999px; div.nb-segmented-button-row-slider 36.0x32.0 bg #1f1f1f r 9999px shadow #000000 @ 0.28 0px 0px 20px 0px |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed | light-selected | light-group |
|---|---|---|---|---|---|---|
| Size (w x h) | 36 x 32 | = | = | = | = | 76 x 36 |
| Padding | 1px 8px | = | = | = | = | 2px |
| Border | none | = | = | = | = | = |
| Radius | 9999px | = | = | = | = | = |
| Background | transparent | = | = | = | = | #f2f0f0 |
| Box shadow | none | = | = | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = | = | = |
| Font | Google Sans Flex 15px/20px 400 | = | = | = | = | Times 16px/normal 400 |
| Letter spacing | normal | = | = | = | = | = |
| Colour | #000000 @ 0.55 | = | = | = | #000000 | #303030 |
| Text node | mat-icon.mat-icon.notranslate.google-symbols: Google Symbols 20px/20px 400, #000000 @ 0.55 | = | = | = | mat-icon.mat-icon.notranslate.google-symbols: Google Symbols 20px/20px 400, #000000 | mat-icon.mat-icon.notranslate.google-symbols: Google Symbols 20px/20px 400, #000000 |
| Transition | color 0.2s ease | = | = | = | = | none |
| Cursor | pointer | = | = | = | = | - |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down | at rest, captured selected | at rest, captured group |
| Painted layers | - | = | button.nb-segmented-button-action 36.0x32.0 r 9999px outline 1px auto #005fcc offset 0px | = | = | nb-segmented-button-row.nb-segmented-button-row.is-initialized 76.0x36.0 bg #f2f0f0 r 9999px; div.nb-segmented-button-row-slider 36.0x32.0 bg #ffffff r 9999px shadow #000000 @ 0.04 0px 0px 20px 0px |

Other finders: selected: `() => Q('button.nb-segmented-button-action[aria-label="Grid view"]')`; light-selected: `() => Q('button.nb-segmented-button-action[aria-label="Grid view"]')`; group: `() => Q('nb-segmented-button-row')`; light-group: `() => Q('nb-segmented-button-row')`.

Crops: `segmented-default.png`, `segmented-hover.png`, `segmented-focus-visible.png`, `segmented-pressed.png`, `segmented-selected.png`, `segmented-group.png`, `segmented-light.png`, `segmented-light-hover.png`, `segmented-light-focus-visible.png`, `segmented-light-pressed.png`, `segmented-light-selected.png`, `segmented-light-group.png`.

#### mobile-tab

Panel tab at 390 (Sources, Chat, Studio).

Page copy: `mobile-notebook-dark-chat`. Finder: `() => Q('button.tab-button:not(.tab-button--active)')`.

Dark theme.

| Property | default | focus-visible | pressed | selected | bar |
|---|---|---|---|---|---|
| Size (w x h) | 118 x 28 | = | = | = | 358 x 32 |
| Padding | 0px | = | = | = | 2px |
| Border | none | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | transparent | = | = | = | #171717 |
| Box shadow | none | = | = | = | = |
| Outline | none | 1px auto #99c8ff offset 0px | = | = | = |
| Font | Google Sans Flex 14px/20px 500 | = | = | = | Times 16px/normal 400 |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff @ 0.55 | = | #e6e6e6 | #e6e6e6 | #c7c7c7 |
| Text node | span: Google Sans Flex 14px/20px 500, #ffffff @ 0.55 | = | span: Google Sans Flex 14px/20px 500, #e6e6e6 | span: Google Sans Flex 14px/20px 500, #e6e6e6 | = |
| Transition | color 0.2s ease | = | = | = | none |
| Cursor | pointer | = | = | = | - |
| Ancestor paint | 1 up div.tabs-slider-container bg #171717 | = | = | = | - |
| How | at rest | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down | at rest, captured selected | at rest, captured bar |
| Painted layers | - | button.tab-button 118.0x28.0 r 9999px outline 1px auto #99c8ff offset 0px | = | = | div.tabs-slider-container 358.0x32.0 bg #171717 r 9999px; div.tabs-slider.tabs-slider--chat 118.0x28.0 bg #1f1f1f r 9999px shadow #000000 @ 0.1 0px 1px 3px 0px |

Light theme.

| Property | light | light-focus-visible | light-pressed | light-selected | light-bar |
|---|---|---|---|---|---|
| Size (w x h) | 118 x 28 | = | = | = | 358 x 32 |
| Padding | 0px | = | = | = | 2px |
| Border | none | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | transparent | = | = | = | #f2f0f0 |
| Box shadow | none | = | = | = | = |
| Outline | none | 1px auto #005fcc offset 0px | = | = | = |
| Font | Google Sans Flex 14px/20px 500 | = | = | = | Times 16px/normal 400 |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 @ 0.55 | = | #000000 | #000000 | #303030 |
| Text node | span: Google Sans Flex 14px/20px 500, #000000 @ 0.55 | = | span: Google Sans Flex 14px/20px 500, #000000 | span: Google Sans Flex 14px/20px 500, #000000 | = |
| Transition | color 0.2s ease | = | = | = | none |
| Cursor | pointer | = | = | = | - |
| Ancestor paint | 1 up div.tabs-slider-container bg #f2f0f0 | = | = | = | - |
| How | at rest | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down | at rest, captured selected | at rest, captured bar |
| Painted layers | - | button.tab-button 118.0x28.0 r 9999px outline 1px auto #005fcc offset 0px | = | = | div.tabs-slider-container 358.0x32.0 bg #f2f0f0 r 9999px; div.tabs-slider.tabs-slider--chat 118.0x28.0 bg #ffffff r 9999px shadow #000000 @ 0.1 0px 1px 3px 0px |

Other finders: selected: `() => Q('button.tab-button--active')`; bar: `() => P(Q('button.tab-button'))`; light-selected: `() => Q('button.tab-button--active')`; light-bar: `() => P(Q('button.tab-button'))`.

Crops: `mobile-tab-default.png`, `mobile-tab-focus-visible.png`, `mobile-tab-pressed.png`, `mobile-tab-selected.png`, `mobile-tab-bar.png`, `mobile-tab-light.png`, `mobile-tab-light-focus-visible.png`, `mobile-tab-light-pressed.png`, `mobile-tab-light-selected.png`, `mobile-tab-light-bar.png`.

### Overlays

#### menu

Menu (notebook card actions).

Page copy: `home-dark-card-menu`. Finder: `() => Q('.mat-mdc-menu-panel')`.

Dark theme.

| Property | default | item | item-hover | item-focus-visible | item-pressed |
|---|---|---|---|---|---|
| Size (w x h) | 206 x 160 | 190 x 36 | 190 x 36 | 190 x 36 | 190 x 36 |
| Padding | 0px | 8px | 8px | 8px | 8px |
| Border | none | = | = | = | = |
| Radius | 20px | 12px | 12px | 12px | 12px |
| Background | #1f1f1f | transparent | #e6e6e6 @ 0.08 | transparent | #e6e6e6 @ 0.08 |
| Box shadow | #000000 @ 0.28 0px 0px 20px 0px | none | none | none | none |
| Outline | none | = | = | = | = |
| Font | Times 16px/normal 400 | Arial 17px/normal 400 | Arial 17px/normal 400 | Arial 17px/normal 400 | Arial 17px/normal 400 |
| Letter spacing | normal | = | = | = | = |
| Colour | #c7c7c7 | #e6e6e6 | #e6e6e6 | #e6e6e6 | #e6e6e6 |
| Text node | mat-icon.mat-icon.notranslate.google-symbols: Luminous Symbols 20px/20px 400, #e6e6e6 | mat-icon.mat-icon.notranslate.google-symbols: Google Symbols 20px/20px 400, #e6e6e6 | mat-icon.mat-icon.notranslate.google-symbols: Google Symbols 20px/20px 400, #e6e6e6 | mat-icon.mat-icon.notranslate.google-symbols: Google Symbols 20px/20px 400, #e6e6e6 | mat-icon.mat-icon.notranslate.google-symbols: Google Symbols 20px/20px 400, #e6e6e6 |
| Transition | none | = | = | = | = |
| Painted layers | div.mat-mdc-menu-panel.mat-menu-after.mat-menu-below 206.0x160.0 bg #1f1f1f r 20px shadow #000000 @ 0.28 0px 0px 20px 0px; button.mat-mdc-menu-item.mat-focus-indicator.project-button-hamburger-menu-action 190.0x36.0 bg #e6e6e6 @ 0.08 r 12px | - | button.mat-mdc-menu-item.mat-focus-indicator.project-button-hamburger-menu-action 190.0x36.0 bg #e6e6e6 @ 0.08 r 12px | button.mat-mdc-menu-item.mat-focus-indicator.project-button-hamburger-menu-action::before 190pxx36px border T:3px solid #c3cafc / R:3px solid #c3cafc / B:3px solid #c3cafc / L:3px solid #c3cafc r 4px | button.mat-mdc-menu-item.mat-focus-indicator.project-button-hamburger-menu-action 190.0x36.0 bg #e6e6e6 @ 0.08 r 12px |
| How | at rest | at rest, captured item | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |
| Gap | - | 8px | 8px | 8px | 8px |
| Cursor | - | pointer | pointer | pointer | pointer |
| Ancestor paint | - | 3 up div.mat-mdc-menu-panel.mat-menu-after.mat-menu-below bg #1f1f1f shadow #000000 @ 0.28 0px 0px 20px 0px | 3 up div.mat-mdc-menu-panel.mat-menu-after.mat-menu-below bg #1f1f1f shadow #000000 @ 0.28 0px 0px 20px 0px | 3 up div.mat-mdc-menu-panel.mat-menu-after.mat-menu-below bg #1f1f1f shadow #000000 @ 0.28 0px 0px 20px 0px | 3 up div.mat-mdc-menu-panel.mat-menu-after.mat-menu-below bg #1f1f1f shadow #000000 @ 0.28 0px 0px 20px 0px |
| ::before | - | = | = | 190px x 36px, absolute, bg #000000 @ 0, radius 4px | = |

Light theme.

| Property | light | light-item | light-item-hover | light-item-focus-visible | light-item-pressed |
|---|---|---|---|---|---|
| Size (w x h) | 206 x 160 | 190 x 36 | 190 x 36 | 190 x 36 | 190 x 36 |
| Padding | 0px | 8px | 8px | 8px | 8px |
| Border | none | = | = | = | = |
| Radius | 20px | 12px | 12px | 12px | 12px |
| Background | #ffffff | transparent | #000000 @ 0.08 | transparent | #000000 @ 0.08 |
| Box shadow | #000000 @ 0.04 0px 0px 20px 0px | none | none | none | none |
| Outline | none | = | = | = | = |
| Font | Times 16px/normal 400 | Arial 17px/normal 400 | Arial 17px/normal 400 | Arial 17px/normal 400 | Arial 17px/normal 400 |
| Letter spacing | normal | = | = | = | = |
| Colour | #303030 | #000000 | #000000 | #000000 | #000000 |
| Text node | mat-icon.mat-icon.notranslate.google-symbols: Luminous Symbols 20px/20px 400, #000000 | mat-icon.mat-icon.notranslate.google-symbols: Google Symbols 20px/20px 400, #000000 | mat-icon.mat-icon.notranslate.google-symbols: Google Symbols 20px/20px 400, #000000 | mat-icon.mat-icon.notranslate.google-symbols: Google Symbols 20px/20px 400, #000000 | mat-icon.mat-icon.notranslate.google-symbols: Google Symbols 20px/20px 400, #000000 |
| Transition | none | = | = | = | = |
| Painted layers | div.mat-mdc-menu-panel.mat-menu-after.mat-menu-below 206.0x160.0 bg #ffffff r 20px shadow #000000 @ 0.04 0px 0px 20px 0px; button.mat-mdc-menu-item.mat-focus-indicator.project-button-hamburger-menu-action 190.0x36.0 bg #000000 @ 0.08 r 12px | - | button.mat-mdc-menu-item.mat-focus-indicator.project-button-hamburger-menu-action 190.0x36.0 bg #000000 @ 0.08 r 12px | button.mat-mdc-menu-item.mat-focus-indicator.project-button-hamburger-menu-action::before 190pxx36px border T:3px solid #4259ff / R:3px solid #4259ff / B:3px solid #4259ff / L:3px solid #4259ff r 4px | button.mat-mdc-menu-item.mat-focus-indicator.project-button-hamburger-menu-action 190.0x36.0 bg #000000 @ 0.08 r 12px |
| How | at rest | at rest, captured item | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |
| Gap | - | 8px | 8px | 8px | 8px |
| Cursor | - | pointer | pointer | pointer | pointer |
| Ancestor paint | - | 3 up div.mat-mdc-menu-panel.mat-menu-after.mat-menu-below bg #ffffff shadow #000000 @ 0.04 0px 0px 20px 0px | 3 up div.mat-mdc-menu-panel.mat-menu-after.mat-menu-below bg #ffffff shadow #000000 @ 0.04 0px 0px 20px 0px | 3 up div.mat-mdc-menu-panel.mat-menu-after.mat-menu-below bg #ffffff shadow #000000 @ 0.04 0px 0px 20px 0px | 3 up div.mat-mdc-menu-panel.mat-menu-after.mat-menu-below bg #ffffff shadow #000000 @ 0.04 0px 0px 20px 0px |
| ::before | - | = | = | 190px x 36px, absolute, bg #000000 @ 0, radius 4px | = |

Other finders: item: `() => Q('.mat-mdc-menu-panel [role=menuitem]', 1)`; light-item: `() => Q('.mat-mdc-menu-panel [role=menuitem]', 1)`; item-hover: `() => Q('.mat-mdc-menu-panel [role=menuitem]', 1)`; light-item-hover: `() => Q('.mat-mdc-menu-panel [role=menuitem]', 1)`; item-focus-visible: `() => Q('.mat-mdc-menu-panel [role=menuitem]', 1)`; light-item-focus-visible: `() => Q('.mat-mdc-menu-panel [role=menuitem]', 1)`; item-pressed: `() => Q('.mat-mdc-menu-panel [role=menuitem]', 1)`; light-item-pressed: `() => Q('.mat-mdc-menu-panel [role=menuitem]', 1)`.

Crops: `menu-default.png`, `menu-item.png`, `menu-item-hover.png`, `menu-item-focus-visible.png`, `menu-item-pressed.png`, `menu-light.png`, `menu-light-item.png`, `menu-light-item-hover.png`, `menu-light-item-focus-visible.png`, `menu-light-item-pressed.png`.

#### menu-settings

Menu (Settings) and its Theme submenu.

Page copy: `home-dark-settings-menu`, `home-dark-theme-submenu`. Finder: `() => Q('.mat-mdc-menu-panel')`.

Dark theme.

| Property | default | submenu |
|---|---|---|
| Size (w x h) | 210.69 x 393 | 128.53 x 124 |
| Padding | 0px | = |
| Border | none | = |
| Radius | 20px | = |
| Background | #1f1f1f | = |
| Box shadow | #000000 @ 0.28 0px 0px 20px 0px | = |
| Outline | none | = |
| Font | Times 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #c7c7c7 | = |
| Text node | mat-icon.mat-icon.notranslate.google-symbols: Luminous Symbols 20px/20px 400, #e6e6e6 | mat-icon.mat-icon.notranslate.google-symbols: Google Symbols 20px/20px 400, #e6e6e6 |
| Transition | none | = |
| Icon | 36 x 10, colour #e6e6e6 | - |
| Painted layers | div.mat-mdc-menu-panel.mat-menu-below.mat-menu-before 210.7x393.0 bg #1f1f1f r 20px shadow #000000 @ 0.28 0px 0px 20px 0px; button.mat-mdc-menu-item.mat-focus-indicator.cdk-focused 194.7x36.0 bg #e6e6e6 @ 0.08 r 12px; mat-divider.mat-divider.mat-divider-horizontal 194.7x1.0 border T:1px solid #444746 | div.mat-mdc-menu-panel.mat-menu-after.mat-menu-below 128.5x124.0 bg #1f1f1f r 20px shadow #000000 @ 0.28 0px 0px 20px 0px; button.mat-mdc-menu-item.mat-focus-indicator.cdk-focused 112.5x36.0 bg #e6e6e6 @ 0.08 r 12px |
| How | at rest | at rest, captured submenu |

Light theme.

| Property | light | light-submenu |
|---|---|---|
| Size (w x h) | 210.69 x 393 | 128.53 x 124 |
| Padding | 0px | = |
| Border | none | = |
| Radius | 20px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0.04 0px 0px 20px 0px | = |
| Outline | none | = |
| Font | Times 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #303030 | = |
| Text node | mat-icon.mat-icon.notranslate.google-symbols: Luminous Symbols 20px/20px 400, #000000 | mat-icon.mat-icon.notranslate.google-symbols: Google Symbols 20px/20px 400, #000000 |
| Transition | none | = |
| Icon | 36 x 10, colour #000000 | - |
| Painted layers | div.mat-mdc-menu-panel.mat-menu-below.mat-menu-before 210.7x393.0 bg #ffffff r 20px shadow #000000 @ 0.04 0px 0px 20px 0px; button.mat-mdc-menu-item.mat-focus-indicator.cdk-focused 194.7x36.0 bg #000000 @ 0.08 r 12px; mat-divider.mat-divider.mat-divider-horizontal 194.7x1.0 border T:1px solid #e1e3e1 | div.mat-mdc-menu-panel.mat-menu-after.mat-menu-below 128.5x124.0 bg #ffffff r 20px shadow #000000 @ 0.04 0px 0px 20px 0px; button.mat-mdc-menu-item.mat-focus-indicator.cdk-focused 112.5x36.0 bg #000000 @ 0.08 r 12px |
| How | at rest | at rest, captured submenu |

Other finders: submenu: `() => [...document.querySelectorAll('.mat-mdc-menu-panel')].pop()`; light-submenu: `() => [...document.querySelectorAll('.mat-mdc-menu-panel')].pop()`.

Crops: `menu-settings-default.png`, `menu-settings-submenu.png`, `menu-settings-light.png`, `menu-settings-light-submenu.png`.

#### tooltip

Tooltip. Its text was scrubbed, since tooltips repeat titles; the live one read "Audio Overview - Generate an AI podcast based on your sources".

Page copy: `notebook-dark-tooltip`. Finder: `() => Q('.mat-mdc-tooltip-surface')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 111.39 x 33 |
| Padding | 8px 16px |
| Border | none |
| Radius | 12px |
| Background | #e6e6e6 |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 13px/17px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Transition | none |
| ::before | 111.391px x 33px, absolute, bg #000000 @ 0, radius 12px |
| Painted layers | div.mat-mdc-tooltip-surface.mdc-tooltip__surface 111.4x33.0 bg #e6e6e6 r 12px; div.mat-mdc-tooltip-surface.mdc-tooltip__surface::before 111.391pxx33px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 111.39 x 33 |
| Padding | 8px 16px |
| Border | none |
| Radius | 12px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 13px/17px 400 |
| Letter spacing | normal |
| Colour | #f2f0f0 |
| Transition | none |
| ::before | 111.391px x 33px, absolute, bg #000000 @ 0, radius 12px |
| Painted layers | div.mat-mdc-tooltip-surface.mdc-tooltip__surface 111.4x33.0 bg #000000 r 12px; div.mat-mdc-tooltip-surface.mdc-tooltip__surface::before 111.391pxx33px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px |
| How | at rest |

Crops: `tooltip-default.png`, `tooltip-light.png`.

#### dialog

Dialog (Delete this notebook?).

Page copy: `home-dark-delete-confirm`. Finder: `() => Q('.mat-mdc-dialog-surface')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 456 x 224 |
| Padding | 0px |
| Border | none |
| Radius | 28px |
| Background | #0f0f0f |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #c7c7c7 |
| Text node | h2.header-title.mat-title-medium: Google Sans Flex 20px/24px 470, #e6e6e6 |
| Transition | transform 0.15s cubic-bezier(0, 0, 0.2, 1) |
| ::before | 456px x 224px, absolute, bg #000000 @ 0, radius 28px |
| Painted layers | div.mat-mdc-dialog-surface.mdc-dialog__surface 456.0x224.0 bg #0f0f0f r 28px; div.mat-mdc-dialog-surface.mdc-dialog__surface::before 456pxx224px border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 28px; div.dialog-container 456.0x224.0 bg #1f1f1f r 28px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 78.7344pxx48px bg #e6e6e6 r 9999px opacity 0; button.mdc-button.mat-mdc-button-base.mat-badge 76.3x48.0 bg #171717 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 76.3438pxx48px bg #e6e6e6 r 9999px opacity 0 |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 456 x 224 |
| Padding | 0px |
| Border | none |
| Radius | 28px |
| Background | #faf9f9 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #303030 |
| Text node | h2.header-title.mat-title-medium: Google Sans Flex 20px/24px 470, #000000 |
| Transition | transform 0.15s cubic-bezier(0, 0, 0.2, 1) |
| ::before | 456px x 224px, absolute, bg #000000 @ 0, radius 28px |
| Painted layers | div.mat-mdc-dialog-surface.mdc-dialog__surface 456.0x224.0 bg #faf9f9 r 28px; div.mat-mdc-dialog-surface.mdc-dialog__surface::before 456pxx224px border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 28px; div.dialog-container 456.0x224.0 bg #ffffff r 28px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 78.7344pxx48px bg #000000 r 9999px opacity 0; button.mdc-button.mat-mdc-button-base.mat-badge 76.3x48.0 bg #f2f0f0 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 76.3438pxx48px bg #000000 r 9999px opacity 0 |
| How | at rest |

Crops: `dialog-default.png`, `dialog-light.png`.

#### dialog-large

Dialog, large (Configure Chat).

Page copy: `notebook-dark-configure-chat`. Finder: `() => Q('.mat-mdc-dialog-surface')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 864 x 482 |
| Padding | 0px |
| Border | none |
| Radius | 28px |
| Background | #0f0f0f |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #c7c7c7 |
| Text node | div.header-title.mat-title-large: Google Sans Flex 22px/36px 400, #f2f2f2 |
| Transition | transform 0.15s cubic-bezier(0, 0, 0.2, 1) |
| ::before | 864px x 482px, absolute, bg #000000 @ 0, radius 28px |
| Painted layers | div.mat-mdc-dialog-surface.mdc-dialog__surface 864.0x482.0 bg #0f0f0f r 28px; div.mat-mdc-dialog-surface.mdc-dialog__surface::before 864pxx482px border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 28px; div.header 864.0x69.0 border B:1px solid #37383b; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 40pxx40px bg #e6e6e6 r 9999px opacity 0.12; mat-button-toggle.mat-button-toggle.mat-button-toggle-checked.mat-button-toggle-appearance-standard 104.9x42.0 bg #4259ff border T:1px solid #37383b / R:1px solid #37383b / B:1px solid #37383b / L:1px solid #37383b r 24px; mat-pseudo-checkbox.mat-pseudo-checkbox.mat-pseudo-checkbox-checked.mat-pseudo-checkbox-minimal::after 14pxx6px border B:2px solid #ffffff / L:2px solid #ffffff |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 864 x 482 |
| Padding | 0px |
| Border | none |
| Radius | 28px |
| Background | #faf9f9 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #303030 |
| Text node | div.header-title.mat-title-large: Google Sans Flex 22px/36px 400, #1b1b1c |
| Transition | transform 0.15s cubic-bezier(0, 0, 0.2, 1) |
| ::before | 864px x 482px, absolute, bg #000000 @ 0, radius 28px |
| Painted layers | div.mat-mdc-dialog-surface.mdc-dialog__surface 864.0x482.0 bg #faf9f9 r 28px; div.mat-mdc-dialog-surface.mdc-dialog__surface::before 864pxx482px border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 28px; div.header 864.0x69.0 border B:1px solid #dde1eb; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 40pxx40px bg #000000 r 9999px opacity 0.12; mat-button-toggle.mat-button-toggle.mat-button-toggle-checked.mat-button-toggle-appearance-standard 104.9x42.0 bg #4259ff border T:1px solid #dde1eb / R:1px solid #dde1eb / B:1px solid #dde1eb / L:1px solid #dde1eb r 24px; mat-pseudo-checkbox.mat-pseudo-checkbox.mat-pseudo-checkbox-checked.mat-pseudo-checkbox-minimal::after 14pxx6px border B:2px solid #ffffff / L:2px solid #ffffff |
| How | at rest |

Crops: none.

#### dialog-announcement

Announcement dialog (what is new).

Page copy: `notebook-dark-announcement`. Finder: `() => Q('.mat-mdc-dialog-surface')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 1000 x 542.59 |
| Padding | 0px |
| Border | none |
| Radius | 28px |
| Background | #0f0f0f |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #c7c7c7 |
| Text node | mat-icon.mat-icon.notranslate.google-symbols: Luminous Symbols 24px/24px 400, #e6e6e6 |
| Transition | transform 0.15s cubic-bezier(0, 0, 0.2, 1) |
| ::before | 1000px x 542.594px, absolute, bg #000000 @ 0, radius 28px |
| Painted layers | div.mat-mdc-dialog-surface.mdc-dialog__surface 1000.0x542.6 bg #0f0f0f r 28px; div.mat-mdc-dialog-surface.mdc-dialog__surface::before 1000pxx542.594px border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 28px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 40pxx40px bg #e6e6e6 r 9999px opacity 0.12; div.header-text 952.0x74.6 border B:1px solid #37383b |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 1000 x 542.59 |
| Padding | 0px |
| Border | none |
| Radius | 28px |
| Background | #faf9f9 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #303030 |
| Text node | mat-icon.mat-icon.notranslate.google-symbols: Luminous Symbols 24px/24px 400, #000000 |
| Transition | transform 0.15s cubic-bezier(0, 0, 0.2, 1) |
| ::before | 1000px x 542.594px, absolute, bg #000000 @ 0, radius 28px |
| Painted layers | div.mat-mdc-dialog-surface.mdc-dialog__surface 1000.0x542.6 bg #faf9f9 r 28px; div.mat-mdc-dialog-surface.mdc-dialog__surface::before 1000pxx542.594px border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 28px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 40pxx40px bg #000000 r 9999px opacity 0.12; div.header-text 952.0x74.6 border B:1px solid #dde1eb |
| How | at rest |

Crops: none.

#### scrim

Dialog scrim.

Page copy: `home-dark-delete-confirm`. Finder: `() => Q('.cdk-overlay-dark-backdrop')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 @ 0.32 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #c7c7c7 |
| Transition | opacity 0.4s cubic-bezier(0.25, 0.8, 0.25, 1) |
| Painted layers | div.cdk-overlay-backdrop.cdk-overlay-dark-backdrop.cdk-overlay-backdrop-showing 1440.0x900.0 bg #000000 @ 0.32 |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 @ 0.32 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #303030 |
| Transition | opacity 0.4s cubic-bezier(0.25, 0.8, 0.25, 1) |
| Painted layers | div.cdk-overlay-backdrop.cdk-overlay-dark-backdrop.cdk-overlay-backdrop-showing 1440.0x900.0 bg #000000 @ 0.32 |
| How | at rest |

Crops: none.

#### toast

Toast (Failed to copy.). The clipboard is blocked in the capture browser, so the copy action reported a failure.

Page copy: `notebook-dark-toast`. Finder: `() => Q('mat-snack-bar-container .mdc-snackbar__surface') // Q('mat-snack-bar-container')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 344 x 48 |
| Padding | 0px 8px 0px 0px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.2 0px 3px 5px -1px, #000000 @ 0.14 0px 6px 10px 0px, #000000 @ 0.12 0px 1px 18px 0px |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #303030 |
| Text node | div.mat-mdc-snack-bar-label.mdc-snackbar__label: Google Sans Flex 15px/20px 400, #303030 |
| Transition | none |
| Painted layers | div.mdc-snackbar__surface.mat-mdc-snackbar-surface 344.0x48.0 bg #ffffff r 16px shadow #000000 @ 0.2 0px 3px 5px -1px, #000000 @ 0.14 0px 6px 10px 0px, #000000 @ 0.12 0px 1px 18px 0px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 344 x 48 |
| Padding | 0px 8px 0px 0px |
| Border | none |
| Radius | 16px |
| Background | #000000 |
| Box shadow | #000000 @ 0.2 0px 3px 5px -1px, #000000 @ 0.14 0px 6px 10px 0px, #000000 @ 0.12 0px 1px 18px 0px |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #f2f2f2 |
| Text node | div.mat-mdc-snack-bar-label.mdc-snackbar__label: Google Sans Flex 15px/20px 400, #f2f2f2 |
| Transition | none |
| Painted layers | div.mdc-snackbar__surface.mat-mdc-snackbar-surface 344.0x48.0 bg #000000 r 16px shadow #000000 @ 0.2 0px 3px 5px -1px, #000000 @ 0.14 0px 6px 10px 0px, #000000 @ 0.12 0px 1px 18px 0px |
| How | at rest |

Crops: `toast-default.png`, `toast-light.png`.

### Lists

#### card

Notebook card.

Page copy: `home-dark`. Finder: `() => Q('project-button mat-card')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 272 x 185 | = | = | = |
| Padding | 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | #171717 | transparent | = | transparent |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #c7c7c7 | = | = | = |
| Text node | div.project-button-box-icon: Times 36px/36px 400, #c7c7c7 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 272px x 185px, absolute, bg #000000 @ 0, radius 40px | = | = | = |
| Painted layers | mat-card.mat-mdc-card.mdc-card.project-button-card 272.0x185.0 bg #171717 r 40px; mat-card.mat-mdc-card.mdc-card.project-button-card::after 272pxx185px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 40px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 28pxx28px bg #ababab r 9999px opacity 0 | mat-card.mat-mdc-card.mdc-card.project-button-card 272.0x185.0 image linear-gradient(0deg, #ffffff @ 0.12, #ffffff @ 0.12), linear-gradient(0deg, #171717, #171 r 40px; mat-card.mat-mdc-card.mdc-card.project-button-card::after 272pxx185px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 40px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 28pxx28px bg #ababab r 9999px opacity 0 | mat-card.mat-mdc-card.mdc-card.project-button-card 272.0x185.0 bg #171717 r 40px; mat-card.mat-mdc-card.mdc-card.project-button-card::after 272pxx185px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 40px; a.mat-ripple.mat-mdc-tooltip-trigger.primary-action-button 272.0x185.0 r 40px outline 1px auto #99c8ff offset 1px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 28pxx28px bg #ababab r 9999px opacity 0 | mat-card.mat-mdc-card.mdc-card.project-button-card 272.0x185.0 image linear-gradient(0deg, #ffffff @ 0.12, #ffffff @ 0.12), linear-gradient(0deg, #171717, #171 r 40px; mat-card.mat-mdc-card.mdc-card.project-button-card::after 272pxx185px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 40px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 28pxx28px bg #ababab r 9999px opacity 0 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) | mouse hover, then held down |
| Background image | - | linear-gradient(0deg, #ffffff @ 0.12, #ffffff @ 0.12), linear-gradient(0deg, #171717, #171717) | = | linear-gradient(0deg, #ffffff @ 0.12, #ffffff @ 0.12), linear-gradient(0deg, #171717, #171717) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 272 x 185 | = | = | = |
| Padding | 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | #f2f0f0 | transparent | = | transparent |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #303030 | = | = | = |
| Text node | div.project-button-box-icon: Times 36px/36px 400, #303030 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 272px x 185px, absolute, bg #000000 @ 0, radius 40px | = | = | = |
| Painted layers | mat-card.mat-mdc-card.mdc-card.project-button-card 272.0x185.0 bg #f2f0f0 r 40px; mat-card.mat-mdc-card.mdc-card.project-button-card::after 272pxx185px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 40px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 28pxx28px bg #5e5e5e r 9999px opacity 0 | mat-card.mat-mdc-card.mdc-card.project-button-card 272.0x185.0 image linear-gradient(0deg, #000000 @ 0.08, #000000 @ 0.08), linear-gradient(0deg, #f2f0f0, #f2f r 40px; mat-card.mat-mdc-card.mdc-card.project-button-card::after 272pxx185px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 40px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 28pxx28px bg #5e5e5e r 9999px opacity 0 | mat-card.mat-mdc-card.mdc-card.project-button-card 272.0x185.0 bg #f2f0f0 r 40px; mat-card.mat-mdc-card.mdc-card.project-button-card::after 272pxx185px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 40px; a.mat-ripple.mat-mdc-tooltip-trigger.primary-action-button 272.0x185.0 r 40px outline 1px auto #005fcc offset 1px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 28pxx28px bg #5e5e5e r 9999px opacity 0 | mat-card.mat-mdc-card.mdc-card.project-button-card 272.0x185.0 image linear-gradient(0deg, #000000 @ 0.08, #000000 @ 0.08), linear-gradient(0deg, #f2f0f0, #f2f r 40px; mat-card.mat-mdc-card.mdc-card.project-button-card::after 272pxx185px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 40px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 28pxx28px bg #5e5e5e r 9999px opacity 0 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) | mouse hover, then held down |
| Background image | - | linear-gradient(0deg, #000000 @ 0.08, #000000 @ 0.08), linear-gradient(0deg, #f2f0f0, #f2f0f0) | = | linear-gradient(0deg, #000000 @ 0.08, #000000 @ 0.08), linear-gradient(0deg, #f2f0f0, #f2f0f0) |

Crops: `card-default.png`, `card-hover.png`, `card-focus-visible.png`, `card-pressed.png`, `card-light.png`, `card-light-hover.png`, `card-light-focus-visible.png`, `card-light-pressed.png`.

#### studio-tile

Studio tile (Audio Overview).

Page copy: `notebook-dark`. Finder: `() => Q('[aria-label="Audio Overview"]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 164 x 48 | 161.54 x 47.28 | = | 159.08 x 46.56 |
| Padding | 4px 12px 4px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 1px inset | = | = | = |
| Outline | none | = | 2px solid #e6e6e6 offset 2px | = |
| Font | Google Sans Flex 12px/16px 500 | = | = | = |
| Letter spacing | 0.096px | = | = | = |
| Colour | #c7c7c7 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.artifact-icon: Luminous Symbols 24px/24px 400, #76a0ff | = | = | = |
| Transition | transform, -webkit-transform 0.2s, 0.2s cubic-bezier(0.05, 0.7, 0.1, 1), cubic-bezier(0.05, 0.7, 0.1, 1) delay 0s, 0s | = | = | transform, -webkit-transform 0.1s, 0.1s cubic-bezier(0.3, 0, 0.8, 0.15), cubic-bezier(0.3, 0, 0.8, 0.15) delay 0s, 0s |
| Transform | matrix(1, 0, 0, 1, 0, 0) | matrix(0.985, 0, 0, 0.985, 0, 0) | = | matrix(0.97, 0, 0, 0.97, 0, 0) |
| Cursor | pointer | = | = | = |
| ::before | 328px x 328px, absolute, bg #000000 @ 0 conic-gradient(#2e64de 34%, #3c8fe3 37%, #7e8fe6 39%, #987be9 41%, #987be9 48%, #7e8fe6 50%, #3c8fe3 52%, #3c8fe3 56, radius 50% | = | = | = |
| ::after | 164px x 48px, absolute, bg #171717, radius 20px, shadow #000000 @ 0 0px 0px 0px 1px inset | = | = | = |
| Painted layers | div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container 164.0x48.0 r 20px shadow #000000 @ 0 0px 0px 0px 1px inset; div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container::before 328pxx328px image conic-gradient(#2e64de 34%, #3c8fe3 37%, #7e8fe6 39%, #987be9 41%, #987be9 48%, #7e8fe6 50 r 50% opacity 0; div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container::after 164pxx48px bg #171717 r 20px shadow #000000 @ 0 0px 0px 0px 1px inset | div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container 161.5x47.3 r 20px shadow #000000 @ 0 0px 0px 0px 1px inset; div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container::before 328pxx328px image conic-gradient(#2e64de 34%, #3c8fe3 37%, #7e8fe6 39%, #987be9 41%, #987be9 48%, #7e8fe6 50 r 50% opacity 0; div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container::after 164pxx48px bg #171717 r 20px shadow #000000 @ 0 0px 0px 0px 1px inset | div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container 164.0x48.0 r 20px shadow #000000 @ 0 0px 0px 0px 1px inset outline 2px solid #e6e6e6 offset 2px; div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container::before 328pxx328px image conic-gradient(#2e64de 34%, #3c8fe3 37%, #7e8fe6 39%, #987be9 41%, #987be9 48%, #7e8fe6 50 r 50% opacity 0; div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container::after 164pxx48px bg #171717 r 20px shadow #000000 @ 0 0px 0px 0px 1px inset | div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container 159.1x46.6 r 20px shadow #000000 @ 0 0px 0px 0px 1px inset; div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container::before 328pxx328px image conic-gradient(#2e64de 34%, #3c8fe3 37%, #7e8fe6 39%, #987be9 41%, #987be9 48%, #7e8fe6 50 r 50% opacity 0; div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container::after 164pxx48px bg #171717 r 20px shadow #000000 @ 0 0px 0px 0px 1px inset |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 164 x 48 | 161.54 x 47.28 | = | 159.08 x 46.56 |
| Padding | 4px 12px 4px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #000000 @ 0.08 0px 0px 0px 1px inset | = | = | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | Google Sans Flex 12px/16px 500 | = | = | = |
| Letter spacing | 0.096px | = | = | = |
| Colour | #303030 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.artifact-icon: Luminous Symbols 24px/24px 400, #2e64de | = | = | = |
| Transition | transform, -webkit-transform 0.2s, 0.2s cubic-bezier(0.05, 0.7, 0.1, 1), cubic-bezier(0.05, 0.7, 0.1, 1) delay 0s, 0s | = | = | transform, -webkit-transform 0.1s, 0.1s cubic-bezier(0.3, 0, 0.8, 0.15), cubic-bezier(0.3, 0, 0.8, 0.15) delay 0s, 0s |
| Transform | matrix(1, 0, 0, 1, 0, 0) | matrix(0.985, 0, 0, 0.985, 0, 0) | = | matrix(0.97, 0, 0, 0.97, 0, 0) |
| Cursor | pointer | = | = | = |
| ::before | 328px x 328px, absolute, bg #000000 @ 0 conic-gradient(#2e64de 34%, #3c8fe3 37%, #7e8fe6 39%, #987be9 41%, #987be9 48%, #7e8fe6 50%, #3c8fe3 52%, #3c8fe3 56, radius 50% | = | = | = |
| ::after | 164px x 48px, absolute, bg #ffffff, radius 20px, shadow #000000 @ 0.08 0px 0px 0px 1px inset | = | = | = |
| Painted layers | div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container 164.0x48.0 r 20px shadow #000000 @ 0.08 0px 0px 0px 1px inset; div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container::before 328pxx328px image conic-gradient(#2e64de 34%, #3c8fe3 37%, #7e8fe6 39%, #987be9 41%, #987be9 48%, #7e8fe6 50 r 50% opacity 0; div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container::after 164pxx48px bg #ffffff r 20px shadow #000000 @ 0.08 0px 0px 0px 1px inset | div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container 161.5x47.3 r 20px shadow #000000 @ 0.08 0px 0px 0px 1px inset; div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container::before 328pxx328px image conic-gradient(#2e64de 34%, #3c8fe3 37%, #7e8fe6 39%, #987be9 41%, #987be9 48%, #7e8fe6 50 r 50% opacity 0; div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container::after 164pxx48px bg #ffffff r 20px shadow #000000 @ 0.08 0px 0px 0px 1px inset | div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container 164.0x48.0 r 20px shadow #000000 @ 0.08 0px 0px 0px 1px inset outline 2px solid #000000 offset 2px; div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container::before 328pxx328px image conic-gradient(#2e64de 34%, #3c8fe3 37%, #7e8fe6 39%, #987be9 41%, #987be9 48%, #7e8fe6 50 r 50% opacity 0; div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container::after 164pxx48px bg #ffffff r 20px shadow #000000 @ 0.08 0px 0px 0px 1px inset | div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container 159.1x46.6 r 20px shadow #000000 @ 0.08 0px 0px 0px 1px inset; div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container::before 328pxx328px image conic-gradient(#2e64de 34%, #3c8fe3 37%, #7e8fe6 39%, #987be9 41%, #987be9 48%, #7e8fe6 50 r 50% opacity 0; div.mat-mdc-tooltip-trigger.blue.create-artifact-button-container::after 164pxx48px bg #ffffff r 20px shadow #000000 @ 0.08 0px 0px 0px 1px inset |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Crops: `studio-tile-default.png`, `studio-tile-hover.png`, `studio-tile-focus-visible.png`, `studio-tile-pressed.png`, `studio-tile-light.png`, `studio-tile-light-hover.png`, `studio-tile-light-focus-visible.png`, `studio-tile-light-pressed.png`.

#### list-row

List row (source).

Page copy: `notebook-dark`. Finder: `() => C(Q('button.source-stretched-button'), '.single-source-container') // Q('button.source-stretched-button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 336 x 36 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #171717 | = | #171717 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #c7c7c7 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.source-item-source-icon: Luminous Symbols 24px/24px 400, #db372d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Placeholder | "" #ffffff, opacity 1, 13.3333px | = | = | = |
| Painted layers | span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 14pxx32px bg #e6e6e6 r 9999px opacity 0 | div.single-source-container.single-source-container-magic-index-only.source-sorting-enabled 336.0x36.0 bg #171717 r 8px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #e6e6e6 r 9999px opacity 0 | button.source-stretched-button 336.0x36.0 r 8px outline 1px auto #99c8ff offset 0px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 14pxx32px bg #e6e6e6 r 9999px opacity 0 | div.single-source-container.single-source-container-magic-index-only.source-sorting-enabled 336.0x36.0 bg #171717 r 8px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #e6e6e6 r 9999px opacity 0 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) | mouse hover, then held down |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 336 x 36 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f2f0f0 | = | #f2f0f0 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #303030 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.source-item-source-icon: Luminous Symbols 24px/24px 400, #db372d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Placeholder | "" #000000, opacity 1, 13.3333px | = | = | = |
| Painted layers | span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 14pxx32px bg #000000 r 9999px opacity 0 | div.single-source-container.single-source-container-magic-index-only.source-sorting-enabled 336.0x36.0 bg #f2f0f0 r 8px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #000000 r 9999px opacity 0 | button.source-stretched-button 336.0x36.0 r 8px outline 1px auto #005fcc offset 0px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 14pxx32px bg #000000 r 9999px opacity 0 | div.single-source-container.single-source-container-magic-index-only.source-sorting-enabled 336.0x36.0 bg #f2f0f0 r 8px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #000000 r 9999px opacity 0 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) | mouse hover, then held down |

Crops: `list-row-default.png`, `list-row-hover.png`, `list-row-focus-visible.png`, `list-row-pressed.png`, `list-row-light.png`, `list-row-light-hover.png`, `list-row-light-focus-visible.png`, `list-row-light-pressed.png`.

#### list-row-output

List row (Studio output).

Page copy: `notebook-dark`. Finder: `() => Q('.artifact-item-button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 336 x 60 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #c7c7c7 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.artifact-icon: Luminous Symbols 24px/24px 400, #3fdda0 | = | = | = |
| Transition | none | = | = | = |
| Painted layers | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 336pxx60px bg #e6e6e6 r 20px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #e6e6e6 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #e6e6e6 r 9999px opacity 0 | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 336pxx60px bg #e6e6e6 r 20px opacity 0.08; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #e6e6e6 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #e6e6e6 r 9999px opacity 0 | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 336pxx60px bg #e6e6e6 r 20px opacity 0; span.mat-focus-indicator::before 336pxx60px border T:3px solid #c3cafc / R:3px solid #c3cafc / B:3px solid #c3cafc / L:3px solid #c3cafc r 20px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #e6e6e6 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #e6e6e6 r 9999px opacity 0 | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 336pxx60px bg #e6e6e6 r 20px opacity 0.12; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #e6e6e6 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #e6e6e6 r 9999px opacity 0 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) | mouse hover, then held down |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 336 x 60 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #303030 | = | = | = |
| Text node | mat-icon.mat-icon.notranslate.artifact-icon: Luminous Symbols 24px/24px 400, #0aac6e | = | = | = |
| Transition | none | = | = | = |
| Painted layers | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 336pxx60px bg #000000 r 20px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #000000 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #000000 r 9999px opacity 0 | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 336pxx60px bg #000000 r 20px opacity 0.08; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #000000 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #000000 r 9999px opacity 0 | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 336pxx60px bg #000000 r 20px opacity 0; span.mat-focus-indicator::before 336pxx60px border T:3px solid #4259ff / R:3px solid #4259ff / B:3px solid #4259ff / L:3px solid #4259ff r 20px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #000000 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #000000 r 9999px opacity 0 | span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 336pxx60px bg #000000 r 20px opacity 0.12; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #000000 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 32pxx32px bg #000000 r 9999px opacity 0 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) | mouse hover, then held down |

Crops: `list-row-output-default.png`, `list-row-output-hover.png`, `list-row-output-focus-visible.png`, `list-row-output-pressed.png`, `list-row-output-light.png`, `list-row-output-light-hover.png`, `list-row-output-light-focus-visible.png`, `list-row-output-light-pressed.png`.

#### chat-bubble

User chat bubble.

Page copy: `notebook-dark`. Finder: `() => P(Q('.from-user-message-inner-content')) // Q('.from-user-message-inner-content')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 162.05 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 40px |
| Background | #171717 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #e6e6e6 |
| Text node | p: Google Sans Flex 16px/24px 400, #c7c7c7 |
| Transition | none |
| ::after | 162.047px x 64px, absolute, bg #000000 @ 0, radius 12px |
| Painted layers | mat-card.mat-mdc-card.mdc-card.from-user-message-card-content 162.0x64.0 bg #171717 r 40px; mat-card.mat-mdc-card.mdc-card.from-user-message-card-content::after 162.047pxx64px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 162.05 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 40px |
| Background | #f2f0f0 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p: Google Sans Flex 16px/24px 400, #303030 |
| Transition | none |
| ::after | 162.047px x 64px, absolute, bg #000000 @ 0, radius 12px |
| Painted layers | mat-card.mat-mdc-card.mdc-card.from-user-message-card-content 162.0x64.0 bg #f2f0f0 r 40px; mat-card.mat-mdc-card.mdc-card.from-user-message-card-content::after 162.047pxx64px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px |
| How | at rest |

Crops: `chat-bubble-default.png`, `chat-bubble-light.png`.

#### citation

Citation marker.

Page copy: `notebook-dark`. Finder: `() => Q('button.citation-marker')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 22 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 50% | = | = | = |
| Background | #171717 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #99c8ff offset 0px | = |
| Font | Google Sans Flex 11.008px/16px 500 | = | = | = |
| Letter spacing | 0.096px | = | = | = |
| Colour | #ababab | = | = | = |
| Text node | span: Google Sans Flex 11.008px/16px 500, #ababab, ls 0.096px | = | = | = |
| Transition | opacity 0.2s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.xap-inline-dialog.citation-marker.chat-bidi-enabled 22.0x22.0 bg #171717 r 50% | button.xap-inline-dialog.citation-marker.chat-bidi-enabled 22.0x22.0 bg #171717 r 50% opacity 0.5 | button.xap-inline-dialog.citation-marker.chat-bidi-enabled 22.0x22.0 bg #171717 r 50% outline 1px auto #99c8ff offset 0px | button.xap-inline-dialog.citation-marker.chat-bidi-enabled 22.0x22.0 bg #171717 r 50% opacity 0.5 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |
| Opacity | - | 0.5 | = | 0.5 |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 22 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 50% | = | = | = |
| Background | #f2f0f0 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Google Sans Flex 11.008px/16px 500 | = | = | = |
| Letter spacing | 0.096px | = | = | = |
| Colour | #5e5e5e | = | = | = |
| Text node | span: Google Sans Flex 11.008px/16px 500, #5e5e5e, ls 0.096px | = | = | = |
| Transition | opacity 0.2s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.xap-inline-dialog.citation-marker.chat-bidi-enabled 22.0x22.0 bg #f2f0f0 r 50% | button.xap-inline-dialog.citation-marker.chat-bidi-enabled 22.0x22.0 bg #f2f0f0 r 50% opacity 0.5 | button.xap-inline-dialog.citation-marker.chat-bidi-enabled 22.0x22.0 bg #f2f0f0 r 50% outline 1px auto #005fcc offset 0px | button.xap-inline-dialog.citation-marker.chat-bidi-enabled 22.0x22.0 bg #f2f0f0 r 50% opacity 0.5 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |
| Opacity | - | 0.5 | = | 0.5 |

Crops: `citation-default.png`, `citation-hover.png`, `citation-focus-visible.png`, `citation-pressed.png`, `citation-light.png`, `citation-light-hover.png`, `citation-light-focus-visible.png`, `citation-light-pressed.png`.

### Tables

#### table-row

Table row (notebook list view).

Page copy: `home-dark-list`. Finder: `() => Q('tbody tr.mat-mdc-row')`.

Dark theme.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1392 x 52 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Google Sans Flex 15px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #e6e6e6 | = |
| Text node | span.project-table-emoji: Google Sans Flex 16px/20px 400, #e6e6e6 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | td.mat-mdc-cell.mdc-data-table__cell.cdk-cell 464.3x52.0 border B:1px solid #404144; td.mat-mdc-cell.mdc-data-table__cell.cdk-cell 263.9x52.0 border B:1px solid #404144; td.mat-mdc-cell.mdc-data-table__cell.cdk-cell 264.0x52.0 border B:1px solid #404144; td.mat-mdc-cell.mdc-data-table__cell.cdk-cell 68.6x52.0 border B:1px solid #404144; td.mat-mdc-cell.mdc-data-table__cell.cdk-cell 263.3x52.0 border B:1px solid #404144; td.mat-mdc-cell.mdc-data-table__cell.cdk-cell 68.0x52.0 border B:1px solid #404144 | = |
| How | at rest | mouse hover |

Light theme.

| Property | light | light-hover |
|---|---|---|
| Size (w x h) | 1392 x 52 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Google Sans Flex 15px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.project-table-emoji: Google Sans Flex 16px/20px 400, #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | td.mat-mdc-cell.mdc-data-table__cell.cdk-cell 464.3x52.0 border B:1px solid #c4c7c5; td.mat-mdc-cell.mdc-data-table__cell.cdk-cell 263.9x52.0 border B:1px solid #c4c7c5; td.mat-mdc-cell.mdc-data-table__cell.cdk-cell 264.0x52.0 border B:1px solid #c4c7c5; td.mat-mdc-cell.mdc-data-table__cell.cdk-cell 68.6x52.0 border B:1px solid #c4c7c5; td.mat-mdc-cell.mdc-data-table__cell.cdk-cell 263.3x52.0 border B:1px solid #c4c7c5; td.mat-mdc-cell.mdc-data-table__cell.cdk-cell 68.0x52.0 border B:1px solid #c4c7c5 | = |
| How | at rest | mouse hover |

Crops: `table-row-default.png`, `table-row-hover.png`, `table-row-light.png`, `table-row-light-hover.png`.

#### table-header

Table header row.

Page copy: `home-dark-list`. Finder: `() => Q('thead tr')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 15px/20px 370 |
| Letter spacing | normal |
| Colour | #e6e6e6 |
| Text node | th.mat-mdc-header-cell.mdc-data-table__header-cell.cdk-header-cell: Google Sans Flex 15px/20px 370, #e6e6e6 |
| Transition | none |
| Painted layers | th.mat-mdc-header-cell.mdc-data-table__header-cell.cdk-header-cell 464.3x56.0 border B:1px solid #404144; th.mat-mdc-header-cell.mdc-data-table__header-cell.cdk-header-cell 263.9x56.0 border B:1px solid #404144; th.mat-mdc-header-cell.mdc-data-table__header-cell.cdk-header-cell 264.0x56.0 border B:1px solid #404144; th.mat-mdc-header-cell.mdc-data-table__header-cell.cdk-header-cell 68.6x56.0 border B:1px solid #404144; th.mat-mdc-header-cell.mdc-data-table__header-cell.cdk-header-cell 263.3x56.0 border B:1px solid #404144; th.mat-mdc-header-cell.mdc-data-table__header-cell.cdk-header-cell 68.0x56.0 border B:1px solid #404144 |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 1392 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 15px/20px 370 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | th.mat-mdc-header-cell.mdc-data-table__header-cell.cdk-header-cell: Google Sans Flex 15px/20px 370, #000000 |
| Transition | none |
| Painted layers | th.mat-mdc-header-cell.mdc-data-table__header-cell.cdk-header-cell 464.3x56.0 border B:1px solid #c4c7c5; th.mat-mdc-header-cell.mdc-data-table__header-cell.cdk-header-cell 263.9x56.0 border B:1px solid #c4c7c5; th.mat-mdc-header-cell.mdc-data-table__header-cell.cdk-header-cell 264.0x56.0 border B:1px solid #c4c7c5; th.mat-mdc-header-cell.mdc-data-table__header-cell.cdk-header-cell 68.6x56.0 border B:1px solid #c4c7c5; th.mat-mdc-header-cell.mdc-data-table__header-cell.cdk-header-cell 263.3x56.0 border B:1px solid #c4c7c5; th.mat-mdc-header-cell.mdc-data-table__header-cell.cdk-header-cell 68.0x56.0 border B:1px solid #c4c7c5 |
| How | at rest |

Crops: `table-header-default.png`, `table-header-light.png`.

#### mobile-list-row

Notebook row at 390.

Page copy: `mobile-home-dark`. Finder: `() => Q('tbody tr.mat-mdc-row')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 342 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 15px/20px 400 |
| Letter spacing | normal |
| Colour | #e6e6e6 |
| Text node | span.project-table-emoji: Google Sans Flex 16px/20px 400, #e6e6e6 |
| Transition | none |
| Cursor | pointer |
| Painted layers | td.mat-mdc-cell.mdc-data-table__cell.cdk-cell 273.6x52.0 border B:1px solid #404144; td.mat-mdc-cell.mdc-data-table__cell.cdk-cell 68.4x52.0 border B:1px solid #404144; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #ababab r 9999px opacity 0 |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 342 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 15px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.project-table-emoji: Google Sans Flex 16px/20px 400, #000000 |
| Transition | none |
| Cursor | pointer |
| Painted layers | td.mat-mdc-cell.mdc-data-table__cell.cdk-cell 273.6x52.0 border B:1px solid #c4c7c5; td.mat-mdc-cell.mdc-data-table__cell.cdk-cell 68.4x52.0 border B:1px solid #c4c7c5; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #5e5e5e r 9999px opacity 0 |
| How | at rest |

Crops: `mobile-list-row-default.png`, `mobile-list-row-light.png`.

### Display

#### avatar

Avatar (account, 32px). The photo was replaced by a grey disc with an L in the copy; size and shape are the product's, the fill is not.

Page copy: `home-dark`. Finder: `() => Q('a[aria-label^="Google Account"]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 40 x 40 |
| Padding | 4px |
| Border | none |
| Radius | 50% |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Text 13px/27px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.gb_0.gbii: Google Sans Text 12px/27px 600, #ffffff |
| Transition | none |
| Cursor | pointer |
| ::before | 40px x 40px, absolute, bg #c4c7c5, radius 100px |
| ::after | 48px x 48px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | a.gb_C.gb_bb.gb_aa::before 40pxx40px bg #c4c7c5 r 100px opacity 0; span.gb_me::after 30pxx30px border T:1px solid #202124 / R:1px solid #202124 / B:1px solid #202124 / L:1px solid #202124 r 50% opacity 0.13; div.gb_0.gbii 32.0x32.0 bg #8a8a8a r 9999px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 40 x 40 |
| Padding | 4px |
| Border | none |
| Radius | 50% |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Text 13px/27px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.gb_0.gbii: Google Sans Text 12px/27px 600, #ffffff |
| Transition | none |
| Cursor | pointer |
| ::before | 40px x 40px, absolute, bg #c4c7c5, radius 100px |
| ::after | 48px x 48px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | a.gb_C.gb_bb.gb_aa::before 40pxx40px bg #c4c7c5 r 100px opacity 0; span.gb_me::after 30pxx30px border T:1px solid #202124 / R:1px solid #202124 / B:1px solid #202124 / L:1px solid #202124 r 50% opacity 0.13; div.gb_0.gbii 32.0x32.0 bg #8a8a8a r 9999px |
| How | at rest |

Crops: none.

#### badge-pro

Badge (PRO).

Page copy: `home-dark`. Finder: `() => Q('.pro-badge')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 40.3 x 24 |
| Padding | 0px 8px |
| Border | none |
| Radius | 8px |
| Background | #ffffff @ 0.12 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #c7c7c7 |
| Text node | span.mat-label-medium.pro-label: Google Sans Flex 11px/16px 500, #ffffff @ 0.55, ls 0.096px |
| Transition | none |
| Painted layers | div.pro-badge 40.3x24.0 bg #ffffff @ 0.12 r 8px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 40.3 x 24 |
| Padding | 0px 8px |
| Border | none |
| Radius | 8px |
| Background | #000000 @ 0.08 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #303030 |
| Text node | span.mat-label-medium.pro-label: Google Sans Flex 11px/16px 500, #000000 @ 0.55, ls 0.096px |
| Transition | none |
| Painted layers | div.pro-badge 40.3x24.0 bg #000000 @ 0.08 r 8px |
| How | at rest |

Crops: `badge-pro-default.png`, `badge-pro-light.png`.

#### badge-new

Badge (New! on a Studio tile).

Page copy: `notebook-dark`. Finder: `() => P(T('New!'))`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 46.7 x 24 |
| Padding | 0px 8px |
| Border | none |
| Radius | 9999px |
| Background | #ffffff @ 0.12 |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 13px/24px 400 |
| Letter spacing | normal |
| Colour | #e6e6e6 |
| Transition | none |
| Painted layers | div.tile-tag.mat-label-small 46.7x24.0 bg #ffffff @ 0.12 r 9999px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 46.7 x 24 |
| Padding | 0px 8px |
| Border | none |
| Radius | 9999px |
| Background | #000000 @ 0.08 |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 13px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Painted layers | div.tile-tag.mat-label-small 46.7x24.0 bg #000000 @ 0.08 r 9999px |
| How | at rest |

Crops: `badge-new-default.png`, `badge-new-light.png`.

#### status-chip

Status chip (Blocked by browser).

Page copy: `home-dark-notifications-dialog`. Finder: `() => P(T('Blocked by browser')) // T('Blocked by browser')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 162.52 x 28 |
| Padding | 4px 12px |
| Gap | 6px |
| Border | none |
| Radius | 16px |
| Background | #ea4335 @ 0.15 |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 12px/20px 400 |
| Letter spacing | 0.096px |
| Colour | #f28b82 |
| Text node | mat-icon.mat-icon.notranslate.status-icon: Google Symbols 16px/16px 400, #f28b82 |
| Transition | none |
| Painted layers | div.status-pill.status-blocked 162.5x28.0 bg #ea4335 @ 0.15 r 16px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 162.52 x 28 |
| Padding | 4px 12px |
| Gap | 6px |
| Border | none |
| Radius | 16px |
| Background | #fce8e6 |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 12px/20px 400 |
| Letter spacing | 0.096px |
| Colour | #c5221f |
| Text node | mat-icon.mat-icon.notranslate.status-icon: Google Symbols 16px/16px 400, #c5221f |
| Transition | none |
| Painted layers | div.status-pill.status-blocked 162.5x28.0 bg #fce8e6 r 16px |
| How | at rest |

Crops: `status-chip-default.png`, `status-chip-light.png`.

#### banner

Inline banner (Studio, Try it).

Page copy: `notebook-dark`. Finder: `() => Q('.artifact-callout') // P(TS('New: You can now'))`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 336 x 60 |
| Padding | 12px |
| Gap | 8px |
| Border | none |
| Radius | 16px |
| Background | #1f1f1f |
| Background image | linear-gradient(268deg, #a9a8ff @ 0.15 0px, #3186ff @ 0.15 100%), none |
| Box shadow | #000000 @ 0.28 0px 0px 20px 0px |
| Outline | none |
| Font | Google Sans Flex 12px/16px 500 |
| Letter spacing | 0.096px |
| Colour | #e6e6e6 |
| Text node | span.banner-icon: Google Sans Flex 16px/16px 500, #e6e6e6, ls 0.096px |
| Transition | none |
| Painted layers | div.artifact-callout.mat-label-medium 336.0x60.0 bg #1f1f1f image linear-gradient(268deg, #a9a8ff @ 0.15 0px, #3186ff @ 0.15 100%), none r 16px shadow #000000 @ 0.28 0px 0px 20px 0px; button.mdc-button.mat-mdc-button-base.mat-badge 56.8x36.0 bg #171717 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 56.7969pxx36px bg #e6e6e6 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #e6e6e6 r 9999px opacity 0 |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 336 x 60 |
| Padding | 12px |
| Gap | 8px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Background image | linear-gradient(268deg, #a9a8ff @ 0.15 0px, #3186ff @ 0.15 100%), none |
| Box shadow | #000000 @ 0.04 0px 0px 20px 0px |
| Outline | none |
| Font | Google Sans Flex 12px/16px 500 |
| Letter spacing | 0.096px |
| Colour | #000000 |
| Text node | span.banner-icon: Google Sans Flex 16px/16px 500, #000000, ls 0.096px |
| Transition | none |
| Painted layers | div.artifact-callout.mat-label-medium 336.0x60.0 bg #ffffff image linear-gradient(268deg, #a9a8ff @ 0.15 0px, #3186ff @ 0.15 100%), none r 16px shadow #000000 @ 0.04 0px 0px 20px 0px; button.mdc-button.mat-mdc-button-base.mat-badge 56.8x36.0 bg #f2f0f0 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 56.7969pxx36px bg #000000 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #000000 r 9999px opacity 0 |
| How | at rest |

Crops: `banner-default.png`, `banner-light.png`.

#### skeleton

Loading skeleton row.

Page copy: `search-dark-loading`. Finder: `() => Q('.skeleton-row')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 4px |
| Background | transparent |
| Background image | linear-gradient(90deg, #3e4a59 25%, #d4d7db 37%, #3e4a59 63%) |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #c7c7c7 |
| Transition | none |
| Painted layers | div.skeleton-row 1392.0x56.0 image linear-gradient(90deg, #3e4a59 25%, #d4d7db 37%, #3e4a59 63%) r 4px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 1392 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 4px |
| Background | transparent |
| Background image | linear-gradient(90deg, #f2f2f2 25%, #d4d7db 37%, #f2f2f2 63%) |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #303030 |
| Transition | none |
| Painted layers | div.skeleton-row 1392.0x56.0 image linear-gradient(90deg, #f2f2f2 25%, #d4d7db 37%, #f2f2f2 63%) r 4px |
| How | at rest |

Crops: `skeleton-default.png`, `skeleton-light.png`.

#### empty-state

Empty state (No notebooks found).

Page copy: `search-dark-empty`. Finder: `() => P(Q('h2.no-results-heading')) // Q('h2.no-results-heading')`.

Dark theme.

| Property | default | action | action-hover | action-focus-visible |
|---|---|---|---|---|
| Size (w x h) | 1392 x 320 | 134.19 x 40 | 134.19 x 40 | 134.19 x 40 |
| Padding | 64px 16px | 0px 24px | 0px 24px | 0px 24px |
| Gap | 8px | - | - | - |
| Border | none | 1px solid #37383b | 1px solid #37383b | 1px solid #37383b |
| Radius | 16px | 100px | 100px | 100px |
| Background | #1b1b1b | transparent | transparent | transparent |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | Google Sans Flex 15px/normal 370 | Google Sans Flex 15px/normal 370 | Google Sans Flex 15px/normal 370 |
| Letter spacing | normal | = | = | = |
| Colour | #c7c7c7 | #f2f2f2 | #f2f2f2 | #f2f2f2 |
| Text node | mat-icon.mat-icon.notranslate.no-results-icon: Luminous Symbols 48px/48px 400, #ffffff @ 0.55 | span.mdc-button__label: Google Sans Flex 15px/normal 370, #f2f2f2 | span.mdc-button__label: Google Sans Flex 15px/normal 370, #f2f2f2 | span.mdc-button__label: Google Sans Flex 15px/normal 370, #f2f2f2 |
| Transition | none | border 0.28s cubic-bezier(0.4, 0, 0.2, 1) | border 0.28s cubic-bezier(0.4, 0, 0.2, 1) | border 0.28s cubic-bezier(0.4, 0, 0.2, 1) |
| Painted layers | div.no-results-container 1392.0x320.0 bg #1b1b1b r 16px; button.mdc-button.mat-mdc-button-base.no-results-clear-button 134.2x40.0 border T:1px solid #37383b / R:1px solid #37383b / B:1px solid #37383b / L:1px solid #37383b r 100px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 134.188pxx40px bg #e6e6e6 r 100px opacity 0 | button.mdc-button.mat-mdc-button-base.no-results-clear-button 134.2x40.0 border T:1px solid #37383b / R:1px solid #37383b / B:1px solid #37383b / L:1px solid #37383b r 100px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 134.188pxx40px bg #e6e6e6 r 100px opacity 0 | button.mdc-button.mat-mdc-button-base.no-results-clear-button 134.2x40.0 border T:1px solid #37383b / R:1px solid #37383b / B:1px solid #37383b / L:1px solid #37383b r 100px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 134.188pxx40px bg #e6e6e6 r 100px opacity 0.08 | button.mdc-button.mat-mdc-button-base.no-results-clear-button 134.2x40.0 border T:1px solid #37383b / R:1px solid #37383b / B:1px solid #37383b / L:1px solid #37383b r 100px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 134.188pxx40px bg #e6e6e6 r 100px opacity 0; span.mat-focus-indicator::before 144.188pxx50px border T:3px solid #c3cafc / R:3px solid #c3cafc / B:3px solid #c3cafc / L:3px solid #c3cafc r 100px |
| How | at rest | at rest, captured action | mouse hover | keyboard: focus(), Shift+Tab, Tab |
| Cursor | - | default | pointer | default |
| Ancestor paint | - | 1 up div.no-results-container bg #1b1b1b | 1 up div.no-results-container bg #1b1b1b | 1 up div.no-results-container bg #1b1b1b |

Light theme.

| Property | light | light-action | light-action-hover | light-action-focus-visible |
|---|---|---|---|---|
| Size (w x h) | 1392 x 320 | 134.19 x 40 | 134.19 x 40 | 134.19 x 40 |
| Padding | 64px 16px | 0px 24px | 0px 24px | 0px 24px |
| Gap | 8px | - | - | - |
| Border | none | 1px solid #dde1eb | 1px solid #dde1eb | 1px solid #dde1eb |
| Radius | 16px | 100px | 100px | 100px |
| Background | #f8fafd | transparent | transparent | transparent |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | Google Sans Flex 15px/normal 370 | Google Sans Flex 15px/normal 370 | Google Sans Flex 15px/normal 370 |
| Letter spacing | normal | = | = | = |
| Colour | #303030 | #1b1b1c | #1b1b1c | #1b1b1c |
| Text node | mat-icon.mat-icon.notranslate.no-results-icon: Luminous Symbols 48px/48px 400, #000000 @ 0.55 | span.mdc-button__label: Google Sans Flex 15px/normal 370, #1b1b1c | span.mdc-button__label: Google Sans Flex 15px/normal 370, #1b1b1c | span.mdc-button__label: Google Sans Flex 15px/normal 370, #1b1b1c |
| Transition | none | border 0.28s cubic-bezier(0.4, 0, 0.2, 1) | border 0.28s cubic-bezier(0.4, 0, 0.2, 1) | border 0.28s cubic-bezier(0.4, 0, 0.2, 1) |
| Painted layers | div.no-results-container 1392.0x320.0 bg #f8fafd r 16px; button.mdc-button.mat-mdc-button-base.no-results-clear-button 134.2x40.0 border T:1px solid #dde1eb / R:1px solid #dde1eb / B:1px solid #dde1eb / L:1px solid #dde1eb r 100px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 134.188pxx40px bg #000000 r 100px opacity 0 | button.mdc-button.mat-mdc-button-base.no-results-clear-button 134.2x40.0 border T:1px solid #dde1eb / R:1px solid #dde1eb / B:1px solid #dde1eb / L:1px solid #dde1eb r 100px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 134.188pxx40px bg #000000 r 100px opacity 0 | button.mdc-button.mat-mdc-button-base.no-results-clear-button 134.2x40.0 border T:1px solid #dde1eb / R:1px solid #dde1eb / B:1px solid #dde1eb / L:1px solid #dde1eb r 100px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 134.188pxx40px bg #000000 r 100px opacity 0.08 | button.mdc-button.mat-mdc-button-base.no-results-clear-button 134.2x40.0 border T:1px solid #dde1eb / R:1px solid #dde1eb / B:1px solid #dde1eb / L:1px solid #dde1eb r 100px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 134.188pxx40px bg #000000 r 100px opacity 0; span.mat-focus-indicator::before 144.188pxx50px border T:3px solid #4259ff / R:3px solid #4259ff / B:3px solid #4259ff / L:3px solid #4259ff r 100px |
| How | at rest | at rest, captured action | mouse hover | keyboard: focus(), Shift+Tab, Tab |
| Cursor | - | default | pointer | default |
| Ancestor paint | - | 1 up div.no-results-container bg #f8fafd | 1 up div.no-results-container bg #f8fafd | 1 up div.no-results-container bg #f8fafd |

Other finders: action: `() => Q('button.no-results-clear-button')`; action-hover: `() => Q('button.no-results-clear-button')`; light-action: `() => Q('button.no-results-clear-button')`; action-focus-visible: `() => Q('button.no-results-clear-button')`; light-action-hover: `() => Q('button.no-results-clear-button')`; light-action-focus-visible: `() => Q('button.no-results-clear-button')`.

Crops: `empty-state-default.png`, `empty-state-action.png`, `empty-state-action-hover.png`, `empty-state-action-focus-visible.png`, `empty-state-light.png`, `empty-state-light-action.png`, `empty-state-light-action-hover.png`, `empty-state-light-action-focus-visible.png`.

### Shell

#### header

Page header (home).

Page copy: `home-dark`. Finder: `() => Q('page-header') // Q('header')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #0f0f0f |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #c7c7c7 |
| Text node | span.logo-text: Google Sans Flex 23px/29px 475, #f2f2f2, ls -0.62px |
| Transition | none |
| Painted layers | page-header.welcome-page-navbar 1440.0x64.0 bg #0f0f0f; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 44pxx36px bg #e6e6e6 r 9999px opacity 0; button.mdc-button.mat-mdc-button-base.mat-badge 109.9x36.0 bg #171717 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 109.891pxx36px bg #e6e6e6 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 96.1562pxx36px bg #e6e6e6 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 91.4219pxx36px bg #e6e6e6 r 9999px opacity 0 |
| Ancestor paint | 1 up welcome-page bg #0f0f0f |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 1440 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #faf9f9 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #303030 |
| Text node | span.logo-text: Google Sans Flex 23px/29px 475, #1b1b1c, ls -0.62px |
| Transition | none |
| Painted layers | page-header.welcome-page-navbar 1440.0x64.0 bg #faf9f9; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 44pxx36px bg #000000 r 9999px opacity 0; button.mdc-button.mat-mdc-button-base.mat-badge 109.9x36.0 bg #f2f0f0 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 109.891pxx36px bg #000000 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 96.1562pxx36px bg #000000 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 91.4219pxx36px bg #000000 r 9999px opacity 0 |
| Ancestor paint | 1 up welcome-page bg #faf9f9 |
| How | at rest |

Crops: none.

#### panel-sources

Sources panel.

Page copy: `notebook-dark`. Finder: `() => Q('section.source-panel')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 354 x 824 |
| Padding | 8px |
| Gap | 0px |
| Border | 1px solid #000000 @ 0 |
| Radius | 32px |
| Background | #1f1f1f |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #c7c7c7 |
| Text node | span: Google Sans Flex 15px/20px 400, #e6e6e6 |
| Transition | inline-size, min-inline-size 0.2s, 0.2s ease-in-out, ease-in-out delay 0s, 0s |
| Placeholder | "" #ffffff, opacity 1, 13.3333px |
| Painted layers | section.source-panel 354.0x824.0 bg #1f1f1f border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 32px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 20pxx20px bg #e6e6e6 r 9999px opacity 0; button.mdc-button.mat-mdc-button-base.mat-badge 336.0x36.0 bg #171717 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 336pxx36px bg #e6e6e6 r 9999px opacity 0; div.mat-mdc-tooltip-trigger.container.mat-mdc-tooltip-disabled 336.0x96.0 bg #171717 r 24px; button.mdc-button.mat-mdc-button-base.mat-badge 102.5x36.0 bg #1f1f1f r 9999px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 354 x 824 |
| Padding | 8px |
| Gap | 0px |
| Border | 1px solid #000000 @ 0 |
| Radius | 32px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #303030 |
| Text node | span: Google Sans Flex 15px/20px 400, #000000 |
| Transition | inline-size, min-inline-size 0.2s, 0.2s ease-in-out, ease-in-out delay 0s, 0s |
| Placeholder | "" #000000, opacity 1, 13.3333px |
| Painted layers | section.source-panel 354.0x824.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 32px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 20pxx20px bg #000000 r 9999px opacity 0; button.mdc-button.mat-mdc-button-base.mat-badge 336.0x36.0 bg #f2f0f0 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 336pxx36px bg #000000 r 9999px opacity 0; div.mat-mdc-tooltip-trigger.container.mat-mdc-tooltip-disabled 336.0x96.0 bg #f2f0f0 r 24px; button.mdc-button.mat-mdc-button-base.mat-badge 102.5x36.0 bg #ffffff r 9999px |
| How | at rest |

Crops: none.

#### panel-chat

Chat panel.

Page copy: `notebook-dark`. Finder: `() => Q('section.chat-panel')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 679.67 x 836 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #0f0f0f |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #c7c7c7 |
| Text node | mat-icon.mat-icon.notranslate.cover-image-empty-icon: Google Symbols 192px/192px 400, #ffffff @ 0.12 |
| Transition | none |
| Placeholder | "Search" #e6e6e6, opacity 1, 12px |
| Painted layers | section.chat-panel 679.7x836.0 bg #0f0f0f; div.chat-panel-top-fade.is-visible 679.7x28.0 image linear-gradient(#0f0f0f 0px, #0f0f0f @ 0.98 10%, #0f0f0f @ 0.88 22%, #0f0f0f @ 0.68 38%, c; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 131.922pxx36px bg #e6e6e6 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #e6e6e6 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #e6e6e6 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #e6e6e6 r 9999px opacity 0 |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 679.67 x 836 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #faf9f9 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #303030 |
| Text node | mat-icon.mat-icon.notranslate.cover-image-empty-icon: Google Symbols 192px/192px 400, #000000 @ 0.08 |
| Transition | none |
| Placeholder | "Search" #e6e6e6, opacity 1, 12px |
| Painted layers | section.chat-panel 679.7x836.0 bg #faf9f9; div.chat-panel-top-fade.is-visible 679.7x28.0 image linear-gradient(#faf9f9 0px, #faf9f9 @ 0.98 10%, #faf9f9 @ 0.88 22%, #faf9f9 @ 0.68 38%, c; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 131.922pxx36px bg #000000 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #000000 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #000000 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #000000 r 9999px opacity 0 |
| How | at rest |

Crops: none.

#### panel-studio

Studio panel.

Page copy: `notebook-dark`. Finder: `() => Q('section.studio-panel')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 354 x 824 |
| Padding | 8px |
| Gap | 0px |
| Border | 1px solid #000000 @ 0 |
| Radius | 32px |
| Background | #1f1f1f |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #c7c7c7 |
| Text node | span: Google Sans Flex 15px/20px 400, #e6e6e6 |
| Transition | inline-size, min-inline-size 0.2s, 0.2s ease-in-out, ease-in-out delay 0s, 0s |
| Painted layers | section.studio-panel 354.0x824.0 bg #1f1f1f border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 32px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 20pxx20px bg #e6e6e6 r 9999px opacity 0; div.artifact-callout.mat-label-medium 336.0x60.0 bg #1f1f1f image linear-gradient(268deg, #a9a8ff @ 0.15 0px, #3186ff @ 0.15 100%), none r 16px shadow #000000 @ 0.28 0px 0px 20px 0px; button.mdc-button.mat-mdc-button-base.mat-badge 56.8x36.0 bg #171717 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 56.7969pxx36px bg #e6e6e6 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #e6e6e6 r 9999px opacity 0 |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 354 x 824 |
| Padding | 8px |
| Gap | 0px |
| Border | 1px solid #000000 @ 0 |
| Radius | 32px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #303030 |
| Text node | span: Google Sans Flex 15px/20px 400, #000000 |
| Transition | inline-size, min-inline-size 0.2s, 0.2s ease-in-out, ease-in-out delay 0s, 0s |
| Painted layers | section.studio-panel 354.0x824.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 32px; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 20pxx20px bg #000000 r 9999px opacity 0; div.artifact-callout.mat-label-medium 336.0x60.0 bg #ffffff image linear-gradient(268deg, #a9a8ff @ 0.15 0px, #3186ff @ 0.15 100%), none r 16px shadow #000000 @ 0.04 0px 0px 20px 0px; button.mdc-button.mat-mdc-button-base.mat-badge 56.8x36.0 bg #f2f0f0 r 9999px; span.mat-mdc-button-persistent-ripple.mdc-button__ripple::before 56.7969pxx36px bg #000000 r 9999px opacity 0; span.mat-mdc-button-persistent-ripple.mdc-icon-button__ripple::before 36pxx36px bg #000000 r 9999px opacity 0 |
| How | at rest |

Crops: none.

### Type

#### type-page-title

Page title (My notebooks).

Page copy: `home-dark`. Finder: `() => Q('h2.projects-header')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 154.41 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 24px/32px 400 |
| Letter spacing | normal |
| Colour | #f2f2f2 |
| Transition | none |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 154.41 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 24px/32px 400 |
| Letter spacing | normal |
| Colour | #1b1b1c |
| Transition | none |
| How | at rest |

Crops: none.

#### type-cover-title

Notebook cover title.

Page copy: `notebook-dark`. Finder: `() => Q('h2.cover-title')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 591.67 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 36px/44px 320 |
| Letter spacing | normal |
| Colour | #e6e6e6 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 591.67 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 36px/44px 320 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: none.

#### type-panel-header

Panel header (Sources).

Page copy: `notebook-dark`. Finder: `() => Q('.panel-header h2') // Q('h2.panel-header-content')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 296 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 15px/20px 400 |
| Letter spacing | normal |
| Colour | #e6e6e6 |
| Text node | span: Google Sans Flex 15px/20px 400, #e6e6e6 |
| Transition | none |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 296 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 15px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Google Sans Flex 15px/20px 400, #000000 |
| Transition | none |
| How | at rest |

Crops: none.

#### type-dialog-title

Dialog title.

Page copy: `home-dark-delete-confirm`. Finder: `() => Q('[role=dialog] h2')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 400 x 32 |
| Padding | 4px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 20px/24px 470 |
| Letter spacing | normal |
| Colour | #e6e6e6 |
| Transition | none |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 400 x 32 |
| Padding | 4px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 20px/24px 470 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: none.

#### type-heading

Answer heading.

Page copy: `notebook-dark`. Finder: `() => Q('.paragraph.heading3') // Q('.paragraph[class*=heading]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 549.67 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 20px/24px 470 |
| Letter spacing | normal |
| Colour | #c7c7c7 |
| Text node | b: Google Sans Flex 20px/24px 470, #c7c7c7 |
| Transition | none |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 549.67 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 20px/24px 470 |
| Letter spacing | normal |
| Colour | #303030 |
| Text node | b: Google Sans Flex 20px/24px 470, #303030 |
| Transition | none |
| How | at rest |

Crops: none.

#### type-body

Answer body paragraph.

Page copy: `notebook-dark`. Finder: `() => Q('labs-tailwind-structural-element-view-v2 .paragraph.normal') // Q('labs-tailwind-structural-element-view-v2 .paragraph')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 549.67 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 17px/24px 400 |
| Letter spacing | normal |
| Colour | #c7c7c7 |
| Text node | span: Google Sans Flex 17px/24px 400, #c7c7c7 |
| Transition | none |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 549.67 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 17px/24px 400 |
| Letter spacing | normal |
| Colour | #303030 |
| Text node | span: Google Sans Flex 17px/24px 400, #303030 |
| Transition | none |
| How | at rest |

Crops: none.

#### type-caption

Card meta line (date, source count).

Page copy: `home-dark`. Finder: `() => Q('.project-button-subtitle-part')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 76.23 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 15px/20px 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.55 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 76.23 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 15px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.55 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: none.

#### type-code

Inline code.

Page copy: `notebook-dark`. Finder: `() => Q('code.code')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 147 x 22 |
| Padding | 4px 6px |
| Border | none |
| Radius | 9999px |
| Background | #171717 |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Code 15px/14px 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.55 |
| Transition | none |
| Painted layers | code.code 147.0x22.0 bg #171717 r 9999px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 147 x 22 |
| Padding | 4px 6px |
| Border | none |
| Radius | 9999px |
| Background | #f2f0f0 |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Code 15px/14px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.55 |
| Transition | none |
| Painted layers | code.code 147.0x22.0 bg #f2f0f0 r 9999px |
| How | at rest |

Crops: none.

#### type-disclaimer

Composer footnote.

Page copy: `notebook-dark`. Finder: `() => Q('.disclaimer')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 628 x 41 |
| Padding | 12px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 13px/17px 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.55 |
| Transition | none |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 628 x 41 |
| Padding | 12px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 13px/17px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.55 |
| Transition | none |
| How | at rest |

Crops: none.
