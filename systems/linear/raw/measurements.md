# Linear component measurements

Computed styles read on 2026-10-17 by `tools/capture/signed-in/measure.mjs` from static page copies of the signed-in app (1440x900 (the mobile-* copies 390x844), deviceScaleFactor 2), and written here by `tools/capture/signed-in/build-measurements.mjs` from [components-computed.json](components-computed.json). Dark copies were taken with the account theme Dark, light copies with it set to Light (and set back afterwards). Dark states have plain names; light states are `light`, `light-<state>`. Every state records `theme` and `snapshot`.

Every component has one table per theme: a column per state, a row per property. A cell that repeats the first column reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline (a hover or selection is sometimes painted on an inner layer, not the element itself); "Ancestor paint" the same for its parents. Linear styles with stylex, whose hashed classes name no variables, so the theme variables behind these values are in [css-vars.json](css-vars.json) instead.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab), skipped where the element cannot take focus; `pressed` is the mouse held down on the element (:active). Linear draws focus rings in plain CSS (:focus-visible), so they survive in the static copies. The rest (`selected`, `open`, `readonly`, `off`, `option-highlighted`) are other elements or copies captured in that state. Light states are prefixed `light` and were read from copies taken with the account theme set to Light. The 390 wide copies are measured at rest only.

47 components, 202 states (202 measured, 0 skipped, 0 not found).

## Shared values

Tallied over every measured state by the build script.

- **Radius scale** (element radius, times seen): 8px (65), 9999px (55), 12px (10), 72px (10), 21px (2), 3px (2), 48px (2), 4px (2), 50% (2), 2.8125px (2).
- **Transitions**: `border, background-color, color, opacity 0.15s ease` (29), `color 0.15s ease` (18), `background-color, opacity 0.15s ease-out` (10), `background-color 0.1s ease` (7), `border 0.15s ease` (6), `border-color 0.15s ease` (4), `background-color, border, color 0.15s ease` (4), `all 0.15s ease` (4), `max-width, background-color 0.22s cubic-bezier(0.43, 0.07, 0.59, 0.94)` (2), `transform 0.2s ease` (2).
- **Font families**: Inter Variable (308), ui-sans-serif (8), Berkeley Mono (4), Apple Color Emoji (2).
- **Type sizes** (size/line-height weight of the first text): 13px/normal 500 (62), 12px/normal 500 (41), 12px/normal 450 (33), 13px/normal 400 (16), 13.3333px/normal 400 (12), 13px/19.5px 400 (6), 12px/0px 600 (6), 15px/22.5px 450 (4), 11px/12.1px 400 (4), 13px/normal 450 (2), 11px/16.5px 450 (2), 11px/12px 500 (2), 16px/24px 400 (2), 24px/32px 600 (2).
- **Shadows**: `#000000 @ 0.3 0px 0.5px 1px 1px` (23); `#000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px` (23); `#000000 @ 0.088 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px` (16); `#ffffff @ 0.137 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px` (9); `#000000 @ 0.09 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px` (9); `#ffffff @ 0.149 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px` (8).
- **Focus-visible, dark** (17 focused states): outline 1px solid #5e6ad2 offset 0px (4); nothing painted on the element (4); outline 1px solid #5e6ad2 offset -1px (4); outline 1px solid #5e6ad2 offset 2px (3); outline 1px solid #5e6ad2 offset 1px (1); shadow #ffffff @ 0.083 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px (1).
- **Focus-visible, light** (17 focused states): outline 1px solid #6d78d5 offset 0px (4); nothing painted on the element (4); outline 1px solid #6d78d5 offset -1px (4); outline 1px solid #6d78d5 offset 2px (3); outline 1px solid #6d78d5 offset 1px (1); shadow #000000 @ 0.088 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px (1).
- **Hover changes, dark** (21 hovered components, 4 with no change on the element or its first painted layer): backgroundColor #5e6ad2 → #6975e2 (3); backgroundColor #1b1c1d → #252527 (2); backgroundColor #000000 @ 0 → #232424 (2); inner layer undefined → #361d1e (1); backgroundColor #2a2b2d → #343538 (1); backgroundColor #000000 @ 0 → #1d1e1f (1); backgroundColor #232325 → #2c2d2f (1); backgroundColor #1c1c1d → #232424 (1).
- **Hover changes, light** (21 hovered components, 4 with no change on the element or its first painted layer): backgroundColor #ffffff → #f3f3f3 (4); backgroundColor #6d78d5 → #5e6ac1 (3); backgroundColor #000000 @ 0 → #f0f0f1 (2); inner layer undefined → #fde9e9 (1); backgroundColor #000000 @ 0 → #efefef (1); backgroundColor #ffffff → #f0f0f1 (1); backgroundColor #000000 @ 0 → #e7e7e8 (1); inner layer undefined → undefined (1).

### Tokens the measured components use

Every custom property a measured component's classes or inline style name, with the value it resolved to in each theme.

| Token | Dark | Light |
|---|---|---|

## Components

### Buttons

#### button-primary

Primary button (Create issue). The composer submit button.

