# Component measurements

Computed styles read from creativemarket.com on 2026-11-12 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the home page, /fonts, a product page, /search, /membership and /sign-in — the CookieYes banner and chat launcher hidden, never answered — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### site-header

Site header. The top bar: All Categories dropdown, the 585px search field, Join | Log in, the amber Save 25% button and the cart icon.

Page: home. Selector: `.site-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 73 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Averta 16px/24px 400 |
| Letter spacing | normal |
| Colour | #303538 |
| Text node | span.ui-select__single-label: Averta 14px/20px 600, #303538 |
| Transition | none |
| Icon | 0 x 0, colour #088178 |
| Painted layers | div.site-header-wrapper 1440.0x73.0 bg #ffffff; button.ui-button.ui-button--ghost 0.0x0.0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 3.35544e+07px; input.search-field__input 585.0x44.0 bg #fafdff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 100px; div::before.search-field__category 1pxx24px bg #899298; div.multiselect__tags 120.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 3px; div.multiselect__content-wrapper 0.0x0.0 bg #ffffff border T:1px solid #edf2f5 / R:1px solid #edf2f5 / B:1px solid #edf2f5 / L:1px solid #edf2f5 r 8px shadow #000000 @ 0.15 0px 0px 8px 0px |
| Ancestor paint | 1 up div bg #ffffff |
| How | at rest |

Crops: `site-header-default.png`.

#### logo

Logo. The Creative Market logo anchor.

Page: home. Selector: `logo anchor`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 88 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Averta 16px/24px 400 |
| Letter spacing | normal |
| Colour | #303538 |
| Transition | color 0.25s ease |
| Cursor | pointer |
| Icon | 87.98 x 34.73, colour #303538, fill #000000 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-search

Nav search field. The 585x44 header search (All Categories dropdown + field); never submitted.

Page: home. Selector: `form.search-field`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 585 x 44 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Averta 15px/22px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #303538 | = | - | = |
| Text node | span.ui-select__single-label: Averta 14px/20px 600, #303538 | = | - | = |
| Transition | none | = | - | = |
| Icon | 16 x 16, colour #899298, fill #000000 | = | - | = |
| Painted layers | input.search-field__input 585.0x44.0 bg #fafdff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 100px; div::before.search-field__category 1pxx24px bg #899298; div.multiselect__tags 120.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 3px; div.multiselect__content-wrapper 0.0x0.0 bg #ffffff border T:1px solid #edf2f5 / R:1px solid #edf2f5 / B:1px solid #edf2f5 / L:1px solid #edf2f5 r 8px shadow #000000 @ 0.15 0px 0px 8px 0px; span.multiselect__option.multiselect__option--highlight 0.0x0.0 bg #edf2f5; div.search-dropdown 0.0x0.0 bg #ffffff r 24px shadow #000000 @ 0.15 0px 0px 8px 0px | input.search-field__input 585.0x44.0 bg #fafdff border T:1px solid #ccd4da / R:1px solid #ccd4da / B:1px solid #ccd4da / L:1px solid #ccd4da r 100px; div::before.search-field__category 1pxx24px bg #899298; div.multiselect__tags 120.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 3px; div.multiselect__content-wrapper 0.0x0.0 bg #ffffff border T:1px solid #edf2f5 / R:1px solid #edf2f5 / B:1px solid #edf2f5 / L:1px solid #edf2f5 r 8px shadow #000000 @ 0.15 0px 0px 8px 0px; span.multiselect__option.multiselect__option--highlight 0.0x0.0 bg #edf2f5; div.search-dropdown 0.0x0.0 bg #ffffff r 24px shadow #000000 @ 0.15 0px 0px 8px 0px | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-search-default.png`, `nav-search-hover.png`, `nav-search-pressed.png`.

#### join-link

Join link. The "Join" user link; measured, never followed.

Page: home. Selector: `a.user-link__link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 31.34 x 18 | 31.34 x 20 | = | 31.34 x 20 |
| Padding | 0px | = | = | = |
| Border | none | T: none; R: none; B: 2px solid #303538; L: none | = | T: none; R: none; B: 2px solid #303538; L: none |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #e06868 offset 1px | = |
| Font | Averta 14px/14px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #303538 | #003a37 | = | #003a37 |
| Transition | color 0.25s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |
| Painted layers | - | a.user-link__link 31.3x20.0 border B:2px solid #303538 | a.user-link__link 31.3x18.0 outline 2px solid #e06868 offset 1px | a.user-link__link 31.3x20.0 border B:2px solid #303538 |

Crops: `join-link-default.png`, `join-link-hover.png`, `join-link-focus-visible.png`, `join-link-pressed.png`.

#### save25-button

Save 25% button. The amber "Save 25%" ui-button--accent (92x32); measured, never followed.

Page: home. Selector: `a.ui-button--accent`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 92.95 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 2px solid #4e42a1 | 2px solid #281f6b | = | 2px solid #281f6b |
| Radius | 8px | = | = | = |
| Background | #4e42a1 | #281f6b | = | #281f6b |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4e42a1 offset 2px | = |
| Font | Averta 14px/14px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.ui-button__label: Averta 14px/14px 600, #ffffff | = | = | = |
| Transition | color, background-color, border-color 0.2s cubic-bezier(0.32, 0, 0.59, 0.03) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.ui-button.ui-button--filled 93.0x32.0 bg #4e42a1 border T:2px solid #4e42a1 / R:2px solid #4e42a1 / B:2px solid #4e42a1 / L:2px solid #4e42a1 r 8px | a.ui-button.ui-button--filled 93.0x32.0 bg #281f6b border T:2px solid #281f6b / R:2px solid #281f6b / B:2px solid #281f6b / L:2px solid #281f6b r 8px | a.ui-button.ui-button--filled 93.0x32.0 bg #4e42a1 border T:2px solid #4e42a1 / R:2px solid #4e42a1 / B:2px solid #4e42a1 / L:2px solid #4e42a1 r 8px outline 2px solid #4e42a1 offset 2px | a.ui-button.ui-button--filled 93.0x32.0 bg #281f6b border T:2px solid #281f6b / R:2px solid #281f6b / B:2px solid #281f6b / L:2px solid #281f6b r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `save25-button-default.png`, `save25-button-hover.png`, `save25-button-focus-visible.png`, `save25-button-pressed.png`.

#### cart-icon

Cart icon. The header cart icon with its count badge.

Page: home. Selector: `cart icon`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 20 x 23 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Averta 14px/14px 600 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #088178 | #003a37 | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 20 x 21, colour #000000 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `cart-icon-default.png`, `cart-icon-hover.png`, `cart-icon-pressed.png`.

#### nav-link

Category nav link. A lower-nav category item (FONTS/TEMPLATES/...); measured, never followed.

Page: home. Selector: `.lower-nav a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 47.94 x 14 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #e06868 offset 1px | = |
| Font | Averta 13px/14px 400 | = | = | = |
| Letter spacing | 1px | = | = | = |
| Colour | #303538 | #088178 | = | #003a37 |
| Transition | color, text-shadow 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.lower-nav__item-link 47.9x14.0 outline 2px solid #e06868 offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

