# Component measurements

Computed styles read from dub.co on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's three painted surfaces — the Next.js marketing pages (light only), the app.dub.co auth shell on /login + /register, and the Mintlify docs surface on /docs measured in both its light and dark themes — with promo and AI-assistant overlays hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### nav

Nav bar. The top nav: wordmark, Product/Solutions/Resources dropdowns, Customers and Pricing links, Log in and the black Sign-up pill.

Page: home. Selector: `nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 472.88 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | button.relative.group/item: Inter 14px/20px 500, #404040 |
| Transition | none |
| Icon | 10 x 10, colour #404040 |
| Painted layers | div.pointer-events-none.absolute 0.0x32.0 bg #171717 @ 0.05 r 8px |
| How | at rest |

Crops: `nav-default.png`.

#### logo

Logo. The Dub wordmark anchor.

Page: home. Selector: `first header link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 61.33 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Transition | none |
| Cursor | pointer |
| Icon | 61.33 x 32, colour #262626 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-trigger

Nav trigger. The Product button that opens the mega-menu on hover; toggled, never followed.

Page: home. Selector: `nav button "Product"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 92.52 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #404040 | #171717 | = | #171717 |
| Transition | color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 10, colour #404040 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.relative.group/item 92.5x32.0 r 8px outline 1px auto #005fcc offset 0px | = |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### nav-link

Nav link. A plain nav link (Customers/Pricing).

Page: home. Selector: `nav a "Customers"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 96.94 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #404040 | #171717 | = | #171717 |
| Transition | color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.relative.group/item 96.9x32.0 r 8px outline 1px auto #005fcc offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Log-in button. The bordered Log-in button; measured never followed.

Page: home. Selector: `a "Log in"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 74.5 x 32 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | 1px solid #e5e5e5 | = | 1px solid #a3a3a3 | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #fafafa | = | #fafafa |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.transition-all.border-border-subtle 74.5x32.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px | a.transition-all.border-border-subtle 74.5x32.0 bg #fafafa border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px | a.transition-all.border-border-subtle 74.5x32.0 bg #ffffff border T:1px solid #a3a3a3 / R:1px solid #a3a3a3 / B:1px solid #a3a3a3 / L:1px solid #a3a3a3 r 8px outline 2px solid #000000 @ 0 offset 2px | a.transition-all.border-border-subtle 74.5x32.0 bg #fafafa border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-cta

Sign-up CTA. The black Sign-up pill; measured never followed.

Page: home. Selector: `a "Sign up"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 84.03 x 32 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = | #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.transition-all.border-black 84.0x32.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 8px | a.transition-all.border-black 84.0x32.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 8px shadow #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | a.transition-all.border-black 84.0x32.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 8px outline 1px auto #005fcc offset 1px | a.transition-all.border-black 84.0x32.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 8px shadow #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-dropdown

Mega-menu panel. The Product mega-menu panel, opened by its own trigger on hover.

Page: home. Selector: `product mega-menu panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 318.66 x 318 |
| Padding | 0px |
| Border | 1px solid #f5f5f5 |
| Radius | 12px |
| Background | #fafafa |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span.mt-3.block: Inter 14px/20px 500, #171717 |
| Transition | none |
| Cursor | pointer |
| Icon | 316.66 x 316, colour #000000 @ 0.1, fill #000000 |
| Painted layers | a.group.relative 318.7x318.0 bg #fafafa border T:1px solid #f5f5f5 / R:1px solid #f5f5f5 / B:1px solid #f5f5f5 / L:1px solid #f5f5f5 r 12px; div.flex.size-4 16.0x16.0 bg #a78bfa r 4px; div.border-border-subtle.bg-bg-default 174.0x54.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 4px; div.bg-bg-emphasis.aspect-square 52.0x52.0 bg #e5e5e5; div.border-border-subtle.flex 108.8x52.0 border L:1px solid #e5e5e5; img.h-2.5.w-3 12.0x10.0 border T:1px solid #000000 @ 0.15 / R:1px solid #000000 @ 0.15 / B:1px solid #000000 @ 0.15 / L:1px solid #000000 @ 0.15 r 2px |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-link

Menu item. A product link inside the opened mega-menu. Only the default reading stands: the menu closed between states during capture, so the hover, focus-visible and pressed readings came from a different element and were removed.

Page: home. Selector: `mega-menu link inside the open panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 307.41 x 304.45 |
| Padding | 0px |
| Border | 1px solid #f5f5f5 |
| Radius | 12px |
| Background | #fafafa |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span.mt-3.block: Inter 14px/20px 500, #171717 |
| Transition | none |
| Cursor | pointer |
| Icon | 305.48 x 302.54, colour #000000 @ 0.1, fill #000000 |
| Painted layers | a.group.relative 307.4x304.5 bg #fafafa border T:1px solid #f5f5f5 / R:1px solid #f5f5f5 / B:1px solid #f5f5f5 / L:1px solid #f5f5f5 r 12px; div.flex.size-4 15.4x15.3 bg #a78bfa r 4px; div.border-border-subtle.bg-bg-default 167.9x51.7 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 4px; div.bg-bg-emphasis.aspect-square 50.2x49.8 bg #e5e5e5; div.border-border-subtle.flex 105.0x49.8 border L:1px solid #e5e5e5; img.h-2.5.w-3 11.6x9.6 border T:1px solid #000000 @ 0.15 / R:1px solid #000000 @ 0.15 / B:1px solid #000000 @ 0.15 / L:1px solid #000000 @ 0.15 r 2px |
| How | at rest |

Crops: `menu-link-default.png`.

### Home hero

#### hero-badge

Announcement pill. The "Introducing our Startup Program / Learn more" pill above the headline; measured never followed.

Page: home. Selector: `announcement pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 211.31 x 28 | = | - | = |
| Padding | 6px 10px 6px 16px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 12px/16px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #262626 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Ancestor paint | 1 up a.group.flex bg #ffffff | 1 up a.group.flex bg #fafafa | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `hero-badge-default.png`, `hero-badge-hover.png`, `hero-badge-pressed.png`.

#### hero-title

Hero headline. The display headline ("Turn clicks into revenue"), Satoshi.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 508.78 x 55.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | satoshi 48px/55.2px 500 |
| Letter spacing | normal |
| Colour | #171717 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-lede

Hero lede. The paragraph under the headline.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/28px 400 |
| Letter spacing | normal |
| Colour | #525252 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `hero-lede-default.png`.

#### hero-cta

Primary CTA. The black "Start for free" button; measured never followed.

Page: home. Selector: `"Start for free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 127.42 x 38 | = | = | = |
| Padding | 8px 20px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #000000 | #262626 | = | #262626 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, #000000 @ 0.05 0px 1px 2px 0px | = | #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, #000000 @ 0.05 0px 1px 2px 0px |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.mx-auto.max-w-fit 127.4x38.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | a.mx-auto.max-w-fit 127.4x38.0 bg #262626 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 8px shadow #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, #000000 @ 0.05 0px 1px 2px 0px | a.mx-auto.max-w-fit 127.4x38.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px outline 1px auto #005fcc offset 1px | a.mx-auto.max-w-fit 127.4x38.0 bg #262626 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 8px shadow #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-demo

