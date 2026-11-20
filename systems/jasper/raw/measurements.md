# Component measurements

Computed styles read from jasper.ai on 2026-11-17 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844). The marketing site is Webflow. The login card on app.jasper.ai was measured at rest. Consent overlays were hidden, never answered. Written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The sticky marketing nav: wordmark, Platform, Solutions, Resources, Company, Pricing, Log in, Free Trial and Get a Demo.

Page: home. Selector: `.nav_contain`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 80 |
| Padding | 16px 20px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | ABC ROM 16px/22.4px 450 |
| Letter spacing | -0.16px |
| Colour | #00063d |
| Text node | div.nav_menu_text.u-text-style-main: ABC ROM 16px/22.4px 450, #00063d, ls -0.16px |
| Transition | none |
| Icon | 98.72 x 37.02, colour #fa4028 |
| Painted layers | div.nav_contain.u-grid-custom 1440.0x80.0 bg #ffffff; div.utility-1_menu 0.0x0.0 bg #ffffff; div.nav_menu_link_color.is-border 9.9x28.2 bg #ceebff; div.nav_menu_link_color.is-center 65.9x28.2 bg #ceebff; div.nav_menu_link_color.is-border 9.9x28.2 bg #ceebff; div.nav_menu_link_color.is-border 10.5x28.2 bg #ffb3a3 |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Jasper wordmark link.

Page: home. Selector: `.nav_contain a[href="/"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 98.72 x 37.02 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC ROM 16px/22.4px 450 |
| Letter spacing | -0.16px |
| Colour | #fa4028 |
| Transition | none |
| Cursor | pointer |
| Icon | 98.72 x 37.02, colour #fa4028 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-item

Nav item. A header menu item (Platform). Hover opens its dropdown. Measured, never followed.

Page: home. Selector: `.nav_menu_link "Platform"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.69 x 28.17 | = | - | = |
| Padding | 8px 12px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | ABC ROM 16px/22.4px 450 | = | - | = |
| Letter spacing | -0.16px | = | - | = |
| Colour | #00063d | = | - | = |
| Text node | div.nav_menu_text.u-text-style-main: ABC ROM 16px/22.4px 450, #00063d, ls -0.16px | = | - | = |
| Transition | none | = | - | = |
| Painted layers | div.nav_menu_link_color.is-border 9.9x28.2 bg #ceebff; div.nav_menu_link_color.is-center 65.9x28.2 bg #ceebff; div.nav_menu_link_color.is-border 9.9x28.2 bg #ceebff | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-pressed.png`.

#### nav-link

Nav link. The Pricing header link.

Page: home. Selector: `a "Pricing"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 74.59 x 28.17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #00063d offset 3px | = |
| Font | ABC ROM 16px/22.4px 450 | = | = | = |
| Letter spacing | -0.16px | = | = | = |
| Colour | #00063d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.g_clickable_link.w-inline-block 74.6x28.2 outline 2px solid #00063d offset 3px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Log in link. The Log In header action. Measured, never followed. It opens app.jasper.ai.

Page: home. Selector: `a "Log In"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 43.97 x 28.17 | = | = | = |
| Padding | 8px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #00063d offset 3px | = |
| Font | ABC ROM 16px/22.4px 450 | = | = | = |
| Letter spacing | -0.16px | = | = | = |
| Colour | #00063d | = | = | = |
| Text node | div.nav_cta_text.u-text-style-main: ABC ROM 16px/22.4px 450, #00063d, ls -0.16px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.nav_cta_link.w-inline-block 44.0x28.2 outline 2px solid #00063d offset 3px | = |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-cta

Nav CTA. The Free Trial header button. Measured, never followed.

Page: home. Selector: `Free Trial`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 65.48 x 28.17 | = | = | = |
| Padding | 8px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #00063d offset 3px | = |
| Font | ABC ROM 16px/22.4px 450 | = | = | = |
| Letter spacing | -0.16px | = | = | = |
| Colour | #00063d | = | = | = |
| Text node | div.nav_cta_text.u-text-style-main: ABC ROM 16px/22.4px 450, #00063d, ls -0.16px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.nav_cta_link.w-inline-block 65.5x28.2 outline 2px solid #00063d offset 3px | = |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-secondary

