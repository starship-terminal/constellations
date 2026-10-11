# TokenTracker component measurements

Computed styles read from TokenTracker v1.3.5's dashboard (the local server the CLI runs, 127.0.0.1:7680) on 2026-10-11 by `tools/capture/public/measure.mjs`, no account signed in, in headless Chromium at 1440 x 900. Keys ending `.light` were read in the light theme, the rest in dark (the default). Private text (paths, session titles, skill names) was replaced before reading. and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### sidebar

Sidebar. The 220px rail on the page wash: no fill of its own, three groups, footer pills.

Page: dashboard. Selector: `aside`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 220 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | div.px-3.pb-1: ui-sans-serif 10px/15px 400, #737373, ls 0.5px |
| Transition | width 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 16 x 16, colour #737373 |
| Painted layers | div.h-9.w-9 36.0x36.0 bg #262626 r 9999px; a.flex.items-center 204.0x32.0 bg #262626 r 8px; span.tt-sidebar-pill.tt-sidebar-theme-face 32.0x32.0 border T:1px solid #404040 / R:1px solid #404040 / B:1px solid #404040 / L:1px solid #404040 r 9999px; span.tt-sidebar-pill.inline-flex 63.9x32.0 border T:1px solid #404040 / R:1px solid #404040 / B:1px solid #404040 / L:1px solid #404040 r 9999px |
| How | at rest |

Crops: `sidebar-default.png`.

#### sidebar-group-label

Sidebar group label.

