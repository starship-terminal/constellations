# Component measurements

Computed styles read from drinkdouze.com on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the light-only boxed surface — the announcement bar and header, the boxed sections on the sable field, the shop grid, the product buy box, the account and cart pages — with any Klaviyo popup or consent overlay hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### announcement-bar

Announcement bar. The top strip ("Livraison gratuite en France métropolitaine à partir de 50€"), sable on the page edge.

Page: home. Selector: `announcement-bar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 36.45 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Robin Regular 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #301816 |
| Text node | p: Robin Semibold 12px/18.4615px 500, #301816, ls 0.96px |
| Transition | none |
| Painted layers | section.section 1390.0x36.5 bg #f6f2e9 r 45px; announcement-bar.announcement-bar 1390.0x36.5 bg #f6f2e9 r 45px |
| How | at rest |

Crops: `announcement-bar-default.png`.

#### header

Header. The sticky transparent header: nav links left, the DOUZE wordmark centre, links + newsletter/account/cart icons right.

Page: home. Selector: `store-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1390 x 57 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Robin Regular 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #301816 |
| Text node | a.header__linklist-link.link--animated: Robin Semibold 12px/13.2px 500, #301816, ls 1.2px |
| Transition | background, color, box-shadow 0.2s, 0.2s, 0.2s ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s |
| Icon | 0 x 0, colour #301816, fill #000000 |
| Painted layers | a::after.header__linklist-link.link--animated 38.6406pxx1px bg #301816; a::after.header__linklist-link.link--animated 116.969pxx1px bg #301816; a::after.header__linklist-link.link--animated 139.672pxx1px bg #301816; a::after.header__linklist-link.link--animated 71.8594pxx1px bg #301816; a::after.header__linklist-link.link--animated 109.766pxx1px bg #301816; a::after.header__linklist-link.link--animated 78.7812pxx1px bg #301816 |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The DOUZE wordmark SVG anchor.

Page: home. Selector: `.header__logo-link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 70 x 23 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Robin Regular 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #301816 |
| Transition | none |
| Cursor | pointer |
| Icon | 70 x 23, colour #301816, fill #000000 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link. A plain header nav link (animated-underline style).

Page: home. Selector: `a.header__linklist-link "Notre Histoire"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 116.97 x 13.19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Robin Semibold 12px/13.2px 500 | = | = | = |
| Letter spacing | 1.2px | = | = | = |
| Colour | #301816 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 116.969px x 1px, absolute, bg #301816, radius 0px | = | = | = |
| Painted layers | a::after.header__linklist-link.link--animated 116.969pxx1px bg #301816 | = | a.header__linklist-link.link--animated 117.0x13.2 outline 1px auto #005fcc offset 1px; a::after.header__linklist-link.link--animated 116.969pxx1px bg #301816 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-pressed.png`.

#### nav-shop

Shop nav link. The Shop link, marked has-dropdown; its panel content is not in the signed-out DOM on hover.

Page: home. Selector: `.header__linklist-item.has-dropdown a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 38.64 x 13.19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Robin Semibold 12px/13.2px 500 | = | = | = |
| Letter spacing | 1.2px | = | = | = |
| Colour | #301816 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 38.6406px x 1px, absolute, bg #301816, radius 0px | = | = | = |
| Painted layers | a::after.header__linklist-link.link--animated 38.6406pxx1px bg #301816 | = | a.header__linklist-link.link--animated 38.6x13.2 outline 1px auto #005fcc offset 1px; a::after.header__linklist-link.link--animated 38.6406pxx1px bg #301816 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-shop-default.png`, `nav-shop-hover.png`, `nav-shop-focus-visible.png`, `nav-shop-pressed.png`.

#### account-icon

Account icon link. The person icon linking to /account/login; measured, never followed.

