# FlowMapp component measurements

Computed styles read from www.flowmapp.com and app.flowmapp.com on 2026-11-15 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the public surfaces — the light-only Webflow marketing pages, the signed-out /signin, /signup and /restore forms of the app, and the published read-only demo project at /share/projects/215285 (the sitemap and user-flow viewers the marketing "Try Demo Project" link opens) — with any consent layer hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Site chrome

#### mkt-header

Site header. The marketing top bar: wordmark, "Try Demo Project", Features and Use cases dropdowns, Pricing, Help, Blog, "Log in" and the "Try for free" pill.

Page: home. Selector: `header / .navbar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1416 x 82.06 |
| Padding | 12px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div: Inter 16px/22.4px undefined, #000000, ls -0.64px |
| Transition | none |
| Icon | 16 x 16, colour #ffffff |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | div.container.nav-cont__is-br-12--is-sh-img 1416.0x70.1 bg #ffffff @ 0.8 r 12px shadow #787c84 @ 0.19 -9.92904px 11.043px 59.7576px 0px; div.nav__link-underline 121.8x23.4 border B:1px #8c9baa; div.nav__pop.is-sh-l--is-bg-wh--is-br-12--is-t-sh-0 377.0x490.5 bg #ffffff r 12px shadow #97a9bb @ 0.58 0px 8px 10px 0px; div.nav__pop.is-sh-l--is-bg-wh--is-br-12--is-t-sh-0 377.0x512.9 bg #ffffff r 12px shadow #97a9bb @ 0.58 0px 8px 10px 0px; a.nav__btn.is-bc-gray__is-br-12--is-mob-hide 77.2x38.5 border T:1px #000000 @ 0.1 / R:1px #000000 @ 0.1 / B:1px #000000 @ 0.1 / L:1px #000000 @ 0.1 r 12px; a.nav__btn.is-bg-black--is-br-12--is-t-wh 127.3x38.5 bg #000000 border T:1px #000000 / R:1px #000000 / B:1px #000000 / L:1px #000000 r 12px |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The FlowMapp wordmark in the header, linking home.

Page: home. Selector: `header first a`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 136.95 x 32.98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 1 up div.container.nav-cont__is-br-12--is-sh-img bg #ffffff @ 0.8 shadow #787c84 @ 0.19 -9.92904px 11.043px 59.7576px 0px |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-link

Nav link. A marketing header nav link (Pricing); measured, never followed.

Page: home. Selector: `.nav__link Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 76.69 x 44.47 | = | = | = |
| Padding | 11.04px 14.08px | = | = | = |
| Gap | normal 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f6f8fa | = | #f6f8fa |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/22.4px 600 | = | = | = |
| Letter spacing | -0.64px | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | background-color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 3 up div.container.nav-cont__is-br-12--is-sh-img bg #ffffff @ 0.8 shadow #787c84 @ 0.19 -9.92904px 11.043px 59.7576px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.nav__link.is-br-8 76.7x44.5 bg #f6f8fa r 8px | = | a.nav__link.is-br-8 76.7x44.5 bg #f6f8fa r 8px |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-features

Features nav trigger. The "Features" nav item that opens the .nav__pop-wrap flyout on hover (Sitemap, User flow, Wireframes, Content, Estimation & invoice…).

Page: home. Selector: `nav Features trigger`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 109.05 x 44.47 | = | - | = | = |
| Padding | 11.04px 14.08px | = | - | = | = |
| Gap | normal 4px | = | - | = | = |
| Border | none | = | - | = | = |
| Radius | 8px | = | - | = | = |
| Background | transparent | #f6f8fa | - | #f6f8fa | = |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | Inter 16px/22.4px 600 | = | - | = | = |
| Letter spacing | -0.64px | = | - | = | = |
| Colour | #000000 | = | - | = | = |
| Text node | div: Inter 16px/22.4px undefined, #000000, ls -0.64px | = | - | = | = |
| Transition | background-color 0.3s ease | = | - | = | = |
| Cursor | pointer | = | - | = | = |
| Painted layers | div.nav__pop.is-sh-l--is-bg-wh--is-br-12--is-t-sh-0 377.0x490.5 bg #ffffff r 12px shadow #97a9bb @ 0.58 0px 8px 10px 0px | div.nav__link.pop__is-br-8 109.0x44.5 bg #f6f8fa r 8px; div.nav__pop.is-sh-l--is-bg-wh--is-br-12--is-t-sh-0 377.0x490.5 bg #ffffff r 12px shadow #97a9bb @ 0.58 0px 8px 10px 0px | - | div.nav__link.pop__is-br-8 109.0x44.5 bg #f6f8fa r 8px; div.nav__pop.is-sh-l--is-bg-wh--is-br-12--is-t-sh-0 377.0x490.5 bg #ffffff r 12px shadow #97a9bb @ 0.58 0px 8px 10px 0px | = |
| Ancestor paint | 3 up div.container.nav-cont__is-br-12--is-sh-img bg #ffffff @ 0.8 shadow #787c84 @ 0.19 -9.92904px 11.043px 59.7576px 0px | = | - | = | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | the Features flyout was already open |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `nav-features-default.png`, `nav-features-hover.png`, `nav-features-pressed.png`, `nav-features-opened.png`.

#### nav-pop-item

Features flyout item. A row inside the opened Features flyout (icon, name, one-line description); measured while the flyout was held open by hover.

Page: home. Selector: `.nav__pop-link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 353 x 93.3 |
| Padding | 12px |
| Gap | normal 16px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/22.4px 600 |
| Letter spacing | -0.64px |
| Colour | #000000 |
| Transition | background-color 0.3s ease |
| Cursor | pointer |
| Ancestor paint | 1 up div.nav__pop.is-sh-l--is-bg-wh--is-br-12--is-t-sh-0 bg #ffffff shadow #97a9bb @ 0.58 0px 8px 10px 0px |
| How | at rest |

Crops: `nav-pop-item-default.png`.

#### nav-demo

Try Demo Project link. The header link to the published read-only demo project on app.flowmapp.com; measured, never followed.

Page: home. Selector: `header Try Demo Project`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 177.92 x 46.06 | = | = | = |
| Padding | 11.04px 14.08px | = | = | = |
| Gap | normal 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f6f8fa | = | #f6f8fa |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/22.4px 600 | = | = | = |
| Letter spacing | -0.64px | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div: Inter 16px/22.4px undefined, #000000, ls -0.64px | = | = | = |
| Transition | background-color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.nav__link-underline 121.8x23.4 border B:1px #8c9baa | a.nav__link.is-br-8 177.9x46.1 bg #f6f8fa r 8px; div.nav__link-underline 121.8x23.4 border B:1px #8c9baa | = | a.nav__link.is-br-8 177.9x46.1 bg #f6f8fa r 8px; div.nav__link-underline 121.8x23.4 border B:1px #8c9baa |
| Ancestor paint | 3 up div.container.nav-cont__is-br-12--is-sh-img bg #ffffff @ 0.8 shadow #787c84 @ 0.19 -9.92904px 11.043px 59.7576px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-demo-default.png`, `nav-demo-hover.png`, `nav-demo-focus-visible.png`, `nav-demo-pressed.png`.

#### nav-login

Log in link. The "Log in" nav action to app.flowmapp.com/signin; measured, never followed.