Page copy: `composer-dark`. Finder: `() => Q('[role=dialog] button[type=submit]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 93.63 x 28 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #5e6ad2 | #6975e2 | = | #6975e2 |
| Box shadow | #000000 @ 0.3 0px 0.5px 1px 1px | = | = | = |
| Outline | none | = | 1px solid #5e6ad2 offset 2px | = |
| Font | Inter Variable 12px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fffeff | = | = | = |
| Transition | border, background-color, color, opacity 0.15s ease | none | = | none |
| Cursor | default | = | = | = |
| Painted layers | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 93.6x28.0 bg #5e6ad2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.3 0px 0.5px 1px 1px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 93.6x28.0 bg #6975e2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.3 0px 0.5px 1px 1px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 93.6x28.0 bg #5e6ad2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.3 0px 0.5px 1px 1px outline 1px solid #5e6ad2 offset 2px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 93.6x28.0 bg #6975e2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.3 0px 0.5px 1px 1px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 93.63 x 28 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #6d78d5 | #5e6ac1 | = | #5e6ac1 |
| Box shadow | #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | = | = | = |
| Outline | none | = | 1px solid #6d78d5 offset 2px | = |
| Font | Inter Variable 12px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fffeff | = | = | = |
| Transition | border, background-color, color, opacity 0.15s ease | none | = | none |
| Cursor | default | = | = | = |
| Painted layers | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 93.6x28.0 bg #6d78d5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 93.6x28.0 bg #5e6ac1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 93.6x28.0 bg #6d78d5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px outline 1px solid #6d78d5 offset 2px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 93.6x28.0 bg #5e6ac1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Crops: `button-primary-default.png`, `button-primary-hover.png`, `button-primary-focus-visible.png`, `button-primary-pressed.png`, `button-primary-light.png`, `button-primary-light-hover.png`, `button-primary-light-focus-visible.png`, `button-primary-light-pressed.png`.

#### button-primary-small

Primary button, page header (Invite).

Page copy: `settings-members-dark`. Finder: `() => TB('Invite', M())`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 59.84 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #5e6ad2 | #6975e2 | = | #6975e2 |
| Box shadow | #000000 @ 0.3 0px 0.5px 1px 1px | = | = | = |
| Outline | none | = | 1px solid #5e6ad2 offset 2px | = |
| Font | Inter Variable 13px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fffeff | = | = | = |
| Transition | border, background-color, color, opacity 0.15s ease | none | = | none |
| Cursor | default | = | = | = |
| Painted layers | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 59.8x32.0 bg #5e6ad2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.3 0px 0.5px 1px 1px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 59.8x32.0 bg #6975e2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.3 0px 0.5px 1px 1px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 59.8x32.0 bg #5e6ad2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.3 0px 0.5px 1px 1px outline 1px solid #5e6ad2 offset 2px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 59.8x32.0 bg #6975e2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.3 0px 0.5px 1px 1px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 59.84 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #6d78d5 | #5e6ac1 | = | #5e6ac1 |
| Box shadow | #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | = | = | = |
| Outline | none | = | 1px solid #6d78d5 offset 2px | = |
| Font | Inter Variable 13px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fffeff | = | = | = |
| Transition | border, background-color, color, opacity 0.15s ease | none | = | none |
| Cursor | default | = | = | = |
| Painted layers | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 59.8x32.0 bg #6d78d5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 59.8x32.0 bg #5e6ac1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 59.8x32.0 bg #6d78d5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px outline 1px solid #6d78d5 offset 2px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 59.8x32.0 bg #5e6ac1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Crops: `button-primary-small-default.png`, `button-primary-small-hover.png`, `button-primary-small-focus-visible.png`, `button-primary-small-pressed.png`, `button-primary-small-light.png`, `button-primary-small-light-hover.png`, `button-primary-small-light-focus-visible.png`, `button-primary-small-light-pressed.png`.

#### button-secondary

Secondary button (Export CSV).

Page copy: `settings-members-dark`. Finder: `() => TB('Export CSV', M())`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 97.27 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #1b1c1d | #252527 | = | #252527 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #5e6ad2 offset 0px | = |
| Font | Inter Variable 13px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #e3e4e6 | = | = | = |
| Transition | border, background-color, color, opacity 0.15s ease | none | = | none |
| Cursor | default | = | = | = |
| ::after | 95.2656px x 30px, absolute, bg #000000 @ 0, radius 9999px, shadow #ffffff @ 0.137 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | 95.2656px x 30px, absolute, bg #000000 @ 0, radius 9999px, shadow #ffffff @ 0.229 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | = | 95.2656px x 30px, absolute, bg #000000 @ 0, radius 9999px, shadow #ffffff @ 0.229 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px |
| Painted layers | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 97.3x32.0 bg #1b1c1d border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 95.2656pxx30px r 9999px shadow #ffffff @ 0.137 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 97.3x32.0 bg #252527 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 95.2656pxx30px r 9999px shadow #ffffff @ 0.229 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 97.3x32.0 bg #1b1c1d border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px outline 1px solid #5e6ad2 offset 0px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 95.2656pxx30px r 9999px shadow #ffffff @ 0.137 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 97.3x32.0 bg #252527 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 95.2656pxx30px r 9999px shadow #ffffff @ 0.229 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 97.27 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | #f3f3f3 | = | #f3f3f3 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #6d78d5 offset 0px | = |
| Font | Inter Variable 13px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2f2f31 | = | = | = |
| Transition | border, background-color, color, opacity 0.15s ease | none | = | none |
| Cursor | default | = | = | = |
| ::after | 95.2656px x 30px, absolute, bg #000000 @ 0, radius 9999px, shadow #000000 @ 0.09 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | 95.2656px x 30px, absolute, bg #000000 @ 0, radius 9999px, shadow #000000 @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | = | 95.2656px x 30px, absolute, bg #000000 @ 0, radius 9999px, shadow #000000 @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px |
| Painted layers | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 97.3x32.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 95.2656pxx30px r 9999px shadow #000000 @ 0.09 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 97.3x32.0 bg #f3f3f3 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 95.2656pxx30px r 9999px shadow #000000 @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 97.3x32.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px outline 1px solid #6d78d5 offset 0px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 95.2656pxx30px r 9999px shadow #000000 @ 0.09 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 97.3x32.0 bg #f3f3f3 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 95.2656pxx30px r 9999px shadow #000000 @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Crops: `button-secondary-default.png`, `button-secondary-hover.png`, `button-secondary-focus-visible.png`, `button-secondary-pressed.png`, `button-secondary-light.png`, `button-secondary-light-hover.png`, `button-secondary-light-focus-visible.png`, `button-secondary-light-pressed.png`.

#### button-danger

Destructive button (Delete workspace). Measured at rest and on hover only; it was never clicked.

Page copy: `settings-workspace-dark`. Finder: `() => TB('Delete workspace', M())`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 131.92 x 32 | = | = |
| Padding | 0px | = | = |
| Gap | 4px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter Variable 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Text node | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4: Inter Variable 13px/normal 500, #ff8683 | = | = |
| Transition | none | = | = |
| Cursor | default | = | = |
| Painted layers | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 137.9x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 137.9x32.0 bg #361d1e border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 137.9x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px outline 1px solid #5e6ad2 offset 0px |
| Ancestor paint | 3 up section.sx-tr9pb5.sx-1i2ui7b.sx-1wadh23 bg #1a1a1b shadow #ffffff @ 0.083 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 131.92 x 32 | = | = |
| Padding | 0px | = | = |
| Gap | 4px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter Variable 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1b1b1b | = | = |
| Text node | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4: Inter Variable 13px/normal 500, #e2253b | = | = |
| Transition | none | = | = |
| Cursor | default | = | = |
| Painted layers | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 137.9x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 137.9x32.0 bg #fde9e9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 137.9x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px outline 1px solid #6d78d5 offset 0px |
| Ancestor paint | 3 up section.sx-tr9pb5.sx-1i2ui7b.sx-1wadh23 bg #ffffff shadow #000000 @ 0.088 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) |

Crops: `button-danger-default.png`, `button-danger-hover.png`, `button-danger-focus-visible.png`, `button-danger-light.png`, `button-danger-light-hover.png`, `button-danger-light-focus-visible.png`.

#### icon-button

Icon button (Copy issue URL).

Page copy: `issue-dark`. Finder: `() => Q('button[aria-label="Copy issue URL"]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 28 x 28 | = | = | = |
| Padding | 0px 2px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #1b1c1d | #252527 | = | #252527 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #5e6ad2 offset 0px | = |
| Font | Inter Variable 12px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #e3e4e6 | = | = | = |
| Transition | border, background-color, color, opacity 0.15s ease | none | = | none |
| Cursor | default | = | = | = |
| Icon | 14 x 14, colour #e3e4e6, fill #959597 | 14 x 14, colour #e3e4e6, fill #ffffff | = | 14 x 14, colour #e3e4e6, fill #ffffff |
| ::before | 32px x 32px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| ::after | 26px x 26px, absolute, bg #000000 @ 0, radius 9999px, shadow #ffffff @ 0.137 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | 26px x 26px, absolute, bg #000000 @ 0, radius 9999px, shadow #ffffff @ 0.229 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | = | 26px x 26px, absolute, bg #000000 @ 0, radius 9999px, shadow #ffffff @ 0.229 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px |
| Painted layers | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 28.0x28.0 bg #1b1c1d border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 26pxx26px r 9999px shadow #ffffff @ 0.137 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 28.0x28.0 bg #252527 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 26pxx26px r 9999px shadow #ffffff @ 0.229 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 28.0x28.0 bg #1b1c1d border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px outline 1px solid #5e6ad2 offset 0px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 26pxx26px r 9999px shadow #ffffff @ 0.137 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 28.0x28.0 bg #252527 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 26pxx26px r 9999px shadow #ffffff @ 0.229 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 28 x 28 | = | = | = |
| Padding | 0px 2px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | #f3f3f3 | = | #f3f3f3 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #6d78d5 offset 0px | = |
| Font | Inter Variable 12px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2f2f31 | = | = | = |
| Transition | border, background-color, color, opacity 0.15s ease | none | = | none |
| Cursor | default | = | = | = |
| Icon | 14 x 14, colour #2f2f31, fill #5c5c5e | 14 x 14, colour #2f2f31, fill #1b1b1b | = | 14 x 14, colour #2f2f31, fill #1b1b1b |
| ::before | 32px x 32px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| ::after | 26px x 26px, absolute, bg #000000 @ 0, radius 9999px, shadow #000000 @ 0.09 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | 26px x 26px, absolute, bg #000000 @ 0, radius 9999px, shadow #000000 @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | = | 26px x 26px, absolute, bg #000000 @ 0, radius 9999px, shadow #000000 @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px |
| Painted layers | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 28.0x28.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 26pxx26px r 9999px shadow #000000 @ 0.09 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 28.0x28.0 bg #f3f3f3 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 26pxx26px r 9999px shadow #000000 @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 28.0x28.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px outline 1px solid #6d78d5 offset 0px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 26pxx26px r 9999px shadow #000000 @ 0.09 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 28.0x28.0 bg #f3f3f3 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 26pxx26px r 9999px shadow #000000 @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Crops: `icon-button-default.png`, `icon-button-hover.png`, `icon-button-focus-visible.png`, `icon-button-pressed.png`, `icon-button-light.png`, `icon-button-light-hover.png`, `icon-button-light-focus-visible.png`, `icon-button-light-pressed.png`.

#### property-chip

Property chip button (composer status).

Page copy: `composer-dark`. Finder: `() => Q('[role=dialog] button[aria-label="Change status"]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 79.77 x 24 | = | = | = |
| Padding | 0px 8px 0px 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #2a2b2d | #343538 | = | #343538 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #5e6ad2 offset 0px | = |
| Font | Inter Variable 12px/12px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9c9da0 | = | = | = |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-167xe44: Inter Variable 12px/normal 450, #e5e6e9 | = | = | = |
| Transition | border, background-color, color, opacity 0.15s ease | none | = | none |
| Cursor | default | = | = | = |
| Icon | 14 x 14, colour #9c9da0, fill #bec2c8 | = | = | = |
| ::before | 85.7656px x 30px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| ::after | 77.7656px x 22px, absolute, bg #000000 @ 0, radius 9999px, shadow #ffffff @ 0.149 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | 77.7656px x 22px, absolute, bg #000000 @ 0, radius 9999px, shadow #ffffff @ 0.248 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | = | 77.7656px x 22px, absolute, bg #000000 @ 0, radius 9999px, shadow #ffffff @ 0.248 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px |
| Painted layers | button.sx-3nfvp2.sx-16dsc37.sx-l56j7k 79.8x24.0 bg #2a2b2d border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-l56j7k::after 77.7656pxx22px r 9999px shadow #ffffff @ 0.149 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | button.sx-3nfvp2.sx-16dsc37.sx-l56j7k 79.8x24.0 bg #343538 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-l56j7k::after 77.7656pxx22px r 9999px shadow #ffffff @ 0.248 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | button.sx-3nfvp2.sx-16dsc37.sx-l56j7k 79.8x24.0 bg #2a2b2d border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px outline 1px solid #5e6ad2 offset 0px; button.sx-3nfvp2.sx-16dsc37.sx-l56j7k::after 77.7656pxx22px r 9999px shadow #ffffff @ 0.149 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | button.sx-3nfvp2.sx-16dsc37.sx-l56j7k 79.8x24.0 bg #343538 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-l56j7k::after 77.7656pxx22px r 9999px shadow #ffffff @ 0.248 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 79.77 x 24 | = | = | = |
| Padding | 0px 8px 0px 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | #f3f3f3 | = | #f3f3f3 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #6d78d5 offset 0px | = |
| Font | Inter Variable 12px/12px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #5e5e60 | = | = | = |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-167xe44: Inter Variable 12px/normal 450, #303032 | = | = | = |
| Transition | border, background-color, color, opacity 0.15s ease | none | = | none |
| Cursor | default | = | = | = |
| Icon | 14 x 14, colour #5e5e60, fill #a8acb2 | = | = | = |
| ::before | 85.7656px x 30px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| ::after | 77.7656px x 22px, absolute, bg #000000 @ 0, radius 9999px, shadow #000000 @ 0.088 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | 77.7656px x 22px, absolute, bg #000000 @ 0, radius 9999px, shadow #000000 @ 0.147 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | = | 77.7656px x 22px, absolute, bg #000000 @ 0, radius 9999px, shadow #000000 @ 0.147 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px |
| Painted layers | button.sx-3nfvp2.sx-16dsc37.sx-l56j7k 79.8x24.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-l56j7k::after 77.7656pxx22px r 9999px shadow #000000 @ 0.088 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | button.sx-3nfvp2.sx-16dsc37.sx-l56j7k 79.8x24.0 bg #f3f3f3 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-l56j7k::after 77.7656pxx22px r 9999px shadow #000000 @ 0.147 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | button.sx-3nfvp2.sx-16dsc37.sx-l56j7k 79.8x24.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px outline 1px solid #6d78d5 offset 0px; button.sx-3nfvp2.sx-16dsc37.sx-l56j7k::after 77.7656pxx22px r 9999px shadow #000000 @ 0.088 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | button.sx-3nfvp2.sx-16dsc37.sx-l56j7k 79.8x24.0 bg #f3f3f3 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-l56j7k::after 77.7656pxx22px r 9999px shadow #000000 @ 0.147 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down |

Crops: `property-chip-default.png`, `property-chip-hover.png`, `property-chip-focus-visible.png`, `property-chip-pressed.png`, `property-chip-light.png`, `property-chip-light-hover.png`, `property-chip-light-focus-visible.png`, `property-chip-light-pressed.png`.

### Links

#### link

Inline link (Read more).

Page copy: `settings-workspace-dark`. Finder: `() => Q('main a[href^="https://linear.app/docs"]')`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 82.69 x 17 | = | = |
| Padding | 1px 4px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | #1d1e1f | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px solid #5e6ad2 offset 1px |
| Font | Inter Variable 12px/normal 450 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | color 0.15s ease | none | = |
| Cursor | pointer | = | = |
| ::after | auto x auto, static, bg #000000 @ 0, radius 0px | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |
| Painted layers | - | a.sx-uxw1ft.sx-splgde.sx-fn1xvj 82.7x17.0 bg #1d1e1f r 8px | a.sx-uxw1ft.sx-splgde.sx-fn1xvj 82.7x17.0 r 8px outline 1px solid #5e6ad2 offset 1px |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 82.69 x 17 | = | = |
| Padding | 1px 4px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | #efefef | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px solid #6d78d5 offset 1px |
| Font | Inter Variable 12px/normal 450 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1b1b1b | = | = |
| Transition | color 0.15s ease | none | = |
| Cursor | pointer | = | = |
| ::after | auto x auto, static, bg #000000 @ 0, radius 0px | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |
| Painted layers | - | a.sx-uxw1ft.sx-splgde.sx-fn1xvj 82.7x17.0 bg #efefef r 8px | a.sx-uxw1ft.sx-splgde.sx-fn1xvj 82.7x17.0 r 8px outline 1px solid #6d78d5 offset 1px |

Crops: `link-default.png`, `link-hover.png`, `link-focus-visible.png`, `link-light.png`, `link-light-hover.png`, `link-light-focus-visible.png`.

#### breadcrumb-link

Breadcrumb link.

Page copy: `issue-dark`. Finder: `() => TB('Issues', M())`.

Dark theme.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 49.02 x 24 | = |
| Padding | 0px 5px 0px 4px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | #232424 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-1srpx65: Inter Variable 13px/normal 500, #e3e4e6 | span.sx-1j61x8r.sx-ggjnk3.sx-1srpx65: Inter Variable 13px/normal 500, #ffffff |
| Transition | color 0.15s ease | none |
| Cursor | default | = |
| How | at rest | mouse hover |
| Painted layers | - | a.sx-78zum5.sx-6s0dn4.sx-euugli 49.0x24.0 bg #232424 r 8px |

Light theme.

| Property | light | light-hover |
|---|---|---|
| Size (w x h) | 49.02 x 24 | = |
| Padding | 0px 5px 0px 4px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | #f0f0f1 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1b1b | = |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-1srpx65: Inter Variable 13px/normal 500, #2f2f31 | span.sx-1j61x8r.sx-ggjnk3.sx-1srpx65: Inter Variable 13px/normal 500, #1b1b1b |
| Transition | color 0.15s ease | none |
| Cursor | default | = |
| How | at rest | mouse hover |
| Painted layers | - | a.sx-78zum5.sx-6s0dn4.sx-euugli 49.0x24.0 bg #f0f0f1 r 8px |

Crops: `breadcrumb-link-default.png`, `breadcrumb-link-hover.png`, `breadcrumb-link-light.png`, `breadcrumb-link-light-hover.png`.

### Inputs

#### text-field

Text field (workspace name).

Page copy: `settings-workspace-dark`. Finder: `() => [...document.querySelectorAll('main input:not([type]), main input[type=text]')].find((i) => !i.readOnly && i.getBoundingClientRect().width > 100) // null`.

Dark theme.

| Property | default | hover | focus-visible | readonly |
|---|---|---|---|---|
| Size (w x h) | 256 x 32 | = | = | = |
| Padding | 6px 12px | = | = | 6px 12px 6px 78px |
| Border | 1px solid #48494c | 1px solid #3e424d | = | = |
| Radius | 8px | = | = | = |
| Background | #1a1a1b | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #5e6ad2 offset -1px | = |
| Font | Inter Variable 13px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | border 0.15s ease | none | = | = |
| Cursor | text | = | = | = |
| Placeholder | "Acme" #5c5d5f, opacity 1, 13px | = | = | "" #ffffff, opacity 1, 13px |
| Painted layers | input.sx-dyb6km.sx-y30hb9.sx-1tq37w7 256.0x32.0 bg #1a1a1b border T:1px solid #48494c / R:1px solid #48494c / B:1px solid #48494c / L:1px solid #48494c r 8px | input.sx-dyb6km.sx-y30hb9.sx-1tq37w7 256.0x32.0 bg #1a1a1b border T:1px solid #3e424d / R:1px solid #3e424d / B:1px solid #3e424d / L:1px solid #3e424d r 8px | input.sx-dyb6km.sx-y30hb9.sx-1tq37w7 256.0x32.0 bg #1a1a1b border T:1px solid #48494c / R:1px solid #48494c / B:1px solid #48494c / L:1px solid #48494c r 8px outline 1px solid #5e6ad2 offset -1px | = |
| Ancestor paint | 3 up section.sx-tr9pb5.sx-1i2ui7b.sx-1wadh23 bg #1a1a1b shadow #ffffff @ 0.083 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | = | = | - |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | at rest, captured readonly |

Light theme.

| Property | light | light-hover | light-focus-visible | light-readonly |
|---|---|---|---|---|
| Size (w x h) | 256 x 32 | = | = | = |
| Padding | 6px 12px | = | = | 6px 12px 6px 78px |
| Border | 1px solid #d8d8d8 | 1px solid #c2c2c2 | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #6d78d5 offset -1px | = |
| Font | Inter Variable 13px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1b | = | = | = |
| Transition | border 0.15s ease | none | = | = |
| Cursor | text | = | = | = |
| Placeholder | "Acme" #a0a0a2, opacity 1, 13px | = | = | "" #1b1b1b, opacity 1, 13px |
| Painted layers | input.sx-dyb6km.sx-y30hb9.sx-1tq37w7 256.0x32.0 bg #ffffff border T:1px solid #d8d8d8 / R:1px solid #d8d8d8 / B:1px solid #d8d8d8 / L:1px solid #d8d8d8 r 8px | input.sx-dyb6km.sx-y30hb9.sx-1tq37w7 256.0x32.0 bg #ffffff border T:1px solid #c2c2c2 / R:1px solid #c2c2c2 / B:1px solid #c2c2c2 / L:1px solid #c2c2c2 r 8px | input.sx-dyb6km.sx-y30hb9.sx-1tq37w7 256.0x32.0 bg #ffffff border T:1px solid #d8d8d8 / R:1px solid #d8d8d8 / B:1px solid #d8d8d8 / L:1px solid #d8d8d8 r 8px outline 1px solid #6d78d5 offset -1px | = |
| Ancestor paint | 3 up section.sx-tr9pb5.sx-1i2ui7b.sx-1wadh23 bg #ffffff shadow #000000 @ 0.088 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | = | = | - |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | at rest, captured readonly |

Other finders: readonly: `() => [...document.querySelectorAll('main input:not([type]), main input[type=text]')].find((i) => i.readOnly && i.getBoundingClientRect().width > 100) // null`; light-readonly: `() => [...document.querySelectorAll('main input:not([type]), main input[type=text]')].find((i) => i.readOnly && i.getBoundingClientRect().width > 100) // null`.

Crops: `text-field-default.png`, `text-field-hover.png`, `text-field-focus-visible.png`, `text-field-readonly.png`, `text-field-light.png`, `text-field-light-hover.png`, `text-field-light-focus-visible.png`, `text-field-light-readonly.png`.

#### search-field

Search field.

Page copy: `settings-members-dark`. Finder: `() => Q('main input[type=search]')`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 300 x 32 | = | = |
| Padding | 6px 25px 6px 32px | = | = |
| Border | 1px solid #3f4042 | 1px solid #363a43 | = |
| Radius | 8px | = | = |
| Background | #1b1c1d | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px solid #5e6ad2 offset -1px |
| Font | Inter Variable 13px/normal 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | border-color 0.15s ease | none | = |
| Cursor | text | = | = |
| Placeholder | "Search by name or email" #959597, opacity 1, 13px | = | = |
| Painted layers | input.sx-dyb6km.sx-y30hb9.sx-1tq37w7 300.0x32.0 bg #1b1c1d border T:1px solid #3f4042 / R:1px solid #3f4042 / B:1px solid #3f4042 / L:1px solid #3f4042 r 8px | input.sx-dyb6km.sx-y30hb9.sx-1tq37w7 300.0x32.0 bg #1b1c1d border T:1px solid #363a43 / R:1px solid #363a43 / B:1px solid #363a43 / L:1px solid #363a43 r 8px | input.sx-dyb6km.sx-y30hb9.sx-1tq37w7 300.0x32.0 bg #1b1c1d border T:1px solid #3f4042 / R:1px solid #3f4042 / B:1px solid #3f4042 / L:1px solid #3f4042 r 8px outline 1px solid #5e6ad2 offset -1px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 300 x 32 | = | = |
| Padding | 6px 25px 6px 32px | = | = |
| Border | 1px solid #d3d3d3 | 1px solid #bdbdbd | = |
| Radius | 8px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px solid #6d78d5 offset -1px |
| Font | Inter Variable 13px/normal 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1b1b1b | = | = |
| Transition | border-color 0.15s ease | none | = |
| Cursor | text | = | = |
| Placeholder | "Search by name or email" #5c5c5e, opacity 1, 13px | = | = |
| Painted layers | input.sx-dyb6km.sx-y30hb9.sx-1tq37w7 300.0x32.0 bg #ffffff border T:1px solid #d3d3d3 / R:1px solid #d3d3d3 / B:1px solid #d3d3d3 / L:1px solid #d3d3d3 r 8px | input.sx-dyb6km.sx-y30hb9.sx-1tq37w7 300.0x32.0 bg #ffffff border T:1px solid #bdbdbd / R:1px solid #bdbdbd / B:1px solid #bdbdbd / L:1px solid #bdbdbd r 8px | input.sx-dyb6km.sx-y30hb9.sx-1tq37w7 300.0x32.0 bg #ffffff border T:1px solid #d3d3d3 / R:1px solid #d3d3d3 / B:1px solid #d3d3d3 / L:1px solid #d3d3d3 r 8px outline 1px solid #6d78d5 offset -1px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |

Crops: `search-field-default.png`, `search-field-hover.png`, `search-field-focus-visible.png`, `search-field-light.png`, `search-field-light-hover.png`, `search-field-light-focus-visible.png`.

#### text-area

Text area (composer description). A ProseMirror editor, not a <textarea>; the second editor in the composer.

Page copy: `composer-dark`. Finder: `() => [...document.querySelectorAll('[role=dialog] [contenteditable=true]')].filter((e) => e.getBoundingClientRect().height > 40)[0] // null`.

Dark theme.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 712 x 76 | = |
| Padding | 6px 0px 12px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 15px/22.5px 450 | = |
| Letter spacing | normal | = |
| Colour | #e4e5e7 | = |
| Transition | none | = |
| Cursor | text | = |
| How | at rest | keyboard: focus(), Shift+Tab, Tab |

Light theme.

| Property | light | light-focus-visible |
|---|---|---|
| Size (w x h) | 712 x 76 | = |
| Padding | 6px 0px 12px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 15px/22.5px 450 | = |
| Letter spacing | normal | = |
| Colour | #303032 | = |
| Transition | none | = |
| Cursor | text | = |
| How | at rest | keyboard: focus(), Shift+Tab, Tab |

Crops: `text-area-default.png`, `text-area-focus-visible.png`, `text-area-light.png`, `text-area-light-focus-visible.png`.

#### select

Select trigger (First day of the week).

Page copy: `settings-prefs-dark`, `settings-prefs-dark-select`. Finder: `() => TB('Sunday', M())`.

Dark theme.

| Property | default | hover | focus-visible | pressed | open | option |
|---|---|---|---|---|---|---|
| Size (w x h) | 86.09 x 30 | = | = | = | 119.19 x 232 | 119.19 x 32 |
| Padding | 1px 28px 1px 10px | = | = | = | 0px | 0px 35px 0px 12px |
| Border | 1px solid #000000 @ 0 | = | = | = | none | none |
| Radius | 8px | = | = | = | 12px | 0px |
| Background | #232325 | #2c2d2f | = | #2c2d2f | #28292b | transparent |
| Box shadow | none | = | = | = | #585a5d 0px 0px 0px 0.5px, #000000 @ 0.125 0px 3px 8px 0px, #000000 @ 0.125 0px 2px 5px 0px, #000000 @ 0.125 0px 1px 1px 0px | = |
| Outline | none | = | 1px solid #5e6ad2 offset 0px | = | = | = |
| Font | Inter Variable 13px/normal 400 | = | = | = | Inter Variable 16px/24px 400 | Inter Variable 13px/19.5px 400 |
| Letter spacing | normal | = | = | = | = | = |
| Colour | #e4e5e7 | = | = | = | #ffffff | #e6e7ea |
| Text node | span.sx-uxw1ft.sx-b3r6kr.sx-lyipyv: Inter Variable 13px/normal 400, #e4e5e7 | = | = | = | span.sx-uxw1ft.sx-b3r6kr.sx-lyipyv: Inter Variable 13px/19.5px 400, #e6e7ea | span.sx-uxw1ft.sx-b3r6kr.sx-lyipyv: Inter Variable 13px/19.5px 400, #e6e7ea |
| Transition | background-color, border, color 0.15s ease | none | = | none | none | none |
| Cursor | default | = | = | = | = | = |
| Icon | 10 x 5, colour #e4e5e7, fill #98999c | = | = | = | 16 x 16, colour #e6e7ea, fill #a0a1a4 | - |
| ::after | 84.0938px x 28px, absolute, bg #000000 @ 0, radius 8px, shadow #ffffff @ 0.143 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | 84.0938px x 28px, absolute, bg #000000 @ 0, radius 8px, shadow #ffffff @ 0.238 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | = | 84.0938px x 28px, absolute, bg #000000 @ 0, radius 8px, shadow #ffffff @ 0.238 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | - | - |
| Painted layers | button.sx-1n2onr6.sx-78zum5.sx-9f619 86.1x30.0 bg #232325 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; button.sx-1n2onr6.sx-78zum5.sx-9f619::after 84.0938pxx28px r 8px shadow #ffffff @ 0.143 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | button.sx-1n2onr6.sx-78zum5.sx-9f619 86.1x30.0 bg #2c2d2f border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; button.sx-1n2onr6.sx-78zum5.sx-9f619::after 84.0938pxx28px r 8px shadow #ffffff @ 0.238 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | button.sx-1n2onr6.sx-78zum5.sx-9f619 86.1x30.0 bg #232325 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px outline 1px solid #5e6ad2 offset 0px; button.sx-1n2onr6.sx-78zum5.sx-9f619::after 84.0938pxx28px r 8px shadow #ffffff @ 0.143 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | button.sx-1n2onr6.sx-78zum5.sx-9f619 86.1x30.0 bg #2c2d2f border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; button.sx-1n2onr6.sx-78zum5.sx-9f619::after 84.0938pxx28px r 8px shadow #ffffff @ 0.238 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | div.sx-1lmytr0.sx-8du1vd.sx-1y0btm7 119.2x232.0 bg #28292b r 12px shadow #585a5d 0px 0px 0px 0.5px, #000000 @ 0.125 0px 3px 8px 0px, #000000 @ 0.125 0px 2px 5px 0px, #000000 @ 0.125 0px 1px 1px 0px | - |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down | at rest, captured open | at rest, captured option |
| ::before | - | = | = | = | = | 111.188px x 32px, absolute, bg #000000 @ 0, radius 8px |
| Ancestor paint | - | = | = | = | = | 2 up div.sx-1lmytr0.sx-8du1vd.sx-1y0btm7 bg #28292b shadow #585a5d 0px 0px 0px 0.5px, #000000 @ 0.125 0px 3px 8px 0px, #000000 @ 0.125 0px 2px 5px 0px, #000000 @ 0.125 0px 1px 1px 0px |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed | light-open | light-option |
|---|---|---|---|---|---|---|
| Size (w x h) | 86.09 x 30 | = | = | = | 119.19 x 232 | 119.19 x 32 |
| Padding | 1px 28px 1px 10px | = | = | = | 0px | 0px 35px 0px 12px |
| Border | 1px solid #000000 @ 0 | = | = | = | none | none |
| Radius | 8px | = | = | = | 12px | 0px |
| Background | #ffffff | #f3f3f3 | = | #f3f3f3 | = | transparent |
| Box shadow | none | = | = | = | #d8d8d8 0px 0px 0px 0.5px, #000000 @ 0.02 0px 6px 18px 0px, #000000 @ 0.04 0px 3px 9px 0px, #000000 @ 0.04 0px 1px 1px 0px | = |
| Outline | none | = | 1px solid #6d78d5 offset 0px | = | = | = |
| Font | Inter Variable 13px/normal 400 | = | = | = | Inter Variable 16px/24px 400 | Inter Variable 13px/19.5px 400 |
| Letter spacing | normal | = | = | = | = | = |
| Colour | #303032 | = | = | = | #000000 | = |
| Text node | span.sx-uxw1ft.sx-b3r6kr.sx-lyipyv: Inter Variable 13px/normal 400, #303032 | = | = | = | span.sx-uxw1ft.sx-b3r6kr.sx-lyipyv: Inter Variable 13px/19.5px 400, #303032 | span.sx-uxw1ft.sx-b3r6kr.sx-lyipyv: Inter Variable 13px/19.5px 400, #303032 |
| Transition | background-color, border, color 0.15s ease | none | = | none | none | none |
| Cursor | default | = | = | = | = | = |
| Icon | 10 x 5, colour #303032, fill #5e5e60 | = | = | = | 16 x 16, colour #303032, fill #5e5e60 | - |
| ::after | 84.0938px x 28px, absolute, bg #000000 @ 0, radius 8px, shadow #000000 @ 0.088 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | 84.0938px x 28px, absolute, bg #000000 @ 0, radius 8px, shadow #000000 @ 0.147 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | = | 84.0938px x 28px, absolute, bg #000000 @ 0, radius 8px, shadow #000000 @ 0.147 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | - | - |
| Painted layers | button.sx-1n2onr6.sx-78zum5.sx-9f619 86.1x30.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; button.sx-1n2onr6.sx-78zum5.sx-9f619::after 84.0938pxx28px r 8px shadow #000000 @ 0.088 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | button.sx-1n2onr6.sx-78zum5.sx-9f619 86.1x30.0 bg #f3f3f3 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; button.sx-1n2onr6.sx-78zum5.sx-9f619::after 84.0938pxx28px r 8px shadow #000000 @ 0.147 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | button.sx-1n2onr6.sx-78zum5.sx-9f619 86.1x30.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px outline 1px solid #6d78d5 offset 0px; button.sx-1n2onr6.sx-78zum5.sx-9f619::after 84.0938pxx28px r 8px shadow #000000 @ 0.088 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | button.sx-1n2onr6.sx-78zum5.sx-9f619 86.1x30.0 bg #f3f3f3 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; button.sx-1n2onr6.sx-78zum5.sx-9f619::after 84.0938pxx28px r 8px shadow #000000 @ 0.147 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | div.sx-1lmytr0.sx-8du1vd.sx-1y0btm7 119.2x232.0 bg #ffffff r 12px shadow #d8d8d8 0px 0px 0px 0.5px, #000000 @ 0.02 0px 6px 18px 0px, #000000 @ 0.04 0px 3px 9px 0px, #000000 @ 0.04 0px 1px 1px 0px | - |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down | at rest, captured open | at rest, captured option |
| ::before | - | = | = | = | = | 111.188px x 32px, absolute, bg #000000 @ 0, radius 8px |
| Ancestor paint | - | = | = | = | = | 2 up div.sx-1lmytr0.sx-8du1vd.sx-1y0btm7 bg #ffffff shadow #d8d8d8 0px 0px 0px 0.5px, #000000 @ 0.02 0px 6px 18px 0px, #000000 @ 0.04 0px 3px 9px 0px, #000000 @ 0.04 0px 1px 1px 0px |

Other finders: open: `() => SHD(Q('[role=listbox]'))`; option: `() => Q('[role=listbox] [role=option]', 2)`; light-open: `() => SHD(Q('[role=listbox]'))`; light-option: `() => Q('[role=listbox] [role=option]', 2)`.

Crops: `select-default.png`, `select-hover.png`, `select-focus-visible.png`, `select-pressed.png`, `select-open.png`, `select-option.png`, `select-light.png`, `select-light-hover.png`, `select-light-focus-visible.png`, `select-light-pressed.png`, `select-light-open.png`, `select-light-option.png`.

#### checkbox

Checkbox (members table row). Opacity 0 in every copy: Linear reveals the row checkbox by script on row hover or selection, which a static copy cannot replay. Geometry only.

Page copy: `settings-members-dark`. Finder: `() => document.querySelector('main input[type=checkbox]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 12 x 12 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 13.3333px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Opacity | 0 |
| Cursor | default |
| Placeholder | "" #ffffff, opacity 1, 13.3333px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 12 x 12 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 13.3333px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Opacity | 0 |
| Cursor | default |
| Placeholder | "" #000000, opacity 1, 13.3333px |
| How | at rest |

Crops: none.

#### switch

Switch, on. An <input type=checkbox> with appearance none.

Page copy: `settings-prefs-dark`. Finder: `() => Q('main input[type=checkbox]:checked')`.

Dark theme.

| Property | default | hover | focus-visible | off | off-hover |
|---|---|---|---|---|---|
| Size (w x h) | 30 x 20 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 72px | = | = | = | = |
| Background | #5e6ad2 | #6975e2 | = | #707172 | #868789 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px solid #5e6ad2 offset 2px | = | = |
| Font | Inter Variable 13.3333px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | = | = | = | = |
| Transition | background-color, opacity 0.15s ease-out | = | = | = | = |
| Cursor | default | = | = | = | = |
| Placeholder | "" #ffffff, opacity 1, 13.3333px | = | = | = | = |
| ::before | 42px x 32px, absolute, bg #000000 @ 0, radius 0px | = | = | = | = |
| ::after | 14px x 14px, absolute, bg #fffeff, radius 7px | 16px x 14px, absolute, bg #fffeff, radius 7px | = | = | 16px x 14px, absolute, bg #fffeff, radius 7px |
| Painted layers | input.sx-jyslct.sx-c342km.sx-2lah0s 30.0x20.0 bg #5e6ad2 r 72px; input.sx-jyslct.sx-c342km.sx-2lah0s::after 14pxx14px bg #fffeff r 7px | input.sx-jyslct.sx-c342km.sx-2lah0s 30.0x20.0 bg #6975e2 r 72px; input.sx-jyslct.sx-c342km.sx-2lah0s::after 16pxx14px bg #fffeff r 7px | input.sx-jyslct.sx-c342km.sx-2lah0s 30.0x20.0 bg #5e6ad2 r 72px outline 1px solid #5e6ad2 offset 2px; input.sx-jyslct.sx-c342km.sx-2lah0s::after 14pxx14px bg #fffeff r 7px | input.sx-jyslct.sx-c342km.sx-2lah0s 30.0x20.0 bg #707172 r 72px; input.sx-jyslct.sx-c342km.sx-2lah0s::after 14pxx14px bg #fffeff r 7px | input.sx-jyslct.sx-c342km.sx-2lah0s 30.0x20.0 bg #868789 r 72px; input.sx-jyslct.sx-c342km.sx-2lah0s::after 16pxx14px bg #fffeff r 7px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | at rest, captured off | mouse hover |

Light theme.

| Property | light | light-hover | light-focus-visible | light-off | light-off-hover |
|---|---|---|---|---|---|
| Size (w x h) | 30 x 20 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 72px | = | = | = | = |
| Background | #6d78d5 | #5e6ac1 | = | #cdcdcd | #bebebe |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px solid #6d78d5 offset 2px | = | = |
| Font | Inter Variable 13.3333px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Transition | background-color, opacity 0.15s ease-out | = | = | = | = |
| Cursor | default | = | = | = | = |
| Placeholder | "" #000000, opacity 1, 13.3333px | = | = | = | = |
| ::before | 42px x 32px, absolute, bg #000000 @ 0, radius 0px | = | = | = | = |
| ::after | 14px x 14px, absolute, bg #fffeff, radius 7px | 16px x 14px, absolute, bg #fffeff, radius 7px | = | = | 16px x 14px, absolute, bg #fffeff, radius 7px |
| Painted layers | input.sx-jyslct.sx-c342km.sx-2lah0s 30.0x20.0 bg #6d78d5 r 72px; input.sx-jyslct.sx-c342km.sx-2lah0s::after 14pxx14px bg #fffeff r 7px | input.sx-jyslct.sx-c342km.sx-2lah0s 30.0x20.0 bg #5e6ac1 r 72px; input.sx-jyslct.sx-c342km.sx-2lah0s::after 16pxx14px bg #fffeff r 7px | input.sx-jyslct.sx-c342km.sx-2lah0s 30.0x20.0 bg #6d78d5 r 72px outline 1px solid #6d78d5 offset 2px; input.sx-jyslct.sx-c342km.sx-2lah0s::after 14pxx14px bg #fffeff r 7px | input.sx-jyslct.sx-c342km.sx-2lah0s 30.0x20.0 bg #cdcdcd r 72px; input.sx-jyslct.sx-c342km.sx-2lah0s::after 14pxx14px bg #fffeff r 7px | input.sx-jyslct.sx-c342km.sx-2lah0s 30.0x20.0 bg #bebebe r 72px; input.sx-jyslct.sx-c342km.sx-2lah0s::after 16pxx14px bg #fffeff r 7px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | at rest, captured off | mouse hover |

Other finders: off: `() => Q('main input[type=checkbox]:not(:checked)')`; off-hover: `() => Q('main input[type=checkbox]:not(:checked)')`; light-off: `() => Q('main input[type=checkbox]:not(:checked)')`; light-off-hover: `() => Q('main input[type=checkbox]:not(:checked)')`.

Crops: `switch-default.png`, `switch-hover.png`, `switch-focus-visible.png`, `switch-off.png`, `switch-off-hover.png`, `switch-light.png`, `switch-light-hover.png`, `switch-light-focus-visible.png`, `switch-light-off.png`, `switch-light-off-hover.png`.

### Navigation

#### tab

View tab (pill).

Page copy: `issues-board-dark`. Finder: `() => TB('Active', M())`.

Dark theme.

| Property | default | hover | focus-visible | pressed | selected |
|---|---|---|---|---|---|
| Size (w x h) | 58.16 x 28 | = | = | = | 76.44 x 28 |
| Padding | 0px 10px | = | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | #1c1c1d | #232424 | = | #232424 | #29292b |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px solid #5e6ad2 offset -1px | = | = |
| Font | Inter Variable 12px/normal 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #959597 | #e3e4e6 | = | #e3e4e6 | #ffffff |
| Text node | div.sx-uxw1ft.sx-b3r6kr.sx-lyipyv: Inter Variable 12px/normal 500, #959597 | div.sx-uxw1ft.sx-b3r6kr.sx-lyipyv: Inter Variable 12px/normal 500, #e3e4e6 | = | div.sx-uxw1ft.sx-b3r6kr.sx-lyipyv: Inter Variable 12px/normal 500, #e3e4e6 | div.sx-uxw1ft.sx-b3r6kr.sx-lyipyv: Inter Variable 12px/normal 500, #ffffff |
| Transition | border, background-color, color, opacity 0.15s ease | none | = | none | = |
| Cursor | default | = | = | = | = |
| ::after | 56.1562px x 26px, absolute, bg #000000 @ 0, radius 9999px, shadow #ffffff @ 0.137 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | 56.1562px x 26px, absolute, bg #000000 @ 0, radius 9999px, shadow #ffffff @ 0.229 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | = | 56.1562px x 26px, absolute, bg #000000 @ 0, radius 9999px, shadow #ffffff @ 0.229 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | 74.4375px x 26px, absolute, bg #000000 @ 0, radius 9999px, shadow #ffffff @ 0.137 0px 0px 0px 0.5px, #000000 @ 0 0px 0px 0px 0px |
| Painted layers | a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 58.2x28.0 bg #1c1c1d border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 56.1562pxx26px r 9999px shadow #ffffff @ 0.137 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 58.2x28.0 bg #232424 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 56.1562pxx26px r 9999px shadow #ffffff @ 0.229 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 58.2x28.0 bg #1c1c1d border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px outline 1px solid #5e6ad2 offset -1px; a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 56.1562pxx26px r 9999px shadow #ffffff @ 0.137 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 58.2x28.0 bg #232424 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 56.1562pxx26px r 9999px shadow #ffffff @ 0.229 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 76.4x28.0 bg #29292b border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 74.4375pxx26px r 9999px shadow #ffffff @ 0.137 0px 0px 0px 0.5px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down | at rest, captured selected |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed | light-selected |
|---|---|---|---|---|---|
| Size (w x h) | 58.16 x 28 | = | = | = | 76.44 x 28 |
| Padding | 0px 10px | = | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | #ffffff | #f0f0f1 | = | #f0f0f1 | #ececed |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px solid #6d78d5 offset -1px | = | = |
| Font | Inter Variable 12px/normal 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #5c5c5e | #2f2f31 | = | #2f2f31 | #1b1b1b |
| Text node | div.sx-uxw1ft.sx-b3r6kr.sx-lyipyv: Inter Variable 12px/normal 500, #5c5c5e | div.sx-uxw1ft.sx-b3r6kr.sx-lyipyv: Inter Variable 12px/normal 500, #2f2f31 | = | div.sx-uxw1ft.sx-b3r6kr.sx-lyipyv: Inter Variable 12px/normal 500, #2f2f31 | div.sx-uxw1ft.sx-b3r6kr.sx-lyipyv: Inter Variable 12px/normal 500, #1b1b1b |
| Transition | border, background-color, color, opacity 0.15s ease | none | = | none | = |
| Cursor | default | = | = | = | = |
| ::after | 56.1562px x 26px, absolute, bg #000000 @ 0, radius 9999px, shadow #000000 @ 0.09 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | 56.1562px x 26px, absolute, bg #000000 @ 0, radius 9999px, shadow #000000 @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | = | 56.1562px x 26px, absolute, bg #000000 @ 0, radius 9999px, shadow #000000 @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | 74.4375px x 26px, absolute, bg #000000 @ 0, radius 9999px, shadow #000000 @ 0.09 0px 0px 0px 0.5px, #000000 @ 0 0px 0px 0px 0px |
| Painted layers | a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 58.2x28.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 56.1562pxx26px r 9999px shadow #000000 @ 0.09 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 58.2x28.0 bg #f0f0f1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 56.1562pxx26px r 9999px shadow #000000 @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 58.2x28.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px outline 1px solid #6d78d5 offset -1px; a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 56.1562pxx26px r 9999px shadow #000000 @ 0.09 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 58.2x28.0 bg #f0f0f1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 56.1562pxx26px r 9999px shadow #000000 @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 76.4x28.0 bg #ececed border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 74.4375pxx26px r 9999px shadow #000000 @ 0.09 0px 0px 0px 0.5px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down | at rest, captured selected |

Other finders: selected: `() => TB('All issues', M())`; light-selected: `() => TB('All issues', M())`.

Crops: `tab-default.png`, `tab-hover.png`, `tab-focus-visible.png`, `tab-pressed.png`, `tab-selected.png`, `tab-light.png`, `tab-light-hover.png`, `tab-light-focus-visible.png`, `tab-light-pressed.png`, `tab-light-selected.png`.

#### nav-item

Sidebar item.

Page copy: `issues-board-dark`. Finder: `() => TB('Inbox')`.

Dark theme.

| Property | default | hover | focus-visible | pressed | selected |
|---|---|---|---|---|---|
| Size (w x h) | 220 x 28 | = | = | = | 201 x 28 |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 8px | = | = | = | = |
| Background | transparent | #18181a | = | #18181a | #232325 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px solid #5e6ad2 offset -1px | = | = |
| Font | Inter Variable 16px/24px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | = | = | = | = |
| Text node | span: Inter Variable 13px/normal 500, #929294 | span: Inter Variable 13px/normal 500, #ffffff | = | span: Inter Variable 13px/normal 500, #ffffff | span.sx-1j61x8r.sx-ggjnk3.sx-1srpx65: Inter Variable 13px/normal 500, #ffffff |
| Transition | color 0.15s ease | none | = | none | = |
| Cursor | default | = | = | = | = |
| Icon | 14 x 14, colour #929294 | 14 x 14, colour #ffffff | = | 14 x 14, colour #ffffff | 14 x 14, colour #ffffff |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down | at rest, captured selected |
| Painted layers | - | a.sx-6s0dn4.sx-1i9j6mr.sx-vijh9v 220.0x28.0 bg #18181a r 8px | a.sx-6s0dn4.sx-1i9j6mr.sx-vijh9v 220.0x28.0 r 8px outline 1px solid #5e6ad2 offset -1px | a.sx-6s0dn4.sx-1i9j6mr.sx-vijh9v 220.0x28.0 bg #18181a r 8px | a.sx-6s0dn4.sx-1i9j6mr.sx-vijh9v 201.0x28.0 bg #232325 r 8px |
| ::before | - | = | = | = | 239px x 28px, absolute, bg #000000 @ 0, radius 0px |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed | light-selected |
|---|---|---|---|---|---|
| Size (w x h) | 220 x 28 | = | = | = | 201 x 28 |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 8px | = | = | = | = |
| Background | transparent | #e7e7e8 | = | #e7e7e8 | #e1e1e2 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px solid #6d78d5 offset -1px | = | = |
| Font | Inter Variable 16px/24px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #1b1b1b | = | = | = | #1a1a1a |
| Text node | span: Inter Variable 13px/normal 500, #59595b | span: Inter Variable 13px/normal 500, #1a1a1a | = | span: Inter Variable 13px/normal 500, #1a1a1a | span.sx-1j61x8r.sx-ggjnk3.sx-1srpx65: Inter Variable 13px/normal 500, #1a1a1a |
| Transition | color 0.15s ease | none | = | none | = |
| Cursor | default | = | = | = | = |
| Icon | 14 x 14, colour #59595b | 14 x 14, colour #1a1a1a | = | 14 x 14, colour #1a1a1a | 14 x 14, colour #1a1a1a |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse hover, then held down | at rest, captured selected |
| Painted layers | - | a.sx-6s0dn4.sx-1i9j6mr.sx-vijh9v 220.0x28.0 bg #e7e7e8 r 8px | a.sx-6s0dn4.sx-1i9j6mr.sx-vijh9v 220.0x28.0 r 8px outline 1px solid #6d78d5 offset -1px | a.sx-6s0dn4.sx-1i9j6mr.sx-vijh9v 220.0x28.0 bg #e7e7e8 r 8px | a.sx-6s0dn4.sx-1i9j6mr.sx-vijh9v 201.0x28.0 bg #e1e1e2 r 8px |
| ::before | - | = | = | = | 239px x 28px, absolute, bg #000000 @ 0, radius 0px |

Other finders: selected: `() => painted([...document.querySelectorAll('a')].filter((a) => a.getBoundingClientRect().x < 60 && a.getBoundingClientRect().width > 150))`; light-selected: `() => painted([...document.querySelectorAll('a')].filter((a) => a.getBoundingClientRect().x < 60 && a.getBoundingClientRect().width > 150))`.

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`, `nav-item-selected.png`, `nav-item-light.png`, `nav-item-light-hover.png`, `nav-item-light-focus-visible.png`, `nav-item-light-pressed.png`, `nav-item-light-selected.png`.

### Overlays

#### menu

Menu (status picker).

Page copy: `issue-dark-menu`. Finder: `() => SHD(Q('[role=listbox]'))`.

Dark theme.

| Property | default | option-highlighted | option |
|---|---|---|---|
| Size (w x h) | 208 x 273.5 | 194 x 32 | 206 x 32 |
| Padding | 0px | = | 0px 18px 0px 14px |
| Border | 1px solid #3c3d40 | none | none |
| Radius | 12px | 8px | 0px |
| Background | #212122 | #313234 | transparent |
| Box shadow | #000000 @ 0.125 0px 3px 8px 0px, #000000 @ 0.125 0px 2px 5px 0px, #000000 @ 0.125 0px 1px 1px 0px | none | none |
| Outline | none | = | = |
| Font | Inter Variable 13px/19.5px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #e5e6e8 | #ffffff | = |
| Text node | kbd.sx-1rg5ohu.sx-11njtxf.sx-2b8uid: Inter Variable 11px/12.1px 400, #9c9d9f | - | span.sx-s83m0k.sx-euugli.sx-193iq5w: Inter Variable 13px/normal 450, #e5e6e8 |
| Transition | none | = | = |
| Cursor | default | = | = |
| Icon | 14 x 14, colour #e5e6e8, fill #bec2c8 | - | 14 x 14, colour #e5e6e8, fill #5e6ad2 |
| Placeholder | "Change status…" #9c9d9f, opacity 1, 13px | - | - |
| Painted layers | div.sx-1lmytr0.sx-8du1vd.sx-1uvtmcs 208.0x273.5 bg #212122 border T:1px solid #3c3d40 / R:1px solid #3c3d40 / B:1px solid #3c3d40 / L:1px solid #3c3d40 r 12px shadow #000000 @ 0.125 0px 3px 8px 0px, #000000 @ 0.125 0px 2px 5px 0px, #000000 @ 0.125 0px 1px 1px 0px; div.sx-zjhap9.sx-nuq7ks.sx-pktdlk 206.0x37.0 border B:1px solid #303134; kbd.sx-1rg5ohu.sx-11njtxf.sx-2b8uid 18.0x18.1 border T:1px solid #303134 / R:1px solid #303134 / B:1px solid #303134 / L:1px solid #303134 r 4px; div.sx-78zum5.sx-dt5ytf.sx-pktdlk 206.0x234.5 bg #000000 @ 0.004; ul.sx-1ghz6dp.sx-g0xzth.sx-5yr21d 206.0x236.0 bg #000000 @ 0.004; div.sx-10l6tqk.sx-13vifvy.sx-clnmbr 194.0x32.0 bg #313234 r 8px | div.sx-10l6tqk.sx-13vifvy.sx-clnmbr 194.0x32.0 bg #313234 r 8px | - |
| How | at rest | at rest, captured option-highlighted | at rest, captured option |

Light theme.

| Property | light | light-option-highlighted | light-option |
|---|---|---|---|
| Size (w x h) | 208 x 273.5 | 194 x 32 | 206 x 32 |
| Padding | 0px | = | 0px 18px 0px 14px |
| Border | 1px solid #e8e8e8 | none | none |
| Radius | 12px | 8px | 0px |
| Background | #ffffff | #f1f1f1 | transparent |
| Box shadow | #000000 @ 0.02 0px 6px 18px 0px, #000000 @ 0.04 0px 3px 9px 0px, #000000 @ 0.04 0px 1px 1px 0px | none | none |
| Outline | none | = | = |
| Font | Inter Variable 13px/19.5px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #303032 | #1b1b1b | = |
| Text node | kbd.sx-1rg5ohu.sx-11njtxf.sx-2b8uid: Inter Variable 11px/12.1px 400, #5e5e60 | - | span.sx-s83m0k.sx-euugli.sx-193iq5w: Inter Variable 13px/normal 450, #303032 |
| Transition | none | = | = |
| Cursor | default | = | = |
| Icon | 14 x 14, colour #303032, fill #a2a6ac | - | 14 x 14, colour #303032, fill #5e6ad2 |
| Placeholder | "Change status…" #5e5e60, opacity 1, 13px | - | - |
| Painted layers | div.sx-1lmytr0.sx-8du1vd.sx-1uvtmcs 208.0x273.5 bg #ffffff border T:1px solid #e8e8e8 / R:1px solid #e8e8e8 / B:1px solid #e8e8e8 / L:1px solid #e8e8e8 r 12px shadow #000000 @ 0.02 0px 6px 18px 0px, #000000 @ 0.04 0px 3px 9px 0px, #000000 @ 0.04 0px 1px 1px 0px; div.sx-zjhap9.sx-nuq7ks.sx-pktdlk 206.0x37.0 border B:1px solid #e8e8e8; kbd.sx-1rg5ohu.sx-11njtxf.sx-2b8uid 18.0x18.1 border T:1px solid #e8e8e8 / R:1px solid #e8e8e8 / B:1px solid #e8e8e8 / L:1px solid #e8e8e8 r 4px; div.sx-78zum5.sx-dt5ytf.sx-pktdlk 206.0x234.5 bg #ffffff @ 0; ul.sx-1ghz6dp.sx-g0xzth.sx-5yr21d 206.0x236.0 bg #ffffff @ 0; div.sx-10l6tqk.sx-13vifvy.sx-clnmbr 194.0x32.0 bg #f1f1f1 r 8px | div.sx-10l6tqk.sx-13vifvy.sx-clnmbr 194.0x32.0 bg #f1f1f1 r 8px | - |
| How | at rest | at rest, captured option-highlighted | at rest, captured option |

Other finders: option-highlighted: `() => HL()`; option: `() => Q('[role=listbox] [role=option]', 4)`; light-option-highlighted: `() => HL()`; light-option: `() => Q('[role=listbox] [role=option]', 4)`.

Crops: `menu-default.png`, `menu-option-highlighted.png`, `menu-option.png`, `menu-light.png`, `menu-light-option-highlighted.png`, `menu-light-option.png`.

#### tooltip

Tooltip.

Page copy: `issue-dark-tooltip`. Finder: `() => { const host = [...document.body.children].filter((c) => /Copy issue URL/.test(c.textContent)).pop(); const t = host && [...host.querySelectorAll('*')].find((e) => /Copy issue URL/.test(e.textContent) && getComputedStyle(e).backgroundColor !== 'rgba(0, 0, 0, 0)'); return t // null; }`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 168.45 x 29.09 |
| Padding | 0px |
| Border | 1px solid #3c3d40 |
| Radius | 8px |
| Background | #212122 |
| Box shadow | #000000 @ 0.3 0px 0.5px 1px 1px |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.sx-1nzvdvg: Inter Variable 11px/16.5px 450, #e5e6e8 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Cursor | default |
| Painted layers | div.sx-1lmytr0.sx-8du1vd.sx-1uvtmcs 168.5x29.1 bg #212122 border T:1px solid #3c3d40 / R:1px solid #3c3d40 / B:1px solid #3c3d40 / L:1px solid #3c3d40 r 8px shadow #000000 @ 0.3 0px 0.5px 1px 1px; kbd.sx-1rg5ohu.sx-11njtxf.sx-2b8uid 18.0x18.1 border T:1px solid #303134 / R:1px solid #303134 / B:1px solid #303134 / L:1px solid #303134 r 4px; kbd.sx-1rg5ohu.sx-11njtxf.sx-2b8uid 18.0x18.1 border T:1px solid #303134 / R:1px solid #303134 / B:1px solid #303134 / L:1px solid #303134 r 4px; kbd.sx-1rg5ohu.sx-11njtxf.sx-2b8uid 18.0x18.1 border T:1px solid #303134 / R:1px solid #303134 / B:1px solid #303134 / L:1px solid #303134 r 4px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 168.45 x 29.09 |
| Padding | 0px |
| Border | 1px solid #e8e8e8 |
| Radius | 8px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.sx-1nzvdvg: Inter Variable 11px/16.5px 450, #303032 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Cursor | default |
| Painted layers | div.sx-1lmytr0.sx-8du1vd.sx-1uvtmcs 168.5x29.1 bg #ffffff border T:1px solid #e8e8e8 / R:1px solid #e8e8e8 / B:1px solid #e8e8e8 / L:1px solid #e8e8e8 r 8px shadow #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px; kbd.sx-1rg5ohu.sx-11njtxf.sx-2b8uid 18.0x18.1 border T:1px solid #e8e8e8 / R:1px solid #e8e8e8 / B:1px solid #e8e8e8 / L:1px solid #e8e8e8 r 4px; kbd.sx-1rg5ohu.sx-11njtxf.sx-2b8uid 18.0x18.1 border T:1px solid #e8e8e8 / R:1px solid #e8e8e8 / B:1px solid #e8e8e8 / L:1px solid #e8e8e8 r 4px; kbd.sx-1rg5ohu.sx-11njtxf.sx-2b8uid 18.0x18.1 border T:1px solid #e8e8e8 / R:1px solid #e8e8e8 / B:1px solid #e8e8e8 / L:1px solid #e8e8e8 r 4px |
| How | at rest |

Crops: `tooltip-default.png`, `tooltip-light.png`.

#### dialog

Dialog (new issue composer).

Page copy: `composer-dark`. Finder: `() => BOX(Q('[role=dialog] button[type=submit]'), 600, 200)`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 750 x 259 |
| Padding | 0px |
| Border | 1px solid #343538 |
| Radius | 21px |
| Background | #1a1a1b |
| Box shadow | #000000 @ 0.1 0px 4px 40px 0px, #000000 @ 0.125 0px 3px 20px 0px, #000000 @ 0.125 0px 3px 12px 0px, #000000 @ 0.125 0px 2px 8px 0px, #000000 @ 0.125 0px 1px 1px 0px |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #e4e5e7 |
| Text node | div.sx-3nfvp2.sx-l56j7k.sx-6s0dn4: Apple Color Emoji 11px/12px 500, #9c9da0 |
| Transition | max-width, background-color 0.22s, 0.1s cubic-bezier(0.43, 0.07, 0.59, 0.94) |
| Cursor | default |
| Icon | 14 x 14, colour #e5e6e9, fill #9c9da0 |
| Placeholder | "" #e4e5e7, opacity 1, 13.3333px |
| Painted layers | div.sx-1lmytr0.sx-xbqdvw.sx-78zum5 750.0x259.0 bg #1a1a1b border T:1px solid #343538 / R:1px solid #343538 / B:1px solid #343538 / L:1px solid #343538 r 21px shadow #000000 @ 0.1 0px 4px 40px 0px, #000000 @ 0.125 0px 3px 20px 0px, #000000 @ 0.125 0px 3px 12px 0px, #000000 @ 0.125 0px 2px 8px 0px, #000000 @ 0.125 0px 1px 1px 0px; button.sx-3nfvp2.sx-16dsc37.sx-l56j7k 66.0x24.0 bg #2a2b2d border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px opacity 0.6; button.sx-3nfvp2.sx-16dsc37.sx-l56j7k::after 63.9531pxx22px r 9999px shadow #ffffff @ 0.149 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 28.0x28.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 28.0x28.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-l56j7k 79.8x24.0 bg #2a2b2d border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 750 x 259 |
| Padding | 0px |
| Border | 1px solid #e8e8e8 |
| Radius | 21px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.08 0px 9px 48px 0px, #000000 @ 0.1 0px 6px 24px 0px, #000000 @ 0.04 0px 1px 1px 0px |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #303032 |
| Text node | div.sx-3nfvp2.sx-l56j7k.sx-6s0dn4: Apple Color Emoji 11px/12px 500, #5e5e60 |
| Transition | max-width, background-color 0.22s, 0.1s cubic-bezier(0.43, 0.07, 0.59, 0.94) |
| Cursor | default |
| Icon | 14 x 14, colour #303032, fill #5e5e60 |
| Placeholder | "" #303032, opacity 1, 13.3333px |
| Painted layers | div.sx-1lmytr0.sx-xbqdvw.sx-78zum5 750.0x259.0 bg #ffffff border T:1px solid #e8e8e8 / R:1px solid #e8e8e8 / B:1px solid #e8e8e8 / L:1px solid #e8e8e8 r 21px shadow #000000 @ 0.08 0px 9px 48px 0px, #000000 @ 0.1 0px 6px 24px 0px, #000000 @ 0.04 0px 1px 1px 0px; button.sx-3nfvp2.sx-16dsc37.sx-l56j7k 66.0x24.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px opacity 0.6; button.sx-3nfvp2.sx-16dsc37.sx-l56j7k::after 63.9531pxx22px r 9999px shadow #000000 @ 0.088 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 28.0x28.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 28.0x28.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-l56j7k 79.8x24.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest |

Crops: `dialog-default.png`, `dialog-light.png`.

#### dialog-scrim

Dialog scrim. The full-window layer behind the composer.

Page copy: `composer-dark`. Finder: `() => [...document.querySelectorAll('[role=dialog], [role=dialog] *, body > div *')].find((e) => { const r = e.getBoundingClientRect(); const c = getComputedStyle(e); return r.width >= innerWidth - 1 && r.height >= innerHeight - 1 && c.backgroundColor !== 'rgba(0, 0, 0, 0)' && !e.closest('main'); }) // null`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 @ 0.4 |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Opacity | 0.95 |
| Cursor | default |
| Painted layers | div.sx-13vifvy.sx-u96u03.sx-3m8u43 1440.0x900.0 bg #000000 @ 0.4 opacity 0.95 |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 @ 0.25 |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Opacity | 0.645035 |
| Cursor | default |
| Painted layers | div.sx-13vifvy.sx-u96u03.sx-3m8u43 1440.0x900.0 bg #000000 @ 0.25 opacity 0.645035 |
| How | at rest |

Crops: none.

#### toast

Toast.

Page copy: `issue-dark-toast`. Finder: `() => BOX(T('Copied issue link to clipboard'), 200, 30)`.

Dark theme.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 384 x 42 | = |
| Padding | 0px | = |
| Border | 1px solid #000000 @ 0 | = |
| Radius | 12px | = |
| Background | #212122 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 13px/19.5px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-1srpx65: ui-sans-serif 13px/normal 500, #ffffff | = |
| Transition | none | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = |
| Cursor | default | = |
| Icon | 16 x 16, colour #ffffff, fill #9c9d9f | = |
| ::after | 382px x 40px, absolute, bg #000000 @ 0, radius 12px, shadow #ffffff @ 0.148 0px 0px 0px 0.5px, #000000 @ 0.125 0px 3px 8px 0px, #000000 @ 0.125 0px 2px 5px 0px, #000000 @ 0.125 0px 1px 1px 0px | = |
| Painted layers | div.sx-1lmytr0.sx-8du1vd.sx-1onz0r3 384.0x42.0 bg #212122 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px; div.sx-1lmytr0.sx-8du1vd.sx-1onz0r3::after 382pxx40px r 12px shadow #ffffff @ 0.148 0px 0px 0px 0.5px, #000000 @ 0.125 0px 3px 8px 0px, #000000 @ 0.125 0px 2px 5px 0px, #000000 @ 0.125 0px 1px 1px 0px | = |
| How | at rest | mouse hover |

Light theme.

| Property | light | light-hover |
|---|---|---|
| Size (w x h) | 384 x 42 | = |
| Padding | 0px | = |
| Border | 1px solid #000000 @ 0 | = |
| Radius | 12px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 13px/19.5px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-1srpx65: ui-sans-serif 13px/normal 500, #1b1b1b | = |
| Transition | none | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = |
| Cursor | default | = |
| Icon | 16 x 16, colour #000000, fill #5e5e60 | = |
| ::after | 382px x 40px, absolute, bg #000000 @ 0, radius 12px, shadow #000000 @ 0.088 0px 0px 0px 0.5px, #000000 @ 0.02 0px 6px 18px 0px, #000000 @ 0.04 0px 3px 9px 0px, #000000 @ 0.04 0px 1px 1px 0px | = |
| Painted layers | div.sx-1lmytr0.sx-8du1vd.sx-1onz0r3 384.0x42.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px; div.sx-1lmytr0.sx-8du1vd.sx-1onz0r3::after 382pxx40px r 12px shadow #000000 @ 0.088 0px 0px 0px 0.5px, #000000 @ 0.02 0px 6px 18px 0px, #000000 @ 0.04 0px 3px 9px 0px, #000000 @ 0.04 0px 1px 1px 0px | = |
| How | at rest | mouse hover |

Crops: `toast-default.png`, `toast-hover.png`, `toast-light.png`, `toast-light-hover.png`.

### Lists

#### card

Board card.

Page copy: `issues-board-dark`. Finder: `() => Q('[data-board-item]')`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 322 x 117 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | #1a1a1b | = | = |
| Box shadow | #ffffff @ 0.083 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px | = | = |
| Outline | none | = | = |
| Font | Inter Variable 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Text node | span.sx-1rg5ohu.sx-uxw1ft.sx-cwjd09: Inter Variable 12px/normal 450, #98999c, ls -0.24px | = | = |
| Transition | background-color 0.1s ease | = | = |
| Cursor | default | = | = |
| Icon | 14 x 14, colour #ffffff | = | = |
| Painted layers | a.sx-78zum5.sx-6s0dn4.sx-1n2onr6 322.0x117.0 bg #1a1a1b r 8px shadow #ffffff @ 0.083 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px; div.sx-78zum5.sx-dt5ytf.sx-l56j7k::before 322pxx117px bg #212223 r 8px opacity 0; div.sx-vx4679.sx-1q0g3np.sx-1ja2u2z 25.0x24.0 bg #1a1a1b border T:1px solid #2f3033 / R:1px solid #2f3033 / B:1px solid #2f3033 / L:1px solid #2f3033 r 48px; div.sx-vx4679.sx-1q0g3np.sx-1ja2u2z 125.4x24.0 bg #1a1a1b border T:1px solid #2f3033 / R:1px solid #2f3033 / B:1px solid #2f3033 / L:1px solid #2f3033 r 48px; div.sx-16rqkct.sx-2lah0s.sx-1wc42o8 9.0x9.0 bg #eb5757 r 50%; div.sx-vx4679.sx-1q0g3np.sx-1ja2u2z 92.8x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 48px | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 322 x 117 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | #ffffff | = | = |
| Box shadow | #000000 @ 0.088 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | = | = |
| Outline | none | = | = |
| Font | Inter Variable 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1b1b1b | = | = |
| Text node | span.sx-1rg5ohu.sx-uxw1ft.sx-cwjd09: Inter Variable 12px/normal 450, #5e5e60, ls -0.24px | = | = |
| Transition | background-color 0.1s ease | = | = |
| Cursor | default | = | = |
| Icon | 14 x 14, colour #1b1b1b | = | = |
| Painted layers | a.sx-78zum5.sx-6s0dn4.sx-1n2onr6 322.0x117.0 bg #ffffff r 8px shadow #000000 @ 0.088 0px 0px 0px 0.5px, #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px; div.sx-78zum5.sx-dt5ytf.sx-l56j7k::before 322pxx117px bg #f5f5f5 r 8px opacity 0; div.sx-vx4679.sx-1q0g3np.sx-1ja2u2z 25.0x24.0 bg #ffffff border T:1px solid #d8d8d8 / R:1px solid #d8d8d8 / B:1px solid #d8d8d8 / L:1px solid #d8d8d8 r 48px; div.sx-vx4679.sx-1q0g3np.sx-1ja2u2z 125.4x24.0 bg #ffffff border T:1px solid #d8d8d8 / R:1px solid #d8d8d8 / B:1px solid #d8d8d8 / L:1px solid #d8d8d8 r 48px; div.sx-16rqkct.sx-2lah0s.sx-1wc42o8 9.0x9.0 bg #eb5757 r 50%; div.sx-vx4679.sx-1q0g3np.sx-1ja2u2z 92.8x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 48px | = | = |
| How | at rest | mouse hover | keyboard: Shift keydown, then focus() |

Crops: `card-default.png`, `card-hover.png`, `card-focus-visible.png`, `card-light.png`, `card-light-hover.png`, `card-light-focus-visible.png`.

#### board-column-header

Board column header.

Page copy: `issues-board-dark`. Finder: `() => [...document.querySelectorAll('main div')].find((e) => /^Backlog\s*\d+/.test(e.textContent.trim()) && e.getBoundingClientRect().width > 200 && e.getBoundingClientRect().width < 400 && e.getBoundingClientRect().height >= 28 && e.getBoundingClientRect().height <= 60) // null`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 348 x 50 |
| Padding | 2px 12px 0px 18px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-1srpx65: Inter Variable 13px/normal 500, #e3e4e6 |
| Transition | transform 0.2s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Cursor | default |
| Icon | 14 x 14, colour #ffffff |
| Painted layers | div.sx-1ja2u2z.sx-47corl.sx-10l6tqk 340.0x46.0 bg #09090a @ 0.4 r 5px 5px 0px 0px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 24.0x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 24.0x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 348 x 50 |
| Padding | 2px 12px 0px 18px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-1srpx65: Inter Variable 13px/normal 500, #2f2f31 |
| Transition | transform 0.2s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Cursor | default |
| Icon | 14 x 14, colour #1b1b1b |
| Painted layers | div.sx-1ja2u2z.sx-47corl.sx-10l6tqk 340.0x46.0 bg #efeff0 @ 0.4 r 5px 5px 0px 0px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 24.0x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 24.0x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest |

Crops: `board-column-header-default.png`, `board-column-header-light.png`.

#### list-row

List row (sub-issue).

Page copy: `issue-dark`. Finder: `() => [...document.querySelectorAll('main a[href*="/issue/"]')].find((a) => a.getBoundingClientRect().height >= 30) // null`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 659.05 x 36 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter Variable 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-1srpx65: Inter Variable 13px/normal 500, #ffffff | = | = |
| Transition | color 0.15s ease | none | = |
| Cursor | default | = | = |
| Icon | 14 x 14, colour #ffffff | = | = |
| Placeholder | "" #ffffff, opacity 1, 13.3333px | = | = |
| ::before | 659.047px x 36px, absolute, bg #000000 @ 0, radius 8px | = | = |
| Painted layers | div.sx-rvj5dj.sx-4w6khx.sx-1osaytk::before 659.047pxx36px bg #1a1a1b r 8px opacity 0; div.sx-3nfvp2.sx-6s0dn4.sx-l56j7k 14.0x14.0 border T:1px solid #737476 / R:1px solid #737476 / B:1px solid #737476 / L:1px solid #737476 r 3px | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 659.05 x 36 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter Variable 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1b1b1b | = | = |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-1srpx65: Inter Variable 13px/normal 500, #1b1b1b | = | = |
| Transition | color 0.15s ease | none | = |
| Cursor | default | = | = |
| Icon | 14 x 14, colour #1b1b1b | = | = |
| Placeholder | "" #000000, opacity 1, 13.3333px | = | = |
| ::before | 659.047px x 36px, absolute, bg #000000 @ 0, radius 8px | = | = |
| Painted layers | div.sx-rvj5dj.sx-4w6khx.sx-1osaytk::before 659.047pxx36px bg #efeff0 r 8px opacity 0; div.sx-3nfvp2.sx-6s0dn4.sx-l56j7k 14.0x14.0 border T:1px solid #7c7c7c / R:1px solid #7c7c7c / B:1px solid #7c7c7c / L:1px solid #7c7c7c r 3px | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |

Crops: `list-row-default.png`, `list-row-hover.png`, `list-row-focus-visible.png`, `list-row-light.png`, `list-row-light-hover.png`, `list-row-light-focus-visible.png`.

### Tables

#### table-row

Table row (projects).

Page copy: `projects-dark`. Finder: `() => W(Q('main a[href*="/project/"]'), 1000) // Q('main a[href*="/project/"]')`.

Dark theme.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1186 x 48 | = |
| Padding | 0px | = |
| Gap | normal 6px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-1srpx65: Inter Variable 13px/normal 500, #ffffff | = |
| Transition | color 0.15s ease | none |
| Cursor | default | = |
| Icon | 16 x 16, colour #ffffff, fill #4ea7fc | = |
| Placeholder | "" #ffffff, opacity 1, 13.3333px | = |
| ::before | 1170px x 48px, absolute, bg #000000 @ 0, radius 8px | = |
| Painted layers | div.sx-3nfvp2.sx-6s0dn4.sx-l56j7k 14.0x14.0 border T:1px solid #737476 / R:1px solid #737476 / B:1px solid #737476 / L:1px solid #737476 r 3px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 107.9x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | div.sx-3nfvp2.sx-6s0dn4.sx-l56j7k 14.0x14.0 border T:1px solid #737476 / R:1px solid #737476 / B:1px solid #737476 / L:1px solid #737476 r 3px; button.sx-78zum5.sx-6s0dn4.sx-l56j7k 28.0x28.0 bg #59bdff @ 0.175 r 8px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 107.9x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover |

Light theme.

| Property | light | light-hover |
|---|---|---|
| Size (w x h) | 1186 x 48 | = |
| Padding | 0px | = |
| Gap | normal 6px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1b1b | = |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-1srpx65: Inter Variable 13px/normal 500, #1b1b1b | = |
| Transition | color 0.15s ease | none |
| Cursor | default | = |
| Icon | 16 x 16, colour #000000, fill #4ea7fc | = |
| Placeholder | "" #000000, opacity 1, 13.3333px | = |
| ::before | 1170px x 48px, absolute, bg #000000 @ 0, radius 8px | = |
| Painted layers | div.sx-3nfvp2.sx-6s0dn4.sx-l56j7k 14.0x14.0 border T:1px solid #7c7c7c / R:1px solid #7c7c7c / B:1px solid #7c7c7c / L:1px solid #7c7c7c r 3px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 107.9x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | div.sx-3nfvp2.sx-6s0dn4.sx-l56j7k 14.0x14.0 border T:1px solid #7c7c7c / R:1px solid #7c7c7c / B:1px solid #7c7c7c / L:1px solid #7c7c7c r 3px; button.sx-78zum5.sx-6s0dn4.sx-l56j7k 28.0x28.0 bg #149bf8 @ 0.125 r 8px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 107.9x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover |

Crops: `table-row-default.png`, `table-row-hover.png`, `table-row-light.png`, `table-row-light-hover.png`.

#### table-header

Table header cell (members, sortable).

Page copy: `settings-members-dark`. Finder: `() => TB('Email', M())`.

Dark theme.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 58.52 x 24 | = |
| Padding | 0px 6px | = |
| Border | 1px solid #000000 @ 0 | = |
| Radius | 9999px | = |
| Background | transparent | #232424 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 12px/normal 500 | = |
| Letter spacing | normal | = |
| Colour | #e3e4e6 | #ffffff |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-167xe44: Inter Variable 12px/normal 450, #959597 | span.sx-1j61x8r.sx-ggjnk3.sx-167xe44: Inter Variable 12px/normal 450, #ffffff |
| Transition | border, background-color, color, opacity 0.15s ease | none |
| Cursor | default | = |
| Icon | 12 x 12, colour #e3e4e6, fill #959597 | 12 x 12, colour #ffffff, fill #959597 |
| Painted layers | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 58.5x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 58.5x24.0 bg #232424 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover |

Light theme.

| Property | light | light-hover |
|---|---|---|
| Size (w x h) | 58.52 x 24 | = |
| Padding | 0px 6px | = |
| Border | 1px solid #000000 @ 0 | = |
| Radius | 9999px | = |
| Background | transparent | #f0f0f1 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 12px/normal 500 | = |
| Letter spacing | normal | = |
| Colour | #2f2f31 | #1b1b1b |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-167xe44: Inter Variable 12px/normal 450, #5c5c5e | span.sx-1j61x8r.sx-ggjnk3.sx-167xe44: Inter Variable 12px/normal 450, #1b1b1b |
| Transition | border, background-color, color, opacity 0.15s ease | none |
| Cursor | default | = |
| Icon | 12 x 12, colour #2f2f31, fill #5c5c5e | 12 x 12, colour #1b1b1b, fill #5c5c5e |
| Painted layers | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 58.5x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 58.5x24.0 bg #f0f0f1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover |

Crops: `table-header-default.png`, `table-header-hover.png`, `table-header-light.png`, `table-header-light-hover.png`.

#### table-member-row

Table row (members).

Page copy: `settings-members-dark`. Finder: `() => W(T('learner@example.com', M()), 1000)`.

Dark theme.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1186 x 50 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | div.sx-16rqkct.sx-h8yej3.sx-5yr21d: Inter Variable 12px/0px 600, #ffffff | = |
| Transition | none | = |
| Cursor | default | = |
| Icon | 16 x 16, colour #e3e4e6, fill #959597 | = |
| Placeholder | "" #ffffff, opacity 1, 13.3333px | = |
| Painted layers | div.sx-3nfvp2.sx-6s0dn4.sx-l56j7k 14.0x14.0 border T:1px solid #737476 / R:1px solid #737476 / B:1px solid #737476 / L:1px solid #737476 r 3px; div.sx-16rqkct.sx-h8yej3.sx-5yr21d 24.0x24.0 bg #8a8a8a r 9999px; div.sx-78zum5.sx-j8oexa.sx-1xijbu4 48.4x19.0 bg #5e6ad2 @ 0.2 r 3px; span.sx-16rqkct.sx-mkeg23.sx-1y0btm7 8.0x8.0 bg #27a644 border T:1px solid #121213 / R:1px solid #121213 / B:1px solid #121213 / L:1px solid #121213 r 50%; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px opacity 0 | div.sx-3nfvp2.sx-6s0dn4.sx-l56j7k 14.0x14.0 border T:1px solid #6975e2 / R:1px solid #6975e2 / B:1px solid #6975e2 / L:1px solid #6975e2 r 3px; div.sx-16rqkct.sx-h8yej3.sx-5yr21d 24.0x24.0 bg #8a8a8a r 9999px; div.sx-78zum5.sx-j8oexa.sx-1xijbu4 48.4x19.0 bg #5e6ad2 @ 0.2 r 3px; span.sx-16rqkct.sx-mkeg23.sx-1y0btm7 8.0x8.0 bg #27a644 border T:1px solid #121213 / R:1px solid #121213 / B:1px solid #121213 / L:1px solid #121213 r 50%; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px opacity 0 |
| How | at rest | mouse hover |

Light theme.

| Property | light | light-hover |
|---|---|---|
| Size (w x h) | 1186 x 50 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1b1b | = |
| Text node | div.sx-16rqkct.sx-h8yej3.sx-5yr21d: Inter Variable 12px/0px 600, #ffffff | = |
| Transition | none | = |
| Cursor | default | = |
| Icon | 16 x 16, colour #2f2f31, fill #5c5c5e | = |
| Placeholder | "" #000000, opacity 1, 13.3333px | = |
| Painted layers | div.sx-3nfvp2.sx-6s0dn4.sx-l56j7k 14.0x14.0 border T:1px solid #7c7c7c / R:1px solid #7c7c7c / B:1px solid #7c7c7c / L:1px solid #7c7c7c r 3px; div.sx-16rqkct.sx-h8yej3.sx-5yr21d 24.0x24.0 bg #8a8a8a r 9999px; div.sx-78zum5.sx-j8oexa.sx-1xijbu4 48.4x19.0 bg #5e6ad2 @ 0.08 r 3px; span.sx-16rqkct.sx-mkeg23.sx-1y0btm7 8.0x8.0 bg #43bc58 border T:1px solid #f9f9fa / R:1px solid #f9f9fa / B:1px solid #f9f9fa / L:1px solid #f9f9fa r 50%; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px opacity 0 | div.sx-3nfvp2.sx-6s0dn4.sx-l56j7k 14.0x14.0 border T:1px solid #5e6ac1 / R:1px solid #5e6ac1 / B:1px solid #5e6ac1 / L:1px solid #5e6ac1 r 3px; div.sx-16rqkct.sx-h8yej3.sx-5yr21d 24.0x24.0 bg #8a8a8a r 9999px; div.sx-78zum5.sx-j8oexa.sx-1xijbu4 48.4x19.0 bg #5e6ad2 @ 0.08 r 3px; span.sx-16rqkct.sx-mkeg23.sx-1y0btm7 8.0x8.0 bg #43bc58 border T:1px solid #f9f9fa / R:1px solid #f9f9fa / B:1px solid #f9f9fa / L:1px solid #f9f9fa r 50%; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px opacity 0 |
| How | at rest | mouse hover |

Crops: `table-member-row-default.png`, `table-member-row-hover.png`, `table-member-row-light.png`, `table-member-row-light-hover.png`.

#### table-group-header

Table group header (Active).

Page copy: `settings-members-dark`. Finder: `() => W(T('Active', M()), 1000)`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 1170 x 32 |
| Padding | 0px 44px 0px 52px |
| Border | T: none; R: none; B: 1px solid #121213; L: none |
| Radius | 8px |
| Background | #161617 |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-84vug0: Inter Variable 12px/normal 500, #959597 |
| Transition | none |
| Cursor | default |
| Painted layers | div.sx-78zum5.sx-vx4679.sx-1q0g3np 1170.0x32.0 bg #161617 border B:1px solid #121213 r 8px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 1170 x 32 |
| Padding | 0px 44px 0px 52px |
| Border | T: none; R: none; B: 1px solid #f9f9fa; L: none |
| Radius | 8px |
| Background | #e9e9ea |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-84vug0: Inter Variable 12px/normal 500, #5c5c5e |
| Transition | none |
| Cursor | default |
| Painted layers | div.sx-78zum5.sx-vx4679.sx-1q0g3np 1170.0x32.0 bg #e9e9ea border B:1px solid #f9f9fa r 8px |
| How | at rest |

Crops: `table-group-header-default.png`, `table-group-header-light.png`.

### Display

#### avatar

Avatar (32px, members). Every avatar photo was replaced by a grey disc with an L in the copy; size and shape are Linear's, the fill is not.

Page copy: `settings-members-dark`. Finder: `() => [...document.querySelectorAll('main div')].find((d) => d.textContent === 'L' && d.getBoundingClientRect().width >= 20 && d.getBoundingClientRect().width <= 40) // null`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 24 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 13px/0px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.sx-16rqkct.sx-h8yej3.sx-5yr21d: Inter Variable 12px/0px 600, #ffffff |
| Transition | none |
| Cursor | default |
| Painted layers | div.sx-16rqkct.sx-h8yej3.sx-5yr21d 24.0x24.0 bg #8a8a8a r 9999px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 24 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 13px/0px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Text node | div.sx-16rqkct.sx-h8yej3.sx-5yr21d: Inter Variable 12px/0px 600, #ffffff |
| Transition | none |
| Cursor | default |
| Painted layers | div.sx-16rqkct.sx-h8yej3.sx-5yr21d 24.0x24.0 bg #8a8a8a r 9999px |
| How | at rest |

Crops: none.

#### badge

Badge (Admin).

Page copy: `settings-members-dark`. Finder: `() => P(T('Admin', M()))`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 48.44 x 19 |
| Padding | 2px 6px |
| Border | none |
| Radius | 3px |
| Background | #5e6ad2 @ 0.2 |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-167xe44: Inter Variable 12px/normal 450, #adbbff |
| Transition | none |
| Cursor | default |
| Painted layers | div.sx-78zum5.sx-j8oexa.sx-1xijbu4 48.4x19.0 bg #5e6ad2 @ 0.2 r 3px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 48.44 x 19 |
| Padding | 2px 6px |
| Border | none |
| Radius | 3px |
| Background | #5e6ad2 @ 0.08 |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-167xe44: Inter Variable 12px/normal 450, #4e6dfb |
| Transition | none |
| Cursor | default |
| Painted layers | div.sx-78zum5.sx-j8oexa.sx-1xijbu4 48.4x19.0 bg #5e6ad2 @ 0.08 r 3px |
| How | at rest |

Crops: `badge-default.png`, `badge-light.png`.

#### label-chip

Label chip on a card.

Page copy: `issues-board-dark`. Finder: `() => [...document.querySelectorAll('[data-board-item] *')].find((e) => { const c = getComputedStyle(e); const r = e.getBoundingClientRect(); return r.height >= 18 && r.height <= 26 && r.width > 50 && parseFloat(c.borderTopLeftRadius) >= 9 && (c.borderTopStyle !== 'none' // c.backgroundColor !== 'rgba(0, 0, 0, 0)'); }) // null`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 125.44 x 24 |
| Padding | 0px 8px |
| Border | 1px solid #2f3033 |
| Radius | 48px |
| Background | #1a1a1b |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-167xe44: Inter Variable 12px/normal 450, #98999c |
| Transition | border-color, color, background-color 0.15s ease |
| Cursor | default |
| Painted layers | div.sx-vx4679.sx-1q0g3np.sx-1ja2u2z 125.4x24.0 bg #1a1a1b border T:1px solid #2f3033 / R:1px solid #2f3033 / B:1px solid #2f3033 / L:1px solid #2f3033 r 48px; div.sx-16rqkct.sx-2lah0s.sx-1wc42o8 9.0x9.0 bg #eb5757 r 50% |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 125.44 x 24 |
| Padding | 0px 8px |
| Border | 1px solid #d8d8d8 |
| Radius | 48px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Text node | span.sx-1j61x8r.sx-ggjnk3.sx-167xe44: Inter Variable 12px/normal 450, #5e5e60 |
| Transition | border-color, color, background-color 0.15s ease |
| Cursor | default |
| Painted layers | div.sx-vx4679.sx-1q0g3np.sx-1ja2u2z 125.4x24.0 bg #ffffff border T:1px solid #d8d8d8 / R:1px solid #d8d8d8 / B:1px solid #d8d8d8 / L:1px solid #d8d8d8 r 48px; div.sx-16rqkct.sx-2lah0s.sx-1wc42o8 9.0x9.0 bg #eb5757 r 50% |
| How | at rest |

Crops: `label-chip-default.png`, `label-chip-light.png`.

#### kbd

Keyboard shortcut in a tooltip.

Page copy: `issue-dark-tooltip`. Finder: `() => { const host = [...document.body.children].filter((c) => /Copy issue URL/.test(c.textContent)).pop(); return host ? [...host.querySelectorAll('*')].find((e) => e.textContent.trim() === '⌘' && e.children.length === 0) : null; }`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 18 x 18.09 |
| Padding | 2px |
| Border | 1px solid #303134 |
| Radius | 4px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 11px/12.1px 400 |
| Letter spacing | normal |
| Colour | #9c9d9f |
| Transition | none |
| Cursor | default |
| Painted layers | kbd.sx-1rg5ohu.sx-11njtxf.sx-2b8uid 18.0x18.1 border T:1px solid #303134 / R:1px solid #303134 / B:1px solid #303134 / L:1px solid #303134 r 4px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 18 x 18.09 |
| Padding | 2px |
| Border | 1px solid #e8e8e8 |
| Radius | 4px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 11px/12.1px 400 |
| Letter spacing | normal |
| Colour | #5e5e60 |
| Transition | none |
| Cursor | default |
| Painted layers | kbd.sx-1rg5ohu.sx-11njtxf.sx-2b8uid 18.0x18.1 border T:1px solid #e8e8e8 / R:1px solid #e8e8e8 / B:1px solid #e8e8e8 / L:1px solid #e8e8e8 r 4px |
| How | at rest |

Crops: `kbd-default.png`, `kbd-light.png`.

#### health-on-track

Project health, On track.

Page copy: `projects-dark`. Finder: `() => TS('On track', M())`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 155.91 x 15 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 12px/normal 500 |
| Letter spacing | normal |
| Colour | #527a58 |
| Transition | all 0.15s ease |
| Cursor | default |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 84.2 x 15 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 12px/normal 500 |
| Letter spacing | normal |
| Colour | #4c8055 |
| Transition | all 0.15s ease |
| Cursor | default |
| How | at rest |

Crops: `health-on-track-default.png`, `health-on-track-light.png`.

#### health-at-risk

Project health, At risk.

Page copy: `projects-dark`. Finder: `() => TS('At risk', M())`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 143.33 x 15 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 12px/normal 500 |
| Letter spacing | normal |
| Colour | #9d854c |
| Transition | all 0.15s ease |
| Cursor | default |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 71.94 x 15 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 12px/normal 500 |
| Letter spacing | normal |
| Colour | #9d8242 |
| Transition | all 0.15s ease |
| Cursor | default |
| How | at rest |

Crops: `health-at-risk-default.png`, `health-at-risk-light.png`.

#### presence-online

Presence dot (Online).

Page copy: `settings-members-dark`. Finder: `() => { const t = T('Online', M()); return t ? [...t.parentElement.querySelectorAll('*')].find((e) => { const r = e.getBoundingClientRect(); return r.width > 2 && r.width < 12 && getComputedStyle(e).backgroundColor !== 'rgba(0, 0, 0, 0)'; }) // null : null; }`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 8 x 8 |
| Padding | 0px |
| Border | 1px solid #121213 |
| Radius | 50% |
| Background | #27a644 |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 12px/normal 450 |
| Letter spacing | normal |
| Colour | #959597 |
| Transition | background-color 0.5s ease |
| Cursor | default |
| Painted layers | span.sx-16rqkct.sx-mkeg23.sx-1y0btm7 8.0x8.0 bg #27a644 border T:1px solid #121213 / R:1px solid #121213 / B:1px solid #121213 / L:1px solid #121213 r 50% |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 8 x 8 |
| Padding | 0px |
| Border | 1px solid #f9f9fa |
| Radius | 50% |
| Background | #43bc58 |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 12px/normal 450 |
| Letter spacing | normal |
| Colour | #5c5c5e |
| Transition | background-color 0.5s ease |
| Cursor | default |
| Painted layers | span.sx-16rqkct.sx-mkeg23.sx-1y0btm7 8.0x8.0 bg #43bc58 border T:1px solid #f9f9fa / R:1px solid #f9f9fa / B:1px solid #f9f9fa / L:1px solid #f9f9fa r 50% |
| How | at rest |

Crops: `presence-online-default.png`, `presence-online-light.png`.

### Shell

#### app-shell-main

Main panel (inset content area).

Page copy: `issues-board-dark`. Finder: `() => BOX(M(), 1000, 600) // M()`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 1188 x 856 |
| Padding | 0px |
| Border | 1px solid #212224 |
| Radius | 12px |
| Background | #121213 |
| Box shadow | #000000 @ 0.3 0px 0.5px 1px 1px |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.sx-78zum5.sx-vx4679.sx-1q0g3np: Inter Variable 13px/normal 500, #e3e4e6 |
| Transition | none |
| Cursor | default |
| Icon | 14 x 14, colour #e3e4e6, fill #959597 |
| Painted layers | main.sx-78zum5.sx-131h156.sx-dt5ytf 1188.0x856.0 bg #121213 border T:1px solid #212224 / R:1px solid #212224 / B:1px solid #212224 / L:1px solid #212224 r 12px shadow #000000 @ 0.3 0px 0.5px 1px 1px; header.sx-78zum5.sx-2lah0s.sx-euugli 1186.0x88.0 bg #121213; div.sx-85fieu.sx-1ow8xz6.sx-16qpidq 1186.0x44.5 border B:1px solid #212224; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 28.0x28.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 28.0x28.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 58.2x28.0 bg #1c1c1d border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 1188 x 856 |
| Padding | 0px |
| Border | 1px solid #e2e2e2 |
| Radius | 12px |
| Background | #f9f9fa |
| Box shadow | #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Text node | div.sx-78zum5.sx-vx4679.sx-1q0g3np: Inter Variable 13px/normal 500, #2f2f31 |
| Transition | none |
| Cursor | default |
| Icon | 14 x 14, colour #2f2f31, fill #5c5c5e |
| Painted layers | main.sx-78zum5.sx-131h156.sx-dt5ytf 1188.0x856.0 bg #f9f9fa border T:1px solid #e2e2e2 / R:1px solid #e2e2e2 / B:1px solid #e2e2e2 / L:1px solid #e2e2e2 r 12px shadow #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px; header.sx-78zum5.sx-2lah0s.sx-euugli 1186.0x88.0 bg #f9f9fa; div.sx-85fieu.sx-1ow8xz6.sx-16qpidq 1186.0x44.5 border B:1px solid #e2e2e2; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 28.0x28.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 28.0x28.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 58.2x28.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest |

Crops: none.

#### page-header

Page header bar.

Page copy: `issues-board-dark`. Finder: `() => H(Q('main button[aria-label="Add to favorites"]'), 40)`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 1136 x 43.5 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.sx-78zum5.sx-vx4679.sx-1q0g3np: Inter Variable 13px/normal 500, #e3e4e6 |
| Transition | none |
| Cursor | default |
| Icon | 14 x 14, colour #e3e4e6, fill #959597 |
| Painted layers | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 28.0x28.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 1136 x 43.5 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Text node | div.sx-78zum5.sx-vx4679.sx-1q0g3np: Inter Variable 13px/normal 500, #2f2f31 |
| Transition | none |
| Cursor | default |
| Icon | 14 x 14, colour #2f2f31, fill #5c5c5e |
| Painted layers | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 28.0x28.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest |

Crops: none.

#### empty-state

Empty state (My issues).

Page copy: `empty-dark`. Finder: `() => TB('Create new issue', M())`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 120.83 x 28 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter Variable 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Text node | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4: Inter Variable 12px/normal 500, #fffeff | = | = |
| Transition | none | = | = |
| Cursor | default | = | = |
| Painted layers | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 120.8x28.0 bg #5e6ad2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.3 0px 0.5px 1px 1px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 120.8x28.0 bg #6975e2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.3 0px 0.5px 1px 1px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 120.8x28.0 bg #5e6ad2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.3 0px 0.5px 1px 1px outline 1px solid #5e6ad2 offset 2px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 120.83 x 28 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter Variable 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1b1b1b | = | = |
| Text node | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4: Inter Variable 12px/normal 500, #fffeff | = | = |
| Transition | none | = | = |
| Cursor | default | = | = |
| Painted layers | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 120.8x28.0 bg #6d78d5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 120.8x28.0 bg #5e6ac1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px | button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 120.8x28.0 bg #6d78d5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0.02 0px 3px 6px -2px, #000000 @ 0.04 0px 1px 1px 0px outline 1px solid #6d78d5 offset 2px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) |

Crops: `empty-state-default.png`, `empty-state-hover.png`, `empty-state-focus-visible.png`, `empty-state-light.png`, `empty-state-light-hover.png`, `empty-state-light-focus-visible.png`.

### Type

#### type-issue-title

Issue title (detail).

Page copy: `issue-dark`. Finder: `() => Q('main .ProseMirror h1, main [contenteditable] > p, main .ProseMirror')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 653.05 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 24px/38.4px 600 |
| Letter spacing | -0.1px |
| Colour | #ffffff |
| Text node | p.text-node: Inter Variable 24px/32px 600, #ffffff, ls -0.16px |
| Transition | none |
| Cursor | text |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 653.05 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 24px/38.4px 600 |
| Letter spacing | -0.1px |
| Colour | #1b1b1b |
| Text node | p.text-node: Inter Variable 24px/32px 600, #1b1b1b, ls -0.16px |
| Transition | none |
| Cursor | text |
| How | at rest |

Crops: none.

#### type-heading

Description heading (h2).

Page copy: `issue-dark`. Finder: `() => Q('main .ProseMirror h2')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 653.05 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 19px/28px 600 |
| Letter spacing | 0.05px |
| Colour | #ffffff |
| Text node | span.attr: Inter Variable 19px/28px 600, #ffffff, ls 0.05px |
| Transition | none |
| Cursor | text |
| Icon | 16 x 16, colour #e3e4e6, fill #959597 |
| Painted layers | div.sx-10l6tqk.sx-15tkfdg.sx-v39vnz 28.0x52.0 bg #121213; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 20.0x20.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 653.05 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 19px/28px 600 |
| Letter spacing | 0.05px |
| Colour | #1b1b1b |
| Text node | span.attr: Inter Variable 19px/28px 600, #1b1b1b, ls 0.05px |
| Transition | none |
| Cursor | text |
| Icon | 16 x 16, colour #2f2f31, fill #5c5c5e |
| Painted layers | div.sx-10l6tqk.sx-15tkfdg.sx-v39vnz 28.0x52.0 bg #f9f9fa; button.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 20.0x20.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest |

Crops: none.

#### type-body

Description body paragraph.

Page copy: `issue-dark`. Finder: `() => Q('[aria-label="Issue description"] p, main .ProseMirror + * p, main .ProseMirror p', 1)`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 653.05 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 15px/24px 450 |
| Letter spacing | -0.1px |
| Colour | #e3e4e6 |
| Text node | span.attr: Inter Variable 15px/24px 450, #e3e4e6, ls -0.1px |
| Transition | none |
| Cursor | text |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 653.05 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 15px/24px 450 |
| Letter spacing | -0.1px |
| Colour | #2f2f31 |
| Text node | span.attr: Inter Variable 15px/24px 450, #2f2f31, ls -0.1px |
| Transition | none |
| Cursor | text |
| How | at rest |

Crops: none.

#### type-code

Inline code.

Page copy: `issue-dark`. Finder: `() => Q('main .ProseMirror code')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 123.75 x 17 |
| Padding | 0.5px 3.51562px |
| Border | none |
| Radius | 2.8125px |
| Background | #ffffff @ 0.075 |
| Box shadow | #3f4042 0px 0px 0px 0.5px inset |
| Outline | none |
| Font | Berkeley Mono 14.0625px/18.2812px 450 |
| Letter spacing | -0.1px |
| Colour | #e3e4e6 |
| Text node | span.attr: Berkeley Mono 14.0625px/18.2812px 450, #e3e4e6, ls -0.1px |
| Transition | none |
| Cursor | text |
| Painted layers | code.inline 123.8x17.0 bg #ffffff @ 0.075 r 2.8125px shadow #3f4042 0px 0px 0px 0.5px inset |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 123.75 x 17 |
| Padding | 0.5px 3.51562px |
| Border | none |
| Radius | 2.8125px |
| Background | #092c78 @ 0.05 |
| Box shadow | #d3d3d3 0px 0px 0px 0.5px inset |
| Outline | none |
| Font | Berkeley Mono 14.0625px/18.2812px 450 |
| Letter spacing | -0.1px |
| Colour | #2f2f31 |
| Text node | span.attr: Berkeley Mono 14.0625px/18.2812px 450, #2f2f31, ls -0.1px |
| Transition | none |
| Cursor | text |
| Painted layers | code.inline 123.8x17.0 bg #092c78 @ 0.05 r 2.8125px shadow #d3d3d3 0px 0px 0px 0.5px inset |
| How | at rest |

Crops: none.

#### type-page-title

Settings page title.

Page copy: `settings-members-dark`. Finder: `() => Q('main h1') // T('Members', M())`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 1074 x 32 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.sx-1j61x8r.sx-hacrq1.sx-dyqlo0: Inter Variable 24px/32px 500, #ffffff, ls -0.16px |
| Transition | none |
| Cursor | default |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 1074 x 32 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Text node | span.sx-1j61x8r.sx-hacrq1.sx-dyqlo0: Inter Variable 24px/32px 500, #1b1b1b, ls -0.16px |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: none.

#### type-section-label

Sidebar section label (Workspace).

Page copy: `issues-board-dark`. Finder: `() => T('Workspace')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 65.02 x 15 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 12px/normal 500 |
| Letter spacing | normal |
| Colour | #929294 |
| Transition | none |
| Cursor | default |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 65.02 x 15 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 12px/normal 500 |
| Letter spacing | normal |
| Colour | #59595b |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: none.

#### type-caption

Card meta line.

Page copy: `issues-board-dark`. Finder: `() => [...document.querySelectorAll('[data-board-item] span')].find((e) => /^CORE-\d+$/.test(e.textContent.trim())) // null`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 113.95 x 15 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 12px/normal 450 |
| Letter spacing | normal |
| Colour | #98999c |
| Text node | span.sx-1rg5ohu.sx-uxw1ft.sx-cwjd09: Inter Variable 12px/normal 450, #98999c, ls -0.24px |
| Transition | none |
| Cursor | default |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 113.95 x 15 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 12px/normal 450 |
| Letter spacing | normal |
| Colour | #5e5e60 |
| Text node | span.sx-1rg5ohu.sx-uxw1ft.sx-cwjd09: Inter Variable 12px/normal 450, #5e5e60, ls -0.24px |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: none.

### Phone

#### mobile-card

Board card at 390.

Page copy: `mobile-issues-board-dark`. Finder: `() => Q('[data-board-item]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 264 x 117 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | #1a1a1b |
| Box shadow | #ffffff @ 0.083 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.sx-1rg5ohu.sx-uxw1ft.sx-cwjd09: Inter Variable 12px/normal 450, #98999c, ls -0.24px |
| Transition | background-color 0.1s ease |
| Cursor | default |
| Icon | 14 x 14, colour #ffffff |
| Painted layers | a.sx-78zum5.sx-6s0dn4.sx-1n2onr6 264.0x117.0 bg #1a1a1b r 8px shadow #ffffff @ 0.083 0px 0px 0px 0.5px, #000000 @ 0.3 0px 0.5px 1px 1px; div.sx-78zum5.sx-dt5ytf.sx-l56j7k::before 264pxx117px bg #212223 r 8px opacity 0; div.sx-vx4679.sx-1q0g3np.sx-1ja2u2z 25.0x24.0 bg #1a1a1b border T:1px solid #2f3033 / R:1px solid #2f3033 / B:1px solid #2f3033 / L:1px solid #2f3033 r 48px; div.sx-vx4679.sx-1q0g3np.sx-1ja2u2z 112.0x24.0 bg #1a1a1b border T:1px solid #2f3033 / R:1px solid #2f3033 / B:1px solid #2f3033 / L:1px solid #2f3033 r 48px; div.sx-16rqkct.sx-2lah0s.sx-1wc42o8 9.0x9.0 bg #eb5757 r 50%; div.sx-vx4679.sx-1q0g3np.sx-1ja2u2z 92.8x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 48px |
| How | at rest |

Crops: `mobile-card-default.png`.

#### mobile-tab

View tab at 390.

Page copy: `mobile-issues-board-dark`. Finder: `() => TB('All issues', M())`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 76.44 x 28 |
| Padding | 0px 10px |
| Border | 1px solid #000000 @ 0 |
| Radius | 9999px |
| Background | #29292b |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 12px/normal 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.sx-uxw1ft.sx-b3r6kr.sx-lyipyv: Inter Variable 12px/normal 500, #ffffff |
| Transition | border, background-color, color, opacity 0.15s ease |
| Cursor | default |
| ::after | 74.4375px x 26px, absolute, bg #000000 @ 0, radius 9999px, shadow #ffffff @ 0.137 0px 0px 0px 0.5px, #000000 @ 0 0px 0px 0px 0px |
| Painted layers | a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4 76.4x28.0 bg #29292b border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a.sx-3nfvp2.sx-16dsc37.sx-6s0dn4::after 74.4375pxx26px r 9999px shadow #ffffff @ 0.137 0px 0px 0px 0.5px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `mobile-tab-default.png`.
