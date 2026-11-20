# Component measurements

Computed styles read from cushion.so on 2026-11-12 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the home, /pricing, /updates, /blog, /slack-alternative and /terms (the Mobile group on the home) — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### nav-bar

Nav bar. The 72px sticky top nav (Pricing / Updates / Blog / Log in / Sign up).

Page: home. Selector: `nav.sticky`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Text node | a.inline-flex.items-center: ui-sans-serif 16px/16px 500, #1f1f1f |
| Transition | none |
| Icon | 112 x 25, colour #1f1f1f |
| Painted layers | a.inline-flex.items-center 91.8x40.0 bg #00a6f4 r 8px |
| Ancestor paint | 1 up body.bg-gray-2.text-gray-12 bg #f5f5f5 |
| How | at rest |

Crops: `nav-bar-default.png`.

#### nav-logo

Nav logo. The Cushion wordmark link.

Page: home. Selector: `nav a`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 112 x 25 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Transition | none |
| Cursor | pointer |
| Icon | 112 x 25, colour #1f1f1f |
| How | at rest |

Crops: `nav-logo-default.png`.

#### nav-link

Nav link. A 40px nav link (Pricing); measured, never followed.

Page: home. Selector: `nav a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 87.52 x 40 | = | = | 85.77 x 39.2 |
| Padding | 0px 18px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #000000 @ 0.05 | = | #000000 @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 16px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1f1f1f | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.inline-flex.items-center 87.5x40.0 bg #000000 @ 0.05 r 8px | a.inline-flex.items-center 87.5x40.0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 85.8x39.2 bg #000000 @ 0.05 r 8px |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Login link. "Log in" — the header auth link; measured, never followed.

Page: home. Selector: `nav a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 80.63 x 40 | = | = | 79.01 x 39.2 |
| Padding | 0px 18px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #000000 @ 0.05 | = | #000000 @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 16px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1f1f1f | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.inline-flex.items-center 80.6x40.0 bg #000000 @ 0.05 r 8px | a.inline-flex.items-center 80.6x40.0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 79.0x39.2 bg #000000 @ 0.05 r 8px |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### signup-btn

Sign-up button. "Sign up" — the 91x40 #00a6f4 nav CTA; measured, never followed.

Page: home. Selector: `nav a.signup`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 91.8 x 40 | = | = | 89.96 x 39.2 |
| Padding | 0px 18px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #00a6f4 | #0085c3 | = | #0085c3 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 16px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 91.8x40.0 bg #00a6f4 r 8px | a.inline-flex.items-center 91.8x40.0 bg #0085c3 r 8px | a.inline-flex.items-center 91.8x40.0 bg #00a6f4 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 90.0x39.2 bg #0085c3 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-btn-default.png`, `signup-btn-hover.png`, `signup-btn-focus-visible.png`, `signup-btn-pressed.png`.

#### cta-start

Get-started CTA. "Get started" — the 119x44 #00a6f4 primary CTA; measured, never followed.

Page: home. Selector: `a.cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 119.83 x 44 | = | = | 117.43 x 43.12 |
| Padding | 0px 18px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #00a6f4 | #0085c3 | = | #0085c3 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 119.8x44.0 bg #00a6f4 r 12px | a.inline-flex.items-center 119.8x44.0 bg #0085c3 r 12px | a.inline-flex.items-center 119.8x44.0 bg #00a6f4 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 117.4x43.1 bg #0085c3 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-start-default.png`, `cta-start-hover.png`, `cta-start-focus-visible.png`, `cta-start-pressed.png`.

#### cta-human

Secondary CTA. "Talk to a human" — the 154x44 #fcfcfc secondary CTA; measured, never followed.

