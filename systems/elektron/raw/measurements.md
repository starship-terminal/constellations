# Elektron component measurements

Computed styles read from elektron.se on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the home page, /shop, the Digitakt II and PL-2 product pages, /explore, /support-downloads, /who-we-are, /contact-us, the empty /cart drawer, the signed-out /my-account magic-login card and /store-locator — with the #thedock-cookie-banner consent modal hidden (never answered) — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). The site paints one dark theme. One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The 56px transparent top bar over the page: Catalog / Shop / Kulture / Search on the left, the Elektron mark centre, Support / Account / Cart on the right — Neue Haas Grotesk Text 14px labels with small icons.

Page: home. Selector: `.header-section-wrapper.is-main-menu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Text Pro 14px/21px 400 |
| Letter spacing | 0.462px |
| Colour | #eeeef2 |
| Text node | span: Neue Haas Grotesk Text Pro 14px/21px 400, #eeeef2, ls 0.462px |
| Transition | color, background-color, transform, -webkit-transform 0.4s, 0.4s, 0.4s, 0.4s cubic-bezier(0.365, 0.305, 0, 1), cubic-bezier(0.365, 0.305, 0, 1), cubic-bezier(0.365, 0.305, 0, 1), cubic-bezier(0.365, 0.305, 0, 1) delay 0s, 0s, 0s, 0s |
| Icon | 28 x 28, colour #eeeef2 |
| Painted layers | div.element-background.has-center-center-position 1440.0x56.0 bg #151515; span 54.3x21.0 image linear-gradient(to right, #333333 0%, #333333 100%); span 35.9x21.0 image linear-gradient(to right, #333333 0%, #333333 100%); span 50.1x21.0 image linear-gradient(to right, #333333 0%, #333333 100%); span 49.3x21.0 image linear-gradient(to right, #333333 0%, #333333 100%); span 55.8x21.0 image linear-gradient(to right, #333333 0%, #333333 100%) |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Elektron wordmark anchor at the centre of the header.

Page: home. Selector: `header logo anchor`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 35 x 24.86 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Text Pro 14px/21px 400 |
| Letter spacing | 0.462px |
| Colour | #eeeef2 |
| Transition | none |
| Cursor | pointer |
| Icon | 35 x 24.86, colour #eeeef2 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link. A header destination anchor (Catalog / Shop / Kulture): a .block-button.button-small_text row 28px tall, icon left of a 14px label. Measured, never followed.

Page: home. Selector: `header .block-button.button-small_text`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 70.92 x 28 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 7px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | Neue Haas Grotesk Text Pro 14px/21px 400 | = | = | = |
| Letter spacing | 0.462px | = | = | = |
| Colour | #eeeef2 | = | = | = |
| Text node | span: Neue Haas Grotesk Text Pro 14px/21px 400, #eeeef2, ls 0.462px | = | = | = |
| Transition | border, background-color, background-position, background-size, background-image, opacity 0.3s, 0.3s, 0.3s, 0.3s, 0.5s, 0.3s ease, ease, ease, ease, ease, ease delay 0s, 0s, 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 28 x 28, colour #eeeef2 | = | = | = |
| Painted layers | span 35.9x21.0 image linear-gradient(to right, #333333 0%, #333333 100%) | = | a.block-button.button-small_text 70.9x28.0 shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px; span 35.9x21.0 image linear-gradient(to right, #333333 0%, #333333 100%) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-icon-link

Nav icon link. A right-side header action (Support / Account / Cart): label left of a small icon. Cart opens the mini-cart drawer — measured, never followed to checkout.

Page: home. Selector: `header Cart anchor`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 65.53 x 28 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 7px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | Neue Haas Grotesk Text Pro 14px/21px 400 | = | = | = |
| Letter spacing | 0.462px | = | = | = |
| Colour | #eeeef2 | = | = | = |
| Text node | span: Neue Haas Grotesk Text Pro 14px/21px 400, #eeeef2, ls 0.462px | = | = | = |
| Transition | border, background-color, background-position, background-size, background-image, opacity 0.3s, 0.3s, 0.3s, 0.3s, 0.5s, 0.3s ease, ease, ease, ease, ease, ease delay 0s, 0s, 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 28 x 28, colour #eeeef2 | = | = | = |
| Painted layers | span 30.5x21.0 image linear-gradient(to right, #333333 0%, #333333 100%); span.num-cart-items 0.0x0.0 image linear-gradient(to right, #333333 0%, #333333 100%) | = | a.block-button.button-small_text 65.5x28.0 shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px; span 30.5x21.0 image linear-gradient(to right, #333333 0%, #333333 100%); span.num-cart-items 0.0x0.0 image linear-gradient(to right, #333333 0%, #333333 100%) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-icon-link-default.png`, `nav-icon-link-hover.png`, `nav-icon-link-focus-visible.png`, `nav-icon-link-pressed.png`.

### Dialogs and overlays

#### search-modal

Search dropdown. The header Search dropdown: a large search-field row under the header.

Page: home. Selector: `opened Search modal`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 1440 x 6785.33 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Text Pro 14px/21px 400 |
| Letter spacing | 0.462px |
| Colour | #eeeef2 |
| Text node | span: Neue Haas Grotesk Text Pro 14px/21px 400, #eeeef2, ls 0.462px |
| Transition | none |
| Icon | 28 x 28, colour #eeeef2 |
| Painted layers | div.element-background.has-center-center-position 1440.0x56.0 bg #151515; span 54.3x21.0 image linear-gradient(to right, #333333 0%, #333333 100%); span 35.9x21.0 image linear-gradient(to right, #333333 0%, #333333 100%); span 50.1x21.0 image linear-gradient(to right, #333333 0%, #333333 100%); span 49.3x21.0 image linear-gradient(to right, #333333 0%, #333333 100%); span 55.8x21.0 image linear-gradient(to right, #333333 0%, #333333 100%) |
| Ancestor paint | 1 up body.home.wp-singular bg #151515 |
| How | held open by an earlier toggle |

Crops: `search-modal-opened.png`.

#### search-field

Search field. The big search input inside the Search dropdown ("Type and press enter to search"). Sample text was typed and deleted; the query was never submitted.

