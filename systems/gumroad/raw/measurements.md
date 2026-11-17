# Component measurements

Computed styles read from gumroad.com and ichigo.gumroad.com on 2026-11-17 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is the field clicked into (nothing typed); `dark` is the same element after the colour-scheme emulation repainted the page through the product's own @media (prefers-color-scheme:dark) theme — gumroad.com has no in-page toggle, and the product subdomain pins a light palette so its dark reads are skipped unpainted; `opened` and the rest are resting states reached by a component's own UI toggle. Nothing was typed, sent, bought or signed into.

## Components

### Site chrome

#### nav-bar

Header bar. The hero header over Discover: wordmark, search, the auth buttons and the category nav.

Page: /discover. Selector: `header.hero, header`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 1440 x 217 | = |
| Padding | 32px 64px | = |
| Border | T: none; R: none; B: 1px solid #000000; L: none | T: none; R: none; B: 1px solid #dddddd @ 0.35; L: none |
| Radius | 0px | = |
| Background | #f4f4f0 | #242423 |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABC Favorit 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | #dddddd |
| Text node | span.inline-block.aspect-115/22: ABC Favorit 16px/22px 400, #000000 | span.inline-block.aspect-115/22: ABC Favorit 16px/22px 400, #dddddd |
| Transition | none | = |
| Icon | 20 x 20, colour #000000 | 20 x 20, colour #dddddd |
| Painted layers | header.hero.relative 1440.0x217.0 bg #f4f4f0 border B:1px solid; span.inline-block.aspect-115/22 245.0x46.9 bg #000000; div.inline-flex.items-center 819.0x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; input.font-[inherit].py-3 789.0x46.0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; datalist.absolute.top-full 0.0x0.0 bg #ffffff border R:1px solid / B:1px solid / L:1px solid r 0px 0px 4px 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px; a.inline-flex.items-center 79.0x48.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px | header.hero.relative 1440.0x217.0 bg #242423 border B:1px solid; span.inline-block.aspect-115/22 245.0x46.9 bg #dddddd; div.inline-flex.items-center 819.0x48.0 bg #000000 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; input.font-[inherit].py-3 789.0x46.0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; datalist.absolute.top-full 0.0x0.0 bg #000000 border R:1px solid / B:1px solid / L:1px solid r 0px 0px 4px 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #dddddd 4px 4px 0px 0px; a.inline-flex.items-center 79.0x48.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px |
| How | resting state | same element after the colour-scheme emulation repainted the page through @media (prefers-color-scheme:dark) |

Crops: `nav-bar-default.png`, `nav-bar-dark.png`.

#### nav-logo

Wordmark link. The GUMROAD wordmark, uppercased display type, linking home.

Page: /discover. Selector: `header a (Gumroad)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 245 x 46.86 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABC Favorit 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.inline-block.aspect-115/22: ABC Favorit 16px/22px 400, #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | span.inline-block.aspect-115/22 245.0x46.9 bg #000000 | = |
| How | resting state | mouse hover over the element |

Crops: `nav-logo-default.png`, `nav-logo-hover.png`.

#### nav-search

Search combobox. The "Search products" field — a combobox that opens a suggestion menu; "focused" is the field clicked into, nothing typed.

Page: /discover. Selector: `header input[role="combobox"], header input`. States: default, focused, dark.

| Property | default | focused | dark |
|---|---|---|---|
| Size (w x h) | 789 x 46 | = | = |
| Padding | 12px 16px | = | = |
| Border | none | = | = |
| Radius | 4px | = | = |
| Background | transparent | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = |
| Font | ABC Favorit 16px/22px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | #dddddd |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000 @ 0.5, opacity 1 | = | #dddddd @ 0.5, opacity 1 |
| Painted layers | input.font-[inherit].py-3 789.0x46.0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Ancestor paint | 1 up div.inline-flex.items-center bg #ffffff | 1 up div.inline-flex.items-center bg #ffffff outline 2px solid #ff90e8 | 1 up div.inline-flex.items-center bg #000000 |
| How | resting state | the field clicked into | same element after the colour-scheme emulation repainted the page through @media (prefers-color-scheme:dark) |

Crops: `nav-search-default.png`, `nav-search-focused.png`, `nav-search-dark.png`.

#### nav-login

"Log in" button. The bordered auth button beside the primary CTA.

Page: /discover. Selector: `header a (Log in)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 79 x 48 | = | - |
| Padding | 12px 16px | = | - |
| Gap | 8px | = | - |
| Border | 1px solid #000000 | = | - |
| Radius | 4px | = | - |
| Background | transparent | = | - |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px | - |
| Outline | none | = | - |
| Font | ABC Favorit 16px/22px 400 | = | - |
| Letter spacing | normal | = | - |
| Colour | #000000 | = | - |
| Transition | transform, translate, scale, rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | - |
| Cursor | pointer | = | - |
| Painted layers | a.inline-flex.items-center 79.0x48.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px | a.inline-flex.items-center 79.0x48.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px | - |
| How | resting state | mouse hover over the element | - |
| ::after | - | 82px x 51px, absolute, bg #000000 @ 0, radius 0px | = |
| Error | - | = | keyboard focus never reached the target — focus-visible state not measurable |

Crops: `nav-login-default.png`, `nav-login-hover.png`.

#### nav-start-selling

"Start selling" button. The filled primary auth CTA — primary background, contrast-primary text.

Page: /discover. Selector: `header a (Start selling)`. States: default, hover, focus-visible, pressed, dark.

