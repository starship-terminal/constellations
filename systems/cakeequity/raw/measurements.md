# Component measurements

Computed styles read from cakeequity.com on 2026-11-11 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844 requested — the page forces a ~745px layout viewport there; see m-header) across the light marketing pages plus the Kinde-hosted login card on authentication.cakeequity.com — with the Chatbase assistant widget hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The fixed marketing navbar: wordmark, Product/Solutions/Resources/Customers mega-nav, Pricing link, Login, Book-a-demo and Get-started-free.

Page: home. Selector: `div.navbar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 74.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #000000 @ 0.2 0px 2px 20px -19px |
| Outline | none |
| Font | Inter 14px/16.8px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.nav-link: Inter 14px/18.2px 400, #222222 |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | div.navbar.w-nav 1440.0x74.2 shadow #000000 @ 0.2 0px 2px 20px -19px; div.navbar-bg-shadow 1440.0x0.0 shadow #000000 @ 0.1 0px 1px 30px 0px; div.absolute-border 0.0x2.0 bg #7e78ff; div.nav-container.for-dropdown 0.0x0.0 bg #ffffff r 20px shadow #18161a @ 0.25 0px 0px 20px -5px; div.nav-grid-column-item 0.0x0.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff; div.spacer-with-line 0.0x0.0 bg #18161a @ 0.1 |
| Ancestor paint | 1 up div.navbar-wrap bg #ffffff |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The cake. wordmark anchor.

Page: home. Selector: `a.navbar-logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 100 x 31.7 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/0px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### nav-trigger

Nav trigger. The Product mega-nav toggle; opens its panel on hover (Webflow w-dropdown), never followed.

Page: home. Selector: `.nav-menu-dropdown .w-dropdown-toggle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 95.95 x 58.19 | = | = | = |
| Padding | 20px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/18.2px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | #4823ff | = | #4823ff |
| Text node | div.nav-link: Inter 14px/18.2px 400, #222222 | div.nav-link: Inter 14px/18.2px 400, #4823ff | = | div.nav-link: Inter 14px/18.2px 400, #4823ff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.absolute-border 0.0x2.0 bg #7e78ff | div.absolute-border 96.0x2.0 bg #7e78ff | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### nav-link

Nav link. The plain Pricing header link.

Page: home. Selector: `header Pricing link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 45.28 x 18.19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/18.2px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | #4823ff | = | #4823ff |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.nav-link.w-nav-link 45.3x18.2 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Login link. The Login header action (links to app.cakeequity.com); measured never followed.

Page: home. Selector: `.primary-nav-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 88.19 x 44.19 | = | = | = |
| Padding | 12px 25px 10px 25px | = | = | = |
| Border | 1px solid #000000 @ 0 | 1px solid #7e78ff @ 0.25 | = | 1px solid #7e78ff @ 0.25 |
| Radius | 50px | = | = | = |
| Background | transparent | #7e78ff @ 0.25 | = | #7e78ff @ 0.25 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/18.2px 400 | = | = | = |
| Letter spacing | -0.02px | = | = | = |
| Colour | #18161a | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.primary-nav-button.transparent 88.2x44.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 50px | a.primary-nav-button.transparent 88.2x44.2 bg #7e78ff @ 0.25 border T:1px solid #7e78ff @ 0.25 / R:1px solid #7e78ff @ 0.25 / B:1px solid #7e78ff @ 0.25 / L:1px solid #7e78ff @ 0.25 r 50px | a.primary-nav-button.transparent 88.2x44.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 50px outline 1px auto #005fcc offset 1px | a.primary-nav-button.transparent 88.2x44.2 bg #7e78ff @ 0.25 border T:1px solid #7e78ff @ 0.25 / R:1px solid #7e78ff @ 0.25 / B:1px solid #7e78ff @ 0.25 / L:1px solid #7e78ff @ 0.25 r 50px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-demo

Book-a-demo button. The secondary header action (primary-button-nav light-grey).

Page: home. Selector: `a.primary-button-nav.light-grey`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 124.36 x 44.19 | = | = | = |
| Padding | 12px 18px | = | = | = |
| Border | 1px solid #4823ff | 1px solid #2b1599 | = | 1px solid #2b1599 |
| Radius | 100px | = | = | = |
| Background | #ffffff @ 0 | #2b1599 | = | #2b1599 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/18.2px 400 | = | = | = |
| Letter spacing | -0.02px | = | = | = |
| Colour | #4823ff | #ffffff | = | #ffffff |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.primary-button-nav.light-grey 124.4x44.2 bg #ffffff @ 0 border T:1px solid #4823ff / R:1px solid #4823ff / B:1px solid #4823ff / L:1px solid #4823ff r 100px | a.primary-button-nav.light-grey 124.4x44.2 bg #2b1599 border T:1px solid #2b1599 / R:1px solid #2b1599 / B:1px solid #2b1599 / L:1px solid #2b1599 r 100px | a.primary-button-nav.light-grey 124.4x44.2 bg #ffffff @ 0 border T:1px solid #4823ff / R:1px solid #4823ff / B:1px solid #4823ff / L:1px solid #4823ff r 100px outline 1px auto #005fcc offset 1px | a.primary-button-nav.light-grey 124.4x44.2 bg #2b1599 border T:1px solid #2b1599 / R:1px solid #2b1599 / B:1px solid #2b1599 / L:1px solid #2b1599 r 100px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-demo-default.png`, `nav-demo-hover.png`, `nav-demo-focus-visible.png`, `nav-demo-pressed.png`.