Demo button. The bordered "Get a demo" button; measured never followed.

Page: home. Selector: `"Get a demo"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 118.64 x 38 | = | = | = |
| Padding | 8px 20px | = | = | = |
| Border | 1px solid #e5e5e5 | 1px solid #a3a3a3 | = | 1px solid #a3a3a3 |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, #000000 @ 0.05 0px 1px 2px 0px | = | #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, #000000 @ 0.05 0px 1px 2px 0px |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #262626 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.mx-auto.max-w-fit 118.6x38.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | a.mx-auto.max-w-fit 118.6x38.0 bg #ffffff border T:1px solid #a3a3a3 / R:1px solid #a3a3a3 / B:1px solid #a3a3a3 / L:1px solid #a3a3a3 r 8px shadow #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, #000000 @ 0.05 0px 1px 2px 0px | a.mx-auto.max-w-fit 118.6x38.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px outline 1px auto #005fcc offset 1px | a.mx-auto.max-w-fit 118.6x38.0 bg #ffffff border T:1px solid #a3a3a3 / R:1px solid #a3a3a3 / B:1px solid #a3a3a3 / L:1px solid #a3a3a3 r 8px shadow #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-demo-default.png`, `hero-demo-hover.png`, `hero-demo-focus-visible.png`, `hero-demo-pressed.png`.

#### hero-tab

Feature tab. An icon tab over the product demo (Affiliate Programs / Conversion Analytics / Short Links).

Page: home. Selector: `feature tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 167.64 x 34 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #e5e5e5 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #262626 | = | = | = |
| Text node | span.text-sm.font-medium: Inter 14px/14px 500, #262626 | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 10, colour #581c87 | 11 x 11, colour #581c87 | = | 11 x 11, colour #581c87 |
| Painted layers | button.group.flex 167.6x34.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px; span.flex.size-4 16.0x16.0 bg #c084fc border T:1px solid #000000 @ 0.05 / R:1px solid #000000 @ 0.05 / B:1px solid #000000 @ 0.05 / L:1px solid #000000 @ 0.05 r 4px | button.group.flex 167.6x34.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px; span.flex.size-4 17.6x17.6 bg #c084fc border T:1px solid #000000 @ 0.05 / R:1px solid #000000 @ 0.05 / B:1px solid #000000 @ 0.05 / L:1px solid #000000 @ 0.05 r 4px | button.group.flex 167.6x34.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 1px auto #005fcc offset 0px; span.flex.size-4 16.0x16.0 bg #c084fc border T:1px solid #000000 @ 0.05 / R:1px solid #000000 @ 0.05 / B:1px solid #000000 @ 0.05 / L:1px solid #000000 @ 0.05 r 4px | button.group.flex 167.6x34.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px; span.flex.size-4 17.6x17.6 bg #c084fc border T:1px solid #000000 @ 0.05 / R:1px solid #000000 @ 0.05 / B:1px solid #000000 @ 0.05 / L:1px solid #000000 @ 0.05 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-tab-default.png`, `hero-tab-hover.png`, `hero-tab-focus-visible.png`, `hero-tab-pressed.png`.

#### demo-panel

Product demo panel. The rendered dashboard mock under the hero — a published demo illustration, not the real app.

Page: home. Selector: `dashboard demo panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 882 x 567 |
| Padding | 0px |
| Border | T: 1px solid #d4d4d4; R: 1px solid #d4d4d4; B: none; L: 1px solid #d4d4d4 |
| Radius | 12px 12px 0px 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Transition | none |
| Icon | 880 x 610.97, colour #0a0a0a, fill #000000 |
| Painted layers | div.relative.size-full 882.0x567.0 bg #ffffff border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 12px 12px 0px 0px |
| How | at rest |

Crops: `demo-panel-default.png`.

#### links-h1

Product page headline. The /links product-page h1 ("Short links with superpowers").

Page: links. Selector: `h1 on /links`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 110.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | satoshi 48px/55.2px 500 |
| Letter spacing | normal |
| Colour | #171717 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `links-h1-default.png`.

### Pricing

#### pricing-h1

Pricing title. The pricing page heading.

Page: pricing. Selector: `h1 on /pricing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672 x 110.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | satoshi 48px/55.2px 500 |
| Letter spacing | normal |
| Colour | #171717 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### billing-toggle

Billing toggle. The Monthly/Yearly period toggle ("10% discount + 12x usage upfront"); the yearly option was toggled for the state, never checked out.

Page: pricing. Selector: `button "Yearly"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 280.58 x 40 | = | = | = |
| Padding | 10px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #e5e5e5 @ 0.3 | = | #e5e5e5 @ 0.3 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Inter 12px/12px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #262626 | #737373 | = | #737373 |
| Text node | p: Inter 12px/12px 500, #262626 | p: Inter 12px/12px 500, #737373 | = | p: Inter 12px/12px 500, #737373 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.max-w-fit.rounded-full 212.5x18.0 image linear-gradient(to right, #dbeafe, #dbeafe @ 0.5, #dbeafe) border T:1px solid #bfdbfe / R:1px solid #bfdbfe / B:1px solid #bfdbfe / L:1px solid #bfdbfe r 9999px | button.relative.flex 280.6x40.0 bg #e5e5e5 @ 0.3 r 12px; span.max-w-fit.rounded-full 212.5x18.0 image linear-gradient(to right, #dbeafe, #dbeafe @ 0.5, #dbeafe) border T:1px solid #bfdbfe / R:1px solid #bfdbfe / B:1px solid #bfdbfe / L:1px solid #bfdbfe r 9999px | button.relative.flex 280.6x40.0 r 12px outline 1px auto #005fcc offset 0px; span.max-w-fit.rounded-full 212.5x18.0 image linear-gradient(to right, #dbeafe, #dbeafe @ 0.5, #dbeafe) border T:1px solid #bfdbfe / R:1px solid #bfdbfe / B:1px solid #bfdbfe / L:1px solid #bfdbfe r 9999px | button.relative.flex 280.6x40.0 bg #e5e5e5 @ 0.3 r 12px; span.max-w-fit.rounded-full 212.5x18.0 image linear-gradient(to right, #dbeafe, #dbeafe @ 0.5, #dbeafe) border T:1px solid #bfdbfe / R:1px solid #bfdbfe / B:1px solid #bfdbfe / L:1px solid #bfdbfe r 9999px |
| Ancestor paint | 1 up div.relative.z-0 bg #f5f5f5 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `billing-toggle-default.png`, `billing-toggle-hover.png`, `billing-toggle-focus-visible.png`, `billing-toggle-pressed.png`.

#### plan-name

Plan name. A plan card's name.

Page: pricing. Selector: `plan name`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 66.48 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 500 |
| Letter spacing | -0.32px |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `plan-name-default.png`.

#### plan-price

Plan price. A plan card's price figure.

Page: pricing. Selector: `plan price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 321.33 x 36 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 500 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span.text-sm.tracking-[-0.02em]: Inter 14px/20px 500, #171717 @ 0.5, ls -0.28px |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. A plan card's "Start 14-day trial" action; measured never followed.

