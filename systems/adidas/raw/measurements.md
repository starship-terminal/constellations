# Component measurements

Computed styles read from adidas.com.cn on  by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The sticky top bar every page shares: a utility strip (在线客服, 请登录), the adidas wordmark, the category nav and the campaign tag strip.

Page: home. Selector: `.navigation-warpper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 124 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p: AdihausDIN 13px/18px 400, #ffffff, ls 0.5px |
| Transition | all 0.3s ease-in |
| Painted layers | section.navigation-warpper.showheaderBar 1440.0x124.0 bg #ffffff; div.notification.flex 1440.0x40.0 bg #000000; p::after.gap-space 1pxx20px bg #eceff1; div.pc-navigation-bar 1440.0x84.0 border B:1px solid #eceff1; div.search-bar-box.cursor-pointer 261.3x32.0 bg #f9f9f9; div.search-overlay.hide-overlay 0.0x0.0 bg #ffffff |
| How | at rest |

Crops: `header-default.png`.

#### nav-item

Nav item. A top-level category item (男装, 男鞋, 女装, 女鞋, 儿童, 配件).

Page: home. Selector: `.catalog-item-first-page`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 47 x 84 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | AdihausDIN 15px/20px 700 | = | = | = |
| Letter spacing | 0.5px | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.cursor-pointer: AdihausDIN 15px/20px 700, #000000, ls 0.5px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | focus failed | CDP forcePseudoState :active:hover |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`.

#### utility-link

Utility link. A utility-strip entry (在线客服 online service, 请登录 sign in).

Page: home. Selector: `.online`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 74 x 38 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | AdihausDIN 13px/18px 400 | = | = | = |
| Letter spacing | 0.5px | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | p: AdihausDIN 13px/18px 400, #ffffff, ls 0.5px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | focus failed | CDP forcePseudoState :active:hover |

Crops: `utility-link-default.png`, `utility-link-hover.png`, `utility-link-focus-visible.png`, `utility-link-pressed.png`.

#### promo-tag

Promo tag. A campaign tag in the strip under the nav (11.11 不止5折, 雪境漫游, 降温毛衣精选).

Page: home. Selector: `promo tag`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 261.33 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #f9f9f9 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.label-4.mr-12: AdihausDIN-Woff 13px/18px 400, #9a9b9b, ls 0.5px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.search-bar-box.cursor-pointer 261.3x32.0 bg #f9f9f9 | = | = | = |
| How | at rest | mouse hover | focus failed | CDP forcePseudoState :active:hover |

Crops: `promo-tag-default.png`, `promo-tag-hover.png`, `promo-tag-focus-visible.png`, `promo-tag-pressed.png`.

#### logo

Wordmark. The adidas wordmark linking home.

Page: home. Selector: `logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 84 x 84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

### Home

#### hero

Hero. The campaign band under the header: photography, a headline and a 立即选购 CTA.

Page: home. Selector: `.feed-com-carousel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 540 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.major.heading-2: adineuePRO 20px/34px 700, #000000, ls 1px |
| Transition | none |
| Painted layers | div.major.heading-2 185.0x34.0 bg #ffffff; div.minor.mt-4 0.0x0.0 bg #ffffff; button.btn.mt-16 200.0x48.0 bg #ffffff; button::before.btn.mt-16 200pxx48px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 |
| How | at rest |

Crops: `hero-default.png`.

#### hero-cta

Primary CTA. A lib-button campaign CTA (立即选购 "Shop now").

Page: home. Selector: `.lib-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 200 x 48 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff | #eceff1 | = | #eceff1 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | AdihausDIN 14px/20px 700 | = | = | = |
| Letter spacing | 2px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 200px x 48px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.btn.mt-16 200.0x48.0 bg #ffffff; button::before.btn.mt-16 200pxx48px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 | button.btn.mt-16 200.0x48.0 bg #eceff1; button::before.btn.mt-16 200pxx48px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 | = | button.btn.mt-16 200.0x48.0 bg #eceff1; button::before.btn.mt-16 200pxx48px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

### Footer

#### footer

Footer. The page foot: link columns and the published service line service line.

Page: home. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 360 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.title.label-1: AdihausDIN 15px/20px 700, #000000, ls 0.5px |
| Transition | none |
| Painted layers | div.px-40.sm:px-0 1440.0x360.0 bg #f9f9f9; div.lib-tooltip-content 108.0x122.0 bg #ffffff; div.lib-tooltip-arrow 8.0x8.0 bg #ffffff; div::before.lib-tooltip-arrow 8pxx8px bg #ffffff; div.lib-tooltip-content 306.0x140.0 bg #ffffff; div.lib-tooltip-arrow 8.0x8.0 bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer link entry.

Page: home. Selector: ``. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 57.8 x 32 | = | = | = |
| Padding | 8px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | AdihausDIN 11px/16px 400 | = | = | = |
| Letter spacing | 0.5px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.label-6 57.8x32.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Catalogue page (PLP)

#### plp-title

Page title. The catalogue page heading.

Page: plp. Selector: ``. States: .

Not found on the page at capture time.

#### filter-row

Filter row. A refinement row in the left filter column (性别 gender, category, price).

Page: plp. Selector: `filter row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 51 x 56 | = | = | = |
| Padding | 19px 24px 19px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | AdihausDIN 13px/18px 400 | = | = | = |
| Letter spacing | 0.5px | = | = | = |
| Colour | #9a9b9b | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.sort-container.sm:ml-16 bg #ffffff | = | = | = |
| How | at rest | mouse hover | focus failed | CDP forcePseudoState :active:hover |

