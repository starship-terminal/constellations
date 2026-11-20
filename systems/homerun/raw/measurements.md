# Component measurements

Computed styles read from www.homerun.co, jobs.homerun.co and the app.homerun.co / app.homerun.hr sign-in cards on 2026-11-17 by `tools/capture/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Nav bar. The sticky 1440 top nav (position:sticky): logo, product pills, dropdown menus, Log-in/Book-a-demo/Start-free-trial actions.

Page: home. Selector: `.nav-new.is-desktop`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 104 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | GT America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #4a3e3e |
| Text node | div: GT America 16px/22px 400, #4a3e3e |
| Transition | none |
| Icon | 42 x 28, colour #4a3e3e |
| Painted layers | div.nav-primary.is-new 1440.0x104.0 bg #ffffff; div.nav-primary.is-new 1440.0x104.0 bg #ffffff; div.nav-new.is-v2 1440.0x104.0 bg #ffffff r 60px; div.mobilenav-bar-menu-icon-v2.new 0.0x0.0 bg #ffffff @ 0 image linear-gradient(#ffffff, #ffffff) r 8px 0px 0px 8px; div.nav-line 0.0x0.0 bg #2d2323; div.nav-line 0.0x0.0 bg #2d2323 |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The HOMERUN logotype anchor (wordmark image).

Page: home. Selector: `a.new-nav_brand`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 126 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link. A text nav link (Pricing) in the top bar.

Page: home. Selector: `a.nav_link-new`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 74 x 58 | = | = | = |
| Padding | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | #f5f3ef | = | #f5f3ef |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | GT America 16px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #4a3e3e | = | = | = |
| Transition | background-color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.nav_link-new.w-nav-link 74.0x58.0 bg #f5f3ef r 10px | a.nav_link-new.w-nav-link 74.0x58.0 r 10px outline 1px auto #101010 offset 1px | a.nav_link-new.w-nav-link 74.0x58.0 bg #f5f3ef r 10px |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-product-pill

Nav product pill. The "ATS Organise your hiring" pill — an icon-bearing product link that tints its icon on hover.

Page: home. Selector: `a.nav_link-new.is-icon[data-nav-menu]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 221 x 58 | = | = | = |
| Padding | 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | #f5f3ef | = | #f5f3ef |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | GT America 16px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #4a3e3e | = | = | = |
| Text node | div: GT America 16px/22px 400, #4a3e3e | = | = | = |
| Transition | background-color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 42 x 28, colour #4a3e3e | 42 x 28, colour #4f75fe | = | 42 x 28, colour #4f75fe |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.nav_link-new.is-icon 221.0x58.0 bg #f5f3ef r 10px | a.nav_link-new.is-icon 221.0x58.0 r 10px outline 1px auto #101010 offset 1px | a.nav_link-new.is-icon 221.0x58.0 bg #f5f3ef r 10px |

Crops: `nav-product-pill-default.png`, `nav-product-pill-hover.png`, `nav-product-pill-focus-visible.png`, `nav-product-pill-pressed.png`.

#### nav-resources

Resources dropdown. The Resources nav dropdown trigger — a hover-open w-dropdown whose panel links Blog/Guides/Templates/Integrations/Help center and Product updates/Careers/Refer/About.

Page: home. Selector: `.nav_link-new.is-dropdown-v2 .w-dropdown-toggle`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 121 x 58 | = | = |
| Padding | 0px 12px 0px 0px | = | = |
| Gap | 4px | = | = |
| Border | none | = | = |
| Radius | 10px | = | = |
| Background | transparent | #f5f3ef | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | GT America 16px/22px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #222222 | = | = |
| Text node | div.nav_link-new.is-dropdown-text: GT America 16px/22px 400, #4a3e3e | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 12 x 13, colour #8a7878 | = | = |
| How | at rest | mouse hover | menu held open by opts.open |
| Painted layers | - | div.dropdown_toggle.is-new-nav 121.0x58.0 bg #f5f3ef r 10px; div.nav_link-new.is-dropdown-text 93.0x58.0 bg #f5f3ef @ 0 r 10px | = |

Crops: `nav-resources-default.png`, `nav-resources-hover.png`, `nav-resources-opened.png`.

#### nav-resources-panel

Resources panel. The open Resources mega-panel (nav_resources-update): two link columns, rounded + shadowed card.

Page: home. Selector: `.nav_dropdown-list-v2.resources`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 436 x 240 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #dddddd @ 0 |
| Box shadow | none |
| Outline | none |
| Font | GT America 16px/22px 400 |
| Letter spacing | normal |
| Colour | #4a3e3e |
| Text node | div.nav_resources-text: GT America 16px/18px 400, #131313 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, -281.6, 0) |
| Icon | 24 x 24, colour #4f75fe |
| Painted layers | nav.nav_dropdown-list-v2.resources 436.0x240.0 bg #dddddd @ 0; div.nav_resources-update 436.0x240.0 bg #ffffff r 28px shadow #43413d @ 0.15 0px 5px 20px 0px |
| How | at rest |

Crops: `nav-resources-panel-default.png`.

#### nav-resources-link

Resources link. A link row inside the open Resources panel; focus/pressed are unreachable while the panel is hover-held.

Page: home. Selector: `a.nav_resources-link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 186 x 40 | = |
| Padding | 8px | = |
| Gap | 16px | = |
| Border | none | = |
| Radius | 0px | 12px |
| Background | transparent | #f5f3ef |
| Box shadow | none | = |
| Outline | none | = |
| Font | GT America 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #4f75fe | = |
| Text node | div.nav_resources-text: GT America 16px/18px 400, #131313 | = |
| Transition | all 0.3s ease | = |
| Cursor | pointer | = |
| Icon | 24 x 24, colour #4f75fe | = |
| Ancestor paint | 2 up div.nav_resources-update bg #ffffff shadow #43413d @ 0.15 0px 5px 20px 0px | = |
| How | at rest | mouse hover |
| Painted layers | - | a.nav_resources-link.is-order-1 186.0x40.0 bg #f5f3ef r 12px |

Crops: `nav-resources-link-default.png`, `nav-resources-link-hover.png`.

#### nav-login

Log-in dropdown. The "Log in" ghost-button dropdown — opens the ATS/HR sign-in menu on hover.

Page: home. Selector: `.nav_cta-dropdown .w-dropdown-toggle`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 78 x 42 | = | = |
| Padding | 4px 16px | = | = |
| Border | 1px solid #edebe7 | = | = |
| Radius | 12px | = | = |
| Background | transparent | #e8e5de | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | GT America 16px/32px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #4a3e3e | = | = |
| Text node | div: GT America 16px/32px 400, #4a3e3e | = | = |
| Transition | background-color 0.3s ease | = | = |
| Cursor | pointer | = | = |
| Painted layers | div.btn-secondary_new.is-tablet-custom 78.0x42.0 border T:1px solid #edebe7 / R:1px solid #edebe7 / B:1px solid #edebe7 / L:1px solid #edebe7 r 12px | div.btn-secondary_new.is-tablet-custom 78.0x42.0 bg #e8e5de border T:1px solid #edebe7 / R:1px solid #edebe7 / B:1px solid #edebe7 / L:1px solid #edebe7 r 12px | = |
| How | at rest | mouse hover | menu held open by opts.open |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-opened.png`.

#### nav-login-panel

Log-in panel. The open Log-in menu: "ATS Organise your hiring" and "HR Manage your team" sign-in links, measured never followed.

Page: home. Selector: `.nav_cta-dropdown-list-outer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 234 x 138 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #4a3e3e |
| Text node | div: GT America 16px/22px 400, #2d2323 |
| Transition | none |
| Icon | 43.74 x 30.12, colour #4f75fe |
| Painted layers | div.nav_cta-dropdown-list.is-new 234.0x130.0 bg #ffffff r 20px shadow #43413d @ 0.15 0px 5px 20px 0px; a.nav-cta_dropdown-link.w-inline-block 218.0x57.0 bg #f5f3ef r 10px |
| How | at rest |

Crops: `nav-login-panel-default.png`.

#### nav-login-link

Log-in menu link. A sign-in link inside the open Log-in menu (to app.homerun.co/login); measured never followed.

Page: home. Selector: `.nav_cta-dropdown a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 218 x 57 | = |
| Padding | 14px 8px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 10px | = |
| Background | #f5f3ef | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | GT America 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #2d2323 | = |
| Text node | div: GT America 16px/22px 400, #2d2323 | = |
| Transition | background-color 0.3s ease | = |
| Cursor | pointer | = |
| Icon | 43.74 x 30.12, colour #4f75fe | = |
| Painted layers | a.nav-cta_dropdown-link.w-inline-block 218.0x57.0 bg #f5f3ef r 10px | = |
| Ancestor paint | 1 up div.nav_cta-dropdown-list.is-new bg #ffffff shadow #43413d @ 0.15 0px 5px 20px 0px | = |
| How | at rest | mouse hover |

