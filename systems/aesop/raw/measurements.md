# Component measurements

Computed styles read from aesop.com on 2026-11-10 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The two-tier top bar every page shares: a thin utility row (Stores, Customer service left; Email sign up, Account, My cart right), the centred Aēsop wordmark, the Search disclosure and the main navigation row. Transparent over the hero, solid elsewhere.

Page: home. Selector: `header.l-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fffef2 @ 0.686 |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 12px/18px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | span.c-storeslink__text: SuisseIntl 12px/14.4px 700, #73736f |
| Transition | background 0.5s ease-out |
| Painted layers | header.l-header 1440.0x30.0 bg #fffef2 @ 0.686; div.h-ph-item 1440.0x30.0 bg #ffffff; div::before.h-ph-item 7200pxx30px image linear-gradient(90deg, #ffffff @ 0 46%, #ffffff @ 0.35 50%, #ffffff @ 0 54%); div.h-ph-col--12.h-ph-row-30 1440.0x30.0 bg #ced4da; div.c-content-panel.m-closed 0.0x0.0 bg #333333; button::before.c-content-panel 16pxx16px bg #fffef2 |
| How | at rest |

Crops: `header-default.png`.

#### logo

Wordmark. The centred "Aēsop." wordmark linking home.

Page: home. Selector: `a.c-logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 140 x 44.09 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 12px/18px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### topnav-link

Utility link. A utility-nav entry on the left of the top row (Stores); Customer service sits beside it.

Page: home. Selector: `a.c-storeslink`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 58.17 x 19 | = | = | = |
| Padding | 0px 0px 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl 12px/14.4px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | = | = | = |
| Text node | span.c-storeslink__text: SuisseIntl 12px/14.4px 700, #333333 | = | = | = |
| Transition | color 0.5s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 0px x 19px, static, bg #333333, radius 0px | = | = | = |
| ::after | 0px x 20px, absolute, bg #333333 @ 0.2, radius 0px | = | = | = |
| Painted layers | a::before.c-storeslink 0pxx19px bg #333333; a::after.c-storeslink 0pxx20px bg #333333 @ 0.2 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `topnav-link-default.png`, `topnav-link-hover.png`, `topnav-link-focus-visible.png`, `topnav-link-pressed.png`.

#### topnav-button

Utility button. The Customer service utility button.

Page: home. Selector: `button.l-header__top-nav-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 109.53 x 14.39 | = | = | = |
| Padding | 0px 0px 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl 12px/14.4px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | = | = | = |
| Transition | color 0.5s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 0px x 20px, absolute, bg #333333 @ 0.2, radius 0px | = | = | = |
| Painted layers | button::after.l-header__top-nav-link 0pxx20px bg #333333 @ 0.2 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `topnav-button-default.png`, `topnav-button-hover.png`, `topnav-button-focus-visible.png`, `topnav-button-pressed.png`.

#### signup-link

Email sign up button. The Email sign up trigger; opens the newsletter modal (a local toggle).

Page: home. Selector: `button.c-signup-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 73.47 x 14.39 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl 12px/14.4px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | = | = | = |
| Text node | span.c-signup-link__text: SuisseIntl 12px/14.4px 700, #333333 | = | = | = |
| Transition | color 0.5s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 0px x 20px, absolute, bg #333333 @ 0.2, radius 0px | = | = | = |
| Painted layers | button::after.c-signup-link 0pxx20px bg #333333 @ 0.2; span::before.c-icon__svg 18pxx18px bg #333333 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-link-default.png`, `signup-link-hover.png`, `signup-link-focus-visible.png`, `signup-link-pressed.png`.

#### account-link

Account entry. The Account slot in the utility row; its link lazy-loads once the header hydrates.

Page: home. Selector: `.l-header__top-nav-item.m-account`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 58.2 x 14.39 | = |
| Padding | 0px 0px 0px 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | SuisseIntl 11px/17.6px 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | = |
| Text node | span.c-user__text.m-login: SuisseIntl 12px/14.4px 700, #333333 | = |
| Transition | none | = |
| ::after | 0px x 20px, absolute, bg #333333 @ 0.2, radius 0px | = |
| Painted layers | li::after.l-header__top-nav-item.m-account 0pxx20px bg #333333 @ 0.2 | = |
| How | at rest | mouse hover |

Crops: `account-link-default.png`, `account-link-hover.png`.

#### cart-button

My cart button. The My cart trigger with its item count ("0 product in cart" empty); opens the right-hand cart drawer.

Page: home. Selector: `button.c-minicart-icon__link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56.61 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl 12px/14.4px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | = | = | = |
| Text node | span.c-minicart-icon: SuisseIntl 12px/14.4px 700, #333333 | = | = | = |
| Transition | color 0.5s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | i.c-minicart-icon__svg 0.0x20.0 bg #333333 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cart-button-default.png`, `cart-button-hover.png`, `cart-button-focus-visible.png`, `cart-button-pressed.png`.

#### nav-link

Nav link. A main-nav entry (Gifts, Shop all, New & Notable, Skin Care, Hand & Body, Fragrance, Home, Hair, Travel, Library, Experience).

Page: home. Selector: `a.c-navigation__link.m-level-1`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 64.89 x 50.8 | = | = | = |
| Padding | 17px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl-Medium 14px/16.8px 400 | SuisseIntl-Medium 14px/16.8px 700 | = | SuisseIntl-Medium 14px/16.8px 700 |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | = | = | = |
| Text node | span.c-navigation__link-name: SuisseIntl-Medium 14px/16.8px 400, #333333 | span.c-navigation__link-name: SuisseIntl-Medium 14px/16.8px 700, #333333 | = | span.c-navigation__link-name: SuisseIntl-Medium 14px/16.8px 700, #333333 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 30.8906px x 0px, static, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| ::before | - | 64.8906px x 3px, absolute, bg #333333, radius 0px | = | 64.8906px x 3px, absolute, bg #333333, radius 0px |
| Painted layers | - | a::before.c-navigation__link.m-level-1 64.8906pxx3px bg #333333 | = | a::before.c-navigation__link.m-level-1 64.8906pxx3px bg #333333 |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### search-button

