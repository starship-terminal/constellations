# Component measurements

Computed styles read from www.intercom.com on 2026-11-17 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### promo-banner

Promo banner. The announcement row at the very top of the shared header ("Introducing Fin 4 … Learn more"): real chrome, kept.

Page: home. Selector: `header banner row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 34 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | #e1e2e5 |
| Box shadow | none |
| Outline | none |
| Font | Saans 14px/20px 400 |
| Letter spacing | normal |
| Colour | #111111 |
| Text node | span.text-current.font-sans: Saans 14px/18.004px 400, #111111, ls 0.496px |
| Transition | none |
| Icon | 16 x 16, colour #111111 |
| Painted layers | div.top-banner.relative 1440.0x34.0 bg #e1e2e5; div.pointer-events-none.absolute 0.0x0.0 bg #d9d9d9; span.text-current.font-sans 0.0x0.0 image linear-gradient(to right in oklab, #111111 0%, #111111 100%); span.text-current.font-sans 76.0x18.0 image linear-gradient(to right in oklab, #111111 0%, #111111 100%) |
| Ancestor paint | 1 up header.shared-header.z-nav bg #ffffff |
| How | at rest |

Crops: `promo-banner-default.png`.

#### header

Nav bar. The shared site header (header.shared-header): Intercom logo, Product/Customers/Resources menu triggers, Pricing link, Log in, Contact sales, View demo and the black "Start free trial" button.

Page: home. Selector: `header.shared-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 108 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Saans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #111111 |
| Text node | span.text-current.font-sans: Saans 14px/18.004px 400, #111111, ls 0.496px |
| Transition | top 0.25s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 16 x 16, colour #111111 |
| Painted layers | header.shared-header.z-nav 1440.0x108.0 bg #ffffff; div.top-banner.relative 1440.0x34.0 bg #e1e2e5; div.pointer-events-none.absolute 0.0x0.0 bg #d9d9d9; span.text-current.font-sans 0.0x0.0 image linear-gradient(to right in oklab, #111111 0%, #111111 100%); span.text-current.font-sans 76.0x18.0 image linear-gradient(to right in oklab, #111111 0%, #111111 100%); a.font-inherit.m-0 0.0x0.0 bg #111111 r 4px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Intercom wordmark home anchor in the nav.

Page: home. Selector: `header a[href="/"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 129.56 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| Cursor | pointer |
| Icon | 0 x 0, colour #000000 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-item

Nav menu trigger. A mega-menu trigger in the nav ("Product"): 40px, radius 6, opens the nav panel.

Page: home. Selector: `header button "Product"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85 x 40 | = | = | = |
| Padding | 0px 4px 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | #f1eee9 | = | #f1eee9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Saans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #111111 | = | = | = |
| Text node | span.font-sans.tracking-normal: Saans 14px/15.4px 400, #111111 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 18 x 18, colour #111111 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.flex.items-center 85.0x40.0 bg #f1eee9 r 6px | button.flex.items-center 85.0x40.0 r 6px outline 1px auto #101010 offset 0px | button.flex.items-center 85.0x40.0 bg #f1eee9 r 6px |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`.

#### nav-link

Nav link. A plain nav link ("Pricing"): 40px ghost row, radius 6.

Page: home. Selector: `header a "Pricing"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 68 x 40 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | #f1eee9 | = | #f1eee9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset 2px | = |
| Font | Saans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #111111 | = | = | = |
| Text node | span.font-sans.tracking-normal: Saans 14px/15.4px 400, #111111 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.flex.h-10 68.0x40.0 bg #f1eee9 r 6px | a.flex.h-10 68.0x40.0 r 6px outline 2px solid #101010 offset 2px | a.flex.h-10 68.0x40.0 bg #f1eee9 r 6px |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Nav log in. The "Log in" link to app.intercom.com; measured, never followed.

Page: home. Selector: `header a[href*=sign_in]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 61 x 40 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | #f1eee9 | = | #f1eee9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Saans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #111111 | = | = | = |
| Text node | span.font-sans.tracking-normal: Saans 14px/15.4px 400, #111111 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.flex.h-10 61.0x40.0 bg #f1eee9 r 6px | a.flex.h-10 61.0x40.0 r 6px outline 1px auto #101010 offset 1px | a.flex.h-10 61.0x40.0 bg #f1eee9 r 6px |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-cta

