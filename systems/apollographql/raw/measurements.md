# Component measurements

Computed styles read from apollographql.com on 2026-11-10 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### cookie-card

Cookie consent card. The OneTrust bottom-left card (white, 16px radius, double shadow): copy, Accept All / Decline Non-Necessary / Manage Preferences buttons.

Page: home. Selector: `.otFloatingRoundedCorner`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 760 x 188.56 |
| Padding | 20px 20px 18px 20px |
| Border | 1px solid #e3e7ea |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #15252d @ 0.14 0px 12px 32px 0px, #15252d @ 0.06 0px 2px 6px 0px |
| Outline | none |
| Font | __interFont_b14d2f 16px/24px 400 |
| Letter spacing | normal |
| Colour | #3d4a52 |
| Text node | div: __interFont_b14d2f 13px/20.15px 400, #3d4a52 |
| Transition | none |
| Painted layers | div.otFloatingRoundedCorner.ot-bottom-left 760.0x188.6 bg #ffffff border T:1px solid #e3e7ea / R:1px solid #e3e7ea / B:1px solid #e3e7ea / L:1px solid #e3e7ea r 16px shadow #15252d @ 0.14 0px 12px 32px 0px, #15252d @ 0.06 0px 2px 6px 0px; button 222.2x32.0 bg #15252d border T:1px solid #15252d / R:1px solid #15252d / B:1px solid #15252d / L:1px solid #15252d r 999px; button 222.2x32.0 bg #15252d border T:1px solid #15252d / R:1px solid #15252d / B:1px solid #15252d / L:1px solid #15252d r 999px; button 222.2x32.0 bg #15252d border T:1px solid #15252d / R:1px solid #15252d / B:1px solid #15252d / L:1px solid #15252d r 999px |
| How | at rest |

Crops: `cookie-card-default.png`.

#### cookie-accept

Cookie Accept button. The dark pill inside the OneTrust card. Measured, never clicked.

Page: home. Selector: `Accept All Cookies`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 222.22 x 32 |
| Padding | 0px 12px |
| Border | 1px solid #15252d |
| Radius | 999px |
| Background | #15252d |
| Box shadow | none |
| Outline | none |
| Font | __interFont_b14d2f 12.5px/12.5px 600 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | background-color, border-color 0.12s, 0.12s ease, ease delay 0s, 0s |
| Cursor | pointer |
| Painted layers | button 222.2x32.0 bg #15252d border T:1px solid #15252d / R:1px solid #15252d / B:1px solid #15252d / L:1px solid #15252d r 999px |
| How | at rest |

Crops: `cookie-accept-default.png`.

#### eyebrow

Summit eyebrow. The "Apollo Summit 2026 keynote available / Watch keynote" strip above the nav, with its own close.

Page: home. Selector: `summit-eyebrow`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 55 |
| Padding | 10px 48px |
| Border | none |
| Radius | 0px |
| Background | #1a1a1a |
| Box shadow | none |
| Outline | none |
| Font | __interFont_b14d2f 16px/24px 400 |
| Letter spacing | normal |
| Colour | #15252d |
| Text node | strong: Aeonik 18px/18px 700, #ffffff |
| Transition | none |
| Icon | 10 x 12, colour #000000 |
| Painted layers | aside.summit-eyebrow_eyebrow 1440.0x55.0 bg #1a1a1a; a.summit-eyebrow_cta 184.4x35.0 bg #ffffff r 999px |
| How | at rest |

Crops: `eyebrow-default.png`.

#### nav-bar

Nav bar. The sticky transparent header over the dark hero: logo, Products/Solutions/Resources/Company disclosures, Pricing and Contact us links, search, Start for free pill.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 65 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __interFont_b14d2f 16px/24px 400 |
| Letter spacing | normal |
| Colour | #15252d |
| Text node | button.group.mx-0.5: __interFont_b14d2f 15px/22.5px 500, oklab(0.999994 0.0000455678 0.0000200868 / 0.72), ls -0.15px |
| Transition | transform, translate, scale, rotate 0.3s cubic-bezier(0.17, 0.17, 0, 1) |
| Icon | 62.33 x 22, colour #15252d |
| Painted layers | div.pointer-events-auto.border-b 1440.0x65.0 bg #02060a border B:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.08); span.mx-1.5.hidden 1.0x24.0 bg oklab(0.999994 0.0000455678 0.0000200868 / 0.12); a.h-10.items-center 110.5x40.0 border T:1px solid #f06d2b / R:1px solid #f06d2b / B:1px solid #f06d2b / L:1px solid #f06d2b r 999px; a.h-10.items-center 123.4x40.0 bg #e75e15 border T:1px solid #e75e15 / R:1px solid #e75e15 / B:1px solid #e75e15 / L:1px solid #e75e15 r 999px |
| How | at rest |

Crops: `nav-bar-default.png`.

#### logo

Logo. The Apollo wordmark, top-left of the nav.

Page: home. Selector: `header logo`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 62.33 x 32 | = | = | = |
| Padding | 5px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ff7b3c offset 2px | = |
| Font | __interFont_b14d2f 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #15252d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 62.33 x 22, colour #15252d | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.mr-4.flex 62.3x32.0 r 8px outline 2px solid #ff7b3c offset 2px | = |

Crops: `logo-default.png`, `logo-hover.png`, `logo-focus-visible.png`, `logo-pressed.png`.

#### nav-trigger

Nav disclosure. A nav menu trigger (Products / Solutions / Resources / Company): 38px, 8px radius, Inter 15px 500 at 72% white.

Page: home. Selector: `nav disclosure`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 104.77 x 38 | = | = | = |
| Padding | 0px 13px | = | = | = |
| Gap | 5px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | oklab(0.999994 0.0000455678 0.0000200868 / 0.15) | = | oklab(0.999994 0.0000455678 0.0000200868 / 0.1) |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ff7b3c offset 2px | = |
| Font | __interFont_b14d2f 15px/22.5px 500 | = | = | = |
| Letter spacing | -0.15px | = | = | = |
| Colour | oklab(0.999994 0.0000455678 0.0000200868 / 0.72) | #ffffff | = | #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 11 x 11, colour oklab(0.999994 0.0000455678 0.0000200868 / 0.72) | 11 x 11, colour #ffffff | = | 11 x 11, colour #ffffff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.group.mx-0.5 104.8x38.0 bg oklab(0.999994 0.0000455678 0.0000200868 / 0.15) r 8px | button.group.mx-0.5 104.8x38.0 r 8px outline 2px solid #ff7b3c offset 2px | button.group.mx-0.5 104.8x38.0 bg oklab(0.999994 0.0000455678 0.0000200868 / 0.1) r 8px |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### nav-menu

Products menu. The Products dropdown panel: product rows with one-line descriptions, plus the two promo links at the foot.

