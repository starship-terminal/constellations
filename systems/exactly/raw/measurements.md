# Component measurements

Computed styles read from exactly.ai on 2026-11-14 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### App shell and navigation

#### nav-header

Marketing header. The fixed top bar: exactly.ai wordmark, Industries/Showcase/Case studies/Pricing, Log in and the orange Start-for-free pill.

Page: home. Selector: `fixed header container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 68 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-1s2cdwf: Inter Variable 14px/20px 400, #ffffff |
| Transition | none |
| Icon | 24 x 24, colour #0000ee, fill #000000 |
| Painted layers | nav.framer-TqhsX.framer-gd57sn 1440.0x68.0 bg #ffffff @ 0; a.framer-VULEO.framer-BjxQL 122.0x36.0 bg #ffffff r 1000px |
| Ancestor paint | 1 up div.framer-vd1a8.framer-owqjC bg #ffffff |
| How | at rest |

Crops: `nav-header-default.png`.

#### nav-logo

Logo. The exactly.ai wordmark in the header; links home.

Page: home. Selector: `header logo link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 124 x 24 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Transition | none |
| Cursor | pointer |
| Icon | 24 x 24, colour #0000ee, fill #000000 |
| How | at rest |

Crops: `nav-logo-default.png`.

#### nav-link

Nav link. A header link (Industries/Showcase/Case studies/Pricing); measured, never followed.

Page: home. Selector: `header nav a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 94 x 36 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 1000px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1s2cdwf: Inter Variable 14px/20px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.6 | = | = |
| Painted layers | - | = | a.framer-Ozp9V.framer-BjxQL 94.0x36.0 r 1000px outline 1px auto #101010 offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Log in link. The Log-in link to threads.exactly.ai/signin; measured never followed.

Page: home. Selector: `header Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 67 x 36 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 1000px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1s2cdwf: Inter Variable 14px/20px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.6 | = | = |
| Painted layers | - | = | a.framer-Ozp9V.framer-BjxQL 67.0x36.0 r 1000px outline 1px auto #101010 offset 1px | = |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-cta

Start-for-free pill. The #fb411f orange Start-for-free pill; links to threads.exactly.ai/signin?action=create, measured never followed.

Page: home. Selector: `header Start for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 122 x 36 | 115.9 x 34.2 | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 1000px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1s2cdwf: Inter Variable 14px/20px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-VULEO.framer-BjxQL 122.0x36.0 bg #ffffff r 1000px | a.framer-VULEO.framer-BjxQL 115.9x34.2 bg #ffffff r 1000px | a.framer-VULEO.framer-BjxQL 122.0x36.0 bg #ffffff r 1000px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(0.95, 0, 0, 0.95, 0, 0) | = | = |
| Opacity | - | 0.8 | = | = |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### hero-h1

Hero headline. "AI automation for your brand's daily creative work." — the display headline over the photo hero.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1424 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 47px/60px 300 |
| Letter spacing | -1.88px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-sub

Hero sub. "Across design, illustration and photography." — the second span inside the hero h1.

Page: home. Selector: `h1 span`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 888.28 x 57 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 47px/60px 300 |
| Letter spacing | -1.88px |
| Colour | #ffffff @ 0.6 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-cta

Hero CTA. The white Start-for-free pill over the hero photo; measured never followed.

Page: home. Selector: `hero Start for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 148 x 56 | 147.39 x 55.77 | = | = |
| Padding | 18px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 1000px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1s2cdwf: Inter Variable 14px/20px 400, #1e1e1e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-McooI.framer-BjxQL 148.0x56.0 bg #ffffff r 1000px | a.framer-McooI.framer-BjxQL 147.4x55.8 bg #ffffff r 1000px | a.framer-McooI.framer-BjxQL 148.0x56.0 bg #ffffff r 1000px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(0.995888, 0, 0, 0.995888, 0, 0) | = | = |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-demo

Book-a-demo pill. The translucent Book-a-demo pill beside the hero CTA; links to /book-a-demo, measured never followed.

Page: home. Selector: `hero Book a demo`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 148 x 56 | 140.6 x 53.2 | = | = |
| Padding | 18px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 1000px | = | = | = |
| Background | #ffffff @ 0.1 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1s2cdwf: Inter Variable 14px/20px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-Q0rKC.framer-BjxQL 148.0x56.0 bg #ffffff @ 0.1 r 1000px | a.framer-Q0rKC.framer-BjxQL 140.6x53.2 bg #ffffff @ 0.1 r 1000px | a.framer-Q0rKC.framer-BjxQL 148.0x56.0 bg #ffffff @ 0.1 r 1000px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(0.95, 0, 0, 0.95, 0, 0) | = | = |
| Opacity | - | 0.8 | = | = |

