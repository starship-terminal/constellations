# Equals component measurements

Computed styles read from Equals' public surface on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the three public sites — the equals.com marketing pages (home, pricing, a use-case page), the go.equals.com sign-in card and the docs.equals.com Mintlify docs in both its themes (dark from a prefers-color-scheme context, never the theme menu) — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened` is the resting state after the component's own local toggle (the "Use cases" mega-menu, a pricing FAQ label, the mobile hamburger).

## Components

### Marketing chrome

#### mkt-header

Marketing header. The top bar: wordmark, Home / Use cases / Pricing / About, "Get a demo" capture and the "Sign in" link.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #faf9f5 |
| Box shadow | none |
| Outline | none |
| Font | Unica77 18px/24px 400 |
| Letter spacing | -0.09px |
| Colour | #000000 |
| Text node | button.header__menu-trigger: Unica77 14px/20px 400, #000000 |
| Transition | none |
| Icon | 108 x 22, colour #0000ee |
| Painted layers | header.header 1440.0x52.0 bg #faf9f5; div.header__menu.header__menu--use-cases 624.0x354.8 bg #ffffff r 12px shadow #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.05 0px 2px 8px -2px, #000000 @ 0.15 0px 8px 24px -4px; form.email-capture-group.get-a-demo 0.0x0.0 bg #ffffff r 50px shadow #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.05 0px 2px 8px -2px, #000000 @ 0.14 0px 2px 10px -4px; button.email-capture-group__button.button 0.0x0.0 bg #b074ce image linear-gradient(#000000 @ 0 75%, #000000 @ 0.04 100%) r 60px; form.email-capture-group.email-capture-group--small 220.0x34.0 bg #ffffff r 50px shadow #000000 @ 0.18 0px 0px 0px 0.5px; button.email-capture-group__button.button 97.0x26.0 bg #b074ce image linear-gradient(#000000 @ 0 75%, #000000 @ 0.04 100%) r 60px |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The Equals wordmark at the left of the header.

Page: home. Selector: `header logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 108 x 21 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Unica77 18px/24px 400 |
| Letter spacing | -0.09px |
| Colour | #0000ee |
| Transition | none |
| Cursor | pointer |
| Icon | 108 x 22, colour #0000ee |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### mkt-nav-link

Nav link. A marketing header link (Pricing/About); measured, never followed.

Page: home. Selector: `header .header__nav-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 42.38 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Unica77 14px/20px 400 | = | = | = |
| Letter spacing | -0.09px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | text-decoration 0.1s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.header__nav-link 42.4x16.0 outline 1px auto #101010 offset 1px | = |

Crops: `mkt-nav-link-default.png`, `mkt-nav-link-hover.png`, `mkt-nav-link-focus-visible.png`, `mkt-nav-link-pressed.png`.

#### mkt-menu-trigger

Use-cases menu trigger. The header "Use cases" button; opened to reveal the mega-menu of use-case links (a local toggle, its links never followed).

Page: home. Selector: `button.header__menu-trigger`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 65 x 20 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = | = |
| Font | Unica77 14px/20px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Transition | text-decoration 0.1s ease-out | = | = | = | = |
| Cursor | default | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | button.header__menu-trigger 65.0x20.0 outline 1px auto #101010 offset 0px | = | = |

Crops: `mkt-menu-trigger-default.png`, `mkt-menu-trigger-hover.png`, `mkt-menu-trigger-focus-visible.png`, `mkt-menu-trigger-pressed.png`, `mkt-menu-trigger-opened.png`.

#### mkt-menu

Use-cases mega-menu. The dropdown the "Use cases" trigger opens: category labels and use-case links.

Page: home. Selector: `.header__menu--use-cases`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 633.76 x 360.31 |
| Padding | 14px 10px |
| Border | none |
| Radius | 12px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.05 0px 2px 8px -2px, #000000 @ 0.15 0px 8px 24px -4px |
| Outline | none |
| Font | Unica77 14px/20px 400 |
| Letter spacing | -0.09px |
| Colour | #000000 |
| Text node | p.header__use-cases-category.text-color-muted: Unica77 14px/20px 400, #000000 @ 0.6, ls -0.09px |
| Transition | opacity, transform 0.16s, 0.16s cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1) delay 0s, 0s |
| Transform | matrix(0.995323, 0, 0, 0.995323, 0, -0.935443) |
| Opacity | 0.766139 |
| Painted layers | div.header__menu.header__menu--use-cases 633.8x360.3 bg #ffffff r 12px shadow #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.05 0px 2px 8px -2px, #000000 @ 0.15 0px 8px 24px -4px |
| How | at rest |

Crops: `mkt-menu-default.png`.

#### mkt-menu-item

Mega-menu link. One use-case link inside the open mega-menu; measured, never followed.

Page: home. Selector: `.header__use-case-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 204.62 x 27.87 | 205.58 x 28 | 205.58 x 28 | 205.58 x 28 |
| Padding | 4px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | #000000 @ 0.05 | #000000 @ 0.05 | #000000 @ 0.05 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | 1px auto #101010 offset 1px |
| Font | Unica77 14px/20px 400 | = | = | = |
| Letter spacing | -0.09px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 3 up div.header__menu.header__menu--use-cases bg #ffffff shadow #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.05 0px 2px 8px -2px, #000000 @ 0.15 0px 8px 24px -4px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.header__use-case-link 205.6x28.0 bg #000000 @ 0.05 r 6px | a.header__use-case-link 205.6x28.0 bg #000000 @ 0.05 r 6px outline 1px auto #101010 offset 1px | a.header__use-case-link 205.6x28.0 bg #000000 @ 0.05 r 6px outline 1px auto #101010 offset 1px |

Crops: `mkt-menu-item-default.png`, `mkt-menu-item-hover.png`, `mkt-menu-item-focus-visible.png`, `mkt-menu-item-pressed.png`.

#### mkt-signin

Sign-in link. The header "Sign in" link to go.equals.com; measured, never followed.

Page: home. Selector: `header Sign in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 41.38 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Unica77 14px/20px 400 | = | = | = |
| Letter spacing | -0.09px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | text-decoration 0.1s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.header__nav-link 41.4x20.0 outline 1px auto #101010 offset 1px | = |

Crops: `mkt-signin-default.png`, `mkt-signin-hover.png`, `mkt-signin-focus-visible.png`, `mkt-signin-pressed.png`.

### Home hero and sections

#### hero-h1

Hero headline. "What’s after Excel?" — the Serrif Condensed display on the hero.

