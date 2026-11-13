# Enode component measurements

Computed styles read from enode.com on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the light `data-mode="light" data-ink="alpha"` marketing pages, the whole-page-dark /platform/overview and /platform/flexibility, the scoped `[data-mode="dark"]` showcase sections inside the light pages, and the separate dark sign-in at platform.enode.com/login — with any consent layer hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Site chrome

#### mkt-header

Site header. The fixed glass top bar: wordmark, Platform/Resources mega-menu buttons, Enterprise/Updates/Company nav pills, Sign in and the "Talk to our team" pill.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 58 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 18px/26.1px 470 |
| Letter spacing | normal |
| Colour | #252322 |
| Text node | button.inline-flex.items-center: Enode Sans 15px/22px 490, #252322 @ 0.827 |
| Transition | none |
| Icon | 81.83 x 16, colour #252322 |
| Painted layers | div.relative.chrome-glass 1440.0x58.0 bg #f0fde8 @ 0.92 shadow #252322 @ 0.06 0px 1px 0px 0px; button::before.inline-flex.items-center 85pxx34px bg oklch(0.858722 0.06 133.217 / 0.6) r 4px; button::before.inline-flex.items-center 100pxx34px bg oklch(0.858722 0.06 133.217 / 0.6) r 4px; a::before.nav-pill.rounded-sm 99pxx34px bg oklch(0.858722 0.06 133.217 / 0.6) r 4px; a::before.nav-pill.rounded-sm 85pxx34px bg oklch(0.858722 0.06 133.217 / 0.6) r 4px; a::before.nav-pill.rounded-sm 91pxx34px bg oklch(0.858722 0.06 133.217 / 0.6) r 4px |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The Enode mark-and-wordmark in the header, linking home.

Page: home. Selector: `header a[aria-label*=Enode]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 81.83 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 2px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 18px/26.1px 470 |
| Letter spacing | normal |
| Colour | #252322 |
| Transition | opacity 0.2s cubic-bezier(0, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 81.83 x 16, colour #252322 |
| Ancestor paint | 2 up div.relative.chrome-glass bg #f0fde8 @ 0.92 shadow #252322 @ 0.06 0px 1px 0px 0px |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-menu-btn

Mega-menu trigger. The "Platform" header button — an aria-haspopup="dialog" trigger for the product mega-menu. The opened state was measured after focusing it and pressing Enter.

Page: home. Selector: `header button[aria-haspopup=dialog] Platform`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 85 x 34 | = | = | = | = |
| Padding | 6px 12px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 4px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Enode Sans 15px/22px 490 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #252322 @ 0.827 | #252322 | = | #252322 | #252322 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | default | = | = | = | = |
| ::before | 85px x 34px, absolute, bg oklch(0.858722 0.06 133.217 / 0.6), radius 4px | = | = | = | = |
| Painted layers | button::before.inline-flex.items-center 85pxx34px bg oklch(0.858722 0.06 133.217 / 0.6) r 4px | = | = | = | = |
| Ancestor paint | 3 up div.relative.chrome-glass bg #f0fde8 @ 0.92 shadow #252322 @ 0.06 0px 1px 0px 0px | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `nav-menu-btn-default.png`, `nav-menu-btn-hover.png`, `nav-menu-btn-focus-visible.png`, `nav-menu-btn-pressed.png`, `nav-menu-btn-opened.png`.

#### nav-link

Nav link. A marketing header nav pill (Enterprise); measured, never followed.

Page: home. Selector: `header a.nav-pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 99 x 34 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #b0f87c offset 2px | = |
| Font | Enode Sans 15px/22px 490 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #252322 @ 0.827 | #252322 @ 0.973 | = | #252322 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 99px x 34px, absolute, bg oklch(0.858722 0.06 133.217 / 0.6), radius 4px | = | = | = |
| Painted layers | a::before.nav-pill.rounded-sm 99pxx34px bg oklch(0.858722 0.06 133.217 / 0.6) r 4px | = | a.nav-pill.rounded-sm 99.0x34.0 r 4px outline 2px solid #b0f87c offset 2px; a::before.nav-pill.rounded-sm 99pxx34px bg oklch(0.858722 0.06 133.217 / 0.6) r 4px | = |
| Ancestor paint | 3 up div.relative.chrome-glass bg #f0fde8 @ 0.92 shadow #252322 @ 0.06 0px 1px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-signin

Sign in link. The "Sign in" nav pill linking to platform.enode.com; measured, never followed.