Nav CTA. The black "Start free trial" button in the nav (--button-primary-* tokens, --button-radius 4px, height --button-height 40px); links to /signup, never followed.

Page: home. Selector: `header a[href*=signup]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 109 x 40 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #111111 | #0007cb | = | #0007cb @ 0.85 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset 2px | = |
| Font | Saans 14px/15.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.font-inherit.m-0 109.0x40.0 bg #111111 r 4px | a.font-inherit.m-0 109.0x40.0 bg #0007cb r 4px | a.font-inherit.m-0 109.0x40.0 bg #111111 r 4px outline 2px solid #101010 offset 2px | a.font-inherit.m-0 109.0x40.0 bg #0007cb @ 0.85 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-menu

Nav mega-menu. The panel the Product/Customers/Resources triggers open (shared-header-switch-card): a white card with the nav-panel border and a drop shadow.

Page: home. Selector: `[class*=switch-card] / nav panel`. States: .

Not found on the page at capture time.

### Home

#### hero-title

Hero title. The home hero headline ("A complete system for AI and human customer service", text-heading-2: Saans, tight tracking).

Page: home. Selector: `first visible h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 585.63 x 192 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 64px/64px 400 |
| Letter spacing | -2.4px |
| Colour | #111111 |
| Text node | span: Saans 64px/64px 400, #111111 @ 0.4, ls -2.4px |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### eyebrow

Eyebrow label. A small label over a section (text-label-lg: SaansMono-family uppercase micro type).

Page: home. Selector: `span.text-label-lg`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1170.67 x 12 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SaansMono 12px/12px 400 |
| Letter spacing | 0.6px |
| Colour | #111111 |
| Transition | none |
| How | at rest |

Crops: `eyebrow-default.png`.

#### hero-cta

Hero CTA. The black "Start free trial" button under the hero copy (--button-primary-*, --button-radius); links to /signup, never followed.

Page: home. Selector: `main a[href*=signup]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 123 x 40 | = | = | = |
| Padding | 4px 14px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #111111 | #0007cb | = | #0007cb @ 0.85 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset 2px | = |
| Font | Saans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.font-inherit.m-0 123.0x40.0 bg #111111 r 4px | a.font-inherit.m-0 123.0x40.0 bg #0007cb r 4px | a.font-inherit.m-0 123.0x40.0 bg #111111 r 4px outline 2px solid #101010 offset 2px | a.font-inherit.m-0 123.0x40.0 bg #0007cb @ 0.85 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-secondary

Hero secondary link. The secondary action beside the hero CTA ("View demo" style link button).

Page: home. Selector: `main a "View demo/Learn more"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 110 x 40 | = | = | = |
| Padding | 4px 14px | = | = | = |
| Border | 1px solid #111111 | 1px solid #111111 @ 0.75 | = | 1px solid #111111 @ 0.75 |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | #111111 @ 0.02 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset 2px | = |
| Font | Saans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #111111 | #111111 @ 0.75 | = | #000000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.font-inherit.m-0 110.0x40.0 border T:1px solid #111111 / R:1px solid #111111 / B:1px solid #111111 / L:1px solid #111111 r 4px | a.font-inherit.m-0 110.0x40.0 border T:1px solid #111111 @ 0.75 / R:1px solid #111111 @ 0.75 / B:1px solid #111111 @ 0.75 / L:1px solid #111111 @ 0.75 r 4px | a.font-inherit.m-0 110.0x40.0 border T:1px solid #111111 / R:1px solid #111111 / B:1px solid #111111 / L:1px solid #111111 r 4px outline 2px solid #101010 offset 2px | a.font-inherit.m-0 110.0x40.0 bg #111111 @ 0.02 border T:1px solid #111111 @ 0.75 / R:1px solid #111111 @ 0.75 / B:1px solid #111111 @ 0.75 / L:1px solid #111111 @ 0.75 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-secondary-default.png`, `hero-secondary-hover.png`, `hero-secondary-focus-visible.png`, `hero-secondary-pressed.png`.

