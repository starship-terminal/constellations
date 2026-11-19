# Component measurements

Computed styles read from mailchimp.com on 2026-11-18 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Announcement bar

#### announce-bar

Announcement link. The trial announcement link above the nav ("Start today"). Measured, never followed. It points at pricing, not a signup submit.

Page: home. Selector: `announcement Start today`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 64.83 x 16 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px dashed #ffffff; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tally 13px/17.55px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| Painted layers | a 64.8x16.0 border B:1px dashed #ffffff |
| How | at rest |

Crops: `announce-bar-default.png`.

### Site chrome

#### site-nav

Site nav. The header (header.iaGlobalNav): wordmark, Industries and Solutions / Integrations / Resources menus, Pricing, Search, Log In, and the yellow Start Free Trial pill. The announcement strip above it is a separate aside.

Page: home. Selector: `header.iaGlobalNav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 68 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tally 16px/21.6px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | button.iaNav__cta: Tally 13px/14.3px 700, #231e15 |
| Transition | none |
| Icon | 0 x 0, colour #231e15, fill #000000 |
| Painted layers | section::after.iaNav__panel.panel__top 100%x100% shadow #000000 @ 0.16 4px 8px 32px 0px; div.iaNav__panelContentHolder 0.0x0.0 bg #ffffff; div::after.iaNav__panelContent.flex 1440pxx100% bg #f6f6f4; a::before.ctaArrow.cta--small autox32px bg #ffe01b r 16px; span.badge.badge--square 0.0x0.0 bg #231e15 r 4px shadow #000000 @ 0.13 0px 2px 4px 0px, #000000 @ 0.11 0px 0px 1px 0px; div.iaNav__panelContent__aux 0.0x0.0 bg #f6f6f4 |
| Ancestor paint | 1 up body.plums-migrate-svg-color-fills-currentcolor.funi-885-navattic-embed-experiment-variant-1 bg #ffffff |
| How | at rest |

Crops: `site-nav-default.png`.

#### nav-logo

Wordmark. The Mailchimp wordmark linking home.

Page: home. Selector: `a[aria-label=Mailchimp Home]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 162.45 x 46 |
| Padding | 0px |
| Border | none |
| Radius | 3px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tally 13px/14.3px 700 |
| Letter spacing | normal |
| Colour | #231e15 |
| Transition | background-color 0.15s ease |
| Cursor | pointer |
| How | at rest |

Crops: `nav-logo-default.png`.

#### nav-menu

Nav menu button. The Resources button (aria-haspopup) that opens the mega menu. The opened state was measured after clicking it. Menu links were never followed.

Page: home. Selector: `button.iaNav__cta Resources`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 101.3 x 30.3 | = | = | = | = |
| Padding | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 3px | = | = | = | = |
| Background | transparent | #231e15 @ 0.05 | #231e15 @ 0.05 | #231e15 @ 0.05 | #231e15 @ 0.05 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #4bc4c2 offset 2px | = | = |
| Font | Tally 13px/14.3px 700 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #231e15 | = | = | = | = |
| Transition | background-color 0.15s ease | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| ::after | 12px x 8px, static, bg #000000 @ 0 url(…), radius 0px | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | button.iaNav__cta 101.3x30.3 bg #231e15 @ 0.05 r 3px | button.iaNav__cta 101.3x30.3 bg #231e15 @ 0.05 r 3px outline 2px solid #4bc4c2 offset 2px | button.iaNav__cta 101.3x30.3 bg #231e15 @ 0.05 r 3px | button.iaNav__cta 101.3x30.3 bg #231e15 @ 0.05 r 3px |

Crops: `nav-menu-default.png`, `nav-menu-hover.png`, `nav-menu-focus-visible.png`, `nav-menu-pressed.png`, `nav-menu-opened.png`.

#### nav-panel

Nav menu panel. The panel opened by Resources (section.iaNav__panel.expanded). Its links were never followed.

