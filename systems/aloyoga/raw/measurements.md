# Component measurements

Computed styles read from aloyoga.com on 2026-11-10 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) in the shop's one light theme, with the Osano consent dialog hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### promo-strip

Promo strip. The thin bar above the header linking the current offer.

Page: home. Selector: `a:has-text("JOIN TO SHOP")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 102.86 x 17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | proxima-nova 14px/19.6px 600 |
| Letter spacing | 0.7px |
| Colour | #ffffff |
| Text node | span: proxima-nova 14px/19.6px 600, #ffffff, ls 0.7px |
| Transition | color 0.3s ease |
| Cursor | pointer |
| How | at rest |

Crops: `promo-strip-default.png`.

#### header

Header. The white bar: wordmark, WOMEN/MEN/SHOES nav, search, account, bag.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | proxima-nova 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.main-nav__item.hover-target: proxima-nova 18px/normal 500, #000000, ls 0.9px |
| Transition | none |
| Icon | 71 x 48, colour #000000 |
| Painted layers | div.desktop-nav.row 1440.0x84.0 border B:1px solid #dedede; div.container-fluid.main-navbar__sub-items 1440.0x15.0 bg #ffffff; div.row.no-gutters 1350.0x570.2 border T:1px solid #dedede / B:1px solid #dedede; div.container-fluid.main-navbar__sub-items 1440.0x15.0 bg #ffffff; div.row.no-gutters 1350.0x395.1 border T:1px solid #dedede / B:1px solid #dedede; div.container-fluid.main-navbar__sub-items 1440.0x15.0 bg #ffffff |
| Ancestor paint | 1 up div.shopify-section bg #ffffff |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo.

Page: home. Selector: `home link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 71 x 53 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | proxima-nova 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | color 0.3s ease |
| Cursor | pointer |
| Icon | 71 x 48, colour #000000 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-item

Nav item. A top-level shop category; hover opens the mega-menu.

Page: home. Selector: `a.main-nav__item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 71.95 x 70 | = | = | = |
| Padding | 24px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset 1px | = |
| Font | proxima-nova 18px/normal 500 | = | = | = |
| Letter spacing | 0.9px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 71.9531px x 3px, absolute, bg #000000 @ 0, radius 0px | 71.9531px x 3px, absolute, bg #000000, radius 0px | 71.9531px x 3px, absolute, bg #000000, radius 0px | 71.9531px x 3px, absolute, bg #000000, radius 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a::after.main-nav__item.hover-target 71.9531pxx3px bg #000000 | a.main-nav__item.hover-target 72.0x70.0 outline 5px auto #005fcc offset 1px; a::after.main-nav__item.hover-target 71.9531pxx3px bg #000000 | a::after.main-nav__item.hover-target 71.9531pxx3px bg #000000 |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`.

#### nav-mega

Mega-menu, open. The nav item while its flyout is open; the panel shows in the crop.

Page: home. Selector: `a.main-nav__item:hover`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 71.95 x 70 |
| Padding | 24px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | proxima-nova 18px/normal 500 |
| Letter spacing | 0.9px |
| Colour | #000000 |
| Transition | color 0.3s ease |
| Cursor | pointer |
| ::after | 71.9531px x 3px, absolute, bg #000000, radius 0px |
| Painted layers | a::after.main-nav__item.hover-target 71.9531pxx3px bg #000000 |
| How | flyout held open by opts.open |

Crops: `nav-mega-opened.png`.

#### search-icon

Search icon.

Page: home. Selector: `#main-navbar-search-icon`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 20 x 25 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | proxima-nova 16px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | #595959 | - | #595959 |
| Transition | color 0.3s ease | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | span.icon-search-static 20.0x20.0 image url(data:…) | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Error | - | = | keyboard focus did not land on the element | = |

Crops: `search-icon-default.png`, `search-icon-hover.png`, `search-icon-pressed.png`.

#### account-icon

Account icon.

Page: home. Selector: `.account-icon`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 18 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset 0px | = |
| Font | proxima-nova 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.icon-account-static 18.0x17.0 image url(data:…) | span.icon-account-solid 18.0x17.0 image url(data:…) | button.account-icon 18.0x20.0 outline 5px auto #005fcc offset 0px; span.icon-account-static 18.0x17.0 image url(data:…) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `account-icon-default.png`, `account-icon-hover.png`, `account-icon-focus-visible.png`, `account-icon-pressed.png`.

#### bag-icon

Bag icon.

