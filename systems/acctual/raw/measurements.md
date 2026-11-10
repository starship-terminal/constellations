# Component measurements

Computed styles read from acctual.com on 2026-11-10 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### nav-bar

Top navigation bar. The top bar: wordmark, Freelancer / Agency / Pricing / Blog links, Log in and the Sign-up pill.

Page: home. Selector: `nav topbar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 80 |
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
| Text node | p.framer-text: Inter 14px/24px 500, #0098f2, ls -0.28px |
| Transition | none |
| Icon | 14 x 14, colour #0000ee, fill #000000 |
| Painted layers | div.framer-1ve1fz9 1034.0x80.0 bg #f5f5f5 @ 0.6 r 0px 0px 20px 20px shadow #000000 @ 0.1 0px 1px 2px 0px; div.framer-1i2m7ev 112.0x16.0 image url(data:…)%22></path><path d=%22M 17.846 0.4 C 17.846 0.179 17.667 0 17.446 0 L 14.554 0 ; a.framer-Ygbcr.framer-z7gpue 148.6x40.0 bg #0d111b r 100px shadow #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px; a::after.framer-Ygbcr.framer-z7gpue 148.562pxx40px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 100px |
| How | at rest |

Crops: `nav-bar-default.png`.

#### nav-logo

Logo. The Acctual wordmark linking home.

Page: home. Selector: `nav logo a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1034 x 32 | = | = | = |
| Padding | 4px 14px 4px 20px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(10px) | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Inter 14px/24px 500, #0098f2, ls -0.28px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #0000ee, fill #000000 | = | = | 14 x 14, colour #ff0000, fill #000000 |
| Ancestor paint | 2 up div.framer-1ve1fz9 bg #f5f5f5 @ 0.6 shadow #000000 @ 0.1 0px 1px 2px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-r1UWv.framer-w2wy95 1034.0x32.0 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-logo-default.png`, `nav-logo-hover.png`, `nav-logo-focus-visible.png`, `nav-logo-pressed.png`.

#### nav-link

Nav link. A section link in the top bar.

Page: home. Selector: `nav a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 74.63 x 35.36 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Open Runde 16px/19.36px 500, #1e1e1e @ 0.7, ls -0.32px | p.framer-text: Open Runde 16px/19.36px 500, #000000, ls -0.32px | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-GZ0tw.framer-ymsmdp 74.6x35.4 r 100px outline 1px auto #005fcc offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-cta

Nav CTA. The "Sign up for free" pill. Hovered and focused only; app.acctual.com is never opened.

Page: home. Selector: `nav cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 148.56 x 40 | = | = | = |
| Padding | 6px 14px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #0d111b | #000000 @ 0.88 | = | = |
| Box shadow | #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Open Runde 16px/24px 500, #ffffff, ls -0.32px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 148.562px x 40px, absolute, bg #000000 @ 0, radius 100px | = | = | = |
| Painted layers | a.framer-Ygbcr.framer-z7gpue 148.6x40.0 bg #0d111b r 100px shadow #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px; a::after.framer-Ygbcr.framer-z7gpue 148.562pxx40px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 100px | a.framer-Ygbcr.framer-z7gpue 148.6x40.0 bg #000000 @ 0.88 r 100px shadow #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px; a::after.framer-Ygbcr.framer-z7gpue 148.562pxx40px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 100px | a.framer-Ygbcr.framer-z7gpue 148.6x40.0 bg #0d111b r 100px shadow #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px outline 1px auto #005fcc offset 1px; a::after.framer-Ygbcr.framer-z7gpue 148.562pxx40px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 100px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-login

Log-in link. The plain Log-in link beside the CTA. app.acctual.com is never opened.

Page: home. Selector: `nav login`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 80.41 x 40 | = | = | = |
| Padding | 6px 14px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Open Runde 16px/24px 500, #1e1e1e @ 0.6, ls -0.32px | p.framer-text: Open Runde 16px/24px 500, #1e1e1e, ls -0.32px | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 80.4062px x 40px, absolute, bg #000000 @ 0, radius 100px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-Ygbcr.framer-z7gpue 80.4x40.0 r 100px outline 1px auto #005fcc offset 1px | = |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### announcement

Announcement banner. The "Acctual is joining Altitude" strip above the nav, linking to /altitude.

