# Component measurements

Computed styles read from linktr.ee on 2026-11-18 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### navbar

Top navigation. The marketing nav: Solutions, Features, Integrations, Resources, Pricing, Log in, and the Sign up free pill.

Page: home. Selector: `nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 138 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Linksans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e2330 |
| Text node | button.flex.items-center: Linksans 16px/20.8px 400, #1e2330 |
| Transition | transform, translate, scale, rotate 0.3s cubic-bezier(0, 0, 0.2, 1) |
| Icon | 118 x 28, colour #000000 |
| Painted layers | div.relative.mx-auto 1296.0x90.0 bg #ffffff border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 9999px; div.pointer-events-none.absolute 1294.0x2.0 bg #ffffff border T:1px solid #000000 @ 0.04 / R:1px solid #000000 @ 0.04 / B:1px solid #000000 @ 0.04 / L:1px solid #000000 @ 0.04 r 36px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 24px 60px 0px; li.pointer-events-none.absolute 0.0x0.0 bg #eff0ec r 16px; span.flex.size-12 0.0x0.0 bg #ecfef2 r 20px; span.flex.size-12 0.0x0.0 bg #ecfef2 r 20px; span.flex.size-12 0.0x0.0 bg #ecfef2 r 20px |
| How | at rest |

Crops: `navbar-default.png`.

#### nav-link

Nav link. The Pricing text link in the bar. Measured, never followed.

Page: home. Selector: `nav a "Pricing"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 86.16 x 48 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | transparent | = | #eff0ec | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Linksans 16px/20.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e2330 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #a8a29e | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | - | a.flex.items-center 86.2x48.0 bg #eff0ec r 16px | - |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Log in link. The quiet Log in link. Measured, never followed. The login wall itself is a separate signed-out page.

Page: home. Selector: `nav a "Log in"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 101.53 x 62 | = | = | = |
| Padding | 0px 26px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | transparent | #eff0ec | = | #eff0ec |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #1e2330 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Linksans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e2330 | = | = | = |
| Transition | background-color, transform 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.inline-flex.items-center 101.5x62.0 bg #eff0ec r 16px | a.inline-flex.items-center 101.5x62.0 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #1e2330 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 101.5x62.0 bg #eff0ec r 16px |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-signup

Sign up free pill. The ink pill in the bar. Measured, never followed.

Page: home. Selector: `nav a "Sign up free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 152.08 x 62 | = | = | = |
| Padding | 0px 26px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #1e2330 | #262d3e | = | #262d3e |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #1e2330 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Linksans 16px/24px 400 | = | = | = |
| Letter spacing | 0.16px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, transform 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 152.1x62.0 bg #1e2330 r 9999px | a.inline-flex.items-center 152.1x62.0 bg #262d3e r 9999px | a.inline-flex.items-center 152.1x62.0 bg #1e2330 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #1e2330 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 152.1x62.0 bg #262d3e r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signup-default.png`, `nav-signup-hover.png`, `nav-signup-focus-visible.png`, `nav-signup-pressed.png`.

#### nav-menu

Nav menu button. The Solutions disclosure. Opened only to record the menu panel; nothing inside was followed.

