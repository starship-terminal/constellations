# Component measurements

Computed styles read from www.airbnb.com (geo-redirected to www.airbnb.com.sg from this network) on 2026-11-21 by `tools/capture/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Header and navigation

#### header

Header. The fixed top bar: the Bélo logo, the category tabs (All, Homes, Experiences, Services) with their icons, "Become a host", the language globe and the profile menu. The search pill sits under it.

Page: home. Selector: `the fixed top bar holding the logo, tabs and user controls`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 96 |
| Padding | 0px 48px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Airbnb Cereal VF 14px/20.02px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | span.t151v0ez.atm_7l_hfv0h6_1nos8r: Airbnb Cereal VF 14px/18px 500, #222222 |
| Transition | none |
| Icon | 102 x 32, colour #ff385c, fill #000000 |
| Painted layers | span.u4v6jzs.atm_uc_glywfm_1e3co8w 3.0x3.0 bg #222222 r 1.5px 0px 0px 1.5px; span.u4v6jzs.atm_uc_glywfm_1e3co8w 60.0x3.0 bg #222222; span.u4v6jzs.atm_uc_glywfm_1e3co8w 3.0x3.0 bg #222222 r 0px 1.5px 1.5px 0px; div.b1x9m868.dir 850.0x66.0 bg #ffffff r 100px; div.b1x9m868.bam02bu 850.0x66.0 bg #ebebeb border T:1px solid #dddddd / R:1px solid #dddddd / B:1px solid #dddddd / L:1px solid #dddddd r 100px; div.b1x9m868.b7v5xmd 850.0x66.0 border T:1px solid #dddddd / R:1px solid #dddddd / B:1px solid #dddddd / L:1px solid #dddddd r 100px shadow #000000 @ 0.02 0px 0px 0px 1px, #000000 @ 0.1 0px 8px 24px 0px |
| How | at rest |

Crops: `header-default.png`.

#### header-host-link

Become a host link. The host entry point in the header. Measured and focused, never followed.

Page: home. Selector: `header "Become a host"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 121.27 x 40 | = | = | 118.84 x 38.4 |
| Padding | 11px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | transparent | #f7f7f7 | = | #f7f7f7 |
| Box shadow | none | = | #222222 0px 0px 0px 2px | = |
| Outline | none | = | = | = |
| Font | Airbnb Cereal VF 14px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | span.bi19i11.dir: Airbnb Cereal VF 14px/18px 500, #222222 | = | = | = |
| Transition | box-shadow, transform, background-color, border-color, color 0.2s, 0.25s, 0.3s, 0.3s, 0.3s cubic-bezier(0.2, 0, 0, 1), cubic-bezier(0.2, 0, 0, 1), cubic-bezier(0.2, 0, 0, 1), cubic-bezier(0.2, 0, 0, 1), cubic-bezier(0.2, 0, 0, 1) delay 0s, 0s, 0s, 0s, 0s | = | box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1) | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 121.3x40.0 bg #f7f7f7 r 20px | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 121.3x40.0 r 20px shadow #222222 0px 0px 0px 2px | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 118.8x38.4 bg #f7f7f7 r 20px |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.96, 0, 0) |

Crops: `header-host-link-default.png`, `header-host-link-hover.png`, `header-host-link-focus-visible.png`, `header-host-link-pressed.png`.

#### header-globe

Language button. The globe icon button that opens the language/region sheet. Hovered and focused only.

Page: home. Selector: `the icon-only globe button in the header`. States: .

Not found on the page at capture time.

#### header-menu

Profile menu button. The account buttons rightmost in the header (navigation menu and Log in or sign up). Pressed state is forced, not clicked: the menu leads to sign-up.

Page: home. Selector: `the menu button rightmost in the header`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | 38 x 38 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 50% | = | = | = |
| Background | #f2f2f2 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Airbnb Cereal VF 14px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | transform 0.25s cubic-bezier(0.2, 0, 0, 1) | = | box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1) | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #222222 | = | = | 19 x 19, colour #222222 |
| ::before | 40px x 40px, absolute, bg #f2f2f2, radius 50% | 40px x 40px, absolute, bg #ebebeb, radius 50% | 40px x 40px, absolute, bg #f2f2f2, radius 50%, shadow #ffffff 0px 0px 0px 2px, #222222 0px 0px 0px 4px | 40px x 40px, absolute, bg #ebebeb, radius 50% |
| Painted layers | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 40.0x40.0 bg #f2f2f2 r 50%; button::before.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 40pxx40px bg #f2f2f2 r 50% | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 40.0x40.0 bg #f2f2f2 r 50%; button::before.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 40pxx40px bg #ebebeb r 50% | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 40.0x40.0 bg #f2f2f2 r 50%; button::before.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 40pxx40px bg #f2f2f2 r 50% shadow #ffffff 0px 0px 0px 2px, #222222 0px 0px 0px 4px | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 38.0x38.0 bg #f2f2f2 r 50%; button::before.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 40pxx40px bg #ebebeb r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.95, 0, 0, 0.95, 0, 0) |

Crops: `header-menu-default.png`, `header-menu-hover.png`, `header-menu-focus-visible.png`, `header-menu-pressed.png`.

#### tab-active

Category tab (active). A category tab in the header (Homes / Experiences / Services), the current one underlined.