Page: home. Selector: `announcement a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1034 x 32 | = | = | = |
| Padding | 4px 14px 4px 20px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(10px) | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Inter 14px/24px 500, #0098f2, ls -0.28px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #0000ee, fill #000000 | = | = | 14 x 14, colour #ff0000, fill #000000 |
| Ancestor paint | 2 up div.framer-1ve1fz9 bg #f5f5f5 @ 0.6 shadow #000000 @ 0.1 0px 1px 2px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-r1UWv.framer-w2wy95 1034.0x32.0 outline 1px auto #005fcc offset 1px | = |

Crops: `announcement-default.png`, `announcement-hover.png`, `announcement-focus-visible.png`, `announcement-pressed.png`.

#### footer

Footer. The footer band: the "Create the world’s most flexible invoice" heading, link columns and the "from NYC" credit.

Page: home. Selector: `footer band`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 404 |
| Padding | 0px |
| Gap | 48px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h6.framer-text.framer-styles-preset-nnsl7o: Open Runde 20px/28px 600, #1e1e1e, ls -0.6px |
| Transition | none |
| Icon | 112 x 40, colour #1e1e1e |
| Painted layers | a.framer-Ygbcr.framer-z7gpue 163.1x40.0 bg #0d111b r 100px shadow #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px; a::after.framer-Ygbcr.framer-z7gpue 163.141pxx40px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 100px |
| Ancestor paint | 1 up div.framer-tzdOn.framer-IfODq bg #fafafa |
| How | at rest |

Crops: `footer-default.png`.

#### footer-heading

Footer heading. The sign-off heading in the footer.

Page: home. Selector: `footer heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 256 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h6.framer-text.framer-styles-preset-nnsl7o: Open Runde 20px/28px 600, #1e1e1e, ls -0.6px |
| Transition | none |
| How | at rest |

Crops: `footer-heading-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40.08 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Open Runde 14px/20px 500 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #8d8d8d | #000000 @ 0.9 | = | #000000 @ 0.9 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-text.framer-styles-preset-ego3sz 40.1x17.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Home

#### hero-title

Hero title. "Small business invoices: Get paid on time" — the display headline.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Runde 64px/72px 600 |
| Letter spacing | -1.92px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### invoice-demo

Invoice demo. The interactive invoice mock in the hero (a marketing demo, not a live product): payment-method dropdown, amount and currency fields.

Page: home. Selector: `invoice demo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 514.92 x 294.11 |
| Padding | 28px 28px 24px 28px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text: Open Runde 12px/16px 500, #8b8b8b |
| Transition | none |
| ::after | 498px x 260px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | div::after.framer-1pnm5qc 498pxx260px border B:1px solid #eeeeee; div.framer-3XVj1.framer-8biYL 146.4x77.7 bg #ffffff r 16px shadow #0a0d14 @ 0.03 0px 1px 2px 0px; div::after.framer-3XVj1.framer-8biYL 142pxx68px border T:1px solid #d8d8d8 / R:1px solid #d8d8d8 / B:1px solid #d8d8d8 / L:1px solid #d8d8d8 r 16px; div.framer-uc2g44 16.0x16.0 image url(data:…)%22></path></svg>"); div.framer-3XVj1.framer-8biYL 146.4x77.7 bg #ffffff r 16px shadow #0a0d14 @ 0.03 0px 1px 2px 0px; div::after.framer-3XVj1.framer-8biYL 142pxx68px border T:1px solid #d8d8d8 / R:1px solid #d8d8d8 / B:1px solid #d8d8d8 / L:1px solid #d8d8d8 r 16px |
| Ancestor paint | 1 up div.framer-1x21adt bg #ffffff shadow #000000 @ 0.05 0px 1.77778px 8px 0px, #000000 @ 0.04 0px 0.888889px 2.66667px 0px |
| How | at rest |

Crops: `invoice-demo-default.png`.

#### section-title

Section title. A section heading ("We designed an invoice that works harder for your business").

Page: home. Selector: `h1 (section)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Runde 40px/48px 600 |
| Letter spacing | -1.2px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### fee-item

Fee item. A fee-comparison row (1% bank transfer / 2.7% card / 1% stablecoin).

Page: home. Selector: `fee item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 82.89 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-qigbz2: Open Runde 16px/24px 500, #0098f2, ls -0.32px |
| Transition | none |
| How | at rest |

Crops: `fee-item-default.png`.

#### persona-card

Persona card. A who-it-is-for card (Contractors).