Page: home. Selector: `h1.home__hero-h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1050 x 110 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Serrif Condensed 110px/110px 400 |
| Letter spacing | -2.2px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-sub

Hero sub. The lede under the headline.

Page: home. Selector: `hero sub`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 618 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Unica77 24px/32px 400 |
| Letter spacing | -0.09px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-email

Demo email field. The "Enter your work email" capture under the hero copy; focused and typed into then cleared — never submitted.

Page: home. Selector: `.home__hero-cta .email-capture-group__input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 380 x 56 | = | = |
| Padding | 18px 150px 18px 28px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Unica77 16px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000 @ 0.6, opacity 1 | = | = |
| Ancestor paint | 1 up form.email-capture-group.get-a-demo bg #ffffff shadow #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.05 0px 2px 8px -2px, #000000 @ 0.14 0px 2px 10px -4px | 1 up form.email-capture-group.get-a-demo bg #ffffff shadow #b074ce 0px 0px 0px 1px, #b074ce @ 0.1 0px 0px 0px 3px, #000000 @ 0.05 0px 2px 8px -2px, #000000 @ 0.14 0px 2px 10px -4px | 1 up form.email-capture-group.get-a-demo bg #ffffff shadow #b074ce 0px 0px 0px 1px, #b074ce @ 0.1 0px 0px 0px 3px, #000000 @ 0.05 0px 2px 8px -2px, #000000 @ 0.14 0px 2px 10px -4px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `hero-email-default.png`, `hero-email-focused.png`, `hero-email-filled.png`.

#### hero-cta

Get-a-demo button. The black "Get a demo" pill on the email capture; measured never pressed (it submits the capture).

Page: home. Selector: `.home__hero-cta .email-capture-group__button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 118 x 44 | = | = | = |
| Padding | 12px 18px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 60px | = | = | = |
| Background | #b074ce | #9b66b5 | = | #9b66b5 |
| Background image | linear-gradient(#000000 @ 0 75%, #000000 @ 0.04 100%) | = | = | = |
| Box shadow | none | = | = | #000000 @ 0.17 0px 1px 3px 0px inset |
| Outline | none | = | = | = |
| Font | Unica77 16px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color 0.15s ease-out | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, -22) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.email-capture-group__button.button 118.0x44.0 bg #b074ce image linear-gradient(#000000 @ 0 75%, #000000 @ 0.04 100%) r 60px | button.email-capture-group__button.button 118.0x44.0 bg #9b66b5 image linear-gradient(#000000 @ 0 75%, #000000 @ 0.04 100%) r 60px | = | button.email-capture-group__button.button 118.0x44.0 bg #9b66b5 image linear-gradient(#000000 @ 0 75%, #000000 @ 0.04 100%) r 60px shadow #000000 @ 0.17 0px 1px 3px 0px inset |
| Ancestor paint | 1 up form.email-capture-group.get-a-demo bg #ffffff shadow #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.05 0px 2px 8px -2px, #000000 @ 0.14 0px 2px 10px -4px | 1 up form.email-capture-group.get-a-demo bg #ffffff shadow #000000 @ 0.18 0px 0px 0px 0.5px, #000000 @ 0.05 0px 2px 8px -2px, #000000 @ 0.14 0px 2px 10px -4px | 1 up form.email-capture-group.get-a-demo bg #ffffff shadow #b074ce 0px 0px 0px 1px, #b074ce @ 0.1 0px 0px 0px 3px, #000000 @ 0.05 0px 2px 8px -2px, #000000 @ 0.14 0px 2px 10px -4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### section-label

Section label. The numbered eyebrow label over a marketing section ("1. TRUST"), coloured by the page’s label-- theme.

Page: home. Selector: `p.section__label`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1266 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aeonik Fono 14px/24px 400 |
| Letter spacing | 0.28px |
| Colour | #ff3716 |
| Transition | none |
| How | at rest |

Crops: `section-label-default.png`.

#### section-h2

Section heading. A marketing section heading ("A single source of truth…").

Page: home. Selector: `h2.section__h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1266 x 100 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Serrif Condensed 48px/50px 400 |
| Letter spacing | -0.48px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

#### build-tab

Persona tab. A "Build …" persona tab in the AI-demo section (the active one carries build-tab--active); measured, never pressed.

Page: home. Selector: `.build-tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 402 x 129 | = | = | = |
| Padding | 16px 0px 32px 0px | = | = | = |
| Gap | 16px | = | = | = |
| Border | T: none; R: none; B: 1px solid #000000 @ 0.1; L: none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Unica77 18px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | p.text-small.text-color-muted: Unica77 14px/16px 400, #000000 @ 0.6 | = | = | = |
| Transition | opacity 0.2s ease-out | = | = | = |
| Opacity | 0.55 | 0.85 | = | 0.85 |
| Cursor | pointer | = | = | = |
| Painted layers | button.build-tab 402.0x129.0 border B:1px solid #000000 @ 0.1; span.build-tab__progress 0.0x1.0 bg #000000 | = | button.build-tab 402.0x129.0 border B:1px solid #000000 @ 0.1 outline 1px auto #101010 offset 0px; span.build-tab__progress 0.0x1.0 bg #000000 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `build-tab-default.png`, `build-tab-hover.png`, `build-tab-focus-visible.png`, `build-tab-pressed.png`.

#### uc-h1

Use-case headline. "ARR Dashboard" — the use-case page’s display heading.

Page: usecase. Selector: `use-case h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1266 x 110 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Serrif Condensed 110px/110px 400 |
| Letter spacing | -2.2px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `uc-h1-default.png`.

#### uc-lede

Use-case lede. The first paragraph under the use-case hero.

Page: usecase. Selector: `use-case first paragraph`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 633 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Unica77 24px/32px 400 |
| Letter spacing | -0.09px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `uc-lede-default.png`.

#### uc-email

Demo email field (use-case). The same email capture on a use-case page; focused and typed into then cleared — never submitted.