Page: home. Selector: `header tab "Homes"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 103.55 x 36 | = | = | = |
| Padding | 0px 0px 0px 5px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 8px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #222222 offset 4px | = |
| Font | Airbnb Cereal VF 14px/20.02px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | span.t151v0ez.atm_7l_hfv0h6_1nos8r: Airbnb Cereal VF 14px/18px 500, #6c6c6c | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.cowqa6u.atm_3f_glywfm_jo46a5 103.5x36.0 r 8px outline 2px solid #222222 offset 4px | = |

Crops: `tab-active-default.png`, `tab-active-hover.png`, `tab-active-focus-visible.png`, `tab-active-pressed.png`.

#### tab

Category tab. A resting category tab. Pressed is forced: a real click would navigate.

Page: home. Selector: `header tab "Experiences"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 124.66 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 8px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #222222 offset 4px | = |
| Font | Airbnb Cereal VF 14px/20.02px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | span.t151v0ez.atm_7l_hfv0h6_1nos8r: Airbnb Cereal VF 14px/18px 500, #6c6c6c | span.t151v0ez.atm_7l_hfv0h6_1nos8r: Airbnb Cereal VF 14px/18px 500, #222222 | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.cowqa6u.atm_3f_glywfm_jo46a5 124.7x36.0 r 8px outline 2px solid #222222 offset 4px | = |

Crops: `tab-default.png`, `tab-hover.png`, `tab-focus-visible.png`, `tab-pressed.png`.

### Search bar

#### search-bar

Search bar. The big white pill: Where, When and Who segments with hairline dividers and the pink gradient submit button. Hovering a segment greys it.

Page: home. Selector: `the pill holding the Where/When/Who segments`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 850 x 66 | = |
| Padding | 0px | = |
| Gap | 2px | = |
| Border | none | = |
| Radius | 32px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Airbnb Cereal VF 14px/20.02px 400 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Text node | div.f1i5a5z.dir: Airbnb Cereal VF 12px/16px 500, #222222 | = |
| Transition | none | = |
| Painted layers | div.f21hh4j.dir 1.0x32.0 bg #dddddd; div.f21hh4j.dir 1.0x32.0 bg #dddddd | div.f21hh4j.dir 1.0x32.0 bg #dddddd; div.fhzfs0e.atm_70_1hkpa4_1w3cfyq 283.3x66.0 bg #ebebeb r 32px; div::before.fhzfs0e.atm_70_1hkpa4_1w3cfyq 291.328pxx32px bg #ffffff; div.f21hh4j.dir 1.0x32.0 bg #dddddd |
| How | at rest | mouse hover |

Crops: `search-bar-default.png`, `search-bar-hover.png`.

#### search-segment

Search segment. One labelled segment of the search pill (Where / When / Who): a label line over a placeholder line. Pressed is forced, never submitted.

Page: home. Selector: `the "Where" segment`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 278.33 x 66 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | transparent | #ebebeb | = | #dddddd |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Airbnb Cereal VF 14px/20.02px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | div.f1i5a5z.dir: Airbnb Cereal VF 12px/16px 500, #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 286.328px x 32px, absolute, bg #000000 @ 0, radius 0px | 282.328px x 32px, absolute, bg #ffffff, radius 0px | = | 282.328px x 32px, absolute, bg #ebebeb, radius 0px |
| ::after | 348.328px x 66px, absolute, bg #000000 @ 0, radius 32px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | div.fhzfs0e.atm_70_1hkpa4_1w3cfyq 278.3x66.0 bg #ebebeb r 32px; div::before.fhzfs0e.atm_70_1hkpa4_1w3cfyq 282.328pxx32px bg #ffffff | div.frq0mqg.dir 278.3x66.0 bg #ffffff border T:1px solid #dddddd / R:1px solid #dddddd / B:1px solid #dddddd / L:1px solid #dddddd r 32px shadow #000000 @ 0.1 0px 3px 12px 0px, #000000 @ 0.08 0px 1px 2px 0px | div.fhzfs0e.atm_70_1hkpa4_1w3cfyq 278.3x66.0 bg #dddddd r 32px; div::before.fhzfs0e.atm_70_1hkpa4_1w3cfyq 282.328pxx32px bg #ebebeb; div.frq0mqg.dir 278.3x66.0 bg #ffffff border T:1px solid #dddddd / R:1px solid #dddddd / B:1px solid #dddddd / L:1px solid #dddddd r 32px shadow #000000 @ 0.1 0px 3px 12px 0px, #000000 @ 0.08 0px 1px 2px 0px |

Crops: `search-segment-default.png`, `search-segment-hover.png`, `search-segment-focus-visible.png`, `search-segment-pressed.png`.

#### search-submit

Search submit button. The pink gradient round button with the magnifier (icon only at rest, icon + "Search" when the bar is expanded). Pressed is forced: a real press runs the search.

Page: home. Selector: `the pink button inside the search bar`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 99.67 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #222222 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Airbnb Cereal VF 14px/20.02px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | div.s15knsuf.dir: Airbnb Cereal VF 16px/20px 500, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| Painted layers | div.s1n779tz.atm_26_x1skbv_1nos8r 99.7x48.0 image linear-gradient(to right, #e61e4d 0%, #e31c5f 50%, #d70466 100%) r 24px | = | button.bc003v3.atm_3f_glywfm_jo46a5 99.7x48.0 r 24px shadow #ffffff 0px 0px 0px 2px, #222222 0px 0px 0px 4px; div.s1n779tz.atm_26_x1skbv_1nos8r 99.7x48.0 image linear-gradient(to right, #e61e4d 0%, #e31c5f 50%, #d70466 100%) r 24px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-submit-default.png`, `search-submit-hover.png`, `search-submit-focus-visible.png`, `search-submit-pressed.png`.

