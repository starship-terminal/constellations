# Glassnode component measurements

Computed styles read from glassnode.com and its public subdomains on 2026-11-16 by `tools/capture/public/measure.mjs`, signed out, in headed Chromium under Xvfb at 1440 x 900 (the Mobile group at 390 x 844) across the surfaces' painted themes — the marketing site's light :root pages (home, /pricing/vector, /contact), the studio product shell at studio.glassnode.com /pricing (painted light; its html[data-theme="dark-theme"] layer is declared but has no public theme control, so it is captured as declared-not-painted tokens only), the Auth0 universal login at auth.glassnode.com/u/login reached through the studio's real "Log in" button (the volatile ?state= is never recorded), the Ghost publication at research.glassnode.com, the GitBook docs at docs.glassnode.com and the dark-by-default registry at tokenization.glassnode.com — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Marketing site chrome

#### mkt-header

Site header. The top bar on every marketing page: the Glassnode wordmark, the Products dropdown trigger, Pricing, Data, About and the "Launch Studio" CTA.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1208 x 72 |
| Padding | 20px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/21px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.dropdownTrigger-module-scss-module__SbGuRq__text: Inter 14px/18.2px 400, #000000 |
| Transition | none |
| Icon | 16 x 16, colour #000000 |
| Painted layers | a.style-module-scss-module__NRs3BG__button.style-module-scss-module__NRs3BG__primary 120.8x33.0 bg #1a1a1a border T:1px solid #1a1a1a / R:1px solid #1a1a1a / B:1px solid #1a1a1a / L:1px solid #1a1a1a r 2px |
| Ancestor paint | 1 up div.style-module-scss-module__LPSrhq__container bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The Glassnode wordmark in the header, linking home.

Page: home. Selector: `header a[href=/]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 100 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/21px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 2 up div.style-module-scss-module__LPSrhq__container bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-dropdown-btn

Nav dropdown trigger. The "Products" header button — aria-expanded flips and the dropdown panel mounts; a hover already opens it and a click toggles it. The opened state was measured after its own toggle.

Page: home. Selector: `header button Products`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 87.06 x 18.19 | - | = | = | = |
| Padding | 0px 4px | - | = | = | = |
| Gap | 4px | - | = | = | = |
| Border | none | - | = | = | = |
| Radius | 2px | - | = | = | = |
| Background | transparent | - | = | = | = |
| Box shadow | none | - | = | = | = |
| Outline | none | - | = | = | = |
| Font | Inter 14px/18.2px 400 | - | = | = | = |
| Letter spacing | normal | - | = | = | = |
| Colour | #000000 | - | = | = | = |
| Text node | span.dropdownTrigger-module-scss-module__SbGuRq__text: Inter 14px/18.2px 400, #000000 | - | = | = | = |
| Transition | all 0.2s cubic-bezier(0.645, 0.045, 0.355, 1) | - | = | = | = |
| Cursor | pointer | - | = | - | = |
| Icon | 16 x 16, colour #000000 | - | = | = | = |
| How | at rest | - | keydown then focus() | CDP forcePseudoState :active:hover | held open by an earlier toggle |
| Error | - | locator.hover: Timeout 5000ms exceeded. Call log:   - waiting for locator('header button').filter({ hasText: /^Products$/ }).first().first().first()     - locator resolved to <button type="button" id= | = | = | = |

Crops: `nav-dropdown-btn-default.png`, `nav-dropdown-btn-focus-visible.png`, `nav-dropdown-btn-pressed.png`, `nav-dropdown-btn-opened.png`.

#### nav-menu-item

Dropdown item. A product entry inside the opened "Products" dropdown (Studio, Data, Research, Market Compass, Alpha Lab); measured, never followed.

Page: home. Selector: `Products dropdown item`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 30.48 x 17 | = |
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
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `nav-menu-item-default.png`.

#### nav-link

Nav link. The "Pricing" header link; measured, never followed.

Page: home. Selector: `header a Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 62 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #000000 | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.style-module-scss-module__LPSrhq__externalNavLink 62.0x21.0 outline 1px auto #101010 offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-cta

Header CTA. The "Launch Studio" header action pointing at studio.glassnode.com; measured, never followed.

Page: home. Selector: `header a Launch Studio`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 120.75 x 32.97 | = | = | = |
| Padding | 6.4px 12px | = | = | = |
| Border | 1px solid #1a1a1a | = | = | 1px solid #333333 |
| Radius | 2px | = | = | = |
| Background | #1a1a1a | = | = | #333333 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 14px/18.2px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.2s cubic-bezier(0.645, 0.045, 0.355, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.style-module-scss-module__NRs3BG__button.style-module-scss-module__NRs3BG__primary 120.8x33.0 bg #1a1a1a border T:1px solid #1a1a1a / R:1px solid #1a1a1a / B:1px solid #1a1a1a / L:1px solid #1a1a1a r 2px | = | a.style-module-scss-module__NRs3BG__button.style-module-scss-module__NRs3BG__primary 120.8x33.0 bg #1a1a1a border T:1px solid #1a1a1a / R:1px solid #1a1a1a / B:1px solid #1a1a1a / L:1px solid #1a1a1a r 2px outline 1px auto #101010 offset 1px | a.style-module-scss-module__NRs3BG__button.style-module-scss-module__NRs3BG__primary 120.8x33.0 bg #333333 border T:1px solid #333333 / R:1px solid #333333 / B:1px solid #333333 / L:1px solid #333333 r 2px |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Marketing home

#### hero-h1

Hero headline. "Pioneering digital asset market intelligence" — the home masthead.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 604 x 184.31 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fraktion 51.2px/61.44px 700 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### section-h2

Section heading. A marketing section heading further down the home page ("Our flagship platform", ...) — a display-size h2, so transient microcopy never counts.