#### nav-cta

Nav CTA. The Get-started-free header action; links to the app signup, measured never followed.

Page: home. Selector: `a.primary-button-nav`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 143.39 x 44.19 | = | = | = |
| Padding | 12px 18px | = | = | = |
| Border | 1px solid #4823ff | 1px solid #2b1599 | = | 1px solid #2b1599 |
| Radius | 100px | = | = | = |
| Background | #4823ff | #2b1599 | = | #2b1599 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/18.2px 400 | = | = | = |
| Letter spacing | -0.02px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.primary-button-nav.w-button 143.4x44.2 bg #4823ff border T:1px solid #4823ff / R:1px solid #4823ff / B:1px solid #4823ff / L:1px solid #4823ff r 100px | a.primary-button-nav.w-button 143.4x44.2 bg #2b1599 border T:1px solid #2b1599 / R:1px solid #2b1599 / B:1px solid #2b1599 / L:1px solid #2b1599 r 100px | a.primary-button-nav.w-button 143.4x44.2 bg #4823ff border T:1px solid #4823ff / R:1px solid #4823ff / B:1px solid #4823ff / L:1px solid #4823ff r 100px outline 1px auto #005fcc offset 1px | a.primary-button-nav.w-button 143.4x44.2 bg #2b1599 border T:1px solid #2b1599 / R:1px solid #2b1599 / B:1px solid #2b1599 / L:1px solid #2b1599 r 100px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-dropdown

Mega-nav panel. The Product mega-menu panel, opened by hovering its own trigger.

Page: home. Selector: `.nav-dropdown.w-dropdown-list.w--open`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1008 x 459.38 |
| Padding | 0px 8px 40px 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/18.2px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.text-block-150: Inter 12.6px/16.38px 400, #333333 |
| Transition | none |
| Painted layers | div.nav-container.for-dropdown 992.0x407.4 bg #ffffff r 20px shadow #18161a @ 0.25 0px 0px 20px -5px; div.nav-grid-column-item 213.2x299.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff; div.spacer-with-line 211.2x1.0 bg #18161a @ 0.1; div.product-shipped.now-live 63.5x22.0 bg #ebffe9 r 50px; div.nav-grid-column-item.equity-incentive 236.8x299.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff; div.spacer-with-line 234.8x1.0 bg #18161a @ 0.1 |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-link

Menu link. A feature link inside the opened mega-nav.