Page: home. Selector: `.main-navbar__icon--bag`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 18 x 29 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset 1px | = |
| Font | proxima-nova 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #595959 | #595959 | #595959 |
| Transition | color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.icon-bag-static 18.0x24.0 image url(data:…) | = | a.main-navbar__icon.main-navbar__icon--bag 18.0x29.0 outline 5px auto #005fcc offset 1px; span.icon-bag-static 18.0x24.0 image url(data:…) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `bag-icon-default.png`, `bag-icon-hover.png`, `bag-icon-focus-visible.png`, `bag-icon-pressed.png`.

#### search-input

Search field. The header search input; focused only, nothing typed.

Page: home. Selector: `#search-keyboard-up`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 175 x 26 | = |
| Padding | 1px 2px | = |
| Border | 2px inset #767676 | = |
| Radius | 0px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | 1px auto #005fcc offset 0px |
| Font | proxima-nova 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #000000, opacity 1 | = |
| Painted layers | input 175.0x26.0 bg #ffffff border T:2px inset #767676 / R:2px inset #767676 / B:2px inset #767676 / L:2px inset #767676 | input 175.0x26.0 bg #ffffff border T:2px inset #767676 / R:2px inset #767676 / B:2px inset #767676 / L:2px inset #767676 outline 1px auto #005fcc offset 0px |
| How | at rest | clicked into the field |

Crops: `search-input-default.png`, `search-input-focused.png`.

### Home

#### hero-button

Hero button. The filled hero CTA ("JOIN NOW"). Measured, never followed.

Page: home. Selector: `.hero-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 160.25 x 48 | = | = | = |
| Padding | 15px 30px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff | #000000 | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset 0px | = |
| Font | proxima-nova 18px/18px 900 | = | = | = |
| Letter spacing | 1.5px | = | = | = |
| Colour | #000000 | #ffffff | = | #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.hero-button.hero-button--white-bg 160.3x48.0 bg #ffffff | button.hero-button.hero-button--white-bg 160.3x48.0 bg #000000 | button.hero-button.hero-button--white-bg 160.3x48.0 bg #ffffff outline 5px auto #005fcc offset 0px | button.hero-button.hero-button--white-bg 160.3x48.0 bg #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-button-default.png`, `hero-button-hover.png`, `hero-button-focus-visible.png`, `hero-button-pressed.png`.

#### grid-card

Category tile. A shop-category image tile (NEW ARRIVALS, PANTS, ...).

Page: home. Selector: `a.image-grid__card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 313.5 x 449.84 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | proxima-nova 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | #595959 |
| Text node | h6.h6.uppercase: proxima-nova 18px/19.8px 500, #000000, ls 0.9px | = |
| Transition | color 0.3s ease | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `grid-card-default.png`, `grid-card-hover.png`.

#### grid-card-label

Tile label.

Page: home. Selector: `inside image-grid__card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 313.5 x 39.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | proxima-nova 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h6.h6.uppercase: proxima-nova 18px/19.8px 500, #000000, ls 0.9px |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `grid-card-label-default.png`.

#### carousel-cta

Carousel CTA link. "Shop Now" over a product carousel.

Page: home. Selector: `a.carousel-header__cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 75.72 x 22.39 | 77.5 x 22.39 | 77.5 x 22.39 | 77.5 x 22.39 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset 1px | = |
| Font | proxima-nova 16px/22.4px 400 | proxima-nova 16px/22.4px 700 | proxima-nova 16px/22.4px 700 | proxima-nova 16px/22.4px 700 |
| Letter spacing | 0.352px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.carousel-header__cta.body-text-link 77.5x22.4 outline 5px auto #005fcc offset 1px | = |

Crops: `carousel-cta-default.png`, `carousel-cta-hover.png`, `carousel-cta-focus-visible.png`, `carousel-cta-pressed.png`.

#### color-tile

Colour-story tile. A Builder.io colourway block.

Page: home. Selector: `a.builder-block`. States: .

Not found on the page at capture time.

#### to-top

Back-to-top button. The floating round return-to-top control.

Page: home. Selector: `#toTop`. States: .

Not found on the page at capture time.

### Shop grid

#### plp-title

Collection title.

Page: plp. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1382.41 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | proxima-nova 40px/44px 600 |
| Letter spacing | -1.2px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `plp-title-default.png`.

#### sort-button

Sort control. The grid sort/filter trigger. Measured, never opened.

