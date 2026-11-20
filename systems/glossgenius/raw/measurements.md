# GlossGenius component measurements

Computed styles read from glossgenius.com, app.glossgenius.com and honeyhivesalon.glossgenius.com on 2026-11-16 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the public surfaces — the light-only Webflow marketing pages, the signed-out /login, /signup and /forgot-password forms of the app, and a real published booking website (every business gets a public <name>.glossgenius.com site; the service list, professional select and /book date-picker step) — with any consent layer hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Site chrome

#### mkt-header

Site header. The marketing top bar: the GlossGenius wordmark, the "How it works" / "Businesses" / "Resources" mega-menus, Pricing, "Log in" and the "Book a demo" pill.

Page: home. Selector: `.header_new`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 72 |
| Padding | 0px 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Grotesk Book 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #17150e |
| Text node | div: Basel Grotesk Book 16px/24px 400, #ffffff |
| Transition | background-color 0.25s cubic-bezier(0.165, 0.84, 0.44, 1) |
| Icon | 148 x 12.47, colour #ffffff |
| Painted layers | div.dropdown_new__list-content.dropdown_new__list-content--hiw 960.0x435.4 bg #ffffff r 16px; a.btn_new.w-variant-86ea12c4-a0f3-2df0-292c-65a8bd110cde 252.7x40.4 bg #9fa6ff border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 0px inset; div.card_new.u-bg-gloss-white 370.7x387.4 bg #f0f7f6 r 16px; div.img-wrapper_new.u-radius-8 354.7x312.1 image linear-gradient(#cccc25, #cacd78) r 8px; div.dropdown_new__list-content.dropdown_new__list-content--customers 607.0x367.0 bg #ffffff r 16px |
| Ancestor paint | 1 up div.page-wrapper_new bg #ffffff |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The GlossGenius wordmark in the header, linking home.

Page: home. Selector: `.header_new__logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 164 x 28.47 |
| Padding | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Grotesk Book 16px/19.2px 500 |
| Letter spacing | 1px |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| Icon | 148 x 12.47, colour #ffffff |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-link

Nav link. A marketing header nav link (Pricing); measured, never followed.

Page: home. Selector: `header Pricing link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 75 x 72 | = | = | = |
| Padding | 24px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Basel Grotesk Book 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.nav-link.u-z-index-1 75.0x72.0 outline 1px auto #101010 offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-hiw

How-it-works menu trigger. The "How it works" nav item that opens the feature mega-menu (Agents, Booking & Scheduling, Marketing & CRM, Payments & POS, Staff & Business, EMR rails).

Page: home. Selector: `nav How it works trigger`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 139 x 72 | = | = | = | = |
| Padding | 24px 12px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Basel Grotesk Book 16px/24px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | = | = | = | = |
| Text node | div: Basel Grotesk Book 16px/24px 400, #ffffff | = | = | = | = |
| Transition | color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | hovered the "How it works" trigger; the CSS-hover mega-menu is held open by the parked pointer (aria-expanded=true at save) |

Crops: `nav-hiw-default.png`, `nav-hiw-hover.png`, `nav-hiw-focus-visible.png`, `nav-hiw-pressed.png`, `nav-hiw-opened.png`.

#### nav-drop-item

Mega-menu item. A feature link inside the opened "How it works" mega-menu; measured while the CSS-hover menu was held open by the parked pointer, never followed.

Page: home. Selector: `.nav-list--dropdown a`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 104 x 41.59 |
| Padding | 8px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Grotesk Book 20px/24px 500 |
| Letter spacing | normal |
| Colour | #17150e |
| Text node | div: Basel Grotesk Book 20px/24px 500, #17150e |
| Transition | color, opacity, box-shadow, flex-grow 0.75s, 0.75s, 0.75s, 0.75s cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.23, 1, 0.32, 1), cubic-bezier(0.23, 1, 0.32, 1) |
| Cursor | pointer |
| How | at rest |

Crops: `nav-drop-item-default.png`.

#### nav-login

Log in button. The header "Log in" button to app.glossgenius.com; measured, never followed.

Page: home. Selector: `header Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 94 x 48.41 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 1440px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px inset | = | = | = |
| Outline | none | = | 1px solid #17150e offset 1.5px | = |
| Font | Basel Grotesk Book 16px/22.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div: Basel Grotesk Book 16px/22.4px 400, #ffffff | = | = | = |
| Transition | color, background-color, box-shadow, border-color 0.5s, 0.5s, 0.5s, 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1) delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn_new.w-variant-325a472b-1f0c-1e9e-2bfc-28654d2d9a2a 94.0x48.4 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset | = | a.btn_new.w-variant-325a472b-1f0c-1e9e-2bfc-28654d2d9a2a 94.0x48.4 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset outline 1px solid #17150e offset 1.5px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-demo

Book a demo pill. The header "Book a demo" pill to /get-demo; measured, never followed.

Page: home. Selector: `header Book a demo`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 143 x 48.41 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #f0f7f6 | = | = | = |
| Radius | 1440px | = | = | = |
| Background | transparent | = | = | #17150e @ 0.0282147 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px inset | = | = | = |
| Outline | none | = | 1px solid #17150e offset 1.5px | = |
| Font | Basel Grotesk Book 16px/22.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div: Basel Grotesk Book 16px/22.4px 400, #ffffff | = | = | = |
| Transition | color, background-color, box-shadow, border-color 0.5s, 0.5s, 0.5s, 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1) delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn_new.w-variant-8c031957-40f4-c354-ca0e-e5ce4a4bf4d7 143.0x48.4 border T:1px #f0f7f6 / R:1px #f0f7f6 / B:1px #f0f7f6 / L:1px #f0f7f6 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset | a.btn_new.w-variant-8c031957-40f4-c354-ca0e-e5ce4a4bf4d7 143.0x48.4 bg #000000 @ 0 border T:1px #f0f7f6 / R:1px #f0f7f6 / B:1px #f0f7f6 / L:1px #f0f7f6 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset | a.btn_new.w-variant-8c031957-40f4-c354-ca0e-e5ce4a4bf4d7 143.0x48.4 border T:1px #f0f7f6 / R:1px #f0f7f6 / B:1px #f0f7f6 / L:1px #f0f7f6 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset outline 1px solid #17150e offset 1.5px | a.btn_new.w-variant-8c031957-40f4-c354-ca0e-e5ce4a4bf4d7 143.0x48.4 bg #17150e @ 0.0282147 border T:1px #f0f7f6 / R:1px #f0f7f6 / B:1px #f0f7f6 / L:1px #f0f7f6 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-demo-default.png`, `nav-demo-hover.png`, `nav-demo-focus-visible.png`, `nav-demo-pressed.png`.

#### gg-support

Support bubble. The fixed support/chat launcher pinned to the corner of every marketing page; measured, never opened.

Page: home. Selector: `.gg-support-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56 x 56 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 1440px | = | = | = |
| Background | #17150e | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Basel Grotesk Book 16px/22.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f0f7f6 | = | = | = |
| Text node | span.icon_new.w-variant-677e82ce-51de-5fa2-88f1-c453538ba1c5: remixicon 20px/20px 400, #f0f7f6 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.gg-support-btn 56.0x56.0 bg #17150e r 1440px | = | button.gg-support-btn 56.0x56.0 bg #17150e r 1440px outline 1px auto #101010 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `gg-support-default.png`, `gg-support-hover.png`, `gg-support-focus-visible.png`, `gg-support-pressed.png`.

### Home

#### hero-eyebrow

Hero eyebrow. The eyebrow line above the hero heading.

Page: home. Selector: `.eyebrow_new`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 96 x 22.39 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Grotesk Book 16px/22.4px 500 |
| Letter spacing | normal |
| Colour | #17150e |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 16) |
| Opacity | 0 |
| How | at rest |

Crops: `hero-eyebrow-default.png`.

#### hero-h1

Hero headline. "Scheduling, payments, and admin. Handled." — the display heading.

Page: home. Selector: `home h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 926.66 x 139.66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Classic Book 72px/69.84px 500 |
| Letter spacing | -2.16px |
| Colour | #f0f7f6 |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-cta

Hero CTA. The hero "Start free trial" button to /free-trial (the u-sm-w-100 button group — the header and mobile-nav button groups are excluded); measured, never followed.

Page: home. Selector: `hero Start free trial`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 154.39 x 48.41 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 1440px | = | = | = |
| Background | #ffffff | #e1e0e0 | = | #e1e1e0 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px inset | = | = | = |
| Outline | none | = | 1px solid #17150e offset 1.5px | = |
| Font | Basel Grotesk Book 16px/22.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #17150e | = | = | = |
| Text node | span.icon_new.w-variant-7af529f9-3bfd-fc24-81c8-b7eb88c81c1a: remixicon 16px/16px 400, #17150e | = | = | = |
| Transition | color, background-color, box-shadow, border-color 0.5s, 0.5s, 0.5s, 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1) delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn_new.w-variant-325a472b-1f0c-1e9e-2bfc-28654d2d9a2a 154.4x48.4 bg #ffffff border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset | a.btn_new.w-variant-325a472b-1f0c-1e9e-2bfc-28654d2d9a2a 154.4x48.4 bg #e1e0e0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset | a.btn_new.w-variant-325a472b-1f0c-1e9e-2bfc-28654d2d9a2a 154.4x48.4 bg #ffffff border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset outline 1px solid #17150e offset 1.5px | a.btn_new.w-variant-325a472b-1f0c-1e9e-2bfc-28654d2d9a2a 154.4x48.4 bg #e1e1e0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-demo

