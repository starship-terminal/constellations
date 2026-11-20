# Component measurements

Computed styles read from www.grammarly.com on 2026-11-16 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Top nav. The fixed bar over every page: the Grammarly lockup, the Product/Work/Education/Resources menu buttons, the Pricing link, then Request a demo, Log in and the Sign Up pill.

Page: home. Selector: `header-global_headerStickyWrapper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 65 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Glyph 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1f243c |
| Text node | span.content_PbRSndwM: Glyph 14px/20px 400, #1c1c1c |
| Transition | none |
| Icon | 158 x 34, colour #0000ee |
| Painted layers | header.primaryHeaderBase_MLJ1wzb3 1440.0x65.0 bg #ffffff border B:1px #d9d9d9; button.base_PbRSndwM.paddingCompact_PbRSndwM 98.0x32.0 bg #ffffff @ 0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px; div.flyoutContainer_CLKm5yp3.flyoutContainerPrimary_CLKm5yp3 0.0x0.0 bg #ffffff shadow #878da2 @ 0.25 0px 2px 12px 0.5px, #878da2 @ 0.1 0px 1px 8px 0.5px, #878da2 @ 0.5 0px 0px 2px 0.5px, #878da2 0px 0px 0px 0.5px; div::after.flyoutFadeTop_CLKm5yp3 autox40px image linear-gradient(#ffffff, #000000 @ 0); li.columnContainer_CLKm5yp3 0.0x0.0 border R:1px #d9d9d9; div::after.flyoutFadeBottom_CLKm5yp3 autox40px image linear-gradient(0deg, #ffffff, #000000 @ 0) |
| How | at rest |

Crops: `header-default.png`.

#### brand

Brand lockup. The Grammarly mark + wordmark link in the nav start.

Page: home. Selector: `a.headerItemLogo_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 158 x 34 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Glyph 16px/normal 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Transition | none |
| Cursor | pointer |
| Icon | 158 x 34, colour #0000ee |
| Ancestor paint | 1 up header.primaryHeaderBase_MLJ1wzb3 bg #ffffff |
| How | at rest |

Crops: `brand-default.png`.

#### nav-menu-button

Nav menu button. A top-level menu trigger (Product): nav text with a chevron; opens the flyout panel.

Page: home. Selector: `header button:has-text("Product")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 98 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #ffffff @ 0 | transparent | = | transparent |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #027e6f offset 0px | = |
| Font | Glyph 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1c1c1c | = | = | = |
| Text node | span.content_PbRSndwM: Glyph 14px/20px 400, #1c1c1c | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 6, colour #1c1c1c | = | = | = |
| Painted layers | button.base_PbRSndwM.paddingCompact_PbRSndwM 98.0x32.0 bg #ffffff @ 0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px | button.base_PbRSndwM.paddingCompact_PbRSndwM 98.0x32.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px | button.base_PbRSndwM.paddingCompact_PbRSndwM 98.0x32.0 bg #ffffff @ 0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px outline 2px solid #027e6f | button.base_PbRSndwM.paddingCompact_PbRSndwM 98.0x32.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-menu-button-default.png`, `nav-menu-button-hover.png`, `nav-menu-button-focus-visible.png`, `nav-menu-button-pressed.png`.

#### nav-panel

Nav dropdown panel. The Product flyout: a floating panel with Learn and Use Grammarly columns of item rows.

Page: home. Selector: `flyout*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 667 x 463 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #878da2 @ 0.25 0px 2px 12px 0.5px, #878da2 @ 0.1 0px 1px 8px 0.5px, #878da2 @ 0.5 0px 0px 2px 0.5px, #878da2 0px 0px 0px 0.5px |
| Outline | none |
| Font | Glyph 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1f243c |
| Text node | span.columnLabel_CLKm5yp3.TS_dkKeNHYB: glyph 14px/21px 700, #1c1c1c, ls 0.5408px |
| Transition | none |
| Icon | 20 x 20, colour #0000ee |
| Painted layers | div.flyoutContainer_CLKm5yp3.flyoutContainerPrimary_CLKm5yp3 667.0x463.0 bg #ffffff shadow #878da2 @ 0.25 0px 2px 12px 0.5px, #878da2 @ 0.1 0px 1px 8px 0.5px, #878da2 @ 0.5 0px 0px 2px 0.5px, #878da2 0px 0px 0px 0.5px; div::after.flyoutFadeTop_CLKm5yp3 652pxx40px image linear-gradient(#ffffff, #000000 @ 0); li.columnContainer_CLKm5yp3 290.0x401.0 border R:1px #d9d9d9; div::after.flyoutFadeBottom_CLKm5yp3 652pxx40px image linear-gradient(0deg, #ffffff, #000000 @ 0) |
| How | at rest |

Crops: `nav-panel-default.png`.

#### nav-panel-item

Nav dropdown item.

Page: home. Selector: `flyout* a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 253 x 38 | = | - | = |
| Padding | 8px 16px | = | - | = |
| Border | none | = | - | = |
| Radius | 4px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | 1px solid #027e6f offset 0px | - | 1px solid #027e6f offset 0px |
| Font | Glyph 16px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #0000ee | = | - | #ff0000 |
| Text node | span.columnLinkLabel_CLKm5yp3: Glyph 14px/22px 400, #1c1c1c | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | Product flyout held open for the state | mouse hover | - | CDP forcePseudoState :active:hover |
| Painted layers | - | a.headerItemLink_CLKm5yp3.columnLink_CLKm5yp3 253.0x38.0 r 4px outline 1px solid #027e6f | = | a.headerItemLink_CLKm5yp3.columnLink_CLKm5yp3 253.0x38.0 r 4px outline 1px solid #027e6f |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-panel-item-default.png`, `nav-panel-item-hover.png`, `nav-panel-item-pressed.png`.

#### nav-link

Nav link. The plain text link in the bar (Pricing).

Page: home. Selector: `header a:has-text("Pricing")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 69 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #027e6f offset 1px | = |
| Font | Glyph 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1c1c1c | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.headerItemLink_CLKm5yp3.headerItemTopLevel_CLKm5yp3 69.0x32.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px | = | a.headerItemLink_CLKm5yp3.headerItemTopLevel_CLKm5yp3 69.0x32.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px outline 2px solid #027e6f | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-demo

Request a demo link. The secondary text link in the nav end. Measured, never followed.

Page: home. Selector: `header :text("Request a demo")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 132 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #027e6f offset 1px | = |
| Font | Glyph 14px/20px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1c1c1c | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.headerItemLink_CLKm5yp3.headerItemTopLevel_CLKm5yp3 132.0x32.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px | = | a.headerItemLink_CLKm5yp3.headerItemTopLevel_CLKm5yp3 132.0x32.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px outline 2px solid #027e6f | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-demo-default.png`, `nav-demo-hover.png`, `nav-demo-focus-visible.png`, `nav-demo-pressed.png`.

#### nav-login

Log in link. The plain sign-in link in the nav end. Measured, never followed.

