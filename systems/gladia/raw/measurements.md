# Gladia component measurements

Computed styles read from gladia.io by `tools/capture/public/measure.mjs`, first read 2026-11-16, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the dark :root marketing pages (home, product, pricing, demo-request and the index pages), /library on the light body.light-mode scope, /blog on the legacy Webflow stack, the Mintlify docs site at docs.gladia.io (its own token layer and a real light/dark preference), the product auth shell at app.gladia.io / and /signup, and the mobile nav sheet — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). Later recaptures merge into the same file: every entry names the run date its states were read under "Read", and a state a re-read missed keeps its earlier reading under its earlier date with the failed attempt beside it. The marketing site ships no theme control: an emulated prefers-color-scheme pass resolved :root identically, and body.light-mode is the only light scope a page mounts. One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into, or a real keyboard focus on a toggle control (a click there would flip the value, so it is never clicked); `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Site chrome

#### mkt-header

Site header. The floating rounded glass navbar at the top of every marketing page: the Gladia wordmark, the Product/Solutions/Developers/Resources/Company mega-menu triggers, Pricing, "Request a demo" and the signup CTA.

Page: home. Selector: `header.site-nav nav.navbar`. States: default.
Read: 2026-11-16.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 72 |
| Padding | 0px |
| Border | 1px solid #1f1f1f |
| Radius | 20px |
| Background | #000000 @ 0.65 |
| Box shadow | none |
| Backdrop filter | blur(40px) |
| Outline | none |
| Font | Suisse Intl 16px/22.4px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.mega-menu-nav-label: Suisse Intl 15px/normal 400, #ffffff @ 0.68 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 109.94 x 28, colour #ffffff |
| Painted layers | nav.navbar 1200.0x72.0 bg #000000 @ 0.65 border T:1px solid #1f1f1f / R:1px solid #1f1f1f / B:1px solid #1f1f1f / L:1px solid #1f1f1f r 20px; a.btn.btn-secondary 146.0x32.0 bg #1c1c1e border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 40px; a.btn.btn-primary 81.0x32.0 bg #ffffff r 40px; button.navbar-menu-toggle 0.0x0.0 bg #ffffff @ 0.04 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 999px; span.navbar-menu-toggle-line 0.0x0.0 bg #ffffff r 1px; span.navbar-menu-toggle-line 0.0x0.0 bg #ffffff r 1px |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The inline-SVG Gladia symbol + wordmark in the header, linking home.

Page: home. Selector: `header a.navbar-logo`. States: default.
Read: 2026-11-16.

| Property | default |
|---|---|
| Size (w x h) | 323.5 x 28 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/22.4px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| Icon | 109.94 x 28, colour #ffffff |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-menu-btn

Mega-menu trigger. The "Product" header button — a hover-intent trigger whose aria-expanded flips while the mega-menu mounts (the opened panel is the mega-panel component below). Hover is the site's own activation, focus+Enter the fallback.

Page: home. Selector: `button[data-menu=product]`. States: default, hover, focus-visible, pressed.
Read: 2026-11-16.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 55 x 31 | 73 x 31 | 73 x 31 | 73 x 31 |
| Padding | 6px 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #947afc offset 2px | = |
| Font | Suisse Intl 15px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #cccccc | #ffffff | #ffffff | #ffffff |
| Text node | span.mega-menu-nav-label: Suisse Intl 15px/normal 400, #ffffff @ 0.68 | span.mega-menu-nav-label: Suisse Intl 15px/normal 400, #ffffff | span.mega-menu-nav-label: Suisse Intl 15px/normal 400, #ffffff | span.mega-menu-nav-label: Suisse Intl 15px/normal 400, #ffffff |
| Transition | color 0.16s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 12, colour #cccccc | 12 x 12, colour #ffffff | 12 x 12, colour #ffffff | 12 x 12, colour #ffffff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.is-active 73.0x31.0 outline 2px solid #947afc offset 2px | = |

Crops: `nav-menu-btn-default.png`, `nav-menu-btn-hover.png`, `nav-menu-btn-focus-visible.png`, `nav-menu-btn-pressed.png`.

#### mega-panel

Mega-menu panel. The product mega-menu panel opened by the "Product" trigger — glass card with product and feature links; its links were never followed.

Page: home. Selector: `.mega-menu-panel`. States: default.
Read: 2026-11-16.

| Property | default |
|---|---|
| Size (w x h) | 1080 x 361.66 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/22.4px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.mega-menu-col-title: Geist Mono 11px/15.4px 400, #947afc @ 0.95, ls 1.54px |
| Transition | none |
| Painted layers | div.mega-menu-panel-body.mega-menu-panel-body--product 1080.0x361.7 bg #000000 r 23px; div.mega-menu-grid.mega-menu-grid--flat 0.0x0.0 bg #000000; div.mega-menu-overview-card 360.0x361.7 image linear-gradient(160deg, #ffffff @ 0.06 0%, #ffffff @ 0 42%), linear-gradient(#000000 @ 0.4 border R:1px solid #ffffff @ 0.1 shadow #ffffff @ 0.14 0px 1px 0px 0px inset; div::before.mega-menu-overview-card 1pxx361.656px image linear-gradient(#ffffff @ 0.45 0%, #ffffff @ 0.08 45%, #947afc @ 0.4 100%); span.btn.btn-primary 138.0x32.0 bg #ffffff r 40px; div.mega-menu-overview-links 359.0x105.0 border T:1px solid #ffffff @ 0.08 |
| Ancestor paint | 3 up div.mega-menu.is-visible bg #060608 @ 0.94 shadow #000000 @ 0.72 0px 32px 100px 0px, #ffffff @ 0.04 0px 0px 0px 1px inset, #947afc @ 0.07 0px 0px 140px 0px |
| How | at rest |

Crops: `mega-panel-default.png`.

#### mega-item

Mega-menu item. A product link inside the opened mega-menu; measured, never followed.

Page: home. Selector: `.mega-menu a`. States: default, hover.
Read: 2026-11-16.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 359 x 172.98 | = |
| Padding | 0px 32px 24px 32px | = |
| Gap | 16px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 16px/22.4px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | span.mega-menu-col-title: Geist Mono 11px/15.4px 400, #947afc @ 0.95, ls 1.54px | = |
| Transition | background 0.16s cubic-bezier(0, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | span.btn.btn-primary 138.0x32.0 bg #ffffff r 40px | span.btn.btn-primary 144.8x32.6 bg #ffffff r 40px |
| Ancestor paint | 1 up div.mega-menu-overview-card shadow #ffffff @ 0.14 0px 1px 0px 0px inset | = |
| How | at rest | mouse hover |

Crops: `mega-item-default.png`, `mega-item-hover.png`.

#### nav-pricing

Nav link. The "Pricing" header link; measured, never followed.

Page: home. Selector: `header a Pricing`. States: default, hover, focus-visible, pressed.
Read: 2026-11-16.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 46 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 15px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.68 | #ffffff | #ffffff | #ffffff |
| Transition | color, transform 0.16s, 0.16s cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 3, 0) | matrix(1, 0, 0, 1, 3, 0) | matrix(1, 0, 0, 1, 3, 0) |
| Painted layers | - | = | a 46.0x21.0 outline 1px auto #101010 offset 1px | = |

Crops: `nav-pricing-default.png`, `nav-pricing-hover.png`, `nav-pricing-focus-visible.png`, `nav-pricing-pressed.png`.

#### nav-demo

Demo link. The "Request a demo" header link to /demo-request; measured, never followed.

Page: home. Selector: `header a Request a demo`. States: default, hover, focus-visible, pressed.
Read: 2026-11-16.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 146 x 32 | 148.92 x 32.64 | = | 148.92 x 32.64 |
| Padding | 6px 16px | = | = | = |
| Border | 1px solid #ffffff @ 0.12 | = | = | = |
| Radius | 40px | = | = | = |
| Background | #1c1c1e | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 14px/19.6px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.btn-text: Suisse Intl 14px/19.6px 400, #ffffff | = | = | = |
| Transition | transform, box-shadow, background-color, color, border-color, opacity 0.25s, 0.25s, 0.2s, 0.2s, 0.2s, 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1) delay 0s, 0s, 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.btn-secondary 146.0x32.0 bg #1c1c1e border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 40px | a.btn.btn-secondary 148.9x32.6 bg #1c1c1e border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 40px | a.btn.btn-secondary 146.0x32.0 bg #1c1c1e border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 40px outline 1px auto #101010 offset 1px | a.btn.btn-secondary 148.9x32.6 bg #1c1c1e border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 40px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1.02, 0, 0, 1.02, 0, 0) | = | matrix(1.02, 0, 0, 1.02, 0, 0) |

Crops: `nav-demo-default.png`, `nav-demo-hover.png`, `nav-demo-focus-visible.png`, `nav-demo-pressed.png`.

#### nav-cta

Header CTA. The header signup CTA (the brand-purple fill) linking to app.gladia.io/signup; measured, never followed.

Page: home. Selector: `header signup CTA`. States: default, hover, focus-visible, pressed.
Read: 2026-11-16.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81 x 32 | 82.62 x 32.64 | = | 82.62 x 32.64 |
| Padding | 6px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | #ffffff | #ffffff @ 0.88 | = | #ffffff @ 0.88 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 14px/19.6px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.btn-text: Suisse Intl 14px/19.6px 400, #000000 | = | = | = |
| Transition | transform, box-shadow, background-color, color, border-color, opacity 0.25s, 0.25s, 0.2s, 0.2s, 0.2s, 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1) delay 0s, 0s, 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.btn-primary 81.0x32.0 bg #ffffff r 40px | a.btn.btn-primary 82.6x32.6 bg #ffffff @ 0.88 r 40px | a.btn.btn-primary 81.0x32.0 bg #ffffff r 40px outline 1px auto #101010 offset 1px | a.btn.btn-primary 82.6x32.6 bg #ffffff @ 0.88 r 40px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1.02, 0, 0, 1.02, 0, 0) | = | matrix(1.02, 0, 0, 1.02, 0, 0) |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### hero-h1

Hero headline. The home masthead display heading on the dark :root surface.

Page: home. Selector: `h1`. States: default.
Read: 2026-11-16.

| Property | default |
|---|---|
| Size (w x h) | 767.41 x 189.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 79px/94.8px 400 |
| Letter spacing | -1.6px |
| Colour | #000000 |
| Text node | span.hero-line.is-in: Suisse Intl 79px/94.8px 400, #000000, ls -1.6px |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-badge

Hero badge. The announcement badge/pill above the hero headline; measured, never followed.

Page: home. Selector: `hero badge`. States: default.
Read: 2026-11-16.

| Property | default |
|---|---|
| Size (w x h) | 338.11 x 37.59 |
| Padding | 4px 12px 4px 4px |
| Gap | 8px |
| Border | 1px solid #000000 @ 0.12 |
| Radius | 9999px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/22.4px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.pill-badge: Suisse Intl 14px/19.6px 500, #000000 @ 0.8 |
| Transition | border-color 0.16s cubic-bezier(0, 0, 0.2, 1) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Cursor | default |
| Painted layers | div.announce-pill.counter-pill 338.1x37.6 bg #ffffff border T:1px solid #000000 @ 0.12 / R:1px solid #000000 @ 0.12 / B:1px solid #000000 @ 0.12 / L:1px solid #000000 @ 0.12 r 9999px; span.pill-badge 53.0x27.6 bg #000000 @ 0.06 r 9999px; span.badge-dot.pulse 6.0x6.0 bg #947afc r 50%; span::after.badge-dot.pulse 12pxx12px bg #947afc r 50% |
| How | at rest |

Crops: `hero-badge-default.png`.

#### section-h2

Section heading. A marketing section heading further down the home page — a display-size h2, so transient microcopy never counts.

Page: home. Selector: `h2 (display size)`. States: default.
Read: 2026-11-16.

| Property | default |
|---|---|
| Size (w x h) | 523.19 x 57.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 48px/57.6px 400 |
| Letter spacing | -0.96px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

#### glass-card

Glass card. A frosted-glass marketing card (the site's --bg-glass + blur + hairline border treatment); measured, never followed.

Page: home. Selector: `.glass-card`. States: .
Read: .

Not found on the page at capture time.

### Footer

#### footer

Footer. The page footer: sitemap columns, social icons, legal links and the Gladia mark.

Page: home. Selector: `footer`. States: default.
Read: 2026-11-16.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 849.38 |
| Padding | 72px 0px 64px 0px |
| Border | T: 1px solid #0c0c0c; R: none; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/22.4px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.footer-column-title: Suisse Intl 14px/19.6px 400, #ffffff |
| Transition | none |
| Icon | 94.23 x 24, colour #ffffff |
| Painted layers | footer.footer 1440.0x849.4 border T:1px solid #0c0c0c; a.footer-cert 141.0x36.2 bg #0c0c0c border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 9999px; a.footer-cert 141.0x36.2 bg #0c0c0c border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 9999px; a.footer-cert 149.0x36.2 bg #0c0c0c border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 9999px; a.footer-cert 170.0x36.2 bg #0c0c0c border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 9999px; div.footer-bottom 1152.0x68.6 border T:1px solid #0c0c0c |
| Ancestor paint | 1 up body.homepage-v3 bg #000000 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer sitemap link; measured, never followed.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.
Read: 2026-11-16.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 211.19 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #a3a3a3 | #ffffff | = | #ffffff |
| Transition | color 0.16s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 211.2x21.0 outline 1px auto #101010 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Product pages

#### prod-h1

Product headline. The /product/speech-to-text-api masthead on the dark surface.

Page: product. Selector: `h1`. States: default.
Read: 2026-11-16.

| Property | default |
|---|---|
| Size (w x h) | 639.98 x 95.03 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 79.2px/95.04px 400 |
| Letter spacing | -3.168px |
| Colour | #ffffff |
| Transition | opacity, transform 0.9s, 0.9s cubic-bezier(0.22, 1, 0.36, 1), cubic-bezier(0.22, 1, 0.36, 1) delay 0.14s |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `prod-h1-default.png`.

#### prod-cta

Product CTA. A call-to-action on the product page; measured, never followed.

Page: product. Selector: `product page CTA`. States: default, hover, focus-visible, pressed.
Read: 2026-11-16.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 146 x 32 | 148.92 x 32.64 | = | 148.92 x 32.64 |
| Padding | 6px 16px | = | = | = |
| Border | 1px solid #ffffff @ 0.12 | = | = | = |
| Radius | 40px | = | = | = |
| Background | #1c1c1e | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 14px/19.6px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.btn-text: Suisse Intl 14px/19.6px 400, #ffffff | = | = | = |
| Transition | transform 0.16s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.btn-secondary 146.0x32.0 bg #1c1c1e border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 40px | a.btn.btn-secondary 148.9x32.6 bg #1c1c1e border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 40px | a.btn.btn-secondary 146.0x32.0 bg #1c1c1e border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 40px outline 1px auto #101010 offset 1px | a.btn.btn-secondary 148.9x32.6 bg #1c1c1e border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 40px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1.02, 0, 0, 1.02, 0, 0) | = | matrix(1.02, 0, 0, 1.02, 0, 0) |

Crops: `prod-cta-default.png`, `prod-cta-hover.png`, `prod-cta-focus-visible.png`, `prod-cta-pressed.png`.

#### prod-code

Code sample. A code sample block on the product page — mono face on an elevated surface.

Page: product. Selector: `pre.stt-dev-code__body`. States: default.
Read: 2026-11-16.

| Property | default |
|---|---|
| Size (w x h) | 549.5 x 681.94 |
| Padding | 20px |
| Border | T: 1px solid #ffffff @ 0.08; R: 1px solid #ffffff @ 0.1; B: 1px solid #ffffff @ 0.1; L: 1px solid #ffffff @ 0.1 |
| Radius | 0px 0px 16px 16px |
| Background | #141414 |
| Box shadow | none |
| Outline | none |
| Font | Geist Mono 13px/20.15px 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.82 |
| Text node | code: Geist Mono 13px/20.15px 400, #ffffff @ 0.82 |
| Transition | none |
| Painted layers | pre.stt-dev-code__body 549.5x681.9 bg #141414 border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 0px 0px 16px 16px |
| Ancestor paint | 1 up div.stt-dev-code bg #111111 |
| How | at rest |

Crops: `prod-code-default.png`.

#### prod-feature

Feature heading. A feature section heading on the product page.

Page: product. Selector: `product h2/h3`. States: default.
Read: 2026-11-16.

| Property | default |
|---|---|
| Size (w x h) | 398.41 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 40px/52px 400 |
| Letter spacing | -0.8px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `prod-feature-default.png`.

### Pricing

#### price-h1

Pricing headline. The /pricing masthead.

Page: pricing. Selector: `h1`. States: default.
Read: 2026-11-16.

| Property | default |
|---|---|
| Size (w x h) | 860 x 76.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 64px/76.8px 400 |
| Letter spacing | -1.28px |
| Colour | #ffffff |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `price-h1-default.png`.

#### price-mode-async

Pricing mode: Async. The "Async" half of the pricing-mode segmented toggle (data-pricing-mode, aria-pressed); a local UI toggle that re-prices the grid — the opened state was measured after its own toggle.

Page: pricing. Selector: `button[data-pricing-mode=async]`. States: default, hover, focus-visible, pressed, opened.
Read: 2026-11-16.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 88 x 35.59 | = | = | = | = |
| Padding | 8px 24px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #1a9eff offset 2px | = | = |
| Font | Suisse Intl 14px/19.6px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Transition | background-color, color 0.16s, 0.32s cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1) delay 0s, 0s | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Ancestor paint | 1 up div.pricing-toggle.is-ready bg #0c0c0c @ 0.55 | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | button.pricing-toggle__btn.is-active 88.0x35.6 r 9999px outline 2px solid #1a9eff offset 2px | = | = |

Crops: `price-mode-async-default.png`, `price-mode-async-hover.png`, `price-mode-async-focus-visible.png`, `price-mode-async-pressed.png`, `price-mode-async-opened.png`.

#### price-mode-rt

Pricing mode: Real-time. The "Real-time" half of the pricing-mode segmented toggle; a local UI toggle — the opened state was measured after its own toggle, then the async side was restored.

Page: pricing. Selector: `button[data-pricing-mode=realtime]`. States: default, hover, focus-visible, pressed, opened.
Read: 2026-11-16.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 114 x 35.59 | = | = | = | = |
| Padding | 8px 24px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #1a9eff offset 2px | = | = |
| Font | Suisse Intl 14px/19.6px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #a3a3a3 | #ffffff | = | #ffffff | #000000 |
| Transition | background-color, color 0.16s, 0.32s cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1) delay 0s, 0s | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Ancestor paint | 1 up div.pricing-toggle.is-ready bg #0c0c0c @ 0.55 | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | button.pricing-toggle__btn 114.0x35.6 r 9999px outline 2px solid #1a9eff offset 2px | = | = |

Crops: `price-mode-rt-default.png`, `price-mode-rt-hover.png`, `price-mode-rt-focus-visible.png`, `price-mode-rt-pressed.png`, `price-mode-rt-opened.png`.

#### plan-card

Plan card. A plan card on /pricing — one column of the pricing grid (.pricing-grid--plans > .pricing-card): name, per-hour price, feature list and its CTA.

Page: pricing. Selector: `.pricing-card`. States: default.
Read: 2026-11-16.

| Property | default |
|---|---|
| Size (w x h) | 428 x 888.13 |
| Padding | 48px 40px 40px 40px |
| Gap | 32px |
| Border | 1px solid #ffffff @ 0.08 |
| Radius | 24px |
| Background | transparent |
| Box shadow | #000000 @ 0.22 0px 8px 28px 0px |
| Backdrop filter | blur(22px) saturate(1.65) |
| Outline | none |
| Font | Suisse Intl 16px/22.4px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | opacity, transform, border-color, box-shadow 1.4s, 1.4s, 0.32s, 0.32s cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1) delay 0.1s |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 16 x 16, colour #a3a3a3 |
| ::before | 426px x 886.125px, absolute, bg #000000 @ 0 linear-gradient(#000000 @ 0.72, #000000 @ 0.6 55%, #000000 @ 0.52), radius 24px |
| Painted layers | div.pricing-card.glass-card 428.0x888.1 border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 24px shadow #000000 @ 0.22 0px 8px 28px 0px; div::before.pricing-card.glass-card 426pxx886.125px image linear-gradient(#000000 @ 0.72, #000000 @ 0.6 55%, #000000 @ 0.52) r 24px; a.btn.btn-primary 346.0x40.0 bg #ffffff r 40px; ul.pricing-card__features 346.0x528.1 border T:1px solid #ffffff @ 0.08 |
| How | at rest |

Crops: none.

#### plan-cta

Plan CTA. A plan card's primary action ("Start with 50€ free credits" or the enterprise contact link); measured, never followed.

Page: pricing. Selector: `.pricing-card CTA`. States: default, hover, focus-visible, pressed.
Read: 2026-11-16.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 346 x 40 | = | - | 352.92 x 40.8 |
| Padding | 8px 20px | = | - | = |
| Border | none | = | - | = |
| Radius | 40px | = | - | = |
| Background | #ffffff | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Suisse Intl 14px/19.6px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Transition | transform 0.16s cubic-bezier(0, 0, 0.2, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | a.btn.btn-primary 346.0x40.0 bg #ffffff r 40px | = | - | a.btn.btn-primary 352.9x40.8 bg #ffffff r 40px |
| Ancestor paint | 3 up div.pricing-card.glass-card shadow #000000 @ 0.22 0px 8px 28px 0px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |
| Transform | - | = | = | matrix(1.02, 0, 0, 1.02, 0, 0) |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-pressed.png`.