Crops: `hero-demo-default.png`, `hero-demo-hover.png`, `hero-demo-focus-visible.png`, `hero-demo-pressed.png`.

#### trusted-strip

Trusted-by line. The "Trusted by the best creative teams and companies, globally" line over the logo wall (UNIQLO, Pentagram, Sony, Glossier, Nike).

Page: home. Selector: `trusted-by strip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `trusted-strip-default.png`.

#### section-h2

Section heading. A marketing section heading further down the home page.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1424 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 47px/60px 300 |
| Letter spacing | -1.88px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

### Footer

#### footer

Footer. The near-black footer: Follow/Company/Industries/Policies link columns, a watermark exactly.ai wordmark and the © line.

Page: home. Selector: `footer (Policies ancestor)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 952 |
| Padding | 328px 8px 160px 8px |
| Gap | 80px 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-95cemn: Inter Variable 21px/32px 400, #ffffff @ 0.6, ls -0.42px |
| Transition | none |
| Ancestor paint | 1 up div.framer-pgyam.framer-gxYHg bg #000000 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-col

Footer column label. A column heading in the footer ("Policies").

Page: home. Selector: `footer column label`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 69.64 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-95cemn: Inter Variable 21px/32px 400, #ffffff @ 0.6, ls -0.42px |
| Transition | none |
| How | at rest |

Crops: `footer-col-default.png`.

#### footer-link

Footer link. A legal link in the footer; measured, never followed.

Page: home. Selector: `footer legal a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 260.09 x 25 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter Variable 21px/32px 400 | = | = | = |
| Letter spacing | -0.42px | = | = | = |
| Colour | #ffffff | #ffffff @ 0.6 | = | #ffffff @ 0.6 |
| Transition | color 0.2s cubic-bezier(0.12, 0.23, 0.5, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-text.framer-styles-preset-lqmk1b 260.1x25.0 outline 1px auto #101010 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Pricing

#### pricing-h1

Pricing headline. "Bring AI into your creative work to automate routine tasks."

Page: pricing. Selector: `h1 on /pricing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 47px/60px 300 |
| Letter spacing | -1.88px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### plan-card

Plan card. A plan card (Pilot): name chip, price, feature list and its Start-for-free CTA.

Page: pricing. Selector: `plan card (price ancestor)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 389.33 x 745 |
| Padding | 0px |
| Gap | 40px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h5.framer-text.framer-styles-preset-1l47swl: Inter 21px/32px 400, #1e1e1e, ls -0.42px |
| Transition | none |
| Icon | 60 x 60, colour #000000 |
| Painted layers | a.framer-V0nb0.framer-BjxQL 140.0x56.0 bg #1e1e1e r 100px; div.framer-1vzejj9 6.0x6.0 bg #1e1e1e r 100%; div.framer-3m782w 6.0x6.0 bg #1e1e1e r 100%; div.framer-1xu1f0h 6.0x6.0 bg #1e1e1e r 100%; div.framer-qthi04 6.0x6.0 bg #1e1e1e r 100%; div.framer-1akdkbf 6.0x6.0 bg #1e1e1e r 100% |
| Ancestor paint | 1 up div.framer-yud3ge bg #f7f7f7 |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-name

Plan name. The plan-name label on a card.

Page: pricing. Selector: `plan name heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 389.33 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h5.framer-text.framer-styles-preset-1l47swl: Inter 21px/32px 400, #1e1e1e, ls -0.42px |
| Transition | none |
| How | at rest |

Crops: `plan-name-default.png`.

#### plan-price

Plan price. "£500 / mo," on the Pilot card.

Page: pricing. Selector: `plan price line`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 389.33 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | em.framer-text: Inter Variable 21px/32px 400, #404040 @ 0.6, ls -0.42px |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-feature

Plan feature row. A feature line inside a plan card.

Page: pricing. Selector: `plan feature p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 365.33 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `plan-feature-default.png`.

#### plan-cta

Plan CTA. A plan card's Start-for-free action; measured never followed.

Page: pricing. Selector: `plan Start for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140 x 56 | 133 x 53.2 | = | = |
| Padding | 18px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #1e1e1e | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1s2cdwf: Inter Variable 14px/20px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-V0nb0.framer-BjxQL 140.0x56.0 bg #1e1e1e r 100px | a.framer-V0nb0.framer-BjxQL 133.0x53.2 bg #1e1e1e r 100px | a.framer-V0nb0.framer-BjxQL 140.0x56.0 bg #1e1e1e r 100px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(0.95, 0, 0, 0.95, 0, 0) | = | = |
| Opacity | - | 0.9 | = | = |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-demo-cta