#### section-title

Section title. A display section heading in page flow (text-heading-3: Saans).

Page: home. Selector: `h2.text-heading-3 first`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1164 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 24px/24px 400 |
| Letter spacing | -0.48px |
| Colour | #111111 |
| Text node | span: Saans 24px/24px 400, #111111 @ 0.4, ls -0.48px |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### feature-card

Feature card. A painted card on the home page (the first bordered/filled rounded container in main).

Page: home. Selector: `first painted card in main`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 728 x 686 | = |
| Padding | 0px | = |
| Border | 1px solid #000000 @ 0.06 | = |
| Radius | 14px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | system-ui 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #111111 | = |
| Text node | div.flex.h-12: system-ui 14px/21px 600, #111111 | = |
| Transition | none | = |
| Icon | 16 x 16, colour #111111 | = |
| Painted layers | div.flex.min-w-0 728.0x686.0 border T:1px solid #000000 @ 0.06 / R:1px solid #000000 @ 0.06 / B:1px solid #000000 @ 0.06 / L:1px solid #000000 @ 0.06 r 14px; div.flex.w-full 220.0x684.0 bg #fbfbf9 border R:1px solid #000000 @ 0.06; button.flex.w-full 203.0x53.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 1px 2px 0px; span.flex.size-5 20.0x20.0 bg #b9a6f5 r 3.35544e+07px; button.flex.w-full 203.0x53.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; span.flex.size-5 20.0x20.0 bg #b9a6f5 r 3.35544e+07px | = |
| Ancestor paint | 1 up div.flex.h-full bg #eff0eb shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.04 0px 1px 3px 0px, #000000 @ 0.06 0px 12px 32px 0px | = |
| How | at rest | mouse hover |

Crops: `feature-card-default.png`, `feature-card-hover.png`.

#### page-ground

Page ground. The body element: --body-bg = --color-cream under the current brand scope.

Page: home. Selector: `document.body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 9579.03 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.text-current.font-sans: Saans 14px/18.004px 400, #111111, ls 0.496px |
| Transition | none |
| Icon | 16 x 16, colour #111111 |
| Painted layers | header.shared-header.z-nav 1440.0x108.0 bg #ffffff; div.top-banner.relative 1440.0x34.0 bg #e1e2e5; div.pointer-events-none.absolute 0.0x0.0 bg #d9d9d9; span.text-current.font-sans 0.0x0.0 image linear-gradient(to right in oklab, #111111 0%, #111111 100%); span.text-current.font-sans 76.0x18.0 image linear-gradient(to right in oklab, #111111 0%, #111111 100%); a.font-inherit.m-0 0.0x0.0 bg #111111 r 4px |
| How | at rest |

Crops: none.

### Pricing

#### pricing-title

Pricing title. "Get Fin and Intercom for a single, fully integrated customer service stack" (text-heading-3).

Page: pricing. Selector: `first visible h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 896 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 48px/48px 400 |
| Letter spacing | -1.6px |
| Colour | #111111 |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### billing-toggle

Billing toggle (selected). The selected half of the annual/monthly billing segmented control ("Billed annually": canvas fill, radius none). Local UI state, switched and switched back.

Page: pricing. Selector: `button "Billed annually"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 104 x 27.59 | = | = | = |
| Padding | 4px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #e7e3db | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Saans 14px/19.6px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #111111 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | button.text-body.px-2 104.0x27.6 bg #e7e3db | = | button.text-body.px-2 104.0x27.6 bg #e7e3db outline 1px auto #101010 offset 0px | = |
| Ancestor paint | 1 up div.border-linen.inline-flex bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `billing-toggle-default.png`, `billing-toggle-hover.png`, `billing-toggle-focus-visible.png`, `billing-toggle-pressed.png`.

#### billing-toggle-off

Billing toggle (unselected). The unselected half ("Billed monthly": transparent).

Page: pricing. Selector: `button "Billed monthly"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 104 x 27.59 | = | = | = |
| Padding | 4px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #111111 | = | #111111 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Saans 14px/19.6px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #111111 | #ffffff | = | #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.border-linen.inline-flex bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.text-body.px-2 104.0x27.6 bg #111111 | button.text-body.px-2 104.0x27.6 outline 1px auto #101010 offset 0px | button.text-body.px-2 104.0x27.6 bg #111111 |

