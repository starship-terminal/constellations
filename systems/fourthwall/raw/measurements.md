# Fourthwall component measurements

Computed styles read from fourthwall.com, products.fourthwall.com, docs.fourthwall.com and help.fourthwall.com on 2026-11-16 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the public surfaces — the marketing pages' light surface and on-ink dark sections, the products catalogue, the signed-out /get-started auth shell, and the docs and help sites in light plus the dark themes their own theme controls paint — with any consent layer hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Site chrome

#### mkt-nav

Nav bar. The fixed top bar: the Fourthwall wordmark, the Features mega-menu and Learn dropdowns, Product catalog / Pricing links, Log in and the "Start now" pill.

Page: home. Selector: `nav.nav-bar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 71.03 |
| Padding | 14px 40px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16.9995px/28.0492px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | a.nav-link: Suisse Intl 16.9995px/28.0492px 450, #ffffff |
| Transition | color 0.32s ease delay 0.18s |
| Icon | 124.3 x 22, colour #ffffff |
| ::before | 1440px x 71.0312px, absolute, bg #0a0a0a, radius 0px |
| Painted layers | nav::before.nav-bar.is-warm 1440pxx71.0312px bg #0a0a0a; a::after.nav-link 89.5156pxx1px bg #ffffff; a::after.mega-link 128pxx1px bg #ffffff; a::after.mega-link 138pxx1px bg #ffffff; a::after.mega-link 199pxx1px bg #ffffff; a::after.mega-link 127pxx1px bg #ffffff |
| Ancestor paint | 1 up body bg #ffffff |
| How | at rest |

Crops: `mkt-nav-default.png`.

#### mkt-logo

Wordmark. The Fourthwall wordmark in the nav, linking home.

Page: home. Selector: `nav.nav-bar wordmark`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 124.3 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16.9995px/28.0492px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | background-color, color 0.32s, 0.32s ease, ease delay 0.18s, 0.18s |
| Cursor | pointer |
| Icon | 124.3 x 22, colour #ffffff |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-features

Mega-menu trigger. The "Features" nav item that opens the mega-menu on hover; its links were never followed.

Page: home. Selector: `.nav-bar Features`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 89.52 x 36.05 | = | = | = |
| Padding | 4px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 16.9995px/28.0492px 450 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color 0.32s, 0.32s ease, ease delay 0.18s, 0.18s | none | none | = |
| Cursor | pointer | = | = | = |
| Icon | 12.58 x 8.48, colour #ffffff, fill #000000 | = | = | = |
| ::after | 89.5156px x 1px, absolute, bg #ffffff, radius 0px | = | = | = |
| Painted layers | a::after.nav-link 89.5156pxx1px bg #ffffff | = | a.nav-link 89.5x36.0 outline 1px auto #101010 offset 1px; a::after.nav-link 89.5156pxx1px bg #ffffff | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| ::before | - | 137.516px x 22px, absolute, bg #000000 @ 0, radius 0px | = | = |

Crops: `nav-features-default.png`, `nav-features-hover.png`, `nav-features-focus-visible.png`, `nav-features-pressed.png`.

#### nav-link

Nav link. A marketing nav link (Pricing); measured, never followed.

Page: home. Selector: `.nav-bar Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56 x 36.05 | = | = | = |
| Padding | 4px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 16.9995px/28.0492px 450 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color 0.32s, 0.32s ease, ease delay 0.18s, 0.18s | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 56px x 1px, absolute, bg #ffffff, radius 0px | = | = | = |
| Painted layers | a::after.nav-link 56pxx1px bg #ffffff | = | a.nav-link 56.0x36.0 outline 1px auto #101010 offset 1px; a::after.nav-link 56pxx1px bg #ffffff | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Log in link. The "Log in" nav link to the shop admin; measured, never followed.

Page: home. Selector: `.nav-bar Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 49 x 36.05 | = | = | = |
| Padding | 4px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 16.9995px/28.0492px 450 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color 0.32s, 0.32s ease, ease delay 0.18s, 0.18s | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 49px x 1px, absolute, bg #ffffff, radius 0px | = | = | = |
| Painted layers | a::after.nav-login 49pxx1px bg #ffffff | = | a.nav-login 49.0x36.0 outline 1px auto #101010 offset 1px; a::after.nav-login 49pxx1px bg #ffffff | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### mega-clip

Mega-menu panel. The Features mega-menu panel — nav columns plus featured cards; opened by hovering its own trigger.

Page: home. Selector: `.mega-clip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 431.08 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16.9995px/28.0492px 450 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Painted layers | a::after.mega-link 128pxx1px bg #ffffff; a::after.mega-link 138pxx1px bg #ffffff; a::after.mega-link 199pxx1px bg #ffffff; a::after.mega-link 127pxx1px bg #ffffff; a::after.mega-link 119pxx1px bg #ffffff; a::after.mega-link 102pxx1px bg #ffffff |
| How | at rest |

Crops: `mega-clip-default.png`.

#### nav-cta

Start now button. The "Start now" pill in the nav — it links to /get-started; measured, never activated.

Page: home. Selector: `.nav-bar a.btn-primary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 116 x 43.03 | = | = | = |
| Padding | 12px 20px | = | = | = |
| Gap | normal 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 16.9995px/28.0492px 450 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Text node | p.btn-text-inner: Suisse Intl 16.9995px/19.0395px 450, #0a0a0a | = | = | = |
| Transition | background-color, color 0.32s, 0.32s ease, ease delay 0.18s, 0.18s | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 116px x 1px, absolute, bg #0a0a0a, radius 0px | = | = | = |
| Painted layers | a.btn-primary.w-variant-3c14d31e-ca3b-dd80-2979-4788e8e158f8 116.0x43.0 bg #ffffff r 12px; a::after.btn-primary.w-variant-3c14d31e-ca3b-dd80-2979-4788e8e158f8 116pxx1px bg #0a0a0a | = | a.btn-primary.w-variant-3c14d31e-ca3b-dd80-2979-4788e8e158f8 116.0x43.0 bg #ffffff r 12px outline 1px auto #101010 offset 1px; a::after.btn-primary.w-variant-3c14d31e-ca3b-dd80-2979-4788e8e158f8 116pxx1px bg #0a0a0a | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### mega-card

Mega-menu card. A .mega-card tile inside the Features mega-menu (Get inspired / Designers / Help / Blog); measured with the menu open, never followed. The tiles compute visibility:hidden until a Webflow reveal — earlier passes read mid-reveal or before it; the settle wait lets it paint.

Page: home. Selector: `a.mega-card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 316 x 325.98 |
| Padding | 4px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16.9995px/28.0492px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | text-decoration-color, color 0.2s, 0.2s ease, ease |
| Cursor | pointer |
| Painted layers | div.mega-card-img 316.0x210.7 bg #ffffff @ 0.07 |
| How | at rest |

Crops: `mega-card-default.png`.

### Home

#### hero-h1

Hero headline. "One platform for premium products and branded shops." — the display masthead.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1008 x 181.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 57.6px/60.48px 420 |
| Letter spacing | -1.152px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-sub

Hero lede. The hero standfirst under the masthead.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 300 x 49.28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16.9995px/24.6493px 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.5 |
| Transition | color 0.2s ease |
| Cursor | pointer |
| How | at rest |

Crops: `hero-sub-default.png`.

#### tile

Product tile. A .ph-tile product/showcase tile in the home scatter grid (product card with hover-swap imagery).

Page: home. Selector: `a.ph-tile`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 336.88 x 428.31 | = |
| Padding | 24px | = |
| Gap | 12px normal | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #f6f6f6 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 16.9995px/28.0492px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Text node | div.ph-tile-rating.ph-tile-rating--flat: Suisse Intl 12px/12px 500, #0a0a0a | = |
| Transition | opacity, transform 1.8s, 1.8s cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1) | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = |
| Cursor | pointer | = |
| Painted layers | a.ph-tile.ph-tile--product 336.9x428.3 bg #f6f6f6; div.ph-tile-rating.ph-tile-rating--flat 50.0x20.0 bg #ffffff r 999px | = |
| How | at rest | mouse hover |

Crops: `tile-default.png`, `tile-hover.png`.

#### rating-card

Rating chip. The star-rating chip inside a product tile (rating + price).

Page: home. Selector: `.ph-tile-rating`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 50 x 20 |
| Padding | 4px 10px 4px 8px |
| Gap | normal 4px |
| Border | none |
| Radius | 999px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 12px/12px 500 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Transition | none |
| Cursor | pointer |
| ::before | 10px x 11.4062px, static, bg #000000 @ 0, radius 0px |
| Painted layers | div.ph-tile-rating.ph-tile-rating--flat 50.0x20.0 bg #ffffff r 999px |
| Ancestor paint | 1 up a.ph-tile.ph-tile--product bg #f6f6f6 |
| How | at rest |

Crops: `rating-card-default.png`.

#### brand-grid

Logo wall. The .ws--trusted "trusted by" section — the creator/company logo wall.

Page: home. Selector: `.ws--trusted`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 444.05 |
| Padding | 88px 40px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16.9995px/28.0492px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | h2.heading-quiet: Suisse Intl 16.9995px/28.0492px 400, #0a0a0a @ 0.6 |
| Transition | none |
| Painted layers | section.page-section.is-editorial 1440.0x444.0 bg #ffffff |
| Ancestor paint | 1 up div.page-content bg #ffffff |
| How | at rest |

Crops: `brand-grid-default.png`.

#### design-preview

Design preview carousel. The storefront design-preview carousel in the .on-ink design section.

Page: home. Selector: `.design-preview`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 516 x 619.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16.9995px/28.0492px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Transition | opacity, transform 1.8s, 1.8s cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1) delay 0.15s |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `design-preview-default.png`.

#### hero-cta

Hero CTA. The primary "Start now" hero action — the only hero action; measured, never followed.