#### calc-hours

Calculator hours field. The pricing calculator's hours-per-month number input (default 500); typed into then cleared — a local UI control, nothing submitted.

Page: pricing. Selector: `#calc-hours`. States: default, focused, filled.
Read: 2026-11-16.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 72 x 19.59 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Suisse Intl 14px/19.6px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #ffffff, opacity 1 | = | = |
| Ancestor paint | 1 up span.pricing-calc__number bg #1c1c1e | = | = |
| How | at rest | clicked into the field | typed "500", then deleted; nothing sent |

Crops: `calc-hours-default.png`, `calc-hours-focused.png`, `calc-hours-filled.png`.

#### calc-range

Calculator range. The "Hours of audio per month" range slider in the calculator; measured at rest, never dragged.

Page: pricing. Selector: `pricing-calc range input`. States: default, focused.
Read: 2026-11-16.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 391 x 20 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | 8px |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | 2px solid #925bff offset 4px |
| Font | Arial 13.3333px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #9d968e | = |
| Transition | none | = |
| Cursor | pointer | = |
| Placeholder | #9d968e, opacity 1 | = |
| Ancestor paint | 3 up div.pricing-calc.glass-card shadow #000000 @ 0.22 0px 8px 28px 0px | = |
| How | at rest | keyboard focus (Shift+Tab, Tab), never clicked |
| Painted layers | - | input.pricing-calc__range 391.0x20.0 r 8px outline 2px solid #925bff offset 4px |

