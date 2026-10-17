# ChatGPT component measurements

Computed styles read on 2026-10-17 by `tools/capture/signed-in/measure.mjs` from static page copies of the signed-in app (1440x900 (the mobile-* snapshots 390x844), deviceScaleFactor 2), and written here by `tools/capture/signed-in/build-measurements.mjs` from [components-computed.json](components-computed.json). Each copy was captured in the dark theme with the blue accent. Dark states have plain names; light states (`light`, `light-<state>`) were read from the same DOM with every data-theme="dark" set to light. Every state records `theme` and `snapshot`.

Every component has one table per theme: a column per state, a row per property. A cell that repeats the first column reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline (a hover or selection is sometimes painted on an inner layer, not the element itself); "Ancestor paint" the same for its parents. "Tokens" lists the custom properties the component's classes name (`bg-token-x` reads `--x`, `bg-(--x)`, `[var(--x)]`) and the inline `--menu-item-*` variables a row sets, with the value each resolved to in that theme.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab), skipped where the element cannot take focus. ChatGPT draws most focus rings from `keyboard-focused:` variants that its own script turns on, so with scripts gone many focused states look like the rest state. The rest (`active`, `selected`, `checked`, `open`, `typed`, `highlighted`, ...) are other elements or copies captured in that state. Light states are prefixed `light`. The 390 wide copies are measured at rest only.

130 components, 670 states (670 measured, 0 skipped, 0 not found).

## Shared values

Tallied over every measured state by the build script.

- **Radius scale** (element radius, times seen): 9999px (278), 8px (90), 12px (52), 999px (50), 16px (48), 4px (12), 24px (11), 26px (8), 6px (6), 22px (6), 3.72px (2), 32px (2), 20px (2), 28px (2).
- **Transitions**: `opacity, color 0.15s ease` (38), `opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1)` (32), `color 0.075s ease` (8), `background-color, border-color, box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1)` (4), `color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0, 0, 0.2, 1)` (3), `height 0.3s cubic-bezier(0.23, 1, 0.32, 1)` (2), `transform 0.3s cubic-bezier(0.2, 0, 0, 1)` (2), `transform, translate, scale, rotate 0.2s cubic-bezier(0, 0, 0.2, 1)` (2).
- **Font families**: -apple-system-body (900), -apple-system (18), ui-monospace (6).
- **Type sizes** (size/line-height weight of the first text): 14px/20px 500 (118), 14px/20px 400 (114), 16px/24px 400 (86), 14px/18px 400 (72), 16px/26px 400 (52), 16px/18px 400 (28), 14px/14px 500 (26), 12px/12px 600 (22), 12px/16px 400 (18), 16px/20px 500 (18), 14px/20px 600 (16), 14px/20px 510 (10), 12px/16px 500 (8), 16px/24px 500 (8).
- **Shadows**: `#ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px` (92); `#ffffff @ 0.2 0px 0px 1px 0px inset` (22); `#ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset` (20); `#000000 @ 0.08 0px 1px 2px -1px` (20); `#000000 @ 0.05 0px 4px 16px 0px` (14); `#3a83f7 0px 0px 0px 2px` (12).
- **Focus-visible, dark** (65 focused states): shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px (23); nothing painted on the element (9); shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px (5); outline 2px solid #3a83f7 offset -2px (4); outline 1px auto #99c8ff offset 1px (4); outline 1px auto #99c8ff offset 0px (4); outline 2px solid #3566f0 offset 2px (4); shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px (3); outline 2px solid #2c67c5 offset 0px (3); outline 2px solid #3a83f7 offset 0px (1); shadow #ffffff @ 0.2 0px 0px 1px 0px inset (1); outline 2px solid #ffffff @ 0.2 offset -2px (1); shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0.13 0px 2px 4px -1px (1); outline 2px solid #3566f0 offset 1px (1); outline 2px solid #3566f0 offset 0px (1).
- **Focus-visible, light** (65 focused states): shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px (23); nothing painted on the element (9); shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px (5); outline 2px solid #3a83f7 offset -2px (4); outline 2px solid #3a83f7 offset 0px (4); outline 1px auto #005fcc offset 1px (4); outline 1px auto #005fcc offset 0px (4); outline 2px solid #3566f0 offset 2px (4); shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px (3); shadow #ffffff @ 0.2 0px 0px 1px 0px inset (1); outline 2px solid #000000 @ 0.15 offset -2px (1); shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0.13 0px 2px 4px -1px (1); outline 2px solid #3566f0 offset 1px (1); outline 2px solid #3566f0 offset 0px (1).
- **Hover changes, dark** (71 hovered components, 24 with no change on the element or its first painted layer): backgroundColor #000000 @ 0 → #ffffff @ 0.1 (18); inner layer #ffffff @ 0.1 → #ffffff @ 0.1 (3); backgroundColor #000000 @ 0 → #ffffff @ 0.0509804 (3); backgroundColor #303030 → #ffffff @ 0.1 (2); backgroundColor #ff6764 @ 0.1 → #ff6764 @ 0.2 (2); backgroundColor #ededed → #ededed @ 0.8 (2); backgroundColor #ededed @ 0.05 → #ededed @ 0.1 (2); backgroundColor #ffffff → #e8e8e8 (2).
- **Hover changes, light** (71 hovered components, 24 with no change on the element or its first painted layer): backgroundColor #000000 @ 0 → #000000 @ 0.05 (18); inner layer #000000 @ 0.05 → #000000 @ 0.05 (3); backgroundColor #000000 @ 0 → #000000 @ 0.0254902 (3); backgroundColor #f3f3f3 → #000000 @ 0.05 (2); backgroundColor #e02e2a @ 0.1 → #e02e2a @ 0.2 (2); backgroundColor #0d0d0d → #0d0d0d @ 0.8 (2); backgroundColor #0d0d0d @ 0.05 → #0d0d0d @ 0.1 (2); backgroundColor #0d0d0d → #212121 (2).

### Tokens the measured components use

Every custom property a measured component's classes or inline style name, with the value it resolved to in each theme.

| Token | Dark | Light |
|---|---|---|
| `--accent-blue` | #3a83f7 | #3a83f7 |
| `--app-menu-gutter` | calc(.25rem * 2.5) | calc(.25rem * 2.5) |
| `--app-menu-item-height` | calc(.25rem * 9) | calc(.25rem * 9) |
| `--app-menu-item-padding` | calc(.25rem * 1.5) calc(.25rem * 2.5) | calc(.25rem * 1.5) calc(.25rem * 2.5) |
| `--app-menu-min-width` | calc(.25rem * 60) | calc(.25rem * 60) |
| `--app-menu-separator-gutter` | calc(.25rem * 2) | calc(.25rem * 2) |
| `--app-shell-application-menu-height` | 0px | 0px |
| `--app-shell-page-banner-height` | 0px | 0px |
| `--app-shell-root-banner-height` | 0px | 0px |
| `--app-shell-titlebar-height` | calc(.25rem * 13) | calc(.25rem * 13) |
| `--bg-primary` | #212121 | - |
| `--border-default` | #ffffff26 | - |
| `--codex-window-zoom` | 1 | 1 |
| `--color-background-tooltip` | #303030 | #0d0d0d |
| `--color-blue` | #3a83f7 | #3a83f7 |
| `--color-border-overlay` | #ffffff26 | #0000001a |
| `--color-dialog-overlay` | #0002 | #0002 |
| `--color-text` | color-mix(in oklab, #ededed 85%, transparent) | color-mix(in oklab, #0d0d0d 85%, transparent) |
| `--color-text-primary-ghost` | #ededed | #0d0d0d |
| `--color-text-tertiary` | #afafaf | #8f8f8f |
| `--color-text-toolbar-action` | #ededed | #0d0d0d |
| `--composer-editor-line-height` | calc(16px * 1.625) | calc(16px * 1.625) |
| `--cursor-interaction` | pointer | pointer |
| `--dialog-content-height` | 164px | 164px |
| `--height-token-row` | calc(16px * 1.5 + calc(.25rem * 1) * 2), 36px | calc(16px * 1.5 + calc(.25rem * 1) * 2), 36px |
| `--height-toolbar` | calc(.25rem * 13) | calc(.25rem * 13) |
| `--icon-leading-size` | calc(.25rem * 5) | calc(.25rem * 5) |
| `--interactive-label-accent-accessible` | #a4cdfb | #2c67c5 |
| `--main-surface-primary` | #000 | #fcfcfc |
| `--markdown-link-color` | currentColor | currentColor |
| `--nav-item-height` | calc(36px - 1px) | calc(36px - 1px) |
| `--padding-row-cell-x` | 10px, 8px | 10px, 8px |
| `--padding-row-x` | calc(.25rem * 2), 6px, 8px | calc(.25rem * 2), 6px, 8px |
| `--padding-row-y` | calc(.25rem * 1.25) | calc(.25rem * 1.25) |
| `--radius-3xl-base` | 1.5rem | 1.5rem |
| `--radius-xl` | calc(.75rem * 1) | calc(.75rem * 1) |
| `--radix-dropdown-menu-content-available-height` | 682.65625px, 832px, 577.203125px | 682.65625px, 832px, 577.203125px |
| `--radix-dropdown-menu-content-available-width` | 1428px | 1428px |
| `--radix-dropdown-menu-content-transform-origin` | 0% 289px, 0% 318px, 100% 0px | 0% 289px, 0% 318px, 100% 0px |
| `--radix-dropdown-menu-trigger-height` | 20px, 48px, 28px | 20px, 48px, 28px |
| `--radix-dropdown-menu-trigger-width` | 20px, 248.1171875px, 80.78125px | 20px, 248.1171875px, 80.78125px |
| `--radix-tooltip-content-available-height` | 464px, 838px | 464px, 838px |
| `--radix-tooltip-content-available-width` | 1424px | 1424px |
| `--radix-tooltip-trigger-width` | 36px | 36px |
| `--shadow-dropdown-overlay` | 0px 0px 0px .5px #ffffff26, 0px 8px 16px -4px #0000001f | 0px 0px 0px .5px #0000001a, 0px 8px 16px -4px #0000001f |
| `--shadow-tooltip` | 0 8px 18px #0f172a33 | 0 8px 18px #0f172a33 |
| `--sidebar-row-action-opacity` | 0 | 0 |
| `--sidebar-row-action-width` | auto | auto |
| `--sidebar-row-menu-overflow` | hidden | hidden |
| `--sidebar-row-menu-width` | 0px | 0px |
| `--spacing` | .25rem | .25rem |
| `--spacing-composer-single-line-controls` | calc(.25rem * 2) | calc(.25rem * 2) |
| `--spacing-menu-item-content` | calc(.25rem * 3) | calc(.25rem * 3) |
| `--spacing-nav-row-content` | calc(.25rem * 1.5) | calc(.25rem * 1.5) |
| `--spacing-token-button-composer` | calc(.25rem * 9) | calc(.25rem * 9) |
| `--spacing-token-safe-header-left` | 6px | 6px |
| `--suggestion-menu-item-padding` | calc(.25rem * 1.5) calc(.25rem * 2) | calc(.25rem * 1.5) calc(.25rem * 2) |
| `--suggestion-menu-item-radius` | calc(calc(.25rem * 5) - calc(.25rem * 2)) | calc(calc(.25rem * 5) - calc(.25rem * 2)) |
| `--text-primary` | #fff | #0d0d0d |
| `--text-secondary` | #cdcdcd | #5d5d5d |
| `--text-sm` | 14px | 14px |
| `--text-tertiary` | #afafaf | #8f8f8f |
| `--thread-composer-overlay-height` | 0px | 0px |
| `--thread-content-margin` | calc(.25rem * 4) | calc(.25rem * 4) |
| `--tracking-tooltip` | -.15px | -.15px |
| `--user-chat-width` | 70% | 70% |

## Components

### Sidebar

#### sidebar

Sidebar (expanded). `aside.LeftPanel`, 340 wide at 1440 (`--spacing-token-sidebar`, clamp(240px, 340px, ...)); header row, nav rows, then the Pinned, Projects and Recents sections and the account row.

Page copy: `home-dark`. Finder: `() => S()`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 340 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | span.text-fade-truncate: -apple-system-body 14px/20px 400, #ededed |
| Transition | none |
| Icon | 77.13 x 18, colour #ededed |
| Painted layers | aside.app-shell-left-panel.pointer-events-auto.relative 340.0x900.0 bg #000000; div.absolute.inset-0.flex 340.0x900.0 bg #000000; button.Button-QTscM8::before 36pxx36px bg #ffffff @ 0.1 r 8px opacity 0; button.Button-QTscM8.group/sidebar-trigger::before 36pxx36px bg #ffffff @ 0.1 r 8px opacity 0; button.sidebar-item.relative.shrink-0 328.0x35.0 bg #ffffff @ 0.1 r 8px |
| Tokens | --color-text-primary-ghost #ededed; --color-text-tertiary #afafaf; --height-token-row calc(16px * 1.5 + calc(.25rem * 1) * 2); --icon-leading-size calc(.25rem * 5); --padding-row-x calc(.25rem * 2); --spacing-nav-row-content calc(.25rem * 1.5) |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 340 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fcfcfc |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span.text-fade-truncate: -apple-system-body 14px/20px 400, #0d0d0d |
| Transition | none |
| Icon | 77.13 x 18, colour #0d0d0d |
| Painted layers | aside.app-shell-left-panel.pointer-events-auto.relative 340.0x900.0 bg #fcfcfc; div.absolute.inset-0.flex 340.0x900.0 bg #fcfcfc; button.Button-QTscM8::before 36pxx36px bg #000000 @ 0.05 r 8px opacity 0; button.Button-QTscM8.group/sidebar-trigger::before 36pxx36px bg #000000 @ 0.05 r 8px opacity 0; button.sidebar-item.relative.shrink-0 328.0x35.0 bg #000000 @ 0.05 r 8px |
| Tokens | --color-text-primary-ghost #0d0d0d; --color-text-tertiary #8f8f8f; --height-token-row calc(16px * 1.5 + calc(.25rem * 1) * 2); --icon-leading-size calc(.25rem * 5); --padding-row-x calc(.25rem * 2); --spacing-nav-row-content calc(.25rem * 1.5) |
| How | at rest |

Crops: `sidebar-default.png`, `sidebar-light.png`.

#### sidebar-icon-button

Icon button (sidebar Search). `Button` with data-color=secondary, data-variant=ghost, data-size=xl: 36x36.

Page copy: `home-dark`. Finder: `() => Q('button[aria-label="Search"]', 0, S())`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #afafaf | = | = | = |
| Transition | opacity, color 0.15s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #afafaf, fill #000000 | = | = | = |
| ::before | 36px x 36px, absolute, bg #ffffff @ 0.1, radius 8px | = | = | 36px x 36px, absolute, bg #ededed @ 0.16, radius 8px |
| ::after | 36px x 36px, absolute, bg #000000 @ 0, radius 8px | = | = | = |
| Painted layers | button.Button-QTscM8::before 36pxx36px bg #ffffff @ 0.1 r 8px opacity 0 | button.Button-QTscM8::before 36pxx36px bg #ffffff @ 0.1 r 8px | button.Button-QTscM8::before 36pxx36px bg #ffffff @ 0.1 r 8px opacity 0; button.Button-QTscM8::after 36pxx36px r 8px outline 2px solid #3a83f7 offset 0px | button.Button-QTscM8::before 36pxx36px bg #ededed @ 0.16 r 8px |
| Tokens | --color-text-primary-ghost #ededed; --color-text-tertiary #afafaf | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #8f8f8f | = | = | = |
| Transition | opacity, color 0.15s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #8f8f8f, fill #000000 | = | = | = |
| ::before | 36px x 36px, absolute, bg #000000 @ 0.05, radius 8px | = | = | 36px x 36px, absolute, bg #0d0d0d @ 0.12, radius 8px |
| ::after | 36px x 36px, absolute, bg #000000 @ 0, radius 8px | = | = | = |
| Painted layers | button.Button-QTscM8::before 36pxx36px bg #000000 @ 0.05 r 8px opacity 0 | button.Button-QTscM8::before 36pxx36px bg #000000 @ 0.05 r 8px | button.Button-QTscM8::before 36pxx36px bg #000000 @ 0.05 r 8px opacity 0; button.Button-QTscM8::after 36pxx36px r 8px outline 2px solid #3a83f7 offset 0px | button.Button-QTscM8::before 36pxx36px bg #0d0d0d @ 0.12 r 8px |
| Tokens | --color-text-primary-ghost #0d0d0d; --color-text-tertiary #8f8f8f | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `sidebar-icon-button-default.png`, `sidebar-icon-button-hover.png`, `sidebar-icon-button-focus-visible.png`, `sidebar-icon-button-pressed.png`, `sidebar-icon-button-light.png`, `sidebar-icon-button-light-hover.png`, `sidebar-icon-button-light-focus-visible.png`, `sidebar-icon-button-light-pressed.png`.

#### nav-row

Nav row (Images). A 36 tall row with a 20px icon and 14px label. The current destination is filled (`active`).

Page copy: `home-dark`, `library-dark`. Finder: `() => Q('button[data-sidebar-destination="builtin:images"]', 0, S())`.

Dark theme.

| Property | default | hover | focus-visible | pressed | active | active-library |
|---|---|---|---|---|---|---|
| Size (w x h) | 328 x 35 | = | = | = | = | = |
| Padding | 6px 10px | = | = | = | = | = |
| Gap | 8px | = | = | = | = | = |
| Border | none | = | = | = | = | = |
| Radius | 8px | = | = | = | = | = |
| Background | transparent | #ffffff @ 0.1 | = | #ffffff @ 0.1 | #ffffff @ 0.1 | #ffffff @ 0.1 |
| Box shadow | none | = | = | = | = | = |
| Outline | none | = | 2px solid #3a83f7 offset -2px | = | = | = |
| Font | -apple-system-body 14px/20px 400 | = | = | = | = | = |
| Letter spacing | normal | = | = | = | = | = |
| Colour | #ededed | = | = | = | = | = |
| Text node | span.text-fade-truncate: -apple-system-body 14px/20px 400, #ededed @ 0.85 | = | = | = | span.text-fade-truncate: -apple-system-body 14px/20px 400, #ededed | span.text-fade-truncate: -apple-system-body 14px/20px 400, #ededed |
| Transition | none | = | = | = | = | = |
| Cursor | pointer | = | = | = | = | = |
| Icon | 20 x 20, colour #ededed @ 0.85, fill #000000 | = | = | = | 20 x 20, colour #ededed | 20 x 20, colour #ededed |
| Tokens | --height-token-row 36px; --icon-leading-size calc(.25rem * 5); --nav-item-height calc(36px - 1px); --padding-row-cell-x 10px; --padding-row-x 6px; --spacing-nav-row-content calc(.25rem * 1.5) | = | = | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) | at rest, captured active | at rest, captured active-library |
| Painted layers | - | button.sidebar-item.relative.shrink-0 328.0x35.0 bg #ffffff @ 0.1 r 8px | button.sidebar-item.relative.shrink-0 328.0x35.0 r 8px outline 2px solid #3a83f7 offset -2px | button.sidebar-item.relative.shrink-0 328.0x35.0 bg #ffffff @ 0.1 r 8px | button.sidebar-item.relative.shrink-0 328.0x35.0 bg #ffffff @ 0.1 r 8px | button.sidebar-item.relative.shrink-0 328.0x35.0 bg #ffffff @ 0.1 r 8px |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed | light-active | light-active-library |
|---|---|---|---|---|---|---|
| Size (w x h) | 328 x 35 | = | = | = | = | = |
| Padding | 6px 10px | = | = | = | = | = |
| Gap | 8px | = | = | = | = | = |
| Border | none | = | = | = | = | = |
| Radius | 8px | = | = | = | = | = |
| Background | transparent | #000000 @ 0.05 | = | #000000 @ 0.05 | #000000 @ 0.05 | #000000 @ 0.05 |
| Box shadow | none | = | = | = | = | = |
| Outline | none | = | 2px solid #3a83f7 offset -2px | = | = | = |
| Font | -apple-system-body 14px/20px 400 | = | = | = | = | = |
| Letter spacing | normal | = | = | = | = | = |
| Colour | #0d0d0d | = | = | = | = | = |
| Text node | span.text-fade-truncate: -apple-system-body 14px/20px 400, #0d0d0d @ 0.85 | = | = | = | span.text-fade-truncate: -apple-system-body 14px/20px 400, #0d0d0d | span.text-fade-truncate: -apple-system-body 14px/20px 400, #0d0d0d |
| Transition | none | = | = | = | = | = |
| Cursor | pointer | = | = | = | = | = |
| Icon | 20 x 20, colour #0d0d0d @ 0.85, fill #000000 | = | = | = | 20 x 20, colour #0d0d0d | 20 x 20, colour #0d0d0d |
| Tokens | --height-token-row 36px; --icon-leading-size calc(.25rem * 5); --nav-item-height calc(36px - 1px); --padding-row-cell-x 10px; --padding-row-x 6px; --spacing-nav-row-content calc(.25rem * 1.5) | = | = | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) | at rest, captured active | at rest, captured active-library |
| Painted layers | - | button.sidebar-item.relative.shrink-0 328.0x35.0 bg #000000 @ 0.05 r 8px | button.sidebar-item.relative.shrink-0 328.0x35.0 r 8px outline 2px solid #3a83f7 offset -2px | button.sidebar-item.relative.shrink-0 328.0x35.0 bg #000000 @ 0.05 r 8px | button.sidebar-item.relative.shrink-0 328.0x35.0 bg #000000 @ 0.05 r 8px | button.sidebar-item.relative.shrink-0 328.0x35.0 bg #000000 @ 0.05 r 8px |

Other finders: active: `() => C(T('New chat', S()), 'button')`; active-library: `() => Q('button[data-sidebar-destination="builtin:library"]', 0, S())`; light-active-library: `() => Q('button[data-sidebar-destination="builtin:library"]', 0, S())`; light-active: `() => C(T('New chat', S()), 'button')`.

Crops: `nav-row-default.png`, `nav-row-hover.png`, `nav-row-focus-visible.png`, `nav-row-pressed.png`, `nav-row-active.png`, `nav-row-active-library.png`, `nav-row-light.png`, `nav-row-light-hover.png`, `nav-row-light-focus-visible.png`, `nav-row-light-pressed.png`, `nav-row-light-active.png`, `nav-row-light-active-library.png`.

#### section-toggle

Section header (Pinned). Collapsible section label in tertiary text.

Page copy: `home-dark`. Finder: `() => Q('button[data-app-action-sidebar-section-toggle]', 0, S())`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 316 x 36 | = | = |
| Padding | 2px 4px | = | = |
| Gap | 4px | = | = |
| Border | none | = | = |
| Radius | 6px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #3a83f7 offset 0px |
| Font | -apple-system-body 14px/18px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #afafaf | = | = |
| Text node | span.min-w-0.truncate: -apple-system-body 14px/18px 500, #afafaf | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 12 x 12, colour #afafaf | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |
| Painted layers | - | = | button.group/section-toggle.-ms-1.flex 316.0x36.0 r 6px outline 2px solid #3a83f7 offset 0px |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 316 x 36 | = | = |
| Padding | 2px 4px | = | = |
| Gap | 4px | = | = |
| Border | none | = | = |
| Radius | 6px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #3a83f7 offset 0px |
| Font | -apple-system-body 14px/18px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #8f8f8f | = | = |
| Text node | span.min-w-0.truncate: -apple-system-body 14px/18px 500, #8f8f8f | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 12 x 12, colour #8f8f8f | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |
| Painted layers | - | = | button.group/section-toggle.-ms-1.flex 316.0x36.0 r 6px outline 2px solid #3a83f7 offset 0px |

Crops: `section-toggle-default.png`, `section-toggle-hover.png`, `section-toggle-focus-visible.png`, `section-toggle-light.png`, `section-toggle-light-hover.png`, `section-toggle-light-focus-visible.png`.

#### chat-row

List row (sidebar chat). A chat in Recents: 36 tall, full radius (`--radius-token-row`), the title truncated; hover fills it and shows Chat actions and Pin. The open chat is filled (`active`).

Page copy: `home-dark`, `thread-dark-code`. Finder: `() => H(Q('a[data-interactive-row-link]', 2, S()), 30)`.

Dark theme.