Page: home. Selector: `search modal input.search-field`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 1440 x 40.5 | = | = |
| Padding | 10.5px 17.5px | = | = |
| Border | 1px solid #151515 | = | = |
| Radius | 7px | = | = |
| Background | #151515 | = | = |
| Box shadow | none | #ffffff 0px 0px 0px 2px | #ffffff 0px 0px 0px 2px |
| Outline | none | 2px solid #000000 offset 2px | 2px solid #000000 offset 2px |
| Font | Analog One V2. 14px/17.5px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #eeeef2 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| Painted layers | input.search-field.has-large-top-padding 1440.0x40.5 bg #151515 border T:1px solid #151515 / R:1px solid #151515 / B:1px solid #151515 / L:1px solid #151515 r 7px | input.search-field.has-large-top-padding 1440.0x40.5 bg #151515 border T:1px solid #151515 / R:1px solid #151515 / B:1px solid #151515 / L:1px solid #151515 r 7px shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px | input.search-field.has-large-top-padding 1440.0x40.5 bg #151515 border T:1px solid #151515 / R:1px solid #151515 / B:1px solid #151515 / L:1px solid #151515 r 7px shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px |
| How | at rest | clicked into the field | typed "digitakt", then deleted; nothing sent |

Crops: `search-field-default.png`, `search-field-focused.png`, `search-field-filled.png`.

#### account-modal

Account drawer. The header Account modal (modal-layout-drawer-right): the magic-login panel — a Log in step (Email field, Send me a code) and Create New Account. Measured, never used.

Page: home. Selector: `opened Account modal`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 1440 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Text Pro 14px/21px 400 |
| Letter spacing | 0.462px |
| Colour | #eeeef2 |
| Text node | h2.wp-block-heading.has-medium-font-size: Neue Haas Grotesk Text Pro 17.99px/26.985px 400, #eeeef2, ls 0.7196px |
| Transition | none |
| Icon | 35 x 35, colour #eeeef2 |
| Painted layers | div.element-background.has-center-center-position 1440.0x844.0 bg #151515; div.element-background.has-center-center-position 420.0x844.0 bg #212121; hr.wp-block-separator.thickness-normal 392.0x2.0 bg #808080; input.block-input.button-full_form 0.0x0.0 bg #eeeef2; input.block-input.button-full_form 0.0x0.0 bg #eeeef2; input.block-input.has-undefined-background-color 0.0x0.0 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff |
| How | held open by an earlier toggle |

Crops: `account-modal-opened.png`.

#### magic-email

Magic-login email field. The Email input of the magic-login drawer: a 42px block-input field. Sample text was typed and deleted; no code was ever requested.

Page: home. Selector: `account drawer email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 392 x 42 | = | = |
| Padding | 10.5px 44px 10.5px 17.5px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | #eeeef2 | #151515 | #151515 |
| Box shadow | none | #ffffff 0px 0px 0px 2px | #ffffff 0px 0px 0px 2px |
| Outline | none | 2px solid #000000 offset 2px | 2px solid #000000 offset 2px |
| Font | digi one v2 14px/21px 400 | = | = |
| Letter spacing | 0.462px | = | = |
| Colour | #151515 | #eeeef2 | #eeeef2 |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| Painted layers | input.block-input.button-full_form 392.0x42.0 bg #eeeef2 | input.block-input.button-full_form 392.0x42.0 bg #151515 shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px | input.block-input.button-full_form 392.0x42.0 bg #151515 shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `magic-email-default.png`, `magic-email-focused.png`, `magic-email-filled.png`.

#### magic-send

Send me a code button. The magic-login submit: a full-width secondary-variant block-button (grey fill, dark label, digi one v2). Measured, never pressed.

Page: home. Selector: `account drawer Send me a code`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 392 x 42 | = | = | = |
| Padding | 10.5px 17.5px | = | = | = |
| Gap | 7px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #cccccc | #151515 | #151515 | #151515 |
| Background image | linear-gradient(to right, #333333 0%, #333333 100%) | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px | #ffffff 0px 0px 0px 2px |
| Outline | none | = | 2px solid #000000 offset 2px | 2px solid #000000 offset 2px |
| Font | digi one v2 14px/21px 400 | = | = | = |
| Letter spacing | 0.462px | = | = | = |
| Colour | #151515 | #cccccc | #cccccc | #cccccc |
| Text node | span: digi one v2 14px/21px 400, #151515, ls 0.462px | span: digi one v2 14px/21px 400, #cccccc, ls 0.462px | span: digi one v2 14px/21px 400, #cccccc, ls 0.462px | span: digi one v2 14px/21px 400, #cccccc, ls 0.462px |
| Transition | background-size 0.4s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.block-button.button-full 392.0x42.0 bg #cccccc image linear-gradient(to right, #333333 0%, #333333 100%) | button.block-button.button-full 392.0x42.0 bg #151515 image linear-gradient(to right, #333333 0%, #333333 100%) | button.block-button.button-full 392.0x42.0 bg #151515 image linear-gradient(to right, #333333 0%, #333333 100%) shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px | button.block-button.button-full 392.0x42.0 bg #151515 image linear-gradient(to right, #333333 0%, #333333 100%) shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `magic-send-default.png`, `magic-send-hover.png`, `magic-send-focus-visible.png`, `magic-send-pressed.png`.

### About

#### hero-h1

Page title. The home page heading.

Page: home. Selector: `first h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 284.63 x 40.95 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Display Pro 30.8px/40.964px 400 |
| Letter spacing | 1.232px |
| Colour | #eeeef2 |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### section-h2

Section heading. A section heading below the fold.

Page: home. Selector: `first h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 749 x 60.84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Display Pro 64.05px/60.8475px 500 |
| Letter spacing | -0.6405px |
| Colour | #eeeef2 |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

#### about-title

About title.

Page: about. Selector: `who-we-are heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 128.94 x 31.94 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Display Pro 24.01px/31.9333px 400 |
| Letter spacing | 0.9604px |
| Colour | #eeeef2 |
| Transition | none |
| How | at rest |

Crops: `about-title-default.png`.

### Shop

#### product-card

Product card. A shop-grid product block: product name (18px Neue Haas Text), a one-line descriptor and the price in $. Measured, never followed.

Page: shop. Selector: `shop product group-content`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 691.31 x 26.97 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Neue Haas Grotesk Text Pro 14px/21px 400 | = | - | = |
| Letter spacing | 0.462px | = | - | = |
| Colour | #eeeef2 | = | - | = |
| Text node | h2.wp-block-heading.has-medium-font-size: Neue Haas Grotesk Text Pro 17.99px/26.985px 400, #eeeef2, ls 0.7196px | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `product-card-default.png`, `product-card-hover.png`, `product-card-pressed.png`.

#### product-card-title

Product card title.

