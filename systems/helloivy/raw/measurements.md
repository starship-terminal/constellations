# Component measurements

Computed styles read from www.helloivy.co and app.helloivy.co on 2026-11-17 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is the login field clicked into (nothing typed); `dark` is the same element after the footer's own "Change theme" toggle repainted html[toggle-theme=dark]; `opened` and the rest are resting states reached by a component's own UI toggle. Nothing was typed, sent or signed into.

## Components

### Site chrome

#### nav-bar

Top navigation bar. The fixed top strip: the Hello Ivy wordmark, Features / Pricing / About / Docs / Blog links, the "Get Started" CTA and the bordered menu box.

Page: home. Selector: `header/nav (top strip)`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 1392 x 116 | = |
| Padding | 0px | = |
| Gap | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | #ffffff |
| Text node | a.framer-text.framer-styles-preset-16lr516: Inter 16px/19.2px 600, #000000 | a.framer-text.framer-styles-preset-16lr516: Inter 16px/19.2px 600, #edecda |
| Transition | none | = |
| Cursor | none | = |
| Icon | 124 x 60, colour #0000ee, fill #000000 | 124 x 60, colour #9e9eff, fill #000000 |
| ::after | 1392px x 116px, absolute, bg #000000 @ 0, radius 0px | = |
| Painted layers | div::after.framer-qTIUJ.framer-o0W2X 1392pxx116px border T:1px solid / R:1px solid / B:1px solid / L:1px solid; div::after.framer-1n1l10e 1232pxx116px border R:1px solid; a.framer-1lje3.framer-12mefgs 154.0x56.0 bg #000000 r 9999px; div::after.framer-p1xt7c 160pxx116px border R:1px solid; div.framer-ig1a2v 104.0x1.0 bg #000000; div.framer-1wtprsd 64.0x1.0 bg #000000 | div::after.framer-qTIUJ.framer-o0W2X 1392pxx116px border T:1px solid / R:1px solid / B:1px solid / L:1px solid; div::after.framer-1n1l10e 1232pxx116px border R:1px solid; a.framer-1lje3.framer-12mefgs 154.0x56.0 bg #faf6f0 r 9999px; div::after.framer-p1xt7c 160pxx116px border R:1px solid; div.framer-ig1a2v 104.0x1.0 bg #edecda; div.framer-1wtprsd 64.0x1.0 bg #edecda |
| How | resting state | same element after the footer "Change theme" toggle repaints html[toggle-theme=dark] |

Crops: `nav-bar-default.png`, `nav-bar-dark.png`.

#### nav-link

Nav link. A nav item in the top strip ("Pricing").

Page: home. Selector: `nav link`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 55 x 20 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | Inter 16px/19.2px 600 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | none | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | a.framer-text.framer-styles-preset-16lr516 55.0x20.0 outline 1px auto #101010 offset 1px |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`.

#### nav-cta

"Get Started" nav button. The solid call-to-action at the right of the nav — links to app.helloivy.co; measured, never followed.

Page: home. Selector: `a/button (text Get Started)`. States: default, hover, focus-visible, pressed, dark.