Crops: `nav-login-link-default.png`, `nav-login-link-hover.png`.

#### nav-demo

Book-a-demo button. The dark "Book a demo" button in the top bar; links to a HubSpot meeting page, never followed.

Page: home. Selector: `nav a.btn-black_new`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 126.91 x 72 | = | = | = |
| Padding | 4px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #2d2323 | #4a3e3e | = | #4a3e3e |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | GT America 16px/32px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn-black_new.is-tablet-custom 126.9x72.0 bg #2d2323 r 12px | a.btn-black_new.is-tablet-custom 126.9x72.0 bg #4a3e3e r 12px | a.btn-black_new.is-tablet-custom 126.9x72.0 bg #2d2323 r 12px outline 1px auto #101010 offset 1px | a.btn-black_new.is-tablet-custom 126.9x72.0 bg #4a3e3e r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-demo-default.png`, `nav-demo-hover.png`, `nav-demo-focus-visible.png`, `nav-demo-pressed.png`.

#### nav-trial

Start-trial button. The blue "Start free trial" button in the top bar; links to /trial, never followed.

Page: home. Selector: `nav a.btn-primary_new`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 135.89 x 72 | = | = | = |
| Padding | 4px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #4f75fe | #254cda | = | #254cda |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | GT America 16px/32px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div: GT America 16px/32px 400, #ffffff | = | = | = |
| Transition | background-color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn-primary_new.hide-tablet 135.9x72.0 bg #4f75fe r 12px | a.btn-primary_new.hide-tablet 135.9x72.0 bg #254cda r 12px | a.btn-primary_new.hide-tablet 135.9x72.0 bg #4f75fe r 12px outline 1px auto #101010 offset 1px | a.btn-primary_new.hide-tablet 135.9x72.0 bg #254cda r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-trial-default.png`, `nav-trial-hover.png`, `nav-trial-focus-visible.png`, `nav-trial-pressed.png`.

### Home

#### hero-title

Hero title. "Beautiful HR tools for modern teams." — the hero display headline.

Page: home. Selector: `h1.new-home-h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 576 x 192 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Walsheim 64px/64px 900 |
| Letter spacing | -1px |
| Colour | #382d2d |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero subline. The hero supporting paragraph under the headline.

Page: home. Selector: `p after h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 92.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT America 22px/30.8px 400 |
| Letter spacing | normal |
| Colour | #4a3e3e |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-cta

Hero CTA. "Try free for 15 days" — the large primary button with an arrow icon under the hero copy; links to /trial, never followed.

Page: home. Selector: `a.btn-primary_new.is-icon.is-large`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 234 x 52 | = | = | = |
| Padding | 12px 16px 12px 20px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #4f75fe | #254cda | = | #254cda |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | GT America 20px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div: GT America 20px/28px 400, #ffffff | = | = | = |
| Transition | color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 25, colour #ffffff | = | = | = |
| Painted layers | a.btn-primary_new.is-icon 234.0x52.0 bg #4f75fe r 12px | a.btn-primary_new.is-icon 234.0x52.0 bg #254cda r 12px | a.btn-primary_new.is-icon 234.0x52.0 bg #4f75fe r 12px outline 1px auto #101010 offset 1px | a.btn-primary_new.is-icon 234.0x52.0 bg #254cda r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-demo

Hero secondary. The "Book a demo" bordered button beside the hero CTA.

Page: home. Selector: `.h-new-hero_left a.btn-secondary_new`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 160 x 54 | = | = | = |
| Padding | 12px 20px | = | = | = |
| Border | 1px solid #edebe7 | = | = | = |
| Radius | 12px | = | = | = |
| Background | #382d2d | #4a3e3e | = | #4a3e3e |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | GT America 20px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn-secondary_new.is-large 160.0x54.0 bg #382d2d border T:1px solid #edebe7 / R:1px solid #edebe7 / B:1px solid #edebe7 / L:1px solid #edebe7 r 12px | a.btn-secondary_new.is-large 160.0x54.0 bg #4a3e3e border T:1px solid #edebe7 / R:1px solid #edebe7 / B:1px solid #edebe7 / L:1px solid #edebe7 r 12px | a.btn-secondary_new.is-large 160.0x54.0 bg #382d2d border T:1px solid #edebe7 / R:1px solid #edebe7 / B:1px solid #edebe7 / L:1px solid #edebe7 r 12px outline 1px auto #101010 offset 1px | a.btn-secondary_new.is-large 160.0x54.0 bg #4a3e3e border T:1px solid #edebe7 / R:1px solid #edebe7 / B:1px solid #edebe7 / L:1px solid #edebe7 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-demo-default.png`, `hero-demo-hover.png`, `hero-demo-focus-visible.png`, `hero-demo-pressed.png`.

#### rating-row

Rating row. The social-proof row under the hero CTAs (Capterra rating, satisfaction, team count).

Page: home. Selector: `.home-new-hero_stats`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 50 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | strong.social-proof_bold: GT America 13px/15.6px 500, #382d2d |
| Transition | none |
| How | at rest |

Crops: `rating-row-default.png`.

#### section-h2

Section title. The first section heading under the hero.

Page: home. Selector: `first h2.new-h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 548 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Walsheim 48px/48px 900 |
| Letter spacing | -0.2px |
| Colour | #1e1818 |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

#### feature-accordion

Feature accordion. A feature accordion row (h-new_features-item w-dropdown): summary bar + expanding body; opened with its own toggle.

Page: home. Selector: `.h-new_features-item.w-dropdown`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 548 x 56 | 548 x 153.72 |
| Padding | 0px | = |
| Border | none | = |
| Radius | 10px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | GT America 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #4a3e3e | = |
| Text node | div.h-new_features-item-heading: GT America 20px/28px 400, #4a3e3e | = |
| Transition | background-color 0.2s ease | = |
| Icon | 17 x 17, colour #4a3e3e | = |
| Painted layers | div.h-new_features-item.is-white 548.0x56.0 bg #ffffff r 10px | div.h-new_features-item.is-white 548.0x153.7 bg #ffffff r 10px |
| How | at rest | own toggle |

Crops: `feature-accordion-default.png`, `feature-accordion-opened.png`.

#### feature-accordion-body

Accordion body. The body text region of an opened feature accordion.

Page: home. Selector: `.h-new_features-item-bot after open`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 548 x 97.72 |
| Padding | 0px 20px 20px 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #4a3e3e |
| Text node | p.h-new_features-item-body: GT America 18px/25.92px 400, #736b6b |
| Transition | none |
| How | at rest |

Crops: `feature-accordion-body-default.png`.

#### testimonial-card

Testimonial card. A customer testimonial card (land-new_testi-item): quote, avatar, name, role.

Page: home. Selector: `.land-new_testi-item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 400 x 354.38 |
| Padding | 60px 50px |
| Gap | 30px |
| Border | none |
| Radius | 20px |
| Background | #f5f1ec |
| Box shadow | #d386de 0px 4px 5px 0px |
| Outline | none |
| Font | GT America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #4a3e3e |
| Text node | p.new-page-paragraph.is-lg: GT America 28px/33.6px 400, #4a3e3e |
| Transition | none |
| Painted layers | div.land-new_testi-item.w-dyn-item 400.0x354.4 bg #f5f1ec r 20px shadow #d386de 0px 4px 5px 0px |
| How | at rest |

Crops: none.

#### marquee-item

Logo marquee item. A company logo cell in the scrolling customer marquee (CSS marquee animation).

Page: home. Selector: `.land-marquee_company-item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 128 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #4a3e3e |
| Transition | none |
| How | at rest |

Crops: none.

#### cta-band

CTA band. The closing call-to-action band before the footer (h-new_cta: label, headline, demo + trial buttons).

Page: home. Selector: `.h-new_cta`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1260 x 461.19 |
| Padding | 64px |
| Border | none |
| Radius | 40px |
| Background | #2d2323 |
| Box shadow | none |
| Outline | none |
| Font | GT America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.new-h2.no-letter-space: GT Walsheim 48px/48px 900, #ffffff |
| Transition | none |
| Icon | 24 x 24, colour #dbd9d5 |
| Painted layers | section.h-new_cta 1260.0x461.2 bg #2d2323 r 40px; a.btn-primary_new.is-icon 190.0x52.0 bg #4f75fe r 12px; a.btn-grey_new.is-large 158.0x52.0 bg #4a3e3e r 12px |
| Ancestor paint | 1 up div.card-container.is-new-home bg #ffffff |
| How | at rest |

Crops: `cta-band-default.png`.

#### page-ground

Page ground. The body element's painted fill — the page ground.

Page: home. Selector: `document.body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 5961.27 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | GT America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #4a3e3e |
| Text node | div: GT America 16px/22px 400, #4a3e3e |
| Transition | none |
| Icon | 42 x 28, colour #4a3e3e |
| Painted layers | body.body-home 1440.0x5961.3 bg #ffffff; div.nav-primary.is-new 1440.0x104.0 bg #ffffff; div.nav-primary.is-new 1440.0x104.0 bg #ffffff; div.nav-new.is-v2 1440.0x104.0 bg #ffffff r 60px; div.mobilenav-bar-menu-icon-v2.new 0.0x0.0 bg #ffffff @ 0 image linear-gradient(#ffffff, #ffffff) r 8px 0px 0px 8px; div.nav-line 0.0x0.0 bg #2d2323 |
| How | at rest |