Page: home. Selector: `h2 (display size)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1208 x 44.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 32px/44.8px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

#### partner-report-link

Partner report link. The "Partner Reports" promo link under the hero ("Xapo Bank + Glassnode: Generating Yield on..."); measured, never followed.

Page: home. Selector: `a Partner Reports`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 276 x 370 | = |
| Padding | 16px | = |
| Gap | 8px | = |
| Border | 1px solid #dedfe1 | = |
| Radius | 2px | = |
| Background | #f7f8fa | = |
| Box shadow | #000000 @ 0.04 0px 2px 4px 0px | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.style-module-scss-module__fLq2pW__linkTag: Inter 12px/18px 700, #6f6f6f | = |
| Transition | all 0.2s ease | = |
| Cursor | pointer | = |
| Painted layers | a.style-module-scss-module__fLq2pW__link 276.0x370.0 bg #f7f8fa border T:1px solid #dedfe1 / R:1px solid #dedfe1 / B:1px solid #dedfe1 / L:1px solid #dedfe1 r 2px shadow #000000 @ 0.04 0px 2px 4px 0px | = |
| How | at rest | mouse hover |

Crops: `partner-report-link-default.png`, `partner-report-link-hover.png`.

### Footer

#### footer

Footer. The page footer: the research subscribe field, the Use cases/Resources/About us/Legal columns and the Privacy settings control.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 334.39 |
| Padding | 64px 72px 24px 72px |
| Border | none |
| Radius | 0px |
| Background | #1a1a1a |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/21px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.style-module-scss-module__mOJdrG__linksHeader: Inter 16px/22.4px 700, #f7f8fa |
| Transition | none |
| Icon | 24 x 24, colour #000000 |
| Painted layers | footer.style-module-scss-module__mOJdrG__footer 1425.0x334.4 bg #1a1a1a |
| How | at rest |

Crops: `footer-default.png`.

#### newsletter-field

Newsletter field. The "Enter your email" subscribe input; focused and typed into then cleared — never subscribed.

Page: home. Selector: `input[type=email] Enter your email`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 336 x 40 | = | = |
| Padding | 0px 16px | = | = |
| Border | 1px solid #808080 | = | = |
| Radius | 2px 0px 0px 2px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | 1px auto #101010 offset 0px | 1px auto #101010 offset 0px |
| Font | Inter 14px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #a0a0a0 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| Painted layers | input 336.0x40.0 border T:1px solid #808080 / R:1px solid #808080 / B:1px solid #808080 / L:1px solid #808080 r 2px 0px 0px 2px | input 336.0x40.0 border T:1px solid #808080 / R:1px solid #808080 / B:1px solid #808080 / L:1px solid #808080 r 2px 0px 0px 2px outline 1px auto #101010 offset 0px | input 336.0x40.0 border T:1px solid #808080 / R:1px solid #808080 / B:1px solid #808080 / L:1px solid #808080 r 2px 0px 0px 2px outline 1px auto #101010 offset 0px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `newsletter-field-default.png`, `newsletter-field-focused.png`, `newsletter-field-filled.png`.

#### newsletter-btn

Subscribe button. The "Send me free research" subscribe button; its states were measured but the button was never clicked — nothing was submitted.

Page: home. Selector: `Send me free research`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 184.84 x 40 | = | - | 151.58 x 21 |
| Padding | 9.6px 16px | = | - | 1px 6px |
| Border | 1px solid #dedfe1 | = | - | 2px outset #767676 @ 0.3 |
| Radius | 0px 2px 2px 0px | = | - | 0px |
| Background | #dedfe1 | = | - | #efefef @ 0.3 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 14px/18.2px 400 | = | - | Arial 13.3333px/normal 400 |
| Letter spacing | normal | = | - | = |
| Colour | #808080 | = | - | #101010 @ 0.3 |
| Transition | all 0.2s cubic-bezier(0.645, 0.045, 0.355, 1) | = | - | none |
| Cursor | not-allowed | = | - | default |
| Painted layers | button.style-module-scss-module__NRs3BG__button.style-module-scss-module__NRs3BG__secondary 184.8x40.0 bg #dedfe1 border T:1px solid #dedfe1 / R:1px solid #dedfe1 / B:1px solid #dedfe1 / L:1px solid #dedfe1 r 0px 2px 2px 0px | = | - | button.style-module-scss-module__NRs3BG__button.style-module-scss-module__NRs3BG__secondary 151.6x21.0 bg #efefef @ 0.3 border T:2px outset #767676 @ 0.3 / R:2px outset #767676 @ 0.3 / B:2px outset #767676 @ 0.3 / L:2px outset #767676 @ 0.3 |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `newsletter-btn-default.png`, `newsletter-btn-hover.png`, `newsletter-btn-pressed.png`.

#### privacy-btn

Privacy settings control. The "Privacy settings" footer control that opens the consent manager; a local UI toggle — measured, never opened.

Page: home. Selector: `Privacy settings`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 105.28 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter 14px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #dedfe1 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button 105.3x17.0 outline 1px auto #101010 offset 0px | = |

Crops: `privacy-btn-default.png`, `privacy-btn-hover.png`, `privacy-btn-focus-visible.png`, `privacy-btn-pressed.png`.

#### footer-link

Footer link. A footer sitemap link; measured, never followed.

Page: home. Selector: `footer link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.34 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 14px/14px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #dedfe1 | = | = | #f7f8fa |
| Transition | all 0.2s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 85.3x17.0 outline 1px auto #101010 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Vector pricing page

#### vec-h1

Vector headline. The /pricing/vector masthead over the Bitcoin Vector pitch.

Page: vector. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 122.88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fraktion 51.2px/61.44px 700 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| How | at rest |

Crops: `vec-h1-default.png`.

#### vec-billing-select

Billing-cycle select. The native <select> switching "Bill quarterly"/"Bill monthly" on the Vector price; measured at rest, never changed.

Page: vector. Selector: `select`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 103 x 17 | = |
| Padding | 0px 20px 0px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | 1px auto #101010 offset 0px |
| Font | Inter 14px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #5a5a5a | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | clicked into the field |
| Painted layers | - | select.style-module-scss-module__neBVSa__billingSelect 103.0x17.0 outline 1px auto #101010 offset 0px |

Crops: `vec-billing-select-default.png`, `vec-billing-select-focused.png`.

#### vec-plan-card

Plan card. A price card on /pricing/vector — the plan name, monthly price and CTA inside a bordered card.

Page: vector. Selector: `plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 373.66 x 185.8 |
| Padding | 24px 32px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | #f7f8fa |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/21px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.style-module-scss-module__lUZDRW__statLabel: Inter 16px/24px 400, #5a5a5a |
| Transition | none |
| Painted layers | div.style-module-scss-module__lUZDRW__stat 373.7x185.8 bg #f7f8fa |
| How | at rest |

Crops: `vec-plan-card-default.png`.

#### vec-download-btn

Download sample button. A "Download sample" control on the Vector page; measured, never pressed — no download was requested.

Page: vector. Selector: `Download sample`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 179.91 x 43 | = | = | = |
| Padding | 12px 16px 12px 24px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #4559dc | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter 14px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #4559dc | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #4559dc | = | = | = |
| Painted layers | button.style-module-scss-module__cVn-Xq__download 179.9x43.0 border T:1px solid #4559dc / R:1px solid #4559dc / B:1px solid #4559dc / L:1px solid #4559dc | = | button.style-module-scss-module__cVn-Xq__download 179.9x43.0 border T:1px solid #4559dc / R:1px solid #4559dc / B:1px solid #4559dc / L:1px solid #4559dc outline 1px auto #101010 offset 0px | = |
| Ancestor paint | 1 up div.style-module-scss-module__cVn-Xq__card.style-module-scss-module__cVn-Xq__isRiskOn bg #f6f7fd | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `vec-download-btn-default.png`, `vec-download-btn-hover.png`, `vec-download-btn-focus-visible.png`, `vec-download-btn-pressed.png`.

#### vec-faq

FAQ accordion. A question row in the Vector FAQ ("How is the Bitcoin Vector delivered?", "Can I unsubscribe at any time?", ...); the opened state was measured after its own toggle — a local UI toggle.

Page: vector. Selector: `Vector FAQ row`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 822 x 82 | = |
| Padding | 24px 0px | = |
| Gap | 24px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 13.3333px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.style-module__vNz2sq__question: Inter 28px/normal 400, #333333 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #f7f8fa | = |
| Painted layers | span.style-module__vNz2sq__toggle 32.0x32.0 bg #1a1a1a r 100% | = |
| How | at rest | held open by an earlier toggle |

Crops: `vec-faq-default.png`, `vec-faq-opened.png`.

### Marketing contact page

#### contact-h1

Contact headline. "How can we connect" — the /contact masthead over the category cards.

Page: contact. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1064 x 67.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fraktion 56px/67.2px 700 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| How | at rest |

Crops: `contact-h1-default.png`.

#### contact-category

Contact category card. A contact-category card ("Contact Sales", "General Inquiries") that routes to the right form; measured, never followed.

Page: contact. Selector: `contact category card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 384 x 193.59 | = |
| Padding | 42px 24px | = |
| Border | 1px solid #dedfe1 | = |
| Radius | 2px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0.08 0px 8px 32px 0px, #000000 @ 0.04 0px 2px 4px 0px | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h3.directoryCard-module-scss-module__dc96PG__title: Inter 24px/33.6px 700, #333333 | = |
| Transition | border 0.2s ease-in-out | = |
| Cursor | pointer | = |
| Painted layers | a.directoryCard-module-scss-module__dc96PG__card 384.0x193.6 bg #ffffff border T:1px solid #dedfe1 / R:1px solid #dedfe1 / B:1px solid #dedfe1 / L:1px solid #dedfe1 r 2px shadow #000000 @ 0.08 0px 8px 32px 0px, #000000 @ 0.04 0px 2px 4px 0px | = |
| How | at rest | mouse hover |

Crops: `contact-category-default.png`, `contact-category-hover.png`.

#### contact-subscribe-btn

Subscribe button (contact). The "Send me free research" subscribe button in the contact page's research band; measured, never pressed.

Page: contact. Selector: `Send me free research`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 184.84 x 40 | = | - | = |
| Padding | 9.6px 16px | = | - | = |
| Border | 1px solid #dedfe1 | = | - | 1px solid #f7f8fa |
| Radius | 0px 2px 2px 0px | = | - | = |
| Background | #dedfe1 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 14px/18.2px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #808080 | = | - | = |
| Transition | all 0.2s cubic-bezier(0.645, 0.045, 0.355, 1) | = | - | = |
| Cursor | not-allowed | = | - | = |
| Painted layers | button.style-module-scss-module__NRs3BG__button.style-module-scss-module__NRs3BG__secondary 184.8x40.0 bg #dedfe1 border T:1px solid #dedfe1 / R:1px solid #dedfe1 / B:1px solid #dedfe1 / L:1px solid #dedfe1 r 0px 2px 2px 0px | = | - | button.style-module-scss-module__NRs3BG__button.style-module-scss-module__NRs3BG__secondary 184.8x40.0 bg #dedfe1 border T:1px solid #f7f8fa / R:1px solid #f7f8fa / B:1px solid #f7f8fa / L:1px solid #f7f8fa r 0px 2px 2px 0px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `contact-subscribe-btn-default.png`, `contact-subscribe-btn-hover.png`, `contact-subscribe-btn-pressed.png`.

