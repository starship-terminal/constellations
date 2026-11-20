# Component measurements

Computed styles read from buymeacoffee.com on 2026-11-11 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's two public frontends — the Nuxt marketing pages and the Vite-built creator page and login card — with the CookieYes (cky-*) consent banner hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The white marketing header: FAQ and Wall-of-love links, the Apps and Resources dropdowns, the wordmark, a fake Search-creators field, Log-in and the yellow Sign-up pill.

Page: home. Selector: `#bmc-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 76 |
| Padding | 14px 24px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Circular Medium 16px/24px 400, #222222 |
| Transition | none |
| Icon | 16 x 15, colour #000000 |
| Painted layers | div.flex.justify-between 1440.0x76.0 bg #ffffff; a::before.text-dark.btn-hover-bg 64.3125pxx40px bg #000000 @ 0.05 r 40px; a::before.btn-hover-bg.w-108 103.516pxx40px bg #000000 @ 0.05 r 40px; div::before.btn-hover-bg.cursor-pointer 92.3125pxx40px bg #000000 @ 0.05 r 40px; div.hidden.min-w-150 0.0x0.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.15 0px 0px 2px 0px, #000000 @ 0.04 0px 8px 40px 0px, #000000 @ 0.05 0px 2px 5px 0px; div::before.btn-hover-bg.cursor-pointer 129.641pxx40px bg #000000 @ 0.05 r 40px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The coffee-cup + "Buy me a coffee" wordmark anchor in the header centre.

Page: home. Selector: `#bmc-header a[href="/"]:has(svg)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 175 x 30 |
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
| Transform | matrix(1, 0, 0, 1, -87.5, 0) |
| Cursor | pointer |
| Icon | 175 x 30, colour #000000 |
| Ancestor paint | 1 up div.flex.justify-between bg #ffffff |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link. A plain header link (FAQ); hover paints a 5%-black pill (::before) that scales in.

Page: home. Selector: `#bmc-header a FAQ`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 64.31 x 40 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Circular Medium 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | span: Circular Medium 16px/24px 400, #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 64.3125px x 40px, absolute, bg #000000 @ 0.05, radius 40px | = | = | = |
| Painted layers | a::before.text-dark.btn-hover-bg 64.3125pxx40px bg #000000 @ 0.05 r 40px | = | a.text-dark.btn-hover-bg 64.3x40.0 outline 1px auto #005fcc offset 1px; a::before.text-dark.btn-hover-bg 64.3125pxx40px bg #000000 @ 0.05 r 40px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-trigger

Nav trigger. The Apps label + chevron that opens the header dropdown; toggled by click, never followed.

Page: home. Selector: `#bmc-header div.btn-hover-bg Apps`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 92.31 x 40 | = | - | = |
| Padding | 8px 16px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Circular Medium 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 20 x 20, colour #000000 | = | - | = |
| ::before | 92.3125px x 40px, absolute, bg #000000 @ 0.05, radius 40px | = | - | = |
| Painted layers | div::before.btn-hover-bg.cursor-pointer 92.3125pxx40px bg #000000 @ 0.05 r 40px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-pressed.png`.

#### nav-dropdown

Nav dropdown. The white drop-up-or-down panel the Apps trigger opens (iOS/Android links).

Page: home. Selector: `#bmc-header .drop-up-or-down`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 150 x 120 |
| Padding | 12px |
| Border | none |
| Radius | 12px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.15 0px 0px 2px 0px, #000000 @ 0.04 0px 8px 40px 0px, #000000 @ 0.05 0px 2px 5px 0px |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.flex.p-12: Circular Bold 16px/24px 400, #222222 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 24 x 24, colour #222222, fill #000000 |
| Painted layers | div.visible.min-w-150 150.0x120.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.15 0px 0px 2px 0px, #000000 @ 0.04 0px 8px 40px 0px, #000000 @ 0.05 0px 2px 5px 0px |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-link

Menu link. A link inside the opened header dropdown.

Page: home. Selector: `dropdown link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 126 x 48 | = | = | = |
| Padding | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | #222222 @ 0.05 | #222222 @ 0.05 | #222222 @ 0.05 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | 1px auto #005fcc offset 1px |
| Font | Circular Bold 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #222222, fill #000000 | = | = | = |
| Ancestor paint | 1 up div.visible.min-w-150 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.15 0px 0px 2px 0px, #000000 @ 0.04 0px 8px 40px 0px, #000000 @ 0.05 0px 2px 5px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.flex.p-12 126.0x48.0 bg #222222 @ 0.05 r 10px | a.flex.p-12 126.0x48.0 bg #222222 @ 0.05 r 10px outline 1px auto #005fcc offset 1px | a.flex.p-12 126.0x48.0 bg #222222 @ 0.05 r 10px outline 1px auto #005fcc offset 1px |

Crops: `menu-link-default.png`, `menu-link-hover.png`, `menu-link-focus-visible.png`, `menu-link-pressed.png`.

#### nav-search

Search field. The "Search creators" pill in the header — a fake input that opens a Trending search overlay on click.

Page: home. Selector: `#bmc-header Search creators`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 113.09 x 24 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Circular Book 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #222222 @ 0.7 | = | - | = |
| Transition | none | = | - | = |
| Cursor | text | = | - | = |
| Ancestor paint | 1 up div.cursor-text.px-16 bg #000000 @ 0.03 | 1 up div.cursor-text.px-16 bg #000000 @ 0.05 | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-search-default.png`, `nav-search-hover.png`, `nav-search-pressed.png`.

#### nav-login

Nav login. The Log-in header link; measured never followed.

Page: home. Selector: `#bmc-header a Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 76.81 x 48 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Circular Medium 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 76.8125px x 48px, absolute, bg #000000 @ 0.05, radius 40px | = | = | = |
| Painted layers | a::before.text-dark.btn-hover-bg 76.8125pxx48px bg #000000 @ 0.05 r 40px | = | a.text-dark.btn-hover-bg 76.8x48.0 outline 1px auto #005fcc offset 1px; a::before.text-dark.btn-hover-bg 76.8125pxx48px bg #000000 @ 0.05 r 40px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-cta

Nav CTA. The yellow Sign-up pill (a.bmc-btn whose ::before paints #fd0, scaling on hover).

Page: home. Selector: `#bmc-header a.bmc-btn Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 87.16 x 48 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Circular Medium 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | span.z-1: Circular Medium 16px/24px 400, #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 87.1562px x 48px, absolute, bg #ffdd00, radius 40px | = | = | = |
| Painted layers | a::before.xs:hidden.bmc-btn 87.1562pxx48px bg #ffdd00 r 40px | = | a.xs:hidden.bmc-btn 87.2x48.0 outline 1px auto #005fcc offset 1px; a::before.xs:hidden.bmc-btn 87.1562pxx48px bg #ffdd00 r 40px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### rating

Rating row. The five stars + "Loved by 2,000,000+ creators" row over the hero.

