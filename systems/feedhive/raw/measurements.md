# FeedHive component measurements

Computed styles read from feedhive.com on 2026-11-15 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the light www.feedhive.com marketing pages (no user theme toggle, no dark mode) and the separate light sign-in/sign-up cards at app.feedhive.com (a Chakra-UI app that shares no token layer with the marketing site) — with any consent layer hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `selected`, `expanded` and the rest are resting states reached by the page or by a local UI toggle.

## Components

### Promo bar

#### promo-bar

Launch promo bar. The top banner ("Limited launch bonus: Double your AI credits for 3 months when you start today →"); measured, never followed.

Page: home. Selector: `launch promo banner`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1440 x 38 | = |
| Padding | 8px 16px | = |
| Border | T: none; R: none; B: 1px solid #000000 @ 0.05; L: none | = |
| Radius | 0px | = |
| Background | #f4f3f2 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/21px 600 | = |
| Letter spacing | -0.14px | = |
| Colour | #2d2f35 | = |
| Text node | span.group-hover:underline.group-hover:underline-offset-2: Inter 14px/21px 600, #2d2f35, ls -0.14px | = |
| Transition | none | = |
| Icon | 14 x 14, colour #4f5fd7 | = |
| Painted layers | div.block.border-b 1440.0x38.0 bg #f4f3f2 border B:1px solid #000000 @ 0.05 | = |
| Ancestor paint | 1 up main.min-h-screen.bg-white bg #ffffff | = |
| How | at rest | mouse hover |

Crops: `promo-bar-default.png`, `promo-bar-hover.png`.

### Site chrome

#### mkt-header

Site header. The 80px header below the promo bar: FeedHive mark, Product / Agents & Automation / Socials / Learn dropdowns, Pricing, Login and the indigo Sign Up pill.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 80 |
| Padding | 20px 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #20232b |
| Text node | span: Inter 14px/21px 500, #4f5562, ls -0.14px |
| Transition | none |
| Icon | 12 x 12, colour #4f5562 |
| Painted layers | a.inline-flex.h-10 0.0x0.0 bg #4457ff r 11px; a.inline-flex.h-10 73.6x40.0 bg #f4f2f0 r 11px; a.inline-flex.h-10 88.0x40.0 bg #4457ff r 11px |
| Ancestor paint | 1 up main.min-h-screen.bg-white bg #ffffff |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The FeedHive mark-and-wordmark in the header, linking home.

Page: home. Selector: `header a[href=/]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 118 x 30.23 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #20232b |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-dropdown

Nav dropdown trigger. The "Product" header trigger — an anchor with href="#" and aria-haspopup="true" that opens the product dropdown. The opened state was measured after clicking it.

Page: home. Selector: `header a[href="#"] Product`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 69.03 x 21 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Gap | 4px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = | = |
| Font | Inter 14px/21px 500 | = | = | = | = |
| Letter spacing | -0.14px | = | = | = | = |
| Colour | #4f5562 | #22252d | #22252d | #22252d | #22252d |
| Text node | span: Inter 14px/21px 500, #4f5562, ls -0.14px | span: Inter 14px/21px 500, #22252d, ls -0.14px | span: Inter 14px/21px 500, #22252d, ls -0.14px | span: Inter 14px/21px 500, #22252d, ls -0.14px | span: Inter 14px/21px 500, #22252d, ls -0.14px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 12 x 12, colour #4f5562 | 12 x 12, colour #22252d | 12 x 12, colour #22252d | 12 x 12, colour #22252d | 12 x 12, colour #22252d |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | a.flex.items-center 69.0x21.0 outline 1px auto #101010 offset 1px | = | = |

Crops: `nav-dropdown-default.png`, `nav-dropdown-hover.png`, `nav-dropdown-focus-visible.png`, `nav-dropdown-pressed.png`, `nav-dropdown-opened.png`.

#### nav-panel

Nav dropdown panel. The dropdown panel opened by the Product trigger; its links were never followed.

Page: home. Selector: `header dropdown panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 316 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #20232b |
| Text node | p.mb-5.text-[12px]: Inter 12px/18px 500, #8b9098, ls 2.4px |
| Transition | none |
| Icon | 20 x 20, colour #5c7cfa |
| Painted layers | div.border-b.border-t 1440.0x316.0 bg #ffffff border T:1px solid #efefed / B:1px solid #efefed shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0f172a @ 0.08 0px 18px 40px 0px; span.flex.h-12 48.0x48.0 bg #ffffff border T:1px solid #e8e7e4 / R:1px solid #e8e7e4 / B:1px solid #e8e7e4 / L:1px solid #e8e7e4 r 14px; span.flex.h-12 48.0x48.0 bg #ffffff border T:1px solid #e8e7e4 / R:1px solid #e8e7e4 / B:1px solid #e8e7e4 / L:1px solid #e8e7e4 r 14px; span.flex.h-12 48.0x48.0 bg #ffffff border T:1px solid #e8e7e4 / R:1px solid #e8e7e4 / B:1px solid #e8e7e4 / L:1px solid #e8e7e4 r 14px; span.flex.h-12 48.0x48.0 bg #ffffff border T:1px solid #e8e7e4 / R:1px solid #e8e7e4 / B:1px solid #e8e7e4 / L:1px solid #e8e7e4 r 14px; span.flex.h-12 48.0x48.0 bg #ffffff border T:1px solid #e8e7e4 / R:1px solid #e8e7e4 / B:1px solid #e8e7e4 / L:1px solid #e8e7e4 r 14px |
| How | at rest |

Crops: `nav-panel-default.png`.

#### nav-menu-item

Nav dropdown item. A link inside the opened dropdown panel; measured, never followed.

Page: home. Selector: `dropdown panel a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 369.33 x 56 | = |
| Padding | 4px | = |
| Gap | 12px | = |
| Border | none | = |
| Radius | 18px | = |
| Background | transparent | #f8f8f7 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #20232b | = |
| Text node | span: Inter 15px/22.5px 600, #17191f, ls -0.375px | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 20 x 20, colour #5c7cfa | = |
| Painted layers | span.flex.h-12 48.0x48.0 bg #ffffff border T:1px solid #e8e7e4 / R:1px solid #e8e7e4 / B:1px solid #e8e7e4 / L:1px solid #e8e7e4 r 14px | a.group.flex 369.3x56.0 bg #f8f8f7 r 18px; span.flex.h-12 48.0x48.0 bg #ffffff border T:1px solid #dfddd9 / R:1px solid #dfddd9 / B:1px solid #dfddd9 / L:1px solid #dfddd9 r 14px |
| How | at rest | mouse hover |

Crops: `nav-menu-item-default.png`, `nav-menu-item-hover.png`.

#### nav-link

Nav link. The "Pricing" header link; measured, never followed.

Page: home. Selector: `header a[href=/pricing]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 47.03 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 14px/21px 500 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #4f5562 | #22252d | = | #22252d |
| Text node | span: Inter 14px/21px 500, #4f5562, ls -0.14px | span: Inter 14px/21px 500, #22252d, ls -0.14px | = | span: Inter 14px/21px 500, #22252d, ls -0.14px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.flex.items-center 47.0x21.0 outline 1px auto #101010 offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Login button. The light "Login" pill in the header linking to app.feedhive.com; measured, never followed.

