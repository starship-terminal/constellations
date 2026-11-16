# Component measurements

Computed styles read from front.com, app.frontapp.com, help.front.com and dev.frontapp.com on 2026-11-16 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844; the appd-* components under app.frontapp.com's own [data-theme="dark"]), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Site chrome

#### mkt-header

Site header. The top bar on every marketing page: the Front wordmark, Product/Solutions/Resources mega-menu triggers, AI, Customers, Pricing, Sign in, Request a demo and Try for free.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 14px/20px 400 |
| Letter spacing | normal |
| Colour | #1c1e20 |
| Text node | button.block.button: Suisse Intl 16px/40px 500, #ffffff |
| Transition | all 0.6s cubic-bezier(0.16, 1, 0.3, 1) |
| Icon | 112 x 26, colour #ffffff, fill #000000 |
| Painted layers | button.block.button 153.0x40.0 bg #ffffff r 40px; button.block.button 111.0x40.0 r 40px shadow #d0c6f0 0px 0px 0px 1px inset; button.button.button-size-circle-medium 0.0x0.0 bg #f3f3f4 r 44px; div.rounded-20.bg-white 26.0x74.0 bg #ffffff border T:5px #e2dcf6 / R:5px #e2dcf6 / B:5px #e2dcf6 / L:5px #e2dcf6 r 20px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.04 0px 60px 60px 0px, #000000 @ 0.03 0px 30.375px 26.156px 0px, #000000 @ 0.02 0px 12px 9.75px 0px, #000000 @ 0.01 0px 2.625px 3.469px 0px; div.table-cell.align-top 378.5x345.0 border R:1px #dedfe2; div.table-cell.align-top 289.0x345.0 border R:1px #dedfe2 / L:1px #dedfe2 |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The Front wordmark in the header, linking home.

Page: home. Selector: `header a[href=/]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 112 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 14px/20px 400 |
| Letter spacing | normal |
| Colour | #1c1e20 |
| Transition | none |
| Cursor | pointer |
| Icon | 112 x 26, colour #ffffff, fill #000000 |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-menu-btn

Mega-menu trigger. The "Product" header button — a local UI toggle whose mega menu mounts under the header; the opened state was measured after its own click (aria-expanded had to stay true).

Page: home. Selector: `header button Product`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 90 x 40 | = | = | = | = |
| Padding | 0px 16px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 40px | = | = | = | = |
| Background | transparent | #5b1f76 | = | #8034bf | #5b1f76 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px solid #8034bf offset 2px | = | = |
| Font | Suisse Intl 16px/40px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | = | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | button.block.button 90.0x40.0 bg #5b1f76 r 40px | button.block.button 90.0x40.0 r 40px outline 1px solid #8034bf offset 2px | button.block.button 90.0x40.0 bg #8034bf r 40px | button.block.button 90.0x40.0 bg #5b1f76 r 40px |

Crops: `nav-menu-btn-default.png`, `nav-menu-btn-hover.png`, `nav-menu-btn-focus-visible.png`, `nav-menu-btn-pressed.png`, `nav-menu-btn-opened.png`.

#### nav-panel

Mega-menu panel. The panel opened by the "Product" trigger (product entries with icons and descriptions); its links were never followed.

Page: home. Selector: `product mega-menu panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1271 x 419 |
| Padding | 32px 8px |
| Border | 5px solid #e2dcf6 |
| Radius | 20px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.04 0px 60px 60px 0px, #000000 @ 0.03 0px 30.375px 26.156px 0px, #000000 @ 0.02 0px 12px 9.75px 0px, #000000 @ 0.01 0px 2.625px 3.469px 0px |
| Outline | none |
| Font | Suisse Intl 14px/20px 400 |
| Letter spacing | normal |
| Colour | #1c1e20 |
| Text node | span.text-16/20.font-500: Suisse Intl 16px/20px 500, #1c1e20 |
| Transition | none |
| Icon | 18 x 18, colour #1c1e20 |
| Painted layers | div.rounded-20.bg-white 1271.0x419.0 bg #ffffff border T:5px #e2dcf6 / R:5px #e2dcf6 / B:5px #e2dcf6 / L:5px #e2dcf6 r 20px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.04 0px 60px 60px 0px, #000000 @ 0.03 0px 30.375px 26.156px 0px, #000000 @ 0.02 0px 12px 9.75px 0px, #000000 @ 0.01 0px 2.625px 3.469px 0px; div.table-cell.align-top 378.5x345.0 border R:1px #dedfe2; div.table-cell.align-top 289.0x345.0 border R:1px #dedfe2 / L:1px #dedfe2; div.table-cell.align-top 289.0x345.0 border R:1px #dedfe2 / L:1px #dedfe2; div.table-cell.align-top 288.5x345.0 border L:1px #dedfe2; div.table-cell.align-top 488.5x149.0 border R:1px #dedfe2 |
| How | at rest |

Crops: `nav-panel-default.png`.

#### nav-menu-item

Mega-menu item. A product entry inside the opened mega menu; measured, never followed.

Page: home. Selector: `mega menu item`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 64 x 19 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 15px/19px 400 | = |
| Letter spacing | normal | = |
| Colour | #1c1e20 | = |
| Transition | none | = |
| Cursor | pointer | = |
| ::before | 240px x 41px, absolute, bg #000000 @ 0, radius 0px | = |
| How | at rest | mouse hover |

Crops: `nav-menu-item-default.png`, `nav-menu-item-hover.png`.

#### nav-pricing

Nav link. The "Pricing" header link; measured, never followed.

Page: home. Selector: `header a Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 84 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | transparent | #5b1f76 | = | #8034bf |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #8034bf offset 2px | = |
| Font | Suisse Intl 16px/40px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.block.button 84.0x40.0 bg #5b1f76 r 40px | a.block.button 84.0x40.0 r 40px outline 1px solid #8034bf offset 2px | a.block.button 84.0x40.0 bg #8034bf r 40px |

Crops: `nav-pricing-default.png`, `nav-pricing-hover.png`, `nav-pricing-focus-visible.png`, `nav-pricing-pressed.png`.

#### nav-signin

Sign-in link. The "Sign in" header link to app.frontapp.com/signin; measured, never followed.

Page: home. Selector: `header a Sign in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 82 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | transparent | #5b1f76 | = | #8034bf |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #8034bf offset 2px | = |
| Font | Suisse Intl 16px/40px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.block.button 82.0x40.0 bg #5b1f76 r 40px | a.block.button 82.0x40.0 r 40px outline 1px solid #8034bf offset 2px | a.block.button 82.0x40.0 bg #8034bf r 40px |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-demo

Request-demo button. The "Request a demo" header action (a bordered secondary button); links to /request-demo, measured never followed.

Page: home. Selector: `header Request a demo`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 153 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | #ffffff | #e2dcf6 | = | #e2dcf6 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Suisse Intl 16px/40px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #300c41 | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.block.button 153.0x40.0 bg #ffffff r 40px | button.block.button 153.0x40.0 bg #e2dcf6 r 40px | button.block.button 153.0x40.0 bg #ffffff r 40px outline 1px solid #ffffff offset 2px | button.block.button 153.0x40.0 bg #e2dcf6 r 40px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-demo-default.png`, `nav-demo-hover.png`, `nav-demo-focus-visible.png`, `nav-demo-pressed.png`.

#### nav-try

Try-free button. The "Try for free" header action; links to /signup, measured never followed.

Page: home. Selector: `header Try for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 111 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | transparent | #f8f1fe @ 0.2 | = | #f8f1fe |
| Box shadow | #d0c6f0 0px 0px 0px 1px inset | #f8f1fe 0px 0px 0px 1px inset | = | #f8f1fe 0px 0px 0px 1px inset |
| Outline | none | = | 1px solid #f8f1fe offset 2px | = |
| Font | Suisse Intl 16px/40px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #d0c6f0 | = | = | #300c41 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.block.button 111.0x40.0 r 40px shadow #d0c6f0 0px 0px 0px 1px inset | button.block.button 111.0x40.0 bg #f8f1fe @ 0.2 r 40px shadow #f8f1fe 0px 0px 0px 1px inset | button.block.button 111.0x40.0 r 40px shadow #d0c6f0 0px 0px 0px 1px inset outline 1px solid #f8f1fe offset 2px | button.block.button 111.0x40.0 bg #f8f1fe r 40px shadow #f8f1fe 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-try-default.png`, `nav-try-hover.png`, `nav-try-focus-visible.png`, `nav-try-pressed.png`.