Crops: none.

### Footer

#### footer

Footer. The footer band: link columns, newsletter form, social icons and legal subfooter.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1340 x 622.17 |
| Padding | 30px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.footer-heading: GT Walsheim 20px/20px 900, #2d2323 |
| Transition | none |
| Icon | 126.39 x 32, colour #4f75fe |
| Painted layers | input.newsletter-text-white-2.w-input 217.0x50.0 bg #2d2323 @ 0.1 r 30px 0px 0px 30px; input.newsletter-white.w-button 96.0x50.0 bg #2d2323 r 0px 30px 30px 0px; div.error-message.w-form-fail 0.0x0.0 bg #ffdede; a.footer__content-socialicon-link.w-inline-block 40.0x40.0 bg #2d2323 r 100px; a.footer__content-socialicon-link.w-inline-block 40.0x40.0 bg #2d2323 r 100px; a.footer__content-socialicon-link.w-inline-block 40.0x40.0 bg #2d2323 r 100px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A link in a footer link column.

Page: home. Selector: `footer a.footer-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 41 x 25 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | GT America 20px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #736b6b | #2d2323 | = | #2d2323 |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.footer-link.text-color-brown-200 41.0x25.0 outline 1px auto #101010 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-heading

Footer heading. A column heading in the footer.

Page: home. Selector: `.footer-heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 303 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Walsheim 20px/20px 900 |
| Letter spacing | normal |
| Colour | #2d2323 |
| Transition | none |
| How | at rest |

Crops: `footer-heading-default.png`.

#### newsletter-field

Newsletter field. The footer newsletter email input; focused locally, never submitted.

Page: home. Selector: `input.newsletter-text-white-2`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 217 x 50 | = |
| Padding | 8px 12px 8px 20px | = |
| Border | none | = |
| Radius | 30px 0px 0px 30px | = |
| Background | #2d2323 @ 0.1 | #2d2323 @ 0.2 |
| Box shadow | none | = |
| Outline | none | = |
| Font | GT America 18px/25.7143px 400 | = |
| Letter spacing | normal | = |
| Colour | #2d2323 | = |
| Transition | all 0.2s ease | = |
| Cursor | text | = |
| Placeholder | #2d2323 @ 0.7, opacity 1 | = |
| Painted layers | input.newsletter-text-white-2.w-input 217.0x50.0 bg #2d2323 @ 0.1 r 30px 0px 0px 30px | input.newsletter-text-white-2.w-input 217.0x50.0 bg #2d2323 @ 0.2 r 30px 0px 0px 30px |
| How | at rest | clicked into the field |

Crops: `newsletter-field-default.png`, `newsletter-field-focused.png`.

#### newsletter-button

Newsletter button. The newsletter subscribe submit; measured never pressed (a submit control).

Page: home. Selector: `.newsletter-white`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 96 x 50 | = |
| Padding | 9px 20px 9px 15px | = |
| Border | none | = |
| Radius | 0px 30px 30px 0px | = |
| Background | #2d2323 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | GT America 18px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | background-color 0.2s ease | = |
| Cursor | pointer | = |
| Placeholder | #ffffff, opacity 1 | = |
| Painted layers | input.newsletter-white.w-button 96.0x50.0 bg #2d2323 r 0px 30px 30px 0px | = |
| How | at rest | mouse hover |

Crops: `newsletter-button-default.png`, `newsletter-button-hover.png`.

### Pricing

#### pricing-title

Pricing title. "Choose the right plan for your team." — the pricing headline.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1120 x 180 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Walsheim 100px/90px 900 |
| Letter spacing | -2px |
| Colour | #1f1818 |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### plan-card

Plan card. A plan card (new-pricing_plan-card): plan name, description, price, job-slot stepper and feature list.

Page: pricing. Selector: `.new-pricing_plan-card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 652 x 442 |
| Padding | 48px |
| Gap | 20px |
| Border | 1px solid #e3e1dd |
| Radius | 32px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | GT America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #2d2323 |
| Text node | div.new-pricing_plan-card-text: GT Walsheim 48px/48px 900, #1f1818 |
| Transition | none |
| Painted layers | div.new-pricing_plan-card.is-white 652.0x442.0 bg #ffffff border T:1px solid #e3e1dd / R:1px solid #e3e1dd / B:1px solid #e3e1dd / L:1px solid #e3e1dd r 32px; a.new-pricing_button.w-button 150.0x52.0 bg #1f1818 r 10px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-stepper-plus

Job-slot stepper. The plus icon in a plan card's job-slot stepper — a local stepper that changes the quoted price; measured, and the minus side paints .disabled.

Page: pricing. Selector: `[job-slots-plus]`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 26 x 32 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | GT America 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1f1818 | #736b6b | #736b6b |
| Transition | color 0.2s ease | = | = |
| Cursor | pointer | = | = |
| Icon | 26 x 26, colour #1f1818 | 26 x 26, colour #736b6b | 26 x 26, colour #736b6b |
| Ancestor paint | 1 up div.new-pricing_plan-selector-wrap.is-large bg #ffffff shadow #e3e1dd 0px 2px 0px 0px | = | = |
| How | at rest | mouse hover | CDP forcePseudoState :active:hover |

Crops: `plan-stepper-plus-default.png`, `plan-stepper-plus-hover.png`, `plan-stepper-plus-pressed.png`.

#### plan-stepper-minus

Job-slot minus (disabled). The minus icon at the stepper's floor — painted with a .disabled class.

Page: pricing. Selector: `[job-slots-minus].disabled`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 26 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #f5f3ef |
| Transition | color 0.2s ease |
| Icon | 26 x 26, colour #f5f3ef |
| Ancestor paint | 1 up div.new-pricing_plan-selector-wrap.is-large bg #ffffff shadow #e3e1dd 0px 2px 0px 0px |
| How | at rest |

Crops: `plan-stepper-minus-default.png`.

#### plan-button

Plan CTA. A "Start free trial" button inside a plan card; links to /trial, never followed.

Page: pricing. Selector: `a.new-pricing_button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 150 x 52 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #1f1818 | #382d2d | = | #382d2d |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | GT America 20px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.new-pricing_button.w-button 150.0x52.0 bg #1f1818 r 10px | a.new-pricing_button.w-button 150.0x52.0 bg #382d2d r 10px | a.new-pricing_button.w-button 150.0x52.0 bg #1f1818 r 10px outline 1px auto #101010 offset 1px | a.new-pricing_button.w-button 150.0x52.0 bg #382d2d r 10px |
| Ancestor paint | 1 up div.new-pricing_plan-card.is-white bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-button-default.png`, `plan-button-hover.png`, `plan-button-focus-visible.png`, `plan-button-pressed.png`.

#### plan-feature

Plan feature row. A feature row inside a plan card (icon + text).

Page: pricing. Selector: `.new-pricing_plan-feature-tab`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 56 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #2d2323 |
| Text node | div.new-pricing_plan-paragraph.is-brown-600: GT America 18px/32px 400, #1f1818 |
| Transition | none |
| Ancestor paint | 1 up div.new-pricing_plan-card.is-white bg #ffffff |
| How | at rest |

Crops: `plan-feature-default.png`.

#### pricing-table

Comparison table. The plan comparison table lives in .section_compare.is-hide — the public page paints the section hidden, so nothing is measured.

Page: pricing. Selector: `.section_compare:not(.is-hide) .pricing_table-block`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 0 x 0 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT America 18px/20px 400 |
| Letter spacing | normal |
| Colour | #e3e1dd |
| Text node | undefined: Oliver 16px/20px 400, #a3a2a2 |
| Transition | none |
| Painted layers | div.pricing_plan-menu.dark 0.0x0.0 bg #2d2323 r 14px; a.pricing_plan-link.w-inline-block 0.0x0.0 bg #dddddd @ 0; a.pricing_plan-link.w-inline-block 0.0x0.0 bg #dddddd @ 0 |
| How | at rest |

Crops: none.

#### pricing-table-head

Table header cell. A header cell in the comparison table — unreachable while the section is hidden.

Page: pricing. Selector: `.section_compare:not(.is-hide) .pricing_table-block-heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 0 x 0 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Walsheim 24px/36px 900 |
| Letter spacing | normal |
| Colour | #e3e1dd |
| Transition | none |
| How | at rest |