Page: home. Selector: `products dropdown`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 1440 x 463 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __interFont_b14d2f 16px/24px 400 |
| Letter spacing | normal |
| Colour | #15252d |
| Text node | span.text-base.font-bold: __interFont_b14d2f 16px/24px 700, #15252d, ls -0.4px |
| Transition | height 0.2s cubic-bezier(0, 0, 0.2, 1) |
| Transform | matrix(1, 0, 0, 1, 0, -6.47463) |
| Opacity | 0.0750526 |
| Icon | 44 x 44, colour #15252d |
| Painted layers | div.pointer-events-auto.w-full 1312.0x463.0 bg #ffffff border T:1px solid #efefef / R:1px solid #efefef / B:1px solid #efefef / L:1px solid #efefef r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #091b23 @ 0.42 0px 28px 64px -20px, #091b23 @ 0.08 0px 6px 16px 0px; a.group.flex 447.0x96.0 image linear-gradient(to right in oklab, #fff1e9 0px, #f3f6f8 100%) border T:1px solid oklab(0.794287 0.0879803 0.0925078 / 0.3) / R:1px solid oklab(0.794287 0.0879803 0.0925078 / 0.3) / B:1px solid oklab(0.794287 0.0879803 0.0925078 / 0.3) / L:1px solid oklab(0.794287 0.0879803 0.0925078 / 0.3) r 12px; a.group.flex 447.0x96.0 image linear-gradient(to right in oklab, #fff1e9 0px, #f3f6f8 100%) border T:1px solid oklab(0.794287 0.0879803 0.0925078 / 0.3) / R:1px solid oklab(0.794287 0.0879803 0.0925078 / 0.3) / B:1px solid oklab(0.794287 0.0879803 0.0925078 / 0.3) / L:1px solid oklab(0.794287 0.0879803 0.0925078 / 0.3) r 12px; hr.col-span-2.m-0 926.0x1.0 border T:1px solid #efefef; div.flex.w-full 320.0x461.0 bg #0a1720 border L:1px solid #efefef |
| How | at rest |

Crops: none.

#### nav-menu-item

Menu item. A product row inside the Products dropdown.

Page: home. Selector: `dropdown item`. States: open, hover.

| Property | open | hover |
|---|---|---|
| Size (w x h) | 149.44 x 48 | = |
| Padding | 0px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 999px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | __aeonikFont_a2019c 16px/24px 500 | = |
| Letter spacing | normal | = |
| Colour | #c74100 | = |
| Text node | span: __aeonikFont_a2019c 16px/24px 500, #c74100 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | span.inline-flex.items-center 149.4x29.0 border B:1px solid #c74100 | = |
| How | at rest | mouse hover |

Crops: `nav-menu-item-open.png`, `nav-menu-item-hover.png`.

#### nav-cta

Start for free button. The pill at the right of the nav; links to studio.apollographql.com/signup. Hovered and focused only.

Page: home. Selector: `nav Start for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 123.42 x 40 | = | = | = |
| Padding | 0px 18px | = | = | = |
| Border | 1px solid #e75e15 | 1px solid #d84f08 | = | 1px solid #d84f08 |
| Radius | 999px | = | = | = |
| Background | #e75e15 | #d84f08 | = | #d84f08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ff7b3c offset 2px | = |
| Font | __interFont_b14d2f 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.h-10.items-center 123.4x40.0 bg #e75e15 border T:1px solid #e75e15 / R:1px solid #e75e15 / B:1px solid #e75e15 / L:1px solid #e75e15 r 999px | a.h-10.items-center 123.4x40.0 bg #d84f08 border T:1px solid #d84f08 / R:1px solid #d84f08 / B:1px solid #d84f08 / L:1px solid #d84f08 r 999px | a.h-10.items-center 123.4x40.0 bg #e75e15 border T:1px solid #e75e15 / R:1px solid #e75e15 / B:1px solid #e75e15 / L:1px solid #e75e15 r 999px outline 2px solid #ff7b3c offset 2px | a.h-10.items-center 123.4x40.0 bg #d84f08 border T:1px solid #d84f08 / R:1px solid #d84f08 / B:1px solid #d84f08 / L:1px solid #d84f08 r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-search

Search button. The Algolia detached search icon in the nav.

Page: home. Selector: `search button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 20 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #f8f8f8 offset 8px | = |
| Font | __interFont_b14d2f 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #15252d | = | = | = |
| Transition | background-color, border-color 0.3s, 0.3s cubic-bezier(0.17, 0.17, 0, 1), cubic-bezier(0.17, 0.17, 0, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 24, colour #f8f8f8 | 20 x 24, colour #f6f6f6 | = | 20 x 24, colour #f6f6f6 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.aa-DetachedSearchButton 20.0x20.0 r 3px outline 1px solid #f8f8f8 offset 8px | = |

Crops: `nav-search-default.png`, `nav-search-hover.png`, `nav-search-focus-visible.png`, `nav-search-pressed.png`.

### Home

#### hero-title

Hero title. "Give AI access to the systems that run your business" — Aeonik 60px white over the dark animated hero.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 832 x 126 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __aeonikFont_a2019c 60px/63px 400 |
| Letter spacing | -1.5px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero subhead. The 20px Aeonik lede under the hero title.

Page: home. Selector: `hero subhead`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 864 x 65 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __aeonikFont_a2019c 20px/32.5px 500 |
| Letter spacing | normal |
| Colour | #d1d1d1 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### cta-primary

Primary CTA. The white 999px pill "Talk to Apollo" (60px tall, Aeonik 18px 500) with a soft warm shadow.

Page: home. Selector: `hero primary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 210.47 x 60 | = | = | = |
| Padding | 16px 48px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 2px solid #000000 @ 0 | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(#02060a, #02060a), conic-gradient(from 411.894deg, #4ca6b5, #f06d2b, #4ca6b5) | linear-gradient(#15252d, #15252d), conic-gradient(from 568.884deg, #7cc3ce, #ff7b3c, #7cc3ce) | linear-gradient(#02060a, #02060a), conic-gradient(from 319.884deg, #4ca6b5, #f06d2b, #4ca6b5) | linear-gradient(#15252d, #15252d), conic-gradient(from 454.878deg, #7cc3ce, #ff7b3c, #7cc3ce) |
| Box shadow | oklab(0.676327 -0.0761709 -0.0438468 / 0.25) 2.3064px -1.6936px 16px 0px, oklab(0.684338 0.128575 0.123564 / 0.25) -2.3064px 1.6936px 16px 0px | oklab(0.77422 -0.0641362 -0.0343847 / 0.25) -1.28373px 2.71627px 16px 0px, oklab(0.727177 0.128214 0.123105 / 0.25) 1.28373px -2.71627px 16px 0px | oklab(0.676327 -0.0761709 -0.0438468 / 0.25) -1.78293px -2.21707px 16px 0px, oklab(0.684338 0.128575 0.123564 / 0.25) 1.78293px 2.21707px 16px 0px | oklab(0.77422 -0.0641362 -0.0343847 / 0.25) 3.7832px 0.2168px 16px 0px, oklab(0.727177 0.128214 0.123105 / 0.25) -3.7832px -0.2168px 16px 0px |
| Outline | none | = | 2px solid #2fd1e0 offset 4px | = |
| Font | __aeonikFont_a2019c 18px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 206.469px x 56px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff @ 0.25 0px 0px 24px 0px | = | = | = |
| Painted layers | a.inline-flex.min-h-12 210.5x60.0 image linear-gradient(#02060a, #02060a), conic-gradient(from 411.894deg, #4ca6b5, #f06d2b, #4ca6 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 999px shadow oklab(0.676327 -0.0761709 -0.0438468 / 0.25) 2.3064px -1.6936px 16px 0px, oklab(0.684338 0.128575 0.123564 / 0.25) -2.3064px 1.6936px 16px 0px; a::after.inline-flex.min-h-12 206.469pxx56px r 999px shadow #ffffff @ 0.25 0px 0px 24px 0px | a.inline-flex.min-h-12 210.5x60.0 image linear-gradient(#15252d, #15252d), conic-gradient(from 568.884deg, #7cc3ce, #ff7b3c, #7cc3 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 999px shadow oklab(0.77422 -0.0641362 -0.0343847 / 0.25) -1.28373px 2.71627px 16px 0px, oklab(0.727177 0.128214 0.123105 / 0.25) 1.28373px -2.71627px 16px 0px; a::after.inline-flex.min-h-12 206.469pxx56px r 999px shadow #ffffff @ 0.25 0px 0px 24px 0px | a.inline-flex.min-h-12 210.5x60.0 image linear-gradient(#02060a, #02060a), conic-gradient(from 319.884deg, #4ca6b5, #f06d2b, #4ca6 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 999px shadow oklab(0.676327 -0.0761709 -0.0438468 / 0.25) -1.78293px -2.21707px 16px 0px, oklab(0.684338 0.128575 0.123564 / 0.25) 1.78293px 2.21707px 16px 0px outline 2px solid #2fd1e0 offset 4px; a::after.inline-flex.min-h-12 206.469pxx56px r 999px shadow #ffffff @ 0.25 0px 0px 24px 0px | a.inline-flex.min-h-12 210.5x60.0 image linear-gradient(#15252d, #15252d), conic-gradient(from 454.878deg, #7cc3ce, #ff7b3c, #7cc3 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 999px shadow oklab(0.77422 -0.0641362 -0.0343847 / 0.25) 3.7832px 0.2168px 16px 0px, oklab(0.727177 0.128214 0.123105 / 0.25) -3.7832px -0.2168px 16px 0px; a::after.inline-flex.min-h-12 206.469pxx56px r 999px shadow #ffffff @ 0.25 0px 0px 24px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-primary-default.png`, `cta-primary-hover.png`, `cta-primary-focus-visible.png`, `cta-primary-pressed.png`.

#### cta-secondary

Secondary CTA. The 1px white/35 outline pill beside the primary.

Page: home. Selector: `hero secondary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 238.02 x 60 | = | = | = |
| Padding | 16px 48px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.35) | 1px solid #ffffff | = | 1px solid #ffffff |
| Radius | 999px | = | = | = |
| Background | transparent | oklab(0.999994 0.0000455678 0.0000200868 / 0.1) | = | oklab(0.999994 0.0000455678 0.0000200868 / 0.1) |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #2fd1e0 offset 4px | = |
| Font | __aeonikFont_a2019c 18px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.min-h-12 238.0x60.0 border T:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.35) / R:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.35) / B:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.35) / L:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.35) r 999px | a.inline-flex.min-h-12 238.0x60.0 bg oklab(0.999994 0.0000455678 0.0000200868 / 0.1) border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 999px | a.inline-flex.min-h-12 238.0x60.0 border T:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.35) / R:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.35) / B:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.35) / L:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.35) r 999px outline 2px solid #2fd1e0 offset 4px | a.inline-flex.min-h-12 238.0x60.0 bg oklab(0.999994 0.0000455678 0.0000200868 / 0.1) border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-secondary-default.png`, `cta-secondary-hover.png`, `cta-secondary-focus-visible.png`, `cta-secondary-pressed.png`.

#### pause-motion

Pause motion button. The ghost chip bottom-right of the hero (80% black fill, 1px white/20 border, 4px radius).

Page: home. Selector: `pause motion`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 118.91 x 34 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.2) | = | = | = |
| Radius | 4px | = | = | = |
| Background | oklab(0.117506 -0.00815131 -0.0132371 / 0.8) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #e75e15 offset 2px | = |
| Font | __aeonikFont_a2019c 12px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklab(0.999994 0.0000455677 0.0000200868 / 0.7) | #ffffff | = | #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour oklab(0.999994 0.0000455677 0.0000200868 / 0.7), fill #000000 | 12 x 12, colour #ffffff, fill #000000 | = | 12 x 12, colour #ffffff, fill #000000 |
| Painted layers | button.hero-depth_pause.absolute 118.9x34.0 bg oklab(0.117506 -0.00815131 -0.0132371 / 0.8) border T:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.2) / R:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.2) / B:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.2) / L:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.2) r 4px | = | button.hero-depth_pause.absolute 118.9x34.0 bg oklab(0.117506 -0.00815131 -0.0132371 / 0.8) border T:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.2) / R:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.2) / B:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.2) / L:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.2) r 4px outline 2px solid #e75e15 offset 2px | = |
| Ancestor paint | 1 up section.relative.isolate bg #02060a | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pause-motion-default.png`, `pause-motion-hover.png`, `pause-motion-focus-visible.png`, `pause-motion-pressed.png`.