Page: home. Selector: `nav button "Solutions"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106.11 x 48 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | transparent | = | #eff0ec | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Linksans 16px/20.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e2330 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #1e2330 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | - | button.flex.items-center 106.1x48.0 bg #eff0ec r 16px | - |

Crops: `nav-menu-default.png`, `nav-menu-hover.png`, `nav-menu-focus-visible.png`, `nav-menu-pressed.png`.

#### nav-menu-panel

Nav menu item. A Solutions menu item, captured after the disclosure is opened. The item has no box until the menu opens. Measured, never followed.

Page: home. Selector: `nav a "Musicians"`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 319 x 48 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 16px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Linksans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e2330 |
| Text node | span.font-linksans.text-base: Linksans 16px/20.8px 400, #1e2330 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 24 x 24, colour #1e2330, fill #000000 |
| How | menu held open |

Crops: `nav-menu-panel-opened.png`.

### Home

#### hero-title

Hero title. "A link in bio built for you." in Linksans.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 616 x 171.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Linksans 80px/85.6px 800 |
| Letter spacing | -1.6px |
| Colour | #254f1a |
| Text node | span.home-hero-b:hidden.home-hero-c:hidden: Linksans 80px/85.6px 800, #254f1a, ls -1.6px |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-cta

Get started for free. The hero claim CTA. Measured, never followed and never submitted.

Page: home. Selector: `a/button "Get started for free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 300 x 60 | = | = | 291 x 58.2 |
| Padding | 0px 36px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #254f1a | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #1e2330 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Linksans 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f3f3f1 | = | = | = |
| Transition | background-color, transform, filter, box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | background-color, transform, filter, box-shadow 0.08s cubic-bezier(0, 0, 0.2, 1) |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.items-center 300.0x60.0 bg #254f1a r 9999px | = | button.inline-flex.items-center 300.0x60.0 bg #254f1a r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #1e2330 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.items-center 291.0x58.2 bg #254f1a r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### claim-field

Claim username field. The linktr.ee/yourname field on the marketing page. A throwaway string was typed and deleted. The form was not submitted.

Page: home. Selector: `input[placeholder*="linktr.ee"]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 290.39 x 60 | = | = |
| Padding | 8px 16px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | 2px solid #ffffff offset 2px | 2px solid #ffffff offset 2px |
| Font | Linksans 16px/24px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #757575 | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #757575 @ 0.5, opacity 1 | = | = |
| Painted layers | input.mb-0.max-h-16 290.4x60.0 bg #ffffff r 8px | input.mb-0.max-h-16 290.4x60.0 bg #ffffff r 8px outline 2px solid #ffffff offset 2px | input.mb-0.max-h-16 290.4x60.0 bg #ffffff r 8px outline 2px solid #ffffff offset 2px |
| How | at rest | clicked into the field | typed "sample", then deleted; nothing sent |

Crops: `claim-field-default.png`, `claim-field-focused.png`, `claim-field-filled.png`.

#### claim-wrap

Claim field shell. The painted shell around the claim field.

Page: home. Selector: `marked claim shell`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 290.39 x 60 |
| Padding | 8px 16px |
| Border | none |
| Radius | 8px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Linksans 16px/24px 500 |
| Letter spacing | normal |
| Colour | #757575 |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | text |
| Placeholder | #757575 @ 0.5, opacity 1 |
| Painted layers | input.mb-0.max-h-16 290.4x60.0 bg #ffffff r 8px |
| How | at rest |

Crops: `claim-wrap-default.png`.

#### claim-submit

Claim your Linktree. The claim button beside the field. Measured, never pressed for real.

Page: home. Selector: `button "Claim your Linktree"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 300 x 60 | = | = | 291 x 58.2 |
| Padding | 0px 36px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #d2e823 | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #1e2330 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Linksans 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e2330 | = | = | = |
| Transition | background-color, transform, filter, box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | background-color, transform, filter, box-shadow 0.08s cubic-bezier(0, 0, 0.2, 1) |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.items-center 300.0x60.0 bg #d2e823 r 9999px | = | button.inline-flex.items-center 300.0x60.0 bg #d2e823 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #1e2330 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.items-center 291.0x58.2 bg #d2e823 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `claim-submit-default.png`, `claim-submit-hover.png`, `claim-submit-focus-visible.png`, `claim-submit-pressed.png`.

#### footer

Footer. The purple footer band with the claim field repeated and the product columns.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1667.45 |
| Padding | 250px 0px 32px 0px |
| Border | none |
| Radius | 0px |
| Background | #502274 |
| Box shadow | none |
| Outline | none |
| Font | Linksans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e2330 |
| Text node | h2.text-h2.text-lavender: Linksans 56px/59.36px 700, #e9c0e9, ls -1.12px |
| Transition | none |
| Icon | 36 x 26, colour #1e2330 |
| Painted layers | footer.relative.overflow-hidden 1440.0x1667.5 bg #502274; input.mb-0.max-h-16 290.4x60.0 bg #ffffff r 8px; button.inline-flex.items-center 300.0x60.0 bg #d2e823 r 9999px; div.relative.z-[1] 1296.0x623.5 bg #ffffff r 16px; a.inline-flex.items-center 102.4x58.0 bg #f3f3f1 r 8px; a.inline-flex.items-center 210.1x58.0 bg #d2e823 r 9999px |
| How | at rest |

