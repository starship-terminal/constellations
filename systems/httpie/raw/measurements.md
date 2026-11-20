# Component measurements

Computed styles read from httpie.io (the marketing surface and the signed-out /app client) on 2026-11-17 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a field clicked into (nothing typed); `light` is the same element after the footer's own LIGHT MODE radio repainted html.light (the site boots html.dark); `opened` and the rest are resting states reached by a component's own UI toggle. Send was never pressed on /app — issuing a request is a network side effect, so the response panel is measured only at its resting 'Not sent' state. Nothing was typed, sent or signed into.

## Components

### Site chrome

#### site-nav

Site navigation bar. The top nav (Navigation_navigation): wordmark, Desktop / Terminal / AI / Docs / Jobs / Blog links and the "Go to App →" primary button.

Page: /. Selector: `nav[class*="Navigation_navigation"]`. States: default, light.

| Property | default | light |
|---|---|---|
| Size (w x h) | 1440 x 130 | = |
| Padding | 0px 55px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Pie Body 16px/24px 400 | = |
| Letter spacing | 0.176px | = |
| Colour | #f5f5f0 | #1e1919 |
| Text node | a.Link_link__58k5P.Navigation_link__hMCGF: Pie Body 18px/30px 400, #f5f5f0, ls 0.198px | a.Link_link__58k5P.Navigation_link__hMCGF: Pie Body 18px/30px 400, #1e1919, ls 0.198px |
| Transition | none | = |
| Icon | 140 x 40.23, colour #f5f5f0 | 140 x 40.23, colour #1e1919 |
| Painted layers | span.Count_count__p9ULf.Navigation_count__CXLW6 19.0x19.0 bg #363636 r 9999px; button.Button_button__mg_cR.Button_primary__PFIP8 180.0x51.0 bg #73dc8c border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px; div.Navigation_featuredIconCircle__n4aZN 0.0x0.0 bg #363636 r 9999px | span.Count_count__p9ULf.Navigation_count__CXLW6 19.0x19.0 bg #ededeb r 9999px; button.Button_button__mg_cR.Button_primary__PFIP8 180.0x51.0 bg #73dc8c border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px; div.Navigation_featuredIconCircle__n4aZN 0.0x0.0 bg #d1d1cf r 9999px |
| How | resting state | same element after the footer's own LIGHT MODE radio repaints html.light (the site boots html.dark, so light is the switched state) |

Crops: `site-nav-default.png`, `site-nav-light.png`.

#### nav-link

Nav link. A primary nav link ("Terminal").

Page: /. Selector: `nav a`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 70.59 x 30 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px |
| Font | Pie Body 18px/30px 400 | = | = |
| Letter spacing | 0.198px | = | = |
| Colour | #f5f5f0 | #73dc8c | #73dc8c |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | a.Link_link__58k5P.Navigation_link__hMCGF 70.6x30.0 outline 2px solid #000000 @ 0 offset 2px |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`.

#### nav-cta

"Go to App →" button. The solid primary button in the nav — links to /app, measured never followed.

Page: /. Selector: `button[class*="Button_button"], a[class*="Button_button"] (text Go to App)`. States: default, hover, focus-visible, pressed, light.

| Property | default | hover | focus-visible | pressed | light |
|---|---|---|---|---|---|
| Size (w x h) | 180 x 51 | = | = | = | = |
| Padding | 13px 21px 13px 19px | = | = | = | = |
| Border | 2px solid #000000 @ 0 | = | 2px solid #73dc8c | = | = |
| Radius | 9999px | = | = | = | = |
| Background | #73dc8c | #4f4d4d | #4f4d4d | #4f4d4d | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | Pie Body 15px/21px 400 | = | = | = | = |
| Letter spacing | 0.165px | = | = | = | = |
| Colour | #1e1919 | #73dc8c | #73dc8c | #73dc8c | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | button.Button_button__mg_cR.Button_primary__PFIP8 180.0x51.0 bg #73dc8c border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px | button.Button_button__mg_cR.Button_primary__PFIP8 180.0x51.0 bg #4f4d4d border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px | button.Button_button__mg_cR.Button_primary__PFIP8 180.0x51.0 bg #4f4d4d border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px outline 2px solid #000000 @ 0 offset 2px | button.Button_button__mg_cR.Button_primary__PFIP8 180.0x51.0 bg #4f4d4d border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press | same element after the footer's own LIGHT MODE radio repaints html.light (the site boots html.dark, so light is the switched state) |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`, `nav-cta-light.png`.

#### site-footer

Site footer. The page footer (Footer_footer): link columns, the social icons, and the LIGHT MODE / AUTO / DARK MODE theme control.

Page: /. Selector: `footer[class*="Footer_footer"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 440.22 |
| Padding | 75px 0px 40px 0px |
| Border | none |
| Radius | 0px |
| Background | #363636 |
| Box shadow | none |
| Outline | none |
| Font | Pie Body 16px/24px 400 |
| Letter spacing | 0.176px |
| Colour | #f5f5f0 |
| Text node | h2.Text_base__4755h.Text_smallSubheading__Ylu0h: Pie Body 16px/22.4px 600, #f5f5f0, ls 0.176px |
| Transition | none |
| Icon | 140 x 40.23, colour #f5f5f0 |
| Painted layers | footer.Footer_footer__MU3xC 1440.0x440.2 bg #363636; div.ThemeToggle_container__5I861 0.0x0.0 bg #1e1919 r 9999px; div.ThemeToggle_radio__IFs89 0.0x0.0 bg #666663 r 9999px; div.ThemeToggle_radio__IFs89 0.0x0.0 bg #666663 r 9999px; div.ThemeToggle_radio__IFs89.ThemeToggle_active__3wrnM 0.0x0.0 bg #f5f5f0 r 9999px; span.Count_count__p9ULf.Footer_count__dSdCn 19.0x19.0 bg #4f4d4d r 9999px |
| How | resting state |

Crops: `site-footer-default.png`.

#### theme-toggle

Theme toggle (LIGHT / AUTO / DARK). The footer's three-segment ThemeToggle radio stack — the product's real theme control. "light" is its own LIGHT MODE press, restored to DARK after.

Page: /. Selector: `[class*="ThemeToggle_wrapper"]`. States: default, light.

| Property | default | light |
|---|---|---|
| Size (w x h) | 70 x 194.44 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Pie Body 16px/24px 400 | = |
| Letter spacing | 0.176px | = |
| Colour | #f5f5f0 | #1e1919 |
| Text node | span.Text_base__4755h.Text_smallBody__zKyrD: Pie Body 10px/14px 400, #ededeb, ls 0.11px | span.Text_base__4755h.Text_smallBody__zKyrD: Pie Body 10px/14px 400, #363636, ls 0.11px |
| Transition | none | = |
| Painted layers | div.ThemeToggle_container__5I861 70.0x30.0 bg #1e1919 r 9999px; div.ThemeToggle_radio__IFs89 4.0x4.0 bg #666663 r 9999px; div.ThemeToggle_radio__IFs89 4.0x4.0 bg #666663 r 9999px; div.ThemeToggle_radio__IFs89.ThemeToggle_active__3wrnM 14.0x14.0 bg #f5f5f0 r 9999px | div.ThemeToggle_container__5I861 70.0x30.0 bg #7d7d7d r 9999px; div.ThemeToggle_radio__IFs89 4.0x4.0 bg #b5b5b2 r 9999px; div.ThemeToggle_radio__IFs89.ThemeToggle_active__3wrnM 14.0x14.0 bg #f5f5f0 r 9999px; div.ThemeToggle_radio__IFs89 4.0x4.0 bg #b5b5b2 r 9999px |
| How | resting state | same element after the footer's own LIGHT MODE radio repaints html.light (the site boots html.dark, so light is the switched state) |

Crops: `theme-toggle-default.png`, `theme-toggle-light.png`.

#### social-button

Social button. A footer social action ("Discord") — a Button_secondary with an icon.

Page: /. Selector: `button[class*="Button_button"], a[class*="Button_button"] (text Discord)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 119.16 x 51 | = |
| Padding | 13px 18px | = |
| Border | 2px solid #000000 @ 0 | = |
| Radius | 9999px | = |
| Background | #f5f5f0 | #4f4d4d |
| Box shadow | none | = |
| Outline | none | = |
| Font | Pie Body 15px/21px 400 | = |
| Letter spacing | 0.165px | = |
| Colour | #1e1919 | #f5f5f0 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 17 x 20.19, colour #1e1919 | 17 x 20.19, colour #f5f5f0 |
| Painted layers | button.Button_button__mg_cR.Button_secondary__kYMEY 119.2x51.0 bg #f5f5f0 border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px | button.Button_button__mg_cR.Button_secondary__kYMEY 119.2x51.0 bg #4f4d4d border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px |
| How | resting state | mouse hover over the element |