Page: home. Selector: `header a:has-text("Log in")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #027e6f offset 1px | = |
| Font | Glyph 14px/20px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1c1c1c | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.headerItemLink_CLKm5yp3.headerItemTopLevel_CLKm5yp3 66.0x32.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px | = | a.headerItemLink_CLKm5yp3.headerItemTopLevel_CLKm5yp3 66.0x32.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px outline 2px solid #027e6f | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-signup

Sign Up (nav). The green pill in the nav end. Measured, never followed.

Page: home. Selector: `header :text("Sign Up")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 121 x 34 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 6px | = | = | = |
| Background | #027e6f | #014c43 | = | #014c43 |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px | = |
| Outline | none | = | 2px solid #027e6f offset 2px | = |
| Font | Glyph 14px/32px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | b: Glyph 14px/32px 700, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.base_PbRSndwM.paddingCompact_PbRSndwM 121.0x34.0 bg #027e6f border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px | a.base_PbRSndwM.paddingCompact_PbRSndwM 121.0x34.0 bg #014c43 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px | a.base_PbRSndwM.paddingCompact_PbRSndwM 121.0x34.0 bg #027e6f border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px shadow #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px outline 2px solid #027e6f | a.base_PbRSndwM.paddingCompact_PbRSndwM 121.0x34.0 bg #014c43 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signup-default.png`, `nav-signup-hover.png`, `nav-signup-focus-visible.png`, `nav-signup-pressed.png`.

### Buttons

#### btn-hero

Primary button (hero). The large green button under the hero ("Sign up It's free"): the brand fill, radius 6-ish, trailing arrow. Measured, never followed.

Page: home. Selector: `a:has-text("Sign up")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 60 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 6px | = | = | = |
| Background | #027e6f | #014c43 | = | #014c43 |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px | = |
| Outline | none | = | 2px solid #027e6f offset 2px | = |
| Font | Glyph 14px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | b: Glyph 14px/24px 700, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 11 x 10, colour #ffffff | = | = | = |
| Painted layers | a.base_PbRSndwM.paddingDefault_PbRSndwM 360.0x60.0 bg #027e6f border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px | a.base_PbRSndwM.paddingDefault_PbRSndwM 360.0x60.0 bg #014c43 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px | a.base_PbRSndwM.paddingDefault_PbRSndwM 360.0x60.0 bg #027e6f border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px shadow #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px outline 2px solid #027e6f | a.base_PbRSndwM.paddingDefault_PbRSndwM 360.0x60.0 bg #014c43 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `btn-hero-default.png`, `btn-hero-hover.png`, `btn-hero-focus-visible.png`, `btn-hero-pressed.png`.

#### btn-google

Secondary button (Google). The bordered white button beside the primary CTA ("Sign up with Google"): hairline border, the G mark, same radius. Measured, never followed.

Page: home. Selector: `:text("Sign up with Google")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 60 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | 1px solid #6d758d | 1px solid #027e6f | = | 1px solid #027e6f |
| Radius | 6px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | #027e6f 0px 0px 0px 1px | #ffffff 0px 0px 0px 2px, #005fcc 0px 0px 0px 4px | #027e6f 0px 0px 0px 1px |
| Outline | none | = | 2px solid #027e6f offset 2px | = |
| Font | Glyph 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #4d536e | = | = | = |
| Text node | span.base-module_text__avuxQ: Glyph 14px/32px 400, #4d536e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #4d536e | = | = | = |
| Painted layers | button.base-module_basic__zzy-b.base-module_colorWhiteHighContrastBorder__AdRXO 360.0x60.0 bg #ffffff border T:1px #6d758d / R:1px #6d758d / B:1px #6d758d / L:1px #6d758d r 6px | button.base-module_basic__zzy-b.base-module_colorWhiteHighContrastBorder__AdRXO 360.0x60.0 bg #ffffff border T:1px #027e6f / R:1px #027e6f / B:1px #027e6f / L:1px #027e6f r 6px shadow #027e6f 0px 0px 0px 1px | button.base-module_basic__zzy-b.base-module_colorWhiteHighContrastBorder__AdRXO 360.0x60.0 bg #ffffff border T:1px #6d758d / R:1px #6d758d / B:1px #6d758d / L:1px #6d758d r 6px shadow #ffffff 0px 0px 0px 2px, #005fcc 0px 0px 0px 4px outline 2px solid #027e6f | button.base-module_basic__zzy-b.base-module_colorWhiteHighContrastBorder__AdRXO 360.0x60.0 bg #ffffff border T:1px #027e6f / R:1px #027e6f / B:1px #027e6f / L:1px #027e6f r 6px shadow #027e6f 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `btn-google-default.png`, `btn-google-hover.png`, `btn-google-focus-visible.png`, `btn-google-pressed.png`.

#### btn-carousel

Carousel arrow button. The round Next arrow on the feature carousel (the Previous arrow sits collapsed at the start of the strip).

Page: home. Selector: `button.carousel_navButton*[aria-label="Next"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #545454 | = | = | = |
| Radius | 50% | = | = | = |
| Background | #f5f5f5 | #d9d9d9 | = | #d9d9d9 |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px | = |
| Outline | none | = | 3px solid #027e6f offset 2px | = |
| Font | Glyph 14px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #545454 | = | = | = |
| Transition | background-color, transform 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #545454 | = | = | = |
| Painted layers | button.base_PbRSndwM.paddingNone_PbRSndwM 48.0x48.0 bg #f5f5f5 border T:1px #545454 / R:1px #545454 / B:1px #545454 / L:1px #545454 r 50% | button.base_PbRSndwM.paddingNone_PbRSndwM 48.0x48.0 bg #d9d9d9 border T:1px #545454 / R:1px #545454 / B:1px #545454 / L:1px #545454 r 50% | button.base_PbRSndwM.paddingNone_PbRSndwM 48.0x48.0 bg #f5f5f5 border T:1px #545454 / R:1px #545454 / B:1px #545454 / L:1px #545454 r 50% shadow #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px outline 3px solid #027e6f | button.base_PbRSndwM.paddingNone_PbRSndwM 48.0x48.0 bg #d9d9d9 border T:1px #545454 / R:1px #545454 / B:1px #545454 / L:1px #545454 r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `btn-carousel-default.png`, `btn-carousel-hover.png`, `btn-carousel-focus-visible.png`, `btn-carousel-pressed.png`.

### Content and cards

#### hero

Hero title. The page's display line ("Think big. We'll take care of the details."): Matter, large size, tight tracking.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 890 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | matter 46px/50px 670 |
| Letter spacing | -0.46px |
| Colour | #0e101a |
| Transition | none |
| How | at rest |

Crops: `hero-default.png`.

#### hero-lede

Hero lede. The supporting line under the hero title.

Page: home. Selector: `h1 + *`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 890 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | glyph 18px/26px 400 |
| Letter spacing | normal |
| Colour | #0e101a |
| Transition | none |
| How | at rest |

Crops: `hero-lede-default.png`.

#### feature-card

Feature card. A card in the capability carousel ("Paragraph rewrites", "Tone suggestions"): a screenshot tile over a title and a lede, on the page ground.

Page: home. Selector: `card_card__*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 417.33 x 382.78 | 429.85 x 394.26 | 429.85 x 394.26 | 408.98 x 375.13 |
| Padding | 0px | = | = | = |
| Border | 1px solid #ebebeb | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | #000000 @ 0.16 0px 12px 32px 0px | = | #000000 @ 0.16 0px 12px 32px 0px |
| Outline | none | = | 3px solid #027e6f offset 3px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | h3.gds-typography.gds-heading: Matter 20.006px/24.0016px 600, #000000 | = | = | = |
| Transition | transform, box-shadow 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.card_card__E3sBu 417.3x382.8 bg #ffffff border T:1px #ebebeb / R:1px #ebebeb / B:1px #ebebeb / L:1px #ebebeb r 8px | button.card_card__E3sBu 429.8x394.3 bg #ffffff border T:1px #ebebeb / R:1px #ebebeb / B:1px #ebebeb / L:1px #ebebeb r 8px shadow #000000 @ 0.16 0px 12px 32px 0px | button.card_card__E3sBu 429.8x394.3 bg #ffffff border T:1px #ebebeb / R:1px #ebebeb / B:1px #ebebeb / L:1px #ebebeb r 8px outline 3px solid #027e6f | button.card_card__E3sBu 409.0x375.1 bg #ffffff border T:1px #ebebeb / R:1px #ebebeb / B:1px #ebebeb / L:1px #ebebeb r 8px shadow #000000 @ 0.16 0px 12px 32px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1.03, 0, 0, 1.03, 0, 0) | matrix(1.03, 0, 0, 1.03, 0, 0) | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `feature-card-default.png`, `feature-card-hover.png`, `feature-card-focus-visible.png`, `feature-card-pressed.png`.

