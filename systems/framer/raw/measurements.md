# Framer component measurements

Computed styles read from framer.com on 2026-11-15 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the www marketing pages that resolve the body-declared `--token-<uuid>` dark palette (home, pricing, contact and the pages in screenshots/), the community stack at /community/gallery (a different app that also paints dark), the light auth shell at /login, and the mobile drawer — with the cookie consent card hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). No painted light variant of the marketing site exists; the only light surface signed out is the auth shell. One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Site chrome

#### mkt-header

Site header. The bar on every marketing page: the Framer mark, the Platform/Solutions/Resources mega-dropdown triggers, Pricing, Enterprise, "Log in" and "Sign up".

Page: home. Selector: `header / top nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 64 |
| Padding | 0px 20px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text: Inter Variable 14px/14px 400, #ffffff, ls -0.01px |
| Transition | none |
| Cursor | default |
| Icon | 8 x 8, colour #000000 |
| Painted layers | div.framer-ngytjn 16.0x24.0 image url(data:…)%22></path></svg>"); div.framer-4mgnl8 87.2x35.6 bg #ffffff @ 0.1 r 8px; div.framer-4mgnl8 92.1x35.6 bg #ffffff @ 0.1 r 8px; div.framer-4mgnl8 102.1x35.6 bg #ffffff @ 0.1 r 8px; div.framer-4mgnl8 86.0x35.6 bg #ffffff @ 0.1 r 8px; div.framer-4mgnl8 64.3x35.6 bg #ffffff @ 0.1 r 8px |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The Framer mark in the header, linking home.

Page: home. Selector: `header a Framer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 76.95 x 26 |
| Padding | 0px |
| Gap | 10px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Text node | p.framer-text: Inter Variable 14px/14px 400, #ffffff, ls -0.01px |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.framer-ngytjn 16.0x24.0 image url(data:…)%22></path></svg>") |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-dropdown-btn

Nav dropdown trigger. The "Platform" header item — an `a` without href whose mega-dropdown opens on hover (never followed).

Page: home. Selector: `header a Platform`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 91.2 x 39.59 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | p.framer-text.framer-styles-preset-rhbxb3: Inter Variable 14px/19.6px 400, #ffffff @ 0.8, ls -0.1px | p.framer-text.framer-styles-preset-rhbxb3: Inter Variable 14px/19.6px 400, #ffffff, ls -0.1px | p.framer-text.framer-styles-preset-rhbxb3: Inter Variable 14px/19.6px 400, #ffffff, ls -0.1px | p.framer-text.framer-styles-preset-rhbxb3: Inter Variable 14px/19.6px 400, #ffffff, ls -0.1px |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 8 x 8, colour #000000 | = | = | = |
| Painted layers | div.framer-4mgnl8 87.2x35.6 bg #ffffff @ 0.1 r 8px | = | a.framer-uTdPy.framer-aZ6KF 91.2x39.6 outline 1px auto #101010 offset 0px; div.framer-4mgnl8 87.2x35.6 bg #ffffff @ 0.1 r 8px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-dropdown-btn-default.png`, `nav-dropdown-btn-hover.png`, `nav-dropdown-btn-focus-visible.png`, `nav-dropdown-btn-pressed.png`.

#### nav-panel

Platform dropdown panel. The mega-dropdown panel opened by hovering "Platform" (Create/Build/Grow columns and the Updates thumbnail); its links were never followed.

Page: home. Selector: `platform mega-dropdown panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 650 x 156.78 |
| Padding | 0px |
| Gap | 10px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-rhbxb3: Inter Variable 14px/19.6px 400, #ffffff @ 0.6, ls -0.1px |
| Transition | none |
| Cursor | default |
| Painted layers | div.framer-4mgnl8 12.6x20.3 bg #ffffff @ 0.1 r 8px; div.framer-4mgnl8 55.8x20.3 bg #ffffff @ 0.1 r 8px; div.framer-4mgnl8 53.8x20.3 bg #ffffff @ 0.1 r 8px; div.framer-4mgnl8 34.4x20.3 bg #ffffff @ 0.1 r 8px; div.framer-4mgnl8 35.4x20.3 bg #ffffff @ 0.1 r 8px; div.framer-4mgnl8 58.6x20.3 bg #ffffff @ 0.1 r 8px |
| How | at rest |

Crops: `nav-panel-default.png`.

#### nav-pricing

Nav link. The "Pricing" header link; measured, never followed.

Page: home. Selector: `header a Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 68.31 x 39.59 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-rhbxb3: Inter Variable 14px/19.6px 400, #ffffff @ 0.8, ls -0.1px | p.framer-text.framer-styles-preset-rhbxb3: Inter Variable 14px/19.6px 400, #ffffff, ls -0.1px | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.framer-4mgnl8 64.3x35.6 bg #ffffff @ 0.1 r 8px | = | a.framer-uTdPy.framer-aZ6KF 68.3x39.6 outline 1px auto #101010 offset 1px; div.framer-4mgnl8 64.3x35.6 bg #ffffff @ 0.1 r 8px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-pricing-default.png`, `nav-pricing-hover.png`, `nav-pricing-focus-visible.png`, `nav-pricing-pressed.png`.

