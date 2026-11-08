# Component measurements

Computed styles read from www.allbirds.com on 2026-11-08 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### promo-bar

Announcement bar. The rotating strip above the header ("Free ground shipping on orders over $100", shipping-delay notices): black fill, centred xs copy, prev/next chevrons at the ends (a Swiper carousel).

Page: home. Selector: `.swiper top bar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geograph 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.text-center.text-[10px]: Geograph 12px/16px 400, #ffffff, ls 0.6px |
| Transition | none |
| Icon | 24 x 24, colour #ffffff |
| Ancestor paint | 1 up div.relative bg #212121 |
| How | at rest |

Crops: `promo-bar-default.png`.

#### promo-bar-next

Announcement bar arrow.

Page: home. Selector: `.swiper-next-button`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 24 x 24 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geograph 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | none | = |
| Cursor | default | = |
| Icon | 24 x 24, colour #ffffff | = |
| How | at rest | mouse hover |

Crops: `promo-bar-next-default.png`, `promo-bar-next-hover.png`.

#### header

Header. The sticky rounded bar: wordmark centre-left, text links NEW ARRIVALS and SHOP ALL, the MEN and WOMEN mega-menu buttons, a Search link and the cart button with its count badge.

Page: home. Selector: `nav pill bar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1400 x 48 |
| Padding | 0px 20px |
| Border | none |
| Radius | 12px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px |
| Outline | none |
| Font | Geograph 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.cursor-pointer.items-center: Geograph 12px/16px 500, #212121, ls 0.6px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 0 x 0, colour #000000 |
| Painted layers | div.absolute.top-5 1400.0x48.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px; span.ease-sine-in.absolute 0.0x0.0 bg #212121 r 3.35544e+07px; span.ease-sine-in.absolute 14.0x14.0 bg #212121 r 3.35544e+07px |
| How | at rest |

Crops: `header-default.png`.

#### nav-link

Nav link. A text nav item: xs, medium, tracking-wider, uppercase.

Page: home. Selector: `nav a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 61.73 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Geograph 12px/16px 500 | = | = | = |
| Letter spacing | 0.6px | = | = | = |
| Colour | #212121 | = | = | = |
| Transition | opacity 0.2s cubic-bezier(0.37, 0, 0.63, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.cursor-pointer.items-center 61.7x16.0 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-menu-button

Mega-menu button. MEN/WOMEN open the mega-menu flyout on hover; measured, also hovered once for the flyout crop.

Page: home. Selector: `nav button`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 30.42 x 16 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Geograph 12px/16px 500 | = | = |
| Letter spacing | 0.6px | = | = |
| Colour | #212121 | = | = |
| Transition | opacity 0.2s cubic-bezier(0.37, 0, 0.63, 1) | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | CDP forcePseudoState :active:hover |

Crops: `nav-menu-button-default.png`, `nav-menu-button-hover.png`, `nav-menu-button-pressed.png`.

#### mega-menu

Mega-menu flyout. The panel under MEN: category links and colour/material rows of circular swatches.

Page: home. Selector: `mega menu flyout`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 155.72 x 202 |
| Padding | 0px |
| Gap | 28px normal |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geograph 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.text-xs.tracking-wider: Geograph 12px/16px 500, #212121, ls 0.6px |
| Transition | none |
| How | at rest |

Crops: `mega-menu-default.png`.

#### cart-button

Cart button. The bag icon with the count badge on top; opens the cart drawer.

Page: home. Selector: `nav cart button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Geograph 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.ease-sine-in.absolute: Geograph 9px/13.5px 500, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #000000 | = | = | = |
| Painted layers | span.ease-sine-in.absolute 14.0x14.0 bg #212121 r 3.35544e+07px | = | button.relative.flex 24.0x24.0 outline 1px auto #005fcc offset 0px; span.ease-sine-in.absolute 14.0x14.0 bg #212121 r 3.35544e+07px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cart-button-default.png`, `cart-button-hover.png`, `cart-button-focus-visible.png`, `cart-button-pressed.png`.

#### search-link

Search link. The magnifier nav item; navigates to /search.