Page: home. Selector: `header a.nav-pill Sign in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 72 x 34 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #b0f87c offset 2px | = |
| Font | Enode Sans 15px/22px 490 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #252322 @ 0.827 | #252322 | = | #252322 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 72px x 34px, absolute, bg oklch(0.858722 0.06 133.217 / 0.6), radius 4px | = | = | = |
| Painted layers | a::before.nav-pill.rounded-sm 72pxx34px bg oklch(0.858722 0.06 133.217 / 0.6) r 4px | = | a.nav-pill.rounded-sm 72.0x34.0 r 4px outline 2px solid #b0f87c offset 2px; a::before.nav-pill.rounded-sm 72pxx34px bg oklch(0.858722 0.06 133.217 / 0.6) r 4px | = |
| Ancestor paint | 3 up div.relative.chrome-glass bg #f0fde8 @ 0.92 shadow #252322 @ 0.06 0px 1px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-cta

Header CTA. The dark "Talk to our team" pill in the header; links to /contact, measured never followed.

Page: home. Selector: `header Talk to our team`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138.2 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #252322 | #b0f87c | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Enode Sans 18px/26.1px 470 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #151413 | = | = |
| Text node | span.text-button.leading-none: Enode Sans 15px/15px 490, #ffffff, ls 0.075px | span.text-button.leading-none: Enode Sans 15px/15px 490, #151413, ls 0.075px | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.h-8 138.2x32.0 bg #252322 r 3.35544e+07px | a.inline-flex.h-8 138.2x32.0 bg #b0f87c r 3.35544e+07px | = | = |
| Ancestor paint | 3 up div.relative.chrome-glass bg #f0fde8 @ 0.92 shadow #252322 @ 0.06 0px 1px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-panel

Mega-menu panel. The dark glass mega-menu panel opened by its own trigger; its links were never followed.

Page: home. Selector: `mega-menu panel (top-full absolute)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1120 x 290 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 18px/26.1px 470 |
| Letter spacing | normal |
| Colour | #252322 |
| Text node | p.flex.items-center: Enode Sans 15px/22px 520, #ffffff |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 146, 0) |
| Icon | 16 x 16, colour #c5c1bf, fill #000000 |
| Painted layers | div.overflow-hidden.rounded-lg 1120.0x290.0 r 10px shadow oklch(1 0 0 / 0.1) 0px 0px 0px 1px; div::before.overflow-hidden.rounded-lg 1120pxx290px bg oklch(0.231995 0.00257147 67.5681 / 0.72) r 10px; a::before.nav-pill.group 271pxx266px bg #ffffff @ 0.08 r 6px; div.relative.aspect-[3/2] 255.0x170.0 bg #151413 r 4px; div.relative.aspect-[3/2] 255.0x170.0 bg #151413 r 4px; div.relative.aspect-[3/2] 255.0x170.0 bg #151413 r 4px |
| Ancestor paint | 2 up div.relative.chrome-glass bg #f0fde8 @ 0.92 shadow #252322 @ 0.06 0px 1px 0px 0px |
| How | at rest |

Crops: `nav-panel-default.png`.

#### nav-menu-item

Mega-menu item. A link inside the opened mega-menu panel; measured, never followed.

Page: home. Selector: `mega-menu panel a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 271 x 266 | = |
| Padding | 8px | = |
| Gap | 12px | = |
| Border | none | = |
| Radius | 6px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Enode Sans 18px/26.1px 470 | = |
| Letter spacing | normal | = |
| Colour | #252322 | = |
| Text node | p.flex.items-center: Enode Sans 15px/22px 520, #ffffff | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| ::before | 271px x 266px, absolute, bg #ffffff @ 0.08, radius 6px | = |
| Painted layers | a::before.nav-pill.group 271pxx266px bg #ffffff @ 0.08 r 6px; div.relative.aspect-[3/2] 255.0x170.0 bg #151413 r 4px | = |
| How | at rest | mouse hover |

Crops: `nav-menu-item-default.png`, `nav-menu-item-hover.png`.

### Home

#### hero-h1

Hero headline. "Orchestrating energy for the next grid" — the text-masthead display heading.

Page: home. Selector: `h1.text-masthead`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 142.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 68px/71.4px 475 |
| Letter spacing | -1.36px |
| Colour | #252322 |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-cta

Hero CTA. The dark "Talk to our team" pill in the hero; measured never followed.

Page: home. Selector: `hero Talk to our team`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138.2 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #252322 | #b0f87c | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Enode Sans 18px/26.1px 470 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #151413 | = | = |
| Text node | span.text-button.leading-none: Enode Sans 15px/15px 490, #ffffff, ls 0.075px | span.text-button.leading-none: Enode Sans 15px/15px 490, #151413, ls 0.075px | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.h-8 138.2x32.0 bg #252322 r 3.35544e+07px | a.inline-flex.h-8 138.2x32.0 bg #b0f87c r 3.35544e+07px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-cta2

Hero secondary CTA. The outlined "Explore our platform" pill beside it; measured never followed.

Page: home. Selector: `hero Explore our platform`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 169.5 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #151413 @ 0.165 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #151413 @ 0.263 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = | = |
| Font | Enode Sans 18px/26.1px 470 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #252322 | = | = | = |
| Text node | span.text-button.leading-none: Enode Sans 15px/15px 490, #252322, ls 0.075px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.h-8 169.5x32.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #151413 @ 0.165 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.h-8 169.5x32.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #151413 @ 0.263 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta2-default.png`, `hero-cta2-hover.png`, `hero-cta2-focus-visible.png`, `hero-cta2-pressed.png`.

#### stat-card

Stat card. A metric card ("960+ Energy device models supported" / "1.6M+ Connected households" / "4,799+ MW").

Page: home. Selector: `stat card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 396 x 184 |
| Padding | 20px |
| Gap | 20px |
| Border | none |
| Radius | 6px |
| Background | oklch(0.9447 0.003 48.7) |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, oklch(0.9214 0.0032 48.7) 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | Enode Sans 18px/26.1px 470 |
| Letter spacing | normal |
| Colour | #252322 |
| Text node | span.inline-block: Enode Sans 36px/41.4px 470, #252322, ls -0.54px |
| Transition | none |
| Painted layers | div.[&>.cap-trim:first-child]:mt-0.5.[&>*+div>.cap-trim:first-child]:mt-0.5 396.0x184.0 bg oklch(0.9447 0.003 48.7) r 6px shadow #000000 @ 0 0px 0px 0px 0px, oklch(0.9214 0.0032 48.7) 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `stat-card-default.png`.

#### section-h2

Section heading. A marketing section heading (text-h2) further down the home page.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 604 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 30px/36px 510 |
| Letter spacing | -0.3px |
| Colour | #252322 |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

### Footer

#### footer

Footer. The page footer: sitemap columns, legal links, social icons.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 682.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 18px/26.1px 470 |
| Letter spacing | normal |
| Colour | #252322 |
| Text node | span.text-text-primary: Enode Sans 15px/22.5px 490, #252322 |
| Transition | none |
| Icon | 18 x 18, colour #4c4948 |
| Painted layers | span.inline-flex.items-center 20.0x20.0 border T:1px solid #dcd8d6 / R:1px solid #dcd8d6 / B:1px solid #dcd8d6 / L:1px solid #dcd8d6 r 3.35544e+07px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer sitemap link; measured, never followed.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 76 x 21.75 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #b0f87c offset 2px | = |
| Font | Enode Sans 15px/21.75px 450 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #252322 @ 0.827 | #252322 | = | #252322 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.group.inline-flex 76.0x21.8 outline 2px solid #b0f87c offset 2px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Dark showcase sections

#### dark-showcase

Dark showcase panel. A scoped [data-mode="dark"] section inside the light page — the hero media/showcase panel painting the dark semantic layer.

Page: home. Selector: `main [data-mode=dark]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1360 x 765 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #151413 |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 18px/26.1px 470 |
| Letter spacing | normal |
| Colour | #252322 |
| Text node | span.font-[490].tracking-[0.06em]: Enode Sans 15px/21.75px 490, #b0f87d, ls 0.9px |
| Transition | none |
| Icon | 32 x 32, colour #efedeb, fill #000000 |
| Painted layers | div.relative.aspect-square 1360.0x765.0 bg #151413; span.h-px.shrink-0 72.0x1.0 bg #a19d9b; span.inline-block.size-2 8.0x8.0 bg #b0f87c r 50%; span.h-px.shrink-0 72.0x1.0 bg #a19d9b; span.inline-block.size-2 8.0x8.0 bg #b0f87c r 50%; span.h-px.shrink-0 72.0x1.0 bg #a19d9b |
| How | at rest |