Page: home. Selector: `persona card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 325.33 x 166 | = |
| Padding | 24px | = |
| Gap | 18px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | #fafafa | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #0000ee | = |
| Text node | h6.framer-text.framer-styles-preset-nnsl7o: Open Runde 20px/28px 600, #1e1e1e, ls -0.6px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 18 x 20, colour #0000ee, fill #000000 | = |
| Painted layers | a.framer-32269w.framer-e2xr0 325.3x166.0 bg #fafafa r 16px | = |
| How | at rest | mouse hover |

Crops: `persona-card-default.png`, `persona-card-hover.png`.

#### security-item

Security item. A trust row (PCI standards / SSL encryption & tokenization).

Page: home. Selector: `security item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 500 x 84 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h6.framer-text.framer-styles-preset-nnsl7o: Open Runde 20px/28px 600, #1e1e1e, ls -0.6px |
| Transition | none |
| How | at rest |

Crops: `security-item-default.png`.

#### faq-item

FAQ item. An accordion question in the FAQs section; toggled open once (a local disclosure).

Page: home. Selector: `faq Closed row`. States: default, open.

| Property | default | open |
|---|---|---|
| Size (w x h) | 1024 x 25 | 1024 x 120 |
| Padding | 0px | = |
| Gap | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | p.framer-text.framer-styles-preset-qigbz2: Open Runde 16px/24px 500, #1e1e1e, ls -0.32px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.framer-1g1x0c 18.0x5.0 image url(data:…)%22></path></svg>"); div.framer-1rzj1sx 5.0x18.0 image url(data:…)%22></path></svg>") | div.framer-1g1x0c 18.0x5.0 image url(data:…)%22></path></svg>"); div.framer-1rzj1sx 18.1x5.3 image url(data:…)%22></path></svg>") |
| How | at rest | question pressed once (a local accordion disclosure) |

Crops: `faq-item-default.png`, `faq-item-open.png`.

### Pricing

#### pricing-title

Page title.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Runde 48px/56px 600 |
| Letter spacing | -1.44px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: none.

#### fee-row

Fee comparison row. A comparison row on the pricing page (payment method, currencies, payout).

Page: pricing. Selector: `fee row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 64 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | #f0f0f0 @ 0.95 |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-nd7hob: Open Runde 14px/20px 500, #1e1e1e, ls -0.28px |
| Transition | none |
| Painted layers | div.framer-berwxq 1024.0x64.0 bg #f0f0f0 @ 0.95; div.framer-kqhyap 188.0x64.0 bg #ffffff; div::after.framer-kqhyap 188pxx64px border B:1px solid #dbdbdb; div.framer-ufd0up 180.0x64.0 bg #ffffff; div::after.framer-ufd0up 180pxx64px border B:1px solid #dbdbdb; div.framer-4oiowl 164.0x64.0 bg #ffffff |
| Ancestor paint | 1 up div.framer-zu2ost bg #ffffff |
| How | at rest |

Crops: none.

#### plan-cta

Page CTA.

Page: pricing. Selector: `page cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 148.56 x 40 | = | = | = |
| Padding | 6px 14px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #0d111b | = | = | = |
| Box shadow | #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Open Runde 16px/24px 500, #ffffff, ls -0.32px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 148.562px x 40px, absolute, bg #000000 @ 0, radius 100px | = | = | = |
| Painted layers | a.framer-Ygbcr.framer-z7gpue 148.6x40.0 bg #0d111b r 100px shadow #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px; a::after.framer-Ygbcr.framer-z7gpue 148.562pxx40px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 100px | = | a.framer-Ygbcr.framer-z7gpue 148.6x40.0 bg #0d111b r 100px shadow #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px outline 1px auto #005fcc offset 1px; a::after.framer-Ygbcr.framer-z7gpue 148.562pxx40px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 100px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

### Company and content pages

#### teams-title

Page title.

Page: teams. Selector: `h1,h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Runde 48px/56px 600 |
| Letter spacing | -1.44px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `teams-title-default.png`.

#### teams-body

Body text.

Page: teams. Selector: `body p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Runde 16px/24px 500 |
| Letter spacing | -0.32px |
| Colour | #8d8d8d |
| Transition | none |
| How | at rest |

Crops: `teams-body-default.png`.

#### about-title

Page title.

Page: about. Selector: `h1,h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Runde 48px/56px 600 |
| Letter spacing | -1.44px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `about-title-default.png`.

#### about-body

Body text.

Page: about. Selector: `body p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Runde 16px/24px 500 |
| Letter spacing | -0.32px |
| Colour | #1e1e1e |
| Text node | span.framer-text: Open Runde 16px/24px 500, #8d8d8d, ls -0.32px |
| Transition | none |
| How | at rest |

