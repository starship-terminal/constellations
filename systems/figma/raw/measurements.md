# Figma component measurements

Computed styles read from figma.com on 2026-11-15 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the light :root marketing pages (home, design, figjam, slides, dev-mode, make, pricing, blog, customers, enterprise, careers, contact, downloads, design-systems, release-notes), the product app shell at /community, /login and /signup (a different stack that does not share the marketing --fig-* layer), and the mobile drawer — with the cookie consent layer hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). The declared :root[data-theme="dark"] token layer resolved no painted surface; no public page carried the attribute. One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Site chrome

#### mkt-header

Site header. The fixed top bar on every marketing page: the Figma mark, Products/Solutions/Community/Resources dropdown triggers, Pricing, Log in, Contact sales and the "Get started for free" CTA.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 78.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | figmaSans 16px/23.2px 400 |
| Letter spacing | -0.14px |
| Colour | #000000 |
| Text node | span.nav-highlight.fig-1wty479: figmaSans 16px/23.2px 400, #000000 |
| Transition | background 0.4s cubic-bezier(0.8, 0, 0.2, 1) |
| Cursor | default |
| Icon | 19 x 28, colour #000000 |
| Painted layers | header.fig-suku18 1440.0x78.4 bg #ffffff; div.fig-1rmlagr 1440.0x78.4 bg #ffffff shadow oklch(0 0 none / 0.16) 0px 1px 0px 0px; span::after.nav-highlight.fig-1wty479 67pxx1px bg #000000; div.fig-56zixy 0.0x0.0 bg #ffffff; span::after.nav-highlight autox1px bg #000000; span::after.nav-highlight autox1px bg #000000 |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The Figma mark in the header, linking home.

Page: home. Selector: `header a[href=/]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 19 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | figmaSans 16px/23.2px 400 |
| Letter spacing | -0.14px |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Icon | 19 x 28, colour #000000 |
| Ancestor paint | 3 up div.fig-1rmlagr bg #ffffff shadow oklch(0 0 none / 0.16) 0px 1px 0px 0px |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-dropdown-btn

Nav dropdown trigger. The "Products" header button — a data-nav-dropdown-trigger that opens the products dropdown. The opened state was measured after its own toggle click; aria-expanded had to stay true.

Page: home. Selector: `button[data-nav-dropdown-trigger] Products`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 103 x 39.19 | = | = | = | = |
| Padding | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px dashed #000000 offset 4px | = | = |
| Font | figmaSans 18px/25.2px 330 | = | = | = | = |
| Letter spacing | -0.14px | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Text node | span.nav-highlight.fig-1wty479: figmaSans 16px/23.2px 400, #000000 | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 18 x 18, colour #000000 | = | = | = | = |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px | = | = | = | = |
| Painted layers | span::after.nav-highlight.fig-1wty479 67pxx1px bg #000000 | = | button.dropdown-label.fig-7comqs 103.0x39.2 outline 2px dashed #000000 offset 4px; span::after.nav-highlight.fig-1wty479 67pxx1px bg #000000 | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `nav-dropdown-btn-default.png`, `nav-dropdown-btn-hover.png`, `nav-dropdown-btn-focus-visible.png`, `nav-dropdown-btn-pressed.png`, `nav-dropdown-btn-opened.png`.

#### nav-panel

Products dropdown panel. The dropdown panel opened by the "Products" trigger (Figma Design, Make, Weave, Dev Mode, Motion, Specs, FigJam, Slides, Draw, Sites, Buzz, AI workflows, Release notes, Downloads); its links were never followed.

Page: home. Selector: `products dropdown panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 522.84 |
| Padding | 40px 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | figmaSans 18px/25.2px 330 |
| Letter spacing | -0.14px |
| Colour | #000000 |
| Text node | h2.fig-4htygd: figmaMono 14px/18.2px 400, oklch(0 0 none / 0.54), ls 0.5px |
| Transition | none |
| Cursor | default |
| Icon | 22.39 x 22.39, colour #000000 |
| Painted layers | div.fig-56zixy 1440.0x522.8 bg #ffffff; span::after.nav-highlight 96pxx1px bg #000000; span::after.nav-highlight 86pxx1px bg #000000; span::after.nav-highlight 94pxx1px bg #000000; span::after.nav-highlight 74pxx1px bg #000000; span::after.nav-highlight 99pxx1px bg #000000 |
| How | at rest |

Crops: `nav-panel-default.png`.

#### nav-menu-item

Dropdown item. The "Figma Design" item inside the opened products dropdown; measured, never followed.

Page: home. Selector: `products dropdown item`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 328 x 49.58 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | figmaSans 18px/25.2px 330 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.nav-highlight: figmaSans 16px/22.4px 400, #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 22.39 x 22.39, colour #000000 | = |
| Painted layers | span::after.nav-highlight 96pxx1px bg #000000 | = |
| How | at rest | mouse hover |

Crops: `nav-menu-item-default.png`, `nav-menu-item-hover.png`.

#### nav-pricing

Nav link. The "Pricing" header link; measured, never followed.

Page: home. Selector: `header a Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 67 x 39.19 | = | = | = |
| Padding | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dashed #000000 offset 4px | = |
| Font | figmaSans 16px/23.2px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.nav-highlight: figmaSans 16px/23.2px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span::after.nav-highlight 51pxx1px bg #000000 | = | a.fig-19xeqcu 67.0x39.2 outline 2px dashed #000000 offset 4px; span::after.nav-highlight 51pxx1px bg #000000 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-pricing-default.png`, `nav-pricing-hover.png`, `nav-pricing-focus-visible.png`, `nav-pricing-pressed.png`.

#### nav-login

Log in link. The "Log in" header link to /login; measured, never followed.

Page: home. Selector: `header a Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 59 x 39.19 | = | = | = |
| Padding | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dashed #000000 offset 4px | = |
| Font | figmaSans 16px/23.2px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.nav-highlight: figmaSans 16px/23.2px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span::after.nav-highlight 43pxx1px bg #000000 | = | a.fig-12retlt 59.0x39.2 outline 2px dashed #000000 offset 4px; span::after.nav-highlight 43pxx1px bg #000000 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-cta

Header CTA. The dark "Get started for free" header pill; links to /signup, measured never followed.

Page: home. Selector: `header a Get started for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 198 x 46.39 | = | = | = |
| Padding | 12px 22px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #000000 | oklch(0 0 none / 0.85) | = | oklch(0 0 none / 0.85) |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dashed #000000 offset 4px | = |
| Font | figmaSans 18px/25.2px 330 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.btn-text.fig-1v6pe89: figmaSans 16px/22.4px 400, #ffffff | = | = | = |
| Transition | background, box-shadow 0.18s, 0.18s ease-out, ease-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = |
| Painted layers | a.fig-4rcs94 198.0x46.4 bg #000000 r 8px | a.fig-4rcs94 198.0x46.4 bg oklch(0 0 none / 0.85) r 8px | a.fig-4rcs94 198.0x46.4 bg #000000 r 8px outline 2px dashed #000000 offset 4px | a.fig-4rcs94 198.0x46.4 bg oklch(0 0 none / 0.85) r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### hero-h1

Hero headline. "The full-stack creative canvas" — the figma.com hero display heading.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 328 x 168 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | figmaSans 56px/56px 400 |
| Letter spacing | -1.25px |
| Colour | #000000 |
| Transition | none |
| Cursor | text |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-cta

Hero CTA. The dark "Get started" pill in the hero; links to /signup, measured never followed.

Page: home. Selector: `hero Get started`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 222.75 x 84 | = | = | = |
| Padding | 24px 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | #000000 | = | = | oklch(0 0 none / 0.85) |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dashed #000000 offset 4px | = |
| Font | figmaSans 16px/23.2px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.btn-text.fig-2vtqnm: figmaSans 30px/36px 400, #ffffff, ls -0.66px | = | = | = |
| Transition | background, box-shadow 0.18s, 0.18s ease-out, ease-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 36 x 36, colour #ffffff | = | = | = |
| Painted layers | a.fig-1ytmgio 222.8x84.0 bg #000000 r 16px | = | a.fig-1ytmgio 222.8x84.0 bg #000000 r 16px outline 2px dashed #000000 offset 4px | a.fig-1ytmgio 222.8x84.0 bg oklch(0 0 none / 0.85) r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### play-btn