Search button. The "Search…" trigger opening the search disclosure under the nav.

Page: home. Selector: `button.l-header__search-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140 x 50.8 | = | = | = |
| Padding | 16px | = | = | = |
| Border | T: none; R: none; B: none; L: 2px solid #ebeade | = | = | = |
| Radius | 0px | = | = | = |
| Background | #fffef2 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl 14px/16.8px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | = | = | = |
| Text node | span.l-header__search-button-label: SuisseIntl 14px/16.8px 700, #333333 | = | = | = |
| Transition | background, color 0.5s, 0.5s ease-out, ease-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 16px x 16px, static, bg #333333, radius 0px | = | = | = |
| Painted layers | button.l-header__search-button 140.0x50.8 bg #fffef2 border L:2px solid #ebeade; button::before.l-header__search-button 16pxx16px bg #333333 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-button-default.png`, `search-button-hover.png`, `search-button-focus-visible.png`, `search-button-pressed.png`.

### Home

#### hero

Hero. The full-bleed campaign band under the transparent header: photography or film, an overlaid eyebrow line, a headline and a bordered CTA card.

Page: home. Selector: `first main band`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 720 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 12px/18px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | span.c-content-hero.h-color-light: SuisseIntl-Medium 14px/21px 400, #fffef2 |
| Transition | none |
| Painted layers | div.flowplayer.use-play-1 1440.0x720.0 bg #333333; flowplayer-endscreen-interstitial.fp-endscreen 0.0x0.0 bg #030303; div.poster 0.0x0.0 image url(…); span.fp-icon.fp-play 0.0x0.0 image url(data:…)' /%3E%3C/svg%3E"); flowplayer-endscreen-grid.interstitial-grid 0.0x0.0 bg #030303; div.fp-previous 0.0x0.0 image url(data:…) |
| How | at rest |

Crops: `hero-default.png`.

#### hero-cta

Hero CTA. A bordered call-to-action card inside the hero (Discover).

Page: home. Selector: `hero cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 390 x 48 | = | = | = |
| Padding | 13px 24px 12px 24px | = | = | = |
| Border | 1px solid #fffef2 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #fffef2 | = | #fffef2 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl-Medium 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fffef2 | #333333 | = | #333333 |
| Transition | background-color, color 0.25s, 0.25s ease-out, ease-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px | = | = | = |
| ::after | 16px x 16px, static, bg #fffef2, radius 0px | = | = | = |
| Painted layers | a.c-button.m-secondary 390.0x48.0 border T:1px solid #fffef2 / R:1px solid #fffef2 / B:1px solid #fffef2 / L:1px solid #fffef2; a::after.c-button.m-secondary 16pxx16px bg #fffef2 | a.c-button.m-secondary 390.0x48.0 bg #fffef2 border T:1px solid #fffef2 / R:1px solid #fffef2 / B:1px solid #fffef2 / L:1px solid #fffef2; a::after.c-button.m-secondary 16pxx16px bg #fffef2 | = | a.c-button.m-secondary 390.0x48.0 bg #fffef2 border T:1px solid #fffef2 / R:1px solid #fffef2 / B:1px solid #fffef2 / L:1px solid #fffef2; a::after.c-button.m-secondary 16pxx16px bg #fffef2 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

### Footer

#### footer

Footer. The page foot: the newsletter block, help and service link columns, social and region links, and the "Online Preferences" OneTrust trigger.

Page: pdp. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1027.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #252525 |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 12px/18px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | span.c-content-reassurance__text: SuisseIntl-Medium 14px/21px 400, #fffef2 |
| Transition | none |
| Painted layers | footer.l-footer 1440.0x1027.2 bg #252525; div.l-footer__top 1440.0x88.0 bg #252525; div.l-footer__middle-inner.l-grid--large 1200.0x846.6 border B:1px solid #fffef2; h2.l-footer__nav-link.m-level-1 176.0x43.0 border B:1px solid #fffef2; h2.l-footer__nav-link.m-level-1 176.0x43.0 border B:1px solid #fffef2; h2.l-footer__nav-link.m-level-1 176.0x43.0 border B:1px solid #fffef2 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-col-title

Footer column title. A footer column heading.

Page: pdp. Selector: `footer column title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 176 x 43 |
| Padding | 0px 0px 15px 0px |
| Border | T: none; R: none; B: 1px solid #fffef2; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 18px/27px 700 |
| Letter spacing | normal |
| Colour | #fffef2 |
| Transition | none |
| Painted layers | h2.l-footer__nav-link.m-level-1 176.0x43.0 border B:1px solid #fffef2 |
| How | at rest |

Crops: `footer-col-title-default.png`.

#### footer-link

Footer link. A footer link (Contact us, FAQs, Shipping, Returns, Track your order).

Page: pdp. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 70 x 24.8 | = | = | = |
| Padding | 0px 0px 8px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl 14px/16.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fffef2 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-prefs-link

Online Preferences link. The OneTrust "Online Preferences" cookie-settings trigger in the footer. Measured, never pressed.

