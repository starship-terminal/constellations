# FlutterFlow component measurements

Computed styles read from flutterflow.io on 2026-11-15 by `tools/capture/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents. The site ships two generations of its marketing skin: the home page's module set (.composer/.cmp-*, .pbtn, .pg-*) and the ff-* layer every other page carries (.ff-btn, .ff-fld, .ff-snav, .ff-acc, .ff-seg, .ff-tsw); both are measured.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `selected` and `open` are resting states reached by the page's own toggles (the billing segmented control, a tab, an accordion, the nav menu button, the mobile sheet); `dark` is the same component measured again with the footer theme switch set to Dark (data-theme="dark"), restored to Light after.

## Components

### Shell and navigation

#### skip-link

Skip to content link. The first tab stop on every page: a visually-hidden link that paints when focused.

Page: pricing. Selector: `.ff-page-skip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 152 x 44 |
| Padding | 0px 22px |
| Border | none |
| Radius | 999px |
| Background | #1a1a1a |
| Box shadow | none |
| Outline | none |
| Font | Inter 15px/23.25px 510 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | transform 0.24s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| Transform | matrix(1, 0, 0, 1, 0, -68) |
| Cursor | pointer |
| Painted layers | a.ff-page-skip 152.0x44.0 bg #1a1a1a r 999px |
| Ancestor paint | 1 up body bg #fcfcfb |
| How | at rest |

Crops: `skip-link-default.png`.

#### announcement

Announcement banner. The slim bar above the header ("FlutterFlow for Web is here"): the accent line colour, a "What's changing" link and a Dismiss icon button. Shown, never dismissed.

Page: pricing. Selector: `.ff-ban`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 1440 x 40 | = |
| Padding | 8px 48px | = |
| Gap | 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #f5f5f5 | #0b0b0b |
| Box shadow | #000000 @ 0.08 0px -0.5px 0px 0px inset | #ffffff @ 0.08 0px -0.5px 0px 0px inset |
| Outline | none | = |
| Font | Inter 13px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #3d3d3d | #c8c8c8 |
| Text node | p: Inter 13px/20px 400, #3d3d3d | p: Inter 13px/20px 400, #c8c8c8 |
| Transition | none | = |
| Icon | 15 x 15, colour #6b6b6b | 15 x 15, colour #a0a0a0 |
| Painted layers | div.ff-ban 1440.0x40.0 bg #f5f5f5 shadow #000000 @ 0.08 0px -0.5px 0px 0px inset | div.ff-ban 1440.0x40.0 bg #0b0b0b shadow #ffffff @ 0.08 0px -0.5px 0px 0px inset |
| Ancestor paint | 1 up body bg #fcfcfb | 1 up body bg #121212 |
| How | at rest | footer theme switch set to Dark (data-theme="dark"), restored after |

Crops: `announcement-default.png`, `announcement-dark.png`.

#### banner-dismiss

Banner dismiss button. The small square icon button that closes the announcement bar. Measured, never pressed.

Page: pricing. Selector: `.ff-ban .ff-ibtn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 28 x 28 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 50% | = | = | = |
| Background | transparent | #1a1a1a @ 0.06 | = | #1a1a1a @ 0.06 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1a1a1a offset 2px | = |
| Font | Inter 13px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6b6b6b | #1a1a1a | = | #1a1a1a |
| Transition | background-color, color 0.12s, 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 15 x 15, colour #6b6b6b | 15 x 15, colour #1a1a1a | = | 15 x 15, colour #1a1a1a |
| Ancestor paint | 1 up div.ff-ban bg #f5f5f5 shadow #000000 @ 0.08 0px -0.5px 0px 0px inset | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.ff-ibtn 28.0x28.0 bg #1a1a1a @ 0.06 r 50% | button.ff-ibtn 28.0x28.0 r 50% outline 2px solid #1a1a1a | button.ff-ibtn 28.0x28.0 bg #1a1a1a @ 0.06 r 50% |

Crops: `banner-dismiss-default.png`, `banner-dismiss-hover.png`, `banner-dismiss-focus-visible.png`, `banner-dismiss-pressed.png`.

#### header

Top nav. The floating bar over every page: brand lockup, the Product/Studio/Resources menu buttons, Pricing and Enterprise links, Sign in and the Start building pill.

Page: pricing. Selector: `.ff-snav`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 1440 x 64 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #fcfcfb @ 0.86 | #121212 @ 0.86 |
| Box shadow | #000000 @ 0 0px 0.5px 0px 0px | = |
| Backdrop filter | blur(20px) saturate(1.3) | = |
| Outline | none | = |
| Font | Inter 16px/24.8px 400 | = |
| Letter spacing | normal | = |
| Colour | #1a1a1a | #ededed |
| Text node | button.ff-snav-menu: Inter 14px/21.7px 400, #6b6b6b | button.ff-snav-menu: Inter 14px/21.7px 400, #a0a0a0 |
| Transition | box-shadow 0.24s cubic-bezier(0.25, 0.46, 0.45, 0.94) | = |
| Icon | 101.95 x 14.44, colour #1a1a1a, fill #000000 | 101.95 x 14.44, colour #ededed, fill #000000 |
| Painted layers | header.ff-snav 1440.0x64.0 bg #fcfcfb @ 0.86 shadow #000000 @ 0 0px 0.5px 0px 0px; div.ff-snav-panel 248.0x236.0 bg #ffffff r 16px shadow #000000 @ 0.08 0px 0px 0px 1px, #000000 @ 0.28 0px 24px 48px -20px; div.ff-snav-panel.ff-snav-panel-studio 688.0x236.0 bg #ffffff r 16px shadow #000000 @ 0.08 0px 0px 0px 1px, #000000 @ 0.28 0px 24px 48px -20px; a.ff-snav-lead 232.0x236.0 bg #f5f5f5 border R:1px #000000 @ 0.08 r 16px 0px 0px 16px; span.ff-ptag-dot.ff-ptag-studio 7.0x7.0 bg #4b39ef r 50%; span.ff-btn.ff-btn-primary 183.0x32.0 bg #1a1a1a r 999px | header.ff-snav 1440.0x64.0 bg #121212 @ 0.86 shadow #000000 @ 0 0px 0.5px 0px 0px; div.ff-snav-panel 248.0x236.0 bg #1b1b1b r 16px shadow #ffffff @ 0.1 0px 0px 0px 1px, #000000 0px 24px 48px -20px; div.ff-snav-panel.ff-snav-panel-studio 688.0x236.0 bg #1b1b1b r 16px shadow #ffffff @ 0.1 0px 0px 0px 1px, #000000 0px 24px 48px -20px; a.ff-snav-lead 232.0x236.0 bg #0b0b0b border R:1px #ffffff @ 0.08 r 16px 0px 0px 16px; span.ff-ptag-dot.ff-ptag-studio 7.0x7.0 bg #b7adff r 50%; span.ff-btn.ff-btn-primary 183.0x32.0 bg #ededed r 999px |
| Ancestor paint | 1 up body bg #fcfcfb | 1 up body bg #121212 |
| How | at rest | footer theme switch set to Dark (data-theme="dark"), restored after |

Crops: `header-default.png`, `header-dark.png`.

#### nav-menu-button

Nav menu button. A top-level menu trigger (Product): 14px nav text with a chevron; opens the snav panel.

Page: pricing. Selector: `.ff-snav-menu`. States: default, hover, focus-visible, pressed, dark.

| Property | default | hover | focus-visible | pressed | dark |
|---|---|---|---|---|---|
| Size (w x h) | 92 x 37.69 | = | = | = | = |
| Padding | 8px 10px 8px 12px | = | = | = | = |
| Gap | 4px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 999px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #1a1a1a offset 2px | = | = |
| Font | Inter 14px/21.7px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #6b6b6b | #1a1a1a | = | #1a1a1a | #a0a0a0 |
| Transition | color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 14 x 14, colour #6b6b6b | 14 x 14, colour #1a1a1a | = | 14 x 14, colour #1a1a1a | 14 x 14, colour #a0a0a0 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | footer theme switch set to Dark (data-theme="dark"), restored after |
| Painted layers | - | = | button.ff-snav-menu 92.0x37.7 r 999px outline 2px solid #1a1a1a | = | = |

Crops: `nav-menu-button-default.png`, `nav-menu-button-hover.png`, `nav-menu-button-focus-visible.png`, `nav-menu-button-pressed.png`, `nav-menu-button-dark.png`.

#### nav-panel

Nav dropdown panel. The Product flyout: a card-radius floating panel with lead link, column headings and item rows.

Page: pricing. Selector: `.ff-snav-panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 248 x 236 |
| Padding | 8px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.08 0px 0px 0px 1px, #000000 @ 0.28 0px 24px 48px -20px |
| Outline | none |
| Font | Inter 16px/24.8px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | p.ff-snav-h: Inter 12px/16px 510, #6b6b6b |
| Transition | opacity, visibility 0.24s, 0.24s cubic-bezier(0.25, 0.46, 0.45, 0.94), ease delay 0s, 0s |
| Icon | 13 x 13, colour #6b6b6b |
| Painted layers | div.ff-snav-panel 248.0x236.0 bg #ffffff r 16px shadow #000000 @ 0.08 0px 0px 0px 1px, #000000 @ 0.28 0px 24px 48px -20px |
| How | at rest |

Crops: `nav-panel-default.png`.

#### nav-panel-item

Nav dropdown item.

Page: pricing. Selector: `.ff-snav-panel a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 216 x 32 | = |
| Padding | 0px 8px | = |
| Gap | 6px | = |
| Border | none | = |
| Radius | 10px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/21.7px 400 | = |
| Letter spacing | normal | = |
| Colour | #1a1a1a | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `nav-panel-item-default.png`, `nav-panel-item-hover.png`.

#### nav-link

Nav link. The plain text links in the bar (Pricing, Enterprise).

Page: pricing. Selector: `.ff-snav-lk`. States: default, hover, focus-visible, pressed, dark.

| Property | default | hover | focus-visible | pressed | dark |
|---|---|---|---|---|---|
| Size (w x h) | 69 x 37.69 | = | = | = | = |
| Padding | 8px 12px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 999px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #1a1a1a offset 2px | = | = |
| Font | Inter 14px/21.7px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #6b6b6b | #1a1a1a | = | #1a1a1a | #a0a0a0 |
| Transition | color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Ancestor paint | 3 up header.ff-snav bg #fcfcfb @ 0.86 shadow #000000 @ 0 0px 0.5px 0px 0px | = | = | = | 3 up header.ff-snav bg #121212 @ 0.86 shadow #000000 @ 0 0px 0.5px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | footer theme switch set to Dark (data-theme="dark"), restored after |
| Painted layers | - | = | a.ff-snav-lk 69.0x37.7 r 999px outline 2px solid #1a1a1a | = | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`, `nav-link-dark.png`.

