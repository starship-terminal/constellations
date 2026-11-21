# Component measurements

Computed styles read from craftwork.design on 2026-11-12 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the home page, /pricing, /components, /catalog, /black-friday and /login — the cookie notice hidden, never answered — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### promo-banner

Promo banner. The Black Friday countdown bar above the nav ("Lifetime Pro for $224 instead of $449 · Ends in · See the deal").

Page: home. Selector: `countdown bar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 36 |
| Padding | 0px 16px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | #161616 |
| Box shadow | none |
| Outline | none |
| Font | euclidCircularALightWebS 13px/19.5px 400 |
| Letter spacing | normal |
| Colour | #f2f2f2 |
| Text node | span.font-medium: euclidCircularALightWebS 13px/19.5px 500, #f2f2f2 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 14 x 14, colour #f2f2f2 |
| Painted layers | a.group.relative 1440.0x36.0 bg #161616; span.inline-flex.h-[22px] 34.0x22.0 bg #ffffff @ 0.06 r 5px; span.inline-flex.h-[22px] 34.0x22.0 bg #ffffff @ 0.06 r 5px; span.inline-flex.h-[22px] 36.1x22.0 bg #ffffff @ 0.06 r 5px; span.inline-flex.h-[22px] 34.0x22.0 bg #ffffff @ 0.06 r 5px |
| How | at rest |

Crops: `promo-banner-default.png`.

#### nav

Nav bar. The top bar: craftwork logo, Assets/Templates/Inspiration dropdowns, search, Pricing, theme toggle, Sign in and the black Connect agent pill.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | euclidCircularALightWebS 16px/24px 400 |
| Letter spacing | -0.32px |
| Colour | #000000 |
| Text node | span.font-semibold.leading-none: euclidCircularALightWebS 20px/20px 600, #000000, ls -0.8px |
| Transition | none |
| Icon | 26 x 26, colour #000000 |
| Painted layers | span.pointer-events-none.absolute 0.0x36.0 bg #000000 @ 0.07 r 8px; div.absolute.left-0 892.4x502.5 bg #ffffff @ 0.9 r 24px shadow #000000 @ 0.14 0px 12px 28px -8px, #000000 @ 0.22 0px 30px 70px -24px; a.flex.items-center 201.8x34.9 bg #7f7f7f @ 0.14 r 12px; div.border-t.border-other-stroke 201.8x47.5 border T:1px solid #000000 @ 0.098; span.relative.block 206.9x155.2 bg #7f7f7f @ 0.1 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #7f7f7f @ 0.1 0px 0px 0px 1px inset; span.header-mega-shimmer.absolute 206.9x155.2 image linear-gradient(100deg, #000000 @ 0 30%, #000000 @ 0.05 50%, #000000 @ 0 70%) |
| Ancestor paint | 1 up div.v11.v12 bg #ffffff |
| How | at rest |

Crops: `nav-default.png`.

#### logo

Logo. The craftwork wordmark anchor.

Page: home. Selector: `logo anchor`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 128.78 x 34 |
| Padding | 4px |
| Gap | 7px |
| Border | none |
| Radius | 6px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | euclidCircularALightWebS 16px/24px 400 |
| Letter spacing | -0.32px |
| Colour | #000000 |
| Text node | span.font-semibold.leading-none: euclidCircularALightWebS 20px/20px 600, #000000, ls -0.8px |
| Transition | none |
| Cursor | pointer |
| Icon | 26 x 26, colour #000000 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link. A nav item (36px h-9 row); measured, never followed.

Page: home. Selector: `nav item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 83.2 x 36 | = | = | 80.71 x 34.92 |
| Padding | 0px 6px 0px 10px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #606060 offset 2px | = |
| Font | euclidCircularALightWebS 16px/22px 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #606060 | #000000 | = | #000000 |
| Transition | color, transform 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #606060 | 16 x 16, colour #000000 | = | 15.52 x 15.52, colour #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.relative.z-10 83.2x36.0 r 8px outline 2px solid #606060 offset 2px | = |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### search-field