### Home

#### a11y-h1

Accessibility h1. "Bring your creative ideas to life." — a visually-hidden h1; recorded for the type style, not painted.

Page: home. Selector: `h1.u-visually-hidden`. States: .

Not found on the page at capture time.

#### search-strip-heading

Hero heading. "Try a new way to search fonts" — the painted headline under the hidden h1.

Page: home. Selector: `smart-search heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 625 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Averta 24px/32px 600 |
| Letter spacing | normal |
| Colour | #303538 |
| Transition | none |
| Ancestor paint | 1 up div.homepage-smart-search-strip__banner bg #f4f8fb |
| How | at rest |

Crops: `search-strip-heading-default.png`.

#### row-title

Section heading. A homepage row heading ("Popular Fonts").

Page: home. Selector: `h2.homepage-row-title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1260 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Averta 24px/32px 600 |
| Letter spacing | normal |
| Colour | #303538 |
| Text node | span.text: Averta 24px/32px 600, #303538 |
| Transition | none |
| Icon | 7 x 14, colour #303538 |
| How | at rest |

Crops: `row-title-default.png`.

#### product-card

Product card. A product card in a home row (artwork, name, shop, teal price pill); measured, never followed.

Page: home. Selector: `.product-card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 337 x 275.52 | = | = | = |
| Padding | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Averta 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #303538 | = | = | = |
| Text node | span.product-thumbnail-badge__text: Averta 14px/14px 400, #303538 | span.product-thumbnail-badge__text: Averta 14px/14px 400, #003a37 | = | = |
| Transition | none | = | = | = |
| Icon | 16 x 16, colour #303538 | = | = | = |
| Painted layers | a 329.0x219.3 bg #edf2f5; div.product-thumbnail-badge 143.4x28.0 bg #ffffff border T:1px solid #edf2f5 / R:1px solid #edf2f5 / B:1px solid #edf2f5 / L:1px solid #edf2f5 r 0px 18px 0px 0px; button.like-button.product-thumbnail__like-button 30.0x30.0 bg #ffffff @ 0.9 r 3.35544e+07px shadow #000000 @ 0.1 0px 1px 8px 0px, #000000 @ 0.05 0px 0px 1px 1px, #ffffff 0px 1px 1px 0px inset, #ffffff @ 0.25 0px -1px 0px 0px inset; button.sp-button.product-card-add-to-cart 0.0x0.0 bg #088178 border T:2px solid #088178 / R:2px solid #088178 / B:2px solid #088178 / L:2px solid #088178; div.product-info__price 36.3x25.0 bg #dff8f6 r 3px | a 329.0x219.3 bg #edf2f5; div.product-thumbnail-badge 143.4x28.0 bg #ffffff border T:1px solid #edf2f5 / R:1px solid #edf2f5 / B:1px solid #edf2f5 / L:1px solid #edf2f5 r 0px 18px 0px 0px; button.like-button.product-thumbnail__like-button 30.0x30.0 bg #ffffff @ 0.9 r 3.35544e+07px shadow #000000 @ 0.1 0px 1px 8px 0px, #000000 @ 0.05 0px 0px 1px 1px, #ffffff 0px 1px 1px 0px inset, #ffffff @ 0.25 0px -1px 0px 0px inset; button.sp-button.product-card-add-to-cart 329.0x44.0 bg #088178 border T:2px solid #088178 / R:2px solid #088178 / B:2px solid #088178 / L:2px solid #088178; div.product-info__price 36.3x25.0 bg #dff8f6 r 3px | a 329.0x219.3 bg #edf2f5 outline 2px solid #e06868 offset 1px; div.product-thumbnail-badge 143.4x28.0 bg #ffffff border T:1px solid #edf2f5 / R:1px solid #edf2f5 / B:1px solid #edf2f5 / L:1px solid #edf2f5 r 0px 18px 0px 0px; button.like-button.product-thumbnail__like-button 30.0x30.0 bg #ffffff @ 0.9 r 3.35544e+07px shadow #000000 @ 0.1 0px 1px 8px 0px, #000000 @ 0.05 0px 0px 1px 1px, #ffffff 0px 1px 1px 0px inset, #ffffff @ 0.25 0px -1px 0px 0px inset; button.sp-button.product-card-add-to-cart 0.0x0.0 bg #088178 border T:2px solid #088178 / R:2px solid #088178 / B:2px solid #088178 / L:2px solid #088178; div.product-info__price 36.3x25.0 bg #dff8f6 r 3px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `product-card-default.png`, `product-card-hover.png`, `product-card-focus-visible.png`, `product-card-pressed.png`.

#### add-to-cart-btn

Card add-to-cart. A product card's sp-button add-to-cart (paints on card hover); measured only — pressing it would change the cart.

Page: home. Selector: `product-card-add-to-cart`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 329 x 44 |
| Padding | 10px 22px |
| Border | 2px solid #003a37 |
| Radius | 0px |
| Background | #003a37 |
| Box shadow | none |
| Outline | none |
| Font | Averta 16px/normal 600 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.no-pointer-events: Averta 16px/normal 600, #ffffff |
| Transition | all 0.25s ease |
| Cursor | pointer |
| Painted layers | button.sp-button.product-card-add-to-cart 329.0x44.0 bg #003a37 border T:2px solid #003a37 / R:2px solid #003a37 / B:2px solid #003a37 / L:2px solid #003a37 |
| How | at rest |

Crops: `add-to-cart-btn-default.png`.

#### newsletter-field

Newsletter field. The email banner input (368x31); filled with a placeholder, never submitted.

Page: home. Selector: `email banner input`. States: default, focus-visible, filled.

| Property | default | focus-visible | filled |
|---|---|---|---|
| Size (w x h) | 368 x 31 | = | = |
| Padding | 1px 2px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Averta 16px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #303538 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| Painted layers | input.email-sign-up-banner__email-input 368.0x31.0 bg #ffffff | = | = |
| Ancestor paint | 1 up div.email-sign-up-banner__input-group bg #ffffff | = | = |
| How | at rest | Shift+Tab, Tab | typed "name@example.com", then deleted; nothing sent |

Crops: `newsletter-field-default.png`, `newsletter-field-focus-visible.png`, `newsletter-field-filled.png`.

### Category

#### category-h1

Category headline. "Fonts" — the category page title.

Page: category. Selector: `category h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1376 x 70.38 |
| Padding | 7.2px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Averta 48px/56px 600 |
| Letter spacing | normal |
| Colour | #303538 |
| Transition | none |
| How | at rest |