Page: shop. Selector: `shop product h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 84.55 x 26.97 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Text Pro 17.99px/26.985px 400 |
| Letter spacing | 0.7196px |
| Colour | #eeeef2 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `product-card-title-default.png`.

#### product-card-sub

Product card subtitle.

Page: shop. Selector: `shop product descriptor`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 261.42 x 21 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Text Pro 14px/21px 400 |
| Letter spacing | 0.462px |
| Colour | #eeeef2 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `product-card-sub-default.png`.

#### price

Price. A product price figure ("349 $").

Page: shop. Selector: `.price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 57.52 x 26.97 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Text Pro 17.99px/26.985px 400 |
| Letter spacing | 0.7196px |
| Colour | #eeeef2 |
| Text node | bdi: Neue Haas Grotesk Text Pro 17.99px/26.985px 400, #eeeef2, ls 0.7196px |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `price-default.png`.

### Product pages

#### pdp-title

Product title. The product name on the detail page, 18px Neue Haas Text.

Page: product-digitakt. Selector: `product h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 86.38 x 26.97 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Text Pro 17.99px/26.985px 400 |
| Letter spacing | 0.7196px |
| Colour | #eeeef2 |
| Transition | none |
| How | at rest |

Crops: `pdp-title-default.png`.

#### pdp-price

Product price. The product price figure ("1149 $").

Page: product-digitakt. Selector: `product .price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 56.89 x 26.97 |
| Padding | 0px |
| Gap | 8.995px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Text Pro 17.99px/26.985px 400 |
| Letter spacing | 0.7196px |
| Colour | #eeeef2 |
| Text node | bdi: Neue Haas Grotesk Text Pro 17.99px/26.985px 400, #eeeef2, ls 0.7196px |
| Transition | none |
| How | at rest |

Crops: `pdp-price-default.png`.

#### pdp-explore

Explore button. The full-width outline action on the product page (EXPLORE DIGITAKT II): a .block-button.button-outline, 2px #eeeef2 border, transparent fill, digi one v2 14px caps at 46px tall. Measured, never followed.