Nav secondary. The Get a Demo header link. Measured, never followed.

Page: home. Selector: `a "Get a Demo"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 130.42 x 48.19 | = | = | = |
| Padding | 12px 18px 11px 18px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #00063d | = | = | = |
| Box shadow | none | #0190ff 4px 4px 0px 0px | = | #0190ff 4px 4px 0px 0px |
| Outline | none | = | 2px solid #00063d offset 3px | = |
| Font | ABC ROM 18px/25.2px 500 | = | = | = |
| Letter spacing | -0.25px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div: ABC ROM 18px/25.2px 500, #ffffff, ls -0.25px | = | = | = |
| Transition | transform, box-shadow, background-color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.ns-button-primary.w-inline-block 130.4x48.2 bg #00063d | a.ns-button-primary.w-inline-block 130.4x48.2 bg #00063d shadow #0190ff 4px 4px 0px 0px | a.ns-button-primary.w-inline-block 130.4x48.2 bg #00063d outline 2px solid #00063d offset 3px | a.ns-button-primary.w-inline-block 130.4x48.2 bg #00063d shadow #0190ff 4px 4px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, -4, -4) | = | matrix(1, 0, 0, 1, -4, -4) |

Crops: `nav-secondary-default.png`, `nav-secondary-hover.png`, `nav-secondary-focus-visible.png`, `nav-secondary-pressed.png`.

#### nav-dropdown

Nav dropdown. The Platform mega-menu panel, opened by hovering its item. The full-viewport .nav_dropdown_wrap is the scrim, not the panel.

Page: home. Selector: `.nav_dropdown`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1320 x 561.8 |
| Padding | 24px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | ABC ROM 16px/22.4px 450 |
| Letter spacing | -0.16px |
| Colour | #00063d |
| Text node | div.nav_geo_tag-text: ABC ROM 12px/16.8px 500, #ffffff |
| Transition | none |
| Icon | 0 x 0, colour #00063d |
| Painted layers | div.nav_dropdown 1320.0x561.8 bg #ffffff; div.nav_geo_card 272.0x385.3 bg #ffffff; div.nav_geo_tag 136.7x20.8 bg #fa4028; div.nav_geo_cta 106.9x28.0 bg #fff0e8; div.nav_dropdown_col.u-flex-vertical-nowrap 293.3x513.8 border R:1px solid #f2f2f3; div.g_background.w-variant-80c8adba-8be7-3ff3-2247-d6edc486dd76 268.3x147.4 bg #fff0e8 |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-link

Menu link. A link inside the opened Platform dropdown.

Page: home. Selector: `.nav_dropdown a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 244.33 x 12.17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #00063d offset 3px | 2px solid #00063d offset 3px |
| Font | ABC ROM 16px/22.4px 450 | = | = | = |
| Letter spacing | -0.16px | = | = | = |
| Colour | #00063d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.g_clickable_link.w-inline-block 244.3x12.2 outline 2px solid #00063d offset 3px | a.g_clickable_link.w-inline-block 244.3x12.2 outline 2px solid #00063d offset 3px |

Crops: `menu-link-default.png`, `menu-link-hover.png`, `menu-link-focus-visible.png`, `menu-link-pressed.png`.

### Home hero

#### hero-title

Hero headline. The display headline, set in Feature.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 840 x 193.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Feature 88px/96.8px 400 |
| Letter spacing | -4px |
| Colour | #00063d |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-cta

Hero CTA. A hero action. Measured, never followed.