Demo play button. A "Play" control on a hero/section product demo video; a local media toggle, measured not held.

Page: home. Selector: `main button Play`. States: .

Not found on the page at capture time.

#### section-h2

Section heading. A marketing section heading further down the home page.

Page: home. Selector: `main h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 901.33 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | figmaSans 30px/36px 400 |
| Letter spacing | -0.66px |
| Colour | #000000 |
| Transition | none |
| Cursor | text |
| How | at rest |

Crops: `section-h2-default.png`.

### Footer

#### footer

Footer. The page footer: product/use-case/resource columns, social icons and the locale button.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1261.47 |
| Padding | 120px 0px |
| Border | T: 1px solid #ffffff @ 0.16; R: none; B: none; L: none |
| Radius | 0px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | figmaSans 16px/23.2px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.fig-1gg9t03: figmaMono 16px/20.8px 400, #ffffff @ 0.6, ls 0.48px |
| Transition | none |
| Cursor | default |
| Icon | 120 x 44, colour #ffffff |
| Painted layers | footer.fig-97erl1 1440.0x1261.5 bg #000000 border T:1px solid #ffffff @ 0.16; a.fig-gdypag 36.0x36.0 bg #ffffff @ 0.24 r 50%; a.fig-gdypag 36.0x36.0 bg #ffffff @ 0.24 r 50%; a.fig-gdypag 36.0x36.0 bg #ffffff @ 0.24 r 50%; a.fig-gdypag 36.0x36.0 bg #ffffff @ 0.24 r 50%; div.fig-1ymitnt 38.8x21.0 bg #ffffff @ 0.16 r 4px |
| Ancestor paint | 1 up div.css-14r34si bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer sitemap link; measured, never followed.

Page: home. Selector: `footer a Careers`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56.17 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dashed #ffffff offset 4px | = |
| Font | figmaSans 18px/25.2px 330 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.fig-bpov6r: figmaSans 16px/23.2px 320, #ffffff, ls -0.12px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.fig-1czkxn0 56.2x20.0 outline 2px dashed #ffffff offset 4px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### locale-btn

Locale button. The "English" locale button in the footer — a local UI toggle for the locale list; measured, never toggled.

Page: home. Selector: `footer button English`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 118 x 39.19 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dashed #ffffff offset 4px | = |
| Font | figmaSans 16px/23.2px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 22 x 22, colour #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.fig-q9rm4z 118.0x39.2 outline 2px dashed #ffffff offset 4px | = |

Crops: `locale-btn-default.png`, `locale-btn-hover.png`, `locale-btn-focus-visible.png`, `locale-btn-pressed.png`.

### Pricing

#### price-h1

Pricing headline. "Pick your plan, choose your seats" — the /pricing masthead.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 840 x 163.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | figmaSans 86px/81.7px 400 |
| Letter spacing | -1.72px |
| Colour | #000000 |
| Transition | none |
| Cursor | text |
| How | at rest |

Crops: `price-h1-default.png`.

#### price-toggle

Billing toggle. The Monthly/Annual segmented control; measured at rest, never toggled (toggling would re-price the grid).

Page: pricing. Selector: `billing Monthly/Annual toggle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 180 x 29 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 80px | = | = | = |
| Background | #000000 @ 0.08 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dashed #000000 offset 4px | = |
| Font | figmaSans 18px/25.2px 330 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.fig-c6t90c: figmaSans 12px/15px 360, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.fig-sqbkms 180.0x29.0 bg #000000 @ 0.08 r 80px; div.fig-k5xzwr 84.0x21.0 bg #ffffff r 80px | = | button.fig-sqbkms 180.0x29.0 bg #000000 @ 0.08 r 80px outline 2px dashed #000000 offset 4px; div.fig-k5xzwr 84.0x21.0 bg #ffffff r 80px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `price-toggle-default.png`, `price-toggle-hover.png`, `price-toggle-focus-visible.png`, `price-toggle-pressed.png`.

#### seat-combo

Seat combobox. The "Full seat" role combobox that re-prices the grid; measured at rest, never opened (its options recompute prices).

Page: pricing. Selector: `seat combobox`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 180 x 53.19 | = | = | = |
| Padding | 24px 36px 4px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #000000 @ 0.08 | = | = | = |
| Box shadow | none | #000000 0px 0px 0px 1px inset | #000000 0px 0px 0px 2px inset | #000000 0px 0px 0px 1px inset |
| Outline | none | = | = | = |
| Font | figmaSans 18px/25.2px 330 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 180px x 53.1875px, absolute, bg #000000, radius 0px | = | = | = |
| Painted layers | button.fig-194w9l5 180.0x53.2 bg #000000 @ 0.08 r 8px; button::after.fig-194w9l5 180pxx53.1875px bg #000000 | button.fig-194w9l5 180.0x53.2 bg #000000 @ 0.08 r 8px shadow #000000 0px 0px 0px 1px inset; button::after.fig-194w9l5 180pxx53.1875px bg #000000 | button.fig-194w9l5 180.0x53.2 bg #000000 @ 0.08 r 8px shadow #000000 0px 0px 0px 2px inset; button::after.fig-194w9l5 180pxx53.1875px bg #000000 | button.fig-194w9l5 180.0x53.2 bg #000000 @ 0.08 r 8px shadow #000000 0px 0px 0px 1px inset; button::after.fig-194w9l5 180pxx53.1875px bg #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `seat-combo-default.png`, `seat-combo-hover.png`, `seat-combo-focus-visible.png`, `seat-combo-pressed.png`.

#### feature-switch

Feature switch. The "All features / Key features" switch (role=switch); measured at rest, never toggled.

Page: pricing. Selector: `features switch`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 280 x 46.5 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 80px | = | = | = |
| Background | #000000 @ 0.08 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dashed #000000 offset 4px | = |
| Font | figmaSans 16px/23.2px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.fig-1hp26q0: figmaSans 18px/22.5px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.fig-1g6lmgu 280.0x46.5 bg #000000 @ 0.08 r 80px; div.fig-l3dzoc 132.0x34.5 bg #ffffff r 80px | = | button.fig-1g6lmgu 280.0x46.5 bg #000000 @ 0.08 r 80px outline 2px dashed #000000 offset 4px; div.fig-l3dzoc 132.0x34.5 bg #ffffff r 80px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `feature-switch-default.png`, `feature-switch-hover.png`, `feature-switch-focus-visible.png`, `feature-switch-pressed.png`.

#### plan-card

Plan card. The Professional plan column: name, price, seat copy and its CTA.

Page: pricing. Selector: `plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 330 x 802.8 |
| Padding | 0px |
| Gap | 24px |
| Border | T: none; R: none; B: none; L: 1px solid #000000 @ 0.16 |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | figmaSans 18px/25.2px 330 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.fig-1sj92if: figmaSans 32px/41.6px 400, #000000, ls -0.32px |
| Transition | none |
| Cursor | default |
| Icon | 16 x 16, colour #000000 |
| Painted layers | article.fig-1vpss82 330.0x802.8 border L:1px solid #000000 @ 0.16; button.fig-sqbkms 180.0x29.0 bg #000000 @ 0.08 r 80px; div.fig-k5xzwr 84.0x21.0 bg #ffffff r 80px; div.fig-qq6tkq 329.0x94.5 border B:1px solid #000000 @ 0.08; div.fig-qq6tkq 329.0x94.5 border B:1px solid #000000 @ 0.08; div.fig-qq6tkq 329.0x94.5 border B:1px solid #000000 @ 0.08 |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-cta

Plan CTA. A plan card's action (Get started / Contact sales), scoped to a plan article so the header's "Contact sales" link cannot match first; measured, never followed.

Page: pricing. Selector: `plan card CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 84 x 26.09 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 2px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dashed #000000 offset 4px | = |
| Font | figmaSans 18px/25.2px 330 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.btn-text.fig-1v6pe89: figmaSans 14px/20.3px 340, #697485 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.fig-1d1iijj 84.0x26.1 r 2px outline 2px dashed #000000 offset 4px | = |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### feature-acc