### Research publication (Ghost)

#### res-header

Site header. The Ghost publication header: the Glassnode apps menu, the tag nav (Week On-chain, Strategy Watch, Market Pulse, Partner Reports, Product & Research), search and the theme toggle.

Page: research. Selector: `research header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 65 |
| Padding | 0px 36px |
| Border | T: none; R: none; B: 1px solid #e6e7e9; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/25.6px 400 |
| Letter spacing | normal |
| Colour | #5f636b |
| Text node | a: Inter 15px/20px 500, #5f636b |
| Transition | none |
| Icon | 16 x 16, colour #5f636b |
| ::before | 1425px x 64px, absolute, bg #ffffff @ 0.86, radius 0px |
| Painted layers | header.gh-head.outer 1425.0x65.0 border B:1px solid #e6e7e9; header::before.gh-head.outer 1425pxx64px bg #ffffff @ 0.86; div.gh-apps__menu 0.0x0.0 bg #ffffff border T:1px solid #e6e7e9 / R:1px solid #e6e7e9 / B:1px solid #e6e7e9 / L:1px solid #e6e7e9 shadow #000000 @ 0.1 0px 8px 24px -12px; button.navbar__mobile__toggle 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 |
| How | at rest |

Crops: `res-header-default.png`.

#### res-nav-link

Nav link. The "Week On-chain" tag link in the header nav; measured, never followed.

Page: research. Selector: `research nav Week On-chain`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 134.36 x 32 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 15px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #5f636b | #08090a | = | #08090a |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 134.4x32.0 outline 1px auto #101010 offset 1px | = |

Crops: `res-nav-link-default.png`, `res-nav-link-hover.png`, `res-nav-link-focus-visible.png`, `res-nav-link-pressed.png`.

#### res-theme-toggle

Theme toggle. The "Switch to dark mode" Ghost theme toggle — a local UI control that removes data-theme="light" and repaints the page; measured at rest, never switched here (the dark surface is captured in the screenshots pass).

Page: research. Selector: `.gh-theme-toggle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | - | = | = |
| Padding | 0px | - | = | = |
| Border | none | - | = | = |
| Radius | 0px | - | = | = |
| Background | transparent | - | = | #000000 @ 0.06 |
| Box shadow | none | - | = | = |
| Outline | none | - | 1px auto #101010 offset 0px | = |
| Font | Inter 16px/25.6px 400 | - | = | = |
| Letter spacing | normal | - | = | = |
| Colour | #5f636b | - | = | #08090a |
| Transition | color, background-color 0.12s, 0.12s ease, ease delay 0s, 0s | - | = | = |
| Cursor | pointer | - | = | = |
| Icon | 16 x 16, colour #5f636b | - | = | 16 x 16, colour #08090a |
| How | at rest | - | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Error | - | locator.hover: Timeout 5000ms exceeded. Call log:   - waiting for locator('button.gh-theme-toggle').first().first().first()     - locator resolved to <button type="button" class="gh-theme-toggle" aria | = | = |
| Painted layers | - | = | button.gh-theme-toggle 32.0x32.0 outline 1px auto #101010 offset 0px | button.gh-theme-toggle 32.0x32.0 bg #000000 @ 0.06 |

Crops: `res-theme-toggle-default.png`, `res-theme-toggle-focus-visible.png`, `res-theme-toggle-pressed.png`.

#### res-post-card

Article card. An article card in the research index (the current Week On-chain issue); measured, never followed.

Page: research. Selector: `research article card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1280 x 407.45 | = |
| Padding | 0px | = |
| Gap | 48px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/25.6px 400 | = |
| Letter spacing | normal | = |
| Colour | #08090a | = |
| Text node | span.post-card-primary-tag: Inter 14px/18.2px 400, #5f636b | = |
| Transition | none | = |
| Icon | 13 x 13, colour #8a8f98 | = |
| Painted layers | a.post-card-image-link 739.2x407.5 bg #f7f7f8 border T:1px solid #ececee / R:1px solid #ececee / B:1px solid #ececee / L:1px solid #ececee r 8px; span::before.post-card-meta-length 2pxx2px bg #8a8f98 r 50% | = |
| How | at rest | mouse hover |

Crops: none.

#### res-subscribe-field

Subscribe field. The "Email" subscribe input on the research site; focused and typed into then cleared — never subscribed.

Page: research. Selector: `research input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 334 x 40 | = | = |
| Padding | 8px 16px | = | = |
| Border | 1px solid #d2d4d8 | 1px solid #a9adb5 | 1px solid #a9adb5 |
| Radius | 0px | = | = |
| Background | #f4f4f5 | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 15px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #08090a | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #8a8f98, opacity 1 | = | = |
| Painted layers | input.newsletter-post-card__form__input 334.0x40.0 bg #f4f4f5 border T:1px solid #d2d4d8 / R:1px solid #d2d4d8 / B:1px solid #d2d4d8 / L:1px solid #d2d4d8 | input.newsletter-post-card__form__input 334.0x40.0 bg #f4f4f5 border T:1px solid #a9adb5 / R:1px solid #a9adb5 / B:1px solid #a9adb5 / L:1px solid #a9adb5 | input.newsletter-post-card__form__input 334.0x40.0 bg #f4f4f5 border T:1px solid #a9adb5 / R:1px solid #a9adb5 / B:1px solid #a9adb5 / L:1px solid #a9adb5 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `res-subscribe-field-default.png`, `res-subscribe-field-focused.png`, `res-subscribe-field-filled.png`.

#### res-footer

Footer. The research footer: the subscribe band, the sitemap columns and the legal links.

Page: research. Selector: `research footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 492.8 x 24 |
| Padding | 0px |
| Gap | 6px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 15px/24px 400 |
| Letter spacing | normal |
| Colour | #8a8f98 |
| Text node | time.post-card-meta-date: Inter 15px/24px 400, #8a8f98 |
| Transition | none |
| Painted layers | span::before.post-card-meta-length 2pxx2px bg #8a8f98 r 50% |
| How | at rest |

Crops: `res-footer-default.png`.

#### res-article-h1

Article headline. The published-article masthead on research.glassnode.com (the current Week On-chain issue); the article URL is recorded on the component.

Page: research-article. Selector: `article h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 840 x 65.72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 62px/65.72px 500 |
| Letter spacing | -1.86px |
| Colour | #08090a |
| Transition | none |
| How | at rest |

Crops: `res-article-h1-default.png`.

#### res-article-p

Article body text. A paragraph in the article body — the Ghost theme's serif/sans reading measure.

Page: research-article. Selector: `article p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 150 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/30px 400 |
| Letter spacing | normal |
| Colour | #5f636b |
| Transition | none |
| How | at rest |

Crops: `res-article-p-default.png`.

#### res-article-tag

Article tag. A tag link on the article; measured, never followed.

Page: research-article. Selector: `article tag link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 0 x 0 | - | - | = |
| Padding | 10px 12px | - | - | = |
| Border | none | - | - | = |
| Radius | 0px | - | - | = |
| Background | transparent | - | - | = |
| Box shadow | none | - | - | = |
| Outline | none | - | - | = |
| Font | Inter 16px/24px 500 | - | - | = |
| Letter spacing | normal | - | - | = |
| Colour | #08090a | - | - | = |
| Transition | none | - | - | = |
| Cursor | pointer | - | - | = |
| How | at rest | - | - | CDP forcePseudoState :active:hover |
| Error | - | locator.hover: Element is not visible Call log:   - waiting for locator('article a[href*="/tag/"], a[href*="/tag/"]').first().first().first()     - locator resolved to <a class="" href="https://resear | = | = |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: none.

### Docs site (GitBook)

#### docs-header

Docs header. The GitBook docs header: "Glassnode Docs", the search field, the Website/Studio/Insights/Twitter links, "More" and the light/system/dark theme buttons.