Crops: `billing-toggle-off-default.png`, `billing-toggle-off-hover.png`, `billing-toggle-off-focus-visible.png`, `billing-toggle-off-pressed.png`.

#### promo-badge

Promo badge button. The helpdesk-blue tinted badge button on pricing ("New customers save 35%", bg-helpdesk/15, 2px radius).

Page: pricing. Selector: `button "save 35%"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 157 x 20.8 | = | = | = |
| Padding | 2px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 2px | = | = | = |
| Background | #0007cb @ 0.15 | #0007cb @ 0.25 | #0007cb @ 0.25 | #0007cb @ 0.25 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Saans 12px/16.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0007cb | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | button.text-helpdesk.absolute 157.0x20.8 bg #0007cb @ 0.15 r 2px | button.text-helpdesk.absolute 157.0x20.8 bg #0007cb @ 0.25 r 2px | button.text-helpdesk.absolute 157.0x20.8 bg #0007cb @ 0.25 r 2px outline 1px auto #101010 offset 0px | button.text-helpdesk.absolute 157.0x20.8 bg #0007cb @ 0.25 r 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `promo-badge-default.png`, `promo-badge-hover.png`, `promo-badge-focus-visible.png`, `promo-badge-pressed.png`.

#### plan-card

Plan card. A pricing plan column (the Essential cell of the @container plan grid: unpainted itself, its plan name, "Includes Fin AI Agent" list and CTA inside).

Page: pricing. Selector: `Essential @container cell`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 286 x 607.56 |
| Padding | 24px |
| Gap | 40px normal |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #111111 |
| Text node | h2.text-heading-5: Saans 24px/24px 400, #111111, ls -0.48px |
| Transition | none |
| Icon | 12 x 12, colour #111111 @ 0.8 |
| Painted layers | del::after.relative.inline-flex 37.4375pxx1.1875px bg #111111 @ 0.5; button.text-helpdesk.absolute 157.0x20.8 bg #0007cb @ 0.15 r 2px; a.font-inherit.m-0 113.0x40.0 bg #111111 r 4px; span.size-1.flex-none 4.0x4.0 bg #111111 @ 0.3; span.size-1.flex-none 4.0x4.0 bg #111111 @ 0.3; span.size-1.flex-none 4.0x4.0 bg #111111 @ 0.3 |
| How | at rest |

Crops: `plan-card-default.png`.

#### faq-item

FAQ accordion item. A question row in the pricing FAQ accordion; opened by its own press.

Page: pricing. Selector: `last ? button`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 696.02 x 64 | = |
| Padding | 20px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Saans 20px/24px 400 | = |
| Letter spacing | -0.2px | = |
| Colour | #111111 | = |
| Text node | h3: Saans 20px/24px 400, #111111, ls -0.2px | = |
| Transition | opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 20 x 20, colour #111111 | = |
| How | at rest | own toggle |

Crops: `faq-item-default.png`, `faq-item-opened.png`.

### Contact sales form

#### form

Contact sales form. The first step of the contact-sales form (Business Email, company size select, opt-in checkbox, Next): measured at rest, never advanced or sent.

Page: contact-sales. Selector: `form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 448 x 372.19 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #111111 |
| Text node | label.label: Saans 14px/19.6px 400, #111111 |
| Transition | none |
| Icon | 8 x 5, colour #111111 @ 0.6 |
| Painted layers | input.input 448.0x40.0 bg #faf9f6 border T:1px solid #111111 @ 0.2 / R:1px solid #111111 @ 0.2 / B:1px solid #111111 @ 0.2 / L:1px solid #111111 @ 0.2 r 2px; button.select.flex 448.0x40.0 bg #faf9f6 border T:1px solid #111111 @ 0.2 / R:1px solid #111111 @ 0.2 / B:1px solid #111111 @ 0.2 / L:1px solid #111111 @ 0.2 r 2px; div.select-popup.overflow-y-auto 0.0x0.0 bg #faf9f6 border T:1px solid #111111 / R:1px solid #111111 / B:1px solid #111111 / L:1px solid #111111 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.checkbox 20.0x20.0 bg #faf9f6 border T:1px solid #111111 @ 0.2 / R:1px solid #111111 @ 0.2 / B:1px solid #111111 @ 0.2 / L:1px solid #111111 @ 0.2; button.font-inherit.m-0 448.0x40.0 bg #111111 r 4px; div.relative.h-px 448.0x1.0 bg #111111 @ 0.1 |
| How | at rest |

