# Endel components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from endel.io and app.endel.io on 2026-11-21, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent or uploaded.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (55 components, 138 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `apercuPro 22/28 400, #ffffff`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (137 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-dark-{state}.png`: the site paints one dark theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages (1x on desktop, 2x on mobile); mobile shots are `mobile-{page}-dark-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `https://endel.io/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [menu-open](screenshots/home-dark-menu-open.png) |
| Focus | `https://endel.io/focus` | [default](screenshots/focus-dark-default.png), [full](screenshots/focus-dark-full.png) |
| Sleep | `https://endel.io/sleep` | [default](screenshots/sleep-dark-default.png), [full](screenshots/sleep-dark-full.png) |
| Relax | `https://endel.io/relax` | [default](screenshots/relax-dark-default.png), [full](screenshots/relax-dark-full.png) |
| Activity | `https://endel.io/activity` | [default](screenshots/activity-dark-default.png), [full](screenshots/activity-dark-full.png) |
| ADHD | `https://endel.io/adhd` | [default](screenshots/adhd-dark-default.png), [full](screenshots/adhd-dark-full.png) |
| Soundscapes | `https://endel.io/soundscapes` | [default](screenshots/soundscapes-dark-default.png), [full](screenshots/soundscapes-dark-full.png) |
| Science | `https://endel.io/science` | [default](screenshots/science-dark-default.png), [full](screenshots/science-dark-full.png) |
| Technology | `https://endel.io/technology` | [default](screenshots/technology-dark-default.png), [full](screenshots/technology-dark-full.png) |
| Streaming | `https://endel.io/streaming` | [default](screenshots/streaming-dark-default.png), [full](screenshots/streaming-dark-full.png) |
| Community | `https://endel.io/community` | [default](screenshots/community-dark-default.png), [full](screenshots/community-dark-full.png) |
| About | `https://endel.io/about` | [default](screenshots/about-dark-default.png), [full](screenshots/about-dark-full.png) |
| Blog | `https://endel.io/blog` | [default](screenshots/blog-dark-default.png), [full](screenshots/blog-dark-full.png) |
| Newsroom | `https://endel.io/newsroom` | [default](screenshots/newsroom-dark-default.png), [full](screenshots/newsroom-dark-full.png) |
| Scenarios | `https://endel.io/scenarios` | [default](screenshots/scenarios-dark-default.png), [full](screenshots/scenarios-dark-full.png) |
| Privacy Policy | `https://endel.io/privacy-policy` | [default](screenshots/privacy-policy-dark-default.png), [full](screenshots/privacy-policy-dark-full.png) |
| Impressum | `https://endel.io/impressum` | [default](screenshots/impressum-dark-default.png), [full](screenshots/impressum-dark-full.png) |
| Web app, explore (signed out) | `https://app.endel.io/` | [default](screenshots/app-explore-dark-default.png), [full](screenshots/app-explore-dark-full.png) |
| Web app, player | `https://app.endel.io/player/focus` | [default](screenshots/app-player-dark-default.png), [full](screenshots/app-player-dark-full.png), [timer-open](screenshots/app-player-dark-timer-open.png) |
| Web app, sign-in card | `https://app.endel.io/ via its own Sign In button` | [default](screenshots/app-login-dark-default.png), [full](screenshots/app-login-dark-full.png) |
| Home, phone | `https://endel.io/` | [default](screenshots/mobile-home-dark-default.png), [full](screenshots/mobile-home-dark-full.png), [menu-open](screenshots/mobile-home-dark-menu-open.png) |
| Focus, phone | `https://endel.io/focus` | [default](screenshots/mobile-focus-dark-default.png), [full](screenshots/mobile-focus-dark-full.png) |
| Soundscapes, phone | `https://endel.io/soundscapes` | [default](screenshots/mobile-soundscapes-dark-default.png), [full](screenshots/mobile-soundscapes-dark-full.png) |
| Scenarios, phone | `https://endel.io/scenarios` | [default](screenshots/mobile-scenarios-dark-default.png), [full](screenshots/mobile-scenarios-dark-full.png) |
| Web app explore, phone | `https://app.endel.io/` | [default](screenshots/mobile-app-explore-dark-default.png), [full](screenshots/mobile-app-explore-dark-full.png) |
| Web app sign-in, phone | `https://app.endel.io/ via Sign In` | [default](screenshots/mobile-app-login-dark-default.png), [full](screenshots/mobile-app-login-dark-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| More flyout, open | header, desktop | the MenuButton's own press | [home-dark-menu-open](screenshots/home-dark-menu-open.png), [nav-more-open](#more-button-open) |
| Mobile menu, open | header, phone | the Menu button's own press | [mobile-home-dark-menu-open](screenshots/mobile-home-dark-menu-open.png), [m-menu-button](#menu-button) |
| Set Timer sheet | player footer | the Set Timer button's own press, closed again | [app-player-dark-timer-open](screenshots/app-player-dark-timer-open.png), [timer-dialog](#shut-off-timer-dialog) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 26 components were given a real keyboard focus (a further 1 could not be driven: `button-mode`). 21 show a visible focus state: `nav-link` (visible change in boxShadow), `nav-more` (visible change in boxShadow), `btn-try` (visible change in boxShadow), `btn-signin` (visible change in boxShadow), `learn-more` (visible change in boxShadow), `try-now` (visible change in boxShadow), `play-button` (visible change in boxShadow), `show-more` (visible change in boxShadow), `accordion-title` (visible change in boxShadow), `press-logo` (visible change in boxShadow), `app-btn-signin` (visible change in boxShadow), `scenario-pill` (visible change in boxShadow), `btn-close-player` (visible change in boxShadow), `btn-set-timer` (visible change in boxShadow), `player-control` (visible change in boxShadow), `btn-continue` (visible change in boxShadow), `btn-oauth` (visible change in boxShadow), `footer-link` (visible change in boxShadow), `footer-social` (visible change in boxShadow), `footer-legal` (visible change in boxShadow), `m-menu-button` (visible change in boxShadow). The other 5 show no change a keyboard user can see: `soundscape-card`, `user-button`, `banner`, `soundscape-row`, `btn-explore`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): controls deepen their fill or dim rather than scale; the nav flyout and framework icons keep their hover scale. Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `ease` | background-color, border-color | accordion-title, app-btn-signin, btn-close-player, btn-continue, btn-oauth, btn-set-timer, btn-signin, btn-try and more |
| 0.25s | `linear` | opacity | button-mode |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [FAQ accordion item](#faq-accordion-item) | 1152 x 76 | - | 12px | #191919 `color.neutral.800` | none | 0 |
| [Soundscape card](#soundscape-card) | 270 x 270.39 | - | - | - | none | 0 |
| [Scenario card](#scenario-card) | 270 x 270 | - | - | transparent | none | 0 |
| [Carousel banner](#carousel-banner) | 956 x 320 | - | 24px | #ffffff `color.neutral.white` | none | 0 |
| [Scenario pill](#scenario-pill) | 202.52 x 56 | 2px solid #262626 `color.neutral.700` | 100px | #262626 `color.neutral.700` | none | 0px 24px |
| [Mini player](#mini-player) | 1440 x 120 | - | 100px | #191919 `color.neutral.800` | none | 16px |

## Components

### Shell and navigation

The fixed header with its scroll scrim, the nav links and the More flyout.

#### Header
The fixed dark bar: the Endel mark, the nav links (ADHD, Sleep, Focus, Relax, Activity), the More flyout, Try Today and Sign In. Read as `header` on the home page.

**Values (default).** size 1440 x 72; background transparent; image linear-gradient(#000000 `color.neutral.black` 0%, rgba(0, 0, 0, 0.65) 50%, transparent 100%); text apercuPro 22/28 400, #ffffff `color.neutral.white`; icon 24 x 24, #ffffff `color.neutral.white`.

![Header default](components/crops/header-default.png)

#### Logo
The 40x40 Endel mark, a link home. Read as `logo` on the home page.

**Values (default).** size 40 x 40; background transparent; text apercuPro 22/28 400, #ffffff `color.neutral.white`.

![Logo default](components/crops/logo-default.png)

#### Nav link
Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 56.77 x 28; background transparent; text apercuPro 22/28 400, #ffffff `color.neutral.white` |
| hover | text apercuPro 22/28 400, #ffffff `color.neutral.white`, underline |
| focus-visible | shadow #666666 0px 0px 0px 6px; child paint a.Link-module__QL15TW__link.Link-module__QL15TW__color-white: size 56.8x28.0; shadow rgb(102, 102, 102) 0px 0px 0px 6px |
| pressed | text apercuPro 22/28 400, #ffffff `color.neutral.white`, underline |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### More button
The nav overflow toggle; its press opens the flyout inside the header. Read as `nav-more` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 81.66 x 28; background transparent; text apercuPro 22/28 400, #ffffff `color.neutral.white`; icon 24 x 24, #ffffff `color.neutral.white` |
| hover | opacity 0.9 |
| focus-visible | shadow #666666 0px 0px 0px 6px; child paint button.MenuButton-module__hXokYa__button.MenuButton-module__hXokYa__closed: size 81.7x28.0; shadow rgb(102, 102, 102) 0px 0px 0px 6px |
| pressed | opacity 0.9 |

![More button default](components/crops/nav-more-default.png) ![More button hover](components/crops/nav-more-hover.png) ![More button focus-visible](components/crops/nav-more-focus-visible.png) ![More button pressed](components/crops/nav-more-pressed.png)

#### Try Today button
The primary header CTA. Measured, never followed. Read as `btn-try` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 94 x 44; padding 0px 12px; border 2px solid transparent; radius 12px; background #262626 `color.neutral.700`; shadow #ffffff 0px 0px 15px 0px; text apercuPro 16/16 400, #ffffff `color.neutral.white`; transition background-color 0.2s ease, border-color 0.2s ease |
| hover | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |
| focus-visible | shadow #666666 0px 0px 0px 6px; child paint button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic: shadow rgb(102, 102, 102) 0px 0px 0px 6px |
| pressed | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |

![Try Today button default](components/crops/btn-try-default.png) ![Try Today button hover](components/crops/btn-try-hover.png) ![Try Today button focus-visible](components/crops/btn-try-focus-visible.png) ![Try Today button pressed](components/crops/btn-try-pressed.png)

#### Sign In button
The header auth link. Measured, never followed. Read as `btn-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 73.58 x 44; padding 0px 12px; border 2px solid #262626 `color.neutral.700`; radius 12px; background #262626 `color.neutral.700`; text apercuPro 16/16 400, #ffffff `color.neutral.white`; transition background-color 0.2s ease, border-color 0.2s ease |
| hover | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |
| focus-visible | shadow #666666 0px 0px 0px 6px; child paint button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic: shadow rgb(102, 102, 102) 0px 0px 0px 6px |
| pressed | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |

![Sign In button default](components/crops/btn-signin-default.png) ![Sign In button hover](components/crops/btn-signin-hover.png) ![Sign In button focus-visible](components/crops/btn-signin-focus-visible.png) ![Sign In button pressed](components/crops/btn-signin-pressed.png)

#### More flyout
The expanded nav groups inside the header after More is pressed (Company, Technology, the store links). Read while held open. Read as `menu-flyout` on the home page.

**Values (default).** size 172 x 28; background transparent; text apercuPro 22/28 400, #ffffff `color.neutral.white`.

![More flyout default](components/crops/menu-flyout-default.png)

#### More button, open
The trigger after its own toggle; the open flyout shows in the crop. Read as `nav-more-open` on the home page.

**Values (opened).** size 81.66 x 28; background transparent; text apercuPro 22/28 400, #ffffff `color.neutral.white`; icon 24 x 24, #ffffff `color.neutral.white`.

![More button, open opened](components/crops/nav-more-open-opened.png)

### Marketing sections

The home and product-page sections: the display wordmark, the FAQ accordion, cards and the newsletter field.

#### Hero title
The "Endel" display wordmark at the top of the home page. Read as `hero-title` on the home page.

**Values (default).** size 149.42 x 72; background transparent; text apercuPro 60/72 400, #ffffff `color.neutral.white`.

![Hero title default](components/crops/hero-title-default.png)

#### Page ground
The near-black every page paints on. Read as `page-ground` on the home page.

**Values (default).** size 1440 x 12092.14; background #000000 `color.neutral.black`; text apercuPro 22/28 400, #ffffff `color.neutral.white`; icon 24 x 24, #ffffff `color.neutral.white`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Section title
Read as `section-title` on the home page.

**Values (default).** size 760 x 56; background transparent; text apercuPro 44/56 400, #ffffff `color.neutral.white`.

![Section title default](components/crops/section-title-default.png)

#### Body text
Read as `body-text` on the home page.

**Values (default).** size 564 x 56; background transparent; text apercuPro 22/28 400, #bfbfbf `color.neutral.300`.

![Body text default](components/crops/body-text-default.png)

#### Learn More link
Read as `learn-more` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 238 x 24; background transparent; text apercuPro 18/24 400, #ffffff `color.neutral.white` |
| hover | text apercuPro 18/24 400, #ffffff `color.neutral.white`, underline |
| focus-visible | shadow #666666 0px 0px 0px 6px; child paint a.Link-module__QL15TW__link.Link-module__QL15TW__color-white: size 238.0x24.0; shadow rgb(102, 102, 102) 0px 0px 0px 6px |
| pressed | text apercuPro 18/24 400, #ffffff `color.neutral.white`, underline |

![Learn More link default](components/crops/learn-more-default.png) ![Learn More link hover](components/crops/learn-more-hover.png) ![Learn More link focus-visible](components/crops/learn-more-focus-visible.png) ![Learn More link pressed](components/crops/learn-more-pressed.png)

#### Try Now link
Read as `try-now` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 516 x 28; background transparent; text apercuPro 22/28 400, #ffffff `color.neutral.white` |
| hover | text apercuPro 22/28 400, #ffffff `color.neutral.white`, underline |
| focus-visible | shadow #666666 0px 0px 0px 6px; child paint a.Link-module__QL15TW__link.Link-module__QL15TW__color-white: size 516.0x28.0; shadow rgb(102, 102, 102) 0px 0px 0px 6px |
| pressed | text apercuPro 22/28 400, #ffffff `color.neutral.white`, underline |

![Try Now link default](components/crops/try-now-default.png) ![Try Now link hover](components/crops/try-now-hover.png) ![Try Now link focus-visible](components/crops/try-now-focus-visible.png) ![Try Now link pressed](components/crops/try-now-pressed.png)

#### Round media button
The 72x72 circular play control over the product imagery. Measured, never pressed. Read as `play-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 72 x 72; border 2px solid #ffffff `color.neutral.white`; radius 100px; background #ffffff `color.neutral.white`; text apercuPro 22/22 400, #ffffff `color.neutral.white`; transition background-color 0.2s ease, border-color 0.2s ease; icon 36 x 36, #ffffff `color.neutral.white`, fill #000000 `color.neutral.black` |
| hover | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-full: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |
| focus-visible | shadow #666666 0px 0px 0px 6px; child paint button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-full: shadow rgb(102, 102, 102) 0px 0px 0px 6px |
| pressed | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-full: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |

![Round media button default](components/crops/play-button-default.png) ![Round media button hover](components/crops/play-button-hover.png) ![Round media button focus-visible](components/crops/play-button-focus-visible.png) ![Round media button pressed](components/crops/play-button-pressed.png)

#### Show More button
Loads more press quotes into the reviews waterfall; a local toggle, never pressed for real beyond states. Read as `show-more` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 368 x 56; padding 0px 24px; border 2px solid #ffffff `color.neutral.white`; radius 12px; background #262626 `color.neutral.700`; text apercuPro 22/22 400, #ffffff `color.neutral.white`; transition background-color 0.2s ease, border-color 0.2s ease |
| hover | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |
| focus-visible | shadow #666666 0px 0px 0px 6px; child paint button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic: shadow rgb(102, 102, 102) 0px 0px 0px 6px |
| pressed | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |

![Show More button default](components/crops/show-more-default.png) ![Show More button hover](components/crops/show-more-hover.png) ![Show More button focus-visible](components/crops/show-more-focus-visible.png) ![Show More button pressed](components/crops/show-more-pressed.png)

#### FAQ accordion item
A question row in the FAQ; its own press expands the answer. Opened once for the reading. Read as `accordion-title` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1152 x 76; radius 12px; background #191919 `color.neutral.800`; text apercuPro 22/28 400, #ffffff `color.neutral.white`; transition background-color 0.2s ease, border-color 0.2s ease; icon 24 x 24, #ffffff `color.neutral.white` |
| hover | background #262626 `color.neutral.700`; child paint button.AccordionTitle-module__8AYIsW__button: background #262626 `color.neutral.700` |
| focus-visible | shadow #666666 0px 0px 0px 6px; child paint button.AccordionTitle-module__8AYIsW__button: shadow rgb(102, 102, 102) 0px 0px 0px 6px |
| pressed | background #262626 `color.neutral.700`; child paint button.AccordionTitle-module__8AYIsW__button: background #262626 `color.neutral.700` |
| opened | background #262626 `color.neutral.700`; child paint button.AccordionTitle-module__8AYIsW__button.AccordionTitle-module__8AYIsW__open: size 1152.0x76.0; background #262626 `color.neutral.700`; radius 12px |

![FAQ accordion item default](components/crops/accordion-title-default.png) ![FAQ accordion item hover](components/crops/accordion-title-hover.png) ![FAQ accordion item focus-visible](components/crops/accordion-title-focus-visible.png) ![FAQ accordion item pressed](components/crops/accordion-title-pressed.png) ![FAQ accordion item opened](components/crops/accordion-title-opened.png)

#### FAQ answer
The answer panel under the open question. Read as `accordion-content` on the home page.

**Values (opened).** size 1152 x 228; background transparent; text apercuPro 22/28 400, #bfbfbf `color.neutral.300`.

Child layers that carry the look: div 1152x228 background #191919 `color.neutral.800` radius 12px.

![FAQ answer opened](components/crops/accordion-content-opened.png)

#### Newsletter email field
The newsletter signup input. Text was typed and deleted again; nothing was submitted. Read as `input-email` on the home page.

Not on the page when it was captured.

#### Subscribe button
Submits the newsletter form. Measured in all states, never pressed for real. Read as `btn-subscribe` on the home page.

Not on the page when it was captured.

#### Press logo
An outlet logo tile in the press wall. Measured, never followed. Read as `press-logo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 211.19 x 50.59; radius 8px; background transparent; text apercuPro 16/normal 400, #ffffff `color.neutral.white` |
| focus-visible | shadow #808080 0px 0px 0px 4px; child paint a.PressWall-module__GcOYjq__item: size 211.2x50.6; radius 8px; shadow rgb(128, 128, 128) 0px 0px 0px 4px |

![Press logo default](components/crops/press-logo-default.png) ![Press logo hover](components/crops/press-logo-hover.png) ![Press logo focus-visible](components/crops/press-logo-focus-visible.png) ![Press logo pressed](components/crops/press-logo-pressed.png)

#### Page title
The product page h1 ("Find your focus with Endel"). Read as `page-title` on the focus page.

**Values (default).** size 564 x 144; background transparent; text apercuPro 60/72 400, #ffffff `color.neutral.white`.

![Page title default](components/crops/page-title-default.png)

#### Soundscape card
A 270x270 soundscape tile linking its page (cover art, title, Try Now). Measured, never followed. Read as `soundscape-card` on the focus page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 270 x 270.39; background transparent; text apercuPro 16/0 400, #ffffff `color.neutral.white` |

Child layers that carry the look: div 270x88 image linear-gradient(transparent 0%, #000000 `color.neutral.black` 72.92%).

![Soundscape card default](components/crops/soundscape-card-default.png) ![Soundscape card hover](components/crops/soundscape-card-hover.png) ![Soundscape card focus-visible](components/crops/soundscape-card-focus-visible.png) ![Soundscape card pressed](components/crops/soundscape-card-pressed.png)

#### Scenario card
A scenario tile from the Timed Scenarios band (same Card module, second row). Read as `scenario-card` on the focus page.

**Values (default).** size 270 x 270; background transparent; text apercuPro 16/0 400, #ffffff `color.neutral.white`.

![Scenario card default](components/crops/scenario-card-default.png)

### Web app (signed out)

app.endel.io's explore page as a signed-out visitor sees it: the banner carousel, scenario pills, soundscape rows and the mini player.

#### App header
The signed-out web app bar: the FREEMIUM account chip and Sign In. Read as `app-header` on the web app's explore page.

**Values (default).** size 1440 x 72; padding 0px 32px; background transparent; image linear-gradient(#000000 `color.neutral.black`, rgba(0, 0, 0, 0.65) 50%, transparent); text apercuProRegular 12/12 400, #e0e0e0 `color.neutral.200`; icon 44 x 44, #ffffff `color.neutral.white`.

![App header default](components/crops/app-header-default.png)

#### FREEMIUM chip
The account state button; opens the account sheet. Measured, never opened (it gates on sign-in). Read as `user-button` on the web app's explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 158.13 x 44; background transparent; text apercuProRegular 12/12 400, #e0e0e0 `color.neutral.200`; icon 44 x 44, #ffffff `color.neutral.white` |

Child layers that carry the look: div 102.1x22 border 1px solid #808080 `color.neutral.500` radius 4px.

![FREEMIUM chip default](components/crops/user-button-default.png) ![FREEMIUM chip hover](components/crops/user-button-hover.png) ![FREEMIUM chip focus-visible](components/crops/user-button-focus-visible.png) ![FREEMIUM chip pressed](components/crops/user-button-pressed.png)

#### Sign In button (app)
Read as `app-btn-signin` on the web app's explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 73.58 x 44; padding 0px 12px; border 2px solid #262626 `color.neutral.700`; radius 12px; background #262626 `color.neutral.700`; text apercuProRegular 16/16 400, #ffffff `color.neutral.white`; transition background-color 0.2s ease, border-color 0.2s ease |
| hover | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |
| focus-visible | shadow #666666 0px 0px 0px 6px; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic: shadow rgb(102, 102, 102) 0px 0px 0px 6px |
| pressed | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |

![Sign In button (app) default](components/crops/app-btn-signin-default.png) ![Sign In button (app) hover](components/crops/app-btn-signin-hover.png) ![Sign In button (app) focus-visible](components/crops/app-btn-signin-focus-visible.png) ![Sign In button (app) pressed](components/crops/app-btn-signin-pressed.png)

#### Carousel banner
A promo card in the explore carousel (SPECIAL OFFER, product updates). Measured, never followed. Read as `banner` on the web app's explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 956 x 320; radius 24px; background transparent; outline 2px solid rgba(255, 255, 255, 0.15), offset -2px; text apercuProMedium 12/12 400, #000000 `color.neutral.black` |
| focus-visible | outline none |

Child layers that carry the look: a 956x320 radius 24px; div 121.7x21 background #ffffff `color.neutral.white` radius 24px.

![Carousel banner default](components/crops/banner-default.png) ![Carousel banner hover](components/crops/banner-hover.png) ![Carousel banner focus-visible](components/crops/banner-focus-visible.png) ![Carousel banner pressed](components/crops/banner-pressed.png)

#### Carousel dot
The selected pager dot under the banner carousel. Read as `banner-dot` on the web app's explore page.

**Values (default).** size 12 x 12; radius 50%; background #ffffff `color.neutral.white`; text Arial 13.33/normal 400, #000000 `color.neutral.black`.

![Carousel dot default](components/crops/banner-dot-default.png)

#### Scenario pill
A rounded-full scenario tag in the explore grid (Focus Timer, ASMR, Meditate…). Selecting one gates on premium; never pressed for real. Read as `scenario-pill` on the web app's explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 202.52 x 56; padding 0px 24px; border 2px solid #262626 `color.neutral.700`; radius 100px; background #262626 `color.neutral.700`; text apercuProRegular 22/22 400, #ffffff `color.neutral.white`; transition background-color 0.2s ease, border-color 0.2s ease; icon 24 x 24, #ffffff `color.neutral.white` |
| hover | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |
| focus-visible | shadow #666666 0px 0px 0px 6px; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full: shadow rgb(102, 102, 102) 0px 0px 0px 6px |
| pressed | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |

![Scenario pill default](components/crops/scenario-pill-default.png) ![Scenario pill hover](components/crops/scenario-pill-hover.png) ![Scenario pill focus-visible](components/crops/scenario-pill-focus-visible.png) ![Scenario pill pressed](components/crops/scenario-pill-pressed.png)

#### Soundscape row
A list row that opens a soundscape in the player (Focus, Colored Noises…). Measured; its destination is the public player. Read as `soundscape-row` on the web app's explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 956 x 56; background transparent; text apercuProRegular 28/28 400, #ffffff `color.neutral.white`; icon 56 x 56, #ffffff `color.neutral.white` |

![Soundscape row default](components/crops/soundscape-row-default.png) ![Soundscape row hover](components/crops/soundscape-row-hover.png) ![Soundscape row focus-visible](components/crops/soundscape-row-focus-visible.png) ![Soundscape row pressed](components/crops/soundscape-row-pressed.png)

#### Mini player
The fixed bottom bar with the paused soundscape and transport. Audio was never started. Read as `mini-player` on the web app's explore page.

**Values (default).** size 1440 x 120; padding 16px; background transparent; image linear-gradient(rgba(0, 0, 0, 0.05) 0%, #000000 `color.neutral.black` 85%); text apercuProRegular 14/14 400, #bfbfbf `color.neutral.300`; icon 56 x 56, #ffffff `color.neutral.white`.

![Mini player default](components/crops/mini-player-default.png)

### Player

The public player at app.endel.io/player/focus: mode icons, transport, volume and the Set Timer sheet.

#### Player header
The soundscape title bar over the visualizer (name + live energy state). Read as `player-header` on the web app's player page.

**Values (default).** size 1440 x 168; background transparent; text apercuProRegular 28/28 400, #ffffff `color.neutral.white`; icon 20 x 20, #ffffff `color.neutral.white`.

Child layers that carry the look: div 1440x56 background #2b2b2b; button 44x44 border 2px solid transparent radius 12px.

![Player header default](components/crops/player-header-default.png)

#### Soundscape title
Read as `player-title` on the web app's player page.

**Values (default).** size 72.25 x 28; background transparent; text apercuProRegular 28/28 400, #ffffff `color.neutral.white`.

![Soundscape title default](components/crops/player-title-default.png)

#### Close button
The icon button that leaves the player for Explore. Measured, never pressed. Read as `btn-close-player` on the web app's player page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44 x 44; border 2px solid transparent; radius 12px; background transparent; text apercuProRegular 16/16 400, #ffffff `color.neutral.white`; transition background-color 0.2s ease, border-color 0.2s ease; icon 20 x 20, #ffffff `color.neutral.white` |
| hover | border 2px solid #2b2b2b; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic: border 2px solid #2b2b2b |
| focus-visible | shadow #666666 0px 0px 0px 6px; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic: shadow rgb(102, 102, 102) 0px 0px 0px 6px |
| pressed | border 2px solid #2b2b2b; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic: border 2px solid #2b2b2b |

![Close button default](components/crops/btn-close-player-default.png) ![Close button hover](components/crops/btn-close-player-hover.png) ![Close button focus-visible](components/crops/btn-close-player-focus-visible.png) ![Close button pressed](components/crops/btn-close-player-pressed.png)

#### Set Timer button
Opens the shut-off timer dialog. Pressed once to read the dialog, closed again. Read as `btn-set-timer` on the web app's player page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 144.88 x 56; padding 0px 24px; border 2px solid #262626 `color.neutral.700`; radius 100px; background transparent; text apercuProRegular 22/22 400, #ffffff `color.neutral.white`; transition background-color 0.2s ease, border-color 0.2s ease |
| hover | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |
| focus-visible | shadow #666666 0px 0px 0px 6px; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full: shadow rgb(102, 102, 102) 0px 0px 0px 6px |
| pressed | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |

![Set Timer button default](components/crops/btn-set-timer-default.png) ![Set Timer button hover](components/crops/btn-set-timer-hover.png) ![Set Timer button focus-visible](components/crops/btn-set-timer-focus-visible.png) ![Set Timer button pressed](components/crops/btn-set-timer-pressed.png)

#### Mode button
One of the energy-mode icon buttons under the visualizer. Read as `button-mode` on the web app's player page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 56 x 56; background transparent; text apercuProRegular 16/0 400, #ffffff `color.neutral.white`; transition opacity 0.25s linear; icon 56 x 56, #ffffff `color.neutral.white` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured, not measured as absent.

![Mode button default](components/crops/button-mode-default.png) ![Mode button hover](components/crops/button-mode-hover.png) ![Mode button pressed](components/crops/button-mode-pressed.png)

#### Mode button, active
The engaged mode icon. Read as `button-mode-active` on the web app's player page.

**Values (default).** size 56 x 56; radius 56px; background transparent; text apercuProRegular 16/0 400, #ffffff `color.neutral.white`; icon 56 x 56, #ffffff `color.neutral.white`.

![Mode button, active default](components/crops/button-mode-active-default.png)

#### Transport button
A round transport control (play/skip). Audio was never started. Read as `player-control` on the web app's player page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 56 x 56; border 2px solid #191919 `color.neutral.800`; radius 100px; background #191919 `color.neutral.800`; text apercuProRegular 22/22 400, #ffffff `color.neutral.white`; transition background-color 0.2s ease, border-color 0.2s ease; icon 24 x 24, #ffffff `color.neutral.white` |
| hover | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |
| focus-visible | shadow #666666 0px 0px 0px 6px; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full: shadow rgb(102, 102, 102) 0px 0px 0px 6px |
| pressed | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |

![Transport button default](components/crops/player-control-default.png) ![Transport button hover](components/crops/player-control-hover.png) ![Transport button focus-visible](components/crops/player-control-focus-visible.png) ![Transport button pressed](components/crops/player-control-pressed.png)

#### Volume slider
The range control at the transport row's right end. Never dragged. Read as `volume` on the web app's player page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 129 x 5; radius 20px; background transparent; image linear-gradient(to right, #ffffff `color.neutral.white` 100%, #808080 `color.neutral.500` 100%); text Arial 13.33/normal 400, #101010 `measured.sliderBase`; placeholder #101010 `measured.sliderBase` |

![Volume slider default](components/crops/volume-default.png) ![Volume slider focused](components/crops/volume-focused.png)

#### Explore button
The back-to-explore pill in the player footer. Measured, never followed. Read as `btn-explore` on the web app's player page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 324 x 58; padding 16px 0px 14px 0px; radius 20px 20px 0px 0px; background transparent; image linear-gradient(#191919 `color.neutral.800` 0%, #000000 `color.neutral.black` 100%); text apercuProRegular 22/normal 400, #ffffff `color.neutral.white` |
| hover | transform translate(0px, -8px) |

![Explore button default](components/crops/btn-explore-default.png) ![Explore button hover](components/crops/btn-explore-hover.png) ![Explore button focus-visible](components/crops/btn-explore-focus-visible.png) ![Explore button pressed](components/crops/btn-explore-pressed.png)

#### Shut-off timer dialog
The bottom sheet Set Timer opens: duration chips, the premium Unlock and Done rows. Unlock was measured, never pressed. Read as `timer-dialog` on the web app's player page.

**Values (opened).** size 1440 x 583; padding 16px 0px; background rgba(0, 0, 0, 0.8); text apercuProRegular 28/normal 400, #ffffff `color.neutral.white`.

![Shut-off timer dialog opened](components/crops/timer-dialog-opened.png)

#### Unlock button
The premium upsell inside the timer dialog. Measured, never pressed (it starts checkout). Read as `btn-unlock` on the web app's player page.

**Values (opened).** size 300 x 56; padding 0px 24px; border 2px solid #ffffff `color.neutral.white`; radius 12px; background #262626 `color.neutral.700`; text apercuProRegular 22/22 400, #ffffff `color.neutral.white`; transition background-color 0.2s ease, border-color 0.2s ease.

![Unlock button opened](components/crops/btn-unlock-opened.png)

### Sign-in card

The sign-in/register panel the app's own Sign In button navigates to.

#### Sign-in card
The "Sign In or Register" panel: an empty email field, Continue, and three icon-only identity-provider buttons (Google, Apple, Facebook). Nothing was typed or submitted. The provider buttons were not clicked. Read as `login-card` on the web app's sign-in page.

**Values (default).** size 564 x 665; padding 88px 0px; background transparent; text apercuProRegular 44/normal 400, #ffffff `color.neutral.white`; icon 24 x 24, #ffffff `color.neutral.white`.

Child layers that carry the look: input 564x62 border 2px solid #808080 `color.neutral.500` radius 12px; button 564x56 background #262626 `color.neutral.700` border 2px solid #ffffff `color.neutral.white` radius 12px; div::before 258.141pxx2px image linear-gradient(90deg, transparent 0%, #262626 `color.neutral.700` 100%) radius 2px.

![Sign-in card default](components/crops/login-card-default.png)

#### Email field (sign-in)
Read default and focused; no address was ever typed on this page. Read as `input-email-login` on the web app's sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 564 x 62; padding 16px 12px 14px 12px; border 2px solid #808080 `color.neutral.500`; radius 12px; background transparent; text apercuProRegular 22/22 400, #ffffff `color.neutral.white`; placeholder transparent |
| focused | border 2px solid #ffffff `color.neutral.white`; child paint input.Input-module__iEWt7a__input: border 2px solid #ffffff `color.neutral.white` |

![Email field (sign-in) default](components/crops/input-email-login-default.png) ![Email field (sign-in) focused](components/crops/input-email-login-focused.png)

#### Continue button
Submits the sign-in form. Measured in all states, never pressed for real. Read as `btn-continue` on the web app's sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 564 x 56; padding 0px 24px; border 2px solid #ffffff `color.neutral.white`; radius 12px; background #262626 `color.neutral.700`; text apercuProRegular 22/22 400, #ffffff `color.neutral.white`; transition background-color 0.2s ease, border-color 0.2s ease |
| hover | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |
| focus-visible | shadow #666666 0px 0px 0px 6px; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic: shadow rgb(102, 102, 102) 0px 0px 0px 6px |
| pressed | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |

![Continue button default](components/crops/btn-continue-default.png) ![Continue button hover](components/crops/btn-continue-hover.png) ![Continue button focus-visible](components/crops/btn-continue-focus-visible.png) ![Continue button pressed](components/crops/btn-continue-pressed.png)

#### Identity-provider button
The Google icon button on the sign-in card. Apple and Facebook sit beside it. Measured, never pressed. Read as `btn-oauth` on the web app's sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 180 x 56; padding 0px 24px; border 2px solid #262626 `color.neutral.700`; radius 12px; background #262626 `color.neutral.700`; text apercuProRegular 22/22 400, #ffffff `color.neutral.white`; transition background-color 0.2s ease, border-color 0.2s ease; icon 24 x 24, #ffffff `color.neutral.white` |
| hover | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |
| focus-visible | shadow #666666 0px 0px 0px 6px; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic: shadow rgb(102, 102, 102) 0px 0px 0px 6px |
| pressed | border 2px solid #808080 `color.neutral.500`; background #808080 `color.neutral.500`; child paint button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic: background #808080 `color.neutral.500`; border 2px solid #808080 `color.neutral.500` |

![Identity-provider button default](components/crops/btn-oauth-default.png) ![Identity-provider button hover](components/crops/btn-oauth-hover.png) ![Identity-provider button focus-visible](components/crops/btn-oauth-focus-visible.png) ![Identity-provider button pressed](components/crops/btn-oauth-pressed.png)

### Footer

The link columns, the newsletter field, stores, socials and legal.

#### Footer
The big footer: Explore and product link columns, stores, legal and socials. Read as `footer` on the home page.

**Values (default).** size 1280 x 569; padding 0px 64px; background transparent; text apercuPro 14/20 400, #bfbfbf `color.neutral.300`.

Child layers that carry the look: input 466x56 border 2px solid #808080 `color.neutral.500` radius 12px; button 466x56 background #262626 `color.neutral.700` border 2px solid #262626 `color.neutral.700` radius 12px; div 1152x73 border 1px solid #191919 `color.neutral.800`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 103.69 x 24; background transparent; text apercuPro 18/24 400, #ffffff `color.neutral.white` |
| hover | text apercuPro 18/24 400, #ffffff `color.neutral.white`, underline |
| focus-visible | shadow #666666 0px 0px 0px 6px; child paint a.Link-module__QL15TW__link.Link-module__QL15TW__color-white: size 103.7x24.0; shadow rgb(102, 102, 102) 0px 0px 0px 6px |
| pressed | text apercuPro 18/24 400, #ffffff `color.neutral.white`, underline |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer social icon
Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 24 x 24; background transparent; text apercuPro 16/0 400, #ffffff `color.neutral.white` |
| hover | opacity 0.7 |
| focus-visible | shadow #666666 0px 0px 0px 4px; child paint a.Link-module__QL15TW__link.Link-module__QL15TW__color-white: size 24.0x24.0; shadow rgb(102, 102, 102) 0px 0px 0px 4px |
| pressed | opacity 0.7 |

![Footer social icon default](components/crops/footer-social-default.png) ![Footer social icon hover](components/crops/footer-social-hover.png) ![Footer social icon focus-visible](components/crops/footer-social-focus-visible.png) ![Footer social icon pressed](components/crops/footer-social-pressed.png)

#### Legal link
Read as `footer-legal` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 106.92 x 24; background transparent; text apercuPro 18/24 400, #bfbfbf `color.neutral.300` |
| hover | text apercuPro 18/24 400, #ffffff `color.neutral.white`, underline |
| focus-visible | shadow #666666 0px 0px 0px 6px; child paint a.Link-module__QL15TW__link.Link-module__QL15TW__color-gray-4: size 106.9x24.0; shadow rgb(102, 102, 102) 0px 0px 0px 6px |
| pressed | text apercuPro 18/24 400, #ffffff `color.neutral.white`, underline |

![Legal link default](components/crops/footer-legal-default.png) ![Legal link hover](components/crops/footer-legal-hover.png) ![Legal link focus-visible](components/crops/footer-legal-focus-visible.png) ![Legal link pressed](components/crops/footer-legal-pressed.png)

### Mobile (390 wide)

The same surfaces at phone width, with the full-screen Menu.

#### Mobile header
The 56px bar: mark, Try Today and the Menu trigger. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 56; background transparent; image linear-gradient(#000000 `color.neutral.black` 0%, rgba(0, 0, 0, 0.65) 50%, transparent 100%); text apercuPro 16/22 400, #ffffff `color.neutral.white`.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
Opens the full-screen nav inside the header; pressed once for the open reading, closed again. Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 81.11 x 36; padding 0px 12px; border 2px solid #262626 `color.neutral.700`; radius 12px; background #262626 `color.neutral.700`; text apercuPro 12/12 400, #ffffff `color.neutral.white`; transition background-color 0.2s ease, border-color 0.2s ease; icon 16 x 16, #ffffff `color.neutral.white` |
| focus-visible | shadow #666666 0px 0px 0px 6px; child paint button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic: shadow rgb(102, 102, 102) 0px 0px 0px 6px |

![Menu button default](components/crops/m-menu-button-default.png) ![Menu button hover](components/crops/m-menu-button-hover.png) ![Menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Menu button pressed](components/crops/m-menu-button-pressed.png) ![Menu button opened](components/crops/m-menu-button-opened.png)

#### Mobile menu, open
A promo row in the open menu (students / teams / gift cards). Read while held open. Read as `m-menu-flyout` on the home page at 390 wide.

**Values (default).** size 326 x 44; radius 4px; background transparent; text apercuPro 16/22 400, #ffffff `color.neutral.white`.

![Mobile menu, open default](components/crops/m-menu-flyout-default.png)

#### Hero title (mobile)
Read as `m-hero-title` on the home page at 390 wide.

**Values (default).** size 90.36 x 42; background transparent; text apercuPro 36/42 400, #ffffff `color.neutral.white`.

![Hero title (mobile) default](components/crops/m-hero-title-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Endel's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **The signed-in app.** app.endel.io was captured signed out only: the FREEMIUM account chip, the scenario pills' premium selection, the timer sheet's Unlock row (which starts checkout) and the sign-in form's Continue and OAuth buttons were measured but never pressed for real. Everything behind an account — library, sync, settings, purchase — is a boundary.
- **Anything that sends or signs in.** No form was submitted and no account was created; the newsletter field, the sign-in card's email field, Try Today/Subscribe/Continue/Unlock and every outbound link were measured, never submitted or followed.
- **The native apps.** iOS/Android/macOS builds and the Apple Watch/TV surfaces the site advertises are not in this package.
- **The newsletter row.** The home page's mid-page newsletter signup (input-email, btn-subscribe) was not on the page at capture time; the footer's own newsletter field was painted instead.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

Both hosts paint one dark theme on every captured route; the bundles declare no light variant, so no light set is emitted.

### Fonts

- **The UI font** is apercuPro, a Next.js-served webfont plus a metric-matched local-Arial fallback (`fonts` in [raw/css-vars.json](raw/css-vars.json)); the font files themselves are not committed.
- Cover art, press logos, the Endel mark and the player visualizer in the screenshots are Endel's property.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Soundscape cover art, the player visualizer imagery, press logos and the wordmark are Endel's content; only the frames and components were measured.