Page: home. Selector: `a.cta-secondary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 154.14 x 44 | = | = | 151.06 x 43.12 |
| Padding | 0px 18px | = | = | = |
| Border | 1px solid #212121 @ 0.1 | = | = | = |
| Radius | 12px | = | = | = |
| Background | #fcfcfc | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1f1f1f | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 154.1x44.0 bg #fcfcfc border T:1px solid #212121 @ 0.1 / R:1px solid #212121 @ 0.1 / B:1px solid #212121 @ 0.1 / L:1px solid #212121 @ 0.1 r 12px | a.inline-flex.items-center 154.1x44.0 bg #f5f5f5 border T:1px solid #212121 @ 0.1 / R:1px solid #212121 @ 0.1 / B:1px solid #212121 @ 0.1 / L:1px solid #212121 @ 0.1 r 12px | a.inline-flex.items-center 154.1x44.0 bg #fcfcfc border T:1px solid #212121 @ 0.1 / R:1px solid #212121 @ 0.1 / B:1px solid #212121 @ 0.1 / L:1px solid #212121 @ 0.1 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 151.1x43.1 bg #f5f5f5 border T:1px solid #212121 @ 0.1 / R:1px solid #212121 @ 0.1 / B:1px solid #212121 @ 0.1 / L:1px solid #212121 @ 0.1 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-human-default.png`, `cta-human-hover.png`, `cta-human-focus-visible.png`, `cta-human-pressed.png`.

#### footer

Footer. The 1240x184 link-columns footer band.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1240 x 184 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Text node | h4.text-gray-12: ui-sans-serif 16px/24px 400, #1f1f1f |
| Transition | none |
| Icon | 89.59 x 20, colour #1f1f1f |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer link (Privacy); measured, never followed.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 52.86 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | ui-sans-serif 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #858585 | #1f1f1f | = | #1f1f1f |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.hover:text-gray-12 52.9x18.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Home

#### hero-h1

Hero heading. "Work messaging that keeps your team organised" — the 60px Inter Tight hero.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 60px/60px 600 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-sub

Hero subhead. "Cushion is the async messaging app for small, distributed teams."

Page: home. Selector: `hero p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 20px/28px 500 |
| Letter spacing | normal |
| Colour | #858585 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### problem-h2

Problem heading. "Workspace messaging is broken" — the animated problem statement.

Page: home. Selector: `h2.max-w-prose`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 728 x 562 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 36px/54px 600 |
| Letter spacing | -0.36px |
| Colour | #1f1f1f |
| Text node | span.block: ui-sans-serif 36px/54px 600, #1f1f1f, ls -0.36px |
| Transition | none |
| Icon | 31.5 x 31.5, colour #1f1f1f |
| Painted layers | span.relative.inline-flex 49.1x33.7 bg oklch(0.637 0.237 25.331) r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px; div.pointer-events-none.select-none 167.9x54.0 image linear-gradient(to right in oklab, #000000 @ 0 0%, #fafafa 100%); div.h-[2px].w-[16px] 16.0x2.0 bg #d1d1d1 r 3.35544e+07px; div.h-[2px].w-[16px] 16.0x2.0 bg #d1d1d1 r 3.35544e+07px; div.h-[2px].w-[16px] 16.0x2.0 bg #d1d1d1 r 3.35544e+07px; div.h-[2px].w-[16px] 16.0x2.0 bg #d1d1d1 r 3.35544e+07px |
| How | at rest |

Crops: `problem-h2-default.png`.

#### feature-h2

Feature heading. "Collaborate without the chaos" — the feature section heading.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 608 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 36px/40px 600 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Transition | none |
| How | at rest |

Crops: `feature-h2-default.png`.

#### mock-frame

App mock frame. The embedded "Acme Inc" inbox product mock.

Page: home. Selector: `app mock frame`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 720 |
| Padding | 0px |
| Border | 1px solid #212121 @ 0.1 |
| Radius | 12px 12px 0px 0px |
| Background | #fcfcfc |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Text node | div.size-5.grid: ui-sans-serif 10px/15px 600, oklch(0.398 0.07 227.392) |
| Transition | none |
| Icon | 16 x 16, colour #1f1f1f |
| Painted layers | div.w-full.h-full 1280.0x720.0 bg #fcfcfc border T:1px solid #212121 @ 0.1 / R:1px solid #212121 @ 0.1 / B:1px solid #212121 @ 0.1 / L:1px solid #212121 @ 0.1 r 12px 12px 0px 0px; div.bg-gray-1.border-r 226.0x718.0 bg #fafafa border R:1px solid #212121 @ 0.1 r 6px 0px 0px; div.size-5.grid 20.0x20.0 bg oklch(0.917 0.08 205.041) r 6px; button.inline-flex.items-center 209.0x32.0 bg #fcfcfc border T:1px solid #212121 @ 0.1 / R:1px solid #212121 @ 0.1 / B:1px solid #212121 @ 0.1 / L:1px solid #212121 @ 0.1 r 6px; div.flex.items-center 20.0x20.0 bg #ebebeb r 6px; div.inline-flex.items-center 31.8x20.0 bg #ebebeb r 6px |
| How | at rest |

Crops: `mock-frame-default.png`.

#### mock-newpost

Mock: New post. The mock inbox "New post" button (209x32).

Page: home. Selector: `mock button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 209 x 32 | = | = | 204.82 x 31.36 |
| Padding | 0px 10px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #212121 @ 0.1 | = | = | = |
| Radius | 6px | = | = | = |
| Background | #fcfcfc | = | = | #f5f5f5 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1f1f1f | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | pointer |
| Icon | 16 x 16, colour #1f1f1f | = | = | 15.68 x 15.68, colour #1f1f1f |
| Painted layers | button.inline-flex.items-center 209.0x32.0 bg #fcfcfc border T:1px solid #212121 @ 0.1 / R:1px solid #212121 @ 0.1 / B:1px solid #212121 @ 0.1 / L:1px solid #212121 @ 0.1 r 6px | = | button.inline-flex.items-center 209.0x32.0 bg #fcfcfc border T:1px solid #212121 @ 0.1 / R:1px solid #212121 @ 0.1 / B:1px solid #212121 @ 0.1 / L:1px solid #212121 @ 0.1 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.items-center 204.8x31.4 bg #f5f5f5 border T:1px solid #212121 @ 0.1 / R:1px solid #212121 @ 0.1 / B:1px solid #212121 @ 0.1 / L:1px solid #212121 @ 0.1 r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mock-newpost-default.png`, `mock-newpost-hover.png`, `mock-newpost-focus-visible.png`, `mock-newpost-pressed.png`.

