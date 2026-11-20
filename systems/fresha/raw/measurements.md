# Component measurements

Computed styles read from www.fresha.com on 2026-11-16 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### shell-header

Top bar. The consumer app bar: logo left, Log in / For businesses / Menu / Get the app right, over the hero.

Page: home. Selector: `header chrome`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 72 |
| Padding | 12px 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 16px/18.4px 400 |
| Letter spacing | -0.1px |
| Colour | #0d0d0d |
| Text node | span.ta_inherit.textStyle_body.m.semibold: Roobert 16px/22px 600, #0d0d0d, ls -0.1px |
| Transition | none |
| Icon | 74.97 x 22, colour #0d0d0d |
| Painted layers | a::before.pos_relative.before:bx-s_border-box 74.9688pxx48px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; a::before.pos_relative.before:bx-s_border-box 86.4062pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 86.4x48.0 bg #131313 @ 0 border T:1px #ffffff @ 0 / R:1px #ffffff @ 0 / B:1px #ffffff @ 0 / L:1px #ffffff @ 0 r 999px; a::before.pos_relative.before:bx-s_border-box 153.609pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 153.6x48.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px; button.ring_none.pos_relative 109.6x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up div.pos_sticky.bg-c_transparent shadow #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `shell-header-default.png`.

#### shell-login-link

Log in link. Header link to the /user-flow chooser. Measured, never followed.

Page: home. Selector: `a:has-text("Log in")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 86.41 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Roobert 16px/18.4px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Text node | span.ta_inherit.textStyle_body.m.semibold: Roobert 16px/22px 600, #0d0d0d, ls -0.1px | = | = | = |
| Transition | max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 86.4062px x 48px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = | = | = |
| Painted layers | a::before.pos_relative.before:bx-s_border-box 86.4062pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 86.4x48.0 bg #131313 @ 0 border T:1px #ffffff @ 0 / R:1px #ffffff @ 0 / B:1px #ffffff @ 0 / L:1px #ffffff @ 0 r 999px | a::before.pos_relative.before:bx-s_border-box 86.4062pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 86.4x48.0 bg #131313 @ 0.04 border T:1px #ffffff @ 0 / R:1px #ffffff @ 0 / B:1px #ffffff @ 0 / L:1px #ffffff @ 0 r 999px | = | a::before.pos_relative.before:bx-s_border-box 86.4062pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 86.4x48.0 bg #131313 @ 0.08 border T:1px #ffffff @ 0 / R:1px #ffffff @ 0 / B:1px #ffffff @ 0 / L:1px #ffffff @ 0 r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `shell-login-link-default.png`, `shell-login-link-hover.png`, `shell-login-link-focus-visible.png`, `shell-login-link-pressed.png`.

#### shell-business-link

For businesses link. Header link to the B2B marketing app. Measured, never followed.

Page: home. Selector: `a:has-text("For businesses")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 153.61 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Roobert 16px/18.4px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Text node | span.ta_inherit.textStyle_body.m.semibold: Roobert 16px/22px 600, #0d0d0d, ls -0.1px | = | = | = |
| Transition | max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 153.609px x 48px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = | = | = |
| Painted layers | a::before.pos_relative.before:bx-s_border-box 153.609pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 153.6x48.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px | a::before.pos_relative.before:bx-s_border-box 153.609pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 153.6x48.0 bg #f5f5f5 border T:1px #bfbfbf / R:1px #bfbfbf / B:1px #bfbfbf / L:1px #bfbfbf r 999px | = | a::before.pos_relative.before:bx-s_border-box 153.609pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 147.5x46.1 bg #f2f2f2 border T:1px #acacac / R:1px #acacac / B:1px #acacac / L:1px #acacac r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `shell-business-link-default.png`, `shell-business-link-hover.png`, `shell-business-link-focus-visible.png`, `shell-business-link-pressed.png`.

#### shell-menu-button

Menu button. Header button that opens the consumer drawer (aria-haspopup).

Page: home. Selector: `button:has-text("Menu")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 109.61 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Roobert 16px/18.4px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Text node | span.ta_inherit.textStyle_body.m.semibold: Roobert 16px/22px 600, #0d0d0d, ls -0.1px | = | = | = |
| Transition | max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #0d0d0d | = | = | 23.04 x 23.04, colour #0d0d0d |
| ::before | 109.609px x 48px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = | = | = |
| Painted layers | button.ring_none.pos_relative 109.6x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 109.609pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 109.6x48.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px | button.ring_none.pos_relative 109.6x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 109.609pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 109.6x48.0 bg #f5f5f5 border T:1px #bfbfbf / R:1px #bfbfbf / B:1px #bfbfbf / L:1px #bfbfbf r 999px | = | button.ring_none.pos_relative 109.6x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 109.609pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 105.2x46.1 bg #f2f2f2 border T:1px #acacac / R:1px #acacac / B:1px #acacac / L:1px #acacac r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `shell-menu-button-default.png`, `shell-menu-button-hover.png`, `shell-menu-button-focus-visible.png`, `shell-menu-button-pressed.png`.

#### shell-getapp-button

Get the app button. Header button. Opens the app-download dialog on click — captured open where the dialog mounts.

Page: home. Selector: `button:has-text("Get the app")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 160.91 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Roobert 16px/18.4px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Text node | span.ta_inherit.textStyle_body.m.semibold: Roobert 16px/22px 600, #0d0d0d, ls -0.1px | = | = | = |
| Transition | max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #0d0d0d | = | = | 23.04 x 23.04, colour #0d0d0d |
| ::before | 160.906px x 48px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = | = | = |
| Painted layers | button.ring_none.pos_relative 160.9x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 160.906pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 160.9x48.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px | = | = | button.ring_none.pos_relative 160.9x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 160.906pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 154.5x46.1 bg #f2f2f2 border T:1px #acacac / R:1px #acacac / B:1px #acacac / L:1px #acacac r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `shell-getapp-button-default.png`, `shell-getapp-button-hover.png`, `shell-getapp-button-focus-visible.png`, `shell-getapp-button-pressed.png`.

#### footer

Footer. The site footer: link columns, app badges, region and legal links.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 310 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #f2f2f2 |
| Box shadow | none |
| Outline | none |
| Font | Roobert 16px/18.4px 400 |
| Letter spacing | -0.1px |
| Colour | #0d0d0d |
| Text node | span.ta_inherit.textStyle_body.m.semibold: Roobert 16px/22px 600, #0d0d0d, ls -0.1px |
| Transition | none |
| Icon | 74.97 x 22, colour #0d0d0d |
| Painted layers | footer.bg-c_background.neutralFaded 1440.0x310.0 bg #f2f2f2; a::before.pos_relative.before:bx-s_border-box 227pxx22px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; button.ring_none.pos_relative 184.9x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 184.906pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 184.9x48.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px; a::before.pos_relative.before:bx-s_border-box 50.3125pxx16px r 4px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px |
| How | at rest |

Crops: `footer-default.png`.

### Dialogs, menus and overlays

#### menu-drawer

Menu drawer. The consumer menu popover opened by the Menu button: "Log in or sign up", "Download the app", "Help and support", "English (US)", "For businesses". Opened by its own button, closed after measuring.