Crops: `dark-showcase-default.png`.

#### demo-card

Product demo card. A product-UI demo tile inside the dark showcase (the live energy diagram/charging numbers); a public demo, not the signed-in product.

Page: home. Selector: `main [data-mode=dark] demo tile`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1360 x 765 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 18px/26.1px 470 |
| Letter spacing | normal |
| Colour | #252322 |
| Text node | span.font-[490].tracking-[0.06em]: Enode Sans 15px/21.75px 490, #b0f87d, ls 0.9px |
| Transition | none |
| Painted layers | span.h-px.shrink-0 72.0x1.0 bg #a19d9b; span.inline-block.size-2 8.0x8.0 bg #b0f87c r 50%; span.h-px.shrink-0 72.0x1.0 bg #a19d9b; span.inline-block.size-2 8.0x8.0 bg #b0f87c r 50%; span.h-px.shrink-0 72.0x1.0 bg #a19d9b; span.inline-block.size-2 8.0x8.0 bg #b0f87c r 50% |
| Ancestor paint | 1 up div.relative.aspect-square bg #151413 |
| How | at rest |

Crops: `demo-card-default.png`.

### Platform pages

#### ov-h1

Page headline. "Connect. Coordinate. Shape." — the platform overview masthead.

Page: overview. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 71.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 68px/71.4px 475 |
| Letter spacing | -1.36px |
| Colour | #efedeb |
| Transition | none |
| How | at rest |

Crops: `ov-h1-default.png`.

#### ov-lede

Platform card copy. The 15px muted feature-card description ("One API for 1,000+ device models…").

Page: overview. Selector: `platform card copy`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 288 x 90 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 15px/22.5px 470 |
| Letter spacing | normal |
| Colour | #b0adab |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| How | at rest |

Crops: `ov-lede-default.png`.

#### section-h2-ov

Section heading (platform). A platform page section heading.

