# Fernand component measurements

Computed styles read from getfernand.com, app.getfernand.com and help.getfernand.com on 2026-11-15 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the public surfaces — the light-only marketing pages, the signed-out /auth/login and /create forms of the app, and the docs site in light plus the dark theme its own "Switch to dark mode" link paints — with any consent layer hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Site chrome

#### mkt-header

Site header. The fixed top bar: wordmark, About us / Pricing / Log in nav links, the "Book a demo" Cal.com action and the "Start for free" button.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 71.5 |
| Padding | 12px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #191e5a @ 0 0px -1px 0px 0px inset |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Text node | a: Inter 14px/14px 500, #6f7b96 |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 35 x 45.5, colour #0000ee |
| Painted layers | header.transit.transit--slow 1440.0x71.5 shadow #191e5a @ 0 0px -1px 0px 0px inset; a 115.0x30.0 bg #ffffff r 6px shadow #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px; a 115.0x30.0 bg #00a0ff r 6px |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The Fernand mark-and-wordmark in the header, linking home.

Page: home. Selector: `header a:first`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 35 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| Cursor | pointer |
| Icon | 35 x 45.5, colour #0000ee |
| Ancestor paint | 3 up header.transit.transit--slow shadow #191e5a @ 0 0px -1px 0px 0px inset |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-link

Nav link. A marketing header nav link (About us); measured, never followed.

Page: home. Selector: `header nav a About us`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 84 x 37 | = | = | = |
| Padding | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #121213 offset 0.96875px | = |
| Font | Inter 14px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6f7b96 | #00a0ff | = | #3f8bc4 |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 84.0x37.0 outline 1px auto #121213 offset 0.96875px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Log in link. The "Log in" nav link to app.getfernand.com; measured, never followed.

Page: home. Selector: `header a Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 62 x 37 | = | = | = |
| Padding | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #121213 offset 0.96875px | = |
| Font | Inter 14px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6f7b96 | #01a0ff | = | #029ffe |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 62.0x37.0 outline 1px auto #121213 offset 0.96875px | = |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-demo

Book a demo action. The "Book a demo" header action — a Cal.com scheduler link (data-cal-link, role="button"); measured, never activated.

Page: home. Selector: `header li.button__demo a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 115 x 30 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px | = | = | = |
| Outline | none | = | 1px auto #1e2024 offset 0px | = |
| Font | Inter 14px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6f7b96 | #5a657f | #6e7a95 | #5b6680 |
| Transition | all 1.5s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a 115.0x30.0 bg #ffffff r 6px shadow #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px | = | a 115.0x30.0 bg #ffffff r 6px shadow #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px outline 1px auto #1e2024 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-demo-default.png`, `nav-demo-hover.png`, `nav-demo-focus-visible.png`, `nav-demo-pressed.png`.

#### nav-cta

Header CTA. The "Start for free" header button linking to the signup; measured, never followed.

Page: home. Selector: `header li.button__header a Start for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 115 x 30 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #00a0ff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #161616 offset 0.96875px | = |
| Font | Inter 14px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a 115.0x30.0 bg #00a0ff r 6px | = | a 115.0x30.0 bg #00a0ff r 6px outline 1px auto #161616 offset 0.96875px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### hero-eyebrow

Update eyebrow pill. The dated changelog pill above the masthead ("Oct. 27 — Dodo Payments integration"); measured, never followed.

Page: home. Selector: `a.hero__eyebrow`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 259 x 30 | = |
| Padding | 5px 12px 5px 5px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 40px | = |
| Background | #ffffff | = |
| Box shadow | #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px | = |
| Outline | none | = |
| Font | Inter 13px/13px 500 | = |
| Letter spacing | normal | = |
| Colour | #1a2035 | #009ffe |
| Text node | span.hero__eyebrow-date: Inter 12px/12px 600, #00a0ff | = |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = |
| Cursor | pointer | = |
| Painted layers | a.hero__eyebrow 259.0x30.0 bg #ffffff r 40px shadow #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px; span.hero__eyebrow-date 61.0x20.0 bg #e7f6ff r 40px | = |
| How | at rest | mouse hover |

Crops: `hero-eyebrow-default.png`, `hero-eyebrow-hover.png`.

#### hero-h1

Hero headline. "The free customer support platform for SaaS teams" — the 38px display heading.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1290 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 38px/48px 400 |
| Letter spacing | normal |
| Colour | #1a2035 |
| Transition | all 1.5s cubic-bezier(0.19, 1, 0.22, 1) |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-sub

Hero lede. The hero standfirst under the masthead.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 84.14 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 17px/28.05px 400 |
| Letter spacing | normal |
| Colour | #717583 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-cta

Hero CTA. The dark "Start for free" hero button (8px radius); measured, never followed.

Page: home. Selector: `a.hero__cta--primary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 170 x 49 | = | = | = |
| Padding | 13px 20px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #1a2035 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #1a2035 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #151515 offset 0.96875px | = |
| Font | Inter 15px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.hero__cta--primary 170.0x49.0 bg #1a2035 border T:1px solid #1a2035 / R:1px solid #1a2035 / B:1px solid #1a2035 / L:1px solid #1a2035 r 8px; kbd 22.0x21.0 bg #3d4259 r 4px | = | a.hero__cta--primary 170.0x49.0 bg #1a2035 border T:1px solid #1a2035 / R:1px solid #1a2035 / B:1px solid #1a2035 / L:1px solid #1a2035 r 8px outline 1px auto #151515 offset 0.96875px; kbd 22.0x21.0 bg #3d4259 r 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-cta2

Hero demo link. The "Book a demo" secondary action in the hero — a Cal.com link; measured, never activated.

Page: home. Selector: `a.hero__cta--demo`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 137 x 48 | = | = | = |
| Padding | 13px 20px | = | = | = |
| Border | 1px solid #123769 @ 0.12 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px | = | = | = |
| Outline | none | = | 1px auto #101011 offset 0px | = |
| Font | Inter 15px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1a2035 | = | = | = |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.hero__cta--demo 137.0x48.0 bg #ffffff border T:1px solid #123769 @ 0.12 / R:1px solid #123769 @ 0.12 / B:1px solid #123769 @ 0.12 / L:1px solid #123769 @ 0.12 r 8px shadow #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px | = | a.hero__cta--demo 137.0x48.0 bg #ffffff border T:1px solid #123769 @ 0.12 / R:1px solid #123769 @ 0.12 / B:1px solid #123769 @ 0.12 / L:1px solid #123769 @ 0.12 r 8px shadow #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px outline 1px auto #101011 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta2-default.png`, `hero-cta2-hover.png`, `hero-cta2-focus-visible.png`, `hero-cta2-pressed.png`.

#### hero-demo-btn

Demo button. The "Watch a 2 minute demo" play button — a local UI toggle opening the video dialog. The opened state measured the dialog it mounts.