Page: home. Selector: `section.iaNav__panel.expanded`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 507.5 |
| Padding | 0px 0px 80px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tally 16px/21.6px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.h5.margin--left-c2: Means Web 24px/31.9999px 400, #231e15 |
| Transition | opacity, -webkit-clip-path, clip-path 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s |
| ::after | 100% x 100%, absolute, bg #000000 @ 0, radius 0px, shadow #000000 @ 0.16 4px 8px 32px 0px |
| Painted layers | section::after.iaNav__panel.panel__top 100%x100% shadow #000000 @ 0.16 4px 8px 32px 0px; div.iaNav__panelContentHolder 1440.0x427.5 bg #ffffff; div::after.iaNav__panelContent.flex 1440pxx427.5px bg #f6f6f4; a::before.ctaArrow.cta--small 32pxx32px bg #ffe01b r 16px; div.iaNav__panelContent__aux 453.3x427.5 bg #f6f6f4 |
| How | at rest |

Crops: `nav-panel-default.png`.

#### nav-link

Nav link. The Pricing link in the nav. Measured, never followed.

Page: home. Selector: `a.iaNav__cta[href=/pricing/marketing/]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 58.95 x 30.3 | = | = | = |
| Padding | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 3px | = | = | = |
| Background | transparent | #231e15 @ 0.05 | #231e15 @ 0.05 | #231e15 @ 0.05 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4bc4c2 offset 2px | = |
| Font | Tally 13px/14.3px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #231e15 | = | = | = |
| Transition | background-color 0.15s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.iaNav__cta 59.0x30.3 bg #231e15 @ 0.05 r 3px | a.iaNav__cta 59.0x30.3 bg #231e15 @ 0.05 r 3px outline 2px solid #4bc4c2 offset 2px | a.iaNav__cta 59.0x30.3 bg #231e15 @ 0.05 r 3px |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Log In. The outlined Log In pill. It points at login.mailchimp.com. Measured, never followed.

Page: home. Selector: `a.ctaSecondary Log In`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.56 x 43.5 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 26px | = | = | = |
| Background | #231e15 @ 0 | = | = | = |
| Box shadow | #231e15 0px 0px 0px 1px | #231e15 0px 0px 0px 1px, #231e15 0px 4.875px 0px 0px | #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px | #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px |
| Outline | none | = | = | = |
| Font | Tally 13px/19.5px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #231e15 | = | = | = |
| Transition | transform, box-shadow 0.3s, 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7), cubic-bezier(0.5, 2.5, 0.7, 0.7) delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | matrix(1, 0, 0, 1, 0, -4.875) | matrix(1, 0, 0, 1, 0, -1.625) | matrix(1, 0, 0, 1, 0, -1.625) |
| Cursor | pointer | = | = | = |
| ::before | 85.5625px x 43.5px, absolute, bg #000000 @ 0, radius 26px | = | = | = |
| Painted layers | a.ctaSecondary 85.6x43.5 bg #231e15 @ 0 r 26px shadow #231e15 0px 0px 0px 1px | a.ctaSecondary 85.6x43.5 bg #231e15 @ 0 r 26px shadow #231e15 0px 0px 0px 1px, #231e15 0px 4.875px 0px 0px | a.ctaSecondary 85.6x43.5 bg #231e15 @ 0 r 26px shadow #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px; a::after.ctaSecondary 85.5625pxx45.125px r 26px outline 2px solid #4bc4c2 offset 3.25px | a.ctaSecondary 85.6x43.5 bg #231e15 @ 0 r 26px shadow #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| ::after | - | = | 85.5625px x 45.125px, absolute, bg #000000 @ 0, radius 26px | = |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-trial

Start Free Trial. The yellow Start Free Trial pill. Measured, never followed. Signup was not started.

Page: home. Selector: `a.ctaPrimary Start Free Trial`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140.36 x 43.5 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 26px | = | = | = |
| Background | #ffe01b | = | = | = |
| Box shadow | #231e15 0px 0px 0px 1px | #231e15 0px 0px 0px 1px, #231e15 0px 4.875px 0px 0px | #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px | #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px |
| Outline | none | = | = | = |
| Font | Tally 13px/19.5px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #231e15 | = | = | = |
| Transition | transform, box-shadow 0.3s, 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7), cubic-bezier(0.5, 2.5, 0.7, 0.7) delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | matrix(1, 0, 0, 1, 0, -4.875) | matrix(1, 0, 0, 1, 0, -1.625) | matrix(1, 0, 0, 1, 0, -1.625) |
| Cursor | pointer | = | = | = |
| ::before | 140.359px x 43.5px, absolute, bg #000000 @ 0, radius 26px | = | = | = |
| Painted layers | a.ctaPrimary.gse_signup_experiment_button 140.4x43.5 bg #ffe01b r 26px shadow #231e15 0px 0px 0px 1px | a.ctaPrimary.gse_signup_experiment_button 140.4x43.5 bg #ffe01b r 26px shadow #231e15 0px 0px 0px 1px, #231e15 0px 4.875px 0px 0px | a.ctaPrimary.gse_signup_experiment_button 140.4x43.5 bg #ffe01b r 26px shadow #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px; a::after.ctaPrimary.gse_signup_experiment_button 140.359pxx45.125px r 26px outline 2px solid #4bc4c2 offset 3.25px | a.ctaPrimary.gse_signup_experiment_button 140.4x43.5 bg #ffe01b r 26px shadow #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| ::after | - | = | 140.359px x 45.125px, absolute, bg #000000 @ 0, radius 26px | = |

Crops: `nav-trial-default.png`, `nav-trial-hover.png`, `nav-trial-focus-visible.png`, `nav-trial-pressed.png`.

### Home

#### hero-h1

Hero headline. The home masthead, set in Means Web on the dark hero.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 960 x 153.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Means Web 64px/76.8px 400 |
| Letter spacing | -1.2px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-cta

Hero CTA. The hero Start Free Trial button. It points at pricing. Measured, never followed.

Page: home. Selector: `a.ctaPrimary[aria-label=Start Free Trial]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 343 x 48 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | #ffe01b | = | = | = |
| Box shadow | #231e15 0px 0px 0px 1px | #231e15 0px 0px 0px 1px, #231e15 0px 5.625px 0px 0px | #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px | #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px |
| Outline | none | = | = | = |
| Font | Tally 15px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #231e15 | = | = | = |
| Transition | transform, box-shadow 0.3s, 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7), cubic-bezier(0.5, 2.5, 0.7, 0.7) delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | matrix(1, 0, 0, 1, 0, -5.625) | matrix(1, 0, 0, 1, 0, -1.625) | matrix(1, 0, 0, 1, 0, -1.625) |
| Cursor | pointer | = | = | = |
| ::before | 343px x 48px, absolute, bg #000000 @ 0, radius 30px | = | = | = |
| Painted layers | a.ctaPrimary 343.0x48.0 bg #ffe01b r 40px shadow #231e15 0px 0px 0px 1px | a.ctaPrimary 343.0x48.0 bg #ffe01b r 40px shadow #231e15 0px 0px 0px 1px, #231e15 0px 5.625px 0px 0px | a.ctaPrimary 343.0x48.0 bg #ffe01b r 40px shadow #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px; a::after.ctaPrimary 343pxx49.625px r 30px outline 2px solid #4bc4c2 offset 3.25px | a.ctaPrimary 343.0x48.0 bg #ffe01b r 40px shadow #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| ::after | - | = | 343px x 49.625px, absolute, bg #000000 @ 0, radius 30px | = |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-secondary