| Property | default | hover | focus-visible | pressed | dark |
|---|---|---|---|---|---|
| Size (w x h) | 154 x 56 | = | = | = | = |
| Padding | 15px 30px | = | = | = | = |
| Gap | 10px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | #000000 | = | = | = | #faf6f0 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = | = |
| Font | sans-serif 12px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #0000ee | = | = | = | #9e9eff |
| Text node | p.framer-text: Inter 16px/19.2px 600, #ffffff | = | = | = | p.framer-text: Inter 16px/19.2px 600, #000000 |
| Transition | none | = | = | = | = |
| Cursor | none | = | = | = | = |
| Painted layers | a.framer-1lje3.framer-12mefgs 154.0x56.0 bg #000000 r 9999px | = | a.framer-1lje3.framer-12mefgs 154.0x56.0 bg #000000 r 9999px outline 1px auto #101010 offset 1px | = | a.framer-1lje3.framer-12mefgs 154.0x56.0 bg #faf6f0 r 9999px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press | same element after the footer "Change theme" toggle repaints html[toggle-theme=dark] |
| Opacity | - | 0.8 | = | = | = |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`, `nav-cta-dark.png`.

#### nav-menu-box

Menu box. The bordered hamburger box at the nav's right edge — opens the 01 HOME / 02 FEATURES … overlay. "opened" is its own press, closed with Escape.

Page: home. Selector: `[data-framer-name="Menu"]`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 160 x 116 | = | 1440 x 381.02 |
| Padding | 24px | = | 0px 0px 0px 48px |
| Gap | 24px | = | 10px |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | sans-serif 12px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | none | = | = |
| ::after | 160px x 116px, absolute, bg #000000 @ 0, radius 0px | = | - |
| Painted layers | div::after.framer-p1xt7c 160pxx116px border R:1px solid; div.framer-ig1a2v 104.0x1.0 bg #000000; div.framer-1wtprsd 64.0x1.0 bg #000000; div.framer-4opjpw 104.0x1.0 bg #000000 | div::after.framer-p1xt7c 160pxx116px border R:1px solid; div.framer-ig1a2v 104.0x1.0 bg #000000; div.framer-1wtprsd 104.0x1.0 bg #000000; div.framer-4opjpw 104.0x1.0 bg #000000 | - |
| How | resting state | mouse hover over the element | the menu box's own press (overlay open; reloaded afterwards) |
| Text node | - | = | p.framer-text.framer-styles-preset-1tg37r6: Inter 24px/33.6px 500, #000000 |

Crops: `nav-menu-box-default.png`, `nav-menu-box-hover.png`, `nav-menu-box-opened.png`.

#### footer

Footer. The page footer: product/resource columns, the social icons, the "Change theme" control and the "Try it for free" CTA.

Page: home. Selector: `footer (the whole block)`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 1392 x 560.41 | = |
| Padding | 0px | = |
| Gap | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | #ffffff |
| Text node | h3.framer-text.framer-styles-preset-1nnq1zc: Unbounded 62px/68.2px 500, #000000 | h3.framer-text.framer-styles-preset-1nnq1zc: Unbounded 62px/68.2px 500, #edecda |
| Transition | none | = |
| Cursor | none | = |
| Icon | 48 x 48, colour #000000 | 48 x 48, colour #edecda |
| ::after | 1392px x 560.406px, absolute, bg #000000 @ 0, radius 0px | = |
| Painted layers | div::after.framer-MCeyU.framer-BAp5c 1392pxx560.406px border T:1px solid / R:1px solid / B:1px solid / L:1px solid; div::after.framer-cmnq2x 1392pxx116.203px border B:1px solid; div.framer-1r83dga 9.0x9.0 bg #000000 r 100px; div::after.framer-ivcetf 1392pxx377px border B:1px solid; div::after.framer-1ddini9 278.391pxx377px border R:1px solid; div::after.framer-14gy5od 278.406pxx377px border R:1px solid | div::after.framer-MCeyU.framer-BAp5c 1392pxx560.406px border T:1px solid / R:1px solid / B:1px solid / L:1px solid; div::after.framer-cmnq2x 1392pxx116.203px border B:1px solid; div.framer-1r83dga 9.0x9.0 bg #edecda r 100px; div::after.framer-ivcetf 1392pxx377px border B:1px solid; div::after.framer-1ddini9 278.391pxx377px border R:1px solid; div::after.framer-14gy5od 278.406pxx377px border R:1px solid |
| How | resting state | same element after the footer "Change theme" toggle repaints html[toggle-theme=dark] |

Crops: `footer-default.png`, `footer-dark.png`.

#### theme-control

"Change theme" control. The footer's own theme toggle — the control that repaints html[toggle-theme] and writes localStorage.currentToggleState. Measured at rest; the painted dark pass lives on the `dark` states of other components.

Page: home. Selector: `footer leaf (text Change theme)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 96 x 21 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/21px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | none | = |
| How | resting state | mouse hover over the element |