Page: home. Selector: `.hero-cta-row a.btn-primary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 132 x 55.03 | = | = | = |
| Padding | 18px 28px | = | = | = |
| Gap | normal 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 16.9995px/28.0492px 450 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Text node | p.btn-text-inner: Suisse Intl 16.9995px/19.0395px 450, #0a0a0a | = | = | = |
| Transition | color, text-decoration-color 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn-primary.w-inline-block 132.0x55.0 bg #ffffff r 12px | = | a.btn-primary.w-inline-block 132.0x55.0 bg #ffffff r 12px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

### On-ink (dark sections)

#### leg-section

Dark feature section. A .page-section.on-ink dark band — the sheet's own on-ink scope class repaints the --_surface---* variables; measured as painted, no theme toggle exists.

Page: home. Selector: `.page-section.on-ink`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1355.89 |
| Padding | 140px 40px |
| Border | none |
| Radius | 0px |
| Background | #0a0a0a |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16.9995px/28.0492px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | h2.heading-h1: Saans 57.6px/60.48px 420, #ffffff, ls -1.152px |
| Transition | none |
| Icon | 9 x 9, colour #ffffff, fill #000000 |
| Painted layers | section.page-section.is-editorial 1440.0x1355.9 bg #0a0a0a; div.design-mockup-slide 518.0x619.2 bg #0a0a0a; div.design-mockup-slide 518.0x619.2 bg #0a0a0a; div.design-mockup-slide 518.0x619.2 bg #0a0a0a; div.design-canvas 278.6x167.2 image repeating-linear-gradient(90deg, #ffffff 0px, #ffffff 5px, #000000 @ 0 5px, #000000 @ 0 11; div.design-tool-bar.design-tool-bar--ai 82.8x37.9 bg #ffffff r 15.738px |
| Ancestor paint | 1 up div.page-content bg #ffffff |
| How | at rest |

Crops: `leg-section-default.png`.

#### wordmark-section

Wordmark section. The dark "Made with Fourthwall" wordmark band — on-ink surface values.

Page: home. Selector: `.wordmark-section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 456.75 |
| Padding | 80px 40px 40px 40px |
| Border | none |
| Radius | 0px |
| Background | #0a0a0a |
| Box shadow | #0a0a0a 0px -4px 0px 0px |
| Outline | none |
| Font | Suisse Intl 16.9995px/28.0492px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span: Suisse Intl 16.9995px/28.0492px 400, #ffffff @ 0.5 |
| Transition | none |
| Icon | 1360 x 240.7, colour #ffffff |
| Painted layers | section.wordmark-section 1440.0x456.8 bg #0a0a0a shadow #0a0a0a 0px -4px 0px 0px; a::after.footer-bottom-link 181pxx1px bg #ffffff @ 0.5; a::after.footer-bottom-link 132pxx1px bg #ffffff @ 0.5; a::after.footer-bottom-link 109pxx1px bg #ffffff @ 0.5; a::after.footer-bottom-link 204pxx1px bg #ffffff @ 0.5 |
| Ancestor paint | 1 up body bg #ffffff |
| How | at rest |

Crops: `wordmark-section-default.png`.

#### closer

Closing CTA section. The closing "Make something worth buying / Start now for free" section.

Page: home. Selector: `.closer-section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 512.8 |
| Padding | 40px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | #0a0a0a |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16.9995px/28.0492px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | a.closer-link: Saans 57.6px/60.48px 420, #ffffff, ls -1.152px |
| Transition | none |
| Cursor | pointer |
| ::before | 1440px x 512.797px, absolute, bg #ad0132, radius 0px |
| Painted layers | section.closer-section 1440.0x512.8 bg #0a0a0a; section::before.closer-section 1440pxx512.797px bg #ad0132; div.g1 948.5x337.8 image radial-gradient(circle, #e84678 @ 0.8 0px, #e84678 @ 0 50%); div.g2 1172.3x417.5 image radial-gradient(circle, #960a37 @ 0.8 0px, #960a37 @ 0 50%); div.g3 1193.5x425.0 image radial-gradient(circle, #c61c4e @ 0.8 0px, #c61c4e @ 0 50%); div.g4 1357.8x483.5 image radial-gradient(circle, #46041e @ 0.8 0px, #46041e @ 0 50%) |
| Ancestor paint | 1 up main.site-main bg #0a0a0a |
| How | at rest |

Crops: `closer-default.png`.

#### made-with

Made-with band. The .made-with "Made with Fourthwall" storefront showcase band — on-ink surface values.

Page: home. Selector: `.made-with`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1067.19 |
| Padding | 140px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | #0a0a0a |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16.9995px/28.0492px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.heading-h1.reveal: Saans 57.6px/60.48px 420, #ffffff, ls -1.152px |
| Transition | none |
| Cursor | grab |
| Painted layers | section.made-with 1440.0x1067.2 bg #0a0a0a; div.tile-inner 397.8x251.7 bg #141414; div.tile-inner 349.6x257.4 bg #141414; div::after.tile-inner 397.797pxx251.547px shadow #ffffff @ 0.1 0px 0px 0px 1px inset; div.tile-inner 235.2x246.4 bg #141414; div.tile-inner 109.4x223.5 bg #141414 |
| Ancestor paint | 1 up div.page-content bg #ffffff |
| How | at rest |

Crops: `made-with-default.png`.

#### closer-cta

Closer CTA. The giant "Make something worth buying" word-link in the closing section — it carries the start flow; measured, never followed.

Page: home. Selector: `.closer-section a.closer-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 412.88 x 135.47 | 429.42 x 140.88 | 429.34 x 140.87 | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Saans 57.6px/60.48px 420 | = | = | = |
| Letter spacing | -1.152px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, text-decoration-color 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.closer-link 429.3x140.9 outline 1px auto #101010 offset 1px | = |

Crops: `closer-cta-default.png`, `closer-cta-hover.png`, `closer-cta-focus-visible.png`, `closer-cta-pressed.png`.

### Footer

#### footer

Footer. The .site-footer.is-warm footer — sitemap columns, social and legal links on the ink surface.

Page: home. Selector: `footer.site-footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 362.33 |
| Padding | 56px 40px 32px 40px |
| Border | none |
| Radius | 0px |
| Background | #0a0a0a |
| Box shadow | #0a0a0a 0px 4px 0px 0px |
| Outline | none |
| Font | Suisse Intl 16.9995px/28.0492px 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.5 |
| Text node | h3.footer-col-title: Suisse Intl 16.9995px/28.0492px 400, #ffffff |
| Transition | none |
| Painted layers | footer.site-footer.is-warm 1440.0x362.3 bg #0a0a0a shadow #0a0a0a 0px 4px 0px 0px; a::after.footer-link 128pxx1px bg #ffffff @ 0.5; a::after.footer-link 51pxx1px bg #ffffff @ 0.5; a::after.footer-link 99pxx1px bg #ffffff @ 0.5; a::after.footer-link 111pxx1px bg #ffffff @ 0.5; a::after.footer-link 55pxx1px bg #ffffff @ 0.5 |
| Ancestor paint | 1 up body bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer sitemap link; measured, never followed.

Page: home. Selector: `footer Pricing link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 55 x 28.05 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 16.9995px/28.0492px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.5 | #ffffff @ 0.9 | = | #ffffff |
| Transition | color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 55px x 1px, absolute, bg #ffffff @ 0.5, radius 0px | 55px x 1px, absolute, bg #ffffff @ 0.9, radius 0px | = | 55px x 1px, absolute, bg #ffffff, radius 0px |
| Painted layers | a::after.footer-link 55pxx1px bg #ffffff @ 0.5 | a::after.footer-link 55pxx1px bg #ffffff @ 0.9 | a.footer-link 55.0x28.0 outline 1px auto #101010 offset 1px; a::after.footer-link 55pxx1px bg #ffffff @ 0.5 | a::after.footer-link 55pxx1px bg #ffffff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Pricing

#### price-h1

Pricing headline. The /pricing masthead.

Page: pricing. Selector: `pricing h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 968 x 60.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 57.6px/60.48px 420 |
| Letter spacing | -1.152px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `price-h1-default.png`.

#### billing-toggle

Billing toggle. The "Pay yearly / Pay monthly" toggle — the monthly state was painted by clicking it (a local UI toggle; Pro reads $19 vs $15).

Page: pricing. Selector: `.billing-toggle`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 290 x 48 |
| Padding | 4px |
| Gap | normal 2px |
| Border | none |
| Radius | 999px |
| Background | #ffffff @ 0.1 |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16.9995px/28.0492px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | p.billing-toggle-text: Suisse Intl 16px/16px 500, #0a0a0a |
| Transition | none |
| Painted layers | div.billing-toggle 290.0x48.0 bg #ffffff @ 0.1 r 999px; div.billing-toggle-thumb 140.0x40.0 bg #ffffff r 999px |
| How | at rest |

Crops: `billing-toggle-default.png`.

#### billing-btn

Billing option. The "Pay monthly" toggle button; measured, and clicked once to paint the monthly state.

Page: pricing. Selector: `.billing-toggle-btn monthly`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140 x 40 | = | = | = |
| Padding | 12px 18px | = | = | = |
| Gap | normal 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Suisse Intl 16.9995px/28.0492px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.5 | #ffffff | = | #ffffff |
| Text node | p.billing-toggle-text: Suisse Intl 16px/16px 500, #ffffff @ 0.5 | p.billing-toggle-text: Suisse Intl 16px/16px 500, #ffffff | = | p.billing-toggle-text: Suisse Intl 16px/16px 500, #ffffff |
| Transition | color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.billing-toggle bg #ffffff @ 0.1 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.billing-toggle-btn 140.0x40.0 r 999px outline 1px auto #101010 offset 0px | = |

Crops: `billing-btn-default.png`, `billing-btn-hover.png`, `billing-btn-focus-visible.png`, `billing-btn-pressed.png`.

#### plan-card

Plan card. A plan card on /pricing (Free / Pro) — one .plan-card cell inside the .pricing-plans grid.

Page: pricing. Selector: `.pricing-plans .plan-card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 544 x 613.53 | = |
| Padding | 40px | = |
| Gap | 24px normal | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #18181b | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 16.9995px/28.0492px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Text node | p.plan-price: Saans 34.56px/36.288px 435, #ffffff, ls -0.3456px | = |
| Transition | opacity, translate, transform 1.1s, 1.1s, 0.4s cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1) delay 0.26s, 0.26s, 0s | transform 0.32s cubic-bezier(0.16, 1, 0.3, 1) |
| Icon | 18 x 18, colour #ffffff | = |
| ::before | 870.375px x 981.625px, absolute, bg #000000 @ 0 radial-gradient(circle at 50% 50%, #ffffff @ 0.086 0px, #000000 @ 0 58%), radius 0px | = |
| ::after | 870.375px x 981.625px, absolute, bg #000000 @ 0 radial-gradient(circle at 50% 50%, #ffffff @ 0.055 0px, #000000 @ 0 58%), radius 0px | = |
| Painted layers | div.plan-card.reveal 544.0x613.5 bg #18181b; div::before.plan-card.reveal 870.375pxx981.625px image radial-gradient(circle at 50% 50%, #ffffff @ 0.086 0px, #000000 @ 0 58%); div::after.plan-card.reveal 870.375pxx981.625px image radial-gradient(circle at 50% 50%, #ffffff @ 0.055 0px, #000000 @ 0 58%); div.plan-divider 464.0x1.0 bg #ffffff @ 0.12; a.btn-primary.w-variant-3f51f10e-51a2-5720-f2c2-15f30fbb69ef 464.0x55.0 bg #ffffff r 12px | = |
| How | at rest | mouse hover |
| Transform | - | matrix(1, 0, 0, 1, 0, 0) |