Page: usecase. Selector: `main .email-capture-group__input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 380 x 56 | = | = |
| Padding | 18px 150px 18px 28px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Unica77 16px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000 @ 0.6, opacity 1 | = | = |
| Ancestor paint | 1 up form.email-capture-group.get-a-demo bg #ffffff shadow #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.05 0px 2px 8px -2px, #000000 @ 0.14 0px 2px 10px -4px | 1 up form.email-capture-group.get-a-demo bg #ffffff shadow #b074ce 0px 0px 0px 1px, #b074ce @ 0.1 0px 0px 0px 3px, #000000 @ 0.05 0px 2px 8px -2px, #000000 @ 0.14 0px 2px 10px -4px | 1 up form.email-capture-group.get-a-demo bg #ffffff shadow #b074ce 0px 0px 0px 1px, #b074ce @ 0.1 0px 0px 0px 3px, #000000 @ 0.05 0px 2px 8px -2px, #000000 @ 0.14 0px 2px 10px -4px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `uc-email-default.png`, `uc-email-focused.png`, `uc-email-filled.png`.

### Workbook mockup

#### wb-mockup

Workbook mockup. The in-page spreadsheet demo: toolbar, formula bar, sheet tabs and cells — a public demo, not the app.

Page: home. Selector: `.mockup-workbook`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 980 x 640 |
| Padding | 0px |
| Border | none |
| Radius | 12px |
| Background | #fcfcfc |
| Box shadow | #262626 @ 0.08 0px 0px 0px 1px, #000000 @ 0.2 0px 2px 8px -4px |
| Outline | none |
| Font | Unica77 18px/24px 400 |
| Letter spacing | 0.18px |
| Colour | #000000 |
| Text node | span.mockup-window-bar__address-url: Unica77 12px/24px 400, #575757, ls 0.18px |
| Transition | none |
| Cursor | default |
| Icon | 12 x 12, colour #8d8d8d |
| Painted layers | div.mockup.mockup-workbook 980.0x640.0 bg #fcfcfc r 12px shadow #262626 @ 0.08 0px 0px 0px 1px, #000000 @ 0.2 0px 2px 8px -4px; div.mockup-window-bar.mockup-window-bar--address 980.0x40.0 border B:1px solid #000000 @ 0.06; span.mockup-window-bar__light.mockup-window-bar__light--close 12.0x12.0 bg #d8d7d4 r 50%; span.mockup-window-bar__light.mockup-window-bar__light--minimise 12.0x12.0 bg #d8d7d4 r 50%; span.mockup-window-bar__light.mockup-window-bar__light--zoom 12.0x12.0 bg #d8d7d4 r 50%; span.mockup-window-bar__address 320.0x26.0 bg #000000 @ 0.04 r 13px |
| How | at rest |

Crops: `wb-mockup-default.png`.

#### wb-toolbar-button

Mock toolbar button. A toolbar icon button inside the workbook mockup; measured, never pressed.

Page: home. Selector: `.mockup-workbook__toolbar-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 4px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Unica77 18px/24px 400 | = | - | = |
| Letter spacing | 0.18px | = | - | = |
| Colour | #262626 | = | - | = |
| Transition | none | = | - | = |
| Cursor | default | = | - | = |
| Icon | 16 x 16, colour #262626 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `wb-toolbar-button-default.png`, `wb-toolbar-button-hover.png`, `wb-toolbar-button-pressed.png`.

#### wb-sheet-tab

Sheet tab. A workbook sheet tab inside the mockup; measured, never pressed.

Page: home. Selector: `.mockup-workbook__sheet-tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 92.63 x 32 | = | - | = |
| Padding | 0px 8px | = | - | = |
| Gap | 6px | = | - | = |
| Border | T: 1px solid #d4d4d4; R: none; B: none; L: 1px solid #d4d4d4 | = | - | = |
| Radius | 0px | = | - | = |
| Background | #fafafa | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Unica77 11px/14px 400 | = | - | = |
| Letter spacing | 0.18px | = | - | = |
| Colour | #737373 | = | - | = |
| Text node | span.mockup-workbook__sheet-name: Unica77 11px/14px 400, #737373, ls 0.18px | = | - | = |
| Transition | none | = | - | = |
| Cursor | default | = | - | = |
| Icon | 11 x 11, colour #737373 | = | - | = |
| Painted layers | div.mockup-workbook__sheet-tab 92.6x32.0 bg #fafafa border T:1px solid #d4d4d4 / L:1px solid #d4d4d4 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `wb-sheet-tab-default.png`, `wb-sheet-tab-hover.png`, `wb-sheet-tab-pressed.png`.

#### wb-cell

Workbook cell. A label cell in the workbook mockup ("Build Summary"); the mockup cycles demo slides, so the reading is whichever cell is painted — its value cells animate as the demo types.

Page: home. Selector: `.mockup-workbook__cell--label`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 131 x 21 |
| Padding | 0px 4px |
| Border | T: none; R: 1px solid #ededed; B: 1px solid #ededed; L: none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Unica77 12px/20px 500 |
| Letter spacing | 0.18px |
| Colour | #262626 |
| Text node | span.mockup-workbook__cell-value: Unica77 12px/20px 500, #262626, ls 0.18px |
| Transition | none |
| Cursor | default |
| Painted layers | div.mockup-workbook__cell.mockup-workbook__cell--label 131.0x21.0 bg #ffffff border R:1px solid #ededed / B:1px solid #ededed |
| How | at rest |

Crops: `wb-cell-default.png`.

### Pricing

#### plan-card

Plan card. An Essential pricing card: plan name, price, "Get a demo" CTA and feature list on the cream page.

Page: pricing. Selector: `.pricing__plan`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 421.33 x 568.8 |
| Padding | 32px |
| Border | none |
| Radius | 0px |
| Background | #faf9f5 |
| Box shadow | none |
| Outline | none |
| Font | Unica77 18px/24px 400 |
| Letter spacing | -0.09px |
| Colour | #000000 |
| Text node | p.plan-name.essential: Unica77 18px/22px 400, #ff3716, ls -0.18px |
| Transition | none |
| Icon | 16 x 16, colour #000000 |
| Painted layers | div.pricing__plan 421.3x568.8 bg #faf9f5; form.email-capture-group.get-a-demo 357.3x42.0 bg #ffffff r 50px shadow #000000 @ 0.15 0px 0px 0px 0.5px; button.email-capture-group__button.button 97.0x30.0 bg #ff3716 image linear-gradient(#000000 @ 0 75%, #000000 @ 0.04 100%) r 60px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-name

Plan name. The "Essential" plan label.

Page: pricing. Selector: `.plan-name`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 357.33 x 22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Unica77 18px/22px 400 |
| Letter spacing | -0.18px |
| Colour | #ff3716 |
| Transition | none |
| Ancestor paint | 1 up div.pricing__plan bg #faf9f5 |
| How | at rest |

Crops: `plan-name-default.png`.

#### plan-price

Plan price. The "$24k /year" price line — the suffix is a smaller muted span.

Page: pricing. Selector: `.plan-price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 357.33 x 52.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Serrif Condensed 48px/52.8px 400 |
| Letter spacing | -0.4px |
| Colour | #000000 |
| Transition | none |
| Ancestor paint | 1 up div.pricing__plan bg #faf9f5 |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. The card’s "Get a demo" action on its accent--amber background; measured never pressed.

