# Component measurements

Computed styles read from riverside.com on 2026-11-20 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) in the site's one light theme (the cookie dialog was hidden, never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The Webflow top bar: logo, Platform, Solutions, Resources, For Business, Pricing, Login, Start for Free.

Page: home. Selector: `.w-nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 64 |
| Padding | 12px 12px 12px 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Instrument Sans 16px/24.8px 400 |
| Letter spacing | 0.16px |
| Colour | #1d1d1d |
| Text node | a.accessibility-menu-item: Instrument Sans 20px/32px 400, #ffffff, ls 0.16px |
| Transition | all 0.2s ease |
| Icon | 13 x 8, colour #1d1d1d |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | a.accessibility-menu-item 210.0x40.0 bg #000000; div.nav-dropdown-list-inner.is--product 1199.7x450.2 bg #ffffff r 8px shadow #242424 @ 0.08 0px 12px 16px -4px, #000000 @ 0.2 0px 4px 6px -2px; div.nav-links__list-item__icon.square 36.8x36.8 bg #9671ff @ 0.2 r 8px; div.nav-links__list-item__icon.square 36.8x36.8 bg #9671ff @ 0.2 r 8px; div.nav-links__list-item__icon.square 36.8x36.8 bg #9671ff @ 0.2 r 8px; div.nav-links__list-item__icon.square 36.8x36.8 bg #9671ff @ 0.2 r 8px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo.

Page: home. Selector: `a.w-nav-brand`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 134.73 x 23.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Instrument Sans 16px/24.8px 400 |
| Letter spacing | 0.16px |
| Colour | #333333 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### nav-dropdown

Nav dropdown. Platform toggle. Opens a menu already in the DOM. Measured, then closed.

Page: home. Selector: `.nav-dropdown-toggle--updated`. States: .

Not found on the page at capture time.

#### nav-menu

Platform menu. The opened Platform dropdown. Crop is the list.

Page: home. Selector: `.w-dropdown-list`. States: .

Not found on the page at capture time.

#### nav-link

Nav link.

Page: home. Selector: `a.c-nav-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 67.16 x 30 | = | = | = |
| Padding | 8px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Instrument Sans 14px/14px 500 | = | = | = |
| Letter spacing | 0.16px | = | = | = |
| Colour | #1d1d1d | #1d1d1d @ 0.6 | = | #1d1d1d @ 0.6 |
| Transition | all 0.25s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.c-nav-link.c-nav-link--default 67.2x30.0 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Login link. Header Login. Measured, never followed. It opens the studio wall.

Page: home. Selector: `a.c-nav-link--login`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 55.31 x 14 | = | = | = |
| Padding | 0px 9px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Instrument Sans 14px/14px 500 | = | = | = |
| Letter spacing | 0.16px | = | = | = |
| Colour | #1d1d1d | #1d1d1d @ 0.6 | = | #1d1d1d @ 0.6 |
| Transition | all 0.25s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.c-nav-link.c-nav-link--default 55.3x14.0 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-cta

Start for Free. Header CTA. Measured, never followed. It opens the register wall.

Page: home. Selector: `a.c-updated-nav-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 128 x 40 | = | = | = |
| Padding | 11px | = | = | = |
| Border | 1px solid #1d1d1d | = | = | = |
| Radius | 300px | = | = | = |
| Background | #1d1d1d | #000000 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Instrument Sans 14px/16px 500 | = | = | = |
| Letter spacing | 0.16px | = | = | = |
| Colour | #ffffff | = | = | #d2d2d2 |
| Transition | all 0.275s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.c-updated-nav-button.get-started-start 128.0x40.0 bg #1d1d1d border T:1px solid #1d1d1d / R:1px solid #1d1d1d / B:1px solid #1d1d1d / L:1px solid #1d1d1d r 300px | a.c-updated-nav-button.get-started-start 128.0x40.0 bg #000000 border T:1px solid #1d1d1d / R:1px solid #1d1d1d / B:1px solid #1d1d1d / L:1px solid #1d1d1d r 300px | a.c-updated-nav-button.get-started-start 128.0x40.0 bg #1d1d1d border T:1px solid #1d1d1d / R:1px solid #1d1d1d / B:1px solid #1d1d1d / L:1px solid #1d1d1d r 300px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### hero-title

Hero title.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 730 x 150 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sharp Grotesk 60px/75px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-cta

Hero CTA. The hero Start for Free. Measured, never followed.

Page: home. Selector: `a.main-button`. States: .

Not found on the page at capture time.

### Pricing

#### pricing-title

Pricing title.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 870 x 62.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sharp Grotesk 50px/62.5px 400 |
| Letter spacing | normal |
| Colour | #1d1d1d |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### plan-tab

Plan tab. The Pro pricing tab. A local UI state. Checkout was never opened.

Page: pricing. Selector: `[role=tab] Pro`. States: .

Not found on the page at capture time.

#### plan-card

Plan panel.

Page: pricing. Selector: `pricing panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 2282.83 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #f7f7f7 |
| Box shadow | none |
| Outline | none |
| Font | Instrument Sans 16px/24.8px 400 |
| Letter spacing | 0.16px |
| Colour | #1d1d1d |
| Text node | h1.pricing__title.is_v2: Sharp Grotesk 50px/62.5px 400, #1d1d1d |
| Transition | none |
| Icon | 9 x 7, colour #1d1d1d |
| Painted layers | div.pricing__wrapper.is--yearly 1440.0x2282.8 bg #f7f7f7; div.pricing__inner.is_v2 1440.0x1639.2 bg #f3f3f1; a.pricing__title-link 74.6x21.0 border B:1px solid #000000; div.c-price-abtest-price-inner.active-yearly 274.0x52.0 bg #ffffff r 10px; div.plan-test-navigator-round.navigator-absolute 129.0x40.0 bg #9671ff @ 0.3 r 6px; div.plan-test-navigator 0.0x0.0 bg #080705 r 20px |
| How | at rest |