Crops: `theme-control-default.png`, `theme-control-hover.png`.

#### footer-link

Footer link. A footer column link (a product page) — an anchor inside the measured footer block.

Page: home. Selector: `a inside the footer block`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 34 x 17 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | none | = |
| How | resting state | mouse hover over the element |

Crops: `footer-link-default.png`, `footer-link-hover.png`.

### Marketing

#### hero-heading

Hero heading (h1). The page's headline — the largest display type on the site.

Page: home. Selector: `h1`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 1344 x 180.41 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Unbounded 82px/90.2px 500 | = |
| Letter spacing | normal | = |
| Colour | #000000 | #faf6f0 |
| Transition | none | = |
| Cursor | none | = |
| How | resting state | same element after the footer "Change theme" toggle repaints html[toggle-theme=dark] |

Crops: `hero-heading-default.png`, `hero-heading-dark.png`.

#### hero-copy

Hero paragraph. The supporting paragraph under the headline.

Page: home. Selector: `p (sentence)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1238 x 121.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 27px/40.5px 400 |
| Letter spacing | -0.54px |
| Colour | #000000 |
| Transition | none |
| Cursor | none |
| How | resting state |

Crops: `hero-copy-default.png`.

#### hero-cta

Hero call-to-action. The trial CTA — the floating "Try it for free" pill painted bottom-right on the marketing pages — links to the app, measured never followed.

Page: home. Selector: `a/button (trial CTA, outside the nav)`. States: default, hover, focus-visible, dark, pressed.

| Property | default | hover | focus-visible | dark | pressed |
|---|---|---|---|---|---|
| Size (w x h) | 196 x 56 | = | = | = | = |
| Padding | 15px 30px | = | = | = | = |
| Gap | 10px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | #000000 | = | = | #faf6f0 | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = | = |
| Font | sans-serif 12px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #0000ee | = | = | #9e9eff | #ff0000 |
| Text node | p.framer-text: Inter 16px/19.2px 600, #ffffff | = | = | p.framer-text: Inter 16px/19.2px 600, #000000 | = |
| Transition | none | = | = | = | = |
| Cursor | none | = | = | = | = |
| Icon | 17 x 22, colour #0000ee, fill #000000 | = | = | 17 x 22, colour #9e9eff, fill #000000 | 17 x 22, colour #ff0000, fill #000000 |
| Painted layers | a.framer-1lje3.framer-12mefgs 196.0x56.0 bg #000000 r 9999px | = | a.framer-1lje3.framer-12mefgs 196.0x56.0 bg #000000 r 9999px outline 1px auto #101010 offset 1px | a.framer-1lje3.framer-12mefgs 196.0x56.0 bg #faf6f0 r 9999px | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | same element after the footer "Change theme" toggle repaints html[toggle-theme=dark] | CDP CSS.forcePseudoState(:active:hover) — no real press |
| Opacity | - | 0.8 | = | = | = |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-dark.png`, `hero-cta-pressed.png`.

#### section-heading

Section heading (h3). A mid-page section heading — the page's display type below the h1.

Page: home. Selector: `h3`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 800 x 136.41 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Unbounded 62px/68.2px 500 | = |
| Letter spacing | normal | = |
| Colour | #000000 | #edecda |
| Transition | none | = |
| Cursor | none | = |
| How | resting state | same element after the footer "Change theme" toggle repaints html[toggle-theme=dark] |

Crops: `section-heading-default.png`, `section-heading-dark.png`.

### Pricing

#### plan-card

Plan card. A pricing card ("Grow" / "Business" / "Enterprise"): name, price, allowance rows and its CTA.