#### nav-signin

Sign in link. The secondary text link in the nav end. Measured, never followed.

Page: pricing. Selector: `.ff-snav-signin`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 68 x 37.69 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1a1a1a offset 2px | = |
| Font | Inter 14px/21.7px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6b6b6b | #1a1a1a | = | #1a1a1a |
| Transition | color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94) | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 3 up header.ff-snav bg #fcfcfb @ 0.86 shadow #000000 @ 0 0px 0.5px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.ff-snav-lk.ff-snav-signin 68.0x37.7 r 999px outline 2px solid #1a1a1a | = |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### btn-primary-sm

Start building (nav, small). The small contrast pill in the nav: --ff-color-contrast fill, --ff-color-contrast-ink text, radius pill. Measured, never followed.

Page: pricing. Selector: `.ff-btn.ff-btn-primary.ff-btn-sm`. States: default, hover, focus-visible, pressed, dark.

| Property | default | hover | focus-visible | pressed | dark |
|---|---|---|---|---|---|
| Size (w x h) | 183 x 32 | = | - | 177.51 x 31.04 | = |
| Padding | 0px 14px | = | - | = | = |
| Gap | 8px | = | - | = | = |
| Border | none | = | - | = | = |
| Radius | 999px | = | - | = | = |
| Background | #1a1a1a | = | - | = | #ededed |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | Inter 13px/20.15px 510 | = | - | = | = |
| Letter spacing | normal | = | - | = | = |
| Colour | #ffffff | = | - | = | #111111 |
| Transition | transform, background-color, box-shadow 0.12s, 0.12s, 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s, 0s | = | - | = | = |
| Cursor | pointer | = | - | = | = |
| Painted layers | span.ff-btn.ff-btn-primary 183.0x32.0 bg #1a1a1a r 999px | = | - | span.ff-btn.ff-btn-primary 177.5x31.0 bg #1a1a1a r 999px | span.ff-btn.ff-btn-primary 183.0x32.0 bg #ededed r 999px |
| Ancestor paint | 1 up a.ff-snav-lead bg #f5f5f5; 2 up div.ff-snav-panel.ff-snav-panel-studio bg #ffffff shadow #000000 @ 0.08 0px 0px 0px 1px, #000000 @ 0.28 0px 24px 48px -20px | = | - | = | 1 up a.ff-snav-lead bg #0b0b0b; 2 up div.ff-snav-panel.ff-snav-panel-studio bg #1b1b1b shadow #ffffff @ 0.1 0px 0px 0px 1px, #000000 0px 24px 48px -20px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | footer theme switch set to Dark (data-theme="dark"), restored after |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) | = |

Crops: `btn-primary-sm-default.png`, `btn-primary-sm-hover.png`, `btn-primary-sm-pressed.png`, `btn-primary-sm-dark.png`.

#### brand

Brand lockup. The FlutterFlow mark + wordmark link; the mark is a filtered image (--ff-theme-logo-filter) so it inverts in dark.

Page: pricing. Selector: `.ff-lkp`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 139.95 x 30 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/31px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Transition | none |
| Cursor | pointer |
| Icon | 101.95 x 14.44, colour #1a1a1a, fill #000000 |
| Ancestor paint | 2 up header.ff-snav bg #fcfcfb @ 0.86 shadow #000000 @ 0 0px 0.5px 0px 0px |
| How | at rest |

Crops: `brand-default.png`.

### Pricing

#### plan-grid

Plan grid. The plans list: a carded grid of plan columns under the billing toggle.

Page: pricing. Selector: `.ff-plg`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1344 x 581.25 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #f5f5f5 |
| Box shadow | #000000 @ 0.08 0px 0px 0px 0.5px inset |
| Outline | none |
| Font | Inter 16px/24.8px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | h2.ff-plg-n: Inter 16px/24px 600, #1a1a1a, ls -0.176px |
| Transition | none |
| Icon | 15 x 15, colour #6b6b6b |
| Painted layers | ul.ff-plg.ff-plg-reg 1344.0x581.3 bg #f5f5f5 r 16px shadow #000000 @ 0.08 0px 0px 0px 0.5px inset; span.ff-ptag-dot.ff-ptag-studio 7.0x7.0 bg #4b39ef r 50%; a.ff-btn.ff-btn-secondary 272.0x44.0 bg #ffffff r 999px shadow #000000 @ 0.08 0px 0px 0px 0.5px inset, #000000 @ 0.04 0px 1px 2px 0px; div.ff-plg-in 272.0x103.5 border T:1px #000000 @ 0.08; span.ff-ptag 108.0x24.0 bg #ffffff r 999px shadow #000000 @ 0.08 0px 0px 0px 0.5px inset; span.ff-ptag-dot 7.0x7.0 bg #0a68e0 r 50% |
| How | at rest |

Crops: `plan-grid-default.png`.

#### plan-card

Plan card. One plan column: name, price, feature rows and its CTA.

Page: pricing. Selector: `.ff-plg > li`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 336 x 581.25 |
| Padding | 32px |
| Gap | 0px normal |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24.8px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | h2.ff-plg-n: Inter 16px/24px 600, #1a1a1a, ls -0.176px |
| Transition | none |
| Icon | 15 x 15, colour #6b6b6b |
| Painted layers | span.ff-ptag-dot.ff-ptag-studio 7.0x7.0 bg #4b39ef r 50%; a.ff-btn.ff-btn-secondary 272.0x44.0 bg #ffffff r 999px shadow #000000 @ 0.08 0px 0px 0px 0.5px inset, #000000 @ 0.04 0px 1px 2px 0px; div.ff-plg-in 272.0x103.5 border T:1px #000000 @ 0.08; span.ff-ptag 108.0x24.0 bg #ffffff r 999px shadow #000000 @ 0.08 0px 0px 0px 0.5px inset; span.ff-ptag-dot 7.0x7.0 bg #0a68e0 r 50%; span.ff-ptag.ff-ptag-studio 80.0x24.0 bg #ffffff r 999px shadow #000000 @ 0.08 0px 0px 0px 0.5px inset |
| Ancestor paint | 1 up ul.ff-plg.ff-plg-reg bg #f5f5f5 shadow #000000 @ 0.08 0px 0px 0px 0.5px inset |
| How | at rest |

Crops: `plan-card-default.png`.

#### billing-seg

Billing period segmented control. A two-option radiogroup (Monthly/Yearly) with a sliding badge: role=radiogroup, each option a role=radio button; the pill slides via --ff-seg-x/width vars.

Page: pricing. Selector: `.ff-seg`. States: default, selected.

| Property | default | selected |
|---|---|---|
| Size (w x h) | 231 x 38 | = |
| Padding | 3px | = |
| Border | none | = |
| Radius | 999px | = |
| Background | transparent | = |
| Box shadow | #000000 @ 0.08 0px 0px 0px 1px inset | = |
| Outline | none | = |
| Font | Inter 16px/24.8px 400 | = |
| Letter spacing | normal | = |
| Colour | #1a1a1a | = |
| Text node | button: Inter 14px/21.7px 510, #1a1a1a | button: Inter 14px/21.7px 510, #6b6b6b |
| Transition | none | = |
| ::before | 82px x 32px, absolute, bg #ffffff, radius 999px, shadow #000000 @ 0.08 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px 0px | 143px x 32px, absolute, bg #ffffff, radius 999px, shadow #000000 @ 0.08 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px 0px |
| Painted layers | div.ff-seg 231.0x38.0 r 999px shadow #000000 @ 0.08 0px 0px 0px 1px inset; div::before.ff-seg 82pxx32px bg #ffffff r 999px shadow #000000 @ 0.08 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px 0px; span.ff-seg-badge 65.0x20.0 bg #f0f0f0 r 999px | div.ff-seg 231.0x38.0 r 999px shadow #000000 @ 0.08 0px 0px 0px 1px inset; div::before.ff-seg 143pxx32px bg #ffffff r 999px shadow #000000 @ 0.08 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px 0px; span.ff-seg-badge 65.0x20.0 bg #f0f0f0 r 999px |
| How | at rest | the page's own control |

Crops: `billing-seg-default.png`, `billing-seg-selected.png`.

#### billing-seg-option

Segmented control option.

Page: pricing. Selector: `.ff-seg [role="radio"], .ff-seg [data-ff-value]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 82 x 32 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1a1a1a offset 2px | = |
| Font | Inter 14px/21.7px 510 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6b6b6b | #1a1a1a | = | #1a1a1a |
| Transition | color, background-color 0.12s, 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.ff-seg shadow #000000 @ 0.08 0px 0px 0px 1px inset | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button 82.0x32.0 r 999px outline 2px solid #1a1a1a | = |

Crops: `billing-seg-option-default.png`, `billing-seg-option-hover.png`, `billing-seg-option-focus-visible.png`, `billing-seg-option-pressed.png`.

#### plan-cta

Plan CTA (secondary). The secondary button: --ff-color-card fill with the hairline rule and resting shadow. Measured, never followed.

Page: pricing. Selector: `.ff-btn.ff-btn-secondary`. States: default, hover, focus-visible, pressed, dark.

| Property | default | hover | focus-visible | pressed | dark |
|---|---|---|---|---|---|
| Size (w x h) | 272 x 44 | = | = | 263.84 x 42.68 | = |
| Padding | 0px 22px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 999px | = | = | = | = |
| Background | #ffffff | #f0f0f0 | = | #f0f0f0 | #1b1b1b |
| Box shadow | #000000 @ 0.08 0px 0px 0px 0.5px inset, #000000 @ 0.04 0px 1px 2px 0px | = | = | = | #ffffff @ 0.08 0px 0px 0px 0.5px inset, #000000 @ 0.04 0px 1px 2px 0px |
| Outline | none | = | 2px solid #1a1a1a offset 2px | = | = |
| Font | Inter 15px/23.25px 510 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #1a1a1a | = | = | = | #ededed |
| Transition | transform, background-color, box-shadow 0.12s, 0.12s, 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s, 0s | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | a.ff-btn.ff-btn-secondary 272.0x44.0 bg #ffffff r 999px shadow #000000 @ 0.08 0px 0px 0px 0.5px inset, #000000 @ 0.04 0px 1px 2px 0px | a.ff-btn.ff-btn-secondary 272.0x44.0 bg #f0f0f0 r 999px shadow #000000 @ 0.08 0px 0px 0px 0.5px inset, #000000 @ 0.04 0px 1px 2px 0px | a.ff-btn.ff-btn-secondary 272.0x44.0 bg #ffffff r 999px shadow #000000 @ 0.08 0px 0px 0px 0.5px inset, #000000 @ 0.04 0px 1px 2px 0px outline 2px solid #1a1a1a | a.ff-btn.ff-btn-secondary 263.8x42.7 bg #f0f0f0 r 999px shadow #000000 @ 0.08 0px 0px 0px 0.5px inset, #000000 @ 0.04 0px 1px 2px 0px | a.ff-btn.ff-btn-secondary 272.0x44.0 bg #1b1b1b r 999px shadow #ffffff @ 0.08 0px 0px 0px 0.5px inset, #000000 @ 0.04 0px 1px 2px 0px |
| Ancestor paint | 2 up ul.ff-plg.ff-plg-reg bg #f5f5f5 shadow #000000 @ 0.08 0px 0px 0px 0.5px inset | = | = | = | 2 up ul.ff-plg.ff-plg-reg bg #0b0b0b shadow #ffffff @ 0.08 0px 0px 0px 0.5px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | footer theme switch set to Dark (data-theme="dark"), restored after |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) | = |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`, `plan-cta-dark.png`.