Crops: none.

#### footer-link

Footer link. A company-column link. Measured, never followed.

Page: home. Selector: `footer a "About"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 39.14 x 19.5 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Linksans 13px/19.5px 400 | = | = | = |
| Letter spacing | -0.169px | = | = | = |
| Colour | #676b5f | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.7 | - | 0.7 |
| Painted layers | - | - | a.font-linksans.font-normal 39.1x19.5 outline 1px auto #005fcc offset 1px | - |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Pricing

#### pricing-title

Pricing title.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 706.42 x 52.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Linksans 48px/52.8px 800 |
| Letter spacing | -1.92px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### plan-card

Plan name. The Pro plan heading on the public pricing page. Selecting a plan was never clicked.

Page: pricing. Selector: `h3 "Pro"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 64.66 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Linksans 36px/36px 800 |
| Letter spacing | -0.54px |
| Colour | #7008e7 |
| Transition | none |
| Ancestor paint | 3 up div.relative.flex shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.12 0px 16px 32px 4px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-select

Try free for 7 days. The Pro plan link. Measured, never followed. Checkout was not opened.

Page: pricing. Selector: `a "Try free for 7 days"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 336 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #7f22fe | #7008e7 | = | #7008e7 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Linksans 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.h-12 336.0x48.0 bg #7f22fe r 9999px | a.inline-flex.h-12 336.0x48.0 bg #7008e7 r 9999px | a.inline-flex.h-12 336.0x48.0 bg #7f22fe r 9999px outline 1px auto #005fcc offset 1px | a.inline-flex.h-12 336.0x48.0 bg #7008e7 r 9999px |
| Ancestor paint | 3 up div.relative.flex shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.12 0px 16px 32px 4px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-select-default.png`, `plan-select-hover.png`, `plan-select-focus-visible.png`, `plan-select-pressed.png`.

#### plan-free

Get started. The free-plan link on the pricing page. Measured, never followed.

Page: pricing. Selector: `a "Get started"`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 336 x 48 | = |
| Padding | 0px 24px | = |
| Gap | 8px | = |
| Border | 1px solid #040403 @ 0.14 | = |
| Radius | 9999px | = |
| Background | #ffffff | #f7f7f7 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Linksans 16px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #040403 @ 0.9 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | a.inline-flex.h-12 336.0x48.0 bg #ffffff border T:1px solid #040403 @ 0.14 / R:1px solid #040403 @ 0.14 / B:1px solid #040403 @ 0.14 / L:1px solid #040403 @ 0.14 r 9999px | a.inline-flex.h-12 336.0x48.0 bg #f7f7f7 border T:1px solid #040403 @ 0.14 / R:1px solid #040403 @ 0.14 / B:1px solid #040403 @ 0.14 / L:1px solid #040403 @ 0.14 r 9999px |
| Ancestor paint | 3 up div.relative.flex shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.02 0px 0px 0px 1px, #000000 @ 0.02 0px 1px 2px 0px, #000000 @ 0.05 0px 8px 32px 0px | = |
| How | at rest | mouse hover |

Crops: `plan-free-default.png`, `plan-free-hover.png`.

### Public profile

#### profile-title

Profile name. The public Linktree profile title (the official linktr.ee page).

Page: profile. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 95.25 x 33 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Link Sans Product 24px/28.8px 600 |
| Letter spacing | normal |
| Colour | #040212 |
| Transition | none |
| How | at rest |

Crops: `profile-title-default.png`.

#### profile-share

Share profile. The share icon button on a public profile. Its name is an aria-label. Measured, never pressed, so no share sheet was sent.