#### stat-card

Customer stat card. A linked card in the dark enterprise strip ("20 days saved annually per user"): dark fill, a stat, a name. Measured, never followed.

Page: home. Selector: `scrollable-content_cardLinkWrapper*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 390 x 500 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | #545454 @ 0.08 0px 8px 20px 0px | = | #545454 @ 0.08 0px 8px 20px 0px |
| Outline | none | = | 2px solid #11a683 offset -4px | = |
| Font | Glyph 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0e101a | = | = | = |
| Text node | h3.HXL_dkKeNHYB.normalWeight_dkKeNHYB: matter 52px/58px 670, #0e101a, ls -0.52px | = | = | = |
| Transition | none | transform 0.2s ease-out | = | transform 0.2s ease-out |
| Cursor | pointer | = | = | = |
| Icon | 11 x 10, colour #0d8065 | = | = | = |
| Painted layers | a.scrollable-content_cardLinkWrapper__8Fc3t.scrollable-content_darkTheme__3VOwK 390.0x500.0 bg #ffffff r 8px | a.scrollable-content_cardLinkWrapper__8Fc3t.scrollable-content_darkTheme__3VOwK 390.0x500.0 bg #ffffff r 8px shadow #545454 @ 0.08 0px 8px 20px 0px | a.scrollable-content_cardLinkWrapper__8Fc3t.scrollable-content_darkTheme__3VOwK 390.0x500.0 bg #ffffff r 8px outline 2px solid #11a683 | a.scrollable-content_cardLinkWrapper__8Fc3t.scrollable-content_darkTheme__3VOwK 390.0x500.0 bg #ffffff r 8px shadow #545454 @ 0.08 0px 8px 20px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, -5) | = | matrix(1, 0, 0, 1, 0, -5) |

Crops: `stat-card-default.png`, `stat-card-hover.png`, `stat-card-focus-visible.png`, `stat-card-pressed.png`.

#### banner

Promo banner. The dark banner aside ("Try Grammarly Pro for free"): dark fill, white text and a pale CTA.

Page: home. Selector: `banner-component_banner*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 51.19 |
| Padding | 0px 14px |
| Border | none |
| Radius | 0px |
| Background | #00231f |
| Box shadow | none |
| Outline | none |
| Font | Glyph 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.banner-component_bannerLink__Nmkct: Matter 20px/normal 570, #ffffff |
| Transition | none |
| Icon | 14 x 12.72, colour #d5ff00 |
| Painted layers | aside.banner-component_banner__MvI88.bg-colors_darkThemeTextColor__F_yv_ 1440.0x51.2 bg #00231f |
| How | at rest |

Crops: `banner-default.png`.

#### section-dark

Dark section. A marketing section painted dark (bg-colors_darkThemeTextColor_*): ink ground with light text, reached without a theme switch.

Page: home. Selector: `page-section_*.bg-colors_darkThemeTextColor_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 469 |
| Padding | 96px 80px 0px 80px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Glyph 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.feature-highlight_eyebrowTextDarkMode__hpqce.TS_dkKeNHYB: glyph 14px/21px 400, #ffffff |
| Transition | none |
| Icon | 11 x 10, colour #1c1c1c |
| Painted layers | a.base_PbRSndwM.paddingDefault_PbRSndwM 193.0x60.0 bg #ffffff border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px; a.base_PbRSndwM.paddingDefault_PbRSndwM 161.0x60.0 bg #ffffff @ 0 border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 6px |
| How | at rest |

Crops: `section-dark-default.png`.

#### link-legal

Inline link. A text link inside body copy ("Terms and Conditions" under the hero buttons).

Page: home. Selector: `a:has-text("Terms")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 133 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 6px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #027e6f offset 1px | = |
| Font | glyph 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #027e6f | #016a5e | = | #014c43 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.link-color_linkDefault__xgSfW.link-color_styles2024__s1yEi 133.0x17.0 r 6px outline 2px solid #027e6f | = |

Crops: `link-legal-default.png`, `link-legal-hover.png`, `link-legal-focus-visible.png`, `link-legal-pressed.png`.

### Footer

#### footer

Footer. The site foot: link columns, the legal bar and the social icons.

Page: home. Selector: `footerContainer_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1188 |
| Padding | 16px 80px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Glyph 14px/normal 400 |
| Letter spacing | normal |
| Colour | #1f243c |
| Text node | div.columnLabel_DbPAKjMT: Glyph 14px/normal 700, #1f243c |
| Transition | none |
| Icon | 20 x 20, colour #1f243c |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 192 x 17.5 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Glyph 14px/17.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1f243c | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.item_GBat7YpO 192.0x17.5 outline 1px auto #101010 | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Pricing

#### billing-switch

Billing period switch. The Monthly/Yearly toggle that used to sit above the plan cards. Not present in the captured /plans markup — recorded as a gap.

Page: plans. Selector: `toggleInput_*`. States: .

Not found on the page at capture time.

#### plan-grid

Plan grid. The three-column plans list: Free, Pro (marked Most popular), Enterprise.

Page: plans. Selector: `boxItemsContainer_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1160 x 786 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Glyph 16px/normal 400 |
| Letter spacing | normal |
| Colour | #0e101a |
| Text node | span.bold_D4VnyDgq.TS_dkKeNHYB: glyph 14px/21px 700, #ffffff |
| Transition | none |
| Icon | 18 x 21, colour #ffffff |
| Painted layers | div.banner_D4VnyDgq 386.7x36.0 bg #027e6f r 8px 8px 0px 0px; div.boxItem_EW72gnlP.first_EW72gnlP 386.7x750.0 border T:1px #cdd1dc / B:1px #cdd1dc / L:1px #cdd1dc r 8px 0px 0px 8px; button.base_PbRSndwM.paddingCompact_PbRSndwM 305.7x48.0 bg #ffffff @ 0 border T:1px #027e6f / R:1px #027e6f / B:1px #027e6f / L:1px #027e6f r 6px; div.banner_D4VnyDgq.isRecommended_D4VnyDgq 386.7x36.0 bg #027e6f r 8px 8px 0px 0px; div.boxItem_EW72gnlP.recommended_EW72gnlP 386.7x750.0 bg #eafaf9 border T:1px #0d8065 / R:1px #0d8065 / B:1px #0d8065 / L:1px #0d8065; div.freeTagBase_BPzbCeRg 70.0x20.0 bg #eafaf9 border T:1px #73e1d4 / R:1px #73e1d4 / B:1px #73e1d4 / L:1px #73e1d4 r 4px |
| How | at rest |