Page: pdp. Selector: `a.optanon-show-settings`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 123.64 x 24.8 | = | = | = |
| Padding | 0px 0px 8px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl 14px/16.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fffef2 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-prefs-link-default.png`, `footer-prefs-link-hover.png`, `footer-prefs-link-focus-visible.png`, `footer-prefs-link-pressed.png`.

#### newsletter-field

Newsletter field. The footer email field, if the region serves one: typed and deleted, never submitted.

Page: pdp. Selector: `footer input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 370 x 40 | = | = |
| Padding | 0px 16px | = | = |
| Border | 1px solid #333333 @ 0.2 | 1px solid #333333 | 1px solid #333333 |
| Radius | 0px | = | = |
| Background | #fffef2 | = | = |
| Box shadow | none | #333333 0px 0px 0px 1px | #333333 0px 0px 0px 1px |
| Outline | none | = | = |
| Font | SuisseIntl 14px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #333333 | #000000 | #000000 |
| Transition | box-shadow, border-color 0.2s, 0.2s ease, ease-in-out delay 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | #000000 @ 0, opacity 1 | #333333, opacity 1 | #333333, opacity 1 |
| Painted layers | input.c-text-field 370.0x40.0 bg #fffef2 border T:1px solid #333333 @ 0.2 / R:1px solid #333333 @ 0.2 / B:1px solid #333333 @ 0.2 / L:1px solid #333333 @ 0.2 | input.c-text-field 370.0x40.0 bg #fffef2 border T:1px solid #333333 / R:1px solid #333333 / B:1px solid #333333 / L:1px solid #333333 shadow #333333 0px 0px 0px 1px | input.c-text-field 370.0x40.0 bg #fffef2 border T:1px solid #333333 / R:1px solid #333333 / B:1px solid #333333 / L:1px solid #333333 shadow #333333 0px 0px 0px 1px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `newsletter-field-default.png`, `newsletter-field-focused.png`, `newsletter-field-filled.png`.

### Catalogue page (PLP)

#### plp-title

Catalogue title. The "Shop all" heading over the results grid, beside the product count.

Page: shopall. Selector: `h1.c-refinements__category-name`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 88.3 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 24px/30px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| How | at rest |

Crops: `plp-title-default.png`.

#### filter-toggle

All filters button. The "All filters" toggle opening the refinement panel.

Page: shopall. Selector: `button.c-refinements-toggler`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 96.77 x 21 | = | = | = |
| Padding | 0px 40px 0px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl-Medium 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | = | = | = |
| Text node | span: SuisseIntl-Medium 14px/21px 400, #333333 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 16px x 16px, absolute, bg #333333, radius 0px | = | = | = |
| Painted layers | button::after.c-refinements-toggler 16pxx16px bg #333333; span.c-refinements-toggler__qty 0.0x0.0 bg #333333 r 50% | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filter-toggle-default.png`, `filter-toggle-hover.png`, `filter-toggle-focus-visible.png`, `filter-toggle-pressed.png`.

#### filter-panel

Refinement rail. The left-hand "Filter by" rail the All filters toggle opens: Price and attribute groups (Skin type, Skin concern, Form, Ingredients, Aroma) as accordion rows, RESET ALL and APPLY at the foot.

Page: shopall. Selector: `refinement rail`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 400 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fffef2 |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 12px/18px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | span.c-anchor__overlay.h-show-for-sr: SuisseIntl 12px/18px 400, #333333 |
| Transition | none |
| Painted layers | div.c-sliding-panel.h-bgcolor-light 400.0x900.0 bg #fffef2; header.c-refinements.h-flex 400.0x57.0 bg #fffef2 border B:1px solid #333333 @ 0.2; button::after.c-refinements__header-back 16pxx16px bg #333333; div.c-refinement.m-range 400.0x49.8 border T:1px solid #bcbbb4; span::after.c-accordion__icon 16pxx16px bg #333333; input.c-text-field 159.0x40.0 bg #fffef2 border T:1px solid #333333 @ 0.2 / R:1px solid #333333 @ 0.2 / B:1px solid #333333 @ 0.2 / L:1px solid #333333 @ 0.2 |
| Ancestor paint | 1 up body.page-search.no-apple-pay bg #fffef2 |
| How | at rest |

Crops: `filter-panel-default.png`.

#### filter-option

Filter option. A refinement row inside the panel.

Page: shopall. Selector: `filter option`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 30.41 x 24 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | SuisseIntl 14px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | = |
| Transition | transform, font-size, left 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = |
| Cursor | pointer | = |
| ::before | 100% x calc(50% + 2px), absolute, bg #fffef2, radius 4px 4px 0px 0px | = |
| Painted layers | label::before.c-sorting.c-select 100%xcalc(50% + 2px) bg #fffef2 r 4px 4px 0px 0px | = |
| How | at rest | mouse hover |

Crops: `filter-option-default.png`, `filter-option-hover.png`.

#### product-card

Product tile. A product cell in the grid: a "New addition" tag when present, the product photograph, the name and the price.

Page: shopall. Selector: `.c-product-tile`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 270 x 540 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | SuisseIntl 12px/18px 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | = |
| Text node | span.c-product-badge: SuisseIntl-Medium 11px/normal 400, #945c26 | = |
| Transition | none | = |
| Painted layers | span::after.c-add-to-wishlist 16pxx16px bg #000000; label::before.c-select.m-float 33.3438pxx10px bg #fffef2 r 4px 4px 0px 0px; div::after.c-select__container 22pxx22px bg #333333; select.c-select 270.0x40.0 bg #fffef2 border T:1px solid #333333 @ 0.2 / R:1px solid #333333 @ 0.2 / B:1px solid #333333 @ 0.2 / L:1px solid #333333 @ 0.2; button.c-button.c-product-add-bag 270.0x48.0 bg #333333 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button::before.c-button.c-product-add-bag 14pxx14px bg #fffef2 | = |
| How | at rest | mouse hover |

Crops: `product-card-default.png`, `product-card-hover.png`.

#### product-card-name

Product tile name. The product name under the tile photograph.

Page: shopall. Selector: `.c-product-tile__name`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 270 x 30.23 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 14px/15.12px 700 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | a: SuisseIntl 14px/15.12px 700, #333333 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `product-card-name-default.png`.

#### product-card-price

Product tile price. The price under the name.

Page: shopall. Selector: `.c-product-price__value`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 270 x 19.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 16px/19.2px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | span.c-product-price: SuisseIntl 16px/19.2px 400, #333333 |
| Transition | none |
| How | at rest |

Crops: `product-card-price-default.png`.

#### tile-badge

Tile badge. The "New addition" tag over a tile photograph.