#### text-link

Text link. The solar-orange inline link (Aeonik 18px 700) inside body copy.

Page: home. Selector: `orange text link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 298.59 x 33 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #e75e15 offset 4px | = |
| Font | __aeonikFont_a2019c 18px/28px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #c74100 | #e75e15 | = | #e75e15 |
| Text node | span: __aeonikFont_a2019c 18px/28px 700, #c74100 | span: __aeonikFont_a2019c 18px/28px 700, #e75e15 | = | span: __aeonikFont_a2019c 18px/28px 700, #e75e15 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #c74100, fill #000000 | 16 x 16, colour #e75e15, fill #000000 | = | 16 x 16, colour #e75e15, fill #000000 |
| Painted layers | span.inline-flex.items-center 298.6x33.0 border B:1px solid #c74100 | span.inline-flex.items-center 298.6x33.0 border B:1px solid #e75e15 | a.inline-flex.items-center 298.6x33.0 outline 2px solid #e75e15 offset 4px; span.inline-flex.items-center 298.6x33.0 border B:1px solid #c74100 | span.inline-flex.items-center 298.6x33.0 border B:1px solid #e75e15 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `text-link-default.png`, `text-link-hover.png`, `text-link-focus-visible.png`, `text-link-pressed.png`.

#### link-pill

Arrow link pill. An orange "Explore … →" pill link between sections (Aeonik 16px 500).

Page: home. Selector: `orange arrow link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 149.44 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #e75e15 offset 4px | = |
| Font | __aeonikFont_a2019c 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #c74100 | = | = | = |
| Text node | span: __aeonikFont_a2019c 16px/24px 500, #c74100 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.inline-flex.items-center 149.4x29.0 border B:1px solid #c74100 | = | a.inline-flex.min-h-12 149.4x48.0 r 999px outline 2px solid #e75e15 offset 4px; span.inline-flex.items-center 149.4x29.0 border B:1px solid #c74100 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `link-pill-default.png`, `link-pill-hover.png`, `link-pill-focus-visible.png`, `link-pill-pressed.png`.

#### section-title-light

Section title (light). An Aeonik 42px heading on a light content section — the site alternates dark hero / light content bands.

Page: home. Selector: `section h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1296 x 52.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __aeonikFont_a2019c 42px/52.5px 400 |
| Letter spacing | -1.05px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `section-title-light-default.png`.

#### video-card

Video card. The 520x293 "PLAY VIDEO" card, 24px radius on eclipse.

Page: home. Selector: `video card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 520 x 292.5 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | #15252d | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #e75e15 offset -4px | = |
| Font | __aeonikFont_a2019c 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span: __aeonikFont_a2019c 14px/14px 700, #15252d | span: __aeonikFont_a2019c 14px/14px 700, #f8f8f8 | span: __aeonikFont_a2019c 14px/14px 700, #f8f8f8 | span: __aeonikFont_a2019c 14px/14px 700, #f8f8f8 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #15252d, fill #000000 | 20 x 20, colour #f8f8f8, fill #000000 | 20 x 20, colour #f8f8f8, fill #000000 | 19 x 19, colour #f8f8f8, fill #000000 |
| Painted layers | button.group.relative 520.0x292.5 bg #15252d r 24px; span.absolute.inset-0 520.0x292.5 bg oklab(0 0 0 / 0.4); span.absolute.inset-0 145.8x52.0 bg oklab(0.363193 -0.0255118 -0.0305304 / 0.9) r 8px; span.flex.h-full 137.8x44.0 bg #f8f8f8 r 6px | button.group.relative 520.0x292.5 bg #15252d r 24px; span.absolute.inset-0 520.0x292.5 bg oklab(0 0 0 / 0.4); span.absolute.inset-0 145.8x52.0 bg oklab(0.363193 -0.0255118 -0.0305304 / 0.9) r 8px; span.flex.h-full 137.8x44.0 bg #15252d r 6px | button.group.relative 520.0x292.5 bg #15252d r 24px outline 2px solid #e75e15 offset -4px; span.absolute.inset-0 520.0x292.5 bg oklab(0 0 0 / 0.4); span.absolute.inset-0 145.8x52.0 bg oklab(0.363193 -0.0255118 -0.0305304 / 0.9) r 8px; span.flex.h-full 137.8x44.0 bg #15252d r 6px | button.group.relative 520.0x292.5 bg #15252d r 24px; span.absolute.inset-0 520.0x292.5 bg oklab(0 0 0 / 0.4); span.absolute.inset-0 138.5x49.4 bg oklab(0.363193 -0.0255118 -0.0305304 / 0.9) r 8px; span.flex.h-full 130.9x41.8 bg #15252d r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `video-card-default.png`, `video-card-hover.png`, `video-card-focus-visible.png`, `video-card-pressed.png`.