Crops: `plan-grid-default.png`.

#### plan-card

Plan card (featured). The Pro column ($12 USD/month as captured): the "Most popular" green header bar, the price, the Try-for-free tag and its CTAs.

Page: plans. Selector: `planBoxContainer_* with $12`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 386.67 x 786 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Glyph 16px/normal 400 |
| Letter spacing | normal |
| Colour | #0e101a |
| Text node | span.bold_D4VnyDgq.TS_dkKeNHYB: glyph 14px/21px 700, #ffffff |
| Transition | none |
| Icon | 18 x 21, colour #ffffff |
| Painted layers | div.banner_D4VnyDgq.isRecommended_D4VnyDgq 386.7x36.0 bg #027e6f r 8px 8px 0px 0px; div.boxItem_EW72gnlP.recommended_EW72gnlP 386.7x750.0 bg #eafaf9 border T:1px #0d8065 / R:1px #0d8065 / B:1px #0d8065 / L:1px #0d8065; div.freeTagBase_BPzbCeRg 70.0x20.0 bg #eafaf9 border T:1px #73e1d4 / R:1px #73e1d4 / B:1px #73e1d4 / L:1px #73e1d4 r 4px; button.base_PbRSndwM.paddingCompact_PbRSndwM 304.7x48.0 bg #027e6f border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-card-plain

Plan card (plain). The Free column: quiet card next to the featured one.

Page: plans. Selector: `planBoxContainer_* first`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 386.67 x 786 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Glyph 16px/normal 400 |
| Letter spacing | normal |
| Colour | #0e101a |
| Text node | span.bold_D4VnyDgq.TS_dkKeNHYB: glyph 14px/21px 700, #ffffff |
| Transition | none |
| Icon | 18 x 21, colour #ffffff |
| Painted layers | div.banner_D4VnyDgq 386.7x36.0 bg #027e6f r 8px 8px 0px 0px; div.boxItem_EW72gnlP.first_EW72gnlP 386.7x750.0 border T:1px #cdd1dc / B:1px #cdd1dc / L:1px #cdd1dc r 8px 0px 0px 8px; button.base_PbRSndwM.paddingCompact_PbRSndwM 305.7x48.0 bg #ffffff @ 0 border T:1px #027e6f / R:1px #027e6f / B:1px #027e6f / L:1px #027e6f r 6px |
| How | at rest |

Crops: `plan-card-plain-default.png`.

#### sticker-tag

Try-for-free tag. The small tag beside the Pro price ("Try for free"): a pill tag with its own fill.

Page: plans. Selector: `freeTagText_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 60 x 18.02 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Glyph 12.04px/18.0152px 400 |
| Letter spacing | normal |
| Colour | #016a5e |
| Transition | none |
| Ancestor paint | 1 up div.freeTagBase_BPzbCeRg bg #eafaf9 |
| How | at rest |

Crops: none.

#### plan-cta-primary

Plan CTA (primary). The green CTA inside the Pro card. Measured, never followed.

Page: plans. Selector: `planBoxContainer_* :text("Try for $0.00")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 304.67 x 48 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 6px | = | = | = |
| Background | #027e6f | #014c43 | = | #014c43 |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px | = |
| Outline | none | = | 2px solid #027e6f offset 2px | = |
| Font | Glyph 16px/25px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Glyph 16px/25px 500, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.base_PbRSndwM.paddingCompact_PbRSndwM 304.7x48.0 bg #027e6f border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px | button.base_PbRSndwM.paddingCompact_PbRSndwM 304.7x48.0 bg #014c43 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px | button.base_PbRSndwM.paddingCompact_PbRSndwM 304.7x48.0 bg #027e6f border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px shadow #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px outline 2px solid #027e6f | button.base_PbRSndwM.paddingCompact_PbRSndwM 304.7x48.0 bg #014c43 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-primary-default.png`, `plan-cta-primary-hover.png`, `plan-cta-primary-focus-visible.png`, `plan-cta-primary-pressed.png`.

#### plan-cta-secondary

Plan CTA (secondary). The bordered CTA in a plan card (Create account / Contact Sales). Measured, never followed.

Page: plans. Selector: `planBoxContainer_* :text("Create account"), :text("Contact Sales")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 305.67 x 48 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Border | 1px solid #027e6f | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff @ 0 | = | = | = |
| Box shadow | none | #027e6f 0px 0px 0px 1px | #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px | #027e6f 0px 0px 0px 1px |
| Outline | none | = | 2px solid #027e6f offset 2px | = |
| Font | Glyph 16px/25px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #027e6f | = | = | = |
| Text node | span: Glyph 16px/25px 500, #027e6f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.base_PbRSndwM.paddingCompact_PbRSndwM 305.7x48.0 bg #ffffff @ 0 border T:1px #027e6f / R:1px #027e6f / B:1px #027e6f / L:1px #027e6f r 6px | button.base_PbRSndwM.paddingCompact_PbRSndwM 305.7x48.0 bg #ffffff @ 0 border T:1px #027e6f / R:1px #027e6f / B:1px #027e6f / L:1px #027e6f r 6px shadow #027e6f 0px 0px 0px 1px | button.base_PbRSndwM.paddingCompact_PbRSndwM 305.7x48.0 bg #ffffff @ 0 border T:1px #027e6f / R:1px #027e6f / B:1px #027e6f / L:1px #027e6f r 6px shadow #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px outline 2px solid #027e6f | button.base_PbRSndwM.paddingCompact_PbRSndwM 305.7x48.0 bg #ffffff @ 0 border T:1px #027e6f / R:1px #027e6f / B:1px #027e6f / L:1px #027e6f r 6px shadow #027e6f 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-secondary-default.png`, `plan-cta-secondary-hover.png`, `plan-cta-secondary-focus-visible.png`, `plan-cta-secondary-pressed.png`.

#### info-icon-button

Info icon button. The round "More information" icon button beside a row in the Compare Plans table.

Page: plans. Selector: `button.gds-icon-button-medium`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | #ebebeb | = | #ebebeb |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #027e6f offset 2px | = |
| Font | Glyph 14px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #707070 | #545454 | = | #545454 |
| Transition | background-color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #707070, fill #000000 @ 0 | 20 x 20, colour #545454, fill #000000 @ 0 | = | 20 x 20, colour #545454, fill #000000 @ 0 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.gds-button.gds-button-tertiary 32.0x32.0 bg #ebebeb r 6px | button.gds-button.gds-button-tertiary 32.0x32.0 r 6px outline 2px solid #027e6f | button.gds-button.gds-button-tertiary 32.0x32.0 bg #ebebeb r 6px |

Crops: `info-icon-button-default.png`, `info-icon-button-hover.png`, `info-icon-button-focus-visible.png`, `info-icon-button-pressed.png`.

#### faq-item

FAQ accordion item. A question row in the plans FAQ ("What will happen to my Premium subscription if I switch to Pro?"): a labelled row with a chevron that opens the answer. Never opened.

Page: plans. Selector: `[class$="-questions"] > div`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 700 x 60 |
| Padding | 16px |
| Border | 1px solid #e7e9f5 |
| Radius | 8px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Glyph 16px/normal 400 |
| Letter spacing | normal |
| Colour | #0e101a |
| Text node | a: glyph 18px/26px 400, #0e101a |
| Transition | none |
| Painted layers | div._2lKz7-section 700.0x60.0 bg #ffffff border T:1px #e7e9f5 / R:1px #e7e9f5 / B:1px #e7e9f5 / L:1px #e7e9f5 r 8px |
| How | at rest |