Page: docs. Selector: `docs header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff @ 0.88 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1d1d1d @ 0.08 0px 1px 0px 0px |
| Backdrop filter | blur(16px) |
| Outline | none |
| Font | Roboto 14px/20px 400 |
| Letter spacing | normal |
| Colour | #1d1d1d |
| Text node | div.text-pretty.line-clamp-2: Roboto 18px/22.5px 600, #ffffff, ls -0.45px |
| Transition | none |
| Icon | 0 x 0, colour #ffffff |
| Painted layers | header.flex.flex-col 1425.0x64.0 bg #ffffff @ 0.88 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1d1d1d @ 0.08 0px 1px 0px 0px; div.site-header:theme-bold:bg-header-background.site-header:theme-bold:shadow-[0px_1px_0px] 1425.0x64.0 bg #1d1d1d shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1d1d1d @ 0.08 0px 1px 0px 0px; button.button.group/button 0.0x0.0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; div.group/input.relative 224.0x39.0 bg #ffffff @ 0.04 border T:1px solid #ffffff @ 0.16 / R:1px solid #ffffff @ 0.16 / B:1px solid #ffffff @ 0.16 / L:1px solid #ffffff @ 0.16 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; button.button.group/button 0.0x0.0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; kbd.flex.h-5 38.8x20.0 bg #1d1d1d border T:1px solid #ffffff @ 0.16 / R:1px solid #ffffff @ 0.16 / B:1px solid #ffffff @ 0.16 / L:1px solid #ffffff @ 0.16 r 6px |
| Ancestor paint | 1 up body.site-background.sheet-open:overflow-hidden bg #ffffff |
| How | at rest |

Crops: `docs-header-default.png`.

#### docs-nav-link

Docs nav link. The "Studio" header link out to studio.glassnode.com; measured, never followed.

Page: docs. Selector: `docs header link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 39.91 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #cbd8fd offset 1px | = |
| Font | Roboto 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #ffffff @ 0.64 | = | #ffffff @ 0.64 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.flex.items-center 39.9x20.0 outline 2px solid #cbd8fd offset 1px | = |

Crops: `docs-nav-link-default.png`, `docs-nav-link-hover.png`, `docs-nav-link-focus-visible.png`, `docs-nav-link-pressed.png`.

#### docs-theme-btn

Theme button. The GitBook "Switch to dark theme" button — a local UI control that flips .light/.dark on <html>; measured at rest, never switched here (the dark surface is captured in the screenshots pass).

Page: docs. Selector: `docs Switch to dark theme`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 33 x 33 | = | = | = |
| Padding | 6px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | #f2f2f2 | #f2f2f2 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| Outline | none | = | 2px solid #cbd8fd offset 0px | = |
| Font | Roboto 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6e6e6e | = | #1d1d1d | #1d1d1d |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #6e6e6e | = | 14 x 14, colour #1d1d1d | 14 x 14, colour #1d1d1d |
| Painted layers | button.button.group/button 33.0x33.0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | button.button.group/button 33.0x33.0 bg #f2f2f2 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #cbd8fd offset 0px | button.button.group/button 33.0x33.0 bg #f2f2f2 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-theme-btn-default.png`, `docs-theme-btn-hover.png`, `docs-theme-btn-focus-visible.png`, `docs-theme-btn-pressed.png`.

#### docs-search

Search field. The docs "Search" field — focused only; typing was not needed to read the focus ring.

Page: docs. Selector: `docs Search`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 121.44 x 37 | - |
| Padding | 8px | - |
| Border | none | - |
| Radius | 0px | - |
| Background | transparent | - |
| Box shadow | none | - |
| Outline | none | - |
| Font | Roboto 14px/21px 400 | - |
| Letter spacing | normal | - |
| Colour | #ffffff | - |
| Transition | none | - |
| Cursor | text | - |
| Placeholder | #ffffff @ 0.72, opacity 1 | - |
| Ancestor paint | 2 up div.group/input.relative bg #ffffff @ 0.04 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | - |
| How | at rest | - |
| Error | - | locator.evaluate: Timeout 8000ms exceeded. Call log:   - waiting for locator('input[placeholder*="Search" i], button[aria-label*="Search" i]').first().first().first()  |

Crops: `docs-search-default.png`.

#### docs-h1

Doc page headline. "Overview" — the docs landing headline on the GitBook stack.

Page: docs. Selector: `docs h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 753 x 45 |
| Padding | 0px |
| Gap | 18px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roboto 36px/45px 700 |
| Letter spacing | -0.9px |
| Colour | #1d1d1d |
| Transition | none |
| How | at rest |

Crops: `docs-h1-default.png`.

#### docs-side-link

Sidebar link. A sidebar navigation link in the docs tree; measured, never followed.

Page: docs. Selector: `docs sidebar link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 282 x 32 | = |
| Padding | 6px 6px 6px 12px | = |
| Gap | 12px | = |
| Border | none | = |
| Radius | 6px | = |
| Background | transparent | #f2f2f2 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Roboto 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #1d1d1d @ 0.64 | #1d1d1d |
| Text node | span: Roboto 14px/20px 400, #1d1d1d @ 0.64 | span: Roboto 14px/20px 400, #1d1d1d |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| ::before | 0px x 32px, absolute, bg #000000 @ 0, radius 0px | = |
| How | at rest | mouse hover |
| Painted layers | - | a.group/toclink.toclink 282.0x32.0 bg #f2f2f2 r 6px |

Crops: `docs-side-link-default.png`, `docs-side-link-hover.png`.

#### docs-quote-btn

Request a quote link. The "Request a quote" banner link on the overview page; measured, never followed.

Page: docs. Selector: `docs Request a quote`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1361 x 44 | = | = | = |
| Padding | 12px 48px 12px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #f7f7f7 | #f5f5f5 | = | #ededed |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| Outline | none | = | 2px solid #cbd8fd offset 1px | = |
| Font | Roboto 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1d1d1d | = | = | = |
| Text node | div: Roboto 14px/20px 400, #1d1d1d | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #787878 | = | = | = |
| Painted layers | a.flex.w-full 1361.0x44.0 bg #f7f7f7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | a.flex.w-full 1361.0x44.0 bg #f5f5f5 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | a.flex.w-full 1361.0x44.0 bg #f7f7f7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #cbd8fd offset 1px | a.flex.w-full 1361.0x44.0 bg #ededed r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-quote-btn-default.png`, `docs-quote-btn-hover.png`, `docs-quote-btn-focus-visible.png`, `docs-quote-btn-pressed.png`.

#### docs-metric-h1

Metric catalog headline. "Metric Catalog" — the API metric index page on the docs site.

Page: docs-metric. Selector: `docs-metric h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 753 x 45 |
| Padding | 0px |
| Gap | 18px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roboto 36px/45px 700 |
| Letter spacing | -0.9px |
| Colour | #1d1d1d |
| Transition | none |
| How | at rest |

Crops: `docs-metric-h1-default.png`.

#### docs-metric-link

Metric category link. A metric-category link in the catalog; measured, never followed.

Page: docs-metric. Selector: `docs metric category link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 85.61 x 16 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Roboto 14px/21px 400 | = |
| Letter spacing | normal | = |
| Colour | #6888fb | #1a1d25 |
| Transition | all 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 12 x 12, colour #6888fb | 12 x 12, colour #1a1d25 |
| How | at rest | mouse hover |

Crops: `docs-metric-link-default.png`, `docs-metric-link-hover.png`.

#### docs-code

Code or metric label. A code/metric label on the catalog page — the GitBook monospace treatment.

Page: docs-metric. Selector: `docs pre/code`. States: .

Not found on the page at capture time.

### Mobile (390 wide)

#### m-topbar

Mobile top bar. The phone header at 390 wide: the wordmark and the hamburger.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 70 |
| Padding | 24px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/21px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Ancestor paint | 1 up div.style-module-scss-module__LPSrhq__container bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-menu-btn

Mobile menu button. The hamburger button — a local UI toggle; the opened state was measured after activating it.

Page: mobile. Selector: `mobile hamburger`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 28 x 22 | = | = | = | = |
| Padding | 1px 6px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = | = |
| Font | Inter 13.3333px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Ancestor paint | 2 up div.style-module-scss-module__LPSrhq__container bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px | = | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | button.style-module-scss-module__oFHV5W__hamburger 28.0x22.0 outline 1px auto #e59700 offset 0px | = | = |

Crops: `m-menu-btn-default.png`, `m-menu-btn-hover.png`, `m-menu-btn-focus-visible.png`, `m-menu-btn-pressed.png`, `m-menu-btn-opened.png`.

#### m-drawer

