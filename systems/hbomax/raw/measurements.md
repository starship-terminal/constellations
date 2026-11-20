# Component measurements

Computed styles read from www.hbomax.com on 2026-11-17 by `tools/capture/public/measure.mjs`, signed out, in headed Chromium under Xvfb at 1440 x 900 (the Mobile group at 390 x 844 — Akamai's edge returns 403 to headless Chromium), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `opened` is a resting state reached by a component's own UI toggle (an FAQ chevron, the carousel's Next arrow, the billing toggle, the language selector, the phone's menu button). The site paints a single dark theme (html data-theme="max"), so there are no dark-state passes. Nothing was typed, sent or signed into — Sign In and the plan CTAs were hovered and focused, never pressed.

## Components

### Site chrome

#### header-bar

Fixed navigation bar. The translucent gradient bar over every page: HBO Max wordmark, nav links and the Sign In button.

Page: /sg/en. Selector: `header nav, nav[class*="Navbar"], nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 60 |
| Padding | 8px 16px |
| Border | none |
| Radius | 0px |
| Background | #000000 @ 0.7 |
| Box shadow | none |
| Outline | none |
| Font | Max Sans 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.sc-bfd2ca80-3.hvTQkZ: Max Sans 15.385px/20.7698px 700, #ffffff |
| Transition | background-color 0.5s ease-in-out |
| Painted layers | nav.sc-408ba553-0.fVYeQF 1425.0x60.0 bg #000000 @ 0.7; a::before.sc-bfd2ca80-0.dDxZmm autoxauto bg #dddddd r 8px; a::before.sc-bfd2ca80-0.dDxZmm 140.406pxx44px bg #dddddd r 8px |
| How | resting state |

Crops: `header-bar-default.png`.

#### header-logo

HBO Max wordmark. The wordmark link at the left of the navbar.

Page: /sg/en. Selector: `nav a[aria-label*="home" i], nav a svg`. States: .

Not found on the page at capture time.

#### header-nav-link

Navbar link. A section link in the navbar (Browse, Series, Movies — whichever renders).

Page: /sg/en. Selector: `nav a`. States: .

Not found on the page at capture time.

#### header-signin

"Sign In" button. The pill button that leads to auth.hbomax.com — hovered and focused only, never pressed (pressing would leave the public site).

Page: /sg/en. Selector: `a (text Sign In)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 136 x 44 | = | - | = |
| Padding | 10px 18px | = | - | = |
| Border | none | = | - | = |
| Radius | 8px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Max Sans 18px/28.8px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Text node | span.sc-bfd2ca80-3.hvTQkZ: Max Sans 15.385px/20.7698px 700, #ffffff | = | - | = |
| Transition | background-color, color, opacity 0.2s cubic-bezier(0, 0, 0.34, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| ::before | 136px x 44px, absolute, bg #000000 @ 0, radius 8px | = | - | = |
| How | resting state | mouse hover over the element | - | CDP CSS.forcePseudoState(:active:hover) — no real press |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `header-signin-default.png`, `header-signin-hover.png`, `header-signin-pressed.png`.

### Hero

#### hero-carousel

Hero carousel. The full-bleed autoplay carousel under the navbar — backdrop art, title treatment, a "Start Subscription" CTA per slide.

Page: /sg/en. Selector: `.carousel, [class*="carousel"], [class*="Carousel"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 694.22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Max Sans 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2: Max Sans 35px/47.25px 600, #ffffff |
| Transition | none |
| Icon | 14 x 26, colour #ffffff |
| Painted layers | li 256.1x98.6 border T:10px solid / B:10px solid r 100%; li 292.1x98.6 border T:10px solid / B:10px solid r 100%; li 410.6x98.6 border T:10px solid / B:10px solid r 100%; li.active 261.8x98.6 border T:10px solid / B:10px solid r 100%; li 244.0x98.6 border T:10px solid / B:10px solid r 100%; li 239.6x98.6 border T:10px solid / B:10px solid r 100% |
| Ancestor paint | 1 up main.w-100.min-vh-100 bg #000000 |
| How | resting state |

Crops: `hero-carousel-default.png`.

#### hero-cta

Slide CTA ("Start Subscription"). The white pill call-to-action in the active slide — an auth.hbomax.com link, hovered and focused but never pressed.

Page: /sg/en. Selector: `a (text Start Subscription/Subscribe/Sign Up)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140.41 x 44 | = | - | - |
| Padding | 10px 18px | = | - | - |
| Border | none | = | - | - |
| Radius | 8px | = | - | - |
| Background | transparent | = | - | - |
| Box shadow | none | = | - | - |
| Outline | none | = | - | - |
| Font | Max Sans 18px/28.8px 400 | = | - | - |
| Letter spacing | normal | = | - | - |
| Colour | #000000 | = | - | - |
| Text node | span.sc-bfd2ca80-3.hvTQkZ: Max Sans 15.385px/20.7698px 700, #000000 | = | - | - |
| Transition | background-color, color, opacity 0.2s cubic-bezier(0, 0, 0.34, 1) | = | - | - |
| Cursor | pointer | = | - | - |
| ::before | 140.406px x 44px, absolute, bg #dddddd, radius 8px | = | - | - |
| Painted layers | a::before.sc-bfd2ca80-0.dDxZmm 140.406pxx44px bg #dddddd r 8px | = | - | - |
| How | resting state | mouse hover over the element | - | - |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |
| Error | - | = | = | cdpSession.send: Protocol error (DOM.getNodeForLocation): No node found at given location |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`.

#### hero-next

Carousel "Next" control. The arrow that advances the hero — "opened" is the slide reached by its own press (a local UI toggle).

Page: /sg/en. Selector: `.carousel-control-next, [class*="carousel"] [aria-label*="next" i], [class*="carousel"] button:last-of-type`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 76.72 x 488.56 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Max Sans 18px/28.8px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | opacity 0.15s ease | = | = |
| Opacity | 0.5 | = | = |
| Cursor | pointer | = | = |
| Icon | 14 x 26, colour #ffffff | = | = |
| How | resting state | mouse hover over the element | the carousel Next arrow's own press — the slide advanced one step |

Crops: `hero-next-default.png`, `hero-next-hover.png`, `hero-next-opened.png`.

#### hero-indicator

Carousel indicator. A slide indicator tab under the hero.

Page: /sg/en. Selector: `.carousel-indicators [data-bs-target], .carousel-indicators li, .carousel-indicators button`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 256.09 x 98.63 | = |
| Padding | 0px 56px | = |
| Border | T: 10px solid #000000 @ 0; R: none; B: 10px solid #000000 @ 0; L: none | = |
| Radius | 100% | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Max Sans 56px/89.6px 100 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | all 0.5s ease-in-out | = |
| Transform | matrix(0.9, 0, 0, 0.9, 0, 0) | = |
| Opacity | 0.5 | = |
| Cursor | pointer | = |
| Painted layers | li 256.1x98.6 border T:10px solid / B:10px solid r 100% | = |
| How | resting state | mouse hover over the element |

Crops: `hero-indicator-default.png`, `hero-indicator-hover.png`.

#### hero-slide

Active carousel slide. The currently painted slide: backdrop image, title and meta row.

Page: /sg/en. Selector: `.carousel .carousel-item.active`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1096 x 430.97 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Max Sans 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | all 0.5s ease-in-out |
| How | resting state |

Crops: `hero-slide-default.png`.

### Plans

#### plan-section

Plans section. The "Choose your plan" section: billing toggle plus the tier cards.

Page: /sg/en. Selector: `[class*="plan" i], section:has-text("plan")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 591 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | url(…) |
| Box shadow | none |
| Outline | none |
| Font | Max Sans 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h1: Max Sans 64px/86.4px 700, #ffffff |
| Transition | opacity, transform 1s ease |
| Icon | 83.45 x 59.98, colour #ffffff |
| ::before | 1425px x 591px, absolute, bg #000000 @ 0 linear-gradient(0deg, #000000 30%, #000000 @ 0 120%), radius 0px |
| Painted layers | section::before.sc-678a58aa-0.bBiobf 1425pxx591px image linear-gradient(0deg, #000000 30%, #000000 @ 0 120%); a::before.sc-bfd2ca80-0.dDxZmm 186.875pxx52px bg #dddddd r 8px; a 132.5x12.0 border T:2px solid / R:2px solid / B:2px solid / L:2px solid; a::before autox1.5px image linear-gradient(to top, #ffffff @ 0.8 0px, #ffffff @ 0.8 1px, #000000 @ 0 1px) |
| Ancestor paint | 1 up main.w-100.min-vh-100 bg #000000 |
| How | resting state |

Crops: `plan-section-default.png`.

#### plan-card

Plan tier card. One subscription tier card: name, price, feature list and its Choose button.

Page: /sg/en. Selector: `[class*="plan-card" i], [class*="tier" i], [class*="PlanCard"]`. States: .

Not found on the page at capture time.

#### plan-toggle

Billing period toggle. The monthly/yearly switch above the cards. "opened" is the prices repainted by its own press — the plan-yearly screenshot shows the result.

Page: /sg/en. Selector: `[class*="toggle" i] button, [role="switch"], [class*="billing" i] button`. States: .

Not found on the page at capture time.

#### plan-choose

"Choose" plan button. The button on a tier card that leads to checkout — hovered and focused only, never pressed.

Page: /sg/en. Selector: `button/a (text Choose/Select/Continue)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 292.95 x 52 | = | - | - |
| Padding | 10px 30px | = | - | - |
| Border | none | = | - | - |
| Radius | 8px | = | - | - |
| Background | transparent | = | - | - |
| Box shadow | none | = | - | - |
| Outline | none | = | - | - |
| Font | Max Sans 18px/28.8px 600 | = | - | - |
| Letter spacing | normal | = | - | - |
| Colour | #000000 | = | - | - |
| Text node | span.sc-bfd2ca80-3.hvTQkZ: Max Sans 20px/27px 700, #000000 | = | - | - |
| Transition | background-color, color, opacity 0.2s cubic-bezier(0, 0, 0.34, 1) | = | - | - |
| Cursor | pointer | = | - | - |
| ::before | 292.953px x 52px, absolute, bg #dddddd, radius 8px | = | - | - |
| Painted layers | a::before.sc-bfd2ca80-0.dDxZmm 292.953pxx52px bg #dddddd r 8px | = | - | - |
| How | resting state | mouse hover over the element | - | - |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |
| Error | - | = | = | cdpSession.send: Protocol error (DOM.getNodeForLocation): No node found at given location |

Crops: `plan-choose-default.png`, `plan-choose-hover.png`.

### FAQ

#### faq-section

FAQ section. The "Questions" accordion near the foot of the home page.

Page: /sg/en. Selector: `.max-section-faq, [class*="faq" i]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 391 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Max Sans 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.sc-538ece39-1.dliVFk: Max Sans 20px/27px 700, #ffffff |
| Transition | none |
| Icon | 24 x 24, colour #ffffff |
| Painted layers | div.sc-24ae6219-0.iVmMkq 920.0x391.0 bg #dddddd @ 0.1 r 8px; div.sc-7be0c765-0.kYwFex 872.0x1.0 bg #ffffff @ 0.3; div.sc-7be0c765-0.kYwFex 872.0x1.0 bg #ffffff @ 0.3; div.sc-7be0c765-0.kYwFex 872.0x1.0 bg #ffffff @ 0.3; div.sc-7be0c765-0.kYwFex 872.0x1.0 bg #ffffff @ 0.3; div.sc-7be0c765-0.kYwFex 872.0x1.0 bg #ffffff @ 0.3 |
| Ancestor paint | 1 up main.w-100.min-vh-100 bg #000000 |
| How | resting state |

Crops: `faq-section-default.png`.

#### faq-item

FAQ accordion item. One question row. "opened" is its own chevron press revealing the answer.

Page: /sg/en. Selector: `.max-section-faq button, [class*="faq" i] button`. States: default, hover, focus-visible, opened.

| Property | default | hover | focus-visible | opened |
|---|---|---|---|---|
| Size (w x h) | 920 x 55 | = | - | = |
| Padding | 14px 24px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Max Sans 18px/28.8px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Text node | div.sc-538ece39-1.dliVFk: Max Sans 20px/27px 700, #ffffff | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 24 x 24, colour #ffffff | = | - | = |
| Ancestor paint | 1 up div.sc-24ae6219-0.iVmMkq bg #dddddd @ 0.1 | = | - | = |
| How | resting state | mouse hover over the element | - | the item's own press — the answer expanded |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `faq-item-default.png`, `faq-item-hover.png`, `faq-item-opened.png`.

### Content rails

#### rail-section

Content rail. A horizontal "Discover" row of title cards.

Page: /sg/en. Selector: `[class*="shelf" i], [class*="rail" i], [class*="carousel" i]:below(:text("Discover"))`. States: .

Not found on the page at capture time.

#### rail-card

Title card link. A poster card in a rail — a link to the title's detail page.

Page: /sg/en. Selector: `main a[href*="/show/"], main a[href*="/movie/"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 350 x 141.05 | = | - |
| Padding | 0px | = | - |
| Border | none | = | - |
| Radius | 0px | = | - |
| Background | transparent | = | - |
| Box shadow | none | = | - |
| Outline | none | = | - |
| Font | Max Sans 18px/28.8px 400 | = | - |
| Letter spacing | normal | = | - |
| Colour | #ffffff | = | - |
| Text node | p.sc-3477fb85-0.gpxYhN: Max Sans 14px/18.9px 600, #ffffff | = | - |
| Transition | none | = | - |
| Cursor | pointer | = | - |
| How | resting state | mouse hover over the element | - |
| Skipped | - | = | focus failed: keyboard focus did not reach the element |

Crops: `rail-card-default.png`, `rail-card-hover.png`.

#### browse-rail-section

Content rail. A horizontal "Discover" row of title cards.

Page: /sg/en/movies. Selector: `[class*="shelf" i], [class*="rail" i], [class*="carousel" i]:below(:text("Discover"))`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 768 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | url(…) |
| Box shadow | none |
| Outline | none |
| Font | Max Sans 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h1.text-left: Max Sans 48px/57.6px 600, #ffffff |
| Transition | none |
| ::before | 1425px x 768px, absolute, bg #000000 @ 0 linear-gradient(#000000 @ 0.6 0%, #000000 @ 0 19.6%), radial-gradient(97.07% 97.07% at 60.4% -13.07%, #000000 @ 0 56.64%, radius 0px |
| Painted layers | section::before.sc-678a58aa-0.bxMPcp 1425pxx768px image linear-gradient(#000000 @ 0.6 0%, #000000 @ 0 19.6%), radial-gradient(97.07% 97.07% at 60.; a::before.sc-bfd2ca80-0.dDxZmm 195.812pxx52px bg #dddddd r 8px |
| Ancestor paint | 1 up main.w-100.min-vh-100 bg #000000 |
| How | resting state |

Crops: none.

#### browse-rail-card

Title card link. A poster card in a browse row — a link to the title's detail page.

Page: /sg/en/movies. Selector: `main a[href*="/show/"], main a[href*="/movie/"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 315 x 201.28 | = | - |
| Padding | 0px | = | - |
| Border | none | = | - |
| Radius | 0px | = | - |
| Background | transparent | = | - |
| Box shadow | none | = | - |
| Outline | none | = | - |
| Font | Max Sans 18px/28.8px 400 | = | - |
| Letter spacing | normal | = | - |
| Colour | #ffffff @ 0.8 | = | - |
| Text node | span.sc-72c045a5-22.gRkBms: Max Sans 11.834px/16.0942px 700, #ffffff @ 0.8 | = | - |
| Transition | none | = | - |
| Cursor | pointer | = | - |
| Painted layers | div.sc-72c045a5-0.emcCTt 323.0x185.2 border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 4px | = | - |
| How | resting state | mouse hover over the element | - |
| Skipped | - | = | focus failed: keyboard focus did not reach the element |

Crops: `browse-rail-card-default.png`, `browse-rail-card-hover.png`.

### Footer

#### footer

Site footer. The footer: link columns, the legal row and the language selector.

Page: /sg/en. Selector: `footer`. States: .

Not found on the page at capture time.

#### footer-link

Footer link. A link in the footer columns.

Page: /sg/en. Selector: `footer a`. States: .

Not found on the page at capture time.

#### footer-legal-link

Legal link. A link in the footer's legal row (Privacy Policy, Terms of Use).

Page: /sg/en. Selector: `footer a (text Privacy/Terms)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 136 x 44 | = |
| Padding | 10px 18px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Max Sans 18px/28.8px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | span.sc-bfd2ca80-3.hvTQkZ: Max Sans 15.385px/20.7698px 700, #ffffff | = |
| Transition | background-color, color, opacity 0.2s cubic-bezier(0, 0, 0.34, 1) | = |
| Cursor | pointer | = |
| ::before | 136px x 44px, absolute, bg #000000 @ 0, radius 8px | = |
| How | resting state | mouse hover over the element |

Crops: `footer-legal-link-default.png`, `footer-legal-link-hover.png`.

#### lang-selector

Language selector. The "English" selector in the footer. "opened" is its own press listing the locales — a local UI toggle, no locale is switched.

Page: /sg/en. Selector: `[class*="language" i] button, footer button:has-text("English")`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 224 x 52 | = | = |
| Padding | 4px 14px 4px 24px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | #3e3e3e @ 0.75 | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Max Sans 20px/27px 700 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | span.sc-cd995dce-2.eezsXj: Max Sans 20px/27px 700, #ffffff | = | = |
| Transition | background-color 0.2s cubic-bezier(0, 0, 0.34, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 24 x 24, colour #ffffff | = | = |
| Painted layers | button.sc-cd995dce-4.ftdzGm 224.0x52.0 bg #3e3e3e @ 0.75 r 8px | = | = |
| How | resting state | mouse hover over the element | the selector's own press — the locale list opened, nothing chosen |

Crops: `lang-selector-default.png`, `lang-selector-hover.png`, `lang-selector-opened.png`.

### Title detail

#### detail-hero

Detail backdrop hero. The full-bleed backdrop area on a title detail page.

Page: /sg/en/show/e6e7bad9-d48d-4434-b334-7c651ffc4bdf. Selector: `[class*="hero" i], [class*="backdrop" i], [class*="detail" i]:has(img)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 842 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | url(…) |
| Box shadow | none |
| Outline | none |
| Font | Max Sans 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.text-left: Max Sans 17px/27.2px 600, #ffffff |
| Transition | none |
| Icon | 20 x 20, colour #ffffff |
| ::before | 1425px x 842px, absolute, bg #000000 @ 0 linear-gradient(#000000 @ 0.6 0%, #000000 @ 0 19.6%), radial-gradient(97.07% 97.07% at 60.4% -13.07%, #000000 @ 0 56.64%, radius 0px |
| Painted layers | section::before.sc-678a58aa-0.bCQeII 1425pxx842px image linear-gradient(#000000 @ 0.6 0%, #000000 @ 0 19.6%), radial-gradient(97.07% 97.07% at 60.; a::before.sc-bfd2ca80-0.dDxZmm 195.812pxx52px bg #dddddd r 8px; a::before.sc-bfd2ca80-0.dDxZmm 206.547pxx52px bg #3e3e3e @ 0.75 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px |
| Ancestor paint | 1 up main.w-100.min-vh-100 bg #000000 |
| How | resting state |

Crops: `detail-hero-default.png`.

#### detail-title

Title heading. The title's display heading on the detail page.

Page: /sg/en/show/e6e7bad9-d48d-4434-b334-7c651ffc4bdf. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 59.73 x 27.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Max Sans 17px/27.2px 600 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | strong: Max Sans 17px/27.2px 700, #ffffff |
| Transition | none |
| How | resting state |

Crops: `detail-title-default.png`.

#### detail-meta

Meta row. The year · rating · runtime/seasons line under the title.

Page: /sg/en/show/e6e7bad9-d48d-4434-b334-7c651ffc4bdf. Selector: `[class*="meta" i], h1 ~ *`. States: .

Not found on the page at capture time.

#### detail-cta

Detail "Start Subscription" CTA. The subscribe call-to-action on a title page — an auth link, hovered and focused only.

Page: /sg/en/show/e6e7bad9-d48d-4434-b334-7c651ffc4bdf. Selector: `a (text Start Subscription/Subscribe)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140.41 x 44 | = | - | - |
| Padding | 10px 18px | = | - | - |
| Border | none | = | - | - |
| Radius | 8px | = | - | - |
| Background | transparent | = | - | - |
| Box shadow | none | = | - | - |
| Outline | none | = | - | - |
| Font | Max Sans 18px/28.8px 400 | = | - | - |
| Letter spacing | normal | = | - | - |
| Colour | #000000 | = | - | - |
| Text node | span.sc-bfd2ca80-3.hvTQkZ: Max Sans 15.385px/20.7698px 700, #000000 | = | - | - |
| Transition | background-color, color, opacity 0.2s cubic-bezier(0, 0, 0.34, 1) | = | - | - |
| Cursor | pointer | = | - | - |
| ::before | 140.406px x 44px, absolute, bg #dddddd, radius 8px | = | - | - |
| Painted layers | a::before.sc-bfd2ca80-0.dDxZmm 140.406pxx44px bg #dddddd r 8px | = | - | - |
| How | resting state | mouse hover over the element | - | - |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |
| Error | - | = | = | cdpSession.send: Protocol error (DOM.getNodeForLocation): No node found at given location |

Crops: `detail-cta-default.png`, `detail-cta-hover.png`.

#### movie-detail-hero

Detail backdrop hero. The full-bleed backdrop area on a title detail page.

Page: /sg/en/movie/710798da-f811-40be-9ed9-3a7443e36278. Selector: `[class*="hero" i], [class*="backdrop" i], [class*="detail" i]:has(img)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 842 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | url(…) |
| Box shadow | none |
| Outline | none |
| Font | Max Sans 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.text-left: Max Sans 17px/27.2px 600, #ffffff |
| Transition | none |
| ::before | 1425px x 842px, absolute, bg #000000 @ 0 linear-gradient(#000000 @ 0.6 0%, #000000 @ 0 19.6%), radial-gradient(97.07% 97.07% at 60.4% -13.07%, #000000 @ 0 56.64%, radius 0px |
| Painted layers | section::before.sc-678a58aa-0.hXZnzx 1425pxx842px image linear-gradient(#000000 @ 0.6 0%, #000000 @ 0 19.6%), radial-gradient(97.07% 97.07% at 60.; a::before.sc-bfd2ca80-0.dDxZmm 195.812pxx52px bg #dddddd r 8px |
| Ancestor paint | 1 up main.w-100.min-vh-100 bg #000000 |
| How | resting state |

Crops: `movie-detail-hero-default.png`.

#### movie-detail-title

Title heading. The title's display heading on the detail page.

Page: /sg/en/movie/710798da-f811-40be-9ed9-3a7443e36278. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 167.64 x 27.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Max Sans 17px/27.2px 600 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | strong: Max Sans 17px/27.2px 700, #ffffff |
| Transition | none |
| How | resting state |

Crops: `movie-detail-title-default.png`.

#### movie-detail-meta

Meta row. The year · rating · runtime/seasons line under the title.

Page: /sg/en/movie/710798da-f811-40be-9ed9-3a7443e36278. Selector: `[class*="meta" i], h1 ~ *`. States: .

Not found on the page at capture time.

#### movie-detail-cta

Detail "Start Subscription" CTA. The subscribe call-to-action on a title page — an auth link, hovered and focused only.

Page: /sg/en/movie/710798da-f811-40be-9ed9-3a7443e36278. Selector: `a (text Start Subscription/Subscribe)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140.41 x 44 | = | - | - |
| Padding | 10px 18px | = | - | - |
| Border | none | = | - | - |
| Radius | 8px | = | - | - |
| Background | transparent | = | - | - |
| Box shadow | none | = | - | - |
| Outline | none | = | - | - |
| Font | Max Sans 18px/28.8px 400 | = | - | - |
| Letter spacing | normal | = | - | - |
| Colour | #000000 | = | - | - |
| Text node | span.sc-bfd2ca80-3.hvTQkZ: Max Sans 15.385px/20.7698px 700, #000000 | = | - | - |
| Transition | background-color, color, opacity 0.2s cubic-bezier(0, 0, 0.34, 1) | = | - | - |
| Cursor | pointer | = | - | - |
| ::before | 140.406px x 44px, absolute, bg #dddddd, radius 8px | = | - | - |
| Painted layers | a::before.sc-bfd2ca80-0.dDxZmm 140.406pxx44px bg #dddddd r 8px | = | - | - |
| How | resting state | mouse hover over the element | - | - |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |
| Error | - | = | = | cdpSession.send: Protocol error (DOM.getNodeForLocation): No node found at given location |

Crops: `movie-detail-cta-default.png`, `movie-detail-cta-hover.png`.

### Cookie consent

#### consent-accept

"Accept All Cookies" button. The primary consent button — styles only, never pressed.

Page: /sg/en. Selector: `button (text Accept)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 152 x 52 | = | = | = |
| Padding | 10px 30px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Max Sans 18px/28.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.sc-bfd2ca80-3.hvTQkZ: Max Sans 20px/27px 700, #000000 | = | = | = |
| Transition | background-color, color, opacity 0.2s cubic-bezier(0, 0, 0.34, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 152px x 52px, absolute, bg #dddddd, radius 8px | 152px x 52px, absolute, bg #ffffff, radius 8px | 152px x 52px, absolute, bg #ffffff, radius 8px | = |
| Painted layers | button::before.sc-bfd2ca80-1.fqnUYL 152pxx52px bg #dddddd r 8px | button::before.sc-bfd2ca80-1.fqnUYL 152pxx52px bg #ffffff r 8px | button::before.sc-bfd2ca80-1.fqnUYL 152pxx52px bg #ffffff r 8px; button::after.sc-bfd2ca80-1.fqnUYL 162pxx62px border T:5px solid / R:5px solid / B:5px solid / L:5px solid r 13px outline 3px solid #000000 offset -6px | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |
| ::after | - | = | 162px x 62px, absolute, bg #000000 @ 0, radius 13px | = |

Crops: `consent-accept-default.png`, `consent-accept-hover.png`, `consent-accept-focus-visible.png`, `consent-accept-pressed.png`.

#### consent-manage

"Manage" / "Reject" control. A secondary consent control — styles only, never pressed.

Page: /sg/en. Selector: `button (text Manage/Reject/Settings)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 212 x 52 | = |
| Padding | 10px 30px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Max Sans 18px/28.8px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.sc-bfd2ca80-3.hvTQkZ: Max Sans 20px/27px 700, #000000 | = |
| Transition | background-color, color, opacity 0.2s cubic-bezier(0, 0, 0.34, 1) | = |
| Cursor | pointer | = |
| ::before | 212px x 52px, absolute, bg #dddddd, radius 8px | 212px x 52px, absolute, bg #ffffff, radius 8px |
| Painted layers | button::before.sc-bfd2ca80-1.fqnUYL 212pxx52px bg #dddddd r 8px | button::before.sc-bfd2ca80-1.fqnUYL 212pxx52px bg #ffffff r 8px |
| How | resting state | mouse hover over the element |

Crops: `consent-manage-default.png`, `consent-manage-hover.png`.

#### consent-dialog

Consent modal. The cookie-preferences modal that opens over a fresh visit — measured as loaded, never accepted or rejected (closePromo hides it for the other groups).

Page: /sg/en. Selector: `.modal, [role="dialog"], [class*="consent" i][class*="modal" i]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Max Sans 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h3.sc-97e6fddb-1.dwmKEE: Max Sans 28px/37.8px 600, #ffffff |
| Transition | none |
| Painted layers | div.modal-content.border-0 692.0x358.0 bg #191919 r 4.8px; div.sc-97e6fddb-4.fCEnZK 692.0x148.2 border B:1px solid; a 77.4x16.0 border T:2px solid / R:2px solid / B:2px solid / L:2px solid; a::before autox1.5px image linear-gradient(to top, #71b8f2 0px, #71b8f2 1px, #000000 @ 0 1px); a 115.6x16.0 border T:2px solid / R:2px solid / B:2px solid / L:2px solid; a::before autox1.5px image linear-gradient(to top, #71b8f2 0px, #71b8f2 1px, #000000 @ 0 1px) |
| How | resting state |

Crops: `consent-dialog-default.png`.

### Site chrome (mobile)

#### m-header

Mobile navbar. The navbar at 390px: wordmark, menu button, Sign In.

Page: /sg/en. Selector: `header nav, nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 56 |
| Padding | 8px 16px |
| Border | none |
| Radius | 0px |
| Background | #000000 @ 0.7 |
| Box shadow | none |
| Outline | none |
| Font | Max Sans 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.sc-bfd2ca80-3.hvTQkZ: Max Sans 14.72px/19.872px 700, #ffffff |
| Transition | background-color 0.5s ease-in-out |
| Painted layers | nav.sc-408ba553-0.fVYeQF 390.0x56.0 bg #000000 @ 0.7; a::before.sc-bfd2ca80-0.dDxZmm 136pxx40px bg #dddddd r 8px; a::before.sc-bfd2ca80-0.dDxZmm autoxauto bg #dddddd r 8px |
| How | resting state |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button. The button that opens the nav at 390px.

Page: /sg/en. Selector: `nav button, header button`. States: .

Not found on the page at capture time.

#### m-nav-open

Mobile nav (open). The navigation opened by the menu button's own press.

Page: /sg/en. Selector: `[class*="drawer" i], [class*="menu" i][class*="open" i], nav ul`. States: .

Not found on the page at capture time.

#### m-hero-cta

Slide CTA at 390px. The "Start Subscription" pill under the hero at phone width.

Page: /sg/en. Selector: `a (text Start Subscription)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 136 x 40 |
| Padding | 8px 20px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Max Sans 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.sc-bfd2ca80-3.hvTQkZ: Max Sans 14.72px/19.872px 700, #000000 |
| Transition | background-color, color, opacity 0.2s cubic-bezier(0, 0, 0.34, 1) |
| Cursor | pointer |
| ::before | 136px x 40px, absolute, bg #dddddd, radius 8px |
| Painted layers | a::before.sc-bfd2ca80-0.dDxZmm 136pxx40px bg #dddddd r 8px |
| How | resting state |

Crops: `m-hero-cta-default.png`.

### Legal prose

#### legal-h1

Legal page title. The "Privacy Policy" heading.

Page: /privacy. Selector: `main h1, h1`. States: .

Not found on the page at capture time.

#### legal-p

Legal paragraph. A body paragraph of the policy.

Page: /privacy. Selector: `main p, article p, p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1348 x 29.91 |
| Padding | 0px 0px 0px 30px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Muli 17.6px/29.92px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | resting state |

Crops: `legal-p-default.png`.

#### legal-link

Legal inline link. A link inside the policy prose.

Page: /privacy. Selector: `main p a, article a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 111.92 x 22 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Muli 17.6px/29.92px 400 | = |
| Letter spacing | normal | = |
| Colour | #317ab9 | = |
| Transition | none | = |
| Cursor | pointer | = |
| ::after | auto x auto, static, bg #000000 @ 0, radius 0px | = |
| How | resting state | mouse hover over the element |

Crops: `legal-link-default.png`, `legal-link-hover.png`.

## Transitions declared in the readable stylesheets

www.hbomax.com serves its own CSS same-origin (/dotcom/generated and /dotcom/_next/static), so this list is the site's own transition declarations the CSSOM could read on each page.

- /privacy: `border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out`, `color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-ou`, `opacity 0.15s linear`, `height 0.35s`, `transform 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-i`, `background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-`, `width 0.6s`, `transform 0.3s ease-out`, `transform 0.6s ease-in-out`, `opacity 0.6s`, `opacity 0.15s`, `transform 420ms cubic-bezier(0.165, 0.84, 0.44, 1)`

- /sg/en: `color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-ou`, `transform 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-i`, `background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-`, `border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out`, `transform 0.3s ease-out`, `transform 0.6s ease-in-out`, `opacity 0.6s`, `opacity 0.15s`, `background-color 0.5s ease-in-out`, `max-height 2s cubic-bezier(0, 1, 0, 1)`, `max-height 2s ease-in-out`, `0.3s`

- /sg/en/movie/710798da-f811-40be-9ed9-3a7443e36278: `color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-ou`, `transform 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-i`, `background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-`, `border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out`, `transform 0.3s ease-out`, `transform 0.6s ease-in-out`, `opacity 0.6s`, `opacity 0.15s`, `background-color 0.5s ease-in-out`, `max-height 2s cubic-bezier(0, 1, 0, 1)`, `max-height 2s ease-in-out`, `0.3s`

- /sg/en/movies: `color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-ou`, `transform 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-i`, `background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-`, `border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out`, `transform 0.3s ease-out`, `transform 0.6s ease-in-out`, `opacity 0.6s`, `opacity 0.15s`, `background-color 0.5s ease-in-out`, `max-height 2s cubic-bezier(0, 1, 0, 1)`, `max-height 2s ease-in-out`, `0.3s`

- /sg/en/show/e6e7bad9-d48d-4434-b334-7c651ffc4bdf: `color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-ou`, `transform 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-i`, `background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-`, `border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out`, `transform 0.3s ease-out`, `transform 0.6s ease-in-out`, `opacity 0.6s`, `opacity 0.15s`, `background-color 0.5s ease-in-out`, `max-height 2s cubic-bezier(0, 1, 0, 1)`, `max-height 2s ease-in-out`, `0.3s`