Crops: `faq-item-default.png`.

### Feature pages

#### tab-list

Feature tab list. The pill tabs over the feature demos (Paragraph rewrites, Proofreading, ...): a row of labelled tabs.

Page: features. Selector: `[role=tablist] / tabs_tabLabels_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 48 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #545454; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Glyph 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1f243c |
| Text node | span.TL_dkKeNHYB.normalWeight_dkKeNHYB: glyph 20px/30px 700, #2e2e2e |
| Transition | none |
| Painted layers | div.tabList_kMkqjCBX.tabs_tabLabels__v2c9T 1280.0x48.0 border B:1px #545454; button.base_PbRSndwM.paddingDefault_PbRSndwM 320.0x48.0 border B:2px #2e2e2e; button.base_PbRSndwM.paddingDefault_PbRSndwM 320.0x48.0 border B:2px #000000 @ 0; button.base_PbRSndwM.paddingDefault_PbRSndwM 320.0x48.0 border B:2px #000000 @ 0; button.base_PbRSndwM.paddingDefault_PbRSndwM 320.0x48.0 border B:2px #000000 @ 0 |
| How | at rest |

Crops: `tab-list-default.png`.

#### tab

Feature tab. One tab in the feature list. Measured and selected only through the tab itself.

Page: features. Selector: `button[role=tab].tabs_tabLabel_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 320 x 48 | = | = | = |
| Padding | 0px 0px 16px 0px | = | = | = |
| Border | T: none; R: none; B: 2px solid #2e2e2e; L: none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Glyph 18px/32px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2e2e2e | #0e101a | = | #0e101a |
| Text node | span.TL_dkKeNHYB.normalWeight_dkKeNHYB: glyph 20px/30px 700, #2e2e2e | span.TL_dkKeNHYB.normalWeight_dkKeNHYB: glyph 20px/30px 700, #0e101a | = | span.TL_dkKeNHYB.normalWeight_dkKeNHYB: glyph 20px/30px 700, #0e101a |
| Transition | color 0.4s ease | = | = | = |
| Cursor | pointer | default | = | default |
| Painted layers | button.base_PbRSndwM.paddingDefault_PbRSndwM 320.0x48.0 border B:2px #2e2e2e | = | button.base_PbRSndwM.paddingDefault_PbRSndwM 320.0x48.0 border B:2px #2e2e2e shadow #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tab-default.png`, `tab-hover.png`, `tab-focus-visible.png`, `tab-pressed.png`.

#### tab-selected

Feature tab, selected. The same tab measured after the page's own tab was pressed: the selected pill.

Page: features. Selector: `tabs_tabLabel*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 320 x 48 |
| Padding | 0px 0px 16px 0px |
| Border | T: none; R: none; B: 2px solid #2e2e2e; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Glyph 18px/32px 700 |
| Letter spacing | normal |
| Colour | #0e101a |
| Text node | span.TL_dkKeNHYB.normalWeight_dkKeNHYB: glyph 20px/30px 700, #0e101a |
| Transition | color 0.4s ease |
| Cursor | default |
| Painted layers | button.base_PbRSndwM.paddingDefault_PbRSndwM 320.0x48.0 border B:2px #2e2e2e |
| How | the page's own tab pressed (a UI toggle) |

Crops: `tab-selected-default.png`.

### Writing tools

#### tools-nav

Tools secondary nav. The sticky strip under the header on the free tools (Grammar Check, Plagiarism Checker, Paraphrasing Tool, ...): icon + label links, the current tool underlined.

Page: grammar-check. Selector: `tools-secondary-nav_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 46 |
| Padding | 0px 8px |
| Border | T: none; R: none; B: 1px solid #d9d9d9; L: none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Glyph 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1f243c |
| Text node | span.font-family-inter.tools-secondary-nav_navLinkText__TMlJ8: Inter 14px/21px 500, #1c1c1c |
| Transition | inset-block-start 0.3s ease |
| Icon | 20 x 20, colour #1c1c1c, fill #000000 @ 0 |
| Painted layers | aside.tools-secondary-nav_banner__M_DtN 1440.0x46.0 bg #ffffff border B:1px #d9d9d9; a::after.tools-secondary-nav_navLink__w9KxT.tools-secondary-nav_active__7KiiO 148pxx1px bg #1c1c1c |
| How | at rest |

Crops: `tools-nav-default.png`.

#### tools-nav-item

Tools nav item. One item in the tools strip; the first is the current page.

Page: grammar-check. Selector: `tools-secondary-nav_* a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 148 x 29 | = | = | = |
| Padding | 4px 8px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #027e6f offset 2px | = |
| Font | Glyph 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1c1c1c | = | = | = |
| Text node | span.font-family-inter.tools-secondary-nav_navLinkText__TMlJ8: Inter 14px/21px 500, #1c1c1c | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #1c1c1c, fill #000000 @ 0 | = | = | = |
| ::after | 148px x 1px, absolute, bg #1c1c1c, radius 0px | = | = | = |
| Painted layers | a::after.tools-secondary-nav_navLink__w9KxT.tools-secondary-nav_active__7KiiO 148pxx1px bg #1c1c1c | = | a.tools-secondary-nav_navLink__w9KxT.tools-secondary-nav_active__7KiiO 148.0x29.0 r 4px outline 2px solid #027e6f; a::after.tools-secondary-nav_navLink__w9KxT.tools-secondary-nav_active__7KiiO 148pxx1px bg #1c1c1c | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tools-nav-item-default.png`, `tools-nav-item-hover.png`, `tools-nav-item-focus-visible.png`, `tools-nav-item-pressed.png`.

### Grammar checker

#### checker

Checker frame. The free grammar checker: a two-column panel — the editor on the left, the Suggestions rail on the right.

Page: grammar-check. Selector: `checker frame`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 666 |
| Padding | 32px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Glyph 16px/normal 400 |
| Letter spacing | normal |
| Colour | #0e101a |
| Text node | h1.HL_dkKeNHYB.normalWeight_dkKeNHYB: matter 46px/50px 670, #0e101a, ls -0.46px |
| Transition | none |
| Icon | 0 x 0, colour #027e6f |
| Painted layers | div.container_ZJuFTATq 1000.0x384.0 bg #ffffff border T:1px #c6cbde / R:1px #c6cbde / B:1px #c6cbde / L:1px #c6cbde r 12px shadow #1a2134 @ 0.11 0px 12px 48px 0px; div.footerButtonsContainer_ZJuFTATq 0.0x0.0 border T:1px #c6cbde; button.base_PbRSndwM.paddingCompact_PbRSndwM 0.0x0.0 bg #ffffff @ 0 border T:1px #027e6f / R:1px #027e6f / B:1px #027e6f / L:1px #027e6f r 6px; div.grammarlyButton_ZJuFTATq 0.0x0.0 bg #191919 r 14px; div.container_kuFepaLr 300.0x382.0 bg #f9faff border L:1px #c6cbde; div.grammarlyButton_ZJuFTATq 28.0x28.0 bg #191919 r 14px |
| Ancestor paint | 1 up div.page-section_pagePaddingContainer1280__tQwLY.bg-colors_lightThemeTextColor__5AdyX bg #ffffff |
| How | at rest |

Crops: `checker-default.png`.

#### checker-editor

