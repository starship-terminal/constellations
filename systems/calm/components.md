# Calm components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from calm.com (plus the WordPress health.calm.com B2B surface) on 2026-11-16, signed out, in headed Chromium under Xvfb at 1440 x 900 (the Mobile group at 390 x 844; PerimeterX refuses the headless and emulated-touch fingerprints), with computed styles read from the running page. Nothing was signed into, bought or submitted; the login card was opened by its own button and never filled or submitted, and the signup flow was reached by its own button and never submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (50 components, 130 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (129 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: the marketing pages paint `light`, the app-shell pages `dark`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [login](screenshots/home-light-login.png) |
| Sleep (app shell) | `/app/sleep` | [default](screenshots/sleep-dark-default.png), [full](screenshots/sleep-dark-full.png) |
| Meditate (app shell) | `/app/meditate` | [default](screenshots/meditate-dark-default.png), [full](screenshots/meditate-dark-full.png) |
| Music (app shell) | `/app/music` | [default](screenshots/music-dark-default.png), [full](screenshots/music-dark-full.png) |
| Family | `/family` | [default](screenshots/family-light-default.png), [full](screenshots/family-light-full.png) |
| Gift | `/gift` | [default](screenshots/gift-light-default.png), [full](screenshots/gift-light-full.png) |
| Science | `/science` | [default](screenshots/science-light-default.png), [full](screenshots/science-light-full.png) |
| Mindfulness tips | `/mindfulness-tips` | [default](screenshots/mindfulness-light-default.png), [full](screenshots/mindfulness-light-full.png) |
| FAQ (Help Center) | `/faq/web` | [default](screenshots/faq-light-default.png), [full](screenshots/faq-light-full.png) |
| Blog | `blog.calm.com` |  |
| Calm Health (B2B) | `health.calm.com` | [default](screenshots/health-light-default.png), [full](screenshots/health-light-full.png) |
| Calm for Organizations | `health.calm.com/calm-for-organizations` | [default](screenshots/healthOrg-light-default.png), [full](screenshots/healthOrg-light-full.png) |
| Terms | `/terms` | [default](screenshots/terms-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the hamburger button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-nav-item) |
| Login card | home | the Log In button's own toggle, dismissed with Escape, never submitted | [home-light-login](screenshots/home-light-login.png), [login-dialog](#login-card) |
| Signup flow | home | the Try Calm for Free button navigates to /signup-flow; the landing stayed PerimeterX-blocked, never submitted | [signup-page](#signup-page), [signup-field](#signup-control) |
| Cookie-consent bar | every page | measured as a component, then hidden, never answered | [cookie-banner](#cookie-bar) |
| Signed-in product | the Calm app behind login | the /app/* preview is the signed-out boundary; playback, library and account live past login | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 27 components were given a real keyboard focus. 16 draw an outline ring: `h-cta` (2px solid #f8d22d, offset 0px), `h-card` (1px solid #eccd37, offset 0.9375px), `nav-link` (1px auto #101010, offset 0px), `nav-trigger` (1px auto #101010, offset 0px), `nav-login` (1px auto #101010, offset 0px), `rail-item` (1px auto #101010, offset 1px), `rail-item-active` (1px auto #101010, offset 1px), `topbar-search` (1px auto #101010, offset 1px), `tab-active` (1px auto #101010, offset 1px), `tab` (1px auto #101010, offset 1px), `content-card` (1px auto #101010, offset 0px), `see-all` (1px auto #101010, offset 1px), `med-card` (1px auto #101010, offset 0px), `footer-link` (1px auto #101010, offset 1px), `social-icon` (1px auto #101010, offset 0px), `m-nav-item` (1px auto #101010, offset 0px). 2 change fill instead: `h-nav-link`, `h-mega-trigger`. The other 9 show no measured change: `nav-cta`, `hero-cta`, `learn-more`, `d-login`, `d-cta`, `carousel-arrow`, `login-email-btn`, `login-social-btn`, `signup-button`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `ease` | all | h-nav |
| 0.3s | `ease` | opacity | content-card, med-card |
| 0.3s | `ease-in` | background-position-y | h-cta |
| 0.3s | `ease-in-out` | all | cookie-banner |
| 0.3s | `ease-out` | all | carousel-arrow, d-cta, d-login, dialog-close, footer-link, hero-cta, learn-more, login-email-btn and more |
| 0.5s | `ease` | all | h-card |
| 0.5s | `ease-out` | all | login-dialog |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Login card](#login-card) | 544 x 596 | 1px solid #ffffff `color.neutral.paper` | 16px | #ffffff `color.neutral.paper` | rgba(0, 0, 0, 0.25) 0px 8px 24px 0px | 0 |
| [Content card](#content-card) | 300 x 256 | - | - | transparent | none | 0 |
| [Meditate card](#meditate-card) | 300 x 256 | - | - | transparent | none | 0 |
| [Health card](#health-card) | 378.66 x 119.34 | 2px solid transparent | 12px | #ffffff `color.neutral.paper` | rgba(0, 0, 0, 0.08) 0px 2px 12px 0px | 0 |
| [Upsell banner](#upsell-banner) | 1153 x 76 | 2px solid rgba(255, 255, 255, 0.1) `color.app.raised` | 16px | rgba(255, 255, 255, 0.1) `color.app.raised` | none | 18px 20px |
| [Signup bar](#signup-bar) | 1425 x 92 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The transparent marketing header over the hero photograph: app-icon logo, section links and the Calm Health dropdown, Log In and the white Try-Calm-for-Free pill, plus the cookie-consent bottom sheet (measured, then hidden, never answered).

#### Cookie bar
The consent bottom sheet ("Cookie Preferences"), measured then hidden and never answered — no consent choice is ever made. Read as `cookie-banner` on the home page.

**Values (default).** size 1425 x 147; padding 24px 16px; border T: 1px solid #aaaaaa `color.neutral.hairline`; background #f7f7f7 `color.neutral.field`; text Figtree 18/18 700, #383838 `color.neutral.on-paper`; transition all 0.3s ease-in-out; icon 26 x 26, #ffffff `color.neutral.paper`.

![Cookie bar default](components/crops/cookie-banner-default.png)

#### Header
The transparent marketing header over the hero photograph: app-icon logo, the Sleep/Stress & Anxiety/Mindfulness links, Screening, the Calm Health dropdown, Log In and the Try-Calm-for-Free pill. Read as `header` on the home page.

**Values (default).** size 1425 x 100; padding 0px 40px; background transparent; image linear-gradient(#176293 0%, rgba(23, 98, 147, 0.337) 71%, rgba(23, 98, 147, 0) 100%); text Figtree 18/normal 700, #ffffff `color.neutral.paper`; icon 56 x 56, #ffffff `color.neutral.paper`; layers ::after rgb(255, 255, 255) 0px none 0.

![Header default](components/crops/header-default.png)

#### Logo
The rounded-square app icon anchor (the #60B4E7->#6461E0 gradient tile with the white wordmark inside). Read as `logo` on the home page.

**Values (default).** size 76 x 60; padding 14px 17.7778px; radius 100px; background transparent; text Figtree 18/28 500, #ffffff `color.neutral.paper`; transition all 0.3s ease-out; icon 56 x 56, #ffffff `color.neutral.paper`; layers ::before rgba(0, 0, 0, 0.15) 0px none 0; ::after rgba(0, 0, 0, 0) 2px none 0; a::before.styles__Wrapper-sc-7193a2d7-0.DOxGo 76pxx60px rgba(0, 0, 0, 0.15) 100px; a::after.styles__Wrapper-sc-7193a2d7-0.DOxGo 76pxx60px T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) / L:2px solid rgb(255, 255, 255) 100px.

Child layers that carry the look: a::before 76pxx60px background rgba(0, 0, 0, 0.15) radius 100px; a::after 76pxx60px border 2px solid #ffffff `color.neutral.paper` radius 100px.

![Logo default](components/crops/logo-default.png)

#### Nav item
A plain header item (Sleep, Mindfulness or Screening) — a styled-components button that opens a section panel, not an anchor. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 46.13 x 22; background transparent; text Figtree 18/normal 700, #ffffff `color.neutral.paper`; transition all 0.3s ease-out |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.styles__Wrapper-sc-2baa1e83-0.dnpxvL 46.1x22.0 1px auto rgb(16, 16, 16) offset 0px |

![Nav item default](components/crops/nav-link-default.png) ![Nav item hover](components/crops/nav-link-hover.png) ![Nav item focus-visible](components/crops/nav-link-focus-visible.png) ![Nav item pressed](components/crops/nav-link-pressed.png)

#### Nav trigger
The Calm Health chevron that opens the dropdown panel; toggled, never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 120.05 x 22; background transparent; text Figtree 18/normal 700, #ffffff `color.neutral.paper`; transition all 0.3s ease-out; icon 10 x 6, #ffffff `color.neutral.paper` |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.styles__Trigger-sc-7676a001-1.lnwsMr 120.0x22.0 1px auto rgb(16, 16, 16) offset 0px |

![Nav trigger default](components/crops/nav-trigger-default.png) ![Nav trigger hover](components/crops/nav-trigger-hover.png) ![Nav trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav trigger pressed](components/crops/nav-trigger-pressed.png)

#### Nav login
The header Log In button; pressing it opens the login card, measured under login-dialog, never submitted. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 50.66 x 22; background transparent; text Figtree 18/normal 700, #ffffff `color.neutral.paper`; transition all 0.3s ease-out |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.styles__Wrapper-sc-2baa1e83-0.dnpxvL 50.7x22.0 1px auto rgb(16, 16, 16) offset 0px |

![Nav login default](components/crops/nav-login-default.png) ![Nav login hover](components/crops/nav-login-hover.png) ![Nav login focus-visible](components/crops/nav-login-focus-visible.png) ![Nav login pressed](components/crops/nav-login-pressed.png)

#### Nav CTA
The white Try-Calm-for-Free header pill; pressing it opens the signup flow (the page measured under signup-), never submitted. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 200 x 56; padding 14px 17.7778px; radius 100px; background #ffffff `color.neutral.paper`; text Figtree 18/28 700, #383838 `color.neutral.on-paper`; transition all 0.3s ease-out; layers ::before rgba(0, 0, 0, 0.15) 0px none 0; ::after rgba(0, 0, 0, 0) 2px none 0 |
| hover | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 0 |
| focus-visible | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 1 |
| pressed | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 0 |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

### Home

The navy hero over the lake photograph, the Try-Calm-for-Free action and the Learn-More sections.

#### Hero headline
The navy "Calm your mind. Change your life." headline. Read as `hero-title` on the home page.

**Values (default).** size 768.69 x 74.25; background transparent; text Figtree 49.5/74.25 700, #1a3e6f `color.neutral.ink`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero copy
The lede under the headline. Read as `hero-sub` on the home page.

**Values (default).** size 768.69 x 28; background transparent; text Figtree 22.5/28 500, rgba(0, 0, 0, 0.8) `color.neutral.muted`.

![Hero copy default](components/crops/hero-sub-default.png)

#### Hero CTA
The navy hero action; measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 335 x 58; padding 14px 17.7778px; radius 100px; background transparent; image linear-gradient(#2477aa `color.brand.blue` 0%, #6461e0 `color.brand.violet` 100%); text Figtree 18/28 700, #ffffff `color.neutral.paper`; transition all 0.3s ease-out; layers ::before rgba(0, 0, 0, 0.15) 0px none 0; ::after rgba(0, 0, 0, 0) 2px none 0 |
| hover | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 0 |
| focus-visible | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 1 |
| pressed | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 0 |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Section card link
A marketing section card (Stress less. / Sleep more. / Live mindfully.) — a button carrying the heading, copy and Learn-more label; measured never followed. Read as `learn-more` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 352.33 x 247; background transparent; text Figtree 31.5/48 500, rgba(0, 0, 0, 0.8) `color.neutral.muted`; transition all 0.3s ease-out; icon 54 x 54, #000000 `color.neutral.link`; layers ::after rgba(0, 0, 0, 0) 2px none 0; button::after.styles__Wrapper-sc-2baa1e83-0.byLhOR 352.328pxx247px T:2px solid rgb(23, 98, 147) / R:2px solid rgb(23, 98, 147) / B:2px solid rgb(23, 98, 147) / L:2px solid rgb(23, 98, 147) 20px |
| hover | text Figtree 31.5/48 500, #176293 |
| focus-visible | layers ::after rgba(0, 0, 0, 0) 2px none 1; button::after.styles__Wrapper-sc-2baa1e83-0.byLhOR 352.328pxx247px T:2px solid rgb(23, 98, 147) / R:2px solid rgb(23, 98, 147) / B:2px solid rgb(23, 98, 147) / L:2px solid rgb(23, 98, 147) 20px |
| pressed | text Figtree 31.5/48 500, #176293 |

Child layers that carry the look: button::after 352.328pxx247px border 2px solid #176293 radius 20px.

![Section card link default](components/crops/learn-more-default.png) ![Section card link hover](components/crops/learn-more-hover.png) ![Section card link focus-visible](components/crops/learn-more-focus-visible.png) ![Section card link pressed](components/crops/learn-more-pressed.png)

#### Section heading
A marketing section heading (Stress less. / Sleep more. / Live mindfully.). Read as `section-h2` on the home page.

**Values (default).** size 1153 x 60; background transparent; text Figtree 36/60 700, #1a3e6f `color.neutral.ink`.

![Section heading default](components/crops/section-h2-default.png)

### App shell (dark)

The signed-out /app/* preview of the real product: the dark left rail, category pill tabs, featured content rails, the gradient upsell bar and the bottom signup bar.

#### App rail
The dark left rail: wordmark, Home/Meditate/Sleep/Music/For Work/Wisdom/Calm Kids/Movement/Profile icon items. Read as `rail` on the sleep (app shell) page.

**Values (default).** size 240 x 900; padding 40px 24px; background rgba(0, 0, 0, 0.3) `color.app.rail`; text Figtree 18/normal 400, #ffffff `color.neutral.paper`; icon 48 x 48, #000000 `color.neutral.link`.

![App rail default](components/crops/rail-default.png)

#### Rail item
An icon-plus-label rail link. Read as `rail-item` on the sleep (app shell) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 192 x 48; background transparent; text Figtree 18/normal 400, #ffffff `color.neutral.paper`; icon 48 x 48, #000000 `color.neutral.link` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.styles__Wrapper-sc-f7711adb-2.FoZvx 192.0x48.0 1px auto rgb(16, 16, 16) offset 1px |

![Rail item default](components/crops/rail-item-default.png) ![Rail item hover](components/crops/rail-item-hover.png) ![Rail item focus-visible](components/crops/rail-item-focus-visible.png) ![Rail item pressed](components/crops/rail-item-pressed.png)

#### Rail item, selected
The selected Sleep rail item (its icon tile filled). Read as `rail-item-active` on the sleep (app shell) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 192 x 48; background transparent; text Figtree 18/normal 700, #ffffff `color.neutral.paper`; icon 48 x 48, #000000 `color.neutral.link` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.styles__Wrapper-sc-f7711adb-2.dEwIdS 192.0x48.0 1px auto rgb(16, 16, 16) offset 1px |

![Rail item, selected default](components/crops/rail-item-active-default.png) ![Rail item, selected hover](components/crops/rail-item-active-hover.png) ![Rail item, selected focus-visible](components/crops/rail-item-active-focus-visible.png) ![Rail item, selected pressed](components/crops/rail-item-active-pressed.png)

#### Search link
The top-bar search icon link to /app/search (the wide search field only paints inside the search page); never followed. Read as `topbar-search` on the sleep (app shell) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 48 x 48; radius 50%; background rgba(255, 255, 255, 0.1) `color.app.raised`; text Figtree 16/normal 400, #000000 `color.neutral.link`; transition all 0.3s ease-out; icon 48 x 48, #000000 `color.neutral.link` |
| focus-visible | outline 1px auto #101010, offset 1px |

![Search link default](components/crops/topbar-search-default.png) ![Search link hover](components/crops/topbar-search-hover.png) ![Search link focus-visible](components/crops/topbar-search-focus-visible.png) ![Search link pressed](components/crops/topbar-search-pressed.png)

#### Dark login
The dark shell's translucent Log In pill (the shell paints no header element); opens the same login card, never submitted. Read as `d-login` on the sleep (app shell) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85.5 x 56; padding 14px 17.7778px; radius 100px; background rgba(255, 255, 255, 0.1) `color.app.raised`; text Figtree 18/28 500, #ffffff `color.neutral.paper`; transition all 0.3s ease-out; layers ::before rgba(0, 0, 0, 0.15) 0px none 0; ::after rgba(0, 0, 0, 0) 2px none 0 |
| hover | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 0 |
| focus-visible | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 1 |
| pressed | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 0 |

![Dark login default](components/crops/d-login-default.png) ![Dark login hover](components/crops/d-login-hover.png) ![Dark login focus-visible](components/crops/d-login-focus-visible.png) ![Dark login pressed](components/crops/d-login-pressed.png)

#### Dark CTA
The white Try-Calm-for-Free pill on the dark top bar; opens the signup flow, never submitted. Read as `d-cta` on the sleep (app shell) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 174.86 x 56; padding 14px 17.7778px; radius 100px; background #ffffff `color.neutral.paper`; text Figtree 18/28 500, #000000 `color.neutral.link`; transition all 0.3s ease-out; layers ::before rgba(0, 0, 0, 0.15) 0px none 0; ::after rgba(0, 0, 0, 0) 2px none 0 |
| hover | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 0 |
| focus-visible | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 1 |
| pressed | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 0 |

![Dark CTA default](components/crops/d-cta-default.png) ![Dark CTA hover](components/crops/d-cta-hover.png) ![Dark CTA focus-visible](components/crops/d-cta-focus-visible.png) ![Dark CTA pressed](components/crops/d-cta-pressed.png)

#### Tab, selected
The selected white category pill (Sleep Stories/All). Read as `tab-active` on the sleep (app shell) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 138.5 x 26; padding 2px 16px; radius 100px; background #ffffff `color.neutral.paper`; text Figtree 18/normal 400, #002152 `color.app.active-ink` |
| focus-visible | outline 1px auto #101010, offset 1px |

![Tab, selected default](components/crops/tab-active-default.png) ![Tab, selected hover](components/crops/tab-active-hover.png) ![Tab, selected focus-visible](components/crops/tab-active-focus-visible.png) ![Tab, selected pressed](components/crops/tab-active-pressed.png)

#### Tab
An unselected dark category pill. Read as `tab` on the sleep (app shell) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 127.59 x 26; padding 2px 16px; radius 100px; background rgba(0, 0, 0, 0.3) `color.app.rail`; text Figtree 18/normal 400, #ffffff `color.neutral.paper` |
| focus-visible | outline 1px auto #101010, offset 1px |

![Tab default](components/crops/tab-default.png) ![Tab hover](components/crops/tab-hover.png) ![Tab focus-visible](components/crops/tab-focus-visible.png) ![Tab pressed](components/crops/tab-pressed.png)

#### Upsell banner
The subscribe upsell bar ("You're missing out on the full Calm experience. Subscribe with 40% off ...") — the whole banner is one anchor. Read as `upsell` on the sleep (app shell) page.

**Values (default).** size 1153 x 76; padding 18px 20px; border 2px solid rgba(255, 255, 255, 0.1) `color.app.raised`; radius 16px; background rgba(255, 255, 255, 0.1) `color.app.raised`; text Figtree 18/28 500, #ffffff `color.neutral.paper`; icon 36 x 24, #000000 `color.neutral.link`.

![Upsell banner default](components/crops/upsell-default.png)

#### Content card
A featured-story card: artwork tile, "New" badge, title and narrator. Read as `content-card` on the sleep (app shell) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 300 x 256; background transparent; text Figtree 10/12 500, #000000 `color.neutral.link`; transition opacity 0.3s ease; icon 16 x 16, #000000 `color.neutral.link`; layers div.styles__ImageWrapper-sc-746cd660-2.gWtqsq 300.0x200.0 rgba(0, 0, 0, 0.2) 0px 4px 12px 0px 16px; div.styles__LockBadge-sc-f065fab4-0.kwtavd 28.0x28.0 rgba(72, 72, 72, 0.4) 50%; div.styles__NewTag-sc-746cd660-1.gFRvzb 33.0x20.0 rgb(255, 255, 255) 999px |
| focus-visible | outline 1px auto #101010, offset 0px; layers a.styles__CardContainer-sc-746cd660-4.gMsfOt 300.0x256.0 1px auto rgb(16, 16, 16) offset 0px; div.styles__ImageWrapper-sc-746cd660-2.gWtqsq 300.0x200.0 rgba(0, 0, 0, 0.2) 0px 4px 12px 0px 16px; div.styles__LockBadge-sc-f065fab4-0.kwtavd 28.0x28.0 rgba(72, 72, 72, 0.4) 50%; div.styles__NewTag-sc-746cd660-1.gFRvzb 33.0x20.0 rgb(255, 255, 255) 999px |

Child layers that carry the look: div 300x200 radius 16px shadow rgba(0, 0, 0, 0.2) 0px 4px 12px 0px; div 28x28 background rgba(72, 72, 72, 0.4) `color.app.card-scrim` radius 50%; div 33x20 background #ffffff `color.neutral.paper` radius 999px.

![Content card default](components/crops/content-card-default.png) ![Content card hover](components/crops/content-card-hover.png) ![Content card focus-visible](components/crops/content-card-focus-visible.png) ![Content card pressed](components/crops/content-card-pressed.png)

#### New badge
The white "New" chip on a card's artwork. Read as `card-badge` on the sleep (app shell) page.

**Values (default).** size 33.05 x 20; padding 4px 6px; radius 999px; background #ffffff `color.neutral.paper`; text Figtree 10/12 500, #000000 `color.neutral.link`.

![New badge default](components/crops/card-badge-default.png)

#### See All
A section "See All" link with its chevron. Read as `see-all` on the sleep (app shell) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 81.27 x 22; background transparent; text Figtree 18/normal 400, #ffffff `color.neutral.paper`; icon 24 x 20, #ffffff `color.neutral.paper` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.styles__Wrapper-sc-dea8a0a4-0.ejjkYV 81.3x22.0 1px auto rgb(16, 16, 16) offset 1px |

![See All default](components/crops/see-all-default.png) ![See All hover](components/crops/see-all-hover.png) ![See All focus-visible](components/crops/see-all-focus-visible.png) ![See All pressed](components/crops/see-all-pressed.png)

#### Carousel arrow
A rail carousel arrow (the "Scroll carousel towards next items" chevron). Read as `carousel-arrow` on the sleep (app shell) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 100px; background rgba(0, 0, 0, 0.4); text Figtree 18/28 500, #ffffff `color.neutral.paper`; transition all 0.3s ease-out; transform matrix(-1, 0, 0, -1, 0, 0); icon 26 x 20, #ffffff `color.neutral.paper`; layers ::before rgba(0, 0, 0, 0.15) 0px none 0; ::after rgba(0, 0, 0, 0) 2px none 0 |
| hover | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 0 |
| focus-visible | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 1 |
| pressed | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 0 |

![Carousel arrow default](components/crops/carousel-arrow-default.png) ![Carousel arrow hover](components/crops/carousel-arrow-hover.png) ![Carousel arrow focus-visible](components/crops/carousel-arrow-focus-visible.png) ![Carousel arrow pressed](components/crops/carousel-arrow-pressed.png)

#### Signup bar
The bottom notification bar ("Get notified of new Calm content ...") — a full-width anchor carrying the Sign-up-today gradient pill; never submitted. Read as `signup-bar` on the sleep (app shell) page.

**Values (default).** size 1425 x 92; background transparent; image linear-gradient(113.79deg, #f1f5fe 7.89%, #c7def8 33%, #d9ecf6 62.5%, #f1f5fe 100%); text Figtree 18/28 500, #000000 `color.neutral.link`.

![Signup bar default](components/crops/signup-bar-default.png)

#### Section title
The page title of an app-shell section (Meditate). Read as `med-title` on the meditate (app shell) page.

**Values (default).** size 1153 x 40; background transparent; text Figtree 31.5/40 400, #ffffff `color.neutral.paper`.

![Section title default](components/crops/med-title-default.png)

#### Meditate card
A featured content card on the Meditate surface (the shared CardContainer: artwork, title, narrator). Read as `med-card` on the meditate (app shell) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 300 x 256; background transparent; text Figtree 13/16.9 600, #ffffff `color.neutral.paper`; transition opacity 0.3s ease; icon 16 x 16, #000000 `color.neutral.link`; layers div.styles__ImageWrapper-sc-746cd660-2.gWtqsq 300.0x200.0 rgba(0, 0, 0, 0.2) 0px 4px 12px 0px 16px; div.styles__LockBadge-sc-f065fab4-0.kwtavd 28.0x28.0 rgba(72, 72, 72, 0.4) 50% |
| focus-visible | outline 1px auto #101010, offset 0px; layers a.styles__CardContainer-sc-746cd660-4.gMsfOt 300.0x256.0 1px auto rgb(16, 16, 16) offset 0px; div.styles__ImageWrapper-sc-746cd660-2.gWtqsq 300.0x200.0 rgba(0, 0, 0, 0.2) 0px 4px 12px 0px 16px; div.styles__LockBadge-sc-f065fab4-0.kwtavd 28.0x28.0 rgba(72, 72, 72, 0.4) 50% |

Child layers that carry the look: div 300x200 radius 16px shadow rgba(0, 0, 0, 0.2) 0px 4px 12px 0px; div 28x28 background rgba(72, 72, 72, 0.4) `color.app.card-scrim` radius 50%.

![Meditate card default](components/crops/med-card-default.png) ![Meditate card hover](components/crops/med-card-hover.png) ![Meditate card focus-visible](components/crops/med-card-focus-visible.png) ![Meditate card pressed](components/crops/med-card-pressed.png)

#### Signup button
The gradient Sign-up-today button (pill-shaped) in the bottom bar; never pressed for real. Read as `signup-button` on the sleep (app shell) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 147.89 x 56; padding 14px 17.7778px; radius 100px; background transparent; image linear-gradient(#2477aa `color.brand.blue` 0%, #6461e0 `color.brand.violet` 100%); text Figtree 18/28 500, #ffffff `color.neutral.paper`; transition all 0.3s ease-out; layers ::before rgba(0, 0, 0, 0.15) 0px none 0; ::after rgba(0, 0, 0, 0) 2px none 0 |
| hover | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 0 |
| focus-visible | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 1 |
| pressed | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 0 |

![Signup button default](components/crops/signup-button-default.png) ![Signup button hover](components/crops/signup-button-hover.png) ![Signup button focus-visible](components/crops/signup-button-focus-visible.png) ![Signup button pressed](components/crops/signup-button-pressed.png)

### Login and signup

The modal auth card the Log In button opens (Log into your account) and the /signup-flow page Try Calm for Free navigates to, each reached by its own button and never submitted.

#### Login card
The white "Log into your account" modal card over a dimmed blur backdrop; opened by its own Log In button, never submitted. Read as `login-dialog` on the home page.

**Values (default).** size 544 x 596; border 1px solid #ffffff `color.neutral.paper`; radius 16px; background #ffffff `color.neutral.paper`; shadow rgba(0, 0, 0, 0.25) 0px 8px 24px 0px; text Figtree 31.5/48 500, #000000 `color.neutral.link`; transition all 0.5s ease-out; icon 26 x 26, #ffffff `color.neutral.paper`.

![Login card default](components/crops/login-dialog-default.png)

#### Sign-in primary
The navy Sign-in-with-Email pill inside the login card; never pressed for real. Read as `login-email-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 462 x 56; padding 14px 17.7778px 14px 19.8519px; border 1px solid #1a3e6f `color.neutral.ink`; radius 100px; background #1a3e6f `color.neutral.ink`; text Figtree 18/28 500, #ffffff `color.neutral.paper`; transition all 0.3s ease-out; icon 26 x 26, #ffffff `color.neutral.paper`; layers ::before rgba(0, 0, 0, 0.15) 0px none 0; ::after rgba(0, 0, 0, 0) 2px none 0 |
| hover | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 0 |
| focus-visible | layers ::before rgba(0, 0, 0, 0.15) 0px none 0.994495; ::after rgba(0, 0, 0, 0) 2px none 0.994495 |
| pressed | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 0 |

![Sign-in primary default](components/crops/login-email-btn-default.png) ![Sign-in primary hover](components/crops/login-email-btn-hover.png) ![Sign-in primary focus-visible](components/crops/login-email-btn-focus-visible.png) ![Sign-in primary pressed](components/crops/login-email-btn-pressed.png)

#### Sign-in social
A white outline social sign-in pill; never pressed for real. Read as `login-social-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 462 x 56; padding 14px 17.7778px; border 1px solid #aaaaaa `color.neutral.hairline`; radius 100px; background #ffffff `color.neutral.paper`; text Figtree 18/28 500, #000000 `color.neutral.link`; transition all 0.3s ease-out; icon 30 x 30, #000000 `color.neutral.link`; layers ::before rgba(0, 0, 0, 0.15) 0px none 0; ::after rgba(0, 0, 0, 0) 2px none 0 |
| hover | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 0 |
| focus-visible | layers ::before rgba(0, 0, 0, 0.15) 0px none 0.979264; ::after rgba(0, 0, 0, 0) 2px none 0.979264 |
| pressed | layers ::before rgba(0, 0, 0, 0.15) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 0 |

![Sign-in social default](components/crops/login-social-btn-default.png) ![Sign-in social hover](components/crops/login-social-btn-hover.png) ![Sign-in social focus-visible](components/crops/login-social-btn-focus-visible.png) ![Sign-in social pressed](components/crops/login-social-btn-pressed.png)

#### Dialog close
The X close control of the login card. Read as `dialog-close` on the home page.

**Values (default).** size 48 x 36; padding 14px 17.7778px; radius 100px; background transparent; text Figtree 18/28 500, #ffffff `color.neutral.paper`; transition all 0.3s ease-out; icon 16 x 16, #ffffff `color.neutral.paper`; layers ::before rgba(0, 0, 0, 0.15) 0px none 0; ::after rgba(0, 0, 0, 0) 2px none 0; button::before.styles__Wrapper-sc-7193a2d7-0.bVnmXP 48pxx36px rgba(0, 0, 0, 0.15) 100px; button::after.styles__Wrapper-sc-7193a2d7-0.bVnmXP 48pxx36px T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) / L:2px solid rgb(255, 255, 255) 100px.

Child layers that carry the look: button::before 48pxx36px background rgba(0, 0, 0, 0.15) radius 100px; button::after 48pxx36px border 2px solid #ffffff `color.neutral.paper` radius 100px.

![Dialog close default](components/crops/dialog-close-default.png)

#### Signup control
The first interactive control on the signup landing page; never pressed for real. Read as `signup-field` on the home page.

Not on the page when it was captured.

#### Signup page
The page the Try-Calm-for-Free button navigates to (/signup-flow?source=homepage) — the signup flow's first step, reached by its own button and never submitted; its landing stayed PerimeterX-blocked this run. Read as `signup-page` on the home page.

Not captured: the page served a PerimeterX bot check ("Press & Hold to confirm you are a human") instead of this view, so the reading is the challenge container, not the product. It is left out here and needs a recapture.

### Calm Health (B2B)

The WordPress B2B surface on health.calm.com: header megamenu, employer hero, cards and footer.

#### Health nav
The WordPress B2B header menu (Solutions/Resources megamenus, Log In, contact CTA). Read as `h-nav` on the health.calm.com page.

**Values (default).** size 1425 x 98; background transparent; text Figtree 16/24 400, #1a1b1f; transition all 0.2s ease; layers div.main-menu__wrapper 1425.0x105.0 B:1px solid rgba(0, 0, 0, 0); ul.main-menu__submenu 0.0x0.0 rgb(255, 255, 255); ul.main-menu__submenu 0.0x0.0 rgb(255, 255, 255); ul.main-menu__submenu 0.0x0.0 rgb(255, 255, 255); ul.main-menu__submenu 0.0x0.0 rgb(255, 255, 255); button.btn.btn--primary 150.8x41.0 100px.

Child layers that carry the look: div 1425x105 border 1px solid transparent; ul 0x0 background #ffffff `color.neutral.paper`; ul 0x0 background #ffffff `color.neutral.paper`.

![Health nav default](components/crops/h-nav-default.png)

#### Health nav link
A top-level B2B nav link. Read as `h-nav-link` on the health.calm.com page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 90.41 x 99; padding 40px 16px; background transparent; text Figtree 16/normal 400, #1a1b1f |
| focus-visible | background rgba(47, 126, 206, 0.4) |

![Health nav link default](components/crops/h-nav-link-default.png) ![Health nav link hover](components/crops/h-nav-link-hover.png) ![Health nav link focus-visible](components/crops/h-nav-link-focus-visible.png) ![Health nav link pressed](components/crops/h-nav-link-pressed.png)

#### Megamenu trigger
A menu item that opens a megamenu panel; toggled, never followed. Read as `h-mega-trigger` on the health.calm.com page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 119.77 x 104; padding 40px 26.4px; background transparent; text Figtree 16/24 400, #1a1b1f |
| focus-visible | background rgba(47, 126, 206, 0.4) |

![Megamenu trigger default](components/crops/h-mega-trigger-default.png) ![Megamenu trigger hover](components/crops/h-mega-trigger-hover.png) ![Megamenu trigger focus-visible](components/crops/h-mega-trigger-focus-visible.png) ![Megamenu trigger pressed](components/crops/h-mega-trigger-pressed.png)

#### Health hero
The B2B hero headline. Read as `h-hero` on the health.calm.com page.

**Values (default).** size 411.52 x 240.75; background transparent; text Figtree 56/60.2 400, #00458e.

![Health hero default](components/crops/h-hero-default.png)

#### Health CTA
The B2B contact/action button; measured never followed. Read as `h-cta` on the health.calm.com page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 150.78 x 41; padding 12px 24px; radius 100px; background transparent; image linear-gradient(0deg, #4e4bb1 0px, #6461e0 `color.brand.violet` 49%, #60b4e7 100%); text Figtree 14/normal 600, #ffffff `color.neutral.paper`; transition background-position-y 0.3s ease-in |
| focus-visible | outline 2px solid #f8d22d, offset 0px |

![Health CTA default](components/crops/h-cta-default.png) ![Health CTA hover](components/crops/h-cta-hover.png) ![Health CTA focus-visible](components/crops/h-cta-focus-visible.png) ![Health CTA pressed](components/crops/h-cta-pressed.png)

#### Health card
A card on the B2B surface (customer story, benefit or resource card). Read as `h-card` on the health.calm.com page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 378.66 x 119.34; border 2px solid transparent; radius 12px; background #ffffff `color.neutral.paper`; shadow rgba(0, 0, 0, 0.08) 0px 2px 12px 0px; text Figtree 24.8/32.24 600, #1a1b1f; transition all 0.5s ease |
| hover | size 378.66 x 180.92; border 2px solid rgba(96, 180, 231, 0.996); text Figtree 24.8/32.24 600, #2f7dcd |
| focus-visible | outline 1px solid #eccd37, offset 0.9375px |
| pressed | size 378.66 x 180.92; border 2px solid rgba(96, 180, 231, 0.965); text Figtree 24.8/32.24 600, #2e7bc8 |

![Health card default](components/crops/h-card-default.png) ![Health card hover](components/crops/h-card-hover.png) ![Health card focus-visible](components/crops/h-card-focus-visible.png) ![Health card pressed](components/crops/h-card-pressed.png)

#### Health footer
The B2B footer. Read as `h-footer` on the health.calm.com page.

**Values (default).** size 1425 x 459.23; background transparent; text Figtree 16/normal 600, #1a1b1f; layers hr 1200.0x1.0 B:1px solid rgb(243, 242, 242).

Child layers that carry the look: hr 1200x1 border 1px solid #f3f2f2.

![Health footer default](components/crops/h-footer-default.png)

### Footer

The marketing footer: link columns, social icons, legal.

#### Footer
The marketing footer: link columns, social icons, legal. Read as `footer` on the home page.

**Values (default).** size 1425 x 524; padding 48px 0px; background #1b2250 `color.neutral.footer-panel`; text Figtree 18/28 500, #ffffff `color.neutral.paper`; icon 18 x 18, #000000 `color.neutral.link`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44.47 x 19; background transparent; text Figtree 16/30 400, #ffffff `color.neutral.paper`; transition all 0.3s ease-out; opacity 0.8 |
| hover | opacity 0.5 |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.styles__FooterItem-sc-523c7602-4.cTpfxy 44.5x19.0 1px auto rgb(16, 16, 16) offset 1px |
| pressed | opacity 0.5 |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social icon
A social icon link in the footer (Facebook/Instagram/Twitter); the footer carries no app-store badges. Read as `social-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 18 x 19; background transparent; text Figtree 16/normal 400, #000000 `color.neutral.link`; opacity 0.8; icon 18 x 18, #000000 `color.neutral.link` |
| focus-visible | outline 1px auto #101010, offset 0px; layers a.styles__SocialIcon-sc-523c7602-7.cNDlHA 18.0x19.0 1px auto rgb(16, 16, 16) offset 0px |

![Social icon default](components/crops/social-icon-default.png) ![Social icon hover](components/crops/social-icon-hover.png) ![Social icon focus-visible](components/crops/social-icon-focus-visible.png) ![Social icon pressed](components/crops/social-icon-pressed.png)

### Mobile (390 wide)

The marketing surface at phone width: slimmer header, the hamburger menu, smaller display type.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 375 x 64; padding 0px 16px; background transparent; image linear-gradient(#176293 0%, rgba(23, 98, 147, 0.337) 71%, rgba(23, 98, 147, 0) 100%); text Figtree 16/28 700, #383838 `color.neutral.on-paper`; layers ::after rgb(255, 255, 255) 0px none 0.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The hamburger menu toggle (aria-label "Open Mobile menu"). Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 48 x 48; radius 100px; background transparent; text Figtree 16/normal 400, #000000 `color.neutral.link`; transition all 0.3s ease-out; layers ::before rgba(0, 0, 0, 0.15) 0px none 0; ::after rgba(0, 0, 0, 0) 2px none 0; button::before.styles__Wrapper-sc-7193a2d7-0.feUdRs 48pxx48px rgba(0, 0, 0, 0.15) 100px; button::after.styles__Wrapper-sc-7193a2d7-0.feUdRs 48pxx48px T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) / L:2px solid rgb(255, 255, 255) 100px; div.styles__Line-sc-be7485e7-0.JgAY.

Child layers that carry the look: button::before 48pxx48px background rgba(0, 0, 0, 0.15) radius 100px; button::after 48pxx48px border 2px solid #ffffff `color.neutral.paper` radius 100px; div 32x2.5 background #ffffff `color.neutral.paper` radius 2.5px.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The full-screen nav panel (aria-label "Mobile navigation menu", fixed z:999) opened by the hamburger toggle. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 375 x 844; padding 64px 0px; background transparent; image linear-gradient(#60b4e7 0%, #6461e0 `color.brand.violet` 100%); text Figtree 24/normal 500, #ffffff `color.neutral.paper`; transition all 0.3s ease-out; icon 33 x 33, #ffffff `color.neutral.paper`; layers ::after rgba(0, 0, 0, 0.2) 0px none 1.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
A button inside the opened mobile menu (Sleep, Mindfulness or Screening — the same styled-components nav items as desktop). Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 60.7 x 29; background transparent; text Figtree 24/normal 500, #ffffff `color.neutral.paper`; transition all 0.3s ease-out |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.styles__Wrapper-sc-2baa1e83-0.dnpxvL 60.7x29.0 1px auto rgb(16, 16, 16) offset 0px |

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 250 x 72; background transparent; text Figtree 24/36 700, #1a3e6f `color.neutral.ink`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Calm app-icon logo, the rail nav's rainbow glyphs, content thumbnails, the footer social icons) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The Calm product itself lives behind the login card, so playback, the home feed, library, check-ins, profile and the checkout all need an account and were never reached. The dark /app/sleep, /app/meditate and /app/music pages are the real product shell with its rail nav and content rails, served signed out as a preview; every locked card, See-All link and play button leads to signup. The login card was opened by its own button, measured and screenshotted, and never filled or submitted; Try Calm for Free navigates to /signup-flow, whose landing stayed PerimeterX-blocked this run.

### Pages

- **The signed-in product.** Every post-login surface (home feed, player, library, profile) was never reached; the login card was captured and never filled or submitted.
- **Checkout and signup.** The signup flow was reached by its own button and measured as far as the gate allowed; its Continue/checkout actions were never followed.
- **PerimeterX.** calm.com sits behind PerimeterX; several pages blocked the capture browser outright and are listed as not captured in the README coverage table rather than inferred.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **Locked-card states.** Every content card in the /app/* rails is already in its signed-out (locked) state; unlocked states need an account.

### Themes

The site paints two surfaces rather than a theme toggle: the marketing pages are light-only and the /app/* preview shell is dark-only. tokens.json keeps the app-shell roles in the dark set.

### Fonts

- **Figtree** is the rendered family across the marketing pages, the app shell and the B2B surface (300–700 served from the Next.js bundle; ITC Souvenir and Neue Plak faces serve alongside but paint nowhere measured). It is served from the Calm CDN; the style guide falls back to system sans.

### Screenshots

- The lake/mountain photography, content artwork, narrator portraits and the Calm logo in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Program copy, meditation/session titles beyond the visible rails and blog article text are the product's content; only frames and components were measured.
