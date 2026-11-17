# Component measurements

Computed styles read from joinhandshake.com's public pages (the App access group from app.joinhandshake.com/access) on 2026-11-17 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is the search field clicked into (nothing typed); `opened` and the rest are resting states reached by a component's own UI toggle. Nothing was typed, sent or signed into.

## Components

### Site chrome

#### hs-nav

Fixed nav bar. The pill-shaped bar fixed under --desktop-nav-top-offset over every marketing page: wordmark, section items, "Sign up" and "Log in".

Page: /. Selector: `nav.fixed`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.rounded-lg.px-4: NoiGrotesk 14px/19.6px 400, #ffffff, ls -0.21px |
| Transition | top, color 0.3s, 0.2s ease-in-out, ease delay 0s, 0s |
| Icon | 0 x 0, colour #d3fb52 |
| Painted layers | div.flex.items-center 1392.0x56.0 bg #ffffff @ 0 r 16px; a.flex.flex-col 73.8x40.0 bg #000000 @ 0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; a.flex.flex-col 80.5x40.0 bg #d3fb52 r 8px |
| How | resting state |

Crops: none.

#### hs-nav-link

Nav section item. A top-level nav item ("Employers") — opens the mega menu on hover.

Page: /. Selector: `nav a (text Employers)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 95.13 x 43.59 | = | = |
| Padding | 12px 16px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | #ffffff @ 0.1 | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | NoiGrotesk 14px/19.6px 400 | = | = |
| Letter spacing | -0.21px | = | = |
| Colour | #ffffff | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.4s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | a.rounded-lg.px-4 95.1x43.6 bg #ffffff @ 0.1 r 8px | a.rounded-lg.px-4 95.1x43.6 r 8px outline 1px auto #101010 offset 1px |

Crops: none.

#### hs-signup-button

"Sign up" button. The solid sign-up control in the nav's right rail.

Page: /. Selector: `nav a,nav button (text Sign up)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 80.53 x 40 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | normal 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #d3fb52 | #a1dd3b | #e7ff89 | #e7ff89 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | NoiGrotesk 14px/15.4px 500 | = | = | = |
| Letter spacing | -0.21px | = | = | = |
| Colour | #14151c | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.flex-col 80.5x40.0 bg #d3fb52 r 8px | a.flex.flex-col 80.5x40.0 bg #a1dd3b r 8px | a.flex.flex-col 80.5x40.0 bg #e7ff89 r 8px outline 1px auto #101010 offset 1px | a.flex.flex-col 80.5x40.0 bg #e7ff89 r 8px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: none.

#### hs-login-link

"Log in" link. The outlined log-in control in the nav's right rail.