#### quinn-launcher

Quinn widget (vendor). The Qualified "Quinn" chat widget host pinned bottom-right — a vendor surface, measured at rest and never opened or typed into.

Page: home. Selector: `#qualified-multimodal-host`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 14px/20px 400 |
| Letter spacing | normal |
| Colour | #1c1e20 |
| Transition | none |
| How | at rest |

Crops: none.

### Home

#### hero-h1

Hero headline. "All your teams. All your AI agents. One place to …" — the display1 masthead.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 840 x 104 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 43px/52px 500 |
| Letter spacing | -0.75px |
| Colour | #f8f1fe |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-sub

Hero subcopy. The paragraph under the hero headline (text-p1).

Page: home. Selector: `hero p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 840 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 20px/28px 400 |
| Letter spacing | normal |
| Colour | #e2dcf6 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### section-heading

Section heading. The first h2 section heading below the hero.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 840 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 30px/36px 500 |
| Letter spacing | -0.45px |
| Colour | #0d1d39 |
| Transition | none |
| How | at rest |

Crops: `section-heading-default.png`.

#### dark-violet-section

Plum section. A section themed [data-theme=theme-dark-violet] — the marketing site's signature dark-plum surface (surface-l0 #300c41, text-primary #f8f1fe).

Page: home. Selector: `[data-theme=theme-dark-violet]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 952 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 14px/20px 400 |
| Letter spacing | normal |
| Colour | #1c1e20 |
| Text node | h1.font-sans.antialiased: Suisse Intl 43px/52px 500, #f8f1fe, ls -0.75px |
| Transition | none |
| Icon | 1056 x 428, colour #1c1e20, fill #000000 |
| Painted layers | div.surface-l0.-mt-header-height-mobile 1440.0x952.0 bg #300c41; button.transition-colors.duration-400 140.0x48.0 bg #dee948 r 64px |
| How | at rest |

Crops: none.

#### gray-section

Gray section. A section themed [data-theme=theme-gray].

Page: home. Selector: `[data-theme=theme-gray]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 404 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 14px/20px 400 |
| Letter spacing | normal |
| Colour | #1c1e20 |
| Text node | h3.font-sans.antialiased: Suisse Intl 25px/30px 500, #0d1d39, ls -0.25px |
| Transition | none |
| Icon | 90 x 23, colour #1c1e20 |
| Painted layers | div.surface-l0.flex 1440.0x404.0 bg #f3f3f4; div.surface-l1.relative 160.0x94.0 bg #ffffff r 8px; div.surface-l1.relative 160.0x94.0 bg #ffffff r 8px; div.surface-l1.relative 215.0x200.0 bg #ffffff r 8px; span.surface-l2.rounded-full 24.0x24.0 bg #f3f3f4 r 100%; div.surface-l1.relative 160.0x94.0 bg #ffffff r 8px |
| How | at rest |

Crops: none.

#### product-h1

Product headline. The /product masthead.

Page: product. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1272 x 136 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 62px/68px 500 |
| Letter spacing | -1.25px |
| Colour | #f8f1fe |
| Transition | none |
| How | at rest |

Crops: `product-h1-default.png`.

#### product-cta

Product CTA. The primary action on the product page; measured never followed.

Page: product. Selector: `product CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 111 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | transparent | #f8f1fe @ 0.2 | = | #f8f1fe |
| Box shadow | #d0c6f0 0px 0px 0px 1px inset | #f8f1fe 0px 0px 0px 1px inset | = | #f8f1fe 0px 0px 0px 1px inset |
| Outline | none | = | 1px solid #f8f1fe offset 2px | = |
| Font | Suisse Intl 16px/40px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #d0c6f0 | = | = | #300c41 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.block.button 111.0x40.0 r 40px shadow #d0c6f0 0px 0px 0px 1px inset | button.block.button 111.0x40.0 bg #f8f1fe @ 0.2 r 40px shadow #f8f1fe 0px 0px 0px 1px inset | button.block.button 111.0x40.0 r 40px shadow #d0c6f0 0px 0px 0px 1px inset outline 1px solid #f8f1fe offset 2px | button.block.button 111.0x40.0 bg #f8f1fe r 40px shadow #f8f1fe 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `product-cta-default.png`, `product-cta-hover.png`, `product-cta-focus-visible.png`, `product-cta-pressed.png`.

#### hero-cta

Hero CTA. The "Request demo" button under the hero copy — the hero's single CTA; links to /request-demo, measured never followed.

Page: home. Selector: `hero Request demo`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140 x 48 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 64px | = | = | = |
| Background | #dee948 | #d6d943 | = | #d3d140 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Suisse Intl 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d1d39 | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.transition-colors.duration-400 140.0x48.0 bg #dee948 r 64px | button.transition-colors.duration-400 140.0x48.0 bg #d6d943 r 64px | button.transition-colors.duration-400 140.0x48.0 bg #dee948 r 64px outline 1px solid #ffffff offset 2px | button.transition-colors.duration-400 140.0x48.0 bg #d3d140 r 64px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### feature-card

Customer-story card. A customer-outcome stat card on the product page (rounded-20, the grid cells that link into customer stories); measured, never followed.

Page: product. Selector: `product stat card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 312 x 358 | = |
| Padding | 8px | = |
| Border | none | = |
| Radius | 20px | = |
| Background | #ffffff @ 0 | #d4b5f4 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #1c1e20 | = |
| Text node | h3.text-display1.font-500: Suisse Intl 62px/68px 500, #001b38, ls -1.24px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 14 x 14, colour #001b38 | = |
| Painted layers | a.p-1.col-span-1 312.0x358.0 bg #ffffff @ 0 r 20px; div.w-37.sm:min-w-38 296.0x342.0 bg #dee948 r 12px; button.block.button 190.0x40.0 bg #ffffff r 40px; div.flex.bg-current 26.0x26.0 bg #001b38 r 100% | a.p-1.col-span-1 312.0x358.0 bg #d4b5f4 r 20px; div.w-37.sm:min-w-38 296.0x342.0 bg #dee948 r 12px; button.block.button 190.0x40.0 bg #ffffff r 40px; div.flex.bg-current 26.0x26.0 bg #001b38 r 100% |
| How | at rest | mouse hover |

Crops: `feature-card-default.png`, `feature-card-hover.png`.

### Footer

#### footer

Site footer. The footer on every marketing page — "The AI customer operations platform.", the link columns, certifications and legal row.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1481.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 14px/20px 400 |
| Letter spacing | normal |
| Colour | #1c1e20 |
| Text node | p.text-30/36.max-w-44: Suisse Intl 30px/36px 400, #e2dcf6 |
| Transition | none |
| Icon | 1440 x 292.56, colour #5b1f76, fill #000000 |
| Painted layers | div.px-container-mobile.md:px-container-desktop 1440.0x820.0 bg #5b1f76; a.flex.flex-col 48.0x48.0 bg #8034bf r 100%; a.flex.flex-col 48.0x48.0 bg #8034bf r 100%; a.flex.flex-col 48.0x48.0 bg #8034bf r 100%; div.px-container-mobile.md:px-container-desktop 1440.0x359.0 bg #300c41; div.border-t.border-solid 1248.0x49.0 border T:1px #b375f4 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A link in the footer columns; measured, never followed.

Page: home. Selector: `footer a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 48 x 48 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 100% | = |
| Background | #8034bf | #8034bf @ 0.5 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #e2dcf6 | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0.55, 0.085, 0.68, 0.53) | = |
| Cursor | pointer | = |
| Painted layers | a.flex.flex-col 48.0x48.0 bg #8034bf r 100% | a.flex.flex-col 48.0x48.0 bg #8034bf @ 0.5 r 100% |
| How | at rest | mouse hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`.

### Pricing

#### pricing-h1

Pricing heading. The first heading on /pricing (the page carries no h1; the first h2 is measured instead).

Page: pricing. Selector: `pricing h1/h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 496.89 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 42px/52px 500 |
| Letter spacing | -0.735px |
| Colour | #0d1d39 |
| Transition | none |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### billing-toggle