Page: home. Selector: `header Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 77.17 x 38.47 | = | = | = |
| Padding | 7.04px 16px | = | = | = |
| Gap | normal 5.92px | = | = | = |
| Border | 1px solid #000000 @ 0.1 | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #000000 | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/22.4px 600 | = | = | = |
| Letter spacing | -0.64px | = | = | = |
| Colour | #000000 | #ffffff | = | #ffffff |
| Text node | div: Inter 16px/22.4px undefined, #000000, ls -0.64px | div: Inter 16px/22.4px undefined, #ffffff, ls -0.64px | = | div: Inter 16px/22.4px undefined, #ffffff, ls -0.64px |
| Transition | color, background-color 0.3s, 0.3s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.nav__btn.is-bc-gray__is-br-12--is-mob-hide 77.2x38.5 border T:1px #000000 @ 0.1 / R:1px #000000 @ 0.1 / B:1px #000000 @ 0.1 / L:1px #000000 @ 0.1 r 12px | a.nav__btn.is-bc-gray__is-br-12--is-mob-hide 77.2x38.5 bg #000000 border T:1px #000000 @ 0.1 / R:1px #000000 @ 0.1 / B:1px #000000 @ 0.1 / L:1px #000000 @ 0.1 r 12px | = | a.nav__btn.is-bc-gray__is-br-12--is-mob-hide 77.2x38.5 bg #000000 border T:1px #000000 @ 0.1 / R:1px #000000 @ 0.1 / B:1px #000000 @ 0.1 / L:1px #000000 @ 0.1 r 12px |
| Ancestor paint | 3 up div.container.nav-cont__is-br-12--is-sh-img bg #ffffff @ 0.8 shadow #787c84 @ 0.19 -9.92904px 11.043px 59.7576px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-cta

Try for free pill. The black "Try for free" header pill to app.flowmapp.com/signup; measured, never followed.

Page: home. Selector: `header Try for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 127.31 x 38.47 | = | = | = |
| Padding | 7.04px 10.08px 7.04px 16px | = | = | = |
| Gap | normal 5.92px | = | = | = |
| Border | 1px solid #000000 | 1px solid #cbd8e5 | = | 1px solid #cbd8e5 |
| Radius | 12px | = | = | = |
| Background | #000000 | transparent | = | transparent |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/22.4px 600 | = | = | = |
| Letter spacing | -0.64px | = | = | = |
| Colour | #ffffff | #000000 | = | #000000 |
| Text node | div: Inter 16px/22.4px undefined, #ffffff, ls -0.64px | div: Inter 16px/22.4px undefined, #000000, ls -0.64px | = | div: Inter 16px/22.4px undefined, #000000, ls -0.64px |
| Transition | border-color, color, background-color 0.3s, 0.3s, 0.3s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| Painted layers | a.nav__btn.is-bg-black--is-br-12--is-t-wh 127.3x38.5 bg #000000 border T:1px #000000 / R:1px #000000 / B:1px #000000 / L:1px #000000 r 12px | a.nav__btn.is-bg-black--is-br-12--is-t-wh 127.3x38.5 border T:1px #cbd8e5 / R:1px #cbd8e5 / B:1px #cbd8e5 / L:1px #cbd8e5 r 12px | = | a.nav__btn.is-bg-black--is-br-12--is-t-wh 127.3x38.5 border T:1px #cbd8e5 / R:1px #cbd8e5 / B:1px #cbd8e5 / L:1px #cbd8e5 r 12px |
| Ancestor paint | 3 up div.container.nav-cont__is-br-12--is-sh-img bg #ffffff @ 0.8 shadow #787c84 @ 0.19 -9.92904px 11.043px 59.7576px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### hero-eyebrow

Hero eyebrow. The "Over 400,000 users" trust line above the hero heading.

Page: home. Selector: `hero trust line`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 237 x 16.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 12px/16.8px 500 |
| Letter spacing | -0.64px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `hero-eyebrow-default.png`.

#### hero-h1

Hero headline. "Visual platform for planning UX and pitching web design" — the display heading.

Page: home. Selector: `home h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 216 |
| Padding | 0px 240px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 72px/72px 700 |
| Letter spacing | -2.16px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-cta

Hero CTA. The hero "Start planning" button (blue pill with the squiggle arrow); measured, never followed.

Page: home. Selector: `hero Start planning`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 477.91 x 120.06 | = | = | = |
| Padding | 12px | = | = | = |
| Gap | normal 13.92px | = | = | = |
| Border | none | = | = | = |
| Radius | 1600px | = | = | = |
| Background | #0080ff @ 0.2 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 30px/42px 600 | = | = | = |
| Letter spacing | -0.9px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.text-block-10: Inter 30px/42px undefined, #ffffff, ls -0.9px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 97.59 x 20.53, colour #ffffff, fill #000000 | = | = | = |
| Painted layers | a.btn.w-inline-block 477.9x120.1 bg #0080ff @ 0.2 r 1600px; div.btn__wrapper 453.9x96.1 bg #0080ff r 1600px shadow #0080ff @ 0.34 0px 8px 10px 0px | a.btn.w-inline-block 477.9x120.1 bg #0080ff @ 0.2 r 1600px; div.btn__wrapper 453.9x96.1 bg #006aff r 1600px shadow #0080ff @ 0.34 0px 8px 10px 0px | = | a.btn.w-inline-block 477.9x120.1 bg #0080ff @ 0.2 r 1600px; div.btn__wrapper 453.9x96.1 bg #006aff r 1600px shadow #0080ff @ 0.34 0px 8px 10px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-avatars

Avatar cluster. The stacked-user avatar cluster beside the trust line.

Page: home. Selector: `.ava-container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 237 x 34 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Painted layers | img.ava-main-1 34.0x34.0 border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 1600px; img.ava-main 34.0x34.0 border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 1600px; img.ava-main 34.0x34.0 border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 1600px; img.ava-main 34.0x34.0 border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 1600px; img.ava-main 34.0x34.0 border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 1600px; img.ava-main 34.0x34.0 border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 1600px |
| How | at rest |

Crops: `hero-avatars-default.png`.

#### trusted-mark

Client mark. One of the "Win more clients" brand marks under the hero CTA (Webflow, Framer, WordPress…).

Page: home. Selector: `home client logos`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 141.42 x 31.14 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `trusted-mark-default.png`.

#### home-h2

Section heading. A section heading on the marketing home.

Page: home. Selector: `home h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 72px/72px 700 |
| Letter spacing | -2.16px |
| Colour | #000000 |
| Text node | span.text-72-pivot: Inter 72px/72px undefined, #000000, ls -2.16px |
| Transition | none |
| How | at rest |

Crops: `home-h2-default.png`.

#### home-prose

Body paragraph. A body paragraph on the marketing home.

Page: home. Selector: `home p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 57.53 x 22.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/22.4px 600 |
| Letter spacing | -0.64px |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 3 up div.nav__pop.is-sh-l--is-bg-wh--is-br-12--is-t-sh-0 bg #ffffff shadow #97a9bb @ 0.58 0px 8px 10px 0px |
| How | at rest |

Crops: `home-prose-default.png`.

#### home-card

Home card. A feature/benefit card on the marketing home.

Page: home. Selector: `home [class*=card]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 386.66 x 518 | = |
| Padding | 24px | = |
| Border | 3px solid #0050ff | = |
| Radius | 32px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | 3px solid #0080ff @ 0.2 offset 0px | = |
| Font | Inter 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | p.text-30-b: Inter 30px/42px undefined, #000000, ls -0.9px | = |
| Transition | none | = |
| Painted layers | div.usecase_card 386.7x518.0 border T:3px #0050ff / R:3px #0050ff / B:3px #0050ff / L:3px #0050ff r 32px outline 3px solid #0080ff @ 0.2 offset 0px | = |
| How | at rest | mouse hover |

Crops: `home-card-default.png`, `home-card-hover.png`.

### Pricing

#### ptab-monthly

Billing tab (monthly). The "Billed monthly" toggle in the pricing switcher; opened is the selected state after clicking (a local UI toggle).

Page: pricing. Selector: `.p-tabs__btn monthly`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 330 x 59.91 | = | = | = | = |
| Padding | 16px 19.2px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 1600px | = | = | = | = |
| Background | #ffffff | = | = | = | #0080ff |
| Box shadow | none | = | = | = | #0080ff @ 0.34 0px 8px 10px 0px |
| Outline | none | = | = | = | = |
| Font | Inter 14px/20px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #222222 | = | = | = | #ffffff |
| Text node | div.text-36-b-pr.m-text-18-sb: Inter 25.6px/27.904px undefined, #222222, ls -0.72px | = | = | = | div.text-36-b-pr.m-text-18-sb: Inter 25.6px/27.904px undefined, #ffffff, ls -0.72px |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | a.p-tabs__btn.w-inline-block 330.0x59.9 bg #ffffff r 1600px | = | = | = | a.p-tabs__btn.w-inline-block 330.0x59.9 bg #0080ff r 1600px shadow #0080ff @ 0.34 0px 8px 10px 0px |
| Ancestor paint | 1 up div.p-tabs__menu.w-tab-menu bg #ffffff | = | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover | clicked "Billed monthly" to select monthly prices |

Crops: `ptab-monthly-default.png`, `ptab-monthly-hover.png`, `ptab-monthly-focus-visible.png`, `ptab-monthly-pressed.png`, `ptab-monthly-opened.png`.

#### ptab-annual

Billing tab (annual). The "Billed annually" toggle carrying the "45% off" badge.

Page: pricing. Selector: `.p-tabs__btn annual`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 330 x 59.91 | = | = | = |
| Padding | 16px 19.2px | = | = | = |
| Border | none | = | = | = |
| Radius | 1600px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | div.text-36-b-pr.m-text-18-sb: Inter 25.6px/27.904px undefined, #222222, ls -0.72px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.p-tabs__btn.is-rel 330.0x59.9 bg #ffffff r 1600px; div.p-tabs__tag 99.3x42.2 bg #99dd2c r 1600px | = | = | = |
| Ancestor paint | 1 up div.p-tabs__menu.w-tab-menu bg #ffffff | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `ptab-annual-default.png`, `ptab-annual-hover.png`, `ptab-annual-focus-visible.png`, `ptab-annual-pressed.png`.

#### plan-card

Plan card. A pricing plan card (Free: $0 forever, features list, CTA).

Page: pricing. Selector: `.p-tabs__card:first`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 305 x 435.09 |
| Padding | 24px |
| Gap | 36px normal |
| Border | none |
| Radius | 24px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.text-36-b: Inter 36px/39.24px undefined, #000000, ls -0.72px |
| Transition | none |
| Painted layers | div.p-tabs__card.is-br-24 305.0x435.1 bg #ffffff r 24px; a.btn-s.w-inline-block 257.0x75.7 bg #0080ff @ 0.2 r 1600px; div.p-tabs__btn-bl 245.0x63.7 bg #0080ff r 1600px shadow #0080ff @ 0.34 0px 8px 10px 0px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-card-paid

Paid plan card. A paid pricing card ($35/mo monthly, $19.25/mo annual); hover is a pointer hover, never clicked through.

Page: pricing. Selector: `.p-tabs__card paid`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 305 x 435.09 | = |
| Padding | 24px | = |
| Gap | 36px normal | = |
| Border | none | = |
| Radius | 24px | = |
| Background | #000000 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h3.text-36-b: Inter 36px/39.24px undefined, #ffffff, ls -0.72px | = |
| Transition | none | = |
| Painted layers | div.p-tabs__card.is-bg-black--is-br-24 305.0x435.1 bg #000000 r 24px; a.btn-s.w-inline-block 257.0x75.7 bg #0080ff @ 0.2 r 1600px; div.p-tabs__btn-bl 245.0x63.7 bg #0080ff r 1600px shadow #0080ff @ 0.34 0px 8px 10px 0px | = |
| How | at rest | mouse hover |

Crops: `plan-card-paid-default.png`, `plan-card-paid-hover.png`.

#### plan-price

Plan price. The price block inside a plan card.

Page: pricing. Selector: `.p-tabs__card price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 257 x 31.39 |
| Padding | 0px |
| Gap | normal 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.text-36-b-pr: Inter 28.8px/31.392px undefined, #000000, ls -0.72px |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. A plan card's action button/link; its states were measured but it was never followed — no checkout.