Crops: none.

#### pricing-table-row

Table row. A feature row in the comparison table — unreachable while the section is hidden.

Page: pricing. Selector: `.section_compare:not(.is-hide) .pricing_table-row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 0 x 0 |
| Padding | 24px 0px |
| Gap | 16px |
| Border | T: none; R: none; B: 1px solid #4a3e3e; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #2d2323 |
| Text node | undefined: GT America 18px/20px 400, #e3e1dd |
| Transition | none |
| Icon | 0 x 0, colour #e3e1dd |
| Painted layers | div.pricing_table-row 0.0x0.0 border B:1px solid #4a3e3e; div.popup-element.long 0.0x0.0 bg #0d0d12 r 8px |
| How | at rest |

Crops: none.

#### faq-item

FAQ item. A pricing FAQ accordion item; opened with its own toggle.

Page: pricing. Selector: `.h-new_features-item`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 677.64 x 56 | 677.64 x 227.53 |
| Padding | 0px | = |
| Border | none | = |
| Radius | 10px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | GT America 25px/37.5px 400 | = |
| Letter spacing | normal | = |
| Colour | #2d2323 | = |
| Text node | div.h-new_features-item-heading.faq: GT America 20px/28px 400, #4a3e3e | = |
| Transition | background-color 0.2s ease | = |
| Icon | 17 x 17, colour #4a3e3e | = |
| Painted layers | div.h-new_features-item.is-white 677.6x56.0 bg #ffffff r 10px | div.h-new_features-item.is-white 677.6x227.5 bg #ffffff r 10px |
| How | at rest | own toggle |

Crops: `faq-item-default.png`, `faq-item-opened.png`.

#### faq-answer

FAQ answer. The rich-text body of an opened FAQ item.

Page: pricing. Selector: `.faq_rich after open`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 633.64 x 151.53 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT America 18px/27px 400 |
| Letter spacing | normal |
| Colour | #2d2323 |
| Text node | p: GT America 18px/25.92px 400, #736b6b |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `faq-answer-default.png`.

#### pricing-cta

Pricing CTA. The closing trial CTA on the pricing page.

Page: pricing. Selector: `a.pricing_button.on-cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 130 x 54 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | GT America 20px/30px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2d2323 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.pricing_button.on-cta 130.0x54.0 bg #ffffff r 10px | = | a.pricing_button.on-cta 130.0x54.0 bg #ffffff r 10px outline 1px auto #101010 offset 1px | = |
| Ancestor paint | 1 up div.pricing_faq-block bg #f5f3ef | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pricing-cta-default.png`, `pricing-cta-hover.png`, `pricing-cta-focus-visible.png`, `pricing-cta-pressed.png`.

### ATS page

#### ats-title

ATS title. The /ats product page headline.

Page: ats. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 192 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Walsheim 64px/64px 900 |
| Letter spacing | -1px |
| Colour | #382d2d |
| Transition | none |
| How | at rest |

Crops: `ats-title-default.png`.

#### ats-feature-item

Feature item. A feature row on the ATS product page (new-ats_feature-item).

Page: ats. Selector: `.new-ats_feature-item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 189 x 54 |
| Padding | 12px 16px |
| Gap | 10px |
| Border | 1px solid #edebe7 |
| Radius | 10px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #4a3e3e |
| Text node | div.new-page-paragraph.is-sm: GT America 18px/25.2px 400, #4a3e3e |
| Transition | none |
| Painted layers | div.new-ats_feature-item 189.0x54.0 border T:1px solid #edebe7 / R:1px solid #edebe7 / B:1px solid #edebe7 / L:1px solid #edebe7 r 10px |
| How | at rest |

Crops: `ats-feature-item-default.png`.

#### ats-tab

ATS feature link. A feature-item link inside the ATS features body; the tab script paints the inactive copies display:none.

Page: ats. Selector: `.new-ats_features-body a.new-ats_feature-item`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 0 x 0 | - |
| Padding | 12px 16px | - |
| Gap | 8px | - |
| Border | 1px solid #edebe7 | - |
| Radius | 10px | - |
| Background | #4f75fe | - |
| Box shadow | none | - |
| Outline | none | - |
| Font | GT America 14px/20px 400 | - |
| Letter spacing | normal | - |
| Colour | #ffffff | - |
| Text node | undefined: GT America 18px/25.2px 400, #4a3e3e | - |
| Transition | none | - |
| Cursor | pointer | - |
| Icon | 0 x 0, colour #ffffff | - |
| Painted layers | a.new-ats_feature-item.is-blue 0.0x0.0 bg #4f75fe border T:1px solid #edebe7 / R:1px solid #edebe7 / B:1px solid #edebe7 / L:1px solid #edebe7 r 10px | - |
| How | at rest | - |
| Error | - | locator.hover: Element is not visible Call log:   - waiting for locator('.new-ats_features-body a.new-ats_feature-item').first().first().first()     - locator resolved to <a href="/product/features" c |

Crops: `ats-tab-default.png`.

#### ats-card

ATS card. A product card on the ATS page (new-ats_card: heading, image, bottom text).

Page: ats. Selector: `.new-ats_card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1260 x 997.98 |
| Padding | 48px 64px |
| Gap | 44px |
| Border | none |
| Radius | 40px |
| Background | #faf9f7 |
| Box shadow | none |
| Outline | none |
| Font | GT America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #4a3e3e |
| Text node | div.overheading-medium.no-margin: Oliver 22px/30.8px 400, #4f75fe |
| Transition | none |
| Painted layers | section.new-ats_card 1260.0x998.0 bg #faf9f7 r 40px |
| Ancestor paint | 1 up div.card-container.is-new-home bg #ffffff |
| How | at rest |

Crops: `ats-card-default.png`.

#### ats-integrate-card

Integration card. An integrations card on the ATS page (new-ats_integrate-card).

Page: ats. Selector: `.new-ats_integrate-card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 356 x 209.19 |
| Padding | 24px |
| Border | none |
| Radius | 20px |
| Background | #ffffff |
| Box shadow | #e3e1dd 0px 2px 0px 0px |
| Outline | none |
| Font | GT America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.new-ats_integrate-card-head: GT Walsheim 24px/31.92px 900, #000000, ls -0.5px |
| Transition | all 0.2s ease |
| Cursor | pointer |
| Painted layers | a.new-ats_integrate-card.w-inline-block 356.0x209.2 bg #ffffff r 20px shadow #e3e1dd 0px 2px 0px 0px |
| How | at rest |

Crops: `ats-integrate-card-default.png`.

### Careers site (jobs.homerun.co)

#### cookie-banner

Cookie banner. The careers site's consent banner (CookieBanner), measured at rest then hidden for every other reading — never answered.

Page: careers. Selector: `[class*=CookieBanner]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 775 x 104 |
| Padding | 30px |
| Gap | 30px |
| Border | none |
| Radius | 5px |
| Background | #ffffff |
| Box shadow | #212b36 @ 0.15 0px 2px 5px 0px |
| Outline | none |
| Font | GT-America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | p.CookieBanner__text__VOzAT: Inter 16px/22px 400, #454f5b |
| Transition | none |
| Painted layers | div.CookieBanner__content__U9KWG.CookieBanner__contentWide__eL32M 775.0x104.0 bg #ffffff r 5px shadow #212b36 @ 0.15 0px 2px 5px 0px; button.btn.CookieBanner__btn__47c-V 82.0x36.0 bg #ffffff border T:1px solid #dfe3e8 / R:1px solid #dfe3e8 / B:1px solid #dfe3e8 / L:1px solid #dfe3e8 r 4px; button.btn.CookieBanner__btn__47c-V 79.0x36.0 bg #0192fd border T:1px solid #0192fd / R:1px solid #0192fd / B:1px solid #0192fd / L:1px solid #0192fd r 4px |
| How | at rest |

Crops: `cookie-banner-default.png`.

#### careers-header

Careers header. The careers site header block (job-blocks career-site-header): company intro and share links.