Page: plp. Selector: `button:has-text("Sort")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 167.03 x 34 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 12px | = | = | = |
| Border | 1px solid #cccccc | 1px solid #e1e1e1 | = | 1px solid #e1e1e1 |
| Radius | 360px | = | = | = |
| Background | #ffffff | #e1e1e1 | = | #e1e1e1 |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset 0px | = |
| Font | proxima-nova 14px/normal 500 | = | = | = |
| Letter spacing | 0.7px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.button-ghost-xs 167.0x34.0 bg #ffffff border T:1px solid #cccccc / R:1px solid #cccccc / B:1px solid #cccccc / L:1px solid #cccccc r 360px; span.alo-filters-icon 20.0x20.0 image url(data:…) | button.button-ghost-xs 167.0x34.0 bg #e1e1e1 border T:1px solid #e1e1e1 / R:1px solid #e1e1e1 / B:1px solid #e1e1e1 / L:1px solid #e1e1e1 r 360px; span.alo-filters-icon 20.0x20.0 image url(data:…) | button.button-ghost-xs 167.0x34.0 bg #ffffff border T:1px solid #cccccc / R:1px solid #cccccc / B:1px solid #cccccc / L:1px solid #cccccc r 360px outline 5px auto #005fcc offset 0px; span.alo-filters-icon 20.0x20.0 image url(data:…) | button.button-ghost-xs 167.0x34.0 bg #e1e1e1 border T:1px solid #e1e1e1 / R:1px solid #e1e1e1 / B:1px solid #e1e1e1 / L:1px solid #e1e1e1 r 360px; span.alo-filters-icon 20.0x20.0 image url(data:…) |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sort-button-default.png`, `sort-button-hover.png`, `sort-button-focus-visible.png`, `sort-button-pressed.png`.

#### product-tile

Product tile. A grid card: image, name, price, colour swatches, member-price link.

Page: plp. Selector: `card containing .swatch`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 324 x 637.8 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | proxima-nova 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | p.body.semibold: proxima-nova 16px/22.4px 600, #000000, ls 0.352px | p.mb-0.quick-add-text: proxima-nova 16px/16px 400, #ffffff, ls 1px |
| Transition | none | = |
| Painted layers | span.icon-wishlist-static 20.0x20.0 image url(data:…); a::after 59.0938pxx0.5px bg #4f7541; button.SwatchUI.swatch 26.0x26.0 bg #513b2c border T:1px solid #ececec / R:1px solid #ececec / B:1px solid #ececec / L:1px solid #ececec r 50%; button::before.SwatchUI.swatch 32pxx32px border T:1px solid #7f7f7f / R:1px solid #7f7f7f / B:1px solid #7f7f7f / L:1px solid #7f7f7f r 50%; button.SwatchUI.swatch 26.0x26.0 bg #000000 border T:1px solid #ececec / R:1px solid #ececec / B:1px solid #ececec / L:1px solid #ececec r 50%; button::before.SwatchUI.swatch 32pxx32px border T:1px solid #7f7f7f / R:1px solid #7f7f7f / B:1px solid #7f7f7f / L:1px solid #7f7f7f r 50% | span.icon-wishlist-static 20.0x20.0 image url(data:…); div.quick-add.quick-add-dark-mode 304.0x58.0 bg #3b3b3b; button.quick-add-size-btn 42.3x25.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.quick-add-size-btn 31.8x25.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.quick-add-size-btn 25.0x25.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.quick-add-size-btn 25.0x25.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 |
| How | at rest | mouse hover |

Crops: `product-tile-default.png`, `product-tile-hover.png`.

#### swatch

Colour swatch. A product colour dot; a local selection toggle.

Page: plp. Selector: `button.swatch`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 26 x 26 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #ececec | = | = | = |
| Radius | 50% | = | = | = |
| Background | #513b2c | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset 0px | = |
| Font | proxima-nova 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 32px x 32px, absolute, bg #000000 @ 0, radius 50% | = | = | = |
| Painted layers | button.SwatchUI.swatch 26.0x26.0 bg #513b2c border T:1px solid #ececec / R:1px solid #ececec / B:1px solid #ececec / L:1px solid #ececec r 50%; button::before.SwatchUI.swatch 32pxx32px border T:1px solid #7f7f7f / R:1px solid #7f7f7f / B:1px solid #7f7f7f / L:1px solid #7f7f7f r 50% | = | button.SwatchUI.swatch 26.0x26.0 bg #513b2c border T:1px solid #ececec / R:1px solid #ececec / B:1px solid #ececec / L:1px solid #ececec r 50% outline 5px auto #005fcc offset 0px; button::before.SwatchUI.swatch 32pxx32px border T:1px solid #7f7f7f / R:1px solid #7f7f7f / B:1px solid #7f7f7f / L:1px solid #7f7f7f r 50% | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `swatch-default.png`, `swatch-hover.png`, `swatch-focus-visible.png`, `swatch-pressed.png`.