See all demos. The hero secondary link under the photo band. Measured, never followed.

Page: home. Selector: `a.ctaArrow See all demos`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 136.72 x 32 | = | = | = |
| Padding | 0px 40px 0px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Tally 16px/32px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #231e15 | = | #231e15 |
| Transition | color, transform 0.15s, 0.3s ease-in-out, ease delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | matrix(1, 0, 0, 1, 4, 0) | = | matrix(1, 0, 0, 1, 4, 0) |
| Cursor | pointer | = | = | = |
| ::before | 32px x 32px, absolute, bg #ffe01b url(…), radius 16px | 152.719px x 32px, absolute, bg #ffe01b url(…), radius 16px | 152.719px x 32px, absolute, bg #ffe01b url(…), radius 16px | 152.719px x 32px, absolute, bg #ffe01b url(…), radius 16px |
| Painted layers | a::before.ctaArrow 32pxx32px bg #ffe01b r 16px | a::before.ctaArrow 152.719pxx32px bg #ffe01b r 16px | a::before.ctaArrow 152.719pxx32px bg #ffe01b r 16px; a::after.ctaArrow 152.719pxx32px r 16px outline 2px solid #4bc4c2 offset 2.5px | a::before.ctaArrow 152.719pxx32px bg #ffe01b r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| ::after | - | = | 152.719px x 32px, absolute, bg #000000 @ 0, radius 16px | = |

Crops: `hero-secondary-default.png`, `hero-secondary-hover.png`, `hero-secondary-focus-visible.png`, `hero-secondary-pressed.png`.

### Footer