Page: pricing. Selector: `.plan-cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 357.33 x 42 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Unica77 18px/24px 400 | = | = | = |
| Letter spacing | -0.09px | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | button.email-capture-group__button.button: Unica77 14px/18px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Painted layers | form.email-capture-group.get-a-demo 357.3x42.0 bg #ffffff r 50px shadow #000000 @ 0.15 0px 0px 0px 0.5px; button.email-capture-group__button.button 97.0x30.0 bg #ff3716 image linear-gradient(#000000 @ 0 75%, #000000 @ 0.04 100%) r 60px | form.email-capture-group.get-a-demo 357.3x42.0 bg #ffffff r 50px shadow #000000 @ 0.18 0px 0px 0px 0.5px; button.email-capture-group__button.button 97.0x30.0 bg #ff3716 image linear-gradient(#000000 @ 0 75%, #000000 @ 0.04 100%) r 60px | form.email-capture-group.get-a-demo 357.3x42.0 bg #ffffff r 50px shadow #ff3716 0px 0px 0px 1px, #ff3716 @ 0.1 0px 0px 0px 3px; button.email-capture-group__button.button 97.0x30.0 bg #ff3716 image linear-gradient(#000000 @ 0 75%, #000000 @ 0.04 100%) r 60px | = |
| Ancestor paint | 1 up div.pricing__plan bg #faf9f5 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-cta-orchid

Plan CTA (orchid). The Business card’s CTA on the accent--orchid background; each plan carries its own accent colour.

Page: pricing. Selector: `.plan-cta.accent--orchid`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 356.33 x 42 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Unica77 18px/24px 400 | = | = | = |
| Letter spacing | -0.09px | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | button.email-capture-group__button.button: Unica77 14px/18px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Painted layers | form.email-capture-group.get-a-demo 356.3x42.0 bg #ffffff r 50px shadow #000000 @ 0.15 0px 0px 0px 0.5px; button.email-capture-group__button.button 97.0x30.0 bg #b074ce image linear-gradient(#000000 @ 0 75%, #000000 @ 0.04 100%) r 60px | form.email-capture-group.get-a-demo 356.3x42.0 bg #ffffff r 50px shadow #000000 @ 0.18 0px 0px 0px 0.5px; button.email-capture-group__button.button 97.0x30.0 bg #b074ce image linear-gradient(#000000 @ 0 75%, #000000 @ 0.04 100%) r 60px | form.email-capture-group.get-a-demo 356.3x42.0 bg #ffffff r 50px shadow #b074ce 0px 0px 0px 1px, #b074ce @ 0.1 0px 0px 0px 3px; button.email-capture-group__button.button 97.0x30.0 bg #b074ce image linear-gradient(#000000 @ 0 75%, #000000 @ 0.04 100%) r 60px | = |
| Ancestor paint | 1 up div.pricing__plan bg #faf9f5 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-orchid-default.png`, `plan-cta-orchid-hover.png`, `plan-cta-orchid-focus-visible.png`, `plan-cta-orchid-pressed.png`.

#### plan-feature

Plan feature row. A feature line inside the plan card ("Unlimited seats").

Page: pricing. Selector: `.plan-features li`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 357.33 x 38 |
| Padding | 8px 0px |
| Gap | 10px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Unica77 16px/22px 400 |
| Letter spacing | -0.09px |
| Colour | #000000 |
| Text node | span: Unica77 16px/22px 400, #000000, ls -0.09px |
| Transition | none |
| Icon | 16 x 16, colour #000000 |
| How | at rest |

Crops: `plan-feature-default.png`.

#### faq

FAQ item. A pricing FAQ row (a checkbox accordion); opened by clicking its label — a local toggle, never a form post.

Page: pricing. Selector: `.faq`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 1266 x 230 | = |
| Padding | 0px | = |
| Border | T: 1px solid #000000 @ 0.1; R: none; B: 1px solid #000000 @ 0.1; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Unica77 18px/24px 400 | = |
| Letter spacing | -0.09px | = |
| Colour | #000000 | = |
| Text node | p.text-large: Unica77 24px/32px 400, #000000, ls -0.09px | = |
| Transition | none | = |
| Icon | 0 x 0, colour #000000 | = |
| Painted layers | div.faq.faq--first 1266.0x230.0 border T:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 | = |
| How | at rest | own toggle |

Crops: `faq-default.png`, `faq-opened.png`.

#### faq-question

FAQ question. The question label of the first FAQ item.

Page: pricing. Selector: `label.faq__question`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1266 x 72 |
| Padding | 24px 0px 16px 0px |
| Gap | 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Unica77 18px/24px 400 |
| Letter spacing | -0.09px |
| Colour | #000000 |
| Text node | p.text-large: Unica77 24px/32px 400, #000000, ls -0.09px |
| Transition | none |
| Cursor | pointer |
| Icon | 0 x 0, colour #000000 |
| How | at rest |

Crops: `faq-question-default.png`.

### Sign in (go.equals.com)

#### signin-card

Sign-in card. The whole "Sign in to Equals" card — heading, subheading, the email form and the footer line.

Page: signin. Selector: `.SignIn`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 300 x 226 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | neue-haas-unica 12px/12px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.SignIn__Heading: Serrif Condensed 30px/39px 400, #000000, ls -0.6px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, -20) |
| Cursor | default |
| Painted layers | input.SignIn__Input 300.0x30.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; input.SignIn__Button 300.0x27.0 bg #7c3aed r 8px |
| Ancestor paint | 1 up div.SignIn__Page bg #ffffff |
| How | at rest |

Crops: `signin-card-default.png`.

#### signin-heading

Sign-in heading. "Sign in to Equals".

Page: signin. Selector: `.SignIn__Heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 300 x 39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Serrif Condensed 30px/39px 400 |
| Letter spacing | -0.6px |
| Colour | #000000 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `signin-heading-default.png`.

#### signin-sub

Sign-in subheading. "Enter your email below to login to your account".

Page: signin. Selector: `.SignIn__Subheading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 300 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | neue-haas-unica 12px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `signin-sub-default.png`.

#### signin-email

Sign-in email field. The "Enter your email" input; focused and typed into then cleared — never submitted.

