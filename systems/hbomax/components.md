# HBO Max components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Read from www.hbomax.com/sg/en on 2026-11-17, signed out, in headed Chromium under Xvfb at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Later recaptures merge into the same file, so every entry names the date its own states were read; a state a re-read missed keeps its earlier date and says so. Nothing was signed into, bought, searched or submitted; the only presses were local UI toggles the page's own chrome provides — the hero carousel's Next arrow, the billing toggle, an FAQ chevron, the language selector and the phone's menu button; every link was measured, never followed.

**Where this was read.** `hbomax.com` redirects to `www.hbomax.com`, which serves the marketing site in the visitor's locale — the capture host resolved to Singapore, so everything below is the `/sg/en` locale (title 'HBO Max | Stream Series and Movies', canonical www.hbomax.com). Akamai's edge returns a 403 'Access Denied' page to headless Chromium, so every capture here ran headed under Xvfb — that block is documented as an access constraint, not worked around. The app itself (play.hbomax.com), sign-in and checkout (auth.hbomax.com) and the help centre (help.hbomax.com) are separate signed-in or out-of-scope surfaces, listed under Gaps.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (41 components, 62 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 16/20.8 400, #000000`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (49 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png` where `{theme}` is the surface the page painted at capture: every www.hbomax.com page ships one theme — `html data-theme="max"`, a dark surface — so every shot is `-dark-`. Desktop shots are 1440 x 900 at 1x; `-full` shots are the whole document bounded at eight GPU-texture chunks (the over-cap remainder recorded as `.partN.png` with the boundary in the shot's `.capture.json` sidecar); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x). The cookie-consent modal shot is `-promo`; `carousel-next`, `plan-yearly` and `faq-open` are the same page after each control's own press.

| Surface | URL | Screenshots |
|---|---|---|
| Home (marketing) | `/sg/en` | [carousel-next](screenshots/home-dark-carousel-next.png), [default](screenshots/home-dark-default.png), [faq-open](screenshots/home-dark-faq-open.png), [full](screenshots/home-dark-full.png), [plan-yearly](screenshots/home-dark-plan-yearly.png), [promo](screenshots/home-dark-promo.png) |
| Movies browse | `/sg/en/movies` | [default](screenshots/movies-dark-default.png), [full](screenshots/movies-dark-full.png) |
| Series browse | `/sg/en/shows` | [default](screenshots/shows-dark-default.png), [full](screenshots/shows-dark-full.png) |
| Channel hub | `/sg/en/channel` | [default](screenshots/channel-dark-default.png), [full](screenshots/channel-dark-full.png) |
| Series detail | `/sg/en/show/e6e7bad9-d48d-4434-b334-7c651ffc4bdf` | [default](screenshots/show-dark-default.png), [full](screenshots/show-dark-full.png) |
| Movie detail | `/sg/en/movie/710798da-f811-40be-9ed9-3a7443e36278` | [default](screenshots/movie-dark-default.png), [full](screenshots/movie-dark-full.png) |
| Kids & Family collection | `/sg/en/collections/genre/kids-family` | [default](screenshots/collection-dark-default.png), [full](screenshots/collection-dark-full.png) |
| Sitemap | `/sg/en/sitemap` | [default](screenshots/sitemap-dark-default.png), [full](screenshots/sitemap-dark-full.png) |
| Corporate information | `/sg/en/corp-info` | [default](screenshots/corp-info-dark-default.png), [full](screenshots/corp-info-dark-full.png) |
| Privacy policy | `/privacy` | [default](screenshots/privacy-dark-default.png), [full](screenshots/privacy-dark-full.png) |
| Home, phone | `/sg/en` | [default](screenshots/mobile-home-dark-default.png), [full](screenshots/mobile-home-dark-full.png), [promo](screenshots/mobile-home-dark-promo.png) |
| Movies browse, phone | `/sg/en/movies` | [default](screenshots/mobile-movies-dark-default.png), [full](screenshots/mobile-movies-dark-full.png) |
| Series detail, phone | `/sg/en/show/e6e7bad9-d48d-4434-b334-7c651ffc4bdf` | [default](screenshots/mobile-show-dark-default.png), [full](screenshots/mobile-show-dark-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie consent modal | home (fresh visit) | the page's own modal, captured as it loaded, then hidden without accepting or rejecting for the rest of the pass | [home-dark-promo](screenshots/home-dark-promo.png), [mobile-home-dark-promo](screenshots/mobile-home-dark-promo.png), [consent-dialog](#consent-modal) |
| Hero carousel next slide | home hero | the carousel's own Next-arrow press — the slide advanced one step | [home-dark-carousel-next](screenshots/home-dark-carousel-next.png), [hero-next](#carousel-next-control) |
| Yearly billing | home plans | the billing toggle's own press — the card prices repainted | [home-dark-plan-yearly](screenshots/home-dark-plan-yearly.png), [plan-toggle](#billing-period-toggle) |
| FAQ item open | home FAQ | a question's own chevron press — the answer expanded | [home-dark-faq-open](screenshots/home-dark-faq-open.png), [faq-item](#faq-accordion-item) |
| Language selector | home footer | the selector's own press — the locale list opened, nothing chosen | [lang-selector](#language-selector) |
| Mobile navigation | home, phone width | the menu button's own press | [m-nav-open](#mobile-nav-open) |
| Sign in, subscribe and checkout | auth.hbomax.com | signed-in surface — never opened; every CTA pointing at it was measured, never followed | boundary; see Gaps |
| The app (play.hbomax.com) and help centre (help.hbomax.com) | player and help | separate surfaces outside the signed-out marketing site — never opened | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 1 components were given a real keyboard focus. 1 draw an outline ring: `consent-accept` (on a child: 3px solid rgb(0, 0, 0) offset -6px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `ease` | opacity | hero-next |
| 0.2s | `cubic-bezier(0, 0, 0.34, 1)` | background-color, color, opacity | consent-accept, consent-manage, detail-cta, footer-legal-link, header-signin, hero-cta, lang-selector, m-hero-cta and more |
| 0.5s | `ease-in-out` | all, background-color | header-bar, hero-indicator, hero-slide, m-header |
| 1s | `ease` | opacity, transform | plan-section |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Consent modal](#consent-modal) | 1425 x 900 | - | - | transparent | none | 0 |
| [Title card link](#title-card-link) | 350 x 141.05 | - | - | transparent | none | 0 |
| [FAQ section](#faq-section) | 1425 x 391 | - | - | transparent | none | 0 |
| [Active carousel slide](#active-carousel-slide) | 1096 x 430.97 | - | - | transparent | none | 0 |

## Components

### Site chrome

The fixed shell every marketing page carries: the translucent navbar over the hero (the HBO Max wordmark, section links and the Sign In pill that leads to auth.hbomax.com — measured, never followed).

#### Fixed navigation bar
The translucent gradient bar over every page: HBO Max wordmark, nav links and the Sign In button. Read as `header-bar` on the home page.
Read on 2026-11-17T06:33:27.284Z.

**Values (default).** size 1425 x 60; padding 8px 16px; background rgba(0, 0, 0, 0.7) `dark.color.component.button.utility.overlay.fill.base`; text Max Sans 15.38/20.76 700, #ffffff `dark.color.action.primary.fill.high`; transition background-color 0.5s ease-in-out.

![Fixed navigation bar default](components/crops/header-bar-default.png)

#### HBO Max wordmark
The wordmark link at the left of the navbar. Read as `header-logo` on the home page.

Not on the page when it was captured.

#### Navbar link
A section link in the navbar (Browse, Series, Movies — whichever renders). Read as `header-nav-link` on the home page.

Not on the page when it was captured.

#### "Sign In" button
The pill button that leads to auth.hbomax.com — hovered and focused only, never pressed (pressing would leave the public site). Read as `header-signin` on the home page.
States read on 2026-11-17T06:33:28.329Z (default); 2026-11-17T06:33:30.290Z (hover); 2026-11-17T06:33:37.027Z (focus-visible); 2026-11-17T06:33:45.499Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 136 x 44; padding 10px 18px; radius 8px; background transparent; text Max Sans 15.38/20.76 700, #ffffff `dark.color.action.primary.fill.high`; transition background-color 0.2s cubic-bezier(0, 0, 0.34, 1), color 0.2s cubic-bezier(0, 0, 0.34, 1), opacity 0.2s cubic-bezier(0, 0, 0.34, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

!["Sign In" button default](components/crops/header-signin-default.png) !["Sign In" button hover](components/crops/header-signin-hover.png) !["Sign In" button pressed](components/crops/header-signin-pressed.png)

### Hero

The full-bleed autoplay carousel under the navbar (Bootstrap markup): backdrop art per slide, a 'Start Subscription' CTA, the Next control and the slide indicators.

#### Hero carousel
The full-bleed autoplay carousel under the navbar — backdrop art, title treatment, a "Start Subscription" CTA per slide. Read as `hero-carousel` on the home page.
Read on 2026-11-17T06:34:00.000Z.

**Values (default).** size 1425 x 694.22; background transparent; text Max Sans 35/47.25 600, #ffffff `dark.color.action.primary.fill.high`; icon 14 x 26, #ffffff `dark.color.action.primary.fill.high`; layers li 256.1x98.6 T:10px solid / B:10px solid 100%; li 292.1x98.6 T:10px solid / B:10px solid 100%; li 410.6x98.6 T:10px solid / B:10px solid 100%; li.active 261.8x98.6 T:10px solid / B:10px solid 100%; li 244.0x98.6 T:10px solid / B:10px solid 100%; li 239.6x98.6 T:10px solid / B:10px solid 100%.

Child layers that carry the look: li 256.1x98.6 border 10px solid radius 100%; li 292.1x98.6 border 10px solid radius 100%; li 410.6x98.6 border 10px solid radius 100%.

![Hero carousel default](components/crops/hero-carousel-default.png)

#### Slide CTA ("Start Subscription")
The white pill call-to-action in the active slide — an auth.hbomax.com link, hovered and focused but never pressed. Read as `hero-cta` on the home page.
States read on 2026-11-17T06:34:10.364Z (pressed); 2026-11-17T06:34:17.025Z (default); 2026-11-17T06:34:19.573Z (hover); 2026-11-17T06:34:25.278Z (focus-visible). `pressed` failed at capture (cdpSession.send: Protocol error (DOM.getNodeForLocation): No node found at given location).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 140.41 x 44; padding 10px 18px; radius 8px; background transparent; text Max Sans 15.38/20.76 700, #000000 `dark.color.surface.low`; transition background-color 0.2s cubic-bezier(0, 0, 0.34, 1), color 0.2s cubic-bezier(0, 0, 0.34, 1), opacity 0.2s cubic-bezier(0, 0, 0.34, 1); layers ::before rgb(221, 221, 221) 0px none 1; a::before.sc-bfd2ca80-0.dDxZmm 140.406pxx44px rgb(221, 221, 221) 8px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: a::before 140.406pxx44px background #dddddd `dark.color.action.neutral.border.mid` radius 8px.

![Slide CTA ("Start Subscription") default](components/crops/hero-cta-default.png) ![Slide CTA ("Start Subscription") hover](components/crops/hero-cta-hover.png)

#### Carousel "Next" control
The arrow that advances the hero — "opened" is the slide reached by its own press (a local UI toggle). Read as `hero-next` on the home page.
States read on 2026-11-17T06:34:27.930Z (default); 2026-11-17T06:34:31.430Z (hover); 2026-11-17T06:34:37.153Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, opened) | size 76.72 x 488.56; background transparent; text Max Sans 18/28.8 400, #ffffff `dark.color.action.primary.fill.high`; transition opacity 0.15s ease; opacity 0.5; icon 14 x 26, #ffffff `dark.color.action.primary.fill.high` |

![Carousel "Next" control default](components/crops/hero-next-default.png) ![Carousel "Next" control hover](components/crops/hero-next-hover.png) ![Carousel "Next" control opened](components/crops/hero-next-opened.png)

#### Carousel indicator
A slide indicator tab under the hero. Read as `hero-indicator` on the home page.
States read on 2026-11-17T06:34:39.252Z (default); 2026-11-17T06:34:43.734Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 256.09 x 98.63; padding 0px 56px; border T: 10px solid transparent; B: 10px solid transparent; radius 100%; background transparent; text Max Sans 56/89.6 100, #ffffff `dark.color.action.primary.fill.high`; transition all 0.5s ease-in-out; transform scale(0.9); opacity 0.5 |

![Carousel indicator default](components/crops/hero-indicator-default.png) ![Carousel indicator hover](components/crops/hero-indicator-hover.png)

#### Active carousel slide
The currently painted slide: backdrop image, title and meta row. Read as `hero-slide` on the home page.
Read on 2026-11-17T06:34:09.360Z.

**Values (default).** size 1096 x 430.97; background transparent; text Max Sans 18/28.8 400, #ffffff `dark.color.action.primary.fill.high`; transition all 0.5s ease-in-out.

![Active carousel slide default](components/crops/hero-slide-default.png)

### Plans

The subscription section: the monthly/yearly billing toggle, the tier cards and their Choose buttons — hovered and focused, never pressed.

#### Plans section
The "Choose your plan" section: billing toggle plus the tier cards. Read as `plan-section` on the home page.
Read on 2026-11-17T06:34:49.620Z.

**Values (default).** size 1425 x 591; background transparent; image url(…); text Max Sans 64/86.4 700, #ffffff `dark.color.action.primary.fill.high`; transition opacity 1s ease, transform 1s ease; icon 83.45 x 59.98, #ffffff `dark.color.action.primary.fill.high`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Plans section default](components/crops/plan-section-default.png)

#### Plan tier card
One subscription tier card: name, price, feature list and its Choose button. Read as `plan-card` on the home page.

Not on the page when it was captured.

#### Billing period toggle
The monthly/yearly switch above the cards. "opened" is the prices repainted by its own press — the plan-yearly screenshot shows the result. Read as `plan-toggle` on the home page.

Not on the page when it was captured.

#### "Choose" plan button
The button on a tier card that leads to checkout — hovered and focused only, never pressed. Read as `plan-choose` on the home page.
States read on 2026-11-17T06:34:49.631Z (pressed); 2026-11-17T06:34:50.820Z (default); 2026-11-17T06:34:57.440Z (hover); 2026-11-17T06:35:03.333Z (focus-visible). `pressed` failed at capture (cdpSession.send: Protocol error (DOM.getNodeForLocation): No node found at given location).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 292.95 x 52; padding 10px 30px; radius 8px; background transparent; text Max Sans 20/27 700, #000000 `dark.color.surface.low`; transition background-color 0.2s cubic-bezier(0, 0, 0.34, 1), color 0.2s cubic-bezier(0, 0, 0.34, 1), opacity 0.2s cubic-bezier(0, 0, 0.34, 1); layers ::before rgb(221, 221, 221) 0px none 1; a::before.sc-bfd2ca80-0.dDxZmm 292.953pxx52px rgb(221, 221, 221) 8px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: a::before 292.953pxx52px background #dddddd `dark.color.action.neutral.border.mid` radius 8px.

!["Choose" plan button default](components/crops/plan-choose-default.png) !["Choose" plan button hover](components/crops/plan-choose-hover.png)

### FAQ

The 'Questions' accordion near the foot of the home page, opened by its own chevron.

#### FAQ section
The "Questions" accordion near the foot of the home page. Read as `faq-section` on the home page.
Read on 2026-11-17T06:35:09.101Z.

**Values (default).** size 1425 x 391; background transparent; text Max Sans 20/27 700, #ffffff `dark.color.action.primary.fill.high`; icon 24 x 24, #ffffff `dark.color.action.primary.fill.high`; layers div.sc-24ae6219-0.iVmMkq 920.0x391.0 rgba(221, 221, 221, 0.1) 8px; div.sc-7be0c765-0.kYwFex 872.0x1.0 rgba(255, 255, 255, 0.3); div.sc-7be0c765-0.kYwFex 872.0x1.0 rgba(255, 255, 255, 0.3); div.sc-7be0c765-0.kYwFex 872.0x1.0 rgba(255, 255, 255, 0.3); div.sc-7be0c765-0.kYwFex 872.0x1.0 rgba(255, 255, 255, 0.3); div.sc-7be0c765-0.kYwFex 872.0x1.0 rgba(255, 255, 255, 0.3).

Child layers that carry the look: div 920x391 background rgba(221, 221, 221, 0.1) `dark.color.action.neutral.fill.mid` radius 8px; div 872x1 background rgba(255, 255, 255, 0.3) `dark.color.component.button.quiet.player.progress.track.time.base`; div 872x1 background rgba(255, 255, 255, 0.3) `dark.color.component.button.quiet.player.progress.track.time.base`.

![FAQ section default](components/crops/faq-section-default.png)

#### FAQ accordion item
One question row. "opened" is its own chevron press revealing the answer. Read as `faq-item` on the home page.
States read on 2026-11-17T06:35:11.026Z (default); 2026-11-17T06:35:13.359Z (hover); 2026-11-17T06:35:14.860Z (focus-visible); 2026-11-17T06:35:18.918Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, opened) | size 920 x 55; padding 14px 24px; background transparent; text Max Sans 20/27 700, #ffffff `dark.color.action.primary.fill.high`; icon 24 x 24, #ffffff `dark.color.action.primary.fill.high` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![FAQ accordion item default](components/crops/faq-item-default.png) ![FAQ accordion item hover](components/crops/faq-item-hover.png) ![FAQ accordion item opened](components/crops/faq-item-opened.png)

### Content rails

The horizontal 'Discover' rows of poster cards on the home and browse pages, each card a link to a title detail page.

#### Content rail
A horizontal "Discover" row of title cards. Read as `rail-section` on the home page.

Not on the page when it was captured.

#### Title card link
A poster card in a rail — a link to the title's detail page. Read as `rail-card` on the home page.
States read on 2026-11-17T06:35:34.456Z (default); 2026-11-17T06:35:37.926Z (hover); 2026-11-17T06:35:41.803Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 350 x 141.05; background transparent; text Max Sans 14/18.9 600, #ffffff `dark.color.action.primary.fill.high` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Title card link default](components/crops/rail-card-default.png) ![Title card link hover](components/crops/rail-card-hover.png)

#### Content rail
A horizontal "Discover" row of title cards. Read as `browse-rail-section` on the movies browse page.
Read on 2026-11-17T06:29:20.842Z.

**Values (default).** size 1425 x 768; background transparent; image url(…); text Max Sans 48/57.6 600, #ffffff `dark.color.action.primary.fill.high`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Title card link
A poster card in a browse row — a link to the title's detail page. Read as `browse-rail-card` on the movies browse page.
States read on 2026-11-17T06:29:48.725Z (default); 2026-11-17T06:29:51.783Z (hover); 2026-11-17T06:29:53.886Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 315 x 201.28; background transparent; text Max Sans 11.83/16.09 700, rgba(255, 255, 255, 0.8) `dark.color.general.border.low`; layers div.sc-72c045a5-0.emcCTt 323.0x185.2 T:2px solid / R:2px solid / B:2px solid / L:2px solid 4px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: div 323x185.2 border 2px solid radius 4px.

![Title card link default](components/crops/browse-rail-card-default.png) ![Title card link hover](components/crops/browse-rail-card-hover.png)

### Footer

The link columns, the legal row and the language selector at the bottom of every page.

#### Site footer
The footer: link columns, the legal row and the language selector. Read as `footer` on the home page.

Not on the page when it was captured.

#### Footer link
A link in the footer columns. Read as `footer-link` on the home page.

Not on the page when it was captured.

#### Legal link
A link in the footer's legal row (Privacy Policy, Terms of Use). Read as `footer-legal-link` on the home page.
States read on 2026-11-17T06:35:45.312Z (default); 2026-11-17T06:35:47.736Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 136 x 44; padding 10px 18px; radius 8px; background transparent; text Max Sans 15.38/20.76 700, #ffffff `dark.color.action.primary.fill.high`; transition background-color 0.2s cubic-bezier(0, 0, 0.34, 1), color 0.2s cubic-bezier(0, 0, 0.34, 1), opacity 0.2s cubic-bezier(0, 0, 0.34, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1 |

![Legal link default](components/crops/footer-legal-link-default.png) ![Legal link hover](components/crops/footer-legal-link-hover.png)

#### Language selector
The "English" selector in the footer. "opened" is its own press listing the locales — a local UI toggle, no locale is switched. Read as `lang-selector` on the home page.
States read on 2026-11-17T06:35:50.448Z (default); 2026-11-17T06:35:52.933Z (hover); 2026-11-17T06:35:56.577Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, opened) | size 224 x 52; padding 4px 14px 4px 24px; radius 8px; background rgba(62, 62, 62, 0.75) `dark.color.action.secondary.fill.mid`; text Max Sans 20/27 700, #ffffff `dark.color.action.primary.fill.high`; transition background-color 0.2s cubic-bezier(0, 0, 0.34, 1); icon 24 x 24, #ffffff `dark.color.action.primary.fill.high` |

![Language selector default](components/crops/lang-selector-default.png) ![Language selector hover](components/crops/lang-selector-hover.png) ![Language selector opened](components/crops/lang-selector-opened.png)

### Title detail

The backdrop hero, display title, meta row and subscribe CTA on the series and movie detail pages.

#### Detail backdrop hero
The full-bleed backdrop area on a title detail page. Read as `detail-hero` on the series detail page.
Read on 2026-11-17T06:27:39.259Z.

**Values (default).** size 1425 x 842; background transparent; image url(…); text Max Sans 17/27.2 600, #ffffff `dark.color.action.primary.fill.high`; icon 20 x 20, #ffffff `dark.color.action.primary.fill.high`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Detail backdrop hero default](components/crops/detail-hero-default.png)

#### Title heading
The title's display heading on the detail page. Read as `detail-title` on the series detail page.
Read on 2026-11-17T06:27:40.167Z.

**Values (default).** size 59.73 x 27.19; background transparent; text Max Sans 17/27.2 700, #ffffff `dark.color.action.primary.fill.high`.

![Title heading default](components/crops/detail-title-default.png)

#### Meta row
The year · rating · runtime/seasons line under the title. Read as `detail-meta` on the series detail page.

Not on the page when it was captured.

#### Detail "Start Subscription" CTA
The subscribe call-to-action on a title page — an auth link, hovered and focused only. Read as `detail-cta` on the series detail page.
States read on 2026-11-17T06:27:40.176Z (pressed); 2026-11-17T06:27:41.071Z (default); 2026-11-17T06:27:43.051Z (hover); 2026-11-17T06:27:44.399Z (focus-visible). `pressed` failed at capture (cdpSession.send: Protocol error (DOM.getNodeForLocation): No node found at given location).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 140.41 x 44; padding 10px 18px; radius 8px; background transparent; text Max Sans 15.38/20.76 700, #000000 `dark.color.surface.low`; transition background-color 0.2s cubic-bezier(0, 0, 0.34, 1), color 0.2s cubic-bezier(0, 0, 0.34, 1), opacity 0.2s cubic-bezier(0, 0, 0.34, 1); layers ::before rgb(221, 221, 221) 0px none 1; a::before.sc-bfd2ca80-0.dDxZmm 140.406pxx44px rgb(221, 221, 221) 8px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: a::before 140.406pxx44px background #dddddd `dark.color.action.neutral.border.mid` radius 8px.

![Detail "Start Subscription" CTA default](components/crops/detail-cta-default.png) ![Detail "Start Subscription" CTA hover](components/crops/detail-cta-hover.png)

#### Detail backdrop hero
The full-bleed backdrop area on a title detail page. Read as `movie-detail-hero` on the movie detail page.
Read on 2026-11-17T06:28:19.272Z.

**Values (default).** size 1425 x 842; background transparent; image url(…); text Max Sans 17/27.2 600, #ffffff `dark.color.action.primary.fill.high`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Detail backdrop hero default](components/crops/movie-detail-hero-default.png)

#### Title heading
The title's display heading on the detail page. Read as `movie-detail-title` on the movie detail page.
Read on 2026-11-17T06:28:20.359Z.

**Values (default).** size 167.64 x 27.19; background transparent; text Max Sans 17/27.2 700, #ffffff `dark.color.action.primary.fill.high`.

![Title heading default](components/crops/movie-detail-title-default.png)

#### Meta row
The year · rating · runtime/seasons line under the title. Read as `movie-detail-meta` on the movie detail page.

Not on the page when it was captured.

#### Detail "Start Subscription" CTA
The subscribe call-to-action on a title page — an auth link, hovered and focused only. Read as `movie-detail-cta` on the movie detail page.
States read on 2026-11-17T06:28:20.377Z (pressed); 2026-11-17T06:28:21.665Z (default); 2026-11-17T06:28:43.268Z (hover); 2026-11-17T06:28:45.143Z (focus-visible). `pressed` failed at capture (cdpSession.send: Protocol error (DOM.getNodeForLocation): No node found at given location).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 140.41 x 44; padding 10px 18px; radius 8px; background transparent; text Max Sans 15.38/20.76 700, #000000 `dark.color.surface.low`; transition background-color 0.2s cubic-bezier(0, 0, 0.34, 1), color 0.2s cubic-bezier(0, 0, 0.34, 1), opacity 0.2s cubic-bezier(0, 0, 0.34, 1); layers ::before rgb(221, 221, 221) 0px none 1; a::before.sc-bfd2ca80-0.dDxZmm 140.406pxx44px rgb(221, 221, 221) 8px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: a::before 140.406pxx44px background #dddddd `dark.color.action.neutral.border.mid` radius 8px.

![Detail "Start Subscription" CTA default](components/crops/movie-detail-cta-default.png) ![Detail "Start Subscription" CTA hover](components/crops/movie-detail-cta-hover.png)

### Legal prose

The privacy policy: headings, paragraphs and inline links.

#### Legal page title
The "Privacy Policy" heading. Read as `legal-h1` on the privacy policy page.

Not on the page when it was captured.

#### Legal paragraph
A body paragraph of the policy. Read as `legal-p` on the privacy policy page.
Read on 2026-11-17T06:30:17.911Z.

**Values (default).** size 1348 x 29.91; padding 0px 0px 0px 30px; background transparent; text Muli 17.6/29.92 400, #000000 `dark.color.surface.low`.

![Legal paragraph default](components/crops/legal-p-default.png)

#### Legal inline link
A link inside the policy prose. Read as `legal-link` on the privacy policy page.
States read on 2026-11-17T06:30:19.160Z (default); 2026-11-17T06:30:21.205Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 111.92 x 22; background transparent; text Muli 17.6/29.92 400, #317ab9; layers ::after rgba(0, 0, 0, 0) 0px none 1 |

![Legal inline link default](components/crops/legal-link-default.png) ![Legal inline link hover](components/crops/legal-link-hover.png)

### Cookie consent

The consent modal that opens over a fresh visit — measured as loaded; Accept/Manage were styled, never pressed.

#### "Accept All Cookies" button
The primary consent button — styles only, never pressed. Read as `consent-accept` on the home page.
States read on 2026-11-17T06:30:41.880Z (default); 2026-11-17T06:30:44.896Z (hover); 2026-11-17T06:30:51.940Z (focus-visible); 2026-11-17T06:30:54.853Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 152 x 52; padding 10px 30px; radius 8px; background transparent; text Max Sans 20/27 700, #000000 `dark.color.surface.low`; transition background-color 0.2s cubic-bezier(0, 0, 0.34, 1), color 0.2s cubic-bezier(0, 0, 0.34, 1), opacity 0.2s cubic-bezier(0, 0, 0.34, 1); layers ::before rgb(221, 221, 221) 0px none 1; button::before.sc-bfd2ca80-1.fqnUYL 152pxx52px rgb(221, 221, 221) 8px |
| hover | layers ::before rgb(255, 255, 255) 0px none 1; button::before.sc-bfd2ca80-1.fqnUYL 152pxx52px rgb(255, 255, 255) 8px |
| focus-visible | layers ::before rgb(255, 255, 255) 0px none 1; ::after rgba(0, 0, 0, 0) 5px none 1; button::before.sc-bfd2ca80-1.fqnUYL 152pxx52px rgb(255, 255, 255) 8px; button::after.sc-bfd2ca80-1.fqnUYL 162pxx62px T:5px solid / R:5px solid / B:5px solid / L:5px solid 3px solid rgb(0, 0, 0) offset -6px 13px |

Child layers that carry the look: button::before 152pxx52px background #dddddd `dark.color.action.neutral.border.mid` radius 8px.

!["Accept All Cookies" button default](components/crops/consent-accept-default.png) !["Accept All Cookies" button hover](components/crops/consent-accept-hover.png) !["Accept All Cookies" button focus-visible](components/crops/consent-accept-focus-visible.png) !["Accept All Cookies" button pressed](components/crops/consent-accept-pressed.png)

#### "Manage" / "Reject" control
A secondary consent control — styles only, never pressed. Read as `consent-manage` on the home page.
States read on 2026-11-17T06:30:58.377Z (default); 2026-11-17T06:31:00.761Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 212 x 52; padding 10px 30px; radius 8px; background transparent; text Max Sans 20/27 700, #000000 `dark.color.surface.low`; transition background-color 0.2s cubic-bezier(0, 0, 0.34, 1), color 0.2s cubic-bezier(0, 0, 0.34, 1), opacity 0.2s cubic-bezier(0, 0, 0.34, 1); layers ::before rgb(221, 221, 221) 0px none 1; button::before.sc-bfd2ca80-1.fqnUYL 212pxx52px rgb(221, 221, 221) 8px |
| hover | layers ::before rgb(255, 255, 255) 0px none 1; button::before.sc-bfd2ca80-1.fqnUYL 212pxx52px rgb(255, 255, 255) 8px |

Child layers that carry the look: button::before 212pxx52px background #dddddd `dark.color.action.neutral.border.mid` radius 8px.

!["Manage" / "Reject" control default](components/crops/consent-manage-default.png) !["Manage" / "Reject" control hover](components/crops/consent-manage-hover.png)

#### Consent modal
The cookie-preferences modal that opens over a fresh visit — measured as loaded, never accepted or rejected (closePromo hides it for the other groups). Read as `consent-dialog` on the home page.
Read on 2026-11-17T06:30:39.467Z.

**Values (default).** size 1425 x 900; background transparent; text Max Sans 28/37.8 600, #ffffff `dark.color.action.primary.fill.high`; layers div.modal-content.border-0 692.0x358.0 rgb(25, 25, 25) 4.8px; div.sc-97e6fddb-4.fCEnZK 692.0x148.2 B:1px solid; a 77.4x16.0 T:2px solid / R:2px solid / B:2px solid / L:2px solid; a::before autox1.5px; a 115.6x16.0 T:2px solid / R:2px solid / B:2px solid / L:2px solid; a::before autox1.5px.

Child layers that carry the look: div 692x358 background #191919 `dark.color.surface.high` radius 4.8px; div 692x148.2 border 1px solid; a 77.4x16 border 2px solid.

![Consent modal default](components/crops/consent-dialog-default.png)

### Site chrome (mobile)

The 390px surface: the navbar, the menu button and the navigation it opens.

#### Mobile navbar
The navbar at 390px: wordmark, menu button, Sign In. Read as `m-header` on the home page.
Read on 2026-11-17T04:32:29.076Z.

**Values (default).** size 390 x 56; padding 8px 16px; background rgba(0, 0, 0, 0.7) `dark.color.component.button.utility.overlay.fill.base`; text Max Sans 14.72/19.87 700, #ffffff `dark.color.action.primary.fill.high`; transition background-color 0.5s ease-in-out.

![Mobile navbar default](components/crops/m-header-default.png)

#### Mobile menu button
The button that opens the nav at 390px. Read as `m-menu-button` on the home page.

Not on the page when it was captured.

#### Mobile nav (open)
The navigation opened by the menu button's own press. Read as `m-nav-open` on the home page.

Not on the page when it was captured.

#### Slide CTA at 390px
The "Start Subscription" pill under the hero at phone width. Read as `m-hero-cta` on the home page.
Read on 2026-11-17T04:32:58.150Z.

**Values (default).** size 136 x 40; padding 8px 20px; radius 8px; background transparent; text Max Sans 14.72/19.87 700, #000000 `dark.color.surface.low`; transition background-color 0.2s cubic-bezier(0, 0, 0.34, 1), color 0.2s cubic-bezier(0, 0, 0.34, 1), opacity 0.2s cubic-bezier(0, 0, 0.34, 1); layers ::before rgb(221, 221, 221) 0px none 1; a::before.sc-bfd2ca80-0.dDxZmm 136pxx40px rgb(221, 221, 221) 8px.

Child layers that carry the look: a::before 136pxx40px background #dddddd `dark.color.action.neutral.border.mid` radius 8px.

![Slide CTA at 390px default](components/crops/m-hero-cta-default.png)

## Icons

15 distinct inline-SVG icons were collected from the live pages into [icons/](icons) by `tools/capture/icons.mjs`, indexed in [icons/INDEX.tsv](icons/INDEX.tsv): a file is named from `tools/capture/icon-names.tsv` where its geometry hash is listed, else the label or class of the control it sits in, else `icon-<hash>`; colour is kept as `currentColor` wherever it matched the text colour, so each icon recolours from CSS `color` the way it does on the site. The icons are the product's artwork — borrow the set's grammar (sizes, stroke-vs-fill, naming roles), never the artwork itself.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [english](icons/english-1ce3b9dd.svg) | 28x28 | 0 0 48 48 | fill | home; movies; shows; channel; show; collection; sitemap; corp-info; cookie modal; faq open; language list | English / Season 1 |
| [english](icons/english-45f96d96.svg) | 24x24 | 0 0 48 48 | fill | home; movies; shows; channel; show; collection; sitemap; corp-info; cookie modal; faq open; language list | English |
| [icon-5f45d4f3](icons/icon-5f45d4f3.svg) | 16x16 | 0 0 48 48 | fill | home; show; movie; cookie modal; faq open; language list | Stream on 2 devices at once / Full HD video resolution / Wat |
| [icon-463cd2fe](icons/icon-463cd2fe.svg) | 24x24 | 0 0 48 48 | fill | home; cookie modal; faq open; language list | What is the HBO Max & Viu Bundle? / What does the HBO Max &  |
| [previous-carousel-slide](icons/previous-carousel-slide.svg) | 14x26 | 0 0 14 26 | stroke | home; cookie modal; faq open; language list | Previous Carousel Slide / Next Carousel Slide |
| [icon-afd3d768](icons/icon-afd3d768.svg) | 28x28 | 0 0 48 48 | fill | movies; shows; channel; collection |  |
| [icon-b0dca436](icons/icon-b0dca436.svg) | 28x28 | 0 0 48 48 | fill | movies; shows; channel; collection |  |
| [icon-40a6cc80](icons/icon-40a6cc80.svg) | 61x25 | 0 0 240 98.57 | fill | channel |  |
| [icon-4b9f7d59](icons/icon-4b9f7d59.svg) | 59x35 | 0 0 184 109.14 | fill | channel |  |
| [icon-4ca9a6de](icons/icon-4ca9a6de.svg) | 63x32 | 0 0 200 101.27 | fill | channel |  |
| [icon-4f3cdfa8](icons/icon-4f3cdfa8.svg) | 42x42 | 0 0 160 159.94 | fill | channel |  |
| [watch-trailer](icons/watch-trailer.svg) | 20x20 | 0 0 48 48 | fill | show | Watch Trailer |
| [icon-7509c25a](icons/icon-7509c25a.svg) | 63x30 | 0 0 184.5 88.5 | fill | channel |  |
| [icon-d3459f78](icons/icon-d3459f78.svg) | 46x46 | 0 0 160 160 | fill | channel |  |
| [icon-d96e4be1](icons/icon-d96e4be1.svg) | 42x25 | 0 0 150 88.24 | fill | channel |  |

## Gaps

### The blocked product surfaces

The streaming app itself was never reached: **play.hbomax.com** (the player) is signed-in, and every entry point to it passes through **auth.hbomax.com** — the navbar's Sign In, each hero slide's 'Start Subscription' CTA and every plan card's Choose button point at `auth.hbomax.com/login` or `auth.hbomax.com/product`. None was followed. **help.hbomax.com** is a separate help-centre site, linked from the footer but never opened. Headless Chromium is refused by Akamai at the edge with a 403 'Access Denied' page — the standard headless pass is documented as that boundary and every capture here ran headed under Xvfb; no other client shape was tried.

### Pages

- **Sign-in, account and checkout (auth.hbomax.com)** — the signed-in surface; never opened.
- **The player (play.hbomax.com)** — requires an account; never opened.
- **The help centre (help.hbomax.com)** — a separate site linked in the footer; not captured.
- **Other locales** — the capture host resolves to Singapore, so only `/sg/en` loaded; `max.com` and other region/locale pairs were not probed.
- **Student, savings and bundle pages** (`/student`, `/savings`, `/bundle/*`) — marketing landers on the same template family; not each measured.

### States

- **Pressed** was forced with DevTools on the controls that carry it, so a state a script adds on mousedown (if any) is missing.
- **The consent modal** was captured as it mounted and then hidden without accepting or rejecting — its Accept/Manage styles are measured, its consent write was never exercised.
- **The language selector** was opened for measurement; no locale was switched.
- **The carousel** autoplays; the `-next` shots are one Next-arrow press past whatever slide the timing landed on.
- **mobile-movies** lost its default shot to a screenshot timeout on the first pass; a re-run is queued — see the capture sidecars.

### Themes

www.hbomax.com ships one theme: `<html data-theme="max">` is the only theme attribute the bundle sets, and the token sheet loads the same `--color_*` declarations on every page — a dark surface. There is no theme control anywhere in the chrome, so there is no light set, no dark-state pass and nothing was fabricated; the `dark` name in file and token names is the painted surface's own.

### Fonts

- **Max Sans** (woff2, weights 300/400/600, `font-display: swap`) is the product face — the token sheet's own `@font-face` in /dotcom/generated/css/hbomax/styles.*.css — proprietary to Warner Bros. Discovery, declared and measured, not shipped. The rendered stack is `Max Sans,Inter,sans-serif,-apple-system,…`; the style guide falls back to the system sans.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- The rendered brand strings on the captured pages (the wordmark and copy) are the product's published content.

### Content left out

- Title names, prices, plan copy and FAQ text are the product's content; only frames and components were measured.