Page: /. Selector: `nav a (text Log in)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 73.75 x 40 | = | = |
| Padding | 12px 16px | = | = |
| Gap | normal 4px | = | = |
| Border | 1px solid #ffffff | 1px solid #000000 @ 0 | 1px solid #f3f4fa |
| Radius | 8px | = | = |
| Background | transparent | #ffffff | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | NoiGrotesk 14px/15.4px 500 | = | = |
| Letter spacing | -0.21px | = | = |
| Colour | #ffffff | #14151c | #f3f4fa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | a.flex.flex-col 73.8x40.0 bg #000000 @ 0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | a.flex.flex-col 73.8x40.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | a.flex.flex-col 73.8x40.0 bg #000000 @ 0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px outline 1px auto #101010 offset 1px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: none.

#### hs-nav-menu

Nav mega menu (open). The hover-opened panel under a nav section item. "opened" is the item's own hover: the pointer rests on it until aria-expanded flips.

Page: /. Selector: `nav [class*="panel"], nav [class*="menu"], [role="menu"]`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 1440 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.rounded-lg.px-4: NoiGrotesk 14px/19.6px 400, #ffffff, ls -0.21px |
| Transition | top, color 0.3s, 0.2s ease-in-out, ease delay 0s, 0s |
| Icon | 0 x 0, colour #d3fb52 |
| Painted layers | div.flex.items-center 1392.0x56.0 bg #ffffff @ 0 r 16px; a.rounded-lg.px-4 95.1x43.6 bg #ffffff @ 0.1 r 8px; div.absolute.top-full 860.0x320.3 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px; a.relative.flex 276.0x304.3 bg #f3f4fa r 12px; div.relative.h-38 244.0x152.0 image linear-gradient(to right in oklab, #004449 0px, #052326 100%) r 12px; div.absolute.inset-0 244.0x152.0 image radial-gradient(circle at right top, #d3fb52 @ 0.2 0px, #000000 @ 0 34%) |
| How | the nav item's own hover — the panel is measured in the nav region it overlays |

Crops: none.

#### hs-footer

Footer. The rounded-top footer (rounded-t-3xl) with link columns.

Page: /. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 766.25 |
| Padding | 24px |
| Border | none |
| Radius | 24px 24px 0px 0px |
| Background | #14151c |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.font-noi-grotesk.text-[36px]/lg: NoiGrotesk 40px/44px 400, #ffffff, ls -1px |
| Transition | none |
| Icon | 140 x 46.09, colour #ffffff, fill #000000 |
| Painted layers | footer.w-full.rounded-t-3xl 1440.0x766.3 bg #14151c r 24px 24px 0px 0px |
| Ancestor paint | 1 up div.relative.z-10 bg #14151c |
| How | resting state |

Crops: none.

#### hs-footer-link

Footer link. A single link inside the footer columns.

Page: /. Selector: `footer a`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 140 x 47.22 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | NoiGrotesk 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | #d3fb52 | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 140 x 46.09, colour #ffffff, fill #000000 | 140 x 46.09, colour #d3fb52, fill #000000 | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | a 140.0x47.2 outline 1px auto #101010 offset 1px |

Crops: none.

### Homepage hero

#### hs-hero-h1

Hero headline (h1). "Let's find your next job" — the hero title in the brand face.

Page: /. Selector: `main h1, h1`. States: .

Not found on the page at capture time.

#### hs-search-form

Job search form. The hero job-search field row — measured at rest; typing and submitting were never done (the form navigates to the app).

Page: /. Selector: `form`. States: .

Not found on the page at capture time.

#### hs-search-input

Job search input. The rounded text field inside the hero form.

Page: /. Selector: `form input[type="text"], form input`. States: .

Not found on the page at capture time.

#### hs-search-button

"Search jobs" button. The submit-styled button inside the hero form — pressed states are CDP-forced, so it never submits.

Page: /. Selector: `form button (text Search jobs)`. States: .

Not found on the page at capture time.

#### hs-filter-pill

Job-type pill. A selectable type pill under the search field ("Full-time").

Page: /. Selector: `button (text Full-time)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 91.13 x 45.91 | = | = |
| Padding | 16px | = | = |
| Border | 1px solid #ffffff @ 0.2 | = | = |
| Radius | 8px | = | = |
| Background | transparent | #ffffff @ 0.1 | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 0px |
| Font | NoiGrotesk 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Text node | span.leading-xs.font-noi-grotesk: NoiGrotesk 14px/11.9px 500, #ffffff, ls -0.21px | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.flex.shrink-0 91.1x45.9 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | button.flex.shrink-0 91.1x45.9 bg #ffffff @ 0.1 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | button.flex.shrink-0 91.1x45.9 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px outline 1px auto #101010 offset 0px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: none.

### Employers page

#### hs-banner

Notification banner. The top banner (its height is --notification-banner-height) with its dismiss control.

Page: /employers/. Selector: `[class*="banner" i], [class*="notification" i]`. States: .

Not found on the page at capture time.

#### hs-banner-dismiss

Banner dismiss button. The "Dismiss notification" control — measured, never pressed.

Page: /employers/. Selector: `button (text Dismiss notification)`. States: .

Not found on the page at capture time.

#### hs-segment-tab

Segment switcher tab. One of Source / Automate / Brand / Measure — opacity carries the selection. "selected" is the tab's own press: it swaps the feature panel.

Page: /employers/. Selector: `button (text Source/Automate)`. States: default, hover, selected.

| Property | default | hover | selected |
|---|---|---|---|
| Size (w x h) | 120 x 44 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | NoiGrotesk 40px/44px 400 | = | = |
| Letter spacing | -1px | = | = |
| Colour | #ffffff | #252630 | #252630 |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | the tab's own press — a local UI toggle that swaps the published panel |

Crops: none.

#### hs-cta

CTA link-button. A solid call-to-action ("Post a job today" / "Get started" / "Contact sales") — the group.inline-flex pill.