Hero demo link. The hero "Get a demo" action; measured, never followed.

Page: home. Selector: `hero Get a demo`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 99 x 33.59 | = | - | = |
| Padding | 8px | = | - | = |
| Gap | 8px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Basel Grotesk Book 16px/17.6px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #17150e | = | - | = |
| Transition | opacity 0.75s cubic-bezier(0.165, 0.84, 0.44, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `hero-demo-default.png`, `hero-demo-hover.png`, `hero-demo-pressed.png`.

#### home-h2

Section heading. A section heading on the marketing home.

Page: home. Selector: `home h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 96 x 22.39 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Grotesk Book 16px/22.4px 500 |
| Letter spacing | normal |
| Colour | #17150e |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `home-h2-default.png`.

#### home-prose

Body paragraph. A body paragraph on the marketing home.

Page: home. Selector: `home p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 532.2 x 38.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Grotesk Book 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #f0f7f6 |
| Transition | none |
| How | at rest |

Crops: `home-prose-default.png`.

#### home-card

Home card. A feature/benefit card on the marketing home.

Page: home. Selector: `home [class*=card]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1243.63 x 659.88 | = |
| Padding | 0px 12px | = |
| Gap | 20px 16px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Basel Grotesk Book 16px/19.2px 500 | = |
| Letter spacing | normal | = |
| Colour | #17150e | = |
| Text node | h4.h4_new.u-mb-8: Basel Grotesk Book 32px/35.2px 500, #17150e, ls -0.64px | = |
| Transition | none | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = |
| Painted layers | div.img-wrapper_new.img-wrapper_new--tabs 1219.6x659.9 image linear-gradient(#f0f7f6, #c7cfd1) r 24px; div.swiper-progress-wrap 1219.6x329.9 image linear-gradient(#000000 @ 0, #17150e @ 0.1); div.swiper-progress 1187.6x8.0 bg #ffffff @ 0.5 r 1440px; div.swiper-progress__bar 1187.6x8.0 bg #ffffff r 1440px | div.img-wrapper_new.img-wrapper_new--tabs 1219.6x659.9 image linear-gradient(#f0f7f6, #c7cfd1) r 24px; div.swiper-progress-wrap 1219.6x329.9 image linear-gradient(#000000 @ 0, #17150e @ 0.1); div.swiper-progress 1187.6x8.0 bg #ffffff @ 0.5 r 1440px; div.swiper-progress__bar 39.2x8.0 bg #ffffff r 1440px |
| How | at rest | mouse hover |

Crops: `home-card-default.png`, `home-card-hover.png`.

### Footer

#### home-footer

Footer. The marketing footer: closing CTA, link columns, legal links and social marks.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 135 x 111.97 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Grotesk Book 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #f0f7f6 |
| Text node | a.link_new: Basel Grotesk Book 16px/17.6px 400, #f0f7f6 |
| Transition | none |
| How | at rest |

Crops: `home-footer-default.png`.

### Pricing

#### ptoggle

Billing toggle. The Monthly/Annual ("save up to 14%") switch above the plan cards — a checkbox-backed .toggle_new that loads annual-checked; opened was measured after clicking its input to select Monthly (a local UI toggle).

Page: pricing. Selector: `.toggle_new`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 307 x 32 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Basel Grotesk Book 16px/19.2px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #17150e | = | = | = | = |
| Text node | span: Basel Grotesk Book 16px/19.2px 500, #778280 | = | = | = | span: Basel Grotesk Book 16px/19.2px 500, #17150e |
| Transition | none | = | = | = | = |
| Painted layers | input.toggle_new__checkbox 64.0x32.0 bg #17150e r 1440px; input::before.toggle_new__checkbox 24pxx24px bg #f0f7f6 r 50% | = | input.toggle_new__checkbox 64.0x32.0 bg #17150e r 1440px outline 1px auto #101010 offset 2px; input::before.toggle_new__checkbox 24pxx24px bg #f0f7f6 r 50% | = | input.toggle_new__checkbox 64.0x32.0 bg #778280 r 1440px; input::before.toggle_new__checkbox 24pxx24px bg #f0f7f6 r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | clicked the Monthly/Annual switch input to show monthly prices (annual is the default) |

Crops: `ptoggle-default.png`, `ptoggle-hover.png`, `ptoggle-focus-visible.png`, `ptoggle-pressed.png`, `ptoggle-opened.png`.

#### ptier

Plan tier dropdown. The "Beauty & Wellness / Medspa & Aesthetics" plan-tier picker; opened was measured after clicking it — a local UI toggle whose options were never activated.

Page: pricing. Selector: `.dropdown_new--pricing-tiers toggle`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 315 x 41 | = | = | = | = |
| Padding | 8px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 32px | = | = | = | = |
| Background | #ffffff | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Basel Grotesk Book 16px/19.2px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #222222 | = | = | = | = |
| Text node | div: Basel Grotesk Book 16px/19.2px 500, #222222 | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | div.dropdown_new__toggle.dropdown_new__toggle--pricing-tiers 315.0x41.0 bg #ffffff r 32px | = | = | = | = |
| Ancestor paint | 1 up div.dropdown_new.dropdown_new--pricing-tiers bg #c7cfd1 | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | clicked the tier dropdown to list "Beauty & Wellness / Medspa & Aesthetics" (aria-expanded=true at save) |

Crops: `ptier-default.png`, `ptier-hover.png`, `ptier-focus-visible.png`, `ptier-pressed.png`, `ptier-opened.png`.

#### ptier-option

Tier option. The "Medspa & Aesthetics" option row inside the opened tier dropdown (the current option, "Beauty & Wellness", is display:none); measured while the list was held open, never activated.

Page: pricing. Selector: `pricing tier option`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 323 x 41.59 |
| Padding | 12px 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Grotesk Book 16px/17.6px 400 |
| Letter spacing | normal |
| Colour | #17150e |
| Transition | opacity 0.75s cubic-bezier(0.165, 0.84, 0.44, 1) |
| Cursor | pointer |
| Ancestor paint | 1 up div.dropdown_new__list-content.dropdown_new__list-content--pricing-tiers bg #c7cfd1 |
| How | at rest |

Crops: `ptier-option-default.png`.

#### plan-card

Plan card. A pricing plan card (Standard: $28/mo monthly, $24/mo annual — "Essential tools for businesses just starting out").

Page: pricing. Selector: `.card-main:first`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 357.33 x 404.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Grotesk Book 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #17150e |
| Text node | div.h3_new: Basel Grotesk Book 40px/40px 500, #17150e, ls -1.2px |
| Transition | none |
| Painted layers | div.pricing-table-row 357.3x52.6 border T:1px #a0afb0 @ 0.7; div.pricing-table-row 357.3x52.6 border T:1px #a0afb0 @ 0.7; a.btn_new.w-inline-block 357.3x48.4 bg #17150e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-card-popular

Popular plan card. The "Most popular" Gold plan card ($56/$48 monthly) — the .card_new--pricing-small column carrying the amber tag; hover is a pointer hover, never clicked through.

Page: pricing. Selector: `.card_new popular`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 389.33 x 629.16 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Basel Grotesk Book 16px/19.2px 500 | = |
| Letter spacing | normal | = |
| Colour | #17150e | = |
| Text node | h3.h3_new: Basel Grotesk Book 40px/40px 500, #17150e, ls -1.2px | = |
| Transition | background-color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1) | = |
| Painted layers | div.card_new.card_new--pricing-small 389.3x629.2 bg #ffffff r 16px; div.tag.w-variant-7e9897a3-00c5-24cf-4cb3-2bdd969fa01a 128.0x37.2 bg #e89c2a border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px; div.pricing-table-row 357.3x52.6 border T:1px #a0afb0 @ 0.7; div.pricing-table-row 357.3x52.6 border T:1px #a0afb0 @ 0.7; a.btn_new.w-inline-block 357.3x48.4 bg #17150e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset | = |
| How | at rest | mouse hover |

Crops: `plan-card-popular-default.png`, `plan-card-popular-hover.png`.

#### plan-price

Plan price. The struck/full price block inside a plan card.

Page: pricing. Selector: `.card_new-price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 357.33 x 40 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Grotesk Book 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #17150e |
| Text node | div.h3_new: Basel Grotesk Book 40px/40px 500, #17150e, ls -1.2px |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. A plan card's action button/link; its states were measured but it was never followed — no checkout.

Page: pricing. Selector: `.card-main action`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 357.33 x 48.41 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 1440px | = | = | = |
| Background | #17150e | #17150e @ 0.800164 | = | #17150e @ 0.8 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px inset | = | = | none |
| Outline | none | = | 1px solid #17150e offset 1.5px | = |
| Font | Basel Grotesk Book 16px/22.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f0f7f6 | = | = | = |
| Text node | div: Basel Grotesk Book 16px/22.4px 400, #f0f7f6 | = | = | = |
| Transition | color, background-color, box-shadow, border-color 0.5s, 0.5s, 0.5s, 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1) delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn_new.w-inline-block 357.3x48.4 bg #17150e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset | a.btn_new.w-inline-block 357.3x48.4 bg #17150e @ 0.800164 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset | a.btn_new.w-inline-block 357.3x48.4 bg #17150e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset outline 1px solid #17150e offset 1.5px | a.btn_new.w-inline-block 357.3x48.4 bg #17150e @ 0.8 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-row