#### plan-cta-primary

Plan CTA (primary). A contrast-fill call to action in the plan grid. Measured, never followed.

Page: pricing. Selector: `.ff-btn.ff-btn-primary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 108 x 32 | = | = | 104.76 x 31.04 |
| Padding | 0px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | #1a1a1a | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1a1a1a offset 2px | = |
| Font | Inter 13px/20.15px 510 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | transform, background-color, box-shadow 0.12s, 0.12s, 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.ff-btn.ff-btn-primary 108.0x32.0 bg #1a1a1a r 999px | = | a.ff-btn.ff-btn-primary 108.0x32.0 bg #1a1a1a r 999px outline 2px solid #1a1a1a | a.ff-btn.ff-btn-primary 104.8x31.0 bg #1a1a1a r 999px |
| Ancestor paint | 3 up header.ff-snav bg #fcfcfb @ 0.86 shadow #000000 @ 0 0px 0.5px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `plan-cta-primary-default.png`, `plan-cta-primary-hover.png`, `plan-cta-primary-focus-visible.png`, `plan-cta-primary-pressed.png`.

#### accordion-item

FAQ accordion item. A details/summary row in the questions list: hairline-separated, a plus/cross marker that turns on open. The first item ships open, so this resting reading is the open look.

Page: pricing. Selector: `.ff-acc-item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 840 x 150 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #000000 @ 0.08; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24.8px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | summary: Inter 17px/26px 510, #1a1a1a, ls -0.204px |
| Transition | none |
| Icon | 21.21 x 21.21, colour #1a1a1a |
| Painted layers | details.ff-acc-item 840.0x150.0 border B:1px #000000 @ 0.08; span.ff-acc-x 39.6x39.6 bg #1a1a1a @ 0.06 r 50% |
| How | at rest |

Crops: `accordion-item-default.png`.

#### accordion-closed

FAQ accordion, closed. The same details element measured closed: the first item ships open, and toggling its own summary shut it — the run's original save named this state "open" before the click was understood.

Page: pricing. Selector: `.ff-acc-item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 840 x 72 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #000000 @ 0.08; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24.8px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | summary: Inter 17px/26px 510, #1a1a1a, ls -0.204px |
| Transition | none |
| Icon | 15 x 15, colour #1a1a1a |
| Painted layers | details.ff-acc-item 840.0x72.0 border B:1px #000000 @ 0.08; span.ff-acc-x 28.0x28.0 bg #1a1a1a @ 0.06 r 50% |
| How | the accordion's own summary (toggled the open item shut) |

Crops: `accordion-closed-default.png`.

#### link-go

Arrow link. The text link with a trailing arrow ("Contact us", question rows): --ff-lnk. Measured, never followed.

Page: pricing. Selector: `.ff-go`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 174.53 x 26 | - | - | = |
| Padding | 0px | - | - | = |
| Gap | 4px | - | - | = |
| Border | none | - | - | = |
| Radius | 0px | - | - | = |
| Background | transparent | - | - | = |
| Box shadow | none | - | - | = |
| Outline | none | - | - | = |
| Font | Inter 15px/26px 510 | - | - | = |
| Letter spacing | -0.176px | - | - | = |
| Colour | #1a1a1a | - | - | = |
| Transition | none | - | - | = |
| Cursor | pointer | - | - | = |
| Icon | 16.05 x 16.05, colour #1a1a1a | - | - | = |
| How | at rest | - | - | CDP forcePseudoState :active:hover |
| Error | - | locator.evaluate: Timeout 8000ms exceeded. Call log:   - waiting for locator('.ff-go').first().first().first()  | = | = |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: none.

### Prompt composer

#### ff-composer

Prompt composer (new skin). The "What should your app do?" field on inner pages: a rounded field (radius-field) with the prompt textarea, idea nav and the send button.

Page: pricing. Selector: `.ff-cmp`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 640 x 130 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24.8px 400 | = |
| Letter spacing | normal | = |
| Colour | #1a1a1a | = |
| Text node | span.ff-cmp-k: Inter 12px/18px 500, #1a1a1a | span.ff-cmp-ghost-t: Inter 16px/24px 400, #6b6b6b @ 0.8 |
| Transition | none | = |
| Icon | 17 x 17, colour #6b6b6b | = |
| Painted layers | div.ff-cmp-card.ff-cmp-big 640.0x130.0 bg #ffffff border T:1px #1a1a1a @ 0.12 / R:1px #1a1a1a @ 0.12 / B:1px #1a1a1a @ 0.12 / L:1px #1a1a1a @ 0.12 r 22px shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px; span.ff-cmp-caret 1.5x18.4 bg #6b6b6b @ 0.8; button.ff-cmp-key 37.0x21.0 bg #fcfcfb border T:1px #000000 @ 0.08 / R:1px #000000 @ 0.08 / B:2px #000000 @ 0.08 / L:1px #000000 @ 0.08 r 6px; button.ff-cmp-go 36.0x36.0 bg #1a1a1a @ 0.08 r 50% | = |
| How | at rest | mouse hover |

Crops: `ff-composer-default.png`, `ff-composer-hover.png`.

#### ff-composer-field

Composer field. The single-line prompt textarea. Text was typed and deleted; nothing was sent.

Page: pricing. Selector: `.ff-cmp-field`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 638 x 128 | = | = |
| Padding | 16px 18px 56px 18px | = | = |
| Border | none | = | = |
| Radius | 0px | 6px | 6px |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1a1a1a | = | = |
| Transition | height 0.32s cubic-bezier(0.2, 0.8, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #000000 @ 0, opacity 1 | = | = |
| Ancestor paint | 1 up div.ff-cmp-card.ff-cmp-big bg #ffffff shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | 1 up div.ff-cmp-card.ff-cmp-big bg #ffffff shadow #1a1a1a @ 0.06 0px 0px 0px 4px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | 1 up div.ff-cmp-card.ff-cmp-big bg #ffffff shadow #1a1a1a @ 0.06 0px 0px 0px 4px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px |
| How | at rest | clicked into the field | typed "A habit tracker for two people", then deleted; nothing sent |

Crops: `ff-composer-field-default.png`, `ff-composer-field-focused.png`, `ff-composer-field-filled.png`.

#### ff-composer-go

Composer send button. The round submit arrow (type=submit). Measured, never pressed.

Page: pricing. Selector: `.ff-cmp-go`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | 33.84 x 33.84 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 50% | = | = | = |
| Background | #1a1a1a @ 0.08 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1a1a1a offset 2px | = |
| Font | Inter 16px/24.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1a1a1a @ 0.4 | = | = | = |
| Transition | background-color, color, transform 0.12s, 0.12s, 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #1a1a1a @ 0.4 | = | = | 16.92 x 16.92, colour #1a1a1a @ 0.4 |
| Painted layers | button.ff-cmp-go 36.0x36.0 bg #1a1a1a @ 0.08 r 50% | = | button.ff-cmp-go 36.0x36.0 bg #1a1a1a @ 0.08 r 50% outline 2px solid #1a1a1a | button.ff-cmp-go 33.8x33.8 bg #1a1a1a @ 0.08 r 50% |
| Ancestor paint | 1 up div.ff-cmp-card.ff-cmp-big bg #ffffff shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | = | 1 up div.ff-cmp-card.ff-cmp-big bg #ffffff shadow #1a1a1a @ 0.06 0px 0px 0px 4px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.94, 0, 0, 0.94, 0, 0) |

Crops: `ff-composer-go-default.png`, `ff-composer-go-hover.png`, `ff-composer-go-focus-visible.png`, `ff-composer-go-pressed.png`.

#### ff-composer-key

Idea key chip. The "Use this idea" suggestion chip inside the composer.

Page: pricing. Selector: `.ff-cmp-key`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 37 x 21 | = | = | = |
| Padding | 0px 7px | = | = | = |
| Border | T: 1px solid #000000 @ 0.08; R: 1px solid #000000 @ 0.08; B: 2px solid #000000 @ 0.08; L: 1px solid #000000 @ 0.08 | T: 1px solid #1a1a1a @ 0.3; R: 1px solid #1a1a1a @ 0.3; B: 2px solid #1a1a1a @ 0.3; L: 1px solid #1a1a1a @ 0.3 | = | T: 1px solid #1a1a1a @ 0.3; R: 1px solid #1a1a1a @ 0.3; B: 2px solid #1a1a1a @ 0.3; L: 1px solid #1a1a1a @ 0.3 |
| Radius | 6px | = | = | = |
| Background | #fcfcfb | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1a1a1a offset 2px | = |
| Font | Inter 12px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1a1a1a | = | = | = |
| Text node | span.ff-cmp-k: Inter 12px/18px 500, #1a1a1a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.ff-cmp-key 37.0x21.0 bg #fcfcfb border T:1px #000000 @ 0.08 / R:1px #000000 @ 0.08 / B:2px #000000 @ 0.08 / L:1px #000000 @ 0.08 r 6px | button.ff-cmp-key 37.0x21.0 bg #fcfcfb border T:1px #1a1a1a @ 0.3 / R:1px #1a1a1a @ 0.3 / B:2px #1a1a1a @ 0.3 / L:1px #1a1a1a @ 0.3 r 6px | button.ff-cmp-key 37.0x21.0 bg #fcfcfb border T:1px #000000 @ 0.08 / R:1px #000000 @ 0.08 / B:2px #000000 @ 0.08 / L:1px #000000 @ 0.08 r 6px outline 2px solid #1a1a1a | button.ff-cmp-key 37.0x21.0 bg #fcfcfb border T:1px #1a1a1a @ 0.3 / R:1px #1a1a1a @ 0.3 / B:2px #1a1a1a @ 0.3 / L:1px #1a1a1a @ 0.3 r 6px |
| Ancestor paint | 3 up div.ff-cmp-card.ff-cmp-big bg #ffffff shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | = | 3 up div.ff-cmp-card.ff-cmp-big bg #ffffff shadow #1a1a1a @ 0.06 0px 0px 0px 4px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ff-composer-key-default.png`, `ff-composer-key-hover.png`, `ff-composer-key-focus-visible.png`, `ff-composer-key-pressed.png`.