#### search-panel-open

Search panel (open). The suggestion panel the Where segment opens ("Suggested destinations": Nearby and city rows with pictograms). Opened by clicking the segment, a local UI toggle; nothing was searched.

Page: home. Selector: `the panel under the expanded search bar`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 393 x 1532 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Airbnb Cereal VF 14px/20.02px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | div.t8con44.dir: Airbnb Cereal VF 12px/16px 400, #222222 |
| Transition | none |
| Painted layers | div.cn9pbab.atm_kd_glywfm_1w3cfyq 361.0x72.0 bg #ffffff r 12px; div.l1ohkupr.atm_mk_h2mmj6_1oqgtup 56.0x56.0 bg #f4f4f4 r 12px; div.cn9pbab.atm_kd_glywfm_1w3cfyq 361.0x72.0 bg #ffffff r 12px; div.l1ohkupr.atm_mk_h2mmj6_1oqgtup 56.0x56.0 bg #f4f4f4 r 12px; div.cn9pbab.atm_kd_glywfm_1w3cfyq 361.0x72.0 bg #ffffff r 12px; div.l1ohkupr.atm_mk_h2mmj6_1oqgtup 56.0x56.0 bg #f4f4f4 r 12px |
| How | clicked the Where segment |

Crops: `search-panel-open-open.png`.

#### mini-search

Mini search pill. The collapsed search pill the results page shows: three segments and the small pink submit. Measured, never opened.

Page: search. Selector: `the compact search bar in the header`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 373.34 x 46 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Airbnb Cereal VF 14px/20.02px 400 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Text node | div.f1wvjdh.fb71sjy: Airbnb Cereal VF 14px/22px 500, #222222 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | button.bc003v3.atm_3f_glywfm_jo46a5 177.9x48.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 40px 4px 4px 40px; span.dqgd72r.dir 1.0x24.0 bg #dddddd; button.bc003v3.atm_3f_glywfm_jo46a5 90.4x48.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; span.dqgd72r.dir 1.0x24.0 bg #dddddd; button.bc003v3.atm_3f_glywfm_jo46a5 109.1x48.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px 40px 40px 4px | = |
| How | at rest | mouse hover |
| Ancestor paint | - | 1 up div.l1qdq8x2.atm_uc_1x5hrc6__1igb08s shadow #000000 @ 0.02 0px 0px 0px 1px, #000000 @ 0.1 0px 8px 24px 0px |

Crops: `mini-search-default.png`, `mini-search-hover.png`.

### Home galleries

#### section-title

Section title. A gallery section head ("Places to stay in Busan") with a chevron that follows to the search page.

Page: home. Selector: `a gallery section title row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 247.92 x 28 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Airbnb Cereal VF 14px/20.02px 400 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Text node | span.t1myg1k4.dir: Airbnb Cereal VF 20px/24px 600, #222222, ls -0.18px | = |
| Transition | box-shadow, transform 0.2s, 0.1s cubic-bezier(0.2, 0, 0, 1), cubic-bezier(0.2, 0, 0, 1) delay 0s, 0s | = |
| Cursor | pointer | = |
| Icon | 12 x 12, colour #222222 | 12.92 x 12.92, colour #222222 |
| Painted layers | span.ipfb646.dir 28.0x28.0 bg #f2f2f2 r 14px | span.ipfb646.dir 30.2x30.2 bg #ebebeb r 14px |
| How | at rest | mouse hover |

Crops: `section-title-default.png`, `section-title-hover.png`.

#### listing-card

Listing card. A home card in a rail: a 12px-radius photo with the Guest favourite badge and wishlist heart over it, then the title, price and star rating rows.

Page: home. Selector: `the first listing-card container in the rail`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 181.7 x 214.61 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 20px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Airbnb Cereal VF 14px/20.02px 400 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Text node | span.t8mq7ht.tpka78r: Airbnb Cereal VF 11px/13px 600, #222222 | = |
| Transition | none | = |
| Icon | 24 x 24, colour #222222, fill #000000 @ 0.5 | = |
| Painted layers | div.c11jbcjg.atm_ks_zryt35__1rgatj2 181.7x172.6 bg #dddddd r 20px; div.rxuv6ej.rjcf2mg 103.6x26.0 bg #ffffff @ 0.8 border T:1px solid #ffffff @ 0.5 / R:1px solid #ffffff @ 0.5 / B:1px solid #ffffff @ 0.5 / L:1px solid #ffffff @ 0.5 r 14px shadow #000000 @ 0.02 0px 0px 0px 1px, #000000 @ 0.04 0px 2px 6px 0px, #000000 @ 0.1 0px 4px 8px 0px | = |
| How | at rest | mouse hover |

Crops: `listing-card-default.png`, `listing-card-hover.png`.

#### rail-arrow

Carousel arrow. The small white round button that pages a card rail. Hovered and focused only; pressing pages the rail.

Page: home. Selector: `the next arrow on a card rail`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 28 x 28 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 50% | = | - | = |
| Background | #f2f2f2 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Airbnb Cereal VF 14px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #c1c1c1 | = | - | = |
| Transition | transform 0.25s cubic-bezier(0.2, 0, 0, 1) | = | - | = |
| Opacity | 0.5 | = | - | = |
| Cursor | not-allowed | = | - | = |
| Icon | 12 x 12, colour #c1c1c1 | 11.2 x 11.2, colour #c1c1c1 | - | 12.92 x 12.92, colour #c1c1c1 |
| ::before | 28px x 28px, absolute, bg #f2f2f2, radius 50% | = | - | = |
| Painted layers | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 28.0x28.0 bg #f2f2f2 r 50%; button::before.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 28pxx28px bg #f2f2f2 r 50% | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, 0) | = | matrix(1, 0, 0, 1, 0, 0) |
| Error | - | = | keyboard focus did not reach the element | = |
| Text node | - | = | = | span.vkhxe59.dir: Airbnb Cereal VF 14px/normal 400, #c1c1c1 |

Crops: `rail-arrow-default.png`, `rail-arrow-hover.png`, `rail-arrow-pressed.png`.

#### card-heart

Wishlist heart. The heart toggle over the card photo. Pressed is forced: a real tap opens the sign-up sheet signed out.

Page: home. Selector: `the heart button inside the card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | 34.56 x 34.56 | 34.56 x 34.56 | 29.44 x 29.44 |
| Padding | 2px 0px 0px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 50% | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #222222 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Airbnb Cereal VF 16px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | transform 0.25s cubic-bezier(0.2, 0, 0, 1) | = | box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1) | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #222222, fill #000000 @ 0.5 | 25.92 x 25.92, colour #222222, fill #000000 @ 0.5 | 25.92 x 25.92, colour #222222, fill #000000 @ 0.5 | 22.08 x 22.08, colour #222222, fill #000000 @ 0.5 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1.08, 0, 0, 1.08, 0, 0) | matrix(1.08, 0, 0, 1.08, 0, 0) | matrix(0.92, 0, 0, 0.92, 0, 0) |
| Painted layers | - | = | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 34.6x34.6 r 50% shadow #ffffff 0px 0px 0px 2px, #222222 0px 0px 0px 4px | = |