Plan feature row. A feature/comparison row inside the pricing block (rate or feature line).

Page: pricing. Selector: `plan feature row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 357.33 x 52.59 |
| Padding | 16px 0px |
| Border | T: 1px solid #a0afb0 @ 0.7; R: none; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Grotesk Book 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #778280 |
| Text node | div: Basel Grotesk Book 16px/19.2px 500, #17150e |
| Transition | none |
| Painted layers | div.pricing-table-row 357.3x52.6 border T:1px #a0afb0 @ 0.7 |
| How | at rest |

Crops: `plan-row-default.png`.

#### ptab-nav

Compare-table plan nav. A plan chip in the "Compare plans" table navigator.

Page: pricing. Selector: `.pricing-table-nav__plan`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 323 x 106.8 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Basel Grotesk Book 16px/19.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #17150e | = | = | = |
| Text node | div: Basel Grotesk Book 22px/26.4px 500, #17150e, ls -0.44px | = | = | = |
| Transition | none | = | = | = |
| Painted layers | div.label_new.u-bg-gloss-white 323.0x42.4 bg #f0f7f6 r 8px; a.btn_new.w-inline-block 323.0x48.4 bg #17150e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset | = | div.label_new.u-bg-gloss-white 323.0x42.4 bg #f0f7f6 r 8px; a.btn_new.w-inline-block 323.0x48.4 bg #17150e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset outline 1px solid #17150e offset 1.5px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ptab-nav-default.png`, `ptab-nav-hover.png`, `ptab-nav-pressed.png`.

#### faq-item

FAQ accordion. A native <details>/<summary> disclosure in the pricing "Included in every plan" list; opened was measured after clicking the summary row (a local UI toggle).

Page: pricing. Selector: `details.accordion-item`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 1352 x 211 | = | 1352 x 97 |
| Padding | 0px | = | = |
| Border | T: none; R: none; B: 1px solid #a0afb0 @ 0.7; L: none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Basel Grotesk Book 16px/19.2px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #17150e | = | = |
| Text node | label.accordion-title.h4_new: Basel Grotesk Book 32px/35.2px 500, #17150e, ls -0.64px | = | = |
| Transition | none | = | = |
| Icon | 67.88 x 67.88, colour #17150e | = | 48 x 48, colour #17150e |
| Painted layers | details.accordion-item 1352.0x211.0 border B:1px #a0afb0 @ 0.7; div.pricing-table-row 1352.0x57.0 border T:1px #a0afb0 @ 0.7; div.pricing-table-row 1352.0x57.0 bg #f0f7f6 @ 0.3 border T:1px #a0afb0 @ 0.7; div.pricing-table-row 1352.0x71.4 bg #f0f7f6 @ 0.3 border T:1px #a0afb0 @ 0.7; div.pricing-table-row 1352.0x71.4 bg #f0f7f6 @ 0.3 border T:1px #a0afb0 @ 0.7; div.pricing-table-row 1352.0x57.0 border T:1px #a0afb0 @ 0.7 | = | details.accordion-item 1352.0x97.0 border B:1px #a0afb0 @ 0.7; div.pricing-table-row 1352.0x57.0 border T:1px #a0afb0 @ 0.7; div.pricing-table-row 1352.0x57.0 bg #f0f7f6 @ 0.3 border T:1px #a0afb0 @ 0.7; div.pricing-table-row 1352.0x71.4 bg #f0f7f6 @ 0.3 border T:1px #a0afb0 @ 0.7; div.pricing-table-row 1352.0x71.4 bg #f0f7f6 @ 0.3 border T:1px #a0afb0 @ 0.7; div.pricing-table-row 1352.0x57.0 border T:1px #a0afb0 @ 0.7 |
| How | at rest | mouse hover | clicked the accordion summary to expand its answer |

Crops: `faq-item-default.png`, `faq-item-hover.png`, `faq-item-opened.png`.

#### faq-answer

Accordion content. An expanded accordion's answer block (plan feature rows).

Page: pricing. Selector: `.accordion-content`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1352 x 285 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Grotesk Book 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #17150e |
| Text node | label.accordion-title.paragraph-body: Basel Grotesk Book 16px/19.2px 500, #17150e |
| Transition | none |
| Painted layers | div.pricing-table-row 1352.0x57.0 border T:1px #a0afb0 @ 0.7; div.pricing-table-row 1352.0x57.0 bg #f0f7f6 @ 0.3 border T:1px #a0afb0 @ 0.7; div.pricing-table-row 1352.0x57.0 bg #f0f7f6 @ 0.3 border T:1px #a0afb0 @ 0.7; div.pricing-table-row 1352.0x57.0 bg #f0f7f6 @ 0.3 border T:1px #a0afb0 @ 0.7; div.pricing-table-row 1352.0x57.0 bg #f0f7f6 @ 0.3 border T:1px #a0afb0 @ 0.7; div.pricing-table-row 1352.0x57.0 bg #f0f7f6 @ 0.3 border T:1px #a0afb0 @ 0.7 |
| How | at rest |

Crops: `faq-answer-default.png`.

### Feature page

#### feat-h1

Feature headline. The /online-booking display heading ("Book more clients fast", h2.h1_new).

Page: feature. Selector: `feature h2.h1_new`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 91.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Classic Book 96px/91.2px 400 |
| Letter spacing | -2.88px |
| Colour | #17150e |
| Transition | none |
| How | at rest |

Crops: `feat-h1-default.png`.

#### feat-cta

Feature CTA. The feature page's "Get started for free" hero action; measured, never followed.

Page: feature. Selector: `feature CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 386.66 x 48.41 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 1440px | = | = | = |
| Background | #17150e | #17150e @ 0.8 | = | #17150e @ 0.800165 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px inset | none | = | = |
| Outline | none | = | 1px solid #17150e offset 1.5px | = |
| Font | Basel Grotesk Book 16px/22.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f0f7f6 | = | = | = |
| Text node | div: Basel Grotesk Book 16px/22.4px 400, #f0f7f6 | = | = | = |
| Transition | color, background-color, box-shadow, border-color 0.5s, 0.5s, 0.5s, 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1) delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn_new.w-inline-block 386.7x48.4 bg #17150e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset | a.btn_new.w-inline-block 386.7x48.4 bg #17150e @ 0.8 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px | a.btn_new.w-inline-block 386.7x48.4 bg #17150e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset outline 1px solid #17150e offset 1.5px | a.btn_new.w-inline-block 386.7x48.4 bg #17150e @ 0.800165 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `feat-cta-default.png`, `feat-cta-hover.png`, `feat-cta-focus-visible.png`, `feat-cta-pressed.png`.

#### feat-card

Feature card. A capability card on the online-booking feature page.

Page: feature. Selector: `feature [class*=card]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 386.66 x 302 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #f0f7f6 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Basel Grotesk Book 16px/19.2px 500 | = |
| Letter spacing | normal | = |
| Colour | #17150e | = |
| Text node | div.stat-number_new: Basel Grotesk Book 72px/69.84px 500, #17150e, ls -2.16px | = |
| Transition | background-color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1) | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = |
| Painted layers | div.card_new.card_new--stat 386.7x302.0 bg #f0f7f6 r 8px | = |
| How | at rest | mouse hover |

Crops: `feat-card-default.png`, `feat-card-hover.png`.

#### feat-prose

Feature paragraph. A body paragraph on the feature page.

Page: feature. Selector: `feature p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 590 x 79.17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Grotesk Book 22px/26.4px 500 |
| Letter spacing | -0.44px |
| Colour | #17150e |
| Transition | none |
| How | at rest |

Crops: `feat-prose-default.png`.

### Demo form

#### demo-h1

Demo headline. The /get-demo page heading ("See how GlossGenius works").

Page: demo. Selector: `demo h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 91.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Classic Book 96px/91.2px 400 |
| Letter spacing | -2.88px |
| Colour | #17150e |
| Transition | none |
| How | at rest |

Crops: `demo-h1-default.png`.

#### demo-field

Demo text field. A step-2 text input (firstname/lastname); measured with the step-2 wrapper unhidden — focused and typed into then cleared, never submitted.

Page: demo. Selector: `form.form-new input.input_new`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 244 x 56 | = | = |
| Padding | 19.2px 16px 0px 16px | = | = |
| Border | 1px solid #000000 @ 0 | 1px solid #17150e | 1px solid #17150e |
| Radius | 12px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Basel Grotesk Book 16px/16px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #17150e | = | = |
| Transition | background-color, border-color 0.3s, 0.3s cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1) delay 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | #000000 @ 0, opacity 1 | = | = |
| Painted layers | input.input_new.u-w-100 244.0x56.0 bg #ffffff border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px | input.input_new.u-w-100 244.0x56.0 bg #ffffff border T:1px #17150e / R:1px #17150e / B:1px #17150e / L:1px #17150e r 12px | input.input_new.u-w-100 244.0x56.0 bg #ffffff border T:1px #17150e / R:1px #17150e / B:1px #17150e / L:1px #17150e r 12px |
| How | at rest | clicked into the field | typed "Example name", then deleted; nothing sent |