Editor area. The writing area with the "Start writing here" placeholder: a large bordered field.

Page: grammar-check. Selector: `[contenteditable]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 670 x 334 | = |
| Padding | 12px 15px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | inter 16px/28px 400 | = |
| Letter spacing | normal | = |
| Colour | #0e101a | = |
| Transition | none | = |
| ::before | 640px x 28px, absolute, bg #000000 @ 0, radius 0px | = |
| How | at rest | clicked into the field |

Crops: `checker-editor-default.png`, `checker-editor-focused.png`.

#### suggestions-panel

Suggestions rail (onboarding). The right rail of the free checker: the Suggestions header and the three-step "Let's get started" card shown to signed-out visitors.

Page: grammar-check. Selector: `contentContainer_* (get started)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 267 x 215 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Glyph 16px/normal 400 |
| Letter spacing | normal |
| Colour | #0e101a |
| Text node | div.TL_dkKeNHYB.bold_dkKeNHYB: glyph 20px/30px 700, #0e101a |
| Transition | none |
| Ancestor paint | 1 up div.container_kuFepaLr bg #f9faff |
| How | at rest |

Crops: `suggestions-panel-default.png`.

#### checker-filled

Editor, filled. The editor after a sample sentence was typed (then deleted): text in the field, issue underlines painted by the checker.

Page: grammar-check. Selector: `[contenteditable]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 670 x 334 |
| Padding | 12px 15px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | inter 16px/28px 400 |
| Letter spacing | normal |
| Colour | #0e101a |
| Text node | p: inter 16px/28px 400, #0e101a |
| Transition | none |
| How | sample text typed into the free checker; deleted after measuring, nothing submitted |

Crops: `checker-filled-default.png`.

#### suggestion-card

Suggestion card. A suggestion card in the rail (issue type, fix, Accept/Dismiss). The checker's issue underlines and cards are painted by a product overlay outside the page's light DOM; nothing matched in the signed-out run — recorded as a gap.

Page: grammar-check. Selector: `suggestionCard_*`. States: .

Not found on the page at capture time.

#### checker-cta

Get Grammarly CTA. The green CTA in the Suggestions rail. Measured, never followed.

Page: grammar-check. Selector: `:text("Get Grammarly")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 267 x 50 | = | = | = |
| Padding | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 6px | = | = | = |
| Background | #0d8065 | #006c51 | = | #006c51 |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #0d8065 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Glyph 14px/32px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.boldText_VGZWQT2b: Glyph 14px/32px 700, #ffffff | = | = | = |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.base_PbRSndwM.paddingDefault_PbRSndwM 267.0x50.0 bg #0d8065 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px | a.base_PbRSndwM.paddingDefault_PbRSndwM 267.0x50.0 bg #006c51 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px | a.base_PbRSndwM.paddingDefault_PbRSndwM 267.0x50.0 bg #0d8065 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px shadow #ffffff 0px 0px 0px 2px, #0d8065 0px 0px 0px 4px | a.base_PbRSndwM.paddingDefault_PbRSndwM 267.0x50.0 bg #006c51 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px |
| Ancestor paint | 1 up div.container_kuFepaLr bg #f9faff | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `checker-cta-default.png`, `checker-cta-hover.png`, `checker-cta-focus-visible.png`, `checker-cta-pressed.png`.

#### copy-button

Copy text button. The quiet button over the editor that copies the field's text (present in the DOM but collapsed when the editor's helper footer is hidden). Measured, never pressed.

Page: grammar-check. Selector: `:text("Copy text")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 0 x 0 | - | - | = |
| Padding | 0px 8px | - | - | = |
| Border | 1px solid #027e6f | - | - | = |
| Radius | 6px | - | - | = |
| Background | #ffffff @ 0 | - | - | = |
| Box shadow | none | - | - | #027e6f 0px 0px 0px 1px |
| Outline | none | - | - | = |
| Font | Glyph 14px/32px 400 | - | - | = |
| Letter spacing | normal | - | - | = |
| Colour | #027e6f | - | - | = |
| Transition | none | - | - | = |
| Cursor | pointer | - | - | = |
| Icon | 0 x 0, colour #027e6f | - | - | = |
| Painted layers | button.base_PbRSndwM.paddingCompact_PbRSndwM 0.0x0.0 bg #ffffff @ 0 border T:1px #027e6f / R:1px #027e6f / B:1px #027e6f / L:1px #027e6f r 6px | - | - | button.base_PbRSndwM.paddingCompact_PbRSndwM 0.0x0.0 bg #ffffff @ 0 border T:1px #027e6f / R:1px #027e6f / B:1px #027e6f / L:1px #027e6f r 6px shadow #027e6f 0px 0px 0px 1px |
| How | at rest | - | - | CDP forcePseudoState :active:hover |
| Error | - | locator.hover: Element is not visible Call log:   - waiting for locator('button, a').filter({ hasText: /^Copy text$/ }).first().first().first()     - locator resolved to <button type="button" data-sta | = | = |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: none.

#### getting-started

Get-started steps. The numbered steps inside the rail's onboarding card ("Add your text...", "Hover over the underlines...", "Click a suggestion...").

Page: grammar-check. Selector: `getStartedList_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 267 x 105 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Glyph 16px/normal 400 |
| Letter spacing | normal |
| Colour | #0e101a |
| Text node | span.listItemStep_kuFepaLr: glyph 14px/21px 700, #0e101a |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `getting-started-default.png`.

### Forms

#### form

Contact sales form. The lead form ("Contact our Sales team"): labelled required fields, selects and the Submit button.

