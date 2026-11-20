# Component measurements

Computed styles read from lumalabs.ai on 2026-11-18 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Marketing shell

#### nav-product

Nav link. The PRODUCT nav link. It points at /app, a marketing route, not the signed-in app. Uppercase Graphik label.

Page: home. Selector: `a[href="/app"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 67.48 x 14 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #005fcc offset 4px |
| Font | __graphik_7126cf 14px/14px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | a.typo-label.tracking-normal 67.5x14.0 outline 1px auto #005fcc offset 4px |

Crops: `nav-product-default.png`, `nav-product-hover.png`, `nav-product-focus-visible.png`.

#### nav-signin

Sign In. The header Sign In pill. It links to app.lumalabs.ai, which redirects to the sign-up host. Measured, never followed.

Page: home. Selector: `a Sign In`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 69.41 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff | = | = | #d9d9d9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 4px | = |
| Font | __graphik_7126cf 14px/20px 500 | = | = | = |
| Letter spacing | -0.4px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.items-center 69.4x32.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | = | a.flex.items-center 69.4x32.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px outline 1px auto #005fcc offset 4px | a.flex.items-center 69.4x32.0 bg #d9d9d9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### footer-link

Footer link. A footer text link.

Page: home. Selector: `footer a Pricing`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 42.88 x 18 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | __graphik_7126cf 14px/24px 400 | = |
| Letter spacing | -0.4px | = |
| Colour | #000000 | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Opacity | 0.7 | - |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`.

### Home

#### hero-h1

Hero heading. The home hero heading.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 576 x 124.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __graphik_7126cf 52px/62.4px 500 |
| Letter spacing | -2.08px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-cta

Try for free. The hero pill. Links to the app host. Measured, never followed. Following it is a sign-in.

Page: home. Selector: `Try for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 155.39 x 48 | = | = | = |
| Padding | 0px 32px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff | #d9d9d9 | = | #d9d9d9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 4px | = |
| Font | __graphik_7126cf 18px/28px 500 | = | = | = |
| Letter spacing | -0.4px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.items-center 155.4x48.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | a.flex.items-center 155.4x48.0 bg #d9d9d9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | a.flex.items-center 155.4x48.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px outline 1px auto #005fcc offset 4px | a.flex.items-center 155.4x48.0 bg #d9d9d9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### prompt

Prompt field. The home prompt. Sample text is typed and deleted. Submit is never pressed.

Page: home. Selector: `textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 510 x 75.56 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | __graphik_7126cf 18px/25.2px 400 | = | = |
| Letter spacing | -0.54px | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000, opacity 1 | = | = |
| Ancestor paint | 1 up form.relative.rounded-xl bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px; 2 up div.flex.min-h-72 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px outline 1px solid #000000 @ 0.2 | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `prompt-default.png`, `prompt-focused.png`, `prompt-filled.png`.

#### prompt-submit

Submit prompt. The prompt submit control. Measured at rest and hover only. Never clicked, so no generation is started.