Crops: `card-heart-default.png`, `card-heart-hover.png`, `card-heart-focus-visible.png`, `card-heart-pressed.png`.

#### card-rating

Rating row. The star and average under the card title.

Page: home. Selector: `the rating text inside the card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 23.64 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Airbnb Cereal VF 12px/16px 400 |
| Letter spacing | normal |
| Colour | #6c6c6c |
| Text node | span: Airbnb Cereal VF 12px/16px 400, #6c6c6c |
| Transition | none |
| How | at rest |

Crops: none.

#### card-badge

Guest favourite badge. The white pill over the card photo (Guest favourite / Superhost).

Page: home. Selector: `the badge pill over a card photo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 157.7 x 53.53 |
| Padding | 0px |
| Gap | normal 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Airbnb Cereal VF 14px/20.02px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | span.t8mq7ht.tpka78r: Airbnb Cereal VF 11px/13px 600, #222222 |
| Transition | none |
| Icon | 24 x 24, colour #222222, fill #000000 @ 0.5 |
| Painted layers | div.rxuv6ej.rjcf2mg 103.6x26.0 bg #ffffff @ 0.8 border T:1px solid #ffffff @ 0.5 / R:1px solid #ffffff @ 0.5 / B:1px solid #ffffff @ 0.5 / L:1px solid #ffffff @ 0.5 r 14px shadow #000000 @ 0.02 0px 0px 0px 1px, #000000 @ 0.04 0px 2px 6px 0px, #000000 @ 0.1 0px 4px 8px 0px |
| How | at rest |

Crops: `card-badge-default.png`.

### Help Centre

#### footer-link

Footer link. A quick link in the footer grid. Pressed is forced: a real click navigates.

Page: help. Selector: `a link in the footer`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 437.33 x 20.02 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Airbnb Cereal VF 14px/20.02px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | span.boql8ez.dir: Airbnb Cereal VF 14px/18px 400, #222222 | = | span.boql8ez.dir: Airbnb Cereal VF 14px/18px 400, #ffffff | = |
| Transition | none | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 117.1x18.0 bg #3f3f3f r 4px shadow #3f3f3f 0px 0px 0px 2px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### help-title

Help title. "Hi, how can we help?" — the Help Centre headline.

Page: help. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1064 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Airbnb Cereal VF 14px/20.02px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | div.tgycn6r.to35a4y: Airbnb Cereal VF 40px/56px 500, #222222, ls -0.96px |
| Transition | none |
| How | at rest |

Crops: `help-title-default.png`.

#### help-search

Help search field. The search field under the headline (the icon + placeholder). Focused only; nothing was searched.

Page: help. Selector: `the search input on the help home`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 342 x 68 | = |
| Padding | 24px 0px 24px 32px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Airbnb Cereal VF 16px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #222222, opacity 1 | = |
| Ancestor paint | 1 up form.ctwlare.atm_26_xwubbp_1nos8r bg #f7f7f7 | = |
| How | at rest | Shift+Tab, Tab |

Crops: `help-search-default.png`, `help-search-focus-visible.png`.

#### help-tile

Help tile. A topic card in the help grid. Pressed is forced: a real click navigates.

Page: help. Selector: `a topic card in the help grid`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 344 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Airbnb Cereal VF 18px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.t1imbvyv.dir 344.0x48.0 outline 1px auto #005fcc offset 1px | = |

Crops: `help-tile-default.png`, `help-tile-hover.png`, `help-tile-focus-visible.png`, `help-tile-pressed.png`.

### Search results

#### filters-button