Page: home. Selector: `div.ratings`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 384.55 x 27 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h4.text-dark.text-18: Circular Regular 18px/27px 400, #222222 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 24 x 24, colour #000000 |
| How | at rest |

Crops: `rating-default.png`.

#### hero-title

Hero headline. The 96px "Fund your creative work" display in Circular Bold.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 730 x 190 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Circular Bold 96px/95px 400 |
| Letter spacing | -2.4px |
| Colour | #222222 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero copy. The 22px tagline under the headline.

Page: home. Selector: `hero tagline`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Circular Regular 22px/33px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, -5.6) |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-cta

Hero CTA. The hero Start-my-page yellow pill (div.btn.header-anim, 74px tall); measured never followed.

Page: home. Selector: `div.btn.header-anim`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 255.55 x 74 | = | - | = |
| Padding | 0px 50px | = | - | = |
| Border | none | = | - | = |
| Radius | 9999px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Circular Bold 24px/36px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Text node | h2: Circular Bold 24px/36px 400, #000000 | = | - | = |
| Transition | none | = | - | = |
| Transform | matrix(1, 0, 0, 1, 0, -28) | matrix(1, 0, 0, 1, 0, -23.6) | - | matrix(1, 0, 0, 1, 0, -29.2) |
| Cursor | pointer | = | - | = |
| Painted layers | div.btn-bg.absolute 255.5x74.0 bg #ffdd00 r 9999px | div.btn-bg.absolute 260.9x77.0 bg #ffdd00 r 9999px | - | div.btn-bg.absolute 260.9x77.0 bg #ffdd00 r 9999px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-pressed.png`.

#### creator-card

Creator card. A floating creator card in the hero artwork (white tile, avatar, supporter count).

Page: home. Selector: `div.creator-tile`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 199.73 x 180.67 |
| Padding | 9px 14px |
| Gap | 8px normal |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.15 0px 0px 2px 0px, #000000 @ 0.04 0px 8px 40px 0px, #000000 @ 0.05 0px 2px 5px 0px |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.text-[15px].leading-16: Circular Book 15px/16px 400, #222222 |
| Transition | all 0.2s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Cursor | pointer |
| Icon | 12.54 x 12.54, colour #000000 |
| Painted layers | div.creator-tile.w-full 199.7x180.7 bg #ffffff r 16px shadow #000000 @ 0.15 0px 0px 2px 0px, #000000 @ 0.04 0px 8px 40px 0px, #000000 @ 0.05 0px 2px 5px 0px |
| Ancestor paint | 1 up a.active.animate bg #ffffff @ 0.7 |
| How | at rest |

Crops: `creator-card-default.png`.

#### section-eyebrow

Eyebrow. The 16px section eyebrow (SUPPORT / MEMBERSHIPS / SHOP, CSS-uppercased).

Page: home. Selector: `h2 eyebrow`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 936 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Circular Bold 16px/16px 700 |
| Letter spacing | 2px |
| Colour | #717171 |
| Transition | all 0.8s cubic-bezier(0.2, 0.75, 0.28, 0.9) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Ancestor paint | 1 up div.mx-auto.container-main-features bg #ffffff |
| How | at rest |

Crops: `section-eyebrow-default.png`.

#### section-h2

Section heading. A 64px section heading in Circular Bold.

Page: home. Selector: `h2 section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 858 x 160 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Circular Bold 64px/80px 400 |
| Letter spacing | -2px |
| Colour | #222222 |
| Transition | all 0.8s cubic-bezier(0.2, 0.75, 0.28, 0.9) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Ancestor paint | 1 up div.mx-auto.container-main-features bg #ffffff |
| How | at rest |

Crops: `section-h2-default.png`.

#### section-lede

Section lede. The 24px Circular Regular lede under a section heading.

Page: home. Selector: `h3 lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 936 x 64 |
| Padding | 0px 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Circular Regular 24px/32px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| Ancestor paint | 1 up div.mx-auto.container-main-features bg #ffffff |
| How | at rest |

Crops: `section-lede-default.png`.

#### page-field

Page field. The #faf8f0 cream wrapper the marketing pages paint on.

Page: home. Selector: `div.bg-floral-white`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 5806.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #faf8f0 |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Circular Medium 16px/24px 400, #222222 |
| Transition | none |
| Icon | 16 x 15, colour #000000 |
| Painted layers | div.bg-floral-white.relative 1440.0x5806.4 bg #faf8f0; div.flex.justify-between 1440.0x76.0 bg #ffffff; a::before.text-dark.btn-hover-bg 64.3125pxx40px bg #000000 @ 0.05 r 40px; a::before.btn-hover-bg.w-108 103.516pxx40px bg #000000 @ 0.05 r 40px; div::before.btn-hover-bg.cursor-pointer 92.3125pxx40px bg #000000 @ 0.05 r 40px; div.hidden.min-w-150 0.0x0.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.15 0px 0px 2px 0px, #000000 @ 0.04 0px 8px 40px 0px, #000000 @ 0.05 0px 2px 5px 0px |
| How | at rest |

Crops: none.

### Creator page

#### c-header

Profile header. The sticky creator-page bar: avatar, name, supporter count, the Home/Membership/Wishlist tabs, more-options and Login.

Page: creator. Selector: `div.tw-header-shadow`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.06 0px 1px 1px 0px, #000000 @ 0 0px 0px 1px 0px |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.text-lg.font-cr-bold: Circular Bold 19px/28.5px 400, #222222 |
| Transition | none |
| Icon | 16 x 4, colour #222222 |
| Painted layers | div.relative.tw-header-shadow 1440.0x64.0 bg #ffffff shadow #000000 @ 0.06 0px 1px 1px 0px, #000000 @ 0 0px 0px 1px 0px; a::after.tw-tab-each.border-before 100%x1px bg #ff813f; a::after.tw-tab-each.border-before 0%x1px bg #ff813f; a::after.tw-tab-each.border-before 0%x1px bg #ff813f; div.h-[1px].bg-greyE9 0.0x0.0 bg #e9e9e9; a::after.tw-tab-each.border-before 41.3438pxx1px bg #ff813f |
| Ancestor paint | 1 up div.min-h-screen.bg-white bg #ffffff |
| How | at rest |

Crops: `c-header-default.png`.

#### c-tab

Tab link. A profile tab (Home/Membership/Wishlist); the active tab paints the theme-colour underline (::before).

Page: creator. Selector: `a.tw-tab-each`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 49.34 x 31.5 | = | = | = |
| Padding | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Circular Medium 15px/22.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ff813f | = | = | = |
| Text node | span.capitalize: Circular Medium 15px/22.5px 400, #ff813f | = | = | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 41.3438px x 1px, static, bg #ff813f, radius 0px | = | = | = |
| Painted layers | a::after.tw-tab-each.border-before 41.3438pxx1px bg #ff813f | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `c-tab-default.png`, `c-tab-hover.png`, `c-tab-focus-visible.png`, `c-tab-pressed.png`.