| Property | default | hover | focus-visible | pressed | dark |
|---|---|---|---|---|---|
| Size (w x h) | 121 x 48 | = | = | = | = |
| Padding | 12px 16px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | 1px solid #000000 | = | = | = | 1px solid #dddddd @ 0.35 |
| Radius | 4px | = | = | = | = |
| Background | #000000 | #ff90e8 | = | #ff90e8 | #dddddd |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 1px auto #101010 offset 1px | = | = |
| Font | ABC Favorit 16px/22px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | #000000 | = | #000000 | #000000 |
| Transition | transform, translate, scale, rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | a.inline-flex.items-center 121.0x48.0 bg #000000 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px | a.inline-flex.items-center 121.0x48.0 bg #ff90e8 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px | a.inline-flex.items-center 121.0x48.0 bg #000000 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px outline 1px auto #101010 offset 1px | a.inline-flex.items-center 121.0x48.0 bg #ff90e8 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 121.0x48.0 bg #dddddd border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press | same element after the colour-scheme emulation repainted the page through @media (prefers-color-scheme:dark) |
| ::after | - | 124px x 51px, absolute, bg #000000 @ 0, radius 0px | = | 124px x 51px, absolute, bg #000000 @ 0, radius 0px | = |

Crops: `nav-start-selling-default.png`, `nav-start-selling-hover.png`, `nav-start-selling-focus-visible.png`, `nav-start-selling-pressed.png`, `nav-start-selling-dark.png`.

#### nav-category

Category nav link. A link in the categories nav ("Design") — underlined text links on the header bar.

Page: /discover. Selector: `header a[href="/design"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 76 x 40 | = | = |
| Padding | 8px 12px | = | = |
| Gap | 8px | = | = |
| Border | 1px solid #000000 @ 0 | 1px solid #000000 | = |
| Radius | 3.35544e+07px | = | = |
| Background | transparent | #ffffff | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | ABC Favorit 16px/22px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | transform, translate, scale, rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | a.inline-flex.items-center 76.0x40.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px | a.inline-flex.items-center 76.0x40.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px | a.inline-flex.items-center 76.0x40.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px outline 1px auto #101010 offset 1px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| ::after | - | 79px x 43px, absolute, bg #000000 @ 0, radius 0px | = |

Crops: `nav-category-default.png`, `nav-category-hover.png`, `nav-category-focus-visible.png`.

#### nav-category-active

Category nav link, current. "All" — the current category, painted with the active marker.

Page: /discover. Selector: `header a[href="/discover"] (All)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 45 x 40 |
| Padding | 8px 12px |
| Gap | 8px |
| Border | 1px solid #000000 |
| Radius | 3.35544e+07px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | ABC Favorit 16px/22px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | transform, translate, scale, rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | a.inline-flex.items-center 45.0x40.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px |
| How | resting state |

Crops: `nav-category-active-default.png`.

### Discover

#### discover-featured-card

Featured product card. A large card in the Featured products carousel: cover, title, blurb, creator, rating and the price flag.

Page: /discover. Selector: `div.override article`. States: default, hover, dark.

| Property | default | hover | dark |
|---|---|---|---|
| Size (w x h) | 704 x 380 | = | = |
| Padding | 0px | = | = |
| Border | 1px solid #000000 | = | 1px solid #dddddd @ 0.35 |
| Radius | 4px | = | = |
| Background | #ffffff | = | #000000 |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px | = |
| Outline | none | = | = |
| Font | ABC Favorit 16px/22px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | #dddddd |
| Text node | h2.line-clamp-3.gap-3: ABC Favorit 20px/26px 400, #000000 | = | h2.line-clamp-3.gap-3: ABC Favorit 20px/26px 400, #dddddd |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Icon | 20 x 20, colour #000000 | = | 20 x 20, colour #dddddd |
| Painted layers | article.relative.flex 704.0x380.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; figure.aspect-square.overflow-hidden 378.0x378.0 border R:1px solid r 4px 0px 0px 4px; img.aspect-square.w-5 20.0x20.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; div.relative.grid 119.0x32.0 border T:1px solid / B:1px solid / L:1px solid; div.bg-accent-with-text.px-2 102.0x30.0 bg #ff90e8; div.border-border.border-r-transparent 16.0x30.0 border T:15px solid / R:15px solid / B:15px solid / L:1px solid | article.relative.flex 704.0x380.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px; figure.aspect-square.overflow-hidden 378.0x378.0 border R:1px solid r 4px 0px 0px 4px; img.aspect-square.w-5 20.0x20.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; div.relative.grid 119.0x32.0 border T:1px solid / B:1px solid / L:1px solid; div.bg-accent-with-text.px-2 102.0x30.0 bg #ff90e8; div.border-border.border-r-transparent 16.0x30.0 border T:15px solid / R:15px solid / B:15px solid / L:1px solid | article.relative.flex 704.0x380.0 bg #000000 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; figure.aspect-square.overflow-hidden 378.0x378.0 border R:1px solid r 4px 0px 0px 4px; img.aspect-square.w-5 20.0x20.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; div.relative.grid 119.0x32.0 border T:1px solid / B:1px solid / L:1px solid; div.bg-accent-with-text.px-2 102.0x30.0 bg #ff90e8; div.border-border.border-r-transparent 16.0x30.0 border T:15px solid / R:15px solid / B:15px solid / L:1px solid |
| How | resting state | mouse hover over the element | same element after the colour-scheme emulation repainted the page through @media (prefers-color-scheme:dark) |

Crops: `discover-featured-card-default.png`, `discover-featured-card-hover.png`, `discover-featured-card-dark.png`.

#### discover-pager-arrow

Carousel pager arrow. The small square arrow button beside the "1 / 8" counter in the Featured header.

Page: /discover. Selector: `section (Featured) button`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | ABC Favorit 16px/22px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 24 x 24, colour #000000 | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `discover-pager-arrow-default.png`, `discover-pager-arrow-hover.png`, `discover-pager-arrow-focus-visible.png`.

#### discover-card

Product card (market grid). A card in the "On the market" grid: cover block, title, creator, rating row and the price cell in the footer.

Page: /discover. Selector: `div.grid-cols-2 article`. States: default, hover, focus-visible, dark.