Page: contact-sales. Selector: `form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 653.33 x 1142 |
| Padding | 32px 40px 40px 40px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Glyph 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1f243c |
| Text node | label.C4_dkKeNHYB.form_label__MvoCd: inter 14px/22px 400, #1f243c |
| Transition | none |
| Icon | 12 x 12, colour #6d758d |
| Painted layers | input.form_input__uMjtd 573.3x42.0 bg #ffffff border T:1px #646b81 / R:1px #646b81 / B:1px #646b81 / L:1px #646b81 r 4px; input.form_input__uMjtd 573.3x42.0 bg #ffffff border T:1px #646b81 / R:1px #646b81 / B:1px #646b81 / L:1px #646b81 r 4px; input.form_input__uMjtd 573.3x42.0 bg #ffffff border T:1px #646b81 / R:1px #646b81 / B:1px #646b81 / L:1px #646b81 r 4px; input.form_input__uMjtd 573.3x42.0 bg #ffffff border T:1px #646b81 / R:1px #646b81 / B:1px #646b81 / L:1px #646b81 r 4px; input.form_input__uMjtd 573.3x42.0 bg #ffffff border T:1px #646b81 / R:1px #646b81 / B:1px #646b81 / L:1px #646b81 r 4px; select.form_select__YEWkq 573.3x42.0 bg #ffffff border T:1px #646b81 / R:1px #646b81 / B:1px #646b81 / L:1px #646b81 r 4px |
| Ancestor paint | 1 up div.card_heroCard__5VWET.form_form__jakRN shadow #1a2134 @ 0.11 0px 12px 48px 0px |
| How | at rest |

Crops: `form-default.png`.

#### form-label

Field label. A field caption ("Work email*"): small text over the input.

Page: contact-sales. Selector: `label`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 573.33 x 22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | inter 14px/22px 400 |
| Letter spacing | normal |
| Colour | #1f243c |
| Transition | none |
| Cursor | default |
| Ancestor paint | 2 up div.card_heroCard__5VWET.form_form__jakRN shadow #1a2134 @ 0.11 0px 12px 48px 0px |
| How | at rest |

Crops: `form-label-default.png`.

#### form-input

Text field. A single-line input in the sales form: hairline border, placeholder only via the label. Text was typed and deleted; nothing sent.

Page: contact-sales. Selector: `form_input_*`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 573.33 x 42 | = | = |
| Padding | 8px 10px | = | = |
| Border | 1px solid #646b81 | 1px solid #2551da | 1px solid #d31332 |
| Radius | 4px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | 1px auto #101010 offset 0px | 1px auto #101010 offset 0px |
| Font | Arial 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000, opacity 1 | = | = |
| Painted layers | input.form_input__uMjtd 573.3x42.0 bg #ffffff border T:1px #646b81 / R:1px #646b81 / B:1px #646b81 / L:1px #646b81 r 4px | input.form_input__uMjtd 573.3x42.0 bg #ffffff border T:1px #2551da / R:1px #2551da / B:1px #2551da / L:1px #2551da r 4px outline 1px auto #101010 | input.form_input__uMjtd.form_inputError__hBtYr 573.3x42.0 bg #ffffff border T:1px #d31332 / R:1px #d31332 / B:1px #d31332 / L:1px #d31332 r 4px outline 1px auto #101010 |
| Ancestor paint | 2 up div.card_heroCard__5VWET.form_form__jakRN shadow #1a2134 @ 0.11 0px 12px 48px 0px | = | = |
| How | at rest | clicked into the field | typed "A short note about the launch", then deleted; nothing sent |

Crops: `form-input-default.png`, `form-input-focused.png`, `form-input-filled.png`.

#### form-select

Select. A dropdown in the sales form (institution type, product, country): same field skin with a chevron. Never opened.

Page: contact-sales. Selector: `form_select_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 573.33 x 42 | = | = | = |
| Padding | 8px 10px | = | = | = |
| Border | 1px solid #646b81 | = | 1px solid #2551da | 1px solid #2551da |
| Radius | 4px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Arial 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | select.form_select__YEWkq 573.3x42.0 bg #ffffff border T:1px #646b81 / R:1px #646b81 / B:1px #646b81 / L:1px #646b81 r 4px | = | select.form_select__YEWkq 573.3x42.0 bg #ffffff border T:1px #2551da / R:1px #2551da / B:1px #2551da / L:1px #2551da r 4px outline 1px auto #101010 | select.form_select__YEWkq 573.3x42.0 bg #ffffff border T:1px #2551da / R:1px #2551da / B:1px #2551da / L:1px #2551da r 4px |
| Ancestor paint | 3 up div.card_heroCard__5VWET.form_form__jakRN shadow #1a2134 @ 0.11 0px 12px 48px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `form-select-default.png`, `form-select-hover.png`, `form-select-focus-visible.png`, `form-select-pressed.png`.

#### form-submit

Submit button. The form's green Submit. Measured, never pressed.

Page: contact-sales. Selector: `button:has-text("Submit")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 93 x 60 | = | - | = |
| Padding | 16px 24px | = | - | = |
| Border | 1px solid #000000 @ 0 | = | - | = |
| Radius | 6px | = | - | = |
| Background | #f0f2fc | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Glyph 14px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #c6cbde | = | - | = |
| Text node | span.content_PbRSndwM: Glyph 14px/24px 400, #c6cbde | = | - | = |
| Transition | none | = | - | = |
| Cursor | not-allowed | = | - | = |
| Painted layers | button.base_PbRSndwM.paddingDefault_PbRSndwM 93.0x60.0 bg #f0f2fc border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px | = | - | = |
| Ancestor paint | 3 up div.card_heroCard__5VWET.form_form__jakRN shadow #1a2134 @ 0.11 0px 12px 48px 0px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `form-submit-default.png`, `form-submit-hover.png`, `form-submit-pressed.png`.

### Dialogs and overlays

#### signin-dialog

Sign-in card. The account card on /signin ("Sign in" with the email field and the provider buttons). Shot and measured, never submitted.

Page: signin. Selector: `main form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 396 x 202 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Glyph 16px/normal 400 |
| Letter spacing | normal |
| Colour | #0e101a |
| Text node | span.signin-module_noOutline__50kPn: Matter 24px/32px 400, #0e101a |
| Transition | none |
| Icon | 16 x 11, colour #000000 |
| Painted layers | div.default-module_inputAndSuffixContainer__Nyhe1 396.0x48.0 border T:1px #6d758d / R:1px #6d758d / B:1px #6d758d / L:1px #6d758d r 4px; input.base-module_input__cksud.default-module_input__TIXuN 394.0x46.0 bg #ffffff r 4px; div.default-module_inputAndSuffixContainer__Nyhe1 396.0x48.0 border T:1px #6d758d / R:1px #6d758d / B:1px #6d758d / L:1px #6d758d r 4px; input.base-module_input__cksud.default-module_input__TIXuN 394.0x46.0 bg #ffffff r 4px; button.base-module_basic__zzy-b.base-module_colorGreen24__mg5-X 396.0x48.0 bg #027e6f border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px |
| Ancestor paint | 2 up div.with_border-module_container__l-mTn bg #ffffff shadow #1a2134 @ 0.11 0px 12px 48px 0px |
| How | at rest |

Crops: `signin-dialog-default.png`.

#### signin-email

Email field. The sign-in email input: hairline border with the Email label inside. Text was typed and deleted; nothing sent.

Page: signin. Selector: `input[type=email] or base-module_input*`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 394 x 46 | = | = |
| Padding | 12px 12px 0px 12px | = | = |
| Border | none | = | = |
| Radius | 4px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | 2px solid #0b6a54 offset 2px | 2px solid #0b6a54 offset 2px |
| Font | Glyph 16px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000, opacity 1 | = | = |
| Painted layers | input.base-module_input__cksud.default-module_input__TIXuN 394.0x46.0 bg #ffffff r 4px | input.base-module_input__cksud.default-module_input__TIXuN 394.0x46.0 bg #ffffff r 4px outline 2px solid #0b6a54 | input.base-module_input__cksud.default-module_input__TIXuN 394.0x46.0 bg #ffffff r 4px outline 2px solid #0b6a54 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `signin-email-default.png`, `signin-email-focused.png`, `signin-email-filled.png`.

#### signin-continue

Continue button. The dialog's green primary. Measured, never pressed.

Page: signin. Selector: `button:has-text("Continue")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 396 x 48 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 6px | = | = | = |
| Background | #027e6f | #014c43 | = | #014c43 |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #027e6f 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Glyph 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.base-module_text__avuxQ: Glyph 14px/32px 700, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.base-module_basic__zzy-b.base-module_colorGreen24__mg5-X 396.0x48.0 bg #027e6f border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px | button.base-module_basic__zzy-b.base-module_colorGreen24__mg5-X 396.0x48.0 bg #014c43 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px | button.base-module_basic__zzy-b.base-module_colorGreen24__mg5-X 396.0x48.0 bg #027e6f border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px shadow #ffffff 0px 0px 0px 2px, #027e6f 0px 0px 0px 4px | button.base-module_basic__zzy-b.base-module_colorGreen24__mg5-X 396.0x48.0 bg #014c43 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px |
| Ancestor paint | 3 up div.with_border-module_container__l-mTn bg #ffffff shadow #1a2134 @ 0.11 0px 12px 48px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-continue-default.png`, `signin-continue-hover.png`, `signin-continue-focus-visible.png`, `signin-continue-pressed.png`.