Crops: `calc-range-default.png`, `calc-range-focused.png`.

#### calc-feature

Calculator feature checkbox. A feature add-on checkbox in the pricing calculator (summarization, sentiment, translation, NER, PII); a local UI control — measured, never toggled.

Page: pricing. Selector: `calculator checkbox`. States: default, focused.
Read: 2026-11-16.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 13 x 13 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | 1px auto #101010 offset 2px |
| Font | Arial 13.3333px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Opacity | 0 | = |
| Cursor | default | = |
| Placeholder | #000000, opacity 1 | = |
| How | at rest | keyboard focus (Shift+Tab, Tab), never clicked |
| Painted layers | - | input 13.0x13.0 outline 1px auto #101010 offset 2px |

Crops: `calc-feature-default.png`, `calc-feature-focused.png`.

#### faq-acc

FAQ accordion. A question row in the pricing FAQ; the opened state was measured after its own toggle — a local UI toggle.

Page: pricing. Selector: `pricing FAQ row`. States: default, opened.
Read: 2026-11-16.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 720 x 86.39 | = |
| Padding | 32px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 16px/22.4px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 20 x 20, colour #727272 | 20 x 20, colour #a3a3a3 |
| How | at rest | own toggle |

Crops: `faq-acc-default.png`, `faq-acc-opened.png`.