#### mock-channel

Mock: channel. A mock sidebar channel button (209x32).

Page: home. Selector: `mock channel button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 209 x 32 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | = | = | #f5f5f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | ui-sans-serif 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1f1f1f | = | = | = |
| Text node | span.shrink-0.text-base: ui-sans-serif 16px/24px 500, #1f1f1f | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.w-full.flex 209.0x32.0 r 6px outline 1px auto #005fcc offset 0px | button.w-full.flex 209.0x32.0 bg #f5f5f5 r 6px |

Crops: `mock-channel-default.png`, `mock-channel-hover.png`, `mock-channel-focus-visible.png`, `mock-channel-pressed.png`.

#### mock-post

Mock: post card. A mock post card in the inbox mock (606x108).

Page: home. Selector: `article.group`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 606 x 108 |
| Padding | 16px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Text node | span.text-sm.font-medium: ui-sans-serif 14px/20px 500, #1f1f1f |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.5s cubic-bezier(0.4, 0, 0.2, 1) |
| Painted layers | span.px-1.5.rounded-md 87.0x18.0 bg #ebebeb r 6px |
| Ancestor paint | 1 up div.relative.z-10 bg #fafafa |
| How | at rest |

Crops: `mock-post-default.png`.

#### mock-post-bar

Mock: post footer. The mock post action bar ("Save for later" / "Post").

Page: home. Selector: `mock footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 655.08 x 48 |
| Padding | 0px 12px |
| Gap | 6px |
| Border | T: 1px solid #212121 @ 0.1; R: none; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Text node | span.text-base.leading-[1lh]: ui-sans-serif 16px/20px 500, #1f1f1f |
| Transition | none |
| Icon | 16 x 16, colour #1f1f1f |
| Painted layers | footer.flex.items-center 655.1x48.0 border T:1px solid #212121 @ 0.1; button.inline-flex.items-center 187.9x32.0 bg #fcfcfc border T:1px solid #212121 @ 0.1 / R:1px solid #212121 @ 0.1 / B:1px solid #212121 @ 0.1 / L:1px solid #212121 @ 0.1 r 6px; button.inline-flex.items-center 201.8x32.0 bg #fcfcfc border T:1px solid #212121 @ 0.1 / R:1px solid #212121 @ 0.1 / B:1px solid #212121 @ 0.1 / L:1px solid #212121 @ 0.1 r 6px; div.bg-pink-300.size-5 20.0x20.0 bg oklch(0.823 0.12 346.018) r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; div.bg-blue-300.size-5 20.0x20.0 bg oklch(0.809 0.105 251.813) r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; div.bg-green-300.size-5 20.0x20.0 bg oklch(0.871 0.15 154.449) r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Ancestor paint | 1 up div.bg-background.aspect-video bg #fcfcfc shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px |
| How | at rest |