Page: shopall. Selector: `tile badge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 67.17 x 14 |
| Padding | 0px |
| Border | none |
| Radius | 0px 4px 4px 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl-Medium 11px/normal 400 |
| Letter spacing | normal |
| Colour | #945c26 |
| Transition | none |
| How | at rest |

Crops: `tile-badge-default.png`.

#### category-title

Category title. The Skin Care landing title.

Page: skincare. Selector: `main h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1170 x 37.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 30px/37.5px 400 |
| Letter spacing | normal |
| Colour | #fffef2 |
| Transition | none |
| How | at rest |

Crops: `category-title-default.png`.

#### category-card

Category card. A subcategory card on the Skin Care landing.

Page: skincare. Selector: `category card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 72.8 x 26.8 | = |
| Padding | 4px 8px 4px 4px | = |
| Gap | 4px | = |
| Border | 1px solid #bcbbb4 | 1px solid #252525 |
| Radius | 4px | = |
| Background | #fffef2 | #f6f5e8 |
| Box shadow | none | = |
| Outline | none | = |
| Font | SuisseIntl 12px/19.2px 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | = |
| Text node | div.c-quicklinks: SuisseIntl 14px/16.8px 400, #333333 | = |
| Transition | background, color, border 0.3s, 0.3s, 0.3s ease, ease, ease delay 0s, 0s, 0s | = |
| Cursor | pointer | = |
| Painted layers | a.c-quicklinks__link 72.8x26.8 bg #fffef2 border T:1px solid #bcbbb4 / R:1px solid #bcbbb4 / B:1px solid #bcbbb4 / L:1px solid #bcbbb4 r 4px | a.c-quicklinks__link 72.8x26.8 bg #f6f5e8 border T:1px solid #252525 / R:1px solid #252525 / B:1px solid #252525 / L:1px solid #252525 r 4px |
| How | at rest | mouse hover |

Crops: `category-card-default.png`, `category-card-hover.png`.

#### filter-group

Filter group row. A refinement group header row inside the rail (Price, Skin type, Skin concern, Form, Ingredients, Aroma).

Page: shopall. Selector: `filter group`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 368 x 48.8 | = | = | = |
| Padding | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl 16px/16.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | = | = | = |
| Text node | span.c-refinement__title-text: SuisseIntl 16px/16.8px 400, #333333 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span::after.c-accordion__icon 16pxx16px bg #333333 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filter-group-default.png`, `filter-group-hover.png`, `filter-group-focus-visible.png`, `filter-group-pressed.png`.

#### filter-apply

Apply button. The black APPLY button at the rail’s foot. Measured, never pressed.

Page: shopall. Selector: `filter apply`. States: .

Not found on the page at capture time.

#### sort-select

Sort select. The "Sort: Featured" dropdown beside the product count.

Page: shopall. Selector: `.c-sorting select`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 160 x 24 | = | = | = |
| Padding | 0px 20px 0px 5px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl 14px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | = | = | = |
| Transition | box-shadow, border-color 0.2s, 0.2s ease, ease-in-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sort-select-default.png`, `sort-select-hover.png`, `sort-select-focus-visible.png`, `sort-select-pressed.png`.

#### category-quicklink

Category quicklink. A quicklink pill on the category landing (Category, Skin type, Skin concern).

Page: skincare. Selector: `.c-quicklinks__link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 72.8 x 26.8 | = | = | = |
| Padding | 4px 8px 4px 4px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #bcbbb4 | 1px solid #252525 | = | 1px solid #252525 |
| Radius | 4px | = | = | = |
| Background | #fffef2 | #f6f5e8 | = | #f6f5e8 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl 12px/19.2px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | = | = | = |
| Text node | div.c-quicklinks: SuisseIntl 14px/16.8px 400, #333333 | = | = | = |
| Transition | background, color, border 0.3s, 0.3s, 0.3s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.c-quicklinks__link 72.8x26.8 bg #fffef2 border T:1px solid #bcbbb4 / R:1px solid #bcbbb4 / B:1px solid #bcbbb4 / L:1px solid #bcbbb4 r 4px | a.c-quicklinks__link 72.8x26.8 bg #f6f5e8 border T:1px solid #252525 / R:1px solid #252525 / B:1px solid #252525 / L:1px solid #252525 r 4px | = | a.c-quicklinks__link 72.8x26.8 bg #f6f5e8 border T:1px solid #252525 / R:1px solid #252525 / B:1px solid #252525 / L:1px solid #252525 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `category-quicklink-default.png`, `category-quicklink-hover.png`, `category-quicklink-focus-visible.png`, `category-quicklink-pressed.png`.

#### category-product

Category product tile. A product tile on the Skin Care landing.

Page: skincare. Selector: `.c-product-tile`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 270 x 540 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | SuisseIntl 12px/18px 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | = |
| Text node | span.c-product-badge: SuisseIntl-Medium 11px/normal 400, #945c26 | = |
| Transition | none | = |
| Painted layers | span::after.c-add-to-wishlist 16pxx16px bg #000000; span::before.c-select.m-float 100%xcalc(50% + 2px) bg #fffef2 r 4px 4px 0px 0px; div.c-select 270.0x40.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.c-button.c-product-add-bag 270.0x48.0 bg #333333 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button::before.c-button.c-product-add-bag 14pxx14px bg #fffef2 | = |
| How | at rest | mouse hover |

Crops: `category-product-default.png`, `category-product-hover.png`.

### Product page (PDP)

#### breadcrumbs

Breadcrumbs. The breadcrumb line over the PDP.

Page: pdp. Selector: `breadcrumbs`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1170 x 30.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 12px/18px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | span.c-breadcrumbs__text: SuisseIntl-Medium 12px/16.8px 400, #333333 |
| Transition | none |
| How | at rest |

Crops: `breadcrumbs-default.png`.

#### breadcrumb-link

Breadcrumb link. A crumb link; the last crumb is the product name.