Page: /employers/. Selector: `a.group.inline-flex (text Get started/Contact sales/Post a job)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 120.38 x 40 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | normal 4px | = | = | = |
| Border | 1px solid #ffffff | 1px solid #000000 @ 0 | 1px solid #f3f4fa | = |
| Radius | 8px | = | = | = |
| Background | transparent | #ffffff | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | NoiGrotesk 16px/17.6px 500 | = | = | = |
| Letter spacing | -0.24px | = | = | = |
| Colour | #ffffff | #14151c | #f3f4fa | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.inline-flex 120.4x40.0 bg #000000 @ 0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | a.group.inline-flex 120.4x40.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | a.group.inline-flex 120.4x40.0 bg #000000 @ 0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px outline 1px auto #101010 offset 1px | = |
| Ancestor paint | 1 up div.flex.flex-1 bg #ffffff @ 0.1 | = | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: none.

#### hs-carousel-dot

Testimonial dot. A carousel page dot ("Go to testimonial N").

Page: /employers/. Selector: `button[aria-label*="testimonial" i]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 8 x 8 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 9999px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | NoiGrotesk 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.size-2.rounded-full 8.0x8.0 bg #ffffff r 9999px | = |
| How | resting state | mouse hover over the element |

Crops: none.

#### hs-faq

FAQ accordion question. A question row in the FAQ. "opened" is the question button's own press: it unfolds the answer.

Page: /employers/. Selector: `button (question)`. States: .

Not found on the page at capture time.

### Pricing page

#### pricing-table

Plan comparison table. One of the plan/feature tables on /employers/pricing/ (the page mounts four).

Page: /employers/pricing/. Selector: `table`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1152 x 856.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | th: NoiGrotesk 16px/24px 700, #000000 |
| Transition | none |
| Icon | 24 x 24, colour #00b1b5 |
| Painted layers | table.w-full.bg-white 1152.0x856.5 bg #ffffff; td.col-span-1.flex 164.6x92.8 bg #252630 @ 0.04; tr.grid.grid-cols-7 1152.0x93.8 border T:1px solid; td.col-span-1.flex 164.6x92.8 bg #252630 @ 0.04; tr.grid.grid-cols-7 1152.0x73.0 border T:1px solid; td.col-span-1.flex 164.6x72.0 bg #252630 @ 0.04 |
| How | resting state |

Crops: none.

#### pricing-th

Table header cell. A th in the comparison table.

Page: /employers/pricing/. Selector: `th`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 83 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | resting state |

Crops: none.

#### pricing-td

Table cell. A td in the comparison table.

Page: /employers/pricing/. Selector: `td`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 493.7 x 92.81 |
| Padding | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.font-noi-grotesk.text-[16px]/xl: NoiGrotesk 16px/22.4px 400, #252630 @ 0.8, ls -0.24px |
| Transition | none |
| How | resting state |

Crops: none.

#### pricing-plan-card

Plan card. A plan column/card on the pricing page.

Page: /employers/pricing/. Selector: `[class*="plan" i], [class*="tier" i], main section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 568 x 70.41 |
| Padding | 0px |
| Gap | normal 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.font-noi-grotesk.text-[32px]/lg: NoiGrotesk 32px/35.2px 400, #000000, ls -0.8px |
| Transition | none |
| Cursor | pointer |
| Icon | 14 x 20, colour #000000 |
| Painted layers | div.flex.size-6 24.0x24.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 9999px |
| How | resting state |

Crops: none.

#### pricing-feature-tab

Feature group tab. A "Target & Connect" / "Centralize" / "Brand" / "Measure" group button that switches the comparison section.

Page: /employers/pricing/. Selector: `button (text Target & Connect/Centralize)`. States: default, hover, selected.

| Property | default | hover | selected |
|---|---|---|---|
| Size (w x h) | 1152 x 74.59 | = | = |
| Padding | 24px | = | = |
| Border | T: none; R: none; B: 1px solid #878aae; L: none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | NoiGrotesk 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | h3.text-left.text-b40: NoiGrotesk 16px/25.6px 600, #000000 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #bebdbf | = | = |
| Painted layers | button.flex.w-full 1152.0x74.6 border B:1px solid | = | = |
| How | resting state | mouse hover over the element | the tab's own press — a local UI toggle |

Crops: none.

### Marketo forms

#### mkto-form

Demo form shell. The "Request a demo" Marketo form — its fields mount from go.joinhandshake.com vendor script.

Page: /employers/request-more-info/. Selector: `form[class*="marketo" i], form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 502.67 x 466 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | button.inline-flex.min-h-12: NoiGrotesk 18px/18px 400, #14151c, ls -0.18px |
| Transition | none |
| Painted layers | input.mktoField.mktoEmailField 502.7x58.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; input.mktoField.mktoTextField 243.3x58.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; input.mktoField.mktoTextField 243.3x58.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; input.mktoField.mktoTextField 502.7x58.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; input.mktoField.mktoTelField 502.7x58.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; input.mktoField.mktoNumberField 502.7x58.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px |
| How | resting state |