Crops: `plan-card-default.png`, `plan-card-hover.png`.

#### plan-row

Plan feature row. A .plan-feature row inside a plan card's .plan-features list.

Page: pricing. Selector: `.plan-card .plan-feature`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 464 x 24.64 |
| Padding | 0px |
| Gap | normal 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16.9995px/24.6493px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.plan-feature-text: Suisse Intl 16.9995px/24.6493px 400, #ffffff |
| Transition | none |
| Icon | 18 x 18, colour #ffffff |
| How | at rest |

Crops: `plan-row-default.png`.

#### faq-summary

FAQ disclosure. A disclosure button in the pricing FAQ; the opened state was measured after clicking it (a local UI toggle).

Page: pricing. Selector: `.ph-faq-summary`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 800 x 69 | = | = | = | = |
| Padding | 20px 24px | = | = | = | = |
| Gap | normal 16px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = | = |
| Font | Suisse Intl 16.9995px/normal 450 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #0a0a0a | = | = | = | = |
| Text node | div: Suisse Intl 16.9995px/normal 450, #0a0a0a | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | div::before.ph-faq-icon 14pxx1.5px bg #0a0a0a @ 0.6; div::after.ph-faq-icon 14pxx1.5px bg #0a0a0a @ 0.6 | = | button.ph-faq-summary 800.0x69.0 outline 1px auto #101010 offset 0px; div::before.ph-faq-icon 14pxx1.5px bg #0a0a0a @ 0.6; div::after.ph-faq-icon 14pxx1.5px bg #0a0a0a @ 0.6 | = | = |
| Ancestor paint | 1 up div.ph-faq-item bg #f6f6f6 | 1 up div.ph-faq-item bg #efeff0 | = | = | 1 up div.ph-faq-item.is-open bg #efeff0 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | clicked the FAQ summary to expand its answer |

Crops: `faq-summary-default.png`, `faq-summary-hover.png`, `faq-summary-focus-visible.png`, `faq-summary-pressed.png`, `faq-summary-opened.png`.

### Blog

#### blog-h1

Blog headline. The /blog masthead.

Page: blog. Selector: `blog h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 434.41 x 121 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 110px/121px 400 |
| Letter spacing | -2.2px |
| Colour | #0a0a0a |
| Transition | none |
| How | at rest |

Crops: `blog-h1-default.png`.

#### blog-card

Post card. A post card on the blog index; measured, never followed.

Page: blog. Selector: `blog post card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1240 x 430.53 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 16.9995px/28.0492px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Transition | color, text-decoration-color 0.2s, 0.2s ease, ease delay 0s, 0s | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `blog-card-default.png`, `blog-card-hover.png`.

#### blog-news

Newsletter field. The newsletter email input on /blog; focused and typed into then cleared — never subscribed.

Page: blog. Selector: `blog email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 488 x 56 | = | = |
| Padding | 12px 9px 12px 16px | = | = |
| Border | 1px solid #b5b3b0 | = | = |
| Radius | 12px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Suisse Intl 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #212d3a | = | = |
| Transition | box-shadow 0.2s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #6e6e68, opacity 1 | = | = |
| Painted layers | input.hsfc-TextInput 488.0x56.0 bg #ffffff border T:1px solid #b5b3b0 / R:1px solid #b5b3b0 / B:1px solid #b5b3b0 / L:1px solid #b5b3b0 r 12px | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `blog-news-default.png`, `blog-news-focused.png`, `blog-news-filled.png`.

### Compare

#### cmp-h1

Compare headline. The /compare masthead.

Page: compare. Selector: `compare h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1360 x 60.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 57.6px/60.48px 420 |
| Letter spacing | -1.152px |
| Colour | #0a0a0a |
| Transition | none |
| How | at rest |

Crops: `cmp-h1-default.png`.

#### cmp-search

Platform search. The "Compare Fourthwall to…" search field; focused and typed into then cleared — a local filter, nothing sent.

Page: compare. Selector: `.cmp-search input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 152 x 24.63 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Suisse Intl 16.9995px/24.6493px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0a0a0a | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #0a0a0a @ 0.6, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "shopify", then deleted; nothing sent |

Crops: `cmp-search-default.png`, `cmp-search-focused.png`, `cmp-search-filled.png`.

#### cmp-card

Comparison card. A comparison card linking to a vs-page (Shopify, Patreon…); measured, never followed.

Page: compare. Selector: `compare card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1360 x 161.44 | = |
| Padding | 32px 0px | = |
| Gap | 24px 48px | = |
| Border | T: none; R: none; B: 1px solid #0a0a0a @ 0.16; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 16.9995px/28.0492px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Text node | h2.body-fluid-lg.cmp-title: Saans 20.9995px/28.3493px 465, #0a0a0a | = |
| Transition | opacity, transform 1.1s, 1.1s cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1) delay 0s, 0s | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = |
| Cursor | pointer | = |
| Painted layers | a.cmp-row.reveal 1360.0x161.4 border B:1px solid #0a0a0a @ 0.16; div::before.btn-secondary 187pxx55.0312px bg #0a0a0a @ 0.06 r 12px; div::after.btn-secondary 187pxx55.0312px bg #0a0a0a @ 0.11 r 12px | = |
| How | at rest | mouse hover |

Crops: `cmp-card-default.png`, `cmp-card-hover.png`.

### Comparison page

#### cmpart-h1

Vs-page headline. The "Fourthwall vs Shopify" masthead.

Page: cmparticle. Selector: `cmparticle h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 683.05 x 60.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 57.6px/60.48px 420 |
| Letter spacing | -1.152px |
| Colour | #0a0a0a |
| Transition | none |
| How | at rest |

Crops: `cmpart-h1-default.png`.

#### cmpart-card

Vs comparison card. A "Choose X if" card in the .cmp2-pair comparison on a vs-page.

Page: cmparticle. Selector: `.cmp2-pair .plan-card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 544 x 604.75 |
| Padding | 40px |
| Gap | 24px normal |
| Border | none |
| Radius | 0px |
| Background | #18161d |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16.9995px/28.0492px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | h3: Saans 28.8px/32.256px 435, #ffffff |
| Transition | transform 0.9s cubic-bezier(0.16, 1, 0.3, 1) |
| ::before | 870.375px x 967.594px, absolute, bg #000000 @ 0 radial-gradient(circle at 50% 50%, #8a4494 @ 0.3 0px, #000000 @ 0 58%), radius 0px |
| ::after | 870.375px x 967.594px, absolute, bg #000000 @ 0 radial-gradient(circle at 50% 50%, #4a3ac8 @ 0.25 0px, #000000 @ 0 58%), radius 0px |
| Painted layers | div.plan-card.plan-card--pro 544.0x604.8 bg #18161d; div::before.plan-card.plan-card--pro 870.375pxx967.594px image radial-gradient(circle at 50% 50%, #8a4494 @ 0.3 0px, #000000 @ 0 58%); div::after.plan-card.plan-card--pro 870.375pxx967.594px image radial-gradient(circle at 50% 50%, #4a3ac8 @ 0.25 0px, #000000 @ 0 58%); li::before 16.9844pxx16.9844px bg #ffffff; li::before 16.9844pxx16.9844px bg #ffffff; li::before 16.9844pxx16.9844px bg #ffffff |
| How | at rest |

Crops: `cmpart-card-default.png`.

### Shops

#### shops-h1

Shops headline. The /shops masthead.

Page: shops. Selector: `shops h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 968 x 60.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 57.6px/60.48px 420 |
| Letter spacing | -1.152px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `shops-h1-default.png`.

#### shops-tile

Shop tile. An example-shop card on /shops (.brand-card showcase / .pg-card grid); measured, never followed.

Page: shops. Selector: `a.brand-card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 432 x 475.31 | = |
| Padding | 0px | = |
| Gap | 24px normal | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 16.9995px/28.0492px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Text node | span: Saans 20.9995px/30.4493px 450, #0a0a0a | = |
| Transition | opacity, transform 1.8s, 1.8s cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1) | = |
| Transform | matrix(1, 0, 0, 1, 0, 56) | matrix(1, 0, 0, 1, 0, 0) |
| Opacity | 0 | - |
| Cursor | pointer | = |
| Painted layers | div.brand-card-box.card-grid-box 432.0x360.0 bg #f6f6f6 | = |
| How | at rest | mouse hover |

Crops: `shops-tile-default.png`, `shops-tile-hover.png`.

### Get inspired

#### insp-h1

Get-inspired headline. The /get-inspired masthead.

Page: inspired. Selector: `inspired h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 968 x 60.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 57.6px/60.48px 420 |
| Letter spacing | -1.152px |
| Colour | #0a0a0a |
| Transition | none |
| How | at rest |

Crops: `insp-h1-default.png`.

#### insp-card

Creator card. An .ex-tile creator/showcase card on /get-inspired; measured, never followed.

Page: inspired. Selector: `a.ex-tile`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 432 x 358.94 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 16.9995px/28.0492px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Text node | p.body-fluid-md.ex-tile-name: Saans 16.9995px/22.9494px 465, #0a0a0a | = |
| Transition | color, text-decoration-color 0.2s, 0.2s ease, ease delay 0s, 0s | = |
| Cursor | pointer | = |
| ::before | 432px x 324px, absolute, bg #000000 @ 0, radius 0px | = |
| Painted layers | img.ex-tile-img.is-loaded 432.0x324.0 border T:1px solid #0a0a0a @ 0.11 / R:1px solid #0a0a0a @ 0.11 / B:1px solid #0a0a0a @ 0.11 / L:1px solid #0a0a0a @ 0.11 | = |
| How | at rest | mouse hover |

Crops: `insp-card-default.png`, `insp-card-hover.png`.

### Contact

#### contact-h1

Contact headline. The /contact masthead.

Page: contact. Selector: `contact h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 968 x 60.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 57.6px/60.48px 420 |
| Letter spacing | -1.152px |
| Colour | #0a0a0a |
| Transition | none |
| How | at rest |