Page: pdp. Selector: `breadcrumb a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 33.95 x 30.8 | = | = | = |
| Padding | 7px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl-Medium 12px/16.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | = | = | = |
| Text node | span.c-breadcrumbs__text: SuisseIntl-Medium 12px/16.8px 400, #333333 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `breadcrumb-link-default.png`, `breadcrumb-link-hover.png`, `breadcrumb-link-focus-visible.png`, `breadcrumb-link-pressed.png`.

#### pdp-title

Product title. The product name heading the purchase column.

Page: pdp. Selector: `pdp h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 185.03 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CircularStd 24px/30px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| How | at rest |

Crops: `pdp-title-default.png`.

#### pdp-price

Product price. The price beside or under the title.

Page: pdp. Selector: `pdp price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 95.8 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 24px/30px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | span.c-product-price: SuisseIntl 24px/30px 400, #333333 |
| Transition | none |
| How | at rest |

Crops: `pdp-price-default.png`.

#### pdp-subtitle

Product descriptor. The short descriptor line under the product name.

Page: pdp. Selector: `pdp descriptor`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 99.53 x 16.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl-Medium 12px/16.8px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `pdp-subtitle-default.png`.

#### add-to-cart

Add to cart button. The primary purchase bar, caught mid-hydration as "Loading …" before its label resolves. Measured and state-forced, never pressed: pressing it adds the item.

Page: pdp. Selector: `add to cart button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 409.5 x 48 | = | = | = |
| Padding | 13px 24px 12px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #333333 | #252525 | = | #252525 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl-Medium 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fffef2 | = | = | = |
| Text node | span: SuisseIntl-Medium 14px/21px 400, #fffef2 | = | = | = |
| Transition | background-color, color 0.25s, 0.25s ease-out, ease-out delay 0s, 0s | = | = | = |
| Cursor | default | = | = | = |
| ::before | 14px x 14px, static, bg #fffef2, radius 0px | = | = | = |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.c-button.c-product-tile 409.5x48.0 bg #333333 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button::before.c-button.c-product-tile 14pxx14px bg #fffef2 | button.c-button.c-product-tile 409.5x48.0 bg #252525 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button::before.c-button.c-product-tile 14pxx14px bg #fffef2 | = | button.c-button.c-product-tile 409.5x48.0 bg #252525 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button::before.c-button.c-product-tile 14pxx14px bg #fffef2 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `add-to-cart-default.png`, `add-to-cart-hover.png`, `add-to-cart-focus-visible.png`, `add-to-cart-pressed.png`.

#### qty-select

Quantity control. The quantity selector beside Add to cart, when the product offers one.

Page: pdp. Selector: `quantity`. States: .

Not found on the page at capture time.

#### pdp-image

Product gallery. The product photograph column.

Page: pdp. Selector: `pdp gallery`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 700.5 x 700 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 12px/18px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| Painted layers | button::before.c-carousel__arrow-prev.js-carousel__arrow-prev 15pxx40px bg #333333; button::before.c-carousel__arrow-next.js-carousel__arrow-next 15pxx40px bg #333333 |
| How | at rest |

Crops: `pdp-image-default.png`.

#### info-row

Service line. A service message near the purchase bar (complimentary shipping, samples).

Page: pdp. Selector: `pdp service line`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 160.13 x 21 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl-Medium 14px/21px 400 |
| Letter spacing | normal |
| Colour | #fffef2 |
| Transition | none |
| How | at rest |

Crops: `info-row-default.png`.

#### variant-box

Variant box. The variant/size selector above the purchase bar (the bordered "Kit $600.00" box on a kit).

Page: pdp. Selector: `variant box`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 173 x 46.5 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl 12px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | = | = | = |
| Text node | div.c-product-tile__variations-label.h-margin-bottom-1: SuisseIntl 11px/16.5px 400, #666666 | = | = | = |
| Transition | none | = | = | = |
| Painted layers | a.c-variations-carousel__link.m-secondary 66.9x25.0 bg #fffef2 border B:1px solid #333333; a.c-variations-carousel__link.m-secondary 97.5x25.0 bg #fffef2 border B:1px solid #fffef2; button.c-carousel__arrow-prev.js-variations-carousel__arrow-prev 0.0x0.0 bg #fffef2; button::before.c-carousel__arrow-prev.js-variations-carousel__arrow-prev 20pxx20px bg #333333; button.c-carousel__arrow-next.js-variations-carousel__arrow-next 24.0x24.0 bg #fffef2; button::before.c-carousel__arrow-next.js-variations-carousel__arrow-next 20pxx20px bg #333333 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `variant-box-default.png`, `variant-box-hover.png`, `variant-box-focus-visible.png`, `variant-box-pressed.png`.

#### accordion

Accordion row. An expandable information row on the PDP (Description). The block carries h-hide-for-large — desktop never paints it — so this is measured on the mobile PDP at 390.

Page: mobile-pdp. Selector: `.c-accordion__title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 49 |
| Padding | 14px 60px 14px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl-Medium 14px/21px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | span: SuisseIntl-Medium 14px/21px 400, #333333 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `accordion-default.png`.

### Panels and overlays

#### search-panel

Search disclosure. The "I'm looking for…" band the Search button reveals under the nav, with a Close button.

Page: search. Selector: `#headerSimpleSearch`. States: .

Not found on the page at capture time.

#### search-field

Search field. The search text field; typed and deleted, never submitted.

Page: search. Selector: `input.c-simple-search__field`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 960.66 x 40 | = | = |
| Padding | 0px 10px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | #fffef2 | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | SuisseIntl 24px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #333333 | #000000 | #000000 |
| Transition | box-shadow, border-color 0.2s, 0.2s ease, ease-in-out delay 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | #666666, opacity 1 | = | = |
| Painted layers | input.c-simple-search 960.7x40.0 bg #fffef2 | = | = |
| Ancestor paint | 1 up div.c-simple-search__input-group bg #fffef2 | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `search-field-default.png`, `search-field-focused.png`, `search-field-filled.png`.

#### search-close

Search close button. The Close button ending the search disclosure.