Page: signin. Selector: `.SignIn__Input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 300 x 30 | = | = |
| Padding | 6px 8px | = | = |
| Border | 1px solid #000000 @ 0 | 1px solid #7c3aed | 1px solid #7c3aed |
| Radius | 8px | = | = |
| Background | #f5f5f5 | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | neue-haas-unica 12px/16px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #262626 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #a3a3a3, opacity 1 | = | = |
| Painted layers | input.SignIn__Input 300.0x30.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | input.SignIn__Input 300.0x30.0 bg #f5f5f5 border T:1px solid #7c3aed / R:1px solid #7c3aed / B:1px solid #7c3aed / L:1px solid #7c3aed r 8px | input.SignIn__Input 300.0x30.0 bg #f5f5f5 border T:1px solid #7c3aed / R:1px solid #7c3aed / B:1px solid #7c3aed / L:1px solid #7c3aed r 8px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `signin-email-default.png`, `signin-email-focused.png`, `signin-email-filled.png`.

#### signin-continue

Continue button. The form’s "Continue" submit; its states were measured but it was never clicked — nothing was submitted.

Page: signin. Selector: `.SignIn__Button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 300 x 27 | = | = | = |
| Padding | 6px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #7c3aed | #6d28d9 | = | #6d28d9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | neue-haas-unica 12px/15px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color 0.15s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Placeholder | #ffffff, opacity 1 | = | = | = |
| Painted layers | input.SignIn__Button 300.0x27.0 bg #7c3aed r 8px | input.SignIn__Button 300.0x27.0 bg #6d28d9 r 8px | input.SignIn__Button 300.0x27.0 bg #7c3aed r 8px outline 1px auto #101010 offset 0px | input.SignIn__Button 300.0x27.0 bg #6d28d9 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-continue-default.png`, `signin-continue-hover.png`, `signin-continue-focus-visible.png`, `signin-continue-pressed.png`.

#### signin-footer

Sign-in footer link. "Don’t have an account? Request a demo" — the footer copy and link; measured, never followed.

Page: signin. Selector: `.SignIn__Footer`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 300 x 16 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | neue-haas-unica 12px/16px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #737373 | = | - | = |
| Transition | none | = | - | = |
| Cursor | default | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `signin-footer-default.png`, `signin-footer-hover.png`, `signin-footer-pressed.png`.

### Docs (docs.equals.com) (light)

#### docs-sidebar

Docs sidebar. The docs left rail: logo, search, theme menu and the nav tree.

Page: docs. Selector: `docs sidebar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 288 x 804 |
| Padding | 0px |
| Border | T: none; R: 1px solid #f1eff5; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #737176 |
| Text node | span: Inter 12px/16px 600, #1a181d, ls 0.12px |
| Transition | transform, translate, scale, rotate 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 20 x 8, colour #a2a0a5, fill #000000 |
| Painted layers | nav.hidden.sticky 288.0x804.0 border R:1px solid #f1eff5; a.group.flex 267.0x32.0 bg #7839e5 @ 0.1 r 12px; div.sidebar-nav-group-divider.h-px 259.0x1.0 bg #f1eff5; div.sidebar-nav-group-divider.h-px 259.0x1.0 bg #f1eff5; div.sidebar-nav-group-divider.h-px 259.0x1.0 bg #f1eff5; div.sidebar-nav-group-divider.h-px 259.0x1.0 bg #f1eff5 |
| How | at rest |

Crops: `docs-sidebar-default.png`.

#### docs-logo

Docs logo. The Equals wordmark at the top of the docs rail.

Page: docs. Selector: `docs logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 117.89 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #737176 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `docs-logo-default.png`.

#### docs-search

Search button. The "Search…" field-styled button in the docs rail; measured, never opened.

Page: docs. Selector: `#search-bar-entry`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 264.33 x 36 | = | = | = |
| Padding | 0px 12px 0px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #0d0b11 @ 0.03 | #0d0b11 @ 0.1 | = | #0d0b11 @ 0.1 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a2a0a5 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #535156 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #535156 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | 1px auto #7839e5 offset 0px | = |
| Font | Inter 14px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #737176 | = | = | = |
| Text node | div.truncate.min-w-0: Inter 14px/24px 400, #737176 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #424045, fill #000000 | 16 x 16, colour #29272c, fill #000000 | = | 16 x 16, colour #29272c, fill #000000 |
| Painted layers | button.group/search.flex 264.3x36.0 bg #0d0b11 @ 0.03 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a2a0a5 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.group/search.flex 264.3x36.0 bg #0d0b11 @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #535156 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.group/search.flex 264.3x36.0 bg #0d0b11 @ 0.03 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a2a0a5 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #7839e5 offset 0px | button.group/search.flex 264.3x36.0 bg #0d0b11 @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #535156 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-search-default.png`, `docs-search-hover.png`, `docs-search-focus-visible.png`, `docs-search-pressed.png`.

#### docs-theme-btn

Theme menu button. The docs theme menu button; measured, never opened (the dark capture used a prefers-color-scheme context instead).

Page: docs. Selector: `#theme-preference-menu-trigger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 30 x 30 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #29272c @ 0.04 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #7839e5 offset 0px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0b11 @ 0.5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 16, colour #535156, fill #000000 | 14 x 16, colour #29272c, fill #000000 | = | 14 x 16, colour #29272c, fill #000000 |
| Painted layers | button.group.disabled:pointer-events-none 30.0x30.0 bg #29272c @ 0.04 r 9999px | = | button.group.disabled:pointer-events-none 30.0x30.0 bg #29272c @ 0.04 r 9999px outline 1px auto #7839e5 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-theme-btn-default.png`, `docs-theme-btn-hover.png`, `docs-theme-btn-focus-visible.png`, `docs-theme-btn-pressed.png`.

#### docs-nav-item

Nav item. A docs sidebar link; measured, never followed.

Page: docs. Selector: `sidebar nav link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 267 x 32 | = | = | = |
| Padding | 6px 12px 6px 28px | = | = | = |
| Gap | normal 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #7839e5 @ 0.1 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #7839e5 offset -2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #7839e5 | = | = | = |
| Text node | span.min-w-0.max-w-full: Inter 14px/20px 400, #7839e5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.flex 267.0x32.0 bg #7839e5 @ 0.1 r 12px | = | a.group.flex 267.0x32.0 bg #7839e5 @ 0.1 r 12px outline 1px auto #7839e5 offset -2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-nav-item-default.png`, `docs-nav-item-hover.png`, `docs-nav-item-focus-visible.png`, `docs-nav-item-pressed.png`.

#### docs-assistant

Assistant button. The "Ask AI" assistant entry in the docs chrome; measured at rest, never opened — nothing was sent.