Crops: `about-body-default.png`.

#### blog-title

Page title.

Page: blog. Selector: `h1,h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 130.02 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Runde 64px/72px 600 |
| Letter spacing | -1.92px |
| Colour | #1e1e1e |
| Transition | none |
| Ancestor paint | 3 up main.framer-egi90z bg #f7fafc shadow #000000 @ 0.25 0px 2px 8px 0px |
| How | at rest |

Crops: `blog-title-default.png`.

#### blog-body

Body text.

Page: blog. Selector: `body p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 388 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Runde 16px/24px 500 |
| Letter spacing | -0.32px |
| Colour | #8d8d8d |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `blog-body-default.png`.

#### blog-item

Blog item. A post row or card on the blog index.

Page: blog. Selector: `blog item`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1032 x 90.84 | = |
| Padding | 0px | = |
| Gap | 48px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #0000ee | = |
| Text node | h6.framer-text.framer-styles-preset-nnsl7o: Open Runde 20px/28px 600, #1e1e1e, ls -0.6px | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `blog-item-default.png`, `blog-item-hover.png`.

#### blog-post-title

Page title.

Page: blog-post. Selector: `h1,h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Runde 30px/42px 600 |
| Letter spacing | -1.2px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `blog-post-title-default.png`.

#### blog-post-body

Body text.

Page: blog-post. Selector: `body p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 25.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Runde 16px/25.6px 400 |
| Letter spacing | -0.32px |
| Colour | #666666 |
| Text node | em.framer-text: Open Runde 16px/25.6px 400, #666666, ls -0.32px |
| Transition | none |
| How | at rest |

Crops: `blog-post-body-default.png`.

#### blog-post-link

Back link. The link returning to the index.

Page: blog-post. Selector: `back link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56.69 x 35.36 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Open Runde 16px/19.36px 500, #1e1e1e @ 0.7, ls -0.32px | p.framer-text: Open Runde 16px/19.36px 500, #000000, ls -0.32px | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-GZ0tw.framer-ymsmdp 56.7x35.4 r 100px outline 1px auto #005fcc offset 1px | = |

Crops: `blog-post-link-default.png`, `blog-post-link-hover.png`, `blog-post-link-focus-visible.png`, `blog-post-link-pressed.png`.

#### altitude-title

Page title.

Page: altitude. Selector: `h1,h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Runde 48px/56px 600 |
| Letter spacing | -1.44px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `altitude-title-default.png`.

#### altitude-body

Body text.

Page: altitude. Selector: `body p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Runde 16px/24px 500 |
| Letter spacing | -0.32px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `altitude-body-default.png`.

#### altitude-link

Back link. The link returning to the index.

Page: altitude. Selector: `back link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56.69 x 35.36 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Open Runde 16px/19.36px 500, #1e1e1e @ 0.7, ls -0.32px | p.framer-text: Open Runde 16px/19.36px 500, #000000, ls -0.32px | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-GZ0tw.framer-ymsmdp 56.7x35.4 r 100px outline 1px auto #005fcc offset 1px | = |

Crops: `altitude-link-default.png`, `altitude-link-hover.png`, `altitude-link-focus-visible.png`, `altitude-link-pressed.png`.

### Landing pages (programmatic)

#### freelancer-invoicing-title

Page title.

Page: freelancer-invoicing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 780 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Runde 48px/56px 600 |
| Letter spacing | -1.44px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `freelancer-invoicing-title-default.png`.

#### freelancer-invoicing-cta

Page CTA.

Page: freelancer-invoicing. Selector: `page cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 148.56 x 40 | = | = | = |
| Padding | 6px 14px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #0d111b | #000000 @ 0.88 | = | = |
| Box shadow | #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Open Runde 16px/24px 500, #ffffff, ls -0.32px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 148.562px x 40px, absolute, bg #000000 @ 0, radius 100px | = | = | = |
| Painted layers | a.framer-Ygbcr.framer-z7gpue 148.6x40.0 bg #0d111b r 100px shadow #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px; a::after.framer-Ygbcr.framer-z7gpue 148.562pxx40px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 100px | a.framer-Ygbcr.framer-z7gpue 148.6x40.0 bg #000000 @ 0.88 r 100px shadow #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px; a::after.framer-Ygbcr.framer-z7gpue 148.562pxx40px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 100px | a.framer-Ygbcr.framer-z7gpue 148.6x40.0 bg #0d111b r 100px shadow #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px outline 1px auto #005fcc offset 1px; a::after.framer-Ygbcr.framer-z7gpue 148.562pxx40px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 100px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `freelancer-invoicing-cta-default.png`, `freelancer-invoicing-cta-hover.png`, `freelancer-invoicing-cta-focus-visible.png`, `freelancer-invoicing-cta-pressed.png`.

#### freelancer-invoicing-section

Section title.

Page: freelancer-invoicing. Selector: `h2 (or second heading)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Runde 40px/48px 600 |
| Letter spacing | -1.2px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `freelancer-invoicing-section-default.png`.

