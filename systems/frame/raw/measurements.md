# Frame.io component measurements

Computed styles read from frame.io on 2026-11-16 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the dark marketing pages (home, pricing, contact, contact/form, customers, the Ford case study, integrations and what's-new), the light sign-in surface at accounts.frame.io/welcome (a separate styled-components stack that shares none of the marketing site's custom properties), and the mobile nav overlay — with the cookie consent layer hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). frame.io exposes no signed-out theme switch; the marketing pages paint the one dark theme and the welcome page paints its own light theme. One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into and left empty; `filled` is not captured, because nothing is typed; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Site chrome (header, announcement, nav, footer)

#### mkt-header

Site header. The fixed top bar on every public page (header is a 0-height sentinel; the painted bar is nav.mainNavigation, 80px under the 36px announcement strip): the Frame.io mark, the Features/Enterprise/Resources mega-menu triggers, Pricing, Contact Us, Sign In and the "Start Free Trial" pill.

Page: home. Selector: `nav[class*=mainNavigation]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times New Roman 10px/10px 400 |
| Letter spacing | normal |
| Colour | #fcfcfc |
| Text node | span.Navigation_navigationMainItemInner__mMl9H: FrameGothic 14px/13.44px 600, #fcfcfc, ls 0.14px |
| Transition | none |
| Icon | 30 x 34, colour #fcfcfc |
| Painted layers | a::before.Button_white__XYP1F.Button_base__1G9eD 155.25pxx37.75px bg #f5f5f8 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px; figure.Navigation_backdrop__xQNG2 1440.0x80.0 bg #0d0d18 @ 0.3 |
| How | at rest |

Crops: `mkt-header-default.png`.

#### page-field

Page field. The near-black field the whole public site paints (the html background layer; body is transparent over it).

Page: home. Selector: `html`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 11936.91 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | Times New Roman 10px/normal 400 |
| Letter spacing | normal |
| Colour | #fcfcfc |
| Text node | a: FrameGothic 12px/12px 600, #fcfcfc, ls 0.12px |
| Transition | none |
| Icon | 24 x 24, colour #fcfcfc |
| Painted layers | html.__variable_9d88cd.__variable_5c99cd 1440.0x11936.9 bg #000000; div.AnnouncementBanner_announcementBanner__g9QLM.Navigation_navigationBannerEl__zSvOh 1440.0x36.0 bg #5b53ff image linear-gradient(355deg, #ffffff @ 0.15 4.03%, #ffffff @ 0 95.81%), none; a::before.Button_white__XYP1F.Button_base__1G9eD 155.25pxx37.75px bg #f5f5f8 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px |
| How | at rest |

Crops: none.

#### mkt-logo

Logo. The Frame.io waveform mark in the header, linking home.

Page: home. Selector: `mainNavigation a[href=/]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 30 x 34 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times New Roman 10px/10px 400 |
| Letter spacing | normal |
| Colour | #fcfcfc |
| Transition | none |
| Cursor | pointer |
| Icon | 30 x 34, colour #fcfcfc |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### announcement

Announcement banner. The site-wide promo strip above the header ("Put your creative context to work with new AI-powered capabilities →") — real chrome, never hidden.

Page: home. Selector: `[class*=AnnouncementBanner]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 36 |
| Padding | 12px 24px |
| Border | none |
| Radius | 0px |
| Background | #5b53ff |
| Background image | linear-gradient(355deg, #ffffff @ 0.15 4.03%, #ffffff @ 0 95.81%), none |
| Box shadow | none |
| Outline | none |
| Font | Times New Roman 10px/10px 400 |
| Letter spacing | normal |
| Colour | #fcfcfc |
| Text node | a: FrameGothic 12px/12px 600, #fcfcfc, ls 0.12px |
| Transition | none |
| Icon | 24 x 24, colour #fcfcfc |
| Painted layers | div.AnnouncementBanner_announcementBanner__g9QLM.Navigation_navigationBannerEl__zSvOh 1440.0x36.0 bg #5b53ff image linear-gradient(355deg, #ffffff @ 0.15 4.03%, #ffffff @ 0 95.81%), none |
| How | at rest |

Crops: `announcement-default.png`.

#### nav-trigger

Mega-menu trigger. The "Features" header button — click opens the mega-menu (the group gains NavGroup_open__ and the nav Navigation_subNavOpen__; hovering does not open it). The opened state was measured after its own toggle click.

Page: home. Selector: `button[class*=navigationMainItem] Features`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 83.92 x 80 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px dotted #fcfcfc offset 0px | = | = |
| Font | FrameGothic 14px/13.44px 600 | = | = | = | = |
| Letter spacing | 0.14px | = | = | = | = |
| Colour | #fcfcfc | = | = | = | = |
| Text node | span.Navigation_navigationMainItemInner__mMl9H: FrameGothic 14px/13.44px 600, #fcfcfc, ls 0.14px | = | = | = | = |
| Transition | color 0.3s cubic-bezier(0.28, 0.44, 0.49, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 9.8 x 9.8, colour #fcfcfc | = | = | = | 12.94 x 12.94, colour #fcfcfc |
| ::before | 111.922px x 80px, absolute, bg #000000 @ 0, radius 0px | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | button.Navigation_navigationMainItem__pIZar.typography_navigation__70PKN 83.9x80.0 outline 1px dotted #fcfcfc offset 0px | = | = |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`, `nav-trigger-opened.png`.

#### nav-panel

Mega-menu panel. The Features mega-menu opened by its trigger (Workflow Management, File Management, Share & Present, Review & Approvals, Camera to Cloud, Integrations, Mounted Storage, Frame.io Drive); its links were never followed.

Page: home. Selector: `[class*=navGroupSubnav] open`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 604.5 |
| Padding | 176px 0px 106px 0px |
| Gap | normal 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times New Roman 10px/10px 400 |
| Letter spacing | normal |
| Colour | #fcfcfc |
| Text node | h2.NavGroup_navGroupLabel__5qD6W.typography_title2__Ry8_z: FrameGothic 48px/48.96px 600, #fcfcfc, ls -1.92px |
| Transition | none |
| Icon | 0 x 0, colour #fcfcfc |
| How | at rest |

Crops: `nav-panel-default.png`.

#### nav-menu-item

Mega-menu item. A destination row inside the opened mega-menu; measured, never followed.

Page: home. Selector: `mega-menu item`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 360 x 49.19 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | NeueMachinaInktrap 12px/10.8px 400 | = |
| Letter spacing | 0.72px | = |
| Colour | #fcfcfc | = |
| Text node | span.NavGroup_navGroupSubcategoryItemInnerContent__hRPQ5.listItemsByIndex_listItemsByIndexItemInner__MLJxI: FrameGothic 24px/31.2px 400, #fcfcfc | = |
| Transition | color 0.6s cubic-bezier(0.28, 0.44, 0.49, 1) | color 0.3s cubic-bezier(0.28, 0.44, 0.49, 1) |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = |
| Cursor | pointer | = |
| ::before | 16.4531px x 10.7969px, static, bg #000000 @ 0, radius 0px | = |
| How | at rest | mouse hover |

Crops: `nav-menu-item-default.png`, `nav-menu-item-hover.png`.

#### nav-pricing

Nav link. The "Pricing" header link; measured, never followed.