#### nav-login

Log in link. The "Log in" header link to /login; measured, never followed.

Page: home. Selector: `header a Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 39.41 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter Variable 14px/19.6px 400 | = | = | = |
| Letter spacing | -0.1px | = | = | = |
| Colour | #ffffff @ 0.6 | #ffffff | = | #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-text.framer-styles-preset-1si2ozi 39.4x17.0 outline 1px auto #101010 offset 1px | = |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-cta

Header CTA. The "Sign up" header button; links to the auth shell, measured never followed.

Page: home. Selector: `header a Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 64.09 x 30 | = | = | = |
| Padding | 8px 10px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | span.framer-text: Inter Variable 14px/14px 400, #000000, ls -0.56px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-16mrjhl.framer-enysp5 64.1x30.0 bg #ffffff r 8px | = | a.framer-16mrjhl.framer-enysp5 64.1x30.0 bg #ffffff r 8px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### hero-h1

Hero headline. "Framer is the pro website builder with a world-class design agent" — the www.framer.com hero display heading.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 782 x 108 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Walsheim Medium 54px/54px 500 |
| Letter spacing | -2.16px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-cta

Hero CTA. The white "Get started for free" pill in the hero; links to the auth shell, measured never followed.

Page: home. Selector: `hero Get started for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 149.41 x 34 | = | = | = |
| Padding | 10px 14px | = | = | = |
| Gap | 7px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Inter Variable 14px/14px 400, #000000, ls -0.28px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-R3ehQ.framer-qkzqfa 149.4x34.0 bg #ffffff r 8px | = | a.framer-R3ehQ.framer-qkzqfa 149.4x34.0 bg #ffffff r 8px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.6 | = | = |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-mcp

Hero secondary button. The "Install the MCP" ghost button beside the hero CTA; measured, never followed.

Page: home. Selector: `hero Install the MCP`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 123.81 x 34 | = | = | = |
| Padding | 10px 14px | = | = | = |
| Gap | 7px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff @ 0.1 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Inter Variable 14px/14px 400, #ffffff, ls -0.28px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-R3ehQ.framer-qkzqfa 123.8x34.0 bg #ffffff @ 0.1 r 8px | = | a.framer-R3ehQ.framer-qkzqfa 123.8x34.0 bg #ffffff @ 0.1 r 8px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.6 | = | = |

Crops: `hero-mcp-default.png`, `hero-mcp-hover.png`, `hero-mcp-focus-visible.png`, `hero-mcp-pressed.png`.

#### section-h2

Section heading. A marketing section heading further down the home page.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 520 x 96.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Walsheim Medium 44px/48.4px 500 |
| Letter spacing | -1.76px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

### Footer

#### footer

Footer. The page footer: product/solutions/resources/company columns, social icons and the English/Japanese locale select.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1240 x 638 |
| Padding | 20px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-rhbxb3: Inter Variable 14px/19.6px 400, #ffffff, ls -0.1px |
| Transition | none |
| Icon | 12 x 12, colour #ffffff, fill #000000 |
| Painted layers | footer.framer-b3P3Z.framer-3wgpx 1240.0x638.0 bg #000000; a.framer-UNEfR.framer-aZ6KF 51.3x22.0 bg #000000 r 8px; div::after.framer-qoCYz.framer-1sisfx8 23.6406pxx13px border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 3px; div::after.framer-qoCYz.framer-1sisfx8 23.6406pxx13px border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 3px; a.framer-UNEfR.framer-aZ6KF 84.9x22.0 bg #000000 r 8px; a.framer-UNEfR.framer-aZ6KF 57.2x22.0 bg #000000 r 8px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer sitemap link; measured, never followed.

Page: home. Selector: `footer a Careers`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 53.31 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 5px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-rhbxb3: Inter Variable 14px/19.6px 400, #ffffff @ 0.6, ls -0.1px | p.framer-text.framer-styles-preset-rhbxb3: Inter Variable 14px/19.6px 400, #ffffff, ls -0.1px | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-UNEfR.framer-aZ6KF 53.3x22.0 r 8px outline 1px auto #101010 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### locale-select

Locale select. The "English" locale select in the footer — a local UI control; measured, never changed.

Page: home. Selector: `footer select locale`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 78 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #767676 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #efefef | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Opacity | 0 | = | = | = |
| Painted layers | select 78.0x18.0 bg #efefef border T:1px solid #767676 / R:1px solid #767676 / B:1px solid #767676 / L:1px solid #767676 | = | select 78.0x18.0 bg #efefef border T:1px solid #767676 / R:1px solid #767676 / B:1px solid #767676 / L:1px solid #767676 outline 1px auto #101010 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `locale-select-default.png`, `locale-select-hover.png`, `locale-select-focus-visible.png`, `locale-select-pressed.png`.

### Pricing

#### price-h1

Pricing headline. "Start free, then scale your site" — the /pricing masthead.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 420 x 108 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Walsheim Medium 54px/54px 500 |
| Letter spacing | -2.16px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `price-h1-default.png`.

#### billing-toggle

Billing toggle. The "Yearly billing" switch beside the plan names; measured at rest, never toggled (toggling would re-price the grid).

Page: pricing. Selector: `yearly billing toggle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.61 x 19.59 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | sans-serif 12px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | p.framer-text.framer-styles-preset-rhbxb3: Inter Variable 14px/19.6px 400, #ffffff @ 0.6, ls -0.1px | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `billing-toggle-default.png`, `billing-toggle-hover.png`, `billing-toggle-pressed.png`.

