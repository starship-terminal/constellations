# Epidemic Sound component measurements

Computed styles read from epidemicsound.com on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the ecru alternative-light marketing pages (/, /pricing/), the dark catalog pages (/music/genres/*, /sound-effects/categories/*) and the dark login.epidemicsound.com Keycloak forms — with the high-z cookie consent card hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### App shell and navigation

#### header

Site header. The sticky top bar: ES logotype, mega-menu triggers (Music / Sound effects / Tools / License / Resources / For business), Pricing, Log in and Create free account.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 100 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.es-text-button-s._text_1qq63_1: Inter 14px/24px 600, #000000 |
| Transition | none |
| Icon | 20 x 24, colour #0000ee |
| Painted layers | div.relative.mx-auto 1359.0x68.0 bg #ffffff r 10000px; button.no-default-focus.focus-visible 76.0x44.0 bg #3d4d74 @ 0 r 10000px; div.flex.w-full 0.0x0.0 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.16 0px 4px 24px 0px; span.flex.size-10 0.0x0.0 bg #3d4d74 @ 0.12 r 4px; span.flex.size-10 0.0x0.0 bg #3d4d74 @ 0.12 r 4px; span.flex.size-10 0.0x0.0 bg #3d4d74 @ 0.12 r 4px |
| Ancestor paint | 1 up body.alternative-light-theme-override.radii-override bg #f1f0eb |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Epidemic Sound glyph + wordmark link.

Page: home. Selector: `a[aria-label=Home]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 40 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 4px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Transition | none |
| Cursor | pointer |
| Icon | 20 x 24, colour #0000ee |
| Ancestor paint | 1 up div.relative.mx-auto bg #ffffff |
| How | at rest |

Crops: `logo-default.png`.

#### nav-trigger

Nav menu trigger. The "Music" ghost button that opens the mega menu — a local disclosure; the opened state was measured after clicking it, its links never followed.

Page: home. Selector: `header button Music`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 76 x 44 | = | = | = | = |
| Padding | 4px 16px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 10000px | = | = | = | = |
| Background | #3d4d74 @ 0 | #3d4d74 @ 0.06 | = | #3d4d74 @ 0.12 | #3d4d74 @ 0.06 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #000000 offset 2px | = | = |
| Font | Inter 14px/24px 600 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Text node | span.es-text-button-s._text_1qq63_1: Inter 14px/24px 600, #000000 | = | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 0 x 0, colour #000000 | = | = | = | = |
| Painted layers | button.no-default-focus.focus-visible 76.0x44.0 bg #3d4d74 @ 0 r 10000px | button.no-default-focus.focus-visible 76.0x44.0 bg #3d4d74 @ 0.06 r 10000px | button.no-default-focus.focus-visible 76.0x44.0 bg #3d4d74 @ 0 r 10000px outline 2px solid #000000 offset 2px | button.no-default-focus.focus-visible 76.0x44.0 bg #3d4d74 @ 0.12 r 10000px | button.no-default-focus.focus-visible 76.0x44.0 bg #3d4d74 @ 0.06 r 10000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`, `nav-trigger-opened.png`.

#### nav-menu

Mega menu. The dropdown opened by the "Music" trigger; its links were never followed.

Page: home. Selector: `mega menu (genres-link ancestor)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1359 x 331 |
| Padding | 24px 24px 40px 24px |
| Gap | 24px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.16 0px 4px 24px 0px |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.es-text-overline-s.es-color-text-secondary: Inter 10px/11px 600, #000000 @ 0.6, ls 1px |
| Transition | none |
| Icon | 16 x 16, colour #000000 |
| Painted layers | div.flex.w-full 1359.0x331.0 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.16 0px 4px 24px 0px; span.flex.size-10 40.0x40.0 bg #3d4d74 @ 0.12 r 4px; span.flex.size-10 40.0x40.0 bg #3d4d74 @ 0.12 r 4px; span.flex.size-10 40.0x40.0 bg #3d4d74 @ 0.12 r 4px; span.flex.size-10 40.0x40.0 bg #3d4d74 @ 0.12 r 4px; span.relative.size-10 40.0x40.0 bg #3d4d74 @ 0.06 r 3.35544e+07px |
| How | at rest |

Crops: `nav-menu-default.png`.

#### nav-menu-item

Mega menu item. A genre link inside the opened mega menu; measured, never followed.

Page: home. Selector: `a[href*=/music/genres/]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 356 x 56 | = |
| Padding | 8px | = |
| Gap | 12px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | transparent | #3d4d74 @ 0.06 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.es-text-button-s._text_1qq63_1: Inter 14px/24px 600, #000000 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #000000 | = |
| Painted layers | span.flex.size-10 40.0x40.0 bg #3d4d74 @ 0.12 r 4px | a.-mx-2.flex 356.0x56.0 bg #3d4d74 @ 0.06 r 4px; span.flex.size-10 40.0x40.0 bg #3d4d74 @ 0.12 r 4px |
| How | at rest | mouse hover |

Crops: `nav-menu-item-default.png`, `nav-menu-item-hover.png`.

#### nav-pricing

Pricing link. The header Pricing link; measured, never followed.

Page: home. Selector: `header a Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 109 x 44 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 10000px | = | = | = |
| Background | transparent | = | = | #3d4d74 @ 0.06 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | Inter 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.es-text-button-s._text_1qq63_1: Inter 14px/24px 600, #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.group/pricing.flex 109.0x44.0 r 10000px outline 2px solid #000000 offset 2px | a.group/pricing.flex 109.0x44.0 bg #3d4d74 @ 0.06 r 10000px |

Crops: `nav-pricing-default.png`, `nav-pricing-hover.png`, `nav-pricing-focus-visible.png`, `nav-pricing-pressed.png`.

#### btn-login

Log in button. The secondary "Log in" button; links to login.epidemicsound.com, measured never followed. The header ships a hidden twin of the same link before the painted one, so the visible copy is the last match.

Page: home. Selector: `header Log in (._secondary_)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 76 x 44 | = | = | = |
| Padding | 4px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 10000px | = | = | = |
| Background | #3d4d74 @ 0.12 | #3d4d74 @ 0.18 | = | #3d4d74 @ 0.24 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | Inter 14px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.no-default-focus.focus-visible 76.0x44.0 bg #3d4d74 @ 0.12 r 10000px | a.no-default-focus.focus-visible 76.0x44.0 bg #3d4d74 @ 0.18 r 10000px | a.no-default-focus.focus-visible 76.0x44.0 bg #3d4d74 @ 0.12 r 10000px outline 2px solid #000000 offset 2px | a.no-default-focus.focus-visible 76.0x44.0 bg #3d4d74 @ 0.24 r 10000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `btn-login-default.png`, `btn-login-hover.png`, `btn-login-focus-visible.png`, `btn-login-pressed.png`.

#### btn-signup

Create account button. The primary "Create free account" button — black fill on the light marketing theme; measured never followed.

Page: home. Selector: `header Create free account (._primary_)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 173 x 44 | = | = | = |
| Padding | 4px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 10000px | = | = | = |
| Background | #000000 | #272727 | = | #333333 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | Inter 14px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.no-default-focus.focus-visible 173.0x44.0 bg #000000 r 10000px | a.no-default-focus.focus-visible 173.0x44.0 bg #272727 r 10000px | a.no-default-focus.focus-visible 173.0x44.0 bg #000000 r 10000px outline 2px solid #000000 offset 2px | a.no-default-focus.focus-visible 173.0x44.0 bg #333333 r 10000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `btn-signup-default.png`, `btn-signup-hover.png`, `btn-signup-focus-visible.png`, `btn-signup-pressed.png`.

#### c-header

Header (dark). The sticky header on the dark catalog theme (header.sticky.top-0); primary button reads white here.

Page: genre. Selector: `header.sticky`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 100 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.es-text-button-s._text_1qq63_1: Inter 14px/24px 600, #ffffff |
| Transition | none |
| Icon | 20 x 24, colour #9e9eff |
| Painted layers | div.relative.mx-auto 1359.0x68.0 bg #292c33 r 10000px; button.no-default-focus.focus-visible 76.0x44.0 bg #cfd6e5 @ 0 r 10000px; div.flex.w-full 0.0x0.0 bg #292c33 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.16 0px 4px 24px 0px; span.flex.size-10 0.0x0.0 bg #cfd6e5 @ 0.16 r 4px; span.flex.size-10 0.0x0.0 bg #cfd6e5 @ 0.16 r 4px; span.flex.size-10 0.0x0.0 bg #cfd6e5 @ 0.16 r 4px |
| Ancestor paint | 1 up body.radii-override.dark-theme-override bg #121418 |
| How | at rest |

Crops: none.

#### c-signup

Create account button (dark). The primary button on the dark theme — white fill, black text; measured never followed. Scoped to the sticky header so a lower banner of the same label cannot match.

Page: genre. Selector: `header.sticky Create free account`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 173 x 44 | = | = | = |
| Padding | 4px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 10000px | = | = | = |
| Background | #ffffff | #e7e7e7 | = | #cfcfcf |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #20afff offset 2px | = |
| Font | Inter 14px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.no-default-focus.focus-visible 173.0x44.0 bg #ffffff r 10000px | a.no-default-focus.focus-visible 173.0x44.0 bg #e7e7e7 r 10000px | a.no-default-focus.focus-visible 173.0x44.0 bg #ffffff r 10000px outline 2px solid #20afff offset 2px | a.no-default-focus.focus-visible 173.0x44.0 bg #cfcfcf r 10000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `c-signup-default.png`, `c-signup-hover.png`, `c-signup-focus-visible.png`, `c-signup-pressed.png`.

### Home (alternative-light marketing)

#### hero-h1

Hero headline. The home hero display heading (es-heading class).

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1104 x 160 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sebenta 80px/80px 500 |
| Letter spacing | -2.4px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-cta

Hero CTA. The primary call-to-action inside the hero; measured never followed.

Page: home. Selector: `hero primary CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 213 x 56 | = | = | = |
| Padding | 9.6px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 10000px | = | = | = |
| Background | #000000 | #272727 | = | #333333 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | Inter 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.no-default-focus.focus-visible 213.0x56.0 bg #000000 r 10000px | a.no-default-focus.focus-visible 213.0x56.0 bg #272727 r 10000px | a.no-default-focus.focus-visible 213.0x56.0 bg #000000 r 10000px outline 2px solid #000000 offset 2px | a.no-default-focus.focus-visible 213.0x56.0 bg #333333 r 10000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### section-h2

Section heading. A marketing section heading further down the home page.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 472 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sebenta 32px/40px 500 |
| Letter spacing | -0.96px |
| Colour | #000000 |
| Text node | span.es-heading-m.es-color-text-primary: Sebenta 40px/48px 500, #000000, ls -1.2px |
| Transition | none |
| Ancestor paint | 1 up div._innerContentWrapper_1rr1h_41.es-color-background-brand-pink bg #ff82c2 |
| How | at rest |

Crops: `section-h2-default.png`.

### Pricing (alternative-light)

#### pr-h1

Pricing headline. "Our subscriptions" — the es-heading-xl display heading over the plan columns.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1328 x 68 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sebenta 64px/68px 500 |
| Letter spacing | -1.92px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `pr-h1-default.png`.

#### billing-switch

Billing switch. The Monthly/Yearly billing switch above the plans — a local toggle; the opened state is the toggled position after clicking it, never checked out.

Page: pricing. Selector: `input[role=switch]`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 40 x 24 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 1000px | = | = | = | = |
| Background | #000000 | #272727 | = | #333333 | #3d4d74 @ 0.12 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #000000 offset 2px | = | = |
| Font | Inter 16px/18.4px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Transition | background-color 0.125s ease-in-out | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Placeholder | #000000, opacity 1 | = | = | = | = |
| ::after | 18px x 18px, absolute, bg #ffffff, radius 50% | = | = | = | = |
| Painted layers | input.no-default-focus.focus-visible 40.0x24.0 bg #000000 r 1000px; input::after.no-default-focus.focus-visible 18pxx18px bg #ffffff r 50% | input.no-default-focus.focus-visible 40.0x24.0 bg #272727 r 1000px; input::after.no-default-focus.focus-visible 18pxx18px bg #ffffff r 50% | input.no-default-focus.focus-visible 40.0x24.0 bg #000000 r 1000px outline 2px solid #000000 offset 2px; input::after.no-default-focus.focus-visible 18pxx18px bg #ffffff r 50% | input.no-default-focus.focus-visible 40.0x24.0 bg #333333 r 1000px; input::after.no-default-focus.focus-visible 18pxx18px bg #ffffff r 50% | input.no-default-focus.focus-visible 40.0x24.0 bg #3d4d74 @ 0.12 r 1000px; input::after.no-default-focus.focus-visible 18pxx18px bg #ffffff r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `billing-switch-default.png`, `billing-switch-hover.png`, `billing-switch-focus-visible.png`, `billing-switch-pressed.png`, `billing-switch-opened.png`.

#### plan-name

Plan name. The "Creator" plan heading (es-subheading-l) over a plan column.

Page: pricing. Selector: `plan h2 Creator`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 368 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/24px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.flex.items-center: Inter 20px/24px 500, #000000 |
| Transition | none |
| How | at rest |

Crops: `plan-name-default.png`.

#### plan-price

Plan price line. The price line inside a plan column.

Page: pricing. Selector: `price text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 688 x 384 |
| Padding | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 500 |
| Letter spacing | normal |
| Colour | #000000 @ 0.6 |
| Text node | p.es-text-m._text_1qq63_1: Inter 16px/24px 500, #000000 @ 0.6 |
| Transition | none |
| How | at rest |

Crops: none.

#### plan-cta

Plan CTA. The primary "Get 30 days free" button inside a plan column — starts a trial; measured never followed.

Page: pricing. Selector: `Get 30 days free (._primary_ ._m_)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 368 x 56 | = | = | = |
| Padding | 9.6px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 10000px | = | = | = |
| Background | #000000 | #272727 | = | #333333 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | Inter 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.no-default-focus.focus-visible 368.0x56.0 bg #000000 r 10000px | a.no-default-focus.focus-visible 368.0x56.0 bg #272727 r 10000px | a.no-default-focus.focus-visible 368.0x56.0 bg #000000 r 10000px outline 2px solid #000000 offset 2px | a.no-default-focus.focus-visible 368.0x56.0 bg #333333 r 10000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### compare-h2

Compare plans heading. The "Compare plans" heading over the feature matrix; a hidden copy precedes it in the DOM, so the painted one is the last match.

Page: pricing. Selector: `h2 Compare plans`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 490.8 x 64 |
| Padding | 0px 0px 16px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sebenta 40px/48px 500 |
| Letter spacing | -1.2px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `compare-h2-default.png`.

### Genre page (dark catalog)

#### breadcrumbs

Breadcrumbs. The MUSIC / GENRES / POP breadcrumb row over the genre banner.

Page: genre. Selector: `[class*=_breadcrumb_]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 46 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 12px/16px 500 |
| Letter spacing | 1.2px |
| Colour | #ffffff @ 0.72 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `breadcrumbs-default.png`.

#### genre-banner

Genre banner. The coloured genre header card (#ff82c2 pink for pop) holding the GENRE kicker and the h1; the _genre_ module class is what paints the colour.

Page: genre. Selector: `div[class*=_genre_]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1328 x 204 |
| Padding | 0px |
| Border | none |
| Radius | 16px 16px 0px 0px |
| Background | #ff82c2 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.es-text-overline-s._text_1qq63_1: Inter 12px/16px 500, #000000, ls 1.2px |
| Transition | none |
| Painted layers | div._container_1i8lh_12._genre_1i8lh_205 1328.0x204.0 bg #ff82c2 r 16px 16px 0px 0px |
| How | at rest |

Crops: `genre-banner-default.png`.

#### genre-h1

Genre heading. "Pop music" — es-heading-m, black on the pink banner.

Page: genre. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 204.2 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sebenta 40px/48px 500 |
| Letter spacing | -1.2px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `genre-h1-default.png`.

#### track-list

Track list. The genre page track list (ul.TrackList); rows virtualise as it scrolls.

Page: genre. Selector: `ul[class*=TrackList_trackList]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1328 x 704 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.es-text-button-s.es-color-text-primary: Inter 14px/24px 600, #ffffff |
| Transition | none |
| Icon | 0 x 0, colour #ffffff |
| Painted layers | button.TrackRowPlayButton_albumCover__Pv48J.overflow-hidden 56.0x56.0 bg #6b6b6b r 4px; button.TrackRowPlayButton_albumCover__Pv48J.rounded-(--es-radius-detail) 0.0x0.0 bg #cfd6e5 @ 0.16 r 4px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0 r 10000px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0 r 10000px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0 r 10000px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0 r 10000px |
| How | at rest |

Crops: `track-list-default.png`.

#### track-row

Track row. A 56px track row: album-cover play button, title, artist, duration, BPM, genre/mood tags; hover reveals row actions.

Page: genre. Selector: `li[class*=TrackRow_trackRow]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1328 x 56 | = |
| Padding | 0px 8px 0px 0px | = |
| Gap | 16px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | #cfd6e5 @ 0.08 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | span.es-text-button-s.es-color-text-primary: Inter 14px/24px 600, #ffffff | = |
| Transition | none | = |
| Icon | 0 x 0, colour #ffffff | 24 x 24, colour #ffffff |
| Painted layers | button.TrackRowPlayButton_albumCover__Pv48J.overflow-hidden 56.0x56.0 bg #6b6b6b r 4px; button.TrackRowPlayButton_albumCover__Pv48J.rounded-(--es-radius-detail) 0.0x0.0 bg #cfd6e5 @ 0.16 r 4px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0 r 10000px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0 r 10000px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0 r 10000px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0 r 10000px | li.TrackRow_trackRow__LM5Mk 1328.0x56.0 bg #cfd6e5 @ 0.08 r 8px; button.TrackRowPlayButton_albumCover__Pv48J.overflow-hidden 0.0x0.0 bg #6b6b6b r 4px; button.TrackRowPlayButton_albumCover__Pv48J.rounded-(--es-radius-detail) 56.0x56.0 bg #cfd6e5 @ 0.16 r 4px; span::before.es-text-xs.es-color-text-inverse 1pxx48px bg #ffffff r 10000px shadow #000000 @ 0.32 1px 0px 0px 0px, #000000 @ 0.32 -1px 0px 0px 0px; span::after.es-text-xs.es-color-text-inverse 32pxx16px bg #ffffff; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0 r 10000px |
| How | at rest | mouse hover |

Crops: `track-row-default.png`, `track-row-hover.png`.

#### track-play

Track play button. A row's album-cover play button; measured, never pressed (signed-out playback is gated anyway). On row hover the cover button is swapped out of the layout entirely — its hover-state box is a real 0x0, not a missed selector.

Page: genre. Selector: `button[aria-label=Play]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56 x 56 | 0 x 0 | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #6b6b6b | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter 16px/18.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | button.TrackRowPlayButton_albumCover__Pv48J.overflow-hidden 56.0x56.0 bg #6b6b6b r 4px | button.TrackRowPlayButton_albumCover__Pv48J.overflow-hidden 0.0x0.0 bg #6b6b6b r 4px | button.TrackRowPlayButton_albumCover__Pv48J.overflow-hidden 56.0x56.0 bg #6b6b6b r 4px outline 1px auto #101010 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `track-play-default.png`, `track-play-focus-visible.png`, `track-play-pressed.png`.

#### track-like

Like button. A row's heart icon button; measured, never toggled (needs an account).

Page: genre. Selector: `button[aria-label=Like]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 10000px | = | = | = |
| Background | #cfd6e5 @ 0 | #cfd6e5 @ 0.08 | #cfd6e5 @ 0.08 | #cfd6e5 @ 0.16 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #20afff offset 2px | = |
| Font | Inter 16px/18.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.72 | #ffffff | = | #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff @ 0.72 | 20 x 20, colour #ffffff | = | 20 x 20, colour #ffffff |
| Painted layers | button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0 r 10000px | button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0.08 r 10000px | button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0.08 r 10000px outline 2px solid #20afff offset 2px | button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0.16 r 10000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `track-like-default.png`, `track-like-hover.png`, `track-like-focus-visible.png`, `track-like-pressed.png`.

#### track-similar

Find similar button. A row's Find-similar icon button; measured, never followed.

Page: genre. Selector: `button[aria-label="Find similar"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 10000px | = | = | = |
| Background | #cfd6e5 @ 0 | #cfd6e5 @ 0.08 | #cfd6e5 @ 0.08 | #cfd6e5 @ 0.16 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #20afff offset 2px | = |
| Font | Inter 16px/18.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.72 | #ffffff | = | #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff @ 0.72 | 20 x 20, colour #ffffff | = | 20 x 20, colour #ffffff |
| Painted layers | button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0 r 10000px | button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0.08 r 10000px | button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0.08 r 10000px outline 2px solid #20afff offset 2px | button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0.16 r 10000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `track-similar-default.png`, `track-similar-hover.png`, `track-similar-focus-visible.png`, `track-similar-pressed.png`.

#### track-add

Add to playlist button. A row's Add-to-playlist icon button; measured, never toggled (needs an account).

Page: genre. Selector: `button[aria-label="Add to playlist"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 10000px | = | = | = |
| Background | #cfd6e5 @ 0 | #cfd6e5 @ 0.08 | #cfd6e5 @ 0.08 | #cfd6e5 @ 0.16 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #20afff offset 2px | = |
| Font | Inter 16px/18.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.72 | #ffffff | = | #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff @ 0.72 | 20 x 20, colour #ffffff | = | 20 x 20, colour #ffffff |
| Painted layers | button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0 r 10000px | button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0.08 r 10000px | button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0.08 r 10000px outline 2px solid #20afff offset 2px | button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0.16 r 10000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `track-add-default.png`, `track-add-hover.png`, `track-add-focus-visible.png`, `track-add-pressed.png`.

#### track-download

Download button. A row's Download icon button; measured, never pressed (licensed download).

Page: genre. Selector: `button[aria-label=Download]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 10000px | = | = | = |
| Background | #cfd6e5 @ 0 | #cfd6e5 @ 0.08 | #cfd6e5 @ 0.08 | #cfd6e5 @ 0.16 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #20afff offset 2px | = |
| Font | Inter 16px/18.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.72 | #ffffff | = | #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff @ 0.72 | 20 x 20, colour #ffffff | = | 20 x 20, colour #ffffff |
| Painted layers | button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0 r 10000px | button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0.08 r 10000px | button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0.08 r 10000px outline 2px solid #20afff offset 2px | button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0.16 r 10000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `track-download-default.png`, `track-download-hover.png`, `track-download-focus-visible.png`, `track-download-pressed.png`.

#### faq-row

FAQ accordion row. An FAQ accordion heading at the bottom of the catalog page — a local disclosure; the opened state was measured after clicking it.

Page: genre. Selector: `faq heading`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 289 x 24 | = | - | = | = |
| Padding | 0px | = | - | = | = |
| Border | none | = | - | = | = |
| Radius | 0px | = | - | = | = |
| Background | transparent | = | - | = | = |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | Inter 16px/24px 600 | = | - | = | = |
| Letter spacing | normal | = | - | = | = |
| Colour | #ffffff | = | - | = | = |
| Transition | none | = | - | = | = |
| Cursor | pointer | = | - | = | = |
| Ancestor paint | 1 up summary.no-default-focus.focus-visible bg #cfd6e5 @ 0.08 | 1 up summary.no-default-focus.focus-visible bg #cfd6e5 @ 0.16 | - | = | 1 up summary.no-default-focus.focus-visible bg #cfd6e5 @ 0.16 |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | own toggle |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `faq-row-default.png`, `faq-row-hover.png`, `faq-row-pressed.png`, `faq-row-opened.png`.

### Signup upsell

#### wantmore

Want-more banner. The #ff82c2 pink "Want more music?" upsell card between the list and the FAQ — an accent-coloured island on the dark page.

Page: genre. Selector: `WantMoreBanner container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1328 x 244 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.es-heading-xs.es-color-text-dark-static: Sebenta 40px/48px 500, #000000, ls -1.2px |
| Transition | none |
| Painted layers | div.WantMoreBanner_wrapper__XCHly.dark-theme-override 1328.0x244.0 bg #ff82c2; a.no-default-focus.focus-visible 173.0x44.0 bg #ffffff r 10000px |
| How | at rest |

Crops: `wantmore-default.png`.

#### wantmore-cta

Upsell CTA. The banner's Create-free-account button; measured never followed.

Page: genre. Selector: `WantMoreBanner CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 173 x 44 | = | = | = |
| Padding | 4px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 10000px | = | = | = |
| Background | #ffffff | #e7e7e7 | = | #cfcfcf |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #20afff offset 2px | = |
| Font | Inter 14px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.no-default-focus.focus-visible 173.0x44.0 bg #ffffff r 10000px | a.no-default-focus.focus-visible 173.0x44.0 bg #e7e7e7 r 10000px | a.no-default-focus.focus-visible 173.0x44.0 bg #ffffff r 10000px outline 2px solid #20afff offset 2px | a.no-default-focus.focus-visible 173.0x44.0 bg #cfcfcf r 10000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `wantmore-cta-default.png`, `wantmore-cta-hover.png`, `wantmore-cta-focus-visible.png`, `wantmore-cta-pressed.png`.

### Footer

#### footer

Footer. The catalog page footer: link columns, social icon buttons, locale line.

Page: genre. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 681 |
| Padding | 80px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h3.es-text-overline-s.es-color-text-secondary: Inter 12px/16px 500, #ffffff @ 0.72, ls 1.2px |
| Transition | none |
| Icon | 0 x 0, colour #ffffff |
| Painted layers | div.m-0.border-b-1 0.0x0.0 border B:1px solid #cfd6e5 @ 0.16; summary.no-default-focus.focus-visible 0.0x0.0 bg #121418 r 8px; div.m-0.border-b-1 0.0x0.0 border B:1px solid #cfd6e5 @ 0.16; summary.no-default-focus.focus-visible 0.0x0.0 bg #121418 r 8px; div.m-0.border-b-1 0.0x0.0 border B:1px solid #cfd6e5 @ 0.16; summary.no-default-focus.focus-visible 0.0x0.0 bg #121418 r 8px |
| Ancestor paint | 1 up body.radii-override.dark-theme-override bg #121418 |
| How | at rest |

Crops: `footer-default.png`.

#### social-icon

Social icon button. A footer social icon button (ghost, _m_ size); measured never followed.

Page: genre. Selector: `a[aria-label=Spotify]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56 x 56 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 10000px | = | = | = |
| Background | #cfd6e5 @ 0 | #cfd6e5 @ 0.08 | #cfd6e5 @ 0.08 | #cfd6e5 @ 0.16 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #20afff offset 2px | = |
| Font | Inter 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.72 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff @ 0.72 | = | = | = |
| Painted layers | a.focus-visible._iconButton_wmtv6_1 56.0x56.0 bg #cfd6e5 @ 0 r 10000px | a.focus-visible._iconButton_wmtv6_1 56.0x56.0 bg #cfd6e5 @ 0.08 r 10000px | a.focus-visible._iconButton_wmtv6_1 56.0x56.0 bg #cfd6e5 @ 0.08 r 10000px outline 2px solid #20afff offset 2px | a.focus-visible._iconButton_wmtv6_1 56.0x56.0 bg #cfd6e5 @ 0.16 r 10000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `social-icon-default.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

### Sound-effects category (dark catalog)

#### sfx-h1

SFX category heading. The sound-effects category page heading on the dark theme.

Page: sfx. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 624.61 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sebenta 40px/48px 500 |
| Letter spacing | -1.2px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `sfx-h1-default.png`.

#### sfx-row

SFX track row. An SFX track row (name, category tags, duration).

Page: sfx. Selector: `track row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1328 x 56 | = |
| Padding | 0px 8px 0px 0px | = |
| Gap | 16px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | #cfd6e5 @ 0.08 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | span.es-text-button-s.es-color-text-primary: Inter 14px/24px 600, #ffffff | = |
| Transition | none | = |
| Icon | 0 x 0, colour #ffffff | 24 x 24, colour #ffffff |
| Painted layers | button.TrackRowPlayButton_albumCover__Pv48J.overflow-hidden 56.0x56.0 bg #6b6b6b r 4px; button.TrackRowPlayButton_albumCover__Pv48J.rounded-(--es-radius-detail) 0.0x0.0 bg #cfd6e5 @ 0.16 r 4px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0 r 10000px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0 r 10000px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0 r 10000px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0 r 10000px | li.TrackRow_trackRow__LM5Mk.TrackRow_isSoundEffect__qnHnA 1328.0x56.0 bg #cfd6e5 @ 0.08 r 8px; button.TrackRowPlayButton_albumCover__Pv48J.overflow-hidden 0.0x0.0 bg #6b6b6b r 4px; button.TrackRowPlayButton_albumCover__Pv48J.rounded-(--es-radius-detail) 56.0x56.0 bg #cfd6e5 @ 0.16 r 4px; span::before.es-text-xs.es-color-text-inverse 1pxx48px bg #ffffff r 10000px shadow #000000 @ 0.32 1px 0px 0px 0px, #000000 @ 0.32 -1px 0px 0px 0px; span::after.es-text-xs.es-color-text-inverse 32pxx16px bg #ffffff; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0 r 10000px |
| How | at rest | mouse hover |

Crops: `sfx-row-default.png`, `sfx-row-hover.png`.

#### sfx-play

SFX play button. An SFX row's play button; measured, never pressed. As on the genre list, row hover swaps the cover button out — the hover-state box is a real 0x0.

Page: sfx. Selector: `button[aria-label=Play]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56 x 56 | 0 x 0 | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #6b6b6b | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter 16px/18.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | button.TrackRowPlayButton_albumCover__Pv48J.overflow-hidden 56.0x56.0 bg #6b6b6b r 4px | button.TrackRowPlayButton_albumCover__Pv48J.overflow-hidden 0.0x0.0 bg #6b6b6b r 4px | button.TrackRowPlayButton_albumCover__Pv48J.overflow-hidden 56.0x56.0 bg #6b6b6b r 4px outline 1px auto #101010 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sfx-play-default.png`, `sfx-play-focus-visible.png`, `sfx-play-pressed.png`.

#### sfx-category-card

SFX subcategory link. A subcategory link inside a row's categories column (e.g. "Suburban" under Ambience) — this page has no large category card, the in-row text link is the real subcategory surface; measured, never followed.

Page: sfx. Selector: `a[class*=scrollingText]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 39 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9e9eff | #ffffff @ 0.72 | = | #ffffff @ 0.72 |
| Text node | span.es-text-xs.es-color-text-secondary: Inter 12px/16px 400, #ffffff @ 0.72 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.TrackRow_scrollingText__fQwVK.TrackRow_trackRowScrollableLink__n7oIr 39.0x20.0 outline 1px auto #101010 offset 1px | = |

Crops: `sfx-category-card-default.png`, `sfx-category-card-hover.png`, `sfx-category-card-focus-visible.png`, `sfx-category-card-pressed.png`.

### Login and signup (Keycloak, dark)

#### kc-card

Login card. The dark Keycloak form-card on login.epidemicsound.com: logo, social buttons, email/password form, links.

Page: login. Selector: `.form-card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 416 x 882.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/26.56px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h1: Sebenta 48px/56px 500, #ffffff, ls -0.96px |
| Transition | none |
| Painted layers | a.button.primary 416.0x56.0 bg #ffffff border T:1px solid #747775 / R:1px solid #747775 / B:1px solid #747775 / L:1px solid #747775 r 10000px; a.button.primary 416.0x56.0 bg #ffffff border T:1px solid #747775 / R:1px solid #747775 / B:1px solid #747775 / L:1px solid #747775 r 10000px; div.socialLine 188.5x1.0 bg #cfd6e5 @ 0.16; div.socialLine 188.5x1.0 bg #cfd6e5 @ 0.16; div.form-group 416.0x56.0 bg #cfd6e5 @ 0.16 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; div.form-group 416.0x56.0 bg #cfd6e5 @ 0.16 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest |

Crops: `kc-card-default.png`.

#### kc-h1

Login heading. The "Log in" heading over the form.

Page: login. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 148.25 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sebenta 48px/56px 500 |
| Letter spacing | -0.96px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `kc-h1-default.png`.

#### kc-social-google

Social button. The "Continue with Google" social button; measured, never followed.

Page: login. Selector: `#social-google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 416 x 56 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #747775 | = | = | = |
| Radius | 10000px | = | = | = |
| Background | #ffffff | #e7e7e7 | = | #cfcfcf |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff offset 2px | = |
| Font | Inter 16px/18px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f0f0f | = | = | = |
| Text node | span: Inter 16px/18px 600, #0f0f0f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.primary 416.0x56.0 bg #ffffff border T:1px solid #747775 / R:1px solid #747775 / B:1px solid #747775 / L:1px solid #747775 r 10000px | a.button.primary 416.0x56.0 bg #e7e7e7 border T:1px solid #747775 / R:1px solid #747775 / B:1px solid #747775 / L:1px solid #747775 r 10000px | a.button.primary 416.0x56.0 bg #ffffff border T:1px solid #747775 / R:1px solid #747775 / B:1px solid #747775 / L:1px solid #747775 r 10000px outline 2px solid #ffffff offset 2px | a.button.primary 416.0x56.0 bg #cfcfcf border T:1px solid #747775 / R:1px solid #747775 / B:1px solid #747775 / L:1px solid #747775 r 10000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `kc-social-google-default.png`, `kc-social-google-hover.png`, `kc-social-google-focus-visible.png`, `kc-social-google-pressed.png`.

#### kc-email

Email field. The login email input; focused and typed into then cleared — never submitted.

Page: login. Selector: `input#username`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 414 x 54 | = | 414 x 56 |
| Padding | 15px 16px | = | 25px 16px 7px 16px |
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
| Placeholder | #757575, opacity 1 | = | = |
| Ancestor paint | 1 up div.form-group bg #cfd6e5 @ 0.16 | 1 up div.form-group bg #cfd6e5 @ 0.24 | 1 up div.form-group bg #cfd6e5 @ 0.24 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `kc-email-default.png`, `kc-email-focused.png`, `kc-email-filled.png`.

#### kc-password

Password field. The login password input; focused and typed into then cleared — never submitted.

Page: login. Selector: `input#password`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 414 x 54 | = | 414 x 56 |
| Padding | 15px 52px 15px 16px | = | 25px 52px 7px 16px |
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
| Placeholder | #757575, opacity 1 | = | = |
| Ancestor paint | 1 up div.form-group bg #cfd6e5 @ 0.16 | 1 up div.form-group bg #cfd6e5 @ 0.24 | 1 up div.form-group bg #cfd6e5 @ 0.24 |
| How | at rest | clicked into the field | typed "not-a-real-password", then deleted; nothing sent |

Crops: `kc-password-default.png`, `kc-password-focused.png`, `kc-password-filled.png`.

#### kc-show-pass

Show-password button. The eye icon button inside the password field (a local reveal toggle); measured, never clicked.

Page: login. Selector: `.password-visibility-toggle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 10000px | = | = | = |
| Background | transparent | #ffffff @ 0.08 | = | #ffffff @ 0.16 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter 16px/26.56px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | background-color 0.1s ease | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, -22) | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.form-group bg #cfd6e5 @ 0.16 | 1 up div.form-group bg #cfd6e5 @ 0.24 | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.password-visibility-toggle 44.0x44.0 bg #ffffff @ 0.08 r 10000px | button.password-visibility-toggle 44.0x44.0 r 10000px outline 1px auto #101010 offset 0px | button.password-visibility-toggle 44.0x44.0 bg #ffffff @ 0.16 r 10000px |

Crops: `kc-show-pass-default.png`, `kc-show-pass-hover.png`, `kc-show-pass-focus-visible.png`, `kc-show-pass-pressed.png`.

#### kc-submit

Log in submit. The white primary submit button; its states were measured but it was never clicked — nothing was submitted.

Page: login. Selector: `#kc-login`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 416 x 56 | = | = | = |
| Padding | 1px 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 10000px | = | = | = |
| Background | #ffffff | #e7e7e7 | = | #cfcfcf |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff offset 2px | = |
| Font | Inter 16px/18px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f0f0f | = | = | = |
| Text node | span.button-inner: Inter 16px/18px 600, #0f0f0f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.button.primary 416.0x56.0 bg #ffffff r 10000px | button.button.primary 416.0x56.0 bg #e7e7e7 r 10000px | button.button.primary 416.0x56.0 bg #ffffff r 10000px outline 2px solid #ffffff offset 2px | button.button.primary 416.0x56.0 bg #cfcfcf r 10000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `kc-submit-default.png`, `kc-submit-hover.png`, `kc-submit-focus-visible.png`, `kc-submit-pressed.png`.

#### kc-signup-link

Create-account link. The "Create account" link over the form; measured, never followed.

Page: login. Selector: `Create account`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 112 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 16px/26.56px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 112.0x20.0 outline 1px auto #101010 offset 1px | = |

Crops: `kc-signup-link-default.png`, `kc-signup-link-hover.png`, `kc-signup-link-focus-visible.png`, `kc-signup-link-pressed.png`.

#### kc-forgot

Forgot-password link. The "Forgot password?" link; measured, never followed.

Page: login. Selector: `a Forgot password`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 131 x 26.55 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 16px/26.56px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 131.0x26.5 outline 1px auto #101010 offset 1px | = |

Crops: `kc-forgot-default.png`, `kc-forgot-hover.png`, `kc-forgot-focus-visible.png`, `kc-forgot-pressed.png`.

#### su-card

Signup card. The Keycloak registration card; measured at rest only.

Page: signup. Selector: `.form-card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 416 x 864.88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/26.56px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h1: Sebenta 48px/56px 500, #ffffff, ls -0.96px |
| Transition | none |
| Icon | 16.45 x 12.8, colour #ffffff @ 0.72, fill #ffffff @ 0.6 |
| Painted layers | a.button.primary 416.0x56.0 bg #ffffff border T:1px solid #747775 / R:1px solid #747775 / B:1px solid #747775 / L:1px solid #747775 r 10000px; a.button.primary 416.0x56.0 bg #ffffff border T:1px solid #747775 / R:1px solid #747775 / B:1px solid #747775 / L:1px solid #747775 r 10000px; div.socialLine 188.5x1.0 bg #cfd6e5 @ 0.16; div.socialLine 188.5x1.0 bg #cfd6e5 @ 0.16; div.form-group 416.0x56.0 bg #cfd6e5 @ 0.16 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; div.form-group 416.0x56.0 bg #cfd6e5 @ 0.16 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest |

Crops: `su-card-default.png`.

#### su-field

Signup field. A registration form input; focused and typed into then cleared — never submitted.

Page: signup. Selector: `signup input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 414 x 54 | = | 414 x 56 |
| Padding | 15px 16px | = | 25px 16px 7px 16px |
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
| Placeholder | #757575, opacity 1 | = | = |
| Ancestor paint | 1 up div.form-group bg #cfd6e5 @ 0.16 | 1 up div.form-group bg #cfd6e5 @ 0.24 | 1 up div.form-group bg #cfd6e5 @ 0.24 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `su-field-default.png`, `su-field-focused.png`, `su-field-filled.png`.

#### su-submit

Signup submit. The registration form's submit action; its states were measured but it was never clicked — nothing was submitted.

Page: signup. Selector: `signup submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 416 x 56 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #747775 | = | = | = |
| Radius | 10000px | = | = | = |
| Background | #ffffff | #e7e7e7 | = | #cfcfcf |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff offset 2px | = |
| Font | Inter 16px/18px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f0f0f | = | = | = |
| Text node | span: Inter 16px/18px 600, #0f0f0f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.primary 416.0x56.0 bg #ffffff border T:1px solid #747775 / R:1px solid #747775 / B:1px solid #747775 / L:1px solid #747775 r 10000px | a.button.primary 416.0x56.0 bg #e7e7e7 border T:1px solid #747775 / R:1px solid #747775 / B:1px solid #747775 / L:1px solid #747775 r 10000px | a.button.primary 416.0x56.0 bg #ffffff border T:1px solid #747775 / R:1px solid #747775 / B:1px solid #747775 / L:1px solid #747775 r 10000px outline 2px solid #ffffff offset 2px | a.button.primary 416.0x56.0 bg #cfcfcf border T:1px solid #747775 / R:1px solid #747775 / B:1px solid #747775 / L:1px solid #747775 r 10000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `su-submit-default.png`, `su-submit-hover.png`, `su-submit-focus-visible.png`, `su-submit-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The phone top bar: ES glyph, Create free account, hamburger.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 100 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | a.no-default-focus.focus-visible: Inter 14px/24px 600, #000000 |
| Transition | none |
| Icon | 20 x 24, colour #9e9eff |
| Painted layers | div.relative.mx-auto 358.0x68.0 bg #292c33 r 10000px; ul.my-0.list-none 0.0x0.0 bg #292c33 r 16px; span.flex.size-10 0.0x0.0 bg #cfd6e5 @ 0.16 r 4px; span.flex.size-10 0.0x0.0 bg #cfd6e5 @ 0.16 r 4px; span.flex.size-10 0.0x0.0 bg #cfd6e5 @ 0.16 r 4px; span.flex.size-10 0.0x0.0 bg #cfd6e5 @ 0.16 r 4px |
| Ancestor paint | 1 up body.radii-override.dark-theme-override bg #121418 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-hamburger

Mobile hamburger. The "Show navigation menu" icon button — a local disclosure; the opened state was measured after clicking it.

Page: mobile. Selector: `button[aria-label*=menu]`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 10000px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #20afff offset 2px | = | 2px solid #20afff offset 2px |
| Font | Inter 16px/18.4px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Ancestor paint | - | 3 up div.relative.mx-auto bg #292c33 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 4px 8px 0px | 3 up div.relative.mx-auto bg #292c33 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 4px 8px 0px | 3 up div.relative.mx-auto bg #292c33 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 4px 8px 0px | = |
| Painted layers | - | = | button.focus-visible._iconButton_wmtv6_1 44.0x44.0 r 10000px outline 2px solid #20afff offset 2px | = | button.focus-visible._iconButton_wmtv6_1 44.0x44.0 r 10000px outline 2px solid #20afff offset 2px |

Crops: `m-hamburger-default.png`, `m-hamburger-hover.png`, `m-hamburger-focus-visible.png`, `m-hamburger-pressed.png`, `m-hamburger-opened.png`.

#### m-nav-item

Mobile nav link. A link inside the opened phone nav; measured, never followed.

Page: mobile. Selector: `mobile nav Pricing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 326 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 10000px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.es-text-button-s._text_1qq63_1: Inter 14px/24px 600, #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 20 x 20, colour #ffffff |
| Ancestor paint | 3 up div.relative.mx-auto bg #292c33 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.035 0px 1.83076px 3.66151px 0px |
| How | at rest |

Crops: `m-nav-item-default.png`.

#### m-cta

Mobile CTA. The Create-free-account button in the phone header; measured never followed.

Page: mobile. Selector: `mobile Create free account`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 173 x 44 | = | = | = |
| Padding | 4px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 10000px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #20afff offset 2px | = |
| Font | Inter 14px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.no-default-focus.focus-visible 173.0x44.0 bg #ffffff r 10000px | = | a.no-default-focus.focus-visible 173.0x44.0 bg #ffffff r 10000px outline 2px solid #20afff offset 2px | = |
| Ancestor paint | 3 up div.relative.mx-auto bg #292c33 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 4px 8px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-cta-default.png`, `m-cta-hover.png`, `m-cta-focus-visible.png`, `m-cta-pressed.png`.

#### m-genre-h1

Mobile genre heading. "Pop music" on the phone genre banner.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 125.69 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sebenta 24px/30px 500 |
| Letter spacing | -0.48px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `m-genre-h1-default.png`.

#### m-track-row

Mobile track row. A 56px track row in the phone list (cover, title, artist).

Page: mobile. Selector: `mobile track row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 56 |
| Padding | 0px 8px 0px 0px |
| Gap | 16px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.es-text-button-s.es-color-text-primary: Inter 14px/24px 600, #ffffff |
| Transition | none |
| Icon | 0 x 0, colour #ffffff |
| Painted layers | button.TrackRowPlayButton_albumCover__Pv48J.overflow-hidden 56.0x56.0 bg #6b6b6b r 4px; button.TrackRowPlayButton_albumCover__Pv48J.rounded-(--es-radius-detail) 0.0x0.0 bg #cfd6e5 @ 0.16 r 4px; button.focus-visible._iconButton_wmtv6_1 0.0x0.0 bg #cfd6e5 @ 0 r 10000px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 bg #cfd6e5 @ 0 r 10000px; button.focus-visible._iconButton_wmtv6_1 0.0x0.0 bg #cfd6e5 @ 0 r 10000px; button.focus-visible._iconButton_wmtv6_1 0.0x0.0 bg #cfd6e5 @ 0 r 10000px |
| How | at rest |

Crops: `m-track-row-default.png`.

## Transitions declared in the readable stylesheets

epidemicsound.com serves its CSS bundles same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- genre: `stroke-width 0.12s linear`, `stroke-dashoffset 0.12s linear, stroke-width 0.16s ease-in 0.06s`, `transform 0.32s ease-in-out`, `transform 0.32s ease-out 0.16s`, `opacity 0.12s ease-in-out`, `opacity 0.1s ease-in-out, transform 0.1s ease-in-out`, `opacity 0.06s ease-in-out`, `opacity 0.2s ease-out`, `opacity 1s cubic-bezier(0.215, 0.61, 0.355, 1)`, `width 0.6s cubic-bezier(0.9, 0, 0, 1)`, `transform 0.6s cubic-bezier(0.9, 0, 0, 1)`, `none`

- home: `stroke-width 0.12s linear`, `stroke-dashoffset 0.12s linear, stroke-width 0.16s ease-in 0.06s`, `transform 0.32s ease-in-out`, `transform 0.32s ease-out 0.16s`, `opacity 0.12s ease-in-out`, `opacity 0.1s ease-in-out, transform 0.1s ease-in-out`, `opacity 0.06s ease-in-out`, `opacity 0.2s ease-out`, `opacity 1s cubic-bezier(0.215, 0.61, 0.355, 1)`, `width 0.6s cubic-bezier(0.9, 0, 0, 1)`, `transform 0.6s cubic-bezier(0.9, 0, 0, 1)`, `none`

- login: `background-color 600000s, color 600000s`, `background-color 100ms`, `100ms`

- pricing: `stroke-width 0.12s linear`, `stroke-dashoffset 0.12s linear, stroke-width 0.16s ease-in 0.06s`, `transform 0.32s ease-in-out`, `transform 0.32s ease-out 0.16s`, `opacity 0.12s ease-in-out`, `opacity 0.1s ease-in-out, transform 0.1s ease-in-out`, `opacity 0.06s ease-in-out`, `opacity 0.2s ease-out`, `opacity 1s cubic-bezier(0.215, 0.61, 0.355, 1)`, `width 0.6s cubic-bezier(0.9, 0, 0, 1)`, `transform 0.6s cubic-bezier(0.9, 0, 0, 1)`, `none`

- sfx: `stroke-width 0.12s linear`, `stroke-dashoffset 0.12s linear, stroke-width 0.16s ease-in 0.06s`, `transform 0.32s ease-in-out`, `transform 0.32s ease-out 0.16s`, `opacity 0.12s ease-in-out`, `opacity 0.1s ease-in-out, transform 0.1s ease-in-out`, `opacity 0.06s ease-in-out`, `opacity 0.2s ease-out`, `opacity 1s cubic-bezier(0.215, 0.61, 0.355, 1)`, `width 0.6s cubic-bezier(0.9, 0, 0, 1)`, `transform 0.6s cubic-bezier(0.9, 0, 0, 1)`, `none`

- signup: `background-color 600000s, color 600000s`, `background-color 100ms`, `100ms`