Billing switch. The "Billed Annually"/"SAVE 24%" switch — a local UI toggle that repaints the plan prices; the opened state is the monthly-billed side, toggled and restored.

Page: pricing. Selector: `pricing billing switch`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 66 x 36 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #1c1e20 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.h-3.rounded-[8px] 66.0x36.0 bg #8034bf r 8px; div.absolute.w-[24px] 24.0x24.0 bg #ffffff r 4px | div.h-3.rounded-[8px] 66.0x36.0 bg #d0c6f0 r 8px; div.absolute.w-[24px] 24.0x24.0 bg #ffffff r 4px |
| How | at rest | own toggle |

Crops: `billing-toggle-default.png`, `billing-toggle-opened.png`.

#### plan-card

Plan card. A pricing tier card (name, price per seat/month, feature list, CTA) — the Starter column of the plan grid.

Page: pricing. Selector: `plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 313 x 460 |
| Padding | 0px |
| Border | none |
| Radius | 24px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 14px/20px 400 |
| Letter spacing | normal |
| Colour | #1c1e20 |
| Text node | span.flex.mr-[8px]: Suisse Intl 20px/28px 500, #0d1d39, ls 0.05px |
| Transition | none |
| Icon | 12 x 12, colour #1c1e20 |
| Painted layers | div.flex.flex-col 313.0x460.0 bg #ffffff r 24px; div.flex.flex-col 313.0x358.0 border T:4px #f3f3f4; button.block.w-full 265.0x40.0 r 40px shadow #5b1f76 0px 0px 0px 1px inset |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-cta

Plan CTA. A plan card's "Try for Free" action (the first tier column's button); links to /signup, measured never followed.

Page: pricing. Selector: `plan card Try for Free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 265 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | transparent | #5b1f76 @ 0.1 | = | #5b1f76 |
| Box shadow | #5b1f76 0px 0px 0px 1px inset | = | = | = |
| Outline | none | = | 1px solid #5b1f76 offset 2px | = |
| Font | Suisse Intl 16px/40px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #5b1f76 | = | = | #f8f1fe |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.block.w-full 265.0x40.0 r 40px shadow #5b1f76 0px 0px 0px 1px inset | button.block.w-full 265.0x40.0 bg #5b1f76 @ 0.1 r 40px shadow #5b1f76 0px 0px 0px 1px inset | button.block.w-full 265.0x40.0 r 40px shadow #5b1f76 0px 0px 0px 1px inset outline 1px solid #5b1f76 offset 2px | button.block.w-full 265.0x40.0 bg #5b1f76 r 40px shadow #5b1f76 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### sales-link

Talk-to-sales link. The "Talk to sales" action in the pricing hero; links to /request-demo, measured never followed.

Page: pricing. Selector: `Talk to sales`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 121.56 x 26 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Suisse Intl 17px/26px 500 | = | = | = |
| Letter spacing | 0.0425px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Suisse Intl 17px/26px 500, #ffffff, ls 0.0425px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.flex.font-500 121.6x26.0 outline 1px solid #ffffff offset 2px | = |

Crops: `sales-link-default.png`, `sales-link-hover.png`, `sales-link-focus-visible.png`, `sales-link-pressed.png`.

#### faq-item

FAQ disclosure. A "Frequently asked questions" disclosure button ("What is a seat?") — a local UI toggle whose answer mounts below; opened by its own click, left open for the shot.

Page: pricing. Selector: `pricing FAQ disclosure`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 872 x 100 | = | = | = | = |
| Padding | 32px 24px | = | = | = | = |
| Gap | 16px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px solid #1c1e20 offset 2px | = | = |
| Font | Suisse Intl 14px/20px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #1c1e20 | = | = | = | = |
| Text node | div.text-p1.md:text-h2: Suisse Intl 30px/36px 500, #000000, ls -0.45px | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 32 x 32, colour #1c1e20, fill #000000 | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | button.w-full.flex 872.0x100.0 outline 1px solid #1c1e20 offset 2px | = | = |

Crops: `faq-item-default.png`, `faq-item-hover.png`, `faq-item-focus-visible.png`, `faq-item-pressed.png`, `faq-item-opened.png`.

#### faq-answer

FAQ answer. The answer text revealed by the FAQ disclosure.

Page: pricing. Selector: `FAQ answer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 824 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 20px/28px 400 |
| Letter spacing | normal |
| Colour | #7c8088 |
| Transition | none |
| How | at rest |

Crops: `faq-answer-default.png`.

### Demo and signup forms

#### demo-h1

Demo heading. The first heading on /request-demo (no h1 ships; the first h2 is measured).

Page: request-demo. Selector: `request-demo h1/h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 507.84 x 84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 36px/42px 500 |
| Letter spacing | -0.63px |
| Colour | #0d1d39 |
| Text node | span.font-serif: Suisse Works 36px/42px 500, #0d1d39, ls -0.63px |
| Transition | none |
| How | at rest |

Crops: `demo-h1-default.png`.

#### demo-email

Work email field. The work-email input on the demo form; focused and typed into then cleared — the form was never submitted.

Page: request-demo. Selector: `request-demo input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 576 x 48 | = | = |
| Padding | 12px 16px | = | = |
| Border | none | = | = |
| Radius | 6px | = | = |
| Background | #f3f3f4 | = | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #dee948 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | #ffffff 0px 0px 0px 0px, #dee948 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | 2px solid #000000 @ 0 offset 2px | none | none |
| Font | Suisse Intl 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0d1d39 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #8e929b, opacity 1 | = | = |
| Painted layers | input.w-full.surface-l1 576.0x48.0 bg #f3f3f4 r 6px outline 2px solid #000000 @ 0 offset 2px | input.w-full.surface-l1 576.0x48.0 bg #f3f3f4 r 6px shadow #ffffff 0px 0px 0px 0px, #dee948 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | input.w-full.surface-l1 576.0x48.0 bg #f3f3f4 r 6px shadow #ffffff 0px 0px 0px 0px, #dee948 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `demo-email-default.png`, `demo-email-focused.png`, `demo-email-filled.png`.

#### demo-submit

Demo submit. The demo form's submit button; its states were measured but the button was never clicked — the form was never sent.

Page: request-demo. Selector: `request-demo form submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 576 x 48 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 64px | = | = | = |
| Background | #f3f3f4 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #300c41 offset 2px | = |
| Font | Suisse Intl 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #caccd0 | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1) | = | = | = |
| Cursor | not-allowed | = | = | = |
| Painted layers | button.transition-colors.duration-400 576.0x48.0 bg #f3f3f4 r 64px | = | button.transition-colors.duration-400 576.0x48.0 bg #f3f3f4 r 64px outline 1px solid #300c41 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `demo-submit-default.png`, `demo-submit-hover.png`, `demo-submit-focus-visible.png`, `demo-submit-pressed.png`.

#### signup-h1

Signup headline. The marketing /signup masthead.

Page: signup. Selector: `signup h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 25px/30px 500 |
| Letter spacing | -0.25px |
| Colour | #0d1d39 |
| Transition | none |
| How | at rest |

Crops: `signup-h1-default.png`.

#### signup-field

Signup field. The first field on the marketing signup form; focused and typed into then cleared — the form was never submitted.

Page: signup. Selector: `signup input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 480 x 48 | = | = |
| Padding | 12px 16px | = | = |
| Border | none | = | = |
| Radius | 6px | = | = |
| Background | #f3f3f4 | = | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #dee948 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | #ffffff 0px 0px 0px 0px, #dee948 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | 2px solid #000000 @ 0 offset 2px | none | none |
| Font | Suisse Intl 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0d1d39 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #8e929b, opacity 1 | = | = |
| Painted layers | input.w-full.surface-l1 480.0x48.0 bg #f3f3f4 r 6px outline 2px solid #000000 @ 0 offset 2px | input.w-full.surface-l1 480.0x48.0 bg #f3f3f4 r 6px shadow #ffffff 0px 0px 0px 0px, #dee948 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | input.w-full.surface-l1 480.0x48.0 bg #f3f3f4 r 6px shadow #ffffff 0px 0px 0px 0px, #dee948 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `signup-field-default.png`, `signup-field-focused.png`, `signup-field-filled.png`.