Filters button. The sliders-icon button that opens the filters sheet. Pressed is forced; opening the sheet is a toggle but the row also navigates.

Page: search. Selector: `the "Filters" button left of the chip row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 92.56 x 40 | = | = | = |
| Padding | 7px 0px | = | = | = |
| Border | 1px solid #dddddd | 1px solid #222222 | = | 1px solid #222222 |
| Radius | 40px | = | = | = |
| Background | #ffffff | #f7f7f7 | = | #f7f7f7 |
| Box shadow | none | = | #222222 0px 0px 0px 4px, #ffffff @ 0.7 0px 0px 0px 5px | = |
| Outline | none | = | 2px solid #ffffff offset 0px | = |
| Font | Airbnb Cereal VF 14px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | span.burar1r.dir: Airbnb Cereal VF 12px/16px 500, #222222 | = | = | = |
| Transition | outline, border 0.15s, 0.15s cubic-bezier(0, 0, 1, 1), cubic-bezier(0, 0, 1, 1) delay 0s, 0s | = | box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1) | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #222222 | = | = | = |
| Painted layers | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 92.6x40.0 bg #ffffff border T:1px solid #dddddd / R:1px solid #dddddd / B:1px solid #dddddd / L:1px solid #dddddd r 40px | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 92.6x40.0 bg #f7f7f7 border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 r 40px | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 92.6x40.0 bg #ffffff border T:1px solid #dddddd / R:1px solid #dddddd / B:1px solid #dddddd / L:1px solid #dddddd r 40px shadow #222222 0px 0px 0px 4px, #ffffff @ 0.7 0px 0px 0px 5px outline 2px solid #ffffff offset 0px | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 92.6x40.0 bg #f7f7f7 border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 r 40px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filters-button-default.png`, `filters-button-hover.png`, `filters-button-focus-visible.png`, `filters-button-pressed.png`.

#### filter-chip

Filter chip. One pill in the quick-filter row (Type of place, Price, Kitchen …). Pressed is forced.

Page: search. Selector: `a filter pill in the row under the header`. States: default, hover, focus-visible, pressed.

Not found on the page at capture time.

#### result-card

Result card. A listing card in the results grid: photo with badge and heart, then title, distance line, bed rows, dates, price and Free cancellation.

Page: search. Selector: `the first listing card in the results grid`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 307.19 x 351.39 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 20px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Airbnb Cereal VF 14px/20.02px 400 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Text node | div: Airbnb Cereal VF 14px/18px 500, #ffffff | = |
| Transition | none | = |
| Icon | 24 x 24, colour #222222, fill #000000 @ 0.5 | = |
| Painted layers | div.c14dgvke.atm_ks_zryt35__1rgatj2 307.2x230.4 bg #dddddd r 20px; div.o47luuh.o1cq78qk 307.2x230.4 image linear-gradient(#000000 @ 0 calc(100% - 51px), #000000 @ 0.34); div.rl50dte.c1dsgsxy 95.8x32.0 bg #222222 @ 0.5 image linear-gradient(to right, #000000 @ 0.7, #000000 @ 0.1), none r 16px shadow #000000 @ 0.01 0px 0px 0px 1px, #000000 @ 0.08 0px 2px 4px 0px; button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 32.0x32.0 bg #ffffff @ 0.9 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 50% shadow #000000 @ 0 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 4px, #000000 @ 0.18 0px 2px 4px 0px; button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 32.0x32.0 bg #ffffff @ 0.9 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 50% shadow #000000 @ 0 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 4px, #000000 @ 0.18 0px 2px 4px 0px; span.d840b0v.atm_uc_glywfm__1rrf6b5 16.0x6.0 bg #ffffff @ 0.925 r 12px | = |
| How | at rest | mouse hover |

Crops: `result-card-default.png`, `result-card-hover.png`.

#### result-badge

Listing badge. The white pill over the photo (Guest favourite / Superhost).

Page: search. Selector: `the badge pill inside the result card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 67.84 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Airbnb Cereal VF 14px/18px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Ancestor paint | 1 up div.rl50dte.c1dsgsxy bg #222222 @ 0.5 shadow #000000 @ 0.01 0px 0px 0px 1px, #000000 @ 0.08 0px 2px 4px 0px |
| How | at rest |

Crops: `result-badge-default.png`.

#### result-heart

Wishlist heart. The heart over the photo. Pressed is forced: signed out it opens the sign-up sheet.

Page: search. Selector: `the heart button on the result card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | 34.56 x 34.56 | 34.56 x 34.56 | 29.44 x 29.44 |
| Padding | 2px 0px 0px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 50% | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #222222 0px 0px 0px 2px, #ffffff @ 0.8 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Airbnb Cereal VF 16px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | transform 0.25s cubic-bezier(0.2, 0, 0, 1) | = | box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1) | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #222222, fill #000000 @ 0.5 | 25.92 x 25.92, colour #222222, fill #000000 @ 0.5 | 25.92 x 25.92, colour #222222, fill #000000 @ 0.5 | 22.08 x 22.08, colour #222222, fill #000000 @ 0.5 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1.08, 0, 0, 1.08, 0, 0) | matrix(1.08, 0, 0, 1.08, 0, 0) | matrix(0.92, 0, 0, 0.92, 0, 0) |
| Painted layers | - | = | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 34.6x34.6 r 50% shadow #222222 0px 0px 0px 2px, #ffffff @ 0.8 0px 0px 0px 4px | = |

Crops: `result-heart-default.png`, `result-heart-hover.png`, `result-heart-focus-visible.png`, `result-heart-pressed.png`.