Crops: `contact-h1-default.png`.

#### contact-card

Contact card. An a.contact-card on /contact (Contact support / Contact sales); measured, never followed.

Page: contact. Selector: `a.contact-card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 316 x 355.14 | = |
| Padding | 0px | = |
| Gap | 16px normal | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 16.9995px/28.0492px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Text node | p.body-fluid-lg.contact-card-title: Saans 20.9995px/28.3493px 465, #0a0a0a | = |
| Transition | color, text-decoration-color 0.2s, 0.2s ease, ease delay 0s, 0s | = |
| Cursor | pointer | = |
| Painted layers | div.contact-card-img 316.0x210.7 bg #0a0a0a @ 0.06 | = |
| How | at rest | mouse hover |

Crops: `contact-card-default.png`, `contact-card-hover.png`.

### Signup (auth shell)

#### auth-card

Auth card. The signed-out auth surface at /get-started (auth.fourthwall.com, Keycloak on the catalogue DS) — the panel holding the Google/Apple/email choices; measured at rest, nothing pressed.

Page: signup. Selector: `auth card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 440 x 176 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Int'l 16px/normal 400 |
| Letter spacing | normal |
| Colour | #161712 |
| Text node | span.sc-jIZahI.kGlnAy: Suisse Int'l 16px/24px 500, #161712 |
| Transition | none |
| Icon | 21 x 20, colour #161712 |
| Painted layers | a.sc-kLLXSa.ioAyRT 440.0x48.0 bg #f2f2f2 r 8px; a.sc-kLLXSa.ioAyRT 440.0x48.0 bg #f2f2f2 r 8px; a.sc-kLLXSa.ioAyRT 440.0x48.0 bg #f2f2f2 r 8px |
| How | at rest |

Crops: `auth-card-default.png`.

#### auth-google

Google provider. The "Continue with Google" provider button; states measured, never pressed — no OAuth flow was started.

Page: signup. Selector: `auth Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 440 x 48 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #f2f2f2 | #eaeae9 | = | #e1e0df |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #161712 offset 2px | = |
| Font | Suisse Int'l 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161712 | = | = | = |
| Text node | span.sc-jIZahI.kGlnAy: Suisse Int'l 16px/24px 500, #161712 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 21 x 20, colour #161712 | = | = | = |
| Painted layers | a.sc-kLLXSa.ioAyRT 440.0x48.0 bg #f2f2f2 r 8px | a.sc-kLLXSa.ioAyRT 440.0x48.0 bg #eaeae9 r 8px | a.sc-kLLXSa.ioAyRT 440.0x48.0 bg #f2f2f2 r 8px outline 2px solid #161712 offset 2px | a.sc-kLLXSa.ioAyRT 440.0x48.0 bg #e1e0df r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `auth-google-default.png`, `auth-google-hover.png`, `auth-google-focus-visible.png`, `auth-google-pressed.png`.

#### auth-apple

Apple provider. The "Continue with Apple" provider button; measured, never pressed.

Page: signup. Selector: `auth Apple`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 440 x 48 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #f2f2f2 | #eaeae9 | = | #e1e0df |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #161712 offset 2px | = |
| Font | Suisse Int'l 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161712 | = | = | = |
| Text node | span.sc-jIZahI.kGlnAy: Suisse Int'l 16px/24px 500, #161712 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 20, colour #161712 | = | = | = |
| Painted layers | a.sc-kLLXSa.ioAyRT 440.0x48.0 bg #f2f2f2 r 8px | a.sc-kLLXSa.ioAyRT 440.0x48.0 bg #eaeae9 r 8px | a.sc-kLLXSa.ioAyRT 440.0x48.0 bg #f2f2f2 r 8px outline 2px solid #161712 offset 2px | a.sc-kLLXSa.ioAyRT 440.0x48.0 bg #e1e0df r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `auth-apple-default.png`, `auth-apple-hover.png`, `auth-apple-focus-visible.png`, `auth-apple-pressed.png`.

#### auth-email

Email provider. The "Continue with email" action; measured, never pressed.

Page: signup. Selector: `auth email`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 440 x 48 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #f2f2f2 | #eaeae9 | = | #e1e0df |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #161712 offset 2px | = |
| Font | Suisse Int'l 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161712 | = | = | = |
| Text node | span.sc-jIZahI.kGlnAy: Suisse Int'l 16px/24px 500, #161712 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #161712 | = | = | = |
| Painted layers | a.sc-kLLXSa.ioAyRT 440.0x48.0 bg #f2f2f2 r 8px | a.sc-kLLXSa.ioAyRT 440.0x48.0 bg #eaeae9 r 8px | a.sc-kLLXSa.ioAyRT 440.0x48.0 bg #f2f2f2 r 8px outline 2px solid #161712 offset 2px | a.sc-kLLXSa.ioAyRT 440.0x48.0 bg #e1e0df r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `auth-email-default.png`, `auth-email-hover.png`, `auth-email-focus-visible.png`, `auth-email-pressed.png`.

#### auth-login

Login link. The "Log in" link on the signup surface; measured, never followed.

Page: signup. Selector: `auth login link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 42 x 28 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Int'l 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161712 | = | = | #6e6e68 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.sc-gicCDH.fjjreh 42.0x28.0 outline 1px auto #101010 offset 1px | = |

Crops: `auth-login-default.png`, `auth-login-hover.png`, `auth-login-focus-visible.png`, `auth-login-pressed.png`.

### Product catalogue

#### cat-nav

Catalogue nav. The products.fourthwall.com top bar — logo, category tabs, search, Log in / Sign up.

Page: catalog. Selector: `catalog header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 551 x 50.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Int'l 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #161712 |
| Text node | span.sc-9ae1efd9-1.ePbzzw: Suisse Int'l 16px/18.4px 500, #161712 |
| Transition | none |
| Painted layers | span::after.sc-9ae1efd9-1.ePbzzw 69pxx2px bg #161712 |
| How | at rest |

Crops: `cat-nav-default.png`.

#### cat-search

Catalogue search. The catalogue search field — a bare input[type=text] in the nav; focused and typed into then cleared — a local filter, nothing sent.

Page: catalog. Selector: `catalog search`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 218 x 38 | 638 x 48 | 638 x 48 |
| Padding | 0px 14px 0px 41px | = | 0px 41px |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Suisse Int'l 16px/38px 400 | Suisse Int'l 16px/48px 400 | Suisse Int'l 16px/48px 400 |
| Letter spacing | normal | = | = |
| Colour | #161712 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #161712, opacity 1 | #757575, opacity 1 | #757575, opacity 1 |
| How | at rest | clicked into the field | typed "hoodie", then deleted; nothing sent |

Crops: `cat-search-default.png`, `cat-search-focused.png`, `cat-search-filled.png`.

#### quiz-card

Quiz card. The "What are you looking for?" product-finder card on the catalogue home.

Page: catalog. Selector: `catalog quiz card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1344 x 907.45 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Int'l 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #161712 |
| Text node | p.sc-1ab47563-2.iZxvGx: Suisse Int'l 14px/21px 400, #6e6e68, ls 0.1px |
| Transition | none |
| Icon | 20 x 20, colour #161712 |
| Painted layers | div.sc-a30299a3-0.UwkhN 1344.0x262.0 bg #ffffff border T:1px solid #e1e0df / R:1px solid #e1e0df / B:1px solid #e1e0df / L:1px solid #e1e0df r 8px; button.sc-d64fc78e-2.gsJhKO 639.0x137.0 bg #f2f2f2 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px; button.sc-d64fc78e-2.gsJhKO 639.0x137.0 bg #f2f2f2 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px; span.sc-b35ada23-0.dVXGnN 77.0x22.0 bg #161712 border T:1px solid #000000 @ 0.12 / R:1px solid #000000 @ 0.12 / B:1px solid #000000 @ 0.12 / L:1px solid #000000 @ 0.12 r 100px; span.sc-b35ada23-0.dxxQXx 70.0x22.0 bg #ffffff border T:1px solid #000000 @ 0.12 / R:1px solid #000000 @ 0.12 / B:1px solid #000000 @ 0.12 / L:1px solid #000000 @ 0.12 r 100px; div.sc-fd6960c6-4.jtbKar 58.0x24.0 border T:1px solid #b5b3b0 / R:1px solid #b5b3b0 / B:1px solid #b5b3b0 / L:1px solid #b5b3b0 r 8px |
| How | at rest |

Crops: `quiz-card-default.png`.

#### quiz-option

Quiz option. A product-finder answer chip; clicking selects it locally (the quiz needs more steps before recommending) — nothing is submitted.

Page: catalog. Selector: `catalog quiz option`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 639 x 137 | = | = | = |
| Padding | 24px | = | = | = |
| Gap | 16px | = | = | = |
| Border | 2px solid #000000 @ 0 | = | = | 2px solid #161712 |
| Radius | 8px | = | = | = |
| Background | #f2f2f2 | = | = | #e1e0df |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Suisse Int'l 16px/18.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161712 | = | = | = |
| Text node | h3.sc-d64fc78e-4.kkgGyN: Suisse Int'l 16px/24px 500, #161712 | = | = | = |
| Transition | border-color, background-color 0.1s, 0.1s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #161712 | = | = | = |
| Painted layers | button.sc-d64fc78e-2.gsJhKO 639.0x137.0 bg #f2f2f2 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px | = | button.sc-d64fc78e-2.gsJhKO 639.0x137.0 bg #f2f2f2 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px outline 1px auto #101010 offset 0px | button.sc-d64fc78e-2.gsJhKO 639.0x137.0 bg #e1e0df border T:2px solid #161712 / R:2px solid #161712 / B:2px solid #161712 / L:2px solid #161712 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `quiz-option-default.png`, `quiz-option-hover.png`, `quiz-option-focus-visible.png`, `quiz-option-pressed.png`.

#### prod-card

Product card. A catalogue product card (thumbnail, name, colour count, "From $" price); measured, never followed.

