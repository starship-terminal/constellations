# Dona components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from dona.ai on 2026-11-12, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, submitted or consented to; the email field was filled with sample text and cleared, the Watch video button's own modal was opened and hidden again, and the Login and Try for free routes to app.dona.ai were never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (40 components, 80 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 16/23.2 400, #19191b`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (77 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the public surface paints one light theme (the light/dark/black app UI themes live inside the product). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at the context's device scale (1x on the desktop pass, 2x on mobile); mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [cookies](screenshots/home-light-cookies.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [video](screenshots/home-light-video.png) |
| About | `/about` | [cookies](screenshots/about-light-cookies.png), [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Privacy policy | `/privacy-policy` | [cookies](screenshots/privacy-policy-light-cookies.png), [default](screenshots/privacy-policy-light-default.png), [full](screenshots/privacy-policy-light-full.png) |
| Terms of service | `/terms-of-service` | [cookies](screenshots/terms-of-service-light-cookies.png), [default](screenshots/terms-of-service-light-default.png), [full](screenshots/terms-of-service-light-full.png) |
| Home, phone | `/` | [cookies](screenshots/mobile-home-light-cookies.png), [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| About, phone | `/about` | [cookies](screenshots/mobile-about-light-cookies.png), [default](screenshots/mobile-about-light-default.png), [full](screenshots/mobile-about-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie banner | every page, first load | screenshotted as its own state, then hidden — the Accept button was never clicked | [home-light-cookies](screenshots/home-light-cookies.png) and every `*-cookies` shot |
| Video modal | home page | the Watch video button's own toggle — opened, screenshotted, measured and hidden again; the embed was never played | [home-light-video](screenshots/home-light-video.png), [video-modal](#video-modal), [modal-close](#modal-close) |
| Newsletter success | newsletter band | the 'Thank you! You're in.' copy sits in the form's DOM but only shows after a real submit — never submitted | not captured; boundary |
| Login / Try for free | header and hero | both open https://app.dona.ai — a different host and the app's sign-in | boundary; see Gaps |
| External socials | about and footer | twitter.com/getdona and the Discord invite are external links | never followed |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 10 components were given a real keyboard focus. 4 draw an outline ring: `cookie-learn` (1px auto #005fcc `measured.focus-outline`, offset 1px), `social-link` (1px auto #005fcc `measured.focus-outline`, offset 1px), `footer-link` (1px auto #005fcc `measured.focus-outline`, offset 1px), `footer-twitter` (1px auto #005fcc `measured.focus-outline`, offset 1px). The other 6 show no measured change: `cookie-accept`, `nav-about`, `nav-login`, `watch-video`, `try-cta`, `join-btn`. Focus could not be captured on 2 more (keyboard focus never landed on them, so their readings are left out): `logo`, `team-card`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): the pill buttons fall back to their resting fill when pressed (the hover grey is a :hover rule, so :active:hover reads as default), the grey chips keep stepping darker (#e0e3e7 → #dde0e4 → #dadde1), and the unstyled social/logo anchors pick up the UA :active link red #ff0000 — a browser default, not a Dona value. Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `ease` | background-color, box-shadow, color | cookie-accept, footer-twitter, join-btn, m-try, m-watch, modal-close, nav-about, nav-login and more |
| 0.25s | `ease` | background-color | join-btn |
| 0.3s | `ease` | opacity, padding | join-btn, video-modal |
| 1s | `cubic-bezier(0.17, 0.17, 0, 1)` | opacity, transform | about-h1, hero-h1, hero-lede, legal-h1, m-hero, mission-text |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Feature tile](#feature-tile) | 534 x 534 | - | 20px | #f4f4f5 `color.fill.tile` | none | 0px 0px 534px 0px |
| [Hero app frame](#hero-app-frame) | 1100 x 688.52 | - | 20px | #eff2f5 `color.fill.media` | rgba(12, 20, 66, 0.02) 0px 4px 12px 0px, rgba(12, 20, 66, 0.08) 0px 30px 80px 0px, #e6e9ed 0px 0px 0px 1px inset | 0 |
| [Team card](#team-card) | 286.66 x 330.05 | - | - | transparent | none | 0 |
| [Cookie banner](#cookie-banner) | 496.28 x 76 | - | 40px | #ffffff `color.neutral.paper` | rgba(12, 20, 66, 0.03) 0px 1px 3px 0px, rgba(12, 20, 66, 0.04) 0px 8px 16px 0px, rgba(12, 20, 66, 0.04) 0px 16px 40px 0px | 18px |
| [Newsletter form](#newsletter-form) | 1100 x 140 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The 68px header bar — the ghost About button, the centred ring-and-wordmark logo, the grey Login pill — and the cookie-consent card it shares the page with.

#### Cookie banner
The "This website uses cookies." consent notice (Learn more / Accept); measured, then hidden — Accept was never clicked. Read as `cookie-banner` on the home page.

**Values (default).** size 496.28 x 76; padding 18px; radius 40px; background #ffffff `color.neutral.paper`; shadow rgba(12, 20, 66, 0.03) 0px 1px 3px 0px, rgba(12, 20, 66, 0.04) 0px 8px 16px 0px, rgba(12, 20, 66, 0.04) 0px 16px 40px 0px; text Inter 16/23.2 400, #19191b `color.neutral.ink`; icon 40 x 40, #19191b `color.neutral.ink`.

![Cookie banner default](components/crops/cookie-banner-default.png)

#### Cookie "Learn more"
The Learn more link inside the cookie banner (to /privacy-policy); measured, never followed. Read as `cookie-learn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 85.63 x 23.19; background transparent; text Inter 16/23.2 400, #19191b `color.neutral.ink`; layers ::before rgb(25, 25, 27) 0px none 1; a::before 85.625pxx1px rgb(25, 25, 27) |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers ::before rgb(25, 25, 27) 0px none 1; a 85.6x23.2 1px auto rgb(0, 95, 204) offset 1px; a::before 85.625pxx1px rgb(25, 25, 27) |

Child layers that carry the look: a::before 85.625pxx1px background #19191b `color.neutral.ink`.

![Cookie "Learn more" default](components/crops/cookie-learn-default.png) ![Cookie "Learn more" hover](components/crops/cookie-learn-hover.png) ![Cookie "Learn more" focus-visible](components/crops/cookie-learn-focus-visible.png) ![Cookie "Learn more" pressed](components/crops/cookie-learn-pressed.png)

#### Cookie accept
The banner's Accept action; measured, never clicked — no consent was ever posted. Read as `cookie-accept` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 87.66 x 36; padding 6px 20px; radius 32px; background #eceff2 `color.fill.control`; image linear-gradient(rgba(255, 255, 255, 0.07) 0%, rgba(255, 255, 255, 0) 100%), none; shadow rgba(12, 20, 66, 0.02) 0px 2px 4px 0px, rgba(12, 20, 66, 0.03) 0px -1px 2px 0px inset; text Inter 14/24 500, #19191b `color.neutral.ink`; transition color 0.15s ease, background-color 0.15s ease, box-shadow 0.15s ease |
| hover | background #e9ecef `color.fill.control-hover` |

![Cookie accept default](components/crops/cookie-accept-default.png) ![Cookie accept hover](components/crops/cookie-accept-hover.png) ![Cookie accept focus-visible](components/crops/cookie-accept-focus-visible.png) ![Cookie accept pressed](components/crops/cookie-accept-pressed.png)

#### Header
The top bar: the About button, the centred dona wordmark and the Login action. Read as `header` on the home page.

**Values (default).** size 1100 x 68; padding 32px 0px 0px 0px; background transparent; text Inter 14/24 500, #19191b `color.neutral.ink`; icon 95.19 x 28, #0000ee `measured.ua-link`; layers button.Button__ButtonWrapper-sc-1eaeu1c-0.cPTtUr 80.5x36.0 32px; button.Button__ButtonWrapper-sc-1eaeu1c-0.khZmSx 76.8x36.0 rgb(236, 239, 242) rgba(12, 20, 66, 0.02) 0px 2px 4px 0px, rgba(12, 20, 66, 0.03) 0px -1px 2px 0px inset 32px.

Child layers that carry the look: button 80.5x36 image linear-gradient(rgba(255, 255, 255, 0.07) 0%, rgba(255, 255, 255, 0) 100%), none radius 32px; button 76.8x36 background #eceff2 `color.fill.control` image linear-gradient(rgba(255, 255, 255, 0.07) 0%, rgba(255, 255, 255, 0) 100%), none radius 32px shadow rgba(12, 20, 66, 0.02) 0px 2px 4px 0px, rgba(12, 20, 66, 0.03) 0px -1px 2px 0px inset.

![Header default](components/crops/header-default.png)

#### Logo
The centred dona logo (ring mark + wordmark), inside an anchor to / whose own box is 0 wide. Read as `logo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 95.19 x 28; background transparent; text Inter 16/23.2 400, #0000ee `measured.ua-link`; transform translate(-47.5938px, 0px); icon 95.19 x 28, #0000ee `measured.ua-link` |

![Logo default](components/crops/logo-default.png) ![Logo hover](components/crops/logo-hover.png) ![Logo pressed](components/crops/logo-pressed.png)

#### About button
The header About action (routes to /about). Read as `nav-about` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 80.53 x 36; padding 6px 20px; radius 32px; background transparent; image linear-gradient(rgba(255, 255, 255, 0.07) 0%, rgba(255, 255, 255, 0) 100%), none; text Inter 14/24 500, #19191b `color.neutral.ink`; transition color 0.15s ease, background-color 0.15s ease, box-shadow 0.15s ease |
| hover | background #f2f4f8 `color.fill.ghost-hover` |

![About button default](components/crops/nav-about-default.png) ![About button hover](components/crops/nav-about-hover.png) ![About button focus-visible](components/crops/nav-about-focus-visible.png) ![About button pressed](components/crops/nav-about-pressed.png)

#### Login button
The header Login action — opens https://app.dona.ai in a new tab; measured, never pressed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 76.83 x 36; padding 6px 20px; radius 32px; background #eceff2 `color.fill.control`; image linear-gradient(rgba(255, 255, 255, 0.07) 0%, rgba(255, 255, 255, 0) 100%), none; shadow rgba(12, 20, 66, 0.02) 0px 2px 4px 0px, rgba(12, 20, 66, 0.03) 0px -1px 2px 0px inset; text Inter 14/24 500, #19191b `color.neutral.ink`; transition color 0.15s ease, background-color 0.15s ease, box-shadow 0.15s ease |
| hover | background #e9ecef `color.fill.control-hover` |

![Login button default](components/crops/nav-login-default.png) ![Login button hover](components/crops/nav-login-hover.png) ![Login button focus-visible](components/crops/nav-login-focus-visible.png) ![Login button pressed](components/crops/nav-login-pressed.png)

### Home

The hero (headline, lede, Watch video / Try for free), the app-frame media tile, the feature grid, the newsletter band and the video modal.

#### Hero headline
The "A more humane / to-do list" display — the first line paints muted, the second ink. Read as `hero-h1` on the home page.

**Values (default).** size 715 x 184.78; background transparent; text Inter 84/92.4 700, #19191b `color.neutral.ink`; transition opacity 1s cubic-bezier(0.17, 0.17, 0, 1), transform 1s cubic-bezier(0.17, 0.17, 0, 1); layers span 644.8x101.0 rgb(120, 128, 136).

Child layers that carry the look: span 644.8x101 background #788088 image linear-gradient(to right, #d3d7db 50%, rgba(179, 207, 255, 0.7) 100%).

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero lede
The "back to basic to-do list" paragraph under the headline. Read as `hero-lede` on the home page.

**Values (default).** size 660 x 69.59; background transparent; text Inter 24/34.8 500, #19191b `color.neutral.ink`; transition opacity 1s cubic-bezier(0.17, 0.17, 0, 1), transform 1s cubic-bezier(0.17, 0.17, 0, 1).

![Hero lede default](components/crops/hero-lede-default.png)

#### Watch video button
The secondary pill with the play-triangle icon; opens the video modal. Read as `watch-video` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 170.81 x 52; padding 14px 26px; radius 32px; background #eceff2 `color.fill.control`; image linear-gradient(rgba(255, 255, 255, 0.07) 0%, rgba(255, 255, 255, 0) 100%), none; shadow rgba(12, 20, 66, 0.02) 0px 2px 4px 0px, rgba(12, 20, 66, 0.03) 0px -1px 2px 0px inset; text Inter 16/24 500, #19191b `color.neutral.ink`; transition color 0.15s ease, background-color 0.15s ease, box-shadow 0.15s ease; icon 16 x 16, #19191b `color.neutral.ink` |
| hover | background #e9ecef `color.fill.control-hover` |

![Watch video button default](components/crops/watch-video-default.png) ![Watch video button hover](components/crops/watch-video-hover.png) ![Watch video button focus-visible](components/crops/watch-video-focus-visible.png) ![Watch video button pressed](components/crops/watch-video-pressed.png)

#### Try for free button
The blue primary pill — opens https://app.dona.ai in a new tab; measured, never pressed. Read as `try-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 157.58 x 52; padding 14px 26px; radius 32px; background #008ffd `color.brand.blue`; image linear-gradient(rgba(255, 255, 255, 0.07) 0%, rgba(255, 255, 255, 0) 100%), none; shadow rgba(12, 20, 66, 0.1) 0px 2px 4px 0px, rgba(12, 20, 66, 0.06) 0px 10px 40px 0px, rgba(12, 20, 66, 0.1) 0px -1px 2px 0px inset; text Inter 16/24 500, #ffffff `color.neutral.paper`; transition color 0.15s ease, background-color 0.15s ease, box-shadow 0.15s ease |
| hover | background #0087fd `color.brand.blue-hover` |

![Try for free button default](components/crops/try-cta-default.png) ![Try for free button hover](components/crops/try-cta-hover.png) ![Try for free button focus-visible](components/crops/try-cta-focus-visible.png) ![Try for free button pressed](components/crops/try-cta-pressed.png)

#### Hero app frame
The autoplay product video under the CTAs (the Dona task UI in a rounded frame). Read as `hero-video` on the home page.

**Values (default).** size 1100 x 688.52; radius 20px; background #eff2f5 `color.fill.media`; shadow rgba(12, 20, 66, 0.02) 0px 4px 12px 0px, rgba(12, 20, 66, 0.08) 0px 30px 80px 0px, #e6e9ed 0px 0px 0px 1px inset; text Inter 16/23.2 400, #19191b `color.neutral.ink`.

![Hero app frame default](components/crops/hero-video-default.png)

#### Section heading
The "Fast & delightful user experience" section title. Read as `section-h2` on the home page.

**Values (default).** size 360 x 86.38; background transparent; text Inter 32/43.2 600, #19191b `color.neutral.ink`.

![Section heading default](components/crops/section-h2-default.png)

#### Feature heading
A feature tile's h3 ("Light, dark & black UI theme" / "Details matter"). Read as `section-h3` on the home page.

**Values (default).** size 360 x 35.09; background transparent; text Inter 26/35.1 600, #19191b `color.neutral.ink`.

![Feature heading default](components/crops/section-h3-default.png)

#### Feature paragraph
A feature tile's body copy. Read as `section-para` on the home page.

**Values (default).** size 360 x 104.38; background transparent; text Inter 18/26.1 400, #616870 `color.neutral.muted`.

![Feature paragraph default](components/crops/section-para-default.png)

#### Feature tile
A half-width feature tile (headline + autoplay video). Read as `feature-tile` on the home page.

**Values (default).** size 534 x 534; padding 0px 0px 534px 0px; radius 20px; background #f4f4f5 `color.fill.tile`; text Inter 26/35.1 600, #19191b `color.neutral.ink`; layers ::before rgb(0, 143, 253) 0px none 0.12.

![Feature tile default](components/crops/feature-tile-default.png)

#### Newsletter form
The email capture: the "Enter your email" field plus the "Join our newsletter" submit with the arrow-circle icon; measured, never submitted. Read as `newsletter` on the home page.

**Values (default).** size 1100 x 140; background transparent; text Inter 16/24 500, #ffffff `color.neutral.paper`; icon 30 x 30, #ffffff `color.neutral.paper`; layers ::before rgb(0, 143, 253) 0px none 0.5; form::before.Newsletter__Wrapper-sc-1ivl8su-0.ePfgSy 1650pxx42px rgb(0, 143, 253) 75%; div::before.Submit__SubmitWrapper-sc-193h5k4-0.epAaVt 199.219pxx52px rgb(111, 171, 255) 0px 8px 140px 0px 32px; button.Submit__ButtonWrapper-sc-193h5k4-1.fvJKjf 199.2x52.0 rgb(25, 25, 27) rgba(12, 20, 66, 0.1) 0px 2px 4px 0px, rgba(12, 20, 66, 0.06) 0px 10px 40px 0px, rgba.

Child layers that carry the look: form::before 1650pxx42px background #008ffd `color.brand.blue` radius 75%; div::before 199.219pxx52px radius 32px shadow #6fabff `color.brand.glow` 0px 8px 140px 0px; button 199.2x52 background #19191b `color.neutral.ink` radius 32px shadow rgba(12, 20, 66, 0.1) 0px 2px 4px 0px, rgba(12, 20, 66, 0.06) 0px 10px 40px 0px, rgba(12, 20, 66, 0.08) 0px -1px 2px 0px inset, transparent 0px 0px 0px 999px inset.

![Newsletter form default](components/crops/newsletter-default.png)

#### Email field
The newsletter email input; focused and given sample text that was deleted again — the form was never submitted. Read as `email-input` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1100 x 60; background transparent; text Inter 40/60 400, #19191b `color.neutral.ink`; placeholder #bfc3c8 `color.neutral.placeholder` |
| focused, filled | placeholder #b0b5ba `color.fill.close` |

![Email field default](components/crops/email-input-default.png) ![Email field focused](components/crops/email-input-focused.png) ![Email field filled](components/crops/email-input-filled.png)

#### Newsletter submit
The "Join our newsletter" submit button; measured — pressed state forced via DevTools, the button itself was never really pressed. Read as `join-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 199.22 x 52; padding 14px 26px; radius 32px; background #19191b `color.neutral.ink`; shadow rgba(12, 20, 66, 0.1) 0px 2px 4px 0px, rgba(12, 20, 66, 0.06) 0px 10px 40px 0px, rgba(12, 20, 66, 0.08) 0px -1px 2px 0px inset; text Inter 16/24 500, #ffffff `color.neutral.paper`; transition background-color 0.25s ease, box-shadow 0.15s ease, padding 0.3s ease; icon 30 x 30, #ffffff `color.neutral.paper` |
| hover | shadow rgba(12, 20, 66, 0.1) 0px 2px 4px 0px, rgba(12, 20, 66, 0.06) 0px 10px 40px 0px, rgba(12, 20, 66, 0.08) 0px -1px 2px 0px inset, rgba(0, 0, 0, 0.5) 0px 0px 0px 999px inset |

![Newsletter submit default](components/crops/join-btn-default.png) ![Newsletter submit hover](components/crops/join-btn-hover.png) ![Newsletter submit focus-visible](components/crops/join-btn-focus-visible.png) ![Newsletter submit pressed](components/crops/join-btn-pressed.png)

#### Video modal
The fixed overlay the Watch video button mounts: a YouTube iframe ("Say hello to Dona") on a dimmed page with a close button. Read as `video-modal` on the home page.

**Values (default).** size 1440 x 900; padding 0px 20px; background rgba(191, 195, 200, 0.8) `color.overlay.scrim`; text Inter 16/23.2 400, #19191b `color.neutral.ink`; transition opacity 0.3s ease; icon 18 x 18, #ffffff `color.neutral.paper`.

![Video modal default](components/crops/video-modal-default.png)

#### Modal close
The close (x) control on the video modal. Read as `modal-close` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 56 x 56; radius 50%; background #b0b5ba `color.fill.close`; text Inter 16/23.2 400, #ffffff `color.neutral.paper`; transition background-color 0.15s ease; icon 18 x 18, #ffffff `color.neutral.paper` |
| hover, pressed | background #a8adb3 `color.fill.close-hover` |

![Modal close default](components/crops/modal-close-default.png) ![Modal close hover](components/crops/modal-close-hover.png) ![Modal close pressed](components/crops/modal-close-pressed.png)

### About

The mission page: the same 84px display, the mission paragraphs and the team card grid with its social chips.

#### About headline
The "We’re building / to-do list you’ll enjoy using" display — muted first line, ink continuation. Read as `about-h1` on the about page.

**Values (default).** size 715 x 277.17; background transparent; text Inter 84/92.4 700, #19191b `color.neutral.ink`; transition opacity 1s cubic-bezier(0.17, 0.17, 0, 1), transform 1s cubic-bezier(0.17, 0.17, 0, 1); layers span 584.4x101.0 rgb(120, 128, 136).

Child layers that carry the look: span 584.4x101 background #788088 image linear-gradient(to right, #d3d7db 50%, rgba(179, 207, 255, 0.7) 100%).

![About headline default](components/crops/about-h1-default.png)

#### Mission text
The mission paragraph; its second sentence paints muted (a span inside the paragraph). Read as `mission-text` on the about page.

**Values (default).** size 660 x 173.98; background transparent; text Inter 24/34.8 600, #19191b `color.neutral.ink`; transition opacity 1s cubic-bezier(0.17, 0.17, 0, 1), transform 1s cubic-bezier(0.17, 0.17, 0, 1).

![Mission text default](components/crops/mission-text-default.png)

#### Team heading
The "Team" section title. Read as `team-h2` on the about page.

**Values (default).** size 980 x 43.19; background transparent; text Inter 32/43.2 600, #19191b `color.neutral.ink`.

![Team heading default](components/crops/team-h2-default.png)

#### Team card
A team-member card: photo, name, one-line bio and social links (Jakub Antalik / Aaron Iker / Nisarg Patel). Read as `team-card` on the about page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 286.66 x 330.05; background transparent; text Inter 18/24.3 600, #19191b `color.neutral.ink`; icon 16 x 16, #0000ee `measured.ua-link`; layers a.about__Social-sc-xipocs-7.kgPcWG 40.0x40.0 rgb(224, 227, 231) rgba(0, 0, 0, 0.02) 0px 2px 4px 0px, rgba(0, 0, 0, 0.03) 0px -1px 2px 0px inset 14px; a.about__Social-sc-xipocs-7.kgPcWG 40.0x40.0 rgb(224, 227, 231) rgba(0, 0, 0, 0.02) 0px 2px 4px 0px, rgba(0, 0, 0, 0.03) 0px -1px 2px 0px inset 14px |

Child layers that carry the look: a 40x40 background #e0e3e7 `color.fill.chip` radius 14px shadow rgba(0, 0, 0, 0.02) 0px 2px 4px 0px, rgba(0, 0, 0, 0.03) 0px -1px 2px 0px inset; a 40x40 background #e0e3e7 `color.fill.chip` radius 14px shadow rgba(0, 0, 0, 0.02) 0px 2px 4px 0px, rgba(0, 0, 0, 0.03) 0px -1px 2px 0px inset.

![Team card default](components/crops/team-card-default.png) ![Team card hover](components/crops/team-card-hover.png) ![Team card pressed](components/crops/team-card-pressed.png)

#### Team avatar
A member photo inside the team card. Read as `team-avatar` on the about page.

**Values (default).** size 125 x 125; radius 12px; background transparent; text Inter 16/23.2 400, #19191b `color.neutral.ink`.

![Team avatar default](components/crops/team-avatar-default.png)

#### Social link
A social link inside a team card (twitter / dribbble glyphs); measured, never followed. Read as `social-link` on the about page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; radius 14px; background #e0e3e7 `color.fill.chip`; shadow rgba(0, 0, 0, 0.02) 0px 2px 4px 0px, rgba(0, 0, 0, 0.03) 0px -1px 2px 0px inset; text Inter 16/23.2 400, #0000ee `measured.ua-link`; transition background-color 0.15s ease; icon 16 x 16, #0000ee `measured.ua-link` |
| hover | background #dde0e4 `color.fill.chip-hover` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |
| pressed | background #dadde1 `color.fill.chip-pressed`; text Inter 16/23.2 400, #ff0000 `measured.ua-link-active`; icon 16 x 16, #ff0000 `measured.ua-link-active` |

![Social link default](components/crops/social-link-default.png) ![Social link hover](components/crops/social-link-hover.png) ![Social link focus-visible](components/crops/social-link-focus-visible.png) ![Social link pressed](components/crops/social-link-pressed.png)

### Legal pages

The privacy policy (the terms page paints the same layout): display head, 16px body and 18px subheads.

#### Legal heading
The "Privacy / policy" display on /privacy-policy; /terms-of-service is the same layout. Read as `legal-h1` on the privacy policy page.

**Values (default).** size 624 x 184.78; background transparent; text Inter 84/92.4 700, #19191b `color.neutral.ink`; transition opacity 1s cubic-bezier(0.17, 0.17, 0, 1), transform 1s cubic-bezier(0.17, 0.17, 0, 1); layers span 306.8x101.0 rgb(120, 128, 136); span 248.9x101.0 rgb(120, 128, 136).

Child layers that carry the look: span 306.8x101 background #788088 image linear-gradient(to right, #d3d7db 50%, rgba(179, 207, 255, 0.7) 100%); span 248.9x101 background #788088 image linear-gradient(to right, #d3d7db 50%, rgba(179, 207, 255, 0.7) 100%).

![Legal heading default](components/crops/legal-h1-default.png)

#### Legal paragraph
A body paragraph of the legal copy. Read as `legal-text` on the privacy policy page.

**Values (default).** size 960 x 46.38; background transparent; text Inter 16/23.2 400, #19191b `color.neutral.ink`.

![Legal paragraph default](components/crops/legal-text-default.png)

#### Legal subheading
A section subheading inside the legal copy ("Cookies", "Terms"). Read as `legal-h4` on the privacy policy page.

**Values (default).** size 960 x 24.3; background transparent; text Inter 18/24.3 600, #19191b `color.neutral.ink`.

![Legal subheading default](components/crops/legal-h4-default.png)

#### Legal link
A link inside the legal copy. The `div a` catch-all landed on the footer's 'Privacy policy' link (14px/20.3px), not a legal-body link, so no in-copy link was verified — the selector is now scoped to the legal content and the entry re-measures on the next capture. Read as `legal-link` on the privacy policy page.

Not on the page when it was captured.

### Footer

The footer row: the dona wordmark, legal links and the grey social chip.

#### Footer
The footer: the copyright line, Terms of Service / Privacy policy links and the @getdona twitter link. Read as `footer` on the home page.

**Values (default).** size 1440 x 176.48; padding 64px 0px; border T: 1px solid #eceff2 `color.fill.control`; background transparent; text Inter 16/23.2 500, #616870 `color.neutral.muted`; icon 16 x 16, #0000ee `measured.ua-link`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A legal link in the footer. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 111.63 x 17; background transparent; text Inter 14/20.3 400, #19191b `color.neutral.ink` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a 111.6x17.0 1px auto rgb(0, 95, 204) offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Twitter link
The @getdona icon link in the footer; measured, never followed. Read as `footer-twitter` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; radius 14px; background #eceff2 `color.fill.control`; shadow rgba(0, 0, 0, 0.02) 0px 2px 4px 0px, rgba(0, 0, 0, 0.03) 0px -1px 2px 0px inset; text Inter 16/23.2 400, #0000ee `measured.ua-link`; transition background-color 0.15s ease; icon 16 x 16, #0000ee `measured.ua-link` |
| hover | background #e9ecef `color.fill.control-hover` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |
| pressed | background #e6e9ed `color.fill.chip-twitter-pressed`; text Inter 16/23.2 400, #ff0000 `measured.ua-link-active`; icon 16 x 16, #ff0000 `measured.ua-link-active` |

![Twitter link default](components/crops/footer-twitter-default.png) ![Twitter link hover](components/crops/footer-twitter-hover.png) ![Twitter link focus-visible](components/crops/footer-twitter-focus-visible.png) ![Twitter link pressed](components/crops/footer-twitter-pressed.png)

### Mobile (390 wide)

The same surface at phone width — the cookie banner's marked node measured as an offscreen 555x64 fixed bar (it never painted on the phone pass, so its real placement is unverified) and the display drops to 40px.

#### Cookie banner (mobile)
The consent notice at 390 wide; hidden after its own reading, never answered. Note: the marked node read as a 555x64 fixed bar at top:1138px — offscreen in the 390x844 viewport and wider than it — and it never painted on the phone pass (the crop caught body text), so the real mobile placement is unverified. Read as `m-cookie-banner` on the home page at 390 wide.

**Values (default).** size 555 x 64; padding 12px; background #ffffff `color.neutral.paper`; shadow rgba(12, 20, 66, 0.03) 0px 1px 3px 0px, rgba(12, 20, 66, 0.04) 0px -8px 16px 0px, rgba(12, 20, 66, 0.04) 0px -16px 40px 0px; text Inter 16/23.2 400, #19191b `color.neutral.ink`; icon 40 x 40, #19191b `color.neutral.ink`.

![Cookie banner (mobile) default](components/crops/m-cookie-banner-default.png)

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 350 x 68; padding 32px 0px 0px 0px; background transparent; text Inter 14/24 500, #19191b `color.neutral.ink`; icon 95.19 x 28, #0000ee `measured.ua-link`; layers button.Button__ButtonWrapper-sc-1eaeu1c-0.cPTtUr 80.5x36.0 32px; button.Button__ButtonWrapper-sc-1eaeu1c-0.khZmSx 76.8x36.0 rgb(236, 239, 242) rgba(12, 20, 66, 0.02) 0px 2px 4px 0px, rgba(12, 20, 66, 0.03) 0px -1px 2px 0px inset 32px.

Child layers that carry the look: button 80.5x36 image linear-gradient(rgba(255, 255, 255, 0.07) 0%, rgba(255, 255, 255, 0) 100%), none radius 32px; button 76.8x36 background #eceff2 `color.fill.control` image linear-gradient(rgba(255, 255, 255, 0.07) 0%, rgba(255, 255, 255, 0) 100%), none radius 32px shadow rgba(12, 20, 66, 0.02) 0px 2px 4px 0px, rgba(12, 20, 66, 0.03) 0px -1px 2px 0px inset.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 350 x 92; background transparent; text Inter 40/44 700, #19191b `color.neutral.ink`; transition opacity 1s cubic-bezier(0.17, 0.17, 0, 1), transform 1s cubic-bezier(0.17, 0.17, 0, 1); layers span 307.0x49.0 rgb(120, 128, 136).

Child layers that carry the look: span 307x49 background #788088 image linear-gradient(to right, #d3d7db 50%, rgba(179, 207, 255, 0.7) 100%).

![Mobile headline default](components/crops/m-hero-default.png)

#### Mobile Watch video
Read as `m-watch` on the home page at 390 wide.

**Values (default).** size 170.81 x 52; padding 14px 26px; radius 32px; background #eceff2 `color.fill.control`; image linear-gradient(rgba(255, 255, 255, 0.07) 0%, rgba(255, 255, 255, 0) 100%), none; shadow rgba(12, 20, 66, 0.02) 0px 2px 4px 0px, rgba(12, 20, 66, 0.03) 0px -1px 2px 0px inset; text Inter 16/24 500, #19191b `color.neutral.ink`; transition color 0.15s ease, background-color 0.15s ease, box-shadow 0.15s ease; icon 16 x 16, #19191b `color.neutral.ink`.

![Mobile Watch video default](components/crops/m-watch-default.png)

#### Mobile Try for free
Read as `m-try` on the home page at 390 wide.

**Values (default).** size 157.58 x 52; padding 14px 26px; radius 32px; background #008ffd `color.brand.blue`; image linear-gradient(rgba(255, 255, 255, 0.07) 0%, rgba(255, 255, 255, 0) 100%), none; shadow rgba(12, 20, 66, 0.1) 0px 2px 4px 0px, rgba(12, 20, 66, 0.06) 0px 10px 40px 0px, rgba(12, 20, 66, 0.1) 0px -1px 2px 0px inset; text Inter 16/24 500, #ffffff `color.neutral.paper`; transition color 0.15s ease, background-color 0.15s ease, box-shadow 0.15s ease.

![Mobile Try for free default](components/crops/m-try-default.png)

#### Mobile email field
Read as `m-email-input` on the home page at 390 wide.

**Values (default).** size 350 x 36; background transparent; text Inter 28/36 400, #19191b `color.neutral.ink`; placeholder #bfc3c8 `color.neutral.placeholder`.

![Mobile email field default](components/crops/m-email-input-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the dona ring-and-wordmark logo, the social glyphs, the play and close marks) are the product's artwork. The sheets do declare the icon sizing vars — 14/16/30/40px --icon-size on the component classes — recorded as light.component.icon.size-* in tokens.json. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

app.dona.ai holds the to-do product — lists, the light/dark/black UI themes the marketing copy advertises, sync, accounts — behind its own sign-in. The Login and Try for free buttons open that host in a new tab and were never followed. The public site is the marketing shell only: four routes (/, /about, /privacy-policy, /terms-of-service).

### Pages

- **The app.** app.dona.ai — the product itself, with the advertised light/dark/black themes, list UI and account flows — was never reached; it needs an account.
- **Login / Try for free.** Both actions open the app host; never clicked, never followed.
- **Newsletter.** The email field was measured, focused and filled with sample text (cleared after); Join our newsletter was never pressed, so the 'Thank you! You're in.' success state and any error state are uncaptured.
- **External surfaces.** twitter.com/getdona, the Discord invite and the legal cross-links out are linked from the site but were never opened.
- **Mobile nav.** The 390-wide header keeps the same About and Login buttons — there is no hamburger or menu overlay to capture.
- **Terms of service.** The terms page paints the same legal layout as the privacy policy; the legal components were measured once on /privacy-policy.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

The public surface paints one light theme and offers no switcher. The marketing copy and video advertise light, dark and black UI themes — those are themes inside the app (visible in the product video), not themes this site paints, so the export holds light only.

### Fonts

- **Inter** is the single face for everything from the 84px display to the 14px legal small, in 400/500/600/700 — dona.ai serves it as inline base64 woff2 plus /static/inter-*.woff2 subset files (the @font-face rules are harvested in raw/css-vars.json). The style guide does not ship the font; samples render in a system sans fallback.

### Screenshots

- The dona wordmark and ring logo, the product video stills inside the app-frame tile and the team avatars in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The team names and roles on /about, the legal text and the marketing copy are the product's published content; only frames and components were measured.