Page: pricing. Selector: `"Start 14-day trial"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 329.33 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Text node | div.min-w-0.truncate: Inter 14px/20px 400, #171717 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.group.flex 329.3x36.0 bg #ffffff border T:1px solid #ededed / R:1px solid #ededed / B:1px solid #ededed / L:1px solid #ededed r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.03 0px 1px 3px 0px outline 2px solid #000000 @ 0 offset 2px | button.group.flex 329.3x36.0 bg #fafafa border T:1px solid #ededed / R:1px solid #ededed / B:1px solid #ededed / L:1px solid #ededed r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.03 0px 1px 3px 0px outline 2px solid #000000 @ 0 offset 2px | a.w-full 329.3x36.0 outline 1px auto #005fcc offset 1px; button.group.flex 329.3x36.0 bg #ffffff border T:1px solid #ededed / R:1px solid #ededed / B:1px solid #ededed / L:1px solid #ededed r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.03 0px 1px 3px 0px outline 2px solid #000000 @ 0 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-card

Plan card. A pricing plan card (the painted ancestor of the plan name).

Page: pricing. Selector: `plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1062 x 623 |
| Padding | 0px |
| Border | 1px solid #ededed |
| Radius | 12px |
| Background | #fafafa |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | h3.text-base.font-medium: Inter 16px/24px 500, #262626, ls -0.32px |
| Transition | none |
| Icon | 0 x 0, colour #262626 |
| Painted layers | div.border-neutral-150.hidden 1062.0x623.0 bg #fafafa border T:1px solid #ededed / R:1px solid #ededed / B:1px solid #ededed / L:1px solid #ededed r 12px; div.w-fit.whitespace-nowrap 75.9x17.8 bg #ddd6fe r 9999px; div.absolute.inset-y-0 1011.0x2.0 bg #e5e5e5 r 9999px; div.absolute.inset-y-0 707.7x2.0 bg #262626 r 9999px; div.absolute.top-1/2 18.0x18.0 bg #262626 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.12 0px 1px 2px 0px outline 2px solid #000000 @ 0 offset 2px; div.w-px.transition-[height,background-color] 1.0x6.0 bg #262626 |
| How | at rest |

Crops: `plan-card-default.png`.

#### faq-trigger

FAQ accordion. A billing-FAQ accordion trigger; toggled for the open state.