Page: careers. Selector: `.career-site-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.1 0px 1px 1px 0px |
| Outline | none |
| Font | GT-America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | p: Inter 14px/32px 400, #000000 @ 0.7 |
| Transition | all 0.4s ease |
| Opacity | 0 |
| Painted layers | header.job-blocks.career-site-header 1440.0x60.0 bg #ffffff shadow #000000 @ 0.1 0px 1px 1px 0px; div.language-selector.js-dropdown 75.0x34.0 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1; div::after.language-selector.js-dropdown 5pxx5px border R:1px solid #000000 @ 0.7 / B:1px solid #000000 @ 0.7; ul 175.0x81.0 r 4px shadow #000000 @ 0.2 0px 1px 4px 1px; li.social-icon-btn.icon-xitter 175.0x40.0 bg #ffffff r 3px 3px 0px 0px; li::before.social-icon-btn.icon-xitter 14pxx14px bg #000000 |
| How | at rest |

Crops: `careers-header-default.png`.

#### careers-logo

Careers logo. The company logo link at the top of the careers site.

Page: careers. Selector: `a.company-logo-link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 220 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GTAmerica-Regular 32px/140px 400 |
| Letter spacing | normal |
| Colour | #466af6 |
| Transition | all 0.18s cubic-bezier(0.55, 0.025, 0.455, 0.98) |
| Cursor | pointer |
| How | at rest |

Crops: `careers-logo-default.png`.

#### careers-share

Share button. A share-this-site social icon button in the careers header; measured never pressed.

Page: careers. Selector: `a.social-icon-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 175 x 40 | = | - | = |
| Padding | 0px 10px 0px 37px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 15px/40px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #736b6b | = | - | = |
| Transition | all 0.18s cubic-bezier(0.55, 0.025, 0.455, 0.98) | = | - | = |
| Cursor | pointer | = | - | = |
| Ancestor paint | 1 up li.social-icon-btn.icon-xitter bg #ffffff; 2 up ul shadow #000000 @ 0.2 0px 1px 4px 1px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `careers-share-pressed.png`.

#### careers-all-jobs

See-all-jobs button. The "See all jobs" button — scrolls to the job list.

Page: careers. Selector: `a.btn-all-jobs`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 179 x 59 | = | - | = |
| Padding | 0px | = | - | = |
| Border | T: none; R: none; B: 1px solid #466af6; L: none | = | - | = |
| Radius | 12px | = | - | = |
| Background | #466af6 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | GTAmerica-Regular 22px/34px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Text node | span: GTAmerica-Regular 22px/34px 400, #ffffff | = | - | = |
| Transition | all 0.18s cubic-bezier(0.55, 0.025, 0.455, 0.98) | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | a.button.btn-all-jobs 179.0x59.0 bg #466af6 border B:1px solid #466af6 r 12px; i.icon-arrow-left 24.0x24.0 bg #ffffff | a.button.btn-all-jobs 179.0x59.0 bg #466af6 border B:1px solid #466af6 r 12px; span.content 179.0x58.0 bg #000000 @ 0.15 r 12px; i.icon-arrow-left 24.0x24.0 bg #ffffff | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `careers-all-jobs-default.png`, `careers-all-jobs-hover.png`, `careers-all-jobs-pressed.png`.

#### careers-filter

Filter button. A job-list filter pill (Department/Location/Job type) — opens a filter popover.

Page: careers. Selector: `button[class*=BaseButton__button]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 110 x 36 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Border | 1px solid #000000 @ 0.1 | 1px solid #000000 @ 0 | = | 1px solid #000000 @ 0 |
| Radius | 8px | = | = | = |
| Background | transparent | #000000 @ 0.7 | = | #000000 @ 0.7 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 15px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.7 | #ffffff | = | #ffffff |
| Transition | all 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.BaseButton__button__EVI95 110.0x36.0 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 8px | button.BaseButton__button__EVI95 110.0x36.0 bg #000000 @ 0.7 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | button.BaseButton__button__EVI95 110.0x36.0 bg #000000 @ 0.7 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `careers-filter-default.png`, `careers-filter-hover.png`, `careers-filter-focus-visible.png`, `careers-filter-pressed.png`.

#### careers-job-card

Job card. A job listing row (title + location + department); links to the job page, never followed.

Page: careers. Selector: `a[class*=JobListItems__listItem]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1080 x 54 | = | = | = |
| Padding | 14px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px 8px 0px 0px | = | = | = |
| Background | #ffffff | #000000 @ 0.7 | = | #000000 @ 0.7 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #22a9e5 | #333333 | #3277b2 | #333333 |
| Text node | p.JobListItems__jobTitle__6cPrj: GT-Walsheim-Ultra-Bold 18px/26px 400, #131313 | p.JobListItems__jobTitle__6cPrj: GT-Walsheim-Ultra-Bold 18px/26px 400, #ffffff | = | p.JobListItems__jobTitle__6cPrj: GT-Walsheim-Ultra-Bold 18px/26px 400, #ffffff |
| Transition | all 0.18s cubic-bezier(0.55, 0.025, 0.455, 0.98) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.JobListItems__lightListItem__Ev5JI.JobListItems__listItem__s8ogh 1080.0x54.0 bg #ffffff r 8px 8px 0px 0px; p::before.JobListItems__listItemInfoText__RdxZL 2pxx2px bg #777777; p::before.JobListItems__listItemInfoText__RdxZL 2pxx2px bg #777777 | a.JobListItems__lightListItem__Ev5JI.JobListItems__listItem__s8ogh 1080.0x54.0 bg #000000 @ 0.7 r 8px 8px 0px 0px; p::before.JobListItems__listItemInfoText__RdxZL 2pxx2px bg #ffffff; p::before.JobListItems__listItemInfoText__RdxZL 2pxx2px bg #ffffff | = | a.JobListItems__lightListItem__Ev5JI.JobListItems__listItem__s8ogh 1080.0x54.0 bg #000000 @ 0.7 r 8px 8px 0px 0px; p::before.JobListItems__listItemInfoText__RdxZL 2pxx2px bg #ffffff; p::before.JobListItems__listItemInfoText__RdxZL 2pxx2px bg #ffffff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `careers-job-card-default.png`, `careers-job-card-hover.png`, `careers-job-card-focus-visible.png`, `careers-job-card-pressed.png`.

#### careers-carousel

Carousel control. The next-arrow of the careers photo carousel (local UI control).

Page: careers. Selector: `button.control.next`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 60 x 120 | = |
| Padding | 1px 6px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | #000000 @ 0.2 | #000000 @ 0.4 |
| Box shadow | none | = |
| Outline | none | = |
| Font | GTAmerica-Regular 22px/34px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | all 0.15s cubic-bezier(0.455, 0.03, 0.515, 0.955) | = |
| Cursor | pointer | = |
| ::after | 22px x 22px, absolute, bg #000000 @ 0, radius 0px | = |
| Painted layers | button.control.next 60.0x120.0 bg #000000 @ 0.2 r 4px; button::after.control.next 22pxx22px border T:4px solid #ffffff / R:4px solid #ffffff | button.control.next 60.0x120.0 bg #000000 @ 0.4 r 4px; button::after.control.next 22pxx22px border T:4px solid #ffffff / R:4px solid #ffffff |
| How | at rest | mouse hover |

Crops: `careers-carousel-default.png`, `careers-carousel-hover.png`.

#### job-title

Job title. The open-application page heading (jobs.homerun.co/open/en).

Page: job. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 160 x 58 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/58px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| Ancestor paint | 1 up header.job-header bg #ffffff shadow #000000 @ 0.15 0px 0px 0px 1px |
| How | at rest |

Crops: `job-title-default.png`.

#### job-apply

Apply button. The "Apply now" button on a job page; links to the application form, measured never followed.

Page: job. Selector: `a.btn-apply`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 130 x 60 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #466af6 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 18px/38px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Inter 18px/38px 400, #ffffff | = | = | = |
| Transition | all 0.18s cubic-bezier(0.55, 0.025, 0.455, 0.98) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.btn-apply 130.0x60.0 bg #466af6; span 130.0x60.0 bg #000000 @ 0.15 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `job-apply-default.png`, `job-apply-hover.png`, `job-apply-focus-visible.png`, `job-apply-pressed.png`.

#### job-prose

Job body. The job description prose block (vacancy-text).

Page: job. Selector: `.vacancy-text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 531 |
| Padding | 0px 0px 60px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GTAmerica-Regular 22px/32px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p: GTAmerica-Regular 22px/32px 400, #ffffff |
| Transition | none |
| Painted layers | a.button.btn-apply 147.0x55.0 bg #466af6 border B:1px solid #466af6 r 4px |
| How | at rest |

Crops: `job-prose-default.png`.

#### job-share

Share link. A share-this-job link (X/LinkedIn); measured never followed.