Page: profile. Selector: `button[aria-label="Share profile"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Link Sans Product 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #000000 | = | = | = |
| Ancestor paint | 1 up div.relative.flex outline 1px solid #ffffff @ 0.4 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | - | button.flex.h-full 40.0x40.0 outline 1px auto #005fcc offset 0px | - |

Crops: `profile-share-default.png`, `profile-share-hover.png`, `profile-share-focus-visible.png`, `profile-share-pressed.png`.

#### profile-tab

Profile tab. The Links tab on the public profile.

Page: profile. Selector: `button "Links"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 93.86 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 64px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Link Sans Product 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.font-product.text-sm: Link Sans Product 16px/24px 500, #000000, ls -0.32px | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | - | button.group.peer 93.9x48.0 r 64px outline 1px auto #005fcc offset 0px | - |

Crops: `profile-tab-default.png`, `profile-tab-hover.png`, `profile-tab-focus-visible.png`, `profile-tab-pressed.png`.

#### profile-tab-shop

Shop tab. The unselected Shop tab. Not selected, so the page content was not swapped.

Page: profile. Selector: `button "Shop"`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 94.16 x 48 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 64px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Link Sans Product 16px/16px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | span.font-product.text-sm: Link Sans Product 16px/24px 500, #ffffff, ls -0.32px | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | CDP forcePseudoState :active:hover |

Crops: `profile-tab-shop-default.png`, `profile-tab-shop-hover.png`, `profile-tab-shop-pressed.png`.

#### profile-social

Social icon button. A social icon on the public profile. Measured, never followed.

Page: profile. Selector: `button "Linktree Instagram"`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 48 x 48 | 51.6 x 51.6 |
| Padding | 8px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #ffffff @ 0 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Link Sans Product 16px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | transform 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 32 x 32, colour #040212 | 34.4 x 34.4, colour #040212 |
| Painted layers | button.z-0.cursor-pointer 48.0x48.0 bg #ffffff @ 0 | button.z-0.cursor-pointer 51.6x51.6 bg #ffffff @ 0 |
| How | at rest | mouse hover |
| Text node | - | span.sr-only: Link Sans Product 16px/16px 400, #000000 |
| Transform | - | matrix(1.075, 0, 0, 1.075, 0, 0) |

Crops: `profile-social-default.png`, `profile-social-hover.png`.

#### profile-link

Profile link card. A published link card on the official profile. Measured, never followed.

Page: profile. Selector: `profile link card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 394.86 x 64 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Link Sans Product 16px/16px 400 | = |
| Letter spacing | -0.2px | = |
| Colour | #14160e | = |
| Transition | none | = |
| Cursor | pointer | = |
| Ancestor paint | 3 up div.LinkContainer_LinkContainer__Kk5IQ.grid bg #ffffff shadow #000000 3px 4px 0px 0px | 3 up div.LinkContainer_LinkContainer__Kk5IQ.grid bg #ffffff shadow #000000 4px 5px 0px 0px |
| How | at rest | mouse hover |

Crops: `profile-link-default.png`, `profile-link-hover.png`.

#### profile-badge

Verified badge. The verified badge on the official profile.

Page: profile. Selector: `button "Verified"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 62.2 x 24 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Link Sans Product 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.75 |
| Text node | span.text-xs.font-product: Link Sans Product 12px/18px 400, #000000 @ 0.75 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `profile-badge-default.png`.

### Sign-in wall (not submitted)

#### login-title

Login title. The signed-out login wall. Nothing was submitted.

Page: login. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 720 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Link Sans Display 32px/36px 800 |
| Letter spacing | -0.64px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `login-title-default.png`.

#### login-field

Login field. The email or username field. Focused only. Nothing was typed and the form was not submitted.