Page: home. Selector: `mega-nav link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 211.16 x 46.88 | = | = | = |
| Padding | 10px 0px 10px 45px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #7e78ff @ 0.1 | #7e78ff @ 0.1 | #7e78ff @ 0.1 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16.8px/26.88px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #18161a | #4823ff | #4823ff | #4823ff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Background image | - | url(…) | url(…) | url(…) |
| Painted layers | - | a.nav-menu-text.main 211.2x46.9 bg #7e78ff @ 0.1 | a.nav-menu-text.main 211.2x46.9 bg #7e78ff @ 0.1 | a.nav-menu-text.main 211.2x46.9 bg #7e78ff @ 0.1 |

Crops: `menu-link-default.png`, `menu-link-hover.png`, `menu-link-focus-visible.png`, `menu-link-pressed.png`.

### Home

#### announce-pill

Announcement pill. The Pulley announcement chip above the hero (links to the managed-migration section anchor).

Page: home. Selector: `a.pm-mig-chip-2`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 334.83 x 37 | = | = | = |
| Padding | 5px 16px 5px 5px | = | = | = |
| Gap | normal 10px | = | = | = |
| Border | 1px solid #ebe8f2 | = | = | = |
| Radius | 100px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 15px/16.8px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #18161a | #4823ff | = | #4823ff |
| Text node | div: Inter 15px/16.8px 500, #18161a | div: Inter 15px/16.8px 500, #4823ff | = | div: Inter 15px/16.8px 500, #4823ff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.pm-mig-chip-2.pagination-next-skip 334.8x37.0 bg #ffffff border T:1px solid #ebe8f2 / R:1px solid #ebe8f2 / B:1px solid #ebe8f2 / L:1px solid #ebe8f2 r 100px; div.pm-pulley-tag 63.8x25.0 bg #616d3b image linear-gradient(#616d3b 0%, #616d3b 55%, #906a37 78%, #c96733 100%) r 100px | = | a.pm-mig-chip-2.pagination-next-skip 334.8x37.0 bg #ffffff border T:1px solid #ebe8f2 / R:1px solid #ebe8f2 / B:1px solid #ebe8f2 / L:1px solid #ebe8f2 r 100px outline 1px auto #005fcc offset 1px; div.pm-pulley-tag 63.8x25.0 bg #616d3b image linear-gradient(#616d3b 0%, #616d3b 55%, #906a37 78%, #c96733 100%) r 100px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `announce-pill-default.png`, `announce-pill-hover.png`, `announce-pill-focus-visible.png`, `announce-pill-pressed.png`.

#### hero-title

Hero headline. The "The equity platform for growing startups" display headline in Exposure.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 579.69 x 132 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Exposure Light 60px/66px 400 |
| Letter spacing | -2px |
| Colour | #18161a |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero copy. The lede under the headline (body-medium).

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 579.69 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/32px 300 |
| Letter spacing | -0.3px |
| Colour | #18161a |
| Text node | strong: Inter 20px/32px 600, #18161a, ls -0.3px |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-cta

Hero CTA. The hero Get-started action (primary-button-v2); links to the app signup, measured never followed.

Page: home. Selector: `a.primary-button-v2`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 188.5 x 58.8 | = | = | = |
| Padding | 20px 36px | = | = | = |
| Border | 1px solid #4823ff | 1px solid #2b1599 | = | 1px solid #2b1599 |
| Radius | 100px | = | = | = |
| Background | #4823ff | #2b1599 | = | #2b1599 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 19.2px/16.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.primary-button-v2 188.5x58.8 bg #4823ff border T:1px solid #4823ff / R:1px solid #4823ff / B:1px solid #4823ff / L:1px solid #4823ff r 100px | a.primary-button-v2 188.5x58.8 bg #2b1599 border T:1px solid #2b1599 / R:1px solid #2b1599 / B:1px solid #2b1599 / L:1px solid #2b1599 r 100px | a.primary-button-v2 188.5x58.8 bg #4823ff border T:1px solid #4823ff / R:1px solid #4823ff / B:1px solid #4823ff / L:1px solid #4823ff r 100px outline 1px auto #005fcc offset 1px | a.primary-button-v2 188.5x58.8 bg #2b1599 border T:1px solid #2b1599 / R:1px solid #2b1599 / B:1px solid #2b1599 / L:1px solid #2b1599 r 100px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-demo

Hero secondary. The hero Book-a-demo ghost button (transparent-button-v2).

Page: home. Selector: `a.transparent-button-v2`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 188.5 x 58.8 | = | = | = |
| Padding | 20px 36px | = | = | = |
| Border | 1px solid #4823ff | 1px solid #2b1599 | = | 1px solid #2b1599 |
| Radius | 100px | = | = | = |
| Background | #ffffff @ 0 | #2b1599 | = | #2b1599 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #015ecc offset 0.984375px | = |
| Font | Inter 19.2px/16.8px 400 | = | = | = |
| Letter spacing | -0.384px | = | = | = |
| Colour | #4823ff | #ffffff | = | #ffffff |
| Transition | all 0.4s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.transparent-button-v2 188.5x58.8 bg #ffffff @ 0 border T:1px solid #4823ff / R:1px solid #4823ff / B:1px solid #4823ff / L:1px solid #4823ff r 100px | a.transparent-button-v2 188.5x58.8 bg #2b1599 border T:1px solid #2b1599 / R:1px solid #2b1599 / B:1px solid #2b1599 / L:1px solid #2b1599 r 100px | a.transparent-button-v2 188.5x58.8 bg #ffffff @ 0 border T:1px solid #4823ff / R:1px solid #4823ff / B:1px solid #4823ff / L:1px solid #4823ff r 100px outline 1px auto #015ecc offset 0.984375px | a.transparent-button-v2 188.5x58.8 bg #2b1599 border T:1px solid #2b1599 / R:1px solid #2b1599 / B:1px solid #2b1599 / L:1px solid #2b1599 r 100px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-demo-default.png`, `hero-demo-hover.png`, `hero-demo-focus-visible.png`, `hero-demo-pressed.png`.