Page: pricing. Selector: `.p-tabs__card action`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 257 x 75.66 | = | = | = |
| Padding | 6px | = | = | = |
| Gap | normal 13.92px | = | = | = |
| Border | none | = | = | = |
| Radius | 1600px | = | = | = |
| Background | #0080ff @ 0.2 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 24px/33.6px 700 | = | = | = |
| Letter spacing | -0.72px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div: Inter 24px/33.6px undefined, #ffffff, ls -0.72px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn-s.w-inline-block 257.0x75.7 bg #0080ff @ 0.2 r 1600px; div.p-tabs__btn-bl 245.0x63.7 bg #0080ff r 1600px shadow #0080ff @ 0.34 0px 8px 10px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-row

Plan feature row. A feature row inside a plan card.

Page: pricing. Selector: `.p-tabs__card feature row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 80.25 x 22.41 |
| Padding | 0px |
| Gap | normal 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.is-t-gr: Inter 16px/22.4px undefined, #8c9baa, ls -0.64px |
| Transition | none |
| How | at rest |

Crops: `plan-row-default.png`.

#### faq-q

FAQ disclosure. A pricing FAQ disclosure row ("Can I cancel a subscription at any time?"); opened was measured after clicking it (a local UI toggle).

Page: pricing. Selector: `.faq__q-wrap`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 730 x 69 | = | - | = | 730 x 159.41 |
| Padding | 0px | = | - | = | = |
| Border | T: none; R: none; B: 1px solid #cbd8e5; L: none | = | - | = | = |
| Radius | 0px | = | - | = | = |
| Background | transparent | = | - | = | = |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | Inter 14px/20px 400 | = | - | = | = |
| Letter spacing | normal | = | - | = | = |
| Colour | #000000 | = | - | = | = |
| Text node | div.text-20-sb.is-t-gr: Inter 20px/28px undefined, #8c9baa, ls -0.8px | = | - | = | = |
| Transition | none | = | - | = | = |
| Cursor | pointer | = | - | = | = |
| Painted layers | div.faq__item.slide-in 730.0x69.0 border B:1px #cbd8e5 | = | - | = | div.faq__item.slide-in 730.0x159.4 border B:1px #cbd8e5 |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | clicked the FAQ row to expand its answer |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `faq-q-default.png`, `faq-q-hover.png`, `faq-q-pressed.png`, `faq-q-opened.png`.

#### faq-a

FAQ answer. An expanded pricing FAQ answer paragraph.

Page: pricing. Selector: `faq answer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 730 x 159.41 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #cbd8e5; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.text-20-sb.is-t-gr: Inter 20px/28px undefined, #8c9baa, ls -0.8px |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.faq__item.slide-in 730.0x159.4 border B:1px #cbd8e5 |
| How | at rest |

Crops: `faq-a-default.png`.

### Feature page

#### feat-h1

Feature headline. The /features/sitemap page heading.

Page: feature. Selector: `feature h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 366.84 x 99.84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 96px/99.84px 700 |
| Letter spacing | -2.88px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `feat-h1-default.png`.

#### feat-cta

Feature CTA. The feature page's primary action; measured, never followed.

Page: feature. Selector: `feature CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 127.31 x 38.47 | = | = | = |
| Padding | 7.04px 10.08px 7.04px 16px | = | = | = |
| Gap | normal 5.92px | = | = | = |
| Border | 1px solid #000000 | 1px solid #cbd8e5 | = | 1px solid #cbd8e5 |
| Radius | 12px | = | = | = |
| Background | #000000 | transparent | = | transparent |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/22.4px 600 | = | = | = |
| Letter spacing | -0.64px | = | = | = |
| Colour | #ffffff | #000000 | = | #000000 |
| Text node | div: Inter 16px/22.4px undefined, #ffffff, ls -0.64px | div: Inter 16px/22.4px undefined, #000000, ls -0.64px | = | div: Inter 16px/22.4px undefined, #000000, ls -0.64px |
| Transition | border-color, color, background-color 0.3s, 0.3s, 0.3s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| Painted layers | a.nav__btn.is-bg-black--is-br-12--is-t-wh 127.3x38.5 bg #000000 border T:1px #000000 / R:1px #000000 / B:1px #000000 / L:1px #000000 r 12px | a.nav__btn.is-bg-black--is-br-12--is-t-wh 127.3x38.5 border T:1px #cbd8e5 / R:1px #cbd8e5 / B:1px #cbd8e5 / L:1px #cbd8e5 r 12px | = | a.nav__btn.is-bg-black--is-br-12--is-t-wh 127.3x38.5 border T:1px #cbd8e5 / R:1px #cbd8e5 / B:1px #cbd8e5 / L:1px #cbd8e5 r 12px |
| Ancestor paint | 3 up div.container.nav-cont__is-br-12--is-sh-img bg #ffffff @ 0.8 shadow #787c84 @ 0.19 -9.92904px 11.043px 59.7576px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `feat-cta-default.png`, `feat-cta-hover.png`, `feat-cta-focus-visible.png`, `feat-cta-pressed.png`.

#### feat-card

Feature card. A capability card on the sitemap feature page.

Page: feature. Selector: `feature [class*=card]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1060 x 776.88 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | p.text-16-sb: Inter 16px/22.4px undefined, #000000, ls -0.24px | = |
| Transition | none | = |
| Painted layers | div.f-tools__card.is-br-32--slide-in 340.0x179.2 bg #ffffff r 32px; div.f-tools__card.is-br-32--slide-in 340.0x179.2 bg #ffffff r 32px; div.f-tools__card.is-br-32--slide-in 340.0x179.2 bg #ffffff r 32px; div.f-tools__card.is-br-32--slide-in 340.0x179.2 bg #ffffff r 32px; div.f-tools__card.is-br-32--slide-in 340.0x179.2 bg #ffffff r 32px; div.f-tools__card.is-br-32--slide-in 340.0x179.2 bg #ffffff r 32px | = |
| How | at rest | mouse hover |

Crops: `feat-card-hover.png`.

#### feat-prose

Feature paragraph. A body paragraph on the feature page.

Page: feature. Selector: `feature p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 57.53 x 22.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/22.4px 600 |
| Letter spacing | -0.64px |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 3 up div.nav__pop.is-sh-l--is-bg-wh--is-br-12--is-t-sh-0 bg #ffffff shadow #97a9bb @ 0.58 0px 8px 10px 0px |
| How | at rest |

Crops: `feat-prose-default.png`.

### Contact

#### contact-h1

Contact headline. The contact page heading.

Page: contact. Selector: `contact h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 730 x 99.84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 96px/99.84px 700 |
| Letter spacing | -2.88px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `contact-h1-default.png`.

#### contact-field

Contact field. A text input in the contact form; focused and typed into then cleared — the form was never submitted.

Page: contact. Selector: `contact input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 492 x 50.08 | = | = |
| Padding | 8px 0px | = | = |
| Border | T: none; R: none; B: 2px solid #cbd8e5; L: none | T: none; R: none; B: 2px solid #3898ec; L: none | T: none; R: none; B: 2px solid #3898ec; L: none |
| Radius | 0px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 20px/28.5714px 400 | = | = |
| Letter spacing | -0.8px | = | = |
| Colour | #333333 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000, opacity 1 | = | = |
| Painted layers | input.form__field.text-20-r 492.0x50.1 bg #ffffff border B:2px #cbd8e5 | input.form__field.text-20-r 492.0x50.1 bg #ffffff border B:2px #3898ec | input.form__field.text-20-r 492.0x50.1 bg #ffffff border B:2px #3898ec |
| How | at rest | clicked into the field | typed "Example name", then deleted; nothing sent |