Crops: `form-default.png`.

#### form-title

Form page title. "Discover the perfect fit with Intercom".

Page: contact-sales. Selector: `first visible h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 512 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 40px/40px 400 |
| Letter spacing | -1.2px |
| Colour | #111111 |
| Transition | none |
| How | at rest |

Crops: `form-title-default.png`.

#### input-label

Field label. A field label (.label: "Business Email *").

Page: contact-sales. Selector: `label.label`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 448 x 25.59 |
| Padding | 0px 0px 6px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 14px/19.6px 400 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `input-label-default.png`.

#### input

Text field. The "Business email address" text input (.input: off-white fill, 2px radius, 40px). Sample text typed and deleted; nothing sent.

Page: contact-sales. Selector: `input.input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 448 x 40 | = | = |
| Padding | 0px 12px | = | = |
| Border | 1px solid #111111 @ 0.2 | 1px solid #111111 | 1px solid #111111 |
| Radius | 2px | = | = |
| Background | #faf9f6 | #f1eee9 | #f1eee9 |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Saans 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #111111 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #111111 @ 0.6, opacity 1 | = | = |
| Painted layers | input.input 448.0x40.0 bg #faf9f6 border T:1px solid #111111 @ 0.2 / R:1px solid #111111 @ 0.2 / B:1px solid #111111 @ 0.2 / L:1px solid #111111 @ 0.2 r 2px | input.input 448.0x40.0 bg #f1eee9 border T:1px solid #111111 / R:1px solid #111111 / B:1px solid #111111 / L:1px solid #111111 r 2px | input.input 448.0x40.0 bg #f1eee9 border T:1px solid #111111 / R:1px solid #111111 / B:1px solid #111111 / L:1px solid #111111 r 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `input-default.png`, `input-focused.png`, `input-filled.png`.

#### select

Select (combobox). The "Your company size" select (button.select, same field styling as .input): its own listbox opened, nothing chosen.

Page: contact-sales. Selector: `button.select`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 448 x 40 | = |
| Padding | 0px 12px | = |
| Border | 1px solid #111111 @ 0.2 | 1px solid #111111 |
| Radius | 2px | = |
| Background | #faf9f6 | #f1eee9 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Saans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #111111 @ 0.6 | = |
| Text node | span: Saans 16px/24px 400, #111111 @ 0.6 | = |
| Transition | none | = |
| Cursor | default | = |
| Icon | 8 x 5, colour #111111 @ 0.6 | = |
| Painted layers | button.select.flex 448.0x40.0 bg #faf9f6 border T:1px solid #111111 @ 0.2 / R:1px solid #111111 @ 0.2 / B:1px solid #111111 @ 0.2 / L:1px solid #111111 @ 0.2 r 2px | button.select.flex 448.0x40.0 bg #f1eee9 border T:1px solid #111111 / R:1px solid #111111 / B:1px solid #111111 / L:1px solid #111111 r 2px |
| How | at rest | own toggle |

Crops: `select-default.png`, `select-opened.png`.

#### select-popup

Select popup. The open listbox of the select (div.select-popup): options list, held open by the select entry.

Page: contact-sales. Selector: `[role=listbox]`. States: .

Not found on the page at capture time.

#### checkbox

Checkbox row. The opt-in checkbox row (label.checkbox-label: "Get updates about upcoming events…"). Never ticked.

Page: contact-sales. Selector: `label.checkbox-label`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 420 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 14px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `checkbox-default.png`.

#### next-button

Next button. The form's black "Next" submit control (--button-primary-*, --button-radius, --button-height): measured with CDP-forced pseudo states only — never pressed, so the form was never advanced.