Page: search. Selector: `search close`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140 x 50.8 | = | = | = |
| Padding | 16px | = | = | = |
| Border | T: none; R: none; B: none; L: 2px solid #ebeade | = | = | = |
| Radius | 0px | = | = | = |
| Background | #fffef2 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl 14px/16.8px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | = | = | = |
| Text node | span.l-header__search-close: SuisseIntl 14px/16.8px 700, #333333 | = | = | = |
| Transition | background, color 0.5s, 0.5s ease-out, ease-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 12px x 12px, static, bg #666666, radius 0px | 12px x 12px, static, bg #343434, radius 0px | = | 12px x 12px, static, bg #363636, radius 0px |
| ::after | 138px x 2px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.l-header__search-button 140.0x50.8 bg #fffef2 border L:2px solid #ebeade; button::before.l-header__search-button 12pxx12px bg #666666; button::after.l-header__search-button 138pxx2px border T:1px solid #fffef2 / R:1px solid #fffef2 / B:1px solid #fffef2 / L:1px solid #fffef2 | button.l-header__search-button 140.0x50.8 bg #fffef2 border L:2px solid #ebeade; button::before.l-header__search-button 12pxx12px bg #343434; button::after.l-header__search-button 138pxx2px border T:1px solid #fffef2 / R:1px solid #fffef2 / B:1px solid #fffef2 / L:1px solid #fffef2 | = | button.l-header__search-button 140.0x50.8 bg #fffef2 border L:2px solid #ebeade; button::before.l-header__search-button 12pxx12px bg #363636; button::after.l-header__search-button 138pxx2px border T:1px solid #fffef2 / R:1px solid #fffef2 / B:1px solid #fffef2 / L:1px solid #fffef2 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-close-default.png`, `search-close-hover.png`, `search-close-focus-visible.png`, `search-close-pressed.png`.

#### cart-panel

Cart drawer. The right-hand sliding panel the My cart button opens; shows the empty-cart state when nothing was added. Its body logs a JSON parse warning in headless Chromium.

Page: cart. Selector: `.c-sliding-panel.m-right`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 405 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fffef2 |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 12px/18px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | span.c-anchor__overlay.h-show-for-sr: SuisseIntl 12px/18px 400, #333333 |
| Transition | none |
| Painted layers | div.c-sliding-panel.h-bgcolor-light 405.0x900.0 bg #fffef2 |
| Ancestor paint | 1 up body.page-homepage.header-transparent bg #fffef2 |
| How | at rest |

Crops: `cart-panel-default.png`.

#### cart-close

Cart close button. The close control at the drawer’s head.

Page: cart. Selector: `cart close`. States: .

Not found on the page at capture time.

#### signup-dialog

Email sign up dialog. The newsletter modal the Email sign up button mounts (a remote Demandware content fragment).

Page: signup. Selector: `signup modal`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 970 x 450 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fffef2 |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 12px/18px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | button.c-modal: SuisseIntl 0px/normal 400, #000000 |
| Transition | none |
| Painted layers | div.c-modal__wrapper 970.0x450.0 bg #fffef2; button::before.c-modal 16pxx16px bg #333333 |
| How | at rest |

Crops: `signup-dialog-default.png`.

#### signup-field

Sign up email field. The email field inside the dialog; typed and deleted, never submitted.

Page: signup. Selector: `signup email input`. States: .

Not found on the page at capture time.

#### signup-checkbox

Sign up checkbox. A consent checkbox row in the dialog.

Page: signup. Selector: `signup checkbox`. States: .

Not found on the page at capture time.

#### signup-submit

Sign up button. The dialog’s submit button. Measured and state-forced, never pressed: pressing it subscribes an address.

Page: signup. Selector: `signup submit`. States: .

Not found on the page at capture time.

### Stores

#### stores-title

Stores title. "Find a store" — the locator heading.

