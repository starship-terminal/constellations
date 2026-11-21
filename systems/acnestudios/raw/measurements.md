# Component measurements

Computed styles read from acnestudios.com on  by `tools/capture/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The fixed top bar: left the section triggers (WOMAN MAN BAGS SCARVES GIFTS on desktop, a Menu button on narrow), centre the Acne Studios wordmark, right SEARCH HELP ACCOUNT and the BAG count, in a two-zone black-on-white layout with hairline rules.

Page: home. Selector: `header.skip-link-target`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Text node | button.as-cell.link--main-nav: Helvetica Now Text 12px/20px 400, #000000, ls 0.3px |
| Transition | none |
| Icon | 0 x 0, colour #000000 |
| Painted layers | header.header.skip-link-target 1440.0x60.0 bg #ffffff; nav.header__nav 1440.0x60.0 shadow #f2f2f2 0px 1px 0px 0px inset, #f2f2f2 0px -1px 0px 0px inset; button.as-cell.link--main-nav 70.5x60.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.as-cell.link--main-nav 48.8x60.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.as-cell.link--main-nav 56.2x60.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.as-cell.link--main-nav 80.2x60.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 |
| How | at rest |

Crops: `header-default.png`.

#### nav-item

Nav item. A section trigger (WOMAN MAN BAGS SCARVES GIFTS): all-caps micro type, opens the section mega-menu on press. Measured, the menu was opened once for its panel.

Page: home. Selector: `header button.link--main-nav "WOMAN"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 70.5 x 60 | = | = | = |
| Padding | 4px 9px 33px 9px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #000000 | #6b6b6b | #051574 | #6b6b6b |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.as-cell.link--main-nav 70.5x60.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | = | = | = |
| Ancestor paint | 1 up nav.header__nav shadow #f2f2f2 0px 1px 0px 0px inset, #f2f2f2 0px -1px 0px 0px inset | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`.

#### logo

Wordmark. The centred Acne Studios logotype image (215px), an img that links home.

Page: home. Selector: `header .logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 214.86 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, -107.43, -14) |
| Opacity | 0 |
| Ancestor paint | 1 up nav.header__nav shadow #f2f2f2 0px 1px 0px 0px inset, #f2f2f2 0px -1px 0px 0px inset |
| How | at rest |

Crops: `logo-default.png`.

#### search-button

Search button. The SEARCH trigger opening the right-side search panel.

Page: home. Selector: `.header__search-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 94.55 x 60 | = | = | = |
| Padding | 4px 9px 33px 9px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #000000 | #6b6b6b | #6b6b6b | #6b6b6b |
| Text node | span.show-for-large-up: Helvetica Now Text 12px/20px 400, #000000, ls 0.3px | span.show-for-large-up: Helvetica Now Text 12px/20px 400, #6b6b6b, ls 0.3px | span.show-for-large-up: Helvetica Now Text 12px/20px 400, #6b6b6b, ls 0.3px | span.show-for-large-up: Helvetica Now Text 12px/20px 400, #6b6b6b, ls 0.3px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #000000 | 12 x 12, colour #6b6b6b | 12 x 12, colour #6b6b6b | 12 x 12, colour #6b6b6b |
| Painted layers | button.header__icon-button.header__search-button 94.5x60.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | = | = | = |
| Ancestor paint | 1 up nav.header__nav shadow #f2f2f2 0px 1px 0px 0px inset, #f2f2f2 0px -1px 0px 0px inset | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-button-default.png`, `search-button-hover.png`, `search-button-focus-visible.png`, `search-button-pressed.png`.

#### help-button

Help button. The HELP trigger in the header.