Page: overview. Selector: `platform h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 576 x 42.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 36px/42.48px 500 |
| Letter spacing | -0.54px |
| Colour | #efedeb |
| Transition | none |
| How | at rest |

Crops: `section-h2-ov-default.png`.

#### feature-row

Platform section nav item. One item in the sticky product-area nav (Asset connectivity / Home energy coordination / Residential flexibility / Intelligence layer).

Page: overview. Selector: `platform nav li`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 188 x 26.09 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 18px/26.1px 470 |
| Letter spacing | normal |
| Colour | #efedeb |
| Text node | a.group.inline-flex: Enode Sans 15px/21.75px 450, #b0adab |
| Transition | none |
| How | at rest |

Crops: `feature-row-default.png`.

#### visual-frame

Visual frame (product mock). A .visual-frame demo tile holding a platform product mock (the browser-framed "platform.enode.com — Client / Users / Assets" screenshot).

Page: overview. Selector: `main .visual-frame`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 304 x 171 |
| Padding | 0px |
| Border | none |
| Radius | 4px |
| Background | #32302f |
| Box shadow | oklch(1 0 0 / 0.042) 0px 0px 0px 1px inset |
| Outline | none |
| Font | Enode Sans 18px/26.1px 470 |
| Letter spacing | normal |
| Colour | #efedeb |
| Text node | span.truncate.px-2: Enode Sans 13px/19.5px 470, #b0adab |
| Transition | background-color 0.2s ease |
| Icon | 5.12 x 5.12, colour #7e7977 |
| Painted layers | div.visual-frame.relative 304.0x171.0 bg #32302f r 4px shadow oklch(1 0 0 / 0.042) 0px 0px 0px 1px inset; div.relative.isolate 304.0x190.0 bg #151413 r 12px; div.relative.z-10 304.0x17.1 bg #151413 r 12px 12px 0px 0px shadow #252322 0px 1px 0px 0px; span.rounded-full.size-3 5.1x5.1 bg #ffffff @ 0.06 r 3.35544e+07px shadow #000000 @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.15 0px 0px 2px 0px, #ffffff @ 0.06 0px 0px 1px 1px inset; span.rounded-full.size-3 5.1x5.1 bg #ffffff @ 0.06 r 3.35544e+07px shadow #000000 @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.15 0px 0px 2px 0px, #ffffff @ 0.06 0px 0px 1px 1px inset; span.rounded-full.size-3 5.1x5.1 bg #ffffff @ 0.06 r 3.35544e+07px shadow #000000 @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.15 0px 0px 2px 0px, #ffffff @ 0.06 0px 0px 1px 1px inset |
| How | at rest |

Crops: `visual-frame-default.png`.

#### code-frame

Visual frame (code). A .visual-frame demo tile holding a code/terminal mock ("import …", "kubectl logs").

Page: overview. Selector: `main .visual-frame code tile`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 304 x 171 |
| Padding | 0px |
| Border | none |
| Radius | 4px |
| Background | #32302f |
| Box shadow | oklch(1 0 0 / 0.042) 0px 0px 0px 1px inset |
| Outline | none |
| Font | Enode Sans 18px/26.1px 470 |
| Letter spacing | normal |
| Colour | #efedeb |
| Text node | span.truncate.px-2: Enode Sans 13px/19.5px 470, #b0adab |
| Transition | background-color 0.2s ease |
| Icon | 5.12 x 5.12, colour #7e7977 |
| Painted layers | div.visual-frame.relative 304.0x171.0 bg #32302f r 4px shadow oklch(1 0 0 / 0.042) 0px 0px 0px 1px inset; div.relative.isolate 304.0x190.0 bg #151413 r 12px; div.relative.z-10 304.0x17.1 bg #151413 r 12px 12px 0px 0px shadow #252322 0px 1px 0px 0px; span.rounded-full.size-3 5.1x5.1 bg #ffffff @ 0.06 r 3.35544e+07px shadow #000000 @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.15 0px 0px 2px 0px, #ffffff @ 0.06 0px 0px 1px 1px inset; span.rounded-full.size-3 5.1x5.1 bg #ffffff @ 0.06 r 3.35544e+07px shadow #000000 @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.15 0px 0px 2px 0px, #ffffff @ 0.06 0px 0px 1px 1px inset; span.rounded-full.size-3 5.1x5.1 bg #ffffff @ 0.06 r 3.35544e+07px shadow #000000 @ 0.15 0px 0px 0px 0.5px, #000000 @ 0.15 0px 0px 2px 0px, #ffffff @ 0.06 0px 0px 1px 1px inset |
| How | at rest |

Crops: `code-frame-default.png`.

### Enterprise

#### ent-h1

Enterprise headline. The /enterprise masthead.

Page: enterprise. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 722.73 x 142.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 68px/71.4px 475 |
| Letter spacing | -1.36px |
| Colour | #252322 |
| Transition | none |
| How | at rest |

Crops: `ent-h1-default.png`.

#### ent-cta

Enterprise CTA. The enterprise contact/demo pill; measured never followed.

Page: enterprise. Selector: `enterprise CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138.2 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #252322 | #b0f87c | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Enode Sans 18px/26.1px 470 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #151413 | = | = |
| Text node | span.text-button.leading-none: Enode Sans 15px/15px 490, #ffffff, ls 0.075px | span.text-button.leading-none: Enode Sans 15px/15px 490, #151413, ls 0.075px | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.h-8 138.2x32.0 bg #252322 r 3.35544e+07px | a.inline-flex.h-8 138.2x32.0 bg #b0f87c r 3.35544e+07px | = | = |
| Ancestor paint | 3 up div.relative.chrome-glass bg #f4f2f1 @ 0.92 shadow #252322 @ 0.06 0px 1px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ent-cta-default.png`, `ent-cta-hover.png`, `ent-cta-focus-visible.png`, `ent-cta-pressed.png`.

#### quote-card

Partner quote card. The enterprise partner quote card ("We’re partnering with Easee…").

Page: enterprise. Selector: `enterprise quote card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 356 x 413.89 |
| Padding | 0px |
| Gap | 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 18px/26.1px 470 |
| Letter spacing | normal |
| Colour | #252322 |
| Text node | p.text-pretty.text-body: Enode Sans 18px/26.1px 470, #4c4948 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.flex.aspect-[3/2] 356.0x237.3 bg #151413 r 4px; span.inline-block.bg-current 195.8x48.0 bg #ffffff |
| Ancestor paint | 1 up a.[&>.cap-trim:first-child]:mt-0.5.[&>*+div>.cap-trim:first-child]:mt-0.5 bg oklch(0.9447 0.003 48.7) shadow #000000 @ 0 0px 0px 0px 0px, oklch(0.9214 0.0032 48.7) 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `quote-card-default.png`.

### Updates

#### upd-h1

Updates headline. "Product news, insights, and stories…" — the /updates masthead.

Page: updates. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 214.17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 68px/71.4px 475 |
| Letter spacing | -1.36px |
| Colour | #252322 |
| Transition | none |
| How | at rest |

Crops: `upd-h1-default.png`.

#### upd-card

Article card. An article card on the updates index (image, tag, title, date); measured, never followed.

Page: updates. Selector: `updates article card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 916 x 75.5 | = |
| Padding | 24px 0px | = |
| Gap | 12px normal | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Enode Sans 18px/26.1px 470 | = |
| Letter spacing | normal | = |
| Colour | #252322 | = |
| Text node | h3.text-pretty.text-body-lg: Enode Sans 20px/27.5px 500, #252322 | = |
| Transition | opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 12 x 12, colour #6e6a68 | 12 x 12, colour #4c4948 |
| How | at rest | mouse hover |

Crops: `upd-card-default.png`, `upd-card-hover.png`.

#### upd-link

Follow link. The "Follow Enode on LinkedIn" social pill; measured, never followed.

Page: updates. Selector: `Follow Enode`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 205.81 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #dcd8d6 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #c5c1bf 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = | = |
| Font | Enode Sans 18px/26.1px 470 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #252322 | = | = | = |
| Text node | span.text-button.leading-none: Enode Sans 15px/15px 490, #252322, ls 0.075px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.h-8 205.8x32.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #dcd8d6 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.h-8 205.8x32.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #c5c1bf 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `upd-link-default.png`, `upd-link-hover.png`, `upd-link-focus-visible.png`, `upd-link-pressed.png`.

### Contact form

#### contact-h1

Contact headline. The /contact masthead over the inquiry form.