#### footer

Footer. The page footer: sitemap columns and legal links.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1041.78 |
| Padding | 60px 0px |
| Border | none |
| Radius | 0px |
| Background | #e7b75f |
| Box shadow | none |
| Outline | none |
| Font | Tally 16px/21.6px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p: Tally 16px/24px 400, #231e15 |
| Transition | none |
| Painted layers | footer.globalFooter__storefront.layout--halfMargin 1440.0x1041.8 bg #e7b75f; hr.margin--vertical-6 1440.0x1.0 bg #231e15 @ 0.3; hr.hr.margin--vertical-3 1440.0x1.0 bg #231e15 @ 0.3; div.formSelect.formSelect--small-secondary 203.0x40.7 border T:1px solid #231e15 / R:1px solid #231e15 / B:1px solid #231e15 / L:1px solid #231e15 |
| Ancestor paint | 1 up body.plums-migrate-svg-color-fills-currentcolor.funi-885-navattic-embed-experiment-variant-1 bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer sitemap link. Measured, never followed.

Page: home. Selector: `footer a.cta[href=/why-mailchimp/]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 90.34 x 15 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #ffe01b @ 0.65 | #ffe01b @ 0.65 | #ffe01b @ 0.65 |
| Box shadow | none | #ffe01b @ 0.65 0px 0px 0px 3.25px | #ffe01b @ 0.65 0px 0px 0px 3.25px | #ffe01b @ 0.65 0px 0px 0px 3.25px |
| Outline | none | = | 2px solid #4bc4c2 offset 6.5px | = |
| Font | Tally 13px/17.55px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #231e15 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.cta 90.3x15.0 bg #ffe01b @ 0.65 shadow #ffe01b @ 0.65 0px 0px 0px 3.25px | a.cta 90.3x15.0 bg #ffe01b @ 0.65 shadow #ffe01b @ 0.65 0px 0px 0px 3.25px outline 2px solid #4bc4c2 offset 6.5px | a.cta 90.3x15.0 bg #ffe01b @ 0.65 shadow #ffe01b @ 0.65 0px 0px 0px 3.25px |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Pricing

#### price-plan

Plan card. The Standard plan card on /pricing/marketing/. The trial link was measured, never followed. Checkout was not started.

Page: pricing. Selector: `.singlePlan__planCardCell`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 370 x 508.25 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tally 16px/21.6px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.h2.margin--bottom-3: Means Web 40px/40px 400, #000000, ls -0.5px |
| Transition | none |
| Icon | 0 x 0, colour #000000, fill #241c15 @ 0.65 |
| Painted layers | div.singlePlanCard.backgroundWhite 370.0x472.3 bg #ffffff shadow #231e15 @ 0.15 0px 0px 20px 3px; form.flex.flex--middle 338.0x47.0 border T:1px solid #231e15 @ 0.3 / R:1px solid #231e15 @ 0.3 / B:1px solid #231e15 @ 0.3 / L:1px solid #231e15 @ 0.3 r 10px; div.formSelect 224.0x44.0 bg #ffffff r 10px; div.card 338.0x102.3 bg #ffffff border T:1px solid #bcbab6 / R:1px solid #bcbab6 / B:1px solid #bcbab6 / L:1px solid #bcbab6 r 10px; div.card.card--closed 338.0x38.0 bg #f5f5f5 border T:1px solid #bcbab6 / R:1px solid #bcbab6 / B:1px solid #bcbab6 / L:1px solid #bcbab6 r 10px; a.ctaBuyNow.ctaPrimary 338.0x43.5 bg #ffe01b r 26px shadow #231e15 0px 0px 0px 1px |
| How | at rest |

Crops: `price-plan-default.png`.

#### price-cta

Plan trial button. The Standard plan Start Free Trial link. It points at /signup/ with a plan query. Measured, never followed. Signup was not started and checkout was not started.

Page: pricing. Selector: `.singlePlan__planCardCell a.ctaBuyNow`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 338 x 43.5 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 26px | = | = | = |
| Background | #ffe01b | = | = | = |
| Box shadow | #231e15 0px 0px 0px 1px | #231e15 0px 0px 0px 1px, #231e15 0px 4.875px 0px 0px | #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px | #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px |
| Outline | none | = | = | = |
| Font | Tally 13px/19.5px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #231e15 | = | = | = |
| Text node | span.desktop: Tally 13px/19.5px 700, #231e15 | = | = | = |
| Transition | transform, box-shadow 0.3s, 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7), cubic-bezier(0.5, 2.5, 0.7, 0.7) delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | matrix(1, 0, 0, 1, 0, -4.875) | matrix(1, 0, 0, 1, 0, -1.625) | matrix(1, 0, 0, 1, 0, -1.625) |
| Cursor | pointer | = | = | = |
| ::before | 338px x 43.5px, absolute, bg #000000 @ 0, radius 26px | = | = | = |
| Painted layers | a.ctaBuyNow.ctaPrimary 338.0x43.5 bg #ffe01b r 26px shadow #231e15 0px 0px 0px 1px | a.ctaBuyNow.ctaPrimary 338.0x43.5 bg #ffe01b r 26px shadow #231e15 0px 0px 0px 1px, #231e15 0px 4.875px 0px 0px | a.ctaBuyNow.ctaPrimary 338.0x43.5 bg #ffe01b r 26px shadow #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px; a::after.ctaBuyNow.ctaPrimary 338pxx45.125px r 26px outline 2px solid #4bc4c2 offset 3.25px | a.ctaBuyNow.ctaPrimary 338.0x43.5 bg #ffe01b r 26px shadow #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| ::after | - | = | 338px x 45.125px, absolute, bg #000000 @ 0, radius 26px | = |

Crops: `price-cta-default.png`, `price-cta-hover.png`, `price-cta-focus-visible.png`, `price-cta-pressed.png`.

#### price-select

Contacts select. The contacts-count select on the pricing page. Measured at rest. The value was not changed and nothing was submitted.

Page: pricing. Selector: `select[name=Number of Contacts]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 214 x 44 |
| Padding | 8px 48px 8px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Means Web 18px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 1 up div.formSelect bg #ffffff |
| How | at rest |