Page: catalog. Selector: `catalog product card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 243.19 x 323.44 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Int'l 16px/18.4px 400 | = |
| Letter spacing | normal | = |
| Colour | #161712 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `prod-card-default.png`, `prod-card-hover.png`.

#### prod-badge

Product badge. A "Best seller" / "Staff pick" badge on a product card.

Page: catalog. Selector: `catalog badge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 77 x 22 |
| Padding | 2px 6px |
| Border | 1px solid #000000 @ 0.12 |
| Radius | 100px |
| Background | #161712 |
| Box shadow | none |
| Outline | none |
| Font | Suisse Int'l 12px/16px 600 |
| Letter spacing | normal |
| Colour | #fdfcfb |
| Transition | none |
| Cursor | default |
| Painted layers | span.sc-b35ada23-0.dVXGnN 77.0x22.0 bg #161712 border T:1px solid #000000 @ 0.12 / R:1px solid #000000 @ 0.12 / B:1px solid #000000 @ 0.12 / L:1px solid #000000 @ 0.12 r 100px |
| How | at rest |

Crops: `prod-badge-default.png`.

#### cat-login

Log in action. The "Log in" catalogue action; measured, never followed. Hydration swaps the nav copy roughly a minute after load, so focus/pressed states could not be captured reliably.

Page: catalog. Selector: `catalog Log in`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 75 x 40 | = |
| Padding | 0px 14px | = |
| Gap | 10px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #f2f2f2 | #eaeae9 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Int'l 16px/24px 500 | = |
| Letter spacing | normal | = |
| Colour | #161712 | = |
| Text node | span.sc-5e55b91-2.hKRSML: Suisse Int'l 16px/24px 500, #161712 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | button.sc-5e55b91-0.esHNFO 75.0x40.0 bg #f2f2f2 r 8px | button.sc-5e55b91-0.esHNFO 75.0x40.0 bg #eaeae9 r 8px |
| How | at rest | mouse hover |

Crops: `cat-login-default.png`, `cat-login-hover.png`.

#### cat-signup

Sign up action. The "Sign up" catalogue action; measured, never followed. Focus/pressed states were not reliably measurable (hydration nav swap).

Page: catalog. Selector: `catalog Sign up`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 87 x 40 | = |
| Padding | 0px 14px | = |
| Gap | 10px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #161712 | #252621 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Int'l 16px/24px 500 | = |
| Letter spacing | normal | = |
| Colour | #fdfcfb | = |
| Text node | span.sc-5e55b91-2.hKRSML: Suisse Int'l 16px/24px 500, #fdfcfb | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | button.sc-5e55b91-0.klNlAI 87.0x40.0 bg #161712 r 8px | button.sc-5e55b91-0.klNlAI 87.0x40.0 bg #252621 r 8px |
| How | at rest | mouse hover |

Crops: `cat-signup-default.png`, `cat-signup-hover.png`.

#### cat-tab

Category tab. A category tab in the catalogue nav strip (Discover / All Products / Apparel…); measured, never followed. Focus/pressed states were not reliably measurable (hydration nav swap).

Page: catalog. Selector: `catalog category tab`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 69 x 28 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Int'l 16px/18.4px 400 | = |
| Letter spacing | normal | = |
| Colour | #161712 | = |
| Text node | span.sc-9ae1efd9-1.ePbzzw: Suisse Int'l 16px/18.4px 500, #161712 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | span::after.sc-9ae1efd9-1.ePbzzw 69pxx2px bg #161712 | = |
| How | at rest | mouse hover |

Crops: `cat-tab-default.png`, `cat-tab-hover.png`.

### Product page

#### pdp-h1

Product headline. The PDP product title ("Comfort Colors Garment-Dyed Heavyweight T-Shirt").

Page: pdp. Selector: `pdp h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 400 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans VF 24px/30px 480 |
| Letter spacing | -0.2px |
| Colour | #161712 |
| Transition | none |
| How | at rest |

Crops: `pdp-h1-default.png`.

#### pdp-badge

PDP badge. The "Best seller" badge beside the title.

Page: pdp. Selector: `pdp badge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 77 x 22 |
| Padding | 2px 6px |
| Border | 1px solid #000000 @ 0.12 |
| Radius | 100px |
| Background | #161712 |
| Box shadow | none |
| Outline | none |
| Font | Suisse Int'l 12px/16px 600 |
| Letter spacing | normal |
| Colour | #fdfcfb |
| Transition | none |
| Cursor | default |
| Painted layers | span.sc-b35ada23-0.dVXGnN 77.0x22.0 bg #161712 border T:1px solid #000000 @ 0.12 / R:1px solid #000000 @ 0.12 / B:1px solid #000000 @ 0.12 / L:1px solid #000000 @ 0.12 r 100px |
| How | at rest |

Crops: `pdp-badge-default.png`.

#### pdp-swatch

Colour swatch. A colour swatch button on the PDP (classless styled-components swatch buttons); selecting one repaints the photo locally — measured, selection states only.

Page: pdp. Selector: `pdp swatch`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 28 x 28 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Suisse Int'l 16px/18.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161712 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.sc-ee66eef2-0.hIhVCE 28.0x28.0 bg #080808 border T:1px solid #b5b3b0 / R:1px solid #b5b3b0 / B:1px solid #b5b3b0 / L:1px solid #b5b3b0 r 50%; div::before.sc-ee66eef2-0.hIhVCE 36pxx36px border T:2px solid #161712 / R:2px solid #161712 / B:2px solid #161712 / L:2px solid #161712 r 50% | = | button 28.0x28.0 outline 1px auto #101010 offset 0px; div.sc-ee66eef2-0.hIhVCE 28.0x28.0 bg #080808 border T:1px solid #b5b3b0 / R:1px solid #b5b3b0 / B:1px solid #b5b3b0 / L:1px solid #b5b3b0 r 50%; div::before.sc-ee66eef2-0.hIhVCE 36pxx36px border T:2px solid #161712 / R:2px solid #161712 / B:2px solid #161712 / L:2px solid #161712 r 50% | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pdp-swatch-default.png`, `pdp-swatch-hover.png`, `pdp-swatch-focus-visible.png`, `pdp-swatch-pressed.png`.

#### pdp-sizeguide-btn

Size-guide button. The "Size guide" control — a local dialog toggle.

Page: pdp. Selector: `pdp Size guide`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 79 x 18.39 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Suisse Int'l 16px/18.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161712 | #0042ff | #0042ff | #0042ff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.sc-7d3c69e8-0.iJstzX 79.0x18.4 outline 1px auto #101010 offset 0px | = |

Crops: `pdp-sizeguide-btn-default.png`, `pdp-sizeguide-btn-hover.png`, `pdp-sizeguide-btn-focus-visible.png`, `pdp-sizeguide-btn-pressed.png`.

#### pdp-price

Price text. The "From $15.45" price text.

Page: pdp. Selector: `pdp price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 79 x 21 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Int'l 14px/21px 400 |
| Letter spacing | normal |
| Colour | #6e6e68 |
| Transition | none |
| How | at rest |

Crops: `pdp-price-default.png`.

#### pdp-design-cta

Sign-in-to-design CTA. The "Sign in to design" action — it starts an auth flow; measured, never pressed.

Page: pdp. Selector: `pdp Sign in to design`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 48 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #161712 | #252621 | = | #343531 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #161712 offset 2px | = |
| Font | Suisse Int'l 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fdfcfb | = | = | = |
| Text node | span.sc-5e55b91-2.hKRSML: Suisse Int'l 16px/24px 500, #fdfcfb | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.sc-5e55b91-0.gcdpkn 400.0x48.0 bg #161712 r 8px | button.sc-5e55b91-0.gcdpkn 400.0x48.0 bg #252621 r 8px | button.sc-5e55b91-0.gcdpkn 400.0x48.0 bg #161712 r 8px outline 2px solid #161712 offset 2px | button.sc-5e55b91-0.gcdpkn 400.0x48.0 bg #343531 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pdp-design-cta-default.png`, `pdp-design-cta-hover.png`, `pdp-design-cta-focus-visible.png`, `pdp-design-cta-pressed.png`.

#### pdp-desc

Product description. The product description paragraph (materials, fit, print specs).

Page: pdp. Selector: `pdp description`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 179 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Int'l 16px/24px 600 |
| Letter spacing | normal |
| Colour | #161712 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `pdp-desc-default.png`.

#### pdp-size

Size-range label. The static "S–4XL" size-range label — no per-size option exists on the public PDP.

Page: pdp. Selector: `pdp size range`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 49 x 18.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Int'l 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #161712 |
| Transition | none |
| How | at rest |

Crops: `pdp-size-default.png`.

#### pdp-sizeguide

Size-guide dialog. The size-table dialog mounted by the Size-guide control; opened by its own toggle.

Page: pdp. Selector: `pdp size dialog`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 804 |
| Padding | 0px |
| Border | none |
| Radius | 32px 32px 0px 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Suisse Int'l 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #161712 |
| Text node | div.sc-78ec26a5-3.gdoaYj: Suisse Int'l 20px/28px 400, #161712 |
| Transition | none |
| Icon | 16 x 16, colour #161712 |
| ::after | 1440px x 50px, absolute, bg #ffffff, radius 0px |
| Painted layers | div.sc-b16f3da-0.jcXgZe 1440.0x804.0 bg #ffffff r 32px 32px 0px 0px; div::after.sc-b16f3da-0.jcXgZe 1440pxx50px bg #ffffff; img.sc-78ec26a5-1.cXqmxT 1440.0x1442.0 border T:1px solid #e1e0df / B:1px solid #e1e0df; button.sc-1999645d-1.kWUdic 35.0x29.0 bg #161712 r 100px; button.sc-1999645d-1.ePrlKV 45.0x29.0 bg #f2f2f2 r 100px; div.sc-fd2f24c-0.jZDPuH 1440.0x458.0 border T:1px solid #e1e0df / R:1px solid #e1e0df / B:1px solid #e1e0df / L:1px solid #e1e0df |
| How | at rest |

Crops: `pdp-sizeguide-default.png`.

### Developer docs

#### docs-nav

Docs navbar. The Mintlify top bar — logo, tabs, search and the theme menu.