Page: contact. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 604 x 93 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 36px/41.4px 500 |
| Letter spacing | -0.54px |
| Colour | #252322 |
| Transition | none |
| How | at rest |

Crops: `contact-h1-default.png`.

#### field-firstname

First name field. The First name text input; focused and typed into then cleared — never submitted.

Page: contact. Selector: `input[name=firstName]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 294 x 48.09 | = | = |
| Padding | 10px 16px | = | = |
| Border | 1px solid #dcd8d6 | 1px solid #252322 | 1px solid #252322 |
| Radius | 6px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Enode Sans 18px/26.1px 470 | = | = |
| Letter spacing | normal | = | = |
| Colour | #252322 | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #252322, opacity 1 | = | = |
| Painted layers | input.mt-2.block 294.0x48.1 bg #ffffff border T:1px solid #dcd8d6 / R:1px solid #dcd8d6 / B:1px solid #dcd8d6 / L:1px solid #dcd8d6 r 6px | input.mt-2.block 294.0x48.1 bg #ffffff border T:1px solid #252322 / R:1px solid #252322 / B:1px solid #252322 / L:1px solid #252322 r 6px | input.mt-2.block 294.0x48.1 bg #ffffff border T:1px solid #252322 / R:1px solid #252322 / B:1px solid #252322 / L:1px solid #252322 r 6px |
| How | at rest | clicked into the field | typed "Ada", then deleted; nothing sent |

Crops: `field-firstname-default.png`, `field-firstname-focused.png`, `field-firstname-filled.png`.

#### field-email

Email field. The work-email input; focused and typed into then cleared — never submitted.

Page: contact. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 294 x 48.09 | = | = |
| Padding | 10px 16px | = | = |
| Border | 1px solid #dcd8d6 | 1px solid #252322 | 1px solid #252322 |
| Radius | 6px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Enode Sans 18px/26.1px 470 | = | = |
| Letter spacing | normal | = | = |
| Colour | #252322 | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #252322, opacity 1 | = | = |
| Painted layers | input.mt-2.block 294.0x48.1 bg #ffffff border T:1px solid #dcd8d6 / R:1px solid #dcd8d6 / B:1px solid #dcd8d6 / L:1px solid #dcd8d6 r 6px | input.mt-2.block 294.0x48.1 bg #ffffff border T:1px solid #252322 / R:1px solid #252322 / B:1px solid #252322 / L:1px solid #252322 r 6px | input.mt-2.block 294.0x48.1 bg #ffffff border T:1px solid #252322 / R:1px solid #252322 / B:1px solid #252322 / L:1px solid #252322 r 6px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `field-email-default.png`, `field-email-focused.png`, `field-email-filled.png`.

#### field-phone

Phone field. The optional phone input; focused and typed into then cleared — never submitted.

Page: contact. Selector: `input[type=tel]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 294 x 48.09 | = | = |
| Padding | 10px 16px | = | = |
| Border | 1px solid #dcd8d6 | 1px solid #252322 | 1px solid #252322 |
| Radius | 6px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Enode Sans 18px/26.1px 470 | = | = |
| Letter spacing | normal | = | = |
| Colour | #252322 | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #252322, opacity 1 | = | = |
| Painted layers | input.mt-2.block 294.0x48.1 bg #ffffff border T:1px solid #dcd8d6 / R:1px solid #dcd8d6 / B:1px solid #dcd8d6 / L:1px solid #dcd8d6 r 6px | input.mt-2.block 294.0x48.1 bg #ffffff border T:1px solid #252322 / R:1px solid #252322 / B:1px solid #252322 / L:1px solid #252322 r 6px | input.mt-2.block 294.0x48.1 bg #ffffff border T:1px solid #252322 / R:1px solid #252322 / B:1px solid #252322 / L:1px solid #252322 r 6px |
| How | at rest | clicked into the field | typed "+47 000 00 000", then deleted; nothing sent |

Crops: `field-phone-default.png`, `field-phone-focused.png`, `field-phone-filled.png`.

#### radio-inquiry

Inquiry radio. One option of the inquiry-type radio group (sr-only inputs behind styled labels); measured, never toggled.

Page: contact. Selector: `inquiry radio label`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 298 x 41.59 |
| Padding | 10px 16px |
| Gap | 8px |
| Border | 1px solid #dcd8d6 |
| Radius | 3.35544e+07px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 14px/19.6px 450 |
| Letter spacing | -0.07px |
| Colour | #4c4948 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | label.flex.cursor-pointer 298.0x41.6 border T:1px solid #dcd8d6 / R:1px solid #dcd8d6 / B:1px solid #dcd8d6 / L:1px solid #dcd8d6 r 3.35544e+07px |
| How | at rest |

Crops: `radio-inquiry-default.png`.

#### send-btn

Send message button. The form's dark "Send message" pill; its states were measured but the button was never clicked — nothing was submitted.

Page: contact. Selector: `contact Send message`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 129.91 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #252322 | #b0f87c | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Enode Sans 18px/26.1px 470 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #151413 | = | = |
| Text node | span.text-button.leading-none: Enode Sans 15px/15px 490, #ffffff, ls 0.075px | span.text-button.leading-none: Enode Sans 15px/15px 490, #151413, ls 0.075px | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.h-8 129.9x32.0 bg #252322 r 3.35544e+07px | button.inline-flex.h-8 129.9x32.0 bg #b0f87c r 3.35544e+07px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `send-btn-default.png`, `send-btn-hover.png`, `send-btn-focus-visible.png`, `send-btn-pressed.png`.

#### field-inquiry

Message textarea. The inquiry-detail textarea; focused and typed into then cleared — never submitted.