Search field. The nav search field with the CMD-K hint; opens a search overlay, never typed into.

Page: home. Selector: `nav search`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 350 x 38 | = | = | = |
| Padding | 0px 8px 0px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #fafafa | #ededed @ 0.698 | = | #ededed @ 0.698 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #606060 offset 2px | = |
| Font | euclidCircularALightWebS 16px/24px 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.flex-1.text-left: euclidCircularALightWebS 16px/22px 400, #999999, ls -0.32px | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #999999 | = | = | = |
| Painted layers | button.header-search.w-[350px] 350.0x38.0 bg #fafafa r 9999px; div.header-search-kbd.bg-background-surface-4 39.9x20.0 bg #ededed @ 0.698 r 9999px | button.header-search.w-[350px] 350.0x38.0 bg #ededed @ 0.698 r 9999px; div.header-search-kbd.bg-background-surface-4 39.9x20.0 bg #ededed @ 0.698 r 9999px | button.header-search.w-[350px] 350.0x38.0 bg #fafafa r 9999px outline 2px solid #606060 offset 2px; div.header-search-kbd.bg-background-surface-4 39.9x20.0 bg #ededed @ 0.698 r 9999px | button.header-search.w-[350px] 350.0x38.0 bg #ededed @ 0.698 r 9999px; div.header-search-kbd.bg-background-surface-4 39.9x20.0 bg #ededed @ 0.698 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-field-default.png`, `search-field-hover.png`, `search-field-focus-visible.png`, `search-field-pressed.png`.

#### theme-toggle

Theme toggle. The nav theme switch (aria-label "Dark theme"): flips data-theme between the painted light and dark surfaces.

Page: home. Selector: `button[aria-label*=theme]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | 31.04 x 31.04 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #000000 @ 0.07 | = | #000000 @ 0.1 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #606060 offset 2px | = |
| Font | euclidCircularALightWebS 16px/24px 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | background-color, color, transform 0.18s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #000000 | = | = | 17.46 x 17.46, colour #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.flex.size-11 32.0x32.0 bg #000000 @ 0.07 r 8px | button.flex.size-11 32.0x32.0 r 8px outline 2px solid #606060 offset 2px | button.flex.size-11 31.0x31.0 bg #000000 @ 0.1 r 8px |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `theme-toggle-default.png`, `theme-toggle-hover.png`, `theme-toggle-focus-visible.png`, `theme-toggle-pressed.png`.

#### signin-link

Sign-in link. The "Sign in" nav link (leads to /login); measured, never followed.

Page: home. Selector: `nav Sign in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 71.39 x 36 | = | = | 69.25 x 34.92 |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #000000 @ 0.07 | = | #000000 @ 0.1 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #606060 offset 2px | = |
| Font | euclidCircularALightWebS 16px/22px 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #606060 | #000000 | = | #000000 |
| Transition | background-color, color, transform 0.18s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.inline-flex.h-11 71.4x36.0 bg #000000 @ 0.07 r 8px | button.inline-flex.h-11 71.4x36.0 r 8px outline 2px solid #606060 offset 2px | button.inline-flex.h-11 69.2x34.9 bg #000000 @ 0.1 r 8px |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `signin-link-default.png`, `signin-link-hover.png`, `signin-link-focus-visible.png`, `signin-link-pressed.png`.

#### connect-cta

Connect agent pill. The black "Connect agent" nav pill; measured, never followed.