#### fees-tag

All-fees tag. The inline tag over the results grid explaining the total price display.

Page: search. Selector: `the "Prices include all fees" row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 179.69 x 28 | = |
| Padding | 10px 0px 0px 40px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Airbnb Cereal VF 14px/18px 500 | = |
| Letter spacing | normal | = |
| Colour | #000000 @ 0 | = |
| Text node | span.tlsrltq.dir: Airbnb Cereal VF 14px/18px 500, #222222 | = |
| Transition | none | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = |
| How | at rest | mouse hover |

Crops: `fees-tag-default.png`, `fees-tag-hover.png`.

### Room page

#### room-title

Room title. The listing headline under the header.

Page: room. Selector: `main h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 913.5 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Airbnb Cereal VF 26px/30px 500 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| How | at rest |

Crops: `room-title-default.png`.

#### room-share

Share button. The underlined Share action beside Save. Pressed is forced.

Page: room. Selector: `the "Share" button by the title`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 77.14 x 34 | = | = | 74.05 x 32.64 |
| Padding | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f7f7f7 | #f7f7f7 | #f7f7f7 |
| Box shadow | none | = | #222222 0px 0px 0px 2px, #ffffff @ 0.8 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Airbnb Cereal VF 14px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | #000000 | = | #000000 |
| Text node | div.cwdvkr.dir: Airbnb Cereal VF 14px/18px 500, #222222 | div.cwdvkr.dir: Airbnb Cereal VF 14px/18px 500, #000000 | = | div.cwdvkr.dir: Airbnb Cereal VF 14px/18px 500, #000000 |
| Transition | box-shadow, transform 0.2s, 0.1s cubic-bezier(0.2, 0, 0, 1), cubic-bezier(0.2, 0, 0, 1) delay 0s, 0s | = | box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1) | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #222222 | 16 x 16, colour #000000 | = | 15.36 x 15.36, colour #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 77.1x34.0 bg #f7f7f7 r 8px | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 77.1x34.0 bg #f7f7f7 r 8px shadow #222222 0px 0px 0px 2px, #ffffff @ 0.8 0px 0px 0px 4px | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 74.1x32.6 bg #f7f7f7 r 8px |
| Transform | - | = | = | matrix(0.96, 0, 0, 0.96, 0, 0) |

Crops: `room-share-default.png`, `room-share-hover.png`, `room-share-focus-visible.png`, `room-share-pressed.png`.

#### room-save

Save button. The heart+Save action. Pressed is forced: signed out, a real press opens the sign-up sheet.

Page: room. Selector: `the "Save" button by the title`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 71 x 34 | = | = | 68.16 x 32.64 |
| Padding | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f7f7f7 | #f7f7f7 | #f7f7f7 |
| Box shadow | none | = | #222222 0px 0px 0px 2px, #ffffff @ 0.8 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Airbnb Cereal VF 14px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | #000000 | = | #000000 |
| Text node | div.cjwz7r6.dir: Airbnb Cereal VF 14px/18px 500, #222222 | div.cjwz7r6.dir: Airbnb Cereal VF 14px/18px 500, #000000 | = | div.cjwz7r6.dir: Airbnb Cereal VF 14px/18px 500, #000000 |
| Transition | box-shadow, transform 0.2s, 0.1s cubic-bezier(0.2, 0, 0, 1), cubic-bezier(0.2, 0, 0, 1) delay 0s, 0s | = | box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1) | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #222222 | 16 x 16, colour #000000 | = | 15.36 x 15.36, colour #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 71.0x34.0 bg #f7f7f7 r 8px | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 71.0x34.0 bg #f7f7f7 r 8px shadow #222222 0px 0px 0px 2px, #ffffff @ 0.8 0px 0px 0px 4px | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 68.2x32.6 bg #f7f7f7 r 8px |
| Transform | - | = | = | matrix(0.96, 0, 0, 0.96, 0, 0) |

Crops: `room-save-default.png`, `room-save-hover.png`, `room-save-focus-visible.png`, `room-save-pressed.png`.

#### photo-grid

Photo collage. The 5-photo mosaic: one large tile left, a 2x2 grid right, 12px radius.

Page: room. Selector: `the photo mosaic under the title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1120 x 476 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Airbnb Cereal VF 16px/20px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | span.c1tr33ss.c1wv5wxo: Airbnb Cereal VF 12px/16px 500, #222222 |
| Transition | none |
| Icon | 16 x 16, colour #222222 |
| Painted layers | div.hfpy7x4.dir 560.0x476.0 bg #222222 @ 0.1; div::after.c1d4ry4s.atm_k4_18fjjhb_9bj8xt 560pxx476px bg #3f3f3f; div.hfpy7x4.dir 272.0x238.0 bg #222222 @ 0.1; div::after.c1d4ry4s.atm_k4_18fjjhb_9bj8xt 272pxx238px bg #3f3f3f; div.hfpy7x4.dir 272.0x230.0 bg #222222 @ 0.1; div::after.c1d4ry4s.atm_k4_18fjjhb_9bj8xt 272pxx230px bg #3f3f3f |
| How | at rest |

Crops: `photo-grid-default.png`.

#### show-photos

Show all photos button. The white pill bottom-right of the collage. Pressed is forced: it opens the photo viewer.

Page: room. Selector: `the "Show all photos" pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140.28 x 32 | = | = | 138.28 x 30 |
| Padding | 8px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #f2f2f2 | #ebebeb | = | #ebebeb |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #222222 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Airbnb Cereal VF 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | span.c1tr33ss.c1wv5wxo: Airbnb Cereal VF 12px/16px 500, #222222 | = | = | = |
| Transition | box-shadow, transform, background-color, border-color, color 0.2s, 0.25s, 0.3s, 0.3s, 0.3s cubic-bezier(0.2, 0, 0, 1), cubic-bezier(0.2, 0, 0, 1), cubic-bezier(0.2, 0, 0, 1), cubic-bezier(0.2, 0, 0, 1), cubic-bezier(0.2, 0, 0, 1) delay 0s, 0s, 0s, 0s, 0s | = | box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1) | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #222222 | = | = | 15.77 x 15, colour #222222 |
| Painted layers | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 140.3x32.0 bg #f2f2f2 r 8px | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 140.3x32.0 bg #ebebeb r 8px | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 140.3x32.0 bg #f2f2f2 r 8px shadow #ffffff 0px 0px 0px 2px, #222222 0px 0px 0px 4px | button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 138.3x30.0 bg #ebebeb r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.985743, 0, 0, 0.9375, 0, 0) |