Crops: `contact-field-default.png`, `contact-field-focused.png`, `contact-field-filled.png`.

#### contact-area

Contact message area. The message textarea; focused and typed into then cleared — never sent.

Page: contact. Selector: `contact textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 492 x 50.08 | = | = |
| Padding | 8px 0px | = | = |
| Border | T: none; R: none; B: 2px solid #cbd8e5; L: none | T: none; R: none; B: 2px solid #3898ec; L: none | T: none; R: none; B: 2px solid #3898ec; L: none |
| Radius | 0px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 20px/28.5714px 400 | = | = |
| Letter spacing | -0.8px | = | = |
| Colour | #333333 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000, opacity 1 | = | = |
| Painted layers | input.form__field.text-20-r 492.0x50.1 bg #ffffff border B:2px #cbd8e5 | input.form__field.text-20-r 492.0x50.1 bg #ffffff border B:2px #3898ec | input.form__field.text-20-r 492.0x50.1 bg #ffffff border B:2px #3898ec |
| How | at rest | clicked into the field | typed "Hello", then deleted; nothing sent |

Crops: `contact-area-default.png`, `contact-area-focused.png`, `contact-area-filled.png`.

#### contact-submit

Contact submit. The contact form's send button; its states were measured but it was never clicked — nothing was sent.

Page: contact. Selector: `contact submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 337.05 x 75.66 | = | = | = |
| Padding | 9px 15px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Placeholder | #000000 @ 0, opacity 1 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `contact-submit-default.png`, `contact-submit-hover.png`, `contact-submit-focus-visible.png`, `contact-submit-pressed.png`.

### App sign-in

#### login-h1

Sign-in headline. The app sign-in heading on app.flowmapp.com/signin.

Page: login. Selector: `signin heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 61.2 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/24px 500 |
| Letter spacing | -0.4px |
| Colour | #1f1f1f |
| Transition | none |
| How | at rest |

Crops: `login-h1-default.png`.

#### login-card

Sign-in card. The sign-in form card — e-mail and password fields, the primary submit and OAuth buttons.

Page: login. Selector: `signin form/card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 440 x 640 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/16.1px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.hello--c8QkQ: Inter 32px/40px undefined, #1f1f1f, ls -1.28px |
| Transition | none |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | form.form--I3Zcx 440.0x414.0 bg #ffffff border T:1px #e0e0e0 / R:1px #e0e0e0 / B:1px #e0e0e0 / L:1px #e0e0e0 r 24px; button.button--PGwt3.xl--uHTBT 374.0x56.0 bg #ffffff border T:1px #000000 @ 0.12 / R:1px #000000 @ 0.12 / B:1px #000000 @ 0.12 / L:1px #000000 @ 0.12 r 16px; input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #f5f5f5 border T:1px #f5f5f5 / R:1px #f5f5f5 / B:1px #f5f5f5 / L:1px #f5f5f5 r 16px; input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #f5f5f5 border T:1px #f5f5f5 / R:1px #f5f5f5 / B:1px #f5f5f5 / L:1px #f5f5f5 r 16px; button.button--PGwt3.xl--uHTBT 374.0x56.0 bg #9fb8f9 r 16px |
| How | at rest |

Crops: `login-card-default.png`.

#### login-field

Email field (sign-in). The sign-in e-mail input; focused and typed into then cleared — never submitted.

Page: login. Selector: `signin email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 374 x 56 | = | = |
| Padding | 20px 20px 20px 44px | = | = |
| Border | 1px solid #f5f5f5 | 1px solid #e0e0e0 | 1px solid #e0e0e0 |
| Radius | 16px | = | = |
| Background | #f5f5f5 | #ffffff | #ffffff |
| Box shadow | none | #000000 @ 0.04 0px 0px 0px 4px | #000000 @ 0.04 0px 0px 0px 4px |
| Outline | none | = | = |
| Font | Inter 16px/16px 400 | = | = |
| Letter spacing | -0.32px | = | = |
| Colour | #999999 | = | #1f1f1f |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #999999, opacity 1 | = | = |
| Painted layers | input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #f5f5f5 border T:1px #f5f5f5 / R:1px #f5f5f5 / B:1px #f5f5f5 / L:1px #f5f5f5 r 16px | input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #ffffff border T:1px #e0e0e0 / R:1px #e0e0e0 / B:1px #e0e0e0 / L:1px #e0e0e0 r 16px shadow #000000 @ 0.04 0px 0px 0px 4px | input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #ffffff border T:1px #e0e0e0 / R:1px #e0e0e0 / B:1px #e0e0e0 / L:1px #e0e0e0 r 16px shadow #000000 @ 0.04 0px 0px 0px 4px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-field-default.png`, `login-field-focused.png`, `login-field-filled.png`.

#### login-pass

Password field (sign-in). The sign-in password input; focused and typed into then cleared — never submitted.

Page: login. Selector: `signin password input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 374 x 56 | = | = |
| Padding | 20px 20px 20px 44px | = | = |
| Border | 1px solid #f5f5f5 | 1px solid #e0e0e0 | 1px solid #e0e0e0 |
| Radius | 16px | = | = |
| Background | #f5f5f5 | #ffffff | #ffffff |
| Box shadow | none | #000000 @ 0.04 0px 0px 0px 4px | #000000 @ 0.04 0px 0px 0px 4px |
| Outline | none | = | = |
| Font | Inter 16px/16px 400 | = | = |
| Letter spacing | -0.32px | = | = |
| Colour | #999999 | = | #1f1f1f |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #999999, opacity 1 | = | = |
| Painted layers | input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #f5f5f5 border T:1px #f5f5f5 / R:1px #f5f5f5 / B:1px #f5f5f5 / L:1px #f5f5f5 r 16px | input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #ffffff border T:1px #e0e0e0 / R:1px #e0e0e0 / B:1px #e0e0e0 / L:1px #e0e0e0 r 16px shadow #000000 @ 0.04 0px 0px 0px 4px | input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #ffffff border T:1px #e0e0e0 / R:1px #e0e0e0 / B:1px #e0e0e0 / L:1px #e0e0e0 r 16px shadow #000000 @ 0.04 0px 0px 0px 4px |
| How | at rest | clicked into the field | typed "sample-pass-123", then deleted; nothing sent |

Crops: `login-pass-default.png`, `login-pass-focused.png`, `login-pass-filled.png`.

#### login-submit

Sign-in submit. The primary "Log In" submit; every state was measured but the button was never clicked — nothing was submitted. Disabled at rest until both fields validate; `enabled` is the fill it paints once sample text sits in both fields.

Page: login. Selector: `signin submit button`. States: default, hover, focus-visible, pressed, enabled.

| Property | default | hover | focus-visible | pressed | enabled |
|---|---|---|---|---|---|
| Size (w x h) | 374 x 56 | = | - | = | = |
| Padding | 20px | = | - | = | = |
| Border | none | = | - | = | = |
| Radius | 16px | = | - | = | = |
| Background | #9fb8f9 | = | - | #102f93 | #0050ff |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | Inter 16px/16px 400 | = | - | = | = |
| Letter spacing | -0.32px | = | - | = | = |
| Colour | #ffffff | = | - | = | = |
| Text node | div.content--uLeCT.noMargin--wsr1o: Inter 16px/16px undefined, #ffffff, ls -0.32px | = | - | = | = |
| Transition | none | = | - | = | = |
| Cursor | pointer | = | - | = | = |
| Painted layers | button.button--PGwt3.xl--uHTBT 374.0x56.0 bg #9fb8f9 r 16px | = | - | button.button--PGwt3.xl--uHTBT 374.0x56.0 bg #102f93 r 16px | button.button--PGwt3.xl--uHTBT 374.0x56.0 bg #0050ff r 16px |
| Ancestor paint | 1 up form.form--I3Zcx bg #ffffff | = | - | = | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | typed sample text into both fields so the submit enabled — still never clicked |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-pressed.png`, `login-submit-enabled.png`.

#### login-google

Google OAuth button. The "Sign in with Google" OAuth button; measured, never activated.