Page: home. Selector: `hero CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 130.42 x 48.19 | = | = | = |
| Padding | 12px 18px 11px 18px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #00063d | = | = | = |
| Box shadow | none | #0190ff 4px 4px 0px 0px | = | #0190ff 4px 4px 0px 0px |
| Outline | none | = | 2px solid #00063d offset 3px | = |
| Font | ABC ROM 18px/25.2px 500 | = | = | = |
| Letter spacing | -0.25px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div: ABC ROM 18px/25.2px 500, #ffffff, ls -0.25px | = | = | = |
| Transition | transform, box-shadow, background-color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.ns-button-primary.w-inline-block 130.4x48.2 bg #00063d | a.ns-button-primary.w-inline-block 130.4x48.2 bg #00063d shadow #0190ff 4px 4px 0px 0px | a.ns-button-primary.w-inline-block 130.4x48.2 bg #00063d outline 2px solid #00063d offset 3px | a.ns-button-primary.w-inline-block 130.4x48.2 bg #00063d shadow #0190ff 4px 4px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, -4, -4) | = | matrix(1, 0, 0, 1, -4, -4) |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-secondary

Hero secondary. The Explore the Platform link. Measured, never followed.

Page: home. Selector: `a "Explore the Platform"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 200.52 x 48.19 | = | = | = |
| Padding | 12px 18px 11px 18px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #00063d | = | = | = |
| Box shadow | none | #0190ff 4px 4px 0px 0px | = | #0190ff 4px 4px 0px 0px |
| Outline | none | = | 2px solid #00063d offset 3px | = |
| Font | ABC ROM 18px/25.2px 500 | = | = | = |
| Letter spacing | -0.25px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div: ABC ROM 18px/25.2px 500, #ffffff, ls -0.25px | = | = | = |
| Transition | transform, box-shadow, background-color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.ns-button-primary.w-inline-block 200.5x48.2 bg #00063d | a.ns-button-primary.w-inline-block 200.5x48.2 bg #00063d shadow #0190ff 4px 4px 0px 0px | a.ns-button-primary.w-inline-block 200.5x48.2 bg #00063d outline 2px solid #00063d offset 3px | a.ns-button-primary.w-inline-block 200.5x48.2 bg #00063d shadow #0190ff 4px 4px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, -4, -4) | = | matrix(1, 0, 0, 1, -4, -4) |

Crops: `hero-secondary-default.png`, `hero-secondary-hover.png`, `hero-secondary-focus-visible.png`, `hero-secondary-pressed.png`.

### Home

#### section-title

Section heading. A Feature display heading in a home section.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 840 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Feature 32px/40px 400 |
| Letter spacing | -1px |
| Colour | #00063d |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### card

Card. A content card on the home page.

Page: home. Selector: `.g_card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1320 x 413.56 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC ROM 16px/22.4px 400 |
| Letter spacing | -0.16px |
| Colour | #00063d |
| Text node | h3.ns-heading-style-h5: Feature 32px/40px 400, #00063d, ls -1px |
| Transition | none |
| Icon | 430 x 201, colour #00063d, fill #000000 |
| Painted layers | a.ns-platform_card.w-inline-block 318.0x413.6 bg #ffffff border T:1px solid #00063d / R:1px solid #00063d / B:1px solid #00063d / L:1px solid #00063d; a.ns-platform_card.w-inline-block 318.0x413.6 bg #ffffff border T:1px solid #00063d / R:1px solid #00063d / B:1px solid #00063d / L:1px solid #00063d; a.ns-platform_card.w-inline-block 318.0x413.6 bg #ffffff border T:1px solid #00063d / R:1px solid #00063d / B:1px solid #00063d / L:1px solid #00063d; a.ns-platform_card.w-inline-block 318.0x413.6 bg #ffffff border T:1px solid #00063d / R:1px solid #00063d / B:1px solid #00063d / L:1px solid #00063d |
| How | at rest |

Crops: `card-default.png`.

#### text-link

Text link. An in-page text link. Measured, never followed.

Page: home. Selector: `a "Learn more"`. States: .

Not found on the page at capture time.

#### platform-h1

Platform headline. The /platform display headline.

Page: platform. Selector: `h1 on /platform`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 786.66 x 240 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Feature 80px/80px 450 |
| Letter spacing | -2.4px |
| Colour | #00063d |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `platform-h1-default.png`.

#### platform-cta

Platform CTA. A platform-page action. Measured, never followed.

Page: platform. Selector: `platform CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 65.48 x 28.17 | = | = | = |
| Padding | 8px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #00063d offset 3px | = |
| Font | ABC ROM 16px/22.4px 450 | = | = | = |
| Letter spacing | -0.16px | = | = | = |
| Colour | #00063d | = | = | = |
| Text node | div.nav_cta_text.u-text-style-main: ABC ROM 16px/22.4px 450, #00063d, ls -0.16px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.nav_cta_link.w-inline-block 65.5x28.2 outline 2px solid #00063d offset 3px | = |