Page: docs. Selector: `#assistant-entry`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 171 x 36 | = | = | = |
| Padding | 0px 14px 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #0d0b11 @ 0.03 | #0d0b11 @ 0.1 | = | #0d0b11 @ 0.1 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a2a0a5 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #535156 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #535156 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | 1px auto #7839e5 offset 0px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #737176 | = | = | = |
| Text node | span.text-sm.text-gray-500: Inter 14px/20px 400, #737176 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #424045, fill #000000 | 16 x 16, colour #29272c, fill #000000 | = | 16 x 16, colour #29272c, fill #000000 |
| Painted layers | button.group/ai.flex-none 171.0x36.0 bg #0d0b11 @ 0.03 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a2a0a5 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.group/ai.flex-none 171.0x36.0 bg #0d0b11 @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #535156 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.group/ai.flex-none 171.0x36.0 bg #0d0b11 @ 0.03 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a2a0a5 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #7839e5 offset 0px | button.group/ai.flex-none 171.0x36.0 bg #0d0b11 @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #535156 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-assistant-default.png`, `docs-assistant-hover.png`, `docs-assistant-focus-visible.png`, `docs-assistant-pressed.png`.

#### docs-h1

Page heading. The doc page’s h1.

Page: docs. Selector: `docs h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 168.89 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 36px/40px 600 |
| Letter spacing | 0.36px |
| Colour | #1a181d |
| Transition | none |
| How | at rest |

Crops: `docs-h1-default.png`.

#### docs-para

Body paragraph. A body paragraph in the doc.

Page: docs. Selector: `main p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 632 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28px 400 |
| Letter spacing | normal |
| Colour | #424045 |
| Transition | none |
| How | at rest |

Crops: `docs-para-default.png`.

#### docs-link

Body link. A link inside the doc body; measured, never followed.

Page: docs. Selector: `main a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 264 x 32 | = | 268 x 32 | = |
| Padding | 4px 0px 4px 16px | = | 4px 0px 4px 20px | = |
| Border | T: none; R: none; B: none; L: 1px solid #7839e5 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #7839e5 offset -2px | = |
| Font | Inter 14px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #7839e5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.text-primary.dark:text-primary-light 264.0x32.0 border L:1px solid #7839e5 | = | a.text-primary.dark:text-primary-light 268.0x32.0 border L:1px solid #7839e5 outline 1px auto #7839e5 offset -2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-link-default.png`, `docs-link-hover.png`, `docs-link-focus-visible.png`, `docs-link-pressed.png`.

#### docs-code

Code block. A code block or inline code span in the doc.

Page: docs. Selector: `main pre/code`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 128 x 20 |
| Padding | 2px 8px |
| Border | none |
| Radius | 6px |
| Background | #f1eff5 @ 0.5 |
| Box shadow | none |
| Outline | none |
| Font | Paper Mono 14px/21px 500 |
| Letter spacing | normal |
| Colour | oklch(0.21 0.034 264.665) |
| Transition | none |
| Painted layers | code 128.0x20.0 bg #f1eff5 @ 0.5 r 6px |
| How | at rest |

Crops: `docs-code-default.png`.

### Docs (docs.equals.com) (dark)

#### d-docs-sidebar

Docs sidebar. The docs left rail: logo, search, theme menu and the nav tree.

Page: docsdark. Selector: `docs sidebar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 288 x 804 |
| Padding | 0px |
| Border | T: none; R: 1px solid #ffffff @ 0.1; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #a2a0a5 |
| Text node | span: Inter 12px/16px 600, #e2e0e5, ls 0.12px |
| Transition | transform, translate, scale, rotate 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 20 x 8, colour #535156, fill #000000 |
| Painted layers | nav.hidden.sticky 288.0x804.0 border R:1px solid #ffffff @ 0.1; a.group.flex 267.0x32.0 bg #7839e5 @ 0.1 r 12px; div.sidebar-nav-group-divider.h-px 259.0x1.0 bg #ffffff @ 0.1; div.sidebar-nav-group-divider.h-px 259.0x1.0 bg #ffffff @ 0.1; div.sidebar-nav-group-divider.h-px 259.0x1.0 bg #ffffff @ 0.1; div.sidebar-nav-group-divider.h-px 259.0x1.0 bg #ffffff @ 0.1 |
| How | at rest |

Crops: `d-docs-sidebar-default.png`.

#### d-docs-logo

Docs logo. The Equals wordmark at the top of the docs rail.

Page: docsdark. Selector: `docs logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 117.89 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #a2a0a5 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `d-docs-logo-default.png`.

#### d-docs-search

Search button. The "Search…" field-styled button in the docs rail; measured, never opened.

Page: docsdark. Selector: `#search-bar-entry`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 264.33 x 36 | = | = | = |
| Padding | 0px 12px 0px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff @ 0.03 | #ffffff @ 0.1 | = | #ffffff @ 0.1 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #535156 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #737176 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #737176 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | 1px auto #7839e5 offset 0px | = |
| Font | Inter 14px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.5 | = | = | = |
| Text node | div.truncate.min-w-0: Inter 14px/24px 400, #ffffff @ 0.5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #a2a0a5, fill #000000 | 16 x 16, colour #e2e0e5, fill #000000 | = | 16 x 16, colour #e2e0e5, fill #000000 |
| Painted layers | button.group/search.flex 264.3x36.0 bg #ffffff @ 0.03 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #535156 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.group/search.flex 264.3x36.0 bg #ffffff @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #737176 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.group/search.flex 264.3x36.0 bg #ffffff @ 0.03 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #535156 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #7839e5 offset 0px | button.group/search.flex 264.3x36.0 bg #ffffff @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #737176 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `d-docs-search-default.png`, `d-docs-search-hover.png`, `d-docs-search-focus-visible.png`, `d-docs-search-pressed.png`.

#### d-docs-theme-btn

Theme menu button. The docs theme menu button; measured, never opened (the dark capture used a prefers-color-scheme context instead).