| Property | default | hover | active |
|---|---|---|---|
| Size (w x h) | 328 x 36 | = | = |
| Padding | 6px 6px 6px 10px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | #ffffff @ 0.1 | #ffffff @ 0.1 |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ededed | = | = |
| Text node | span: -apple-system-body 14px/20px 400, #ededed @ 0.85 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 14 x 14, colour #cdcdcd, fill #000000 | = | = |
| Tokens | --height-token-row 36px; --padding-row-cell-x 10px; --padding-row-x 6px | = | --color-text color-mix(in oklab, #ededed 85%, transparent); --height-token-row 36px; --padding-row-cell-x 10px; --padding-row-x 6px |
| How | at rest | mouse hover on its row | at rest, captured active |
| Painted layers | - | div.group.relative.cursor-interaction 328.0x36.0 bg #ffffff @ 0.1 r 8px | div.group.relative.cursor-interaction 328.0x36.0 bg #ffffff @ 0.1 r 8px |

Light theme.

| Property | light | light-hover | light-active |
|---|---|---|---|
| Size (w x h) | 328 x 36 | = | = |
| Padding | 6px 6px 6px 10px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | #000000 @ 0.05 | #000000 @ 0.05 |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0d0d0d | = | = |
| Text node | span: -apple-system-body 14px/20px 400, #0d0d0d @ 0.85 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 14 x 14, colour #5d5d5d, fill #000000 | = | = |
| Tokens | --height-token-row 36px; --padding-row-cell-x 10px; --padding-row-x 6px | = | --color-text color-mix(in oklab, #0d0d0d 85%, transparent); --height-token-row 36px; --padding-row-cell-x 10px; --padding-row-x 6px |
| How | at rest | mouse hover on its row | at rest, captured active |
| Painted layers | - | div.group.relative.cursor-interaction 328.0x36.0 bg #000000 @ 0.05 r 8px | div.group.relative.cursor-interaction 328.0x36.0 bg #000000 @ 0.05 r 8px |

Other finders: active: `() => P(QA('a[aria-current=page]', 0, S()))`; light-active: `() => P(QA('a[aria-current=page]', 0, S()))`.

Crops: `chat-row-default.png`, `chat-row-hover.png`, `chat-row-active.png`, `chat-row-light.png`, `chat-row-light-hover.png`, `chat-row-light-active.png`.

#### chat-row-link

Chat row link (keyboard focus). The row's own link, focused from the keyboard.

Page copy: `home-dark`. Finder: `() => Q('a[data-interactive-row-link]', 2, S())`.

Dark theme.

| Property | focus-visible |
|---|---|
| Size (w x h) | 253 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | 1px auto #99c8ff offset 1px |
| Font | -apple-system-body 14px/20px 400 |
| Letter spacing | normal |
| Colour | #ededed @ 0.85 |
| Text node | span: -apple-system-body 14px/20px 400, #ededed @ 0.85 |
| Transition | none |
| Cursor | pointer |
| ::before | 328px x 36px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | a.flex.min-w-0.flex-1 253.0x20.0 outline 1px auto #99c8ff offset 1px; a.flex.min-w-0.flex-1::before 328pxx36px outline 2px solid #3a83f7 offset -2px |
| How | keyboard: focus(), Shift+Tab, Tab |

Light theme.

| Property | light-focus-visible |
|---|---|
| Size (w x h) | 253 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | 1px auto #005fcc offset 1px |
| Font | -apple-system-body 14px/20px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d @ 0.85 |
| Text node | span: -apple-system-body 14px/20px 400, #0d0d0d @ 0.85 |
| Transition | none |
| Cursor | pointer |
| ::before | 328px x 36px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | a.flex.min-w-0.flex-1 253.0x20.0 outline 1px auto #005fcc offset 1px; a.flex.min-w-0.flex-1::before 328pxx36px outline 2px solid #3a83f7 offset -2px |
| How | keyboard: focus(), Shift+Tab, Tab |

Crops: `chat-row-link-focus-visible.png`, `chat-row-link-light-focus-visible.png`.

#### chat-row-actions

Chat actions button. A 20x20 `Button` (size 3xs, transparent, pill), shown when its row is hovered; measured while the row is hovered.

Page copy: `home-dark`. Finder: `() => QA('button[aria-label="Chat actions"]', 2, S())`.

Dark theme.

| Property | hover |
|---|---|
| Size (w x h) | 20 x 20 |
| Padding | 0px |
| Gap | 3px |
| Border | none |
| Radius | 9999px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 12px/12px 500 |
| Letter spacing | normal |
| Colour | #cdcdcd |
| Transition | opacity, color 0.15s ease |
| Cursor | pointer |
| Icon | 14 x 14, colour #cdcdcd, fill #000000 |
| ::after | 20px x 20px, absolute, bg #000000 @ 0, radius 9999px |
| How | mouse hover on its row |

Light theme.

| Property | light-hover |
|---|---|
| Size (w x h) | 20 x 20 |
| Padding | 0px |
| Gap | 3px |
| Border | none |
| Radius | 9999px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 12px/12px 500 |
| Letter spacing | normal |
| Colour | #5d5d5d |
| Transition | opacity, color 0.15s ease |
| Cursor | pointer |
| Icon | 14 x 14, colour #5d5d5d, fill #000000 |
| ::after | 20px x 20px, absolute, bg #000000 @ 0, radius 9999px |
| How | mouse hover on its row |

Crops: `chat-row-actions-hover.png`, `chat-row-actions-light-hover.png`.

#### project-row

Project row. Each project with its own icon; hover reveals project actions and a new-chat button.

Page copy: `home-dark`. Finder: `() => Q('[data-app-action-sidebar-project-row]', 0, S())`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 328 x 36 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | #ffffff @ 0.1 | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #3a83f7 offset -2px |
| Font | -apple-system-body 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ededed @ 0.85 | = | = |
| Text node | span.content-I_RXQY: -apple-system-body 14px/20px 400, #ededed @ 0.85 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 19.5 x 19.5, colour #ededed | = | = |
| Tokens | --height-token-row 36px; --sidebar-row-action-opacity 0; --sidebar-row-action-width auto; --sidebar-row-menu-overflow hidden; --sidebar-row-menu-width 0px | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |
| Painted layers | - | div.group.relative.cursor-interaction 328.0x36.0 bg #ffffff @ 0.1 r 8px | div.group.relative.cursor-interaction 328.0x36.0 r 8px outline 2px solid #3a83f7 offset -2px |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 328 x 36 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | #000000 @ 0.05 | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #3a83f7 offset -2px |
| Font | -apple-system-body 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0d0d0d @ 0.85 | = | = |
| Text node | span.content-I_RXQY: -apple-system-body 14px/20px 400, #0d0d0d @ 0.85 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 19.5 x 19.5, colour #0d0d0d | = | = |
| Tokens | --height-token-row 36px; --sidebar-row-action-opacity 0; --sidebar-row-action-width auto; --sidebar-row-menu-overflow hidden; --sidebar-row-menu-width 0px | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |
| Painted layers | - | div.group.relative.cursor-interaction 328.0x36.0 bg #000000 @ 0.05 r 8px | div.group.relative.cursor-interaction 328.0x36.0 r 8px outline 2px solid #3a83f7 offset -2px |

Crops: `project-row-default.png`, `project-row-hover.png`, `project-row-focus-visible.png`, `project-row-light.png`, `project-row-light-hover.png`, `project-row-light-focus-visible.png`.

#### account-row

Account row. `Button` primary ghost size 4xl: the 24px avatar, the name over the plan.

Page copy: `home-dark`, `home-dark-user-menu`. Finder: `() => Q('button[aria-label="Open profile menu"]', 0, S())`.

Dark theme.

| Property | default | hover | focus-visible | pressed | open |
|---|---|---|---|---|---|
| Size (w x h) | 248.11 x 48 | = | = | = | = |
| Padding | 0px 8px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 12px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | -apple-system-body 16px/16px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ededed | = | = | = | = |
| Text node | div.shrink-0.object-cover.rounded-full: -apple-system-body 12px/12px 600, #ffffff | = | = | = | = |
| Transition | opacity, color 0.15s ease | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| ::before | 248.109px x 48px, absolute, bg #ffffff @ 0.1, radius 12px | = | = | 248.109px x 48px, absolute, bg #ededed @ 0.16, radius 12px | = |
| ::after | 248.109px x 48px, absolute, bg #000000 @ 0, radius 12px | = | = | = | = |
| Painted layers | button.Button-QTscM8.outline-hidden.cursor-interaction::before 248.109pxx48px bg #ffffff @ 0.1 r 12px opacity 0; div.shrink-0.object-cover.rounded-full 24.0x24.0 bg #8a8a8a r 9999px | button.Button-QTscM8.outline-hidden.cursor-interaction::before 248.109pxx48px bg #ffffff @ 0.1 r 12px; div.shrink-0.object-cover.rounded-full 24.0x24.0 bg #8a8a8a r 9999px | button.Button-QTscM8.outline-hidden.cursor-interaction::before 248.109pxx48px bg #ffffff @ 0.1 r 12px opacity 0; button.Button-QTscM8.outline-hidden.cursor-interaction::after 248.109pxx48px r 12px outline 2px solid #3a83f7 offset -1px; div.shrink-0.object-cover.rounded-full 24.0x24.0 bg #8a8a8a r 9999px | button.Button-QTscM8.outline-hidden.cursor-interaction::before 248.109pxx48px bg #ededed @ 0.16 r 12px; div.shrink-0.object-cover.rounded-full 24.0x24.0 bg #8a8a8a r 9999px | button.Button-QTscM8.outline-hidden.cursor-interaction::before 248.109pxx48px bg #ffffff @ 0.1 r 12px opacity 0.6; div.shrink-0.object-cover.rounded-full 24.0x24.0 bg #8a8a8a r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) | at rest, captured open |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed | light-open |
|---|---|---|---|---|---|
| Size (w x h) | 248.11 x 48 | = | = | = | = |
| Padding | 0px 8px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 12px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | -apple-system-body 16px/16px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #0d0d0d | = | = | = | = |
| Text node | div.shrink-0.object-cover.rounded-full: -apple-system-body 12px/12px 600, #ffffff | = | = | = | = |
| Transition | opacity, color 0.15s ease | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| ::before | 248.109px x 48px, absolute, bg #000000 @ 0.05, radius 12px | = | = | 248.109px x 48px, absolute, bg #0d0d0d @ 0.12, radius 12px | = |
| ::after | 248.109px x 48px, absolute, bg #000000 @ 0, radius 12px | = | = | = | = |
| Painted layers | button.Button-QTscM8.outline-hidden.cursor-interaction::before 248.109pxx48px bg #000000 @ 0.05 r 12px opacity 0; div.shrink-0.object-cover.rounded-full 24.0x24.0 bg #8a8a8a r 9999px | button.Button-QTscM8.outline-hidden.cursor-interaction::before 248.109pxx48px bg #000000 @ 0.05 r 12px; div.shrink-0.object-cover.rounded-full 24.0x24.0 bg #8a8a8a r 9999px | button.Button-QTscM8.outline-hidden.cursor-interaction::before 248.109pxx48px bg #000000 @ 0.05 r 12px opacity 0; button.Button-QTscM8.outline-hidden.cursor-interaction::after 248.109pxx48px r 12px outline 2px solid #3a83f7 offset -1px; div.shrink-0.object-cover.rounded-full 24.0x24.0 bg #8a8a8a r 9999px | button.Button-QTscM8.outline-hidden.cursor-interaction::before 248.109pxx48px bg #0d0d0d @ 0.12 r 12px; div.shrink-0.object-cover.rounded-full 24.0x24.0 bg #8a8a8a r 9999px | button.Button-QTscM8.outline-hidden.cursor-interaction::before 248.109pxx48px bg #000000 @ 0.05 r 12px opacity 0.6; div.shrink-0.object-cover.rounded-full 24.0x24.0 bg #8a8a8a r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) | at rest, captured open |

Other finders: open: `() => Q('button[aria-label="Open profile menu"]', 0, S())`; light-open: `() => Q('button[aria-label="Open profile menu"]', 0, S())`.

Crops: `account-row-default.png`, `account-row-hover.png`, `account-row-focus-visible.png`, `account-row-pressed.png`, `account-row-open.png`, `account-row-light.png`, `account-row-light-hover.png`, `account-row-light-focus-visible.png`, `account-row-light-pressed.png`, `account-row-light-open.png`.

#### avatar

Avatar. Redacted to a grey disc with an L; the real one is the account photo at 24px.

Page copy: `home-dark`. Finder: `() => Q('button[aria-label="Open profile menu"] .rounded-full', 0, S())`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 24 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 9999px |
| Background | #8a8a8a |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 12px/12px 600 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.shrink-0.object-cover.rounded-full 24.0x24.0 bg #8a8a8a r 9999px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 24 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 9999px |
| Background | #8a8a8a |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 12px/12px 600 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.shrink-0.object-cover.rounded-full 24.0x24.0 bg #8a8a8a r 9999px |
| How | at rest |

Crops: `avatar-default.png`, `avatar-light.png`.

#### sidebar-upgrade

Outline pill button (account Upgrade).

Page copy: `home-dark`. Finder: `() => C(T('Upgrade', S()), 'button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 71.89 x 28 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #ffffff @ 0.15 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #212121 | #2f2f2f | = | #2f2f2f |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 71.9x28.0 bg #212121 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px | button.no-drag.cursor-interaction.items-center 71.9x28.0 bg #2f2f2f border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px | button.no-drag.cursor-interaction.items-center 71.9x28.0 bg #212121 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 71.9x28.0 bg #2f2f2f border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px opacity 0.8 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |
| Opacity | - | = | = | 0.8 |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 71.89 x 28 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0.15 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | #f9f9f9 | = | #f9f9f9 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 71.9x28.0 bg #ffffff border T:1px solid #000000 @ 0.15 / R:1px solid #000000 @ 0.15 / B:1px solid #000000 @ 0.15 / L:1px solid #000000 @ 0.15 r 9999px | button.no-drag.cursor-interaction.items-center 71.9x28.0 bg #f9f9f9 border T:1px solid #000000 @ 0.15 / R:1px solid #000000 @ 0.15 / B:1px solid #000000 @ 0.15 / L:1px solid #000000 @ 0.15 r 9999px | button.no-drag.cursor-interaction.items-center 71.9x28.0 bg #ffffff border T:1px solid #000000 @ 0.15 / R:1px solid #000000 @ 0.15 / B:1px solid #000000 @ 0.15 / L:1px solid #000000 @ 0.15 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 71.9x28.0 bg #f9f9f9 border T:1px solid #000000 @ 0.15 / R:1px solid #000000 @ 0.15 / B:1px solid #000000 @ 0.15 / L:1px solid #000000 @ 0.15 r 9999px opacity 0.8 |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |
| Opacity | - | = | = | 0.8 |

Crops: `sidebar-upgrade-default.png`, `sidebar-upgrade-hover.png`, `sidebar-upgrade-focus-visible.png`, `sidebar-upgrade-pressed.png`, `sidebar-upgrade-light.png`, `sidebar-upgrade-light-hover.png`, `sidebar-upgrade-light-focus-visible.png`, `sidebar-upgrade-light-pressed.png`.

#### sidebar-rail

Sidebar collapsed to the rail. 52 wide: show sidebar, new chat, search, pinned, recents, library, then the avatar.

Page copy: `home-dark-sidebar-collapsed`. Finder: `() => S()`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 52 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | div.shrink-0.object-cover.rounded-full: -apple-system-body 12px/12px 600, #ffffff |
| Transition | none |
| Icon | 24 x 24, colour #ededed |
| Painted layers | aside.app-shell-left-panel.pointer-events-auto.relative 52.0x900.0 bg #000000; nav.group/sidebar-rail.pointer-events-none.relative 52.0x900.0 bg #000000; button.Button-QTscM8.group/sidebar-trigger.cursor-e-resize::before 36pxx36px bg #ffffff @ 0.1 r 8px opacity 0; button.sidebar-item.relative.shrink-0 36.0x35.0 bg #ffffff @ 0.1 r 8px; button.Button-QTscM8.outline-hidden.cursor-interaction::before 36pxx36px bg #ffffff @ 0.1 r 8px opacity 0; div.shrink-0.object-cover.rounded-full 24.0x24.0 bg #8a8a8a r 9999px |
| Tokens | --color-text-primary-ghost #ededed; --color-text-tertiary #afafaf; --height-token-row calc(16px * 1.5 + calc(.25rem * 1) * 2); --icon-leading-size calc(.25rem * 5); --padding-row-x calc(.25rem * 2); --spacing-nav-row-content calc(.25rem * 1.5) |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 52 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fcfcfc |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | div.shrink-0.object-cover.rounded-full: -apple-system-body 12px/12px 600, #ffffff |
| Transition | none |
| Icon | 24 x 24, colour #0d0d0d |
| Painted layers | aside.app-shell-left-panel.pointer-events-auto.relative 52.0x900.0 bg #fcfcfc; nav.group/sidebar-rail.pointer-events-none.relative 52.0x900.0 bg #fcfcfc; button.Button-QTscM8.group/sidebar-trigger.cursor-e-resize::before 36pxx36px bg #000000 @ 0.05 r 8px opacity 0; button.sidebar-item.relative.shrink-0 36.0x35.0 bg #000000 @ 0.05 r 8px; button.Button-QTscM8.outline-hidden.cursor-interaction::before 36pxx36px bg #000000 @ 0.05 r 8px opacity 0; div.shrink-0.object-cover.rounded-full 24.0x24.0 bg #8a8a8a r 9999px |
| Tokens | --color-text-primary-ghost #0d0d0d; --color-text-tertiary #8f8f8f; --height-token-row calc(16px * 1.5 + calc(.25rem * 1) * 2); --icon-leading-size calc(.25rem * 5); --padding-row-x calc(.25rem * 2); --spacing-nav-row-content calc(.25rem * 1.5) |
| How | at rest |

Crops: `sidebar-rail-default.png`, `sidebar-rail-light.png`.

#### rail-button

Rail button (New chat).

Page copy: `home-dark-sidebar-collapsed`. Finder: `() => C(T('New chat', S()), 'button') // Q('button[data-sidebar-cycle-item]', 0, S())`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 36 x 35 | = | = |
| Padding | 5px 8px | = | = |
| Gap | 8px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | #ffffff @ 0.1 | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #3a83f7 offset -2px |
| Font | -apple-system-body 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ededed | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 19.5 x 19.5, colour #ededed | = | = |
| Painted layers | button.sidebar-item.relative.shrink-0 36.0x35.0 bg #ffffff @ 0.1 r 8px | = | button.sidebar-item.relative.shrink-0 36.0x35.0 bg #ffffff @ 0.1 r 8px outline 2px solid #3a83f7 offset -2px |
| Tokens | --height-token-row 36px; --icon-leading-size calc(.25rem * 5); --nav-item-height calc(36px - 1px); --padding-row-cell-x 8px; --padding-row-x 8px; --spacing-nav-row-content calc(.25rem * 1.5) | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 36 x 35 | = | = |
| Padding | 5px 8px | = | = |
| Gap | 8px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | #000000 @ 0.05 | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #3a83f7 offset -2px |
| Font | -apple-system-body 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0d0d0d | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 19.5 x 19.5, colour #0d0d0d | = | = |
| Painted layers | button.sidebar-item.relative.shrink-0 36.0x35.0 bg #000000 @ 0.05 r 8px | = | button.sidebar-item.relative.shrink-0 36.0x35.0 bg #000000 @ 0.05 r 8px outline 2px solid #3a83f7 offset -2px |
| Tokens | --height-token-row 36px; --icon-leading-size calc(.25rem * 5); --nav-item-height calc(36px - 1px); --padding-row-cell-x 8px; --padding-row-x 8px; --spacing-nav-row-content calc(.25rem * 1.5) | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |

Crops: `rail-button-default.png`, `rail-button-hover.png`, `rail-button-focus-visible.png`, `rail-button-light.png`, `rail-button-light-hover.png`, `rail-button-light-focus-visible.png`.

### Top bar

#### page-header

Page header. 52 tall: the Chat / Work toggle centred, Upgrade and temporary chat at the end.

Page copy: `home-dark`. Finder: `() => QA('[data-testid=app-shell-header-context-menu-surface]') // W(B('Temporary chat'), 1000)`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 1100 x 52 |
| Padding | 0px 8px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | button.no-drag.cursor-interaction.items-center: -apple-system-body 14px/20px 500, #63a8f8 |
| Transition | none |
| Icon | 20 x 20, colour #63a8f8, fill #000000 |
| Painted layers | button.no-drag.cursor-interaction.items-center 106.2x34.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| Tokens | --height-toolbar calc(.25rem * 13) |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 1100 x 52 |
| Padding | 0px 8px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | button.no-drag.cursor-interaction.items-center: -apple-system-body 14px/20px 500, #3a83f7 |
| Transition | none |
| Icon | 20 x 20, colour #3a83f7, fill #000000 |
| Painted layers | button.no-drag.cursor-interaction.items-center 106.2x34.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| Tokens | --height-toolbar calc(.25rem * 13) |
| How | at rest |

Crops: `page-header-default.png`, `page-header-light.png`.

#### mode-toggle

Chat / Work segmented toggle. A pill track with two 112x36 segments; the selected one carries a filled thumb.

Page copy: `home-dark`. Finder: `() => P(C(T('Chat', M()), 'button').parentElement)`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 1100 x 900 |
| Padding | 0px |
| Border | T: none; R: none; B: none; L: 1px solid #ffffff @ 0.15 |
| Radius | 0px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | button.no-drag.cursor-interaction.items-center: -apple-system-body 14px/20px 500, #63a8f8 |
| Transition | none |
| Icon | 20 x 20, colour #63a8f8, fill #000000 |
| Placeholder | "Ask ChatGPT" #afafaf, opacity 1, 16px |
| Painted layers | main.outline-none.MainContentSurface-EnuIYE.MainContentLeftBorder-IFAvO_ 1100.0x900.0 bg #000000 border L:1px solid #ffffff @ 0.15; button.no-drag.cursor-interaction.items-center 106.2x34.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; span.pointer-events-none.absolute.inset-x-px 222.0x34.0 bg #131313 r 9999px; span.pointer-events-none.relative.z-10 121.0x37.0 bg #1b1b1b border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px opacity 0 |
| Tokens | --app-shell-application-menu-height 0px; --app-shell-page-banner-height 0px; --app-shell-root-banner-height 0px; --app-shell-titlebar-height calc(.25rem * 13); --color-text-primary-ghost #ededed; --color-text-tertiary #afafaf; --height-toolbar calc(.25rem * 13); --spacing .25rem; --spacing-token-safe-header-left 6px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 1100 x 900 |
| Padding | 0px |
| Border | T: none; R: none; B: none; L: 1px solid #000000 @ 0.1 |
| Radius | 0px |
| Background | #fcfcfc |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | button.no-drag.cursor-interaction.items-center: -apple-system-body 14px/20px 500, #3a83f7 |
| Transition | none |
| Icon | 20 x 20, colour #3a83f7, fill #000000 |
| Placeholder | "Ask ChatGPT" #8f8f8f, opacity 1, 16px |
| Painted layers | main.outline-none.MainContentSurface-EnuIYE.MainContentLeftBorder-IFAvO_ 1100.0x900.0 bg #fcfcfc border L:1px solid #000000 @ 0.1; button.no-drag.cursor-interaction.items-center 106.2x34.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; span.pointer-events-none.absolute.inset-x-px 222.0x34.0 bg #0d0d0d @ 0.03 r 9999px; span.pointer-events-none.relative.z-10 121.0x37.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px shadow #000000 @ 0.05 0px 1px 6px 0px; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px opacity 0 |
| Tokens | --app-shell-application-menu-height 0px; --app-shell-page-banner-height 0px; --app-shell-root-banner-height 0px; --app-shell-titlebar-height calc(.25rem * 13); --color-text-primary-ghost #0d0d0d; --color-text-tertiary #8f8f8f; --height-toolbar calc(.25rem * 13); --spacing .25rem; --spacing-token-safe-header-left 6px |
| How | at rest |

Crops: `mode-toggle-default.png`, `mode-toggle-light.png`.

#### mode-segment

Mode segment (Work, not selected).

Page copy: `home-dark`. Finder: `() => C(TS('Work', M()), 'button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed | selected | selected-hover |
|---|---|---|---|---|---|---|
| Size (w x h) | 112 x 36 | = | = | = | = | = |
| Padding | 0px 14px 0px 6px | = | = | = | 0px 6px 0px 14px | 0px 6px 0px 14px |
| Border | none | = | = | = | = | = |
| Radius | 9999px | = | = | = | = | = |
| Background | transparent | = | = | = | = | = |
| Box shadow | none | = | = | = | = | = |
| Outline | none | = | 1px auto #99c8ff offset 0px | = | = | = |
| Font | -apple-system-body 14px/20px 500 | = | = | = | = | = |
| Letter spacing | normal | = | = | = | = | = |
| Colour | #cdcdcd | #ffffff | #ffffff | #ffffff | #ffffff | #ffffff |
| Text node | span.relative.inline-flex.items-center: -apple-system-body 14px/20px 500, #ffffff | = | = | = | - | - |
| Transition | none | = | = | = | = | = |
| Cursor | pointer | = | = | = | = | = |
| Icon | 12 x 12, colour #ffffff, fill #000000 | = | = | = | - | - |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) | at rest, captured selected | mouse hover |
| Painted layers | - | = | button.cursor-interaction.relative.z-10 112.0x36.0 r 9999px outline 1px auto #99c8ff offset 0px | = | = | = |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed | light-selected | light-selected-hover |
|---|---|---|---|---|---|---|
| Size (w x h) | 112 x 36 | = | = | = | = | = |
| Padding | 0px 14px 0px 6px | = | = | = | 0px 6px 0px 14px | 0px 6px 0px 14px |
| Border | none | = | = | = | = | = |
| Radius | 9999px | = | = | = | = | = |
| Background | transparent | = | = | = | = | = |
| Box shadow | none | = | = | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = | = | = |
| Font | -apple-system-body 14px/20px 500 | = | = | = | = | = |
| Letter spacing | normal | = | = | = | = | = |
| Colour | #5d5d5d | #0d0d0d | #0d0d0d | #0d0d0d | #0d0d0d | #0d0d0d |
| Text node | span.relative.inline-flex.items-center: -apple-system-body 14px/20px 500, #0d0d0d | = | = | = | - | - |
| Transition | none | = | = | = | = | = |
| Cursor | pointer | = | = | = | = | = |
| Icon | 12 x 12, colour #0d0d0d, fill #000000 | = | = | = | - | - |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) | at rest, captured selected | mouse hover |
| Painted layers | - | = | button.cursor-interaction.relative.z-10 112.0x36.0 r 9999px outline 1px auto #005fcc offset 0px | = | = | = |

Other finders: selected: `() => C(T('Chat', M()), 'button')`; selected-hover: `() => C(T('Chat', M()), 'button')`; light-selected: `() => C(T('Chat', M()), 'button')`; light-selected-hover: `() => C(T('Chat', M()), 'button')`.

Crops: `mode-segment-default.png`, `mode-segment-hover.png`, `mode-segment-focus-visible.png`, `mode-segment-pressed.png`, `mode-segment-selected.png`, `mode-segment-selected-hover.png`, `mode-segment-light.png`, `mode-segment-light-hover.png`, `mode-segment-light-focus-visible.png`, `mode-segment-light-pressed.png`, `mode-segment-light-selected.png`, `mode-segment-light-selected-hover.png`.

#### header-upgrade

Link-style button (header Upgrade). Transparent pill, accent sparkle and label in `--color-text-header-upgrade`.

Page copy: `home-dark`. Finder: `() => B('Upgrade', QA('header') // document)`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106.16 x 34 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 3px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #a4cdfb @ 0.2 | #a4cdfb @ 0.2 | #a4cdfb @ 0.2 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #63a8f8 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #63a8f8, fill #000000 | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 106.2x34.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.no-drag.cursor-interaction.items-center 106.2x34.0 bg #a4cdfb @ 0.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.no-drag.cursor-interaction.items-center 106.2x34.0 bg #a4cdfb @ 0.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 106.2x34.0 bg #a4cdfb @ 0.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 106.16 x 34 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 3px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #3a83f7 @ 0.09 | #3a83f7 @ 0.09 | #3a83f7 @ 0.09 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #3a83f7 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #3a83f7, fill #000000 | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 106.2x34.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.no-drag.cursor-interaction.items-center 106.2x34.0 bg #3a83f7 @ 0.09 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.no-drag.cursor-interaction.items-center 106.2x34.0 bg #3a83f7 @ 0.09 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 106.2x34.0 bg #3a83f7 @ 0.09 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `header-upgrade-default.png`, `header-upgrade-hover.png`, `header-upgrade-focus-visible.png`, `header-upgrade-pressed.png`, `header-upgrade-light.png`, `header-upgrade-light-hover.png`, `header-upgrade-light-focus-visible.png`, `header-upgrade-light-pressed.png`.

#### header-icon-button

Icon button (Temporary chat).

Page copy: `home-dark`. Finder: `() => Q('button[aria-label="Temporary chat"]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #ffffff @ 0.1 | = | #ffffff @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ededed | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ededed, fill #000000 | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #ffffff @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #ffffff @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #000000 @ 0.05 | = | #000000 @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #0d0d0d, fill #000000 | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `header-icon-button-default.png`, `header-icon-button-hover.png`, `header-icon-button-focus-visible.png`, `header-icon-button-pressed.png`, `header-icon-button-light.png`, `header-icon-button-light-hover.png`, `header-icon-button-light-focus-visible.png`, `header-icon-button-light-pressed.png`.

#### share-button

Secondary button (Share).

Page copy: `thread-dark-code`. Finder: `() => B('Share')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 87.27 x 36 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #ffffff @ 0.1 | = | #ffffff @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ededed | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ededed, fill #000000 | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 87.3x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.no-drag.cursor-interaction.items-center 87.3x36.0 bg #ffffff @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.no-drag.cursor-interaction.items-center 87.3x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 87.3x36.0 bg #ffffff @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| Ancestor paint | 1 up div.flex.items-center.gap-toolbar-action bg #000000 | = | = | = |
| Tokens | --color-text-toolbar-action #ededed | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 87.27 x 36 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #000000 @ 0.05 | = | #000000 @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #0d0d0d, fill #000000 | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 87.3x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.no-drag.cursor-interaction.items-center 87.3x36.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.no-drag.cursor-interaction.items-center 87.3x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 87.3x36.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| Ancestor paint | 1 up div.flex.items-center.gap-toolbar-action bg #fcfcfc | = | = | = |
| Tokens | --color-text-toolbar-action #0d0d0d | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `share-button-default.png`, `share-button-hover.png`, `share-button-focus-visible.png`, `share-button-pressed.png`, `share-button-light.png`, `share-button-light-hover.png`, `share-button-light-focus-visible.png`, `share-button-light-pressed.png`.

#### more-button

Icon button (More, thread).

Page copy: `thread-dark-code`. Finder: `() => Q('button[aria-label="More"]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ededed | = | = | = |
| Transition | opacity, color 0.15s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ededed, fill #000000 | = | = | = |
| ::before | 36px x 36px, absolute, bg #ffffff @ 0.1, radius 8px | = | = | 36px x 36px, absolute, bg #ededed @ 0.16, radius 8px |
| ::after | 36px x 36px, absolute, bg #000000 @ 0, radius 8px | = | = | = |
| Painted layers | button.Button-QTscM8.Toolbar-TcAqyt.no-drag::before 36pxx36px bg #ffffff @ 0.1 r 8px opacity 0 | button.Button-QTscM8.Toolbar-TcAqyt.no-drag::before 36pxx36px bg #ffffff @ 0.1 r 8px | button.Button-QTscM8.Toolbar-TcAqyt.no-drag::before 36pxx36px bg #ffffff @ 0.1 r 8px opacity 0; button.Button-QTscM8.Toolbar-TcAqyt.no-drag::after 36pxx36px r 8px outline 2px solid #3a83f7 offset -1px | button.Button-QTscM8.Toolbar-TcAqyt.no-drag::before 36pxx36px bg #ededed @ 0.16 r 8px |
| Ancestor paint | 1 up div.flex.items-center.gap-toolbar-action bg #000000 | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | opacity, color 0.15s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #0d0d0d, fill #000000 | = | = | = |
| ::before | 36px x 36px, absolute, bg #000000 @ 0.05, radius 8px | = | = | 36px x 36px, absolute, bg #0d0d0d @ 0.12, radius 8px |
| ::after | 36px x 36px, absolute, bg #000000 @ 0, radius 8px | = | = | = |
| Painted layers | button.Button-QTscM8.Toolbar-TcAqyt.no-drag::before 36pxx36px bg #000000 @ 0.05 r 8px opacity 0 | button.Button-QTscM8.Toolbar-TcAqyt.no-drag::before 36pxx36px bg #000000 @ 0.05 r 8px | button.Button-QTscM8.Toolbar-TcAqyt.no-drag::before 36pxx36px bg #000000 @ 0.05 r 8px opacity 0; button.Button-QTscM8.Toolbar-TcAqyt.no-drag::after 36pxx36px r 8px outline 2px solid #3a83f7 offset -1px | button.Button-QTscM8.Toolbar-TcAqyt.no-drag::before 36pxx36px bg #0d0d0d @ 0.12 r 8px |
| Ancestor paint | 1 up div.flex.items-center.gap-toolbar-action bg #fcfcfc | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `more-button-default.png`, `more-button-hover.png`, `more-button-focus-visible.png`, `more-button-pressed.png`, `more-button-light.png`, `more-button-light-hover.png`, `more-button-light-focus-visible.png`, `more-button-light-pressed.png`.

### Home

#### home-heading

Home heading.

Page copy: `home-dark`. Finder: `() => T('Ready when you are.')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 212.8 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 24px/28.8px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | span: -apple-system-body 24px/28.8px 400, #ededed |
| Transition | none |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 212.8 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 24px/28.8px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span: -apple-system-body 24px/28.8px 400, #0d0d0d |
| Transition | none |
| How | at rest |

Crops: `home-heading-default.png`, `home-heading-light.png`.

#### suggestion-row

Suggestion row. 768x52, icon and 16px tertiary text; hover fills with `--color-background-home-suggestion-hover`.

Page copy: `home-dark`. Finder: `() => C(T('Write or edit'), 'button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 768 x 52 | = | = | = |
| Padding | 0px 44px 0px 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/26px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #afafaf | #ededed | #ededed | #ededed |
| Text node | span.min-w-0.flex-1.truncate: -apple-system-body 16px/26px 400, #afafaf | span.min-w-0.flex-1.truncate: -apple-system-body 16px/26px 400, #ededed | span.min-w-0.flex-1.truncate: -apple-system-body 16px/26px 400, #ededed | span.min-w-0.flex-1.truncate: -apple-system-body 16px/26px 400, #ededed |
| Transition | color 0.075s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Tokens | --spacing .25rem; --spacing-composer-single-line-controls calc(.25rem * 2); --spacing-token-button-composer calc(.25rem * 9) | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |
| Ancestor paint | - | 1 up div.group/home-suggestion-list-item.relative.rounded-2xl bg #ffffff @ 0.1 | 1 up div.group/home-suggestion-list-item.relative.rounded-2xl bg #ffffff @ 0.1 | 1 up div.group/home-suggestion-list-item.relative.rounded-2xl bg #ffffff @ 0.1 |
| Painted layers | - | = | button.cursor-interaction.outline-none.flex 768.0x52.0 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 768 x 52 | = | = | = |
| Padding | 0px 44px 0px 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/26px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #8f8f8f | #0d0d0d | #0d0d0d | #0d0d0d |
| Text node | span.min-w-0.flex-1.truncate: -apple-system-body 16px/26px 400, #8f8f8f | span.min-w-0.flex-1.truncate: -apple-system-body 16px/26px 400, #0d0d0d | span.min-w-0.flex-1.truncate: -apple-system-body 16px/26px 400, #0d0d0d | span.min-w-0.flex-1.truncate: -apple-system-body 16px/26px 400, #0d0d0d |
| Transition | color 0.075s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Tokens | --spacing .25rem; --spacing-composer-single-line-controls calc(.25rem * 2); --spacing-token-button-composer calc(.25rem * 9) | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |
| Ancestor paint | - | 1 up div.group/home-suggestion-list-item.relative.rounded-2xl bg #000000 @ 0.05 | 1 up div.group/home-suggestion-list-item.relative.rounded-2xl bg #000000 @ 0.05 | 1 up div.group/home-suggestion-list-item.relative.rounded-2xl bg #000000 @ 0.05 |
| Painted layers | - | = | button.cursor-interaction.outline-none.flex 768.0x52.0 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |

Crops: `suggestion-row-default.png`, `suggestion-row-hover.png`, `suggestion-row-focus-visible.png`, `suggestion-row-pressed.png`, `suggestion-row-light.png`, `suggestion-row-light-hover.png`, `suggestion-row-light-focus-visible.png`, `suggestion-row-light-pressed.png`.

#### promo-card

Card (Plus nudge). 768x74 card pinned under the suggestions: icon, title and line, a filled Get Plus button and a dismiss button.

Page copy: `home-dark`. Finder: `() => Q('aside[class*="surface-"]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 768 x 74 |
| Padding | 16px |
| Gap | 12px |
| Border | none |
| Radius | 24px |
| Background | #1b1b1b |
| Box shadow | #000000 @ 0.05 0px 4px 16px 0px |
| Outline | 1px solid #ffffff @ 0.05 offset -0.5px |
| Font | -apple-system 14px/20px 400 |
| Letter spacing | -0.15px |
| Colour | #ededed |
| Text node | div.title-TGNnMU: -apple-system 14px/20px 510, #ededed, ls -0.15px |
| Transition | none |
| Icon | 20 x 20, colour #afafaf, fill #000000 |
| Painted layers | aside.surface-NbxhOL 768.0x74.0 bg #1b1b1b r 24px shadow #000000 @ 0.05 0px 4px 16px 0px outline 1px solid #ffffff @ 0.05 offset -0.5px; button.no-drag.cursor-interaction.items-center 86.0x36.0 bg #ededed r 9999px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 768 x 74 |
| Padding | 16px |
| Gap | 12px |
| Border | none |
| Radius | 24px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.05 0px 4px 16px 0px |
| Outline | 1px solid #0d0d0d @ 0.05 offset -0.5px |
| Font | -apple-system 14px/20px 400 |
| Letter spacing | -0.15px |
| Colour | #0d0d0d |
| Text node | div.title-TGNnMU: -apple-system 14px/20px 510, #0d0d0d, ls -0.15px |
| Transition | none |
| Icon | 20 x 20, colour #8f8f8f, fill #000000 |
| Painted layers | aside.surface-NbxhOL 768.0x74.0 bg #ffffff r 24px shadow #000000 @ 0.05 0px 4px 16px 0px outline 1px solid #0d0d0d @ 0.05 offset -0.5px; button.no-drag.cursor-interaction.items-center 86.0x36.0 bg #0d0d0d r 9999px |
| How | at rest |

Crops: `promo-card-default.png`, `promo-card-light.png`.

#### promo-button

Primary button (Get Plus).

Page copy: `home-dark`. Finder: `() => B('Get Plus')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.98 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ededed | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system 14px/20px 510 | = | = | = |
| Letter spacing | -0.18px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 86.0x36.0 bg #ededed r 9999px | button.no-drag.cursor-interaction.items-center 86.0x36.0 bg #ededed r 9999px opacity 0.8 | button.no-drag.cursor-interaction.items-center 86.0x36.0 bg #ededed r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 86.0x36.0 bg #ededed r 9999px opacity 0.8 |
| Ancestor paint | 3 up aside.surface-NbxhOL bg #1b1b1b shadow #000000 @ 0.05 0px 4px 16px 0px outline 1px solid #ffffff @ 0.05 | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |
| Opacity | - | 0.8 | = | 0.8 |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 85.98 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #0d0d0d | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system 14px/20px 510 | = | = | = |
| Letter spacing | -0.18px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 86.0x36.0 bg #0d0d0d r 9999px | button.no-drag.cursor-interaction.items-center 86.0x36.0 bg #0d0d0d r 9999px opacity 0.8 | button.no-drag.cursor-interaction.items-center 86.0x36.0 bg #0d0d0d r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 86.0x36.0 bg #0d0d0d r 9999px opacity 0.8 |
| Ancestor paint | 3 up aside.surface-NbxhOL bg #ffffff shadow #000000 @ 0.05 0px 4px 16px 0px outline 1px solid #0d0d0d @ 0.05 | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |
| Opacity | - | 0.8 | = | 0.8 |

Crops: `promo-button-default.png`, `promo-button-hover.png`, `promo-button-focus-visible.png`, `promo-button-pressed.png`, `promo-button-light.png`, `promo-button-light-hover.png`, `promo-button-light-focus-visible.png`, `promo-button-light-pressed.png`.

#### promo-dismiss

Dismiss button.

Page copy: `home-dark`. Finder: `() => Q('button[class*="dismissButton"]')`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 20 x 20 | = | = |
| Padding | 0px | = | = |
| Gap | 4px | = | = |
| Border | none | = | = |
| Radius | 9999px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | -apple-system 14px/20px 400 | = | = |
| Letter spacing | -0.15px | = | = |
| Colour | #afafaf | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 20 x 20, colour #afafaf, fill #000000 | = | = |
| Ancestor paint | 2 up aside.surface-NbxhOL bg #1b1b1b shadow #000000 @ 0.05 0px 4px 16px 0px outline 1px solid #ffffff @ 0.05 | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |
| Opacity | - | 0.8 | = |
| Painted layers | - | = | button.no-drag.cursor-interaction.items-center 20.0x20.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 20 x 20 | = | = |
| Padding | 0px | = | = |
| Gap | 4px | = | = |
| Border | none | = | = |
| Radius | 9999px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | -apple-system 14px/20px 400 | = | = |
| Letter spacing | -0.15px | = | = |
| Colour | #8f8f8f | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 20 x 20, colour #8f8f8f, fill #000000 | = | = |
| Ancestor paint | 2 up aside.surface-NbxhOL bg #ffffff shadow #000000 @ 0.05 0px 4px 16px 0px outline 1px solid #0d0d0d @ 0.05 | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |
| Opacity | - | 0.8 | = |
| Painted layers | - | = | button.no-drag.cursor-interaction.items-center 20.0x20.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |

Crops: `promo-dismiss-default.png`, `promo-dismiss-hover.png`, `promo-dismiss-focus-visible.png`, `promo-dismiss-light.png`, `promo-dismiss-light-hover.png`, `promo-dismiss-light-focus-visible.png`.

### Composer

#### composer

Text area (composer). A pill on the home page, 768 wide: + button, the ProseMirror field, Think, dictate, voice.

Page copy: `home-dark`, `home-dark-composer-typed`, `thread-dark-code`. Finder: `() => P(Q('.ProseMirror').parentElement)`.

Dark theme.

| Property | default | focus-visible | typed | thread |
|---|---|---|---|---|
| Size (w x h) | 768 x 52 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 26px | = | = | = |
| Background | #1b1b1b | = | = | = |
| Box shadow | #ffffff @ 0.2 0px 0px 1px 0px inset | = | = | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ededed | = | = | = |
| Text node | span: -apple-system-body 16px/26px 400, #afafaf | = | p: -apple-system-body 16px/26px 400, #ededed | = |
| Transition | none | = | = | = |
| Icon | 20 x 20, colour #ededed, fill #000000 | = | = | = |
| Placeholder | "Ask ChatGPT" #afafaf, opacity 1, 16px | = | - | = |
| Painted layers | div.ComposerLayoutBody-uBBf1A 768.0x52.0 bg #1b1b1b r 26px shadow #ffffff @ 0.2 0px 0px 1px 0px inset; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.cursor-interaction.size-token-button-composer.flex 36.0x36.0 bg #2c67c5 r 9999px | = | = | div.ComposerLayoutRoot-XCKS7O 768.0x52.0 bg #1b1b1b r 26px shadow #ffffff @ 0.2 0px 0px 1px 0px inset; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.cursor-interaction.size-token-button-composer.flex 36.0x36.0 bg #2c67c5 r 9999px |
| Tokens | --composer-editor-line-height calc(16px * 1.625); --spacing .25rem; --spacing-token-button-composer calc(.25rem * 9); --text-sm 14px | = | = | = |
| How | at rest | keyboard: focus(), Shift+Tab, Tab (on the field inside) | at rest, captured typed | at rest, captured thread |

Light theme.

| Property | light | light-focus-visible | light-typed | light-thread |
|---|---|---|---|---|
| Size (w x h) | 768 x 52 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 26px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #ffffff @ 0.2 0px 0px 1px 0px inset | = | = | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Text node | span: -apple-system-body 16px/26px 400, #8f8f8f | = | p: -apple-system-body 16px/26px 400, #0d0d0d | = |
| Transition | none | = | = | = |
| Icon | 20 x 20, colour #0d0d0d, fill #000000 | = | = | = |
| Placeholder | "Ask ChatGPT" #8f8f8f, opacity 1, 16px | = | - | = |
| Painted layers | div.ComposerLayoutBody-uBBf1A 768.0x52.0 bg #ffffff r 26px shadow #ffffff @ 0.2 0px 0px 1px 0px inset; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.cursor-interaction.size-token-button-composer.flex 36.0x36.0 bg #3a83f7 r 9999px | = | = | div.ComposerLayoutRoot-XCKS7O 768.0x52.0 bg #ffffff r 26px shadow #ffffff @ 0.2 0px 0px 1px 0px inset; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.cursor-interaction.size-token-button-composer.flex 36.0x36.0 bg #3a83f7 r 9999px |
| Tokens | --composer-editor-line-height calc(16px * 1.625); --spacing .25rem; --spacing-token-button-composer calc(.25rem * 9); --text-sm 14px | = | = | = |
| How | at rest | keyboard: focus(), Shift+Tab, Tab (on the field inside) | at rest, captured typed | at rest, captured thread |

Other finders: typed: `() => P(Q('.ProseMirror').parentElement)`; light-typed: `() => P(Q('.ProseMirror').parentElement)`; thread: `() => P(Q('.ProseMirror').parentElement)`; light-thread: `() => P(Q('.ProseMirror').parentElement)`.

Crops: `composer-default.png`, `composer-focus-visible.png`, `composer-typed.png`, `composer-thread.png`, `composer-light.png`, `composer-light-focus-visible.png`, `composer-light-typed.png`, `composer-light-thread.png`.

#### composer-placeholder

Composer placeholder.

Page copy: `home-dark`. Finder: `() => Q('.ProseMirror p')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 528.03 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/26px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Transition | none |
| Placeholder | "Ask ChatGPT" #afafaf, opacity 1, 16px |
| ::before | 528.031px x 26px, absolute, bg #000000 @ 0, radius 0px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 528.03 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/26px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Transition | none |
| Placeholder | "Ask ChatGPT" #8f8f8f, opacity 1, 16px |
| ::before | 528.031px x 26px, absolute, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `composer-placeholder-default.png`, `composer-placeholder-light.png`.

#### composer-plus

Icon button (composer +).

Page copy: `home-dark`. Finder: `() => Q('button[aria-label="Add files and more"]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #ffffff @ 0.1 | = | #ffffff @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/26px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #afafaf | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ededed, fill #000000 | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #ffffff @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #ffffff @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| Tokens | --spacing .25rem; --text-sm 14px | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #000000 @ 0.05 | = | #000000 @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/26px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #8f8f8f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #0d0d0d, fill #000000 | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| Tokens | --spacing .25rem; --text-sm 14px | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `composer-plus-default.png`, `composer-plus-hover.png`, `composer-plus-focus-visible.png`, `composer-plus-pressed.png`, `composer-plus-light.png`, `composer-plus-light-hover.png`, `composer-plus-light-focus-visible.png`, `composer-plus-light-pressed.png`.

#### think-chip

Think chip.

Page copy: `home-dark`. Finder: `() => C(T('Think'), 'button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 91.97 x 36 | = | = | = |
| Padding | 0px 14px 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #ffffff @ 0.1 | = | #ffffff @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/26px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #afafaf | = | = | = |
| Text node | span: -apple-system-body 16px/26px 400, #afafaf | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #afafaf, fill #000000 | = | = | = |
| Tokens | --spacing-token-button-composer calc(.25rem * 9) | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |
| Painted layers | - | button.no-drag.cursor-interaction.items-center 92.0x36.0 bg #ffffff @ 0.1 r 9999px | button.no-drag.cursor-interaction.items-center 92.0x36.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 92.0x36.0 bg #ffffff @ 0.1 r 9999px |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 91.97 x 36 | = | = | = |
| Padding | 0px 14px 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #000000 @ 0.05 | = | #000000 @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/26px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #8f8f8f | = | = | = |
| Text node | span: -apple-system-body 16px/26px 400, #8f8f8f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #8f8f8f, fill #000000 | = | = | = |
| Tokens | --spacing-token-button-composer calc(.25rem * 9) | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |
| Painted layers | - | button.no-drag.cursor-interaction.items-center 92.0x36.0 bg #000000 @ 0.05 r 9999px | button.no-drag.cursor-interaction.items-center 92.0x36.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 92.0x36.0 bg #000000 @ 0.05 r 9999px |

Crops: `think-chip-default.png`, `think-chip-hover.png`, `think-chip-focus-visible.png`, `think-chip-pressed.png`, `think-chip-light.png`, `think-chip-light-hover.png`, `think-chip-light-focus-visible.png`, `think-chip-light-pressed.png`.

#### dictate-button

Icon button (Dictate).

Page copy: `home-dark`. Finder: `() => Q('button[aria-label="Dictate"]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #ffffff @ 0.1 | = | #ffffff @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/26px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #afafaf | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ededed, fill #000000 | = | = | = |
| ::after | 40px x 36px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #ffffff @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #ffffff @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| Tokens | --spacing .25rem; --text-sm 14px | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #000000 @ 0.05 | = | #000000 @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/26px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #8f8f8f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #0d0d0d, fill #000000 | = | = | = |
| ::after | 40px x 36px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| Tokens | --spacing .25rem; --text-sm 14px | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `dictate-button-default.png`, `dictate-button-hover.png`, `dictate-button-focus-visible.png`, `dictate-button-pressed.png`, `dictate-button-light.png`, `dictate-button-light-hover.png`, `dictate-button-light-focus-visible.png`, `dictate-button-light-pressed.png`.

#### voice-button

Accent icon button (Start Voice). A 36px circle in `--color-background-composer-primary`, the accent.

Page copy: `home-dark`. Finder: `() => Q('button[aria-label="Start Voice"]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 2px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #2c67c5 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #2c67c5 offset 0px | = |
| Font | -apple-system-body 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ededed | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff, fill #000000 | = | = | = |
| ::after | 40px x 36px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.cursor-interaction.size-token-button-composer.flex 36.0x36.0 bg #2c67c5 r 9999px | = | button.cursor-interaction.size-token-button-composer.flex 36.0x36.0 bg #2c67c5 r 9999px outline 2px solid #2c67c5 offset 0px | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 2px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #3a83f7 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3a83f7 offset 0px | = |
| Font | -apple-system-body 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff, fill #000000 | = | = | = |
| ::after | 40px x 36px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.cursor-interaction.size-token-button-composer.flex 36.0x36.0 bg #3a83f7 r 9999px | = | button.cursor-interaction.size-token-button-composer.flex 36.0x36.0 bg #3a83f7 r 9999px outline 2px solid #3a83f7 offset 0px | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `voice-button-default.png`, `voice-button-hover.png`, `voice-button-focus-visible.png`, `voice-button-pressed.png`, `voice-button-light.png`, `voice-button-light-hover.png`, `voice-button-light-focus-visible.png`, `voice-button-light-pressed.png`.

#### send-button

Accent icon button (Send, typed).

Page copy: `home-dark-composer-typed`. Finder: `() => Q('button[aria-label="Send"]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 2px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #2c67c5 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #2c67c5 offset 0px | = |
| Font | -apple-system-body 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ededed | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = |
| Painted layers | button.cursor-interaction.size-token-button-composer.flex 36.0x36.0 bg #2c67c5 r 9999px | = | button.cursor-interaction.size-token-button-composer.flex 36.0x36.0 bg #2c67c5 r 9999px outline 2px solid #2c67c5 offset 0px | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 2px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #3a83f7 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3a83f7 offset 0px | = |
| Font | -apple-system-body 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = |
| Painted layers | button.cursor-interaction.size-token-button-composer.flex 36.0x36.0 bg #3a83f7 r 9999px | = | button.cursor-interaction.size-token-button-composer.flex 36.0x36.0 bg #3a83f7 r 9999px outline 2px solid #3a83f7 offset 0px | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `send-button-default.png`, `send-button-hover.png`, `send-button-focus-visible.png`, `send-button-pressed.png`, `send-button-light.png`, `send-button-light-hover.png`, `send-button-light-focus-visible.png`, `send-button-light-pressed.png`.

#### tooltip

Tooltip (Dictate). Opened by keyboard focus on the Dictate button: `--color-background-tooltip` fill, rounded, 14px text.

Page copy: `home-dark-tooltip`. Finder: `() => Q('[role=tooltip]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 73.66 x 30 |
| Padding | 5px 12px |
| Border | 1px solid #ededed @ 0.05 |
| Radius | 16px |
| Background | #303030 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0f172a @ 0.2 0px 8px 18px 0px |
| Outline | none |
| Font | -apple-system-body 14px/18px 600 |
| Letter spacing | -0.15px |
| Colour | #ededed |
| Text node | div.min-w-0: -apple-system-body 14px/18px 600, #ededed, ls -0.15px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 1167.5, 428) |
| Painted layers | div.w-fit.text-sm.whitespace-normal 73.7x30.0 bg #303030 border T:1px solid #ededed @ 0.05 / R:1px solid #ededed @ 0.05 / B:1px solid #ededed @ 0.05 / L:1px solid #ededed @ 0.05 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0f172a @ 0.2 0px 8px 18px 0px |
| Tokens | --color-background-tooltip #303030; --radix-tooltip-content-available-height 464px; --radix-tooltip-content-available-width 1424px; --radix-tooltip-trigger-width 36px; --shadow-tooltip 0 8px 18px #0f172a33; --tracking-tooltip -.15px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 73.66 x 30 |
| Padding | 5px 12px |
| Border | 1px solid #ffffff @ 0.05 |
| Radius | 16px |
| Background | #0d0d0d |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0f172a @ 0.2 0px 8px 18px 0px |
| Outline | none |
| Font | -apple-system-body 14px/18px 600 |
| Letter spacing | -0.15px |
| Colour | #ffffff |
| Text node | div.min-w-0: -apple-system-body 14px/18px 600, #ffffff, ls -0.15px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 1167.5, 428) |
| Painted layers | div.w-fit.text-sm.whitespace-normal 73.7x30.0 bg #0d0d0d border T:1px solid #ffffff @ 0.05 / R:1px solid #ffffff @ 0.05 / B:1px solid #ffffff @ 0.05 / L:1px solid #ffffff @ 0.05 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0f172a @ 0.2 0px 8px 18px 0px |
| Tokens | --color-background-tooltip #0d0d0d; --radix-tooltip-content-available-height 464px; --radix-tooltip-content-available-width 1424px; --radix-tooltip-trigger-width 36px; --shadow-tooltip 0 8px 18px #0f172a33; --tracking-tooltip -.15px |
| How | at rest |

Crops: `tooltip-default.png`, `tooltip-light.png`.

### Thread

#### user-bubble

User message bubble. `--color-background-user-message` / `--color-text-user-message`; right-aligned, rounded.

Page copy: `thread-dark-user-turn`. Finder: `() => Q('[data-user-message-bubble]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 537.59 x 462 |
| Padding | 10px 16px |
| Border | none |
| Radius | 22px |
| Background | #173e76 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f6fafe |
| Text node | span: -apple-system-body 16px/26px 400, #f6fafe |
| Transition | none |
| Painted layers | div.bg-user-message.text-user-message.min-w-0 537.6x462.0 bg #173e76 r 22px |
| Tokens | --thread-content-margin calc(.25rem * 4); --user-chat-width 70% |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 537.59 x 462 |
| Padding | 10px 16px |
| Border | none |
| Radius | 22px |
| Background | #e8f3fe |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0c274a |
| Text node | span: -apple-system-body 16px/26px 400, #0c274a |
| Transition | none |
| Painted layers | div.bg-user-message.text-user-message.min-w-0 537.6x462.0 bg #e8f3fe r 22px |
| Tokens | --thread-content-margin calc(.25rem * 4); --user-chat-width 70% |
| How | at rest |

Crops: `user-bubble-default.png`, `user-bubble-light.png`.

#### markdown

Assistant markdown body.

Page copy: `thread-dark-table`. Finder: `() => Q('[class*="MarkdownRoot"]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 768 x 2695 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/26px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | span: -apple-system-body 16px/26px 400, #ededed |
| Transition | none |
| Icon | 12 x 12, colour #cdcdcd, fill #000000 |
| Painted layers | th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 128.0x33.0 border B:1px solid #ffffff @ 0.2; th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 448.0x33.0 border B:1px solid #ffffff @ 0.2; th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 128.0x33.0 border B:1px solid #ffffff @ 0.2; th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 448.0x33.0 border B:1px solid #ffffff @ 0.2; th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 256.0x33.0 border B:1px solid #ffffff @ 0.2; td.TableCell-WcsygL.SingleChildTableCell-Sv7jTC 128.0x125.0 border B:1px solid #ffffff @ 0.05 |
| Tokens | --markdown-link-color currentColor |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 768 x 2695 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/26px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span: -apple-system-body 16px/26px 400, #0d0d0d |
| Transition | none |
| Icon | 12 x 12, colour #5d5d5d, fill #000000 |
| Painted layers | th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 128.0x33.0 border B:1px solid #000000 @ 0.15; th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 448.0x33.0 border B:1px solid #000000 @ 0.15; th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 128.0x33.0 border B:1px solid #000000 @ 0.15; th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 448.0x33.0 border B:1px solid #000000 @ 0.15; th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 256.0x33.0 border B:1px solid #000000 @ 0.15; td.TableCell-WcsygL.SingleChildTableCell-Sv7jTC 128.0x125.0 border B:1px solid #000000 @ 0.05 |
| Tokens | --markdown-link-color currentColor |
| How | at rest |

Crops: `markdown-default.png`, `markdown-light.png`.

#### md-paragraph

Markdown paragraph.

Page copy: `thread-dark-table`. Finder: `() => Q('[class*="MarkdownRoot"] p')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 768 x 78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/26px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | span: -apple-system-body 16px/26px 400, #ededed |
| Transition | none |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 768 x 78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/26px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span: -apple-system-body 16px/26px 400, #0d0d0d |
| Transition | none |
| How | at rest |

Crops: `md-paragraph-default.png`, `md-paragraph-light.png`.

#### md-heading

Markdown heading.

Page copy: `thread-dark-table`. Finder: `() => Q('[class*="MarkdownRoot"] h1, [class*="MarkdownRoot"] h2, [class*="MarkdownRoot"] h3')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 768 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 18px/28px 600 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | span: -apple-system-body 18px/28px 600, #ededed |
| Transition | none |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 768 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 18px/28px 600 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span: -apple-system-body 18px/28px 600, #0d0d0d |
| Transition | none |
| How | at rest |

Crops: `md-heading-default.png`, `md-heading-light.png`.

#### md-strong

Markdown strong.

Page copy: `thread-dark-table`. Finder: `() => Q('[class*="MarkdownRoot"] strong')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 357.2 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/26px 600 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | span: -apple-system-body 16px/26px 600, #ededed |
| Transition | none |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 357.2 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/26px 600 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span: -apple-system-body 16px/26px 600, #0d0d0d |
| Transition | none |
| How | at rest |

Crops: `md-strong-default.png`, `md-strong-light.png`.

#### md-inline-code

Inline code.

Page copy: `thread-dark-code`. Finder: `() => [...document.querySelectorAll('[class*="MarkdownRoot"] code')].find((c) => !c.closest('pre') && c.getBoundingClientRect().width > 1 && c.getBoundingClientRect().top > 0)`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 17.28 x 19.47 |
| Padding | 0.744px 4.1664px |
| Border | none |
| Radius | 3.72px |
| Background | #212121 @ 0.82 |
| Box shadow | none |
| Outline | none |
| Font | ui-monospace 14.88px/26px 500 |
| Letter spacing | normal |
| Colour | #ededed |
| Transition | none |
| Painted layers | code.Code-kbs71c 17.3x19.5 bg #212121 @ 0.82 r 3.72px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 17.28 x 19.47 |
| Padding | 0.744px 4.1664px |
| Border | none |
| Radius | 3.72px |
| Background | #f3f3f3 @ 0.82 |
| Box shadow | none |
| Outline | none |
| Font | ui-monospace 14.88px/26px 500 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Transition | none |
| Painted layers | code.Code-kbs71c 17.3x19.5 bg #f3f3f3 @ 0.82 r 3.72px |
| How | at rest |

Crops: `md-inline-code-default.png`, `md-inline-code-light.png`.

#### md-link

Link (citation in an answer).

Page copy: `thread-dark-table`. Finder: `() => Q('[class*="MarkdownRoot"] a[href]')`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 129.94 x 18 | = | = |
| Padding | 0px 8px 0px 4px | = | = |
| Border | none | = | = |
| Radius | 12px | = | = |
| Background | #303030 | #ffffff @ 0.1 | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #99c8ff offset 1px |
| Font | -apple-system-body 9px/9px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #cdcdcd | #ededed | = |
| Text node | span.min-w-0.grow.truncate: -apple-system-body 9px/9px 500, #cdcdcd | span.min-w-0.grow.truncate: -apple-system-body 9px/9px 500, #ededed | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 12 x 12, colour #cdcdcd, fill #000000 | 12 x 12, colour #ededed, fill #000000 | = |
| Painted layers | a.no-underline!.group.cursor-interaction 129.9x18.0 bg #303030 r 12px | a.no-underline!.group.cursor-interaction 129.9x18.0 bg #ffffff @ 0.1 r 12px | a.no-underline!.group.cursor-interaction 129.9x18.0 bg #303030 r 12px outline 1px auto #99c8ff offset 1px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 129.94 x 18 | = | = |
| Padding | 0px 8px 0px 4px | = | = |
| Border | none | = | = |
| Radius | 12px | = | = |
| Background | #f3f3f3 | #000000 @ 0.05 | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px |
| Font | -apple-system-body 9px/9px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #5d5d5d | #0d0d0d | = |
| Text node | span.min-w-0.grow.truncate: -apple-system-body 9px/9px 500, #5d5d5d | span.min-w-0.grow.truncate: -apple-system-body 9px/9px 500, #0d0d0d | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 12 x 12, colour #5d5d5d, fill #000000 | 12 x 12, colour #0d0d0d, fill #000000 | = |
| Painted layers | a.no-underline!.group.cursor-interaction 129.9x18.0 bg #f3f3f3 r 12px | a.no-underline!.group.cursor-interaction 129.9x18.0 bg #000000 @ 0.05 r 12px | a.no-underline!.group.cursor-interaction 129.9x18.0 bg #f3f3f3 r 12px outline 1px auto #005fcc offset 1px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |

Crops: `md-link-default.png`, `md-link-hover.png`, `md-link-focus-visible.png`, `md-link-light.png`, `md-link-light-hover.png`, `md-link-light-focus-visible.png`.

#### code-block

Code block.

Page copy: `thread-dark-code`. Finder: `() => Q('[class*="CodeSurface"]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 768 x 262 |
| Padding | 0px |
| Border | 1px solid #ffffff @ 0.05 |
| Radius | 24px |
| Background | #303030 |
| Background image | linear-gradient(#ffffff @ 0.1, #ffffff @ 0.1) |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/26px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | div.min-w-0.flex-1.truncate: -apple-system-body 14px/20px 500, #ededed |
| Transition | none |
| Icon | 20 x 20, colour #ededed, fill #000000 |
| Painted layers | div.relative.Root-iW7ipz.w-full 768.0x262.0 bg #303030 image linear-gradient(#ffffff @ 0.1, #ffffff @ 0.1) border T:1px solid #ffffff @ 0.05 / R:1px solid #ffffff @ 0.05 / B:1px solid #ffffff @ 0.05 / L:1px solid #ffffff @ 0.05 r 24px; div.flex.items-center.font-sans 766.0x48.0 bg #303030 image linear-gradient(#ffffff @ 0.1, #ffffff @ 0.1); button.group/scroll-to-bottom.cursor-interaction.absolute 32.0x32.0 bg #303030 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px opacity 0 |
| Tokens | --radius-3xl-base 1.5rem |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 768 x 262 |
| Padding | 0px |
| Border | 1px solid #000000 @ 0.05 |
| Radius | 24px |
| Background | #f3f3f3 |
| Background image | linear-gradient(#000000 @ 0.05, #000000 @ 0.05) |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/26px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | div.min-w-0.flex-1.truncate: -apple-system-body 14px/20px 500, #0d0d0d |
| Transition | none |
| Icon | 20 x 20, colour #0d0d0d, fill #000000 |
| Painted layers | div.relative.Root-iW7ipz.w-full 768.0x262.0 bg #f3f3f3 image linear-gradient(#000000 @ 0.05, #000000 @ 0.05) border T:1px solid #000000 @ 0.05 / R:1px solid #000000 @ 0.05 / B:1px solid #000000 @ 0.05 / L:1px solid #000000 @ 0.05 r 24px; div.flex.items-center.font-sans 766.0x48.0 bg #f3f3f3 image linear-gradient(#000000 @ 0.05, #000000 @ 0.05); button.group/scroll-to-bottom.cursor-interaction.absolute 32.0x32.0 bg #f3f3f3 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px opacity 0 |
| Tokens | --radius-3xl-base 1.5rem |
| How | at rest |

Crops: `code-block-default.png`, `code-block-light.png`.

#### code-text

Code text (inside a code block). The `code` element itself, not the language label in the block header; `typography.code` is read from it.

Page copy: `thread-dark-code`. Finder: `() => Q('[class*="CodeSurface"] pre code')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 462.45 x 194 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-monospace 12px/20px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | span.text-codex-syntax-keyword: ui-monospace 12px/20px 400, #f8a6c8 |
| Transition | none |
| Cursor | text |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 462.45 x 194 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-monospace 12px/20px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span.text-codex-syntax-keyword: ui-monospace 12px/20px 400, #ab4f7a |
| Transition | none |
| Cursor | text |
| How | at rest |

Crops: `code-text-default.png`, `code-text-light.png`.

#### code-block-button

Code block icon button.

Page copy: `thread-dark-code`. Finder: `() => Q('[class*="CodeSurface"] button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #ffffff @ 0.1 | = | #ffffff @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ededed | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ededed, fill #000000 | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |
| Painted layers | - | button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #ffffff @ 0.1 r 9999px | button.no-drag.cursor-interaction.items-center 36.0x36.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #ffffff @ 0.1 r 9999px |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #000000 @ 0.05 | = | #000000 @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #0d0d0d, fill #000000 | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |
| Painted layers | - | button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #000000 @ 0.05 r 9999px | button.no-drag.cursor-interaction.items-center 36.0x36.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #000000 @ 0.05 r 9999px |

Crops: `code-block-button-default.png`, `code-block-button-hover.png`, `code-block-button-focus-visible.png`, `code-block-button-pressed.png`, `code-block-button-light.png`, `code-block-button-light-hover.png`, `code-block-button-light-focus-visible.png`, `code-block-button-light-pressed.png`.

#### md-table

Table.

Page copy: `thread-dark-table`. Finder: `() => Q('table')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 1408 x 447 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 14px/26px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | span: -apple-system-body 14px/16px 600, #ededed |
| Transition | none |
| Icon | 12 x 12, colour #cdcdcd, fill #000000 |
| Painted layers | th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 128.0x33.0 border B:1px solid #ffffff @ 0.2; th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 448.0x33.0 border B:1px solid #ffffff @ 0.2; th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 128.0x33.0 border B:1px solid #ffffff @ 0.2; th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 448.0x33.0 border B:1px solid #ffffff @ 0.2; th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 256.0x33.0 border B:1px solid #ffffff @ 0.2; td.TableCell-WcsygL.SingleChildTableCell-Sv7jTC 128.0x125.0 border B:1px solid #ffffff @ 0.05 |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 1408 x 447 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 14px/26px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span: -apple-system-body 14px/16px 600, #0d0d0d |
| Transition | none |
| Icon | 12 x 12, colour #5d5d5d, fill #000000 |
| Painted layers | th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 128.0x33.0 border B:1px solid #000000 @ 0.15; th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 448.0x33.0 border B:1px solid #000000 @ 0.15; th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 128.0x33.0 border B:1px solid #000000 @ 0.15; th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 448.0x33.0 border B:1px solid #000000 @ 0.15; th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 256.0x33.0 border B:1px solid #000000 @ 0.15; td.TableCell-WcsygL.SingleChildTableCell-Sv7jTC 128.0x125.0 border B:1px solid #000000 @ 0.05 |
| How | at rest |

Crops: `md-table-default.png`, `md-table-light.png`.

#### md-th

Table header cell.

Page copy: `thread-dark-table`. Finder: `() => Q('table th')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 128 x 33 |
| Padding | 8px 24px 8px 0px |
| Border | T: none; R: none; B: 1px solid #ffffff @ 0.2; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 14px/16px 600 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | span: -apple-system-body 14px/16px 600, #ededed |
| Transition | none |
| Painted layers | th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 128.0x33.0 border B:1px solid #ffffff @ 0.2 |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 128 x 33 |
| Padding | 8px 24px 8px 0px |
| Border | T: none; R: none; B: 1px solid #000000 @ 0.15; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 14px/16px 600 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span: -apple-system-body 14px/16px 600, #0d0d0d |
| Transition | none |
| Painted layers | th.TableHeaderCell-esYSpn.SingleChildTableCell-Sv7jTC 128.0x33.0 border B:1px solid #000000 @ 0.15 |
| How | at rest |

Crops: `md-th-default.png`, `md-th-light.png`.

#### md-td

Table cell.

Page copy: `thread-dark-table`. Finder: `() => Q('table td')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 128 x 125 |
| Padding | 10px 24px 10px 0px |
| Border | T: none; R: none; B: 1px solid #ffffff @ 0.05; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 14px/26px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | span: -apple-system-body 14px/26px 600, #ededed |
| Transition | none |
| Painted layers | td.TableCell-WcsygL.SingleChildTableCell-Sv7jTC 128.0x125.0 border B:1px solid #ffffff @ 0.05 |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 128 x 125 |
| Padding | 10px 24px 10px 0px |
| Border | T: none; R: none; B: 1px solid #000000 @ 0.05; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 14px/26px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span: -apple-system-body 14px/26px 600, #0d0d0d |
| Transition | none |
| Painted layers | td.TableCell-WcsygL.SingleChildTableCell-Sv7jTC 128.0x125.0 border B:1px solid #000000 @ 0.05 |
| How | at rest |

Crops: `md-td-default.png`, `md-td-light.png`.

#### turn-action

Turn action button (Copy).

Page copy: `thread-dark-code`. Finder: `() => { const mds = [...document.querySelectorAll('[class*="MarkdownRoot"]')]; const md = mds[mds.length - 1]; let n = md; for (let i = 0; i < 10 && n; i++) { n = n.parentElement; const bs = [...n.querySelectorAll('button')].filter((b) => !md.contains(b) && Math.round(b.getBoundingClientRect().width) === 32 && !/Scroll/.test(b.getAttribute('aria-label') // '')); if (bs.length >= 3) return bs[0]; } return null; }`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #ffffff @ 0.1 | = | #ffffff @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #afafaf | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #afafaf | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.no-drag.cursor-interaction.items-center 32.0x32.0 bg #ffffff @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.no-drag.cursor-interaction.items-center 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 32.0x32.0 bg #ffffff @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #000000 @ 0.05 | = | #000000 @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #8f8f8f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #8f8f8f | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.no-drag.cursor-interaction.items-center 32.0x32.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.no-drag.cursor-interaction.items-center 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 32.0x32.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `turn-action-default.png`, `turn-action-hover.png`, `turn-action-focus-visible.png`, `turn-action-pressed.png`, `turn-action-light.png`, `turn-action-light-hover.png`, `turn-action-light-focus-visible.png`, `turn-action-light-pressed.png`.

#### scroll-button

Scroll to bottom button.

Page copy: `thread-dark-user-turn`. Finder: `() => Q('button[aria-label="Scroll to bottom"]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #ffffff @ 0.15 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #99c8ff offset 0px | = |
| Font | -apple-system-body 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #cdcdcd | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ededed, fill #000000 | = | = | = |
| Painted layers | button.group/scroll-to-bottom.cursor-interaction.absolute 32.0x32.0 bg #000000 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px | = | button.group/scroll-to-bottom.cursor-interaction.absolute 32.0x32.0 bg #000000 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px outline 1px auto #99c8ff offset 0px | = |
| Tokens | --spacing .25rem; --thread-composer-overlay-height 0px | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #000000 @ 0.1 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #fcfcfc | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | -apple-system-body 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #5d5d5d | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #0d0d0d, fill #000000 | = | = | = |
| Painted layers | button.group/scroll-to-bottom.cursor-interaction.absolute 32.0x32.0 bg #fcfcfc border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px | = | button.group/scroll-to-bottom.cursor-interaction.absolute 32.0x32.0 bg #fcfcfc border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px outline 1px auto #005fcc offset 0px | = |
| Tokens | --spacing .25rem; --thread-composer-overlay-height 0px | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `scroll-button-default.png`, `scroll-button-hover.png`, `scroll-button-focus-visible.png`, `scroll-button-pressed.png`, `scroll-button-light.png`, `scroll-button-light-hover.png`, `scroll-button-light-focus-visible.png`, `scroll-button-light-pressed.png`.

#### thread-disclaimer

Thread disclaimer.

Page copy: `thread-dark-code`. Finder: `() => TS('ChatGPT can make mistakes')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 1067 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 12px/16px 400 |
| Letter spacing | normal |
| Colour | #afafaf |
| Transition | none |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 1067 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 12px/16px 400 |
| Letter spacing | normal |
| Colour | #8f8f8f |
| Transition | none |
| How | at rest |

Crops: `thread-disclaimer-default.png`, `thread-disclaimer-light.png`.

### Feedback

#### streaming-dot

Loading indicator (streaming dot). Where the answer will appear while it is being generated: a 12px dot in the composer colour that pulses (the copy shows one frame).

Page copy: `thread-dark-streaming`. Finder: `() => Q('.pulsing-dot')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 12 x 12 |
| Padding | 0px |
| Border | none |
| Radius | 9999px |
| Background | #2c67c5 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Transition | none |
| Painted layers | span.inline-block.size-3.pulsing-dot 12.0x12.0 bg #2c67c5 r 9999px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 12 x 12 |
| Padding | 0px |
| Border | none |
| Radius | 9999px |
| Background | #3a83f7 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Transition | none |
| Painted layers | span.inline-block.size-3.pulsing-dot 12.0x12.0 bg #3a83f7 r 9999px |
| How | at rest |

Crops: `streaming-dot-default.png`, `streaming-dot-light.png`.

#### stop-button

Icon button (Stop, while streaming). The composer's send button becomes Stop for as long as the answer streams.

Page copy: `thread-dark-streaming`. Finder: `() => Q('[data-testid="stop-button"], button[aria-label*="Stop"]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 2px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #2c67c5 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #2c67c5 offset 0px | = |
| Font | -apple-system-body 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ededed | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = |
| Painted layers | button.cursor-interaction.size-token-button-composer.flex 36.0x36.0 bg #2c67c5 r 9999px | = | button.cursor-interaction.size-token-button-composer.flex 36.0x36.0 bg #2c67c5 r 9999px outline 2px solid #2c67c5 offset 0px | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 2px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #3a83f7 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3a83f7 offset 0px | = |
| Font | -apple-system-body 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = |
| Painted layers | button.cursor-interaction.size-token-button-composer.flex 36.0x36.0 bg #3a83f7 r 9999px | = | button.cursor-interaction.size-token-button-composer.flex 36.0x36.0 bg #3a83f7 r 9999px outline 2px solid #3a83f7 offset 0px | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `stop-button-default.png`, `stop-button-hover.png`, `stop-button-focus-visible.png`, `stop-button-pressed.png`, `stop-button-light.png`, `stop-button-light-hover.png`, `stop-button-light-focus-visible.png`, `stop-button-light-pressed.png`.

#### toast

Toast (error: Couldn’t copy to clipboard). Copy on a code block failed (the capture browser refuses clipboard writes), and ChatGPT said so in a toast at the top centre: an icon, a bold line, a second line, and a close button.

Page copy: `thread-dark-copied`. Finder: `() => C(T('Couldn\u2019t copy to clipboard'), '.alert-root')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 539.05 x 66 |
| Padding | 8px 12px |
| Gap | 8px |
| Border | 1px solid #fa423e @ 0.4 |
| Radius | 12px |
| Background | #280b0a |
| Box shadow | #000000 @ 0.1 0px 4px 12px 0px |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ff6764 |
| Text node | div.flex.min-h-6.items-center: -apple-system-body 16px/24px 500, #ff6764 |
| Transition | none |
| Icon | 16 x 16, colour #ff6764, fill #000000 |
| Painted layers | div.alert-root.inline-flex.flex-col 539.0x66.0 bg #280b0a border T:1px solid #fa423e @ 0.4 / R:1px solid #fa423e @ 0.4 / B:1px solid #fa423e @ 0.4 / L:1px solid #fa423e @ 0.4 r 12px shadow #000000 @ 0.1 0px 4px 12px 0px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 539.05 x 66 |
| Padding | 8px 12px |
| Gap | 8px |
| Border | 1px solid #e02e2a @ 0.15 |
| Radius | 12px |
| Background | #fff0f0 |
| Box shadow | #000000 @ 0.1 0px 4px 12px 0px |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #e02e2a |
| Text node | div.flex.min-h-6.items-center: -apple-system-body 16px/24px 500, #e02e2a |
| Transition | none |
| Icon | 16 x 16, colour #e02e2a, fill #000000 |
| Painted layers | div.alert-root.inline-flex.flex-col 539.0x66.0 bg #fff0f0 border T:1px solid #e02e2a @ 0.15 / R:1px solid #e02e2a @ 0.15 / B:1px solid #e02e2a @ 0.15 / L:1px solid #e02e2a @ 0.15 r 12px shadow #000000 @ 0.1 0px 4px 12px 0px |
| How | at rest |

Crops: `toast-default.png`, `toast-light.png`.

#### toast-close

Icon button (close toast).

Page copy: `thread-dark-copied`. Finder: `() => C(T('Couldn\u2019t copy to clipboard'), '.alert-root').querySelector('button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #ffffff @ 0.00509804 | = | #ffffff @ 0.00509804 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #99c8ff offset 0px | = |
| Font | -apple-system-body 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ff6764 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ff6764, fill #000000 | = | = | = |
| Ancestor paint | 2 up div.alert-root.inline-flex.flex-col bg #280b0a shadow #000000 @ 0.1 0px 4px 12px 0px | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |
| Painted layers | - | button.flex.size-6.shrink-0 24.0x24.0 bg #ffffff @ 0.00509804 r 9999px | button.flex.size-6.shrink-0 24.0x24.0 r 9999px outline 1px auto #99c8ff offset 0px | button.flex.size-6.shrink-0 24.0x24.0 bg #ffffff @ 0.00509804 r 9999px |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #000000 @ 0.00254902 | = | #000000 @ 0.00254902 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | -apple-system-body 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #e02e2a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #e02e2a, fill #000000 | = | = | = |
| Ancestor paint | 2 up div.alert-root.inline-flex.flex-col bg #fff0f0 shadow #000000 @ 0.1 0px 4px 12px 0px | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |
| Painted layers | - | button.flex.size-6.shrink-0 24.0x24.0 bg #000000 @ 0.00254902 r 9999px | button.flex.size-6.shrink-0 24.0x24.0 r 9999px outline 1px auto #005fcc offset 0px | button.flex.size-6.shrink-0 24.0x24.0 bg #000000 @ 0.00254902 r 9999px |

Crops: `toast-close-default.png`, `toast-close-hover.png`, `toast-close-focus-visible.png`, `toast-close-pressed.png`, `toast-close-light.png`, `toast-close-light-hover.png`, `toast-close-light-focus-visible.png`, `toast-close-light-pressed.png`.

#### save-chat

Popover (Save chat, temporary chat). After the first answer in a temporary chat, a popover under the header offers to save the chat to the history.

Page copy: `thread-dark-copied`. Finder: `() => PW(T('Save chat'), 300)`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 320 x 88 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #303030 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 8px -2px |
| Outline | none |
| Font | -apple-system-body 14px/20px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | div.min-w-0.text-base.font-medium: -apple-system-body 16px/18px 500, #ededed, ls -0.08px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 1112, 54) |
| Icon | 16 x 16, colour #afafaf, fill #000000 |
| Painted layers | div.w-fit.text-sm.whitespace-normal 320.0x88.0 bg #303030 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 8px -2px; button.no-drag.cursor-interaction.items-center 24.0x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px; div.pointer-events-none.absolute.rotate-45 17.0x17.0 bg #303030 r 2px |
| Tokens | --radix-tooltip-content-available-height 838px; --radix-tooltip-content-available-width 1424px; --radix-tooltip-trigger-width 36px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 320 x 88 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 8px -2px |
| Outline | none |
| Font | -apple-system-body 14px/20px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | div.min-w-0.text-base.font-medium: -apple-system-body 16px/18px 500, #0d0d0d, ls -0.08px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 1112, 54) |
| Icon | 16 x 16, colour #8f8f8f, fill #000000 |
| Painted layers | div.w-fit.text-sm.whitespace-normal 320.0x88.0 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 8px -2px; button.no-drag.cursor-interaction.items-center 24.0x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px; div.pointer-events-none.absolute.rotate-45 17.0x17.0 bg #ffffff r 2px |
| Tokens | --radix-tooltip-content-available-height 838px; --radix-tooltip-content-available-width 1424px; --radix-tooltip-trigger-width 36px |
| How | at rest |

Crops: `save-chat-default.png`, `save-chat-light.png`.

#### temp-bubble

User bubble (temporary chat). In a temporary chat the user bubble keeps the accent fill and gains a dashed outline.

Page copy: `thread-dark-copied`. Finder: `() => Q('[class*="bg-user-message"]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 537.59 x 98 |
| Padding | 10px 16px |
| Border | none |
| Radius | 22px |
| Background | #173e76 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f6fafe |
| Text node | div.text-size-chat.whitespace-pre-wrap: -apple-system-body 16px/26px 400, #f6fafe |
| Transition | none |
| Icon | 537.59 x 98, colour #f6fafe, fill #000000 |
| Painted layers | div.bg-user-message.text-user-message.min-w-0 537.6x98.0 bg #173e76 r 22px |
| Tokens | --thread-content-margin calc(.25rem * 4); --user-chat-width 70% |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 537.59 x 98 |
| Padding | 10px 16px |
| Border | none |
| Radius | 22px |
| Background | #e8f3fe |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0c274a |
| Text node | div.text-size-chat.whitespace-pre-wrap: -apple-system-body 16px/26px 400, #0c274a |
| Transition | none |
| Icon | 537.59 x 98, colour #0c274a, fill #000000 |
| Painted layers | div.bg-user-message.text-user-message.min-w-0 537.6x98.0 bg #e8f3fe r 22px |
| Tokens | --thread-content-margin calc(.25rem * 4); --user-chat-width 70% |
| How | at rest |

Crops: `temp-bubble-default.png`, `temp-bubble-light.png`.

### Menus

#### chat-menu

Menu (chat row). Rename, Pin, Share, Archive, Delete (danger), Move to project; hairline separators between groups.

Page copy: `home-dark-chat-menu`. Finder: `() => Q('[role=menu]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 188.88 x 287 |
| Padding | 10px |
| Border | none |
| Radius | 16px |
| Background | #303030 @ 0.9 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.15 0px 0px 0px 0.5px, #ffffff @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px |
| Backdrop filter | blur(8px) |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | span.truncate: -apple-system-body 14px/20px 400, #ededed |
| Transition | none |
| Icon | 16 x 16, colour #ededed, fill #000000 |
| Painted layers | div.no-drag.z-50.m-px 188.9x287.0 bg #303030 @ 0.9 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.15 0px 0px 0px 0.5px, #ffffff @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px; span.icon-sm.shrink-0.bg-current 18.0x18.0 bg #ededed; span.icon-sm.shrink-0.bg-current 18.0x18.0 bg #ededed; div.h-px.w-full.bg-border 152.9x1.0 bg #ffffff @ 0.15; span.icon-sm.shrink-0.bg-current 18.0x18.0 bg #ededed; div.h-px.w-full.bg-border 152.9x1.0 bg #ffffff @ 0.15 |
| Tokens | --app-menu-gutter calc(.25rem * 2.5); --app-menu-separator-gutter calc(.25rem * 2); --color-border-overlay #ffffff26; --padding-row-x calc(.25rem * 2); --radix-dropdown-menu-content-available-height 682.65625px; --radix-dropdown-menu-content-available-width 1428px; --radix-dropdown-menu-content-transform-origin 0% 289px; --radix-dropdown-menu-trigger-height 20px; --radix-dropdown-menu-trigger-width 20px; --shadow-dropdown-overlay 0px 0px 0px .5px #ffffff26, 0px 8px 16px -4px #0000001f |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 188.88 x 287 |
| Padding | 10px |
| Border | none |
| Radius | 16px |
| Background | #ffffff @ 0.9 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px |
| Backdrop filter | blur(8px) |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span.truncate: -apple-system-body 14px/20px 400, #0d0d0d |
| Transition | none |
| Icon | 16 x 16, colour #0d0d0d, fill #000000 |
| Painted layers | div.no-drag.z-50.m-px 188.9x287.0 bg #ffffff @ 0.9 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px; span.icon-sm.shrink-0.bg-current 18.0x18.0 bg #0d0d0d; span.icon-sm.shrink-0.bg-current 18.0x18.0 bg #0d0d0d; div.h-px.w-full.bg-border 152.9x1.0 bg #000000 @ 0.1; span.icon-sm.shrink-0.bg-current 18.0x18.0 bg #0d0d0d; div.h-px.w-full.bg-border 152.9x1.0 bg #000000 @ 0.1 |
| Tokens | --app-menu-gutter calc(.25rem * 2.5); --app-menu-separator-gutter calc(.25rem * 2); --color-border-overlay #0000001a; --padding-row-x calc(.25rem * 2); --radix-dropdown-menu-content-available-height 682.65625px; --radix-dropdown-menu-content-available-width 1428px; --radix-dropdown-menu-content-transform-origin 0% 289px; --radix-dropdown-menu-trigger-height 20px; --radix-dropdown-menu-trigger-width 20px; --shadow-dropdown-overlay 0px 0px 0px .5px #0000001a, 0px 8px 16px -4px #0000001f |
| How | at rest |

Crops: `chat-menu-default.png`, `chat-menu-light.png`.

#### menu-item

Menu item.

Page copy: `home-dark-chat-menu`. Finder: `() => Q('[role=menu] [role=menuitem]', 0)`.

Dark theme.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 168.88 x 36 | = | = |
| Padding | 6px 10px | = | = |
| Border | none | = | = |
| Radius | 12px | = | = |
| Background | transparent | #ffffff @ 0.1 | #ffffff @ 0.1 |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ededed | = | = |
| Text node | span.truncate: -apple-system-body 14px/20px 400, #ededed | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Painted layers | span.icon-sm.shrink-0.bg-current 18.0x18.0 bg #ededed | div.no-drag.itemBase-Uk8vyp.rounded-xl 168.9x36.0 bg #ffffff @ 0.1 r 12px; span.icon-sm.shrink-0.bg-current 18.0x18.0 bg #ededed | div.no-drag.itemBase-Uk8vyp.rounded-xl 168.9x36.0 bg #ffffff @ 0.1 r 12px; span.icon-sm.shrink-0.bg-current 18.0x18.0 bg #ededed |
| Ancestor paint | 1 up div.no-drag.z-50.m-px bg #303030 @ 0.9 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.15 0px 0px 0px 0.5px, #ffffff @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px | = | = |
| Tokens | --spacing .25rem | = | = |
| How | at rest | mouse hover | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-pressed |
|---|---|---|---|
| Size (w x h) | 168.88 x 36 | = | = |
| Padding | 6px 10px | = | = |
| Border | none | = | = |
| Radius | 12px | = | = |
| Background | transparent | #000000 @ 0.05 | #000000 @ 0.05 |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0d0d0d | = | = |
| Text node | span.truncate: -apple-system-body 14px/20px 400, #0d0d0d | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Painted layers | span.icon-sm.shrink-0.bg-current 18.0x18.0 bg #0d0d0d | div.no-drag.itemBase-Uk8vyp.rounded-xl 168.9x36.0 bg #000000 @ 0.05 r 12px; span.icon-sm.shrink-0.bg-current 18.0x18.0 bg #0d0d0d | div.no-drag.itemBase-Uk8vyp.rounded-xl 168.9x36.0 bg #000000 @ 0.05 r 12px; span.icon-sm.shrink-0.bg-current 18.0x18.0 bg #0d0d0d |
| Ancestor paint | 1 up div.no-drag.z-50.m-px bg #ffffff @ 0.9 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px | = | = |
| Tokens | --spacing .25rem | = | = |
| How | at rest | mouse hover | mouse button held down on it (:hover:active) |

Crops: `menu-item-default.png`, `menu-item-hover.png`, `menu-item-pressed.png`, `menu-item-light.png`, `menu-item-light-hover.png`, `menu-item-light-pressed.png`.

#### menu-item-danger

Menu item (Delete, danger).

Page copy: `home-dark-chat-menu`. Finder: `() => C(T('Delete', Q('[role=menu]')), '[role=menuitem]')`.

Dark theme.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 168.88 x 36 | = |
| Padding | 6px 10px | = |
| Border | none | = |
| Radius | 12px | = |
| Background | transparent | #ffffff @ 0.1 |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system-body 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #ff6764 | = |
| Text node | span.truncate: -apple-system-body 14px/20px 400, #ff6764 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | span.icon-sm.shrink-0.bg-current 18.0x18.0 bg #ff6764 | div.no-drag.itemBase-Uk8vyp.rounded-xl 168.9x36.0 bg #ffffff @ 0.1 r 12px; span.icon-sm.shrink-0.bg-current 18.0x18.0 bg #ff6764 |
| Ancestor paint | 1 up div.no-drag.z-50.m-px bg #303030 @ 0.9 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.15 0px 0px 0px 0.5px, #ffffff @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px | = |
| Tokens | --spacing .25rem | = |
| How | at rest | mouse hover |

Light theme.

| Property | light | light-hover |
|---|---|---|
| Size (w x h) | 168.88 x 36 | = |
| Padding | 6px 10px | = |
| Border | none | = |
| Radius | 12px | = |
| Background | transparent | #000000 @ 0.05 |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system-body 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #e02e2a | = |
| Text node | span.truncate: -apple-system-body 14px/20px 400, #e02e2a | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | span.icon-sm.shrink-0.bg-current 18.0x18.0 bg #e02e2a | div.no-drag.itemBase-Uk8vyp.rounded-xl 168.9x36.0 bg #000000 @ 0.05 r 12px; span.icon-sm.shrink-0.bg-current 18.0x18.0 bg #e02e2a |
| Ancestor paint | 1 up div.no-drag.z-50.m-px bg #ffffff @ 0.9 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px | = |
| Tokens | --spacing .25rem | = |
| How | at rest | mouse hover |

Crops: `menu-item-danger-default.png`, `menu-item-danger-hover.png`, `menu-item-danger-light.png`, `menu-item-danger-light-hover.png`.

#### plus-menu

Menu (composer +). Not a role=menu: a popover of buttons at the composer's width, each with a title and a grey hint.

Page copy: `home-dark-plus-menu`. Finder: `() => PW(TS('Add photos'), 500)`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 750 x 36 |
| Padding | 6px 8px |
| Border | none |
| Radius | 12px |
| Background | #ffffff @ 0.1 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 14px/20px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | span.min-w-0.truncate.shrink-0: -apple-system-body 14px/20px 400, #ededed |
| Transition | none |
| Cursor | pointer |
| Icon | 20 x 20, colour #ededed, fill #000000 |
| Painted layers | button.text-default.outline-hidden.cursor-interaction 750.0x36.0 bg #ffffff @ 0.1 r 12px |
| Tokens | --app-menu-item-height calc(.25rem * 9); --app-menu-item-padding calc(.25rem * 1.5) calc(.25rem * 2.5); --padding-row-x calc(.25rem * 2); --padding-row-y calc(.25rem * 1.25); --radius-xl calc(.75rem * 1); --spacing .25rem; --spacing-menu-item-content calc(.25rem * 3); --suggestion-menu-item-padding calc(.25rem * 1.5) calc(.25rem * 2); --suggestion-menu-item-radius calc(calc(.25rem * 5) - calc(.25rem * 2)) |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 750 x 36 |
| Padding | 6px 8px |
| Border | none |
| Radius | 12px |
| Background | #000000 @ 0.05 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 14px/20px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span.min-w-0.truncate.shrink-0: -apple-system-body 14px/20px 400, #0d0d0d |
| Transition | none |
| Cursor | pointer |
| Icon | 20 x 20, colour #0d0d0d, fill #000000 |
| Painted layers | button.text-default.outline-hidden.cursor-interaction 750.0x36.0 bg #000000 @ 0.05 r 12px |
| Tokens | --app-menu-item-height calc(.25rem * 9); --app-menu-item-padding calc(.25rem * 1.5) calc(.25rem * 2.5); --padding-row-x calc(.25rem * 2); --padding-row-y calc(.25rem * 1.25); --radius-xl calc(.75rem * 1); --spacing .25rem; --spacing-menu-item-content calc(.25rem * 3); --suggestion-menu-item-padding calc(.25rem * 1.5) calc(.25rem * 2); --suggestion-menu-item-radius calc(calc(.25rem * 5) - calc(.25rem * 2)) |
| How | at rest |

Crops: `plus-menu-default.png`, `plus-menu-light.png`.

#### plus-menu-item

Menu item with hint (composer +).

Page copy: `home-dark-plus-menu`. Finder: `() => C(TS('Add from library'), 'button')`.

Dark theme.

| Property | default | hover | highlighted |
|---|---|---|---|
| Size (w x h) | 750 x 36 | = | = |
| Padding | 6px 8px | = | = |
| Border | none | = | = |
| Radius | 12px | = | = |
| Background | transparent | = | #ffffff @ 0.1 |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ededed | = | = |
| Text node | span.min-w-0.truncate.shrink-0: -apple-system-body 14px/20px 400, #ededed | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 20 x 20, colour #ededed, fill #000000 | = | = |
| Tokens | --app-menu-item-height calc(.25rem * 9); --app-menu-item-padding calc(.25rem * 1.5) calc(.25rem * 2.5); --padding-row-x calc(.25rem * 2); --padding-row-y calc(.25rem * 1.25); --radius-xl calc(.75rem * 1); --spacing .25rem; --spacing-menu-item-content calc(.25rem * 3); --suggestion-menu-item-padding calc(.25rem * 1.5) calc(.25rem * 2); --suggestion-menu-item-radius calc(calc(.25rem * 5) - calc(.25rem * 2)) | = | = |
| How | at rest | mouse hover | at rest, captured highlighted |
| Painted layers | - | = | button.text-default.outline-hidden.cursor-interaction 750.0x36.0 bg #ffffff @ 0.1 r 12px |

Light theme.

| Property | light | light-hover | light-highlighted |
|---|---|---|---|
| Size (w x h) | 750 x 36 | = | = |
| Padding | 6px 8px | = | = |
| Border | none | = | = |
| Radius | 12px | = | = |
| Background | transparent | = | #000000 @ 0.05 |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0d0d0d | = | = |
| Text node | span.min-w-0.truncate.shrink-0: -apple-system-body 14px/20px 400, #0d0d0d | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 20 x 20, colour #0d0d0d, fill #000000 | = | = |
| Tokens | --app-menu-item-height calc(.25rem * 9); --app-menu-item-padding calc(.25rem * 1.5) calc(.25rem * 2.5); --padding-row-x calc(.25rem * 2); --padding-row-y calc(.25rem * 1.25); --radius-xl calc(.75rem * 1); --spacing .25rem; --spacing-menu-item-content calc(.25rem * 3); --suggestion-menu-item-padding calc(.25rem * 1.5) calc(.25rem * 2); --suggestion-menu-item-radius calc(calc(.25rem * 5) - calc(.25rem * 2)) | = | = |
| How | at rest | mouse hover | at rest, captured highlighted |
| Painted layers | - | = | button.text-default.outline-hidden.cursor-interaction 750.0x36.0 bg #000000 @ 0.05 r 12px |

Other finders: highlighted: `() => C(TS('Add photos'), 'button')`; light-highlighted: `() => C(TS('Add photos'), 'button')`.

Crops: `plus-menu-item-default.png`, `plus-menu-item-hover.png`, `plus-menu-item-highlighted.png`, `plus-menu-item-light.png`, `plus-menu-item-light-hover.png`, `plus-menu-item-light-highlighted.png`.

#### user-menu

Menu (account).

Page copy: `home-dark-user-menu`. Finder: `() => Q('[role=menu]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 324 x 316 |
| Padding | 10px |
| Border | none |
| Radius | 16px |
| Background | #303030 @ 0.9 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.15 0px 0px 0px 0.5px, #ffffff @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px |
| Backdrop filter | blur(8px) |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | div.shrink-0.object-cover.rounded-full: -apple-system-body 12px/17.1429px 600, #ffffff |
| Transition | none |
| Icon | 16 x 16, colour #afafaf, fill #000000 |
| Painted layers | div.no-drag.z-50.m-px 324.0x316.0 bg #303030 @ 0.9 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.15 0px 0px 0px 0.5px, #ffffff @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px; div.shrink-0.object-cover.rounded-full 20.0x20.0 bg #8a8a8a r 9999px; div.h-px.w-full.bg-border 288.0x1.0 bg #ffffff @ 0.15; div.h-px.w-full.bg-border 288.0x1.0 bg #ffffff @ 0.15 |
| Tokens | --app-menu-gutter calc(.25rem * 2.5); --app-menu-separator-gutter calc(.25rem * 2); --color-border-overlay #ffffff26; --padding-row-x calc(.25rem * 2); --radix-dropdown-menu-content-available-height 832px; --radix-dropdown-menu-content-available-width 1428px; --radix-dropdown-menu-content-transform-origin 0% 318px; --radix-dropdown-menu-trigger-height 48px; --radix-dropdown-menu-trigger-width 248.1171875px; --shadow-dropdown-overlay 0px 0px 0px .5px #ffffff26, 0px 8px 16px -4px #0000001f |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 324 x 316 |
| Padding | 10px |
| Border | none |
| Radius | 16px |
| Background | #ffffff @ 0.9 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px |
| Backdrop filter | blur(8px) |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | div.shrink-0.object-cover.rounded-full: -apple-system-body 12px/17.1429px 600, #ffffff |
| Transition | none |
| Icon | 16 x 16, colour #8f8f8f, fill #000000 |
| Painted layers | div.no-drag.z-50.m-px 324.0x316.0 bg #ffffff @ 0.9 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px; div.shrink-0.object-cover.rounded-full 20.0x20.0 bg #8a8a8a r 9999px; div.h-px.w-full.bg-border 288.0x1.0 bg #000000 @ 0.1; div.h-px.w-full.bg-border 288.0x1.0 bg #000000 @ 0.1 |
| Tokens | --app-menu-gutter calc(.25rem * 2.5); --app-menu-separator-gutter calc(.25rem * 2); --color-border-overlay #0000001a; --padding-row-x calc(.25rem * 2); --radix-dropdown-menu-content-available-height 832px; --radix-dropdown-menu-content-available-width 1428px; --radix-dropdown-menu-content-transform-origin 0% 318px; --radix-dropdown-menu-trigger-height 48px; --radix-dropdown-menu-trigger-width 248.1171875px; --shadow-dropdown-overlay 0px 0px 0px .5px #0000001a, 0px 8px 16px -4px #0000001f |
| How | at rest |

Crops: `user-menu-default.png`, `user-menu-light.png`.

#### checkbox-menu-item

Checkbox menu item (checked). `menuitemcheckbox`, aria-checked=true, a trailing check.

Page copy: `settings-dark-notifications-menu`. Finder: `() => Q('[role=menuitemcheckbox]')`.

Dark theme.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 220 x 36 | = |
| Padding | 6px 10px | = |
| Border | none | = |
| Radius | 12px | = |
| Background | transparent | #ffffff @ 0.1 |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system-body 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #ededed | = |
| Text node | span.truncate: -apple-system-body 14px/20px 400, #ededed | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #ededed | = |
| Ancestor paint | 1 up div.no-drag.z-50.m-px bg #303030 @ 0.9 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.15 0px 0px 0px 0.5px, #ffffff @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px | = |
| Tokens | --spacing .25rem | = |
| How | at rest | mouse hover |
| Painted layers | - | div.no-drag.flex.flex-col 220.0x36.0 bg #ffffff @ 0.1 r 12px |

Light theme.

| Property | light | light-hover |
|---|---|---|
| Size (w x h) | 220 x 36 | = |
| Padding | 6px 10px | = |
| Border | none | = |
| Radius | 12px | = |
| Background | transparent | #000000 @ 0.05 |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system-body 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #0d0d0d | = |
| Text node | span.truncate: -apple-system-body 14px/20px 400, #0d0d0d | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #0d0d0d | = |
| Ancestor paint | 1 up div.no-drag.z-50.m-px bg #ffffff @ 0.9 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px | = |
| Tokens | --spacing .25rem | = |
| How | at rest | mouse hover |
| Painted layers | - | div.no-drag.flex.flex-col 220.0x36.0 bg #000000 @ 0.05 r 12px |

Crops: `checkbox-menu-item-default.png`, `checkbox-menu-item-hover.png`, `checkbox-menu-item-light.png`, `checkbox-menu-item-light-hover.png`.

#### accent-menu

Select listbox (accent colour). Default, Blue (checked), Green, Yellow, Pink, Orange, Purple, White, Custom; each with a colour dot.

Page copy: `settings-dark-accent-menu`. Finder: `() => Q('[role=menu]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 240 x 344 |
| Padding | 10px |
| Border | none |
| Radius | 16px |
| Background | #303030 @ 0.9 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.15 0px 0px 0px 0.5px, #ffffff @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px |
| Backdrop filter | blur(8px) |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | span.flex.items-center.gap-2: -apple-system-body 14px/20px 500, #ededed |
| Transition | none |
| Icon | 18 x 18, colour #ededed |
| Painted layers | div.no-drag.z-50.m-px 240.0x344.0 bg #303030 @ 0.9 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.15 0px 0px 0px 0.5px, #ffffff @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px; span.size-3.shrink-0.rounded-full 12.0x12.0 bg #ffffff border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px; span.size-3.shrink-0.rounded-full 12.0x12.0 bg #3566f0 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px; span.size-3.shrink-0.rounded-full 12.0x12.0 bg #04bb9f border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px; span.size-3.shrink-0.rounded-full 12.0x12.0 bg #ffcc38 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px; span.size-3.shrink-0.rounded-full 12.0x12.0 bg #fa70ab border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px |
| Tokens | --app-menu-gutter calc(.25rem * 2.5); --app-menu-min-width calc(.25rem * 60); --color-border-overlay #ffffff26; --radix-dropdown-menu-content-available-height 577.203125px; --radix-dropdown-menu-content-available-width 1428px; --radix-dropdown-menu-content-transform-origin 100% 0px; --radix-dropdown-menu-trigger-height 28px; --radix-dropdown-menu-trigger-width 80.78125px; --shadow-dropdown-overlay 0px 0px 0px .5px #ffffff26, 0px 8px 16px -4px #0000001f; --spacing .25rem |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 240 x 344 |
| Padding | 10px |
| Border | none |
| Radius | 16px |
| Background | #ffffff @ 0.9 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px |
| Backdrop filter | blur(8px) |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span.flex.items-center.gap-2: -apple-system-body 14px/20px 500, #0d0d0d |
| Transition | none |
| Icon | 18 x 18, colour #0d0d0d |
| Painted layers | div.no-drag.z-50.m-px 240.0x344.0 bg #ffffff @ 0.9 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px; span.size-3.shrink-0.rounded-full 12.0x12.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px; span.size-3.shrink-0.rounded-full 12.0x12.0 bg #3566f0 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px; span.size-3.shrink-0.rounded-full 12.0x12.0 bg #04bb9f border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px; span.size-3.shrink-0.rounded-full 12.0x12.0 bg #ffcc38 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px; span.size-3.shrink-0.rounded-full 12.0x12.0 bg #fa70ab border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px |
| Tokens | --app-menu-gutter calc(.25rem * 2.5); --app-menu-min-width calc(.25rem * 60); --color-border-overlay #0000001a; --radix-dropdown-menu-content-available-height 577.203125px; --radix-dropdown-menu-content-available-width 1428px; --radix-dropdown-menu-content-transform-origin 100% 0px; --radix-dropdown-menu-trigger-height 28px; --radix-dropdown-menu-trigger-width 80.78125px; --shadow-dropdown-overlay 0px 0px 0px .5px #0000001a, 0px 8px 16px -4px #0000001f; --spacing .25rem |
| How | at rest |

Crops: `accent-menu-default.png`, `accent-menu-light.png`.

#### accent-item

Select option (accent).

Page copy: `settings-dark-accent-menu`. Finder: `() => Q('[role=menu] [role=menuitem], [role=menu] [role=menuitemradio]', 2)`.

Dark theme.

| Property | default | hover | checked |
|---|---|---|---|
| Size (w x h) | 220 x 36 | = | = |
| Padding | 6px 10px | = | = |
| Border | none | = | = |
| Radius | 12px | = | = |
| Background | transparent | #ffffff @ 0.1 | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ededed | = | = |
| Text node | span.flex.items-center.gap-2: -apple-system-body 14px/20px 500, #ededed | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Painted layers | span.size-3.shrink-0.rounded-full 12.0x12.0 bg #04bb9f border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px | div.no-drag.itemBase-Uk8vyp.rounded-xl 220.0x36.0 bg #ffffff @ 0.1 r 12px; span.size-3.shrink-0.rounded-full 12.0x12.0 bg #04bb9f border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px | span.size-3.shrink-0.rounded-full 12.0x12.0 bg #3566f0 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px |
| Ancestor paint | 3 up div.no-drag.z-50.m-px bg #303030 @ 0.9 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.15 0px 0px 0px 0.5px, #ffffff @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px | = | = |
| Tokens | --spacing .25rem | = | = |
| How | at rest | mouse hover | at rest, captured checked |
| Icon | - | = | 18 x 18, colour #ededed |

Light theme.

| Property | light | light-hover | light-checked |
|---|---|---|---|
| Size (w x h) | 220 x 36 | = | = |
| Padding | 6px 10px | = | = |
| Border | none | = | = |
| Radius | 12px | = | = |
| Background | transparent | #000000 @ 0.05 | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0d0d0d | = | = |
| Text node | span.flex.items-center.gap-2: -apple-system-body 14px/20px 500, #0d0d0d | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Painted layers | span.size-3.shrink-0.rounded-full 12.0x12.0 bg #04bb9f border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px | div.no-drag.itemBase-Uk8vyp.rounded-xl 220.0x36.0 bg #000000 @ 0.05 r 12px; span.size-3.shrink-0.rounded-full 12.0x12.0 bg #04bb9f border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px | span.size-3.shrink-0.rounded-full 12.0x12.0 bg #3566f0 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px |
| Ancestor paint | 3 up div.no-drag.z-50.m-px bg #ffffff @ 0.9 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.12 0px 8px 16px -4px | = | = |
| Tokens | --spacing .25rem | = | = |
| How | at rest | mouse hover | at rest, captured checked |
| Icon | - | = | 18 x 18, colour #0d0d0d |

Other finders: checked: `() => Q('[role=menu] [aria-checked=true]') // C(T('Blue', Q('[role=menu]')), '[role^=menuitem]')`; light-checked: `() => Q('[role=menu] [aria-checked=true]') // C(T('Blue', Q('[role=menu]')), '[role^=menuitem]')`.

Crops: `accent-item-default.png`, `accent-item-hover.png`, `accent-item-checked.png`, `accent-item-light.png`, `accent-item-light-hover.png`, `accent-item-light-checked.png`.

### Dialogs

#### confirm-dialog

Dialog (delete confirmation). 420 wide: title, body naming the chat, Cancel and a danger Delete chat, close in the corner.

Page copy: `home-dark-delete-confirm`. Finder: `() => Q('[role=dialog]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 420 x 164 |
| Padding | 0px |
| Border | none |
| Radius | 24px |
| Background | #303030 @ 0.9 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.1 0px 4px 8px -2px |
| Backdrop filter | blur(24px) |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | div.heading-dialog.min-w-0.font-semibold: -apple-system-body 20px/28px 600, #ededed |
| Transition | height 0.3s cubic-bezier(0.23, 1, 0.32, 1) |
| Icon | 16 x 16, colour #ededed @ 0.8 |
| Painted layers | div.codex-dialog.z-50.outline-none 420.0x164.0 bg #303030 @ 0.9 r 24px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.1 0px 4px 8px -2px; button.no-drag.cursor-interaction.items-center 83.9x32.0 bg #303030 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px; button.no-drag.cursor-interaction.items-center 116.9x32.0 bg #ff6764 @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| Tokens | --dialog-content-height 164px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 420 x 164 |
| Padding | 0px |
| Border | none |
| Radius | 24px |
| Background | #ffffff @ 0.9 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.1 0px 4px 8px -2px |
| Backdrop filter | blur(24px) |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | div.heading-dialog.min-w-0.font-semibold: -apple-system-body 20px/28px 600, #0d0d0d |
| Transition | height 0.3s cubic-bezier(0.23, 1, 0.32, 1) |
| Icon | 16 x 16, colour #0d0d0d @ 0.8 |
| Painted layers | div.codex-dialog.z-50.outline-none 420.0x164.0 bg #ffffff @ 0.9 r 24px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.1 0px 4px 8px -2px; button.no-drag.cursor-interaction.items-center 83.9x32.0 bg #f3f3f3 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px; button.no-drag.cursor-interaction.items-center 116.9x32.0 bg #e02e2a @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| Tokens | --dialog-content-height 164px |
| How | at rest |

Crops: `confirm-dialog-default.png`, `confirm-dialog-light.png`.

#### dialog-backdrop

Dialog backdrop.

Page copy: `home-dark-delete-confirm`. Finder: `() => [...document.querySelectorAll('body *')].find((e) => { const c = getComputedStyle(e); const r = e.getBoundingClientRect(); return (c.position === 'fixed' // c.position === 'absolute') && r.width >= innerWidth - 1 && r.height >= innerHeight - 1 && (c.backgroundColor !== 'rgba(0, 0, 0, 0)' // c.backdropFilter !== 'none'); })`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 @ 0.133 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Transition | none |
| Painted layers | div.codex-dialog-overlay.inset-0.z-50 1440.0x900.0 bg #000000 @ 0.133 |
| Tokens | --color-dialog-overlay #0002 |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 @ 0.133 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Transition | none |
| Painted layers | div.codex-dialog-overlay.inset-0.z-50 1440.0x900.0 bg #000000 @ 0.133 |
| Tokens | --color-dialog-overlay #0002 |
| How | at rest |

Crops: none.

#### button-danger

Danger button (Delete chat).

Page copy: `home-dark-delete-confirm`. Finder: `() => B('Delete chat')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 116.86 x 32 | = | = | = |
| Padding | 6px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ff6764 @ 0.1 | #ff6764 @ 0.2 | = | #ff6764 @ 0.2 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ff6764 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 116.9x32.0 bg #ff6764 @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 116.9x32.0 bg #ff6764 @ 0.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 116.9x32.0 bg #ff6764 @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 116.9x32.0 bg #ff6764 @ 0.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 116.86 x 32 | = | = | = |
| Padding | 6px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #e02e2a @ 0.1 | #e02e2a @ 0.2 | = | #e02e2a @ 0.2 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #e02e2a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 116.9x32.0 bg #e02e2a @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 116.9x32.0 bg #e02e2a @ 0.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 116.9x32.0 bg #e02e2a @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 116.9x32.0 bg #e02e2a @ 0.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `button-danger-default.png`, `button-danger-hover.png`, `button-danger-focus-visible.png`, `button-danger-pressed.png`, `button-danger-light.png`, `button-danger-light-hover.png`, `button-danger-light-focus-visible.png`, `button-danger-light-pressed.png`.

#### button-secondary

Secondary button (Cancel).

Page copy: `home-dark-delete-confirm`. Finder: `() => B('Cancel')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 83.89 x 32 | = | = | = |
| Padding | 6px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #ffffff @ 0.15 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #303030 | #ffffff @ 0.1 | = | #ffffff @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ededed | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 83.9x32.0 bg #303030 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px | button.no-drag.cursor-interaction.items-center 83.9x32.0 bg #ffffff @ 0.1 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px | button.no-drag.cursor-interaction.items-center 83.9x32.0 bg #303030 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 83.9x32.0 bg #ffffff @ 0.1 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 83.89 x 32 | = | = | = |
| Padding | 6px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0.1 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #f3f3f3 | #000000 @ 0.05 | = | #000000 @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 83.9x32.0 bg #f3f3f3 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px | button.no-drag.cursor-interaction.items-center 83.9x32.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px | button.no-drag.cursor-interaction.items-center 83.9x32.0 bg #f3f3f3 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 83.9x32.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `button-secondary-default.png`, `button-secondary-hover.png`, `button-secondary-focus-visible.png`, `button-secondary-pressed.png`, `button-secondary-light.png`, `button-secondary-light-hover.png`, `button-secondary-light-focus-visible.png`, `button-secondary-light-pressed.png`.

#### dialog-close

Dialog close button.

Page copy: `home-dark-delete-confirm`. Finder: `() => B('Close dialog', D() // document)`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #ffffff @ 0.1 | = | #ffffff @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ededed @ 0.8 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ededed @ 0.8 | = | = | = |
| Ancestor paint | 1 up div.codex-dialog.z-50.outline-none bg #303030 @ 0.9 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.1 0px 4px 8px -2px | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |
| Painted layers | - | button.no-drag.cursor-interaction.leading-none 24.0x24.0 bg #ffffff @ 0.1 r 4px | button.no-drag.cursor-interaction.leading-none 24.0x24.0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.leading-none 24.0x24.0 bg #ffffff @ 0.1 r 4px |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #000000 @ 0.05 | = | #000000 @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d @ 0.8 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #0d0d0d @ 0.8 | = | = | = |
| Ancestor paint | 1 up div.codex-dialog.z-50.outline-none bg #ffffff @ 0.9 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.1 0px 4px 8px -2px | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |
| Painted layers | - | button.no-drag.cursor-interaction.leading-none 24.0x24.0 bg #000000 @ 0.05 r 4px | button.no-drag.cursor-interaction.leading-none 24.0x24.0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.leading-none 24.0x24.0 bg #000000 @ 0.05 r 4px |

Crops: `dialog-close-default.png`, `dialog-close-hover.png`, `dialog-close-focus-visible.png`, `dialog-close-pressed.png`, `dialog-close-light.png`, `dialog-close-light-hover.png`, `dialog-close-light-focus-visible.png`, `dialog-close-light-pressed.png`.

#### search-dialog

Dialog (global search).

Page copy: `home-dark-search`. Finder: `() => Q('[role=dialog]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 720 x 460 |
| Padding | 0px |
| Border | 1px solid #ffffff @ 0.15 |
| Radius | 16px |
| Background | #212121 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.19 0px 16px 32px -8px |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | h3.m-0.px-6.py-2: -apple-system-body 14px/20px 400, #cdcdcd |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, -360, -230) |
| Icon | 20 x 20, colour #cdcdcd, fill #000000 |
| Placeholder | "Search…" #afafaf, opacity 1, 16px |
| Painted layers | div.codex-dialog.z-50.outline-none 720.0x460.0 bg #212121 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.19 0px 16px 32px -8px; header.shrink-0.border-b.transition-colors 718.0x65.0 border B:1px solid #000000 @ 0 |
| Tokens | --codex-window-zoom 1; --spacing .25rem |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 720 x 460 |
| Padding | 0px |
| Border | 1px solid #000000 @ 0.1 |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.19 0px 16px 32px -8px |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | h3.m-0.px-6.py-2: -apple-system-body 14px/20px 400, #5d5d5d |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, -360, -230) |
| Icon | 20 x 20, colour #5d5d5d, fill #000000 |
| Placeholder | "Search…" #8f8f8f, opacity 1, 16px |
| Painted layers | div.codex-dialog.z-50.outline-none 720.0x460.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.19 0px 16px 32px -8px; header.shrink-0.border-b.transition-colors 718.0x65.0 border B:1px solid #000000 @ 0 |
| Tokens | --codex-window-zoom 1; --spacing .25rem |
| How | at rest |

Crops: `search-dialog-default.png`, `search-dialog-light.png`.

#### search-field

Text field (search).

Page copy: `home-dark-search`, `home-dark-search-empty`. Finder: `() => Q('[role=dialog] input')`.

Dark theme.

| Property | default | focus-visible | typed |
|---|---|---|---|
| Size (w x h) | 642 x 24 | = | 565.13 x 24 |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 16px/24px 400 | = | = |
| Letter spacing | -0.4px | = | = |
| Colour | #ededed | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | "Search…" #afafaf, opacity 1, 16px | = | = |
| Ancestor paint | 3 up div.codex-dialog.z-50.outline-none bg #212121 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.19 0px 16px 32px -8px | = | = |
| How | at rest | keyboard: focus(), Shift+Tab, Tab | at rest, captured typed |

Light theme.

| Property | light | light-focus-visible | light-typed |
|---|---|---|---|
| Size (w x h) | 642 x 24 | = | 565.13 x 24 |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 16px/24px 400 | = | = |
| Letter spacing | -0.4px | = | = |
| Colour | #0d0d0d | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | "Search…" #8f8f8f, opacity 1, 16px | = | = |
| Ancestor paint | 3 up div.codex-dialog.z-50.outline-none bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.19 0px 16px 32px -8px | = | = |
| How | at rest | keyboard: focus(), Shift+Tab, Tab | at rest, captured typed |

Other finders: typed: `() => Q('[role=dialog] input')`; light-typed: `() => Q('[role=dialog] input')`.

Crops: `search-field-default.png`, `search-field-focus-visible.png`, `search-field-typed.png`, `search-field-light.png`, `search-field-light-focus-visible.png`, `search-field-light-typed.png`.

#### search-result

List row (search result).

Page copy: `home-dark-search`. Finder: `() => { const t = TS('Sample title', D()); return t && (C(t, 'button,a,[role=option],li') // W(t, 600)); }`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 694 x 48 | = | = |
| Padding | 8px 12px | = | = |
| Gap | 12px | = | = |
| Border | none | = | = |
| Radius | 12px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #ffffff @ 0.2 offset -2px |
| Font | -apple-system-body 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ededed | = | = |
| Text node | span: -apple-system-body 14px/20px 400, #ededed | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 20 x 20, colour #ededed, fill #000000 | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |
| Painted layers | - | = | a.cursor-interaction.mx-3.flex 694.0x48.0 r 12px outline 2px solid #ffffff @ 0.2 offset -2px |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 694 x 48 | = | = |
| Padding | 8px 12px | = | = |
| Gap | 12px | = | = |
| Border | none | = | = |
| Radius | 12px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #000000 @ 0.15 offset -2px |
| Font | -apple-system-body 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0d0d0d | = | = |
| Text node | span: -apple-system-body 14px/20px 400, #0d0d0d | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 20 x 20, colour #0d0d0d, fill #000000 | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |
| Painted layers | - | = | a.cursor-interaction.mx-3.flex 694.0x48.0 r 12px outline 2px solid #000000 @ 0.15 offset -2px |

Crops: `search-result-default.png`, `search-result-hover.png`, `search-result-focus-visible.png`, `search-result-light.png`, `search-result-light-hover.png`, `search-result-light-focus-visible.png`.

#### search-tab

Tab (search filter).

Page copy: `home-dark-search-empty`. Finder: `() => Q('[role=dialog] [role=tab][aria-selected=false]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed | selected |
|---|---|---|---|---|---|
| Size (w x h) | 61.52 x 36 | = | = | = | 40.08 x 36 |
| Padding | 0px 12px | = | = | = | = |
| Gap | 6px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | transparent | #ffffff @ 0.1 | = | #ffffff @ 0.1 | #ededed @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = | = | = |
| Font | -apple-system-body 14px/20px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #cdcdcd | = | = | = | #ededed |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| How | at rest | mouse hover | keyboard: Shift keydown, then focus() | mouse button held down on it (:hover:active) | at rest, captured selected |
| Painted layers | - | button.cursor-interaction.items-center.text-sm 61.5x36.0 bg #ffffff @ 0.1 r 9999px | button.cursor-interaction.items-center.text-sm 61.5x36.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | button.cursor-interaction.items-center.text-sm 61.5x36.0 bg #ffffff @ 0.1 r 9999px | button.cursor-interaction.items-center.text-sm 40.1x36.0 bg #ededed @ 0.05 r 9999px |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed | light-selected |
|---|---|---|---|---|---|
| Size (w x h) | 61.52 x 36 | = | = | = | 40.08 x 36 |
| Padding | 0px 12px | = | = | = | = |
| Gap | 6px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | transparent | #000000 @ 0.05 | = | #000000 @ 0.05 | #0d0d0d @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = | = | = |
| Font | -apple-system-body 14px/20px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #5d5d5d | = | = | = | #0d0d0d |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| How | at rest | mouse hover | keyboard: Shift keydown, then focus() | mouse button held down on it (:hover:active) | at rest, captured selected |
| Painted layers | - | button.cursor-interaction.items-center.text-sm 61.5x36.0 bg #000000 @ 0.05 r 9999px | button.cursor-interaction.items-center.text-sm 61.5x36.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | button.cursor-interaction.items-center.text-sm 61.5x36.0 bg #000000 @ 0.05 r 9999px | button.cursor-interaction.items-center.text-sm 40.1x36.0 bg #0d0d0d @ 0.05 r 9999px |

Other finders: selected: `() => Q('[role=dialog] [role=tab][aria-selected=true]')`; light-selected: `() => Q('[role=dialog] [role=tab][aria-selected=true]')`.

Crops: `search-tab-default.png`, `search-tab-hover.png`, `search-tab-focus-visible.png`, `search-tab-pressed.png`, `search-tab-selected.png`, `search-tab-light.png`, `search-tab-light-hover.png`, `search-tab-light-focus-visible.png`, `search-tab-light-pressed.png`, `search-tab-light-selected.png`.

#### search-empty

Empty state (no results).

Page copy: `home-dark-search-empty`. Finder: `() => W(T('No results', D()), 200)`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 718 x 333 |
| Padding | 20px 24px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #afafaf |
| Transition | none |
| Icon | 20 x 20, colour #afafaf, fill #000000 |
| Ancestor paint | 2 up div.codex-dialog.z-50.outline-none bg #212121 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.19 0px 16px 32px -8px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 718 x 333 |
| Padding | 20px 24px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #8f8f8f |
| Transition | none |
| Icon | 20 x 20, colour #8f8f8f, fill #000000 |
| Ancestor paint | 2 up div.codex-dialog.z-50.outline-none bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.19 0px 16px 32px -8px |
| How | at rest |

Crops: `search-empty-default.png`, `search-empty-light.png`.

### Library

#### library-title

Page title (Library).

Page copy: `library-dark`. Finder: `() => Q('main h1')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 74.11 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 24px/28.8px 500 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | span: -apple-system-body 24px/28.8px 500, #ededed |
| Transition | none |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 74.11 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 24px/28.8px 500 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span: -apple-system-body 24px/28.8px 500, #0d0d0d |
| Transition | none |
| How | at rest |

Crops: `library-title-default.png`, `library-title-light.png`.

#### library-icon-button

Icon button (List view).

Page copy: `library-dark`. Finder: `() => Q('button[aria-label="List view"]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed | selected |
|---|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Gap | 6px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | -apple-system-body 14px/14px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #cdcdcd | #ededed | = | #ededed | #ededed |
| Transition | opacity, color 0.15s ease | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 20 x 20, colour #cdcdcd, fill #000000 | 20 x 20, colour #ededed, fill #000000 | = | 20 x 20, colour #ededed, fill #000000 | 20 x 20, colour #ededed, fill #000000 |
| ::before | 36px x 36px, absolute, bg #ffffff @ 0.1, radius 9999px | = | = | 36px x 36px, absolute, bg #ededed @ 0.16, radius 9999px | = |
| ::after | 36px x 36px, absolute, bg #000000 @ 0, radius 9999px | = | = | = | = |
| Painted layers | button.Button-QTscM8::before 36pxx36px bg #ffffff @ 0.1 r 9999px opacity 0 | button.Button-QTscM8::before 36pxx36px bg #ffffff @ 0.1 r 9999px | button.Button-QTscM8::before 36pxx36px bg #ffffff @ 0.1 r 9999px opacity 0; button.Button-QTscM8::after 36pxx36px r 9999px outline 2px solid #3a83f7 offset -1px | button.Button-QTscM8::before 36pxx36px bg #ededed @ 0.16 r 9999px | button.Button-QTscM8::before 36pxx36px bg #ffffff @ 0.1 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) | at rest, captured selected |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed | light-selected |
|---|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Gap | 6px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | -apple-system-body 14px/14px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #5d5d5d | #0d0d0d | = | #0d0d0d | #0d0d0d |
| Transition | opacity, color 0.15s ease | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 20 x 20, colour #5d5d5d, fill #000000 | 20 x 20, colour #0d0d0d, fill #000000 | = | 20 x 20, colour #0d0d0d, fill #000000 | 20 x 20, colour #0d0d0d, fill #000000 |
| ::before | 36px x 36px, absolute, bg #000000 @ 0.05, radius 9999px | = | = | 36px x 36px, absolute, bg #0d0d0d @ 0.12, radius 9999px | = |
| ::after | 36px x 36px, absolute, bg #000000 @ 0, radius 9999px | = | = | = | = |
| Painted layers | button.Button-QTscM8::before 36pxx36px bg #000000 @ 0.05 r 9999px opacity 0 | button.Button-QTscM8::before 36pxx36px bg #000000 @ 0.05 r 9999px | button.Button-QTscM8::before 36pxx36px bg #000000 @ 0.05 r 9999px opacity 0; button.Button-QTscM8::after 36pxx36px r 9999px outline 2px solid #3a83f7 offset -1px | button.Button-QTscM8::before 36pxx36px bg #0d0d0d @ 0.12 r 9999px | button.Button-QTscM8::before 36pxx36px bg #000000 @ 0.05 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) | at rest, captured selected |

Other finders: selected: `() => Q('button[aria-label="Grid view"]')`; light-selected: `() => Q('button[aria-label="Grid view"]')`.

Crops: `library-icon-button-default.png`, `library-icon-button-hover.png`, `library-icon-button-focus-visible.png`, `library-icon-button-pressed.png`, `library-icon-button-selected.png`, `library-icon-button-light.png`, `library-icon-button-light-hover.png`, `library-icon-button-light-focus-visible.png`, `library-icon-button-light-pressed.png`, `library-icon-button-light-selected.png`.

#### library-search

Text field (Search library).

Page copy: `library-dark`. Finder: `() => P(Q('input[id^="library-search"]').parentElement)`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 240 x 36 | = | = |
| Padding | 0px 12px | = | = |
| Gap | 8px | = | = |
| Border | 1px solid #ffffff @ 0.2 | = | = |
| Radius | 9999px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ededed | = | = |
| Transition | none | = | = |
| Icon | 20 x 20, colour #cdcdcd, fill #000000 | = | = |
| Placeholder | "Search library" #afafaf, opacity 1, 14px | = | = |
| Painted layers | div.no-drag.flex.items-center 240.0x36.0 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 9999px | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 240 x 36 | = | = |
| Padding | 0px 12px | = | = |
| Gap | 8px | = | = |
| Border | 1px solid #000000 @ 0.15 | = | = |
| Radius | 9999px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0d0d0d | = | = |
| Transition | none | = | = |
| Icon | 20 x 20, colour #5d5d5d, fill #000000 | = | = |
| Placeholder | "Search library" #8f8f8f, opacity 1, 14px | = | = |
| Painted layers | div.no-drag.flex.items-center 240.0x36.0 border T:1px solid #000000 @ 0.15 / R:1px solid #000000 @ 0.15 / B:1px solid #000000 @ 0.15 / L:1px solid #000000 @ 0.15 r 9999px | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) |

Crops: `library-search-default.png`, `library-search-hover.png`, `library-search-focus-visible.png`, `library-search-light.png`, `library-search-light-hover.png`, `library-search-light-focus-visible.png`.

#### library-new

Inverted button (New).

Page copy: `library-dark`. Finder: `() => C(T('New', M()), 'button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 74.78 x 36 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #ffffff @ 0.15 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ededed | #ededed @ 0.8 | = | #ededed @ 0.8 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Text node | span: -apple-system-body 14px/18px 400, #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #0d0d0d, fill #000000 | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 74.8x36.0 bg #ededed border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px | button.no-drag.cursor-interaction.items-center 74.8x36.0 bg #ededed @ 0.8 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px | button.no-drag.cursor-interaction.items-center 74.8x36.0 bg #ededed border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 74.8x36.0 bg #ededed @ 0.8 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 74.78 x 36 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0.1 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #0d0d0d | #0d0d0d @ 0.8 | = | #0d0d0d @ 0.8 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: -apple-system-body 14px/18px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff, fill #000000 | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 74.8x36.0 bg #0d0d0d border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px | button.no-drag.cursor-interaction.items-center 74.8x36.0 bg #0d0d0d @ 0.8 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px | button.no-drag.cursor-interaction.items-center 74.8x36.0 bg #0d0d0d border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 74.8x36.0 bg #0d0d0d @ 0.8 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `library-new-default.png`, `library-new-hover.png`, `library-new-focus-visible.png`, `library-new-pressed.png`, `library-new-light.png`, `library-new-light-hover.png`, `library-new-light-focus-visible.png`, `library-new-light-pressed.png`.

#### library-tab

Tab (Library).

Page copy: `library-dark`. Finder: `() => Q('main [role=tab][aria-selected=false]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed | selected |
|---|---|---|---|---|---|
| Size (w x h) | 94.03 x 36 | = | = | = | 105.28 x 36 |
| Padding | 0px 16px | = | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | transparent | #ffffff @ 0.0509804 | = | #ffffff @ 0.0509804 | #ffffff @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = | = | = |
| Font | -apple-system-body 14px/20px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #cdcdcd | #ededed | = | #ededed | #ededed |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | button.cursor-interaction.items-center.text-sm 94.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.cursor-interaction.items-center.text-sm 94.0x36.0 bg #ffffff @ 0.0509804 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.cursor-interaction.items-center.text-sm 94.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | button.cursor-interaction.items-center.text-sm 94.0x36.0 bg #ffffff @ 0.0509804 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.cursor-interaction.items-center.text-sm 105.3x36.0 bg #ffffff @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover | keyboard: Shift keydown, then focus() | mouse button held down on it (:hover:active) | at rest, captured selected |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed | light-selected |
|---|---|---|---|---|---|
| Size (w x h) | 94.03 x 36 | = | = | = | 105.28 x 36 |
| Padding | 0px 16px | = | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | transparent | #000000 @ 0.0254902 | = | #000000 @ 0.0254902 | #000000 @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = | = | = |
| Font | -apple-system-body 14px/20px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #5d5d5d | #0d0d0d | = | #0d0d0d | #0d0d0d |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | button.cursor-interaction.items-center.text-sm 94.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.cursor-interaction.items-center.text-sm 94.0x36.0 bg #000000 @ 0.0254902 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.cursor-interaction.items-center.text-sm 94.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | button.cursor-interaction.items-center.text-sm 94.0x36.0 bg #000000 @ 0.0254902 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.cursor-interaction.items-center.text-sm 105.3x36.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover | keyboard: Shift keydown, then focus() | mouse button held down on it (:hover:active) | at rest, captured selected |

Other finders: selected: `() => Q('main [role=tab][aria-selected=true]')`; light-selected: `() => Q('main [role=tab][aria-selected=true]')`.

Crops: `library-tab-default.png`, `library-tab-hover.png`, `library-tab-focus-visible.png`, `library-tab-pressed.png`, `library-tab-selected.png`, `library-tab-light.png`, `library-tab-light-hover.png`, `library-tab-light-focus-visible.png`, `library-tab-light-pressed.png`, `library-tab-light-selected.png`.

#### library-card

Card (Library file). Masonry grid cards (5 columns at 1440): a thumbnail (blanked in the copies) over the file name.

Page copy: `library-dark`. Finder: `() => P(Q('[data-library-item] button'))`.

Dark theme.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 238.75 x 159.83 | = |
| Padding | 0px | = |
| Border | 1px solid #ffffff @ 0.05 | = |
| Radius | 16px | = |
| Background | #1b1b1b | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 4px 16px 0px | = |
| Outline | none | = |
| Font | -apple-system-body 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ededed | = |
| Transition | none | = |
| Icon | 20 x 20, colour #ffffff, fill #000000 | = |
| Painted layers | div.relative.overflow-hidden.rounded-2xl 238.8x159.8 bg #1b1b1b border T:1px solid #ffffff @ 0.05 / R:1px solid #ffffff @ 0.05 / B:1px solid #ffffff @ 0.05 / L:1px solid #ffffff @ 0.05 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 4px 16px 0px; span.pointer-events-none.absolute.inset-0 236.8x157.8 bg #ededed @ 0.05 opacity 0; button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #000000 @ 0.2 r 9999px; button.group.peer.shrink-0 20.0x20.0 bg #000000 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.13 0px 2px 4px -1px | div.relative.overflow-hidden.rounded-2xl 238.8x159.8 bg #1b1b1b border T:1px solid #ffffff @ 0.05 / R:1px solid #ffffff @ 0.05 / B:1px solid #ffffff @ 0.05 / L:1px solid #ffffff @ 0.05 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 4px 16px 0px; span.pointer-events-none.absolute.inset-0 236.8x157.8 bg #ededed @ 0.05; button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #000000 @ 0.2 r 9999px; button.group.peer.shrink-0 20.0x20.0 bg #000000 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.13 0px 2px 4px -1px |
| How | at rest | mouse hover on its row |

Light theme.

| Property | light | light-hover |
|---|---|---|
| Size (w x h) | 238.75 x 159.83 | = |
| Padding | 0px | = |
| Border | 1px solid #000000 @ 0.05 | = |
| Radius | 16px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 4px 16px 0px | = |
| Outline | none | = |
| Font | -apple-system-body 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0d0d0d | = |
| Transition | none | = |
| Icon | 20 x 20, colour #ffffff, fill #000000 | = |
| Painted layers | div.relative.overflow-hidden.rounded-2xl 238.8x159.8 bg #ffffff border T:1px solid #000000 @ 0.05 / R:1px solid #000000 @ 0.05 / B:1px solid #000000 @ 0.05 / L:1px solid #000000 @ 0.05 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 4px 16px 0px; span.pointer-events-none.absolute.inset-0 236.8x157.8 bg #0d0d0d @ 0.02 opacity 0; button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #000000 @ 0.2 r 9999px; button.group.peer.shrink-0 20.0x20.0 bg #fcfcfc border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.13 0px 2px 4px -1px | div.relative.overflow-hidden.rounded-2xl 238.8x159.8 bg #ffffff border T:1px solid #000000 @ 0.05 / R:1px solid #000000 @ 0.05 / B:1px solid #000000 @ 0.05 / L:1px solid #000000 @ 0.05 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 4px 16px 0px; span.pointer-events-none.absolute.inset-0 236.8x157.8 bg #0d0d0d @ 0.02; button.no-drag.cursor-interaction.items-center 36.0x36.0 bg #000000 @ 0.2 r 9999px; button.group.peer.shrink-0 20.0x20.0 bg #fcfcfc border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.13 0px 2px 4px -1px |
| How | at rest | mouse hover on its row |

Crops: `library-card-default.png`, `library-card-hover.png`, `library-card-light.png`, `library-card-light-hover.png`.

#### checkbox

Checkbox (select a file). A 20x20 `role=checkbox` button on each card, shown on hover.

Page copy: `library-dark`. Finder: `() => QA('[data-library-item] [role=checkbox]')`.

Dark theme.

| Property | hover | focus-visible |
|---|---|---|
| Size (w x h) | 20 x 20 | = |
| Padding | 0px | = |
| Border | 1px solid #ffffff @ 0.15 | 1px solid #3a83f7 |
| Radius | 4px | = |
| Background | #000000 | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.13 0px 2px 4px -1px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0.13 0px 2px 4px -1px |
| Outline | none | = |
| Font | -apple-system-body 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ededed | = |
| Transition | background-color, border-color, box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.group.peer.shrink-0 20.0x20.0 bg #000000 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.13 0px 2px 4px -1px | button.group.peer.shrink-0 20.0x20.0 bg #000000 border T:1px solid #3a83f7 / R:1px solid #3a83f7 / B:1px solid #3a83f7 / L:1px solid #3a83f7 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0.13 0px 2px 4px -1px |
| Ancestor paint | 3 up div.relative.overflow-hidden.rounded-2xl bg #1b1b1b shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 4px 16px 0px | = |
| How | mouse hover on its row | keyboard: focus(), Shift+Tab, Tab |

Light theme.

| Property | light-hover | light-focus-visible |
|---|---|---|
| Size (w x h) | 20 x 20 | = |
| Padding | 0px | = |
| Border | 1px solid #000000 @ 0.1 | 1px solid #3a83f7 |
| Radius | 4px | = |
| Background | #fcfcfc | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.13 0px 2px 4px -1px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0.13 0px 2px 4px -1px |
| Outline | none | = |
| Font | -apple-system-body 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0d0d0d | = |
| Transition | background-color, border-color, box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.group.peer.shrink-0 20.0x20.0 bg #fcfcfc border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.13 0px 2px 4px -1px | button.group.peer.shrink-0 20.0x20.0 bg #fcfcfc border T:1px solid #3a83f7 / R:1px solid #3a83f7 / B:1px solid #3a83f7 / L:1px solid #3a83f7 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0.13 0px 2px 4px -1px |
| Ancestor paint | 3 up div.relative.overflow-hidden.rounded-2xl bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 4px 16px 0px | = |
| How | mouse hover on its row | keyboard: focus(), Shift+Tab, Tab |

Crops: `checkbox-hover.png`, `checkbox-focus-visible.png`, `checkbox-light-hover.png`, `checkbox-light-focus-visible.png`.

#### library-error

Error state (Failed to load files). Shown when the file list request fails (the capture guard refused it); a centred line and a Try again button.

Page copy: `library-dark-error`. Finder: `() => B('Try again') && B('Try again').parentElement`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 1003 x 160 |
| Padding | 48px 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Transition | none |
| Painted layers | button.no-drag.cursor-interaction.items-center 77.0x24.0 bg #ededed border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 1003 x 160 |
| Padding | 48px 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Transition | none |
| Painted layers | button.no-drag.cursor-interaction.items-center 77.0x24.0 bg #0d0d0d border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px |
| How | at rest |

Crops: `library-error-default.png`, `library-error-light.png`.

#### retry-button

Small button (Try again).

Page copy: `library-dark-error`. Finder: `() => B('Try again')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 77.05 x 24 | = | = | = |
| Padding | 2px 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #ffffff @ 0.15 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ededed | #ededed @ 0.8 | = | #ededed @ 0.8 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 77.0x24.0 bg #ededed border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px | button.no-drag.cursor-interaction.items-center 77.0x24.0 bg #ededed @ 0.8 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px | button.no-drag.cursor-interaction.items-center 77.0x24.0 bg #ededed border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 77.0x24.0 bg #ededed @ 0.8 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 77.05 x 24 | = | = | = |
| Padding | 2px 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0.1 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #0d0d0d | #0d0d0d @ 0.8 | = | #0d0d0d @ 0.8 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 77.0x24.0 bg #0d0d0d border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px | button.no-drag.cursor-interaction.items-center 77.0x24.0 bg #0d0d0d @ 0.8 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px | button.no-drag.cursor-interaction.items-center 77.0x24.0 bg #0d0d0d border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 77.0x24.0 bg #0d0d0d @ 0.8 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `retry-button-default.png`, `retry-button-hover.png`, `retry-button-focus-visible.png`, `retry-button-pressed.png`, `retry-button-light.png`, `retry-button-light-hover.png`, `retry-button-light-focus-visible.png`, `retry-button-light-pressed.png`.

#### inline-error

Inline error (partial search results).

Page copy: `library-dark-search-error`. Finder: `() => W(TS('Some search results'), 300)`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 1003 x 56 |
| Padding | 16px 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Transition | none |
| Painted layers | button.no-drag.cursor-interaction.items-center 77.0x24.0 bg #ededed border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 1003 x 56 |
| Padding | 16px 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Transition | none |
| Painted layers | button.no-drag.cursor-interaction.items-center 77.0x24.0 bg #0d0d0d border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px |
| How | at rest |

Crops: `inline-error-default.png`, `inline-error-light.png`.

#### library-loading

Loading placeholder (file card shimmer). While the file list loads, the grid holds shimmer cards of the file card's size (the capture guard held the request open). The shimmer is animated in the product; the copy has no scripts, so it shows one frame.

Page copy: `library-dark-loading`. Finder: `() => Q('[class*="LoadingResultsShimmer"]').parentElement`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 238.75 x 198.95 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Transition | none |
| Painted layers | div.LoadingResultsShimmer-IzeCFB::before 716.25pxx198.953px image linear-gradient(90deg, #afafaf @ 0.1, #afafaf @ 0.16, #afafaf @ 0.1) |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 238.75 x 198.95 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Transition | none |
| Painted layers | div.LoadingResultsShimmer-IzeCFB::before 716.25pxx198.953px image linear-gradient(90deg, #8f8f8f @ 0.1, #8f8f8f @ 0.16, #8f8f8f @ 0.1) |
| How | at rest |

Crops: `library-loading-default.png`, `library-loading-light.png`.

### Images

#### images-tab

Tab (Images).

Page copy: `images-dark`. Finder: `() => Q('main [role=tab][aria-selected=false]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed | selected |
|---|---|---|---|---|---|
| Size (w x h) | 102.16 x 36 | = | = | = | 92.25 x 36 |
| Padding | 0px 16px | = | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | transparent | #ffffff @ 0.0509804 | = | #ffffff @ 0.0509804 | #ffffff @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = | = | = |
| Font | -apple-system-body 14px/20px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #cdcdcd | #ededed | = | #ededed | #ededed |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | button.cursor-interaction.items-center.text-sm 102.2x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.cursor-interaction.items-center.text-sm 102.2x36.0 bg #ffffff @ 0.0509804 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.cursor-interaction.items-center.text-sm 102.2x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | button.cursor-interaction.items-center.text-sm 102.2x36.0 bg #ffffff @ 0.0509804 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.cursor-interaction.items-center.text-sm 92.3x36.0 bg #ffffff @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover | keyboard: Shift keydown, then focus() | mouse button held down on it (:hover:active) | at rest, captured selected |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed | light-selected |
|---|---|---|---|---|---|
| Size (w x h) | 102.16 x 36 | = | = | = | 92.25 x 36 |
| Padding | 0px 16px | = | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | transparent | #000000 @ 0.0254902 | = | #000000 @ 0.0254902 | #000000 @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = | = | = |
| Font | -apple-system-body 14px/20px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #5d5d5d | #0d0d0d | = | #0d0d0d | #0d0d0d |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | button.cursor-interaction.items-center.text-sm 102.2x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.cursor-interaction.items-center.text-sm 102.2x36.0 bg #000000 @ 0.0254902 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.cursor-interaction.items-center.text-sm 102.2x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | button.cursor-interaction.items-center.text-sm 102.2x36.0 bg #000000 @ 0.0254902 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.cursor-interaction.items-center.text-sm 92.3x36.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover | keyboard: Shift keydown, then focus() | mouse button held down on it (:hover:active) | at rest, captured selected |

Other finders: selected: `() => Q('main [role=tab][aria-selected=true]')`; light-selected: `() => Q('main [role=tab][aria-selected=true]')`.

Crops: `images-tab-default.png`, `images-tab-hover.png`, `images-tab-focus-visible.png`, `images-tab-pressed.png`, `images-tab-selected.png`, `images-tab-light.png`, `images-tab-light-hover.png`, `images-tab-light-focus-visible.png`, `images-tab-light-pressed.png`, `images-tab-light-selected.png`.

#### image-card

Card (image template).

Page copy: `images-dark`. Finder: `() => P(Q('main img').parentElement) // W(Q('main img'), 100)`.

Dark theme.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 139.19 x 173.98 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | #000000 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system-body 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ededed | = |
| Text node | span.line-clamp-2.w-full.text-start: -apple-system-body 14px/20px 500, #ffffff | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | button.group/use.relative.flex 139.2x174.0 bg #000000 r 16px; div.pointer-events-none.absolute.inset-x-0 139.2x61.0 image linear-gradient(to top, #000000 @ 0.8 0%, #000000 @ 0.3 50%, #000000 @ 0 100%) | = |
| How | at rest | mouse hover |

Light theme.

| Property | light | light-hover |
|---|---|---|
| Size (w x h) | 139.19 x 173.98 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | #fcfcfc | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system-body 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0d0d0d | = |
| Text node | span.line-clamp-2.w-full.text-start: -apple-system-body 14px/20px 500, #ffffff | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | button.group/use.relative.flex 139.2x174.0 bg #fcfcfc r 16px; div.pointer-events-none.absolute.inset-x-0 139.2x61.0 image linear-gradient(to top, #000000 @ 0.8 0%, #000000 @ 0.3 50%, #000000 @ 0 100%) | = |
| How | at rest | mouse hover |

Crops: `image-card-default.png`, `image-card-hover.png`, `image-card-light.png`, `image-card-light-hover.png`.

### Plugins

#### plugins-search

Text field (Search plugins).

Page copy: `plugins-dark`. Finder: `() => P(Q('#plugins-store-page-search').parentElement)`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 920 x 44 | = | = |
| Padding | 0px 10px | = | = |
| Gap | 8px | = | = |
| Border | 1px solid #ffffff @ 0.2 | = | = |
| Radius | 9999px | = | = |
| Background | #1b1b1b | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 16px/18px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ededed | = | = |
| Transition | none | = | = |
| Icon | 18 x 18, colour #cdcdcd | = | = |
| Placeholder | "Search plugins" #afafaf, opacity 1, 16px | = | = |
| Painted layers | div.no-drag.flex.items-center 920.0x44.0 bg #1b1b1b border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 9999px | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 920 x 44 | = | = |
| Padding | 0px 10px | = | = |
| Gap | 8px | = | = |
| Border | 1px solid #000000 @ 0.15 | = | = |
| Radius | 9999px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 16px/18px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0d0d0d | = | = |
| Transition | none | = | = |
| Icon | 18 x 18, colour #5d5d5d | = | = |
| Placeholder | "Search plugins" #8f8f8f, opacity 1, 16px | = | = |
| Painted layers | div.no-drag.flex.items-center 920.0x44.0 bg #ffffff border T:1px solid #000000 @ 0.15 / R:1px solid #000000 @ 0.15 / B:1px solid #000000 @ 0.15 / L:1px solid #000000 @ 0.15 r 9999px | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) |

Crops: `plugins-search-default.png`, `plugins-search-hover.png`, `plugins-search-focus-visible.png`, `plugins-search-light.png`, `plugins-search-light-hover.png`, `plugins-search-light-focus-visible.png`.

#### plugins-tab

Tab (Plugins / Skills).

Page copy: `plugins-dark`. Finder: `() => Q('[role=tab][aria-selected=false]')`.

Dark theme.

| Property | default | hover | focus-visible | selected |
|---|---|---|---|---|
| Size (w x h) | 68.73 x 36 | = | = | 82.39 x 36 |
| Padding | 0px 16px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #ffffff @ 0.0509804 | = | #ffffff @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #cdcdcd | #ededed | = | #ededed |
| Text node | span.inline-flex.items-center.gap-1: -apple-system-body 14px/20px 500, #cdcdcd | span.inline-flex.items-center.gap-1: -apple-system-body 14px/20px 500, #ededed | = | - |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.cursor-interaction.items-center.text-sm 68.7x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.cursor-interaction.items-center.text-sm 68.7x36.0 bg #ffffff @ 0.0509804 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.cursor-interaction.items-center.text-sm 68.7x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | button.cursor-interaction.items-center.text-sm 82.4x36.0 bg #ffffff @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover | keyboard: Shift keydown, then focus() | at rest, captured selected |

Light theme.

| Property | light | light-hover | light-focus-visible | light-selected |
|---|---|---|---|---|
| Size (w x h) | 68.73 x 36 | = | = | 82.39 x 36 |
| Padding | 0px 16px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #000000 @ 0.0254902 | = | #000000 @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #5d5d5d | #0d0d0d | = | #0d0d0d |
| Text node | span.inline-flex.items-center.gap-1: -apple-system-body 14px/20px 500, #5d5d5d | span.inline-flex.items-center.gap-1: -apple-system-body 14px/20px 500, #0d0d0d | = | - |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.cursor-interaction.items-center.text-sm 68.7x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.cursor-interaction.items-center.text-sm 68.7x36.0 bg #000000 @ 0.0254902 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.cursor-interaction.items-center.text-sm 68.7x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | button.cursor-interaction.items-center.text-sm 82.4x36.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover | keyboard: Shift keydown, then focus() | at rest, captured selected |

Other finders: selected: `() => Q('[role=tab][aria-selected=true]')`; light-selected: `() => Q('[role=tab][aria-selected=true]')`.

Crops: `plugins-tab-default.png`, `plugins-tab-hover.png`, `plugins-tab-focus-visible.png`, `plugins-tab-selected.png`, `plugins-tab-light.png`, `plugins-tab-light-hover.png`, `plugins-tab-light-focus-visible.png`, `plugins-tab-light-selected.png`.

#### plugin-row

List row (plugin card). A bordered card with a link laid over the whole of it; hover fills the card, keyboard focus rings the link (see the next row).

Page copy: `plugins-dark`. Finder: `() => CK(T('Gmail'), 'rounded-2xl border p-2')`.

Dark theme.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 448 x 64.75 | = | = |
| Padding | 8px | = | = |
| Gap | 10px | = | = |
| Border | none | = | = |
| Radius | 16px | = | = |
| Background | transparent | #ededed @ 0.05 | #ededed @ 0.05 |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ededed | = | = |
| Text node | span.truncate: -apple-system-body 16px/24px 500, #ededed | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 18 x 18, colour #afafaf | = | = |
| Painted layers | span.flex.size-9.shrink-0 36.0x36.0 bg #000000 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 8px | div.flex.flex-col.gap-2.5 448.0x64.8 bg #ededed @ 0.05 r 16px; span.flex.size-9.shrink-0 36.0x36.0 bg #000000 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 8px | div.flex.flex-col.gap-2.5 448.0x64.8 bg #ededed @ 0.05 r 16px; span.flex.size-9.shrink-0 36.0x36.0 bg #000000 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 8px |
| How | at rest | mouse hover | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-pressed |
|---|---|---|---|
| Size (w x h) | 448 x 64.75 | = | = |
| Padding | 8px | = | = |
| Gap | 10px | = | = |
| Border | none | = | = |
| Radius | 16px | = | = |
| Background | transparent | #0d0d0d @ 0.05 | #0d0d0d @ 0.05 |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0d0d0d | = | = |
| Text node | span.truncate: -apple-system-body 16px/24px 500, #0d0d0d | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 18 x 18, colour #8f8f8f | = | = |
| Painted layers | span.flex.size-9.shrink-0 36.0x36.0 bg #fcfcfc border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 8px | div.flex.flex-col.gap-2.5 448.0x64.8 bg #0d0d0d @ 0.05 r 16px; span.flex.size-9.shrink-0 36.0x36.0 bg #fcfcfc border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 8px | div.flex.flex-col.gap-2.5 448.0x64.8 bg #0d0d0d @ 0.05 r 16px; span.flex.size-9.shrink-0 36.0x36.0 bg #fcfcfc border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 8px |
| How | at rest | mouse hover | mouse button held down on it (:hover:active) |

Crops: `plugin-row-default.png`, `plugin-row-hover.png`, `plugin-row-pressed.png`, `plugin-row-light.png`, `plugin-row-light-hover.png`, `plugin-row-light-pressed.png`.

#### plugin-row-link

List row link (plugin card, focus ring).

Page copy: `plugins-dark`. Finder: `() => { const c = CK(T('Gmail'), 'rounded-2xl border p-2'); return c && c.querySelector('a'); }`.

Dark theme.

| Property | focus-visible |
|---|---|
| Size (w x h) | 448 x 64.75 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | transparent |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Transition | none |
| Cursor | pointer |
| Painted layers | a.absolute.inset-0.cursor-interaction 448.0x64.8 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px |
| How | keyboard: focus(), Shift+Tab, Tab |

Light theme.

| Property | light-focus-visible |
|---|---|
| Size (w x h) | 448 x 64.75 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | transparent |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Transition | none |
| Cursor | pointer |
| Painted layers | a.absolute.inset-0.cursor-interaction 448.0x64.8 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px inset, #3a83f7 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px |
| How | keyboard: focus(), Shift+Tab, Tab |

Crops: `plugin-row-link-focus-visible.png`, `plugin-row-link-light-focus-visible.png`.

### Settings

#### settings-nav-item

Settings nav item.

Page copy: `settings-dark-appearance`. Finder: `() => C(T('General'), 'a,button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed | selected |
|---|---|---|---|---|---|
| Size (w x h) | 328 x 35 | = | = | = | = |
| Padding | 6px 10px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 8px | = | = | = | = |
| Background | transparent | #ffffff @ 0.1 | = | #ffffff @ 0.1 | #ffffff @ 0.1 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #3a83f7 offset -2px | = | = |
| Font | -apple-system-body 14px/20px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ededed | = | = | = | = |
| Text node | span.text-fade-truncate: -apple-system-body 14px/20px 400, #ededed | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 20 x 20, colour #ededed, fill #000000 | = | = | = | = |
| Tokens | --height-token-row 36px; --icon-leading-size calc(.25rem * 5); --nav-item-height calc(36px - 1px); --padding-row-cell-x 10px; --padding-row-x 6px; --spacing-nav-row-content calc(.25rem * 1.5) | = | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) | at rest, captured selected |
| Painted layers | - | button.sidebar-item.relative.shrink-0 328.0x35.0 bg #ffffff @ 0.1 r 8px | button.sidebar-item.relative.shrink-0 328.0x35.0 r 8px outline 2px solid #3a83f7 offset -2px | button.sidebar-item.relative.shrink-0 328.0x35.0 bg #ffffff @ 0.1 r 8px | button.sidebar-item.relative.shrink-0 328.0x35.0 bg #ffffff @ 0.1 r 8px |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed | light-selected |
|---|---|---|---|---|---|
| Size (w x h) | 328 x 35 | = | = | = | = |
| Padding | 6px 10px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 8px | = | = | = | = |
| Background | transparent | #000000 @ 0.05 | = | #000000 @ 0.05 | #000000 @ 0.05 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #3a83f7 offset -2px | = | = |
| Font | -apple-system-body 14px/20px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #0d0d0d | = | = | = | = |
| Text node | span.text-fade-truncate: -apple-system-body 14px/20px 400, #0d0d0d | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 20 x 20, colour #0d0d0d, fill #000000 | = | = | = | = |
| Tokens | --height-token-row 36px; --icon-leading-size calc(.25rem * 5); --nav-item-height calc(36px - 1px); --padding-row-cell-x 10px; --padding-row-x 6px; --spacing-nav-row-content calc(.25rem * 1.5) | = | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) | at rest, captured selected |
| Painted layers | - | button.sidebar-item.relative.shrink-0 328.0x35.0 bg #000000 @ 0.05 r 8px | button.sidebar-item.relative.shrink-0 328.0x35.0 r 8px outline 2px solid #3a83f7 offset -2px | button.sidebar-item.relative.shrink-0 328.0x35.0 bg #000000 @ 0.05 r 8px | button.sidebar-item.relative.shrink-0 328.0x35.0 bg #000000 @ 0.05 r 8px |

Other finders: selected: `() => C(T('Appearance', Q('nav') // document), 'a,button')`; light-selected: `() => C(T('Appearance', Q('nav') // document), 'a,button')`.

Crops: `settings-nav-item-default.png`, `settings-nav-item-hover.png`, `settings-nav-item-focus-visible.png`, `settings-nav-item-pressed.png`, `settings-nav-item-selected.png`, `settings-nav-item-light.png`, `settings-nav-item-light-hover.png`, `settings-nav-item-light-focus-visible.png`, `settings-nav-item-light-pressed.png`, `settings-nav-item-light-selected.png`.

#### settings-row

Settings row.

Page copy: `settings-dark-data-controls`. Finder: `() => H(T('Archive all chats'), 56)`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 766 x 60 |
| Padding | 12px 16px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | div.min-w-0.break-words.text-default: -apple-system-body 14px/20px 500, #ededed |
| Transition | none |
| ::after | 734px x 1px, absolute, bg #ffffff @ 0.15, radius 0px |
| Painted layers | div.@container/settings-row.px-4.items-center::after 734pxx1px bg #ffffff @ 0.15; button.no-drag.cursor-interaction.items-center 92.5x36.0 bg #ededed @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| Ancestor paint | 1 up div.flex.flex-col.rounded-2xl bg #000000 |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 766 x 60 |
| Padding | 12px 16px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | div.min-w-0.break-words.text-default: -apple-system-body 14px/20px 500, #0d0d0d |
| Transition | none |
| ::after | 734px x 1px, absolute, bg #000000 @ 0.1, radius 0px |
| Painted layers | div.@container/settings-row.px-4.items-center::after 734pxx1px bg #000000 @ 0.1; button.no-drag.cursor-interaction.items-center 92.5x36.0 bg #0d0d0d @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| Ancestor paint | 1 up div.flex.flex-col.rounded-2xl bg #fcfcfc |
| How | at rest |

Crops: `settings-row-default.png`, `settings-row-light.png`.

#### switch-on

Switch (on).

Page copy: `settings-dark-data-controls`. Finder: `() => Q('[role=switch][aria-checked=true]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 9999px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ededed | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.relative.inline-flex.shrink-0 32.0x20.0 bg #3a83f7 r 9999px; span.rounded-full.border.shadow-sm 16.0x16.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 1px 2px -1px | = | button.inline-flex.items-center.text-sm 32.0x20.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.relative.inline-flex.shrink-0 32.0x20.0 bg #3a83f7 r 9999px; span.rounded-full.border.shadow-sm 16.0x16.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 1px 2px -1px | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 9999px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.relative.inline-flex.shrink-0 32.0x20.0 bg #3a83f7 r 9999px; span.rounded-full.border.shadow-sm 16.0x16.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 1px 2px -1px | = | button.inline-flex.items-center.text-sm 32.0x20.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.relative.inline-flex.shrink-0 32.0x20.0 bg #3a83f7 r 9999px; span.rounded-full.border.shadow-sm 16.0x16.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 1px 2px -1px | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `switch-on-default.png`, `switch-on-hover.png`, `switch-on-focus-visible.png`, `switch-on-pressed.png`, `switch-on-light.png`, `switch-on-light-hover.png`, `switch-on-light-focus-visible.png`, `switch-on-light-pressed.png`.

#### switch-off

Switch (off).

Page copy: `settings-dark-data-controls`. Finder: `() => Q('[role=switch][aria-checked=false]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 9999px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ededed | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.relative.inline-flex.shrink-0 32.0x20.0 bg #ededed @ 0.1 r 9999px; span.rounded-full.border.shadow-sm 16.0x16.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 1px 2px -1px | = | button.inline-flex.items-center.text-sm 32.0x20.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.relative.inline-flex.shrink-0 32.0x20.0 bg #ededed @ 0.1 r 9999px; span.rounded-full.border.shadow-sm 16.0x16.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 1px 2px -1px | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 9999px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.relative.inline-flex.shrink-0 32.0x20.0 bg #0d0d0d @ 0.1 r 9999px; span.rounded-full.border.shadow-sm 16.0x16.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 1px 2px -1px | = | button.inline-flex.items-center.text-sm 32.0x20.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.relative.inline-flex.shrink-0 32.0x20.0 bg #0d0d0d @ 0.1 r 9999px; span.rounded-full.border.shadow-sm 16.0x16.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 1px 2px -1px | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `switch-off-default.png`, `switch-off-hover.png`, `switch-off-focus-visible.png`, `switch-off-pressed.png`, `switch-off-light.png`, `switch-off-light-hover.png`, `switch-off-light-focus-visible.png`, `switch-off-light-pressed.png`.

#### button-outline

Outline button (Archive all).

Page copy: `settings-dark-data-controls`. Finder: `() => B('Archive all')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 92.5 x 36 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ededed @ 0.05 | #ededed @ 0.1 | = | #ededed @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ededed | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 92.5x36.0 bg #ededed @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 92.5x36.0 bg #ededed @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 92.5x36.0 bg #ededed @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 92.5x36.0 bg #ededed @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 92.5 x 36 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #0d0d0d @ 0.05 | #0d0d0d @ 0.1 | = | #0d0d0d @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 92.5x36.0 bg #0d0d0d @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 92.5x36.0 bg #0d0d0d @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 92.5x36.0 bg #0d0d0d @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 92.5x36.0 bg #0d0d0d @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `button-outline-default.png`, `button-outline-hover.png`, `button-outline-focus-visible.png`, `button-outline-pressed.png`, `button-outline-light.png`, `button-outline-light-hover.png`, `button-outline-light-focus-visible.png`, `button-outline-light-pressed.png`.

#### button-danger-outline

Danger outline button (Delete all).

Page copy: `settings-dark-data-controls`. Finder: `() => B('Delete all')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.94 x 36 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ff6764 @ 0.1 | #ff6764 @ 0.2 | = | #ff6764 @ 0.2 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ff6764 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 85.9x36.0 bg #ff6764 @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 85.9x36.0 bg #ff6764 @ 0.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 85.9x36.0 bg #ff6764 @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 85.9x36.0 bg #ff6764 @ 0.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 85.94 x 36 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #e02e2a @ 0.1 | #e02e2a @ 0.2 | = | #e02e2a @ 0.2 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #e02e2a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 85.9x36.0 bg #e02e2a @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 85.9x36.0 bg #e02e2a @ 0.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 85.9x36.0 bg #e02e2a @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 85.9x36.0 bg #e02e2a @ 0.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `button-danger-outline-default.png`, `button-danger-outline-hover.png`, `button-danger-outline-focus-visible.png`, `button-danger-outline-pressed.png`, `button-danger-outline-light.png`, `button-danger-outline-light-hover.png`, `button-danger-outline-light-focus-visible.png`, `button-danger-outline-light-pressed.png`.

#### button-disabled

Button (disabled, Restore defaults).

Page copy: `settings-dark-keyboard`. Finder: `() => B('Restore defaults')`.

Dark theme.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 142.05 x 36 | = |
| Padding | 0px 16px | = |
| Gap | 4px | = |
| Border | 1px solid #ffffff @ 0.15 | = |
| Radius | 9999px | = |
| Background | #ededed | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system-body 14px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #0d0d0d | = |
| Transition | none | = |
| Opacity | 0.4 | = |
| Cursor | default | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 142.0x36.0 bg #ededed border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px opacity 0.4 | = |
| Ancestor paint | 1 up div.flex.flex-wrap.items-center bg #000000 | = |
| How | at rest | mouse hover |

Light theme.

| Property | light | light-hover |
|---|---|---|
| Size (w x h) | 142.05 x 36 | = |
| Padding | 0px 16px | = |
| Gap | 4px | = |
| Border | 1px solid #000000 @ 0.1 | = |
| Radius | 9999px | = |
| Background | #0d0d0d | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system-body 14px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | none | = |
| Opacity | 0.4 | = |
| Cursor | default | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 142.0x36.0 bg #0d0d0d border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px opacity 0.4 | = |
| Ancestor paint | 1 up div.flex.flex-wrap.items-center bg #fcfcfc | = |
| How | at rest | mouse hover |

Crops: `button-disabled-default.png`, `button-disabled-hover.png`, `button-disabled-light.png`, `button-disabled-light-hover.png`.

#### keyboard-switch

Switch (keyboard shortcut on).

Page copy: `settings-dark-keyboard`. Finder: `() => Q('[role=switch]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 32 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 14px/20px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Transition | none |
| Cursor | pointer |
| Painted layers | span.relative.inline-flex.shrink-0 32.0x20.0 bg #3a83f7 r 9999px; span.rounded-full.border.shadow-sm 16.0x16.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 1px 2px -1px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 32 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 14px/20px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Transition | none |
| Cursor | pointer |
| Painted layers | span.relative.inline-flex.shrink-0 32.0x20.0 bg #3a83f7 r 9999px; span.rounded-full.border.shadow-sm 16.0x16.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 1px 2px -1px |
| How | at rest |

Crops: `keyboard-switch-default.png`, `keyboard-switch-light.png`.

#### select

Select (notification channel).

Page copy: `settings-dark-notifications-menu`. Finder: `() => Q('main button[aria-haspopup=menu]', 1)`.

Dark theme.

| Property | default | hover | focus-visible | pressed | open |
|---|---|---|---|---|---|
| Size (w x h) | 78.03 x 36 | = | = | = | = |
| Padding | 0px 12px | = | = | = | = |
| Gap | 4px | = | = | = | = |
| Border | 1px solid #ffffff @ 0.15 | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | #303030 | = | = | = | #ffffff @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ededed | = | = | = | = |
| Text node | span.truncate: -apple-system-body 14px/18px 400, #ededed | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 16 x 16, colour #afafaf | = | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 78.0x36.0 bg #303030 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px | = | button.no-drag.cursor-interaction.items-center 78.0x36.0 bg #303030 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = | button.no-drag.cursor-interaction.items-center 78.0x36.0 bg #ffffff @ 0.1 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) | at rest, captured open |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed | light-open |
|---|---|---|---|---|---|
| Size (w x h) | 78.03 x 36 | = | = | = | = |
| Padding | 0px 12px | = | = | = | = |
| Gap | 4px | = | = | = | = |
| Border | 1px solid #000000 @ 0.1 | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | #f3f3f3 | = | = | = | #000000 @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #0d0d0d | = | = | = | = |
| Text node | span.truncate: -apple-system-body 14px/18px 400, #0d0d0d | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 16 x 16, colour #8f8f8f | = | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 78.0x36.0 bg #f3f3f3 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px | = | button.no-drag.cursor-interaction.items-center 78.0x36.0 bg #f3f3f3 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = | button.no-drag.cursor-interaction.items-center 78.0x36.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) | at rest, captured open |

Other finders: open: `() => Q('main button[aria-expanded=true]')`; light-open: `() => Q('main button[aria-expanded=true]')`.

Crops: `select-default.png`, `select-hover.png`, `select-focus-visible.png`, `select-pressed.png`, `select-open.png`, `select-light.png`, `select-light-hover.png`, `select-light-focus-visible.png`, `select-light-pressed.png`, `select-light-open.png`.

#### code-theme-select

Select (code theme).

Page copy: `settings-dark-appearance`. Finder: `() => Q('button[aria-label="Dark code theme"]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 176 x 36 | = | = | = |
| Padding | 0px 12px 0px 7px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #ffffff @ 0.15 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #000000 | #ffffff @ 0.1 | = | #ffffff @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ededed | = | = | = |
| Text node | span.flex.shrink-0.items-center: -apple-system-body 12px/12px 600, #3a83f7 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #afafaf | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 176.0x36.0 bg #000000 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px; span.flex.shrink-0.items-center 20.0x20.0 bg #000000 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 9999px | button.no-drag.cursor-interaction.items-center 176.0x36.0 bg #ffffff @ 0.1 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px; span.flex.shrink-0.items-center 20.0x20.0 bg #000000 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 9999px | button.no-drag.cursor-interaction.items-center 176.0x36.0 bg #000000 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.flex.shrink-0.items-center 20.0x20.0 bg #000000 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 9999px | button.no-drag.cursor-interaction.items-center 176.0x36.0 bg #ffffff @ 0.1 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px; span.flex.shrink-0.items-center 20.0x20.0 bg #000000 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 9999px |
| Tokens | --spacing .25rem; --spacing-token-button-composer calc(.25rem * 9) | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 176 x 36 | = | = | = |
| Padding | 0px 12px 0px 7px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0.1 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #fcfcfc | #000000 @ 0.05 | = | #000000 @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Text node | span.flex.shrink-0.items-center: -apple-system-body 12px/12px 600, #3a83f7 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #8f8f8f | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 176.0x36.0 bg #fcfcfc border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px; span.flex.shrink-0.items-center 20.0x20.0 bg #000000 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 9999px | button.no-drag.cursor-interaction.items-center 176.0x36.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px; span.flex.shrink-0.items-center 20.0x20.0 bg #000000 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 9999px | button.no-drag.cursor-interaction.items-center 176.0x36.0 bg #fcfcfc border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.flex.shrink-0.items-center 20.0x20.0 bg #000000 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 9999px | button.no-drag.cursor-interaction.items-center 176.0x36.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px; span.flex.shrink-0.items-center 20.0x20.0 bg #000000 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 9999px |
| Tokens | --spacing .25rem; --spacing-token-button-composer calc(.25rem * 9) | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `code-theme-select-default.png`, `code-theme-select-hover.png`, `code-theme-select-focus-visible.png`, `code-theme-select-pressed.png`, `code-theme-select-light.png`, `code-theme-select-light-hover.png`, `code-theme-select-light-focus-visible.png`, `code-theme-select-light-pressed.png`.

#### color-field

Text field (colour hex).

Page copy: `settings-dark-appearance`. Finder: `() => Q('input[aria-label="Dark background color"]')`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 56 x 16 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 12px/16px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ededed | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | "" #ededed, opacity 1, 12px | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |
| Ancestor paint | - | = | 1 up div.relative.flex.h-7 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 56 x 16 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 12px/16px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0d0d0d | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | "" #0d0d0d, opacity 1, 12px | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab |
| Ancestor paint | - | = | 1 up div.relative.flex.h-7 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |

Crops: `color-field-default.png`, `color-field-hover.png`, `color-field-focus-visible.png`, `color-field-light.png`, `color-field-light-hover.png`, `color-field-light-focus-visible.png`.

#### archived-search

Text field (Search archived chats).

Page copy: `settings-dark-archived`. Finder: `() => P(Q('#archived-tasks-search').parentElement)`.

Dark theme.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 432 x 44 | = | = |
| Padding | 0px 10px | = | = |
| Gap | 8px | = | = |
| Border | 1px solid #ffffff @ 0.2 | = | = |
| Radius | 9999px | = | = |
| Background | #1b1b1b | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 16px/18px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ededed | = | = |
| Transition | none | = | = |
| Icon | 18 x 18, colour #cdcdcd | = | = |
| Placeholder | "Search archived chats" #afafaf, opacity 1, 16px | = | = |
| Painted layers | div.no-drag.flex.items-center 432.0x44.0 bg #1b1b1b border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 9999px | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) |

Light theme.

| Property | light | light-hover | light-focus-visible |
|---|---|---|---|
| Size (w x h) | 432 x 44 | = | = |
| Padding | 0px 10px | = | = |
| Gap | 8px | = | = |
| Border | 1px solid #000000 @ 0.15 | = | = |
| Radius | 9999px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system-body 16px/18px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0d0d0d | = | = |
| Transition | none | = | = |
| Icon | 18 x 18, colour #5d5d5d | = | = |
| Placeholder | "Search archived chats" #8f8f8f, opacity 1, 16px | = | = |
| Painted layers | div.no-drag.flex.items-center 432.0x44.0 bg #ffffff border T:1px solid #000000 @ 0.15 / R:1px solid #000000 @ 0.15 / B:1px solid #000000 @ 0.15 / L:1px solid #000000 @ 0.15 r 9999px | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab (on the field inside) |

Crops: `archived-search-default.png`, `archived-search-hover.png`, `archived-search-focus-visible.png`, `archived-search-light.png`, `archived-search-light-hover.png`, `archived-search-light-focus-visible.png`.

#### archived-row

List row (archived chat).

Page copy: `settings-dark-archived`. Finder: `() => C(Q('button[data-archived-chat-unarchive]'), '[class*="settings-row"]') // H(Q('button[data-archived-chat-unarchive]'), 56)`.

Dark theme.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 766 x 62 | = |
| Padding | 12px 16px | = |
| Gap | 24px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system-body 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ededed | = |
| Text node | a.cursor-interaction.truncate.text-info: -apple-system-body 14px/20px 500, #2c67c5 | = |
| Transition | none | = |
| Icon | 18 x 18, colour #ededed | = |
| ::after | 734px x 1px, absolute, bg #ffffff @ 0.15, radius 0px | = |
| Painted layers | div.@container/settings-row.px-4.items-center::after 734pxx1px bg #ffffff @ 0.15; button.no-drag.cursor-interaction.items-center 90.8x36.0 bg #ededed @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.no-drag.cursor-interaction.items-center 67.8x36.0 bg #ff6764 @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | = |
| Ancestor paint | 1 up div.flex.flex-col.rounded-2xl bg #000000 | = |
| How | at rest | mouse hover |

Light theme.

| Property | light | light-hover |
|---|---|---|
| Size (w x h) | 766 x 62 | = |
| Padding | 12px 16px | = |
| Gap | 24px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system-body 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0d0d0d | = |
| Text node | a.cursor-interaction.truncate.text-info: -apple-system-body 14px/20px 500, #2c67c5 | = |
| Transition | none | = |
| Icon | 18 x 18, colour #0d0d0d | = |
| ::after | 734px x 1px, absolute, bg #000000 @ 0.1, radius 0px | = |
| Painted layers | div.@container/settings-row.px-4.items-center::after 734pxx1px bg #000000 @ 0.1; button.no-drag.cursor-interaction.items-center 90.8x36.0 bg #0d0d0d @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.no-drag.cursor-interaction.items-center 67.8x36.0 bg #e02e2a @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | = |
| Ancestor paint | 1 up div.flex.flex-col.rounded-2xl bg #fcfcfc | = |
| How | at rest | mouse hover |

Crops: `archived-row-default.png`, `archived-row-hover.png`, `archived-row-light.png`, `archived-row-light-hover.png`.

#### archived-link

Link (archived chat title).

Page copy: `settings-dark-archived`. Finder: `() => Q('main a[href*="/c/"]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 90.61 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #99c8ff offset 1px | = |
| Font | -apple-system-body 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2c67c5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |
| Painted layers | - | = | a.cursor-interaction.truncate.text-info 90.6x20.0 outline 1px auto #99c8ff offset 1px | = |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 90.61 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | -apple-system-body 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2c67c5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |
| Painted layers | - | = | a.cursor-interaction.truncate.text-info 90.6x20.0 outline 1px auto #005fcc offset 1px | = |

Crops: `archived-link-default.png`, `archived-link-hover.png`, `archived-link-focus-visible.png`, `archived-link-pressed.png`, `archived-link-light.png`, `archived-link-light-hover.png`, `archived-link-light-focus-visible.png`, `archived-link-light-pressed.png`.

#### unarchive-button

Outline button (Unarchive).

Page copy: `settings-dark-archived`. Finder: `() => Q('button[data-archived-chat-unarchive]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 90.84 x 36 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ededed @ 0.05 | #ededed @ 0.1 | = | #ededed @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ededed | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 90.8x36.0 bg #ededed @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 90.8x36.0 bg #ededed @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 90.8x36.0 bg #ededed @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 90.8x36.0 bg #ededed @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 90.84 x 36 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #0d0d0d @ 0.05 | #0d0d0d @ 0.1 | = | #0d0d0d @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 90.8x36.0 bg #0d0d0d @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 90.8x36.0 bg #0d0d0d @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 90.8x36.0 bg #0d0d0d @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 90.8x36.0 bg #0d0d0d @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `unarchive-button-default.png`, `unarchive-button-hover.png`, `unarchive-button-focus-visible.png`, `unarchive-button-pressed.png`, `unarchive-button-light.png`, `unarchive-button-light-hover.png`, `unarchive-button-light-focus-visible.png`, `unarchive-button-light-pressed.png`.

#### text-link

Link (Manage tasks).

Page copy: `settings-dark-notifications-menu`. Finder: `() => C(T('Manage tasks'), 'a')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 78.11 x 15 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #99c8ff offset 1px | = |
| Font | -apple-system-body 12px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #cdcdcd | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |
| Painted layers | - | = | a.underline 78.1x15.0 outline 1px auto #99c8ff offset 1px | = |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 78.11 x 15 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | -apple-system-body 12px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #5d5d5d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |
| Painted layers | - | = | a.underline 78.1x15.0 outline 1px auto #005fcc offset 1px | = |

Crops: `text-link-default.png`, `text-link-hover.png`, `text-link-focus-visible.png`, `text-link-pressed.png`, `text-link-light.png`, `text-link-light-hover.png`, `text-link-light-focus-visible.png`, `text-link-light-pressed.png`.

### Pricing

#### pricing-dialog

Full-screen dialog (pricing).

Page copy: `pricing-dark`. Finder: `() => Q('[role=dialog]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | span: -apple-system-body 36px/40px 600, #ffffff |
| Transition | none |
| Icon | 20 x 20, colour #cdcdcd, fill #000000 |
| Painted layers | main.surface-Ypz1VS.page-F1Na4G 1440.0x900.0 bg #212121; button.no-drag.cursor-interaction.items-center 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; div.relative.rounded-full.p-1 352.0x44.0 bg #424242 r 20px; div.bg-(--bg-primary).absolute.inset-0 170.0x36.0 bg #212121 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 1px 2px -1px; div.border-s.border-e.border-t 384.0x736.0 bg #212121 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 24px shadow #000000 @ 0.05 0px 4px 8px 0px; button.no-drag.cursor-interaction.items-center 336.0x44.0 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px opacity 0.4 |
| Tokens | --cursor-interaction pointer |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span: -apple-system-body 36px/40px 600, #0d0d0d |
| Transition | none |
| Icon | 20 x 20, colour #5d5d5d, fill #000000 |
| Painted layers | main.surface-Ypz1VS.page-F1Na4G 1440.0x900.0 bg #f3f3f3; button.no-drag.cursor-interaction.items-center 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; div.relative.rounded-full.p-1 352.0x44.0 bg #ececec r 20px; div.bg-(--bg-primary).absolute.inset-0 170.0x36.0 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 1px 2px -1px; div.border-s.border-e.border-t 384.0x736.0 bg #fcfcfc border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 24px shadow #000000 @ 0.05 0px 4px 8px 0px; div.relative.flex.flex-col 336.0x294.0 bg #fcfcfc |
| Tokens | --cursor-interaction pointer |
| How | at rest |

Crops: none.

#### segmented-radio

Radio segment (Business, not checked).

Page copy: `pricing-dark`. Finder: `() => Q('[role=dialog] [role=radio][aria-checked=false]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed | checked |
|---|---|---|---|---|---|
| Size (w x h) | 170 x 36 | = | = | = | = |
| Padding | 8px 20px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 16px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #99c8ff offset 0px | = | = |
| Font | -apple-system-body 14px/20px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #afafaf | = | = | = | #ffffff |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Tokens | --cursor-interaction pointer; --text-tertiary #afafaf | = | = | = | --cursor-interaction pointer; --text-primary #fff |
| How | at rest | mouse hover | keyboard: Shift keydown, then focus() | mouse button held down on it (:hover:active) | at rest, captured checked |
| Painted layers | - | = | button.box-border.flex.h-full 170.0x36.0 r 16px outline 1px auto #99c8ff offset 0px | = | = |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed | light-checked |
|---|---|---|---|---|---|
| Size (w x h) | 170 x 36 | = | = | = | = |
| Padding | 8px 20px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 16px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = | = |
| Font | -apple-system-body 14px/20px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #8f8f8f | = | = | = | #0d0d0d |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Tokens | --cursor-interaction pointer; --text-tertiary #8f8f8f | = | = | = | --cursor-interaction pointer; --text-primary #0d0d0d |
| How | at rest | mouse hover | keyboard: Shift keydown, then focus() | mouse button held down on it (:hover:active) | at rest, captured checked |
| Painted layers | - | = | button.box-border.flex.h-full 170.0x36.0 r 16px outline 1px auto #005fcc offset 0px | = | = |

Other finders: checked: `() => Q('[role=dialog] [role=radio][aria-checked=true]')`; light-checked: `() => Q('[role=dialog] [role=radio][aria-checked=true]')`.

Crops: `segmented-radio-default.png`, `segmented-radio-hover.png`, `segmented-radio-focus-visible.png`, `segmented-radio-pressed.png`, `segmented-radio-checked.png`, `segmented-radio-light.png`, `segmented-radio-light-hover.png`, `segmented-radio-light-focus-visible.png`, `segmented-radio-light-pressed.png`, `segmented-radio-light-checked.png`.

#### pricing-card

Card (Free plan).

Page copy: `pricing-dark`. Finder: `() => P(Q('[data-pricing-plan-type=free]')) // Q('[data-pricing-plan-type=free]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 384 x 736 |
| Padding | 23px 23px 25px 23px |
| Gap | 24px |
| Border | 1px solid #ffffff @ 0.15 |
| Radius | 24px |
| Background | #212121 |
| Box shadow | #000000 @ 0.05 0px 4px 8px 0px |
| Outline | none |
| Font | -apple-system-body 14px/20px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.flex.min-w-0.flex-wrap: -apple-system-body 18px/32px 600, #ffffff, ls -0.18px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0, 0, 0.2, 1) |
| Icon | 20 x 20, colour #ffffff |
| Painted layers | div.border-s.border-e.border-t 384.0x736.0 bg #212121 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 24px shadow #000000 @ 0.05 0px 4px 8px 0px; button.no-drag.cursor-interaction.items-center 336.0x44.0 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px opacity 0.4 |
| Tokens | --bg-primary #212121; --border-default #ffffff26; --main-surface-primary #000; --text-primary #fff; --text-secondary #cdcdcd |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 336 x 294 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fcfcfc |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 14px/20px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span.flex.min-w-0.flex-wrap: -apple-system-body 18px/32px 600, #0d0d0d, ls -0.18px |
| Transition | none |
| Painted layers | div.relative.flex.flex-col 336.0x294.0 bg #fcfcfc; button.no-drag.cursor-interaction.items-center 336.0x44.0 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px opacity 0.4 |
| Ancestor paint | 1 up div.border-s.border-e.border-t bg #fcfcfc shadow #000000 @ 0.05 0px 4px 8px 0px |
| Tokens | --main-surface-primary #fcfcfc; --text-primary #0d0d0d; --text-secondary #5d5d5d |
| How | at rest |

Crops: `pricing-card-default.png`, `pricing-card-light.png`.

#### pricing-card-plus

Card (Plus plan, recommended).

Page copy: `pricing-dark`. Finder: `() => { const b = T('RECOMMENDED') // TS('Recommended'); let n = b; while (n && n.getBoundingClientRect().width < 300) n = n.parentElement; return P(n) // n; }`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 384 x 736 |
| Padding | 23px 23px 25px 23px |
| Gap | 24px |
| Border | 1px solid #3a83f7 @ 0.5 |
| Radius | 24px |
| Background | transparent |
| Background image | linear-gradient(#212121 0%, #274b72 100%) |
| Box shadow | #000000 @ 0.05 0px 4px 8px 0px |
| Outline | none |
| Font | -apple-system-body 14px/20px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.flex.min-w-0.flex-wrap: -apple-system-body 18px/32px 600, #ffffff, ls -0.18px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0, 0, 0.2, 1) |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | div.relative.z-10.flex 384.0x736.0 image linear-gradient(#212121 0%, #274b72 100%) border T:1px solid #3a83f7 @ 0.5 / R:1px solid #3a83f7 @ 0.5 / B:1px solid #3a83f7 @ 0.5 / L:1px solid #3a83f7 @ 0.5 r 24px shadow #000000 @ 0.05 0px 4px 8px 0px; span.ms-1.rounded-4xl.px-2 103.5x27.0 bg #3a83f7 @ 0.2 r 32px; button.no-drag.cursor-interaction.items-center 336.0x44.0 bg #3a83f7 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| Tokens | --accent-blue #3a83f7; --color-blue #3a83f7; --interactive-label-accent-accessible #a4cdfb; --text-primary #fff; --text-secondary #cdcdcd |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 384 x 736 |
| Padding | 23px 23px 25px 23px |
| Gap | 24px |
| Border | 1px solid #3a83f7 @ 0.5 |
| Radius | 24px |
| Background | transparent |
| Background image | linear-gradient(#ffffff 0%, #eef6ff 100%) |
| Box shadow | #000000 @ 0.05 0px 4px 8px 0px |
| Outline | none |
| Font | -apple-system-body 14px/20px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span.flex.min-w-0.flex-wrap: -apple-system-body 18px/32px 600, #0d0d0d, ls -0.18px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0, 0, 0.2, 1) |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | div.relative.z-10.flex 384.0x736.0 image linear-gradient(#ffffff 0%, #eef6ff 100%) border T:1px solid #3a83f7 @ 0.5 / R:1px solid #3a83f7 @ 0.5 / B:1px solid #3a83f7 @ 0.5 / L:1px solid #3a83f7 @ 0.5 r 24px shadow #000000 @ 0.05 0px 4px 8px 0px; span.ms-1.rounded-4xl.px-2 103.5x27.0 bg #3a83f7 @ 0.09 r 32px; button.no-drag.cursor-interaction.items-center 336.0x44.0 bg #3a83f7 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| Tokens | --accent-blue #3a83f7; --color-blue #3a83f7; --interactive-label-accent-accessible #2c67c5; --text-primary #0d0d0d; --text-secondary #5d5d5d |
| How | at rest |

Crops: `pricing-card-plus-default.png`, `pricing-card-plus-light.png`.

#### badge

Badge (RECOMMENDED).

Page copy: `pricing-dark`. Finder: `() => T('RECOMMENDED') // TS('Recommended')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 103.45 x 27 |
| Padding | 6px 8px 5px 8px |
| Border | none |
| Radius | 32px |
| Background | #3a83f7 @ 0.2 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 11px/16px 600 |
| Letter spacing | -0.18px |
| Colour | #a4cdfb |
| Transition | none |
| Painted layers | span.ms-1.rounded-4xl.px-2 103.5x27.0 bg #3a83f7 @ 0.2 r 32px |
| Tokens | --accent-blue #3a83f7; --interactive-label-accent-accessible #a4cdfb |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 103.45 x 27 |
| Padding | 6px 8px 5px 8px |
| Border | none |
| Radius | 32px |
| Background | #3a83f7 @ 0.09 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 11px/16px 600 |
| Letter spacing | -0.18px |
| Colour | #2c67c5 |
| Transition | none |
| Painted layers | span.ms-1.rounded-4xl.px-2 103.5x27.0 bg #3a83f7 @ 0.09 r 32px |
| Tokens | --accent-blue #3a83f7; --interactive-label-accent-accessible #2c67c5 |
| How | at rest |

Crops: `badge-default.png`, `badge-light.png`.

#### button-disabled-plan

Button (disabled, Your current plan).

Page copy: `pricing-dark`. Finder: `() => B('Your current plan')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 336 x 44 |
| Padding | 0px 16px |
| Gap | 4px |
| Border | 1px solid #ffffff @ 0.15 |
| Radius | 9999px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 14px/20px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Opacity | 0.4 |
| Cursor | default |
| Painted layers | button.no-drag.cursor-interaction.items-center 336.0x44.0 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px opacity 0.4 |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 336 x 44 |
| Padding | 0px 16px |
| Gap | 4px |
| Border | 1px solid #000000 @ 0.1 |
| Radius | 9999px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 14px/20px 500 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Transition | none |
| Opacity | 0.4 |
| Cursor | default |
| Painted layers | button.no-drag.cursor-interaction.items-center 336.0x44.0 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px opacity 0.4 |
| How | at rest |

Crops: `button-disabled-plan-default.png`, `button-disabled-plan-light.png`.

#### pricing-primary

Accent button (Rejoin Plus).

Page copy: `pricing-dark`. Finder: `() => B('Rejoin Plus')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 336 x 44 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #3a83f7 | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 336.0x44.0 bg #3a83f7 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | = | button.no-drag.cursor-interaction.items-center 336.0x44.0 bg #3a83f7 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 336 x 44 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #3a83f7 | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 336.0x44.0 bg #3a83f7 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | = | button.no-drag.cursor-interaction.items-center 336.0x44.0 bg #3a83f7 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `pricing-primary-default.png`, `pricing-primary-hover.png`, `pricing-primary-focus-visible.png`, `pricing-primary-pressed.png`, `pricing-primary-light.png`, `pricing-primary-light-hover.png`, `pricing-primary-light-focus-visible.png`, `pricing-primary-light-pressed.png`.

#### pricing-close

Icon button (Close pricing).

Page copy: `pricing-dark`. Finder: `() => Q('button[aria-label="Close pricing"]')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #ffffff @ 0.1 | = | #ffffff @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #cdcdcd | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #cdcdcd, fill #000000 | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 32.0x32.0 bg #ffffff @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 32.0x32.0 bg #ffffff @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #000000 @ 0.05 | = | #000000 @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system-body 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #5d5d5d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #5d5d5d, fill #000000 | = | = | = |
| Painted layers | button.no-drag.cursor-interaction.items-center 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 32.0x32.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.no-drag.cursor-interaction.items-center 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #3a83f7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.no-drag.cursor-interaction.items-center 32.0x32.0 bg #000000 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `pricing-close-default.png`, `pricing-close-hover.png`, `pricing-close-focus-visible.png`, `pricing-close-pressed.png`, `pricing-close-light.png`, `pricing-close-light-hover.png`, `pricing-close-light-focus-visible.png`, `pricing-close-light-pressed.png`.

### Signed out

#### onb-nudge

Card (sign-in nudge). The sidebar card a signed-out visitor sees: a heading, one line on what signing in adds, and a full-width Log in button.

Page copy: `onboarding-dark`. Finder: `() => C(T('Get responses tailored to you'), 'section')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 260 x 185 |
| Padding | 20px |
| Border | T: 1px solid #ffffff @ 0.15; R: none; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.x1gqwrcx.xpugu0j.xdj266r: -apple-system-body 14px/20px 500, #ffffff, ls -0.2px |
| Transition | none |
| Painted layers | section.x1y8v6su.x1o24gnf.x13fuv20 260.0x185.0 border T:1px solid #ffffff @ 0.15; button.x1d5dutw.xewkrzm.xllfjz4 220.0x44.0 bg #212121 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 999px |
| Ancestor paint | 1 up div.x1cho1rl.xz472uy.x5cu31j bg #000000 |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 260 x 185 |
| Padding | 20px |
| Border | T: 1px solid #000000 @ 0.1; R: none; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | h2.x1gqwrcx.xpugu0j.xdj266r: -apple-system-body 14px/20px 500, #0d0d0d, ls -0.2px |
| Transition | none |
| Painted layers | section.x1y8v6su.x1o24gnf.x13fuv20 260.0x185.0 border T:1px solid #000000 @ 0.1; button.x1d5dutw.xewkrzm.xllfjz4 220.0x44.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 999px |
| Ancestor paint | 1 up div.x1cho1rl.xz472uy.x5cu31j bg #fcfcfc |
| How | at rest |

Crops: `onb-nudge-default.png`, `onb-nudge-light.png`.

#### onb-login-header

Inverted button (Log in, header).

Page copy: `onboarding-dark`. Finder: `() => [...document.querySelectorAll('button')].find((b) => b.textContent.trim() === 'Log in' && b.getBoundingClientRect().y < 60)`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 64.03 x 44 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | #ffffff | #e8e8e8 | = | #cdcdcd |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3566f0 offset 2px | = |
| Font | -apple-system-body 14px/20px 600 | = | = | = |
| Letter spacing | -0.08px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.x6s0dn4.xgwjoxm.x1y0btm7 64.0x44.0 bg #ffffff r 999px | button.x6s0dn4.xgwjoxm.x1y0btm7 64.0x44.0 bg #e8e8e8 r 999px | button.x6s0dn4.xgwjoxm.x1y0btm7 64.0x44.0 bg #ffffff r 999px outline 2px solid #3566f0 offset 2px | button.x6s0dn4.xgwjoxm.x1y0btm7 64.0x44.0 bg #cdcdcd r 999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 64.03 x 44 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | #0d0d0d | #212121 | = | #303030 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3566f0 offset 2px | = |
| Font | -apple-system-body 14px/20px 600 | = | = | = |
| Letter spacing | -0.08px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.x6s0dn4.xgwjoxm.x1y0btm7 64.0x44.0 bg #0d0d0d r 999px | button.x6s0dn4.xgwjoxm.x1y0btm7 64.0x44.0 bg #212121 r 999px | button.x6s0dn4.xgwjoxm.x1y0btm7 64.0x44.0 bg #0d0d0d r 999px outline 2px solid #3566f0 offset 2px | button.x6s0dn4.xgwjoxm.x1y0btm7 64.0x44.0 bg #303030 r 999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `onb-login-header-default.png`, `onb-login-header-hover.png`, `onb-login-header-focus-visible.png`, `onb-login-header-pressed.png`, `onb-login-header-light.png`, `onb-login-header-light-hover.png`, `onb-login-header-light-focus-visible.png`, `onb-login-header-light-pressed.png`.

#### onb-signup-header

Secondary button (Sign up for free).

Page copy: `onboarding-dark`. Finder: `() => B('Sign up for free')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 128.8 x 44 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #ffffff @ 0.2 | = | = | = |
| Radius | 999px | = | = | = |
| Background | #212121 | #303030 | = | #303030 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3566f0 offset 2px | = |
| Font | -apple-system-body 14px/20px 600 | = | = | = |
| Letter spacing | -0.08px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.x1gnnqk1.x9f619.xc0rdgb 128.8x44.0 bg #212121 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 999px | button.x1gnnqk1.x9f619.xc0rdgb 128.8x44.0 bg #303030 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 999px | button.x1gnnqk1.x9f619.xc0rdgb 128.8x44.0 bg #212121 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 999px outline 2px solid #3566f0 offset 2px | button.x1gnnqk1.x9f619.xc0rdgb 128.8x44.0 bg #303030 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 128.8 x 44 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0.2 | = | = | = |
| Radius | 999px | = | = | = |
| Background | #ffffff | #f3f3f3 | = | #f3f3f3 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3566f0 offset 2px | = |
| Font | -apple-system-body 14px/20px 600 | = | = | = |
| Letter spacing | -0.08px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.x1gnnqk1.x9f619.xc0rdgb 128.8x44.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 999px | button.x1gnnqk1.x9f619.xc0rdgb 128.8x44.0 bg #f3f3f3 border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 999px | button.x1gnnqk1.x9f619.xc0rdgb 128.8x44.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 999px outline 2px solid #3566f0 offset 2px | button.x1gnnqk1.x9f619.xc0rdgb 128.8x44.0 bg #f3f3f3 border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `onb-signup-header-default.png`, `onb-signup-header-hover.png`, `onb-signup-header-focus-visible.png`, `onb-signup-header-pressed.png`, `onb-signup-header-light.png`, `onb-signup-header-light-hover.png`, `onb-signup-header-light-focus-visible.png`, `onb-signup-header-light-pressed.png`.

#### onb-login-card

Secondary button (Log in, card).

Page copy: `onboarding-dark`. Finder: `() => C(T('Get responses tailored to you'), 'section').querySelector('button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 220 x 44 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #ffffff @ 0.2 | = | = | = |
| Radius | 999px | = | = | = |
| Background | #212121 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3566f0 offset 2px | = |
| Font | -apple-system-body 14px/18.6666px 500 | = | = | = |
| Letter spacing | -0.2px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.x1d5dutw.xewkrzm.xllfjz4 220.0x44.0 bg #212121 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 999px | = | button.x1d5dutw.xewkrzm.xllfjz4 220.0x44.0 bg #212121 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 999px outline 2px solid #3566f0 offset 2px | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 220 x 44 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0.2 | = | = | = |
| Radius | 999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3566f0 offset 2px | = |
| Font | -apple-system-body 14px/18.6666px 500 | = | = | = |
| Letter spacing | -0.2px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.x1d5dutw.xewkrzm.xllfjz4 220.0x44.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 999px | = | button.x1d5dutw.xewkrzm.xllfjz4 220.0x44.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 999px outline 2px solid #3566f0 offset 2px | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `onb-login-card-default.png`, `onb-login-card-hover.png`, `onb-login-card-focus-visible.png`, `onb-login-card-pressed.png`, `onb-login-card-light.png`, `onb-login-card-light-hover.png`, `onb-login-card-light-focus-visible.png`, `onb-login-card-light-pressed.png`.

#### onb-dialog

Dialog (Log in or sign up). Opened by Sign up for free: three provider buttons, an OR rule, an email field and Continue.

Page copy: `onboarding-dark-signup`. Finder: `() => [...document.querySelectorAll('dialog[open], [role=dialog]')].filter((d) => d.getBoundingClientRect().width > 300).pop()`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 448 x 504 |
| Padding | 0px |
| Border | none |
| Radius | 20px |
| Background | #303030 |
| Box shadow | #000000 @ 0.22 0px 24px 64px 0px, #000000 @ 0.12 0px 4px 16px 0px |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.xorku9x.xcg35fi.x1h1fi3m: -apple-system-body 24px/32px 400, #ffffff |
| Transition | transform 0.3s cubic-bezier(0.2, 0, 0, 1) |
| Transform | matrix(1, 0, 0, 1, -224, -252) |
| Icon | 20 x 20, colour #ffffff |
| Placeholder | "" #ffffff, opacity 1, 16px |
| Painted layers | dialog.xm7sogi.x1jpqdmu.x1l9hn29 448.0x504.0 bg #303030 r 20px shadow #000000 @ 0.22 0px 24px 64px 0px, #000000 @ 0.12 0px 4px 16px 0px; section.x1f9q82l.xxny6gs.x1v1hne3 448.0x504.0 bg #303030; button.x6s0dn4.xgwjoxm.x1y0btm7 44.0x44.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px; a.x6s0dn4.xgwjoxm.x1y0btm7 365.0x48.0 bg #212121 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 999px; a.x6s0dn4.xgwjoxm.x1y0btm7 365.0x48.0 bg #212121 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 999px; button.x6s0dn4.xgwjoxm.x1y0btm7 365.0x48.0 bg #212121 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 999px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 448 x 504 |
| Padding | 0px |
| Border | none |
| Radius | 20px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.22 0px 24px 64px 0px, #000000 @ 0.12 0px 4px 16px 0px |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | h2.xorku9x.xcg35fi.x1h1fi3m: -apple-system-body 24px/32px 400, #0d0d0d |
| Transition | transform 0.3s cubic-bezier(0.2, 0, 0, 1) |
| Transform | matrix(1, 0, 0, 1, -224, -252) |
| Icon | 20 x 20, colour #0d0d0d |
| Placeholder | "" #000000, opacity 1, 16px |
| Painted layers | dialog.xm7sogi.x1jpqdmu.x1l9hn29 448.0x504.0 bg #ffffff r 20px shadow #000000 @ 0.22 0px 24px 64px 0px, #000000 @ 0.12 0px 4px 16px 0px; section.x1f9q82l.xxny6gs.x1v1hne3 448.0x504.0 bg #ffffff; button.x6s0dn4.xgwjoxm.x1y0btm7 44.0x44.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px; a.x6s0dn4.xgwjoxm.x1y0btm7 365.0x48.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 999px; a.x6s0dn4.xgwjoxm.x1y0btm7 365.0x48.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 999px; button.x6s0dn4.xgwjoxm.x1y0btm7 365.0x48.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 999px |
| How | at rest |

Crops: `onb-dialog-default.png`, `onb-dialog-light.png`.

#### onb-provider

Outline button (Continue with Google).

Page copy: `onboarding-dark-signup`. Finder: `() => C(T('Continue with Google'), 'a,button')`.

Dark theme.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 364.66 x 47.96 | 365 x 48 | 365 x 48 | 365 x 48 |
| Padding | 0px 16px 0px 12.0001px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #ffffff @ 0.2 | = | = | = |
| Radius | 999px | = | = | = |
| Background | #212121 | #303030 | = | #414141 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3566f0 offset 1px | = |
| Font | -apple-system-body 16px/20px 500 | = | = | = |
| Letter spacing | -0.08px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: -apple-system-body 16px/20px 500, #ffffff, ls -0.08px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 19.98 x 19.98, colour #ffffff | 20 x 20, colour #ffffff | 20 x 20, colour #ffffff | 20 x 20, colour #ffffff |
| Painted layers | a.x6s0dn4.xgwjoxm.x1y0btm7 364.7x48.0 bg #212121 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 999px | a.x6s0dn4.xgwjoxm.x1y0btm7 365.0x48.0 bg #303030 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 999px | a.x6s0dn4.xgwjoxm.x1y0btm7 365.0x48.0 bg #212121 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 999px outline 2px solid #3566f0 offset 1px | a.x6s0dn4.xgwjoxm.x1y0btm7 365.0x48.0 bg #414141 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed |
|---|---|---|---|---|
| Size (w x h) | 364.66 x 47.96 | 365 x 48 | 365 x 48 | 365 x 48 |
| Padding | 0px 16px 0px 12.0001px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0.2 | = | = | = |
| Radius | 999px | = | = | = |
| Background | #ffffff | #f3f3f3 | = | #e8e8e8 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3566f0 offset 1px | = |
| Font | -apple-system-body 16px/20px 500 | = | = | = |
| Letter spacing | -0.08px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Text node | span: -apple-system-body 16px/20px 500, #0d0d0d, ls -0.08px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 19.98 x 19.98, colour #0d0d0d | 20 x 20, colour #0d0d0d | 20 x 20, colour #0d0d0d | 20 x 20, colour #0d0d0d |
| Painted layers | a.x6s0dn4.xgwjoxm.x1y0btm7 364.7x48.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 999px | a.x6s0dn4.xgwjoxm.x1y0btm7 365.0x48.0 bg #f3f3f3 border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 999px | a.x6s0dn4.xgwjoxm.x1y0btm7 365.0x48.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 999px outline 2px solid #3566f0 offset 1px | a.x6s0dn4.xgwjoxm.x1y0btm7 365.0x48.0 bg #e8e8e8 border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) |

Crops: `onb-provider-default.png`, `onb-provider-hover.png`, `onb-provider-focus-visible.png`, `onb-provider-pressed.png`, `onb-provider-light.png`, `onb-provider-light-hover.png`, `onb-provider-light-focus-visible.png`, `onb-provider-light-pressed.png`.

#### onb-email

Text field (email).

Page copy: `onboarding-dark-signup`, `onboarding-dark-email-error`. Finder: `() => Q('input[type=email]')`.

Dark theme.

| Property | default | hover | focus-visible | error |
|---|---|---|---|---|
| Size (w x h) | 365 x 48 | = | = | = |
| Padding | 1px 16px | = | = | = |
| Border | 1px solid #ffffff @ 0.15 | = | = | 1px solid #fa423e |
| Radius | 999px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3566f0 offset 2px | = |
| Font | -apple-system-body 16px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | text | = | = | = |
| Placeholder | "Email address" #cdcdcd, opacity 1, 16px | = | = | = |
| Painted layers | input.x1pw6kkn.x7xwk5j.x1v3hlx4 365.0x48.0 bg #000000 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 999px | = | input.x1pw6kkn.x7xwk5j.x1v3hlx4 365.0x48.0 bg #000000 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 999px outline 2px solid #3566f0 offset 2px | input.x1pw6kkn.x7xwk5j.x1v3hlx4 365.0x48.0 bg #000000 border T:1px solid #fa423e / R:1px solid #fa423e / B:1px solid #fa423e / L:1px solid #fa423e r 999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | at rest, captured error |

Light theme.

| Property | light | light-hover | light-focus-visible | light-error |
|---|---|---|---|---|
| Size (w x h) | 365 x 48 | = | = | 364.97 x 48 |
| Padding | 1px 16px | = | = | = |
| Border | 1px solid #000000 @ 0.1 | = | = | 1px solid #ba2623 |
| Radius | 999px | = | = | = |
| Background | #fcfcfc | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3566f0 offset 2px | = |
| Font | -apple-system-body 16px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | text | = | = | = |
| Placeholder | "Email address" #5d5d5d, opacity 1, 16px | = | = | = |
| Painted layers | input.x1pw6kkn.x7xwk5j.x1v3hlx4 365.0x48.0 bg #fcfcfc border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 999px | = | input.x1pw6kkn.x7xwk5j.x1v3hlx4 365.0x48.0 bg #fcfcfc border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 999px outline 2px solid #3566f0 offset 2px | input.x1pw6kkn.x7xwk5j.x1v3hlx4 365.0x48.0 bg #fcfcfc border T:1px solid #ba2623 / R:1px solid #ba2623 / B:1px solid #ba2623 / L:1px solid #ba2623 r 999px |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | at rest, captured error |

Other finders: error: `() => Q('input[type=email]')`; light-error: `() => Q('input[type=email]')`.

Crops: `onb-email-default.png`, `onb-email-hover.png`, `onb-email-focus-visible.png`, `onb-email-error.png`, `onb-email-light.png`, `onb-email-light-hover.png`, `onb-email-light-focus-visible.png`, `onb-email-light-error.png`.

#### onb-email-error

Field error text (Email is not valid.). Shown under the field after Continue with an incomplete address; the field gets a red border and aria-invalid.

Page copy: `onboarding-dark-email-error`. Finder: `() => C(T('Email is not valid.'), 'p') // T('Email is not valid.')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 364.86 x 15.99 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 12px/16px 400 |
| Letter spacing | normal |
| Colour | #ff6764 |
| Text node | span: -apple-system-body 12px/16px 400, #ff6764 |
| Transition | none |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 364.66 x 15.99 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 12px/16px 400 |
| Letter spacing | normal |
| Colour | #ba2623 |
| Text node | span: -apple-system-body 12px/16px 400, #ba2623 |
| Transition | none |
| How | at rest |

Crops: `onb-email-error-default.png`, `onb-email-error-light.png`.

#### onb-continue

Primary button (Continue).

Page copy: `onboarding-dark-signup`, `onboarding-dark-email-error`. Finder: `() => B('Continue')`.

Dark theme.

| Property | default | hover | focus-visible | pressed | after-error |
|---|---|---|---|---|---|
| Size (w x h) | 364.66 x 47.96 | 365 x 48 | 365 x 48 | 365 x 48 | = |
| Padding | 0px 16px | = | = | = | = |
| Gap | 6px | = | = | = | = |
| Border | 1px solid #ffffff | = | = | = | = |
| Radius | 999px | = | = | = | = |
| Background | #ffffff | #e8e8e8 | = | #cdcdcd | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #3566f0 offset 0px | = | = |
| Font | -apple-system-body 16px/20px 500 | = | = | = | = |
| Letter spacing | -0.08px | = | = | = | = |
| Colour | #0d0d0d | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | button.x6s0dn4.xgwjoxm.x1y0btm7 364.7x48.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 999px | button.x6s0dn4.xgwjoxm.x1y0btm7 365.0x48.0 bg #e8e8e8 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 999px | button.x6s0dn4.xgwjoxm.x1y0btm7 365.0x48.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 999px outline 2px solid #3566f0 offset 0px | button.x6s0dn4.xgwjoxm.x1y0btm7 365.0x48.0 bg #cdcdcd border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 999px | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) | at rest, captured after-error |

Light theme.

| Property | light | light-hover | light-focus-visible | light-pressed | light-after-error |
|---|---|---|---|---|---|
| Size (w x h) | 364.66 x 47.96 | 365 x 48 | 365 x 48 | 365 x 48 | = |
| Padding | 0px 16px | = | = | = | = |
| Gap | 6px | = | = | = | = |
| Border | 1px solid #0d0d0d | = | = | = | = |
| Radius | 999px | = | = | = | = |
| Background | #0d0d0d | #212121 | = | #303030 | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #3566f0 offset 0px | = | = |
| Font | -apple-system-body 16px/20px 500 | = | = | = | = |
| Letter spacing | -0.08px | = | = | = | = |
| Colour | #ffffff | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | button.x6s0dn4.xgwjoxm.x1y0btm7 364.7x48.0 bg #0d0d0d border T:1px solid #0d0d0d / R:1px solid #0d0d0d / B:1px solid #0d0d0d / L:1px solid #0d0d0d r 999px | button.x6s0dn4.xgwjoxm.x1y0btm7 365.0x48.0 bg #212121 border T:1px solid #0d0d0d / R:1px solid #0d0d0d / B:1px solid #0d0d0d / L:1px solid #0d0d0d r 999px | button.x6s0dn4.xgwjoxm.x1y0btm7 365.0x48.0 bg #0d0d0d border T:1px solid #0d0d0d / R:1px solid #0d0d0d / B:1px solid #0d0d0d / L:1px solid #0d0d0d r 999px outline 2px solid #3566f0 offset 0px | button.x6s0dn4.xgwjoxm.x1y0btm7 365.0x48.0 bg #303030 border T:1px solid #0d0d0d / R:1px solid #0d0d0d / B:1px solid #0d0d0d / L:1px solid #0d0d0d r 999px | = |
| How | at rest | mouse hover | keyboard: focus(), Shift+Tab, Tab | mouse button held down on it (:hover:active) | at rest, captured after-error |

Other finders: after-error: `() => B('Continue')`; light-after-error: `() => B('Continue')`.

Crops: `onb-continue-default.png`, `onb-continue-hover.png`, `onb-continue-focus-visible.png`, `onb-continue-pressed.png`, `onb-continue-after-error.png`, `onb-continue-light.png`, `onb-continue-light-hover.png`, `onb-continue-light-focus-visible.png`, `onb-continue-light-pressed.png`, `onb-continue-light-after-error.png`.

### Phone

#### m-header

Phone header.

Page copy: `mobile-home-dark`. Finder: `() => QA('header')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 390 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | button.cursor-interaction.relative.z-10: -apple-system-body 14px/20px 500, #ffffff |
| Transition | none |
| Icon | 20 x 20, colour #afafaf, fill #000000 |
| Painted layers | div.rounded-lg.bg-surface 36.0x36.0 bg #000000 r 8px; button.Button-QTscM8.group/sidebar-trigger::before 36pxx36px bg #ffffff @ 0.1 r 8px opacity 0; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; span.pointer-events-none.absolute.inset-x-px 222.0x34.0 bg #131313 r 9999px; span.pointer-events-none.relative.z-10 121.0x37.0 bg #1b1b1b border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| Ancestor paint | 1 up main.outline-none.MainContentSurface-EnuIYE.MainContentLeftBorder-IFAvO_ bg #000000 |
| Tokens | --app-shell-application-menu-height 0px; --app-shell-page-banner-height 0px; --app-shell-root-banner-height 0px; --app-shell-titlebar-height calc(.25rem * 13); --color-text-primary-ghost #ededed; --color-text-tertiary #afafaf; --height-toolbar calc(.25rem * 13); --spacing .25rem; --spacing-token-safe-header-left 6px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 390 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | button.cursor-interaction.relative.z-10: -apple-system-body 14px/20px 500, #0d0d0d |
| Transition | none |
| Icon | 20 x 20, colour #8f8f8f, fill #000000 |
| Painted layers | div.rounded-lg.bg-surface 36.0x36.0 bg #fcfcfc r 8px; button.Button-QTscM8.group/sidebar-trigger::before 36pxx36px bg #000000 @ 0.05 r 8px opacity 0; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; span.pointer-events-none.absolute.inset-x-px 222.0x34.0 bg #0d0d0d @ 0.03 r 9999px; span.pointer-events-none.relative.z-10 121.0x37.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px shadow #000000 @ 0.05 0px 1px 6px 0px |
| Ancestor paint | 1 up main.outline-none.MainContentSurface-EnuIYE.MainContentLeftBorder-IFAvO_ bg #fcfcfc |
| Tokens | --app-shell-application-menu-height 0px; --app-shell-page-banner-height 0px; --app-shell-root-banner-height 0px; --app-shell-titlebar-height calc(.25rem * 13); --color-text-primary-ghost #0d0d0d; --color-text-tertiary #8f8f8f; --height-toolbar calc(.25rem * 13); --spacing .25rem; --spacing-token-safe-header-left 6px |
| How | at rest |

Crops: `m-header-default.png`, `m-header-light.png`.

#### m-composer

Phone composer.

Page copy: `mobile-home-dark`. Finder: `() => P(Q('.ProseMirror').parentElement)`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 358 x 87 |
| Padding | 0px |
| Border | none |
| Radius | 28px |
| Background | #1b1b1b |
| Box shadow | #ffffff @ 0.2 0px 0px 1px 0px inset |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Transition | none |
| Icon | 20 x 20, colour #ededed, fill #000000 |
| Placeholder | "Ask ChatGPT" #afafaf, opacity 1, 16px |
| Painted layers | div.ComposerLayoutBody-uBBf1A 358.0x87.0 bg #1b1b1b r 28px shadow #ffffff @ 0.2 0px 0px 1px 0px inset; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.cursor-interaction.size-token-button-composer.flex 36.0x36.0 bg #2c67c5 r 9999px |
| Tokens | --composer-editor-line-height calc(16px * 1.625); --spacing .25rem; --text-sm 14px |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 358 x 87 |
| Padding | 0px |
| Border | none |
| Radius | 28px |
| Background | #ffffff |
| Box shadow | #ffffff @ 0.2 0px 0px 1px 0px inset |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Transition | none |
| Icon | 20 x 20, colour #0d0d0d, fill #000000 |
| Placeholder | "Ask ChatGPT" #8f8f8f, opacity 1, 16px |
| Painted layers | div.ComposerLayoutBody-uBBf1A 358.0x87.0 bg #ffffff r 28px shadow #ffffff @ 0.2 0px 0px 1px 0px inset; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.no-drag.cursor-interaction.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; button.cursor-interaction.size-token-button-composer.flex 36.0x36.0 bg #3a83f7 r 9999px |
| Tokens | --composer-editor-line-height calc(16px * 1.625); --spacing .25rem; --text-sm 14px |
| How | at rest |

Crops: `m-composer-default.png`, `m-composer-light.png`.

#### m-drawer

Phone drawer.

Page copy: `mobile-home-dark-drawer`. Finder: `() => S() // D()`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 260 x 844 |
| Padding | 0px |
| Border | T: none; R: 1px solid #ffffff @ 0.15; B: none; L: none |
| Radius | 0px |
| Background | #000000 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 8px -2px |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | span.text-fade-truncate: -apple-system-body 14px/20px 400, #ededed |
| Transition | transform, translate, scale, rotate 0.2s cubic-bezier(0, 0, 0.2, 1) |
| Icon | 77.13 x 18, colour #ededed |
| Painted layers | div.codex-dialog.z-50.outline-none 260.0x844.0 bg #000000 border R:1px solid #ffffff @ 0.15 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 8px -2px; button.Button-QTscM8::before 36pxx36px bg #ffffff @ 0.1 r 8px opacity 0; button.Button-QTscM8.group/sidebar-trigger::before 36pxx36px bg #ffffff @ 0.1 r 8px opacity 0; button.sidebar-item.relative.shrink-0 247.0x35.0 bg #ffffff @ 0.1 r 8px |
| Tokens | --color-text-primary-ghost #ededed; --color-text-tertiary #afafaf; --height-token-row calc(16px * 1.5 + calc(.25rem * 1) * 2); --icon-leading-size calc(.25rem * 5); --padding-row-x calc(.25rem * 2); --spacing-nav-row-content calc(.25rem * 1.5) |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 260 x 844 |
| Padding | 0px |
| Border | T: none; R: 1px solid #000000 @ 0.1; B: none; L: none |
| Radius | 0px |
| Background | #fcfcfc |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 8px -2px |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span.text-fade-truncate: -apple-system-body 14px/20px 400, #0d0d0d |
| Transition | transform, translate, scale, rotate 0.2s cubic-bezier(0, 0, 0.2, 1) |
| Icon | 77.13 x 18, colour #0d0d0d |
| Painted layers | div.codex-dialog.z-50.outline-none 260.0x844.0 bg #fcfcfc border R:1px solid #000000 @ 0.1 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 8px -2px; button.Button-QTscM8::before 36pxx36px bg #000000 @ 0.05 r 8px opacity 0; button.Button-QTscM8.group/sidebar-trigger::before 36pxx36px bg #000000 @ 0.05 r 8px opacity 0; button.sidebar-item.relative.shrink-0 247.0x35.0 bg #000000 @ 0.05 r 8px |
| Tokens | --color-text-primary-ghost #0d0d0d; --color-text-tertiary #8f8f8f; --height-token-row calc(16px * 1.5 + calc(.25rem * 1) * 2); --icon-leading-size calc(.25rem * 5); --padding-row-x calc(.25rem * 2); --spacing-nav-row-content calc(.25rem * 1.5) |
| How | at rest |

Crops: `m-drawer-default.png`, `m-drawer-light.png`.

#### m-drawer-row

Phone drawer row.

Page copy: `mobile-home-dark-drawer`. Finder: `() => Q('button[data-sidebar-destination="builtin:images"]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 247 x 35 |
| Padding | 6px 10px |
| Gap | 8px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 14px/20px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | span.text-fade-truncate: -apple-system-body 14px/20px 400, #ededed @ 0.85 |
| Transition | none |
| Cursor | pointer |
| Icon | 20 x 20, colour #ededed @ 0.85, fill #000000 |
| Tokens | --height-token-row 36px; --icon-leading-size calc(.25rem * 5); --nav-item-height calc(36px - 1px); --padding-row-cell-x 10px; --padding-row-x 6px; --spacing-nav-row-content calc(.25rem * 1.5) |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 247 x 35 |
| Padding | 6px 10px |
| Gap | 8px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 14px/20px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span.text-fade-truncate: -apple-system-body 14px/20px 400, #0d0d0d @ 0.85 |
| Transition | none |
| Cursor | pointer |
| Icon | 20 x 20, colour #0d0d0d @ 0.85, fill #000000 |
| Tokens | --height-token-row 36px; --icon-leading-size calc(.25rem * 5); --nav-item-height calc(36px - 1px); --padding-row-cell-x 10px; --padding-row-x 6px; --spacing-nav-row-content calc(.25rem * 1.5) |
| How | at rest |

Crops: `m-drawer-row-default.png`, `m-drawer-row-light.png`.

#### m-user-bubble

Phone user bubble.

Page copy: `mobile-thread-dark`. Finder: `() => Q('[data-user-message-bubble]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 250.59 x 574 |
| Padding | 10px 16px |
| Border | none |
| Radius | 22px |
| Background | #173e76 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f6fafe |
| Text node | span: -apple-system-body 16px/26px 400, #f6fafe |
| Transition | none |
| Icon | 16 x 16, colour #f6fafe |
| Painted layers | div.bg-user-message.text-user-message.min-w-0 250.6x574.0 bg #173e76 r 22px |
| Tokens | --thread-content-margin calc(.25rem * 4); --user-chat-width 70% |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 250.59 x 574 |
| Padding | 10px 16px |
| Border | none |
| Radius | 22px |
| Background | #e8f3fe |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0c274a |
| Text node | span: -apple-system-body 16px/26px 400, #0c274a |
| Transition | none |
| Icon | 16 x 16, colour #0c274a |
| Painted layers | div.bg-user-message.text-user-message.min-w-0 250.6x574.0 bg #e8f3fe r 22px |
| Tokens | --thread-content-margin calc(.25rem * 4); --user-chat-width 70% |
| How | at rest |

Crops: `m-user-bubble-default.png`, `m-user-bubble-light.png`.

#### m-code-block

Phone code block.

Page copy: `mobile-thread-dark-bottom`. Finder: `() => Q('[class*="CodeSurface"]')`.

Dark theme.

| Property | default |
|---|---|
| Size (w x h) | 358 x 250.25 |
| Padding | 0px |
| Border | 1px solid #ffffff @ 0.05 |
| Radius | 24px |
| Background | #303030 |
| Background image | linear-gradient(#ffffff @ 0.1, #ffffff @ 0.1) |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/26px 400 |
| Letter spacing | normal |
| Colour | #ededed |
| Text node | div.min-w-0.flex-1.truncate: -apple-system-body 14px/20px 500, #ededed |
| Transition | none |
| Icon | 20 x 20, colour #ededed, fill #000000 |
| Painted layers | div.relative.Root-iW7ipz.w-full 358.0x250.3 bg #303030 image linear-gradient(#ffffff @ 0.1, #ffffff @ 0.1) border T:1px solid #ffffff @ 0.05 / R:1px solid #ffffff @ 0.05 / B:1px solid #ffffff @ 0.05 / L:1px solid #ffffff @ 0.05 r 24px; div.flex.items-center.font-sans 356.0x48.0 bg #303030 image linear-gradient(#ffffff @ 0.1, #ffffff @ 0.1); button.group/scroll-to-bottom.cursor-interaction.absolute 32.0x32.0 bg #303030 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 9999px opacity 0 |
| Tokens | --radius-3xl-base 1.5rem |
| How | at rest |

Light theme.

| Property | light |
|---|---|
| Size (w x h) | 358 x 250.25 |
| Padding | 0px |
| Border | 1px solid #000000 @ 0.05 |
| Radius | 24px |
| Background | #f3f3f3 |
| Background image | linear-gradient(#000000 @ 0.05, #000000 @ 0.05) |
| Box shadow | none |
| Outline | none |
| Font | -apple-system-body 16px/26px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | div.min-w-0.flex-1.truncate: -apple-system-body 14px/20px 500, #0d0d0d |
| Transition | none |
| Icon | 20 x 20, colour #0d0d0d, fill #000000 |
| Painted layers | div.relative.Root-iW7ipz.w-full 358.0x250.3 bg #f3f3f3 image linear-gradient(#000000 @ 0.05, #000000 @ 0.05) border T:1px solid #000000 @ 0.05 / R:1px solid #000000 @ 0.05 / B:1px solid #000000 @ 0.05 / L:1px solid #000000 @ 0.05 r 24px; div.flex.items-center.font-sans 356.0x48.0 bg #f3f3f3 image linear-gradient(#000000 @ 0.05, #000000 @ 0.05); button.group/scroll-to-bottom.cursor-interaction.absolute 32.0x32.0 bg #f3f3f3 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 9999px opacity 0 |
| Tokens | --radius-3xl-base 1.5rem |
| How | at rest |

Crops: `m-code-block-default.png`, `m-code-block-light.png`.
