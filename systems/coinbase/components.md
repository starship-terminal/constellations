# Coinbase components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from coinbase.com on 2026-11-17, signed out, in headed Chromium (Cloudflare gates headless) at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, paid for or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (38 components, 85 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `CoinbaseSans 16/24 400, #0a0b0d`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (87 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png`; every public route paints the same light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages (1x on desktop, 2x on mobile); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/en-sg` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Explore (prices) | `/en-sg/explore` | [default](screenshots/explore-light-default.png), [full](screenshots/explore-light-full.png) |
| Coinbase One | `/en-sg/one` | [default](screenshots/one-light-default.png), [full](screenshots/one-light-full.png) |
| Business | `/en-sg/business` | [default](screenshots/business-light-default.png), [full](screenshots/business-light-full.png) |
| Prime | `/en-sg/prime` | [default](screenshots/prime-light-default.png), [full](screenshots/prime-light-full.png) |
| Advanced Trade | `/en-sg/advanced-trade` | [default](screenshots/advanced-light-default.png), [full](screenshots/advanced-light-full.png) |
| Developer Platform | `/en-sg/developer-platform` | [default](screenshots/developers-light-default.png), [full](screenshots/developers-light-full.png) |
| USDC | `/en-sg/usdc` | [default](screenshots/usdc-light-default.png), [full](screenshots/usdc-light-full.png) |
| Learn | `/en-sg/learn` | [default](screenshots/learn-light-default.png), [full](screenshots/learn-light-full.png) |
| About | `/en-sg/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Careers | `/en-sg/careers` | [default](screenshots/careers-light-default.png), [full](screenshots/careers-light-full.png) |
| Blog | `/en-sg/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Privacy | `/legal/privacy` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| Sign-in (boundary) | `login.coinbase.com/signin` | [default](screenshots/signin-light-default.png) |
| Home, phone | `/en-sg` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu-open](screenshots/mobile-home-light-menu-open.png) |
| Explore, phone | `/en-sg/explore` | [default](screenshots/mobile-explore-light-default.png), [full](screenshots/mobile-explore-light-full.png) |
| Coinbase One, phone | `/en-sg/one` | [default](screenshots/mobile-one-light-default.png), [full](screenshots/mobile-one-light-full.png) |
| Business, phone | `/en-sg/business` | [default](screenshots/mobile-business-light-default.png), [full](screenshots/mobile-business-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu, open | bar, phone | the hamburger's own press | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-menu-open](#m-menu-open) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 14 components were given a real keyboard focus (a further 1 could not be driven: `signin-submit`). 14 show a visible focus state: `nav-item` (1px auto #101010, offset 1px), `nav-signin` (2px solid #0052ff `color.blue.60`, offset 2px), `nav-cta` (2px solid #0052ff `color.blue.60`, offset 2px), `hero-cta` (2px solid #0052ff `color.blue.60`, offset 2px), `chip` (2px solid #578bfa, offset 2px), `cta-dark` (2px solid #0052ff `color.blue.60`, offset 2px), `price-row` (1px auto #101010, offset 0px), `one-cta` (2px solid #0052ff `color.blue.60`, offset 2px), `prime-cta` (2px solid #0052ff `color.blue.60`, offset 2px), `signin-oauth` (2px solid #0052ff `color.blue.60`, offset 2px), `signin-passkey` (2px solid #0052ff `color.blue.60`, offset 2px), `footer-link` (1px auto #101010, offset 1px), `footer-social` (1px auto #101010, offset 1px), `m-menu-link` (1px auto #e59700, offset 1px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). On 5 of 15 measured controls pressed reads as the same painted step as hover; the rest differ — `nav-signin`, `nav-cta`, `hero-cta`, `chip`, `cta-dark`, `one-cta`, `prime-cta`, `signin-submit`, `signin-oauth`, `signin-passkey` (their rows show the diff). Nothing a real press would submit, navigate or write (the CTAs navigate onward, the sign-in OAuth and Log-in controls submit) was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `ease-in-out` | background-color, box-shadow | explore-search, m-menu-link, promo-banner |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Promo card](#promo-card) | 1425 x 724.38 | - | - | #141519 | none | 0 |
| [Price row](#price-row) | 1002 x 76 | - | - | #ffffff `color.gray.0` | none | 0 |
| [Sign-in card](#sign-in-card) | 400 x 146 | - | - | transparent | none | 0 |
| [Dark panel](#dark-panel) | 656.5 x 640 | - | 40px | #0a0b0d `color.gray.100` | none | 0 |

## Components

### Shell and navigation

The promo banner row and the fixed site nav: the Coinbase logo, the mega-menu links, the search and language icons, the Sign-in ghost and the blue Sign-up pill.

#### Promo banner
The announcement row at the top of the header (Banner__StyledLink → /partner/ai-signup-offer) — real chrome, kept. Read as `promo-banner` on the home page.

**Values (default).** size 1425 x 48; background transparent; text CoinbaseSans 16/24 600, #11206b `color.indigo.90`; transition background-color 0.2s ease-in-out.

![Promo banner default](components/crops/promo-banner-default.png)

#### Nav bar
The fixed site header (data-testid=main-nav): Coinbase logo, mega-menu links, search + language icons, Sign in ghost and the Sign up pill. Read as `header` on the home page.

**Values (default).** size 1425 x 117; background #ffffff `color.gray.0`; text CoinbaseSans 16/24 600, #11206b `color.indigo.90`.

![Nav bar default](components/crops/header-default.png)

#### Logo
The Coinbase logo home anchor in the nav. Read as `logo` on the home page.

**Values (default).** size 44 x 44; background transparent; text CoinbaseSans 16/18.4 400, #0667d0.

![Logo default](components/crops/logo-default.png)

#### Nav link
A mega-menu nav trigger ("Crypto", data-testid=main-nav-link-prices); its dropdown renders eager in the DOM. Read as `nav-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 101.33 x 44; radius 100000px; background transparent; text CoinbaseSans 16/20 600, #0a0b0d `color.gray.100` |
| hover | child paint div.flex-ff5rfy6._1000-_tqhrr9: size 101.3x44.0; background rgba(247, 247, 247, 0.88) `color.role.bgTertiaryHovered`; radius 100000px |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.GlobalNavLink__StyledLink-sc-1a5db85c-0.jJkJkH: size 101.3x44.0; radius 100000px; outline 1px auto rgb(16, 16, 16) offset 1px |

![Nav link default](components/crops/nav-item-default.png) ![Nav link hover](components/crops/nav-item-hover.png) ![Nav link focus-visible](components/crops/nav-item-focus-visible.png) ![Nav link pressed](components/crops/nav-item-pressed.png)

#### Nav sign-in
The "Sign in" ghost button linking to login.coinbase.com; measured never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 100.95 x 44; padding 0px 24px; radius 56px; background #eef0f3 `color.gray.10`; text CoinbaseSans 16/20 600, #0a0b0d `color.gray.100` |
| hover | background rgba(229, 231, 234, 0.88) `color.role.backgroundAltHovered`; child paint a.flex-ff5rfy6.fgInverse-f1sdlwjn: background rgba(229, 231, 234, 0.88) `color.role.backgroundAltHovered` |
| focus-visible | outline 2px solid #0052ff `color.blue.60`, offset 2px; child paint a.flex-ff5rfy6.fgInverse-f1sdlwjn: outline 2px solid rgb(0, 82, 255) offset 2px |
| pressed | size 98.93 x 43.12; background rgba(242, 244, 246, 0.82) `color.role.bgSecondaryPressed`; transform scale(0.98); child paint a.flex-ff5rfy6.fgInverse-f1sdlwjn: size 98.9x43.1; background rgba(242, 244, 246, 0.82) `color.role.bgSecondaryPressed` |

![Nav sign-in default](components/crops/nav-signin-default.png) ![Nav sign-in hover](components/crops/nav-signin-hover.png) ![Nav sign-in focus-visible](components/crops/nav-signin-focus-visible.png) ![Nav sign-in pressed](components/crops/nav-signin-pressed.png)

#### Nav CTA
The blue "Sign up" CDS pill (cds-Button, bgPrimary) in the nav; links to /signup, never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 106.2 x 44; padding 0px 24px; radius 56px; background #0052ff `color.blue.60`; text CoinbaseSans 16/20 600, #ffffff `color.gray.0` |
| hover | background rgba(0, 72, 224, 0.88) `color.role.bgBrandHovered`; child paint a.flex-ff5rfy6.fgInverse-f1sdlwjn: background rgba(0, 72, 224, 0.88) `color.role.bgBrandHovered` |
| focus-visible | outline 2px solid #0052ff `color.blue.60`, offset 2px; child paint a.flex-ff5rfy6.fgInverse-f1sdlwjn: outline 2px solid rgb(0, 82, 255) offset 2px |
| pressed | size 104.08 x 43.12; background rgba(0, 67, 209, 0.82) `color.role.bgBrandPressed`; transform scale(0.98); child paint a.flex-ff5rfy6.fgInverse-f1sdlwjn: size 104.1x43.1; background rgba(0, 67, 209, 0.82) `color.role.bgBrandPressed` |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

### Home

The hero ("The most trusted crypto exchange"), the Sign-up-with-Singpass pill, the promo-carousel cards, the market chips and the .coinbase.dark band.

#### Hero title
"The most trusted crypto exchange" — the hero headline (CoinbaseDisplay scale). Read as `hero-title` on the home page.

**Values (default).** size 656.5 x 240; background transparent; text CoinbaseDisplay 80/80 400, #0a0b0d `color.gray.100`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero CTA
The "Sign up with Singpass" dark pill (cds-Button, bgInverse) under the hero copy; links to /signup, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 256.73 x 56; padding 16px 32px; radius 56px; background #0a0b0d `color.gray.100`; text CoinbaseSans 18/24 600, #ffffff `color.gray.0` |
| hover | background rgba(17, 18, 20, 0.88) `color.role.bgPrimaryHovered`; child paint a.flex-ff5rfy6.fgInverse-f1sdlwjn: background rgba(17, 18, 20, 0.88) `color.role.bgPrimaryHovered` |
| focus-visible | outline 2px solid #0052ff `color.blue.60`, offset 2px; child paint a.flex-ff5rfy6.fgInverse-f1sdlwjn: outline 2px solid rgb(0, 82, 255) offset 2px |
| pressed | size 251.6 x 54.88; background rgba(21, 22, 24, 0.82) `color.role.bgPrimaryPressed`; transform scale(0.98); child paint a.flex-ff5rfy6.fgInverse-f1sdlwjn: size 251.6x54.9; background rgba(21, 22, 24, 0.82) `color.role.bgPrimaryPressed` |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Promo card
A promo-carousel card in the home flow (promo-carousel-item-*, autoplay rotating offers). Read as `carousel-card` on the home page.

**Values (default).** size 1425 x 724.38; background #141519; text CoinbaseDisplay 52/52 400, #ffffff `color.gray.0`.

![Promo card default](components/crops/carousel-card-default.png)

#### Filter chip
A filter chip inside the dark asset panel on home ("Tradable"/"Top gainers"/"New on Coinbase", data-testid=chip, dark themed). Read as `chip` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 117.03 x 44; padding 0px 24px; radius 56px; background #282b31; text CoinbaseSans 16/20 600, #ffffff `color.gray.0` |
| hover | background rgba(47, 50, 55, 0.88); child paint button.flex-ff5rfy6.fgInverse-f1sdlwjn: background rgba(47, 50, 55, 0.88) |
| focus-visible | outline 2px solid #578bfa, offset 2px; child paint button.flex-ff5rfy6.fgInverse-f1sdlwjn: outline 2px solid rgb(87, 139, 250) offset 2px |
| pressed | size 114.69 x 43.12; background rgba(50, 53, 59, 0.82); transform scale(0.98); child paint button.flex-ff5rfy6.fgInverse-f1sdlwjn: size 114.7x43.1; background rgba(50, 53, 59, 0.82) |

![Filter chip default](components/crops/chip-default.png) ![Filter chip hover](components/crops/chip-hover.png) ![Filter chip focus-visible](components/crops/chip-focus-visible.png) ![Filter chip pressed](components/crops/chip-pressed.png)

#### Dark panel
The .coinbase.dark themed asset panel on home (the dark Tradable/Top-gainers card) — its paint lands on children; the theme element itself reads transparent. Read as `dark-band` on the home page.

**Values (default).** size 656.5 x 640; background transparent; text CoinbaseSans 16/20 600, #ffffff `color.gray.0`.

Child layers that carry the look: div 656.5x640 background #0a0b0d `color.gray.100` radius 40px; div 452.7x44 background #0a0b0d `color.gray.100`; button 117x44 background #282b31 radius 56px.

![Dark panel default](components/crops/dark-band-default.png)

#### Dark CTA
The "See more assets" dark pill under the crypto band (fgInverse on bgInverse #0a0b0d, pill radius); links to /explore, never followed. Read as `cta-dark` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 207.88 x 56; padding 16px 32px; radius 56px; background #0a0b0d `color.gray.100`; text CoinbaseSans 18/24 600, #ffffff `color.gray.0` |
| hover | background rgba(17, 18, 20, 0.88) `color.role.bgPrimaryHovered`; child paint a.flex-ff5rfy6.fgInverse-f1sdlwjn: background rgba(17, 18, 20, 0.88) `color.role.bgPrimaryHovered` |
| focus-visible | outline 2px solid #0052ff `color.blue.60`, offset 2px; child paint a.flex-ff5rfy6.fgInverse-f1sdlwjn: outline 2px solid rgb(0, 82, 255) offset 2px |
| pressed | size 203.72 x 54.88; background rgba(21, 22, 24, 0.82) `color.role.bgPrimaryPressed`; transform scale(0.98); child paint a.flex-ff5rfy6.fgInverse-f1sdlwjn: size 203.7x54.9; background rgba(21, 22, 24, 0.82) `color.role.bgPrimaryPressed` |

![Dark CTA default](components/crops/cta-dark-default.png) ![Dark CTA hover](components/crops/cta-dark-hover.png) ![Dark CTA focus-visible](components/crops/cta-dark-focus-visible.png) ![Dark CTA pressed](components/crops/cta-dark-pressed.png)

#### Section title
A display section heading in page content ("Unlock zero trading fees…" style, CoinbaseDisplay scale). Read as `section-title` on the home page.

**Values (default).** size 544 x 48; background transparent; text CoinbaseDisplay 44/48 400, #0a0b0d `color.gray.100`.

![Section title default](components/crops/section-title-default.png)

#### Page ground
The body element painted fill — the page ground. Read as `page-ground` on the home page.

**Values (default).** size 1425 x 900; background transparent; text CoinbaseSans 13/16 600, #0a0b0d `color.gray.100`.

Child layers that carry the look: div 1425x0 background #ffffff `color.gray.0`; a 1425x36 background #eef0f3 `color.gray.10`; a 1425x36 background #eef0f3 `color.gray.10`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Explore (prices)

The /explore route: the asset search, the market chips and the live crypto price table.

#### Explore title
"Explore Crypto" — the prices page headline. Read as `explore-title` on the explore page.

**Values (default).** size 194.53 x 36; background transparent; text CoinbaseDisplay 28/36 600, #0a0b0d `color.gray.100`.

![Explore title default](components/crops/explore-title-default.png)

#### Asset search field
The asset search input on /explore (input-interactable-area) — a focus reading only; nothing typed. Read as `explore-search` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 309 x 42; border 1px solid transparent; radius 100000px; background #eef0f3 `color.gray.10`; text CoinbaseSans 16/18.4 400, #000000; transition box-shadow 0.2s ease-in-out |

![Asset search field default](components/crops/explore-search-default.png) ![Asset search field focused](components/crops/explore-search-focused.png)

#### Price table
The live crypto price table (data-testid=prices-table-v2) with sortable columns. Read as `price-table` on the explore page.

**Values (default).** size 1002 x 816; background #ffffff `color.gray.0`; text CoinbaseSans 16/24 600, #5b616e `color.gray.60`; icon 64 x 32, #0a0b0d `color.gray.100`.

![Price table default](components/crops/price-table-default.png)

#### Price row
An asset row in the price table (icon, name, price, sparkline, change). Read as `price-row` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1002 x 76; background #ffffff `color.gray.0`; text CoinbaseIcons 16/16 400, #0a0b0d `color.gray.100`; icon 64 x 32, #0a0b0d `color.gray.100` |
| hover | background rgba(247, 248, 249, 0.35); child paint tr.tableRowCss-t1cncu43.tableRowHoverCss-tg1utdg: background rgba(247, 248, 249, 0.35) |
| focus-visible | background rgba(247, 248, 249, 0.35); outline 1px auto #101010, offset 0px; child paint tr.tableRowCss-t1cncu43.tableRowHoverCss-tg1utdg: background rgba(247, 248, 249, 0.35); outline 1px auto rgb(16, 16, 16) offset 0px |
| pressed | background rgba(247, 248, 249, 0.35); child paint tr.tableRowCss-t1cncu43.tableRowHoverCss-tg1utdg: background rgba(247, 248, 249, 0.35) |

![Price row default](components/crops/price-row-default.png) ![Price row hover](components/crops/price-row-hover.png) ![Price row focus-visible](components/crops/price-row-focus-visible.png) ![Price row pressed](components/crops/price-row-pressed.png)

#### Price figure
A price figure cell in the price table (the "S$132,809.31"-style value). Read as `price-figure` on the explore page.

**Values (default).** size 93.3 x 24; background transparent; text CoinbaseSans 16/24 400, #0a0b0d `color.gray.100`.

![Price figure default](components/crops/price-figure-default.png)

#### Sort icon
A sort arrow on a sortable price-table column; measured at rest, never toggled. Read as `sort-icon` on the explore page.

**Values (default).** size 12 x 12; background transparent; text CoinbaseIcons 12/12 400, #5b616e `color.gray.60`.

![Sort icon default](components/crops/sort-icon-default.png)

### Coinbase One page

The /one route: the Coinbase One subscription page.

#### Coinbase One title
The Coinbase One subscription page headline. Read as `one-title` on the one page.

**Values (default).** size 656.5 x 240; background transparent; text CoinbaseDisplay 80/80 400, #0a0b0d `color.gray.100`.

![Coinbase One title default](components/crops/one-title-default.png)

#### Coinbase One CTA
The first CDS pill CTA on the Coinbase One page; links onward, never followed. Read as `one-cta` on the one page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 235.45 x 56; padding 16px 32px; radius 56px; background #0052ff `color.blue.60`; text CoinbaseSans 18/24 600, #ffffff `color.gray.0` |
| hover | background rgba(0, 72, 224, 0.88) `color.role.bgBrandHovered`; child paint a.flex-ff5rfy6.fgInverse-f1sdlwjn: background rgba(0, 72, 224, 0.88) `color.role.bgBrandHovered` |
| focus-visible | outline 2px solid #0052ff `color.blue.60`, offset 2px; child paint a.flex-ff5rfy6.fgInverse-f1sdlwjn: outline 2px solid rgb(0, 82, 255) offset 2px |
| pressed | size 230.74 x 54.88; background rgba(0, 67, 209, 0.82) `color.role.bgBrandPressed`; transform scale(0.98); child paint a.flex-ff5rfy6.fgInverse-f1sdlwjn: size 230.7x54.9; background rgba(0, 67, 209, 0.82) `color.role.bgBrandPressed` |

![Coinbase One CTA default](components/crops/one-cta-default.png) ![Coinbase One CTA hover](components/crops/one-cta-hover.png) ![Coinbase One CTA focus-visible](components/crops/one-cta-focus-visible.png) ![Coinbase One CTA pressed](components/crops/one-cta-pressed.png)

### Prime page

The /prime route: the institutional Prime page.

#### Prime title
The Coinbase Prime institutional page headline. Read as `prime-title` on the prime page.

**Values (default).** size 1361 x 192; background transparent; text CoinbaseDisplay 96/96 400, #0a0b0d `color.gray.100`.

![Prime title default](components/crops/prime-title-default.png)

#### Prime CTA
The first CDS pill CTA on the Prime page; links onward, never followed. Read as `prime-cta` on the prime page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 165.52 x 56; padding 16px 32px; radius 56px; background #0a0b0d `color.gray.100`; text CoinbaseSans 18/24 600, #ffffff `color.gray.0` |
| hover | background rgba(17, 18, 20, 0.88) `color.role.bgPrimaryHovered`; child paint a.flex-ff5rfy6.fgInverse-f1sdlwjn: background rgba(17, 18, 20, 0.88) `color.role.bgPrimaryHovered` |
| focus-visible | outline 2px solid #0052ff `color.blue.60`, offset 2px; child paint a.flex-ff5rfy6.fgInverse-f1sdlwjn: outline 2px solid rgb(0, 82, 255) offset 2px |
| pressed | size 162.21 x 54.88; background rgba(21, 22, 24, 0.82) `color.role.bgPrimaryPressed`; transform scale(0.98); child paint a.flex-ff5rfy6.fgInverse-f1sdlwjn: size 162.2x54.9; background rgba(21, 22, 24, 0.82) `color.role.bgPrimaryPressed` |

![Prime CTA default](components/crops/prime-cta-default.png) ![Prime CTA hover](components/crops/prime-cta-hover.png) ![Prime CTA focus-visible](components/crops/prime-cta-focus-visible.png) ![Prime CTA pressed](components/crops/prime-cta-pressed.png)

### App sign-in (boundary)

login.coinbase.com/signin — the product's public login surface, measured at rest; nothing was typed, signed into or submitted.

#### Sign-in card
The login.coinbase.com sign-in surface the app paints. Measured at rest, never submitted. Read as `signin-card` on the sign-in page.

**Values (default).** size 400 x 146; background transparent; text CoinbaseSans 16/24 600, #ffffff `color.gray.0`.

Child layers that carry the look: span 400x58 background #ffffff `color.gray.0` border 1px solid rgba(91, 97, 110, 0.66) `color.role.bgLineHeavy` radius 8px; button 400x56 background #1460ff radius 56px.

![Sign-in card default](components/crops/signin-card-default.png)

#### Email field
The sign-in email input (data-testid=email-input) — a focus reading only; nothing typed, nothing sent. Read as `signin-field` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 398 x 56; padding 16px; background transparent; text CoinbaseSans 16/24 400, #0a0b0d `color.gray.100`; placeholder #5b616e `color.gray.60` |
| focused | wrapper span.flex-ff5rfy6._100-_x44gs4: shadow #0052ff 0px 0px 0px 1px; opacity 0.88 |

![Email field default](components/crops/signin-field-default.png) ![Email field focused](components/crops/signin-field-focused.png)

#### Continue button
The "Continue" submit on the sign-in card; measured never pressed — it would submit the form. Read as `signin-submit` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 400 x 56; padding 16px 32px; radius 56px; background #1460ff; text CoinbaseSans 16/24 600, #ffffff `color.gray.0`; opacity 0.5 |
| pressed | size 392 x 54.88; transform scale(0.98); child paint button.flex-ff5rfy6.fgInverse-f1sdlwjn: size 392.0x54.9 |

![Continue button default](components/crops/signin-submit-default.png) ![Continue button hover](components/crops/signin-submit-hover.png) ![Continue button pressed](components/crops/signin-submit-pressed.png)

#### OAuth button
A "Sign in with Google" OAuth row on the sign-in card; measured never pressed. Read as `signin-oauth` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 58; padding 16px 24px; border 1px solid rgba(91, 97, 110, 0.2) `color.role.bgLine`; radius 56px; background rgba(255, 255, 255, 0) `color.role.transparent`; text CoinbaseSans 16/24 600, #0a0b0d `color.gray.100`; icon 20 x 20, #0a0b0d `color.gray.100` |
| hover | border 1px solid rgba(80, 85, 97, 0.2); background transparent; child paint button.flex-ff5rfy6.fg-f1sorag4: border 1px solid rgba(80, 85, 97, 0.2) |
| focus-visible | outline 2px solid #0052ff `color.blue.60`, offset 2px; child paint button.flex-ff5rfy6.fg-f1sorag4: outline 2px solid rgb(0, 82, 255) offset 2px |
| pressed | size 392 x 56.84; border 1px solid rgba(75, 80, 90, 0.2); background transparent; transform scale(0.98); icon 19.6 x 19.6, #0a0b0d `color.gray.100`; child paint button.flex-ff5rfy6.fg-f1sorag4: size 392.0x56.8; border 1px solid rgba(75, 80, 90, 0.2) |

![OAuth button default](components/crops/signin-oauth-default.png) ![OAuth button hover](components/crops/signin-oauth-hover.png) ![OAuth button focus-visible](components/crops/signin-oauth-focus-visible.png) ![OAuth button pressed](components/crops/signin-oauth-pressed.png)

#### Passkey button
The "Sign in with passkey" row on the sign-in card; measured never pressed. Read as `signin-passkey` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 58; padding 16px 24px; border 1px solid rgba(91, 97, 110, 0.2) `color.role.bgLine`; radius 56px; background rgba(255, 255, 255, 0) `color.role.transparent`; text CoinbaseIcons 20/20 400, #0a0b0d `color.gray.100` |
| hover | border 1px solid rgba(80, 85, 97, 0.2); background transparent; child paint button.flex-ff5rfy6.fg-f1sorag4: border 1px solid rgba(80, 85, 97, 0.2) |
| focus-visible | outline 2px solid #0052ff `color.blue.60`, offset 2px; child paint button.flex-ff5rfy6.fg-f1sorag4: outline 2px solid rgb(0, 82, 255) offset 2px |
| pressed | size 392 x 56.84; border 1px solid rgba(75, 80, 90, 0.2); background transparent; transform scale(0.98); child paint button.flex-ff5rfy6.fg-f1sorag4: size 392.0x56.8; border 1px solid rgba(75, 80, 90, 0.2) |

![Passkey button default](components/crops/signin-passkey-default.png) ![Passkey button hover](components/crops/signin-passkey-hover.png) ![Passkey button focus-visible](components/crops/signin-passkey-focus-visible.png) ![Passkey button pressed](components/crops/signin-passkey-pressed.png)

### Footer

The site footer: link columns, social icons, the region selector and the legal row.

#### Footer
The site footer: link columns (Company/Individuals/Businesses/Institutions/Developers/Support), social icons, region selector and the legal row. Read as `footer` on the home page.

**Values (default).** size 1425 x 1230; background transparent; text CoinbaseIcons 64/64 400, #0052ff `color.blue.60`.

Child layers that carry the look: section 1425x1230 background #eef0f3 `color.gray.10`; div 1425x1230 background #eef0f3 `color.gray.10`; hr 1361x1 background rgba(91, 97, 110, 0.2) `color.role.bgLine`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A link in a footer link column. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 48.52 x 24; background transparent; text CoinbaseText 16/24 400, #5b616e `color.gray.60` |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.CDSFooterLink__Link-sc-9ac24f85-0.jAlaFt: size 48.5x24.0; outline 1px auto rgb(16, 16, 16) offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A footer social icon anchor (X/LinkedIn/Instagram). Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 16 x 27; background transparent; text CoinbaseText 18/27 400, #0a0b0d `color.gray.100` |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.CDSFooterLink__Link-sc-9ac24f85-0.jAlaFt: size 16.0x27.0; outline 1px auto rgb(16, 16, 16) offset 1px |

![Social link default](components/crops/footer-social-default.png) ![Social link hover](components/crops/footer-social-hover.png) ![Social link focus-visible](components/crops/footer-social-focus-visible.png) ![Social link pressed](components/crops/footer-social-pressed.png)

#### Region selector
The "Language and region" pair in the footer (Singapore / English selectors) — the enclosing control cluster. Read as `footer-region` on the home page.

**Values (default).** size 201.75 x 26; background transparent; text CoinbaseIcons 24/24 400, #5b616e `color.gray.60`.

Child layers that carry the look: button 26x26 background rgba(255, 255, 255, 0) `color.role.transparent` border 1px solid rgba(255, 255, 255, 0) `color.role.transparent`; button 83.1x26 background rgba(255, 255, 255, 0) `color.role.transparent` border 1px solid rgba(255, 255, 255, 0) `color.role.transparent`; button 61.4x26 background rgba(255, 255, 255, 0) `color.role.transparent` border 1px solid rgba(255, 255, 255, 0) `color.role.transparent`.

![Region selector default](components/crops/footer-region-default.png)

### Mobile (390 wide)

The same surface at phone width: the collapsed bar and the open menu overlay.

#### Mobile bar
The 390 mobile nav bar (data-testid=mobile-nav): logo, search, language and menu toggle. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 129; background transparent; shadow #ffffff 0px -1px 0px 1px; text CoinbaseSans 13/16 600, #0a0b0d `color.gray.100`.

![Mobile bar default](components/crops/m-header-default.png)

#### Menu button
The hamburger (data-testid=mobile-menu-toggle, aria-label "open navigation menu"); its own press opens the menu. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 44 x 47; radius 56px; background #eef0f3 `color.gray.10`; wrapper div.flex-ff5rfy6.MobileNav__StickyWrapper-sc-113ae5f-1: shadow #ffffff 0px -1px 0px 1px; text CoinbaseIcons 20/20 400, #0a0b0d `color.gray.100`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The menu overlay after the hamburger press. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 715; padding 32px 4px 0px 4px; background #ffffff `color.gray.0`; text CoinbaseSans 24/28 400, #0a0b0d `color.gray.100`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Menu link
A link/accordion row inside the open mobile menu. Read as `m-menu-link` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 382 x 56; padding 0px 16px; radius 16px; background transparent; text CoinbaseSans 24/28 400, #0a0b0d `color.gray.100`; transition background-color 0.2s ease-in-out |
| hover | background rgba(247, 247, 247, 0.88) `color.role.bgTertiaryHovered`; child paint a.GlobalNavLink__StyledLink-sc-1a5db85c-0.jJkJkH: size 382.0x56.0; background rgba(247, 247, 247, 0.88) `color.role.bgTertiaryHovered`; radius 16px |
| focus-visible | background rgba(247, 247, 247, 0.88) `color.role.bgTertiaryHovered`; outline 1px auto #e59700, offset 1px; child paint a.GlobalNavLink__StyledLink-sc-1a5db85c-0.jJkJkH: size 382.0x56.0; background rgba(247, 247, 247, 0.88) `color.role.bgTertiaryHovered`; radius 16px; outline 1px auto rgb(229, 151, 0) offset 1px |
| pressed | background rgba(247, 247, 247, 0.88) `color.role.bgTertiaryHovered`; child paint a.GlobalNavLink__StyledLink-sc-1a5db85c-0.jJkJkH: size 382.0x56.0; background rgba(247, 247, 247, 0.88) `color.role.bgTertiaryHovered`; radius 16px |

![Menu link default](components/crops/m-menu-link-default.png) ![Menu link hover](components/crops/m-menu-link-hover.png) ![Menu link focus-visible](components/crops/m-menu-link-focus-visible.png) ![Menu link pressed](components/crops/m-menu-link-pressed.png)

#### Mobile headline
The hero headline at 390. Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 358 x 156; background transparent; text CoinbaseDisplay 52/52 400, #0a0b0d `color.gray.100`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Coinbase's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **The product itself.** Coinbase's app — the exchange, wallet, portfolio and account settings — lives behind login.coinbase.com sign-in; the public login surface was measured but never submitted, and no trade or checkout was ever entered.
- **The app itself is a different surface.** The marketing site is a styled-components/CDS build; the exchange UI behind login.coinbase.com sign-in is not reachable signed out and is not claimed here. docs.cdp.coinbase.com (the developer docs) was not captured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

One theme: the whole public surface paints light. One dark island exists inside the theme — the home asset panel mounts `div.coinbase.dark` and redeclares the `--color-*` roles — but no second theme is offered; the promo row and footer band are the light scheme's bgAlternate grey.

### Fonts

- **The UI fonts** are webfonts the site ships (CoinbaseDisplay, CoinbaseSans, CoinbaseText, CoinbaseMono and CoinbaseCondensed via the --cds-font-* stacks; `fonts` in [raw/css-vars.json](raw/css-vars.json) holds the @font-face records); the font files themselves are not committed.
- Illustrations, photography, the app mockups and the wordmark in the screenshots are Coinbase's property; partner and logo marks are their owners' marks.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The hero artwork, app mockups and the Coinbase logo are Coinbase's content; only the frames and components were measured. Partner marks are their owners' artwork.