Crops: `demo-field-default.png`, `demo-field-focused.png`, `demo-field-filled.png`.

#### demo-email

Demo email field. The step-2 e-mail input; measured with the step-2 wrapper unhidden — focused and typed into then cleared, never submitted.

Page: demo. Selector: `form.form-new email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 244 x 56 | = | = |
| Padding | 19.2px 16px 0px 16px | = | = |
| Border | 1px solid #000000 @ 0 | 1px solid #17150e | 1px solid #17150e |
| Radius | 12px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Basel Grotesk Book 16px/16px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #17150e | = | = |
| Transition | background-color, border-color 0.3s, 0.3s cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1) delay 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | #000000 @ 0, opacity 1 | = | = |
| Painted layers | input.input_new.u-w-100 244.0x56.0 bg #ffffff border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px | input.input_new.u-w-100 244.0x56.0 bg #ffffff border T:1px #17150e / R:1px #17150e / B:1px #17150e / L:1px #17150e r 12px | input.input_new.u-w-100 244.0x56.0 bg #ffffff border T:1px #17150e / R:1px #17150e / B:1px #17150e / L:1px #17150e r 12px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `demo-email-default.png`, `demo-email-focused.png`, `demo-email-filled.png`.

#### demo-select

Demo select. A step-2 native <select> (professional type / team size / booking system); measured with the step-2 wrapper unhidden — focused, never changed or submitted.

Page: demo. Selector: `form.form-new select`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 504 x 56 | = |
| Padding | 19.2px 16px 0px 16px | = |
| Border | 1px solid #000000 @ 0 | 1px solid #17150e |
| Radius | 12px | = |
| Background | #ffffff | = |
| Background image | url(…) | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Basel Grotesk Book 16px/16px 500 | = |
| Letter spacing | normal | = |
| Colour | #000000 @ 0 | = |
| Transition | background-color, border-color 0.3s, 0.3s cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1) delay 0s, 0s | = |
| Cursor | default | = |
| Painted layers | select.input_new.input_new--select 504.0x56.0 bg #ffffff border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px | select.input_new.input_new--select 504.0x56.0 bg #ffffff border T:1px #17150e / R:1px #17150e / B:1px #17150e / L:1px #17150e r 12px |
| How | at rest | clicked into the field |

Crops: `demo-select-default.png`, `demo-select-focused.png`.

#### demo-radio

Team-size radio pill. A step-1 "How big is your team?" pill (Just me / 2-4 / 5-9 / 10+) — a label.radio_new tab; measured at rest and hovered, never chosen.

Page: demo. Selector: `#email-form label.radio_new`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 504 x 51.19 | = |
| Padding | 16px | = |
| Gap | 0px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Basel Grotesk Book 16px/19.2px 700 | = |
| Letter spacing | normal | = |
| Colour | #17150e | = |
| Text node | span.radio-btn_new__label.w-form-label: Basel Grotesk Book 16px/19.2px 400, #17150e | = |
| Transition | none | = |
| Cursor | pointer | = |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px | = |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px | = |
| Painted layers | div.w-form-formradioinput.w-form-formradioinput--inputType-custom 504.0x51.2 bg #ffffff border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 16px | div.w-form-formradioinput.w-form-formradioinput--inputType-custom 504.0x51.2 bg #ffffff border T:1px #17150e / R:1px #17150e / B:1px #17150e / L:1px #17150e r 16px |
| How | at rest | mouse hover |

Crops: `demo-radio-default.png`, `demo-radio-hover.png`.

#### demo-submit

Demo submit. The step-2 "Submit" button; measured with the step-2 wrapper unhidden but never clicked — nothing was sent.

Page: demo. Selector: `form.form-new submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 504 x 48.41 | = | = | = |
| Padding | 12px 48px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 1440px | = | = | = |
| Background | #17150e | #17150e @ 0.800386 | = | #17150e @ 0.800718 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px inset | = | = | = |
| Outline | none | = | 1px solid #17150e offset 1.5px | = |
| Font | Basel Grotesk Book 16px/22.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f0f7f6 | = | = | = |
| Transition | color, background-color, box-shadow, border-color 0.5s, 0.5s, 0.5s, 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1) delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.btn_new.btn_new--submit 504.0x48.4 bg #17150e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset | button.btn_new.btn_new--submit 504.0x48.4 bg #17150e @ 0.800386 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset | button.btn_new.btn_new--submit 504.0x48.4 bg #17150e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset outline 1px solid #17150e offset 1.5px | button.btn_new.btn_new--submit 504.0x48.4 bg #17150e @ 0.800718 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `demo-submit-default.png`, `demo-submit-hover.png`, `demo-submit-focus-visible.png`, `demo-submit-pressed.png`.

#### demo-card

Demo form card. The .card-main card holding the two-step demo form on the right of the heading.

Page: demo. Selector: `demo .card-main`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 504 x 1366.94 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Grotesk Book 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #17150e |
| Text node | h2.h3_new.u-mb-32: Basel Grotesk Book 40px/40px 500, #17150e, ls -1.2px |
| Transition | none |
| Painted layers | div.w-form-formradioinput.w-form-formradioinput--inputType-custom 504.0x51.2 bg #ffffff border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 16px; div.w-form-formradioinput.w-form-formradioinput--inputType-custom 504.0x51.2 bg #ffffff border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 16px; div.w-form-formradioinput.w-form-formradioinput--inputType-custom 504.0x51.2 bg #ffffff border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 16px; div.w-form-formradioinput.w-form-formradioinput--inputType-custom 504.0x51.2 bg #ffffff border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 16px; a.btn_new.w-variant-8c031957-40f4-c354-ca0e-e5ce4a4bf4d7 504.0x48.4 border T:1px #17150e / R:1px #17150e / B:1px #17150e / L:1px #17150e r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset; div.w-form-done 0.0x0.0 bg #dddddd |
| How | at rest |

Crops: `demo-card-default.png`.

#### demo-step-cta

Step-1 continue. The "Get a demo" link that reveals step 2; its states were measured but it was never activated — step 2 was read with its wrapper unhidden instead.

Page: demo. Selector: `demo Get a demo`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 504 x 48.41 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #17150e | 1px solid #17150e @ 0.7 | = | 1px solid #17150e @ 0.700579 |
| Radius | 1440px | = | = | = |
| Background | transparent | #17150e @ 0.1 | = | #17150e @ 0.0998069 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px inset | none | = | = |
| Outline | none | = | 1px solid #17150e offset 1.5px | = |
| Font | Basel Grotesk Book 16px/22.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #17150e | = | = | = |
| Text node | div: Basel Grotesk Book 16px/22.4px 400, #17150e | = | = | = |
| Transition | color, background-color, box-shadow, border-color 0.5s, 0.5s, 0.5s, 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1) delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn_new.w-variant-8c031957-40f4-c354-ca0e-e5ce4a4bf4d7 504.0x48.4 border T:1px #17150e / R:1px #17150e / B:1px #17150e / L:1px #17150e r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset | a.btn_new.w-variant-8c031957-40f4-c354-ca0e-e5ce4a4bf4d7 504.0x48.4 bg #17150e @ 0.1 border T:1px #17150e @ 0.7 / R:1px #17150e @ 0.7 / B:1px #17150e @ 0.7 / L:1px #17150e @ 0.7 r 1440px | a.btn_new.w-variant-8c031957-40f4-c354-ca0e-e5ce4a4bf4d7 504.0x48.4 border T:1px #17150e / R:1px #17150e / B:1px #17150e / L:1px #17150e r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset outline 1px solid #17150e offset 1.5px | a.btn_new.w-variant-8c031957-40f4-c354-ca0e-e5ce4a4bf4d7 504.0x48.4 bg #17150e @ 0.0998069 border T:1px #17150e @ 0.700579 / R:1px #17150e @ 0.700579 / B:1px #17150e @ 0.700579 / L:1px #17150e @ 0.700579 r 1440px shadow #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `demo-step-cta-default.png`, `demo-step-cta-hover.png`, `demo-step-cta-focus-visible.png`, `demo-step-cta-pressed.png`.

### App sign-up

#### signup-h1

Sign-up headline. The "Let's get started" sign-up heading on app.glossgenius.com/signup.

Page: signup. Selector: `signup heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 450 x 37 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | baselClassic 36px/37px 500 |
| Letter spacing | -1.08px |
| Colour | #2a2f2e |
| Transition | none |
| How | at rest |

Crops: `signup-h1-default.png`.

#### signup-name

Name field (sign-up). The sign-up first-name input; focused and typed into then cleared — never submitted.

Page: signup. Selector: `signup first_name input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 191 x 21 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | baselGrotesk 17px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #2a2f2e | = | = |
| Transition | box-shadow, opacity 0.2s, 0.2s ease-in-out, ease delay 0s, 0s | = | = |
| Opacity | 0 | - | - |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "Example", then deleted; nothing sent |

Crops: `signup-name-default.png`, `signup-name-focused.png`, `signup-name-filled.png`.

#### signup-email

Email field (sign-up). The sign-up e-mail input; focused and typed into then cleared — never submitted.

Page: signup. Selector: `signup email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 424 x 21 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | baselGrotesk 17px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #2a2f2e | = | = |
| Transition | box-shadow, opacity 0.2s, 0.2s ease-in-out, ease delay 0s, 0s | = | = |
| Opacity | 0 | - | - |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `signup-email-default.png`, `signup-email-focused.png`, `signup-email-filled.png`.