#### c-login

Header login. The Login link at the profile header's right edge; measured never followed.

Page: creator. Selector: `header Login`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 37.55 x 22.5 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Circular Book 15px/22.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | all 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `c-login-default.png`, `c-login-hover.png`, `c-login-focus-visible.png`, `c-login-pressed.png`.

#### c-more

More options. The ellipsis trigger (aria-haspopup=menu) that opens the profile context menu.

Page: creator. Selector: `[aria-label="more options"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #222222 @ 0.05 | = | = | #222222 @ 0.1 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | ui-sans-serif 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | all 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 4, colour #222222 | = | = | = |
| Painted layers | div.w-8.h-8 32.0x32.0 bg #222222 @ 0.05 r 9999px | = | div.w-8.h-8 32.0x32.0 bg #222222 @ 0.05 r 9999px outline 1px auto #005fcc offset 0px | div.w-8.h-8 32.0x32.0 bg #222222 @ 0.1 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `c-more-default.png`, `c-more-hover.png`, `c-more-focus-visible.png`, `c-more-pressed.png`.

#### c-context

Context menu. The small menu the more-options trigger opens: Follow, Share, Report.

Page: creator. Selector: `ul[role=menu]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 198 x 120 |
| Padding | 6px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | div.text-dark.text-sm: Circular Book 15px/20px 400, #222222 |
| Transition | none |
| Icon | 20 x 20, colour #222222 |
| Ancestor paint | 1 up div.w-[200px].origin-top-right bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #212121 @ 0.05 0px 0px 16px 0px |
| How | at rest |

Crops: `c-context-default.png`.

#### c-about

About box. The "About Cara" sidebar box (aria region): bio copy, links, icon row.

