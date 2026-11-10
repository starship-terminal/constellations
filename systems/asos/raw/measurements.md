# Component measurements

Computed styles read from asos.com on 2026-11-10 by `tools/capture/public/measure.mjs`, signed out, in headed Chrome at 1440 x 900 (the Mobile group at 390 x 844) in the site's one light theme — Akamai 403s headless browsers — with the OneTrust consent dialog hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### app-strip

App strip. The dark link at the very top right of the page, above the header.

Page: home. Selector: `[data-testid="download-app"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 194.45 x 30 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | #051a6e |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 14px/30px 600 |
| Letter spacing | 0.6px |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| Painted layers | a.eWFSkWC.ZHWKoMf 194.4x30.0 bg #051a6e |
| How | at rest |

Crops: `app-strip-default.png`.

#### header

Header. The black bar: white wordmark, WOMEN/MEN tabs, search field, account, saved and bag icons.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 140 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.eWFSkWC.ZHWKoMf: futura-pt 14px/30px 600, #ffffff, ls 0.6px |
| Transition | none |
| Icon | 16 x 16, colour #2d2d2d, fill #000000 |
| Painted layers | div.Fmy9ifd 0.0x0.0 bg #ffebcc; div::before.AIkY9uF 18pxx18px image url(data:…)'%3E %3Ctspan x='7.332' y='12'%3E!%3C/tspan%3E %3C/text%3E%3C/g%3E%3C/svg%3E"); div.vcXJfPO.fVdHxMU 1440.0x30.0 bg #f8f8f8; a.eWFSkWC.ZHWKoMf 194.4x30.0 bg #051a6e; li 51.0x30.0 border R:1px solid #dddddd / L:1px solid #dddddd; div.R9mnQSo 1440.0x60.0 bg #000000 |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo.

Page: home. Selector: `[data-testid="asoslogo"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 113 x 60 |
| Padding | 0px 20px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 14px/14px 400 |
| Letter spacing | 0.4px |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### nav-tab

Gender tab. WOMEN/MEN — the audience switch in the header.

Page: home. Selector: `[data-testid="women-floor"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 115 x 60 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset -2px | = |
| Font | futura-pt 14px/60px 900 | = | = | = |
| Letter spacing | 2px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.mQdrZay: futura-pt 14px/60px 900, #ffffff, ls 2px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.izvZA3y.fVdHxMU 115.0x60.0 bg #000000 | = | a.izvZA3y.fVdHxMU 115.0x60.0 bg #000000 outline 5px auto #005fcc offset -2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-tab-default.png`, `nav-tab-hover.png`, `nav-tab-focus-visible.png`, `nav-tab-pressed.png`.

#### nav-item

Category button. A button in the category nav row (New in, Clothing, Dresses…); each opens a flyout.

Page: plp. Selector: `[data-testid="primarynav-button"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 64.56 x 50 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #000000 | #051a6e | #051a6e | #051a6e |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset -2px | = |
| Font | futura-pt 14px/50px 400 | = | = | = |
| Letter spacing | 0.8px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: futura-pt 14px/50px 400, #ffffff, ls 0.8px | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | button.yI6sHXc.TYb4J9A 64.6x50.0 bg #000000 | button.yI6sHXc.TYb4J9A 64.6x50.0 bg #051a6e | button.yI6sHXc.TYb4J9A 64.6x50.0 bg #051a6e outline 5px auto #005fcc offset -2px | button.yI6sHXc.TYb4J9A 64.6x50.0 bg #051a6e |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`.

#### nav-mega

Category flyout, open. The nav button while its flyout is open.

Page: plp. Selector: `[data-testid="primarynav-button"]:hover`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 64.56 x 50 |
| Padding | 0px 10px |
| Border | none |
| Radius | 0px |
| Background | #051a6e |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 14px/50px 400 |
| Letter spacing | 0.8px |
| Colour | #ffffff |
| Text node | span: futura-pt 14px/50px 400, #ffffff, ls 0.8px |
| Transition | none |
| Cursor | default |
| Painted layers | button.yI6sHXc.TYb4J9A 64.6x50.0 bg #051a6e |
| How | flyout held open by opts.open |

Crops: `nav-mega-opened.png`.

#### search-input

Search field. The header search input; focused only, nothing typed.

Page: home. Selector: `[data-testid="search-input"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 764 x 38 | = |
| Padding | 0px 70px 0px 16px | = |
| Border | none | = |
| Radius | 19px 50% | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | 5px auto #005fcc offset -2px |
| Font | futura-pt 16px/16px 400 | = |
| Letter spacing | 0.4px | = |
| Colour | #2d2d2d | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #757575, opacity 1 | = |
| Painted layers | input.KRZT5cj.fVdHxMU 764.0x38.0 bg #ffffff r 19px / 50% | input.KRZT5cj.fVdHxMU 764.0x38.0 bg #ffffff r 19px / 50% outline 5px auto #005fcc offset -2px |
| Ancestor paint | 1 up div.MsBN5Ou bg #666666 | = |
| How | at rest | clicked into the field |

Crops: `search-input-default.png`, `search-input-focused.png`.

#### search-button

Search button. The magnifier at the end of the search field. Measured, never pressed.

Page: home. Selector: `[data-testid="search-button-inline"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 38 x 38 | = | - | = |
| Padding | 10px | = | - | = |
| Border | 1px solid #000000 @ 0 | = | - | = |
| Radius | 50% | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | futura-pt 14px/14px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #2d2d2d | = | - | = |
| Transition | background-color 0.3s ease | = | - | = |
| Cursor | default | = | - | = |
| Icon | 16 x 16, colour #2d2d2d, fill #000000 | = | - | = |
| Painted layers | button.vjmVpyd 38.0x38.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 50% | = | - | = |
| Ancestor paint | 1 up div.MsBN5Ou bg #666666 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Error | - | = | keyboard focus did not land on the element | = |

Crops: `search-button-default.png`, `search-button-hover.png`, `search-button-pressed.png`.

#### account-icon

Account icon. Opens the My Account dropdown (Sign In / Join); measured, never opened.

Page: home. Selector: `[data-testid="myAccountIcon"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50 x 60 | = | = | = |
| Padding | 12px 15px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset -2px | = |
| Font | futura-pt 0px/60px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.dejKRrj.c_IO2I_ 20.0x20.0 bg #ffffff | = | button.KH34gk4.TYb4J9A 50.0x60.0 outline 5px auto #005fcc offset -2px; span.dejKRrj.c_IO2I_ 20.0x20.0 bg #ffffff | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `account-icon-default.png`, `account-icon-hover.png`, `account-icon-focus-visible.png`, `account-icon-pressed.png`.

#### saved-icon

Saved-lists icon. The heart. Measured, never followed.

Page: home. Selector: `[data-testid="savedItemsIcon"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50 x 60 | = | = | = |
| Padding | 12px 15px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset -2px | = |
| Font | futura-pt 0px/60px 400 | = | = | = |
| Letter spacing | 0.4px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.vQeUV7s.c_IO2I_ 20.0x20.0 bg #ffffff | = | a.KH34gk4.TYb4J9A 50.0x60.0 outline 5px auto #005fcc offset -2px; span.vQeUV7s.c_IO2I_ 20.0x20.0 bg #ffffff | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `saved-icon-default.png`, `saved-icon-hover.png`, `saved-icon-focus-visible.png`, `saved-icon-pressed.png`.

#### bag-icon

Bag icon. "Bag 0 items". Measured, never followed.

Page: home. Selector: `[data-testid="miniBagIcon"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50 x 60 | = | = | = |
| Padding | 12px 15px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset -2px | = |
| Font | futura-pt 0px/60px 400 | = | = | = |
| Letter spacing | 0.4px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.LpoEdV8.c_IO2I_ 20.0x20.0 bg #ffffff | = | a.KH34gk4.TYb4J9A 50.0x60.0 outline 5px auto #005fcc offset -2px; span.LpoEdV8.c_IO2I_ 20.0x20.0 bg #ffffff | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `bag-icon-default.png`, `bag-icon-hover.png`, `bag-icon-focus-visible.png`, `bag-icon-pressed.png`.

#### promo-strip

Promo strip. The dark panel under the header carrying the new-customer offer and WOMEN/MEN toggle buttons.

Page: home. Selector: `leaf container:has-text("New here?")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1351 x 48 |
| Padding | 0px 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Futura-pt 13px/15px 400 |
| Letter spacing | 1px |
| Colour | #000000 |
| Text node | a.Button-module_button__0sgpT: Futura-pt 10.5625px/26px 700, #ffffff, ls 1px |
| Transition | none |
| Cursor | default |
| Painted layers | a.Button-module_button__0sgpT 100.0x30.0 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff; div.Tooltip-module_tooltip__f9BC8 720.0x72.0 bg #f2f2f2 shadow #696969 @ 0.5 3px 3px 0px 0px; div::before.Tooltip-module_tooltip__f9BC8 0pxx0px border R:5px solid #000000 @ 0 / B:5px solid #f2f2f2 / L:5px solid #000000 @ 0; a.Button-module_button__0sgpT 100.0x30.0 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff |
| Ancestor paint | 1 up div.Column-module_column__G41kz bg #2d2d2d |
| How | at rest |

Crops: `promo-strip-default.png`.

#### promo-tab

Promo strip tab. The bordered WOMEN/MEN buttons inside the promo strip.

Page: home. Selector: `inside promo strip: a/button "MEN"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 100 x 30 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 2px solid #ffffff | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Futura-pt 10.5625px/26px 700 | = | = | = |
| Letter spacing | 1px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | opacity 0.8s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.Button-module_button__0sgpT 100.0x30.0 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff | = | a.Button-module_button__0sgpT 100.0x30.0 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.563477 | 0.992271 | 0.593706 |

Crops: `promo-tab-default.png`, `promo-tab-hover.png`, `promo-tab-focus-visible.png`, `promo-tab-pressed.png`.

#### country-link

Country selector. "You're in Singapore Change" — a flag button in the top bar; opens the country picker, never pressed.

Page: home. Selector: `[data-testid="country-selector-btn"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 49 x 30 | = | = | = |
| Padding | 0px 17px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset -2px | = |
| Font | futura-pt 14px/14px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | pointer | = | pointer |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.breiRmE.TYb4J9A 49.0x30.0 outline 5px auto #005fcc offset -2px | = |

Crops: `country-link-default.png`, `country-link-hover.png`, `country-link-focus-visible.png`, `country-link-pressed.png`.

#### help-link

Help link. "Help & FAQs" in the top bar.

Page: home. Selector: `[data-testid="help"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 114.2 x 30 | = | = | = |
| Padding | 0px 19px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset -2px | = |
| Font | futura-pt 14px/30px 400 | = | = | = |
| Letter spacing | 0.4px | = | = | = |
| Colour | #666666 | #0770cf | #0770cf | #0770cf |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.R2BDZ6J.TYb4J9A 114.2x30.0 outline 5px auto #005fcc offset -2px | = |

Crops: `help-link-default.png`, `help-link-hover.png`, `help-link-focus-visible.png`, `help-link-pressed.png`.

#### nav-flyout

Category flyout panel. The open mega-menu panel itself, while the button is hovered.

Page: plp. Selector: `[data-testid="secondarynav-flyout"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1302 x 399.1 |
| Padding | 24px 10px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.t7yPX2W.TNLlZ7K: futura-pt 14px/20px 700, #000000, ls 0.8px |
| Transition | min-height 0.2s ease-in-out |
| Painted layers | nav.y39fWf8 1302.0x399.1 bg #ffffff; div.mI7C7np 48.0x48.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 50%; div.VU47dop.nU2sw3N 40.0x40.0 bg #eeeeee r 50%; div.mI7C7np 48.0x48.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 50%; div.VU47dop.nU2sw3N 40.0x40.0 bg #eeeeee r 50%; div.mI7C7np 48.0x48.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 50% |
| How | at rest |

Crops: `nav-flyout-default.png`.

#### flyout-link

Flyout link. A link inside the open mega-menu ("View all", "New In: Today"…). Measured, never followed.

Page: plp. Selector: `[data-testid="secondarynav-flyout"] [data-testid="text-link"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 68.38 x 28 | = | - | - |
| Padding | 8px 5px 0px 5px | = | - | - |
| Border | none | = | - | - |
| Radius | 0px | = | - | - |
| Background | transparent | = | - | - |
| Box shadow | none | = | - | - |
| Outline | none | = | - | - |
| Font | futura-pt 14px/29.96px 700 | = | - | - |
| Letter spacing | 0.8px | = | - | - |
| Colour | #666666 | #0770cf | - | - |
| Transition | none | = | - | - |
| Cursor | pointer | = | - | - |
| How | at rest | mouse hover | - | - |
| Error | - | = | locator.evaluate: Timeout 8000ms exceeded. Call log:   - waiting for locator('[data-testid="secondarynav-flyout"]').filter({ visible: true }).first().locator('[data-testid="text-link"]').filter({ visi | locator.evaluate: Timeout 8000ms exceeded. Call log:   - waiting for locator('[data-testid="secondarynav-flyout"]').filter({ visible: true }).first().locator('[data-testid="text-link"]').filter({ visi |

Crops: `flyout-link-default.png`, `flyout-link-hover.png`.

### Home

#### hero-cta

Hero CTA. The filled hero button ("SHOP WOMENS"). Measured, never followed.

Page: home. Selector: `a:has-text("SHOP WOMENS")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 184 x 44 | = | = | = |
| Padding | 9px 14px | = | = | = |
| Border | 2px solid #ffffff | 2px solid #000000 | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff | #000000 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | futura-pt 16px/22px 700 | = | = | = |
| Letter spacing | 2px | = | = | = |
| Colour | #000000 | #ffffff | = | = |
| Text node | span.cta__inner: futura-pt 16px/21px 700, #000000, ls 2px | span.cta__inner: futura-pt 16px/21px 700, #ffffff, ls 2px | = | = |
| Transition | background-color, border-color, color 0.4s, 0.4s, 0.4s ease, ease, ease-in-out delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.hero__cta.js-buttonHover 184.0x44.0 bg #ffffff border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff | a.hero__cta.js-buttonHover 184.0x44.0 bg #000000 border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 | a.hero__cta.js-buttonHover 184.0x44.0 bg #ffffff border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-cta-alt

Hero CTA, alternate.

Page: home. Selector: `a:has-text("SHOP MENS")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 184 x 44 | = | = | = |
| Padding | 9px 14px | = | = | = |
| Border | 2px solid #ffffff | 2px solid #000000 | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff | #000000 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | futura-pt 16px/22px 700 | = | = | = |
| Letter spacing | 2px | = | = | = |
| Colour | #000000 | #ffffff | = | = |
| Text node | span.cta__inner: futura-pt 16px/21px 700, #000000, ls 2px | span.cta__inner: futura-pt 16px/21px 700, #ffffff, ls 2px | = | = |
| Transition | background-color, border-color, color 0.4s, 0.4s, 0.4s ease, ease, ease-in-out delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.hero__cta.js-buttonHover 184.0x44.0 bg #ffffff border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff | a.hero__cta.js-buttonHover 184.0x44.0 bg #000000 border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 | a.hero__cta.js-buttonHover 184.0x44.0 bg #ffffff border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-alt-default.png`, `hero-cta-alt-hover.png`, `hero-cta-alt-focus-visible.png`, `hero-cta-alt-pressed.png`.

#### grid-tile

Content tile. A dark marketing tile lower on the home page ("NEW HERE?"…).

Page: home. Selector: `a.feature__link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 345 x 213.73 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | futura-pt 0px/0px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `grid-tile-default.png`, `grid-tile-hover.png`.

### Hub pages

#### hub-title

Hub section title. "The latest drops" — the hub's visible section heading (the h1 is screen-reader only).

Page: women. Selector: `h2:has-text("The latest drops")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 215.98 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 28px/36px 700 |
| Letter spacing | 1.2px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `hub-title-default.png`.

#### hub-tile

Hub hero tile. The "THE PARTY EDIT / SHOP NOW" campaign tile.

Page: women. Selector: `a.hero__link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1440 x 640 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | futura-pt 0px/0px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | h2.hero-title__text.js-dynamicText 0.0x0.0 bg #ffffff shadow #ffffff 10px 0px 0px 0px, #ffffff -10px 0px 0px 0px, #ffffff 10px 0px 0px 0px, #ffffff -10px 0px 0px 0px, #ffffff 10px 0px 0px 0px, #ffffff -10px 0px 0px 0px, #ffffff 10px 0px 0px 0px, #ffffff -10px 0px 0px 0px; h2.hero-title__text 0.0x0.0 bg #ffffff shadow #ffffff 10px 0px 0px 0px, #ffffff -10px 0px 0px 0px, #ffffff 10px 0px 0px 0px, #ffffff -10px 0px 0px 0px, #ffffff 10px 0px 0px 0px, #ffffff -10px 0px 0px 0px, #ffffff 10px 0px 0px 0px, #ffffff -10px 0px 0px 0px | = |
| How | at rest | mouse hover |

Crops: `hub-tile-default.png`, `hub-tile-hover.png`.

#### hub-banner

Hub promo banner. The dark "SINGLES' DAY — UP TO 40% OFF" banner under the header.

Page: women. Selector: `leaf container:has-text("UP TO 40% OFF")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 446.69 x 152.78 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.aria-invisible: futura-pt 16px/16px 400, #ffffff |
| Transition | none |
| Cursor | pointer |
| Painted layers | mark 92.2x39.3 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff |
| How | at rest |

Crops: `hub-banner-default.png`.

#### hub-card

Hub rail card. A product card in the "latest drops" rail.

Page: women. Selector: `main a:has(h2)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 446.69 x 152.78 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | futura-pt 16px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h2.aria-invisible: futura-pt 16px/16px 400, #ffffff | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.flexible-banner__background 1440.0x200.8 bg #2d2d2d; mark 92.2x39.3 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff | = |
| How | at rest | mouse hover |

Crops: `hub-card-default.png`, `hub-card-hover.png`.

### Shop grid

#### breadcrumb

Breadcrumb. Home / Women / New In / New In: Clothing.

Page: plp. Selector: `breadcrumb nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a: futura-pt 14px/20px 400, #2d2d2d, ls 0.6px |
| Transition | none |
| How | at rest |

Crops: `breadcrumb-default.png`.

#### plp-title

Collection title. "New In Clothing for Women" in Futura bold.

Page: plp. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 344.69 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 24px/30px 700 |
| Letter spacing | 1.7px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `plp-title-default.png`.

#### cat-pill

Category pill. A chip in the sub-category carousel ("New in: Today"…).

Page: plp. Selector: `:has-text("New in: Today")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 125.87 x 36 | = | = | = |
| Padding | 10px | = | = | = |
| Border | 1px solid #dddddd | 1px solid #999999 | = | 1px solid #999999 |
| Radius | 0px | = | = | = |
| Background | #ffffff | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | futura-pt 16px/14px 400 | = | = | = |
| Letter spacing | 1px | = | = | = |
| Colour | #2d2d2d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.pill_QzHek 125.9x36.0 bg #ffffff border T:1px solid #dddddd / R:1px solid #dddddd / B:1px solid #dddddd / L:1px solid #dddddd | a.pill_QzHek 125.9x36.0 bg #f5f5f5 border T:1px solid #999999 / R:1px solid #999999 / B:1px solid #999999 / L:1px solid #999999 | a.pill_QzHek 125.9x36.0 bg #ffffff border T:1px solid #dddddd / R:1px solid #dddddd / B:1px solid #dddddd / L:1px solid #dddddd outline 1px auto #005fcc offset 1px | a.pill_QzHek 125.9x36.0 bg #f5f5f5 border T:1px solid #999999 / R:1px solid #999999 / B:1px solid #999999 / L:1px solid #999999 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cat-pill-default.png`, `cat-pill-hover.png`, `cat-pill-focus-visible.png`, `cat-pill-pressed.png`.

#### sort-button

Sort control. The grid sort trigger. Measured, never opened.

Page: plp. Selector: `[data-testid="sort-button"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 92 x 43 | = | = | = |
| Padding | 7px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #dddddd | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | futura-pt 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.buttonLabel_TC2Dh: futura-pt 16px/16px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.button_q5Rog 92.0x43.0 border T:1px solid #dddddd / R:1px solid #dddddd / B:1px solid #dddddd / L:1px solid #dddddd; span::after.sort_rST8U 24pxx24px bg #2d2d2d | = | button.button_q5Rog 92.0x43.0 border T:1px solid #dddddd / R:1px solid #dddddd / B:1px solid #dddddd / L:1px solid #dddddd outline 1px auto #005fcc offset 0px; span::after.sort_rST8U 24pxx24px bg #2d2d2d | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sort-button-default.png`, `sort-button-hover.png`, `sort-button-focus-visible.png`, `sort-button-pressed.png`.

#### filter-button

Filter button. Opens the filter panel; measured, never opened.

Page: plp. Selector: `[data-testid="filter-button-desktop"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 92 x 43 | = | = | = |
| Padding | 7px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #dddddd | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | futura-pt 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.buttonLabel_TC2Dh: futura-pt 16px/16px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.button_q5Rog 92.0x43.0 border T:1px solid #dddddd / R:1px solid #dddddd / B:1px solid #dddddd / L:1px solid #dddddd; span::after.filter_YuD6a 24pxx24px bg #2d2d2d | = | button.button_q5Rog 92.0x43.0 border T:1px solid #dddddd / R:1px solid #dddddd / B:1px solid #dddddd / L:1px solid #dddddd outline 1px auto #005fcc offset 0px; span::after.filter_YuD6a 24pxx24px bg #2d2d2d | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filter-button-default.png`, `filter-button-hover.png`, `filter-button-focus-visible.png`, `filter-button-pressed.png`.

#### styles-count

Styles count. "2,697 styles found".

Page: plp. Selector: `:has-text("styles found")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 110.52 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 14px/20px 400 |
| Letter spacing | 0.5px |
| Colour | #666666 |
| Transition | none |
| How | at rest |

Crops: `styles-count-default.png`.

#### product-tile

Product tile. A grid card: image, save heart, name, price, MORE COLOURS / SELLING FAST badges.

Page: plp. Selector: `[class*="productTile"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 335 x 559.41 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | futura-pt 16px/0px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | p.productDescription_sryaw: futura-pt 14px/22px 400, #2d2d2d, ls 0.6px | = |
| Transition | none | = |
| Icon | 19.99 x 17.77, colour #2d2d2d, fill #000000 | = |
| Painted layers | div.badge_juy1n.productBadge_yGKk_ 106.0x20.0 bg #ffffff @ 0.8 border T:1px solid #dddddd / R:1px solid #dddddd / B:1px solid #dddddd / L:1px solid #dddddd; div.badge_juy1n.sellingFastBadge_AHx_Z 91.9x20.0 bg #666666; span.container_p0yFn.icon_xgNGS 38.0x37.0 bg #ffffff @ 0.8 border T:4px solid #000000 @ 0 / R:4px solid #000000 @ 0 / B:4px solid #000000 @ 0 / L:4px solid #000000 @ 0 r 50% outline 1px solid #000000 @ 0 offset 0px | = |
| How | at rest | mouse hover |

Crops: `product-tile-default.png`, `product-tile-hover.png`.

#### tile-name

Product link. The whole-card link inside the tile: image, name and price.

Page: plp. Selector: `a.productLink`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 335 x 559.41 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | futura-pt 16px/0px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.productDescription_sryaw: futura-pt 14px/22px 400, #2d2d2d, ls 0.6px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.badge_juy1n.productBadge_yGKk_ 106.0x20.0 bg #ffffff @ 0.8 border T:1px solid #dddddd / R:1px solid #dddddd / B:1px solid #dddddd / L:1px solid #dddddd; div.badge_juy1n.sellingFastBadge_AHx_Z 91.9x20.0 bg #666666 | = | a.productLink_KM4PI 335.0x559.4 outline 1px auto #005fcc offset 1px; div.badge_juy1n.productBadge_yGKk_ 106.0x20.0 bg #ffffff @ 0.8 border T:1px solid #dddddd / R:1px solid #dddddd / B:1px solid #dddddd / L:1px solid #dddddd; div.badge_juy1n.sellingFastBadge_AHx_Z 91.9x20.0 bg #666666 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tile-name-default.png`, `tile-name-hover.png`, `tile-name-focus-visible.png`, `tile-name-pressed.png`.

#### tile-price

Tile price. SGD pricing on the geo-served surface.

Page: plp. Selector: `:has-text("SGD$")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 335 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/0px 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Text node | span.price_m0bg_: futura-pt 14px/20px 700, #2d2d2d, ls 0.8px |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `tile-price-default.png`.

#### save-heart

Save heart. The heart on a product tile; a local save toggle, never pressed.

Page: plp. Selector: `tile button[aria-label*="Save"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 46 x 45 | = | = | = |
| Padding | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | futura-pt 16px/0px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 19.99 x 17.77, colour #2d2d2d, fill #000000 | = | = | = |
| Painted layers | span.container_p0yFn.icon_xgNGS 38.0x37.0 bg #ffffff @ 0.8 border T:4px solid #000000 @ 0 / R:4px solid #000000 @ 0 / B:4px solid #000000 @ 0 / L:4px solid #000000 @ 0 r 50% outline 1px solid #000000 @ 0 offset 0px | span.container_p0yFn.icon_xgNGS 38.0x37.0 bg #ffffff @ 0.8 border T:4px solid #000000 @ 0 / R:4px solid #000000 @ 0 / B:4px solid #000000 @ 0 / L:4px solid #000000 @ 0 r 50% shadow #2d2d2d @ 0.14 0px 2px 4px 0px outline 1px solid #000000 @ 0 offset 0px | span.container_p0yFn.icon_xgNGS 38.0x37.0 bg #ffffff @ 0.8 border T:4px solid #2d2d2d / R:4px solid #2d2d2d / B:4px solid #2d2d2d / L:4px solid #2d2d2d r 50% outline 1px solid #ffffff offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `save-heart-default.png`, `save-heart-hover.png`, `save-heart-focus-visible.png`, `save-heart-pressed.png`.

#### tile-badge

Tile badge. SELLING FAST or MORE COLOURS — the small status text under a tile.

Page: plp. Selector: `:has-text("SELLING FAST")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 335 x 100 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/0px 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Text node | p.productDescription_sryaw: futura-pt 14px/22px 400, #2d2d2d, ls 0.6px |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.badge_juy1n.productBadge_yGKk_ 106.0x20.0 bg #ffffff @ 0.8 border T:1px solid #dddddd / R:1px solid #dddddd / B:1px solid #dddddd / L:1px solid #dddddd; div.badge_juy1n.sellingFastBadge_AHx_Z 91.9x20.0 bg #666666 |
| How | at rest |

Crops: `tile-badge-default.png`.

#### load-more

Load more. The grid pagination button. Measured, never pressed.

Page: plp. Selector: `[data-auto-id="loadMoreProducts"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 300 x 54.5 | = | = | = |
| Padding | 15px | = | = | = |
| Border | 2px solid #dddddd | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff | = | = | #eeeeee |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | futura-pt 16px/normal 900 | = | = | = |
| Letter spacing | 2px | = | = | = |
| Colour | #2d2d2d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.loadButton_wWQ3F 300.0x54.5 bg #ffffff border T:2px solid #dddddd / R:2px solid #dddddd / B:2px solid #dddddd / L:2px solid #dddddd | = | a.loadButton_wWQ3F 300.0x54.5 bg #ffffff border T:2px solid #dddddd / R:2px solid #dddddd / B:2px solid #dddddd / L:2px solid #dddddd outline 1px auto #005fcc offset 1px | a.loadButton_wWQ3F 300.0x54.5 bg #eeeeee border T:2px solid #dddddd / R:2px solid #dddddd / B:2px solid #dddddd / L:2px solid #dddddd |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `load-more-default.png`, `load-more-hover.png`, `load-more-focus-visible.png`, `load-more-pressed.png`.

### undefined

#### pdp_url

PDP URL.

Page: pdp. Selector: ``. States: default.

| Property | default |
|---|---|
| Note | https://www.asos.com/arrange/arrange-velvet-plunge-halter-cinch-waist-maxi-dress-with-train-in-chocolate/prd/208967950#colourWayId-208967954 |

Crops: none.

### Product page

#### pdp-title

Product title.

Page: pdp. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 275.98 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 18px/24px 400 |
| Letter spacing | 0.6px |
| Colour | #2d2d2d |
| Transition | none |
| How | at rest |

Crops: `pdp-title-default.png`.

#### pdp-price

Product price.

Page: pdp. Selector: `[data-testid="product-price"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 299.98 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.ky6t2: futura-pt 16px/16px 400, #000000 |
| Transition | none |
| How | at rest |

Crops: `pdp-price-default.png`.

#### rating

Star rating. The 3.8 (30) review stars under the price.

Page: pdp. Selector: `[data-testid="rating-button"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 156.89 x 22.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 14px/20px 400 |
| Letter spacing | 0.6px |
| Colour | #2d2d2d |
| Text node | p.seSWD: futura-pt 14px/20px 400, #2d2d2d, ls 0.6px |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `rating-default.png`.

#### promo-banner

Promo banner. The light-blue strip "Get 20% off! With code: WOW" between price and colour.

Page: pdp. Selector: `[data-testid="promo-message-box"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 299.98 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #cde2f5 |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.XfX1K: futura-pt 14px/20px 400, #2d2d2d, ls 0.6px |
| Transition | none |
| Painted layers | div.MEwVh 300.0x44.0 bg #cde2f5 |
| How | at rest |

Crops: `promo-banner-default.png`.

#### colour-label

Colour label.

Page: pdp. Selector: `[data-testid="productColour"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 299.98 x 22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.iXWkL: futura-pt 12px/16px 700, #2d2d2d, ls 1px |
| Transition | none |
| How | at rest |

Crops: `colour-label-default.png`.

#### fit-link

Fit Assistant link. "Find your Fit Assistant size" beside SIZE:. Measured, never pressed.

Page: pdp. Selector: `[data-testid="fitAssistantLink"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 182.42 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | futura-pt 14px/20px 400 | = | = | = |
| Letter spacing | 0.6px | = | = | = |
| Colour | #2d2d2d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.agHJy 18.0x18.0 bg #060e89 r 9px | = | button.eJWsf 182.4x20.0 outline 1px auto #005fcc offset 0px; span.agHJy 18.0x18.0 bg #060e89 r 9px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `fit-link-default.png`, `fit-link-hover.png`, `fit-link-focus-visible.png`, `fit-link-pressed.png`.

#### size-select

Size select. The native "Please select" dropdown; a size was picked then restored, never submitted.

Page: pdp. Selector: `select`. States: default, focused, picked.

| Property | default | focused | picked |
|---|---|---|---|
| Size (w x h) | 299.98 x 38 | = | = |
| Padding | 7px 29.9922px 7px 8px | = | = |
| Border | 1px solid #555555 | = | = |
| Radius | 0px | = | = |
| Background | #ffffff | = | = |
| Background image | url(…) | = | = |
| Box shadow | none | = | = |
| Outline | none | 3px auto #005fcc offset 0px | = |
| Font | futura-pt 16px/22px 400 | = | = |
| Letter spacing | 0.4px | = | = |
| Colour | #2d2d2d | = | = |
| Transition | none | = | = |
| Cursor | default | = | = |
| Painted layers | select 300.0x38.0 bg #ffffff border T:1px solid #555555 / R:1px solid #555555 / B:1px solid #555555 / L:1px solid #555555 | select 300.0x38.0 bg #ffffff border T:1px solid #555555 / R:1px solid #555555 / B:1px solid #555555 / L:1px solid #555555 outline 3px auto #005fcc offset 0px | = |
| How | at rest | clicked into the field | selectOption index 1, then restored to index 0; nothing submitted |

Crops: `size-select-default.png`, `size-select-focused.png`, `size-select-picked.png`.

#### add-to-bag

Add to bag. The green buy button; measured in every state except a real press.

Page: pdp. Selector: `[data-testid="add-button"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 243.98 x 44 | = | = | = |
| Padding | 4px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #018849 | #006637 | = | #006637 |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px auto #005fcc offset 0px | = |
| Font | futura-pt 16px/22px 700 | = | = | = |
| Letter spacing | 0.6px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.MRMAA: futura-pt 16px/22px 700, #ffffff, ls 0.6px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.jAEfQ.LLfrW 244.0x44.0 bg #018849 | button.jAEfQ.LLfrW 244.0x44.0 bg #006637 | button.jAEfQ.LLfrW 244.0x44.0 bg #018849 outline 3px auto #005fcc offset 0px | button.jAEfQ.LLfrW 244.0x44.0 bg #006637 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `add-to-bag-default.png`, `add-to-bag-hover.png`, `add-to-bag-focus-visible.png`, `add-to-bag-pressed.png`.

#### save-button

Save for later. The heart button beside Add to bag; a local save toggle, never pressed.

Page: pdp. Selector: `[data-testid="saveForLater"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #eeeeee | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | futura-pt 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.AGXyD.GIdCP 44.0x44.0 bg #eeeeee r 100px | = | button.AGXyD.GIdCP 44.0x44.0 bg #eeeeee r 100px outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `save-button-default.png`, `save-button-hover.png`, `save-button-focus-visible.png`, `save-button-pressed.png`.

#### delivery-link

Delivery link.

Page: pdp. Selector: `[data-testid="deliveryAndReturns__termsLink"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 220.37 x 17.5 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | futura-pt 14px/20px 400 | = | = | = |
| Letter spacing | 0.6px | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | span.jWCNS: futura-pt 14px/20px 400, #2d2d2d, ls 0.6px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 220.4x17.5 outline 1px auto #005fcc offset 1px | = |

Crops: `delivery-link-default.png`, `delivery-link-hover.png`, `delivery-link-focus-visible.png`, `delivery-link-pressed.png`.

#### pdp-accordion

PDP accordion. A disclosure row (Size & Fit / Product Details / Brand).

Page: pdp. Selector: `[data-testid="product-description-section"] button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 299.98 x 44 | = | = | = |
| Padding | 14px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px auto #005fcc offset 0px | = |
| Font | futura-pt 14px/16px 700 | = | = | = |
| Letter spacing | 0.8px | = | = | = |
| Colour | #2d2d2d | = | = | = |
| Text node | span.accordion-item-module_titleText__rWfj1: futura-pt 14px/16px 700, #2d2d2d, ls 0.8px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.accordion-item-module_titleBtn__wIijl 300.0x44.0 outline 3px auto #005fcc offset 0px | = |

Crops: `pdp-accordion-default.png`, `pdp-accordion-hover.png`, `pdp-accordion-focus-visible.png`, `pdp-accordion-pressed.png`.

#### pdp-accordion-open

PDP accordion, open.

Page: pdp. Selector: `accordion button`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 299.98 x 44 |
| Padding | 14px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | 3px auto #005fcc offset 0px |
| Font | futura-pt 14px/16px 700 |
| Letter spacing | 0.8px |
| Colour | #2d2d2d |
| Text node | span.accordion-item-module_titleText__rWfj1: futura-pt 14px/16px 700, #2d2d2d, ls 0.8px |
| Transition | none |
| Cursor | pointer |
| Painted layers | button.accordion-item-module_titleBtn__wIijl 300.0x44.0 outline 3px auto #005fcc offset 0px |
| How | own toggle |

Crops: `pdp-accordion-open-opened.png`.

#### gallery-chevron

Gallery chevron. The prev/next control on the product gallery. Measured, never pressed.

Page: pdp. Selector: `[data-testid="imageGalleryChevrons"] button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66 x 65 | = | = | = |
| Padding | 15px 16px 15px 29px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | futura-pt 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, -32.5) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.sKOc0.fQCRy 66.0x65.0 outline 1px auto #005fcc offset 0px | = |

Crops: `gallery-chevron-default.png`, `gallery-chevron-hover.png`, `gallery-chevron-focus-visible.png`, `gallery-chevron-pressed.png`.

#### reviews-cta

Reviews CTA. "VIEW ALL REVIEWS" — measured, never pressed.

Page: pdp. Selector: `[data-testid="reviewsViewAll"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 359 x 44 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | 2px solid #dddddd | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff | #eeeeee | = | #eeeeee |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | futura-pt 16px/18px 700 | = | = | = |
| Letter spacing | 0.6px | = | = | = |
| Colour | #2d2d2d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.iOgob 359.0x44.0 bg #ffffff border T:2px solid #dddddd / R:2px solid #dddddd / B:2px solid #dddddd / L:2px solid #dddddd | button.iOgob 359.0x44.0 bg #eeeeee border T:2px solid #dddddd / R:2px solid #dddddd / B:2px solid #dddddd / L:2px solid #dddddd | button.iOgob 359.0x44.0 bg #ffffff border T:2px solid #dddddd / R:2px solid #dddddd / B:2px solid #dddddd / L:2px solid #dddddd outline 1px auto #005fcc offset 0px | button.iOgob 359.0x44.0 bg #eeeeee border T:2px solid #dddddd / R:2px solid #dddddd / B:2px solid #dddddd / L:2px solid #dddddd |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `reviews-cta-default.png`, `reviews-cta-hover.png`, `reviews-cta-focus-visible.png`, `reviews-cta-pressed.png`.

### Bag

#### bag-title

Bag title. "MY BAG".

Page: bag. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 362 x 66 |
| Padding | 44px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | url(data:…)%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cg%20id%3D%22M02B_empty_bag_signed_in%22%20transform%3D%22translate(0.000000%2C%20131.000000)%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cg%20id%3D%22ico |
| Box shadow | none |
| Outline | none |
| Font | futura-pt-n7 17.6px/22px 700 |
| Letter spacing | 2.5px |
| Colour | #2d2d2d |
| Transition | none |
| Painted layers | h1.empty-bag-title 362.0x66.0 image url(data:…)%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cg%20id%3D%22M02B_empty_bag_signed_ |
| How | at rest |

Crops: `bag-title-default.png`.

#### bag-empty

Bag body. The signed-out bag with nothing in it.

Page: bag. Selector: `main`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 455 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.empty-bag-title: futura-pt-n7 17.6px/22px 700, #2d2d2d, ls 2.5px |
| Transition | none |
| Painted layers | div.bag-contents-holder.bag-contents-holder-panel 1420.0x434.0 bg #ffffff; h1.empty-bag-title 362.0x66.0 image url(data:…)%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cg%20id%3D%22M02B_empty_bag_signed_; button.main-button 288.0x44.0 bg #018849 |
| How | at rest |

Crops: `bag-empty-default.png`.

#### bag-cta

Bag CTA. Measured, never followed.

Page: bag. Selector: `a:has-text("Shop")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 288 x 44 | = | = | = |
| Padding | 15px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #018849 | #006637 | #006637 | #006637 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | futura-pt-n7 14px/14px 700 | = | = | = |
| Letter spacing | 1.2px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.main-button 288.0x44.0 bg #018849 | button.main-button 288.0x44.0 bg #006637 | button.main-button 288.0x44.0 bg #006637 outline 1px auto #005fcc offset 0px | button.main-button 288.0x44.0 bg #006637 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `bag-cta-default.png`, `bag-cta-hover.png`, `bag-cta-focus-visible.png`, `bag-cta-pressed.png`.

### Saved lists

#### saved-title

Saved title.

Page: saved. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 221.35 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 18px/24px 700 |
| Letter spacing | 0.8px |
| Colour | #2d2d2d |
| Transition | none |
| How | at rest |

Crops: `saved-title-default.png`.

#### saved-empty

Saved body. Saved items is signed-out empty.

Page: saved. Selector: `main`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 444 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.noItemsTitle_uTxWD.title_uIMya: futura-pt 18px/24px 700, #2d2d2d, ls 0.8px |
| Transition | none |
| Icon | 24 x 24, colour #2d2d2d, fill #000000 |
| Painted layers | button.button_g2MO4.noItemsButton_DY_8I 288.0x44.0 bg #2d2d2d |
| How | at rest |

Crops: `saved-empty-default.png`.

#### saved-cta

Saved CTA. Measured, never followed.

Page: saved. Selector: `a:has-text("Sign in")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 288 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #2d2d2d | #000000 | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | futura-pt 16px/22px 700 | = | = | = |
| Letter spacing | 0.6px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.button_g2MO4.noItemsButton_DY_8I 288.0x44.0 bg #2d2d2d | button.button_g2MO4.noItemsButton_DY_8I 288.0x44.0 bg #000000 | button.button_g2MO4.noItemsButton_DY_8I 288.0x44.0 bg #2d2d2d outline 1px auto #005fcc offset 0px | button.button_g2MO4.noItemsButton_DY_8I 288.0x44.0 bg #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `saved-cta-default.png`, `saved-cta-hover.png`, `saved-cta-focus-visible.png`, `saved-cta-pressed.png`.

### Account gate

#### login-title

Login title. "Hi friend!"

Page: account. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 343 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 24px/30px 600 |
| Letter spacing | 1.2px |
| Colour | #2d2d2d |
| Transition | none |
| How | at rest |

Crops: `login-title-default.png`.

#### email-input

Email field. Text was typed and deleted; the form was never submitted.

Page: account. Selector: `input[name="email"]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 343 x 44 | = | = |
| Padding | 10px 8px 10px 16px | = | = |
| Border | 1px solid #767676 | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | 2px solid #0770cf offset -2px | 2px solid #0770cf offset -2px |
| Font | futura-pt 16px/22px 400 | = | = |
| Letter spacing | 0.4px | = | = |
| Colour | #2d2d2d | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #2d2d2d, opacity 1 | = | = |
| Painted layers | input.VuK4CecepGSeSwTkC1CQ 343.0x44.0 border T:1px solid #767676 / R:1px solid #767676 / B:1px solid #767676 / L:1px solid #767676 | input.VuK4CecepGSeSwTkC1CQ 343.0x44.0 border T:1px solid #767676 / R:1px solid #767676 / B:1px solid #767676 / L:1px solid #767676 outline 2px solid #0770cf offset -2px | input.VuK4CecepGSeSwTkC1CQ 343.0x44.0 border T:1px solid #767676 / R:1px solid #767676 / B:1px solid #767676 / L:1px solid #767676 outline 2px solid #0770cf offset -2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `email-input-default.png`, `email-input-focused.png`, `email-input-filled.png`.

#### continue-button

Continue button. The submit; measured except a real press — the form was never submitted.

Page: account. Selector: `button:has-text("CONTINUE")`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 343 x 48 | = | = |
| Padding | 8px 16px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | #2d2d2d | #000000 | #000000 |
| Box shadow | none | = | = |
| Outline | none | = | 1px solid #0770cf offset 3px |
| Font | futura-pt 16px/18px 600 | = | = |
| Letter spacing | 0.6px | = | = |
| Colour | #ffffff | = | = |
| Text node | span.button-module_content__jG0if: futura-pt 16px/18px 600, #ffffff, ls 0.6px | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.button-module_button__LoxGZ.button-module_primary__Vy8HB 343.0x48.0 bg #2d2d2d | button.button-module_button__LoxGZ.button-module_primary__Vy8HB 343.0x48.0 bg #000000 | button.button-module_button__LoxGZ.button-module_primary__Vy8HB 343.0x48.0 bg #000000 outline 1px solid #0770cf offset 3px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `continue-button-default.png`, `continue-button-hover.png`, `continue-button-focus-visible.png`.

#### social-button

Social sign-in button. Measured, never pressed.

Page: account. Selector: `button:has-text("GOOGLE")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 52 x 52 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | 2px solid #dddddd | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Background image | url(…) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #0770cf offset 3px | = |
| Font | futura-pt 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2d2d2d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button-module_button__LoxGZ.button-module_secondary__FWMDD 52.0x52.0 border T:2px solid #dddddd / R:2px solid #dddddd / B:2px solid #dddddd / L:2px solid #dddddd | = | a.button-module_button__LoxGZ.button-module_secondary__FWMDD 52.0x52.0 border T:2px solid #dddddd / R:2px solid #dddddd / B:2px solid #dddddd / L:2px solid #dddddd outline 1px solid #0770cf offset 3px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `social-button-default.png`, `social-button-hover.png`, `social-button-focus-visible.png`, `social-button-pressed.png`.

### Footer

#### footer

Footer.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 723.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.IoxIrTY: futura-pt 14px/16px 700, #ffffff, ls 0.8px |
| Transition | none |
| Painted layers | footer.Va6oZkc 1440.0x723.5 bg #000000; a.qQoHatg.sY3mB1c 1440.0x48.0 bg #051a6e; div.yoIGaVj.igCTEVJ 1440.0x625.5 bg #1f1e1e; div.czXbn_y 1440.0x625.5 bg #000000; div.IEEiAYL 1366.0x118.0 bg #000000; input.g_zQLNZ 566.5x38.5 bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1440 x 48 | = | = | = |
| Padding | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #051a6e | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | futura-pt 14px/16px 700 | = | = | = |
| Letter spacing | 0.8px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.IoxIrTY: futura-pt 14px/16px 700, #ffffff, ls 0.8px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.qQoHatg.sY3mB1c 1440.0x48.0 bg #051a6e | = | a.qQoHatg.sY3mB1c 1440.0x48.0 bg #051a6e outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Footer social icon.

Page: home. Selector: `[data-testid="social-link"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 30 x 30 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | futura-pt 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.cYGKXSQ 30.0x30.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

#### newsletter-input

Newsletter field. Focused only; never subscribed.

Page: home. Selector: `footer input[type="email"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 566.55 x 38.5 | = |
| Padding | 9px 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | 1px auto #005fcc offset 0px |
| Font | futura-pt 16px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #2d2d2d | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #757575, opacity 1 | = |
| Painted layers | input.g_zQLNZ 566.5x38.5 bg #ffffff | input.g_zQLNZ 566.5x38.5 bg #ffffff outline 1px auto #005fcc offset 0px |
| How | at rest | clicked into the field |

Crops: `newsletter-input-default.png`, `newsletter-input-focused.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.MPBSeA6.TNLlZ7K: futura-pt 14px/20px 700, #ffffff, ls 0.8px |
| Transition | none |
| Icon | 0 x 0, colour #2d2d2d, fill #000000 |
| Painted layers | div.Fmy9ifd 0.0x0.0 bg #ffebcc; div::before.AIkY9uF 18pxx18px image url(data:…)'%3E %3Ctspan x='7.332' y='12'%3E!%3C/tspan%3E %3C/text%3E%3C/g%3E%3C/svg%3E"); div.R9mnQSo 390.0x50.0 bg #000000; span.BKBoO9a.TYb4J9A 20.0x20.0 bg #ffffff; div.jgxJaMT 390.0x884.0 bg #2d2d2d @ 0.65; form.zel29Kx 0.0x0.0 bg #eeeeee |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button.

Page: home. Selector: `[data-testid="burger-menu-button"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 58 x 50 | = | = | = |
| Padding | 0px 18px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | futura-pt 14px/14px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.BKBoO9a.TYb4J9A 20.0x20.0 bg #ffffff | = | button.btUA6FL 58.0x50.0 outline 1px auto #005fcc offset 0px; span.BKBoO9a.TYb4J9A 20.0x20.0 bg #ffffff | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The button after its own toggle; the open drawer shows in the crop.

Page: home. Selector: `[data-testid="burger-menu-button"]`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 58 x 50 |
| Padding | 0px 18px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 14px/14px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Painted layers | span.BKBoO9a.TYb4J9A 20.0x20.0 bg #ffffff |
| How | own toggle |

Crops: `m-menu-open-opened.png`.

#### m-nav-link

Mobile nav link. A category row inside the opened side panel (NEW IN, CLOTHING…).

Page: home. Selector: `[data-testid="menu-item"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 288 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #eeeeee |
| Background image | url(…) |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/18px 900 |
| Letter spacing | 2px |
| Colour | #000000 |
| Text node | span: futura-pt 16px/18px 900, #2d2d2d, ls 2px |
| Transition | none |
| Cursor | pointer |
| Painted layers | button.OvxiwGm.nEgs3gH 288.0x96.0 bg #eeeeee |
| How | at rest |

Crops: `m-nav-link-default.png`.

#### m-floor-tab

Mobile floor tab. The WOMEN tab at the top of the open side panel.

Page: home. Selector: `[data-testid="women-floor"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 160 x 49 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 14px/50px 900 |
| Letter spacing | 2px |
| Colour | #ffffff |
| Text node | span.mQdrZay: futura-pt 14px/50px 900, #ffffff, ls 2px |
| Transition | none |
| Cursor | pointer |
| Painted layers | button.izvZA3y.fVdHxMU 160.0x49.0 bg #000000; span.mQdrZay 65.9x21.5 border B:2px solid #ffffff |
| How | at rest |

Crops: `m-floor-tab-default.png`.

#### m-search-icon

Mobile search icon. The magnifier that opens the search overlay (there is no inline field on mobile).

Page: home. Selector: `[data-testid="searchIcon"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50 x 50 | = | = | = |
| Padding | 12px 15px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset -2px | = |
| Font | futura-pt 0px/50px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.uszE8X4.c_IO2I_ 20.0x20.0 bg #ffffff | = | button.KH34gk4.TYb4J9A 50.0x50.0 outline 5px auto #005fcc offset -2px; span.uszE8X4.c_IO2I_ 20.0x20.0 bg #ffffff | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-search-icon-default.png`, `m-search-icon-hover.png`, `m-search-icon-focus-visible.png`, `m-search-icon-pressed.png`.

#### m-feature-tile

Mobile content tile. A dark marketing tile under the hero.

Page: home. Selector: `a.feature__link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 187 x 115.85 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 0px/0px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `m-feature-tile-default.png`.

## Transitions declared in the readable stylesheets

appwrite.io's bundle is served cross-origin from cdn.appwrite.io, so this list holds only what the CSSOM could read on each page (inline styles and same-origin sheets); the per-state Transition rows above are computed values and cover the bundle's rules.

- home: `opacity 0.3s linear`, `background-color 0.3s`, `opacity 0.3s ease-in`, `transform 0.2s`, `left 0.25s ease-out`, `opacity 0.4s`, `margin-left 0.5s ease-in-out`, `background-color 0.4s, border-color 0.4s, color 0.4s ease-in-out`, `height 0.5s`, `opacity 300ms`, `transform 200ms, right 200ms`, `opacity 0.3s`