Page: docsdark. Selector: `#theme-preference-menu-trigger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 30 x 30 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff @ 0.1 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #7839e5 offset 0px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 16, colour #d1cfd5, fill #000000 | 14 x 16, colour #f1eff5, fill #000000 | = | 14 x 16, colour #f1eff5, fill #000000 |
| Painted layers | button.group.disabled:pointer-events-none 30.0x30.0 bg #ffffff @ 0.1 r 9999px | = | button.group.disabled:pointer-events-none 30.0x30.0 bg #ffffff @ 0.1 r 9999px outline 1px auto #7839e5 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `d-docs-theme-btn-default.png`, `d-docs-theme-btn-hover.png`, `d-docs-theme-btn-focus-visible.png`, `d-docs-theme-btn-pressed.png`.

#### d-docs-nav-item

Nav item. A docs sidebar link; measured, never followed.

Page: docsdark. Selector: `sidebar nav link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 267 x 32 | = | = | = |
| Padding | 6px 12px 6px 28px | = | = | = |
| Gap | normal 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #7839e5 @ 0.1 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #7839e5 offset -2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #7839e5 | = | = | = |
| Text node | span.min-w-0.max-w-full: Inter 14px/20px 400, #7839e5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.flex 267.0x32.0 bg #7839e5 @ 0.1 r 12px | = | a.group.flex 267.0x32.0 bg #7839e5 @ 0.1 r 12px outline 1px auto #7839e5 offset -2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `d-docs-nav-item-default.png`, `d-docs-nav-item-hover.png`, `d-docs-nav-item-focus-visible.png`, `d-docs-nav-item-pressed.png`.

#### d-docs-assistant

Assistant button. The "Ask AI" assistant entry in the docs chrome; measured at rest, never opened — nothing was sent.

Page: docsdark. Selector: `#assistant-entry`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 171 x 36 | = | = | = |
| Padding | 0px 14px 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff @ 0.03 | #ffffff @ 0.1 | = | #ffffff @ 0.1 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #535156 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #737176 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #737176 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | 1px auto #7839e5 offset 0px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #a2a0a5 | = | = | = |
| Text node | span.text-sm.text-gray-500: Inter 14px/20px 400, #ffffff @ 0.5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #a2a0a5, fill #000000 | 16 x 16, colour #e2e0e5, fill #000000 | = | 16 x 16, colour #e2e0e5, fill #000000 |
| Painted layers | button.group/ai.flex-none 171.0x36.0 bg #ffffff @ 0.03 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #535156 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.group/ai.flex-none 171.0x36.0 bg #ffffff @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #737176 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.group/ai.flex-none 171.0x36.0 bg #ffffff @ 0.03 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #535156 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #7839e5 offset 0px | button.group/ai.flex-none 171.0x36.0 bg #ffffff @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #737176 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `d-docs-assistant-default.png`, `d-docs-assistant-hover.png`, `d-docs-assistant-focus-visible.png`, `d-docs-assistant-pressed.png`.

#### d-docs-h1

Page heading. The doc page’s h1.

Page: docsdark. Selector: `docs h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 168.89 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 36px/40px 600 |
| Letter spacing | 0.36px |
| Colour | #e2e0e5 |
| Transition | none |
| How | at rest |

Crops: `d-docs-h1-default.png`.

#### d-docs-para

Body paragraph. A body paragraph in the doc.

Page: docsdark. Selector: `main p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 632 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28px 400 |
| Letter spacing | normal |
| Colour | #a2a0a5 |
| Transition | none |
| How | at rest |

Crops: `d-docs-para-default.png`.

#### d-docs-link

Body link. A link inside the doc body; measured, never followed.

Page: docsdark. Selector: `main a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 264 x 32 | = | 268 x 32 | = |
| Padding | 4px 0px 4px 16px | = | 4px 0px 4px 20px | = |
| Border | T: none; R: none; B: none; L: 1px solid #7839e5 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #7839e5 offset -2px | = |
| Font | Inter 14px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #7839e5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.text-primary.dark:text-primary-light 264.0x32.0 border L:1px solid #7839e5 | = | a.text-primary.dark:text-primary-light 268.0x32.0 border L:1px solid #7839e5 outline 1px auto #7839e5 offset -2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `d-docs-link-default.png`, `d-docs-link-hover.png`, `d-docs-link-focus-visible.png`, `d-docs-link-pressed.png`.

#### d-docs-code

Code block. A code block or inline code span in the doc.

Page: docsdark. Selector: `main pre/code`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 128 x 20 |
| Padding | 2px 8px |
| Border | none |
| Radius | 6px |
| Background | #ffffff @ 0.05 |
| Box shadow | none |
| Outline | none |
| Font | Paper Mono 14px/21px 500 |
| Letter spacing | normal |
| Colour | #e2e0e5 |
| Transition | none |
| Painted layers | code 128.0x20.0 bg #ffffff @ 0.05 r 6px |
| How | at rest |

Crops: `d-docs-code-default.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The top bar at 390: wordmark, hamburger and "Get a demo".

Page: mobile. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 53 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #000000 @ 0.15; L: none |
| Radius | 0px |
| Background | #faf9f5 |
| Box shadow | none |
| Outline | none |
| Font | Unica77 18px/24px 400 |
| Letter spacing | -0.09px |
| Colour | #000000 |
| Transition | none |
| Icon | 108 x 22, colour #0000ee |
| Painted layers | header.header 390.0x53.0 bg #faf9f5 border B:1px solid #000000 @ 0.15; span.header__hamburger-line 16.0x1.5 bg #000000; span.header__hamburger-line 16.0x1.5 bg #000000; form.email-capture-group.get-a-demo 0.0x0.0 bg #ffffff r 50px shadow #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.05 0px 2px 8px -2px, #000000 @ 0.14 0px 2px 10px -4px; button.email-capture-group__button.button 0.0x0.0 bg #b074ce image linear-gradient(#000000 @ 0 75%, #000000 @ 0.04 100%) r 60px; form.email-capture-group.email-capture-group--small 0.0x0.0 bg #ffffff r 50px shadow #000000 @ 0.18 0px 0px 0px 0.5px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-hamburger

Hamburger. The mobile nav toggle (a label over a hidden checkbox); opened to reveal the drawer — a local toggle, its links never followed.

Page: mobile. Selector: `label.header__mobile-nav-toggle`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | - | = | = |
| Padding | 0px | = | - | = | = |
| Border | none | = | - | = | = |
| Radius | 0px | = | - | = | = |
| Background | transparent | = | - | = | = |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | Unica77 18px/24px 400 | = | - | = | = |
| Letter spacing | -0.09px | = | - | = | = |
| Colour | #000000 | = | - | = | = |
| Transition | none | = | - | = | = |
| Cursor | pointer | = | - | = | = |
| Painted layers | span.header__hamburger-line 16.0x1.5 bg #000000; span.header__hamburger-line 16.0x1.5 bg #000000 | = | - | = | span.header__hamburger-line 12.4x12.4 bg #000000; span.header__hamburger-line 12.4x12.4 bg #000000 |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | own toggle |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `m-hamburger-default.png`, `m-hamburger-hover.png`, `m-hamburger-pressed.png`, `m-hamburger-opened.png`.