#### signup-pass

Password field (sign-up). The sign-up password input; focused and typed into then cleared — never submitted.

Page: signup. Selector: `signup password input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 384 x 21 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | baselGrotesk 17px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #2a2f2e | = | = |
| Transition | box-shadow, opacity 0.2s, 0.2s ease-in-out, ease delay 0s, 0s | = | = |
| Opacity | 0 | - | - |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "sample-pass-123", then deleted; nothing sent |

Crops: `signup-pass-default.png`, `signup-pass-focused.png`, `signup-pass-filled.png`.

#### signup-phone

Phone field (sign-up). The sign-up phone-number input; focused and typed into then cleared — never submitted.

Page: signup. Selector: `signup phone input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 424 x 21 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | baselGrotesk 17px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #2a2f2e | = | = |
| Transition | box-shadow, opacity 0.2s, 0.2s ease-in-out, ease delay 0s, 0s | = | = |
| Opacity | 0 | - | - |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "555 010 0100", then deleted; nothing sent |

Crops: `signup-phone-default.png`, `signup-phone-focused.png`, `signup-phone-filled.png`.

#### signup-checkbox

Professional checkbox. The "I confirm that I'm a professional or business owner" checkbox; focused via .focus() on its inner input — never clicked, never checked.

Page: signup. Selector: `signup checkbox`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 450 x 42 | = |
| Padding | 0px | = |
| Gap | 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | interLatin 14px/19.25px 100 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | span.Text_root__XjK0i.Text_size-base__5hTlv: baselGrotesk 17px/21px 500, #2a2f2e | = |
| Transition | none | = |
| Cursor | default | = |
| Painted layers | div.Checkbox_iconContainer__w3ypg 24.0x24.0 border T:1px #8e9695 / R:1px #8e9695 / B:1px #8e9695 / L:1px #8e9695 r 8px | input.Checkbox_input__iVUsy 24.0x24.0 outline 1px auto #101010 offset 2px; div.Checkbox_iconContainer__w3ypg 24.0x24.0 border T:1px #8e9695 / R:1px #8e9695 / B:1px #8e9695 / L:1px #8e9695 r 8px outline 1px solid #0d80a2 offset 0px |
| How | at rest | focused the inner input via .focus() — never clicked (a label click would check the box) |

Crops: `signup-checkbox-default.png`, `signup-checkbox-focused.png`.

#### signup-promo

Promo-code button. The "Add Promo Code" secondary button; measured, never activated.

Page: signup. Selector: `signup promo button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 159 x 36 | = | = | = |
| Padding | 0px 12px 0px 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #c9cdcc | = | = | = |
| Radius | 1000px | = | = | = |
| Background | #ffffff | #f7f9f9 | = | #eef0f0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | baselGrotesk 17px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2a2f2e | = | = | = |
| Text node | span.Button_content__g_F_4: baselGrotesk 15px/21px 535, #2a2f2e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button_root__UrOfw.Button_secondary__rHE23 159.0x36.0 bg #ffffff border T:1px #c9cdcc / R:1px #c9cdcc / B:1px #c9cdcc / L:1px #c9cdcc r 1000px | button.Button_root__UrOfw.Button_secondary__rHE23 159.0x36.0 bg #f7f9f9 border T:1px #c9cdcc / R:1px #c9cdcc / B:1px #c9cdcc / L:1px #c9cdcc r 1000px | button.Button_root__UrOfw.Button_secondary__rHE23 159.0x36.0 bg #ffffff border T:1px #c9cdcc / R:1px #c9cdcc / B:1px #c9cdcc / L:1px #c9cdcc r 1000px outline 1px auto #101010 offset 0px | button.Button_root__UrOfw.Button_secondary__rHE23 159.0x36.0 bg #eef0f0 border T:1px #c9cdcc / R:1px #c9cdcc / B:1px #c9cdcc / L:1px #c9cdcc r 1000px |
| Ancestor paint | 1 up div.SignupFormFields_addPromo__48B9Q bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-promo-default.png`, `signup-promo-hover.png`, `signup-promo-focus-visible.png`, `signup-promo-pressed.png`.

#### signup-submit

Sign-up submit. The primary sign-up submit; its states were measured but the button was never clicked — no account was created.

Page: signup. Selector: `signup submit button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 450 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 1000px | = | = | = |
| Background | #2a2f2e | #444a49 | = | #585f5e |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | baselGrotesk 17px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.Button_content__g_F_4: baselGrotesk 17px/21px 535, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button_root__UrOfw.Button_primary___mSSD 450.0x48.0 bg #2a2f2e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1000px | button.Button_root__UrOfw.Button_primary___mSSD 450.0x48.0 bg #444a49 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1000px | button.Button_root__UrOfw.Button_primary___mSSD 450.0x48.0 bg #2a2f2e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1000px outline 1px auto #101010 offset 0px | button.Button_root__UrOfw.Button_primary___mSSD 450.0x48.0 bg #585f5e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-submit-default.png`, `signup-submit-hover.png`, `signup-submit-focus-visible.png`, `signup-submit-pressed.png`.

### App restore

#### forgot-h1

Restore headline. The "Password recovery" heading on app.glossgenius.com/forgot-password.

Page: forgot. Selector: `forgot heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 450 x 37 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | baselClassic 36px/37px 500 |
| Letter spacing | -1.08px |
| Colour | #2a2f2e |
| Transition | none |
| How | at rest |

Crops: `forgot-h1-default.png`.

#### forgot-field

Email field (restore). The restore e-mail input; focused and typed into then cleared — never submitted.

Page: forgot. Selector: `forgot email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 424 x 21 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | baselGrotesk 17px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #2a2f2e | = | = |
| Transition | box-shadow, opacity 0.2s, 0.2s ease-in-out, ease delay 0s, 0s | = | = |
| Opacity | 0 | - | - |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `forgot-field-default.png`, `forgot-field-focused.png`, `forgot-field-filled.png`.

#### forgot-send

Restore submit. The "Send reset link" submit; its states were measured but the button was never clicked — no reset e-mail was sent.

Page: forgot. Selector: `forgot submit button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 450 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 1000px | = | = | = |
| Background | #2a2f2e | #444a49 | = | #585f5e |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | baselGrotesk 17px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.Button_content__g_F_4: baselGrotesk 17px/21px 535, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button_root__UrOfw.Button_primary-brand__yEKsA 450.0x48.0 bg #2a2f2e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1000px | button.Button_root__UrOfw.Button_primary-brand__yEKsA 450.0x48.0 bg #444a49 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1000px | button.Button_root__UrOfw.Button_primary-brand__yEKsA 450.0x48.0 bg #2a2f2e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1000px outline 1px auto #101010 offset 0px | button.Button_root__UrOfw.Button_primary-brand__yEKsA 450.0x48.0 bg #585f5e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `forgot-send-default.png`, `forgot-send-hover.png`, `forgot-send-focus-visible.png`, `forgot-send-pressed.png`.

#### forgot-back

Back-to-login link. The "Back to login" link; measured, never followed.

Page: forgot. Selector: `forgot back link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 450 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 1000px | = | = | = |
| Background | transparent | #f7f9f9 | = | #eef0f0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | baselGrotesk 17px/21px 100 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2a2f2e | = | = | = |
| Text node | span.Button_content__g_F_4: baselGrotesk 17px/21px 535, #2a2f2e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.Button_root__UrOfw.Button_transparent__GJaZO 450.0x48.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1000px | a.Button_root__UrOfw.Button_transparent__GJaZO 450.0x48.0 bg #f7f9f9 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1000px | a.Button_root__UrOfw.Button_transparent__GJaZO 450.0x48.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1000px outline 1px auto #101010 offset 1px | a.Button_root__UrOfw.Button_transparent__GJaZO 450.0x48.0 bg #eef0f0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `forgot-back-default.png`, `forgot-back-hover.png`, `forgot-back-focus-visible.png`, `forgot-back-pressed.png`.

### Published booking site

#### bk-nav

Booking-site nav. The published booking website's top nav (About, Our Team, Services, Portfolio, Shop, Contact, BOOK NOW).

Page: bookhome. Selector: `booking nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1312 x 199.06 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | basefont 16.96px/23.32px 100 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | a: headingfont 15.264px/25.9488px 100, #ffffff, ls 6.1056px |
| Transition | none |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | div.Navigation_overlay__f8_Ln.Navigation_overlayClosed__VFdWR 1440.0x900.0 bg #1b1d21 @ 0.5; ul.Navigation_subNav__9hoL3 208.0x48.2 bg #ffffff shadow #ffffff @ 0.1 0px 2px 4px 0px; div.Navigation_menuContainer__Hohhy.Navigation_menuContainerClosed__L_Xk3 0.0x0.0 bg #151619; button.Button_root__kEMCx.Button_transparent__cfDRh 0.0x0.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 |
| How | at rest |

Crops: `bk-nav-default.png`.

#### bk-nav-item

Booking nav link. A nav link on the booking site; measured, never followed.

Page: bookhome. Selector: `booking nav link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117.86 x 19.19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | headingfont 15.264px/25.9488px 100 | = | = | = |
| Letter spacing | 6.1056px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 117.9x19.2 outline 1px auto #101010 offset 1px | = |