Crops: `filter-row-default.png`, `filter-row-hover.png`, `filter-row-focus-visible.png`, `filter-row-pressed.png`.

#### product-card

Product tile. A product card linking /pdp?articleId=… : image, name, price.

Page: plp. Selector: `a[href*="/pdp"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 338.5 x 454.5 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 0px/0px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span: AdihausDIN 11px/16px 400, #000000, ls 0.5px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.product-card-whole.fill-bg-light-gray 338.5x454.5 bg #eceff1 border T:1px solid #eceff1 / R:1px solid #eceff1 / B:1px solid #eceff1 / L:1px solid #eceff1; li.plp-item-label.text-bg-white 40.3x24.0 bg #ffffff; div.point 2.0x2.0 bg #9a9b9b | div.product-card-whole.fill-bg-light-gray 338.5x454.5 bg #eceff1 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000; li.plp-item-label.text-bg-white 40.3x24.0 bg #ffffff; div.point 2.0x2.0 bg #9a9b9b |
| How | at rest | mouse hover |

Crops: `product-card-default.png`, `product-card-hover.png`.

#### product-card-name

Tile name. The product name inside a tile.

Page: plp. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 312.5 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 0px/0px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.plp-item-article-name.label-3: AdihausDIN 13px/18px 700, #000000, ls 0.5px |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `product-card-name-default.png`.

#### product-card-price

Tile price. The ¥ price inside a tile.

Page: plp. Selector: ``. States: .

Not found on the page at capture time.

### Product page (PDP)

#### pdp-title

Product title. The product name heading.

Page: pdp. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 399.94 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | adineuePRO 24px/30px 700 |
| Letter spacing | 1px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `pdp-title-default.png`.

#### pdp-price

Product price. The ¥ price beside the title.

Page: pdp. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 41.67 x 22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | adineuePRO 18px/22px 700 |
| Letter spacing | 0.5px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `pdp-price-default.png`.

#### add-to-cart

Add-to-cart button. The primary purchase bar (加入购物袋). Measured, never pressed.

Page: pdp. Selector: `lib-button atc`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 399.94 x 48 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | AdihausDIN 14px/20px 700 | = | = | = |
| Letter spacing | 2px | = | = | = |
| Colour | #c8cbcc | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| ::before | 399.938px x 48px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.mt-16.flex 399.9x48.0 bg #ffffff; button::before.mt-16.flex 399.938pxx48px border T:1px solid #c8cbcc / R:1px solid #c8cbcc / B:1px solid #c8cbcc / L:1px solid #c8cbcc | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `add-to-cart-default.png`, `add-to-cart-hover.png`, `add-to-cart-focus-visible.png`, `add-to-cart-pressed.png`.

#### size-cell

Size cell. A size/spec cell on the PDP.

Page: pdp. Selector: ``. States: .

Not found on the page at capture time.

#### accordion

Accordion row. An expandable detail row on the PDP.

Page: pdp. Selector: ``. States: .

Not found on the page at capture time.

### Mobile (390 wide)

#### m-header

Mobile header. The top bar at 390 wide: a search-field pill, no nav row.

Page: home. Selector: `.search-bar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 48 |
| Padding | 4px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.label-4.mr-12: AdihausDIN-Woff 13px/18px 400, #9a9b9b, ls 0.5px |
| Transition | none |
| Painted layers | div.search-bar-box.cursor-pointer 310.0x32.0 bg #f9f9f9 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-burger

Burger button. The menu button on mobile. None is mounted at 390 — the top bar is the search field, so this records a miss rather than an icon glyph.

Page: home. Selector: `menu control`. States: .

Not found on the page at capture time.

## Transitions declared in the readable stylesheets

Every readable stylesheet on each captured page (adidas's Demandware bundles are same-origin); the per-state Transition rows above are computed values.

- home: `opacity 0.25s linear`, `transform 0.25s ease-in-out`, `transform 0.4s`, `transform 0.3s ease-in`, `height 0.25s ease-in-out`, `width 0.1s, opacity 0.4s`, `none`, `transform 0.5s 0.2s`, `1s`, `0.3s ease-in`, `0.1s cubic-bezier(0.3, 0, 0.45, 1)`, `0.2s cubic-bezier(0.2, 0, 0.45, 1)`

- home@390: `opacity 0.25s linear`, `transform 0.25s ease-in-out`, `transform 0.4s`, `transform 0.3s ease-in`, `height 0.25s ease-in-out`, `width 0.1s, opacity 0.4s`, `none`, `transform 0.5s 0.2s`, `1s`, `0.3s ease-in`, `0.1s cubic-bezier(0.3, 0, 0.45, 1)`, `0.2s cubic-bezier(0.2, 0, 0.45, 1)`
