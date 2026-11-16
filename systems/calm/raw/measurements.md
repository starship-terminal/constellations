# Component measurements

Computed styles read from calm.com (and the WordPress health.calm.com B2B surface) on 2026-11-16 by `tools/capture/public/measure.mjs`, signed out, in headed Chromium under Xvfb at 1440 x 900 (the Mobile group at 390 x 844) across the site's two painted surfaces — the light marketing pages and the dark signed-out /app/* preview shell — with the cookie-consent bar measured once, then hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Calm Health (B2B)

#### h-nav

Health nav. The WordPress B2B header menu (Solutions/Resources megamenus, Log In, contact CTA).

Page: health. Selector: `nav.main-menu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Figtree 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1a1b1f |
| Text node | button.main-menu__link.main-menu__submenu-btn: Figtree 16px/24px 400, #1a1b1f |
| Transition | all 0.2s ease |
| Icon | 137 x 56, colour #2f7ece |
| Painted layers | div.main-menu__wrapper 1425.0x105.0 border B:1px solid #000000 @ 0; ul.main-menu__submenu 0.0x0.0 bg #ffffff; ul.main-menu__submenu 0.0x0.0 bg #ffffff; ul.main-menu__submenu 0.0x0.0 bg #ffffff; ul.main-menu__submenu 0.0x0.0 bg #ffffff; button.btn.btn--primary 150.8x41.0 image linear-gradient(0deg, #4e4bb1 0px, #6461e0 49%, #60b4e7 100%) r 100px |
| How | at rest |

Crops: `h-nav-default.png`.

#### h-nav-link

Health nav link. A top-level B2B nav link.

Page: health. Selector: `.main-menu a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 90.41 x 99 | = | = | = |
| Padding | 40px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | #2f7ece @ 0.4 | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Figtree 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1a1b1f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.main-menu__link.main-menu__link--support 90.4x99.0 bg #2f7ece @ 0.4 | = |

Crops: `h-nav-link-default.png`, `h-nav-link-hover.png`, `h-nav-link-focus-visible.png`, `h-nav-link-pressed.png`.

#### h-mega-trigger

Megamenu trigger. A menu item that opens a megamenu panel; toggled, never followed.

Page: health. Selector: `.main-menu trigger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 119.77 x 104 | = | = | = |
| Padding | 40px 26.4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | #2f7ece @ 0.4 | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Figtree 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1a1b1f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.main-menu__link.main-menu__submenu-btn 119.8x104.0 bg #2f7ece @ 0.4 | = |

Crops: `h-mega-trigger-default.png`, `h-mega-trigger-hover.png`, `h-mega-trigger-focus-visible.png`, `h-mega-trigger-pressed.png`.

#### h-hero

Health hero. The B2B hero headline.

Page: health. Selector: `health h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 411.52 x 240.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Figtree 56px/60.2px 400 |
| Letter spacing | normal |
| Colour | #00458e |
| Transition | none |
| How | at rest |

Crops: `h-hero-default.png`.

#### h-cta

Health CTA. The B2B contact/action button; measured never followed.

Page: health. Selector: `health CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 150.78 x 41 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(0deg, #4e4bb1 0px, #6461e0 49%, #60b4e7 100%) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f8d22d offset 0px | = |
| Font | Figtree 14px/normal 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-position-y 0.3s ease-in | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.btn.btn--primary 150.8x41.0 image linear-gradient(0deg, #4e4bb1 0px, #6461e0 49%, #60b4e7 100%) r 100px | = | button.btn.btn--primary 150.8x41.0 image linear-gradient(0deg, #4e4bb1 0px, #6461e0 49%, #60b4e7 100%) r 100px outline 2px solid #f8d22d offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Ancestor paint | - | = | 1 up li.main-menu__item.main-menu__item--right outline 2px solid #f8d22d | = |

Crops: `h-cta-default.png`, `h-cta-hover.png`, `h-cta-focus-visible.png`, `h-cta-pressed.png`.

#### h-card

Health card. A card on the B2B surface (customer story, benefit or resource card).

Page: health. Selector: `health card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 378.66 x 119.34 | 378.66 x 180.92 | = | 378.66 x 180.92 |
| Padding | 0px | = | = | = |
| Border | 2px solid #000000 @ 0 | 2px solid #60b4e7 @ 0.996 | = | 2px solid #60b4e7 @ 0.965 |
| Radius | 12px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0.08 0px 2px 12px 0px | = | = | = |
| Outline | none | = | 1px solid #eccd37 offset 0.9375px | = |
| Font | Figtree 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2f7ece | = | = | = |
| Text node | h4.custom-cards__card__title: Figtree 24.8px/32.24px 600, #1a1b1f | h4.custom-cards__card__title: Figtree 24.8px/32.24px 600, #2f7dcd | = | h4.custom-cards__card__title: Figtree 24.8px/32.24px 600, #2e7bc8 |
| Transition | all 0.5s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.custom-cards__card.custom-cards__card--hover 378.7x119.3 bg #ffffff border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px shadow #000000 @ 0.08 0px 2px 12px 0px | a.custom-cards__card.custom-cards__card--hover 378.7x180.9 bg #ffffff border T:2px solid #60b4e7 @ 0.996 / R:2px solid #60b4e7 @ 0.996 / B:2px solid #60b4e7 @ 0.996 / L:2px solid #60b4e7 @ 0.996 r 12px shadow #000000 @ 0.08 0px 2px 12px 0px | a.custom-cards__card.custom-cards__card--hover 378.7x119.3 bg #ffffff border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px shadow #000000 @ 0.08 0px 2px 12px 0px outline 1px solid #eccd37 offset 0.9375px | a.custom-cards__card.custom-cards__card--hover 378.7x180.9 bg #ffffff border T:2px solid #60b4e7 @ 0.965 / R:2px solid #60b4e7 @ 0.965 / B:2px solid #60b4e7 @ 0.965 / L:2px solid #60b4e7 @ 0.965 r 12px shadow #000000 @ 0.08 0px 2px 12px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `h-card-default.png`, `h-card-hover.png`, `h-card-focus-visible.png`, `h-card-pressed.png`.