Page: home. Selector: `nav a[href*=search]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Geograph 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 24.0x24.0 outline 1px auto #005fcc offset 1px | = |

Crops: `search-link-default.png`, `search-link-hover.png`, `search-link-focus-visible.png`, `search-link-pressed.png`.

#### footer

Footer. The black footer: subscribe row, HELP/SHOP/COMPANY link columns, legal links, the OneTrust "Do Not Sell" settings button.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 763 |
| Padding | 80px 40px 20px 40px |
| Border | none |
| Radius | 0px |
| Background | #212121 |
| Box shadow | none |
| Outline | none |
| Font | Geograph 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.mb-8.font-mono: Akkurat Mono 12px/16px 400, #ffffff, ls 1.2px |
| Transition | none |
| Icon | 24 x 24, colour #ffffff |
| Painted layers | footer.bg-black.px-5 1440.0x763.0 bg #212121; input.h-full.w-full 384.0x42.0 bg #ffffff border T:1px solid #212121 / R:1px solid #212121 / B:1px solid #212121 / L:1px solid #212121 r 3.35544e+07px; div.flex.items-center 42.0x42.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 3.35544e+07px; div.flex.items-center 42.0x42.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 3.35544e+07px; div.flex.items-center 42.0x42.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 3.35544e+07px; div.flex.items-center 42.0x42.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 3.35544e+07px |
| How | at rest |

Crops: `footer-default.png`.

### Collection grid

#### collection-title

Collection title. The collection page heading.

Page: collection. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 139.19 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geograph 24px/32px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `collection-title-default.png`.

#### filter-button

Filter button. Opens the filter/sort sheet; labelled with the product count. The sheet itself is the filter-sheet component.

Page: collection. Selector: `button filter`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 183.48 x 34 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Geograph 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.text-sm.font-medium: Geograph 14px/20px 500, oklch(0.446 0.03 256.802), ls 0.35px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #000000 | = | = | = |
| Painted layers | span.flex.items-center 34.0x34.0 border T:1px solid #212121 / R:1px solid #212121 / B:1px solid #212121 / L:1px solid #212121 r 3.35544e+07px | = | button.flex.flex-shrink-0 183.5x34.0 outline 1px auto #005fcc offset 0px; span.flex.items-center 34.0x34.0 border T:1px solid #212121 / R:1px solid #212121 / B:1px solid #212121 / L:1px solid #212121 r 3.35544e+07px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filter-button-default.png`, `filter-button-hover.png`, `filter-button-focus-visible.png`, `filter-button-pressed.png`.

#### filter-sheet

Filter sheet. The panel the Filter button opens: size/price/colour groups with checkboxes.

Page: collection. Selector: `filter sheet`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 1280 x 628 |
| Padding | 68px 24px 24px 24px |
| Gap | 48px |
| Border | none |
| Radius | 20px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px |
| Outline | none |
| Font | Geograph 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Geograph 16px/24px 500, #000000 |
| Transition | none |
| Icon | 32 x 32, colour #000000 |
| Painted layers | form.inset-0.mb-0 1280.0x628.0 bg #ffffff r 20px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px; label.flex.size-full 49.0x48.0 border T:1px solid oklch(0.872 0.01 258.338) / R:1px solid oklch(0.872 0.01 258.338) / B:1px solid oklch(0.872 0.01 258.338) / L:1px solid oklch(0.872 0.01 258.338); label.flex.size-full 49.0x48.0 border T:1px solid oklch(0.872 0.01 258.338) / R:1px solid oklch(0.872 0.01 258.338) / B:1px solid oklch(0.872 0.01 258.338) / L:1px solid oklch(0.872 0.01 258.338); label.flex.size-full 49.0x48.0 border T:1px solid oklch(0.872 0.01 258.338) / R:1px solid oklch(0.872 0.01 258.338) / B:1px solid oklch(0.872 0.01 258.338) / L:1px solid oklch(0.872 0.01 258.338); label.flex.size-full 49.0x48.0 border T:1px solid oklch(0.872 0.01 258.338) / R:1px solid oklch(0.872 0.01 258.338) / B:1px solid oklch(0.872 0.01 258.338) / L:1px solid oklch(0.872 0.01 258.338); label.flex.size-full 49.0x48.0 border T:1px solid oklch(0.872 0.01 258.338) / R:1px solid oklch(0.872 0.01 258.338) / B:1px solid oklch(0.872 0.01 258.338) / L:1px solid oklch(0.872 0.01 258.338) |
| How | at rest |

Crops: `filter-sheet-open.png`.

#### product-card

Product card. A grid card: rounded-2xl photo, name, colour name, price; hover swaps in the second photo (opacity fade on a z-[1] image).

Page: collection. Selector: `a[href*=/products/] card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 280.5 x 65 | = |
| Padding | 0px | = |
| Gap | 4px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geograph 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | p.font-sans.text-xs: Geograph 14px/20px 500, #000000, ls 0.7px | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `product-card-default.png`, `product-card-hover.png`.

#### card-image

Card photo.

Page: collection. Selector: `card img`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 312.5 x 312.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geograph 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| How | at rest |

Crops: `card-image-default.png`.

#### more-colors

More colours link. The "+6" under a card: xs medium underline, points at the product page.

Page: collection. Selector: `card +N link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 16.7 x 14 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geograph 14px/14px 500 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `more-colors-default.png`, `more-colors-hover.png`.

### Product page

#### pdp-title

Product title. "Men's Tree Runner NZ" in the brand serif.

Page: product. Selector: `h1.font-serif`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 483.19 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Self Modern 30px/36px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `pdp-title-default.png`.

