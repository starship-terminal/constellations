# Component measurements

Computed styles read from boords.com on 2026-11-11 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) in the site's one light theme, with any consent overlay hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header pill. The floating rounded-full header bar: logo, nav, menu button, Book a demo.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1344 x 64 |
| Padding | 0px 8px 0px 32px |
| Border | none |
| Radius | 9999px |
| Background | transparent |
| Box shadow | #ffffff 0px 0px 0px 0px, #121212 @ 0.04 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | matter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: matter 14.4px/18px 400, #121212 @ 0.6 |
| Transition | box-shadow 0.3s cubic-bezier(0, 0, 0.2, 1) |
| Icon | 16 x 16, colour #121212 @ 0.6 |
| Painted layers | header.pointer-events-auto.relative 1344.0x64.0 r 9999px shadow #ffffff 0px 0px 0px 0px, #121212 @ 0.04 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; span.pointer-events-none.absolute 1344.0x64.0 bg #ffffff r 9999px; a.relative.z-40 0.0x0.0 bg #121212 r 9999px; a.px-5.text-center 158.3x42.0 bg #121212 border T:3px solid #121212 / R:3px solid #121212 / B:3px solid #121212 / L:3px solid #121212 r 9999px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo.

Page: home. Selector: `header a[href="/"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 160 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | matter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 3 up header.pointer-events-auto.relative shadow #ffffff 0px 0px 0px 0px, #121212 @ 0.04 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link.

Page: home. Selector: `header a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 69.17 x 28 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #121212 @ 0.05 | = | #121212 @ 0.05 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | matter 14.4px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #121212 @ 0.6 | #121212 | = | #121212 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.whitespace-nowrap.rounded-full 69.2x28.0 bg #121212 @ 0.05 r 9999px | a.whitespace-nowrap.rounded-full 69.2x28.0 r 9999px outline 1px auto #005fcc offset 1px | a.whitespace-nowrap.rounded-full 69.2x28.0 bg #121212 @ 0.05 r 9999px |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-trigger

Nav dropdown. A nav-menu-trigger in the header; opens a flyout.