Page: home. Selector: `header a[href*=signin]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 73.61 x 40 | = | = | = |
| Padding | 0px 18px | = | = | = |
| Border | none | = | = | = |
| Radius | 11px | = | = | = |
| Background | #f4f2f0 | #efedeb | = | #efedeb |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 14px/21px 500 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #272b34 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.h-10 73.6x40.0 bg #f4f2f0 r 11px | a.inline-flex.h-10 73.6x40.0 bg #efedeb r 11px | a.inline-flex.h-10 73.6x40.0 bg #f4f2f0 r 11px outline 1px auto #101010 offset 1px | a.inline-flex.h-10 73.6x40.0 bg #efedeb r 11px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-signup

Sign Up button. The indigo "Sign Up" pill in the header linking to app.feedhive.com/signup; measured, never followed.

Page: home. Selector: `header a[href*=signup] (the painted copy)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 88.05 x 40 | = | = | = |
| Padding | 0px 18px | = | = | = |
| Border | none | = | = | = |
| Radius | 11px | = | = | = |
| Background | #4457ff | #3347fb | = | #3347fb |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 14px/21px 500 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.h-10 88.0x40.0 bg #4457ff r 11px | a.inline-flex.h-10 88.0x40.0 bg #3347fb r 11px | a.inline-flex.h-10 88.0x40.0 bg #4457ff r 11px outline 1px auto #101010 offset 1px | a.inline-flex.h-10 88.0x40.0 bg #3347fb r 11px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signup-default.png`, `nav-signup-hover.png`, `nav-signup-focus-visible.png`, `nav-signup-pressed.png`.

### Home

#### hero-badge

Release badge. The "Introducing FeedHive v2.0" pill badge over the hero — the gradient-ring outer div.