Crops: `category-h1-default.png`.

#### filter-btn

Filter button. The "Browse by Category" filter disclosure; toggled locally.

Page: category. Selector: `button.open-filter-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 218.95 x 44 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 32px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #e06868 offset 0px | = |
| Font | Averta 16px/normal 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 7, colour #000000 | = | = | = |
| Painted layers | button.open-filter-btn 219.0x44.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 32px | = | button.open-filter-btn 219.0x44.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 32px outline 2px solid #e06868 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filter-btn-default.png`, `filter-btn-hover.png`, `filter-btn-focus-visible.png`, `filter-btn-pressed.png`.

#### filter-group

Filter groups. The Classification/Style/Aesthetic filter column.

Page: category. Selector: `.filter-groups-container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 202 |
| Padding | 12px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Averta 16px/24px 400 |
| Letter spacing | normal |
| Colour | #303538 |
| Text node | span.selection-pill__label: Averta 16px/24px 400, #000000 |
| Transition | none |
| Icon | 4 x 4, colour #303538 |
| Painted layers | a.selection-pill 149.5x54.0 border T:1px solid #ccd4da / R:1px solid #ccd4da / B:1px solid #ccd4da / L:1px solid #ccd4da r 32px; a.selection-pill 86.4x54.0 border T:1px solid #ccd4da / R:1px solid #ccd4da / B:1px solid #ccd4da / L:1px solid #ccd4da r 32px; a.selection-pill 118.7x54.0 border T:1px solid #ccd4da / R:1px solid #ccd4da / B:1px solid #ccd4da / L:1px solid #ccd4da r 32px; a.selection-pill 74.8x54.0 border T:1px solid #ccd4da / R:1px solid #ccd4da / B:1px solid #ccd4da / L:1px solid #ccd4da r 32px; a.selection-pill 103.8x54.0 border T:1px solid #ccd4da / R:1px solid #ccd4da / B:1px solid #ccd4da / L:1px solid #ccd4da r 32px; a.selection-pill 107.1x54.0 border T:1px solid #ccd4da / R:1px solid #ccd4da / B:1px solid #ccd4da / L:1px solid #ccd4da r 32px |
| Ancestor paint | 1 up div.filters-dropdown bg #ffffff shadow #000000 @ 0.15 0px 0px 8px 0px |
| How | at rest |

Crops: `filter-group-default.png`.

#### category-card

Category product card. A product thumbnail card in the category grid (image, name, shop); measured, never followed.

Page: category. Selector: `product-thumbnail card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 320 x 213.33 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Averta 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #303538 | = | = | = |
| Text node | span.product-thumbnail-badge__text: Averta 14px/14px 400, #303538 | span.product-thumbnail-badge__text: Averta 14px/14px 400, #003a37 | = | = |
| Transition | none | = | = | = |
| Icon | 16 x 16, colour #303538 | = | = | = |
| Painted layers | a 320.0x213.3 bg #edf2f5; div.product-thumbnail-badge 143.4x28.0 bg #ffffff border T:1px solid #edf2f5 / R:1px solid #edf2f5 / B:1px solid #edf2f5 / L:1px solid #edf2f5 r 0px 18px 0px 0px; button.like-button.product-thumbnail__like-button 30.0x30.0 bg #ffffff @ 0.9 r 3.35544e+07px shadow #000000 @ 0.1 0px 1px 8px 0px, #000000 @ 0.05 0px 0px 1px 1px, #ffffff 0px 1px 1px 0px inset, #ffffff @ 0.25 0px -1px 0px 0px inset; button.sp-button.product-card-add-to-cart 0.0x0.0 bg #088178 border T:2px solid #088178 / R:2px solid #088178 / B:2px solid #088178 / L:2px solid #088178 | a 320.0x213.3 bg #edf2f5; div.product-thumbnail__font-preview 320.0x213.3 bg #ffffff; div.product-thumbnail-badge 143.4x28.0 bg #ffffff border T:1px solid #edf2f5 / R:1px solid #edf2f5 / B:1px solid #edf2f5 / L:1px solid #edf2f5 r 0px 18px 0px 0px; button.like-button.product-thumbnail__like-button 30.0x30.0 bg #ffffff @ 0.9 r 3.35544e+07px shadow #000000 @ 0.1 0px 1px 8px 0px, #000000 @ 0.05 0px 0px 1px 1px, #ffffff 0px 1px 1px 0px inset, #ffffff @ 0.25 0px -1px 0px 0px inset; button.sp-button.product-card-add-to-cart 320.0x44.0 bg #088178 border T:2px solid #088178 / R:2px solid #088178 / B:2px solid #088178 / L:2px solid #088178 | a 320.0x213.3 bg #edf2f5 outline 2px solid #e06868 offset 1px; div.product-thumbnail__font-preview 320.0x213.3 bg #ffffff; div.product-thumbnail-badge 143.4x28.0 bg #ffffff border T:1px solid #edf2f5 / R:1px solid #edf2f5 / B:1px solid #edf2f5 / L:1px solid #edf2f5 r 0px 18px 0px 0px; button.like-button.product-thumbnail__like-button 30.0x30.0 bg #ffffff @ 0.9 r 3.35544e+07px shadow #000000 @ 0.1 0px 1px 8px 0px, #000000 @ 0.05 0px 0px 1px 1px, #ffffff 0px 1px 1px 0px inset, #ffffff @ 0.25 0px -1px 0px 0px inset; button.sp-button.product-card-add-to-cart 0.0x0.0 bg #088178 border T:2px solid #088178 / R:2px solid #088178 / B:2px solid #088178 / L:2px solid #088178 | a 320.0x213.3 bg #edf2f5; div.product-thumbnail__font-preview 320.0x213.3 bg #ffffff; div.product-thumbnail-badge 143.4x28.0 bg #ffffff border T:1px solid #edf2f5 / R:1px solid #edf2f5 / B:1px solid #edf2f5 / L:1px solid #edf2f5 r 0px 18px 0px 0px; button.like-button.product-thumbnail__like-button 30.0x30.0 bg #ffffff @ 0.9 r 3.35544e+07px shadow #000000 @ 0.1 0px 1px 8px 0px, #000000 @ 0.05 0px 0px 1px 1px, #ffffff 0px 1px 1px 0px inset, #ffffff @ 0.25 0px -1px 0px 0px inset; button.sp-button.product-card-add-to-cart 320.0x44.0 bg #088178 border T:2px solid #088178 / R:2px solid #088178 / B:2px solid #088178 / L:2px solid #088178 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `category-card-default.png`, `category-card-hover.png`, `category-card-focus-visible.png`, `category-card-pressed.png`.