Page: login. Selector: `input username`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 478 x 54.84 | = |
| Padding | 24px 16px 8px 16px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = |
| Font | Link Sans Product 16px/22.8571px 400 | = |
| Letter spacing | 0.32px | = |
| Colour | #040403 @ 0.898 | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, -webkit-backdrop-filter, backdrop-filter 0.075s cubic-bezier(0, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #000000 @ 0, opacity 1 | = |
| Painted layers | input.text-body-small-regular.w-full 478.0x54.8 outline 2px solid #000000 @ 0 offset 2px | = |
| Ancestor paint | 1 up div.group/field.relative bg #ffffff | 1 up div.group/field.relative bg #ffffff shadow #fbfaf9 0px 0px 0px 0px, #040403 @ 0.898 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field |

Crops: `login-field-default.png`, `login-field-focused.png`.

#### login-continue

Continue. The primary continue button. Measured, never pressed.

Page: login. Selector: `button "Continue"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 480 x 56 | = | - | 470.4 x 54.88 |
| Padding | 0px 20px | = | - | = |
| Gap | 4px | = | - | = |
| Border | none | = | - | = |
| Radius | 9999px | = | - | = |
| Background | #e5e4e1 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Link Sans Product 16px/24px 500 | = | - | = |
| Letter spacing | 0.16px | = | - | = |
| Colour | #040403 @ 0.18 | = | - | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | - | = |
| Cursor | default | = | - | = |
| ::before | 480px x 56px, absolute, bg #ffffff @ 0.14, radius 9999px | = | - | 480px x 56px, absolute, bg #ffffff @ 0.2, radius 9999px |
| Painted layers | button.inline-flex.items-center 480.0x56.0 bg #e5e4e1 r 9999px; button::before.inline-flex.items-center 480pxx56px bg #ffffff @ 0.14 r 9999px | = | - | button.inline-flex.items-center 470.4x54.9 bg #e5e4e1 r 9999px; button::before.inline-flex.items-center 480pxx56px bg #ffffff @ 0.2 r 9999px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | - | focus failed: keyboard focus did not reach the element | - |
| Transform | - | - | - | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `login-continue-default.png`, `login-continue-hover.png`, `login-continue-pressed.png`.

#### login-google

Continue with Google. The Google button on the signed-out wall. Measured, never pressed.

Page: login. Selector: `button "Continue with Google"`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 480 x 56 | = |
| Padding | 0px 20px | = |
| Gap | 4px | = |
| Border | 1px solid #040403 @ 0.14 | = |
| Radius | 9999px | = |
| Background | transparent | #040403 @ 0.05 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Link Sans Product 16px/24px 500 | = |
| Letter spacing | 0.16px | = |
| Colour | #040403 @ 0.898 | = |
| Text node | span: Link Sans Product 16px/24px 500, #040403 @ 0.898, ls 0.16px | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 24 x 24, colour #040403 @ 0.898 | = |
| Painted layers | button.inline-flex.items-center 480.0x56.0 border T:1px solid #040403 @ 0.14 / R:1px solid #040403 @ 0.14 / B:1px solid #040403 @ 0.14 / L:1px solid #040403 @ 0.14 r 9999px | button.inline-flex.items-center 480.0x56.0 bg #040403 @ 0.05 border T:1px solid #040403 @ 0.14 / R:1px solid #040403 @ 0.14 / B:1px solid #040403 @ 0.14 / L:1px solid #040403 @ 0.14 r 9999px |
| How | at rest | mouse hover |

Crops: `login-google-default.png`, `login-google-hover.png`.

#### login-signup

Sign up link. The sign-up link on the login wall. Measured, never followed.

Page: login. Selector: `Sign up`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 51.69 x 19.98 | = |
| Padding | 0px | = |
| Gap | 4px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Link Sans Product 14px/20px 400 | = |
| Letter spacing | 0.28px | = |
| Colour | #7008e7 | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `login-signup-default.png`, `login-signup-hover.png`.

### Mobile (390 wide)

#### m-navbar

Mobile nav. The marketing nav at 390 wide, with the menu toggle.

Page: home. Selector: `nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 89.22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Linksans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e2330 |
| Text node | a.inline-flex.items-center: Linksans 11.7px/17.55px 400, #1e2330 |
| Transition | transform, translate, scale, rotate 0.3s cubic-bezier(0, 0, 0.2, 1) |
| Icon | 0 x 0, colour #000000 |
| Painted layers | div.relative.mx-auto 362.7x65.8 bg #ffffff border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 9999px; div.pointer-events-none.absolute 0.0x0.0 bg #ffffff border T:1px solid #000000 @ 0.04 / R:1px solid #000000 @ 0.04 / B:1px solid #000000 @ 0.04 / L:1px solid #000000 @ 0.04 r 9.75px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 24px 60px 0px; a.inline-flex.items-center 73.3x46.4 bg #eff0ec r 7.8px; a.inline-flex.items-center 110.2x46.4 bg #1e2330 r 9999px; span.absolute.left-0 16.0x1.5 bg #1e2330 r 3.35544e+07px; span.absolute.left-0 16.0x1.5 bg #1e2330 r 3.35544e+07px |
| How | at rest |