#### pdp-price

Price.

Page: product. Selector: `pdp $ leaf`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 44.86 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geograph 18px/28px 500 |
| Letter spacing | 0.9px |
| Colour | #212121 |
| Transition | none |
| How | at rest |

Crops: `pdp-price-default.png`.

#### swatch-group

Swatch group. The colour picker: rows of circular swatches (uppercase group labels like "JERSEY", "STRIPE").

Page: product. Selector: `.swatch-group`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 483.19 x 76 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geograph 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Icon | 0 x 0, colour #000000 |
| Painted layers | span.inset-ring-light-charcoal-0.7.pointer-events-none 36.0x36.0 image linear-gradient(135deg, #8b8a8f 50%, #e0e2dc 50%) border T:3px solid #ffffff / R:3px solid #ffffff / B:3px solid #ffffff / L:3px solid #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #575757 @ 0.7 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #212121 0px 0px 0px 1px; span.inset-ring-light-charcoal-0.7.pointer-events-none 36.0x36.0 image linear-gradient(135deg, #242729 50%, #e0e2dc 50%) border T:3px solid #ffffff / R:3px solid #ffffff / B:3px solid #ffffff / L:3px solid #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #575757 @ 0.7 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.inset-ring-light-charcoal-0.7.pointer-events-none 36.0x36.0 bg #242729 border T:3px solid #ffffff / R:3px solid #ffffff / B:3px solid #ffffff / L:3px solid #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #575757 @ 0.7 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.inset-ring-light-charcoal-0.7.pointer-events-none 36.0x36.0 image linear-gradient(to right, #e0e2dc 33%, #090c43 33%, #090c43 66%, #e0e2dc 66%) border T:3px solid #ffffff / R:3px solid #ffffff / B:3px solid #ffffff / L:3px solid #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #575757 @ 0.7 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.inset-ring-light-charcoal-0.7.pointer-events-none 36.0x36.0 bg #e0e2dc border T:3px solid #ffffff / R:3px solid #ffffff / B:3px solid #ffffff / L:3px solid #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #575757 @ 0.7 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.inset-ring-light-charcoal-0.7.pointer-events-none 36.0x36.0 image linear-gradient(135deg, #b4a897 50%, #e5dcc2 50%) border T:3px solid #ffffff / R:3px solid #ffffff / B:3px solid #ffffff / L:3px solid #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #575757 @ 0.7 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `swatch-group-default.png`.

#### swatch

Swatch. One colour circle; the selected one carries a ring.

Page: product. Selector: `swatch`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Geograph 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #000000 | = | = | = |
| Painted layers | span.inset-ring-light-charcoal-0.7.pointer-events-none 36.0x36.0 image linear-gradient(135deg, #8b8a8f 50%, #e0e2dc 50%) border T:3px solid #ffffff / R:3px solid #ffffff / B:3px solid #ffffff / L:3px solid #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #575757 @ 0.7 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #212121 0px 0px 0px 1px | = | button.relative.size-9 36.0x36.0 r 3.35544e+07px outline 1px auto #005fcc offset 0px; span.inset-ring-light-charcoal-0.7.pointer-events-none 36.0x36.0 image linear-gradient(135deg, #8b8a8f 50%, #e0e2dc 50%) border T:3px solid #ffffff / R:3px solid #ffffff / B:3px solid #ffffff / L:3px solid #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #575757 @ 0.7 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #212121 0px 0px 0px 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `swatch-default.png`, `swatch-hover.png`, `swatch-focus-visible.png`, `swatch-pressed.png`.

#### size-tab-active

Size tab, active. The underlined "MEN'S SIZES" tab of the men/women size-grid switch.

Page: product. Selector: `size tab`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 121.95 x 17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Akkurat Mono 14px/20px 400 |
| Letter spacing | 0.7px |
| Colour | #575757 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `size-tab-active-default.png`.

#### size-tab

Size tab. The inactive tab: light-charcoal, transparent border.

Page: product. Selector: `size tab`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 121.95 x 21 | = |
| Padding | 0px | = |
| Border | T: none; R: none; B: 1px solid #000000 @ 0; L: none | T: none; R: none; B: 1px solid #212121; L: none |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Akkurat Mono 14px/20px 400 | = |
| Letter spacing | 0.7px | = |
| Colour | #575757 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | a.text-light-charcoal.border-b 122.0x21.0 border B:1px solid #000000 @ 0 | a.text-light-charcoal.border-b 122.0x21.0 border B:1px solid #212121 |
| How | at rest | mouse hover |

Crops: `size-tab-default.png`, `size-tab-hover.png`.

#### size-button

Size button. .btn-size: the bordered size chip; selected state fills black with white text (measured after one was clicked).

Page: product. Selector: `button.btn-size`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 62.17 x 42 | = | = |
| Padding | 12px 0px | = | = |
| Border | 1px solid #cdcdcd | = | = |
| Radius | 2px | = | = |
| Background | transparent | #575757 @ 0.19 | #575757 @ 0.19 |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Geograph 12px/16px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.37, 0, 0.63, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.btn-size 62.2x42.0 border T:1px solid #cdcdcd / R:1px solid #cdcdcd / B:1px solid #cdcdcd / L:1px solid #cdcdcd r 2px | button.btn-size 62.2x42.0 bg #575757 @ 0.19 border T:1px solid #cdcdcd / R:1px solid #cdcdcd / B:1px solid #cdcdcd / L:1px solid #cdcdcd r 2px | button.btn-size 62.2x42.0 bg #575757 @ 0.19 border T:1px solid #cdcdcd / R:1px solid #cdcdcd / B:1px solid #cdcdcd / L:1px solid #cdcdcd r 2px |
| How | at rest | mouse hover | CDP forcePseudoState :active:hover |

Crops: `size-button-default.png`, `size-button-hover.png`, `size-button-pressed.png`.

#### size-button-disabled

Size button, sold out. .btn-size.disabled: the struck-through greyed chip.

Page: product. Selector: `button.btn-size.disabled`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 62.16 x 42 |
| Padding | 12px 0px |
| Border | 1px solid #cdcdcd |
| Radius | 2px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geograph 12px/16px 500 |
| Letter spacing | normal |
| Colour | oklch(0.707 0.022 261.325) |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.37, 0, 0.63, 1) |
| Opacity | 0.7 |
| Cursor | pointer |
| Icon | 60.16 x 40, colour oklch(0.707 0.022 261.325), fill #000000 |
| Painted layers | button.btn-size.disabled 62.2x42.0 border T:1px solid #cdcdcd / R:1px solid #cdcdcd / B:1px solid #cdcdcd / L:1px solid #cdcdcd r 2px |
| How | at rest |

Crops: `size-button-disabled-default.png`.

#### fit-guide

Fit Guide link. The underlined text button under the size grid.

Page: product. Selector: `fit guide`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 51.63 x 16 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geograph 12px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #575757 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `fit-guide-default.png`, `fit-guide-hover.png`.

#### atc-button

Add to Cart button. .btn.btn-secondary: the full-width black pill under the buy box ("ADD TO CART - $100"). Mounted once a size is picked; clicked once for the cart drawer, checkout never pressed.

Page: product. Selector: `btn-secondary ATC`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 483.19 x 49 | = | = | = |
| Padding | 16px | = | = | = |
| Border | 1px solid #212121 | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #212121 | #575757 | = | #575757 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto oklch(0.546 0.245 262.881) offset 0px | = |
| Font | Geograph 12px/15px 500 | = | = | = |
| Letter spacing | 0.6px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color, border-color, opacity 0.2s, 0.2s, 0.2s, 0.2s cubic-bezier(0.37, 0, 0.63, 1), cubic-bezier(0.37, 0, 0.63, 1), cubic-bezier(0.37, 0, 0.63, 1), cubic-bezier(0.61, 1, 0.88, 1) delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.btn.btn-secondary 483.2x49.0 bg #212121 border T:1px solid #212121 / R:1px solid #212121 / B:1px solid #212121 / L:1px solid #212121 r 3.35544e+07px | button.btn.btn-secondary 483.2x49.0 bg #575757 border T:1px solid #212121 / R:1px solid #212121 / B:1px solid #212121 / L:1px solid #212121 r 3.35544e+07px | button.btn.btn-secondary 483.2x49.0 bg #212121 border T:1px solid #212121 / R:1px solid #212121 / B:1px solid #212121 / L:1px solid #212121 r 3.35544e+07px outline 1px auto oklch(0.546 0.245 262.881) offset 0px | button.btn.btn-secondary 483.2x49.0 bg #575757 border T:1px solid #212121 / R:1px solid #212121 / B:1px solid #212121 / L:1px solid #212121 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `atc-button-default.png`, `atc-button-hover.png`, `atc-button-focus-visible.png`, `atc-button-pressed.png`.

#### accordion

Accordion row. A PDP details row (WHY WE LOVE THIS, MATERIALS & SUSTAINABILITY, CARE INSTRUCTIONS): full-width, py-6, plus/minus on the right.

Page: product. Selector: `button[aria-expanded]`. States: default, open, hover.

| Property | default | open | hover |
|---|---|---|---|
| Size (w x h) | 1364 x 72 | = | = |
| Padding | 24px 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Geograph 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | span.font-mono.text-base: Akkurat Mono 16px/24px 400, #000000, ls 1.6px | = | = |
| Transition | none | = | = |
| Cursor | default | = | = |
| Painted layers | span.absolute.top-1/2 16.0x1.0 bg #000000; span.absolute.top-1/2 16.0x1.0 bg #000000 | = | = |
| Ancestor paint | 1 up div.rounded-3xl.bg-white bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px; 3 up div.m-2.5.my-10 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = |
| How | at rest | accordion opened | mouse hover |

Crops: `accordion-default.png`, `accordion-open.png`, `accordion-hover.png`.

#### tooltip-pill

Tooltip pill. The black pill over the gallery (e.g. "Tree-based upper for lightweight comfort") that opens a material tooltip.

Page: product. Selector: `tooltip pill`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 273.73 x 40 | = |
| Padding | 10px 12px | = |
| Gap | 4px | = |
| Border | none | = |
| Radius | 3.35544e+07px | = |
| Background | #242424 | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.12 0px 2px 20px 0px | = |
| Backdrop filter | blur(8px) | = |
| Outline | none | = |
| Font | Barlow 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | span.min-w-0.leading-xl: Barlow 14px/20px 400, #ffffff | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.inline-flex.max-w-[calc(var(--viewport-w,100vw)-2rem)] 273.7x40.0 bg #242424 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.12 0px 2px 20px 0px | = |
| How | at rest | mouse hover |

Crops: `tooltip-pill-default.png`, `tooltip-pill-hover.png`.

### Cart drawer

#### cart-drawer

Cart drawer. The right-hand .z-takeover drawer after Add to Cart: CART heading, free-shipping meter, item rows, upsell carousel, subtotal and the checkout buttons. Never checked out.

Page: product. Selector: `.z-takeover cart`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 531 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px |
| Outline | none |
| Font | Geograph 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.text-xs.font-medium: Geograph 12px/16px 500, #000000 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 32 x 32, colour #000000 |
| Painted layers | div.z-takeover.fixed 531.0x900.0 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px; div.bg-natural-white.h-[7px] 511.0x7.0 bg #e0dacf r 4px; div.h-[7px].w-full 511.0x7.0 bg #212121 r 4px; div.bg-natural-white-60.absolute 0.0x0.0 bg #ece9e2; li.border-light-charcoal-0.3.mb-2 511.0x99.0 border B:1px solid #575757 @ 0.19; div.border-stroke.inline-flex 100.0x32.0 border T:1px solid #cdcdcd / R:1px solid #cdcdcd / B:1px solid #cdcdcd / L:1px solid #cdcdcd r 20px |
| How | at rest |

Crops: `cart-drawer-open.png`.

#### cart-qty

Quantity stepper. The +/- stepper on a cart row.

Page: product. Selector: `qty button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 7.2 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geograph 12px/16px 500 |
| Letter spacing | normal |
| Colour | #212121 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `cart-qty-default.png`.

#### cart-upsell-card

Upsell card. RECOMMENDED FOR YOU carousel cards with a size select and an "Add+" link.

Page: product. Selector: `.cart-upsells`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 338 x 116 |
| Padding | 10px |
| Border | 1px solid oklch(0.928 0.006 264.531) |
| Radius | 10px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Geograph 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.font-regular.text-light-charcoal: Geograph 14px/20px 400, #575757 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 16 x 16, colour #000000 |
| Painted layers | div.swiper-slide.!flex 338.0x116.0 bg #ffffff border T:1px solid oklch(0.928 0.006 264.531) / R:1px solid oklch(0.928 0.006 264.531) / B:1px solid oklch(0.928 0.006 264.531) / L:1px solid oklch(0.928 0.006 264.531) r 10px; button.h-5.w-5 20.0x20.0 border T:1px solid #212121 / R:1px solid #212121 / B:1px solid #212121 / L:1px solid #212121 r 3.35544e+07px; div.m-auto.size-[14px] 14.0x14.0 bg #242729 r 3.35544e+07px; label.pointer-events-none.absolute 18.0x18.0 border T:1px solid #212121 / R:1px solid #212121 / B:1px solid #212121 / L:1px solid #212121 r 20px; select.border-back.w-full 165.0x34.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 20px |
| How | at rest |

Crops: `cart-upsell-card-default.png`.

#### checkout-button

Checkout button. The black "Checkout+ | $104.98" pill in the cart drawer footer. Rendered by Shopify's checkout surface (shadow DOM / iframe): visible in the drawer crop but not introspectable from the page DOM, so no computed style was recorded. Never pressed.

Page: product. Selector: `checkout button`. States: .

Not found on the page at capture time.

#### express-button

Express pay buttons. The Amazon Pay / G Pay / PayPal / Shop Pay wallet row under checkout. Shopify-hosted (iframes/shadow): visible in the drawer crop, not introspectable from the page DOM, so no computed style was recorded.

Page: product. Selector: `express row`. States: .

Not found on the page at capture time.

### Forms

#### search-input

Search field. The /search page field. Text was typed and deleted; never submitted.

Page: search. Selector: `search input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 676 x 40 | = | = |
| Padding | 8px 32px 8px 8px | = | = |
| Border | none | = | = |
| Radius | 6px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Geograph 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | oklab(0 0 0 / 0.5), opacity 1 | = | = |
| How | at rest | clicked into the field | typed "wool runner", then deleted; nothing sent |

Crops: `search-input-default.png`, `search-input-focused.png`, `search-input-filled.png`.

#### search-submit

Search submit. Measured, never pressed.

Page: search. Selector: `search submit`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 24 x 40 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geograph 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 24 x 24, colour #000000 | = |
| How | at rest | mouse hover |

Crops: `search-submit-default.png`, `search-submit-hover.png`.

#### login-input

Login email field. The account sign-in field on the public login page. Text was typed and deleted; never submitted.

Page: account. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 337 x 47 | = | = |
| Padding | 13.55px 10px | = | 21.05px 10px 6.05px 10px |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | lBKuE1Nf 14px/18.9px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | all 0.2s ease-in-out | = | = |
| Cursor | text | = | = |
| Placeholder | #707070, opacity 1 | = | #707070, opacity 0 |
| Ancestor paint | 1 up div._7ozb2ub._7ozb2ua bg #ffffff outline 0px solid #212a2f @ 0.3 | 1 up div._7ozb2ub._7ozb2ua bg #ffffff shadow #212a2f 0px 0px 0px 0.5px outline 3px solid #212a2f @ 0.3 | 1 up div._7ozb2ub._7ozb2ua bg #ffffff shadow #212a2f 0px 0px 0px 0.5px outline 3px solid #212a2f @ 0.3 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-input-default.png`, `login-input-focused.png`, `login-input-filled.png`.

#### login-submit

Sign-in button. Measured, never pressed; signing in was out of scope. The account page is Shopify-hosted (Shop account UI).

Page: account. Selector: `login submit`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 345 x 50 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #5433eb | #4524db |
| Box shadow | none | = |
| Outline | none | = |
| Font | GTStandard-M 14px/21px 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | = |
| Text node | span.mx-auto.flex: GTStandard-M 16px/22px 500, #ffffff, ls -0.5px | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 38.39 x 16, colour #ffffff | = |
| Painted layers | button.relative.m-0 345.0x50.0 bg #5433eb r 8px | button.relative.m-0 345.0x50.0 bg #4524db r 8px |
| How | at rest | mouse hover |

Crops: `login-submit-default.png`, `login-submit-hover.png`.

#### email-input

Email field. The footer subscribe field. Text was typed and deleted; never submitted.

Page: home. Selector: `footer input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 384 x 42 | = | = |
| Padding | 10px 80px 10px 12px | = | = |
| Border | 1px solid #212121 | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | 1px auto #005fcc offset 0px | 1px auto #005fcc offset 0px |
| Font | Geograph 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #212121 | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | oklch(0.551 0.027 264.364), opacity 1 | = | = |
| Painted layers | input.h-full.w-full 384.0x42.0 bg #ffffff border T:1px solid #212121 / R:1px solid #212121 / B:1px solid #212121 / L:1px solid #212121 r 3.35544e+07px | input.h-full.w-full 384.0x42.0 bg #ffffff border T:1px solid #212121 / R:1px solid #212121 / B:1px solid #212121 / L:1px solid #212121 r 3.35544e+07px outline 1px auto #005fcc offset 0px | input.h-full.w-full 384.0x42.0 bg #ffffff border T:1px solid #212121 / R:1px solid #212121 / B:1px solid #212121 / L:1px solid #212121 r 3.35544e+07px outline 1px auto #005fcc offset 0px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `email-input-default.png`, `email-input-focused.png`, `email-input-filled.png`.

#### signup-button

Sign Up button. .btn.btn-outline on the subscribe row. Measured, never submitted.

Page: home. Selector: `footer button[type=submit]`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 81.58 x 31 | = | = |
| Padding | 8px 16px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | Geograph 12px/15px 700 | = | = |
| Letter spacing | 0.3px | = | = |
| Colour | #212121 | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) delay 0s, 0s, 0s, 0s | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | CDP forcePseudoState :active:hover |
| Opacity | - | = | 0.85 |
| Painted layers | - | = | button.btn.btn-outline 81.6x31.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |

Crops: `signup-button-default.png`, `signup-button-hover.png`, `signup-button-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The rounded pill bar: hamburger, wordmark, search and bag icons.

Page: home. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 46 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #212121 |
| Box shadow | none |
| Outline | none |
| Font | Geograph 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.text-center.text-[10px]: Geograph 10px/15px 400, #ffffff, ls 0.5px |
| Transition | none |
| Icon | 24 x 24, colour #ffffff |
| Painted layers | div.relative 390.0x46.0 bg #212121 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-hamburger

Hamburger button. Opens the mobile menu drawer.

Page: home. Selector: `mobile menu button`. States: default, pressed.

| Property | default | pressed |
|---|---|---|
| Size (w x h) | 24 x 24 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 6px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geograph 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | default | = |
| Icon | 0 x 0, colour #000000 | = |
| Ancestor paint | 3 up div.absolute.top-5 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | = |
| How | at rest | CDP forcePseudoState :active:hover |

Crops: `m-hamburger-default.png`, `m-hamburger-pressed.png`.

#### m-menu-drawer

Mobile menu drawer. The sheet the hamburger opens: NEW ARRIVALS / SHOP ALL text rows, MEN and WOMEN with chevrons, and a footer of category links.

Page: home. Selector: `.header-mobile-menu`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 390 x 798 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geograph 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.flex-auto.pr-20: Geograph 14px/21px 500, #000000, ls 0.7px |
| Transition | none |
| Icon | 24 x 24, colour #000000 |
| Painted layers | span.bg-natural-white-60.fixed 390.0x844.0 bg #ece9e2; ul.flex.flex-col 350.0x131.0 bg #ffffff r 4px; div.bg-natural-white.relative 0.0x0.0 bg #e0dacf r 20px; div.bg-natural-white.relative 0.0x0.0 bg #e0dacf r 20px |
| How | at rest |

Crops: `m-menu-drawer-open.png`.

#### m-ai-chip

Shop with AI chip. The floating pill bottom-right: spark icon, label, close X. Never opened.

Page: home. Selector: `ai chip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 199.73 x 64 |
| Padding | 0px |
| Border | 2px solid oklab(0.260318 0.0000118539 0.00000520051 / 0.2) |
| Radius | 3.35544e+07px |
| Background | transparent |
| Box shadow | #000000 @ 0.25 0px 2px 20px 0px, #000000 @ 0.25 0px 0px 1px 0px |
| Outline | none |
| Font | Barlow 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.entrypoint-shimmer-text.min-w-0: Barlow 16px/22px 400, #000000 @ 0 |
| Transition | none |
| Cursor | pointer |
| Icon | 24 x 24, colour #ffffff |
| Painted layers | div.relative.max-w-[calc(var(--viewport-w,100vw)-2rem)] 199.7x64.0 border T:2px solid oklab(0.260318 0.0000118539 0.00000520051 / 0.2) / R:2px solid oklab(0.260318 0.0000118539 0.00000520051 / 0.2) / B:2px solid oklab(0.260318 0.0000118539 0.00000520051 / 0.2) / L:2px solid oklab(0.260318 0.0000118539 0.00000520051 / 0.2) r 3.35544e+07px shadow #000000 @ 0.25 0px 2px 20px 0px, #000000 @ 0.25 0px 0px 1px 0px; div.relative.isolate 195.7x60.0 bg #ffffff r 3.35544e+07px; div.flex-center.size-full 44.0x44.0 image linear-gradient(135deg, #2e3138 0%, #242424 30%, #666666 50%, #242424 70%, #2e3138 100%) r 3.35544e+07px; div.entrypoint-shimmer-text.min-w-0 85.7x24.0 image linear-gradient(90deg, #242424 0%, #242424 30%, #707070 45%, #bdbdbd 50%, #707070 55%, #24; div.entrypoint-beam-dot.absolute 80.0x80.0 image radial-gradient(closest-side, #242424, #000000 @ 0) |
| How | at rest |

Crops: `m-ai-chip-default.png`.

### Home

#### hero

Hero. The first band: a rounded-corner photo card carrying the "Wildly Comfortable. Super Natural." headline and the two pill CTAs.

Page: home. Selector: `hero container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1420 x 784 |
| Padding | 0px |
| Border | none |
| Radius | 20px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geograph 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.z-content.relative: Akkurat Mono 12px/20px 500, #ffffff, ls 1.2px |
| Transition | none |
| Painted layers | a.btn.btn-primary 122.3x33.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 3.35544e+07px; a.btn.btn-primary 122.3x33.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 3.35544e+07px |
| How | at rest |

Crops: `hero-default.png`.

#### hero-title

Hero title. Display copy in the brand serif, fluid-sized.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 414.53 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geograph 24px/32px 400 |
| Letter spacing | 0.6px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### cta-primary

Primary button. .btn.btn-primary: the white pill CTA ("SHOP MEN"), xs medium uppercase tracking-wider.

Page: home. Selector: `a.btn.btn-primary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 122.25 x 33 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | 1px solid #ffffff | 1px solid #212121 | = | 1px solid #212121 |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff | #212121 | = | #212121 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto oklch(0.546 0.245 262.881) offset 1px | = |
| Font | Geograph 12px/15px 500 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #212121 | #ffffff | = | #ffffff |
| Transition | background-color, color, border-color, opacity 0.2s, 0.2s, 0.2s, 0.2s cubic-bezier(0.37, 0, 0.63, 1), cubic-bezier(0.37, 0, 0.63, 1), cubic-bezier(0.37, 0, 0.63, 1), cubic-bezier(0.61, 1, 0.88, 1) delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.btn-primary 122.3x33.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 3.35544e+07px | a.btn.btn-primary 122.3x33.0 bg #212121 border T:1px solid #212121 / R:1px solid #212121 / B:1px solid #212121 / L:1px solid #212121 r 3.35544e+07px | a.btn.btn-primary 122.3x33.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 3.35544e+07px outline 1px auto oklch(0.546 0.245 262.881) offset 1px | a.btn.btn-primary 122.3x33.0 bg #212121 border T:1px solid #212121 / R:1px solid #212121 / B:1px solid #212121 / L:1px solid #212121 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-primary-default.png`, `cta-primary-hover.png`, `cta-primary-focus-visible.png`, `cta-primary-pressed.png`.

#### cta-outline-white

Outline button. .btn.btn-outline-white: the bordered pill used on category cards.

Page: home. Selector: `a.btn.btn-outline-white`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 122.25 x 33 | = |
| Padding | 8px 16px | = |
| Border | 1px solid #ffffff | = |
| Radius | 3.35544e+07px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geograph 12px/15px 500 | = |
| Letter spacing | 0.3px | = |
| Colour | #ffffff | = |
| Transition | background-color, color, border-color, opacity 0.2s, 0.2s, 0.2s, 0.2s cubic-bezier(0.37, 0, 0.63, 1), cubic-bezier(0.37, 0, 0.63, 1), cubic-bezier(0.37, 0, 0.63, 1), cubic-bezier(0.61, 1, 0.88, 1) delay 0s, 0s, 0s, 0s | = |
| Cursor | pointer | = |
| Painted layers | a.category-row-item-cta-button.btn 122.3x33.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 3.35544e+07px | = |
| How | at rest | mouse hover |

Crops: `cta-outline-white-default.png`, `cta-outline-white-hover.png`.

#### section-title

Section title. Marketing section headline in the brand serif, fluid 30-40px.

Page: home. Selector: `h2.font-serif`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 407.92 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Self Modern 40px/60px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### carousel-nav

Carousel arrow. A 24-40px round icon button at the edge of a product/media carousel.

Page: home. Selector: `.swiper-prev-button`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 24 x 24 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geograph 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | none | = |
| Cursor | default | = |
| Icon | 24 x 24, colour #ffffff | = |
| How | at rest | mouse hover |

Crops: `carousel-nav-default.png`, `carousel-nav-hover.png`.

## Transitions declared in the readable stylesheets

Gauth's own CSS is served cross-origin, so this list holds only what the CSSOM could read on each page (antd's CSS-in-JS and inline styles); the per-state Transition rows above are computed values and cover Gauth's own rules.