Crops: none.

#### mkto-input

Form text field. A text input inside the Marketo form.

Page: /employers/request-more-info/. Selector: `form input[type="text"], form input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 502.67 x 58 | = |
| Padding | 16px | = |
| Border | 1px solid #484851 | 1px solid #ff455b |
| Radius | 4px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | 1px auto #9b53f6 offset 0px |
| Font | NoiGrotesk 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #252630 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #bebdbf, opacity 1 | = |
| Painted layers | input.mktoField.mktoEmailField 502.7x58.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px | input.mktoField.mktoEmailField 502.7x58.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px outline 1px auto #9b53f6 offset 0px |
| How | resting state | the field clicked into |

Crops: none.

#### mkto-select

Form select. A select inside the Marketo form.

Page: /employers/request-more-info/. Selector: `form select`. States: .

Not found on the page at capture time.

#### mkto-submit

Form submit button. The form's submit control — measured, never pressed (pressed states are CDP-forced).

Page: /employers/request-more-info/. Selector: `form button[type="submit"], form button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 502.67 x 48 | = | = | = |
| Padding | 14px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #d3fb52 | #d7fb61 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | NoiGrotesk 18px/18px 400 | = | = | = |
| Letter spacing | -0.18px | = | = | = |
| Colour | #14151c | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.min-h-12 502.7x48.0 bg #d3fb52 r 4px | button.inline-flex.min-h-12 502.7x48.0 bg #d7fb61 r 4px | button.inline-flex.min-h-12 502.7x48.0 bg #d3fb52 r 4px outline 1px auto #101010 offset 0px | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: none.

#### cc-form

Career-center contact form. The EDU contact form on /career-centers/contact/ — same Marketo stack.

Page: /career-centers/contact/. Selector: `form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 728 x 921.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | label.mktoLabel.mktoHasWidth: NoiGrotesk 16px/25.6px 400, #000000 |
| Transition | none |
| Painted layers | input.mktoField.mktoTextField 728.0x40.0 bg #f3f4fa r 3px; input.mktoField.mktoTextField 728.0x40.0 bg #f3f4fa r 3px; input.mktoField.mktoEmailField 728.0x40.0 bg #f3f4fa r 3px; input.mktoField.mktoTelField 728.0x40.0 bg #f3f4fa r 3px; input.mktoField.mktoTextField 728.0x40.0 bg #f3f4fa r 3px; select.mktoField.mktoHasWidth 728.0x35.0 bg #f3f4fa r 3px |
| How | resting state |

Crops: none.

### Students page

#### stu-email-input

Email capture field. The "Type school or personal email here" field in the hero — measured at rest, nothing typed.

Page: /students/. Selector: `input[type="email"]`. States: .

Not found on the page at capture time.

#### stu-signup-button

"Sign up" CTA. The students sign-up button (group.inline-flex).

Page: /students/. Selector: `button.group.inline-flex (text Sign up)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 82.53 x 40 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | normal 4px | = | = | = |
| Border | 1px solid #ffffff | 1px solid #000000 @ 0 | 1px solid #f3f4fa | 1px solid #000000 @ 0 |
| Radius | 8px | = | = | = |
| Background | transparent | #ffffff | = | #ffffff |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | NoiGrotesk 14px/15.4px 500 | = | = | = |
| Letter spacing | -0.21px | = | = | = |
| Colour | #ffffff | #14151c | #f3f4fa | #14151c |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.flex-col 82.5x40.0 bg #000000 @ 0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | a.flex.flex-col 82.5x40.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | a.flex.flex-col 82.5x40.0 bg #000000 @ 0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px outline 1px auto #101010 offset 1px | a.flex.flex-col 82.5x40.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: none.