Crops: `platform-cta-default.png`, `platform-cta-hover.png`, `platform-cta-focus-visible.png`, `platform-cta-pressed.png`.

### Pricing

#### pricing-h1

Pricing title. The pricing page headline.

Page: pricing. Selector: `h1 on /pricing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 817.55 x 160 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Feature 80px/80px 450 |
| Letter spacing | -2.4px |
| Colour | #00063d |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### price-card

Price card. A pricing tier card.

Page: pricing. Selector: `pricing card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 328 x 119.69 |
| Padding | 16px 0px |
| Border | T: none; R: 1px solid #e0e0e1; B: none; L: 1px solid #e0e0e1 |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC ROM 16px/22.4px 450 |
| Letter spacing | -0.16px |
| Colour | #00063d |
| Text node | p: Feature 24px/26.4px 450, #00063d |
| Transition | none |
| Painted layers | div.price_chart_category_col.is-border 328.0x119.7 border R:1px solid #e0e0e1 / L:1px solid #e0e0e1; div.btn_main_wrap.w-variant-e85564cd-af30-a478-692b-71732aefb3ab 164.1x47.7 border T:1px solid #00063d / R:1px solid #00063d / B:1px solid #00063d / L:1px solid #00063d |
| How | at rest |

Crops: `price-card-default.png`.

#### price-cta

Price CTA. A pricing action. Measured, never followed.

Page: pricing. Selector: `pricing CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 130.42 x 48.19 | = | = | = |
| Padding | 12px 18px 11px 18px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #00063d | = | = | = |
| Box shadow | none | #0190ff 4px 4px 0px 0px | = | #0190ff 4px 4px 0px 0px |
| Outline | none | = | 2px solid #00063d offset 3px | = |
| Font | ABC ROM 18px/25.2px 500 | = | = | = |
| Letter spacing | -0.25px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div: ABC ROM 18px/25.2px 500, #ffffff, ls -0.25px | = | = | = |
| Transition | transform, box-shadow, background-color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.ns-button-primary.w-inline-block 130.4x48.2 bg #00063d | a.ns-button-primary.w-inline-block 130.4x48.2 bg #00063d shadow #0190ff 4px 4px 0px 0px | a.ns-button-primary.w-inline-block 130.4x48.2 bg #00063d outline 2px solid #00063d offset 3px | a.ns-button-primary.w-inline-block 130.4x48.2 bg #00063d shadow #0190ff 4px 4px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, -4, -4) | = | matrix(1, 0, 0, 1, -4, -4) |

Crops: `price-cta-default.png`, `price-cta-hover.png`, `price-cta-focus-visible.png`, `price-cta-pressed.png`.

#### faq-item

FAQ item. An FAQ row. Toggled for its open state. Nothing is submitted.

Page: pricing. Selector: `faq item`. States: .

Not found on the page at capture time.

### Brand page

#### brand-h1

Brand title. The /brand page headline.

Page: brand. Selector: `h1 on /brand`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1021.94 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Feature 80px/80px 450 |
| Letter spacing | -2.4px |
| Colour | #00063d |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `brand-h1-default.png`.

#### brand-download

Brand download. A logo download link on /brand. Measured, never followed.

Page: brand. Selector: `a "Download PNG"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 99.61 x 23.59 | = | = | = |
| Padding | 4.8px 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #00063d | 1px solid #fa4028 | = | 1px solid #fa4028 |
| Radius | 0px | = | = | = |
| Background | #ffffff | #ffe8e2 | = | #ffe8e2 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #00063d offset 3px | = |
| Font | ABC ROM Mono 12px/12px 450 | = | = | = |
| Letter spacing | -0.16px | = | = | = |
| Colour | #00063d | #fa4028 | = | #fa4028 |
| Text node | div: ABC ROM Mono 12px/12px 450, #00063d, ls -0.16px | div: ABC ROM Mono 12px/12px 450, #fa4028, ls -0.16px | = | div: ABC ROM Mono 12px/12px 450, #fa4028, ls -0.16px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.brand_asset_btn.w-inline-block 99.6x23.6 bg #ffffff border T:1px solid #00063d / R:1px solid #00063d / B:1px solid #00063d / L:1px solid #00063d | a.brand_asset_btn.w-inline-block 99.6x23.6 bg #ffe8e2 border T:1px solid #fa4028 / R:1px solid #fa4028 / B:1px solid #fa4028 / L:1px solid #fa4028 | a.brand_asset_btn.w-inline-block 99.6x23.6 bg #ffffff border T:1px solid #00063d / R:1px solid #00063d / B:1px solid #00063d / L:1px solid #00063d outline 2px solid #00063d offset 3px | a.brand_asset_btn.w-inline-block 99.6x23.6 bg #ffe8e2 border T:1px solid #fa4028 / R:1px solid #fa4028 / B:1px solid #fa4028 / L:1px solid #fa4028 |
| Ancestor paint | 3 up div.brand-logo.cc-light shadow #8c87c2 @ 0.12 0px 18px 52px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `brand-download-default.png`, `brand-download-hover.png`, `brand-download-focus-visible.png`, `brand-download-pressed.png`.