#### copy-row

Copy control row. One of the three 416x84 copy rows in the architecture animation panel.

Page: home. Selector: `copyControl row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 416 x 84 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #666666 offset 4px | = |
| Font | __aeonikFont_a2019c 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.architecture-animation_copyControl 416.0x84.0 outline 2px solid #666666 offset 4px | = |

Crops: `copy-row-default.png`, `copy-row-hover.png`, `copy-row-focus-visible.png`, `copy-row-pressed.png`.

#### carousel-arrow

Carousel arrow. A 42x42 white 16px-radius arrow button on the logo/customer carousel.

Page: home. Selector: `carousel arrow`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 42 x 42 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #bec4c2 | = | = | = |
| Radius | 16px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #99c8ff offset 0px | = |
| Font | __aeonikFont_a2019c 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #000000 | = | = | = |
| Painted layers | button.flex.h-[42px] 42.0x42.0 bg #ffffff border T:1px solid #bec4c2 / R:1px solid #bec4c2 / B:1px solid #bec4c2 / L:1px solid #bec4c2 r 16px | = | button.flex.h-[42px] 42.0x42.0 bg #ffffff border T:1px solid #bec4c2 / R:1px solid #bec4c2 / B:1px solid #bec4c2 / L:1px solid #bec4c2 r 16px outline 5px auto #99c8ff offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `carousel-arrow-default.png`, `carousel-arrow-hover.png`, `carousel-arrow-focus-visible.png`, `carousel-arrow-pressed.png`.

#### footer

Footer. The footer band: tagline, five link columns, small orange Start for free pill, social icons.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 627.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __interFont_b14d2f 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f8f8f8 |
| Text node | strong: __interFont_b14d2f 16px/24px 900, #f8f8f8 |
| Transition | none |
| Icon | 85 x 30, colour #f8f8f8 |
| Painted layers | div.footer_content 1344.0x367.5 border B:1px solid #f6f6f6; a.relative.flex 107.2x34.0 bg #e75e15 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px |
| Ancestor paint | 1 up section.relative.overflow-hidden bg #02060a |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A 14px Inter footer column link at 97% white.

Page: home. Selector: `footer link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 129.86 x 36 | = | = | = |
| Padding | 8px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #99c8ff offset 1px | = |
| Font | __interFont_b14d2f 14px/20.006px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f8f8f8 | = | = | = |
| Transition | transform, translate, scale, rotate 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #f8f8f8 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.text-surface-default.text-body-sm 129.9x36.0 outline 1px auto #99c8ff offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-link

Social icon. A 28x28 social icon in the footer row.

Page: home. Selector: `social link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 28 x 28 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #99c8ff offset 1px | = |
| Font | __interFont_b14d2f 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f8f8f8 | = | = | = |
| Transition | color, transform 0.3s, 0.15s cubic-bezier(0.17, 0.17, 0, 1), cubic-bezier(0.17, 0.17, 0, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 28 x 32, colour #f8f8f8 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.footer_socialLink 28.0x28.0 outline 1px auto #99c8ff offset 1px | = |

Crops: `social-link-default.png`, `social-link-hover.png`, `social-link-focus-visible.png`, `social-link-pressed.png`.

### Pricing

#### pricing-title

Pricing title. "Pricing that makes sense at any scale…" — Inter 50px 500 on the dark page.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 880 x 276.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __interFont_b14d2f 50px/55px 500 |
| Letter spacing | normal |
| Colour | #f8f8f8 |
| Transition | none |
| Icon | 25 x 25, colour #f8f8f8 |
| Painted layers | a.relative.flex 146.8x49.0 bg #e75e15 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px; a.relative.flex 190.5x49.0 border T:1px solid #e75e15 / R:1px solid #e75e15 / B:1px solid #e75e15 / L:1px solid #e75e15 r 999px |
| How | at rest |

Crops: `pricing-title-default.png`.

#### tier-segment

Tier segment. A plan-tier filter pill (Developer / …), 43px tall, 20px radius, 1px white border.

Page: pricing. Selector: `tier pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 125.55 x 43 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #f8f8f8 | = | = | = |
| Radius | 20px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #99c8ff offset 0px | = |
| Font | __interFont_b14d2f 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f8f8f8 | #ffffff | = | #ffffff |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.flex.cursor-pointer 125.5x43.0 border T:1px solid #f8f8f8 / R:1px solid #f8f8f8 / B:1px solid #f8f8f8 / L:1px solid #f8f8f8 r 20px; span.radio-indicator.relative 16.0x16.0 bg #ff6b35 r 999px; span::after.radio-indicator.relative 6pxx6px bg #15252d r 999px | = | button.flex.cursor-pointer 125.5x43.0 border T:1px solid #f8f8f8 / R:1px solid #f8f8f8 / B:1px solid #f8f8f8 / L:1px solid #f8f8f8 r 20px outline 5px auto #99c8ff offset 0px; span.radio-indicator.relative 16.0x16.0 bg #ff6b35 r 999px; span::after.radio-indicator.relative 6pxx6px bg #15252d r 999px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tier-segment-default.png`, `tier-segment-hover.png`, `tier-segment-focus-visible.png`, `tier-segment-pressed.png`.

#### billing-segment

Billing segment. The Monthly/Yearly billing pill beside the tier pills.