Page: home. Selector: `nav Connect agent`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 126.98 x 30 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #1e1e1e | #383838 | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #606060 offset 2px | = |
| Font | euclidCircularALightWebS 16px/22px 500 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.relative.inline-flex: euclidCircularALightWebS 16px/22px 500, #ffffff, ls -0.32px | = | = | = |
| Transition | transform 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.flex-row 127.0x30.0 bg #1e1e1e r 8px; span.pointer-events-none.absolute 53.2x30.0 image linear-gradient(90deg, #000000 @ 0, #808080 @ 0.32, #000000 @ 0) | a.flex.flex-row 127.0x30.0 bg #383838 r 8px; span.pointer-events-none.absolute 53.2x30.0 image linear-gradient(90deg, #000000 @ 0, #808080 @ 0.32, #000000 @ 0) | a.flex.flex-row 127.0x30.0 bg #1e1e1e r 8px outline 2px solid #606060 offset 2px; span.pointer-events-none.absolute 53.2x30.0 image linear-gradient(90deg, #000000 @ 0, #808080 @ 0.32, #000000 @ 0) | a.flex.flex-row 127.0x30.0 bg #000000 r 8px; span.pointer-events-none.absolute 53.2x30.0 image linear-gradient(90deg, #000000 @ 0, #808080 @ 0.32, #000000 @ 0) |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, -1) | = | matrix(1, 0, 0, 1, 0, -1) |

Crops: `connect-cta-default.png`, `connect-cta-hover.png`, `connect-cta-focus-visible.png`, `connect-cta-pressed.png`.

### Home

#### hero-h1

Hero headline. The 68px Euclid Circular hero ("UI kits, templates and fonts made by real designers").

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 835.84 x 141.44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | euclidCircularALightWebS 68px/70.72px 600 |
| Letter spacing | -2.38px |
| Colour | #000000 |
| Text node | span.home-blur-char.inline-block: euclidCircularALightWebS 68px/70.72px 600, #000000, ls -2.38px |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-sub

Hero subline. "4,000+ packs for Figma, Framer, Webflow and code by 570+ independent designers."

Page: home. Selector: `hero subline`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 544 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | euclidCircularALightWebS 20px/30px 400 |
| Letter spacing | -0.32px |
| Colour | #606060 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-cta

Hero CTA. The black "Get full access" hero button (leads to pricing); measured, never followed.

Page: home. Selector: `hero Get full access`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 178.52 x 46 | = | = | 174.95 x 45.08 |
| Padding | 0px 20px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #1e1e1e | #383838 | = | #000000 |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.45 0px 10px 24px -12px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.45 0px 10px 24px -12px |
| Outline | none | = | 2px solid #606060 offset 2px | = |
| Font | euclidCircularALightWebS 16px/22px 500 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.relative.inline-flex: euclidCircularALightWebS 16px/22px 500, #ffffff, ls -0.32px | = | = | = |
| Transition | all 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | = | = | 23.52 x 23.52, colour #ffffff |
| Painted layers | a.flex.flex-row 178.5x46.0 bg #1e1e1e r 10px; span.pointer-events-none.absolute 76.2x46.0 image linear-gradient(90deg, #000000 @ 0, #808080 @ 0.32, #000000 @ 0) | a.flex.flex-row 178.5x46.0 bg #383838 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.45 0px 10px 24px -12px; span.pointer-events-none.absolute 76.2x46.0 image linear-gradient(90deg, #000000 @ 0, #808080 @ 0.32, #000000 @ 0) | a.flex.flex-row 178.5x46.0 bg #1e1e1e r 10px outline 2px solid #606060 offset 2px; span.pointer-events-none.absolute 76.2x46.0 image linear-gradient(90deg, #000000 @ 0, #808080 @ 0.32, #000000 @ 0) | a.flex.flex-row 174.9x45.1 bg #000000 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.45 0px 10px 24px -12px; span.pointer-events-none.absolute 74.7x45.1 image linear-gradient(90deg, #000000 @ 0, #808080 @ 0.32, #000000 @ 0) |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, -2) | = | matrix(0.98, 0, 0, 0.98, 0, -2) |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-cta-2

Hero secondary. The light "Browse the catalog" hero button; measured, never followed.