### Product

#### product-h1

Product title. "Silver Garden - Nostalgic Font Duo" (h1.sp-h4).

Page: product. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 391.14 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Averta 24px/32px 600 |
| Letter spacing | normal |
| Colour | #303538 |
| Transition | none |
| How | at rest |

Crops: `product-h1-default.png`.

#### shop-byline

Shop byline. "SilverStag Type Foundry | Featured" — the author row.

Page: product. Selector: `.shop-info-details`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 391.14 x 25.22 |
| Padding | 0px |
| Gap | 8px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Averta 14px/14px 400 |
| Letter spacing | normal |
| Colour | #303538 |
| Text node | span.header-badge__text: Averta 14px/14px 400, #303538 |
| Transition | none |
| Painted layers | a.header-badge.header-badge--shop 197.3x25.2 bg #f4f8fb r 14400px; div::after.header-badge__icon 17.2188pxx17.2188px r 50% shadow #000000 @ 0.07 0px 0px 0px 1px inset; span.header-badge.header-badge--featured-shop 99.1x25.2 bg #f4f8fb r 14400px |
| How | at rest |

Crops: `shop-byline-default.png`.

#### buy-box-price

Price. The buy-box price ($79).

Page: product. Selector: `.buy-box-price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 50.08 x 35 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Averta 16px/24px 400 |
| Letter spacing | normal |
| Colour | #303538 |
| Text node | span.buy-box-price: Averta 28px/35px 600, #303538 |
| Transition | none |
| Painted layers | span.tooltip-text 0.0x0.0 bg #303538 r 6px shadow #000000 @ 0.2 0px 2px 4px 0px |
| How | at rest |

Crops: `buy-box-price-default.png`.

#### license-row

License row. A license option row in the buy box (label + $79.00 price).

Page: product. Selector: `.checkbox-row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 450 x 24 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Averta 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #303538 | = |
| Text node | label.checkbox-label: Averta 16px/24px 600, #303538 | = |
| Transition | none | = |
| Icon | 16 x 14, colour #899298 | = |
| Painted layers | input 18.0x18.0 bg #088178 border T:2px solid #088178 / R:2px solid #088178 / B:2px solid #088178 / L:2px solid #088178 r 4px; input::after 12pxx12px image url(data:…); span.tooltip-text 0.0x0.0 bg #303538 r 6px shadow #000000 @ 0.2 0px 2px 4px 0px | = |
| How | at rest | mouse hover |

Crops: `license-row-default.png`, `license-row-hover.png`.

#### add-cart

Add to cart. The primary buy-box button (450x45); measured only — never pressed.

Page: product. Selector: `btn--primary Add to cart`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 450 x 45 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 2px solid #088178 | 2px solid #003a37 | 2px solid #003a37 | 2px solid #003a37 |
| Radius | 8px | = | = | = |
| Background | #088178 | #003a37 | #003a37 | #003a37 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Averta 14px/32px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.no-pointer-events: Averta 14px/32px 600, #ffffff | = | = | = |
| Transition | color, background-color, border-color 0.2s cubic-bezier(0.32, 0, 0.59, 0.03) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 713.594px x 713.594px, absolute, bg #003a37, radius 3.35544e+07px | = | = | = |
| Painted layers | button.btn.btn--primary 450.0x45.0 bg #088178 border T:2px solid #088178 / R:2px solid #088178 / B:2px solid #088178 / L:2px solid #088178 r 8px; button::before.btn.btn--primary 713.594pxx713.594px bg #003a37 r 3.35544e+07px | button.btn.btn--primary 450.0x45.0 bg #003a37 border T:2px solid #003a37 / R:2px solid #003a37 / B:2px solid #003a37 / L:2px solid #003a37 r 8px; button::before.btn.btn--primary 713.594pxx713.594px bg #003a37 r 3.35544e+07px | button.btn.btn--primary 450.0x45.0 bg #003a37 border T:2px solid #003a37 / R:2px solid #003a37 / B:2px solid #003a37 / L:2px solid #003a37 r 8px; button::before.btn.btn--primary 713.594pxx713.594px bg #003a37 r 3.35544e+07px | button.btn.btn--primary 450.0x45.0 bg #003a37 border T:2px solid #003a37 / R:2px solid #003a37 / B:2px solid #003a37 / L:2px solid #003a37 r 8px; button::before.btn.btn--primary 713.594pxx713.594px bg #003a37 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `add-cart-default.png`, `add-cart-hover.png`, `add-cart-focus-visible.png`, `add-cart-pressed.png`.

#### buy-now

Buy now. The secondary buy-box button (450x40); measured only — never pressed.

Page: product. Selector: `buy-box Buy now`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 450 x 40 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Border | 1px solid #899298 | 1px solid #088178 | 1px solid #088178 | 1px solid #088178 |
| Radius | 8px | = | = | = |
| Background | #ffffff | #dff8f6 | #dff8f6 | #dff8f6 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Averta 14px/32px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #088178 | #003a37 | #003a37 | #003a37 |
| Text node | span.no-pointer-events: Averta 14px/32px 600, #088178 | span.no-pointer-events: Averta 14px/32px 600, #003a37 | span.no-pointer-events: Averta 14px/32px 600, #003a37 | span.no-pointer-events: Averta 14px/32px 600, #003a37 |
| Transition | color, background-color, border-color 0.2s cubic-bezier(0.32, 0, 0.59, 0.03) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 716.797px x 716.797px, absolute, bg #dff8f6, radius 3.35544e+07px | = | = | = |
| Painted layers | button.buy-box-actions__buy-now.btn 450.0x40.0 bg #ffffff border T:1px solid #899298 / R:1px solid #899298 / B:1px solid #899298 / L:1px solid #899298 r 8px; button::before.buy-box-actions__buy-now.btn 716.797pxx716.797px bg #dff8f6 r 3.35544e+07px | button.buy-box-actions__buy-now.btn 450.0x40.0 bg #dff8f6 border T:1px solid #088178 / R:1px solid #088178 / B:1px solid #088178 / L:1px solid #088178 r 8px; button::before.buy-box-actions__buy-now.btn 716.797pxx716.797px bg #dff8f6 r 3.35544e+07px | button.buy-box-actions__buy-now.btn 450.0x40.0 bg #dff8f6 border T:1px solid #088178 / R:1px solid #088178 / B:1px solid #088178 / L:1px solid #088178 r 8px; button::before.buy-box-actions__buy-now.btn 716.797pxx716.797px bg #dff8f6 r 3.35544e+07px | button.buy-box-actions__buy-now.btn 450.0x40.0 bg #dff8f6 border T:1px solid #088178 / R:1px solid #088178 / B:1px solid #088178 / L:1px solid #088178 r 8px; button::before.buy-box-actions__buy-now.btn 716.797pxx716.797px bg #dff8f6 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `buy-now-default.png`, `buy-now-hover.png`, `buy-now-focus-visible.png`, `buy-now-pressed.png`.