Page: product-digitakt. Selector: `.block-button.button-outline EXPLORE`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 461.33 x 46 | = | = | = |
| Padding | 10.5px 17.5px | = | = | = |
| Gap | 7px | = | = | = |
| Border | 2px solid #eeeef2 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #eeeef2 | = | #eeeef2 |
| Background image | linear-gradient(to right, #333333 0%, #333333 100%) | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | digi one v2 14px/21px 400 | = | = | = |
| Letter spacing | 0.462px | = | = | = |
| Colour | #eeeef2 | #151515 | = | #151515 |
| Text node | span: digi one v2 14px/21px 400, #eeeef2, ls 0.462px | span: digi one v2 14px/21px 400, #151515, ls 0.462px | = | span: digi one v2 14px/21px 400, #151515, ls 0.462px |
| Transition | background-size 0.4s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.block-button.button-outline 461.3x46.0 image linear-gradient(to right, #333333 0%, #333333 100%) border T:2px solid #eeeef2 / R:2px solid #eeeef2 / B:2px solid #eeeef2 / L:2px solid #eeeef2 | a.block-button.button-outline 461.3x46.0 bg #eeeef2 image linear-gradient(to right, #333333 0%, #333333 100%) border T:2px solid #eeeef2 / R:2px solid #eeeef2 / B:2px solid #eeeef2 / L:2px solid #eeeef2 | a.block-button.button-outline 461.3x46.0 image linear-gradient(to right, #333333 0%, #333333 100%) border T:2px solid #eeeef2 / R:2px solid #eeeef2 / B:2px solid #eeeef2 / L:2px solid #eeeef2 shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px | a.block-button.button-outline 461.3x46.0 bg #eeeef2 image linear-gradient(to right, #333333 0%, #333333 100%) border T:2px solid #eeeef2 / R:2px solid #eeeef2 / B:2px solid #eeeef2 / L:2px solid #eeeef2 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pdp-explore-default.png`, `pdp-explore-hover.png`, `pdp-explore-focus-visible.png`, `pdp-explore-pressed.png`.

#### accordion

Key Features accordion. A 24px Neue Haas Grotesk Display block row with a right icon that expands the feature section — a local UI toggle.

Page: product-digitakt. Selector: `.block-button Key Features`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 461.33 x 37.81 | = | - | = | = |
| Padding | 0px | = | - | = | = |
| Gap | 12.005px | = | - | = | = |
| Border | none | = | - | = | = |
| Radius | 0px | = | - | = | = |
| Background | transparent | = | - | = | = |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | Neue Haas Grotesk Display Pro 24.01px/36.015px 450 | = | - | = | = |
| Letter spacing | 0.9604px | = | - | = | = |
| Colour | #eeeef2 | = | - | = | = |
| Text node | span: Neue Haas Grotesk Display Pro 24.01px/36.015px 450, #eeeef2, ls 0.9604px | = | - | = | = |
| Transition | border, background-color, background-position, background-size, background-image, opacity 0.3s, 0.3s, 0.3s, 0.3s, 0.5s, 0.3s ease, ease, ease, ease, ease, ease delay 0s, 0s, 0s, 0s, 0s, 0s | = | - | = | = |
| Cursor | pointer | = | - | = | = |
| Painted layers | span 146.6x36.0 image linear-gradient(to right, #333333 0%, #333333 100%) | = | - | = | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | own toggle |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `accordion-default.png`, `accordion-hover.png`, `accordion-pressed.png`, `accordion-opened.png`.

#### pdp-title-accessory

Product title (accessory).

Page: product-accessory. Selector: `product h1 on /product/pl-2-protective-lid`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 173.94 x 26.97 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Text Pro 17.99px/26.985px 400 |
| Letter spacing | 0.7196px |
| Colour | #eeeef2 |
| Transition | none |
| How | at rest |

Crops: `pdp-title-accessory-default.png`.

#### add-to-cart

Add to cart button. The in-stock product action: a 2px #eeeef2 outline block-button, digi one v2 14px caps, 46px tall. Measured, never pressed — nothing was added to the cart.

Page: product-accessory. Selector: `.single_add_to_cart_button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 244.67 x 46 | = | = | = |
| Padding | 10.5px 17.5px | = | = | = |
| Gap | 7px | = | = | = |
| Border | 2px solid #eeeef2 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #eeeef2 | = | #eeeef2 |
| Background image | linear-gradient(to right, #333333 0%, #333333 100%) | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | digi one v2 14px/21px 400 | = | = | = |
| Letter spacing | 0.462px | = | = | = |
| Colour | #eeeef2 | #151515 | = | #151515 |
| Transition | background-size 0.4s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.single_add_to_cart_button.block-button 244.7x46.0 image linear-gradient(to right, #333333 0%, #333333 100%) border T:2px solid #eeeef2 / R:2px solid #eeeef2 / B:2px solid #eeeef2 / L:2px solid #eeeef2 | button.single_add_to_cart_button.block-button 244.7x46.0 bg #eeeef2 image linear-gradient(to right, #333333 0%, #333333 100%) border T:2px solid #eeeef2 / R:2px solid #eeeef2 / B:2px solid #eeeef2 / L:2px solid #eeeef2 | button.single_add_to_cart_button.block-button 244.7x46.0 image linear-gradient(to right, #333333 0%, #333333 100%) border T:2px solid #eeeef2 / R:2px solid #eeeef2 / B:2px solid #eeeef2 / L:2px solid #eeeef2 shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px | button.single_add_to_cart_button.block-button 244.7x46.0 bg #eeeef2 image linear-gradient(to right, #333333 0%, #333333 100%) border T:2px solid #eeeef2 / R:2px solid #eeeef2 / B:2px solid #eeeef2 / L:2px solid #eeeef2 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `add-to-cart-default.png`, `add-to-cart-hover.png`, `add-to-cart-focus-visible.png`, `add-to-cart-pressed.png`.

### Explore

#### explore-title

Explore title.

Page: explore. Selector: `first h1 on /explore`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 219.03 x 42.16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Display Pro 44.3912px/42.1716px 500 |
| Letter spacing | -0.443912px |
| Colour | #eeeef2 |
| Text node | a: Neue Haas Grotesk Display Pro 44.3912px/42.1716px 500, #eeeef2, ls -0.443912px |
| Transition | none |
| Painted layers | a 223.5x53.0 image linear-gradient(to right, #333333 0%, #333333 100%) |
| How | at rest |

Crops: `explore-title-default.png`.

#### explore-link

Explore product link. A product-name row in the Explore index; measured, never followed.

Page: explore. Selector: `explore product link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 322.45 x 53 | = | = | = |
| Padding | 0px 4.43912px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(to right, #333333 0%, #333333 100%) | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | Neue Haas Grotesk Display Pro 44.3912px/42.1716px 500 | = | = | = |
| Letter spacing | -0.443912px | = | = | = |
| Colour | #eeeef2 | = | = | = |
| Transition | background-size 0.4s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a 322.5x53.0 image linear-gradient(to right, #333333 0%, #333333 100%) | = | a 322.5x53.0 image linear-gradient(to right, #333333 0%, #333333 100%) shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `explore-link-default.png`, `explore-link-hover.png`, `explore-link-focus-visible.png`, `explore-link-pressed.png`.

### Support and downloads

#### support-title

Support title. The 64px Neue Haas Grotesk Display page title.

Page: support. Selector: `support h1/h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 400.31 x 121.69 |
| Padding | 0px 0px 0px 70px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Display Pro 64.05px/60.8475px 500 |
| Letter spacing | -0.6405px |
| Colour | #eeeef2 |
| Transition | none |
| ::before | 37.9844px x 19.9531px, absolute, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `support-title-default.png`.

#### download-row

Support action link. A support/downloads action row (a .block-button.button-text link with a right icon) in the page content. Measured, never followed.

Page: support. Selector: `support action link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 28 x 28 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 7px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | Neue Haas Grotesk Text Pro 14px/21px 400 | = | = | = |
| Letter spacing | 0.462px | = | = | = |
| Colour | #eeeef2 | = | = | = |
| Transition | border, background-color, background-position, background-size, background-image, opacity 0.3s, 0.3s, 0.3s, 0.3s, 0.5s, 0.3s ease, ease, ease, ease, ease, ease delay 0s, 0s, 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 28 x 28, colour #eeeef2 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.block-button.button-text 28.0x28.0 shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px | = |

Crops: `download-row-default.png`, `download-row-hover.png`, `download-row-focus-visible.png`, `download-row-pressed.png`.

#### locator-title

Store locator title.

Page: store-locator. Selector: `store-locator heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 400.31 x 121.69 |
| Padding | 0px 0px 0px 70px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Display Pro 64.05px/60.8475px 500 |
| Letter spacing | -0.6405px |
| Colour | #eeeef2 |
| Transition | none |
| ::before | 37.9844px x 19.9531px, absolute, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `locator-title-default.png`.

### Contact

#### contact-title

Contact title. The 64px Neue Haas Grotesk Display Pro 500 page title.

Page: contact. Selector: `contact h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 373.03 x 60.84 |
| Padding | 0px 0px 0px 70px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Display Pro 64.05px/60.8475px 500 |
| Letter spacing | -0.6405px |
| Colour | #eeeef2 |
| Transition | none |
| ::before | 37.9844px x 19.9531px, absolute, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `contact-title-default.png`.

#### text-field

Text field. A 42px block-input: #eeeef2 field, #151515 text, Neue Haas Text 14px, square corners. Sample text was typed and deleted; the form was never submitted.

Page: contact. Selector: `.block-input input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 609 x 42 | = | = |
| Padding | 10.5px 14px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | #eeeef2 | = | = |
| Box shadow | none | #ffffff 0px 0px 0px 2px | #ffffff 0px 0px 0px 2px |
| Outline | none | 2px solid #000000 offset 2px | 2px solid #000000 offset 2px |
| Font | Neue Haas Grotesk Text Pro 14px/21px 400 | = | = |
| Letter spacing | 0.56px | = | = |
| Colour | #151515 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| Painted layers | input.block-input.has-secondary-background-color 609.0x42.0 bg #eeeef2 | input.block-input.has-secondary-background-color 609.0x42.0 bg #eeeef2 shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px | input.block-input.has-secondary-background-color 609.0x42.0 bg #eeeef2 shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px |
| How | at rest | clicked into the field | typed "Test name", then deleted; nothing sent |

Crops: `text-field-default.png`, `text-field-focused.png`, `text-field-filled.png`.

#### select-field

Select field. The Category select: same 42px field treatment; never changed.

Page: contact. Selector: `select.block-input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 609 x 42 | = |
| Padding | 10.5px 35px 10.5px 14px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #eeeef2 | = |
| Box shadow | none | #ffffff 0px 0px 0px 2px |
| Outline | none | 2px solid #000000 offset 2px |
| Font | Neue Haas Grotesk Text Pro 14px/21px 400 | = |
| Letter spacing | 0.56px | = |
| Colour | #151515 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | select.block-input.has-secondary-background-color 609.0x42.0 bg #eeeef2 | select.block-input.has-secondary-background-color 609.0x42.0 bg #eeeef2 shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px |
| How | at rest | clicked into the field |

Crops: `select-field-default.png`, `select-field-focused.png`.

#### textarea-field

Text area. The Message area: a taller #eeeef2 field. Focused only; nothing typed was sent.

Page: contact. Selector: `textarea.block-input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 609 x 126 | = |
| Padding | 10.5px 14px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #eeeef2 | = |
| Box shadow | none | #ffffff 0px 0px 0px 2px |
| Outline | none | 2px solid #000000 offset 2px |
| Font | Neue Haas Grotesk Text Pro 14px/21px 400 | = |
| Letter spacing | 0.56px | = |
| Colour | #151515 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #757575, opacity 1 | = |
| Painted layers | textarea.block-input.has-secondary-background-color 609.0x126.0 bg #eeeef2 | textarea.block-input.has-secondary-background-color 609.0x126.0 bg #eeeef2 shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px |
| How | at rest | clicked into the field |

Crops: `textarea-field-default.png`, `textarea-field-focused.png`.

#### submit-button

Submit button. The contact form SUBMIT: a 2px #eeeef2 outline block-button, digi one v2 14px caps, 46px tall. Measured, never pressed — the form was never sent.

Page: contact. Selector: `contact Submit button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 104.77 x 46 | = | = | = |
| Padding | 10.5px 17.5px | = | = | = |
| Gap | 7px | = | = | = |
| Border | 2px solid #eeeef2 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #eeeef2 | = | #eeeef2 |
| Background image | linear-gradient(to right, #333333 0%, #333333 100%) | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | digi one v2 14px/21px 400 | = | = | = |
| Letter spacing | 0.462px | = | = | = |
| Colour | #eeeef2 | #151515 | = | #151515 |
| Text node | span: digi one v2 14px/21px 400, #eeeef2, ls 0.462px | span: digi one v2 14px/21px 400, #151515, ls 0.462px | = | span: digi one v2 14px/21px 400, #151515, ls 0.462px |
| Transition | background-size 0.4s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.block-button.button-outline 104.8x46.0 image linear-gradient(to right, #333333 0%, #333333 100%) border T:2px solid #eeeef2 / R:2px solid #eeeef2 / B:2px solid #eeeef2 / L:2px solid #eeeef2 | button.block-button.button-outline 104.8x46.0 bg #eeeef2 image linear-gradient(to right, #333333 0%, #333333 100%) border T:2px solid #eeeef2 / R:2px solid #eeeef2 / B:2px solid #eeeef2 / L:2px solid #eeeef2 | button.block-button.button-outline 104.8x46.0 image linear-gradient(to right, #333333 0%, #333333 100%) border T:2px solid #eeeef2 / R:2px solid #eeeef2 / B:2px solid #eeeef2 / L:2px solid #eeeef2 shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px | button.block-button.button-outline 104.8x46.0 bg #eeeef2 image linear-gradient(to right, #333333 0%, #333333 100%) border T:2px solid #eeeef2 / R:2px solid #eeeef2 / B:2px solid #eeeef2 / L:2px solid #eeeef2 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `submit-button-default.png`, `submit-button-hover.png`, `submit-button-focus-visible.png`, `submit-button-pressed.png`.

### Account and cart

#### cart-drawer

Mini-cart drawer. The cart side drawer (a 392px right drawer, dialog.tdc-cart): "Your cart is empty." with a CONTINUE SHOPPING action. Nothing was ever added.

Page: cart. Selector: `dialog.tdc-cart`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 14px/16.1px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.skip-link: Neue Haas Grotesk Text Pro 14px/normal 700, #21759b, ls 0.462px |
| Transition | none |
| Icon | 28 x 28, colour #eeeef2 |
| Painted layers | body.wp-singular.page-template-default 1440.0x4069.1 bg #151515; a.skip-link 156.9x34.4 bg #f1f1f1 image linear-gradient(to right, #333333 0%, #333333 100%) shadow #000000 @ 0.6 0px 0px 2px 2px; div.element-background.has-center-center-position 1440.0x56.0 bg #151515; span 54.3x21.0 image linear-gradient(to right, #333333 0%, #333333 100%); span 35.9x21.0 image linear-gradient(to right, #333333 0%, #333333 100%); span 50.1x21.0 image linear-gradient(to right, #333333 0%, #333333 100%) |
| How | at rest |

Crops: `cart-drawer-default.png`.

#### cart-continue

Continue shopping action. The empty-cart action row; measured, never followed.

Page: cart. Selector: `cart continue action`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 350 x 46 | = | = | = |
| Padding | 10.5px 17.5px | = | = | = |
| Gap | 7px | = | = | = |
| Border | 2px solid #eeeef2 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #eeeef2 | = | #eeeef2 |
| Background image | linear-gradient(to right, #333333 0%, #333333 100%) | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | digi one v2 14px/21px 400 | = | = | = |
| Letter spacing | 0.462px | = | = | = |
| Colour | #eeeef2 | #151515 | = | #151515 |
| Transition | background-size 0.4s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.button.tdc-button 350.0x46.0 image linear-gradient(to right, #333333 0%, #333333 100%) border T:2px solid #eeeef2 / R:2px solid #eeeef2 / B:2px solid #eeeef2 / L:2px solid #eeeef2 | button.button.tdc-button 350.0x46.0 bg #eeeef2 image linear-gradient(to right, #333333 0%, #333333 100%) border T:2px solid #eeeef2 / R:2px solid #eeeef2 / B:2px solid #eeeef2 / L:2px solid #eeeef2 | button.button.tdc-button 350.0x46.0 image linear-gradient(to right, #333333 0%, #333333 100%) border T:2px solid #eeeef2 / R:2px solid #eeeef2 / B:2px solid #eeeef2 / L:2px solid #eeeef2 shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px | button.button.tdc-button 350.0x46.0 bg #eeeef2 image linear-gradient(to right, #333333 0%, #333333 100%) border T:2px solid #eeeef2 / R:2px solid #eeeef2 / B:2px solid #eeeef2 / L:2px solid #eeeef2 |
| Ancestor paint | 3 up div.tdc-cart__panel bg #151515 shadow #000000 @ 0.18 -7px 0px 35px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cart-continue-default.png`, `cart-continue-hover.png`, `cart-continue-focus-visible.png`, `cart-continue-pressed.png`.

#### login-panel

Login panel. The /my-account magic-login surface (the same Send me a code form as the header drawer). Captured, never used.

Page: my-account. Selector: `my-account form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 392 x 141.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Text Pro 14px/21px 400 |
| Letter spacing | 0.462px |
| Colour | #eeeef2 |
| Text node | span: digi one v2 14px/21px 400, #151515, ls 0.462px |
| Transition | none |
| Icon | 24 x 24, colour #ffffff, fill #000000 |
| Painted layers | input.block-input.button-full_form 392.0x42.0 bg #eeeef2; input.block-input.button-full_form 0.0x0.0 bg #eeeef2; input.block-input.has-undefined-background-color 0.0x0.0 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff; input 0.0x0.0 bg #151515 border T:2px solid #eeeef2 / R:2px solid #eeeef2 / B:2px solid #eeeef2 / L:2px solid #eeeef2; button.block-button.button-full 0.0x0.0 bg #cccccc image linear-gradient(to right, #333333 0%, #333333 100%); a 0.0x0.0 image linear-gradient(to right, #333333 0%, #333333 100%) |
| How | at rest |

Crops: none.

#### login-email

Login email field. The Email input of the magic-login form. Sample text was typed and deleted; no code was ever requested.

Page: my-account. Selector: `my-account email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 392 x 42 | = | = |
| Padding | 10.5px 44px 10.5px 17.5px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | #eeeef2 | #151515 | #151515 |
| Box shadow | none | #ffffff 0px 0px 0px 2px | #ffffff 0px 0px 0px 2px |
| Outline | none | 2px solid #000000 offset 2px | 2px solid #000000 offset 2px |
| Font | digi one v2 14px/21px 400 | = | = |
| Letter spacing | 0.462px | = | = |
| Colour | #151515 | #eeeef2 | #eeeef2 |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| Painted layers | input.block-input.button-full_form 392.0x42.0 bg #eeeef2 | input.block-input.button-full_form 392.0x42.0 bg #151515 shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px | input.block-input.button-full_form 392.0x42.0 bg #151515 shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-email-default.png`, `login-email-focused.png`, `login-email-filled.png`.

#### login-send

Send me a code button. The full-width secondary-variant block-button (grey #cccccc fill, #151515 digi label). Measured, never pressed.

Page: my-account. Selector: `my-account Send me a code`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 392 x 42 | = | = | = |
| Padding | 10.5px 17.5px | = | = | = |
| Gap | 7px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #cccccc | #151515 | = | #151515 |
| Background image | linear-gradient(to right, #333333 0%, #333333 100%) | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | digi one v2 14px/21px 400 | = | = | = |
| Letter spacing | 0.462px | = | = | = |
| Colour | #151515 | #cccccc | = | #cccccc |
| Text node | span: digi one v2 14px/21px 400, #151515, ls 0.462px | span: digi one v2 14px/21px 400, #cccccc, ls 0.462px | = | span: digi one v2 14px/21px 400, #cccccc, ls 0.462px |
| Transition | background-size 0.4s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.block-button.button-full 392.0x42.0 bg #cccccc image linear-gradient(to right, #333333 0%, #333333 100%) | button.block-button.button-full 392.0x42.0 bg #151515 image linear-gradient(to right, #333333 0%, #333333 100%) | button.block-button.button-full 392.0x42.0 bg #cccccc image linear-gradient(to right, #333333 0%, #333333 100%) shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px | button.block-button.button-full 392.0x42.0 bg #151515 image linear-gradient(to right, #333333 0%, #333333 100%) |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-send-default.png`, `login-send-hover.png`, `login-send-focus-visible.png`, `login-send-pressed.png`.

#### login-create

Create account button. The secondary account action; measured, never pressed.

Page: my-account. Selector: `my-account Create New Account`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 392 x 42 | = | = | = |
| Padding | 10.5px 17.5px | = | = | = |
| Gap | 7px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #cccccc | #151515 | = | #151515 |
| Background image | linear-gradient(to right, #333333 0%, #333333 100%) | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | digi one v2 14px/21px 400 | = | = | = |
| Letter spacing | 0.462px | = | = | = |
| Colour | #151515 | #cccccc | = | #cccccc |
| Text node | span: digi one v2 14px/21px 400, #151515, ls 0.462px | span: digi one v2 14px/21px 400, #cccccc, ls 0.462px | = | span: digi one v2 14px/21px 400, #cccccc, ls 0.462px |
| Transition | background-size 0.4s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.block-button.button-full 392.0x42.0 bg #cccccc image linear-gradient(to right, #333333 0%, #333333 100%) | a.block-button.button-full 392.0x42.0 bg #151515 image linear-gradient(to right, #333333 0%, #333333 100%) | a.block-button.button-full 392.0x42.0 bg #cccccc image linear-gradient(to right, #333333 0%, #333333 100%) shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px | a.block-button.button-full 392.0x42.0 bg #151515 image linear-gradient(to right, #333333 0%, #333333 100%) |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-create-default.png`, `login-create-hover.png`, `login-create-focus-visible.png`, `login-create-pressed.png`.

### Footer

#### footer

Footer. The footer: the Elektron wordmark, the Navigation / Shop / Support / Resources columns of 24px Neue Haas Display links, legal row and the cookie-settings reopen link.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 656.42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Text Pro 14px/21px 400 |
| Letter spacing | 0.462px |
| Colour | #eeeef2 |
| Text node | h2.wp-block-heading.has-normal-font-size: Neue Haas Grotesk Text Pro 14px/21px 400, #eeeef2, ls 0.462px |
| Transition | none |
| Icon | 213 x 25.55, colour #eeeef2 |
| Painted layers | div.element-background.has-center-center-position 1440.0x656.4 bg #151515 @ 0.1; a.block-button.button-medium_text 58.0x36.0 image linear-gradient(to right, #333333 0%, #333333 100%); a.block-button.button-medium_text 89.6x36.0 image linear-gradient(to right, #333333 0%, #333333 100%); a.block-button.button-medium_light_text 63.3x36.0 image linear-gradient(to right, #333333 0%, #333333 100%); a.block-button.button-medium_light_text 153.0x36.0 image linear-gradient(to right, #333333 0%, #333333 100%); a.block-button.button-medium_light_text 140.8x36.0 image linear-gradient(to right, #333333 0%, #333333 100%) |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer column link: 24px Neue Haas Grotesk Display 450, measured, never followed.

Page: home. Selector: `footer .block-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 58.05 x 36.02 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 12.005px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(to right, #333333 0%, #333333 100%) | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | Neue Haas Grotesk Display Pro 24.01px/36.015px 450 | = | = | = |
| Letter spacing | 0.9604px | = | = | = |
| Colour | #eeeef2 | = | = | = |
| Transition | background-size 0.4s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.block-button.button-medium_text 58.0x36.0 image linear-gradient(to right, #333333 0%, #333333 100%) | = | a.block-button.button-medium_text 58.0x36.0 image linear-gradient(to right, #333333 0%, #333333 100%) shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-wordmark

Footer wordmark. The Elektron logo link at the foot of the page.

Page: home. Selector: `footer wordmark`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 213 x 25.55 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Text Pro 14px/21px 400 |
| Letter spacing | 0.462px |
| Colour | #eeeef2 |
| Transition | none |
| Cursor | pointer |
| Icon | 213 x 25.55, colour #eeeef2 |
| How | at rest |

Crops: `footer-wordmark-default.png`.

#### social-icon

Social link. A social link in the footer.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 17.97 x 18.38 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | Neue Haas Grotesk Text Pro 14px/21px 400 | = | = | = |
| Letter spacing | 0.462px | = | = | = |
| Colour | #eeeef2 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.block-icon.is-brand 18.0x18.4 shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px | = |

Crops: `social-icon-default.png`, `social-icon-hover.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 63 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Text Pro 14px/21px 400 |
| Letter spacing | 0.462px |
| Colour | #eeeef2 |
| Transition | box-shadow, height, color, background-color, -webkit-box-shadow 0.8s, 0.4s, 0.4s, 0.4s, 0.8s cubic-bezier(0.365, 0.305, 0, 1), cubic-bezier(0, 1.05, 0.65, 1.01), cubic-bezier(0.365, 0.305, 0, 1), cubic-bezier(0.365, 0.305, 0, 1), cubic-bezier(0.365, 0.305, 0, 1) delay 0s, 0s, 0s, 0s, 0s |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 35 x 24.86, colour #eeeef2 |
| Painted layers | div.element-background.has-center-center-position 390.0x63.0 bg #151515 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The burger anchor that toggles the mobile menu panel.

Page: mobile. Selector: `a[href=#menu-trigger]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 35 x 35 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Text Pro 14px/21px 400 |
| Letter spacing | 0.462px |
| Colour | #eeeef2 |
| Transition | none |
| Cursor | pointer |
| Icon | 35 x 35, colour #eeeef2 |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The opened mobile navigation panel: the header expands to a fullscreen menu with a search row and Catalog / Shop / Kulture / Support / Account links.

Page: mobile. Selector: `opened mobile menu header`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Text Pro 14px/21px 400 |
| Letter spacing | 0.462px |
| Colour | #eeeef2 |
| Text node | span: Neue Haas Grotesk Display Pro 24.01px/36.015px 450, #eeeef2, ls 0.9604px |
| Transition | none |
| Icon | 35 x 24.86, colour #eeeef2 |
| Painted layers | div.element-background.has-center-center-position 390.0x63.0 bg #151515; div.element-background.has-center-center-position 390.0x781.0 bg #151515; input.search-field.has-normal-border 362.0x48.6 bg #151515 border T:2px solid #eeeef2 / R:2px solid #eeeef2 / B:2px solid #eeeef2 / L:2px solid #eeeef2; span 86.6x36.0 image linear-gradient(to right, #333333 0%, #333333 100%); span 58.0x36.0 image linear-gradient(to right, #333333 0%, #333333 100%); span 80.3x36.0 image linear-gradient(to right, #333333 0%, #333333 100%) |
| Ancestor paint | 1 up body.home.wp-singular bg #151515 |
| How | held open by an earlier toggle |

Crops: `m-menu-open-opened.png`.

#### m-nav-item

Mobile nav item. A row inside the opened mobile menu.

Page: mobile. Selector: `mobile menu row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138.41 x 36.02 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 16.8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px | #ffffff 0px 0px 0px 2px |
| Outline | none | = | 2px solid #000000 offset 2px | 2px solid #000000 offset 2px |
| Font | Neue Haas Grotesk Display Pro 24.01px/36.015px 450 | = | = | = |
| Letter spacing | 0.9604px | = | = | = |
| Colour | #eeeef2 | = | = | = |
| Text node | span: Neue Haas Grotesk Display Pro 24.01px/36.015px 450, #eeeef2, ls 0.9604px | = | = | = |
| Transition | border, background-color, background-position, background-size, background-image, opacity 0.3s, 0.3s, 0.3s, 0.3s, 0.5s, 0.3s ease, ease, ease, ease, ease, ease delay 0s, 0s, 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 35 x 35, colour #eeeef2 | = | = | = |
| Painted layers | span 86.6x36.0 image linear-gradient(to right, #333333 0%, #333333 100%) | = | a.block-button.button-medium_text 138.4x36.0 shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px; span 86.6x36.0 image linear-gradient(to right, #333333 0%, #333333 100%) | a.block-button.button-medium_text 138.4x36.0 shadow #ffffff 0px 0px 0px 2px outline 2px solid #000000 offset 2px; span 86.6x36.0 image linear-gradient(to right, #333333 0%, #333333 100%) |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile heading.

Page: mobile. Selector: `first heading at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 219.94 x 31.64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Neue Haas Grotesk Display Pro 23.8px/31.654px 400 |
| Letter spacing | 0.952px |
| Colour | #eeeef2 |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

elektron.se serves its theme and plugin sheets same-origin, so this list covers the transition rules the page itself exposes; the per-state Transition rows above are the computed values the page paints.

- about: `opacity var(--tdss-transition) var(--tdss-loading-delay)`, `background-color var(--tdss-transition)`, `none`, `background-size 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index)),top 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index))`, `opacity 0s linear calc(60ms*var(--char-index))`, `background-size 0.5s`, `box-shadow 0.3s, -webkit-box-shadow 0.3s`, `color 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `transform 0.3s cubic-bezier(0.365, 0.305, 0, 1), width 0.3s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), transform 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.4s cubic-bezier(0.365, 0.305, 0, 1)`, `box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1), height 0.4s cubic-bezier(0, 1.05, 0.65, 1.01), color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1)`, `0.7s cubic-bezier(0, 1.05, 0.65, 1.01)`

- cart: `opacity var(--tdss-transition) var(--tdss-loading-delay)`, `background-color var(--tdss-transition)`, `none`, `background-size 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index)),top 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index))`, `opacity 0s linear calc(60ms*var(--char-index))`, `background-size 0.5s`, `box-shadow 0.3s, -webkit-box-shadow 0.3s`, `color 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `transform 0.3s cubic-bezier(0.365, 0.305, 0, 1), width 0.3s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), transform 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.4s cubic-bezier(0.365, 0.305, 0, 1)`, `box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1), height 0.4s cubic-bezier(0, 1.05, 0.65, 1.01), color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1)`, `0.7s cubic-bezier(0, 1.05, 0.65, 1.01)`

- contact: `opacity var(--tdss-transition) var(--tdss-loading-delay)`, `background-color var(--tdss-transition)`, `none`, `background-size 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index)),top 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index))`, `opacity 0s linear calc(60ms*var(--char-index))`, `background-size 0.5s`, `box-shadow 0.3s, -webkit-box-shadow 0.3s`, `color 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `transform 0.3s cubic-bezier(0.365, 0.305, 0, 1), width 0.3s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), transform 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.4s cubic-bezier(0.365, 0.305, 0, 1)`, `box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1), height 0.4s cubic-bezier(0, 1.05, 0.65, 1.01), color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1)`, `0.7s cubic-bezier(0, 1.05, 0.65, 1.01)`

- explore: `opacity var(--tdss-transition) var(--tdss-loading-delay)`, `background-color var(--tdss-transition)`, `none`, `background-size 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index)),top 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index))`, `opacity 0s linear calc(60ms*var(--char-index))`, `background-size 0.5s`, `box-shadow 0.3s, -webkit-box-shadow 0.3s`, `color 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `transform 0.3s cubic-bezier(0.365, 0.305, 0, 1), width 0.3s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), transform 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.4s cubic-bezier(0.365, 0.305, 0, 1)`, `box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1), height 0.4s cubic-bezier(0, 1.05, 0.65, 1.01), color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1)`, `0.7s cubic-bezier(0, 1.05, 0.65, 1.01)`

- home: `opacity var(--tdss-transition) var(--tdss-loading-delay)`, `background-color var(--tdss-transition)`, `none`, `background-size 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index)),top 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index))`, `opacity 0s linear calc(60ms*var(--char-index))`, `background-size 0.5s`, `box-shadow 0.3s, -webkit-box-shadow 0.3s`, `color 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `transform 0.3s cubic-bezier(0.365, 0.305, 0, 1), width 0.3s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), transform 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.4s cubic-bezier(0.365, 0.305, 0, 1)`, `box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1), height 0.4s cubic-bezier(0, 1.05, 0.65, 1.01), color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1)`, `0.7s cubic-bezier(0, 1.05, 0.65, 1.01)`