Page: job. Selector: `.share-job a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 16 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #736b6b | transparent | transparent | transparent |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | #a3a2a2 | #a3a2a2 | #a3a2a2 |
| Text node | undefined: Inter 14px/20px 400, #333333 | undefined: Inter 14px/20px 400, #a3a2a2 | undefined: Inter 14px/20px 400, #a3a2a2 | undefined: Inter 14px/20px 400, #a3a2a2 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.social-icon-btn.icon-xitter 16.0x16.0 bg #736b6b | - | - | - |
| Ancestor paint | 3 up header.job-header.show bg #ffffff shadow #000000 @ 0.15 0px 0px 0px 1px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `job-share-default.png`, `job-share-hover.png`, `job-share-focus-visible.png`, `job-share-pressed.png`.

#### job-back

Back link. The back-to-career-site link at the job page top; measured never followed.

Page: job. Selector: `a.back-to-career-site`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 60 x 60 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #e3e1dd | = | #e3e1dd |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | GT-America 14px/60px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | = | = | = |
| Transition | background-color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 24px x 54px, relative, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.back-to-career-site.genericon-collapse 60.0x60.0 bg #e3e1dd | = | a.back-to-career-site.genericon-collapse 60.0x60.0 bg #e3e1dd |

Crops: `job-back-default.png`, `job-back-hover.png`, `job-back-focus-visible.png`, `job-back-pressed.png`.

### Application form

#### apply-steps

Form steps. The 4-step indicator (Your details / Questions / Preview / Submit).

Page: apply. Selector: `nav.progressbar ul.nav-tabs`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 0px/0px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | a: Inter 18px/40px 400, #ffffff |
| Transition | none |
| Painted layers | span.fill-bar 1440.0x40.0 bg #000000 @ 0.3; i 0.0x40.0 bg #4f75fe; ul.nav.nav-tabs 1440.0x41.0 border B:1px solid #000000 @ 0.3; li.active 360.0x40.0 bg #4f75fe; li 360.0x40.0 border L:1px solid #000000 @ 0.1; li 360.0x40.0 border L:1px solid #000000 @ 0.1 |
| Ancestor paint | 1 up body.ng-scope bg #1f1818 |
| How | at rest |

Crops: `apply-steps-default.png`.

#### apply-field

Text field. A text input in the application form; focused locally, never submitted.

Page: apply. Selector: `input[name=first_name]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 235 x 40 | = |
| Padding | 0px 10px | = |
| Border | 1px solid #e8e8e8 | 1px solid #cccccc |
| Radius | 2px | = |
| Background | #fafafa | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 17px/24.2857px 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | = |
| Transition | all 0.2s ease-out | = |
| Cursor | text | = |
| Placeholder | #333333, opacity 1 | = |
| Painted layers | input.ng-pristine.ng-untouched 235.0x40.0 bg #fafafa border T:1px solid #e8e8e8 / R:1px solid #e8e8e8 / B:1px solid #e8e8e8 / L:1px solid #e8e8e8 r 2px | input.ng-pristine.ng-untouched 235.0x40.0 bg #fafafa border T:1px solid #cccccc / R:1px solid #cccccc / B:1px solid #cccccc / L:1px solid #cccccc r 2px |
| Ancestor paint | 3 up div.center-container bg #ffffff shadow #000000 @ 0.1 0px 0px 0px 1px | = |
| How | at rest | clicked into the field |

Crops: `apply-field-default.png`, `apply-field-focused.png`.

#### apply-email

Email field. The email input in the application form; focused locally, never submitted.

Page: apply. Selector: `input[name=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 480 x 40 | = |
| Padding | 0px 10px | = |
| Border | 1px solid #e8e8e8 | 1px solid #cccccc |
| Radius | 2px | = |
| Background | #fafafa | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 17px/24.2857px 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | = |
| Transition | all 0.2s ease-out | = |
| Cursor | text | = |
| Placeholder | #333333, opacity 1 | = |
| Painted layers | input.ng-pristine.ng-untouched 480.0x40.0 bg #fafafa border T:1px solid #e8e8e8 / R:1px solid #e8e8e8 / B:1px solid #e8e8e8 / L:1px solid #e8e8e8 r 2px | input.ng-pristine.ng-untouched 480.0x40.0 bg #fafafa border T:1px solid #cccccc / R:1px solid #cccccc / B:1px solid #cccccc / L:1px solid #cccccc r 2px |
| Ancestor paint | 3 up div.center-container bg #ffffff shadow #000000 @ 0.1 0px 0px 0px 1px | = |
| How | at rest | clicked into the field |

Crops: `apply-email-default.png`, `apply-email-focused.png`.

#### apply-file

File dropzone. The resume upload dropzone (.file-drop wraps the hidden native file input); measured at rest, nothing uploaded.

Page: apply. Selector: `.file-drop`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 0 x 0 |
| Padding | 50px |
| Border | 1px solid #e8e8e8 |
| Radius | 3px |
| Background | #fafafa |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/25.7143px 400 |
| Letter spacing | normal |
| Colour | #999999 |
| Text node | undefined: Inter 17px/28px 400, #ffffff |
| Transition | none |
| Painted layers | div.file-drop.ng-isolate-scope 0.0x0.0 bg #fafafa border T:1px solid #e8e8e8 / R:1px solid #e8e8e8 / B:1px solid #e8e8e8 / L:1px solid #e8e8e8 r 3px; div.answer-button.selected 0.0x0.0 bg #4f75fe r 22px |
| Ancestor paint | 3 up div.center-container bg #ffffff shadow #000000 @ 0.1 0px 0px 0px 1px |
| How | at rest |

Crops: none.

#### apply-checkbox

Consent checkbox. A data-consent checkbox row (label.checkbox-container paints the custom box around the hidden input); never ticked.

Page: apply. Selector: `label.checkbox-container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 0 x 0 |
| Padding | 20px 0px 0px 0px |
| Gap | 10px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/25.7143px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | undefined: Inter 18px/25.7143px 400, #333333 |
| Transition | none |
| Cursor | pointer |
| Painted layers | i.checkbox.icon-filled-check-4 0.0x0.0 border T:2px solid #e5e5e5 / R:2px solid #e5e5e5 / B:2px solid #e5e5e5 / L:2px solid #e5e5e5 r 3px |
| Ancestor paint | 1 up div.center-container bg #ffffff shadow #000000 @ 0.1 0px 0px 0px 1px |
| How | at rest |

Crops: none.

#### apply-next

Next-step button. The "Next: Questions" control — measured never pressed (it advances the wizard; the final Submit is never reached).

Page: apply. Selector: `button.tab-control.next`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 538 x 80 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px 0px 5px 5px | = |
| Background | #4f75fe | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 24px/34.2857px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | span: Inter 24px/80px 400, #ffffff | = |
| Transition | all 0.1s cubic-bezier(0.455, 0.03, 0.515, 0.955) | = |
| Cursor | default | = |
| ::after | 10px x 10px, absolute, bg #000000 @ 0, radius 0px | = |
| Painted layers | button.tab-control.full-width 538.0x80.0 bg #4f75fe r 0px 0px 5px 5px; button::after.tab-control.full-width 10pxx10px border B:2px solid #ffffff / L:2px solid #ffffff | button.tab-control.full-width 538.0x80.0 bg #4f75fe r 0px 0px 5px 5px; button::after.tab-control.full-width 10pxx10px border B:2px solid #ffffff / L:2px solid #ffffff; span 538.0x80.0 bg #ffffff @ 0.15 |
| How | at rest | mouse hover |

Crops: `apply-next-default.png`, `apply-next-hover.png`.

#### apply-back

Back link. The back-to-job link in the application bar; measured never followed.

Page: apply. Selector: `a.btn-back`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 61 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | T: none; R: 1px solid #000000 @ 0.1; B: none; L: none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #ffffff @ 0.15 | #ffffff @ 0.15 | #ffffff @ 0.15 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 0px/0px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #22a9e5 | #333333 | #3277b2 | #333333 |
| Transition | all 0.2s ease | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 7px x 7px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | a.btn-back.in-bar 61.0x40.0 border R:1px solid #000000 @ 0.1; a::after.btn-back.in-bar 7pxx7px border B:2px solid #ffffff / L:2px solid #ffffff | a.btn-back.in-bar 61.0x40.0 bg #ffffff @ 0.15 border R:1px solid #000000 @ 0.1; a::after.btn-back.in-bar 7pxx7px border B:2px solid #ffffff / L:2px solid #ffffff | a.btn-back.in-bar 61.0x40.0 bg #ffffff @ 0.15 border R:1px solid #000000 @ 0.1; a::after.btn-back.in-bar 7pxx7px border B:2px solid #ffffff / L:2px solid #ffffff | a.btn-back.in-bar 61.0x40.0 bg #ffffff @ 0.15 border R:1px solid #000000 @ 0.1; a::after.btn-back.in-bar 7pxx7px border B:2px solid #ffffff / L:2px solid #ffffff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `apply-back-default.png`, `apply-back-hover.png`, `apply-back-focus-visible.png`, `apply-back-pressed.png`.

### ATS sign-in (boundary)

#### signin-card

Sign-in card. The app.homerun.co login card the Angular SPA paints (ATS/HR variant tabs, SSO buttons, email/password). Measured at rest, never submitted.