Page: pricing. Selector: `billing pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 111.5 x 43 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #f8f8f8 | = | = | = |
| Radius | 20px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #99c8ff offset 0px | = |
| Font | __interFont_b14d2f 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f8f8f8 | #ffffff | = | #ffffff |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.flex.cursor-pointer 111.5x43.0 border T:1px solid #f8f8f8 / R:1px solid #f8f8f8 / B:1px solid #f8f8f8 / L:1px solid #f8f8f8 r 20px; span.radio-indicator.relative 16.0x16.0 bg #ff6b35 r 999px; span::after.radio-indicator.relative 6pxx6px bg #15252d r 999px | = | button.flex.cursor-pointer 111.5x43.0 border T:1px solid #f8f8f8 / R:1px solid #f8f8f8 / B:1px solid #f8f8f8 / L:1px solid #f8f8f8 r 20px outline 5px auto #99c8ff offset 0px; span.radio-indicator.relative 16.0x16.0 bg #ff6b35 r 999px; span::after.radio-indicator.relative 6pxx6px bg #15252d r 999px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `billing-segment-default.png`, `billing-segment-hover.png`, `billing-segment-focus-visible.png`, `billing-segment-pressed.png`.

#### volume-pill-on

Volume pill (selected). The held request-volume pill: #fc5200 solar fill, eclipse text, 8px radius.

Page: pricing. Selector: `volume pill on`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 39.97 x 39 | = | = | = |
| Padding | 8px 10px | = | = | = |
| Border | 1px solid #fc5200 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #fc5200 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f8f8f8 offset 2px | = |
| Font | __interFont_b14d2f 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #15252d | = | = | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.cursor-pointer.rounded-[8px] 40.0x39.0 bg #fc5200 border T:1px solid #fc5200 / R:1px solid #fc5200 / B:1px solid #fc5200 / L:1px solid #fc5200 r 8px | = | button.cursor-pointer.rounded-[8px] 40.0x39.0 bg #fc5200 border T:1px solid #fc5200 / R:1px solid #fc5200 / B:1px solid #fc5200 / L:1px solid #fc5200 r 8px outline 2px solid #f8f8f8 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `volume-pill-on-default.png`, `volume-pill-on-hover.png`, `volume-pill-on-focus-visible.png`, `volume-pill-on-pressed.png`.

#### volume-pill

Volume pill. An unheld volume pill: transparent, 1px border, 8px radius.

Page: pricing. Selector: `volume pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48.8 x 39 | = | = | = |
| Padding | 8px 10px | = | = | = |
| Border | 1px solid #f8f8f8 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f8f8f8 offset 2px | = |
| Font | __interFont_b14d2f 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f8f8f8 | = | = | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.cursor-pointer.rounded-[8px] 48.8x39.0 border T:1px solid #f8f8f8 / R:1px solid #f8f8f8 / B:1px solid #f8f8f8 / L:1px solid #f8f8f8 r 8px | = | button.cursor-pointer.rounded-[8px] 48.8x39.0 border T:1px solid #f8f8f8 / R:1px solid #f8f8f8 / B:1px solid #f8f8f8 / L:1px solid #f8f8f8 r 8px outline 2px solid #f8f8f8 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `volume-pill-default.png`, `volume-pill-hover.png`, `volume-pill-focus-visible.png`, `volume-pill-pressed.png`.

#### plan-cta

Plan CTA. The orange "Start for free" pill on pricing (49px, Inter 16px 500). Links to Studio signup; hovered and focused only.

Page: pricing. Selector: `pricing cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 146.78 x 49.03 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 999px | = | = | = |
| Background | #e75e15 | oklab(0.649255 0.136349 0.125914 / 0.9) | = | oklab(0.649255 0.136349 0.125914 / 0.9) |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #e75e15 offset 8px | = |
| Font | __interFont_b14d2f 16px/15.04px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f8f8f8 | = | = | = |
| Text node | span.hide-mobile-and-tablet: __interFont_b14d2f 16px/15.04px 500, #f8f8f8 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.relative.flex 146.8x49.0 bg #e75e15 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px | a.relative.flex 146.8x49.0 bg oklab(0.649255 0.136349 0.125914 / 0.9) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px | a.relative.flex 146.8x49.0 bg #e75e15 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px outline 2px solid #e75e15 offset 8px | a.relative.flex 146.8x49.0 bg oklab(0.649255 0.136349 0.125914 / 0.9) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### stats-card

Stats band card. The 1344x670 eclipse card ("Trusted by digital leaders"), 32px radius.

Page: pricing. Selector: `stats card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1344 x 669.5 |
| Padding | 94px 80px |
| Border | none |
| Radius | 32px |
| Background | #15252d |
| Box shadow | none |
| Outline | none |
| Font | __interFont_b14d2f 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f8f8f8 |
| Text node | h3.trusted-brands_title.h2: __interFont_b14d2f 38px/47.5px 700, #f8f8f8 |
| Transition | none |
| Icon | 158.39 x 25.44, colour #f8f8f8, fill #000000 |
| Painted layers | div.relative.overflow-hidden 1344.0x669.5 bg #15252d r 32px; div.relative.overflow-hidden 266.0x142.0 bg #15252d border T:1px solid #9fb2bc / R:1px solid #9fb2bc / B:1px solid #9fb2bc / L:1px solid #9fb2bc r 32px; div.relative.overflow-hidden 266.0x142.0 bg #15252d border T:1px solid #9fb2bc / R:1px solid #9fb2bc / B:1px solid #9fb2bc / L:1px solid #9fb2bc r 32px; div.relative.overflow-hidden 266.0x142.0 bg #15252d border T:1px solid #9fb2bc / R:1px solid #9fb2bc / B:1px solid #9fb2bc / L:1px solid #9fb2bc r 32px; div.relative.overflow-hidden 266.0x142.0 bg #15252d border T:1px solid #9fb2bc / R:1px solid #9fb2bc / B:1px solid #9fb2bc / L:1px solid #9fb2bc r 32px; div.relative.overflow-hidden 266.0x142.0 bg #15252d border T:1px solid #9fb2bc / R:1px solid #9fb2bc / B:1px solid #9fb2bc / L:1px solid #9fb2bc r 32px |
| How | at rest |

Crops: `stats-card-default.png`.

#### faq-card