Page: home. Selector: `button[aria-label=Submit prompt]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 44 x 44 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | __graphik_7126cf 16px/24px 400 | = |
| Letter spacing | -0.4px | = |
| Colour | #ffffff | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 44 x 44, colour #a6a6a6 | = |
| Ancestor paint | 1 up form.relative.rounded-xl bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px; 2 up div.flex.min-h-72 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px outline 1px solid #000000 @ 0.2 | = |
| How | at rest | mouse hover |
| Opacity | - | 0.7 |

Crops: `prompt-submit-default.png`, `prompt-submit-hover.png`.

#### idea-chip

Idea chip. A suggested-prompt chip. A local control. It was not used to submit a prompt.

Page: home. Selector: `Product Hero Shots`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 149.08 x 32 | = | = |
| Padding | 0px 12px | = | = |
| Border | 1px solid #000000 @ 0 | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | #ffffff | #d9d9d9 | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #005fcc offset 4px |
| Font | __graphik_7126cf 14px/20px 500 | = | = |
| Letter spacing | -0.4px | = | = |
| Colour | #000000 | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.flex.items-center 149.1x32.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | button.flex.items-center 149.1x32.0 bg #d9d9d9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | button.flex.items-center 149.1x32.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px outline 1px auto #005fcc offset 4px |
| Ancestor paint | 2 up div.flex.min-h-72 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px outline 1px solid #000000 @ 0.2 | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `idea-chip-default.png`, `idea-chip-hover.png`, `idea-chip-focus-visible.png`.

### Pricing

#### price-h1

Pricing heading. Plans and Pricing heading.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 337.59 x 62.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __graphik_7126cf 52px/62.4px 500 |
| Letter spacing | -2.08px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `price-h1-default.png`.

#### price-monthly

Monthly. The billing-interval button. A local toggle. Checkout is never opened.

Page: pricing. Selector: `Monthly`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 131.14 x 50.39 | = | = |
| Padding | 14px 36px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | __graphik_7126cf 16px/22.4px 500 | = | = |
| Letter spacing | -0.48px | = | = |
| Colour | #000000 | = | = |
| Text node | span.relative.text-inverted-primary: __graphik_7126cf 16px/22.4px 500, #ffffff, ls -0.48px | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | default | = | = |
| Painted layers | div.absolute.inset-0 131.1x50.4 bg #000000 r 3.35544e+07px | = | = |
| Ancestor paint | 1 up div.inline-flex.rounded-full bg #ffffff | = | = |
| How | at rest | mouse hover | CDP forcePseudoState :active:hover |

Crops: `price-monthly-default.png`, `price-monthly-hover.png`, `price-monthly-pressed.png`.

#### price-yearly

Yearly. The yearly interval button. A local toggle.

Page: pricing. Selector: `Yearly`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 115.69 x 50.39 | = | = |
| Padding | 14px 36px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | __graphik_7126cf 16px/22.4px 500 | = | = |
| Letter spacing | -0.48px | = | = |
| Colour | #000000 | = | = |
| Text node | span.relative.text-secondary: __graphik_7126cf 16px/22.4px 500, #737373, ls -0.48px | span.relative.text-secondary: __graphik_7126cf 16px/22.4px 500, #000000, ls -0.48px | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | default | = | = |
| Ancestor paint | 1 up div.inline-flex.rounded-full bg #ffffff | = | = |
| How | at rest | mouse hover | CDP forcePseudoState :active:hover |

Crops: `price-yearly-default.png`, `price-yearly-hover.png`, `price-yearly-pressed.png`.

#### price-cta

Start Now. A plan CTA. Measured, never followed. Following it is a sign-in and a checkout.

Page: pricing. Selector: `Start Now`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 350 x 40 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff | #f2f2f2 | = | #f2f2f2 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 4px | = |
| Font | __graphik_7126cf 16px/24px 500 | = | = | = |
| Letter spacing | -0.4px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.items-center 350.0x40.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | a.flex.items-center 350.0x40.0 bg #f2f2f2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | a.flex.items-center 350.0x40.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px outline 1px auto #005fcc offset 4px | a.flex.items-center 350.0x40.0 bg #f2f2f2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `price-cta-default.png`, `price-cta-hover.png`, `price-cta-focus-visible.png`, `price-cta-pressed.png`.

#### price-card

Plan card. The Plus plan card. Cropped from the node whose text starts with Plus and whose box is card-sized.

Page: pricing. Selector: `Plus card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 18434.06 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | __graphik_7126cf 16px/24px 400 |
| Letter spacing | -0.4px |
| Colour | #000000 |
| Text node | a.typo-label.tracking-normal: __graphik_7126cf 14px/14px 500, #000000 |
| Transition | none |
| Icon | 80 x 18, colour #000000 |
| Painted layers | body.tracking-tight 1440.0x18434.1 bg #ffffff; main.light.flex 1440.0x18434.1 bg #ffffff; div.pointer-events-none.fixed 0.0x0.0 bg #ffffff; div.h-px.w-full 1376.0x1.0 bg #000000 @ 0.3; div.fixed.top-[var(--eyebrow-offset,0px)] 0.0x0.0 bg #ffffff @ 0.8; div.h-top-nav.border-b 0.0x0.0 border B:1px solid #000000 @ 0.3 |
| Ancestor paint | 1 up html.__variable_7126cf.__variable_a83cde bg #ffffff |
| How | at rest |

Crops: none.

#### faq

FAQ row. A pricing FAQ button. A local toggle. Nothing is submitted.

Page: pricing. Selector: `FAQ`. States: .

Not found on the page at capture time.

### About

#### about-h1

About heading. The about page heading.

Page: about. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 287.97 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __graphik_7126cf 48px/57.6px 500 |
| Letter spacing | -1.92px |
| Colour | #737373 |
| Transition | none |
| Icon | 162.22 x 40, colour #000000 |
| How | at rest |

Crops: `about-h1-default.png`.

#### about-faq

About FAQ. An about FAQ button. A local toggle.

Page: about. Selector: `What is Luma?`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 830 x 62.8 | = | = |
| Padding | 16px 28px | = | = |
| Gap | 16px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | __graphik_7126cf 16px/24px 500 | = | = |
| Letter spacing | -0.4px | = | = |
| Colour | #000000 | = | = |
| Text node | span.flex-1.typo-h4: __graphik_7126cf 22px/30.8px 500, #000000, ls -0.66px | = | = |
| Transition | none | = | = |
| Cursor | default | = | = |
| Icon | 28.28 x 28.28, colour #737373 | 28.28 x 28.28, colour #000000 | 20 x 20, colour #000000 |
| How | at rest | mouse hover | own toggle |