Plan Book-a-demo. The dark Book-a-demo action on the enterprise cards; measured never followed.

Page: pricing. Selector: `plan Book a demo`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140 x 56 | 133 x 53.2 | = | = |
| Padding | 18px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #1e1e1e | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1s2cdwf: Inter Variable 14px/20px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-V0nb0.framer-BjxQL 140.0x56.0 bg #1e1e1e r 100px | a.framer-V0nb0.framer-BjxQL 133.0x53.2 bg #1e1e1e r 100px | a.framer-V0nb0.framer-BjxQL 140.0x56.0 bg #1e1e1e r 100px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(0.95, 0, 0, 0.95, 0, 0) | = | = |
| Opacity | - | 0.9 | = | = |

Crops: `plan-demo-cta-default.png`, `plan-demo-cta-hover.png`, `plan-demo-cta-focus-visible.png`, `plan-demo-cta-pressed.png`.

#### compare-bar

Plan comparison bar. The sticky Solo/Team/Enterprise bar that pins over the comparison table on scroll.

Page: pricing. Selector: `sticky compare bar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1344 x 148 |
| Padding | 40px 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-1s2cdwf: Inter Variable 14px/20px 400, #1e1e1e |
| Transition | none |
| Painted layers | div.framer-1xxlbc7 1344.0x148.0 bg #ffffff; a.framer-VULEO.framer-BjxQL 122.0x36.0 bg #fb411f r 1000px; a.framer-VULEO.framer-BjxQL 123.0x36.0 bg #fb411f r 1000px; a.framer-VULEO.framer-BjxQL 123.0x36.0 bg #fb411f r 1000px |
| How | at rest |

Crops: `compare-bar-default.png`.

#### compare-h2

Compare heading. "Compare our plans in detail and find the right fit for your team".

Page: pricing. Selector: `compare h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1424 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 47px/60px 300 |
| Letter spacing | -1.88px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `compare-h2-default.png`.

#### faq-strip

FAQ strip. The "Still have questions? Take a look at our FAQ" closing block.

Page: pricing. Selector: `faq strip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1424 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.framer-text.framer-styles-preset-15bnuvr: Inter 47px/60px 300, #1e1e1e, ls -1.88px |
| Transition | none |
| Ancestor paint | 1 up div.framer-68g8lc bg #ffffff |
| How | at rest |

Crops: `faq-strip-default.png`.

### Showcase and case studies

#### showcase-h1

Showcase headline. "Any brand's visual style, mastered. We just get what works."

Page: showcase. Selector: `h1 on /showcase`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1424 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 47px/60px 300 |
| Letter spacing | -1.88px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `showcase-h1-default.png`.

#### showcase-chip

Category chip. A category tag on a brand card ("Tech"); the card links to /showcase/opal, measured never followed.

Page: showcase. Selector: `showcase category chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 35 x 20 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter Variable 14px/20px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `showcase-chip-default.png`, `showcase-chip-hover.png`, `showcase-chip-pressed.png`.

#### showcase-card

Brand card. A showcase brand card (cover image, category chip, brand name, tagline, Read more); measured, never followed.