Page: home. Selector: `hero Browse the catalog`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 181.02 x 46 | = | = | 177.4 x 45.08 |
| Padding | 0px 20px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #efefef | #e1e1e1 | = | #e1e1e1 |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.08 0px 1px 0px 0px inset | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.08 0px 1px 0px 0px inset |
| Outline | none | = | 2px solid #606060 offset 2px | = |
| Font | euclidCircularALightWebS 16px/22px 500 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.relative.inline-flex: euclidCircularALightWebS 16px/22px 500, #000000, ls -0.32px | = | = | = |
| Transition | all 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.flex-row 181.0x46.0 bg #efefef r 10px | a.flex.flex-row 181.0x46.0 bg #e1e1e1 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.08 0px 1px 0px 0px inset | a.flex.flex-row 181.0x46.0 bg #efefef r 10px outline 2px solid #606060 offset 2px | a.flex.flex-row 177.4x45.1 bg #e1e1e1 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.08 0px 1px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `hero-cta-2-default.png`, `hero-cta-2-hover.png`, `hero-cta-2-focus-visible.png`, `hero-cta-2-pressed.png`.

#### product-card

Product card. A catalog product card in the home rail (artwork, name, "from $N" price); measured, never followed.

Page: home. Selector: `product card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 362.67 x 311 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #606060 offset 2px | = |
| Font | euclidCircularALightWebS 16px/24px 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.min-w-0.truncate: euclidCircularALightWebS 18px/22px 500, #000000, ls -0.36px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.block 362.7x311.0 outline 2px solid #000000 @ 0 offset 2px; div.absolute.w-full 362.7x272.0 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 10px | = | a.group.block 362.7x311.0 outline 2px solid #606060 offset 2px; span.block.group-focus-visible:rounded-[10px] 362.7x272.0 r 10px outline 2px solid #606060 offset 2px; div.absolute.w-full 362.7x272.0 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 10px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `product-card-default.png`, `product-card-hover.png`, `product-card-focus-visible.png`, `product-card-pressed.png`.

### Pricing

#### price-h1

Pricing headline. "Browse for free. Go Pro to use it all."

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 500.97 x 132 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | euclidCircularALightWebS 62px/66px 600 |
| Letter spacing | -2.4px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: none.

#### plan-card

Plan card. A pricing plan card (name, price, feature list, CTA); measured, never purchased.

Page: pricing. Selector: `plan card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 547.19 x 340 | = | - | = |
| Padding | 24px 0px 0px 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | euclidCircularALightWebS 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | span.min-w-0.flex-1: euclidCircularALightWebS 14px/21px 400, #606060 | = | - | = |
| Transition | none | = | - | = |
| Icon | 16 x 16, colour #ffffff | = | - | = |
| Painted layers | span.pointer-events-none.absolute 437.8x192.0 bg #000000 @ 0.03 r 9999px; span.absolute.inset-0 419.2x224.3 bg #f4f4f4 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.45 0px 24px 48px -16px; span.absolute.inset-0 455.9x244.5 bg #f4f4f4 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.45 0px 24px 48px -16px; span.absolute.inset-0 493.1x265.1 bg #f4f4f4 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.45 0px 24px 48px -16px; span.absolute.inset-0 490.9x263.1 image linear-gradient(#000000 @ 0 35%, #f4f4f4 100%); div.border.border-stroke-primary 443.0x55.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 16px | span.pointer-events-none.absolute 437.8x192.0 bg #000000 @ 0.03 r 9999px; span.absolute.inset-0 416.5x230.0 bg #f4f4f4 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.45 0px 24px 48px -16px; span.absolute.inset-0 451.6x249.7 bg #f4f4f4 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.45 0px 24px 48px -16px; span.absolute.inset-0 486.9x269.6 bg #f4f4f4 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.45 0px 24px 48px -16px; span.absolute.inset-0 484.9x267.6 image linear-gradient(#000000 @ 0 35%, #f4f4f4 100%); div.border.border-stroke-primary 443.0x55.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 16px | - | = |
| Ancestor paint | 1 up li.group.relative bg #f4f4f4 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px inset | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: none.

#### plan-price

Plan price. A plan price figure.

Page: pricing. Selector: `price figure`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 388 x 44 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | euclidCircularALightWebS 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.text-[40px].font-semibold: euclidCircularALightWebS 40px/44px 600, #000000, ls -1.6px |
| Transition | none |
| How | at rest |

Crops: none.

#### faq-row

FAQ row. A pricing FAQ accordion row; toggled locally, never submitted.