#### swatch-selected

Swatch, selected.

Page: plp. Selector: `button.swatch.active`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 26 x 26 |
| Padding | 0px |
| Border | 1px solid #ececec |
| Radius | 50% |
| Background | #513b2c |
| Box shadow | none |
| Outline | none |
| Font | proxima-nova 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| ::before | 32px x 32px, absolute, bg #000000 @ 0, radius 50% |
| Painted layers | button.SwatchUI.swatch 26.0x26.0 bg #513b2c border T:1px solid #ececec / R:1px solid #ececec / B:1px solid #ececec / L:1px solid #ececec r 50%; button::before.SwatchUI.swatch 32pxx32px border T:1px solid #7f7f7f / R:1px solid #7f7f7f / B:1px solid #7f7f7f / L:1px solid #7f7f7f r 50% |
| How | at rest |

Crops: `swatch-selected-default.png`.

#### product-name

Product name link.

Page: plp. Selector: `product name a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 324 x 22.39 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset 1px | = |
| Font | proxima-nova 16px/20px 500 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #000000 | #595959 | #595959 | #595959 |
| Text node | p.body.semibold: proxima-nova 16px/22.4px 600, #000000, ls 0.352px | = | = | = |
| Transition | color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 324.0x22.4 outline 5px auto #005fcc offset 1px | = |

Crops: `product-name-default.png`, `product-name-hover.png`, `product-name-focus-visible.png`, `product-name-pressed.png`.

#### member-link

Member-price link. "Join Now" — the membership hook. Measured, never followed.

Page: plp. Selector: `a:has-text("Join Now")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 59.09 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset 1px | = |
| Font | proxima-nova 14px/18px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #4f7541 | = | = | = |
| Transition | color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 59.0938px x 0.5px, absolute, bg #4f7541, radius 0px | = | = | = |
| Painted layers | a::after 59.0938pxx0.5px bg #4f7541 | = | a 59.1x18.0 outline 5px auto #005fcc offset 1px; a::after 59.0938pxx0.5px bg #4f7541 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `member-link-default.png`, `member-link-hover.png`, `member-link-focus-visible.png`, `member-link-pressed.png`.

#### more-colors

More colours chip.

Page: plp. Selector: `.more-colors-icon`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 33 x 17 | = | = | = |
| Padding | 0px 0px 0px 5px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | proxima-nova 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #595959 | #595959 | #595959 |
| Text node | label.ps-have-more: proxima-nova 14px/normal 400, #000000 | label.ps-have-more: proxima-nova 14px/normal 400, #595959 | label.ps-have-more: proxima-nova 14px/normal 400, #595959 | label.ps-have-more: proxima-nova 14px/normal 400, #595959 |
| Transition | color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.alo-add-thick-icon.icon__increment 9.0x9.0 image url(data:…)' stroke='%23000' stroke-width='3.333' stroke-miterlimit='50'%3E%3Cpath d='M10  | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `more-colors-default.png`, `more-colors-hover.png`, `more-colors-focus-visible.png`, `more-colors-pressed.png`.

### undefined

#### pdp_url

PDP URL.

Page: pdp. Selector: ``. States: default.

| Property | default |
|---|---|
| Note | https://www.aloyoga.com/en-sg/products/w4530r-sherpa-edge-bomber-espresso |

Crops: none.

### Product page

#### pdp-title

Product title.

Page: pdp. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 231.53 x 26.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | proxima-nova 24px/26.4px 500 |
| Letter spacing | 0.24px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `pdp-title-default.png`.

#### pdp-price

Product price.