Page: login. Selector: `signin Google button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 374 x 56 | = | = | = |
| Padding | 19px | = | = | = |
| Border | 1px solid #000000 @ 0.12 | = | = | = |
| Radius | 16px | = | = | = |
| Background | #ffffff | #000000 @ 0.06 | = | #000000 @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter 16px/16px 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #000000 @ 0.56 | #1f1f1f | = | #1f1f1f |
| Text node | div.content--uLeCT: Inter 16px/16px undefined, #000000 @ 0.56, ls -0.32px | div.content--uLeCT: Inter 16px/16px undefined, #1f1f1f, ls -0.32px | = | div.content--uLeCT: Inter 16px/16px undefined, #1f1f1f, ls -0.32px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| Painted layers | button.button--PGwt3.xl--uHTBT 374.0x56.0 bg #ffffff border T:1px #000000 @ 0.12 / R:1px #000000 @ 0.12 / B:1px #000000 @ 0.12 / L:1px #000000 @ 0.12 r 16px | button.button--PGwt3.xl--uHTBT 374.0x56.0 bg #000000 @ 0.06 border T:1px #000000 @ 0.12 / R:1px #000000 @ 0.12 / B:1px #000000 @ 0.12 / L:1px #000000 @ 0.12 r 16px | button.button--PGwt3.xl--uHTBT 374.0x56.0 bg #ffffff border T:1px #000000 @ 0.12 / R:1px #000000 @ 0.12 / B:1px #000000 @ 0.12 / L:1px #000000 @ 0.12 r 16px outline 1px auto #101010 offset 0px | button.button--PGwt3.xl--uHTBT 374.0x56.0 bg #000000 @ 0.08 border T:1px #000000 @ 0.12 / R:1px #000000 @ 0.12 / B:1px #000000 @ 0.12 / L:1px #000000 @ 0.12 r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-google-default.png`, `login-google-hover.png`, `login-google-focus-visible.png`, `login-google-pressed.png`.

#### login-forgot

Forgot-password link. The "Forgot password?" link to /restore; measured, never followed.

Page: login. Selector: `signin forgot link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 165.2 x 24 | = | = | = |
| Padding | 8px 0px 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/16px 400 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #999999 | #0050ff | = | #0050ff |
| Transition | color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up form.form--I3Zcx bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-forgot-default.png`, `login-forgot-hover.png`, `login-forgot-focus-visible.png`, `login-forgot-pressed.png`.

#### login-signup

Sign-up link. The "Sign Up" link beside the sign-in form; measured, never followed.

Page: login. Selector: `signin signup link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 88.48 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/20px 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #0050ff | = | = | = |
| Transition | color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-signup-default.png`, `login-signup-hover.png`, `login-signup-focus-visible.png`, `login-signup-pressed.png`.

### App sign-up

#### signup-h1

Sign-up headline. The app sign-up heading on app.flowmapp.com/signup.

Page: signup. Selector: `signup heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 70.2 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/24px 500 |
| Letter spacing | -0.4px |
| Colour | #1f1f1f |
| Transition | none |
| How | at rest |

Crops: `signup-h1-default.png`.

#### signup-field

Email field (sign-up). The sign-up e-mail input; focused and typed into then cleared — never submitted.

Page: signup. Selector: `signup email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 374 x 56 | = | = |
| Padding | 20px 20px 20px 44px | = | = |
| Border | 1px solid #f5f5f5 | 1px solid #e0e0e0 | 1px solid #e0e0e0 |
| Radius | 16px | = | = |
| Background | #f5f5f5 | #ffffff | #ffffff |
| Box shadow | none | #000000 @ 0.04 0px 0px 0px 4px | #000000 @ 0.04 0px 0px 0px 4px |
| Outline | none | = | = |
| Font | Inter 16px/16px 400 | = | = |
| Letter spacing | -0.32px | = | = |
| Colour | #999999 | = | #1f1f1f |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #999999, opacity 1 | = | = |
| Painted layers | input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #f5f5f5 border T:1px #f5f5f5 / R:1px #f5f5f5 / B:1px #f5f5f5 / L:1px #f5f5f5 r 16px | input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #ffffff border T:1px #e0e0e0 / R:1px #e0e0e0 / B:1px #e0e0e0 / L:1px #e0e0e0 r 16px shadow #000000 @ 0.04 0px 0px 0px 4px | input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #ffffff border T:1px #e0e0e0 / R:1px #e0e0e0 / B:1px #e0e0e0 / L:1px #e0e0e0 r 16px shadow #000000 @ 0.04 0px 0px 0px 4px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `signup-field-default.png`, `signup-field-focused.png`, `signup-field-filled.png`.

#### signup-name

Name field (sign-up). The sign-up name input; focused and typed into then cleared — never submitted.

Page: signup. Selector: `signup name input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 374 x 56 | = | = |
| Padding | 20px 20px 20px 44px | = | = |
| Border | 1px solid #f5f5f5 | 1px solid #e0e0e0 | 1px solid #e0e0e0 |
| Radius | 16px | = | = |
| Background | #f5f5f5 | #ffffff | #ffffff |
| Box shadow | none | #000000 @ 0.04 0px 0px 0px 4px | #000000 @ 0.04 0px 0px 0px 4px |
| Outline | none | = | = |
| Font | Inter 16px/16px 400 | = | = |
| Letter spacing | -0.32px | = | = |
| Colour | #999999 | = | #1f1f1f |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #999999, opacity 1 | = | = |
| Painted layers | input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #f5f5f5 border T:1px #f5f5f5 / R:1px #f5f5f5 / B:1px #f5f5f5 / L:1px #f5f5f5 r 16px | input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #ffffff border T:1px #e0e0e0 / R:1px #e0e0e0 / B:1px #e0e0e0 / L:1px #e0e0e0 r 16px shadow #000000 @ 0.04 0px 0px 0px 4px | input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #ffffff border T:1px #e0e0e0 / R:1px #e0e0e0 / B:1px #e0e0e0 / L:1px #e0e0e0 r 16px shadow #000000 @ 0.04 0px 0px 0px 4px |
| How | at rest | clicked into the field | typed "Example User", then deleted; nothing sent |

Crops: `signup-name-default.png`, `signup-name-focused.png`, `signup-name-filled.png`.

#### signup-pass

Password field (sign-up). The sign-up password input; focused and typed into then cleared — never submitted.

Page: signup. Selector: `signup password input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 374 x 56 | = | = |
| Padding | 20px 20px 20px 44px | = | = |
| Border | 1px solid #f5f5f5 | 1px solid #e0e0e0 | 1px solid #e0e0e0 |
| Radius | 16px | = | = |
| Background | #f5f5f5 | #ffffff | #ffffff |
| Box shadow | none | #000000 @ 0.04 0px 0px 0px 4px | #000000 @ 0.04 0px 0px 0px 4px |
| Outline | none | = | = |
| Font | Inter 16px/16px 400 | = | = |
| Letter spacing | -0.32px | = | = |
| Colour | #999999 | = | #1f1f1f |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #999999, opacity 1 | = | = |
| Painted layers | input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #f5f5f5 border T:1px #f5f5f5 / R:1px #f5f5f5 / B:1px #f5f5f5 / L:1px #f5f5f5 r 16px | input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #ffffff border T:1px #e0e0e0 / R:1px #e0e0e0 / B:1px #e0e0e0 / L:1px #e0e0e0 r 16px shadow #000000 @ 0.04 0px 0px 0px 4px | input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #ffffff border T:1px #e0e0e0 / R:1px #e0e0e0 / B:1px #e0e0e0 / L:1px #e0e0e0 r 16px shadow #000000 @ 0.04 0px 0px 0px 4px |
| How | at rest | clicked into the field | typed "sample-pass-123", then deleted; nothing sent |

Crops: `signup-pass-default.png`, `signup-pass-focused.png`, `signup-pass-filled.png`.

#### signup-submit

Sign-up submit. The primary sign-up submit; its states were measured but the button was never clicked — no account was created.

Page: signup. Selector: `signup submit button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 374 x 56 | = | = | = |
| Padding | 19px | = | = | = |
| Border | 1px solid #000000 @ 0.12 | = | = | = |
| Radius | 16px | = | = | = |
| Background | #ffffff | #000000 @ 0.06 | = | #000000 @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter 16px/16px 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #000000 @ 0.56 | #1f1f1f | = | #1f1f1f |
| Text node | div.content--uLeCT: Inter 16px/16px undefined, #000000 @ 0.56, ls -0.32px | div.content--uLeCT: Inter 16px/16px undefined, #1f1f1f, ls -0.32px | = | div.content--uLeCT: Inter 16px/16px undefined, #1f1f1f, ls -0.32px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| Painted layers | button.button--PGwt3.xl--uHTBT 374.0x56.0 bg #ffffff border T:1px #000000 @ 0.12 / R:1px #000000 @ 0.12 / B:1px #000000 @ 0.12 / L:1px #000000 @ 0.12 r 16px | button.button--PGwt3.xl--uHTBT 374.0x56.0 bg #000000 @ 0.06 border T:1px #000000 @ 0.12 / R:1px #000000 @ 0.12 / B:1px #000000 @ 0.12 / L:1px #000000 @ 0.12 r 16px | button.button--PGwt3.xl--uHTBT 374.0x56.0 bg #ffffff border T:1px #000000 @ 0.12 / R:1px #000000 @ 0.12 / B:1px #000000 @ 0.12 / L:1px #000000 @ 0.12 r 16px outline 1px auto #101010 offset 0px | button.button--PGwt3.xl--uHTBT 374.0x56.0 bg #000000 @ 0.08 border T:1px #000000 @ 0.12 / R:1px #000000 @ 0.12 / B:1px #000000 @ 0.12 / L:1px #000000 @ 0.12 r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-submit-default.png`, `signup-submit-hover.png`, `signup-submit-focus-visible.png`, `signup-submit-pressed.png`.

#### signup-google