Crops: `bk-nav-item-default.png`, `bk-nav-item-hover.png`, `bk-nav-item-focus-visible.png`, `bk-nav-item-pressed.png`.

#### bk-book-cta

Book Now button. The booking site's "BOOK NOW" nav button to the service list; measured, never followed.

Page: bookhome. Selector: `booking BOOK NOW`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 131.86 x 19.19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | headingfont 15.264px/25.9488px 100 | = | = | = |
| Letter spacing | 6.1056px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.Navigation_fullText__X1A8G: headingfont 15.264px/25.9488px 100, #ffffff, ls 6.1056px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 131.9x19.2 outline 1px auto #101010 offset 1px | = |

Crops: `bk-book-cta-default.png`, `bk-book-cta-hover.png`, `bk-book-cta-focus-visible.png`, `bk-book-cta-pressed.png`.

#### bk-title

Booking title. The business-name display heading ("HONEY HIVE SALON", SalonHeading) on the published booking site; the nav also carries a hidden h2 business name.

Page: bookhome. Selector: `booking h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 352.86 x 76.34 |
| Padding | 0px 0px 17.6px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | headingfont 30.528px/41.976px 300 |
| Letter spacing | 3.0528px |
| Colour | #ffffff |
| Text node | a: headingfont 30.528px/41.976px 300, #ffffff, ls 3.0528px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, -176.43, 0) |
| Cursor | pointer |
| How | at rest |

Crops: `bk-title-default.png`.

#### bk-badge

Powered-by badge. The "powered by GLOSSGENIUS" badge on the published site.

Page: bookhome. Selector: `booking powered-by`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 82.69 x 16.06 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | basefont 11.68px/16.06px 100 |
| Letter spacing | 1.168px |
| Colour | #aaaaaa |
| Transition | none |
| How | at rest |

Crops: `bk-badge-default.png`.

#### bk-pro-select

Professional select. The "Select a Professional" react-select on the service list (Any Professional, the business's pros); opened was measured with its .gg-dropdown__menu held open — an option was never chosen.

Page: bookservices. Selector: `booking professional select`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 496 x 56 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | 1px solid #9295a5 @ 0.5 | = | = | = | = |
| Radius | 10px | = | = | = | = |
| Background | #2c2e32 @ 0.25 | = | = | = | = |
| Box shadow | none | = | #727587 0px 0px 0px 1px | = | #727587 0px 0px 0px 1px |
| Outline | none | = | = | = | = |
| Font | basefont 16.96px/23.32px 100 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | = | = | = | = |
| Text node | div.gg-dropdown__single-value.css-99cyyk-singleValue: basefont 16px/22px 100, #ffffff | = | span: basefont 16.96px/23.32px 100, #ffffff | = | span: basefont 16.96px/23.32px 100, #ffffff |
| Transition | box-shadow, -webkit-box-shadow 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = | = |
| Icon | 20 x 20, colour #cccccc | = | 20 x 20, colour #666666 | = | 20 x 20, colour #666666 |
| Painted layers | div.Select_selectOuterContainer__T42GH 496.0x56.0 bg #2c2e32 @ 0.25 border T:1px #9295a5 @ 0.5 / R:1px #9295a5 @ 0.5 / B:1px #9295a5 @ 0.5 / L:1px #9295a5 @ 0.5 r 10px; div.Select_selectErrorContainer__xe9Ll 494.0x0.0 bg #21242a r 0px 0px 10px 10px | = | div.Select_selectOuterContainer__T42GH 496.0x56.0 bg #2c2e32 @ 0.25 border T:1px #9295a5 @ 0.5 / R:1px #9295a5 @ 0.5 / B:1px #9295a5 @ 0.5 / L:1px #9295a5 @ 0.5 r 10px shadow #727587 0px 0px 0px 1px; div.Select_selectErrorContainer__xe9Ll 494.0x0.0 bg #21242a r 0px 0px 10px 10px | = | div.Select_selectOuterContainer__T42GH 496.0x56.0 bg #2c2e32 @ 0.25 border T:1px #9295a5 @ 0.5 / R:1px #9295a5 @ 0.5 / B:1px #9295a5 @ 0.5 / L:1px #9295a5 @ 0.5 r 10px shadow #727587 0px 0px 0px 1px; div.gg-dropdown__menu.css-1y5o33s-menu 462.0x122.0 bg #ffffff r 4px shadow #000000 @ 0.1 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 11px 0px; div.gg-dropdown__menu-list.css-66c50f 462.0x122.0 bg #2c2e32; div.gg-dropdown__option.gg-dropdown__option--is-focused 462.0x38.0 bg #21242a @ 0.5; div.gg-dropdown__option.css-xw4ttq-option 462.0x38.0 bg #2c2e32; div.gg-dropdown__option.css-xw4ttq-option 462.0x38.0 bg #2c2e32 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | clicked "Any Professional" to open the react-select menu |

Crops: `bk-pro-select-default.png`, `bk-pro-select-hover.png`, `bk-pro-select-focus-visible.png`, `bk-pro-select-pressed.png`, `bk-pro-select-opened.png`.

#### bk-pro-option

Professional option. An option row inside the opened professional menu; measured while the menu was held open, never chosen.

Page: bookservices. Selector: `.gg-dropdown__option`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 462 x 38 |
| Padding | 8px 12px |
| Border | none |
| Radius | 0px |
| Background | #21242a @ 0.5 |
| Box shadow | none |
| Outline | none |
| Font | basefont 16px/22px 100 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.gg-dropdown__option.gg-dropdown__option--is-focused 462.0x38.0 bg #21242a @ 0.5 |
| Ancestor paint | 1 up div.gg-dropdown__menu-list.css-66c50f bg #2c2e32; 2 up div.gg-dropdown__menu.css-1y5o33s-menu bg #ffffff shadow #000000 @ 0.1 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 11px 0px |
| How | at rest |

Crops: `bk-pro-option-default.png`.

#### bk-service-card

Service card. A service card on the published list (category, name, description, price, duration, Select).

Page: bookservices. Selector: `booking service card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1154.56 x 287 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | #1b1d21 @ 0.5 0px 0px 46px 0px | = |
| Outline | none | = |
| Font | basefont 16.96px/25.44px 100 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | h2.ClassicService_title__NL0l6: headingfont 16px/19.2px 500, #0f0f11, ls 0.32px | = |
| Transition | none | = |
| Painted layers | article.ClassicService_root__Mgwgs.ClassicService_card__1cK2m 1154.6x287.0 shadow #1b1d21 @ 0.5 0px 0px 46px 0px; div.ClassicService_main__r92Ya 750.5x287.0 bg #ffffff shadow #1b1d21 @ 0.5 0px 0px 46px 0px; div::before.ClassicService_main__r92Ya 750.469pxx64px image linear-gradient(#ffffff @ 0, #ffffff 12px); button.ClassicService_button__8gVD_ 94.0x36.0 image linear-gradient(to right, #505718 0%, #807443 100%); span::after.ClassicService_option__PIV5l 0pxx18px border R:1px #747c80 | = |
| How | at rest | mouse hover |

Crops: `bk-service-card-hover.png`.

#### bk-service-select

Service Select button. A service row's "Select" button marking it for booking; opened was measured on the same pinned node after clicking it — the button flips to its selected state and the header becomes "BOOK 1 SERVICE". A local selection toggle, not a submission.