Crops: `social-button-default.png`, `social-button-hover.png`.

### Buttons and links

#### button-secondary

Secondary button. An outlined action ("Read blog post" on the changelog banner).

Page: /. Selector: `button[class*="Button_button"], a[class*="Button_button"] (text Read blog post)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 180 x 51 | = | = | - |
| Padding | 13px 18px | = | = | - |
| Border | 2px solid #000000 @ 0 | = | 2px solid #f5f5f0 | - |
| Radius | 9999px | = | = | - |
| Background | #f5f5f0 | #4f4d4d | #4f4d4d | - |
| Box shadow | none | = | = | - |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | - |
| Font | Pie Body 15px/21px 400 | = | = | - |
| Letter spacing | 0.165px | = | = | - |
| Colour | #1e1919 | #f5f5f0 | #f5f5f0 | - |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | - |
| Cursor | pointer | = | = | - |
| Painted layers | button.Button_button__mg_cR.Button_secondary__kYMEY 180.0x51.0 bg #f5f5f0 border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px | button.Button_button__mg_cR.Button_secondary__kYMEY 180.0x51.0 bg #4f4d4d border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px | button.Button_button__mg_cR.Button_secondary__kYMEY 180.0x51.0 bg #4f4d4d border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px outline 2px solid #000000 @ 0 offset 2px | - |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | - |
| Error | - | = | = | cdpSession.send: Protocol error (DOM.getNodeForLocation): No node found at given location |

Crops: `button-secondary-default.png`, `button-secondary-hover.png`, `button-secondary-focus-visible.png`.

#### button-counter

Counter button ("Star on GitHub"). The GitHub star button carrying its live count — Button_counter.

Page: /. Selector: `button[class*="Button_button"], a[class*="Button_button"] (text Star on GitHub)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 253.31 x 53 | = | = |
| Padding | 14px 100px 14px 18px | = | = |
| Border | 2px solid #000000 @ 0 | = | 2px solid #f5f5f0 |
| Radius | 9999px | = | = |
| Background | #f5f5f0 | #4f4d4d | #4f4d4d |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px |
| Font | Pie Body 15px/21px 400 | = | = |
| Letter spacing | 0.165px | = | = |
| Colour | #1e1919 | #f5f5f0 | #f5f5f0 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 17 x 17, colour #1e1919 | 17 x 17, colour #f5f5f0 | 17 x 17, colour #f5f5f0 |
| Painted layers | button.Button_button__mg_cR.Button_counter__Xwdnb 253.3x53.0 bg #f5f5f0 border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px; div.Button_counterElement__fBsBu 79.0x49.0 bg #1e1919 r 100px | button.Button_button__mg_cR.Button_counter__Xwdnb 253.3x53.0 bg #4f4d4d border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px; div.Button_counterElement__fBsBu 79.0x49.0 bg #f5f5f0 r 100px | button.Button_button__mg_cR.Button_counter__Xwdnb 253.3x53.0 bg #4f4d4d border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px outline 2px solid #000000 @ 0 offset 2px; div.Button_counterElement__fBsBu 79.0x49.0 bg #f5f5f0 r 100px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `button-counter-default.png`, `button-counter-hover.png`, `button-counter-focus-visible.png`.

#### button-share

Share button. "Share on Twitter" in the testimonial wall footer — Button_share.

