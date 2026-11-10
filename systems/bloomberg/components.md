# Bloomberg components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from bloomberg.com on 2026-11-10, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, subscribed, bought or submitted; the paywall fence was never crossed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (59 components, 82 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (88 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the news surface paints one light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home front (Asia edition) | `/asia` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [signin](screenshots/home-light-signin.png), [sitemap](screenshots/home-light-sitemap.png) |
| Markets | `/markets` | [default](screenshots/markets-light-default.png), [full](screenshots/markets-light-full.png) |
| Economics front | `/economics` | [default](screenshots/economics-light-default.png), [full](screenshots/economics-light-full.png) |
| Article (paywalled) | `first story link on the home front` |  |
| S&P 500 quote | `/quote/SPX:IND` | [default](screenshots/quote-light-default.png), [full](screenshots/quote-light-full.png) |
| Live TV | `/live` | [default](screenshots/live-light-default.png), [full](screenshots/live-light-full.png) |
| Subscription offers | `/subscriptions` | [default](screenshots/subscriptions-light-default.png), [full](screenshots/subscriptions-light-full.png) |
| Home front, phone | `/asia` |  |
| Article, phone | `first story link on the home front` |  |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Privacy preferences modal | front pages, on some loads | did not mount on this pass; measured states would be recorded as they arrive, then hidden (never answered) | component specs recorded as missing |
| Company sitemap | utility bar, home | the 'Bloomberg the Company & Its Products' button's own toggle | [home-light-sitemap](screenshots/home-light-sitemap.png) |
| Sign-in sheet | logo bar, home | the Sign In button mounts the /account/iframe/login sheet; opened and left | [home-light-signin](screenshots/home-light-signin.png), [signin-sheet](#sign-in-sheet) |
| Article paywall | every article | the page's resting state for a signed-out reader; never crossed. The article screenshot run was PerimeterX-blocked on every retry | [paywall](#paywall-fence) |
| Live TV paywall | /live | the gated player's resting state | [live-light-default](screenshots/live-light-default.png), [live-paywall](#live-paywall) |
| Mobile menu drawer | home, phone | the mobile home front was PerimeterX-blocked on every retry of this pass | not captured |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 14 components were given a real keyboard focus. 14 draw an outline ring: `utility-toggle` (1px auto #005fcc `measured.focus-outline`, offset 2px), `signin-button` (1px auto #005fcc `measured.focus-outline`, offset 0px), `subscribe-nav` (1px auto #005fcc `measured.focus-outline`, offset 1px), `search-button` (1px auto #005fcc `measured.focus-outline`, offset 0px), `nav-link` (1px auto #005fcc `measured.focus-outline`, offset 1px), `ticker-item` (1px auto #005fcc `measured.focus-outline`, offset 1px), `story-link` (1px auto #005fcc `measured.focus-outline`, offset 1px), `quote-link` (1px auto #005fcc `measured.focus-outline`, offset 1px), `follow-button` (1px auto #005fcc `measured.focus-outline`, offset 0px), `offer-cta` (on a child: 1px dotted rgb(255, 255, 255) offset 2px), `plan-cta` (on a child: 1px dotted rgb(0, 0, 0) offset 2px), `topic-link` (1px auto #005fcc `measured.focus-outline`, offset 1px), `claim-offer` (1px auto #005fcc `measured.focus-outline`, offset 0px), `footer-link` (1px auto #005fcc `measured.focus-outline`, offset 1px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): controls deepen their fill or dim rather than scale; the nav flyout and framework icons keep their hover scale. Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, color, fill, stroke, text-decoration-color | claim-offer |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, color, fill, stroke, text-decoration-color | follow-button |
| 0.3s | `ease-in-out` | gap | live-player |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Secondary story](#secondary-story) | 333 x 38.38 | - | - | transparent | none | 0 |
| [Media module](#media-module) | 565 x 216.33 | - | - | transparent | none | 0 |
| [Plan card](#plan-card) | 402 x 255.56 | 1px solid #b3b3b3 `color.neutral.line` | - | #ffffff `color.neutral.paper` | none | 24px 0px |

## Components

### Shell and navigation

The utility strip, the black logo bar, the section nav and the sign-in sheet.

#### Privacy preferences modal
The consent/preferences card every front page mounts. Measured as it arrives, then hidden; no checkbox or button was ever answered. Read as `privacy-dialog` on the home front page.

Not on the page when it was captured.

#### Privacy checkbox
Read as `privacy-checkbox` on the home front page.

Not on the page when it was captured.

#### Privacy modal button
The modal’s own button, states only — a real click would answer the prompt, which never happens. Read as `privacy-button` on the home front page.

Not on the page when it was captured.

#### Utility bar
The thin top strip: "Bloomberg the Company & Its Products", Terminal demo, Anywhere login, customer support. Read as `utility-bar` on the home front page.

**Values (default).** size 1440 x 30; background transparent; text AvenirNextPForBBG 15/22.5 400, #f3f4ef; layers a.bb-that__skip-to-content 20.0x1.0 rgb(0, 0, 0); a.bb-that-header__link 219.5x12.0 L:1px solid rgb(179, 179, 179); a.bb-that-header__link 239.2x16.0 L:1px solid rgb(179, 179, 179); a.bb-that-header__link 188.5x12.0 L:1px solid rgb(179, 179, 179); section.bb-that-category 327.2x231.0 rgb(20, 20, 20); section.bb-that-category 327.2x193.7 rgb(20, 20, 20).

Child layers that carry the look: a 20x1 background #000000 `color.neutral.ink`; a 219.5x12 border 1px solid #b3b3b3 `color.neutral.line`; a 239.2x16 border 1px solid #b3b3b3 `color.neutral.line`.

![Utility bar default](components/crops/utility-bar-default.png)

#### Company sitemap toggle
Opens the "Bloomberg the Company & Its Products" sitemap dropdown. Read as `utility-toggle` on the home front page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 246.45 x 12; padding 0px 27px 0px 0px; background transparent; text AvenirNextPForBBG 12/12 600, #f3f4ef; layers ::after rgba(0, 0, 0, 0) 0px none 0.7 |
| hover | layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 2px; layers ::after rgba(0, 0, 0, 0) 0px none 0.7; a.bb-that-header__link.bb-that-header--sitemap-trigger 246.5x12.0 1px auto rgb(0, 95, 204) offset 2px |
| pressed | layers ::after rgba(0, 0, 0, 0) 0px none 1 |

![Company sitemap toggle default](components/crops/utility-toggle-default.png) ![Company sitemap toggle hover](components/crops/utility-toggle-hover.png) ![Company sitemap toggle focus-visible](components/crops/utility-toggle-focus-visible.png) ![Company sitemap toggle pressed](components/crops/utility-toggle-pressed.png)

#### Company sitemap, open
The toggle after its own press; the dropdown shows in the crop of the opened panel. Read as `utility-toggle-open` on the home front page.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Logo bar
The black bar: wordmark, Sign In, Subscribe, search. Read as `logo-bar` on the home front page.

**Values (default).** size 1326 x 52; background transparent; text BWHaasGroteskWeb 14/21 500, #ffffff `color.neutral.paper`; layers div.nav-ui-Logo__logo__TG9nb.nav-ui-Logo__dark__TG9nb 211.0x42.0 rgb(0, 0, 0); button.nav-ui-LogoBar__signInButton__TG9nb 66.8x30.0 rgb(0, 0, 0); a.nav-ui-LogoBar__subscribeButton__TG9nb 91.2x30.0 rgb(255, 255, 255) T:1px solid rgb(118, 118, 118) / R:1px solid rgb(118, 118, 118) / B:1px solid rgb(118, 118, 118) / L:1px solid rgb(118, 118, 118) 4px; div.nav-ui-LogoBar__search__TG9nb 1440.0x0.0 rgb(.

Child layers that carry the look: div 211x42 background #000000 `color.neutral.ink`; button 66.8x30 background #000000 `color.neutral.ink`; a 91.2x30 background #ffffff `color.neutral.paper` border 1px solid #767676 `color.neutral.line-strong` radius 4px.

![Logo bar default](components/crops/logo-bar-default.png)

#### Logo
Read as `logo` on the home front page.

**Values (default).** size 211 x 42; background transparent; text BWHaasGroteskWeb 16/24 400, #ffffff `color.neutral.paper`.

![Logo default](components/crops/logo-default.png)

#### Sign In button
Opens the sign-in sheet; never a real sign-in. Read as `signin-button` on the home front page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 66.77 x 30; padding 6px 10px; background #000000 `color.neutral.ink`; text BWHaasGroteskWeb 14/21 500, #ffffff `color.neutral.paper` |
| hover | text BWHaasGroteskWeb 14/21 500, #cccccc |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px |
| pressed | text BWHaasGroteskWeb 14/21 500, #cccccc |

![Sign In button default](components/crops/signin-button-default.png) ![Sign In button hover](components/crops/signin-button-hover.png) ![Sign In button focus-visible](components/crops/signin-button-focus-visible.png) ![Sign In button pressed](components/crops/signin-button-pressed.png)

#### Subscribe button
The white Subscribe CTA in the logo bar. Measured, never followed. Read as `subscribe-nav` on the home front page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 91.16 x 30; padding 6px 10px; border 1px solid #767676 `color.neutral.line-strong`; radius 4px; background #ffffff `color.neutral.paper`; text BWHaasGroteskWeb 14/21 500, #000000 `color.neutral.ink` |
| hover | background #1c1c1c `color.neutral.ticker`; text BWHaasGroteskWeb 14/21 500, #ffffff `color.neutral.paper` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |
| pressed | background #1c1c1c `color.neutral.ticker`; text BWHaasGroteskWeb 14/21 500, #ffffff `color.neutral.paper` |

![Subscribe button default](components/crops/subscribe-nav-default.png) ![Subscribe button hover](components/crops/subscribe-nav-hover.png) ![Subscribe button focus-visible](components/crops/subscribe-nav-focus-visible.png) ![Subscribe button pressed](components/crops/subscribe-nav-pressed.png)

#### Search button
Read as `search-button` on the home front page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 28 x 28; background transparent; text BWHaasGroteskWeb 16/24 400, #ffffff `color.neutral.paper`; icon 24 x 24, #ffffff `color.neutral.paper` |
| hover | text BWHaasGroteskWeb 16/24 400, #cccccc; icon 24 x 24, #cccccc |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px; layers button.nav-ui-LogoBar__searchButton__TG9nb 28.0x28.0 1px auto rgb(0, 95, 204) offset 0px |
| pressed | text BWHaasGroteskWeb 16/24 400, #cccccc; icon 24 x 24, #cccccc |

![Search button default](components/crops/search-button-default.png) ![Search button hover](components/crops/search-button-hover.png) ![Search button focus-visible](components/crops/search-button-focus-visible.png) ![Search button pressed](components/crops/search-button-pressed.png)

#### Section nav
The strip under the logo bar: Live TV, Markets, Finance, Economics …. Read as `section-nav` on the home front page.

Not on the page when it was captured.

#### Section link
Read as `nav-link` on the home front page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 75.34 x 21; background transparent; text BWHaasGroteskWeb 14/21 500, #ffffff `color.neutral.paper` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a 75.3x21.0 1px auto rgb(0, 95, 204) offset 1px |

![Section link default](components/crops/nav-link-default.png) ![Section link hover](components/crops/nav-link-hover.png) ![Section link focus-visible](components/crops/nav-link-focus-visible.png) ![Section link pressed](components/crops/nav-link-pressed.png)

#### Nav dropdown
A chevron item in the section nav; opens a subnav list. Read as `nav-dropdown` on the home front page.

Not on the page when it was captured.

#### Nav dropdown, open
After its own toggle; the opened list shows in the crop. Read as `nav-dropdown-open` on the home front page.

Not on the page when it was captured.

#### Edition selector
Read as `edition-select` on the home front page.

Not on the page when it was captured.

#### Sign-in sheet
The /account/iframe/login sheet the Sign In button mounts. Opened and left; never used. Read as `signin-sheet` on the home front page.

**Values (default).** size 700 x 675; background #ffffff `color.neutral.paper`; shadow rgba(0, 0, 0, 0.3) 0px 0px 5px 0px; text BWHaasGroteskWeb 16/24 400, #000000 `color.neutral.ink`.

![Sign-in sheet default](components/crops/signin-sheet-default.png)

#### Sign-in email field
Inside the sign-in iframe. Focused only; nothing typed. Read as `signin-email` on the home front page.

Not on the page when it was captured.

#### Sign-in continue
The sheet’s submit, measured at rest and never pressed. Read as `signin-continue` on the home front page.

Not on the page when it was captured.

### Home front

The ticker strip, the lead story, secondary blocks and topic lanes.

#### Ticker bar
The securities strip: Top Securities plus index quotes. Read as `ticker-bar` on the home front page.

**Values (default).** size 1326 x 55; padding 0px 0px 1px 0px; border R: 1px solid #b3b3b3 `color.neutral.line`; B: 1px solid #b3b3b3 `color.neutral.line`; L: 1px solid #b3b3b3 `color.neutral.line`; background transparent; text BWHaasGroteskWeb 14/21 500, #000000 `color.neutral.ink`; icon 16 x 16, #000000 `color.neutral.ink`; layers div.PhoenixTickerBarWrapper_tickerBarWrapper__2cAU2 1326.0x55.0 R:1px solid rgb(179, 179, 179) / B:1px solid rgb(179, 179, 179) / L:1px solid rgb(179, 179, 179); div.media-ui-TickerBarWithPill_securities-QkJSeChnEgQ-.button-dropdown 165.4x53.0 rgb(0, 0, 0) 0px 0px 0px 0px; ul.media-ui-ButtonDropdown_menu-nTOQvv7qJHg- 0.0x0.0 rgb(255, 255, 255) T:1px solid rgb(248, 248, 248) / R:1px solid rgb(248, .

Child layers that carry the look: div 1326x55 border 1px solid #b3b3b3 `color.neutral.line`; div 165.4x53 shadow #000000 `color.neutral.ink` 0px 0px 0px 0px; ul 0x0 background #ffffff `color.neutral.paper` border 1px solid #f8f8f8 radius 4px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px.

![Ticker bar default](components/crops/ticker-bar-default.png)

#### Ticker quote
One index in the strip (S&P 500 and its change). Links to the quote page; measured, never followed. Read as `ticker-item` on the home front page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 211.73 x 31.5; padding 0px 10px 0px 0px; background transparent; text BWHaasGroteskWeb 14/17.5 500, #ffffff `color.neutral.paper`; icon 12 x 10, #f05143; layers div.media-ui-SecurityPill_securityPill-tHtSdrlxcjI-.media-ui-SecurityPill_negative-3yJm-9q9Vkg- 201.7x31.5 rgb(28, 28, 28) 8px |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a.media-ui-TickerBarWithPill_ticker-5arx5cdkyZQ- 211.7x31.5 1px auto rgb(0, 95, 204) offset 1px; div.media-ui-SecurityPill_securityPill-tHtSdrlxcjI-.media-ui-SecurityPill_negative-3yJm-9q9Vkg- 201.7x31.5 rgb(28, 28, 28) 8px |

Child layers that carry the look: div 201.7x31.5 background #1c1c1c `color.neutral.ticker` radius 8px.

![Ticker quote default](components/crops/ticker-item-default.png) ![Ticker quote hover](components/crops/ticker-item-hover.png) ![Ticker quote focus-visible](components/crops/ticker-item-focus-visible.png) ![Ticker quote pressed](components/crops/ticker-item-pressed.png)

#### Security pill
Read as `ticker-pill` on the home front page.

**Values (default).** size 201.73 x 31.5; padding 6px 8px 8px 8px; radius 8px; background #1c1c1c `color.neutral.ticker`; text BWHaasGroteskWeb 14/17.5 500, #ffffff `color.neutral.paper`; icon 12 x 10, #f05143.

![Security pill default](components/crops/ticker-pill-default.png)

#### Lead story block
The top-story frame on the front page. Read as `hero-story` on the home front page.

**Values (default).** size 459 x 109.56; background transparent; text BWHaasHead 32/33.6 500, #000000 `color.neutral.ink`.

![Lead story block default](components/crops/hero-story-default.png)

#### Lead headline
The big BWHaasGrotesk headline of the lead story. Read as `hero-headline` on the home front page.

**Values (default).** size 459 x 67.19; background transparent; text BWHaasHead 32/33.6 500, #000000 `color.neutral.ink`.

![Lead headline default](components/crops/hero-headline-default.png)

#### Secondary story
A smaller story block beside the lead. Read as `story-secondary` on the home front page.

**Values (default).** size 333 x 38.38; background transparent; text BWHaasGroteskWeb 16/19.2 500, #000000 `color.neutral.ink`.

![Secondary story default](components/crops/story-secondary-default.png)

#### Story link
A headline link; measured, never followed. Read as `story-link` on the home front page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 333 x 38.38; background transparent; text BWHaasGroteskWeb 16/19.2 500, #000000 `color.neutral.ink` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; text BWHaasGroteskWeb 16/19.2 500, #545454; layers a.StoryBlock_storyLink__5nXw8 333.0x38.4 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text BWHaasGroteskWeb 16/19.2 500, #545454 |

![Story link default](components/crops/story-link-default.png) ![Story link hover](components/crops/story-link-hover.png) ![Story link focus-visible](components/crops/story-link-focus-visible.png) ![Story link pressed](components/crops/story-link-pressed.png)

#### Story dek
The summary paragraph under a headline. Read as `dek` on the home front page.

**Values (default).** size 459 x 36.38; background transparent; text BWHaasGroteskWeb 14/18.2 400, #3c3c3c `color.neutral.body`.

![Story dek default](components/crops/dek-default.png)

#### Module title
A section header on the front (a topic or lane name). Read as `section-title` on the home front page.

**Values (default).** size 48.42 x 19.19; background transparent; text BWHaasGroteskWeb 16/19.2 700, #000000 `color.neutral.ink`.

![Module title default](components/crops/section-title-default.png)

#### Subscriber-only badge
The caps label marking paywalled stories. Read as `subscriber-badge` on the home front page.

Not on the page when it was captured.

#### Media module
A video/story card in a topic lane. Read as `media-module` on the home front page.

**Values (default).** size 565 x 216.33; background transparent; text BWHaasGroteskWeb 10/12 500, #545454; layers div.video-js.vjs-paused 247.0x138.9 rgb(0, 0, 0); div.vjs-title-bar.vjs-hidden 0.0x0.0; div.vjs-loading-spinner 0.0x0.0 T:8px solid rgba(43, 51, 63, 0.7) / R:8px solid rgba(43, 51, 63, 0.7) / B:8px solid rgba(43, 51, 63, 0.7) / L:8px solid rgba(43, 51, 63, 0.7) 50%; div::before.vjs-loading-spinner 70pxx70px T:8px solid rgb(255, 255, 255) / R:8px solid rgba(0, 0, 0, 0) / B:8px solid rgba(0, 0, 0, 0.

Child layers that carry the look: div 247x138.9 background #000000 `color.neutral.ink`; div 0x0 image linear-gradient(rgba(0, 0, 0, 0.8) 4.32%, transparent 95.05%); div 0x0 border 8px solid rgba(43, 51, 63, 0.7) radius 50%.

![Media module default](components/crops/media-module-default.png)

### Markets

The markets front: index cards and mover rows.

#### Markets title
Read as `markets-title` on the markets front page.

Not on the page when it was captured.

#### Index card
A market index summary card. Read as `index-card` on the markets front page.

Not on the page when it was captured.

#### Quote link
A row linking a security’s quote page; measured, never followed. Read as `quote-link` on the markets front page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 211.73 x 31.5; padding 0px 10px 0px 0px; background transparent; text BWHaasGroteskWeb 14/17.5 500, #ffffff `color.neutral.paper`; icon 12 x 10, #f05143; layers div.media-ui-SecurityPill_securityPill-tHtSdrlxcjI-.media-ui-SecurityPill_negative-3yJm-9q9Vkg- 201.7x31.5 rgb(28, 28, 28) 8px |
| hover | layers div.media-ui-SecurityPill_securityPill-tHtSdrlxcjI-.media-ui-SecurityPill_negative-3yJm-9q9Vkg- 201.7x31.5 rgb(60, 60, 60) 8px |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a.media-ui-TickerBarWithPill_ticker-5arx5cdkyZQ- 211.7x31.5 1px auto rgb(0, 95, 204) offset 1px; div.media-ui-SecurityPill_securityPill-tHtSdrlxcjI-.media-ui-SecurityPill_negative-3yJm-9q9Vkg- 201.7x31.5 rgb(28, 28, 28) 8px |

Child layers that carry the look: div 201.7x31.5 background #1c1c1c `color.neutral.ticker` radius 8px.

![Quote link default](components/crops/quote-link-default.png) ![Quote link hover](components/crops/quote-link-hover.png) ![Quote link focus-visible](components/crops/quote-link-focus-visible.png) ![Quote link pressed](components/crops/quote-link-pressed.png)

#### Market tab
Read as `market-tab` on the markets front page.

Not on the page when it was captured.

### Article (paywalled)

The article frame up to the fence: headline, byline, lede and the paywall band.

#### Kicker
The section breadcrumb over the headline (Technology / AI). Read as `article-kicker` on the article page.

**Values (default).** size 194 x 116.19; background transparent; text BWHaasGroteskWeb 24/28.8 400, #000000 `color.neutral.ink`.

![Kicker default](components/crops/article-kicker-default.png)

#### Article headline
Read as `article-headline` on the article page.

**Values (default).** size 777 x 88.19; background transparent; text BWHaasGroteskWeb 42/44.1 700, #000000 `color.neutral.ink`.

![Article headline default](components/crops/article-headline-default.png)

#### Byline
Read as `byline` on the article page.

**Values (default).** size 618 x 127.78; background transparent; text BWHaasGroteskWeb 18/21.6 400, #000000 `color.neutral.ink`; icon 20 x 20, #000000 `color.neutral.ink`; layers button._bookmarksButton_1jxg5_1.outlined-button 87.0x30.0 rgb(255, 255, 255) T:1px solid rgb(107, 114, 128) / R:1px solid rgb(107, 114, 128) / B:1px solid rgb(107, 114, 128) / L:1px solid rgb(107, 114, 128) 9999px; button.styles_readInEnglish__DG_5t.outlined-button 103.1x30.0 rgb(255, 255, 255) T:1px solid rgb(107, 114, 128) / R:1px solid rgb(107, 114, 128) / B:1px solid rgb(107, 114, 128) / L:1px.

Child layers that carry the look: button 87x30 background #ffffff `color.neutral.paper` border 1px solid #6b7280 radius 9999px; button 103.1x30 background #ffffff `color.neutral.paper` border 1px solid #6b7280 radius 9999px.

![Byline default](components/crops/byline-default.png)

#### Lede media
The lede image/video frame (the video itself errors headless). Read as `lede-media` on the article page.

**Values (default).** size 618 x 399.63; background transparent; text BWHaasGroteskWeb 20/24 500, #ffffff `color.neutral.paper`; layers button.media-ui-IconButton_wrapper-ZtMlyZ3p34k-.media-ui-IconButton_outlined-z7c334w-V9s- 0.0x0.0 T:1px solid rgb(153, 153, 153) / R:1px solid rgb(153, 153, 153) / B:1px solid rgb(153, 153, 153) / L:1px solid rgb(153, 153, 153) 9999px; button::after.media-ui-IconButton_wrapper-ZtMlyZ3p34k-.media-ui-IconButton_outlined-z7c334w-V9s- autoxauto rgb(0, 0, 0); button.media-ui-IconButton_wrapper-ZtMlyZ3p.

Child layers that carry the look: button 0x0 border 1px solid #999999 radius 9999px; button::after autoxauto background #000000 `color.neutral.ink`; button 0x0 border 1px solid #999999 radius 9999px.

![Lede media default](components/crops/lede-media-default.png)

#### Share link
Read as `share-button` on the article page.

Not on the page when it was captured.

#### Topic link
A related-topic pill under the nav. Read as `topic-link` on the article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 199.61 x 19; background transparent; text BWHaasGroteskWeb 16/24 400, #000000 `color.neutral.ink` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a 199.6x19.0 1px auto rgb(0, 95, 204) offset 1px |

![Topic link default](components/crops/topic-link-default.png) ![Topic link hover](components/crops/topic-link-hover.png) ![Topic link focus-visible](components/crops/topic-link-focus-visible.png) ![Topic link pressed](components/crops/topic-link-pressed.png)

#### Paywall fence
The "Get unlimited access" band that gates the article body. The boundary of the public capture: nothing past it is public. Read as `paywall` on the article page.

**Values (default).** size 1440 x 164.39; padding 0px 16px 24px 16px; background #1c1c1c `color.neutral.ticker`; text BWHaasGroteskWeb 32/32 700, #ffffff `color.neutral.paper`.

![Paywall fence default](components/crops/paywall-default.png)

#### Claim offer CTA
The paywall’s action; links to the offers page, measured, never followed. Read as `claim-offer` on the article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 171.08 x 46; padding 0px 24px; radius 8px; background #ffffff `color.neutral.paper`; text BWHaasGroteskWeb 16/16 500, #000000 `color.neutral.ink`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #efefef `color.neutral.smoke` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px |
| pressed | background #efefef `color.neutral.smoke` |

![Claim offer CTA default](components/crops/claim-offer-default.png) ![Claim offer CTA hover](components/crops/claim-offer-hover.png) ![Claim offer CTA focus-visible](components/crops/claim-offer-focus-visible.png) ![Claim offer CTA pressed](components/crops/claim-offer-pressed.png)

#### Body paragraph
A body-text paragraph; absent while the paywall holds. Read as `article-body` on the article page.

Not on the page when it was captured.

### Quote page

The public quote: name, price, change and key stats.

#### Quote title
The index name and ticker (S&P 500 INDEX / SPX:IND). Read as `quote-title` on the quote page.

**Values (default).** size 618 x 72.39; background transparent; text BWHaasGroteskWeb 32/38.4 700, #000000 `color.neutral.ink`; icon 16 x 16, #ffffff `color.neutral.paper`; layers button.media-ui-RoundedToggleButton_RoundedToggleButton-jupSnVE3YEE-.media-ui-RoundedToggleButton_baseBackground-xtN1SsCKNUk- 113.0x31.0 rgb(0, 0, 0) T:1px solid rgb(0, 0, 0) / R:1px solid rgb(0, 0, 0) / B:1px solid rgb(0, 0, 0) / L:1px solid rgb(0, 0, 0) 9999px; button.media-ui-RoundedToggleButton_RoundedToggleButton-jupSnVE3YEE-.media-ui-RoundedToggleButton_baseBackground-xtN1SsCKNUk- 0.0x0.0 rg.

Child layers that carry the look: button 113x31 background #000000 `color.neutral.ink` border 1px solid #000000 `color.neutral.ink` radius 9999px; button 0x0 background #000000 `color.neutral.ink` border 1px solid #000000 `color.neutral.ink` radius 9999px.

![Quote title default](components/crops/quote-title-default.png)

#### Follow button
The Follow toggle beside the title — a real press would need an account, so it was never pressed. Read as `follow-button` on the quote page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 113 x 31; padding 4px 12px; border 1px solid #000000 `color.neutral.ink`; radius 9999px; background #000000 `color.neutral.ink`; text BWHaasGroteskWeb 14/21 500, #ffffff `color.neutral.paper`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #ffffff `color.neutral.paper` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px |
| pressed | background #3c3c3c `color.neutral.body` |

![Follow button default](components/crops/follow-button-default.png) ![Follow button hover](components/crops/follow-button-hover.png) ![Follow button focus-visible](components/crops/follow-button-focus-visible.png) ![Follow button pressed](components/crops/follow-button-pressed.png)

#### Last price
Read as `quote-price` on the quote page.

Not on the page when it was captured.

#### Price change
Read as `quote-change` on the quote page.

Not on the page when it was captured.

#### Key stat
A key-statistics row (open, range, market cap). Read as `quote-stat` on the quote page.

Not on the page when it was captured.

### Live TV

The gated live player and its schedule.

#### Live player
The gated live-TV frame; the stream itself needs an account. Read as `live-player` on the live TV page.

**Values (default).** size 1252 x 457.48; background transparent; text BWHaasGroteskWeb 20/24 500, #ffffff `color.neutral.paper`; transition gap 0.3s ease-in-out; layers div.video-js.vjs-paused 813.3x457.5 rgb(0, 0, 0); div.vjs-title-bar.vjs-hidden 0.0x0.0; div.vjs-loading-spinner 0.0x0.0 T:8px solid rgba(43, 51, 63, 0.7) / R:8px solid rgba(43, 51, 63, 0.7) / B:8px solid rgba(43, 51, 63, 0.7) / L:8px solid rgba(43, 51, 63, 0.7) 50%; div::before.vjs-loading-spinner 70pxx70px T:8px solid rgb(255, 255, 255) / R:8px solid rgba(0, 0, 0, 0) / B:8px solid rgba(0, 0, 0, 0.

Child layers that carry the look: div 813.3x457.5 background #000000 `color.neutral.ink`; div 0x0 image linear-gradient(rgba(0, 0, 0, 0.8) 4.32%, transparent 95.05%); div 0x0 border 8px solid rgba(43, 51, 63, 0.7) radius 50%.

![Live player default](components/crops/live-player-default.png)

#### Live paywall
Read as `live-paywall` on the live TV page.

**Values (default).** size 813.33 x 457.48; background transparent; text BWHaasGroteskWeb 20/24 500, #ffffff `color.neutral.paper`; layers div.video-js.vjs-paused 813.3x457.5 rgb(0, 0, 0); div.vjs-title-bar.vjs-hidden 0.0x0.0; div.vjs-loading-spinner 0.0x0.0 T:8px solid rgba(43, 51, 63, 0.7) / R:8px solid rgba(43, 51, 63, 0.7) / B:8px solid rgba(43, 51, 63, 0.7) / L:8px solid rgba(43, 51, 63, 0.7) 50%; div::before.vjs-loading-spinner 70pxx70px T:8px solid rgb(255, 255, 255) / R:8px solid rgba(0, 0, 0, 0) / B:8px solid rgba(0, 0, 0, 0.

Child layers that carry the look: div 813.3x457.5 background #000000 `color.neutral.ink`; div 0x0 image linear-gradient(rgba(0, 0, 0, 0.8) 4.32%, transparent 95.05%); div 0x0 border 8px solid rgba(43, 51, 63, 0.7) radius 50%.

![Live paywall default](components/crops/live-paywall-default.png)

#### Schedule row
Read as `live-schedule` on the live TV page.

Not on the page when it was captured.

### Subscription offers

The WordPress offer pages: hero block, price and plan cards.

#### Offers header
Read as `offer-header` on the subscription offers page.

**Values (default).** size 1254 x 30; background transparent; text AvenirNextPForBBG 12/12 600, #f3f4ef; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1; a.bb-that-header__link 219.5x12.0 L:1px solid rgb(179, 179, 179); a.bb-that-header__link 239.2x16.0 L:1px solid rgb(179, 179, 179); a.bb-that-header__link 188.5x12.0 L:1px solid rgb(179, 179, 179).

Child layers that carry the look: a 219.5x12 border 1px solid #b3b3b3 `color.neutral.line`; a 239.2x16 border 1px solid #b3b3b3 `color.neutral.line`; a 188.5x12 border 1px solid #b3b3b3 `color.neutral.line`.

![Offers header default](components/crops/offer-header-default.png)

#### Offer hero
The lead WordPress offer block ("Get context beyond the headlines"). Read as `offer-hero` on the subscription offers page.

**Values (default).** size 1290 x 512; padding 16px 18px; background transparent; text BW Haas Grotesk Web 40/44 700, #ffffff `color.neutral.paper`; layers div.wp-block-group.header-left-column 534.0x359.6 rgb(0, 0, 0); a.wp-ga-button.button-dark-theme 247.0x48.0 rgb(53, 35, 255) 8px.

Child layers that carry the look: div 534x359.6 background #000000 `color.neutral.ink`; a 247x48 background #3523ff `color.brand.accent` radius 8px.

![Offer hero default](components/crops/offer-hero-default.png)

#### Offer price
Read as `offer-price` on the subscription offers page.

**Values (default).** size 372.75 x 24; background transparent; text BW Haas Grotesk Web 20/24 700, #808080.

![Offer price default](components/crops/offer-price-default.png)

#### Offer CTA
The offer’s own action; links to checkout, measured, never followed. Read as `offer-cta` on the subscription offers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 247 x 48; background transparent; text BW Haas Grotesk Web 16/24.8 500, #ffffff `color.neutral.paper`; layers a.wp-ga-button.button-dark-theme 247.0x48.0 rgb(53, 35, 255) 8px |
| hover | layers a.wp-ga-button.button-dark-theme 247.0x48.0 rgb(79, 79, 255) 8px |
| focus-visible | layers a.wp-ga-button.button-dark-theme 247.0x48.0 rgb(53, 35, 255) 1px dotted rgb(255, 255, 255) offset 2px 8px |

Child layers that carry the look: a 247x48 background #3523ff `color.brand.accent` radius 8px.

![Offer CTA default](components/crops/offer-cta-default.png) ![Offer CTA hover](components/crops/offer-cta-hover.png) ![Offer CTA focus-visible](components/crops/offer-cta-focus-visible.png) ![Offer CTA pressed](components/crops/offer-cta-pressed.png)

#### Plan card
A rate-plan option block (billing choices). Read as `plan-card` on the subscription offers page.

**Values (default).** size 402 x 255.56; padding 24px 0px; border 1px solid #b3b3b3 `color.neutral.line`; background #ffffff `color.neutral.paper`; text BW Haas Grotesk Web 20/24 500, #000000 `color.neutral.ink`.

![Plan card default](components/crops/plan-card-default.png)

#### Plan CTA
Read as `plan-cta` on the subscription offers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 376 x 48; background transparent; text BW Haas Grotesk Web 16/19.2 500, #000000 `color.neutral.ink`; layers a.wp-ga-button.button-light-theme 354.0x48.0 rgb(255, 255, 255) T:1px solid rgb(0, 0, 0) / R:1px solid rgb(0, 0, 0) / B:1px solid rgb(0, 0, 0) / L:1px solid rgb(0, 0, 0) 8px |
| hover | layers a.wp-ga-button.button-light-theme 354.0x48.0 rgb(239, 239, 239) T:1px solid rgb(0, 0, 0) / R:1px solid rgb(0, 0, 0) / B:1px solid rgb(0, 0, 0) / L:1px solid rgb(0, 0, 0) 8px |
| focus-visible | layers a.wp-ga-button.button-light-theme 354.0x48.0 rgb(255, 255, 255) T:1px solid rgb(0, 0, 0) / R:1px solid rgb(0, 0, 0) / B:1px solid rgb(0, 0, 0) / L:1px solid rgb(0, 0, 0) 1px dotted rgb(0, 0, 0) offset 2px 8px |

Child layers that carry the look: a 354x48 background #ffffff `color.neutral.paper` border 1px solid #000000 `color.neutral.ink` radius 8px.

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

### Footer

The sitemap and legal row.

#### Footer
Read as `footer` on the home front page.

**Values (default).** size 605.52 x 21; background transparent; text BWHaasGroteskWeb 14/21 500, #ffffff `color.neutral.paper`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home front page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 177 x 42; background transparent; text BWHaasGroteskWeb 16/24 400, #ffffff `color.neutral.paper` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a.nav-ui-Logo__logo__TG9nb 177.0x42.0 1px auto rgb(0, 95, 204) offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Bloomberg's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### PerimeterX rate-limiting

bloomberg.com runs PerimeterX: after a run of automated loads it serves an "unusual activity / PRESS & HOLD" challenge for a while to this client. On this pass the article route's screenshots and every 390px mobile load were challenge-gated on every retry, and the stylesheet harvest (raw/css-vars.json) came back thin for the same reason — so the tokens are measured computed values, not var aliases, and the mobile group is recorded as missing rather than fabricated.

### Pages

- **The article body, comments and every page past the fence.** The subscription paywall is the boundary of the public capture: an article renders its kicker, headline, byline and lede, then the 'Get unlimited access' band. Nothing below it is public and nothing in it was measured.
- **The signed-in product.** Portfolio, watchlist, alerts, account settings, the real Live TV stream and Bloomberg Terminal surfaces need an account and were never reached. The sign-in sheet and the Follow button were opened/measured, never used.
- **Search.** The search button was measured; no query was ever run.
- **Checkout.** The offer CTAs link to the checkout flow; every one was measured at rest and never followed.
- **bloombergmedia.com, the Terminal and the app.** Separate front ends, not part of this capture.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface; the paywalled page is itself an error-adjacent resting state.

### Themes

The news surface paints one light theme on every captured route; the /subscriptions offer pages invert their hero to near-black by design, still light theme. No dark or reduced-contrast mode is offered.

### Fonts

- **BWHaasGrotesk** (Haas Grotesk for Bloomberg) is the licensed news face — headlines, prices, UI. It is not distributed; the style guide falls back to Helvetica.
- **Avenir Next for Bloomberg** (AvenirNextPForBBG) is the licensed UI/label face — nav labels, badges, tickers. Also not distributed.

### Screenshots

- Photography, the Bloomberg wordmark and ad creative in the screenshots are Bloomberg's and its advertisers' content. The article captured is whichever story the home front listed first at run time (recorded as `article` in components-computed.json); another run lands on a different story.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Story photography, video stills, market charts and the leaderboard ads are the product's content; only the frames and components were measured.