#### signup-submit

Signup submit. The marketing signup form's submit button (the rounded-[64px] "Submit" under the e-mail field); measured, never pressed.

Page: signup. Selector: `signup submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 480 x 48 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 64px | = | = | = |
| Background | #f3f3f4 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #300c41 offset 2px | = |
| Font | Suisse Intl 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #caccd0 | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1) delay 0.1s | = | = | = |
| Cursor | not-allowed | = | = | = |
| Painted layers | button.transition-colors.duration-400 480.0x48.0 bg #f3f3f4 r 64px | = | button.transition-colors.duration-400 480.0x48.0 bg #f3f3f4 r 64px outline 1px solid #300c41 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-submit-default.png`, `signup-submit-hover.png`, `signup-submit-focus-visible.png`, `signup-submit-pressed.png`.

#### demo-field

Company-size select. The company-size select on the demo form; focused, never changed or submitted.

Page: request-demo. Selector: `request-demo select`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 576 x 48 | = |
| Padding | 12px 48px 12px 16px | = |
| Border | none | = |
| Radius | 6px | = |
| Background | #f3f3f4 | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #dee948 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | 2px solid #000000 @ 0 offset 2px | = |
| Font | Suisse Intl 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0d1d39 | = |
| Transition | none | = |
| Cursor | default | = |
| Painted layers | select.appearance-none.w-full 576.0x48.0 bg #f3f3f4 r 6px outline 2px solid #000000 @ 0 offset 2px | select.appearance-none.w-full 576.0x48.0 bg #f3f3f4 r 6px shadow #ffffff 0px 0px 0px 0px, #dee948 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field |

Crops: `demo-field-default.png`, `demo-field-focused.png`.

### Auth shell (app.frontapp.com)

#### app-panel

Auth panel. The sign-in card on app.frontapp.com — the elevated panel holding the e-mail field, Continue, the SSO buttons and the legal links.

Page: signin. Selector: `signin card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 332 x 576.69 |
| Padding | 48px |
| Gap | 32px |
| Border | 1px solid #000000 @ 0.08 |
| Radius | 20px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.09 0px 2px 8px 0px |
| Outline | none |
| Font | system-ui 14px/14px 400 |
| Letter spacing | normal |
| Colour | #15131b |
| Text node | span.sc-385091d5-1.eegbkz: system-ui 14px/20px 700, #ffffff |
| Transition | none |
| Cursor | default |
| Icon | 112 x 26.69, colour #15131b |
| Painted layers | form.sc-f4506f74-1.kXddCT 332.0x576.7 bg #ffffff border T:1px #000000 @ 0.08 / R:1px #000000 @ 0.08 / B:1px #000000 @ 0.08 / L:1px #000000 @ 0.08 r 20px shadow #000000 @ 0.09 0px 2px 8px 0px; div.sc-eafbd4e-2.fowyWF 234.0x38.0 bg #000000 @ 0.05 r 6px outline 2px solid #000000 @ 0 offset 0px; div.sc-eafbd4e-2.fowyWF 234.0x38.0 bg #000000 @ 0.05 r 6px outline 2px solid #000000 @ 0 offset 0px; button.sc-385091d5-0.khndyR 234.0x38.0 bg #6257f4 r 8px; div::before.sc-f4506f74-3.bcTkbZ 58.9062pxx1px bg #000000 @ 0.08; div::after.sc-f4506f74-3.bcTkbZ 58.9062pxx1px bg #000000 @ 0.08 |
| How | at rest |

Crops: `app-panel-default.png`.

#### app-email

Email field. The e-mail input on the sign-in form; focused and typed into then cleared — Enter was never pressed and nothing was submitted.

Page: signin. Selector: `signin input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 210 x 20 | = | 186 x 20 |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Arial 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #15131b | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #a9abb2, opacity 1 | = | = |
| Ancestor paint | 1 up div.sc-eafbd4e-2.fowyWF bg #000000 @ 0.05 outline 2px solid #000000 @ 0 | 1 up div.sc-eafbd4e-2.fowyWF bg #000000 @ 0.08 outline 2px solid #6257f4 | 1 up div.sc-eafbd4e-2.fowyWF bg #000000 @ 0.08 outline 2px solid #6257f4 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `app-email-default.png`, `app-email-focused.png`, `app-email-filled.png`.

#### app-continue

Continue button. The sign-in form's primary button (the --color-bg-fill-brand fill); measured, never pressed.

Page: signin. Selector: `signin Continue`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 234 x 38 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #6257f4 | #584def | = | #3c3faa |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | system-ui 14px/20px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.sc-385091d5-1.eegbkz: system-ui 14px/20px 700, #ffffff | = | = | = |
| Transition | background-color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.sc-385091d5-0.khndyR 234.0x38.0 bg #6257f4 r 8px | button.sc-385091d5-0.khndyR 234.0x38.0 bg #584def r 8px | = | button.sc-385091d5-0.khndyR 234.0x38.0 bg #3c3faa r 8px |
| Ancestor paint | 2 up form.sc-f4506f74-1.kXddCT bg #ffffff shadow #000000 @ 0.09 0px 2px 8px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `app-continue-default.png`, `app-continue-hover.png`, `app-continue-focus-visible.png`, `app-continue-pressed.png`.

#### app-sso

SSO button. A single-sign-on button on the auth shell; measured, never pressed.

Page: signin. Selector: `signin SSO`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 234 x 38 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #d8d6db | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff @ 0 | #000000 @ 0.05 | = | #000000 @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | system-ui 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #15131b | = | = | = |
| Text node | span.sc-385091d5-1.eegbkz: system-ui 14px/20px 500, #15131b | = | = | = |
| Transition | background-color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.sc-385091d5-0.khndyR 234.0x38.0 bg #ffffff @ 0 border T:1px #d8d6db / R:1px #d8d6db / B:1px #d8d6db / L:1px #d8d6db r 8px | button.sc-385091d5-0.khndyR 234.0x38.0 bg #000000 @ 0.05 border T:1px #d8d6db / R:1px #d8d6db / B:1px #d8d6db / L:1px #d8d6db r 8px | = | button.sc-385091d5-0.khndyR 234.0x38.0 bg #000000 @ 0.08 border T:1px #d8d6db / R:1px #d8d6db / B:1px #d8d6db / L:1px #d8d6db r 8px |
| Ancestor paint | 2 up form.sc-f4506f74-1.kXddCT bg #ffffff shadow #000000 @ 0.09 0px 2px 8px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `app-sso-default.png`, `app-sso-hover.png`, `app-sso-focus-visible.png`, `app-sso-pressed.png`.

#### app-forgot

Forgot link. The "Forgot password" link to /forgot-password; measured, never followed.

Page: signin. Selector: `signin Forgot`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 234 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | system-ui 12px/16px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #584def | #3c3faa | = | #3c3faa |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 3 up form.sc-f4506f74-1.kXddCT bg #ffffff shadow #000000 @ 0.09 0px 2px 8px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `app-forgot-default.png`, `app-forgot-hover.png`, `app-forgot-focus-visible.png`, `app-forgot-pressed.png`.

#### appd-panel

Auth panel under [data-theme=dark]. The sign-in card on app.frontapp.com under [data-theme=dark] — the elevated panel holding the e-mail field, Continue, the SSO buttons and the legal links.