Page: home. Selector: `main div.cta-gradient-ring`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 217.94 x 35 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 3.35544e+07px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #20232b | = |
| Text node | span: Inter 14px/21px 700, #31343a, ls -0.42px | = |
| Transition | none | = |
| ::before | 223.938px x 41px, absolute, bg #000000 @ 0 conic-gradient(from 0deg, #4f7dff, #7165ff, #d650ff, #ff7f59, #4f7dff), radius 9999px | 223.938px x 41px, absolute, bg #000000 @ 0 conic-gradient(from 68.1778deg, #4f7dff, #7165ff, #d650ff, #ff7f59, #4f7dff), radius 9999px |
| ::after | 227.938px x 45px, absolute, bg #000000 @ 0 radial-gradient(circle, #636eff @ 0.42, #000000 @ 0 68%), radius 9999px | = |
| Painted layers | div::before.cta-gradient-ring.cta-gradient-ring-pill 223.938pxx41px image conic-gradient(from 0deg, #4f7dff, #7165ff, #d650ff, #ff7f59, #4f7dff) r 9999px; div::after.cta-gradient-ring.cta-gradient-ring-pill 227.938pxx45px image radial-gradient(circle, #636eff @ 0.42, #000000 @ 0 68%) r 9999px; div.inline-flex.items-center 217.9x35.0 bg #ffffff border T:1px solid #dfdfe4 / R:1px solid #dfdfe4 / B:1px solid #dfdfe4 / L:1px solid #dfdfe4 r 3.35544e+07px; span.rounded-md.border 35.3x16.0 bg #f7f7f9 border T:1px solid #cfd1d9 / R:1px solid #cfd1d9 / B:1px solid #cfd1d9 / L:1px solid #cfd1d9 r 6px | div::before.cta-gradient-ring.cta-gradient-ring-pill 223.938pxx41px image conic-gradient(from 68.1778deg, #4f7dff, #7165ff, #d650ff, #ff7f59, #4f7dff) r 9999px; div::after.cta-gradient-ring.cta-gradient-ring-pill 227.938pxx45px image radial-gradient(circle, #636eff @ 0.42, #000000 @ 0 68%) r 9999px; div.inline-flex.items-center 217.9x35.0 bg #ffffff border T:1px solid #dfdfe4 / R:1px solid #dfdfe4 / B:1px solid #dfdfe4 / L:1px solid #dfdfe4 r 3.35544e+07px; span.rounded-md.border 35.3x16.0 bg #f7f7f9 border T:1px solid #cfd1d9 / R:1px solid #cfd1d9 / B:1px solid #cfd1d9 / L:1px solid #cfd1d9 r 6px |
| How | at rest | mouse hover |

Crops: `hero-badge-default.png`, `hero-badge-hover.png`.

#### hero-h1

Hero headline. "Social media using Automation & AI Agents." — the display heading; the second line paints the indigo accent.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 620 x 115.45 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 55px/56.1px 600 |
| Letter spacing | -1.925px |
| Colour | #23252b |
| Text node | span.block: Plus Jakarta Sans 55px/56.1px 600, #23252b, ls -1.925px |
| Transition | none |
| Painted layers | span.agent-logo-badge 51.7x51.7 bg #ffffff @ 0.98 border T:1px solid #cfd3dd @ 0.9 / R:1px solid #cfd3dd @ 0.9 / B:1px solid #cfd3dd @ 0.9 / L:1px solid #cfd3dd @ 0.9 r 11px |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-sub

Hero lede. The muted lede under the headline.

Page: home. Selector: `hero lede p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 560 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | -0.416px |
| Colour | #666c77 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-cta

Hero CTA. The indigo "Get started for free" button in the hero; measured, never followed.

Page: home. Selector: `hero Get started for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 196.02 x 50 | = | = | = |
| Padding | 0px 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 15px | = | = | = |
| Background | #4457ff | #3347fb | = | #3347fb |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 15px/22.5px 500 | = | = | = |
| Letter spacing | -0.45px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.h-[50px] 196.0x50.0 bg #4457ff r 15px | a.inline-flex.h-[50px] 196.0x50.0 bg #3347fb r 15px | a.inline-flex.h-[50px] 196.0x50.0 bg #4457ff r 15px outline 1px auto #101010 offset 1px | a.inline-flex.h-[50px] 196.0x50.0 bg #3347fb r 15px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-check

Feature check row. A checked feature row ("Create with AI. Generate content that fits your tone-of-voice & brand.").

Page: home. Selector: `hero check list li`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 560 x 23.19 |
| Padding | 0px |
| Gap | 10px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/23.2px 400 |
| Letter spacing | -0.416px |
| Colour | #666c77 |
| Text node | span.font-bold.text-[#24262d]: Inter 16px/23.2px 700, #24262d, ls -0.416px |
| Transition | none |
| Icon | 16 x 16, colour #4457ff |
| How | at rest |

Crops: `hero-check-default.png`.

#### hero-mock

Product mock panel. The product screenshot beside the hero — a static public image clipped by a rounded container, not the signed-in product.

Page: home. Selector: `hero product mock (img clip)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 688.48 x 592.52 |
| Padding | 0px |
| Border | none |
| Radius | 16px 0px 0px 16px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #20232b |
| Transition | none |
| Painted layers | div.pointer-events-none.absolute 89.5x592.5 image linear-gradient(to left, #ffffff 0%, #ffffff @ 0.48 50%, #000000 @ 0 100%); div.pointer-events-none.absolute 688.5x100.7 image linear-gradient(to top, #ffffff 0%, #ffffff @ 0.52 50%, #000000 @ 0 100%) |
| How | at rest |

Crops: `hero-mock-default.png`.

#### agent-card

Agent card. An AI-agent feature card ("Hermes Agent ↗ — Use Herm…") on the home page; measured, never followed.

Page: home. Selector: `agent feature card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 585 x 416.16 | = |
| Padding | 24px 34px 0px 34px | = |
| Border | none | = |
| Radius | 15px | = |
| Background | #f6f6f8 | #f0f1f6 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.7 0px 1px 0px 0px inset | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #20232b | = |
| Text node | p.sometype_mono_75ea6769-module__w3R14q__className.mb-2: Sometype Mono 11px/16.5px 700, #4457ff, ls 1.1px | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | a.group.relative 585.0x416.2 bg #f6f6f8 r 15px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.7 0px 1px 0px 0px inset | a.group.relative 585.0x416.2 bg #f0f1f6 r 15px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.7 0px 1px 0px 0px inset |
| How | at rest | mouse hover |

Crops: `agent-card-default.png`, `agent-card-hover.png`.

#### section-h2

Section heading. A marketing section heading further down the home page.

Page: home. Selector: `main h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 760 x 113.66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 58px/56.84px 600 |
| Letter spacing | -1.74px |
| Colour | #23252b |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

### Feature tabs

#### tab-pill

Feature tab pill. One of the feature tab pills (Composer / AI Assistant / Automation / …) that switch the showcase panel — a local UI toggle; selected by clicking.

Page: home. Selector: `main button Composer`. States: default, hover, selected.

| Property | default | hover | selected |
|---|---|---|---|
| Size (w x h) | 94.77 x 30 | = | 106.77 x 30 |
| Padding | 0px 12px | = | 0px 20px 0px 16px |
| Border | 1px dashed #d8dbe2 | 1px dashed #979daa | 1px solid #84a1ff |
| Radius | 3.35544e+07px | = | = |
| Background | #ffffff | = | #eef2ff |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 14px/21px 500 | = | = |
| Letter spacing | -0.28px | = | = |
| Colour | #585f6b | #2c3139 | #5a84ff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.inline-flex.h-[30px] 94.8x30.0 bg #ffffff border T:1px dashed #d8dbe2 / R:1px dashed #d8dbe2 / B:1px dashed #d8dbe2 / L:1px dashed #d8dbe2 r 3.35544e+07px | button.inline-flex.h-[30px] 94.8x30.0 bg #ffffff border T:1px dashed #979daa / R:1px dashed #979daa / B:1px dashed #979daa / L:1px dashed #979daa r 3.35544e+07px | button.inline-flex.h-[30px] 106.8x30.0 bg #eef2ff border T:1px solid #84a1ff / R:1px solid #84a1ff / B:1px solid #84a1ff / L:1px solid #84a1ff r 3.35544e+07px; span.tag-check-bounce.absolute 24.0x24.0 bg #5a84ff border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 3.35544e+07px |
| How | at rest | mouse hover | own toggle, then left selected |
| Icon | - | = | 14 x 14, colour #ffffff |

Crops: `tab-pill-default.png`, `tab-pill-hover.png`, `tab-pill-selected.png`.

#### tab-pill-active

Feature tab pill (active). A feature tab pill in its selected state — the #eef2ff indigo tint, #84a1ff border and #5a84ff ink the pills select into; selected by clicking (the at-load selection auto-rotates).

Page: home. Selector: `main button AI Assistant`. States: selected.

| Property | selected |
|---|---|
| Size (w x h) | 116.64 x 30 |
| Padding | 0px 20px 0px 16px |
| Border | 1px solid #84a1ff |
| Radius | 3.35544e+07px |
| Background | #eef2ff |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/21px 500 |
| Letter spacing | -0.28px |
| Colour | #5a84ff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 14 x 14, colour #ffffff |
| Painted layers | button.inline-flex.h-[30px] 116.6x30.0 bg #eef2ff border T:1px solid #84a1ff / R:1px solid #84a1ff / B:1px solid #84a1ff / L:1px solid #84a1ff r 3.35544e+07px; span.tag-check-bounce.absolute 24.0x24.0 bg #5a84ff border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 3.35544e+07px |
| How | own toggle, then left selected |

Crops: `tab-pill-active-selected.png`.

### Footer

#### footer

Footer. The page footer: sitemap columns, legal links, social icons, the cookie-preferences button.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 814.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #20232b |
| Text node | p.mt-6.max-w-[260px]: Inter 15px/24.75px 400, #737987, ls -0.3px |
| Transition | none |
| Icon | 18 x 18, colour #767c88 |
| Painted layers | footer.relative.overflow-hidden 1440.0x814.5 bg #ffffff; div.pointer-events-none.absolute 1440.0x1.0 image linear-gradient(90deg, #e6e2dc @ 0 0%, #e6e2dc 16%, #e6e2dc 84%, #e6e2dc @ 0 100%); span.inline-flex.min-h-[34px] 162.0x34.0 bg #ffffff @ 0.92 border T:1px solid #e3e0db / R:1px solid #e3e0db / B:1px solid #e3e0db / L:1px solid #e3e0db r 3.35544e+07px; span.inline-flex.min-h-[34px] 145.7x34.0 bg #ffffff @ 0.92 border T:1px solid #e3e0db / R:1px solid #e3e0db / B:1px solid #e3e0db / L:1px solid #e3e0db r 3.35544e+07px; span.inline-flex.min-h-[34px] 129.2x34.0 bg #ffffff @ 0.92 border T:1px solid #e3e0db / R:1px solid #e3e0db / B:1px solid #e3e0db / L:1px solid #e3e0db r 3.35544e+07px; span.inline-flex.min-h-[34px] 140.7x34.0 bg #ffffff @ 0.92 border T:1px solid #e3e0db / R:1px solid #e3e0db / B:1px solid #e3e0db / L:1px solid #e3e0db r 3.35544e+07px |
| Ancestor paint | 1 up main.min-h-screen.bg-white bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer sitemap link; measured, never followed.

Page: home. Selector: `footer a Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44.91 x 19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 15px/24px 400 | = | = | = |
| Letter spacing | -0.3px | = | = | = |
| Colour | #676e7b | #22252d | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.transition.hover:text-[#22252d] 44.9x19.0 outline 1px auto #101010 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Pricing

#### price-h1

Pricing headline. "The best social solution, for the best price." — the /pricing masthead.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 760 x 125.44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 64px/62.72px 600 |
| Letter spacing | -2.56px |
| Colour | #23252b |
| Transition | none |
| How | at rest |

Crops: `price-h1-default.png`.

#### billing-monthly

Billing toggle (Monthly). The "Monthly" half of the billing pill — a local UI toggle that re-renders the prices; selected by clicking.

Page: pricing. Selector: `pricing Monthly button`. States: default, hover, selected.

| Property | default | hover | selected |
|---|---|---|---|
| Size (w x h) | 112 x 41 | = | = |
| Padding | 10px 20px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | transparent | = | #3347fb |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 14px/21px 600 | = | = |
| Letter spacing | -0.28px | = | = |
| Colour | #757b86 | #2b2f37 | #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | default | = | = |
| Ancestor paint | 1 up div.inline-flex.rounded-full bg #ffffff @ 0.95 | = | = |
| How | at rest | mouse hover | own toggle, then left selected |
| Painted layers | - | = | button.min-w-[112px].rounded-full 112.0x41.0 bg #3347fb r 3.35544e+07px |

Crops: `billing-monthly-default.png`, `billing-monthly-hover.png`, `billing-monthly-selected.png`.

#### billing-yearly

Billing toggle (Yearly). The "Yearly" half of the billing pill, selected on load.

Page: pricing. Selector: `pricing Yearly button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 112 x 41 | = | = | = |
| Padding | 10px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #4457ff | #3347fb | = | #3347fb |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter 14px/21px 600 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | button.min-w-[112px].rounded-full 112.0x41.0 bg #4457ff r 3.35544e+07px | button.min-w-[112px].rounded-full 112.0x41.0 bg #3347fb r 3.35544e+07px | button.min-w-[112px].rounded-full 112.0x41.0 bg #4457ff r 3.35544e+07px outline 1px auto #101010 offset 0px | button.min-w-[112px].rounded-full 112.0x41.0 bg #3347fb r 3.35544e+07px |
| Ancestor paint | 1 up div.inline-flex.rounded-full bg #ffffff @ 0.95 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `billing-yearly-default.png`, `billing-yearly-hover.png`, `billing-yearly-focus-visible.png`, `billing-yearly-pressed.png`.

#### plan-card

Plan card (Business). The highlighted indigo "Business" plan card ("POPULAR" chip).

Page: pricing. Selector: `Business plan article`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 297 x 652.5 |
| Padding | 20px 20px 24px 20px |
| Border | 1px solid #4457ff |
| Radius | 16px |
| Background | #4457ff |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.plus_jakarta_sans_4684badf-module__N0Y3xW__className.text-[31px]: Plus Jakarta Sans 31px/31px 600, #ffffff, ls -1.24px |
| Transition | none |
| Icon | 14 x 14, colour #ffffff |
| Painted layers | article.relative.flex 297.0x652.5 bg #4457ff border T:1px solid #4457ff / R:1px solid #4457ff / B:1px solid #4457ff / L:1px solid #4457ff r 16px; div.min-h-[212px].border-b 255.0x252.5 border B:1px solid #ffffff @ 0.1; span.rounded-full.border 84.2x21.0 bg #ffffff border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 3.35544e+07px; a.inline-flex.h-[50px] 255.0x50.0 bg #ffffff r 15px; span.mt-0.5.inline-flex 20.0x20.0 bg #ffffff @ 0.1 border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 3.35544e+07px; span.mt-0.5.inline-flex 20.0x20.0 bg #ffffff @ 0.1 border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 3.35544e+07px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-card-plain

Plan card (Creator). A plain plan card beside the highlighted one.

Page: pricing. Selector: `Creator plan article`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 297 x 652.5 |
| Padding | 20px 20px 24px 20px |
| Border | 1px solid #e8e4dd |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #20232b |
| Text node | h2.plus_jakarta_sans_4684badf-module__N0Y3xW__className.text-[31px]: Plus Jakarta Sans 31px/31px 600, #23252b, ls -1.24px |
| Transition | none |
| Icon | 14 x 14, colour #2c3138 |
| Painted layers | article.relative.flex 297.0x652.5 bg #ffffff border T:1px solid #e8e4dd / R:1px solid #e8e4dd / B:1px solid #e8e4dd / L:1px solid #e8e4dd r 16px; div.min-h-[212px].border-b 255.0x252.5 border B:1px solid #ece8e1; a.inline-flex.h-[50px] 255.0x50.0 bg #4457ff r 15px; span.mt-0.5.inline-flex 20.0x20.0 bg #f8f7f4 border T:1px solid #ddd9d2 / R:1px solid #ddd9d2 / B:1px solid #ddd9d2 / L:1px solid #ddd9d2 r 3.35544e+07px; span.mt-0.5.inline-flex 20.0x20.0 bg #f8f7f4 border T:1px solid #ddd9d2 / R:1px solid #ddd9d2 / B:1px solid #ddd9d2 / L:1px solid #ddd9d2 r 3.35544e+07px; span.mt-0.5.inline-flex 20.0x20.0 bg #f8f7f4 border T:1px solid #ddd9d2 / R:1px solid #ddd9d2 / B:1px solid #ddd9d2 / L:1px solid #ddd9d2 r 3.35544e+07px |
| How | at rest |

Crops: `plan-card-plain-default.png`.

#### plan-cta

Plan CTA. A plan card's "Get started" button; measured, never followed.

Page: pricing. Selector: `plan Get started`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 255 x 50 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 15px | = | = | = |
| Background | #4457ff | #3347fb | = | #3347fb |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 15px/22.5px 600 | = | = | = |
| Letter spacing | -0.45px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.h-[50px] 255.0x50.0 bg #4457ff r 15px | a.inline-flex.h-[50px] 255.0x50.0 bg #3347fb r 15px | a.inline-flex.h-[50px] 255.0x50.0 bg #4457ff r 15px outline 1px auto #101010 offset 1px | a.inline-flex.h-[50px] 255.0x50.0 bg #3347fb r 15px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### trial-badge

Trial badge. The "7-day free trial" pill over the plan cards — the gradient-ring outer div.

Page: pricing. Selector: `7-day free trial badge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 154.28 x 35 |
| Padding | 0px |
| Border | none |
| Radius | 3.35544e+07px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #20232b |
| Text node | span: Inter 14px/21px 700, #31343a, ls -0.42px |
| Transition | none |
| Icon | 16 x 16, colour #5a78ff |
| ::before | 160.281px x 41px, absolute, bg #000000 @ 0 conic-gradient(from 0deg, #4f7dff, #7165ff, #d650ff, #ff7f59, #4f7dff), radius 9999px |
| ::after | 164.281px x 45px, absolute, bg #000000 @ 0 radial-gradient(circle, #636eff @ 0.42, #000000 @ 0 68%), radius 9999px |
| Painted layers | div::before.cta-gradient-ring.cta-gradient-ring-pill 160.281pxx41px image conic-gradient(from 0deg, #4f7dff, #7165ff, #d650ff, #ff7f59, #4f7dff) r 9999px; div::after.cta-gradient-ring.cta-gradient-ring-pill 164.281pxx45px image radial-gradient(circle, #636eff @ 0.42, #000000 @ 0 68%) r 9999px; div.inline-flex.items-center 154.3x35.0 bg #ffffff border T:1px solid #dfdfe4 / R:1px solid #dfdfe4 / B:1px solid #dfdfe4 / L:1px solid #dfdfe4 r 3.35544e+07px |
| How | at rest |

Crops: `trial-badge-default.png`.

### Feature pages

#### feat-eyebrow

Page eyebrow. The tracked caps eyebrow label ("SCHEDULING", Sometype Mono) over the feature page masthead.

Page: features. Selector: `feature eyebrow`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 560 x 21 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sometype Mono 14px/21px 700 |
| Letter spacing | 1.96px |
| Colour | #4457ff |
| Transition | none |
| How | at rest |

Crops: `feat-eyebrow-default.png`.

#### feat-h1

Feature headline. "Plan and schedule your content." — the /features/scheduling masthead.

Page: features. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 560 x 121.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 62px/60.76px 600 |
| Letter spacing | -1.86px |
| Colour | #23252b |
| Transition | none |
| How | at rest |

Crops: `feat-h1-default.png`.

#### feat-cta

Feature CTA. The feature page's "Get started for free" call-to-action; measured, never followed.

Page: features. Selector: `feature Get started CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 196.02 x 50 | = | = | = |
| Padding | 0px 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 15px | = | = | = |
| Background | #4457ff | #3347fb | = | #3347fb |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 15px/22.5px 500 | = | = | = |
| Letter spacing | -0.45px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.h-[50px] 196.0x50.0 bg #4457ff r 15px | a.inline-flex.h-[50px] 196.0x50.0 bg #3347fb r 15px | a.inline-flex.h-[50px] 196.0x50.0 bg #4457ff r 15px outline 1px auto #101010 offset 1px | a.inline-flex.h-[50px] 196.0x50.0 bg #3347fb r 15px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `feat-cta-default.png`, `feat-cta-hover.png`, `feat-cta-focus-visible.png`, `feat-cta-pressed.png`.

#### feat-card

Feature card. A feature card in the scheduling page grid ("AI Image Generation", "Post Recycling", …).

Page: features. Selector: `feature article card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 247.19 x 225 | 249.66 x 227.25 |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px 0px 5px 0px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #424a77 @ 0.08 0px 24px 60px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #424a77 @ 0.14 0px 30px 68px 0px |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #20232b | = |
| Text node | h3.plus_jakarta_sans_4684badf-module__N0Y3xW__className.text-[20px]: Plus Jakarta Sans 20px/30px 600, #2f3343, ls -0.8px | h3.plus_jakarta_sans_4684badf-module__N0Y3xW__className.text-[20px]: Plus Jakarta Sans 20px/30px 600, #232735, ls -0.8px |
| Transition | transform, box-shadow 0.3s cubic-bezier(0.22, 1, 0.36, 1) | = |
| Icon | 19 x 19, colour #df6b85 | 19.77 x 19.77, colour #df6b85 |
| Painted layers | article.group.relative 247.2x225.0 bg #ffffff r 0px 0px 5px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #424a77 @ 0.08 0px 24px 60px 0px; div.pointer-events-none.absolute 247.2x225.0 image radial-gradient(circle at 50% 100%, #f4a1bd @ 0.28, #ffffff @ 0 72%); span.mb-3.inline-flex 40.0x40.0 bg #ffe9ef r 12px | article.group.relative 249.7x227.3 bg #ffffff r 0px 0px 5px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #424a77 @ 0.14 0px 30px 68px 0px; div.pointer-events-none.absolute 249.7x227.3 image radial-gradient(circle at 50% 100%, #f4a1bd @ 0.28, #ffffff @ 0 72%); span.mb-3.inline-flex 41.6x41.6 bg #ffe9ef r 12px |
| Ancestor paint | 1 up div.relative.grid bg #edeef3 | = |
| How | at rest | mouse hover |

Crops: `feat-card-default.png`, `feat-card-hover.png`.

### Blog

#### blog-h1

Blog headline. "FeedHive blog" — the /blog masthead.

Page: blog. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 760 x 65.27 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 68px/65.28px 600 |
| Letter spacing | -3.06px |
| Colour | #23252b |
| Transition | none |
| How | at rest |

Crops: `blog-h1-default.png`.

#### blog-card

Featured post card. The featured article card on the blog index; measured, never followed.

Page: blog. Selector: `blog featured card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1248 x 419.59 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #20232b | = |
| Text node | span.inline-flex.items-center: Inter 11px/16.5px 600, #516fe2, ls 1.54px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.overflow-hidden.rounded-[16px] 652.3x366.9 bg #efeff3 r 16px; span.inline-flex.items-center 138.0x30.5 bg #ffffff border T:1px solid #dfe2ea / R:1px solid #dfe2ea / B:1px solid #dfe2ea / L:1px solid #dfe2ea r 3.35544e+07px; div.mt-8.flex 555.7x80.0 bg #f6f6f8 r 16px; span.inline-flex.min-h-[40px] 114.6x40.0 bg #ffffff r 11px | div.overflow-hidden.rounded-[16px] 652.3x366.9 bg #efeff3 r 16px; span.inline-flex.items-center 138.0x30.5 bg #ffffff border T:1px solid #dfe2ea / R:1px solid #dfe2ea / B:1px solid #dfe2ea / L:1px solid #dfe2ea r 3.35544e+07px; div.mt-8.flex 555.7x80.0 bg #f1f2f5 r 16px; span.inline-flex.min-h-[40px] 114.6x40.0 bg #ffffff r 11px |
| How | at rest | mouse hover |

Crops: `blog-card-default.png`.

#### blog-row

Article row. An article card/row in the archive list; measured, never followed.

Page: blog. Selector: `blog archive row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 382.66 x 598.28 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #20232b | = |
| Text node | span: Inter 13px/19.5px 500, #6c7280, ls -0.26px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | article.flex.h-full 382.7x598.3 bg #f6f6f8 r 16px; div.overflow-hidden.bg-[#eceef3] 382.7x215.2 bg #eceef3; div.mt-6.border-t 326.7x60.0 border T:1px solid #e7e8ec | article.flex.h-full 382.7x598.3 bg #f1f2f5 r 16px; div.overflow-hidden.bg-[#eceef3] 382.7x215.2 bg #eceef3; div.mt-6.border-t 326.7x60.0 border T:1px solid #e7e8ec |
| How | at rest | mouse hover |

Crops: `blog-row-default.png`, `blog-row-hover.png`.

### Tools

#### bio-h1

Tool headline. "Free AI bio generator for social media" — the /tools/bio-generator masthead.

Page: tools-bio. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 760 x 122.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 60px/61.2px 600 |
| Letter spacing | -2.4px |
| Colour | #23252b |
| Transition | none |
| How | at rest |

Crops: `bio-h1-default.png`.

#### bio-platform

Platform option. A platform option button (TikTok / Instagram / LinkedIn) — a local UI toggle; selected by clicking.

Page: tools-bio. Selector: `bio platform Instagram`. States: default, hover, selected.

| Property | default | hover | selected |
|---|---|---|---|
| Size (w x h) | 116 x 40 | = | = |
| Padding | 0px | = | = |
| Gap | 8px | = | = |
| Border | none | = | = |
| Radius | 9px | = | = |
| Background | #ffffff | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #dfdfe4 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = |
| Font | Inter 14px/21px 500 | = | = |
| Letter spacing | -0.28px | = | = |
| Colour | #23252b | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 15 x 15, colour #23252b | = | = |
| Painted layers | button.inline-flex.min-h-10 116.0x40.0 bg #ffffff r 9px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #dfdfe4 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Ancestor paint | 1 up div.mt-2.5.grid-cols-3 bg #f6f6f8 | = | = |
| How | at rest | mouse hover | own toggle, then left selected |

Crops: `bio-platform-default.png`, `bio-platform-hover.png`, `bio-platform-selected.png`.

#### bio-tone

Tone option. A tone option button (Professional / Friendly / Funny / Bold / Aesthetic); measured at rest.

Page: tools-bio. Selector: `bio tone Professional`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 104.89 x 36 | = |
| Padding | 0px 14px | = |
| Border | 1px solid #dfdfe4 | 1px solid #c6cad4 |
| Radius | 3.35544e+07px | = |
| Background | #ffffff | #fafafa |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 13px/19.5px 500 | = |
| Letter spacing | -0.26px | = |
| Colour | #4c525e | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.inline-flex.min-h-9 104.9x36.0 bg #ffffff border T:1px solid #dfdfe4 / R:1px solid #dfdfe4 / B:1px solid #dfdfe4 / L:1px solid #dfdfe4 r 3.35544e+07px | button.inline-flex.min-h-9 104.9x36.0 bg #fafafa border T:1px solid #c6cad4 / R:1px solid #c6cad4 / B:1px solid #c6cad4 / L:1px solid #c6cad4 r 3.35544e+07px |
| How | at rest | mouse hover |

Crops: `bio-tone-default.png`, `bio-tone-hover.png`.

#### bio-textarea

Bio input. The "describe yourself" textarea; focused and typed into then cleared — never submitted.

Page: tools-bio. Selector: `bio textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 362 x 110 | = | = |
| Padding | 14px 16px 0px 16px | = | = |
| Border | none | = | = |
| Radius | 12px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 15px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #23252b | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #a3a8b3, opacity 1 | = | = |
| Ancestor paint | 1 up div.mt-2.5.rounded-[12px] bg #ffffff | = | = |
| How | at rest | clicked into the field | typed "A ceramics studio posting reels.", then deleted; nothing sent |

Crops: `bio-textarea-default.png`, `bio-textarea-focused.png`, `bio-textarea-filled.png`.

#### bio-submit

Generate button. The "Generate bios" submit; its states were measured but the button was never clicked — nothing was submitted.

Page: tools-bio. Selector: `bio Generate bios`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 364 x 50 | = | - | = |
| Padding | 0px 24px | = | - | = |
| Gap | 8px | = | - | = |
| Border | none | = | - | = |
| Radius | 15px | = | - | = |
| Background | #b9c0f5 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 15px/22.5px 500 | = | - | = |
| Letter spacing | -0.45px | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | - | = |
| Cursor | not-allowed | = | - | = |
| Icon | 20 x 20, colour #ffffff | = | - | = |
| Painted layers | button.inline-flex.h-[50px] 364.0x50.0 bg #b9c0f5 r 15px | = | - | = |
| Ancestor paint | 1 up form.rounded-[12px].bg-white bg #ffffff | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `bio-submit-default.png`, `bio-submit-hover.png`, `bio-submit-pressed.png`.

### App sign-in (Chakra)

#### login-panel

Sign-in card. The sign-in card over the pale field: "Let's get you signed in".

Page: login. Selector: `signin card (painted ancestor of email input)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 512 x 610.31 |
| Padding | 44.16px |
| Border | none |
| Radius | 20px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.04 0px 10px 10px -5px |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1a202c |
| Text node | h2.chakra-heading.css-1y49h1s: Inter 18.4px/22.08px 700, #1a202c |
| Transition | none |
| Icon | 14.72 x 14.72, colour #ffffff |
| Painted layers | div.css-a2vays 512.0x610.3 bg #ffffff r 20px shadow #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.04 0px 10px 10px -5px; button.chakra-button.css-15oj2jg 423.7x60.9 border T:1px solid #edf2f7 / R:1px solid #edf2f7 / B:1px solid #edf2f7 / L:1px solid #edf2f7 r 9999px shadow #1b1979 @ 0.05 0px 2px 8px 0px outline 2px solid #000000 @ 0 offset 2px; hr.chakra-divider.css-svjswr 185.6x1.0 border B:1px solid #edf2f7; hr.chakra-divider.css-svjswr 185.6x1.0 border B:1px solid #edf2f7; input.chakra-input.css-1f2r15g 423.7x60.9 border T:1px solid #edf2f7 / R:1px solid #edf2f7 / B:1px solid #edf2f7 / L:1px solid #edf2f7 r 9999px shadow #1b1979 @ 0.05 0px 2px 8px 0px outline 2px solid #000000 @ 0 offset 2px; input.chakra-input.css-1f2r15g 423.7x60.9 border T:1px solid #edf2f7 / R:1px solid #edf2f7 / B:1px solid #edf2f7 / L:1px solid #edf2f7 r 9999px shadow #1b1979 @ 0.05 0px 2px 8px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `login-panel-default.png`.

#### login-google

Google sign-in. The "Sign in with Google" outlined pill; measured, never followed.

Page: login. Selector: `signin Google button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 423.69 x 60.88 | = | = | = |
| Padding | 29.44px | = | = | = |
| Border | 1px solid #edf2f7 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #f7fafc | = | #edf2f7 |
| Box shadow | #1b1979 @ 0.05 0px 2px 8px 0px | = | none | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 14.72px/17.664px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1a202c | = | = | = |
| Transition | background-color, border-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.chakra-button.css-15oj2jg 423.7x60.9 border T:1px solid #edf2f7 / R:1px solid #edf2f7 / B:1px solid #edf2f7 / L:1px solid #edf2f7 r 9999px shadow #1b1979 @ 0.05 0px 2px 8px 0px outline 2px solid #000000 @ 0 offset 2px | button.chakra-button.css-15oj2jg 423.7x60.9 bg #f7fafc border T:1px solid #edf2f7 / R:1px solid #edf2f7 / B:1px solid #edf2f7 / L:1px solid #edf2f7 r 9999px shadow #1b1979 @ 0.05 0px 2px 8px 0px outline 2px solid #000000 @ 0 offset 2px | button.chakra-button.css-15oj2jg 423.7x60.9 border T:1px solid #edf2f7 / R:1px solid #edf2f7 / B:1px solid #edf2f7 / L:1px solid #edf2f7 r 9999px outline 2px solid #000000 @ 0 offset 2px | button.chakra-button.css-15oj2jg 423.7x60.9 bg #edf2f7 border T:1px solid #edf2f7 / R:1px solid #edf2f7 / B:1px solid #edf2f7 / L:1px solid #edf2f7 r 9999px shadow #1b1979 @ 0.05 0px 2px 8px 0px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up div.css-a2vays bg #ffffff shadow #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.04 0px 10px 10px -5px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-google-default.png`, `login-google-hover.png`, `login-google-focus-visible.png`, `login-google-pressed.png`.

#### login-field-email

Email field (sign-in). The Email input on the app sign-in; focused and typed into then cleared — never submitted.

Page: login. Selector: `signin input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 423.69 x 60.88 | = | = |
| Padding | 29.44px | = | = |
| Border | 1px solid #edf2f7 | 1px solid #3b82f6 | 1px solid #3b82f6 |
| Radius | 9999px | = | = |
| Background | transparent | = | = |
| Box shadow | #1b1979 @ 0.05 0px 2px 8px 0px | none | none |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | Inter 14.72px/22.08px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1a202c | = | = |
| Transition | background-color, border-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #a0aec0, opacity 1 | = | = |
| Painted layers | input.chakra-input.css-1f2r15g 423.7x60.9 border T:1px solid #edf2f7 / R:1px solid #edf2f7 / B:1px solid #edf2f7 / L:1px solid #edf2f7 r 9999px shadow #1b1979 @ 0.05 0px 2px 8px 0px outline 2px solid #000000 @ 0 offset 2px | input.chakra-input.css-1f2r15g 423.7x60.9 border T:1px solid #3b82f6 / R:1px solid #3b82f6 / B:1px solid #3b82f6 / L:1px solid #3b82f6 r 9999px outline 2px solid #000000 @ 0 offset 2px | input.chakra-input.css-1f2r15g 423.7x60.9 border T:1px solid #3b82f6 / R:1px solid #3b82f6 / B:1px solid #3b82f6 / L:1px solid #3b82f6 r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-field-email-default.png`, `login-field-email-focused.png`, `login-field-email-filled.png`.

#### login-field-pass

Password field (sign-in). The Password input on the app sign-in; focused and typed into then cleared — never submitted.

Page: login. Selector: `signin input[type=password]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 423.69 x 60.88 | = | = |
| Padding | 29.44px | = | = |
| Border | 1px solid #edf2f7 | 1px solid #3b82f6 | 1px solid #3b82f6 |
| Radius | 9999px | = | = |
| Background | transparent | = | = |
| Box shadow | #1b1979 @ 0.05 0px 2px 8px 0px | none | none |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | Inter 14.72px/22.08px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1a202c | = | = |
| Transition | background-color, border-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #a0aec0, opacity 1 | = | = |
| Painted layers | input.chakra-input.css-1f2r15g 423.7x60.9 border T:1px solid #edf2f7 / R:1px solid #edf2f7 / B:1px solid #edf2f7 / L:1px solid #edf2f7 r 9999px shadow #1b1979 @ 0.05 0px 2px 8px 0px outline 2px solid #000000 @ 0 offset 2px | input.chakra-input.css-1f2r15g 423.7x60.9 border T:1px solid #3b82f6 / R:1px solid #3b82f6 / B:1px solid #3b82f6 / L:1px solid #3b82f6 r 9999px outline 2px solid #000000 @ 0 offset 2px | input.chakra-input.css-1f2r15g 423.7x60.9 border T:1px solid #3b82f6 / R:1px solid #3b82f6 / B:1px solid #3b82f6 / L:1px solid #3b82f6 r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "not-a-real-password", then deleted; nothing sent |

Crops: `login-field-pass-default.png`, `login-field-pass-focused.png`, `login-field-pass-filled.png`.

#### login-submit

Sign in submit. The sign-in submit button; its states were measured but the button was never clicked — nothing was submitted.

Page: login. Selector: `signin Sign in submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 423.69 x 58.88 | 415.21 x 57.7 | = | 415.21 x 57.7 |
| Padding | 29.44px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #3b82f6 | = | = | = |
| Background image | linear-gradient(60deg, #4457ff, #7583fd) | = | = | = |
| Box shadow | #596aff @ 0.28 0px 0px 35px 10px | = | none | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 14.72px/17.664px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14.72 x 14.72, colour #ffffff | 14.42 x 14.42, colour #ffffff | = | 14.42 x 14.42, colour #ffffff |
| Painted layers | button.chakra-button.css-56yz0x 423.7x58.9 bg #3b82f6 image linear-gradient(60deg, #4457ff, #7583fd) r 9999px shadow #596aff @ 0.28 0px 0px 35px 10px outline 2px solid #000000 @ 0 offset 2px | button.chakra-button.css-56yz0x 415.2x57.7 bg #3b82f6 image linear-gradient(60deg, #4457ff, #7583fd) r 9999px shadow #596aff @ 0.28 0px 0px 35px 10px outline 2px solid #000000 @ 0 offset 2px | button.chakra-button.css-56yz0x 423.7x58.9 bg #3b82f6 image linear-gradient(60deg, #4457ff, #7583fd) r 9999px outline 2px solid #000000 @ 0 offset 2px | button.chakra-button.css-56yz0x 415.2x57.7 bg #3b82f6 image linear-gradient(60deg, #4457ff, #7583fd) r 9999px shadow #596aff @ 0.28 0px 0px 35px 10px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(0.98, 0, 0, 0.98, 0, 0) | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-focus-visible.png`, `login-submit-pressed.png`.

#### login-forgot

Forgot password link. The "Forgot your password?" link under the submit; measured, never followed.

Page: login. Selector: `signin Forgot your password`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 423.69 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #5d60ec | = | = | = |
| Transition | background-color, border-color, color, fill, stroke, opacity, box-shadow, transform 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.chakra-link.css-5orusm 423.7x21.0 outline 2px solid #000000 @ 0 offset 2px | = | = | = |
| Ancestor paint | 3 up div.css-a2vays bg #ffffff shadow #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.04 0px 10px 10px -5px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-forgot-default.png`, `login-forgot-hover.png`, `login-forgot-focus-visible.png`, `login-forgot-pressed.png`.

### App sign-up (Chakra)

#### signup-panel

Sign-up card. The sign-up card on app.feedhive.com/signup.

Page: signup. Selector: `signup card (painted ancestor of first input)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 512 x 821.42 |
| Padding | 44.16px |
| Border | none |
| Radius | 20px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.04 0px 10px 10px -5px |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1a202c |
| Text node | h2.chakra-heading.css-1y49h1s: Inter 18.4px/22.08px 700, #1a202c |
| Transition | none |
| Icon | 14.72 x 14.72, colour #ffffff |
| Painted layers | div.css-1xhiihc 512.0x821.4 bg #ffffff r 20px shadow #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.04 0px 10px 10px -5px; button.chakra-button.css-15oj2jg 423.7x60.9 border T:1px solid #edf2f7 / R:1px solid #edf2f7 / B:1px solid #edf2f7 / L:1px solid #edf2f7 r 9999px shadow #1b1979 @ 0.05 0px 2px 8px 0px outline 2px solid #000000 @ 0 offset 2px; hr.chakra-divider.css-svjswr 185.6x1.0 border B:1px solid #edf2f7; hr.chakra-divider.css-svjswr 185.6x1.0 border B:1px solid #edf2f7; input.chakra-input.css-53h9yg 423.7x60.9 border T:1px solid #edf2f7 / R:1px solid #edf2f7 / B:1px solid #edf2f7 / L:1px solid #edf2f7 r 9999px shadow #1b1979 @ 0.05 0px 2px 8px 0px outline 2px solid #000000 @ 0 offset 2px; input.chakra-input.css-53h9yg 423.7x60.9 border T:1px solid #edf2f7 / R:1px solid #edf2f7 / B:1px solid #edf2f7 / L:1px solid #edf2f7 r 9999px shadow #1b1979 @ 0.05 0px 2px 8px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `signup-panel-default.png`.

#### signup-google

Google sign-up. The Google sign-up button; measured, never followed.

Page: signup. Selector: `signup Google button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 423.69 x 60.88 | = | = | = |
| Padding | 29.44px | = | = | = |
| Border | 1px solid #edf2f7 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #f7fafc | = | #edf2f7 |
| Box shadow | #1b1979 @ 0.05 0px 2px 8px 0px | = | none | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 14.72px/17.664px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1a202c | = | = | = |
| Transition | background-color, border-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.chakra-button.css-15oj2jg 423.7x60.9 border T:1px solid #edf2f7 / R:1px solid #edf2f7 / B:1px solid #edf2f7 / L:1px solid #edf2f7 r 9999px shadow #1b1979 @ 0.05 0px 2px 8px 0px outline 2px solid #000000 @ 0 offset 2px | button.chakra-button.css-15oj2jg 423.7x60.9 bg #f7fafc border T:1px solid #edf2f7 / R:1px solid #edf2f7 / B:1px solid #edf2f7 / L:1px solid #edf2f7 r 9999px shadow #1b1979 @ 0.05 0px 2px 8px 0px outline 2px solid #000000 @ 0 offset 2px | button.chakra-button.css-15oj2jg 423.7x60.9 border T:1px solid #edf2f7 / R:1px solid #edf2f7 / B:1px solid #edf2f7 / L:1px solid #edf2f7 r 9999px outline 2px solid #000000 @ 0 offset 2px | button.chakra-button.css-15oj2jg 423.7x60.9 bg #edf2f7 border T:1px solid #edf2f7 / R:1px solid #edf2f7 / B:1px solid #edf2f7 / L:1px solid #edf2f7 r 9999px shadow #1b1979 @ 0.05 0px 2px 8px 0px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up div.css-1xhiihc bg #ffffff shadow #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.04 0px 10px 10px -5px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-google-default.png`, `signup-google-hover.png`, `signup-google-focus-visible.png`, `signup-google-pressed.png`.

#### signup-field

Field (sign-up). The first text field on the app sign-up; focused and typed into then cleared — never submitted.

Page: signup. Selector: `signup first input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 423.69 x 60.88 | = | = |
| Padding | 29.44px | = | = |
| Border | 1px solid #edf2f7 | 1px solid #3b82f6 | 1px solid #3b82f6 |
| Radius | 9999px | = | = |
| Background | transparent | = | = |
| Box shadow | #1b1979 @ 0.05 0px 2px 8px 0px | none | none |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | Inter 14.72px/22.08px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1a202c | = | = |
| Transition | background-color, border-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #a0aec0, opacity 1 | = | = |
| Painted layers | input.chakra-input.css-53h9yg 423.7x60.9 border T:1px solid #edf2f7 / R:1px solid #edf2f7 / B:1px solid #edf2f7 / L:1px solid #edf2f7 r 9999px shadow #1b1979 @ 0.05 0px 2px 8px 0px outline 2px solid #000000 @ 0 offset 2px | input.chakra-input.css-53h9yg 423.7x60.9 border T:1px solid #3b82f6 / R:1px solid #3b82f6 / B:1px solid #3b82f6 / L:1px solid #3b82f6 r 9999px outline 2px solid #000000 @ 0 offset 2px | input.chakra-input.css-53h9yg 423.7x60.9 border T:1px solid #3b82f6 / R:1px solid #3b82f6 / B:1px solid #3b82f6 / L:1px solid #3b82f6 r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `signup-field-default.png`, `signup-field-focused.png`, `signup-field-filled.png`.

#### signup-submit

Sign-up submit. The filled "Sign up" submit (the "Sign up with Google" outline is signup-google); its states were measured but the button was never clicked — nothing was submitted.

Page: signup. Selector: `signup Sign up submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 423.69 x 58.88 | 415.21 x 57.7 | = | 415.21 x 57.7 |
| Padding | 29.44px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #3b82f6 | = | = | = |
| Background image | linear-gradient(60deg, #4457ff, #7583fd) | = | = | = |
| Box shadow | #596aff @ 0.28 0px 0px 35px 10px | = | none | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 14.72px/17.664px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14.72 x 14.72, colour #ffffff | 14.42 x 14.42, colour #ffffff | = | 14.42 x 14.42, colour #ffffff |
| Painted layers | button.chakra-button.css-56yz0x 423.7x58.9 bg #3b82f6 image linear-gradient(60deg, #4457ff, #7583fd) r 9999px shadow #596aff @ 0.28 0px 0px 35px 10px outline 2px solid #000000 @ 0 offset 2px | button.chakra-button.css-56yz0x 415.2x57.7 bg #3b82f6 image linear-gradient(60deg, #4457ff, #7583fd) r 9999px shadow #596aff @ 0.28 0px 0px 35px 10px outline 2px solid #000000 @ 0 offset 2px | button.chakra-button.css-56yz0x 423.7x58.9 bg #3b82f6 image linear-gradient(60deg, #4457ff, #7583fd) r 9999px outline 2px solid #000000 @ 0 offset 2px | button.chakra-button.css-56yz0x 415.2x57.7 bg #3b82f6 image linear-gradient(60deg, #4457ff, #7583fd) r 9999px shadow #596aff @ 0.28 0px 0px 35px 10px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(0.98, 0, 0, 0.98, 0, 0) | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `signup-submit-default.png`, `signup-submit-hover.png`, `signup-submit-focus-visible.png`, `signup-submit-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The phone header: FeedHive mark, the icon-only menu button and the Sign Up pill.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 76 |
| Padding | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #20232b |
| Text node | a.inline-flex.h-10: Inter 14px/21px 500, #ffffff, ls -0.28px |
| Transition | none |
| Icon | 0 x 0, colour #4f5562 |
| Painted layers | a.inline-flex.h-10 88.0x40.0 bg #4457ff r 11px; a.inline-flex.h-10 0.0x0.0 bg #f4f2f0 r 11px; a.inline-flex.h-10 0.0x0.0 bg #4457ff r 11px |
| Ancestor paint | 1 up main.min-h-screen.bg-white bg #ffffff |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-btn

Mobile menu button. The icon-only button (aria-label "Open menu") that opens the phone nav overlay — a local UI toggle; the opened state was measured after clicking it.

Page: mobile. Selector: `mobile header button[aria-label*=menu]`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = | = |
| Font | Inter 16px/24px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #17191f | = | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | default | = | = | = | = |
| Icon | 20 x 20, colour #17191f | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | button.inline-flex.h-11 44.0x44.0 outline 1px auto #e59700 offset 0px | = | = |

Crops: `m-menu-btn-default.png`, `m-menu-btn-hover.png`, `m-menu-btn-focus-visible.png`, `m-menu-btn-pressed.png`, `m-menu-btn-opened.png`.

#### m-drawer

Mobile nav overlay. The nav overlay opened by the menu button; its links were never followed.

Page: mobile. Selector: `mobile nav overlay`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fbfaf7 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #20232b |
| Text node | a.inline-flex.h-10: Inter 14px/21px 500, #272b34, ls -0.28px |
| Transition | none |
| Icon | 20 x 20, colour #17191f |
| Painted layers | div.fixed.inset-0 390.0x844.0 bg #fbfaf7; a.inline-flex.h-10 73.6x40.0 bg #f4f2f0 r 11px; a.inline-flex.h-10 88.0x40.0 bg #4457ff r 11px; div.border-t.border-[#e8e4dd] 358.0x73.0 border T:1px solid #e8e4dd; div.border-t.border-[#e8e4dd] 358.0x73.0 border T:1px solid #e8e4dd; div.border-t.border-[#e8e4dd] 358.0x73.0 border T:1px solid #e8e4dd |
| How | at rest |

Crops: `m-drawer-default.png`.

#### m-hero-h1

Mobile hero headline. The masthead at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 190.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 46px/46.92px 600 |
| Letter spacing | -1.61px |
| Colour | #23252b |
| Text node | span.block: Plus Jakarta Sans 46px/46.92px 600, #23252b, ls -1.61px |
| Transition | none |
| Icon | 25.75 x 25.75, colour #ea4b71 |
| Painted layers | span.agent-logo-badge 43.2x43.2 bg #ffffff @ 0.98 border T:1px solid #cfd3dd @ 0.9 / R:1px solid #cfd3dd @ 0.9 / B:1px solid #cfd3dd @ 0.9 / L:1px solid #cfd3dd @ 0.9 r 9.2px |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-hero-cta

Mobile hero CTA. The hero "Get started for free" button at 390 wide; measured, never followed.

Page: mobile. Selector: `mobile hero CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 196.02 x 50 | = | = | = |
| Padding | 0px 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 15px | = | = | = |
| Background | #4457ff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | Inter 15px/22.5px 500 | = | = | = |
| Letter spacing | -0.45px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.h-[50px] 196.0x50.0 bg #4457ff r 15px | = | a.inline-flex.h-[50px] 196.0x50.0 bg #4457ff r 15px outline 1px auto #e59700 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-hero-cta-default.png`, `m-hero-cta-hover.png`, `m-hero-cta-focus-visible.png`, `m-hero-cta-pressed.png`.

## Transitions declared in the readable stylesheets

feedhive.com serves its CSS same-origin as _next/static chunks, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- blog: `unset`, `initial`, `revert`, `background-size 0.25s, color 0.25s`, `stroke 0.15s`, `opacity var(--cc-modal-transition-duration)ease,visibility var(--cc-modal-transition-duration)ease,transform var(--cc-modal-transition-duration)ease`, `background-color 0.15s, border-color 0.15s, color 0.15s`, `0.15s`, `background-color 0.25s, border-color 0.25s`, `none`, `0.25s`, `transform 0.25s, background-color 0.25s`

- features: `unset`, `initial`, `revert`, `background-size 0.25s, color 0.25s`, `stroke 0.15s`, `opacity var(--cc-modal-transition-duration)ease,visibility var(--cc-modal-transition-duration)ease,transform var(--cc-modal-transition-duration)ease`, `background-color 0.15s, border-color 0.15s, color 0.15s`, `0.15s`, `background-color 0.25s, border-color 0.25s`, `none`, `0.25s`, `transform 0.25s, background-color 0.25s`

- home: `unset`, `initial`, `revert`, `background-size 0.25s, color 0.25s`, `stroke 0.15s`, `opacity var(--cc-modal-transition-duration)ease,visibility var(--cc-modal-transition-duration)ease,transform var(--cc-modal-transition-duration)ease`, `background-color 0.15s, border-color 0.15s, color 0.15s`, `0.15s`, `background-color 0.25s, border-color 0.25s`, `none`, `0.25s`, `transform 0.25s, background-color 0.25s`

- login: `opacity 0.4s`, `background-color 0.4s cubic-bezier(0.27, 1.27, 0.48, 0.56)`, `opacity 0.25s cubic-bezier(0.3, 1.2, 0.2, 1)`, `color 0.1s ease-out`, `opacity 0.2s ease-out`, `height 0.2s`, `left 0.2s, top, width, height`, `none`, `0.2s`, `opacity 0.16s, visibility linear 0.16s`, `opacity 0.16s, visibility`

- pricing: `unset`, `initial`, `revert`, `background-size 0.25s, color 0.25s`, `stroke 0.15s`, `opacity var(--cc-modal-transition-duration)ease,visibility var(--cc-modal-transition-duration)ease,transform var(--cc-modal-transition-duration)ease`, `background-color 0.15s, border-color 0.15s, color 0.15s`, `0.15s`, `background-color 0.25s, border-color 0.25s`, `none`, `0.25s`, `transform 0.25s, background-color 0.25s`

- signup: `opacity 0.4s`, `background-color 0.4s cubic-bezier(0.27, 1.27, 0.48, 0.56)`, `opacity 0.25s cubic-bezier(0.3, 1.2, 0.2, 1)`, `color 0.1s ease-out`, `opacity 0.2s ease-out`, `height 0.2s`, `left 0.2s, top, width, height`, `none`, `0.2s`, `opacity 0.16s, visibility linear 0.16s`, `opacity 0.16s, visibility`

- tools-bio: `unset`, `initial`, `revert`, `background-size 0.25s, color 0.25s`, `stroke 0.15s`, `opacity var(--cc-modal-transition-duration)ease,visibility var(--cc-modal-transition-duration)ease,transform var(--cc-modal-transition-duration)ease`, `background-color 0.15s, border-color 0.15s, color 0.15s`, `0.15s`, `background-color 0.25s, border-color 0.25s`, `none`, `0.25s`, `transform 0.25s, background-color 0.25s`

## Reduced motion

- home (`header a[href="/pricing"]` under prefers-reduced-motion): transition `color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1)`, animation `none 0s ease 0s 1 normal none running`, html scroll-behavior `smooth`