Page: stores. Selector: `stores h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 399.5 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 30px/30px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `stores-title-default.png`.

#### store-search

Store search field. The "Address, city, postal code…" locator field (a floating-label text field): typed and deleted, never submitted.

Page: stores. Selector: `store search`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 512 x 40 | = | = |
| Padding | 0px 35px | = | = |
| Border | 1px solid #333333 @ 0.2 | 1px solid #333333 | 1px solid #333333 |
| Radius | 0px | = | = |
| Background | #fffef2 | = | = |
| Box shadow | none | #333333 0px 0px 0px 1px | #333333 0px 0px 0px 1px |
| Outline | none | = | = |
| Font | SuisseIntl 14px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #333333 | #000000 | #000000 |
| Transition | box-shadow, border-color 0.2s, 0.2s ease, ease-in-out delay 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | #333333, opacity 1 | = | = |
| Painted layers | input.c-text-field 512.0x40.0 bg #fffef2 border T:1px solid #333333 @ 0.2 / R:1px solid #333333 @ 0.2 / B:1px solid #333333 @ 0.2 / L:1px solid #333333 @ 0.2 | input.c-text-field 512.0x40.0 bg #fffef2 border T:1px solid #333333 / R:1px solid #333333 / B:1px solid #333333 / L:1px solid #333333 shadow #333333 0px 0px 0px 1px | input.c-text-field 512.0x40.0 bg #fffef2 border T:1px solid #333333 / R:1px solid #333333 / B:1px solid #333333 / L:1px solid #333333 shadow #333333 0px 0px 0px 1px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `store-search-default.png`, `store-search-focused.png`, `store-search-filled.png`.

#### store-card

Store card. A boutique listing card on the locator page.

Page: stores. Selector: `store card`. States: .

Not found on the page at capture time.

#### store-geolocate

Geolocate button. The "Geolocate me" option under the search field.

Page: stores. Selector: `geolocate`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 116.13 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl-Medium 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 16px x 16px, static, bg #333333, radius 0px | = | = | = |
| Painted layers | button::before.c-selection-group__geolocation.c-link 16pxx16px bg #333333 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `store-geolocate-default.png`, `store-geolocate-hover.png`, `store-geolocate-focus-visible.png`, `store-geolocate-pressed.png`.

#### store-filters

Store filters. The Filters select beside the search field.

Page: stores. Selector: `store filters`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 178.13 x 40 | = | = | = |
| Padding | 0px 45px 0px 20px | = | = | = |
| Border | 1px solid #333333 @ 0.2 | 1px solid #333333 | = | 1px solid #333333 |
| Radius | 0px | = | = | = |
| Background | #fffef2 | = | = | = |
| Box shadow | none | #333333 0px 0px 0px 1px inset | = | #333333 0px 0px 0px 1px inset |
| Outline | none | = | = | = |
| Font | SuisseIntl 14px/40px 400 | SuisseIntl 14px/40px 500 | = | SuisseIntl 14px/40px 500 |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | #000000 | = | #000000 |
| Text node | span.c-select__text.h-text-size-14: SuisseIntl 14px/40px 400, #333333 | span.c-select__text.h-text-size-14: SuisseIntl 14px/40px 500, #000000 | = | span.c-select__text.h-text-size-14: SuisseIntl 14px/40px 500, #000000 |
| Transition | box-shadow, border-color 0.2s, 0.2s ease, ease-in-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 22px x 22px, absolute, bg #333333, radius 0px | = | = | = |
| Painted layers | button.c-select__placeholder 178.1x40.0 bg #fffef2 border T:1px solid #333333 @ 0.2 / R:1px solid #333333 @ 0.2 / B:1px solid #333333 @ 0.2 / L:1px solid #333333 @ 0.2; button::after.c-select__placeholder 22pxx22px bg #333333; span::before.c-icon__svg 20pxx20px bg #333333 | button.c-select__placeholder 178.1x40.0 bg #fffef2 border T:1px solid #333333 / R:1px solid #333333 / B:1px solid #333333 / L:1px solid #333333 shadow #333333 0px 0px 0px 1px inset; button::after.c-select__placeholder 22pxx22px bg #333333; span::before.c-icon__svg 20pxx20px bg #333333 | = | button.c-select__placeholder 178.1x40.0 bg #fffef2 border T:1px solid #333333 / R:1px solid #333333 / B:1px solid #333333 / L:1px solid #333333 shadow #333333 0px 0px 0px 1px inset; button::after.c-select__placeholder 22pxx22px bg #333333; span::before.c-icon__svg 20pxx20px bg #333333 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `store-filters-default.png`, `store-filters-hover.png`, `store-filters-focus-visible.png`, `store-filters-pressed.png`.

#### map-toggle

Map/Satellite toggle. The Map/Satellite segmented toggle over the map.

Page: stores. Selector: `map toggle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 69.56 x 40 | = | = | = |
| Padding | 0px 17px | = | = | = |
| Border | none | = | = | = |
| Radius | 2px 0px 0px 2px | = | = | = |
| Background | #ffffff | #ebebeb | = | = |
| Box shadow | #000000 @ 0.3 0px 1px 4px -1px | = | = | = |
| Outline | none | = | = | = |
| Font | Roboto 18px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button 69.6x40.0 bg #ffffff r 2px 0px 0px 2px shadow #000000 @ 0.3 0px 1px 4px -1px | button 69.6x40.0 bg #ebebeb r 2px 0px 0px 2px shadow #000000 @ 0.3 0px 1px 4px -1px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `map-toggle-default.png`, `map-toggle-hover.png`, `map-toggle-focus-visible.png`, `map-toggle-pressed.png`.

#### no-result-dialog

No-result dialog. The "No result found / Sorry no stores found" dialog the locator raises for a region with no boutiques; carries an OK dismiss button.

Page: stores. Selector: `no result dialog`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 415 x 210.89 |
| Padding | 24px |
| Border | none |
| Radius | 0px |
| Background | #fffef2 |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 12px/18px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | h2.c-modal: SuisseIntl 30px/37.5px 400, #333333 |
| Transition | none |
| Painted layers | div.c-modal__wrapper 415.0x210.9 bg #fffef2; button.c-button.aos-init 230.0x48.0 bg #333333 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button::before.c-modal 16pxx16px bg #333333 |
| How | at rest |

Crops: `no-result-dialog-default.png`.

#### see-all-link

See all locations link. The "See all locations" link beside the map.

Page: stores. Selector: `see all locations`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 91.94 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl-Medium 12px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `see-all-link-default.png`, `see-all-link-hover.png`, `see-all-link-focus-visible.png`, `see-all-link-pressed.png`.

### Sign in

#### login-title

Sign in title. The sign-in page heading.

Page: login. Selector: `login h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 50.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 36px/50.4px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | span.account_header: SuisseIntl 36px/50.4px 400, #333333 |
| Transition | none |
| How | at rest |

Crops: `login-title-default.png`.

#### login-email

Email field. The sign-in email field: typed and deleted, never submitted.

Page: login. Selector: `login email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 1440 x 40 | = | = |
| Padding | 0px 16px | = | = |
| Border | 1px solid #333333 @ 0.2 | 1px solid #333333 | 1px solid #333333 |
| Radius | 0px | = | = |
| Background | #fffef2 | = | = |
| Box shadow | none | #333333 0px 0px 0px 1px | #333333 0px 0px 0px 1px |
| Outline | none | = | = |
| Font | SuisseIntl 14px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #333333 | #000000 | #000000 |
| Transition | box-shadow, border-color 0.2s, 0.2s ease, ease-in-out delay 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | #333333, opacity 1 | #000000, opacity 1 | #000000, opacity 1 |
| Painted layers | input.textinput.f_email 1440.0x40.0 bg #fffef2 border T:1px solid #333333 @ 0.2 / R:1px solid #333333 @ 0.2 / B:1px solid #333333 @ 0.2 / L:1px solid #333333 @ 0.2 | input.textinput.f_email 1440.0x40.0 bg #fffef2 border T:1px solid #333333 / R:1px solid #333333 / B:1px solid #333333 / L:1px solid #333333 shadow #333333 0px 0px 0px 1px | input.textinput.f_email 1440.0x40.0 bg #fffef2 border T:1px solid #333333 / R:1px solid #333333 / B:1px solid #333333 / L:1px solid #333333 shadow #333333 0px 0px 0px 1px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-email-default.png`, `login-email-focused.png`, `login-email-filled.png`.