Page: signin. Selector: `[class*=Login__container]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT-America 16px/22px 400 |
| Letter spacing | normal |
| Colour | #4a3e3e |
| Text node | span.h-button-content: GT-America 16px/22px 400, #4f75fe |
| Transition | none |
| Icon | 24 x 24, colour #4a3e3e |
| Painted layers | div.LayoutPublic__page__UAEh7.LayoutPublic__light__KdQm5 1440.0x900.0 bg #f5f3ef; a.Login__platform-button__MFLx3.Login__ats__G0I7b 231.0x64.0 bg #ffffff r 20px 20px 0px 0px; a.Login__platform-button__MFLx3.Login__hr__CKQ6x 231.0x64.0 bg #edebe7 r 20px 20px 0px 0px; div.Login__form__S81Mo.public__form-container__srWiu 462.0x541.0 bg #ffffff r 0px 0px 20px 20px shadow #e3e1dd 0px 2px 0px 0px; button.LoginForm__sso-button__HrA8R.public__sso-button__Kprsc 382.0x44.0 border T:1px solid #665757 @ 0.2 / R:1px solid #665757 @ 0.2 / B:1px solid #665757 @ 0.2 / L:1px solid #665757 @ 0.2 r 10px shadow #e3e1dd 0px 2px 0px 0px; button.LoginForm__sso-button__HrA8R.public__sso-button__Kprsc 382.0x44.0 border T:1px solid #665757 @ 0.2 / R:1px solid #665757 @ 0.2 / B:1px solid #665757 @ 0.2 / L:1px solid #665757 @ 0.2 r 10px shadow #e3e1dd 0px 2px 0px 0px |
| How | at rest |

Crops: `signin-card-default.png`.

#### signin-tab

Product tab. The ATS/HR product tab at the card top (the HR variant links to app.homerun.hr; measured never followed).

Page: signin. Selector: `a[class*=Login__platform-button]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 231 x 64 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 20px 20px 0px 0px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | GT-America 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #4a3e3e | = |
| Transition | none | = |
| Cursor | default | = |
| Painted layers | a.Login__platform-button__MFLx3.Login__ats__G0I7b 231.0x64.0 bg #ffffff r 20px 20px 0px 0px | = |
| How | at rest | mouse hover |

Crops: `signin-tab-default.png`, `signin-tab-hover.png`.

#### signin-sso

SSO button. "Log in with Google" — an SSO button on the card; measured never pressed.

Page: signin. Selector: `button[class*=sso-button]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 382 x 44 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | 1px solid #665757 @ 0.2 | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | #f5f3ef | = | #f5f3ef |
| Box shadow | #e3e1dd 0px 2px 0px 0px | = | = | = |
| Outline | none | = | 5px auto #101010 offset 0px | = |
| Font | GT-America 16px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #4a3e3e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #4a3e3e | = | = | = |
| Painted layers | button.LoginForm__sso-button__HrA8R.public__sso-button__Kprsc 382.0x44.0 border T:1px solid #665757 @ 0.2 / R:1px solid #665757 @ 0.2 / B:1px solid #665757 @ 0.2 / L:1px solid #665757 @ 0.2 r 10px shadow #e3e1dd 0px 2px 0px 0px | button.LoginForm__sso-button__HrA8R.public__sso-button__Kprsc 382.0x44.0 bg #f5f3ef border T:1px solid #665757 @ 0.2 / R:1px solid #665757 @ 0.2 / B:1px solid #665757 @ 0.2 / L:1px solid #665757 @ 0.2 r 10px shadow #e3e1dd 0px 2px 0px 0px | button.LoginForm__sso-button__HrA8R.public__sso-button__Kprsc 382.0x44.0 border T:1px solid #665757 @ 0.2 / R:1px solid #665757 @ 0.2 / B:1px solid #665757 @ 0.2 / L:1px solid #665757 @ 0.2 r 10px shadow #e3e1dd 0px 2px 0px 0px outline 5px auto #101010 offset 0px | button.LoginForm__sso-button__HrA8R.public__sso-button__Kprsc 382.0x44.0 bg #f5f3ef border T:1px solid #665757 @ 0.2 / R:1px solid #665757 @ 0.2 / B:1px solid #665757 @ 0.2 / L:1px solid #665757 @ 0.2 r 10px shadow #e3e1dd 0px 2px 0px 0px |
| Ancestor paint | 2 up div.Login__form__S81Mo.public__form-container__srWiu bg #ffffff shadow #e3e1dd 0px 2px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-sso-default.png`, `signin-sso-hover.png`, `signin-sso-focus-visible.png`, `signin-sso-pressed.png`.

#### signin-email

Email field. The email input on the sign-in card; focused locally, never submitted.

Page: signin. Selector: `input[type=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 382 x 44 | = |
| Padding | 0px 15px | = |
| Border | none | = |
| Radius | 10px | = |
| Background | #f5f3ef | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | GT-America 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #2d2323 | = |
| Transition | border-color, box-shadow 0.3s, 0.3s ease-out, ease-out delay 0s, 0s | = |
| Cursor | text | = |
| Placeholder | #2d2323, opacity 1 | = |
| Painted layers | input 382.0x44.0 bg #f5f3ef r 10px | = |
| How | at rest | clicked into the field |

Crops: `signin-email-default.png`, `signin-email-focused.png`.

#### signin-password

Password field. The password input; measured at rest, never typed.

Page: signin. Selector: `input[type=password]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 382 x 44 |
| Padding | 0px 15px |
| Border | none |
| Radius | 10px |
| Background | #f5f3ef |
| Box shadow | none |
| Outline | none |
| Font | GT-America 16px/22px 400 |
| Letter spacing | normal |
| Colour | #2d2323 |
| Transition | border-color, box-shadow 0.3s, 0.3s ease-out, ease-out delay 0s, 0s |
| Cursor | text |
| Placeholder | #2d2323, opacity 1 |
| Painted layers | input 382.0x44.0 bg #f5f3ef r 10px |
| How | at rest |

Crops: `signin-password-default.png`.

#### signin-button

Log-in button. The "Log in" submit-style button (h-button-secondary); measured never pressed.

Page: signin. Selector: `button.h-button-secondary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 382 x 44 | = | = | = |
| Padding | 4px 14px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #4f75fe | #254cda | = | #254cda |
| Box shadow | none | = | #ffffff 0px 0px 0px 1px, #c9d5fd 0px 0px 2px 2px | = |
| Outline | none | = | = | = |
| Font | GT-America 16px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.h-button-content: GT-America 16px/22px 400, #ffffff | = | = | = |
| Transition | background, color 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #ffffff | = | = | = |
| Painted layers | button.h-button.h-button-secondary 382.0x44.0 bg #4f75fe r 10px; div.h-button-icon-wrapper 0.0x0.0 bg #254cda; span::after.h-spinner.h-spinner-small 50%x50% border T:2px solid #ffffff / L:2px solid #ffffff r 100% 0px 0px | button.h-button.h-button-secondary 382.0x44.0 bg #254cda r 10px; div.h-button-icon-wrapper 0.0x0.0 bg #254cda; span::after.h-spinner.h-spinner-small 50%x50% border T:2px solid #ffffff / L:2px solid #ffffff r 100% 0px 0px | button.h-button.h-button-secondary 382.0x44.0 bg #4f75fe r 10px shadow #ffffff 0px 0px 0px 1px, #c9d5fd 0px 0px 2px 2px; div.h-button-icon-wrapper 0.0x0.0 bg #254cda; span::after.h-spinner.h-spinner-small 50%x50% border T:2px solid #ffffff / L:2px solid #ffffff r 100% 0px 0px | button.h-button.h-button-secondary 382.0x44.0 bg #254cda r 10px; div.h-button-icon-wrapper 0.0x0.0 bg #254cda; span::after.h-spinner.h-spinner-small 50%x50% border T:2px solid #ffffff / L:2px solid #ffffff r 100% 0px 0px |
| Ancestor paint | 3 up div.Login__form__S81Mo.public__form-container__srWiu bg #ffffff shadow #e3e1dd 0px 2px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-button-default.png`, `signin-button-hover.png`, `signin-button-focus-visible.png`, `signin-button-pressed.png`.

#### signin-link

Account link. "I don't have an account" / "Forgot your password?" — link-styled controls; measured never followed.