Page: showcase. Selector: `a /showcase/<brand> card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 708 x 798.03 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1s2cdwf: Inter Variable 14px/20px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 23 x 23, colour #0000ee, fill #000000 | 11.5 x 11.5, colour #0000ee, fill #000000 | = | 23 x 23, colour #ff0000, fill #000000 |
| Painted layers | div.framer-cp81vd 708.0x690.0 bg #f7f7f7 r 40px; div::after.framer-cp81vd 708pxx690.031px border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 40px; div.framer-18vbn0f 4.0x4.0 bg #ffffff r 100px; div.framer-OHYgj.framer-VKc57 64.0x64.0 bg #ffffff @ 0.2 r 100px; div::after.framer-OHYgj.framer-VKc57 64pxx64px border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 100px | div.framer-cp81vd 708.0x690.0 bg #f7f7f7 r 40px; div::after.framer-cp81vd 708pxx690.031px border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 40px; div.framer-18vbn0f 4.0x4.0 bg #ffffff r 100px; div.framer-OHYgj.framer-VKc57 138.8x60.0 bg #ffffff @ 0.2 r 100px; div::after.framer-OHYgj.framer-VKc57 138.75pxx60px border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 100px | a.framer-owwqjv.framer-12v43ry 708.0x798.0 outline 1px auto #101010 offset 1px; div.framer-cp81vd 708.0x690.0 bg #f7f7f7 r 40px; div::after.framer-cp81vd 708pxx690.031px border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 40px; div.framer-18vbn0f 4.0x4.0 bg #ffffff r 100px; div.framer-OHYgj.framer-VKc57 64.0x64.0 bg #ffffff @ 0.2 r 100px; div::after.framer-OHYgj.framer-VKc57 64pxx64px border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 100px | = |
| Ancestor paint | 1 up div.framer-1xkq19g bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `showcase-card-default.png`, `showcase-card-hover.png`, `showcase-card-focus-visible.png`, `showcase-card-pressed.png`.

#### showcase-card-title

Brand name. The brand name heading on a showcase card.

Page: showcase. Selector: `card h4`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 43.48 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 21px/32px 400 |
| Letter spacing | -0.63px |
| Colour | #1e1e1e |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `showcase-card-title-default.png`.

#### read-more

Read-more link. The "Read more" caption link on a brand card; measured, never followed.

Page: showcase. Selector: `card Read more`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 37.38 x 10 | 41.16 x 11.01 | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 14px/20px 600 | = | - | = |
| Letter spacing | -0.14px | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `read-more-default.png`, `read-more-hover.png`, `read-more-pressed.png`.

#### brand-h1

Brand headline. The brand page headline ("Revolut — Change the way you money").

Page: showcase-brand. Selector: `h1 on /showcase/revolut`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1424 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 47px/60px 300 |
| Letter spacing | -1.88px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `brand-h1-default.png`.

#### brand-chip

Brand category. The category label on the brand page.

Page: showcase-brand. Selector: `brand category`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 363.17 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 47px/60px 300 |
| Letter spacing | -1.88px |
| Colour | #1e1e1e |
| Text node | a.framer-text.framer-styles-preset-lqmk1b: Inter 47px/60px 300, #ffffff, ls -1.88px |
| Transition | none |
| How | at rest |

Crops: `brand-chip-default.png`.

#### brand-body

Brand intro. The brand description paragraph.

Page: showcase-brand. Selector: `brand intro p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 588 x 224 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 22px/32px 400 |
| Letter spacing | -0.22px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `brand-body-default.png`.

#### cases-h1

Case-studies headline. The case-studies index headline.

Page: case-studies. Selector: `h1 on /case-studies`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1424 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 47px/60px 300 |
| Letter spacing | -1.88px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `cases-h1-default.png`.

#### case-card

Case-study row. A case-study row on the index: brand name, tagline, description, Read-study pill and image.

Page: case-studies. Selector: `case row (brand + Read study ancestor)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 767 x 240 |
| Padding | 0px |
| Gap | 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h4.framer-text.framer-styles-preset-18s8tru: Inter Variable 21px/32px 400, #1e1e1e, ls -0.63px |
| Transition | none |
| Painted layers | a.framer-RjskD.framer-BjxQL 140.0x56.0 bg #7c7c7c @ 0.08 r 1000px |
| How | at rest |

Crops: `case-card-default.png`.

#### article-h1

Article headline. The case-study article headline.

Page: case-study. Selector: `article h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1152 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 47px/60px 300 |
| Letter spacing | -1.88px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `article-h1-default.png`.

#### article-body

Article body. A body paragraph in the article prose.

Page: case-study. Selector: `article p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 730.67 x 128 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 22px/32px 400 |
| Letter spacing | -0.22px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `article-body-default.png`.

#### article-quote

Article quote. A pull quote or stat line inside the article, where the page carries one.

Page: case-study. Selector: `article blockquote/p`. States: .

Not found on the page at capture time.

#### case-read

Read-study pill. The "Read study" pill on a case-study row — the outer anchor that paints the grey fill, not the text box inside it; measured, never followed.

Page: case-studies. Selector: `Read study pill (outer a)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140 x 56 | 133 x 53.2 | = | = |
| Padding | 18px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 1000px | = | = | = |
| Background | #7c7c7c @ 0.08 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1s2cdwf: Inter Variable 14px/20px 400, #1e1e1e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-RjskD.framer-BjxQL 140.0x56.0 bg #7c7c7c @ 0.08 r 1000px | a.framer-RjskD.framer-BjxQL 133.0x53.2 bg #7c7c7c @ 0.08 r 1000px | a.framer-RjskD.framer-BjxQL 140.0x56.0 bg #7c7c7c @ 0.08 r 1000px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(0.95, 0, 0, 0.95, 0, 0) | = | = |
| Opacity | - | 0.8 | = | = |

Crops: `case-read-default.png`, `case-read-hover.png`, `case-read-focus-visible.png`, `case-read-pressed.png`.

#### article-h2

Article heading. A section heading inside the article.