Page: pricing. Selector: `FAQ accordion row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 572 x 68 | = | = | = |
| Padding | 20px 0px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | euclidCircularALightWebS 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.flex-1.text-[17px]: euclidCircularALightWebS 17px/24px 500, #000000, ls -0.2px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 22.63 x 22.63, colour #ffffff | = | = | = |
| Painted layers | span.flex.size-7 39.6x39.6 bg #1e1e1e r 9999px | = | button.group.flex 572.0x68.0 outline 2px solid #000000 offset 2px; span.flex.size-7 39.6x39.6 bg #1e1e1e r 9999px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

### Catalog

#### components-h1

Components headline. "Components, 1,224" — the catalog count heading.

Page: components. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1 x 1 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | euclidCircularALightWebS 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `components-h1-default.png`.

#### components-filter

Filter field. A catalog filter/search input; measured in place, never submitted.

Page: components. Selector: `catalog input`. States: default, focus-visible, filled.

| Property | default | focus-visible | filled |
|---|---|---|---|
| Size (w x h) | 157 x 30 | = | 135 x 30 |
| Padding | 0px 8px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | euclidCircularALightWebS 14px/20px 400 | = | = |
| Letter spacing | -0.1px | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #999999, opacity 1 | #000000 @ 0, opacity 1 | #000000 @ 0, opacity 1 |
| Painted layers | input.h-full.w-full 157.0x30.0 outline 2px solid #000000 @ 0 offset 2px | = | input.h-full.w-full 135.0x30.0 outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up div.cursor-default.cursor-pointer bg #000000 @ 0.04 | 1 up div.cursor-default.cursor-pointer bg #000000 @ 0.07 | 1 up div.cursor-default.cursor-pointer bg #000000 @ 0.07 |
| How | at rest | Shift+Tab, Tab | filled state not recaptured; the typed crop was removed |

Crops: `components-filter-default.png`, `components-filter-focus-visible.png`. The filled crop was removed.

#### components-card

Catalog card. An asset card in the catalog grid; measured, never followed.

Page: components. Selector: `catalog asset card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Error | locator.evaluate: Timeout 8000ms exceeded. Call log:   - waiting for locator('[data-m-mark="catcard"]').visible().first().visible().first().visible().first()  | locator.hover: Timeout 5000ms exceeded. Call log:   - waiting for locator('[data-m-mark="catcard"]').visible().first().visible().first().visible().first()  | = | = |

Crops: none.

#### catalog-h1

Catalog headline. "Assets" — the catalog heading.

Page: catalog. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 472.38 x 47.52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | euclidCircularALightWebS 44px/47.52px 600 |
| Letter spacing | -1.32px |
| Colour | #000000 |
| Text node | span.inline-block.whitespace-pre: euclidCircularALightWebS 44px/47.52px 600, #000000, ls -1.32px |
| Transition | none |
| How | at rest |

Crops: `catalog-h1-default.png`.

#### catalog-filter

Filter field. A catalog filter/search input; measured in place, never submitted.

Page: catalog. Selector: `catalog input`. States: default, focus-visible, filled.

| Property | default | focus-visible | filled |
|---|---|---|---|
| Size (w x h) | 193 x 30 | = | 171 x 30 |
| Padding | 0px 8px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | euclidCircularALightWebS 14px/20px 400 | = | = |
| Letter spacing | -0.1px | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #999999, opacity 1 | #000000 @ 0, opacity 1 | #000000 @ 0, opacity 1 |
| Painted layers | input.h-full.w-full 193.0x30.0 outline 2px solid #000000 @ 0 offset 2px | = | input.h-full.w-full 171.0x30.0 outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up div.cursor-default.cursor-pointer bg #000000 @ 0.04 | 1 up div.cursor-default.cursor-pointer bg #000000 @ 0.07 | 1 up div.cursor-default.cursor-pointer bg #000000 @ 0.07 |
| How | at rest | Shift+Tab, Tab | filled state not recaptured; the typed crop was removed |

Crops: `catalog-filter-default.png`, `catalog-filter-focus-visible.png`. The filled crop was removed.

#### catalog-card