Page: home. Selector: `button.hero-demo__btn`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 240 x 50 | = | = | = | = |
| Padding | 16px 20px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 40px | = | = | = | = |
| Background | #ffffff | = | = | = | = |
| Box shadow | #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Inter 15px/15px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #3d4259 | = | = | = | = |
| Transition | transform 0.16s cubic-bezier(0.23, 1, 0.32, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 18 x 18, colour #3d4259 | = | = | = | = |
| Painted layers | button.hero-demo__btn 240.0x50.0 bg #ffffff r 40px shadow #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px | = | = | = | = |
| Ancestor paint | 2 up div.hero-demo__frame shadow #1b3541 @ 0.12 0px 0px 30px 10px, #0e1117 @ 0 0px 0px 2px 2px | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | clicked "Watch a 2 minute demo" to open the video dialog |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 0) | = |

Crops: `hero-demo-btn-default.png`, `hero-demo-btn-hover.png`, `hero-demo-btn-focus-visible.png`, `hero-demo-btn-pressed.png`, `hero-demo-btn-opened.png`.

#### demo-dialog

Demo dialog. The video dialog mounted by the demo button — a YouTube-nocookie embed over .demo-modal__backdrop; opened by its own toggle, closed with Escape.

Page: home. Selector: `.demo-modal__dialog`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 720 |
| Padding | 0px |
| Border | none |
| Radius | 4px |
| Background | #eef2f4 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Text node | button.demo-modal__close: Inter 16px/16px 400, #3a5571 |
| Transition | none |
| Painted layers | div.demo-modal__dialog 1280.0x720.0 bg #eef2f4 r 4px; button.demo-modal__close 32.0x32.0 bg #ffffff r 100% shadow #000000 @ 0.1 0px 5px 18px -5px, #000000 @ 0.1 0px 8px 8px -6px |
| How | at rest |

Crops: `demo-dialog-default.png`.

#### ai-setup-toggle

Install-with-AI menu button. The "Install with AI" button — an aria-haspopup="menu" trigger whose menu copies a setup prompt per agent. The opened state was measured after clicking it.

Page: home. Selector: `button.ai-setup__toggle`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 183 x 47 | = | = | 177.51 x 45.59 | = |
| Padding | 13px 20px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 8px | = | = | = | = |
| Background | transparent | #000000 @ 0.04 | = | #000000 @ 0.04 | #000000 @ 0.04 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #1a2035 offset 2px | = | = |
| Font | Inter 15px/21px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #6f7b96 | #1a2035 | = | #1a2035 | #1a2035 |
| Transition | color, background, transform 0.15s, 0.15s, 0.16s ease-out, ease-out, cubic-bezier(0.23, 1, 0.32, 1) delay 0s, 0s, 0s | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 15 x 15, colour #6f7b96 | 15 x 15, colour #1a2035 | = | 14.55 x 14.55, colour #1a2035 | 15 x 15, colour #1a2035 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | clicked the "Install with AI" button to open its menu (aria-expanded=true at save) |
| Painted layers | - | button.ai-setup__toggle 183.0x47.0 bg #000000 @ 0.04 r 8px | button.ai-setup__toggle 183.0x47.0 r 8px outline 2px solid #1a2035 offset 2px | button.ai-setup__toggle 177.5x45.6 bg #000000 @ 0.04 r 8px | button.ai-setup__toggle.is-open 183.0x47.0 bg #000000 @ 0.04 r 8px |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) | = |

Crops: `ai-setup-toggle-default.png`, `ai-setup-toggle-hover.png`, `ai-setup-toggle-focus-visible.png`, `ai-setup-toggle-pressed.png`, `ai-setup-toggle-opened.png`.

#### ai-setup-item

AI-setup menu item. One item in the Install-with-AI menu (an agent prompt to copy); the menu was opened by its own toggle; the item was never activated.

Page: home. Selector: `.ai-setup__item`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 332 x 29.59 | = |
| Padding | 7px 8px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 7px | = |
| Background | transparent | #1a2035 @ 0.043 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 13px/15.6px 500 | = |
| Letter spacing | normal | = |
| Colour | #1a2035 | = |
| Text node | span: Inter 13px/15.6px 500, #1a2035 | = |
| Transition | background, color 0.12s, 0.15s ease-out, ease-out delay 0s, 0s | = |
| Cursor | pointer | = |
| Icon | 14 x 14, colour #3a4154 | = |
| Ancestor paint | 1 up div.ai-setup__menu.is-open bg #ffffff shadow #123769 @ 0.12 0px 12px 32px 0px, #123769 @ 0.06 0px 2px 6px 0px, #123769 @ 0.08 0px 0px 0px 1px | = |
| How | at rest | mouse hover |
| Painted layers | - | a.ai-setup__item 332.0x29.6 bg #1a2035 @ 0.043 r 7px |

Crops: `ai-setup-item-default.png`, `ai-setup-item-hover.png`.

#### section-tag

Section tag pill. The small white eyebrow pill labelling each marketing section.

Page: home. Selector: `.section__tag`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 132 x 28 |
| Padding | 7px 14px |
| Gap | 7px |
| Border | none |
| Radius | 40px |
| Background | #ffffff |
| Box shadow | #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px |
| Outline | none |
| Font | Inter 13px/13px 500 |
| Letter spacing | normal |
| Colour | #1a2035 |
| Transition | none |
| Icon | 14 x 14, colour #1a2035 |
| Painted layers | span.section__tag 132.0x28.0 bg #ffffff r 40px shadow #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px |
| How | at rest |

Crops: `section-tag-default.png`.

#### channels-card

Channel card. A card in the "Consolidate all your support channels" carousel (300px, #f7fafc, 10px radius).

Page: home. Selector: `.channels__card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 300 x 256 | = |
| Padding | 24px | = |
| Border | none | = |
| Radius | 10px | = |
| Background | #f7fafc | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #131e40 | = |
| Text node | h3: Inter 18px/30px 400, #1a2035 | = |
| Transition | none | = |
| Cursor | grab | = |
| Icon | 18 x 18, colour #1a2035 | = |
| Painted layers | div.channels__card 300.0x256.0 bg #f7fafc r 10px; div.cillu__icon 36.0x36.0 bg #ffffff border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 9px | = |
| How | at rest | mouse hover |

Crops: `channels-card-default.png`, `channels-card-hover.png`.

#### channels-arrow

Carousel arrow. The channels carousel's "Scroll right" arrow button; measured, never used to page the carousel.

Page: home. Selector: `button.channels__arrow--right`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | 37.4 x 37.4 | 37.4 x 37.4 |
| Padding | 1px 6px | = | = | = |
| Border | 1px solid #e8e8f0 | = | = | = |
| Radius | 50% | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0.1 0px 2px 12px 0px | #000000 @ 0.15 0px 4px 20px 0px | = | #000000 @ 0.15 0px 4px 20px 0px |
| Outline | none | = | = | = |
| Font | Inter 16px/18.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1a2035 | = | = | = |
| Transition | opacity, transform, box-shadow 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, -22) | = | matrix(0.85, 0, 0, 0.85, 0, -22) | matrix(0.85, 0, 0, 0.85, 0, -22) |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #1a2035 | = | 13.6 x 13.6, colour #1a2035 | 13.6 x 13.6, colour #1a2035 |
| Painted layers | button.channels__arrow.channels__arrow--right 44.0x44.0 bg #ffffff border T:1px solid #e8e8f0 / R:1px solid #e8e8f0 / B:1px solid #e8e8f0 / L:1px solid #e8e8f0 r 50% shadow #000000 @ 0.1 0px 2px 12px 0px | button.channels__arrow.channels__arrow--right 44.0x44.0 bg #ffffff border T:1px solid #e8e8f0 / R:1px solid #e8e8f0 / B:1px solid #e8e8f0 / L:1px solid #e8e8f0 r 50% shadow #000000 @ 0.15 0px 4px 20px 0px | button.channels__arrow.channels__arrow--right 37.4x37.4 bg #ffffff border T:1px solid #e8e8f0 / R:1px solid #e8e8f0 / B:1px solid #e8e8f0 / L:1px solid #e8e8f0 r 50% shadow #000000 @ 0.1 0px 2px 12px 0px | button.channels__arrow.channels__arrow--right 37.4x37.4 bg #ffffff border T:1px solid #e8e8f0 / R:1px solid #e8e8f0 / B:1px solid #e8e8f0 / L:1px solid #e8e8f0 r 50% shadow #000000 @ 0.15 0px 4px 20px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | = | 0 | 0 |

Crops: `channels-arrow-default.png`, `channels-arrow-hover.png`, `channels-arrow-focus-visible.png`, `channels-arrow-pressed.png`.

#### feat-card

Feature card. A feat3 feature card in "Support finally connects with your team and product strategy" — product-mock tiles; measured, never followed.

Page: home. Selector: `.feat3__card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 416.67 x 569.61 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #ffffff | = |
| Box shadow | #f0f0f5 0px 0px 0px 1px | = |
| Outline | none | = |
| Font | Inter 16px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #131e40 | = |
| Text node | div.feat3__aavatar.feat3__aavatar--lg: Inter 14px/14px 400, #3b82f6 | = |
| Transition | none | = |
| Icon | 16 x 16, colour #858ba6 | = |
| Painted layers | div.feat3__card 416.7x569.6 bg #ffffff r 8px shadow #f0f0f5 0px 0px 0px 1px; div.feat3__ticket 280.0x68.0 bg #ffffff r 8px shadow #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px; div.feat3__aavatar.feat3__aavatar--lg 40.0x40.0 bg #dbeafe r 50%; div.feat3__tbadge 280.0x32.0 bg #ffffff @ 0.34 r 8px shadow #123769 @ 0.02 0px 1px 1px 0px, #123769 @ 0.06 0px 0px 0px 1px | = |
| How | at rest | mouse hover |

Crops: `feat-card-default.png`, `feat-card-hover.png`.

#### why-btn

Product-mock button. The "View account" primary button inside the "Build your product" product illustration — a drawn mock control, not a live action.

Page: home. Selector: `product-mock View account button`. States: .

Not found on the page at capture time.

#### why-ghost

Product-mock ghost button. The "Upgrade plan" ghost button inside the same product illustration.

Page: home. Selector: `product-mock Upgrade plan button`. States: .

Not found on the page at capture time.

#### testimonial

Testimonial. A customer quote block (22px/1.55 display copy).

Page: home. Selector: `.testimonial`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 720 x 293.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Text node | p: Inter 22px/34.1px 400, #1a2035 |
| Transition | none |
| How | at rest |

Crops: `testimonial-default.png`.

#### trusted-card

Trusted-by card. A "trusted by" customer card in the dark strip (name + company).

Page: home. Selector: `.trusted__card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 147 x 60.48 | = |
| Padding | 0px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #131e40 | = |
| Text node | strong.trusted__name: Inter 13px/16.9px 600, #ffffff | = |
| Transition | none | = |
| How | at rest | mouse hover |

Crops: `trusted-card-default.png`, `trusted-card-hover.png`.

#### int-logo

Integration logo tile. One logo tile in the "Integrates with your entire stack" grid.

Page: home. Selector: `.int-logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 28 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Transition | none |
| Cursor | pointer |
| Icon | 28 x 28, colour #131e40 |
| Ancestor paint | 1 up a.ilogo-wrap.lev-b bg #ffffff shadow #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px |
| How | at rest |

Crops: `int-logo-default.png`.

#### wpg-playground

Widget playground. The "Live chat and AI, embedded in your product" interactive widget playground — an in-page demo of the embeddable widget.

Page: home. Selector: `.wpg* playground`. States: .

Not found on the page at capture time.

#### wpg-color

Widget colour swatch. A brand-colour swatch in the widget playground (the selected one carries the double ring); clicking retints the demo widget.

Page: home. Selector: `button.wpg-color`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 22 x 22 | = | = | = |
| Padding | 1px 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 50% | = | = | = |
| Background | #00a0ff | = | = | = |
| Box shadow | #ffffff 0px 0px 0px 2px, #00a0ff 0px 0px 0px 4px | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/18.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | box-shadow 0.15s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.wpg-color 22.0x22.0 bg #00a0ff r 50% shadow #ffffff 0px 0px 0px 2px, #00a0ff 0px 0px 0px 4px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `wpg-color-default.png`, `wpg-color-hover.png`, `wpg-color-focus-visible.png`, `wpg-color-pressed.png`.

#### wpg-tab

Widget tab. A tab in the playground widget preview (Home / Chat / Articles).

Page: home. Selector: `.wpg-tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81.33 x 31 | = | - | = |
| Padding | 4px 2px | = | - | = |
| Gap | 2px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 10px/10px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #00a0ff | = | - | = |
| Text node | span: Inter 10px/10px 400, #00a0ff | = | - | = |
| Transition | color 0.2s ease | = | - | = |
| Cursor | default | = | - | = |
| Icon | 11 x 11, colour #00a0ff | = | - | = |
| Ancestor paint | 3 up div.widget-pg__widget--light.widget-pg__widget bg #ffffff shadow #123769 @ 0.16 0px 8px 32px 0px, #123769 @ 0.08 0px 0px 0px 1px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `wpg-tab-default.png`, `wpg-tab-hover.png`, `wpg-tab-pressed.png`.

#### wpg-article

Widget article row. A knowledge-base article row inside the playground widget preview.

Page: home. Selector: `.wpg-article`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 252 x 23 | = |
| Padding | 6px 11px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 11px/11px 400 | = |
| Letter spacing | normal | = |
| Colour | #2c3145 | = |
| Text node | span: Inter 11px/11px 400, #2c3145 | = |
| Transition | color 0.25s ease | = |
| Cursor | default | = |
| Icon | 8 x 8, colour #9498a5 | = |
| How | at rest | mouse hover |

Crops: `wpg-article-default.png`, `wpg-article-hover.png`.

### Fernand widget

#### launcher

Widget launcher. The Fernand chat-widget launcher on the marketing site — the product's own embeddable widget at rest (48px bubble).

Page: home. Selector: `.fernand__launcher`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 48 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 100% |
| Background | transparent |
| Box shadow | #000000 @ 0.1 0px 5px 18px -5px, #000000 @ 0.1 0px 8px 8px -6px |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| Cursor | pointer |
| Icon | 24 x 24, colour #5f667d |
| Painted layers | div.fernand__launcher.transit 48.0x48.0 r 100% shadow #000000 @ 0.1 0px 5px 18px -5px, #000000 @ 0.1 0px 8px 8px -6px; div.fernand__launcher__icon 48.0x48.0 bg #ffffff r 100% |
| How | at rest |

Crops: `launcher-default.png`.

#### launcher-panel

Widget panel. The chat-widget panel opened by its own launcher click — the product's public widget UI; never typed into.

Page: home. Selector: `.fernand__backdrop`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 400 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | radial-gradient(at right bottom, #1d2736 @ 0.1 0px, #1d2736 @ 0 70%) |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| Painted layers | div.fernand__backdrop 400.0x900.0 image radial-gradient(at right bottom, #1d2736 @ 0.1 0px, #1d2736 @ 0 70%) |
| How | at rest |

Crops: `launcher-panel-default.png`.

### Footer

#### footer-cta

Footer CTA. The "Start free. Email included." call-to-action button in the closing section; measured, never followed.

Page: home. Selector: `.footer-cta__section CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 170 x 49 | = | = | = |
| Padding | 13px 20px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #1a2035 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #1a2035 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #171717 offset 0.96875px | = |
| Font | Inter 15px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.hero__cta--primary 170.0x49.0 bg #1a2035 border T:1px solid #1a2035 / R:1px solid #1a2035 / B:1px solid #1a2035 / L:1px solid #1a2035 r 8px; kbd 22.0x21.0 bg #3d4259 r 4px | = | a.hero__cta--primary 170.0x49.0 bg #1a2035 border T:1px solid #1a2035 / R:1px solid #1a2035 / B:1px solid #1a2035 / L:1px solid #1a2035 r 8px outline 1px auto #171717 offset 0.96875px; kbd 22.0x21.0 bg #3d4259 r 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-cta-default.png`, `footer-cta-hover.png`, `footer-cta-focus-visible.png`, `footer-cta-pressed.png`.

#### footer

Footer. The page footer: sitemap columns, legal links, status/social links.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 417 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #151618 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Text node | h4: Inter 15px/15px 400, #ffffff |
| Transition | none |
| ::before | 1440px x 5px, absolute, bg #151618, radius 0px |
| Painted layers | footer 1440.0x417.0 bg #151618; footer::before 1440pxx5px bg #151618 |
| How | at rest |

Crops: none.

#### footer-link

Footer link. A footer sitemap link; measured, never followed.

Page: home. Selector: `footer a Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 194 x 25 | = | = | = |
| Padding | 5px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #131313 @ 0.99 offset 0.96875px | = |
| Font | Inter 15px/15px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.5 | #ffffff @ 0.996 | = | #ffffff @ 0.992 |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 194.0x25.0 outline 1px auto #131313 @ 0.99 offset 0.96875px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Pricing

#### pricing-eyebrow

Plan eyebrow. The blue "FREE" eyebrow over a plan price.

Page: pricing. Selector: `.pricing__eyebrow`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 580 x 12 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 12px/12px 600 |
| Letter spacing | 0.48px |
| Colour | #00a0ff |
| Transition | none |
| Ancestor paint | 2 up article.pricing__col.pricing__col--free bg #ffffff shadow #00a0ff @ 0.18 16px 22px 64px 0px, #00a0ff @ 0.4 0px 0px 0px 1px, #123769 @ 0.06 0px 8px 24px 0px |
| How | at rest |

Crops: `pricing-eyebrow-default.png`.

#### price-free

Free plan card. The $0 plan card — the blue radial-gradient fill and ringed shadow variant.

Page: pricing. Selector: `.pricing__col--free`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 636 x 573.16 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Background image | radial-gradient(115% 78% at 100% 100%, #00a0ff @ 0.34, #9fe3ff @ 0.18 46%, #ffffff @ 0 78%), none |
| Box shadow | #00a0ff @ 0.18 16px 22px 64px 0px, #00a0ff @ 0.4 0px 0px 0px 1px, #123769 @ 0.06 0px 8px 24px 0px |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Text node | span.pricing__eyebrow: Inter 12px/12px 600, #00a0ff, ls 0.48px |
| Transition | none |
| Icon | 16 x 16, colour #00a0ff |
| Painted layers | article.pricing__col.pricing__col--free 636.0x573.2 bg #ffffff image radial-gradient(115% 78% at 100% 100%, #00a0ff @ 0.34, #9fe3ff @ 0.18 46%, #ffffff @ 0 78% r 16px shadow #00a0ff @ 0.18 16px 22px 64px 0px, #00a0ff @ 0.4 0px 0px 0px 1px, #123769 @ 0.06 0px 8px 24px 0px; div.pricing__line 636.0x44.6 border T:1px solid #f1f3f6; div.pricing__line 636.0x44.6 border T:1px solid #f1f3f6; div.pricing__line 636.0x44.6 border T:1px solid #f1f3f6; div.pricing__line 636.0x44.6 border T:1px solid #f1f3f6; div.pricing__line 636.0x44.6 border T:1px solid #f1f3f6 |
| How | at rest |

Crops: `price-free-default.png`.

#### price-paid

Paid plan card. The paid plan card ($29 per active human per month).

Page: pricing. Selector: `.pricing__col`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 424 x 573.16 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Text node | span.pricing__eyebrow.pricing__eyebrow--muted: Inter 12px/12px 600, #8c8f9a, ls 0.48px |
| Transition | none |
| Icon | 16 x 16, colour #00a0ff |
| Painted layers | article.pricing__col 424.0x573.2 bg #ffffff r 16px shadow #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px; span.u--dotted 42.0x18.0 border B:1px dotted #9fa3b5; div.popover.transit 380.0x112.0 bg #ffffff r 4px shadow #000000 @ 0.09 0px 2px 5px 0px; div.pricing__line 424.0x44.6 border T:1px solid #f1f3f6; div.pricing__line 424.0x44.6 border T:1px solid #f1f3f6; div.pricing__line 424.0x44.6 border T:1px solid #f1f3f6 |
| How | at rest |

Crops: `price-paid-default.png`.

#### pricing-line

Plan feature row. One feature line inside a plan card.

Page: pricing. Selector: `.pricing__line`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 636 x 43.59 |
| Padding | 12px 28px |
| Gap | 10px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/19.6px 500 |
| Letter spacing | normal |
| Colour | #1a2035 |
| Text node | span: Inter 14px/19.6px 500, #1a2035 |
| Transition | none |
| Icon | 16 x 16, colour #00a0ff |
| Ancestor paint | 1 up article.pricing__col.pricing__col--free bg #ffffff shadow #00a0ff @ 0.18 16px 22px 64px 0px, #00a0ff @ 0.4 0px 0px 0px 1px, #123769 @ 0.06 0px 8px 24px 0px |
| How | at rest |

Crops: `pricing-line-default.png`.

#### pricing-cta

Pricing CTA. The large "Start for free" button on the pricing hero; measured, never followed.

Page: pricing. Selector: `pricing Start for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 136 x 48 | = | = | = |
| Padding | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #00a0ff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #161616 offset 0.96875px | = |
| Font | Inter 16px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.button--large 136.0x48.0 bg #00a0ff r 6px | = | a.button.button--large 136.0x48.0 bg #00a0ff r 6px outline 1px auto #161616 offset 0.96875px | = |
| Ancestor paint | 2 up article.pricing__col.pricing__col--free bg #ffffff shadow #00a0ff @ 0.18 16px 22px 64px 0px, #00a0ff @ 0.4 0px 0px 0px 1px, #123769 @ 0.06 0px 8px 24px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pricing-cta-default.png`, `pricing-cta-hover.png`, `pricing-cta-focus-visible.png`, `pricing-cta-pressed.png`.

#### faq-dt

FAQ question. A question in the "Questions & answers" list (dt/dd pairs).

Page: pricing. Selector: `dl.faq dt`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 508 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 17px/16px 500 |
| Letter spacing | normal |
| Colour | #131e40 |
| Transition | none |
| How | at rest |

Crops: `faq-dt-default.png`.

#### faq-dd

FAQ answer. An answer in the same FAQ list.

Page: pricing. Selector: `dl.faq dd`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 508 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 15px/24px 400 |
| Letter spacing | normal |
| Colour | #717583 |
| Transition | none |
| How | at rest |

Crops: `faq-dd-default.png`.

### Updates

#### upd-h1

Updates headline. The /updates changelog masthead.

Page: updates. Selector: `updates h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1080 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 38px/48px 400 |
| Letter spacing | normal |
| Colour | #1a2035 |
| Transition | all 1.5s cubic-bezier(0.19, 1, 0.22, 1) |
| How | at rest |

Crops: `upd-h1-default.png`.

#### upd-article

Update entry. One changelog entry on /updates (title column + body).

Page: updates. Selector: `.updates li article`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1080 x 1206.14 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Text node | a.updates__title-name: Inter 18px/25px 600, #1a2035 |
| Transition | none |
| Painted layers | img.wp-image-324 770.0x330.1 border T:1px solid #c8d9e8 / R:1px solid #c8d9e8 / B:1px solid #c8d9e8 / L:1px solid #c8d9e8 r 5px; a 125.0x21.0 border B:1px solid #00a0ff; code 17.8x21.0 bg #ffffff border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 4px; code 17.8x21.0 bg #ffffff border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 4px; a 251.0x21.0 border B:1px solid #00a0ff |
| How | at rest |

Crops: `upd-article-default.png`.

#### upd-title

Update title. The sticky title cell of a changelog entry.

Page: updates. Selector: `.updates__title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 280 x 1206.14 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/25px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Text node | a.updates__title-name: Inter 18px/25px 600, #1a2035 |
| Transition | none |
| How | at rest |

Crops: `upd-title-default.png`.

### Integrations

#### int-essential

Essential integration card. An "Essentials" integration card with a product mock (the Stripe plan card); measured, never followed.

Page: integrations. Selector: `.feat3__card.essential-card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 324.67 x 551.61 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #ffffff | = |
| Box shadow | #f0f0f5 0px 0px 0px 1px | = |
| Outline | none | = |
| Font | Inter 16px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #131e40 | = |
| Text node | div.feat3__aavatar.feat3__aavatar--lg: Inter 14px/14px 400, #d97706 | = |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = |
| Cursor | pointer | = |
| Icon | 18 x 18, colour #1a2035 | = |
| Painted layers | a.feat3__card.essential-card 324.7x551.6 bg #ffffff r 8px shadow #f0f0f5 0px 0px 0px 1px; div.feat3__aavatar.feat3__aavatar--lg 40.0x40.0 bg #fef3c7 r 50%; span.fsb__email 131.0x16.0 border B:1px dotted #8c8f9a; div.fsb__plan-card.feat3__stripe-plan 280.0x56.0 bg #ffffff r 10px shadow #000000 @ 0.06 0px 1px 3px 0px, #000000 @ 0.04 0px 0px 0px 1px; div.subscription__illu 32.0x32.0 bg #33c27f r 5px; div 16.0x16.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 50% | = |
| How | at rest | mouse hover |

Crops: `int-essential-default.png`, `int-essential-hover.png`.

#### int-card

Integration card. A grid card linking to one integration page (Stripe / Paddle / Polar / Dodo); measured, never followed.

Page: integrations. Selector: `a.card integration`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 324.66 x 236 | = |
| Padding | 24px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #ffffff | = |
| Box shadow | #f2f2f6 0px 0px 0px 1px | = |
| Outline | none | = |
| Font | Inter 16px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #131e40 | = |
| Text node | h3: Inter 18px/30px 400, #1a2035 | = |
| Transition | all 1.5s cubic-bezier(0.19, 1, 0.22, 1) | = |
| Cursor | pointer | = |
| Icon | 18 x 18, colour #1a2035 | = |
| Painted layers | a.card 324.7x236.0 bg #ffffff r 8px shadow #f2f2f6 0px 0px 0px 1px; div.cillu__icon 36.0x36.0 bg #ffffff border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 9px | = |
| How | at rest | mouse hover |

Crops: `int-card-default.png`, `int-card-hover.png`.

#### int-eyebrow

Group eyebrow. An all-caps group label (ESSENTIALS / PAYMENTS / PRODUCT AND ENGINEERING).

Page: integrations. Selector: `integrations eyebrow`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 276.66 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/30px 400 |
| Letter spacing | normal |
| Colour | #1a2035 |
| Transition | all 1.5s cubic-bezier(0.19, 1, 0.22, 1) |
| Cursor | pointer |
| Ancestor paint | 1 up a.card bg #ffffff shadow #f2f2f6 0px 0px 0px 1px |
| How | at rest |

Crops: `int-eyebrow-default.png`.

### Alternative page

#### alt-h1

Alternative headline. The comparison page masthead ("The fast, calm Intercom alternative…").

Page: alternative. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1290 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 38px/48px 400 |
| Letter spacing | normal |
| Colour | #1a2035 |
| Transition | all 1.5s cubic-bezier(0.19, 1, 0.22, 1) |
| How | at rest |

Crops: `alt-h1-default.png`.

#### alt-table

Comparison table. The "Intercom vs Fernand comparison" table — a real data table on the public site.

Page: alternative. Selector: `table.alt-table`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1290 x 756.22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/14px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Text node | th: Inter 12px/18.6px 600, #9aa3b8, ls 0.84px |
| Transition | none |
| Painted layers | th 186.0x47.6 border B:1px solid #eef0f6; th 547.4x47.6 border B:1px solid #eef0f6; th.alt-table__fernand 556.6x47.6 bg #f0f8ff border B:1px solid #eef0f6 r 8px 8px 0px 0px; td 186.0x50.7 border B:1px solid #f0f1f6; td 547.4x50.7 border B:1px solid #f0f1f6; td.alt-table__fernand 556.6x50.7 bg #f0f8ff border B:1px solid #f0f1f6 |
| How | at rest |

Crops: `alt-table-default.png`.

#### alt-faq

FAQ accordion item. One item in the comparison FAQ accordion.

Page: alternative. Selector: `.alt-faq__item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 584 x 54.25 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #f0f1f6; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Text node | button.alt-faq__summary: Inter 15px/17.25px 500, #1a2035 |
| Transition | none |
| Icon | 14 x 14, colour #9aa3b8 |
| Painted layers | div.alt-faq__item 584.0x54.3 border B:1px solid #f0f1f6 |
| Ancestor paint | 1 up div.alt-faq bg #ffffff shadow #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px |
| How | at rest |

Crops: `alt-faq-default.png`.

#### alt-faq-summary

FAQ disclosure. A disclosure button in the comparison FAQ; the opened state was measured after clicking it (a local UI toggle).

Page: alternative. Selector: `button.alt-faq__summary`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 584 x 53.25 | = | = | = | = |
| Padding | 18px 0px | = | = | = | = |
| Gap | 16px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Inter 15px/17.25px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #1a2035 | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 14 x 14, colour #9aa3b8 | = | = | = | = |
| Ancestor paint | 2 up div.alt-faq bg #ffffff shadow #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | clicked the FAQ summary to expand its answer (aria-expanded=true at save) |

Crops: `alt-faq-summary-default.png`, `alt-faq-summary-hover.png`, `alt-faq-summary-focus-visible.png`, `alt-faq-summary-pressed.png`, `alt-faq-summary-opened.png`.

### Feature page

#### ag-switch

Permission switch. An on/off switch in the "Every key only does what you allow" permissions demo — a local UI toggle flipping the demo.

Page: feature. Selector: `button.ag-switch`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | #16a34a | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1a2035 offset 2px | = |
| Font | Inter 13px/14.95px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | background-color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.is-on.ag-switch 32.0x18.0 bg #16a34a r 40px; span 14.0x14.0 bg #ffffff r 50% shadow #123769 @ 0.2 0px 1px 2px 0px | = | button.is-on.ag-switch 32.0x18.0 bg #16a34a r 40px outline 2px solid #1a2035 offset 2px; span 14.0x14.0 bg #ffffff r 50% shadow #123769 @ 0.2 0px 1px 2px 0px | button.is-on.ag-switch 32.0x18.0 bg #16a34a r 40px; span 16.0x14.0 bg #ffffff r 50% shadow #123769 @ 0.2 0px 1px 2px 0px |
| Ancestor paint | 3 up div.ag-key bg #ffffff shadow #eaecf8 0px 0px 0px 1px, #123769 @ 0.04 0px 4px 12px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ag-switch-default.png`, `ag-switch-hover.png`, `ag-switch-focus-visible.png`, `ag-switch-pressed.png`.

#### ag-replay

Replay button. The "↻ Replay" control on the agent animation demo.

Page: feature. Selector: `button.ag-replay`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81 x 26.94 | = | = | 78.57 x 26.13 |
| Padding | 6px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 13px/14.95px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6f7b96 | #58637d | = | #58637d |
| Transition | color, transform 0.15s, 0.16s ease, ease-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.ag-replay 81.0x26.9 bg #ffffff r 6px shadow #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px | = | = | button.ag-replay 78.6x26.1 bg #ffffff r 6px shadow #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `ag-replay-default.png`, `ag-replay-hover.png`, `ag-replay-focus-visible.png`, `ag-replay-pressed.png`.

### App login

#### login-h1

Login headline. "Welcome back" — the 25px sign-in heading.

Page: login. Selector: `login h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 25px/30px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Transition | none |
| How | at rest |

Crops: `login-h1-default.png`.

#### login-card

Login card. The sign-in card on app.getfernand.com/auth/login — e-mail and password fields, the primary submit and the account links.

Page: login. Selector: `login form/card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 216.25 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Text node | a: Inter 15px/17.25px 400, #9fa3b5 |
| Transition | none |
| Icon | 20 x 20, colour #0000ee |
| Painted layers | input 350.0x46.0 bg #ffffff border T:1px solid #d1d5e6 / R:1px solid #d1d5e6 / B:1px solid #d1d5e6 / L:1px solid #d1d5e6 r 4px; input 350.0x46.0 bg #ffffff border T:1px solid #d1d5e6 / R:1px solid #d1d5e6 / B:1px solid #d1d5e6 / L:1px solid #d1d5e6 r 4px; input.button.button--primary 350.0x46.0 bg #00a0ff border T:2px solid #00a0ff / R:2px solid #00a0ff / B:2px solid #00a0ff / L:2px solid #00a0ff r 4px |
| How | at rest |

Crops: `login-card-default.png`.

#### login-field

Email field (login). The "Your work email" input; focused and typed into then cleared — never submitted.

Page: login. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 350 x 46 | = | = |
| Padding | 0px 14px | = | = |
| Border | 1px solid #d1d5e6 | 1px solid #01a0ff | 1px solid #00a0ff |
| Radius | 4px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #10a6ff @ 0.416 0px 0px 4.97644px 0px, #000000 @ 0 0px 0px 0px 0px | #10a6ff @ 0.42 0px 0px 5px 0px |
| Outline | none | = | = |
| Font | Inter 15px/17.25px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #131e40 | = | = |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #9fa3b5, opacity 1 | = | = |
| Painted layers | input 350.0x46.0 bg #ffffff border T:1px solid #d1d5e6 / R:1px solid #d1d5e6 / B:1px solid #d1d5e6 / L:1px solid #d1d5e6 r 4px | input 350.0x46.0 bg #ffffff border T:1px solid #01a0ff / R:1px solid #01a0ff / B:1px solid #01a0ff / L:1px solid #01a0ff r 4px shadow #10a6ff @ 0.416 0px 0px 4.97644px 0px, #000000 @ 0 0px 0px 0px 0px | input 350.0x46.0 bg #ffffff border T:1px solid #00a0ff / R:1px solid #00a0ff / B:1px solid #00a0ff / L:1px solid #00a0ff r 4px shadow #10a6ff @ 0.42 0px 0px 5px 0px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-field-default.png`, `login-field-focused.png`, `login-field-filled.png`.

#### login-pass

Password field (login). The "Your password" input; focused and typed into then cleared — never submitted.

Page: login. Selector: `input[type=password]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 350 x 46 | = | = |
| Padding | 0px 14px | = | = |
| Border | 1px solid #d1d5e6 | 1px solid #03a1ff | 1px solid #00a0ff |
| Radius | 4px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #10a6ff @ 0.416 0px 0px 4.93091px 0px, #000000 @ 0 0px 0px 0px 0px | #10a6ff @ 0.42 0px 0px 5px 0px |
| Outline | none | = | = |
| Font | Inter 15px/17.25px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #131e40 | = | = |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #9fa3b5, opacity 1 | = | = |
| Painted layers | input 350.0x46.0 bg #ffffff border T:1px solid #d1d5e6 / R:1px solid #d1d5e6 / B:1px solid #d1d5e6 / L:1px solid #d1d5e6 r 4px | input 350.0x46.0 bg #ffffff border T:1px solid #03a1ff / R:1px solid #03a1ff / B:1px solid #03a1ff / L:1px solid #03a1ff r 4px shadow #10a6ff @ 0.416 0px 0px 4.93091px 0px, #000000 @ 0 0px 0px 0px 0px | input 350.0x46.0 bg #ffffff border T:1px solid #00a0ff / R:1px solid #00a0ff / B:1px solid #00a0ff / L:1px solid #00a0ff r 4px shadow #10a6ff @ 0.42 0px 0px 5px 0px |
| How | at rest | clicked into the field | typed "sample-pass-123", then deleted; nothing sent |

Crops: `login-pass-default.png`, `login-pass-focused.png`, `login-pass-filled.png`.

#### login-submit

Login submit. The primary "Login" submit; its states were measured but the button was never clicked — nothing was submitted.

Page: login. Selector: `login input[type=submit]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 350 x 46 | = | = | = |
| Padding | 12px 18px | = | = | = |
| Border | 2px solid #00a0ff | = | = | = |
| Radius | 4px | = | = | = |
| Background | #00a0ff | = | = | = |
| Box shadow | none | #e7ebf3 @ 0.718 0px 1.98512px 1.98512px 0px, #363d54 @ 0.05 0px 0px 14.8884px 0px | #11a6ff @ 0.408 0px 0.00339661px 4.85793px 0px, #363d54 @ 0 0px 0px 0.0254746px 0px | #e7ebf3 @ 0.71 0px 1.96646px 1.97135px 0px, #363d54 @ 0.05 0px 0px 14.7485px 0px |
| Outline | none | = | = | = |
| Font | Inter 15px/17.25px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Placeholder | #ffffff, opacity 1 | = | = | = |
| Painted layers | input.button.button--primary 350.0x46.0 bg #00a0ff border T:2px solid #00a0ff / R:2px solid #00a0ff / B:2px solid #00a0ff / L:2px solid #00a0ff r 4px | input.button.button--primary 350.0x46.0 bg #00a0ff border T:2px solid #00a0ff / R:2px solid #00a0ff / B:2px solid #00a0ff / L:2px solid #00a0ff r 4px shadow #e7ebf3 @ 0.718 0px 1.98512px 1.98512px 0px, #363d54 @ 0.05 0px 0px 14.8884px 0px | input.button.button--primary 350.0x46.0 bg #00a0ff border T:2px solid #00a0ff / R:2px solid #00a0ff / B:2px solid #00a0ff / L:2px solid #00a0ff r 4px shadow #11a6ff @ 0.408 0px 0.00339661px 4.85793px 0px, #363d54 @ 0 0px 0px 0.0254746px 0px | input.button.button--primary 350.0x46.0 bg #00a0ff border T:2px solid #00a0ff / R:2px solid #00a0ff / B:2px solid #00a0ff / L:2px solid #00a0ff r 4px shadow #e7ebf3 @ 0.71 0px 1.96646px 1.97135px 0px, #363d54 @ 0.05 0px 0px 14.7485px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-focus-visible.png`, `login-submit-pressed.png`.

#### login-link

Login link. The "Create an account" / "Lost password?" link beside the form; measured, never followed.

Page: login. Selector: `login account link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 127 x 19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #131414 offset 0.96875px | = |
| Font | Inter 15px/17.25px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9fa3b5 | #01a0fe | = | #03a0fe |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 127.0x19.0 outline 1px auto #131414 offset 0.96875px | = |

Crops: `login-link-default.png`, `login-link-hover.png`, `login-link-focus-visible.png`, `login-link-pressed.png`.

### App signup

#### create-panel

Signup intro panel. The left intro panel of /create — "Bonjour, I'm Fernand. The better, faster and calmer helpdesk experience."

Page: signup. Selector: `.wrapper__create-left`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 720 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Transition | opacity 0.3s ease-in-out |
| Icon | 720 x 216.28, colour #131e40, fill #000000 |
| How | at rest |

Crops: `create-panel-default.png`.

#### create-h1

Signup headline. The signup greeting heading.

Page: signup. Selector: `create h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 599 x 90 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 25px/30px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Text node | span.u--subtle.u--block: Inter 25px/30px 400, #636d83 |
| Transition | none |
| How | at rest |

Crops: `create-h1-default.png`.

#### create-field

Email field (signup). The "Your work email" signup input; focused and typed into then cleared — never submitted.

Page: signup. Selector: `create input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 599 x 46 | = | = |
| Padding | 0px 14px | = | = |
| Border | 1px solid #d1d5e6 | 1px solid #02a1ff | 1px solid #00a0ff |
| Radius | 4px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #10a6ff @ 0.416 0px 0px 4.94347px 0px, #000000 @ 0 0px 0px 0px 0px | #10a6ff @ 0.42 0px 0px 5px 0px |
| Outline | none | = | = |
| Font | Inter 15px/17.25px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #131e40 | = | = |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #9fa3b5, opacity 1 | = | = |
| Painted layers | input 599.0x46.0 bg #ffffff border T:1px solid #d1d5e6 / R:1px solid #d1d5e6 / B:1px solid #d1d5e6 / L:1px solid #d1d5e6 r 4px | input 599.0x46.0 bg #ffffff border T:1px solid #02a1ff / R:1px solid #02a1ff / B:1px solid #02a1ff / L:1px solid #02a1ff r 4px shadow #10a6ff @ 0.416 0px 0px 4.94347px 0px, #000000 @ 0 0px 0px 0px 0px | input 599.0x46.0 bg #ffffff border T:1px solid #00a0ff / R:1px solid #00a0ff / B:1px solid #00a0ff / L:1px solid #00a0ff r 4px shadow #10a6ff @ 0.42 0px 0px 5px 0px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `create-field-default.png`, `create-field-focused.png`, `create-field-filled.png`.

#### create-field-name

Product name field. The "Your product's name" input; focused and typed into then cleared — never submitted.

Page: signup. Selector: `create input[type=text]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 599 x 46 | = | = |
| Padding | 0px 14px | = | = |
| Border | 1px solid #d1d5e6 | 1px solid #02a1ff | 1px solid #00a0ff |
| Radius | 4px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #10a6ff @ 0.416 0px 0px 4.94347px 0px, #000000 @ 0 0px 0px 0px 0px | #10a6ff @ 0.42 0px 1.20147e-08px 5px 0px, #363d54 @ 0 0px 0px 9.01104e-08px 0px |
| Outline | none | = | = |
| Font | Inter 15px/17.25px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #131e40 | = | = |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #9fa3b5, opacity 1 | = | = |
| Painted layers | input 599.0x46.0 bg #ffffff border T:1px solid #d1d5e6 / R:1px solid #d1d5e6 / B:1px solid #d1d5e6 / L:1px solid #d1d5e6 r 4px | input 599.0x46.0 bg #ffffff border T:1px solid #02a1ff / R:1px solid #02a1ff / B:1px solid #02a1ff / L:1px solid #02a1ff r 4px shadow #10a6ff @ 0.416 0px 0px 4.94347px 0px, #000000 @ 0 0px 0px 0px 0px | input 599.0x46.0 bg #ffffff border T:1px solid #00a0ff / R:1px solid #00a0ff / B:1px solid #00a0ff / L:1px solid #00a0ff r 4px shadow #10a6ff @ 0.42 0px 1.20147e-08px 5px 0px, #363d54 @ 0 0px 0px 9.01104e-08px 0px |
| How | at rest | clicked into the field | typed "Example Inc", then deleted; nothing sent |

Crops: `create-field-name-default.png`, `create-field-name-focused.png`, `create-field-name-filled.png`.

#### create-checkbox

Terms checkbox. The terms-of-service checkbox (a styled .fake__checkbox over the native input); measured, never toggled.

Page: signup. Selector: `create input[type=checkbox]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 18 x 18 |
| Padding | 0px |
| Border | 1px solid #d1d5e6 |
| Radius | 5px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 15px/17.25px 400 |
| Letter spacing | normal |
| Colour | #00a0ff |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| Cursor | pointer |
| Placeholder | #00a0ff, opacity 1 |
| Painted layers | input 18.0x18.0 bg #ffffff border T:1px solid #d1d5e6 / R:1px solid #d1d5e6 / B:1px solid #d1d5e6 / L:1px solid #d1d5e6 r 5px |
| How | at rest |

Crops: `create-checkbox-default.png`.

#### create-tos

Terms text. The "Accept our terms of service" line; its link was never followed.

Page: signup. Selector: `create ToS line`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 599 x 18.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/16.1px 400 |
| Letter spacing | normal |
| Colour | #5e6271 |
| Transition | none |
| Cursor | pointer |
| Painted layers | input 18.0x18.0 bg #ffffff border T:1px solid #d1d5e6 / R:1px solid #d1d5e6 / B:1px solid #d1d5e6 / L:1px solid #d1d5e6 r 5px |
| How | at rest |

Crops: `create-tos-default.png`.

#### create-continue

Continue button. The primary "Continue" submit; its states were measured but the button was never clicked — nothing was submitted.

Page: signup. Selector: `create button.button--primary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 153 x 47 | = | = | = |
| Padding | 12px 18px | = | = | = |
| Border | 2px solid #00a0ff | = | = | = |
| Radius | 4px | = | = | = |
| Background | #00a0ff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #121212 offset 0px | = |
| Font | Inter 15px/17.25px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.button.button--primary 153.0x47.0 bg #00a0ff border T:2px solid #00a0ff / R:2px solid #00a0ff / B:2px solid #00a0ff / L:2px solid #00a0ff r 4px; kbd 43.0x17.0 bg #ffffff @ 0.2 r 4px | = | button.button.button--primary 153.0x47.0 bg #00a0ff border T:2px solid #00a0ff / R:2px solid #00a0ff / B:2px solid #00a0ff / L:2px solid #00a0ff r 4px outline 1px auto #121212 offset 0px; kbd 43.0x17.0 bg #ffffff @ 0.2 r 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `create-continue-default.png`, `create-continue-hover.png`, `create-continue-focus-visible.png`, `create-continue-pressed.png`.

### Help center

#### help-header

Docs header. The docs site header: logo, the collection nav, the search and menu toggles and the dark-mode switch.

Page: help. Selector: `help header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 900 |
| Padding | 22px |
| Border | T: none; R: 1px solid #eaecf8; B: none; L: none |
| Radius | 0px |
| Background | #f7fafc |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/25.6px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Text node | a.router-link-active.router-link-exact-active: Inter 14px/22.4px 400, #00a0ff |
| Transition | none |
| Icon | 0 x 0, colour #131e40 |
| Painted layers | header.header 350.0x900.0 bg #f7fafc border R:1px solid #eaecf8; a.router-link-active.router-link-exact-active 290.0x40.4 bg #ffffff border T:1px solid #eaecf8 / R:1px solid #eaecf8 / B:1px solid #eaecf8 / L:1px solid #eaecf8 r 5px shadow #000000 @ 0.05 0px 1px 3px 0px; a 290.0x40.4 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 5px; ul::after 1pxx0px bg #eaecf8; a 268.0x40.4 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 5px; ul::after 1pxx0px bg #eaecf8 |
| How | at rest |

Crops: `help-header-default.png`.

#### help-logo

Docs logo. The Fernand Docs wordmark.

Page: help. Selector: `help header logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 290 x 42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/25.6px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| Cursor | pointer |
| How | at rest |

Crops: `help-logo-default.png`.

#### help-nav-item

Docs nav item. A collection link in the docs nav; measured, never followed.

Page: help. Selector: `help nav a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 290 x 40.39 | = | = | = |
| Padding | 8px 0px 8px 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 5px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #111111 offset 0.984375px | = |
| Font | Inter 14px/22.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #454c65 | = | = | = |
| Text node | span: Inter 14px/22.4px 400, #454c65 | = | = | = |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #9fa3b5 | = | = | = |
| Painted layers | a 290.0x40.4 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 5px | = | a 290.0x40.4 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 5px outline 1px auto #111111 offset 0.984375px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `help-nav-item-default.png`, `help-nav-item-hover.png`, `help-nav-item-focus-visible.png`, `help-nav-item-pressed.png`.

#### help-search

Search field. The docs search field ("Start typing to search an article, collection…", ⌘K hint); focused and typed into — a local filter, nothing sent.

Page: help. Selector: `#search-field`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 480 x 42 | = | - |
| Padding | 1px 2px 1px 40px | = | - |
| Border | 1px solid #eaecf8 | 1px solid #01a0ff | - |
| Radius | 5px | = | - |
| Background | #ffffff | = | - |
| Box shadow | #1a1c21 @ 0.03 0px 2px 3px 0px | = | - |
| Outline | none | = | - |
| Font | Inter 14px/16.1px 400 | = | - |
| Letter spacing | normal | = | - |
| Colour | #131e40 | = | - |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | - |
| Cursor | text | = | - |
| Placeholder | #5f667d, opacity 1 | = | - |
| Painted layers | input.transit 480.0x42.0 bg #ffffff border T:1px solid #eaecf8 / R:1px solid #eaecf8 / B:1px solid #eaecf8 / L:1px solid #eaecf8 r 5px shadow #1a1c21 @ 0.03 0px 2px 3px 0px | input.transit 480.0x42.0 bg #ffffff border T:1px solid #01a0ff / R:1px solid #01a0ff / B:1px solid #01a0ff / L:1px solid #01a0ff r 5px shadow #1a1c21 @ 0.03 0px 2px 3px 0px | - |
| How | at rest | clicked into the field | - |
| Error | - | = | locator.evaluate: Timeout 8000ms exceeded. Call log:   - waiting for locator('#search-field').first().first().first()  |

Crops: `help-search-default.png`, `help-search-focused.png`.

#### help-search-pop

Search popover. The results popover the docs search opens while typing.

Page: help. Selector: `.search__popover`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 350 |
| Padding | 10px 20px |
| Border | none |
| Radius | 5px |
| Background | #ffffff |
| Box shadow | #535765 @ 0.17 0px 1px 4px 0px, #363d54 @ 0.15 0px 9px 50px 0px |
| Outline | none |
| Font | Inter 14px/22.4px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Text node | div.collection__icon: Inter 14px/22.4px 400, #9fa3b5 |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Painted layers | div.search__popover.transit 480.0x350.0 bg #ffffff r 5px shadow #535765 @ 0.17 0px 1px 4px 0px, #363d54 @ 0.15 0px 9px 50px 0px; li.active 460.0x66.0 bg #f5f7f9 r 5px; a.u--flex 460.0x54.0 bg #f5f7f9 r 5px; div.collection__icon 42.0x42.0 bg #c0a643 @ 0.1 r 100%; div.collection__icon 42.0x42.0 bg #583870 @ 0.1 r 100%; div.collection__icon 42.0x42.0 bg #f7fafc r 100% |
| How | at rest |

Crops: `help-search-pop-default.png`.

#### help-dark-toggle

Dark-mode switch. The docs site's own "Switch to dark mode" link — the real user-facing toggle that sets body.dark-mode; its states were measured but it was only toggled on the helpdark pass.

Page: help. Selector: `a.switch__dark`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 30 x 30 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #121212 offset 0.96875px | = |
| Font | Inter 16px/25.6px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #5f667d | #01a0fe | = | #029ffd |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 24, colour #9fa3b5 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.switch__dark 30.0x30.0 r 20px outline 1px auto #121212 offset 0.96875px | = |

Crops: `help-dark-toggle-default.png`, `help-dark-toggle-hover.png`, `help-dark-toggle-focus-visible.png`, `help-dark-toggle-pressed.png`.

#### help-card

Collection card. A collection card on the docs home (emoji glyph, title, article count, description); measured, never followed.

Page: help. Selector: `help a.card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 310 x 146.78 | = |
| Padding | 22px | = |
| Border | 1px solid #eaecf8 | 1px solid #d1d5e6 |
| Radius | 5px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/25.6px 400 | = |
| Letter spacing | normal | = |
| Colour | #131e40 | = |
| Text node | div.collection__icon: Inter 16px/25.6px 400, #9fa3b5 | = |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = |
| Cursor | pointer | = |
| Painted layers | a.card 310.0x146.8 border T:1px solid #eaecf8 / R:1px solid #eaecf8 / B:1px solid #eaecf8 / L:1px solid #eaecf8 r 5px; div.collection__icon 42.0x42.0 bg #c0a643 @ 0.1 r 100% | a.card 310.0x146.8 border T:1px solid #d1d5e6 / R:1px solid #d1d5e6 / B:1px solid #d1d5e6 / L:1px solid #d1d5e6 r 5px; div.collection__icon 42.0x42.0 bg #c0a643 @ 0.1 r 100% |
| How | at rest | mouse hover |

Crops: `help-card-default.png`, `help-card-hover.png`.

#### help-article-item

Article row. An article row inside a collection (title + standfirst); measured, never followed.

Page: help. Selector: `help .wrapper__articles a`. States: .

Not found on the page at capture time.

#### help-goto

Go-to-Fernand link. The "→ Go to Fernand" link in the sticky search bar; measured, never followed.

Page: help. Selector: `help Go to Fernand`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 114 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101011 offset 0.984375px | = |
| Font | Inter 14px/22.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #131e40 | #009ffe | = | #009efc |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.u--fs14 114.0x17.0 outline 1px auto #101011 offset 0.984375px | = |

Crops: `help-goto-default.png`, `help-goto-hover.png`, `help-goto-focus-visible.png`, `help-goto-pressed.png`.

#### help-h1

Article headline. The article title on a docs page ("Getting started").

Page: helparticle. Selector: `help h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 962 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 42px/50px 500 |
| Letter spacing | normal |
| Colour | #131e40 |
| Transition | none |
| How | at rest |

Crops: `help-h1-default.png`.

#### help-prose

Article body. A body paragraph in a docs article.

Page: helparticle. Selector: `help article p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 962 x 25.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/25.6px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Transition | none |
| How | at rest |

Crops: `help-prose-default.png`.

#### help-content-link

Article link. An in-content link inside a docs article; measured, never followed.

Page: helparticle. Selector: `help article a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 58 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101011 offset 0.96875px | = |
| Font | Inter 14px/22.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #131e40 | #009ffd | = | #009efc |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.u--fs14 58.0x17.0 outline 1px auto #101011 offset 0.96875px | = |

Crops: `help-content-link-default.png`, `help-content-link-hover.png`, `help-content-link-focus-visible.png`, `help-content-link-pressed.png`.

### Help center (dark)

#### hd-page

Docs page (dark). The docs article surface under body.dark-mode — reached through the site's own "Switch to dark mode" link, not a reconstruction.

Page: helpdark. Selector: `help main (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1090 x 1506.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/25.6px 400 |
| Letter spacing | normal |
| Colour | #a1a1aa |
| Text node | kbd.transit.m--hide: Inter 12px/23px 400, #8a8f98 |
| Transition | none |
| Icon | 20 x 20, colour #a1a1aa, fill #8a8f98 |
| Painted layers | div::after.wrapper.wrapper__pageheader 1090pxx120px image linear-gradient(#161618, #161618 60%, #121212 @ 0); input.transit 480.0x42.0 bg #161618 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 5px shadow #1a1c21 @ 0.03 0px 2px 3px 0px; kbd.transit.m--hide 30.0x28.0 bg #18181b border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px; a.transit.m--show 0.0x0.0 bg #18181b border L:1px solid #44474e r 0px 5px 5px 0px; div.search__popover.transit 480.0x20.0 bg #1f2023 r 5px shadow #000000 @ 0.5 0px 16px 70px 0px; a.card 310.0x184.8 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 5px |
| How | at rest |

Crops: `hd-page-default.png`.

#### hd-h1

Article headline (dark). The article title under dark-mode.

Page: helpdark. Selector: `help h1 (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 962 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 42px/50px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hd-h1-default.png`.

#### hd-nav-item

Docs nav item (dark). A collection link in the docs nav under dark-mode.

Page: helpdark. Selector: `help nav a (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 290 x 40.39 |
| Padding | 8px 0px 8px 12px |
| Border | 1px solid #232326 |
| Radius | 5px |
| Background | #232326 |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/22.4px 400 |
| Letter spacing | normal |
| Colour | #00a0ff |
| Text node | span: Inter 14px/22.4px 400, #00a0ff |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| Cursor | pointer |
| Icon | 20 x 20, colour #f7f8f8 |
| Painted layers | a.router-link-active.router-link-exact-active 290.0x40.4 bg #232326 border T:1px solid #232326 / R:1px solid #232326 / B:1px solid #232326 / L:1px solid #232326 r 5px |
| How | at rest |

Crops: `hd-nav-item-default.png`.

#### hd-search

Search field (dark). The docs search field under dark-mode.

Page: helpdark. Selector: `#search-field (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 42 |
| Padding | 1px 2px 1px 40px |
| Border | 1px solid #ffffff @ 0.1 |
| Radius | 5px |
| Background | #161618 |
| Box shadow | #1a1c21 @ 0.03 0px 2px 3px 0px |
| Outline | none |
| Font | Inter 14px/16.1px 400 |
| Letter spacing | normal |
| Colour | #f7f8f8 |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| Cursor | text |
| Placeholder | #8a8f98, opacity 1 |
| Painted layers | input.transit 480.0x42.0 bg #161618 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 5px shadow #1a1c21 @ 0.03 0px 2px 3px 0px |
| How | at rest |

Crops: `hd-search-default.png`.

#### hd-card

Collection card (dark). A collection card under dark-mode.

Page: helpdark. Selector: `help a.card (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 310 x 184.77 |
| Padding | 22px |
| Border | 1px solid #ffffff @ 0.1 |
| Radius | 5px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/25.6px 400 |
| Letter spacing | normal |
| Colour | #f7f8f8 |
| Text node | div.collection__icon: Inter 16px/25.6px 400, #e6e9eb |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| Cursor | pointer |
| Painted layers | a.card 310.0x184.8 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 5px; div.collection__icon 42.0x42.0 bg #546cc8 @ 0.1 r 100% |
| How | at rest |

Crops: `hd-card-default.png`.

#### hd-prose

Article body (dark). A body paragraph in a docs article under dark-mode.

Page: helpdark. Selector: `help article p (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 962 x 25.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/25.6px 400 |
| Letter spacing | normal |
| Colour | #a1a1aa |
| Transition | none |
| How | at rest |

Crops: `hd-prose-default.png`.

### Mobile (390 wide)

#### m-topbar

Mobile top bar. The phone header: Fernand mark, nav links and "Start for free" (Book a demo hides at this width).

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 71.5 |
| Padding | 12px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #191e5a @ 0 0px -1px 0px 0px inset |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #131e40 |
| Text node | a: Inter 14px/14px 500, #6f7b96 |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 35 x 45.5, colour #0000ee |
| Painted layers | header.transit.transit--slow 390.0x71.5 shadow #191e5a @ 0 0px -1px 0px 0px inset; a 0.0x0.0 bg #ffffff r 6px shadow #123769 @ 0.08 0px 2px 4px 0px, #123769 @ 0.04 0px 1px 1px 0px, #123769 @ 0.08 0px 0px 0px 1px; a 115.0x30.0 bg #00a0ff r 6px |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-cta

Mobile header CTA. The header "Start for free" button at 390 wide; measured never followed.

Page: mobile. Selector: `mobile Start for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 115 x 30 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #00a0ff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e69a06 offset 0.96875px | = |
| Font | Inter 14px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a 115.0x30.0 bg #00a0ff r 6px | = | a 115.0x30.0 bg #00a0ff r 6px outline 1px auto #e69a06 offset 0.96875px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-cta-default.png`, `m-cta-hover.png`, `m-cta-focus-visible.png`, `m-cta-pressed.png`.

#### m-hero-h1

Mobile hero headline. The masthead at 390 wide — the 38px display heading drops to 26px.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 26px/33px 400 |
| Letter spacing | normal |
| Colour | #1a2035 |
| Transition | all 1.5s cubic-bezier(0.19, 1, 0.22, 1) |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-hero-cta

Mobile hero CTA. The hero "Start for free" button at 390 wide; measured never followed.

Page: mobile. Selector: `mobile hero CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 169 x 49 | = | = | = |
| Padding | 13px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #1a2035 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #1a2035 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e69905 offset 0.96875px | = |
| Font | Inter 15px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.75s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.hero__cta--primary 169.0x49.0 bg #1a2035 border T:1px solid #1a2035 / R:1px solid #1a2035 / B:1px solid #1a2035 / L:1px solid #1a2035 r 8px; kbd 22.0x21.0 bg #3d4259 r 4px | = | a.hero__cta--primary 169.0x49.0 bg #1a2035 border T:1px solid #1a2035 / R:1px solid #1a2035 / B:1px solid #1a2035 / L:1px solid #1a2035 r 8px outline 1px auto #e69905 offset 0.96875px; kbd 22.0x21.0 bg #3d4259 r 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-hero-cta-default.png`, `m-hero-cta-hover.png`, `m-hero-cta-focus-visible.png`, `m-hero-cta-pressed.png`.

## Transitions declared in the readable stylesheets

getfernand.com serves its CSS same-origin (inline blocks plus _nuxt chunks; the app serves one bundled index sheet), so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- alternative: `0.75s cubic-bezier(0.19, 1, 0.22, 1)`, `1.5s cubic-bezier(0.19, 1, 0.22, 1)`, `0.5s cubic-bezier(0.19, 1, 0.22, 1)`, `0.2s cubic-bezier(0.19, 1, 0.22, 1)`, `opacity 0.2s, transform 0.2s, box-shadow 0.2s`, `transform 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `opacity 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `transform 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `background 0.2s ease-out, opacity 0.2s ease-out`, `background 0.2s, opacity 0.3s, transform 0.3s`

- feature: `0.75s cubic-bezier(0.19, 1, 0.22, 1)`, `1.5s cubic-bezier(0.19, 1, 0.22, 1)`, `0.5s cubic-bezier(0.19, 1, 0.22, 1)`, `0.2s cubic-bezier(0.19, 1, 0.22, 1)`, `opacity 0.2s, transform 0.2s, box-shadow 0.2s`, `transform 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `opacity 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `transform 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `background 0.2s ease-out, opacity 0.2s ease-out`, `background 0.2s, opacity 0.3s, transform 0.3s`

- help: `0.5s cubic-bezier(0.19, 1, 0.22, 1)`, `0.75s cubic-bezier(0.19, 1, 0.22, 1)`, `1.5s cubic-bezier(0.19, 1, 0.22, 1)`, `3s cubic-bezier(0.19, 1, 0.22, 1)`, `0.2s cubic-bezier(0.19, 1, 0.22, 1)`, `none`, `1s cubic-bezier(0.19, 1, 0.22, 1)`, `0.15s ease-out`, `0.25s ease-in`, `opacity 0.3s`, `transform 0.3s cubic-bezier(0.2, 0, 0.2, 1)`

- home: `0.75s cubic-bezier(0.19, 1, 0.22, 1)`, `1.5s cubic-bezier(0.19, 1, 0.22, 1)`, `0.5s cubic-bezier(0.19, 1, 0.22, 1)`, `0.2s cubic-bezier(0.19, 1, 0.22, 1)`, `opacity 0.2s, transform 0.2s, box-shadow 0.2s`, `transform 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `opacity 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `transform 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `background 0.2s ease-out, opacity 0.2s ease-out`, `background 0.2s, opacity 0.3s, transform 0.3s`

- integrations: `0.75s cubic-bezier(0.19, 1, 0.22, 1)`, `1.5s cubic-bezier(0.19, 1, 0.22, 1)`, `0.5s cubic-bezier(0.19, 1, 0.22, 1)`, `0.2s cubic-bezier(0.19, 1, 0.22, 1)`, `opacity 0.2s, transform 0.2s, box-shadow 0.2s`, `transform 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `opacity 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `transform 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `background 0.2s ease-out, opacity 0.2s ease-out`, `background 0.2s, opacity 0.3s, transform 0.3s`

- login: `0.5s cubic-bezier(0.19, 1, 0.22, 1)`, `0.2s cubic-bezier(0.19, 1, 0.22, 1)`, `0.75s cubic-bezier(0.19, 1, 0.22, 1)`, `width 0.3s`, `opacity 0.3s`, `stroke-dasharray 0.3s`, `opacity 0.15s, transform 0.15s, visibility 0.15s`, `opacity 0.75s cubic-bezier(0.19, 1, 0.22, 1)`, `background-color 0.75s cubic-bezier(0.19, 1, 0.22, 1)`, `0.3s linear`, `0.1s ease-out`, `opacity`

- pricing: `0.75s cubic-bezier(0.19, 1, 0.22, 1)`, `1.5s cubic-bezier(0.19, 1, 0.22, 1)`, `0.5s cubic-bezier(0.19, 1, 0.22, 1)`, `0.2s cubic-bezier(0.19, 1, 0.22, 1)`, `opacity 0.2s, transform 0.2s, box-shadow 0.2s`, `transform 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `opacity 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `transform 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `background 0.2s ease-out, opacity 0.2s ease-out`, `background 0.2s, opacity 0.3s, transform 0.3s`

- signup: `0.5s cubic-bezier(0.19, 1, 0.22, 1)`, `0.2s cubic-bezier(0.19, 1, 0.22, 1)`, `0.75s cubic-bezier(0.19, 1, 0.22, 1)`, `width 0.3s`, `opacity 0.3s`, `stroke-dasharray 0.3s`, `opacity 0.15s, transform 0.15s, visibility 0.15s`, `opacity 0.75s cubic-bezier(0.19, 1, 0.22, 1)`, `background-color 0.75s cubic-bezier(0.19, 1, 0.22, 1)`, `0.3s linear`, `0.1s ease-out`, `opacity`

- updates: `0.75s cubic-bezier(0.19, 1, 0.22, 1)`, `1.5s cubic-bezier(0.19, 1, 0.22, 1)`, `0.5s cubic-bezier(0.19, 1, 0.22, 1)`, `0.2s cubic-bezier(0.19, 1, 0.22, 1)`, `opacity 0.2s, transform 0.2s, box-shadow 0.2s`, `transform 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `opacity 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `transform 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `background 0.2s ease-out, opacity 0.2s ease-out`, `background 0.2s, opacity 0.3s, transform 0.3s`

## Reduced motion

- home (`header li.button__header a` under prefers-reduced-motion): transition `1.5s cubic-bezier(0.19, 1, 0.22, 1)`, animation `none 0s ease 0s 1 normal none running`, html scroll-behavior `auto`