Page: case-study. Selector: `article h2/h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 730.67 x 88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 32px/44px 400 |
| Letter spacing | -0.32px |
| Colour | #1e1e1e |
| Text node | a: Inter Variable 32px/44px 400, #1e1e1e, ls -0.32px |
| Transition | none |
| How | at rest |

Crops: `article-h2-default.png`.

### Industries

#### industries-h1

Industries headline. The industries index headline.

Page: industries. Selector: `h1 on /industries`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1424 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 47px/60px 300 |
| Letter spacing | -1.88px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `industries-h1-default.png`.

#### industry-card

Industry card. An industry card on the index; measured, never followed.

Page: industries. Selector: `industry card a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 708 x 892 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-2vnz17: Inter 14px/20px 600, #ffffff, ls -0.14px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #0000ee, fill #000000 | 11.5 x 11.5, colour #0000ee, fill #000000 | = | 20 x 20, colour #ff0000, fill #000000 |
| Painted layers | div.framer-ij66mj 708.0x708.0 bg #f7f7f7 r 32px; div::after.framer-ij66mj 708pxx708px border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 32px; div.framer-OHYgj.framer-VKc57 52.0x52.0 bg #ffffff @ 0.2 r 100px; div::after.framer-OHYgj.framer-VKc57 52pxx52px border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 100px | div.framer-ij66mj 708.0x708.0 bg #f7f7f7 r 32px; div::after.framer-ij66mj 708pxx708px border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 32px; div.framer-OHYgj.framer-VKc57 138.8x60.0 bg #ffffff @ 0.2 r 100px; div::after.framer-OHYgj.framer-VKc57 138.75pxx60px border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 100px | a.framer-bP7zE.framer-WHDvl 708.0x892.0 outline 1px auto #101010 offset 1px; div.framer-ij66mj 708.0x708.0 bg #f7f7f7 r 32px; div::after.framer-ij66mj 708pxx708px border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 32px; div.framer-OHYgj.framer-VKc57 52.0x52.0 bg #ffffff @ 0.2 r 100px; div::after.framer-OHYgj.framer-VKc57 52pxx52px border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 100px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `industry-card-default.png`, `industry-card-hover.png`, `industry-card-focus-visible.png`, `industry-card-pressed.png`.

#### industry-h1

Industry headline. The industry page headline.

Page: industry. Selector: `h1 on /industries/saas-n-mobile-apps`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1408 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 47px/60px 300 |
| Letter spacing | -1.88px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `industry-h1-default.png`.

#### industry-body

Industry body. A body paragraph on the industry page.

Page: industry. Selector: `industry p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 14px/20px 400 |
| Letter spacing | -0.14px |
| Colour | #404040 @ 0.48 |
| Transition | none |
| How | at rest |

Crops: `industry-body-default.png`.

### Help center

#### help-sidebar

Help sidebar. The left doc rail: Getting started, AI style transfer, Library and more groups of article links.

Page: help-center. Selector: `help sidebar rail`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 240 x 1560 |
| Padding | 240px 24px 24px 24px |
| Gap | 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-1s2cdwf: Inter Variable 14px/20px 400, #1e1e1e |
| Transition | none |
| Ancestor paint | 1 up div.framer-pz1x15 bg #ffffff |
| How | at rest |

Crops: none.

#### help-nav-group

Nav group label. A sidebar group label ("Getting started").

Page: help-center. Selector: `sidebar group label`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 106 x 28 |
| Padding | 0px |
| Gap | 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-1s2cdwf: Inter Variable 14px/20px 400, #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `help-nav-group-default.png`.

#### help-nav-link

Sidebar link. A sidebar article link; measured, never followed.

Page: help-center. Selector: `sidebar a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 86 x 32 | = | = | = |
| Padding | 6px 0px 6px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 1000px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1ugvs47: Inter 14px/20px 400, #1e1e1e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-t2H42.framer-siwSQ 86.0x32.0 r 1000px outline 1px auto #101010 offset 1px | = |

Crops: `help-nav-link-default.png`, `help-nav-link-hover.png`, `help-nav-link-focus-visible.png`, `help-nav-link-pressed.png`.

#### help-h1

Help headline. "Help center".

Page: help-center. Selector: `h1 on /help-center`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 47px/60px 300 |
| Letter spacing | -1.88px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `help-h1-default.png`.

#### help-search

Search trigger. The "Search…" affordance on the help landing: a rounded field that opens the Framer search modal when its overlay button is clicked (a local UI toggle).

