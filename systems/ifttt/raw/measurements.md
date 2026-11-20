# Component measurements

Computed styles read from ifttt.com and ifttt.ai on 2026-11-18 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `opened`, `selected`, `toggled` and the rest are resting states reached by the page or by a UI toggle (the Share button's own modal, the billing switch, the featured tabs, the hamburger). Nothing was typed, sent, searched, shared, bought or signed into.

## Components

### Site chrome

#### site-header

Site header. header.unified-header: the IFTTT.ai wordmark, the search field, Explore / Plans links, "Log in" (outlined) and "Get started" (filled) — .dark.on-color over the dark heroes.

Page: explore. Selector: `header.unified-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 99 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #111111 |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 18px/18px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | a.nav-link.link-menu: Museo Sans Rounded 20px/22px 900, #ffffff |
| Transition | color 0.5s ease |
| Icon | 118.8 x 24.11, colour #111111 |
| Painted layers | header.unified-header.dark 1440.0x99.0 bg #111111; input.ifttt-search-input 400.0x48.0 bg #111111 border T:2px solid #ffffff @ 0.3 / R:2px solid #ffffff @ 0.3 / B:2px solid #ffffff @ 0.3 / L:2px solid #ffffff @ 0.3 r 32px; section.universal-search-helper 400.0x496.0 bg #ffffff r 8px shadow #000000 @ 0.14 0px 0px 10px 0px; div.recent-search-icon 40.0x40.0 bg #0099ff r 8px; div.recent-search-icon 40.0x40.0 bg #000000 r 8px; div.recent-search-icon 40.0x40.0 bg #ff0000 r 8px |
| Ancestor paint | 1 up body.explore-body.index-action bg #111111 |
| How | resting state |

Crops: `site-header-default.png`.

#### nav-logo

IFTTT.ai wordmark. The logo link home: the IFTTT.ai mark as inline SVG.

Page: explore. Selector: `a.logo.logo-ifttt-ai`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 118.8 x 24.11 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 18px/18px 700 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| Cursor | pointer |
| Icon | 118.8 x 24.11, colour #111111 |
| How | resting state |

Crops: `nav-logo-default.png`.

#### nav-search

Header search field. input.ifttt-search-input "Search for Applets, services, etc." — measured and focused, never queried.

Page: explore. Selector: `input.ifttt-search-input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 400 x 48 | = |
| Padding | 12px 44px | = |
| Border | 2px solid #ffffff @ 0.3 | 2px solid #ffffff |
| Radius | 32px | = |
| Background | #111111 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Museo Sans Rounded 18px/23.4px 700 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #eeeeee, opacity 1 | #999999, opacity 1 |
| Painted layers | input.ifttt-search-input 400.0x48.0 bg #111111 border T:2px solid #ffffff @ 0.3 / R:2px solid #ffffff @ 0.3 / B:2px solid #ffffff @ 0.3 / L:2px solid #ffffff @ 0.3 r 32px | input.ifttt-search-input 400.0x48.0 bg #111111 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 32px |
| How | resting state | the field clicked into |

Crops: `nav-search-default.png`.

#### nav-link

Nav link. A primary nav link ("Explore") — a.nav-link.link-menu.

Page: explore. Selector: `a.nav-link`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 71 x 22 | = | - |
| Padding | 0px | = | - |
| Border | none | = | - |
| Radius | 0px | = | - |
| Background | transparent | = | - |
| Box shadow | none | = | - |
| Outline | none | = | - |
| Font | Museo Sans Rounded 20px/22px 900 | = | - |
| Letter spacing | normal | = | - |
| Colour | #ffffff | = | - |
| Transition | none | = | - |
| Cursor | pointer | = | - |
| How | resting state | mouse hover over the element | - |
| Skipped | - | = | focus failed: keyboard focus did not reach the element |

Crops: `nav-link-default.png`.

#### nav-login

"Log in" button. a.sign-in.button-tertiary.button-outlined — the outlined pill; measured, never followed (it leads to sign-in).

Page: explore. Selector: `a.sign-in.button-tertiary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 115 x 54 | = | = | = |
| Padding | 0px 28px | = | = | = |
| Border | none | = | = | = |
| Radius | 64px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #ffffff 0px 0px 0px 2px inset | = | = | = |
| Outline | none | = | = | = |
| Font | Museo Sans Rounded 20px/22px 900 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.sign-in.button-tertiary 115.0x54.0 r 64px shadow #ffffff 0px 0px 0px 2px inset | = | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-signup

"Get started" button. a.button-tertiary.sign-up — the filled near-black pill in the header; measured, never followed (it leads to /join).

Page: explore. Selector: `a.sign-up.button-tertiary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 162 x 54 | = | = | = |
| Padding | 0px 28px | = | = | = |
| Border | none | = | = | = |
| Radius | 64px | = | = | = |
| Background | #ffffff | #eeeeee | #eeeeee | #eeeeee |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Museo Sans Rounded 20px/22px 900 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #111111 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button-tertiary.button-on-color 162.0x54.0 bg #ffffff r 64px | a.button-tertiary.button-on-color 162.0x54.0 bg #eeeeee r 64px | a.button-tertiary.button-on-color 162.0x54.0 bg #eeeeee r 64px | a.button-tertiary.button-on-color 162.0x54.0 bg #eeeeee r 64px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |
| Opacity | - | 0.8 | = | = |

Crops: `nav-signup-default.png`, `nav-signup-hover.png`, `nav-signup-focus-visible.png`, `nav-signup-pressed.png`.

#### site-footer

Site footer. The page footer: link columns, the app-store badges and the social icons.

Page: explore. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 851.91 |
| Padding | 48px 48px 64px 48px |
| Border | T: 1px solid #ffffff @ 0.3; R: none; B: none; L: none |
| Radius | 0px |
| Background | #111111 |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 18px/21.6px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.pro-upsell-heading: Museo Sans Rounded 34px/37.4px 900, #111111 |
| Transition | none |
| Icon | 88.97 x 24, colour #111111 |
| Painted layers | footer.site-footer.ifttt_next_bucket 1440.0x851.9 bg #111111 border T:1px solid #ffffff @ 0.3; a.pro-upsell.pro-ad 1344.0x143.0 bg #01b6ff r 32px; div.pro-upsell-text 568.0x143.0 bg #ffffff; div.button-secondary.button-on-color 324.0x79.0 bg #ffffff r 64px; a.social-icon 48.0x48.0 bg #ffffff @ 0.1 r 50%; a.social-icon 48.0x48.0 bg #ffffff @ 0.1 r 50% |
| Ancestor paint | 1 up body.explore-body.index-action bg #111111 |
| How | resting state |

Crops: none.

#### footer-link

Footer link. A link inside the footer columns.

Page: explore. Selector: `footer a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1344 x 143 | = |
| Padding | 32px | = |
| Gap | 48px | = |
| Border | none | = |
| Radius | 32px | = |
| Background | #01b6ff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Museo Sans Rounded 18px/21.6px 500 | = |
| Letter spacing | normal | = |
| Colour | #111111 | = |
| Text node | span.pro-upsell-heading: Museo Sans Rounded 34px/37.4px 900, #111111 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 88.97 x 24, colour #111111 | = |
| Painted layers | a.pro-upsell.pro-ad 1344.0x143.0 bg #01b6ff r 32px; div.pro-upsell-text 568.0x143.0 bg #ffffff; div.button-secondary.button-on-color 324.0x79.0 bg #ffffff r 64px | = |
| Ancestor paint | 1 up footer.site-footer.ifttt_next_bucket bg #111111 | = |
| How | resting state | mouse hover over the element |

Crops: `footer-link-default.png`, `footer-link-hover.png`.

### Home

#### hero-headline

Hero headline. The home hero h1 "The easiest way to automate anything" — Museo Sans Rounded 900.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1084 x 158.66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 79.3296px/79.3296px 900 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| How | resting state |

Crops: `hero-headline-default.png`.

#### hero-prompt

"Describe what you'd like to build" field. textarea.prompt-hero-input — the AI prompt box the hero is built around. focused is the field clicked into; nothing is typed or submitted.

Page: home. Selector: `textarea.prompt-hero-input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 628 x 78 | = |
| Padding | 8px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Museo Sans Rounded 16px/20.8px 700 | = |
| Letter spacing | normal | = |
| Colour | #111111 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #111111 @ 0.4, opacity 1 | = |
| Ancestor paint | 1 up div.prompt-hero-field bg #ffffff | = |
| How | resting state | the field clicked into |

Crops: `hero-prompt-default.png`, `hero-prompt-focused.png`.

#### hero-submit

"Start building" button. button.button-primary.prompt-hero-submit — the big black pill under the prompt. Measured, never pressed (it submits the prompt).

Page: home. Selector: `button.prompt-hero-submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 348 x 101 | = | = | = |
| Padding | 0px 64px | = | = | = |
| Border | none | = | = | = |
| Radius | 64px | = | = | = |
| Background | #111111 | = | #111111 @ 0.6 | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Museo Sans Rounded 34px/37.4px 900 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.button-primary.prompt-hero-submit 348.0x101.0 bg #111111 r 64px | = | button.button-primary.prompt-hero-submit 348.0x101.0 bg #111111 @ 0.6 r 64px | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |
| Opacity | - | 0.8 | = | = |

Crops: `hero-submit-default.png`, `hero-submit-hover.png`, `hero-submit-focus-visible.png`, `hero-submit-pressed.png`.

#### featured-tab

Featured category tab. A featured-Applets category tab (button.featured-tab). "selected" is its own activation — a local UI toggle, restored to Popular after.

Page: home. Selector: `button.featured-tab`. States: default, hover, selected.

| Property | default | hover | selected |
|---|---|---|---|
| Size (w x h) | 142 x 48 | = | = |
| Padding | 11px 19px | = | = |
| Border | 1px solid #111111 @ 0.1 | = | 1px solid #111111 |
| Radius | 8px | = | = |
| Background | #111111 @ 0.05 | #111111 @ 0.1 | #111111 |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Museo Sans Rounded 18px/24px 700 | = | = |
| Letter spacing | normal | = | = |
| Colour | #111111 | = | #ffffff |
| Transition | background-color 0.2s ease | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.featured-tab 142.0x48.0 bg #111111 @ 0.05 border T:1px solid #111111 @ 0.1 / R:1px solid #111111 @ 0.1 / B:1px solid #111111 @ 0.1 / L:1px solid #111111 @ 0.1 r 8px | button.featured-tab 142.0x48.0 bg #111111 @ 0.1 border T:1px solid #111111 @ 0.1 / R:1px solid #111111 @ 0.1 / B:1px solid #111111 @ 0.1 / L:1px solid #111111 @ 0.1 r 8px | button.featured-tab.active 142.0x48.0 bg #111111 border T:1px solid #111111 / R:1px solid #111111 / B:1px solid #111111 / L:1px solid #111111 r 8px |
| How | resting state | mouse hover over the element | the tab's own activation |

Crops: `featured-tab-default.png`, `featured-tab-hover.png`, `featured-tab-selected.png`.

#### featured-tab-active

Featured tab, active. The resting "Popular" tab — the selected pill state.

Page: home. Selector: `button.featured-tab.active`. States: default.

Selector missed the element. The saved element is the Smart home tab (text "Smart home", classes "featured-tab active"), left selected by the featured-tab reading. It is not the resting Popular tab. The style is kept on featured-tab's selected state, which is that same reading. Not republished as the Popular default.

#### service-chip

Service icon chip. One floating service icon in the hero automation canvas — the rounded-square brand tiles that drift across the hero.

Page: home. Selector: `img, a, div`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 48 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 12px |
| Background | #111111 |
| Background image | url(…) |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 18px/21.6px 500 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.integrations-card__service-icon 48.0x48.0 bg #111111 r 12px |
| Ancestor paint | 1 up div.integrations-card__item bg #111111 @ 0.05 |
| How | resting state |

Crops: `service-chip-default.png`.

#### secondary-cta

Secondary CTA. "Join today" / "Explore all Applets" — a.button-secondary, the large outlined action. Measured, never followed (it leads to /join or /explore).

Page: home. Selector: `a.button-secondary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 222 x 79 | = | = | = |
| Padding | 0px 40px | = | = | = |
| Border | none | = | = | = |
| Radius | 64px | = | = | = |
| Background | #111111 | = | #111111 @ 0.6 | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Museo Sans Rounded 28px/30.8px 900 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button-secondary.how-it-works-cta 222.0x79.0 bg #111111 r 64px | = | a.button-secondary.how-it-works-cta 222.0x79.0 bg #111111 @ 0.6 r 64px | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |
| Opacity | - | 0.8 | = | = |

Crops: `secondary-cta-default.png`, `secondary-cta-hover.png`, `secondary-cta-focus-visible.png`, `secondary-cta-pressed.png`.

#### section-heading

Section heading. A home section heading (an h2 in the modules below the fold).

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 548 x 100 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 50px/50px 900 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| How | resting state |

Crops: `section-heading-default.png`.

### Explore

#### applet-card

Applet card. A gallery applet card (a.applet-card-body inside li.web-applet-card): the tile with service icons, title, author and use count.

Page: explore. Selector: `a.applet-card-body`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 432 x 296.19 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 24px | = |
| Background | #1db954 | = |
| Box shadow | #000000 @ 0.24 0px 1.5px 6px 0px | = |
| Outline | none | = |
| Font | Museo Sans Rounded 18px/21.6px 500 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | span: Museo Sans Rounded 26.7812px/29.4594px 900, #ffffff | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | a.applet-card-body.spec-prefetch 432.0x296.2 bg #1db954 r 24px shadow #000000 @ 0.24 0px 1.5px 6px 0px | = |
| How | resting state | mouse hover over the element |

Crops: `applet-card-default.png`, `applet-card-hover.png`.

#### explore-hero

Explore hero (dark). The dark "Automate X with Y" hero band on /explore: near-black ground, the prompt card and the cycling service names.

Page: explore. Selector: `section, div[class*="hero"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 579.36 |
| Padding | 108px 48px |
| Gap | 40px |
| Border | none |
| Radius | 0px |
| Background | #111111 |
| Background image | url(…) |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 18px/21.6px 500 |
| Letter spacing | normal |
| Colour | #111111 |
| Text node | span.explore-hero-title-lead: Museo Sans Rounded 32px/41.6px 700, #ffffff |
| Transition | none |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | section.explore-prompt-hero.explore-prompt-hero-ifttt-ai 1440.0x579.4 bg #111111; span.explore-hero-service-icon 40.0x40.0 bg #ec7505 r 12px; span.explore-hero-service-icon 40.0x40.0 bg #e60023 r 12px; span.explore-hero-service-icon 40.0x40.0 bg #0099ff r 12px; span.explore-hero-service-icon 40.0x40.0 bg #0062fe r 12px; span.explore-hero-service-icon 40.0x40.0 bg #ff0000 r 12px |
| How | resting state |

Crops: `explore-hero-default.png`.

#### explore-prompt

Explore prompt field. textarea.prompt-hero-input inside the dark hero card — "tell us what you'd like to automate". focused only; never submitted.

Page: explore. Selector: `textarea.prompt-hero-input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 628 x 58 | = |
| Padding | 8px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Museo Sans Rounded 16px/20.8px 700 | = |
| Letter spacing | normal | = |
| Colour | #111111 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #111111 @ 0.4, opacity 1 | = |
| Ancestor paint | 1 up div.prompt-hero-field bg #ffffff | = |
| How | resting state | the field clicked into |

Crops: `explore-prompt-default.png`, `explore-prompt-focused.png`.

#### explore-prompt-card

Prompt card. The white card holding the prompt field and its "Start building" submit inside the dark hero.

Page: explore. Selector: `[class*="prompt"]`. States: default.

Selector missed the element. The saved element is section.explore-prompt-hero (1440 x 579, background #111111), the dark hero, not the white prompt card. No card-sized white ancestor is in the saved paint layers, so the card's size, radius and shadow are unmeasured. Not republished as the prompt card.

#### explore-service-chip

Service chip in hero. a.explore-hero-service — a service name chip ("Pinterest") in the "Automate X with Y" cycler.

Page: explore. Selector: `a.explore-hero-service`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 181 x 42 | = |
| Padding | 0px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Museo Sans Rounded 32px/41.6px 700 | = |
| Letter spacing | normal | = |
| Colour | #ee831e | = |
| Transition | none | = |
| Transform | matrix(1, 0, 0, 1, 0, -42) | = |
| Opacity | 0 | = |
| Cursor | pointer | = |
| Painted layers | span.explore-hero-service-icon 40.0x40.0 bg #ec7505 r 12px | = |
| How | resting state | mouse hover over the element |

Crops: `explore-service-chip-hover.png`.

#### example-prompt-card

"Try these examples" card. One translucent suggestion card under the prompt ("If there's a new Tweet with keyword, add to sheets.").

Page: explore. Selector: `a, div`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 660 x 111.36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 18px/21.6px 500 |
| Letter spacing | normal |
| Colour | #111111 |
| Text node | p: Museo Sans Rounded 16px/20.8px 900, #ffffff @ 0.6 |
| Transition | none |
| Painted layers | button 214.7x86.6 bg #ffffff @ 0.1 r 10px; button 214.7x86.6 bg #ffffff @ 0.1 r 10px; button 214.7x86.6 bg #ffffff @ 0.1 r 10px |
| Ancestor paint | 1 up section.explore-prompt-hero.explore-prompt-hero-ifttt-ai bg #111111 |
| How | resting state |

Crops: none.

#### explore-tab

Explore gallery tab. The All / Applets / Services / Stories gallery tabs (a.text-h5). "active" is the current tab.

Page: explore. Selector: `a.text-h5`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 85 x 52.8 | = |
| Padding | 16px 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Museo Sans Rounded 16px/20.8px 900 | = |
| Letter spacing | normal | = |
| Colour | #111111 @ 0.6 | #111111 |
| Transition | none | = |
| Cursor | pointer | = |
| How | resting state | mouse hover over the element |

Crops: `explore-tab-default.png`, `explore-tab-hover.png`.

#### explore-tab-active

Explore gallery tab, active. The resting "All" tab — the active state (a.text-h5.active).

Page: explore. Selector: `a.text-h5.active`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 44 x 52.8 |
| Padding | 16px 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 16px/20.8px 900 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| ::after | 44px x 2px, absolute, bg #111111, radius 0px |
| Painted layers | a::after.text-h5.active 44pxx2px bg #111111 |
| How | resting state |

Crops: `explore-tab-active-default.png`.

#### service-card

Service card. a.service-card — a service tile in the gallery grid: brand icon over name on white.

Page: explore. Selector: `a.service-card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 432 x 296.19 | = |
| Padding | 32px 24px | = |
| Gap | 40px | = |
| Border | none | = |
| Radius | 24px | = |
| Background | #14223d | = |
| Box shadow | #000000 @ 0.24 0px 1.5px 6px 0px | = |
| Outline | none | = |
| Font | Museo Sans Rounded 18px/21.6px 500 | = |
| Letter spacing | normal | = |
| Colour | #111111 | = |
| Text node | span.service-card-title: Museo Sans Rounded 20px/22px 900, #ffffff | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | a.service-card.spec-prefetch 432.0x296.2 bg #14223d r 24px shadow #000000 @ 0.24 0px 1.5px 6px 0px | = |
| How | resting state | mouse hover over the element |

Crops: `service-card-default.png`, `service-card-hover.png`.

#### story-card

Story card. a.story-box — a story tile ("Put AI to work for you") in the gallery.

Page: explore. Selector: `a.story-box`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 432 x 296.19 |
| Padding | 0px |
| Border | none |
| Radius | 24px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 18px/21.6px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.text-h5: Museo Sans Rounded 16px/20.8px 900, #ffffff |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.overlay 432.0x296.2 image linear-gradient(#1084fa @ 0 0%, #1084fa 50%) |
| How | resting state |

Crops: `story-card-default.png`.

#### gallery-search

"Search automations" field. The gallery's own search input (input.ifttt-search-input "Search automations"). Focused only; never queried.

Page: explore. Selector: `input[placeholder*="automations" i]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 432 x 55 | = |
| Padding | 16px 44px | = |
| Border | 2px solid #111111 @ 0.1 | 2px solid #111111 |
| Radius | 32px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Museo Sans Rounded 18px/23.4px 700 | = |
| Letter spacing | normal | = |
| Colour | #111111 @ 0.4 | #111111 |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #111111 @ 0.4, opacity 1 | #999999, opacity 1 |
| Painted layers | input.ifttt-search-input 432.0x55.0 bg #ffffff border T:2px solid #111111 @ 0.1 / R:2px solid #111111 @ 0.1 / B:2px solid #111111 @ 0.1 / L:2px solid #111111 @ 0.1 r 32px | input.ifttt-search-input 432.0x55.0 bg #ffffff border T:2px solid #111111 / R:2px solid #111111 / B:2px solid #111111 / L:2px solid #111111 r 32px |
| How | resting state | the field clicked into |

Crops: `gallery-search-default.png`, `gallery-search-focused.png`.

### Plans

#### billing-toggle

Monthly / Yearly switch. button.switch-field (role=switch) in the credits-plans-toggle — the billing-period control. "yearly"/"monthly" are its own presses, the repainted prices proof; restored to the default (Yearly).

Page: plans. Selector: `button.switch-field[role="switch"]`. States: default, hover, toggled.

| Property | default | hover | toggled |
|---|---|---|---|
| Size (w x h) | 48 x 32 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 16px | = | = |
| Background | #01b6ff | = | #111111 @ 0.4 |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Museo Sans Rounded 13.3333px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | background-color 0.12s ease-in-out | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.switch-field.switch-field-on 48.0x32.0 bg #01b6ff r 16px; span.switch-field-knob 28.0x28.0 bg #ffffff r 50% | = | button.switch-field 48.0x32.0 bg #111111 @ 0.4 r 16px; span.switch-field-knob 28.0x28.0 bg #ffffff r 50% |
| How | resting state | mouse hover over the element | the switch's own press (Yearly -> Monthly, then restored) |

Crops: `billing-toggle-default.png`, `billing-toggle-hover.png`, `billing-toggle-toggled.png`.

#### billing-toggle-wrap

Billing toggle with labels. div.credits-plans-toggle — Monthly | switch | Yearly + the "SAVE 30%" badge.

Page: plans. Selector: `div.credits-plans-toggle`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 193 x 56 |
| Padding | 4px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 18px/21.6px 500 |
| Letter spacing | normal |
| Colour | #111111 |
| Text node | span.credits-plans-toggle-label.is-active: Museo Sans Rounded 16px/20.8px 700, #111111 |
| Transition | none |
| Painted layers | button.switch-field 48.0x32.0 bg #111111 @ 0.4 r 16px; span.switch-field-knob 28.0x28.0 bg #ffffff r 50%; span.credits-plans-save 65.0x20.6 bg #0dd14e r 6px |
| How | resting state |

Crops: `billing-toggle-wrap-default.png`.

#### save-badge

"SAVE 30%" badge. The green discount badge beside the yearly label.

Page: plans. Selector: `span, div`. States: default.

Selector missed the element. The saved element is div.credits-plans-toggle (193 x 56, text "Monthly Yearly SAVE 30%"), the whole billing row. span.credits-plans-save appears only as a paint-layer size (65.0x20.6, bg rgb(13, 209, 78), radius 6px) with no computed style of its own, so the badge's fill, ink and type are unmeasured. Not republished as the badge.

#### plan-card

Plan card (Free). A pricing card: name, $ price, credits line, feature list with check icons and a "Get started" outline CTA.

Page: plans. Selector: `div, li`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 310 x 434.14 |
| Padding | 26px 22px 22px 22px |
| Gap | 32px |
| Border | 2px solid #111111 @ 0.1 |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 18px/21.6px 500 |
| Letter spacing | normal |
| Colour | #111111 |
| Text node | h2.credits-plan-card-name: Museo Sans Rounded 18px/normal 900, #111111 |
| Transition | none |
| Icon | 16 x 16, colour #111111 @ 0.7 |
| Painted layers | li.credits-plan-card 310.0x434.1 bg #ffffff border T:2px solid #111111 @ 0.1 / R:2px solid #111111 @ 0.1 / B:2px solid #111111 @ 0.1 / L:2px solid #111111 @ 0.1 r 16px; p.credits-plan-card-credits.body-medium 206.0x39.4 border T:2px solid #111111 @ 0.1 / R:2px solid #111111 @ 0.1 / B:2px solid #111111 @ 0.1 / L:2px solid #111111 @ 0.1 r 12px |
| How | resting state |

Crops: `plan-card-default.png`.

#### plan-card-recommended

Plan card, recommended (Pro). The highlighted Pro card — dark header, "RECOMMENDED" ribbon, filled "Get started" CTA.

Page: plans. Selector: `div, li`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 310 x 456.14 |
| Padding | 26px 22px 22px 22px |
| Gap | 32px |
| Border | T: 24px solid #111111; R: 2px solid #111111; B: 2px solid #111111; L: 2px solid #111111 |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 18px/21.6px 500 |
| Letter spacing | normal |
| Colour | #111111 |
| Text node | span.credits-plan-card-flag: Museo Sans Rounded 12px/15.6px 700, #ffffff @ 0.85 |
| Transition | none |
| Icon | 10 x 10, colour #ffffff @ 0.85 |
| Painted layers | li.credits-plan-card.credits-plan-card-recommended 310.0x456.1 bg #ffffff border T:24px solid #111111 / R:2px solid #111111 / B:2px solid #111111 / L:2px solid #111111 r 16px; p.credits-plan-card-credits.body-medium 218.0x39.4 border T:2px solid #111111 @ 0.1 / R:2px solid #111111 @ 0.1 / B:2px solid #111111 @ 0.1 / L:2px solid #111111 @ 0.1 r 12px; a.button-tertiary 262.0x54.0 bg #111111 r 64px |
| How | resting state |

Crops: `plan-card-recommended-default.png`.

#### plan-price

Plan price figure. The big "$0.00 / month" figure on a plan card — the display number style.

Page: plans. Selector: `span, div`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 135 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 50px/50px 900 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| How | resting state |

Crops: `plan-price-default.png`.

#### plan-feature

Plan feature row. A feature line inside a plan card ("All features unlocked") with its check icon.

Page: plans. Selector: `li`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 262 x 18.19 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 14px/18.2px 700 |
| Letter spacing | normal |
| Colour | #111111 @ 0.7 |
| Transition | none |
| Icon | 16 x 16, colour #111111 @ 0.7 |
| How | resting state |

Crops: `plan-feature-default.png`.

#### plan-cta

Plan "Get started" CTA. The outlined button on a plan card — measured, never followed (it leads to checkout).

Page: plans. Selector: `a.button-tertiary`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 262 x 54 | = | = |
| Padding | 0px 28px | = | = |
| Border | none | = | = |
| Radius | 64px | = | = |
| Background | transparent | #111111 @ 0.05 | = |
| Box shadow | #111111 0px 0px 0px 2px inset | = | = |
| Outline | none | = | = |
| Font | Museo Sans Rounded 20px/22px 900 | = | = |
| Letter spacing | normal | = | = |
| Colour | #111111 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Painted layers | a.button-tertiary.button-outlined 262.0x54.0 r 64px shadow #111111 0px 0px 0px 2px inset | a.button-tertiary.button-outlined 262.0x54.0 bg #111111 @ 0.05 r 64px shadow #111111 0px 0px 0px 2px inset | = |
| Ancestor paint | 1 up li.credits-plan-card bg #ffffff | = | = |
| How | resting state | mouse hover over the element | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-pressed.png`.

#### plan-cta-filled

Plan CTA on the recommended card. The filled "Get started" on the Pro card — measured, never followed.

Page: plans. Selector: `a.button-tertiary:not(.button-outlined)`. States: default, hover, pressed.

Selector missed the element. The saved element is a.button-tertiary.sign-up at y 22.5 (162 x 54), the header signup. The recommended card's filled CTA was not the element measured. Not republished as the plan CTA.

### Detail pages

#### back-button

Back button. The fixed "Back" pill on service/applet/connect pages — measured, never followed.

Page: connect. Selector: `a[class*="back-button"], a.button-with-icon`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 134 x 54 | = | = |
| Padding | 0px 28px | = | = |
| Gap | 8px | = | = |
| Border | none | = | = |
| Radius | 64px | = | = |
| Background | transparent | #ffffff @ 0.1 | = |
| Box shadow | #ffffff 0px 0px 0px 2px inset | = | = |
| Outline | none | = | = |
| Font | Museo Sans Rounded 20px/22px 900 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Text node | span.hide-on-xs: Museo Sans Rounded 20px/22px 900, #ffffff | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 24 x 24, colour #ffffff | = | = |
| Painted layers | a.button-tertiary.button-outlined 134.0x54.0 r 64px shadow #ffffff 0px 0px 0px 2px inset | a.button-tertiary.button-outlined 134.0x54.0 bg #ffffff @ 0.1 r 64px shadow #ffffff 0px 0px 0px 2px inset | = |
| How | resting state | mouse hover over the element | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `back-button-default.png`, `back-button-hover.png`, `back-button-pressed.png`.

#### share-button

Share button. button.modal-open "Share" — opens the site's own share modal. "opened" is its own press painting .modal; the modal is closed with its X after.

Page: connect. Selector: `button.modal-open`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 148.19 x 54 | = | 1440 x 900 |
| Padding | 0px 28px | = | 0px |
| Gap | 8px | = | - |
| Border | none | = | = |
| Radius | 64px | = | 0px |
| Background | transparent | #ffffff @ 0.1 | = |
| Box shadow | #ffffff 0px 0px 0px 2px inset | = | none |
| Outline | none | = | = |
| Font | Museo Sans Rounded 20px/22px 900 | = | Museo Sans Rounded 18px/21.6px 500 |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | #111111 |
| Text node | span.hide-on-xs: Museo Sans Rounded 20px/22px 900, #ffffff | = | h4.hide-on-xs: Museo Sans Rounded 20px/22px 900, #111111 |
| Transition | none | = | = |
| Cursor | pointer | = | - |
| Icon | 24 x 24, colour #ffffff | = | 21 x 21, colour #111111 |
| Painted layers | button.modal-open.button-tertiary 148.2x54.0 r 64px shadow #ffffff 0px 0px 0px 2px inset | button.modal-open.button-tertiary 148.2x54.0 bg #ffffff @ 0.1 r 64px shadow #ffffff 0px 0px 0px 2px inset | div.modal-background 1440.0x900.0 bg #000000 @ 0.5; div.modal-content 504.0x252.6 bg #ffffff border T:1px solid #000000 @ 0.05 / R:1px solid #000000 @ 0.05 / B:1px solid #000000 @ 0.05 / L:1px solid #000000 @ 0.05 r 8px shadow #000000 @ 0.25 0px 8px 16px 0px; input.share-url-input.hide-on-xs 418.0x55.0 bg #111111 @ 0.05 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 16px; button.copy.button 121.0x54.0 bg #111111 r 64px; input.share-url-input.hide-above-xs 0.0x0.0 bg #111111 @ 0.05 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 16px; button.copy.button 0.0x0.0 bg #111111 r 64px |
| How | resting state | mouse hover over the element | the Share button's own press (the share modal open; closed with its X after) |

Crops: `share-button-default.png`, `share-button-hover.png`, `share-button-opened.png`.

#### share-modal-copy

Share modal "Copy" button. The black Copy pill inside the share modal — measured inside the opened modal, never pressed (a clipboard side effect).

Page: connect. Selector: `.share-modal button, .share-modal a, .modal button, .modal a`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 121 x 54 |
| Padding | 0px 28px |
| Border | none |
| Radius | 64px |
| Background | #111111 |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 20px/22px 900 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| Painted layers | button.copy.button 121.0x54.0 bg #111111 r 64px |
| How | resting state |

Crops: `share-modal-copy-default.png`.

#### share-url-field

Share URL field. input.share-url-input — the read-only short-link field in the share modal.

Page: connect. Selector: `input.share-url-input`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 418 x 55 |
| Padding | 0px 16px |
| Border | 2px solid #000000 @ 0 |
| Radius | 16px |
| Background | #111111 @ 0.05 |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 18px/23.4px 700 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| Cursor | pointer |
| Placeholder | #111111, opacity 1 |
| Painted layers | input.share-url-input.hide-on-xs 418.0x55.0 bg #111111 @ 0.05 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 16px |
| Ancestor paint | 3 up div.modal-content bg #ffffff shadow #000000 @ 0.25 0px 8px 16px 0px |
| How | resting state |

Crops: `share-url-field-default.png`.

#### service-hero

Service / applet hero. The branded hero band on a detail page: service icons, the display headline and lede — dark on service and connect pages, the partner brand colour on applet pages.

Page: connect. Selector: `section, div`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1344 x 1466.25 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 18px/21.6px 500 |
| Letter spacing | normal |
| Colour | #111111 |
| Text node | h2: Museo Sans Rounded 34px/37.4px 900, #111111 |
| Transition | none |
| Painted layers | a.applet-card-body.spec-prefetch 432.0x330.8 bg #e4405f r 24px shadow #000000 @ 0.24 0px 1.5px 6px 0px; a.applet-card-body.spec-prefetch 432.0x330.8 bg #e4405f r 24px shadow #000000 @ 0.24 0px 1.5px 6px 0px; a.applet-card-body.spec-prefetch 432.0x330.8 bg #e4405f r 24px shadow #000000 @ 0.24 0px 1.5px 6px 0px; a.applet-card-body.spec-prefetch 432.0x330.8 bg #e4405f r 24px shadow #000000 @ 0.24 0px 1.5px 6px 0px; a.applet-card-body.spec-prefetch 432.0x330.8 bg #e4405f r 24px shadow #000000 @ 0.24 0px 1.5px 6px 0px; a.applet-card-body.spec-prefetch 432.0x330.8 bg #e4405f r 24px shadow #000000 @ 0.24 0px 1.5px 6px 0px |
| Ancestor paint | 1 up main.container.web bg #ffffff |
| How | resting state |

Crops: `service-hero-default.png`.

#### service-icon

Service icon. The service's rounded-square brand tile in a hero or card.

Page: connect. Selector: `img`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 110 x 110 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 18px/21.6px 500 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 1 up a.service-container bg #5865f2 shadow #ffffff @ 0.3 0px 0px 0px 2px inset |
| How | resting state |

Crops: `service-icon-default.png`.

#### get-started-today

"Get started today" button. The white pill on the dark heroes — measured, never followed (it leads to sign-up).

Page: connect. Selector: `a, button`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 413 x 101 | = | = |
| Padding | 0px 64px | = | = |
| Border | none | = | = |
| Radius | 64px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Museo Sans Rounded 34px/37.4px 900 | = | = |
| Letter spacing | normal | = | = |
| Colour | #111111 | = | = |
| Text node | span: Museo Sans Rounded 34px/37.4px 900, #111111 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Painted layers | a.button-primary.button-on-color 413.0x101.0 bg #ffffff r 64px | = | = |
| How | resting state | mouse hover over the element | CDP CSS.forcePseudoState(:active:hover) — no real press |
| Opacity | - | 0.8 | = |

Crops: `get-started-today-default.png`, `get-started-today-hover.png`, `get-started-today-pressed.png`.

### Applet page

#### connect-toggle

"Connect" toggle. The big black pill with the brand-coloured knob — the applet's install control, styled like a giant switch. Measured, never pressed (it leads to sign-in).

Page: applet. Selector: `a, button, div.connect-cta`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 480.05 x 95.94 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 47.97px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Museo Sans Rounded 18px/21.6px 900 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Text node | span: Museo Sans Rounded 33.9219px/40.7062px 900, #ffffff | = | = |
| Transition | opacity 0.4s ease | = | = |
| Cursor | pointer | = | = |
| Ancestor paint | 1 up div.platform-preview.connect-button bg #111111 | = | = |
| How | resting state | mouse hover over the element | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `connect-toggle-default.png`, `connect-toggle-hover.png`, `connect-toggle-pressed.png`.

#### applet-meta

Applet meta line. .applet-meta-line — the "iRobot · 20.8k" byline under the headline.

Page: applet. Selector: `.applet-meta-line`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480.05 x 45 |
| Padding | 0px |
| Gap | 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 18px/21.6px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.author: Museo Sans Rounded 16px/20.8px 900, #ffffff |
| Transition | none |
| How | resting state |

Crops: `applet-meta-default.png`.

#### author-link

Author link. a.author-link.link-on-color — the applet author on the brand-coloured hero.

Page: applet. Selector: `a.author-link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 78.78 x 20.8 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Museo Sans Rounded 16px/20.8px 900 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | span.author: Museo Sans Rounded 16px/20.8px 900, #ffffff | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | resting state | mouse hover over the element |

Crops: `author-link-default.png`, `author-link-hover.png`.

#### trigger-row

Trigger row. A trigger line in the "About this Applet" detail ("You exit an area" — a.meta-type "Realtime trigger").

Page: applet. Selector: `a.meta-type`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 143 x 25.69 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 18px/21.6px 500 |
| Letter spacing | normal |
| Colour | #111111 |
| Text node | span.meta-text: Museo Sans Rounded 14px/18.2px 700, #111111 |
| Transition | none |
| Icon | 16 x 16, colour #111111 |
| Painted layers | a.meta-type 143.0x24.2 bg #111111 @ 0.05 border T:1px solid #111111 @ 0.1 / R:1px solid #111111 @ 0.1 / B:1px solid #111111 @ 0.1 / L:1px solid #111111 @ 0.1 r 6px; div.tool-tip.tool-tip--dark 305.0x152.0 bg #333333 r 10px shadow #000000 @ 0.25 0px 3px 4px 0px |
| How | resting state |

Crops: `trigger-row-default.png`.

#### service-item

Service list row. a.service-item — a service row in the page's service list ("Location", "iRobot").

Page: applet. Selector: `a.service-item`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 480.05 x 64 | = |
| Padding | 12px 0px | = |
| Gap | 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Museo Sans Rounded 18px/21.6px 500 | = |
| Letter spacing | normal | = |
| Colour | #111111 | = |
| Text node | span.service-name.text-h4: Museo Sans Rounded 20px/22px 900, #111111 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 15 x 20, colour #111111 | = |
| Painted layers | div.service-icon-wrapper 40.0x40.0 bg #0099ff border T:1px solid #111111 @ 0.1 / R:1px solid #111111 @ 0.1 / B:1px solid #111111 @ 0.1 / L:1px solid #111111 @ 0.1 r 8px | = |
| How | resting state | mouse hover over the element |

Crops: `service-item-default.png`, `service-item-hover.png`.

### Solutions

#### solutions-hero

Solutions hero. The hero band on a solutions page ("Achieve more in less time").

Page: solutions-productivity. Selector: `section, div`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 936 x 588.44 |
| Padding | 63.999px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 18px/21.6px 500 |
| Letter spacing | normal |
| Colour | #111111 |
| Text node | h1.heading: Museo Sans Rounded 50px/50px 900, #111111 |
| Transition | none |
| Painted layers | a.button-primary 300.0x101.0 bg #111111 r 64px |
| How | resting state |

Crops: `solutions-hero-default.png`.

#### solutions-card

Solutions feature card. A feature or use-case card on the solutions page.

Page: solutions-productivity. Selector: `div, a`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 311.39 x 324.53 |
| Padding | 9px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 18px/21.6px 500 |
| Letter spacing | normal |
| Colour | #111111 |
| Text node | span: Museo Sans Rounded 26.9453px/29.6398px 900, #ffffff |
| Transition | none |
| Painted layers | a.applet-card-body.spec-prefetch 293.4x306.5 bg #2c6efc r 24px shadow #000000 @ 0.24 0px 1.5px 6px 0px |
| How | resting state |

Crops: `solutions-card-default.png`.

### Marketing pages

#### marketing-h1

Marketing h1. The page headline on a marketing surface (mcp / about / careers).

Page: mcp. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1116 x 128 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 64px/64px 900 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| How | resting state |

Crops: `marketing-h1-default.png`.

#### prose-p

Body paragraph. A body paragraph of marketing or legal prose.

Page: mcp. Selector: `p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 567 x 70.17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 18px/23.4px 600 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| How | resting state |

Crops: `prose-p-default.png`.

#### prose-link

Inline prose link. A link inside body prose — the legal pages carry them (/mcp prose has no inline links).

Page: terms. Selector: `main p a, p a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 38 x 19 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Museo Sans Rounded 16px/20.8px 900 | = |
| Letter spacing | normal | = |
| Colour | #01b6ff | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | resting state | mouse hover over the element |

Crops: `prose-link-default.png`, `prose-link-hover.png`.

### Mobile (390)

#### m-header

Mobile header. The 390px header: wordmark, search button and the hamburger.

Page: mobile. Selector: `header.unified-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Museo Sans Rounded 20px/20px 700 |
| Letter spacing | normal |
| Colour | #111111 |
| Transition | none |
| Icon | 103.42 x 21, colour #111111 |
| Painted layers | header.unified-header.signed-out 390.0x64.0 bg #ffffff; input.ifttt-search-input 0.0x0.0 bg #ffffff border T:2px solid #111111 @ 0.1 / R:2px solid #111111 @ 0.1 / B:2px solid #111111 @ 0.1 / L:2px solid #111111 @ 0.1 r 32px; section.universal-search-helper 0.0x0.0 bg #ffffff r 8px shadow #000000 @ 0.14 0px 0px 10px 0px; div.recent-search-icon 0.0x0.0 bg #0099ff r 8px; div.recent-search-icon 0.0x0.0 bg #000000 r 8px; div.recent-search-icon 0.0x0.0 bg #ff0000 r 8px |
| Ancestor paint | 1 up body.home-body.show-action bg #ffffff |
| How | resting state |

Crops: `m-header-default.png`.

#### m-menu-button

Hamburger button. The mobile menu button. "opened" is its own press painting the full-screen menu (logo, Explore/Plans links, Log in / Get started) — closed with its own X.

Page: mobile. Selector: `button.closed`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 48 x 48 | 390 x 614 |
| Padding | 0px | 0px 20px |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Museo Sans Rounded 13.3333px/normal 400 | Museo Sans Rounded 20px/20px 700 |
| Letter spacing | normal | = |
| Colour | #111111 | = |
| Transition | none | = |
| Cursor | pointer | - |
| Icon | 24 x 24, colour #111111 | 0 x 0, colour #111111 |
| How | resting state | the hamburger's own press (the full-screen mobile menu open; closed with its X after) |
| Text node | - | a.nav-link.link-menu: Museo Sans Rounded 32px/32px 700, #111111 |
| Painted layers | - | a.sign-in.button-tertiary 351.0x54.0 r 64px shadow #111111 0px 0px 0px 2px inset; a.button-tertiary.sign-up 351.0x54.0 bg #111111 r 64px |

Crops: `m-menu-button-default.png`, `m-menu-button-opened.png`.

## Transitions declared in the readable stylesheets

IFTTT's sheets on web-assets.ifttt.com are CORS-readable, so this list holds the transition declarations the CSSOM could read on each page; the per-state Transition rows above are computed values regardless.

- applet: `opacity 0.15s`, `background-color 0.3s, opacity 0.15s`, `left 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955), background-color 0.3s`, `opacity 0.4s`, `opacity 1.4s linear`, `color 0.5s`, `background-color 0.15s ease-in-out`, `background-color 0.12s ease-in-out`, `transform 0.12s ease-in-out`, `opacity 0.15s ease-in-out`, `border-color 0.2s, opacity 0.2s`, `transform 0.2s`

- connect: `opacity 0.15s`, `background-color 0.3s, opacity 0.15s`, `left 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955), background-color 0.3s`, `opacity 0.4s`, `opacity 1.4s linear`, `color 0.5s`, `background-color 0.15s ease-in-out`, `background-color 0.12s ease-in-out`, `transform 0.12s ease-in-out`, `opacity 0.15s ease-in-out`, `border-color 0.2s, opacity 0.2s`, `transform 0.2s`

- explore: `opacity 0.15s`, `background-color 0.3s, opacity 0.15s`, `left 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955), background-color 0.3s`, `opacity 0.4s`, `opacity 1.4s linear`, `color 0.5s`, `background-color 0.15s ease-in-out`, `background-color 0.12s ease-in-out`, `transform 0.12s ease-in-out`, `opacity 0.15s ease-in-out`, `opacity 0.15s ease-out`

- home: `opacity 0.15s`, `background-color 0.3s, opacity 0.15s`, `left 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955), background-color 0.3s`, `opacity 0.4s`, `opacity 1.4s linear`, `color 0.5s`, `opacity 0.15s ease-in-out`, `opacity 0.2s`, `background-color 0.2s`

- mcp: `opacity 0.15s`, `background-color 0.3s, opacity 0.15s`, `left 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955), background-color 0.3s`, `opacity 0.4s`, `opacity 1.4s linear`, `color 0.5s`, `opacity 0.15s ease-in-out`, `background-color 0.1s ease-in-out`, `transform 0.2s ease-in-out`, `opacity 0.2s`, `background-color 0.2s`, `background-color 0.12s ease-in-out`

- mobile: `opacity 0.15s`, `background-color 0.3s, opacity 0.15s`, `left 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955), background-color 0.3s`, `opacity 0.4s`, `opacity 1.4s linear`, `color 0.5s`, `opacity 0.15s ease-in-out`, `opacity 0.2s`, `background-color 0.2s`

- plans: `opacity 0.15s`, `background-color 0.3s, opacity 0.15s`, `left 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955), background-color 0.3s`, `opacity 0.4s`, `opacity 1.4s linear`, `color 0.5s`, `opacity 0.15s ease-in-out`, `background-color 0.1s ease-in-out`, `transform 0.2s ease-in-out`, `opacity 0.2s`, `background-color 0.2s`, `background-color 0.12s ease-in-out`

- service: `opacity 0.15s`, `background-color 0.3s, opacity 0.15s`, `left 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955), background-color 0.3s`, `opacity 0.4s`, `opacity 1.4s linear`, `color 0.5s`, `background-color 0.15s ease-in-out`, `background-color 0.12s ease-in-out`, `transform 0.12s ease-in-out`, `opacity 0.15s ease-in-out`, `opacity 0.15s ease-out`, `border-color 0.2s`

- solutions-productivity: `0.1s`, `opacity 0.15s`, `background-color 0.3s, opacity 0.15s`, `left 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955), background-color 0.3s`, `opacity 0.4s`, `opacity 1.4s linear`, `color 0.5s`, `background-color 0.15s ease-in-out`, `background-color 0.12s ease-in-out`, `transform 0.12s ease-in-out`, `opacity 0.15s ease-in-out`, `border-color 0.2s, opacity 0.2s`

- terms: `opacity 0.15s`, `background-color 0.3s, opacity 0.15s`, `left 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955), background-color 0.3s`, `opacity 0.4s`, `opacity 1.4s linear`, `2s`, `3.5s`, `translateY 0.3s`