#### stablecoin-invoicing-title

Page title.

Page: stablecoin-invoicing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 576 x 216 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Selecta Medium 72px/72px 500 |
| Letter spacing | -1.44px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `stablecoin-invoicing-title-default.png`.

#### stablecoin-invoicing-cta

Page CTA.

Page: stablecoin-invoicing. Selector: `page cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 148.56 x 40 | = | = | = |
| Padding | 6px 14px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #0d111b | #000000 @ 0.88 | = | = |
| Box shadow | #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Open Runde 16px/24px 500, #ffffff, ls -0.32px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 148.562px x 40px, absolute, bg #000000 @ 0, radius 100px | = | = | = |
| Painted layers | a.framer-Ygbcr.framer-z7gpue 148.6x40.0 bg #0d111b r 100px shadow #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px; a::after.framer-Ygbcr.framer-z7gpue 148.562pxx40px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 100px | a.framer-Ygbcr.framer-z7gpue 148.6x40.0 bg #000000 @ 0.88 r 100px shadow #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px; a::after.framer-Ygbcr.framer-z7gpue 148.562pxx40px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 100px | a.framer-Ygbcr.framer-z7gpue 148.6x40.0 bg #0d111b r 100px shadow #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px outline 1px auto #005fcc offset 1px; a::after.framer-Ygbcr.framer-z7gpue 148.562pxx40px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 100px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `stablecoin-invoicing-cta-default.png`, `stablecoin-invoicing-cta-hover.png`, `stablecoin-invoicing-cta-focus-visible.png`, `stablecoin-invoicing-cta-pressed.png`.

#### stablecoin-invoicing-section

Section title.

Page: stablecoin-invoicing. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 297.38 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Selecta Medium 56px/56px 500 |
| Letter spacing | -1.68px |
| Colour | #000000 @ 0.9 |
| Transition | none |
| How | at rest |

Crops: `stablecoin-invoicing-section-default.png`.

#### location-title

Page title.

Page: location. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 695 x 128 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Selecta Medium 64px/64px 500 |
| Letter spacing | -1.3px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `location-title-default.png`.

#### location-cta

Page CTA.

Page: location. Selector: `page cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 148.56 x 40 | = | = | = |
| Padding | 6px 14px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #0d111b | #000000 @ 0.88 | = | = |
| Box shadow | #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Open Runde 16px/24px 500, #ffffff, ls -0.32px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 148.562px x 40px, absolute, bg #000000 @ 0, radius 100px | = | = | = |
| Painted layers | a.framer-Ygbcr.framer-z7gpue 148.6x40.0 bg #0d111b r 100px shadow #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px; a::after.framer-Ygbcr.framer-z7gpue 148.562pxx40px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 100px | a.framer-Ygbcr.framer-z7gpue 148.6x40.0 bg #000000 @ 0.88 r 100px shadow #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px; a::after.framer-Ygbcr.framer-z7gpue 148.562pxx40px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 100px | a.framer-Ygbcr.framer-z7gpue 148.6x40.0 bg #0d111b r 100px shadow #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px outline 1px auto #005fcc offset 1px; a::after.framer-Ygbcr.framer-z7gpue 148.562pxx40px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 100px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `location-cta-default.png`, `location-cta-hover.png`, `location-cta-focus-visible.png`, `location-cta-pressed.png`.

#### location-section

Section title.

Page: location. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Selecta Medium 64px/64px 500 |
| Letter spacing | -1.28px |
| Colour | #1a1a1a |
| Transition | none |
| How | at rest |

Crops: `location-section-default.png`.

### Legal text

#### terms-title

Page title.