#### enterprise-cta

Enterprise CTA. "Enterprise or Custom License / Contact sales" row (450x52).

Page: product. Selector: `buy-box-enterprise-cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 450 x 52 | = | = | = |
| Padding | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #dff8f6 | #b6e7e4 | = | #b6e7e4 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #088178 offset 0px | = |
| Font | Averta 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #303538 | = | = | = |
| Text node | span.buy-box-enterprise-cta__title-text: Averta 16px/normal 600, #303538 | = | = | = |
| Transition | background-color 0.15s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 14, colour #088178 | = | = | = |
| Painted layers | button.buy-box-enterprise-cta 450.0x52.0 bg #dff8f6 r 8px; span.tooltip-text 0.0x0.0 bg #303538 r 6px shadow #000000 @ 0.2 0px 2px 4px 0px | button.buy-box-enterprise-cta 450.0x52.0 bg #b6e7e4 r 8px; span.tooltip-text 0.0x0.0 bg #303538 r 6px shadow #000000 @ 0.2 0px 2px 4px 0px | button.buy-box-enterprise-cta 450.0x52.0 bg #dff8f6 r 8px outline 2px solid #088178 offset 0px; span.tooltip-text 0.0x0.0 bg #303538 r 6px shadow #000000 @ 0.2 0px 2px 4px 0px | button.buy-box-enterprise-cta 450.0x52.0 bg #b6e7e4 r 8px; span.tooltip-text 0.0x0.0 bg #303538 r 6px shadow #000000 @ 0.2 0px 2px 4px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `enterprise-cta-default.png`, `enterprise-cta-hover.png`, `enterprise-cta-focus-visible.png`, `enterprise-cta-pressed.png`.

#### follow-btn

Follow button. The shop FOLLOW button; measured, never pressed.

Page: product. Selector: `FOLLOW button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 232 x 35 | = | = | = |
| Padding | 6px 28px | = | = | = |
| Border | 1px solid #e2e9ee | = | = | = |
| Radius | 24px | = | = | = |
| Background | #ffffff | #fafdff | = | #fafdff |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #e06868 offset 0px | = |
| Font | Averta 14px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #303538 | = | = | = |
| Text node | span.action-btn-inner-wrapper: Averta 14px/normal 400, #303538 | = | = | = |
| Transition | text-shadow, background, border-color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 14, colour #303538 | = | = | = |
| Painted layers | button 232.0x35.0 bg #ffffff border T:1px solid #e2e9ee / R:1px solid #e2e9ee / B:1px solid #e2e9ee / L:1px solid #e2e9ee r 24px | button 232.0x35.0 bg #fafdff border T:1px solid #e2e9ee / R:1px solid #e2e9ee / B:1px solid #e2e9ee / L:1px solid #e2e9ee r 24px | button 232.0x35.0 bg #ffffff border T:1px solid #e2e9ee / R:1px solid #e2e9ee / B:1px solid #e2e9ee / L:1px solid #e2e9ee r 24px outline 2px solid #e06868 offset 0px | button 232.0x35.0 bg #fafdff border T:1px solid #e2e9ee / R:1px solid #e2e9ee / B:1px solid #e2e9ee / L:1px solid #e2e9ee r 24px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `follow-btn-default.png`, `follow-btn-hover.png`, `follow-btn-focus-visible.png`, `follow-btn-pressed.png`.

#### specs

Product Specs. The Product Specs block: File Size, Vector, Web Font, creation date.

Page: product. Selector: `section.product-specs-section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 450 x 259 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Averta 16px/24px 400 |
| Letter spacing | normal |
| Colour | #303538 |
| Text node | h2.sp-h4.mb-0: Averta 24px/24px 600, #303538 |
| Transition | none |
| Icon | 16 x 16, colour #4b5258 |
| Painted layers | span::before.icon 100%xauto bg #303538; i::before.property-icon.svg-icon-file-size 24pxx24px bg #4b5258; i::before.property-icon.svg-icon-vector 24pxx24px bg #4b5258; i::before.property-icon.svg-icon-web-font 24pxx24px bg #4b5258; i::before.property-icon.svg-icon-calendar 22pxx23px bg #4b5258; div.report-product 450.0x39.0 border T:1px solid #e2e9ee |
| How | at rest |

Crops: `specs-default.png`.

#### accordion-row

Accordion row. A details/summary accordion row (Reviews/Comments/FAQs); opened state toggled locally, closed again.

Page: product. Selector: `summary`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 878 x 88 | = |
| Padding | 32px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Averta 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #303538 | = |
| Text node | h2.sp-h4.mb-0: Averta 24px/24px 600, #303538 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | span::before.icon 24pxx24px bg #303538 | = |
| How | at rest | own toggle |

Crops: `accordion-row-default.png`, `accordion-row-opened.png`.

#### search-chip

Suggested-search chip. A Suggested Searches pill (Serif, Script, Nostalgic...); measured, never followed.

Page: product. Selector: `a.sp-pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 69.95 x 44 | = | = | = |
| Padding | 10px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | #fee4c3 | #fcc875 | = | #fcc875 |
| Box shadow | none | = | #b9ddff @ 0.45 0px 0px 0px 5px | = |
| Outline | none | = | = | = |
| Font | Averta 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #303538 | #003a37 | = | #003a37 |
| Text node | span.sp-pill__text: Averta 14px/14px 600, #303538 | = | = | = |
| Transition | color 0.25s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.sp-pill 70.0x44.0 bg #fee4c3 r 20px | a.sp-pill 70.0x44.0 bg #fcc875 r 20px | a.sp-pill 70.0x44.0 bg #fee4c3 r 20px shadow #b9ddff @ 0.45 0px 0px 0px 5px | a.sp-pill 70.0x44.0 bg #fcc875 r 20px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-chip-default.png`, `search-chip-hover.png`, `search-chip-focus-visible.png`, `search-chip-pressed.png`.

#### shop-card