Page: dashboard. Selector: `leaf "Tools"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 204 x 35 |
| Padding | 16px 12px 4px 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 10px/15px 400 |
| Letter spacing | 0.5px |
| Colour | #737373 |
| Transition | none |
| How | at rest |

Crops: `sidebar-group-label-default.png`.

#### nav-item-active

Nav item, current.

Page: dashboard. Selector: `a[href="/dashboard"] (Tokens)`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 204 x 32 | = |
| Padding | 6px 8px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #262626 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 13px/19.5px 500 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | span.truncate: ui-sans-serif 13px/19.5px 500, #ffffff | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 15 x 15, colour #ffffff | = |
| Painted layers | a.flex.items-center 204.0x32.0 bg #262626 r 8px | = |
| How | at rest | Shift+Tab, Tab |

Crops: `nav-item-active-default.png`, `nav-item-active-focus-visible.png`.

#### nav-item

Nav item.

Page: dashboard. Selector: `a[href="/sessions"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 204 x 32 | = | = | = |
| Padding | 6px 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #262626 @ 0.6 | = | #262626 @ 0.6 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 13px/19.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #a3a3a3 | #ffffff | = | #ffffff |
| Text node | span.truncate: ui-sans-serif 13px/19.5px 400, #a3a3a3 | span.truncate: ui-sans-serif 13px/19.5px 400, #ffffff | = | span.truncate: ui-sans-serif 13px/19.5px 400, #ffffff |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 15 x 15, colour #a3a3a3 | 15 x 15, colour #ffffff | = | 15 x 15, colour #ffffff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.flex.items-center 204.0x32.0 bg #262626 @ 0.6 r 8px | = | a.flex.items-center 204.0x32.0 bg #262626 @ 0.6 r 8px |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`.

#### nav-icon

Nav icon. Lucide History at the nav size.

Page: dashboard. Selector: `a[href="/sessions"] svg`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 15 x 15 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 13px/19.5px 400 |
| Letter spacing | normal |
| Colour | #a3a3a3 |
| Transition | none |
| Cursor | pointer |
| Icon | 15 x 15, colour #a3a3a3 |
| How | at rest |

Crops: `nav-icon-default.png`.

#### content-panel

Content panel. The rounded panel the pages sit in, inset from the window edge on the page wash.

Page: dashboard. Selector: `first rounded, filled ancestor of main`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1208 x 880 |
| Padding | 0px |
| Border | 1px solid #262626 |
| Radius | 16px |
| Background | #171717 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | span.flex.items-center: ui-sans-serif 9px/13.5px 600, #ffffff @ 0.9, ls -0.225px |
| Transition | none |
| Icon | 0 x 0, colour #a3a3a3 |
| Painted layers | div.flex-1.min-h-0 1208.0x880.0 bg #171717 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; div.lg:hidden.flex 0.0x0.0 border B:1px solid #262626; div.relative.rounded-xl 375.3x259.5 bg #171717 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 16px; div.relative.h-24 341.3x96.0 bg #020617 r 12px shadow #ffffff 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; div.absolute.-left-10 224.0x144.0 bg #4f46e5 @ 0.25 r 9999px; div.absolute.-right-8 192.0x128.0 bg #0ea5e9 @ 0.15 r 9999px |
| How | at rest |

Crops: none.

#### theme-toggle

Theme toggle.

Page: dashboard. Selector: `button[aria-label*=theme]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 44 x 44 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 9999px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #fafafa | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 14 x 14, colour #a3a3a3 | 14 x 14, colour #ffffff |
| Painted layers | span.tt-sidebar-pill.tt-sidebar-theme-face 32.0x32.0 border T:1px solid #404040 / R:1px solid #404040 / B:1px solid #404040 / L:1px solid #404040 r 9999px | span.tt-sidebar-pill.tt-sidebar-theme-face 32.0x32.0 bg #262626 border T:1px solid #525252 / R:1px solid #525252 / B:1px solid #525252 / L:1px solid #525252 r 9999px |
| How | at rest | mouse hover |

Crops: `theme-toggle-default.png`, `theme-toggle-hover.png`.

#### star-pill

GitHub star pill.

Page: dashboard. Selector: `a[href*=github]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 63.92 x 44 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 9999px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #fafafa | = |
| Text node | span: ui-sans-serif 12px/12px 500, #a3a3a3 | span: ui-sans-serif 12px/12px 500, #ffffff |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 12 x 12, colour #a3a3a3 | 12 x 12, colour #ffffff |
| Painted layers | span.tt-sidebar-pill.inline-flex 63.9x32.0 border T:1px solid #404040 / R:1px solid #404040 / B:1px solid #404040 / L:1px solid #404040 r 9999px | span.tt-sidebar-pill.inline-flex 63.9x32.0 bg #262626 border T:1px solid #525252 / R:1px solid #525252 / B:1px solid #525252 / L:1px solid #525252 r 9999px |
| How | at rest | mouse hover |

Crops: `star-pill-default.png`, `star-pill-hover.png`.

#### sidebar.light

Sidebar. The 220px rail on the page wash: no fill of its own, three groups, footer pills.

Page: dashboard. Selector: `aside`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 220 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span.truncate.flex-1: ui-sans-serif 13px/19.5px 500, #404040 |
| Transition | width 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 16 x 16, colour #737373 |
| Painted layers | a.flex.items-center 204.0x32.0 bg #e5e5e5 @ 0.7 r 8px; span.tt-sidebar-pill.tt-sidebar-theme-face 32.0x32.0 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px; span.tt-sidebar-pill.inline-flex 63.9x32.0 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px |
| How | at rest |

Crops: `sidebar.light-default.png`.

#### sidebar-group-label.light

Sidebar group label.

Page: dashboard. Selector: `leaf "Tools"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 204 x 35 |
| Padding | 16px 12px 4px 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 10px/15px 400 |
| Letter spacing | 0.5px |
| Colour | #737373 |
| Transition | none |
| How | at rest |

Crops: `sidebar-group-label.light-default.png`.

#### nav-item-active.light

Nav item, current.

Page: dashboard. Selector: `a[href="/dashboard"] (Tokens)`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 204 x 32 | = |
| Padding | 6px 8px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #e5e5e5 @ 0.7 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 13px/19.5px 500 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Text node | span.truncate: ui-sans-serif 13px/19.5px 500, #0a0a0a | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 15 x 15, colour #0a0a0a | = |
| Painted layers | a.flex.items-center 204.0x32.0 bg #e5e5e5 @ 0.7 r 8px | = |
| How | at rest | Shift+Tab, Tab |

Crops: `nav-item-active.light-default.png`, `nav-item-active.light-focus-visible.png`.

#### nav-item.light

Nav item.

Page: dashboard. Selector: `a[href="/sessions"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 204 x 32 | = | = | = |
| Padding | 6px 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #e5e5e5 @ 0.5 | = | #e5e5e5 @ 0.5 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 13px/19.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #525252 | #0a0a0a | = | #0a0a0a |
| Text node | span.truncate: ui-sans-serif 13px/19.5px 400, #525252 | span.truncate: ui-sans-serif 13px/19.5px 400, #0a0a0a | = | span.truncate: ui-sans-serif 13px/19.5px 400, #0a0a0a |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 15 x 15, colour #525252 | 15 x 15, colour #0a0a0a | = | 15 x 15, colour #0a0a0a |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.flex.items-center 204.0x32.0 bg #e5e5e5 @ 0.5 r 8px | = | a.flex.items-center 204.0x32.0 bg #e5e5e5 @ 0.5 r 8px |

Crops: `nav-item.light-default.png`, `nav-item.light-hover.png`, `nav-item.light-focus-visible.png`, `nav-item.light-pressed.png`.

#### nav-icon.light

Nav icon. Lucide History at the nav size.

Page: dashboard. Selector: `a[href="/sessions"] svg`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 15 x 15 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 13px/19.5px 400 |
| Letter spacing | normal |
| Colour | #525252 |
| Transition | none |
| Cursor | pointer |
| Icon | 15 x 15, colour #525252 |
| How | at rest |

Crops: `nav-icon.light-default.png`.

#### content-panel.light

Content panel. The rounded panel the pages sit in, inset from the window edge on the page wash.

Page: dashboard. Selector: `first rounded, filled ancestor of main`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1208 x 880 |
| Padding | 0px |
| Border | 1px solid #e5e5e5 |
| Radius | 16px |
| Background | #fafafa |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span.flex.items-center: ui-sans-serif 9px/13.5px 600, #ffffff @ 0.9, ls -0.225px |
| Transition | none |
| Icon | 0 x 0, colour #525252 |
| Painted layers | div.flex-1.min-h-0 1208.0x880.0 bg #fafafa border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; div.lg:hidden.flex 0.0x0.0 border B:1px solid #e5e5e5; div.relative.rounded-xl 375.3x259.5 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 16px; div.relative.h-24 341.3x96.0 bg #020617 r 12px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; div.absolute.-left-10 224.0x144.0 bg #4f46e5 @ 0.25 r 9999px; div.absolute.-right-8 192.0x128.0 bg #0ea5e9 @ 0.15 r 9999px |
| How | at rest |

Crops: none.

#### theme-toggle.light

Theme toggle.

Page: dashboard. Selector: `button[aria-label*=theme]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 44 x 44 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 9999px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 14 x 14, colour #525252 | 14 x 14, colour #0a0a0a |
| Painted layers | span.tt-sidebar-pill.tt-sidebar-theme-face 32.0x32.0 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px | span.tt-sidebar-pill.tt-sidebar-theme-face 32.0x32.0 bg #e5e5e5 @ 0.6 border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 9999px |
| How | at rest | mouse hover |

Crops: `theme-toggle.light-default.png`, `theme-toggle.light-hover.png`.

#### star-pill.light

GitHub star pill.

Page: dashboard. Selector: `a[href*=github]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 63.92 x 44 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 9999px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Text node | span: ui-sans-serif 12px/12px 500, #525252 | span: ui-sans-serif 12px/12px 500, #0a0a0a |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 12 x 12, colour #525252 | 12 x 12, colour #0a0a0a |
| Painted layers | span.tt-sidebar-pill.inline-flex 63.9x32.0 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px | span.tt-sidebar-pill.inline-flex 63.9x32.0 bg #e5e5e5 @ 0.6 border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 9999px |
| How | at rest | mouse hover |

Crops: `star-pill.light-default.png`, `star-pill.light-hover.png`.

### Buttons and segmented controls

#### period-tabs

Period tabs.

Page: dashboard. Selector: `[role=tablist][aria-label="Time period"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 599.27 x 28 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | button.shrink-0.whitespace-nowrap: ui-sans-serif 12px/16px 500, #d4d4d4 |
| Transition | none |
| Painted layers | button.shrink-0.whitespace-nowrap 60.8x28.0 bg #262626 r 8px |
| How | at rest |

Crops: `period-tabs-default.png`.

#### period-tab-selected

Period tab, selected.

Page: dashboard. Selector: `[role=tab][aria-selected=true]`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 60.8 x 28 | = |
| Padding | 6px 12px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #262626 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 12px/16px 500 | = |
| Letter spacing | normal | = |
| Colour | #fafafa | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.shrink-0.whitespace-nowrap 60.8x28.0 bg #262626 r 8px | = |
| How | at rest | Shift+Tab, Tab |

Crops: `period-tab-selected-default.png`, `period-tab-selected-focus-visible.png`.

#### period-tab

Period tab.

Page: dashboard. Selector: `[role=tab][aria-selected=false]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 46.08 x 28 | = | = |
| Padding | 6px 12px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | #262626 | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | ui-sans-serif 12px/16px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #d4d4d4 | #fafafa | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | keydown then focus() |
| Painted layers | - | button.shrink-0.whitespace-nowrap 46.1x28.0 bg #262626 r 8px | = |

Crops: `period-tab-default.png`, `period-tab-hover.png`, `period-tab-focus-visible.png`.

#### share-button

Secondary button. Outlined, as on Share. Measured, never pressed.

Page: dashboard. Selector: `button "Share"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 79.41 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #404040 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #171717 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #fafafa | = | = | = |
| Painted layers | button.inline-flex.items-center 79.4x32.0 bg #171717 border T:1px solid #404040 / R:1px solid #404040 / B:1px solid #404040 / L:1px solid #404040 r 8px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `share-button-default.png`, `share-button-hover.png`, `share-button-focus-visible.png`, `share-button-pressed.png`.

#### primary-button

Primary button. Solid near-black in light, near-white in dark. Measured, never pressed.

Page: dashboard. Selector: `button "Open in Mac app"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 121.02 x 28 | 124.65 x 28.84 | = | = |
| Padding | 6px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #fafafa | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.items-center 121.0x28.0 bg #fafafa r 8px | button.inline-flex.items-center 124.6x28.8 bg #fafafa r 8px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1.03, 0, 0, 1.03, 0, 0) | = | = |
| Opacity | - | 0.9 | = | 0.9 |

Crops: `primary-button-default.png`, `primary-button-hover.png`, `primary-button-focus-visible.png`, `primary-button-pressed.png`.

#### segmented-2d

Small segmented control. 2D / 3D switch on the heatmap.

Page: dashboard. Selector: `parent of button "2D"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 65.53 x 25 |
| Padding | 2px |
| Border | 1px solid #262626 |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 10px/15px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | button.px-2.py-0.5: ui-sans-serif 10px/15px 500, #fafafa |
| Transition | none |
| Painted layers | div.flex.rounded-md 65.5x25.0 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 8px; button.px-2.py-0.5 29.8x19.0 bg #262626 r 4px |
| How | at rest |

Crops: `segmented-2d-default.png`.

#### icon-button

Icon button. Refresh at the top right. Measured, never pressed.

Page: sessions. Selector: `main button[aria-label]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #262626 | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #262626 | = | #262626 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | OpenAI Sans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #a3a3a3 | #ffffff | = | #ffffff |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #a3a3a3 | 16 x 16, colour #ffffff | = | 16 x 16, colour #ffffff |
| Painted layers | button.inline-flex.h-9 36.0x36.0 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 12px | button.inline-flex.h-9 36.0x36.0 bg #262626 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 12px | button.inline-flex.h-9 36.0x36.0 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.h-9 36.0x36.0 bg #262626 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `icon-button-default.png`, `icon-button-hover.png`, `icon-button-focus-visible.png`, `icon-button-pressed.png`.

#### segmented

Segmented control.

Page: settings. Selector: `parent of button "Compact"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 126.88 x 34 |
| Padding | 2px |
| Border | 1px solid #262626 |
| Radius | 12px |
| Background | #171717 |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | span: OpenAI Sans 12px/16px 500, #ffffff |
| Transition | none |
| Painted layers | div.inline-flex.items-center 126.9x34.0 bg #171717 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 12px; button.inline-flex.items-center 76.3x28.0 bg #262626 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest |

Crops: `segmented-default.png`.

#### segment-selected

Segment, selected.

Page: settings. Selector: `button "Compact"`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 76.31 x 28 | = |
| Padding | 6px 12px | = |
| Gap | 6px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #262626 | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = |
| Outline | none | = |
| Font | OpenAI Sans 12px/16px 500 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | span: OpenAI Sans 12px/16px 500, #ffffff | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.inline-flex.items-center 76.3x28.0 bg #262626 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = |
| Ancestor paint | 1 up div.inline-flex.items-center bg #171717 | = |
| How | at rest | Shift+Tab, Tab |

Crops: `segment-selected-default.png`, `segment-selected-focus-visible.png`.

#### segment

Segment. Hovered and focused only; never pressed, so the setting is unchanged.

Page: settings. Selector: `button "Full"`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 44.56 x 28 | = | = |
| Padding | 6px 12px | = | = |
| Gap | 6px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | OpenAI Sans 12px/16px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #a3a3a3 | #ffffff | = |
| Text node | span: OpenAI Sans 12px/16px 500, #a3a3a3 | span: OpenAI Sans 12px/16px 500, #ffffff | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Ancestor paint | 1 up div.inline-flex.items-center bg #171717 | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `segment-default.png`, `segment-hover.png`, `segment-focus-visible.png`.

#### period-tabs.light

Period tabs.

Page: dashboard. Selector: `[role=tablist][aria-label="Time period"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 599.27 x 28 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | button.shrink-0.whitespace-nowrap: ui-sans-serif 12px/16px 500, #737373 |
| Transition | none |
| Painted layers | button.shrink-0.whitespace-nowrap 60.8x28.0 bg #f5f5f5 r 8px |
| How | at rest |

Crops: `period-tabs.light-default.png`.

#### period-tab-selected.light

Period tab, selected.

Page: dashboard. Selector: `[role=tab][aria-selected=true]`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 60.8 x 28 | = |
| Padding | 6px 12px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #f5f5f5 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 12px/16px 500 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.shrink-0.whitespace-nowrap 60.8x28.0 bg #f5f5f5 r 8px | = |
| How | at rest | Shift+Tab, Tab |

Crops: `period-tab-selected.light-default.png`, `period-tab-selected.light-focus-visible.png`.

#### period-tab.light

Period tab.

Page: dashboard. Selector: `[role=tab][aria-selected=false]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 46.08 x 28 | = | = |
| Padding | 6px 12px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | #fafafa | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | ui-sans-serif 12px/16px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #737373 | #0a0a0a | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | keydown then focus() |
| Painted layers | - | button.shrink-0.whitespace-nowrap 46.1x28.0 bg #fafafa r 8px | = |

Crops: `period-tab.light-default.png`, `period-tab.light-hover.png`, `period-tab.light-focus-visible.png`.

#### share-button.light

Secondary button. Outlined, as on Share. Measured, never pressed.

Page: dashboard. Selector: `button "Share"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 79.41 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #d4d4d4 | 1px solid #059669 | = | 1px solid #059669 |
| Radius | 8px | = | = | = |
| Background | #fafafa | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | #059669 | = | #059669 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #0a0a0a | 14 x 14, colour #059669 | = | 14 x 14, colour #059669 |
| Painted layers | button.inline-flex.items-center 79.4x32.0 bg #fafafa border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 8px | button.inline-flex.items-center 79.4x32.0 bg #fafafa border T:1px solid #059669 / R:1px solid #059669 / B:1px solid #059669 / L:1px solid #059669 r 8px | = | button.inline-flex.items-center 79.4x32.0 bg #fafafa border T:1px solid #059669 / R:1px solid #059669 / B:1px solid #059669 / L:1px solid #059669 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `share-button.light-default.png`, `share-button.light-hover.png`, `share-button.light-focus-visible.png`, `share-button.light-pressed.png`.

#### primary-button.light

Primary button. Solid near-black in light, near-white in dark. Measured, never pressed.

Page: dashboard. Selector: `button "Open in Mac app"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 121.02 x 28 | 124.65 x 28.84 | = | = |
| Padding | 6px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #171717 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.items-center 121.0x28.0 bg #171717 r 8px | button.inline-flex.items-center 124.6x28.8 bg #171717 r 8px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1.03, 0, 0, 1.03, 0, 0) | = | = |
| Opacity | - | 0.9 | = | 0.9 |

Crops: `primary-button.light-default.png`, `primary-button.light-hover.png`, `primary-button.light-focus-visible.png`, `primary-button.light-pressed.png`.

#### segmented-2d.light

Small segmented control. 2D / 3D switch on the heatmap.

Page: dashboard. Selector: `parent of button "2D"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 65.53 x 25 |
| Padding | 2px |
| Border | 1px solid #e5e5e5 |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 10px/15px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | button.px-2.py-0.5: ui-sans-serif 10px/15px 500, #0a0a0a |
| Transition | none |
| Painted layers | div.flex.rounded-md 65.5x25.0 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px; button.px-2.py-0.5 29.8x19.0 bg #f5f5f5 r 4px |
| How | at rest |

Crops: `segmented-2d.light-default.png`.

#### icon-button.light

Icon button. Refresh at the top right. Measured, never pressed.

Page: sessions. Selector: `main button[aria-label]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #e5e5e5 | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | OpenAI Sans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #525252 | #0a0a0a | = | #0a0a0a |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #525252 | 16 x 16, colour #0a0a0a | = | 16 x 16, colour #0a0a0a |
| Painted layers | button.inline-flex.h-9 36.0x36.0 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 12px | button.inline-flex.h-9 36.0x36.0 bg #f5f5f5 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 12px | button.inline-flex.h-9 36.0x36.0 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.h-9 36.0x36.0 bg #f5f5f5 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `icon-button.light-default.png`, `icon-button.light-hover.png`, `icon-button.light-focus-visible.png`, `icon-button.light-pressed.png`.

#### segmented.light

Segmented control.

Page: settings. Selector: `parent of button "Compact"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 126.88 x 34 |
| Padding | 2px |
| Border | 1px solid #e5e5e5 |
| Radius | 12px |
| Background | #fafafa |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span: OpenAI Sans 12px/16px 500, #0a0a0a |
| Transition | none |
| Painted layers | div.inline-flex.items-center 126.9x34.0 bg #fafafa border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 12px; button.inline-flex.items-center 76.3x28.0 bg #ffffff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest |

Crops: `segmented.light-default.png`.

#### segment-selected.light

Segment, selected.

Page: settings. Selector: `button "Compact"`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 76.31 x 28 | = |
| Padding | 6px 12px | = |
| Gap | 6px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = |
| Outline | none | = |
| Font | OpenAI Sans 12px/16px 500 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Text node | span: OpenAI Sans 12px/16px 500, #0a0a0a | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.inline-flex.items-center 76.3x28.0 bg #ffffff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = |
| Ancestor paint | 1 up div.inline-flex.items-center bg #fafafa | = |
| How | at rest | Shift+Tab, Tab |

Crops: `segment-selected.light-default.png`, `segment-selected.light-focus-visible.png`.

#### segment.light

Segment. Hovered and focused only; never pressed, so the setting is unchanged.

Page: settings. Selector: `button "Full"`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 44.56 x 28 | = | = |
| Padding | 6px 12px | = | = |
| Gap | 6px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | OpenAI Sans 12px/16px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #737373 | #0a0a0a | = |
| Text node | span: OpenAI Sans 12px/16px 500, #737373 | span: OpenAI Sans 12px/16px 500, #0a0a0a | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Ancestor paint | 1 up div.inline-flex.items-center bg #fafafa | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `segment.light-default.png`, `segment.light-hover.png`, `segment.light-focus-visible.png`.

### Tokens page

#### hero-label

Hero metric label. Set in uppercase by CSS (the text is "Total tokens").

Page: dashboard. Selector: `leaf "Total tokens"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 724.67 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 12px/16px 400 |
| Letter spacing | 0.6px |
| Colour | #d4d4d4 |
| Transition | none |
| How | at rest |

Crops: `hero-label-default.png`.

#### hero-metric

Hero metric. The one giant number: total tokens for the period.

Page: dashboard. Selector: `largest text in main`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 724.67 x 87 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 72px/72px 700 |
| Letter spacing | -1.8px |
| Colour | #fafafa |
| Text node | span: ui-sans-serif 72px/72px 700, #fafafa, ls -1.8px |
| Transition | none |
| Painted layers | span 133.1x0.0 image linear-gradient(#0a0a0a @ 0.98, #0a0a0a @ 0); span 133.1x0.0 image linear-gradient(to top, #0a0a0a @ 0.98, #0a0a0a @ 0); div.mx-auto.h-[58px] 0.0x0.0 bg #262626 r 16px |
| How | at rest |

Crops: `hero-metric-default.png`.

#### hero-cost

Hero cost. Cost under the hero number, in the brand green.

Page: dashboard. Selector: `text matching $n.nn`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 133.09 x 28 |
| Padding | 0px |
| Gap | 6px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 20px/28px 700 |
| Letter spacing | normal |
| Colour | #059669 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 16 x 16, colour #059669 |
| How | at rest |

Crops: `hero-cost-default.png`.

#### provider-tile

Provider share tile.

Page: dashboard. Selector: `tile holding "CLAUDE"`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 172.17 x 96.5 | = |
| Padding | 12px | = |
| Border | 1px solid #404040 | 1px solid #525252 |
| Radius | 12px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #fafafa | = |
| Text node | span.text-sm.font-medium: ui-sans-serif 14px/20px 500, #fafafa | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.min-w-0.text-left 172.2x96.5 border T:1px solid #404040 / R:1px solid #404040 / B:1px solid #404040 / L:1px solid #404040 r 12px | button.min-w-0.text-left 172.2x96.5 border T:1px solid #525252 / R:1px solid #525252 / B:1px solid #525252 / L:1px solid #525252 r 12px |
| How | at rest | mouse hover |

Crops: `provider-tile-default.png`, `provider-tile-hover.png`.

#### provider-tile-all

Provider share tile, all.

Page: dashboard. Selector: `tile holding "All"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 172.16 x 96.5 |
| Padding | 12px |
| Border | 1px solid #404040 |
| Radius | 12px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | span.text-sm.font-medium: ui-sans-serif 14px/20px 500, #fafafa |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 15 x 15, colour #fafafa |
| Painted layers | button.min-w-0.text-left 172.2x96.5 border T:1px solid #404040 / R:1px solid #404040 / B:1px solid #404040 / L:1px solid #404040 r 12px |
| How | at rest |

Crops: `provider-tile-all-default.png`.

#### stat-chip

Stat chip. A small filled tile: value over a caption (7d, 30d, avg, convs).

Page: dashboard. Selector: `parent of "7d"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 77.33 x 53 |
| Padding | 8px |
| Border | none |
| Radius | 12px |
| Background | #262626 |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | span.w-full.min-w-0: ui-sans-serif 14px/20px 600, #fafafa |
| Transition | none |
| Painted layers | div.min-w-0.flex 77.3x53.0 bg #262626 r 12px |
| How | at rest |

Crops: `stat-chip-default.png`.

#### card-title

Card title (legacy, uppercase). Older cards title themselves in small tracked uppercase.

Page: dashboard. Selector: `leaf "Activity heatmap"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 138.94 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 14px/20px 500 |
| Letter spacing | 0.35px |
| Colour | #d4d4d4 |
| Transition | none |
| How | at rest |

Crops: `card-title-default.png`.

#### heatmap-cell

Heatmap cell, busiest.

Page: dashboard. Selector: `span.rounded-[2px] whose fill is farthest from the empty fill`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 12 x 12 | 15 x 15 |
| Padding | 0px | = |
| Border | none | = |
| Radius | 2px | = |
| Background | #34d399 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #fafafa | = |
| Transition | transform 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | span.rounded-[2px].transition-transform 12.0x12.0 bg #34d399 r 2px | span.rounded-[2px].transition-transform 15.0x15.0 bg #34d399 r 2px |
| How | at rest | mouse hover |
| Transform | - | matrix(1.25, 0, 0, 1.25, 0, 0) |

Crops: `heatmap-cell-default.png`, `heatmap-cell-hover.png`.

#### heatmap-cell-empty

Heatmap cell, empty.

Page: dashboard. Selector: `span.rounded-[2px] with the least saturated fill`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 12 x 12 |
| Padding | 0px |
| Border | none |
| Radius | 2px |
| Background | #121212 |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | transform 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | span.rounded-[2px].transition-transform 12.0x12.0 bg #121212 r 2px |
| How | at rest |

Crops: `heatmap-cell-empty-default.png`.

#### cost-button

Hero cost button. The cost under the hero number is a button that opens the cost breakdown.

Page: dashboard. Selector: `button[aria-label="View cost breakdown"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 133.09 x 28 | = | = |
| Padding | 0px | = | = |
| Gap | 6px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | ui-sans-serif 20px/28px 700 | = | = |
| Letter spacing | normal | = | = |
| Colour | #059669 | #10b981 | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #059669 | 16 x 16, colour #10b981 | = |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `cost-button-default.png`, `cost-button-hover.png`, `cost-button-focus-visible.png`.

#### hero-label.light

Hero metric label. Set in uppercase by CSS (the text is "Total tokens").

Page: dashboard. Selector: `leaf "Total tokens"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 724.67 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 12px/16px 400 |
| Letter spacing | 0.6px |
| Colour | #737373 |
| Transition | none |
| How | at rest |

Crops: `hero-label.light-default.png`.

#### hero-metric.light

Hero metric. The one giant number: total tokens for the period.

Page: dashboard. Selector: `largest text in main`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 724.67 x 87 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 72px/72px 700 |
| Letter spacing | -1.8px |
| Colour | #0a0a0a |
| Text node | span: ui-sans-serif 72px/72px 700, #0a0a0a, ls -1.8px |
| Transition | none |
| Painted layers | span 133.1x8.0 image linear-gradient(#ffffff @ 0.96, #ffffff @ 0); span 133.1x8.0 image linear-gradient(to top, #ffffff @ 0.96, #ffffff @ 0); div.mx-auto.h-[58px] 0.0x0.0 bg #f5f5f5 r 16px |
| How | at rest |

Crops: `hero-metric.light-default.png`.

#### hero-cost.light

Hero cost. Cost under the hero number, in the brand green.

Page: dashboard. Selector: `text matching $n.nn`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 133.98 x 28 |
| Padding | 0px |
| Gap | 6px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 20px/28px 700 |
| Letter spacing | normal |
| Colour | #059669 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 16 x 16, colour #059669 |
| How | at rest |

Crops: `hero-cost.light-default.png`.

#### provider-tile.light

Provider share tile.

Page: dashboard. Selector: `tile holding "CLAUDE"`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 172.17 x 96.5 | = |
| Padding | 12px | = |
| Border | 1px solid #e5e5e5 | 1px solid #d4d4d4 |
| Radius | 12px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Text node | span.text-sm.font-medium: ui-sans-serif 14px/20px 500, #0a0a0a | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.min-w-0.text-left 172.2x96.5 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 12px | button.min-w-0.text-left 172.2x96.5 border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 12px |
| How | at rest | mouse hover |

Crops: `provider-tile.light-default.png`, `provider-tile.light-hover.png`.

#### provider-tile-all.light

Provider share tile, all.

Page: dashboard. Selector: `tile holding "All"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 172.16 x 96.5 |
| Padding | 12px |
| Border | 1px solid #e5e5e5 |
| Radius | 12px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span.text-sm.font-medium: ui-sans-serif 14px/20px 500, #0a0a0a |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 15 x 15, colour #059669 |
| Painted layers | button.min-w-0.text-left 172.2x96.5 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 12px |
| How | at rest |

Crops: `provider-tile-all.light-default.png`.

#### stat-chip.light

Stat chip. A small filled tile: value over a caption (7d, 30d, avg, convs).

Page: dashboard. Selector: `parent of "7d"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 77.33 x 53 |
| Padding | 8px |
| Border | none |
| Radius | 12px |
| Background | #fafafa |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span.w-full.min-w-0: ui-sans-serif 14px/20px 600, #0a0a0a |
| Transition | none |
| Painted layers | div.min-w-0.flex 77.3x53.0 bg #fafafa r 12px |
| How | at rest |

Crops: `stat-chip.light-default.png`.

#### card-title.light

Card title (legacy, uppercase). Older cards title themselves in small tracked uppercase.

Page: dashboard. Selector: `leaf "Activity heatmap"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 138.94 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 14px/20px 500 |
| Letter spacing | 0.35px |
| Colour | #737373 |
| Transition | none |
| How | at rest |

Crops: `card-title.light-default.png`.

#### heatmap-cell.light

Heatmap cell, busiest.

Page: dashboard. Selector: `span.rounded-[2px] whose fill is farthest from the empty fill`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 12 x 12 | 15 x 15 |
| Padding | 0px | = |
| Border | none | = |
| Radius | 2px | = |
| Background | #10b981 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Transition | transform 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | span.rounded-[2px].transition-transform 12.0x12.0 bg #10b981 r 2px | span.rounded-[2px].transition-transform 15.0x15.0 bg #10b981 r 2px |
| How | at rest | mouse hover |
| Transform | - | matrix(1.25, 0, 0, 1.25, 0, 0) |

Crops: `heatmap-cell.light-default.png`, `heatmap-cell.light-hover.png`.

#### heatmap-cell-empty.light

Heatmap cell, empty.

Page: dashboard. Selector: `span.rounded-[2px] with the least saturated fill`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 12 x 12 |
| Padding | 0px |
| Border | none |
| Radius | 2px |
| Background | #ebedf0 |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Transition | transform 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | span.rounded-[2px].transition-transform 12.0x12.0 bg #ebedf0 r 2px |
| How | at rest |

Crops: `heatmap-cell-empty.light-default.png`.

#### cost-button.light

Hero cost button. The cost under the hero number is a button that opens the cost breakdown.

Page: dashboard. Selector: `button[aria-label="View cost breakdown"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 133.98 x 28 | = | = |
| Padding | 0px | = | = |
| Gap | 6px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | ui-sans-serif 20px/28px 700 | = | = |
| Letter spacing | normal | = | = |
| Colour | #059669 | #047857 | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #059669 | 16 x 16, colour #047857 | = |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `cost-button.light-default.png`, `cost-button.light-hover.png`, `cost-button.light-focus-visible.png`.

#### card

Card. The Activity heatmap card: the shared card surface.

Page: dashboard. Selector: `card around "Activity heatmap"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 375.33 x 231 |
| Padding | 20px |
| Border | 1px solid #262626 |
| Radius | 16px |
| Background | #171717 |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | h3.text-sm.font-medium: ui-sans-serif 14px/20px 500, #d4d4d4, ls 0.35px |
| Transition | none |
| Painted layers | div.relative.rounded-xl 375.3x231.0 bg #171717 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 16px; div.flex.rounded-md 65.5x25.0 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 8px; button.px-2.py-0.5 29.8x19.0 bg #262626 r 4px; div.grid.text-[10px] 26.0x102.0 bg #171717; span.rounded-[2px].transition-transform 12.0x12.0 bg #121212 r 2px; span.rounded-[2px].transition-transform 12.0x12.0 bg #121212 r 2px |
| How | at rest |

Crops: `card-default.png`.

#### card.light

Card. The Activity heatmap card: the shared card surface.

Page: dashboard. Selector: `card around "Activity heatmap"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 375.33 x 231 |
| Padding | 20px |
| Border | 1px solid #e5e5e5 |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | h3.text-sm.font-medium: ui-sans-serif 14px/20px 500, #737373, ls 0.35px |
| Transition | none |
| Painted layers | div.relative.rounded-xl 375.3x231.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 16px; div.flex.rounded-md 65.5x25.0 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px; button.px-2.py-0.5 29.8x19.0 bg #f5f5f5 r 4px; div.grid.text-[10px] 26.0x102.0 bg #ffffff; span.rounded-[2px].transition-transform 12.0x12.0 bg #ebedf0 r 2px; span.rounded-[2px].transition-transform 12.0x12.0 bg #ebedf0 r 2px |
| How | at rest |

Crops: `card.light-default.png`.

### Badges, tooltips and status

#### beta-badge

Badge.

Page: dashboard. Selector: `leaf "BETA"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 31.57 x 14.4 |
| Padding | 2px 6px |
| Border | none |
| Radius | 4px |
| Background | #262626 @ 0.8 |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 8px/12px 600 |
| Letter spacing | 0.4px |
| Colour | #a3a3a3 |
| Transition | none |
| Transform | matrix(0.9, 0, 0, 0.9, 0, 0) |
| Painted layers | span.px-1.5.py-0.5 31.6x14.4 bg #262626 @ 0.8 r 4px |
| How | at rest |

Crops: `beta-badge-default.png`.

#### dialog

Dialog (cost breakdown). Opened by the hero cost button, closed with Escape.

Page: dashboard. Selector: `[role=dialog]`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 460 x 868 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #0a0a0a |
| Box shadow | #ffffff 0px 0px 0px 0px, #262626 0px 0px 0px 1px, #000000 @ 0.65 0px 20px 60px -10px |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | p.text-label.uppercase: -apple-system 11px/14.3px 600, #a3a3a3, ls 1.32px |
| Transition | opacity, transform 0.22s, 0.26s cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1) delay 0s, 0s |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 16 x 16, colour #a3a3a3 |
| Painted layers | div.cost-modal-popup.relative 460.0x868.0 bg #0a0a0a r 16px shadow #ffffff 0px 0px 0px 0px, #262626 0px 0px 0px 1px, #000000 @ 0.65 0px 20px 60px -10px; div.flex.items-center 436.0x31.3 border B:1px solid #262626 |
| How | at rest |

Crops: `dialog-open.png`.

#### status-badge

Status badge. STALE / RE-AUTH pill with a coloured dot.

Page: limits. Selector: `pill reading STALE`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 101.11 x 19.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | span.inline-flex.items-center: OpenAI Sans 9px/13.5px 600, #a3a3a3, ls 0.45px |
| Transition | none |
| Cursor | help |
| Painted layers | span.inline-flex.items-center 101.1x19.5 bg #262626 border T:1px solid #404040 @ 0.6 / R:1px solid #404040 @ 0.6 / B:1px solid #404040 @ 0.6 / L:1px solid #404040 @ 0.6 r 9999px; span.h-1.5.w-1.5 6.0x6.0 bg #f59e0b r 9999px; span.pointer-events-none.absolute 182.4x56.0 bg #262626 border T:1px solid #404040 / R:1px solid #404040 / B:1px solid #404040 / L:1px solid #404040 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px; span.absolute.left-1/2 7.6x7.6 border T:4px solid #262626 / R:4px solid #000000 @ 0 / B:4px solid #000000 @ 0 / L:4px solid #000000 @ 0 |
| How | at rest |

Crops: `status-badge-default.png`.

#### status-row

Service status row.

Page: status. Selector: `row around "Claude"`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 544 x 130 | = |
| Padding | 20px | = |
| Border | 1px solid #262626 | 1px solid #404040 |
| Radius | 16px | = |
| Background | #171717 | #262626 @ 0.6 |
| Box shadow | none | = |
| Outline | none | = |
| Font | OpenAI Sans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #fafafa | = |
| Text node | span.font-medium.text-sm: OpenAI Sans 16px/24px 500, #fafafa | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #a3a3a3 | 16 x 16, colour #ffffff |
| Painted layers | a.group.block 544.0x130.0 bg #171717 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 16px; span.absolute.inline-flex 16.0x16.0 bg #eab308 r 9999px; span.relative.inline-flex 8.0x8.0 bg #eab308 r 9999px | a.group.block 544.0x130.0 bg #262626 @ 0.6 border T:1px solid #404040 / R:1px solid #404040 / B:1px solid #404040 / L:1px solid #404040 r 16px; span.absolute.inline-flex 16.0x16.0 bg #eab308 r 9999px; span.relative.inline-flex 8.0x8.0 bg #eab308 r 9999px |
| How | at rest | mouse hover |

Crops: `status-row-default.png`, `status-row-hover.png`.

#### beta-badge.light

Badge.

Page: dashboard. Selector: `leaf "BETA"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 31.57 x 14.4 |
| Padding | 2px 6px |
| Border | none |
| Radius | 4px |
| Background | #f5f5f5 |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 8px/12px 600 |
| Letter spacing | 0.4px |
| Colour | #737373 |
| Transition | none |
| Transform | matrix(0.9, 0, 0, 0.9, 0, 0) |
| Painted layers | span.px-1.5.py-0.5 31.6x14.4 bg #f5f5f5 r 4px |
| How | at rest |

Crops: `beta-badge.light-default.png`.

#### dialog.light

Dialog (cost breakdown). Opened by the hero cost button, closed with Escape.

Page: dashboard. Selector: `[role=dialog]`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 460 x 868 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 1px, #000000 @ 0.25 0px 20px 60px -20px |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | p.text-label.uppercase: -apple-system 11px/14.3px 600, #737373, ls 1.32px |
| Transition | opacity, transform 0.22s, 0.26s cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1) delay 0s, 0s |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 16 x 16, colour #737373 |
| Painted layers | div.cost-modal-popup.relative 460.0x868.0 bg #ffffff r 16px shadow #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 1px, #000000 @ 0.25 0px 20px 60px -20px; div.flex.items-center 436.0x31.3 border B:1px solid #e5e5e5 |
| How | at rest |

Crops: `dialog.light-open.png`.

#### status-badge.light

Status badge. STALE / RE-AUTH pill with a coloured dot.

Page: limits. Selector: `pill reading STALE`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 101.11 x 19.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span.inline-flex.items-center: OpenAI Sans 9px/13.5px 600, #737373, ls 0.45px |
| Transition | none |
| Cursor | help |
| Painted layers | span.inline-flex.items-center 101.1x19.5 bg #fafafa border T:1px solid #e5e5e5 @ 0.6 / R:1px solid #e5e5e5 @ 0.6 / B:1px solid #e5e5e5 @ 0.6 / L:1px solid #e5e5e5 @ 0.6 r 9999px; span.h-1.5.w-1.5 6.0x6.0 bg #f59e0b r 9999px; span.pointer-events-none.absolute 182.4x56.0 bg #171717 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px; span.absolute.left-1/2 7.6x7.6 border T:4px solid #171717 / R:4px solid #000000 @ 0 / B:4px solid #000000 @ 0 / L:4px solid #000000 @ 0 |
| How | at rest |

Crops: `status-badge.light-default.png`.

#### status-row.light

Service status row.

Page: status. Selector: `row around "Claude"`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 544 x 130 | = |
| Padding | 20px | = |
| Border | 1px solid #e5e5e5 | 1px solid #d4d4d4 |
| Radius | 16px | = |
| Background | #ffffff | #fafafa |
| Box shadow | none | = |
| Outline | none | = |
| Font | OpenAI Sans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Text node | span.font-medium.text-sm: OpenAI Sans 16px/24px 500, #0a0a0a | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #a3a3a3 | 16 x 16, colour #0a0a0a |
| Painted layers | a.group.block 544.0x130.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 16px; span.absolute.inline-flex 15.8x15.8 bg #eab308 r 9999px; span.relative.inline-flex 8.0x8.0 bg #eab308 r 9999px | a.group.block 544.0x130.0 bg #fafafa border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 16px; span.absolute.inline-flex 15.5x15.5 bg #eab308 r 9999px; span.relative.inline-flex 8.0x8.0 bg #eab308 r 9999px |
| How | at rest | mouse hover |

Crops: `status-row.light-default.png`, `status-row.light-hover.png`.

### Tables and lists

#### table-tab-selected

Table tab, selected.

Page: dashboard. Selector: `button "Daily Breakdown"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 119.97 x 28 |
| Padding | 6px 12px |
| Border | none |
| Radius | 4px |
| Background | #262626 |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 12px/16px 500 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | button.text-xs.font-medium 120.0x28.0 bg #262626 r 4px |
| How | at rest |

Crops: `table-tab-selected-default.png`.

#### table-tab

Table tab.

Page: dashboard. Selector: `button "Project Usage"`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 105.06 x 28 | = |
| Padding | 6px 12px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | transparent | #262626 @ 0.5 |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 12px/16px 500 | = |
| Letter spacing | normal | = |
| Colour | #d4d4d4 | #fafafa |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |
| Painted layers | - | button.text-xs.font-medium 105.1x28.0 bg #262626 @ 0.5 r 4px |

Crops: `table-tab-default.png`, `table-tab-hover.png`.

#### table-header

Table header cell.

Page: dashboard. Selector: `thead th:nth(1)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 102.94 x 33.3 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #171717 |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 700 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | span: ui-sans-serif 12px/16.8px 500, #d4d4d4, ls 0.12px |
| Transition | none |
| Painted layers | th.text-left.p-0 102.9x33.3 bg #171717 |
| How | at rest |

Crops: `table-header-default.png`.

#### table-cell

Table cell (numeric).

Page: dashboard. Selector: `tbody td:nth(1)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 102.94 x 38 |
| Padding | 8px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 14px/21px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | span: ui-sans-serif 14px/21px 400, #fafafa |
| Transition | none |
| How | at rest |

Crops: `table-cell-default.png`.

#### table-row

Table row.

Page: dashboard. Selector: `tbody tr:nth(1)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 756.67 x 38 | = |
| Padding | 0px | = |
| Border | T: none; R: none; B: 1px solid #262626; L: none | = |
| Radius | 0px | = |
| Background | transparent | #262626 @ 0.5 |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #fafafa | = |
| Text node | td.px-2.5.sm:px-4: ui-sans-serif 14px/21px 400, #d4d4d4 | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Painted layers | tr.border-b.border-oai-gray-100 756.7x38.0 border B:1px solid #262626 | tr.border-b.border-oai-gray-100 756.7x38.0 bg #262626 @ 0.5 border B:1px solid #262626 |
| How | at rest | mouse hover |

Crops: `table-row-default.png`, `table-row-hover.png`.

#### summary-strip

Summary strip. Four figures in one bordered box, split by rules.

Page: sessions. Selector: `box around "Matching sessions"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1070 x 48 |
| Padding | 0px |
| Gap | 12px normal |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | dt.text-xs.text-oai-gray-500: OpenAI Sans 12px/16px 400, #a3a3a3 |
| Transition | none |
| Icon | 14 x 14, colour #a3a3a3 |
| Painted layers | div 267.5x48.0 border L:1px solid #262626; div 267.5x48.0 border L:1px solid #262626; div 267.5x48.0 border L:1px solid #262626 |
| How | at rest |

Crops: `summary-strip-default.png`.

#### summary-label

Summary label.

Page: sessions. Selector: `leaf "Matching sessions"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 267.5 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 12px/16px 400 |
| Letter spacing | normal |
| Colour | #a3a3a3 |
| Transition | none |
| How | at rest |

Crops: `summary-label-default.png`.

#### list-header

List column header.

Page: sessions. Selector: `leaf "Session / project"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 760 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 12px/16px 400 |
| Letter spacing | normal |
| Colour | #a3a3a3 |
| Transition | none |
| How | at rest |

Crops: `list-header-default.png`.

#### list-row

Session row.

Page: sessions. Selector: `.sessions-row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1104 x 63 | = |
| Padding | 12px 0px | = |
| Gap | 16px | = |
| Border | T: 1px solid #262626; R: none; B: none; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | OpenAI Sans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #fafafa | = |
| Text node | button.sessions-row-title.block: OpenAI Sans 14px/20px 500, #ffffff | = |
| Transition | none | = |
| Icon | 16 x 16, colour #a3a3a3 | = |
| Painted layers | li.sessions-row.sessions-row-grid 1104.0x63.0 border T:1px solid #262626; div.pointer-events-none.absolute 68.8x28.4 bg #171717 @ 0.9 border T:1px solid #262626 @ 0.5 / R:1px solid #262626 @ 0.5 / B:1px solid #262626 @ 0.5 / L:1px solid #262626 @ 0.5 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px | = |
| How | at rest | mouse hover |

Crops: `list-row-default.png`, `list-row-hover.png`.

#### list-row-title

Session row title.

Page: sessions. Selector: `.sessions-row-title`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 61.42 x 20 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 4px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | OpenAI Sans 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | button.sessions-row-title.block 61.4x20.0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |

Crops: `list-row-title-default.png`, `list-row-title-hover.png`, `list-row-title-focus-visible.png`.

#### table-tab-selected.light

Table tab, selected.

Page: dashboard. Selector: `button "Daily Breakdown"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 119.97 x 28 |
| Padding | 6px 12px |
| Border | none |
| Radius | 4px |
| Background | #f5f5f5 |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 12px/16px 500 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | button.text-xs.font-medium 120.0x28.0 bg #f5f5f5 r 4px |
| How | at rest |

Crops: `table-tab-selected.light-default.png`.

#### table-tab.light

Table tab.

Page: dashboard. Selector: `button "Project Usage"`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 105.06 x 28 | = |
| Padding | 6px 12px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | transparent | #fafafa |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 12px/16px 500 | = |
| Letter spacing | normal | = |
| Colour | #737373 | #0a0a0a |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |
| Painted layers | - | button.text-xs.font-medium 105.1x28.0 bg #fafafa r 4px |

Crops: `table-tab.light-default.png`, `table-tab.light-hover.png`.

#### table-header.light

Table header cell.

Page: dashboard. Selector: `thead th:nth(1)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 102.94 x 33.3 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 700 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span: ui-sans-serif 12px/16.8px 500, #525252, ls 0.12px |
| Transition | none |
| Painted layers | th.text-left.p-0 102.9x33.3 bg #ffffff |
| How | at rest |

Crops: `table-header.light-default.png`.

#### table-cell.light

Table cell (numeric).

Page: dashboard. Selector: `tbody td:nth(1)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 102.94 x 38 |
| Padding | 8px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 14px/21px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span: ui-sans-serif 14px/21px 400, #0a0a0a |
| Transition | none |
| How | at rest |

Crops: `table-cell.light-default.png`.

#### table-row.light

Table row.

Page: dashboard. Selector: `tbody tr:nth(1)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 756.67 x 38 | = |
| Padding | 0px | = |
| Border | T: none; R: none; B: 1px solid #f5f5f5; L: none | = |
| Radius | 0px | = |
| Background | transparent | #fafafa @ 0.5 |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Text node | td.px-2.5.sm:px-4: ui-sans-serif 14px/21px 400, #737373 | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Painted layers | tr.border-b.border-oai-gray-100 756.7x38.0 border B:1px solid #f5f5f5 | tr.border-b.border-oai-gray-100 756.7x38.0 bg #fafafa @ 0.5 border B:1px solid #f5f5f5 |
| How | at rest | mouse hover |

Crops: `table-row.light-default.png`, `table-row.light-hover.png`.

#### summary-strip.light

Summary strip. Four figures in one bordered box, split by rules.

Page: sessions. Selector: `box around "Matching sessions"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1070 x 48 |
| Padding | 0px |
| Gap | 12px normal |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | dt.text-xs.text-oai-gray-500: OpenAI Sans 12px/16px 400, #737373 |
| Transition | none |
| Icon | 14 x 14, colour #737373 |
| Painted layers | div 267.5x48.0 border L:1px solid #e5e5e5; div 267.5x48.0 border L:1px solid #e5e5e5; div 267.5x48.0 border L:1px solid #e5e5e5 |
| How | at rest |

Crops: `summary-strip.light-default.png`.

#### summary-label.light

Summary label.

Page: sessions. Selector: `leaf "Matching sessions"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 267.5 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 12px/16px 400 |
| Letter spacing | normal |
| Colour | #737373 |
| Transition | none |
| How | at rest |

Crops: `summary-label.light-default.png`.

#### list-header.light

List column header.

Page: sessions. Selector: `leaf "Session / project"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 760 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 12px/16px 400 |
| Letter spacing | normal |
| Colour | #737373 |
| Transition | none |
| How | at rest |

Crops: `list-header.light-default.png`.

#### list-row.light

Session row.

Page: sessions. Selector: `.sessions-row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1104 x 63 | = |
| Padding | 12px 0px | = |
| Gap | 16px | = |
| Border | T: 1px solid #e5e5e5; R: none; B: none; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | OpenAI Sans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Text node | button.sessions-row-title.block: OpenAI Sans 14px/20px 500, #0a0a0a | = |
| Transition | none | = |
| Icon | 16 x 16, colour #737373 | = |
| Painted layers | li.sessions-row.sessions-row-grid 1104.0x63.0 border T:1px solid #e5e5e5; div.pointer-events-none.absolute 68.8x28.4 bg #ffffff @ 0.9 border T:1px solid #e5e5e5 @ 0.5 / R:1px solid #e5e5e5 @ 0.5 / B:1px solid #e5e5e5 @ 0.5 / L:1px solid #e5e5e5 @ 0.5 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px | = |
| How | at rest | mouse hover |

Crops: `list-row.light-default.png`, `list-row.light-hover.png`.

#### list-row-title.light

Session row title.

Page: sessions. Selector: `.sessions-row-title`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 61.42 x 20 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 4px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | OpenAI Sans 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0a0a0a | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | button.sessions-row-title.block 61.4x20.0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |

Crops: `list-row-title.light-default.png`, `list-row-title.light-hover.png`, `list-row-title.light-focus-visible.png`.

### Page header

#### page-title

Page title.

Page: sessions. Selector: `main h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 304.95 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 36px/40px 600 |
| Letter spacing | -0.9px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `page-title-default.png`.

#### page-subtitle

Page subtitle.

Page: sessions. Selector: `main h1 + p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 304.95 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #a3a3a3 |
| Transition | none |
| How | at rest |

Crops: `page-subtitle-default.png`.

#### page-title.light

Page title.

Page: sessions. Selector: `main h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 304.95 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 36px/40px 600 |
| Letter spacing | -0.9px |
| Colour | #0a0a0a |
| Transition | none |
| How | at rest |

Crops: `page-title.light-default.png`.

#### page-subtitle.light

Page subtitle.

Page: sessions. Selector: `main h1 + p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 304.95 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #737373 |
| Transition | none |
| How | at rest |

Crops: `page-subtitle.light-default.png`.

### Fields and selects

#### search-field

Search field.

Page: sessions. Selector: `input[placeholder^=Search] parent`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 400 x 36 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | OpenAI Sans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #fafafa | = |
| Transition | none | = |
| Painted layers | input.w-full.bg-oai-white 400.0x36.0 bg #171717 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 8px | = |
| How | at rest | mouse hover |

Crops: `search-field-default.png`, `search-field-hover.png`.

#### search-input

Search input. A model name was typed and deleted; nothing was sent.

Page: sessions. Selector: `input[placeholder^=Search]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 400 x 36 | = | = |
| Padding | 0px 48px 0px 40px | = | = |
| Border | 1px solid #262626 | = | = |
| Radius | 8px | = | = |
| Background | #171717 | = | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | OpenAI Sans 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #fafafa | = | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #a3a3a3, opacity 1 | = | = |
| Painted layers | input.w-full.bg-oai-white 400.0x36.0 bg #171717 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 8px | input.w-full.bg-oai-white 400.0x36.0 bg #171717 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | input.w-full.bg-oai-white 400.0x36.0 bg #171717 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field | typed "claude-opus", then deleted; nothing sent |

Crops: `search-input-default.png`, `search-input-focused.png`, `search-input-filled.png`.

#### select

Select button.

Page: sessions. Selector: `button holding "All tools"`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 168 x 36 | = | = |
| Padding | 0px 12px | = | = |
| Gap | 8px | = | = |
| Border | 1px solid #262626 | 1px solid #404040 | = |
| Radius | 6px | = | = |
| Background | #171717 | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | OpenAI Sans 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Text node | span.truncate: OpenAI Sans 14px/20px 400, #ffffff | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 14 x 14, colour #a3a3a3 | = | = |
| Painted layers | button.relative.inline-flex 168.0x36.0 bg #171717 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 6px | button.relative.inline-flex 168.0x36.0 bg #171717 border T:1px solid #404040 / R:1px solid #404040 / B:1px solid #404040 / L:1px solid #404040 r 6px | button.relative.inline-flex 168.0x36.0 bg #171717 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `select-default.png`, `select-hover.png`, `select-focus-visible.png`.

#### select-menu

Select menu.

Page: sessions. Selector: `[role=listbox]`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 158 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | div: -apple-system 12px/16px 400, #ffffff |
| Transition | none |
| Icon | 12 x 12, colour #d4d4d4 |
| Painted layers | div.flex.w-full 158.0x28.0 bg #262626 @ 0.7 r 12px; div.flex.w-full 158.0x28.0 r 12px outline 2px solid #000000 @ 0 offset 2px; div.flex.w-full 158.0x28.0 r 12px outline 2px solid #000000 @ 0 offset 2px; div.flex.w-full 158.0x28.0 r 12px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up div.max-h-[min(18rem,var(--available-height))].origin-[var(--transform-origin)] bg #171717 shadow #ffffff 0px 0px 0px 0px, #ffffff @ 0.05 0px 0px 0px 1px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px |
| How | at rest |

Crops: `select-menu-open.png`.

#### select-option-selected

Select option, selected.

Page: sessions. Selector: `first option`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 158 x 28 |
| Padding | 6px 24px 6px 6px |
| Gap | 6px |
| Border | none |
| Radius | 12px |
| Background | #262626 @ 0.7 |
| Box shadow | none |
| Outline | 2px solid #000000 @ 0 offset 2px |
| Font | -apple-system 12px/16px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div: -apple-system 12px/16px 400, #ffffff |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 12 x 12, colour #d4d4d4 |
| Painted layers | div.flex.w-full 158.0x28.0 bg #262626 @ 0.7 r 12px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 2 up div.max-h-[min(18rem,var(--available-height))].origin-[var(--transform-origin)] bg #171717 shadow #ffffff 0px 0px 0px 0px, #ffffff @ 0.05 0px 0px 0px 1px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px |
| How | at rest |

Crops: `select-option-selected-open.png`.

#### select-option

Select option.

Page: sessions. Selector: `second option`. States: open, hover.

| Property | open | hover |
|---|---|---|
| Size (w x h) | 158 x 28 | = |
| Padding | 6px 24px 6px 6px | = |
| Gap | 6px | = |
| Border | none | = |
| Radius | 12px | = |
| Background | transparent | #262626 @ 0.6 |
| Box shadow | none | = |
| Outline | 2px solid #000000 @ 0 offset 2px | none |
| Font | -apple-system 12px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #d4d4d4 | = |
| Text node | div: -apple-system 12px/16px 400, #d4d4d4 | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | div.flex.w-full 158.0x28.0 r 12px outline 2px solid #000000 @ 0 offset 2px | div.flex.w-full 158.0x28.0 bg #262626 @ 0.6 r 12px |
| Ancestor paint | 2 up div.max-h-[min(18rem,var(--available-height))].origin-[var(--transform-origin)] bg #171717 shadow #ffffff 0px 0px 0px 0px, #ffffff @ 0.05 0px 0px 0px 1px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px | = |
| How | at rest | mouse hover |

Crops: `select-option-open.png`, `select-option-hover.png`.

#### search-field.light

Search field.

Page: sessions. Selector: `input[placeholder^=Search] parent`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 400 x 36 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | OpenAI Sans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Transition | none | = |
| Painted layers | input.w-full.bg-oai-white 400.0x36.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px | = |
| How | at rest | mouse hover |

Crops: `search-field.light-default.png`, `search-field.light-hover.png`.

#### search-input.light

Search input. A model name was typed and deleted; nothing was sent.

Page: sessions. Selector: `input[placeholder^=Search]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 400 x 36 | = | = |
| Padding | 0px 48px 0px 40px | = | = |
| Border | 1px solid #e5e5e5 | = | = |
| Radius | 8px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | OpenAI Sans 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0a0a0a | = | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #737373, opacity 1 | = | = |
| Painted layers | input.w-full.bg-oai-white 400.0x36.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px | input.w-full.bg-oai-white 400.0x36.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | input.w-full.bg-oai-white 400.0x36.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field | typed "claude-opus", then deleted; nothing sent |

Crops: `search-input.light-default.png`, `search-input.light-focused.png`, `search-input.light-filled.png`.

#### select.light

Select button.

Page: sessions. Selector: `button holding "All tools"`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 168 x 36 | = | = |
| Padding | 0px 12px | = | = |
| Gap | 8px | = | = |
| Border | 1px solid #e5e5e5 | 1px solid #d4d4d4 | = |
| Radius | 6px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | OpenAI Sans 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0a0a0a | = | = |
| Text node | span.truncate: OpenAI Sans 14px/20px 400, #0a0a0a | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 14 x 14, colour #737373 | = | = |
| Painted layers | button.relative.inline-flex 168.0x36.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 6px | button.relative.inline-flex 168.0x36.0 bg #ffffff border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 6px | button.relative.inline-flex 168.0x36.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `select.light-default.png`, `select.light-hover.png`, `select.light-focus-visible.png`.

#### select-menu.light

Select menu.

Page: sessions. Selector: `[role=listbox]`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 158 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | div: -apple-system 12px/16px 400, #0a0a0a |
| Transition | none |
| Icon | 12 x 12, colour #737373 |
| Painted layers | div.flex.w-full 158.0x28.0 bg #f5f5f5 r 12px; div.flex.w-full 158.0x28.0 r 12px outline 2px solid #000000 @ 0 offset 2px; div.flex.w-full 158.0x28.0 r 12px outline 2px solid #000000 @ 0 offset 2px; div.flex.w-full 158.0x28.0 r 12px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up div.max-h-[min(18rem,var(--available-height))].origin-[var(--transform-origin)] bg #ffffff shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.04 0px 0px 0px 1px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px |
| How | at rest |

Crops: `select-menu.light-open.png`.

#### select-option-selected.light

Select option, selected.

Page: sessions. Selector: `first option`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 158 x 28 |
| Padding | 6px 24px 6px 6px |
| Gap | 6px |
| Border | none |
| Radius | 12px |
| Background | #f5f5f5 |
| Box shadow | none |
| Outline | 2px solid #000000 @ 0 offset 2px |
| Font | -apple-system 12px/16px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | div: -apple-system 12px/16px 400, #0a0a0a |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 12 x 12, colour #737373 |
| Painted layers | div.flex.w-full 158.0x28.0 bg #f5f5f5 r 12px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 2 up div.max-h-[min(18rem,var(--available-height))].origin-[var(--transform-origin)] bg #ffffff shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.04 0px 0px 0px 1px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px |
| How | at rest |

Crops: `select-option-selected.light-open.png`.

#### select-option.light

Select option.

Page: sessions. Selector: `second option`. States: open, hover.

| Property | open | hover |
|---|---|---|
| Size (w x h) | 158 x 28 | = |
| Padding | 6px 24px 6px 6px | = |
| Gap | 6px | = |
| Border | none | = |
| Radius | 12px | = |
| Background | transparent | #fafafa |
| Box shadow | none | = |
| Outline | 2px solid #000000 @ 0 offset 2px | none |
| Font | -apple-system 12px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #525252 | = |
| Text node | div: -apple-system 12px/16px 400, #525252 | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | div.flex.w-full 158.0x28.0 r 12px outline 2px solid #000000 @ 0 offset 2px | div.flex.w-full 158.0x28.0 bg #fafafa r 12px |
| Ancestor paint | 2 up div.max-h-[min(18rem,var(--available-height))].origin-[var(--transform-origin)] bg #ffffff shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.04 0px 0px 0px 1px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px | = |
| How | at rest | mouse hover |

Crops: `select-option.light-open.png`, `select-option.light-hover.png`.

### Limits

#### limits-card

Limits card.

Page: limits. Selector: `card around the "Usage limits" title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1104 x 2340.81 |
| Padding | 0px |
| Border | 1px solid #262626 |
| Radius | 16px |
| Background | #171717 |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | h3.text-sm.font-medium: OpenAI Sans 14px/20px 500, #d4d4d4, ls 0.35px |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 14 x 14, colour #fafafa |
| Painted layers | div.rounded-xl.border 1104.0x2340.8 bg #171717 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 16px; div.pointer-events-none.absolute 162.5x42.9 bg #171717 @ 0.9 border T:1px solid #262626 @ 0.5 / R:1px solid #262626 @ 0.5 / B:1px solid #262626 @ 0.5 / L:1px solid #262626 @ 0.5 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px; div.relative.flex-1 931.0x6.0 bg #404040 @ 0.5 r 9999px; div.bg-emerald-500.rounded-full 270.0x6.0 bg #10b981 r 9999px; div.absolute.top-0 6.0x6.0 bg #404040 @ 0.5; div.absolute.top-0 2.0x6.0 bg #10b981 |
| How | at rest |

Crops: none.

#### limits-title

Limits card title.

Page: limits. Selector: `leaf "Usage limits"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1062 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 14px/20px 500 |
| Letter spacing | 0.35px |
| Colour | #d4d4d4 |
| Transition | none |
| How | at rest |

Crops: `limits-title-default.png`.

#### usage-row

Usage row. Window label, a thin track with a pace tick, percent and time left.

Page: limits. Selector: `row around the first track`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1062 x 16.5 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | div.pointer-events-none.absolute: OpenAI Sans 10.5px/14.4375px 400, #e5e5e5 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.pointer-events-none.absolute 162.5x42.9 bg #171717 @ 0.9 border T:1px solid #262626 @ 0.5 / R:1px solid #262626 @ 0.5 / B:1px solid #262626 @ 0.5 / L:1px solid #262626 @ 0.5 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px; div.relative.flex-1 931.0x6.0 bg #404040 @ 0.5 r 9999px; div.bg-emerald-500.rounded-full 270.0x6.0 bg #10b981 r 9999px; div.absolute.top-0 6.0x6.0 bg #404040 @ 0.5; div.absolute.top-0 2.0x6.0 bg #10b981 |
| How | at rest |

Crops: `usage-row-default.png`.

#### usage-track

Usage track.

Page: limits. Selector: `first track`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 931 x 6 |
| Padding | 0px |
| Border | none |
| Radius | 9999px |
| Background | #404040 @ 0.5 |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.relative.flex-1 931.0x6.0 bg #404040 @ 0.5 r 9999px; div.bg-emerald-500.rounded-full 270.0x6.0 bg #10b981 r 9999px; div.absolute.top-0 6.0x6.0 bg #404040 @ 0.5; div.absolute.top-0 2.0x6.0 bg #10b981 |
| How | at rest |

Crops: `usage-track-default.png`.

#### usage-fill

Usage fill.

Page: limits. Selector: `its fill`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 269.98 x 6 |
| Padding | 0px |
| Border | none |
| Radius | 9999px |
| Background | #10b981 |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | width 0.5s cubic-bezier(0, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | div.bg-emerald-500.rounded-full 270.0x6.0 bg #10b981 r 9999px |
| Ancestor paint | 1 up div.relative.flex-1 bg #404040 @ 0.5 |
| How | at rest |

Crops: `usage-fill-default.png`.

#### code-block

Code block.

Page: limits. Selector: `main pre`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1040 x 51.38 |
| Padding | 6px 8px |
| Border | none |
| Radius | 4px |
| Background | #171717 @ 0.6 |
| Box shadow | none |
| Outline | none |
| Font | SF Mono 10.5px/13.125px 400 |
| Letter spacing | normal |
| Colour | #d4d4d4 |
| Transition | none |
| Cursor | pointer |
| Painted layers | pre.mt-1.5.overflow-x-auto 1040.0x51.4 bg #171717 @ 0.6 r 4px |
| Ancestor paint | 1 up div.mt-1.rounded-md bg #78350f @ 0.1 |
| How | at rest |

Crops: `code-block-default.png`.

#### limits-card.light

Limits card.

Page: limits. Selector: `card around the "Usage limits" title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1104 x 2340.81 |
| Padding | 0px |
| Border | 1px solid #e5e5e5 |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | h3.text-sm.font-medium: OpenAI Sans 14px/20px 500, #737373, ls 0.35px |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 14 x 14, colour #0a0a0a |
| Painted layers | div.rounded-xl.border 1104.0x2340.8 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 16px; div.pointer-events-none.absolute 162.5x42.9 bg #ffffff @ 0.9 border T:1px solid #e5e5e5 @ 0.5 / R:1px solid #e5e5e5 @ 0.5 / B:1px solid #e5e5e5 @ 0.5 / L:1px solid #e5e5e5 @ 0.5 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px; div.relative.flex-1 931.0x6.0 bg #f5f5f5 r 9999px; div.bg-emerald-500.rounded-full 270.0x6.0 bg #10b981 r 9999px; div.absolute.top-0 6.0x6.0 bg #f5f5f5; div.absolute.top-0 2.0x6.0 bg #10b981 |
| How | at rest |

Crops: none.

#### limits-title.light

Limits card title.

Page: limits. Selector: `leaf "Usage limits"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1062 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 14px/20px 500 |
| Letter spacing | 0.35px |
| Colour | #737373 |
| Transition | none |
| How | at rest |

Crops: `limits-title.light-default.png`.

#### usage-row.light

Usage row. Window label, a thin track with a pace tick, percent and time left.

Page: limits. Selector: `row around the first track`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1062 x 16.5 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | div.pointer-events-none.absolute: OpenAI Sans 10.5px/14.4375px 400, #404040 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.pointer-events-none.absolute 162.5x42.9 bg #ffffff @ 0.9 border T:1px solid #e5e5e5 @ 0.5 / R:1px solid #e5e5e5 @ 0.5 / B:1px solid #e5e5e5 @ 0.5 / L:1px solid #e5e5e5 @ 0.5 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px; div.relative.flex-1 931.0x6.0 bg #f5f5f5 r 9999px; div.bg-emerald-500.rounded-full 270.0x6.0 bg #10b981 r 9999px; div.absolute.top-0 6.0x6.0 bg #f5f5f5; div.absolute.top-0 2.0x6.0 bg #10b981 |
| How | at rest |

Crops: `usage-row.light-default.png`.

#### usage-track.light

Usage track.

Page: limits. Selector: `first track`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 931 x 6 |
| Padding | 0px |
| Border | none |
| Radius | 9999px |
| Background | #f5f5f5 |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.relative.flex-1 931.0x6.0 bg #f5f5f5 r 9999px; div.bg-emerald-500.rounded-full 270.0x6.0 bg #10b981 r 9999px; div.absolute.top-0 6.0x6.0 bg #f5f5f5; div.absolute.top-0 2.0x6.0 bg #10b981 |
| How | at rest |

Crops: `usage-track.light-default.png`.

#### usage-fill.light

Usage fill.

Page: limits. Selector: `its fill`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 269.98 x 6 |
| Padding | 0px |
| Border | none |
| Radius | 9999px |
| Background | #10b981 |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Transition | width 0.5s cubic-bezier(0, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | div.bg-emerald-500.rounded-full 270.0x6.0 bg #10b981 r 9999px |
| Ancestor paint | 1 up div.relative.flex-1 bg #f5f5f5 |
| How | at rest |

Crops: `usage-fill.light-default.png`.

#### code-block.light

Code block.

Page: limits. Selector: `main pre`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1040 x 51.38 |
| Padding | 6px 8px |
| Border | none |
| Radius | 4px |
| Background | #f5f5f5 |
| Box shadow | none |
| Outline | none |
| Font | SF Mono 10.5px/13.125px 400 |
| Letter spacing | normal |
| Colour | #525252 |
| Transition | none |
| Cursor | pointer |
| Painted layers | pre.mt-1.5.overflow-x-auto 1040.0x51.4 bg #f5f5f5 r 4px |
| Ancestor paint | 1 up div.mt-1.rounded-md bg #fffbeb @ 0.5 |
| How | at rest |

Crops: `code-block.light-default.png`.

### Settings

#### subnav-item-active

Settings nav item, current.

Page: settings. Selector: `button "Appearance"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 176 x 40 |
| Padding | 8px 12px |
| Gap | 8px |
| Border | none |
| Radius | 8px |
| Background | #262626 |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 14px/20px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.truncate: OpenAI Sans 14px/20px 500, #ffffff |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | button.inline-flex.min-h-10 176.0x40.0 bg #262626 r 8px |
| How | at rest |

Crops: `subnav-item-active-default.png`.

#### subnav-item

Settings nav item.

Page: settings. Selector: `button "Account"`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 176 x 40 | = | = |
| Padding | 8px 12px | = | = |
| Gap | 8px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | #171717 | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | OpenAI Sans 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #a3a3a3 | #e5e5e5 | = |
| Text node | span.truncate: OpenAI Sans 14px/20px 500, #a3a3a3 | span.truncate: OpenAI Sans 14px/20px 500, #e5e5e5 | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #737373 | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | button.inline-flex.min-h-10 176.0x40.0 bg #171717 r 8px | button.inline-flex.min-h-10 176.0x40.0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |

Crops: `subnav-item-default.png`, `subnav-item-hover.png`, `subnav-item-focus-visible.png`.

#### subnav-group-label

Settings nav group label.

Page: settings. Selector: `leaf "App"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 176 x 19 |
| Padding | 0px 12px 4px 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 10px/15px 600 |
| Letter spacing | 1.6px |
| Colour | #737373 |
| Transition | none |
| How | at rest |

Crops: `subnav-group-label-default.png`.

#### section-title

Section title.

Page: settings. Selector: `main h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 20px/28px 600 |
| Letter spacing | -0.5px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### settings-card

Settings card.

Page: settings. Selector: `card around "Theme"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 726 x 377 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | div.text-sm.text-oai-gray-900: OpenAI Sans 14px/20px 400, #e5e5e5 |
| Transition | none |
| Icon | 14 x 14, colour #a3a3a3 |
| Painted layers | div.inline-flex.items-center 237.3x34.0 bg #171717 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 12px; button.inline-flex.items-center 86.9x28.0 bg #262626 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; div.flex.flex-col 726.0x63.0 border T:1px solid #262626 @ 0.6; button.relative.inline-flex 108.9x30.0 bg #171717 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 12px; input 1.0x1.0 bg #3b3b3b; div.flex.flex-col 726.0x63.0 border T:1px solid #262626 @ 0.6 |
| How | at rest |

Crops: none.

#### setting-label

Setting label.

Page: settings. Selector: `leaf "Theme"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 472.7 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 14px/20px 400 |
| Letter spacing | normal |
| Colour | #e5e5e5 |
| Transition | none |
| How | at rest |

Crops: `setting-label-default.png`.

#### setting-description

Setting description.

Page: settings. Selector: `leaf description`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 472.7 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 12px/16px 400 |
| Letter spacing | normal |
| Colour | #a3a3a3 |
| Transition | none |
| How | at rest |

Crops: `setting-description-default.png`.

#### footer-link

Footer link.

Page: settings. Selector: `button "Check for updates"`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 103.95 x 16 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | OpenAI Sans 12px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #737373 | #d4d4d4 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`.

#### subnav-item-active.light

Settings nav item, current.

Page: settings. Selector: `button "Appearance"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 176 x 40 |
| Padding | 8px 12px |
| Gap | 8px |
| Border | none |
| Radius | 8px |
| Background | #f5f5f5 |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 14px/20px 500 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span.truncate: OpenAI Sans 14px/20px 500, #0a0a0a |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 16 x 16, colour #0a0a0a |
| Painted layers | button.inline-flex.min-h-10 176.0x40.0 bg #f5f5f5 r 8px |
| How | at rest |

Crops: `subnav-item-active.light-default.png`.

#### subnav-item.light

Settings nav item.

Page: settings. Selector: `button "Account"`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 176 x 40 | = | = |
| Padding | 8px 12px | = | = |
| Gap | 8px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | #fafafa | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | OpenAI Sans 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #737373 | #171717 | = |
| Text node | span.truncate: OpenAI Sans 14px/20px 500, #737373 | span.truncate: OpenAI Sans 14px/20px 500, #171717 | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #a3a3a3 | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | button.inline-flex.min-h-10 176.0x40.0 bg #fafafa r 8px | button.inline-flex.min-h-10 176.0x40.0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |

Crops: `subnav-item.light-default.png`, `subnav-item.light-hover.png`, `subnav-item.light-focus-visible.png`.

#### subnav-group-label.light

Settings nav group label.

Page: settings. Selector: `leaf "App"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 176 x 19 |
| Padding | 0px 12px 4px 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 10px/15px 600 |
| Letter spacing | 1.6px |
| Colour | #a3a3a3 |
| Transition | none |
| How | at rest |

Crops: `subnav-group-label.light-default.png`.

#### section-title.light

Section title.

Page: settings. Selector: `main h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 20px/28px 600 |
| Letter spacing | -0.5px |
| Colour | #0a0a0a |
| Transition | none |
| How | at rest |

Crops: `section-title.light-default.png`.

#### settings-card.light

Settings card.

Page: settings. Selector: `card around "Theme"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 726 x 377 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | div.text-sm.text-oai-gray-900: OpenAI Sans 14px/20px 400, #171717 |
| Transition | none |
| Icon | 14 x 14, colour #737373 |
| Painted layers | div.inline-flex.items-center 237.3x34.0 bg #fafafa border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 12px; button.inline-flex.items-center 86.9x28.0 bg #ffffff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; div.flex.flex-col 726.0x63.0 border T:1px solid #e5e5e5 @ 0.6; button.relative.inline-flex 108.9x30.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 12px; input 1.0x1.0 bg #ffffff; div.flex.flex-col 726.0x63.0 border T:1px solid #e5e5e5 @ 0.6 |
| How | at rest |

Crops: none.

#### setting-label.light

Setting label.

Page: settings. Selector: `leaf "Theme"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 472.7 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 14px/20px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Transition | none |
| How | at rest |

Crops: `setting-label.light-default.png`.

#### setting-description.light

Setting description.

Page: settings. Selector: `leaf description`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 472.7 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | OpenAI Sans 12px/16px 400 |
| Letter spacing | normal |
| Colour | #737373 |
| Transition | none |
| How | at rest |

Crops: `setting-description.light-default.png`.

#### footer-link.light

Footer link.

Page: settings. Selector: `button "Check for updates"`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 103.95 x 16 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | OpenAI Sans 12px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #737373 | #404040 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `footer-link.light-default.png`, `footer-link.light-hover.png`.

## Transitions declared in the readable stylesheets

Every rule in the one same-origin CSS bundle that declares a transition or animation, by page (first 12 distinct values).

- dashboard: `opacity 0.2s ease-out`, `opacity 0.22s cubic-bezier(0.16, 1, 0.3, 1), transform 0.26s cubic-bezier(0.16, 1, 0.3, 1)`, `opacity 0.2s ease-out, transform 0.2s cubic-bezier(0.16, 1, 0.3, 1)`, `none`, `opacity 0.22s`