### Demo request form

#### demo-h1

Demo headline. The /demo-request masthead over the sales form.

Page: demo. Selector: `h1`. States: default.
Read: 2026-11-16.

| Property | default |
|---|---|
| Size (w x h) | 860 x 76.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 64px/76.8px 400 |
| Letter spacing | -1.28px |
| Colour | #ffffff |
| Transition | opacity, transform 0.8s, 0.8s cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1) delay 0s, 0s |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `demo-h1-default.png`.

#### demo-email

Email field. The work-e-mail input on the demo-request form; focused and typed into then cleared — never submitted.

Page: demo. Selector: `#demo-email`. States: default, focused, filled.
Read: 2026-11-16.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 462 x 44 | = | = |
| Padding | 0px 16px | = | = |
| Border | 1px solid #ffffff @ 0.08 | 1px solid #947afc | 1px solid #947afc |
| Radius | 8px | = | = |
| Background | #ffffff @ 0.04 | #ffffff @ 0.06 | #ffffff @ 0.06 |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Suisse Intl 14px/19.6px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | border-color, background-color 0.16s, 0.16s cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1) delay 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | #727272, opacity 1 | = | = |
| Painted layers | input.form-input 462.0x44.0 bg #ffffff @ 0.04 border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 8px | input.form-input 462.0x44.0 bg #ffffff @ 0.06 border T:1px solid #947afc / R:1px solid #947afc / B:1px solid #947afc / L:1px solid #947afc r 8px | input.form-input 462.0x44.0 bg #ffffff @ 0.06 border T:1px solid #947afc / R:1px solid #947afc / B:1px solid #947afc / L:1px solid #947afc r 8px |
| Ancestor paint | 3 up div.contact-form-card.hero-ebook-form-card bg #000000 shadow #ffffff @ 0.06 0px 1px 0px 0px inset, #000000 @ 0.28 0px 24px 48px 0px | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `demo-email-default.png`, `demo-email-focused.png`, `demo-email-filled.png`.

#### demo-name

First-name field. The first-name input on the demo-request form; focused and typed into then cleared — never submitted.

Page: demo. Selector: `#demo-first-name`. States: default, focused, filled.
Read: 2026-11-16.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 223 x 44 | = | = |
| Padding | 0px 16px | = | = |
| Border | 1px solid #ffffff @ 0.08 | 1px solid #947afc | 1px solid #947afc |
| Radius | 8px | = | = |
| Background | #ffffff @ 0.04 | #ffffff @ 0.06 | #ffffff @ 0.06 |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Suisse Intl 14px/19.6px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | border-color, background-color 0.16s, 0.16s cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1) delay 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | #727272, opacity 1 | = | = |
| Painted layers | input.form-input 223.0x44.0 bg #ffffff @ 0.04 border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 8px | input.form-input 223.0x44.0 bg #ffffff @ 0.06 border T:1px solid #947afc / R:1px solid #947afc / B:1px solid #947afc / L:1px solid #947afc r 8px | input.form-input 223.0x44.0 bg #ffffff @ 0.06 border T:1px solid #947afc / R:1px solid #947afc / B:1px solid #947afc / L:1px solid #947afc r 8px |
| How | at rest | clicked into the field | typed "Alex", then deleted; nothing sent |

Crops: `demo-name-default.png`, `demo-name-focused.png`, `demo-name-filled.png`.

#### demo-company-size

Company-size select. The company-size select on the demo-request form; measured at rest, never changed.

Page: demo. Selector: `#demo-company-size`. States: default, focused.
Read: 2026-11-16.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 462 x 44 | = |
| Padding | 0px 40px 0px 16px | = |
| Border | 1px solid #ffffff @ 0.08 | 1px solid #947afc |
| Radius | 8px | = |
| Background | #ffffff @ 0.04 | #ffffff @ 0.06 |
| Background image | url(data:…) | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 14px/19.6px 400 | = |
| Letter spacing | normal | = |
| Colour | #727272 | = |
| Transition | border-color, background-color 0.16s, 0.16s cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1) delay 0s, 0s | = |
| Cursor | pointer | = |
| Painted layers | select.form-input.form-select 462.0x44.0 bg #ffffff @ 0.04 image url(data:…) border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 8px; option 0.0x0.0 bg #1c1c1e; option 0.0x0.0 bg #1c1c1e; option 0.0x0.0 bg #1c1c1e; option 0.0x0.0 bg #1c1c1e; option 0.0x0.0 bg #1c1c1e | select.form-input.form-select 462.0x44.0 bg #ffffff @ 0.06 image url(data:…) border T:1px solid #947afc / R:1px solid #947afc / B:1px solid #947afc / L:1px solid #947afc r 8px; option 0.0x0.0 bg #1c1c1e; option 0.0x0.0 bg #1c1c1e; option 0.0x0.0 bg #1c1c1e; option 0.0x0.0 bg #1c1c1e; option 0.0x0.0 bg #1c1c1e |
| Ancestor paint | 3 up div.contact-form-card.hero-ebook-form-card bg #000000 shadow #ffffff @ 0.06 0px 1px 0px 0px inset, #000000 @ 0.28 0px 24px 48px 0px | = |
| How | at rest | keyboard focus (Shift+Tab, Tab), never clicked |

Crops: `demo-company-size-default.png`, `demo-company-size-focused.png`.

#### demo-terms

Terms checkbox. The required terms-acceptance checkbox on the demo-request form (the input is visually hidden behind its styled label); measured at rest, never toggled.

Page: demo. Selector: `demo terms checkbox label`. States: default, focused.
Read: 2026-11-16.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 462 x 18 | - |
| Padding | 0px | - |
| Gap | 12px | - |
| Border | none | - |
| Radius | 0px | - |
| Background | transparent | - |
| Box shadow | none | - |
| Outline | none | - |
| Font | Suisse Intl 16px/22.4px 400 | - |
| Letter spacing | normal | - |
| Colour | #ffffff | - |
| Text node | span.form-checkbox-label: Suisse Intl 12px/18px 400, #727272 | - |
| Transition | none | - |
| Cursor | pointer | - |
| Painted layers | span.form-checkbox-mark 16.0x16.0 bg #1c1c1e border T:1px solid #252525 / R:1px solid #252525 / B:1px solid #252525 / L:1px solid #252525 | - |
| Ancestor paint | 3 up div.contact-form-card.hero-ebook-form-card bg #000000 shadow #ffffff @ 0.06 0px 1px 0px 0px inset, #000000 @ 0.28 0px 24px 48px 0px | - |
| How | at rest | - |
| Skipped | - | focus failed: keyboard focus did not reach the element |

Crops: `demo-terms-default.png`.

#### demo-submit

Submit button. The demo-request form's submit button; its states were measured but the button was never clicked — the form was never sent.