Page: signin-dark. Selector: `signin card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 332 x 576.69 |
| Padding | 48px |
| Gap | 32px |
| Border | 1px solid #ffffff @ 0.08 |
| Radius | 20px |
| Background | #221e29 |
| Box shadow | #000000 @ 0.09 0px 2px 8px 0px |
| Outline | none |
| Font | system-ui 14px/14px 400 |
| Letter spacing | normal |
| Colour | #f4f2f8 |
| Text node | span.sc-385091d5-1.eegbkz: system-ui 14px/20px 700, #ffffff |
| Transition | none |
| Cursor | default |
| Icon | 112 x 26.69, colour #f4f2f8 |
| Painted layers | form.sc-f4506f74-1.kXddCT 332.0x576.7 bg #221e29 border T:1px #ffffff @ 0.08 / R:1px #ffffff @ 0.08 / B:1px #ffffff @ 0.08 / L:1px #ffffff @ 0.08 r 20px shadow #000000 @ 0.09 0px 2px 8px 0px; div.sc-eafbd4e-2.fowyWF 234.0x38.0 bg #ffffff @ 0.08 r 6px outline 2px solid #000000 @ 0 offset 0px; div.sc-eafbd4e-2.fowyWF 234.0x38.0 bg #ffffff @ 0.08 r 6px outline 2px solid #000000 @ 0 offset 0px; button.sc-385091d5-0.khndyR 234.0x38.0 bg #584def r 8px; div::before.sc-f4506f74-3.bcTkbZ 58.9062pxx1px bg #ffffff @ 0.08; div::after.sc-f4506f74-3.bcTkbZ 58.9062pxx1px bg #ffffff @ 0.08 |
| How | at rest |

Crops: `appd-panel-default.png`.

#### appd-email

Email field under [data-theme=dark]. The e-mail input on the sign-in form under [data-theme=dark]; focused and typed into then cleared — Enter was never pressed and nothing was submitted.

Page: signin-dark. Selector: `signin input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 210 x 20 | = | 186 x 20 |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Arial 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #f4f2f8 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #656972, opacity 1 | = | = |
| Ancestor paint | 1 up div.sc-eafbd4e-2.fowyWF bg #ffffff @ 0.08 outline 2px solid #000000 @ 0 | 1 up div.sc-eafbd4e-2.fowyWF bg #ffffff @ 0.12 outline 2px solid #6257f4 | 1 up div.sc-eafbd4e-2.fowyWF bg #ffffff @ 0.12 outline 2px solid #6257f4 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `appd-email-default.png`, `appd-email-focused.png`, `appd-email-filled.png`.

#### appd-continue

Continue button under [data-theme=dark]. The sign-in form's primary button under [data-theme=dark] (the --color-bg-fill-brand fill); measured, never pressed.

Page: signin-dark. Selector: `signin Continue`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 234 x 38 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #584def | #6257f4 | = | #7989f7 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | system-ui 14px/20px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.sc-385091d5-1.eegbkz: system-ui 14px/20px 700, #ffffff | = | = | = |
| Transition | background-color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.sc-385091d5-0.khndyR 234.0x38.0 bg #584def r 8px | button.sc-385091d5-0.khndyR 234.0x38.0 bg #6257f4 r 8px | = | button.sc-385091d5-0.khndyR 234.0x38.0 bg #7989f7 r 8px |
| Ancestor paint | 2 up form.sc-f4506f74-1.kXddCT bg #221e29 shadow #000000 @ 0.09 0px 2px 8px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `appd-continue-default.png`, `appd-continue-hover.png`, `appd-continue-focus-visible.png`, `appd-continue-pressed.png`.

#### appd-sso

SSO button under [data-theme=dark]. A single-sign-on button on the auth shell under [data-theme=dark]; measured, never pressed.

Page: signin-dark. Selector: `signin SSO`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 234 x 38 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #504c57 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff @ 0 | #ffffff @ 0.05 | = | #ffffff @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | system-ui 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f4f2f8 | = | = | = |
| Text node | span.sc-385091d5-1.eegbkz: system-ui 14px/20px 500, #f4f2f8 | = | = | = |
| Transition | background-color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.sc-385091d5-0.khndyR 234.0x38.0 bg #ffffff @ 0 border T:1px #504c57 / R:1px #504c57 / B:1px #504c57 / L:1px #504c57 r 8px | button.sc-385091d5-0.khndyR 234.0x38.0 bg #ffffff @ 0.05 border T:1px #504c57 / R:1px #504c57 / B:1px #504c57 / L:1px #504c57 r 8px | = | button.sc-385091d5-0.khndyR 234.0x38.0 bg #ffffff @ 0.08 border T:1px #504c57 / R:1px #504c57 / B:1px #504c57 / L:1px #504c57 r 8px |
| Ancestor paint | 2 up form.sc-f4506f74-1.kXddCT bg #221e29 shadow #000000 @ 0.09 0px 2px 8px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `appd-sso-default.png`, `appd-sso-hover.png`, `appd-sso-focus-visible.png`, `appd-sso-pressed.png`.

#### appd-forgot

Forgot link under [data-theme=dark]. The "Forgot password" link to /forgot-password; measured, never followed.

Page: signin-dark. Selector: `signin Forgot`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 234 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | system-ui 12px/16px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #7989f7 | #6257f4 | = | #6257f4 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 3 up form.sc-f4506f74-1.kXddCT bg #221e29 shadow #000000 @ 0.09 0px 2px 8px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `appd-forgot-default.png`, `appd-forgot-hover.png`, `appd-forgot-focus-visible.png`, `appd-forgot-pressed.png`.

#### signup-panel

Signup panel. The create-account card on app.frontapp.com/signup.

Page: signup-app. Selector: `signup card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 332 x 576.69 |
| Padding | 48px |
| Gap | 32px |
| Border | 1px solid #000000 @ 0.08 |
| Radius | 20px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.09 0px 2px 8px 0px |
| Outline | none |
| Font | system-ui 14px/14px 400 |
| Letter spacing | normal |
| Colour | #15131b |
| Text node | span.sc-385091d5-1.eegbkz: system-ui 14px/20px 700, #ffffff |
| Transition | none |
| Cursor | default |
| Icon | 112 x 26.69, colour #15131b |
| Painted layers | form.sc-f4506f74-1.kXddCT 332.0x576.7 bg #ffffff border T:1px #000000 @ 0.08 / R:1px #000000 @ 0.08 / B:1px #000000 @ 0.08 / L:1px #000000 @ 0.08 r 20px shadow #000000 @ 0.09 0px 2px 8px 0px; div.sc-eafbd4e-2.fowyWF 234.0x38.0 bg #000000 @ 0.05 r 6px outline 2px solid #000000 @ 0 offset 0px; div.sc-eafbd4e-2.fowyWF 234.0x38.0 bg #000000 @ 0.05 r 6px outline 2px solid #000000 @ 0 offset 0px; button.sc-385091d5-0.khndyR 234.0x38.0 bg #6257f4 r 8px; div::before.sc-f4506f74-3.bcTkbZ 58.8906pxx1px bg #000000 @ 0.08; div::after.sc-f4506f74-3.bcTkbZ 58.9062pxx1px bg #000000 @ 0.08 |
| How | at rest |

Crops: `signup-panel-default.png`.

#### signup-email

Signup email field. The e-mail input on the product signup form; typed into then cleared — never submitted.

Page: signup-app. Selector: `signup email`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 210 x 20 | = | 186 x 20 |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Arial 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #15131b | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #a9abb2, opacity 1 | = | = |
| Ancestor paint | 1 up div.sc-eafbd4e-2.fowyWF bg #000000 @ 0.05 outline 2px solid #000000 @ 0 | 1 up div.sc-eafbd4e-2.fowyWF bg #000000 @ 0.08 outline 2px solid #6257f4 | 1 up div.sc-eafbd4e-2.fowyWF bg #000000 @ 0.08 outline 2px solid #6257f4 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `signup-email-default.png`, `signup-email-focused.png`, `signup-email-filled.png`.

#### forgot-panel

Reset panel. The reset-password card on app.frontapp.com/forgot-password.

Page: forgot. Selector: `forgot card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 332 x 576.69 |
| Padding | 48px |
| Gap | 32px |
| Border | 1px solid #000000 @ 0.08 |
| Radius | 20px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.09 0px 2px 8px 0px |
| Outline | none |
| Font | system-ui 14px/14px 400 |
| Letter spacing | normal |
| Colour | #15131b |
| Text node | span.sc-385091d5-1.eegbkz: system-ui 14px/20px 700, #ffffff |
| Transition | none |
| Cursor | default |
| Icon | 112 x 26.69, colour #15131b |
| Painted layers | form.sc-f4506f74-1.kXddCT 332.0x576.7 bg #ffffff border T:1px #000000 @ 0.08 / R:1px #000000 @ 0.08 / B:1px #000000 @ 0.08 / L:1px #000000 @ 0.08 r 20px shadow #000000 @ 0.09 0px 2px 8px 0px; div.sc-eafbd4e-2.fowyWF 234.0x38.0 bg #000000 @ 0.05 r 6px outline 2px solid #000000 @ 0 offset 0px; div.sc-eafbd4e-2.fowyWF 234.0x38.0 bg #000000 @ 0.05 r 6px outline 2px solid #000000 @ 0 offset 0px; button.sc-385091d5-0.khndyR 234.0x38.0 bg #6257f4 r 8px; div::before.sc-f4506f74-3.bcTkbZ 58.9062pxx1px bg #000000 @ 0.08; div::after.sc-f4506f74-3.bcTkbZ 58.9062pxx1px bg #000000 @ 0.08 |
| How | at rest |