Page: contact. Selector: `textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 604 x 100.28 | = | = |
| Padding | 10px 16px | = | = |
| Border | 1px solid #dcd8d6 | = | = |
| Radius | 6px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Enode Sans 18px/26.1px 470 | = | = |
| Letter spacing | normal | = | = |
| Colour | #252322 | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | default | = | = |
| Placeholder | #252322, opacity 1 | = | = |
| Painted layers | textarea.mt-2.block 604.0x100.3 bg #ffffff border T:1px solid #dcd8d6 / R:1px solid #dcd8d6 / B:1px solid #dcd8d6 / L:1px solid #dcd8d6 r 6px | = | = |
| How | at rest | clicked into the field | typed "A short question about the API.", then deleted; nothing sent |

Crops: `field-inquiry-default.png`, `field-inquiry-focused.png`, `field-inquiry-filled.png`.

### Platform login (dark)

#### login-panel

Login panel. The dark sign-in panel over a dimmed product screenshot: "Sign in to Enode Platform".

Page: login. Selector: `login form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 900 |
| Padding | 64px 72px |
| Border | T: none; R: 1px solid #dcd8d6; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 16px/normal 450 |
| Letter spacing | normal |
| Colour | #252322 |
| Text node | h1.title: Enode Sans 30px/36px 500, #252322, ls -0.6px |
| Transition | none |
| Icon | 81.83 x 16, colour #252322 |
| Painted layers | div.panel 600.0x900.0 border R:1px solid #dcd8d6; input.input 455.0x41.0 bg #ffffff border T:1px solid #dcd8d6 / R:1px solid #dcd8d6 / B:1px solid #dcd8d6 / L:1px solid #dcd8d6 r 6px; button.enode-button 455.0x32.0 bg #252322 r 999px; p::before.divider 210pxx1px bg #dcd8d6; p::after.divider 210pxx1px bg #dcd8d6; a.enode-button 455.0x32.0 r 999px shadow #dcd8d6 0px 0px 0px 1px inset |
| How | at rest |

Crops: `login-panel-default.png`.

#### login-field

Email field (login). The e-mail input on the platform login; focused and typed into then cleared — never submitted.

Page: login. Selector: `input[name=email_address]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 455 x 41 | = | = |
| Padding | 10px 16px | = | = |
| Border | 1px solid #dcd8d6 | 1px solid #252322 | 1px solid #252322 |
| Radius | 6px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Enode Sans 16px/normal 450 | = | = |
| Letter spacing | normal | = | = |
| Colour | #252322 | = | = |
| Transition | border-color 0.15s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #252322, opacity 1 | = | = |
| Painted layers | input.input 455.0x41.0 bg #ffffff border T:1px solid #dcd8d6 / R:1px solid #dcd8d6 / B:1px solid #dcd8d6 / L:1px solid #dcd8d6 r 6px | input.input 455.0x41.0 bg #ffffff border T:1px solid #252322 / R:1px solid #252322 / B:1px solid #252322 / L:1px solid #252322 r 6px | input.input 455.0x41.0 bg #ffffff border T:1px solid #252322 / R:1px solid #252322 / B:1px solid #252322 / L:1px solid #252322 r 6px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-field-default.png`, `login-field-focused.png`, `login-field-filled.png`.

#### login-submit

Log in submit. The login submit button; its states were measured but the button was never clicked — nothing was submitted.

Page: login. Selector: `login Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 455 x 32 | = | = | = |
| Padding | 1px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | #252322 | #b0f87c | = | #b0f87c |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #b0f87c offset 2px | = |
| Font | Enode Sans 15px/15px 490 | = | = | = |
| Letter spacing | 0.075px | = | = | = |
| Colour | #ffffff | #151413 | = | #151413 |
| Text node | span.enode-button-label: Enode Sans 15px/15px 490, #ffffff, ls 0.075px | span.enode-button-label: Enode Sans 15px/15px 490, #151413, ls 0.075px | = | span.enode-button-label: Enode Sans 15px/15px 490, #151413, ls 0.075px |
| Transition | background-color, color, box-shadow 0.15s, 0.15s, 0.15s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.enode-button 455.0x32.0 bg #252322 r 999px | button.enode-button 455.0x32.0 bg #b0f87c r 999px | button.enode-button 455.0x32.0 bg #252322 r 999px outline 2px solid #b0f87c offset 2px | button.enode-button 455.0x32.0 bg #b0f87c r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | = | = | 0.9 |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-focus-visible.png`, `login-submit-pressed.png`.

#### login-sso

SAML SSO link. The "Continue with SAML SSO" action; measured, never followed.

Page: login. Selector: `login SAML SSO`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 455 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #dcd8d6 0px 0px 0px 1px inset | #c5c1bf 0px 0px 0px 1px inset | = | #c5c1bf 0px 0px 0px 1px inset |
| Outline | none | = | 2px solid #b0f87c offset 2px | = |
| Font | Enode Sans 15px/15px 490 | = | = | = |
| Letter spacing | 0.075px | = | = | = |
| Colour | #252322 | = | = | = |
| Text node | span.enode-button-label: Enode Sans 15px/15px 490, #252322, ls 0.075px | = | = | = |
| Transition | background-color, color, box-shadow 0.15s, 0.15s, 0.15s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #252322, fill #000000 | = | = | = |
| Painted layers | a.enode-button 455.0x32.0 r 999px shadow #dcd8d6 0px 0px 0px 1px inset | a.enode-button 455.0x32.0 r 999px shadow #c5c1bf 0px 0px 0px 1px inset | a.enode-button 455.0x32.0 r 999px shadow #dcd8d6 0px 0px 0px 1px inset outline 2px solid #b0f87c offset 2px | a.enode-button 455.0x32.0 r 999px shadow #c5c1bf 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | = | = | 0.9 |

Crops: `login-sso-default.png`, `login-sso-hover.png`, `login-sso-focus-visible.png`, `login-sso-pressed.png`.

### Mobile (390 wide)

#### m-topbar