#### composer

Prompt composer (home skin). The hero prompt field: a large rounded card with the ghost idea text, the Tab hint and the round send button.

Page: home. Selector: `.composer`. States: default, hover, dark.

| Property | default | hover | dark |
|---|---|---|---|
| Size (w x h) | 720 x 130 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 16px/24.8px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1a1a1a | = | #ededed |
| Text node | span.cmp-ghost-t: Inter 16px/24px 400, #6b6b6b @ 0.8 | = | span.cmp-ghost-t: Inter 16px/24px 400, #a0a0a0 @ 0.8 |
| Transition | none | = | = |
| Icon | 17 x 17, colour #6b6b6b | = | 17 x 17, colour #a0a0a0 |
| Painted layers | div.cmp-card.big 720.0x130.0 bg #ffffff border T:1px #1a1a1a @ 0.12 / R:1px #1a1a1a @ 0.12 / B:1px #1a1a1a @ 0.12 / L:1px #1a1a1a @ 0.12 r 22px shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px; span.cmp-caret 1.5x18.4 bg #6b6b6b @ 0.8; button.cmp-key 39.0x21.0 bg #fcfcfb border T:1px #000000 @ 0.07 / R:1px #000000 @ 0.07 / B:2px #000000 @ 0.07 / L:1px #000000 @ 0.07 r 6px; button.cmp-go 36.0x36.0 bg #1a1a1a @ 0.08 r 50% | = | div.cmp-card.big 720.0x130.0 bg #1b1b1b border T:1px #ededed @ 0.12 / R:1px #ededed @ 0.12 / B:1px #ededed @ 0.12 / L:1px #ededed @ 0.12 r 22px shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px; span.cmp-caret 1.5x18.4 bg #a0a0a0 @ 0.8; button.cmp-key 39.0x21.0 bg #121212 border T:1px #ffffff @ 0.08 / R:1px #ffffff @ 0.08 / B:2px #ffffff @ 0.08 / L:1px #ffffff @ 0.08 r 6px; button.cmp-go 36.0x36.0 bg #ededed @ 0.08 r 50% |
| How | at rest | mouse hover | footer theme switch set to Dark (data-theme="dark"), restored after |

Crops: `composer-default.png`, `composer-hover.png`, `composer-dark.png`.

#### composer-field

Composer textarea. The prompt textarea; text was typed and deleted, nothing sent.