Page: terms. Selector: `h1-h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 158.05 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Runde 64px/64px 600 |
| Letter spacing | -1.92px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `terms-title-default.png`.

#### terms-body

Body text.

Page: terms. Selector: `legal p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 704 x 196 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Selecta Regular 18px/28px 400 |
| Letter spacing | -0.32px |
| Colour | #666666 |
| Transition | none |
| How | at rest |

Crops: `terms-body-default.png`.

#### privacy-title

Page title.

Page: privacy. Selector: `h1-h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 158.05 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Runde 64px/64px 600 |
| Letter spacing | -1.92px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `privacy-title-default.png`.

#### privacy-body

Body text.

Page: privacy. Selector: `legal p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 704 x 308 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Selecta Regular 18px/28px 400 |
| Letter spacing | -0.32px |
| Colour | #666666 |
| Transition | none |
| How | at rest |

Crops: `privacy-body-default.png`.

### Mobile (390 wide)

#### m-nav-bar

Mobile top bar. The mobile header: logo left, menu trigger right.

Page: home. Selector: `mobile nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 48 |
| Padding | 0px 24px 8px 20px |
| Border | none |
| Radius | 0px 0px 24px 24px |
| Background | transparent |
| Box shadow | none |
| Backdrop filter | blur(10px) |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Icon | 18 x 14, colour #000000 |
| Painted layers | div.framer-1i2m7ev 112.0x16.0 image url(data:…)%22></path><path d=%22M 17.846 0.4 C 17.846 0.179 17.667 0 17.446 0 L 14.554 0  |
| Ancestor paint | 1 up div.framer-1ve1fz9 bg #f5f5f5 @ 0.6 shadow #000000 @ 0.1 0px 1px 2px 0px |
| How | at rest |

Crops: `m-nav-bar-default.png`.

#### m-menu-trigger

Mobile menu trigger. The menu button (the 24px icon box at the right of the top bar). Pressed once below to open the menu; a local disclosure.

Page: home. Selector: `nav icon box`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Icon | 18 x 14, colour #000000 | = | = | = |
| Ancestor paint | 2 up div.framer-1ve1fz9 bg #f5f5f5 @ 0.6 shadow #000000 @ 0.1 0px 1px 2px 0px | = | = | = |
| How | at rest | mouse hover | focus failed | CDP forcePseudoState :active:hover |

Crops: `m-menu-trigger-default.png`, `m-menu-trigger-hover.png`, `m-menu-trigger-focus-visible.png`, `m-menu-trigger-pressed.png`.

#### m-hero-title

Mobile hero title.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Runde 40px/48px 600 |
| Letter spacing | -1.2px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `m-hero-title-default.png`.

#### m-nav-panel

Mobile menu (open). The opened mobile menu panel; pressed once, nothing navigated.

Page: home. Selector: `mobile menu open`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px 16px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | #fafafa |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text: Selecta Medium 40px/40px 500, #000000 @ 0.9, ls -1.2px |
| Transition | none |
| Icon | 14 x 14, colour #0000ee, fill #000000 |
| Painted layers | div.framer-TvleB.framer-135zmhh 390.0x844.0 bg #fafafa; a.framer-F1GKW.framer-1xvz6nn 358.0x40.0 image linear-gradient(#ffffff 1.42525%, #dedede 100%) r 40px shadow #000000 @ 0.25 0px 1px 1px 0px inset, #000000 @ 0.15 3px 3px 3px 0px; a.framer-Ygbcr.framer-z7gpue 358.0x40.0 bg #0d111b r 100px shadow #242628 0px 0px 0px 1px, #1b1c1d @ 0.48 0px 1px 2px 0px; a::after.framer-Ygbcr.framer-z7gpue 358pxx40px border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 100px; div.framer-1ve1fz9 358.0x80.0 bg #f5f5f5 @ 0.6 r 0px 0px 20px 20px shadow #000000 @ 0.1 0px 1px 2px 0px; div.framer-1i2m7ev 112.0x16.0 image url(data:…)%22></path><path d=%22M 17.846 0.4 C 17.846 0.179 17.667 0 17.446 0 L 14.554 0  |
| How | menu trigger pressed once |

Crops: `m-nav-panel-open.png`.

## Transitions declared in the readable stylesheets

acctual.com is a Framer site that inlines its stylesheets, all same-origin readable; its design tokens are hashed --token-<uuid> custom properties (see css-vars.json). The values below are computed styles read off the running pages; the per-state Transition rows are computed values.

- home: `opacity 0.4s ease-out`, `unset`

- pricing: none