#### h-footer

Health footer. The B2B footer.

Page: health. Selector: `health footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 459.23 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Figtree 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1a1b1f |
| Text node | span.footer__menu__title: Figtree 16px/normal 600, #1a1b1f |
| Transition | none |
| Painted layers | hr 1200.0x1.0 border B:1px solid #f3f2f2 |
| How | at rest |

Crops: `h-footer-default.png`.

### Shell and navigation

#### cookie-banner

Cookie bar. The consent bottom sheet ("Cookie Preferences"), measured then hidden and never answered — no consent choice is ever made.

Page: home. Selector: `div.Banner (cookie text)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 147 |
| Padding | 24px 16px |
| Border | T: 1px solid #aaaaaa; R: none; B: none; L: none |
| Radius | 0px |
| Background | #f7f7f7 |
| Box shadow | none |
| Outline | none |
| Font | Figtree 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.styles__StyledText-sc-a4b5006e-0.fCFjxZ: Figtree 18px/18px 700, #383838 |
| Transition | all 0.3s ease-in-out |
| Icon | 26 x 26, colour #ffffff, fill #000000 |
| Painted layers | div.styles__Banner-sc-15ea5bec-3.jOgWEN 1425.0x147.0 bg #f7f7f7 border T:1px solid #aaaaaa; button::before.styles__Wrapper-sc-7193a2d7-0.dnevEd 48pxx26px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.dnevEd 48pxx26px border T:2px solid #1a3e6f / R:2px solid #1a3e6f / B:2px solid #1a3e6f / L:2px solid #1a3e6f r 100px |
| How | at rest |

Crops: `cookie-banner-default.png`.

#### header

