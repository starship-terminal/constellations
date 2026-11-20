# Glorify component measurements

Computed styles read from glorify.com and app.glorify.com on 2026-11-16 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the public surfaces — the light-only Framer marketing pages, the dark signed-out auth cards at /dashboard/login and /dashboard/register, and the anonymous editor the marketing "Play for free" CTA opens at /designer/use-template/0 (the upload onboarding, the Craft dialog behind "Try with Placeholder Image" and the canvas chrome) — with any consent layer hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `enabled` is a submit's fill once sample text sits in its fields, still never clicked; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle (the Features dropdown, the billing switcher, the inspector LAYERS tab, the Craft dialog's style pick).

## Components

### Site chrome

#### page-bg

Page field. The marketing body element — the painted field every page sits on.

Page: home. Selector: `body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 15728.42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | strong.framer-text: Inter 9px/10.8px 700, #fff9f3 |
| Transition | none |
| Icon | 75 x 24, colour #0000ee, fill #000000 |
| Painted layers | body 1440.0x15728.4 bg #ffffff; div.framer-2po4Y.framer-8uwo3 1440.0x15728.4 bg #ffffff; div.framer-165vwyy 1440.0x64.0 bg #111111; nav.framer-1zja2.framer-Ju3FI 1440.0x64.0 bg #ffffff; nav::after.framer-1zja2.framer-Ju3FI 1440pxx64px border B:1px #e5e0db; a.framer-1pxcn6y.framer-1v7amdl 97.0x23.6 bg #111111 r 2px |
| How | at rest |

Crops: none.

#### mkt-header

Site header. The marketing top bar: wordmark, the "Who is it for?"/Features/Resources/Templates dropdowns, Pricing, Login, "Play for free" and "Get Started Now".

Page: home. Selector: `[data-framer-name="Top nav"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 64 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | #111111 |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | strong.framer-text: Inter 9px/10.8px 700, #fff9f3 |
| Transition | none |
| Icon | 75 x 24, colour #0000ee, fill #000000 |
| Painted layers | div.framer-165vwyy 1440.0x64.0 bg #111111; nav.framer-1zja2.framer-Ju3FI 1440.0x64.0 bg #ffffff; nav::after.framer-1zja2.framer-Ju3FI 1440pxx64px border B:1px #e5e0db; a.framer-1pxcn6y.framer-1v7amdl 97.0x23.6 bg #111111 r 2px; a.framer-Jpd6U.framer-njOND 126.2x32.0 bg #ffffff r 8px; a.framer-Jpd6U.framer-njOND 95.4x32.0 bg #ffffff r 8px |
| Ancestor paint | 1 up div.framer-2po4Y.framer-8uwo3 bg #ffffff |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The Glorify wordmark in the header, linking home.

Page: home. Selector: `logo framer component`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 182 x 24 |
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
| Text node | strong.framer-text: Inter 9px/10.8px 700, #fff9f3 |
| Transition | none |
| Icon | 75 x 24, colour #0000ee, fill #000000 |
| Painted layers | a.framer-1pxcn6y.framer-1v7amdl 97.0x23.6 bg #111111 r 2px |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-link

Nav link. A marketing header nav link (Pricing); measured, never followed.

Page: home. Selector: `nav Pricing link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 61.61 x 30 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #eceffd | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1126out: Inter 14px/14px 500, #111111, ls -0.2px | p.framer-text.framer-styles-preset-1126out: Inter 14px/14px 500, #455eed @ 0.992, ls -0.2px | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-Jpd6U.framer-njOND 61.6x30.0 bg #ffffff r 8px | a.framer-Jpd6U.framer-njOND 61.6x30.0 bg #eceffd r 8px | a.framer-Jpd6U.framer-njOND 61.6x30.0 bg #ffffff r 8px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-features

Features nav trigger. The "Features" nav item that opens the feature-page dropdown on hover.

Page: home. Selector: `nav Features trigger`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 59.41 x 14 | = | - | = | = |
| Padding | 0px | = | - | = | = |
| Border | none | = | - | = | = |
| Radius | 0px | = | - | = | = |
| Background | transparent | = | - | = | = |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | Inter 14px/14px 500 | = | - | = | = |
| Letter spacing | -0.2px | = | - | = | = |
| Colour | #111111 | #455eed @ 0.894 | - | = | #455eed |
| Transition | none | = | - | = | = |
| Cursor | pointer | = | - | = | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | hovered the "Features" nav trigger to open its dropdown |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `nav-features-default.png`, `nav-features-hover.png`, `nav-features-pressed.png`, `nav-features-opened.png`.

#### nav-login

Login link. The "Login" nav action to app.glorify.com/welcome; measured, never followed.

Page: home. Selector: `nav Login link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 57.02 x 32 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #ffffff | #eceffd | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1k26699: Inter-Medium 16px/16px 500, #000000, ls -0.2px | p.framer-text.framer-styles-preset-1k26699: Inter-Medium 16px/16px 500, #455eec, ls -0.2px | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-nVpef.framer-R8fVZ 57.0x32.0 bg #ffffff r 4px | a.framer-nVpef.framer-R8fVZ 57.0x32.0 bg #eceffd r 4px | a.framer-nVpef.framer-R8fVZ 57.0x32.0 bg #ffffff r 4px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-play

Play for free link. The "Play for free" nav action to the anonymous editor on app.glorify.com; measured, never followed.

Page: home. Selector: `nav Play for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 119.41 x 42 | = | = | = |
| Padding | 14px 18px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #455eed | #374bbf | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1126out: Inter 14px/14px 500, #fff9f3, ls -0.2px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-cLpv3.framer-R8fVZ 119.4x42.0 bg #455eed r 8px | a.framer-cLpv3.framer-R8fVZ 119.4x42.0 bg #374bbf r 8px | a.framer-cLpv3.framer-R8fVZ 119.4x42.0 bg #455eed r 8px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-play-default.png`, `nav-play-hover.png`, `nav-play-focus-visible.png`, `nav-play-pressed.png`.

#### nav-cta

Get Started Now button. The header "Get Started Now" CTA on /pricing ([data-framer-name="Button Wrap"]); measured, never followed.

Page: pricing. Selector: `[data-framer-name="Button Wrap"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 188.42 x 42 | = | - | = |
| Padding | 0px | = | - | = |
| Gap | 12px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | sans-serif 12px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | p.framer-text.framer-styles-preset-1k26699: Inter-Medium 16px/16px 500, #000000, ls -0.2px | = | - | = |
| Transition | none | = | - | = |
| Painted layers | a.framer-nVpef.framer-R8fVZ 57.0x32.0 bg #ffffff r 4px; a.framer-cLpv3.framer-R8fVZ 119.4x42.0 bg #455eed r 8px | a.framer-nVpef.framer-R8fVZ 57.0x32.0 bg #ffffff r 4px; a.framer-cLpv3.framer-R8fVZ 119.4x42.0 bg #374bbf r 8px | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-pressed.png`.

### Home

#### hero-h1

Hero headline. "Easily create marketing visuals that turn browsers to buyers." — the display heading.

Page: home. Selector: `home h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 838 x 230.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PolySans Trial Median 64px/76.8px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span: PolySans Trial Median 64px/76.8px 400, #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-sub

Hero subline. The paragraph under the hero heading ("Enjoy the ultimate Ecom design tool…").

Page: home. Selector: `hero paragraph`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 432 x 51.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/25.6px 500 |
| Letter spacing | -0.2px |
| Colour | #737373 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-cta

Hero CTA. The hero "Play for free" button to the anonymous editor — an outlined ghost on the dark hero band, not the filled nav button (the leaf text is tagged in-page: the nav's identical label is the DOM-first match). Measured, never followed.

Page: home. Selector: `hero Play for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 119.41 x 46 | = | = | = |
| Padding | 14px 18px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1126out: Inter 14px/14px 500, #ffffff, ls -0.2px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 119.406px x 46px, absolute, bg #000000 @ 0, radius 8px | = | = | = |
| Painted layers | a::after.framer-13l81z2.framer-19c9wqe 119.406pxx46px border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 8px | = | a.framer-13l81z2.framer-19c9wqe 119.4x46.0 r 8px outline 1px auto #101010 offset 1px; a::after.framer-13l81z2.framer-19c9wqe 119.406pxx46px border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 8px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | = |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### home-h2

Section heading. A section heading on the marketing home.

Page: home. Selector: `home h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 288 x 28.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PolySans Trial Median 24px/28.8px 400 |
| Letter spacing | normal |
| Colour | #212121 |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 3 up div.framer-HsAFm.framer-Rpfsn shadow #000000 @ 0.25 0px 4px 40px 0px |
| How | at rest |

Crops: `home-h2-default.png`.

#### home-card

Home card. A feature/benefit card on the marketing home.

Page: home. Selector: `home card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 252 x 257.34 | = |
| Padding | 12px | = |
| Gap | 30px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0.1 0px 4px 24px 0px | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | p.framer-text.framer-styles-preset-1atgx5g: Inter 14px/19.6px 500, #403d3a, ls -0.2px | = |
| Transition | none | = |
| Icon | 24 x 24, colour #fd4370 | = |
| ::after | 252px x 257.344px, absolute, bg #000000 @ 0, radius 16px | = |
| Painted layers | div.framer-119jd0n 252.0x257.3 bg #ffffff r 16px shadow #000000 @ 0.1 0px 4px 24px 0px; div::after.framer-119jd0n 252pxx257.344px border T:1px #cccccc / R:1px #cccccc / B:1px #cccccc / L:1px #cccccc r 16px; div.framer-94x9fa 28.0x28.0 bg #ffedf1 r 226px; div.framer-rkxvci 28.0x28.0 bg #ffedf1 r 226px | = |
| How | at rest | mouse hover |

Crops: `home-card-default.png`, `home-card-hover.png`.

#### home-learn-more

Learn more link. A "Learn more" link inside a home feature row; measured, never followed.

Page: home. Selector: `home Learn more link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 89.02 x 34 | 99.05 x 34 | = | = |
| Padding | 10px 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | 8.07662% 23.5294% | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-ikf2jj: Inter-SemiBold 12px/12px 600, #51cab4, ls -0.2px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #0000ee, fill #000000 | = | = | 14 x 14, colour #ff0000, fill #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, 0) | = | = |
| Painted layers | - | = | a.framer-cLpv3.framer-R8fVZ 89.0x34.0 r 8px outline 1px auto #101010 offset 1px | = |

Crops: `home-learn-more-default.png`, `home-learn-more-hover.png`, `home-learn-more-focus-visible.png`, `home-learn-more-pressed.png`.

### Footer

#### footer-col

Footer. The marketing footer: sitemap columns, legal and social links.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 916.39 |
| Padding | 48px 48px 0px 48px |
| Gap | 48px |
| Border | none |
| Radius | 0px |
| Background | #111111 |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | strong.framer-text: Inter 9px/10.8px 700, #111110 |
| Transition | none |
| Icon | 100 x 32, colour #0000ee, fill #000000 |
| Painted layers | div.framer-1t6j7b6 1440.0x916.4 bg #111111; a.framer-1pxcn6y.framer-1v7amdl 97.0x23.6 bg #fff9f3 r 2px; a.framer-cLpv3.framer-R8fVZ 192.8x48.0 bg #455eed r 8px; div.framer-115osdi 21.0x21.0 image url(data:…)%22></path></svg>"); a.framer-tJd9d.framer-papEL 105.0x23.2 bg #51cab4 r 51px; a.framer-tJd9d.framer-papEL 104.0x23.2 bg #6245f2 r 51px |
| Ancestor paint | 1 up div.framer-bDhx2.framer-U3eTC bg #111111 |
| How | at rest |

Crops: `footer-col-default.png`.

#### footer-link

Footer link. A link inside the marketing footer; measured, never followed.

Page: home. Selector: `footer link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 113.2 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 14px/19.6px 500 | = | = | = |
| Letter spacing | -0.2px | = | = | = |
| Colour | #c0bcb8 | #455eed | = | #455eed |
| Transition | color 0.3s cubic-bezier(0.44, 0, 0.56, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-text.framer-styles-preset-e6xapj 113.2x17.0 outline 1px auto #101010 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Pricing

#### bill-monthly

Billing tab (monthly). The "Monthly" side of the pricing billing switcher; opened is the state after clicking it — a local UI toggle.

Page: pricing. Selector: `billing Monthly`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 60.33 x 20 | = | - | = | = |
| Padding | 0px | = | - | = | = |
| Border | none | = | - | = | = |
| Radius | 0px | = | - | = | = |
| Background | transparent | = | - | = | = |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | Inter-Medium 16px/20px 500 | = | - | = | = |
| Letter spacing | -0.24px | = | - | = | = |
| Colour | #111111 | = | - | = | = |
| Transition | none | = | - | = | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | clicked "Monthly" to show monthly prices |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `bill-monthly-default.png`, `bill-monthly-hover.png`, `bill-monthly-pressed.png`, `bill-monthly-opened.png`.

#### bill-yearly

Billing tab (yearly). The "Yearly" side of the billing switcher; opened is the state after clicking it — a local UI toggle.

Page: pricing. Selector: `billing Yearly`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 46.56 x 20 | = | - | = | = |
| Padding | 0px | = | - | = | = |
| Border | none | = | - | = | = |
| Radius | 0px | = | - | = | = |
| Background | transparent | = | - | = | = |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | Inter-Medium 16px/20px 500 | = | - | = | = |
| Letter spacing | -0.24px | = | - | = | = |
| Colour | #acacac | = | - | = | = |
| Transition | none | = | - | = | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | clicked "Yearly" to show annual prices |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `bill-yearly-default.png`, `bill-yearly-hover.png`, `bill-yearly-pressed.png`, `bill-yearly-opened.png`.

#### plan-card

Plan card. A pricing plan card (name, price, feature list, trial CTA) — the Framer "Card/Card Plans Free" component (~230x154).

Page: pricing. Selector: `pricing plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 230 x 149.41 |
| Padding | 18px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.framer-text: PolySans Trial Median 22px/26.4px 400, #000000 |
| Transition | none |
| Icon | 14 x 14, colour #0000ee, fill #000000 |
| ::after | 230px x 149.406px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | div.framer-1f3dyck 230.0x149.4 bg #ffffff; div::after.framer-1f3dyck 230pxx149.406px border L:1px #e5e0db; a.framer-cLpv3.framer-R8fVZ 142.6x34.0 bg #eceffd r 8px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-price

Plan price. The price figure inside a plan card.

Page: pricing. Selector: `pricing price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 34 x 38.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PolySans Trial Median 32px/38.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. A plan card's "Start … Trial" action to /dashboard/register; its states were measured but it was never followed — no trial was started.

Page: pricing. Selector: `pricing Start Pro Trial`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 135 x 39.2 | = | = | = |
| Padding | 10px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #455eed | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-bj3z9v: Inter-Medium 12px/19.2px 500, #fff9f3 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-cLpv3.framer-R8fVZ 135.0x39.2 bg #455eed r 8px; div.framer-115osdi 14.0x14.0 image url(data:…)%22></path></svg>") | = | a.framer-cLpv3.framer-R8fVZ 135.0x39.2 bg #455eed r 8px outline 1px auto #101010 offset 1px; div.framer-115osdi 14.0x14.0 image url(data:…)%22></path></svg>") | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-row

Plan feature row. A feature row inside a plan card or the compare table.

Page: pricing. Selector: `pricing feature row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 90.2 x 14 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/14px 500 |
| Letter spacing | -0.2px |
| Colour | #111111 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `plan-row-default.png`.

#### compare-h2

Compare heading. The "Compare Plans" table heading.

Page: pricing. Selector: `pricing Compare Plans`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 38.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PolySans Trial Median 32px/38.4px 400 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| How | at rest |

Crops: `compare-h2-default.png`.

### Feature page

#### feat-h1

Feature headline. The /features/background-remover page heading.

Page: feature. Selector: `feature h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 568 x 153.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PolySans Trial Median 64px/76.8px 400 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| How | at rest |

Crops: `feat-h1-default.png`.

#### feat-cta

Feature CTA. The feature hero's filled "Get Started Now" action — the nav's "Play for free" is the DOM-first match, so the leaf text is tagged in-page. Measured, never followed.

Page: feature. Selector: `feature CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 178.02 x 48 | = | = | = |
| Padding | 14px 18px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #455eed | #374bbf | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1126out: Inter 14px/14px 500, #fff9f3, ls -0.2px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-cLpv3.framer-R8fVZ 178.0x48.0 bg #455eed r 8px; div.framer-115osdi 21.0x21.0 image url(data:…)%22></path></svg>") | a.framer-cLpv3.framer-R8fVZ 178.0x48.0 bg #374bbf r 8px; div.framer-115osdi 21.0x21.0 image url(data:…)%22></path></svg>") | a.framer-cLpv3.framer-R8fVZ 178.0x48.0 bg #455eed r 8px outline 1px auto #101010 offset 1px; div.framer-115osdi 21.0x21.0 image url(data:…)%22></path></svg>") | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `feat-cta-default.png`, `feat-cta-hover.png`, `feat-cta-focus-visible.png`, `feat-cta-pressed.png`.

#### feat-card

Feature card. A benefit card on the feature page ("Fast", "Inexpensive", "Manual Option").

Page: feature. Selector: `feature card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1200 x 572.8 | = |
| Padding | 0px | = |
| Gap | 48px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h2.framer-text.framer-styles-preset-1wlsuh1: PolySans Trial Median 24px/28.8px 400, #111111 | = |
| Transition | none | = |
| How | at rest | mouse hover |

Crops: `feat-card-default.png`, `feat-card-hover.png`.

#### feat-prose

Feature paragraph. A body paragraph on the feature page.

Page: feature. Selector: `feature p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 518 x 84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter-Medium 20px/28px 500 |
| Letter spacing | -0.3px |
| Colour | #111111 |
| Transition | none |
| How | at rest |

Crops: `feat-prose-default.png`.

### Templates

#### tpl-h1

Templates headline. The templates gallery heading.

Page: templates. Selector: `templates h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 149 x 19.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter-Medium 12px/19.2px 500 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| How | at rest |

Crops: `tpl-h1-default.png`.

#### tpl-card

Template tile. A template thumbnail tile on the /templates draggable canvas (a Framer "Row n - m"/"Beauty n - m" tile with artwork) — the gallery is a pan-canvas, not a link grid.

Page: templates. Selector: `templates tile (data-framer-name tile)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 193.93 x 102.31 | 187.14 x 102.26 |
| Padding | 0px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| How | at rest | mouse hover |

Crops: `tpl-card-default.png`, `tpl-card-hover.png`.

#### tpl-cat

Template category link. A template-category link; measured, never followed.

Page: templates. Selector: `templates category link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 97.61 x 28 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-ikf2jj: Inter-SemiBold 12px/12px 600, #ffffff, ls -0.2px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-Gl7qc.framer-vGu9P 97.6x28.0 outline 1px auto #101010 offset 1px | = |

Crops: `tpl-cat-default.png`, `tpl-cat-hover.png`, `tpl-cat-focus-visible.png`, `tpl-cat-pressed.png`.

### Template marketplace

#### mk-h1

Marketplace headline. The "New template marketplace" heading.

Page: marketplace. Selector: `marketplace h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 185 x 19.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter-Medium 12px/19.2px 500 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| How | at rest |

Crops: `mk-h1-default.png`.

#### mk-tag

Marketplace filter. A use-case/style filter pill on the marketplace.

Page: marketplace. Selector: `marketplace filter`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 100 x 23.41 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | sans-serif 12px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | h3.framer-text.framer-styles-preset-1gkuhzd: Inter 18px/23.4px 700, #111111, ls -0.36px | = | - | = |
| Transition | none | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `mk-tag-default.png`, `mk-tag-hover.png`, `mk-tag-pressed.png`.

#### mk-card

Marketplace card. A template card in the marketplace grid (the first thumbnail link over 150px); measured, never followed.

Page: marketplace. Selector: `marketplace card (a>img)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 384 x 256 | 395.52 x 263.68 |
| Padding | 0px | = |
| Gap | 10px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #0000ee | = |
| Text node | span.framer-text: Inter 14px/14px 700, #51cab4, ls -0.2px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.framer-jDlMw.framer-qt0hyh 47.2x30.0 bg #ffffff r 6px shadow #000000 @ 0.15 0px 1px 3px 0px; span.framer-text 35.4x18.2 image linear-gradient(54deg, #1db89b 8%, #2cd1b3 74%) | div.framer-jDlMw.framer-qt0hyh 48.6x30.9 bg #ffffff r 6px shadow #000000 @ 0.15 0px 1px 3px 0px; span.framer-text 36.5x18.7 image linear-gradient(54deg, #1db89b 8%, #2cd1b3 74%) |
| How | at rest | mouse hover |
| Transform | - | matrix(1.03, 0, 0, 1.03, 0, 0) |

Crops: `mk-card-default.png`, `mk-card-hover.png`.

### Learn

#### learn-h1

Learn headline. The "Learn about Glorify, Ecom, Design and more" heading.

Page: learn. Selector: `learn h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 153.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PolySans Trial Median 64px/76.8px 400 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| How | at rest |

Crops: `learn-h1-default.png`.

#### learn-cat

Learn filter. The "All" category pill on the Learn hub; the leaf text node is tagged in-page because a hasText filter resolves the page wrapper.

Page: learn. Selector: `learn filter`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 18.41 x 16 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter-Medium 16px/16px 500 | = | - | = |
| Letter spacing | -0.2px | = | - | = |
| Colour | #fff9f3 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `learn-cat-default.png`, `learn-cat-hover.png`, `learn-cat-pressed.png`.

#### learn-card

Article card. A Learn article card (cover, category tag, title) — the card wrapping the first article-title heading; measured, never followed.

Page: learn. Selector: `learn article card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 384 x 433.86 | = |
| Padding | 12px | = |
| Gap | 15px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #fff9f3 | #ffffff |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #0000ee | = |
| Text node | h3.framer-text.framer-styles-preset-e95k8c: Inter-Bold 14px/19.6px 700, #455eed | = |
| Transition | none | = |
| Cursor | pointer | = |
| ::after | 384px x 433.859px, absolute, bg #000000 @ 0, radius 8px | = |
| Painted layers | a.framer-Ui7ks.framer-uMrcI 384.0x433.9 bg #fff9f3 r 8px; a::after.framer-Ui7ks.framer-uMrcI 384pxx433.859px border T:1px #d9d4ce / R:1px #d9d4ce / B:1px #d9d4ce / L:1px #d9d4ce r 8px; div.framer-1k8gj12 360.0x202.5 r 8px shadow #000000 @ 0 0px 0px 0px 0px; div::after.framer-1k8gj12 360pxx202.484px border T:1px #d9d4ce / R:1px #d9d4ce / B:1px #d9d4ce / L:1px #d9d4ce r 8px | a.framer-Ui7ks.framer-uMrcI 384.0x433.9 bg #ffffff r 8px; a::after.framer-Ui7ks.framer-uMrcI 384pxx433.859px border T:1px #4a61ec / R:1px #4a61ec / B:1px #4a61ec / L:1px #4a61ec r 8px; div.framer-1k8gj12 360.0x202.5 r 8px shadow #000000 @ 0.15 0px 14.7299px 14.7299px 0px; div::after.framer-1k8gj12 360pxx202.484px border T:1px #d9d4ce / R:1px #d9d4ce / B:1px #d9d4ce / L:1px #d9d4ce r 8px |
| How | at rest | mouse hover |

Crops: `learn-card-default.png`, `learn-card-hover.png`.

#### learn-tag

Article tag. A category tag on an article card.

Page: learn. Selector: `learn article tag`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 84.2 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-ikf2jj: Inter-SemiBold 12px/12px 600, #8c8c87, ls -0.2px |
| Transition | none |
| Painted layers | a.framer-Gl7qc.framer-vGu9P 84.2x28.0 bg #fff9f3 r 4px |
| How | at rest |

Crops: `learn-tag-default.png`.

### Submit a template

#### st-h1

Submit headline. The "Submit your template" heading.

Page: submit. Selector: `submit h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 76.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PolySans Trial Median 64px/76.8px 400 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| How | at rest |

Crops: `st-h1-default.png`.

#### st-quote

Privileges card. The "Creator Privileges" card on the submit-a-template page.

Page: submit. Selector: `submit card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 148.8 |
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
| Text node | h2.framer-text.framer-styles-preset-1wlsuh1: PolySans Trial Median 24px/28.8px 400, #111111 |
| Transition | none |
| Painted layers | div.framer-ezV4n.framer-V0vyO 369.3x88.0 bg #eefaf8 r 16px; div::after.framer-ezV4n.framer-V0vyO 369.328pxx88px border T:1px #7cd7c6 / R:1px #7cd7c6 / B:1px #7cd7c6 / L:1px #7cd7c6 r 16px; div::after.framer-hh2qk4 64pxx64px border T:1px #51cab4 / R:1px #51cab4 / B:1px #51cab4 / L:1px #51cab4 r 8px; div.framer-ezV4n.framer-V0vyO 369.3x88.0 bg #eefaf8 r 16px; div::after.framer-ezV4n.framer-V0vyO 369.328pxx88px border T:1px #7cd7c6 / R:1px #7cd7c6 / B:1px #7cd7c6 / L:1px #7cd7c6 r 16px; div::after.framer-hh2qk4 64pxx64px border T:1px #51cab4 / R:1px #51cab4 / B:1px #51cab4 / L:1px #51cab4 r 8px |
| How | at rest |

Crops: `st-quote-default.png`.

#### st-prose

Submit paragraph. A guidelines paragraph on the submit page.

Page: submit. Selector: `submit p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 718 x 76.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/25.6px 500 |
| Letter spacing | -0.2px |
| Colour | #111111 |
| Transition | none |
| How | at rest |

Crops: `st-prose-default.png`.

### App sign-in

#### app-bg

App page field. The app body element — the dark field the auth cards and editor chrome sit on.

Page: login. Selector: `body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #212121 |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.text-heading-2.font-medium: Inter 20px/32px 500, #ffffff |
| Transition | none |
| Cursor | url(…), default |
| Icon | 16 x 16, colour #6a7ef1 |
| Painted layers | body.page--onboarding.using-mouse 1440.0x900.0 bg #212121; div.w-full.justify-center 352.0x48.0 bg #212121; button.button.button-primary 352.0x32.0 border T:1px #6a7ef1 / R:1px #6a7ef1 / B:1px #6a7ef1 / L:1px #6a7ef1 r 8px outline 2px solid #000000 @ 0 offset 2px; hr.w-full.border-light-300 158.5x1.0 border T:1px #434242; hr.w-full.border-light-300 158.5x1.0 border T:1px #434242; div.field-container.flex 352.0x32.0 bg #323232 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest |

Crops: none.

#### login-title

Sign-in headline. The "Sign in to your account" heading (a p leaf) on app.glorify.com/dashboard/login.

Page: login. Selector: `signin heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 219 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/32px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | url(…), default |
| How | at rest |

Crops: `login-title-default.png`.

#### login-card

Sign-in card. The sign-in form card — the flex column (~352px) holding the e-mail and password fields, the primary submit and the Google OAuth button; tagged by walking up from the e-mail input to the first card-sized ancestor.

Page: login. Selector: `signin card ancestor`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 352 x 384 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.text-heading-2.font-medium: Inter 20px/32px 500, #ffffff |
| Transition | none |
| Cursor | url(…), default |
| Icon | 16 x 16, colour #6a7ef1 |
| Painted layers | div.w-full.justify-center 352.0x48.0 bg #212121; button.button.button-primary 352.0x32.0 border T:1px #6a7ef1 / R:1px #6a7ef1 / B:1px #6a7ef1 / L:1px #6a7ef1 r 8px outline 2px solid #000000 @ 0 offset 2px; hr.w-full.border-light-300 158.5x1.0 border T:1px #434242; hr.w-full.border-light-300 158.5x1.0 border T:1px #434242; div.field-container.flex 352.0x32.0 bg #323232 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px outline 2px solid #000000 @ 0 offset 0px; input.field-container__input.w-full-imp 336.0x30.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 2px |
| How | at rest |

Crops: `login-card-default.png`.

#### login-field

Email field (sign-in). The sign-in e-mail input; focused and typed into then cleared — never submitted.

Page: login. Selector: `signin email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 336 x 30 | = | = |
| Padding | 6px 0px | = | = |
| Border | 1px solid #000000 @ 0 | = | = |
| Radius | 2px | = | = |
| Background | transparent | = | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 12px/16px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | background-color, border-color, color, fill, stroke 0.3s linear | = | = |
| Cursor | text | = | = |
| Placeholder | #a7a5a5, opacity 1 | = | = |
| Painted layers | input.field-container__input.w-full-imp 336.0x30.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 2px | input.field-container__input.w-full-imp 336.0x30.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 2px shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | input.field-container__input.w-full-imp 336.0x30.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 2px shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-field-default.png`, `login-field-focused.png`, `login-field-filled.png`.

#### login-pass

Password field (sign-in). The sign-in password input; focused and typed into then cleared — never submitted.

Page: login. Selector: `signin password input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 313.09 x 30 | = | = |
| Padding | 6px 0px | = | = |
| Border | 1px solid #000000 @ 0 | = | = |
| Radius | 2px | = | = |
| Background | transparent | = | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 12px/16px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | background-color, border-color, color, fill, stroke 0.3s linear | = | = |
| Cursor | text | = | = |
| Placeholder | #a7a5a5, opacity 1 | = | = |
| Painted layers | input.field-container__input.w-full-imp 313.1x30.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 2px | input.field-container__input.w-full-imp 313.1x30.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 2px shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | input.field-container__input.w-full-imp 313.1x30.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 2px shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "sample-pass-123", then deleted; nothing sent |

Crops: `login-pass-default.png`, `login-pass-focused.png`, `login-pass-filled.png`.

#### login-submit

Sign-in submit. The primary "Sign in" submit; every state was measured but the button was never clicked — nothing was submitted. `enabled` is the fill it paints once sample text sits in both fields.

Page: login. Selector: `signin submit button`. States: default, hover, focus-visible, pressed, enabled.

| Property | default | hover | focus-visible | pressed | enabled |
|---|---|---|---|---|---|
| Size (w x h) | 352 x 32 | = | - | = | = |
| Padding | 8px 16px | = | - | = | = |
| Gap | 8px | = | - | = | = |
| Border | 1px solid #000000 @ 0 | = | - | = | = |
| Radius | 8px | = | - | = | = |
| Background | #868484 | = | - | = | #6a7ef1 |
| Box shadow | none | = | - | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | - | = | = |
| Font | Inter 14px/20px 400 | = | - | = | = |
| Letter spacing | normal | = | - | = | = |
| Colour | #ffffff | = | - | = | = |
| Text node | span.text-button-2.text-light-100: Inter 12px/16px 500, #ffffff | = | - | = | = |
| Transition | all 0.25s linear | = | - | = | = |
| Cursor | url(…), default | = | - | = | pointer |
| Painted layers | button.button.button-primary 352.0x32.0 bg #868484 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px outline 2px solid #000000 @ 0 offset 2px | = | - | = | button.button.button-primary 352.0x32.0 bg #6a7ef1 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | typed sample text into both fields so the submit enabled — still never clicked |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-pressed.png`, `login-submit-enabled.png`.

#### login-google

Google OAuth button. The "Sign in with Google" OAuth button; measured, never activated.

Page: login. Selector: `signin Google button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 352 x 32 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #6a7ef1 | = | 1px solid #272b42 | = |
| Radius | 8px | = | = | = |
| Background | transparent | #6a7ef1 | = | #6a7ef1 |
| Box shadow | none | = | #272b42 0px 0px 0px 1px | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.text-button-2.text-light-100: Inter 12px/16px 500, #6a7ef1 | span.text-button-2.text-light-100: Inter 12px/16px 500, #ffffff | = | span.text-button-2.text-light-100: Inter 12px/16px 500, #ffffff |
| Transition | all 0.25s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #6a7ef1 | 16 x 16, colour #ffffff | = | 16 x 16, colour #ffffff |
| Painted layers | button.button.button-primary 352.0x32.0 border T:1px #6a7ef1 / R:1px #6a7ef1 / B:1px #6a7ef1 / L:1px #6a7ef1 r 8px outline 2px solid #000000 @ 0 offset 2px | button.button.button-primary 352.0x32.0 bg #6a7ef1 border T:1px #6a7ef1 / R:1px #6a7ef1 / B:1px #6a7ef1 / L:1px #6a7ef1 r 8px outline 2px solid #000000 @ 0 offset 2px | button.button.button-primary 352.0x32.0 border T:1px #272b42 / R:1px #272b42 / B:1px #272b42 / L:1px #272b42 r 8px shadow #272b42 0px 0px 0px 1px outline 2px solid #000000 @ 0 offset 2px | button.button.button-primary 352.0x32.0 bg #6a7ef1 border T:1px #6a7ef1 / R:1px #6a7ef1 / B:1px #6a7ef1 / L:1px #6a7ef1 r 8px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-google-default.png`, `login-google-hover.png`, `login-google-focus-visible.png`, `login-google-pressed.png`.

#### login-forgot

Forgot/remember control. The "Forgot password?" link or "Remember me" checkbox label on the sign-in card; measured, never followed.

Page: login. Selector: `signin forgot/remember`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 113 x 16 | = | - | = |
| Padding | 0px 0px 0px 24px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 14px/20px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #434242 | #ffffff | - | #ffffff |
| Text node | span.text-subheading-2.text-light-700: Inter 12px/16px 500, #ffffff | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 16 x 16, colour #a7a5a5 | 16 x 16, colour #ffffff | - | = |
| ::after | 12px x 12px, absolute, bg #212121, radius 9999px | = | - | = |
| Painted layers | label::after.selection-control.checkbox 12pxx12px bg #212121 r 9999px; input.hidden 0.0x0.0 bg #ffffff border T:1px #6b7280 / R:1px #6b7280 / B:1px #6b7280 / L:1px #6b7280 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Ancestor paint | - | 1 up div.button.button-secondary bg #434242 | = | = |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `login-forgot-default.png`, `login-forgot-hover.png`, `login-forgot-pressed.png`.

#### login-signup

Sign-up link. The "Sign up" link beside the sign-in form; measured, never followed.

Page: login. Selector: `signin signup link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 46 x 16 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 12px/16px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #6a7ef1 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `login-signup-default.png`, `login-signup-hover.png`, `login-signup-pressed.png`.

### App sign-up

#### reg-title

Sign-up headline. The "Create your account" heading (a p leaf) on app.glorify.com/dashboard/register.

Page: register. Selector: `signup heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 199 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/32px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | url(…), default |
| How | at rest |

Crops: `reg-title-default.png`.

#### reg-name

Name field (sign-up). The sign-up "Full name" input; focused and typed into then cleared — never submitted.

Page: register. Selector: `signup name input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 336 x 30 | = | = |
| Padding | 6px 0px | = | = |
| Border | 1px solid #000000 @ 0 | = | = |
| Radius | 2px | = | = |
| Background | transparent | = | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 12px/16px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | background-color, border-color, color, fill, stroke 0.3s linear | = | = |
| Cursor | text | = | = |
| Placeholder | #a7a5a5, opacity 1 | = | = |
| Painted layers | input.field-container__input.w-full-imp 336.0x30.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 2px | input.field-container__input.w-full-imp 336.0x30.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 2px shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | input.field-container__input.w-full-imp 336.0x30.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 2px shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "Example User", then deleted; nothing sent |

Crops: `reg-name-default.png`, `reg-name-focused.png`, `reg-name-filled.png`.

#### reg-email

Email field (sign-up). The sign-up e-mail input; focused and typed into then cleared — never submitted.

Page: register. Selector: `signup email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 336 x 30 | = | = |
| Padding | 6px 0px | = | = |
| Border | 1px solid #000000 @ 0 | = | = |
| Radius | 2px | = | = |
| Background | transparent | = | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 12px/16px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | background-color, border-color, color, fill, stroke 0.3s linear | = | = |
| Cursor | text | = | = |
| Placeholder | #a7a5a5, opacity 1 | = | = |
| Painted layers | input.field-container__input.w-full-imp 336.0x30.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 2px | input.field-container__input.w-full-imp 336.0x30.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 2px shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | input.field-container__input.w-full-imp 336.0x30.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 2px shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `reg-email-default.png`, `reg-email-focused.png`, `reg-email-filled.png`.

#### reg-pass

Password field (sign-up). The sign-up password input; focused and typed into then cleared — never submitted.

Page: register. Selector: `signup password input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 313.09 x 30 | = | = |
| Padding | 6px 0px | = | = |
| Border | 1px solid #000000 @ 0 | = | = |
| Radius | 2px | = | = |
| Background | transparent | = | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 12px/16px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | background-color, border-color, color, fill, stroke 0.3s linear | = | = |
| Cursor | text | = | = |
| Placeholder | #a7a5a5, opacity 1 | = | = |
| Painted layers | input.field-container__input.w-full-imp 313.1x30.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 2px | input.field-container__input.w-full-imp 313.1x30.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 2px shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | input.field-container__input.w-full-imp 313.1x30.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 2px shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "sample-pass-123", then deleted; nothing sent |

Crops: `reg-pass-default.png`, `reg-pass-focused.png`, `reg-pass-filled.png`.

#### reg-submit

Sign-up submit. The primary sign-up submit; its states were measured but the button was never clicked — no account was created.

Page: register. Selector: `signup submit button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 352 x 32 | = | - | = |
| Padding | 8px 16px | = | - | = |
| Gap | 8px | = | - | = |
| Border | 1px solid #000000 @ 0 | = | - | = |
| Radius | 8px | = | - | = |
| Background | #868484 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | - | = |
| Font | Inter 14px/20px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Text node | span.text-button-2.text-light-100: Inter 12px/16px 500, #ffffff | = | - | = |
| Transition | all 0.25s linear | = | - | = |
| Cursor | url(…), default | = | - | = |
| Painted layers | button.button.button-primary 352.0x32.0 bg #868484 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px outline 2px solid #000000 @ 0 offset 2px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `reg-submit-default.png`, `reg-submit-hover.png`, `reg-submit-pressed.png`.

#### reg-google

Google OAuth button (sign-up). The "Sign up with Google" button; measured, never activated.

Page: register. Selector: `signup Google button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 352 x 32 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #6a7ef1 | = | 1px solid #272b42 | = |
| Radius | 8px | = | = | = |
| Background | transparent | #6a7ef1 | = | #6a7ef1 |
| Box shadow | none | = | #272b42 0px 0px 0px 1px | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.text-button-2.text-light-100: Inter 12px/16px 500, #6a7ef1 | span.text-button-2.text-light-100: Inter 12px/16px 500, #ffffff | = | span.text-button-2.text-light-100: Inter 12px/16px 500, #ffffff |
| Transition | all 0.25s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #6a7ef1 | 16 x 16, colour #ffffff | = | 16 x 16, colour #ffffff |
| Painted layers | button.button.button-primary 352.0x32.0 border T:1px #6a7ef1 / R:1px #6a7ef1 / B:1px #6a7ef1 / L:1px #6a7ef1 r 8px outline 2px solid #000000 @ 0 offset 2px | button.button.button-primary 352.0x32.0 bg #6a7ef1 border T:1px #6a7ef1 / R:1px #6a7ef1 / B:1px #6a7ef1 / L:1px #6a7ef1 r 8px outline 2px solid #000000 @ 0 offset 2px | button.button.button-primary 352.0x32.0 border T:1px #272b42 / R:1px #272b42 / B:1px #272b42 / L:1px #272b42 r 8px shadow #272b42 0px 0px 0px 1px outline 2px solid #000000 @ 0 offset 2px | button.button.button-primary 352.0x32.0 bg #6a7ef1 border T:1px #6a7ef1 / R:1px #6a7ef1 / B:1px #6a7ef1 / L:1px #6a7ef1 r 8px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `reg-google-default.png`, `reg-google-hover.png`, `reg-google-focus-visible.png`, `reg-google-pressed.png`.

#### reg-terms

Terms link. The terms/privacy link under the sign-up form; measured, never followed.

Page: register. Selector: `signup terms link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117 x 15 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6a7ef1 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.text-link-1.text-primary-300 117.0x15.0 outline 1px auto #101010 offset 1px | = |

Crops: `reg-terms-default.png`, `reg-terms-hover.png`, `reg-terms-focus-visible.png`, `reg-terms-pressed.png`.

### Anonymous editor

#### ob-title

Onboarding headline. The "Generate designs for your campaign" heading on the anonymous editor's upload screen.

Page: designer. Selector: `onboarding heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 346 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 500 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| Cursor | url(…), default |
| How | at rest |

Crops: `ob-title-default.png`.

#### ob-drop

Upload dropzone. The onboarding upload dropzone — the card-sized ancestor of the "Drag and drop…" prompt; measured at rest — no file was ever chosen or uploaded.

Page: designer. Selector: `onboarding dropzone (text ancestor)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 398 x 200 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 12px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.text-subheading-3.text-light-700: Inter 12px/16px 500, #111111 |
| Transition | all 0.25s linear |
| Cursor | url(…), default |
| Icon | 20 x 20, colour #a7a5a5 |
| Painted layers | form.form-upload.rounded-[12px] 398.0x200.0 bg #ffffff r 12px; input.file-input 0.0x0.0 bg #323232 r 2px |
| How | at rest |

Crops: `ob-drop-default.png`.

#### ob-ph

Placeholder Image card. The "Try with Placeholder Image" card — the product's own demo path into the canvas; measured, and only ever activated through its own spec flow.

Page: designer. Selector: `onboarding placeholder card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 206 x 46 | = | - | = |
| Padding | 0px | = | - | = |
| Gap | 6px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 14px/20px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Text node | h6.card-product__title: Inter 12px/16px 600, #455eed | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Ancestor paint | 1 up div.card-product.w-full bg #eceffd | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `ob-ph-default.png`, `ob-ph-hover.png`, `ob-ph-pressed.png`.

#### ob-own

Own-start link. The "I'll get started on my own" link (it bounces to /dashboard/register signed out); measured, never followed.

Page: designer. Selector: `onboarding own-start link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 142 x 16 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 12px/16px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #111111 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Ancestor paint | - | 1 up button.button.button-secondary bg #e0e0e0 outline 2px solid #000000 @ 0 | = | = |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `ob-own-default.png`, `ob-own-hover.png`, `ob-own-pressed.png`.

#### ed-header

Editor header. The editor top bar: file name dropdown, Login/Signup, zoom, Share, Download.

Page: designer. Selector: `header.app-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 545 x 56 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.dropdown__trigger-text.truncate: Inter 12px/16px 400, #ffffff |
| Transition | all 0.3s linear |
| Cursor | url(…), default |
| Icon | 20 x 20, colour #ffffff |
| Painted layers | div.panel-header-side-wrapper.sm:w-[fit-content] 331.0x56.0 bg #212121 border T:1px #434242 / R:1px #434242 / B:1px #434242 / L:1px #434242 r 12px; div.panel-header-side.flex 75.0x50.0 bg #212121 r 12px; button.default.dropdown__trigger 58.0x42.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px outline 2px solid #000000 @ 0 offset 2px; div.dropdown__menu.rounded-[12px] 0.0x0.0 bg #212121 border T:1px #434242 / R:1px #434242 / B:1px #434242 / L:1px #434242 r 16px shadow #000000 @ 0.06 0px 8px 17px 0px, #000000 @ 0.04 0px 31px 31px 0px, #000000 @ 0.02 0px 40px 42px 0px; div.bg-ui-01.rounded 0.0x0.0 bg #212121 r 8px; hr.border-ui-04 0.0x0.0 border T:1px #434242 |
| How | at rest |

Crops: `ed-header-default.png`.

#### ed-login

Editor Login button. The outlined "Login" button in the editor header; measured, never clicked.

Page: designer. Selector: `editor Login button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 65 x 32 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #455eed | = | 1px solid #272b42 | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | #455eed |
| Box shadow | none | = | #272b42 0px 0px 0px 1px | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.text-button-2.text-light-100: Inter 12px/16px 500, #455eed | = | = | span.text-button-2.text-light-100: Inter 12px/16px 500, #ffffff |
| Transition | all 0.25s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.button.button-primary 65.0x32.0 border T:1px #455eed / R:1px #455eed / B:1px #455eed / L:1px #455eed r 8px outline 2px solid #000000 @ 0 offset 2px | = | button.button.button-primary 65.0x32.0 border T:1px #272b42 / R:1px #272b42 / B:1px #272b42 / L:1px #272b42 r 8px shadow #272b42 0px 0px 0px 1px outline 2px solid #000000 @ 0 offset 2px | button.button.button-primary 65.0x32.0 bg #455eed border T:1px #455eed / R:1px #455eed / B:1px #455eed / L:1px #455eed r 8px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up div.panel-header-side__not-logged-box bg #212121; 2 up div.panel-header-side__not-logged.sm:hidden shadow #000000 @ 0.06 0px 8px 17px 0px, #000000 @ 0.04 0px 31px 31px 0px, #000000 @ 0.02 0px 40px 42px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ed-login-default.png`, `ed-login-hover.png`, `ed-login-focus-visible.png`, `ed-login-pressed.png`.

#### ed-signup

Editor Signup button. The filled "Signup" button in the editor header; measured, never clicked.

Page: designer. Selector: `editor Signup button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 73 x 32 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #272b42 | = |
| Radius | 8px | = | = | = |
| Background | #455eed | = | = | #374bbe |
| Box shadow | none | = | #272b42 0px 0px 0px 1px | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.text-button-2.text-light-100: Inter 12px/16px 500, #ffffff | = | = | = |
| Transition | all 0.25s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.button.button-primary 73.0x32.0 bg #455eed border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px outline 2px solid #000000 @ 0 offset 2px | = | button.button.button-primary 73.0x32.0 bg #455eed border T:1px #272b42 / R:1px #272b42 / B:1px #272b42 / L:1px #272b42 r 8px shadow #272b42 0px 0px 0px 1px outline 2px solid #000000 @ 0 offset 2px | button.button.button-primary 73.0x32.0 bg #374bbe border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up div.panel-header-side__not-logged-box bg #212121; 2 up div.panel-header-side__not-logged.sm:hidden shadow #000000 @ 0.06 0px 8px 17px 0px, #000000 @ 0.04 0px 31px 31px 0px, #000000 @ 0.02 0px 40px 42px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ed-signup-default.png`, `ed-signup-hover.png`, `ed-signup-focus-visible.png`, `ed-signup-pressed.png`.

#### ed-share

Share button. The "Share" button in the editor header; measured, never clicked.

Page: designer. Selector: `editor Share button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 60 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #434242 | = | = | 1px solid #455eed |
| Radius | 8px | = | = | = |
| Background | #212121 | = | = | #272b42 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Inter 12px/16px 500, #ffffff | = | = | = |
| Transition | none 0.3s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.group.transition-none 60.0x32.0 bg #212121 border T:1px #434242 / R:1px #434242 / B:1px #434242 / L:1px #434242 r 8px outline 2px solid #000000 @ 0 offset 2px | = | = | button.group.transition-none 60.0x32.0 bg #272b42 border T:1px #455eed / R:1px #455eed / B:1px #455eed / L:1px #455eed r 8px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ed-share-default.png`, `ed-share-hover.png`, `ed-share-focus-visible.png`, `ed-share-pressed.png`.

#### ed-download

Download button. The "Download" button in the editor header; measured, never clicked.

Page: designer. Selector: `editor Download button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 82 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #455eed | = | = | #475beb |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Inter 12px/16px 500, #ffffff | = | = | = |
| Transition | all 0.3s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.group.px-3 82.0x32.0 bg #455eed r 8px outline 2px solid #000000 @ 0 offset 2px | = | = | button.group.px-3 82.0x32.0 bg #475beb r 8px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ed-download-default.png`, `ed-download-hover.png`, `ed-download-focus-visible.png`, `ed-download-pressed.png`.

#### ed-zoom

Zoom control. The zoom-percentage dropdown trigger in the editor header; measured, never toggled.

Page: designer. Selector: `editor zoom trigger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 72 x 32 | = | = | = |
| Padding | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | #272b42 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 12px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | #455eed |
| Text node | span.text-button-2: Inter 12px/16px 500, #ffffff | = | = | = |
| Transition | none 0.3s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | 16 x 16, colour #455eed |
| Painted layers | button.p-2.dropdown__trigger 72.0x32.0 r 8px outline 2px solid #000000 @ 0 offset 2px | = | = | button.p-2.dropdown__trigger 72.0x32.0 bg #272b42 r 8px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ed-zoom-default.png`, `ed-zoom-hover.png`, `ed-zoom-focus-visible.png`, `ed-zoom-pressed.png`.

#### ed-tool

Tool rail button. A labelled tool-rail button (Text/Video/Elements…) on the editor's left rail — 48x48 .dropdown-toolbar buttons over a 20px icon; its flyout was never opened.

Page: designer. Selector: `.dropdown-toolbar tool`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #212121 | = | = | #272b42 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #a7a5a5 | = | = | = |
| Text node | p.text.group-hover:text-text-02: Inter 10px/16px 400, #a7a5a5 | = | = | p.text.group-hover:text-text-02: Inter 10px/16px 400, #ffffff |
| Transition | all 0.3s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #a7a5a5 | = | = | 20 x 20, colour #455eed |
| Painted layers | button.group.cursor-pointer 48.0x48.0 bg #212121 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px outline 2px solid #000000 @ 0 offset 2px | = | = | button.group.cursor-pointer 48.0x48.0 bg #272b42 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ed-tool-default.png`, `ed-tool-hover.png`, `ed-tool-focus-visible.png`, `ed-tool-pressed.png`.

#### ed-tool-active

Active tool button. The selected tool on the left rail (Pointer, marked dropdown--icon-active).

Page: designer. Selector: `.dropdown-toolbar.dropdown--icon-active`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 48 x 48 |
| Padding | 0px |
| Border | 1px solid #475beb |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #374bbe |
| Text node | p.text.group-hover:text-text-02: Inter 10px/16px 400, #ffffff |
| Transition | none |
| Cursor | pointer |
| Icon | 20 x 20, colour #455eed |
| Painted layers | div.dropdown--icon-active.dropdown-toolbar 48.0x48.0 border T:1px #475beb / R:1px #475beb / B:1px #475beb / L:1px #475beb r 8px; button.relative.js-tool-select 20.0x20.0 outline 2px solid #000000 @ 0 offset 2px; div.dropdown__menu.py-1 0.0x0.0 bg #212121 border T:1px #434242 / R:1px #434242 / B:1px #434242 / L:1px #434242 r 16px shadow #000000 @ 0.06 0px 8px 17px 0px, #000000 @ 0.04 0px 31px 31px 0px, #000000 @ 0.02 0px 40px 42px 0px; button.flex.justify-between 0.0x0.0 bg #212121 r 8px outline 2px solid #000000 @ 0 offset 2px; button.flex.justify-between 0.0x0.0 bg #212121 r 8px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `ed-tool-active-default.png`.

#### ed-inspector

Inspector panel. The right-hand inspector (.panel--inspector, ~280px): EDIT/LAYERS/PAGES tabs over the Page Background and Color controls.

Page: designer. Selector: `.panel--inspector`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 280 x 824 |
| Padding | 0px |
| Border | 1px solid #434242 |
| Radius | 12px |
| Background | #212121 |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span: Inter 11px/16px 600, #ffffff |
| Transition | all 0.3s linear |
| Cursor | url(…), default |
| Icon | 20 x 20, colour #ffffff |
| Painted layers | div.panel.panel-editor 280.0x824.0 bg #212121 border T:1px #434242 / R:1px #434242 / B:1px #434242 / L:1px #434242 r 12px; div.flex-shrink-0.border-b 278.0x41.0 border B:1px #434242; div.tab.rounded-[0px!important] 92.7x40.0 bg #212121; div::after.tab.rounded-[0px!important] 92.6719pxx2px bg #455eed; div.tab.rounded-[0px!important] 92.7x40.0 bg #212121; div::after.tab.rounded-[0px!important] 92.6562pxx2px bg #455eed |
| Ancestor paint | 1 up div.relative.page--editor bg #e6e6e6 |
| How | at rest |

Crops: `ed-inspector-default.png`.

#### ed-tab

Inspector tab. The EDIT inspector tab; opened was measured after switching to LAYERS — a local UI toggle.

Page: designer. Selector: `inspector EDIT tab`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 92.67 x 40 | = | - | = | = |
| Padding | 0px | = | - | = | = |
| Border | none | = | - | = | = |
| Radius | 0px | = | - | = | = |
| Background | #212121 | = | - | = | = |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | Inter 11px/16px 600 | = | - | = | = |
| Letter spacing | normal | = | - | = | = |
| Colour | #ffffff | = | - | = | = |
| Text node | span: Inter 11px/16px 600, #ffffff | = | - | = | = |
| Transition | none | = | - | = | = |
| Cursor | pointer | = | - | = | = |
| ::after | 92.6719px x 2px, absolute, bg #455eed, radius 0px | = | - | = | = |
| Painted layers | div.tab.rounded-[0px!important] 92.7x40.0 bg #212121; div::after.tab.rounded-[0px!important] 92.6719pxx2px bg #455eed | = | - | = | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | clicked the LAYERS inspector tab |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `ed-tab-default.png`, `ed-tab-pressed.png`, `ed-tab-opened.png`.

#### ed-tab-layers

Layers tab. The LAYERS inspector tab; measured at rest.

Page: designer. Selector: `inspector LAYERS tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 92.66 x 40 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | #212121 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 11px/16px 600 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Text node | span: Inter 11px/16px 600, #ffffff | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| ::after | 92.6562px x 2px, absolute, bg #455eed, radius 0px | = | - | = |
| Painted layers | div.tab.rounded-[0px!important] 92.7x40.0 bg #212121; div::after.tab.rounded-[0px!important] 92.6562pxx2px bg #455eed | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `ed-tab-layers-default.png`, `ed-tab-layers-hover.png`, `ed-tab-layers-pressed.png`.

#### ed-color

Inspector colour field. The page-background colour input in the inspector (the hex field, placeholder "000"); focused, never typed into.

Page: designer. Selector: `inspector colour input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 86 x 28 | = |
| Padding | 8px 4px 8px 26px | = |
| Border | 1px solid #434242 | = |
| Radius | 8px | = |
| Background | #323232 | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 12px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | background-color, border-color, color, fill, stroke 0.3s linear | = |
| Cursor | text | = |
| Placeholder | #868484, opacity 1 | = |
| Painted layers | input.pr-1.w-full 86.0x28.0 bg #323232 border T:1px #434242 / R:1px #434242 / B:1px #434242 / L:1px #434242 r 8px | input.pr-1.w-full 86.0x28.0 bg #323232 border T:1px #434242 / R:1px #434242 / B:1px #434242 / L:1px #434242 r 8px shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field |

Crops: `ed-color-default.png`, `ed-color-focused.png`.

#### ed-craft

Craft dialog. The "Craft Professional Assets" dialog (.modal__content): brand name, product description, the style grid, the image pane and "Add to canvas".

Page: designer. Selector: `craft dialog`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 792 x 640 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #212121 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 10px 0px |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.text-subtitle-2.font-semibold: Inter 12px/16px 600, #ffffff |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | url(…), default |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | div.modal__content.max-w-[792px] 792.0x640.0 bg #212121 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 10px 0px; div.w-full.pr-2 792.0x48.0 bg #212121 r 12px 12px 0px 0px; button.button-icon.group 32.0x32.0 r 8px outline 2px solid #000000 @ 0 offset 0px; div.flex.items-start 792.0x592.0 border T:1px #434242; textarea.h-8.overflow-hidden 307.6x32.0 bg #323232 border T:1px #434242 / R:1px #434242 / B:1px #434242 / L:1px #434242 r 8px; textarea.h-8.overflow-hidden 307.6x73.0 bg #323232 border T:1px #434242 / R:1px #434242 / B:1px #434242 / L:1px #434242 r 8px |
| How | at rest |

Crops: `ed-craft-default.png`.

#### ed-craft-field

Brand-name field. The "Enter your brand name" textarea in the Craft dialog; focused and typed into then cleared — never used.

Page: designer. Selector: `craft brand textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 307.59 x 32 | = | = |
| Padding | 8px 12px | = | = |
| Border | 1px solid #434242 | 1px solid #475beb | 1px solid #475beb |
| Radius | 8px | = | = |
| Background | #323232 | #272b42 | #272b42 |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 12px/16px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #868484, opacity 1 | = | = |
| Painted layers | textarea.h-8.overflow-hidden 307.6x32.0 bg #323232 border T:1px #434242 / R:1px #434242 / B:1px #434242 / L:1px #434242 r 8px | textarea.h-8.overflow-hidden 307.6x32.0 bg #272b42 border T:1px #475beb / R:1px #475beb / B:1px #475beb / L:1px #475beb r 8px shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | textarea.h-8.overflow-hidden 307.6x32.0 bg #272b42 border T:1px #475beb / R:1px #475beb / B:1px #475beb / L:1px #475beb r 8px shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "Example Brand", then deleted; nothing sent |

Crops: `ed-craft-field-default.png`, `ed-craft-field-focused.png`, `ed-craft-field-filled.png`.

#### ed-craft-area

Description area. The "Write a short description about your product" textarea; focused and typed into then cleared — never used.

Page: designer. Selector: `craft description textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 307.59 x 73 | = | = |
| Padding | 8px 12px | = | = |
| Border | 1px solid #434242 | 1px solid #475beb | 1px solid #475beb |
| Radius | 8px | = | = |
| Background | #323232 | #272b42 | #272b42 |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 12px/16px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #868484, opacity 1 | = | = |
| Painted layers | textarea.h-8.overflow-hidden 307.6x73.0 bg #323232 border T:1px #434242 / R:1px #434242 / B:1px #434242 / L:1px #434242 r 8px | textarea.h-8.overflow-hidden 307.6x73.0 bg #272b42 border T:1px #475beb / R:1px #475beb / B:1px #475beb / L:1px #475beb r 8px shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | textarea.h-8.overflow-hidden 307.6x73.0 bg #272b42 border T:1px #475beb / R:1px #475beb / B:1px #475beb / L:1px #475beb r 8px shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "A sample product description", then deleted; nothing sent |

Crops: `ed-craft-area-default.png`, `ed-craft-area-focused.png`, `ed-craft-area-filled.png`.

#### ed-craft-style

Style card. A style card in the Craft dialog grid (Modern); opened is the selected state after clicking it — a local UI toggle that enables "Add to canvas".

Page: designer. Selector: `craft style card`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 97.19 x 106 | = | - | = | = |
| Padding | 8px | = | - | = | = |
| Gap | 8px | = | - | = | = |
| Border | 1px solid #000000 @ 0 | = | - | = | 1px solid #b53d11 |
| Radius | 8px | = | - | = | = |
| Background | #3e261d | = | - | = | = |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | Inter 14px/20px 400 | = | - | = | = |
| Letter spacing | normal | = | - | = | = |
| Colour | #ffffff | = | - | = | = |
| Text node | p: Inter 12px/16px 400, #ffffff | = | - | = | = |
| Transition | all 0.25s linear | = | - | = | = |
| Cursor | url(…), default | = | - | = | = |
| Painted layers | div.card__select-style.retro 97.2x106.0 bg #3e261d border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px | = | - | = | div.card__select-style.retro 97.2x106.0 bg #3e261d border T:1px #b53d11 / R:1px #b53d11 / B:1px #b53d11 / L:1px #b53d11 r 8px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | clicked the "Modern" style card to enable "Add to canvas" — the button itself was never pressed |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `ed-craft-style-default.png`, `ed-craft-style-hover.png`, `ed-craft-style-pressed.png`, `ed-craft-style-opened.png`.

#### ed-add

Add to canvas. The Craft dialog's primary submit — disabled until a style is picked; `enabled` is the fill after the style click. The button itself was never pressed in this pass.

Page: designer. Selector: `craft Add to canvas`. States: default, hover, focus-visible, pressed, enabled.

| Property | default | hover | focus-visible | pressed | enabled |
|---|---|---|---|---|---|
| Size (w x h) | 424.41 x 40 | = | = | = | = |
| Padding | 8px 16px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #272b42 | = | = |
| Radius | 8px | = | = | = | = |
| Background | #455eed | #374bbe | = | #374bbe | = |
| Box shadow | none | = | #272b42 0px 0px 0px 1px | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = | = |
| Font | Inter 14px/20px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | = | = | = | = |
| Text node | span.text-button-2.text-light-100: Inter 12px/16px 500, #ffffff | = | = | = | = |
| Transition | all 0.25s linear | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | button.flex.button 424.4x40.0 bg #455eed border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px outline 2px solid #000000 @ 0 offset 2px | button.flex.button 424.4x40.0 bg #374bbe border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px outline 2px solid #000000 @ 0 offset 2px | button.flex.button 424.4x40.0 bg #455eed border T:1px #272b42 / R:1px #272b42 / B:1px #272b42 / L:1px #272b42 r 8px shadow #272b42 0px 0px 0px 1px outline 2px solid #000000 @ 0 offset 2px | button.flex.button 424.4x40.0 bg #374bbe border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px outline 2px solid #000000 @ 0 offset 2px | = |
| Ancestor paint | 3 up div.modal__content.max-w-[792px] bg #212121 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 10px 0px | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | clicked the "Modern" style card to enable "Add to canvas" — the button itself was never pressed |

Crops: `ed-add-default.png`, `ed-add-hover.png`, `ed-add-focus-visible.png`, `ed-add-pressed.png`, `ed-add-enabled.png`.

#### ed-replace

Replace image button. The "Replace" button on the Craft dialog's image pane; measured, never clicked.

Page: designer. Selector: `craft Replace button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 104 x 32 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #323232 | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #a7a5a5 | = | #a7a5a5 |
| Box shadow | none | = | #323232 0px 0px 0px 1px | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.text-button-2.text-light-100: Inter 12px/16px 500, #212121 | = | = | = |
| Transition | all 0.25s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #212121 | = | = | = |
| Painted layers | button.button.button-secondary 104.0x32.0 bg #ffffff border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px outline 2px solid #000000 @ 0 offset 2px | button.button.button-secondary 104.0x32.0 bg #a7a5a5 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px outline 2px solid #000000 @ 0 offset 2px | button.button.button-secondary 104.0x32.0 bg #ffffff border T:1px #323232 / R:1px #323232 / B:1px #323232 / L:1px #323232 r 8px shadow #323232 0px 0px 0px 1px outline 2px solid #000000 @ 0 offset 2px | button.button.button-secondary 104.0x32.0 bg #a7a5a5 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ed-replace-default.png`, `ed-replace-hover.png`, `ed-replace-focus-visible.png`, `ed-replace-pressed.png`.

#### ed-close

Dialog close. The Craft dialog's own close button; measured, never clicked.

Page: designer. Selector: `.modal__close inside craft dialog`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | #434242 | #434242 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | 2px solid #646363 offset 0px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.25s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| Painted layers | button.button-icon.group 32.0x32.0 r 8px outline 2px solid #000000 @ 0 offset 0px | = | button.button-icon.group 32.0x32.0 bg #434242 r 8px outline 2px solid #646363 offset 0px | button.button-icon.group 32.0x32.0 bg #434242 r 8px outline 2px solid #000000 @ 0 offset 0px |
| Ancestor paint | 3 up div.modal__content.max-w-[792px] bg #212121 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 10px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ed-close-default.png`, `ed-close-hover.png`, `ed-close-focus-visible.png`, `ed-close-pressed.png`.

### Mobile (390 wide)

#### m-topbar

Mobile top bar. The phone header at 390 wide: wordmark, the burger and the actions that survive the width.

Page: mobile. Selector: `mobile top nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 64 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | #111111 |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | strong.framer-text: Inter 9px/10.8px 700, #fff9f3 |
| Transition | none |
| Icon | 75 x 24, colour #0000ee, fill #000000 |
| Painted layers | div.framer-165vwyy 390.0x64.0 bg #111111; nav.framer-1zja2.framer-Ju3FI 390.0x64.0 bg #ffffff; nav::after.framer-1zja2.framer-Ju3FI 390pxx64px border B:1px #e5e0db; a.framer-1pxcn6y.framer-1v7amdl 97.0x23.6 bg #111111 r 2px; div.framer-17rl7jd 20.0x2.0 bg #404040 r 10px; div.framer-c8jx7r 20.0x2.0 bg #404040 r 10px |
| Ancestor paint | 1 up div.framer-2po4Y.framer-8uwo3 bg #ffffff |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-burger

Mobile burger. The nav burger at 390 wide (the 60x60 "Menu Icon" — the overlay it opens is the [data-framer-name="Menu"] panel); opened was measured after tapping it.

Page: mobile. Selector: `[data-framer-name="Menu Icon"]`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 60 x 60 | = | - | = | = |
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
| Painted layers | div.framer-17rl7jd 20.0x2.0 bg #404040 r 10px; div.framer-c8jx7r 20.0x2.0 bg #404040 r 10px | = | - | = | div.framer-17rl7jd 15.6x15.6 bg #404040 r 50% / 500%; div.framer-c8jx7r 15.6x15.6 bg #404040 r 50% / 500% |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | tapped the nav "Menu Icon" to open the mobile menu |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |
| Cursor | - | = | = | = | pointer |

Crops: `m-burger-default.png`, `m-burger-hover.png`, `m-burger-pressed.png`, `m-burger-opened.png`.

#### m-menu-link

Mobile menu link. A link inside the opened mobile nav menu.

Page: mobile. Selector: `mobile menu link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 75 x 24 |
| Padding | 0px |
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
| Icon | 75 x 24, colour #0000ee, fill #000000 |
| How | at rest |

Crops: `m-menu-link-default.png`.

#### m-hero-h1

Mobile hero headline. The hero display heading at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 172.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PolySans Trial Median 36px/43.2px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span: PolySans Trial Median 36px/43.2px 400, #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-hero-cta

Mobile hero CTA. The hero action at 390 wide — the same outlined ghost as desktop, centred under the hero copy (the DOM-first "Play for free" is the menu overlay's full-width filled button, so the leaf text is tagged in-page). Measured, never followed.

Page: mobile. Selector: `mobile hero CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 119.41 x 46 | = | = | = |
| Padding | 14px 18px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1126out: Inter 14px/14px 500, #ffffff, ls -0.2px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 119.406px x 46px, absolute, bg #000000 @ 0, radius 8px | = | = | = |
| Painted layers | a::after.framer-13l81z2.framer-19c9wqe 119.406pxx46px border T:1px #455eed / R:1px #455eed / B:1px #455eed / L:1px #455eed r 8px | = | a.framer-13l81z2.framer-19c9wqe 119.4x46.0 r 8px outline 1px auto #101010 offset 1px; a::after.framer-13l81z2.framer-19c9wqe 119.406pxx46px border T:1px #455eed / R:1px #455eed / B:1px #455eed / L:1px #455eed r 8px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | = |

Crops: `m-hero-cta-default.png`, `m-hero-cta-hover.png`, `m-hero-cta-focus-visible.png`, `m-hero-cta-pressed.png`.

## Transitions declared in the readable stylesheets

glorify.com serves its CSS same-origin-readable (the Framer bundle plus inline blocks; app.glorify.com serves its own sheets), so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- designer: `opacity 0.2s linear`, `opacity linear`, `0.25s linear`, `0.2s`, `0.5s linear`, `max-height 0.4s`, `1s`, `box-shadow, background 0.3s`, `width 0.2s ease-in-out`, `max-width 150ms ease-in-out`, `0.3s linear`, `color 0.1s ease-out`

- feature: `color 0.3s cubic-bezier(0.44, 0, 0.56, 1)`, `visibility 0.2s linear, opacity`, `box-shadow 0.2s linear, -webkit-box-shadow`, `height 350ms cubic-bezier(0.25, 0.1, 0, 1), width, max-width, max-height, top, bottom, left, right, transform, -webkit-transform`, `none`, `opacity 0.4s ease-out`, `unset`

- home: `color 0.3s cubic-bezier(0.44, 0, 0.56, 1)`, `visibility 0.2s linear, opacity`, `box-shadow 0.2s linear, -webkit-box-shadow`, `height 350ms cubic-bezier(0.25, 0.1, 0, 1), width, max-width, max-height, top, bottom, left, right, transform, -webkit-transform`, `none`, `opacity 0.4s ease-out`, `unset`

- login: `background-color 600000s, color 600000s`, `stroke-dashoffset 0.5s`, `opacity 0.2s linear`, `opacity linear`, `0.25s linear`, `0.2s`, `0.5s linear`, `none`, `opacity 0.1s, z-index, visibility`, `opacity 0.2s, padding 0.2s`, `1.5s`

- pricing: `color 0.3s cubic-bezier(0.44, 0, 0.56, 1)`, `visibility 0.2s linear, opacity`, `box-shadow 0.2s linear, -webkit-box-shadow`, `height 350ms cubic-bezier(0.25, 0.1, 0, 1), width, max-width, max-height, top, bottom, left, right, transform, -webkit-transform`, `none`, `opacity 0.4s ease-out`, `unset`

## Reduced motion

- home (`[data-framer-name="Top nav"] a, header a` under prefers-reduced-motion): transition `all`, animation `none`, html scroll-behavior `auto`
