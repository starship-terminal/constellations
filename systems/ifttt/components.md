# IFTTT components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Read from ifttt.com and ifttt.ai on 2026-11-18, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, paid for, typed, searched, shared or submitted; the only presses were local UI toggles the product's own chrome provides — the detail pages' Share button (its own modal, closed with its X), the plans Monthly/Yearly billing switch, the featured category tabs, 'show more' expanders and the mobile hamburger. 'Log in', 'Get started', 'Connect', the plan CTAs, the store badges and the share modal's Copy were measured, never followed or pressed.

**Where this was read.** ifttt.com 301s to ifttt.ai for the marketing home; ifttt.com itself hosts /explore(+services,+stories,+applets), /plans (the real pricing route — /pricing 404s), service pages (/twitter, /todoist), applet pages, /connect/* pairings, /solutions/*, /mcp, /about, /careers, /partners and /terms. Sign-in, /join and every account surface were never entered; the Applet 'Connect' install was never pressed; help.ifttt.com answers 403 to automation and platform.ifttt.com redirects to ifttt.ai — all documented as boundaries under Gaps, not captures.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (55 components, 98 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the token in [tokens.json](tokens.json) with the same value, when there is one (the `light.*` roles first — the only painted theme; `light.component.dark.*` holds the dark-painted sections). Text is written family size/line-height weight, then its colour, for example `Museo Sans Rounded 16/24 400, #222222`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (91 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: IFTTT paints one theme on every signed-out surface — there is no theme control anywhere — so `light` is the painted (only) surface; the dark grounds on explore and the detail heroes are painted sections, captured in place and measured as component tokens, not a theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are the whole page at CSS scale, bounded at eight chunks with the boundary recorded in the shot's `.capture.json` sidecar (the explore galleries are the long pages); mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x). `notfound-*` is a made-up route, which 404s — captured as the product's not-found page.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `ifttt.ai/` | [default](screenshots/home-light-default.png), [featured-tab](screenshots/home-light-featured-tab.png), [full](screenshots/home-light-full.png), [prompt-focused](screenshots/home-light-prompt-focused.png) |
| Explore gallery | `/explore` | [default](screenshots/explore-light-default.png), [full](screenshots/explore-light-full.png), [prompt-focused](screenshots/explore-light-prompt-focused.png) |
| Explore, services | `/explore/services` | [default](screenshots/explore-services-light-default.png), [full](screenshots/explore-services-light-full.png) |
| Explore, stories | `/explore/stories` | [default](screenshots/explore-stories-light-default.png), [full](screenshots/explore-stories-light-full.png) |
| Explore, applets | `/explore/applets` | [default](screenshots/explore-applets-light-default.png), [full](screenshots/explore-applets-light-full.png) |
| Plans / pricing | `/plans` | [default](screenshots/plans-light-default.png), [full](screenshots/plans-light-full.png), [monthly](screenshots/plans-light-monthly.png) |
| Service page (X) | `/twitter` | [default](screenshots/service-twitter-light-default.png), [full](screenshots/service-twitter-light-full.png), [share-modal](screenshots/service-twitter-light-share-modal.png), [show-more](screenshots/service-twitter-light-show-more.png) |
| Service page (Todoist) | `/todoist` | [default](screenshots/service-todoist-light-default.png), [full](screenshots/service-todoist-light-full.png), [share-modal](screenshots/service-todoist-light-share-modal.png) |
| Applet page | `/applets/A38TqjpD-...` | [default](screenshots/applet-light-default.png), [full](screenshots/applet-light-full.png), [share-modal](screenshots/applet-light-share-modal.png) |
| Connect page | `/connect/discord/instagram` | [default](screenshots/connect-light-default.png), [full](screenshots/connect-light-full.png), [share-modal](screenshots/connect-light-share-modal.png) |
| Solutions: productivity | `/solutions/productivity` | [default](screenshots/solutions-productivity-light-default.png), [full](screenshots/solutions-productivity-light-full.png) |
| Solutions: smart home | `/solutions/smart-home` | [default](screenshots/solutions-smart-home-light-default.png), [full](screenshots/solutions-smart-home-light-full.png) |
| MCP | `/mcp` | [default](screenshots/mcp-light-default.png), [full](screenshots/mcp-light-full.png) |
| About | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Careers | `/careers` | [default](screenshots/careers-light-default.png), [full](screenshots/careers-light-full.png) |
| Partners | `/partners` | [default](screenshots/partners-light-default.png), [full](screenshots/partners-light-full.png) |
| Terms | `/terms` | [default](screenshots/terms-light-default.png), [full](screenshots/terms-light-full.png) |
| 404 page (made-up route) | `/this-page-does-not-exist-capture` | [default](screenshots/notfound-light-default.png), [full](screenshots/notfound-light-full.png) |
| Home, phone | `ifttt.ai/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu-open](screenshots/mobile-home-light-menu-open.png) |
| Explore, phone | `/explore` | [default](screenshots/mobile-explore-light-default.png), [full](screenshots/mobile-explore-light-full.png) |
| Plans, phone | `/plans` | [default](screenshots/mobile-plans-light-default.png), [full](screenshots/mobile-plans-light-full.png) |
| Service page, phone | `/twitter` | [default](screenshots/mobile-service-light-default.png), [full](screenshots/mobile-service-light-full.png) |
| Applet page, phone | `/applets/A38TqjpD-...` | [default](screenshots/mobile-applet-light-default.png), [full](screenshots/mobile-applet-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Share modal | service, applet and connect pages | the 'Share' button's own press — the site's own share sheet opened, captured, closed with its X; 'Copy' was never pressed | [service-twitter-light-share-modal](screenshots/service-twitter-light-share-modal.png) |
| Billing switch | /plans | the Monthly/Yearly switch's own press (role=switch) — the repainted prices captured, then Yearly restored | [plans-light-monthly](screenshots/plans-light-monthly.png) |
| Featured tabs | home | a featured category tab's own activation — repainted card row captured, then Popular restored | [home-light-featured-tab](screenshots/home-light-featured-tab.png) |
| Prompt focus | home, explore | the 'Describe what you'd like to build' field clicked into — never typed in or submitted | [home-light-prompt-focused](screenshots/home-light-prompt-focused.png) |
| 'show more' expander | /twitter | the service blurb's own 'show more' toggle | [service-twitter-light-show-more](screenshots/service-twitter-light-show-more.png) |
| Mobile menu | home at 390px | the hamburger's own press — the full-screen menu captured, closed with its X | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png) |
| 'Connect' toggle | applet page | the Applet install control, measured at rest — never pressed (it leads to sign-in) | see the applet shots |
| Sign-in, /join, checkout | header, plan cards | never entered — the account and paid product | boundary; see Gaps |
| help.ifttt.com, platform.ifttt.com | docs links | help answers 403 to automation; platform redirects to ifttt.ai | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 4 components were given a real keyboard focus. 3 change their fill: `nav-signup`, `hero-submit`, `secondary-cta`. The other 1 show no measured change: `nav-login`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.12s | `ease-in-out` | background-color | billing-toggle |
| 0.2s | `ease` | background-color | featured-tab, featured-tab-active |
| 0.4s | `ease` | opacity | connect-toggle |
| 0.5s | `ease` | color | site-header |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Applet card](#applet-card) | 432 x 296.19 | - | 24px | #1db954 `light.component.card.appletBg` | rgba(0, 0, 0, 0.24) 0px 1.5px 6px 0px | 0 |
| [Service card](#service-card) | 432 x 296.19 | - | 24px | #14223d `light.component.card.serviceBg` | rgba(0, 0, 0, 0.24) 0px 1.5px 6px 0px | 32px 24px |
| [Story card](#story-card) | 432 x 296.19 | - | 24px | transparent | none | 0 |
| [Plan card (Free)](#plan-card-free) | 310 x 434.14 | 2px solid rgba(17, 17, 17, 0.1) `core.palette.pba1717` | 16px | #ffffff `light.color.bg.page` | none | 26px 22px 22px 22px |
| [Plan card, recommended (Pro)](#plan-card-recommended-pro) | 310 x 456.14 | T: 24px solid #111111 `light.color.action.fill`; R: 2px solid #111111 `light.color.action.fill`; B: 2px solid #111111 `light.color.action.fill`; L: 2px solid #111111 `light.color.action.fill` | 16px | #ffffff `light.color.bg.page` | none | 26px 22px 22px 22px |
| ["Try these examples" card](#try-these-examples-card) | 660 x 111.36 | - | - | transparent | none | 0 |
| [Header search field](#header-search-field) | 400 x 48 | 2px solid rgba(255, 255, 255, 0.3) `light.component.input.searchBorder` | 32px | #111111 `light.color.action.fill` | none | 12px 44px |
| ["Describe what you'd like to build" field](#describe-what-youd-like-to-build-field) | 628 x 78 | - | - | transparent | none | 8px |
| [Monthly / Yearly switch](#monthly--yearly-switch) | 48 x 32 | - | 16px | #01b6ff `light.color.text.link` | none | 0 |
| [Featured category tab](#featured-category-tab) | 142 x 48 | 1px solid rgba(17, 17, 17, 0.1) `core.palette.pba1717` | 8px | rgba(17, 17, 17, 0.05) `light.component.input.shareFieldBg` | none | 11px 19px |
| ["Connect" toggle](#connect-toggle) | 480.05 x 95.94 | - | 47.97px | transparent | none | 0 |

## Components

### Site chrome

The frame every page carries: header.unified-header (the IFTTT.ai wordmark, the search field, Explore / Plans links, the outlined 'Log in' and filled 'Get started' pills — .dark.on-color over the dark heroes) and the footer with its link columns, app-store badges and social icons.

#### Site header
header.unified-header: the IFTTT.ai wordmark, the search field, Explore / Plans links, "Log in" (outlined) and "Get started" (filled) — .dark.on-color over the dark heroes. Read as `site-header` on the explore page.
Read on 2026-11-17T20:24:44.675Z.

**Values (default).** size 1440 x 99; background #111111 `light.color.action.fill`; text Museo Sans Rounded 20/22 900, #ffffff `light.color.bg.page`; transition color 0.5s ease; icon 118.8 x 24.11, #111111 `light.color.action.fill`.

![Site header default](components/crops/site-header-default.png)

#### IFTTT.ai wordmark
The logo link home: the IFTTT.ai mark as inline SVG. Read as `nav-logo` on the explore page.
Read on 2026-11-17T20:24:45.973Z.

**Values (default).** size 118.8 x 24.11; background transparent; text Museo Sans Rounded 18/18 700, #111111 `light.color.action.fill`; icon 118.8 x 24.11, #111111 `light.color.action.fill`.

![IFTTT.ai wordmark default](components/crops/nav-logo-default.png)

#### Header search field
input.ifttt-search-input "Search for Applets, services, etc." — measured and focused, never queried. Read as `nav-search` on the explore page.
States read on 2026-11-17T20:24:47.920Z (default); 2026-11-17T20:25:04.616Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 48; padding 12px 44px; border 2px solid rgba(255, 255, 255, 0.3) `light.component.input.searchBorder`; radius 32px; background #111111 `light.color.action.fill`; text Museo Sans Rounded 18/23.4 700, #ffffff `light.color.bg.page`; placeholder #eeeeee `core.palette.grey2` |
| focused | border 2px solid #ffffff `light.color.bg.page`; placeholder #999999 `core.palette.grey22` |

![Header search field default](components/crops/nav-search-default.png)

#### Nav link
A primary nav link ("Explore") — a.nav-link.link-menu. Read as `nav-link` on the explore page.
States read on 2026-11-17T20:25:22.904Z (default); 2026-11-17T20:25:44.763Z (hover); 2026-11-17T20:26:20.069Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 71 x 22; background transparent; text Museo Sans Rounded 20/22 900, #ffffff `light.color.bg.page` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Nav link default](components/crops/nav-link-default.png)

#### "Log in" button
a.sign-in.button-tertiary.button-outlined — the outlined pill; measured, never followed (it leads to sign-in). Read as `nav-login` on the explore page.
States read on 2026-11-17T20:26:43.867Z (default); 2026-11-17T20:26:50.269Z (hover); 2026-11-17T20:27:07.583Z (focus-visible); 2026-11-17T20:27:09.789Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 115 x 54; padding 0px 28px; radius 64px; background transparent; shadow #ffffff 0px 0px 0px 2px inset; text Museo Sans Rounded 20/22 900, #ffffff `light.color.bg.page`; layers a.sign-in.button-tertiary 115.0x54.0 #ffffff 0px 0px 0px 2px inset 64px |

!["Log in" button default](components/crops/nav-login-default.png) !["Log in" button hover](components/crops/nav-login-hover.png) !["Log in" button focus-visible](components/crops/nav-login-focus-visible.png) !["Log in" button pressed](components/crops/nav-login-pressed.png)

#### "Get started" button
a.button-tertiary.sign-up — the filled near-black pill in the header; measured, never followed (it leads to /join). Read as `nav-signup` on the explore page.
States read on 2026-11-17T20:27:11.059Z (default); 2026-11-17T20:27:13.393Z (hover); 2026-11-17T20:27:28.823Z (focus-visible); 2026-11-17T20:27:39.194Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 162 x 54; padding 0px 28px; radius 64px; background #ffffff `light.color.bg.page`; text Museo Sans Rounded 20/22 900, #111111 `light.color.action.fill` |
| hover | background #eeeeee `core.palette.grey2`; opacity 0.8 |
| focus-visible, pressed | background #eeeeee `core.palette.grey2` |

!["Get started" button default](components/crops/nav-signup-default.png) !["Get started" button hover](components/crops/nav-signup-hover.png) !["Get started" button focus-visible](components/crops/nav-signup-focus-visible.png) !["Get started" button pressed](components/crops/nav-signup-pressed.png)

#### Site footer
The page footer: link columns, the app-store badges and the social icons. Read as `site-footer` on the explore page.
Read on 2026-11-17T20:27:58.825Z.

**Values (default).** size 1440 x 851.91; padding 48px 48px 64px 48px; border T: 1px solid rgba(255, 255, 255, 0.3) `light.component.input.searchBorder`; background #111111 `light.color.action.fill`; text Museo Sans Rounded 34/37.4 900, #111111 `light.color.action.fill`; icon 88.97 x 24, #111111 `light.color.action.fill`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Footer link
A link inside the footer columns. Read as `footer-link` on the explore page.
States read on 2026-11-17T20:28:25.932Z (default); 2026-11-17T20:28:29.432Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1344 x 143; padding 32px; radius 32px; background #01b6ff `light.color.text.link`; text Museo Sans Rounded 34/37.4 900, #111111 `light.color.action.fill`; icon 88.97 x 24, #111111 `light.color.action.fill` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png)

### Home

The ifttt.ai home: the 'Describe what you'd like to build' prompt the hero is built around, 'Start building', the featured-Applets category tabs and the applet cards. The prompt field was clicked into for its focus look; nothing was typed or submitted.

#### Hero headline
The home hero h1 "The easiest way to automate anything" — Museo Sans Rounded 900. Read as `hero-headline` on the home page.
Read on 2026-11-17T21:18:49.459Z.

**Values (default).** size 1084 x 158.66; background transparent; text Museo Sans Rounded 79.32/79.32 900, #111111 `light.color.action.fill`.

![Hero headline default](components/crops/hero-headline-default.png)

#### "Describe what you'd like to build" field
textarea.prompt-hero-input — the AI prompt box the hero is built around. focused is the field clicked into; nothing is typed or submitted. Read as `hero-prompt` on the home page.
States read on 2026-11-17T21:18:51.954Z (default); 2026-11-17T21:18:55.452Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 628 x 78; padding 8px; background transparent; text Museo Sans Rounded 16/20.8 700, #111111 `light.color.action.fill`; placeholder rgba(17, 17, 17, 0.4) `light.component.switch.trackOff` |

!["Describe what you'd like to build" field default](components/crops/hero-prompt-default.png) !["Describe what you'd like to build" field focused](components/crops/hero-prompt-focused.png)

#### "Start building" button
button.button-primary.prompt-hero-submit — the big black pill under the prompt. Measured, never pressed (it submits the prompt). Read as `hero-submit` on the home page.
States read on 2026-11-17T21:18:58.464Z (default); 2026-11-17T21:19:02.858Z (hover); 2026-11-17T21:19:06.884Z (focus-visible); 2026-11-17T21:19:09.611Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 348 x 101; padding 0px 64px; radius 64px; background #111111 `light.color.action.fill`; text Museo Sans Rounded 34/37.4 900, #ffffff `light.color.bg.page` |
| hover | opacity 0.8 |
| focus-visible | background rgba(17, 17, 17, 0.6) `core.palette.grey` |

!["Start building" button default](components/crops/hero-submit-default.png) !["Start building" button hover](components/crops/hero-submit-hover.png) !["Start building" button focus-visible](components/crops/hero-submit-focus-visible.png) !["Start building" button pressed](components/crops/hero-submit-pressed.png)

#### Featured category tab
A featured-Applets category tab (button.featured-tab). "selected" is its own activation — a local UI toggle, restored to Popular after. Read as `featured-tab` on the home page.
States read on 2026-11-17T21:19:11.102Z (default); 2026-11-17T21:19:13.064Z (hover); 2026-11-17T21:19:15.328Z (selected).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 142 x 48; padding 11px 19px; border 1px solid rgba(17, 17, 17, 0.1) `core.palette.pba1717`; radius 8px; background rgba(17, 17, 17, 0.05) `light.component.input.shareFieldBg`; text Museo Sans Rounded 18/24 700, #111111 `light.color.action.fill`; transition background-color 0.2s ease |
| hover | background rgba(17, 17, 17, 0.1) `core.palette.pba1717` |
| selected | border 1px solid #111111 `light.color.action.fill`; background #111111 `light.color.action.fill`; text Museo Sans Rounded 18/24 700, #ffffff `light.color.bg.page` |

![Featured category tab default](components/crops/featured-tab-default.png) ![Featured category tab hover](components/crops/featured-tab-hover.png) ![Featured category tab selected](components/crops/featured-tab-selected.png)

#### Featured tab, active
The resting "Popular" tab — the selected pill state. Read as `featured-tab-active` on the home page.
Read on 2026-11-17T21:19:16.438Z.

**Selector missed the element.** The saved element is the Smart home tab (text "Smart home", classes "featured-tab active"), left selected by the featured-tab reading. It is not the resting Popular tab. The style is kept on featured-tab's selected state, which is that same reading. Not republished as the Popular default. The saved style is not published as this component's measurement.

#### Service icon chip
One floating service icon in the hero automation canvas — the rounded-square brand tiles that drift across the hero. Read as `service-chip` on the home page.
Read on 2026-11-17T21:19:17.414Z.

**Values (default).** size 48 x 48; radius 12px; background #111111 `light.color.action.fill`; image url(…); text Museo Sans Rounded 18/21.6 500, #111111 `light.color.action.fill`.

![Service icon chip default](components/crops/service-chip-default.png)

#### Secondary CTA
"Join today" / "Explore all Applets" — a.button-secondary, the large outlined action. Measured, never followed (it leads to /join or /explore). Read as `secondary-cta` on the home page.
States read on 2026-11-17T21:19:19.408Z (default); 2026-11-17T21:19:22.718Z (hover); 2026-11-17T21:19:26.678Z (focus-visible); 2026-11-17T21:19:30.248Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 222 x 79; padding 0px 40px; radius 64px; background #111111 `light.color.action.fill`; text Museo Sans Rounded 28/30.8 900, #ffffff `light.color.bg.page` |
| hover | opacity 0.8 |
| focus-visible | background rgba(17, 17, 17, 0.6) `core.palette.grey` |

![Secondary CTA default](components/crops/secondary-cta-default.png) ![Secondary CTA hover](components/crops/secondary-cta-hover.png) ![Secondary CTA focus-visible](components/crops/secondary-cta-focus-visible.png) ![Secondary CTA pressed](components/crops/secondary-cta-pressed.png)

#### Section heading
A home section heading (an h2 in the modules below the fold). Read as `section-heading` on the home page.
Read on 2026-11-17T21:19:32.036Z.

**Values (default).** size 548 x 100; background transparent; text Museo Sans Rounded 50/50 900, #111111 `light.color.action.fill`.

![Section heading default](components/crops/section-heading-default.png)

### Explore

The /explore gallery: the dark 'Automate X with Y' hero with its prompt card and service-chip cycler, the All / Applets / Services / Stories tabs, the service and story cards and the 'Search automations' field — clicked into, never queried.

#### Applet card
A gallery applet card (a.applet-card-body inside li.web-applet-card): the tile with service icons, title, author and use count. Read as `applet-card` on the explore page.
States read on 2026-11-17T21:07:38.813Z (default); 2026-11-17T21:07:41.965Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 432 x 296.19; radius 24px; background #1db954 `light.component.card.appletBg`; shadow rgba(0, 0, 0, 0.24) 0px 1.5px 6px 0px; text Museo Sans Rounded 26.78/29.45 900, #ffffff `light.color.bg.page` |

![Applet card default](components/crops/applet-card-default.png) ![Applet card hover](components/crops/applet-card-hover.png)

#### Explore hero (dark)
The dark "Automate X with Y" hero band on /explore: near-black ground, the prompt card and the cycling service names. Read as `explore-hero` on the explore page.
Read on 2026-11-17T21:05:17.969Z.

**Values (default).** size 1440 x 579.36; padding 108px 48px; background #111111 `light.color.action.fill`; image url(…); text Museo Sans Rounded 32/41.6 700, #ffffff `light.color.bg.page`; icon 16 x 16, #ffffff `light.color.bg.page`.

![Explore hero (dark) default](components/crops/explore-hero-default.png)

#### Explore prompt field
textarea.prompt-hero-input inside the dark hero card — "tell us what you'd like to automate". focused only; never submitted. Read as `explore-prompt` on the explore page.
States read on 2026-11-17T21:05:21.895Z (default); 2026-11-17T21:05:25.024Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 628 x 58; padding 8px; background transparent; text Museo Sans Rounded 16/20.8 700, #111111 `light.color.action.fill`; placeholder rgba(17, 17, 17, 0.4) `light.component.switch.trackOff` |

![Explore prompt field default](components/crops/explore-prompt-default.png) ![Explore prompt field focused](components/crops/explore-prompt-focused.png)

#### Prompt card
The white card holding the prompt field and its "Start building" submit inside the dark hero. Read as `explore-prompt-card` on the explore page.
Read on 2026-11-17T21:05:43.664Z.

**Selector missed the element.** The saved element is section.explore-prompt-hero (1440 x 579, background #111111), the dark hero, not the white prompt card. No card-sized white ancestor is in the saved paint layers, so the card's size, radius and shadow are unmeasured. Not republished as the prompt card. The saved style is not published as this component's measurement.

#### Service chip in hero
a.explore-hero-service — a service name chip ("Pinterest") in the "Automate X with Y" cycler. Read as `explore-service-chip` on the explore page.
States read on 2026-11-17T21:06:04.880Z (default); 2026-11-17T21:06:30.664Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 181 x 42; background transparent; text Museo Sans Rounded 32/41.6 700, #ee831e `light.component.dark.chipInk`; transform translate(0px, -42px); opacity 0; layers span.explore-hero-service-icon 40.0x40.0 #ec7505 12px |

Child layers that carry the look: span 40x40 background #ec7505 radius 12px.

![Service chip in hero hover](components/crops/explore-service-chip-hover.png)

#### "Try these examples" card
One translucent suggestion card under the prompt ("If there's a new Tweet with keyword, add to sheets."). Read as `example-prompt-card` on the explore page.
Read on 2026-11-17T21:07:05.934Z.

**Values (default).** size 660 x 111.36; background transparent; text Museo Sans Rounded 16/20.8 900, rgba(255, 255, 255, 0.6) `core.palette.pba25522`; layers button 214.7x86.6 rgba(255, 255, 255, 0.1) 10px; button 214.7x86.6 rgba(255, 255, 255, 0.1) 10px; button 214.7x86.6 rgba(255, 255, 255, 0.1) 10px.

Child layers that carry the look: button 214.7x86.6 background rgba(255, 255, 255, 0.1) `core.palette.pba2552` radius 10px; button 214.7x86.6 background rgba(255, 255, 255, 0.1) `core.palette.pba2552` radius 10px; button 214.7x86.6 background rgba(255, 255, 255, 0.1) `core.palette.pba2552` radius 10px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Explore gallery tab
The All / Applets / Services / Stories gallery tabs (a.text-h5). "active" is the current tab. Read as `explore-tab` on the explore page.
States read on 2026-11-17T21:07:18.315Z (default); 2026-11-17T21:07:23.175Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85 x 52.8; padding 16px 12px; background transparent; text Museo Sans Rounded 16/20.8 900, rgba(17, 17, 17, 0.6) `core.palette.grey` |
| hover | text Museo Sans Rounded 16/20.8 900, #111111 `light.color.action.fill` |

![Explore gallery tab default](components/crops/explore-tab-default.png) ![Explore gallery tab hover](components/crops/explore-tab-hover.png)

#### Explore gallery tab, active
The resting "All" tab — the active state (a.text-h5.active). Read as `explore-tab-active` on the explore page.
Read on 2026-11-17T21:07:24.600Z.

**Values (default).** size 44 x 52.8; padding 16px 12px; background transparent; text Museo Sans Rounded 16/20.8 900, #111111 `light.color.action.fill`; layers ::after #111111 0px none 1; a::after.text-h5.active 44pxx2px #111111.

Child layers that carry the look: a::after 44pxx2px background #111111 `light.color.action.fill`.

![Explore gallery tab, active default](components/crops/explore-tab-active-default.png)

#### Service card
a.service-card — a service tile in the gallery grid: brand icon over name on white. Read as `service-card` on the explore page.
States read on 2026-11-17T21:07:45.057Z (default); 2026-11-17T21:07:47.250Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 432 x 296.19; padding 32px 24px; radius 24px; background #14223d `light.component.card.serviceBg`; shadow rgba(0, 0, 0, 0.24) 0px 1.5px 6px 0px; text Museo Sans Rounded 20/22 900, #ffffff `light.color.bg.page` |

![Service card default](components/crops/service-card-default.png) ![Service card hover](components/crops/service-card-hover.png)

#### Story card
a.story-box — a story tile ("Put AI to work for you") in the gallery. Read as `story-card` on the explore page.
Read on 2026-11-17T21:07:49.286Z.

**Values (default).** size 432 x 296.19; radius 24px; background transparent; text Museo Sans Rounded 16/20.8 900, #ffffff `light.color.bg.page`; layers div.overlay 432.0x296.2.

Child layers that carry the look: div 432x296.2 image linear-gradient(rgba(16, 132, 250, 0) 0%, #1084fa 50%).

![Story card default](components/crops/story-card-default.png)

#### "Search automations" field
The gallery's own search input (input.ifttt-search-input "Search automations"). Focused only; never queried. Read as `gallery-search` on the explore page.
States read on 2026-11-17T21:07:52.927Z (default); 2026-11-17T21:08:03.621Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 432 x 55; padding 16px 44px; border 2px solid rgba(17, 17, 17, 0.1) `core.palette.pba1717`; radius 32px; background #ffffff `light.color.bg.page`; text Museo Sans Rounded 18/23.4 700, rgba(17, 17, 17, 0.4) `light.component.switch.trackOff`; placeholder rgba(17, 17, 17, 0.4) `light.component.switch.trackOff` |
| focused | border 2px solid #111111 `light.color.action.fill`; text Museo Sans Rounded 18/23.4 700, #111111 `light.color.action.fill`; placeholder #999999 `core.palette.grey22` |

!["Search automations" field default](components/crops/gallery-search-default.png) !["Search automations" field focused](components/crops/gallery-search-focused.png)

### Plans

The /plans pricing: the Monthly / Yearly billing switch (role=switch, pressed and restored), the plan cards (the Pro card carries the RECOMMENDED dark header), the 'SAVE 30%' badge and the 'Get started' CTAs — measured, never followed to checkout.

#### Monthly / Yearly switch
button.switch-field (role=switch) in the credits-plans-toggle — the billing-period control. "yearly"/"monthly" are its own presses, the repainted prices proof; restored to the default (Yearly). Read as `billing-toggle` on the plans page.
States read on 2026-11-17T20:33:13.278Z (default); 2026-11-17T20:33:16.348Z (hover); 2026-11-17T20:33:18.600Z (toggled).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 48 x 32; radius 16px; background #01b6ff `light.color.text.link`; text Museo Sans Rounded 13.33/normal 400, #000000 `core.palette.p000000`; transition background-color 0.12s ease-in-out |
| toggled | background rgba(17, 17, 17, 0.4) `light.component.switch.trackOff` |

![Monthly / Yearly switch default](components/crops/billing-toggle-default.png) ![Monthly / Yearly switch hover](components/crops/billing-toggle-hover.png) ![Monthly / Yearly switch toggled](components/crops/billing-toggle-toggled.png)

#### Billing toggle with labels
div.credits-plans-toggle — Monthly | switch | Yearly + the "SAVE 30%" badge. Read as `billing-toggle-wrap` on the plans page.
Read on 2026-11-17T20:33:19.803Z.

**Values (default).** size 193 x 56; padding 4px; background transparent; text Museo Sans Rounded 16/20.8 700, #111111 `light.color.action.fill`; layers button.switch-field 48.0x32.0 rgba(17, 17, 17, 0.4) 16px; span.switch-field-knob 28.0x28.0 #ffffff 50%; span.credits-plans-save 65.0x20.6 #0dd14e 6px.

Child layers that carry the look: button 48x32 background rgba(17, 17, 17, 0.4) `light.component.switch.trackOff` radius 16px; span 28x28 background #ffffff `light.color.bg.page` radius 50%; span 65x20.6 background #0dd14e `core.palette.saveGreen` radius 6px.

![Billing toggle with labels default](components/crops/billing-toggle-wrap-default.png)

#### "SAVE 30%" badge
The green discount badge beside the yearly label. Read as `save-badge` on the plans page.
Read on 2026-11-17T20:33:21.572Z.

**Selector missed the element.** The saved element is div.credits-plans-toggle (193 x 56, text "Monthly Yearly SAVE 30%"), the whole billing row. span.credits-plans-save appears only as a paint-layer size (65.0x20.6, bg rgb(13, 209, 78), radius 6px) with no computed style of its own, so the badge's fill, ink and type are unmeasured. Not republished as the badge. The saved style is not published as this component's measurement.

#### Plan card (Free)
A pricing card: name, $ price, credits line, feature list with check icons and a "Get started" outline CTA. Read as `plan-card` on the plans page.
Read on 2026-11-17T20:33:24.648Z.

**Values (default).** size 310 x 434.14; padding 26px 22px 22px 22px; border 2px solid rgba(17, 17, 17, 0.1) `core.palette.pba1717`; radius 16px; background #ffffff `light.color.bg.page`; text Museo Sans Rounded 18/normal 900, #111111 `light.color.action.fill`; icon 16 x 16, rgba(17, 17, 17, 0.7) `light.color.text.muted`.

![Plan card (Free) default](components/crops/plan-card-default.png)

#### Plan card, recommended (Pro)
The highlighted Pro card — dark header, "RECOMMENDED" ribbon, filled "Get started" CTA. Read as `plan-card-recommended` on the plans page.
Read on 2026-11-17T20:33:26.025Z.

**Values (default).** size 310 x 456.14; padding 26px 22px 22px 22px; border T: 24px solid #111111 `light.color.action.fill`; R: 2px solid #111111 `light.color.action.fill`; B: 2px solid #111111 `light.color.action.fill`; L: 2px solid #111111 `light.color.action.fill`; radius 16px; background #ffffff `light.color.bg.page`; text Museo Sans Rounded 12/15.6 700, rgba(255, 255, 255, 0.85) `core.palette.pba2552222222`; icon 10 x 10, rgba(255, 255, 255, 0.85) `core.palette.pba2552222222`.

![Plan card, recommended (Pro) default](components/crops/plan-card-recommended-default.png)

#### Plan price figure
The big "$0.00 / month" figure on a plan card — the display number style. Read as `plan-price` on the plans page.
Read on 2026-11-17T20:33:27.092Z.

**Values (default).** size 135 x 50; background transparent; text Museo Sans Rounded 50/50 900, #111111 `light.color.action.fill`.

![Plan price figure default](components/crops/plan-price-default.png)

#### Plan feature row
A feature line inside a plan card ("All features unlocked") with its check icon. Read as `plan-feature` on the plans page.
Read on 2026-11-17T20:33:28.576Z.

**Values (default).** size 262 x 18.19; background transparent; text Museo Sans Rounded 14/18.2 700, rgba(17, 17, 17, 0.7) `light.color.text.muted`; icon 16 x 16, rgba(17, 17, 17, 0.7) `light.color.text.muted`.

![Plan feature row default](components/crops/plan-feature-default.png)

#### Plan "Get started" CTA
The outlined button on a plan card — measured, never followed (it leads to checkout). Read as `plan-cta` on the plans page.
States read on 2026-11-17T20:33:29.753Z (default); 2026-11-17T20:33:31.603Z (hover); 2026-11-17T20:33:32.887Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 262 x 54; padding 0px 28px; radius 64px; background transparent; shadow #111111 0px 0px 0px 2px inset; text Museo Sans Rounded 20/22 900, #111111 `light.color.action.fill`; layers a.button-tertiary.button-outlined 262.0x54.0 #111111 0px 0px 0px 2px inset 64px |
| hover | background rgba(17, 17, 17, 0.05) `light.component.input.shareFieldBg`; layers none |

![Plan "Get started" CTA default](components/crops/plan-cta-default.png) ![Plan "Get started" CTA hover](components/crops/plan-cta-hover.png) ![Plan "Get started" CTA pressed](components/crops/plan-cta-pressed.png)

#### Plan CTA on the recommended card
The filled "Get started" on the Pro card — measured, never followed. Read as `plan-cta-filled` on the plans page.
States read on 2026-11-17T20:33:33.918Z (default); 2026-11-17T20:33:35.766Z (hover); 2026-11-17T20:33:37.063Z (pressed).

**Selector missed the element.** The saved element is a.button-tertiary.sign-up at y 22.5 (162 x 54), the header signup. The recommended card's filled CTA was not the element measured. Not republished as the plan CTA. The saved style is not published as this component's measurement.

### Detail pages

The chrome service, applet and connect pages share: the fixed 'Back' pill, the 'Share' button whose own press paints the site's share modal (the read-only URL field, the social icons and the Copy pill — measured, never pressed, closed with its own X), and the branded hero band.

#### Back button
The fixed "Back" pill on service/applet/connect pages — measured, never followed. Read as `back-button` on the connect page page.
States read on 2026-11-17T21:41:05.355Z (default); 2026-11-17T21:41:07.264Z (hover); 2026-11-17T21:41:09.658Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 134 x 54; padding 0px 28px; radius 64px; background transparent; shadow #ffffff 0px 0px 0px 2px inset; text Museo Sans Rounded 20/22 900, #ffffff `light.color.bg.page`; icon 24 x 24, #ffffff `light.color.bg.page`; layers a.button-tertiary.button-outlined 134.0x54.0 #ffffff 0px 0px 0px 2px inset 64px |
| hover | background rgba(255, 255, 255, 0.1) `core.palette.pba2552`; layers none |

![Back button default](components/crops/back-button-default.png) ![Back button hover](components/crops/back-button-hover.png) ![Back button pressed](components/crops/back-button-pressed.png)

#### Share button
button.modal-open "Share" — opens the site's own share modal. "opened" is its own press painting .modal; the modal is closed with its X after. Read as `share-button` on the connect page page.
States read on 2026-11-17T21:41:10.815Z (default); 2026-11-17T21:41:20.853Z (hover); 2026-11-17T21:41:37.665Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 148.19 x 54; padding 0px 28px; radius 64px; background transparent; shadow #ffffff 0px 0px 0px 2px inset; text Museo Sans Rounded 20/22 900, #ffffff `light.color.bg.page`; icon 24 x 24, #ffffff `light.color.bg.page`; layers button.modal-open.button-tertiary 148.2x54.0 #ffffff 0px 0px 0px 2px inset 64px |
| hover | background rgba(255, 255, 255, 0.1) `core.palette.pba2552`; layers none |
| opened | size 1440 x 900; padding none; radius none; shadow none; text Museo Sans Rounded 20/22 900, #111111 `light.color.action.fill`; icon 21 x 21, #111111 `light.color.action.fill`; layers div.modal-background 1440.0x900.0 rgba(0, 0, 0, 0.5); div.modal-content 504.0x252.6 #ffffff T:1px solid rgba(0, 0, 0, 0.05) / R:1px solid rgba(0, 0, 0, 0.05) / B:1px solid rgba(0, 0, 0, 0.05) / L:1px solid rgba(0, 0, 0, 0.05) rgba(0, 0, 0, 0.25) 0px 8px 16px 0px 8px; input.share-url-input.hide-on-xs 418.0x55.0 rgba(17, 17, 17, 0.05) T:2px solid transparent / R:2px solid transparent / B:2px solid t |

![Share button default](components/crops/share-button-default.png) ![Share button hover](components/crops/share-button-hover.png) ![Share button opened](components/crops/share-button-opened.png)

#### Share modal "Copy" button
The black Copy pill inside the share modal — measured inside the opened modal, never pressed (a clipboard side effect). Read as `share-modal-copy` on the connect page page.
Read on 2026-11-17T21:41:42.696Z.

**Values (default).** size 121 x 54; padding 0px 28px; radius 64px; background #111111 `light.color.action.fill`; text Museo Sans Rounded 20/22 900, #ffffff `light.color.bg.page`.

![Share modal "Copy" button default](components/crops/share-modal-copy-default.png)

#### Share URL field
input.share-url-input — the read-only short-link field in the share modal. Read as `share-url-field` on the connect page page.
Read on 2026-11-17T21:42:00.472Z.

**Values (default).** size 418 x 55; padding 0px 16px; border 2px solid transparent; radius 16px; background rgba(17, 17, 17, 0.05) `light.component.input.shareFieldBg`; text Museo Sans Rounded 18/23.4 700, #111111 `light.color.action.fill`; placeholder #111111 `light.color.action.fill`.

![Share URL field default](components/crops/share-url-field-default.png)

#### Service / applet hero
The branded hero band on a detail page: service icons, the display headline and lede — dark on service and connect pages, the partner brand colour on applet pages. Read as `service-hero` on the connect page page.
Read on 2026-11-17T21:42:03.189Z.

**Values (default).** size 1344 x 1466.25; background transparent; text Museo Sans Rounded 34/37.4 900, #111111 `light.color.action.fill`; layers a.applet-card-body.spec-prefetch 432.0x330.8 #e4405f rgba(0, 0, 0, 0.24) 0px 1.5px 6px 0px 24px; a.applet-card-body.spec-prefetch 432.0x330.8 #e4405f rgba(0, 0, 0, 0.24) 0px 1.5px 6px 0px 24px; a.applet-card-body.spec-prefetch 432.0x330.8 #e4405f rgba(0, 0, 0, 0.24) 0px 1.5px 6px 0px 24px; a.applet-card-body.spec-prefetch 432.0x330.8 #e4405f rgba(0, 0, 0, 0.24) 0px 1.5px 6px 0px 24px; a.applet-car.

Child layers that carry the look: a 432x330.8 background #e4405f radius 24px shadow rgba(0, 0, 0, 0.24) `core.palette.pba000022` 0px 1.5px 6px 0px; a 432x330.8 background #e4405f radius 24px shadow rgba(0, 0, 0, 0.24) `core.palette.pba000022` 0px 1.5px 6px 0px; a 432x330.8 background #e4405f radius 24px shadow rgba(0, 0, 0, 0.24) `core.palette.pba000022` 0px 1.5px 6px 0px.

![Service / applet hero default](components/crops/service-hero-default.png)

#### Service icon
The service's rounded-square brand tile in a hero or card. Read as `service-icon` on the connect page page.
Read on 2026-11-17T21:42:06.078Z.

**Values (default).** size 110 x 110; background transparent; text Museo Sans Rounded 18/21.6 500, #111111 `light.color.action.fill`.

![Service icon default](components/crops/service-icon-default.png)

#### "Get started today" button
The white pill on the dark heroes — measured, never followed (it leads to sign-up). Read as `get-started-today` on the connect page page.
States read on 2026-11-17T21:42:07.033Z (default); 2026-11-17T21:42:08.956Z (hover); 2026-11-17T21:42:10.365Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 413 x 101; padding 0px 64px; radius 64px; background #ffffff `light.color.bg.page`; text Museo Sans Rounded 34/37.4 900, #111111 `light.color.action.fill` |
| hover | opacity 0.8 |

!["Get started today" button default](components/crops/get-started-today-default.png) !["Get started today" button hover](components/crops/get-started-today-hover.png) !["Get started today" button pressed](components/crops/get-started-today-pressed.png)

### Applet page

What an Applet detail page adds: the big 'Connect' toggle (the install control — measured, never pressed; it leads to sign-in), the meta byline, author link, the trigger/action detail and the service list rows.

#### "Connect" toggle
The big black pill with the brand-coloured knob — the applet's install control, styled like a giant switch. Measured, never pressed (it leads to sign-in). Read as `connect-toggle` on the applet page page.
States read on 2026-11-17T21:10:43.034Z (default); 2026-11-17T21:10:52.469Z (hover); 2026-11-17T21:11:03.345Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 480.05 x 95.94; radius 47.97px; background transparent; text Museo Sans Rounded 33.92/40.70 900, #ffffff `light.color.bg.page`; transition opacity 0.4s ease |

!["Connect" toggle default](components/crops/connect-toggle-default.png) !["Connect" toggle hover](components/crops/connect-toggle-hover.png) !["Connect" toggle pressed](components/crops/connect-toggle-pressed.png)

#### Applet meta line
.applet-meta-line — the "iRobot · 20.8k" byline under the headline. Read as `applet-meta` on the applet page page.
Read on 2026-11-17T21:11:09.197Z.

**Values (default).** size 480.05 x 45; background transparent; text Museo Sans Rounded 16/20.8 900, #ffffff `light.color.bg.page`.

![Applet meta line default](components/crops/applet-meta-default.png)

#### Author link
a.author-link.link-on-color — the applet author on the brand-coloured hero. Read as `author-link` on the applet page page.
States read on 2026-11-17T21:11:19.607Z (default); 2026-11-17T21:11:27.228Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 78.78 x 20.8; background transparent; text Museo Sans Rounded 16/20.8 900, #ffffff `light.color.bg.page` |

![Author link default](components/crops/author-link-default.png) ![Author link hover](components/crops/author-link-hover.png)

#### Trigger row
A trigger line in the "About this Applet" detail ("You exit an area" — a.meta-type "Realtime trigger"). Read as `trigger-row` on the applet page page.
Read on 2026-11-17T21:11:34.541Z.

**Values (default).** size 143 x 25.69; background transparent; text Museo Sans Rounded 14/18.2 700, #111111 `light.color.action.fill`; icon 16 x 16, #111111 `light.color.action.fill`; layers a.meta-type 143.0x24.2 rgba(17, 17, 17, 0.05) T:1px solid rgba(17, 17, 17, 0.1) / R:1px solid rgba(17, 17, 17, 0.1) / B:1px solid rgba(17, 17, 17, 0.1) / L:1px solid rgba(17, 17, 17, 0.1) 6px; div.tool-tip.tool-tip--dark 305.0x152.0 #333333 rgba(0, 0, 0, 0.25) 0px 3px 4px 0px 10px.

Child layers that carry the look: a 143x24.2 background rgba(17, 17, 17, 0.05) `light.component.input.shareFieldBg` border 1px solid rgba(17, 17, 17, 0.1) `core.palette.pba1717` radius 6px; div 305x152 background #333333 `core.palette.p333333` radius 10px shadow rgba(0, 0, 0, 0.25) `core.palette.pba0000222` 0px 3px 4px 0px.

![Trigger row default](components/crops/trigger-row-default.png)

#### Service list row
a.service-item — a service row in the page's service list ("Location", "iRobot"). Read as `service-item` on the applet page page.
States read on 2026-11-17T21:11:44.807Z (default); 2026-11-17T21:11:51.374Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 480.05 x 64; padding 12px 0px; background transparent; text Museo Sans Rounded 20/22 900, #111111 `light.color.action.fill`; icon 15 x 20, #111111 `light.color.action.fill`; layers div.service-icon-wrapper 40.0x40.0 #0099ff T:1px solid rgba(17, 17, 17, 0.1) / R:1px solid rgba(17, 17, 17, 0.1) / B:1px solid rgba(17, 17, 17, 0.1) / L:1px solid rgba(17, 17, 17, 0.1) 8px |

Child layers that carry the look: div 40x40 background #0099ff `core.palette.p0099ff` border 1px solid rgba(17, 17, 17, 0.1) `core.palette.pba1717` radius 8px.

![Service list row default](components/crops/service-item-default.png) ![Service list row hover](components/crops/service-item-hover.png)

### Solutions

The /solutions/* marketing surfaces: hero band and feature cards.

#### Solutions hero
The hero band on a solutions page ("Achieve more in less time"). Read as `solutions-hero` on the solutions page page.
Read on 2026-11-17T20:42:49.343Z.

**Values (default).** size 936 x 588.44; padding 63.999px 0px; background transparent; text Museo Sans Rounded 50/50 900, #111111 `light.color.action.fill`; layers a.button-primary 300.0x101.0 #111111 64px.

Child layers that carry the look: a 300x101 background #111111 `light.color.action.fill` radius 64px.

![Solutions hero default](components/crops/solutions-hero-default.png)

#### Solutions feature card
A feature or use-case card on the solutions page. Read as `solutions-card` on the solutions page page.
Read on 2026-11-17T20:42:52.740Z.

**Values (default).** size 311.39 x 324.53; padding 9px; background transparent; text Museo Sans Rounded 26.94/29.63 900, #ffffff `light.color.bg.page`; layers a.applet-card-body.spec-prefetch 293.4x306.5 #2c6efc rgba(0, 0, 0, 0.24) 0px 1.5px 6px 0px 24px.

Child layers that carry the look: a 293.4x306.5 background #2c6efc radius 24px shadow rgba(0, 0, 0, 0.24) `core.palette.pba000022` 0px 1.5px 6px 0px.

![Solutions feature card default](components/crops/solutions-card-default.png)

### Marketing pages

The prose layer: page h1s, body paragraphs and inline links on /mcp, /about, /careers and /terms.

#### Marketing h1
The page headline on a marketing surface (mcp / about / careers). Read as `marketing-h1` on the MCP page page.
Read on 2026-11-17T20:43:43.873Z.

**Values (default).** size 1116 x 128; background transparent; text Museo Sans Rounded 64/64 900, #111111 `light.color.action.fill`.

![Marketing h1 default](components/crops/marketing-h1-default.png)

#### Body paragraph
A body paragraph of marketing or legal prose. Read as `prose-p` on the MCP page page.
Read on 2026-11-17T20:44:00.808Z.

**Values (default).** size 567 x 70.17; background transparent; text Museo Sans Rounded 18/23.4 600, #111111 `light.color.action.fill`.

![Body paragraph default](components/crops/prose-p-default.png)

#### Inline prose link
A link inside body prose — the legal pages carry them (/mcp prose has no inline links). Read as `prose-link` on the terms page.
States read on 2026-11-17T21:44:23.476Z (default); 2026-11-17T21:44:27.411Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 38 x 19; background transparent; text Museo Sans Rounded 16/20.8 900, #01b6ff `light.color.text.link` |

![Inline prose link default](components/crops/prose-link-default.png) ![Inline prose link hover](components/crops/prose-link-hover.png)

### Mobile (390)

The 390px surface: the mobile header (wordmark, search, hamburger) and the full-screen menu the hamburger's own press paints — closed with its own X.

#### Mobile header
The 390px header: wordmark, search button and the hamburger. Read as `m-header` on the home page at 390 wide.
Read on 2026-11-17T20:44:56.413Z.

**Values (default).** size 390 x 64; background #ffffff `light.color.bg.page`; text Museo Sans Rounded 20/20 700, #111111 `light.color.action.fill`; icon 103.42 x 21, #111111 `light.color.action.fill`.

![Mobile header default](components/crops/m-header-default.png)

#### Hamburger button
The mobile menu button. "opened" is its own press painting the full-screen menu (logo, Explore/Plans links, Log in / Get started) — closed with its own X. Read as `m-menu-button` on the home page at 390 wide.
States read on 2026-11-17T20:44:58.606Z (default); 2026-11-17T20:45:02.039Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 48 x 48; background transparent; text Museo Sans Rounded 13.33/normal 400, #111111 `light.color.action.fill`; icon 24 x 24, #111111 `light.color.action.fill` |
| opened | size 390 x 614; padding 0px 20px; text Museo Sans Rounded 32/32 700, #111111 `light.color.action.fill`; icon none; layers a.sign-in.button-tertiary 351.0x54.0 #111111 0px 0px 0px 2px inset 64px; a.button-tertiary.sign-up 351.0x54.0 #111111 64px |

![Hamburger button default](components/crops/m-menu-button-default.png) ![Hamburger button opened](components/crops/m-menu-button-opened.png)

## Icons

39 distinct inline-SVG icons were collected from the live pages into [icons/](icons) by `tools/capture/icons.mjs`, indexed in [icons/INDEX.tsv](icons/INDEX.tsv): a file is named from `tools/capture/icon-names.tsv` where its geometry hash is listed, else the label or class of the control it sits in, else `icon-<hash>`; colour is kept as `currentColor` wherever it matched the text colour, so each icon recolours from CSS `color` the way it does on the site. The icons are the product's artwork — borrow the set's grammar (sizes, stroke-vs-fill, naming roles), never the artwork itself.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [icon-b5cb0ec1](icons/icon-b5cb0ec1.svg) | 60x24 | 0 0 152 61 | fill | home; explore; plans; service; applet; connect; mcp; about; careers | More credits, more possibilities Upgrade |
| [icon-a9f0c2bf](icons/icon-a9f0c2bf.svg) | 20x20 | 0 0 25 25 | fill | home; explore; plans; service; applet; connect; mcp; about; careers |  |
| [share](icons/share.svg) | 24x24 | 0 0 24 24 | fill | service; applet; connect | share |
| [polling-trigger](icons/polling-trigger.svg) | 12x12 | 0 0 24 22 | fill | service; applet; connect | Polling trigger |
| [back-button](icons/back-button.svg) | 24x24 | 0 0 24 24 | fill | service; applet; connect | Back button |
| [try-it-out](icons/try-it-out.svg) | 16x16 20x20 | 0 0 20 20 | stroke | home; explore; mcp | Try it out / Connect to IFTTT.ai MCP / More customer communi |
| [icon-69e13004](icons/icon-69e13004.svg) | 28x16 40x22 | 0 0 28 16 | stroke | service; connect |  |
| [value-prop-title](icons/value-prop-title-a1c8396e.svg) | 12x12 18x18 | 0 0 22 24 | fill | home; applet; connect | Your integrations, your way / Query |
| [icon-27b481ef](icons/icon-27b481ef.svg) | 48x48 | 0 0 28 28 | fill | service |  |
| [quote-icon](icons/quote-icon.svg) | 62x42 | 0 0 48 32 | fill | home; mcp | I use IFTTT.ai for my business in many w / I use IFTTT.ai to |
| [bin-full](icons/bin-full.svg) | 16x16 | 0 0 16 11 | fill | applet; connect | Bin full / Clean by Room / Any new photo by you |
| [facebook](icons/facebook.svg) | 16x11 | 0 0 16 11 | fill | service | Facebook / Instagram / Fleep |
| [value-prop-title](icons/value-prop-title-a53d1a36.svg) | 16x16 18x18 | 0 0 21 23 | fill | home; applet | Energy-saving automations / Realtime trigger |
| [action](icons/action.svg) | 12x12 16x16 | 0 0 25 25 | fill | applet; connect | Action |
| [icon-11313cb7](icons/icon-11313cb7.svg) | 24x24 | 0 0 24 24 | fill | plans |  |
| [location](icons/location.svg) | 15x20 | 0 0 15 22 | fill | applet | Location / iRobot |
| [claude-paid-plans](icons/claude-paid-plans.svg) | 14x14 | 0 0 24 24 | stroke | mcp | Claude paid plans / Add IFTTT to Claude |
| [up-level-with-ai](icons/up-level-with-ai.svg) | 18x18 | 0 0 19 18 | fill | home | Up-level with AI |
| [icon-21c07798](icons/icon-21c07798.svg) | 56x56 | 0 0 56 56 | fill | service |  |
| [value-prop-title](icons/value-prop-title-36ebbd56.svg) | 18x18 | 0 0 18 18 | fill | home | Streamline work communication |
| [icon-3746e623](icons/icon-3746e623.svg) | 56x56 | 0 0 56 56 | fill | service |  |
| [value-prop-title](icons/value-prop-title-37669afa.svg) | 18x18 | 0 0 18 18 | fill | home | Do more with multiple actions |
| [icon-464cd88f](icons/icon-464cd88f.svg) | 24x24 | 0 0 24 24 | fill | home |  |
| [icon-4a8d182e](icons/icon-4a8d182e.svg) | 24x24 | 0 0 24 24 | fill | plans |  |
| [all-features-unlocked](icons/all-features-unlocked.svg) | 16x16 | 0 0 16 16 | fill | plans | All features unlocked / Unlimited Applets / All services & i |
| [icon-7c4a587f](icons/icon-7c4a587f.svg) | 56x56 | 0 0 56 56 | fill | service |  |
| [voice-assistants](icons/voice-assistants.svg) | 18x18 | 0 0 18 18 | fill | home | Voice assistants |
| [sync-tasks-and-calendars](icons/sync-tasks-and-calendars.svg) | 18x18 | 0 0 18 18 | fill | home | Sync tasks and calendars |
| [icon-bc21a6f9](icons/icon-bc21a6f9.svg) | 21x21 | 0 0 11 11 | stroke | service |  |
| [track-billable-hours](icons/track-billable-hours.svg) | 18x18 | 0 0 18 18 | stroke | home | Track billable hours |
| [easy-diy-building](icons/easy-diy-building.svg) | 18x18 | 0 0 18 18 | fill | home | Easy DIY building |
| [icon-c78206a4](icons/icon-c78206a4.svg) | 10x10 | 0 0 10 10 | fill | plans | RECOMMENDED Pro $5.49 / month $65.88 bil |
| [value-prop-title](icons/value-prop-title-ca5ec476.svg) | 18x18 | 0 0 18 18 | fill | home | Smart home security automation |
| [value-prop-title](icons/value-prop-title-d03bed50.svg) | 18x18 | 0 0 22 22 | fill | home | Use AI to jumpstart projects |
| [icon-d16e8c22](icons/icon-d16e8c22.svg) | 32x32 | 0 0 32 32 | fill | plans |  |
| [icon-d350c96a](icons/icon-d350c96a.svg) | 56x56 | 0 0 56 56 | fill | service |  |
| [about-credits](icons/about-credits.svg) | 12x12 | 0 0 24 24 | fill | plans | About Credits / About AI in Applets / About Access to IFTTT. |
| [location-based-control](icons/location-based-control.svg) | 18x18 | 0 0 18 18 | fill | home | Location-based control |
| [icon-fed707d8](icons/icon-fed707d8.svg) | 32x32 | 0 0 16 16 | fill | plans |  |

## Gaps

### The blocked product surfaces

The signed-in product was never entered: 'Log in', 'Get started' and every /join path were measured, never followed, and no account was created. The Applet **'Connect' toggle** was never pressed — installing is an account feature. The plan cards' **'Get started'** CTAs lead to checkout and were never followed. **help.ifttt.com** answers HTTP 403 to automation, so the docs/help product is a documented blocked boundary. **platform.ifttt.com** redirects to ifttt.ai — no separate public platform surface exists. **/pricing** is not a live route (the pricing surface is /plans); a made-up route was captured as the 404. The **iOS/Android store badges** link off-site and were never followed.