Page: demo. Selector: `#demo-form-btn`. States: default, hover, focus-visible, pressed.
Read: 2026-11-16.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 462 x 48 | = | = | = |
| Padding | 12px 28px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Suisse Intl 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.btn-text: Suisse Intl 16px/normal 400, #000000 | = | = | = |
| Transition | opacity, transform 1.25s, 1.25s cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1) delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.btn.btn-primary 462.0x48.0 bg #ffffff r 40px | = | button.btn.btn-primary 462.0x48.0 bg #ffffff r 40px outline 1px auto #101010 offset 0px | = |
| Ancestor paint | 2 up div.contact-form-card.hero-ebook-form-card bg #000000 shadow #ffffff @ 0.06 0px 1px 0px 0px inset, #000000 @ 0.28 0px 24px 48px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `demo-submit-default.png`, `demo-submit-hover.png`, `demo-submit-focus-visible.png`, `demo-submit-pressed.png`.

### Blog, library and marketing indexes

#### lib-h1

Library headline. The /library masthead — the one marketing page that carries body.light-mode and paints the light token scope.

Page: library. Selector: `h1`. States: default.
Read: 2026-11-15.

| Property | default |
|---|---|
| Size (w x h) | 357.64 x 57.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 48px/57.6px 400 |
| Letter spacing | -0.96px |
| Colour | #000000 |
| Transition | opacity, transform 0.8s, 0.8s cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1) delay 0s, 0s |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `lib-h1-default.png`.

#### lib-card

Resource card. A content card on the library index; measured, never followed.

Page: library. Selector: `library card link`. States: default, hover.
Read: 2026-11-15.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 0 x 0 | - |
| Padding | 10px 32px | - |
| Gap | 12px | - |
| Border | none | - |
| Radius | 0px | - |
| Background | transparent | - |
| Box shadow | none | - |
| Outline | none | - |
| Font | Suisse Intl 16px/22.4px 400 | - |
| Letter spacing | normal | - |
| Colour | #000000 | - |
| Transition | background 0.16s cubic-bezier(0, 0, 0.2, 1) | - |
| Cursor | pointer | - |
| Ancestor paint | 2 up div.mega-menu-overview-card shadow #ffffff @ 0.14 0px 1px 0px 0px inset | - |
| How | at rest | - |
| Error | - | locator.hover: Element is not visible Call log:   - waiting for locator('a').filter({ has: locator('img') }).first().first().first()     - locator resolved to <a class="mega-menu-item" href="/product/ |

Crops: none.

#### blog-h1

Blog headline. The /blog index masthead on the legacy Webflow stack — its own stylesheets, painted light.

Page: blog. Selector: `h1`. States: default.
Read: 2026-11-15.

| Property | default |
|---|---|
| Size (w x h) | 0 x 0 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisseintl 120px/132px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: none.

#### blog-card

Article card. An article card in the blog index; measured, never followed.

Page: blog. Selector: `blog article card`. States: default, hover.
Read: 2026-11-15.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 0 x 0 | - |
| Padding | 16px 12px | - |
| Gap | 16px | - |
| Border | 1px solid #0d0d0d | - |
| Radius | 12px | - |
| Background | transparent | - |
| Box shadow | none | - |
| Outline | none | - |
| Font | Suisseintl 16px/24px 400 | - |
| Letter spacing | normal | - |
| Colour | #ffffff | - |
| Transition | none | - |
| Cursor | pointer | - |
| Painted layers | a.dropdown_item.w-inline-block 0.0x0.0 border T:1px solid #0d0d0d / R:1px solid #0d0d0d / B:1px solid #0d0d0d / L:1px solid #0d0d0d r 12px; img.dropdown_item-image 0.0x0.0 bg #1a1a1a r 10px shadow #ffffff @ 0.12 0px 0px 0px 1px | - |
| How | at rest | - |
| Error | - | locator.hover: Element is not visible Call log:   - waiting for locator('a').filter({ has: locator('img') }).filter({ hasText: /\S{6,}/ }).first().first().first()     - locator resolved to <a tabindex |

Crops: none.

### Docs site (Mintlify)

#### docs-h1

Docs headline. The docs introduction masthead on the Mintlify stack.

Page: docs-home. Selector: `docs h1`. States: default.
Read: 2026-11-15.

| Property | default |
|---|---|
| Size (w x h) | 309.7 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 36px/40px 600 |
| Letter spacing | -0.9px |
| Colour | #181818 |
| Transition | none |
| How | at rest |

Crops: `docs-h1-default.png`.

#### docs-nav-link

Sidebar link. A sidebar navigation link in the docs tree; measured, never followed.

Page: docs-home. Selector: `docs sidebar link`. States: default, hover.
Read: 2026-11-15.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 240 x 32 | = |
| Padding | 6px 12px 6px 16px | = |
| Gap | normal 12px | = |
| Border | none | = |
| Radius | 12px | = |
| Background | transparent | #515151 @ 0.05 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #3f4040 | #181818 |
| Text node | span.min-w-0.max-w-full: Inter 14px/20px 400, #3f4040 | span.min-w-0.max-w-full: Inter 14px/20px 400, #181818 |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |
| Painted layers | - | a.group.flex 240.0x32.0 bg #515151 @ 0.05 r 12px |

Crops: `docs-nav-link-default.png`, `docs-nav-link-hover.png`.

#### docs-h1b

Doc page headline. "Quickstart" — a docs article headline on the Mintlify stack.

Page: docs. Selector: `docs article h1`. States: default.
Read: 2026-11-16.

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
| Colour | #181818 |
| Transition | none |
| How | at rest |

Crops: `docs-h1b-default.png`.

#### docs-search

Search trigger. The docs' search button — a local UI toggle for the search overlay; measured, never opened.

Page: docs. Selector: `docs search button`. States: default, hover, focus-visible, pressed.
Read: 2026-11-16.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 224 x 36 | = | = | = |
| Padding | 0px 12px 0px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9fa0a0 @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #515151 @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #515151 @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | 1px auto #2e343e offset 0px | = |
| Font | Inter 14px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #717171 | = | = | = |
| Text node | div.truncate.min-w-0: Inter 14px/24px 400, #717171 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #3f4040, fill #000000 | 16 x 16, colour #262627, fill #000000 | = | 16 x 16, colour #262627, fill #000000 |
| Painted layers | button.group/search.flex 224.0x36.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9fa0a0 @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | button.group/search.flex 224.0x36.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #515151 @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | button.group/search.flex 224.0x36.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9fa0a0 @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #2e343e offset 0px | button.group/search.flex 224.0x36.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #515151 @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-search-default.png`, `docs-search-hover.png`, `docs-search-focus-visible.png`, `docs-search-pressed.png`.

#### docs-theme-btn

Theme toggle. The docs' theme-preference control — a local UI toggle that flips the Mintlify page between light and dark; measured at rest, never switched here (the dark surface is captured in the screenshots pass).

Page: docs. Selector: `docs theme button`. States: default, hover, focus-visible, pressed.
Read: 2026-11-16.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 20 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #dfe0e0 @ 0.5 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #2e343e offset 0px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #515151 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #515151, fill #000000 | = | = | = |
| Painted layers | button.switch-option.z-10 20.0x20.0 bg #dfe0e0 @ 0.5 r 9999px | = | button.switch-option.z-10 20.0x20.0 bg #dfe0e0 @ 0.5 r 9999px outline 1px auto #2e343e offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-theme-btn-default.png`, `docs-theme-btn-hover.png`, `docs-theme-btn-focus-visible.png`, `docs-theme-btn-pressed.png`.

#### docs-code

Code block. A code block on the docs article; Mintlify's own syntax-highlight layer paints these. Inline code (`transcribe()` and friends) is a different element and never counts.

Page: docs. Selector: `docs pre`. States: default.
Read: 2026-11-16.

| Property | default |
|---|---|
| Size (w x h) | 592 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | Paper Mono 14px/24px 400 |
| Letter spacing | normal |
| Colour | #1f2328 |
| Text node | span: Paper Mono 14px/24px 400, #953800 |
| Transition | none |
| Painted layers | pre.shiki.shiki-themes 592.0x24.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; code 592.0x24.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.line 200.0x16.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span 24.0x16.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span 64.0x16.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span 112.0x16.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Ancestor paint | 1 up div.font-mono.whitespace-pre shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #0b0b0c; 2 up div.min-w-full!.h-full shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #0b0b0c; 3 up div.size-full.rounded-[inherit] shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #0b0b0c |
| How | at rest |