- collection: `background-color .2s var(--ease-sine-in-out),color .2s var(--ease-sine-in-out),border-color .2s var(--ease-sine-in-out),opacity .2s var(--ease-sine-out)`, `transform 50ms ease-in-out`, `opacity .2s var(--ease-sine-in-out)`, `opacity .2s var(--ease-sine-out)`, `opacity .8s var(--ease-sine-out)`, `opacity 0.3s`, `transform 0.2s, top 0.2s`, `transform 0.2s, left 0.2s`, `transform 0.2s, right 0.2s`, `opacity 0.2s, transform 0.1s`, `opacity .2s var(--ease-sine-in)`, `top 0.3s cubic-bezier(0.215, 0.61, 0.355, 1)`

- home: `background-color .2s var(--ease-sine-in-out),color .2s var(--ease-sine-in-out),border-color .2s var(--ease-sine-in-out),opacity .2s var(--ease-sine-out)`, `transform 50ms ease-in-out`, `opacity .2s var(--ease-sine-in-out)`, `opacity .2s var(--ease-sine-out)`, `opacity .8s var(--ease-sine-out)`, `opacity 0.3s`, `transform 0.2s, top 0.2s`, `transform 0.2s, left 0.2s`, `transform 0.2s, right 0.2s`, `opacity 0.2s, transform 0.1s`, `opacity .2s var(--ease-sine-in)`, `top 0.3s cubic-bezier(0.215, 0.61, 0.355, 1)`

- product: `background-color .2s var(--ease-sine-in-out),color .2s var(--ease-sine-in-out),border-color .2s var(--ease-sine-in-out),opacity .2s var(--ease-sine-out)`, `transform 50ms ease-in-out`, `opacity .2s var(--ease-sine-in-out)`, `opacity .2s var(--ease-sine-out)`, `opacity .8s var(--ease-sine-out)`, `opacity 0.3s`, `transform 0.2s, top 0.2s`, `transform 0.2s, left 0.2s`, `transform 0.2s, right 0.2s`, `opacity 0.2s, transform 0.1s`, `opacity .2s var(--ease-sine-in)`, `top 0.3s cubic-bezier(0.215, 0.61, 0.355, 1)`