FAQ card. The light regolith-grey FAQ card (#e3e3e3), 32px radius.

Page: pricing. Selector: `faq card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1344 x 612.5 |
| Padding | 72px |
| Border | none |
| Radius | 32px |
| Background | #e3e3e3 |
| Box shadow | none |
| Outline | none |
| Font | __interFont_b14d2f 16px/24px 400 |
| Letter spacing | normal |
| Colour | #15252d |
| Text node | h3.faqs_title.h2: __interFont_b14d2f 38px/47.5px 700, #15252d |
| Transition | none |
| Icon | 48 x 48, colour #15252d |
| Painted layers | div.relative.overflow-hidden 1344.0x612.5 bg #e3e3e3 r 32px; div.faqs_accordionItem 1200.0x113.0 border T:1px solid #15252d; div.faqs_accordionItem 1200.0x113.0 border T:1px solid #15252d; div.faqs_accordionItem 1200.0x113.0 border T:1px solid #15252d |
| How | at rest |

Crops: `faq-card-default.png`.

#### faq-item

FAQ item. A question row inside the FAQ card.

Page: pricing. Selector: `faq row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1200 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | __interFont_b14d2f 38px/47.5px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #15252d | = | = | = |
| Text node | h5.faqs_accordionTitle: __interFont_b14d2f 24px/31.2px 400, #15252d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 48 x 48, colour #15252d | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `faq-item-default.png`, `faq-item-hover.png`, `faq-item-focus-visible.png`, `faq-item-pressed.png`.

#### promo-banner

Promo banner. The "Amazing together" connectors promo card: eclipse fill, 32px radius.

Page: pricing. Selector: `promo banner`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1344 x 264.53 |
| Padding | 40px |
| Gap | 16px |
| Border | none |
| Radius | 32px |
| Background | #15252d |
| Box shadow | none |
| Outline | none |
| Font | __interFont_b14d2f 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f8f8f8 |
| Text node | h3.h4: __interFont_b14d2f 38px/47.5px 700, #f8f8f8 |
| Transition | none |
| Painted layers | div.connectors-promo_promoBanner 1344.0x264.5 bg #15252d r 32px; a.relative.flex 146.8x49.0 bg #e75e15 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px |
| How | at rest |

Crops: `promo-banner-default.png`.

### Customers

#### customers-title

Customers title. "API Orchestration Success Stories" — Inter 50px 500.

Page: customers. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 392.14 x 110 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __interFont_b14d2f 50px/55px 500 |
| Letter spacing | normal |
| Colour | #f8f8f8 |
| Transition | none |
| How | at rest |

Crops: `customers-title-default.png`.

#### cta-orange

Orange CTA. The solar-orange pill "Talk to an expert" (49px, Inter 16px 500, eclipse text on orange).

Page: customers. Selector: `orange cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 175.83 x 49.03 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 999px | = | = | = |
| Background | #e75e15 | oklab(0.649255 0.136349 0.125914 / 0.9) | = | oklab(0.649255 0.136349 0.125914 / 0.9) |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #e75e15 offset 8px | = |
| Font | __interFont_b14d2f 16px/15.04px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #15252d | = | = | = |
| Text node | span: __interFont_b14d2f 16px/15.04px 500, #15252d | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.relative.flex 175.8x49.0 bg #e75e15 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px | a.relative.flex 175.8x49.0 bg oklab(0.649255 0.136349 0.125914 / 0.9) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px | a.relative.flex 175.8x49.0 bg #e75e15 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px outline 2px solid #e75e15 offset 8px | a.relative.flex 175.8x49.0 bg oklab(0.649255 0.136349 0.125914 / 0.9) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-orange-default.png`, `cta-orange-hover.png`, `cta-orange-focus-visible.png`, `cta-orange-pressed.png`.

#### cta-orange-outline

Orange outline CTA. The 1px orange-outline pill beside the filled one.

Page: customers. Selector: `orange outline cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 176.89 x 49.03 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | 1px solid #e75e15 | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | oklab(0.649255 0.136349 0.125914 / 0.1) | = | oklab(0.649255 0.136349 0.125914 / 0.1) |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #e75e15 offset 8px | = |
| Font | __interFont_b14d2f 16px/15.04px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: __interFont_b14d2f 16px/15.04px 500, #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.relative.flex 176.9x49.0 border T:1px solid #e75e15 / R:1px solid #e75e15 / B:1px solid #e75e15 / L:1px solid #e75e15 r 999px | a.relative.flex 176.9x49.0 bg oklab(0.649255 0.136349 0.125914 / 0.1) border T:1px solid #e75e15 / R:1px solid #e75e15 / B:1px solid #e75e15 / L:1px solid #e75e15 r 999px | a.relative.flex 176.9x49.0 border T:1px solid #e75e15 / R:1px solid #e75e15 / B:1px solid #e75e15 / L:1px solid #e75e15 r 999px outline 2px solid #e75e15 offset 8px | a.relative.flex 176.9x49.0 bg oklab(0.649255 0.136349 0.125914 / 0.1) border T:1px solid #e75e15 / R:1px solid #e75e15 / B:1px solid #e75e15 / L:1px solid #e75e15 r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-orange-outline-default.png`, `cta-orange-outline-hover.png`, `cta-orange-outline-focus-visible.png`, `cta-orange-outline-pressed.png`.

#### stats-band

Stats band. The eclipse stats card ("0M monthly downloads / 0% of the Fortune 100…"), 32px radius.

Page: customers. Selector: `stats band`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1344 x 332 |
| Padding | 0px |
| Border | none |
| Radius | 32px |
| Background | #15252d |
| Box shadow | none |
| Outline | none |
| Font | __interFont_b14d2f 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f8f8f8 |
| Text node | span: __firaCodeFont_e66e50 72px/72px 700, #f8f8f8 |
| Transition | none |
| Painted layers | div.relative.overflow-hidden 1344.0x332.0 bg #15252d r 32px; div::after.stats_stat 1pxx332px image linear-gradient(to top, #f8f8f8 33%, #ffffff @ 0 0px); div::after.stats_stat 1pxx332px image linear-gradient(to top, #f8f8f8 33%, #ffffff @ 0 0px); div::after.stats_stat 1pxx332px image linear-gradient(to top, #f8f8f8 33%, #ffffff @ 0 0px) |
| How | at rest |

Crops: `stats-band-default.png`.

#### story-card

Story card. A customer-story card (432x585): white 32px-radius card with cover image, company name, title and author.

Page: customers. Selector: `story card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 432 x 584.5 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | __interFont_b14d2f 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #15252d | = | = | = |
| Text node | h4: __interFont_b14d2f 30px/37.5px 700, #15252d | = | = | = |
| Transition | none | = | = | = |
| Painted layers | div.relative.overflow-hidden 432.0x584.5 bg #f8f8f8 r 32px outline 1px solid #000000 @ 0 offset 6px; div.customer-story-article_contentWrapper 432.0x283.5 bg #efefef r 32px | = | div.relative.overflow-hidden 432.0x584.5 bg #f8f8f8 r 32px outline 1px solid #15252d offset 6px; div.customer-story-article_contentWrapper 432.0x283.5 bg #efefef r 32px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `story-card-default.png`, `story-card-hover.png`, `story-card-focus-visible.png`, `story-card-pressed.png`.

### Blog

#### blog-title

Blog title. "What's new" — Aeonik 60px on the light page.

Page: blog. Selector: `blog h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1368 x 67.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __aeonikFont_68f9fd 60px/67.2px 400 |
| Letter spacing | -1.2px |
| Colour | #15252d |
| Transition | none |
| How | at rest |

Crops: `blog-title-default.png`.

#### article-card

Article card (satellite). A featured article card on the satellite grey (#cfd7d6), 32px radius: date, title, author.

Page: blog. Selector: `article card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 444 x 298.81 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | #cfd7d6 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | __Inter_8b46f2 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #15252d | = | = | = |
| Text node | small.blog-article_dateWrapper: __Inter_8b46f2 16px/22.4px 400, #15252d | = | = | = |
| Transition | transform 0.5s cubic-bezier(0.06, 0.47, 0.1, 1) | = | = | = |
| Painted layers | article.card_card.card_theme-satellite 444.0x298.8 bg #cfd7d6 r 32px; span.blog-article_ellipse 10.0x10.0 bg #fc5200 r 9999px; hr.blog-article_hr 396.0x1.0 border T:1px dashed #15252d | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, -2.98119) | = | matrix(1, 0, 0, 1, 0, -2.95858) |

Crops: `article-card-default.png`, `article-card-hover.png`, `article-card-focus-visible.png`, `article-card-pressed.png`.

#### article-card-regolith

Article card (regolith). A past-posts card on white regolith, 32px radius.

Page: blog. Selector: `regolith card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 672 x 209.39 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | __Inter_8b46f2 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #15252d | = | = | = |
| Text node | small.blog-article_dateWrapper: __Inter_8b46f2 16px/22.4px 400, #15252d | = | = | = |
| Transition | background-color 0.3s cubic-bezier(0.06, 0.47, 0.1, 1) | = | = | = |
| Painted layers | article.card_card.card_theme-regolith 672.0x209.4 bg #ffffff r 32px; span.blog-article_ellipse 10.0x10.0 bg #fc5200 r 9999px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `article-card-regolith-default.png`, `article-card-regolith-hover.png`, `article-card-regolith-focus-visible.png`, `article-card-regolith-pressed.png`.

#### pagination

Pagination button. A numbered page button in the archive pagination.

Page: blog. Selector: `page button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 23 x 24.47 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #99c8ff offset 0px | = |
| Font | __Inter_8b46f2 18px/24.48px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #15252d | = | = | = |
| Transition | opacity 0.3s cubic-bezier(0.06, 0.47, 0.1, 1) | = | = | = |
| Opacity | 0.3 | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.pagination_pageBtn.paragraph 23.0x24.5 outline 5px auto #99c8ff offset 0px | = |

Crops: `pagination-default.png`, `pagination-hover.png`, `pagination-focus-visible.png`, `pagination-pressed.png`.

#### pagination-on

Pagination (active). The held page number in the pagination.

Page: blog. Selector: `page on`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 23 x 24.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __Inter_8b46f2 18px/24.48px 400 |
| Letter spacing | normal |
| Colour | #15252d |
| Transition | opacity 0.3s cubic-bezier(0.06, 0.47, 0.1, 1) |
| Cursor | pointer |
| How | at rest |

Crops: `pagination-on-default.png`.

### Contact sales

#### contact-title

Contact title. "Contact us" — Inter 50px 500, eclipse on the light page.

Page: contact. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 498 x 55 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __interFont_b14d2f 50px/55px 500 |
| Letter spacing | normal |
| Colour | #15252d |
| Transition | none |
| How | at rest |

Crops: `contact-title-default.png`.

#### field

Text field. A HubSpot text input: 54px, 16px radius, eclipse fill, 1px white border, Inter 18px. Clicked into once; nothing typed or sent.

Page: contact. Selector: `input.hs-input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 574.03 x 54 | = |
| Padding | 0px 24px | = |
| Border | 1px solid #f8f8f8 | 1px solid #fc5200 |
| Radius | 16px | = |
| Background | #15252d | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | __interFont_b14d2f 18px/25.2px 400 | = |
| Letter spacing | normal | = |
| Colour | #f8f8f8 | = |
| Transition | border-color 0.3s cubic-bezier(0.23, 0.4, 0.53, 0.88) | = |
| Cursor | text | = |
| Placeholder | #ffeadb @ 0.5, opacity 1 | = |
| Painted layers | input.hs-input 574.0x54.0 bg #15252d border T:1px solid #f8f8f8 / R:1px solid #f8f8f8 / B:1px solid #f8f8f8 / L:1px solid #f8f8f8 r 16px | input.hs-input 574.0x54.0 bg #15252d border T:1px solid #fc5200 / R:1px solid #fc5200 / B:1px solid #fc5200 / L:1px solid #fc5200 r 16px |
| How | at rest | clicked into the field |

Crops: `field-default.png`, `field-focused.png`.

#### field-filled

Text field (filled). The same field with text typed, then deleted before close; the form was never submitted.

Page: contact. Selector: `input.hs-input`. States: filled.

| Property | filled |
|---|---|
| Size (w x h) | 574.03 x 54 |
| Padding | 0px 24px |
| Border | 1px solid #fc5200 |
| Radius | 16px |
| Background | #15252d |
| Box shadow | none |
| Outline | none |
| Font | __interFont_b14d2f 18px/25.2px 400 |
| Letter spacing | normal |
| Colour | #f8f8f8 |
| Transition | border-color 0.3s cubic-bezier(0.23, 0.4, 0.53, 0.88) |
| Cursor | text |
| Placeholder | #ffeadb @ 0.5, opacity 1 |
| Painted layers | input.hs-input 574.0x54.0 bg #15252d border T:1px solid #fc5200 / R:1px solid #fc5200 / B:1px solid #fc5200 / L:1px solid #fc5200 r 16px |
| How | typed "name@example.com", then deleted; nothing sent |

Crops: `field-filled-filled.png`.

#### select

Select. A country/topic select: same 54x16 field shell, placeholder state.

Page: contact. Selector: `select.hs-input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 574.03 x 54 | = |
| Padding | 0px 24px | = |
| Border | 1px solid #f8f8f8 | 1px solid #fc5200 |
| Radius | 16px | = |
| Background | #15252d | = |
| Background image | url(data:…) | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | __interFont_b14d2f 18px/25.2px 400 | = |
| Letter spacing | normal | = |
| Colour | #f8f8f8 | = |
| Transition | border-color 0.3s cubic-bezier(0.23, 0.4, 0.53, 0.88) | = |
| Cursor | default | = |
| Painted layers | select.hs-input.is-placeholder 574.0x54.0 bg #15252d image url(data:…) border T:1px solid #f8f8f8 / R:1px solid #f8f8f8 / B:1px solid #f8f8f8 / L:1px solid #f8f8f8 r 16px | select.hs-input.is-placeholder 574.0x54.0 bg #15252d image url(data:…) border T:1px solid #fc5200 / R:1px solid #fc5200 / B:1px solid #fc5200 / L:1px solid #fc5200 r 16px |
| How | at rest | clicked into the field |

Crops: `select-default.png`, `select-focused.png`.

#### textarea

Textarea. The 120px message textarea, same field shell.

Page: contact. Selector: `textarea.hs-input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 574.03 x 120 | = |
| Padding | 0px 24px | = |
| Border | 1px solid #f8f8f8 | 1px solid #fc5200 |
| Radius | 16px | = |
| Background | #15252d | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | __interFont_b14d2f 18px/25.2px 400 | = |
| Letter spacing | normal | = |
| Colour | #f8f8f8 | = |
| Transition | border-color 0.3s cubic-bezier(0.23, 0.4, 0.53, 0.88) | = |
| Cursor | text | = |
| Placeholder | #ffeadb @ 0.5, opacity 1 | = |
| Painted layers | textarea.hs-input.hs-fieldtype-textarea 574.0x120.0 bg #15252d border T:1px solid #f8f8f8 / R:1px solid #f8f8f8 / B:1px solid #f8f8f8 / L:1px solid #f8f8f8 r 16px | textarea.hs-input.hs-fieldtype-textarea 574.0x120.0 bg #15252d border T:1px solid #fc5200 / R:1px solid #fc5200 / B:1px solid #fc5200 / L:1px solid #fc5200 r 16px |
| How | at rest | clicked into the field |

Crops: `textarea-default.png`, `textarea-focused.png`.

#### submit

Submit button. The orange pill submit (50px, radius 9999, Inter 16px 500). Measured and hovered only — never clicked.

Page: contact. Selector: `.hs-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 103.25 x 50 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #fc5200 | = |
| Radius | 9999px | = | = | = |
| Background | #e75e15 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #e75e15 offset 8px | = |
| Font | __interFont_b14d2f 16px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Placeholder | #ffffff, opacity 1 | = | = | = |
| Painted layers | input.hs-button.primary 103.3x50.0 bg #e75e15 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | = | input.hs-button.primary 103.3x50.0 bg #e75e15 border T:1px solid #fc5200 / R:1px solid #fc5200 / B:1px solid #fc5200 / L:1px solid #fc5200 r 9999px outline 2px solid #e75e15 offset 8px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.9 | = | 0.9 |

Crops: `submit-default.png`, `submit-hover.png`, `submit-focus-visible.png`, `submit-pressed.png`.

### Mobile (390 wide)

#### m-nav-bar

Mobile nav bar. The mobile header: logo left, hamburger right.

Page: home. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 65 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __interFont_b14d2f 16px/24px 400 |
| Letter spacing | normal |
| Colour | #15252d |
| Transition | transform, translate, scale, rotate 0.3s cubic-bezier(0.17, 0.17, 0, 1) |
| Icon | 62.33 x 22, colour #15252d |
| Painted layers | div.pointer-events-auto.border-b 390.0x65.0 bg #02060a border B:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.08); span.mx-1.5.hidden 0.0x0.0 bg oklab(0.999994 0.0000455678 0.0000200868 / 0.12); a.h-10.items-center 0.0x0.0 border T:1px solid #f06d2b / R:1px solid #f06d2b / B:1px solid #f06d2b / L:1px solid #f06d2b r 999px; a.h-10.items-center 0.0x0.0 bg #e75e15 border T:1px solid #e75e15 / R:1px solid #e75e15 / B:1px solid #e75e15 / L:1px solid #e75e15 r 999px |
| How | at rest |

Crops: `m-nav-bar-default.png`.

#### m-burger

Hamburger. The mobile menu button. Not opened — the menu overlays the measured content.

Page: home. Selector: `burger`. States: default, pressed.

| Property | default | pressed |
|---|---|---|
| Size (w x h) | 40 x 40 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | __interFont_b14d2f 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | oklab(0.999994 0.0000455678 0.0000200868 / 0.82) | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 20 x 20, colour oklab(0.999994 0.0000455678 0.0000200868 / 0.82) | = |
| How | at rest | CDP forcePseudoState :active:hover |

Crops: `m-burger-default.png`, `m-burger-pressed.png`.

#### m-hero-title

Mobile hero title.

Page: home. Selector: `mobile hero`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 113.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __aeonikFont_a2019c 36px/37.8px 400 |
| Letter spacing | -0.9px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-hero-title-default.png`.

#### m-cta-primary

Mobile primary CTA. The white pill, full width on phone.

Page: home. Selector: `mobile primary`. States: default, pressed.

| Property | default | pressed |
|---|---|---|
| Size (w x h) | 342 x 60 | = |
| Padding | 16px 48px | = |
| Gap | 8px | = |
| Border | 2px solid #000000 @ 0 | = |
| Radius | 999px | = |
| Background | transparent | = |
| Background image | linear-gradient(#02060a, #02060a), conic-gradient(from 458.976deg, #4ca6b5, #f06d2b, #4ca6b5) | linear-gradient(#15252d, #15252d), conic-gradient(from 513.972deg, #7cc3ce, #ff7b3c, #7cc3ce) |
| Box shadow | oklab(0.676327 -0.0761709 -0.0438468 / 0.25) 3.60106px 0.398941px 16px 0px, oklab(0.684338 0.128575 0.123564 / 0.25) -3.60106px -0.398941px 16px 0px | oklab(0.77422 -0.0641362 -0.0343847 / 0.25) 1.15679px 2.84321px 16px 0px, oklab(0.727177 0.128214 0.123105 / 0.25) -1.15679px -2.84321px 16px 0px |
| Outline | none | = |
| Font | __aeonikFont_a2019c 18px/24px 500 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| ::after | 338px x 56px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff @ 0.25 0px 0px 24px 0px | = |
| Painted layers | a.inline-flex.min-h-12 342.0x60.0 image linear-gradient(#02060a, #02060a), conic-gradient(from 458.976deg, #4ca6b5, #f06d2b, #4ca6 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 999px shadow oklab(0.676327 -0.0761709 -0.0438468 / 0.25) 3.60106px 0.398941px 16px 0px, oklab(0.684338 0.128575 0.123564 / 0.25) -3.60106px -0.398941px 16px 0px; a::after.inline-flex.min-h-12 338pxx56px r 999px shadow #ffffff @ 0.25 0px 0px 24px 0px | a.inline-flex.min-h-12 342.0x60.0 image linear-gradient(#15252d, #15252d), conic-gradient(from 513.972deg, #7cc3ce, #ff7b3c, #7cc3 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 999px shadow oklab(0.77422 -0.0641362 -0.0343847 / 0.25) 1.15679px 2.84321px 16px 0px, oklab(0.727177 0.128214 0.123105 / 0.25) -1.15679px -2.84321px 16px 0px; a::after.inline-flex.min-h-12 338pxx56px r 999px shadow #ffffff @ 0.25 0px 0px 24px 0px |
| How | at rest | CDP forcePseudoState :active:hover |

Crops: `m-cta-primary-default.png`, `m-cta-primary-pressed.png`.

#### m-cta-secondary

Mobile secondary CTA. The outline pill under it.

Page: home. Selector: `mobile secondary`. States: default, pressed.

| Property | default | pressed |
|---|---|---|
| Size (w x h) | 342 x 60 | = |
| Padding | 16px 48px | = |
| Gap | 8px | = |
| Border | 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.35) | = |
| Radius | 999px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | __aeonikFont_a2019c 18px/24px 500 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | a.inline-flex.min-h-12 342.0x60.0 border T:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.35) / R:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.35) / B:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.35) / L:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.35) r 999px | = |
| How | at rest | CDP forcePseudoState :active:hover |