- my-account: `opacity var(--tdss-transition) var(--tdss-loading-delay)`, `background-color var(--tdss-transition)`, `none`, `background-size 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index)),top 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index))`, `opacity 0s linear calc(60ms*var(--char-index))`, `background-size 0.5s`, `box-shadow 0.3s, -webkit-box-shadow 0.3s`, `color 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `transform 0.3s cubic-bezier(0.365, 0.305, 0, 1), width 0.3s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), transform 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.4s cubic-bezier(0.365, 0.305, 0, 1)`, `box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1), height 0.4s cubic-bezier(0, 1.05, 0.65, 1.01), color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1)`, `0.7s cubic-bezier(0, 1.05, 0.65, 1.01)`

- product-digitakt: `opacity var(--tdss-transition) var(--tdss-loading-delay)`, `background-color var(--tdss-transition)`, `none`, `background-size 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index)),top 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index))`, `opacity 0s linear calc(60ms*var(--char-index))`, `background-size 0.5s`, `box-shadow 0.3s, -webkit-box-shadow 0.3s`, `color 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `transform 0.3s cubic-bezier(0.365, 0.305, 0, 1), width 0.3s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), transform 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.4s cubic-bezier(0.365, 0.305, 0, 1)`, `box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1), height 0.4s cubic-bezier(0, 1.05, 0.65, 1.01), color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1)`, `0.7s cubic-bezier(0, 1.05, 0.65, 1.01)`