Crops: `show-photos-default.png`, `show-photos-hover.png`, `show-photos-focus-visible.png`, `show-photos-pressed.png`.

#### room-subtitle

Listing subtitle. The "Entire rental unit in …" line and the guests/bedrooms/beds row.

Page: room. Selector: `the subtitle under the collage`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 653.33 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Airbnb Cereal VF 22px/26px 500 |
| Letter spacing | -0.44px |
| Colour | #222222 |
| Text node | h2.rghzvl1.atm_kd_idpfg4_pfnrn2: Airbnb Cereal VF 22px/26px 500, #222222, ls -0.44px |
| Transition | none |
| How | at rest |

Crops: `room-subtitle-default.png`.

#### guest-plaque

Guest favourite plaque. The laurel-bordered strip: "Guest favourite / One of the most loved homes on Airbnb" with the rating and review count.

Page: room. Selector: `the laurel plaque under the subtitle`. States: default.

Not found on the page at capture time.

#### reserve-card

Reservation card. The booking card pinned right: "Add dates for prices", the CHECK-IN/CHECK-OUT/GUESTS field grid. Nothing was booked.

Page: room. Selector: `the card with the date and guest fields`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 372.33 x 312 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Airbnb Cereal VF 16px/20px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | span.u10vhw1l.dir: Airbnb Cereal VF 22px/26px 500, #222222 |
| Transition | none |
| Icon | 16 x 16, colour #222222 |
| ::before | 372.328px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 372.328px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | aside.b13oolvs.atm_6h_idpfg4_vmdu4 372.3x280.0 border T:1px solid #dddddd / R:1px solid #dddddd / B:1px solid #dddddd / L:1px solid #dddddd r 12px shadow #000000 @ 0.12 0px 6px 16px 0px; div.r4cfcaw.rx1v2qp 322.3x116.0 bg #ffffff r 12px; button.c1nv5ob0.dir 322.3x56.0 bg #ffffff; div.cwf8ttw.ilm12jv 161.7x56.0 border L:1px solid #8c8c8c; div.fj95cgj.d1h1yz8o 322.3x57.0 border T:1px solid #8c8c8c / R:1px solid #8c8c8c / B:1px solid #8c8c8c / L:1px solid #8c8c8c r 12px 12px 0px 0px; div.fj95cgj.d1h1yz8o 322.3x61.0 border T:1px solid #8c8c8c / R:1px solid #8c8c8c / B:1px solid #8c8c8c / L:1px solid #8c8c8c r 0px 0px 12px 12px |
| How | at rest |

Crops: `reserve-card-default.png`.

#### reserve-field

Date field. A labelled field cell in the booking grid (CHECK-IN / CHECKOUT / GUESTS).

Page: room. Selector: `the CHECK-IN field cell`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 160.67 x 56 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Airbnb Cereal VF 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | div.kpk3g6v.dir: Airbnb Cereal VF 10px/12px 700, #222222 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Ancestor paint | 1 up button.c1nv5ob0.dir bg #ffffff | = |
| How | at rest | mouse hover |

Crops: `reserve-field-default.png`, `reserve-field-hover.png`.

#### promo-strip

Promo strip. The discount banner ("Get $25 SGD off your getaway") with the outlined Claim button. Measured, never pressed.

Page: room. Selector: `the promo banner near the top of the listing`. States: default.

Not found on the page at capture time.

#### promo-claim

Claim button. The outlined Claim action on the promo strip. Pressed is forced: claiming needs an account.

Page: room. Selector: `the Claim button on the promo strip`. States: default, hover, focus-visible, pressed.

Not found on the page at capture time.

#### host-row

Host row. The "Hosted by" row with the circular avatar.

Page: room. Selector: `the Hosted-by row under the plaque`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 148.64 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Airbnb Cereal VF 16px/20px 500 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| How | at rest |

Crops: `host-row-default.png`.

### Host landing

#### host-hero

Host headline. "Your home could make money on Airbnb".

Page: host. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 556 x 192 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Airbnb Cereal VF 60px/64px 700 |
| Letter spacing | -1.8px |
| Colour | #222222 |
| Transition | none |
| How | at rest |

Crops: `host-hero-default.png`.

#### host-cta

Get started button. The rausch CTA in the nav and on the page. Pressed is forced: it starts the host sign-up flow.