Crops: `price-select-default.png`.

#### price-radio

Plan radio. A trial-or-discount radio on a plan card. Measured at rest, never changed.

Page: pricing. Selector: `input.av-radio`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 20 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tally 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | default |
| Placeholder | #000000, opacity 1 |
| How | at rest |

Crops: `price-radio-default.png`.

### Features

#### feat-h1

Features headline. The /features/ masthead.

Page: features. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 853.33 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Means Web 48px/48px 400 |
| Letter spacing | -1px |
| Colour | #231e15 |
| Transition | none |
| How | at rest |

Crops: `feat-h1-default.png`.

### About

#### about-h1

About headline. The /about/ masthead. A public page that loads signed out.

Page: about. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 365.89 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Means Web 48px/48px 400 |
| Letter spacing | -1px |
| Colour | #231e15 |
| Transition | none |
| How | at rest |

Crops: `about-h1-default.png`.

### App log-in

#### login-panel

Log-in card. The signed-out log-in card on login.mailchimp.com. A separate app from the marketing site. Nothing was submitted. Sign-in was not started.

Page: login. Selector: `#unified-login-form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 422 x 453 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik Web 16px/24px 500 |
| Letter spacing | normal |
| Colour | #21262a |
| Text node | h1.text-align--center.!margin-bottom--lv3: Graphik Web 20px/22px 500, #21262a, ls -0.4px |
| Transition | none |
| Painted layers | a 140.2x20.0 border B:1px solid #017e89; input.rounded-corners-4.av-text 422.0x46.0 bg #ffffff border T:1px solid #c3ced5 / R:1px solid #c3ced5 / B:1px solid #c3ced5 / L:1px solid #c3ced5 r 4px; button.identifier-first-login-btn.button-wide 422.0x36.0 bg #017e89 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; a 138.0x20.0 border B:1px solid #017e89; a 136.0x20.0 border B:1px solid #017e89; div.bottom-panel 422.0x107.0 border T:1px solid #dbd9d2 |
| How | at rest |

Crops: `login-panel-default.png`.

#### login-username

Username field. The Username or Email field. Focused and typed into with a placeholder, then cleared. Nothing was submitted.

Page: login. Selector: `#username`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 422 x 46 | = | = |
| Padding | 0px 15px | = | = |
| Border | 1px solid #c3ced5 | 1px solid #007c89 | 1px solid #007c89 |
| Radius | 4px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #007c89 0px 0px 0px 1px inset | #007c89 0px 0px 0px 1px inset |
| Outline | none | = | = |
| Font | Graphik Web 17px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #21262a | = | = |
| Transition | all 0.2s ease-in-out | = | = |
| Cursor | text | = | = |
| Placeholder | #21262a, opacity 1 | = | = |
| Painted layers | input.rounded-corners-4.av-text 422.0x46.0 bg #ffffff border T:1px solid #c3ced5 / R:1px solid #c3ced5 / B:1px solid #c3ced5 / L:1px solid #c3ced5 r 4px | input.rounded-corners-4.av-text 422.0x46.0 bg #ffffff border T:1px solid #007c89 / R:1px solid #007c89 / B:1px solid #007c89 / L:1px solid #007c89 r 4px shadow #007c89 0px 0px 0px 1px inset | input.rounded-corners-4.av-text 422.0x46.0 bg #ffffff border T:1px solid #007c89 / R:1px solid #007c89 / B:1px solid #007c89 / L:1px solid #007c89 r 4px shadow #007c89 0px 0px 0px 1px inset |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-username-default.png`, `login-username-focused.png`, `login-username-filled.png`.