Page: home. Selector: `a[aria-label="Connexion"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 25 x 25 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Robin Regular 16px/19.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #301816 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 25 x 25, colour #301816 | = | = | = |
| ::before | 37px x 37px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.header__icon-wrapper.tap-area 25.0x25.0 outline 1px auto #005fcc offset 1px | = |

Crops: `account-icon-default.png`, `account-icon-hover.png`, `account-icon-focus-visible.png`, `account-icon-pressed.png`.

#### cart-icon

Cart icon. The bag icon with the floating cart-count bubble; toggles the mini-cart drawer.

Page: home. Selector: `a[aria-controls="mini-cart"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 20 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Robin Regular 16px/19.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #301816 | = | = | = |
| Text node | cart-count.header__cart-count.header__cart-count--floating: Robin Regular 9px/8.55px 600, #f6f2e9 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 18, colour #301816, fill #000000 | = | = | = |
| ::before | 32px x 30px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | cart-count.header__cart-count.header__cart-count--floating 15.0x15.0 bg #301816 r 15px | = | a.header__icon-wrapper.tap-area 20.0x18.0 outline 1px auto #005fcc offset 1px; cart-count.header__cart-count.header__cart-count--floating 15.0x15.0 bg #301816 r 15px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cart-icon-default.png`, `cart-icon-hover.png`, `cart-icon-focus-visible.png`, `cart-icon-pressed.png`.

#### cart-count

Cart count bubble. The numeric bubble on the bag icon (0 signed out).

Page: home. Selector: `cart-count`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 15 x 15 |
| Padding | 0px |
| Border | none |
| Radius | 15px |
| Background | #301816 |
| Box shadow | none |
| Outline | none |
| Font | Robin Regular 9px/8.55px 600 |
| Letter spacing | normal |
| Colour | #f6f2e9 |
| Transition | background, color 0.2s, 0.2s ease-in-out, ease-in-out delay 0s, 0s |
| Cursor | pointer |
| Painted layers | cart-count.header__cart-count.header__cart-count--floating 15.0x15.0 bg #301816 r 15px |
| How | at rest |

Crops: `cart-count-default.png`.

### Home hero

#### hero-title

Hero headline. The boxed hero's Boogy display heading (60-72px, italic accent on the flavour name), sable text over the photo.

Page: home. Selector: `.image-hero__heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 559.8 x 194.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Boogy 72px/64.8px 300 |
| Letter spacing | -0.72px |
| Colour | #f6f2e9 |
| Text node | em: Boogy Italic 72px/64.8px 300, #f6f2e9, ls -0.72px |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-cta

Hero CTA. The "SHOP" button over the hero media: dusk fill, white label, square 0px corners.

Page: home. Selector: `.image-hero__button .button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 67.69 x 44 | = | = | = |
| Padding | 0px 15px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #301816 | = | = | = |
| Background image | linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), linear-gradient(#301816, #301816) | = | = | = |
| Box shadow | none | #000000 @ 0.15 0px 4px 8px 0px | = | #000000 @ 0.15 0px 4px 8px 0px |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Robin Semibold 12px/14.4px 500 | = | = | = |
| Letter spacing | 0.96px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | transform, box-shadow 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | matrix(1, 0, 0, 1, 0, -2) | = | matrix(1, 0, 0, 1, 0, -2) |
| Cursor | pointer | = | = | = |
| ::before | 20px x 44px, absolute, bg #301816, radius 0px | = | = | = |
| ::after | 20px x 44px, absolute, bg #301816, radius 0px | = | = | = |
| Painted layers | a.button.button--primary 67.7x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li; a::before.button.button--primary 20pxx44px bg #301816; a::after.button.button--primary 20pxx44px bg #301816 | a.button.button--primary 67.7x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li shadow #000000 @ 0.15 0px 4px 8px 0px; a::before.button.button--primary 20pxx44px bg #301816; a::after.button.button--primary 20pxx44px bg #301816 | a.button.button--primary 67.7x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li outline 1px auto #005fcc offset 1px; a::before.button.button--primary 20pxx44px bg #301816; a::after.button.button--primary 20pxx44px bg #301816 | a.button.button--primary 67.7x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li shadow #000000 @ 0.15 0px 4px 8px 0px; a::before.button.button--primary 20pxx44px bg #301816; a::after.button.button--primary 20pxx44px bg #301816 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

### Home sections

#### marquee

Moving banner. The scrolling claim strip ("Sans sucre ajouté · Faible en calories · …") between sections.

Page: home. Selector: `.moving-banner`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Robin Regular 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #301816 |
| Text node | p: Robin Semibold 12px/14.4px 600, #301816, ls 0.96px |
| Transition | none |
| Painted layers | div::after.moving-banner_divider 9pxx9px bg #cfe6f4 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 50%; div::after.moving-banner_divider 9pxx9px bg #cfe6f4 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 50%; div::after.moving-banner_divider 9pxx9px bg #cfe6f4 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 50%; div::after.moving-banner_divider 9pxx9px bg #cfe6f4 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 50%; div::after.moving-banner_divider 9pxx9px bg #cfe6f4 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 50%; div::after.moving-banner_divider 9pxx9px bg #cfe6f4 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 50% |
| How | at rest |

Crops: `marquee-default.png`.

#### marquee-item

Moving banner item. One claim inside the scrolling strip, divided by 9px dots.

Page: home. Selector: `.moving-banner item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 96.06 x 28.78 |
| Padding | 0px |
| Gap | 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Robin Regular 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #301816 |
| Text node | p: Robin Semibold 12px/14.4px 600, #301816, ls 0.96px |
| Transition | none |
| How | at rest |

Crops: none.

#### section-h2

Section heading. A Boogy section heading inside a boxed section.

Page: home. Selector: `h2.heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 779 x 104 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Boogy 52px/52px 300 |
| Letter spacing | -0.52px |
| Colour | #ffffff |
| Text node | p: Boogy 52px/52px 300, #ffffff, ls -0.52px |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

#### product-item

Product card. A product-item card in the featured row: packshot, flavour title, price button; hover swaps to the second image.

Page: home. Selector: `product-item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 398.66 x 498.31 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 45px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Robin Regular 16px/19.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #301816 | = | = | = |
| Text node | p.h5: Robin Semibold 12px/14.4px 600, #301816, ls 0.96px | span.loader-button__text: Robin Semibold 12px/14.4px 500, #ffffff, ls 0.96px | = | - |
| Transition | none | = | = | = |
| Icon | 0 x 0, colour #ffffff, fill #000000 | = | = | = |
| Painted layers | button.button.button--primary 209.8x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li; button::before.button.button--primary 20pxx44px bg #301816; button::after.button.button--primary 20pxx44px bg #301816 | = | a 0.0x0.0 outline 1px auto #005fcc offset 1px; button.button.button--primary 209.8x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li; button::before.button.button--primary 20pxx44px bg #301816; button::after.button.button--primary 20pxx44px bg #301816 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `product-item-default.png`, `product-item-hover.png`, `product-item-focus-visible.png`, `product-item-pressed.png`.

#### product-price

Product price. The price inside the card's quick-add button — the form reveals on card hover.

Page: home. Selector: `.product-item__btn-price (hover-revealed)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 26.3 x 14.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Robin Semibold 12px/14.4px 500 |
| Letter spacing | 0.96px |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 2 up button.button.button--primary bg #301816 shadow #000000 @ 0.15 0px 4px 8px 0px |
| How | at rest |

Crops: `product-price-default.png`.

#### testimonial

Testimonial. A customer quote in the "Douze & vous" section.

Page: home. Selector: `.testimonials-2 testimonial`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1390 x 453.31 |
| Padding | 0px |
| Gap | 20px |
| Border | none |
| Radius | 45px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Robin Regular 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #301816 |
| Text node | p: Boogy 72px/64.8px 300, #301816, ls -0.72px |
| Transition | none |
| Icon | 10 x 16, colour #ffffff |
| Painted layers | button.testimonials-2__nav-btn.testimonials-2__nav-btn--prev 35.0x35.0 bg #babec5 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 50%; div.testimonials-2__item.text--center 450.0x368.5 bg #301816 r 45px; div.testimonials-2__item.text--center 450.0x368.5 bg #301816 r 45px; div.testimonials-2__item.text--center 450.0x368.5 bg #301816 r 45px; div.testimonials-2__item.text--center 450.0x368.5 bg #301816 r 45px; div.testimonials-2__item.text--center 450.0x368.5 bg #301816 r 45px |
| How | at rest |

Crops: `testimonial-default.png`.

### Shop

#### shop-title

Shop banner. The collection page's image-hero band — the page leads with media; the heading node is a wordmark image with no live text.

Page: shop. Selector: `.image-overlay__text-container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1390 x 550 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Robin Regular 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `shop-title-default.png`.

#### product-card

Product card. A product-item in the /collections/all grid; its per-flavour --button-background-color rebinds the button fill (#f26554 for Orange Sanguine & Piment).

Page: shop. Selector: `product-item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 398.66 x 498.31 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 45px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Robin Regular 16px/19.2px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #301816 | = | - | = |
| Text node | p.h5: Robin Semibold 12px/14.4px 600, #301816, ls 0.96px | span.loader-button__text: Robin Semibold 12px/14.4px 500, #ffffff, ls 0.96px | - | - |
| Transition | none | = | - | = |
| Icon | 0 x 0, colour #ffffff, fill #000000 | = | - | = |
| Painted layers | button.button.button--primary 209.8x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li; button::before.button.button--primary 20pxx44px bg #301816; button::after.button.button--primary 20pxx44px bg #301816 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `product-card-default.png`, `product-card-hover.png`, `product-card-pressed.png`.

#### product-card-title

Product card wordmark. The flavour title on a grid card is a wordmark image (no live text), over a pack-line paragraph.

Page: shop. Selector: `.product-item__title-wrapper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 378.66 x 65 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Boogy 60px/39px 500 |
| Letter spacing | normal |
| Colour | #301816 |
| Transition | none |
| How | at rest |

Crops: `product-card-title-default.png`.

#### product-card-price

Quick-add price. The price span inside the quick-add button.

Page: shop. Selector: `.product-item__btn-price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 26.3 x 14.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Robin Semibold 12px/14.4px 500 |
| Letter spacing | 0.96px |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `product-card-price-default.png`.

#### quick-add

Quick-add button. The card's Ajouter-au-panier — visibility:hidden until the card is hovered; the press posts to /cart/add so it is measured, never pressed.

Page: shop. Selector: `.product-item__add-to-cart-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 209.75 x 44 | = | = | = |
| Padding | 0px 15px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #301816 | = | = | = |
| Background image | linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), linear-gradient(#301816, #301816) | = | = | = |
| Box shadow | none | #000000 @ 0.15 0px 4px 8px 0px | = | #000000 @ 0.15 0px 4px 8px 0px |
| Outline | none | = | 1px auto #005fcc offset 0px | 1px auto #005fcc offset 0px |
| Font | Robin Semibold 12px/14.4px 500 | = | = | = |
| Letter spacing | 0.96px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.loader-button__text: Robin Semibold 12px/14.4px 500, #ffffff, ls 0.96px | = | = | = |
| Transition | transform, box-shadow 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | matrix(1, 0, 0, 1, 0, -2) | = | matrix(1, 0, 0, 1, 0, -2) |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #ffffff, fill #000000 | = | = | = |
| ::before | 20px x 44px, absolute, bg #301816, radius 0px | = | = | = |
| ::after | 20px x 44px, absolute, bg #301816, radius 0px | = | = | = |
| Painted layers | button.button.button--primary 209.8x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li; button::before.button.button--primary 20pxx44px bg #301816; button::after.button.button--primary 20pxx44px bg #301816 | button.button.button--primary 209.8x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li shadow #000000 @ 0.15 0px 4px 8px 0px; button::before.button.button--primary 20pxx44px bg #301816; button::after.button.button--primary 20pxx44px bg #301816 | button.button.button--primary 209.8x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li outline 1px auto #005fcc offset 0px; button::before.button.button--primary 20pxx44px bg #301816; button::after.button.button--primary 20pxx44px bg #301816 | button.button.button--primary 209.8x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li shadow #000000 @ 0.15 0px 4px 8px 0px outline 1px auto #005fcc offset 0px; button::before.button.button--primary 20pxx44px bg #301816; button::after.button.button--primary 20pxx44px bg #301816 |
| How | hovered the card to reveal the quick-add form | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `quick-add-default.png`, `quick-add-hover.png`, `quick-add-focus-visible.png`, `quick-add-pressed.png`.

#### sort-control

Sort control. A sort/filter control on the collection grid, if one paints.

Page: shop. Selector: `shop select`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 71.2 x 44 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | 1px solid #301816 | = | = | = |
| Radius | 999px | = | = | = |
| Background | #301816 | = | = | = |
| Box shadow | none | #000000 @ 0.15 0px 4px 8px 0px | = | #000000 @ 0.15 0px 4px 8px 0px |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Robin Semibold 12px/14.4px 500 | = | = | = |
| Letter spacing | 0.96px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | transform, box-shadow 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | matrix(1, 0, 0, 1, 0, -2) | = | matrix(1, 0, 0, 1, 0, -2) |
| Cursor | pointer | = | = | = |
| ::before | 20px x 100%, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| ::after | 20px x 100%, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.tabs-nav__item.button 71.2x44.0 bg #301816 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 999px | button.tabs-nav__item.button 71.2x44.0 bg #301816 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 999px shadow #000000 @ 0.15 0px 4px 8px 0px | button.tabs-nav__item.button 71.2x44.0 bg #301816 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 999px outline 1px auto #005fcc offset 0px | button.tabs-nav__item.button 71.2x44.0 bg #301816 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 999px shadow #000000 @ 0.15 0px 4px 8px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sort-control-default.png`, `sort-control-hover.png`, `sort-control-focus-visible.png`, `sort-control-pressed.png`.

#### pagination

Pagination. The grid's pagination, if the catalogue is long enough to need one.

Page: shop. Selector: `pagination`. States: none.

Not found on the page at capture time.

#### product-card-pack

Card pack line. The "6 canettes 25cl" pack description under the wordmark, h5 style.

Page: shop. Selector: `.product-item__info-wrapper .h5`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 252.56 x 14.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Robin Semibold 12px/14.4px 600 |
| Letter spacing | 0.96px |
| Colour | #301816 |
| Transition | none |
| How | at rest |

Crops: `product-card-pack-default.png`.

### Product page

#### pdp-media

Product media. The packshot gallery left of the buy box.

Page: product. Selector: `.product__media`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 695 x 810 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Robin Regular 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #301816 |
| Transition | none |
| Icon | 0 x 0, colour #301816 |
| Painted layers | div.product__media-image-wrapper 695.0x810.0 bg #f6f2e9; div.product__media-image-wrapper 695.0x810.0 bg #f6f2e9; div.product__media-image-wrapper 695.0x810.0 bg #f6f2e9; button.dots-nav__item.tap-area 0.0x0.0 bg #301816; button.dots-nav__item.tap-area 0.0x0.0 bg #301816; button.dots-nav__item.tap-area 0.0x0.0 bg #301816 |
| How | at rest |

Crops: `pdp-media-default.png`.

#### pdp-title

Product title. The 60px Boogy flavour title in the buy box.

Page: product. Selector: `.product-item__title-wrapper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 403.33 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Boogy 60px/39px 500 |
| Letter spacing | normal |
| Colour | #301816 |
| Transition | none |
| How | at rest |

Crops: `pdp-title-default.png`.

#### pdp-price

Price. The selling price figure (21.00€ for a 6-pack).

Page: product. Selector: `[data-product-price-list] .price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 23.48 x 14.39 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Robin Semibold 12px/14.4px 600 |
| Letter spacing | 0.96px |
| Colour | #ffffff |
| Text node | span.product-form__current-price: Robin Semibold 12px/14.4px 700, #ffffff, ls 0.96px |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `pdp-price-default.png`.

#### variant-swatch

Pack-size swatch (checked). The checked "6 Canettes" block-swatch radio label.

Page: product. Selector: `label.block-swatch__item "6 CANETTES"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106.19 x 36.39 | = | - | = |
| Padding | 10px | = | - | = |
| Border | 1px solid #301816 | = | - | = |
| Radius | 999px | = | - | = |
| Background | #f26554 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Robin Semibold 12px/14.4px 600 | = | - | = |
| Letter spacing | 0.96px | = | - | = |
| Colour | #301816 | = | - | = |
| Transition | background 0.2s ease | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | label.block-swatch__item.h5 106.2x36.4 bg #f26554 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 999px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `variant-swatch-default.png`, `variant-swatch-hover.png`, `variant-swatch-pressed.png`.

#### variant-swatch-2

Pack-size swatch. An unchecked block-swatch option (12 Canettes); one was toggled selected for the state shots, never added to the cart.

Page: product. Selector: `label.block-swatch__item "12 CANETTES"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 111.83 x 36.39 | = | - | = |
| Padding | 10px | = | - | = |
| Border | 1px solid #301816 | = | - | = |
| Radius | 999px | = | - | = |
| Background | #ffffff | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Robin Semibold 12px/14.4px 600 | = | - | = |
| Letter spacing | 0.96px | = | - | = |
| Colour | #301816 | = | - | = |
| Transition | background 0.2s ease | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | label.block-swatch__item.h5 111.8x36.4 bg #ffffff border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 999px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `variant-swatch-2-default.png`, `variant-swatch-2-hover.png`, `variant-swatch-2-pressed.png`.

#### swatch-selected

Swatch, newly selected. The 24-Canettes swatch in its selected state, reached by the swatch's own click.

Page: product. Selector: `selected block-swatch`. States: selected.

| Property | selected |
|---|---|
| Size (w x h) | 113.8 x 36.39 |
| Padding | 10px |
| Border | 1px solid #301816 |
| Radius | 999px |
| Background | #f26554 |
| Box shadow | none |
| Outline | none |
| Font | Robin Semibold 12px/14.4px 600 |
| Letter spacing | 0.96px |
| Colour | #301816 |
| Transition | background 0.2s ease |
| Cursor | pointer |
| Painted layers | label.block-swatch__item.h5 113.8x36.4 bg #f26554 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 999px |
| How | own toggle |

Crops: `swatch-selected-selected.png`.

#### add-to-cart

Add to cart button. The "Ajouter au panier — 21€" submit; measured, never pressed — a press posts to /cart/add.

Page: product. Selector: `.product-form__add-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 380 x 44 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #301816 | = | = | = |
| Background image | linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), linear-gradient(#301816, #301816) | = | = | = |
| Box shadow | none | #000000 @ 0.15 0px 4px 8px 0px | = | #000000 @ 0.15 0px 4px 8px 0px |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Robin Semibold 12px/14.4px 500 | = | = | = |
| Letter spacing | 0.96px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.product-form__add-button-text: Robin Semibold 12px/14.4px 500, #ffffff, ls 0.96px | = | = | = |
| Transition | transform, box-shadow 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | matrix(1, 0, 0, 1, 0, -2) | = | matrix(1, 0, 0, 1, 0, -2) |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #ffffff, fill #000000 | = | = | = |
| ::before | 20px x 44px, absolute, bg #301816, radius 0px | = | = | = |
| ::after | 20px x 44px, absolute, bg #301816, radius 0px | = | = | = |
| Painted layers | button.product-form__add-button.button 380.0x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li; button::before.product-form__add-button.button 20pxx44px bg #301816; button::after.product-form__add-button.button 20pxx44px bg #301816 | button.product-form__add-button.button 380.0x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li shadow #000000 @ 0.15 0px 4px 8px 0px; button::before.product-form__add-button.button 20pxx44px bg #301816; button::after.product-form__add-button.button 20pxx44px bg #301816 | button.product-form__add-button.button 380.0x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li outline 1px auto #005fcc offset 0px; button::before.product-form__add-button.button 20pxx44px bg #301816; button::after.product-form__add-button.button 20pxx44px bg #301816 | button.product-form__add-button.button 380.0x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li shadow #000000 @ 0.15 0px 4px 8px 0px; button::before.product-form__add-button.button 20pxx44px bg #301816; button::after.product-form__add-button.button 20pxx44px bg #301816 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `add-to-cart-default.png`, `add-to-cart-hover.png`, `add-to-cart-focus-visible.png`, `add-to-cart-pressed.png`.

#### reassurance

Reassurance line. A trust line under the buy button ("livraison à J+2…"), dusk text with a flavour-coloured divider.

Page: product. Selector: `.product-info__reassurance-item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 245.11 x 26.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Robin Semibold 11px/13.2px 500 |
| Letter spacing | 0.96px |
| Colour | #301816 |
| Text node | p: Robin Semibold 11px/13.2px 500, #301816, ls 0.96px |
| Transition | none |
| How | at rest |

Crops: `reassurance-default.png`.

#### reviews-tab

Reviews tab. A Klaviyo-reviews tab ("Avis" / "Écrire un avis") — a vendor widget painted in the theme's chrome.

Page: product. Selector: `.kl_reviews__list__tabs`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1304.69 x 52 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 24px | = | = | = |
| Border | T: none; R: none; B: 1px solid #e9e9eb; L: none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Robin Regular 16px/19.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #301816 | = | = | = |
| Text node | button.kl_reviews__button: Robin Regular 12px/15px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Painted layers | div.kl_reviews__list__tabs 1304.7x52.0 border B:1px solid #e9e9eb; button.kl_reviews__button 89.7x31.0 bg #301816 r 8px; button::after.kl_reviews__list__tab.kl_reviews__list__tab--active 71.625pxx5px bg #212b37 r 5px | = | div.kl_reviews__list__tabs 1304.7x52.0 border B:1px solid #e9e9eb; button.kl_reviews__button 89.7x31.0 bg #301816 r 8px outline 3px solid #212b37 offset 1px; button::after.kl_reviews__list__tab.kl_reviews__list__tab--active 71.625pxx5px bg #212b37 r 5px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `reviews-tab-default.png`, `reviews-tab-hover.png`, `reviews-tab-focus-visible.png`, `reviews-tab-pressed.png`.

#### sort-select

Review sort select. The Klaviyo reviews sort <select> — the one native select that paints signed out.

Page: product. Selector: `select#kl_reviews__sort_by_reviews`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 152 x 35.98 | = | = | = |
| Padding | 8px 36px 8px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | #301816 @ 0.1 | = | #170b0a @ 0.19 | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Robin Regular 12.04px/19.9864px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #301816 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | select 152.0x36.0 bg #301816 @ 0.1 r 24px | = | select 152.0x36.0 bg #170b0a @ 0.19 r 24px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sort-select-default.png`, `sort-select-hover.png`, `sort-select-focus-visible.png`, `sort-select-pressed.png`.

#### trio-title

Bundle title. The Trio Douze buy-box title.

Page: trio. Selector: `trio .product-item__title-wrapper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 403.33 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Boogy 60px/39px 500 |
| Letter spacing | normal |
| Colour | #301816 |
| Transition | none |
| How | at rest |

Crops: `trio-title-default.png`.

#### subscription-radio

Purchase-option radio. The one-off vs. subscription radio in the buy box (it renders after the pack-size is settled, seen in the variant shot); never toggled past the default.

Page: trio. Selector: `label "ACHAT UNIQUE"`. States: none.

Not found on the page at capture time.

### Content pages

#### faq-title

Page title. The "Page FAQ" heading — the page is a stub with no accordion painted signed out.

Page: faq. Selector: `faq .heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 850 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Boogy 52px/52px 300 |
| Letter spacing | -0.52px |
| Colour | #301816 |
| Transition | none |
| How | at rest |

Crops: `faq-title-default.png`.

#### accordion

Accordion. A disclosure row, where one paints (none on the FAQ stub).

Page: faq. Selector: `details`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 632.34 x 57 | = | = | = |
| Padding | 21px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Robin Semibold 12px/14.4px 600 | = | = | = |
| Letter spacing | 0.96px | = | = | = |
| Colour | #301816 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span::before.animated-plus 15pxx1px bg #301816; span::after.animated-plus 1pxx15px bg #301816 | = | button.collapsible-toggle.h5 632.3x57.0 outline 1px auto #005fcc offset 0px; span::before.animated-plus 15pxx1px bg #301816; span::after.animated-plus 1pxx15px bg #301816 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `accordion-default.png`, `accordion-hover.png`, `accordion-focus-visible.png`, `accordion-pressed.png`.

#### story-h1

Story title. The Notre-histoire page heading.

Page: story. Selector: `story .heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 524.13 x 104 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Boogy 52px/52px 300 |
| Letter spacing | -0.52px |
| Colour | #f6f2e9 |
| Text node | p: Boogy 52px/52px 300, #f6f2e9, ls -0.52px |
| Transition | none |
| How | at rest |

Crops: `story-h1-default.png`.

#### story-lede

Story paragraph. A body paragraph in the story page, Robin Regular.

Page: story. Selector: `story p`. States: none.

Mismeasured on the first pass and withdrawn: the selector caught the announcement-strip paragraph ("LIVRAISON GRATUITE EN FRANCE METROPOLITAINE A PARTIR DE 50EUR"), not a story body paragraph — no story paragraph was measured. The selector was tightened in tools/capture/public/measure.mjs; a live re-measure is queued.

#### search-title

Search title. The search results heading for ?q=douze.

Page: search. Selector: `search .heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 704 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Boogy 52px/52px 300 |
| Letter spacing | -0.52px |
| Colour | #301816 |
| Transition | none |
| How | at rest |

Crops: `search-title-default.png`.

#### search-field

Search field. The search page's input, prefilled with "douze"; never re-submitted.

Page: search. Selector: `input[name="q"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 390 x 80 | = |
| Padding | 0px 80px 0px 30px | = |
| Border | 1px solid #301816 | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | #301816 0px 0px 0px 1px inset |
| Outline | none | = |
| Font | Robin Semibold 16px/19.2px 500 | = |
| Letter spacing | 0.96px | = |
| Colour | #301816 | = |
| Transition | border, box-shadow 0.2s, 0.2s ease-in-out, ease-in-out delay 0s, 0s | = |
| Cursor | text | = |
| Placeholder | #301816 @ 0.7, opacity 1 | = |
| Painted layers | input.main-search__input.input__field 390.0x80.0 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 | input.main-search__input.input__field 390.0x80.0 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 shadow #301816 0px 0px 0px 1px inset |
| How | at rest | clicked into the field |

Crops: `search-field-default.png`, `search-field-focused.png`.

#### search-result

Search result card. A product result in the search grid.

Page: search. Selector: `search product-item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 229.25 x 286.56 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 45px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Robin Regular 16px/19.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #301816 | = | = | = |
| Text node | p.h5: Robin Semibold 12px/14.4px 600, #301816, ls 0.96px | label.product-item__block-swatch: Robin Semibold 12px/14.4px 600, #301816, ls 0.96px | = | - |
| Transition | none | = | = | = |
| Icon | 0 x 0, colour #ffffff, fill #000000 | = | = | = |
| Painted layers | label.product-item__block-swatch 111.8x32.4 bg #d1e8f5 border T:1px solid #321a18 / R:1px solid #321a18 / B:1px solid #321a18 / L:1px solid #321a18 r 3.35544e+07px; label.product-item__block-swatch 113.8x32.4 bg #ffffff border T:1px solid #321a18 / R:1px solid #321a18 / B:1px solid #321a18 / L:1px solid #321a18 r 3.35544e+07px; button.button.button--primary 209.3x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li; button::before.button.button--primary 20pxx44px bg #301816; button::after.button.button--primary 20pxx44px bg #301816 | label.product-item__block-swatch 111.8x32.4 bg #d1e8f5 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 3.35544e+07px; label.product-item__block-swatch 113.8x32.4 bg #ffffff border T:1px solid #321a18 / R:1px solid #321a18 / B:1px solid #321a18 / L:1px solid #321a18 r 3.35544e+07px; button.button.button--primary 209.3x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li; button::before.button.button--primary 20pxx44px bg #301816; button::after.button.button--primary 20pxx44px bg #301816 | a 0.0x0.0 outline 1px auto #005fcc offset 1px; label.product-item__block-swatch 111.8x32.4 bg #d1e8f5 border T:1px solid #321a18 / R:1px solid #321a18 / B:1px solid #321a18 / L:1px solid #321a18 r 3.35544e+07px; label.product-item__block-swatch 113.8x32.4 bg #ffffff border T:1px solid #321a18 / R:1px solid #321a18 / B:1px solid #321a18 / L:1px solid #321a18 r 3.35544e+07px; button.button.button--primary 209.3x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li; button::before.button.button--primary 20pxx44px bg #301816; button::after.button.button--primary 20pxx44px bg #301816 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-result-default.png`, `search-result-hover.png`, `search-result-focus-visible.png`, `search-result-pressed.png`.

### Account and cart

#### login-card

Login card. The centred customer-login card; never filled or submitted.

Page: login. Selector: `.customer-form-card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 481.56 |
| Padding | 44px 48px |
| Border | none |
| Radius | 45px |
| Background | #f6f2e9 |
| Box shadow | none |
| Outline | none |
| Font | Robin Regular 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #301816 |
| Text node | h1.customer-form-card__title.heading: Boogy Italic 72px/86.4px 300, #301816 |
| Transition | none |
| Painted layers | div.customer-form-card.login-form-container 480.0x481.6 bg #f6f2e9 r 45px; input.input__field 384.0x52.0 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 16px; label.input__label 1.0x1.0 bg #ffffff; input.input__field 384.0x52.0 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 16px; label.input__label 1.0x1.0 bg #ffffff; button.form__submit.button 384.0x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li |
| How | at rest |

Crops: `login-card-default.png`.

#### email-field

Email field. The E-mail input with its floating label; sample text was typed and deleted, nothing sent.

Page: login. Selector: `input[name="customer[email]"]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 384 x 52 | = | = |
| Padding | 0px 18px | = | = |
| Border | 1px solid #301816 | = | = |
| Radius | 16px | = | = |
| Background | transparent | = | = |
| Box shadow | none | #301816 0px 0px 0px 1px inset | #301816 0px 0px 0px 1px inset |
| Outline | none | = | = |
| Font | Robin Semibold 12px/14.4px 500 | = | = |
| Letter spacing | 0.96px | = | = |
| Colour | #301816 | = | = |
| Transition | border, box-shadow 0.2s, 0.2s ease-in-out, ease-in-out delay 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | #301816 @ 0.6, opacity 1 | = | = |
| Painted layers | input.input__field 384.0x52.0 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 16px | input.input__field 384.0x52.0 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 16px shadow #301816 0px 0px 0px 1px inset | input.input__field.is-filled 384.0x52.0 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 16px shadow #301816 0px 0px 0px 1px inset |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `email-field-default.png`, `email-field-focused.png`, `email-field-filled.png`.

#### password-field

Password field. The Mot-de-passe input; focused only, never filled.

Page: login. Selector: `input[name="customer[password]"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 384 x 52 | = |
| Padding | 0px 18px | = |
| Border | 1px solid #301816 | = |
| Radius | 16px | = |
| Background | transparent | = |
| Box shadow | none | #301816 0px 0px 0px 1px inset |
| Outline | none | = |
| Font | Robin Semibold 12px/14.4px 500 | = |
| Letter spacing | 0.96px | = |
| Colour | #301816 | = |
| Transition | border, box-shadow 0.2s, 0.2s ease-in-out, ease-in-out delay 0s, 0s | = |
| Cursor | text | = |
| Placeholder | #301816 @ 0.6, opacity 1 | = |
| Painted layers | input.input__field 384.0x52.0 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 16px | input.input__field 384.0x52.0 border T:1px solid #301816 / R:1px solid #301816 / B:1px solid #301816 / L:1px solid #301816 r 16px shadow #301816 0px 0px 0px 1px inset |
| How | at rest | clicked into the field |

Crops: `password-field-default.png`, `password-field-focused.png`.

#### login-button

Login button. The Se-connecter submit; measured, never pressed (a press would submit).

Page: login. Selector: `form button "Se connecter"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 384 x 44 | = | = | = |
| Padding | 0px 15px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #301816 | = | = | = |
| Background image | linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), linear-gradient(#301816, #301816) | = | = | = |
| Box shadow | none | = | = | #000000 @ 0.15 0px 4px 8px 0px |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Robin Semibold 12px/14.4px 500 | = | = | = |
| Letter spacing | 0.96px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | transform, box-shadow 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | matrix(1, 0, 0, 1, 0, -2) |
| Cursor | pointer | = | = | = |
| ::before | 20px x 44px, absolute, bg #301816, radius 0px | = | = | = |
| ::after | 20px x 44px, absolute, bg #301816, radius 0px | = | = | = |
| Painted layers | button.form__submit.button 384.0x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li; button::before.form__submit.button 20pxx44px bg #301816; button::after.form__submit.button 20pxx44px bg #301816 | = | button.form__submit.button 384.0x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li outline 1px auto #005fcc offset 0px; button::before.form__submit.button 20pxx44px bg #301816; button::after.form__submit.button 20pxx44px bg #301816 | button.form__submit.button 384.0x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li shadow #000000 @ 0.15 0px 4px 8px 0px; button::before.form__submit.button 20pxx44px bg #301816; button::after.form__submit.button 20pxx44px bg #301816 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-button-default.png`, `login-button-hover.png`, `login-button-focus-visible.png`, `login-button-pressed.png`.

#### recover-link

Recover toggle. The "Mot de passe oublié ?" button — it swaps the card to the recover form in place; measured, and the swap itself captured as a state.

Page: login. Selector: `button "Mot de passe oublié"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 163.78 x 14.39 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Robin Regular 12px/14.4px 500 | = | = | = |
| Letter spacing | 0.96px | = | = | = |
| Colour | #301816 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.customer-form-card__forgot-link 163.8x14.4 outline 1px auto #005fcc offset 0px | = |

Crops: `recover-link-default.png`, `recover-link-hover.png`, `recover-link-focus-visible.png`, `recover-link-pressed.png`.

#### cart-empty

Cart, empty. The "Votre panier est vide" empty state — the only cart surface reachable without adding an item.

Page: cart. Selector: `.empty-state`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1162.22 x 197.98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Robin Regular 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #301816 |
| Text node | h1.heading.h1: Boogy 72px/64.8px 300, #301816, ls -0.72px |
| Transition | none |
| Painted layers | a.button.button--primary 1162.2x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li; a::before.button.button--primary 20pxx44px bg #301816; a::after.button.button--primary 20pxx44px bg #301816 |
| How | at rest |

Crops: `cart-empty-default.png`.

#### cart-cta

Empty-cart CTA. The "Explorer nos produits" action in the empty state.

Page: cart. Selector: `.empty-state .button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1162.22 x 44 | = | = | = |
| Padding | 0px 15px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #301816 | = | = | = |
| Background image | linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), linear-gradient(#301816, #301816) | = | = | = |
| Box shadow | none | #000000 @ 0.15 0px 4px 8px 0px | = | #000000 @ 0.15 0px 4px 8px 0px |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Robin Semibold 12px/14.4px 500 | = | = | = |
| Letter spacing | 0.96px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | transform, box-shadow 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | matrix(1, 0, 0, 1, 0, -2) | = | matrix(1, 0, 0, 1, 0, -2) |
| Cursor | pointer | = | = | = |
| ::before | 20px x 44px, absolute, bg #301816, radius 0px | = | = | = |
| ::after | 20px x 44px, absolute, bg #301816, radius 0px | = | = | = |
| Painted layers | a.button.button--primary 1162.2x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li; a::before.button.button--primary 20pxx44px bg #301816; a::after.button.button--primary 20pxx44px bg #301816 | a.button.button--primary 1162.2x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li shadow #000000 @ 0.15 0px 4px 8px 0px; a::before.button.button--primary 20pxx44px bg #301816; a::after.button.button--primary 20pxx44px bg #301816 | a.button.button--primary 1162.2x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li outline 1px auto #005fcc offset 1px; a::before.button.button--primary 20pxx44px bg #301816; a::after.button.button--primary 20pxx44px bg #301816 | a.button.button--primary 1162.2x44.0 bg #301816 image linear-gradient(178deg, #301816, #301816 10%, #000000 @ 0.07 10%, #000000 @ 0.07 100%), li shadow #000000 @ 0.15 0px 4px 8px 0px; a::before.button.button--primary 20pxx44px bg #301816; a::after.button.button--primary 20pxx44px bg #301816 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cart-cta-default.png`, `cart-cta-hover.png`, `cart-cta-focus-visible.png`, `cart-cta-pressed.png`.

#### register-link

Register link. The "S'inscrire" link to /account/register.

Page: login. Selector: `a[href*="register"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 74.17 x 14.39 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Robin Regular 12px/14.4px 500 | = | = | = |
| Letter spacing | 0.96px | = | = | = |
| Colour | #301816 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.customer-form-card__footer-link 74.2x14.4 outline 1px auto #005fcc offset 1px | = |

Crops: `register-link-default.png`, `register-link-hover.png`, `register-link-focus-visible.png`, `register-link-pressed.png`.

### Footer

#### footer

Footer. The boxed footer section over its photo background: nav columns, the "La News Douze" Klaviyo signup and the locale selector.

Page: home. Selector: `footer.footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1390 x 903.17 |
| Padding | 20px 0px |
| Border | none |
| Radius | 45px |
| Background | #f6f2e9 |
| Background image | url(…) |
| Box shadow | none |
| Outline | none |
| Font | Robin Regular 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #301816 |
| Text node | a.h5: Robin Semibold 12px/14.4px 600, #f6f2e9, ls 0.96px |
| Transition | none |
| Icon | 220 x 66, colour #f6f2e9, fill #000000 |
| Painted layers | footer.section.footer 1390.0x903.2 bg #f6f2e9 r 45px; form.needsclick.klaviyo-form 450.0x50.0 bg #ffffff @ 0; input.needsclick.go3414965134 450.0x34.0 bg #ffffff @ 0 border B:1px solid #f6f2e9; button.needsclick.go3038017783 32.0x34.0 bg #26853b @ 0; input 0.0x0.0 border B:1px solid #f6f2e9; div.footer__bottom 1342.0x536.3 border T:1px solid #f6f2e9 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer nav link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 37.69 x 15 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Robin Semibold 12px/14.4px 600 | = | = | = |
| Letter spacing | 0.96px | = | = | = |
| Colour | #f6f2e9 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.h5 37.7x15.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### newsletter-field

Newsletter field. The email input inside the footer's Klaviyo embed; focused only, never filled or submitted.

Page: home. Selector: `.klaviyo-form input[type=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 450 x 34 | = |
| Padding | 0px | = |
| Border | T: none; R: none; B: 1px solid #f6f2e9; L: none | = |
| Radius | 0px | = |
| Background | #ffffff @ 0 | = |
| Box shadow | none | = |
| Outline | none | 2px auto #f6f2e9 offset 0px |
| Font | Robin Semibold 12px/14.4px 400 | = |
| Letter spacing | 0.96px | = |
| Colour | #f6f2e9 | = |
| Transition | none | = |
| Placeholder | #f6f2e9, opacity 1 | = |
| Painted layers | input.needsclick.go3414965134 450.0x34.0 bg #ffffff @ 0 border B:1px solid #f6f2e9 | input.needsclick.go3414965134 450.0x34.0 bg #ffffff @ 0 border B:1px solid #f6f2e9 outline 2px auto #f6f2e9 offset 0px |
| How | at rest | clicked into the field |

Crops: `newsletter-field-default.png`, `newsletter-field-focused.png`.

#### newsletter-button

Newsletter button. The signup submit inside the Klaviyo embed; measured, never pressed.

Page: home. Selector: `.klaviyo-form button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 34 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #26853b @ 0 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px auto #f6f2e9 offset 0px | = |
| Font | Nunito-Sans-Klaviyo-Hosted 20px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f6f2e9 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.needsclick.go3038017783 32.0x34.0 bg #26853b @ 0 | = | button.needsclick.go3038017783 32.0x34.0 bg #26853b @ 0 outline 2px auto #f6f2e9 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `newsletter-button-default.png`, `newsletter-button-hover.png`, `newsletter-button-focus-visible.png`, `newsletter-button-pressed.png`.

#### social-icon

Social icon link. A social link, where the footer paints one (none in the captured DOM).

Page: home. Selector: `footer social a`. States: none.

Not found on the page at capture time.

#### locale-button

Locale button. The FRANÇAIS locale selector in the footer.

Page: home. Selector: `footer locale button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 110.77 x 26.39 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Robin Semibold 12px/14.4px 600 | = | = | = |
| Letter spacing | 0.96px | = | = | = |
| Colour | #f6f2e9 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 9 x 6, colour #f6f2e9, fill #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.select.select--small 110.8x26.4 outline 1px auto #005fcc offset 0px | = |

Crops: `locale-button-default.png`, `locale-button-hover.png`, `locale-button-focus-visible.png`, `locale-button-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The compact header at 390: hamburger, wordmark, cart.

Page: mobile. Selector: `store-header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 65 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Robin Regular 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #301816 |
| Text node | cart-count.header__cart-count.header__cart-count--floating: Robin Regular 9px/8.55px 600, #f6f2e9 |
| Transition | background, color, box-shadow 0.2s, 0.2s, 0.2s ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s |
| Icon | 18 x 14, colour #301816, fill #000000 |
| Painted layers | a::after.header__linklist-link.link--animated 100%x1px bg #301816; a::after.header__linklist-link.link--animated 100%x1px bg #301816; a::after.header__linklist-link.link--animated 100%x1px bg #301816; a::after.header__linklist-link.link--animated 100%x1px bg #301816; a::after.header__linklist-link.link--animated 100%x1px bg #301816; a::after.header__linklist-link.link--animated 100%x1px bg #301816 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The hamburger toggle for the mobile-navigation drawer.

Page: mobile. Selector: `button[aria-controls="mobile-menu-drawer"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 18 x 14 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Robin Regular 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #301816 |
| Transition | none |
| Cursor | pointer |
| Icon | 18 x 14, colour #301816, fill #000000 |
| ::before | 30px x 26px, absolute, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The from-left navigation drawer opened by its own toggle.

Page: mobile. Selector: `mobile-navigation`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Robin Regular 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #301816 |
| Text node | a.mobile-nav__link.heading: Robin Semibold 12px/13.44px 300, #301816, ls 0.96px |
| Transition | transform, visibility 0.6s, 0.6s cubic-bezier(0.75, 0, 0.175, 1), cubic-bezier(0.75, 0, 0.175, 1) delay 0s, 0s |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 14 x 14, colour #301816, fill #000000 |
| Painted layers | mobile-navigation.drawer.drawer--from-left 390.0x844.0 bg #ffffff; span.drawer__overlay 390.0x844.0 bg #000000; div.drawer__header.drawer__header--shadowed 390.0x52.0 bg #ffffff; div.drawer__footer.drawer__footer--tight 390.0x66.0 border T:1px solid #301816 @ 0.12 shadow #321a18 0px 1px 0px 0px inset; div::before.drawer__footer.drawer__footer--tight 390pxx24px image linear-gradient(#ffffff @ 0, #ffffff) |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. A link inside the opened navigation drawer.

Page: mobile. Selector: `mobile-navigation a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 390 x 45.44 | = | = | = |
| Padding | 16px 40px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Robin Semibold 12px/13.44px 300 | = | = | = |
| Letter spacing | 0.96px | = | = | = |
| Colour | #301816 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.mobile-nav__link.heading 390.0x45.4 outline 1px auto #005fcc offset 1px | = |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero-title

Mobile hero title. The Boogy hero heading at 390 (the hidden-tablet-and-up variant).

Page: mobile. Selector: `.image-hero__heading at 390`. States: none.

Mismeasured on the first pass and withdrawn: the selector caught the hero SHOP button container, not the mobile Boogy heading — the 390px hero heading was not measured. The selector was tightened in tools/capture/public/measure.mjs; a live re-measure is queued.

#### m-hero-cta

Mobile hero CTA. The SHOP button at 390.

Page: mobile. Selector: `.image-hero__button at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 77.69 x 38 |
| Padding | 0px 20px |
| Border | none |
| Radius | 0px |
| Background | #301816 |
| Box shadow | none |
| Outline | none |
| Font | Robin Semibold 12px/14.4px 500 |
| Letter spacing | 0.96px |
| Colour | #ffffff |
| Transition | transform, box-shadow 0.2s, 0.2s ease, ease delay 0s, 0s |
| Cursor | pointer |
| ::before | 20px x 38px, absolute, bg #301816, radius 0px |
| ::after | 20px x 38px, absolute, bg #301816, radius 0px |
| Painted layers | a.button.button--primary 77.7x38.0 bg #301816; a::before.button.button--primary 20pxx38px bg #301816; a::after.button.button--primary 20pxx38px bg #301816 |
| How | at rest |

Crops: `m-hero-cta-default.png`.

#### m-product-card

Mobile product card. A product-item in the featured row at 390.

Page: mobile. Selector: `product-item at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 316 x 395 |
| Padding | 0px |
| Border | none |
| Radius | 22.5px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Robin Regular 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #301816 |
| Text node | p.h5: Robin Semibold 12px/14.4px 600, #301816, ls 0.96px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 5.99359) |
| Opacity | 0.828755 |
| Icon | 0 x 0, colour #ffffff, fill #000000 |
| Painted layers | button.button.button--primary 219.8x38.0 bg #301816; button::before.button.button--primary 20pxx38px bg #301816; button::after.button.button--primary 20pxx38px bg #301816 |
| How | at rest |

Crops: `m-product-card-default.png`.

## Transitions declared in the readable stylesheets

drinkdouze.com serves its theme.css and douze-custom.css same-origin (the checkout-button sheet is cross-origin and was read from network responses), so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- home: `0.3s`, `opacity 333ms cubic-bezier(0.4, 0, 0.22, 1)`, `transform 333ms cubic-bezier(0.4, 0, 0.22, 1)`, `none`, `opacity 0.25s ease-in-out 0.2s, transform 0.25s ease-in-out`, `transform 0.25s ease-in-out`, `visibility 0.2s linear`, `text-decoration-color 0.2s ease-in-out, color 0.2s ease-in-out, -webkit-text-decoration-color 0.2s ease-in-out`, `transform 0.3s`, `opacity 0.25s ease-in-out`, `opacity 0.2s ease-in-out`, `transform 0.4s ease-in-out, opacity 0.4s ease-in-out`

- product: `0.3s`, `opacity 333ms cubic-bezier(0.4, 0, 0.22, 1)`, `transform 333ms cubic-bezier(0.4, 0, 0.22, 1)`, `none`, `opacity 0.25s ease-in-out 0.2s, transform 0.25s ease-in-out`, `transform 0.25s ease-in-out`, `visibility 0.2s linear`, `text-decoration-color 0.2s ease-in-out, color 0.2s ease-in-out, -webkit-text-decoration-color 0.2s ease-in-out`, `transform 0.3s`, `opacity 0.25s ease-in-out`, `opacity 0.2s ease-in-out`, `transform 0.4s ease-in-out, opacity 0.4s ease-in-out`

- shop: `0.3s`, `opacity 333ms cubic-bezier(0.4, 0, 0.22, 1)`, `transform 333ms cubic-bezier(0.4, 0, 0.22, 1)`, `none`, `opacity 0.25s ease-in-out 0.2s, transform 0.25s ease-in-out`, `transform 0.25s ease-in-out`, `visibility 0.2s linear`, `text-decoration-color 0.2s ease-in-out, color 0.2s ease-in-out, -webkit-text-decoration-color 0.2s ease-in-out`, `transform 0.3s`, `opacity 0.25s ease-in-out`, `opacity 0.2s ease-in-out`, `transform 0.4s ease-in-out, opacity 0.4s ease-in-out`