Crops: `m-cta-secondary-default.png`, `m-cta-secondary-pressed.png`.

## Transitions declared in the readable stylesheets

apollographql.com is a Next.js build: its stylesheets are same-origin and readable, and it ships a real token layer — the --color-*, --font-*, --radius-* and --duration-* custom properties recorded in css-vars.json — plus Tailwind utilities and CSS modules; the per-state Transition rows are computed values.

- blog: `opacity 0.2s ease-in, filter 0.2s ease-in`, `none`, `background-color var(--duration-normal) var(--ease-slow),border-color var(--duration-normal) var(--ease-slow)`, `color var(--duration-normal) var(--ease-slow)`, `background-color 0.15s`, `background-color 0.15s, border-color 0.15s, color 0.15s`, `color 0.15s, background-color 0.15s`, `transform 0.2s, opacity 0.2s`, `height 0.2s ease-out`, `color 0.15s`, `background-color 0.15s, color 0.15s`, `transform 0.15s`

- contact: `transform 1s var(--ease-galactic-out),opacity 1s var(--ease-galactic-out)`, `transform var(--duration-slow)var(--ease-galactic-out),opacity var(--duration-slow)var(--ease-galactic-out)`, `all var(--duration-normal)var(--ease-galactic)`, `height .5s var(--ease-galactic-out)`, `opacity 0.2s ease-in, filter 0.2s ease-in`, `none`, `background-color var(--duration-normal)var(--ease-slow),border-color var(--duration-normal)var(--ease-slow)`, `color var(--duration-normal)var(--ease-slow)`, `opacity 0.15s`, `border-color var(--duration-normal,.2s) var(--ease-out-soft,ease)`, `background-color 0.2s`, `color var(--duration-normal,.3s) var(--ease-slow,ease-out),transform var(--duration-fast,.2s) var(--ease-slow,ease-out)`