Catalog card. An asset card in the catalog grid; measured, never followed.

Page: catalog. Selector: `catalog asset card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1050 x 550.59 | = | = | = |
| Padding | 60px 0px 100px 0px | = | = | = |
| Gap | 30px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | euclidCircularALightWebS 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | p.text-[22px].font-semibold: euclidCircularALightWebS 22px/28px 600, #000000, ls -0.66px | = | = | = |
| Transition | none | = | = | = |
| Painted layers | a.flex.flex-row 167.0x38.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2f2b43 @ 0.1 0px -1px 0px 0px inset, #2f2b43 @ 0.1 0px 1px 3px 0px | = | a.flex.flex-row 167.0x38.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2f2b43 @ 0.1 0px -1px 0px 0px inset, #2f2b43 @ 0.1 0px 1px 3px 0px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `catalog-card-default.png`, `catalog-card-hover.png`, `catalog-card-focus-visible.png`, `catalog-card-pressed.png`.

#### library-row

Library row. A component-library row in the left list ("Smooth UI | 231"). The page's only h1 ("Components, 1,224") is a 1x1 accessibility heading.

Page: components. Selector: `library list row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 259 x 34 | = | = | = |
| Padding | 2px 8px 2px 2px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #000000 @ 0.07 | #000000 @ 0.04 | = | #000000 @ 0.04 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | euclidCircularALightWebS 14px/20px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.truncate.transition-opacity: euclidCircularALightWebS 14px/20px 400, #000000, ls -0.1px | = | = | = |
| Transition | background-color, color 0.18s, 0.18s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #525252 | = | = | = |
| Painted layers | a.cursor-default.cursor-pointer 259.0x34.0 bg #000000 @ 0.07 r 10px; span.catalog-tint-plate.flex 30.0x30.0 bg #a3a3a3 @ 0.16 r 8px | a.cursor-default.cursor-pointer 259.0x34.0 bg #000000 @ 0.04 r 10px; span.catalog-tint-plate.flex 30.0x30.0 bg #a3a3a3 @ 0.26 r 8px | a.cursor-default.cursor-pointer 259.0x34.0 bg #000000 @ 0.07 r 10px outline 1px auto #005fcc offset 1px; span.catalog-tint-plate.flex 30.0x30.0 bg #a3a3a3 @ 0.16 r 8px | a.cursor-default.cursor-pointer 259.0x34.0 bg #000000 @ 0.04 r 10px; span.catalog-tint-plate.flex 30.0x30.0 bg #a3a3a3 @ 0.26 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `library-row-default.png`, `library-row-hover.png`, `library-row-focus-visible.png`, `library-row-pressed.png`.

### Login

#### login-h1

Login headline. "Log in or sign up to ..." on the OTP auth card.

Page: login. Selector: `login heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 122.08 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | euclidCircularALightWebS 14px/20px 400 |
| Letter spacing | -0.1px |
| Colour | #606060 |
| Transition | none |
| How | at rest |

Crops: `login-h1-default.png`.

#### login-field

Email field. The "Your Email" OTP field (390 wide); filled with a placeholder for the shot, never submitted.

Page: login. Selector: `input[type=email]`. States: default, focus-visible, filled.

| Property | default | focus-visible | filled |
|---|---|---|---|
| Size (w x h) | 338 x 46 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | euclidCircularALightWebS 16px/22px 400 | = | = |
| Letter spacing | -0.32px | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #999999, opacity 1 | = | = |
| Painted layers | input.px-3.h-[46px] 338.0x46.0 outline 2px solid #000000 @ 0 offset 2px | = | = |
| Ancestor paint | 1 up div.px-3.h-[46px] bg #fafafa shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.02 0px 4px 4px 0px inset | 1 up div.px-3.h-[46px] bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.02 0px 4px 4px 0px inset | 1 up div.px-3.h-[46px] bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.02 0px 4px 4px 0px inset |
| How | at rest | Shift+Tab, Tab | filled state not recaptured; the typed crop was removed |

Crops: `login-field-default.png`, `login-field-focus-visible.png`. The filled crop was removed.

#### send-code

Send code button. The "Send code" submit (390x46); measured only — pressing it would send a one-time code, so it is never pressed.

Page: login. Selector: `Send code button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 46 |
| Padding | 0px 12px |
| Gap | 6px |
| Border | 1px solid #000000 @ 0.1 |
| Radius | 10px |
| Background | #efefef |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2f2b43 @ 0.1 0px -1px 0px 0px inset, #2f2b43 @ 0.1 0px 1px 3px 0px |
| Outline | none |
| Font | euclidCircularALightWebS 16px/22px 500 |
| Letter spacing | -0.32px |
| Colour | #000000 |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | default |
| Painted layers | button.flex.flex-row 390.0x46.0 bg #efefef border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2f2b43 @ 0.1 0px -1px 0px 0px inset, #2f2b43 @ 0.1 0px 1px 3px 0px |
| How | at rest |