Page: host. Selector: `a "Get started" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 143.92 x 48 | = | = | 138.17 x 46.08 |
| Padding | 14px 28px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | transparent | = | = | #ff385c |
| Background image | linear-gradient(to right, #e61e4d 0%, #e31c5f 50%, #d70466 100%) | = | = | - |
| Box shadow | none | = | #ffffff @ 0.8 0px 0px 0px 2px, #222222 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Airbnb Cereal VF 16px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.cbx4cei.dir: Airbnb Cereal VF 16px/20px 500, #ffffff | = | = | = |
| Transition | box-shadow, transform 0.2s, 0.1s cubic-bezier(0.2, 0, 0, 1), cubic-bezier(0.2, 0, 0, 1) delay 0s, 0s | = | box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1) | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 143.9x48.0 image linear-gradient(to right, #e61e4d 0%, #e31c5f 50%, #d70466 100%) r 40px; span.t1setlb.atm_k4_kb7nvz_1nos8r 200.0x48.0 image radial-gradient(circle, #ff385c 0%, #e61e4d 27.5%, #e31c5f 40%, #d70466 57.5%, #bd1e59 75% | = | a.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 143.9x48.0 image linear-gradient(to right, #e61e4d 0%, #e31c5f 50%, #d70466 100%) r 40px shadow #ffffff @ 0.8 0px 0px 0px 2px, #222222 0px 0px 0px 4px; span.t1setlb.atm_k4_kb7nvz_1nos8r 200.0x48.0 image radial-gradient(circle, #ff385c 0%, #e61e4d 27.5%, #e31c5f 40%, #d70466 57.5%, #bd1e59 75% | a.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 138.2x46.1 bg #ff385c r 40px; span.t1setlb.atm_k4_kb7nvz_1nos8r 192.0x46.1 image radial-gradient(circle, #ff385c 0%, #e61e4d 27.5%, #e31c5f 40%, #d70466 57.5%, #bd1e59 75% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.96, 0, 0, 0.96, 0, 0) |

Crops: `host-cta-default.png`, `host-cta-hover.png`, `host-cta-focus-visible.png`, `host-cta-pressed.png`.

#### estimator-card

Earnings estimator. The interactive earnings card (location field, guest slider, monthly total). Measured at rest; nothing was submitted.

Page: host. Selector: `the earnings estimate card on the host page`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 376 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Airbnb Cereal VF 14px/20.02px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | h1.wt4h85h.atm_eh_4b0q0n_126qwya: Airbnb Cereal VF 60px/64px 700, #222222, ls -1.8px |
| Transition | none |
| Icon | 16 x 16, colour #222222 |
| Painted layers | button.c1n9sd8s.atm_kd_glywfm_pfnrn2 418.0x64.0 bg #ffffff border T:1px solid #dddddd / R:1px solid #dddddd / B:1px solid #dddddd / L:1px solid #dddddd r 40px |
| How | at rest |

Crops: `estimator-card-default.png`.

### Mobile (390 wide)

#### m-search-pill

Mobile search pill. The compact search bar at the top of the mobile home.

Page: mobile. Selector: `the search pill under the header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 68 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Airbnb Cereal VF 14px/20.02px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | span.pyaa2he.dir: Airbnb Cereal VF 14px/18px 500, #222222 |
| Transition | none |
| Icon | 12 x 12, colour #222222 |
| Painted layers | div.csvqdle.c4r49d2 390.0x68.0 bg #ffffff; button.l1lx1n3h.atm_npmupv_14b5rvc_10saat9 342.0x56.0 bg #ffffff border T:1px solid #dddddd / R:1px solid #dddddd / B:1px solid #dddddd / L:1px solid #dddddd r 9999px shadow #000000 @ 0.1 0px 6px 20px 0px; dialog.dhbx8r3.cu89ibe 0.0x0.0 bg #f0f0f0 @ 0.86 |
| How | at rest |

Crops: `m-search-pill-default.png`.

#### m-listing-card

Mobile listing card. A home card in the mobile rail: full-bleed photo, badge, heart, title, price.

Page: mobile. Selector: `the first listing card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 165 x 214.75 |
| Padding | 0px |
| Border | none |
| Radius | 20px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Airbnb Cereal VF 14px/20.02px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | span.t8mq7ht.tpka78r: Airbnb Cereal VF 11px/13px 600, #222222 |
| Transition | none |
| Icon | 24 x 24, colour #222222, fill #000000 @ 0.5 |
| Painted layers | div.c11jbcjg.atm_ks_zryt35__1rgatj2 165.0x156.8 bg #dddddd r 20px shadow #000000 @ 0.02 0px 0px 0px 1px, #000000 @ 0.1 0px 8px 24px 0px; div.rxuv6ej.rjcf2mg 103.6x26.0 bg #ffffff @ 0.8 border T:1px solid #ffffff @ 0.5 / R:1px solid #ffffff @ 0.5 / B:1px solid #ffffff @ 0.5 / L:1px solid #ffffff @ 0.5 r 14px shadow #000000 @ 0.02 0px 0px 0px 1px, #000000 @ 0.04 0px 2px 6px 0px, #000000 @ 0.1 0px 4px 8px 0px |
| How | at rest |

Crops: `m-listing-card-default.png`.

## Transitions declared in the readable stylesheets

Airbnb serves its stylesheet same-origin, so the CSSOM read every rule on each page; the per-state Transition rows above are the computed values and this list holds the declared transition properties on the elements measured.