Feature accordion. A feature-list accordion in the comparison grid ("Components", "Auto layout", ...); the opened state was measured after clicking it — a local UI toggle.

Page: pricing. Selector: `feature accordion button`. States: default, opened, hover.

| Property | default | opened | hover |
|---|---|---|---|
| Size (w x h) | 412 x 24 | = | = |
| Padding | 0px | = | = |
| Gap | 4px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | figmaSans 16px/18.4px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | p.fig-g46nf5: figmaSans 16px/23.2px 320, #000000 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 24 x 24, colour #000000 | = | = |
| Painted layers | button.fig-1vcqcp2 412.0x24.0 bg #ffffff | = | = |
| How | at rest | own toggle | mouse hover |

Crops: `feature-acc-default.png`, `feature-acc-opened.png`, `feature-acc-hover.png`.

### Contact sales form

#### contact-h1

Contact headline. The /contact masthead over the sales form.

Page: contact. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 510 x 61.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | figmaSans 56px/61.6px 400 |
| Letter spacing | -0.84px |
| Colour | #000000 |
| Transition | none |
| Cursor | text |
| How | at rest |

Crops: `contact-h1-default.png`.

#### field-email

Email field. The work-email input; focused and typed into then cleared — never submitted.

Page: contact. Selector: `input[name=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 600 x 58.19 | = | = |
| Padding | 27px 12px 6px 12px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | #000000 @ 0.08 | = | = |
| Box shadow | none | #000000 0px 0px 0px 2px inset | #000000 0px 0px 0px 2px inset |
| Outline | none | = | = |
| Font | figmaSans 18px/25.2px 330 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000, opacity 1 | = | = |
| Painted layers | input.fig-1yvyd6q 600.0x58.2 bg #000000 @ 0.08 r 8px | input.fig-1yvyd6q 600.0x58.2 bg #000000 @ 0.08 r 8px shadow #000000 0px 0px 0px 2px inset | input.fig-1yvyd6q 600.0x58.2 bg #000000 @ 0.08 r 8px shadow #000000 0px 0px 0px 2px inset |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `field-email-default.png`, `field-email-focused.png`, `field-email-filled.png`.

#### field-firstname

First name field. The first-name input; focused and typed into then cleared — never submitted.

Page: contact. Selector: `input[name=firstName]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 294 x 58.19 | = | = |
| Padding | 27px 12px 6px 12px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | #000000 @ 0.08 | = | = |
| Box shadow | none | #000000 0px 0px 0px 2px inset | #000000 0px 0px 0px 2px inset |
| Outline | none | = | = |
| Font | figmaSans 18px/25.2px 330 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000, opacity 1 | = | = |
| Painted layers | input.fig-1yvyd6q 294.0x58.2 bg #000000 @ 0.08 r 8px | input.fig-1yvyd6q 294.0x58.2 bg #000000 @ 0.08 r 8px shadow #000000 0px 0px 0px 2px inset | input.fig-1yvyd6q 294.0x58.2 bg #000000 @ 0.08 r 8px shadow #000000 0px 0px 0px 2px inset |
| How | at rest | clicked into the field | typed "Ada", then deleted; nothing sent |

Crops: `field-firstname-default.png`, `field-firstname-focused.png`, `field-firstname-filled.png`.

#### field-lastname

Last name field. The last-name input; focused and typed into then cleared — never submitted.

Page: contact. Selector: `input[name=lastName]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 294 x 58.19 | = | = |
| Padding | 27px 12px 6px 12px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | #000000 @ 0.08 | = | = |
| Box shadow | none | #000000 0px 0px 0px 2px inset | #000000 0px 0px 0px 2px inset |
| Outline | none | = | = |
| Font | figmaSans 18px/25.2px 330 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000, opacity 1 | = | = |
| Painted layers | input.fig-1yvyd6q 294.0x58.2 bg #000000 @ 0.08 r 8px | input.fig-1yvyd6q 294.0x58.2 bg #000000 @ 0.08 r 8px shadow #000000 0px 0px 0px 2px inset | input.fig-1yvyd6q 294.0x58.2 bg #000000 @ 0.08 r 8px shadow #000000 0px 0px 0px 2px inset |
| How | at rest | clicked into the field | typed "Lovelace", then deleted; nothing sent |

Crops: `field-lastname-default.png`, `field-lastname-focused.png`, `field-lastname-filled.png`.

#### field-topic

Free-text field. The unnamed free-text input on the sales form's first step (the name=topic twin is a display:none honeypot); focused and typed into then cleared — never submitted.

Page: contact. Selector: `contact unnamed text input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 600 x 58.19 | = | = |
| Padding | 27px 40px 6px 12px | = | = |
| Border | none | = | = |
| Radius | 8px | 8px 8px 0px 0px | = |
| Background | #000000 @ 0.08 | = | = |
| Box shadow | none | #000000 0px 0px 0px 2px inset | #000000 0px 0px 0px 2px inset |
| Outline | none | = | = |
| Font | figmaSans 18px/25.2px 330 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Placeholder | #000000, opacity 1 | = | = |
| Painted layers | input.fig-2wwy56 600.0x58.2 bg #000000 @ 0.08 r 8px | input.fig-2wwy56 600.0x58.2 bg #000000 @ 0.08 r 8px 8px 0px 0px shadow #000000 0px 0px 0px 2px inset | input.fig-2wwy56 600.0x58.2 bg #000000 @ 0.08 r 8px shadow #000000 0px 0px 0px 2px inset |
| How | at rest | clicked into the field | typed "A product question", then deleted; nothing sent |

Crops: `field-topic-default.png`, `field-topic-focused.png`, `field-topic-filled.png`.

#### next-btn

Next step button. The multi-step form's "Next step" button; its states were measured but the button was never clicked — the form never advanced.

Page: contact. Selector: `contact Next step`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 480 x 46.39 | = | = | = |
| Padding | 12px 22px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #000000 | oklch(0 0 none / 0.85) | = | oklch(0 0 none / 0.85) |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dashed #000000 offset 4px | = |
| Font | figmaSans 16px/18.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.btn-text.fig-1v6pe89: figmaSans 16px/22.4px 400, #ffffff | = | = | = |
| Transition | background, box-shadow 0.18s, 0.18s ease-out, ease-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = |
| Painted layers | button.fig-1oacq5 480.0x46.4 bg #000000 r 8px | button.fig-1oacq5 480.0x46.4 bg oklch(0 0 none / 0.85) r 8px | button.fig-1oacq5 480.0x46.4 bg #000000 r 8px outline 2px dashed #000000 offset 4px | button.fig-1oacq5 480.0x46.4 bg oklch(0 0 none / 0.85) r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `next-btn-default.png`, `next-btn-hover.png`, `next-btn-focus-visible.png`, `next-btn-pressed.png`.

### Login and signup (product shell)

#### login-panel

Login panel. The product-shell sign-in card on /login: "Sign in to Figma" with Google SSO, e-mail and password.

