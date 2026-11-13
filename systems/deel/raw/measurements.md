# Component measurements

Computed styles read from deel.com on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the home, /pricing/, /hr/, /global-payroll/ and /about-us/ (the Mobile group on the home and /pricing/) — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### promo-banner

Promo banner. The "Special Offer" strip above the nav ("Get 3 months free of PEO" + Claim offer + close); a dismissible banner, never dismissed.

Page: home. Selector: `#top-banner`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.87 |
| Text node | div.MuiBox-root.mui-1wjc8ik: Inter 12px/12px 600, #000000 @ 0.87, ls 0.24px |
| Transition | none |
| Icon | 24 x 24, colour #ffffff |
| Painted layers | div.MuiBox-root.mui-r1bhz9 1440.0x64.0 bg #1b1b1b; div.MuiBox-root.mui-1wjc8ik 111.1x28.0 bg #b1d8fc r 2px; button.mui-1rh4x73 85.4x32.0 bg #ffffff r 200px |
| How | at rest |

Crops: `promo-banner-default.png`.

#### promo-cta

Promo CTA. "Claim offer" — the banner button; measured, never followed.

Page: home. Selector: `#top-banner button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.36 x 32 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 200px | = | = | = |
| Background | #ffffff | #3f3f3f | = | #3f3f3f |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | BagossStandardVF 12px/20.4px 500 | = | = | = |
| Letter spacing | 0.18px | = | = | = |
| Colour | #1b1b1b | #ffffff | = | #ffffff |
| Transition | all 0.1s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.mui-1rh4x73 85.4x32.0 bg #ffffff r 200px | button.mui-1rh4x73 85.4x32.0 bg #3f3f3f r 200px | button.mui-1rh4x73 85.4x32.0 bg #ffffff r 200px outline 1px auto #005fcc offset 0px | button.mui-1rh4x73 85.4x32.0 bg #3f3f3f r 200px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `promo-cta-default.png`, `promo-cta-hover.png`, `promo-cta-focus-visible.png`, `promo-cta-pressed.png`.

#### header-nav

Header nav. The sticky nav inside the header: logo, Solutions/Use cases/Who we serve/Resources, Pricing, EN, Log in, Book a demo.

Page: home. Selector: `header nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 80 |
| Padding | 20px 64px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.87 |
| Text node | button.mui-1fo3fxi: BagossStandardVF 15px/24px 500, #1b1b1b, ls 0.375px |
| Transition | box-shadow 0.2s ease-in-out |
| Icon | 24 x 24, colour #1b1b1b |
| Painted layers | nav.mui-8qiahu 1440.0x80.0 bg #ffffff; img.border.border-white 12.5x12.5 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 3.35544e+07px; button.hidden-phone.mui-ti8o1k 75.1x40.0 border T:2px solid #1b1b1b @ 0.16 / R:2px solid #1b1b1b @ 0.16 / B:2px solid #1b1b1b @ 0.16 / L:2px solid #1b1b1b @ 0.16 r 200px; button.mui-1wshw4o 117.2x40.0 bg #1b1b1b r 200px |
| How | at rest |

Crops: `header-nav-default.png`.

#### nav-logo

Logo. The Deel wordmark in the nav.

Page: home. Selector: `#navbar-logo-link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 78 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Transition | color 0.1s ease-in-out |
| Cursor | pointer |
| How | at rest |

Crops: `nav-logo-default.png`.

#### nav-link

Nav item (dropdown). "Solutions" — a dropdown nav item; measured, never followed.

Page: home. Selector: `nav .mui-1fo3fxi`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 95.31 x 40 | = | = | = | = |
| Padding | 8px 0px | = | = | = | = |
| Gap | 4px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = | = |
| Font | BagossStandardVF 15px/24px 500 | = | = | = | = |
| Letter spacing | 0.375px | = | = | = | = |
| Colour | #1b1b1b | = | = | = | = |
| Transition | all 0.1s ease-in-out | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 24 x 24, colour #1b1b1b | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Opacity | - | 0.7 | = | 0.7 | 0.7 |
| Painted layers | - | = | button.mui-1fo3fxi 95.3x40.0 outline 1px auto #005fcc offset 0px | = | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`, `nav-link-opened.png`.

#### nav-plain-link

Nav link. "Pricing" — a plain nav link; measured, never followed.