Crops: `forgot-panel-default.png`.

#### forgot-email

Reset email field. The e-mail input on the reset form; typed into then cleared — never submitted.

Page: forgot. Selector: `forgot email`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 210 x 20 | = | 186 x 20 |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Arial 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #15131b | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #a9abb2, opacity 1 | = | = |
| Ancestor paint | 1 up div.sc-eafbd4e-2.fowyWF bg #000000 @ 0.05 outline 2px solid #000000 @ 0 | 1 up div.sc-eafbd4e-2.fowyWF bg #000000 @ 0.08 outline 2px solid #6257f4 | 1 up div.sc-eafbd4e-2.fowyWF bg #000000 @ 0.08 outline 2px solid #6257f4 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `forgot-email-default.png`, `forgot-email-focused.png`, `forgot-email-filled.png`.

#### forgot-submit

Reset submit. The submit on /forgot-password — the route paints the same auth card as /signin, so no dedicated reset button exists signed out; measured, never pressed.

Page: forgot. Selector: `forgot submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 234 x 38 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #6257f4 | #584def | = | #3c3faa |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | system-ui 14px/20px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.sc-385091d5-1.eegbkz: system-ui 14px/20px 700, #ffffff | = | = | = |
| Transition | background-color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.sc-385091d5-0.khndyR 234.0x38.0 bg #6257f4 r 8px | button.sc-385091d5-0.khndyR 234.0x38.0 bg #584def r 8px | = | button.sc-385091d5-0.khndyR 234.0x38.0 bg #3c3faa r 8px |
| Ancestor paint | 2 up form.sc-f4506f74-1.kXddCT bg #ffffff shadow #000000 @ 0.09 0px 2px 8px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `forgot-submit-default.png`, `forgot-submit-hover.png`, `forgot-submit-focus-visible.png`, `forgot-submit-pressed.png`.

#### signup-app-submit

Signup submit (app). The submit on app.frontapp.com/signup — the route paints the same auth card as /signin (email, password, "Sign in"); measured, never pressed.

Page: signup-app. Selector: `app signup submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 234 x 38 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #6257f4 | #584def | = | #3c3faa |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | system-ui 14px/20px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.sc-385091d5-1.eegbkz: system-ui 14px/20px 700, #ffffff | = | = | = |
| Transition | background-color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.sc-385091d5-0.khndyR 234.0x38.0 bg #6257f4 r 8px | button.sc-385091d5-0.khndyR 234.0x38.0 bg #584def r 8px | = | button.sc-385091d5-0.khndyR 234.0x38.0 bg #3c3faa r 8px |
| Ancestor paint | 2 up form.sc-f4506f74-1.kXddCT bg #ffffff shadow #000000 @ 0.09 0px 2px 8px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-app-submit-default.png`, `signup-app-submit-hover.png`, `signup-app-submit-focus-visible.png`, `signup-app-submit-pressed.png`.

### Help centre (help.front.com)

#### help-header

Help header. The help centre's own header (Front's Knowledge Base product): the mark, the nav and the search.

Page: help. Selector: `help header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 306 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #f8f1fe |
| Box shadow | none |
| Outline | none |
| Font | CustomFont 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.page-header-inner-title: CustomFont 18px/21.6px 600, #3e3e40 |
| Transition | none |
| Icon | 0 x 0, colour #000000 |
| Painted layers | div.page-header 1440.0x306.0 bg #f8f1fe; div::before.page-header-inner-title-container 1pxx50px bg #3e3e40; a.kb-button.primary 98.0x30.0 bg #803fbf r 100px; div.search-box 440.0x40.0 bg #000000 @ 0.1 r 8px; button.ais-SearchBox-submit 0.0x0.0 bg #efefef; button.ais-SearchBox-reset 0.0x0.0 bg #efefef |
| Ancestor paint | 1 up div.page-wrapper bg #ffffff |
| How | at rest |

Crops: `help-header-default.png`.

#### help-search

Search field. The help centre's search input; focused and typed into then cleared — no search was submitted.

Page: help. Selector: `help search input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 408 x 40 | 404 x 40 | 404 x 40 |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | CustomFont 14px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #3e3e40 | #19191a | #19191a |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #3e3e40, opacity 0.8 | #19191a, opacity 0.8 | #19191a, opacity 0.8 |
| How | at rest | clicked into the field | typed "channels", then deleted; nothing sent |

Crops: `help-search-default.png`, `help-search-focused.png`, `help-search-filled.png`.

#### help-card

Category card. A help-category card (kb-category-card) on the help home; measured, never followed.

Page: help. Selector: `help category card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 402 x 259 | = |
| Padding | 32px | = |
| Border | 1px solid #000000 @ 0.08 | = |
| Radius | 24px | = |
| Background | #ffffff | #f5f5f5 |
| Box shadow | #000000 @ 0.08 0px 1px 9px 0px | = |
| Outline | none | = |
| Font | CustomFont 16px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #0000ee | = |
| Text node | div.kb-category-name: CustomFont 18px/24px 600, #19191a | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 32 x 32, colour #803fbf | = |
| Painted layers | a.kb-category-card 402.0x259.0 bg #ffffff border T:1px #000000 @ 0.08 / R:1px #000000 @ 0.08 / B:1px #000000 @ 0.08 / L:1px #000000 @ 0.08 r 24px shadow #000000 @ 0.08 0px 1px 9px 0px; div.kb-category-icon-background 64.0x64.0 bg #803fbf | a.kb-category-card 402.0x259.0 bg #f5f5f5 border T:1px #000000 @ 0.08 / R:1px #000000 @ 0.08 / B:1px #000000 @ 0.08 / L:1px #000000 @ 0.08 r 24px shadow #000000 @ 0.08 0px 1px 9px 0px; div.kb-category-icon-background 64.0x64.0 bg #803fbf |
| How | at rest | mouse hover |

Crops: `help-card-default.png`, `help-card-hover.png`.

#### helpa-h1

Article headline. A help article headline inside Front's Knowledge Base product.

Page: help-article. Selector: `help article h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 630 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CustomFont 24px/32px 800 |
| Letter spacing | normal |
| Colour | #19191a |
| Transition | none |
| Ancestor paint | 1 up div.article-content-container bg #ffffff shadow #000000 @ 0.08 0px 1px 9px 0px |
| How | at rest |

Crops: `helpa-h1-default.png`.

#### helpa-body

Article body. The article body column (--article-* vars paint the prose).

Page: help-article. Selector: `help article body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 840 x 5285.33 |
| Padding | 80px 104px |
| Border | 1px solid #000000 @ 0.08 |
| Radius | 24px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.08 0px 1px 9px 0px |
| Outline | none |
| Font | CustomFont 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.article-title: CustomFont 24px/32px 800, #19191a |
| Transition | none |
| Painted layers | div.article-content-container 840.0x5285.3 bg #ffffff border T:1px #000000 @ 0.08 / R:1px #000000 @ 0.08 / B:1px #000000 @ 0.08 / L:1px #000000 @ 0.08 r 24px shadow #000000 @ 0.08 0px 1px 9px 0px; div.kb-inline-icon.checkmark 0.0x0.0 bg #10aa40; div.kb-inline-icon.link 16.0x16.0 bg #3e3e40; hr.kb-horizontal-rule 630.0x2.0 border T:1px #d4d6d9 / R:1px #d4d6d9 / B:1px #d4d6d9 / L:1px #d4d6d9; div.kb-inline-icon.checkmark 0.0x0.0 bg #10aa40; div.kb-inline-icon.link 16.0x16.0 bg #3e3e40 |
| How | at rest |

Crops: none.

#### helpa-crumb

Breadcrumb link. A breadcrumb or section link on the article page; measured, never followed.

Page: help-article. Selector: `help article link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 145 x 21.59 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | CustomFont 18px/21.6px 600 | = |
| Letter spacing | normal | = |
| Colour | #3e3e40 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `helpa-crumb-default.png`, `helpa-crumb-hover.png`.