| Property | default | hover | focus-visible | dark |
|---|---|---|---|---|
| Size (w x h) | 301.33 x 522.33 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #000000 | = | = | 1px solid #dddddd @ 0.35 |
| Radius | 4px | = | = | = |
| Background | #ffffff | = | = | #000000 |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px | = | = |
| Outline | none | = | = | = |
| Font | ABC Favorit 16px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | #dddddd |
| Text node | h4.line-clamp-4.lg:text-xl: ABC Favorit 20px/28px 400, #000000 | = | = | h4.line-clamp-4.lg:text-xl: ABC Favorit 20px/28px 400, #dddddd |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Icon | 20 x 20, colour #000000 | = | = | 20 x 20, colour #dddddd |
| Painted layers | article.relative.flex 301.3x522.3 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; figure.aspect-square.overflow-hidden 299.3x299.3 border B:1px solid r 4px 4px 0px 0px; header.flex.flex-1 299.3x157.0 border B:1px solid; img.aspect-square.w-5 20.0x20.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; div.relative.grid 107.0x32.0 border T:1px solid / B:1px solid / L:1px solid; div.bg-accent-with-text.px-2 90.0x30.0 bg #ff90e8 | article.relative.flex 301.3x522.3 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px; figure.aspect-square.overflow-hidden 299.3x299.3 border B:1px solid r 4px 4px 0px 0px; header.flex.flex-1 299.3x157.0 border B:1px solid; img.aspect-square.w-5 20.0x20.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; div.relative.grid 107.0x32.0 border T:1px solid / B:1px solid / L:1px solid; div.bg-accent-with-text.px-2 90.0x30.0 bg #ff90e8 | article.relative.flex 301.3x522.3 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; figure.aspect-square.overflow-hidden 299.3x299.3 border B:1px solid r 4px 4px 0px 0px; header.flex.flex-1 299.3x157.0 border B:1px solid; a.no-underline.before:absolute 267.3x56.0 outline 1px auto #101010 offset 1px; img.aspect-square.w-5 20.0x20.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; div.relative.grid 107.0x32.0 border T:1px solid / B:1px solid / L:1px solid | article.relative.flex 301.3x522.3 bg #000000 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; figure.aspect-square.overflow-hidden 299.3x299.3 border B:1px solid r 4px 4px 0px 0px; header.flex.flex-1 299.3x157.0 border B:1px solid; img.aspect-square.w-5 20.0x20.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; div.relative.grid 107.0x32.0 border T:1px solid / B:1px solid / L:1px solid; div.bg-accent-with-text.px-2 90.0x30.0 bg #ff90e8 |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | same element after the colour-scheme emulation repainted the page through @media (prefers-color-scheme:dark) |

Crops: `discover-card-default.png`, `discover-card-hover.png`, `discover-card-focus-visible.png`, `discover-card-dark.png`.

#### discover-card-price

Price flag. The price cell in a card footer — the accent flag tag ("SGD 47.67").

Page: /discover. Selector: `article footer (price)`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 102 x 30 | = |
| Padding | 4px 8px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #ff90e8 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABC Favorit 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Painted layers | div.bg-accent-with-text.px-2 102.0x30.0 bg #ff90e8 | = |
| How | resting state | same element after the colour-scheme emulation repainted the page through @media (prefers-color-scheme:dark) |

Crops: `discover-card-price-default.png`, `discover-card-price-dark.png`.

#### discover-card-rating

Rating stars row. The star rating in a card footer ("5.0 (6)").