Google OAuth button (sign-up). The "Sign up with Google" button; measured, never activated.

Page: signup. Selector: `signup Google button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 374 x 56 | = | = | = |
| Padding | 19px | = | = | = |
| Border | 1px solid #000000 @ 0.12 | = | = | = |
| Radius | 16px | = | = | = |
| Background | #ffffff | #000000 @ 0.06 | = | #000000 @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter 16px/16px 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #000000 @ 0.56 | #1f1f1f | = | #1f1f1f |
| Text node | div.content--uLeCT: Inter 16px/16px undefined, #000000 @ 0.56, ls -0.32px | div.content--uLeCT: Inter 16px/16px undefined, #1f1f1f, ls -0.32px | = | div.content--uLeCT: Inter 16px/16px undefined, #1f1f1f, ls -0.32px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| Painted layers | button.button--PGwt3.xl--uHTBT 374.0x56.0 bg #ffffff border T:1px #000000 @ 0.12 / R:1px #000000 @ 0.12 / B:1px #000000 @ 0.12 / L:1px #000000 @ 0.12 r 16px | button.button--PGwt3.xl--uHTBT 374.0x56.0 bg #000000 @ 0.06 border T:1px #000000 @ 0.12 / R:1px #000000 @ 0.12 / B:1px #000000 @ 0.12 / L:1px #000000 @ 0.12 r 16px | button.button--PGwt3.xl--uHTBT 374.0x56.0 bg #ffffff border T:1px #000000 @ 0.12 / R:1px #000000 @ 0.12 / B:1px #000000 @ 0.12 / L:1px #000000 @ 0.12 r 16px outline 1px auto #101010 offset 0px | button.button--PGwt3.xl--uHTBT 374.0x56.0 bg #000000 @ 0.08 border T:1px #000000 @ 0.12 / R:1px #000000 @ 0.12 / B:1px #000000 @ 0.12 / L:1px #000000 @ 0.12 r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-google-default.png`, `signup-google-hover.png`, `signup-google-focus-visible.png`, `signup-google-pressed.png`.

#### signup-terms

Terms line. The terms/privacy line under the sign-up form; its links were never followed.

Page: signup. Selector: `signup terms line`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 115.77 x 17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/18px 400 |
| Letter spacing | -0.14px |
| Colour | #999999 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `signup-terms-default.png`.

### App restore

#### restore-h1

Restore headline. The password-restore heading on app.flowmapp.com/restore.

Page: restore. Selector: `restore heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 185.2 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/24px 500 |
| Letter spacing | -0.4px |
| Colour | #1f1f1f |
| Transition | none |
| How | at rest |

Crops: `restore-h1-default.png`.

#### restore-field

Email field (restore). The restore e-mail input; focused and typed into then cleared — never submitted.

Page: restore. Selector: `restore email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 374 x 56 | = | = |
| Padding | 20px 20px 20px 44px | = | = |
| Border | 1px solid #f5f5f5 | 1px solid #e0e0e0 | 1px solid #e0e0e0 |
| Radius | 16px | = | = |
| Background | #f5f5f5 | #ffffff | #ffffff |
| Box shadow | none | #000000 @ 0.04 0px 0px 0px 4px | #000000 @ 0.04 0px 0px 0px 4px |
| Outline | none | = | = |
| Font | Inter 16px/16px 400 | = | = |
| Letter spacing | -0.32px | = | = |
| Colour | #999999 | = | #1f1f1f |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #999999, opacity 1 | = | = |
| Painted layers | input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #f5f5f5 border T:1px #f5f5f5 / R:1px #f5f5f5 / B:1px #f5f5f5 / L:1px #f5f5f5 r 16px | input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #ffffff border T:1px #e0e0e0 / R:1px #e0e0e0 / B:1px #e0e0e0 / L:1px #e0e0e0 r 16px shadow #000000 @ 0.04 0px 0px 0px 4px | input.input--LVdIP.xl--i7mzS 374.0x56.0 bg #ffffff border T:1px #e0e0e0 / R:1px #e0e0e0 / B:1px #e0e0e0 / L:1px #e0e0e0 r 16px shadow #000000 @ 0.04 0px 0px 0px 4px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `restore-field-default.png`, `restore-field-focused.png`, `restore-field-filled.png`.

#### restore-send

Restore submit. The restore submit; its states were measured but the button was never clicked — no reset e-mail was sent.

Page: restore. Selector: `restore submit button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 374 x 56 | = | - | = |
| Padding | 20px | = | - | = |
| Border | none | = | - | = |
| Radius | 16px | = | - | = |
| Background | #9fb8f9 | = | - | #102f93 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 16px/16px 400 | = | - | = |
| Letter spacing | -0.32px | = | - | = |
| Colour | #ffffff | = | - | = |
| Text node | div.content--uLeCT.noMargin--wsr1o: Inter 16px/16px undefined, #ffffff, ls -0.32px | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | button.button--PGwt3.xl--uHTBT 374.0x56.0 bg #9fb8f9 r 16px | = | - | button.button--PGwt3.xl--uHTBT 374.0x56.0 bg #102f93 r 16px |
| Ancestor paint | 1 up form.form--NUHsb bg #ffffff | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `restore-send-default.png`, `restore-send-hover.png`, `restore-send-pressed.png`.

#### restore-back

Back-to-login link. The link back to the sign-in form; measured, never followed.

Page: restore. Selector: `restore back link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 47.77 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/20px 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #0050ff | = | = | = |
| Transition | color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `restore-back-default.png`, `restore-back-hover.png`, `restore-back-focus-visible.png`, `restore-back-pressed.png`.

### Shared demo project

#### sh-menu

Project dropdown. The "Demo Project" dropdown in the share viewer header listing the published project's boards; opened was measured after clicking it — a local UI toggle whose items were never activated.

Page: sharesitemap. Selector: `share .ant-dropdown-trigger`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 141.64 x 40 | = | = | = | = |
| Padding | 12px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 12px | = | = | = | = |
| Background | transparent | #000000 @ 0.04 | = | #000000 @ 0.04 | #000000 @ 0.04 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = | = |
| Font | Inter 14px/16px 400 | = | = | = | = |
| Letter spacing | -0.28px | = | = | = | = |
| Colour | #707070 | #1f1f1f | = | #1f1f1f | #1f1f1f |
| Text node | div.content--uLeCT: Inter 14px/16px undefined, #707070, ls -0.28px | div.content--uLeCT: Inter 14px/16px undefined, #1f1f1f, ls -0.28px | = | div.content--uLeCT: Inter 14px/16px undefined, #1f1f1f, ls -0.28px | div.content--uLeCT: Inter 14px/16px undefined, #1f1f1f, ls -0.28px |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 16 x 16, colour #707070 | 16 x 16, colour #1f1f1f | = | 16 x 16, colour #1f1f1f | 16 x 16, colour #1f1f1f |
| Ancestor paint | 1 up div.wrapper--UxlY4 bg #f5f5f5 @ 0.8 | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | clicked the "Demo Project" button to open its dropdown |
| Painted layers | - | button.ant-dropdown-trigger.button--PGwt3 141.6x40.0 bg #000000 @ 0.04 r 12px | button.ant-dropdown-trigger.button--PGwt3 141.6x40.0 r 12px outline 1px auto #101010 offset 0px | button.ant-dropdown-trigger.button--PGwt3 141.6x40.0 bg #000000 @ 0.04 r 12px | button.ant-dropdown-trigger.ant-dropdown-open 141.6x40.0 bg #000000 @ 0.04 r 12px |

Crops: `sh-menu-default.png`, `sh-menu-hover.png`, `sh-menu-focus-visible.png`, `sh-menu-pressed.png`, `sh-menu-opened.png`.

#### sh-tab-structure

Structure tab. The "Structure" toolbar tab in the share viewer.