Meet the shop. The shop profile card: avatar, name, bio, FOLLOW/MESSAGE, stats (joined, sales, rating).

Page: product. Selector: `.meet-the-shop`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1376 x 797.33 |
| Padding | 40px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Averta 16px/24px 400 |
| Letter spacing | normal |
| Colour | #303538 |
| Text node | h2.shop-name: Averta 32px/40px 600, #303538 |
| Transition | none |
| Icon | 16 x 16, colour #303538 |
| Painted layers | div.meet-the-shop__profile 1376.0x797.3 bg #ffffff r 16px; div.featured-shop-badge 127.0x32.0 bg #f4f8fb r 18px; button 232.0x35.0 bg #ffffff border T:1px solid #e2e9ee / R:1px solid #e2e9ee / B:1px solid #e2e9ee / L:1px solid #e2e9ee r 24px; button 232.0x35.0 bg #ffffff border T:1px solid #e2e9ee / R:1px solid #e2e9ee / B:1px solid #e2e9ee / L:1px solid #e2e9ee r 24px; div.shop-stats 1296.0x114.0 border T:1px solid #e2e9ee / B:1px solid #e2e9ee; a 416.0x277.3 bg #edf2f5 r 8px |
| How | at rest |

Crops: `shop-card-default.png`.

#### related-card

Related product card. A card in "More from this shop"/"Similar Fonts"; measured, never followed. The rails rendered empty on this capture — recorded as a miss if absent.

Page: product. Selector: `related card`. States: .

Not found on the page at capture time.

### Search

#### search-h1

Search heading. The results heading for ?q=font.

Page: search. Selector: `results h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1376 x 70.38 |
| Padding | 7.2px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Averta 48px/56px 600 |
| Letter spacing | normal |
| Colour | #303538 |
| Transition | none |
| How | at rest |

Crops: `search-h1-default.png`.

#### result-card

Result card. A results-grid card; measured, never followed.

Page: search. Selector: `result card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 320 x 213.33 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Averta 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #303538 | = | - | = |
| Text node | span.product-thumbnail-badge__text: Averta 14px/14px 400, #303538 | span.product-thumbnail-badge__text: Averta 14px/14px 400, #003a37 | - | = |
| Transition | none | = | - | = |
| Icon | 16 x 16, colour #303538 | = | - | = |
| Painted layers | a 320.0x213.3 bg #edf2f5; div.product-thumbnail-badge 143.4x28.0 bg #ffffff border T:1px solid #edf2f5 / R:1px solid #edf2f5 / B:1px solid #edf2f5 / L:1px solid #edf2f5 r 0px 18px 0px 0px; button.like-button.product-thumbnail__like-button 30.0x30.0 bg #ffffff @ 0.9 r 3.35544e+07px shadow #000000 @ 0.1 0px 1px 8px 0px, #000000 @ 0.05 0px 0px 1px 1px, #ffffff 0px 1px 1px 0px inset, #ffffff @ 0.25 0px -1px 0px 0px inset; button.sp-button.product-card-add-to-cart 0.0x0.0 bg #088178 border T:2px solid #088178 / R:2px solid #088178 / B:2px solid #088178 / L:2px solid #088178 | a 320.0x213.3 bg #edf2f5; div.product-thumbnail__font-preview 320.0x213.3 bg #ffffff; div.product-thumbnail-badge 143.4x28.0 bg #ffffff border T:1px solid #edf2f5 / R:1px solid #edf2f5 / B:1px solid #edf2f5 / L:1px solid #edf2f5 r 0px 18px 0px 0px; button.like-button.product-thumbnail__like-button 30.0x30.0 bg #ffffff @ 0.9 r 3.35544e+07px shadow #000000 @ 0.1 0px 1px 8px 0px, #000000 @ 0.05 0px 0px 1px 1px, #ffffff 0px 1px 1px 0px inset, #ffffff @ 0.25 0px -1px 0px 0px inset; button.sp-button.product-card-add-to-cart 320.0x44.0 bg #088178 border T:2px solid #088178 / R:2px solid #088178 / B:2px solid #088178 / L:2px solid #088178 | - | a 320.0x213.3 bg #edf2f5; div.product-thumbnail__font-preview 320.0x213.3 bg #ffffff; div.product-thumbnail-badge 143.4x28.0 bg #ffffff border T:1px solid #edf2f5 / R:1px solid #edf2f5 / B:1px solid #edf2f5 / L:1px solid #edf2f5 r 0px 18px 0px 0px; button.like-button.product-thumbnail__like-button 30.0x30.0 bg #ffffff @ 0.9 r 3.35544e+07px shadow #000000 @ 0.1 0px 1px 8px 0px, #000000 @ 0.05 0px 0px 1px 1px, #ffffff 0px 1px 1px 0px inset, #ffffff @ 0.25 0px -1px 0px 0px inset; button.sp-button.product-card-add-to-cart 320.0x44.0 bg #088178 border T:2px solid #088178 / R:2px solid #088178 / B:2px solid #088178 / L:2px solid #088178 |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `result-card-default.png`, `result-card-hover.png`, `result-card-pressed.png`.

### Membership

#### membership-h1

Membership headline. The membership page heading.

Page: membership. Selector: `membership h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 730 x 160 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Brule 72px/80px 600 |
| Letter spacing | normal |
| Colour | #4e42a1 |
| Transition | none |
| How | at rest |

Crops: `membership-h1-default.png`.

#### plan-card

Plan card. A membership plan card (name, price, benefits, CTA); measured, never purchased.

Page: membership. Selector: `plan card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 274 x 323 | = | - | = |
| Padding | 30px | = | - | = |
| Border | none | = | - | = |
| Radius | 16px | = | - | = |
| Background | #ffffff | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Averta 16px/28px 700 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #303538 | = | - | = |
| Text node | h3.pricing-tier__title: Averta 16px/28px 700, #6e777d | = | - | = |
| Transition | none | = | - | = |
| Painted layers | div.pricing-tier 274.0x323.0 bg #ffffff r 16px; hr.pricing-tier__hr 214.0x1.0 bg #edf2f5; button.btn.btn--tertiary-alternative 214.0x45.0 bg #edeeff border T:2px solid #edeeff / R:2px solid #edeeff / B:2px solid #edeeff / L:2px solid #edeeff r 8px; button::before.btn.btn--tertiary-alternative 336pxx336px bg #4e42a1 r 3.35544e+07px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `plan-card-default.png`, `plan-card-hover.png`, `plan-card-pressed.png`.

### Sign-in

#### signin-h1

Sign-in headline. "Welcome back to the world's marketplace for design".