Page: creator. Selector: `[role=region][aria-label="About Cara"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 452 x 321 |
| Padding | 0px 0px 24px 0px |
| Border | T: none; R: none; B: 1px solid #dddddd @ 0.8; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.text-md.xs:pr-4: Circular Medium 16px/24px 400, #222222 |
| Transition | none |
| Icon | 20 x 20, colour #000000 |
| Painted layers | div.pb-6.mb-6 452.0x321.0 border B:1px solid #dddddd @ 0.8 |
| Ancestor paint | 1 up div.tw-feature-box.xs:bg-transparent bg #ffffff |
| How | at rest |

Crops: `c-about-default.png`.

#### c-widget

Support widget. The "Buy Cara a coffee" card (aria region): quantity pills, custom amount, name field, message, monthly checkbox, the orange Support button.

Page: creator. Selector: `[role=region][aria-label="Support Cara"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 500 x 507 |
| Padding | 32px 40px |
| Border | none |
| Radius | 24px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.text-2xl.text-dark: Circular Bold 24px/32px 400, #222222 |
| Transition | none |
| Icon | 16 x 16, colour #000000 |
| Painted layers | div.tw-feature-box.!px-10 500.0x507.0 bg #ffffff r 24px; div.absolute.transition-all 228.0x81.7 bg #ffffff border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 8px shadow #000000 @ 0.05 0px 5px 20px 0px; div.-bottom-0.h-3 226.1x11.4 bg #ffffff r 6px; div.-bottom-1.tooltip-arrow 16.1x16.1 bg #ffffff border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb shadow #000000 @ 0.05 0px 5px 20px 0px; div.items-center.rounded-xl 420.0x82.0 bg #ff813f @ 0.05 border T:1px solid #ff813f @ 0.25 / R:1px solid #ff813f @ 0.25 / B:1px solid #ff813f @ 0.25 / L:1px solid #ff813f @ 0.25 r 12px; div.bg-pageTheme.text-themeTextColor 48.0x48.0 bg #ff813f border T:1px solid #ff813f @ 0.25 / R:1px solid #ff813f @ 0.25 / B:1px solid #ff813f @ 0.25 / L:1px solid #ff813f @ 0.25 r 9999px |
| How | at rest |

Crops: `c-widget-default.png`.

#### c-qty-on

Quantity pill, selected. The checked coffee-count pill: the theme-colour #FF813F fill with white count.

Page: creator. Selector: `.tw-coffee-counter.bg-pageTheme`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #ff813f @ 0.25 | 1px solid #ff813f | = | 1px solid #ff813f |
| Radius | 9999px | = | = | = |
| Background | #ff813f | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.text-lg.font-cr-bold: Circular Bold 19px/28.5px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Painted layers | div.bg-pageTheme.text-themeTextColor 48.0x48.0 bg #ff813f border T:1px solid #ff813f @ 0.25 / R:1px solid #ff813f @ 0.25 / B:1px solid #ff813f @ 0.25 / L:1px solid #ff813f @ 0.25 r 9999px; input.absolute.opacity-0 46.0x46.0 bg #2563eb image url(data:…) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 100% | div.bg-pageTheme.text-themeTextColor 48.0x48.0 bg #ff813f border T:1px solid #ff813f / R:1px solid #ff813f / B:1px solid #ff813f / L:1px solid #ff813f r 9999px; input.absolute.opacity-0 46.0x46.0 bg #2563eb image url(data:…) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 100% | div.bg-pageTheme.text-themeTextColor 48.0x48.0 bg #ff813f border T:1px solid #ff813f @ 0.25 / R:1px solid #ff813f @ 0.25 / B:1px solid #ff813f @ 0.25 / L:1px solid #ff813f @ 0.25 r 9999px; input.absolute.opacity-0 46.0x46.0 bg #2563eb image url(data:…) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 100% shadow #ffffff 0px 0px 0px 2px, #2563eb 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | div.bg-pageTheme.text-themeTextColor 48.0x48.0 bg #ff813f border T:1px solid #ff813f / R:1px solid #ff813f / B:1px solid #ff813f / L:1px solid #ff813f r 9999px; input.absolute.opacity-0 46.0x46.0 bg #2563eb image url(data:…) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 100% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `c-qty-on-default.png`, `c-qty-on-hover.png`, `c-qty-on-focus-visible.png`, `c-qty-on-pressed.png`.

#### c-qty-off

Quantity pill. An unchecked coffee-count pill (white fill, theme-colour count and hairline border).

Page: creator. Selector: `.tw-coffee-counter.bg-white`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #ff813f @ 0.25 | 1px solid #ff813f | = | 1px solid #ff813f |
| Radius | 9999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ff813f | = | = | = |
| Text node | span.text-lg.font-cr-bold: Circular Bold 19px/28.5px 400, #ff813f | = | = | = |
| Transition | none | = | = | = |
| Painted layers | div.bg-white.text-pageTheme 48.0x48.0 bg #ffffff border T:1px solid #ff813f @ 0.25 / R:1px solid #ff813f @ 0.25 / B:1px solid #ff813f @ 0.25 / L:1px solid #ff813f @ 0.25 r 9999px; input.absolute.opacity-0 46.0x46.0 bg #ffffff border T:1px solid #6b7280 / R:1px solid #6b7280 / B:1px solid #6b7280 / L:1px solid #6b7280 r 100% | div.bg-white.text-pageTheme 48.0x48.0 bg #ffffff border T:1px solid #ff813f / R:1px solid #ff813f / B:1px solid #ff813f / L:1px solid #ff813f r 9999px; input.absolute.opacity-0 46.0x46.0 bg #ffffff border T:1px solid #6b7280 / R:1px solid #6b7280 / B:1px solid #6b7280 / L:1px solid #6b7280 r 100% | div.bg-white.text-pageTheme 48.0x48.0 bg #ffffff border T:1px solid #ff813f @ 0.25 / R:1px solid #ff813f @ 0.25 / B:1px solid #ff813f @ 0.25 / L:1px solid #ff813f @ 0.25 r 9999px; input.absolute.opacity-0 46.0x46.0 bg #ffffff border T:1px solid #6b7280 / R:1px solid #6b7280 / B:1px solid #6b7280 / L:1px solid #6b7280 r 100% shadow #ffffff 0px 0px 0px 2px, #2563eb 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | div.bg-white.text-pageTheme 48.0x48.0 bg #ffffff border T:1px solid #ff813f / R:1px solid #ff813f / B:1px solid #ff813f / L:1px solid #ff813f r 9999px; input.absolute.opacity-0 46.0x46.0 bg #ffffff border T:1px solid #6b7280 / R:1px solid #6b7280 / B:1px solid #6b7280 / L:1px solid #6b7280 r 100% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `c-qty-off-default.png`, `c-qty-off-hover.png`, `c-qty-off-focus-visible.png`, `c-qty-off-pressed.png`.

#### c-amount

Custom amount. The free-amount field inside the last quantity pill (number input, "20").

Page: creator. Selector: `input[aria-label="quantity input"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 48 x 48 |
| Padding | 12px 4px |
| Border | 1px solid #222222 @ 0.1 |
| Radius | 12px |
| Background | #ffffff |
| Box shadow | #ffffff 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | 2px solid #000000 @ 0 offset 2px |
| Font | Circular Medium 19px/24px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | all 0.25s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | text |
| Placeholder | #222222 @ 0.3, opacity 1 |
| Painted layers | input.w-full.tw-remove-default-styling 48.0x48.0 bg #ffffff border T:1px solid #222222 @ 0.1 / R:1px solid #222222 @ 0.1 / B:1px solid #222222 @ 0.1 / L:1px solid #222222 @ 0.1 r 12px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `c-amount-default.png`.

#### c-name

Name field. The "Name or @yoursocial" text input in the support widget.

Page: creator. Selector: `#supporterDisplayName`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 420 x 52 | = | = |
| Padding | 12px | = | = |
| Border | 2px solid #000000 @ 0 | 2px solid #ff813f | 2px solid #ff813f |
| Radius | 12px | = | = |
| Background | #f0f0f0 | #ffffff | #ffffff |
| Box shadow | #ffffff 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | Circular Book 17px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #151515 | = | = |
| Transition | all 0.25s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #6b7280, opacity 1 | = | = |
| Painted layers | input.w-full.tw-remove-default-styling 420.0x52.0 bg #f0f0f0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | input.w-full.tw-remove-default-styling 420.0x52.0 bg #ffffff border T:2px solid #ff813f / R:2px solid #ff813f / B:2px solid #ff813f / L:2px solid #ff813f r 12px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | input.w-full.tw-remove-default-styling 420.0x52.0 bg #ffffff border T:2px solid #ff813f / R:2px solid #ff813f / B:2px solid #ff813f / L:2px solid #ff813f r 12px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "Ada", then deleted; nothing sent |

Crops: `c-name-default.png`, `c-name-focused.png`, `c-name-filled.png`.

#### c-message

Message field. The "Say something nice..." textarea (tw-box-common-v2).

Page: creator. Selector: `textarea Say something`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 416 x 100 | = |
| Padding | 12px | = |
| Border | none | = |
| Radius | 12px | = |
| Background | transparent | = |
| Box shadow | #ffffff 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | 2px solid #000000 @ 0 offset 2px | = |
| Font | Circular Book 17px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #151515 | = |
| Transition | all 0.25s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #6b7280, opacity 1 | = |
| ::before | auto x auto, absolute, bg #000000 @ 0, radius 0px | = |
| Painted layers | textarea.tw-box-common-v2.tw-input-common 416.0x100.0 r 12px shadow #ffffff 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | textarea.tw-box-common-v2.tw-input-common 416.0x100.0 r 12px shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up div.undefined.relative bg #f0f0f0 | 1 up div.undefined.relative bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field |

Crops: `c-message-default.png`, `c-message-focused.png`.

#### c-monthly

Monthly checkbox. The "Make this monthly" checkbox label; the visible box is a .tw-checkmark span.

Page: creator. Selector: `label[for=doMonthlySupport]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 150.34 x 25.5 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.text-dark.text-sm: Circular Regular 15px/22.5px 400, #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | input.tw-checkbox.absolute 150.3x25.5 bg #ffffff border T:1px solid #6b7280 / R:1px solid #6b7280 / B:1px solid #6b7280 / L:1px solid #6b7280; span.border-dark/50.hover:border-dark/90 20.0x20.0 border T:1px solid #222222 @ 0.5 / R:1px solid #222222 @ 0.5 / B:1px solid #222222 @ 0.5 / L:1px solid #222222 @ 0.5 r 6px shadow #ffffff 0px 0px 0px 0px, #d1d5db 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span::after.border-dark/50.hover:border-dark/90 14pxx14px image url(data:…) shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | input.tw-checkbox.absolute 150.3x25.5 bg #ffffff border T:1px solid #6b7280 / R:1px solid #6b7280 / B:1px solid #6b7280 / L:1px solid #6b7280 shadow #ffffff 0px 0px 0px 2px, #2563eb 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px; span.border-dark/50.hover:border-dark/90 20.0x20.0 border T:1px solid #222222 @ 0.5 / R:1px solid #222222 @ 0.5 / B:1px solid #222222 @ 0.5 / L:1px solid #222222 @ 0.5 r 6px shadow #ffffff 0px 0px 0px 0px, #d1d5db 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span::after.border-dark/50.hover:border-dark/90 14pxx14px image url(data:…) shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `c-monthly-default.png`, `c-monthly-hover.png`, `c-monthly-focus-visible.png`, `c-monthly-pressed.png`.

#### c-private

Private checkbox. The "Make this message private" checkbox label.

Page: creator. Selector: `label[for=makeMsgPrivate]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 204.59 x 25.5 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.text-dark.text-sm: Circular Regular 15px/22.5px 400, #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | input.tw-checkbox.absolute 204.6x25.5 bg #ffffff border T:1px solid #6b7280 / R:1px solid #6b7280 / B:1px solid #6b7280 / L:1px solid #6b7280; span.border-dark/50.hover:border-dark/90 20.0x20.0 border T:1px solid #222222 @ 0.5 / R:1px solid #222222 @ 0.5 / B:1px solid #222222 @ 0.5 / L:1px solid #222222 @ 0.5 r 6px shadow #ffffff 0px 0px 0px 0px, #d1d5db 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span::after.border-dark/50.hover:border-dark/90 14pxx14px image url(data:…) shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | input.tw-checkbox.absolute 204.6x25.5 bg #ffffff border T:1px solid #6b7280 / R:1px solid #6b7280 / B:1px solid #6b7280 / L:1px solid #6b7280 shadow #ffffff 0px 0px 0px 2px, #2563eb 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px; span.border-dark/50.hover:border-dark/90 20.0x20.0 border T:1px solid #222222 @ 0.5 / R:1px solid #222222 @ 0.5 / B:1px solid #222222 @ 0.5 / L:1px solid #222222 @ 0.5 r 6px shadow #ffffff 0px 0px 0px 0px, #d1d5db 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span::after.border-dark/50.hover:border-dark/90 14pxx14px image url(data:…) shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `c-private-default.png`, `c-private-hover.png`, `c-private-focus-visible.png`, `c-private-pressed.png`.

#### c-support

Support button. The orange "Support $5" submit pill: a type=submit button measured in every state, never pressed.

Page: creator. Selector: `button.tw-btn-bg Support`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 420 x 48 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Circular Bold 17px/25.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.opacity-100.bmc-btn-v-7: Circular Bold 17px/25.5px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 420px x 48px, absolute, bg #ff813f, radius 9999px | 420px x 48px, absolute, bg #ff6b1c, radius 9999px | = | 420px x 48px, absolute, bg #ff6b1c, radius 9999px |
| Painted layers | button::before.tw-btn-bg.relative 420pxx48px bg #ff813f r 9999px; span.dot-flashing.bg-themeTextColor 8.0x8.0 bg #ffffff @ 0.537 r 9999px; span::before.dot-flashing.bg-themeTextColor 8pxx8px bg #ffffff @ 0.64 r 9999px; span::after.dot-flashing.bg-themeTextColor 8pxx8px bg #ffffff @ 0.5 r 9999px | button::before.tw-btn-bg.relative 420pxx48px bg #ff6b1c r 9999px; span.dot-flashing.bg-themeTextColor 8.0x8.0 bg #ffffff @ 0.5 r 9999px; span::before.dot-flashing.bg-themeTextColor 8pxx8px bg #ffffff @ 0.5 r 9999px; span::after.dot-flashing.bg-themeTextColor 8pxx8px bg #ffffff @ 0.7 r 9999px | button.tw-btn-bg.relative 420.0x48.0 outline 2px solid #000000 @ 0 offset 2px; button::before.tw-btn-bg.relative 420pxx48px bg #ff813f r 9999px; span.dot-flashing.bg-themeTextColor 8.0x8.0 bg #ffffff @ 0.5 r 9999px; span::before.dot-flashing.bg-themeTextColor 8pxx8px bg #ffffff @ 0.5 r 9999px; span::after.dot-flashing.bg-themeTextColor 8pxx8px bg #ffffff @ 0.5 r 9999px | button::before.tw-btn-bg.relative 420pxx48px bg #ff6b1c r 9999px; span.dot-flashing.bg-themeTextColor 8.0x8.0 bg #ffffff @ 0.92 r 9999px; span::before.dot-flashing.bg-themeTextColor 8pxx8px bg #ffffff @ 0.54 r 9999px; span::after.dot-flashing.bg-themeTextColor 8pxx8px bg #ffffff @ 0.5 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `c-support-default.png`, `c-support-hover.png`, `c-support-focus-visible.png`, `c-support-pressed.png`.

#### c-supporter

Supporter row. A row in the Recent-supporters list ("SolanaNami bought 2 coffees"), avatar + text + more icon.

Page: creator. Selector: `supporter row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 364 x 22.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Circular Regular 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Circular Medium 15px/22.5px 400, #222222 |
| Transition | none |
| How | at rest |

Crops: `c-supporter-default.png`.

#### c-tier

Membership tier. A membership-level group in "Become a member": tier name, price, benefits list, Join button.

Page: creator. Selector: `[role=group][aria-label*="membership level"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 420 x 262 |
| Padding | 0px 0px 12px 0px |
| Border | T: none; R: none; B: 1px solid #dddddd @ 0.8; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | h2.font-cr-bold.text-xl: Circular Bold 20px/28px 400, #222222 |
| Transition | none |
| Icon | 18 x 18, colour #222222 |
| Painted layers | div.text-dark.relative 420.0x262.0 border B:1px solid #dddddd @ 0.8; button::before.tw-btn-bg.relative 420pxx48px bg #ff813f r 9999px; span.dot-flashing.bg-themeTextColor 8.0x8.0 bg #ffffff @ 0.5 r 9999px; span::before.dot-flashing.bg-themeTextColor 8pxx8px bg #ffffff @ 0.5 r 9999px; span::after.dot-flashing.bg-themeTextColor 8pxx8px bg #ffffff @ 0.57 r 9999px; span.inline-block.w-2 8.0x8.0 bg #222222 r 9999px |
| How | at rest |

Crops: `c-tier-default.png`.

#### c-join

Join button. A membership tier's join action; measured never followed.

Page: creator. Selector: `tier Join button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 420 x 48 | = | = | = |
| Padding | 0px 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Circular Bold 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.opacity-100.bmc-btn-v-9: Circular Bold 16px/24px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 420px x 48px, absolute, bg #ff813f, radius 9999px | 420px x 48px, absolute, bg #ff6b1c, radius 9999px | = | 420px x 48px, absolute, bg #ff6b1c, radius 9999px |
| Painted layers | button::before.tw-btn-bg.relative 420pxx48px bg #ff813f r 9999px; span.dot-flashing.bg-themeTextColor 8.0x8.0 bg #ffffff @ 0.576 r 9999px; span::before.dot-flashing.bg-themeTextColor 8pxx8px bg #ffffff @ 0.7 r 9999px; span::after.dot-flashing.bg-themeTextColor 8pxx8px bg #ffffff @ 0.5 r 9999px | button::before.tw-btn-bg.relative 420pxx48px bg #ff6b1c r 9999px; span.dot-flashing.bg-themeTextColor 8.0x8.0 bg #ffffff @ 0.5 r 9999px; span::before.dot-flashing.bg-themeTextColor 8pxx8px bg #ffffff @ 0.5 r 9999px; span::after.dot-flashing.bg-themeTextColor 8pxx8px bg #ffffff @ 0.78 r 9999px | button.tw-btn-bg.relative 420.0x48.0 outline 2px solid #000000 @ 0 offset 2px; button::before.tw-btn-bg.relative 420pxx48px bg #ff813f r 9999px; span.dot-flashing.bg-themeTextColor 8.0x8.0 bg #ffffff @ 0.5 r 9999px; span::before.dot-flashing.bg-themeTextColor 8pxx8px bg #ffffff @ 0.518 r 9999px; span::after.dot-flashing.bg-themeTextColor 8pxx8px bg #ffffff @ 0.5 r 9999px | button::before.tw-btn-bg.relative 420pxx48px bg #ff6b1c r 9999px; span.dot-flashing.bg-themeTextColor 8.0x8.0 bg #ffffff @ 0.882 r 9999px; span::before.dot-flashing.bg-themeTextColor 8pxx8px bg #ffffff @ 0.525 r 9999px; span::after.dot-flashing.bg-themeTextColor 8pxx8px bg #ffffff @ 0.5 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `c-join-default.png`, `c-join-hover.png`, `c-join-focus-visible.png`, `c-join-pressed.png`.

#### c-follow

Follow item. The Follow row inside the more-options menu (follow-user); measured never toggled — following needs an account.

Page: creator. Selector: `li.follow-user`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 186 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | 1px auto #005fcc offset 0px |
| Font | ui-sans-serif 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | div.text-dark.text-sm: Circular Book 15px/20px 400, #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #222222 | = | = | = |
| Ancestor paint | 2 up div.w-[200px].origin-top-right bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #212121 @ 0.05 0px 0px 16px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | div.px-3.py-2 186.0x36.0 bg #222222 @ 0.05 r 8px | li.cursor-pointer.select-none 186.0x36.0 outline 1px auto #005fcc offset 0px; div.px-3.py-2 186.0x36.0 bg #222222 @ 0.05 r 8px | li.cursor-pointer.select-none 186.0x36.0 outline 1px auto #005fcc offset 0px; div.px-3.py-2 186.0x36.0 bg #222222 @ 0.05 r 8px |

Crops: `c-follow-default.png`, `c-follow-hover.png`, `c-follow-focus-visible.png`, `c-follow-pressed.png`.

#### c-share

Share item. The Share row inside the more-options menu (px-3 py-2, dark/5 hover fill).

Page: creator. Selector: `menu Share li`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 186 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | 1px auto #005fcc offset 0px |
| Font | ui-sans-serif 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | div.text-dark.font-cr-book: Circular Book 15px/20px 400, #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #222222 | = | = | = |
| Ancestor paint | 2 up div.w-[200px].origin-top-right bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #212121 @ 0.05 0px 0px 16px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | div.px-3.py-2 186.0x36.0 bg #222222 @ 0.05 r 8px | li.cursor-pointer 186.0x36.0 outline 1px auto #005fcc offset 0px; div.px-3.py-2 186.0x36.0 bg #222222 @ 0.05 r 8px | li.cursor-pointer 186.0x36.0 outline 1px auto #005fcc offset 0px; div.px-3.py-2 186.0x36.0 bg #222222 @ 0.05 r 8px |

Crops: `c-share-default.png`, `c-share-hover.png`, `c-share-focus-visible.png`, `c-share-pressed.png`.

#### c-page-field

Page field. The white wrapper a creator page paints on (carries the inline --theme-color* vars).

Page: creator. Selector: `div.min-h-screen.bg-white`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 2356.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.text-lg.font-cr-bold: Circular Bold 19px/28.5px 400, #222222 |
| Transition | none |
| Icon | 16 x 4, colour #222222 |
| Painted layers | div.min-h-screen.bg-white 1440.0x2356.5 bg #ffffff; div.relative.tw-header-shadow 1440.0x64.0 bg #ffffff shadow #000000 @ 0.06 0px 1px 1px 0px, #000000 @ 0 0px 0px 1px 0px; a::after.tw-tab-each.border-before 100%x1px bg #ff813f; a::after.tw-tab-each.border-before 0%x1px bg #ff813f; a::after.tw-tab-each.border-before 0%x1px bg #ff813f; div.h-[1px].bg-greyE9 0.0x0.0 bg #e9e9e9 |
| How | at rest |

Crops: none.

### Login

#### l-title

Login title. The "Welcome back" heading on the centred login card.

Page: login. Selector: `Welcome back`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 380 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Circular Bold 30px/36px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: none.

#### l-email

Email field. The Email input on the login card (grey fill, rounded); typed into and cleared, never submitted.

Page: login. Selector: `input Email`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 380 x 48 | = | = |
| Padding | 12px 16px | = | = |
| Border | 2px solid #000000 @ 0 | 2px solid #151515 | 2px solid #151515 |
| Radius | 12px | = | = |
| Background | #f0f0f0 | #ffffff | #ffffff |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px | 2px solid #000000 @ 0 offset 2px |
| Font | Circular Medium 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #222222 | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, -webkit-backdrop-filter, backdrop-filter 0.075s cubic-bezier(0.4, 0, 0.2, 1) | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, -webkit-backdrop-filter, backdrop-filter 0.075s cubic-bezier(0, 0, 0.2, 1) | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, -webkit-backdrop-filter, backdrop-filter 0.075s cubic-bezier(0, 0, 0.2, 1) |
| Cursor | text | = | = |
| Placeholder | #717171, opacity 1 | = | = |
| Painted layers | input.w-full.border-2 380.0x48.0 bg #f0f0f0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px | input.w-full.border-2 380.0x48.0 bg #ffffff border T:2px solid #151515 / R:2px solid #151515 / B:2px solid #151515 / L:2px solid #151515 r 12px shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | input.w-full.border-2 380.0x48.0 bg #ffffff border T:2px solid #151515 / R:2px solid #151515 / B:2px solid #151515 / L:2px solid #151515 r 12px shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: none.

#### l-cta

Continue button. The yellow "Continue with email" pill (tw-btn-bg, theme-colour paint); a submit button measured, never pressed.

Page: login. Selector: `button.tw-btn-bg Continue with email`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 380 x 48 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Circular Medium 17px/25.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.opacity-100.bmc-btn-v-2: Circular Medium 17px/25.5px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 380px x 48px, absolute, bg #ffdd00, radius 9999px | 380px x 48px, absolute, bg #ffc800, radius 9999px | = | 380px x 48px, absolute, bg #ffc800, radius 9999px |
| Painted layers | button::before.tw-btn-bg.relative 380pxx48px bg #ffdd00 r 9999px; span.dot-flashing-dark.bg-dark 8.0x8.0 bg #222222 r 9999px; span::before.dot-flashing-dark.bg-dark 8pxx8px bg #222222 r 9999px; span::after.dot-flashing-dark.bg-dark 8pxx8px bg #222222 r 9999px | button::before.tw-btn-bg.relative 380pxx48px bg #ffc800 r 9999px; span.dot-flashing-dark.bg-dark 8.0x8.0 bg #222222 r 9999px; span::before.dot-flashing-dark.bg-dark 8pxx8px bg #222222 r 9999px; span::after.dot-flashing-dark.bg-dark 8pxx8px bg #222222 r 9999px | button.tw-btn-bg.relative 380.0x48.0 outline 2px solid #000000 @ 0 offset 2px; button::before.tw-btn-bg.relative 380pxx48px bg #ffdd00 r 9999px; span.dot-flashing-dark.bg-dark 8.0x8.0 bg #222222 r 9999px; span::before.dot-flashing-dark.bg-dark 8pxx8px bg #222222 r 9999px; span::after.dot-flashing-dark.bg-dark 8pxx8px bg #222222 r 9999px | button::before.tw-btn-bg.relative 380pxx48px bg #ffc800 r 9999px; span.dot-flashing-dark.bg-dark 8.0x8.0 bg #222222 r 9999px; span::before.dot-flashing-dark.bg-dark 8pxx8px bg #222222 r 9999px; span::after.dot-flashing-dark.bg-dark 8pxx8px bg #222222 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### l-social

Social button. A white "Continue with Google" button (greyE5 border, rounded-lg); measured never pressed.

Page: login. Selector: `button Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 380 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #e5e5e5 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #222222 @ 0.05 | = | #222222 @ 0.05 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Circular Book 15px/22.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | span.auth-social-google-btn-v-3: Circular Book 15px/22.5px 400, #222222 | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 22 x 22, colour #222222 | = | = | = |
| Painted layers | button.relative.bg-white 380.0x48.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px | button.relative.bg-white 380.0x48.0 bg #222222 @ 0.05 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px | button.relative.bg-white 380.0x48.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px outline 2px solid #000000 @ 0 offset 2px | button.relative.bg-white 380.0x48.0 bg #222222 @ 0.05 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### l-divider

Divider. The "or login with" divider between the email pill and the social buttons.

Page: login. Selector: `or login with`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 380 x 65 |
| Padding | 32px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Circular Regular 15px/22.5px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | span.bg-white.py-2: Circular Regular 15px/22.5px 400, #222222 |
| Transition | none |
| Painted layers | span.block.w-full 380.0x1.0 bg #e5e5e5; span.bg-white.py-2 114.3x38.5 bg #ffffff |
| How | at rest |

Crops: none.

#### l-signup-link

Signup link. The "Sign up" link at the card's top right ("Don't have an account?").

Page: login. Selector: `Sign up link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56.64 x 25.5 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Circular Regular 17px/25.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

### Reviews

#### r-title

Wall title. The "Wall of ❤" page title.

Page: reviews. Selector: `h1 on /reviews`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 239.38 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Borel Regular 64px/96px 400 |
| Letter spacing | normal |
| Colour | #1f2022 |
| Transition | none |
| How | at rest |

Crops: `r-title-default.png`.

#### r-tweet

Tweet card. A testimonial card on the Wall of Love (white, shadow-sm, slight transform on hover).

Page: reviews. Selector: `a.tweet-card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 371.09 x 306 | 381.55 x 318.76 | = | 381.55 x 318.76 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 4px 0px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | ui-sans-serif 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.text-13.font-cr-medium: Circular Medium 13px/19.5px 400, #222222 | = | = | = |
| Transition | all 0.1s linear | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.xs:w-300.bg-white 371.1x306.0 bg #ffffff r 24px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 4px 0px | a.xs:w-300.bg-white 381.5x318.8 bg #ffffff r 24px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 4px 0px | a.xs:w-300.bg-white 371.1x306.0 bg #ffffff r 24px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 4px 0px outline 1px auto #005fcc offset 1px | a.xs:w-300.bg-white 381.5x318.8 bg #ffffff r 24px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 4px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `r-tweet-default.png`, `r-tweet-hover.png`, `r-tweet-focus-visible.png`, `r-tweet-pressed.png`.

#### r-slide

Slide button. A carousel "slide next" button: 40px square bordered control, dark fill on hover.

Page: reviews. Selector: `button[aria-label="slide next"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 2px solid #000000 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #000000 | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 36 x 40, colour #000000 | = | = | = |
| Painted layers | button.cursor-pointer.hover:bg-black 40.0x40.0 border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 9999px | button.cursor-pointer.hover:bg-black 40.0x40.0 bg #000000 border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 9999px | = | button.cursor-pointer.hover:bg-black 40.0x40.0 bg #000000 border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `r-slide-default.png`, `r-slide-hover.png`, `r-slide-focus-visible.png`, `r-slide-pressed.png`.

### FAQ

#### f-h1

FAQ title. The "Frequently Asked Questions" heading.

Page: faq. Selector: `h1 on /faq`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 674.17 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Borel Regular 48px/72px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| How | at rest |

Crops: `f-h1-default.png`.

#### f-q

FAQ question. A question heading (static, not an accordion).

Page: faq. Selector: `h2 question`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 268.42 x 30 |
| Padding | 0px 12px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Circular Medium 20px/30px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `f-q-default.png`.

#### f-a

FAQ answer. An answer paragraph under a question.

Page: faq. Selector: `h3 answer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 586 x 97 |
| Padding | 0px 35px 16px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Circular Regular 18px/27px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | div: Circular Regular 18px/27px 400, #222222 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `f-a-default.png`.

#### f-cta

FAQ CTA. A bordered "Contact support" pill (btn-with-br-2-dark variant); measured never followed.

Page: faq. Selector: `a.bmc-btn Contact support`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 154.48 x 44 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Circular Bold 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | span: Circular Bold 16px/24px 400, #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 154.484px x 44px, absolute, bg #000000 @ 0, radius 40px | = | = | = |
| Painted layers | a::before.bmc-btn.btn-with-br-2-dark 154.484pxx44px border T:2px solid #222222 / R:2px solid #222222 / B:2px solid #222222 / L:2px solid #222222 r 40px | = | a.bmc-btn.btn-with-br-2-dark 154.5x44.0 r 40px outline 1px auto #005fcc offset 1px; a::before.bmc-btn.btn-with-br-2-dark 154.484pxx44px border T:2px solid #222222 / R:2px solid #222222 / B:2px solid #222222 / L:2px solid #222222 r 40px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `f-cta-default.png`, `f-cta-hover.png`, `f-cta-focus-visible.png`, `f-cta-pressed.png`.

### Footer

#### footer

Footer. The marketing footer bar (its own Vue component): the Apps/Resources/Legal drop-up triggers, socials and the legal line; the link lists live in the drop-up panels.

Page: home. Selector: `[data-v-35e7fb9e] root`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 144 |
| Padding | 48px 0px 70px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.font-cr-regular.flex-shrink-0: Circular Regular 16px/24px 400, #717171 |
| Transition | none |
| Icon | 12 x 9, colour #222222 |
| Painted layers | div.hidden.min-w-150 0.0x0.0 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 2.65546px 95px 0px; div.hidden.min-w-[220px] 0.0x0.0 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 2.65546px 95px 0px; div.bg-white.shadow-x-xsm 0.0x0.0 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 2.65546px 95px 0px; div.bg-white.shadow-x-xsm 0.0x0.0 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 2.65546px 95px 0px; div.hidden.min-w-[180px] 0.0x0.0 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 2.65546px 95px 0px |
| Ancestor paint | 1 up div.bg-floral-white.relative bg #faf8f0 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A legal link inside the opened footer drop-up panel.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 209.08 x 36 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | #222222 @ 0.05 | #222222 @ 0.05 | #222222 @ 0.05 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | 1px auto #005fcc offset 1px |
| Font | Circular Bold 16px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.visible.min-w-[180px] bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 2.65546px 95px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.block.px-12 209.1x36.0 bg #222222 @ 0.05 r 10px | a.block.px-12 209.1x36.0 bg #222222 @ 0.05 r 10px outline 1px auto #005fcc offset 1px | a.block.px-12 209.1x36.0 bg #222222 @ 0.05 r 10px outline 1px auto #005fcc offset 1px |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Social link. A social icon link in the footer.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 26 | 26.4 x 28.6 | = | 26.4 x 28.6 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | ui-sans-serif 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | all 0.1s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #000000 | 26.4 x 26.4, colour #000000 | = | 26.4 x 26.4, colour #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1.1, 0, 0, 1.1, 0, 0) | = | matrix(1.1, 0, 0, 1.1, 0, 0) |
| Painted layers | - | = | a.inline-block.icon-transition 24.0x26.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

#### footer-trigger

Footer trigger. The "Legal" drop-up trigger in the footer bar; opens the legal link list.

Page: home. Selector: `footer Legal trigger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 57.83 x 24 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Circular Medium 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #222222 | #777777 | - | #777777 |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 12 x 9, colour #222222 | 12 x 9, colour #777777 | - | 12 x 9, colour #777777 |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `footer-trigger-default.png`, `footer-trigger-hover.png`, `footer-trigger-pressed.png`.

#### footer-menu

Footer menu. The drop-up panel the Legal trigger opens (Terms of Use, Privacy Policy, Cookie Policy...).

Page: home. Selector: `footer .drop-up-or-down`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 225.08 x 268 |
| Padding | 8px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 2.65546px 95px 0px |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.block.px-12: Circular Bold 16px/20px 400, #222222 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Painted layers | div.visible.min-w-[180px] 225.1x268.0 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 2.65546px 95px 0px |
| How | at rest |

Crops: `footer-menu-default.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The header at 390: wordmark, Log-in link, Start-my-page pill and the burger.

Page: mobile. Selector: `#bmc-header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 65 |
| Padding | 14px 16px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.text-dark.btn-hover-bg: Circular Medium 14px/21px 400, #222222 |
| Transition | none |
| Icon | 0 x 0, colour #000000 |
| Painted layers | div.flex.justify-between 390.0x65.0 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a::before.text-dark.btn-hover-bg 100%x100% bg #000000 @ 0.05 r 40px; a::before.btn-hover-bg.w-108 100%x100% bg #000000 @ 0.05 r 40px; div::before.btn-hover-bg.cursor-pointer 100%x100% bg #000000 @ 0.05 r 40px; div.hidden.min-w-150 0.0x0.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.15 0px 0px 2px 0px, #000000 @ 0.04 0px 8px 40px 0px, #000000 @ 0.05 0px 2px 5px 0px; div::before.btn-hover-bg.cursor-pointer 100%x100% bg #000000 @ 0.05 r 40px |
| How | at rest |

Crops: none.

#### m-menu-button

Menu button. The burger that slides the full-screen menu in (translate-x-full -> translate-x-0).

Page: mobile. Selector: `#bmc-header div.cursor-pointer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 14 x 12 |
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
| Icon | 14 x 12, colour #000000 |
| Ancestor paint | 3 up div.flex.justify-between bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: none.

#### m-menu-open

Mobile menu, open. The full-screen white panel the burger slides in (FAQ, Wall of, iOS, Android, Start my page).

Page: mobile. Selector: `div[class*=translate] menu panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 16px 12px 72px 12px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Circular Medium 20px/30px 400, #222222 |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 16 x 16, colour #000000 |
| Painted layers | div.translate-x-0.h-full 390.0x844.0 bg #ffffff; a::before.text-dark.btn-hover-bg 56.3906pxx34px bg #000000 @ 0.05 r 40px; a::before.btn-hover-bg.mobile-nav-item 103.391pxx34px bg #000000 @ 0.05 r 40px; div.btn-bg.absolute 350.0x48.0 bg #ffdd00 r 9999px |
| Ancestor paint | 1 up div.flex.justify-between bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: none.

#### m-nav-item

Mobile nav item. A link inside the opened mobile menu.

Page: mobile. Selector: `a.mobile-nav-item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56.39 x 34 | = | = | = |
| Padding | 2px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | Circular Medium 20px/30px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | span: Circular Medium 20px/30px 400, #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 56.3906px x 34px, absolute, bg #000000 @ 0.05, radius 40px | = | = | = |
| Painted layers | a::before.text-dark.btn-hover-bg 56.3906pxx34px bg #000000 @ 0.05 r 40px | = | a.text-dark.btn-hover-bg 56.4x34.0 outline 1px auto #e59700 offset 1px; a::before.text-dark.btn-hover-bg 56.3906pxx34px bg #000000 @ 0.05 r 40px | = |
| Ancestor paint | 3 up div.flex.justify-between bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### m-hero

Mobile headline. The hero display at 390.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 326 x 110 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Circular Bold 48px/55px 400 |
| Letter spacing | -1.2px |
| Colour | #222222 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: none.

## Transitions declared in the readable stylesheets

buymeacoffee.com serves its Nuxt-marketing stylesheets same-origin while the creator page and login card load theirs from cdn.buymeacoffee.com (cross-origin, invisible to the CSSOM), so this list holds the transitions the readable sheets declare on each page — the creator app contributes none here; the per-state Transition rows above are computed values and cover every rule the page paints.

- creator: `opacity 150ms ease-in`, `opacity 250ms ease-out`

- home: `0.2s`, `background-color 0.1s ease-out`, `0.1s ease-in-out`, `0.4s`, `width 0.5s`, `opacity 1.5s`, `0.1s`, `opacity 0.5s`, `75ms ease-in-out`, `0.5s`, `0.5s cubic-bezier(0.2, 0.75, 0.28, 0.9)`, `1s cubic-bezier(0.2, 0.75, 0.28, 0.9)`

- login: none

- reviews: `0.2s`, `background-color 0.1s ease-out`, `0.1s ease-in-out`, `0.4s`, `width 0.5s`, `opacity 1.5s`, `0.1s`, `opacity 0.5s`, `75ms ease-in-out`, `0.5s cubic-bezier(0.2, 0.75, 0.28, 0.9)`, `0.8s cubic-bezier(0.2, 0.75, 0.28, 0.9)`, `1s cubic-bezier(0.2, 0.75, 0.28, 0.9)`