Page: home. Selector: `.cmp-field`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 718 x 128 | = | = |
| Padding | 16px 18px 56px 18px | = | = |
| Border | none | = | = |
| Radius | 0px | 6px | 6px |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1a1a1a | = | = |
| Transition | height 0.32s cubic-bezier(0.2, 0.8, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #000000 @ 0, opacity 1 | = | = |
| Ancestor paint | 1 up div.cmp-card.big bg #ffffff shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | 1 up div.cmp-card.big bg #ffffff shadow #1a1a1a @ 0.06 0px 0px 0px 4px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | 1 up div.cmp-card.big bg #ffffff shadow #1a1a1a @ 0.06 0px 0px 0px 4px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px |
| How | at rest | clicked into the field | typed "A habit tracker for two people", then deleted; nothing sent |

Crops: `composer-field-default.png`, `composer-field-focused.png`, `composer-field-filled.png`.

#### composer-ghost

Composer ghost idea. The suggested prompt painted as placeholder ghost text.

Page: home. Selector: `.cmp-ghost-t`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 225 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #6b6b6b @ 0.8 |
| Transition | none |
| Ancestor paint | 2 up div.cmp-card.big bg #ffffff shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px |
| How | at rest |

Crops: `composer-ghost-default.png`.

#### composer-nav

Idea nav button. The previous/next idea arrows in the composer.

Page: home. Selector: `.cmp-nav`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 30 x 30 | = | - | 0 x 0 |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 50% | = | - | = |
| Background | transparent | #1a1a1a @ 0.06 | - | #1a1a1a @ 0.06 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 16px/24.8px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #6b6b6b | #1a1a1a | - | #1a1a1a |
| Transition | background-color, color 0.15s, 0.15s ease, ease delay 0s, 0s | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 17 x 17, colour #6b6b6b | 17 x 17, colour #1a1a1a | - | 0 x 0, colour #1a1a1a |
| Ancestor paint | 2 up div.cmp-card.big bg #ffffff shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Painted layers | - | button.cmp-nav 30.0x30.0 bg #1a1a1a @ 0.06 r 50% | = | button.cmp-nav 0.0x0.0 bg #1a1a1a @ 0.06 r 50% |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `composer-nav-default.png`, `composer-nav-hover.png`.

#### composer-key

Idea key chip. The "Use this idea" chip under the ghost text (home skin); only painted in the dock composer on this page.

Page: home. Selector: `.cmp-key`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 39 x 21 | - | - | 0 x 0 |
| Padding | 0px 7px | - | - | = |
| Border | T: 1px solid #000000 @ 0.07; R: 1px solid #000000 @ 0.07; B: 2px solid #000000 @ 0.07; L: 1px solid #000000 @ 0.07 | - | - | T: 1px solid #1a1a1a @ 0.3; R: 1px solid #1a1a1a @ 0.3; B: 2px solid #1a1a1a @ 0.3; L: 1px solid #1a1a1a @ 0.3 |
| Radius | 6px | - | - | = |
| Background | #fcfcfb | - | - | = |
| Box shadow | none | - | - | = |
| Outline | none | - | - | = |
| Font | Inter 12px/18px 500 | - | - | = |
| Letter spacing | normal | - | - | = |
| Colour | #1a1a1a | - | - | = |
| Text node | span.k: Inter 12px/18px 500, #1a1a1a | - | - | - |
| Transition | none | - | - | = |
| Cursor | pointer | - | - | = |
| Painted layers | button.cmp-key 39.0x21.0 bg #fcfcfb border T:1px #000000 @ 0.07 / R:1px #000000 @ 0.07 / B:2px #000000 @ 0.07 / L:1px #000000 @ 0.07 r 6px | - | - | button.cmp-key 0.0x0.0 bg #fcfcfb border T:1px #1a1a1a @ 0.3 / R:1px #1a1a1a @ 0.3 / B:2px #1a1a1a @ 0.3 / L:1px #1a1a1a @ 0.3 r 6px |
| Ancestor paint | 3 up div.cmp-card.big bg #ffffff shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | - | - | = |
| How | at rest | - | - | CDP forcePseudoState :active:hover |
| Error | - | locator.hover: Element is not visible Call log:   - waiting for locator('.cmp-key').first().first().first()     - locator resolved to <button data-use="" type="button" class="cmp-key" aria-label="Use  | = | = |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `composer-key-default.png`.

#### composer-go

Send button. The round submit arrow in the composer (type=submit). Measured, never pressed.

Page: home. Selector: `.cmp-go`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | 33.84 x 33.84 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 50% | = | = | = |
| Background | #1a1a1a @ 0.08 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0a68e0 offset 2px | = |
| Font | Inter 16px/24.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1a1a1a @ 0.4 | = | = | = |
| Transition | background-color, color, transform 0.12s, 0.12s, 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #1a1a1a @ 0.4 | = | = | 16.92 x 16.92, colour #1a1a1a @ 0.4 |
| Painted layers | button.cmp-go 36.0x36.0 bg #1a1a1a @ 0.08 r 50% | = | button.cmp-go 36.0x36.0 bg #1a1a1a @ 0.08 r 50% outline 2px solid #0a68e0 | button.cmp-go 33.8x33.8 bg #1a1a1a @ 0.08 r 50% |
| Ancestor paint | 1 up div.cmp-card.big bg #ffffff shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | = | 1 up div.cmp-card.big bg #ffffff shadow #1a1a1a @ 0.06 0px 0px 0px 4px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.94, 0, 0, 0.94, 0, 0) |

Crops: `composer-go-default.png`, `composer-go-hover.png`, `composer-go-focus-visible.png`, `composer-go-pressed.png`.

### Footer

#### footer

Footer. The site foot: brand lockup, link columns, the legal bar, the theme switch and the privacy-choices button.

Page: pricing. Selector: `.ff-ftr-site-foot`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1344 x 868.59 |
| Padding | 64px 0px 0px 0px |
| Border | T: 1px solid #000000 @ 0.08; R: none; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 13px/20.15px 400 |
| Letter spacing | normal |
| Colour | #6b6b6b |
| Text node | p: Inter 13px/19.5px 400, #6b6b6b |
| Transition | none |
| Icon | 91.69 x 12.98, colour #1a1a1a, fill #000000 |
| Painted layers | footer.ff-ftr-site-foot.ff-ftr-all 1344.0x868.6 border T:1px #000000 @ 0.08; div.ff-ftr-id 1344.0x92.0 border B:1px #000000 @ 0.08; span.ff-ptag-dot.ff-ptag-studio 7.0x7.0 bg #4b39ef r 50%; div.ff-tsw 96.0x30.0 r 999px shadow #000000 @ 0.08 0px 0px 0px 1px inset; button 30.0x24.0 bg #ffffff r 999px shadow #000000 @ 0.08 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px 0px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: pricing. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 125.88 x 27 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 7.2px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 4px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1a1a1a offset 3px | = |
| Font | Inter 18px/27.9px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1a1a1a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 91.69 x 12.98, colour #1a1a1a, fill #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.ff-lkp.ff-ftr-brand 125.9x27.0 r 4px outline 2px solid #1a1a1a | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### theme-switch

Theme switch. The footer Light/Dark/"Match your system" radiogroup (data-ff-tsw; writes ff-theme to localStorage). The dark reading is measured with the switch on Dark.

Page: pricing. Selector: `.ff-tsw`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 96 x 30 | = |
| Padding | 3px | = |
| Border | none | = |
| Radius | 999px | = |
| Background | transparent | = |
| Box shadow | #000000 @ 0.08 0px 0px 0px 1px inset | #ffffff @ 0.08 0px 0px 0px 1px inset |
| Outline | none | = |
| Font | Inter 13px/20.15px 400 | = |
| Letter spacing | normal | = |
| Colour | #6b6b6b | #a0a0a0 |
| Transition | none | = |
| Icon | 14 x 14, colour #6b6b6b | 14 x 14, colour #a0a0a0 |
| Painted layers | div.ff-tsw 96.0x30.0 r 999px shadow #000000 @ 0.08 0px 0px 0px 1px inset; button 30.0x24.0 bg #ffffff r 999px shadow #000000 @ 0.08 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px 0px | div.ff-tsw 96.0x30.0 r 999px shadow #ffffff @ 0.08 0px 0px 0px 1px inset; button 30.0x24.0 bg #1b1b1b r 999px shadow #ffffff @ 0.08 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px 0px |
| How | at rest | footer theme switch set to Dark (data-theme="dark"), restored after |

Crops: `theme-switch-default.png`, `theme-switch-dark.png`.

#### theme-switch-pick

Theme switch option. A role=radio button in the switch; the checked one carries aria-checked=true.

Page: pricing. Selector: `.ff-tsw [data-ff-tsw-pick]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 30 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | 4px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1a1a1a offset 3px | = |
| Font | Inter 13px/20.15px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6b6b6b | #1a1a1a | = | #1a1a1a |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #6b6b6b | 14 x 14, colour #1a1a1a | = | 14 x 14, colour #1a1a1a |
| Ancestor paint | 1 up div.ff-tsw shadow #000000 @ 0.08 0px 0px 0px 1px inset | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button 30.0x24.0 r 4px outline 2px solid #1a1a1a | = |

Crops: `theme-switch-pick-default.png`, `theme-switch-pick-hover.png`, `theme-switch-pick-focus-visible.png`, `theme-switch-pick-pressed.png`.

#### cookie-button

Privacy choices button. The "Your Privacy Choices" footer button (hidden outside banner regions). Measured at rest.

Page: pricing. Selector: `.ft-cookie`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 0 x 0 |
| Padding | 0px |
| Gap | 6px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 13px/20.15px 400 |
| Letter spacing | normal |
| Colour | #6b6b6b |
| Transition | none |
| Cursor | pointer |
| Icon | 0 x 0, colour #6b6b6b, fill #000000 |
| How | at rest |

Crops: none.

#### theme-switch-home

Theme switch (home skin).

Page: home. Selector: `.ft-theme`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 96 x 30 |
| Padding | 3px |
| Border | none |
| Radius | 999px |
| Background | transparent |
| Box shadow | #e7e7e5 0px 0px 0px 1px inset |
| Outline | none |
| Font | Inter 13px/20.15px 400 |
| Letter spacing | normal |
| Colour | #6b6b6b |
| Transition | none |
| Icon | 14 x 14, colour #6b6b6b |
| Painted layers | div.ft-theme 96.0x30.0 r 999px shadow #e7e7e5 0px 0px 0px 1px inset; button 30.0x24.0 bg #ffffff r 999px shadow #000000 @ 0.07 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px 0px |
| How | at rest |

Crops: `theme-switch-home-default.png`.

### Enterprise contact form

#### contact-form

Contact form. The enterprise inquiry form: a carded column of labelled fields, topic radios, two custom selects, a textarea and the submit button. Measured and shot; never submitted.

Page: enterprise. Selector: `form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 904 x 952 |
| Padding | 64px 0px 64px 64px |
| Gap | 24px 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24.8px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | label.ff-fld-l: Inter 14px/20px 510, #1a1a1a |
| Transition | none |
| Icon | 0 x 0, colour #c4320a |
| Painted layers | input.ff-fld-i.astro-bgnjr626 410.0x44.0 bg #ffffff border T:1px #1a1a1a @ 0.12 / R:1px #1a1a1a @ 0.12 / B:1px #1a1a1a @ 0.12 / L:1px #1a1a1a @ 0.12 r 999px shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px; input.ff-fld-i.astro-bgnjr626 410.0x44.0 bg #ffffff border T:1px #1a1a1a @ 0.12 / R:1px #1a1a1a @ 0.12 / B:1px #1a1a1a @ 0.12 / L:1px #1a1a1a @ 0.12 r 999px shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px; input.ff-fld-i.astro-bgnjr626 410.0x44.0 bg #ffffff border T:1px #1a1a1a @ 0.12 / R:1px #1a1a1a @ 0.12 / B:1px #1a1a1a @ 0.12 / L:1px #1a1a1a @ 0.12 r 999px shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px; input.ff-fld-i.astro-bgnjr626 410.0x44.0 bg #ffffff border T:1px #1a1a1a @ 0.12 / R:1px #1a1a1a @ 0.12 / B:1px #1a1a1a @ 0.12 / L:1px #1a1a1a @ 0.12 r 999px shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px; input.ff-fld-i.astro-bgnjr626 410.0x44.0 bg #ffffff border T:1px #1a1a1a @ 0.12 / R:1px #1a1a1a @ 0.12 / B:1px #1a1a1a @ 0.12 / L:1px #1a1a1a @ 0.12 r 999px shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px; select.ff-fld-i 1.0x1.0 bg #ffffff image url(data:…) r 999px shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px |
| How | at rest |

Crops: `contact-form-default.png`.

#### field

Field wrapper. One form row: label (.ff-fld-l), the control (.ff-fld-i), an optional hint and the alert slot (.ff-fld-e).

Page: enterprise. Selector: `.ff-fld`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 410 x 72 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24.8px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | label.ff-fld-l: Inter 14px/20px 510, #1a1a1a |
| Transition | none |
| Painted layers | input.ff-fld-i.astro-bgnjr626 410.0x44.0 bg #ffffff border T:1px #1a1a1a @ 0.12 / R:1px #1a1a1a @ 0.12 / B:1px #1a1a1a @ 0.12 / L:1px #1a1a1a @ 0.12 r 999px shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px |
| How | at rest |

Crops: `field-default.png`.

#### field-label

Field label.

Page: enterprise. Selector: `.ff-fld-l`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 410 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 510 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: none.

#### text-field

Text field. A .ff-fld-i input: --ff-color-card fill, hairline border, radius-field-tall, --ff-shadow-field; focus paints --ff-shadow-field-focus. Text was typed and deleted; the form was never submitted.

Page: enterprise. Selector: `.ff-fld-i`. States: default, hover, focused, filled.

| Property | default | hover | focused | filled |
|---|---|---|---|---|
| Size (w x h) | 410 x 44 | = | = | = |
| Padding | 0px 18px | = | = | = |
| Border | 1px solid #1a1a1a @ 0.12 | = | 1px solid #1a1a1a @ 0.4 | 1px solid #1a1a1a @ 0.4 |
| Radius | 999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | = | #1a1a1a @ 0.06 0px 0px 0px 4px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | #1a1a1a @ 0.06 0px 0px 0px 4px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px |
| Outline | none | = | = | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1a1a1a | = | = | = |
| Transition | border-color, box-shadow 0.12s, 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s | = | = | = |
| Cursor | text | = | = | = |
| Placeholder | #6b6b6b @ 0.8, opacity 1 | = | = | = |
| Painted layers | input.ff-fld-i.astro-bgnjr626 410.0x44.0 bg #ffffff border T:1px #1a1a1a @ 0.12 / R:1px #1a1a1a @ 0.12 / B:1px #1a1a1a @ 0.12 / L:1px #1a1a1a @ 0.12 r 999px shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | = | input.ff-fld-i.astro-bgnjr626 410.0x44.0 bg #ffffff border T:1px #1a1a1a @ 0.4 / R:1px #1a1a1a @ 0.4 / B:1px #1a1a1a @ 0.4 / L:1px #1a1a1a @ 0.4 r 999px shadow #1a1a1a @ 0.06 0px 0px 0px 4px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | input.ff-fld-i.astro-bgnjr626 410.0x44.0 bg #ffffff border T:1px #1a1a1a @ 0.4 / R:1px #1a1a1a @ 0.4 / B:1px #1a1a1a @ 0.4 / L:1px #1a1a1a @ 0.4 r 999px shadow #1a1a1a @ 0.06 0px 0px 0px 4px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px |
| How | at rest | mouse hover | clicked into the field | typed "A habit tracker for two people", then deleted; nothing sent |

Crops: `text-field-hover.png`, `text-field-focused.png`, `text-field-filled.png`.

#### textarea

Text area.

Page: enterprise. Selector: `textarea.ff-fld-i`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 840 x 122 | = |
| Padding | 12px 18px | = |
| Border | 1px solid #1a1a1a @ 0.12 | 1px solid #1a1a1a @ 0.4 |
| Radius | 22px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | #1a1a1a @ 0.06 0px 0px 0px 4px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #1a1a1a | = |
| Transition | border-color, box-shadow 0.12s, 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s | = |
| Cursor | text | = |
| Placeholder | #6b6b6b @ 0.8, opacity 1 | = |
| Painted layers | textarea.ff-fld-i.astro-bgnjr626 840.0x122.0 bg #ffffff border T:1px #1a1a1a @ 0.12 / R:1px #1a1a1a @ 0.12 / B:1px #1a1a1a @ 0.12 / L:1px #1a1a1a @ 0.12 r 22px shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | textarea.ff-fld-i.astro-bgnjr626 840.0x122.0 bg #ffffff border T:1px #1a1a1a @ 0.4 / R:1px #1a1a1a @ 0.4 / B:1px #1a1a1a @ 0.4 / L:1px #1a1a1a @ 0.4 r 22px shadow #1a1a1a @ 0.06 0px 0px 0px 4px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px |
| How | at rest | clicked into the field |

Crops: `textarea-default.png`, `textarea-focused.png`.

#### radio

Topic radio. A native radio in the topic list; the checked state is the accent dot.

Page: enterprise. Selector: `input[name="topic"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 18 x 18 |
| Padding | 0px |
| Border | 1px solid #1a1a1a @ 0.3 |
| Radius | 50% |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Arial 13.3333px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | background-color, border-color 0.12s, 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s |
| Cursor | pointer |
| Placeholder | #000000, opacity 1 |
| Painted layers | input 18.0x18.0 bg #ffffff border T:1px #1a1a1a @ 0.3 / R:1px #1a1a1a @ 0.3 / B:1px #1a1a1a @ 0.3 / L:1px #1a1a1a @ 0.3 r 50% |
| How | at rest |

Crops: `radio-default.png`.

#### radio-checked

Topic radio, checked.

Page: enterprise. Selector: `input[name="topic"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 18 x 18 |
| Padding | 0px |
| Border | 1px solid #1a1a1a |
| Radius | 50% |
| Background | #1a1a1a |
| Box shadow | none |
| Outline | none |
| Font | Arial 13.3333px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | background-color, border-color 0.12s, 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s |
| Cursor | pointer |
| Placeholder | #000000, opacity 1 |
| ::after | 8px x 8px, static, bg #ffffff, radius 50% |
| Painted layers | input 18.0x18.0 bg #1a1a1a border T:1px #1a1a1a / R:1px #1a1a1a / B:1px #1a1a1a / L:1px #1a1a1a r 50%; input::after 8pxx8px bg #ffffff r 50% |
| How | at rest |

Crops: `radio-checked-default.png`.

#### select

Select (custom combobox). A role=combobox button styled as a field (.ff-fld-i.ff-sel-t); opens .ff-sel-p listbox of .ff-sel-o options. The native select behind it is kept at 1x1 off screen.

Page: enterprise. Selector: `button.ff-sel-t`. States: default, focused, hover, focus-visible, pressed.

| Property | default | focused | hover | focus-visible | pressed |
|---|---|---|---|---|---|
| Size (w x h) | 410 x 44 | - | = | = | = |
| Padding | 0px 44px 0px 18px | - | = | = | = |
| Border | 1px solid #1a1a1a @ 0.12 | - | = | 1px solid #1a1a1a @ 0.4 | = |
| Radius | 999px | - | = | = | = |
| Background | #ffffff | - | = | = | = |
| Background image | url(data:…) | - | = | = | = |
| Box shadow | #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | - | = | #1a1a1a @ 0.06 0px 0px 0px 4px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | = |
| Outline | none | - | = | = | = |
| Font | Inter 16px/24px 400 | - | = | = | = |
| Letter spacing | normal | - | = | = | = |
| Colour | #6b6b6b | - | = | = | = |
| Text node | span.ff-sel-v: Inter 16px/24px 400, #6b6b6b | - | = | = | = |
| Transition | border-color, box-shadow 0.12s, 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s | - | = | = | = |
| Cursor | default | - | = | = | = |
| Painted layers | button.ff-fld-i.ff-sel-t 410.0x44.0 bg #ffffff image url(data:…) border T:1px #1a1a1a @ 0.12 / R:1px #1a1a1a @ 0.12 / B:1px #1a1a1a @ 0.12 / L:1px #1a1a1a @ 0.12 r 999px shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | - | = | button.ff-fld-i.ff-sel-t 410.0x44.0 bg #ffffff image url(data:…) border T:1px #1a1a1a @ 0.4 / R:1px #1a1a1a @ 0.4 / B:1px #1a1a1a @ 0.4 / L:1px #1a1a1a @ 0.4 r 999px shadow #1a1a1a @ 0.06 0px 0px 0px 4px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | = |
| How | at rest | - | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Error | - | locator.click: Timeout 4000ms exceeded. Call log:   - waiting for locator('select.ff-fld-i').first().first()     - locator resolved to <select required="" tabindex="-1" class="ff-fld-i" id="contact-si | = | = | = |

Crops: `select-default.png`, `select-hover.png`, `select-focus-visible.png`.

#### select-trigger

Custom select trigger. A role=combobox button styled as a field (.ff-fld-i.ff-sel-t); opens .ff-sel-p listbox of .ff-sel-o options.

Page: enterprise. Selector: `button.ff-sel-t`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 410 x 44 | = | = | = |
| Padding | 0px 44px 0px 18px | = | = | = |
| Border | 1px solid #1a1a1a @ 0.12 | = | 1px solid #1a1a1a @ 0.4 | = |
| Radius | 999px | = | = | = |
| Background | #ffffff | = | = | = |
| Background image | url(data:…) | = | = | = |
| Box shadow | #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | = | #1a1a1a @ 0.06 0px 0px 0px 4px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | = |
| Outline | none | = | = | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6b6b6b | = | = | = |
| Text node | span.ff-sel-v: Inter 16px/24px 400, #6b6b6b | = | = | = |
| Transition | border-color, box-shadow 0.12s, 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | button.ff-fld-i.ff-sel-t 410.0x44.0 bg #ffffff image url(data:…) border T:1px #1a1a1a @ 0.12 / R:1px #1a1a1a @ 0.12 / B:1px #1a1a1a @ 0.12 / L:1px #1a1a1a @ 0.12 r 999px shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | = | button.ff-fld-i.ff-sel-t 410.0x44.0 bg #ffffff image url(data:…) border T:1px #1a1a1a @ 0.4 / R:1px #1a1a1a @ 0.4 / B:1px #1a1a1a @ 0.4 / L:1px #1a1a1a @ 0.4 r 999px shadow #1a1a1a @ 0.06 0px 0px 0px 4px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `select-trigger-default.png`, `select-trigger-hover.png`, `select-trigger-focus-visible.png`, `select-trigger-pressed.png`.

#### select-popup

Custom select listbox. The option popup: role=listbox card with option rows and the floating shadow.

Page: enterprise. Selector: `.ff-sel-p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 410 x 308 |
| Padding | 0px |
| Border | none |
| Radius | 20px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.08 0px 0px 0px 1px, #000000 @ 0.28 0px 24px 48px -20px |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | span: Inter 16px/24px 400, #6b6b6b |
| Transition | none |
| Painted layers | div.ff-sel-p 410.0x308.0 bg #ffffff r 20px shadow #000000 @ 0.08 0px 0px 0px 1px, #000000 @ 0.28 0px 24px 48px -20px; div.ff-sel-o.ff-sel-active 410.0x44.0 bg #1a1a1a @ 0.06 |
| How | at rest |

Crops: `select-popup-default.png`.

#### select-option

Custom select option.

Page: enterprise. Selector: `.ff-sel-o`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 410 x 44 | = |
| Padding | 10px 18px | = |
| Gap | 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #6b6b6b | = |
| Text node | span: Inter 16px/24px 400, #6b6b6b | = |
| Transition | none | = |
| Cursor | default | = |
| Ancestor paint | 1 up div.ff-sel-p bg #ffffff shadow #000000 @ 0.08 0px 0px 0px 1px, #000000 @ 0.28 0px 24px 48px -20px | = |
| How | at rest | mouse hover |

Crops: `select-option-default.png`, `select-option-hover.png`.

#### field-error

Field error text. The alert slot under a field ("Pick the topic that best fits."): role=alert, --ff-color-danger text. Rendered in the DOM at rest but not painted until validation, so this is the declared style of the slot, not an observed error.

Page: enterprise. Selector: `.ff-fld-e`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 0 x 0 |
| Padding | 0px |
| Gap | 6px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 13px/18px 400 |
| Letter spacing | normal |
| Colour | #c4320a |
| Transition | none |
| Icon | 0 x 0, colour #c4320a |
| How | at rest |

Crops: none.

#### submit

Submit button. The primary submit ("Submit"). Measured, never pressed — the form was never sent.

Page: enterprise. Selector: `button[data-ff-submit]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 94 x 44 | = | = | 91.19 x 42.68 |
| Padding | 0px 22px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | #1a1a1a | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1a1a1a offset 2px | = |
| Font | Inter 15px/23.25px 510 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | transform, background-color, box-shadow 0.12s, 0.12s, 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.ff-btn.ff-btn-primary 94.0x44.0 bg #1a1a1a r 999px | = | button.ff-btn.ff-btn-primary 94.0x44.0 bg #1a1a1a r 999px outline 2px solid #1a1a1a | button.ff-btn.ff-btn-primary 91.2x42.7 bg #1a1a1a r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.970101, 0, 0, 0.970101, 0, 0) |

Crops: `submit-default.png`, `submit-hover.png`, `submit-focus-visible.png`, `submit-pressed.png`.

### Content pages

#### cells-grid

Feature cells grid. The bordered feature grid on the studio/enterprise pages: hairline cells with an icon, a title and a line each.

Page: enterprise. Selector: `.ff-cells-grid`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1344 x 456 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #f5f5f5 |
| Box shadow | #000000 @ 0.08 0px 0px 0px 0.5px inset |
| Outline | none |
| Font | Inter 16px/24.8px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | h3: Inter 18px/26px 510, #1a1a1a, ls -0.252px |
| Transition | none |
| Painted layers | ul.ff-cells-grid.ff-cells-n3 1344.0x456.0 bg #f5f5f5 r 16px shadow #000000 @ 0.08 0px 0px 0px 0.5px inset; li 448.0x456.0 border L:1px #000000 @ 0.08; li 448.0x456.0 border L:1px #000000 @ 0.08 |
| How | at rest |

Crops: `cells-grid-default.png`.

#### studio-hero

Studio page display.

Page: studio. Selector: `main h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 505.42 x 67.97 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 66px/67.98px 600 |
| Letter spacing | -2.31px |
| Colour | #1a1a1a |
| Text node | span.ff-ln: Inter 66px/67.98px 600, #1a1a1a, ls -2.31px |
| Transition | none |
| How | at rest |

Crops: `studio-hero-default.png`.

#### ptag-studio

Studio product tag. The tinted product tag (.ff-ptag-studio): --ff-color-studio-tint ground, --ff-color-studio-ink label.

Page: studio. Selector: `.ff-ptag`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 134 x 24 |
| Padding | 0px 10px 0px 8px |
| Gap | 6px |
| Border | none |
| Radius | 999px |
| Background | #ececfd |
| Box shadow | none |
| Outline | none |
| Font | Inter 12px/16px 510 |
| Letter spacing | normal |
| Colour | #4b39ef |
| Transition | none |
| Painted layers | span.ff-ptag.ff-ptag-studio 134.0x24.0 bg #ececfd r 999px; span.ff-ptag-dot 7.0x7.0 bg #4b39ef r 50% |
| How | at rest |

Crops: `ptag-studio-default.png`.

#### cells-item

Feature cell.

Page: enterprise. Selector: `.ff-cells-grid > *`. States: default.

Not found on the page at capture time.

#### showcase-card

Showcase card. A published-app card in the Studio showcase grid. Hovered only; never opened.

Page: showcase. Selector: `main a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 303.61 x 624.52 | = |
| Padding | 0px | = |
| Gap | 20px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24.8px 400 | = |
| Letter spacing | normal | = |
| Colour | #1a1a1a | = |
| Text node | span.ff-awb.ff-awb-wrap: Inter 12px/16px 510, #1a1a1a | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 13 x 13, colour #1a1a1a | = |
| Painted layers | div.ff-phn-ap 240.0x503.2 bg #111113 r 36px shadow #4a4a4f 0px 0px 0px 0.96px inset, #7c7c82 0px 0px 0px 0.72px, #000000 @ 0.45 0px 24px 48px -28px; span.ff-awb.ff-awb-wrap 202.0x24.0 bg #ffffff r 999px shadow #000000 @ 0.08 0px 0px 0px 0.5px inset | = |
| How | at rest | mouse hover |

Crops: `showcase-card-default.png`, `showcase-card-hover.png`.

### Tabs and disclosure

#### tablist

Tab list. A vertical tablist ("Parts of the backend"): role=tab rows over tabpanels; the selected tab is filled.

Page: product. Selector: `.ff-tbs-tabs`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 376 x 220 |
| Padding | 0px |
| Border | T: 1px solid #000000 @ 0.08; R: none; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24.8px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | span.ff-tbs-n: Inter 15px/24px 510, #1a1a1a, ls -0.165px |
| Transition | none |
| Icon | 16 x 16, colour #1a1a1a |
| Painted layers | ul.ff-tbs-tabs 376.0x220.0 border T:1px #000000 @ 0.08; li 376.0x113.0 border B:1px #000000 @ 0.08; li 376.0x53.0 border B:1px #000000 @ 0.08; li 376.0x53.0 border B:1px #000000 @ 0.08 |
| How | at rest |

Crops: `tablist-default.png`.

#### tab-selected

Tab, selected. The aria-selected tab: filled with the tint wash.

Page: product. Selector: `[role="tab"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 376 x 112 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 8px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1a1a1a offset -2px | = |
| Font | Inter 15px/24px 510 | = | = | = |
| Letter spacing | -0.165px | = | = | = |
| Colour | #1a1a1a | = | = | = |
| Text node | span.ff-tbs-n: Inter 15px/24px 510, #1a1a1a, ls -0.165px | = | = | = |
| Transition | color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #1a1a1a | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button 376.0x112.0 r 8px outline 2px solid #1a1a1a | = |

Crops: `tab-selected-default.png`, `tab-selected-hover.png`, `tab-selected-focus-visible.png`.

#### tab

Tab. An unselected tab row. The selected state was reached by clicking it (a UI toggle).

Page: product. Selector: `[role="tab"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 376 x 52 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 8px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1a1a1a offset -2px | = |
| Font | Inter 15px/24px 510 | = | = | = |
| Letter spacing | -0.165px | = | = | = |
| Colour | #6b6b6b | #1a1a1a | = | #1a1a1a |
| Text node | span.ff-tbs-n: Inter 15px/24px 510, #6b6b6b, ls -0.165px | span.ff-tbs-n: Inter 15px/24px 510, #1a1a1a, ls -0.165px | = | span.ff-tbs-n: Inter 15px/24px 510, #1a1a1a, ls -0.165px |
| Transition | color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #6b6b6b | 16 x 16, colour #1a1a1a | = | 16 x 16, colour #1a1a1a |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button 376.0x52.0 r 8px outline 2px solid #1a1a1a | = |

Crops: `tab-hover.png`, `tab-focus-visible.png`, `tab-pressed.png`.

#### tab-after-click

Tab after selection. The same tab after the page's own click selected it.

Page: product. Selector: `[role="tab"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 376 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 15px/24px 510 |
| Letter spacing | -0.165px |
| Colour | #1a1a1a |
| Text node | span.ff-tbs-n: Inter 15px/24px 510, #1a1a1a, ls -0.165px |
| Transition | color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| Cursor | pointer |
| Icon | 16 x 16, colour #1a1a1a |
| How | at rest |

Crops: `tab-after-click-default.png`.

#### accordion-item-product

FAQ accordion item (product).

Page: product. Selector: `.ff-acc-item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 840 x 176 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #000000 @ 0.08; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24.8px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | summary: Inter 17px/26px 510, #1a1a1a, ls -0.204px |
| Transition | none |
| Icon | 21.21 x 21.21, colour #1a1a1a |
| Painted layers | details.ff-acc-item 840.0x176.0 border B:1px #000000 @ 0.08; span.ff-acc-x 39.6x39.6 bg #1a1a1a @ 0.06 r 50% |
| How | at rest |

Crops: `accordion-item-product-default.png`.

### Home (earlier skin)

#### replay-btn

Replay button. The small outline "Replay" control on the demo panels (.ff-pbtn-outline).

Page: product. Selector: `.ff-pbtn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 92 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | transparent | #bcbcbc | = | #bcbcbc |
| Box shadow | #dedede 0px 0px 0px 1px inset | #a3a3a3 0px 0px 0px 1px inset | = | #a3a3a3 0px 0px 0px 1px inset |
| Outline | none | = | 2px solid #1a1a1a offset 2px | = |
| Font | Inter 14px/21.7px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1a1a1a | = | = | = |
| Transition | background, box-shadow, opacity 0.15s, 0.15s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #1a1a1a | = | = | = |
| Painted layers | button.ff-pbtn.ff-pbtn-outline 92.0x32.0 r 24px shadow #dedede 0px 0px 0px 1px inset | button.ff-pbtn.ff-pbtn-outline 92.0x32.0 bg #bcbcbc r 24px shadow #a3a3a3 0px 0px 0px 1px inset | button.ff-pbtn.ff-pbtn-outline 92.0x32.0 r 24px shadow #dedede 0px 0px 0px 1px inset outline 2px solid #1a1a1a | button.ff-pbtn.ff-pbtn-outline 92.0x32.0 bg #bcbcbc r 24px shadow #a3a3a3 0px 0px 0px 1px inset |
| Ancestor paint | 1 up div.ff-rb.ff-drip bg oklch(0.9702 0 0) shadow #000000 @ 0.08 0px 0px 0px 1px, #000000 @ 0.22 0px 18px 40px -22px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `replay-btn-default.png`, `replay-btn-hover.png`, `replay-btn-focus-visible.png`, `replay-btn-pressed.png`.

#### home-hero

Home hero. The first band: the two-line display headline, the lede, the prompt composer and the check line, over the page ground with its grain texture.

Page: home. Selector: `.composer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1344 x 651.13 |
| Padding | 115.2px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24.8px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | span.os.ios: Inter 14px/20px 500, #555555 |
| Transition | none |
| Icon | 12.2 x 15, colour #1a1a1a |
| Painted layers | p.hx-plat 191.1x34.0 bg #ffffff @ 0.6 r 999px shadow #000000 @ 0.08 0px 0px 0px 1px inset; i 1.0x12.0 bg #1a1a1a @ 0.14; div.cmp-card.big 720.0x130.0 bg #ffffff border T:1px #1a1a1a @ 0.12 / R:1px #1a1a1a @ 0.12 / B:1px #1a1a1a @ 0.12 / L:1px #1a1a1a @ 0.12 r 22px shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px; span.cmp-caret 1.5x18.4 bg #6b6b6b @ 0.8; button.cmp-key 39.0x21.0 bg #fcfcfb border T:1px #000000 @ 0.07 / R:1px #000000 @ 0.07 / B:2px #000000 @ 0.07 / L:1px #000000 @ 0.07 r 6px; button.cmp-go 36.0x36.0 bg #1a1a1a @ 0.08 r 50% |
| How | at rest |

Crops: none.

#### home-title

Hero display. "Build an app by describing it" in the --ff-text-display size.

Page: home. Selector: `h1`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 427.05 x 135.94 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 66px/67.98px 600 | = |
| Letter spacing | -2.31px | = |
| Colour | #1a1a1a | #ededed |
| Text node | span.ln: Inter 66px/67.98px 600, #1a1a1a, ls -2.31px | span.ln: Inter 66px/67.98px 600, #ededed, ls -2.31px |
| Transition | none | = |
| How | at rest | footer theme switch set to Dark (data-theme="dark"), restored after |

Crops: `home-title-default.png`, `home-title-dark.png`.

#### btn-contrast

Contrast button (footer band). The "Talk to sales" pill in the closing band: the old skin's contrast fill.

Page: home. Selector: `.btn.btn-contrast`. States: default, hover, focus-visible, pressed, dark.

| Property | default | hover | focus-visible | pressed | dark |
|---|---|---|---|---|---|
| Size (w x h) | 135 x 44 | = | = | = | = |
| Padding | 0px 22px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 999px | = | = | = | = |
| Background | #1a1a1a | = | = | = | #ededed |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #0a68e0 offset 2px | = | = |
| Font | Inter 15px/23.25px 510 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | = | = | = | #111111 |
| Transition | transform, background-color, box-shadow 0.12s, 0.12s, 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s, 0s | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | a.btn.btn-contrast 135.0x44.0 bg #1a1a1a r 999px | = | a.btn.btn-contrast 135.0x44.0 bg #1a1a1a r 999px outline 2px solid #0a68e0 | = | a.btn.btn-contrast 135.0x44.0 bg #ededed r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | footer theme switch set to Dark (data-theme="dark"), restored after |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 0) | = |

Crops: `btn-contrast-default.png`, `btn-contrast-hover.png`, `btn-contrast-focus-visible.png`, `btn-contrast-pressed.png`, `btn-contrast-dark.png`.

#### btn-quiet

Quiet button. The secondary pill next to it.

Page: home. Selector: `.btn.btn-quiet`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 219 x 44 | = | = | = |
| Padding | 0px 22px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | #ffffff | #f0f0f0 | = | = |
| Box shadow | #000000 @ 0.08 0px 0px 0px 0.5px inset, #000000 @ 0.04 0px 1px 2px 0px | = | = | = |
| Outline | none | = | 2px solid #0a68e0 offset 2px | = |
| Font | Inter 15px/23.25px 510 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1a1a1a | = | = | = |
| Transition | transform, background-color, box-shadow 0.12s, 0.12s, 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.btn-quiet 219.0x44.0 bg #ffffff r 999px shadow #000000 @ 0.08 0px 0px 0px 0.5px inset, #000000 @ 0.04 0px 1px 2px 0px | a.btn.btn-quiet 219.0x44.0 bg #f0f0f0 r 999px shadow #000000 @ 0.08 0px 0px 0px 0.5px inset, #000000 @ 0.04 0px 1px 2px 0px | a.btn.btn-quiet 219.0x44.0 bg #ffffff r 999px shadow #000000 @ 0.08 0px 0px 0px 0.5px inset, #000000 @ 0.04 0px 1px 2px 0px outline 2px solid #0a68e0 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 0) |

Crops: `btn-quiet-default.png`, `btn-quiet-hover.png`, `btn-quiet-focus-visible.png`, `btn-quiet-pressed.png`.

#### replay-btn-home

Replay button (home skin). The small outline Replay on the demo modules; never painted at rest on this page, so this is the hidden DOM slot's declared style, not a painted reading.

Page: home. Selector: `.pbtn.outline`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 0 x 0 | - | - | = |
| Padding | 0px 12px | - | - | = |
| Gap | 6px | - | - | = |
| Border | none | - | - | = |
| Radius | 24px | - | - | = |
| Background | transparent | - | - | #ffffff |
| Box shadow | #dedede 0px 0px 0px 1px inset | - | - | #a3a3a3 0px 0px 0px 1px inset |
| Outline | none | - | - | = |
| Font | Inter 14px/21.7px 500 | - | - | = |
| Letter spacing | normal | - | - | = |
| Colour | #6b6b6b | - | - | #1a1a1a |
| Transition | background, box-shadow, opacity 0.15s, 0.15s, 0.2s ease, ease, ease delay 0s, 0s, 0s | - | - | = |
| Cursor | pointer | - | - | = |
| Icon | 0 x 0, colour #6b6b6b | - | - | 0 x 0, colour #1a1a1a |
| Painted layers | button.pbtn.outline 0.0x0.0 r 24px shadow #dedede 0px 0px 0px 1px inset | - | - | button.pbtn.outline 0.0x0.0 bg #ffffff r 24px shadow #a3a3a3 0px 0px 0px 1px inset |
| How | at rest | - | - | CDP forcePseudoState :active:hover |
| Error | - | locator.hover: Element is not visible Call log:   - waiting for locator('.pbtn.outline').first().first().first()     - locator resolved to <button hidden="" type="button" id="bx-replay" aria-label="Re | = | = |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: none.

#### app-card

Generated app card. A generated-app tile in the demo reel.

Page: home. Selector: `.apps`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 318 x 518 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24.8px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | span: -apple-system 10.3926px/10.3926px 600, #000000, ls -0.103926px |
| Transition | none |
| Icon | 11.22 x 7.48, colour #000000 |
| Painted layers | div.field 318.0x430.0 bg #f5f5f5 r 16px shadow #000000 @ 0.08 0px 0px 0px 0.5px inset; div.phone 241.7x508.4 bg #111113 r 38.67px shadow #4a4a4f 0px 0px 0px 0.96675px inset, #1c1c1f 0px 0px 0px 2.65856px inset, #7c7c82 0px 0px 0px 0.725062px, #000000 @ 0.45 0px 24px 60px -30px; div.screen 227.2x493.9 bg #f0f0f0 r 31.4194px; div::before.screen 67.6719pxx20.5312px bg #000000 r 999px; div::after.screen 227.188pxx64.2031px image linear-gradient(#000000 @ 0.42, #000000 @ 0) |
| How | at rest |

Crops: `app-card-default.png`.

#### ptag

Product tag chip. The small platform/product tag (dot + label).

Page: home. Selector: `.ff-ptag`. States: default.

Not found on the page at capture time.

### Mobile (390 wide)

#### m-nav

Top nav (390). The 390-wide bar: brand, the Open menu icon button.

Page: home. Selector: `.ff-snav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fcfcfb @ 0.86 |
| Box shadow | #000000 @ 0 0px 0.5px 0px 0px |
| Backdrop filter | blur(20px) saturate(1.3) |
| Outline | none |
| Font | Inter 16px/24.8px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | a.ff-btn.ff-btn-primary: Inter 13px/20.15px 510, #ffffff |
| Transition | box-shadow 0.24s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| Icon | 91.69 x 12.98, colour #1a1a1a, fill #000000 |
| Painted layers | header.ff-snav 390.0x56.0 bg #fcfcfb @ 0.86 shadow #000000 @ 0 0px 0.5px 0px 0px; div.ff-snav-panel 0.0x0.0 bg #ffffff r 12px shadow #000000 @ 0.08 0px 0px 0px 1px, #000000 @ 0.28 0px 24px 48px -20px; div.ff-snav-panel.ff-snav-panel-studio 0.0x0.0 bg #ffffff r 12px shadow #000000 @ 0.08 0px 0px 0px 1px, #000000 @ 0.28 0px 24px 48px -20px; a.ff-snav-lead 0.0x0.0 bg #f5f5f5 border R:1px #000000 @ 0.08 r 12px 0px 0px 12px; span.ff-ptag-dot.ff-ptag-studio 0.0x0.0 bg #4b39ef r 50%; span.ff-btn.ff-btn-primary 0.0x0.0 bg #1a1a1a r 999px |
| Ancestor paint | 1 up body bg #fcfcfb |
| How | at rest |

Crops: `m-nav-default.png`.

#### m-open-menu

Open menu button.

Page: home. Selector: `.ff-ibtn[aria-label="Open menu"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 50% | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1a1a1a offset 2px | = |
| Font | Inter 16px/24.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6b6b6b | = | = | = |
| Transition | background-color, color 0.12s, 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #6b6b6b | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.ff-ibtn 36.0x36.0 r 50% outline 2px solid #1a1a1a | = |

Crops: `m-open-menu-default.png`, `m-open-menu-hover.png`, `m-open-menu-focus-visible.png`, `m-open-menu-pressed.png`.

#### m-menu-close

Close menu button.

Page: home. Selector: `.ff-ibtn[aria-label="Close menu"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 50% | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1a1a1a offset 2px | = |
| Font | Inter 16px/24.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6b6b6b | = | = | = |
| Transition | background-color, color 0.12s, 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #6b6b6b | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.ff-ibtn 36.0x36.0 r 50% outline 2px solid #1a1a1a | = |

Crops: `m-menu-close-default.png`, `m-menu-close-hover.png`, `m-menu-close-focus-visible.png`, `m-menu-close-pressed.png`.

#### m-composer

Composer (390).

Page: home. Selector: `.composer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 170 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24.8px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | span.cmp-ghost-t: Inter 16px/24px 400, #6b6b6b @ 0.8 |
| Transition | none |
| Icon | 17 x 17, colour #6b6b6b |
| Painted layers | div.cmp-card.big 350.0x170.0 bg #ffffff border T:1px #1a1a1a @ 0.12 / R:1px #1a1a1a @ 0.12 / B:1px #1a1a1a @ 0.12 / L:1px #1a1a1a @ 0.12 r 22px shadow #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.14 0px 8px 24px -14px; span.cmp-caret 1.5x18.4 bg #6b6b6b @ 0.8; button.cmp-key 50.0x21.0 bg #fcfcfb border T:1px #000000 @ 0.07 / R:1px #000000 @ 0.07 / B:2px #000000 @ 0.07 / L:1px #000000 @ 0.07 r 6px; button.cmp-go 36.0x36.0 bg #1a1a1a @ 0.08 r 50% |
| How | at rest |

Crops: `m-composer-default.png`.

#### m-btn-primary

Primary button (390).

Page: home. Selector: `.ff-btn-primary`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 0 x 0 |
| Padding | 0px 12px |
| Gap | 8px |
| Border | none |
| Radius | 999px |
| Background | #1a1a1a |
| Box shadow | none |
| Outline | none |
| Font | Inter 13px/20.15px 510 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | transform, background-color, box-shadow 0.12s, 0.12s, 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s, 0s |
| Cursor | pointer |
| Painted layers | span.ff-btn.ff-btn-primary 0.0x0.0 bg #1a1a1a r 999px |
| Ancestor paint | 1 up a.ff-snav-lead bg #f5f5f5; 2 up div.ff-snav-panel.ff-snav-panel-studio bg #ffffff shadow #000000 @ 0.08 0px 0px 0px 1px, #000000 @ 0.28 0px 24px 48px -20px |
| How | at rest |

Crops: none.

#### m-hero-title

Hero display (390).

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 265.48 x 88.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 42px/44.1px 600 |
| Letter spacing | -1.47px |
| Colour | #1a1a1a |
| Text node | span.ln: Inter 42px/44.1px 600, #1a1a1a, ls -1.47px |
| Transition | none |
| How | at rest |

Crops: `m-hero-title-default.png`.

### Dialogs and overlays

#### m-menu-dialog

Mobile menu sheet. The full-screen dialog.ff-snav-ms opened by the menu button: nav links, the lead card and the sign-in row.

Page: home. Selector: `.ff-snav-ms`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fcfcfb |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24.8px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | a: Inter 22px/28px 510, #1a1a1a, ls -0.396px |
| Transition | none |
| Icon | 91.69 x 12.98, colour #1a1a1a, fill #000000 |
| Painted layers | dialog.ff-snav-ms 390.0x844.0 bg #fcfcfb; li 350.0x57.0 border B:1px #000000 @ 0.08; li 350.0x57.0 border B:1px #000000 @ 0.08; div.ff-snav-ms-foot 350.0x153.1 border T:1px #000000 @ 0.08; a.ff-btn.ff-btn-primary 350.0x44.0 bg #1a1a1a r 999px; a.ff-btn.ff-btn-secondary 350.0x44.0 bg #ffffff r 999px shadow #000000 @ 0.08 0px 0px 0px 0.5px inset, #000000 @ 0.04 0px 1px 2px 0px |
| Ancestor paint | 1 up body bg #fcfcfb |
| How | at rest |

Crops: `m-menu-dialog-default.png`.

## Transitions declared in the readable stylesheets

flutterflow.io's sheets are same-origin, so the CSSOM could read every rule; this list holds the transition and animation declarations on each measured page. The per-state Transition rows above are the computed values.

- home: `none`, `transform var(--d1) var(--ease-ui),background-color var(--d1) var(--ease-ui),box-shadow var(--d1) var(--ease-ui)`, `box-shadow var(--d2) var(--ease-ui)`, `color var(--d1) var(--ease-ui)`, `opacity .5s ease calc(var(--i, 0) * .1s),transform .9s var(--sp-soft) calc(var(--i, 0) * .1s)`, `background 0.25s`, `background 0.15s, box-shadow 0.15s, opacity 0.2s`, `opacity .35s ease,transform .6s var(--ease)`, `background-color .15s ease,color .15s ease,transform .15s var(--ease)`, `opacity .4s ease .1s,transform .6s var(--ease)`, `transform .55s cubic-bezier(.22,1,.36,1),opacity .3s ease calc(.1s + var(--i) * .09s),translate .8s var(--sp-soft) calc(.1s + var(--i) * .09s)`, `opacity 0.35s 1.05s`

- pricing: `transform var(--ff-duration-base) var(--ff-ease-ui)`, `none`, `transform var(--ff-duration-fast) var(--ff-ease-ui),background-color var(--ff-duration-fast) var(--ff-ease-ui),box-shadow var(--ff-duration-fast) var(--ff-ease-ui)`, `background 0.15s, box-shadow 0.15s, opacity 0.2s`, `background-color var(--ff-duration-fast) var(--ff-ease-ui),color var(--ff-duration-fast) var(--ff-ease-ui)`, `background-color var(--ff-duration-fast) var(--ff-ease-ui),border-color var(--ff-duration-fast) var(--ff-ease-ui)`, `transform var(--ff-duration-fast) var(--ff-ease-ui),background-color var(--ff-duration-fast) var(--ff-ease-ui)`, `color var(--ff-duration-fast) var(--ff-ease-ui),background-color var(--ff-duration-fast) var(--ff-ease-ui)`, `transform var(--ff-duration-base) var(--ff-ease-ui),width var(--ff-duration-base) var(--ff-ease-ui)`, `border-color var(--ff-duration-fast) var(--ff-ease-ui),box-shadow var(--ff-duration-fast) var(--ff-ease-ui)`, `background-color var(--ff-duration-fast) var(--ff-ease-ui),border-color var(--ff-duration-fast) var(--ff-ease-ui),color var(--ff-duration-fast) var(--ff-ease-ui)`, `background-color var(--d1, .12s) ease`