Crops: `docs-code-default.png`.

#### docs-tab

Code-language tab. A language tab on a docs code sample; a local UI toggle — measured, never switched.

Page: docs. Selector: `docs code tab`. States: default, opened.
Read: 2026-11-16.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 75 x 24 | = |
| Padding | 0px | = |
| Gap | 6px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 12px/24px 500 | = |
| Letter spacing | normal | = |
| Colour | #2e343e | = |
| Text node | div.peer/title.flex: Inter 12px/24px 500, #2e343e | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.absolute.-bottom-1.5 75.0x2.0 bg #2e343e r 9999px | div.peer/title.flex 75.0x24.0 bg #dfe0e0 @ 0.5 r 8px; div.absolute.-bottom-1.5 75.0x2.0 bg #2e343e r 9999px |
| How | at rest | own toggle |

Crops: `docs-tab-default.png`, `docs-tab-opened.png`.

### Login and signup (app shell)

#### login-panel

Login panel. The sign-in card on app.gladia.io/ — the shell's only signed-out landing: fields, SSO and the sign-in action. Measured, never submitted.

Page: login. Selector: `app.gladia.io login card`. States: default.
Read: 2026-11-15.

| Property | default |
|---|---|
| Size (w x h) | 720 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h1.text-display-xs.font-semibold: Inter 24px/32px 600, #ffffff |
| Transition | none |
| Icon | 127 x 32, colour #ffffff, fill #000000 |
| Painted layers | div.relative.py-2 360.0x40.0 bg #15181d r 8px shadow #000000 @ 0 0px 0px 0px 0px, #2e343e 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; div.relative.py-2 360.0x40.0 bg #15181d r 8px shadow #000000 @ 0 0px 0px 0px 0px, #2e343e 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; button.relative.inline-flex 360.0x44.0 bg #6446db r 8px shadow #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.12 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; button.relative.inline-flex 360.0x44.0 bg #15181d r 8px shadow #000000 @ 0 0px 0px 0px 0px, #404854 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Ancestor paint | 1 up div.h-full.lg:flex bg #15181d |
| How | at rest |

Crops: `login-panel-default.png`.

#### login-email

Email field. The e-mail input on the sign-in shell; focused and typed into then cleared — never submitted.

Page: login. Selector: `login email input`. States: default, focused, filled.
Read: 2026-11-15.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 0 x 0 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #ffffff, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: none.

#### login-password

Password field. The password input on the sign-in shell; focused and typed into then cleared — never submitted.

Page: login. Selector: `login password input`. States: default, focused, filled.
Read: 2026-11-15.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 336 x 24 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #f1f2f4 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #6f7c90, opacity 1 | = | = |
| Ancestor paint | 1 up div.relative.py-2 bg #15181d shadow #000000 @ 0 0px 0px 0px 0px, #2e343e 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | 1 up div.relative.py-2 bg #15181d shadow #000000 @ 0 0px 0px 0px 0px, #404854 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | 1 up div.relative.py-2 bg #15181d shadow #000000 @ 0 0px 0px 0px 0px, #404854 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | clicked into the field | typed "password", then deleted; nothing sent |

Crops: `login-password-default.png`, `login-password-focused.png`, `login-password-filled.png`.

#### login-sso

SSO button. A "Continue with" SSO button on the sign-in shell; measured, never pressed.

Page: login. Selector: `login SSO button`. States: default, hover, focus-visible, pressed.
Read: 2026-11-15.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 44 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #15181d | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #404854 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| Outline | none | = | 2px solid #7e65e1 offset 2px | = |
| Font | Inter 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f1f2f4 | = | = | = |
| Text node | span: Inter 16px/24px 600, #f1f2f4 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #f1f2f4, fill #000000 | = | = | = |
| Painted layers | button.relative.inline-flex 360.0x44.0 bg #15181d r 8px shadow #000000 @ 0 0px 0px 0px 0px, #404854 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | button.relative.inline-flex 360.0x44.0 bg #15181d r 8px shadow #000000 @ 0 0px 0px 0px 0px, #404854 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #7e65e1 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-sso-default.png`, `login-sso-hover.png`, `login-sso-focus-visible.png`, `login-sso-pressed.png`.

#### login-submit

Sign-in button. The sign-in action; its states were measured but the button was never clicked — nothing was submitted.

Page: login. Selector: `login submit`. States: default, hover, focus-visible, pressed.
Read: 2026-11-15.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 44 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #6446db | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.12 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| Outline | none | = | 2px solid #7e65e1 offset 2px | = |
| Font | Inter 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.relative.inline-flex 360.0x44.0 bg #6446db r 8px shadow #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.12 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | button.relative.inline-flex 360.0x44.0 bg #6446db r 8px shadow #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.12 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #7e65e1 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-focus-visible.png`, `login-submit-pressed.png`.

#### login-signup-link

Sign-up link. The sign-up link on the login shell; measured, never followed.

Page: login. Selector: `login sign-up link`. States: .
Read: .

Not found on the page at capture time.

#### signup-panel

Signup panel. The sign-up card on app.gladia.io/signup; measured, never submitted.

Page: signup. Selector: `app.gladia.io/signup card`. States: default.
Read: 2026-11-15.

| Property | default |
|---|---|
| Size (w x h) | 720 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h1.text-display-xs.font-semibold: Inter 24px/32px 600, #ffffff |
| Transition | none |
| Icon | 127 x 32, colour #ffffff, fill #000000 |
| Painted layers | div.relative.py-2 360.0x40.0 bg #15181d r 8px shadow #000000 @ 0 0px 0px 0px 0px, #2e343e 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; div.relative.py-2 360.0x40.0 bg #15181d r 8px shadow #000000 @ 0 0px 0px 0px 0px, #2e343e 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; div.relative.py-2 360.0x40.0 bg #15181d r 8px shadow #000000 @ 0 0px 0px 0px 0px, #2e343e 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; div.relative.py-2 360.0x40.0 bg #15181d r 8px shadow #000000 @ 0 0px 0px 0px 0px, #2e343e 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; div.size-[1rem].shrink-0 16.0x16.0 border T:1px solid #2e343e / R:1px solid #2e343e / B:1px solid #2e343e / L:1px solid #2e343e r 4px; div.size-[1rem].shrink-0 16.0x16.0 border T:1px solid #2e343e / R:1px solid #2e343e / B:1px solid #2e343e / L:1px solid #2e343e r 4px |
| Ancestor paint | 1 up div.h-full.lg:flex bg #15181d |
| How | at rest |

Crops: `signup-panel-default.png`.

#### signup-email

Email field (signup). The e-mail input on the sign-up shell; focused and typed into then cleared — never submitted.

Page: signup. Selector: `signup email input`. States: default, focused, filled.
Read: 2026-11-15.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 0 x 0 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #ffffff, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: none.

#### signup-sso

SSO button (signup). A "Continue with" SSO button on /signup; measured, never pressed.

Page: signup. Selector: `signup SSO button`. States: default, hover, focus-visible, pressed.
Read: 2026-11-15.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 44 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #15181d | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #404854 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| Outline | none | = | 2px solid #7e65e1 offset 2px | = |
| Font | Inter 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f1f2f4 | = | = | = |
| Text node | span: Inter 16px/24px 600, #f1f2f4 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #f1f2f4, fill #000000 | = | = | = |
| Painted layers | button.relative.inline-flex 360.0x44.0 bg #15181d r 8px shadow #000000 @ 0 0px 0px 0px 0px, #404854 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | button.relative.inline-flex 360.0x44.0 bg #15181d r 8px shadow #000000 @ 0 0px 0px 0px 0px, #404854 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #7e65e1 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-sso-default.png`, `signup-sso-hover.png`, `signup-sso-focus-visible.png`, `signup-sso-pressed.png`.

#### signup-submit