Page: pdp. Selector: `[class*="price"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 420 x 50 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | proxima-nova 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.gated-sale-display-price: proxima-nova 18px/24px 400, #000000 |
| Transition | none |
| Painted layers | a::after 67.5312pxx0.5px bg #4f7541; div::before.review-star autoxauto image linear-gradient(90deg, #ceb18f calc(92.459%), #ffffff calc(92.459%)) |
| How | at rest |

Crops: `pdp-price-default.png`.

#### pdp-swatch

PDP swatch.

Page: pdp. Selector: `button.swatch`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 46 x 46 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset 0px | = |
| Font | proxima-nova 14px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.swatch: proxima-nova 14px/normal 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.swatch__wrapper 46.0x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 50%; span.swatch 35.0x35.0 bg #000000 r 50%; span.swatch-disabled-ui 0.0x0.0 bg #ffffff; span.line 0.0x0.0 bg #979797 | = | label.UserSelection.square 46.0x46.0 outline 5px auto #005fcc offset 0px; span.swatch__wrapper 46.0x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 50%; span.swatch 35.0x35.0 bg #000000 r 50%; span.swatch-disabled-ui 0.0x0.0 bg #ffffff; span.line 0.0x0.0 bg #979797 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pdp-swatch-default.png`, `pdp-swatch-hover.png`, `pdp-swatch-focus-visible.png`, `pdp-swatch-pressed.png`.

#### pdp-swatch-picked

PDP swatch, picked. A colour swatch after its own toggle; never an add-to-bag.

Page: pdp. Selector: `button.swatch`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 46 x 46 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | proxima-nova 14px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.swatch: proxima-nova 14px/normal 400, #000000 |
| Transition | none |
| Cursor | pointer |
| Painted layers | span.swatch__wrapper 46.0x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 50%; span.swatch 35.0x35.0 bg #01305c r 50%; span.swatch-disabled-ui 0.0x0.0 bg #ffffff; span.line 0.0x0.0 bg #979797 |
| How | own toggle |

Crops: `pdp-swatch-picked-opened.png`.

#### size-button

Size button.

Page: pdp. Selector: `size option button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 134 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #000000 | 1px solid #000000 |
| Radius | 0px | = | = | = |
| Background | #ffffff | = | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | 1px solid #cccccc offset 0px | = | 5px auto #005fcc offset 0px | 1px solid #000000 offset 0px |
| Font | proxima-nova 16px/normal 500 | = | = | = |
| Letter spacing | 0.8px | = | = | = |
| Colour | #000000 | = | = | #ffffff |
| Text node | span: proxima-nova 16px/normal 500, #000000, ls 0.8px | = | = | span: proxima-nova 16px/normal 500, #ffffff, ls 0.8px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.button-size-selector__button 134.0x40.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 outline 1px solid #cccccc offset 0px | = | button.button-size-selector__button 134.0x40.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 outline 5px auto #005fcc offset 0px | button.button-size-selector__button 134.0x40.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 outline 1px solid #000000 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `size-button-default.png`, `size-button-hover.png`, `size-button-focus-visible.png`, `size-button-pressed.png`.

#### add-to-bag

Add to bag. The purchase action; measured in every state except a real press.

Page: pdp. Selector: `button:has-text("Add to bag")`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 420 x 52 | = | = |
| Padding | 14px 16px | = | = |
| Gap | 12px | = | = |
| Border | 1px solid #000000 | = | = |
| Radius | 0px | = | = |
| Background | #000000 | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 5px auto #005fcc offset 0px |
| Font | proxima-nova 18px/normal 700 | = | = |
| Letter spacing | 0.9px | = | = |
| Colour | #ffffff | = | = |
| Transition | background-color 0.5s ease-in-out | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.button-primary.product__buy--button 420.0x52.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 | = | button.button-primary.product__buy--button 420.0x52.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 outline 5px auto #005fcc offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `add-to-bag-default.png`, `add-to-bag-hover.png`, `add-to-bag-focus-visible.png`.

#### size-guide

Size-guide link.

Page: pdp. Selector: `a:has-text("Size guide")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 79.22 x 22.39 | = | 80.84 x 22.39 | 80.84 x 22.39 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset 0px | = |
| Font | proxima-nova 16px/22.4px 400 | = | proxima-nova 16px/22.4px 700 | proxima-nova 16px/22.4px 700 |
| Letter spacing | 0.352px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | span.label-add.size-guide-trigger 80.8x22.4 outline 5px auto #005fcc offset 0px | = |

Crops: `size-guide-default.png`, `size-guide-hover.png`, `size-guide-focus-visible.png`, `size-guide-pressed.png`.

#### pdp-accordion

PDP accordion. Details/shipping disclosure row.

Page: pdp. Selector: `button[aria-expanded]`. States: .

Not found on the page at capture time.

#### pdp-accordion-open

PDP accordion, open.

Page: pdp. Selector: `button[aria-expanded]`. States: .

Not found on the page at capture time.

#### size-oos