#### signin-provider

Provider button. A social sign-in row (Google, Facebook, Apple, SSO): bordered, icon left, chevron right. Measured, never followed.

Page: signin. Selector: `:text("Sign in with Google")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 396 x 48 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | 1px solid #6d758d | = | = | = |
| Radius | 4px | = | = | = |
| Background | #ffffff | #f9faff | = | #f9faff |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #005fcc 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Glyph 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #4d536e | = | = | = |
| Text node | span.base-module_text__avuxQ.base-module_textWithArrow__G5bFo: Glyph 14px/32px 400, #4d536e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #4d536e | = | = | = |
| Painted layers | button.base-module_basic__zzy-b.base-module_colorWhiteHighContrastBorder__AdRXO 396.0x48.0 bg #ffffff border T:1px #6d758d / R:1px #6d758d / B:1px #6d758d / L:1px #6d758d r 4px | button.base-module_basic__zzy-b.base-module_colorWhiteHighContrastBorder__AdRXO 396.0x48.0 bg #f9faff border T:1px #6d758d / R:1px #6d758d / B:1px #6d758d / L:1px #6d758d r 4px | button.base-module_basic__zzy-b.base-module_colorWhiteHighContrastBorder__AdRXO 396.0x48.0 bg #ffffff border T:1px #6d758d / R:1px #6d758d / B:1px #6d758d / L:1px #6d758d r 4px shadow #ffffff 0px 0px 0px 2px, #005fcc 0px 0px 0px 4px | button.base-module_basic__zzy-b.base-module_colorWhiteHighContrastBorder__AdRXO 396.0x48.0 bg #f9faff border T:1px #6d758d / R:1px #6d758d / B:1px #6d758d / L:1px #6d758d r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-provider-default.png`, `signin-provider-hover.png`, `signin-provider-focus-visible.png`, `signin-provider-pressed.png`.

#### signin-help-link

Troubleshoot link. The quiet link under the primary ("Can't sign in?") and the "I don't have an account" link. Measured, never followed.

Page: signin. Selector: `:text("Can't sign in")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 144 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 2px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #027e6f offset 2px | = |
| Font | Glyph 14px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #027e6f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.gds-link.gds-link-primary 144.0x17.0 r 2px outline 2px solid #027e6f | = |

Crops: `signin-help-link-default.png`, `signin-help-link-hover.png`, `signin-help-link-focus-visible.png`, `signin-help-link-pressed.png`.

### Mobile (390 wide)

#### m-header

Top nav (mobile). The 390-wide header: lockup and the menu button.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 65 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Glyph 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1f243c |
| Transition | none |
| Icon | 149 x 32, colour #0000ee |
| Painted layers | header.primaryHeaderBase_MLJ1wzb3 390.0x65.0 bg #ffffff border B:1px #d9d9d9; button.base_PbRSndwM.paddingCompact_PbRSndwM 0.0x0.0 bg #ffffff @ 0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px; div.flyoutContainer_CLKm5yp3.flyoutContainerPrimary_CLKm5yp3 0.0x0.0 bg #ffffff shadow #878da2 @ 0.25 0px 2px 12px 0.5px, #878da2 @ 0.1 0px 1px 8px 0.5px, #878da2 @ 0.5 0px 0px 2px 0.5px, #878da2 0px 0px 0px 0.5px; div::after.flyoutFadeTop_CLKm5yp3 autox40px image linear-gradient(#ffffff, #000000 @ 0); div::after.flyoutFadeBottom_CLKm5yp3 autox40px image linear-gradient(0deg, #ffffff, #000000 @ 0); button.base_PbRSndwM.paddingCompact_PbRSndwM 0.0x0.0 bg #ffffff @ 0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The icon button that opens the mobile navigation sheet.

Page: home. Selector: `openButton_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 38 x 32 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff @ 0 | transparent | = | transparent |
| Box shadow | none | = | = | = |
| Outline | none | 1px solid #027e6f offset 0px | 2px solid #027e6f offset 0px | 1px solid #027e6f offset 0px |
| Font | Glyph 14px/32px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 22 x 13, colour #000000 | = | = | = |
| Painted layers | button.base_PbRSndwM.paddingCompact_PbRSndwM 38.0x32.0 bg #ffffff @ 0 r 6px | button.base_PbRSndwM.paddingCompact_PbRSndwM 38.0x32.0 r 6px outline 1px solid #027e6f | button.base_PbRSndwM.paddingCompact_PbRSndwM 38.0x32.0 bg #ffffff @ 0 r 6px outline 2px solid #027e6f | button.base_PbRSndwM.paddingCompact_PbRSndwM 38.0x32.0 r 6px outline 1px solid #027e6f |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu

Mobile menu. The open navigation sheet at 390: the link list and the sign-in row.

Page: home. Selector: `headerMobileMenu_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Glyph 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1f243c |
| Text node | span.content_PbRSndwM.headerItemExpandableButtonContent_CLKm5yp3: Glyph 14px/20px 400, #1c1c1c |
| Transition | visibility, transform 0.3s, 0.3s ease, ease-in delay 0s, 0s |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 149 x 32, colour #0000ee |
| Painted layers | nav.headerMobileMenu_kZ8afyJa.headerMobileMenuOpen_kZ8afyJa 390.0x844.0 bg #ffffff; div.headerMobileMenuTopContainer_kZ8afyJa 390.0x65.0 border B:1px #cdd1dc; button.base_PbRSndwM.paddingCompact_PbRSndwM 30.0x32.0 bg #ffffff @ 0 r 6px; li.headerMobileMenuListItem_kZ8afyJa 326.0x59.0 border B:1px #cdd1dc; button.base_PbRSndwM.paddingDefault_PbRSndwM 306.0x38.0 bg #ffffff @ 0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px; li.headerMobileMenuListItem_kZ8afyJa 326.0x59.0 border B:1px #cdd1dc |
| How | at rest |

Crops: none.

#### m-hero-btn

Primary button (mobile). The hero CTA at 390.

Page: home. Selector: `:text("Sign up")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 358 x 60 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 6px | = | = | = |
| Background | #027e6f | #014c43 | = | #014c43 |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px | = |
| Outline | none | = | 2px solid #027e6f offset 2px | = |
| Font | Glyph 14px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | b: Glyph 14px/24px 700, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 11 x 10, colour #ffffff | = | = | = |
| Painted layers | a.base_PbRSndwM.paddingDefault_PbRSndwM 358.0x60.0 bg #027e6f border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px | a.base_PbRSndwM.paddingDefault_PbRSndwM 358.0x60.0 bg #014c43 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px | a.base_PbRSndwM.paddingDefault_PbRSndwM 358.0x60.0 bg #027e6f border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px shadow #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px outline 2px solid #027e6f | a.base_PbRSndwM.paddingDefault_PbRSndwM 358.0x60.0 bg #014c43 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-hero-btn-default.png`, `m-hero-btn-hover.png`, `m-hero-btn-focus-visible.png`, `m-hero-btn-pressed.png`.

## Transitions declared in the readable stylesheets

grammarly.com's own CSS is served cross-origin (static-web.grammarly.com), so this list holds only what the CSSOM could read on each page (inline and same-origin styles); the per-state Transition rows above are computed values and cover Grammarly's own rules.