Page: home. Selector: `header HELP button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 72.89 x 60 | = | = | = |
| Padding | 4px 9px 33px 9px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #000000 | #6b6b6b | #6b6b6b | #6b6b6b |
| Text node | span.show-for-large-up: Helvetica Now Text 12px/20px 400, #000000, ls 0.3px | span.show-for-large-up: Helvetica Now Text 12px/20px 400, #6b6b6b, ls 0.3px | span.show-for-large-up: Helvetica Now Text 12px/20px 400, #6b6b6b, ls 0.3px | span.show-for-large-up: Helvetica Now Text 12px/20px 400, #6b6b6b, ls 0.3px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #000000 | 12 x 12, colour #6b6b6b | 12 x 12, colour #6b6b6b | 12 x 12, colour #6b6b6b |
| Ancestor paint | 1 up nav.header__nav shadow #f2f2f2 0px 1px 0px 0px inset, #f2f2f2 0px -1px 0px 0px inset | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `help-button-default.png`, `help-button-hover.png`, `help-button-focus-visible.png`, `help-button-pressed.png`.

#### account-link

Account link. The ACCOUNT entry, an <a> to the sign-in page. Hovered and focused, never followed.

Page: home. Selector: `header a[href*="account"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 101.02 x 60 | = | = | = |
| Padding | 4px 9px 33px 9px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #000000 | #6b6b6b | #6b6b6b | #6b6b6b |
| Text node | span.show-for-large-up: Helvetica Now Text 12px/20px 400, #000000, ls 0.3px | span.show-for-large-up: Helvetica Now Text 12px/20px 400, #6b6b6b, ls 0.3px | span.show-for-large-up: Helvetica Now Text 12px/20px 400, #6b6b6b, ls 0.3px | span.show-for-large-up: Helvetica Now Text 12px/20px 400, #6b6b6b, ls 0.3px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 11, colour #000000 | 10 x 11, colour #6b6b6b | 10 x 11, colour #6b6b6b | 10 x 11, colour #6b6b6b |
| Ancestor paint | 1 up nav.header__nav shadow #f2f2f2 0px 1px 0px 0px inset, #f2f2f2 0px -1px 0px 0px inset | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `account-link-default.png`, `account-link-hover.png`, `account-link-focus-visible.png`, `account-link-pressed.png`.

#### bag-button

Bag button. The BAG item-count button (shows "00" empty); opens the shopping-bag drawer.

Page: home. Selector: `header bag button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 53.97 x 60 | = | = | = |
| Padding | 4px 9px 33px 9px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #6b6b6b | = | = | = |
| Text node | span: Helvetica Now Text 12px/20px 400, #6b6b6b, ls 0.3px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 10, colour #6b6b6b | = | = | = |
| Ancestor paint | 1 up nav.header__nav shadow #f2f2f2 0px 1px 0px 0px inset, #f2f2f2 0px -1px 0px 0px inset | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `bag-button-default.png`, `bag-button-hover.png`, `bag-button-focus-visible.png`, `bag-button-pressed.png`.

### Home

#### hero

Hero. The full-bleed campaign band: black ground, a seasonal photo, the white Acne Studios wordmark set over it, a GIFT GUIDE eyebrow top-left and WOMEN’S/MEN’S GIFT GUIDE bars at the foot.

Page: home. Selector: `first main band`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 810 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Text node | span: Helvetica Now Text 12px/20px 400, #ffffff, ls 0.3px |
| Transition | none |
| Painted layers | div::after.tile.tile-type--content 1440pxx810px shadow #000000 0px 0px 0px 1px inset; div.as-cell.tile__pos--top 1440.0x30.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; div.as-cell.tile__pos--top 1440.0x30.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 |
| How | at rest |

Crops: `hero-default.png`.

#### hero-wordmark

Hero wordmark. The giant white "Acne Studios" image headline set over the FW26 campaign photo.

Page: home. Selector: `hero wordmark image`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1080 x 211.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Monospaced Pro 9px/10.35px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `hero-wordmark-default.png`.

#### gift-link

Gift guide bar. A hero-foot link bar (WOMEN’S GIFT GUIDE / MEN’S GIFT GUIDE).

Page: home. Selector: `gift guide link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1440 x 30 | = | = | = |
| Padding | 4px 9px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span: Helvetica Now Text 12px/20px 400, #ffffff, ls 0.3px | = | = | = |
| Transition | none | = | = | = |
| Painted layers | div.as-cell.tile__pos--top 1440.0x30.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | = | = | = |
| How | at rest | mouse hover | focus failed | CDP forcePseudoState :active:hover |
| Opacity | - | 0 | = | = |

Crops: `gift-link-default.png`, `gift-link-hover.png`, `gift-link-focus-visible.png`, `gift-link-pressed.png`.

### Footer

#### footer

Footer. The page foot: newsletter signup, contact methods (Live chat / Call / Email), four link columns, social icons, the "SHIPPING TO SINGAPORE (ENGLISH)" region selector and a cookie-settings link.

Page: home. Selector: `footer.skip-link-target`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 572 |
| Padding | 0px |
| Border | T: 1px solid #f2f2f2; R: none; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Text node | h2.color--blue: Helvetica Now Text 12px/20px 400, #0018a8, ls 0.3px |
| Transition | none |
| Painted layers | footer.footer.skip-link-target 1440.0x572.0 border T:1px solid #f2f2f2; form.as-cell.cell--span-5 450.0x140.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; input 430.0x60.0 bg #f7f7f7 border T:1px solid #f7f7f7 / R:1px solid #f7f7f7 / B:1px solid #f7f7f7 / L:1px solid #f7f7f7; div.as-cell.cell--span-3 270.0x70.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; div.as-cell.cell--span-3 270.0x70.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; nav.footer__top.cell--span-16---medium-up 1440.0x161.0 border T:1px solid #f2f2f2 |
| How | at rest |

Crops: `footer-default.png`.

#### newsletter-label

Newsletter heading. The NEWSLETTER block opening the footer, with the email field under it.

Page: home. Selector: `footer newsletter block`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 430 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #0018a8 |
| Transition | none |
| How | at rest |

Crops: `newsletter-label-default.png`.

#### newsletter-field

Newsletter email field. The EMAIL text field in the footer: typed and deleted, never submitted.

Page: home. Selector: `footer input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 430 x 60 | = | = |
| Padding | 19px 10px | 30.4px 10px 7.6px 10px | 30.4px 10px 7.6px 10px |
| Border | 1px solid #f7f7f7 | 1px solid #000000 | 1px solid #000000 |
| Radius | 0px | = | = |
| Background | #f7f7f7 | #e8f0fe | #e8f0fe |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Helvetica Now Text 18px/20px 400 | = | = |
| Letter spacing | 0.3px | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #c2c2c2, opacity 0 | #c2c2c2, opacity 1 | #c2c2c2, opacity 1 |
| Painted layers | input 430.0x60.0 bg #f7f7f7 border T:1px solid #f7f7f7 / R:1px solid #f7f7f7 / B:1px solid #f7f7f7 / L:1px solid #f7f7f7 | input 430.0x60.0 bg #e8f0fe border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 | input 430.0x60.0 bg #e8f0fe border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 |
| How | at rest | clicked into the field | typed a placeholder, then deleted; nothing sent |

Crops: `newsletter-field-default.png`, `newsletter-field-focused.png`, `newsletter-field-filled.png`.

#### footer-col-title

Footer column title. A column heading (HELP, CLIENT SERVICES, COMPANY, CONTACT US) in micro caps.

Page: home. Selector: `footer column title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 340 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `footer-col-title-default.png`.

#### footer-link

Footer link. A blue footer link (Contact us, FAQs, Find a store).

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 340 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/24px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #0018a8 | #051574 | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-link

Social link. A two-letter social link (IG FB TW YT PT WB).

Page: home. Selector: `footer social link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 33.45 x 30 | = | = | = |
| Padding | 4px 9px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #0018a8 | #051574 | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.as-cell.link 33.5x30.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `social-link-default.png`, `social-link-hover.png`, `social-link-focus-visible.png`, `social-link-pressed.png`.

#### geo-selector

Region selector. "SHIPPING TO SINGAPORE (ENGLISH)": the geo prompt serving the SG storefront. Hovered and focused only.

Page: home. Selector: `footer shipping selector`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 227.52 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #0018a8 | #051574 | = | = |
| Text node | span.current-country__shipping-to: Helvetica Now Text 12px/20px 400, #0018a8, ls 0.3px | span.current-country__shipping-to: Helvetica Now Text 12px/20px 400, #051574, ls 0.3px | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | focus failed | CDP forcePseudoState :active:hover |

Crops: `geo-selector-default.png`, `geo-selector-hover.png`, `geo-selector-focus-visible.png`, `geo-selector-pressed.png`.

### Category page (PLP)

#### subnav-link

Subnav link. The under-header section links on a category page (New Arrivals, Gifts for Her, Winter Dressing, Seasonal Denim, Scarf Personalisation): underlined micro caps.

Page: woman. Selector: `plp subnav a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 94.59 x 30 | = | = | = |
| Padding | 4px 9px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #5c5c5c | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.as-cell 94.6x30.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `subnav-link-default.png`, `subnav-link-hover.png`, `subnav-link-focus-visible.png`, `subnav-link-pressed.png`.

#### plp-title

Category title. "WOMEN’S NEW ARRIVALS" with the item count under it.

Page: woman. Selector: `plp title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 30 |
| Padding | 4px 9px |
| Border | 1px solid #000000 @ 0 |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Transition | none |
| Painted layers | h1.cell.cell--collapse 1440.0x30.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 |
| How | at rest |

Crops: `plp-title-default.png`.

#### filter-toggle

Filter button. The FILTER button opening the FILTER & SORTING rail: a header-style button in the toolbar.

Page: woman. Selector: `button.filter__toggle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 83.47 x 30 | = | = | = |
| Padding | 4px 9px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #000000 | #6b6b6b | #6b6b6b | #6b6b6b |
| Text node | span: Helvetica Now Text 12px/20px 400, #000000, ls 0.3px | span: Helvetica Now Text 12px/20px 400, #6b6b6b, ls 0.3px | span: Helvetica Now Text 12px/20px 400, #6b6b6b, ls 0.3px | span: Helvetica Now Text 12px/20px 400, #6b6b6b, ls 0.3px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 9, colour #000000 | 12 x 9, colour #6b6b6b | 12 x 9, colour #6b6b6b | 12 x 9, colour #6b6b6b |
| Ancestor paint | 1 up div.search-section__nav.flex bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filter-toggle-default.png`, `filter-toggle-hover.png`, `filter-toggle-focus-visible.png`, `filter-toggle-pressed.png`.

#### product-card

Product tile. A product cell: a 4-span tile with the product photo(s), the name in caps and the monospace price under it. Hover swaps the photo.

Page: woman. Selector: `.tile.product-tile`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 360 x 590 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Helvetica Now Text 12px/20px 400 | = |
| Letter spacing | 0.3px | = |
| Colour | #000000 | = |
| Text node | a: Helvetica Now Text 12px/20px 400, #0018a8, ls 0.3px | = |
| Transition | none | = |
| ::after | 360px x 590px, absolute, bg #000000 @ 0, radius 0px, shadow #000000 0px 0px 0px 1px inset | = |
| Painted layers | div::after.tile.tile--span-4 360pxx590px shadow #000000 0px 0px 0px 1px inset; picture.lazyload-image-wrapper.media-wrapper--ratio-2-3 360.0x540.0 bg #f7f7f7; picture.lazyload-image-wrapper.media-wrapper--ratio-2-3 360.0x540.0 bg #f7f7f7; button.horizontal-slider 0.0x0.0 image linear-gradient(45deg, #000000, #000000); button.horizontal-slider 0.0x0.0 image linear-gradient(45deg, #000000 @ 0.3, #000000 @ 0.3); div.product-tile__inforomation.as-cell 360.0x50.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | = |
| How | at rest | mouse hover |

Crops: `product-card-default.png`, `product-card-hover.png`.

#### product-card-name

Product tile name. The product name under the tile photo, caps micro type.

Page: woman. Selector: `.product-tile__name`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 287.88 x 20 |
| Padding | 0px 10px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Text node | a: Helvetica Now Text 12px/20px 400, #0018a8, ls 0.3px |
| Transition | none |
| How | at rest |

Crops: `product-card-name-default.png`.

#### product-card-price

Product tile price. The monospace price under the name (S$4,500).

Page: woman. Selector: `.product-tile__price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 52.13 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Text node | span: Helvetica Now Text 12px/20px 400, #000000, ls 0.3px |
| Transition | none |
| How | at rest |

Crops: `product-card-price-default.png`.

#### load-more

Load more button. The black "LOAD MORE" button under the grid: a full-caps black pill the width of its cell.

Page: woman. Selector: `.action--primary.action--color-black`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 320 x 60 | = | = | = |
| Padding | 19px 9px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #000000 | #0018a8 | #0018a8 | #0018a8 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset -3px | 1px solid #ffffff offset -3px |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.progress-bar--message: Helvetica Now Text 12px/20px 400, #ffffff, ls 0.3px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.action--primary.action--color-black 320.0x60.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; div.progress-bar--status 318.0x58.0 image linear-gradient(270deg, #051574, #051574) | button.action--primary.action--color-black 320.0x60.0 bg #0018a8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; div.progress-bar--status 318.0x58.0 image linear-gradient(270deg, #051574, #051574) | button.action--primary.action--color-black 320.0x60.0 bg #0018a8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 outline 1px solid #ffffff offset -3px; div.progress-bar--status 318.0x58.0 image linear-gradient(270deg, #051574, #051574) | button.action--primary.action--color-black 320.0x60.0 bg #0018a8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 outline 1px solid #ffffff offset -3px; div.progress-bar--status 318.0x58.0 image linear-gradient(270deg, #051574, #051574) |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `load-more-default.png`, `load-more-hover.png`, `load-more-focus-visible.png`, `load-more-pressed.png`.

### Product page (PDP)

#### breadcrumbs

Breadcrumbs. The breadcrumb line over the PDP (Clothing / Outerwear / product name), sticky at the page top.

Page: pdp. Selector: `nav.breadcrumbs`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 31 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #f2f2f2; L: none |
| Radius | 0px |
| Background | #ffffff |
| Background image | linear-gradient(#f2f2f2 1px, #000000 @ 0 0px) |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Text node | a.as-cell: Helvetica Now Text 12px/20px 400, #000000, ls 0.3px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Painted layers | nav.breadcrumbs.breadcrumbs--sticky 1440.0x31.0 bg #ffffff image linear-gradient(#f2f2f2 1px, #000000 @ 0 0px) border B:1px solid #f2f2f2; button.tile-grid__control.tile-grid__control--prev 30.0x30.0 bg #ffffff; button::before.tile-grid__control.tile-grid__control--prev 20pxx30px image linear-gradient(270deg, #ffffff @ 0 0px, #ffffff 75%); a.as-cell 85.8x30.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; a.as-cell 82.6x30.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; a.as-cell 187.0x30.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 |
| How | at rest |

Crops: `breadcrumbs-default.png`.

#### breadcrumb-link

Breadcrumb link. A crumb link (Clothing, Outerwear); the last crumb is the product name.

Page: pdp. Selector: `nav.breadcrumbs a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.8 x 30 | = | = | = |
| Padding | 4px 9px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #000000 | #5c5c5c | = | #5c5c5c |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | auto x auto, static, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | a.as-cell 85.8x30.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `breadcrumb-link-default.png`, `breadcrumb-link-hover.png`, `breadcrumb-link-focus-visible.png`, `breadcrumb-link-pressed.png`.

#### pdp-title

Product title. The product name in caps, right column head.

Page: pdp. Selector: `pdp h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 345 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Transition | none |
| Ancestor paint | 1 up div.as-cell.grid bg #ffffff |
| How | at rest |

Crops: `pdp-title-default.png`.

#### pdp-price

Product price. The monospace price (S$4,500) beside the title.

Page: pdp. Selector: `.pdp__price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 115 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Monospaced Pro 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Text node | span.value: Helvetica Monospaced Pro 12px/20px 400, #000000, ls 0.3px |
| Transition | none |
| Ancestor paint | 1 up div.as-cell.grid bg #ffffff |
| How | at rest |

Crops: `pdp-price-default.png`.

#### pdp-color

Colour name. The colourway under the title (Dark brown).

Page: pdp. Selector: `pdp colour`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 68 x 17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #6b6b6b |
| Transition | none |
| How | at rest |

Crops: `pdp-color-default.png`.

#### fit-predictor

Fit Predictor button. The "Fit Predictor - Calculate your size" link-button beside the size grid.

Page: pdp. Selector: `button.fp-element`. States: .

Not found on the page at capture time.

#### size-guide-link

Size guide link. The Size guide trigger opening the size drawer.

Page: pdp. Selector: `size guide button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106.19 x 49 | = | = | = |
| Padding | 19px 9px 4px 9px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/24px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #0018a8 | #051574 | #051574 | #051574 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 19 x 10, colour #0018a8 | 19 x 10, colour #051574 | 19 x 10, colour #051574 | 19 x 10, colour #051574 |
| Painted layers | button.cell.cell--large 106.2x49.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `size-guide-link-default.png`, `size-guide-link-hover.png`, `size-guide-link-focus-visible.png`, `size-guide-link-pressed.png`.

#### size-cell

Size cell. A size button in the variations grid (32–42): a bordered cell, caps numeral; the picked size gains a heavy black edge.

Page: pdp. Selector: `button.variations__grid-item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 77.34 x 45 | = | = | = |
| Padding | 4px 9px 19px 9px | = | = | = |
| Border | 1px solid #c2c2c2 | 1px solid #000000 | 1px solid #000000 | 1px solid #000000 |
| Radius | 0px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #000000 offset -3px | = |
| Font | Helvetica Monospaced Pro 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #000000 | #051574 | = | #051574 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.variations__grid-item 77.3x45.0 bg #ffffff border T:1px solid #c2c2c2 / R:1px solid #c2c2c2 / B:1px solid #c2c2c2 / L:1px solid #c2c2c2 | button.variations__grid-item 77.3x45.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 | button.variations__grid-item 77.3x45.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 outline 1px solid #000000 offset -3px | button.variations__grid-item 77.3x45.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `size-cell-default.png`, `size-cell-hover.png`, `size-cell-focus-visible.png`, `size-cell-pressed.png`.

#### size-cell-selected

Size cell, picked. The selected size cell, pressed through the page’s own toggle.

Page: pdp. Selector: `size cell selected`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 77.34 x 45 |
| Padding | 4px 9px 19px 9px |
| Border | 1px solid #0018a8 |
| Radius | 0px |
| Background | #e8f0fe |
| Box shadow | #ffffff 0px 0px 0px 1px inset |
| Outline | none |
| Font | Helvetica Monospaced Pro 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #0018a8 |
| Transition | none |
| Cursor | pointer |
| Painted layers | button.variations__grid-item 77.3x45.0 bg #e8f0fe border T:1px solid #0018a8 / R:1px solid #0018a8 / B:1px solid #0018a8 / L:1px solid #0018a8 shadow #ffffff 0px 0px 0px 1px inset |
| How | at rest |

Crops: `size-cell-selected-default.png`.

#### add-to-bag

Add to bag button. The electric-blue ADD TO BAG bar; hovered it retitles to "PLEASE SELECT SIZE" until a size is picked. Measured and state-forced, never pressed: pressing it adds the item.

Page: pdp. Selector: `.action--primary.action--color-blue`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 60 | = | = | = |
| Padding | 19px 9px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #0018a8 | #051574 | #051574 | #051574 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset -3px | 1px solid #ffffff offset -3px |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.action--primary.action--color-blue 400.0x60.0 bg #0018a8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | button.action--primary.action--color-blue 400.0x60.0 bg #051574 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | button.action--primary.action--color-blue 400.0x60.0 bg #051574 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 outline 1px solid #ffffff offset -3px | button.action--primary.action--color-blue 400.0x60.0 bg #051574 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 outline 1px solid #ffffff offset -3px |
| Ancestor paint | 1 up div.as-cell.flexgrid bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `add-to-bag-default.png`, `add-to-bag-hover.png`, `add-to-bag-focus-visible.png`, `add-to-bag-pressed.png`.

#### wishlist-button

Wishlist button. The white heart button beside ADD TO BAG, blue heart outline. Measured, never pressed.

Page: pdp. Selector: `.action--primary.action--color-white`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 60 x 60 | = | = | = |
| Padding | 19px 9px | = | = | = |
| Border | 1px solid #0018a8 | 1px solid #051574 | 1px solid #051574 | 1px solid #051574 |
| Radius | 0px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #051574 offset -3px | 1px solid #051574 offset -3px |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #000000 | #051574 | #051574 | #051574 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 11, colour #ffffff | = | = | = |
| Painted layers | button.action--primary.color--blue 60.0x60.0 bg #ffffff border T:1px solid #0018a8 / R:1px solid #0018a8 / B:1px solid #0018a8 / L:1px solid #0018a8; span 0.0x0.0 image linear-gradient(90deg, #f2f2f2 0px, #c2c2c2 15%, #c2c2c2 22%, #f2f2f2 30%) | button.action--primary.color--blue 60.0x60.0 bg #ffffff border T:1px solid #051574 / R:1px solid #051574 / B:1px solid #051574 / L:1px solid #051574; span 0.0x0.0 image linear-gradient(90deg, #f2f2f2 0px, #c2c2c2 15%, #c2c2c2 22%, #f2f2f2 30%) | button.action--primary.color--blue 60.0x60.0 bg #ffffff border T:1px solid #051574 / R:1px solid #051574 / B:1px solid #051574 / L:1px solid #051574 outline 1px solid #051574 offset -3px; span 0.0x0.0 image linear-gradient(90deg, #f2f2f2 0px, #c2c2c2 15%, #c2c2c2 22%, #f2f2f2 30%) | button.action--primary.color--blue 60.0x60.0 bg #ffffff border T:1px solid #051574 / R:1px solid #051574 / B:1px solid #051574 / L:1px solid #051574 outline 1px solid #051574 offset -3px; span 0.0x0.0 image linear-gradient(90deg, #f2f2f2 0px, #c2c2c2 15%, #c2c2c2 22%, #f2f2f2 30%) |
| Ancestor paint | 1 up div.as-cell.flexgrid bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `wishlist-button-default.png`, `wishlist-button-hover.png`, `wishlist-button-focus-visible.png`, `wishlist-button-pressed.png`.

#### info-row

Info row. An expandable service row (FREE DELIVERY & EASY RETURNS, COMPLIMENTARY GIFTWRAPPING, PICK UP IN STORE): caps label with a hairline rule and a chevron.

Page: pdp. Selector: `pdp info row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 460 x 50 | = |
| Padding | 4px 9px | = |
| Border | 1px solid #f2f2f2 | 1px solid #000000 |
| Radius | 0px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Helvetica Now Text 12px/20px 400 | = |
| Letter spacing | 0.3px | = |
| Colour | #000000 | = |
| Text node | span: Helvetica Now Text 12px/20px 400, #0018a8, ls 0.3px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | button.action--tertiary.action--color-white 460.0x50.0 bg #ffffff border T:1px solid #f2f2f2 / R:1px solid #f2f2f2 / B:1px solid #f2f2f2 / L:1px solid #f2f2f2 | button.action--tertiary.action--color-white 460.0x50.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 |
| How | at rest | mouse hover |

Crops: `info-row-default.png`, `info-row-hover.png`.

#### description

Description block. The product story and bullet spec list under the info rows.

Page: pdp. Selector: `.experience-description`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 250 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Text node | span: Helvetica Now Text 12px/20px 400, #000000, ls 0.3px |
| Transition | none |
| How | at rest |

Crops: `description-default.png`.

#### show-more

Show more link. The "+ SHOW MORE" spec expander.

Page: pdp. Selector: `show more`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 460 x 30 | = | = | = |
| Padding | 0px 0px 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/30px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #0018a8 | #051574 | #051574 | #051574 |
| Text node | span.on--expanded-false: Helvetica Now Text 12px/30px 400, #0018a8, ls 0.3px | span.on--expanded-false: Helvetica Now Text 12px/30px 400, #051574, ls 0.3px | span.on--expanded-false: Helvetica Now Text 12px/30px 400, #051574, ls 0.3px | span.on--expanded-false: Helvetica Now Text 12px/30px 400, #051574, ls 0.3px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 460px x 60px, absolute, bg #000000 @ 0 linear-gradient(#ffffff @ 0 0px, #ffffff 50%), radius 0px | = | = | = |
| Painted layers | button::after 460pxx60px image linear-gradient(#ffffff @ 0 0px, #ffffff 50%) | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `show-more-default.png`, `show-more-hover.png`, `show-more-focus-visible.png`, `show-more-pressed.png`.

### Panels and overlays

#### search-panel

Search panel. The right-side SEARCH drawer: a SEARCH HERE field, SUGGESTIONS links in blue caps and SUGGESTED PRODUCTS thumbnails.

Page: search. Selector: `nav.drawer search panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 555 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Text node | div.as-cell: Helvetica Now Text 12px/20px 400, #000000, ls 0.3px |
| Transition | none |
| Icon | 12 x 12, colour #000000 |
| Painted layers | nav.search-state-container.state-container 360.0x555.0 bg #ffffff; div.drawer.flex 360.0x45.0 bg #ffffff; div.as-cell 72.5x45.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.bg--white.drawer 77.5x45.0 bg #ffffff; input.search-field.field-size--small 360.0x30.0 bg #f7f7f7 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000; div.grid.grid--dense 0.0x0.0 bg #f2f2f2 |
| How | at rest |

Crops: `search-panel-default.png`.

#### search-field

Search field. The SEARCH HERE text field; typed and deleted, never submitted.

Page: search. Selector: `input[type=search]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 360 x 30 | = | = |
| Padding | 4px 31px | = | = |
| Border | 1px solid #000000 | = | = |
| Radius | 0px | = | = |
| Background | #f7f7f7 | #e8f0fe | #e8f0fe |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Helvetica Now Text 12px/20px 400 | = | = |
| Letter spacing | 0.3px | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #c2c2c2, opacity 0 | #c2c2c2, opacity 1 | #c2c2c2, opacity 1 |
| Painted layers | input.search-field.field-size--small 360.0x30.0 bg #f7f7f7 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 | input.search-field.field-size--small 360.0x30.0 bg #e8f0fe border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 | input.search-field.field-size--small 360.0x30.0 bg #e8f0fe border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 |
| How | at rest | clicked into the field | typed a placeholder, then deleted; nothing sent |

Crops: `search-field-default.png`, `search-field-focused.png`, `search-field-filled.png`.

#### search-suggestion

Search suggestion. A suggestion link in the panel (Outerwear, Knitwear, Bags, Scarves, Jeans), blue caps.

Page: search. Selector: `suggestion link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 30 | = | = | = |
| Padding | 4px 9px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #0018a8 | #051574 | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.suggestions__item.as-cell 360.0x30.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-suggestion-default.png`, `search-suggestion-hover.png`, `search-suggestion-focus-visible.png`, `search-suggestion-pressed.png`.

#### menu-panel

Section menu. The WOMAN mega-menu: columns of category links under the header.

Page: menu. Selector: `mega menu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 391 |
| Padding | 0px |
| Border | T: 1px solid #000000; R: none; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Text node | button.button.action--color-white: Helvetica Now Text 12px/20px 400, #051574, ls 0.3px |
| Transition | none |
| Painted layers | nav.category-state-container.state-container 1440.0x391.0 border T:1px solid #000000; div.state-container.cell--span-all 0.0x0.0 bg #ffffff border B:1px solid #000000; h2.as-cell.text--uppercase 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.button.action--color-white 504.0x57.0 bg #ffffff; ul.sub-menu__grid 1440.0x390.0 image repeating-linear-gradient(#f7f7f7, #f7f7f7 30px, #ffffff 0px, #ffffff 60px); h3.as-cell 360.0x30.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 |
| How | at rest |

Crops: `menu-panel-default.png`.

#### menu-link

Menu link. A category link inside the mega-menu.

Page: menu. Selector: `menu a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 30 | = | = | = |
| Padding | 4px 9px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #0018a8 | #051574 | = | = |
| Text node | div.text-mask: Helvetica Now Text 12px/20px 400, #0018a8, ls 0.3px | div.text-mask: Helvetica Now Text 12px/20px 400, #051574, ls 0.3px | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.link.as-cell 360.0x30.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `menu-link-default.png`, `menu-link-hover.png`, `menu-link-focus-visible.png`, `menu-link-pressed.png`.

#### filter-rail

Filter rail. The FILTER & SORTING drawer on the right: SORT BY radios (Newest, Price High/Low, Popularity) and TYPE OF PRODUCT radios, a bordered row for the picked option, the black SHOW N ITEMS apply button at the foot.

Page: filter. Selector: `filter rail`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 901 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Text node | h2.as-cell: Helvetica Now Text 12px/20px 400, #000000, ls 0.3px |
| Transition | none |
| Painted layers | section.filter.drawer 360.0x901.0 bg #ffffff; div.drawer.flex 360.0x45.0 bg #ffffff border B:1px solid #000000; h2.as-cell 137.9x44.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; div::before.drawer__scroll-area.scroll-area 340pxx45px image linear-gradient(0deg, #ffffff @ 0 0px, #ffffff); div::after.drawer__scroll-area.scroll-area 340pxx45px image linear-gradient(#ffffff @ 0 0px, #ffffff); h3.filter-group.as-cell--small 340.0x30.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 |
| How | at rest |

Crops: `filter-rail-default.png`.

#### sort-option

Sort option. A radio row in the filter rail; the picked sort gains a hairline box.

Page: filter. Selector: `sort option`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 320 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up button.filter-button.as-radio bg #ffffff | = | = | = |
| How | at rest | mouse hover | focus failed | CDP forcePseudoState :active:hover |

Crops: `sort-option-default.png`, `sort-option-hover.png`, `sort-option-focus-visible.png`, `sort-option-pressed.png`.

#### show-items

Show items button. The black "SHOW N ITEMS" apply button at the rail’s foot. Measured, never pressed.

Page: filter. Selector: `show items button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 165 x 44 | = | = | = |
| Padding | 4px 9px 18px 9px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #000000 | #0018a8 | #0018a8 | #0018a8 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.button.filter-action-button 165.0x44.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 | button.button.filter-action-button 165.0x44.0 bg #0018a8 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 | button.button.filter-action-button 165.0x44.0 bg #0018a8 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 | button.button.filter-action-button 165.0x44.0 bg #0018a8 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `show-items-default.png`, `show-items-hover.png`, `show-items-focus-visible.png`, `show-items-pressed.png`.

#### filter-close

Rail close button. The X CLOSE at the rail’s head.

Page: filter. Selector: `rail close`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 77.48 x 42 | = | = | = |
| Padding | 4px 9px 18px 9px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #051574 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.drawer.flex bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filter-close-default.png`, `filter-close-hover.png`, `filter-close-focus-visible.png`, `filter-close-pressed.png`.

### Sign in

#### login-title

Sign in title. "Sign in or register" — the gate for the account area.

Page: login. Selector: `login h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 510 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 18px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `login-title-default.png`.

#### login-benefit

Benefit row. A member-benefit line (Priority access to new collections…) with an en-dash bullet.

Page: login. Selector: `benefit row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 490 x 20 |
| Padding | 0px 0px 0px 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Transition | none |
| ::before | 13.7969px x 20px, absolute, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `login-benefit-default.png`.

#### login-email

Email field. The grey EMAIL field: typed and deleted, never submitted.

Page: login. Selector: `login email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 520 x 60 | = | = |
| Padding | 19px 10px | 30.4px 10px 7.6px 10px | 30.4px 10px 7.6px 10px |
| Border | 1px solid #f7f7f7 | 1px solid #000000 | 1px solid #000000 |
| Radius | 0px | = | = |
| Background | #f7f7f7 | #e8f0fe | #e8f0fe |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Helvetica Now Text 18px/20px 400 | = | = |
| Letter spacing | 0.3px | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #c2c2c2, opacity 0 | #c2c2c2, opacity 1 | #c2c2c2, opacity 1 |
| Painted layers | input 520.0x60.0 bg #f7f7f7 border T:1px solid #f7f7f7 / R:1px solid #f7f7f7 / B:1px solid #f7f7f7 / L:1px solid #f7f7f7 | input 520.0x60.0 bg #e8f0fe border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 | input.error 520.0x60.0 bg #e8f0fe border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 |
| How | at rest | clicked into the field | typed a placeholder, then deleted; nothing sent |

Crops: `login-email-default.png`, `login-email-focused.png`, `login-email-filled.png`.

#### login-continue

Continue button. The black CONTINUE bar. Measured, never pressed.

Page: login. Selector: `login continue`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 520 x 60 | = | = | = |
| Padding | 19px 9px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #000000 | #0018a8 | #0018a8 | #0018a8 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset -3px | 1px solid #ffffff offset -3px |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.progress-bar--message: Helvetica Now Text 12px/20px 400, #ffffff, ls 0.3px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.action--primary.action--color-black 520.0x60.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; div.progress-bar--status 518.0x58.0 image linear-gradient(270deg, #051574, #051574) | button.action--primary.action--color-black 520.0x60.0 bg #0018a8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; div.progress-bar--status 518.0x58.0 image linear-gradient(270deg, #051574, #051574) | button.action--primary.action--color-black 520.0x60.0 bg #0018a8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 outline 1px solid #ffffff offset -3px; div.progress-bar--status 518.0x58.0 image linear-gradient(270deg, #051574, #051574) | button.action--primary.action--color-black 520.0x60.0 bg #0018a8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 outline 1px solid #ffffff offset -3px; div.progress-bar--status 518.0x58.0 image linear-gradient(270deg, #051574, #051574) |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-continue-default.png`, `login-continue-hover.png`, `login-continue-focus-visible.png`, `login-continue-pressed.png`.

#### login-google

Google button. The white-bordered GOOGLE oauth row. Measured, never pressed.

Page: login. Selector: `login google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 520 x 60 | = | = | = |
| Padding | 19px 9px | = | = | = |
| Border | 1px solid #000000 | 1px solid #0018a8 | 1px solid #0018a8 | 1px solid #0018a8 |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #0018a8 offset -3px | 1px solid #0018a8 offset -3px |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #000000 | #0018a8 | #0018a8 | #0018a8 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.action--primary 520.0x60.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 | button.action--primary 520.0x60.0 border T:1px solid #0018a8 / R:1px solid #0018a8 / B:1px solid #0018a8 / L:1px solid #0018a8 | button.action--primary 520.0x60.0 border T:1px solid #0018a8 / R:1px solid #0018a8 / B:1px solid #0018a8 / L:1px solid #0018a8 outline 1px solid #0018a8 offset -3px | button.action--primary 520.0x60.0 border T:1px solid #0018a8 / R:1px solid #0018a8 / B:1px solid #0018a8 / L:1px solid #0018a8 outline 1px solid #0018a8 offset -3px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-google-default.png`, `login-google-hover.png`, `login-google-focus-visible.png`, `login-google-pressed.png`.

#### change-location

Change location link. The change-location line under the title. The place name is not recorded.

Page: login. Selector: `change location`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 97.16 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #0018a8 | #051574 | #051574 | #051574 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `change-location-default.png`, `change-location-hover.png`, `change-location-focus-visible.png`, `change-location-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The bar at 390: a Menu button, the wordmark and the bag count only.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 45 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Transition | none |
| Icon | 10 x 7, colour #000000 |
| Painted layers | header.header.skip-link-target 390.0x45.0 bg #ffffff; nav.header__nav 390.0x45.0 shadow #f2f2f2 0px 1px 0px 0px inset, #f2f2f2 0px -1px 0px 0px inset; button.as-cell.link--main-nav 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.as-cell.link--main-nav 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.as-cell.link--main-nav 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.as-cell.link--main-nav 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button. The Menu trigger; opens the drawer.

Page: home. Selector: `m menu button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 45 x 45 | = | = | = |
| Padding | 4px 9px 18px 9px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Now Text 12px/20px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #000000 | #6b6b6b | #6b6b6b | #6b6b6b |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 7, colour #000000 | 10 x 7, colour #6b6b6b | 10 x 7, colour #6b6b6b | 10 x 7, colour #6b6b6b |
| Ancestor paint | 1 up nav.header__nav shadow #f2f2f2 0px 1px 0px 0px inset, #f2f2f2 0px -1px 0px 0px inset | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-drawer

Mobile menu drawer. The navigation drawer the Menu button opens.

Page: home. Selector: `mobile drawer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Text node | a.as-cell.color--black: Helvetica Now Text 12px/20px 400, #000000, ls 0.3px |
| Transition | padding-bottom 0.15s ease |
| Icon | 12 x 12, colour #000000 |
| Painted layers | nav.navigation-state-container.state-container--overflow-auto---small-down 390.0x844.0 bg #ffffff; div.state-container.cell--span-all 390.0x46.0 bg #ffffff border B:1px solid #000000; a.as-cell.color--black 144.6x45.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.as-cell.nav__search-button 390.0x45.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.as-cell.link--main-nav 390.0x45.0 image linear-gradient(#f2f2f2 1px, #000000 @ 0 0px) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.as-cell.link--main-nav 390.0x45.0 image linear-gradient(#f2f2f2 1px, #000000 @ 0 0px) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 |
| How | at rest |

Crops: `m-menu-drawer-default.png`.

#### m-hero

Mobile main. The mobile page canvas under the header.

Page: home. Selector: `main`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 4251 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Now Text 12px/20px 400 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Text node | span: Helvetica Now Text 12px/20px 400, #ffffff, ls 0.3px |
| Transition | none |
| Painted layers | div::after.tile.tile-type--content 390pxx585px shadow #000000 0px 0px 0px 1px inset; div.as-cell.tile__pos--top 390.0x45.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; div.as-cell.tile__pos--top 390.0x45.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; div::after.tile.tile-type--content 390pxx585px shadow #000000 0px 0px 0px 1px inset; div.as-cell.tile__pos--top 390.0x45.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; div.as-cell.tile__pos--top 390.0x45.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

Gauth's own CSS is served cross-origin, so this list holds only what the CSSOM could read on each page (antd's CSS-in-JS and inline styles); the per-state Transition rows above are computed values and cover Gauth's own rules.

- home: `opacity 0.1s linear`, `opacity 0.5s ease-in-out`, `padding-bottom 0.15s`, `margin-bottom 0.15s`, `max-height 0.2s cubic-bezier(0, 0, 0.2, 1)`, `none`

- woman: `opacity 0.1s linear`, `opacity 0.5s ease-in-out`, `padding-bottom 0.15s`, `margin-bottom 0.15s`, `max-height 0.2s cubic-bezier(0, 0, 0.2, 1)`, `none`