- customers: `transform 1s var(--ease-galactic-out),opacity 1s var(--ease-galactic-out)`, `transform var(--duration-slow)var(--ease-galactic-out),opacity var(--duration-slow)var(--ease-galactic-out)`, `all var(--duration-normal)var(--ease-galactic)`, `height .5s var(--ease-galactic-out)`, `opacity 0.2s ease-in, filter 0.2s ease-in`, `none`, `background-color var(--duration-normal)var(--ease-slow),border-color var(--duration-normal)var(--ease-slow)`, `color var(--duration-normal)var(--ease-slow)`, `border-color var(--duration-normal,.2s) var(--ease-out-soft,ease)`, `background-color 0.2s`, `opacity 0.15s`, `var(--duration-normal) var(--ease-out-soft)`

- home: `transform 1s var(--ease-galactic-out),opacity 1s var(--ease-galactic-out)`, `transform var(--duration-slow)var(--ease-galactic-out),opacity var(--duration-slow)var(--ease-galactic-out)`, `all var(--duration-normal)var(--ease-galactic)`, `height .5s var(--ease-galactic-out)`, `opacity 0.2s ease-in, filter 0.2s ease-in`, `none`, `background-color var(--duration-normal)var(--ease-slow),border-color var(--duration-normal)var(--ease-slow)`, `color var(--duration-normal)var(--ease-slow)`, `opacity 0.15s`, `opacity var(--duration-normal) ease-in-out`, `var(--duration-normal) var(--ease-out-soft)`, `color var(--duration-slow) ease-out`

- pricing: `transform 1s var(--ease-galactic-out),opacity 1s var(--ease-galactic-out)`, `transform var(--duration-slow)var(--ease-galactic-out),opacity var(--duration-slow)var(--ease-galactic-out)`, `all var(--duration-normal)var(--ease-galactic)`, `height .5s var(--ease-galactic-out)`, `opacity 0.2s ease-in, filter 0.2s ease-in`, `none`, `background-color var(--duration-normal)var(--ease-slow),border-color var(--duration-normal)var(--ease-slow)`, `color var(--duration-normal)var(--ease-slow)`, `opacity 0.15s`, `transform var(--duration-fast) var(--ease-out-soft)`, `color var(--duration-normal,.3s) var(--ease-slow,ease-out),transform var(--duration-fast,.2s) var(--ease-slow,ease-out)`, `0.1s`