Page: help-center. Selector: `help "Search…" field container`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 640 x 52 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | sans-serif 12px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | p.framer-text.framer-styles-preset-1ugvs47: Inter 14px/20px 400, #404040 @ 0.48 | = | - | = |
| Transition | none | = | - | = |
| Painted layers | div.framer-6tgDK.framer-siwSQ 640.0x52.0 bg #7c7c7c @ 0.08 r 32px; div.framer-i4x7f7 15.0x15.0 image url(data:…)%22></path></svg>") | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `help-search-default.png`, `help-search-hover.png`, `help-search-pressed.png`.

#### help-search-input

Search field. The real input inside the Framer search modal; focused and typed into then cleared — never submitted.

Page: help-center. Selector: `search modal input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 348 x 32 | = | 316 x 32 |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 16px/32px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1e1e1e | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000 @ 0.4, opacity 1 | = | = |
| Ancestor paint | 2 up div bg #ffffff shadow #000000 @ 0.15 0px 20px 40px 0px | = | = |
| How | at rest | clicked into the field | typed "train a style", then deleted; nothing sent |

Crops: `help-search-input-default.png`, `help-search-input-focused.png`, `help-search-input-filled.png`.

#### help-card

Article-collection card. A collection card ("FAQ — Get quick answers — 12 articles"); measured, never followed.

Page: help-center. Selector: `help collection card a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 640 x 296 | = | = | = |
| Padding | 40px | = | = | = |
| Gap | 80px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | #7c7c7c @ 0.08 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | h5.framer-text.framer-styles-preset-1l47swl: Inter 21px/32px 400, #1e1e1e, ls -0.42px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-rrzppi.framer-jtqjef 640.0x296.0 bg #7c7c7c @ 0.08 r 40px | = | a.framer-rrzppi.framer-jtqjef 640.0x296.0 bg #7c7c7c @ 0.08 r 40px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `help-card-default.png`, `help-card-hover.png`, `help-card-focus-visible.png`, `help-card-pressed.png`.

#### faq-h1

FAQ headline. "Frequently asked questions" — the FAQ article page.

Page: help-faq. Selector: `h1 on /help-center/frequently-asked-questions`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 47px/60px 300 |
| Letter spacing | -1.88px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `faq-h1-default.png`.

#### faq-question

FAQ question. An anchor-linked question heading inside the FAQ article (H3).

Page: help-faq. Selector: `faq h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 22px/32px 400 |
| Letter spacing | -0.22px |
| Colour | #1e1e1e |
| Text node | a: Inter Variable 22px/32px 400, #1e1e1e, ls -0.22px |
| Transition | none |
| How | at rest |

Crops: `faq-question-default.png`.

#### faq-answer

FAQ answer. The answer paragraph under a question heading.

Page: help-faq. Selector: `faq answer p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 22px/32px 400 |
| Letter spacing | -0.22px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `faq-answer-default.png`.

#### article-link