Mobile nav overlay. The navigation overlay opened by the hamburger (the same destinations as the desktop header); its links were never followed.

Page: mobile. Selector: `mobile nav overlay`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 290 x 844 |
| Padding | 0px 32px |
| Border | none |
| Radius | 0px |
| Background | #1a1a1a |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/21px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Inter 13.3333px/normal 400, #dedfe1 |
| Transition | none |
| Icon | 16 x 16, colour #dedfe1, fill #000000 |
| Painted layers | nav.style-module-scss-module__WhQwwG__nav 290.0x844.0 bg #1a1a1a; a.style-module-scss-module__NRs3BG__button.style-module-scss-module__NRs3BG__secondary 120.8x33.0 bg #ffffff border T:1px solid #bfbfbf / R:1px solid #bfbfbf / B:1px solid #bfbfbf / L:1px solid #bfbfbf r 2px |
| Ancestor paint | 2 up div.style-module-scss-module__LPSrhq__container bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `m-drawer-default.png`.

#### m-hero-h1

Mobile hero headline. The masthead at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fraktion 40px/48px 700 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-newsletter-field

Mobile newsletter field. The "Enter your email" subscribe input at 390 wide; focused and typed into then cleared — never subscribed.

Page: mobile. Selector: `mobile input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 342 x 40 | = | = |
| Padding | 0px 16px | = | = |
| Border | 1px solid #808080 | = | = |
| Radius | 2px 0px 0px 2px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | 1px auto #e59700 offset 0px | 1px auto #e59700 offset 0px |
| Font | Inter 14px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #a0a0a0 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| Painted layers | input 342.0x40.0 border T:1px solid #808080 / R:1px solid #808080 / B:1px solid #808080 / L:1px solid #808080 r 2px 0px 0px 2px | input 342.0x40.0 border T:1px solid #808080 / R:1px solid #808080 / B:1px solid #808080 / L:1px solid #808080 r 2px 0px 0px 2px outline 1px auto #e59700 offset 0px | input 342.0x40.0 border T:1px solid #808080 / R:1px solid #808080 / B:1px solid #808080 / L:1px solid #808080 r 2px 0px 0px 2px outline 1px auto #e59700 offset 0px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `m-newsletter-field-default.png`, `m-newsletter-field-focused.png`, `m-newsletter-field-filled.png`.

### Studio shell (signed out)

#### st-navbar

Studio navbar. The product-shell top bar on studio.glassnode.com: the wordmark, Home/Dashboards/Charts/Market Compass/Alpha Lab/Research/Tokenization nav, Resources, the search control, "Log in" and "Sign up".

Page: studio-pricing. Selector: `.navbar_container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 70 |
| Padding | 0px |
| Gap | normal 16px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #dedfe1 0px -1px 0px 0px inset |
| Outline | none |
| Font | Inter Variable 14px/22.001px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.88 |
| Text node | a.navigation_link-hlUTI: Inter Variable 14px/22.001px 400, #6f6f6f |
| Transition | none |
| Icon | 0 x 0, colour #333333 |
| Painted layers | div.navbar_container-Cjq1s 1425.0x70.0 bg #ffffff shadow #dedfe1 0px -1px 0px 0px inset; input.ant-input.ant-input-outlined 0.0x0.0 bg #f7f8fa r 2px; div.globalSearch_accessKey-3ede- 0.0x0.0 bg #edeff2 border T:1px solid #dedfe1 / R:1px solid #dedfe1 / B:1px solid #dedfe1 / L:1px solid #dedfe1 r 3px; button.ant-btn.ant 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px; sup.ant-scroll-number.ant-badge-dot 6.0x6.0 bg #4559dc r 100% shadow #ffffff 0px 0px 0px 1px; button.ant-btn.ant 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px |
| How | at rest |

Crops: `st-navbar-default.png`.

#### st-nav-link

Studio nav link. The "Charts" navbar link to /charts?a=BTC; measured, never followed.

Page: studio-pricing. Selector: `studio nav Charts`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 43.7 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter Variable 14px/22.001px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6f6f6f | #333333 | = | #333333 |
| Transition | color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `st-nav-link-default.png`, `st-nav-link-hover.png`, `st-nav-link-focus-visible.png`, `st-nav-link-pressed.png`.

#### st-login-btn

Log in button. The navbar "Log in" — navigates to the Auth0 universal login at auth.glassnode.com; measured, never pressed (the login form is captured on the auth-login pass).

Page: studio-pricing. Selector: `studio Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50.5 x 32 | = | = | = |
| Padding | 0px 4px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 2px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #404040 offset 1px | = |
| Font | Inter Variable 14px/22.001px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1a1a1a | #000000 | = | = |
| Text node | span: Inter Variable 14px/22.001px 400, #1a1a1a | span: Inter Variable 14px/22.001px 400, #000000 | = | = |
| Transition | all 0.2s cubic-bezier(0.645, 0.045, 0.355, 1) | = | outline-offset, outline 0s, 0s ease, ease delay 0s, 0s | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.ant-btn.ant 50.5x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px | = | button.ant-btn.ant 50.5x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px outline 3px solid #404040 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `st-login-btn-default.png`, `st-login-btn-hover.png`, `st-login-btn-focus-visible.png`, `st-login-btn-pressed.png`.

#### st-signup-btn

Sign up button. The navbar "Sign up" — navigates to the Auth0 signup; measured, never pressed.

Page: studio-pricing. Selector: `studio Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 82.03 x 32 | = | = | = |
| Padding | 0px 15px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 2px | = | = | = |
| Background | #1a1a1a | #262626 | = | #000000 |
| Box shadow | #191919 @ 0.1 0px 2px 0px 0px | = | = | = |
| Outline | none | = | 3px solid #404040 offset 1px | = |
| Font | Inter Variable 14px/22.001px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Inter Variable 14px/22.001px 400, #ffffff | = | = | = |
| Transition | all 0.2s cubic-bezier(0.645, 0.045, 0.355, 1) | = | outline-offset, outline 0s, 0s ease, ease delay 0s, 0s | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.ant-btn.ant 82.0x32.0 bg #1a1a1a border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px shadow #191919 @ 0.1 0px 2px 0px 0px | button.ant-btn.ant 82.0x32.0 bg #262626 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px shadow #191919 @ 0.1 0px 2px 0px 0px | button.ant-btn.ant 82.0x32.0 bg #1a1a1a border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px shadow #191919 @ 0.1 0px 2px 0px 0px outline 3px solid #404040 offset 1px | button.ant-btn.ant 82.0x32.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px shadow #191919 @ 0.1 0px 2px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `st-signup-btn-default.png`, `st-signup-btn-hover.png`, `st-signup-btn-focus-visible.png`, `st-signup-btn-pressed.png`.

#### st-search-btn

Search trigger. The navbar search button that opens the metric/asset search; a local UI toggle — measured, never opened.

Page: studio-pricing. Selector: `studio search button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 2px | = | = | = |
| Background | transparent | #000000 @ 0.04 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #404040 offset 1px | = |
| Font | Inter Variable 14px/22.001px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.88 | = | = | = |
| Transition | all 0.2s cubic-bezier(0.645, 0.045, 0.355, 1) | = | outline-offset, outline 0s, 0s ease, ease delay 0s, 0s | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 @ 0.88 | = | = | = |
| Painted layers | button.ant-btn.ant 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px | button.ant-btn.ant 32.0x32.0 bg #000000 @ 0.04 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px | button.ant-btn.ant 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px outline 3px solid #404040 offset 1px | = |
| Ancestor paint | 2 up div.navbar_container-Cjq1s bg #ffffff shadow #dedfe1 0px -1px 0px 0px inset | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `st-search-btn-default.png`, `st-search-btn-hover.png`, `st-search-btn-focus-visible.png`, `st-search-btn-pressed.png`.

#### st-h1

Pricing headline. "Plans & Pricing" — the studio /pricing masthead.

Page: studio-pricing. Selector: `studio h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1377 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 40px/48px 700 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| How | at rest |

Crops: `st-h1-default.png`.

#### st-plan-card

Plan card. A plan card on studio /pricing — one column of the plan grid (ADVANCED/PROFESSIONAL/...): name, price, billing copy and CTA.