Size button, out of stock. The sold-out size state (a "notify me" affordance). Never pressed.

Page: pdp. Selector: `button.out-of-stock`. States: .

Not found on the page at capture time.

#### wishlist-button

Wishlist button. The ghost sibling of Add to bag. Measured, never pressed.

Page: pdp. Selector: `button.button-ghost`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 420 x 52 | = | = | = |
| Padding | 14px 32px | = | = | = |
| Gap | 10px | = | = | = |
| Border | 1px solid #000000 | = | = | 1px solid #e1e1e1 |
| Radius | 0px | = | = | = |
| Background | #ffffff | = | = | #e1e1e1 |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset 0px | = |
| Font | proxima-nova 18px/normal 700 | = | = | = |
| Letter spacing | 0.9px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.button-ghost.uppercase 420.0x52.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000; span.icon-wishlist-static 20.0x20.0 image url(data:…) | = | button.button-ghost.uppercase 420.0x52.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 outline 5px auto #005fcc offset 0px; span.icon-wishlist-static 20.0x20.0 image url(data:…) | button.button-ghost.uppercase 420.0x52.0 bg #e1e1e1 border T:1px solid #e1e1e1 / R:1px solid #e1e1e1 / B:1px solid #e1e1e1 / L:1px solid #e1e1e1; span.icon-wishlist-static 20.0x20.0 image url(data:…) |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `wishlist-button-default.png`, `wishlist-button-hover.png`, `wishlist-button-focus-visible.png`, `wishlist-button-pressed.png`.

### Cart

#### cart-empty

Empty cart. The signed-out bag with nothing in it.

Page: cart. Selector: `main`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 651.17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | proxima-nova 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h4.h4.uppercase: proxima-nova 24px/26.4px 600, #000000 |
| Transition | none |
| Icon | 0 x 0, colour #ffffff, fill #000000 |
| ::before | 1440px x 651.172px, absolute, bg #000000 @ 0.35, radius 0px |
| Painted layers | main::before.main 1440pxx651.172px bg #000000 @ 0.35; div.full-width__line.d-block 0.0x0.0 border B:1px solid #dfdfdf; div.shopping-bag-block.shopping-bag-block__new 770.0x244.4 border T:1px solid #cfcfcf; a.btn.btn-primary 112.7x40.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; div.loader-overlay.is--visible 0.0x0.0 bg #ffffff @ 0.5; div::before.spinner 100%x100% border T:1px solid #000000 @ 0 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 100% |
| Ancestor paint | 1 up body.antialiased.template-cart bg #ffffff |
| How | at rest |

Crops: `cart-empty-default.png`.

#### cart-continue

Continue shopping. Measured, never followed.

Page: cart. Selector: `a:has-text("Continue")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 112.67 x 40 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Border | 1px solid #000000 @ 0 | 1px solid #404040 | 1px solid #404040 | 1px solid #000000 |
| Radius | 0px | = | = | = |
| Background | #000000 | #404040 | #404040 | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset 1px | = |
| Font | proxima-nova 15px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fefefe | = | = | = |
| Transition | color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.btn-primary 112.7x40.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | a.btn.btn-primary 112.7x40.0 bg #404040 border T:1px solid #404040 / R:1px solid #404040 / B:1px solid #404040 / L:1px solid #404040 | a.btn.btn-primary 112.7x40.0 bg #404040 border T:1px solid #404040 / R:1px solid #404040 / B:1px solid #404040 / L:1px solid #404040 outline 5px auto #005fcc offset 1px | a.btn.btn-primary 112.7x40.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cart-continue-default.png`, `cart-continue-hover.png`, `cart-continue-focus-visible.png`, `cart-continue-pressed.png`.

### Account gate

#### login-title

Login title.

Page: account. Selector: `login form heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 448 x 22.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | proxima-nova 16px/22.4px 500 |
| Letter spacing | 0.352px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `login-title-default.png`.

#### email-input

Email field. Text was typed and deleted; the form was never submitted.

Page: account. Selector: `input[type="email"]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 588 x 35 | = | = |
| Padding | 0px 0px 0px 14px | = | = |
| Border | 1px solid #a3a3a3 | 1px solid #000000 | 1px solid #000000 |
| Radius | 0px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | proxima-nova 14px/normal 400 | = | = |
| Letter spacing | 0.352px | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #636363, opacity 1 | = | = |
| Painted layers | input.yoga-ui-input.react-input 588.0x35.0 bg #ffffff border T:1px solid #a3a3a3 / R:1px solid #a3a3a3 / B:1px solid #a3a3a3 / L:1px solid #a3a3a3 | input.yoga-ui-input.react-input 588.0x35.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 | input.yoga-ui-input.react-input 588.0x35.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `email-input-default.png`, `email-input-focused.png`, `email-input-filled.png`.