#### credits-select

Credits select. The "Credits per month" select on a plan card (1,000–10,000 AI credits); measured at rest, never opened (its options recompute prices).

Page: pricing. Selector: `credits per month select`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 250 x 34 | = | = | = |
| Padding | 8px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/18.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.8 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `credits-select-default.png`, `credits-select-hover.png`, `credits-select-focus-visible.png`, `credits-select-pressed.png`.

#### plan-card

Plan card. The Pro plan column: name, price, feature list and its CTA.

Page: pricing. Selector: `Pro plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 300 x 552.23 |
| Padding | 20px |
| Gap | 5px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.framer-text.framer-styles-preset-ojsfn5: Inter Variable 18px/24.3px 400, #ffffff, ls -0.2px |
| Transition | none |
| Icon | 12 x 12, colour #000000 |
| Painted layers | div.framer-f267wx 260.0x1.0 bg #1a1a1a; div::before.framer-form-input-wrapper.framer-form-select-wrapper 16pxx18px bg #ffffff @ 0.8; div::after.framer-form-input-wrapper.framer-form-select-wrapper 260pxx34px border T:1px solid #1a1a1a / R:1px solid #1a1a1a / B:1px solid #1a1a1a / L:1px solid #1a1a1a r 8px; div.framer-xmqd09 260.0x1.0 bg #1a1a1a; a.framer-R3ehQ.framer-qkzqfa 260.0x34.0 bg #0099ff r 8px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-cta

Plan CTA. The Pro plan card's action button; measured, never followed.

Page: pricing. Selector: `Pro plan CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 260 x 34 | = | = | = |
| Padding | 10px 14px | = | = | = |
| Gap | 7px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #0099ff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Inter Variable 14px/14px 400, #ffffff, ls -0.28px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-R3ehQ.framer-qkzqfa 260.0x34.0 bg #0099ff r 8px | = | a.framer-R3ehQ.framer-qkzqfa 260.0x34.0 bg #0099ff r 8px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.6 | = | = |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### faq-acc

FAQ row. A question row in the /pricing FAQ ("What are credits?"); measured at rest and on hover, never toggled.

Page: pricing. Selector: `FAQ row What are credits`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 420 x 24.3 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h3.framer-text.framer-styles-preset-ojsfn5: Inter Variable 18px/24.3px 400, #ffffff, ls -0.2px | = |
| Transition | none | = |
| How | at rest | mouse hover |

Crops: `faq-acc-default.png`, `faq-acc-hover.png`.

### Contact

#### contact-h1

