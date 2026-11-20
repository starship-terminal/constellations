# Component measurements

Computed styles read from dailyartmagazine.com on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the home, /latest/, /category/art-movements/impressionism/, an article, /about-dailyart-magazine/, /contact/ and /?s=van+gogh (the Mobile group on the home) — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### nav-bar

Top header. The full-width top bar over the dark hero: hamburger, Stories/Shop/Courses, wordmark, social icons and the Search button.

Page: home. Selector: `#top-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 65 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #19191c |
| Box shadow | none |
| Outline | none |
| Font | Basier 16px/16px 400 |
| Letter spacing | -0.288px |
| Colour | #4d5761 |
| Text node | a: Basier 14px/17px 600, #ffffff |
| Transition | all 0.5s ease |
| Icon | 0 x 0, colour #000000 |
| Painted layers | header 1440.0x65.0 bg #19191c; div.wrapper 1440.0x65.0 bg #19191c; div.ham-border 36.8x37.0 bg #19191c border T:1px solid #c6002f / R:1px solid #c6002f / B:1px solid #c6002f / L:1px solid #c6002f r 3px; span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff |
| How | at rest |

Crops: `nav-bar-default.png`.

#### nav-logo

Logo. The DailyArt Magazine wordmark (inline SVG).

Page: home. Selector: `a.logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 111 x 30.17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 16px/16px 400 |
| Letter spacing | -0.288px |
| Colour | #0000ee |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, -55.5, -15.0859) |
| Cursor | pointer |
| Icon | 111 x 28.17, colour #0000ee, fill #000000 |
| Ancestor paint | 1 up div.wrapper bg #19191c |
| How | at rest |

Crops: `nav-logo-default.png`.

#### nav-link

Nav link. "Stories" — a primary-nav item; measured, never followed.

Page: home. Selector: `#primary-top-menu a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 46.48 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #ffffff offset 1px | = |
| Font | Basier 14px/17px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 0px x 2px, absolute, bg #ffffff, radius 0px | 45.9844px x 2px, absolute, bg #ffffff, radius 0px | = | 43.3281px x 2px, absolute, bg #ffffff, radius 0px |
| Painted layers | a::after 0pxx2px bg #ffffff | a::after 45.9844pxx2px bg #ffffff | a 46.5x18.0 outline 1px dotted #ffffff offset 1px; a::after 0pxx2px bg #ffffff | a::after 43.3281pxx2px bg #ffffff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-outbound

Outbound nav link. "Shop" — outbound to shop.dailyartmagazine.com; measured, never followed.

Page: home. Selector: `#primary-top-menu a[target="_blank"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 33.28 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #ffffff offset 1px | = |
| Font | Basier 14px/17px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 0px x 2px, absolute, bg #ffffff, radius 0px | 32.9062px x 2px, absolute, bg #ffffff, radius 0px | = | 32.1875px x 2px, absolute, bg #ffffff, radius 0px |
| Painted layers | a::after 0pxx2px bg #ffffff | a::after 32.9062pxx2px bg #ffffff | a 33.3x18.0 outline 1px dotted #ffffff offset 1px; a::after 0pxx2px bg #ffffff | a::after 32.1875pxx2px bg #ffffff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-outbound-default.png`, `nav-outbound-hover.png`, `nav-outbound-focus-visible.png`, `nav-outbound-pressed.png`.

#### hamburger

Hamburger. The six-bar hamburger that toggles the fixed-nav category menu.

Page: home. Selector: `#hamburger`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 20 x 15 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Basier 16px/16px 400 | = | = |
| Letter spacing | -0.288px | = | = |
| Colour | #4d5761 | = | = |
| Transition | all 0.5s ease-in-out | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = |
| Cursor | pointer | = | = |
| Painted layers | span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff | = | = |
| Ancestor paint | 1 up div.ham-border bg #19191c | 1 up div.ham-border bg #c6002f | = |
| How | at rest | mouse hover | CDP forcePseudoState :active:hover |

Crops: `hamburger-default.png`, `hamburger-hover.png`, `hamburger-pressed.png`.

#### cat-nav

Category nav. The fixed-nav category menu (Art Movements tree) opened by the hamburger.

Page: home. Selector: `nav.fixed-nav`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 1440 x 633 |
| Padding | 20px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.25 0px 16px 48px 0px |
| Outline | none |
| Font | Basier 16px/16px 400 |
| Letter spacing | -0.288px |
| Colour | #4d5761 |
| Text node | a: RoslindaleNarrow 16px/18px 600, #000000, ls 0.16px |
| Transition | all 1s ease |
| Transform | matrix(1, 0, 0, 1, -720, 0) |
| Icon | 0 x 0, colour #0000ee |
| ::before | 0px x 633px, absolute, bg #000000 @ 0, radius 0px |
| ::after | 0px x 633px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | nav.fixed-nav.navigation 1440.0x633.0 bg #ffffff shadow #000000 @ 0.25 0px 16px 48px 0px; a 298.3x59.0 border B:1px solid #2e2e32; li::after.promo-category.menu-item 4pxx4px bg #c6002f r 50%; li::after.promo-category.menu-item 4pxx4px bg #c6002f r 50%; li::after.promo-category.menu-item 4pxx4px bg #c6002f r 50%; a 149.1x59.0 border B:1px solid #2e2e32 |
| Ancestor paint | 1 up header bg #19191c |
| How | held open by an earlier toggle |

Crops: none.

#### cat-nav-item

Category nav item. A top-level category link ("Art Movements") in the opened nav; measured, never followed.