#### m-drawer

Mobile nav drawer. The nav the hamburger opens.

Page: mobile. Selector: `mobile nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 52 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Unica77 18px/24px 400 |
| Letter spacing | -0.09px |
| Colour | #000000 |
| Text node | a.header__nav-link: Unica77 24px/30px 400, #000000, ls -0.09px |
| Transition | none |
| Icon | 108 x 22, colour #0000ee |
| Painted layers | span.header__hamburger-line 12.4x12.4 bg #000000; span.header__hamburger-line 12.4x12.4 bg #000000; ul.header__nav 390.0x792.0 bg #faf9f5; form.email-capture-group.get-a-demo 358.0x52.0 bg #ffffff r 50px shadow #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.05 0px 2px 8px -2px, #000000 @ 0.14 0px 2px 10px -4px; button.email-capture-group__button.button 118.0x40.0 bg #b074ce image linear-gradient(#000000 @ 0 75%, #000000 @ 0.04 100%) r 60px; form.email-capture-group.email-capture-group--small 0.0x0.0 bg #ffffff r 50px shadow #000000 @ 0.18 0px 0px 0px 0.5px |
| Ancestor paint | 1 up header.header bg #faf9f5 |
| How | at rest |

Crops: `m-drawer-default.png`.

#### m-hero-h1

Hero headline (mobile). "What’s after Excel?" at 390 wide.

Page: mobile. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 980 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Serrif Condensed 48px/48px 400 |
| Letter spacing | -0.96px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-email

Demo email field (mobile). The email capture at 390; focused and typed into then cleared — never submitted.

Page: mobile. Selector: `.email-capture-group__input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 358 x 52 | = | = |
| Padding | 16px 28px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Unica77 16px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000 @ 0.6, opacity 1 | = | = |
| Ancestor paint | 1 up form.email-capture-group.get-a-demo bg #ffffff shadow #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0.05 0px 2px 8px -2px, #000000 @ 0.14 0px 2px 10px -4px | 1 up form.email-capture-group.get-a-demo bg #ffffff shadow #b074ce 0px 0px 0px 1px, #b074ce @ 0.1 0px 0px 0px 3px, #000000 @ 0.05 0px 2px 8px -2px, #000000 @ 0.14 0px 2px 10px -4px | 1 up form.email-capture-group.get-a-demo bg #ffffff shadow #b074ce 0px 0px 0px 1px, #b074ce @ 0.1 0px 0px 0px 3px, #000000 @ 0.05 0px 2px 8px -2px, #000000 @ 0.14 0px 2px 10px -4px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `m-email-default.png`, `m-email-focused.png`, `m-email-filled.png`.

## Transitions declared in the readable stylesheets

equals.com and go.equals.com serve their stylesheets same-origin and docs.equals.com reads through the CSSOM as well, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- docs: `top 0.16s cubic-bezier(0.25, 0.75, 0.2, 1)`, `width var(--duration-long) var(--timing),height var(--duration-long) var(--timing),background var(--duration-short) ease,scale var(--duration-short) var(--timing)`, `none`, `border-color 0.3s`, `filter 0.35s, opacity 0.35s`, `opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1)`, `opacity var(--lightbox-pull-snap-duration,var(--lightbox-vt-duration)) var(--lightbox-pull-snap-easing,var(--lightbox-vt-root-easing))`, `opacity var(--lightbox-vt-duration) var(--lightbox-vt-root-easing)`, `opacity 0.2s, visibility linear`, `opacity 0.2s, visibility linear 0.2s`, `opacity 0.2s`

- docsdark: `top 0.16s cubic-bezier(0.25, 0.75, 0.2, 1)`, `width var(--duration-long) var(--timing),height var(--duration-long) var(--timing),background var(--duration-short) ease,scale var(--duration-short) var(--timing)`, `none`, `border-color 0.3s`, `filter 0.35s, opacity 0.35s`, `opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1)`, `opacity var(--lightbox-pull-snap-duration,var(--lightbox-vt-duration)) var(--lightbox-pull-snap-easing,var(--lightbox-vt-root-easing))`, `opacity var(--lightbox-vt-duration) var(--lightbox-vt-root-easing)`, `opacity 0.2s, visibility linear`, `opacity 0.2s, visibility linear 0.2s`, `opacity 0.2s`

- home: `box-shadow 0.2s ease-in-out, border 0.2s ease-in-out`, `box-shadow 0.1s ease-out`, `width 0.15s ease-out`, `background-color 0.15s ease-out`, `opacity 0.1s ease-out`, `text-decoration 0.1s ease-out`, `opacity 0.16s cubic-bezier(0.16, 1, 0.3, 1), transform 0.16s cubic-bezier(0.16, 1, 0.3, 1)`, `transform 0.2s ease-out`, `opacity 0.5s ease-in-out`, `transform 0.3s ease-in-out`, `background-color 0.1s`, `opacity var(--slack-stream-reveal-dur) ease-out,transform var(--slack-stream-reveal-dur) var(--slack-stream-ease)`

- pricing: `box-shadow 0.2s ease-in-out, border 0.2s ease-in-out`, `box-shadow 0.1s ease-out`, `width 0.15s ease-out`, `background-color 0.15s ease-out`, `opacity 0.1s ease-out`, `text-decoration 0.1s ease-out`, `opacity 0.16s cubic-bezier(0.16, 1, 0.3, 1), transform 0.16s cubic-bezier(0.16, 1, 0.3, 1)`, `transform 0.2s ease-out`, `opacity 0.5s ease-in-out`, `transform 0.3s ease-in-out`, `background-color 0.1s`, `opacity var(--slack-stream-reveal-dur) ease-out,transform var(--slack-stream-reveal-dur) var(--slack-stream-ease)`

- signin: none

- usecase: `box-shadow 0.2s ease-in-out, border 0.2s ease-in-out`, `box-shadow 0.1s ease-out`, `width 0.15s ease-out`, `background-color 0.15s ease-out`, `opacity 0.1s ease-out`, `text-decoration 0.1s ease-out`, `opacity 0.16s cubic-bezier(0.16, 1, 0.3, 1), transform 0.16s cubic-bezier(0.16, 1, 0.3, 1)`, `transform 0.2s ease-out`, `opacity 0.5s ease-in-out`, `transform 0.3s ease-in-out`, `background-color 0.1s`, `opacity var(--slack-stream-reveal-dur) ease-out,transform var(--slack-stream-reveal-dur) var(--slack-stream-ease)`