Contact headline. "Get in touch with the team" — the /contact masthead over the support/billing/sales directory.

Page: contact. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 369 x 108 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Walsheim Medium 54px/54px 500 |
| Letter spacing | -2.16px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `contact-h1-default.png`.

#### contact-card

Contact card. The Support directory card; a contact surface, not a form.

Page: contact. Selector: `Support card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 186.89 |
| Padding | 30px |
| Gap | 20px |
| Border | none |
| Radius | 0px |
| Background | #ffffff @ 0 |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.framer-text.framer-styles-preset-ojsfn5: Inter Variable 18px/24.3px 400, #ffffff, ls -0.2px |
| Transition | none |
| Icon | 12 x 12, colour #0000ee, fill #000000 |
| ::after | 1200px x 186.891px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | div.framer-6ksu8k 1200.0x186.9 bg #ffffff @ 0; div::after.framer-6ksu8k 1200pxx186.891px border R:1px solid #1a1a1a / B:1px solid #1a1a1a; a.framer-R3ehQ.framer-qkzqfa 92.0x34.0 bg #ffffff r 8px |
| How | at rest |

Crops: `contact-card-default.png`.

#### contact-link

Contact link. A link inside a contact directory card; measured, never followed.

Page: contact. Selector: `contact card link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 92.02 x 34 | = | = | = |
| Padding | 10px 14px | = | = | = |
| Gap | 7px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | p.framer-text: Inter Variable 15px/15px 400, #000000, ls -0.3px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-R3ehQ.framer-qkzqfa 92.0x34.0 bg #ffffff r 8px | = | a.framer-R3ehQ.framer-qkzqfa 92.0x34.0 bg #ffffff r 8px outline 1px auto #101010 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.6 | = | = |

Crops: `contact-link-default.png`, `contact-link-hover.png`, `contact-link-focus-visible.png`, `contact-link-pressed.png`.

### Login (auth shell)

#### login-panel

Login panel. The auth-shell sign-in card on /login: "Welcome to Framer" with Google SSO and an e-mail field. The auth shell is a light third stack.

Page: login. Selector: `login form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable UI 13px/normal 450 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | span.translate: Inter Variable UI 20px/24px 550, #222222, ls -0.2px |
| Transition | none |
| Icon | 16 x 24, colour #222222, fill #000000 |
| Painted layers | body.notranslate.login 1440.0x900.0 bg #ffffff; div.a1ffer84 1440.0x900.0 bg #ffffff; div.s1n8l1x5.c1yzp6zb 260.0x270.0 bg #ffffff; button.b1rdbf0o.bygx14j 230.0x30.0 bg #222222 r 8px; div::before.t1qclljk 92pxx1px border B:1px solid #eeeeee; div::after.t1qclljk 92pxx1px border B:1px solid #eeeeee |
| How | at rest |

Crops: `login-panel-default.png`.

#### login-google

Google SSO button. The "Continue with Google" button; measured, never pressed.

Page: login. Selector: `login Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 230 x 30 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #222222 | #333333 | #333333 | #333333 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter Variable UI 12px/normal 450 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 11 x 11, colour #ffffff, fill #999999 | = | = | = |
| Painted layers | button.b1rdbf0o.bygx14j 230.0x30.0 bg #222222 r 8px | button.b1rdbf0o.bygx14j 230.0x30.0 bg #333333 r 8px | button.b1rdbf0o.bygx14j 230.0x30.0 bg #333333 r 8px | button.b1rdbf0o.bygx14j 230.0x30.0 bg #333333 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-google-default.png`, `login-google-hover.png`, `login-google-focus-visible.png`, `login-google-pressed.png`.

#### login-email

Email field (login). The work e-mail input on the sign-in card; focused and typed into then cleared — never submitted.

Page: login. Selector: `login email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 228 x 30 | = | = |
| Padding | 0px 7px 1px 7px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter Variable UI 12px/normal 450 | = | = |
| Letter spacing | normal | = | = |
| Colour | #222222 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #999999, opacity 1 | = | = |
| Ancestor paint | 1 up div.i1ubxgci bg #000000 @ 0.05 | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-email-default.png`, `login-email-focused.png`, `login-email-filled.png`.

#### login-submit

Continue submit. The "Continue" submit button; its states were measured but the button was never clicked — nothing was submitted.