Header. The transparent marketing header over the hero photograph: app-icon logo, the Sleep/Stress & Anxiety/Mindfulness links, Screening, the Calm Health dropdown, Log In and the Try-Calm-for-Free pill.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 100 |
| Padding | 0px 40px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(#176293 0%, #176293 @ 0.337 71%, #176293 @ 0 100%) |
| Box shadow | none |
| Outline | none |
| Font | Figtree 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | button.styles__Wrapper-sc-2baa1e83-0.dnpxvL: Figtree 18px/normal 700, #ffffff |
| Transition | none |
| Icon | 56 x 56, colour #ffffff |
| ::after | 1425px x 100px, absolute, bg #ffffff, radius 0px |
| Painted layers | header.styles__Wrapper-sc-5441692d-0.fhYVJu 1425.0x100.0 image linear-gradient(#176293 0%, #176293 @ 0.337 71%, #176293 @ 0 100%); header::after.styles__Wrapper-sc-5441692d-0.fhYVJu 1425pxx100px bg #ffffff; a::before.styles__Wrapper-sc-7193a2d7-0.DOxGo 76pxx60px bg #000000 @ 0.15 r 100px; a::after.styles__Wrapper-sc-7193a2d7-0.DOxGo 76pxx60px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px; ul.styles__List-sc-7676a001-4.hAMGLQ 0.0x0.0 bg #ffffff r 10px shadow #000000 @ 0.16 0px 4px 16px 0px; button.styles__Wrapper-sc-7193a2d7-0.gHvnMY 200.0x56.0 bg #ffffff r 100px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The rounded-square app icon anchor (the #60B4E7->#6461E0 gradient tile with the white wordmark inside).

Page: home. Selector: `header a[aria-label*="Calm Logo"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 76 x 60 |
| Padding | 14px 17.7778px |
| Border | none |
| Radius | 100px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Figtree 18px/28px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | all 0.3s ease-out |
| Cursor | pointer |
| Icon | 56 x 56, colour #ffffff |
| ::before | 76px x 60px, absolute, bg #000000 @ 0.15, radius 100px |
| ::after | 76px x 60px, absolute, bg #000000 @ 0, radius 100px |
| Painted layers | a::before.styles__Wrapper-sc-7193a2d7-0.DOxGo 76pxx60px bg #000000 @ 0.15 r 100px; a::after.styles__Wrapper-sc-7193a2d7-0.DOxGo 76pxx60px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav item. A plain header item (Sleep, Mindfulness or Screening) — a styled-components button that opens a section panel, not an anchor.

Page: home. Selector: `header button (Sleep)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 46.13 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Figtree 18px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.styles__Wrapper-sc-2baa1e83-0.dnpxvL 46.1x22.0 outline 1px auto #101010 offset 0px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-trigger

Nav trigger. The Calm Health chevron that opens the dropdown panel; toggled, never followed.

Page: home. Selector: `header button.Trigger (Calm Health)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 120.05 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Figtree 18px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 6, colour #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.styles__Trigger-sc-7676a001-1.lnwsMr 120.0x22.0 outline 1px auto #101010 offset 0px | = |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### nav-login

Nav login. The header Log In button; pressing it opens the login card, measured under login-dialog, never submitted.

Page: home. Selector: `button[data-testid=desktopnav-login-button]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50.66 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Figtree 18px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.styles__Wrapper-sc-2baa1e83-0.dnpxvL 50.7x22.0 outline 1px auto #101010 offset 0px | = |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-cta

Nav CTA. The white Try-Calm-for-Free header pill; pressing it opens the signup flow (the page measured under signup-), never submitted.

Page: home. Selector: `header a/button (Try Calm)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 200 x 56 | = | = | = |
| Padding | 14px 17.7778px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Figtree 18px/28px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #383838 | = | = | = |
| Transition | all 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 200px x 56px, absolute, bg #000000 @ 0.15, radius 100px | = | = | = |
| ::after | 200px x 56px, absolute, bg #000000 @ 0, radius 100px | = | 212px x 68px, absolute, bg #000000 @ 0, radius 100px | = |
| Painted layers | button.styles__Wrapper-sc-7193a2d7-0.gHvnMY 200.0x56.0 bg #ffffff r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.gHvnMY 200pxx56px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.gHvnMY 200pxx56px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px | = | button.styles__Wrapper-sc-7193a2d7-0.dRbckz 200.0x56.0 bg #ffffff r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.dRbckz 200pxx56px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.dRbckz 212pxx68px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px | button.styles__Wrapper-sc-7193a2d7-0.lgXjgr 200.0x56.0 bg #ffffff r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.lgXjgr 200pxx56px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.lgXjgr 200pxx56px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### hero-title

Hero headline. The navy "Calm your mind. Change your life." headline.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768.69 x 74.25 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Figtree 49.5px/74.25px 700 |
| Letter spacing | normal |
| Colour | #1a3e6f |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero copy. The lede under the headline.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768.69 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Figtree 22.5px/28px 500 |
| Letter spacing | normal |
| Colour | #000000 @ 0.8 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-cta

Hero CTA. The navy hero action; measured never followed.

Page: home. Selector: `hero Try Calm for Free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 335 x 58 | = | = | = |
| Padding | 14px 17.7778px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(#2477aa 0%, #6461e0 100%) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Figtree 18px/28px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 335px x 58px, absolute, bg #000000 @ 0.15, radius 100px | = | = | = |
| ::after | 335px x 58px, absolute, bg #000000 @ 0, radius 100px | = | 347px x 70px, absolute, bg #000000 @ 0, radius 100px | = |
| Painted layers | button.styles__Wrapper-sc-7193a2d7-0.iODOPy 335.0x58.0 image linear-gradient(#2477aa 0%, #6461e0 100%) r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.iODOPy 335pxx58px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.iODOPy 335pxx58px border T:2px solid #1a3e6f / R:2px solid #1a3e6f / B:2px solid #1a3e6f / L:2px solid #1a3e6f r 100px | = | button.styles__Wrapper-sc-7193a2d7-0.iiDXSx 335.0x58.0 image linear-gradient(#2477aa 0%, #6461e0 100%) r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.iiDXSx 335pxx58px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.iiDXSx 347pxx70px border T:2px solid #1a3e6f / R:2px solid #1a3e6f / B:2px solid #1a3e6f / L:2px solid #1a3e6f r 100px | button.styles__Wrapper-sc-7193a2d7-0.hMFFGF 335.0x58.0 image linear-gradient(#2477aa 0%, #6461e0 100%) r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.hMFFGF 335pxx58px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.hMFFGF 335pxx58px border T:2px solid #1a3e6f / R:2px solid #1a3e6f / B:2px solid #1a3e6f / L:2px solid #1a3e6f r 100px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### learn-more

Section card link. A marketing section card (Stress less. / Sleep more. / Live mindfully.) — a button carrying the heading, copy and Learn-more label; measured never followed.

Page: home. Selector: `section card button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 352.33 x 247 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Figtree 18px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | h3.styles__StyledText-sc-a4b5006e-0.gOTvMR: Figtree 31.5px/48px 500, #000000 @ 0.8 | h3.styles__StyledText-sc-a4b5006e-0.gOTvMR: Figtree 31.5px/48px 500, #176293 | = | h3.styles__StyledText-sc-a4b5006e-0.gOTvMR: Figtree 31.5px/48px 500, #176293 |
| Transition | all 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 54 x 54, colour #000000 | = | = | = |
| ::after | 352.328px x 247px, absolute, bg #000000 @ 0, radius 20px | = | = | = |
| Painted layers | button::after.styles__Wrapper-sc-2baa1e83-0.byLhOR 352.328pxx247px border T:2px solid #176293 / R:2px solid #176293 / B:2px solid #176293 / L:2px solid #176293 r 20px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `learn-more-default.png`, `learn-more-hover.png`, `learn-more-focus-visible.png`, `learn-more-pressed.png`.

#### section-h2

Section heading. A marketing section heading (Stress less. / Sleep more. / Live mindfully.).

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1153 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Figtree 36px/60px 700 |
| Letter spacing | normal |
| Colour | #1a3e6f |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

### App shell (dark)

#### rail

App rail. The dark left rail: wordmark, Home/Meditate/Sleep/Music/For Work/Wisdom/Calm Kids/Movement/Profile icon items.

Page: sleep. Selector: `aside`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 240 x 900 |
| Padding | 40px 24px |
| Border | none |
| Radius | 0px |
| Background | #000000 @ 0.3 |
| Box shadow | none |
| Backdrop filter | blur(12px) |
| Outline | none |
| Font | Figtree 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.styles__Label-sc-f7711adb-1.ggIiXQ: Figtree 18px/normal 400, #ffffff |
| Transition | none |
| Icon | 48 x 48, colour #000000 |
| Painted layers | aside.styles__Wrapper-sc-149d7411-0.jRJrtc 240.0x900.0 bg #000000 @ 0.3; div.styles__HandoffExpandedWrapper-sc-bcee87bb-1.bOXHkK 240.0x284.0 bg #ffffff r 20px 20px 0px 0px; button::before.styles__Wrapper-sc-7193a2d7-0.iOYRrd 50pxx50px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.iOYRrd 50pxx50px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px |
| How | at rest |

Crops: `rail-default.png`.

#### rail-item

Rail item. An icon-plus-label rail link.

Page: sleep. Selector: `nav[aria-label="main app"] a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 192 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Figtree 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.styles__Label-sc-f7711adb-1.ggIiXQ: Figtree 18px/normal 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 48 x 48, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.styles__Wrapper-sc-f7711adb-2.FoZvx 192.0x48.0 outline 1px auto #101010 offset 1px | = |

Crops: `rail-item-default.png`, `rail-item-hover.png`, `rail-item-focus-visible.png`, `rail-item-pressed.png`.

#### rail-item-active

Rail item, selected. The selected Sleep rail item (its icon tile filled).

Page: sleep. Selector: `rail a Sleep`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 192 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Figtree 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.styles__Label-sc-f7711adb-1.ggIiXQ: Figtree 18px/normal 700, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 48 x 48, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.styles__Wrapper-sc-f7711adb-2.dEwIdS 192.0x48.0 outline 1px auto #101010 offset 1px | = |

Crops: `rail-item-active-default.png`, `rail-item-active-hover.png`, `rail-item-active-focus-visible.png`, `rail-item-active-pressed.png`.

#### topbar-search

Search link. The top-bar search icon link to /app/search (the wide search field only paints inside the search page); never followed.

Page: sleep. Selector: `a[href=/app/search]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 50% | = | = | = |
| Background | #ffffff @ 0.1 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Figtree 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | all 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 48 x 48, colour #000000 | = | = | = |
| Painted layers | a.styles__Wrapper-sc-cc9e3e04-0.cUuRcC 48.0x48.0 bg #ffffff @ 0.1 r 50% | = | a.styles__Wrapper-sc-cc9e3e04-0.cUuRcC 48.0x48.0 bg #ffffff @ 0.1 r 50% outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `topbar-search-default.png`, `topbar-search-hover.png`, `topbar-search-focus-visible.png`, `topbar-search-pressed.png`.

#### d-login

Dark login. The dark shell's translucent Log In pill (the shell paints no header element); opens the same login card, never submitted.

Page: sleep. Selector: `button (Log In)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.5 x 56 | = | = | = |
| Padding | 14px 17.7778px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #ffffff @ 0.1 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Figtree 18px/28px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 85.5px x 56px, absolute, bg #000000 @ 0.15, radius 100px | = | = | = |
| ::after | 85.5px x 56px, absolute, bg #000000 @ 0, radius 100px | = | 97.5px x 68px, absolute, bg #000000 @ 0, radius 100px | = |
| Painted layers | button.styles__Wrapper-sc-7193a2d7-0.TEFB 85.5x56.0 bg #ffffff @ 0.1 r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.TEFB 85.5pxx56px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.TEFB 85.5pxx56px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px | = | button.styles__Wrapper-sc-7193a2d7-0.gXaFrb 85.5x56.0 bg #ffffff @ 0.1 r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.gXaFrb 85.5pxx56px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.gXaFrb 97.5pxx68px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px | button.styles__Wrapper-sc-7193a2d7-0.bERca-D 85.5x56.0 bg #ffffff @ 0.1 r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.bERca-D 85.5pxx56px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.bERca-D 85.5pxx56px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `d-login-default.png`, `d-login-hover.png`, `d-login-focus-visible.png`, `d-login-pressed.png`.

#### d-cta

Dark CTA. The white Try-Calm-for-Free pill on the dark top bar; opens the signup flow, never submitted.

Page: sleep. Selector: `button (Try Calm)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 174.86 x 56 | = | = | = |
| Padding | 14px 17.7778px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Figtree 18px/28px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | all 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 174.859px x 56px, absolute, bg #000000 @ 0.15, radius 100px | = | = | = |
| ::after | 174.859px x 56px, absolute, bg #000000 @ 0, radius 100px | = | 186.859px x 68px, absolute, bg #000000 @ 0, radius 100px | = |
| Painted layers | button.styles__Wrapper-sc-7193a2d7-0.ibyBYQ 174.9x56.0 bg #ffffff r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.ibyBYQ 174.859pxx56px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.ibyBYQ 174.859pxx56px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px | = | button.styles__Wrapper-sc-7193a2d7-0.ldfyvC 174.9x56.0 bg #ffffff r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.ldfyvC 174.859pxx56px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.ldfyvC 186.859pxx68px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px | button.styles__Wrapper-sc-7193a2d7-0.jQvDii 174.9x56.0 bg #ffffff r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.jQvDii 174.859pxx56px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.jQvDii 174.859pxx56px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `d-cta-default.png`, `d-cta-hover.png`, `d-cta-focus-visible.png`, `d-cta-pressed.png`.

#### tab-active

Tab, selected. The selected white category pill (Sleep Stories/All).

Page: sleep. Selector: `category tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138.5 x 26 | = | = | = |
| Padding | 2px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Figtree 18px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #002152 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.styles__NavItem-sc-554e2362-1.jjoqob 138.5x26.0 bg #ffffff r 100px | = | a.styles__NavItem-sc-554e2362-1.jjoqob 138.5x26.0 bg #ffffff r 100px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `tab-active-default.png`, `tab-active-hover.png`, `tab-active-focus-visible.png`, `tab-active-pressed.png`.

#### tab

Tab. An unselected dark category pill.

Page: sleep. Selector: `category tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 127.59 x 26 | = | = | = |
| Padding | 2px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #000000 @ 0.3 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Figtree 18px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.styles__NavItem-sc-554e2362-1.hWziVS 127.6x26.0 bg #000000 @ 0.3 r 100px | = | a.styles__NavItem-sc-554e2362-1.hWziVS 127.6x26.0 bg #000000 @ 0.3 r 100px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tab-default.png`, `tab-hover.png`, `tab-focus-visible.png`, `tab-pressed.png`.

#### upsell

Upsell banner. The subscribe upsell bar ("You're missing out on the full Calm experience. Subscribe with 40% off ...") — the whole banner is one anchor.

Page: sleep. Selector: `a.UpsellBanner`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1153 x 76 |
| Padding | 18px 20px |
| Border | 2px solid #ffffff @ 0.1 |
| Radius | 16px |
| Background | #ffffff @ 0.1 |
| Box shadow | none |
| Outline | none |
| Font | Figtree 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.styles__StyledText-sc-a4b5006e-0.isyFQh: Figtree 18px/28px 500, #ffffff |
| Transition | none |
| Cursor | pointer |
| Icon | 36 x 24, colour #000000 |
| Painted layers | a.styles__UpsellBannerWrapper-sc-b2c89714-0.kHNScb 1153.0x76.0 bg #ffffff @ 0.1 border T:2px solid #ffffff @ 0.1 / R:2px solid #ffffff @ 0.1 / B:2px solid #ffffff @ 0.1 / L:2px solid #ffffff @ 0.1 r 16px; div.styles__TimeIconWrapper-sc-b2c89714-5.eJQfaq 36.0x36.0 image linear-gradient(135deg, #75f0f0 0%, #7575f0 100%) r 8px |
| How | at rest |

Crops: `upsell-default.png`.

#### content-card

Content card. A featured-story card: artwork tile, "New" badge, title and narrator.

Page: sleep. Selector: `featured card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 300 x 256 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Figtree 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.styles__NewTag-sc-746cd660-1.gFRvzb: Figtree 10px/12px 500, #000000 | = | = | = |
| Transition | opacity 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | = | = | = |
| Painted layers | div.styles__ImageWrapper-sc-746cd660-2.gWtqsq 300.0x200.0 r 16px shadow #000000 @ 0.2 0px 4px 12px 0px; div.styles__LockBadge-sc-f065fab4-0.kwtavd 28.0x28.0 bg #484848 @ 0.4 r 50%; div.styles__NewTag-sc-746cd660-1.gFRvzb 33.0x20.0 bg #ffffff r 999px | = | a.styles__CardContainer-sc-746cd660-4.gMsfOt 300.0x256.0 outline 1px auto #101010 offset 0px; div.styles__ImageWrapper-sc-746cd660-2.gWtqsq 300.0x200.0 r 16px shadow #000000 @ 0.2 0px 4px 12px 0px; div.styles__LockBadge-sc-f065fab4-0.kwtavd 28.0x28.0 bg #484848 @ 0.4 r 50%; div.styles__NewTag-sc-746cd660-1.gFRvzb 33.0x20.0 bg #ffffff r 999px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `content-card-default.png`, `content-card-hover.png`, `content-card-focus-visible.png`, `content-card-pressed.png`.

#### card-badge

New badge. The white "New" chip on a card's artwork.

Page: sleep. Selector: `[data-testid=new-icon]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 33.05 x 20 |
| Padding | 4px 6px |
| Border | none |
| Radius | 999px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Figtree 10px/12px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.styles__NewTag-sc-746cd660-1.gFRvzb 33.0x20.0 bg #ffffff r 999px |
| Ancestor paint | 1 up div.styles__ImageWrapper-sc-746cd660-2.gWtqsq shadow #000000 @ 0.2 0px 4px 12px 0px |
| How | at rest |

Crops: `card-badge-default.png`.

#### see-all

See All. A section "See All" link with its chevron.

Page: sleep. Selector: `See All`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81.27 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Figtree 18px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 20, colour #ffffff, fill #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.styles__Wrapper-sc-dea8a0a4-0.ejjkYV 81.3x22.0 outline 1px auto #101010 offset 1px | = |

Crops: `see-all-default.png`, `see-all-hover.png`, `see-all-focus-visible.png`, `see-all-pressed.png`.

#### carousel-arrow

Carousel arrow. A rail carousel arrow (the "Scroll carousel towards next items" chevron).

Page: sleep. Selector: `button[aria-label*=carousel][aria-label*=next]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #000000 @ 0.4 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Figtree 18px/28px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s ease-out | = | = | = |
| Transform | matrix(-1, 0, 0, -1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 26 x 20, colour #ffffff, fill #000000 | = | = | = |
| ::before | 44px x 44px, absolute, bg #000000 @ 0.15, radius 100px | = | = | = |
| ::after | 32px x 32px, absolute, bg #000000 @ 0, radius 100px | = | 44px x 44px, absolute, bg #000000 @ 0, radius 100px | = |
| Painted layers | button.styles__Wrapper-sc-7193a2d7-0.bVnmXP 32.0x32.0 bg #000000 @ 0.4 r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.bVnmXP 44pxx44px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.bVnmXP 32pxx32px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px | = | button.styles__Wrapper-sc-7193a2d7-0.gsUBKf 32.0x32.0 bg #000000 @ 0.4 r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.gsUBKf 44pxx44px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.gsUBKf 44pxx44px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `carousel-arrow-default.png`, `carousel-arrow-hover.png`, `carousel-arrow-focus-visible.png`, `carousel-arrow-pressed.png`.

#### signup-bar

Signup bar. The bottom notification bar ("Get notified of new Calm content ...") — a full-width anchor carrying the Sign-up-today gradient pill; never submitted.

Page: sleep. Selector: `a.UpsellFooter`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 92 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(113.79deg, #f1f5fe 7.89%, #c7def8 33%, #d9ecf6 62.5%, #f1f5fe 100%) |
| Box shadow | none |
| Outline | none |
| Font | Figtree 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.styles__StyledText-sc-a4b5006e-0.eSbVtx: Figtree 18px/28px 500, #000000 |
| Transition | none |
| Cursor | pointer |
| Painted layers | a.styles__UpsellFooterWrapper-sc-ec929e2c-0.fFdbui 1425.0x92.0 image linear-gradient(113.79deg, #f1f5fe 7.89%, #c7def8 33%, #d9ecf6 62.5%, #f1f5fe 100%); button.styles__Wrapper-sc-7193a2d7-0.lgttZs 147.9x56.0 image linear-gradient(#2477aa 0%, #6461e0 100%) r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.lgttZs 147.891pxx56px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.lgttZs 147.891pxx56px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px |
| How | at rest |

Crops: `signup-bar-default.png`.

#### med-title

Section title. The page title of an app-shell section (Meditate).

Page: meditate. Selector: `section h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1153 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Figtree 31.5px/40px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `med-title-default.png`.

#### med-card

Meditate card. A featured content card on the Meditate surface (the shared CardContainer: artwork, title, narrator).

Page: meditate. Selector: `a.CardContainer`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 300 x 256 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Figtree 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | h3.styles__StyledText-sc-a4b5006e-0.fSkNas: Figtree 13px/16.9px 600, #ffffff | = | = | = |
| Transition | opacity 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | = | = | = |
| Painted layers | div.styles__ImageWrapper-sc-746cd660-2.gWtqsq 300.0x200.0 r 16px shadow #000000 @ 0.2 0px 4px 12px 0px; div.styles__LockBadge-sc-f065fab4-0.kwtavd 28.0x28.0 bg #484848 @ 0.4 r 50% | = | a.styles__CardContainer-sc-746cd660-4.gMsfOt 300.0x256.0 outline 1px auto #101010 offset 0px; div.styles__ImageWrapper-sc-746cd660-2.gWtqsq 300.0x200.0 r 16px shadow #000000 @ 0.2 0px 4px 12px 0px; div.styles__LockBadge-sc-f065fab4-0.kwtavd 28.0x28.0 bg #484848 @ 0.4 r 50% | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `med-card-default.png`, `med-card-hover.png`, `med-card-focus-visible.png`, `med-card-pressed.png`.

#### signup-button

Signup button. The gradient Sign-up-today button (pill-shaped) in the bottom bar; never pressed for real.

Page: sleep. Selector: `Sign up today button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 147.89 x 56 | = | = | = |
| Padding | 14px 17.7778px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(#2477aa 0%, #6461e0 100%) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Figtree 18px/28px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 147.891px x 56px, absolute, bg #000000 @ 0.15, radius 100px | = | = | = |
| ::after | 147.891px x 56px, absolute, bg #000000 @ 0, radius 100px | = | 159.891px x 68px, absolute, bg #000000 @ 0, radius 100px | = |
| Painted layers | button.styles__Wrapper-sc-7193a2d7-0.lgttZs 147.9x56.0 image linear-gradient(#2477aa 0%, #6461e0 100%) r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.lgttZs 147.891pxx56px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.lgttZs 147.891pxx56px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px | = | button.styles__Wrapper-sc-7193a2d7-0.bfLmPO 147.9x56.0 image linear-gradient(#2477aa 0%, #6461e0 100%) r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.bfLmPO 147.891pxx56px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.bfLmPO 159.891pxx68px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px | button.styles__Wrapper-sc-7193a2d7-0.bualYm 147.9x56.0 image linear-gradient(#2477aa 0%, #6461e0 100%) r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.bualYm 147.891pxx56px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.bualYm 147.891pxx56px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-button-default.png`, `signup-button-hover.png`, `signup-button-focus-visible.png`, `signup-button-pressed.png`.

### Footer

#### footer

Footer. The marketing footer: link columns, social icons, legal.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 524 |
| Padding | 48px 0px |
| Border | none |
| Radius | 0px |
| Background | #1b2250 |
| Box shadow | none |
| Outline | none |
| Font | Figtree 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.styles__StyledText-sc-a4b5006e-0.bgBUUE: Figtree 18px/28px 500, #ffffff |
| Transition | none |
| Icon | 18 x 18, colour #000000, fill #ffffff |
| Painted layers | footer.styles__Wrapper-sc-523c7602-5.bvfLbF 1425.0x524.0 bg #1b2250 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44.47 x 19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Figtree 16px/30px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s ease-out | = | = | = |
| Opacity | 0.8 | 0.5 | = | 0.5 |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.styles__FooterItem-sc-523c7602-4.cTpfxy 44.5x19.0 outline 1px auto #101010 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-icon

Social icon. A social icon link in the footer (Facebook/Instagram/Twitter); the footer carries no app-store badges.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 18 x 19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Figtree 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Opacity | 0.8 | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #000000, fill #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.styles__SocialIcon-sc-523c7602-7.cNDlHA 18.0x19.0 outline 1px auto #101010 offset 0px | = |

Crops: `social-icon-default.png`, `social-icon-hover.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

### Login and signup

#### login-dialog

Login card. The white "Log into your account" modal card over a dimmed blur backdrop; opened by its own Log In button, never submitted.

Page: login. Selector: `[role=dialog]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 544 x 596 |
| Padding | 0px |
| Border | 1px solid #ffffff |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.25 0px 8px 24px 0px |
| Outline | none |
| Font | Figtree 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.styles__StyledText-sc-a4b5006e-0.gtyXdW: Figtree 31.5px/48px 500, #000000 |
| Transition | all 0.5s ease-out |
| Icon | 26 x 26, colour #ffffff, fill #000000 |
| Painted layers | div.styles__ModalBody-sc-e05c3eed-4.cMCVMv 544.0x596.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 16px shadow #000000 @ 0.25 0px 8px 24px 0px; button.styles__Wrapper-sc-7193a2d7-0.gwQCvD 462.0x56.0 bg #1a3e6f border T:1px solid #1a3e6f / R:1px solid #1a3e6f / B:1px solid #1a3e6f / L:1px solid #1a3e6f r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.gwQCvD 460pxx54px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.gwQCvD 460pxx54px border T:2px solid #1a3e6f / R:2px solid #1a3e6f / B:2px solid #1a3e6f / L:2px solid #1a3e6f r 100px; button.styles__Wrapper-sc-7193a2d7-0.cMTxYR 462.0x56.0 bg #ffffff border T:1px solid #aaaaaa / R:1px solid #aaaaaa / B:1px solid #aaaaaa / L:1px solid #aaaaaa r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.cMTxYR 460pxx54px bg #000000 @ 0.15 r 100px |
| How | at rest |

Crops: `login-dialog-default.png`.

#### login-email-btn

Sign-in primary. The navy Sign-in-with-Email pill inside the login card; never pressed for real.

Page: login. Selector: `dialog Sign in with Email`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 462 x 56 | = | = | = |
| Padding | 14px 17.7778px 14px 19.8519px | = | = | = |
| Border | 1px solid #1a3e6f | = | = | = |
| Radius | 100px | = | = | = |
| Background | #1a3e6f | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Figtree 18px/28px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 26 x 26, colour #ffffff, fill #000000 | = | = | = |
| ::before | 460px x 54px, absolute, bg #000000 @ 0.15, radius 100px | = | = | = |
| ::after | 460px x 54px, absolute, bg #000000 @ 0, radius 100px | = | 471.906px x 65.9062px, absolute, bg #000000 @ 0, radius 100px | = |
| Painted layers | button.styles__Wrapper-sc-7193a2d7-0.gwQCvD 462.0x56.0 bg #1a3e6f border T:1px solid #1a3e6f / R:1px solid #1a3e6f / B:1px solid #1a3e6f / L:1px solid #1a3e6f r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.gwQCvD 460pxx54px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.gwQCvD 460pxx54px border T:2px solid #1a3e6f / R:2px solid #1a3e6f / B:2px solid #1a3e6f / L:2px solid #1a3e6f r 100px | = | button.styles__Wrapper-sc-7193a2d7-0.itvKJD 462.0x56.0 bg #1a3e6f border T:1px solid #1a3e6f / R:1px solid #1a3e6f / B:1px solid #1a3e6f / L:1px solid #1a3e6f r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.itvKJD 460pxx54px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.itvKJD 471.906pxx65.9062px border T:2px solid #1a3e6f / R:2px solid #1a3e6f / B:2px solid #1a3e6f / L:2px solid #1a3e6f r 100px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-email-btn-default.png`, `login-email-btn-hover.png`, `login-email-btn-focus-visible.png`, `login-email-btn-pressed.png`.

#### login-social-btn

Sign-in social. A white outline social sign-in pill; never pressed for real.

Page: login. Selector: `dialog social button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 462 x 56 | = | = | = |
| Padding | 14px 17.7778px | = | = | = |
| Border | 1px solid #aaaaaa | = | = | = |
| Radius | 100px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Figtree 18px/28px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | all 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 30 x 30, colour #000000 | = | = | = |
| ::before | 460px x 54px, absolute, bg #000000 @ 0.15, radius 100px | = | = | = |
| ::after | 460px x 54px, absolute, bg #000000 @ 0, radius 100px | = | 471.75px x 65.75px, absolute, bg #000000 @ 0, radius 100px | = |
| Painted layers | button.styles__Wrapper-sc-7193a2d7-0.cMTxYR 462.0x56.0 bg #ffffff border T:1px solid #aaaaaa / R:1px solid #aaaaaa / B:1px solid #aaaaaa / L:1px solid #aaaaaa r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.cMTxYR 460pxx54px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.cMTxYR 460pxx54px border T:2px solid #1a3e6f / R:2px solid #1a3e6f / B:2px solid #1a3e6f / L:2px solid #1a3e6f r 100px | = | button.styles__Wrapper-sc-7193a2d7-0.esNbEZ 462.0x56.0 bg #ffffff border T:1px solid #aaaaaa / R:1px solid #aaaaaa / B:1px solid #aaaaaa / L:1px solid #aaaaaa r 100px; button::before.styles__Wrapper-sc-7193a2d7-0.esNbEZ 460pxx54px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.esNbEZ 471.75pxx65.75px border T:2px solid #1a3e6f / R:2px solid #1a3e6f / B:2px solid #1a3e6f / L:2px solid #1a3e6f r 100px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-social-btn-default.png`, `login-social-btn-hover.png`, `login-social-btn-focus-visible.png`, `login-social-btn-pressed.png`.

#### dialog-close

Dialog close. The X close control of the login card.

Page: login. Selector: `button[data-testid=modal-close]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 48 x 36 |
| Padding | 14px 17.7778px |
| Border | none |
| Radius | 100px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Figtree 18px/28px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | all 0.3s ease-out |
| Cursor | pointer |
| Icon | 16 x 16, colour #ffffff |
| ::before | 48px x 36px, absolute, bg #000000 @ 0.15, radius 100px |
| ::after | 48px x 36px, absolute, bg #000000 @ 0, radius 100px |
| Painted layers | button::before.styles__Wrapper-sc-7193a2d7-0.bVnmXP 48pxx36px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.bVnmXP 48pxx36px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px |
| Ancestor paint | 1 up div.styles__ModalBody-sc-e05c3eed-4.cMCVMv bg #ffffff shadow #000000 @ 0.25 0px 8px 24px 0px |
| How | at rest |

Crops: `dialog-close-default.png`.

#### signup-field

Signup control. The first interactive control on the signup landing page; never pressed for real.

Page: login. Selector: `signup page control`. States: .

Not found on the page at capture time.

#### signup-page

Signup page. The page the Try-Calm-for-Free button navigates to (/signup-flow?source=homepage) — the signup flow's first step, reached by its own button and never submitted; its landing stayed PerimeterX-blocked this run.

Page: login. Selector: `signup landing main`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1424 x 0 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times New Roman 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.px-captcha-header: Roboto 29px/24.07px 500, #626364 |
| Transition | none |
| Painted layers | div.px-captcha-container 530.0x340.0 bg #ffffff r 3px shadow #000000 @ 0.13 0px 2px 9px -1px; div.px-captcha-refid 530.0x28.0 bg #fafbfc border T:1px solid #f0eeee r 0px 0px 3px 3px |
| Ancestor paint | 1 up body bg #fafbfc |
| How | at rest |

Crops: none.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 375 x 64 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(#176293 0%, #176293 @ 0.337 71%, #176293 @ 0 100%) |
| Box shadow | none |
| Outline | none |
| Font | Figtree 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | button.styles__Wrapper-sc-7193a2d7-0.gHvnMY: Figtree 16px/28px 700, #383838 |
| Transition | none |
| Icon | 0 x 0, colour #ffffff |
| ::after | 375px x 64px, absolute, bg #ffffff, radius 0px |
| Painted layers | header.styles__Wrapper-sc-5441692d-0.fhYVJu 375.0x64.0 image linear-gradient(#176293 0%, #176293 @ 0.337 71%, #176293 @ 0 100%); header::after.styles__Wrapper-sc-5441692d-0.fhYVJu 375pxx64px bg #ffffff; a::before.styles__Wrapper-sc-7193a2d7-0.DOxGo 64pxx25px bg #000000 @ 0.15 r 100px; a::after.styles__Wrapper-sc-7193a2d7-0.DOxGo 64pxx25px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px; ul.styles__List-sc-7676a001-4.hAMGLQ 0.0x0.0 bg #ffffff r 10px shadow #000000 @ 0.16 0px 4px 16px 0px; button.styles__Wrapper-sc-7193a2d7-0.gHvnMY 180.0x52.0 bg #ffffff r 100px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The hamburger menu toggle (aria-label "Open Mobile menu").

Page: mobile. Selector: `button[aria-label*=menu]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 48 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 100px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Figtree 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | all 0.3s ease-out |
| Cursor | pointer |
| ::before | 48px x 48px, absolute, bg #000000 @ 0.15, radius 100px |
| ::after | 48px x 48px, absolute, bg #000000 @ 0, radius 100px |
| Painted layers | button::before.styles__Wrapper-sc-7193a2d7-0.feUdRs 48pxx48px bg #000000 @ 0.15 r 100px; button::after.styles__Wrapper-sc-7193a2d7-0.feUdRs 48pxx48px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px; div.styles__Line-sc-be7485e7-0.JgAYr 32.0x2.5 bg #ffffff r 2.5px; div.styles__Line-sc-be7485e7-0.JgAYr 32.0x2.5 bg #ffffff r 2.5px; div.styles__Line-sc-be7485e7-0.JgAYr 32.0x2.5 bg #ffffff r 2.5px |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The full-screen nav panel (aria-label "Mobile navigation menu", fixed z:999) opened by the hamburger toggle.

Page: mobile. Selector: `nav[aria-label=Mobile navigation menu]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 375 x 844 |
| Padding | 64px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(#60b4e7 0%, #6461e0 100%) |
| Box shadow | none |
| Outline | none |
| Font | Figtree 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | button.styles__Wrapper-sc-2baa1e83-0.dnpxvL: Figtree 24px/normal 500, #ffffff |
| Transition | all 0.3s ease-out |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 33 x 33, colour #ffffff |
| ::after | 360px x 829px, absolute, bg #000000 @ 0.2, radius 0px |
| Painted layers | nav.styles__Wrapper-sc-cf6e034c-0.dQNHHK 375.0x844.0 image linear-gradient(#60b4e7 0%, #6461e0 100%); nav::after.styles__Wrapper-sc-cf6e034c-0.dQNHHK 360pxx829px bg #000000 @ 0.2 |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. A button inside the opened mobile menu (Sleep, Mindfulness or Screening — the same styled-components nav items as desktop).

Page: mobile. Selector: `mobile nav button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 60.7 x 29 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Figtree 24px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.styles__Wrapper-sc-2baa1e83-0.dnpxvL 60.7x29.0 outline 1px auto #101010 offset 0px | = |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 250 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Figtree 24px/36px 700 |
| Letter spacing | normal |
| Colour | #1a3e6f |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

calm.com serves its Next.js CSS bundles and styled-components blocks same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- health: `0.2s`, `opacity 0.5s`, `background-position-y 0.3s ease-in`, `box-shadow 250ms, background 250ms`, `opacity 0.2s`, `150ms ease-in-out`, `opacity 0.2s, transform 0.2s`, `250ms ease-in-out`, `0.8s ease-in-out`, `80ms`, `all`, `transform, opacity`

- home: `0.3s ease-out`, `margin 0.3s ease-out, opacity 0.3s ease-out`, `transform 0.2s`, `transform 0.2s ease-in-out`, `300ms ease-in-out`

- sleep: `0.3s ease-out`, `margin 0.3s ease-out, opacity 0.3s ease-out`, `background 0.3s ease-out`, `opacity 0.3s ease-out`, `transform 0.3s ease-out`, `opacity 0.3s`, `transform 0.2s ease-in-out`