Page: login. Selector: `login form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 422 x 479.59 |
| Padding | 0px 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Figma Sans 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.898 |
| Text node | h1.auth_form--header--fr1Af.auth_form--headerBase--dPZBh: Figma Sans 32px/41.6px 500, #000000 @ 0.898, ls -0.32px |
| Transition | none |
| Icon | 18 x 18, colour #000000 @ 0.898, fill #000000 |
| Painted layers | button.brand_buttons--brandButton--Y6xZJ.auth_view--brandButton--dD0L7 358.0x48.0 border T:1px solid #2c2c2c / R:1px solid #2c2c2c / B:1px solid #2c2c2c / L:1px solid #2c2c2c r 8px; input.lazy_input--lazyInput--akTHe 358.0x53.0 bg #000000 @ 0.05 r 6px; input.lazy_input--lazyInput--akTHe 358.0x53.0 bg #000000 @ 0.05 r 6px; button.brand_buttons--brandButton--Y6xZJ.auth_view--brandButton--dD0L7 358.0x48.0 bg #2c2c2c r 8px |
| How | at rest |

Crops: `login-panel-default.png`.

#### login-google

Google SSO button. The "Continue with Google" button; measured, never pressed.

Page: login. Selector: `login Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 358 x 48 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | 1px solid #2c2c2c | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dashed #2c2c2c offset 4px | = |
| Font | Figma Sans 16px/24px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.898 | = | = | = |
| Text node | span.brand_buttons--googleText--8KC1c: Figma Sans 18px/25.2px 480, #000000 @ 0.898, ls -0.09px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #000000 @ 0.898, fill #000000 | = | = | = |
| Painted layers | button.brand_buttons--brandButton--Y6xZJ.auth_view--brandButton--dD0L7 358.0x48.0 border T:1px solid #2c2c2c / R:1px solid #2c2c2c / B:1px solid #2c2c2c / L:1px solid #2c2c2c r 8px | = | button.brand_buttons--brandButton--Y6xZJ.auth_view--brandButton--dD0L7 358.0x48.0 border T:1px solid #2c2c2c / R:1px solid #2c2c2c / B:1px solid #2c2c2c / L:1px solid #2c2c2c r 8px outline 2px dashed #2c2c2c offset 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-google-default.png`, `login-google-hover.png`, `login-google-focus-visible.png`, `login-google-pressed.png`.

#### login-email

Email field (login). The e-mail input on the sign-in card; focused and typed into then cleared — never submitted.

Page: login. Selector: `login input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 358 x 53 | = | = |
| Padding | 24px 12px 6px 12px | = | = |
| Border | none | = | = |
| Radius | 6px | = | = |
| Background | #000000 @ 0.05 | = | = |
| Box shadow | none | #444444 0px 0px 0px 2px inset | #444444 0px 0px 0px 2px inset |
| Outline | none | = | = |
| Font | Figma Sans 18px/25px 320 | = | = |
| Letter spacing | -0.09px | = | = |
| Colour | #000000 @ 0.898 | = | = |
| Transition | none | = | = |
| Placeholder | #000000 @ 0.898, opacity 1 | = | = |
| Painted layers | input.lazy_input--lazyInput--akTHe 358.0x53.0 bg #000000 @ 0.05 r 6px | input.lazy_input--lazyInput--akTHe 358.0x53.0 bg #000000 @ 0.05 r 6px shadow #444444 0px 0px 0px 2px inset | input.lazy_input--lazyInput--akTHe 358.0x53.0 bg #000000 @ 0.05 r 6px shadow #444444 0px 0px 0px 2px inset |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-email-default.png`, `login-email-focused.png`, `login-email-filled.png`.

#### login-password

Password field (login). The password input on the sign-in card; focused and typed into then cleared — never submitted.

Page: login. Selector: `login input[type=password]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 358 x 53 | = | = |
| Padding | 24px 12px 6px 12px | = | = |
| Border | none | = | = |
| Radius | 6px | = | = |
| Background | #000000 @ 0.05 | = | = |
| Box shadow | none | #444444 0px 0px 0px 2px inset | #444444 0px 0px 0px 2px inset |
| Outline | none | = | = |
| Font | Figma Sans 18px/25px 320 | = | = |
| Letter spacing | 3.6px | = | = |
| Colour | #000000 @ 0.898 | = | = |
| Transition | none | = | = |
| Placeholder | #000000 @ 0.898, opacity 1 | = | = |
| Painted layers | input.lazy_input--lazyInput--akTHe 358.0x53.0 bg #000000 @ 0.05 r 6px | input.lazy_input--lazyInput--akTHe 358.0x53.0 bg #000000 @ 0.05 r 6px shadow #444444 0px 0px 0px 2px inset | input.lazy_input--lazyInput--akTHe 358.0x53.0 bg #000000 @ 0.05 r 6px shadow #444444 0px 0px 0px 2px inset |
| How | at rest | clicked into the field | typed "not-a-real-password", then deleted; nothing sent |

Crops: `login-password-default.png`, `login-password-focused.png`, `login-password-filled.png`.

#### login-submit

Log in submit. The "Log in" submit button; its states were measured but the button was never clicked — nothing was submitted.

Page: login. Selector: `login Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 358 x 48 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | 0px | = | 0px |
| Background | #2c2c2c | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dashed #2c2c2c offset 4px | = |
| Font | Figma Sans 18px/24px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.898 | = | = | = |
| Text node | span.brand_buttons--brandButtonContent--ZFibF: Figma Sans 18px/25.2px 480, #ffffff @ 0.898, ls -0.09px | = | = | = |
| Transition | border-radius 0.16s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 22 x 21, colour #ffffff @ 0.898, fill #ffffff | = | = | = |
| Painted layers | button.brand_buttons--brandButton--Y6xZJ.auth_view--brandButton--dD0L7 358.0x48.0 bg #2c2c2c r 8px | button.brand_buttons--brandButton--Y6xZJ.auth_view--brandButton--dD0L7 358.0x48.0 bg #2c2c2c | button.brand_buttons--brandButton--Y6xZJ.auth_view--brandButton--dD0L7 358.0x48.0 bg #2c2c2c r 8px outline 2px dashed #2c2c2c offset 4px | button.brand_buttons--brandButton--Y6xZJ.auth_view--brandButton--dD0L7 358.0x48.0 bg #2c2c2c |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-focus-visible.png`, `login-submit-pressed.png`.

#### login-sso

SSO link. The "Use single sign-on" link; measured, never followed.

Page: login. Selector: `login Use single sign-on`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #757575 offset 1px | = |
| Font | Figma Sans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0768cf | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 117.0x20.0 outline 1px solid #757575 offset 1px | = |

Crops: `login-sso-default.png`, `login-sso-hover.png`, `login-sso-focus-visible.png`, `login-sso-pressed.png`.

#### signup-panel

Signup panel. The product-shell sign-up card on /signup: "Welcome to Figma" with Google SSO and an e-mail field.

Page: signup. Selector: `signup form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 422 x 302.59 |
| Padding | 0px 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Figma Sans 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.898 |
| Text node | h1.auth_form--header--fr1Af.auth_form--headerBase--dPZBh: Figma Sans 32px/41.6px 500, #000000 @ 0.898, ls -0.32px |
| Transition | none |
| Icon | 18 x 18, colour #000000 @ 0.898, fill #000000 |
| Painted layers | button.brand_buttons--brandButton--Y6xZJ.auth_view--brandButton--dD0L7 358.0x48.0 border T:1px solid #2c2c2c / R:1px solid #2c2c2c / B:1px solid #2c2c2c / L:1px solid #2c2c2c r 8px; input.lazy_input--lazyInput--akTHe 358.0x53.0 bg #000000 @ 0.05 r 6px; button.brand_buttons--brandButton--Y6xZJ.auth_view--brandButton--dD0L7 358.0x48.0 bg #2c2c2c r 8px |
| How | at rest |

Crops: `signup-panel-default.png`.

#### signup-google

Google SSO button (signup). The "Continue with Google" button on /signup; measured, never pressed.

Page: signup. Selector: `signup Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 358 x 48 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | 1px solid #2c2c2c | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dashed #2c2c2c offset 4px | = |
| Font | Figma Sans 16px/24px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.898 | = | = | = |
| Text node | span.brand_buttons--googleText--8KC1c: Figma Sans 18px/25.2px 480, #000000 @ 0.898, ls -0.09px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #000000 @ 0.898, fill #000000 | = | = | = |
| Painted layers | button.brand_buttons--brandButton--Y6xZJ.auth_view--brandButton--dD0L7 358.0x48.0 border T:1px solid #2c2c2c / R:1px solid #2c2c2c / B:1px solid #2c2c2c / L:1px solid #2c2c2c r 8px | = | button.brand_buttons--brandButton--Y6xZJ.auth_view--brandButton--dD0L7 358.0x48.0 border T:1px solid #2c2c2c / R:1px solid #2c2c2c / B:1px solid #2c2c2c / L:1px solid #2c2c2c r 8px outline 2px dashed #2c2c2c offset 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-google-default.png`, `signup-google-hover.png`, `signup-google-focus-visible.png`, `signup-google-pressed.png`.