Page: home. Selector: `nav .mui-1moi9ht`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50.2 x 40 | = | = | = |
| Padding | 8px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | BagossStandardVF 15px/24px 500 | = | = | = |
| Letter spacing | 0.375px | = | = | = |
| Colour | #1b1b1b | #4e4e4e | = | #4e4e4e |
| Transition | color 0.1s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.mui-1moi9ht 50.2x40.0 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-plain-link-default.png`, `nav-plain-link-hover.png`, `nav-plain-link-focus-visible.png`, `nav-plain-link-pressed.png`.

#### nav-locale

Locale switch. The "EN" language/locale switch in the nav; measured, never changed.

Page: home. Selector: `nav a, nav button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 68.11 x 36 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | #fff7ed @ 0.8 | = | #fff7ed @ 0.8 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Inter 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.text-sm.font-semibold: Inter 14px/20px 600, #1b1b1b | = | = | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | img.border.border-white 12.5x12.5 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 3.35544e+07px | button.flex.items-center 68.1x36.0 bg #fff7ed @ 0.8 r 3.35544e+07px; img.border.border-white 12.5x12.5 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 3.35544e+07px | button.flex.items-center 68.1x36.0 r 3.35544e+07px outline 1px auto #005fcc offset 0px; img.border.border-white 12.5x12.5 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 3.35544e+07px | button.flex.items-center 68.1x36.0 bg #fff7ed @ 0.8 r 3.35544e+07px; img.border.border-white 12.5x12.5 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-locale-default.png`, `nav-locale-hover.png`, `nav-locale-focus-visible.png`, `nav-locale-pressed.png`.

#### nav-login

Log in link. "Log in" — outbound to app.deel.com; measured, never followed.

Page: home. Selector: `nav a[href*="app.deel.com"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 75.14 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1b | #4e4e4e | = | #4e4e4e |
| Text node | button.hidden-phone.mui-ti8o1k: BagossStandardVF 14px/23.8px 500, #1b1b1b, ls 0.21px | = | = | = |
| Transition | color 0.1s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.hidden-phone.mui-ti8o1k 75.1x40.0 border T:2px solid #1b1b1b @ 0.16 / R:2px solid #1b1b1b @ 0.16 / B:2px solid #1b1b1b @ 0.16 / L:2px solid #1b1b1b @ 0.16 r 200px | button.hidden-phone.mui-ti8o1k 75.1x40.0 border T:2px solid #1b1b1b @ 0.4 / R:2px solid #1b1b1b @ 0.4 / B:2px solid #1b1b1b @ 0.4 / L:2px solid #1b1b1b @ 0.4 r 200px | a.mui-15k05j0 75.1x40.0 outline 1px auto #005fcc offset 1px; button.hidden-phone.mui-ti8o1k 75.1x40.0 border T:2px solid #1b1b1b @ 0.16 / R:2px solid #1b1b1b @ 0.16 / B:2px solid #1b1b1b @ 0.16 / L:2px solid #1b1b1b @ 0.16 r 200px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-demo

Book a demo CTA. The nav "Book a demo" button; measured, never followed.

Page: home. Selector: `nav .mui-1wshw4o`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117.22 x 40 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 200px | = | = | = |
| Background | #1b1b1b | #4e4e4e | = | #4e4e4e |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | BagossStandardVF 14px/23.8px 500 | = | = | = |
| Letter spacing | 0.21px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.1s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.mui-1wshw4o 117.2x40.0 bg #1b1b1b r 200px | button.mui-1wshw4o 117.2x40.0 bg #4e4e4e r 200px | button.mui-1wshw4o 117.2x40.0 bg #1b1b1b r 200px outline 1px auto #005fcc offset 0px | button.mui-1wshw4o 117.2x40.0 bg #4e4e4e r 200px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-demo-default.png`, `nav-demo-hover.png`, `nav-demo-focus-visible.png`, `nav-demo-pressed.png`.

#### footer