#### login-password

Password field. The password field: focused only, never filled or submitted.

Page: login. Selector: `login password input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 1440 x 40 | = |
| Padding | 0px 16px | = |
| Border | 1px solid #333333 @ 0.2 | 1px solid #333333 |
| Radius | 0px | = |
| Background | #fffef2 | = |
| Box shadow | none | #333333 0px 0px 0px 1px |
| Outline | none | = |
| Font | SuisseIntl 14px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | #000000 |
| Transition | box-shadow, border-color 0.2s, 0.2s ease, ease-in-out delay 0s, 0s | = |
| Cursor | text | = |
| Placeholder | #333333, opacity 1 | #000000, opacity 1 |
| Painted layers | input.textinput.f_password 1440.0x40.0 bg #fffef2 border T:1px solid #333333 @ 0.2 / R:1px solid #333333 @ 0.2 / B:1px solid #333333 @ 0.2 / L:1px solid #333333 @ 0.2 | input.textinput.f_password 1440.0x40.0 bg #fffef2 border T:1px solid #333333 / R:1px solid #333333 / B:1px solid #333333 / L:1px solid #333333 shadow #333333 0px 0px 0px 1px |
| How | at rest | clicked into the field |

Crops: `login-password-default.png`, `login-password-focused.png`.

#### login-submit

Sign in button. The sign-in submit. Measured, never pressed.

Page: login. Selector: `login submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 96.72 x 48 | = | = | = |
| Padding | 13px 24px 12px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #393939 | #252525 | #333333 | #252525 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl-Medium 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fcfbef | #fffef2 | #fffef2 | #fffef2 |
| Transition | background-color, color 0.25s, 0.25s ease-out, ease-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.m-autosize.c-button 96.7x48.0 bg #393939 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | button.m-autosize.c-button 96.7x48.0 bg #252525 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | button.m-autosize.c-button 96.7x48.0 bg #333333 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | button.m-autosize.c-button 96.7x48.0 bg #252525 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-focus-visible.png`, `login-submit-pressed.png`.

#### login-register

Register link. The create-account link beside the form.

Page: login. Selector: `register link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 130.39 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl 12px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | #000000 | = | #000000 |
| Text node | span: SuisseIntl 12px/18px 400, #333333 | span: SuisseIntl 12px/18px 400, #000000 | = | span: SuisseIntl 12px/18px 400, #000000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-register-default.png`, `login-register-hover.png`, `login-register-focus-visible.png`, `login-register-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The bar at 390: the burger button, the wordmark, search and cart.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fffef2 @ 0.686 |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 12px/18px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | background 0.5s ease-out |
| Painted layers | header.l-header 390.0x50.0 bg #fffef2 @ 0.686; div.h-ph-item 390.0x50.0 bg #ffffff; div::before.h-ph-item 1950pxx50px image linear-gradient(90deg, #ffffff @ 0 46%, #ffffff @ 0.35 50%, #ffffff @ 0 54%); div.h-ph-col--12.h-ph-row-30 390.0x50.0 bg #ced4da; div.c-content-panel.m-closed 0.0x0.0 bg #333333; button::before.c-content-panel 16pxx16px bg #fffef2 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Burger button. The menu trigger; opens the navigation drawer.

Page: home. Selector: `button.c-hamburger__button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50 x 52 | = | = | = |
| Padding | 18px 16px 10px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| ::before | 20px x 20px, static, bg #333333, radius 0px | = | = | = |
| Painted layers | button::before.c-hamburger 20pxx20px bg #333333 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-drawer

Mobile menu drawer. The navigation accordion the burger button opens.

Page: home. Selector: `mobile drawer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 539.17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 12px/18px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | span.c-navigation__link-name: SuisseIntl 14px/16.8px 400, #333333 |
| Transition | none |
| Painted layers | ul.c-navigation__list.m-level-1 390.0x539.2 bg #fffef2; li.c-navigation__item.m-parent 390.0x49.0 border B:1px solid #333333 @ 0.2; span::after.c-navigation__icon 12pxx12px bg #333333; div.c-navigation__flyout-element 390.0x0.0 bg #f6f5e8; ul.c-navigation__list.m-level-2 390.0x197.1 bg #f6f5e8; span.c-navigation__item-title.m-level-2 390.0x48.0 bg #f6f5e8 |
| Ancestor paint | 1 up div.c-hamburger__content bg #f6f5e8 |
| How | at rest |

Crops: `m-menu-drawer-default.png`.

#### m-nav-item

Mobile nav item. A level-1 accordion row inside the drawer (Gifts, New & Notable, Skin Care…).

Page: home. Selector: `m nav item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 390 x 48.02 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl 14px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

## Transitions declared in the readable stylesheets

Every readable stylesheet on each captured page (Aesop's Demandware bundles are same-origin); the per-state Transition rows above are computed values.

- home: `filter 0.4s`, `box-shadow 0.2s, border-color 0.2s ease-in-out`, `transform 0.2s, font-size 0.2s, left 0.2s`, `0.2s ease-in-out`, `transform 0.15s ease-out`, `transform 0.3s`, `max-height 0.1s`, `opacity, background 0.5s`, `background-color 0.25s ease-out, color 0.25s ease-out`, `0.3s ease-in-out`, `background 0.3s ease-out`, `opacity 0.5s, transform 0.5s`

- shopall: `filter 0.4s`, `box-shadow 0.2s, border-color 0.2s ease-in-out`, `transform 0.2s, font-size 0.2s, left 0.2s`, `0.2s ease-in-out`, `transform 0.15s ease-out`, `transform 0.3s`, `max-height 0.1s`, `opacity, background 0.5s`, `background-color 0.25s ease-out, color 0.25s ease-out`, `0.3s ease-in-out`, `background 0.3s ease-out`, `opacity 0.5s, transform 0.5s`