#### signup-email

Email field (signup). The e-mail input on the sign-up card; focused and typed into then cleared — never submitted.

Page: signup. Selector: `signup input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 358 x 53 | = | = |
| Padding | 24px 12px 6px 12px | = | = |
| Border | none | = | = |
| Radius | 6px | = | = |
| Background | #000000 @ 0.05 | = | = |
| Box shadow | none | #444444 0px 0px 0px 2px inset | #444444 0px 0px 0px 2px inset |
| Outline | none | = | = |
| Font | Figma Sans 18px/25px 320 | = | = |
| Letter spacing | -0.09px | = | = |
| Colour | #000000 @ 0.898 | = | = |
| Transition | none | = | = |
| Placeholder | #000000 @ 0.898, opacity 1 | = | = |
| Painted layers | input.lazy_input--lazyInput--akTHe 358.0x53.0 bg #000000 @ 0.05 r 6px | input.lazy_input--lazyInput--akTHe 358.0x53.0 bg #000000 @ 0.05 r 6px shadow #444444 0px 0px 0px 2px inset | input.lazy_input--lazyInput--akTHe 358.0x53.0 bg #000000 @ 0.05 r 6px shadow #444444 0px 0px 0px 2px inset |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `signup-email-default.png`, `signup-email-focused.png`, `signup-email-filled.png`.

#### signup-continue

Continue with email. The "Continue with email" button; its states were measured but the button was never clicked — nothing was submitted.

Page: signup. Selector: `signup Continue with email`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 358 x 48 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | 0px | = | 0px |
| Background | #2c2c2c | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dashed #2c2c2c offset 4px | = |
| Font | Figma Sans 18px/24px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.898 | = | = | = |
| Text node | span.brand_buttons--brandButtonContent--ZFibF: Figma Sans 18px/25.2px 480, #ffffff @ 0.898, ls -0.09px | = | = | = |
| Transition | border-radius 0.16s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 22 x 21, colour #ffffff @ 0.898, fill #ffffff | = | = | = |
| Painted layers | button.brand_buttons--brandButton--Y6xZJ.auth_view--brandButton--dD0L7 358.0x48.0 bg #2c2c2c r 8px | button.brand_buttons--brandButton--Y6xZJ.auth_view--brandButton--dD0L7 358.0x48.0 bg #2c2c2c | button.brand_buttons--brandButton--Y6xZJ.auth_view--brandButton--dD0L7 358.0x48.0 bg #2c2c2c r 8px outline 2px dashed #2c2c2c offset 4px | button.brand_buttons--brandButton--Y6xZJ.auth_view--brandButton--dD0L7 358.0x48.0 bg #2c2c2c |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-continue-default.png`, `signup-continue-hover.png`, `signup-continue-focus-visible.png`, `signup-continue-pressed.png`.

### Community (product shell)

#### comm-h1

Community headline. "Discover community-made libraries, plugins, icon sets, and more" — the /community masthead in the product shell.

Page: community. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 420 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 24px/32px 500 |
| Letter spacing | -0.019px |
| Colour | #000000 @ 0.898 |
| Text node | span.hero--textElement---kwB-.hero--highlightedTextElement--PWmWw: Inter 24px/32px 500, #007be5, ls -0.019px |
| Transition | none |
| Cursor | default |
| Icon | 92 x 52.9, colour #007be5, fill #000000 |
| Painted layers | img.hero--pluginImg--3qnJi 19.8x19.8 r 8px shadow #000000 @ 0 0px 21px 6px 0px, #000000 @ 0.01 0px 14px 5px 0px, #000000 @ 0.05 0px 8px 5px 0px, #000000 @ 0.09 0px 3px 3px 0px, #000000 @ 0.1 0px 1px 2px 0px; img.hero--pluginImg--3qnJi 19.8x19.8 r 8px shadow #000000 @ 0 0px 21px 6px 0px, #000000 @ 0.01 0px 14px 5px 0px, #000000 @ 0.05 0px 8px 5px 0px, #000000 @ 0.09 0px 3px 3px 0px, #000000 @ 0.1 0px 1px 2px 0px; img.hero--pluginImg--3qnJi 18.1x18.1 r 8px shadow #000000 @ 0 0px 21px 6px 0px, #000000 @ 0.01 0px 14px 5px 0px, #000000 @ 0.05 0px 8px 5px 0px, #000000 @ 0.09 0px 3px 3px 0px, #000000 @ 0.1 0px 1px 2px 0px; img.hero--pluginImg--3qnJi 19.8x19.8 r 8px shadow #000000 @ 0 0px 21px 6px 0px, #000000 @ 0.01 0px 14px 5px 0px, #000000 @ 0.05 0px 8px 5px 0px, #000000 @ 0.09 0px 3px 3px 0px, #000000 @ 0.1 0px 1px 2px 0px; img.hero--pluginImg--3qnJi 19.8x19.8 r 8px shadow #000000 @ 0 0px 21px 6px 0px, #000000 @ 0.01 0px 14px 5px 0px, #000000 @ 0.05 0px 8px 5px 0px, #000000 @ 0.09 0px 3px 3px 0px, #000000 @ 0.1 0px 1px 2px 0px; img.hero--pluginImg--3qnJi 18.1x18.1 r 8px shadow #000000 @ 0 0px 21px 6px 0px, #000000 @ 0.01 0px 14px 5px 0px, #000000 @ 0.05 0px 8px 5px 0px, #000000 @ 0.09 0px 3px 3px 0px, #000000 @ 0.1 0px 1px 2px 0px |
| How | at rest |

Crops: `comm-h1-default.png`.

#### comm-search

Community search. The "Search for resources like …" input; focused and typed into then cleared — never searched.

Page: community. Selector: `community search input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 284 x 40 | = | 252 x 40 |
| Padding | 0px 8px 0px 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 11px/16px 450 | = | = |
| Letter spacing | 0.05504px | = | = |
| Colour | #000000 @ 0.898 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000 @ 0.3, opacity 1 | = | = |
| Ancestor paint | 1 up div bg #f5f5f5 shadow #000000 @ 0 0px 0px 0px 1px inset | 1 up div bg #f5f5f5 shadow #0d99ff 0px 0px 0px 1px inset | 1 up div bg #f5f5f5 shadow #0d99ff 0px 0px 0px 1px inset |
| How | at rest | clicked into the field | typed "portfolio", then deleted; nothing sent |

Crops: `comm-search-default.png`, `comm-search-focused.png`, `comm-search-filled.png`.

#### comm-cat

Category button. A category filter button (Design resources / Websites / Extensions / Whiteboarding / Presentations); measured at rest, never toggled.

Page: community. Selector: `community category button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 146.95 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 5px | = | = | = |
| Background | transparent | #f5f5f5 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #0d99ff offset 1px | = |
| Font | Inter 13px/24px 500 | = | = | = |
| Letter spacing | -0.003px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 8 x 8, colour #000000, fill #000000 @ 0.898 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button._19xx72g0.nav_category_selector_2--navCategorySelectorTextHover--V2Ws8 147.0x32.0 bg #f5f5f5 r 5px | button._19xx72g0.nav_category_selector_2--navCategorySelectorText--V2TK0 147.0x32.0 r 5px outline 1px solid #0d99ff offset 1px | = |