Crops: `plan-card-default.png`.

### FAQ

#### faq-title

FAQ title.

Page: faq. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1380 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sharp Grotesk 32px/40px 700 |
| Letter spacing | normal |
| Colour | #181b21 |
| Text node | strong: Sharp Grotesk 32px/40px 500, #181b21 |
| Transition | none |
| Ancestor paint | 1 up div.c-faq-page-header bg #eef1fa |
| How | at rest |

Crops: `faq-title-default.png`.

### Blog

#### blog-title

Blog title.

Page: blog. Selector: `h1`. States: .

Not found on the page at capture time.

#### blog-card

Blog card. A published post card. Measured, never followed in this pass.

Page: blog. Selector: `a blog card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 671 x 80 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Instrument Sans 32px/40px 400 | = |
| Letter spacing | 0.16px | = |
| Colour | #151c22 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `blog-card-default.png`, `blog-card-hover.png`.

#### newsletter-field

Newsletter field. Focused only. Nothing typed. Nothing submitted.

Page: blog. Selector: `input[type=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 334 x 52 | = |
| Padding | 8px 24px | = |
| Border | 1px solid #e6e6e6 | 1px solid #7d7aff |
| Radius | 5px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Instrument Sans 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #1d1d1d | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #1d1d1d @ 0.6, opacity 1 | = |
| Painted layers | input.blog-subscribe-input.w-input 334.0x52.0 bg #ffffff border T:1px solid #e6e6e6 / R:1px solid #e6e6e6 / B:1px solid #e6e6e6 / L:1px solid #e6e6e6 r 5px | input.blog-subscribe-input.w-input 334.0x52.0 bg #ffffff border T:1px solid #7d7aff / R:1px solid #7d7aff / B:1px solid #7d7aff / L:1px solid #7d7aff r 5px |
| How | at rest | clicked into the field |

Crops: `newsletter-field-default.png`, `newsletter-field-focused.png`.

### Login wall

#### login-title

Login title.

Page: login. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 320 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sharp Grotesk Book 20px/28px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `login-title-default.png`.

#### login-email

Login email. Focused only. Nothing typed. Nothing submitted.

Page: login. Selector: `login email`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 320 x 40 | = |
| Padding | 8px 12px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #222222 | = |
| Box shadow | none | #b196ff 0px 0px 0px 1px inset |
| Outline | none | = |
| Font | Inter 14px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #fafafa | = |
| Transition | background-color 0.1s ease | = |
| Cursor | text | = |
| Placeholder | #888888, opacity 1 | = |
| Painted layers | input.input-q6h84o 320.0x40.0 bg #222222 r 8px | input.input-q6h84o 320.0x40.0 bg #222222 r 8px shadow #b196ff 0px 0px 0px 1px inset |
| How | at rest | clicked into the field |

Crops: `login-email-default.png`, `login-email-focused.png`.

#### login-password

Login password. Focused only. Nothing typed. Nothing submitted.

Page: login. Selector: `input[type=password]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 320 x 33 | = |
| Padding | 8px 0px 8px 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #fafafa | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #888888, opacity 1 | = |
| How | at rest | clicked into the field |
| Ancestor paint | - | 2 up div.wrapper-rBIkSf bg #2b2b2b shadow #b196ff 0px 0px 0px 1px inset |

Crops: `login-password-default.png`, `login-password-focused.png`.

#### login-sso

SSO button. Visible on the wall. Never clicked.

Page: login. Selector: `SSO`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 320 x 20 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #b196ff |
| Text node | span.root--v_1_202_0--hcxfpIUi.linkSmall--v_1_202_0--Mx9f3faz: Inter 12px/20px 700, #b196ff, ls 0.2px |
| Transition | none |
| Cursor | pointer |
| Icon | 20 x 20, colour #b196ff |
| How | at rest |

Crops: `login-sso-default.png`.

### Footer

#### footer-link

Footer legal link.

Page: home. Selector: `a Privacy`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 41.17 x 13 | = | = | = |
| Padding | 0px | = | = | = |
| Border | T: none; R: none; B: 1px solid #000000 @ 0; L: none | T: none; R: none; B: 1px solid #c7c7c7; L: none | = | T: none; R: none; B: 1px solid #c7c7c7 @ 0.6; L: none |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Instrument Sans 12px/12px 400 | = | = | = |
| Letter spacing | 0.16px | = | = | = |
| Colour | #c7c7c7 | = | = | #c7c7c7 @ 0.6 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.c-footer-link.c-footer-bottom_link 41.2x13.0 border B:1px solid #000000 @ 0 | a.c-footer-link.c-footer-bottom_link 41.2x13.0 border B:1px solid #c7c7c7 | a.c-footer-link.c-footer-bottom_link 41.2x13.0 border B:1px solid #000000 @ 0 outline 1px auto #005fcc offset 1px | a.c-footer-link.c-footer-bottom_link 41.2x13.0 border B:1px solid #c7c7c7 @ 0.6 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Footer social icon.

Page: home. Selector: `social link`. States: .

Not found on the page at capture time.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `.w-nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 60 |
| Padding | 14px 12px 14px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Instrument Sans 16px/24.8px 400 |
| Letter spacing | 0.16px |
| Colour | #1d1d1d |
| Text node | a.accessibility-menu-item: Instrument Sans 20px/32px 400, #ffffff, ls 0.16px |
| Transition | none |
| Icon | 0 x 0, colour #1d1d1d |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | a.accessibility-menu-item 210.0x40.0 bg #000000; nav.nav-menu-updated.w-nav-menu 0.0x0.0 bg #fafafa r 0px 0px 8px 8px; div.c-updated-nav-left.with-mobile 0.0x0.0 bg #ffffff; div.nav-dropdown.pr_8 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; div.nav-dropdown-toggle--updated.w-dropdown-toggle 0.0x0.0 border B:1px solid #1d1d1d @ 0.05; div.nav-dropdown-list-inner.is--product 0.0x0.0 bg #ffffff shadow #242424 @ 0.08 0px 12px 16px -4px, #000000 @ 0.2 0px 4px 6px -2px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button.

Page: home. Selector: `.w-nav-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 2px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Instrument Sans 24px/24.8px 400 | = | = | = |
| Letter spacing | 0.16px | = | = | = |
| Colour | #1d1d1d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 24px x 2px, static, bg #1d1d1d, radius 0px | = | = | = |
| ::after | 24px x 2px, static, bg #1d1d1d, radius 0px | = | = | = |
| Painted layers | div::before.menu-button._w-nav-button 24pxx2px bg #1d1d1d; div::after.menu-button._w-nav-button 24pxx2px bg #1d1d1d | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The hamburger after its own toggle.

Page: home. Selector: `.w-nav-button`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 32 x 32 |
| Padding | 2px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Instrument Sans 24px/24.8px 400 |
| Letter spacing | 0.16px |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| ::before | 20px x 2px, static, bg #1d1d1d, radius 10px |
| ::after | 20px x 2px, static, bg #1d1d1d, radius 10px |
| Painted layers | div::before.menu-button._w-nav-button 20pxx2px bg #1d1d1d r 10px; div::after.menu-button._w-nav-button 20pxx2px bg #1d1d1d r 10px |
| How | own toggle |

Crops: `m-menu-open-opened.png`.

#### m-nav-link

Mobile nav link. Read inside the open menu.

Page: home. Selector: `a Pricing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 46 |
| Padding | 16px 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Instrument Sans 14px/14px 500 |
| Letter spacing | 0.16px |
| Colour | #1d1d1d |
| Transition | all 0.25s ease |
| Cursor | pointer |
| How | at rest |

Crops: `m-nav-link-default.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- home: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `opacity 0.2s`, `0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55)`, `0.275s`, `0.25s`, `0.35s`, `0.325s`, `color 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55)`, `0.2s`, `opacity 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55)`