Page: studio-pricing. Selector: `studio plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 399.5 x 337.41 |
| Padding | 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 14px/22.001px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.88 |
| Text node | div.pricingCardsSection_planLabel-QsxJ7: Inter Variable 12px/18.858px 500, #5a5a5a, ls 0.6px |
| Transition | none |
| Icon | 12 x 12, colour #5a5a5a |
| Painted layers | div.ant-select.ant-select-sm 100.0x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px; button.ant-btn.ant 335.5x40.0 bg #ffffff border T:1px solid #d9d9d9 / R:1px solid #d9d9d9 / B:1px solid #d9d9d9 / L:1px solid #d9d9d9 r 2px shadow #000000 @ 0.02 0px 2px 0px 0px |
| How | at rest |

Crops: `st-plan-card-default.png`.

#### st-plan-signup-btn

Plan CTA. A "Sign up" call-to-action inside a plan card; measured, never pressed.

Page: studio-pricing. Selector: `plan card Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 396.59 x 40 | = | = | = |
| Padding | 0px 15px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #d9d9d9 | 1px solid #262626 | = | 1px solid #000000 |
| Radius | 2px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0.02 0px 2px 0px 0px | = | = | = |
| Outline | none | = | 3px solid #404040 offset 1px | = |
| Font | Inter Variable 14px/22.001px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.88 | #262626 | = | #000000 |
| Text node | span: Inter Variable 14px/22.001px 400, #000000 @ 0.88 | span: Inter Variable 14px/22.001px 400, #262626 | = | span: Inter Variable 14px/22.001px 400, #000000 |
| Transition | all 0.2s cubic-bezier(0.645, 0.045, 0.355, 1) | = | outline-offset, outline 0s, 0s ease, ease delay 0s, 0s | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.ant-btn.ant 396.6x40.0 bg #ffffff border T:1px solid #d9d9d9 / R:1px solid #d9d9d9 / B:1px solid #d9d9d9 / L:1px solid #d9d9d9 r 2px shadow #000000 @ 0.02 0px 2px 0px 0px | button.ant-btn.ant 396.6x40.0 bg #ffffff border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 2px shadow #000000 @ 0.02 0px 2px 0px 0px | button.ant-btn.ant 396.6x40.0 bg #ffffff border T:1px solid #d9d9d9 / R:1px solid #d9d9d9 / B:1px solid #d9d9d9 / L:1px solid #d9d9d9 r 2px shadow #000000 @ 0.02 0px 2px 0px 0px outline 3px solid #404040 offset 1px | button.ant-btn.ant 396.6x40.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px shadow #000000 @ 0.02 0px 2px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `st-plan-signup-btn-default.png`, `st-plan-signup-btn-hover.png`, `st-plan-signup-btn-focus-visible.png`, `st-plan-signup-btn-pressed.png`.

#### st-configure-btn

Configure button. The "Configure" control on the custom/enterprise plan card; measured, never pressed.

Page: studio-pricing. Selector: `plan card Configure`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 335.5 x 40 | = | = | = |
| Padding | 0px 15px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #333333 | = | = | = |
| Radius | 2px | = | = | = |
| Background | #333333 | = | = | = |
| Box shadow | #191919 @ 0.1 0px 2px 0px 0px | = | = | = |
| Outline | none | = | 3px solid #404040 offset 1px | = |
| Font | Inter Variable 14px/22.001px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Inter Variable 14px/22.001px 400, #ffffff | = | = | = |
| Transition | all 0.2s cubic-bezier(0.645, 0.045, 0.355, 1) | = | outline-offset, outline 0s, 0s ease, ease delay 0s, 0s | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.ant-btn.ant 335.5x40.0 bg #333333 border T:1px solid #333333 / R:1px solid #333333 / B:1px solid #333333 / L:1px solid #333333 r 2px shadow #191919 @ 0.1 0px 2px 0px 0px | = | button.ant-btn.ant 335.5x40.0 bg #333333 border T:1px solid #333333 / R:1px solid #333333 / B:1px solid #333333 / L:1px solid #333333 r 2px shadow #191919 @ 0.1 0px 2px 0px 0px outline 3px solid #404040 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `st-configure-btn-default.png`, `st-configure-btn-hover.png`, `st-configure-btn-focus-visible.png`, `st-configure-btn-pressed.png`.

#### st-metrics-expander

Metric catalog expander. A "Show N more metrics" expander in the public metric catalog on /pricing; the opened state was measured after its own toggle — a local UI toggle that reveals more catalog rows.

Page: studio-pricing. Selector: `Show N more metrics`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 1160 x 42.84 | = |
| Padding | 12px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 12px/18.858px 400 | = |
| Letter spacing | normal | = |
| Colour | #4559dc | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | button.metricCatalog_showMoreBtn-MDd-m 1160.0x42.8 bg #ffffff | = |
| How | at rest | own toggle |

Crops: `st-metrics-expander-default.png`, `st-metrics-expander-opened.png`.

#### st-faq

FAQ accordion. A question row in the studio pricing FAQ ("How many assets does Glassnode...", "Is API access included...", ...); the opened state was measured after its own toggle — a local UI toggle.

Page: studio-pricing. Selector: `studio pricing FAQ`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 510 x 54.39 | = |
| Padding | 16px 0px | = |
| Gap | 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 14px/22.001px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 @ 0.88 | = |
| Text node | span.faqSection_question-szsuB: Inter Variable 16px/22.4px 500, #333333 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 20 x 20, colour #4559dc | 28.28 x 28.28, colour #4559dc |
| How | at rest | own toggle |

Crops: `st-faq-default.png`, `st-faq-opened.png`.

### Auth0 universal login

#### __auth

Auth0 origin reached — page marker, no component states.

#### auth-card

Login card. The Auth0 universal-login card on auth.glassnode.com/u/login — the username/password form, "Continue", "Continue with Google", "Reset password" and "Sign up". Reached through the studio shell's real "Log in" button; the volatile ?state= parameter is never recorded.

Page: auth-login. Selector: `auth0 login form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 320 x 210 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ulp-font 14px/14px 400 |
| Letter spacing | normal |
| Colour | #1e212a |
| Text node | label.cea96adc7.cd251e14b: ulp-font 16px/16px 400, #65676e |
| Transition | none |
| Painted layers | div.c50d1bce1.c0d0ae1c1 320.0x52.0 bg #ffffff; label.cea96adc7.cd251e14b 121.1x18.0 bg #ffffff; input.input.cac2a821f 320.0x52.0 bg #ffffff border T:1px solid #c9cace / R:1px solid #c9cace / B:1px solid #c9cace / L:1px solid #c9cace; div.c50d1bce1.c0d0ae1c1 320.0x54.0 bg #ffffff border T:1px solid #c9cace / R:1px solid #c9cace / B:1px solid #c9cace / L:1px solid #c9cace; label.cea96adc7.cd251e14b 89.9x18.0 bg #ffffff; input.input.cac2a821f 274.0x52.0 bg #ffffff |
| How | at rest |

Crops: `auth-card-default.png`.

#### auth-email

Username field. The e-mail/username input on the Auth0 card; focused and typed into then cleared — never submitted.

Page: auth-login. Selector: `input[name=username]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 320 x 52 | = | = |
| Padding | 0px 16px | = | = |
| Border | 1px solid #c9cace | 1px solid #635dff | 1px solid #635dff |
| Radius | 0px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #635dff 0px 0px 0px 1px | #635dff 0px 0px 0px 1px |
| Outline | none | = | = |
| Font | ulp-font 16px/17.6px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | box-shadow, border-color 0.15s, 0.15s ease-in-out, ease-in-out delay 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | #000000, opacity 1 | = | = |
| Painted layers | input.input.cac2a821f 320.0x52.0 bg #ffffff border T:1px solid #c9cace / R:1px solid #c9cace / B:1px solid #c9cace / L:1px solid #c9cace | input.input.cac2a821f 320.0x52.0 bg #ffffff border T:1px solid #635dff / R:1px solid #635dff / B:1px solid #635dff / L:1px solid #635dff shadow #635dff 0px 0px 0px 1px | input.input.cac2a821f 320.0x52.0 bg #ffffff border T:1px solid #635dff / R:1px solid #635dff / B:1px solid #635dff / L:1px solid #635dff shadow #635dff 0px 0px 0px 1px |
| Ancestor paint | 1 up div.c50d1bce1.c0d0ae1c1 bg #ffffff | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `auth-email-default.png`, `auth-email-focused.png`, `auth-email-filled.png`.

#### auth-password

Password field. The password input on the Auth0 card; focused only — nothing was typed or submitted.