Page: pricing. Selector: `box (priced plan with its own CTA)`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 464 x 571 | = |
| Padding | 0px | = |
| Gap | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | #ffffff |
| Text node | h6.framer-text.framer-styles-preset-73gayi: Unbounded 20px/28px 500, #000000, ls 0.4px | h6.framer-text.framer-styles-preset-73gayi: Unbounded 20px/28px 500, #edecda, ls 0.4px |
| Transition | none | = |
| Cursor | none | = |
| Icon | 20 x 20, colour #000000 | 20 x 20, colour #ffffff, fill #000000 |
| Painted layers | div::after.framer-1fhyswc 464pxx166.391px border B:1px solid; a.framer-vVI5g.framer-4vbkq 416.0x49.6 bg #000000 | div::after.framer-1fhyswc 464pxx166.391px border B:1px solid; a.framer-vVI5g.framer-4vbkq 416.0x49.6 bg #edecda |
| How | resting state | same element after the footer "Change theme" toggle repaints html[toggle-theme=dark] |

Crops: `plan-card-default.png`, `plan-card-dark.png`.

#### plan-cta

Plan CTA button. A plan's call-to-action inside the measured plan card — links to the app; measured, never followed.

Page: pricing. Selector: `a/button inside the plan card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 416 x 49.59 | = | = | = |
| Padding | 12px 20px | = | = | = |
| Gap | 6px | 12px | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | h1.framer-text.framer-styles-preset-1fllz1t: Unbounded 16px/25.6px 500, #faf6f0, ls 0.48px | = | = | = |
| Transition | none | = | = | = |
| Cursor | none | = | = | = |
| Painted layers | a.framer-vVI5g.framer-4vbkq 416.0x49.6 bg #000000 | = | a.framer-vVI5g.framer-4vbkq 416.0x49.6 bg #000000 outline 1px auto #101010 offset 1px | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### faq-question

FAQ accordion question. A question row in the pricing FAQ. "opened" is its own press revealing the answer, pressed again to close.

Page: pricing. Selector: `row (text Is Hello Ivy only useful for design teams?)`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 1300 x 25.59 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter-Medium 16px/25.6px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | none | = | = |
| How | resting state | mouse hover over the element | the question row's own press (answer visible; pressed again to close) |

Crops: `faq-question-default.png`, `faq-question-hover.png`, `faq-question-opened.png`.

### Features

#### feature-card

Feature card. A feature tile on /features — an illustration, name and description.

Page: features. Selector: `box (feature tile)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 300 x 40.8 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h4.framer-text.framer-styles-preset-9cjmkx: Unbounded 34px/40.8px 500, #000000, ls 0.34px | = |
| Transition | none | = |
| Cursor | none | = |
| How | resting state | mouse hover over the element |

Crops: `feature-card-default.png`, `feature-card-hover.png`.

### Blog

#### post-card

Post card. A post row/card on the blog index — cover, title, excerpt, date.

Page: blog. Selector: `box (post card)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 464 x 607.08 | = |
| Padding | 0px | = |
| Gap | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #0000ee | = |
| Text node | p.framer-text.framer-styles-preset-1j07l0l: Inter-Medium 16px/25.6px 500, #999999 | = |
| Transition | none | = |
| Cursor | none | = |
| ::after | 464px x 607.078px, absolute, bg #000000 @ 0, radius 0px | = |
| Painted layers | a::after.framer-myzsC.framer-MJX7Q 464pxx607.078px border T:1px solid / R:1px solid / B:1px solid / L:1px solid; div::after.framer-inu18k 464pxx424.703px border B:1px solid | a::after.framer-myzsC.framer-MJX7Q 464pxx607.078px border T:1px solid / R:1px solid / B:1px solid / L:1px solid; div::after.framer-inu18k 510.391pxx467.172px border B:1px solid |
| How | resting state | mouse hover over the element |

Crops: `post-card-hover.png`.

### Docs

#### docs-nav

Docs sidebar. The docs index navigation — the section list (Getting Started, Main tools, …) beside the content.

Page: doc-post. Selector: `aside/nav (docs sections)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 200 x 134.78 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text: General Sans 14px/19.6px 600, #111111 |
| Transition | none |
| How | resting state |