Page: home. Selector: `nav.fixed-nav #primary-menu > li > a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 298.3 x 59 | - | = | = |
| Padding | 20px 0px | - | = | = |
| Border | T: none; R: none; B: 1px solid #2e2e32; L: none | - | = | = |
| Radius | 0px | - | = | = |
| Background | transparent | - | = | = |
| Box shadow | none | - | = | = |
| Outline | none | - | 1px dotted #000000 offset 1px | = |
| Font | RoslindaleNarrow 16px/18px 600 | - | = | = |
| Letter spacing | 0.16px | - | = | = |
| Colour | #000000 | - | = | = |
| Transition | all 0.3s ease | - | = | = |
| Cursor | pointer | - | = | = |
| Painted layers | a 298.3x59.0 border B:1px solid #2e2e32 | - | a 298.3x59.0 border B:1px solid #2e2e32 outline 1px dotted #000000 offset 1px | = |
| How | at rest | - | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Error | - | locator.hover: Element is outside of the viewport Call log:   - waiting for locator('nav.fixed-nav #primary-menu > li > a, nav.navigation #primary-menu > li > a').visible().first().visible().first().v | = | = |

Crops: `cat-nav-item-default.png`, `cat-nav-item-focus-visible.png`, `cat-nav-item-pressed.png`.

#### cat-nav-sub

Category sub-menu item. A sub-menu link ("Prehistoric Art") painted while its parent is hovered in the opened nav; measured, never followed.

Page: home. Selector: `nav.fixed-nav .sub-menu a`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 92.25 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 14px/18px 400 |
| Letter spacing | -0.21px |
| Colour | #c6002f |
| Transition | all 0.3s ease |
| Cursor | pointer |
| How | held open by an earlier toggle |

Crops: `cat-nav-sub-opened.png`.

#### search-btn

Search button. The "Search" button in the header (a submit that GETs /?s=); measured, never submitted.

Page: home. Selector: `.social-media form button.primary.btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 87.5 x 38 | = | = | = |
| Padding | 9px 20px | = | = | = |
| Border | 1px solid #c6002f | = | = | = |
| Radius | 3px | = | = | = |
| Background | transparent | #c6002f | = | #c6002f |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Basier 14px/normal 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.primary.btn 87.5x38.0 border T:1px solid #c6002f / R:1px solid #c6002f / B:1px solid #c6002f / L:1px solid #c6002f r 3px | button.primary.btn 87.5x38.0 bg #c6002f border T:1px solid #c6002f / R:1px solid #c6002f / B:1px solid #c6002f / L:1px solid #c6002f r 3px | = | button.primary.btn 87.5x38.0 bg #c6002f border T:1px solid #c6002f / R:1px solid #c6002f / B:1px solid #c6002f / L:1px solid #c6002f r 3px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-btn-default.png`, `search-btn-hover.png`, `search-btn-focus-visible.png`, `search-btn-pressed.png`.

#### nl-form

Newsletter form. The newsletter signup form (email + consent checkbox + send).