Page: signin. Selector: `a.h-button-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 170 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 1px, #c9d5fd 0px 0px 2px 2px | = |
| Outline | none | = | = | = |
| Font | GT-America 16px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #4f75fe | #254cda | = | #254cda |
| Text node | span.h-button-content: GT-America 16px/22px 400, #4f75fe | span.h-button-content: GT-America 16px/22px 400, #254cda | = | span.h-button-content: GT-America 16px/22px 400, #254cda |
| Transition | color 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.h-button.h-button-link 170.0x22.0 shadow #ffffff 0px 0px 0px 1px, #c9d5fd 0px 0px 2px 2px | = |

Crops: `signin-link-default.png`, `signin-link-hover.png`, `signin-link-focus-visible.png`, `signin-link-pressed.png`.

### HR sign-in (boundary)

#### hr-card

HR sign-in card. The app.homerun.hr logon card (the outermost form container). Measured at rest, never submitted.

Page: signinhr. Selector: `outermost form ancestor of the password input`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 382 x 278 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT-America 16px/24px 400 |
| Letter spacing | normal |
| Colour | #4a3e3e |
| Text node | label.public-form__label: GT-America 16px/24px 300, #4a3e3e |
| Transition | none |
| Painted layers | input.public-form__input 382.0x44.0 bg #f5f3ef r 10px; input.public-form__input 382.0x44.0 bg #f5f3ef r 10px; button.public-form__button.mt-0 382.0x44.0 bg #00b16b r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px |
| Ancestor paint | 3 up div.sm:mx-auto.rounded-b-3xl bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e3e1dd 0px 2px 0px 0px |
| How | at rest |

Crops: `hr-card-default.png`.

#### hr-field

HR email field. The email input (public-form__input); focused locally, never submitted.

Page: signinhr. Selector: `input.public-form__input[type=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 382 x 44 | = |
| Padding | 2px 12px | = |
| Border | none | = |
| Radius | 10px | = |
| Background | #f5f3ef | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px |
| Font | GT-America 16px/40px 400 | = |
| Letter spacing | normal | = |
| Colour | #4a3e3e | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #4a3e3e, opacity 1 | = |
| Painted layers | input.public-form__input 382.0x44.0 bg #f5f3ef r 10px | input.public-form__input 382.0x44.0 bg #f5f3ef r 10px shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field |

Crops: `hr-field-default.png`, `hr-field-focused.png`.

#### hr-password

HR password field. The password input; measured at rest, never typed.

Page: signinhr. Selector: `input.public-form__input[type=password]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 382 x 44 |
| Padding | 2px 12px |
| Border | none |
| Radius | 10px |
| Background | #f5f3ef |
| Box shadow | none |
| Outline | none |
| Font | GT-America 16px/40px 400 |
| Letter spacing | normal |
| Colour | #4a3e3e |
| Transition | none |
| Cursor | text |
| Placeholder | #4a3e3e, opacity 1 |
| Painted layers | input.public-form__input 382.0x44.0 bg #f5f3ef r 10px |
| How | at rest |

Crops: `hr-password-default.png`.

#### hr-button

HR log-in button. The "Log in" button (public-form__button); measured never pressed.

Page: signinhr. Selector: `button.public-form__button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 382 x 44 | = | = | = |
| Padding | 11px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #00b16b | #128053 | = | #128053 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = | = | = |
| Outline | none | = | 2px solid #00b16b offset 2px | = |
| Font | GT-America 16px/22px 300 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.public-form__button.mt-0 382.0x44.0 bg #00b16b r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | button.public-form__button.mt-0 382.0x44.0 bg #128053 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | button.public-form__button.mt-0 382.0x44.0 bg #00b16b r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px outline 2px solid #00b16b offset 2px | button.public-form__button.mt-0 382.0x44.0 bg #128053 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hr-button-default.png`, `hr-button-hover.png`, `hr-button-focus-visible.png`, `hr-button-pressed.png`.

#### hr-link

HR account link. "I don't have an account" / "Forgot your password?" — measured never followed.

Page: signinhr. Selector: `a.public-form__button--link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 170 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | GT-America 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #00b16b | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.public-form__button--link.mt-0 170.0x24.0 outline 1px auto #101010 offset 1px | = |

Crops: `hr-link-default.png`, `hr-link-hover.png`, `hr-link-focus-visible.png`, `hr-link-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile bar. The 390 mobile nav bar: logo + hamburger + trial button.

Page: home. Selector: `.nav-new.is-mobile at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | GT America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #4a3e3e |
| Text node | div: GT America 16px/32px 400, #ffffff |
| Transition | none |
| Icon | 0 x 0, colour #4a3e3e |
| Painted layers | div.nav-primary.is-new 390.0x72.0 bg #ffffff; div.nav-primary.is-new 390.0x72.0 bg #ffffff; div.nav-new.is-v2 0.0x0.0 bg #ffffff r 60px; div.mobilenav-bar-menu-icon-v2.new 0.0x0.0 bg #ffffff @ 0 image linear-gradient(#ffffff, #ffffff) r 8px; div.nav-line 0.0x0.0 bg #2d2323; div.nav-line 0.0x0.0 bg #2d2323 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The hamburger (the painted w-nav-button copy); its own press opens the menu sheet.

Page: home. Selector: `visible .w-nav-button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 39.19 x 40 |
| Padding | 0px 10px |
| Border | none |
| Radius | 8px |
| Background | #ffffff @ 0 |
| Background image | linear-gradient(#ffffff, #ffffff) |
| Box shadow | none |
| Outline | none |
| Font | GT America 18px/20px 400 |
| Letter spacing | normal |
| Colour | #4e101f |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.mobilenav-bar-menu-icon-v2.new 39.2x40.0 bg #ffffff @ 0 image linear-gradient(#ffffff, #ffffff) r 8px; div.nav-line 19.2x2.0 bg #2d2323; div.nav-line 19.2x2.0 bg #2d2323; div.nav-line 19.2x2.0 bg #2d2323 |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The opened mobile menu sheet after the hamburger press.

Page: home. Selector: `.nav_menu-new.is-mobile after toggle press`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 451 |
| Padding | 0px 0px 64px 0px |
| Border | 1px solid #edebe7 |
| Radius | 20px |
| Background | #ffffff |
| Box shadow | #43413d @ 0.15 0px 5px 20px 0px |
| Outline | none |
| Font | GT America 14px/20px 400 |
| Letter spacing | normal |
| Colour | #4a3e3e |
| Text node | div: GT America 16px/22px 400, #4a3e3e |
| Transition | all, transform 0s, 0.4s ease, ease delay 0s, 0s |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 42 x 28, colour #4a3e3e |
| Painted layers | nav.nav_menu-new.is-mobile 358.0x451.0 bg #ffffff border T:1px solid #edebe7 / R:1px solid #edebe7 / B:1px solid #edebe7 / L:1px solid #edebe7 r 20px shadow #43413d @ 0.15 0px 5px 20px 0px; div.new-menu_container.is-mobile 356.0x385.0 bg #ffffff r 24px; nav.nav_dropdown-list-v2.resources 0.0x0.0 bg #dddddd border T:1px solid #f5f3ef / R:1px solid #f5f3ef / B:1px solid #f5f3ef / L:1px solid #f5f3ef r 10px; div.nav_resources-update 0.0x0.0 bg #ffffff @ 0; a::before.nav_resources-link.is-order-3 autox1px bg #edebe7; a::before.nav_resources-link.is-order-3 autox1px bg #edebe7 |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-menu-link

Menu link. A link row inside the open mobile menu.

Page: home. Selector: `first link inside the open menu`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 324 x 60 | = | = | = |
| Padding | 16px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | #f5f3ef | #f5f3ef | #f5f3ef |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | GT America 16px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #4a3e3e | = | = | = |
| Text node | div: GT America 16px/22px 400, #4a3e3e | = | = | = |
| Transition | background-color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 42 x 28, colour #4a3e3e | 42 x 28, colour #4f75fe | 42 x 28, colour #4f75fe | 42 x 28, colour #4f75fe |
| Ancestor paint | 3 up nav.nav_menu-new.is-mobile bg #ffffff shadow #43413d @ 0.15 0px 5px 20px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.nav_link-new.is-icon 324.0x60.0 bg #f5f3ef r 10px | a.nav_link-new.is-icon 324.0x60.0 bg #f5f3ef r 10px | a.nav_link-new.is-icon 324.0x60.0 bg #f5f3ef r 10px |

Crops: `m-menu-link-default.png`, `m-menu-link-hover.png`, `m-menu-link-focus-visible.png`, `m-menu-link-pressed.png`.

#### m-hero

Mobile headline. The hero headline at 390.

Page: home. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 322.19 x 160 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Walsheim 40px/40px 900 |
| Letter spacing | normal |
| Colour | #382d2d |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

Homerun's marketing site is a Webflow build whose shared CDN stylesheet is CSSOM-readable, so this list holds that sheet's declared transitions plus whatever else the CSSOM could read on each page; the per-state Transition rows above are computed values and cover every surface.

- home: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `background-color 0.2s`, `0.2s`, `opacity 0.2s`, `transform 0.2s`, `background-color 0.2s, color 0.2s`, `border 0.2s, transform 0.2s`, `border 0.2s`, `box-shadow 0.2s, transform 0.2s`, `0.1s`