Crops: `docs-nav-default.png`.

#### docs-link

Docs nav link. A docs section/article link.

Page: doc-post. Selector: `docs a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 117 x 19.59 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | General Sans 14px/19.6px 600 | = |
| Letter spacing | normal | = |
| Colour | #111111 | = |
| Transition | none | = |
| How | resting state | mouse hover over the element |

Crops: `docs-link-default.png`, `docs-link-hover.png`.

### App login

#### login-card

Login card. The centred card on app.helloivy.co/login ("Welcome back", email/password fields, Continue, Google). The auth boundary: nothing is entered or submitted.

Page: login. Selector: `form/card (login)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 500 x 498.84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 15px/22.5px 400 |
| Letter spacing | normal |
| Colour | #37352f |
| Text node | p.auth-title: Inter 23px/27.6px 600, #37352f |
| Transition | none |
| Icon | 30 x 20, colour #707b8b |
| Painted layers | input.w-full.outline-none 500.0x48.5 bg #fcfcfc border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 10px outline 2px solid #000000 @ 0 offset 2px; input.w-full.outline-none 500.0x48.5 bg #fcfcfc border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 10px outline 2px solid #000000 @ 0 offset 2px; button.inline-flex.items-center 500.0x53.3 bg #222222 r 10px; button.inline-flex.items-center 500.0x56.0 border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 10px; div.w-full.border-t 500.0x1.0 border T:1px solid; span.px-10.pt-10 34.0x31.0 bg #ffffff |
| How | resting state |

Crops: `login-card-default.png`.

#### login-input-email

Email input. The "Your email" field — measured at rest; nothing is entered.