#### login-submit

Log in submit. The Log in submit. States were measured. The button was never clicked. Sign-in was not started.

Page: login. Selector: `login submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 422 x 36 | = | = | = |
| Padding | 0px 42px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #017e89 | #006771 | = | #006771 |
| Box shadow | none | = | #017e89 0px 0px 0px 1px inset | = |
| Outline | none | = | = | = |
| Font | Graphik Web 14px/34px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, opacity 0.2s, 0.2s ease-in-out, ease-in-out delay 0s, 0s | = | = | = |
| Cursor | default | pointer | = | pointer |
| Painted layers | button.identifier-first-login-btn.button-wide 422.0x36.0 bg #017e89 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.identifier-first-login-btn.button-wide 422.0x36.0 bg #006771 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.identifier-first-login-btn.button-wide 422.0x36.0 bg #017e89 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px shadow #017e89 0px 0px 0px 1px inset | button.identifier-first-login-btn.button-wide 422.0x36.0 bg #006771 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-focus-visible.png`, `login-submit-pressed.png`.

#### login-forgot

Forgot username. A forgot-username or forgot-password link. Measured, never followed.

Page: login. Selector: `forgot link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | T: none; R: none; B: 1px solid #017e89; L: none | T: none; R: none; B: 1px solid #004e56; L: none | = | T: none; R: none; B: 1px solid #004e56; L: none |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Graphik Web 16px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #017e89 | #004e56 | = | #004e56 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a 138.0x20.0 border B:1px solid #017e89 | a 138.0x20.0 border B:1px solid #004e56 | a 138.0x20.0 border B:1px solid #017e89 outline 1px auto #005fcc offset 1px | a 138.0x20.0 border B:1px solid #004e56 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-forgot-default.png`, `login-forgot-hover.png`, `login-forgot-focus-visible.png`, `login-forgot-pressed.png`.

#### login-create

Create an account. The Create an account link. Signup was not started and was not followed.

Page: login. Selector: `Create an account`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140.17 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | T: none; R: none; B: 1px solid #017e89; L: none | T: none; R: none; B: 1px solid #004e56; L: none | = | T: none; R: none; B: 1px solid #004e56; L: none |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Graphik Web 16px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #017e89 | #004e56 | = | #004e56 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a 140.2x20.0 border B:1px solid #017e89 | a 140.2x20.0 border B:1px solid #004e56 | a 140.2x20.0 border B:1px solid #017e89 outline 1px auto #005fcc offset 1px | a 140.2x20.0 border B:1px solid #004e56 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-create-default.png`, `login-create-hover.png`, `login-create-focus-visible.png`, `login-create-pressed.png`.

### Mobile (390 wide)

#### m-nav

Mobile nav. The phone nav bar.