Page: contact-sales. Selector: `button "Next"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 448 x 40 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #111111 | #0007cb | = | #0007cb @ 0.85 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset 2px | = |
| Font | Saans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.font-inherit.m-0 448.0x40.0 bg #111111 r 4px | button.font-inherit.m-0 448.0x40.0 bg #0007cb r 4px | button.font-inherit.m-0 448.0x40.0 bg #111111 r 4px outline 2px solid #101010 offset 2px | button.font-inherit.m-0 448.0x40.0 bg #0007cb @ 0.85 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `next-button-default.png`, `next-button-hover.png`, `next-button-focus-visible.png`, `next-button-pressed.png`.

### Help center

#### help-header

Help center header. The help center's own header bar (a different surface from the marketing shell: white, no theme-light class).

Page: help. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 60 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #111111 @ 0.12; L: none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | MediumLLWeb-Regular 15px/23.25px 400 |
| Letter spacing | normal |
| Colour | #111111 |
| Text node | a.DocsTopBar_tab__AXxRm: MediumLLWeb-Regular 14px/14px 400, #111111 @ 0.78 |
| Transition | none |
| Icon | 14 x 14, colour #111111 @ 0.78 |
| Painted layers | header.DocsTopBar_bar__i14eF 1440.0x60.0 bg #ffffff border B:1px solid #111111 @ 0.12; select.peer.absolute 105.0x30.0 bg #efefef; button.DocsTopBar_search__tI7kY 140.0x30.0 bg #111111 @ 0.05 border T:1px solid #111111 @ 0.5 / R:1px solid #111111 @ 0.5 / B:1px solid #111111 @ 0.5 / L:1px solid #111111 @ 0.5 r 8px |
| Ancestor paint | 1 up div.tokens_docsRoot__1XQPC bg #ffffff |
| How | at rest |

Crops: none.

#### help-search

Help search field. The help center search ("Search for articles… ⌘K"): focused once, nothing typed.

Page: help. Selector: `search input/button`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 140 x 30 | = |
| Padding | 0px 16px | = |
| Gap | 12px | = |
| Border | 1px solid #111111 @ 0.5 | = |
| Radius | 8px | = |
| Background | #111111 @ 0.05 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | MediumLLWeb-Regular 14px/21.7px 400 | = |
| Letter spacing | normal | = |
| Colour | #111111 @ 0.78 | = |
| Text node | span: MediumLLWeb-Regular 14px/21.7px 400, #111111 @ 0.78 | = |
| Transition | background, border-color 0.15s, 0.15s ease, ease delay 0s, 0s | = |
| Cursor | pointer | = |
| Painted layers | button.DocsTopBar_search__tI7kY 140.0x30.0 bg #111111 @ 0.05 border T:1px solid #111111 @ 0.5 / R:1px solid #111111 @ 0.5 / B:1px solid #111111 @ 0.5 / L:1px solid #111111 @ 0.5 r 8px | = |
| How | at rest | clicked into the field |

Crops: `help-search-default.png`, `help-search-focused.png`.

#### help-hero

Help center title. "Great service changes everything."

Page: help. Selector: `first visible h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 700 x 134.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | IvoryLLSub-Light 60px/67.2px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `help-hero-default.png`.

#### help-card

Help article card. A category/article card on the help center home (first painted rounded container in main).

Page: help. Selector: `marked card in main`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 260.66 x 252 | = |
| Padding | 0px | = |
| Border | 1px solid #1a1a1a @ 0.15 | = |
| Radius | 8px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | MediumLLWeb-Regular 15px/23.25px 400 | = |
| Letter spacing | normal | = |
| Colour | #1a1a1a | = |
| Text node | a.DocsHome_cardTitle__zVFWo: IvoryLLSub-Light 15px/19.5px 600, #1a1a1a | = |
| Transition | background-color 0.15s ease | = |
| Painted layers | div.DocsHome_card__WgIjM 260.7x252.0 bg #ffffff border T:1px solid #1a1a1a @ 0.15 / R:1px solid #1a1a1a @ 0.15 / B:1px solid #1a1a1a @ 0.15 / L:1px solid #1a1a1a @ 0.15 r 8px; span.DocsHome_cardIcon___3jlp 40.0x40.0 bg #faf9f6 r 8px; div.DocsHome_cardBody__oaxTm 258.7x123.0 border T:1px solid #1a1a1a @ 0.1 | = |
| How | at rest | mouse hover |