### Pages

- **Sign-in, /join and account surfaces** — 'Log in', 'Get started' and the plan CTAs lead to the account product: measured, never followed.
- **The Applet 'Connect' toggle and any 'Connect' action** — installing an Applet is an account feature; the control was measured at rest, never pressed.
- **help.ifttt.com (the help centre)** — returns HTTP 403 to automation on every route; the docs product is a blocked boundary, not a capture.
- **platform.ifttt.com** — redirects to ifttt.ai; no separate public platform surface exists.
- **The App Store and Play Store badges** — off-site links (apps.apple.com, play.google.com); external surfaces, out of scope.
- **/pricing** — not a live route; /plans is the pricing surface. A made-up route was captured as the product's 404.
- **Long pages** — the explore galleries (~17k+ px) shots are bounded at eight chunks; the sidecars record the boundary.

### States

- **Pressed** was forced with DevTools on the controls that carry it, so a state a script adds on mousedown (if any) is missing.
- **The search and prompt fields were never queried** — clicked into for the focus look only; the 'Start building' submit and the search results surfaces were never exercised.
- **The share modal's 'Copy'** — measured inside the opened modal, never pressed (a clipboard side effect); the social share icons were never followed.
- **The billing switch** was pressed for the Monthly repaint, then Yearly (the default) was restored.
- **'Log in', 'Get started', 'Join today', plan CTAs and store badges** — measured, never followed: sign-in, sign-up, checkout and off-site surfaces are boundaries.

### Themes

IFTTT paints one theme on every signed-out surface: there is no theme control anywhere, `prefers-color-scheme` emulation does not repaint the page, and the dark grounds on /explore and the service/applet/connect heroes are painted sections reading their own literals — not a switched :root. The package therefore has a `light` set alone; dark-painted values live under light.component.dark as the measured values they are. No dark theme was fabricated.

### Fonts

- **Museo Sans Rounded is proprietary and never shipped**: the site serves weights 300/500/700/900 plus italics from web-assets.ifttt.com — the faces are measured and declared by name only (raw/css-vars.json fonts); the style guide falls back to system faces.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- The rendered brand strings and applet copy on the captured pages are the product's published content.
- Public service names, applet authors and use counts on the captured pages are published content and are kept; nothing private was captured.

### Content left out

- Applet and service copy, plan feature lists and blog/story text are the product's published content; only frames and components were measured.