Crops: `about-faq-default.png`, `about-faq-hover.png`, `about-faq-opened.png`.

### API

#### api-h1

API heading. Build with Luma APIs.

Page: api. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 464.42 x 62.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __graphik_7126cf 52px/62.4px 500 |
| Letter spacing | -2.6px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `api-h1-default.png`.

#### api-cta

Use the API. The API CTA. Measured, never followed. Keys and billing sit behind sign-in.

Page: api. Selector: `Use the API`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 97.81 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #000000 | #262626 | = | #262626 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 4px | = |
| Font | __graphik_7126cf 14px/20px 500 | = | = | = |
| Letter spacing | -0.4px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.items-center 97.8x32.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | a.flex.items-center 97.8x32.0 bg #262626 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | a.flex.items-center 97.8x32.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px outline 1px auto #005fcc offset 4px | a.flex.items-center 97.8x32.0 bg #262626 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `api-cta-default.png`, `api-cta-hover.png`, `api-cta-focus-visible.png`, `api-cta-pressed.png`.

#### api-tab

Model tab. A model switch on the API page. A local toggle.

Page: api. Selector: `Uni-1.1`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 94.64 x 40 | = | = |
| Padding | 0px 24px | = | = |
| Border | 1px solid #000000 @ 0 | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | #f2f2f2 | #ededed | #ededed |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | __graphik_7126cf 16px/24px 500 | = | = |
| Letter spacing | -0.4px | = | = |
| Colour | #000000 | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | default | = | = |
| Painted layers | button.flex.items-center 94.6x40.0 bg #f2f2f2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | button.flex.items-center 94.6x40.0 bg #ededed border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | button.flex.items-center 94.6x40.0 bg #ededed border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px |
| How | at rest | mouse hover | CDP forcePseudoState :active:hover |

Crops: `api-tab-default.png`, `api-tab-hover.png`, `api-tab-pressed.png`.

#### api-docs

Explore docs. The docs link. Measured, never followed from this page. Docs were captured as their own route.

Page: api. Selector: `Explore docs`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 172.41 x 48 | = | = |
| Padding | 0px 32px | = | = |
| Border | 1px solid #000000 @ 0 | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | #f2f2f2 | #ededed | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #005fcc offset 4px |
| Font | __graphik_7126cf 18px/28px 500 | = | = |
| Letter spacing | -0.4px | = | = |
| Colour | #000000 | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | a.flex.items-center 172.4x48.0 bg #f2f2f2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | a.flex.items-center 172.4x48.0 bg #ededed border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | a.flex.items-center 172.4x48.0 bg #f2f2f2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px outline 1px auto #005fcc offset 4px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `api-docs-default.png`, `api-docs-hover.png`, `api-docs-focus-visible.png`.

### Ray

#### ray-h1

Ray heading. The Ray3.2 page heading on the dark field.

Page: ray. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 767.06 x 62.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __graphik_7126cf 52px/62.4px 500 |
| Letter spacing | -2.08px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `ray-h1-default.png`.

#### ray-faq

Ray FAQ. A Ray FAQ button. A local toggle.

Page: ray. Selector: `What Is Ray3.2?`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 830 x 62.8 | = | = |
| Padding | 16px 28px | = | = |
| Gap | 16px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | __graphik_7126cf 16px/24px 500 | = | = |
| Letter spacing | -0.4px | = | = |
| Colour | #ffffff | = | = |
| Text node | span.flex-1.typo-h4: __graphik_7126cf 22px/30.8px 500, #ffffff, ls -0.66px | = | = |
| Transition | none | = | = |
| Cursor | default | = | = |
| Icon | 20 x 20, colour #8c8c8c | 20 x 20, colour #ffffff | 28.28 x 28.28, colour #ffffff |
| How | at rest | mouse hover | own toggle |

Crops: `ray-faq-default.png`, `ray-faq-hover.png`, `ray-faq-opened.png`.

### News

#### news-h1

News heading. The news index heading.

Page: news. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 127.92 x 62.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __graphik_7126cf 52px/62.4px 500 |
| Letter spacing | -2.08px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `news-h1-default.png`.

#### news-filter

News filter. A news category filter. A local toggle. Subscribe was not clicked.

Page: news. Selector: `Product`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 107.78 x 40 | = | = |
| Padding | 0px 24px | = | = |
| Border | 1px solid #000000 @ 0 | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | #f2f2f2 | #ededed | #ededed |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | __graphik_7126cf 16px/24px 500 | = | = |
| Letter spacing | -0.4px | = | = |
| Colour | #000000 | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | default | = | = |
| Painted layers | button.flex.items-center 107.8x40.0 bg #f2f2f2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | button.flex.items-center 107.8x40.0 bg #ededed border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | button.flex.items-center 107.8x40.0 bg #ededed border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px |
| How | at rest | mouse hover | CDP forcePseudoState :active:hover |

