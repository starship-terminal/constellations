# Component measurements

Computed styles read from docs.x.ai on 2026-11-17 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is the search field clicked into (nothing typed); `dark` is the same element after the header's own "Switch to dark theme" button repainted html.dark; `opened` and the rest are resting states reached by a component's own UI toggle. Nothing was typed, sent or signed into.

## Components

### Docs chrome

#### docs-header

Fixed header bar. The 80px bar fixed over every page: wordmark, product switcher, section links, the ⌘K search pill, theme button and GitHub link.

Page: /overview. Selector: `header`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 1440 x 80 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | xVf 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | #ffffff |
| Text node | a.rounded-md.py-1.5: xVf 14px/20px 500, #0a0a0a | a.rounded-md.py-1.5: xVf 14px/20px 500, #ffffff |
| Transition | all 0.2s ease | = |
| Icon | 49.22 x 20, colour #0a0a0a | 49.22 x 20, colour #ffffff |
| Painted layers | div.from-background.lg:from-background/75 1440.0x96.0 image linear-gradient(#ffffff @ 0.75 0%, #000000 @ 0 100%); button.focus-visible:ring-ring.items-center 208.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; div.bg-primary.flex 145.0x36.0 bg #0a0a0a r 3.35544e+07px; div.bg-primary-foreground/20.w-px 1.0x36.0 bg #f9f8f6 @ 0.2; div.bg-background.border-primary/[0.06] 160.0x401.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.22 0px 16px 48px -8px; div.bg-primary/[0.04].pointer-events-none 0.0x0.0 bg #0a0a0a @ 0.04 r 6px | div.from-background.lg:from-background/75 1440.0x96.0 image linear-gradient(#0a0a0a @ 0.75 0%, #000000 @ 0 100%); button.focus-visible:ring-ring.items-center 208.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; div.bg-primary.flex 145.0x36.0 bg #ffffff r 3.35544e+07px; div.bg-primary-foreground/20.w-px 1.0x36.0 bg #0a0a0a @ 0.2; div.bg-background.border-primary/[0.06] 160.0x401.0 bg #0a0a0a border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.22 0px 16px 48px -8px; div.bg-primary/[0.04].pointer-events-none 0.0x0.0 bg #ffffff @ 0.04 r 6px |
| Ancestor paint | 1 up div.group/sidebar-wrapper.min-h-svh bg #ffffff | 1 up div.group/sidebar-wrapper.min-h-svh bg #0a0a0a |
| How | resting state | same element after the header theme button repaints html.dark |

Crops: `docs-header-default.png`, `docs-header-dark.png`.

#### docs-logo

Wordmark link. The svg wordmark in the header, coloured by the primary foreground role.

Page: /overview. Selector: `header a[aria-label*="home"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 57.22 x 28 |
| Padding | 4px |
| Border | none |
| Radius | 6px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | xVf 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Icon | 49.22 x 20, colour #0a0a0a |
| How | resting state |

Crops: `docs-logo-default.png`.

#### docs-section-link

Header section link. A product-section link in the header nav ("Grok Bot" — an inactive pill-shaped label).

Page: /overview. Selector: `header nav a`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 85 x 32 | = | = |
| Padding | 6px 12px | = | = |
| Gap | 4px | = | = |
| Border | none | = | = |
| Radius | 6px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | xVf 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0a0a0a @ 0.6 | #0a0a0a | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | a.flex.items-center 85.0x32.0 r 6px outline 1px auto #101010 offset 1px |

Crops: `docs-section-link-default.png`, `docs-section-link-hover.png`, `docs-section-link-focus-visible.png`.

#### docs-search-pill

Search pill (⌘K). The rounded search field in the header that opens the cmdk dialog; carries the ⌘K hint.

Page: /overview. Selector: `header button (text Search)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 208 x 36 | = | = |
| Padding | 0px 12px 0px 16px | = | = |
| Gap | normal 8px | = | = |
| Border | 1px solid #0a0a0a @ 0.15 | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | transparent | #0c0c0c @ 0.03 | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0a0a0a 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | xVf 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0a0a0a | = | = |
| Text node | p.text-sm.text-muted: xVf 14px/20px 500, #0a0a0a @ 0.6 | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #0a0a0a @ 0.6 | = | = |
| Painted layers | button.focus-visible:ring-ring.items-center 208.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.focus-visible:ring-ring.items-center 208.0x36.0 bg #0c0c0c @ 0.03 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.focus-visible:ring-ring.items-center 208.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0a0a0a 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `docs-search-pill-default.png`, `docs-search-pill-hover.png`, `docs-search-pill-focus-visible.png`.

#### docs-theme-button

Theme button. The round icon button that switches html.light/html.dark. "dark" shows it after its own press repaints the page.

Page: /overview. Selector: `header button[aria-label*="theme"]`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 28 x 28 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 3.35544e+07px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | xVf 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a @ 0.6 | #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #0a0a0a @ 0.6 | 16 x 16, colour #ffffff |
| How | resting state | same element after the header theme button repaints html.dark |

Crops: `docs-theme-button-default.png`, `docs-theme-button-dark.png`.

#### docs-sidebar

Section sidebar. The left nav column: product links, the collapsible page groups and the active-page marker.

Page: /overview. Selector: `aside`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 272 x 828 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | xVf 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | #ffffff |
| Text node | span.min-w-0.truncate: xVf 13px/19.5px 500, #0a0a0a | span.min-w-0.truncate: xVf 13px/19.5px 500, #ffffff |
| Transition | none | = |
| Icon | 12 x 12, colour #0a0a0a @ 0.6 | 12 x 12, colour #ffffff @ 0.6 |
| Painted layers | a.peer/menu-button.group/menu-button 256.0x32.0 bg #ffffff r 10px; div.focus:ring-ring.gap-1 42.0x18.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; div.focus:ring-ring.gap-1 36.0x18.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; div.focus:ring-ring.gap-1 36.0x18.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; div.focus:ring-ring.gap-1 36.0x18.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; div.focus:ring-ring.gap-1 36.0x18.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px | a.peer/menu-button.group/menu-button 256.0x32.0 bg #212121 r 10px; div.focus:ring-ring.gap-1 42.0x18.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; div.focus:ring-ring.gap-1 36.0x18.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; div.focus:ring-ring.gap-1 36.0x18.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; div.focus:ring-ring.gap-1 36.0x18.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; div.focus:ring-ring.gap-1 36.0x18.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px |
| How | resting state | same element after the header theme button repaints html.dark |

Crops: `docs-sidebar-default.png`, `docs-sidebar-dark.png`.

#### docs-sidebar-link

Sidebar page link. A single page link in the sidebar nav.

Page: /overview. Selector: `aside a`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 256 x 32 | = | = |
| Padding | 6px 8px | = | = |
| Gap | 8px | = | = |
| Border | none | = | = |
| Radius | 10px | = | = |
| Background | transparent | #0c0c0c @ 0.03 | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0a0a0a 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | xVf 13px/18.5714px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0a0a0a @ 0.6 | #0a0a0a | = |
| Text node | span.min-w-0.truncate: xVf 13px/18.5714px 500, #0a0a0a @ 0.6 | span.min-w-0.truncate: xVf 13px/18.5714px 500, #0a0a0a | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | a.peer/menu-button.group/menu-button 256.0x32.0 bg #0c0c0c @ 0.03 r 10px | a.peer/menu-button.group/menu-button 256.0x32.0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0a0a0a 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px |

Crops: `docs-sidebar-link-default.png`, `docs-sidebar-link-hover.png`, `docs-sidebar-link-focus-visible.png`.

#### docs-sidebar-active

Sidebar active link. The link for the page being read, painted with the active style.

Page: /overview. Selector: `aside a (first)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 256 x 32 |
| Padding | 6px 8px |
| Gap | 8px |
| Border | none |
| Radius | 10px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | xVf 13px/18.5714px 500 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span.min-w-0.truncate: xVf 13px/18.5714px 500, #0a0a0a |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | a.peer/menu-button.group/menu-button 256.0x32.0 bg #ffffff r 10px |
| How | resting state |

Crops: `docs-sidebar-active-default.png`.

#### docs-sidebar-group

Sidebar collapsible group. A collapsible group row; "opened" is reached by its own chevron press.

Page: /overview. Selector: `aside button[class*="peer/menu-button"]`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 256 x 32 | = |
| Padding | 6px 8px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 10px | = |
| Background | transparent | #0c0c0c @ 0.03 |
| Box shadow | none | = |
| Outline | none | = |
| Font | xVf 13px/18.5714px 500 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a @ 0.6 | #0a0a0a |
| Text node | span.min-w-0.truncate: xVf 13px/18.5714px 500, #0a0a0a @ 0.6 | span.min-w-0.truncate: xVf 13px/18.5714px 500, #0a0a0a |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 12 x 12, colour #0a0a0a @ 0.6 | 12 x 12, colour #0a0a0a |
| How | resting state | reached by the component's own UI toggle |
| Painted layers | - | button.peer/menu-button.group/menu-button 256.0x32.0 bg #0c0c0c @ 0.03 r 10px |

Crops: `docs-sidebar-group-default.png`, `docs-sidebar-group-opened.png`.

#### docs-page-footer

Page footer bar. The sticky bottom bar (bg-base, border-border-l1) with the page actions.

Page: /developers/quickstart. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 212 x 81 |
| Padding | 16px 0px |
| Gap | 8px |
| Border | T: 1px solid #d5d9e2 @ 0.55; R: none; B: none; L: none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | xVf 14px/20px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a @ 0.6 |
| Text node | span: xVf 14px/20px 400, #0a0a0a @ 0.6 |
| Transition | none |
| Icon | 16 x 16, colour #0a0a0a @ 0.6 |
| Painted layers | footer.border-border-l1.text-muted 212.0x81.0 bg #ffffff border T:1px solid |
| How | resting state |

Crops: `docs-page-footer-default.png`.

#### docs-markdown-link

"View as Markdown" link. The small muted link that serves the page's raw markdown.

Page: /developers/quickstart. Selector: `a (text Markdown)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 133 x 16 | = |
| Padding | 0px | = |
| Gap | 6px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | xVf 12px/16px 600 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a @ 0.6 | #0a0a0a |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #0a0a0a @ 0.6 | 16 x 16, colour #0a0a0a |
| How | resting state | mouse hover over the element |

Crops: `docs-markdown-link-default.png`, `docs-markdown-link-hover.png`.

#### docs-footer-button

"Share feedback" button. A footer action button in the sticky bar — measured, never pressed (it may open a feedback form).

Page: /developers/quickstart. Selector: `footer button (text Share feedback)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 212 x 20 | = |
| Padding | 0px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | xVf 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a @ 0.6 | #0a0a0a |
| Text node | span: xVf 14px/20px 400, #0a0a0a @ 0.6 | span: xVf 14px/20px 400, #0a0a0a |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #0a0a0a @ 0.6 | 16 x 16, colour #0a0a0a |
| Ancestor paint | 1 up footer.border-border-l1.text-muted bg #ffffff | = |
| How | resting state | mouse hover over the element |

Crops: `docs-footer-button-default.png`, `docs-footer-button-hover.png`.

### Docs widgets

#### docs-code-block

Code block (shiki). The shiki-highlighted sample under the hero: a dark-tinted panel even in the light theme.

Page: /overview. Selector: `pre.shiki`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 549.19 x 200 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | xMono 13px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #e1e4e8 | = |
| Text node | span: xMono 13px/20px 400, #f97583 | = |
| Transition | none | = |
| How | resting state | same element after the header theme button repaints html.dark |

Crops: `docs-code-block-default.png`, `docs-code-block-dark.png`.

#### docs-cta

Primary CTA link. A solid call-to-action in the hero ("Get Started" / "Create API key") — primary bg, primary-foreground text.

Page: /overview. Selector: `main a (text Get Started/Create API key/View model)`. States: default, hover, focus-visible, pressed, dark.

| Property | default | hover | focus-visible | pressed | dark |
|---|---|---|---|---|---|
| Size (w x h) | 151 x 40 | = | = | = | = |
| Padding | 10px 18px | = | = | = | = |
| Gap | normal 4px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 3.35544e+07px | = | = | = | = |
| Background | #0a0a0a | = | = | = | #ffffff |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #0a0a0a @ 0.3 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = | = | = |
| Font | xVf 14px/20px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #f9f8f6 | = | = | = | #0a0a0a |
| Transition | color, background-color, border-color, filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 16 x 16, colour #f9f8f6 | = | = | = | 16 x 16, colour #0a0a0a |
| Painted layers | a.relative.isolate 151.0x40.0 bg #0a0a0a r 3.35544e+07px | = | a.relative.isolate 151.0x40.0 bg #0a0a0a r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #0a0a0a @ 0.3 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = | a.relative.isolate 151.0x40.0 bg #ffffff r 3.35544e+07px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press | same element after the header theme button repaints html.dark |

Crops: `docs-cta-default.png`, `docs-cta-hover.png`, `docs-cta-focus-visible.png`, `docs-cta-pressed.png`, `docs-cta-dark.png`.

#### docs-text-link

Inline feature link. A small underlined link inside a feature row (decoration-primary/30).

Page: /overview. Selector: `main a (text Configurable/Learn more/Read more)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 97 x 18.56 | = |
| Padding | 0px | = |
| Gap | 4px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | xVf 13px/18.5714px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 12 x 12, colour #0a0a0a | = |
| How | resting state | mouse hover over the element |

Crops: `docs-text-link-default.png`, `docs-text-link-hover.png`.

#### docs-code-tabs

SDK tabs. The language picker above a code sample ("Python", "TypeScript", "cURL", ...): a Radix tablist.

Page: /developers/quickstart. Selector: `[role="tablist"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 432 x 24 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | xVf 12px/16px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span.flex.items-center: xVf 12px/16px 400, #0a0a0a |
| Transition | none |
| Icon | 16 x 16, colour #0a0a0a |
| Painted layers | span.bg-primary/[0.06].pointer-events-none 98.0x24.0 bg #0a0a0a @ 0.06 r 3.35544e+07px |
| How | resting state |

Crops: `docs-code-tabs-default.png`.

#### docs-code-tab

SDK tab. One tab in the picker. "selected" is the tab's own activation — a local UI toggle that swaps the published snippet.

Page: /developers/quickstart. Selector: `[role="tab"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 98 x 24 | = | = |
| Padding | 4px 8px | = | = |
| Border | none | = | = |
| Radius | 12px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 0px |
| Font | xVf 12px/16px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0a0a0a | = | = |
| Text node | span.flex.items-center: xVf 12px/16px 400, #0a0a0a | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #0a0a0a | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | button.mb-0.inline-flex 98.0x24.0 r 12px outline 1px auto #101010 offset 0px |

Crops: `docs-code-tab-default.png`, `docs-code-tab-hover.png`, `docs-code-tab-focus-visible.png`.

#### docs-next-card

Nav card. A filled card link at the foot of a docs page (bg-card, hover:bg-card-hover).

Page: /developers/quickstart. Selector: `main a.bg-card, main a[class*="bg-card"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 672 x 156 | = | = |
| Padding | 28px | = | = |
| Border | none | = | = |
| Radius | 16px | = | = |
| Background | #f9f8f6 | #edecea | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | xVf 14px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0a0a0a | = | = |
| Text node | h3.font-display.text-primary: xVf 20px/28px 500, #0a0a0a, ls -0.2px | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 12 x 12, colour #0a0a0a @ 0.6 | 12 x 12, colour #0a0a0a | = |
| Painted layers | a.bg-card.hover:bg-card-hover 672.0x156.0 bg #f9f8f6 r 16px | a.bg-card.hover:bg-card-hover 672.0x156.0 bg #edecea r 16px | a.bg-card.hover:bg-card-hover 672.0x156.0 bg #f9f8f6 r 16px outline 1px auto #101010 offset 1px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `docs-next-card-default.png`, `docs-next-card-hover.png`, `docs-next-card-focus-visible.png`.

#### pricing-table

Pricing table. A token-pricing table: header row with a bottom border, dense cells.

Page: /developers/pricing. Selector: `table`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 806 x 646.66 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | xVf 14px/21px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | #d5d9e2 |
| Text node | th.text-secondary.whitespace-nowrap: xVf 14px/20px 500, #0a0a0a | th.text-secondary.whitespace-nowrap: xVf 14px/20px 500, #d5d9e2 |
| Transition | none | = |
| Painted layers | th.whitespace-nowrap.px-3 235.5x42.7 border L:1px solid; tr.border-border.border-b 806.0x44.5 border B:1px solid; th.text-secondary.whitespace-nowrap 81.5x44.5 border L:1px solid; tr 806.0x70.0 border B:1px solid; td.whitespace-nowrap.px-3 246.0x70.0 border B:1px solid; td.whitespace-nowrap.px-3 81.0x70.0 border B:1px solid | = |
| How | resting state | same element after the header theme button repaints html.dark |

Crops: `pricing-table-default.png`, `pricing-table-dark.png`.

#### pricing-th

Table header cell. A th in the pricing table.

Page: /developers/pricing. Selector: `th`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 246 x 87.16 |
| Padding | 8px 12px 16px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | xVf 14px/20px 500 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Transition | none |
| How | resting state |

Crops: `pricing-th-default.png`.

#### pricing-td

Table cell. A td in the pricing table.

Page: /developers/pricing. Selector: `td`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 246 x 70 |
| Padding | 14px 12px 14px 0px |
| Border | T: none; R: none; B: 1px solid #d5d9e2 @ 0.55; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | xVf 14px/21px 500 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | a.hover:underline: xVf 14px/21px 500, #0a0a0a |
| Transition | none |
| Painted layers | td.whitespace-nowrap.px-3 246.0x70.0 border B:1px solid |
| How | resting state |

Crops: `pricing-td-default.png`.

#### gbm-panel

Grok Bot phone panel. The phone-shaped routine panel (.gbm-panel) on the Grok Bot page — the product's illustrative mock.

Page: /grok-bot/overview. Selector: `section.gbm-panel, [class*="gbm-panel"]`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 231 x 172.38 | = |
| Padding | 0px | = |
| Gap | 10px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | system-ui 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | #f2f2f2 |
| Text node | text: DejaVu Sans 12px/18px 700, #0a0a0a | text: DejaVu Sans 12px/18px 700, #f2f2f2 |
| Transition | none | = |
| Icon | 231 x 144.38, colour #0a0a0a, fill #000000 | 231 x 144.38, colour #f2f2f2, fill #000000 |
| How | resting state | same element after the header theme button repaints html.dark |

Crops: `gbm-panel-default.png`, `gbm-panel-dark.png`.

### Docs prose

#### prose-h1

Page title (h1). The article title in font-display.

Page: /developers/quickstart. Selector: `main h1`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 672 x 52.8 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | xVf 48px/52.8px 450 | = |
| Letter spacing | -0.48px | = |
| Colour | #0a0a0a | #ffffff |
| Text node | a.not-prose: xVf 48px/52.8px 450, #0a0a0a, ls -0.48px | a.not-prose: xVf 48px/52.8px 450, #ffffff, ls -0.48px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = |
| How | resting state | same element after the header theme button repaints html.dark |

Crops: `prose-h1-default.png`, `prose-h1-dark.png`.

#### prose-h2

Section heading (h2). A numbered step heading.

Page: /developers/quickstart. Selector: `main h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672 x 37.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | xVf 30px/37.5px 500 |
| Letter spacing | -0.3px |
| Colour | #0a0a0a |
| Text node | a.not-prose: xVf 30px/37.5px 500, #0a0a0a, ls -0.3px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| How | resting state |

Crops: `prose-h2-default.png`.

#### prose-p

Body paragraph. A paragraph of the quickstart.

Page: /developers/quickstart. Selector: `main p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | xVf 14px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Transition | none |
| How | resting state |

Crops: `prose-p-default.png`.

#### prose-inline-code

Inline code span. A `code` span inside prose, tinted by the solar accent.

Page: /developers/quickstart. Selector: `main p code, main li code`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 32 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | xMono 13.3px/24px 400 |
| Letter spacing | normal |
| Colour | #ff640a |
| Transition | none |
| How | resting state |

Crops: `prose-inline-code-default.png`.

#### prose-copy-llm

"Copy for LLM" button. The small muted button that copies the page for an LLM — a local clipboard action, pressed only with forcePseudoState.

Page: /developers/faq/general. Selector: `main button (text Copy for LLM)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 102 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | xVf 12px/16px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a @ 0.6 | #0a0a0a | = | #0a0a0a |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #0a0a0a @ 0.6 | 16 x 16, colour #0a0a0a | = | 16 x 16, colour #0a0a0a |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |
| Painted layers | - | = | button.text-muted.hover:text-primary 102.0x16.0 outline 1px auto #101010 offset 0px | = |

Crops: `prose-copy-llm-default.png`, `prose-copy-llm-hover.png`, `prose-copy-llm-focus-visible.png`, `prose-copy-llm-pressed.png`.

#### faq-question

FAQ question (h3). A question heading on the FAQ page — the FAQ lists plain headings, no accordion.

Page: /developers/faq/general. Selector: `main h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672 x 33 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | xVf 24px/33px 500 |
| Letter spacing | -0.24px |
| Colour | #0a0a0a |
| Text node | a.not-prose: xVf 24px/33px 500, #0a0a0a, ls -0.24px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| How | resting state |

Crops: `faq-question-default.png`.

#### prose-link

Prose link. A body-text link (the "Connectors" link on the Grok help page), underlined with the dotted solar decoration for code spans.

Page: /grok/overview. Selector: `main p a, main li a`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 62 x 16 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | xVf 14px/24px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0a0a0a | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | a.text-primary.underline 62.0x16.0 outline 1px auto #101010 offset 1px |

Crops: `prose-link-default.png`, `prose-link-hover.png`, `prose-link-focus-visible.png`.

### Docs search

#### docs-search-dialog

Search dialog (cmdk). The ⌘K command menu: "Ask Grok" plus page suggestions, painted by the page's own shortcut.

Page: /overview. Selector: `.docs-search-modal, [cmdk-root]`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 1000 x 485 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | #ffffff | #0a0a0a |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.35 0px 32px 80px -24px | = |
| Outline | none | = |
| Font | xVf 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | #ffffff |
| Text node | div.text-subtle.mb-3: xVf 14px/20px 400, #0a0a0a @ 0.6 | div.text-subtle.mb-3: xVf 14px/20px 400, #ffffff @ 0.6 |
| Transition | none | = |
| Icon | 16 x 16, colour #0a0a0a @ 0.6 | 16 x 16, colour #ffffff @ 0.6 |
| Painted layers | div.relative.flex 1000.0x485.0 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.35 0px 32px 80px -24px; div.relative.flex 1000.0x48.0 border B:1px solid; div.max-w-dvw.flex 500.0x400.0 border R:1px solid; div.data-[disabled=true]:text-muted.flex 475.0x54.0 bg #525252 @ 0.1 r 8px | div.relative.flex 1000.0x485.0 bg #0a0a0a r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.35 0px 32px 80px -24px; div.relative.flex 1000.0x48.0 border B:1px solid; div.max-w-dvw.flex 500.0x400.0 border R:1px solid; div.data-[disabled=true]:text-muted.flex 475.0x54.0 bg #525252 @ 0.1 r 8px |
| How | resting state | the dialog was closed, the header theme button repainted html.dark, and Ctrl+K reopened it |

Crops: `docs-search-dialog-default.png`, `docs-search-dialog-dark.png`.

#### docs-search-input

Search input. The command field; "focused" is the field clicked into — nothing is typed.

Page: /overview. Selector: `.docs-search-modal input, [cmdk-input]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 1000 x 48 | = |
| Padding | 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | xVf 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #0a0a0a @ 0.6, opacity 1 | = |
| Ancestor paint | 3 up div.relative.flex bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.35 0px 32px 80px -24px | = |
| How | resting state | the field clicked into |

Crops: `docs-search-input-default.png`, `docs-search-input-focused.png`.

#### docs-search-item

Suggestion row. A suggestion row in the open menu ("Ask Grok anything", "Quickstart", ...).

Page: /overview. Selector: `[cmdk-item], [role="option"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 475 x 54 | = |
| Padding | 8px 12px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #525252 @ 0.1 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | xVf 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | div.truncate.text-sm: xVf 14px/20px 500, #000000 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #0a0a0a @ 0.6 | = |
| Painted layers | div.data-[disabled=true]:text-muted.flex 475.0x54.0 bg #525252 @ 0.1 r 8px | = |
| How | resting state | mouse hover over the element |

Crops: `docs-search-item-default.png`, `docs-search-item-hover.png`.

### Docs chrome (mobile)

#### m-docs-topbar

Mobile header. The fixed bar at 390px: hamburger, wordmark, search and theme icons.

Page: /overview. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 68 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | xVf 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | all 0.2s ease |
| Icon | 49.22 x 20, colour #0a0a0a |
| Painted layers | div.from-background.lg:from-background/75 390.0x128.0 image linear-gradient(in oklab, #ffffff 0%, #000000 @ 0 100%); button.focus-visible:ring-ring.items-center 0.0x0.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; div.bg-primary.flex 0.0x0.0 bg #0a0a0a r 3.35544e+07px; div.bg-primary-foreground/20.w-px 0.0x0.0 bg #f9f8f6 @ 0.2; div.bg-background.border-primary/[0.06] 0.0x0.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.22 0px 16px 48px -8px; div.bg-primary/[0.04].pointer-events-none 0.0x0.0 bg #0a0a0a @ 0.04 r 6px |
| Ancestor paint | 1 up div.group/sidebar-wrapper.min-h-svh bg #ffffff |
| How | resting state |

Crops: `m-docs-topbar-default.png`.

#### m-docs-hamburger

"Open navigation menu" button. The hamburger that opens the nav sheet.

Page: /overview. Selector: `header button[aria-label*="navigation" i], header button[aria-label*="menu" i]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 36 x 36 | = |
| Padding | 0px | = |
| Gap | normal 8px | = |
| Border | none | = |
| Radius | 3.35544e+07px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | xVf 14px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 20 x 20, colour #0a0a0a | = |
| How | resting state | mouse hover over the element |

Crops: `m-docs-hamburger-default.png`, `m-docs-hamburger-hover.png`.

#### m-docs-drawer

Nav sheet (open). The opened navigation sheet — a full-screen fixed aside over the page. The "Open navigation menu" press happens in find(): the sheet is only visible once open, so the state itself is a no-op.

Page: /overview. Selector: `aside.fixed.inset-0`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 56px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | xVf 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.flex.items-center: xVf 16px/24px 500, #0a0a0a |
| Transition | none |
| Icon | 12 x 12, colour #0a0a0a @ 0.6 |
| Painted layers | aside.pt-(--topbar-height).bg-background 390.0x844.0 bg #ffffff; div.border-b.px-4 390.0x307.0 border B:1px solid; a.peer/menu-button.group/menu-button 374.0x32.0 bg #ffffff r 10px; div.focus:ring-ring.gap-1 42.0x18.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; div.focus:ring-ring.gap-1 36.0x18.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; div.focus:ring-ring.gap-1 36.0x18.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px |
| How | the "Open navigation menu" button's own press |

Crops: `m-docs-drawer-opened.png`.

## Transitions declared in the readable stylesheets

docs.x.ai serves its own CSS same-origin (/_next/static/chunks), so this list is the site's own transition declarations the CSSOM could read on each page.

- /developers/faq/general: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- /developers/pricing: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- /developers/quickstart: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- /grok-bot/overview: `fill 0.6s`, `transform 0.9s cubic-bezier(0.22, 1, 0.36, 1)`, `opacity 0.15s`, `opacity var(--plugin-row-mark) ease`, `none`, `background-color 0.12s`, `background-color 0.12s, color 0.12s`, `background-color 0.12s, opacity 0.12s`, `background-color 0.12s, border-color 0.12s`, `border-color 0.12s`, `opacity 0.12s`, `border-radius 0.38s cubic-bezier(0.2, 0, 0, 1)`

- /grok/overview: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- /overview: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`