Crops: `mock-post-bar-default.png`.

#### cmp-h1

Comparison heading. "The best Slack alternative for async teams".

Page: slackalt. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 60px/60px 600 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Transition | none |
| How | at rest |

Crops: `cmp-h1-default.png`.

#### cmp-article

Comparison section. A comparison page section/article.

Page: slackalt. Selector: `article`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 366 x 148 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | #fcfcfc |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 0px 0px 1px, #000000 @ 0.05 0px 1px 2px 0px |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Text node | p.text-sm.font-medium: ui-sans-serif 14px/20px 500, #1f1f1f |
| Transition | none |
| Painted layers | article.flex.flex-col 366.0x148.0 bg #fcfcfc r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 0px 0px 1px, #000000 @ 0.05 0px 1px 2px 0px; div.relative.grid 24.0x24.0 bg oklch(0.715 0.143 215.221) r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fcfcfc 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; div.absolute.bottom-0 6.0x6.0 bg oklch(0.723 0.219 149.579) r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fcfcfc 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; div.bg-gray-6.h-2 167.0x8.0 bg #d1d1d1 r 3.35544e+07px; div.bg-gray-4.h-2 300.6x8.0 bg #e0e0e0 r 3.35544e+07px; div.bg-gray-4.h-2 200.4x8.0 bg #e0e0e0 r 3.35544e+07px |
| How | at rest |

Crops: `cmp-article-default.png`.

### Pricing

#### pricing-h2

Pricing heading. "Everything you need for just $8/mo/user."

Page: pricing. Selector: `pricing h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 579 x 160 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 36px/40px 600 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Transition | none |
| Painted layers | mark.bg-accent/30.rounded-md 188.8x43.0 bg #00a6f4 @ 0.3 r 6px |
| How | at rest |

Crops: `pricing-h2-default.png`.

#### plan-panel

Plan panel. The single-plan panel ($8/mo/user + 30-day trial copy).

Page: pricing. Selector: `div.bg-gray-1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1240 x 354 |
| Padding | 24px |
| Gap | 32px |
| Border | 1px solid #212121 @ 0.1 |
| Radius | 16px |
| Background | #fafafa |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Text node | h2.text-3xl.lg:text-4xl: ui-sans-serif 36px/40px 600, #1f1f1f |
| Transition | none |
| Icon | 20 x 20, colour #00a6f4 |
| Painted layers | div.flex.flex-col 1240.0x354.0 bg #fafafa border T:1px solid #212121 @ 0.1 / R:1px solid #212121 @ 0.1 / B:1px solid #212121 @ 0.1 / L:1px solid #212121 @ 0.1 r 16px; mark.bg-accent/30.rounded-md 188.8x43.0 bg #00a6f4 @ 0.3 r 6px; button.inline-flex.items-center 143.8x56.0 bg #00a6f4 r 16px |
| How | at rest |

Crops: `plan-panel-default.png`.

#### pricing-cta

Pricing CTA. "Get started" — the pricing-page CTA; measured, never followed.

Page: pricing. Selector: `pricing cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 143.81 x 56 | = | = | 140.94 x 54.88 |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | #00a6f4 | #0085c3 | = | #0085c3 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 20px/28px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | pointer | = | pointer |
| Painted layers | button.inline-flex.items-center 143.8x56.0 bg #00a6f4 r 16px | button.inline-flex.items-center 143.8x56.0 bg #0085c3 r 16px | button.inline-flex.items-center 143.8x56.0 bg #00a6f4 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.items-center 140.9x54.9 bg #0085c3 r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pricing-cta-default.png`, `pricing-cta-hover.png`, `pricing-cta-focus-visible.png`, `pricing-cta-pressed.png`.

#### faq-item

FAQ item. A FAQ accordion row ("How's this different from Slack?"); opened and closed locally.