Crops: `m-navbar-default.png`.

#### m-menu

Menu toggle. The mobile menu button. Its name is an aria-label. Opened once for the menu link.

Page: home. Selector: `button[aria-label="Toggle menu"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48.23 x 48.23 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #eff0ec | = | #eff0ec |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = |
| Font | Linksans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e2330 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.absolute.left-0 16.0x1.5 bg #1e2330 r 3.35544e+07px; span.absolute.left-0 16.0x1.5 bg #1e2330 r 3.35544e+07px; span.absolute.left-0 16.0x1.5 bg #1e2330 r 3.35544e+07px | button.hidden.items-center 48.2x48.2 bg #eff0ec r 9999px; span.absolute.left-0 16.0x1.5 bg #1e2330 r 3.35544e+07px; span.absolute.left-0 16.0x1.5 bg #1e2330 r 3.35544e+07px; span.absolute.left-0 16.0x1.5 bg #1e2330 r 3.35544e+07px | button.hidden.items-center 48.2x48.2 r 9999px outline 1px auto #e59700 offset 0px; span.absolute.left-0 16.0x1.5 bg #1e2330 r 3.35544e+07px; span.absolute.left-0 16.0x1.5 bg #1e2330 r 3.35544e+07px; span.absolute.left-0 16.0x1.5 bg #1e2330 r 3.35544e+07px | button.hidden.items-center 48.2x48.2 bg #eff0ec r 9999px; span.absolute.left-0 16.0x1.5 bg #1e2330 r 3.35544e+07px; span.absolute.left-0 16.0x1.5 bg #1e2330 r 3.35544e+07px; span.absolute.left-0 16.0x1.5 bg #1e2330 r 3.35544e+07px |
| Ancestor paint | 1 up div.relative.mx-auto bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-menu-default.png`, `m-menu-hover.png`, `m-menu-focus-visible.png`, `m-menu-pressed.png`.

#### m-signup

Mobile signup. The signup control at 390 wide. Measured, never followed.

Page: home. Selector: `signup`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 110.22 x 46.39 |
| Padding | 13.689px 18.525px 15.171px 18.525px |
| Border | none |
| Radius | 9999px |
| Background | #1e2330 |
| Box shadow | none |
| Outline | none |
| Font | Linksans 11.7px/17.55px 400 |
| Letter spacing | 0.117px |
| Colour | #ffffff |
| Transition | background-color, transform 0.15s cubic-bezier(0, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | a.inline-flex.items-center 110.2x46.4 bg #1e2330 r 9999px |
| How | at rest |

Crops: `m-signup-default.png`.

#### m-menu-panel

Mobile menu link. A link inside the opened mobile menu. Measured, never followed.

Page: home. Selector: `a "Pricing"`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 390 x 64 |
| Padding | 20px 16px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Linksans 20px/24px 500 |
| Letter spacing | -0.4px |
| Colour | #1e2330 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 16 x 16, colour #a8a29e |
| How | menu held open |

Crops: `m-menu-panel-opened.png`.

## Transitions declared in the readable stylesheets

Transitions the CSSOM could read on each captured page. The per-state Transition rows above are the computed values.