Page: auth-login. Selector: `input[name=password]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 274 x 52 | = |
| Padding | 0px 16px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ulp-font 16px/17.6px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | box-shadow, border-color 0.15s, 0.15s ease-in-out, ease-in-out delay 0s, 0s | = |
| Cursor | text | = |
| Placeholder | #000000, opacity 1 | = |
| Painted layers | input.input.cac2a821f 274.0x52.0 bg #ffffff | = |
| Ancestor paint | 1 up div.c50d1bce1.c0d0ae1c1 bg #ffffff | 1 up div.c50d1bce1.c0d0ae1c1 bg #ffffff shadow #635dff 0px 0px 0px 1px |
| How | at rest | clicked into the field |

Crops: `auth-password-default.png`, `auth-password-focused.png`.

#### auth-continue

Continue button. The login form's "Continue" submit; its states were measured but the button was never clicked — no credentials were entered and nothing was submitted.

Page: auth-login. Selector: `auth0 Continue`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 320 x 52 | = | = | = |
| Padding | 4px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 2px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | none | #000000 @ 0.1 0px 0px 0px 150px inset | = | #c9cfda 0px 0px 2px 0px |
| Outline | none | = | 2px solid #635dff offset 2px | = |
| Font | ulp-font 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, box-shadow 0.25s, 0.25s ease-in-out, ease-in-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.c5900ab5b.c564047a1 320.0x52.0 bg #000000 r 2px | button.c5900ab5b.c564047a1 320.0x52.0 bg #000000 r 2px shadow #000000 @ 0.1 0px 0px 0px 150px inset | button.c5900ab5b.c564047a1 320.0x52.0 bg #000000 r 2px outline 2px solid #635dff offset 2px | button.c5900ab5b.c564047a1 320.0x52.0 bg #000000 r 2px shadow #c9cfda 0px 0px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `auth-continue-default.png`, `auth-continue-hover.png`, `auth-continue-focus-visible.png`, `auth-continue-pressed.png`.

#### auth-google

Google SSO button. The "Continue with Google" social-login submit; measured, never pressed.

Page: auth-login. Selector: `auth0 Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 320 x 52 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 16px | = | = | = |
| Border | 1px solid #c9cace | = | = | = |
| Radius | 2px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | #000000 @ 0.1 0px 0px 0px 150px inset | = | #635dff @ 0.15 0px 0px 0px 150px inset |
| Outline | none | = | 2px solid #635dff offset 2px | = |
| Font | ulp-font 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e212a | = | = | = |
| Text node | span.ce6a568ad: ulp-font 16px/16px 400, #1e212a | = | = | = |
| Transition | box-shadow, background-color 0.15s, 0.15s ease-in-out, ease-in-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.c837464f7.cd9aef2d7 320.0x52.0 bg #ffffff border T:1px solid #c9cace / R:1px solid #c9cace / B:1px solid #c9cace / L:1px solid #c9cace r 2px; span.c0d94c7af.cbc6eca94 20.0x20.0 image url(data:…)' fill='%23FBBC05' d='M0 37V11l17 13z'/%3E%3Cpath clip-path='url(…)' fill='%23E | button.c837464f7.cd9aef2d7 320.0x52.0 bg #ffffff border T:1px solid #c9cace / R:1px solid #c9cace / B:1px solid #c9cace / L:1px solid #c9cace r 2px shadow #000000 @ 0.1 0px 0px 0px 150px inset; span.c0d94c7af.cbc6eca94 20.0x20.0 image url(data:…)' fill='%23FBBC05' d='M0 37V11l17 13z'/%3E%3Cpath clip-path='url(…)' fill='%23E | button.c837464f7.cd9aef2d7 320.0x52.0 bg #ffffff border T:1px solid #c9cace / R:1px solid #c9cace / B:1px solid #c9cace / L:1px solid #c9cace r 2px outline 2px solid #635dff offset 2px; span.c0d94c7af.cbc6eca94 20.0x20.0 image url(data:…)' fill='%23FBBC05' d='M0 37V11l17 13z'/%3E%3Cpath clip-path='url(…)' fill='%23E | button.c837464f7.cd9aef2d7 320.0x52.0 bg #ffffff border T:1px solid #c9cace / R:1px solid #c9cace / B:1px solid #c9cace / L:1px solid #c9cace r 2px shadow #635dff @ 0.15 0px 0px 0px 150px inset; span.c0d94c7af.cbc6eca94 20.0x20.0 image url(data:…)' fill='%23FBBC05' d='M0 37V11l17 13z'/%3E%3Cpath clip-path='url(…)' fill='%23E |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `auth-google-default.png`, `auth-google-hover.png`, `auth-google-focus-visible.png`, `auth-google-pressed.png`.

#### auth-reset

Reset password link. The "Reset password" link to the Auth0 password-reset start; measured, never followed.

Page: auth-login. Selector: `auth0 Reset password`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 115.38 x 24 | = | = | = |
| Padding | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 3px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #635dff offset -1px | = |
| Font | ulp-font 14px/21px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #635dff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.c6017cfca.cdfbf1f1b 115.4x24.0 r 3px outline 2px solid #635dff offset -1px | = |

Crops: `auth-reset-default.png`, `auth-reset-hover.png`, `auth-reset-focus-visible.png`, `auth-reset-pressed.png`.

#### auth-signup-link

Sign up link. The "Sign up" link beside the login form; measured, never followed.

Page: auth-login. Selector: `auth0 Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 59.33 x 24 | = | = | = |
| Padding | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 3px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #635dff offset -1px | = |
| Font | ulp-font 14px/21px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #635dff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.c6017cfca.cd3cfae4f 59.3x24.0 r 3px outline 2px solid #635dff offset -1px | = |

Crops: `auth-signup-link-default.png`, `auth-signup-link-hover.png`, `auth-signup-link-focus-visible.png`, `auth-signup-link-pressed.png`.

### Tokenization registry

#### tok-shell

Registry nav. The registry navigation on tokenization.glassnode.com: the Glassnode apps menu, search, the theme button and the Overview/Assets/Issuers/Products/Derivatives items with their live counts.

Page: tokenization. Selector: `tokenization nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 220 x 852 |
| Padding | 12px 8px 0px 8px |
| Border | T: none; R: 1px solid #2a2a2a; B: none; L: none |
| Radius | 0px |
| Background | #141414 |
| Box shadow | none |
| Outline | none |
| Font | inter 13px/18.85px 400 |
| Letter spacing | normal |
| Colour | #e8e8e6 |
| Text node | div.rail-heading.block: inter 11.5px/16.675px 500, #8a8a87 |
| Transition | width 0.15s ease |
| Icon | 16 x 16, colour #16cc8c |
| Painted layers | nav.rail.hidden 220.0x852.0 bg #141414 border R:1px solid #2a2a2a; a.rail-item.relative 203.0x30.0 bg #2b2b2b r 6px; div.rail-foot.mt-auto 203.0x85.0 border T:1px solid #2a2a2a |
| How | at rest |

Crops: `tok-shell-default.png`.

#### tok-nav-item

Nav item. The "Assets" nav item with its live asset count (3,727 at capture); measured, never followed.

Page: tokenization. Selector: `tokenization nav Assets`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 203 x 30 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | #232323 | = | #232323 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #16cc8c offset 2px | = |
| Font | inter 13px/18.85px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #b8b8b5 | #e8e8e6 | = | #e8e8e6 |
| Text node | span.rail-label.min-w-0: inter 13px/18.85px 500, #b8b8b5 | span.rail-label.min-w-0: inter 13px/18.85px 500, #e8e8e6 | = | span.rail-label.min-w-0: inter 13px/18.85px 500, #e8e8e6 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #8a8a87 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.rail-item.relative 203.0x30.0 bg #232323 r 6px | a.rail-item.relative 203.0x30.0 r 6px outline 2px solid #16cc8c offset 2px | a.rail-item.relative 203.0x30.0 bg #232323 r 6px |

Crops: `tok-nav-item-default.png`, `tok-nav-item-hover.png`, `tok-nav-item-focus-visible.png`, `tok-nav-item-pressed.png`.

#### tok-search-btn

Search control. The "Search assets, issuers, products..." search control; a local UI toggle — measured, never opened.