Page: home. Selector: `[data-m-mark="drawer"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 198 x 177 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 16px/18.4px 400 |
| Letter spacing | -0.1px |
| Colour | #0d0d0d |
| Text node | span.d_block.ov_hidden: Roobert 14px/20px 500, #6950f3, ls -0.1px |
| Transition | none |
| Icon | 20 x 20, colour #0d0d0d |
| Painted layers | li.menu-item-group.pos_relative 222.0x40.0 bg #131313 @ 0 r 8px outline 2px solid #000000 @ 0 offset 2px; li::before.menu-item-group.pos_relative 222pxx40px r 8px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; a.pos_absolute.before:bx-s_border-box 222.0x40.0 outline 2px solid #000000 @ 0 offset 0px; a::before.pos_absolute.before:bx-s_border-box 222pxx40px r 12px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; li.menu-item-group.pos_relative 222.0x40.0 bg #131313 @ 0 r 8px outline 2px solid #000000 @ 0 offset 2px; li::before.menu-item-group.pos_relative 222pxx40px r 8px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px |
| How | at rest |

Crops: `menu-drawer-default.png`.

#### menu-item

Menu drawer item. A row in the menu popover. Measured, never followed.

Page: home. Selector: `menu item`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 198 x 20 | - |
| Padding | 0px | - |
| Border | none | - |
| Radius | 0px | - |
| Background | transparent | - |
| Box shadow | none | - |
| Outline | none | - |
| Font | Roobert 14px/20px 500 | - |
| Letter spacing | -0.1px | - |
| Colour | #6950f3 | - |
| Transition | none | - |
| Cursor | pointer | - |
| How | at rest | - |
| Error | - | locator.hover: Timeout 5000ms exceeded. Call log:   - waiting for locator('[data-m-mark="drawer-signup"]').first().first()  |

Crops: `menu-item-default.png`.

#### search-suggestions

Search suggestions. The dropdown the treatment field opens on focus: suggestion rows for services and venues. Opened by focusing the field; Escape closes it; nothing is chosen.

Page: home. Selector: `[role="listbox"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 536 x 2049 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 16px/18.4px 400 |
| Letter spacing | -0.1px |
| Colour | #0d0d0d |
| Text node | span.ta_inherit.max-w-is_[200px]: Roobert 14px/20px 500, #ffffff, ls -0.1px |
| Transition | none |
| Icon | 20 x 20, colour #6950f3 |
| Painted layers | div.pos_sticky.inset-bs_0 600.0x81.0 bg #ffffff; div.w-is_100%.pos_relative 536.0x37.0 bg #ffffff; div.pos_absolute.pointer-events_none 64.0x36.0 image linear-gradient(to left, #000000 @ 0, #ffffff); li.pos_relative.before:bx-s_border-box 46.7x36.0 bg #0d0d0d r 999px outline 2px solid #000000 @ 0 offset 2px; li::before.pos_relative.before:bx-s_border-box 46.7031pxx36px border T:2px #0d0d0d / R:2px #0d0d0d / B:2px #0d0d0d / L:2px #0d0d0d r 999px shadow #ffffff 0px 0px 0px 2px inset; li.pos_relative.before:bx-s_border-box 111.0x36.0 r 999px shadow #131313 @ 0.1 0px 0px 0px 1px inset outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 2 up div.bg-c_background.page.bdr_xl bg #ffffff shadow #131313 @ 0.08 0px 2px 8px 0px, #131313 @ 0.12 0px 4px 20px 0px |
| How | at rest |

Crops: none.

#### nav-flyout

Nav flyout. The mega-menu under "Business types": a column of vertical links (Salon, Barber, Nails, Spa & sauna, Medspa, Massage …). Opened by its own button.

Page: business. Selector: `[role=menu] flyout`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 588 x 391 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #f5f5f5 |
| Box shadow | none |
| Outline | none |
| Font | Roobert 16px/24px 400 |
| Letter spacing | -0.1px |
| Colour | #141414 |
| Text node | h3.tw_pretty.pbe_50: Roobert 28px/36px 600, #141414, ls -0.2px |
| Transition | none |
| Icon | 37.48 x 11, colour #141414, fill #ffffff |
| Painted layers | div.d_grid.grid-tc_repeat(1,_minmax(0,_1fr)) 588.0x391.0 bg #f5f5f5 r 16px; div.d_flex.w-is_600 48.0x48.0 bg #141414 r 12px; a.textStyle_body.m.semibold.tw_nowrap 120.0x36.0 bg #141414 r 999px; a.textStyle_body.m.semibold.tw_nowrap 120.0x36.0 bg #141414 r 999px; div.h-bs_[50.5px].w-is_[82px] 82.0x50.5 bg #dbddff r 5.45px shadow #0d1619 @ 0.02 0px 0.627px 1.253px 0px, #0d1619 @ 0.16 0px 6.893px 15.666px 0px; div.h-bs_[60.11px].w-is_[82px] 82.0x60.1 bg #ffbf69 r 5.45px shadow #0d1619 @ 0.02 0px 0.627px 1.253px 0px, #0d1619 @ 0.16 0px 6.893px 15.666px 0px |
| How | at rest |

Crops: `nav-flyout-default.png`.

#### tooltip

Tooltip. The tooltip an info icon opens on hover: dark fill, small body copy. Opened by hovering its trigger, dismissed by moving off.

Page: pricing. Selector: `[role=tooltip]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 260 x 48 |
| Padding | 8px |
| Border | none |
| Radius | 8px |
| Background | #141414 |
| Box shadow | #000000 @ 0.05 0px 1px 2px 0px |
| Outline | none |
| Font | Roobert 12px/16px 400 |
| Letter spacing | -0.1px |
| Colour | #ffffff |
| Transition | none |
| Painted layers | div.z_50.us_none 260.0x48.0 bg #141414 r 8px shadow #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest |

Crops: `tooltip-default.png`.

### Consumer home

#### home-hero-title

Hero title. "Book local selfcare services" — the Roobert display size over the home hero.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 960 x 68 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 64px/68px 700 |
| Letter spacing | -0.2px |
| Colour | #0d0d0d |
| Transition | none |
| How | at rest |

Crops: `home-hero-title-default.png`.

#### carousel-button

Carousel arrow. The circular Prev/Next buttons on the recommended carousel.

Page: home. Selector: `button[aria-label] arrow`. States: default, pressed, hover, focus-visible.

| Property | default | pressed | hover | focus-visible |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Roobert 16px/18.4px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | opacity 0.1s cubic-bezier(0.85, 0, 0.15, 1) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, -24) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #0d0d0d | = | = | = |
| ::before | 48px x 48px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = | = | = |
| Painted layers | button.ring_none.pos_absolute 48.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_absolute 48pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 48.0x48.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px | button.ring_none.pos_absolute 48.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_absolute 48pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 46.1x46.1 bg #f2f2f2 border T:1px #acacac / R:1px #acacac / B:1px #acacac / L:1px #acacac r 999px | button.ring_none.pos_absolute 48.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_absolute 48pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 48.0x48.0 bg #f5f5f5 border T:1px #bfbfbf / R:1px #bfbfbf / B:1px #bfbfbf / L:1px #bfbfbf r 999px | = |
| How | at rest | CDP forcePseudoState :active:hover | mouse hover | element.focus() |
| Opacity | - | 0 | = | = |

Crops: `carousel-button-default.png`, `carousel-button-pressed.png`, `carousel-button-hover.png`, `carousel-button-focus-visible.png`.

### Search

#### search-treatment-field

Treatment field. The "All treatments" combobox of the hero search bar. Focused opens a suggestion list; nothing is submitted.

Page: home. Selector: `input/[role=combobox] treatments`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 274.53 x 22 | = |
| Padding | 1px 2px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = |
| Font | Roobert 14px/20px 500 | = |
| Letter spacing | -0.1px | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #0d0d0d, opacity 1 | = |
| Painted layers | input.ap_none.bg-c_transparent 274.5x22.0 outline 2px solid #000000 @ 0 offset 2px | = |
| How | at rest | clicked into the field |
| Ancestor paint | - | 2 up label.d_flex.ai_center bg #ffffff shadow #131313 @ 0.08 0px 2px 8px 0px, #131313 @ 0.12 0px 4px 20px 0px |

Crops: `search-treatment-field-default.png`, `search-treatment-field-focused.png`.

#### search-location-field

Location field. The "Current location" input of the hero search bar. Focused only — no query is sent.

Page: home. Selector: `input location`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 274.53 x 22 | = |
| Padding | 1px 2px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = |
| Font | Roobert 14px/20px 500 | = |
| Letter spacing | -0.1px | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #0d0d0d, opacity 1 | = |
| Painted layers | input.ap_none.bg-c_transparent 274.5x22.0 outline 2px solid #000000 @ 0 offset 2px | = |
| How | at rest | clicked into the field |
| Ancestor paint | - | 2 up label.d_flex.ai_center bg #ffffff shadow #131313 @ 0.08 0px 2px 8px 0px, #131313 @ 0.12 0px 4px 20px 0px |

Crops: `search-location-field-default.png`, `search-location-field-focused.png`.

#### search-when-control

When control. The "Any time" control of the hero search bar: opens the date/time popover. Focused state only in the field view; the open popover is measured where it mounts.

Page: home. Selector: `"Any time" control`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 274.53 x 22 | = |
| Padding | 1px 2px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = |
| Font | Roobert 14px/20px 500 | = |
| Letter spacing | -0.1px | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #0d0d0d, opacity 1 | = |
| Painted layers | input.ap_none.bg-c_transparent 274.5x22.0 outline 2px solid #000000 @ 0 offset 2px | = |
| How | at rest | clicked into the field |
| Ancestor paint | - | 2 up label.d_flex.ai_center bg #ffffff shadow #131313 @ 0.08 0px 2px 8px 0px, #131313 @ 0.12 0px 4px 20px 0px |

Crops: `search-when-control-default.png`, `search-when-control-focused.png`.

#### search-button

Search button. The hero search submit. Measured, never pressed — a press runs a search query.

Page: home. Selector: `button "Search"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 94.41 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Roobert 16px/18.4px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Text node | span.ta_inherit.textStyle_body.m.semibold: Roobert 16px/22px 600, #ffffff, ls -0.1px | = | = | = |
| Transition | max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 94.4062px x 48px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = | = | = |
| Painted layers | button.ring_none.pos_relative 94.4x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 94.4062pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 94.4x48.0 bg #0d0d0d border T:1px #0d0d0d / R:1px #0d0d0d / B:1px #0d0d0d / L:1px #0d0d0d r 999px | button.ring_none.pos_relative 94.4x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 94.4062pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 94.4x48.0 bg #262626 border T:1px #262626 / R:1px #262626 / B:1px #262626 / L:1px #262626 r 999px | = | button.ring_none.pos_relative 94.4x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 94.4062pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 90.6x46.1 bg #4a4a4a border T:1px #4a4a4a / R:1px #4a4a4a / B:1px #4a4a4a / L:1px #4a4a4a r 999px |
| Ancestor paint | 1 up form.bdr_[100px].ov_hidden bg #f2f2f2; 2 up div.bkdp_[saturate(4.5)_blur(10px)].bx-sh_[inset_0_0_0_6px_rgb(156_156_156_/_8%)] shadow #9c9c9c @ 0.08 0px 0px 0px 6px inset | = | 1 up form.bdr_[100px].ov_hidden bg #ffffff; 2 up div.bkdp_[saturate(4.5)_blur(10px)].bx-sh_[inset_0_0_0_6px_rgb(156_156_156_/_8%)] shadow #9c9c9c @ 0.08 0px 0px 0px 6px inset | 1 up form.bdr_[100px].ov_hidden bg #ffffff; 2 up div.bkdp_[saturate(4.5)_blur(10px)].bx-sh_[inset_0_0_0_6px_rgb(156_156_156_/_8%)] shadow #9c9c9c @ 0.08 0px 0px 0px 6px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-button-default.png`, `search-button-hover.png`, `search-button-focus-visible.png`, `search-button-pressed.png`.

### Cards

#### venue-card

Venue card. A recommended-venue card in the home carousel: photo, name, rating badge and score, address line and a tag ("Best in Class", "Featured"). The whole card is one link; measured, never followed.

Page: home. Selector: `a[href*="/a/"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 322 x 284.66 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Roobert 16px/18.4px 400 | = |
| Letter spacing | -0.1px | = |
| Colour | #0d0d0d | = |
| Text node | p.textStyle_body.m.semibold.flex-g_1: Roobert 16px/22px 600, #0d0d0d, ls -0.1px | = |
| Transition | none | = |
| Icon | 14 x 14, colour #ffc00a | = |
| Painted layers | a::before.pos_absolute.before:bx-s_border-box 322pxx284.656px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; button.ring_none.pos_relative 32.0x32.0 bg #131313 @ 0.33 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 32pxx32px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.bx-sh_[0_8px_40px_0_rgba(13,13,13,0.12),_0_0_0_0.5px_token(colors.background.shade300),_-1.25px_0_0_-0.75px_token(colors.background.shade300),_1.25px_0_0_-0.75px_token(colors.background.shade300)].d_inline-flex 177.2x24.0 image linear-gradient(#ffffff @ 0.7, #ffffff @ 0.7) r 999px shadow #0d0d0d @ 0.12 0px 8px 40px 0px, #131313 @ 0.1 0px 0px 0px 0.5px, #131313 @ 0.1 -1.25px 0px 0px -0.75px, #131313 @ 0.1 1.25px 0px 0px -0.75px; div::before.bx-sh_[0_8px_40px_0_rgba(13,13,13,0.12),_0_0_0_0.5px_token(colors.background.shade300),_-1.25px_0_0_-0.75px_token(colors.background.shade300),_1.25px_0_0_-0.75px_token(colors.background.shade300)].d_inline-flex 177.203pxx24px r 999px shadow #ffffff @ 0.15 0px 1px 0px 0px inset, #ffffff @ 0.1 0px -1px 0px 0px inset, #ffffff @ 0.2 0px 40px 10px -40px inset, #ffffff @ 0.2 0px -40px 10px -40px inset | = |
| How | at rest | mouse hover |

Crops: `venue-card-default.png`, `venue-card-hover.png`.

#### rating-badge

Rating badge. The score chip on a venue card ("4.9" with a star): badge fill plus the count beside it. The screen-reader "4.9 rating" copy is excluded.

Page: home. Selector: `rating chip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 18.7 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 13px/16px 600 |
| Letter spacing | -0.1px |
| Colour | #0d0d0d |
| Transition | none |
| How | at rest |

Crops: `rating-badge-default.png`.

#### business-type-card

Business-type card. A vertical-market card ("More info on …"): name plus icon. A link; measured, never followed.

Page: business. Selector: `a business type`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 378.66 x 378.67 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 18px | = |
| Background | transparent | = |
| Box shadow | none | #0d1619 @ 0.06 0px 4px 8px 0px, #0d1619 @ 0.06 0px 12px 20px 0px |
| Outline | none | = |
| Font | Roobert 16px/24px 400 | = |
| Letter spacing | -0.1px | = |
| Colour | #141414 | = |
| Text node | div.fs_17px.laptop:fs_28px: Roobert 28px/36px 700, #ffffff, ls -0.1px | = |
| Transition | box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 24 x 24, colour #141414 | = |
| Painted layers | div.pos_absolute.z_10 378.7x378.7 image linear-gradient(0deg, #000000 -5%, #000000 @ 0 20%) r 18px; button.textStyle_body.m.semibold.tw_nowrap 42.0x42.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px | a.pos_relative.justify-self_stretch 378.7x378.7 r 18px shadow #0d1619 @ 0.06 0px 4px 8px 0px, #0d1619 @ 0.06 0px 12px 20px 0px; div.pos_absolute.z_10 378.7x378.7 image linear-gradient(0deg, #000000 -5%, #000000 @ 0 20%) r 18px; button.textStyle_body.m.semibold.tw_nowrap 42.0x42.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px |
| How | at rest | mouse hover |

Crops: `business-type-card-default.png`, `business-type-card-hover.png`.

### Sign-in shell

#### back-button

Back button. The round "Go back" control every auth-shell page carries.

Page: userflow. Selector: `button "Go back"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Roobert 16px/18.4px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #0d0d0d | = | = | = |
| ::before | 48px x 48px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = | = | = |
| Painted layers | button.ring_none.pos_sticky 48.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_sticky 48pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 48.0x48.0 bg #131313 @ 0 border T:1px #ffffff @ 0 / R:1px #ffffff @ 0 / B:1px #ffffff @ 0 / L:1px #ffffff @ 0 r 999px | button.ring_none.pos_sticky 48.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_sticky 48pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 48.0x48.0 bg #131313 @ 0.04 border T:1px #ffffff @ 0 / R:1px #ffffff @ 0 / B:1px #ffffff @ 0 / L:1px #ffffff @ 0 r 999px | = | button.ring_none.pos_sticky 48.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_sticky 48pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 46.1x46.1 bg #131313 @ 0.08 border T:1px #ffffff @ 0 / R:1px #ffffff @ 0 / B:1px #ffffff @ 0 / L:1px #ffffff @ 0 r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `back-button-default.png`, `back-button-hover.png`, `back-button-focus-visible.png`, `back-button-pressed.png`.

#### chooser-card

Customer/professional card. One of the two chooser cards on /user-flow ("Fresha for customers", "Fresha for professionals"): title, description and chevron. A link to the auth shell; measured, never followed.

Page: userflow. Selector: `a:has-text("Fresha for customers")`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 368 x 42 | = | - |
| Padding | 0px | = | - |
| Border | none | = | - |
| Radius | 0px | = | - |
| Background | transparent | = | - |
| Box shadow | none | = | - |
| Outline | none | = | - |
| Font | Roobert 16px/18.4px 400 | = | - |
| Letter spacing | -0.1px | = | - |
| Colour | #0d0d0d | = | - |
| Text node | h3.ta_inherit.wb_normal: Roobert 16px/22px 500, #0d0d0d, ls -0.1px | = | - |
| Transition | none | = | - |
| Cursor | pointer | = | - |
| How | at rest | mouse hover | - |
| Skipped | - | = | focus failed: keyboard focus did not reach the element |

Crops: `chooser-card-default.png`, `chooser-card-hover.png`.

#### language-button

Language button. The "English (US)" locale picker on the chooser. Measured; not opened (opening it may navigate).

Page: userflow. Selector: `button:has-text("English")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 97.81 x 36 | = | = | = |
| Padding | 8px 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Roobert 16px/18.4px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #6950f3 | #5c4ace | = | #403591 |
| Text node | span.textStyle_link.s.medium: Roobert 14px/20px 500, #6950f3, ls -0.1px | span.textStyle_link.s.medium: Roobert 14px/20px 500, #5c4ace, ls -0.1px | = | span.textStyle_link.s.medium: Roobert 14px/20px 500, #403591, ls -0.1px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #6950f3 | 20 x 20, colour #5c4ace | = | 20 x 20, colour #403591 |
| ::before | 97.8125px x 36px, absolute, bg #000000 @ 0, radius 0px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = | = | = |
| Painted layers | button.ring_none.pos_relative 97.8x36.0 outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 97.8125pxx36px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `language-button-default.png`, `language-button-hover.png`, `language-button-focus-visible.png`, `language-button-pressed.png`.

#### auth-back

Auth back button.

Page: auth. Selector: `button back`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Roobert 16px/18.4px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #0d0d0d | = | = | = |
| ::before | 48px x 48px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = | = | = |
| Painted layers | button.ring_none.pos_sticky 48.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_sticky 48pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 48.0x48.0 bg #131313 @ 0 border T:1px #ffffff @ 0 / R:1px #ffffff @ 0 / B:1px #ffffff @ 0 / L:1px #ffffff @ 0 r 999px | button.ring_none.pos_sticky 48.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_sticky 48pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 48.0x48.0 bg #131313 @ 0.04 border T:1px #ffffff @ 0 / R:1px #ffffff @ 0 / B:1px #ffffff @ 0 / L:1px #ffffff @ 0 r 999px | = | button.ring_none.pos_sticky 48.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_sticky 48pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 46.1x46.1 bg #131313 @ 0.08 border T:1px #ffffff @ 0 / R:1px #ffffff @ 0 / B:1px #ffffff @ 0 / L:1px #ffffff @ 0 r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `auth-back-default.png`, `auth-back-hover.png`, `auth-back-focus-visible.png`, `auth-back-pressed.png`.

#### auth-continue

Continue button. The email submit — a press requests a verification code, so it is only measured.

Page: auth. Selector: `button "Continue"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 448 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Roobert 16px/18.4px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Text node | span.ta_inherit.textStyle_body.m.semibold: Roobert 16px/22px 600, #ffffff, ls -0.1px | = | = | = |
| Transition | max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 448px x 48px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = | = | = |
| Painted layers | button.ring_none.pos_relative 448.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 448pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 448.0x48.0 bg #0d0d0d border T:1px #0d0d0d / R:1px #0d0d0d / B:1px #0d0d0d / L:1px #0d0d0d r 999px | button.ring_none.pos_relative 448.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 448pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 448.0x48.0 bg #262626 border T:1px #262626 / R:1px #262626 / B:1px #262626 / L:1px #262626 r 999px | = | button.ring_none.pos_relative 448.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 448pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 430.1x46.1 bg #4a4a4a border T:1px #4a4a4a / R:1px #4a4a4a / B:1px #4a4a4a / L:1px #4a4a4a r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `auth-continue-default.png`, `auth-continue-hover.png`, `auth-continue-focus-visible.png`, `auth-continue-pressed.png`.

#### sso-button

SSO button. "Continue with Google" (the Apple and passkey rows share the style): a full-width outlined button with the provider mark. Never pressed — a press starts an OAuth flow.

Page: auth. Selector: `button:has-text("Continue with Google")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 448 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Roobert 16px/18.4px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Text node | span.textStyle_body.m.semibold: Roobert 16px/22px 600, #0d0d0d, ls -0.1px | = | = | = |
| Transition | max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 448px x 48px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = | = | = |
| Painted layers | button.ring_none.pos_relative 448.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 448pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_space-between 448.0x48.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px | button.ring_none.pos_relative 448.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 448pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_space-between 448.0x48.0 bg #f5f5f5 border T:1px #bfbfbf / R:1px #bfbfbf / B:1px #bfbfbf / L:1px #bfbfbf r 999px | = | button.ring_none.pos_relative 448.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 448pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_space-between 430.1x46.1 bg #f2f2f2 border T:1px #acacac / R:1px #acacac / B:1px #acacac / L:1px #acacac r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sso-button-default.png`, `sso-button-hover.png`, `sso-button-focus-visible.png`, `sso-button-pressed.png`.

#### passkey-button

Passkey button.

Page: auth. Selector: `button:has-text("passkey")`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 448 x 48 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 999px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = |
| Font | Roobert 16px/18.4px 400 | = |
| Letter spacing | -0.1px | = |
| Colour | #0d0d0d | = |
| Text node | span.ta_inherit.textStyle_body.m.semibold: Roobert 16px/22px 600, #0d0d0d, ls -0.1px | = |
| Transition | max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) | = |
| Cursor | pointer | = |
| Icon | 24 x 24, colour #0d0d0d | = |
| ::before | 448px x 48px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = |
| Painted layers | button.ring_none.pos_relative 448.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 448pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_space-between 448.0x48.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px | button.ring_none.pos_relative 448.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 448pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_space-between 448.0x48.0 bg #f5f5f5 border T:1px #bfbfbf / R:1px #bfbfbf / B:1px #bfbfbf / L:1px #bfbfbf r 999px |
| How | at rest | mouse hover |

Crops: `passkey-button-default.png`, `passkey-button-hover.png`.

#### auth-cross-link

Cross-over link. "Have a business account? Go to Fresha for professionals" — the link out to the partner sign-in. Measured, never followed.

Page: auth. Selector: `a:has-text("professionals")`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 198.02 x 16 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Roobert 14px/20px 500 | = |
| Letter spacing | -0.1px | = |
| Colour | #6950f3 | #5c4ace |
| Transition | none | = |
| Cursor | pointer | = |
| ::before | 198.016px x 16px, absolute, bg #000000 @ 0, radius 4px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = |
| Painted layers | a::before.pos_relative.before:bx-s_border-box 198.016pxx16px r 4px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = |
| How | at rest | mouse hover |

Crops: `auth-cross-link-default.png`, `auth-cross-link-hover.png`.

#### partner-continue

Partner continue button. The professional sign-in submit. Measured, never pressed.

Page: partner. Selector: `button submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 396 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Roobert 14px/16.1px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Text node | span.ta_inherit.textStyle_body.m.semibold: Roobert 17px/24px 600, #ffffff, ls -0.2px | = | = | = |
| Transition | max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.ring_none.pos_relative 396.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; div.d_inline-flex.jc_center 396.0x48.0 bg #0d0d0d border T:1px #0d0d0d / R:1px #0d0d0d / B:1px #0d0d0d / L:1px #0d0d0d r 999px | button.ring_none.pos_relative 396.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; div.d_inline-flex.jc_center 396.0x48.0 bg #262626 border T:1px #262626 / R:1px #262626 / B:1px #262626 / L:1px #262626 r 999px | button.ring_none.pos_relative 396.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 396pxx48px r 999px shadow #ffffff 0px 0px 0px 2px outline 2px solid #0d0d0d offset 2px; div.d_inline-flex.jc_center 396.0x48.0 bg #0d0d0d border T:1px #0d0d0d / R:1px #0d0d0d / B:1px #0d0d0d / L:1px #0d0d0d r 999px | button.ring_none.pos_relative 396.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; div.d_inline-flex.jc_center 380.2x46.1 bg #4a4a4a border T:1px #4a4a4a / R:1px #4a4a4a / B:1px #4a4a4a / L:1px #4a4a4a r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| ::before | - | = | 396px x 48px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff 0px 0px 0px 2px | = |

Crops: `partner-continue-default.png`, `partner-continue-hover.png`, `partner-continue-focus-visible.png`, `partner-continue-pressed.png`.

#### partner-sso

Partner SSO button.

Page: partner. Selector: `button Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 396 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Roobert 14px/16.1px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Text node | span.textStyle_body.m.semibold: Roobert 17px/24px 600, #0d0d0d, ls -0.2px | = | = | = |
| Transition | max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.ring_none.pos_relative 396.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; div.d_inline-flex.jc_space-between 396.0x48.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px | button.ring_none.pos_relative 396.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; div.d_inline-flex.jc_space-between 396.0x48.0 bg #f5f5f5 border T:1px #bfbfbf / R:1px #bfbfbf / B:1px #bfbfbf / L:1px #bfbfbf r 999px | button.ring_none.pos_relative 396.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 396pxx48px r 999px shadow #ffffff 0px 0px 0px 2px outline 2px solid #0d0d0d offset 2px; div.d_inline-flex.jc_space-between 396.0x48.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px | button.ring_none.pos_relative 396.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; div.d_inline-flex.jc_space-between 380.2x46.1 bg #f2f2f2 border T:1px #acacac / R:1px #acacac / B:1px #acacac / L:1px #acacac r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| ::before | - | = | 396px x 48px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff 0px 0px 0px 2px | = |

Crops: `partner-sso-default.png`, `partner-sso-hover.png`, `partner-sso-focus-visible.png`, `partner-sso-pressed.png`.

#### partner-cross-link

Partner cross link. The link sending customers back to the consumer sign-in. Measured, never followed.

Page: partner. Selector: `a customer`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 184.41 x 18 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Roobert 15px/20px 500 | = |
| Letter spacing | -0.1px | = |
| Colour | #6950f3 | #5c4ace |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `partner-cross-link-default.png`, `partner-cross-link-hover.png`.

### Form controls

#### auth-email-field

Email field. The auth shell's single text input: "We'll send you a verification code". Typed into then cleared; Continue is never pressed — no code is ever requested.

Page: auth. Selector: `input email`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 374 x 46 | = | = |
| Padding | 16px | = | = |
| Border | none | = | = |
| Radius | 12px | = | = |
| Background | #131313 @ 0 | = | = |
| Box shadow | none | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | Roobert 16px/22px 400 | = | = |
| Letter spacing | -0.1px | = | = |
| Colour | #0d0d0d | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #0d0d0d, opacity 1 | = | = |
| Painted layers | input.pos_relative.w-is_100% 374.0x46.0 bg #131313 @ 0 r 12px outline 2px solid #000000 @ 0 offset 2px | = | = |
| Ancestor paint | 1 up div.d_flex.flex-g_1 bg #ffffff | = | = |
| How | at rest | clicked into the field | typed "hello@example.com", then deleted; nothing sent |

Crops: `auth-email-field-default.png`, `auth-email-field-focused.png`, `auth-email-field-filled.png`.

#### partner-email-field

Partner email field. The professional sign-in's email input. Typed into then cleared; nothing is submitted.

Page: partner. Selector: `input[type="email"]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 394 x 46 | = | = |
| Padding | 16px | = | = |
| Border | none | = | = |
| Radius | 12px | = | = |
| Background | #131313 @ 0 | = | = |
| Box shadow | none | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | Roobert 15px/20px 400 | = | = |
| Letter spacing | -0.1px | = | = |
| Colour | #0d0d0d | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #0d0d0d, opacity 1 | = | = |
| Painted layers | input.pos_relative.w-is_100% 394.0x46.0 bg #131313 @ 0 r 12px outline 2px solid #000000 @ 0 offset 2px | = | = |
| Ancestor paint | 1 up div.d_flex.flex-g_1 bg #ffffff | = | = |
| How | at rest | clicked into the field | typed "haircut", then deleted; nothing sent |

Crops: `partner-email-field-default.png`, `partner-email-field-focused.png`, `partner-email-field-filled.png`.

#### lp-sort-select

Sort select. The "Sort by" native select over the results list.

Page: lp. Selector: `select`. States: .

Not found on the page at capture time.

#### partner-decoy-password

Hidden password input. An off-viewport input[type=password] (x≈-1278) in the partner sign-in form — a browser-autocomplete decoy, not a painted control. The real flow is email + verification code.

Page: partner. Selector: `input[type="password"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 183 x 22.09 |
| Padding | 1px 2px |
| Border | 2px inset #767676 |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Roobert 14px/16.1px 400 |
| Letter spacing | -0.1px |
| Colour | #000000 |
| Transition | none |
| Cursor | text |
| Placeholder | #000000, opacity 1 |
| Painted layers | input 183.0x22.1 bg #ffffff border T:2px #767676 / R:2px #767676 / B:2px #767676 / L:2px #767676 |
| How | at rest |

Crops: none.

### Venue page

#### breadcrumb

Breadcrumb. The category/location breadcrumb over the venue title.

Page: venue. Selector: `nav[aria-label*=breadcrumb]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1376 x 36 |
| Padding | 0px 0px 16px 0px |
| Gap | 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 16px/18.4px 400 |
| Letter spacing | -0.1px |
| Colour | #0d0d0d |
| Text node | a.pos_relative.before:bx-s_border-box: Roobert 14px/20px 400, #767676, ls -0.1px |
| Transition | none |
| Painted layers | a::before.pos_relative.before:bx-s_border-box 38.6094pxx16px r 4px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; a::before.pos_relative.before:bx-s_border-box 70.9062pxx16px r 4px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; a::before.pos_relative.before:bx-s_border-box 67.1094pxx16px r 4px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; a::before.pos_relative.before:bx-s_border-box 67.1094pxx16px r 4px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; a::before.pos_relative.before:bx-s_border-box 70.8125pxx16px r 4px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; a::before.pos_relative.before:bx-s_border-box 109.312pxx16px r 4px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px |
| How | at rest |

Crops: `breadcrumb-default.png`.

#### venue-tab

Venue section tab. The sticky section nav (Services / Team / Reviews / About / Photos) — anchor links that scroll the page. Measured, never followed.

Page: venue. Selector: `nav a`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 48.41 x 52 | = |
| Padding | 0px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 2px | = |
| Background | #131313 @ 0 | = |
| Box shadow | none | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = |
| Font | Roobert 16px/18.4px 400 | = |
| Letter spacing | -0.1px | = |
| Colour | #0d0d0d | = |
| Text node | span.ta_inherit.max-w-is_[200px]: Roobert 14px/20px 500, #0d0d0d, ls -0.1px | = |
| Transition | none | = |
| Cursor | pointer | = |
| ::before | 64.4062px x 48px, absolute, bg #000000 @ 0, radius 8px, shadow #ffffff 0px 0px 0px 2px inset | = |
| ::after | 48.4062px x 4px, absolute, bg #0d0d0d, radius 4px 4px 0px 0px | = |
| Painted layers | li.pos_relative.before:bx-s_border-box 48.4x52.0 bg #131313 @ 0 r 2px outline 2px solid #000000 @ 0 offset 2px; li::before.pos_relative.before:bx-s_border-box 64.4062pxx48px border T:2px #0d0d0d / R:2px #0d0d0d / B:2px #0d0d0d / L:2px #0d0d0d r 8px shadow #ffffff 0px 0px 0px 2px inset; li::after.pos_relative.before:bx-s_border-box 48.4062pxx4px bg #0d0d0d r 4px 4px 0px 0px | = |
| How | at rest | Shift+Tab, Tab |

Crops: `venue-tab-default.png`, `venue-tab-focus-visible.png`.

#### book-now

Book now button. The venue page's primary CTA — the primary button style. Never pressed: a press starts the booking wizard.

Page: venue. Selector: `button "Book now"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 388 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Roobert 16px/18.4px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Text node | span.ta_inherit.textStyle_body.m.semibold: Roobert 16px/22px 600, #ffffff, ls -0.1px | = | = | = |
| Transition | max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 388px x 48px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = | = | = |
| Painted layers | a::before.pos_relative.before:bx-s_border-box 388pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 388.0x48.0 bg #0d0d0d border T:1px #0d0d0d / R:1px #0d0d0d / B:1px #0d0d0d / L:1px #0d0d0d r 999px | a::before.pos_relative.before:bx-s_border-box 388pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 388.0x48.0 bg #262626 border T:1px #262626 / R:1px #262626 / B:1px #262626 / L:1px #262626 r 999px | = | a::before.pos_relative.before:bx-s_border-box 388pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 372.5x46.1 bg #4a4a4a border T:1px #4a4a4a / R:1px #4a4a4a / B:1px #4a4a4a / L:1px #4a4a4a r 999px |
| Ancestor paint | 2 up div.trs-prop_box-shadow,_transform.trs-dur_short.s bg #ffffff shadow #131313 @ 0.08 0px 4px 12px 0px, #131313 @ 0.02 0px 2px 6px 2px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `book-now-default.png`, `book-now-hover.png`, `book-now-focus-visible.png`, `book-now-pressed.png`.

#### gallery-button

Gallery button. "See all images" over the photo grid. Measured only — opening it navigates to the gallery.

Page: venue. Selector: `button "See all images"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 123.61 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Roobert 16px/18.4px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Text node | span.ta_inherit.textStyle_body.s.medium: Roobert 14px/20px 500, #0d0d0d, ls -0.1px | = | = | = |
| Transition | max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 123.609px x 36px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = | = | = |
| ::after | 135.609px x 48px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.ring_none.pos_absolute 123.6x36.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_absolute 123.609pxx36px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 123.6x36.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px | button.ring_none.pos_absolute 123.6x36.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_absolute 123.609pxx36px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 123.6x36.0 bg #f5f5f5 border T:1px #bfbfbf / R:1px #bfbfbf / B:1px #bfbfbf / L:1px #bfbfbf r 999px | = | button.ring_none.pos_absolute 123.6x36.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_absolute 123.609pxx36px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 118.7x34.6 bg #f2f2f2 border T:1px #acacac / R:1px #acacac / B:1px #acacac / L:1px #acacac r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `gallery-button-default.png`, `gallery-button-hover.png`, `gallery-button-focus-visible.png`, `gallery-button-pressed.png`.

#### venue-title

Venue title. The venue name heading.

Page: venue. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1248 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 48px/52px 700 |
| Letter spacing | -0.2px |
| Colour | #0d0d0d |
| Transition | none |
| How | at rest |

Crops: `venue-title-default.png`.

#### service-row

Service row. A bookable service line: name, duration, price and a Select/Book control. Measured, never booked.

Page: venue. Selector: `li service row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 836 x 74 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Roobert 16px/18.4px 400 | = |
| Letter spacing | -0.1px | = |
| Colour | #0d0d0d | = |
| Text node | h3.ta_inherit.wb_normal: Roobert 16px/22px 500, #0d0d0d, ls -0.1px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | button.ring_none.pos_relative 65.6x36.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 65.6094pxx36px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 65.6x36.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px | = |
| Ancestor paint | 1 up div.li-s_none.c_foreground.neutral bg #ffffff shadow #e5e5e5 0px 0px 0px 1px inset | = |
| How | at rest | mouse hover |

Crops: `service-row-default.png`, `service-row-hover.png`.

#### service-book-button

Service select button. The per-service select control. Never pressed.

Page: venue. Selector: `button "Select"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 65.61 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Roobert 16px/18.4px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Text node | span.ta_inherit.textStyle_body.s.medium: Roobert 14px/20px 500, #0d0d0d, ls -0.1px | = | = | = |
| Transition | max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 65.6094px x 36px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = | = | = |
| Painted layers | button.ring_none.pos_relative 65.6x36.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 65.6094pxx36px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 65.6x36.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px | button.ring_none.pos_relative 65.6x36.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 65.6094pxx36px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 65.6x36.0 bg #f5f5f5 border T:1px #bfbfbf / R:1px #bfbfbf / B:1px #bfbfbf / L:1px #bfbfbf r 999px | = | button.ring_none.pos_relative 65.6x36.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 65.6094pxx36px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 63.0x34.6 bg #f2f2f2 border T:1px #acacac / R:1px #acacac / B:1px #acacac / L:1px #acacac r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `service-book-button-default.png`, `service-book-button-hover.png`, `service-book-button-focus-visible.png`, `service-book-button-pressed.png`.

#### review-card

Review card. A venue review: star row, comment text, service and staff line, date.

Page: venue. Selector: `article review`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 418 x 170 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 16px/18.4px 400 |
| Letter spacing | -0.1px |
| Colour | #0d0d0d |
| Text node | span.c_foreground.accent.textStyle_header.s.semibold: Roobert 22px/28px 600, #6950f3, ls -0.2px |
| Transition | none |
| Icon | 14 x 14, colour #ffc00a |
| Painted layers | div.d_inline-block.pos_relative 64.0x64.0 bg #f0f0ff border T:1px #f0f0ff / R:1px #f0f0ff / B:1px #f0f0ff / L:1px #f0f0ff r 999px; button.ring_none.pos_relative 23.5x16.0 r 4px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 23.5156pxx16px r 4px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px |
| How | at rest |

Crops: `review-card-default.png`.

#### hours-table

Opening times. The "Opening times" week schedule in the About section — green dot per open day, grey for closed.

Page: venue. Selector: `opening-times block`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 418 x 250 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 16px/18.4px 400 |
| Letter spacing | -0.1px |
| Colour | #0d0d0d |
| Text node | h3.textStyle_header.xs.semibold.tablet:textStyle_header.m.semibold: Roobert 24px/32px 600, #0d0d0d, ls -0.2px |
| Transition | none |
| Painted layers | span.as_center.bdr_rounded 13.0x13.0 bg #78d240 r 999px; span.as_center.bdr_rounded 13.0x13.0 bg #bfbfbf r 999px; span.as_center.bdr_rounded 13.0x13.0 bg #78d240 r 999px; span.as_center.bdr_rounded 13.0x13.0 bg #78d240 r 999px; span.as_center.bdr_rounded 13.0x13.0 bg #78d240 r 999px; span.as_center.bdr_rounded 13.0x13.0 bg #78d240 r 999px |
| How | at rest |

Crops: `hours-table-default.png`.

#### staff-avatar

Staff avatar. A Team circle: photo, name, "Top stylist" label and rating badge.

Page: venue. Selector: `staff card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 120 x 180 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = |
| Font | Roobert 16px/18.4px 400 | = |
| Letter spacing | -0.1px | = |
| Colour | #0d0d0d | = |
| Text node | span.ta_inherit.c_foreground.neutral: Roobert 14px/20px 600, #0d0d0d, ls -0.1px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #ffc00a | = |
| ::before | 120px x 180px, absolute, bg #000000 @ 0, radius 8px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = |
| Painted layers | button.ring_none.pos_relative 120.0x180.0 r 8px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 120pxx180px r 8px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-block.pos_relative 120.0x120.0 bg #f0f0ff border T:1px #f0f0ff / R:1px #f0f0ff / B:1px #f0f0ff / L:1px #f0f0ff r 999px; div.d_inline-flex.jc_center 58.7x30.0 bg #ffffff border T:1px #dbddff / R:1px #dbddff / B:1px #dbddff / L:1px #dbddff r 999px | button.ring_none.pos_relative 120.0x180.0 r 8px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 120pxx180px r 8px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-block.pos_relative 120.0x120.0 bg #dbddff border T:1px #dbddff / R:1px #dbddff / B:1px #dbddff / L:1px #dbddff r 999px; div.d_inline-flex.jc_center 58.7x30.0 bg #ffffff border T:1px #dbddff / R:1px #dbddff / B:1px #dbddff / L:1px #dbddff r 999px |
| How | at rest | mouse hover |

Crops: `staff-avatar-default.png`, `staff-avatar-hover.png`.

#### review-score

Review score. The big "5.0 Best in Class" review block: display-size score with trophy badges.

Page: venue. Selector: `review score`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 40.7 x 20 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 16px/18.4px 400 |
| Letter spacing | -0.1px |
| Colour | #0d0d0d |
| Text node | span.ta_inherit.c_foreground.neutral: Roobert 14px/20px 600, #0d0d0d, ls -0.1px |
| Transition | none |
| Cursor | pointer |
| Icon | 16 x 16, colour #ffc00a |
| How | at rest |

Crops: `review-score-default.png`.

### Booking wizard

#### booking-header

Booking header. The wizard chrome: back arrow, the "Services › Professional › Time › Confirm" step trail and a close control.

Page: booking. Selector: `wizard chrome`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 72 |
| Padding | 0px 32px |
| Gap | 48px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 16px/18.4px 400 |
| Letter spacing | -0.1px |
| Colour | #0d0d0d |
| Text node | span.w-is_100%.max-w-is_100%: Roobert 19px/24px 600, #0d0d0d, ls -0.2px |
| Transition | none |
| Icon | 0 x 0, colour #0d0d0d |
| Painted layers | button.ring_none.pos_relative 48.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 48pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 48.0x48.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px; button.ring_none.pos_relative 48.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 48pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 48.0x48.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px |
| Ancestor paint | 1 up div.d_flex.flex-d_column bg #f5f5f5 |
| How | at rest |

Crops: `booking-header-default.png`.

#### booking-step

Wizard step. A step label in the "Services / Professional / Time / Confirm" trail — the current step emphasised.

Page: booking. Selector: `step label`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 82.2 x 20 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 14px/20px 500 |
| Letter spacing | -0.1px |
| Colour | #0d0d0d |
| Text node | span: Roobert 14px/20px 500, #0d0d0d, ls -0.1px |
| Transition | none |
| Icon | 0 x 0, colour #0d0d0d |
| How | at rest |

Crops: `booking-step-default.png`.

#### booking-service-row

Booking service row. A selectable service card: name, duration, notes and price, with a round "+" add control. Adding only marks the service in the local cart; nothing is booked.

Page: booking. Selector: `li booking service`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 596 x 124 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Roobert 16px/18.4px 400 | = |
| Letter spacing | -0.1px | = |
| Colour | #0d0d0d | = |
| Text node | h3.textStyle_body.m.medium.mbe_25: Roobert 16px/22px 500, #0d0d0d, ls -0.1px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #0d0d0d | = |
| Painted layers | button.ring_none.pos_relative 36.0x36.0 bg #ffffff border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 999px shadow #131313 @ 0.12 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px | = |
| Ancestor paint | 3 up div.li-s_none.c_foreground.neutral bg #ffffff shadow #e5e5e5 0px 0px 0px 1px inset | = |
| How | at rest | mouse hover |

Crops: `booking-service-row-default.png`, `booking-service-row-hover.png`.

#### booking-add-button

Add-service button. The round "+" that selects a service for the cart. Its pressed state is captured for real: one press adds the service, then it is removed again — the wizard never advances.

Page: booking. Selector: `button "+"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #e5e5e5 | 1px solid #d3d3d3 | = | 1px solid #bfbfbf |
| Radius | 999px | = | = | = |
| Background | #ffffff | #f5f5f5 | = | #f2f2f2 |
| Box shadow | #131313 @ 0.12 0px 2px 4px 0px | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Roobert 16px/18.4px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #0d0d0d | = | = | = |
| Painted layers | button.ring_none.pos_relative 36.0x36.0 bg #ffffff border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 999px shadow #131313 @ 0.12 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px | button.ring_none.pos_relative 36.0x36.0 bg #f5f5f5 border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px shadow #131313 @ 0.12 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px | = | button.ring_none.pos_relative 36.0x36.0 bg #f2f2f2 border T:1px #bfbfbf / R:1px #bfbfbf / B:1px #bfbfbf / L:1px #bfbfbf r 999px shadow #131313 @ 0.12 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `booking-add-button-default.png`, `booking-add-button-hover.png`, `booking-add-button-focus-visible.png`, `booking-add-button-pressed.png`.

#### booking-category-pill

Category pill. The service-category chips under "Select services" (Featured, Promotion, Set menu, CUT & TRIM …) — the active one is solid.

Page: booking. Selector: `category pill`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 91.2 x 36 | = |
| Padding | 0px 16px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 999px | = |
| Background | #0d0d0d | = |
| Box shadow | none | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = |
| Font | Roobert 16px/18.4px 400 | = |
| Letter spacing | -0.1px | = |
| Colour | #ffffff | = |
| Text node | span.ta_inherit.max-w-is_[200px]: Roobert 14px/20px 500, #ffffff, ls -0.1px | = |
| Transition | none | = |
| Cursor | pointer | = |
| ::before | 91.2031px x 36px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff 0px 0px 0px 2px inset | = |
| Painted layers | li.pos_relative.before:bx-s_border-box 91.2x36.0 bg #0d0d0d r 999px outline 2px solid #000000 @ 0 offset 2px; li::before.pos_relative.before:bx-s_border-box 91.2031pxx36px border T:2px #0d0d0d / R:2px #0d0d0d / B:2px #0d0d0d / L:2px #0d0d0d r 999px shadow #ffffff 0px 0px 0px 2px inset | = |
| How | at rest | mouse hover |

Crops: `booking-category-pill-default.png`, `booking-category-pill-hover.png`.

#### booking-cart

Cart summary. The right-hand booking summary: venue card (photo, rating, address), the selected-services list, Total and the step button.

Page: booking. Selector: `aside cart`. States: default, service-added.

| Property | default | service-added |
|---|---|---|
| Size (w x h) | 444 x 756 | = |
| Padding | 0px 32px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Roobert 16px/18.4px 400 | = |
| Letter spacing | -0.1px | = |
| Colour | #0d0d0d | = |
| Text node | p.textStyle_body.m.semibold: Roobert 16px/22px 600, #0d0d0d, ls -0.1px | = |
| Transition | none | = |
| Icon | 16 x 16, colour #ffc00a | = |
| Painted layers | div.pos_sticky.z_1 380.0x98.0 bg #ffffff; a::before.pos_relative.before:bx-s_border-box 64pxx64px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.pos_relative.d_flex 64.0x64.0 bg #ffffff border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 8px; hr.bd_none.m_0 380.0x1.0 bg #0d0d0d; div.pos_sticky.inset-be_[84px] 380.0x53.0 bg #ffffff; hr.bd_none.m_0 380.0x1.0 bg #0d0d0d | div.pos_sticky.z_1 380.0x98.0 bg #ffffff; a::before.pos_relative.before:bx-s_border-box 64pxx64px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.pos_relative.d_flex 64.0x64.0 bg #ffffff border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 8px; hr.bd_none.m_0 380.0x1.0 bg #0d0d0d; div.li-s_none.c_foreground.neutral 380.0x42.0 bg #131313 @ 0 r 16px shadow #ffffff @ 0 0px 0px 0px 0px inset; div.pos_sticky.inset-be_[84px] 380.0x53.0 bg #ffffff |
| How | at rest | one service added by its own "+", then removed; the wizard never advanced |

Crops: `booking-cart-default.png`, `booking-cart-service-added.png`.

#### booking-continue

Continue button. The wizard's step button — grey while the cart is empty, dark once a service is selected. Measured, never pressed: a press advances to "Professional". The wizard never goes past step 1 in this capture.

Page: booking. Selector: `button "Continue"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 380 x 48 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 999px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | - | = |
| Font | Roobert 16px/18.4px 400 | = | - | = |
| Letter spacing | -0.1px | = | - | = |
| Colour | #0d0d0d | = | - | = |
| Text node | span.ta_inherit.textStyle_body.m.semibold: Roobert 16px/22px 600, #ffffff, ls -0.1px | = | - | = |
| Transition | max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 0 x 0, colour #ffffff | = | - | = |
| ::before | 380px x 48px, absolute, bg #000000 @ 0, radius 999px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = | - | = |
| Painted layers | button.ring_none.pos_relative 380.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 380pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 380.0x48.0 bg #0d0d0d border T:1px #0d0d0d / R:1px #0d0d0d / B:1px #0d0d0d / L:1px #0d0d0d r 999px | = | - | button.ring_none.pos_relative 380.0x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 380pxx48px r 999px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.d_inline-flex.jc_center 364.8x46.1 bg #4a4a4a border T:1px #4a4a4a / R:1px #4a4a4a / B:1px #4a4a4a / L:1px #4a4a4a r 999px |
| Ancestor paint | 1 up div.d_flex.pos_sticky bg #ffffff | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `booking-continue-default.png`, `booking-continue-hover.png`, `booking-continue-pressed.png`.

### For-business marketing

#### b2b-header

B2B top bar. The marketing app bar shared by /for-business, /pricing, /blog and /careers: product logo, Business types / Features flyouts, Marketplace, Pricing, Help, Blog, "Try for free".

Page: pricing. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Backdrop filter | blur(0px) |
| Outline | none |
| Font | Roobert 16px/24px 400 |
| Letter spacing | -0.1px |
| Colour | #141414 |
| Text node | button.textStyle_body.m.semibold.tw_nowrap: Roobert 17px/24px 600, #141414, ls -0.2px |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 75 x 22, colour #141414 |
| Painted layers | div.pos_absolute.inset-s_200 0.0x0.0 bg #ffffff r 24px shadow #0d1619 @ 0.16 0px 8px 32px 0px; div.pos_absolute.inset-s_200 0.0x0.0 bg #ffffff r 24px shadow #0d1619 @ 0.16 0px 8px 32px 0px; a.textStyle_body.m.semibold.tw_nowrap 171.8x48.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px; a.textStyle_body.m.semibold.tw_nowrap 101.6x48.0 bg #141414 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 999px; button.textStyle_body.m.semibold.tw_nowrap 117.2x48.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px; a.textStyle_body.s.medium.tw_nowrap 0.0x0.0 bg #141414 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 999px |
| Ancestor paint | 1 up div.scrs-t_[y_mandatory].bg-c_background.base bg #ffffff |
| How | at rest |

Crops: `b2b-header-default.png`.

#### nav-flyout-button

Nav flyout button. "Business types" and "Features" in the marketing nav — each opens a mega-menu flyout on click/hover.

Page: business. Selector: `button nav`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 160.2 x 48 | = | = |
| Padding | 0px 20px | = | = |
| Border | none | = | = |
| Radius | 999px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px |
| Font | Roobert 17px/24px 600 | = | = |
| Letter spacing | -0.2px | = | = |
| Colour | #141414 | #6950f3 | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0, 0.55, 0.45, 1) | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | button.textStyle_body.m.semibold.tw_nowrap 160.2x48.0 r 999px outline 2px solid #000000 @ 0 offset 2px |

Crops: `nav-flyout-button-default.png`, `nav-flyout-button-hover.png`, `nav-flyout-button-focus-visible.png`.

#### b2b-hero-title

Marketing hero title. The /for-business display heading.

Page: business. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1028 x 156 |
| Padding | 80px 0px 16px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 56px/60px 700 |
| Letter spacing | -0.1px |
| Colour | #141414 |
| Transition | none |
| How | at rest |

Crops: `b2b-hero-title-default.png`.

#### b2b-cta

Marketing CTA. The primary marketing button. Measured, never pressed.

Page: business. Selector: `button CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 180.02 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | #141414 | #2f2f2f | = | #2f2f2f |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Roobert 17px/24px 600 | = | = | = |
| Letter spacing | -0.2px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | transform 0.2s cubic-bezier(0, 0.55, 0.45, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.textStyle_body.m.semibold.tw_nowrap 180.0x48.0 bg #141414 r 999px | a.textStyle_body.m.semibold.tw_nowrap 180.0x48.0 bg #2f2f2f r 999px | a.textStyle_body.m.semibold.tw_nowrap 180.0x48.0 bg #141414 r 999px outline 2px solid #000000 @ 0 offset 2px | a.textStyle_body.m.semibold.tw_nowrap 180.0x48.0 bg #2f2f2f r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 0) |

Crops: `b2b-cta-default.png`, `b2b-cta-hover.png`, `b2b-cta-focus-visible.png`, `b2b-cta-pressed.png`.

#### watch-button

Watch button. "Watch an overview" — the secondary media button.

Page: business. Selector: `button Watch`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 227.61 x 48 | = | = | 218.51 x 46.08 |
| Padding | 0px 24px | = | = | = |
| Border | 1px solid #d3d3d3 | 1px solid #bfbfbf | = | 1px solid #acacac |
| Radius | 999px | = | = | = |
| Background | #ffffff | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Roobert 17px/24px 600 | = | = | = |
| Letter spacing | -0.2px | = | = | = |
| Colour | #141414 | = | = | = |
| Transition | transform 0.2s cubic-bezier(0, 0.55, 0.45, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #141414 | = | = | 19.2 x 19.2, colour #141414 |
| Painted layers | button.textStyle_body.m.semibold.tw_nowrap 227.6x48.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px | button.textStyle_body.m.semibold.tw_nowrap 227.6x48.0 bg #f5f5f5 border T:1px #bfbfbf / R:1px #bfbfbf / B:1px #bfbfbf / L:1px #bfbfbf r 999px | button.textStyle_body.m.semibold.tw_nowrap 227.6x48.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px outline 2px solid #000000 @ 0 offset 2px | button.textStyle_body.m.semibold.tw_nowrap 218.5x46.1 bg #f5f5f5 border T:1px #acacac / R:1px #acacac / B:1px #acacac / L:1px #acacac r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.96, 0, 0, 0.96, 0, 0) |

Crops: `watch-button-default.png`, `watch-button-hover.png`, `watch-button-focus-visible.png`, `watch-button-pressed.png`.

#### stat

Stat. A proof-point figure in the marketing stats row.

Page: business. Selector: `stat`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 193.02 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 48px/52px 700 |
| Letter spacing | -0.1px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `stat-default.png`.

### Pricing

#### plan-card

Plan card. A pricing plan column (Independent / Team / Enterprise): plan name, monthly price, "7 day trial" badge, feature list and its CTA.

Page: pricing. Selector: `article plan`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 277 x 368.5 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Roobert 16px/24px 400 | = |
| Letter spacing | -0.1px | = |
| Colour | #141414 | = |
| Text node | h3.textStyle_header.m.semibold: Roobert 24px/32px 600, #141414, ls -0.2px | = |
| Transition | none | = |
| Painted layers | div.min-w-is_0.trunc_true 98.9x30.0 bg #f0f0ff border T:1px #dbddff / R:1px #dbddff / B:1px #dbddff / L:1px #dbddff r 999px | = |
| How | at rest | mouse hover |

Crops: `plan-card-default.png`, `plan-card-hover.png`.

#### plan-price

Plan price. The price display inside a plan card (amount + period + commission line).

Page: pricing. Selector: `price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 277 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 40px/44px 700 |
| Letter spacing | -0.1px |
| Colour | #141414 |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. The plan card's call to action. Measured, never pressed: a press starts sign-up.

Page: pricing. Selector: `button CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 151.41 x 48 | = | = | 145.35 x 46.08 |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | #141414 | #2f2f2f | = | #2f2f2f |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Roobert 17px/24px 600 | = | = | = |
| Letter spacing | -0.2px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.min-w-is_0.trunc_true: Roobert 17px/24px 600, #ffffff, ls -0.2px | = | = | = |
| Transition | transform 0.2s cubic-bezier(0, 0.55, 0.45, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.textStyle_body.m.semibold.tw_nowrap 151.4x48.0 bg #141414 r 999px | button.textStyle_body.m.semibold.tw_nowrap 151.4x48.0 bg #2f2f2f r 999px | button.textStyle_body.m.semibold.tw_nowrap 151.4x48.0 bg #141414 r 999px outline 2px solid #000000 @ 0 offset 2px | button.textStyle_body.m.semibold.tw_nowrap 145.4x46.1 bg #2f2f2f r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.96, 0, 0, 0.96, 0, 0) |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### feature-row

Feature row. A line in a plan's feature list (label plus checkmark or info icon).

Page: pricing. Selector: `li feature`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 277 x 22.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 15px/22.5px 400 |
| Letter spacing | -0.1px |
| Colour | #767676 |
| Transition | none |
| How | at rest |

Crops: `feature-row-default.png`.

#### info-icon

Info icon. The "i" badge beside a feature — hovering opens a tooltip.

Page: pricing. Selector: `button info`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 16 x 16 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 0px |
| Font | Roobert 15px/20px 400 | = | = |
| Letter spacing | -0.1px | = | = |
| Colour | #767676 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 17 x 16, colour #767676 | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | button.d_none.laptop:d_block 16.0x16.0 outline 1px auto #101010 offset 0px |

Crops: `info-icon-default.png`, `info-icon-hover.png`, `info-icon-focus-visible.png`.

#### faq-item

FAQ item. A pricing FAQ disclosure: question row with a chevron. The open state is captured by its own toggle.

Page: pricing. Selector: `button faq`. States: default, hover, open.

| Property | default | hover | open |
|---|---|---|---|
| Size (w x h) | 800 x 68 | = | = |
| Padding | 20px 24px | = | = |
| Gap | 12px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Roobert 16px/24px 400 | = | = |
| Letter spacing | -0.1px | = | = |
| Colour | #141414 | = | = |
| Text node | h3.ta_start.textStyle_body.m.semibold: Roobert 20px/28px 600, #141414, ls -0.2px | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 24 x 24, colour #141414 | = | = |
| Ancestor paint | 1 up div.pos_relative.mbe_200 bg #f2f2f2 | 1 up div.pos_relative.mbe_200 bg #f5f5f5 | 1 up div.pos_relative.mbe_200 bg #f5f5f5 |
| How | at rest | mouse hover | opened by its own toggle; the answer panel below measured with it |

Crops: `faq-item-default.png`, `faq-item-hover.png`, `faq-item-open.png`.

### Marketplace browse (/lp)

#### lp-header

LP top bar. The /lp microsite chrome: its own stylesheet, no Panda vars — every value here is measured.

Page: lp. Selector: `lp chrome`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 66 |
| Padding | 8px 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #0d1619 |
| Text node | div.axDOAG.FkLavb: Roobert 14px/20px 500, #0d0d0d, ls -0.1px |
| Transition | none |
| Icon | 74.97 x 22, colour #0d1619, fill #000000 |
| Painted layers | div.zeLhfM.KUb747 720.0x48.0 bg #ffffff border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 999px shadow #141414 @ 0.02 0px 2px 3px 0px, #141414 @ 0.03 0px 4px 6px 0px; a::before.OP1nBW._aj4fe 1pxx20px bg #e5e5e5; a::before.OP1nBW._aj4fe 1pxx20px bg #e5e5e5; a::before.OP1nBW._aj4fe 1pxx20px bg #e5e5e5; span.jxuPik 36.0x36.0 bg #0d0d0d r 999px; div.zjRND1.teEzkc 0.0x0.0 bg #ffffff |
| Ancestor paint | 1 up div.cvV1n9 bg #ffffff |
| How | at rest |

Crops: `lp-header-default.png`.

#### lp-venue-card

Browse venue card. A venue result in the /lp list: photo, name, address, rating and review count, next-availability line.

Page: lp. Selector: `article venue`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 381.33 x 543.5 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Roobert 16px/18.4px 400 | = |
| Letter spacing | normal | = |
| Colour | #0d1619 | = |
| Text node | span.axDOAG.KODqUv: Roobert 13px/16px 600, #0d0d0d, ls -0.1px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #0d1619, fill #000000 | = |
| Painted layers | span.axDOAG.KODqUv 81.2x24.0 image linear-gradient(#ffffff @ 0.7, #ffffff @ 0.7) r 999px shadow #141414 @ 0.12 0px 1px 6px 0px, #141414 @ 0.04 0px 0px 0px 1px; span::before.axDOAG.KODqUv 79.2031pxx22px image linear-gradient(135deg, #ffffff @ 0.8 20%, #ffffff @ 0 40%, #ffffff @ 0 60%, #ffffff @ 0.6 r 999px; span.axDOAG.KODqUv 57.5x24.0 image linear-gradient(#ffffff @ 0.7, #ffffff @ 0.7) r 999px shadow #141414 @ 0.12 0px 1px 6px 0px, #141414 @ 0.04 0px 0px 0px 1px; span::before.axDOAG.KODqUv 55.5156pxx22px image linear-gradient(135deg, #ffffff @ 0.8 20%, #ffffff @ 0 40%, #ffffff @ 0 60%, #ffffff @ 0.6 r 999px; div.jc1E8C 381.3x64.0 bg #f5f5f5 r 16px; div.jc1E8C 381.3x64.0 bg #f5f5f5 r 16px | = |
| Ancestor paint | 1 up div.paUULP.Z1aKNU bg #ffffff | = |
| How | at rest | mouse hover |

Crops: `lp-venue-card-default.png`, `lp-venue-card-hover.png`.

#### lp-map-button

See map button. Opens the map panel over the results. Measured at rest and opened by its own control where the overlay mounts.

Page: lp. Selector: `button "See map"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 63.31 x 19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0d0d0d offset 2px | = |
| Font | Roobert 16px/22px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #6950f3 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.OP1nBW 63.3x19.0 outline 2px solid #0d0d0d offset 2px | = |

Crops: `lp-map-button-default.png`, `lp-map-button-hover.png`, `lp-map-button-focus-visible.png`, `lp-map-button-pressed.png`.

#### lp-pagination

Pagination. The result-list pager. Measured, never followed.

Page: lp. Selector: `pagination`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 64.61 x 38 | = |
| Padding | 8px 16px | = |
| Border | 1px solid #d3d3d3 | 1px solid #bfbfbf |
| Radius | 999px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Roobert 14px/20px 500 | = |
| Letter spacing | -0.1px | = |
| Colour | #0d0d0d | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | a.buRoOI 64.6x38.0 bg #ffffff border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 999px | a.buRoOI 64.6x38.0 bg #ffffff border T:1px #bfbfbf / R:1px #bfbfbf / B:1px #bfbfbf / L:1px #bfbfbf r 999px |
| How | at rest | mouse hover |

Crops: `lp-pagination-default.png`, `lp-pagination-hover.png`.

#### lp-category-chip

Category chip. A category pill in the footer browse row (Beauty Salons, Barbers, Nail Salons …). A link; measured, never followed.

Page: lp. Selector: `category chip`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 126.7 x 36 | = |
| Padding | 6px 16px | = |
| Border | 1px solid #e5e5e5 | 1px solid #b7babe |
| Radius | 999px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Roobert 14px/20px 500 | = |
| Letter spacing | -0.1px | = |
| Colour | #0d0d0d | = |
| Text node | span.DpJCAG: Roobert 14px/20px 500, #0d0d0d, ls -0.1px | = |
| Transition | border-color 0.25s cubic-bezier(0.42, 0, 0.58, 1) | = |
| Cursor | pointer | = |
| Painted layers | a.OP1nBW.QoUCns 126.7x36.0 bg #ffffff border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 999px | a.OP1nBW.QoUCns 126.7x36.0 bg #ffffff border T:1px #b7babe / R:1px #b7babe / B:1px #b7babe / L:1px #b7babe r 999px |
| How | at rest | mouse hover |

Crops: `lp-category-chip-default.png`, `lp-category-chip-hover.png`.

#### lp-see-all

See all services link. The "See all N services" link inside a venue card. Measured, never followed.

Page: lp. Selector: `see-all link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 381.33 x 19 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Roobert 14px/19px 500 | = |
| Letter spacing | -0.1px | = |
| Colour | #6950f3 | #5c4ace |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `lp-see-all-default.png`, `lp-see-all-hover.png`.

#### lp-price

Card price. A service price inside a venue card ("$98", "from $0").

Page: lp. Selector: `price span`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 26.7 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 14px/20px 500 |
| Letter spacing | -0.1px |
| Colour | #0d0d0d |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `lp-price-default.png`.

### Help centre

#### help-search

Help search field. The help-centre search input (a 654x60 pill). Focused only — no query is sent.

Page: help. Selector: `input "Search our help center"`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 654 x 60 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = |
| Font | Roobert 16px/16px 400 | = |
| Letter spacing | -0.1px | = |
| Colour | #262627 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #9ca3af, opacity 1 | = |
| Painted layers | input.[&::-webkit-search-decoration]:d_none.[&::-webkit-search-cancel-button]:d_none 654.0x60.0 bg #ffffff outline 2px solid #000000 @ 0 offset 2px | = |
| How | at rest | clicked into the field |

Crops: `help-search-default.png`, `help-search-focused.png`.

#### topic-card

Help topic card. A help topic tile linking to an article group. Measured, never followed.

Page: help. Selector: `a topic`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 362.66 x 210 | = |
| Padding | 32px | = |
| Gap | 16px | = |
| Border | 1px solid #e5e5e5 | 1px solid #d3d3d3 |
| Radius | 8px | = |
| Background | #ffffff | #f5f5f5 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Roobert 16px/24px 400 | = |
| Letter spacing | -0.1px | = |
| Colour | #0d0d0d | = |
| Text node | h3.mbe_25.tablet:mbe_50: Roobert 20px/28px 600, #0d0d0d, ls -0.2px | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | a.d_flex.ai_center 362.7x210.0 bg #ffffff border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 8px | a.d_flex.ai_center 362.7x210.0 bg #f5f5f5 border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 8px |
| How | at rest | mouse hover |

Crops: `topic-card-default.png`, `topic-card-hover.png`.

#### article-link

Article link. A help article row. Measured, never followed.

Page: help. Selector: `a article`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 362.67 x 234 | = |
| Padding | 32px | = |
| Gap | 16px | = |
| Border | 1px solid #e5e5e5 | 1px solid #d3d3d3 |
| Radius | 8px | = |
| Background | #ffffff | #f5f5f5 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Roobert 16px/24px 400 | = |
| Letter spacing | -0.1px | = |
| Colour | #0d0d0d | = |
| Text node | h3.mbe_25.tablet:mbe_50: Roobert 20px/28px 600, #0d0d0d, ls -0.2px | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | a.d_flex.ai_center 362.7x234.0 bg #ffffff border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 8px | a.d_flex.ai_center 362.7x234.0 bg #f5f5f5 border T:1px #d3d3d3 / R:1px #d3d3d3 / B:1px #d3d3d3 / L:1px #d3d3d3 r 8px |
| How | at rest | mouse hover |

Crops: `article-link-default.png`, `article-link-hover.png`.

### Mobile (390 wide)

#### m-header

Mobile top bar. The 390x72 sticky mobile bar: wordmark left, icon burger right.

Page: home. Selector: `nav sticky`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | Roobert 16px/18.4px 400 |
| Letter spacing | -0.1px |
| Colour | #0d0d0d |
| Transition | block-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) |
| Icon | 74.97 x 22, colour #0d0d0d |
| Painted layers | div.pos_sticky.bg-c_transparent 390.0x72.0 shadow #000000 @ 0 0px 0px 0px 0px; a::before.pos_relative.before:bx-s_border-box 74.9688pxx48px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; button.ring_none.pos_relative 32.0x32.0 outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 32pxx32px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px; div.inset-x_0.inset-bs_[var(--navbar-height)] 0.0x772.0 bg #131313 @ 0.25 |
| Ancestor paint | 1 up div.bg-c_background.page bg #ffffff |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button. The 32x32 icon-only burger (aria-label "Menu") in the mobile bar.

Page: home. Selector: `button[aria-label=Menu]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Roobert 16px/18.4px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 32 x 32, colour #0d0d0d | = | = | = |
| ::before | 32px x 32px, absolute, bg #000000 @ 0, radius 0px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = | = | = |
| Painted layers | button.ring_none.pos_relative 32.0x32.0 outline 2px solid #000000 @ 0 offset 2px; button::before.ring_none.pos_relative 32pxx32px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-search-field

Mobile search field.

Page: home. Selector: `input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 238 x 24 | = |
| Padding | 1px 2px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = |
| Font | Roobert 16px/22px 500 | = |
| Letter spacing | -0.1px | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #0d0d0d, opacity 1 | = |
| Painted layers | input.ap_none.bg-c_transparent 238.0x24.0 outline 2px solid #000000 @ 0 offset 2px | = |
| How | at rest | clicked into the field |

Crops: `m-search-field-default.png`, `m-search-field-focused.png`.

#### m-venue-card

Mobile venue card.

Page: home. Selector: `a[href*="/a/"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 236 x 227.33 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 16px/18.4px 400 |
| Letter spacing | -0.1px |
| Colour | #0d0d0d |
| Transition | none |
| Cursor | pointer |
| ::before | 236px x 227.328px, absolute, bg #000000 @ 0, radius 0px, shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px |
| Painted layers | a::before.pos_absolute.before:bx-s_border-box 236pxx227.328px shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px |
| How | at rest |

Crops: `m-venue-card-default.png`.

## Transitions declared in the readable stylesheets

Fresha compiles its Panda layer to hashed selectors and atomic class names, so this list holds the transitions and animations the CSSOM could read on each page, by hashed selector; the per-state Transition rows above are computed values and cover the same rules.

- auth: `inset-inline-start 0.18s, inline-size 0.18s, opacity 0.12s`, `max-inline-size`, `none`, `scale var(--duration-var) var(--easing-var), max-inline-size var(--duration-var-1) var(--easing-var-1), padding var(--duration-var-1) var(--easing-var-1), gap var(--duration-var-1) var(--easing-var-1)`, `scale`

- booking: `inset-inline-start 0.18s, inline-size 0.18s, opacity 0.12s`, `max-inline-size`, `none`, `scale var(--duration-var) var(--easing-var), max-inline-size var(--duration-var-1) var(--easing-var-1), padding var(--duration-var-1) var(--easing-var-1), gap var(--duration-var-1) var(--easing-var-1)`, `scale`

- home: `inset-inline-start 0.18s, inline-size 0.18s, opacity 0.12s`, `max-inline-size`, `none`, `scale var(--duration-var) var(--easing-var), max-inline-size var(--duration-var-1) var(--easing-var-1), padding var(--duration-var-1) var(--easing-var-1), gap var(--duration-var-1) var(--easing-var-1)`, `scale`

- lp: `fill 200ms`, `border-color 200ms`, `background-color 180ms cubic-bezier(0.42, 0, 0.58, 1)`, `max-height 300ms ease-out`, `max-height 600ms ease-in-out`, `opacity 150ms, transform 150ms, visibility linear 150ms`, `opacity 250ms, transform 250ms`, `background-color 150ms cubic-bezier(0.215, 0.61, 0.355, 1), border-color`, `box-shadow 180ms cubic-bezier(0.42, 0, 0.58, 1)`, `background-color 150ms cubic-bezier(0.42, 0, 0.58, 1), border-color, opacity, visibility`, `border-color 150ms cubic-bezier(0.215, 0.61, 0.355, 1)`, `transform 250ms cubic-bezier(0.42, 0, 0.58, 1)`

- partner: `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`

- pricing: `all var(--jKFPlR) cubic-bezier(.4,0,.2,1)`, `border-color var(--egBACz) var(--izYRnJ)`, `color var(--jKFPlR) cubic-bezier(.4,0,.2,1),background-color var(--jKFPlR) cubic-bezier(.4,0,.2,1),border-color var(--jKFPlR) cubic-bezier(.4,0,.2,1),text-decoration-color var(--jKFPlR) cubic-bezier(.4,0,.2,1),fill var(--jKFPlR) cubic-bezier(.4,0,.2,1),stroke var(--jKFPlR) cubic-bezier(.4,0,.2,1)`, `height var(--jKFPlR) var(--izYRnJ),width var(--jKFPlR) var(--izYRnJ)`, `opacity var(--jKFPlR) ease-in,filter var(--jKFPlR) ease-in`, `scale var(--duration-var) var(--easing-var),max-inline-size var(--duration-var-1) var(--easing-var-1),padding var(--duration-var-1) var(--easing-var-1),gap var(--duration-var-1) var(--easing-var-1)`, `transform var(--jKFPlR) cubic-bezier(.4,0,.2,1)`, `none`

- venue: `inset-inline-start 0.18s, inline-size 0.18s, opacity 0.12s`, `max-inline-size`, `none`, `scale var(--duration-var) var(--easing-var), max-inline-size var(--duration-var-1) var(--easing-var-1), padding var(--duration-var-1) var(--easing-var-1), gap var(--duration-var-1) var(--easing-var-1)`, `scale`