Page: login. Selector: `login Continue`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 230 x 30 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #000000 @ 0.05 | #000000 @ 0.07 | #000000 @ 0.07 | #000000 @ 0.07 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter Variable UI 12px/normal 450 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | = | = | = |
| Transition | background-color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.b1rdbf0o.fwwdn1t 230.0x30.0 bg #000000 @ 0.05 r 8px | button.b1rdbf0o.fwwdn1t 230.0x30.0 bg #000000 @ 0.07 r 8px | button.b1rdbf0o.fwwdn1t 230.0x30.0 bg #000000 @ 0.07 r 8px | button.b1rdbf0o.fwwdn1t 230.0x30.0 bg #000000 @ 0.07 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-focus-visible.png`, `login-submit-pressed.png`.

### Community gallery (product stack)

#### gal-h1

Gallery headline. "Gallery" — the /community/gallery masthead in the community stack (a different app that also paints dark).

Page: gallery. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 92.61 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | walsheim 30px/30px 500 |
| Letter spacing | -1.2px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `gal-h1-default.png`.

#### gal-search

Gallery search. The "Search Gallery" input; focused and typed into then cleared — never searched.

Page: gallery. Selector: `gallery search input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 203 x 14.39 | = |
| Padding | 0px 0px 0px 1px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | inter 12px/14.4px 450 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #999999, opacity 1 | = |
| Ancestor paint | 1 up label.Wf6zXG_field bg #1f1f1f | 1 up label.Wf6zXG_field bg #1f1f1f shadow #333333 0px 0px 0px 1px inset |
| How | at rest | clicked into the field |

Crops: `gal-search-default.png`, `gal-search-focused.png`.

#### gal-filter

Filter button. A gallery sort button (Trending / Recent / Vibe); measured at rest, never toggled (toggling would re-sort the grid).

Page: gallery. Selector: `gallery Trending`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 74 x 30 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #1f1f1f | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | inter 12px/12px 450 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.DFz--G_inner: inter 12px/12px 450, #ffffff | = | = | = |
| Transition | background-color, color 0.15s, 0.15s cubic-bezier(0.4, 0, 0.2, 1), cubic-bezier(0.4, 0, 0.2, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.DFz--G_root.DFz--G_active 74.0x30.0 bg #1f1f1f r 8px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `gal-filter-default.png`, `gal-filter-hover.png`, `gal-filter-focus-visible.png`, `gal-filter-pressed.png`.

#### gal-open

Card Open button. An "Open" button on a gallery card; measured, never followed (it would open the site's page).

Page: gallery. Selector: `gallery Open`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 55 x 30 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Gap | 10px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #1f1f1f | #262626 | = | #262626 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | inter 12px/12px 450 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.AZdcjW_content: inter 12px/12px 450, #ffffff | = | = | = |
| Transition | background-color, box-shadow, color, opacity 0.15s, 0.15s, 0.15s, 0.15s cubic-bezier(0.4, 0, 0.2, 1), cubic-bezier(0.4, 0, 0.2, 1), cubic-bezier(0.4, 0, 0.2, 1), cubic-bezier(0.4, 0, 0.2, 1) delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.AZdcjW_root.AZdcjW_variant-default 55.0x30.0 bg #1f1f1f border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | a.AZdcjW_root.AZdcjW_variant-default 55.0x30.0 bg #262626 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | a.AZdcjW_root.AZdcjW_variant-default 55.0x30.0 bg #262626 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | = | = | 0.8 |

Crops: `gal-open-default.png`, `gal-open-hover.png`, `gal-open-focus-visible.png`, `gal-open-pressed.png`.

#### gal-comm

Community menu button. The "Community" dropdown button in the gallery header — a local UI toggle; measured, never toggled.

Page: gallery. Selector: `gallery Community button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117 x 30 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #1f1f1f | #262626 | = | #262626 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | inter 12px/18px 450 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.q0Xw5q_label: inter 12px/normal 450, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 15, colour #ffffff | = | = | = |
| Painted layers | button.q0Xw5q_trigger 117.0x30.0 bg #1f1f1f r 8px | button.q0Xw5q_trigger 117.0x30.0 bg #262626 r 8px | = | button.q0Xw5q_trigger 117.0x30.0 bg #262626 r 8px |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `gal-comm-default.png`, `gal-comm-hover.png`, `gal-comm-focus-visible.png`, `gal-comm-pressed.png`.

### Mobile (390 wide)

#### m-topbar