Crops: `comm-cat-default.png`, `comm-cat-hover.png`, `comm-cat-focus-visible.png`, `comm-cat-pressed.png`.

#### comm-login

Community Log in. The product-shell "Log in" button; measured, never pressed.

Page: community. Selector: `community Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 34.03 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 11px/16px 400 | = | = | = |
| Letter spacing | 0.005px | = | = | = |
| Colour | #000000 @ 0.898 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | button._19xx72g0.auth_buttons--logInButton--hl0bb 34.0x32.0 bg #ffffff r 6px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `comm-login-default.png`, `comm-login-hover.png`, `comm-login-focus-visible.png`, `comm-login-pressed.png`.

#### comm-signup

Community Sign up. The product-shell "Sign up" button; measured, never pressed.

Page: community. Selector: `community Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 70.05 x 32 | = | = | = |
| Padding | 7px 13px | = | 6px 12px | = |
| Border | 1px solid #000000 @ 0.898 | = | 2px solid #0d99ff | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | = | = | #e6e6e6 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 11px/16px 400 | = | = | = |
| Letter spacing | 0.005px | = | = | = |
| Colour | #000000 @ 0.898 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | button._19xx72g0.auth_buttons--signUpButton--T74jF 70.0x32.0 bg #ffffff border T:1px solid #000000 @ 0.898 / R:1px solid #000000 @ 0.898 / B:1px solid #000000 @ 0.898 / L:1px solid #000000 @ 0.898 r 6px | = | button._19xx72g0.auth_buttons--signUpButton--T74jF 70.0x32.0 bg #ffffff border T:2px solid #0d99ff / R:2px solid #0d99ff / B:2px solid #0d99ff / L:2px solid #0d99ff r 6px | button._19xx72g0.auth_buttons--signUpButton--T74jF 70.0x32.0 bg #e6e6e6 border T:1px solid #000000 @ 0.898 / R:1px solid #000000 @ 0.898 / B:1px solid #000000 @ 0.898 / L:1px solid #000000 @ 0.898 r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `comm-signup-default.png`, `comm-signup-hover.png`, `comm-signup-focus-visible.png`, `comm-signup-pressed.png`.

#### comm-banner-nav

Banner carousel control. The hero banner carousel's "Next banner" control — a local UI toggle; measured, never cycled.

Page: community. Selector: `community Next banner`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #e6e6e6 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0d99ff offset 2px | = |
| Font | Inter 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.898 | = | = | = |
| Transition | none | = | = | = |
| Icon | 16 x 16, colour #000000 @ 0.898 | = | = | = |
| Painted layers | button._19xx72g0 24.0x24.0 bg #ffffff border T:1px solid #e6e6e6 / R:1px solid #e6e6e6 / B:1px solid #e6e6e6 / L:1px solid #e6e6e6 r 9999px | button._19xx72g0 24.0x24.0 bg #f5f5f5 border T:1px solid #e6e6e6 / R:1px solid #e6e6e6 / B:1px solid #e6e6e6 / L:1px solid #e6e6e6 r 9999px | button._19xx72g0 24.0x24.0 bg #ffffff border T:1px solid #e6e6e6 / R:1px solid #e6e6e6 / B:1px solid #e6e6e6 / L:1px solid #e6e6e6 r 9999px outline 2px solid #0d99ff offset 2px | button._19xx72g0 24.0x24.0 bg #f5f5f5 border T:1px solid #e6e6e6 / R:1px solid #e6e6e6 / B:1px solid #e6e6e6 / L:1px solid #e6e6e6 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `comm-banner-nav-default.png`, `comm-banner-nav-hover.png`, `comm-banner-nav-focus-visible.png`, `comm-banner-nav-pressed.png`.

#### comm-card

Resource card. A community "Riff" card (thumbnail, title, author, like count); measured, never followed.

Page: community. Selector: `community Riff card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 394.66 x 532.81 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| How | at rest | mouse hover |
| Cursor | - | pointer |

Crops: `comm-card-default.png`, `comm-card-hover.png`.

#### comm-like

Like button. A resource card's like button; measured, never pressed (a like would write to an account).

Page: community. Selector: `community like button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 20 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | 5px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #0d99ff offset 1px | = |
| Font | Inter 14px/24px 600 | = | = | = |
| Letter spacing | -0.006px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | = | = | = |
| ::after | 65.875px x 30px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Ancestor paint | 1 up div bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.base_like_button--buttonContainerPrettyCompact--6qXsV.base_like_button--buttonContainerPretty--KdBsv 20.0x20.0 r 5px outline 1px solid #0d99ff offset 1px | = |

Crops: `comm-like-default.png`, `comm-like-hover.png`, `comm-like-focus-visible.png`, `comm-like-pressed.png`.

### Prompt surfaces

#### prompt-h1

Make headline. The /make masthead — "Figma Make".

Page: make. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672 x 48.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | figmaSans 44px/48.4px 400 |
| Letter spacing | -0.66px |
| Colour | #000000 |
| Transition | none |
| Cursor | text |
| Icon | 39.59 x 39.59, colour #000000 |
| How | at rest |

Crops: `prompt-h1-default.png`.

#### prompt-textarea

Prompt textarea. The "What do you want to make?" prompt box on /make; focused and typed into then cleared — never submitted.

Page: make. Selector: `make textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 672 x 97.19 | = | = |
| Padding | 36px 96px 36px 32px | 35px 95px 35px 31px | 35px 95px 35px 31px |
| Border | 1px solid oklch(0 0 none / 0.16) | 2px solid #000000 | 2px solid #000000 |
| Radius | 24px | = | = |
| Background | #ffffff | = | = |
| Box shadow | oklch(0 0 none / 0.1) 0px 24px 70px 0px | = | = |
| Outline | none | = | = |
| Font | figmaSans 16px/22.4px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | box-shadow, border-color 0.18s, 0.18s ease, ease delay 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | oklch(0 0 none / 0.54), opacity 1 | = | = |
| Painted layers | textarea.fig-14ig7xd 672.0x97.2 bg #ffffff border T:1px solid oklch(0 0 none / 0.16) / R:1px solid oklch(0 0 none / 0.16) / B:1px solid oklch(0 0 none / 0.16) / L:1px solid oklch(0 0 none / 0.16) r 24px shadow oklch(0 0 none / 0.1) 0px 24px 70px 0px | textarea.fig-14ig7xd 672.0x97.2 bg #ffffff border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 24px shadow oklch(0 0 none / 0.1) 0px 24px 70px 0px | textarea.fig-14ig7xd 672.0x97.2 bg #ffffff border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 24px shadow oklch(0 0 none / 0.1) 0px 24px 70px 0px |
| How | at rest | clicked into the field | typed "A landing page for a coffee roaster", then deleted; nothing sent |

Crops: `prompt-textarea-default.png`, `prompt-textarea-focused.png`, `prompt-textarea-filled.png`.

#### prompt-submit

Prompt submit. The prompt box's icon-only submit button; its states were measured but the button was never clicked — nothing was sent.

Page: make. Selector: `make submit button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #d2d9e2 | = | = | #4d49fc |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dashed #000000 offset 4px | = |
| Font | figmaSans 16px/18.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background, box-shadow 0.18s, 0.18s ease-out, ease-out delay 0s, 0s | = | = | = |
| Opacity | 0.6 | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 20, colour #ffffff | = | = | = |
| Painted layers | button.fig-rfrio7 48.0x48.0 bg #d2d9e2 r 9999px | = | button.fig-rfrio7 48.0x48.0 bg #d2d9e2 r 9999px outline 2px dashed #000000 offset 4px | button.fig-rfrio7 48.0x48.0 bg #4d49fc r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `prompt-submit-default.png`, `prompt-submit-hover.png`, `prompt-submit-focus-visible.png`, `prompt-submit-pressed.png`.

### Blog, downloads and careers