Crops: `help-card-default.png`, `help-card-hover.png`.

#### help-nav

Docs nav. The help center's expandable docs navigation tree (Overview, Getting Started, Operator, Fin AI Agent …).

Page: help. Selector: `nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 287 x 14 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | MediumLLWeb-Regular 15px/23.25px 400 |
| Letter spacing | normal |
| Colour | #111111 |
| Text node | a.DocsTopBar_tab__AXxRm: MediumLLWeb-Regular 14px/14px 400, #111111 @ 0.78 |
| Transition | none |
| How | at rest |

Crops: `help-nav-default.png`.

### Changelog

#### changes-title

Changelog title. The changelog header (the older "header__lite" surface: #f3f5f7 ground, MediumLL-era type).

Page: changes. Selector: `first visible h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 900 x 40.91 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 33px/40.92px 400 |
| Letter spacing | normal |
| Colour | #3a3c4c |
| Transition | none |
| How | at rest |

Crops: none.

#### changes-entry

Changelog entry. A release-note entry on /changes/en (div.paper.newsfeed__newsitem: white card, 4px radius on the #f3f5f7 header__lite ground).

Page: changes. Selector: `.newsfeed__newsitem`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 900 x 967.39 |
| Padding | 0px |
| Border | none |
| Radius | 4px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.03 0px 3px 8px 0px |
| Outline | none |
| Font | system-ui 16px/25.6px 400 |
| Letter spacing | normal |
| Colour | #565867 |
| Text node | div.newsitem_label: system-ui 14px/22px 600, #ffffff |
| Transition | border, transform, background-color, box-shadow, opacity 0.15s, 0.15s, 0.15s, 0.15s, 0.15s linear, linear, linear, linear, linear delay 0s, 0s, 0s, 0s, 0s |
| Painted layers | div.paper.newsfeed__newsitem 900.0x967.4 bg #ffffff r 4px shadow #000000 @ 0.03 0px 3px 8px 0px; div.newsitem_label 59.4x26.0 bg #000000 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px; div.newsitem_label 68.0x26.0 bg #000000 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px; div.newsitem_label 49.2x26.0 bg #000000 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px; img.avatar__image 32.0x32.0 r 50% shadow #ffffff 0px 0px 0px 2px; a.intercom-h2b-button 177.9x39.8 bg #000000 r 4px |
| How | at rest |

Crops: none.

### Blog

#### blog-title

Blog title. "Blog" (text-heading-*: Saans).

Page: blog. Selector: `first visible h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 814.66 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 48px/48px 400 |
| Letter spacing | -1.6px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `blog-title-default.png`.

#### blog-card

Blog article card. An article row in the /blog index list (li.border-t over the white section).

Page: blog. Selector: `first article li in main`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 696.5 x 274 | = |
| Padding | 32px 32px 32px 0px | = |
| Border | T: 1px solid #000000 @ 0.1; R: none; B: none; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Saans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.inline-flex.items-center: Saans 14px/14px 400, #000000 | = |
| Transition | none | = |
| Painted layers | li.border-t.py-4 696.5x274.0 border T:1px solid #000000 @ 0.1; span.inline-flex.items-center 127.0x24.0 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 3.35544e+07px | = |
| How | at rest | mouse hover |

Crops: `blog-card-default.png`, `blog-card-hover.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The header at 390: logo + the menu button (the desktop nav unmounts).

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 108 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Saans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #111111 |
| Text node | span.text-current.font-sans: Saans 14px/18.004px 400, #111111, ls 0.496px |
| Transition | top 0.25s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 16 x 16, colour #111111 |
| Painted layers | header.shared-header.z-nav 390.0x108.0 bg #ffffff; div.top-banner.relative 390.0x34.0 bg #e1e2e5; div.pointer-events-none.absolute 390.0x34.0 bg #d9d9d9; span.text-current.font-sans 76.0x18.0 image linear-gradient(to right in oklab, #111111 0%, #111111 100%); span.text-current.font-sans 0.0x0.0 image linear-gradient(to right in oklab, #111111 0%, #111111 100%); a.font-inherit.m-0 109.0x40.0 bg #111111 r 4px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button. The hamburger toggle in the mobile header (aria-label "Open navigation menu"); opens the menu overlay.

Page: home. Selector: `header menu button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = |
| Font | Saans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #111111 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 24 x 24, colour #111111 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.rounded-md.p-2 40.0x40.0 r 6px outline 1px auto #e59700 offset 0px | = |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-hero

Mobile hero. The hero title at 390 (the responsive text-heading-*-mobile size).

Page: home. Selector: `first visible h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 152 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 40px/38px 400 |
| Letter spacing | -1.2px |
| Colour | #111111 |
| Text node | span: Saans 40px/38px 400, #111111 @ 0.4, ls -1.2px |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

#### m-menu-overlay

Mobile menu overlay. The full-height navigation sheet the mobile menu button opens (div[role=dialog].shared-header-portal, off-white ground).

Page: home. Selector: `[role=dialog].shared-header-portal`. States: .

Not found on the page at capture time.

### Footer

#### footer

Footer. The site footer: link columns, social icons, the locale selector and legal row on the page ground.

Page: blog. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 577.69 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.text-xs.font-medium: SaansMono 12px/15.6px 500, #000000 @ 0.6, ls 1.2px |
| Transition | none |
| Icon | 26 x 12, colour #000000 |
| Painted layers | a.font-sans.font-normal 33.0x17.0 image linear-gradient(to right in oklab, #000000 0%, #000000 100%); a.font-sans.font-normal 58.0x17.0 image linear-gradient(to right in oklab, #000000 0%, #000000 100%); a.font-sans.font-normal 45.0x17.0 image linear-gradient(to right in oklab, #000000 0%, #000000 100%); a.font-sans.font-normal 45.0x17.0 image linear-gradient(to right in oklab, #000000 0%, #000000 100%); a.font-sans.font-normal 84.0x17.0 image linear-gradient(to right in oklab, #000000 0%, #000000 100%); a.font-sans.font-normal 76.0x17.0 image linear-gradient(to right in oklab, #000000 0%, #000000 100%) |
| Ancestor paint | 1 up div.relative.isolate bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer link (Saans, muted); focus-visible carries the site outline.

Page: blog. Selector: `footer a first`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 33 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(to right in oklab, #000000 0%, #000000 100%) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Saans 14px/17.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | background-size 0.2s ease-out | = | = | = |
| Opacity | 0.9 | - | - | - |
| Cursor | pointer | = | = | = |
| Painted layers | a.font-sans.font-normal 33.0x17.0 image linear-gradient(to right in oklab, #000000 0%, #000000 100%) | = | a.font-sans.font-normal 33.0x17.0 image linear-gradient(to right in oklab, #000000 0%, #000000 100%) outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### locale-select

Locale selector. The footer language selector ("English").

Page: blog. Selector: `footer language control`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Saans 14px/17.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Opacity | 0.9 | - | - | - |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.text-base.opacity-90 44.0x17.0 outline 1px auto #101010 offset 1px | = |

Crops: `locale-select-default.png`, `locale-select-hover.png`, `locale-select-focus-visible.png`, `locale-select-pressed.png`.

## Transitions declared in the readable stylesheets

intercom.com ships its CSS as same-origin inline <style> blocks (a Tailwind v4 build), so this list holds the transition and animation declarations the CSSOM could read on each page; the per-state Transition rows above are computed values of the same rules.

- home: `background-size 0.2s ease-out`, `opacity .6s var(--ease-out-quart)`, `color 0.3s`, `translate .7s var(--ease-out-quart), color .3s`, `translate .7s var(--ease-out-quart), opacity .3s`, `color 0.2s`, `border-color 0.2s`, `translate .7s var(--ease-out-quart)`, `0.1s`, `300ms ease-in`, `width 200ms, height 200ms, max-height 200ms, transform 300ms cubic-bezier(0, 1.2, 1, 1), opacity 83ms ease-out`, `transform 167ms cubic-bezier(0.33, 0, 0, 1)`