#### password-input

Password field. Focused only; nothing was typed.

Page: account. Selector: `input[type="password"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 588 x 35 | = |
| Padding | 0px 0px 0px 14px | = |
| Border | 1px solid #a3a3a3 | 1px solid #000000 |
| Radius | 0px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | proxima-nova 14px/normal 400 | = |
| Letter spacing | 0.352px | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #636363, opacity 1 | = |
| Painted layers | input.yoga-ui-input.react-input 588.0x35.0 bg #ffffff border T:1px solid #a3a3a3 / R:1px solid #a3a3a3 / B:1px solid #a3a3a3 / L:1px solid #a3a3a3 | input.yoga-ui-input.react-input 588.0x35.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 |
| How | at rest | clicked into the field |

Crops: `password-input-default.png`, `password-input-focused.png`.

#### signin-button

Sign in button. The submit; measured except a real press — the form was never submitted.

Page: account. Selector: `login form submit`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 588 x 38 | = | - |
| Padding | 14px 16px | = | - |
| Gap | 12px | = | - |
| Border | 1px solid #cccccc | = | - |
| Radius | 0px | = | - |
| Background | #cccccc | = | - |
| Box shadow | none | = | - |
| Outline | none | = | - |
| Font | proxima-nova 16px/5.6px 900 | = | - |
| Letter spacing | 1.28px | = | - |
| Colour | #636363 | = | - |
| Transition | none | = | - |
| Cursor | not-allowed | = | - |
| Painted layers | button.button-primary.btn-primary 588.0x38.0 bg #cccccc border T:1px solid #cccccc / R:1px solid #cccccc / B:1px solid #cccccc / L:1px solid #cccccc | = | - |
| How | at rest | mouse hover | - |
| Error | - | = | keyboard focus did not land on the element |

Crops: `signin-button-default.png`, `signin-button-hover.png`.

#### forgot-link

Forgot-password link.

Page: account. Selector: `a:has-text("Forgot")`. States: .

Not found on the page at capture time.

#### create-account

Create-account link. Measured, never followed.

Page: account. Selector: `a:has-text("Create")`. States: .

Not found on the page at capture time.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 57 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | proxima-nova 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Icon | 0 x 0, colour #000000 |
| Painted layers | div.desktop-nav.row 0.0x0.0 border B:1px solid #dedede; div.container-fluid.main-navbar__sub-items 0.0x0.0 bg #ffffff; div.row.no-gutters 0.0x0.0 border T:1px solid #dedede / B:1px solid #dedede; div.container-fluid.main-navbar__sub-items 0.0x0.0 bg #ffffff; div.row.no-gutters 0.0x0.0 border T:1px solid #dedede / B:1px solid #dedede; div.container-fluid.main-navbar__sub-items 0.0x0.0 bg #ffffff |
| Ancestor paint | 1 up div.shopify-section bg #ffffff |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button.

Page: home. Selector: `header button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 30 x 30 | = | = | = |
| Padding | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #e59700 offset 0px | = |
| Font | proxima-nova 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.navbar__toggler.hamburger 30.0x30.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; span.icon-yoga-hamburger 20.0x20.0 image url(data:…) | = | button.navbar__toggler.hamburger 30.0x30.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 outline 5px auto #e59700 offset 0px; span.icon-yoga-hamburger 20.0x20.0 image url(data:…) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.7 | 0.7 | 0.7 |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The button after its own toggle; the open drawer shows in the crop.

Page: home. Selector: `header button`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 29 x 29 |
| Padding | 4px |
| Border | 1px solid #000000 @ 0 |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | proxima-nova 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Opacity | 0.7 |
| Cursor | pointer |
| Painted layers | button.navbar__toggler.hamburger 29.0x29.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; span.icon-yoga-hamburger 0.0x0.0 image url(data:…) |
| How | own toggle |

Crops: `m-menu-open-opened.png`.

#### m-nav-link

Mobile nav link. A row inside the opened menu drawer.

Page: home. Selector: `open menu a`. States: .

Not found on the page at capture time.

#### m-hero-button

Mobile hero button.