#### dl-h1

Downloads headline. The /downloads masthead — "Figma downloads".

Page: downloads. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 780 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | figmaSans 72px/72px 400 |
| Letter spacing | -1.44px |
| Colour | #000000 |
| Transition | none |
| Cursor | text |
| How | at rest |

Crops: `dl-h1-default.png`.

#### dl-btn

Download link. The "Desktop app for macOS" download link (desktop apps, mobile apps, font installers, the Chrome extension); measured, never followed.

Page: downloads. Selector: `downloads platform link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 195 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dashed #000000 offset 4px | = |
| Font | figmaSans 18px/25.2px 330 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 195.0x20.0 outline 2px dashed #000000 offset 4px | = |

Crops: `dl-btn-default.png`, `dl-btn-hover.png`, `dl-btn-focus-visible.png`, `dl-btn-pressed.png`.

#### blog-topics

Topics button. The blog index's "Topics" filter button — a local UI toggle; measured, never toggled.

Page: blog. Selector: `blog Topics`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 105.14 x 27 | = | = | = |
| Padding | 8px 0px 0px 32px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dashed #ffffff offset 4px | = |
| Font | figmaSans 18px/18px 330 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 11.14 x 13, colour #ffffff | = | = | = |
| ::before | 1px x 19px, absolute, bg #ffffff, radius 0px | = | = | = |
| Painted layers | button::before.fig-1xfqluc 1pxx19px bg #ffffff | = | button.fig-1xfqluc 105.1x27.0 outline 1px dashed #ffffff offset 4px; button::before.fig-1xfqluc 1pxx19px bg #ffffff | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `blog-topics-default.png`, `blog-topics-hover.png`, `blog-topics-focus-visible.png`, `blog-topics-pressed.png`.

#### blog-search

Search button. The blog index's "Search" button — a local UI toggle; measured, never toggled.

Page: blog. Selector: `blog Search`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 27 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px dashed #ffffff offset 4px | = |
| Font | figmaSans 18px/25.2px 330 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.fig-11smye 40.0x27.0 outline 1px dashed #ffffff offset 4px | = |

Crops: `blog-search-default.png`, `blog-search-hover.png`, `blog-search-focus-visible.png`, `blog-search-pressed.png`.

#### blog-subscribe

Newsletter field. The editorial-newsletter e-mail input in the blog rail; focused and typed into then cleared — never subscribed.

Page: blog. Selector: `blog newsletter input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 743 x 53.89 | = | = |
| Padding | 0px 70px 0px 0px | = | = |
| Border | T: none; R: none; B: 1px solid #ffffff; L: none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | figmaSans 46px/52.9px 400 | = | = |
| Letter spacing | -0.69px | = | = |
| Colour | #ffffff | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | #757575, opacity 0 | #757575, opacity 0 |
| Painted layers | input.fig-1fitj2g 743.0x53.9 border B:1px solid #ffffff | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `blog-subscribe-default.png`, `blog-subscribe-focused.png`, `blog-subscribe-filled.png`.

#### careers-cta

Careers CTA. The "See open positions" link on /careers; measured, never followed.

Page: careers. Selector: `careers See open positions`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 194 x 46.39 | = | = | = |
| Padding | 12px 22px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dashed #000000 offset 4px | = |
| Font | figmaSans 16px/23.2px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.btn-text.fig-1v6pe89: figmaSans 16px/22.4px 400, #ffffff | = | = | = |
| Transition | background, box-shadow 0.18s, 0.18s ease-out, ease-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = |
| Painted layers | a.fig-1jz30fp 194.0x46.4 bg #000000 r 8px | = | a.fig-1jz30fp 194.0x46.4 bg #000000 r 8px outline 2px dashed #000000 offset 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `careers-cta-default.png`, `careers-cta-hover.png`, `careers-cta-focus-visible.png`, `careers-cta-pressed.png`.

#### job-link

Job link. An open-position link in the careers list; measured, never followed.

Page: careers. Selector: `careers job link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 246 x 20 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | figmaSans 18px/25.2px 330 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.fig-11wp5ad: figmaSans 18px/25.2px 330, #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `job-link-default.png`, `job-link-hover.png`.

### FAQ accordions

#### faq-acc

FAQ accordion. A question row in the /design-systems FAQ (all accordions mount open); the closed state was measured after clicking the row — a local UI toggle.

Page: faq. Selector: `FAQ accordion button`. States: default, closed.

| Property | default | closed |
|---|---|---|
| Size (w x h) | 720 x 97.59 | 720 x 105.59 |
| Padding | 32px 0px 24px 0px | 32px 0px |
| Gap | 16px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | figmaSans 32px/41.6px 400 | = |
| Letter spacing | -0.32px | = |
| Colour | #000000 | = |
| Transition | padding 0.25s ease | = |
| Cursor | pointer | = |
| Icon | 32 x 32, colour #000000 | = |
| How | at rest | own toggle |

Crops: `faq-acc-default.png`, `faq-acc-closed.png`.

### Mobile (390 wide)

#### m-topbar

Mobile top bar. The phone header at 390 wide: the Figma mark, "Get started for free", the nav button and the locale button.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | oklch(0 0 none / 0.16) 0px 1px 0px 0px |
| Outline | none |
| Font | figmaSans 16px/23.2px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.btn-text.fig-1v6pe89: figmaSans 16px/22.4px 400, #ffffff |
| Transition | none |
| Icon | 32 x 48, colour #000000 |
| Painted layers | header.fig-scjrgl 390.0x72.0 bg #ffffff shadow oklch(0 0 none / 0.16) 0px 1px 0px 0px; span::after.nav-highlight autox1px bg #000000; a.fig-42wdr4 0.0x0.0 bg oklch(0 0 none / 0) r 8px shadow oklch(0 0 none / 0.16) 0px 0px 0px 1px inset; a.fig-13b0elo 0.0x0.0 bg #000000 r 8px; a.fig-4rcs94 198.0x46.4 bg #000000 r 8px |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-cta

Mobile header CTA. The header "Get started for free" pill at 390 wide; measured never followed.

Page: mobile. Selector: `mobile header Get started for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 198 x 46.39 | = | = | = |
| Padding | 12px 22px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #000000 | oklch(0 0 none / 0.85) | = | oklch(0 0 none / 0.85) |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dashed #000000 offset 4px | = |
| Font | figmaSans 18px/25.2px 330 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.btn-text.fig-1v6pe89: figmaSans 16px/22.4px 400, #ffffff | = | = | = |
| Transition | background, box-shadow 0.18s, 0.18s ease-out, ease-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = |
| Painted layers | a.fig-4rcs94 198.0x46.4 bg #000000 r 8px | a.fig-4rcs94 198.0x46.4 bg oklch(0 0 none / 0.85) r 8px | a.fig-4rcs94 198.0x46.4 bg #000000 r 8px outline 2px dashed #000000 offset 4px | a.fig-4rcs94 198.0x46.4 bg oklch(0 0 none / 0.85) r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-cta-default.png`, `m-cta-hover.png`, `m-cta-focus-visible.png`, `m-cta-pressed.png`.

#### m-menu-btn

Mobile menu button. The "Open navigation menu" button — a local UI toggle; the opened state was measured after activating it.

Page: mobile. Selector: `button[aria-label=Open navigation menu]`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = | = |
| Padding | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px dashed #000000 offset 4px | = | = |
| Font | figmaSans 16px/23.2px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | default | = | = | = | = |
| Icon | 24 x 24, colour #000000 | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | button.fig-1aem8bs 40.0x40.0 outline 2px dashed #000000 offset 4px | = | = |

Crops: `m-menu-btn-default.png`, `m-menu-btn-hover.png`, `m-menu-btn-focus-visible.png`, `m-menu-btn-pressed.png`, `m-menu-btn-opened.png`.

#### m-drawer

Mobile nav overlay. The accordion nav inside the nav overlay opened by the menu button (Products/Solutions/Community/Resources accordions plus the page links); its links were never followed.