#### help-card-2

Category card (second). A second help-category card on the help home — the home lists categories, not article links; measured, never followed.

Page: help. Selector: `help category card 2`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 402 x 259 | = |
| Padding | 32px | = |
| Border | 1px solid #000000 @ 0.08 | = |
| Radius | 24px | = |
| Background | #ffffff | #f5f5f5 |
| Box shadow | #000000 @ 0.08 0px 1px 9px 0px | = |
| Outline | none | = |
| Font | CustomFont 16px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #0000ee | = |
| Text node | div.kb-category-name: CustomFont 18px/24px 600, #19191a | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 32 x 32, colour #803fbf | = |
| Painted layers | a.kb-category-card 402.0x259.0 bg #ffffff border T:1px #000000 @ 0.08 / R:1px #000000 @ 0.08 / B:1px #000000 @ 0.08 / L:1px #000000 @ 0.08 r 24px shadow #000000 @ 0.08 0px 1px 9px 0px; div.kb-category-icon-background 64.0x64.0 bg #803fbf | a.kb-category-card 402.0x259.0 bg #f5f5f5 border T:1px #000000 @ 0.08 / R:1px #000000 @ 0.08 / B:1px #000000 @ 0.08 / L:1px #000000 @ 0.08 r 24px shadow #000000 @ 0.08 0px 1px 9px 0px; div.kb-category-icon-background 64.0x64.0 bg #803fbf |
| How | at rest | mouse hover |

Crops: `help-card-2-default.png`, `help-card-2-hover.png`.

### Developer portal (dev.frontapp.com)

#### dev-header

Dev header. The developer portal's header — the ReadMe vendor platform skinned to Front.

Page: dev. Selector: `dev header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1430 x 94 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #300c41 |
| Box shadow | #000000 @ 0.1 0px 1px 0px 0px |
| Outline | none |
| Font | Twemoji Country Flags 14px/normal 400 |
| Letter spacing | normal |
| Colour | #061b36 |
| Text node | a.Button.Button_md: Twemoji Country Flags 14px/normal 500, #300c41 |
| Transition | none |
| Icon | 0 x 0, colour #484c58 |
| Painted layers | header.Header3zzata9F_ZPQ.rm-Header_classic 1430.0x94.0 bg #300c41 shadow #000000 @ 0.1 0px 1px 0px 0px; div.rm-Header-top.Header-topuTMpygDG4e1V 1430.0x52.0 border B:1px #000000 @ 0.1; a.Button.Button_md 119.6x32.0 bg #ffffff border T:1px #000000 @ 0.1 / R:1px #000000 @ 0.1 / B:1px #000000 @ 0.1 / L:1px #000000 @ 0.1 r 6px shadow #051c8e @ 0.2 0px 0px 0px 1px inset; a.rm-Logo.Header-logo1Xy41PtkzbdG 36.0x41.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px; a.Button.Button_md 67.7x32.0 bg #ffffff @ 0.1 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px; a.Button.Button_md 113.8x32.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px |
| How | at rest |

Crops: `dev-header-default.png`.

#### dev-search

Search trigger. The portal's search control — a local UI toggle for the search overlay; measured at rest, never opened.

Page: dev. Selector: `dev search`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 150 x 32 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0.1 0px 0px 0px 1px | = | #ffffff @ 0.75 0px 0px 0px 1px, #ffffff @ 0.25 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Twemoji Country Flags 13.3333px/32px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.Header-search-placeholder3Vx4OmMPcjAi.rm-SearchToggle-placeholder: Twemoji Country Flags 14px/32px 400, #666b79 | = | = | = |
| Transition | box-shadow, -webkit-box-shadow 0.15s, 0.15s cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.rm-SearchToggle 150.0x32.0 bg #ffffff r 6px shadow #000000 @ 0.1 0px 0px 0px 1px | = | button.rm-SearchToggle 150.0x32.0 bg #ffffff r 6px shadow #ffffff @ 0.75 0px 0px 0px 1px, #ffffff @ 0.25 0px 0px 0px 4px | = |
| Ancestor paint | 1 up div.rm-Header-search.Header-searchtb6Foi0-D9Vx shadow #300c41 -12px 0px 6px -6px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `dev-search-default.png`, `dev-search-hover.png`, `dev-search-focus-visible.png`, `dev-search-pressed.png`.

#### dev-h1

Doc headline. A docs headline on dev.frontapp.com (ReadMe).

Page: dev. Selector: `dev h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1078 x 39.84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Twemoji Country Flags 31px/39.8567px 600 |
| Letter spacing | normal |
| Colour | #32343a |
| Transition | none |
| How | at rest |

Crops: `dev-h1-default.png`.

#### dev-side-link

Sidebar link. A sidebar navigation link in the docs tree; measured, never followed.

Page: dev. Selector: `dev sidebar link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 251 x 32 | = |
| Padding | 6.006px 5px 6.006px 10px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #0090da @ 0.09 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Twemoji Country Flags 14px/20.0004px 450 | = |
| Letter spacing | normal | = |
| Colour | #0090da | = |
| Text node | span.Sidebar-link-text_label1gCT_uPnx7Gu: Twemoji Country Flags 14px/20.0004px 450, #0090da | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | a.Sidebar-link2Dsha-r-GKh2.childless 251.0x32.0 bg #0090da @ 0.09 r 8px | = |
| How | at rest | mouse hover |

Crops: `dev-side-link-default.png`, `dev-side-link-hover.png`.

#### devref-h1

Reference headline. An API-reference page headline on the ReadMe stack.

Page: dev-ref. Selector: `dev ref h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 239.92 x 39.84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Twemoji Country Flags 31px/39.8567px 600 |
| Letter spacing | normal |
| Colour | #32343a |
| Transition | none |
| How | at rest |

Crops: none.

#### devref-code

Code block. A code block on the reference page.

Page: dev-ref. Selector: `dev pre/code`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 430 x 45 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #ffffff @ 0.05; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #000000 @ 0.1 0px -1px 0px 0px inset |
| Outline | none |
| Font | monospace 13px/19.5px 400 |
| Letter spacing | normal |
| Colour | #32343a |
| Text node | div.CodeMirror-linenumber.CodeMirror-gutter-elt: SF Mono 12px/18px 400, #bebcd7 |
| Transition | none |
| Painted layers | pre.CodeSnippet 430.0x45.0 border B:1px #ffffff @ 0.05 shadow #000000 @ 0.1 0px -1px 0px 0px inset; div.CodeMirror-gutter-filler 0.0x0.0 bg #ffffff; div.CodeMirror-sizer 446.0x44.0 border R:50px #000000 @ 0 |
| Ancestor paint | 1 up div.APIRequest3ZiZ6icF7aNH.rm-PlaygroundRequest bg #2b2c31 shadow #ffffff @ 0.3 0px 1px 0px 0px inset, #000000 @ 0.1 0px -1px 2px 0px inset |
| How | at rest |

Crops: `devref-code-default.png`.

### Mobile (390 wide)

#### m-topbar