Mobile top bar. The phone header at 390 wide: the Framer mark and the nav toggle.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 64 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text: Inter Variable 14px/14px 400, #ffffff, ls -0.01px |
| Transition | none |
| Cursor | default |
| Painted layers | div.framer-ngytjn 16.0x24.0 image url(data:…)%22></path></svg>"); a.framer-16mrjhl.framer-enysp5 64.1x30.0 bg #ffffff r 8px; div.framer-cw6b3u 20.0x2.0 bg #ffffff r 10px; div.framer-1ctjw9m 20.0x2.0 bg #ffffff r 10px; div.framer-1gyv5v7 390.0x64.0 bg #000000 |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-menu-btn

Mobile menu button. The header nav toggle at 390 wide — a local UI toggle; the opened state was measured after activating it.

Page: mobile. Selector: `mobile nav toggle`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 64 x 64 | = | - | = | = |
| Padding | 0px | = | - | = | = |
| Border | none | = | - | = | = |
| Radius | 0px | = | - | = | = |
| Background | transparent | = | - | = | = |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | sans-serif 12px/normal 400 | = | - | = | = |
| Letter spacing | normal | = | - | = | = |
| Colour | #000000 | = | - | = | = |
| Transition | none | = | - | = | = |
| Transform | matrix(1, 0, 0, 1, 0, -32) | = | - | = | matrix(1, 0, 0, 6.72655, 0, 183.25) |
| Cursor | default | = | - | = | = |
| Painted layers | div.framer-cw6b3u 20.0x2.0 bg #ffffff r 10px; div.framer-1ctjw9m 20.0x2.0 bg #ffffff r 10px | = | - | = | div.framer-cw6b3u 20.0x2.0 bg #ffffff r 50% / 500%; div.framer-1ctjw9m 20.0x2.0 bg #ffffff r 50% / 500% |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | own toggle |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `m-menu-btn-default.png`, `m-menu-btn-hover.png`, `m-menu-btn-pressed.png`, `m-menu-btn-opened.png`.

#### m-drawer

Mobile nav overlay. The nav overlay opened by the menu button (the page links plus Log in/Sign up); its links were never followed.

Page: mobile. Selector: `mobile nav overlay`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text: Inter Variable 14px/14px 400, #ffffff, ls -0.01px |
| Transition | none |
| Painted layers | nav.framer-vzLJR.framer-140pdlc 390.0x844.0 bg #000000; div.framer-z96yy7 390.0x844.0 bg #000000; div.framer-ngytjn 16.0x24.0 image url(data:…)%22></path></svg>"); a.framer-uTdPy.framer-aZ6KF 55.2x19.6 bg #ffffff @ 0 r 8px; div.framer-4mgnl8 51.2x15.6 bg #ffffff @ 0.1 r 8px; a.framer-uTdPy.framer-aZ6KF 60.1x19.6 bg #ffffff @ 0 r 8px |
| Ancestor paint | 1 up div.framer-nwUvx.framer-k4Apk bg #000000 |
| How | at rest |

Crops: `m-drawer-default.png`.

#### m-hero-h1

Mobile hero headline. The masthead at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Walsheim Medium 36px/36px 500 |
| Letter spacing | -1.44px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-hero-cta

Mobile hero CTA. The hero "Get started for free" pill at 390 wide; measured never followed.

Page: mobile. Selector: `mobile hero CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 137.81 x 29 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 7px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Inter Variable 13px/13px 400, #000000, ls -0.26px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-R3ehQ.framer-qkzqfa 137.8x29.0 bg #ffffff r 8px | = | a.framer-R3ehQ.framer-qkzqfa 137.8x29.0 bg #ffffff r 8px outline 1px auto #e59700 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-hero-cta-default.png`, `m-hero-cta-hover.png`, `m-hero-cta-focus-visible.png`, `m-hero-cta-pressed.png`.

## Transitions declared in the readable stylesheets

www.framer.com is a Framer site: its CSS is one linked /sites/…/*.css bundle plus the Framer runtime's inline <style> blocks, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- home: `color 0.2s cubic-bezier(0.44, 0, 0.56, 1)`, `color cubic-bezier(0, 0, 1, 1)`, `color 0.15s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `opacity 0.4s ease-out`, `unset`, `0.3s ease-in-out`

## Reduced motion

- home (`a[href*="signup"], a[href*="login"]` under prefers-reduced-motion): transition `color cubic-bezier(0, 0, 1, 1)`, animation `none 0s ease 0s 1 normal none running`, html scroll-behavior `auto`