### Demo form boundary

#### demo-card

Demo form. The Get a Demo HubSpot form, measured at rest. Nothing was typed or submitted.

Page: demo. Selector: `form on /demo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 547.33 x 393.92 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC ROM 16px/22.4px 450 |
| Letter spacing | -0.16px |
| Colour | #00063d |
| Text node | span: ABC ROM 16px/20px 500, #00063d, ls -0.32px |
| Transition | none |
| Painted layers | input.hs-input 547.3x48.0 bg #ffffff border T:1px solid #000000 @ 0.5 / R:1px solid #000000 @ 0.5 / B:1px solid #000000 @ 0.5 / L:1px solid #000000 @ 0.5; input.hs-input 265.7x48.0 bg #ffffff border T:1px solid #000000 @ 0.5 / R:1px solid #000000 @ 0.5 / B:1px solid #000000 @ 0.5 / L:1px solid #000000 @ 0.5; input.hs-input 265.7x48.0 bg #ffffff border T:1px solid #000000 @ 0.5 / R:1px solid #000000 @ 0.5 / B:1px solid #000000 @ 0.5 / L:1px solid #000000 @ 0.5; input.hs-input 547.3x48.0 bg #ffffff border T:1px solid #000000 @ 0.5 / R:1px solid #000000 @ 0.5 / B:1px solid #000000 @ 0.5 / L:1px solid #000000 @ 0.5; input.hs-input 0.0x0.0 bg #ffffff border T:1px solid #000000 @ 0.5 / R:1px solid #000000 @ 0.5 / B:1px solid #000000 @ 0.5 / L:1px solid #000000 @ 0.5; input.hs-input 0.0x0.0 bg #ffffff border T:1px solid #000000 @ 0.5 / R:1px solid #000000 @ 0.5 / B:1px solid #000000 @ 0.5 / L:1px solid #000000 @ 0.5 |
| How | at rest |

Crops: `demo-card-default.png`.

#### demo-field

Demo email field. The work-email field. Focused only. Nothing typed, nothing submitted.

Page: demo. Selector: `input[name=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 547.33 x 48 | = |
| Padding | 12.8px | = |
| Border | 1px solid #000000 @ 0.5 | 1px solid #fa4028 |
| Radius | 0px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABC ROM 16px/17.6px 450 | = |
| Letter spacing | -0.32px | = |
| Colour | #000000 @ 0.65 | #00063d |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #64748b, opacity 1 | = |
| Painted layers | input.hs-input 547.3x48.0 bg #ffffff border T:1px solid #000000 @ 0.5 / R:1px solid #000000 @ 0.5 / B:1px solid #000000 @ 0.5 / L:1px solid #000000 @ 0.5 | input.hs-input 547.3x48.0 bg #ffffff border T:1px solid #fa4028 / R:1px solid #fa4028 / B:1px solid #fa4028 / L:1px solid #fa4028 |
| How | at rest | clicked into the field |

Crops: `demo-field-default.png`, `demo-field-focused.png`.

#### demo-submit

Demo submit. The form submit. Measured, never pressed.

Page: demo. Selector: `form submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 547.33 x 48 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #fa4028 | #801a10 | = | #801a10 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #0462cd offset 0px | = |
| Font | ABC ROM 16px/16px 450 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.4s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Placeholder | #ffffff, opacity 1 | = | = | = |
| Painted layers | input.hs-button.primary 547.3x48.0 bg #fa4028 | input.hs-button.primary 547.3x48.0 bg #801a10 | input.hs-button.primary 547.3x48.0 bg #fa4028 outline 1px auto #0462cd offset 0px | input.hs-button.primary 547.3x48.0 bg #801a10 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `demo-submit-default.png`, `demo-submit-hover.png`, `demo-submit-focus-visible.png`, `demo-submit-pressed.png`.

### App login boundary

#### login-card

Login card. The app.jasper.ai login column. The boundary before the product. Never filled, never submitted, no OAuth followed.

Page: signin. Selector: `login column`. States: .

Not found on the page at capture time.

#### login-field

Login email field. The email field on the login card. Focused only. Nothing typed.

Page: signin. Selector: `login input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 410 x 20 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #1d2534 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #818794, opacity 1 | = |
| Ancestor paint | 1 up label.group/input.flex bg #ffffff | 1 up label.group/input.flex bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0070ee 0px 0px 0px 1px inset |
| How | at rest | clicked into the field |

Crops: `login-field-default.png`, `login-field-focused.png`.

#### login-submit

Continue with email. The email submit. Measured, never pressed.

Page: signin. Selector: `button "Continue with email"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 432 x 32 | = | = | = |
| Padding | 5px 12px | = | = | = |
| Gap | 0px | = | = | = |
| Border | 1px solid #0070ee | 1px solid #0056d4 | = | 1px solid #0056d4 |
| Radius | 6px | = | = | = |
| Background | #0070ee | #2887f0 | = | #2887f0 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #cce2fc 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.pointer-events-none.text-center: Inter 14px/20px 500, #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.items-center 432.0x32.0 bg #0070ee border T:1px solid #0070ee / R:1px solid #0070ee / B:1px solid #0070ee / L:1px solid #0070ee r 6px | button.inline-flex.items-center 432.0x32.0 bg #2887f0 border T:1px solid #0056d4 / R:1px solid #0056d4 / B:1px solid #0056d4 / L:1px solid #0056d4 r 6px | button.inline-flex.items-center 432.0x32.0 bg #0070ee border T:1px solid #0070ee / R:1px solid #0070ee / B:1px solid #0070ee / L:1px solid #0070ee r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #cce2fc 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.items-center 432.0x32.0 bg #2887f0 border T:1px solid #0056d4 / R:1px solid #0056d4 / B:1px solid #0056d4 / L:1px solid #0056d4 r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-focus-visible.png`, `login-submit-pressed.png`.

#### login-google

Continue with Google. The Google OAuth button. Measured, never followed.

Page: signin. Selector: `button "Continue with Google"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 432 x 32 | = | = | = |
| Padding | 5px 12px 5px 8px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #dee0e4 | = | 1px solid #0070ee | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | #f3f4f6 | = | #f3f4f6 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #cce2fc 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1d2534 | = | = | = |
| Text node | span.pointer-events-none.text-center: Inter 14px/20px 500, #1d2534 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #1d2534 | = | = | = |
| Painted layers | button.inline-flex.items-center 432.0x32.0 bg #ffffff border T:1px solid #dee0e4 / R:1px solid #dee0e4 / B:1px solid #dee0e4 / L:1px solid #dee0e4 r 6px | button.inline-flex.items-center 432.0x32.0 bg #f3f4f6 border T:1px solid #dee0e4 / R:1px solid #dee0e4 / B:1px solid #dee0e4 / L:1px solid #dee0e4 r 6px | button.inline-flex.items-center 432.0x32.0 bg #ffffff border T:1px solid #0070ee / R:1px solid #0070ee / B:1px solid #0070ee / L:1px solid #0070ee r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #cce2fc 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.items-center 432.0x32.0 bg #f3f4f6 border T:1px solid #dee0e4 / R:1px solid #dee0e4 / B:1px solid #dee0e4 / L:1px solid #dee0e4 r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-google-default.png`, `login-google-hover.png`, `login-google-focus-visible.png`, `login-google-pressed.png`.

#### login-signup

Sign up link. The Sign up action on the login card. Measured, never followed.

Page: signin. Selector: `Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50.03 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0070ee | #2887f0 | #2887f0 | #2887f0 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-signup-default.png`, `login-signup-hover.png`, `login-signup-focus-visible.png`, `login-signup-pressed.png`.

### Footer

#### footer

Footer. The site footer: link columns and legal.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1189.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #00063d |
| Box shadow | none |
| Outline | none |
| Font | ABC ROM 16px/22.4px 450 |
| Letter spacing | -0.16px |
| Colour | #ffffff |
| Text node | div.u-text-style-h4: Feature 24px/26.4px 450, #ffffff |
| Transition | none |
| Icon | 12 x 12, colour #ffffff |
| Painted layers | div.footer_wrap.w-variant-d9560e08-2b3d-c749-d924-7ab428ce867e 1440.0x1189.5 bg #00063d; div.footer_column_divider 304.0x1.0 bg #ffffff; ul.footer_sublist.w-list-unstyled 152.7x51.2 border L:1px solid #ffffff @ 0.2; ul.footer_sublist.w-list-unstyled 152.7x51.2 border L:1px solid #ffffff @ 0.2; ul.footer_sublist.w-list-unstyled 136.5x73.5 border L:1px solid #ffffff @ 0.2; div.footer_column_divider 304.0x1.0 bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 126.73 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #00063d offset 3px | = |
| Font | ABC ROM 16px/22.4px 450 | = | = | = |
| Letter spacing | -0.16px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.u-text-style-h4: Feature 24px/26.4px 450, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.footer_heading_wrap.u-flex-horizontal-nowrap 126.7x24.0 outline 2px solid #00063d offset 3px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `.nav_contain at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | ABC ROM 16px/22.4px 450 |
| Letter spacing | -0.16px |
| Colour | #00063d |
| Text node | div.nav_cta_text.u-text-style-main: ABC ROM 16px/22.4px 450, #00063d, ls -0.16px |
| Transition | none |
| Icon | 98.72 x 37.02, colour #fa4028 |
| Painted layers | div.nav_wrap 390.0x80.0 bg #ffffff; div.nav_overlay 0.0x0.0 bg #000000 @ 0.6; div.nav_contain.u-grid-custom 390.0x80.0 bg #ffffff; div.utility-1_menu 0.0x0.0 bg #ffffff; div.nav_menu_link_color.is-border 0.0x0.0 bg #ceebff; div.nav_menu_link_color.is-center 0.0x0.0 bg #ceebff |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The mobile menu toggle.

Page: mobile. Selector: `mobile menu button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 104 x 37.02 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC ROM 16px/22.4px 450 |
| Letter spacing | normal |
| Colour | #00063d |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The mobile nav panel opened by its own toggle.

Page: mobile. Selector: `mobile menu open`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 40 |
| Padding | 0px 0px 24px 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | ABC ROM 16px/22.4px 450 |
| Letter spacing | -0.16px |
| Colour | #00063d |
| Text node | div.nav_dropdown_mobile_text.u-text-style-h3: Feature 28px/30.8px 450, #00063d, ls -0.56px |
| Transition | none |
| Icon | 12.8 x 8, colour #00063d |
| Painted layers | div.nav_dropdown 350.0x40.0 bg #ffffff; div.nav_dropdown_mobile_main-link 350.0x169.7 border B:1px solid #0095ff; div.nav_card_wrap.u-flex-vertical-nowrap 350.0x169.7 border T:1px solid #0043d3 / R:1px solid #0043d3 / B:1px solid #0043d3 / L:1px solid #0043d3; div.nav_geo_card 272.0x329.2 bg #ffffff; div.nav_geo_tag 136.7x20.8 bg #fa4028; div.nav_geo_cta 106.9x28.0 bg #fff0e8 |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. An item inside the opened mobile menu.

Page: mobile. Selector: `mobile nav item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 43.97 x 28.17 | = | = | = |
| Padding | 8px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #00063d offset 3px | = |
| Font | ABC ROM 16px/22.4px 450 | = | = | = |
| Letter spacing | -0.16px | = | = | = |
| Colour | #00063d | = | = | = |
| Text node | div.nav_cta_text.u-text-style-main: ABC ROM 16px/22.4px 450, #00063d, ls -0.16px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.nav_cta_link.w-inline-block 44.0x28.2 outline 2px solid #00063d offset 3px | = |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Feature 40px/44px 400 |
| Letter spacing | -1.25px |
| Colour | #00063d |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

jasper.ai serves its Webflow CSS from a CDN. This list holds the transitions the readable sheets declare on each page. The per-state Transition rows above are computed values.

- demo: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `border-color, color, background-color`, `border-color 0.2s, color 0.2s, background-color 0.2s`, `0.4s`, `opacity 0.4s`, `background-color 0.4s ease-out, border-color 0.4s ease-out, padding-top 0.4s ease-out, padding-left 0.4s ease-out`, `opacity 0.2s`, `0.15s`, `bottom 0.8s`, `opacity 0.5s`

- home: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `border-color, color, background-color`, `border-color 0.2s, color 0.2s, background-color 0.2s`, `0.4s`, `opacity 0.4s`, `background-color 0.4s ease-out, border-color 0.4s ease-out, padding-top 0.4s ease-out, padding-left 0.4s ease-out`, `opacity 0.2s`, `0.15s`, `bottom 0.8s`, `opacity 0.5s`

- platform: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `border-color, color, background-color`, `border-color 0.2s, color 0.2s, background-color 0.2s`, `0.4s`, `opacity 0.4s`, `background-color 0.4s ease-out, border-color 0.4s ease-out, padding-top 0.4s ease-out, padding-left 0.4s ease-out`, `opacity 0.2s`, `0.15s`, `bottom 0.8s`, `opacity 0.5s`

- pricing: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `border-color, color, background-color`, `border-color 0.2s, color 0.2s, background-color 0.2s`, `0.4s`, `opacity 0.4s`, `background-color 0.4s ease-out, border-color 0.4s ease-out, padding-top 0.4s ease-out, padding-left 0.4s ease-out`, `opacity 0.2s`, `0.15s`, `bottom 0.8s`, `opacity 0.5s`

- signin: `margin-right 0.3s`, `0.2s`, `opacity 0.1s, transform 0.3s`, `background-color 0.2s`, `opacity 0.2s`, `opacity 0.1s ease-out, transform 0.2s ease-out`, `transform 0.3s`, `0.3s`, `opacity 0.4s ease-out 0.25s`, `color 0.4s ease-out 0.25s`, `transform 0.4s ease-out 0.25s`, `opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1)`