Page: mobile. Selector: `mobile .iaNav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tally 16px/21.6px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.ctaPrimary.iaNav__cta__longerTextCtaForMobile: Tally 13px/19.5px 700, #231e15 |
| Transition | none |
| Icon | 0 x 0, colour #231e15, fill #000000 |
| Painted layers | nav.iaNav__nav 390.0x60.0 bg #ffffff; section::after.iaNav__panel.panel__top 100%x100% shadow #000000 @ 0.16 4px 8px 32px 0px; div.iaNav__panelContentHolder 0.0x0.0 bg #ffffff; div::after.iaNav__panelContent.flex 390pxx100% bg #f6f6f4; a::before.ctaArrow.cta--small autox32px bg #ffe01b r 16px; span.badge.badge--square 0.0x0.0 bg #231e15 r 4px shadow #000000 @ 0.13 0px 2px 4px 0px, #000000 @ 0.11 0px 0px 1px 0px |
| Ancestor paint | 1 up body.plums-migrate-svg-color-fills-currentcolor.funi-885-navattic-embed-experiment-variant-1 bg #ffffff |
| How | at rest |

Crops: `m-nav-default.png`.

#### m-menu

Mobile menu button. The Main Menu button. Opened locally. Links were never followed.

Page: mobile. Selector: `button.iaNav__menuOpen`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 46 x 39.3 | = | = | = | = |
| Padding | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 3px | = | = | = | = |
| Background | transparent | #231e15 @ 0.05 | #231e15 @ 0.05 | #231e15 @ 0.05 | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #4bc4c2 offset 2px | = | = |
| Font | Tally 13px/14.3px 700 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #231e15 | = | = | = | = |
| Transition | background-color 0.15s ease | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| ::before | 30px x 20px, static, bg #000000 @ 0 url(…), radius 0px | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | button.iaNav__menuOpen.iaNav__cta 46.0x39.3 bg #231e15 @ 0.05 r 3px | button.iaNav__menuOpen.iaNav__cta 46.0x39.3 bg #231e15 @ 0.05 r 3px outline 2px solid #4bc4c2 offset 2px | button.iaNav__menuOpen.iaNav__cta 46.0x39.3 bg #231e15 @ 0.05 r 3px | = |

Crops: `m-menu-default.png`, `m-menu-hover.png`, `m-menu-focus-visible.png`, `m-menu-pressed.png`, `m-menu-opened.png`.

#### m-hero

Mobile hero. The home masthead at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 343 x 93.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Means Web 36px/46.8px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

Mailchimp's Plums/CXP sheets are same-origin, so this list is what the CSSOM could read on each page. The per-state Transition rows above are computed values.

- features: `transform 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7), box-shadow 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7)`, `bottom 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7)`, `transform 0.4s, box-shadow 0.4s`, `0.15s linear`, `color 0.15s ease-in-out, transform 0.3s`, `left 0.3s cubic-bezier(0.34, 1.2, 0.64, 1), right 0.3s, background-position 0.3s`, `right 0.3s, background-position 0.3s`, `background 0.4s, padding-left 0.4s, transform 0.4s`, `background 0.4s, padding-left, transform`, `left 0.2s, right 0.3s, background-position 0.3s`, `right 0.3s cubic-bezier(0.34, 1.2, 0.64, 1), left 0.3s, background-position 0.3s`, `left 0.3s, background-position 0.3s`

- home: `transform 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7), box-shadow 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7)`, `bottom 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7)`, `transform 0.4s, box-shadow 0.4s`, `0.15s linear`, `color 0.15s ease-in-out, transform 0.3s`, `left 0.3s cubic-bezier(0.34, 1.2, 0.64, 1), right 0.3s, background-position 0.3s`, `right 0.3s, background-position 0.3s`, `background 0.4s, padding-left 0.4s, transform 0.4s`, `background 0.4s, padding-left, transform`, `left 0.2s, right 0.3s, background-position 0.3s`, `right 0.3s cubic-bezier(0.34, 1.2, 0.64, 1), left 0.3s, background-position 0.3s`, `left 0.3s, background-position 0.3s`

- login: `0.1s`, `300ms ease-in`, `none`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `0.2s`, `0.25s ease-out`, `0.1s ease-in`

- pricing: `transform 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7), box-shadow 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7)`, `bottom 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7)`, `transform 0.4s, box-shadow 0.4s`, `0.15s linear`, `color 0.15s ease-in-out, transform 0.3s`, `left 0.3s cubic-bezier(0.34, 1.2, 0.64, 1), right 0.3s, background-position 0.3s`, `right 0.3s, background-position 0.3s`, `background 0.4s, padding-left 0.4s, transform 0.4s`, `background 0.4s, padding-left, transform`, `left 0.2s, right 0.3s, background-position 0.3s`, `right 0.3s cubic-bezier(0.34, 1.2, 0.64, 1), left 0.3s, background-position 0.3s`, `left 0.3s, background-position 0.3s`