Page: sharesitemap. Selector: `share Structure tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 113.48 x 40 | = | = | = |
| Padding | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #000000 @ 0.04 | = | #000000 @ 0.04 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter 14px/16px 400 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #707070 | #1f1f1f | = | #1f1f1f |
| Text node | div.content--uLeCT: Inter 14px/16px undefined, #707070, ls -0.28px | div.content--uLeCT: Inter 14px/16px undefined, #1f1f1f, ls -0.28px | = | div.content--uLeCT: Inter 14px/16px undefined, #1f1f1f, ls -0.28px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #707070 | 16 x 16, colour #1f1f1f | = | 16 x 16, colour #1f1f1f |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |
| Painted layers | - | button.button--PGwt3.m--_mvvS 113.5x40.0 bg #000000 @ 0.04 r 12px | button.button--PGwt3.m--_mvvS 113.5x40.0 r 12px outline 1px auto #101010 offset 0px | button.button--PGwt3.m--_mvvS 113.5x40.0 bg #000000 @ 0.04 r 12px |

Crops: `sh-tab-structure-default.png`, `sh-tab-structure-hover.png`, `sh-tab-structure-focus-visible.png`, `sh-tab-structure-pressed.png`.

#### sh-tab-estimation

Estimation tab. The "Estimation" toolbar tab; opened was measured after clicking it — a local UI toggle switching the viewer pane.

Page: sharesitemap. Selector: `share Estimation tab`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 122.2 x 40 | = | = | = | = |
| Padding | 12px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 12px | = | = | = | = |
| Background | transparent | #000000 @ 0.04 | = | #000000 @ 0.04 | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = | = |
| Font | Inter 14px/16px 400 | = | = | = | = |
| Letter spacing | -0.28px | = | = | = | = |
| Colour | #707070 | #1f1f1f | = | #1f1f1f | = |
| Text node | div.content--uLeCT: Inter 14px/16px undefined, #707070, ls -0.28px | div.content--uLeCT: Inter 14px/16px undefined, #1f1f1f, ls -0.28px | = | div.content--uLeCT: Inter 14px/16px undefined, #1f1f1f, ls -0.28px | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 16 x 16, colour #707070 | 16 x 16, colour #1f1f1f | = | 16 x 16, colour #1f1f1f | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | clicked the "Estimation" tab |
| Painted layers | - | button.button--PGwt3.m--_mvvS 122.2x40.0 bg #000000 @ 0.04 r 12px | button.button--PGwt3.m--_mvvS 122.2x40.0 r 12px outline 1px auto #101010 offset 0px | button.button--PGwt3.m--_mvvS 122.2x40.0 bg #000000 @ 0.04 r 12px | = |

Crops: `sh-tab-estimation-default.png`, `sh-tab-estimation-hover.png`, `sh-tab-estimation-focus-visible.png`, `sh-tab-estimation-pressed.png`, `sh-tab-estimation-opened.png`.

#### sh-login-btn

Share Log In button. The "Log In" header button in the share viewer; measured, never clicked — the viewer stays signed out.

Page: sharesitemap. Selector: `share Log In button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 65.33 x 40 | = | = | = |
| Padding | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | #000000 @ 0.04 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter 14px/16px 400 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #707070 | = | = | #1f1f1f |
| Text node | div.content--uLeCT.noMargin--wsr1o: Inter 14px/16px undefined, #707070, ls -0.28px | = | = | div.content--uLeCT.noMargin--wsr1o: Inter 14px/16px undefined, #1f1f1f, ls -0.28px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.button--PGwt3.m--_mvvS 65.3x40.0 r 12px outline 1px auto #101010 offset 0px | button.button--PGwt3.m--_mvvS 65.3x40.0 bg #000000 @ 0.04 r 12px |

Crops: `sh-login-btn-default.png`, `sh-login-btn-hover.png`, `sh-login-btn-focus-visible.png`, `sh-login-btn-pressed.png`.

#### sh-signup-btn

Share Sign Up button. The "Sign Up" header button in the share viewer; measured, never clicked.

Page: sharesitemap. Selector: `share Sign Up button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 76.05 x 40 | = | = | = |
| Padding | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | #000000 @ 0.04 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter 14px/16px 400 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #707070 | = | = | #1f1f1f |
| Text node | div.content--uLeCT.noMargin--wsr1o: Inter 14px/16px undefined, #707070, ls -0.28px | = | = | div.content--uLeCT.noMargin--wsr1o: Inter 14px/16px undefined, #1f1f1f, ls -0.28px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.button--PGwt3.m--_mvvS 76.0x40.0 r 12px outline 1px auto #101010 offset 0px | button.button--PGwt3.m--_mvvS 76.0x40.0 bg #000000 @ 0.04 r 12px |

Crops: `sh-signup-btn-default.png`, `sh-signup-btn-hover.png`, `sh-signup-btn-focus-visible.png`, `sh-signup-btn-pressed.png`.

#### sh-popup

Sign-up nudge. The "Hi, Log In or Sign Up to start planning amazing websites!" toast pinned over the viewer (dismissable, left in place for the reading).

Page: sharesitemap. Selector: `share [class*=popup]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 251.58 x 80 |
| Padding | 16px 20px |
| Border | none |
| Radius | 14px |
| Background | #000000 @ 0.56 |
| Box shadow | none |
| Backdrop filter | blur(8px) |
| Outline | none |
| Font | Inter 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.content--d9vm2: Inter 14px/24px undefined, #ffffff, ls -0.14px |
| Transition | none |
| Painted layers | div.popup--Numk9 251.6x80.0 bg #000000 @ 0.56 r 14px |
| How | at rest |

Crops: `sh-popup-default.png`.

#### sh-card

Sitemap page card. A page card on the published sitemap canvas (title, mini-map of sections); read-only.

Page: sharesitemap. Selector: `share [class*=card--]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 95.07 x 104.35 | = |
| Padding | 0px | = |
| Border | 2px solid #1f1f1f | = |
| Radius | 16px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/18.4px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | div.title--J6qJN: Inter 16px/20px undefined, #1f1f1f, ls -0.32px | = |
| Transition | opacity 0.2s ease-in-out | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = |
| Cursor | pointer | = |
| Painted layers | div.card--ua7fI 95.1x104.3 bg #ffffff border T:2px #1f1f1f / R:2px #1f1f1f / B:2px #1f1f1f / L:2px #1f1f1f r 16px; div.label--ICrwG 52.8x9.3 bg #1f1f1f border T:1px #1f1f1f / R:1px #1f1f1f / B:1px #1f1f1f / L:1px #1f1f1f r 12px; div.cover--ktowA 81.2x55.7 bg #f5cc00 @ 0.16 r 8px | = |
| How | at rest | mouse hover |

Crops: `sh-card-default.png`, `sh-card-hover.png`.

#### sh-blocks

Sitemap card blocks. The section list inside a sitemap page card (Menu, Header, Featured Services…).

Page: sharesitemap. Selector: `share [class*=blocks--]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 81.16 x 113.62 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.title--Hzp4i: Inter 12px/20px undefined, #f5cc00 |
| Transition | none |
| Cursor | pointer |
| Icon | 6.96 x 6.96, colour #1f1f1f |
| Painted layers | div.block--uZwRO 81.2x20.9 bg #f5cc00 @ 0.16 r 8px; div.block--uZwRO 81.2x20.9 bg #ffa334 @ 0.16 r 8px; div.block--uZwRO 81.2x20.9 bg #ffa334 @ 0.16 r 8px; div.block--uZwRO 81.2x20.9 bg #ffa334 @ 0.16 r 8px; div.block--uZwRO 81.2x20.9 bg #36eb8d @ 0.16 r 8px |
| How | at rest |

Crops: `sh-blocks-default.png`.

#### sh-toolbar-btn

Canvas toolbar button. An icon button on the share viewer's bottom toolbar panel.

Page: sharesitemap. Selector: `share toolbar button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | #000000 @ 0.04 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 20px/20px 400 | = | = | = |
| Letter spacing | -0.4px | = | = | = |
| Colour | #1f1f1f | = | = | #0050ff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #1f1f1f | = | = | 16 x 16, colour #0050ff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | = | button.button--uOHwQ.m--nyhEe 36.0x36.0 bg #000000 @ 0.04 r 12px |

Crops: `sh-toolbar-btn-default.png`, `sh-toolbar-btn-hover.png`, `sh-toolbar-btn-focus-visible.png`, `sh-toolbar-btn-pressed.png`.

#### sh-toolbar-disabled

Disabled toolbar button. A disabled icon button on the share viewer's bottom toolbar.

Page: sharesitemap. Selector: `share disabled toolbar button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 40 x 40 |
| Padding | 10px |
| Border | none |
| Radius | 12px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/20px 400 |
| Letter spacing | -0.4px |
| Colour | #1f1f1f |
| Transition | none |
| Opacity | 0.2 |
| Cursor | pointer |
| Icon | 16 x 16, colour #1f1f1f |
| How | at rest |

Crops: `sh-toolbar-disabled-default.png`.

#### sh-zoom

Zoom button. The zoom-percentage button on the share viewer toolbar; measured, never toggled.

Page: sharesitemap. Selector: `share zoom button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 53.19 x 40 | = | = | = |
| Padding | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | #000000 @ 0.04 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter 14px/16px 400 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #707070 | = | = | #1f1f1f |
| Text node | div.content--uLeCT.noMargin--wsr1o: Inter 14px/16px undefined, #707070, ls -0.28px | = | = | div.content--uLeCT.noMargin--wsr1o: Inter 14px/16px undefined, #1f1f1f, ls -0.28px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.button--PGwt3.m--_mvvS 53.2x40.0 r 12px outline 1px auto #101010 offset 0px | button.button--PGwt3.m--_mvvS 53.2x40.0 bg #000000 @ 0.04 r 12px |

Crops: `sh-zoom-default.png`, `sh-zoom-hover.png`, `sh-zoom-focus-visible.png`, `sh-zoom-pressed.png`.

#### sh-help

Help button. The "?" help button on the share viewer chrome.

Page: sharesitemap. Selector: `share help button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 100% | = | = | = |
| Background | #000000 @ 0.4 | = | = | #1f1f1f |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter 14px/16px 400 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| Painted layers | button.helpBtn--pWwdL.button--PGwt3 32.0x32.0 bg #000000 @ 0.4 r 100% | = | button.helpBtn--pWwdL.button--PGwt3 32.0x32.0 bg #000000 @ 0.4 r 100% outline 1px auto #101010 offset 0px | button.helpBtn--pWwdL.button--PGwt3 32.0x32.0 bg #1f1f1f r 100% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sh-help-default.png`, `sh-help-hover.png`, `sh-help-focus-visible.png`, `sh-help-pressed.png`.