Page: docs. Selector: `docs navbar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #6f6f6f |
| Text node | div.truncate.min-w-0: Inter 14px/24px 400, #6f6f6f |
| Transition | none |
| Icon | 16 x 16, colour #3e3e3e, fill #000000 |
| Painted layers | div.absolute.w-full 1440.0x112.0 bg #ffffff border B:1px solid #6f6f6f @ 0.05; div.h-full.relative 1344.0x64.0 border B:1px solid #6f6f6f @ 0.05; button.group/search.flex 437.3x36.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9e9e9e @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; span.absolute.inset-0 113.0x36.0 bg #000000 r 12px; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 0.0x0.0 bg #6f6f6f; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 0.0x0.0 bg #6f6f6f |
| How | at rest |

Crops: `docs-nav-default.png`.

#### docs-search

Search trigger. The docs search control — opens the cmdk dialog; states measured.

Page: docs. Selector: `docs search`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 437.33 x 36 | = | = | = |
| Padding | 0px 12px 0px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9e9e9e @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4f4f4f @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4f4f4f @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | 1px auto #000000 offset 0px | = |
| Font | Inter 14px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6f6f6f | = | = | = |
| Text node | div.truncate.min-w-0: Inter 14px/24px 400, #6f6f6f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #3e3e3e, fill #000000 | 16 x 16, colour #252525, fill #000000 | = | 16 x 16, colour #252525, fill #000000 |
| Painted layers | button.group/search.flex 437.3x36.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9e9e9e @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | button.group/search.flex 437.3x36.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4f4f4f @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | button.group/search.flex 437.3x36.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9e9e9e @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #000000 offset 0px | button.group/search.flex 437.3x36.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4f4f4f @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-search-default.png`, `docs-search-hover.png`, `docs-search-focus-visible.png`, `docs-search-pressed.png`.

#### docs-theme-btn

Theme menu button. The "Change theme preference" button — the docs site's real Light/Dark/System menu; measured, the Dark choice is made only on the docsdark pass.