- shop: `opacity var(--tdss-transition) var(--tdss-loading-delay)`, `background-color var(--tdss-transition)`, `none`, `background-size 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index)),top 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index))`, `opacity 0s linear calc(60ms*var(--char-index))`, `background-size 0.5s`, `box-shadow 0.3s, -webkit-box-shadow 0.3s`, `color 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `transform 0.3s cubic-bezier(0.365, 0.305, 0, 1), width 0.3s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), transform 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.4s cubic-bezier(0.365, 0.305, 0, 1)`, `box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1), height 0.4s cubic-bezier(0, 1.05, 0.65, 1.01), color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1)`, `0.7s cubic-bezier(0, 1.05, 0.65, 1.01)`

- store-locator: `opacity var(--tdss-transition) var(--tdss-loading-delay)`, `background-color var(--tdss-transition)`, `none`, `background-size 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index)),top 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index))`, `opacity 0s linear calc(60ms*var(--char-index))`, `background-size 0.5s`, `box-shadow 0.3s, -webkit-box-shadow 0.3s`, `color 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `transform 0.3s cubic-bezier(0.365, 0.305, 0, 1), width 0.3s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), transform 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.4s cubic-bezier(0.365, 0.305, 0, 1)`, `box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1), height 0.4s cubic-bezier(0, 1.05, 0.65, 1.01), color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1)`, `0.7s cubic-bezier(0, 1.05, 0.65, 1.01)`

- support: `opacity var(--tdss-transition) var(--tdss-loading-delay)`, `background-color var(--tdss-transition)`, `none`, `background-size 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index)),top 1.5s cubic-bezier(.77,0,.175,1) calc(100ms*var(--line-index))`, `opacity 0s linear calc(60ms*var(--char-index))`, `background-size 0.5s`, `box-shadow 0.3s, -webkit-box-shadow 0.3s`, `color 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `transform 0.3s cubic-bezier(0.365, 0.305, 0, 1), width 0.3s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.3s cubic-bezier(0.365, 0.305, 0, 1)`, `color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), transform 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.4s cubic-bezier(0.365, 0.305, 0, 1)`, `box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1), height 0.4s cubic-bezier(0, 1.05, 0.65, 1.01), color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1)`, `0.7s cubic-bezier(0, 1.05, 0.65, 1.01)`