Page: home. Selector: `header a Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48.98 x 80 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #fcfcfc offset 1px | = |
| Font | FrameGothic 14px/13.44px 600 | = | = | = |
| Letter spacing | 0.14px | = | = | = |
| Colour | #fcfcfc | = | = | = |
| Text node | span: FrameGothic 14px/13.44px 600, #fcfcfc, ls 0.14px | = | = | = |
| Transition | color 0.3s cubic-bezier(0.28, 0.44, 0.49, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 76.9844px x 80px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.Navigation_navigationMainItem__pIZar.typography_navigation__70PKN 49.0x80.0 outline 1px dotted #fcfcfc offset 1px | = |

Crops: `nav-pricing-default.png`, `nav-pricing-hover.png`, `nav-pricing-focus-visible.png`, `nav-pricing-pressed.png`.

#### nav-contact

Contact Us link. The "Contact Us" header link; measured, never followed.

Page: home. Selector: `header a Contact Us`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81 x 13.44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #fcfcfc offset 1px | = |
| Font | FrameGothic 14px/13.44px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fcfcfc | = | = | = |
| Text node | span: FrameGothic 14px/13.44px 600, #fcfcfc | = | = | = |
| Transition | color 0.3s cubic-bezier(0.28, 0.44, 0.49, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 109px x 13.4375px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.NavItem_isReducedNavNavItem__kqUAm.typography_reducedNavigation__4_qzl 81.0x13.4 outline 1px dotted #fcfcfc offset 1px | = |

Crops: `nav-contact-default.png`, `nav-contact-hover.png`, `nav-contact-focus-visible.png`, `nav-contact-pressed.png`.

#### nav-signin

Sign In link. The "Sign In" header link to app.frame.io (which redirects to the accounts.frame.io/welcome sign-in surface); measured, never followed.

Page: home. Selector: `header a Sign In`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44.98 x 13.44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #fcfcfc offset 1px | = |
| Font | FrameGothic 14px/13.44px 600 | = | = | = |
| Letter spacing | 0.14px | = | = | = |
| Colour | #fcfcfc | = | = | = |
| Text node | span: FrameGothic 14px/13.44px 600, #fcfcfc, ls 0.14px | = | = | = |
| Transition | color 0.3s cubic-bezier(0.28, 0.44, 0.49, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 72.9844px x 13.4375px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.Navigation_navigationMainItem__pIZar.typography_navigation__70PKN 45.0x13.4 outline 1px dotted #fcfcfc offset 1px | = |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-cta

Header CTA. The white "Start Free Trial" header pill; links to the trial sign-up, measured never followed.

Page: home. Selector: `header a Start Free Trial`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 157.25 x 39.75 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #fcfcfc offset 1px | = |
| Font | FrameGothic 14px/13.44px 600 | = | = | = |
| Letter spacing | 0.14px | = | = | = |
| Colour | #000000 | = | = | #fcfcfc |
| Text node | span.Button_buttonText__Yzd9S: FrameGothic 14px/13.44px 600, #000000, ls 0.14px | = | = | span.Button_buttonText__Yzd9S: FrameGothic 14px/13.44px 600, #fcfcfc, ls 0.14px |
| Transition | color 0.3s cubic-bezier(0, 0.44, 0.6, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 155.25px x 37.75px, absolute, bg #f5f5f8, radius 100px | 155.25px x 37.75px, absolute, bg #e9e9ff @ 0.7, radius 100px | 155.25px x 37.75px, absolute, bg #e9e9ff @ 0.7, radius 100px | 157.25px x 39.75px, absolute, bg #000000 @ 0, radius 100px |
| ::after | 157.25px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #c1c2d9 0px 0px 0px 2px inset | 157.25px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #fcfcfc 0px 0px 0px 2px inset | = | 157.25px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #d1d1fb @ 0.2 0px 0px 0px 4px inset |
| Painted layers | a::before.Button_white__XYP1F.Button_base__1G9eD 155.25pxx37.75px bg #f5f5f8 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px | a::before.Button_white__XYP1F.Button_base__1G9eD 155.25pxx37.75px bg #e9e9ff @ 0.7 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px; a::after.Button_white__XYP1F.Button_base__1G9eD 157.25pxx39.75px r 100px shadow #fcfcfc 0px 0px 0px 2px inset | a.Button_white__XYP1F.Button_base__1G9eD 157.3x39.8 r 100px outline 1px dotted #fcfcfc offset 1px; a::before.Button_white__XYP1F.Button_base__1G9eD 155.25pxx37.75px bg #e9e9ff @ 0.7 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px | a::after.Button_white__XYP1F.Button_base__1G9eD 157.25pxx39.75px r 100px shadow #d1d1fb @ 0.2 0px 0px 0px 4px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### footer

Site footer. The dark footer on every public page: link columns, legal row, "Cookie preferences" and the language selector.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 838.39 |
| Padding | 96px 0px 48px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times New Roman 10px/10px 400 |
| Letter spacing | normal |
| Colour | #fcfcfc |
| Text node | p.FooterGroup_groupLabel__jg7Ks.typography_eyebrow__vJy3S: NeueMachinaInktrap 12px/10.8px 400, #e9e9ff @ 0.7, ls 0.72px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, -14.598) |
| Icon | 30 x 34, colour #fcfcfc |
| Painted layers | div::before.Footer_rowSecondary__dHZWA.global_grid__4e_JW 1080pxx2px bg #bdbdf4 @ 0.1 r 2px; div.Footer_backdrop__Asw9G 1440.0x838.4 bg #0d0d18 @ 0.8 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A legal/support link in the footer; measured, never followed.

Page: home. Selector: `footer a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 87 x 36 | = |
| Padding | 0px 24px 16px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | FrameGothic 16px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #fcfcfc | = |
| Transition | color 0.3s cubic-bezier(0.28, 0.44, 0.49, 1) | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`.

#### locale-btn

Language selector. The "English (US)" footer trigger (LanguageSelector_trigger); measured at rest, never opened.

Page: home. Selector: `footer English (US)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 120 x 32 | = | = | = |
| Padding | 4px 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 5px | = | = | = |
| Background | transparent | #9d9dff @ 0.05 | = | #9d9dff @ 0.05 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #5b53ff offset 2px | = |
| Font | FrameGothic 10px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6a6b83 | #fcfcfc | = | #fcfcfc |
| Transition | color, background-color 0.2s, 0.2s cubic-bezier(0.25, 0.1, 0.25, 1), cubic-bezier(0.25, 0.1, 0.25, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #6a6b83 | 16 x 16, colour #fcfcfc | = | 16 x 16, colour #fcfcfc |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.LanguageSelector_trigger__IwXGd.typography_footnote__h8r_U 120.0x32.0 bg #9d9dff @ 0.05 r 5px | button.LanguageSelector_trigger__IwXGd.typography_footnote__h8r_U 120.0x32.0 r 5px outline 2px solid #5b53ff offset 2px | button.LanguageSelector_trigger__IwXGd.typography_footnote__h8r_U 120.0x32.0 bg #9d9dff @ 0.05 r 5px |

Crops: `locale-btn-default.png`, `locale-btn-hover.png`, `locale-btn-focus-visible.png`, `locale-btn-pressed.png`.

#### cookie-prefs

Cookie preferences. The footer "Cookie preferences" button, which mounts the consent manager on demand; measured at rest, never pressed.

Page: home. Selector: `footer Cookie preferences`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 93 x 12 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #fcfcfc offset 0px | = |
| Font | FrameGothic 10px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fcfcfc | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.Footer_bottomLeftItem__EmEaX.typography_footnote__h8r_U 93.0x12.0 outline 1px dotted #fcfcfc offset 0px | = |

Crops: `cookie-prefs-default.png`, `cookie-prefs-hover.png`, `cookie-prefs-focus-visible.png`, `cookie-prefs-pressed.png`.

### Home

#### hero-h1

Hero headline. "One platform for all your creative work." — the frame.io hero display heading in FrameGothic 80px.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 504 x 249.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | FrameGothic 80px/83.2px 600 |
| Letter spacing | -3.6px |
| Colour | #fcfcfc |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-cta

Hero CTA. The hero "Start Free Trial" button; measured, never followed.

Page: home. Selector: `main Start Free Trial`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 157.25 x 39.75 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #fcfcfc offset 1px | = |
| Font | FrameGothic 14px/13.44px 600 | = | = | = |
| Letter spacing | 0.14px | = | = | = |
| Colour | #000000 | = | = | #fcfcfc |
| Text node | span.Button_buttonText__Yzd9S: FrameGothic 14px/13.44px 600, #000000, ls 0.14px | = | = | span.Button_buttonText__Yzd9S: FrameGothic 14px/13.44px 600, #fcfcfc, ls 0.14px |
| Transition | color 0.3s cubic-bezier(0, 0.44, 0.6, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 155.25px x 37.75px, absolute, bg #f5f5f8, radius 100px | 155.25px x 37.75px, absolute, bg #e9e9ff @ 0.7, radius 100px | 155.25px x 37.75px, absolute, bg #e9e9ff @ 0.7, radius 100px | 157.25px x 39.75px, absolute, bg #000000 @ 0, radius 100px |
| ::after | 157.25px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #c1c2d9 0px 0px 0px 2px inset | 157.25px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #fcfcfc 0px 0px 0px 2px inset | = | 157.25px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #d1d1fb @ 0.2 0px 0px 0px 4px inset |
| Painted layers | a::before.Button_white__XYP1F.Button_base__1G9eD 155.25pxx37.75px bg #f5f5f8 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px | a::before.Button_white__XYP1F.Button_base__1G9eD 155.25pxx37.75px bg #e9e9ff @ 0.7 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px; a::after.Button_white__XYP1F.Button_base__1G9eD 157.25pxx39.75px r 100px shadow #fcfcfc 0px 0px 0px 2px inset | a.Button_white__XYP1F.Button_base__1G9eD 157.3x39.8 r 100px outline 1px dotted #fcfcfc offset 1px; a::before.Button_white__XYP1F.Button_base__1G9eD 155.25pxx37.75px bg #e9e9ff @ 0.7 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px | a::after.Button_white__XYP1F.Button_base__1G9eD 157.25pxx39.75px r 100px shadow #d1d1fb @ 0.2 0px 0px 0px 4px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-tour

Hero secondary action. The hero "Take a Product Tour" ghost button; measured, never followed.

Page: home. Selector: `main Take a Product Tour`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 208.67 x 39.75 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #fcfcfc offset 1px | = |
| Font | FrameGothic 14px/13.44px 600 | = | = | = |
| Letter spacing | 0.14px | = | = | = |
| Colour | #fcfcfc | = | = | = |
| Text node | span.Button_buttonText__Yzd9S: FrameGothic 14px/13.44px 600, #fcfcfc, ls 0.14px | = | = | = |
| Transition | color 0.3s cubic-bezier(0, 0.44, 0.6, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 4.44 x 7.5, colour #fcfcfc | = | = | = |
| ::before | 208.672px x 39.75px, absolute, bg #d1d1fb @ 0.2, radius 100px | 208.672px x 39.75px, absolute, bg #dcdcff @ 0.3, radius 100px | 208.672px x 39.75px, absolute, bg #dcdcff @ 0.298, radius 100px | 208.672px x 39.75px, absolute, bg #000000 @ 0, radius 100px |
| ::after | 208.672px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #9d9dff @ 0.05 0px 0px 0px 1px inset | 208.672px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #bdbdf4 @ 0.1 0px 0px 0px 2px inset | = | 208.672px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #d1d1fb @ 0.2 0px 0px 0px 4px inset |
| Painted layers | a::before.Button_glass__B8SwH.Button_base__1G9eD 208.672pxx39.75px bg #d1d1fb @ 0.2 r 100px; a::after.Button_glass__B8SwH.Button_base__1G9eD 208.672pxx39.75px r 100px shadow #9d9dff @ 0.05 0px 0px 0px 1px inset; span::after.AnimatedSvgArrow_cssTail__yibfW 20pxx1.65625px bg #f5f5f8 r 1px | a::before.Button_glass__B8SwH.Button_base__1G9eD 208.672pxx39.75px bg #dcdcff @ 0.3 r 100px; a::after.Button_glass__B8SwH.Button_base__1G9eD 208.672pxx39.75px r 100px shadow #bdbdf4 @ 0.1 0px 0px 0px 2px inset; span::after.AnimatedSvgArrow_cssTail__yibfW 20pxx1.65625px bg #f5f5f8 r 1px | a.Button_glass__B8SwH.Button_base__1G9eD 208.7x39.8 r 100px outline 1px dotted #fcfcfc offset 1px; a::before.Button_glass__B8SwH.Button_base__1G9eD 208.672pxx39.75px bg #dcdcff @ 0.298 r 100px; a::after.Button_glass__B8SwH.Button_base__1G9eD 208.672pxx39.75px r 100px shadow #9d9dff @ 0.05 0px 0px 0px 1px inset; span::after.AnimatedSvgArrow_cssTail__yibfW 20pxx1.65625px bg #f5f5f8 r 1px | a::after.Button_glass__B8SwH.Button_base__1G9eD 208.672pxx39.75px r 100px shadow #d1d1fb @ 0.2 0px 0px 0px 4px inset; span::after.AnimatedSvgArrow_cssTail__yibfW 20pxx1.65625px bg #f5f5f8 r 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-tour-default.png`, `hero-tour-hover.png`, `hero-tour-focus-visible.png`, `hero-tour-pressed.png`.

#### section-h2

Section headline. A section heading on the home page; first visible h2.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 896 x 97.91 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | FrameGothic 48px/48.96px 600 |
| Letter spacing | -1.92px |
| Colour | #eaeaff @ 0.5 |
| Text node | span: FrameGothic 48px/48.96px 600, #eaeaff @ 0.5, ls -1.92px |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

### Pricing

#### price-h1

Pricing headline. The /pricing masthead.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 804 x 166.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | FrameGothic 80px/83.2px 600 |
| Letter spacing | -3.6px |
| Colour | #fcfcfc |
| Transition | none |
| How | at rest |

Crops: `price-h1-default.png`.

#### price-toggle

Billing toggle. The "Monthly" side of the Monthly/Annually billing switch — a pair of round radio controls (a 24px circle ringed grey-60, a 10px turquoise-triumph dot on the selected side), not a segmented pill; a local UI toggle, measured at rest — the alternate price state was not toggled.

Page: pricing. Selector: `billing Monthly control`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 91.98 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #fcfcfc offset 0px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fcfcfc | = | = | = |
| Text node | span.RadioButtons_radioButtonTitle__j2ltU.typography_button__Uyx6e: FrameGothic 14px/13.44px 600, #fcfcfc, ls 0.14px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | figure.RadioButtons_radioButtonIcon__ih70y 24.0x24.0 border T:1px solid #81859f / R:1px solid #81859f / B:1px solid #81859f / L:1px solid #81859f r 12px; figure::after.RadioButtons_radioButtonIcon__ih70y 10pxx10px bg #6199f6 r 5px | = | button.RadioButtons_radioButtonInner__TrHlG 92.0x24.0 outline 1px dotted #fcfcfc offset 0px; figure.RadioButtons_radioButtonIcon__ih70y 24.0x24.0 border T:1px solid #81859f / R:1px solid #81859f / B:1px solid #81859f / L:1px solid #81859f r 12px; figure::after.RadioButtons_radioButtonIcon__ih70y 10pxx10px bg #6199f6 r 5px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `price-toggle-default.png`, `price-toggle-hover.png`, `price-toggle-focus-visible.png`, `price-toggle-pressed.png`.

#### price-toggle-alt

Billing toggle (annual). The "Annually — SAVE 13%" side of the billing switch — the same round radio control, measured at rest, never toggled.

Page: pricing. Selector: `billing Annually control`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 174.86 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #fcfcfc offset 0px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fcfcfc | = | = | = |
| Text node | span.RadioButtons_radioButtonTitle__j2ltU.typography_button__Uyx6e: FrameGothic 14px/13.44px 600, #fcfcfc, ls 0.14px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | figure.RadioButtons_radioButtonIcon__ih70y 24.0x24.0 border T:1px solid #81859f / R:1px solid #81859f / B:1px solid #81859f / L:1px solid #81859f r 12px; span.RadioButtons_radioButtonSubtitle__g5iTZ.typography_button__Uyx6e 72.7x14.6 bg #6199f6 border T:1px solid #6199f6 / R:1px solid #6199f6 / B:1px solid #6199f6 / L:1px solid #6199f6 r 100px | = | button.RadioButtons_radioButtonInner__TrHlG 174.9x24.0 outline 1px dotted #fcfcfc offset 0px; figure.RadioButtons_radioButtonIcon__ih70y 24.0x24.0 border T:1px solid #81859f / R:1px solid #81859f / B:1px solid #81859f / L:1px solid #81859f r 12px; span.RadioButtons_radioButtonSubtitle__g5iTZ.typography_button__Uyx6e 72.7x14.6 bg #6199f6 border T:1px solid #6199f6 / R:1px solid #6199f6 / B:1px solid #6199f6 / L:1px solid #6199f6 r 100px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `price-toggle-alt-default.png`, `price-toggle-alt-hover.png`, `price-toggle-alt-focus-visible.png`, `price-toggle-alt-pressed.png`.

#### plan-card

Plan card. A pricing plan card (Free / Pro / Team / Enterprise, $0–$25 monthly); the card wrapping a "Sign Up Now" CTA.

Page: pricing. Selector: `[class*=PricingCard_pricingCard__]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 252 x 796.59 |
| Padding | 24px |
| Border | 1px solid #9d9dff @ 0.1 |
| Radius | 10px |
| Background | #101017 @ 0.5 |
| Box shadow | #181826 12px 12px 50px 0px inset, #000000 @ 0.31 84.68px 149.711px 80px 0px, #000000 @ 0.26 54.885px 97.035px 46.852px 0px, #000000 @ 0.23 32.618px 57.666px 25.481px 0px, #000000 @ 0.2 16.936px 29.942px 13px 0px, #000000 @ 0.18 6.9px 12.199px 6.519px 0px, #000000 @ 0.2 1.568px 2.772px 3.148px 0px |
| Backdrop filter | blur(75px) |
| Outline | none |
| Font | Times New Roman 10px/10px 400 |
| Letter spacing | normal |
| Colour | #fcfcfc |
| Text node | div.PricingCard_cardEyebrow__WHDag.typography_eyebrow__vJy3S: NeueMachinaInktrap 12px/10.8px 400, #6199f6, ls 0.72px |
| Transition | none |
| Icon | 16 x 17, colour #fcfcfc |
| Painted layers | div.PricingCard_pricingCard__iX2Cv.PricingCard_pricingCardColumns4__WxrbD 252.0x796.6 bg #101017 @ 0.5 border T:1px solid #9d9dff @ 0.1 / R:1px solid #9d9dff @ 0.1 / B:1px solid #9d9dff @ 0.1 / L:1px solid #9d9dff @ 0.1 r 10px shadow #181826 12px 12px 50px 0px inset, #000000 @ 0.31 84.68px 149.711px 80px 0px, #000000 @ 0.26 54.885px 97.035px 46.852px 0px, #000000 @ 0.23 32.618px 57.666px 25.481px 0px, #000000 @ 0.2 16.936px 29.942px 13px 0px, #000000 @ 0.18 6.9px 12.199px 6.519px 0px, #000000 @ 0.2 1.568px 2.772px 3.148px 0px; div.PricingCard_cardDescription__l9bxj.typography_body__vVxn5 202.0x114.3 border T:1px solid #d1d1fb @ 0.2; a::before.Button_white__XYP1F.Button_base__1G9eD 200pxx37.75px bg #f5f5f8 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-signup

Plan CTA. A plan card's "Sign Up Now" button; measured, never followed or clicked (it begins account creation).

Page: pricing. Selector: `plan Sign Up Now`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 202 x 39.75 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #fcfcfc offset 1px | = |
| Font | FrameGothic 14px/13.44px 600 | = | = | = |
| Letter spacing | 0.14px | = | = | = |
| Colour | #000000 | = | = | #a3a3a3 |
| Text node | span.Button_buttonText__Yzd9S: FrameGothic 14px/13.44px 600, #000000, ls 0.14px | = | = | span.Button_buttonText__Yzd9S: FrameGothic 14px/13.44px 600, #a3a3a3, ls 0.14px |
| Transition | color 0.3s cubic-bezier(0, 0.44, 0.6, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 200px x 37.75px, absolute, bg #f5f5f8, radius 100px | = | 200px x 37.75px, absolute, bg #e9e9ff @ 0.706, radius 100px | 202px x 39.75px, absolute, bg #f5f5f8 @ 0.353, radius 100px |
| ::after | 202px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #c1c2d9 0px 0px 0px 2px inset | 202px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #fcfcfc 0px 0px 0px 2px inset | = | 202px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #d1d1fb @ 0.2 0px 0px 0px 4px inset |
| Painted layers | a::before.Button_white__XYP1F.Button_base__1G9eD 200pxx37.75px bg #f5f5f8 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px | = | a.Button_white__XYP1F.Button_base__1G9eD 202.0x39.8 r 100px outline 1px dotted #fcfcfc offset 1px; a::before.Button_white__XYP1F.Button_base__1G9eD 200pxx37.75px bg #e9e9ff @ 0.706 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px | a::before.Button_white__XYP1F.Button_base__1G9eD 202pxx39.75px bg #f5f5f8 @ 0.353 r 100px; a::after.Button_white__XYP1F.Button_base__1G9eD 202pxx39.75px r 100px shadow #d1d1fb @ 0.2 0px 0px 0px 4px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-signup-default.png`, `plan-signup-hover.png`, `plan-signup-focus-visible.png`, `plan-signup-pressed.png`.

#### plan-trial

Plan trial CTA. A plan card's "Start Free Trial" button; measured, never followed.

Page: pricing. Selector: `plan Start Free Trial`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 202 x 39.75 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #fcfcfc offset 1px | = |
| Font | FrameGothic 14px/13.44px 600 | = | = | = |
| Letter spacing | 0.14px | = | = | = |
| Colour | #000000 | = | = | #fcfcfc |
| Text node | span.Button_buttonText__Yzd9S: FrameGothic 14px/13.44px 600, #000000, ls 0.14px | = | = | span.Button_buttonText__Yzd9S: FrameGothic 14px/13.44px 600, #fcfcfc, ls 0.14px |
| Transition | color 0.3s cubic-bezier(0, 0.44, 0.6, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 200px x 37.75px, absolute, bg #f5f5f8, radius 100px | 200px x 37.75px, absolute, bg #e9e9ff @ 0.7, radius 100px | 200px x 37.75px, absolute, bg #f0f0fb @ 0.843, radius 100px | 202px x 39.75px, absolute, bg #000000 @ 0, radius 100px |
| ::after | 202px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #c1c2d9 0px 0px 0px 2px inset | 202px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #fcfcfc 0px 0px 0px 2px inset | = | 202px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #d1d1fb @ 0.2 0px 0px 0px 4px inset |
| Painted layers | a::before.Button_white__XYP1F.Button_base__1G9eD 200pxx37.75px bg #f5f5f8 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px | a::before.Button_white__XYP1F.Button_base__1G9eD 200pxx37.75px bg #e9e9ff @ 0.7 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px; a::after.Button_white__XYP1F.Button_base__1G9eD 202pxx39.75px r 100px shadow #fcfcfc 0px 0px 0px 2px inset | a.Button_white__XYP1F.Button_base__1G9eD 202.0x39.8 r 100px outline 1px dotted #fcfcfc offset 1px; a::before.Button_white__XYP1F.Button_base__1G9eD 200pxx37.75px bg #f0f0fb @ 0.843 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px | a::after.Button_white__XYP1F.Button_base__1G9eD 202pxx39.75px r 100px shadow #d1d1fb @ 0.2 0px 0px 0px 4px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-trial-default.png`, `plan-trial-hover.png`, `plan-trial-focus-visible.png`, `plan-trial-pressed.png`.

#### plan-meeting

Plan meeting CTA. The Enterprise card's "Book a Meeting" button; measured, never followed.

Page: pricing. Selector: `plan Book a Meeting`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 202 x 39.75 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #fcfcfc offset 0px | = |
| Font | FrameGothic 14px/13.44px 600 | = | = | = |
| Letter spacing | 0.14px | = | = | = |
| Colour | #000000 | = | = | #eaeaea |
| Text node | span.Button_buttonText__Yzd9S: FrameGothic 14px/13.44px 600, #000000, ls 0.14px | = | = | span.Button_buttonText__Yzd9S: FrameGothic 14px/13.44px 600, #eaeaea, ls 0.14px |
| Transition | color 0.3s cubic-bezier(0, 0.44, 0.6, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 200px x 37.75px, absolute, bg #f5f5f8, radius 100px | 200px x 37.75px, absolute, bg #e9e9ff @ 0.7, radius 100px | 200px x 37.75px, absolute, bg #ededfd @ 0.776, radius 100px | 202px x 39.75px, absolute, bg #f5f5f8 @ 0.07, radius 100px |
| ::after | 202px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #c1c2d9 0px 0px 0px 2px inset | 202px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #fcfcfc 0px 0px 0px 2px inset | = | 202px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #d1d1fb @ 0.2 0px 0px 0px 4px inset |
| Painted layers | button::before.Button_white__XYP1F.Button_base__1G9eD 200pxx37.75px bg #f5f5f8 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px | button::before.Button_white__XYP1F.Button_base__1G9eD 200pxx37.75px bg #e9e9ff @ 0.7 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px; button::after.Button_white__XYP1F.Button_base__1G9eD 202pxx39.75px r 100px shadow #fcfcfc 0px 0px 0px 2px inset | button.Button_white__XYP1F.Button_base__1G9eD 202.0x39.8 r 100px outline 1px dotted #fcfcfc offset 0px; button::before.Button_white__XYP1F.Button_base__1G9eD 200pxx37.75px bg #ededfd @ 0.776 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px | button::before.Button_white__XYP1F.Button_base__1G9eD 202pxx39.75px bg #f5f5f8 @ 0.07 r 100px; button::after.Button_white__XYP1F.Button_base__1G9eD 202pxx39.75px r 100px shadow #d1d1fb @ 0.2 0px 0px 0px 4px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-meeting-default.png`, `plan-meeting-hover.png`, `plan-meeting-focus-visible.png`, `plan-meeting-pressed.png`.

#### ptable-acc

Feature-comparison accordion. A category row in the feature-comparison table (Users, Storage, Projects & workspaces, Feedback & collaboration, … — the rows mount expanded); the closed state was measured after clicking the row — a local UI toggle.

Page: pricing. Selector: `comparison category accordion`. States: default, closed.

| Property | default | closed |
|---|---|---|
| Size (w x h) | 1080 x 36.09 | = |
| Padding | 0px 0px 10px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | FrameGothic 18px/26.1px 400 | = |
| Letter spacing | normal | = |
| Colour | #fcfcfc | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 10 x 10, colour #fcfcfc, fill #000000 | = |
| How | at rest | own toggle |

Crops: `ptable-acc-default.png`, `ptable-acc-closed.png`.

#### faq-acc

FAQ accordion. A question row in the pricing FAQ; the opened state was measured after clicking it — a local UI toggle.

Page: pricing. Selector: `pricing FAQ accordion`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 1080 x 19.5 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | FrameGothic 15px/19.5px 500 | = |
| Letter spacing | normal | = |
| Colour | #fcfcfc | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #fcfcfc, fill #000000 | = |
| How | at rest | own toggle |

Crops: `faq-acc-default.png`, `faq-acc-opened.png`.

### Contact

#### contact-h1

Contact headline. "Hello, how can we help you?" — the /contact hub.

Page: contact. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 712 x 166.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | FrameGothic 80px/83.2px 600 |
| Letter spacing | -3.6px |
| Colour | #fcfcfc |
| Transition | none |
| How | at rest |

Crops: `contact-h1-default.png`.

#### schedule-btn

Schedule a Meeting. The white "Schedule a Meeting" button on /contact (it mounts a Calendly scheduler — a vendor widget, never opened); measured, never pressed.

Page: contact. Selector: `contact Schedule a Meeting`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 186.53 x 39.75 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #fcfcfc offset 0px | = |
| Font | FrameGothic 14px/13.44px 600 | = | = | = |
| Letter spacing | 0.14px | = | = | = |
| Colour | #000000 | = | = | #fcfcfc |
| Text node | span.Button_buttonText__Yzd9S: FrameGothic 14px/13.44px 600, #000000, ls 0.14px | = | = | span.Button_buttonText__Yzd9S: FrameGothic 14px/13.44px 600, #fcfcfc, ls 0.14px |
| Transition | color 0.3s cubic-bezier(0, 0.44, 0.6, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 184.531px x 37.75px, absolute, bg #f5f5f8, radius 100px | 184.531px x 37.75px, absolute, bg #e9e9ff @ 0.7, radius 100px | 184.531px x 37.75px, absolute, bg #e9e9ff @ 0.7, radius 100px | 186.531px x 39.75px, absolute, bg #000000 @ 0, radius 100px |
| ::after | 186.531px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #c1c2d9 0px 0px 0px 2px inset | 186.531px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #fcfcfc 0px 0px 0px 2px inset | = | 186.531px x 39.75px, absolute, bg #000000 @ 0, radius 100px, shadow #d1d1fb @ 0.2 0px 0px 0px 4px inset |
| Painted layers | button::before.Button_white__XYP1F.Button_base__1G9eD 184.531pxx37.75px bg #f5f5f8 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px | button::before.Button_white__XYP1F.Button_base__1G9eD 184.531pxx37.75px bg #e9e9ff @ 0.7 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px; button::after.Button_white__XYP1F.Button_base__1G9eD 186.531pxx39.75px r 100px shadow #fcfcfc 0px 0px 0px 2px inset | button.Button_white__XYP1F.Button_base__1G9eD 186.5x39.8 r 100px outline 1px dotted #fcfcfc offset 0px; button::before.Button_white__XYP1F.Button_base__1G9eD 184.531pxx37.75px bg #e9e9ff @ 0.7 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px | button::after.Button_white__XYP1F.Button_base__1G9eD 186.531pxx39.75px r 100px shadow #d1d1fb @ 0.2 0px 0px 0px 4px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `schedule-btn-default.png`, `schedule-btn-hover.png`, `schedule-btn-focus-visible.png`, `schedule-btn-pressed.png`.

#### sales-link

Talk with Sales. The "Talk with Sales" text-link button on /contact (leads to /contact/form); measured, never followed.

Page: contact. Selector: `contact Talk with Sales`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 132 x 32 | = | = | = |
| Padding | 0px 24px 16px 0px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #fcfcfc offset 0px | = |
| Font | FrameGothic 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f5f5f8 | #fcfcfc | = | #fcfcfc |
| Text node | span.Button_buttonText__Yzd9S: FrameGothic 16px/16px 400, #f5f5f8 | span.Button_buttonText__Yzd9S: FrameGothic 16px/16px 400, #fcfcfc | = | span.Button_buttonText__Yzd9S: FrameGothic 16px/16px 400, #fcfcfc |
| Transition | color 0.3s cubic-bezier(0.28, 0.44, 0.49, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 132px x 32px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.Button_textLink__A_4Vq.Button_base__1G9eD 132.0x32.0 outline 1px dotted #fcfcfc offset 0px | = |

Crops: `sales-link-default.png`, `sales-link-hover.png`, `sales-link-focus-visible.png`, `sales-link-pressed.png`.

### Contact form

#### form-panel

Contact form card. The dark form card on /contact/form — "Enter your info below. We'll get back to you shortly." with Name/Email/Message fields and a Submit pill; never submitted.

Page: contactform. Selector: `contact form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1543.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times New Roman 10px/10px 400 |
| Letter spacing | normal |
| Colour | #fcfcfc |
| Text node | h1.PortableText_title1__NfBJS.typography_title1__Na5gU: FrameGothic 80px/83.2px 600, #fcfcfc, ls -3.6px |
| Transition | none |
| Painted layers | div.PageSection_pageSection__8v9It.PageSection_isNextSectionSameLevel__ujiEc 1440.0x1543.5 bg #000000; div.Form_inner__RZlVF.global_subgrid__ZRhT6 1080.0x545.8 bg #0d0d18 @ 0.5 border T:1px solid #bdbdf4 @ 0.1 / R:1px solid #bdbdf4 @ 0.1 / B:1px solid #bdbdf4 @ 0.1 / L:1px solid #bdbdf4 @ 0.1 r 5px; input.TextInput_textInput__d8dTK.typography_body__vVxn5 431.0x48.0 border B:1px solid #2e2f40; input.TextInput_textInput__d8dTK.typography_body__vVxn5 431.0x48.0 border B:1px solid #2e2f40; input.TextInput_textInput__d8dTK.typography_body__vVxn5 886.0x48.0 border B:1px solid #2e2f40; button::before.Button_white__XYP1F.Button_base__1G9eD 95.8438pxx37.75px bg #bdbdf4 @ 0.1 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px |
| How | at rest |

Crops: `form-panel-default.png`.

#### form-name

Name field. The underlined "Name" input; photographed empty; focus lands in the field; nothing is typed.

Page: contactform. Selector: `contact Name input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 431 x 48 | = |
| Padding | 1px 2px | = |
| Border | T: none; R: none; B: 1px solid #2e2f40; L: none | T: none; R: none; B: 1px solid #fcfcfc; L: none |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | FrameGothic 15px/21.75px 400 | = |
| Letter spacing | normal | = |
| Colour | #dedfee | = |
| Transition | border-color 0.3s cubic-bezier(0.25, 0.1, 0.25, 1) | = |
| Cursor | text | = |
| Placeholder | #dedfee, opacity 1 | = |
| Painted layers | input.TextInput_textInput__d8dTK.typography_body__vVxn5 431.0x48.0 border B:1px solid #2e2f40 | input.TextInput_textInput__d8dTK.typography_body__vVxn5 431.0x48.0 border B:1px solid #fcfcfc |
| How | at rest | clicked into the field |

Crops: `form-name-default.png`, `form-name-focused.png`.

#### form-email

Email field. The underlined "Email" input; photographed empty; focus lands in the field; nothing is typed.

Page: contactform. Selector: `contact Email input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 431 x 48 | = |
| Padding | 1px 2px | = |
| Border | T: none; R: none; B: 1px solid #2e2f40; L: none | T: none; R: none; B: 1px solid #fcfcfc; L: none |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | FrameGothic 15px/21.75px 400 | = |
| Letter spacing | normal | = |
| Colour | #dedfee | = |
| Transition | border-color 0.3s cubic-bezier(0.25, 0.1, 0.25, 1) | = |
| Cursor | text | = |
| Placeholder | #dedfee, opacity 1 | = |
| Painted layers | input.TextInput_textInput__d8dTK.typography_body__vVxn5 431.0x48.0 border B:1px solid #2e2f40 | input.TextInput_textInput__d8dTK.typography_body__vVxn5 431.0x48.0 border B:1px solid #fcfcfc |
| How | at rest | clicked into the field |

Crops: `form-email-default.png`, `form-email-focused.png`.

#### form-message

Message field. The underlined "Message" input; photographed empty; focus lands in the field; nothing is typed.

Page: contactform. Selector: `contact Message input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 886 x 48 | = |
| Padding | 1px 2px | = |
| Border | T: none; R: none; B: 1px solid #2e2f40; L: none | T: none; R: none; B: 1px solid #fcfcfc; L: none |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | FrameGothic 15px/21.75px 400 | = |
| Letter spacing | normal | = |
| Colour | #dedfee | = |
| Transition | border-color 0.3s cubic-bezier(0.25, 0.1, 0.25, 1) | = |
| Cursor | text | = |
| Placeholder | #dedfee, opacity 1 | = |
| Painted layers | input.TextInput_textInput__d8dTK.typography_body__vVxn5 886.0x48.0 border B:1px solid #2e2f40 | input.TextInput_textInput__d8dTK.typography_body__vVxn5 886.0x48.0 border B:1px solid #fcfcfc |
| How | at rest | clicked into the field |

Crops: `form-message-default.png`, `form-message-focused.png`.

#### form-submit

Submit. The form's pill "Submit" button; its states were measured but the button was never clicked — nothing was sent.

Page: contactform. Selector: `contact Submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 97.84 x 39.75 | = | - | = |
| Padding | 0px 24px | = | - | = |
| Gap | 16px | = | - | = |
| Border | none | = | - | = |
| Radius | 100px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | FrameGothic 14px/13.44px 600 | = | - | = |
| Letter spacing | 0.14px | = | - | = |
| Colour | #4f5167 | = | - | = |
| Text node | span: FrameGothic 14px/13.44px 600, #4f5167, ls 0.14px | = | - | = |
| Transition | color 0.3s cubic-bezier(0, 0.44, 0.6, 1) | = | - | = |
| Cursor | not-allowed | = | - | = |
| ::before | 95.8438px x 37.75px, absolute, bg #bdbdf4 @ 0.1, radius 100px | = | - | = |
| ::after | auto x auto, absolute, bg #000000 @ 0, radius 100px, shadow #c1c2d9 0px 0px 0px 2px inset | = | - | = |
| Painted layers | button::before.Button_white__XYP1F.Button_base__1G9eD 95.8438pxx37.75px bg #bdbdf4 @ 0.1 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px; div::after.SubmitButtonAnimation_dot__vO6gD 2.5pxx2.5px bg #fcfcfc r 50% | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `form-submit-default.png`, `form-submit-hover.png`, `form-submit-pressed.png`.

### Sign-in surface (accounts.frame.io — a different stack)

#### login-panel

Sign-in panel. The accounts.frame.io/welcome sign-in card — the Frame.io mark, "Welcome / Enter your email to get started.", an e-mail field and a "Let's go" submit on a light page (styled-components — a different stack from the marketing site); never submitted.

Page: welcome. Selector: `welcome form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 346 x 345.84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Avenir Next 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.StyledHeader__Title-sc-1mv5dl-1.kEJACn: Avenir Next 24px/normal 700, #000000 |
| Transition | none |
| Icon | 56 x 64, colour #000000 |
| Painted layers | input.TextInput__Input-a3o9vm-1.irdNuq 346.0x40.0 bg #ffffff border T:1px solid #e0475f / R:1px solid #e0475f / B:1px solid #e0475f / L:1px solid #e0475f r 4px; button.Button__StyledButton-tzx5l-0.fmdBhl 346.0x40.0 bg #5b53ff r 6px shadow #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest |

Crops: `login-panel-default.png`.

#### login-email

Email field (sign-in). The "Email" input with placeholder "you@example.com"; photographed empty; focus lands in the field; nothing is typed.

Page: welcome. Selector: `welcome input[type=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 346 x 40 | = |
| Padding | 12px | = |
| Border | 1px solid #e0475f | 1px solid #5b53ff |
| Radius | 4px | = |
| Background | #ffffff | = |
| Box shadow | none | #5b53ff @ 0.1 0px 0px 8px 0px |
| Outline | none | = |
| Font | Avenir Next 14px/21px 400 | = |
| Letter spacing | normal | = |
| Colour | #20222b | = |
| Transition | background-color 0.3s ease | = |
| Cursor | text | = |
| Placeholder | #7d829c, opacity 1 | = |
| Painted layers | input.TextInput__Input-a3o9vm-1.irdNuq 346.0x40.0 bg #ffffff border T:1px solid #e0475f / R:1px solid #e0475f / B:1px solid #e0475f / L:1px solid #e0475f r 4px | input.TextInput__Input-a3o9vm-1.irdNuq 346.0x40.0 bg #ffffff border T:1px solid #5b53ff / R:1px solid #5b53ff / B:1px solid #5b53ff / L:1px solid #5b53ff r 4px shadow #5b53ff @ 0.1 0px 0px 8px 0px |
| How | at rest | clicked into the field |

Crops: `login-email-default.png`, `login-email-focused.png`.

#### login-submit

Let's go submit. The cobalt "Let's go" submit; its states were measured but the button was never clicked — nothing was submitted.

Page: welcome. Selector: `welcome Lets go`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 346 x 40 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #5b53ff | #564ef2 | = | #514ae5 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px inset | = | #53afff 0px 0px 0px 1px inset, #53afff 0px 0px 4px 1px | = |
| Outline | none | = | = | = |
| Font | Avenir Next 14px/14px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.flex-x9ump0-0.Button__ChildrenWrapper-tzx5l-1: Avenir Next 14px/14px 700, #ffffff | = | = | = |
| Transition | background-color, color, box-shadow, opacity 0.2s, 0.2s, 0.2s, 0.0002s ease, ease, ease, ease delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button__StyledButton-tzx5l-0.fmdBhl 346.0x40.0 bg #5b53ff r 6px shadow #000000 @ 0 0px 0px 0px 0px inset | button.Button__StyledButton-tzx5l-0.fmdBhl 346.0x40.0 bg #564ef2 r 6px shadow #000000 @ 0 0px 0px 0px 0px inset | button.Button__StyledButton-tzx5l-0.fmdBhl 346.0x40.0 bg #5b53ff r 6px shadow #53afff 0px 0px 0px 1px inset, #53afff 0px 0px 4px 1px | button.Button__StyledButton-tzx5l-0.fmdBhl 346.0x40.0 bg #514ae5 r 6px shadow #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-focus-visible.png`, `login-submit-pressed.png`.

### Customers, case study, integrations, what's new

#### cust-h1

Customers headline. The /customers masthead.

Page: customers. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 528 x 166.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | FrameGothic 80px/83.2px 600 |
| Letter spacing | -3.6px |
| Colour | #fcfcfc |
| Text node | span: FrameGothic 80px/83.2px 600, #fcfcfc, ls -3.6px |
| Transition | none |
| How | at rest |

Crops: `cust-h1-default.png`.

#### cust-card

Customer card. A customer-story card on /customers; measured, never followed.

Page: customers. Selector: `customer card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1080 x 220 | = |
| Padding | 0px | = |
| Gap | 24px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Times New Roman 10px/10px 400 | = |
| Letter spacing | normal | = |
| Colour | #fcfcfc | = |
| Text node | h2.PortableText_title2__uOViD.typography_title2__Ry8_z: FrameGothic 80px/57.6px 500, #fcfcfc | = |
| Transition | none | = |
| Icon | 182 x 46, colour #eaeaff @ 0.5 | = |
| Painted layers | div.StatsCard_statsCard__U67L3.global_cardHover__VD7I6 344.0x220.0 image linear-gradient(140deg, #1b1b26 -41.97%, #09090d 77.06%) r 10px; div::after.StatsCard_statsCard__U67L3.global_cardHover__VD7I6 342pxx218px border T:1px solid #9d9dff @ 0.05 / R:1px solid #9d9dff @ 0.05 / B:1px solid #9d9dff @ 0.05 / L:1px solid #9d9dff @ 0.05 r 5px; div.StatsCard_statsCard__U67L3.global_cardHover__VD7I6 344.0x220.0 image linear-gradient(140deg, #1b1b26 -41.97%, #09090d 77.06%) r 10px; div::after.StatsCard_statsCard__U67L3.global_cardHover__VD7I6 342pxx218px border T:1px solid #9d9dff @ 0.05 / R:1px solid #9d9dff @ 0.05 / B:1px solid #9d9dff @ 0.05 / L:1px solid #9d9dff @ 0.05 r 5px; div.StatsCard_statsCard__U67L3.global_cardHover__VD7I6 344.0x220.0 image linear-gradient(140deg, #1b1b26 -41.97%, #09090d 77.06%) r 10px; div::after.StatsCard_statsCard__U67L3.global_cardHover__VD7I6 342pxx218px border T:1px solid #9d9dff @ 0.05 / R:1px solid #9d9dff @ 0.05 / B:1px solid #9d9dff @ 0.05 / L:1px solid #9d9dff @ 0.05 r 5px | = |
| How | at rest | mouse hover |

Crops: `cust-card-default.png`, `cust-card-hover.png`.

#### cs-h1

Case-study headline. The masthead of a published case study (Ford); published editorial content, measured at rest.

Page: casestudy. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 712 x 83.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | FrameGothic 80px/83.2px 600 |
| Letter spacing | -3.6px |
| Colour | #fcfcfc |
| Transition | none |
| How | at rest |

Crops: `cs-h1-default.png`.

#### int-h1

Integrations headline. The /integrations masthead.

Page: integrations. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 712 x 166.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | FrameGothic 80px/83.2px 600 |
| Letter spacing | -3.6px |
| Colour | #fcfcfc |
| Text node | span: FrameGothic 80px/83.2px 600, #fcfcfc, ls -3.6px |
| Transition | none |
| How | at rest |

Crops: `int-h1-default.png`.

#### int-card

Integration card. An integration card on /integrations; measured, never followed.

Page: integrations. Selector: `[class*=tileItem]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 252 x 82 | = |
| Padding | 26px 28px 28px 28px | = |
| Border | 1px solid #9d9dff @ 0.05 | 1px solid #252736 @ 0.996 |
| Radius | 5px | = |
| Background | #12131d | #12131d @ 0.004 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Arial 13.3333px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #fcfcfc | = |
| Text node | p.LogoTextItem_label__tJ9F_.typography_formDisclaimer__WbKTP: FrameGothic 11px/13.75px 500, #a3a4bf | = |
| Transition | background-color, border-color 0.5s, 0.5s cubic-bezier(0, 0.44, 0.6, 1), cubic-bezier(0, 0.44, 0.6, 1) delay 0s, 0s | = |
| Cursor | pointer | = |
| Icon | 26 x 21, colour #fcfcfc | = |
| Painted layers | div.LogoTextItem_logoTextItem__gD_il.TileTable_tileItem__4XxcJ 252.0x82.0 bg #12131d border T:1px solid #9d9dff @ 0.05 / R:1px solid #9d9dff @ 0.05 / B:1px solid #9d9dff @ 0.05 / L:1px solid #9d9dff @ 0.05 r 5px | div.LogoTextItem_logoTextItem__gD_il.TileTable_tileItem__4XxcJ 252.0x82.0 bg #12131d @ 0.004 border T:1px solid #252736 @ 0.996 / R:1px solid #252736 @ 0.996 / B:1px solid #252736 @ 0.996 / L:1px solid #252736 @ 0.996 r 5px |
| How | at rest | mouse hover |

Crops: `int-card-default.png`, `int-card-hover.png`.

#### wn-h1

What's New headline. The /whats-new release-notes index masthead.

Page: whatsnew. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1080 x 166.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | FrameGothic 80px/83.2px 600 |
| Letter spacing | -3.6px |
| Colour | #fcfcfc |
| Transition | none |
| How | at rest |

Crops: `wn-h1-default.png`.

#### wn-card

Release card. A release-note card on /whats-new; measured, never followed.

Page: whatsnew. Selector: `whats-new card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 528 x 466.2 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Times New Roman 10px/10px 400 | = |
| Letter spacing | normal | = |
| Colour | #fcfcfc | = |
| Text node | h5.PortableText_title5__n09GN.typography_title5__xlC2_: FrameGothic 20px/24.6px 600, #fcfcfc, ls -0.5px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 4.44 x 7.5, colour #f5f5f8 | = |
| Painted layers | span::after.AnimatedSvgArrow_cssTail__yibfW 20pxx1.65625px bg #f5f5f8 r 1px | = |
| How | at rest | mouse hover |

Crops: `wn-card-default.png`, `wn-card-hover.png`.

### Mobile (390 wide)

#### m-topbar

Mobile top bar. The phone header at 390 wide: the Frame.io mark, "Start Free Trial" and the nav button.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times New Roman 10px/10px 400 |
| Letter spacing | normal |
| Colour | #fcfcfc |
| Text node | a: FrameGothic 12px/12px 600, #fcfcfc, ls 0.12px |
| Transition | transform 0.5s cubic-bezier(0.42, 0, 0.28, 0.99) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 24 x 24, colour #fcfcfc |
| Painted layers | div.AnnouncementBanner_announcementBanner__g9QLM.Navigation_navigationBannerEl__zSvOh 390.0x48.0 bg #5b53ff image linear-gradient(355deg, #ffffff @ 0.15 4.03%, #ffffff @ 0 95.81%), none; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 bg #f0f0f7 r 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 bg #f0f0f7 r 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 bg #f0f0f7 r 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 bg #f0f0f7 r 9.33333px; a::before.Button_white__XYP1F.Button_base__1G9eD autoxauto bg #f5f5f8 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-cta

Drawer CTA. The nav overlay's white "Start Free Trial" pill at 390 wide — the closed top bar carries none (mark, Sign In and the menu button only); measured with the drawer open, never followed.

Page: mobile. Selector: `mobile drawer Start Free Trial`. States: default, focus-visible, pressed.

| Property | default | focus-visible | pressed |
|---|---|---|---|
| Size (w x h) | 165 x 37.75 | - | = |
| Padding | 0px 24px | - | = |
| Gap | 16px | - | = |
| Border | none | - | = |
| Radius | 100px | - | = |
| Background | transparent | - | = |
| Box shadow | none | - | = |
| Outline | none | - | = |
| Font | FrameGothic 14px/13.44px 600 | - | = |
| Letter spacing | 0.14px | - | = |
| Colour | #000000 | - | #fcfcfc |
| Transition | color 0.3s cubic-bezier(0, 0.44, 0.6, 1) | - | = |
| Cursor | pointer | - | = |
| ::before | 163px x 35.75px, absolute, bg #f5f5f8, radius 100px | - | 165px x 37.75px, absolute, bg #000000 @ 0, radius 100px |
| ::after | 165px x 37.75px, absolute, bg #000000 @ 0, radius 100px, shadow #c1c2d9 0px 0px 0px 2px inset | - | 165px x 37.75px, absolute, bg #000000 @ 0, radius 100px, shadow #d1d1fb @ 0.2 0px 0px 0px 4px inset |
| How | at rest | - | CDP forcePseudoState :active:hover |
| Skipped | - | focus failed: keyboard focus did not reach the element | = |

Crops: none.

#### m-menu-btn

Mobile menu button. The "Toggle mobile navigation" button — a local UI toggle; the opened state was measured after activating it.

Page: mobile. Selector: `mobile nav toggle`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 25 x 20 | = | = | = | 20.15 x 23.77 |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px dotted #fcfcfc offset 0px | = | = |
| Font | Arial 13.3333px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #fcfcfc | = | = | = | = |
| Transition | none | = | = | = | = |
| Transform | matrix(0, -1, 1, 0, 0, 0) | = | = | = | matrix(0.849411, -0.126644, 0.126644, 0.849411, 0, 0) |
| Cursor | pointer | = | = | = | = |
| Painted layers | span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 bg #f0f0f7 r 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 bg #f0f0f7 r 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 bg #f0f0f7 r 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 bg #f0f0f7 r 9.33333px | = | button.ToggleButton_navMobileButton__WW3qe 25.0x20.0 outline 1px dotted #fcfcfc offset 0px; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 bg #f0f0f7 r 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 bg #f0f0f7 r 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 bg #f0f0f7 r 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 bg #f0f0f7 r 9.33333px | = | span.ToggleButton_navMobileButtonLineEl__IvuHL 9.3x7.5 bg #f0f0f7 r 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 7.5x9.3 bg #f0f0f7 r 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 9.3x7.5 bg #f0f0f7 r 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 7.5x9.3 bg #f0f0f7 r 9.33333px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `m-menu-btn-default.png`, `m-menu-btn-hover.png`, `m-menu-btn-focus-visible.png`, `m-menu-btn-pressed.png`, `m-menu-btn-opened.png`.

#### m-drawer

Mobile nav overlay. The nav list inside the overlay opened by the menu button; its links were never followed.

Page: mobile. Selector: `mobile nav overlay`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 210 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times New Roman 10px/10px 400 |
| Letter spacing | normal |
| Colour | #fcfcfc |
| Text node | span.Navigation_navigationMainItemInner__mMl9H: FrameGothic 30px/34.5px 600, #fcfcfc, ls -0.9px |
| Transition | none |
| Icon | 30 x 15, colour #fcfcfc, fill #81859f |
| How | at rest |

Crops: `m-drawer-default.png`.

#### m-hero-h1

Mobile hero headline. The masthead at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 145.17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | FrameGothic 44px/48.4px 600 |
| Letter spacing | -1.32px |
| Colour | #fcfcfc |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-hero-cta

Mobile hero CTA. The hero "Start Free Trial" button at 390 wide; measured never followed.

Page: mobile. Selector: `mobile hero Start Free Trial`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 342 x 37.75 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #fcfcfc offset 1px | = |
| Font | FrameGothic 14px/13.44px 600 | = | = | = |
| Letter spacing | 0.14px | = | = | = |
| Colour | #000000 | = | = | #fcfcfc |
| Text node | span.Button_buttonText__Yzd9S: FrameGothic 14px/13.44px 600, #000000, ls 0.14px | = | = | span.Button_buttonText__Yzd9S: FrameGothic 14px/13.44px 600, #fcfcfc, ls 0.14px |
| Transition | color 0.3s cubic-bezier(0, 0.44, 0.6, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 340px x 35.75px, absolute, bg #f5f5f8, radius 100px | = | = | 342px x 37.75px, absolute, bg #000000 @ 0, radius 100px |
| ::after | 342px x 37.75px, absolute, bg #000000 @ 0, radius 100px, shadow #c1c2d9 0px 0px 0px 2px inset | = | = | 342px x 37.75px, absolute, bg #000000 @ 0, radius 100px, shadow #d1d1fb @ 0.2 0px 0px 0px 4px inset |
| Painted layers | a::before.Button_white__XYP1F.Button_base__1G9eD 340pxx35.75px bg #f5f5f8 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px | = | a.Button_white__XYP1F.Button_base__1G9eD 342.0x37.8 r 100px outline 1px dotted #fcfcfc offset 1px; a::before.Button_white__XYP1F.Button_base__1G9eD 340pxx35.75px bg #f5f5f8 border T:1px solid #c1c2d9 / R:1px solid #c1c2d9 / B:1px solid #c1c2d9 / L:1px solid #c1c2d9 r 100px | a::after.Button_white__XYP1F.Button_base__1G9eD 342pxx37.75px r 100px shadow #d1d1fb @ 0.2 0px 0px 0px 4px inset |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `m-hero-cta-default.png`, `m-hero-cta-hover.png`, `m-hero-cta-focus-visible.png`, `m-hero-cta-pressed.png`.

## Transitions declared in the readable stylesheets

frame.io serves most of its CSS as linked `/_next/static/css` chunks (cross-origin-readable only through the network), so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- casestudy: `opacity var(--duration-500ms)`, `var(--duration-300ms) transform var(--ease-basic-butter),var(--duration-300ms) background-color var(--ease-basic-butter)`, `var(--duration-300ms) transform var(--ease-basic-butter)`, `opacity var(--duration-300ms) var(--ease-default)`, `all var(--duration-300ms) var(--ease-default)`, `border-color var(--duration-300ms) var(--ease-default)`, `transform var(--duration-60ms) var(--ease-micro-bounce)`, `var(--duration-600ms) opacity var(--ease-basic-butter)`, `opacity var(--duration-200ms) var(--ease-basic-butter)`, `color var(--duration-200ms) var(--ease-basic-butter)`, `var(--duration-500ms) background-color var(--ease-micro-bounce),var(--duration-500ms) border-color var(--ease-micro-bounce)`, `0.1s ease-out`

- contact: `opacity var(--duration-500ms)`, `var(--duration-300ms) transform var(--ease-basic-butter),var(--duration-300ms) background-color var(--ease-basic-butter)`, `var(--duration-300ms) transform var(--ease-basic-butter)`, `opacity var(--duration-300ms) var(--ease-default)`, `all var(--duration-300ms) var(--ease-default)`, `border-color var(--duration-300ms) var(--ease-default)`, `transform var(--duration-60ms) var(--ease-micro-bounce)`, `var(--duration-600ms) opacity var(--ease-basic-butter)`, `opacity var(--duration-200ms) var(--ease-basic-butter)`, `color var(--duration-200ms) var(--ease-basic-butter)`, `var(--duration-500ms) background-color var(--ease-micro-bounce),var(--duration-500ms) border-color var(--ease-micro-bounce)`, `0.1s ease-out`

- contactform: `opacity var(--duration-500ms)`, `var(--duration-300ms) transform var(--ease-basic-butter),var(--duration-300ms) background-color var(--ease-basic-butter)`, `var(--duration-300ms) transform var(--ease-basic-butter)`, `opacity var(--duration-300ms) var(--ease-default)`, `all var(--duration-300ms) var(--ease-default)`, `border-color var(--duration-300ms) var(--ease-default)`, `transform var(--duration-60ms) var(--ease-micro-bounce)`, `var(--duration-600ms) opacity var(--ease-basic-butter)`, `opacity var(--duration-200ms) var(--ease-basic-butter)`, `color var(--duration-200ms) var(--ease-basic-butter)`, `var(--duration-500ms) background-color var(--ease-micro-bounce),var(--duration-500ms) border-color var(--ease-micro-bounce)`, `0.1s ease-out`

- customers: `opacity var(--duration-500ms)`, `var(--duration-300ms) transform var(--ease-basic-butter),var(--duration-300ms) background-color var(--ease-basic-butter)`, `var(--duration-300ms) transform var(--ease-basic-butter)`, `opacity var(--duration-300ms) var(--ease-default)`, `all var(--duration-300ms) var(--ease-default)`, `border-color var(--duration-300ms) var(--ease-default)`, `transform var(--duration-60ms) var(--ease-micro-bounce)`, `var(--duration-600ms) opacity var(--ease-basic-butter)`, `opacity var(--duration-200ms) var(--ease-basic-butter)`, `color var(--duration-200ms) var(--ease-basic-butter)`, `var(--duration-500ms) background-color var(--ease-micro-bounce),var(--duration-500ms) border-color var(--ease-micro-bounce)`, `0.1s ease-out`

- home: `opacity var(--duration-500ms)`, `var(--duration-300ms) transform var(--ease-basic-butter),var(--duration-300ms) background-color var(--ease-basic-butter)`, `var(--duration-300ms) transform var(--ease-basic-butter)`, `opacity var(--duration-300ms) var(--ease-default)`, `all var(--duration-300ms) var(--ease-default)`, `border-color var(--duration-300ms) var(--ease-default)`, `transform var(--duration-60ms) var(--ease-micro-bounce)`, `var(--duration-600ms) opacity var(--ease-basic-butter)`, `opacity var(--duration-200ms) var(--ease-basic-butter)`, `color var(--duration-200ms) var(--ease-basic-butter)`, `var(--duration-500ms) background-color var(--ease-micro-bounce),var(--duration-500ms) border-color var(--ease-micro-bounce)`, `0.1s ease-out`

- integrations: `opacity var(--duration-500ms)`, `var(--duration-300ms) transform var(--ease-basic-butter),var(--duration-300ms) background-color var(--ease-basic-butter)`, `var(--duration-300ms) transform var(--ease-basic-butter)`, `opacity var(--duration-300ms) var(--ease-default)`, `all var(--duration-300ms) var(--ease-default)`, `border-color var(--duration-300ms) var(--ease-default)`, `transform var(--duration-60ms) var(--ease-micro-bounce)`, `var(--duration-600ms) opacity var(--ease-basic-butter)`, `opacity var(--duration-200ms) var(--ease-basic-butter)`, `color var(--duration-200ms) var(--ease-basic-butter)`, `var(--duration-500ms) background-color var(--ease-micro-bounce),var(--duration-500ms) border-color var(--ease-micro-bounce)`, `0.1s ease-out`

- pricing: `opacity var(--duration-500ms)`, `var(--duration-300ms) transform var(--ease-basic-butter),var(--duration-300ms) background-color var(--ease-basic-butter)`, `var(--duration-300ms) transform var(--ease-basic-butter)`, `opacity var(--duration-300ms) var(--ease-default)`, `all var(--duration-300ms) var(--ease-default)`, `border-color var(--duration-300ms) var(--ease-default)`, `transform var(--duration-60ms) var(--ease-micro-bounce)`, `var(--duration-600ms) opacity var(--ease-basic-butter)`, `opacity var(--duration-200ms) var(--ease-basic-butter)`, `color var(--duration-200ms) var(--ease-basic-butter)`, `var(--duration-500ms) background-color var(--ease-micro-bounce),var(--duration-500ms) border-color var(--ease-micro-bounce)`, `0.1s ease-out`

- welcome: `background-color 0.2s, color 0.2s, box-shadow 0.2s, opacity 0.2ms`, `border-color 0.2s ease-in-out`, `background-color 300ms`

- whatsnew: `opacity var(--duration-500ms)`, `var(--duration-300ms) transform var(--ease-basic-butter),var(--duration-300ms) background-color var(--ease-basic-butter)`, `var(--duration-300ms) transform var(--ease-basic-butter)`, `opacity var(--duration-300ms) var(--ease-default)`, `all var(--duration-300ms) var(--ease-default)`, `border-color var(--duration-300ms) var(--ease-default)`, `transform var(--duration-60ms) var(--ease-micro-bounce)`, `var(--duration-600ms) opacity var(--ease-basic-butter)`, `opacity var(--duration-200ms) var(--ease-basic-butter)`, `color var(--duration-200ms) var(--ease-basic-butter)`, `var(--duration-500ms) background-color var(--ease-micro-bounce),var(--duration-500ms) border-color var(--ease-micro-bounce)`, `0.1s ease-out`

## Reduced motion

- home (`header a[class*="Button"], [class*="navigationMainItem"]` under prefers-reduced-motion): transition `color 0.3s cubic-bezier(0, 0.44, 0.6, 1)`, animation `none 0s ease 0s 1 normal none running`, html scroll-behavior `smooth`