#### uf-card

User-flow card. A screen/flow card on the published user-flow canvas; read-only.

Page: shareuserflow. Selector: `userflow [class*=card--]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 139.22 x 191.43 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/18.4px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | div.title--J6qJN: Inter 16px/20px undefined, #1f1f1f, ls -0.32px | = |
| Transition | none | = |
| Icon | 100.94 x 62.65, colour #6696ff | = |
| Painted layers | div.card--ua7fI 142.7x194.9 bg #ffffff border T:2px #1f1f1f / R:2px #1f1f1f / B:2px #1f1f1f / L:2px #1f1f1f r 16px; div.label--ICrwG 31.3x13.9 bg #f5cc00 @ 0.4 border T:1px #f5cc00 @ 0.4 / R:1px #f5cc00 @ 0.4 / B:1px #f5cc00 @ 0.4 / L:1px #f5cc00 @ 0.4 r 12px; div.label--ICrwG 63.5x13.9 bg #ff7c43 @ 0.4 border T:1px #ff7c43 @ 0.4 / R:1px #ff7c43 @ 0.4 / B:1px #ff7c43 @ 0.4 / L:1px #ff7c43 @ 0.4 r 12px; div.label--ICrwG 54.8x13.9 bg #6696ff @ 0.4 border T:1px #6696ff @ 0.4 / R:1px #6696ff @ 0.4 / B:1px #6696ff @ 0.4 / L:1px #6696ff @ 0.4 r 12px; div.cover--ktowA 121.8x83.5 bg #6696ff @ 0.16 r 8px; div.dot--Nxoe3 10.0x10.0 bg #ffffff border T:2px #0050ff / R:2px #0050ff / B:2px #0050ff / L:2px #0050ff r 100% | = |
| How | at rest | mouse hover |

Crops: `uf-card-default.png`, `uf-card-hover.png`.

#### uf-tag

Status tag. A status pill on the user-flow canvas (NEW / IN PROGRESS / DONE…).

Page: shareuserflow. Selector: `userflow status tag`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 104.42 x 34.81 |
| Padding | 0px 0px 4px 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.content--f8YW3: Inter 9px/12px undefined, #f5cc00 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.label--ICrwG 31.3x13.9 bg #f5cc00 @ 0.4 border T:1px #f5cc00 @ 0.4 / R:1px #f5cc00 @ 0.4 / B:1px #f5cc00 @ 0.4 / L:1px #f5cc00 @ 0.4 r 12px; div.label--ICrwG 63.5x13.9 bg #ff7c43 @ 0.4 border T:1px #ff7c43 @ 0.4 / R:1px #ff7c43 @ 0.4 / B:1px #ff7c43 @ 0.4 / L:1px #ff7c43 @ 0.4 r 12px; div.label--ICrwG 54.8x13.9 bg #6696ff @ 0.4 border T:1px #6696ff @ 0.4 / R:1px #6696ff @ 0.4 / B:1px #6696ff @ 0.4 / L:1px #6696ff @ 0.4 r 12px |
| How | at rest |

Crops: `uf-tag-default.png`.

### Mobile (390 wide)

#### m-topbar

Mobile top bar. The phone header at 390 wide: wordmark, the burger and the actions that survive the width.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 381.75 x 54.69 |
| Padding | 4.134px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Icon | 0 x 0, colour #ffffff |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | div.nav__bg 0.0x0.0 bg #000000 @ 0.5; div.container.nav-cont__is-br-12--is-sh-img 381.8x50.6 bg #ffffff @ 0.8 r 12px shadow #787c84 @ 0.19 -9.92904px 11.043px 59.7576px 0px; div.nav__links 0.0x0.0 bg #ffffff r 12px; div.nav__link-underline 0.0x0.0 border B:1px #8c9baa; div.nav__pop.is-sh-l--is-bg-wh--is-br-12--is-t-sh-0 0.0x0.0 bg #ffffff r 12px shadow #787c84 @ 0 0px 0px 0px 0px; a.nav__pop-link.is-br-8 0.0x0.0 bg #f6f8fa r 8px |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-burger

Mobile burger. The nav burger at 390 wide; opened was measured after tapping it (a local UI toggle opening the mobile menu).

Page: mobile. Selector: `mobile burger`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 35.88 x 35.88 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Inter 24px/20px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | #ffffff |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 35.88 x 35.88, colour #000000 | = | = | = | 35.88 x 35.88, colour #ffffff, fill #000000 |
| Ancestor paint | 2 up div.container.nav-cont__is-br-12--is-sh-img bg #ffffff @ 0.8 shadow #787c84 @ 0.19 -9.92904px 11.043px 59.7576px 0px | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | tapped the nav burger to open the mobile menu (aria-expanded=true at save) |

Crops: `m-burger-default.png`, `m-burger-hover.png`, `m-burger-focus-visible.png`, `m-burger-pressed.png`, `m-burger-opened.png`.

#### m-menu-link

Mobile menu link. A link inside the opened mobile nav menu.

Page: mobile. Selector: `mobile menu link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 348.53 x 47.7 |
| Padding | 11.388px 14.508px |
| Gap | normal 4.134px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16.614px/23.2596px 600 |
| Letter spacing | -0.312px |
| Colour | #000000 |
| Text node | div: Inter 16.614px/23.2596px undefined, #000000, ls -0.312px |
| Transition | background-color 0.3s ease |
| Cursor | pointer |
| Painted layers | div.nav__link-underline 135.0x24.3 border B:1px #8c9baa |
| Ancestor paint | 1 up div.nav__links bg #ffffff |
| How | at rest |

Crops: `m-menu-link-default.png`.

#### m-hero-h1

Mobile hero headline. The hero display heading at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 348.53 x 99.7 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 33.228px/33.228px 700 |
| Letter spacing | -1.053px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-hero-cta

Mobile hero CTA. The hero action at 390 wide; measured never followed.

Page: mobile. Selector: `mobile hero CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 316.75 x 78.17 | = | = | = |
| Padding | 5.85px | = | = | = |
| Gap | normal 6.786px | = | = | = |
| Border | none | = | = | = |
| Radius | 780px | = | = | = |
| Background | #0080ff @ 0.2 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 20.748px/29.0472px 600 | = | = | = |
| Letter spacing | -0.43875px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.text-block-10: Inter 22.62px/29.0472px undefined, #ffffff, ls -0.43875px | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 65.52 x 13.78, colour #ffffff, fill #000000 | = | = | = |
| Painted layers | a.btn.w-inline-block 316.8x78.2 bg #0080ff @ 0.2 r 780px; div.btn__wrapper 305.1x66.5 bg #0080ff r 780px shadow #0080ff @ 0.34 0px 8px 10px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-hero-cta-default.png`, `m-hero-cta-hover.png`, `m-hero-cta-focus-visible.png`, `m-hero-cta-pressed.png`.

## Transitions declared in the readable stylesheets

www.flowmapp.com serves its CSS same-origin-readable (the Webflow CDN bundle plus an inline block; the app serves its CSS-module chunks), so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- feature: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `color 0.3s, background-color 0.3s`, `border-color 0.3s, color 0.3s, background-color 0.3s`, `background-color 0.3s`, `transform 0.3s`, `height 0.3s, opacity 0.3s`, `opacity 0.3s`, `background-color 0.4s`, `box-shadow 0.3s`, `color 0.3s`

- home: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `color 0.3s, background-color 0.3s`, `border-color 0.3s, color 0.3s, background-color 0.3s`, `background-color 0.3s`, `transform 0.3s`, `height 0.3s, opacity 0.3s`, `opacity 0.3s`, `background-color 0.4s`, `box-shadow 0.3s`, `color 0.3s`

- login: `color 0.3s`, `0.2s, background`, `0.2s`, `background 0.3s`, `0.3s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `background-color 300s ease-in-out`, `150ms ease-out`, `200ms`

- pricing: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `color 0.3s, background-color 0.3s`, `border-color 0.3s, color 0.3s, background-color 0.3s`, `background-color 0.3s`, `transform 0.3s`, `height 0.3s, opacity 0.3s`, `opacity 0.3s`, `background-color 0.4s`, `box-shadow 0.3s`, `color 0.3s`

- sharesitemap: `color 0.3s`, `transform 0.2s`, `outline-offset, outline`, `0.2s`, `color 0.2s, background-color 0.2s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `background-color 300s ease-in-out`, `150ms ease-out`, `200ms`

## Reduced motion

- home (`header a, .nav__link` under prefers-reduced-motion): transition `background-color 0.3s`, animation `none 0s ease 0s 1 normal none running`, html scroll-behavior `auto`