Page: signin. Selector: `sign-in heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 673 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Averta 36px/48px 600 |
| Letter spacing | normal |
| Colour | #303538 |
| Transition | none |
| How | at rest |

Crops: `signin-h1-default.png`.

#### username-field

Username field. The username text field; filled with a placeholder, never submitted.

Page: signin. Selector: `input[name=username]`. States: default, focus-visible, filled.

| Property | default | focus-visible | filled |
|---|---|---|---|
| Size (w x h) | 436.66 x 43 | = | = |
| Padding | 0px 16px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Averta 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #303538 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #303538, opacity 1 | = | = |
| Ancestor paint | 1 up div.ui-text-field.ui-text-field--md bg #ffffff shadow #000000 @ 0 0px 0px 0px 3px | 1 up div.ui-text-field.ui-text-field--md bg #ffffff shadow #b6e7e4 0px 0px 0px 3px | 1 up div.ui-text-field.ui-text-field--md bg #ffffff shadow #b6e7e4 0px 0px 0px 3px |
| How | at rest | Shift+Tab, Tab | typed "name@example.com", then deleted; nothing sent |

Crops: `username-field-default.png`, `username-field-focus-visible.png`, `username-field-filled.png`.

#### password-field

Password field. The password field; never filled, never submitted.

Page: signin. Selector: `input[type=password]`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 392.66 x 43 | = |
| Padding | 0px 0px 0px 16px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Averta 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #303538 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #303538, opacity 1 | = |
| Ancestor paint | 1 up div.ui-text-field.ui-text-field--md bg #ffffff shadow #000000 @ 0 0px 0px 0px 3px | 1 up div.ui-text-field.ui-text-field--md bg #ffffff shadow #b6e7e4 0px 0px 0px 3px |
| How | at rest | Shift+Tab, Tab |

Crops: `password-field-default.png`, `password-field-focus-visible.png`.

#### remember-check

Checkbox. A sign-in checkbox (remember me); never toggled.

Page: signin. Selector: `input[type=checkbox]`. States: .

Not found on the page at capture time.

#### login-btn

Log In button. The sign-in submit; measured only — pressing it would post credentials.

Page: signin. Selector: `Log In button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 438.66 x 51 | = | = | = |
| Padding | 12px 30px | = | = | = |
| Border | 2px solid #088178 | 2px solid #003a37 | = | 2px solid #003a37 |
| Radius | 3px | = | = | = |
| Background | #088178 | #003a37 | = | #003a37 |
| Box shadow | none | = | #b6e7e4 @ 0.45 0px 0px 0px 5px | = |
| Outline | none | = | = | = |
| Font | Averta 18px/normal 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.25s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.sp-button.sp-button--primary 438.7x51.0 bg #088178 border T:2px solid #088178 / R:2px solid #088178 / B:2px solid #088178 / L:2px solid #088178 r 3px | button.sp-button.sp-button--primary 438.7x51.0 bg #003a37 border T:2px solid #003a37 / R:2px solid #003a37 / B:2px solid #003a37 / L:2px solid #003a37 r 3px | button.sp-button.sp-button--primary 438.7x51.0 bg #088178 border T:2px solid #088178 / R:2px solid #088178 / B:2px solid #088178 / L:2px solid #088178 r 3px shadow #b6e7e4 @ 0.45 0px 0px 0px 5px | button.sp-button.sp-button--primary 438.7x51.0 bg #003a37 border T:2px solid #003a37 / R:2px solid #003a37 / B:2px solid #003a37 / L:2px solid #003a37 r 3px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-btn-default.png`, `login-btn-hover.png`, `login-btn-focus-visible.png`, `login-btn-pressed.png`.

#### sso-btn

Google SSO. "Log In Using Google"; measured, OAuth never followed.

Page: signin. Selector: `Google SSO button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 438.66 x 51 | = | = | = |
| Padding | 12px 30px | = | = | = |
| Border | 2px solid #303538 | = | = | = |
| Radius | 3px | = | = | = |
| Background | #ffffff | #303538 @ 0.1 | = | #303538 @ 0.1 |
| Box shadow | none | = | #b6e7e4 @ 0.45 0px 0px 0px 5px | = |
| Outline | none | = | = | = |
| Font | Averta 18px/normal 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #303538 | = | = | = |
| Transition | all 0.25s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.sp-button.google 438.7x51.0 bg #ffffff border T:2px solid #303538 / R:2px solid #303538 / B:2px solid #303538 / L:2px solid #303538 r 3px | button.sp-button.google 438.7x51.0 bg #303538 @ 0.1 border T:2px solid #303538 / R:2px solid #303538 / B:2px solid #303538 / L:2px solid #303538 r 3px | button.sp-button.google 438.7x51.0 bg #ffffff border T:2px solid #303538 / R:2px solid #303538 / B:2px solid #303538 / L:2px solid #303538 r 3px shadow #b6e7e4 @ 0.45 0px 0px 0px 5px | button.sp-button.google 438.7x51.0 bg #303538 @ 0.1 border T:2px solid #303538 / R:2px solid #303538 / B:2px solid #303538 / L:2px solid #303538 r 3px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sso-btn-default.png`, `sso-btn-hover.png`, `sso-btn-focus-visible.png`, `sso-btn-pressed.png`.

### Footer

#### footer

Footer. The footer: the logo/about column plus the five link sections (c-site-footer__main, 1376x322).

Page: home. Selector: `.c-site-footer__main`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 488.5 |
| Padding | 48px 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Averta 16px/24px 400 |
| Letter spacing | normal |
| Colour | #303538 |
| Text node | p: Averta 14px/22px 400, #303538 |
| Transition | none |
| Icon | 99.98 x 39.47, colour #303538, fill #000000 |
| Ancestor paint | 1 up div bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer link; measured, never followed.

Page: home. Selector: `footer nav a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 169.16 x 19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #e06868 offset 1px | = |
| Font | Averta 15px/37.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #303538 | #003a37 | = | #003a37 |
| Transition | color 0.25s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 169.2x19.0 outline 2px solid #e06868 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-icon

Social link. A social icon in the about column.

Page: home. Selector: `footer socials a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 20 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #e06868 offset 1px | = |
| Font | Averta 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | all 0.2s ease-in-out | = | = | = |
| Opacity | 0.7 | - | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #303538, fill #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 20.0x20.0 outline 2px solid #e06868 offset 1px | = |