Inline link. The "Data protection & privacy" link inside the FAQ article prose (the #help-center-rich-text body); measured, never followed.

Page: help-faq. Selector: `#help-center-rich-text a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 292.41 x 26 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter Variable 22px/32px 400 | = | = | = |
| Letter spacing | -0.22px | = | = | = |
| Colour | #1e1e1e | = | = | = |
| Transition | opacity 0.2s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.7 | = | = |
| Painted layers | - | = | a 292.4x26.0 outline 1px auto #101010 offset 1px | = |

Crops: `article-link-default.png`, `article-link-hover.png`, `article-link-focus-visible.png`, `article-link-pressed.png`.

### Book a demo

#### demo-h1

Demo headline. "See how exactly.ai works. Let us help you scale your creative processes."

Page: book-a-demo. Selector: `demo headline`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 180 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 47px/60px 300 |
| Letter spacing | -1.88px |
| Colour | #404040 @ 0.36 |
| Text node | span.framer-text: Inter 47px/60px 300, #1e1e1e, ls -1.88px |
| Transition | none |
| How | at rest |

Crops: `demo-h1-default.png`.

#### demo-scheduler

Scheduler embed. The embedded scheduling widget (a Calendly-style day picker in a srcdoc iframe): measured as a region at rest — no day, time or contact detail was ever picked or typed.

Page: book-a-demo. Selector: `scheduler iframe`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 600 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: none.

### Mobile (390 wide)

#### m-topbar

Mobile top bar. The phone top bar: exactly.ai wordmark, Join pill, hamburger.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-1s2cdwf: Inter Variable 14px/20px 400, #1e1e1e |
| Transition | none |
| Icon | 86 x 24, colour #0000ee, fill #000000 |
| Painted layers | nav.framer-TqhsX.framer-gd57sn 390.0x56.0 bg #ffffff @ 0; div.framer-194xxwj 28.0x2.0 bg #ffffff; div.framer-1713bdv 28.0x2.0 bg #ffffff; a.framer-VULEO.framer-BjxQL 55.0x32.0 bg #ffffff r 1000px |
| Ancestor paint | 1 up div.framer-vd1a8.framer-owqjC bg #ffffff |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-join

Join pill. The white Join pill in the phone top bar; measured never followed.

Page: mobile. Selector: `mobile Join`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 55 x 32 | 52.25 x 30.4 | = | = |
| Padding | 6px 12px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 1000px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1s2cdwf: Inter Variable 14px/20px 400, #1e1e1e | = | = | = |
| Transition | none | = | = | = |
| Painted layers | a.framer-VULEO.framer-BjxQL 55.0x32.0 bg #ffffff r 1000px | a.framer-VULEO.framer-BjxQL 52.3x30.4 bg #ffffff r 1000px | a.framer-VULEO.framer-BjxQL 55.0x32.0 bg #ffffff r 1000px outline 1px auto #e59700 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(0.95, 0, 0, 0.95, 0, 0) | = | = |

Crops: `m-join-default.png`, `m-join-hover.png`, `m-join-focus-visible.png`, `m-join-pressed.png`.

#### m-hamburger

Mobile hamburger. The burger that opens the phone nav overlay — a local UI toggle; the opened state was measured after tapping it.

Page: mobile. Selector: `Mobile menu toggle`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = | = |
| Font | sans-serif 12px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | div.framer-194xxwj 28.0x2.0 bg #ffffff; div.framer-1713bdv 28.0x2.0 bg #ffffff | = | div.framer-1dourkh 32.0x32.0 outline 1px auto #e59700 offset 0px; div.framer-194xxwj 28.0x2.0 bg #ffffff; div.framer-1713bdv 28.0x2.0 bg #ffffff | = | div.framer-194xxwj 18.4x18.4 bg #1e1e1e; div.framer-1713bdv 18.4x18.4 bg #1e1e1e |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `m-hamburger-default.png`, `m-hamburger-hover.png`, `m-hamburger-focus-visible.png`, `m-hamburger-pressed.png`, `m-hamburger-opened.png`.

#### m-drawer-link

Drawer link. A nav link inside the opened overlay; measured, never followed.

Page: mobile. Selector: `drawer a`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 32 |
| Padding | 4px 16px |
| Gap | 10px |
| Border | none |
| Radius | 1000px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Text node | h5.framer-text.framer-styles-preset-1l47swl: Inter 17px/24px 400, #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `m-drawer-link-default.png`.

#### m-hero-h1

Mobile hero headline. The hero display at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 374 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 27px/36px 300 |
| Letter spacing | -0.81px |
| Colour | #1e1e1e |
| Text node | span.framer-text: Inter 27px/36px 300, #ffffff, ls -0.81px |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-hero-cta

Mobile hero CTA. The white Start-for-free pill over the phone hero; measured never followed.

Page: mobile. Selector: `mobile Start for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 132 x 56 | = | = | = |
| Padding | 18px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 1000px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1s2cdwf: Inter Variable 14px/20px 400, #1e1e1e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-McooI.framer-BjxQL 132.0x56.0 bg #ffffff r 1000px | = | a.framer-McooI.framer-BjxQL 132.0x56.0 bg #ffffff r 1000px outline 1px auto #e59700 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-hero-cta-default.png`, `m-hero-cta-hover.png`, `m-hero-cta-focus-visible.png`, `m-hero-cta-pressed.png`.

#### m-hero-demo

Mobile demo pill. The translucent Book-a-demo pill on the phone hero; measured never followed.

Page: mobile. Selector: `mobile Book a demo`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 132 x 56 | = | = | = |
| Padding | 18px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 1000px | = | = | = |
| Background | #ffffff @ 0.1 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1s2cdwf: Inter Variable 14px/20px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-Q0rKC.framer-BjxQL 132.0x56.0 bg #ffffff @ 0.1 r 1000px | = | a.framer-Q0rKC.framer-BjxQL 132.0x56.0 bg #ffffff @ 0.1 r 1000px outline 1px auto #e59700 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-hero-demo-default.png`, `m-hero-demo-hover.png`, `m-hero-demo-focus-visible.png`, `m-hero-demo-pressed.png`.

## Transitions declared in the readable stylesheets

exactly.ai's own CSS is served in inline <style> blocks, so this list holds every rule declaring transition or animation that the CSSOM could read on each page; the per-state Transition rows above are the computed values.

- case-studies: `color 0.2s cubic-bezier(0.12, 0.23, 0.5, 1)`, `opacity 0.4s ease-out`, `unset`, `color var(--sp-transitions-default), background var(--sp-transitions-default)`, `max-width 0.3s ease-out`, `opacity 0.2s, visibility 0.2s`, `margin 0.3s ease-out`, `padding 0.3s ease-out`, `opacity 0.3s`, `none`, `opacity 0.3s, visibility linear 0.35s`, `opacity 0.25s ease-in`

- case-study: `color 0.2s cubic-bezier(0.12, 0.23, 0.5, 1)`, `opacity 0.4s ease-out`, `unset`, `color var(--sp-transitions-default), background var(--sp-transitions-default)`, `max-width 0.3s ease-out`, `opacity 0.2s, visibility 0.2s`, `margin 0.3s ease-out`, `padding 0.3s ease-out`, `opacity 0.3s`, `none`, `opacity 0.3s, visibility linear 0.35s`, `opacity 0.25s ease-in`

- help-center: `color 0.2s cubic-bezier(0.12, 0.23, 0.5, 1)`, `opacity 0.4s ease-out`, `unset`, `color var(--sp-transitions-default), background var(--sp-transitions-default)`

- help-faq: `color 0.2s cubic-bezier(0.44, 0, 0.56, 1)`, `color 0.2s cubic-bezier(0.12, 0.23, 0.5, 1)`, `opacity 0.4s ease-out`, `unset`, `color var(--sp-transitions-default), background var(--sp-transitions-default)`

- home: `color 0.2s cubic-bezier(0.12, 0.23, 0.5, 1)`, `opacity 0.4s ease-out`, `unset`, `color var(--sp-transitions-default), background var(--sp-transitions-default)`, `max-width 0.3s ease-out`, `opacity 0.2s, visibility 0.2s`, `margin 0.3s ease-out`, `padding 0.3s ease-out`, `opacity 0.3s`, `none`, `opacity 0.3s, visibility linear 0.35s`, `opacity 0.25s ease-in`

- industries: `color 0.2s cubic-bezier(0.12, 0.23, 0.5, 1)`, `opacity 0.4s ease-out`, `unset`, `color var(--sp-transitions-default), background var(--sp-transitions-default)`, `max-width 0.3s ease-out`, `opacity 0.2s, visibility 0.2s`, `margin 0.3s ease-out`, `padding 0.3s ease-out`, `opacity 0.3s`, `none`, `opacity 0.3s, visibility linear 0.35s`, `opacity 0.25s ease-in`

- industry: `color 0.15s`, `color 0.2s cubic-bezier(0.12, 0.23, 0.5, 1)`, `opacity 0.4s ease-out`, `unset`, `color var(--sp-transitions-default), background var(--sp-transitions-default)`, `max-width 0.3s ease-out`, `opacity 0.2s, visibility 0.2s`, `margin 0.3s ease-out`, `padding 0.3s ease-out`, `opacity 0.3s`, `none`, `opacity 0.3s, visibility linear 0.35s`

- pricing: `color 0.2s cubic-bezier(0.12, 0.23, 0.5, 1)`, `opacity 0.4s ease-out`, `unset`, `color var(--sp-transitions-default), background var(--sp-transitions-default)`, `initial`, `max-width 0.3s ease-out`, `opacity 0.2s, visibility 0.2s`, `margin 0.3s ease-out`, `padding 0.3s ease-out`, `opacity 0.3s`, `none`, `opacity 0.3s, visibility linear 0.35s`

- showcase: `color 0.2s cubic-bezier(0.12, 0.23, 0.5, 1)`, `opacity 0.4s ease-out`, `unset`, `color var(--sp-transitions-default), background var(--sp-transitions-default)`, `max-width 0.3s ease-out`, `opacity 0.2s, visibility 0.2s`, `margin 0.3s ease-out`, `padding 0.3s ease-out`, `opacity 0.3s`, `none`, `opacity 0.3s, visibility linear 0.35s`, `opacity 0.25s ease-in`

- showcase-brand: `color 0.15s cubic-bezier(0.44, 0, 0.56, 1), text-decoration-color 0.15s cubic-bezier(0.44, 0, 0.56, 1), text-decoration-thickness 0.15s cubic-bezier(0.44, 0, 0.56, 1), text-underline-offset 0.15s cubic-bezier(0.44, 0, 0.56, 1)`, `color 0.2s cubic-bezier(0.12, 0.23, 0.5, 1)`, `opacity 0.4s ease-out`, `unset`, `color var(--sp-transitions-default), background var(--sp-transitions-default)`, `max-width 0.3s ease-out`, `opacity 0.2s, visibility 0.2s`, `margin 0.3s ease-out`, `padding 0.3s ease-out`, `opacity 0.3s`, `none`, `opacity 0.3s, visibility linear 0.35s`