Mobile top bar. The phone header: Enode mark, the round menu button and the "Talk to our team" pill.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 18px/26.1px 470 |
| Letter spacing | normal |
| Colour | #252322 |
| Text node | span.text-button.leading-none: Enode Sans 15px/15px 490, #ffffff, ls 0.075px |
| Transition | none |
| Icon | 81.83 x 16, colour #252322 |
| Painted layers | div.relative.chrome-glass 390.0x60.0 bg #f0fde8 @ 0.92 shadow #252322 @ 0.06 0px 1px 0px 0px; button::before.inline-flex.items-center autoxauto bg oklch(0.858722 0.06 133.217 / 0.6) r 4px; button::before.inline-flex.items-center autoxauto bg oklch(0.858722 0.06 133.217 / 0.6) r 4px; a::before.nav-pill.rounded-sm autoxauto bg oklch(0.858722 0.06 133.217 / 0.6) r 4px; a::before.nav-pill.rounded-sm autoxauto bg oklch(0.858722 0.06 133.217 / 0.6) r 4px; a::before.nav-pill.rounded-sm autoxauto bg oklch(0.858722 0.06 133.217 / 0.6) r 4px |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-cta

Mobile header CTA. The header "Talk to our team" pill at 390 wide; measured never followed.

Page: mobile. Selector: `mobile Talk to our team`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138.2 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #252322 | #b0f87c | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Enode Sans 18px/26.1px 470 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #151413 | = | = |
| Text node | span.text-button.leading-none: Enode Sans 15px/15px 490, #ffffff, ls 0.075px | span.text-button.leading-none: Enode Sans 15px/15px 490, #151413, ls 0.075px | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.h-8 138.2x32.0 bg #252322 r 3.35544e+07px | a.inline-flex.h-8 138.2x32.0 bg #b0f87c r 3.35544e+07px | = | = |
| Ancestor paint | 3 up div.relative.chrome-glass bg #f0fde8 @ 0.92 shadow #252322 @ 0.06 0px 1px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-cta-default.png`, `m-cta-hover.png`, `m-cta-focus-visible.png`, `m-cta-pressed.png`.

#### m-menu-btn

Mobile menu button. The icon-only round button that opens the phone nav overlay — a local UI toggle; the opened state was measured after clicking it.

Page: mobile. Selector: `mobile header menu button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 3.35544e+07px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Enode Sans 18px/26.1px 470 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #252322 | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | default | = | = | = | = |
| Icon | 20 x 20, colour #252322, fill #000000 | = | = | = | = |
| Ancestor paint | 3 up div.relative.chrome-glass bg #f0fde8 @ 0.92 shadow #252322 @ 0.06 0px 1px 0px 0px | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

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
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 18px/26.1px 470 |
| Letter spacing | normal |
| Colour | #252322 |
| Text node | span.text-button.leading-none: Enode Sans 15px/15px 490, #ffffff, ls 0.075px |
| Transition | none |
| Icon | 81.83 x 16, colour #252322 |
| Painted layers | div.shrink-0.border-b 390.0x61.0 border B:1px solid #151413 @ 0.165; a.inline-flex.h-8 138.2x32.0 bg #252322 r 3.35544e+07px; span.inline-flex.items-center 21.6x20.0 border T:1px solid #151413 @ 0.165 / R:1px solid #151413 @ 0.165 / B:1px solid #151413 @ 0.165 / L:1px solid #151413 @ 0.165 r 3.35544e+07px |
| Ancestor paint | 1 up div.fixed.inset-0 bg #f0fde8 |
| How | at rest |

Crops: `m-drawer-default.png`.

#### m-hero-h1

Mobile hero headline. The masthead at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 72.63 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Enode Sans 34.586px/36.3153px 475 |
| Letter spacing | -0.69172px |
| Colour | #252322 |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-hero-cta

Mobile hero CTA. The hero "Talk to our team" pill at 390 wide; measured never followed.

Page: mobile. Selector: `mobile hero CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138.2 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #252322 | #b0f87c | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Enode Sans 18px/26.1px 470 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #151413 | = | = |
| Text node | span.text-button.leading-none: Enode Sans 15px/15px 490, #ffffff, ls 0.075px | span.text-button.leading-none: Enode Sans 15px/15px 490, #151413, ls 0.075px | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.h-8 138.2x32.0 bg #252322 r 3.35544e+07px | a.inline-flex.h-8 138.2x32.0 bg #b0f87c r 3.35544e+07px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-hero-cta-default.png`, `m-hero-cta-hover.png`, `m-hero-cta-focus-visible.png`, `m-hero-cta-pressed.png`.

## Transitions declared in the readable stylesheets

enode.com serves its CSS same-origin as one inline `app-css` bundle plus any lazy chunks, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- contact: `text-decoration-color 0.15s ease-out`, `none`, `background-color 0.2s`, `opacity .3s var(--ease-in-out)`, `background-color 0.15s`, `background-color var(--theme-fade-duration,.4s) var(--theme-fade-ease,ease)`, `opacity .3s ease,backdrop-filter var(--theme-fade-duration,.4s) var(--theme-fade-ease,ease)`, `opacity 0.15s`, `transform 0.75s linear(0 0%, 0.006 1.1%, 0.023 2.2%, 0.096 4.8%, 0.532 15.4%, 0.72 21%, 0.793 23.85%, 0.853 26.7%, 0.902 29.8667%, 0.941 33.0333%, 0.968 36.2%, 0.987 39.7%, 1 43.7%, 1.007 48.3%, 1.009 55.3%, 1.002 78.2%, 1 100%)`, `opacity 0.3s ease-in`, `max-height 1s ease-in`, `transform 1s linear(0 0%, 0.006 1.15%, 0.022 2.3%, 0.091 5.1%, 0.18 7.6%, 0.508 16.3%, 0.607 19.325%, 0.691 22.35%, 0.762 25.375%, 0.822 28.4%, 0.872 31.75%, 0.912 35.1%, 0.944 38.9%, 0.968 43%, 0.985 47.6%, 0.996 53.1%, 1.001 58.4%, 1.003 65.1%, 1 100%)`