Page: bookservices. Selector: `booking Select button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 94 x 36 | = | = | = | = |
| Padding | 0px 12px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | #1b1d21 |
| Background image | linear-gradient(to right, #505718 0%, #807443 100%) | = | = | = | - |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = | = |
| Font | basefont 12px/18px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | = | = | = | #ffffff @ 0.5 |
| Transition | background 0.3s ease | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| ::after | 750.469px x 287px, absolute, bg #000000 @ 0, radius 0px | = | = | = | 743.969px x 287px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | button.ClassicService_button__8gVD_ 94.0x36.0 image linear-gradient(to right, #505718 0%, #807443 100%) | = | button.ClassicService_button__8gVD_ 94.0x36.0 image linear-gradient(to right, #505718 0%, #807443 100%) outline 1px auto #101010 offset 0px | = | button.ClassicService_button__8gVD_.ClassicService_buttonSelected__zlrdO 94.0x36.0 bg #1b1d21 |
| Ancestor paint | 3 up div.ClassicService_main__r92Ya bg #ffffff shadow #1b1d21 @ 0.5 0px 0px 46px 0px | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | clicked "Select" on a service — the row is marked for booking, nothing sent |
| Opacity | - | 0.8 | = | 0.8 | 0.8 |

Crops: `bk-service-select-default.png`, `bk-service-select-hover.png`, `bk-service-select-focus-visible.png`, `bk-service-select-pressed.png`, `bk-service-select-opened.png`.

#### bk-book-btn

BOOK bar button. The "BOOK n SERVICE" header bar; measured after a service was selected (the header's "Clear All" is a different control, never measured as this button). In the screenshot pass it was clicked to reach /book — a public navigation, never a submission.

Page: bookservices. Selector: `booking BOOK button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 211 x 40 | = | = | = |
| Padding | 12px 18px 11px 18px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(to right, #505718 0%, #807443 100%) | = | = | = |
| Box shadow | none | = | #727587 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | headingfont 14px/normal 300 | = | = | = |
| Letter spacing | 3px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: headingfont 14px/normal 300, #ffffff, ls 3px | = | = | = |
| Transition | box-shadow, opacity, -webkit-box-shadow 0.2s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 9.84, colour #ffffff | = | = | = |
| Painted layers | button.Button_root__8nq_L.BookingHeader_btnBook__lrjRh 211.0x40.0 image linear-gradient(to right, #505718 0%, #807443 100%) r 20px | = | button.Button_root__8nq_L.BookingHeader_btnBook__lrjRh 211.0x40.0 image linear-gradient(to right, #505718 0%, #807443 100%) r 20px shadow #727587 0px 0px 0px 3px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.9 | = | 0.9 |

Crops: `bk-book-btn-default.png`, `bk-book-btn-hover.png`, `bk-book-btn-focus-visible.png`, `bk-book-btn-pressed.png`.

#### bk-steps

Booking stepper. The SELECT SERVICE / DATE & TIME / YOUR DETAILS step header on /book.

Page: bookflow. Selector: `booking stepper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 173.97 x 128.73 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | basefont 16.96px/23.32px 100 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.Progress_buttonText__32Le9: headingfont 16px/22px 100, #ffffff, ls 0.64px |
| Transition | none |
| Icon | 26.17 x 26.17, colour #ffffff |
| Painted layers | button.Progress_icon__pRrDR.Progress_cursor__a8LOv 69.4x69.4 border T:2px #ffffff / R:2px #ffffff / B:2px #ffffff / L:2px #ffffff r 100%; button::before.Progress_icon__pRrDR.Progress_cursor__a8LOv 122.92pxx1px bg #ffffff; button::after.Progress_icon__pRrDR.Progress_cursor__a8LOv 122.906pxx1px bg #ffffff |
| How | at rest |

Crops: `bk-steps-default.png`.

#### bk-cal

Booking calendar. The month calendar on the date-picker step.

Page: bookflow. Selector: `booking calendar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 355.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | basefont 16.96px/23.32px 100 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.style_caption_label__nLxVF.Calendar_calendarCaption__1umkm: basefont 18px/24.75px 400, #ffffff |
| Transition | none |
| Icon | 16 x 16, colour #ffffff, fill #000000 |
| Painted layers | button.style_button_reset__4kj87.style_button__0VMxM 50.0x50.0 border T:2px #000000 @ 0 / R:2px #000000 @ 0 / B:2px #000000 @ 0 / L:2px #000000 @ 0 r 100%; div.style_caption_label__nLxVF.Calendar_calendarCaption__1umkm 149.0x28.8 border T:2px #000000 @ 0 / R:2px #000000 @ 0 / B:2px #000000 @ 0 / L:2px #000000 @ 0; button.style_button_reset__4kj87.style_button__0VMxM 50.0x50.0 border T:2px #000000 @ 0 / R:2px #000000 @ 0 / B:2px #000000 @ 0 / L:2px #000000 @ 0 r 100%; tr.Calendar_calendarHeadRow__3q8Fy 350.0x50.0 border B:1px #ffffff @ 0.4; tr.style_row__LSKg5.Calendar_calendarRow__EEFXi 350.0x51.0 border B:1px #ffffff @ 0.2; button.style_button_reset__4kj87.style_button__0VMxM 50.0x50.0 bg #21242a border T:2px #000000 @ 0 / R:2px #000000 @ 0 / B:2px #000000 @ 0 / L:2px #000000 @ 0 |
| How | at rest |

Crops: `bk-cal-default.png`.

#### bk-day

Day cell. A day cell in the booking calendar.

Page: bookflow. Selector: `booking day cell`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 50 x 51 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | basefont 16.96px/23.32px 100 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | button.style_button_reset__4kj87.style_button__0VMxM: basefont 16.96px/23.32px 100, #ffffff | = |
| Transition | none | = |
| Painted layers | button.style_button_reset__4kj87.style_button__0VMxM 50.0x50.0 bg #21242a border T:2px #000000 @ 0 / R:2px #000000 @ 0 / B:2px #000000 @ 0 / L:2px #000000 @ 0 | = |
| How | at rest | mouse hover |

Crops: `bk-day-default.png`, `bk-day-hover.png`.

#### bk-next

Next button. The date-step "Next" button; its states were measured but it was never clicked — no details form was reached.

Page: bookflow. Selector: `booking Next button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 208 x 55 | = | = | = |
| Padding | 0px 48px | = | = | = |
| Border | none | = | = | = |
| Radius | 27px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(to right, #505718 0%, #807443 100%) | = | = | = |
| Box shadow | none | = | #727587 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | basefont 16px/55px 300 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: basefont 16px/55px 300, #ffffff | = | = | = |
| Transition | box-shadow, opacity, -webkit-box-shadow 0.2s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button_root__8nq_L 208.0x55.0 image linear-gradient(to right, #505718 0%, #807443 100%) r 27px | = | button.Button_root__8nq_L 208.0x55.0 image linear-gradient(to right, #505718 0%, #807443 100%) r 27px shadow #727587 0px 0px 0px 3px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `bk-next-default.png`, `bk-next-hover.png`, `bk-next-focus-visible.png`, `bk-next-pressed.png`.

### Mobile (390 wide)

#### m-topbar

Mobile top bar. The phone header at 390 wide: wordmark, the burger and the actions that survive the width.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 72 |
| Padding | 8px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Grotesk Book 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #17150e |
| Text node | div: Basel Grotesk Book 24px/36px 400, #17150e |
| Transition | background-color 0.25s cubic-bezier(0.165, 0.84, 0.44, 1) |
| Icon | 140 x 11.8, colour #ffffff |
| Painted layers | nav.header_new__nav.w-variant-045f9404-9514-8e8f-98d8-8ee7ebff042a 390.0x0.0 bg #ffffff; div.header_new__nav-overlay.w-variant-045f9404-9514-8e8f-98d8-8ee7ebff042a 390.0x88.0 bg #ffffff; ul.nav-list.nav-list--header 358.0x208.0 bg #ffffff; div.nav-link.w-dropdown-toggle 358.0x52.0 bg #ffffff; div.dropdown_new__list-content.dropdown_new__list-content--hiw 358.0x1738.3 bg #ffffff r 16px; a.btn_new.w-variant-86ea12c4-a0f3-2df0-292c-65a8bd110cde 358.0x40.4 bg #9fa6ff border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 0px inset |
| Ancestor paint | 1 up div.page-wrapper_new bg #ffffff |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-burger

Mobile burger. The nav burger at 390 wide; opened was measured after tapping it (a local UI toggle opening the mobile menu).

Page: mobile. Selector: `mobile burger`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 390px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = | = |
| Font | Basel Grotesk Book 16px/22.4px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | = | = | = | = |
| Text node | span.icon_new.w-variant-677e82ce-51de-5fa2-88f1-c453538ba1c5: remixicon 20px/20px 400, #ffffff | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | tapped the nav burger to open the mobile menu |
| Painted layers | - | = | button.gg-support-btn 48.0x48.0 r 390px outline 1px auto #e59700 offset 0px | = | = |

Crops: `m-burger-default.png`, `m-burger-hover.png`, `m-burger-focus-visible.png`, `m-burger-pressed.png`, `m-burger-opened.png`.

#### m-menu-link

Mobile menu link. A link inside the opened mobile nav menu.

Page: mobile. Selector: `mobile menu link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 156 x 27.8 |
| Padding | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Grotesk Book 16px/19.2px 500 |
| Letter spacing | 1px |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| Icon | 140 x 11.8, colour #ffffff |
| How | at rest |

Crops: `m-menu-link-default.png`.

#### m-hero-h1

Mobile hero headline. The hero display heading ("Scheduling, payments, and admin. Handled.") at 390 wide, measured before the nav menu opens.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 326.5 x 116.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Basel Classic Book 40px/38.8px 500 |
| Letter spacing | -1.2px |
| Colour | #f0f7f6 |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-hero-cta

Mobile hero CTA. The hero action at 390 wide; measured never followed.

Page: mobile. Selector: `mobile hero CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 358 x 48.41 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #17150e | = | = | 1px solid #17150e @ 0.702644 |
| Radius | 390px | = | = | = |
| Background | transparent | = | = | #17150e @ 0.0991186 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px inset | = | = | = |
| Outline | none | = | 1px solid #17150e offset 1.5px | = |
| Font | Basel Grotesk Book 16px/22.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #17150e | = | = | = |
| Text node | div: Basel Grotesk Book 16px/22.4px 400, #17150e | = | = | = |
| Transition | color, background-color, box-shadow, border-color 0.5s, 0.5s, 0.5s, 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1), cubic-bezier(0.165, 0.84, 0.44, 1) delay 0s, 0s, 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, -16) | = | = | = |
| Opacity | 0 | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn_new.w-variant-8c031957-40f4-c354-ca0e-e5ce4a4bf4d7 358.0x48.4 border T:1px #17150e / R:1px #17150e / B:1px #17150e / L:1px #17150e r 390px shadow #000000 @ 0 0px 0px 0px 0px inset | = | a.btn_new.w-variant-8c031957-40f4-c354-ca0e-e5ce4a4bf4d7 358.0x48.4 border T:1px #17150e / R:1px #17150e / B:1px #17150e / L:1px #17150e r 390px shadow #000000 @ 0 0px 0px 0px 0px inset outline 1px solid #17150e offset 1.5px | a.btn_new.w-variant-8c031957-40f4-c354-ca0e-e5ce4a4bf4d7 358.0x48.4 bg #17150e @ 0.0991186 border T:1px #17150e @ 0.702644 / R:1px #17150e @ 0.702644 / B:1px #17150e @ 0.702644 / L:1px #17150e @ 0.702644 r 390px shadow #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-hero-cta-default.png`, `m-hero-cta-hover.png`, `m-hero-cta-focus-visible.png`, `m-hero-cta-pressed.png`.

### App sign-in

#### login-h1

Sign-in headline. The "Welcome back!" sign-in heading on app.glossgenius.com/login; pinned by size because a 1px hidden heading also matches.

Page: login. Selector: `login heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 37 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | baselClassic 36px/37px 500 |
| Letter spacing | -1.08px |
| Colour | #2a2f2e |
| Transition | none |
| How | at rest |

Crops: `login-h1-default.png`.

#### login-card

Sign-in card. The sign-in form card — e-mail and password fields, the primary "Log in" submit and the forgot-password link.

Page: login. Selector: `login form/card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 230 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | interLatin 14px/19.25px 100 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.Text_root__XjK0i.Text_size-base__5hTlv: baselGrotesk 17px/21px 500, #707877 |
| Transition | none |
| Painted layers | div.BaseInputContainer_root__UQzho.BaseInput_inputContainer__Q1AQt 390.0x59.0 bg #ffffff border T:1px #c9cdcc / R:1px #c9cdcc / B:1px #c9cdcc / L:1px #c9cdcc r 12px; div.BaseInputContainer_root__UQzho.BaseInput_inputContainer__Q1AQt 390.0x59.0 bg #ffffff border T:1px #c9cdcc / R:1px #c9cdcc / B:1px #c9cdcc / L:1px #c9cdcc r 12px; button.Button_root__UrOfw.Button_transparent__GJaZO 28.0x28.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1000px; button.Button_root__UrOfw.Button_primary-brand__yEKsA 390.0x48.0 bg #2a2f2e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1000px |
| How | at rest |

Crops: `login-card-default.png`.

#### login-field

Email field (sign-in). The sign-in e-mail input; focused and typed into then cleared — never submitted.

Page: login. Selector: `login email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 364 x 21 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | baselGrotesk 17px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #2a2f2e | = | = |
| Transition | box-shadow, opacity 0.2s, 0.2s ease-in-out, ease delay 0s, 0s | = | = |
| Opacity | 0 | - | - |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-field-default.png`, `login-field-focused.png`, `login-field-filled.png`.

#### login-pass

Password field (sign-in). The sign-in password input; focused and typed into then cleared — never submitted.

Page: login. Selector: `login password input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 324 x 21 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | baselGrotesk 17px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #2a2f2e | = | = |
| Transition | box-shadow, opacity 0.2s, 0.2s ease-in-out, ease delay 0s, 0s | = | = |
| Opacity | 0 | - | - |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "sample-pass-123", then deleted; nothing sent |

Crops: `login-pass-default.png`, `login-pass-focused.png`, `login-pass-filled.png`.

#### login-submit

Sign-in submit. The primary "Log in" submit; its states were measured but the button was never clicked — nothing was submitted.

Page: login. Selector: `login submit button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 390 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 1000px | = | = | = |
| Background | #2a2f2e | #444a49 | = | #585f5e |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | baselGrotesk 17px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.Button_content__g_F_4: baselGrotesk 17px/21px 535, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button_root__UrOfw.Button_primary-brand__yEKsA 390.0x48.0 bg #2a2f2e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1000px | button.Button_root__UrOfw.Button_primary-brand__yEKsA 390.0x48.0 bg #444a49 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1000px | button.Button_root__UrOfw.Button_primary-brand__yEKsA 390.0x48.0 bg #2a2f2e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1000px outline 1px auto #101010 offset 0px | button.Button_root__UrOfw.Button_primary-brand__yEKsA 390.0x48.0 bg #585f5e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 1000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-focus-visible.png`, `login-submit-pressed.png`.

#### login-forgot

Forgot-password link. The "Forgot Password?" link to /forgot-password; measured, never followed.

Page: login. Selector: `login forgot link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | interLatin 14px/19.25px 100 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.Text_root__XjK0i.Text_size-sm__Stkp_: baselGrotesk 15px/19px 500, #585f5e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.Login_forgotPasswordLink__06EN7 117.0x20.0 outline 1px auto #101010 offset 1px | = |

Crops: `login-forgot-default.png`, `login-forgot-hover.png`, `login-forgot-focus-visible.png`, `login-forgot-pressed.png`.

#### login-signup

Sign-up link. The "Sign up for free trial" link beside the sign-in form; measured, never followed.

Page: login. Selector: `login signup link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 129 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | baselGrotesk 15px/19px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2a2f2e | #444a49 | #585f5e | #444a49 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.TextAction_root__0Cr5x.TextAction_secondary__EEy5G 129.0x18.0 outline 1px auto #101010 offset 1px | = |

Crops: `login-signup-default.png`, `login-signup-hover.png`, `login-signup-focus-visible.png`, `login-signup-pressed.png`.

#### login-footer

App footer. The app's public footer band (About, Careers, Terms, Privacy, Contact, social icons); pinned by width because a 24px footer-classed icon also matches.

Page: login. Selector: `app footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 109 |
| Padding | 20px 72px |
| Gap | 32px |
| Border | none |
| Radius | 0px |
| Background | #eef0f0 |
| Box shadow | none |
| Outline | none |
| Font | interLatin 14px/19.25px 100 |
| Letter spacing | normal |
| Colour | #585f5e |
| Text node | span.Text_root__XjK0i.Text_size-sm__Stkp_: baselGrotesk 15px/19px 500, #2a2f2e |
| Transition | none |
| Icon | 24 x 24, colour #585f5e |
| Painted layers | footer.Footer_footer__Jo12e 1440.0x109.0 bg #eef0f0 |
| Ancestor paint | 1 up div.LoginContainer_root__rhf5N bg #ffffff |
| How | at rest |

Crops: `login-footer-default.png`.

## Transitions declared in the readable stylesheets

glossgenius.com serves its CSS same-origin-readable (the Webflow CDN bundle plus inline blocks; the app and the booking site serve their Next.js CSS chunks), so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- bookhome: `unset`, `background-color 0.5s`, `transform 0.5s ease-out, opacity 0.5s ease-out, -webkit-transform 0.5s ease-out`, `opacity 3s ease-out, opacity 3s ease-out`, `box-shadow 0.2s, -webkit-box-shadow 0.2s`, `transform 0.3s, -webkit-transform 0.3s`, `opacity 0.3s`, `background-color 0.3s`, `color 0.5s`, `opacity 0.3s, visibility 0.3s`, `top 0.5s ease-in-out, opacity 0.5s ease-in-out`, `0.2s`

- bookservices: `unset`, `background-color 0.5s`, `transform 0.5s ease-out, opacity 0.5s ease-out, -webkit-transform 0.5s ease-out`, `opacity 3s ease-out, opacity 3s ease-out`, `box-shadow 0.2s, -webkit-box-shadow 0.2s`, `transform 0.3s, -webkit-transform 0.3s`, `opacity 0.3s`, `background-color 0.3s`, `color 0.5s`, `opacity 0.3s, visibility 0.3s`, `top 0.5s ease-in-out, opacity 0.5s ease-in-out`, `0.2s`

- feature: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `0.2s`, `background-color 0.25s cubic-bezier(0.165, 0.84, 0.44, 1)`, `background-color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1)`, `color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1)`, `background-color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1)`, `color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1)`, `opacity 0.75s cubic-bezier(0.165, 0.84, 0.44, 1)`, `width 0.3s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1)`, `transform 0.75s cubic-bezier(0.23, 1, 0.32, 1)`

- home: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `0.2s`, `opacity 0.75s cubic-bezier(0.23, 1, 0.32, 1)`, `background-color 0.25s cubic-bezier(0.165, 0.84, 0.44, 1)`, `background-color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1)`, `color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1)`, `background-color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1)`, `color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1)`, `opacity 0.75s cubic-bezier(0.165, 0.84, 0.44, 1)`, `width 0.3s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1)`

- login: `unset`, `transform 0.3s ease-out, width 0.3s ease-out`, `box-shadow 0.2s`, `opacity 0.6s ease-out`, `color 0.2s`, `0.2s`, `opacity 0.2s`, `box-shadow 0.2s ease-in-out, opacity 0.5s`, `box-shadow 0.2s ease-in-out, opacity 0.2s`, `opacity var(--slide-fade-duration) ease-in-out`

- pricing: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `0.2s`, `background-color 0.25s cubic-bezier(0.165, 0.84, 0.44, 1)`, `background-color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1)`, `color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1)`, `background-color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1)`, `color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1)`, `border-radius 0.75s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `transform 0.5s cubic-bezier(0.165, 0.84, 0.44, 1)`

## Reduced motion

- home (`.btn_new, .link_new, .header_new a` under prefers-reduced-motion): transition `none`, animation `none 0s ease 0s 1 normal none running`, html scroll-behavior `auto`