Page: /. Selector: `button[class*="Button_button"], a[class*="Button_button"] (text Share on Twitter)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 183.64 x 51 | = |
| Padding | 13px 18px | = |
| Border | 2px solid #000000 @ 0 | = |
| Radius | 9999px | = |
| Background | #363636 | #7d7d7d |
| Box shadow | none | = |
| Outline | none | = |
| Font | Pie Body 15px/21px 400 | = |
| Letter spacing | 0.165px | = |
| Colour | #f5f5f0 | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 17 x 13.81, colour #f5f5f0 | = |
| Painted layers | button.Button_button__mg_cR.Button_share__Z0BDa 183.6x51.0 bg #363636 border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px | button.Button_button__mg_cR.Button_share__Z0BDa 183.6x51.0 bg #7d7d7d border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px |
| How | resting state | mouse hover over the element |

Crops: `button-share-default.png`, `button-share-hover.png`.

#### text-link

Text link. A Link_link in page content.

Page: /. Selector: `a[class*="Link_link"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 140 x 40 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Pie Body 16px/24px 400 | = |
| Letter spacing | 0.176px | = |
| Colour | #f5f5f0 | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | default | = |
| Icon | 140 x 40.23, colour #f5f5f0 | = |
| How | resting state | mouse hover over the element |

Crops: `text-link-default.png`, `text-link-hover.png`.

### Home

#### hero-headline

Hero headline. The home hero h1 "FLOW THROUGH APIs" — Pie Headline (FK Screamer).

Page: /. Selector: `h1`. States: default, light.

| Property | default | light |
|---|---|---|
| Size (w x h) | 296.16 x 261.61 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Pie Headline 109px/87.2px 400 | = |
| Letter spacing | 1.308px | = |
| Colour | #f5f5f0 | #1e1919 |
| Transition | none | = |
| How | resting state | same element after the footer's own LIGHT MODE radio repaints html.light (the site boots html.dark, so light is the switched state) |

Crops: `hero-headline-default.png`, `hero-headline-light.png`.

#### testimonial-card

Testimonial card. A tweet card in the community wall (TestimonialCard_tweet): avatar, name, handle, body, timestamp.

Page: /. Selector: `[class*="TestimonialCard_tweet"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 238 |
| Padding | 44px 30px 30px 30px |
| Border | none |
| Radius | 10px |
| Background | #4b78e6 |
| Box shadow | none |
| Outline | none |
| Font | Pie Body 16px/24px 400 |
| Letter spacing | 0.176px |
| Colour | #f5f5f0 |
| Text node | div.Text_base__4755h.Text_smallBody__zKyrD: Pie Body 15px/21px 400, #f5f5f0, ls 0.165px |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Painted layers | div.TestimonialCard_tweet__BY5ak.TestimonialCard_blue__i1ES8 360.0x238.0 bg #4b78e6 r 10px |
| How | resting state |

Crops: none.

#### newsletter-input

Newsletter email input. The "Enter email address" field of a NewsletterForm. "focused" is the field clicked into — nothing is typed, the form is never submitted.

Page: /. Selector: `input[type="email"]`. States: default, focused, light.

| Property | default | focused | light |
|---|---|---|---|
| Size (w x h) | 427.33 x 44 | = | = |
| Padding | 12px 12px 13px 20px | = | = |
| Border | 2px solid #000000 @ 0 | 2px solid #73dc8c | = |
| Radius | 9999px | = | = |
| Background | #3354a6 | = | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #73dc8c 0px 0px 0px 1px, #73dc8c 0px 0px 0px 1px | = |
| Outline | none | 2px solid #000000 @ 0 offset 2px | = |
| Font | Pie Body 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #f5f5f0 | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #b5b5b2, opacity 1 | = | = |
| Painted layers | input.NewsletterForm_textInput__CWjAF.NewsletterForm_community__DgwWa 427.3x44.0 bg #3354a6 border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px | input.NewsletterForm_textInput__CWjAF.NewsletterForm_community__DgwWa 427.3x44.0 bg #3354a6 border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px shadow #ffffff 0px 0px 0px 0px, #73dc8c 0px 0px 0px 1px, #73dc8c 0px 0px 0px 1px outline 2px solid #000000 @ 0 offset 2px | = |
| How | resting state | the field clicked into | same element after the footer's own LIGHT MODE radio repaints html.light (the site boots html.dark, so light is the switched state) |

Crops: `newsletter-input-default.png`, `newsletter-input-focused.png`, `newsletter-input-light.png`.

#### newsletter-button

Newsletter submit button. The form's arrow submit — measured, never pressed.

Page: /. Selector: `form button`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 38 x 38 | 32.3 x 32.3 |
| Padding | 0px | = |
| Border | none | = |
| Radius | 9999px | = |
| Background | #73dc8c | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Pie Body 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #f5f5f0 | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 8 x 14.39, colour #1e1919 | 6.8 x 12.23, colour #1e1919 |
| Painted layers | button.NewsletterForm_button__XpGNJ.NewsletterForm_community__DgwWa 38.0x38.0 bg #73dc8c r 9999px | button.NewsletterForm_button__XpGNJ.NewsletterForm_community__DgwWa 32.3x32.3 bg #73dc8c r 9999px |
| How | resting state | mouse hover over the element |
| Transform | - | matrix(0.85, 0, 0, 0.85, 0, 0) |

Crops: `newsletter-button-default.png`, `newsletter-button-hover.png`.

#### early-access-badge

"Public beta" badge. The β Public beta pill on the hero (EarlyAccessBadge).

Page: /. Selector: `[class*="EarlyAccessBadge"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 132.7 x 34 |
| Padding | 4px 12px 4px 4px |
| Border | none |
| Radius | 9999px |
| Background | #363636 |
| Box shadow | none |
| Outline | none |
| Font | Pie Body 16px/24px 400 |
| Letter spacing | 0.176px |
| Colour | #f5f5f0 |
| Text node | span.Text_base__4755h.Text_smallBody__zKyrD: Pie Body 14px/24px 600, #1e1919, ls 0.154px |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | div.EarlyAccessBadge_badge__meFy7.AppSection_earlyAccessBadge__cWP_T 132.7x34.0 bg #363636 r 9999px; span.EarlyAccessBadge_pill__anq3U.EarlyAccessBadge_pingAnimation__caxLr 26.0x26.0 bg #fa9bfa r 9999px; span::after.EarlyAccessBadge_pill__anq3U.EarlyAccessBadge_pingAnimation__caxLr 26pxx26px bg #fa9bfa r 9999px |
| How | resting state |

Crops: `early-access-badge-default.png`.

#### section-heading

Section heading. A home section heading (the testimonial wall's h2).

Page: /. Selector: `main h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 653 x 84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Pie Body 30px/42px 600 |
| Letter spacing | 0.33px |
| Colour | #f5f5f0 |
| Text node | a.Link_link__58k5P: Pie Body 30px/42px 600, #f5f5f0, ls 0.33px |
| Transition | none |
| How | resting state |

Crops: `section-heading-default.png`.

### Terminal page

#### cli-install-select

Install tool selector. A package-manager pill in the CLI install picker (InstallationSelect_tool: apt / brew / choco…).

Page: /cli. Selector: `[class*="InstallationSelect_tool"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 54.73 x 21 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 0px |
| Font | Pie Monospace 15px/21px 400 | = | = |
| Letter spacing | 0.18px | = | = |
| Colour | #a1b8f2 | #73dc8c | #73dc8c |
| Text node | strong: Pie Monospace 15px/21px 600, #a1b8f2, ls 0.18px | strong: Pie Monospace 15px/21px 600, #73dc8c, ls 0.18px | strong: Pie Monospace 15px/21px 600, #73dc8c, ls 0.18px |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 12 x 10, colour #a1b8f2 | 12 x 10, colour #73dc8c | 12 x 10, colour #73dc8c |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | span.InstallationSelect_tool__G9vXs 54.7x21.0 outline 1px auto #101010 offset 0px |

Crops: `cli-install-select-default.png`, `cli-install-select-hover.png`, `cli-install-select-focus-visible.png`.

#### cli-code-block

Terminal/code block. A dark code panel with an install command and its copy button.

Page: /cli. Selector: `pre, [class*="code" i]`. States: default, light.

| Property | default | light |
|---|---|---|
| Size (w x h) | 626.23 x 39 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Pie Monospace 15px/21px 400 | = |
| Letter spacing | -0.18px | = |
| Colour | #f5f5f0 | #1e1919 |
| Text node | span.token.prompt: Pie Monospace 15px/21px 400, #fa9bfa, ls -0.18px | = |
| Transition | none | = |
| How | resting state | same element after the footer's own LIGHT MODE radio repaints html.light (the site boots html.dark, so light is the switched state) |

Crops: `cli-code-block-default.png`, `cli-code-block-light.png`.

#### copy-button

Copy button. The CopyButton beside an install command — pressed only with forcePseudoState.

Page: /cli. Selector: `[class*="CopyButton_button"], button[aria-label*="copy" i]`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 28 x 24 | = | - |
| Padding | 0px | = | - |
| Border | none | = | - |
| Radius | 0px | = | - |
| Background | transparent | = | - |
| Box shadow | none | = | - |
| Outline | none | = | - |
| Font | Pie Body 16px/24px 400 | = | - |
| Letter spacing | 0.176px | = | - |
| Colour | #f5f5f0 | = | - |
| Text node | p.Text_base__4755h.Text_smallBody__zKyrD: Pie Body 13px/18.2px 300, #1e1919, ls 0.143px | = | - |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | - |
| Icon | 14 x 18.11, colour #d1d1cf | = | - |
| Painted layers | div.Tooltip_tooltip__MB_31.CopyButton_tooltip__SPsgL 60.0x26.2 bg #b5b5b2 r 5px; div::before.Tooltip_tooltip__MB_31.CopyButton_tooltip__SPsgL 20pxx8px border R:10px solid / B:8px solid / L:10px solid; div::after.Tooltip_tooltip__MB_31.CopyButton_tooltip__SPsgL 16pxx8px border R:8px solid / B:8px solid / L:8px solid | = | - |
| How | resting state | mouse hover over the element | - |
| Error | - | = | cdpSession.send: Protocol error (DOM.getNodeForLocation): No node found at given location |

Crops: `copy-button-default.png`, `copy-button-hover.png`.

### Blog

#### post-card

Post preview card. A changelog post row on the blog index (PostPreview_post): title, excerpt, meta.

Page: /blog. Selector: `[class*="PostPreview_post"], article, li`. States: default, light.

| Property | default | light |
|---|---|---|
| Size (w x h) | 653 x 398.2 | = |
| Padding | 64px 0px 72px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Pie Body 16px/24px 400 | = |
| Letter spacing | 0.176px | = |
| Colour | #f5f5f0 | #1e1919 |
| Text node | span.Text_base__4755h.Text_smallCaption__bYTBX: Pie Body 12px/16.8px 400, #f5f5f0, ls 0.132px | span.Text_base__4755h.Text_smallCaption__bYTBX: Pie Body 12px/16.8px 400, #1e1919, ls 0.132px |
| Transition | none | = |
| Painted layers | button.Button_button__mg_cR.Button_secondary__kYMEY 180.0x51.0 bg #f5f5f0 border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px | button.Button_button__mg_cR.Button_secondary__kYMEY 180.0x51.0 bg #1e1919 border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px |
| How | resting state | same element after the footer's own LIGHT MODE radio repaints html.light (the site boots html.dark, so light is the switched state) |

Crops: `post-card-default.png`, `post-card-light.png`.

#### post-title-link

Post title link. The post's title inside an index card.

Page: /blog. Selector: `[class*="PostPreview"] a, main a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 628.88 x 72 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Pie Body 30px/42px 600 | = |
| Letter spacing | 0.33px | = |
| Colour | #f5f5f0 | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| How | resting state | mouse hover over the element |

Crops: `post-title-link-default.png`, `post-title-link-hover.png`.

### Prose

#### prose-h1

Article title (h1). The changelog post title.

Page: /blog/changelog-0027. Selector: `main h1`. States: default, light.

| Property | default | light |
|---|---|---|
| Size (w x h) | 653 x 84 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Pie Body 30px/42px 600 | = |
| Letter spacing | 0.33px | = |
| Colour | #f5f5f0 | #1e1919 |
| Transition | none | = |
| How | resting state | same element after the footer's own LIGHT MODE radio repaints html.light (the site boots html.dark, so light is the switched state) |

Crops: `prose-h1-default.png`.

#### prose-p

Body paragraph. A paragraph of article prose.

Page: /blog/changelog-0027. Selector: `main p (sentence)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 653 x 75.61 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Pie Body 18px/25.2px 300 |
| Letter spacing | 0.198px |
| Colour | #ededeb |
| Transition | none |
| How | resting state |

Crops: `prose-p-default.png`.

#### prose-link

Prose link. A body-text link inside the article.

Page: /blog/changelog-0027. Selector: `main p a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 68.39 x 30 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Pie Body 18px/30px 400 | = |
| Letter spacing | 0.198px | = |
| Colour | #f5f5f0 | #73dc8c |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| How | resting state | mouse hover over the element |

Crops: `prose-link-default.png`, `prose-link-hover.png`.

#### prose-code

Inline code. An inline code span in prose.

Page: /blog/changelog-0027. Selector: `main p code`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 75.27 x 25 |
| Padding | 1px 5px 1px 4px |
| Border | 1px solid #4f4d4d |
| Radius | 4px |
| Background | #363636 |
| Box shadow | none |
| Outline | none |
| Font | Pie Monospace 15px/21px 300 |
| Letter spacing | 0.18px |
| Colour | #f5f5f0 |
| Transition | none |
| Painted layers | code.CodeInline_wrapper__1mNHX.MarkdownTags_code__OOnn0 75.3x25.0 bg #363636 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px |
| How | resting state |

Crops: `prose-code-default.png`.

#### prose-pre

Code block. A fenced code block in the article (syntax-tinted).

Page: /blog/changelog-0027. Selector: `main pre`. States: .

Not found on the page at capture time.

### Docs

#### docs-toc

Docs table of contents. The right-rail "On this page" TOC aside on a docs page.

Page: /docs/desktop. Selector: `aside[class*="DocsPage_tableOfContents"]`. States: default, light.

| Property | default | light |
|---|---|---|
| Size (w x h) | 314.5 x 770 | = |
| Padding | 0px 0px 60px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Pie Body 16px/24px 400 | = |
| Letter spacing | 0.176px | = |
| Colour | #f5f5f0 | #1e1919 |
| Text node | div.Text_base__4755h.Text_smallBody__zKyrD: Pie Body 15px/32px 700, #f5f5f0, ls 0.165px | div.Text_base__4755h.Text_smallBody__zKyrD: Pie Body 15px/32px 700, #1e1919, ls 0.165px |
| Transition | none | = |
| How | resting state | same element after the footer's own LIGHT MODE radio repaints html.light (the site boots html.dark, so light is the switched state) |

Crops: `docs-toc-default.png`, `docs-toc-light.png`.

#### docs-side-link

Docs nav section link. A section link in the docs left nav ("Request method").

Page: /docs/desktop. Selector: `main a, [class*="Docs"] a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 271.98 x 33 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Pie Body 32px/44.8px 600 | = |
| Letter spacing | 0.352px | = |
| Colour | #f5f5f0 | = |
| Transition | none | = |
| Cursor | pointer | = |
| ::before | 23.3594px x 44.7969px, absolute, bg #000000 @ 0, radius 0px | = |
| How | resting state | mouse hover over the element |

Crops: `docs-side-link-default.png`, `docs-side-link-hover.png`.

#### docs-code-block

Docs code block. A fenced code block inside the docs article pane — the surface the code-* syntax palette paints (the captured changelog post carries no fenced block, so this is the package's syntax-block evidence).

Page: /docs/desktop. Selector: `pre, [class*="code" i] pre`. States: default, light.

| Property | default | light |
|---|---|---|
| Size (w x h) | 745.5 x 48 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Pie Monospace 16px/24px 400 | = |
| Letter spacing | 0.192px | = |
| Colour | #f5f5f0 | #1e1919 |
| Text node | span: Pie Body 15px/21px 400, #fa9bfa, ls -0.18px | = |
| Transition | none | = |
| Ancestor paint | 1 up div.CodeBlock_block__zmBzF bg #363636 | 1 up div.CodeBlock_block__zmBzF bg #ededeb |
| How | resting state | same element after the footer's own LIGHT MODE radio repaints html.light (the site boots html.dark, so light is the switched state) |

Crops: `docs-code-block-default.png`, `docs-code-block-light.png`.

#### docs-inline-code

Docs inline code. An inline code span inside the docs article pane.

Page: /docs/desktop. Selector: `code`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 167.06 x 25 |
| Padding | 1px 5px 1px 4px |
| Border | 1px solid #4f4d4d |
| Radius | 4px |
| Background | #363636 |
| Box shadow | none |
| Outline | none |
| Font | Pie Monospace 15px/21px 300 |
| Letter spacing | 0.18px |
| Colour | #f5f5f0 |
| Transition | none |
| Painted layers | code.CodeInline_wrapper__1mNHX.MarkdownTags_code__OOnn0 167.1x25.0 bg #363636 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px |
| How | resting state |

Crops: `docs-inline-code-default.png`.

### App shell

#### app-sidebar

App sidebar. The left rail (Layout_sidebar): space switcher, Collection/Drafts/Environments panel.

Page: /app. Selector: `aside[class*="Layout_sidebar"]`. States: default, light.

| Property | default | light |
|---|---|---|
| Size (w x h) | 49 x 900 | = |
| Padding | 0px | = |
| Border | T: none; R: 1px solid #ffffff @ 0.04; B: none; L: none | T: none; R: 1px solid #000000 @ 0.06; B: none; L: none |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | PolySans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #f5f5f0 | #1c1818 |
| Transition | none | = |
| Icon | 30 x 32, colour #73dc8c | 30 x 32, colour #52ab66 |
| Painted layers | aside.Layout_sidebar__OHKsB 49.0x900.0 border R:1px solid; span.Layout_logoLink__fn7pT 32.0x48.0 outline 2px solid #000000 @ 0 offset 2px; button.MenuItem_button__lVvmy.mt-1 32.0x32.0 bg #ffffff @ 0.06 r 8px; hr.m-1.border-t 24.0x1.0 border T:1px solid | aside.Layout_sidebar__OHKsB 49.0x900.0 border R:1px solid; span.Layout_logoLink__fn7pT 32.0x48.0 outline 2px solid #000000 @ 0 offset 2px; button.MenuItem_button__lVvmy.mt-1 32.0x32.0 bg #000000 @ 0.06 r 8px; hr.m-1.border-t 24.0x1.0 border T:1px solid |
| Ancestor paint | 1 up div.Layout_container__7m_2v.Layout_withSidePanel__GJ5j7 bg #191515 | 1 up div.Layout_container__7m_2v.Layout_withSidePanel__GJ5j7 bg #edede8 |
| How | resting state | same element after the footer's own LIGHT MODE radio repaints html.light (the site boots html.dark, so light is the switched state) |

Crops: `app-sidebar-default.png`, `app-sidebar-light.png`.

#### app-space-button

"Incognito space" button. The space switcher button. "opened" is its own press opening the current space's tab (variables/settings) in the strip — no dropdown menu paints for the unsigned product.

Page: /app. Selector: `button (text Incognito space)`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 109 x 24 | = | 1042.5 x 900 |
| Padding | 0px 0px 0px 6px | = | 0px 8px |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | PolySans 14.2px/24px 400 | = | PolySans 16px/24px 400 |
| Letter spacing | normal | = | = |
| Colour | #f5f5f0 @ 0.6 | = | #f5f5f0 |
| Transition | none | = | = |
| Cursor | default | = | - |
| How | resting state | mouse hover over the element | the "Incognito space" switcher's own press (the current space's tab — variables/settings — opens in the strip) |
| Text node | - | = | span.font-ui-secondary.text-left: PolySans 12.8px/16px 400, #f5f5f0 |
| Icon | - | = | 16 x 16, colour #7d7d7d |
| Painted layers | - | = | div::before.Container_container__Dzv7w.Tabs_tabsScrollableContainer__YxAiG 32pxx28px image linear-gradient(90deg, #191515 0px, #191515 @ 0 100%); div::after.Container_container__Dzv7w.Tabs_tabsScrollableContainer__YxAiG 32pxx28px image linear-gradient(270deg, #191515 0px, #191515 @ 0 100%); div.TabCard_tab__0R39Q.Tab_tab__eWtGS 152.0x28.0 bg #201c1c r 6px outline 2px solid #000000 @ 0 offset 2px; div.EntityIcon_substrate__eAQqs.group-hover:bg-code-gray 20.0x20.0 bg #7d7d7d border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; span.Tabs_buttonSeparator__zk7D_.flex-shrink-0 1.0x28.0 border L:1px solid; div.TabHeadingRow_container__UR_wt.TabHeadingRow_editable__FhyxA 1026.5x44.0 bg #1c1818 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.02 0px 0px 0px 1px |

Crops: `app-space-button-default.png`, `app-space-button-hover.png`, `app-space-button-opened.png`.

#### app-drafts-tab

"Drafts" shelf header. The Drafts collection header in the sidebar panel — the unsaved-requests shelf.

Page: /app. Selector: `button (text Drafts)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 291.5 x 24 | 249.5 x 24 |
| Padding | 0px 6px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | PolySans 14.2px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #f5f5f0 | = |
| Transition | none | = |
| Cursor | default | = |
| How | resting state | mouse hover over the element |
| Ancestor paint | - | 1 up div.CollectionList_titleContainer__GhtcW bg #ffffff @ 0.03 |

Crops: `app-drafts-tab-default.png`, `app-drafts-tab-hover.png`.

#### app-env-button

"Environments" selector. The Environments button in the tab bar — opens the environments manager panel.

Page: /app. Selector: `button[class*="Tabs_environmentSelector"], button (text Environments)`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 111 x 28 | = | 152 x 24 |
| Padding | 4px 8px | = | 0px 6px |
| Border | none | = | = |
| Radius | 6px | = | 4px |
| Background | transparent | #ffffff @ 0.03 | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | PolySans 12.8px/16px 400 | = | PolySans 16px/24px 400 |
| Letter spacing | normal | = | = |
| Colour | #f5f5f0 @ 0.6 | = | #f5f5f0 |
| Text node | span.Button_text__HlyT_: PolySans 12.8px/16px 400, #f5f5f0 @ 0.6 | = | div.font-code-main.text-left: PolySans 14.2px/24px 400, #f5f5f0 |
| Transition | none | = | = |
| Cursor | default | = | = |
| Icon | 16 x 16, colour #7d7d7d | = | - |
| How | resting state | mouse hover over the element | the "Environments" button's own press (the manager panel open; Collection pressed to restore) |
| Painted layers | - | button.Tabs_environmentSelector__eZ3hx.Button_button__oR2Kf 111.0x28.0 bg #ffffff @ 0.03 r 6px | div.AdornmentableTextControl_container__h_T_O.MultilineInput_container__pe_B3 152.0x24.0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Gap | - | = | 4px |

Crops: `app-env-button-default.png`, `app-env-button-hover.png`, `app-env-button-opened.png`.

#### app-drafts-empty

Drafts empty state. The InfoBlock inside the Drafts shelf: "Drafts are your unsaved requests. Organize the ones you want to keep in a collection" — the signed-out draft list is empty.

Page: /app. Selector: `[class*="InfoBlock_container"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 323.5 x 52 |
| Padding | 8px |
| Border | 2px solid #ffffff @ 0.04 |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PolySans 12.8px/16px 400 |
| Letter spacing | normal |
| Colour | #f5f5f0 @ 0.6 |
| Transition | none |
| Painted layers | span.font-ui-secondary.text-left 323.5x52.0 border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 8px |
| How | resting state |

Crops: `app-drafts-empty-default.png`.

### Request builder

#### app-request-tab

Request tab card. The "GET untitled" draft tab (TabCard_tab, Tab_isActive) in the tab strip.

Page: /app. Selector: `[class*="TabCard_tab"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 104 x 28 | = |
| Padding | 4px 2px 4px 4px | = |
| Border | none | = |
| Radius | 6px | = |
| Background | #201c1c | = |
| Box shadow | none | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = |
| Font | PolySans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #f5f5f0 | = |
| Text node | span.font-code-micro.text-left: PolySansMono 8.5px/16px 400, #73dc8c | = |
| Transition | none | = |
| Cursor | default | = |
| Icon | 12 x 12, colour #f5f5f0 @ 0.6 | = |
| Painted layers | div.TabCard_tab__0R39Q.Tab_tab__eWtGS 104.0x28.0 bg #201c1c r 6px outline 2px solid #000000 @ 0 offset 2px | = |
| How | resting state | mouse hover over the element |

Crops: `app-request-tab-default.png`, `app-request-tab-hover.png`.

#### app-method-button

Method select (GET). The method dropdown button on the request line. "opened" is its own press painting the GET/HEAD/POST/… menu — closed with Escape.

Page: /app. Selector: `button (text GET)`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 53 x 28 | = | 140 x 249 |
| Padding | 2px 6px 2px 8px | = | 0px |
| Border | none | = | = |
| Radius | 6px | = | 0px |
| Background | transparent | #ffffff @ 0.03 | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | PolySansMono 14.2px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #73dc8c | = | #f5f5f0 |
| Text node | span.Button_text__HlyT_: PolySansMono 14.2px/24px 400, #73dc8c | = | span.text-code-green: PolySans 14.2px/24px 400, #73dc8c |
| Transition | none | = | = |
| Cursor | default | = | - |
| Icon | 12 x 12, colour #73dc8c | = | 16 x 16, colour #f5f5f0 |
| Ancestor paint | 2 up div.TabHeadingRow_container__UR_wt.TabHeadingRow_editable__FhyxA bg #1c1818 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.02 0px 0px 0px 1px | 2 up div.TabHeadingRow_container__UR_wt.TabHeadingRow_editable__FhyxA bg #1e1a1a shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.02 0px 0px 0px 1px | 2 up div.Substrate_substrate__jjBcc.Dropdown_container__JJM8m bg #292424 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.04 0px 0px 0px 1px inset, #000000 @ 0.5 0px 8px 40px 0px, #000000 @ 0.5 0px 0px 2px 0px |
| How | resting state | mouse hover over the element | the method button's own press (GET/HEAD/POST/PUT/PATCH/DELETE/OPTIONS/Custom menu open; Escape restores) |
| Painted layers | - | button.MethodSelector_methodSelect__Jr_wh.MethodSelector_methodSelectText__uMHa5 53.0x28.0 bg #ffffff @ 0.03 r 6px | button.DropdownItemButton_button___Abfj.DropdownItemButton_selected__Uq5_o 140.0x28.0 bg #ffffff @ 0.06 r 6px outline 2px solid #000000 @ 0 offset 2px; button.DropdownItemButton_button___Abfj.DropdownItemButton_withCheckmark__YxXws 140.0x28.0 r 6px outline 2px solid #000000 @ 0 offset 2px; button.DropdownItemButton_button___Abfj.DropdownItemButton_withCheckmark__YxXws 140.0x28.0 r 6px outline 2px solid #000000 @ 0 offset 2px; button.DropdownItemButton_button___Abfj.DropdownItemButton_withCheckmark__YxXws 140.0x28.0 r 6px outline 2px solid #000000 @ 0 offset 2px; button.DropdownItemButton_button___Abfj.DropdownItemButton_withCheckmark__YxXws 140.0x28.0 r 6px outline 2px solid #000000 @ 0 offset 2px; button.DropdownItemButton_button___Abfj.DropdownItemButton_withCheckmark__YxXws 140.0x28.0 r 6px outline 2px solid #000000 @ 0 offset 2px |
| Gap | - | = | 2px |

Crops: `app-method-button-default.png`, `app-method-button-hover.png`, `app-method-button-opened.png`.

#### app-url-field

URL field. The request URL editor (UrlBar, a CodeMirror single-line field) holding the prefilled httpie.io/hello.

Page: /app. Selector: `[class*="UrlBar_urlTextareaContainer"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 848.5 x 44 | = |
| Padding | 8px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | PolySans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #f5f5f0 | = |
| Text node | span.cm-placeholder: PolySansMono 14.2px/24px 400, #f5f5f0 @ 0.35 | = |
| Transition | none | = |
| Painted layers | div.cm-cursor.cm-cursor-primary 0.0x0.0 border L:1px solid | div.cm-cursor.cm-cursor-primary 1.0x14.0 border L:1px solid |
| Ancestor paint | 1 up div.TabHeadingRow_container__UR_wt.TabHeadingRow_editable__FhyxA bg #1c1818 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.02 0px 0px 0px 1px | 1 up div.TabHeadingRow_container__UR_wt.TabHeadingRow_editable__FhyxA bg #201c1c shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.02 0px 0px 0px 1px |
| How | resting state | the field clicked into |

Crops: `app-url-field-default.png`, `app-url-field-focused.png`.

#### app-send-button

"Send" button. The request's primary action — measured at rest and with forcePseudoState only; a real press would issue a network request, so it is never fired.

Page: /app. Selector: `button (text Send)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 57 x 28 | = | = | = |
| Padding | 2px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #73dc8c | #a1e8b0 | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset, #000000 @ 0.25 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b5eba 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | PolySans 14.2px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1c1818 | = | = | = |
| Text node | span.Button_text__HlyT_: PolySans 14.2px/24px 400, #1c1818 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | button.SubmitButton_sendButton__ZpsRE.Button_button__oR2Kf 57.0x28.0 bg #73dc8c r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset, #000000 @ 0.25 0px 1px 2px 0px | button.SubmitButton_sendButton__ZpsRE.Button_button__oR2Kf 57.0x28.0 bg #a1e8b0 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset, #000000 @ 0.25 0px 1px 2px 0px | button.SubmitButton_sendButton__ZpsRE.Button_button__oR2Kf 57.0x28.0 bg #73dc8c r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b5eba 0px 0px 0px 2px outline 2px solid #000000 @ 0 offset 2px | = |
| Ancestor paint | 2 up div.TabHeadingRow_container__UR_wt.TabHeadingRow_editable__FhyxA bg #1c1818 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.02 0px 0px 0px 1px | 2 up div.TabHeadingRow_container__UR_wt.TabHeadingRow_editable__FhyxA bg #1e1a1a shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.02 0px 0px 0px 1px | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `app-send-button-default.png`, `app-send-button-hover.png`, `app-send-button-focus-visible.png`, `app-send-button-pressed.png`.

#### app-panel-tabs

Request panel tablist. The Params / Headers / Auth / Body tablist (PanelTabs) above the request editor.

Page: /app. Selector: `[class*="PanelTabs_container"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 237 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PolySans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f5f5f0 |
| Text node | span.Button_text__HlyT_: PolySans 14.2px/24px 400, #f5f5f0 |
| Transition | none |
| Painted layers | button.PanelTabButton_button__iYu6s.PanelTabs_aloneActiveTab___1VKK 64.0x28.0 bg #ffffff @ 0.06 r 6px |
| How | resting state |

Crops: `app-panel-tabs-default.png`.

#### app-panel-tab

Request panel tab. One request panel tab ("Headers"). "selected" is its own activation — a local UI toggle.

Page: /app. Selector: `button[class*="PanelTabButton"]`. States: default, hover, selected.

| Property | default | hover | selected |
|---|---|---|---|
| Size (w x h) | 70 x 28 | = | = |
| Padding | 2px 8px | = | = |
| Border | none | = | = |
| Radius | 6px | = | = |
| Background | transparent | #ffffff @ 0.03 | #ffffff @ 0.06 |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px |
| Font | PolySans 14.2px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #f5f5f0 @ 0.6 | = | #f5f5f0 |
| Text node | span.Button_text__HlyT_: PolySans 14.2px/24px 400, #f5f5f0 @ 0.6 | = | span.Button_text__HlyT_: PolySans 14.2px/24px 400, #f5f5f0 |
| Transition | none | = | = |
| Cursor | default | = | = |
| How | resting state | mouse hover over the element | the tab's own activation |
| Painted layers | - | button.PanelTabButton_button__iYu6s.PanelTabs_aloneActiveTab___1VKK 70.0x28.0 bg #ffffff @ 0.03 r 6px | button.PanelTabButton_button__iYu6s.PanelTabs_aloneActiveTab___1VKK 70.0x28.0 bg #ffffff @ 0.06 r 6px outline 2px solid #000000 @ 0 offset 2px |

Crops: `app-panel-tab-default.png`, `app-panel-tab-hover.png`, `app-panel-tab-selected.png`.

#### app-param-checkbox

Param row checkbox. The enable checkbox on a params row — the painted box is Checkbox_container; the real input is a hidden 1px control.

Page: /app. Selector: `[class*="Checkbox_container"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 16 x 16 |
| Padding | 0px |
| Border | 1px solid #ffffff @ 0.04 |
| Radius | 4px |
| Background | transparent |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | PolySans 16px/12px 400 |
| Letter spacing | normal |
| Colour | #f5f5f0 |
| Transition | none |
| Cursor | default |
| Painted layers | div.Checkbox_container__NK4I_ 16.0x16.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | resting state |

Crops: `app-param-checkbox-default.png`.

#### app-response-empty

Response empty state. The response panel before any send ("Not sent" — the send surface is never fired, so this resting panel is the honest evidence).

Page: /app. Selector: `[class*="PanelState_container"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 599.3 x 712 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PolySans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f5f5f0 |
| Text node | p.font-ui-main.text-center: PolySans 14.2px/24px 400, #f5f5f0 @ 0.6 |
| Transition | none |
| Icon | 48 x 48, colour #f5f5f0 @ 0.6 |
| Painted layers | div.PanelState_iconCircle__DPIoa.mb-2 64.0x64.0 bg #ffffff @ 0.04 r 9999px |
| How | resting state |

Crops: `app-response-empty-default.png`.

#### app-auth-tab

Auth panel (opened). The Auth tab's panel: the "No authentication" select with None / Basic auth / Bearer token / API key options. The tab's own press opens it.

Page: /app. Selector: `button[class*="PanelTabButton"] (Auth) -> panel`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 118 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PolySans 14.2px/24px 400 |
| Letter spacing | normal |
| Colour | #f5f5f0 @ 0.6 |
| Transition | none |
| Cursor | default |
| How | resting state |

Crops: `app-auth-tab-opened.png`.

#### app-body-tab

Body panel (opened). The Body tab's panel: the body-type select (None / Text / Form / File / GraphQL).

Page: /app. Selector: `button[class*="PanelTabButton"] (Body) -> panel`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 53 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PolySans 14.2px/24px 400 |
| Letter spacing | normal |
| Colour | #f5f5f0 @ 0.6 |
| Transition | none |
| Cursor | default |
| How | resting state |

Crops: `app-body-tab-opened.png`.

#### app-auth-select

Auth type select. The "None" auth-type control inside the opened Auth panel — measured, its menu never opened.

Page: /app. Selector: `select or button (auth type)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 74 x 24 | = |
| Padding | 4px 8px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | #ffffff @ 0.04 | #ffffff @ 0.06 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.02 0px 0px 0px 1px inset, #000000 @ 0.25 0px 1px 2px 0px | = |
| Outline | none | = |
| Font | PolySans 12.8px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #f5f5f0 @ 0.6 | = |
| Text node | span.Button_text__HlyT_: PolySans 12.8px/16px 400, #f5f5f0 @ 0.6 | = |
| Transition | none | = |
| Cursor | default | = |
| Icon | 16 x 16, colour #f5f5f0 @ 0.6 | = |
| Painted layers | button.Select_trigger__zMG_1.Button_button__oR2Kf 74.0x24.0 bg #ffffff @ 0.04 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.02 0px 0px 0px 1px inset, #000000 @ 0.25 0px 1px 2px 0px | button.Select_trigger__zMG_1.Button_button__oR2Kf 74.0x24.0 bg #ffffff @ 0.06 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.02 0px 0px 0px 1px inset, #000000 @ 0.25 0px 1px 2px 0px |
| How | resting state | mouse hover over the element |

Crops: `app-auth-select-default.png`, `app-auth-select-hover.png`.

### Environments

#### app-env-panel

Environments manager. The environments manager (Variables / Settings / Defaults tabs, "Create environment"), opened by the Environments selector's own press.

Page: /app. Selector: `[class*="SpaceTab_panel"], [class*="PanelContainer_container"]`. States: opened, light.

| Property | opened | light |
|---|---|---|
| Size (w x h) | 1026.5 x 796 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #1c1818 | #f5f5f0 |
| Box shadow | none | = |
| Outline | none | = |
| Font | PolySans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #f5f5f0 | #1c1818 |
| Text node | span.Button_text__HlyT_: PolySans 14.2px/24px 400, #f5f5f0 | span.Button_text__HlyT_: PolySans 14.2px/24px 400, #1c1818 |
| Transition | none | = |
| Icon | 16 x 16, colour #f5f5f0 @ 0.6 | 16 x 16, colour #1c1818 @ 0.6 |
| Painted layers | div.SpaceTab_panel__LJTwp.Panel_type_form__fn2h9 1026.5x796.0 bg #1c1818; button.PanelTabButton_button__iYu6s.PanelTabs_aloneActiveTab___1VKK 74.0x28.0 bg #ffffff @ 0.06 r 6px; th.VariablesTable_cell__rDhQm.VariablesTable_isHeader___CzuK 200.0x36.0 bg #1c1818 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.04 1px 0px 0px 0px; th::before.VariablesTable_cell__rDhQm.VariablesTable_isHeader___CzuK 16pxx38px bg #1c1818; th::after.VariablesTable_cell__rDhQm.VariablesTable_isHeader___CzuK 8pxx36px bg #1c1818 r 8px 0px 0px 8px; th.VariablesTable_cell__rDhQm.VariablesTable_isDefaultEnv__uOQBX 200.0x36.0 bg #231f19 | div.SpaceTab_panel__LJTwp.Panel_type_form__fn2h9 1026.5x796.0 bg #f5f5f0; button.PanelTabButton_button__iYu6s.PanelTabs_aloneActiveTab___1VKK 74.0x28.0 bg #000000 @ 0.06 r 6px; th.VariablesTable_cell__rDhQm.VariablesTable_isHeader___CzuK 200.0x36.0 bg #f5f5f0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 1px 0px 0px 0px; th::before.VariablesTable_cell__rDhQm.VariablesTable_isHeader___CzuK 16pxx38px bg #f5f5f0; th::after.VariablesTable_cell__rDhQm.VariablesTable_isHeader___CzuK 8pxx36px bg #f5f5f0 r 8px 0px 0px 8px; th.VariablesTable_cell__rDhQm.VariablesTable_isDefaultEnv__uOQBX 200.0x36.0 bg #efefdc |
| Ancestor paint | 1 up div.Panel_panelSet__1cv0n.SpaceTab_container__8k9ae bg #1c1818 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.02 0px 0px 0px 1px | 1 up div.Panel_panelSet__1cv0n.SpaceTab_container__8k9ae bg #f5f5f0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.02 0px 0px 0px 1px |
| How | resting state | same element after the footer's own LIGHT MODE radio repaints html.light (the site boots html.dark, so light is the switched state) |

Crops: `app-env-panel-opened.png`, `app-env-panel-light.png`.

#### app-env-create

"Create environment" button. The environments manager's primary action — measured, never pressed.

Page: /app. Selector: `button (text Create environment)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 147 x 24 | = |
| Padding | 4px 8px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | transparent | #ffffff @ 0.03 |
| Box shadow | none | = |
| Outline | none | = |
| Font | PolySans 12.8px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #f5f5f0 @ 0.6 | = |
| Text node | span.Button_text__HlyT_: PolySans 12.8px/16px 400, #f5f5f0 @ 0.6 | = |
| Transition | none | = |
| Cursor | default | = |
| Icon | 16 x 16, colour #f5f5f0 @ 0.6 | = |
| How | resting state | mouse hover over the element |
| Painted layers | - | button.Button_button__oR2Kf.Button_kind_ghost__NkouH 147.0x24.0 bg #ffffff @ 0.03 r 4px |

Crops: `app-env-create-default.png`, `app-env-create-hover.png`.

### Site chrome (mobile)

#### m-nav

Mobile nav. The nav at 390px (links wrap; no hamburger).

Page: /. Selector: `nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 85 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Pie Body 16px/24px 400 |
| Letter spacing | 0.176px |
| Colour | #f5f5f0 |
| Transition | none |
| Icon | 0 x 0, colour #f5f5f0 |
| Painted layers | span.Count_count__p9ULf.Navigation_count__CXLW6 0.0x0.0 bg #363636 r 9999px; button.Button_button__mg_cR.Button_primary__PFIP8 0.0x0.0 bg #73dc8c border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 9999px; div.Navigation_featuredIconCircle__n4aZN 45.0x45.0 bg #363636 r 9999px |
| How | resting state |

Crops: `m-nav-default.png`.

## Transitions declared in the readable stylesheets

httpie.io serves its own CSS same-origin (/_next/static/css), so this list is the site's own transition declarations the CSSOM could read on each page.

- /: `color 0.3s, background-color 0.3s`, `0.15s`, `0.3s cubic-bezier(0.75, -0.02, 0.2, 0.97)`

- /app: `background-color 0.3s ease-in, border-color 0.5s ease-in`

- /blog: `color 0.3s, background-color 0.3s`, `0.15s`

- /blog/changelog-0027: `color 0.3s, background-color 0.3s`, `0.15s`

- /cli: `color 0.3s, background-color 0.3s`, `0.15s`

- /docs/desktop: `color 0.3s, background-color 0.3s`, `0.15s`