Crops: `social-icon-default.png`, `social-icon-hover.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 119 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Averta 14px/21px 400 |
| Letter spacing | normal |
| Colour | #303538 |
| Text node | span.badge.badge--green: Averta 10px/8px 600, #ffffff, ls 0.5px |
| Transition | none |
| Icon | 18 x 19, colour #088178 |
| Painted layers | div.site-header-wrapper 390.0x119.0 bg #ffffff; button.ui-button.ui-button--ghost 45.0x45.0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 3.35544e+07px; input.search-field__input 0.0x0.0 bg #fafdff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 100px; div::before.search-field__category 1pxx24px bg #899298; div.multiselect__tags 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 3px; div.multiselect__content-wrapper 0.0x0.0 bg #ffffff border T:1px solid #edf2f5 / R:1px solid #edf2f5 / B:1px solid #edf2f5 / L:1px solid #edf2f5 r 8px shadow #000000 @ 0.15 0px 0px 8px 0px |
| Ancestor paint | 1 up div bg #ffffff |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The header menu button that opens the nav overlay.

Page: home. Selector: `header menu button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 45 x 45 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 2px solid #000000 @ 0 | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #088178 offset 2px | = |
| Font | Averta 14px/14px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #088178 | = | = | = |
| Transition | color, background-color, border-color 0.2s cubic-bezier(0.32, 0, 0.59, 0.03) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 19, colour #088178 | = | = | = |
| Painted layers | button.ui-button.ui-button--ghost 45.0x45.0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 3.35544e+07px | = | button.ui-button.ui-button--ghost 45.0x45.0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 3.35544e+07px outline 2px solid #088178 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The opened nav overlay (.mobile-menu).

Page: home. Selector: `opened mobile menu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 295.5 x 844 |
| Padding | 32px 24px 48px 24px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Averta 14px/21px 400 |
| Letter spacing | normal |
| Colour | #303538 |
| Text node | span: Averta 14px/22px 600, #303538 |
| Transition | all 0.4s cubic-bezier(0.25, 1, 0.5, 1) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 18 x 18, colour #088178, fill #000000 |
| Painted layers | div.mobile-menu.mobile-nav__mobile-menu 295.5x844.0 bg #ffffff; button.mobile-menu-header__button.mobile-menu-header__button--close-btn 45.0x45.0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px; button::before.mobile-menu-header__button.mobile-menu-header__button--close-btn 65.5938pxx65.5938px bg #dff8f6 r 3.35544e+07px; nav::after.mobile-nav-categories 271.5pxx30px image linear-gradient(#ffffff @ 0, #ffffff); ul.item.item--has-divider 247.5x116.0 border T:1px solid #edf2f5 / B:1px solid #edf2f5; a.pill.pill--tertiary 54.5x34.0 bg #ffeaf6 border T:1px solid #ffeaf6 / R:1px solid #ffeaf6 / B:1px solid #ffeaf6 / L:1px solid #ffeaf6 r 190px |
| Ancestor paint | 1 up div.mobile-nav.mobile-nav--mobile-menu-open bg #ffffff |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile menu row. A row inside the opened nav overlay.

Page: home. Selector: `mobile menu row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40.73 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #e06868 offset 1px | = |
| Font | Averta 14px/21px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #303538 | #003a37 | = | #003a37 |
| Transition | color 0.25s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 40.7x18.0 outline 2px solid #e06868 offset 1px | = |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-heading

Mobile heading.

Page: home. Selector: `painted heading at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 283.83 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Averta 20px/24px 600 |
| Letter spacing | normal |
| Colour | #303538 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `m-heading-default.png`.

#### m-search

Mobile search. The mobile search bar; never submitted.

Page: home. Selector: `mobile search-field`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 358 x 46 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Averta 15px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #303538 | = | = | = |
| Text node | span.ui-select__single-label: Averta 14px/20px 600, #303538 | = | = | = |
| Transition | none | = | = | = |
| Icon | 16 x 16, colour #899298, fill #000000 | = | = | = |
| Painted layers | input.search-field__input 358.0x46.0 bg #fafdff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 100px; div::before.search-field__category 1pxx24px bg #899298; div.multiselect__tags 120.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 3px; div.multiselect__content-wrapper 0.0x0.0 bg #ffffff border T:1px solid #edf2f5 / R:1px solid #edf2f5 / B:1px solid #edf2f5 / L:1px solid #edf2f5 r 8px shadow #000000 @ 0.15 0px 0px 8px 0px; span.multiselect__option.multiselect__option--highlight 0.0x0.0 bg #edf2f5; div.search-dropdown 0.0x0.0 bg #ffffff r 24px shadow #000000 @ 0.15 0px 0px 8px 0px | input.search-field__input 358.0x46.0 bg #fafdff border T:1px solid #ccd4da / R:1px solid #ccd4da / B:1px solid #ccd4da / L:1px solid #ccd4da r 100px; div::before.search-field__category 1pxx24px bg #899298; div.multiselect__tags 120.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 3px; div.multiselect__content-wrapper 0.0x0.0 bg #ffffff border T:1px solid #edf2f5 / R:1px solid #edf2f5 / B:1px solid #edf2f5 / L:1px solid #edf2f5 r 8px shadow #000000 @ 0.15 0px 0px 8px 0px; span.multiselect__option.multiselect__option--highlight 0.0x0.0 bg #edf2f5; div.search-dropdown 0.0x0.0 bg #ffffff r 24px shadow #000000 @ 0.15 0px 0px 8px 0px | input.search-field__input 358.0x46.0 bg #fafdff border T:1px solid #ccd4da / R:1px solid #ccd4da / B:1px solid #ccd4da / L:1px solid #ccd4da r 100px; div::before.search-field__category 1pxx24px bg #899298; div.multiselect__tags 120.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 3px; div.multiselect__content-wrapper 0.0x0.0 bg #ffffff border T:1px solid #edf2f5 / R:1px solid #edf2f5 / B:1px solid #edf2f5 / L:1px solid #edf2f5 r 8px shadow #000000 @ 0.15 0px 0px 8px 0px; span.multiselect__option.multiselect__option--highlight 0.0x0.0 bg #edf2f5; div.search-dropdown 0.0x0.0 bg #ffffff r 24px shadow #000000 @ 0.15 0px 0px 8px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-search-default.png`, `m-search-hover.png`, `m-search-focus-visible.png`, `m-search-pressed.png`.

## Transitions declared in the readable stylesheets

creativemarket.com serves its Sass sheets from the cross-origin d3ui957tjb5bqd.cloudfront.net CDN, so the CSSOM lists only the page's own rules; the per-state Transition rows above are the computed values the page paints.

- category: `1s`, `all`, `0.2s ease-in-out`, `0.4s`

- home: `1s`, `all`, `0.2s ease-in-out`, `0.4s`

- product: `1s`, `all`, `0.2s ease-in-out`, `0.4s`