Page: mobile. Selector: `mobile nav overlay accordion`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 844 |
| Padding | 110px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | figmaSans 16px/23.2px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.nav-highlight: figmaSans 24px/28.8px 400, #000000, ls -0.66px |
| Transition | none |
| Icon | 24 x 24, colour #000000 |
| Painted layers | div.fig-5w9uj6 358.0x371.8 border B:1px solid oklch(0 0 none / 0.16); button.dropdown-label.fig-1wo6hfm 358.0x61.8 border T:1px solid oklch(0 0 none / 0.16); span::after.nav-highlight autox1px bg #000000; span::after.nav-highlight autox1px bg #000000; span::after.nav-highlight autox1px bg #000000; span::after.nav-highlight autox1px bg #000000 |
| Ancestor paint | 1 up div.fig-eppsle bg #ffffff |
| How | at rest |

Crops: `m-drawer-default.png`.

#### m-hero-h1

Mobile hero headline. The masthead at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | figmaSans 36px/36px 400 |
| Letter spacing | -1.25px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-hero-cta

Mobile hero CTA. The hero "Get started" pill at 390 wide; measured never followed.

Page: mobile. Selector: `mobile hero Get started`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 196.75 x 76.8 | = | = | = |
| Padding | 24px 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | #000000 | #000000 @ 0.946565 | = | oklch(0 0 none / 0.85) |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dashed #000000 offset 4px | = |
| Font | figmaSans 16px/23.2px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.btn-text.fig-2vtqnm: figmaSans 24px/28.8px 400, #ffffff, ls -0.66px | = | = | = |
| Transition | background, box-shadow 0.18s, 0.18s ease-out, ease-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 36 x 36, colour #ffffff | = | = | = |
| Painted layers | a.fig-1ytmgio 196.8x76.8 bg #000000 r 16px | a.fig-1ytmgio 196.8x76.8 bg #000000 @ 0.946565 r 16px | a.fig-1ytmgio 196.8x76.8 bg #000000 r 16px outline 2px dashed #000000 offset 4px | a.fig-1ytmgio 196.8x76.8 bg oklch(0 0 none / 0.85) r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-hero-cta-default.png`, `m-hero-cta-hover.png`, `m-hero-cta-focus-visible.png`, `m-hero-cta-pressed.png`.

## Transitions declared in the readable stylesheets

figma.com serves most of its CSS as inline Emotion `<style data-emotion>` blocks plus linked `/_netlify/_next/static/css` bundles, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- blog: `transform 250ms`, `200ms`, `180ms ease-out`, `transform 180ms ease-out`, `opacity 200ms cubic-bezier(0.25, 0, 0.75, 1)`, `transform 400ms cubic-bezier(0.8, 0, 0.2, 1)`, `width 400ms cubic-bezier(0.8, 0, 0.2, 1)`, `background-size 400ms cubic-bezier(0.8, 0, 0.2, 1)`, `background 180ms ease-out, box-shadow 180ms ease-out`, `opacity 180ms ease-out`, `translate 180ms ease-out`, `background-color 10000s linear, color 10000s linear`

- careers: `transform 250ms`, `200ms`, `background 0.4s cubic-bezier(0.8, 0, 0.2, 1)`, `transform 250ms, opacity 250ms`, `background 180ms ease-out, box-shadow 180ms ease-out`, `opacity 180ms ease-out`, `translate 180ms ease-out`, `180ms ease-out`, `transform 180ms ease-out`

- community: `opacity 0.2s ease-in-out`, `opacity 0.4s ease-in-out`, `0.15s`, `0.2s`, `background-color 0.15s, border-color 0.15s`, `height 0.3s, max-height 0.3s`, `height 0.3s`, `mask-size, mask-position, -webkit-mask-size, -webkit-mask-position 0.2s ease-in-out`, `opacity 0.15s`, `opacity 0.1s ease-in-out`, `opacity 0.25s`, `opacity 0.3s`

- contact: `transform 250ms`, `200ms`, `background 0.4s cubic-bezier(0.8, 0, 0.2, 1)`, `transform 250ms, opacity 250ms`, `background 180ms ease-out, box-shadow 180ms ease-out`, `opacity 180ms ease-out`, `translate 180ms ease-out`

- downloads: `transform 250ms`, `200ms`, `background 0.4s cubic-bezier(0.8, 0, 0.2, 1)`, `transform 250ms, opacity 250ms`, `background 180ms ease-out, box-shadow 180ms ease-out`, `opacity 180ms ease-out`, `translate 180ms ease-out`, `180ms ease-out`, `transform 180ms ease-out`

- faq: `transform 250ms`, `200ms`, `background 0.4s cubic-bezier(0.8, 0, 0.2, 1)`, `transform 250ms, opacity 250ms`, `background 180ms ease-out, box-shadow 180ms ease-out`, `opacity 180ms ease-out`, `translate 180ms ease-out`, `180ms ease-out`, `transform 180ms ease-out`, `padding 250ms`, `background 180ms ease-out, border-radius 180ms ease-out, box-shadow 180ms ease-out`

- home: `transform 250ms`, `200ms`, `background 0.4s cubic-bezier(0.8, 0, 0.2, 1)`, `transform 250ms, opacity 250ms`, `background 180ms ease-out, box-shadow 180ms ease-out`, `opacity 180ms ease-out`, `translate 180ms ease-out`, `180ms ease-out`, `transform 180ms ease-out`, `opacity var(--fig-animation-400, 400ms) ease,transform var(--fig-animation-400, 400ms) ease`, `none`, `background 180ms ease-out, border-radius 180ms ease-out, box-shadow 180ms ease-out`

- login: `opacity 0.2s ease-in-out`, `opacity 0.4s ease-in-out`, `opacity 0.25s`, `none`, `0.2s`, `border-radius 0.16s ease-out`, `translate 0.16s ease-out`, `opacity 0.16s ease-out`, `height var(--duration-sm) cubic-bezier(.645,.045,.355,1)`, `background var(--duration-sm) cubic-bezier(.645,.045,.355,1)`, `left 70ms ease-out, width 70ms ease-out`, `mask-size, mask-position`

- make: `transform 250ms`, `200ms`, `background 0.4s cubic-bezier(0.8, 0, 0.2, 1)`, `transform 250ms, opacity 250ms`, `background 180ms ease-out, box-shadow 180ms ease-out`, `opacity 180ms ease-out`, `translate 180ms ease-out`, `top var(--fig-animation-180, 180ms) ease`, `box-shadow var(--fig-animation-180, 180ms) ease,border-color var(--fig-animation-180, 180ms) ease`, `opacity var(--fig-animation-180, 180ms) ease-out`, `padding 250ms, background 180ms ease-out`, `max-width 250ms`

- pricing: `transform 250ms`, `200ms`, `background 0.4s cubic-bezier(0.8, 0, 0.2, 1)`, `transform 250ms, opacity 250ms`, `background 180ms ease-out, box-shadow 180ms ease-out`, `opacity 180ms ease-out`, `translate 180ms ease-out`, `180ms ease-out`, `transform 180ms ease-out`, `padding 250ms`

- signup: `opacity 0.2s ease-in-out`, `opacity 0.4s ease-in-out`, `opacity 0.25s`, `none`, `0.2s`, `border-radius 0.16s ease-out`, `translate 0.16s ease-out`, `opacity 0.16s ease-out`, `height var(--duration-sm) cubic-bezier(.645,.045,.355,1)`, `background var(--duration-sm) cubic-bezier(.645,.045,.355,1)`, `left 70ms ease-out, width 70ms ease-out`, `mask-size, mask-position`

## Reduced motion

- home (`header a[href="/signup"], header a[href="https://www.figma.com/signup"]` under prefers-reduced-motion): transition `background 0.18s ease-out, box-shadow 0.18s ease-out`, animation `none 0s ease 0s 1 normal none running`, html scroll-behavior `smooth`