Crops: `send-code-default.png`.

#### google-btn

Google SSO. The "Log in with Google" button; measured, OAuth never followed.

Page: login. Selector: `Google login button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 390 x 46 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #1e1e1e | #383838 | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | euclidCircularALightWebS 16px/22px 500 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.body-s-regular.text-text-icons-reversed: euclidCircularALightWebS 16px/22px 400, #ffffff, ls -0.32px | = | = | = |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | = | = | = |
| Painted layers | button.flex.flex-row 390.0x46.0 bg #1e1e1e r 10px | button.flex.flex-row 390.0x46.0 bg #383838 r 10px | button.flex.flex-row 390.0x46.0 bg #1e1e1e r 10px outline 1px auto #005fcc offset 0px | button.flex.flex-row 390.0x46.0 bg #000000 r 10px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `google-btn-default.png`, `google-btn-hover.png`, `google-btn-focus-visible.png`, `google-btn-pressed.png`.

### Footer

#### footer

Footer. The footer: category link columns and the legal row.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1400 x 938 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | euclidCircularALightWebS 16px/24px 400 |
| Letter spacing | -0.32px |
| Colour | #000000 |
| Text node | a.foot-note-medium.text-text-icons-tertiary: euclidCircularALightWebS 14px/20px 500, #999999, ls -0.28px |
| Transition | none |
| Icon | 20 x 20, colour #999999 |
| Painted layers | div.mx-auto.max-w-[1110px] 1110.0x938.0 bg #f4f4f4 r 24px; a.flex.items-center 157.2x32.0 bg #f9f9f9 r 10px; a.flex.items-center 121.9x32.0 bg #f9f9f9 r 10px; a.flex.items-center 97.6x32.0 bg #f9f9f9 r 10px; button.cursor-default.flex 30.0x30.0 bg #ededed @ 0.698 r 8px; nav.mt-10.flex 1020.0x101.0 border T:1px solid #000000 @ 0.1 |
| Ancestor paint | 1 up div.v11.v12 bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer link; measured, never followed.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 42.48 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #606060 offset 2px | = |
| Font | euclidCircularALightWebS 14px/20px 500 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #999999 | #000000 | = | #000000 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.foot-note-medium.text-text-icons-tertiary 42.5x20.0 outline 2px solid #606060 offset 2px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-icon

Social link. A social link in the footer.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 30 x 30 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f9f9f9 | = | #f9f9f9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #606060 offset 2px | = |
| Font | euclidCircularALightWebS 16px/24px 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #999999 | #000000 | = | #000000 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 20 x 20, colour #999999 | 20 x 20, colour #000000 | = | 20 x 20, colour #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.cursor-default.flex 30.0x30.0 bg #f9f9f9 r 8px | a.cursor-default.flex 30.0x30.0 r 8px outline 2px solid #606060 offset 2px | a.cursor-default.flex 30.0x30.0 bg #f9f9f9 r 8px |

Crops: `social-icon-default.png`, `social-icon-hover.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | euclidCircularALightWebS 16px/24px 400 |
| Letter spacing | -0.32px |
| Colour | #000000 |
| Text node | button.inline-flex.h-11: euclidCircularALightWebS 16px/22px 400, #606060, ls -0.32px |
| Transition | none |
| Icon | 26 x 26, colour #000000 |
| Painted layers | span.pointer-events-none.absolute 0.0x0.0 bg #000000 @ 0.07 r 8px; div.absolute.left-0 0.0x0.0 bg #ffffff @ 0.9 r 24px shadow #000000 @ 0.14 0px 12px 28px -8px, #000000 @ 0.22 0px 30px 70px -24px; a.flex.items-center 0.0x0.0 bg #7f7f7f @ 0.14 r 12px; div.border-t.border-other-stroke 0.0x0.0 border T:1px solid #000000 @ 0.098; span.relative.block 0.0x0.0 bg #7f7f7f @ 0.1 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #7f7f7f @ 0.1 0px 0px 0px 1px inset; span.header-mega-shimmer.absolute 0.0x0.0 image linear-gradient(100deg, #000000 @ 0 30%, #000000 @ 0.05 50%, #000000 @ 0 70%) |
| Ancestor paint | 1 up div.v11.v12 bg #ffffff |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The header menu button that opens the nav overlay.