Page: pricing. Selector: `button[aria-expanded]`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 1238 x 72 | = |
| Padding | 0px 16px | = |
| Border | T: none; R: none; B: 1px solid #212121 @ 0.1; L: none | = |
| Radius | 0px | = |
| Background | #fcfcfc | #ebebeb |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #1f1f1f | = |
| Text node | h2.font-medium.text-gray-12: ui-sans-serif 18px/28px 500, #1f1f1f | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #1f1f1f | = |
| Painted layers | button.w-full.flex 1238.0x72.0 bg #fcfcfc border B:1px solid #212121 @ 0.1 | button.w-full.flex 1238.0x72.0 bg #ebebeb border B:1px solid #212121 @ 0.1 |
| How | at rest | own toggle |

Crops: `faq-item-default.png`, `faq-item-opened.png`.

### Updates

#### update-entry

Update entry. A changelog entry (date + items, ~1024x1719).

Page: updates. Selector: `article.md:flex-row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 1719.88 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Text node | span.text-sm.text-gray-9: ui-sans-serif 14px/20px 400, #8f8f8f |
| Transition | none |
| How | at rest |

Crops: `update-entry-default.png`.

#### update-h2

Update title. A release title ("Post Redesign, Slack Sync Upgrades, and more").

Page: updates. Selector: `article h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 840 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 24px/32px 600 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `update-h2-default.png`.

#### update-h3

Update item. A release item heading.

Page: updates. Selector: `article h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 840 x 35.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 22px/35.2px 600 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Transition | none |
| How | at rest |

Crops: `update-h3-default.png`.

### Blog

#### blog-featured

Featured post. The featured blog row (1240x339); measured, never followed.

Page: blog. Selector: `article`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1240 x 339.75 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | ui-sans-serif 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #1f1f1f | = | - | = |
| Text node | span.text-xs.text-gray-11: ui-sans-serif 12px/16px 400, #666666 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `blog-featured-default.png`, `blog-featured-hover.png`, `blog-featured-pressed.png`.

#### blog-card

Blog card. A 397x403 post card; measured, never followed.

Page: blog. Selector: `article.rounded-xl`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 397.33 x 403.5 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 12px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | ui-sans-serif 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #1f1f1f | = | - | = |
| Text node | span.text-xs.text-gray-11: ui-sans-serif 12px/16px 400, #666666 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `blog-card-default.png`, `blog-card-hover.png`, `blog-card-pressed.png`.

#### blog-card-title

Card title. A post card title (text-lg).

Page: blog. Selector: `article h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 604 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 30px/36px 600 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `blog-card-title-default.png`.

### Legal

#### legal-h1

Legal heading. "Terms of Service" — the legal page heading.

Page: terms. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 736 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 36px/40px 700 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Transition | none |
| How | at rest |

Crops: `legal-h1-default.png`.

#### legal-body

Legal paragraph. A body paragraph of the terms text.

Page: terms. Selector: `legal p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 736 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/26px 400 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Transition | none |
| How | at rest |

Crops: `legal-body-default.png`.

### Mobile (390 wide)

#### m-nav-bar

Mobile nav.

Page: home. Selector: `nav at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fcfcfc |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Transition | none |
| Icon | 112 x 25, colour #1f1f1f |
| Painted layers | nav.sticky.top-0 390.0x72.0 bg #fcfcfc; a.inline-flex.items-center 0.0x0.0 bg #00a6f4 r 8px |
| Ancestor paint | 1 up body.bg-gray-2.text-gray-12 bg #f5f5f5 |
| How | at rest |

Crops: `m-nav-bar-default.png`.

#### m-hero-h1

Mobile hero. The hero at 390px.

Page: home. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 192 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 48px/48px 600 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-cta-start

Mobile CTA. "Get started" at 390px; measured, never followed.

Page: home. Selector: `cta at 390`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 350 x 44 | = | = | 343 x 43.12 |
| Padding | 0px 18px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #00a6f4 | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 350.0x44.0 bg #00a6f4 r 12px | = | a.inline-flex.items-center 350.0x44.0 bg #00a6f4 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 343.0x43.1 bg #00a6f4 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-cta-start-default.png`, `m-cta-start-hover.png`, `m-cta-start-focus-visible.png`, `m-cta-start-pressed.png`.

## Transitions declared in the readable stylesheets

cushion.so is a light-only Tailwind marketing site; the embedded "Acme Inc" inbox is a marketing mock, not the authenticated app. Every value above is the computed value the page paints.

- blog: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- home: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- pricing: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- slackalt: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- updates: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`