Page: tokenization. Selector: `tokenization Search`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 560 x 32 | = | = | = |
| Padding | 0px 6px 0px 10px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #2a2a2a | 1px solid #363636 | = | 1px solid #363636 |
| Radius | 6px | = | = | = |
| Background | #262626 | #1c1c1c | = | #1c1c1c |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #16cc8c offset 2px | = |
| Font | inter 13px/18.85px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #8a8a87 | = | = | = |
| Text node | span.flex-1.truncate: inter 13px/18.85px 400, #8a8a87 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 15 x 15, colour #8a8a87 | = | = | = |
| Painted layers | button.hidden.h-8 560.0x32.0 bg #262626 border T:1px solid #2a2a2a / R:1px solid #2a2a2a / B:1px solid #2a2a2a / L:1px solid #2a2a2a r 6px; kbd.h-5 30.6x20.0 bg #262626 border T:1px solid #363636 / R:1px solid #363636 / B:2px solid #363636 / L:1px solid #363636 r 4px | button.hidden.h-8 560.0x32.0 bg #1c1c1c border T:1px solid #363636 / R:1px solid #363636 / B:1px solid #363636 / L:1px solid #363636 r 6px; kbd.h-5 30.6x20.0 bg #262626 border T:1px solid #363636 / R:1px solid #363636 / B:2px solid #363636 / L:1px solid #363636 r 4px | button.hidden.h-8 560.0x32.0 bg #262626 border T:1px solid #2a2a2a / R:1px solid #2a2a2a / B:1px solid #2a2a2a / L:1px solid #2a2a2a r 6px outline 2px solid #16cc8c offset 2px; kbd.h-5 30.6x20.0 bg #262626 border T:1px solid #363636 / R:1px solid #363636 / B:2px solid #363636 / L:1px solid #363636 r 4px | button.hidden.h-8 560.0x32.0 bg #1c1c1c border T:1px solid #363636 / R:1px solid #363636 / B:1px solid #363636 / L:1px solid #363636 r 6px; kbd.h-5 30.6x20.0 bg #262626 border T:1px solid #363636 / R:1px solid #363636 / B:2px solid #363636 / L:1px solid #363636 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tok-search-btn-default.png`, `tok-search-btn-hover.png`, `tok-search-btn-focus-visible.png`, `tok-search-btn-pressed.png`.

#### tok-theme-btn

Theme button. The "Switch to light theme" control — flips [data-theme] on <html>; measured at rest on the painted dark surface, never switched here (the light surface is captured in the screenshots pass).

Page: tokenization. Selector: `tokenization Switch to light theme`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 28 x 28 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | #232323 | = | #232323 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #16cc8c offset 2px | = |
| Font | inter 13px/18.85px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #8a8a87 | #e8e8e6 | = | #e8e8e6 |
| Transition | background, color 0.12s, 0.12s ease, ease delay 0s, 0s | = | = | = |
| Cursor | default | = | = | = |
| Icon | 15 x 15, colour #8a8a87 | 15 x 15, colour #e8e8e6 | = | 15 x 15, colour #e8e8e6 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.ib 28.0x28.0 bg #232323 r 6px | button.ib 28.0x28.0 r 6px outline 2px solid #16cc8c offset 2px | button.ib 28.0x28.0 bg #232323 r 6px |

Crops: `tok-theme-btn-default.png`, `tok-theme-btn-hover.png`, `tok-theme-btn-focus-visible.png`, `tok-theme-btn-pressed.png`.

#### tok-request-btn

Request access link. The "Request access" nav action to /api-access; measured, never followed.

Page: tokenization. Selector: `tokenization Request access`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 203 x 30 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | #232323 | = | #232323 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #16cc8c offset 2px | = |
| Font | inter 13px/18.85px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #b8b8b5 | #e8e8e6 | = | #e8e8e6 |
| Text node | span.rail-label.min-w-0: inter 13px/18.85px 500, #b8b8b5 | span.rail-label.min-w-0: inter 13px/18.85px 500, #e8e8e6 | = | span.rail-label.min-w-0: inter 13px/18.85px 500, #e8e8e6 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #8a8a87 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.rail-item.relative 203.0x30.0 bg #232323 r 6px | a.rail-item.relative 203.0x30.0 r 6px outline 2px solid #16cc8c offset 2px | a.rail-item.relative 203.0x30.0 bg #232323 r 6px |

Crops: `tok-request-btn-default.png`, `tok-request-btn-hover.png`, `tok-request-btn-focus-visible.png`, `tok-request-btn-pressed.png`.

#### tok-stat

Registry stat. A live registry count (assets/issuers/products/derivatives) in the nav or hero — the dark theme's numeric treatment.

Page: tokenization. Selector: `registry stat`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 203 x 30 |
| Padding | 0px 10px |
| Gap | 10px |
| Border | none |
| Radius | 6px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | inter 13px/18.85px 500 |
| Letter spacing | normal |
| Colour | #b8b8b5 |
| Text node | span.rail-label.min-w-0: inter 13px/18.85px 500, #b8b8b5 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 16 x 16, colour #8a8a87 |
| How | at rest |

Crops: `tok-stat-default.png`.

## Transitions declared in the readable stylesheets

glassnode.com serves its CSS as Next.js chunks plus SCSS-module blocks; studio.glassnode.com ships a large Ant Design + --gds-* layer; the Ghost, GitBook and registry surfaces ship their own sheets. This list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- auth-login: none

- contact: `0.2s cubic-bezier(0.645, 0.045, 0.355, 1)`, `box-shadow 0.2s`, `opacity 0.6s, transform 0.6s`, `background-color 0.2s ease-in-out`, `color 0.2s ease-in-out`, `background-color 0.15s`, `background-color 0.15s, border-color 0.15s, color 0.15s`, `background-color 0.15s, color 0.15s`, `color 0.15s, background-color 0.15s`, `0.2s`, `opacity 0.4s`, `opacity 0.4s, filter 0.4s, transform 0.5s`

- docs: none

- docs-metric: none

- home: `0.2s cubic-bezier(0.645, 0.045, 0.355, 1)`, `box-shadow 0.2s`, `opacity 0.6s, transform 0.6s`, `background-color 0.2s ease-in-out`, `color 0.2s ease-in-out`, `background-color 0.15s`, `background-color 0.15s, border-color 0.15s, color 0.15s`, `background-color 0.15s, color 0.15s`, `color 0.15s, background-color 0.15s`, `0.2s`, `opacity 0.4s`, `opacity 0.4s, filter 0.4s, transform 0.5s`

- research: `transform 0.3s cubic-bezier(0.2, 0.6, 0.3, 1), width 0.3s cubic-bezier(0.2, 0.6, 0.3, 1)`, `transform 0.25s cubic-bezier(0.2, 0.7, 0.3, 1), width 0.25s cubic-bezier(0.2, 0.7, 0.3, 1)`, `transform 0.2s cubic-bezier(0.2, 0.7, 0.3, 1), width 0.2s cubic-bezier(0.2, 0.7, 0.3, 1)`, `border-color 0.2s`, `0.2s ease-in-out`, `transform 0.2s ease-in-out`, `height 0.2s, content-visibility 0.2s allow-discrete`, `opacity 333ms cubic-bezier(0.4, 0, 0.22, 1)`, `transform 333ms cubic-bezier(0.4, 0, 0.22, 1)`, `none`, `opacity 0.2s`, `opacity 0.25s ease-out`

- studio-pricing: `background-color var(--ant-motion-duration-mid)`, `all var(--ant-motion-duration-mid) var(--ant-motion-ease-out-back)`, `all var(--ant-motion-duration-slow) var(--ant-motion-ease-out-back)`, `height 0.2s`, `left 0.2s, top 0.2s, width 0.2s, height 0.2s`, `none`, `0.2s`, `unset`, `background-color 0.1s ease-in-out`, `transform 0.15s`, `background-color 0.15s, color 0.15s`, `transform 0.2s`

- tokenization: `border-color 0.12s, box-shadow 0.12s`, `background 0.12s, border-color 0.12s, color 0.12s`, `background 0.12s, color 0.12s`, `width 0.15s`

- vector: `0.2s cubic-bezier(0.645, 0.045, 0.355, 1)`, `box-shadow 0.2s`, `opacity 0.6s, transform 0.6s`, `background-color 0.2s ease-in-out`, `color 0.2s ease-in-out`, `background-color 0.15s`, `background-color 0.15s, border-color 0.15s, color 0.15s`, `background-color 0.15s, color 0.15s`, `color 0.15s, background-color 0.15s`, `0.2s`, `opacity 0.4s`, `opacity 0.4s, filter 0.4s, transform 0.5s`

## Reduced motion

- home (`header a[href*="studio.glassnode.com"]` under prefers-reduced-motion): element not found