- enterprise: `text-decoration-color 0.15s ease-out`, `none`, `background-color 0.2s`, `opacity .3s var(--ease-in-out)`, `background-color 0.15s`, `background-color var(--theme-fade-duration,.4s) var(--theme-fade-ease,ease)`, `opacity .3s ease,backdrop-filter var(--theme-fade-duration,.4s) var(--theme-fade-ease,ease)`, `opacity 0.15s`, `opacity 0.2s, background-color 0.15s, outline-color 0.15s, color 0.15s`, `opacity 0.2s`, `color 0.3s`, `transform 0.75s linear(0 0%, 0.006 1.1%, 0.023 2.2%, 0.096 4.8%, 0.532 15.4%, 0.72 21%, 0.793 23.85%, 0.853 26.7%, 0.902 29.8667%, 0.941 33.0333%, 0.968 36.2%, 0.987 39.7%, 1 43.7%, 1.007 48.3%, 1.009 55.3%, 1.002 78.2%, 1 100%)`

- home: `text-decoration-color 0.15s ease-out`, `none`, `background-color 0.2s`, `opacity .3s var(--ease-in-out)`, `background-color 0.15s`, `background-color var(--theme-fade-duration,.4s) var(--theme-fade-ease,ease)`, `opacity .3s ease,backdrop-filter var(--theme-fade-duration,.4s) var(--theme-fade-ease,ease)`, `opacity 0.15s`, `transform 0.75s linear(0 0%, 0.006 1.1%, 0.023 2.2%, 0.096 4.8%, 0.532 15.4%, 0.72 21%, 0.793 23.85%, 0.853 26.7%, 0.902 29.8667%, 0.941 33.0333%, 0.968 36.2%, 0.987 39.7%, 1 43.7%, 1.007 48.3%, 1.009 55.3%, 1.002 78.2%, 1 100%)`, `opacity 0.3s ease-in`, `max-height 1s ease-in`, `transform 1s linear(0 0%, 0.006 1.15%, 0.022 2.3%, 0.091 5.1%, 0.18 7.6%, 0.508 16.3%, 0.607 19.325%, 0.691 22.35%, 0.762 25.375%, 0.822 28.4%, 0.872 31.75%, 0.912 35.1%, 0.944 38.9%, 0.968 43%, 0.985 47.6%, 0.996 53.1%, 1.001 58.4%, 1.003 65.1%, 1 100%)`

- login: `background-color 0.2s`, `opacity .3s var(--ease-in-out)`, `background-color 0.15s`, `background-color var(--theme-fade-duration,.4s) var(--theme-fade-ease,ease)`, `opacity .3s ease,backdrop-filter var(--theme-fade-duration,.4s) var(--theme-fade-ease,ease)`, `opacity 0.15s`, `transform 0.15s`, `opacity var(--bfen18e)`, `stroke-dashoffset 0.25s ease-in-out`, `transform var(--bfen18e)`, `text-decoration-color 0.15s`, `background-color 0.15s, color 0.15s, box-shadow 0.15s`

- overview: `text-decoration-color 0.15s ease-out`, `none`, `background-color 0.2s`, `opacity .3s var(--ease-in-out)`, `background-color 0.15s`, `background-color var(--theme-fade-duration,.4s) var(--theme-fade-ease,ease)`, `opacity .3s ease,backdrop-filter var(--theme-fade-duration,.4s) var(--theme-fade-ease,ease)`, `opacity 0.15s`, `transform 0.75s linear(0 0%, 0.006 1.1%, 0.023 2.2%, 0.096 4.8%, 0.532 15.4%, 0.72 21%, 0.793 23.85%, 0.853 26.7%, 0.902 29.8667%, 0.941 33.0333%, 0.968 36.2%, 0.987 39.7%, 1 43.7%, 1.007 48.3%, 1.009 55.3%, 1.002 78.2%, 1 100%)`, `opacity 0.3s ease-in`, `max-height 1s ease-in`, `transform 1s linear(0 0%, 0.006 1.15%, 0.022 2.3%, 0.091 5.1%, 0.18 7.6%, 0.508 16.3%, 0.607 19.325%, 0.691 22.35%, 0.762 25.375%, 0.822 28.4%, 0.872 31.75%, 0.912 35.1%, 0.944 38.9%, 0.968 43%, 0.985 47.6%, 0.996 53.1%, 1.001 58.4%, 1.003 65.1%, 1 100%)`

- updates: `text-decoration-color 0.15s ease-out`, `none`, `background-color 0.2s`, `opacity .3s var(--ease-in-out)`, `background-color 0.15s`, `background-color var(--theme-fade-duration,.4s) var(--theme-fade-ease,ease)`, `opacity .3s ease,backdrop-filter var(--theme-fade-duration,.4s) var(--theme-fade-ease,ease)`, `opacity 0.15s`, `transform 0.75s linear(0 0%, 0.006 1.1%, 0.023 2.2%, 0.096 4.8%, 0.532 15.4%, 0.72 21%, 0.793 23.85%, 0.853 26.7%, 0.902 29.8667%, 0.941 33.0333%, 0.968 36.2%, 0.987 39.7%, 1 43.7%, 1.007 48.3%, 1.009 55.3%, 1.002 78.2%, 1 100%)`, `opacity 0.3s ease-in`, `max-height 1s ease-in`, `transform 1s linear(0 0%, 0.006 1.15%, 0.022 2.3%, 0.091 5.1%, 0.18 7.6%, 0.508 16.3%, 0.607 19.325%, 0.691 22.35%, 0.762 25.375%, 0.822 28.4%, 0.872 31.75%, 0.912 35.1%, 0.944 38.9%, 0.968 43%, 0.985 47.6%, 0.996 53.1%, 1.001 58.4%, 1.003 65.1%, 1 100%)`

## Reduced motion

- home (`header a[class*="rounded-full"]` under prefers-reduced-motion): transition `color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1)`, animation `none 0s ease 0s 1 normal none running`, html scroll-behavior `auto`