#### stu-text-link

Arrow text link. "Find jobs and internships →" — an arrow-suffixed text link in the brand face.

Page: /students/. Selector: `a (text Find jobs and internships)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 243.53 x 46.41 | = | = |
| Padding | 12px 20px | = | = |
| Gap | 8px | = | = |
| Border | none | = | = |
| Radius | 32px | = | = |
| Background | #052326 @ 0.8 | #004449 @ 0.8 | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | NoiGrotesk 16px/22.4px 500 | = | = |
| Letter spacing | -0.24px | = | = |
| Colour | #ffffff | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | a.font-noi-grotesk.text-[16px]/xl 243.5x46.4 bg #052326 @ 0.8 r 32px | a.font-noi-grotesk.text-[16px]/xl 243.5x46.4 bg #004449 @ 0.8 r 32px | a.font-noi-grotesk.text-[16px]/xl 243.5x46.4 bg #052326 @ 0.8 r 32px outline 1px auto #101010 offset 1px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: none.

#### stu-carousel-btn

Card carousel arrow. A "Slide to the next/previous card" arrow button.

Page: /students/. Selector: `button[aria-label*="card" i]`. States: .

Not found on the page at capture time.

### Blog

#### blog-search-input

Blog search field. The search input on the blog index — measured at rest, nothing typed.

Page: /blog/. Selector: `input[type="search"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 343 x 27 | = |
| Padding | 0px 0px 0px 8px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #f3f4fa | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | NoiGrotesk 22px/22px 400 | = |
| Letter spacing | -0.44px | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #000000, opacity 1 | = |
| Painted layers | input.w-full.bg-neutral-10 343.0x27.0 bg #f3f4fa | = |
| How | resting state | the field clicked into |
| Ancestor paint | - | 2 up div.flex.min-h-12 bg #f3f4fa outline 1px solid #000000 |

Crops: none.

#### blog-search-button

Search button. The Search button beside the field — CDP-forced states only.

Page: /blog/. Selector: `button (text Search)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 88.92 x 48 | = | = | = |
| Padding | 14px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #052326 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | NoiGrotesk 18px/18px 400 | = | = | = |
| Letter spacing | -0.18px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.min-h-12 88.9x48.0 bg #052326 r 4px | = | button.inline-flex.min-h-12 88.9x48.0 bg #052326 r 4px outline 1px auto #101010 offset 0px | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: none.

#### blog-category-link

Category link. An uppercase category link ("AI SKILLS STUDIO").

Page: /blog/. Selector: `a.uppercase`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 137 x 17 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | NoiGrotesk 16px/24px 600 | = | = |
| Letter spacing | normal | = | = |
| Colour | #2e6aff | #1552d6 | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | a.uppercase.font-semibold 137.0x17.0 outline 1px auto #101010 offset 1px |

Crops: none.

#### blog-card

Article card. An article card link on the blog index.

Page: /blog/. Selector: `main a[href*="/blog/"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 137 x 17 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | NoiGrotesk 16px/24px 600 | = |
| Letter spacing | normal | = |
| Colour | #2e6aff | #1552d6 |
| Transition | none | = |
| Cursor | pointer | = |
| How | resting state | mouse hover over the element |

Crops: none.

#### blog-readmore

"Read More" link. The Read More affordance on an article card.

Page: /blog/. Selector: `a (text Read More)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 536 x 25.5 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | NoiGrotesk 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | p.font-noi-grotesk.text-[18px]/xl: NoiGrotesk 22px/24.2px 700, #000000, ls -0.33px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 14.11 x 24, colour #000000 | = |
| Ancestor paint | 1 up div.flex.flex-col bg #ffffff | = |
| How | resting state | mouse hover over the element |

Crops: none.

### Careers page

#### car-benefit-tab

Benefits tab. A benefits category button ("Health & wellness") — the tab's own press swaps the panel.

Page: /careers/. Selector: `button (text Health & wellness)`. States: default, hover, selected.

| Property | default | hover | selected |
|---|---|---|---|
| Size (w x h) | 568 x 35.2 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | NoiGrotesk 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | h2.font-noi-grotesk.text-[32px]/lg: NoiGrotesk 32px/35.2px 400, #000000, ls -0.8px | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 14 x 20, colour #000000 | = | = |
| Painted layers | div.flex.size-6 24.0x24.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 9999px | = | = |
| How | resting state | mouse hover over the element | the tab's own press — a local UI toggle |

Crops: none.

#### car-search-input

Roles search field. The open-roles search input — measured at rest, nothing typed.

Page: /careers/. Selector: `input[placeholder*="earch" i], input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 688 x 56 | = |
| Padding | 16px 12px | = |
| Border | 1px solid #252630 @ 0.1 | 1px solid #252630 |
| Radius | 12px | = |
| Background | #ffffff | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #252630 0px 0px 0px 1px |
| Outline | none | = |
| Font | NoiGrotesk 16px/22.4px 400 | = |
| Letter spacing | -0.24px | = |
| Colour | #14151c | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #bebdbf, opacity 1 | #bebdbf, opacity 0 |
| Painted layers | input.border.transition-all 688.0x56.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px | input.border.transition-all 688.0x56.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #252630 0px 0px 0px 1px |
| How | resting state | the field clicked into |

Crops: none.

#### car-dept-button

Department accordion. A department group header in the roles list — "opened" is the header's own press.

Page: /careers/. Selector: `button.group.flex`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 218.67 x 56 | = | = |
| Padding | 16px 12px | = | = |
| Border | 1px solid #252630 @ 0.1 | 1px solid #bebdbf | 1px solid #252630 |
| Radius | 12px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #252630 0px 0px 0px 1px |
| Outline | none | = | = |
| Font | NoiGrotesk 14px/19.6px 400 | = | = |
| Letter spacing | -0.21px | = | = |
| Colour | #14151c | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 24 x 24, colour #14151c, fill #000000 | = | = |
| Painted layers | button.group.flex 218.7x56.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px | = | button.group.flex 218.7x56.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #252630 0px 0px 0px 1px |
| How | resting state | mouse hover over the element | the header's own press — a local UI toggle |

Crops: none.

#### car-job-link

Job row link. An open-role link in the list.

Page: /careers/. Selector: `a (job title)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1392 x 122 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | NoiGrotesk 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | p.font-noi-grotesk.text-[24px]/lg: NoiGrotesk 24px/26.4px 400, #000000, ls -0.36px | p.font-noi-grotesk.text-[24px]/lg: NoiGrotesk 24px/26.4px 400, #ffffff, ls -0.36px |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.group.flex 1392.0x122.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px; div.group.inline-flex 73.8x40.0 bg #252630 r 8px | div.group.flex 1392.0x122.0 bg #252630 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px; div.group.inline-flex 73.8x40.0 bg #d3fb52 r 8px |
| How | resting state | mouse hover over the element |

Crops: none.

#### car-page-button

Pagination button. A page number in the roles pagination.

Page: /careers/. Selector: `button.group.inline-flex (text 1/2/3)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = |
| Padding | 0px | = | = |
| Border | 1px solid #14151c | = | = |
| Radius | 12px | = | = |
| Background | #14151c | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 0px |
| Font | NoiGrotesk 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.group.inline-flex 48.0x48.0 bg #14151c border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px | = | button.group.inline-flex 48.0x48.0 bg #14151c border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px outline 1px auto #101010 offset 0px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: none.

### Legal pages

#### legal-nav-active

Legal nav link (active). The current section link in the legal left rail (opacity-100).

Page: /legal/tos/. Selector: `a.font-medium`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 73.75 x 40 | = |
| Padding | 12px 16px | = |
| Gap | normal 4px | = |
| Border | 1px solid #252630 | 1px solid #000000 @ 0 |
| Radius | 8px | = |
| Background | transparent | #14151c @ 0.1 |
| Box shadow | none | = |
| Outline | none | = |
| Font | NoiGrotesk 14px/15.4px 500 | = |
| Letter spacing | -0.21px | = |
| Colour | #252630 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | a.flex.flex-col 73.8x40.0 bg #000000 @ 0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | a.flex.flex-col 73.8x40.0 bg #14151c @ 0.1 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px |
| How | resting state | mouse hover over the element |

Crops: none.

#### legal-nav-link

Legal nav link. An inactive section link in the legal left rail (opacity-60).

Page: /legal/tos/. Selector: `a.opacity-60`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 305.5 x 22.41 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | NoiGrotesk 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | p.font-noi-grotesk.text-[16px]/xl: NoiGrotesk 16px/22.4px 400, #000000, ls -0.24px | = | = |
| Transition | none | = | = |
| Opacity | 0.6 | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | a.opacity-60 305.5x22.4 outline 1px auto #101010 offset 1px |

Crops: none.

### App access

#### app-shell

Login page shell. The /access page body — the consumer app's signed-out entry.

Page: https://app.joinhandshake.com/access. Selector: `main, #maincontent, body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 72px 0px 76px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Noi Grotesk 15px/18px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | output.rosetta-select__option-ellipsis.rosetta-select__output: Noi Grotesk 15px/18px 400, #121212 |
| Transition | none |
| Icon | 20 x 20, colour #121212 @ 0.7, fill #000000 |
| Painted layers | div.rosetta-field__base.sc-ezOQGI 137.0x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; div.sc-bYMpWt.jDuFBQ 0.0x0.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px shadow #000000 @ 0.08 0px 6px 30px 0px, #000000 @ 0.08 0px 1px 3px 0px; div.rosetta-select__option.rosetta-body-medium 0.0x0.0 bg #e7e7e7 r 8px; select.rosetta-select__hidden 1.0x1.0 bg #efefef; svg.rosetta-logo-app-icon.rosetta-entity-avatar 48.0x48.0 bg #ffffff r 8px outline 1px solid #121212 @ 0.12 offset -1px; hr.sc-fNAUDI.fQrJOK 157.0x2.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid |
| How | resting state |

Crops: none.

#### app-locale-select

Locale select. The "English (US)" rosetta-select in the page chrome.

Page: https://app.joinhandshake.com/access. Selector: `select.rosetta-select__hidden, select`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 137 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Noi Grotesk 15px/18px 400 |
| Letter spacing | normal |
| Colour | #121212 |
| Text node | output.rosetta-select__option-ellipsis.rosetta-select__output: Noi Grotesk 15px/18px 400, #121212 |
| Transition | none |
| Icon | 20 x 20, colour #121212 @ 0.7, fill #000000 |
| Painted layers | div.rosetta-field__base.sc-ezOQGI 137.0x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; div.sc-bYMpWt.jDuFBQ 0.0x0.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px shadow #000000 @ 0.08 0px 6px 30px 0px, #000000 @ 0.08 0px 1px 3px 0px; div.rosetta-select__option.rosetta-body-medium 0.0x0.0 bg #e7e7e7 r 8px; select.rosetta-select__hidden 1.0x1.0 bg #efefef |
| How | resting state |

Crops: none.

#### app-email-field

Email field. The "Enter your email" rosetta-field — measured at rest, nothing typed.

Page: https://app.joinhandshake.com/access. Selector: `input[name="email"], input[type="text"]`. States: .

Not found on the page at capture time.

#### app-continue-button

"Continue with email" button. The rosetta-button submit — pressed states are CDP-forced, so the form never submits.

Page: https://app.joinhandshake.com/access. Selector: `button.rosetta-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 344 x 40 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #04191b | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #003bcc offset 2px | = |
| Font | Noi Grotesk 15px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.rosetta-button.sc-ftTHYK 344.0x40.0 bg #04191b r 8px | button.rosetta-button.sc-ftTHYK 344.0x40.0 bg #04191b image linear-gradient(#ffffff @ 0.06, #ffffff @ 0.06) r 8px | button.rosetta-button.sc-ftTHYK 344.0x40.0 bg #04191b r 8px outline 2px solid #003bcc offset 2px | button.rosetta-button.sc-ftTHYK 344.0x40.0 bg #04191b image linear-gradient(#ffffff @ 0.12, #ffffff @ 0.12) r 8px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |
| Background image | - | linear-gradient(#ffffff @ 0.06, #ffffff @ 0.06) | = | linear-gradient(#ffffff @ 0.12, #ffffff @ 0.12) |

Crops: none.

#### app-google-button

Google SSO button. The "Continue with Google" button — Google's own rendered widget (GSI), recorded as vendor.

Page: https://app.joinhandshake.com/access. Selector: `[class*="LgbsSe"], [id*="gsi" i], iframe[title*="Google" i]`. States: .

Not found on the page at capture time.

#### app-employer-link

"Sign up as an employer" link. The employer sign-up link under the login card.

Page: https://app.joinhandshake.com/access. Selector: `a (text employer)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 61 x 16 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Noi Grotesk 15px/18px 400 | = |
| Letter spacing | normal | = |
| Colour | #1569e0 | #0e489a |
| Transition | none | = |
| Cursor | pointer | = |
| How | resting state | mouse hover over the element |

Crops: none.

#### app-tos-link

Terms link. The Terms of Service link in the fine print.

Page: https://app.joinhandshake.com/access. Selector: `a (text Terms of Service)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 106.09 x 14 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Noi Grotesk 13px/15.6px 400 | = |
| Letter spacing | 0.13px | = |
| Colour | #1569e0 | #0e489a |
| Transition | none | = |
| Cursor | pointer | = |
| Ancestor paint | 1 up div bg #ffffff @ 0.6 | = |
| How | resting state | mouse hover over the element |

Crops: none.

### Site chrome (mobile)

#### m-hs-topbar

Mobile header pill. The floating pill at 390px: the mobile nav wrapper is a 0-height relative container; the painted bar is its fixed child (wordmark, links, the "Open menu" button).

Page: /. Selector: `nav[class*="xl:hidden"] > div:first-child (fixed pill)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 48 |
| Padding | 8px |
| Border | none |
| Radius | 12px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.group.items-center: NoiGrotesk 16px/14.4px 500, #252630, ls -0.24px |
| Transition | none |
| Icon | 32 x 32, colour #000000 |
| Painted layers | div.fixed.top-(--mobile-top-offset) 358.0x48.0 bg #ffffff r 12px; a.group.items-center 88.3x40.0 bg #000000 @ 0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; a.group.items-center 76.6x40.0 bg #252630 r 8px; a.group.items-center 0.0x0.0 bg #252630 r 8px |
| How | resting state |

Crops: none.

#### m-hs-hamburger

"Open menu" button. The icon-only button (aria-label "Open menu", no text content) that opens the mobile nav sheet.

Page: /. Selector: `button[aria-label="Open menu"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 24 x 16 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | NoiGrotesk 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #000000 | = |
| How | resting state | mouse hover over the element |

Crops: none.

#### m-hs-drawer

Nav sheet (open). The opened mobile navigation sheet. The "Open menu" press happens in find(): the sheet is only reachable once open, so the state itself is a no-op.

Page: /. Selector: `div[class*="mobile-nav-height"][class*="100dvh"] (the fixed sheet under the bar; Ketch's dialog is excluded)`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 390 x 772 |
| Padding | 8px 16px 24px 16px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | button.flex.w-full: NoiGrotesk 28px/30.8px 400, #000000, ls -0.7px |
| Transition | none |
| Icon | 16 x 16, colour #000000 |
| Painted layers | div.fixed.top-[calc(var(--mobile-top-offset)+var(--mobile-nav-height))] 390.0x772.0 bg #ffffff; div.fixed.inset-0 390.0x772.0 bg #ffffff; div.h-px.w-screen 390.0x1.0 bg #252630 @ 0.1; div.h-px.bg-neutral-90/10 358.0x1.0 bg #252630 @ 0.1; div.h-px.bg-neutral-90/10 358.0x1.0 bg #252630 @ 0.1; div.h-px.bg-neutral-90/10 358.0x1.0 bg #252630 @ 0.1 |
| How | the "Open menu" button's own press |

Crops: none.

## Transitions declared in the readable stylesheets

joinhandshake.com serves its own CSS same-origin (/_next/static/css) and app.joinhandshake.com from handshake-production-cdn.joinhandshake.com, so this list is the sites' own transition declarations the CSSOM could read on each page.

- /: `opacity 0.25s linear`

- /blog/: `transform 0.1s ease-in-out`, `transform 0.1s ease-out`, `opacity 0.25s linear`

- /career-centers/contact/: `transform 0.1s ease-in-out`, `transform 0.1s ease-out`, `opacity 0.25s linear`

- /careers/: `opacity 0.25s linear`

- /employers/: `opacity 0.25s linear`

- /employers/pricing/: `opacity 0.25s linear`

- /employers/request-more-info/: `transform 0.1s ease-in-out`, `transform 0.1s ease-out`, `opacity 0.25s linear`

- /legal/tos/: `transform 0.1s ease-in-out`, `transform 0.1s ease-out`, `opacity 0.25s linear`

- /students/: `opacity 0.25s linear`

- https://app.joinhandshake.com/access: `transform 300ms ease-in`, `opacity 150ms ease-in`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`