Sign-up button. The sign-up action; measured, never clicked — nothing was submitted.

Page: signup. Selector: `signup submit`. States: default, hover, focus-visible, pressed.
Read: 2026-11-15.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 44 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #6446db | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.12 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| Outline | none | = | 2px solid #7e65e1 offset 2px | = |
| Font | Inter 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.relative.inline-flex 360.0x44.0 bg #6446db r 8px shadow #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.12 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | button.relative.inline-flex 360.0x44.0 bg #6446db r 8px shadow #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.12 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #7e65e1 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-submit-default.png`, `signup-submit-hover.png`, `signup-submit-focus-visible.png`, `signup-submit-pressed.png`.

### Mobile (390 wide)

#### m-topbar

Mobile top bar. The phone header at 390 wide: the wordmark and the "Open menu" button.

Page: mobile. Selector: `mobile nav.navbar`. States: default.
Read: 2026-11-16.

| Property | default |
|---|---|
| Size (w x h) | 358 x 56 |
| Padding | 0px |
| Border | 1px solid #1f1f1f |
| Radius | 20px |
| Background | #000000 @ 0.65 |
| Box shadow | none |
| Backdrop filter | blur(40px) |
| Outline | none |
| Font | Suisse Intl 16px/22.4px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.btn-text: Suisse Intl 14px/19.6px 400, #000000 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 0 x 0, colour #ffffff |
| Painted layers | nav.navbar 358.0x56.0 bg #000000 @ 0.65 border T:1px solid #1f1f1f / R:1px solid #1f1f1f / B:1px solid #1f1f1f / L:1px solid #1f1f1f r 20px; a.btn.btn-secondary 0.0x0.0 bg #1c1c1e border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 40px; a.btn.btn-primary 77.0x36.0 bg #ffffff r 40px; button.navbar-menu-toggle 36.0x36.0 bg #ffffff @ 0.04 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 999px; span.navbar-menu-toggle-line 18.0x1.5 bg #ffffff r 1px; span.navbar-menu-toggle-line 18.0x1.5 bg #ffffff r 1px |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-menu-btn

Mobile menu button. The "Open menu" button — a local UI toggle; the opened state was measured after activating it.

Page: mobile. Selector: `navbar-menu-toggle`. States: default, hover, focus-visible, pressed, opened.
Read: 2026-11-16.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | 1px solid #ffffff @ 0.1 | 1px solid #ffffff @ 0.18 | 1px solid #ffffff @ 0.18 | 1px solid #ffffff @ 0.18 | 1px solid #ffffff @ 0.18 |
| Radius | 999px | = | = | = | = |
| Background | #ffffff @ 0.04 | #ffffff @ 0.1 | #ffffff @ 0.1 | #ffffff @ 0.1 | #ffffff @ 0.1 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #947afc offset 2px | = | = |
| Font | Suisse Intl 13.3333px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | = | = | = | = |
| Transition | background, border-color 0.16s, 0.16s cubic-bezier(0, 0, 0.2, 1), cubic-bezier(0, 0, 0.2, 1) delay 0s, 0s | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | button.navbar-menu-toggle 36.0x36.0 bg #ffffff @ 0.04 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 999px; span.navbar-menu-toggle-line 18.0x1.5 bg #ffffff r 1px; span.navbar-menu-toggle-line 18.0x1.5 bg #ffffff r 1px | button.navbar-menu-toggle 36.0x36.0 bg #ffffff @ 0.1 border T:1px solid #ffffff @ 0.18 / R:1px solid #ffffff @ 0.18 / B:1px solid #ffffff @ 0.18 / L:1px solid #ffffff @ 0.18 r 999px; span.navbar-menu-toggle-line 18.0x1.5 bg #ffffff r 1px; span.navbar-menu-toggle-line 18.0x1.5 bg #ffffff r 1px | button.navbar-menu-toggle 36.0x36.0 bg #ffffff @ 0.1 border T:1px solid #ffffff @ 0.18 / R:1px solid #ffffff @ 0.18 / B:1px solid #ffffff @ 0.18 / L:1px solid #ffffff @ 0.18 r 999px outline 2px solid #947afc offset 2px; span.navbar-menu-toggle-line 18.0x1.5 bg #ffffff r 1px; span.navbar-menu-toggle-line 18.0x1.5 bg #ffffff r 1px | button.navbar-menu-toggle 36.0x36.0 bg #ffffff @ 0.1 border T:1px solid #ffffff @ 0.18 / R:1px solid #ffffff @ 0.18 / B:1px solid #ffffff @ 0.18 / L:1px solid #ffffff @ 0.18 r 999px; span.navbar-menu-toggle-line 18.0x1.5 bg #ffffff r 1px; span.navbar-menu-toggle-line 18.0x1.5 bg #ffffff r 1px | button.navbar-menu-toggle.is-open 36.0x36.0 bg #ffffff @ 0.1 border T:1px solid #ffffff @ 0.18 / R:1px solid #ffffff @ 0.18 / B:1px solid #ffffff @ 0.18 / L:1px solid #ffffff @ 0.18 r 999px; span.navbar-menu-toggle-line 13.8x13.8 bg #ffffff r 1px; span.navbar-menu-toggle-line 13.8x13.8 bg #ffffff r 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `m-menu-btn-default.png`, `m-menu-btn-hover.png`, `m-menu-btn-focus-visible.png`, `m-menu-btn-pressed.png`, `m-menu-btn-opened.png`.

#### m-drawer