Page: docs. Selector: `docs theme button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #000000 offset 0px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a @ 0.5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #6f6f6f, fill #000000 | 16 x 16, colour #3e3e3e, fill #000000 | = | 16 x 16, colour #3e3e3e, fill #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.group.disabled:pointer-events-none 32.0x32.0 r 8px outline 1px auto #000000 offset 0px | = |

Crops: `docs-theme-btn-default.png`, `docs-theme-btn-hover.png`, `docs-theme-btn-focus-visible.png`, `docs-theme-btn-pressed.png`.

#### docs-sidebar

Docs sidebar. The Mintlify sidebar nav tree.

Page: docs. Selector: `docs sidebar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 288 x 788 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #6f6f6f |
| Text node | a.link.nav-anchor: Inter 14px/24px 500, #4f4f4f |
| Transition | none |
| Icon | 16 x 16, colour #9e9e9e, fill #000000 |
| Painted layers | div.sticky.top-0 256.0x32.0 image linear-gradient(in oklab, #ffffff 0%, #000000 @ 0 100%); div.mr-4.rounded-md 24.0x24.0 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0a0a0a @ 0.07 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 bg #9e9e9e; div.mr-4.rounded-md 24.0x24.0 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0a0a0a @ 0.07 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 bg #9e9e9e; a.group.flex 256.0x36.0 bg #000000 @ 0.1 r 12px |
| How | at rest |

Crops: `docs-sidebar-default.png`.

#### docs-side-item

Sidebar item. A sidebar nav link; measured, never followed.

Page: docs. Selector: `docs sidebar link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 256 x 36 | = | = | = |
| Padding | 6px 12px 6px 16px | = | = | = |
| Gap | normal 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #4f4f4f @ 0.05 | = | #4f4f4f @ 0.05 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #000000 offset -2px | = |
| Font | Inter 14px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #3e3e3e | #161616 | = | #161616 |
| Text node | span.min-w-0.max-w-full: Inter 14px/24px 400, #3e3e3e | span.min-w-0.max-w-full: Inter 14px/24px 400, #161616 | = | span.min-w-0.max-w-full: Inter 14px/24px 400, #161616 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.group.flex 256.0x36.0 bg #4f4f4f @ 0.05 r 12px | a.group.flex 256.0x36.0 r 12px outline 1px auto #000000 offset -2px | a.group.flex 256.0x36.0 bg #4f4f4f @ 0.05 r 12px |

Crops: `docs-side-item-default.png`, `docs-side-item-hover.png`, `docs-side-item-focus-visible.png`, `docs-side-item-pressed.png`.

#### docs-card

Docs card. A .card tile on the docs landing page (Platform API / Webhooks / …); measured, never followed.

Page: docs. Selector: `docs .card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 336.41 x 182 | = |
| Padding | 0px | = |
| Border | 1px solid #0a0a0a @ 0.1 | 1px solid #000000 |
| Radius | 16px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = |
| Font | Inter 16px/28px 400 | = |
| Letter spacing | normal | = |
| Colour | #3e3e3e | = |
| Text node | h2.not-prose.font-semibold: Inter 16px/24px 600, #252525 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 0 x 0, colour #9e9e9e, fill #000000 | 0 x 0, colour #000000 |
| Painted layers | div.card.block 336.4x182.0 bg #ffffff border T:1px solid #0a0a0a @ 0.1 / R:1px solid #0a0a0a @ 0.1 / B:1px solid #0a0a0a @ 0.1 / L:1px solid #0a0a0a @ 0.1 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; a 0.0x0.0 border B:1px solid #000000; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 24.0x24.0 bg #000000 | div.card.block 336.4x182.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; a 0.0x0.0 border B:2px solid #000000; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 24.0x24.0 bg #000000 |
| How | at rest | mouse hover |

Crops: `docs-card-default.png`, `docs-card-hover.png`.

#### docs-h1

Article headline. The docs article title (the /quickstart page).

Page: docsart. Selector: `docs h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 172.02 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 36px/40px 600 |
| Letter spacing | -0.9px |
| Colour | #161616 |
| Transition | none |
| How | at rest |

Crops: `docs-h1-default.png`.

#### docs-prose

Article body. A body paragraph in a docs article.

Page: docsart. Selector: `docs article p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 688.81 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28px 400 |
| Letter spacing | normal |
| Colour | #3e3e3e |
| Transition | none |
| How | at rest |

Crops: `docs-prose-default.png`.

#### docs-code

Code block. A fenced code block in a docs article.

Page: docsart. Selector: `docs pre`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 650.81 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | Paper Mono 14px/24px 400 |
| Letter spacing | normal |
| Colour | #1f2328 |
| Text node | span: Paper Mono 14px/24px 400, #6e7781 |
| Transition | none |
| Painted layers | pre.shiki.shiki-themes 650.8x72.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; code 650.8x72.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.line 376.0x16.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span 376.0x16.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.line 312.0x16.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span 32.0x16.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Ancestor paint | 1 up div.font-mono.whitespace-pre shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #0a0a0a; 2 up div.min-w-full!.h-full shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #0a0a0a; 3 up div.size-full.rounded-[inherit] shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #0a0a0a |
| How | at rest |

Crops: `docs-code-default.png`.

#### docs-anchor

Article link. An in-content link inside a docs article; measured, never followed.

Page: docsart. Selector: `docs article a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 264 x 32 | = | 268 x 32 | = |
| Padding | 4px 0px | = | 4px 0px 4px 4px | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #000000 offset -2px | = |
| Font | Inter 14px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.text-primary.dark:text-primary-light 268.0x32.0 outline 1px auto #000000 offset -2px | = |

Crops: `docs-anchor-default.png`, `docs-anchor-hover.png`, `docs-anchor-focus-visible.png`, `docs-anchor-pressed.png`.

#### docs-toc

On-this-page rail. The right-hand table-of-contents rail.

Page: docsart. Selector: `docs toc`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 264 x 176 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/24px 400 |
| Letter spacing | normal |
| Colour | #4f4f4f |
| Text node | span: Inter 14px/24px 500, #3e3e3e |
| Transition | none |
| Icon | 12 x 12, colour #3e3e3e, fill #000000 |
| How | at rest |

Crops: `docs-toc-default.png`.

#### docs-search-dialog

Search dialog. The Mintlify search dialog; opened by its own search control, nothing sent.

Page: docs. Selector: `docs search dialog`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 62 |
| Padding | 0px |
| Border | none |
| Radius | 20px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0a0a0a @ 0.06 0px 0px 0px 1px, #000000 @ 0.01 0px 57px 34px 0px, #000000 @ 0.02 0px 25px 25px 0px, #000000 @ 0.02 0px 6px 14px 0px |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | transform, scale, opacity 0.25s cubic-bezier(0.22, 1, 0.36, 1) |
| Icon | 16 x 16, colour #6f6f6f, fill #000000 |
| Painted layers | div.origin-center.will-change-[transform,scale,opacity] 640.0x62.0 bg #ffffff r 20px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0a0a0a @ 0.06 0px 0px 0px 1px, #000000 @ 0.01 0px 57px 34px 0px, #000000 @ 0.02 0px 25px 25px 0px, #000000 @ 0.02 0px 6px 14px 0px; div.relative.h-full 628.0x50.0 bg #ffffff border T:1px solid #dedede / R:1px solid #dedede / B:1px solid #dedede / L:1px solid #dedede r 16px; input.flex-1.min-w-0 612.0x36.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `docs-search-dialog-default.png`.

### Developer docs (dark)

#### dd-page

Docs page (dark). The docs article surface under html.dark — reached through the site's own theme menu, not a reconstruction.

Page: docsdark. Selector: `docs main (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1088 x 1887.7 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #9e9e9e |
| Text node | span: Inter 14px/24px 500, #cecece |
| Transition | none |
| Icon | 12 x 12, colour #cecece, fill #000000 |
| Painted layers | a::before.anchor-link 24pxx24px bg #0a0a0c r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3e3e3e @ 0.25 0px 0px 0px 1px, #000000 @ 0.05 0px 1px 2px 0px; a::after.anchor-link 12pxx12px bg #ffffff @ 0.5; div.callout.my-4 688.8x54.0 bg #2563eb @ 0.2 border T:1px solid #1e3a8a / R:1px solid #1e3a8a / B:1px solid #1e3a8a / L:1px solid #1e3a8a r 16px; a.link 204.0x21.0 border B:1px solid #4d4d4d; a::before.anchor-link 24pxx24px bg #0a0a0c r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3e3e3e @ 0.25 0px 0px 0px 1px, #000000 @ 0.05 0px 1px 2px 0px; a::after.anchor-link 12pxx12px bg #ffffff @ 0.5 |
| How | at rest |

Crops: none.

#### dd-h1

Article headline (dark). The article title under html.dark.

Page: docsdark. Selector: `docs h1 (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 172.02 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 36px/40px 600 |
| Letter spacing | -0.9px |
| Colour | #dedede |
| Transition | none |
| How | at rest |

Crops: `dd-h1-default.png`.

#### dd-nav

Docs navbar (dark). The Mintlify navbar under html.dark.

Page: docsdark. Selector: `docs navbar (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #9e9e9e |
| Text node | div.truncate.min-w-0: Inter 14px/24px 400, #ffffff @ 0.5 |
| Transition | none |
| Icon | 16 x 16, colour #9e9e9e, fill #000000 |
| Painted layers | div.absolute.w-full 1440.0x112.0 bg #0a0a0c border B:1px solid #cecece @ 0.06; div.h-full.relative 1344.0x64.0 border B:1px solid #cecece @ 0.06; button.group/search.flex 437.3x36.0 bg #0a0a0c r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4f4f4f @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; span.absolute.inset-0 113.0x36.0 bg #000000 r 12px; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 0.0x0.0 bg #9e9e9e; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 0.0x0.0 bg #9e9e9e |
| How | at rest |

Crops: `dd-nav-default.png`.

#### dd-prose

Article body (dark). A body paragraph under html.dark.

Page: docsdark. Selector: `docs article p (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 688.81 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28px 400 |
| Letter spacing | normal |
| Colour | #9e9e9e |
| Transition | none |
| How | at rest |

Crops: `dd-prose-default.png`.

#### dd-code

Code block (dark). A code block under html.dark.

Page: docsdark. Selector: `docs pre (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 650.81 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | Paper Mono 14px/24px 400 |
| Letter spacing | normal |
| Colour | #d4d4d4 |
| Text node | span: Paper Mono 14px/24px 400, #6a9955 |
| Transition | none |
| Painted layers | pre.shiki.shiki-themes 650.8x72.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; code 650.8x72.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.line 376.0x16.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span 376.0x16.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.line 312.0x16.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span 32.0x16.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Ancestor paint | 1 up div.font-mono.whitespace-pre shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #f2f2f2; 2 up div.min-w-full!.h-full shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #f2f2f2; 3 up div.size-full.rounded-[inherit] shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #f2f2f2 |
| How | at rest |

Crops: `dd-code-default.png`.

#### dd-card

Docs card (dark). A docs card under html.dark.

Page: docsdark. Selector: `docs card (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 336.41 x 134 |
| Padding | 0px |
| Border | 1px solid #ffffff @ 0.1 |
| Radius | 16px |
| Background | #0a0a0c |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | Inter 16px/28px 400 |
| Letter spacing | normal |
| Colour | #9e9e9e |
| Text node | h2.not-prose.font-semibold: Inter 16px/24px 600, #ffffff |
| Transition | none |
| Cursor | pointer |
| Icon | 0 x 0, colour #6f6f6f, fill #000000 |
| Painted layers | div.card.block 336.4x134.0 bg #0a0a0c border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; a 0.0x0.0 border B:1px solid #4d4d4d; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 24.0x24.0 bg #4d4d4d |
| How | at rest |

Crops: `dd-card-default.png`.

### Help center

#### help-navbar

Help navbar. The Docusaurus navbar — "Help center" wordmark, the ctrl-K search, the Fourthwall link and the colour-mode toggle.

Page: help. Selector: `.navbar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 56 |
| Padding | 8px 20px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/24px 400 |
| Letter spacing | normal |
| Colour | #161712 |
| Text node | b.navbar__title.text--truncate: Suisse Intl 16px/24px 500, #161712 |
| Transition | none |
| Icon | 0 x 0, colour #161712, fill #000000 |
| Painted layers | nav.theme-layout-navbar.navbar 1440.0x56.0 bg #ffffff; div.navbar-sidebar__backdrop 1440.0x900.0 bg #000000 @ 0.6 |
| How | at rest |

Crops: `help-navbar-default.png`.

#### help-search

Search field. The help search field (ctrl-K hint); focused and typed into then cleared — a local filter, nothing sent.

Page: help. Selector: `help search input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 852 x 48 | = | = |
| Padding | 0px 16px 0px 48px | = | = |
| Border | none | = | = |
| Radius | 4px | = | = |
| Background | #000000 @ 0.05 | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Arial 16px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #444950 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #6e6e68, opacity 1 | = | = |
| Painted layers | input.navbar__search-input.searchInput_YFbd 852.0x48.0 bg #000000 @ 0.05 r 4px | = | = |
| How | at rest | clicked into the field | typed "storefront", then deleted; nothing sent |

Crops: `help-search-default.png`, `help-search-focused.png`, `help-search-filled.png`.

#### help-theme

Colour-mode toggle. The navbar colour-mode button — the help site's real dark toggle (data-theme); its states were measured but it was only switched on the helpdark pass.

Page: help. Selector: `help theme toggle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 50% | = | = | = |
| Background | transparent | #ebedf0 | = | #ebedf0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Suisse Intl 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161712 | = | = | = |
| Transition | background 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #161712, fill #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.clean-btn.toggleButton_gllP 32.0x32.0 bg #ebedf0 r 50% | button.clean-btn.toggleButton_gllP 32.0x32.0 r 50% outline 1px auto #101010 offset 0px | button.clean-btn.toggleButton_gllP 32.0x32.0 bg #ebedf0 r 50% |

Crops: `help-theme-default.png`, `help-theme-hover.png`, `help-theme-focus-visible.png`, `help-theme-pressed.png`.

#### help-fw-link

Fourthwall link. The "Fourthwall ↗" navbar link back to the product; measured, never followed.

Page: help. Selector: `help Fourthwall link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117 x 32 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161712 | = | = | = |
| Transition | color 0.2s cubic-bezier(0.08, 0.52, 0.52, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #161712, fill #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.navbar__item.navbar__link 117.0x32.0 outline 1px auto #101010 offset 1px | = |

Crops: `help-fw-link-default.png`, `help-fw-link-hover.png`, `help-fw-link-focus-visible.png`, `help-fw-link-pressed.png`.

#### help-card

Category link. A category link row on the help landing list ("Setting up your shop", "Design my storefront", …); measured, never followed.

Page: help. Selector: `help category link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 252 x 24 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #6e6e68 | #161712 |
| Transition | color 0.2s cubic-bezier(0.08, 0.52, 0.52, 1) | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `help-card-default.png`, `help-card-hover.png`.

#### help-side-item

Sidebar item. A help sidebar menu link on the category page; measured, never followed.

Page: helpcat. Selector: `help sidebar link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 238 x 36 | = | = | = |
| Padding | 4px 14px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 14px/21px 500 | = | = | = |
| Letter spacing | 0.1px | = | = | = |
| Colour | #161712 | = | = | = |
| Text node | span.categoryLinkLabel_W154: Suisse Intl 14px/21px 500, #161712, ls 0.1px | = | = | = |
| Transition | background-color, color 0.15s, 0.15s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Ancestor paint | - | 1 up div.menu__list-item-collapsible bg #000000 @ 0.05 | = | = |
| Painted layers | - | = | a.categoryLink_byQd.menu__link 238.0x36.0 r 4px outline 1px auto #101010 offset 1px | = |

Crops: `help-side-item-default.png`, `help-side-item-hover.png`, `help-side-item-focus-visible.png`, `help-side-item-pressed.png`.

#### help-h1

Category headline. The category page title ("Setting up your shop").

Page: helpcat. Selector: `help h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 740 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 40px/50px 450 |
| Letter spacing | -0.6px |
| Colour | #161712 |
| Transition | none |
| How | at rest |

Crops: `help-h1-default.png`.

#### help-doc-link

Article link. An article link inside a help category; measured, never followed.

Page: helpcat. Selector: `help article link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 38.06 x 28.22 | = | = | = |
| Padding | 5.12px 10.24px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | transparent | #000000 @ 0.05 | = | #000000 @ 0.05 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 12px/18px 400 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #6e6e68 | = | = | = |
| Transition | background, color 0.2s cubic-bezier(0.08, 0.52, 0.52, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 17.59 x 17.59, colour #6e6e68, fill #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.breadcrumbs__link 38.1x28.2 bg #000000 @ 0.05 r 24px | a.breadcrumbs__link 38.1x28.2 r 24px outline 1px auto #101010 offset 1px | a.breadcrumbs__link 38.1x28.2 bg #000000 @ 0.05 r 24px |

Crops: `help-doc-link-default.png`, `help-doc-link-hover.png`, `help-doc-link-focus-visible.png`, `help-doc-link-pressed.png`.

#### help-prose

Category body. A body paragraph on the help category page.

Page: helpcat. Selector: `help category p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 740 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/24px 400 |
| Letter spacing | normal |
| Colour | #6e6e68 |
| Transition | none |
| How | at rest |

Crops: `help-prose-default.png`.

#### help-search-pop

Search results dropdown. The local-search results dropdown the navbar search opens while typing.

Page: help. Selector: `help search dropdown`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 852 x 652.39 |
| Padding | 12px |
| Border | none |
| Radius | 6px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.12 0px 4px 16px 0px |
| Outline | none |
| Font | Suisse Intl 16px/24px 400 |
| Letter spacing | normal |
| Colour | #161712 |
| Text node | mark: Suisse Intl 14.4px/21.6px 500, #ffffff |
| Transition | none |
| Icon | 0 x 0, colour #ffffff, fill #000000 |
| Painted layers | span.dropdownMenu_qbY6.with-1 852.0x652.4 bg #ffffff r 6px shadow #000000 @ 0.12 0px 4px 16px 0px; div.suggestion_fB_2.cursor_eG29 828.0x56.0 bg #161712 r 4px; div.suggestion_fB_2 828.0x56.0 bg #000000 @ 0.05 r 4px; div.suggestion_fB_2 828.0x56.0 bg #000000 @ 0.05 r 4px; div.suggestion_fB_2 828.0x56.0 bg #000000 @ 0.05 r 4px; div.suggestion_fB_2 828.0x56.0 bg #000000 @ 0.05 r 4px |
| How | at rest |

Crops: `help-search-pop-default.png`.

### Help center (dark)

#### hd-page

Help page (dark). The help category surface under data-theme=dark — reached through the site's own colour-mode toggle, not a reconstruction.

Page: helpdark. Selector: `help main (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1140 x 788 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fdfcfb |
| Text node | span: Suisse Intl 12px/18px 400, #b5b3b0, ls 0.2px |
| Transition | none |
| Icon | 17.59 x 17.59, colour #b5b3b0, fill #000000 |
| Painted layers | li::after.breadcrumbs__item 8pxx8px image url(data:…); li::after.breadcrumbs__item 8pxx8px image url(data:…); span.breadcrumbs__link 138.5x28.2 bg #ffffff @ 0.05 r 24px; a.card_FHn8 358.0x131.0 border T:1px solid #343531 / R:1px solid #343531 / B:1px solid #343531 / L:1px solid #343531 r 4px; a.card_FHn8 358.0x131.0 border T:1px solid #343531 / R:1px solid #343531 / B:1px solid #343531 / L:1px solid #343531 r 4px |
| How | at rest |

Crops: `hd-page-default.png`.

#### hd-h1

Category headline (dark). The category title under data-theme=dark.

Page: helpdark. Selector: `help h1 (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 740 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 40px/50px 450 |
| Letter spacing | -0.6px |
| Colour | #fdfcfb |
| Transition | none |
| How | at rest |

Crops: `hd-h1-default.png`.

#### hd-navbar

Help navbar (dark). The Docusaurus navbar under data-theme=dark.

Page: helpdark. Selector: `help navbar (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 56 |
| Padding | 8px 20px |
| Border | none |
| Radius | 0px |
| Background | #161712 |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fdfcfb |
| Text node | b.navbar__title.text--truncate: Suisse Intl 16px/24px 500, #fdfcfb |
| Transition | none |
| Icon | 16 x 16, colour #fdfcfb, fill #000000 |
| Painted layers | nav.theme-layout-navbar.navbar 1440.0x56.0 bg #161712; input.navbar__search-input.searchInput_YFbd 500.0x36.0 bg #ffffff @ 0.06 r 4px; div 0.0x0.0 border T:2px solid #ebedf0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 50%; div 0.0x0.0 border T:2px solid #ebedf0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 50%; div 0.0x0.0 border T:2px solid #ebedf0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 50%; div 0.0x0.0 border T:2px solid #ebedf0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 50% |
| How | at rest |

Crops: `hd-navbar-default.png`.

#### hd-search

Search field (dark). The help search field under data-theme=dark.

Page: helpdark. Selector: `help search (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 500 x 36 |
| Padding | 4px 12px 4px 40px |
| Border | none |
| Radius | 4px |
| Background | #ffffff @ 0.06 |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/normal 400 |
| Letter spacing | normal |
| Colour | #fdfcfb |
| Transition | none |
| Cursor | text |
| Placeholder | #b5b3b0, opacity 1 |
| Painted layers | input.navbar__search-input.searchInput_YFbd 500.0x36.0 bg #ffffff @ 0.06 r 4px |
| How | at rest |

Crops: `hd-search-default.png`.

#### hd-card

Category card (dark). A help category card under data-theme=dark.

Page: helpdark. Selector: `help card (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 238 x 36 |
| Padding | 4px 14px |
| Border | none |
| Radius | 4px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 14px/21px 500 |
| Letter spacing | 0.1px |
| Colour | #fdfcfb |
| Text node | span.categoryLinkLabel_W154: Suisse Intl 14px/21px 500, #fdfcfb, ls 0.1px |
| Transition | background-color, color 0.15s, 0.15s ease, ease delay 0s, 0s |
| Cursor | pointer |
| How | at rest |

Crops: `hd-card-default.png`.

### Mobile (390 wide)

#### m-nav

Mobile nav bar. The phone nav bar: wordmark, menu toggle and the Start-now pill.

Page: mobile. Selector: `mobile nav.nav-bar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 64 |
| Padding | 0px 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/26.4px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | color 0.32s ease delay 0.18s |
| Icon | 113 x 20, colour #ffffff |
| ::before | 390px x 64px, absolute, bg #0a0a0a, radius 0px |
| Painted layers | nav::before.nav-bar.is-warm 390pxx64px bg #0a0a0a; a::after.nav-link 100%x1px bg #ffffff; a::after.mega-link 100%x1px bg #ffffff; a::after.mega-link 100%x1px bg #ffffff; a::after.mega-link 100%x1px bg #ffffff; a::after.mega-link 100%x1px bg #ffffff |
| Ancestor paint | 1 up body bg #0a0a0a |
| How | at rest |

Crops: `m-nav-default.png`.

#### m-menu-btn

Menu toggle. The mobile menu toggle; measured, never used to navigate.

Page: mobile. Selector: `mobile menu button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = |
| Font | Suisse Intl 16px/26.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.nav-burger-bar 22.0x2.0 bg #ffffff; span.nav-burger-bar 22.0x2.0 bg #ffffff | = | button.nav-burger 44.0x44.0 outline 1px auto #e59700 offset 0px; span.nav-burger-bar 22.0x2.0 bg #ffffff; span.nav-burger-bar 22.0x2.0 bg #ffffff | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-menu-btn-default.png`, `m-menu-btn-hover.png`, `m-menu-btn-focus-visible.png`, `m-menu-btn-pressed.png`.

#### m-hero-h1

Mobile hero headline. The masthead at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 131 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Saans 29.25px/32.76px 420 |
| Letter spacing | -0.585px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

## Transitions declared in the readable stylesheets

fourthwall.com serves its CSS same-origin (the Webflow mkt.css plus inline blocks; the catalogue SPA bundles its DS sheet; Mintlify and Docusaurus serve their own), so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- blog: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `color 0.2s ease-in-out, background-color 0.2s ease-in-out`, `border-color 0.4s`, `0.2s`, `color 0.2s`, `color 0.2s, opacity 0.2s`, `transform 0.3s, opacity 0.2s`, `background-color 0.2s`, `opacity 0.2s`, `background-color 0.2s linear`

- catalog: `width 200ms var(--motion-ease-in-out)`, `transform 200ms var(--motion-ease-in-out)`, `background-color 0.15s`, `right 200ms var(--motion-ease-in-out)`, `0.2s ease-in-out`, `transform 0.15s ease-in-out, opacity 0.15s ease-in-out, visibility 0.15s ease-in-out`, `stroke 0.1s`, `opacity 0.1s`, `border-color 0.1s, background-color 0.1s`, `transform 0.3s`, `0.3s`, `transform 0.2s`

- cmparticle: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `color 0.2s ease-in-out, background-color 0.2s ease-in-out`, `border-color 0.4s`, `0.2s`, `color 0.2s`, `color 0.2s, opacity 0.2s`, `transform 0.3s, opacity 0.2s`, `background-color 0.2s`, `opacity 0.2s`, `background-color 0.2s linear`

- compare: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `color 0.2s ease-in-out, background-color 0.2s ease-in-out`, `border-color 0.4s`, `0.2s`, `color 0.2s`, `color 0.2s, opacity 0.2s`, `transform 0.3s, opacity 0.2s`, `background-color 0.2s`, `opacity 0.2s`, `background-color 0.2s linear`

- docs: `top 0.16s cubic-bezier(0.25, 0.75, 0.2, 1)`, `width var(--duration-long) var(--timing),height var(--duration-long) var(--timing),background var(--duration-short) ease,scale var(--duration-short) var(--timing)`, `none`, `border-color 0.3s`, `filter 0.35s, opacity 0.35s`, `opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1)`, `opacity var(--lightbox-pull-snap-duration,var(--lightbox-vt-duration)) var(--lightbox-pull-snap-easing,var(--lightbox-vt-root-easing))`, `opacity var(--lightbox-vt-duration) var(--lightbox-vt-root-easing)`, `opacity 0.2s, visibility linear`, `opacity 0.2s, visibility linear 0.2s`, `opacity 0.2s`

- help: `color var(--ifm-transition-fast) var(--ifm-transition-timing-default)`, `opacity var(--ifm-transition-fast) var(--ifm-transition-timing-default)`, `background var(--ifm-transition-fast) var(--ifm-transition-timing-default)`, `transform var(--ifm-transition-fast) linear`, `transform var(--ifm-transition-fast) ease-in-out`, `border-color var(--ifm-transition-fast) var(--ifm-transition-timing-default)`, `background-color var(--ifm-transition-fast) var(--ifm-transition-timing-default)`, `background-color 0.15s, color 0.15s`, `border-color 0.15s`, `transform var(--ifm-transition-fast) ease`, `var(--docusaurus-details-transition)`, `opacity 0.15s`

- home: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `color 0.2s ease-in-out, background-color 0.2s ease-in-out`, `border-color 0.4s`, `0.2s`, `color 0.2s`, `color 0.2s, opacity 0.2s`, `transform 0.3s, opacity 0.2s`, `background-color 0.2s`, `opacity 0.2s`, `background-color 0.2s linear`

- pdp: `width 200ms var(--motion-ease-in-out)`, `width 0.3s ease-in-out`, `right 200ms var(--motion-ease-in-out)`, `transform 0.15s ease-in-out, opacity 0.15s ease-in-out, visibility 0.15s ease-in-out`, `transform 200ms var(--motion-ease-in-out)`, `background-color 0.15s`, `transform 0.3s`, `opacity 0.1s`, `0.3s`, `transform 0.2s`

- pricing: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `color 0.2s ease-in-out, background-color 0.2s ease-in-out`, `border-color 0.4s`, `0.2s`, `color 0.2s`, `color 0.2s, opacity 0.2s`, `transform 0.3s, opacity 0.2s`, `background-color 0.2s`, `opacity 0.2s`, `background-color 0.2s linear`

- shops: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `color 0.2s ease-in-out, background-color 0.2s ease-in-out`, `border-color 0.4s`, `0.2s`, `color 0.2s`, `color 0.2s, opacity 0.2s`, `transform 0.3s, opacity 0.2s`, `background-color 0.2s`, `opacity 0.2s`, `background-color 0.2s linear`

- signup: `opacity 0.3s`, `transform 0.2s, top 0.2s`, `transform 0.2s, left 0.2s`, `transform 0.2s, right 0.2s`, `opacity 0.3s ease-in-out`

## Reduced motion

- home (`.nav-bar a, .nav-bar button` under prefers-reduced-motion): transition `background-color 0.32s 0.18s, color 0.32s 0.18s`, animation `none 0s ease 0s 1 normal none running`, html scroll-behavior `auto`