Page: /discover. Selector: `article footer (rating)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 24 x 22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Favorit 16px/22px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | resting state |

Crops: `discover-card-rating-default.png`.

#### discover-tab

Market tab. A tab in the market switcher ("Trending" / "Best Sellers" / "Hot & New") — a bordered pill link.

Page: /discover. Selector: `a[role="tab"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 114 x 40 | = | - |
| Padding | 8px 12px | = | - |
| Border | 1px solid #000000 @ 0 | 1px solid #000000 | - |
| Radius | 3.35544e+07px | = | - |
| Background | transparent | = | - |
| Box shadow | none | = | - |
| Outline | none | = | - |
| Font | ABC Favorit 16px/22px 400 | = | - |
| Letter spacing | normal | = | - |
| Colour | #000000 | = | - |
| Transition | none | = | - |
| Cursor | pointer | = | - |
| Painted layers | a.border.no-underline 114.0x40.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px | = | - |
| How | resting state | mouse hover over the element | - |
| Error | - | = | keyboard focus never reached the target — focus-visible state not measurable |

Crops: `discover-tab-default.png`, `discover-tab-hover.png`.

#### discover-tab-active

Market tab, selected. "Trending" — the selected tab, filled with the inverted colours.

Page: /discover. Selector: `a[role="tab"][aria-selected="true"]`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 91 x 40 | = |
| Padding | 8px 12px | = |
| Border | 1px solid #000000 | 1px solid #dddddd @ 0.35 |
| Radius | 3.35544e+07px | = |
| Background | #ffffff | #000000 |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABC Favorit 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | #dddddd |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | a.border.no-underline 91.0x40.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px | a.border.no-underline 91.0x40.0 bg #000000 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px |
| How | resting state | same element after the colour-scheme emulation repainted the page through @media (prefers-color-scheme:dark) |

Crops: `discover-tab-active-default.png`, `discover-tab-active-dark.png`.

#### discover-filters

Filters disclosure. The "Filters" details/summary panel — "opened" is its own disclosure press.

Page: /discover. Selector: `details`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 310 x 55 | 310 x 277 |
| Padding | 16px | = |
| Gap | 16px | = |
| Border | T: none; R: none; B: 1px solid #000000; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABC Favorit 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | summary.flex.cursor-pointer: ABC Favorit 16px/22px 400, #000000 | = |
| Transition | none | = |
| Icon | 20 x 20, colour #000000 | = |
| Painted layers | details.flex-wrap.items-center 310.0x55.0 border B:1px solid; input.appearance-none.size-[calc(1lh+0.125rem)] 24.0x24.0 bg #ff90e8 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; input.appearance-none.size-[calc(1lh+0.125rem)] 24.0x24.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; input.appearance-none.size-[calc(1lh+0.125rem)] 24.0x24.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; input.appearance-none.size-[calc(1lh+0.125rem)] 24.0x24.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; input.appearance-none.size-[calc(1lh+0.125rem)] 24.0x24.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | details.flex-wrap.items-center 310.0x277.0 border B:1px solid; input.appearance-none.size-[calc(1lh+0.125rem)] 24.0x24.0 bg #ff90e8 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; input.appearance-none.size-[calc(1lh+0.125rem)] 24.0x24.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; input.appearance-none.size-[calc(1lh+0.125rem)] 24.0x24.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; input.appearance-none.size-[calc(1lh+0.125rem)] 24.0x24.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; input.appearance-none.size-[calc(1lh+0.125rem)] 24.0x24.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px |
| Ancestor paint | 1 up div.grid.divide-y bg #ffffff | = |
| How | resting state | the disclosure's own press |

Crops: `discover-filters-default.png`, `discover-filters-opened.png`.

#### discover-filter-checkbox

Filter checkbox. A checkbox row inside the open Filters panel (the square box with the tick).

Page: /discover. Selector: `details[open] input`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 24 x 24 | = |
| Padding | 0px | = |
| Border | 1px solid #000000 | = |
| Radius | 8px | = |
| Background | #ff90e8 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Arial 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #545454 | = |
| Transition | none | = |
| Opacity | 0.3 | = |
| Cursor | not-allowed | = |
| Placeholder | #545454, opacity 1 | = |
| Painted layers | input.appearance-none.size-[calc(1lh+0.125rem)] 24.0x24.0 bg #ff90e8 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | = |
| How | resting state | mouse hover over the element |

Crops: `discover-filter-checkbox-default.png`, `discover-filter-checkbox-hover.png`.

#### discover-load-more

"Load more" button. The bordered pagination button under the market grid.

Page: /discover. Selector: `button (Load more)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 113 x 48 | = | = | - |
| Padding | 12px 16px | = | = | - |
| Gap | 8px | = | = | - |
| Border | 1px solid #000000 | = | = | - |
| Radius | 4px | = | = | - |
| Background | transparent | = | = | - |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px | = | - |
| Outline | none | = | 1px auto #101010 offset 0px | - |
| Font | ABC Favorit 16px/22px 400 | = | = | - |
| Letter spacing | normal | = | = | - |
| Colour | #000000 | = | = | - |
| Transition | transform, translate, scale, rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | - |
| Cursor | pointer | = | = | - |
| Painted layers | button.inline-flex.items-center 113.0x48.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px | button.inline-flex.items-center 113.0x48.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px | button.inline-flex.items-center 113.0x48.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px outline 1px auto #101010 offset 0px | - |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | - |
| ::after | - | 116px x 51px, absolute, bg #000000 @ 0, radius 0px | = | = |
| Error | - | = | = | cdpSession.send: Protocol error (DOM.getNodeForLocation): No node found at given location |

Crops: `discover-load-more-default.png`, `discover-load-more-hover.png`, `discover-load-more-focus-visible.png`.

#### discover-currency-select

Currency select. The currency picker at the foot of the page ("$ (US Dollars)").

Page: /discover. Selector: `select`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 338 x 48 | = |
| Padding | 12px 44px 12px 16px | = |
| Border | 1px solid #000000 | = |
| Radius | 4px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABC Favorit 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | default | = |
| Painted layers | select.font-[inherit].py-3 338.0x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px | = |
| How | resting state | mouse hover over the element |

Crops: `discover-currency-select-default.png`, `discover-currency-select-hover.png`.

### Home

#### home-hero

Hero section. The landing hero ("Go from 0 to $1") — display heading over the brand illustration.

Page: /. Selector: `main header, header.grid`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 1440 x 776 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #f4f4f0 | #000000 |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABC Favorit 16px/26px 400 | = |
| Letter spacing | -0.4px | = |
| Colour | #000000 | #ffffff |
| Text node | h1.leading-none.text-6xl: ABC Favorit 96px/96px 400, #000000, ls -0.4px | h1.leading-none.text-6xl: ABC Favorit 96px/96px 400, #ffffff, ls -0.4px |
| Transition | none | = |
| Icon | 24 x 24, colour #242423 | 24 x 24, colour #ffffff @ 0.7 |
| Painted layers | header.grid.grid-cols-1 1440.0x776.0 bg #f4f4f0; div.absolute.inset-0 189.8x64.0 bg #f1f333 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; div.absolute.inset-0 189.8x64.0 bg #dc341e border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; a.relative.inline-flex 189.8x64.0 bg #000000 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; input.!bg-gray.mr-8 420.0x64.0 bg #f4f4f0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; button.bg-white.dark:bg-dark-gray 42.0x42.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 6px | header.grid.grid-cols-1 1440.0x776.0 bg #000000; div.absolute.inset-0 189.8x64.0 bg #f1f333 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; div.absolute.inset-0 189.8x64.0 bg #dc341e border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; a.relative.inline-flex 189.8x64.0 bg #ff90e8 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; input.!bg-gray.mr-8 420.0x64.0 bg #242423 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; button.bg-white.dark:bg-dark-gray 42.0x42.0 bg #242423 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 6px |
| Ancestor paint | 1 up div.bg-gray.dark:bg-black bg #f4f4f0 | 1 up div.bg-gray.dark:bg-black bg #000000 |
| How | resting state | same element after the colour-scheme emulation repainted the page through @media (prefers-color-scheme:dark) |

Crops: `home-hero-default.png`, `home-hero-dark.png`.

#### home-h1

Hero heading. The display headline in ABC Favorit.

Page: /. Selector: `h1`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 672.02 x 96 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABC Favorit 96px/96px 400 | = |
| Letter spacing | -0.4px | = |
| Colour | #000000 | #ffffff |
| Transition | none | = |
| How | resting state | same element after the colour-scheme emulation repainted the page through @media (prefers-color-scheme:dark) |

Crops: `home-h1-default.png`, `home-h1-dark.png`.

#### home-search

Marketplace search field. The hero's "Search marketplace" input with its own search button.

Page: /. Selector: `input#marketplace-search, form input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 420 x 64 | = |
| Padding | 0px 80px 0px 32px | = |
| Border | 1px solid #242423 | = |
| Radius | 4px | = |
| Background | #f4f4f0 | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ff90e8 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = |
| Font | ABC Favorit 20px/28px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #757575, opacity 1 | = |
| Painted layers | input.!bg-gray.mr-8 420.0x64.0 bg #f4f4f0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px | input.!bg-gray.mr-8 420.0x64.0 bg #f4f4f0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ff90e8 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| How | resting state | the field clicked into |

Crops: `home-search-default.png`, `home-search-focused.png`.

#### home-search-button

Search button. The square button attached to the hero search field.

Page: /. Selector: `form button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 42 x 42 | = | = | = |
| Padding | 8px | = | = | = |
| Border | 1px solid #242423 | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 24 x 24, colour #242423 | = | = | = |
| Painted layers | button.bg-white.dark:bg-dark-gray 42.0x42.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 6px | = | button.bg-white.dark:bg-dark-gray 42.0x42.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 6px outline 1px auto #101010 offset 0px | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `home-search-button-default.png`, `home-search-button-hover.png`, `home-search-button-focus-visible.png`, `home-search-button-pressed.png`.

#### home-subscribe-input

Email capture field. The footer email field of the "subscribe" form.

Page: /. Selector: `form input[type="email"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 560.41 x 48 |
| Padding | 0px 16px |
| Border | 1px solid #ffffff @ 0.3 |
| Radius | 4px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Favorit 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | text |
| Placeholder | #ffffff @ 0.5, opacity 1 |
| Painted layers | input.w-full.h-12 560.4x48.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px |
| How | resting state |

Crops: `home-subscribe-input-default.png`.

#### home-footer

Page footer. The footer strip with the link columns.

Page: /. Selector: `footer, main > section:last-child`. States: .

Not found on the page at capture time.

#### home-subscribe-form

Subscribe form. The email capture form row at the foot of the landing page — the field plus its arrow submit.

Page: /. Selector: `form.flex.gap-1, form`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 630.41 x 48 | = |
| Padding | 0px | = |
| Gap | 4px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABC Favorit 16px/26px 400 | = |
| Letter spacing | -0.4px | = |
| Colour | #ffffff | = |
| Text node | button.relative.inline-flex: Arial 16px/24px 400, #000000 | = |
| Transition | none | = |
| Painted layers | input.w-full.h-12 560.4x48.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; div.absolute.inset-0 66.0x48.0 bg #f1f333 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; div.absolute.inset-0 66.0x48.0 bg #dc341e border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; button.relative.inline-flex 66.0x48.0 bg #ff90e8 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px | = |
| How | resting state | same element after the colour-scheme emulation repainted the page through @media (prefers-color-scheme:dark) |

Crops: `home-subscribe-form-default.png`, `home-subscribe-form-dark.png`.

### Auth

#### login-card

Login form card. The centred card: OAuth buttons, the divider, the email/password fieldset and the submit.

Page: /login. Selector: `form`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 736 x 738 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABC Favorit 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | #dddddd |
| Text node | button.inline-flex.items-center: ABC Favorit 16px/22px 400, #ffffff | = |
| Transition | none | = |
| Icon | 20 x 20, colour #ffffff | = |
| Painted layers | button.inline-flex.items-center 736.0x48.0 bg #000000 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; button.inline-flex.items-center 736.0x48.0 bg #5383ec border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; button.inline-flex.items-center 736.0x48.0 bg #000000 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; button.inline-flex.items-center 736.0x48.0 bg #625bf6 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; div::before.override.grid 348.5pxx0px border B:1px solid; div::after.override.grid 348.5pxx0px border B:1px solid | = |
| How | resting state | same element after the colour-scheme emulation repainted the page through @media (prefers-color-scheme:dark) |

Crops: `login-card-default.png`, `login-card-dark.png`.

#### login-oauth

OAuth button. An identity-provider button ("Apple" / "Google" / "X" / "Stripe") — full-width bordered.

Page: /login. Selector: `form button`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 736 x 48 | = | = |
| Padding | 12px 16px | = | = |
| Gap | 8px | = | = |
| Border | 1px solid #000000 | = | = |
| Radius | 4px | = | = |
| Background | #000000 | = | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px | = |
| Outline | none | = | 1px auto #101010 offset 0px |
| Font | ABC Favorit 16px/22px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | transform, translate, scale, rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 20 x 20, colour #ffffff | = | = |
| Painted layers | button.inline-flex.items-center 736.0x48.0 bg #000000 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px | button.inline-flex.items-center 736.0x48.0 bg #000000 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px | button.inline-flex.items-center 736.0x48.0 bg #000000 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px outline 1px auto #101010 offset 0px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| ::after | - | 739px x 51px, absolute, bg #000000 @ 0, radius 0px | = |

Crops: `login-oauth-default.png`, `login-oauth-hover.png`, `login-oauth-focus-visible.png`.

#### login-email

Email input. The labelled email field — measured, never typed into.

Page: /login. Selector: `form input[type="email"]`. States: default, focused, dark.

| Property | default | focused | dark |
|---|---|---|---|
| Size (w x h) | 736 x 48 | = | = |
| Padding | 12px 16px | = | = |
| Border | 1px solid #000000 | = | 1px solid #dddddd @ 0.35 |
| Radius | 4px | = | = |
| Background | #ffffff | = | #000000 |
| Box shadow | none | = | = |
| Outline | none | 2px solid #ff90e8 offset 0px | = |
| Font | ABC Favorit 16px/22px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | #dddddd |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000, opacity 1 | = | #dddddd, opacity 1 |
| Painted layers | input.font-[inherit].py-3 736.0x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px | input.font-[inherit].py-3 736.0x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px outline 2px solid #ff90e8 offset 0px | input.font-[inherit].py-3 736.0x48.0 bg #000000 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px |
| How | resting state | the field clicked into | same element after the colour-scheme emulation repainted the page through @media (prefers-color-scheme:dark) |

Crops: `login-email-default.png`, `login-email-focused.png`, `login-email-dark.png`.

#### login-password

Password input. The password field with its "Show password" eye button.

Page: /login. Selector: `form input[type="password"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 702 x 46 |
| Padding | 12px 16px |
| Border | none |
| Radius | 4px |
| Background | transparent |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | ABC Favorit 16px/22px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | text |
| Placeholder | #000000, opacity 1 |
| Painted layers | input.font-[inherit].py-3 702.0x46.0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Ancestor paint | 1 up div.inline-flex.items-center bg #ffffff |
| How | resting state |

Crops: `login-password-default.png`.

#### login-submit

"Login" button. The filled submit — measured and hovered only, never pressed for real.

Page: /login. Selector: `form button (Login)`. States: default, hover, focus-visible, pressed, dark.

| Property | default | hover | focus-visible | pressed | dark |
|---|---|---|---|---|---|
| Size (w x h) | 736 x 48 | = | = | = | = |
| Padding | 12px 16px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | 1px solid #000000 | = | = | = | 1px solid #dddddd @ 0.35 |
| Radius | 4px | = | = | = | = |
| Background | #000000 | #ff90e8 | = | = | #dddddd |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = | = |
| Font | ABC Favorit 16px/22px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | #000000 | = | = | #000000 |
| Transition | transform, translate, scale, rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | button.inline-flex.items-center 736.0x48.0 bg #000000 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px | button.inline-flex.items-center 736.0x48.0 bg #ff90e8 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px | button.inline-flex.items-center 736.0x48.0 bg #000000 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px outline 1px auto #101010 offset 0px | = | button.inline-flex.items-center 736.0x48.0 bg #dddddd border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press | same element after the colour-scheme emulation repainted the page through @media (prefers-color-scheme:dark) |
| ::after | - | 739px x 51px, absolute, bg #000000 @ 0, radius 0px | = | = | = |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-focus-visible.png`, `login-submit-pressed.png`, `login-submit-dark.png`.

#### login-forgot

"Forgot your password?" link. The muted recovery link inside the password fieldset.

Page: /login. Selector: `form a (Forgot)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 168 x 22 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABC Favorit 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | resting state | mouse hover over the element |

Crops: `login-forgot-default.png`, `login-forgot-hover.png`.

### Product page

#### product-header

Product header. The title block over the buy panel on a <creator>.gumroad.com/l/ page.

Page: https://ichigo.gumroad.com/l/ichigo-reader. Selector: `article header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 758.66 x 96 |
| Padding | 24px |
| Gap | 16px |
| Border | T: none; R: 1px solid #000000; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Favorit 16px/22px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.wrap-break-word: ABC Favorit 40px/48px 400, #000000 |
| Transition | none |
| Painted layers | header.grid.gap-4 758.7x96.0 border R:1px solid |
| Ancestor paint | 1 up article.relative.grid bg #ffffff |
| How | resting state |

Crops: `product-header-default.png`.

#### product-tier

Tier option (radio). A priced tier card — a radio-style button carrying the price and tier emoji label.

Page: https://ichigo.gumroad.com/l/ichigo-reader. Selector: `[role="radio"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 331.34 x 100 | = |
| Padding | 12px 16px | = |
| Gap | 12px | = |
| Border | 1px solid #36a9ae | = |
| Radius | 4px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #36a9ae 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #36a9ae 0px 0px 0px 1px, #000000 4px 4px 0px 0px |
| Outline | none | = |
| Font | ABC Favorit 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | div.inline-flex.align-middle: ABC Favorit 16px/22px 400, #000000 | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.cursor-pointer.text-current 331.3x100.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #36a9ae 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; div.inline-flex.align-middle 160.0x40.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px | button.cursor-pointer.text-current 331.3x100.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #36a9ae 0px 0px 0px 1px, #000000 4px 4px 0px 0px; div.inline-flex.align-middle 160.0x40.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px |
| How | resting state | mouse hover over the element |
| ::after | - | 334.344px x 103px, absolute, bg #000000 @ 0, radius 0px |

Crops: `product-tier-default.png`, `product-tier-hover.png`.

#### product-term-select

Billing term select. The "Monthly | Yearly" select in the buy controls.

Page: https://ichigo.gumroad.com/l/ichigo-reader. Selector: `select`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 331.34 x 48 | = | = |
| Padding | 12px 44px 12px 16px | = | = |
| Border | 1px solid #000000 | = | = |
| Radius | 4px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #36a9ae offset 0px |
| Font | ABC Favorit 16px/22px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | default | = | = |
| Painted layers | select.font-[inherit].py-3 331.3x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px | = | select.font-[inherit].py-3 331.3x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px outline 2px solid #36a9ae offset 0px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `product-term-select-default.png`, `product-term-select-hover.png`, `product-term-select-focus-visible.png`.

#### product-buy

Purchase link. The "Subscribe"/"I want this" link that navigates to gumroad.com/checkout — measured, never followed in this run.

Page: https://ichigo.gumroad.com/l/ichigo-reader. Selector: `a (Subscribe/I want this)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 109 x 48 | = | = | - |
| Padding | 12px 16px | = | = | - |
| Gap | 8px | = | = | - |
| Border | 1px solid #000000 | = | = | - |
| Radius | 4px | = | = | - |
| Background | #36a9ae | = | = | - |
| Box shadow | none | = | = | - |
| Outline | none | = | 1px auto #101010 offset 1px | - |
| Font | ABC Favorit 16px/22px 400 | = | = | - |
| Letter spacing | normal | = | = | - |
| Colour | #000000 | = | = | - |
| Transition | transform, translate, scale, rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | - |
| Cursor | pointer | = | = | - |
| Painted layers | a.inline-flex.items-center 109.0x48.0 bg #36a9ae border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px | = | a.inline-flex.items-center 109.0x48.0 bg #36a9ae border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px outline 1px auto #101010 offset 1px | - |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | - |
| Error | - | = | = | cdpSession.send: Protocol error (DOM.getNodeForLocation): No node found at given location |

Crops: `product-buy-default.png`, `product-buy-hover.png`, `product-buy-focus-visible.png`.

#### product-wishlist

"Add to wishlist" control. The combobox-shaped wishlist picker beside the purchase link.

Page: https://ichigo.gumroad.com/l/ichigo-reader. Selector: `[role="combobox"] (wishlist)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 219.34 x 48 | = |
| Padding | 12px 16px | = |
| Border | 1px solid #000000 | = |
| Radius | 4px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABC Favorit 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.flex-1.truncate: ABC Favorit 16px/22px 400, #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 20 x 20, colour #000000 | = |
| Painted layers | div.flex.cursor-pointer 219.3x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px | = |
| How | resting state | mouse hover over the element |

Crops: `product-wishlist-default.png`, `product-wishlist-hover.png`.

#### product-share

"Share" button + popover. The Share button; "opened" is its own popover state.

Page: https://ichigo.gumroad.com/l/ichigo-reader. Selector: `button (Share)`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 104 x 48 | = | = |
| Padding | 12px 16px | = | = |
| Gap | 8px | = | = |
| Border | 1px solid #000000 | = | = |
| Radius | 4px | = | = |
| Background | transparent | = | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | ABC Favorit 16px/22px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | transform, translate, scale, rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 20 x 20, colour #000000 | = | = |
| Painted layers | button.inline-flex.items-center 104.0x48.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px | button.inline-flex.items-center 104.0x48.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px | button.inline-flex.items-center 104.0x48.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | resting state | mouse hover over the element | the button's own press, opening the share popover |
| ::after | - | 107px x 51px, absolute, bg #000000 @ 0, radius 0px | 107px x 51px, absolute, bg #000000 @ 0, radius 0px |

Crops: `product-share-default.png`, `product-share-hover.png`, `product-share-opened.png`.

#### product-ratings

Ratings + reviews. The ratings column beside the buy panel — the 4.1 summary, the star histogram and the review feed under it.

Page: https://ichigo.gumroad.com/l/ichigo-reader. Selector: `article section (Ratings)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 379.34 x 1783.3 |
| Padding | 24px |
| Gap | 16px |
| Border | T: 1px solid #000000; R: none; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Favorit 16px/22px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3: ABC Favorit 18.4px/25.3px 400, #000000 |
| Transition | none |
| Icon | 20 x 20, colour #000000 |
| Painted layers | section.grid.gap-4 379.3x1783.3 border T:1px solid; meter.h-[1lh].w-full 223.3x22.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; meter.h-[1lh].w-full 223.3x22.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; meter.h-[1lh].w-full 223.3x22.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; meter.h-[1lh].w-full 223.3x22.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; meter.h-[1lh].w-full 223.3x22.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px |
| How | resting state |

Crops: `product-ratings-default.png`.

#### product-review-load

"Load more" reviews. The underlined reviews pagination button.

Page: https://ichigo.gumroad.com/l/ichigo-reader. Selector: `button (Load more)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 331.34 x 22 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABC Favorit 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | resting state | mouse hover over the element |

Crops: `product-review-load-default.png`, `product-review-load-hover.png`.

#### product-footer

"Powered by Gumroad" footer. The slim footer under the product page — the brand link and currency select.

Page: https://ichigo.gumroad.com/l/ichigo-reader. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 176 |
| Padding | 64px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Favorit 16px/22px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div: ABC Favorit 16px/22px 400, #000000 |
| Transition | none |
| Icon | 20 x 20, colour #000000 @ 0.5 |
| Painted layers | span.inline-block.aspect-115/22 115.0x22.0 bg #000000; select.font-[inherit].py-3 338.0x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px |
| How | resting state |

Crops: `product-footer-default.png`.

### Checkout

#### checkout-summary

Order summary card. The cart block: item thumbnail with quantity badge, Edit/Remove, the "Give as a gift?" toggle and the totals.

Page: https://gumroad.com/checkout. Selector: `div#app div.grid.gap-8 > div > div:first-child`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 832 x 567 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Favorit 16px/22px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: ABC Favorit 12px/16px 400, #ffffff |
| Transition | none |
| Icon | 20 x 20, colour #000000 @ 0.5 |
| Painted layers | div.rounded-sm.border 832.0x257.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; figure.tailwind-override.overflow-hidden 120.0x120.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; div.absolute.top-0 24.0x24.0 bg #000000 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; button.inline-flex.items-center 60.0x32.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; button.inline-flex.items-center 60.0x32.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; div.border-t.border-border 830.0x55.0 border T:1px solid |
| How | resting state |

Crops: `checkout-summary-default.png`.

#### checkout-gift-toggle

"Give as a gift?" switch. The iOS-style switch — measured, never toggled.

Page: https://gumroad.com/checkout. Selector: `[role="switch"], [role="checkbox"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 34 x 20 | = |
| Padding | 0px | = |
| Border | 1px solid #000000 | = |
| Radius | 3.35544e+07px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Arial 13.3333px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Placeholder | #000000, opacity 1 | = |
| ::after | 14px x 14px, absolute, bg #000000, radius 8px | = |
| Painted layers | input.cursor-pointer.appearance-none 34.0x20.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; input::after.cursor-pointer.appearance-none 14pxx14px bg #000000 r 8px | = |
| How | resting state | mouse hover over the element |

Crops: `checkout-gift-toggle-default.png`, `checkout-gift-toggle-hover.png`.

#### checkout-email

Email field. The labelled Email address input — measured as found, never typed into.

Page: https://gumroad.com/checkout. Selector: `input[type="email"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 374 x 48 | = |
| Padding | 12px 16px | = |
| Border | 1px solid #000000 | = |
| Radius | 4px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | 2px solid #36a9ae offset 0px |
| Font | ABC Favorit 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #000000, opacity 1 | = |
| Painted layers | input.font-[inherit].py-3 374.0x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px | input.font-[inherit].py-3 374.0x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px outline 2px solid #36a9ae offset 0px |
| How | resting state | the field clicked into |

Crops: `checkout-email-default.png`, `checkout-email-focused.png`.

#### checkout-name

Full name field. The labelled Full name input.

Page: https://gumroad.com/checkout. Selector: `input[id*="fullName" i]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 374 x 48 |
| Padding | 12px 16px |
| Border | 1px solid #000000 |
| Radius | 4px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | ABC Favorit 16px/22px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | text |
| Placeholder | #000000, opacity 1 |
| Painted layers | input.font-[inherit].py-3 374.0x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px |
| How | resting state |

Crops: `checkout-name-default.png`.

#### checkout-country

Country select. The country picker, pre-detected to the visitor's region.

Page: https://gumroad.com/checkout. Selector: `select`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 790 x 48 | = | = |
| Padding | 12px 44px 12px 16px | = | = |
| Border | 1px solid #000000 | = | = |
| Radius | 4px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #36a9ae offset 0px |
| Font | ABC Favorit 16px/22px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | default | = | = |
| Painted layers | select.font-[inherit].py-3 790.0x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px | = | select.font-[inherit].py-3 790.0x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px outline 2px solid #36a9ae offset 0px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `checkout-country-default.png`, `checkout-country-hover.png`, `checkout-country-focus-visible.png`.

#### checkout-currency

Currency select. The "SGD$ (Singapore Dollars) — detected" select in the totals column.

Page: https://gumroad.com/checkout. Selector: `select (currency)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 374 x 48 |
| Padding | 12px 44px 12px 16px |
| Border | 1px solid #000000 |
| Radius | 4px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | ABC Favorit 16px/22px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | default |
| Painted layers | select.font-[inherit].py-3 374.0x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px |
| How | resting state |

Crops: `checkout-currency-default.png`.

#### checkout-pay

Pay button. The filled pay submit at the foot of the payment column — measured, never pressed.

Page: https://gumroad.com/checkout. Selector: `button[type="submit"], button (Pay)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 374 x 56 | = |
| Padding | 16px | = |
| Gap | 12px | = |
| Border | 1px solid #000000 | = |
| Radius | 4px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABC Favorit 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.font-medium: ABC Favorit 16px/22px 500, #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 20 x 20, colour #000000 | = |
| Painted layers | button.box-border.flex 374.0x56.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px | = |
| How | resting state | mouse hover over the element |

Crops: `checkout-pay-default.png`, `checkout-pay-hover.png`.

### Site chrome (mobile)

#### m-nav-bar

Mobile header. The header at 390px: wordmark, search and the menu button.

Page: /discover. Selector: `header.hero, header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 243.86 |
| Padding | 32px 16px |
| Border | T: none; R: none; B: 1px solid #000000; L: none |
| Radius | 0px |
| Background | #f4f4f0 |
| Box shadow | none |
| Outline | none |
| Font | ABC Favorit 16px/22px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.inline-block.aspect-115/22: ABC Favorit 16px/22px 400, #000000 |
| Transition | none |
| Icon | 20 x 20, colour #000000 |
| Painted layers | header.hero.relative 390.0x243.9 bg #f4f4f0 border B:1px solid; span.inline-block.aspect-115/22 245.0x46.9 bg #000000; div.inline-flex.items-center 294.0x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; input.font-[inherit].py-3 264.0x46.0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; datalist.absolute.top-full 0.0x0.0 bg #ffffff border R:1px solid / B:1px solid / L:1px solid r 0px 0px 4px 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 4px 4px 0px 0px; button.inline-flex.items-center 48.0x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px |
| How | resting state |

Crops: `m-nav-bar-default.png`.

#### m-nav-menu-button

Menu button. The button that opens the mobile nav panel.

Page: /discover. Selector: `header button, nav button`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 24 x 24 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABC Favorit 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 24 x 24, colour #000000 | = |
| How | resting state | mouse hover over the element |

Crops: `m-nav-menu-button-default.png`, `m-nav-menu-button-hover.png`.

### Discover (mobile)

#### m-discover-card

Product card, phone. A market-grid card at 390px — the grid collapses to a single column.

Page: /discover. Selector: `article`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 234 x 498 |
| Padding | 0px |
| Border | 1px solid #000000 |
| Radius | 4px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | ABC Favorit 16px/22px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.line-clamp-3.gap-3: ABC Favorit 20px/26px 400, #000000 |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 20 x 20, colour #000000 |
| Painted layers | article.relative.flex 234.0x498.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; figure.aspect-square.overflow-hidden 232.0x232.0 border B:1px solid r 4px 4px 0px 0px; header.flex.flex-1 232.0x145.0 border B:1px solid; img.aspect-square.w-5 20.0x20.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; div.flex-1.p-4 232.0x65.0 border B:1px solid; div.relative.grid 109.0x32.0 border T:1px solid / B:1px solid / L:1px solid |
| How | resting state |

Crops: `m-discover-card-default.png`.

## Transitions declared in the readable stylesheets

gumroad.com serves its design-*.css bundle cross-origin (assets.gumroad.com), invisible to the CSSOM, so this list only covers the per-page inline <style> blocks the CSSOM could read; the bundle's transition declarations are in css-vars.json instead.

- /: `transform 0.1s linear`

- /discover: `transform 0.1s linear`

- /login: `transform 0.1s linear`

- https://gumroad.com/checkout?product=rsMja&option=6Fm6gGP9cDXYcJRRo8U3pA%3D%3D&recurrence=monthly&quantity=1: `transform 0.1s linear`

- https://ichigo.gumroad.com/l/ichigo-reader: `transform 0.1s linear`