Crops: `news-filter-default.png`, `news-filter-hover.png`, `news-filter-pressed.png`.

#### news-card

News card. A published news card. A public article link.

Page: news. Selector: `news card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 253.52 x 58.8 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | __graphik_7126cf 22px/30.8px 500 | = |
| Letter spacing | -0.66px | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `news-card-default.png`, `news-card-hover.png`.

### Enterprise

#### ent-h1

Enterprise heading. The enterprise page heading.

Page: enterprise. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 832 x 124.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __graphik_7126cf 52px/62.4px 500 |
| Letter spacing | -2.08px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `ent-h1-default.png`.

#### ent-field

Enterprise field. A field on the enterprise form. Focused only. Nothing is typed that would be submitted, and Submit is never clicked.

Page: enterprise. Selector: `input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 400 x 36 | = |
| Padding | 4px 10px | = |
| Border | 1px solid oklch(0.75 0 0) | 1px solid oklch(0.708 0 0) |
| Radius | 6px | = |
| Background | transparent | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a1a1a1 @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| Outline | none | = |
| Font | __graphik_7126cf 14px/20px 400 | = |
| Letter spacing | -0.4px | = |
| Colour | #000000 | = |
| Transition | color, box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #000000, opacity 1 | = |
| Painted layers | input.h-9.w-full 400.0x36.0 border T:1px solid oklch(0.75 0 0) / R:1px solid oklch(0.75 0 0) / B:1px solid oklch(0.75 0 0) / L:1px solid oklch(0.75 0 0) r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | input.h-9.w-full 400.0x36.0 border T:1px solid oklch(0.708 0 0) / R:1px solid oklch(0.708 0 0) / B:1px solid oklch(0.708 0 0) / L:1px solid oklch(0.708 0 0) r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a1a1a1 @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | clicked into the field |

Crops: `ent-field-default.png`, `ent-field-focused.png`.

#### ent-submit

Enterprise submit. The enterprise form submit. Measured at rest and hover. Never clicked, so no sales form is sent.

Page: enterprise. Selector: `Submit`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 832 x 48 | = |
| Padding | 0px 10px | = |
| Gap | 6px | = |
| Border | 1px solid #000000 @ 0 | = |
| Radius | 3.35544e+07px | = |
| Background | #000000 | #000000 @ 0.8 |
| Box shadow | none | = |
| Outline | none | = |
| Font | __graphik_7126cf 18px/28px 500 | = |
| Letter spacing | -0.4px | = |
| Colour | oklch(0.985 0 0) | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | default | = |
| Painted layers | button.group/button.inline-flex 832.0x48.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | button.group/button.inline-flex 832.0x48.0 bg #000000 @ 0.8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px |
| How | at rest | mouse hover |

Crops: `ent-submit-default.png`, `ent-submit-hover.png`.

### Phone (390 wide)

#### m-menu

Phone menu. The mobile navigation toggle at 390px. A local control. Sign In inside it is not followed.

Page: home. Selector: `header menu button`. States: default, hover, pressed, opened.

| Property | default | hover | pressed | opened |
|---|---|---|---|---|
| Size (w x h) | 20 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | __graphik_7126cf 16px/24px 400 | = | = | = |
| Letter spacing | -0.4px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = |
| How | at rest | mouse hover | CDP forcePseudoState :active:hover | own toggle |

Crops: `m-menu-default.png`, `m-menu-hover.png`, `m-menu-pressed.png`, `m-menu-opened.png`.

#### m-h1

Phone heading. The home heading at 390px.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 76.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __graphik_7126cf 32px/38.4px 500 |
| Letter spacing | -1.28px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-h1-default.png`.

#### m-signin

Phone Sign In. Sign In at 390px. Measured, never followed.

Page: home. Selector: `Sign In`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 69.41 x 32 | = |
| Padding | 0px 12px | = |
| Border | 1px solid #000000 @ 0 | = |
| Radius | 3.35544e+07px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | __graphik_7126cf 14px/20px 500 | = |
| Letter spacing | -0.4px | = |
| Colour | #000000 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | a.flex.items-center 69.4x32.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | = |
| How | at rest | mouse hover |

Crops: `m-signin-default.png`, `m-signin-hover.png`.

## Transitions declared in the readable stylesheets

This list holds only the transitions the CSSOM could read on each page; a stylesheet it could not read is not in it. The per-state Transition rows above are computed values and cover every rule.

- home: none