Page: login. Selector: `input[type="email"], input[name*="email" i]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 500 x 48.5 | = |
| Padding | 12px 20px | = |
| Border | 1px solid #c4c4c4 | 1px solid #777777 |
| Radius | 10px | = |
| Background | #fcfcfc | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #777777 0px 0px 0px 0.5px |
| Outline | 2px solid #000000 @ 0 offset 2px | = |
| Font | Inter 15px/22.5px 400 | = |
| Letter spacing | normal | = |
| Colour | #222222 | #000000 |
| Transition | all 0.05s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #bbbbbb, opacity 1 | = |
| Painted layers | input.w-full.outline-none 500.0x48.5 bg #fcfcfc border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 10px outline 2px solid #000000 @ 0 offset 2px | input.w-full.outline-none 500.0x48.5 bg #fcfcfc border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #777777 0px 0px 0px 0.5px outline 2px solid #000000 @ 0 offset 2px |
| How | resting state | the field clicked into |

Crops: `login-input-email-default.png`, `login-input-email-focused.png`.

#### login-input-password

Password input. The "Your password" field — measured at rest; nothing is entered.

Page: login. Selector: `input[type="password"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 500 x 48.5 |
| Padding | 12px 20px |
| Border | 1px solid #c4c4c4 |
| Radius | 10px |
| Background | #fcfcfc |
| Box shadow | none |
| Outline | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 15px/22.5px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | all 0.05s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | text |
| Placeholder | #bbbbbb, opacity 1 |
| Painted layers | input.w-full.outline-none 500.0x48.5 bg #fcfcfc border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 10px outline 2px solid #000000 @ 0 offset 2px |
| How | resting state |

Crops: `login-input-password-default.png`.

#### login-continue

"Continue" button. The form's submit — measured, never pressed (it would submit).

Page: login. Selector: `button (text Continue)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 500 x 53.25 | = | = |
| Padding | 16px 0px | = | = |
| Border | none | = | = |
| Radius | 10px | = | = |
| Background | #222222 | #000000 | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 17px/21.25px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Text node | span: Inter 17px/21.25px 500, #ffffff | = | = |
| Transition | all 0.05s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.inline-flex.items-center 500.0x53.3 bg #222222 r 10px | button.inline-flex.items-center 500.0x53.3 bg #000000 r 10px | button.inline-flex.items-center 500.0x53.3 bg #222222 r 10px outline 2px solid #000000 @ 0 offset 2px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `login-continue-default.png`, `login-continue-hover.png`, `login-continue-focus-visible.png`.

#### login-google

"Login with Google" button. The OAuth button — measured, never pressed.

Page: login. Selector: `button (text Login with Google)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 500 x 56 | = |
| Padding | 16px 10px | = |
| Border | 2px solid #000000 | = |
| Radius | 10px | = |
| Background | transparent | #fafafa |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/17.5px 400 | = |
| Letter spacing | normal | = |
| Colour | #707b8b | = |
| Text node | p.ml-5.text-black: Inter 15px/18.75px 400, #000000 | = |
| Transition | all 0.05s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 30 x 20, colour #707b8b | = |
| Painted layers | button.inline-flex.items-center 500.0x56.0 border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 10px | button.inline-flex.items-center 500.0x56.0 bg #fafafa border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 10px |
| How | resting state | mouse hover over the element |

Crops: `login-google-default.png`, `login-google-hover.png`.

#### login-signup

"Sign up" link. The "Don't have an account yet? Sign up" link — measured, never followed.

Page: login. Selector: `a (text Sign up)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 50 x 17 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/21px 400 | = |
| Letter spacing | normal | = |
| Colour | #111111 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | resting state | mouse hover over the element |

Crops: `login-signup-default.png`, `login-signup-hover.png`.

#### login-forgot

"Forgot password?" link. The reset link — measured, never followed.

Page: login. Selector: `a (text Forgot password?)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 112 x 19.5 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 13px/19.5px 400 | = |
| Letter spacing | normal | = |
| Colour | #37352f | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | resting state | mouse hover over the element |

Crops: `login-forgot-default.png`, `login-forgot-hover.png`.

### Share document

#### share-header

Share page header. The document page's top strip — the "hello ivy" name and the Settings button.

Page: share. Selector: `header/toolbar (share)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1000 x 68.75 |
| Padding | 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 15px/22.5px 400 |
| Letter spacing | normal |
| Colour | #37352f |
| Text node | p.font-medium.pr-1: Inter 15px/22.5px 500, #000000 |
| Transition | none |
| Ancestor paint | 1 up div.fixed.top-0 bg #ffffff |
| How | resting state |

Crops: `share-header-default.png`.

#### share-settings

"Settings" button. The document's own settings control — a local UI toggle opening the document menu (Send to mail / Print / word count). "opened" is its own press, closed with Escape.

Page: share. Selector: `button (text Settings)`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 91 x 28.75 | = | = |
| Padding | 5px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 15px/18.75px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #37352f | = | = |
| Text node | span: Inter 15px/18.75px 400, #37352f | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Opacity | 0.5 | - | - |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | the "Settings" button's own press (menu open; Escape restores) |
| Painted layers | - | = | button.inline-flex.items-center 91.0x28.8 outline 2px solid #000000 @ 0 offset 2px |

Crops: `share-settings-default.png`, `share-settings-hover.png`, `share-settings-opened.png`.

#### share-doc

Media-kit document. The document canvas — the public marketing disclaimer, the Hello Ivy logo and product screenshots the file carries.

Page: share. Selector: `article/main (doc)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 795 x 3376.61 |
| Padding | 0px 0px 250px 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/25.6px 400 |
| Letter spacing | normal |
| Colour | #323235 |
| Text node | p: Inter 16px/25.6px 400, #323235 |
| Transition | none |
| Painted layers | div.relative.mr-10 739.5x557.4 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1.4px 6px 0px, #000000 @ 0.09 0px 3.6px 12.6px 0px; div.relative.mr-10 739.5x670.3 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1.4px 6px 0px, #000000 @ 0.09 0px 3.6px 12.6px 0px; div.relative.mr-10 739.5x557.4 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1.4px 6px 0px, #000000 @ 0.09 0px 3.6px 12.6px 0px; div.relative.mr-10 739.5x557.4 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1.4px 6px 0px, #000000 @ 0.09 0px 3.6px 12.6px 0px |
| How | resting state |

Crops: none.

### Site chrome (mobile)

#### m-nav-bar

Mobile nav bar. The top strip at 390px — wordmark and the menu box (the menu element's painted ancestor bar).

Page: home. Selector: `top strip (ancestor of Menu)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 116 |
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
| Transition | none |
| Icon | 124 x 60, colour #0000ee, fill #000000 |
| ::after | 358px x 116px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | div::after.framer-qTIUJ.framer-o0W2X 358pxx116px border T:1px solid / R:1px solid / B:1px solid / L:1px solid; div::after.framer-1n1l10e 198pxx116px border R:1px solid; div::after.framer-p1xt7c 160pxx116px border R:1px solid; div.framer-ig1a2v 104.0x1.0 bg #000000; div.framer-1wtprsd 64.0x1.0 bg #000000; div.framer-4opjpw 104.0x1.0 bg #000000 |
| How | resting state |

Crops: `m-nav-bar-default.png`.

#### m-menu-box

Menu box (drawer open). The nav menu box at 390px — a real tap opens the full-screen overlay (data-framer-name "Menu"). "opened" is its own tap, closed with Escape.

Page: home. Selector: `[data-framer-name="Menu"]`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 390 x 343.98 |
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
| Text node | p.framer-text.framer-styles-preset-1j07l0l: Inter-Medium 16px/25.6px 500, #000000 |
| Transition | none |
| Painted layers | div::after.framer-k36hk2 44pxx44px border T:1px solid / R:1px solid / B:1px solid / L:1px solid; div.framer-13cooux 19.1x19.1 bg #000000; div.framer-1itw2xu 19.1x19.1 bg #000000 |
| How | the menu box's own tap (overlay open; reloaded afterwards) |

Crops: `m-menu-box-opened.png`.

### Marketing (mobile)

#### m-hero-heading

Hero heading at 390px. The headline on the phone — the display type compressed to the small width (an h3 at this width).

Page: home. Selector: `h1,h2,h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 310 x 192.03 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Unbounded 32px/38.4px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | resting state |

Crops: `m-hero-heading-default.png`.

## Transitions declared in the readable stylesheets

www.helloivy.co is a Framer SSR build — its sheets are inline <style> blocks; app.helloivy.co serves its own CSS same-origin (/assets/index-*.css), so this list is each surface's own transition declarations the CSSOM could read on each page.

- blog: none

- doc-post: none

- features: none

- home: none

- login: `width 0.5s linear`, `0.2s ease-in-out`, `stroke 0.3s linear`, `stroke-dasharray 0.7s linear`, `var(--vc-day-content-transition)`, `transform var(--vc-slide-duration) var(--vc-slide-timing),opacity var(--vc-slide-duration)`, `opacity 0.2s ease-in-out`, `0.3s cubic-bezier(1, 0.5, 0.8, 1)`, `opacity 0.2s, visibility 0.2s`, `order 0.5s`, `background 0.4s`, `0.3s`

- pricing: none

- share: `width 0.5s linear`, `0.2s ease-in-out`, `stroke 0.3s linear`, `stroke-dasharray 0.7s linear`, `var(--vc-day-content-transition)`, `transform var(--vc-slide-duration) var(--vc-slide-timing),opacity var(--vc-slide-duration)`, `opacity 0.2s ease-in-out`, `0.3s cubic-bezier(1, 0.5, 0.8, 1)`, `opacity 0.2s, visibility 0.2s`, `order 0.5s`, `background 0.4s`, `0.3s`