Footer. The footer band: product/company/resource columns, social icons, legal links.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1015.38 |
| Padding | 0px 64px |
| Border | none |
| Radius | 0px |
| Background | #1b1b1b |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.87 |
| Text node | p.mui-1711c28: Inter 14px/23.8px 560, #faf4ee |
| Transition | none |
| Icon | 20 x 20, colour #ffffff |
| Painted layers | footer.mui-1aarjlu 1440.0x1015.4 bg #1b1b1b; div.MuiBox-root.mui-8qgzw2 1312.0x120.8 border B:1px solid #faf4ee @ 0.16; div.MuiBox-root.mui-1l1lj2r 1312.0x600.8 border B:1px solid #faf4ee @ 0.16; div.MuiBox-root.mui-azjfhw 8.0x8.0 bg #53a945 r 50%; div.MuiBox-root.mui-y71o3e 1312.0x193.4 border B:1px solid #faf4ee @ 0.16; button.mui-z5ov0c 44.0x44.0 bg #1b1b1b r 200px |
| Ancestor paint | 1 up body bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-heading

Footer column heading. A footer column heading ("Solutions"/"Deel Platform"/"Resources").

Page: home. Selector: `footer h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 236.8 x 18.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BagossCondensedFont 16px/18.4px 500 |
| Letter spacing | normal |
| Colour | #faf4ee |
| Transition | none |
| How | at rest |

Crops: `footer-heading-default.png`.

#### footer-link

Footer link. "About us" — a footer menu link; measured, never followed.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 60.42 x 23.8 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1b | #4e4e4e | = | #4e4e4e |
| Text node | p.mui-1711c28: Inter 14px/23.8px 560, #faf4ee | = | = | = |
| Transition | color 0.1s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |
| Painted layers | - | = | a.mui-i1l04d 60.4x23.8 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-link

Social icon link. A social icon link in the footer; measured, never followed.

Page: home. Selector: `footer a[href*="linkedin"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |
| Painted layers | - | = | a.mui-j04pfz 32.0x32.0 outline 1px auto #005fcc offset 1px | = |

Crops: `social-link-default.png`, `social-link-hover.png`, `social-link-focus-visible.png`, `social-link-pressed.png`.

#### menu-item

Mega-menu item. "Deel Payroll - Pay teams locally or globally" — a link inside the Solutions mega dropdown; measured after clicking the nav item open, never followed.

Page: home. Selector: `menu a`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 334 x 66 | = |
| Padding | 8px | = |
| Gap | 16px | = |
| Border | none | = |
| Radius | 14px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | 1px auto #005fcc offset 1px |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1b1b | = |
| Text node | p.mui-ic7icj: BagossStandardVF 16px/25.6px 540, #1b1b1b, ls 0.4px | = |
| Transition | background 0.1s ease-in-out | = |
| Cursor | pointer | = |
| Painted layers | div.link-icon.MuiBox-root 48.0x48.0 bg #f6f0fe r 12px | a.mui-egns2o 334.0x66.0 r 14px outline 1px auto #005fcc offset 1px; div.link-icon.MuiBox-root 48.0x48.0 bg #f6f0fe r 12px |
| How | at rest | Shift+Tab, Tab |

Crops: `menu-item-default.png`, `menu-item-focus-visible.png`.

#### menu-panel

Mega-menu panel. The Solutions mega dropdown container (1241x629) opened by the nav item click; measured open, its links never followed.

Page: home. Selector: `js:[...document.querySelectorAll("a")].find((a) => /deel payroll overview/i.test(a.textContent))?.parentElement`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1241 x 629 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.87 |
| Text node | p.mui-194yby4: BagossStandardVF 13px/14.95px 500, #1b1b1b @ 0.7, ls 0.78px |
| Transition | none |
| Icon | 12 x 12, colour #ffffff |
| Painted layers | p.mui-194yby4 692.0x32.0 border B:1px solid #1b1b1b @ 0.16; div.link-icon.MuiBox-root 48.0x48.0 bg #f6f0fe r 12px; div.link-icon.MuiBox-root 48.0x48.0 bg #f6f0fe r 12px; div.link-icon.MuiBox-root 48.0x48.0 bg #f6f0fe r 12px; div.link-icon.MuiBox-root 48.0x48.0 bg #f6f0fe r 12px; div.link-icon.MuiBox-root 48.0x48.0 bg #f6f0fe r 12px |
| How | main-world query (locators never settle on this route) |

Crops: `menu-panel-default.png`.

### Home

#### hero-block

Hero block. The dark hero section ("Hire, manage, pay, & equip anyone, anywhere." on a dark field).

Page: home. Selector: `hero section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1416 x 732 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.87 |
| Text node | h1.text-balance.m-0: BagossCondensedFont 60px/63px 500, #ffffff, ls -0.19px |
| Transition | none |
| Painted layers | div.w-full.flex 702.6x732.0 bg #201547 image linear-gradient(118deg, #5938b7 @ 0 48.33%, #5938b7 92.96%), none r 12px; button.group.flex 181.5x80.0 bg #ffffff @ 0.04 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 12px; span.inline-flex.items-center 18.0x18.0 border T:2px solid #a98df6 / R:2px solid #a98df6 / B:2px solid #a98df6 / L:2px solid #a98df6 r 4px; button.group.flex 181.5x80.0 bg #ffffff @ 0.04 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 12px; span.inline-flex.items-center 18.0x18.0 border T:2px solid #a98df6 / R:2px solid #a98df6 / B:2px solid #a98df6 / L:2px solid #a98df6 r 4px; button.group.flex 117.0x89.6 bg #ffffff @ 0.04 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 12px |
| Ancestor paint | 1 up section.w-full.overflow-hidden bg #ffffff |
| How | at rest |

Crops: `hero-block-default.png`.

#### hero-h1

Hero heading. "Hire, manage, pay, & equip anyone, anywhere." — the BagossCondensed hero title.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 574.59 x 189 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BagossCondensedFont 60px/63px 500 |
| Letter spacing | -0.19px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-tile

Hero action tile. "Hire anywhere" — a quick-action tile under the hero title; measured, never followed.

Page: home. Selector: `a.group`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 181.5 x 80 | = | = | = |
| Padding | 12px | = | = | = |
| Gap | 12px | = | = | = |
| Border | 1px solid #ffffff @ 0.1 | = | = | 1px solid #ffffff @ 0.2 |
| Radius | 12px | = | = | = |
| Background | #ffffff @ 0.04 | = | = | #ffffff @ 0.08 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.leading-[1.2].whitespace-pre-line: Inter 14px/16.8px 600, #ffffff | = | = | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.group.flex 181.5x80.0 bg #ffffff @ 0.04 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 12px; span.inline-flex.items-center 18.0x18.0 border T:2px solid #a98df6 / R:2px solid #a98df6 / B:2px solid #a98df6 / L:2px solid #a98df6 r 4px | = | button.group.flex 181.5x80.0 bg #ffffff @ 0.04 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.7 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.inline-flex.items-center 18.0x18.0 border T:2px solid #a98df6 / R:2px solid #a98df6 / B:2px solid #a98df6 / L:2px solid #a98df6 r 4px | button.group.flex 181.5x80.0 bg #ffffff @ 0.08 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 12px; span.inline-flex.items-center 18.0x18.0 border T:2px solid #a98df6 / R:2px solid #a98df6 / B:2px solid #a98df6 / L:2px solid #a98df6 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-tile-default.png`, `hero-tile-hover.png`, `hero-tile-focus-visible.png`, `hero-tile-pressed.png`.

#### hero-demo

Hero demo button. The hero "Book a demo" pill (375x51 rounded-full); measured, never followed.

Page: home. Selector: `main a, main button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 375 x 51 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff | #ffffff @ 0.9 | = | #ffffff @ 0.9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Inter 18px/30.6px 600 | = | = | = |
| Letter spacing | 0.24px | = | = | = |
| Colour | #1b1b1b | = | = | = |
| Transition | all 0.1s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.!rounded-full.!w-full 375.0x51.0 bg #ffffff r 3.35544e+07px | button.!rounded-full.!w-full 375.0x51.0 bg #ffffff @ 0.9 r 3.35544e+07px | button.!rounded-full.!w-full 375.0x51.0 bg #ffffff r 3.35544e+07px outline 1px auto #005fcc offset 0px | button.!rounded-full.!w-full 375.0x51.0 bg #ffffff @ 0.9 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-demo-default.png`, `hero-demo-hover.png`, `hero-demo-focus-visible.png`, `hero-demo-pressed.png`.

#### section-heading

Section heading. A big Bagoss section heading ("The global people platform").

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 506.84 x 46.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BagossCondensedFont 44px/46.2px 500 |
| Letter spacing | -0.22px |
| Colour | #000000 @ 0.87 |
| Transition | none |
| How | at rest |

Crops: `section-heading-default.png`.

#### product-card

Product card. A "Deel Payroll" product card in the global-people-platform grid; measured, never followed.

Page: home. Selector: `section a`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 418.66 x 438 | = | = |
| Padding | 24px | = | = |
| Border | none | = | = |
| Radius | 16px | = | = |
| Background | #f7f5f2 | = | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px | = |
| Outline | none | = | 1px auto #005fcc offset 1px |
| Font | Inter 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0000ee | = | = |
| Text node | h3.text-balance.m-0: BagossCondensedFont 24px/27.6px 500, #1b1b1b | = | = |
| Transition | all 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | a.group.relative 418.7x438.0 bg #f7f5f2 r 16px | a.group.relative 418.7x438.0 bg #f7f5f2 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px | a.group.relative 418.7x438.0 bg #f7f5f2 r 16px outline 1px auto #005fcc offset 1px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `product-card-default.png`, `product-card-hover.png`, `product-card-focus-visible.png`.

#### review-card

Review card. A customer-review slide inside the video-carousel band (the ~840x638 video card plus caption and case-study link); its link measured, never followed.

Page: home. Selector: `video-carousel slide`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 840 x 638 |
| Padding | 0px |
| Gap | 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.87 |
| Text node | video.mui-1hbrrqt: Inter 16px/24px 400, #000000 @ 0.87 |
| Transition | none |
| Cursor | pointer |
| Icon | 60 x 60, colour #000000 |
| Painted layers | div.relative.w-full 840.0x500.0 bg #141414 r 24px; span.mui-mv42ai 183.4x51.0 border T:2px solid #1b1b1b @ 0.16 / R:2px solid #1b1b1b @ 0.16 / B:2px solid #1b1b1b @ 0.16 / L:2px solid #1b1b1b @ 0.16 r 200px |
| How | at rest |

Crops: `review-card-default.png`.

#### review-band

Reviews band. The "Our customer reviews" video-carousel band (1440x1206).

Page: home. Selector: `reviews section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1205.88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.87 |
| Text node | p.m-0.text-tertiary: Inter 13px/22.1px 500, #1b1b1b @ 0.7, ls 0.78px |
| Transition | none |
| Icon | 60 x 60, colour #000000 |
| Painted layers | div.video-carousel.w-full 1440.0x1205.9 bg #ffffff; div.relative.w-full 840.0x500.0 bg #141414 r 24px; span.mui-mv42ai 183.4x51.0 border T:2px solid #1b1b1b @ 0.16 / R:2px solid #1b1b1b @ 0.16 / B:2px solid #1b1b1b @ 0.16 / L:2px solid #1b1b1b @ 0.16 r 200px; div.relative.w-full 798.0x475.0 bg #141414 r 24px; span.mui-mv42ai 174.3x48.4 border T:2px solid #1b1b1b @ 0.16 / R:2px solid #1b1b1b @ 0.16 / B:2px solid #1b1b1b @ 0.16 / L:2px solid #1b1b1b @ 0.16 r 200px; div.relative.w-full 798.0x475.0 bg #141414 r 24px |
| How | at rest |

Crops: `review-band-default.png`.

### Pricing

#### price-h1

Pricing heading. "Transparent and fair pricing that grows with your business".

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1000 x 117.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BagossCondensedFont 56px/58.8px 500 |
| Letter spacing | -0.28px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `price-h1-default.png`.

#### price-card

Price card. A pricing tier card (Find talent / Hire contractors / Hire employees).

Page: pricing. Selector: `div[class*="elevation"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 458.66 x 928.31 |
| Padding | 0px |
| Border | none |
| Radius | 12px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1b1b1b @ 0.04 0px 8px 16px 0px, #1b1b1b @ 0.04 0px 2px 8px 0px |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.87 |
| Text node | h3.text-balance.m-0: BagossCondensedFont 28px/32.2px 500, #1b1b1b, ls -0.14px |
| Transition | none |
| Painted layers | div.relative.flex 458.7x928.3 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1b1b1b @ 0.04 0px 8px 16px 0px, #1b1b1b @ 0.04 0px 2px 8px 0px; div.absolute.left-0 458.7x16.0 bg #b1d8fc r 12px 12px 0px 0px; button.w-full.mui-1cqp2we 394.7x51.0 bg #1b1b1b r 200px |
| How | at rest |

Crops: `price-card-default.png`.

#### price-cta

Price CTA. The "Book a demo"/"Get started" button inside a pricing tier card (395x51); measured, never followed.

Page: pricing. Selector: `tier card a, tier card button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 394.66 x 51 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 200px | = | = | = |
| Background | #1b1b1b | #4e4e4e | = | #4e4e4e |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | BagossStandardVF 16px/27.2px 500 | = | = | = |
| Letter spacing | 0.24px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.1s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.w-full.mui-1cqp2we 394.7x51.0 bg #1b1b1b r 200px | button.w-full.mui-1cqp2we 394.7x51.0 bg #4e4e4e r 200px | button.w-full.mui-1cqp2we 394.7x51.0 bg #1b1b1b r 200px outline 1px auto #005fcc offset 0px | button.w-full.mui-1cqp2we 394.7x51.0 bg #4e4e4e r 200px |
| Ancestor paint | 2 up div.relative.flex bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1b1b1b @ 0.04 0px 8px 16px 0px, #1b1b1b @ 0.04 0px 2px 8px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `price-cta-default.png`, `price-cta-hover.png`, `price-cta-focus-visible.png`, `price-cta-pressed.png`.

#### faq-item

FAQ accordion. A product-faqs MUI accordion summary; opened via its own click toggle.

Page: pricing. Selector: `[class*="MuiAccordionSummary"]`. States: default, opened, focus-visible.

| Property | default | opened | focus-visible |
|---|---|---|---|
| Size (w x h) | 952 x 80.2 | = | = |
| Padding | 0px | = | = |
| Border | T: 1px solid #faf4ee @ 0.16; R: none; B: none; L: none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | #000000 @ 0.12 |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 @ 0.87 | = | = |
| Text node | h3.MuiTypography-root.MuiTypography-h3: BagossStandardVF 24px/31.2px 440, #ffffff | = | = |
| Transition | opacity 0.1s ease-in-out | = | = |
| Cursor | pointer | = | = |
| Icon | 0 x 0, colour #ffffff | 30 x 30, colour #ffffff | 30 x 30, colour #ffffff |
| Painted layers | div.MuiButtonBase-root.MuiAccordionSummary-root 952.0x80.2 border T:1px solid #faf4ee @ 0.16; div.expandIconWrapper.MuiBox-root 0.0x0.0 bg #faf4ee @ 0.4 r 100%; div.collapseIconWrapper.MuiBox-root 32.0x32.0 bg #faf4ee @ 0.4 r 100% | div.MuiButtonBase-root.MuiAccordionSummary-root 952.0x80.2 border T:1px solid #faf4ee @ 0.16; div.expandIconWrapper.MuiBox-root 32.0x32.0 bg #faf4ee @ 0.4 r 100%; div.collapseIconWrapper.MuiBox-root 0.0x0.0 bg #faf4ee @ 0.4 r 100% | div.MuiButtonBase-root.Mui-focusVisible 952.0x80.2 bg #000000 @ 0.12 border T:1px solid #faf4ee @ 0.16; div.expandIconWrapper.MuiBox-root 32.0x32.0 bg #faf4ee @ 0.4 r 100%; div.collapseIconWrapper.MuiBox-root 0.0x0.0 bg #faf4ee @ 0.4 r 100% |
| Ancestor paint | 1 up div.MuiPaper-root.MuiPaper-elevation bg #201547 | = | = |
| How | at rest | own toggle | Shift+Tab, Tab |
| Opacity | - | 0.6 | = |

Crops: `faq-item-default.png`, `faq-item-opened.png`, `faq-item-focus-visible.png`.

### Deel HR

#### hr-h1

Product heading. The Deel HR page hero heading.

Page: hr. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 574.59 x 109.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BagossCondensedFont 52px/54.6px 500 |
| Letter spacing | -0.19px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hr-h1-default.png`.

#### hr-cta

Product CTA. A product-page CTA; measured, never followed.

Page: hr. Selector: `main a, main button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 430 x 51 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff | #ffffff @ 0.9 | = | #ffffff @ 0.9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter 18px/30.6px 600 | = | = | = |
| Letter spacing | 0.24px | = | = | = |
| Colour | #1b1b1b | = | = | = |
| Transition | all 0.1s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.!bg-white.!text-[#1B1B1B] 430.0x51.0 bg #ffffff r 3.35544e+07px | button.!bg-white.!text-[#1B1B1B] 430.0x51.0 bg #ffffff @ 0.9 r 3.35544e+07px | button.!bg-white.!text-[#1B1B1B] 430.0x51.0 bg #ffffff r 3.35544e+07px outline 1px auto #101010 offset 0px | button.!bg-white.!text-[#1B1B1B] 430.0x51.0 bg #ffffff @ 0.9 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hr-cta-default.png`, `hr-cta-hover.png`, `hr-cta-focus-visible.png`, `hr-cta-pressed.png`.

### Global Payroll

#### payroll-h1

Payroll heading. The Global Payroll page hero heading.

Page: payroll. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 610 x 117.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BagossCondensedFont 56px/58.8px 500 |
| Letter spacing | -0.28px |
| Colour | #faf4ee |
| Transition | none |
| How | at rest |

Crops: `payroll-h1-default.png`.

### About

#### about-h1

About heading. The About page heading.

Page: about. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 283 x 160 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BagossCondensedFont 160px/160px 600 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `about-h1-default.png`.

### Mobile (390 wide)

#### m-nav-bar

Mobile nav.

Page: home. Selector: `nav at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 64 |
| Padding | 12px 24px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.87 |
| Text node | button.mui-1wshw4o: BagossStandardVF 14px/23.8px 500, #ffffff, ls 0.21px |
| Transition | box-shadow 0.2s ease-in-out |
| Icon | 0 x 0, colour #1b1b1b |
| Painted layers | nav.mui-8qiahu 390.0x64.0 bg #ffffff; div.MuiBox-root.mui-1d9b0hw 0.0x0.0 border B:1px solid #1b1b1b @ 0.16; div.MuiBox-root.mui-1d9b0hw 0.0x0.0 border B:1px solid #1b1b1b @ 0.16; div.MuiBox-root.mui-1d9b0hw 0.0x0.0 border B:1px solid #1b1b1b @ 0.16; div.MuiBox-root.mui-1d9b0hw 0.0x0.0 border B:1px solid #1b1b1b @ 0.16; img.border.border-white 0.0x0.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 3.35544e+07px |
| How | at rest |

Crops: `m-nav-bar-default.png`.

#### m-logo

Mobile logo.

Page: home. Selector: `#navbar-logo-link at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 78 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Transition | color 0.1s ease-in-out |
| Cursor | pointer |
| How | at rest |

Crops: `m-logo-default.png`.

#### m-hamburger

Mobile hamburger. The hamburger/drawer trigger at 390px.

Page: home. Selector: `header button`. States: default, pressed.

| Property | default | pressed |
|---|---|---|
| Size (w x h) | 40 x 40 | = |
| Padding | 0px | = |
| Gap | 4px | = |
| Border | none | = |
| Radius | 50% | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | BagossStandardVF 16px/27.2px 500 | = |
| Letter spacing | 0.24px | = |
| Colour | #1b1b1b | = |
| Transition | all 0.1s ease-in-out | = |
| Cursor | pointer | = |
| Icon | 24 x 24, colour #1b1b1b | = |
| How | at rest | CDP forcePseudoState :active:hover |
| Opacity | - | 0.7 |

Crops: `m-hamburger-default.png`, `m-hamburger-pressed.png`.

#### m-h1

Mobile hero heading. The hero h1 at 390px.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 334 x 119.67 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BagossCondensedFont 38px/39.9px 500 |
| Letter spacing | -0.19px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-h1-default.png`.

#### m-demo

Mobile demo CTA. A Book a demo button at 390px; measured, never followed.

Page: home. Selector: `main a, main button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 118.31 x 40 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 200px | = | = | = |
| Background | #1b1b1b | #4e4e4e | = | #4e4e4e |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = |
| Font | BagossStandardVF 14px/23.8px 500 | = | = | = |
| Letter spacing | 0.21px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.1s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.mui-1wshw4o 118.3x40.0 bg #1b1b1b r 200px | button.mui-1wshw4o 118.3x40.0 bg #4e4e4e r 200px | button.mui-1wshw4o 118.3x40.0 bg #1b1b1b r 200px outline 1px auto #e59700 offset 0px | button.mui-1wshw4o 118.3x40.0 bg #4e4e4e r 200px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-demo-default.png`, `m-demo-hover.png`, `m-demo-focus-visible.png`, `m-demo-pressed.png`.

## Transitions declared in the readable stylesheets

deel.com is a light-only Next.js + MUI marketing site; the Cookiebot banner and the promo strip were hidden for clean captures, never answered; the nav dropdowns, hero action tiles and FAQ accordions are local UI toggles; the Book a demo, Claim offer, Log in and every product link was measured but never followed, and app.deel.com was never reached. Every value above is the computed value the page paints.

- about: `0.2s ease-out`, `0.2s ease-in`, `background-color 0.4s`, `none`, `background-color 0.2s ease-out, border-color 0.2s ease-out, translate 0.2s ease-out, box-shadow 0.2s ease-out`, `opacity 0.7s, transform 0.7s, visibility 0.7s`, `opacity 0.3s ease-out, transform 0.3s, visibility 0.3s`, `opacity 0.5s ease-out 0.3s, transform 0.5s ease-out 0.3s, visibility 0.3s`, `opacity 0.7s ease-out, transform 1.2s ease-out`, `color 0.1s ease-in-out`, `0.1s ease-in-out`, `fill 200ms cubic-bezier(0.4, 0, 0.2, 1)`

- home: `0.2s ease-out`, `0.2s ease-in`, `background-color 0.4s`, `none`, `background-color 0.2s ease-out, border-color 0.2s ease-out, translate 0.2s ease-out, box-shadow 0.2s ease-out`, `opacity 0.7s, transform 0.7s, visibility 0.7s`, `opacity 0.3s ease-out, transform 0.3s, visibility 0.3s`, `opacity 0.5s ease-out 0.3s, transform 0.5s ease-out 0.3s, visibility 0.3s`, `opacity 0.7s ease-out, transform 1.2s ease-out`, `color 0.1s ease-in-out`, `0.1s ease-in-out`, `fill 200ms cubic-bezier(0.4, 0, 0.2, 1)`

- hr: `0.2s ease-out`, `0.2s ease-in`, `background-color 0.4s`, `none`, `background-color 0.2s ease-out, border-color 0.2s ease-out, translate 0.2s ease-out, box-shadow 0.2s ease-out`, `opacity 0.7s, transform 0.7s, visibility 0.7s`, `opacity 0.3s ease-out, transform 0.3s, visibility 0.3s`, `opacity 0.5s ease-out 0.3s, transform 0.5s ease-out 0.3s, visibility 0.3s`, `opacity 0.7s ease-out, transform 1.2s ease-out`, `color 0.1s ease-in-out`, `0.1s ease-in-out`, `fill 200ms cubic-bezier(0.4, 0, 0.2, 1)`

- payroll: `0.2s ease-out`, `0.2s ease-in`, `background-color 0.4s`, `none`, `background-color 0.2s ease-out, border-color 0.2s ease-out, translate 0.2s ease-out, box-shadow 0.2s ease-out`, `opacity 0.7s, transform 0.7s, visibility 0.7s`, `opacity 0.3s ease-out, transform 0.3s, visibility 0.3s`, `opacity 0.5s ease-out 0.3s, transform 0.5s ease-out 0.3s, visibility 0.3s`, `opacity 0.7s ease-out, transform 1.2s ease-out`, `color 0.1s ease-in-out`, `0.1s ease-in-out`, `fill 200ms cubic-bezier(0.4, 0, 0.2, 1)`

- pricing: `0.2s ease-out`, `0.2s ease-in`, `background-color 0.4s`, `none`, `background-color 0.2s ease-out, border-color 0.2s ease-out, translate 0.2s ease-out, box-shadow 0.2s ease-out`, `opacity 0.7s, transform 0.7s, visibility 0.7s`, `opacity 0.3s ease-out, transform 0.3s, visibility 0.3s`, `opacity 0.5s ease-out 0.3s, transform 0.5s ease-out 0.3s, visibility 0.3s`, `opacity 0.7s ease-out, transform 1.2s ease-out`, `color 0.1s ease-in-out`, `0.1s ease-in-out`, `fill 200ms cubic-bezier(0.4, 0, 0.2, 1)`