Page: home. Selector: `.hero-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140.25 x 38 | = | = | = |
| Padding | 10px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff | = | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #e59700 offset 0px | = |
| Font | proxima-nova 18px/18px 900 | = | = | = |
| Letter spacing | 1.5px | = | = | = |
| Colour | #000000 | = | = | #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.hero-button.hero-button--white-bg 140.3x38.0 bg #ffffff | = | button.hero-button.hero-button--white-bg 140.3x38.0 bg #ffffff outline 5px auto #e59700 offset 0px | button.hero-button.hero-button--white-bg 140.3x38.0 bg #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-hero-button-default.png`, `m-hero-button-hover.png`, `m-hero-button-focus-visible.png`, `m-hero-button-pressed.png`.

#### m-product-tile

Mobile product tile.

Page: home. Selector: `grid card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 499.92 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | proxima-nova 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.h3: proxima-nova 24px/26.4px 600, #000000, ls -0.72px |
| Transition | none |
| Painted layers | span.icon-wishlist-static 20.0x20.0 image url(data:…); span 40.0x40.0 bg #ffffff @ 0.5 r 50%; span.alo-quick-add-icon 20.0x20.0 image url(data:…); a::after 59.0938pxx0.5px bg #4f7541; button.SwatchUI.swatch 16.0x6.0 bg #735841 border T:2px outset #000000 / R:2px outset #000000 / B:2px outset #000000 / L:2px outset #000000; button.SwatchUI.swatch 16.0x6.0 bg #000000 border T:2px outset #000000 / R:2px outset #000000 / B:2px outset #000000 / L:2px outset #000000 |
| How | at rest |

Crops: `m-product-tile-default.png`.

### Footer

#### footer

Footer.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 643.27 |
| Padding | 28px 0px 64px 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | proxima-nova 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.footer-title.body: proxima-nova 16px/22.4px 600, #ffffff, ls 0.352px |
| Transition | none |
| Painted layers | footer.footer 1440.0x643.3 bg #000000; hr.sc-modal-trigger-divider 0.0x0.0 border T:1px solid #e3e3e3; p::after.small-p.country-name 10pxx10px border B:1px solid #ffffff / L:1px solid #ffffff; input.yoga-ui-input.react-input 293.0x48.4 border T:1px solid #a3a3a3 / R:1px solid #a3a3a3 / B:1px solid #a3a3a3 / L:1px solid #a3a3a3; button.button-invert 50.0x48.4 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff; span.alo-chevron-right-icon 20.0x20.0 image url(data:…)' fill-rule='evenodd' clip-rule='evenodd' d='M13.333 17.5l-7.5-7.5 7.5-7.5.834. |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 88.83 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset 1px | = |
| Font | proxima-nova 16px/22.4px 400 | = | = | = |
| Letter spacing | 0.352px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.body 88.8x20.0 outline 5px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Footer social icon.

Page: home. Selector: `footer a[aria-label]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 27 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset 1px | = |
| Font | proxima-nova 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.nav-link 27.0x20.0 outline 5px auto #005fcc offset 1px | = |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

#### newsletter-input

Newsletter field. Focused only; never subscribed.

Page: home. Selector: `footer input[type="email"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 468 x 35 | = |
| Padding | 0px 0px 0px 14px | = |
| Border | 1px solid #a3a3a3 | 1px solid #000000 |
| Radius | 0px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | proxima-nova 14px/normal 400 | = |
| Letter spacing | 0.352px | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #636363, opacity 1 | = |
| Painted layers | input.yoga-ui-input.react-input 468.0x35.0 bg #ffffff border T:1px solid #a3a3a3 / R:1px solid #a3a3a3 / B:1px solid #a3a3a3 / L:1px solid #a3a3a3 | input.yoga-ui-input.react-input 468.0x35.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 |
| How | at rest | clicked into the field |

Crops: `newsletter-input-default.png`, `newsletter-input-focused.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page: inline styles and same-origin sheets, since a cross-origin sheet stays unreadable there. The per-state Transition rows in the tables above are computed values and cover every rule the page paints.

- home: `transform 100ms linear, opacity 200ms linear, visibility linear`, `flex-grow 1000ms linear`, `none`, `background-color 0.2s ease-out`, `opacity 200ms linear, visibility 200ms linear 200ms`, `opacity 200ms linear, visibility linear`, `background 0.2s ease-in-out`, `background 0.1s, box-shadow 0.1s, color 0.1s`, `color 0.1s`, `opacity 0.1s`, `background 0.1s`, `background-color 0.5s linear`