Page: home. Selector: `header menu button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | 42.68 x 42.68 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | #000000 @ 0.1 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #606060 offset 2px | = |
| Font | euclidCircularALightWebS 16px/24px 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | background-color, color, transform 0.18s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #000000 | = | = | 17.46 x 17.46, colour #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.flex.size-11 44.0x44.0 r 8px outline 2px solid #606060 offset 2px | button.flex.size-11 42.7x42.7 bg #000000 @ 0.1 r 8px |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The opened nav overlay.

Page: home. Selector: `opened mobile menu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 300 x 1186 |
| Padding | 0px |
| Gap | 40px 30px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | euclidCircularALightWebS 16px/24px 400 |
| Letter spacing | -0.32px |
| Colour | #000000 |
| Text node | a.foot-note-medium.text-text-icons-tertiary: euclidCircularALightWebS 14px/20px 500, #999999, ls -0.28px |
| Transition | none |
| Icon | 20 x 20, colour #999999 |
| Ancestor paint | 1 up div.mx-auto.max-w-[1110px] bg #f4f4f4 |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile menu row. A row inside the opened nav overlay.

Page: home. Selector: `mobile menu row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 42.48 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #606060 offset 2px | = |
| Font | euclidCircularALightWebS 14px/20px 500 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #999999 | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.foot-note-medium.text-text-icons-tertiary 42.5x20.0 outline 2px solid #606060 offset 2px | = |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: home. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 123.09 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | euclidCircularALightWebS 38px/41.04px 600 |
| Letter spacing | -1.33px |
| Colour | #000000 |
| Text node | span.home-blur-char.inline-block: euclidCircularALightWebS 38px/41.04px 600, #000000, ls -1.33px |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

craftwork.design serves its Next.js sheets same-origin; this list covers the transition rules the page itself exposes, and the per-state Transition rows above are the computed values the page paints.

- home: `background-color 0.18s, color 0.18s`, `background 0.3s, box-shadow 0.3s cubic-bezier(0.16, 1, 0.3, 1)`, `transform 0.36s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.22s`, `transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.2s`, `transform 0.42s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.2s`, `transform 0.45s cubic-bezier(0.16, 1, 0.3, 1)`, `background-color 5000s ease-in-out`, `background-color 0.15s`, `opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1)`, `transform 0.5s ease-out`, `opacity 0.22s, transform 0.22s, color 0.18s`, `opacity 0.18s`

- pricing: `background-color 0.18s, color 0.18s`, `background 0.3s, box-shadow 0.3s cubic-bezier(0.16, 1, 0.3, 1)`, `transform 0.36s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.22s`, `transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.2s`, `transform 0.42s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.2s`, `transform 0.45s cubic-bezier(0.16, 1, 0.3, 1)`, `background-color 5000s ease-in-out`, `background-color 0.15s`, `opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1)`, `transform 0.5s ease-out`, `opacity 0.22s, transform 0.22s, color 0.18s`, `opacity 0.18s`