Page: home. Selector: `button.nav-menu-trigger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 101.33 x 30 | = | = | 98.29 x 29.1 |
| Padding | 6px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #121212 @ 0.05 | #121212 @ 0.05 | #121212 @ 0.05 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | matter 14.4px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #121212 @ 0.6 | #121212 | #121212 | #121212 |
| Text node | span: matter 14.4px/18px 400, #121212 @ 0.6 | span: matter 14.4px/18px 400, #121212 | span: matter 14.4px/18px 400, #121212 | span: matter 14.4px/18px 400, #121212 |
| Transition | color, background-color, transform 0.2s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #121212 @ 0.6 | 16 x 16, colour #121212 | 16 x 16, colour #121212 | 15.52 x 15.52, colour #121212 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.nav-menu-trigger.group 101.3x30.0 bg #121212 @ 0.05 r 9999px | button.nav-menu-trigger.group 101.3x30.0 bg #121212 @ 0.05 r 9999px outline 1px auto #005fcc offset 0px | button.nav-menu-trigger.group 98.3x29.1 bg #121212 @ 0.05 r 9999px |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### nav-trigger-open

Nav dropdown, open. After its own toggle; the opened flyout shows in the crop.

Page: home. Selector: `button.nav-menu-trigger`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 101.33 x 30 |
| Padding | 6px 12px |
| Border | none |
| Radius | 9999px |
| Background | #121212 @ 0.05 |
| Box shadow | none |
| Outline | none |
| Font | matter 14.4px/18px 400 |
| Letter spacing | normal |
| Colour | #121212 |
| Text node | span: matter 14.4px/18px 400, #121212 |
| Transition | color, background-color, transform 0.2s cubic-bezier(0, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 16 x 16, colour #121212 |
| Painted layers | button.nav-menu-trigger.group 101.3x30.0 bg #121212 @ 0.05 r 9999px |
| How | own toggle |

Crops: `nav-trigger-open-opened.png`.

#### menu-button

Menu button. The round icon button that opens the site menu.

Page: home. Selector: `button[aria-label="Open menu"]`. States: .

Not found on the page at capture time.

#### cta-demo

Book a demo CTA. The header CTA; links to the demo form, measured never followed.

Page: home. Selector: `a[href^="/demo"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 111.13 x 30 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #121212 @ 0.05 | = | #121212 @ 0.05 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | matter 14.4px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #121212 @ 0.6 | #121212 | = | #121212 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.hidden.whitespace-nowrap 111.1x30.0 bg #121212 @ 0.05 r 9999px | a.hidden.whitespace-nowrap 111.1x30.0 r 9999px outline 1px auto #005fcc offset 1px | a.hidden.whitespace-nowrap 111.1x30.0 bg #121212 @ 0.05 r 9999px |

Crops: `cta-demo-default.png`, `cta-demo-hover.png`, `cta-demo-focus-visible.png`, `cta-demo-pressed.png`.

### Home

#### hero-title

Hero headline.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1152 x 133.09 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | matter 64px/66.56px 600 |
| Letter spacing | -1.6px |
| Colour | #121212 |
| Text node | span.whitespace-nowrap: matter 64px/66.56px 600, #121212, ls -1.6px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-cta

Hero CTA. The hero action; measured never followed.

Page: home. Selector: `main a CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 222.31 x 56 | = | = | 211.2 x 53.2 |
| Padding | 12px 40px | = | = | = |
| Border | 1px solid #e8aa42 | 1px solid #d89b3c | = | 1px solid #d89b3c |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(to right bottom, #f4bd64 @ 0.8, #f4bd64) | linear-gradient(to right bottom, #f4bd64, #f4bd64) | = | linear-gradient(to right bottom, #f4bd64, #f4bd64) |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #6cbce4 @ 0.2 0px 4px 6px -1px, #6cbce4 @ 0.2 0px 2px 4px -2px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #6cbce4 @ 0.2 0px 4px 6px -1px, #6cbce4 @ 0.2 0px 2px 4px -2px |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | matter 20px/30px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #121212 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.px-5.text-center 222.3x56.0 image linear-gradient(to right bottom, #f4bd64 @ 0.8, #f4bd64) border T:1px solid #e8aa42 / R:1px solid #e8aa42 / B:1px solid #e8aa42 / L:1px solid #e8aa42 r 9999px | a.px-5.text-center 222.3x56.0 image linear-gradient(to right bottom, #f4bd64, #f4bd64) border T:1px solid #d89b3c / R:1px solid #d89b3c / B:1px solid #d89b3c / L:1px solid #d89b3c r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #6cbce4 @ 0.2 0px 4px 6px -1px, #6cbce4 @ 0.2 0px 2px 4px -2px | a.px-5.text-center 222.3x56.0 image linear-gradient(to right bottom, #f4bd64 @ 0.8, #f4bd64) border T:1px solid #e8aa42 / R:1px solid #e8aa42 / B:1px solid #e8aa42 / L:1px solid #e8aa42 r 9999px outline 2px solid #000000 @ 0 offset 2px | a.px-5.text-center 211.2x53.2 image linear-gradient(to right bottom, #f4bd64, #f4bd64) border T:1px solid #d89b3c / R:1px solid #d89b3c / B:1px solid #d89b3c / L:1px solid #d89b3c r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #6cbce4 @ 0.2 0px 4px 6px -1px, #6cbce4 @ 0.2 0px 2px 4px -2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.95, 0, 0, 0.95, 0, 0) |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-sub

Hero copy. The lede paragraph under the headline.

Page: home. Selector: `hero paragraph`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 553.88 x 21.68 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | matter 14.4px/25.2px 400 |
| Letter spacing | normal |
| Colour | #7b7b7b |
| Transition | none |
| Ancestor paint | 3 up div.rounded-t-sm.bg-white bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest |

Crops: `hero-sub-default.png`.

#### feature-card

Feature card. A card-surface section card on the home page.

Page: home. Selector: `.card-surface`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 324 x 256 |
| Padding | 24px |
| Gap | 24px |
| Border | none |
| Radius | 24px |
| Background | #f3f3e9 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | matter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #121212 |
| Text node | span.text-sm.font-semibold: matter 14.4px/18px 600, #121212 |
| Transition | none |
| Cursor | pointer |
| Icon | 16 x 16, colour #121212 |
| Painted layers | a.card-surface.group 324.0x256.0 bg #f3f3e9 r 24px shadow #000000 @ 0 0px 0px 0px 0px; span.flex.h-8 32.0x32.0 bg #121212 @ 0.06 r 9999px |
| How | at rest |

Crops: `feature-card-default.png`.

#### feature-link

Feature link.

Page: home. Selector: `main link`. States: .

Not found on the page at capture time.

### Pricing

#### price-title

Pricing title.

Page: pricing. Selector: `h1/h2 on /pricing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 817.91 x 133.09 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | matter 64px/66.56px 600 |
| Letter spacing | -1.6px |
| Colour | #121212 |
| Text node | span: matter 64px/66.56px 600, #121212, ls -1.6px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `price-title-default.png`.

#### billing-tab

Billing tab. A monthly/yearly billing tab; toggled for the yearly screenshot, left on default.

Page: pricing. Selector: `button[role="tab"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 84.88 x 36 | = | = | = |
| Padding | 6px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | = | #ffffff 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | matter 14.4px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #121212 | = | = | = |
| Text node | span: matter 14.4px/18px 400, #121212 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.rounded-full.px-4 84.9x36.0 bg #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px outline 2px solid #000000 @ 0 offset 2px | = | button.rounded-full.px-4 84.9x36.0 bg #ffffff r 9999px shadow #ffffff 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px outline 2px solid #000000 @ 0 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `billing-tab-default.png`, `billing-tab-hover.png`, `billing-tab-focus-visible.png`, `billing-tab-pressed.png`.

#### plan-card

Plan card. One plan tier card (the rounded-card surfaces).

Page: pricing. Selector: `.card-surface`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 324 x 423.8 |
| Padding | 0px |
| Border | none |
| Radius | 24px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.04 0px 0px 0px 1px |
| Outline | none |
| Font | matter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.text-title.font-semibold: matter 20px/26px 600, #000000 |
| Transition | none |
| Icon | 20 x 20, colour #121212 |
| Painted layers | div.card-surface.relative 324.0x423.8 bg #ffffff r 24px shadow #000000 @ 0.04 0px 0px 0px 1px; a.border-b.border-[#CECDCA]/60 85.7x19.0 border B:1px solid #cecdca @ 0.6; a.border-b.border-[#CECDCA]/60 175.6x19.0 border B:1px solid #cecdca @ 0.6; span.border-b.border-[#CECDCA]/60 116.5x19.0 border B:1px solid #cecdca @ 0.6; a.px-5.text-center 268.0x42.0 bg #121212 border T:3px solid #121212 / R:3px solid #121212 / B:3px solid #121212 / L:3px solid #121212 r 9999px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-price

Plan price. A plan price figure inside a tier card.

Page: pricing. Selector: `.card-surface span with a $ amount`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 43.89 x 40.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | matter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.text-lg: matter 20px/30px 400, #000000 |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. A tier action; measured never followed or pressed.

Page: pricing. Selector: `plan card CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 268 x 42 | = | = | 254.6 x 39.9 |
| Padding | 6px 20px | = | = | = |
| Border | 3px solid #121212 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | matter 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #121212 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.px-5.text-center 268.0x42.0 border T:3px solid #121212 / R:3px solid #121212 / B:3px solid #121212 / L:3px solid #121212 r 9999px | = | a.px-5.text-center 268.0x42.0 border T:3px solid #121212 / R:3px solid #121212 / B:3px solid #121212 / L:3px solid #121212 r 9999px outline 2px solid #000000 @ 0 offset 2px | a.px-5.text-center 254.6x39.9 border T:3px solid #121212 / R:3px solid #121212 / B:3px solid #121212 / L:3px solid #121212 r 9999px |
| Ancestor paint | 3 up div.card-surface.relative bg #ffffff shadow #000000 @ 0.04 0px 0px 0px 1px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.95, 0, 0, 0.95, 0, 0) |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### feature-row

Feature row. A comparison-table row/accordion.

Page: pricing. Selector: `button[aria-expanded]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 882.67 x 80 | = | = | = |
| Padding | 24px 28px | = | = | = |
| Gap | 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 0px, #121212 @ 0.4 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | matter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | h3.text-title.font-semibold: matter 20px/26px 600, #121212 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #121212 @ 0.6 | = | = | = |
| Painted layers | span.flex.size-8 32.0x32.0 bg #121212 @ 0.05 r 9999px | = | button.flex.w-full 882.7x80.0 r 24px shadow #ffffff 0px 0px 0px 0px, #121212 @ 0.4 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px; span.flex.size-8 32.0x32.0 bg #121212 @ 0.05 r 9999px | = |
| Ancestor paint | 1 up div.card-surface.rounded-card bg #ffffff shadow #000000 @ 0.04 0px 0px 0px 1px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `feature-row-default.png`, `feature-row-hover.png`, `feature-row-focus-visible.png`, `feature-row-pressed.png`.

#### feature-row-open

Feature row, open. The accordion row after its own toggle.

Page: pricing. Selector: `button[aria-expanded]`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 882.67 x 80 |
| Padding | 24px 28px |
| Gap | 24px |
| Border | none |
| Radius | 24px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | matter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.text-title.font-semibold: matter 20px/26px 600, #121212 |
| Transition | none |
| Cursor | pointer |
| Icon | 16 x 16, colour #121212 @ 0.6 |
| Painted layers | span.flex.size-8 32.0x32.0 bg #121212 @ 0.05 r 9999px |
| Ancestor paint | 1 up div.card-surface.rounded-card bg #ffffff shadow #000000 @ 0.04 0px 0px 0px 1px |
| How | own toggle |

Crops: `feature-row-open-opened.png`.

### Public tools

#### timer-display

Timer display. The script timer readout on the public tool page.

Page: script-timer. Selector: `timer element`. States: .

Not found on the page at capture time.

#### timer-field

Script field. The paste-your-script textarea; filled with sample text and cleared, never submitted.

Page: script-timer. Selector: `textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 552 x 331 | = | 552 x 390.81 |
| Padding | 12px 16px | = | = |
| Border | 1px solid #121212 @ 0.1 | 1px solid #121212 @ 0.4 | 1px solid #121212 @ 0.4 |
| Radius | 16px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #b77a1e @ 0.3 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | #ffffff 0px 0px 0px 0px, #b77a1e @ 0.3 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px | 2px solid #000000 @ 0 offset 2px |
| Font | matter 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #121212 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #121212 @ 0.6, opacity 1 | = | = |
| Painted layers | textarea.mt-5.min-h-80 552.0x331.0 bg #ffffff border T:1px solid #121212 @ 0.1 / R:1px solid #121212 @ 0.1 / B:1px solid #121212 @ 0.1 / L:1px solid #121212 @ 0.1 r 16px | textarea.mt-5.min-h-80 552.0x331.0 bg #ffffff border T:1px solid #121212 @ 0.4 / R:1px solid #121212 @ 0.4 / B:1px solid #121212 @ 0.4 / L:1px solid #121212 @ 0.4 r 16px shadow #ffffff 0px 0px 0px 0px, #b77a1e @ 0.3 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | textarea.mt-5.min-h-80 552.0x390.8 bg #ffffff border T:1px solid #121212 @ 0.4 / R:1px solid #121212 @ 0.4 / B:1px solid #121212 @ 0.4 / L:1px solid #121212 @ 0.4 r 16px shadow #ffffff 0px 0px 0px 0px, #b77a1e @ 0.3 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up div.card-surface.rounded-card bg #ffffff shadow #000000 @ 0.04 0px 0px 0px 1px | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `timer-field-default.png`, `timer-field-focused.png`, `timer-field-filled.png`.

#### timer-toggle

Timer toggle. An aria-pressed option toggle on the timer.

Page: script-timer. Selector: `button[aria-pressed]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 178.66 x 66.41 | = | = | = |
| Padding | 12px 8px | = | = | = |
| Border | 1px solid #121212 @ 0.15 | 1px solid #121212 @ 0.3 | = | 1px solid #121212 @ 0.3 |
| Radius | 16px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #121212 @ 0.4 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | matter 14.4px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #121212 @ 0.7 | #121212 | = | #121212 |
| Text node | span.block: matter 14.4px/18px 500, #121212 @ 0.7 | span.block: matter 14.4px/18px 500, #121212 | = | span.block: matter 14.4px/18px 500, #121212 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.rounded-media.border 178.7x66.4 bg #ffffff border T:1px solid #121212 @ 0.15 / R:1px solid #121212 @ 0.15 / B:1px solid #121212 @ 0.15 / L:1px solid #121212 @ 0.15 r 16px | button.rounded-media.border 178.7x66.4 bg #ffffff border T:1px solid #121212 @ 0.3 / R:1px solid #121212 @ 0.3 / B:1px solid #121212 @ 0.3 / L:1px solid #121212 @ 0.3 r 16px | button.rounded-media.border 178.7x66.4 bg #ffffff border T:1px solid #121212 @ 0.15 / R:1px solid #121212 @ 0.15 / B:1px solid #121212 @ 0.15 / L:1px solid #121212 @ 0.15 r 16px shadow #ffffff 0px 0px 0px 2px, #121212 @ 0.4 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | button.rounded-media.border 178.7x66.4 bg #ffffff border T:1px solid #121212 @ 0.3 / R:1px solid #121212 @ 0.3 / B:1px solid #121212 @ 0.3 / L:1px solid #121212 @ 0.3 r 16px |
| Ancestor paint | 3 up div.card-surface.flex bg #ffffff shadow #000000 @ 0.04 0px 0px 0px 1px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `timer-toggle-default.png`, `timer-toggle-hover.png`, `timer-toggle-focus-visible.png`, `timer-toggle-pressed.png`.

### Product pages

#### page-title

Product page title.

Page: ai-storyboard. Selector: `h1 on /ai-storyboard-generator`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1063.28 x 133.09 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | matter 64px/66.56px 600 |
| Letter spacing | -1.6px |
| Colour | #121212 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `page-title-default.png`.

#### page-cta

Product page CTA.

Page: ai-storyboard. Selector: `main CTA`. States: .

Not found on the page at capture time.

### Sign-in and demo forms

#### signup-form

Signup form. The public signup card; fields focused/filled only, never submitted.

Page: signup. Selector: `form`. States: .

Not found on the page at capture time.

#### signup-field

Signup field.

Page: signup. Selector: `form input`. States: .

Not found on the page at capture time.

#### signup-submit

Signup submit. The form submit; measured at rest, never pressed.

Page: signup. Selector: `form submit`. States: .

Not found on the page at capture time.

#### login-form

Login form. The login card; never used.

Page: login. Selector: `form`. States: .

Not found on the page at capture time.

#### login-field

Login field.

Page: login. Selector: `form input on /login`. States: .

Not found on the page at capture time.

### Footer

#### footer

Footer. The footer: link columns, social, legal.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1416 x 492 |
| Padding | 0px 80px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | matter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.block.whitespace-nowrap: matter 14.4px/21.6px 400, #ffffff |
| Transition | none |
| Icon | 14.41 x 14.41, colour #f4bd64 |
| Painted layers | span.flex.rounded-full 152.0x50.1 bg #ffffff @ 0.1 r 9999px; div.w-full.justify-between 1400.0x52.0 bg #ffffff @ 0.06 r 24px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 152 x 50.09 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | matter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.text-xxs.mt-0.5: matter 10.4px/17.68px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14.41 x 14.41, colour #f4bd64 | = | = | = |
| Painted layers | span.flex.rounded-full 152.0x50.1 bg #ffffff @ 0.1 r 9999px | span.flex.rounded-full 152.0x50.1 bg #ffffff @ 0.15 r 9999px | a 152.0x50.1 outline 1px auto #005fcc offset 1px; span.flex.rounded-full 152.0x50.1 bg #ffffff @ 0.1 r 9999px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-icon

Social icon.

Page: home. Selector: `footer social link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 20 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | matter 14.4px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Opacity | 0.3 | 0.6 | = | 0.6 |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.opacity-30.hover:opacity-60 20.0x20.0 outline 1px auto #005fcc offset 1px | = |

Crops: `social-icon-default.png`, `social-icon-hover.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 366 x 56 |
| Padding | 0px 8px 0px 20px |
| Border | none |
| Radius | 9999px |
| Background | transparent |
| Box shadow | #ffffff 0px 0px 0px 0px, #121212 @ 0.04 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | matter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | box-shadow 0.3s cubic-bezier(0, 0, 0.2, 1) |
| Icon | 0 x 0, colour #121212 @ 0.6 |
| Painted layers | header.pointer-events-auto.relative 366.0x56.0 r 9999px shadow #ffffff 0px 0px 0px 0px, #121212 @ 0.04 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; span.pointer-events-none.absolute 366.0x56.0 bg #ffffff r 9999px; a.relative.z-40 125.0x30.0 bg #121212 r 9999px; a.px-5.text-center 0.0x0.0 bg #121212 border T:2px solid #121212 / R:2px solid #121212 / B:2px solid #121212 / L:2px solid #121212 r 9999px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button.

Page: mobile. Selector: `button[aria-label="Open menu"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #121212 @ 0.05 | = | #121212 @ 0.05 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = |
| Font | matter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 3 up header.pointer-events-auto.relative shadow #ffffff 0px 0px 0px 0px, #121212 @ 0.04 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.flex.h-10 40.0x40.0 bg #121212 @ 0.05 r 9999px | button.flex.h-10 40.0x40.0 r 9999px outline 1px auto #e59700 offset 0px | button.flex.h-10 40.0x40.0 bg #121212 @ 0.05 r 9999px |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The button after its own toggle; the opened menu shows in the crop.

Page: mobile. Selector: `button[aria-label="Open menu"]`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 40 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 9999px |
| Background | transparent |
| Box shadow | none |
| Outline | 1px auto #e59700 offset 0px |
| Font | matter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | button.flex.h-10 40.0x40.0 r 9999px outline 1px auto #e59700 offset 0px |
| Ancestor paint | 3 up header.pointer-events-auto.relative shadow #ffffff 0px 0px 0px 0px, #121212 @ 0.04 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| How | own toggle |

Crops: `m-menu-open-opened.png`.

#### m-nav-item

Mobile nav item. A link inside the opened menu overlay.

Page: mobile. Selector: `menu overlay a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 334 x 40 | = | = | 317.3 x 38 |
| Padding | 6px 20px | = | = | = |
| Border | 2px solid #ffffff | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | matter 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #121212 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.px-5.text-center 334.0x40.0 bg #ffffff border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 9999px | = | a.px-5.text-center 334.0x40.0 bg #ffffff border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 9999px outline 2px solid #000000 @ 0 offset 2px | a.px-5.text-center 317.3x38.0 bg #ffffff border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.95, 0, 0, 0.95, 0, 0) |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 334 x 149.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | matter 36.0013px/37.4414px 600 |
| Letter spacing | -0.900033px |
| Colour | #121212 |
| Text node | span.whitespace-nowrap: matter 36.0013px/37.4414px 600, #121212, ls -0.900033px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page: inline styles and same-origin sheets, since a cross-origin sheet stays unreadable there. The per-state Transition rows in the tables above are computed values and cover every rule the page paints.

- home: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- pricing: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- script-timer: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`