Mobile nav overlay. The navigation sheet opened by the menu button (div#mobileNav.mobile-nav, .is-open while aria-hidden flips to false); its links were never followed.

Page: mobile. Selector: `#mobileNav.mobile-nav`. States: default.
Read: 2026-11-16.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/22.4px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span: Suisse Intl 16px/normal 500, #ffffff, ls -0.16px |
| Transition | none |
| Icon | 16 x 16, colour #ffffff @ 0.8 |
| Painted layers | div.mobile-nav-backdrop 390.0x844.0 bg #000000 @ 0.55; div.mobile-nav-sheet 358.0x744.0 bg #0d0d0d border T:1px solid #1f1f1f / R:1px solid #1f1f1f / B:1px solid #1f1f1f / L:1px solid #1f1f1f r 20px; div.mobile-nav-section.is-open 324.0x640.0 border B:1px solid #ffffff @ 0.06; span.mega-menu-item-icon 32.0x32.0 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.06 / R:1px solid #ffffff @ 0.06 / B:1px solid #ffffff @ 0.06 / L:1px solid #ffffff @ 0.06 r 8px; span.mega-menu-item-icon 32.0x32.0 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.06 / R:1px solid #ffffff @ 0.06 / B:1px solid #ffffff @ 0.06 / L:1px solid #ffffff @ 0.06 r 8px; span.mega-menu-item-icon 32.0x32.0 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.06 / R:1px solid #ffffff @ 0.06 / B:1px solid #ffffff @ 0.06 / L:1px solid #ffffff @ 0.06 r 8px |
| How | at rest |

Crops: `m-drawer-default.png`.

#### m-hero-h1

Mobile hero headline. The masthead at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.
Read: 2026-11-16.

| Property | default |
|---|---|
| Size (w x h) | 342 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 40px/48px 400 |
| Letter spacing | -1.6px |
| Colour | #000000 |
| Text node | span.hero-line.is-in: Suisse Intl 40px/48px 400, #000000, ls -1.6px |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

## Transitions declared in the readable stylesheets

www.gladia.io serves its CSS as linked /assets/*.css and /css/*.css bundles plus large inline <style> blocks (the homepage declares its token layer inline); docs.gladia.io ships a separate Mintlify sheet. This list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- blog: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `0.4s cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `color 0.6s cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `background-color 0.6s cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `color 0.2s`, `color 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `background-color 0.4s cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `box-shadow 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `background-color 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955)`

- demo: `opacity .8s var(--ease-out),transform .8s var(--ease-out)`, `color 0.15s`, `background 0.15s, border-color 0.15s`, `background 0.15s`, `opacity 0.2s cubic-bezier(0, 0, 0.2, 1), transform 0.2s cubic-bezier(0, 0, 0.2, 1), visibility 0.2s`, `transform 0.2s, box-shadow 0.2s`, `opacity 0.15s`, `border-color 0.18s ease-out, background 0.18s ease-out`, `background 0.15s ease-out, border-color 0.15s ease-out`, `color 0.15s ease-out, gap 0.15s ease-out`, `transform 0.18s ease-out`, `color var(--duration-160) var(--ease-out)`

- docs: `top 0.16s cubic-bezier(0.25, 0.75, 0.2, 1)`, `width var(--duration-long) var(--timing),height var(--duration-long) var(--timing),background var(--duration-short) ease,scale var(--duration-short) var(--timing)`, `none`, `border-color 0.3s`, `filter 0.35s, opacity 0.35s`, `opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1)`, `opacity var(--lightbox-pull-snap-duration,var(--lightbox-vt-duration)) var(--lightbox-pull-snap-easing,var(--lightbox-vt-root-easing))`, `opacity var(--lightbox-vt-duration) var(--lightbox-vt-root-easing)`, `opacity 0.2s, visibility linear`, `opacity 0.2s, visibility linear 0.2s`, `opacity 0.2s`, `transform 167ms cubic-bezier(0.33, 0, 0, 1)`

- docs-home: `top 0.16s cubic-bezier(0.25, 0.75, 0.2, 1)`, `width var(--duration-long) var(--timing),height var(--duration-long) var(--timing),background var(--duration-short) ease,scale var(--duration-short) var(--timing)`, `none`, `border-color 0.3s`, `filter 0.35s, opacity 0.35s`, `opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1)`, `opacity var(--lightbox-pull-snap-duration,var(--lightbox-vt-duration)) var(--lightbox-pull-snap-easing,var(--lightbox-vt-root-easing))`, `opacity var(--lightbox-vt-duration) var(--lightbox-vt-root-easing)`, `opacity 0.2s, visibility linear`, `opacity 0.2s, visibility linear 0.2s`, `opacity 0.2s`, `transform 167ms cubic-bezier(0.33, 0, 0, 1)`

- home: `color 0.15s`, `background 0.15s, border-color 0.15s`, `background 0.15s`, `opacity 0.2s cubic-bezier(0, 0, 0.2, 1), transform 0.2s cubic-bezier(0, 0, 0.2, 1), visibility 0.2s`, `transform 0.2s, box-shadow 0.2s`, `opacity 0.15s`, `border-color 0.18s ease-out, background 0.18s ease-out`, `background 0.15s ease-out, border-color 0.15s ease-out`, `color 0.15s ease-out, gap 0.15s ease-out`, `transform 0.18s ease-out`, `color var(--duration-160) var(--ease-out)`, `opacity 0.25s var(--ease-out),transform 0.25s var(--ease-out),visibility 0.25s`

- library: `color var(--duration-160) var(--ease-out),border-color var(--duration-160) var(--ease-out),background var(--duration-160) var(--ease-out)`, `border-color var(--duration-160) var(--ease-out),transform var(--duration-160) var(--ease-out),background var(--duration-160) var(--ease-out)`, `opacity .8s var(--ease-out),transform .8s var(--ease-out)`, `color 0.15s`, `background 0.15s, border-color 0.15s`, `background 0.15s`, `opacity 0.2s cubic-bezier(0, 0, 0.2, 1), transform 0.2s cubic-bezier(0, 0, 0.2, 1), visibility 0.2s`, `transform 0.2s, box-shadow 0.2s`, `opacity 0.15s`, `border-color 0.18s ease-out, background 0.18s ease-out`, `background 0.15s ease-out, border-color 0.15s ease-out`, `color 0.15s ease-out, gap 0.15s ease-out`

- login: `none`, `transform 0.75s linear(0 0%, 0.006 1.1%, 0.023 2.2%, 0.096 4.8%, 0.532 15.4%, 0.72 21%, 0.793 23.85%, 0.853 26.7%, 0.902 29.8667%, 0.941 33.0333%, 0.968 36.2%, 0.987 39.7%, 1 43.7%, 1.007 48.3%, 1.009 55.3%, 1.002 78.2%, 1 100%)`, `opacity 0.3s ease-in`, `max-height 1s ease-in`, `transform 1s linear(0 0%, 0.006 1.15%, 0.022 2.3%, 0.091 5.1%, 0.18 7.6%, 0.508 16.3%, 0.607 19.325%, 0.691 22.35%, 0.762 25.375%, 0.822 28.4%, 0.872 31.75%, 0.912 35.1%, 0.944 38.9%, 0.968 43%, 0.985 47.6%, 0.996 53.1%, 1.001 58.4%, 1.003 65.1%, 1 100%)`

- pricing: `opacity var(--duration-160) var(--ease-out)`, `background-color var(--duration-160) var(--ease-out),color var(--duration-160) var(--ease-out)`, `border-color var(--duration-160) var(--ease-out)`, `transform var(--duration-160) var(--ease-out)`, `color var(--duration-160) var(--ease-out)`, `background-color var(--duration-160) var(--ease-out)`, `transform var(--duration-240) var(--ease-spring)`, `translate var(--duration-320) var(--ease-out),box-shadow var(--duration-320) var(--ease-out)`, `opacity .72s var(--enter-ease),transform .72s var(--enter-ease)`, `opacity .72s cubic-bezier(.22,1,.36,1),transform .72s cubic-bezier(.22,1,.36,1),border-color var(--duration-320) var(--ease-out),box-shadow var(--duration-320) var(--ease-out)`, `opacity 0.72s cubic-bezier(0.22, 1, 0.36, 1), transform 0.72s cubic-bezier(0.22, 1, 0.36, 1)`, `opacity .9s cubic-bezier(.22,1,.36,1) .26s,filter 1s cubic-bezier(.22,1,.36,1) .26s,transform 1.2s cubic-bezier(.22,1,.36,1) .26s,translate var(--duration-320) var(--ease-out),box-shadow var(--duration-320) var(--ease-out)`

- product: `background var(--duration-160) var(--ease-out)`, `height .8s var(--ease-out)`, `width .8s var(--ease-out)`, `transform 0.85s cubic-bezier(0.22, 1, 0.36, 1)`, `opacity .45s var(--ease-out) .28s,transform .45s var(--ease-out) .28s`, `none`, `text-decoration-color var(--duration-160) var(--ease-out)`, `opacity .8s var(--ease-out),transform .8s var(--ease-out)`, `color 0.15s`, `background 0.15s, border-color 0.15s`, `background 0.15s`, `opacity 0.2s cubic-bezier(0, 0, 0.2, 1), transform 0.2s cubic-bezier(0, 0, 0.2, 1), visibility 0.2s`

- signup: `none`, `transform 0.75s linear(0 0%, 0.006 1.1%, 0.023 2.2%, 0.096 4.8%, 0.532 15.4%, 0.72 21%, 0.793 23.85%, 0.853 26.7%, 0.902 29.8667%, 0.941 33.0333%, 0.968 36.2%, 0.987 39.7%, 1 43.7%, 1.007 48.3%, 1.009 55.3%, 1.002 78.2%, 1 100%)`, `opacity 0.3s ease-in`, `max-height 1s ease-in`, `transform 1s linear(0 0%, 0.006 1.15%, 0.022 2.3%, 0.091 5.1%, 0.18 7.6%, 0.508 16.3%, 0.607 19.325%, 0.691 22.35%, 0.762 25.375%, 0.822 28.4%, 0.872 31.75%, 0.912 35.1%, 0.944 38.9%, 0.968 43%, 0.985 47.6%, 0.996 53.1%, 1.001 58.4%, 1.003 65.1%, 1 100%)`

## Reduced motion

- home (`header.site-nav a, header a` under prefers-reduced-motion): transition `1e-05s`, animation `1e-05s ease 0s 1 normal none running none`, html scroll-behavior `auto`