#### eyebrow

Section eyebrow. A small-caps section label (eyebrow-2 plum).

Page: home. Selector: `.eyebrow-2.plum`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 152 x 29.2 |
| Padding | 5px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/19.2px 600 |
| Letter spacing | 0.8px |
| Colour | #18161a @ 0.5 |
| Transition | none |
| How | at rest |

Crops: `eyebrow-default.png`.

#### section-h2

Section heading. A 44px section heading.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 565.33 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Exposure Light 44px/44px 300 |
| Letter spacing | -1px |
| Colour | #18161a |
| Transition | none |
| Painted layers | span.hp26-mark 349.3x53.0 image linear-gradient(#000000 @ 0 64%, #e7ff6e 64%, #e7ff6e 93%, #000000 @ 0 93%) |
| How | at rest |

Crops: `section-h2-default.png`.

#### dark-section

Dark band. The Cake-MCP section: the one dark surface on the page (hp26-aidark-2).

Page: home. Selector: `section.hp26-aidark-2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1296 x 635 |
| Padding | 0px |
| Border | none |
| Radius | 28px |
| Background | #0e0d12 |
| Background image | url(…) |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/16.8px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.eyebrow.lemon: Inter 14px/16.8px 600, #e7ff6e, ls 0.7px |
| Transition | none |
| Painted layers | section.hp26-aidark-2.pm-mcp-sec 1296.0x635.0 bg #0e0d12 r 28px; div.hp26-acc 540.9x145.2 border T:1px solid #f4f4f4 @ 0.18; div.hp26-acc 540.9x125.0 border T:1px solid #f4f4f4 @ 0.18; a.resource-cta-text.link-right-chev 98.1x26.8 bg #ffffff @ 0 |
| Ancestor paint | 1 up section.main-section bg #ffffff |
| How | at rest |

Crops: `dark-section-default.png`.

#### story-card

Story card. A customer-quote card in the stories section.

Page: home. Selector: `.story-card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 420 x 102.73 | = | - | = |
| Padding | 16px | = | - | = |
| Gap | 8px | = | - | = |
| Border | none | = | - | = |
| Radius | 16px | = | - | = |
| Background | #ffffff | = | - | = |
| Box shadow | #000000 @ 0.2 0px 2px 5px 0px | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 16px/16.8px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #0000ee | #4823ff | - | = |
| Text node | p.story-quote-hover-home: Exposure Light 18px/23.4px 300, #18161a | = | - | = |
| Transition | opacity 0.2s ease | = | - | = |
| Transform | matrix(1, 0, 0, 1, -210, -6) | matrix(1, 0, 0, 1, -210, -12) | - | = |
| Opacity | 0 | - | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | div.story-card 420.0x102.7 bg #ffffff r 16px shadow #000000 @ 0.2 0px 2px 5px 0px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `story-card-default.png`, `story-card-hover.png`, `story-card-pressed.png`.

#### faq-item

FAQ item. A Frequently-Asked accordion card; toggled open by clicking its question wrap (a local UI toggle revealing the answer).

Page: home. Selector: `.faq-item-card`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 907.19 x 79.88 | 907.19 x 301.64 |
| Padding | 16px 0px | = |
| Border | T: none; R: none; B: 1px solid #18161a @ 0.1; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | #000000 @ 0.2 0px 2px 10px -8px |
| Outline | none | = |
| Font | Inter 16px/16.8px 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | = |
| Text node | h4.h4-faq: Inter 22.4px/26.88px 300, #18161a, ls -0.3px | = |
| Transition | transform 0.3s ease | = |
| Cursor | pointer | = |
| Painted layers | div.faq-item-card 907.2x79.9 border B:1px solid #18161a @ 0.1; div.faq-open-icon-vertical 1.0x12.0 bg #7e78ff r 20px; div.faq-open-icon-horizontal 12.0x1.0 bg #7e78ff r 20px | div.faq-item-card 907.2x301.6 border B:1px solid #18161a @ 0.1 shadow #000000 @ 0.2 0px 2px 10px -8px; div.faq-open-icon-vertical 12.0x1.0 bg #7e78ff r 20px; div.faq-open-icon-horizontal 12.0x1.0 bg #7e78ff r 20px |
| How | at rest | own toggle |
| Transform | - | matrix(1, 0, 0, 1, 0, -2) |

Crops: `faq-item-default.png`, `faq-item-opened.png`.

### Pricing

#### pricing-h1

Pricing title. The "Growth-friendly pricing, no complexity" display heading.

Page: pricing. Selector: `h1 on /pricing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1043.23 x 66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Exposure Light 60px/66px 400 |
| Letter spacing | -2px |
| Colour | #18161a |
| Transition | none |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### country-select

Country select. The region <select> (United States/Canada/Australia/UK/Singapore/New Zealand) that re-prices the plans; geo-defaulted to Singapore in this capture. Tapped into focus, never changed.

Page: pricing. Selector: `#countrySelect`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 200 x 48 | = |
| Padding | 8px 18px | = |
| Border | 1px solid #d9d9e0 | 1px solid #3898ec |
| Radius | 100px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/normal 500 | = |
| Letter spacing | normal | = |
| Colour | #18161a | = |
| Transition | none | = |
| Cursor | default | = |
| Painted layers | select.text-field-7.w-input 200.0x48.0 bg #ffffff border T:1px solid #d9d9e0 / R:1px solid #d9d9e0 / B:1px solid #d9d9e0 / L:1px solid #d9d9e0 r 100px | select.text-field-7.w-input 200.0x48.0 bg #ffffff border T:1px solid #3898ec / R:1px solid #3898ec / B:1px solid #3898ec / L:1px solid #3898ec r 100px |
| How | at rest | clicked into the field |

Crops: `country-select-default.png`, `country-select-focused.png`.

#### billing-toggle

Billing toggle. The Yearly/Quarterly save switch (label.w-checkbox over #cycleCheckbox); a local UI toggle measured at rest — clicking it re-prices client-side, captured in screenshots only.

Page: pricing. Selector: `label.w-checkbox.ms-switch-wrap`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 236 x 48 |
| Padding | 0px 0px 0px 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16.8px 700 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | span.ms-switch-option.yearly: Inter 14px/16.8px 500, #ffffff |
| Transition | none |
| Cursor | default |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | div.ms-switch-select.yearly 114.0x40.0 bg #18161a r 999px; div.save-pill-div 43.6x20.8 bg #c6f0dc r 30px; div.ms-switch-bg 236.0x48.0 bg #ffffff border T:1px solid #d9d9e0 / R:1px solid #d9d9e0 / B:1px solid #d9d9e0 / L:1px solid #d9d9e0 r 999px |
| How | at rest |

Crops: `billing-toggle-default.png`.

#### calc-field

Calculator field. The estimate inputs of the pricing form — they all sit in .pp-hidden-fields (display:none) behind the country select, so nothing paints; recorded missing.

Page: pricing. Selector: `calculator input`. States: .

Not found on the page at capture time.

#### plan-card

Plan card. The Growth plan card (.pricing-cards.pop, the featured tier).

Page: pricing. Selector: `.pricing-cards.pop`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 312 x 741.2 |
| Padding | 0px |
| Gap | 0px |
| Border | 1px solid #7e78ff @ 0.25 |
| Radius | 0px 0px 20px 20px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16.8px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | h4.pricing-card-name: Inter 20px/24px 500, #18161a, ls -0.4px |
| Transition | none |
| Painted layers | div.pricing-cards.pop 312.0x741.2 bg #ffffff border T:1px solid #7e78ff @ 0.25 / R:1px solid #7e78ff @ 0.25 / B:1px solid #7e78ff @ 0.25 / L:1px solid #7e78ff @ 0.25 r 0px 0px 20px 20px; div.pricing-card-top.tabbed 310.0x181.4 bg #faf9ff image url(data:…), none border B:1px solid #18161a @ 0.1; div.most-pop-pill-div 312.0x32.0 bg #ede9ff border T:1px solid #7e78ff @ 0.25 / R:1px solid #7e78ff @ 0.25 / L:1px solid #7e78ff @ 0.25 r 16px 16px 0px 0px; div.most-pop-pill-div.annual-only-pill-div 0.0x0.0 bg #ececf0 @ 0.5 border T:1px solid #18161a @ 0.1 / R:1px solid #18161a @ 0.1 / L:1px solid #18161a @ 0.1 r 16px 16px 0px 0px; div.save-batch-2 77.8x20.4 bg #c6f0dc r 20px; a.primary-button-v2.short 270.0x49.0 bg #4823ff border T:1px solid #4823ff / R:1px solid #4823ff / B:1px solid #4823ff / L:1px solid #4823ff r 100px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-price

Plan price. A plan card's price figure (S$1,128 annually for the detected region).

Page: pricing. Selector: `.price-card-rate`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 262 x 40 |
| Padding | 0px |
| Gap | 8px normal |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16.8px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.currency-span: Inter 40px/40px 400, #18161a, ls -1.6px |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-badge

Plan badge. The "Most popular" pill on the featured plan card.

Page: pricing. Selector: `.most-popular-pill`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 80.91 x 13 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 13px/13px 500 |
| Letter spacing | normal |
| Colour | #4823ff |
| Transition | none |
| How | at rest |

Crops: `plan-badge-default.png`.

#### plan-cta

Plan CTA. A plan Start-free action; links to the app signup, measured never followed.

Page: pricing. Selector: `a.primary-button-v2.paid-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 270 x 49 | = | = | = |
| Padding | 13px 20px | = | = | = |
| Border | 1px solid #4823ff | 1px solid #2b1599 | = | 1px solid #2b1599 |
| Radius | 100px | = | = | = |
| Background | #4823ff | #2b1599 | = | #2b1599 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 15px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.primary-button-v2.short 270.0x49.0 bg #4823ff border T:1px solid #4823ff / R:1px solid #4823ff / B:1px solid #4823ff / L:1px solid #4823ff r 100px | a.primary-button-v2.short 270.0x49.0 bg #2b1599 border T:1px solid #2b1599 / R:1px solid #2b1599 / B:1px solid #2b1599 / L:1px solid #2b1599 r 100px | a.primary-button-v2.short 270.0x49.0 bg #4823ff border T:1px solid #4823ff / R:1px solid #4823ff / B:1px solid #4823ff / L:1px solid #4823ff r 100px outline 1px auto #005fcc offset 1px | a.primary-button-v2.short 270.0x49.0 bg #2b1599 border T:1px solid #2b1599 / R:1px solid #2b1599 / B:1px solid #2b1599 / L:1px solid #2b1599 r 100px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

### Blog and demo

#### feature-h1

Feature headline. The /features/cap-table display heading; one of ~25 sibling feature pages on the same template.

Page: feature. Selector: `h1 on /features/cap-table`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 478.39 x 132 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Exposure Light 60px/66px 400 |
| Letter spacing | -2px |
| Colour | #18161a |
| Transition | none |
| How | at rest |

Crops: `feature-h1-default.png`.

#### blog-h1

Blog title. The "Cake blog" heading.

Page: blog. Selector: `h1 on /blog`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 265.36 x 66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Exposure Light 60px/66px 400 |
| Letter spacing | -2px |
| Colour | #18161a |
| Transition | none |
| How | at rest |

Crops: `blog-h1-default.png`.

#### collection-card

Article card. A blog collection card (the featured post).

Page: blog. Selector: `.collection-card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 693.36 x 695.92 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/16.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | #18161a | = | = |
| Text node | h2: Exposure Light 44px/44px 300, #18161a, ls -1px | = | = | = |
| Transition | none | = | = | = |
| Painted layers | a.resource-cta-text.link-right-chev 94.0x29.2 bg #ffffff @ 0 | = | a.card-link-overlay.w-inline-block 693.4x695.9 outline 1px auto #005fcc offset 1px; a.resource-cta-text.link-right-chev 94.0x29.2 bg #ffffff @ 0 | = |
| Ancestor paint | 1 up div.col-card-wrap-image.large bg #ffffff | 1 up div.col-card-wrap-image.large bg #ffffff shadow #000000 @ 0.2 0px 0px 20px -10px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `collection-card-default.png`, `collection-card-hover.png`, `collection-card-focus-visible.png`, `collection-card-pressed.png`.

#### demo-h1

Demo title. The /demo-request heading.

Page: demo. Selector: `h1 on /demo-request`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 536.77 x 198 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Exposure Light 60px/66px 400 |
| Letter spacing | -2px |
| Colour | #18161a |
| Transition | none |
| How | at rest |

Crops: `demo-h1-default.png`.

#### demo-form

Demo form embed. The HubSpot form region (a cross-origin hsforms.net iframe; its inner fields are third-party paint, documented as a boundary).

Page: demo. Selector: `.form-grid-embed`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 599.59 x 1122.13 |
| Padding | 20px |
| Border | none |
| Radius | 20px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/16.8px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.body-smaller.italic: Inter 15.4px/21.56px 300, #18161a |
| Transition | none |
| Painted layers | div.form-grid-embed 599.6x1122.1 bg #ffffff r 20px; div.code-embed-8.w-embed 559.6x999.0 bg #ffffff |
| How | at rest |

Crops: `demo-form-default.png`.

### Login (Kinde hosted auth)

#### login-card

Login card. The Kinde hosted-auth card (Welcome back): email field, Continue, Google and LinkedIn OAuth.

Page: login. Selector: `article.kinde-layout-page-card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 496 x 608.53 |
| Padding | 48px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | -0.08px |
| Colour | #2b2b2b |
| Text node | h1.kinde-heading.kinde-heading-variant-large: Inter 24px/31.9999px 500, #0f0f0f, ls -0.48px |
| Transition | none |
| Icon | 24 x 24, colour #0f0f0f |
| Painted layers | article.kinde-layout-page-card 496.0x608.5 bg #ffffff r 16px; input.kinde-control-select-text 400.0x48.0 border T:1px solid #ababab / R:1px solid #ababab / B:1px solid #ababab / L:1px solid #ababab r 8px; button.kinde-button.kinde-button-variant-primary 400.0x48.0 bg #5a38fd border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; button.kinde-button.kinde-button-variant-secondary 400.0x48.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; button.kinde-button.kinde-button-variant-secondary 400.0x48.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest |

Crops: `login-card-default.png`.

#### login-title

Login title. The "Welcome back" auth heading.

Page: login. Selector: `h1.kinde-heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 400 x 31.98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 24px/31.9999px 500 |
| Letter spacing | -0.48px |
| Colour | #0f0f0f |
| Transition | none |
| How | at rest |

Crops: `login-title-default.png`.

#### login-field

Email field. The auth email input; tapped into focus, never typed into or submitted.

Page: login. Selector: `input.kinde-control-select-text`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 400 x 48 | = |
| Padding | 12px | = |
| Border | 1px solid #ababab | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | 2px solid #0054f0 offset 2px |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #2b2b2b | = |
| Transition | outline-offset, border-color 0.15s, 0.15s cubic-bezier(0.25, 0, 0.1, 1), cubic-bezier(0.25, 0, 0.1, 1) delay 0s, 0s | = |
| Cursor | text | = |
| Placeholder | #2b2b2b, opacity 1 | = |
| Painted layers | input.kinde-control-select-text 400.0x48.0 border T:1px solid #ababab / R:1px solid #ababab / B:1px solid #ababab / L:1px solid #ababab r 8px | input.kinde-control-select-text 400.0x48.0 border T:1px solid #ababab / R:1px solid #ababab / B:1px solid #ababab / L:1px solid #ababab r 8px outline 2px solid #0054f0 offset 2px |
| How | at rest | clicked into the field |

Crops: `login-field-default.png`, `login-field-focused.png`.

#### login-cta

Continue button. The primary Continue action (a submit button — measured, never pressed for real).

Page: login. Selector: `button.kinde-button-variant-primary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 48 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #5a38fd | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0054f0 offset 2px | = |
| Font | Inter 16px/24px 500 | = | = | = |
| Letter spacing | -0.08px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.kinde-button-text: Inter 16px/24px 500, #ffffff, ls -0.08px | = | = | = |
| Transition | outline-offset, background-color 0.15s, 0.15s cubic-bezier(0.25, 0, 0.1, 1), cubic-bezier(0.25, 0, 1, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.kinde-button.kinde-button-variant-primary 400.0x48.0 bg #5a38fd border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | button.kinde-button.kinde-button-variant-primary 400.0x48.0 bg #5a38fd border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px outline 2px solid #0054f0 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-cta-default.png`, `login-cta-hover.png`, `login-cta-focus-visible.png`, `login-cta-pressed.png`.

#### login-oauth

OAuth button. A secondary Continue-with provider button (Google/LinkedIn).

Page: login. Selector: `button.kinde-button-variant-secondary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 48 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #f5f5f5 | #ebebeb | = | #dbdbdb |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0054f0 offset 2px | = |
| Font | Inter 16px/24px 500 | = | = | = |
| Letter spacing | -0.08px | = | = | = |
| Colour | #0f0f0f | = | = | = |
| Text node | span.kinde-button-text: Inter 16px/24px 500, #0f0f0f, ls -0.08px | = | = | = |
| Transition | outline-offset, background-color 0.15s, 0.15s cubic-bezier(0.25, 0, 0.1, 1), cubic-bezier(0.25, 0, 1, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #0f0f0f | = | = | = |
| Painted layers | button.kinde-button.kinde-button-variant-secondary 400.0x48.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.kinde-button.kinde-button-variant-secondary 400.0x48.0 bg #ebebeb border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.kinde-button.kinde-button-variant-secondary 400.0x48.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px outline 2px solid #0054f0 offset 2px | button.kinde-button.kinde-button-variant-secondary 400.0x48.0 bg #dbdbdb border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-oauth-default.png`, `login-oauth-hover.png`, `login-oauth-focus-visible.png`, `login-oauth-pressed.png`.

#### login-link

Create-one link. The "Create one" signup link under the OAuth buttons.

Page: login. Selector: `a.kinde-text-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 83.11 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 2px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0054f0 offset 2px | = |
| Font | Inter 16px/24px 500 | = | = | = |
| Letter spacing | -0.08px | = | = | = |
| Colour | #1c029d | = | = | = |
| Transition | outline-offset, color 0.15s, 0.15s cubic-bezier(0.25, 0, 0.1, 1), cubic-bezier(0.9, 0, 0.1, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.kinde-text-link.kinde-text-link-is-inline 83.1x20.0 r 2px outline 2px solid #0054f0 offset 2px | = |

Crops: `login-link-default.png`, `login-link-hover.png`, `login-link-focus-visible.png`, `login-link-pressed.png`.

### Footer

#### footer

Footer. The footer-section: office address, link columns, socials, legal.

Page: home. Selector: `.footer-section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 659.08 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #18161a |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/16.8px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.body-smaller.white: Inter 15.4px/21.56px 300, #ffffff |
| Transition | none |
| Painted layers | div.footer-section 1440.0x659.1 bg #18161a |
| Ancestor paint | 1 up body bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.48 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/16px 300 | = | = | = |
| Letter spacing | -0.16px | = | = | = |
| Colour | #ffffff | #7e78ff | = | #7e78ff |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.footer-link-16px 85.5x20.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-icon

Social link. A social link in the footer.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 25 x 25 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/16.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | #4823ff | = | #4823ff |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, -5) | = | matrix(1, 0, 0, 1, 0, -5) |
| Painted layers | - | = | a.social-profile-wrapper.w-inline-block 25.0x25.0 outline 1px auto #005fcc offset 1px | = |

Crops: `social-icon-default.png`, `social-icon-hover.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The navbar at 390 — the page forces a ~745px layout viewport (a .comparison-grid min-width:700px plus navbar chrome), so the hamburger sits outside the 390 visual viewport: the shots record what a phone actually paints.

Page: mobile. Selector: `.navbar at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 745 x 68 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #000000 @ 0.2 0px 2px 20px -19px |
| Outline | none |
| Font | Inter 14px/16.8px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | div.navbar.w-nav 745.0x68.0 shadow #000000 @ 0.2 0px 2px 20px -19px; div.navbar-bg-shadow 745.0x0.0 shadow #000000 @ 0.1 0px 1px 30px 0px; nav.navbar-menu.w-nav-menu 0.0x0.0 bg #ffffff; div.nav-menu_link-wrap.w-dropdown-toggle 0.0x0.0 border B:1px solid #cfdbde; div.absolute-border 0.0x0.0 bg #7e78ff; div.nav-container.for-dropdown 0.0x0.0 bg #ffffff r 10px |
| Ancestor paint | 1 up div.navbar-wrap bg #ffffff |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The hamburger (menu-button w-nav-button); painted at x~660 of the forced 745 layout, off the 390 visual viewport.

Page: mobile. Selector: `.w-nav-button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 48 x 48 |
| Padding | 8px |
| Border | none |
| Radius | 4px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 24px/16.8px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 351 x 228.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Exposure Light 52px/57.2px 400 |
| Letter spacing | -2px |
| Colour | #18161a |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

cakeequity.com serves its Webflow CSS bundle from a cross-origin CDN, so the DOM-readable sheet list is thin — the per-state Transition rows above are computed values and cover the rules the page actually paints.

- home: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `0.2s`, `none`, `background-color 0.2s`, `color 0.2s`, `opacity 0.2s`, `0.4s ease-out`, `0.35s`, `0.5s`, `50ms`

- pricing: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `0.2s`, `none`, `background-color 0.2s`, `color 0.2s`, `opacity 0.2s`, `0.4s ease-out`, `0.35s`, `0.5s`, `50ms`