Page: home. Selector: `form.newsletter-form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 368 x 180 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 16px/16px 400 |
| Letter spacing | -0.288px |
| Colour | #4d5761 |
| Text node | p.small-p: Basier 14px/18px 400, #606a73, ls -1.8% |
| Transition | none |
| Painted layers | input.email.email-newsletter 368.0x40.0 bg #ffffff border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 3px; label::after 16pxx16px bg #ffffff border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 2px; button.primary.btn 368.0x38.0 border T:1px solid #c6002f / R:1px solid #c6002f / B:1px solid #c6002f / L:1px solid #c6002f r 3px |
| How | at rest |

Crops: `nl-form-default.png`.

#### nl-email

Newsletter email field. The newsletter email input; typed into for the filled state, then cleared — never submitted.

Page: home. Selector: `input.email-newsletter`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 368 x 40 | = | = |
| Padding | 10px | = | = |
| Border | 1px solid #989da7 | 1px solid #000000 | 1px solid #000000 |
| Radius | 3px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Basier 14px/18px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | all 0.3s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| Painted layers | input.email.email-newsletter 368.0x40.0 bg #ffffff border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 3px | input.email.email-newsletter 368.0x40.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 3px | input.email.email-newsletter 368.0x40.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 3px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `nl-email-default.png`, `nl-email-focused.png`, `nl-email-filled.png`.

#### nl-checkbox

Newsletter consent checkbox. The required consent checkbox; measured, never toggled.

Page: home. Selector: `.newsletter-form input[type="checkbox"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 13 x 13 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Basier 14px/18px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | all 0.3s ease | = |
| Opacity | 0 | = |
| Cursor | default | = |
| Placeholder | #000000, opacity 1 | = |
| How | at rest | mouse hover |

Crops: `nl-checkbox-default.png`, `nl-checkbox-hover.png`.

#### nl-send

Newsletter send button. The newsletter submit; measured, never submitted.

Page: home. Selector: `.newsletter-send`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 368 x 38 | = | = | = |
| Padding | 9px 20px | = | = | = |
| Border | 1px solid #c6002f | = | = | = |
| Radius | 3px | = | = | = |
| Background | transparent | #c6002f | = | #c6002f |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Basier 14px/normal 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #ffffff | = | #ffffff |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.primary.btn 368.0x38.0 border T:1px solid #c6002f / R:1px solid #c6002f / B:1px solid #c6002f / L:1px solid #c6002f r 3px | button.primary.btn 368.0x38.0 bg #c6002f border T:1px solid #c6002f / R:1px solid #c6002f / B:1px solid #c6002f / L:1px solid #c6002f r 3px | = | button.primary.btn 368.0x38.0 bg #c6002f border T:1px solid #c6002f / R:1px solid #c6002f / B:1px solid #c6002f / L:1px solid #c6002f r 3px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nl-send-default.png`, `nl-send-hover.png`, `nl-send-focus-visible.png`, `nl-send-pressed.png`.

#### footer

Footer. The footer band: six link menus, social icons and the newsletter form.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 842 |
| Padding | 0px 20px 50px 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 16px/16px 400 |
| Letter spacing | -0.288px |
| Colour | #4d5761 |
| Text node | span.small-heading: Basier 12px/14px 700, #000000, ls -0.24px |
| Transition | none |
| Painted layers | div.separator 1152.0x1.0 bg #000000; div.separator 561.0x1.0 bg #000000; div.separator 561.0x1.0 bg #000000; input.email-newsletter 561.0x40.0 bg #ffffff border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 3px; label::after 16pxx16px bg #ffffff border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 2px; button.primary.btn 561.0x38.0 border T:1px solid #c6002f / R:1px solid #c6002f / B:1px solid #c6002f / L:1px solid #c6002f r 3px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. "About Us" — a footer menu link; measured, never followed.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 58.77 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #c6002f offset 1px | = |
| Font | Basier 14px/18px 400 | = | = | = |
| Letter spacing | -0.21px | = | = | = |
| Colour | #c6002f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 58.8x18.0 outline 1px dotted #c6002f offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-link

Social icon link. A social-media icon link; measured, never followed.

Page: home. Selector: `.social-media a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 10 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #0000ee offset 1px | = |
| Font | Basier 16px/16px 400 | = | = | = |
| Letter spacing | -0.288px | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 16, colour #0000ee | 13 x 20.8, colour #0000ee | = | 13 x 20.8, colour #ff0000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 10.0x18.0 outline 1px dotted #0000ee offset 1px | = |

Crops: `social-link-default.png`, `social-link-hover.png`, `social-link-focus-visible.png`, `social-link-pressed.png`.

#### nl-modal

Newsletter modal. The newsletter dialog (720px white box on a 90%-black overlay); opened with the site's own .modal-r--show class — it never self-mounted during the public pass.

Page: home. Selector: `section.newsletter-modal`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 720 x 156.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Basier 16px/16px 400 |
| Letter spacing | -0.288px |
| Colour | #4d5761 |
| Text node | p.small-p: Basier 16px/21.6px 400, #000000, ls -0.288px |
| Transition | none |
| Painted layers | section.donation.newsletter-modal 720.0x156.8 bg #ffffff; input.email-newsletter 0.0x0.0 bg #ffffff border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7; label::after 16pxx16px bg #ffffff border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 2px; button.btn.btn-box-l 0.0x0.0 bg #c6002f r 3px |
| Ancestor paint | 1 up div.modal-r.modal-r--show bg #000000 @ 0.9 |
| How | opened via the .modal-r--show class the site toggles — the modal never self-mounted on the public surface |

Crops: `nl-modal-default.png`.

#### nav-cluster

Nav cluster. The left cluster inside the header: hamburger + the Stories/Shop/Courses menu.

Page: home. Selector: `nav.primary-navigation`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 300.08 x 37 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 16px/16px 400 |
| Letter spacing | -0.288px |
| Colour | #4d5761 |
| Text node | a: Basier 14px/17px 600, #ffffff |
| Transition | none |
| Icon | 0 x 0, colour #000000 |
| Painted layers | div.ham-border 36.8x37.0 bg #19191c border T:1px solid #c6002f / R:1px solid #c6002f / B:1px solid #c6002f / L:1px solid #c6002f r 3px; span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff |
| Ancestor paint | 1 up div.wrapper bg #19191c |
| How | at rest |

Crops: `nav-cluster-default.png`.

### Home

#### feed-tab

Feed tab. The Latest/Trending tab label in the main feed heading.

Page: home. Selector: `.main-p-tab`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 62.94 x 33 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | RoslindaleCondensed 28px/32px 500 | = |
| Letter spacing | 0.32px | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `feed-tab-default.png`, `feed-tab-hover.png`.

#### feed-tab-active

Feed tab (active). The active feed tab ("Latest").

Page: home. Selector: `.main-p-tab-active`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 62.94 x 33 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | RoslindaleCondensed 28px/32px 500 |
| Letter spacing | 0.32px |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `feed-tab-active-default.png`.

#### browse-link

Browse-more link. "Browse More" beside the feed heading; measured, never followed.

Page: home. Selector: `a.link-browse`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 86.73 x 14 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #c6002f offset 1px | = |
| Font | Basier 12px/14px 700 | = | = | = |
| Letter spacing | -0.24px | = | = | = |
| Colour | #c6002f | = | = | = |
| Transition | all 0.5s ease | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 0px x 2px, absolute, bg #000000 @ 0, radius 0px | 85.7656px x 2px, absolute, bg #000000 @ 0, radius 0px | = | 80.8594px x 2px, absolute, bg #000000 @ 0, radius 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.801133 | = | 0.8068 |
| Painted layers | - | = | a.link.link-browse-more-latest 86.7x14.0 outline 1px dotted #c6002f offset 1px | = |

Crops: `browse-link-default.png`, `browse-link-hover.png`, `browse-link-focus-visible.png`, `browse-link-pressed.png`.

#### post-card-h

Post card (horizontal). A horizontal story card in the Latest feed.

Page: home. Selector: `.single-post__horizontal`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 760 x 194 | = |
| Padding | 0px 0px 16px 0px | = |
| Border | T: none; R: none; B: 1px solid #ebeced; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Basier 16px/16px 400 | = |
| Letter spacing | -0.288px | = |
| Colour | #4d5761 | = |
| Text node | a.category: Basier 10px/12.25px 700, #ffffff, ls -0.15px | = |
| Transition | none | = |
| Painted layers | div.single-post.single-post__horizontal 760.0x194.0 border B:1px solid #ebeced; a.category 30.9x20.3 bg #c6002f r 3px | = |
| How | at rest | mouse hover |

Crops: `post-card-h-default.png`, `post-card-h-hover.png`.

#### post-card-img

Card image. The card's 264x177 thumbnail block.

Page: home. Selector: `.post-image`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 260 x 177 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 16px/16px 400 |
| Letter spacing | -0.288px |
| Colour | #4d5761 |
| Text node | a.category: Basier 10px/12.25px 700, #ffffff, ls -0.15px |
| Transition | none |
| Painted layers | a.category 30.9x20.3 bg #c6002f r 3px |
| How | at rest |

Crops: `post-card-img-default.png`.

#### post-card-title

Card title link. A story title link inside a feed card; measured, never followed.

Page: home. Selector: `.post-content a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 412.23 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #000000 offset 1px | = |
| Font | RoslindaleNarrow 20px/24px 700 | = | = | = |
| Letter spacing | 0.4px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 412.2x48.0 outline 1px dotted #000000 offset 1px | = |

Crops: `post-card-title-default.png`, `post-card-title-hover.png`, `post-card-title-focus-visible.png`, `post-card-title-pressed.png`.

#### post-card-excerpt

Card excerpt. The story excerpt paragraph under a card title.

Page: home. Selector: `.post-excerpt`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 452 x 24 |
| Padding | 4px 0px 20px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 16px/24px 400 |
| Letter spacing | -1.8% |
| Colour | #606a73 |
| Transition | none |
| How | at rest |

Crops: `post-card-excerpt-default.png`.

#### post-card-cat

Category chip. The pink category chip on a card image ("Quiz", "Asian Art"); measured, never followed.

Page: home. Selector: `.single-post a.category`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 119.31 x 20.25 | = | = | = |
| Padding | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 3px | = | = | = |
| Background | #c6002f | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #ffffff offset 1px | = |
| Font | Basier 10px/12.25px 700 | = | = | = |
| Letter spacing | -0.15px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 41px x 1px, absolute, bg #2e2e32, radius 0px | = | = | = |
| ::after | 41px x 1px, absolute, bg #2e2e32, radius 0px | = | = | = |
| Painted layers | a.category 119.3x20.3 bg #c6002f r 3px; a::before.category 41pxx1px bg #2e2e32; a::after.category 41pxx1px bg #2e2e32 | = | a.category 119.3x20.3 bg #c6002f r 3px outline 1px dotted #ffffff offset 1px; a::before.category 41pxx1px bg #2e2e32; a::after.category 41pxx1px bg #2e2e32 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `post-card-cat-default.png`, `post-card-cat-hover.png`, `post-card-cat-focus-visible.png`, `post-card-cat-pressed.png`.

#### post-card-author

Author link. A byline author link; measured, never followed.

Page: home. Selector: `.author-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 103.73 x 15 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #f3003a offset 1px | = |
| Font | Basier 12px/14px 700 | = | = | = |
| Letter spacing | -0.24px | = | = | = |
| Colour | #f3003a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.author-link 103.7x15.0 outline 1px dotted #f3003a offset 1px | = |

Crops: `post-card-author-default.png`, `post-card-author-hover.png`, `post-card-author-focus-visible.png`, `post-card-author-pressed.png`.

#### post-card-date

Card date. A card's publication date.

Page: home. Selector: `.single-post .date`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 143.02 x 15 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 12px/14px 700 |
| Letter spacing | -0.24px |
| Colour | #000000 |
| Transition | none |
| ::before | auto x auto, relative, bg #000000 @ 0, radius 0px |
| ::after | auto x auto, relative, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `post-card-date-default.png`.

#### post-card-v

Post card (vertical). A vertical/small story card.

Page: home. Selector: `.single-post__vertical`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 275.5 x 292.75 | = |
| Padding | 0px 0px 20px 0px | = |
| Border | T: none; R: none; B: 1px solid #2e2e32; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Basier 16px/16px 400 | = |
| Letter spacing | -0.288px | = |
| Colour | #ffffff | = |
| Text node | a.category: Basier 10px/12.25px 700, #ffffff, ls -0.15px | = |
| Transition | none | = |
| Painted layers | div.single-post.single-post__vertical 275.5x292.8 border B:1px solid #2e2e32; a.category 119.3x20.3 bg #c6002f r 3px; a::before.category 41pxx1px bg #2e2e32; a::after.category 41pxx1px bg #2e2e32 | = |
| How | at rest | mouse hover |

Crops: `post-card-v-default.png`, `post-card-v-hover.png`.

#### load-more

Load-more button. The feed's "load more" control; measured, never clicked.

Page: home. Selector: `.load-more-arts`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 760 x 38 | = | = | = |
| Padding | 9px 20px | = | = | = |
| Border | 1px solid #c6002f | = | = | = |
| Radius | 3px | = | = | = |
| Background | transparent | #c6002f | = | #c6002f |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Basier 14px/normal 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #ffffff | = | #ffffff |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.primary.btn 760.0x38.0 border T:1px solid #c6002f / R:1px solid #c6002f / B:1px solid #c6002f / L:1px solid #c6002f r 3px | button.primary.btn 760.0x38.0 bg #c6002f border T:1px solid #c6002f / R:1px solid #c6002f / B:1px solid #c6002f / L:1px solid #c6002f r 3px | = | button.primary.btn 760.0x38.0 bg #c6002f border T:1px solid #c6002f / R:1px solid #c6002f / B:1px solid #c6002f / L:1px solid #c6002f r 3px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `load-more-default.png`, `load-more-hover.png`, `load-more-focus-visible.png`, `load-more-pressed.png`.

#### donation

Donation block. The donation call-out block.

Page: home. Selector: `.donation`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 760 x 385.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 16px/16px 400 |
| Letter spacing | -0.288px |
| Colour | #4d5761 |
| Text node | span.pink: RoslindaleCondensed 28px/33.6px 500, #f997af, ls 0.28px |
| Transition | none |
| Painted layers | div::before.donate-row.is-bg-ready 760pxx385.562px bg #c6002f; a.btn 100.0x40.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 3px; a.btn 100.0x40.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 3px; a.btn 100.0x40.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 3px; a.btn 100.0x40.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 3px; a.btn 150.0x40.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 3px |
| How | at rest |

Crops: `donation-default.png`.

#### ad-slot

Ad slot. A painted a.pub.network ad placeholder (billboard/leaderboard/right-rail); read, never clicked.

Page: home. Selector: `[id^="dailyartmagazine_"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 760 x 98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 16px/0px 400 |
| Letter spacing | -0.288px |
| Colour | #4d5761 |
| Transition | none |
| Painted layers | div.separator 760.0x1.0 bg #ebeced |
| How | at rest |

Crops: none.

#### hero-block

Hero block. The dark hero section over the white page ("Scandalous Rodin" featured story + side cards).

Page: home. Selector: `section.intro`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 798.75 |
| Padding | 63px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | #19191c |
| Box shadow | none |
| Outline | none |
| Font | Basier 16px/16px 400 |
| Letter spacing | -0.288px |
| Colour | #4d5761 |
| Text node | span.category.center: Basier 10px/12.25px 700, #ffffff, ls -0.15px |
| Transition | none |
| Painted layers | section.intro.intro-posts 1440.0x798.8 bg #19191c; span.category.center 93.3x20.3 bg #c6002f r 3px; span::before.category.center 41pxx1px bg #2e2e32; span::after.category.center 41pxx1px bg #2e2e32; div.single-post.single-post__vertical 275.5x292.8 border B:1px solid #2e2e32; a.category 119.3x20.3 bg #c6002f r 3px |
| How | at rest |

Crops: `hero-block-default.png`.

#### hero-tag

Hero tag. The "Featured Story" pink pill above the hero title.

Page: home. Selector: `.intro .category`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 93.34 x 20.25 |
| Padding | 4px |
| Border | none |
| Radius | 3px |
| Background | #c6002f |
| Box shadow | none |
| Outline | none |
| Font | Basier 10px/12.25px 700 |
| Letter spacing | -0.15px |
| Colour | #ffffff |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| ::before | 41px x 1px, absolute, bg #2e2e32, radius 0px |
| ::after | 41px x 1px, absolute, bg #2e2e32, radius 0px |
| Painted layers | span.category.center 93.3x20.3 bg #c6002f r 3px; span::before.category.center 41pxx1px bg #2e2e32; span::after.category.center 41pxx1px bg #2e2e32 |
| How | at rest |

Crops: `hero-tag-default.png`.

#### hero-h1

Hero heading. "Scandalous Rodin" — the serif hero title on the dark block.

Page: home. Selector: `.intro h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 900 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | RoslindaleCondensed 56px/60px 500 |
| Letter spacing | 0.56px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-card

Hero card. A story card inside the dark hero.

Page: home. Selector: `.intro .single-post`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 275.5 x 292.75 | = |
| Padding | 0px 0px 20px 0px | = |
| Border | T: none; R: none; B: 1px solid #2e2e32; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Basier 16px/16px 400 | = |
| Letter spacing | -0.288px | = |
| Colour | #ffffff | = |
| Text node | a.category: Basier 10px/12.25px 700, #ffffff, ls -0.15px | = |
| Transition | none | = |
| Painted layers | div.single-post.single-post__vertical 275.5x292.8 border B:1px solid #2e2e32; a.category 119.3x20.3 bg #c6002f r 3px; a::before.category 41pxx1px bg #2e2e32; a::after.category 41pxx1px bg #2e2e32 | = |
| How | at rest | mouse hover |

Crops: `hero-card-default.png`, `hero-card-hover.png`.

#### section-heading

Section heading. A big serif section heading ("Latest" / "Long reads" / "Featured").

Page: home. Selector: `h3.big`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 104.67 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | RoslindaleCondensed 32px/40px 500 |
| Letter spacing | 0.32px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `section-heading-default.png`.

### Latest

#### latest-h1

Index heading. The stories index heading.

Page: latest. Selector: `latest h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 125.39 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | RoslindaleCondensed 56px/60px 500 |
| Letter spacing | 0.56px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `latest-h1-default.png`.

#### latest-row

Story row. A story row on the Latest index.

Page: latest. Selector: `.single-post`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 760 x 194 | = |
| Padding | 0px 0px 16px 0px | = |
| Border | T: none; R: none; B: 1px solid #ebeced; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Basier 16px/16px 400 | = |
| Letter spacing | -0.288px | = |
| Colour | #4d5761 | = |
| Text node | a.category: Basier 10px/12.25px 700, #ffffff, ls -0.15px | = |
| Transition | none | = |
| Painted layers | div.single-post.single-post__horizontal 760.0x194.0 border B:1px solid #ebeced; a.category 59.9x20.3 bg #c6002f r 3px | = |
| How | at rest | mouse hover |

Crops: `latest-row-default.png`, `latest-row-hover.png`.

#### latest-link

Story link. A story title link on the index; measured, never followed.

Page: latest. Selector: `.post-content a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 407.2 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #000000 offset 1px | = |
| Font | RoslindaleNarrow 20px/24px 700 | = | = | = |
| Letter spacing | 0.4px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 407.2x48.0 outline 1px dotted #000000 offset 1px | = |

Crops: `latest-link-default.png`, `latest-link-hover.png`, `latest-link-focus-visible.png`, `latest-link-pressed.png`.

### Category

#### cat-h1

Category heading. "Impressionism" — the category archive heading.

Page: category. Selector: `category h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 304.38 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | RoslindaleCondensed 56px/60px 500 |
| Letter spacing | 0.56px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `cat-h1-default.png`.

#### cat-card

Archive card. A story card in the category archive.

Page: category. Selector: `.single-post`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 760 x 194 | = |
| Padding | 0px 0px 16px 0px | = |
| Border | T: none; R: none; B: 1px solid #ebeced; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Basier 16px/16px 400 | = |
| Letter spacing | -0.288px | = |
| Colour | #4d5761 | = |
| Text node | a.category: Basier 10px/12.25px 700, #ffffff, ls -0.15px | = |
| Transition | none | = |
| Painted layers | div.single-post.single-post__horizontal 760.0x194.0 border B:1px solid #ebeced; a.category 85.7x20.3 bg #c6002f r 3px | = |
| How | at rest | mouse hover |

Crops: `cat-card-default.png`, `cat-card-hover.png`.

#### cat-card-title

Archive title link. An archive card title link; measured, never followed.

Page: category. Selector: `.single-post a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 280.23 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #000000 offset 1px | = |
| Font | RoslindaleNarrow 20px/24px 700 | = | = | = |
| Letter spacing | 0.4px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 280.2x24.0 outline 1px dotted #000000 offset 1px | = |

Crops: `cat-card-title-default.png`, `cat-card-title-hover.png`, `cat-card-title-focus-visible.png`, `cat-card-title-pressed.png`.

### Article

#### art-h1

Article title. "10 Incredible Japanese Woodblock Prints You Need to See" — the article h1.

Page: article. Selector: `h1.title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1152 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | RoslindaleCondensed 56px/60px 500 |
| Letter spacing | 0.56px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `art-h1-default.png`.

#### art-meta

Article meta. The byline/date block under the title.

Page: article. Selector: `.info`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1152 x 14.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 12px/14.75px 400 |
| Letter spacing | -1.8% |
| Colour | #4d5761 |
| Text node | a: Basier 12px/14px 700, #c6002f, ls -0.24px |
| Transition | none |
| How | at rest |

Crops: `art-meta-default.png`.

#### art-cat

Article category link. A category chip on the article; measured, never followed.

Page: article. Selector: `.cat a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 61.7 x 15 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #c6002f offset 1px | = |
| Font | Basier 12px/14px 700 | = | = | = |
| Letter spacing | -0.24px | = | = | = |
| Colour | #c6002f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 61.7x15.0 outline 1px dotted #c6002f offset 1px | = |

Crops: `art-cat-default.png`, `art-cat-hover.png`, `art-cat-focus-visible.png`, `art-cat-pressed.png`.

#### art-para

Article paragraph. A body paragraph in the article flow.

Page: article. Selector: `.project-module p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 648 x 168 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 18px/24px 400 |
| Letter spacing | -1.8% |
| Colour | #4d5761 |
| Text node | em: Basier 18px/24px 400, #4d5761, ls -1.8% |
| Transition | none |
| How | at rest |

Crops: `art-para-default.png`.

#### art-inline-link

Inline link. An in-copy link inside the article; measured, never followed.

Page: article. Selector: `.project-module p a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 163.73 x 23 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #f3003a offset 1px | = |
| Font | Basier 18px/24px 400 | = | = | = |
| Letter spacing | -1.8% | = | = | = |
| Colour | #f3003a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 163.7x23.0 outline 1px dotted #f3003a offset 1px | = |

Crops: `art-inline-link-default.png`, `art-inline-link-hover.png`, `art-inline-link-focus-visible.png`, `art-inline-link-pressed.png`.

#### art-figure

Article figure. A figure block (image + caption) in the article flow; the lightgallery viewer is not opened.

Page: article. Selector: `.project-module-single_image`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 648 x 1013.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 16px/16px 400 |
| Letter spacing | -0.288px |
| Colour | #4d5761 |
| Text node | p: Basier 12px/16.2px 400, #606a73, ls -1.8% |
| Transition | none |
| Painted layers | figcaption 648.0x27.2 border B:1px solid #ebeced |
| How | at rest |

Crops: `art-figure-default.png`.

#### art-caption

Figure caption. A figure caption under an article image.

Page: article. Selector: `figcaption`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 648 x 27.2 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #ebeced; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 12px/16.2px 400 |
| Letter spacing | -0.288px |
| Colour | #4d5761 |
| Text node | p: Basier 12px/16.2px 400, #606a73, ls -1.8% |
| Transition | none |
| Painted layers | figcaption 648.0x27.2 border B:1px solid #ebeced |
| How | at rest |

Crops: `art-caption-default.png`.

#### share-btn

Share button. A share icon button in the article share-links row; measured, never followed.

Page: article. Selector: `.share-links a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 72 x 32 | = | = | = |
| Padding | 7px 10px | = | = | = |
| Border | 1px solid #989da7 | 1px solid #c6002f | = | 1px solid #c6002f |
| Radius | 3px | = | = | = |
| Background | #ffffff | #c6002f | = | #c6002f |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #0000ee offset 1px | = |
| Font | Basier 16px/16px 400 | = | = | = |
| Letter spacing | -0.288px | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Transition | all 0.3s ease-in | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 50 x 16, colour #0000ee | = | = | 50 x 16, colour #ff0000 |
| Painted layers | a.icon-btn 72.0x32.0 bg #ffffff border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 3px | a.icon-btn 72.0x32.0 bg #c6002f border T:1px solid #c6002f / R:1px solid #c6002f / B:1px solid #c6002f / L:1px solid #c6002f r 3px | a.icon-btn 72.0x32.0 bg #ffffff border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 3px outline 1px dotted #0000ee offset 1px | a.icon-btn 72.0x32.0 bg #c6002f border T:1px solid #c6002f / R:1px solid #c6002f / B:1px solid #c6002f / L:1px solid #c6002f r 3px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `share-btn-default.png`, `share-btn-hover.png`, `share-btn-focus-visible.png`, `share-btn-pressed.png`.

#### art-tag

Tag link. An article tag link in the tags-menu; measured, never followed.

Page: article. Selector: `.tags-menu a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66.56 x 20.25 | = | = | = |
| Padding | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 3px | = | = | = |
| Background | #c6002f | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dotted #ffffff offset 1px | = |
| Font | Basier 10px/12.25px 700 | = | = | = |
| Letter spacing | -0.15px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.category 66.6x20.3 bg #c6002f r 3px | = | a.category 66.6x20.3 bg #c6002f r 3px outline 1px dotted #ffffff offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `art-tag-default.png`, `art-tag-hover.png`, `art-tag-focus-visible.png`, `art-tag-pressed.png`.

#### author-box

Author box. The author bio box at the end of the article (avatar, name, bio).

Page: article. Selector: `section.author-footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 205 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 16px/16px 400 |
| Letter spacing | -0.288px |
| Colour | #4d5761 |
| Text node | a: RoslindaleNarrow 20px/24px 700, #000000, ls 0.4px |
| Transition | none |
| Painted layers | div.separator 560.0x1.0 bg #000000; div.separator 560.0x1.0 bg #000000 |
| How | at rest |

Crops: `author-box-default.png`.

#### related-card

Related card. A related-stories card under the article.

Page: article. Selector: `.small-post`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 337 x 107 | = |
| Padding | 12px 0px 16px 0px | = |
| Border | T: none; R: none; B: 1px solid #ebeced; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Basier 16px/16px 400 | = |
| Letter spacing | -0.288px | = |
| Colour | #4d5761 | = |
| Text node | a: Basier 12px/14px 700, #c6002f, ls -0.24px | = |
| Transition | none | = |
| Painted layers | div.small-post 337.0x107.0 border B:1px solid #ebeced | = |
| How | at rest | mouse hover |

Crops: `related-card-default.png`, `related-card-hover.png`.

#### nl-form-article

Article newsletter form. The newsletter form under the article.

Page: article. Selector: `.newsletter-form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 561 x 146 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 16px/16px 400 |
| Letter spacing | -0.288px |
| Colour | #4d5761 |
| Text node | label: Basier 14px/18px 400, #4d5761, ls -0.21px |
| Transition | none |
| Painted layers | input.email-newsletter 561.0x40.0 bg #ffffff border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 3px; label::after 16pxx16px bg #ffffff border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 2px; button.primary.btn 561.0x38.0 border T:1px solid #c6002f / R:1px solid #c6002f / B:1px solid #c6002f / L:1px solid #c6002f r 3px |
| How | at rest |

Crops: `nl-form-article-default.png`.

### About

#### about-h1

About heading. The About page heading.

Page: about. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 770 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | RoslindaleCondensed 56px/60px 500 |
| Letter spacing | 0.56px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `about-h1-default.png`.

#### about-para

About paragraph. A body paragraph in the About page content.

Page: about. Selector: `.page-content p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 689 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 18px/24px 400 |
| Letter spacing | -0.27px |
| Colour | #606a73 |
| Text node | span: Basier 18px/24px 400, #606a73, ls -0.27px |
| Transition | none |
| How | at rest |

Crops: `about-para-default.png`.

### Contact

#### contact-h1

Contact heading. The Contact page heading.

Page: contact. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 750 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | RoslindaleCondensed 56px/60px 500 |
| Letter spacing | 0.56px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `contact-h1-default.png`.

#### cf7-form

Contact form. The Contact Form 7 form (name, email, message, consent, Send).

Page: contact. Selector: `form.wpcf7-form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 669 x 418 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 16px/16px 400 |
| Letter spacing | -0.288px |
| Colour | #4d5761 |
| Text node | span.wpcf7-list-item-label: Basier 14px/18px 400, #606a73, ls -0.21px |
| Transition | none |
| Painted layers | input 0.0x0.0 border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 2px; input 0.0x0.0 border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 2px; input 0.0x0.0 border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 2px; input 0.0x0.0 border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 2px; input 0.0x0.0 border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 2px; input 0.0x0.0 border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 2px |
| How | at rest |

Crops: `cf7-form-default.png`.

#### cf7-name

Text field. The "Your name" required text field; typed into for filled, then cleared — never submitted.

Page: contact. Selector: `input.wpcf7-text`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 319.5 x 40 | = | = |
| Padding | 10px | = | = |
| Border | 1px solid #989da7 | = | = |
| Radius | 2px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Basier 14px/18px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | all 0.3s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| Painted layers | input.wpcf7-form-control.wpcf7-text 319.5x40.0 bg #ffffff border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 2px | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `cf7-name-default.png`, `cf7-name-focused.png`, `cf7-name-filled.png`.

#### cf7-email

Email field. The "Your email" required email field; typed into for filled, then cleared — never submitted.

Page: contact. Selector: `input.wpcf7-email`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 319.5 x 40 | = | = |
| Padding | 10px | = | = |
| Border | 1px solid #989da7 | = | = |
| Radius | 2px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Basier 14px/18px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | all 0.3s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| Painted layers | input.wpcf7-form-control.wpcf7-email 319.5x40.0 bg #ffffff border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 2px | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `cf7-email-default.png`, `cf7-email-focused.png`, `cf7-email-filled.png`.

#### cf7-message

Textarea. The "Your message" textarea; typed into for filled, then cleared — never submitted.

Page: contact. Selector: `textarea.wpcf7-textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 669 x 202 | = | = |
| Padding | 10px | = | = |
| Border | 1px solid #989da7 | = | = |
| Radius | 2px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Basier 14px/18px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | all 0.3s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| Painted layers | textarea.wpcf7-form-control.wpcf7-textarea 669.0x202.0 bg #ffffff border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 2px | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `cf7-message-default.png`, `cf7-message-focused.png`, `cf7-message-filled.png`.

#### cf7-accept

Acceptance checkbox. The wpcf7 acceptance control: the native input is visibility:hidden, the box is painted by the label span ::before; measured, never toggled.

Page: contact. Selector: `.wpcf7-acceptance label`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 669 x 42 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Basier 14px/18px 400 | = |
| Letter spacing | -0.21px | = |
| Colour | #606a73 | = |
| Text node | span.wpcf7-list-item-label: Basier 14px/18px 400, #606a73, ls -0.21px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | span::before.wpcf7-list-item-label 16pxx16px border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 2px | = |
| How | at rest | mouse hover |

Crops: `cf7-accept-default.png`, `cf7-accept-hover.png`.

#### cf7-send

Send button. The wpcf7 "Send" submit; measured, never submitted.

Page: contact. Selector: `input.wpcf7-submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 669 x 46 | = | - | = |
| Padding | 15px 10px 12px 10px | = | - | = |
| Border | 1px solid #989da7 | = | - | = |
| Radius | 2px | = | - | = |
| Background | #000000 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Basier 14px/17px 600 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | all 0.3s ease | = | - | = |
| Cursor | not-allowed | = | - | = |
| Placeholder | #ffffff, opacity 1 | = | - | = |
| Painted layers | input.wpcf7-form-control.wpcf7-submit 669.0x46.0 bg #000000 border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 2px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `cf7-send-default.png`, `cf7-send-hover.png`, `cf7-send-pressed.png`.

### Search

#### search-h1

Search heading. The results heading for ?s=van+gogh.

Page: search. Selector: `search h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 750 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | RoslindaleCondensed 56px/60px 500 |
| Letter spacing | 0.56px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `search-h1-default.png`.

#### search-card

Result card. A search-result story card.

Page: search. Selector: `.single-post`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 760 x 194 | = |
| Padding | 0px 0px 16px 0px | = |
| Border | T: none; R: none; B: 1px solid #ebeced; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Basier 16px/16px 400 | = |
| Letter spacing | -0.288px | = |
| Colour | #4d5761 | = |
| Text node | a.category: Basier 10px/12.25px 700, #ffffff, ls -0.15px | = |
| Transition | none | = |
| Painted layers | div.single-post.single-post__horizontal 760.0x194.0 border B:1px solid #ebeced; a.category 119.3x20.3 bg #c6002f r 3px | = |
| How | at rest | mouse hover |

Crops: `search-card-default.png`, `search-card-hover.png`.

### Mobile (390 wide)

#### m-nav-bar

Mobile nav.

Page: home. Selector: `nav at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 366 x 37 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 16px/16px 400 |
| Letter spacing | -0.288px |
| Colour | #4d5761 |
| Transition | none |
| Icon | 24 x 24, colour #000000 |
| Painted layers | div.ham-border 36.8x37.0 bg #19191c border T:1px solid #c6002f / R:1px solid #c6002f / B:1px solid #c6002f / L:1px solid #c6002f r 3px; span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff |
| Ancestor paint | 1 up div.wrapper bg #19191c; 2 up header bg #19191c shadow #000000 @ 0 0px 5px 20px 0px |
| How | at rest |

Crops: `m-nav-bar-default.png`.

#### m-logo

Mobile logo.

Page: home. Selector: `a.logo at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 111 x 30.17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 16px/16px 400 |
| Letter spacing | -0.288px |
| Colour | #0000ee |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, -55.5, -15.0859) |
| Cursor | pointer |
| Icon | 111 x 28.17, colour #0000ee, fill #000000 |
| Ancestor paint | 1 up div.wrapper bg #19191c; 2 up header bg #19191c shadow #000000 @ 0 0px 5px 20px 0px |
| How | at rest |

Crops: `m-logo-default.png`.

#### m-hamburger

Mobile hamburger. The hamburger at 390px.

Page: home. Selector: `#hamburger`. States: default, pressed.

| Property | default | pressed |
|---|---|---|
| Size (w x h) | 20 x 15 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Basier 16px/16px 400 | = |
| Letter spacing | -0.288px | = |
| Colour | #4d5761 | = |
| Transition | all 0.5s ease-in-out | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = |
| Cursor | pointer | = |
| Painted layers | span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff; span 10.0x2.0 bg #ffffff | = |
| Ancestor paint | 1 up div.ham-border bg #19191c | = |
| How | at rest | CDP forcePseudoState :active:hover |

Crops: `m-hamburger-default.png`, `m-hamburger-pressed.png`.

#### m-post-card

Mobile post card. A story card at 390px.

Page: home. Selector: `.single-post`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 366 x 346.75 |
| Padding | 0px 0px 15px 0px |
| Border | T: none; R: none; B: 1px solid #2e2e32; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basier 16px/16px 400 |
| Letter spacing | -0.288px |
| Colour | #ffffff |
| Text node | a.category: Basier 10px/12.25px 700, #ffffff, ls -0.15px |
| Transition | none |
| Painted layers | div.single-post.single-post__vertical 366.0x346.8 border B:1px solid #2e2e32; a.category 65.1x20.3 bg #c6002f r 3px; a::before.category 41pxx1px bg #2e2e32 |
| How | at rest |

Crops: `m-post-card-default.png`.

#### m-nl-email

Mobile newsletter field. The newsletter input at 390px; typed into for filled, then cleared — never submitted.

Page: home. Selector: `.email-newsletter`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 356 x 40 | = | = |
| Padding | 10px | = | = |
| Border | 1px solid #989da7 | 1px solid #000000 | 1px solid #000000 |
| Radius | 3px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Basier 14px/18px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | all 0.3s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| Painted layers | input.email-newsletter 356.0x40.0 bg #ffffff border T:1px solid #989da7 / R:1px solid #989da7 / B:1px solid #989da7 / L:1px solid #989da7 r 3px | input.email-newsletter 356.0x40.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 3px | input.email-newsletter 356.0x40.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 3px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `m-nl-email-default.png`, `m-nl-email-focused.png`, `m-nl-email-filled.png`.

## Transitions declared in the readable stylesheets

dailyartmagazine.com is a light-only WordPress magazine; the a.pub.network ad slots and the newsletter modal were read, never answered, and the wpcf7/newsletter forms were measured but never submitted. Every value above is the computed value the page paints.

- about: `height 0.5s`, `opacity 0.3s`, `transform 0.2s, top 0.2s, -webkit-transform 0.2s`, `transform 0.2s, left 0.2s, -webkit-transform 0.2s`, `transform 0.2s, right 0.2s, -webkit-transform 0.2s`, `color 0.2s linear`, `opacity 0.2s ease-out`, `transform 250ms cubic-bezier(0, 0, 0.25, 1), opacity 250ms cubic-bezier(0, 0, 0.25, 1)`, `border-color 0.25s`, `opacity 0.3s ease-in`, `transform 0.25s cubic-bezier(0.17, 0.88, 0.32, 1.28), opacity 0.1s`, `opacity 0.12s ease-in`

- article: `height 0.5s`, `color 0.2s linear`, `opacity 0.2s ease-out`, `transform 250ms cubic-bezier(0, 0, 0.25, 1), opacity 250ms cubic-bezier(0, 0, 0.25, 1)`, `border-color 0.25s`, `opacity 0.3s ease-in`, `transform 0.25s cubic-bezier(0.17, 0.88, 0.32, 1.28), opacity 0.1s`, `opacity 0.12s ease-in`, `opacity 0.08s`, `transform 0.5s cubic-bezier(0.12, 0.415, 0.01, 1.19)`, `transform 0.8s cubic-bezier(0, 0, 0.25, 1)`, `transform 0.5s cubic-bezier(0.12, 0.415, 0.01, 1.19), opacity 0.15s`

- category: `height 0.5s`, `opacity 0.3s`, `transform 0.2s, top 0.2s, -webkit-transform 0.2s`, `transform 0.2s, left 0.2s, -webkit-transform 0.2s`, `transform 0.2s, right 0.2s, -webkit-transform 0.2s`, `color 0.2s linear`, `opacity 0.2s ease-out`, `transform 250ms cubic-bezier(0, 0, 0.25, 1), opacity 250ms cubic-bezier(0, 0, 0.25, 1)`, `border-color 0.25s`, `opacity 0.3s ease-in`, `transform 0.25s cubic-bezier(0.17, 0.88, 0.32, 1.28), opacity 0.1s`, `opacity 0.12s ease-in`

- contact: `height 0.5s`, `opacity 0.3s`, `transform 0.2s, top 0.2s, -webkit-transform 0.2s`, `transform 0.2s, left 0.2s, -webkit-transform 0.2s`, `transform 0.2s, right 0.2s, -webkit-transform 0.2s`, `color 0.2s linear`, `opacity 0.2s ease-out`, `transform 250ms cubic-bezier(0, 0, 0.25, 1), opacity 250ms cubic-bezier(0, 0, 0.25, 1)`, `border-color 0.25s`, `opacity 0.3s ease-in`, `transform 0.25s cubic-bezier(0.17, 0.88, 0.32, 1.28), opacity 0.1s`, `opacity 0.12s ease-in`

- home: `height 0.5s`, `opacity 0.3s`, `transform 0.2s, top 0.2s, -webkit-transform 0.2s`, `transform 0.2s, left 0.2s, -webkit-transform 0.2s`, `transform 0.2s, right 0.2s, -webkit-transform 0.2s`, `color 0.2s linear`, `opacity 0.2s ease-out`, `transform 250ms cubic-bezier(0, 0, 0.25, 1), opacity 250ms cubic-bezier(0, 0, 0.25, 1)`, `border-color 0.25s`, `opacity 0.3s ease-in`, `transform 0.25s cubic-bezier(0.17, 0.88, 0.32, 1.28), opacity 0.1s`, `opacity 0.12s ease-in`

- latest: `height 0.5s`, `opacity 0.3s`, `transform 0.2s, top 0.2s, -webkit-transform 0.2s`, `transform 0.2s, left 0.2s, -webkit-transform 0.2s`, `transform 0.2s, right 0.2s, -webkit-transform 0.2s`, `color 0.2s linear`, `opacity 0.2s ease-out`, `transform 250ms cubic-bezier(0, 0, 0.25, 1), opacity 250ms cubic-bezier(0, 0, 0.25, 1)`, `border-color 0.25s`, `opacity 0.3s ease-in`, `transform 0.25s cubic-bezier(0.17, 0.88, 0.32, 1.28), opacity 0.1s`, `opacity 0.12s ease-in`

- search: `height 0.5s`, `opacity 0.3s`, `transform 0.2s, top 0.2s, -webkit-transform 0.2s`, `transform 0.2s, left 0.2s, -webkit-transform 0.2s`, `transform 0.2s, right 0.2s, -webkit-transform 0.2s`, `color 0.2s linear`, `opacity 0.2s ease-out`, `transform 250ms cubic-bezier(0, 0, 0.25, 1), opacity 250ms cubic-bezier(0, 0, 0.25, 1)`, `border-color 0.25s`, `opacity 0.3s ease-in`, `transform 0.25s cubic-bezier(0.17, 0.88, 0.32, 1.28), opacity 0.1s`, `opacity 0.12s ease-in`
