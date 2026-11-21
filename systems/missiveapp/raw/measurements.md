# Missive component measurements

Computed styles read from missiveapp.com on 2026-11-20 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The desktop nav: logo, Product, Pricing, Customers, Resources, Log in, Book a demo, Try for free.

Page: home. Selector: `.navbar:not(.mobile-only)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 61 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 14px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div: Inter 14px/20px 400, #34363a |
| Transition | none |
| Icon | 144 x 36, colour #34363a |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | div.custom-nav.s-blur 1440.0x61.0 bg #ffffff border B:1px solid #f5f6f6; nav.navbar-submenu.w-dropdown-list 0.0x0.0 bg #dddddd; div.floating-menu 0.0x0.0 bg #ffffff shadow #e4e6e9 0px 1px 1px 0px, #000000 @ 0.05 0px 48px 56px -8px; nav.navbar-submenu.w-dropdown-list 0.0x0.0 bg #dddddd; div.floating-menu 0.0x0.0 bg #ffffff shadow #e4e6e9 0px 1px 1px 0px, #000000 @ 0.05 0px 48px 56px -8px; a.button-base.w-button 99.2x44.0 bg #2266ed r 8px |
| Ancestor paint | 1 up body.body bg #ffffff |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo.

Page: home. Selector: `.navbar a[href="/"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 144 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 14px/20px 400 |
| Letter spacing | normal |
| Colour | #2266ed |
| Transition | none |
| Cursor | pointer |
| Icon | 144 x 36, colour #34363a |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link. A top-level nav link. Measured, never followed.

Page: home. Selector: `nav a Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 70 x 44 | = | = | = |
| Padding | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f5f6f6 | = | #e4e6e9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #34363a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.button-base.s-ghost 70.0x44.0 bg #f5f6f6 r 8px | a.button-base.s-ghost 70.0x44.0 r 8px outline 1px auto #005fcc offset 1px | a.button-base.s-ghost 70.0x44.0 bg #e4e6e9 r 8px |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Log in link. Opens the mail.missiveapp.com login wall. Measured, never followed.

Page: home. Selector: `nav a Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 64.5 x 44 | = | = | = |
| Padding | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f5f6f6 | = | #e4e6e9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #34363a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.button-base.s-ghost 64.5x44.0 bg #f5f6f6 r 8px | a.button-base.s-ghost 64.5x44.0 r 8px outline 1px auto #005fcc offset 1px | a.button-base.s-ghost 64.5x44.0 bg #e4e6e9 r 8px |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-demo

Book a demo. Opens an external Calendly page. Measured, never followed.

Page: home. Selector: `nav a Book a demo`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 110.77 x 44 | = | = | = |
| Padding | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f5f6f6 | = | #e4e6e9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #34363a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.button-base.s-ghost 110.8x44.0 bg #f5f6f6 r 8px | a.button-base.s-ghost 110.8x44.0 r 8px outline 1px auto #005fcc offset 1px | a.button-base.s-ghost 110.8x44.0 bg #e4e6e9 r 8px |

Crops: `nav-demo-default.png`, `nav-demo-hover.png`, `nav-demo-focus-visible.png`, `nav-demo-pressed.png`.

#### nav-cta

Try for free. Opens the signup wall. Measured, never followed.

Page: home. Selector: `nav a Try for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 99.22 x 44 | = | = | = |
| Padding | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #2266ed | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button-base.w-button 99.2x44.0 bg #2266ed r 8px | a.button-base.w-button 99.2x44.0 bg #2266ed image linear-gradient(#000000 @ 0.15, #000000 @ 0.15) r 8px | a.button-base.w-button 99.2x44.0 bg #2266ed r 8px outline 1px auto #005fcc offset 1px | a.button-base.w-button 99.2x44.0 bg #2266ed image linear-gradient(#000000 @ 0.25, #000000 @ 0.25) r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Background image | - | linear-gradient(#000000 @ 0.15, #000000 @ 0.15) | = | linear-gradient(#000000 @ 0.25, #000000 @ 0.25) |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### flyout-trigger

Product menu trigger. The nav item that opens the Product mega menu.

Page: home. Selector: `.w-dropdown-toggle Product`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 95.81 x 44 | = | = | = |
| Padding | 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f5f6f6 | = | #e4e6e9 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #34363a | = | = | = |
| Text node | div: Inter 14px/20px 400, #34363a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #34363a | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | div.button-base.s-ghost 95.8x44.0 bg #f5f6f6 r 8px | = | div.button-base.s-ghost 95.8x44.0 bg #e4e6e9 r 8px |

Crops: `flyout-trigger-default.png`, `flyout-trigger-hover.png`, `flyout-trigger-focus-visible.png`, `flyout-trigger-pressed.png`.

#### flyout-open

Product menu, open. The Product mega menu after hover. Links are recorded in site-tree.md and not followed here.

Page: home. Selector: `Product dropdown`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 95.81 x 44 |
| Padding | 12px |
| Gap | 4px |
| Border | none |
| Radius | 8px |
| Background | #f5f6f6 |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #34363a |
| Text node | div: Inter 14px/20px 400, #34363a |
| Transition | none |
| Cursor | pointer |
| Icon | 16 x 16, colour #34363a |
| Painted layers | div.button-base.s-ghost 95.8x44.0 bg #f5f6f6 r 8px |
| How | own toggle |

Crops: `flyout-open-opened.png`.

### Home

#### hero-title

Hero title.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tiempos Headline 56px/60px 400 |
| Letter spacing | normal |
| Colour | #34363a |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-cta

Hero CTA. The hero Try for free. Measured, never followed.

Page: home. Selector: `hero Try for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 143.84 x 52 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #2266ed | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 17.84px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button-xl.w-button 143.8x52.0 bg #2266ed r 8px | a.button-xl.w-button 143.8x52.0 bg #2266ed image linear-gradient(#000000 @ 0.15, #000000 @ 0.15) r 8px | a.button-xl.w-button 143.8x52.0 bg #2266ed r 8px outline 1px auto #005fcc offset 1px | a.button-xl.w-button 143.8x52.0 bg #2266ed image linear-gradient(#000000 @ 0.25, #000000 @ 0.25) r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Background image | - | linear-gradient(#000000 @ 0.15, #000000 @ 0.15) | = | linear-gradient(#000000 @ 0.25, #000000 @ 0.25) |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-secondary

Watch demo. Opens the on-page demo lightbox. Measured, not submitted.

Page: home. Selector: `Watch demo`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 156.89 x 54 | = |
| Padding | 16px 24px | = |
| Border | 1px solid #e4e6e9 | 1px solid #cdd0d4 |
| Radius | 8px | = |
| Background | #f5f6f6 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 17.84px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #34363a | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | a.button-xl.s-secondary 156.9x54.0 bg #f5f6f6 border T:1px solid #e4e6e9 / R:1px solid #e4e6e9 / B:1px solid #e4e6e9 / L:1px solid #e4e6e9 r 8px | a.button-xl.s-secondary 156.9x54.0 bg #f5f6f6 image linear-gradient(#000000 @ 0.03, #000000 @ 0.03) border T:1px solid #cdd0d4 / R:1px solid #cdd0d4 / B:1px solid #cdd0d4 / L:1px solid #cdd0d4 r 8px |
| How | at rest | mouse hover |
| Background image | - | linear-gradient(#000000 @ 0.03, #000000 @ 0.03) |

Crops: `hero-secondary-default.png`, `hero-secondary-hover.png`.

#### section-title

Section heading.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 626.23 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 30px/36px 400 |
| Letter spacing | normal |
| Colour | #34363a |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### tab

Feature tab. An in-page tab. Selecting it does not navigate.

Page: home. Selector: `.w-tab-link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 592 x 174 | = |
| Padding | 16px | = |
| Border | 1px solid #ffffff | 1px solid #e4e6e9 |
| Radius | 24px | = |
| Background | transparent | #ffffff |
| Box shadow | none | = |
| Outline | none | = |
| Font | Arial 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Text node | p.text-2xl.u-semibold: Inter 20px/28px 500, #34363a | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 24 x 24, colour #34363a | = |
| Painted layers | a.tabs--card.w-inline-block 592.0x174.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 24px; div.token--solid 40.0x40.0 bg #34363a @ 0.05 r 8px; div.tab-timer-container 80.0x8.0 bg #e4e6e9 border T:1px solid #e4e6e9 / R:1px solid #e4e6e9 / B:1px solid #e4e6e9 / L:1px solid #e4e6e9 r 4px; div.tab-timer-bar.u-style-02 0.0x6.0 bg #2266ed r 4px | a.tabs--card.w-inline-block 592.0x174.0 bg #ffffff border T:1px solid #e4e6e9 / R:1px solid #e4e6e9 / B:1px solid #e4e6e9 / L:1px solid #e4e6e9 r 24px; div.token--solid 40.0x40.0 bg #34363a @ 0.05 r 8px; div.tab-timer-container 80.0x8.0 bg #e4e6e9 border T:1px solid #e4e6e9 / R:1px solid #e4e6e9 / B:1px solid #e4e6e9 / L:1px solid #e4e6e9 r 4px; div.tab-timer-bar.u-style-02 0.0x6.0 bg #2266ed r 4px |
| How | at rest | mouse hover |

Crops: `tab-default.png`, `tab-hover.png`.

#### card

Customer story card. A story card. Measured, not opened in this pass.

Page: home. Selector: `a[href^="/customers/"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 143.53 x 54 | = |
| Padding | 16px 24px | = |
| Border | 1px solid #e4e6e9 | 1px solid #cdd0d4 |
| Radius | 8px | = |
| Background | #f5f6f6 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 17.84px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #34363a | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | a.button-xl.s-secondary 143.5x54.0 bg #f5f6f6 border T:1px solid #e4e6e9 / R:1px solid #e4e6e9 / B:1px solid #e4e6e9 / L:1px solid #e4e6e9 r 8px | a.button-xl.s-secondary 143.5x54.0 bg #f5f6f6 image linear-gradient(#000000 @ 0.03, #000000 @ 0.03) border T:1px solid #cdd0d4 / R:1px solid #cdd0d4 / B:1px solid #cdd0d4 / L:1px solid #cdd0d4 r 8px |
| How | at rest | mouse hover |
| Background image | - | linear-gradient(#000000 @ 0.03, #000000 @ 0.03) |

Crops: `card-default.png`, `card-hover.png`.

### Pricing

#### pricing-title

Pricing title.

Page: pricing. Selector: `h1/h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 708.42 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tiempos Headline 56px/60px 400 |
| Letter spacing | normal |
| Colour | #34363a |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### plan-card

Plan card. A pricing plan column. Its CTA goes to the signup wall and is not followed.

Page: pricing. Selector: `pricing plan`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 401 x 422 |
| Padding | 32px |
| Gap | 32px |
| Border | 1px solid #e4e6e9 |
| Radius | 16px 0px 0px 16px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 14px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | p.heading-3xl: Inter 30px/36px 400, #34363a |
| Transition | none |
| Icon | 16 x 16, colour #333333 |
| Painted layers | div.flex-row--left-top.u-gap-8 401.0x422.0 border T:1px solid #e4e6e9 / R:1px solid #e4e6e9 / B:1px solid #e4e6e9 / L:1px solid #e4e6e9 r 16px 0px 0px 16px |
| How | at rest |

Crops: `plan-card-default.png`.

#### faq-question

FAQ question.

Page: pricing. Selector: `pricing FAQ`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 800 x 60 | = | = | = |
| Padding | 16px | 16px 16px 16px 24px | = | 16px 16px 16px 24px |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | 16px | = | 16px |
| Background | transparent | #f5f6f6 | = | #f5f6f6 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Arial 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | div.text-2xl.u-semibold: Inter 20px/28px 500, #34363a | = | = | = |
| Transition | padding 0.2s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #34363a | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | div.accordion--title.w-dropdown-toggle 800.0x60.0 bg #f5f6f6 r 16px | = | div.accordion--title.w-dropdown-toggle 800.0x60.0 bg #f5f6f6 r 16px |

Crops: `faq-question-default.png`, `faq-question-hover.png`, `faq-question-focus-visible.png`, `faq-question-pressed.png`.

#### faq-open

FAQ, open. The pricing FAQ after its own toggle.

Page: pricing. Selector: `pricing FAQ`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 800 x 60 |
| Padding | 16px 16px 16px 24px |
| Gap | 16px |
| Border | none |
| Radius | 16px |
| Background | #f5f6f6 |
| Box shadow | none |
| Outline | none |
| Font | Arial 14px/20px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | div.text-2xl.u-semibold: Inter 20px/28px 500, #34363a |
| Transition | padding 0.2s ease-in-out |
| Cursor | pointer |
| Icon | 33.94 x 33.94, colour #34363a |
| Painted layers | div.accordion--title.w-dropdown-toggle 800.0x60.0 bg #f5f6f6 r 16px |
| How | own toggle |

Crops: `faq-open-opened.png`.

### Docs

#### docs-title

Docs title.

Page: docs. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 45 |
| Padding | 0px |
| Gap | 18px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 36px/45px 700 |
| Letter spacing | -0.9px |
| Colour | #1d1d1e |
| Transition | none |
| How | at rest |

Crops: `docs-title-default.png`.

#### docs-search

Docs search. Focused only. Nothing typed, nothing submitted.

Page: docs. Selector: `input[name=search-input]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 337.77 x 37 | 379.77 x 37 |
| Padding | 8px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/21px 400 | = |
| Letter spacing | normal | = |
| Colour | #1d1d1e | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #6c6e71 @ 0.72, opacity 1 | = |
| Ancestor paint | 2 up div.group/input.relative bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #d7d9db @ 0.4 0px 1px 2px 0px | 2 up div.group/input.relative bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #b2cdff 0px 0px 0px 2px, #d2e7ff 0px 10px 15px -3px, #d2e7ff 0px 4px 6px -4px |
| How | at rest | clicked into the field |

Crops: `docs-search-default.png`, `docs-search-focused.png`.

### Footer

#### footer

Footer.

Page: home. Selector: `.is-footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 621 |
| Padding | 80px 32px |
| Gap | 16px |
| Border | T: 1px solid #34363a; R: none; B: none; L: none |
| Radius | 0px |
| Background | #050607 |
| Box shadow | none |
| Outline | none |
| Font | Arial 14px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.text-lg.u-semibold: Inter 16px/24px 500, #ffffff |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 16 x 16, colour #34363a |
| Painted layers | section.section--radius-8.neutral-1000 1440.0x621.0 bg #050607 border T:1px solid #34363a; div.flex-row--left-top.u-gap-2 0.0x0.0 bg #16171a border T:1px solid #34363a / R:1px solid #34363a / B:1px solid #34363a / L:1px solid #34363a r 12px |
| Ancestor paint | 1 up body.body bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a Features`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 65.52 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Arial 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2266ed | = | = | = |
| Text node | div.text-lg.text-color-d: Inter 16px/24px 400, #cdd0d4 | div.text-lg.text-color-d: Inter 16px/24px 400, #e4e6e9 | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.w-inline-block 65.5x24.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `.navbar.mobile-only`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 57 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 14px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | a.button-lg.s-ghost: Inter 14px/20px 400, #34363a |
| Transition | none |
| Icon | 120 x 30, colour #34363a |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | div.container.mw-80 390.0x57.0 bg #ffffff border B:1px solid #f5f6f6; a.button-lg.w-button 74.5x36.0 bg #2266ed r 8px; nav.menu-mobile-list.w-dropdown-list 0.0x0.0 bg #dddddd |
| Ancestor paint | 1 up body.body bg #ffffff |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button.

Page: home. Selector: `.menu-mobile-toggle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f5f6f6 | = | #f5f6f6 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Arial 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #34363a | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | div.menu-mobile-toggle.w-dropdown-toggle 40.0x40.0 bg #f5f6f6 r 8px | = | div.menu-mobile-toggle.w-dropdown-toggle 40.0x40.0 bg #f5f6f6 r 8px |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The phone menu after its own toggle.

Page: home. Selector: `.menu-mobile-toggle`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 40 x 40 |
| Padding | 8px |
| Gap | 8px |
| Border | none |
| Radius | 8px |
| Background | #f5f6f6 |
| Box shadow | none |
| Outline | none |
| Font | Arial 14px/20px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| Cursor | pointer |
| Icon | 0 x 0, colour #34363a |
| Painted layers | div.menu-mobile-toggle.w-dropdown-toggle 40.0x40.0 bg #f5f6f6 r 8px |
| How | own toggle |

Crops: `m-menu-open-opened.png`.

#### m-nav-link

Mobile nav link. Read inside the open menu.

Page: home. Selector: `nav link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 76.09 x 44 |
| Padding | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28px 500 |
| Letter spacing | normal |
| Colour | #34363a |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `m-nav-link-default.png`.

## Transitions declared in the readable stylesheets

Missive's marketing CSS is Webflow. This list holds transitions the CSSOM could read on each page. The per-state Transition rows above are computed values.

- home: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `background-color 0.5s`, `padding 0.2s ease-in-out`, `background-color 0.2s`, `opacity 0.3s`, `opacity 0.25s linear`