Page: pricing. Selector: `faq accordion button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 688 x 56 | = | = | = |
| Padding | 16px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Inter 18px/28px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Text node | h3.text-left.text-base: Inter 16px/24px 500, #262626 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #0a0a0a, fill #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.flex.flex-1 688.0x56.0 outline 1px auto #005fcc offset 0px | = |

Crops: `faq-trigger-default.png`, `faq-trigger-hover.png`, `faq-trigger-focus-visible.png`, `faq-trigger-pressed.png`.

### Compare (vs Bitly)

#### cmp-h1

Compare headline. The "Dub vs Bitly" page heading.

Page: compare. Selector: `h1 on /compare/bitly`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 576 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | satoshi 48px/48px 500 |
| Letter spacing | normal |
| Colour | #171717 |
| Transition | none |
| How | at rest |

Crops: `cmp-h1-default.png`.

#### cmp-table

Comparison table. The feature comparison table (Dub vs Bitly).

Page: compare. Selector: `table`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 958 x 1384 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span.font-display.font-bold: satoshi 16px/24px 700, #1f2937 |
| Transition | none |
| Icon | 16 x 16, colour #6b7280 |
| Painted layers | th.w-60.p-2 479.0x113.0 border B:1px solid #e5e7eb; div.relative.isolate 134.0x30.0 bg #ffffff image linear-gradient(to right, #f3f4f6, #f3f4f6 @ 0) border T:1px solid #d1d5db / R:1px solid #d1d5db / B:1px solid #d1d5db / L:1px solid #d1d5db r 9999px; div.absolute.inset-0 40.0x24.0 image linear-gradient(to right bottom, #1f2937, #6b7280) r 9999px; th.relative.w-28 239.5x113.0 bg #ffffff border B:1px solid #e5e7eb r 16px 16px 0px 0px; div.pointer-events-none.absolute 239.5x113.0 border T:2px solid #8b5cf6 / R:2px solid #8b5cf6 / L:2px solid #8b5cf6 r 16px 16px 0px 0px; th.w-28.py-8 239.5x113.0 border B:1px solid #e5e7eb |
| Ancestor paint | 1 up div.overflow-x-scroll.rounded-md bg #f9fafb shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #c7c7c7 @ 0.2 10px -50px 94px 0px inset |
| How | at rest |

Crops: `cmp-table-default.png`.

#### cmp-check

Comparison cell. A cell in the comparison table.

Page: compare. Selector: `comparison td`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 479 x 77 |
| Padding | 16px |
| Border | T: none; R: none; B: 1px solid #e5e7eb; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | h3.font-display.font-bold: satoshi 16px/24px 700, #1f2937 |
| Transition | none |
| Painted layers | td.p-2.md:p-4 479.0x77.0 border B:1px solid #e5e7eb |
| How | at rest |

Crops: `cmp-check-default.png`.

### Customers

#### cust-h1

Customers headline. The "Meet our customers" heading.

Page: customers. Selector: `h1 on /customers`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 512 x 55.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | satoshi 48px/55.2px 500 |
| Letter spacing | normal |
| Colour | #171717 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `cust-h1-default.png`.

#### customer-card

Customer card. A customer story card/logo tile; measured never followed.

Page: customers. Selector: `customer card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 128 x 480 | 175.83 x 480 | = | 174.66 x 480 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #171717 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | h3.max-w-md.text-balance: Inter 18px/28px 500, #ffffff | = | = | = |
| Transition | flex-grow, flex-basis 0.5s cubic-bezier(0.215, 0.61, 0.355, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.relative 128.0x480.0 bg #171717 r 12px; div.bg-[#16c].absolute 128.0x480.0 bg #1166cc; div.absolute.inset-0 128.0x480.0 image linear-gradient(to right, #000000 @ 0.6, #000000 @ 0); div.absolute.inset-0 128.0x480.0 image linear-gradient(to top, #000000 @ 0.6, #000000 @ 0); span.mt-4.inline-flex 95.9x32.0 bg #ffffff r 8px | a.group.relative 175.8x480.0 bg #171717 r 12px; div.bg-[#16c].absolute 175.8x480.0 bg #1166cc; div.absolute.inset-0 175.8x480.0 image linear-gradient(to right, #000000 @ 0.6, #000000 @ 0); div.absolute.inset-0 175.8x480.0 image linear-gradient(to top, #000000 @ 0.6, #000000 @ 0); span.mt-4.inline-flex 95.9x32.0 bg #f5f5f5 r 8px | a.group.relative 128.0x480.0 bg #171717 r 12px outline 1px auto #005fcc offset 1px; div.bg-[#16c].absolute 128.0x480.0 bg #1166cc; div.absolute.inset-0 128.0x480.0 image linear-gradient(to right, #000000 @ 0.6, #000000 @ 0); div.absolute.inset-0 128.0x480.0 image linear-gradient(to top, #000000 @ 0.6, #000000 @ 0); span.mt-4.inline-flex 95.9x32.0 bg #ffffff r 8px | a.group.relative 174.7x480.0 bg #171717 r 12px; div.bg-[#16c].absolute 174.7x480.0 bg #1166cc; div.absolute.inset-0 174.7x480.0 image linear-gradient(to right, #000000 @ 0.6, #000000 @ 0); div.absolute.inset-0 174.7x480.0 image linear-gradient(to top, #000000 @ 0.6, #000000 @ 0); span.mt-4.inline-flex 95.9x32.0 bg #f5f5f5 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `customer-card-default.png`, `customer-card-hover.png`, `customer-card-focus-visible.png`, `customer-card-pressed.png`.

### Contact sales form

#### sales-card

Contact form card. The centred Talk-to-sales card; never filled past a deleted sample, never submitted.

Page: sales. Selector: `sales form card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 346 |
| Padding | 0px |
| Border | T: none; R: 1px solid #e5e5e5; B: none; L: 1px solid #e5e5e5 |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | label.mb-2.block: Inter 14px/20px 500, #171717 |
| Transition | none |
| Painted layers | div.border-grid-border.relative 800.0x346.0 bg #ffffff border R:1px solid #e5e5e5 / L:1px solid #e5e5e5; input.relative.z-10 750.0x38.0 bg #ffffff border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 6px; textarea.block.w-full 750.0x118.0 bg #ffffff border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 6px; button.group.flex 123.8x40.0 bg #f5f5f5 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up div.relative.overflow-hidden bg #fafafa |
| How | at rest |

Crops: `sales-card-default.png`.

#### sales-email

Email field. The work-email input; sample text was typed and deleted, nothing sent.

Page: sales. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 750 x 38 | = | = |
| Padding | 8px 12px | = | = |
| Border | 1px solid #d4d4d4 | 1px solid #737373 | 1px solid #737373 |
| Radius | 6px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #737373 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | #ffffff 0px 0px 0px 0px, #737373 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #171717 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #a3a3a3, opacity 1 | = | = |
| Painted layers | input.relative.z-10 750.0x38.0 bg #ffffff border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 6px | input.relative.z-10 750.0x38.0 bg #ffffff border T:1px solid #737373 / R:1px solid #737373 / B:1px solid #737373 / L:1px solid #737373 r 6px shadow #ffffff 0px 0px 0px 0px, #737373 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | input.relative.z-10 750.0x38.0 bg #ffffff border T:1px solid #737373 / R:1px solid #737373 / B:1px solid #737373 / L:1px solid #737373 r 6px shadow #ffffff 0px 0px 0px 0px, #737373 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `sales-email-default.png`, `sales-email-focused.png`, `sales-email-filled.png`.

#### sales-message

Message textarea. The "Tell us about your company's needs" textarea; focused only.

Page: sales. Selector: `textarea`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 750 x 118 | = |
| Padding | 8px 12px | = |
| Border | 1px solid #d4d4d4 | 1px solid #737373 |
| Radius | 6px | = |
| Background | #ffffff | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #737373 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #171717 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #a3a3a3, opacity 1 | = |
| Painted layers | textarea.block.w-full 750.0x118.0 bg #ffffff border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 6px | textarea.block.w-full 750.0x118.0 bg #ffffff border T:1px solid #737373 / R:1px solid #737373 / B:1px solid #737373 / L:1px solid #737373 r 6px shadow #ffffff 0px 0px 0px 0px, #737373 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field |

Crops: `sales-message-default.png`, `sales-message-focused.png`.

#### sales-topic

Topic option. A selectable topic pill on the contact form (Tools/Legal/…); toggled, never submitted.

Page: sales. Selector: `topic pill button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 57.52 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #737373 | #404040 | = | #404040 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.075s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #737373 | 14 x 14, colour #404040 | = | 14 x 14, colour #404040 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.sm:inline-flex.flex 57.5x20.0 outline 1px auto #005fcc offset 0px | = |

Crops: `sales-topic-default.png`, `sales-topic-hover.png`, `sales-topic-focus-visible.png`, `sales-topic-pressed.png`.

#### sales-submit

Send button. The Send-message submit; measured, never pressed (a press would submit the form).

Page: sales. Selector: `button "Send message"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 123.75 x 40 | = | - | = |
| Padding | 0px 12px | = | - | = |
| Gap | 8px | = | - | = |
| Border | 1px solid #e5e5e5 | = | - | = |
| Radius | 8px | = | - | = |
| Background | #f5f5f5 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | - | = |
| Font | Inter 14px/20px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #737373 | = | - | = |
| Text node | div.min-w-0.truncate: Inter 14px/20px 400, #737373 | = | - | = |
| Transition | none | = | - | = |
| Cursor | not-allowed | = | - | = |
| Painted layers | button.group.flex 123.8x40.0 bg #f5f5f5 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `sales-submit-default.png`, `sales-submit-hover.png`, `sales-submit-pressed.png`.

### Log in and sign up

#### login-card

Login card. The centred sign-in column (heading, email form, SSO buttons); never filled past a deleted sample, never submitted.

Page: login. Selector: `login card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 384 x 562 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.text-center.text-xl: ui-sans-serif 20px/28px 600, #000000 |
| Transition | none |
| Icon | 16 x 16, colour #171717, fill #000000 |
| Painted layers | input.block.w-full 376.0x38.0 bg #ffffff border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; button.group.flex 376.0x40.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 8px; div.grow.basis-0 171.3x1.0 border B:1px solid #e5e5e5; div.grow.basis-0 171.3x1.0 border B:1px solid #e5e5e5; button.group.flex 376.0x40.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px; button.group.flex 376.0x40.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `login-card-default.png`.

#### email-field

Email field. The email input; sample text was typed and deleted, nothing sent.

Page: login. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 376 x 38 | = | = |
| Padding | 8px 12px | = | = |
| Border | 1px solid #d4d4d4 | 1px solid #000000 | 1px solid #000000 |
| Radius | 6px | = | = |
| Background | #ffffff | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | #ffffff 0px 0px 0px 0px, #000000 0px 0px 0px 1px, #000000 @ 0.05 0px 1px 2px 0px | #ffffff 0px 0px 0px 0px, #000000 0px 0px 0px 1px, #000000 @ 0.05 0px 1px 2px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px | 2px solid #000000 @ 0 offset 2px |
| Font | ui-sans-serif 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #a3a3a3, opacity 1 | = | = |
| Painted layers | input.block.w-full 376.0x38.0 bg #ffffff border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | input.block.w-full 376.0x38.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 6px shadow #ffffff 0px 0px 0px 0px, #000000 0px 0px 0px 1px, #000000 @ 0.05 0px 1px 2px 0px outline 2px solid #000000 @ 0 offset 2px | input.block.w-full 376.0x38.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 6px shadow #ffffff 0px 0px 0px 0px, #000000 0px 0px 0px 1px, #000000 @ 0.05 0px 1px 2px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `email-field-default.png`, `email-field-focused.png`, `email-field-filled.png`.

#### email-submit

Email submit. The "Log in with email" submit; measured, never pressed (a press would start a sign-in).

Page: login. Selector: `button "Log in with email"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 376 x 40 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = | #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | ui-sans-serif 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.min-w-0.truncate: ui-sans-serif 14px/20px 400, #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.group.flex 376.0x40.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 8px | button.group.flex 376.0x40.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 8px shadow #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | button.group.flex 376.0x40.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 8px outline 1px auto #005fcc offset 0px | button.group.flex 376.0x40.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 8px shadow #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `email-submit-default.png`, `email-submit-hover.png`, `email-submit-focus-visible.png`, `email-submit-pressed.png`.

#### oauth-google

Google SSO. The Continue-with-Google button; measured, never followed.

Page: login. Selector: `"Continue with Google"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 376 x 40 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e5e5e5 | = | 1px solid #a3a3a3 | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #fafafa | = | #fafafa |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | ui-sans-serif 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Text node | div.min-w-0.truncate: ui-sans-serif 14px/20px 400, #171717 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #171717, fill #000000 | = | = | = |
| Painted layers | button.group.flex 376.0x40.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px | button.group.flex 376.0x40.0 bg #fafafa border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px | button.group.flex 376.0x40.0 bg #ffffff border T:1px solid #a3a3a3 / R:1px solid #a3a3a3 / B:1px solid #a3a3a3 / L:1px solid #a3a3a3 r 8px outline 2px solid #000000 @ 0 offset 2px | button.group.flex 376.0x40.0 bg #fafafa border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `oauth-google-default.png`, `oauth-google-hover.png`, `oauth-google-focus-visible.png`, `oauth-google-pressed.png`.

#### oauth-github

GitHub SSO. The Continue-with-GitHub button; measured, never followed.

Page: login. Selector: `"Continue with GitHub"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 376 x 40 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e5e5e5 | = | 1px solid #a3a3a3 | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #fafafa | = | #fafafa |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | ui-sans-serif 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Text node | div.min-w-0.truncate: ui-sans-serif 14px/20px 400, #171717 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | = | = | = |
| Painted layers | button.group.flex 376.0x40.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px | button.group.flex 376.0x40.0 bg #fafafa border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px | button.group.flex 376.0x40.0 bg #ffffff border T:1px solid #a3a3a3 / R:1px solid #a3a3a3 / B:1px solid #a3a3a3 / L:1px solid #a3a3a3 r 8px outline 2px solid #000000 @ 0 offset 2px | button.group.flex 376.0x40.0 bg #fafafa border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `oauth-github-default.png`, `oauth-github-hover.png`, `oauth-github-focus-visible.png`, `oauth-github-pressed.png`.

#### oauth-saml

SAML SSO. The Continue-with-SAML-SSO button; measured, never followed.

Page: login. Selector: `"Continue with SAML SSO"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 376 x 40 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e5e5e5 | = | 1px solid #a3a3a3 | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #fafafa | = | #fafafa |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | ui-sans-serif 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Text node | div.min-w-0.truncate: ui-sans-serif 14px/20px 400, #171717 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #171717 | = | = | = |
| Painted layers | button.group.flex 376.0x40.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px | button.group.flex 376.0x40.0 bg #fafafa border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px | button.group.flex 376.0x40.0 bg #ffffff border T:1px solid #a3a3a3 / R:1px solid #a3a3a3 / B:1px solid #a3a3a3 / L:1px solid #a3a3a3 r 8px outline 2px solid #000000 @ 0 offset 2px | button.group.flex 376.0x40.0 bg #fafafa border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `oauth-saml-default.png`, `oauth-saml-hover.png`, `oauth-saml-focus-visible.png`, `oauth-saml-pressed.png`.

#### auth-link

Auth switch link. The "Sign up" link under the card; measured never followed.

Page: login. Selector: `a "Sign up"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50.7 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | ui-sans-serif 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #404040 | #171717 | = | #171717 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.font-semibold.text-neutral-700 50.7x17.0 outline 1px auto #005fcc offset 1px | = |

Crops: `auth-link-default.png`, `auth-link-hover.png`, `auth-link-focus-visible.png`, `auth-link-pressed.png`.

#### register-card

Register card. The centred create-account column; never filled or submitted.

Page: register. Selector: `register card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 384 x 510 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.text-center.text-xl: ui-sans-serif 20px/28px 600, #000000 |
| Transition | none |
| Icon | 16 x 16, colour #171717, fill #000000 |
| Painted layers | input.w-full.max-w-md 376.0x38.0 bg #ffffff border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 6px; button.group.flex 376.0x40.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 8px; div.grow.basis-0 171.3x1.0 border B:1px solid #e5e5e5; div.grow.basis-0 171.3x1.0 border B:1px solid #e5e5e5; button.group.flex 376.0x40.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px; button.group.flex 376.0x40.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `register-card-default.png`.

#### register-field

Register email field. The signup email input; focused only, never filled or submitted.

Page: register. Selector: `register input[type=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 376 x 38 | = |
| Padding | 8px 12px | = |
| Border | 1px solid #d4d4d4 | 1px solid #737373 |
| Radius | 6px | = |
| Background | #ffffff | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #737373 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px |
| Font | ui-sans-serif 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #171717 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #a3a3a3, opacity 1 | = |
| Painted layers | input.w-full.max-w-md 376.0x38.0 bg #ffffff border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 6px | input.w-full.max-w-md 376.0x38.0 bg #ffffff border T:1px solid #737373 / R:1px solid #737373 / B:1px solid #737373 / L:1px solid #737373 r 6px shadow #ffffff 0px 0px 0px 0px, #737373 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field |

Crops: `register-field-default.png`, `register-field-focused.png`.

### Docs and help (Mintlify)

#### docs-sidebar

Docs sidebar. The left docs navigation column.

Page: docs. Selector: `docs sidebar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 288 x 804 |
| Padding | 0px |
| Border | T: none; R: 1px solid #eef0f5; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #707277 |
| Text node | span: Inter 12px/16px 700, #17191e |
| Transition | transform, translate, scale, rotate 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 20 x 8, colour #9fa1a6, fill #000000 |
| Painted layers | nav.hidden.sticky 288.0x804.0 border R:1px solid #eef0f5; a.group.flex 267.0x32.0 bg #155dfc @ 0.1 r 12px; div.sidebar-nav-group-divider.h-px 259.0x1.0 bg #eef0f5; div.sidebar-nav-group-divider.h-px 259.0x1.0 bg #eef0f5; div.sidebar-nav-group-divider.h-px 259.0x1.0 bg #eef0f5; div.z-10.flex 4.0x772.0 bg #fafafa r 9999px |
| How | at rest |

Crops: `docs-sidebar-default.png`.

#### docs-nav-item

Docs nav item. A sidebar navigation item.

Page: docs. Selector: `docs nav item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 267 x 32 | = | = | = |
| Padding | 6px 12px 6px 16px | = | = | = |
| Gap | normal 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #155dfc @ 0.1 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #155dfc offset -2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #155dfc | = | = | = |
| Text node | span.min-w-0.max-w-full: Inter 14px/20px 400, #155dfc | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.flex 267.0x32.0 bg #155dfc @ 0.1 r 12px | = | a.group.flex 267.0x32.0 bg #155dfc @ 0.1 r 12px outline 1px auto #155dfc offset -2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-nav-item-default.png`, `docs-nav-item-hover.png`, `docs-nav-item-focus-visible.png`, `docs-nav-item-pressed.png`.

#### docs-search

Search trigger. The "Search… ⌘K" trigger; measured, the palette was never opened.

Page: docs. Selector: `"Search…"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 384 x 36 | = | = | = |
| Padding | 0px 12px 0px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #0a0d11 @ 0.03 | #0a0d11 @ 0.1 | = | #0a0d11 @ 0.1 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9fa1a6 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #505257 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #505257 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | 1px auto #155dfc offset 0px | = |
| Font | Inter 14px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #707277 | = | = | = |
| Text node | div.truncate.min-w-0: Inter 14px/24px 400, #707277 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #3f4146, fill #000000 | 16 x 16, colour #25282d, fill #000000 | = | 16 x 16, colour #25282d, fill #000000 |
| Painted layers | button.group/search.flex 384.0x36.0 bg #0a0d11 @ 0.03 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9fa1a6 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.group/search.flex 384.0x36.0 bg #0a0d11 @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #505257 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.group/search.flex 384.0x36.0 bg #0a0d11 @ 0.03 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9fa1a6 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #155dfc offset 0px | button.group/search.flex 384.0x36.0 bg #0a0d11 @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #505257 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-search-default.png`, `docs-search-hover.png`, `docs-search-focus-visible.png`, `docs-search-pressed.png`.

#### docs-theme

Theme toggle. The "Change theme preference" button; its dropdown supplied the docs dark shots.

Page: docs. Selector: `theme preference button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 30 x 30 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #25282d @ 0.04 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #155dfc offset 0px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0d11 @ 0.5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 16, colour #505257, fill #000000 | 14 x 16, colour #25282d, fill #000000 | = | 14 x 16, colour #25282d, fill #000000 |
| Painted layers | button.group.disabled:pointer-events-none 30.0x30.0 bg #25282d @ 0.04 r 9999px | = | button.group.disabled:pointer-events-none 30.0x30.0 bg #25282d @ 0.04 r 9999px outline 1px auto #155dfc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-theme-default.png`, `docs-theme-hover.png`, `docs-theme-focus-visible.png`, `docs-theme-pressed.png`.

#### docs-h1

Docs headline. The docs page h1 (Introduction).

Page: docs. Selector: `docs h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 194.67 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Satoshi 36px/40px 600 |
| Letter spacing | -0.9px |
| Colour | #17191e |
| Transition | none |
| How | at rest |

Crops: `docs-h1-default.png`.

#### docs-copy

Copy-page button. The "Copy page" action; measured, never pressed.

Page: docs. Selector: `"Copy page"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 121.55 x 34 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Border | T: 1px solid #dfe1e6; R: none; B: 1px solid #dfe1e6; L: 1px solid #dfe1e6 | = | = | = |
| Radius | 12px 0px 0px 12px | = | = | = |
| Background | #ffffff | #505257 @ 0.05 | = | #505257 @ 0.05 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #155dfc offset 0px | = |
| Font | Inter 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #3f4146 | = | = | = |
| Text node | span.col-start-1.row-start-1: Inter 14px/20px 500, #3f4146 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #3f4146, fill #000000 | = | = | = |
| Painted layers | button.rounded-l-xl.px-3 121.5x34.0 bg #ffffff border T:1px solid #dfe1e6 / B:1px solid #dfe1e6 / L:1px solid #dfe1e6 r 12px 0px 0px 12px | button.rounded-l-xl.px-3 121.5x34.0 bg #505257 @ 0.05 border T:1px solid #dfe1e6 / B:1px solid #dfe1e6 / L:1px solid #dfe1e6 r 12px 0px 0px 12px | button.rounded-l-xl.px-3 121.5x34.0 bg #ffffff border T:1px solid #dfe1e6 / B:1px solid #dfe1e6 / L:1px solid #dfe1e6 r 12px 0px 0px 12px outline 1px auto #155dfc offset 0px | button.rounded-l-xl.px-3 121.5x34.0 bg #505257 @ 0.05 border T:1px solid #dfe1e6 / B:1px solid #dfe1e6 / L:1px solid #dfe1e6 r 12px 0px 0px 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-copy-default.png`, `docs-copy-hover.png`, `docs-copy-focus-visible.png`, `docs-copy-pressed.png`.

#### docs-feedback

Feedback button. A docs "Was this helpful" Yes/No button; measured, never pressed (a press would send feedback).

Page: docs. Selector: `feedback Yes button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81.98 x 34 | = | = | = |
| Padding | 8px 14px | = | = | = |
| Gap | 12px | = | = | = |
| Border | 1px solid #dfe1e6 @ 0.7 | 1px solid #707277 | = | 1px solid #707277 |
| Radius | 12px | = | = | = |
| Background | #ffffff @ 0.5 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #155dfc offset -2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #505257 | #3f4146 | = | #3f4146 |
| Text node | small.text-sm.font-normal: Inter 14px/16px 400, #505257 | small.text-sm.font-normal: Inter 14px/16px 400, #3f4146 | = | small.text-sm.font-normal: Inter 14px/16px 400, #3f4146 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #505257, fill #000000 | 16 x 16, colour #3f4146, fill #000000 | = | 16 x 16, colour #3f4146, fill #000000 |
| Painted layers | button.px-3.5.py-2 82.0x34.0 bg #ffffff @ 0.5 border T:1px solid #dfe1e6 @ 0.7 / R:1px solid #dfe1e6 @ 0.7 / B:1px solid #dfe1e6 @ 0.7 / L:1px solid #dfe1e6 @ 0.7 r 12px | button.px-3.5.py-2 82.0x34.0 bg #ffffff @ 0.5 border T:1px solid #707277 / R:1px solid #707277 / B:1px solid #707277 / L:1px solid #707277 r 12px | button.px-3.5.py-2 82.0x34.0 bg #ffffff @ 0.5 border T:1px solid #dfe1e6 @ 0.7 / R:1px solid #dfe1e6 @ 0.7 / B:1px solid #dfe1e6 @ 0.7 / L:1px solid #dfe1e6 @ 0.7 r 12px outline 2px solid #155dfc offset -2px | button.px-3.5.py-2 82.0x34.0 bg #ffffff @ 0.5 border T:1px solid #707277 / R:1px solid #707277 / B:1px solid #707277 / L:1px solid #707277 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-feedback-default.png`, `docs-feedback-hover.png`, `docs-feedback-focus-visible.png`, `docs-feedback-pressed.png`.

#### docs-nav-tab

Docs nav tab. The docs surface's top navigation tab (API Reference); measured never followed. A docs landing card was never captured — an earlier global locator read this nav tab under the card name.

Page: docs. Selector: `docs top nav tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 118.81 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #155dfc offset 1px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #25282d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #25282d, fill #000000 | = | = | = |
| Painted layers | svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 bg #25282d | svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 bg #25282d; div.absolute.bottom-0 118.8x1.0 bg #dfe1e6 | a.link.nav-tabs-item 118.8x40.0 outline 1px auto #155dfc offset 1px; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 bg #25282d | svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 bg #25282d; div.absolute.bottom-0 118.8x1.0 bg #dfe1e6 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-nav-tab-default.png`, `docs-nav-tab-hover.png`, `docs-nav-tab-focus-visible.png`, `docs-nav-tab-pressed.png`.

#### dk-docs-h1

Docs headline (dark). The docs h1 with html.dark painted — the real dark theme.

Page: docs-dark. Selector: `docs h1 dark`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 194.67 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Satoshi 36px/40px 600 |
| Letter spacing | -0.9px |
| Colour | #dfe1e6 |
| Transition | none |
| How | at rest |

Crops: `dk-docs-h1-default.png`.

#### dk-docs-sidebar

Docs sidebar (dark). The left nav column in dark.

Page: docs-dark. Selector: `docs sidebar dark`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 288 x 804 |
| Padding | 0px |
| Border | T: none; R: 1px solid #ffffff @ 0.1; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #9fa1a6 |
| Text node | span: Inter 12px/16px 700, #dfe1e6 |
| Transition | transform, translate, scale, rotate 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 20 x 8, colour #505257, fill #000000 |
| Painted layers | nav.hidden.sticky 288.0x804.0 border R:1px solid #ffffff @ 0.1; a.group.flex 267.0x32.0 bg #155dfc @ 0.1 r 12px; div.sidebar-nav-group-divider.h-px 259.0x1.0 bg #ffffff @ 0.1; div.sidebar-nav-group-divider.h-px 259.0x1.0 bg #ffffff @ 0.1; div.sidebar-nav-group-divider.h-px 259.0x1.0 bg #ffffff @ 0.1; div.z-10.flex 4.0x772.0 bg #262626 r 9999px |
| How | at rest |

Crops: `dk-docs-sidebar-default.png`.

#### dk-docs-nav-item

Docs nav item (dark). A sidebar item in dark.

Page: docs-dark. Selector: `docs nav item dark`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 267 x 32 | = | = | = |
| Padding | 6px 12px 6px 16px | = | = | = |
| Gap | normal 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #155dfc @ 0.1 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #155dfc offset -2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #155dfc | = | = | = |
| Text node | span.min-w-0.max-w-full: Inter 14px/20px 400, #155dfc | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.flex 267.0x32.0 bg #155dfc @ 0.1 r 12px | = | a.group.flex 267.0x32.0 bg #155dfc @ 0.1 r 12px outline 1px auto #155dfc offset -2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `dk-docs-nav-item-default.png`, `dk-docs-nav-item-hover.png`, `dk-docs-nav-item-focus-visible.png`, `dk-docs-nav-item-pressed.png`.

#### dk-docs-copy

Copy-page button (dark). The "Copy page" action in dark.

Page: docs-dark. Selector: `"Copy page" dark`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 121.55 x 34 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Border | T: 1px solid #ffffff @ 0.07; R: none; B: 1px solid #ffffff @ 0.07; L: 1px solid #ffffff @ 0.07 | = | = | = |
| Radius | 12px 0px 0px 12px | = | = | = |
| Background | #090b10 | #dfe1e6 @ 0.05 | = | #dfe1e6 @ 0.05 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #155dfc offset 0px | = |
| Font | Inter 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ced0d5 | = | = | = |
| Text node | span.col-start-1.row-start-1: Inter 14px/20px 500, #ced0d5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ced0d5, fill #000000 | = | = | = |
| Painted layers | button.rounded-l-xl.px-3 121.5x34.0 bg #090b10 border T:1px solid #ffffff @ 0.07 / B:1px solid #ffffff @ 0.07 / L:1px solid #ffffff @ 0.07 r 12px 0px 0px 12px | button.rounded-l-xl.px-3 121.5x34.0 bg #dfe1e6 @ 0.05 border T:1px solid #ffffff @ 0.07 / B:1px solid #ffffff @ 0.07 / L:1px solid #ffffff @ 0.07 r 12px 0px 0px 12px | button.rounded-l-xl.px-3 121.5x34.0 bg #090b10 border T:1px solid #ffffff @ 0.07 / B:1px solid #ffffff @ 0.07 / L:1px solid #ffffff @ 0.07 r 12px 0px 0px 12px outline 1px auto #155dfc offset 0px | button.rounded-l-xl.px-3 121.5x34.0 bg #dfe1e6 @ 0.05 border T:1px solid #ffffff @ 0.07 / B:1px solid #ffffff @ 0.07 / L:1px solid #ffffff @ 0.07 r 12px 0px 0px 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `dk-docs-copy-default.png`, `dk-docs-copy-hover.png`, `dk-docs-copy-focus-visible.png`, `dk-docs-copy-pressed.png`.

#### dk-docs-search

Search trigger (dark). The "Search…" trigger in dark.

Page: docs-dark. Selector: `"Search…" dark`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 384 x 36 | = | = | = |
| Padding | 0px 12px 0px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff @ 0.03 | #ffffff @ 0.1 | = | #ffffff @ 0.1 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #505257 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #707277 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #707277 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | 1px auto #155dfc offset 0px | = |
| Font | Inter 14px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.5 | = | = | = |
| Text node | div.truncate.min-w-0: Inter 14px/24px 400, #ffffff @ 0.5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #9fa1a6, fill #000000 | 16 x 16, colour #dfe1e6, fill #000000 | = | 16 x 16, colour #dfe1e6, fill #000000 |
| Painted layers | button.group/search.flex 384.0x36.0 bg #ffffff @ 0.03 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #505257 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.group/search.flex 384.0x36.0 bg #ffffff @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #707277 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.group/search.flex 384.0x36.0 bg #ffffff @ 0.03 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #505257 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #155dfc offset 0px | button.group/search.flex 384.0x36.0 bg #ffffff @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #707277 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `dk-docs-search-default.png`, `dk-docs-search-hover.png`, `dk-docs-search-focus-visible.png`, `dk-docs-search-pressed.png`.

### Footer

#### footer

Footer. The marketing footer: wordmark, social icons and the Product/Solutions/Resources/Tools/Company link columns.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 402 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | h3.text-sm.font-medium: Inter 14px/20px 500, #171717 |
| Transition | none |
| Icon | 61.33 x 32, colour #262626 |
| Painted layers | span.flex.size-4 16.0x16.0 bg #c084fc border T:1px solid #000000 @ 0.05 / R:1px solid #000000 @ 0.05 / B:1px solid #000000 @ 0.05 / L:1px solid #000000 @ 0.05 r 4px; span.flex.size-4 16.0x16.0 bg #4ade80 border T:1px solid #000000 @ 0.05 / R:1px solid #000000 @ 0.05 / B:1px solid #000000 @ 0.05 / L:1px solid #000000 @ 0.05 r 4px; span.flex.size-4 16.0x16.0 bg #fb923c border T:1px solid #000000 @ 0.05 / R:1px solid #000000 @ 0.05 / B:1px solid #000000 @ 0.05 / L:1px solid #000000 @ 0.05 r 4px; span.flex.size-4 16.0x16.0 bg #a3a3a3 border T:1px solid #000000 @ 0.05 / R:1px solid #000000 @ 0.05 / B:1px solid #000000 @ 0.05 / L:1px solid #000000 @ 0.05 r 4px; span.flex.size-4 16.0x16.0 bg #c084fc border T:1px solid #000000 @ 0.05 / R:1px solid #000000 @ 0.05 / B:1px solid #000000 @ 0.05 / L:1px solid #000000 @ 0.05 r 4px; span.flex.size-4 16.0x16.0 bg #c084fc border T:1px solid #000000 @ 0.05 / R:1px solid #000000 @ 0.05 / B:1px solid #000000 @ 0.05 / L:1px solid #000000 @ 0.05 r 4px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 164 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #737373 | #404040 | = | #404040 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.075s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.flex.items-center 164.0x20.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-link

Social icon link. A social icon button in the footer (Twitter/GitHub/LinkedIn/YouTube).

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #171717, fill #000000 | 16 x 16, colour #525252, fill #000000 | = | 16 x 16, colour #525252, fill #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.group.rounded-full 24.0x24.0 r 9999px outline 1px auto #005fcc offset 1px | = |

Crops: `social-link-default.png`, `social-link-hover.png`, `social-link-focus-visible.png`, `social-link-pressed.png`.

### Mobile (390 wide)

#### m-nav

Mobile nav. The sticky top bar at 390 (wordmark + menu button).

Page: mobile. Selector: `top bar at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 46 x 24, colour #000000 |
| Painted layers | div.absolute.inset-0 390.0x56.0 border B:1px solid #000000 @ 0; div.pointer-events-none.absolute 0.0x0.0 bg #171717 @ 0.05 r 8px; a.transition-all.border-border-subtle 0.0x0.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px; a.transition-all.border-black 0.0x0.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 8px |
| Ancestor paint | 1 up div.relative.z-10 bg #ffffff |
| How | at rest |

Crops: `m-nav-default.png`.

#### m-menu-button

Menu button. The round menu toggle in the mobile nav.

Page: mobile. Selector: `mobile menu button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 36 x 36 |
| Padding | 8px |
| Border | none |
| Radius | 9999px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 20 x 20, colour #525252 |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The menu panel opened by its own toggle.

Page: mobile. Selector: `mobile menu panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 64px 20px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | p.font-semibold: Inter 16px/24px 600, #0a0a0a |
| Transition | none |
| Icon | 20 x 20, colour #737373 |
| Painted layers | nav.fixed.inset-0 390.0x844.0 bg #ffffff; li.py-3 350.0x49.0 border T:1px solid #e5e5e5; li.py-3 350.0x49.0 border T:1px solid #e5e5e5; li.py-3 350.0x49.0 border T:1px solid #e5e5e5; li.py-3 350.0x49.0 border T:1px solid #e5e5e5; li.py-3 350.0x49.0 border T:1px solid #e5e5e5 |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. An item inside the opened mobile menu.

Page: mobile. Selector: `mobile menu item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 350 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Text node | p.font-semibold: Inter 16px/24px 600, #0a0a0a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #737373 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.flex.w-full 350.0x24.0 outline 1px auto #005fcc offset 0px | = |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 294 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | satoshi 36px/40px 500 |
| Letter spacing | normal |
| Colour | #171717 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

dub.co serves its Next.js and Mintlify CSS bundles same-origin (the fontshare sheet was read from network responses), so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- docs: `top 0.16s cubic-bezier(0.25, 0.75, 0.2, 1)`, `width var(--duration-long) var(--timing),height var(--duration-long) var(--timing),background var(--duration-short) ease,scale var(--duration-short) var(--timing)`, `none`, `border-color 0.3s`, `filter 0.35s, opacity 0.35s`, `opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1)`, `opacity var(--lightbox-pull-snap-duration,var(--lightbox-vt-duration)) var(--lightbox-pull-snap-easing,var(--lightbox-vt-root-easing))`, `opacity var(--lightbox-vt-duration) var(--lightbox-vt-root-easing)`, `opacity 0.2s, visibility linear`, `opacity 0.2s, visibility linear 0.2s`, `opacity 0.2s`

- home: `opacity 0.3s`, `transform 0.5s cubic-bezier(0.32, 0.72, 0, 1)`, `opacity 0.5s cubic-bezier(0.32, 0.72, 0, 1)`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- login: `transform 0.5s cubic-bezier(0.32, 0.72, 0, 1)`, `opacity 0.5s cubic-bezier(0.32, 0.72, 0, 1)`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- pricing: `opacity 0.3s`, `transform 0.5s cubic-bezier(0.32, 0.72, 0, 1)`, `opacity 0.5s cubic-bezier(0.32, 0.72, 0, 1)`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- sales: `opacity 0.3s`, `transform 0.5s cubic-bezier(0.32, 0.72, 0, 1)`, `opacity 0.5s cubic-bezier(0.32, 0.72, 0, 1)`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`