Mobile top bar. The phone header at 390 wide: the wordmark, the CTAs and the burger.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 14px/20px 400 |
| Letter spacing | normal |
| Colour | #1c1e20 |
| Transition | all 0.6s cubic-bezier(0.16, 1, 0.3, 1) |
| Icon | 112 x 26, colour #ffffff, fill #000000 |
| Painted layers | button.block.button 0.0x0.0 bg #ffffff r 40px; button.block.button 0.0x0.0 r 40px shadow #d0c6f0 0px 0px 0px 1px inset; button.button.button-size-circle-medium 44.0x44.0 bg #f3f3f4 r 44px; div.rounded-20.bg-white 0.0x0.0 bg #ffffff border T:5px #e2dcf6 / R:5px #e2dcf6 / B:5px #e2dcf6 / L:5px #e2dcf6 r 20px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.04 0px 60px 60px 0px, #000000 @ 0.03 0px 30.375px 26.156px 0px, #000000 @ 0.02 0px 12px 9.75px 0px, #000000 @ 0.01 0px 2.625px 3.469px 0px; div.table-cell.align-top 0.0x0.0 border R:1px #dedfe2; div.table-cell.align-top 0.0x0.0 border R:1px #dedfe2 / L:1px #dedfe2 |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-menu-btn

Burger button. The mobile menu button — a local UI toggle; the opened state was measured after activating it.

Page: mobile. Selector: `mobile menu button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 44px | = | = | = | = |
| Background | #f3f3f4 | #dedfe2 | #dedfe2 | #dedfe2 | #dfe0e3 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px solid #1c1e20 offset 1.98438px | = | = |
| Font | Suisse Intl 14px/44px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #1c1e20 | = | = | = | = |
| Transition | all 0.4s cubic-bezier(0.16, 1, 0.3, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | button.button.button-size-circle-medium 44.0x44.0 bg #f3f3f4 r 44px | button.button.button-size-circle-medium 44.0x44.0 bg #dedfe2 r 44px | button.button.button-size-circle-medium 44.0x44.0 bg #dedfe2 r 44px outline 1px solid #1c1e20 offset 1.98438px | button.button.button-size-circle-medium 44.0x44.0 bg #dedfe2 r 44px | button.button.button-size-circle-medium 44.0x44.0 bg #dfe0e3 r 44px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `m-menu-btn-default.png`, `m-menu-btn-hover.png`, `m-menu-btn-focus-visible.png`, `m-menu-btn-pressed.png`, `m-menu-btn-opened.png`.

#### m-drawer

Mobile nav overlay. The navigation overlay opened by the burger (the same destinations as the desktop header); its links were never followed.

Page: mobile. Selector: `mobile nav overlay`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 96px 0px 120px 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 14px/20px 400 |
| Letter spacing | normal |
| Colour | #1c1e20 |
| Text node | span.block: Suisse Intl 28px/28px 500, #1c1e20 |
| Transition | none |
| Icon | 20 x 20, colour #1c1e20 |
| Painted layers | div.2xl:hidden.fixed 390.0x844.0 bg #ffffff; div.border-b.border-solid 390.0x109.0 border B:1px #dedfe2; div.border-b.border-solid 390.0x109.0 border B:1px #dedfe2; div.border-b.border-solid 390.0x109.0 border B:1px #dedfe2; div.border-b.border-solid 390.0x109.0 border B:1px #dedfe2; div.border-b.border-solid 390.0x109.0 border B:1px #dedfe2 |
| How | at rest |

Crops: `m-drawer-default.png`.

#### m-hero-h1

Mobile hero headline. The masthead at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 184 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 36px/46px 500 |
| Letter spacing | -0.75px |
| Colour | #f8f1fe |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-cta

Mobile CTA. The hero action at 390 wide; measured never followed.

Page: mobile. Selector: `mobile CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 167 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #caccd0 0px 0px 0px 1px inset | #a1a5ad 0px 0px 0px 1px inset | #a1a5ad 0px 0px 0px 1px inset | #a1a5ad 0px 0px 0px 1px inset |
| Outline | none | = | 1px solid #000000 offset 1.98438px | = |
| Font | Suisse Intl 16px/40px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | all 0.4s cubic-bezier(0.16, 1, 0.3, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.block.button 167.0x40.0 r 40px shadow #caccd0 0px 0px 0px 1px inset | button.block.button 167.0x40.0 r 40px shadow #a1a5ad 0px 0px 0px 1px inset | button.block.button 167.0x40.0 r 40px shadow #a1a5ad 0px 0px 0px 1px inset outline 1px solid #000000 offset 1.98438px | button.block.button 167.0x40.0 r 40px shadow #a1a5ad 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-cta-default.png`, `m-cta-hover.png`, `m-cta-focus-visible.png`, `m-cta-pressed.png`.

## Transitions declared in the readable stylesheets

front.com's sheets are same-origin and fully readable (the Next.js chunks, the app shell's injected token layer and the Froyo sheet all sit on first-party hosts); vendor sheets (Qualified, ReadMe CDN) are unreadable to the CSSOM, so their rows list only what the page computed.

- dev: `background 0.5s cubic-bezier(0.16, 1, 0.3, 1), color 0.5s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.5s cubic-bezier(0.16, 1, 0.3, 1)`, `color 0.5s cubic-bezier(0.16, 1, 0.3, 1)`, `opacity 0.5s cubic-bezier(0.16, 1, 0.3, 1)`, `0.2s ease-in-out`, `0.2s ease-out`, `0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94)`

- dev-ref: `background 0.5s cubic-bezier(0.16, 1, 0.3, 1), color 0.5s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.5s cubic-bezier(0.16, 1, 0.3, 1)`, `color 0.5s cubic-bezier(0.16, 1, 0.3, 1)`, `opacity 0.5s cubic-bezier(0.16, 1, 0.3, 1)`

- forgot: `background-color 100ms`, `outline-color 100ms, background-color 100ms`

- help: `0.1s`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `300ms ease-in`, `0.2s`, `0.25s ease-out`, `0.1s ease-in`

- help-article: `0.1s`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `300ms ease-in`, `0.2s`, `0.25s ease-out`, `0.1s ease-in`

- home: `text-decoration-color 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `opacity 0.2s cubic-bezier(0.455, 0.03, 0.515, 0.955), transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)`, `transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)`, `background-size 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `0.4s cubic-bezier(0.16, 1, 0.3, 1)`, `color 9999s ease-out 9999s, background-color 9999s ease-out 9999s`, `0.1s`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `300ms ease-in`, `0.2s`

- pricing: `text-decoration-color 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `opacity 0.2s cubic-bezier(0.455, 0.03, 0.515, 0.955), transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)`, `transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)`, `background-size 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `0.4s cubic-bezier(0.16, 1, 0.3, 1)`, `color 9999s ease-out 9999s, background-color 9999s ease-out 9999s`, `background-position 0.3s 0.3s`, `0.1s`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `300ms ease-in`

- product: `text-decoration-color 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `opacity 0.2s cubic-bezier(0.455, 0.03, 0.515, 0.955), transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)`, `transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)`, `background-size 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `0.4s cubic-bezier(0.16, 1, 0.3, 1)`, `color 9999s ease-out 9999s, background-color 9999s ease-out 9999s`, `background-position 0.3s 0.3s`, `opacity 0.3s`, `transform 0.2s, top 0.2s`, `transform 0.2s, left 0.2s`, `transform 0.2s, right 0.2s`, `0.1s`

- request-demo: `text-decoration-color 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `opacity 0.2s cubic-bezier(0.455, 0.03, 0.515, 0.955), transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)`, `transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)`, `background-size 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `0.4s cubic-bezier(0.16, 1, 0.3, 1)`, `color 9999s ease-out 9999s, background-color 9999s ease-out 9999s`, `opacity 0.25s ease-in-out 0.1s`, `background-color 400ms linear`, `0.1s`, `0.2s ease-in`, `0.4s`, `150ms ease-in`

- signin: `background-color 100ms`, `outline-color 100ms, background-color 100ms`

- signin-dark: `background-color 100ms`, `outline-color 100ms, background-color 100ms`

- signup: `text-decoration-color 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `opacity 0.2s cubic-bezier(0.455, 0.03, 0.515, 0.955), transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)`, `transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)`, `background-size 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `0.4s cubic-bezier(0.16, 1, 0.3, 1)`, `color 9999s ease-out 9999s, background-color 9999s ease-out 9999s`, `opacity 0.25s ease-in-out 0.1s`, `background-color 400ms linear`, `0.1s`, `0.2s ease-in`, `0.4s`, `150ms ease-in`

- signup-app: `background-color 100ms`, `outline-color 100ms, background-color 100ms`
