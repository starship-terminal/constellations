# Deezer components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from deezer.com on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the login and signup forms were never sent; the plan and playback actions were never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (76 components, 198 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (194 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: the home hero paints `light`, every other surface paints `dark`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home (light hero) | `/en/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Offers | `/en/offers` | [default](screenshots/offers-dark-default.png), [full](screenshots/offers-dark-full.png) |
| Premium plan | `/en/offers/premium` | [default](screenshots/premium-dark-default.png), [full](screenshots/premium-dark-full.png) |
| Features | `/explore/features/` | [default](screenshots/features-dark-default.png), [full](screenshots/features-dark-full.png) |
| Download | `/explore/download/` | [default](screenshots/download-dark-default.png), [full](screenshots/download-dark-full.png) |
| Artist (app) | `/en/artist/27` | [default](screenshots/artist-dark-default.png), [full](screenshots/artist-dark-full.png), [menu](screenshots/artist-dark-menu.png) |
| Album (app) | `/en/album/302127` | [default](screenshots/album-dark-default.png), [full](screenshots/album-dark-full.png) |
| Playlist (app) | `/en/playlist/3155776842` | [default](screenshots/playlist-dark-default.png), [full](screenshots/playlist-dark-full.png) |
| Log in | `account.deezer.com/en/login/` | [default](screenshots/login-dark-default.png) |
| Sign up | `account.deezer.com/en/signup/` | [default](screenshots/signup-dark-default.png) |
| Artist, phone | `/en/artist/27` | [default](screenshots/mobile-artist-dark-default.png), [full](screenshots/mobile-artist-dark-full.png) |
| Home, phone | `/en/` | [default](screenshots/mobile-home-dark-default.png), [full](screenshots/mobile-home-dark-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| GDPR cookie modal | every page | hidden, never answered (no consent button was ever clicked) | hidden before every shot and reading |
| Track overflow popover | /en/artist/27 | the 'View menu' trigger's own toggle | [artist-dark-menu](screenshots/artist-dark-menu.png), [menu-popover](#overflow-popover), [menu-item](#overflow-menu-item) |
| Billing-period toggle | /en/offers | the Monthly/Annual options' own toggle | [billing-toggle](#billing-toggle), [toggle-option](#toggle-option) |
| Mobile nav overlay | artist page, phone width | the burger's own toggle | [m-drawer](#mobile-drawer) |
| Header search | /en/artist/27 | typed into then cleared — typing navigates to /search/<q> | [a-search](#search-field) |
| Signed-in product | a Deezer account | every post-login surface needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 34 components were given a real keyboard focus. 17 draw an outline ring: `a-nav-home` (2px solid #ad47ff `color.tempo.darkPrimary.100`, offset -2px), `a-nav-explore` (2px solid #ad47ff `color.tempo.darkPrimary.100`, offset -2px), `a-create-playlist` (2px solid #ad47ff `color.tempo.darkPrimary.100`, offset 0px), `mix-btn` (2px solid #f5f2f8 `color.tempo.neutralPrimary.10`, offset 0px), `fav-btn` (2px solid #ad47ff `color.tempo.darkPrimary.100`, offset 0px), `menu-btn` (2px solid #ad47ff `color.tempo.darkPrimary.100`, offset 0px), `track-row` (on a child: 2px solid rgb(245, 242, 248) offset 0px), `track-play` (2px solid #f5f2f8 `color.tempo.neutralPrimary.10`, offset 0px), `track-fav` (2px solid #ad47ff `color.tempo.darkPrimary.100`, offset 0px), `player-play` (2px solid #f5f2f8 `color.tempo.neutralPrimary.10`, offset 0px), `player-next` (2px solid #ad47ff `color.tempo.darkPrimary.100`, offset 0px), `player-shuffle` (2px solid #ad47ff `color.tempo.darkPrimary.100`, offset 0px), `player-more` (2px solid #ad47ff `color.tempo.darkPrimary.100`, offset 0px), `album-play` (2px solid #f5f2f8 `color.tempo.neutralPrimary.10`, offset 0px), `login-submit` (2px solid #f5f2f8 `color.tempo.neutralPrimary.10`, offset 0px), `login-forgot` (1px auto #ad47ff `color.tempo.darkPrimary.100`, offset 1px), `social-btn` (1px solid #ad47ff `color.tempo.darkPrimary.100`, offset 0px). 1 draw a focus ring as a shadow instead: `tab-item`. 1 change only their border: `a-login`. The other 15 show no measured change: `a-plans-link`, `a-signup`, `view-all`, `playlist-card`, `banner-cta`, `mkt-nav-link`, `mkt-login`, `mkt-signup`, `hero-cta`, `toggle-option`, `plan-cta`, `learn-more`, `m-signup`, `login-show-password`, `login-signup`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0, 0, 0.2, 1)` | background-color, border-color, box-shadow, color, fill, opacity, outline-color, stroke, transform | a-logo, a-nav-explore, a-nav-home, a-plans-link, player-track |
| 0.2s | `ease` | background-color, border-color, box-shadow, color, fill, opacity, outline-color, stroke, transform | a-create-playlist, a-login, a-search, a-signup, album-play, banner-cta, fav-btn, hero-cta and more |
| 0.5s | `cubic-bezier(0.77, 0, 0.175, 1)` | padding-bottom | a-sidebar |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 600 x 258 | - | - | transparent | none | 0 |
| [Playlist promo card](#playlist-promo-card) | 203 x 188.69 | - | 8px | #242326 `color.tempo.neutralPrimary.180` | none | 16px |
| [Playlist card](#playlist-card) | 240 x 48 | - | - | transparent | none | 0 |
| [Overflow popover](#overflow-popover) | 308.36 x 208.14 | - | 24px | #141216 `color.tempo.neutralPrimary.190` | rgba(0, 0, 0, 0.4) 0px 0px 25px 10px, rgba(0, 0, 0, 0.04) 0px 10px 10px -5px | 0 |
| [Signup banner](#signup-banner) | 1440 x 80 | - | - | #ead1ff | none | 16px |
| [App sidebar](#app-sidebar) | 243 x 900 | - | - | #141216 `color.tempo.neutralPrimary.190` | none | 0px 0px 80px 0px |

## Components

### App shell and navigation

The dark Chakra-UI shell on the signed-out catalog pages: the 243px sidebar rail with wordmark, Home/Explore and the playlist promo card, the header search, Plans/Log-in/Sign-up actions.

#### App sidebar
The left rail: DEEZER wordmark, Home/Explore, the Playlists promo card with Create-a-playlist. Read as `a-sidebar` on the artist page.

**Values (default).** size 243 x 900; padding 0px 0px 80px 0px; background #141216 `color.tempo.neutralPrimary.190`; text Inter 15/18.75 550, #ffffff `color.tempo.gray.50`; transition padding-bottom 0.5s cubic-bezier(0.77, 0, 0.175, 1).

![App sidebar default](components/crops/a-sidebar-default.png)

#### Sidebar logo
The DEEZER wordmark at the top of the rail. Read as `a-logo` on the artist page.

**Values (default).** size 127 x 32; background transparent; outline 2px solid transparent, offset 2px; text Inter 16/21.32 400, #ffffff `color.tempo.gray.50`; transition background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1); layers a.chakra-link.css-2yr2kp 127.0x32.0 2px solid rgba(0, 0, 0, 0) offset 2px.

Child layers that carry the look: a 127x32.

![Sidebar logo default](components/crops/a-logo-default.png)

#### Sidebar link
The "Home" nav item (icon + label); measured, never followed. Read as `a-nav-home` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 227 x 40; padding 8px 12px; radius 16px; background transparent; outline 2px solid transparent, offset 2px; text Inter 15/18.75 550, #ffffff `color.tempo.gray.50`; transition background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1); icon 24 x 24, #a19fa4 `color.tempo.neutralPrimary.70`; layers a.chakra-link.css-qiubdp 227.0x40.0 2px solid rgba(0, 0, 0, 0) offset 2px 16px |
| hover | background #242326 `color.tempo.neutralPrimary.180`; icon 24 x 24, #f5f2f8 `color.tempo.neutralPrimary.10`; layers none |
| focus-visible | outline 2px solid #ad47ff `color.tempo.darkPrimary.100`, offset -2px; layers a.chakra-link.css-qiubdp 227.0x40.0 2px solid rgb(173, 71, 255) offset -2px 16px |
| pressed | background #2e2c30 `color.tempo.gray.800`; outline none; layers none |

Child layers that carry the look: a 227x40 radius 16px.

![Sidebar link default](components/crops/a-nav-home-default.png) ![Sidebar link hover](components/crops/a-nav-home-hover.png) ![Sidebar link focus-visible](components/crops/a-nav-home-focus-visible.png) ![Sidebar link pressed](components/crops/a-nav-home-pressed.png)

#### Sidebar link 2
The "Explore" nav item; measured, never followed. Read as `a-nav-explore` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 227 x 40; padding 8px 12px; radius 16px; background transparent; outline 2px solid transparent, offset 2px; text Inter 15/18.75 550, #ffffff `color.tempo.gray.50`; transition background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1); icon 24 x 24, #a19fa4 `color.tempo.neutralPrimary.70`; layers a.chakra-link.css-qiubdp 227.0x40.0 2px solid rgba(0, 0, 0, 0) offset 2px 16px |
| hover | background #242326 `color.tempo.neutralPrimary.180`; icon 24 x 24, #f5f2f8 `color.tempo.neutralPrimary.10`; layers none |
| focus-visible | outline 2px solid #ad47ff `color.tempo.darkPrimary.100`, offset -2px; layers a.chakra-link.css-qiubdp 227.0x40.0 2px solid rgb(173, 71, 255) offset -2px 16px |
| pressed | background #2e2c30 `color.tempo.gray.800`; outline none; layers none |

Child layers that carry the look: a 227x40 radius 16px.

![Sidebar link 2 default](components/crops/a-nav-explore-default.png) ![Sidebar link 2 hover](components/crops/a-nav-explore-hover.png) ![Sidebar link 2 focus-visible](components/crops/a-nav-explore-focus-visible.png) ![Sidebar link 2 pressed](components/crops/a-nav-explore-pressed.png)

#### Playlist promo card
The sidebar "Create your first playlist" card — an upsell/empty-state nudge. Read as `a-playlist-promo` on the artist page.

**Values (default).** size 203 x 188.69; padding 16px; radius 8px; background #242326 `color.tempo.neutralPrimary.180`; text Inter 15/22.5 550, #ffffff `color.tempo.gray.50`.

![Playlist promo card default](components/crops/a-playlist-promo-default.png)

#### Create playlist button
The promo card's white "Create a playlist" action; measured, never clicked (it would need an account). Read as `a-create-playlist` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 141 x 32; padding 4px 16px; radius 12px; background #ffffff `color.tempo.gray.50`; outline 2px solid transparent, offset 0px; text Inter 13/18.57 550, #000000 `color.tempo.gray.900`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease |
| hover | background #f5f2f8 `color.tempo.neutralPrimary.10`; text Inter 13/18.57 550, #141216 `color.tempo.neutralPrimary.190` |
| focus-visible | outline 2px solid #ad47ff `color.tempo.darkPrimary.100`, offset 0px |
| pressed | background #e2dfe6 `color.tempo.gray.100`; text Inter 13/18.57 550, #242326 `color.tempo.neutralPrimary.180` |

![Create playlist button default](components/crops/a-create-playlist-default.png) ![Create playlist button hover](components/crops/a-create-playlist-hover.png) ![Create playlist button focus-visible](components/crops/a-create-playlist-focus-visible.png) ![Create playlist button pressed](components/crops/a-create-playlist-pressed.png)

#### Search field
The "Artists, tracks, podcasts..." header search; focused and typed into then cleared — never submitted. Typing into it navigates to a search-results page, which is why it is measured last here. Read as `a-search` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 375 x 48; padding 0px 44px; border 2px solid transparent; radius 16px; background #242326 `color.tempo.neutralPrimary.180`; outline 2px solid transparent, offset -2px; text Inter 15/22.5 450, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; placeholder #706e73 `color.tempo.neutralPrimary.110` |
| focused, filled | border 2px solid #ad47ff `color.tempo.darkPrimary.100`; background #2e2c30 `color.tempo.gray.800`; text Inter 15/22.5 450, #f5f2f8 `color.tempo.neutralPrimary.10` |

![Search field default](components/crops/a-search-default.png) ![Search field focused](components/crops/a-search-focused.png) ![Search field filled](components/crops/a-search-filled.png)

#### Plans link
The header "Plans" link to /en/offers; measured, never followed. Read as `a-plans-link` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 43 x 21.31; background transparent; outline 2px solid transparent, offset 2px; text Inter 16/21.32 700, #ffffff `color.tempo.gray.50`; transition background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1); layers a.chakra-link.css-rwg70c 43.0x21.3 2px solid rgba(0, 0, 0, 0) offset 2px |
| focus-visible | outline none; layers none |
| pressed | outline none; text Inter 16/21.32 700, #bb73ff `color.tempo.darkPrimary.90`; layers none |

Child layers that carry the look: a 43x21.3.

![Plans link default](components/crops/a-plans-link-default.png) ![Plans link hover](components/crops/a-plans-link-hover.png) ![Plans link focus-visible](components/crops/a-plans-link-focus-visible.png) ![Plans link pressed](components/crops/a-plans-link-pressed.png)

#### Log in button (app)
The dark-outline Log-in pill in the app header; links to account.deezer.com, measured never followed. Read as `a-login` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 73 x 32; padding 4px 16px; border 1px solid #4e4c51 `color.tempo.gray.700`; radius 12px; background transparent; outline 1px solid transparent, offset 0px; text Inter 13/18.57 550, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease |
| hover | border 1px solid #59575c `color.tempo.neutralPrimary.130`; background #2e2c30 `color.tempo.gray.800`; text Inter 13/18.57 550, #f5f2f8 `color.tempo.neutralPrimary.10` |
| focus-visible | border 1px solid #ad47ff `color.tempo.darkPrimary.100`; outline none |
| pressed | border 1px solid #656367 `color.tempo.gray.600`; background #38373b `color.tempo.neutralPrimary.160`; outline none; text Inter 13/18.57 550, #e2dfe6 `color.tempo.gray.100` |

![Log in button (app) default](components/crops/a-login-default.png) ![Log in button (app) hover](components/crops/a-login-hover.png) ![Log in button (app) focus-visible](components/crops/a-login-focus-visible.png) ![Log in button (app) pressed](components/crops/a-login-pressed.png)

#### Sign up button (app)
The purple Sign-up pill in the app header; measured never followed. Read as `a-signup` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 81 x 32; padding 4px 16px; radius 12px; background #ad47ff `color.tempo.darkPrimary.100`; outline 2px solid transparent, offset 0px; text Inter 13/18.57 550, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease |
| hover | background #bb73ff `color.tempo.darkPrimary.90`; text Inter 13/18.57 550, #f5f2f8 `color.tempo.neutralPrimary.10` |
| focus-visible | outline none |
| pressed | background #ca97ff `color.tempo.darkPrimary.80`; outline none; text Inter 13/18.57 550, #e2dfe6 `color.tempo.gray.100` |

![Sign up button (app) default](components/crops/a-signup-default.png) ![Sign up button (app) hover](components/crops/a-signup-hover.png) ![Sign up button (app) focus-visible](components/crops/a-signup-focus-visible.png) ![Sign up button (app) pressed](components/crops/a-signup-pressed.png)

#### Marketing header
The dark top bar over the light hero: wordmark, Plans/Features/Music, Log in and the purple Sign up pill. Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 80; padding 0px 112px; border B: 1px solid #555257; background transparent; text Inter 16/normal 700, #fdfcfe; layers nav.tempo-topbar 1440.0x80.0 B:1px solid rgb(85, 82, 87); a.topbar-action.tempo-btn 84.0x37.0 T:1px solid rgb(85, 82, 87) / R:1px solid rgb(85, 82, 87) / B:1px solid rgb(85, 82, 87) / L:1px solid rgb(85, 82, 87) 12px; a.topbar-action.tempo-btn 95.0x37.0 rgb(162, 56, 255) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 12px; .

Child layers that carry the look: nav 1440x80 border 1px solid #555257; a 84x37 border 1px solid #555257 radius 12px; a 95x37 background #a238ff `color.tempo.lightPrimary.100` border 1px solid transparent radius 12px.

![Marketing header default](components/crops/mkt-header-default.png)

#### Logo
The Deezer heart-and-wordmark in the header. Read as `mkt-logo` on the home page.

**Values (default).** size 106.66 x 30; background transparent; text Inter 16/normal 400, #fdfcfe.

![Logo default](components/crops/mkt-logo-default.png)

#### Nav link
A marketing header link (Plans/Features/Music); measured, never followed. Read as `mkt-nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 43 x 20; background transparent; text Inter 16/normal 700, #fdfcfe |
| hover, pressed | text Inter 16/normal 700, #a238ff `color.tempo.lightPrimary.100` |

![Nav link default](components/crops/mkt-nav-link-default.png) ![Nav link hover](components/crops/mkt-nav-link-hover.png) ![Nav link focus-visible](components/crops/mkt-nav-link-focus-visible.png) ![Nav link pressed](components/crops/mkt-nav-link-pressed.png)

#### Log in button
The dark-outline Log-in pill; links to account.deezer.com, measured never followed. Read as `mkt-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 84 x 37; padding 9px 20px; border 1px solid #555257; radius 12px; background transparent; text Inter 14/normal 700, #fdfcfe; transition background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, transform 0.2s ease |
| hover | background #29282d |
| pressed | size 79.8 x 35.15; background #29282d; transform scale(0.95) |

![Log in button default](components/crops/mkt-login-default.png) ![Log in button hover](components/crops/mkt-login-hover.png) ![Log in button focus-visible](components/crops/mkt-login-focus-visible.png) ![Log in button pressed](components/crops/mkt-login-pressed.png)

#### Sign up button
The purple Sign-up pill in the header; measured never followed. Read as `mkt-signup` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 95 x 37; padding 9px 20px; border 1px solid transparent; radius 12px; background #a238ff `color.tempo.lightPrimary.100`; text Inter 14/normal 700, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, transform 0.2s ease |
| hover | background #9333e8 |
| pressed | size 90.25 x 35.15; background #9333e8; transform scale(0.95) |

![Sign up button default](components/crops/mkt-signup-default.png) ![Sign up button hover](components/crops/mkt-signup-hover.png) ![Sign up button focus-visible](components/crops/mkt-signup-focus-visible.png) ![Sign up button pressed](components/crops/mkt-signup-pressed.png)

### Home (light)

The light home hero: the 140px Deezer Brand display, the Try-for-free pill, the five-star ratings line, section headings.

#### Hero headline
"WHERE MUSIC COMES TO LIFE" — the condensed display headline on the light hero. Read as `hero-h1` on the home page.

**Values (default).** size 900 x 378; background transparent; text Deezer Brand 140/126 800, #0f0d13.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero sub
"Music streaming by Deezer" under the headline. Read as `hero-sub` on the home page.

**Values (default).** size 1384 x 56; padding 0px 0px 14px 0px; background transparent; text Deezer Brand 35/42 700, #0f0d13.

![Hero sub default](components/crops/hero-sub-default.png)

#### Hero CTA
The purple "Try for free" pill under the hero copy; measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 162 x 42; padding 8px 32px; border 1px solid transparent; radius 16px; background #a238ff `color.tempo.lightPrimary.100`; text Inter 16/normal 700, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, transform 0.2s ease |
| hover | background #9333e8 |
| pressed | size 153.9 x 39.9; background #9333e8; transform scale(0.95) |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Rating line
The five-star "Over 3 million 5-star ratings" strip under the hero. Read as `rating` on the home page.

**Values (default).** size 380 x 25; background transparent; text Inter 16/25 400, #0f0d13.

![Rating line default](components/crops/rating-default.png)

#### Section heading
A marketing section heading further down the home page. Read as `section-h2` on the home page.

**Values (default).** size 880 x 150; padding 0px 28px 28px 28px; background transparent; text Deezer Brand 56/normal 700, #fdfcfe.

![Section heading default](components/crops/section-h2-default.png)

### Offers (dark marketing)

The dark /en/offers surface: the 78px headline, the Monthly/Annual billing toggle and the white plan cards with their dark Try-for-free actions.

#### Offers headline
"Get 1 month of Premium free" — the display heading on the dark offers page. Read as `offers-h1` on the offers page.

**Values (default).** size 860.75 x 85; background transparent; text Deezer Product 78/normal 700, #fdfcfe.

![Offers headline default](components/crops/offers-h1-default.png)

#### Region notice
The "Deezer Free is not available in your country" notice card — an info/alert surface. Read as `notice` on the offers page.

Not on the page when it was captured.

#### Billing toggle
The Monthly/Annual segmented control over the plan cards; toggled, never checked out. Read as `billing-toggle` on the offers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 180 x 40; padding 4px; radius 256px; background #29282d; text Inter 14/20 600, #000000 `color.tempo.gray.900` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Billing toggle default](components/crops/billing-toggle-default.png) ![Billing toggle hover](components/crops/billing-toggle-hover.png) ![Billing toggle pressed](components/crops/billing-toggle-pressed.png)

#### Toggle option
The "Annual" option inside the billing toggle; clicked open for the annual shot, never checked out. Read as `toggle-option` on the offers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 82 x 32; padding 4px 16px; radius 8px; background transparent; text Inter 14/20 600, #a9a6aa; layers ::after rgb(248, 248, 249) 0px none 0; li::after 82pxx32px rgb(248, 248, 249) 256px |

Child layers that carry the look: li::after 82pxx32px background #f8f8f9 radius 256px.

![Toggle option default](components/crops/toggle-option-default.png) ![Toggle option focus-visible](components/crops/toggle-option-focus-visible.png)

#### Plan card
A white plan card (PREMIUM) on the purple band: title chip, account count, free month, price, Try-for-free CTA and Learn more. Read as `plan-card` on the offers page.

**Values (default).** size 600 x 258; background transparent; text Deezer Product 24/24 700, #ffffff `color.tempo.gray.50`; layers div.unlogged-card 600.0x258.0 rgb(253, 252, 254) 4px; h2.unlogged-card-title 98.0x32.0 rgb(162, 56, 255) 9px / 75%; span.unlogged-card-tag 84.0x25.6 rgb(235, 231, 238) 4px; a.tempo-btn.tempo-btn-l 552.0x54.0 rgb(18, 18, 22) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 16px.

Child layers that carry the look: div 600x258 background #fdfcfe radius 4px; h2 98x32 background #a238ff `color.tempo.lightPrimary.100` radius 9px / 75%; span 84x25.6 background #ebe7ee radius 4px.

![Plan card default](components/crops/plan-card-default.png)

#### Plan name chip
The purple "PREMIUM" chip on the plan card. Read as `plan-title` on the offers page.

**Values (default).** size 98 x 32; padding 4px 8px; radius 9px 75%; background #a238ff `color.tempo.lightPrimary.100`; text Deezer Product 24/24 700, #ffffff `color.tempo.gray.50`.

![Plan name chip default](components/crops/plan-title-default.png)

#### Plan price line
"1 month free / then US$11.99/month" on the card. Read as `plan-price` on the offers page.

**Values (default).** size 171 x 56; background transparent; text Inter 20/24 700, #0f0d13.

![Plan price line default](components/crops/plan-price-default.png)

#### Plan CTA
The black "Try for free" action on the plan card — links to payment/go.php; measured never followed. Read as `plan-cta` on the offers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 552 x 54; padding 12px 32px; border 1px solid transparent; radius 16px; background #121216; text Inter 16/normal 700, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, transform 0.2s ease |
| hover | background #32323d |
| pressed | size 524.4 x 51.3; background #32323d; transform scale(0.95) |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Learn more link
The underlined caption link inside the plan card; measured never followed. Read as `learn-more` on the offers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 171 x 24; background transparent; text Inter 20/24 700, #0f0d13 |

![Learn more link default](components/crops/learn-more-default.png) ![Learn more link hover](components/crops/learn-more-hover.png) ![Learn more link focus-visible](components/crops/learn-more-focus-visible.png) ![Learn more link pressed](components/crops/learn-more-pressed.png)

### Artist page (dark app)

The public artist page: avatar, display name and fan count, the Mix/favourite/overflow actions, the Discography tab strip, the Top-tracks rows and the Playlists aside cards.

#### Artist image
The artist's round photo in the page header (the first large chakra-image on the page). Read as `artist-avatar` on the artist page.

**Values (default).** size 278 x 278; background transparent; text Inter 16/21.32 400, #ffffff `color.tempo.gray.50`.

![Artist image default](components/crops/artist-avatar-default.png)

#### Artist name
The artist's display name heading. Read as `artist-name` on the artist page.

**Values (default).** size 644 x 64; padding 8px 0px 0px 0px; background transparent; text Deezer Headline VF 56/56 640, #ffffff `color.tempo.gray.50`.

![Artist name default](components/crops/artist-name-default.png)

#### Fan count
The "5,237,122 fans" muted count under the name. Read as `artist-fans` on the artist page.

**Values (default).** size 144 x 18.56; background transparent; text Inter 13/18.57 450, #a19fa4 `color.tempo.neutralPrimary.70`.

![Fan count default](components/crops/artist-fans-default.png)

#### Mix button
The purple "▶ Mix" primary action; measured, never pressed (it would start playback and, signed out, a paywall). Read as `mix-btn` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 95 x 48; padding 12px 24px 12px 16px; radius 16px; background #ad47ff `color.tempo.darkPrimary.100`; outline 2px solid transparent, offset 0px; text Inter 15/22.5 550, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; icon 24 x 24, #ffffff `color.tempo.gray.50` |
| hover | background #bb73ff `color.tempo.darkPrimary.90`; text Inter 15/22.5 550, #f5f2f8 `color.tempo.neutralPrimary.10`; icon 24 x 24, #f5f2f8 `color.tempo.neutralPrimary.10` |
| focus-visible | outline 2px solid #f5f2f8 `color.tempo.neutralPrimary.10`, offset 0px |
| pressed | background #ca97ff `color.tempo.darkPrimary.80`; text Inter 15/22.5 550, #e2dfe6 `color.tempo.gray.100`; icon 24 x 24, #e2dfe6 `color.tempo.gray.100` |

![Mix button default](components/crops/mix-btn-default.png) ![Mix button hover](components/crops/mix-btn-hover.png) ![Mix button focus-visible](components/crops/mix-btn-focus-visible.png) ![Mix button pressed](components/crops/mix-btn-pressed.png)

#### Favourite icon button
The heart "Add" icon button beside Mix; measured, never toggled (it needs an account). Read as `fav-btn` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 48 x 48; radius 256px; background transparent; outline 2px solid transparent, offset 0px; text Inter 15/22.5 550, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; icon 24 x 24, #ffffff `color.tempo.gray.50`; layers button.chakra-button.css-15ctxfi 48.0x48.0 2px solid rgba(0, 0, 0, 0) offset 0px 256px |
| hover | background #2e2c30 `color.tempo.gray.800`; text Inter 15/22.5 550, #f5f2f8 `color.tempo.neutralPrimary.10`; icon 24 x 24, #f5f2f8 `color.tempo.neutralPrimary.10`; layers none |
| focus-visible | outline 2px solid #ad47ff `color.tempo.darkPrimary.100`, offset 0px; layers button.chakra-button.css-15ctxfi 48.0x48.0 2px solid rgb(173, 71, 255) offset 0px 256px |
| pressed | background #38373b `color.tempo.neutralPrimary.160`; text Inter 15/22.5 550, #e2dfe6 `color.tempo.gray.100`; icon 24 x 24, #e2dfe6 `color.tempo.gray.100`; layers none |

Child layers that carry the look: button 48x48 radius 256px.

![Favourite icon button default](components/crops/fav-btn-default.png) ![Favourite icon button hover](components/crops/fav-btn-hover.png) ![Favourite icon button focus-visible](components/crops/fav-btn-focus-visible.png) ![Favourite icon button pressed](components/crops/fav-btn-pressed.png)

#### Track overflow button
The "..." ("View menu") icon button — a Chakra popover trigger; the opened state was measured after clicking it, its items never followed. Read as `menu-btn` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 48 x 48; radius 256px; background transparent; outline 2px solid transparent, offset 0px; text Inter 15/22.5 550, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; icon 24 x 24, #ffffff `color.tempo.gray.50`; layers button.chakra-button.popper-wrapper 48.0x48.0 2px solid rgba(0, 0, 0, 0) offset 0px 256px |
| hover | background #2e2c30 `color.tempo.gray.800`; text Inter 15/22.5 550, #f5f2f8 `color.tempo.neutralPrimary.10`; icon 24 x 24, #f5f2f8 `color.tempo.neutralPrimary.10`; layers none |
| focus-visible | outline 2px solid #ad47ff `color.tempo.darkPrimary.100`, offset 0px; layers button.chakra-button.popper-wrapper 48.0x48.0 2px solid rgb(173, 71, 255) offset 0px 256px |
| pressed | background #38373b `color.tempo.neutralPrimary.160`; text Inter 15/22.5 550, #e2dfe6 `color.tempo.gray.100`; icon 24 x 24, #e2dfe6 `color.tempo.gray.100`; layers none |
| opened | background #2e2c30 `color.tempo.gray.800`; text Inter 15/22.5 550, #f5f2f8 `color.tempo.neutralPrimary.10`; icon 24 x 24, #f5f2f8 `color.tempo.neutralPrimary.10`; layers none |

Child layers that carry the look: button 48x48 radius 256px.

![Track overflow button default](components/crops/menu-btn-default.png) ![Track overflow button hover](components/crops/menu-btn-hover.png) ![Track overflow button focus-visible](components/crops/menu-btn-focus-visible.png) ![Track overflow button pressed](components/crops/menu-btn-pressed.png) ![Track overflow button opened](components/crops/menu-btn-opened.png)

#### Overflow popover
The track overflow menu opened by its own trigger (a Chakra popper panel); its items were never followed. Read as `menu-popover` on the artist page.

**Values (default).** size 308.36 x 208.14; radius 24px; background #141216 `color.tempo.neutralPrimary.190`; shadow rgba(0, 0, 0, 0.4) 0px 0px 25px 10px, rgba(0, 0, 0, 0.04) 0px 10px 10px -5px; text Inter 13/18.57 450, #ffffff `color.tempo.gray.50`; transform scale(0.963613); opacity 0.258889; icon 23.13 x 23.13, #ffffff `color.tempo.gray.50`.

![Overflow popover default](components/crops/menu-popover-default.png)

#### Overflow menu item
An item inside the opened overflow popover; measured, never followed. Read as `menu-item` on the artist page.

**Values (default).** size 313.16 x 39.15; padding 0px 8px; background transparent; text Inter 13/18.57 450, #ffffff `color.tempo.gray.50`; icon 23.49 x 23.49, #ffffff `color.tempo.gray.50`; layers button.chakra-stack.css-kcvewa 297.5x39.1 rgb(20, 18, 22) 16px.

Child layers that carry the look: button 297.5x39.1 background #141216 `color.tempo.neutralPrimary.190` radius 16px.

![Overflow menu item default](components/crops/menu-item-default.png)

#### Tab strip
The Discography/Top-tracks/Similar-artists/Playlists/Bio tab bar under the artist header. Read as `tabs-nav` on the artist page.

**Values (default).** size 1117 x 43; border B: 1px solid #4e4c51 `color.tempo.gray.700`; background transparent; shadow rgba(25, 25, 34, 0.16) 0px 2px 6px -4px; text Inter 15/27 600, #ffffff `color.tempo.gray.50`; layers nav.navbar 1117.0x43.0 B:1px solid rgb(78, 76, 81) rgba(25, 25, 34, 0.16) 0px 2px 6px -4px; a.chakra-text.navbar-link 96.0x42.0 B:3px solid rgb(173, 71, 255); a.chakra-text.navbar-link 83.0x42.0 B:3px solid rgba(0, 0, 0, 0); a.chakra-text.navbar-link 106.0x42.0 B:3px solid rgba(0, 0, 0, 0); a.chakra-text.navbar-link 65.0x42.0 B:3px solid rgba(0, 0, 0, 0); a.chakra-text.navbar-link 24.0x42.0 B:3px .

![Tab strip default](components/crops/tabs-nav-default.png)

#### Tab item
The selected "Discography" tab (a real link with an underline indicator); measured, never followed. Read as `tab-item` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 96 x 42; padding 0px 0px 12px 0px; border B: 3px solid #ad47ff `color.tempo.darkPrimary.100`; background transparent; text Inter 15/27 600, #ffffff `color.tempo.gray.50`; layers a.chakra-text.navbar-link 96.0x42.0 B:3px solid rgb(173, 71, 255) |
| hover | border B: 3px solid #bb73ff `color.tempo.darkPrimary.90`; text Inter 15/27 600, #f5f2f8 `color.tempo.neutralPrimary.10`; layers a.chakra-text.navbar-link 96.0x42.0 B:3px solid rgb(187, 115, 255) |
| focus-visible | shadow #ad47ff 0px -1px 0px 0px inset; layers a.chakra-text.navbar-link 96.0x42.0 B:3px solid rgb(173, 71, 255) rgb(173, 71, 255) 0px -1px 0px 0px inset |
| pressed | border B: 3px solid #bb73ff `color.tempo.darkPrimary.90`; text Inter 15/27 600, #f5f2f8 `color.tempo.neutralPrimary.10`; layers a.chakra-text.navbar-link 96.0x42.0 B:3px solid rgb(187, 115, 255) |

Child layers that carry the look: a 96x42 border 3px solid #ad47ff `color.tempo.darkPrimary.100`.

![Tab item default](components/crops/tab-item-default.png) ![Tab item hover](components/crops/tab-item-hover.png) ![Tab item focus-visible](components/crops/tab-item-focus-visible.png) ![Tab item pressed](components/crops/tab-item-pressed.png)

#### Track list
The "Top tracks" numbered list under the tab bar. Read as `track-list` on the artist page.

**Values (default).** size 789 x 224; background transparent; text Inter 15/18.75 550, #bb73ff `color.tempo.darkPrimary.90`; icon 24 x 24, #ffffff `color.tempo.gray.50`; layers div.css-1f88yyt 40.0x40.0 T:1px solid rgba(0, 0, 0, 0.12) / R:1px solid rgba(0, 0, 0, 0.12) / B:1px solid rgba(0, 0, 0, 0.12) / L:1px solid rgba(0, 0, 0, 0.12) 8px; button.chakra-button.css-3yg119 32.0x32.0 rgb(173, 71, 255) 2px solid rgba(0, 0, 0, 0) offset 0px 256px; button.chakra-button.css-5xmo61 32.0x32.0 2px solid rgba(0, 0, 0, 0) offset 0px 256px; button.chakra-button.popper-wrapper 32.0x32.

Child layers that carry the look: div 40x40 border 1px solid rgba(0, 0, 0, 0.12) radius 8px; button 32x32 background #ad47ff `color.tempo.darkPrimary.100` radius 256px; button 32x32 radius 256px.

![Track list default](components/crops/track-list-default.png)

#### Track row
A numbered track row (play button, title, heart, "...") in Top tracks. Read as `track-row` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 789 x 56; background transparent; text Inter 15/18.75 550, #bb73ff `color.tempo.darkPrimary.90`; icon 24 x 24, #ffffff `color.tempo.gray.50`; layers div.css-1f88yyt 40.0x40.0 T:1px solid rgba(0, 0, 0, 0.12) / R:1px solid rgba(0, 0, 0, 0.12) / B:1px solid rgba(0, 0, 0, 0.12) / L:1px solid rgba(0, 0, 0, 0.12) 8px; button.chakra-button.css-3yg119 32.0x32.0 rgb(173, 71, 255) 2px solid rgba(0, 0, 0, 0) offset 0px 256px; button.chakra-button.css-5xmo61 32.0x32.0 2px solid rgba(0, 0, 0, 0) offset 0px 256px; button.chakra-button.popper-wrapper 32.0x32 |
| hover | layers div.JIYRe.Fp81z 789.0x56.0 rgb(20, 18, 22) 16px; div.css-1f88yyt 40.0x40.0 T:1px solid rgba(0, 0, 0, 0.12) / R:1px solid rgba(0, 0, 0, 0.12) / B:1px solid rgba(0, 0, 0, 0.12) / L:1px solid rgba(0, 0, 0, 0.12) 8px; button.chakra-button.css-3yg119 32.0x32.0 rgb(173, 71, 255) 2px solid rgba(0, 0, 0, 0) offset 0px 256px; button.chakra-button.css-5xmo61 32.0x32.0 2px solid rgba(0, 0, 0, 0) offset 0px 2 |
| focus-visible | layers div.css-1f88yyt 40.0x40.0 T:1px solid rgba(0, 0, 0, 0.12) / R:1px solid rgba(0, 0, 0, 0.12) / B:1px solid rgba(0, 0, 0, 0.12) / L:1px solid rgba(0, 0, 0, 0.12) 8px; button.chakra-button.css-3yg119 32.0x32.0 rgb(173, 71, 255) 2px solid rgb(245, 242, 248) offset 0px 256px; button.chakra-button.css-5xmo61 32.0x32.0 2px solid rgba(0, 0, 0, 0) offset 0px 256px; button.chakra-button.popper-wrapper 32.0x |

Child layers that carry the look: div 40x40 border 1px solid rgba(0, 0, 0, 0.12) radius 8px; button 32x32 background #ad47ff `color.tempo.darkPrimary.100` radius 256px; button 32x32 radius 256px.

![Track row default](components/crops/track-row-default.png) ![Track row hover](components/crops/track-row-hover.png) ![Track row focus-visible](components/crops/track-row-focus-visible.png)

#### Track play button
A row's purple circular play button ("Play Instant Crush ..."); measured, never pressed. Read as `track-play` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 256px; background #ad47ff `color.tempo.darkPrimary.100`; outline 2px solid transparent, offset 0px; text Inter 13/18.57 550, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; icon 24 x 24, #ffffff `color.tempo.gray.50` |
| hover | background #bb73ff `color.tempo.darkPrimary.90`; text Inter 13/18.57 550, #f5f2f8 `color.tempo.neutralPrimary.10`; icon 24 x 24, #f5f2f8 `color.tempo.neutralPrimary.10` |
| focus-visible | outline 2px solid #f5f2f8 `color.tempo.neutralPrimary.10`, offset 0px |
| pressed | background #ca97ff `color.tempo.darkPrimary.80`; text Inter 13/18.57 550, #e2dfe6 `color.tempo.gray.100`; icon 24 x 24, #e2dfe6 `color.tempo.gray.100` |

![Track play button default](components/crops/track-play-default.png) ![Track play button hover](components/crops/track-play-hover.png) ![Track play button focus-visible](components/crops/track-play-focus-visible.png) ![Track play button pressed](components/crops/track-play-pressed.png)

#### Track favourite button
A row's heart icon button; measured, never toggled. Read as `track-fav` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 256px; background transparent; outline 2px solid transparent, offset 0px; text Inter 13/18.57 550, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; icon 24 x 24, #ffffff `color.tempo.gray.50`; layers button.chakra-button.css-5xmo61 32.0x32.0 2px solid rgba(0, 0, 0, 0) offset 0px 256px |
| hover | background #2e2c30 `color.tempo.gray.800`; text Inter 13/18.57 550, #f5f2f8 `color.tempo.neutralPrimary.10`; icon 24 x 24, #f5f2f8 `color.tempo.neutralPrimary.10`; layers none |
| focus-visible | outline 2px solid #ad47ff `color.tempo.darkPrimary.100`, offset 0px; layers button.chakra-button.css-5xmo61 32.0x32.0 2px solid rgb(173, 71, 255) offset 0px 256px |
| pressed | background #38373b `color.tempo.neutralPrimary.160`; text Inter 13/18.57 550, #e2dfe6 `color.tempo.gray.100`; icon 24 x 24, #e2dfe6 `color.tempo.gray.100`; layers none |

Child layers that carry the look: button 32x32 radius 256px.

![Track favourite button default](components/crops/track-fav-default.png) ![Track favourite button hover](components/crops/track-fav-hover.png) ![Track favourite button focus-visible](components/crops/track-fav-focus-visible.png) ![Track favourite button pressed](components/crops/track-fav-pressed.png)

#### View all button
The section's "View all" ghost action; measured, never followed. Read as `view-all` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 93 x 24; background transparent; text Inter 13/18.57 550, #ffffff `color.tempo.gray.50`; layers button.chakra-button.css-r7fpo3 85.0x32.0 T:1px solid rgb(78, 76, 81) / R:1px solid rgb(78, 76, 81) / B:1px solid rgb(78, 76, 81) / L:1px solid rgb(78, 76, 81) 1px solid rgba(0, 0, 0, 0) offset 0px 12px |
| hover | text Inter 13/18.57 550, #f5f2f8 `color.tempo.neutralPrimary.10`; layers button.chakra-button.css-r7fpo3 85.0x32.0 rgb(46, 44, 48) T:1px solid rgb(89, 87, 92) / R:1px solid rgb(89, 87, 92) / B:1px solid rgb(89, 87, 92) / L:1px solid rgb(89, 87, 92) 1px solid rgba(0, 0, 0, 0) offset 0px 12px |

Child layers that carry the look: button 85x32 border 1px solid #4e4c51 `color.tempo.gray.700` radius 12px.

![View all button default](components/crops/view-all-default.png) ![View all button hover](components/crops/view-all-hover.png) ![View all button focus-visible](components/crops/view-all-focus-visible.png) ![View all button pressed](components/crops/view-all-pressed.png)

#### Section heading (app)
A catalog section heading ("Top tracks"/"Playlists"). Read as `a-section-h2` on the artist page.

**Values (default).** size 240 x 24; background transparent; text Inter 20/24 700, #ffffff `color.tempo.gray.50`; icon 16 x 16, #ffffff `color.tempo.gray.50`; layers a.chakra-link.header-link 103.0x24.0 2px solid rgba(0, 0, 0, 0) offset 2px.

Child layers that carry the look: a 103x24.

![Section heading (app) default](components/crops/a-section-h2-default.png)

#### Playlist card
A "Playlists" aside card (cover, title, fan count, heart); measured, never followed. Read as `playlist-card` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 240 x 48; background transparent; text Inter 15/18.75 550, #ffffff `color.tempo.gray.50`; layers div.css-1f88yyt 48.0x48.0 T:1px solid rgba(0, 0, 0, 0.12) / R:1px solid rgba(0, 0, 0, 0.12) / B:1px solid rgba(0, 0, 0, 0.12) / L:1px solid rgba(0, 0, 0, 0.12) 8px; a.chakra-link.css-ttnijr 118.0x19.0 2px solid rgba(0, 0, 0, 0) offset 2px; button.chakra-button.popper-wrapper 0.0x0.0 2px solid rgba(0, 0, 0, 0) offset 0px 256px; button.chakra-button.css-5xmo61 32.0x32.0 2px solid rgba(0, 0, 0, 0) of |
| hover, pressed | icon 24 x 24, #ffffff `color.tempo.gray.50`; layers div.css-1f88yyt 48.0x48.0 T:1px solid rgba(0, 0, 0, 0.12) / R:1px solid rgba(0, 0, 0, 0.12) / B:1px solid rgba(0, 0, 0, 0.12) / L:1px solid rgba(0, 0, 0, 0.12) 8px; a.chakra-link.css-ttnijr 100.0x37.8 2px solid rgba(0, 0, 0, 0) offset 2px; button.chakra-button.popper-wrapper 32.0x32.0 2px solid rgba(0, 0, 0, 0) offset 0px 256px; button.chakra-button.css-5xmo61 32.0x32.0 2px solid rgba(0, 0, 0, 0)  |

Child layers that carry the look: div 48x48 border 1px solid rgba(0, 0, 0, 0.12) radius 8px; a 118x19; button 0x0 radius 256px.

![Playlist card default](components/crops/playlist-card-default.png) ![Playlist card hover](components/crops/playlist-card-hover.png) ![Playlist card focus-visible](components/crops/playlist-card-focus-visible.png) ![Playlist card pressed](components/crops/playlist-card-pressed.png)

#### Album cover
The album's square cover art in the page header (the first large chakra-image). Read as `album-cover` on the album page.

**Values (default).** size 278 x 278; background transparent; text Inter 16/21.32 400, #ffffff `color.tempo.gray.50`.

![Album cover default](components/crops/album-cover-default.png)

#### Album title
The album's title heading. Read as `album-title` on the album page.

**Values (default).** size 805 x 64; padding 8px 0px 0px 0px; background transparent; text Deezer Headline VF 56/56 640, #ffffff `color.tempo.gray.50`.

![Album title default](components/crops/album-title-default.png)

#### Track play button
The first track row's purple circular play button; measured, never pressed. Read as `album-play` on the album page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 256px; background #ad47ff `color.tempo.darkPrimary.100`; outline 2px solid transparent, offset 0px; text Inter 13/18.57 550, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; icon 24 x 24, #ffffff `color.tempo.gray.50` |
| hover | background #bb73ff `color.tempo.darkPrimary.90`; text Inter 13/18.57 550, #f5f2f8 `color.tempo.neutralPrimary.10`; icon 24 x 24, #f5f2f8 `color.tempo.neutralPrimary.10` |
| focus-visible | outline 2px solid #f5f2f8 `color.tempo.neutralPrimary.10`, offset 0px |
| pressed | background #ca97ff `color.tempo.darkPrimary.80`; text Inter 13/18.57 550, #e2dfe6 `color.tempo.gray.100`; icon 24 x 24, #e2dfe6 `color.tempo.gray.100` |

![Track play button default](components/crops/album-play-default.png) ![Track play button hover](components/crops/album-play-hover.png) ![Track play button focus-visible](components/crops/album-play-focus-visible.png) ![Track play button pressed](components/crops/album-play-pressed.png)

#### Album track row
A numbered track row on the album page. Read as `album-track-row` on the album page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1117 x 56; background transparent; text Inter 15/18.75 550, #bb73ff `color.tempo.darkPrimary.90`; icon 24 x 24, #ffffff `color.tempo.gray.50`; layers div.JIYRe.SiAe9 1117.0x56.0 rgb(0, 0, 0) 16px; div.css-1f88yyt 40.0x40.0 T:1px solid rgba(0, 0, 0, 0.12) / R:1px solid rgba(0, 0, 0, 0.12) / B:1px solid rgba(0, 0, 0, 0.12) / L:1px solid rgba(0, 0, 0, 0.12) 8px; button.chakra-button.css-3yg119 32.0x32.0 rgb(173, 71, 255) 2px solid rgba(0, 0, 0, 0) offset 0px 256px; button.chakra-button.css-5xmo61 32.0x32.0 2px solid rgba(0, 0, 0, 0) offset 0px 256 |
| hover | layers div.JIYRe.SiAe9 1117.0x56.0 rgb(20, 18, 22) 16px; div.css-1f88yyt 40.0x40.0 T:1px solid rgba(0, 0, 0, 0.12) / R:1px solid rgba(0, 0, 0, 0.12) / B:1px solid rgba(0, 0, 0, 0.12) / L:1px solid rgba(0, 0, 0, 0.12) 8px; button.chakra-button.css-3yg119 32.0x32.0 rgb(173, 71, 255) 2px solid rgba(0, 0, 0, 0) offset 0px 256px; button.chakra-button.css-5xmo61 32.0x32.0 2px solid rgba(0, 0, 0, 0) offset 0px  |

Child layers that carry the look: div 1117x56 background #000000 `color.tempo.gray.900` radius 16px; div 40x40 border 1px solid rgba(0, 0, 0, 0.12) radius 8px; button 32x32 background #ad47ff `color.tempo.darkPrimary.100` radius 256px.

![Album track row default](components/crops/album-track-row-default.png) ![Album track row hover](components/crops/album-track-row-hover.png)

### Player bar

The fixed bottom playback bar: track title and artists, the heart and context actions, transport controls, queue and volume.

#### Player bar
The bottom playback bar: track title/artists, heart and add, transport controls, queue and volume. Read as `player-bar` on the artist page.

**Values (default).** size 1416 x 80; padding 0px 12px; background transparent; text Inter 15/18.75 550, #ffffff `color.tempo.gray.50`; icon 24 x 24, #ffffff `color.tempo.gray.50`; layers div.css-1f88yyt 48.0x48.0 T:1px solid rgba(0, 0, 0, 0.12) / R:1px solid rgba(0, 0, 0, 0.12) / B:1px solid rgba(0, 0, 0, 0.12) / L:1px solid rgba(0, 0, 0, 0.12) 8px; a.chakra-link.css-o05beu 301.0x19.0 2px solid rgba(0, 0, 0, 0) offset 2px; a.chakra-link.css-o05beu 63.0x16.0 2px solid rgba(0, 0, 0, 0) offset 2px; a.chakra-link.css-o05beu 123.0x16.0 2px solid rgba(0, 0, 0, 0) offset 2px; button.chak.

Child layers that carry the look: div 48x48 border 1px solid rgba(0, 0, 0, 0.12) radius 8px; a 301x19; a 63x16.

![Player bar default](components/crops/player-bar-default.png)

#### Player track
The playing track's title in the player bar. Read as `player-track` on the artist page.

**Values (default).** size 301 x 19; background transparent; outline 2px solid transparent, offset 2px; text Inter 15/18.75 550, #ffffff `color.tempo.gray.50`; transition background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1); layers a.chakra-link.css-o05beu 301.0x19.0 2px solid rgba(0, 0, 0, 0) offset 2px.

Child layers that carry the look: a 301x19.

![Player track default](components/crops/player-track-default.png)

#### Play button (player)
The player's round purple play toggle; measured, never pressed. Read as `player-play` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 256px; background #ad47ff `color.tempo.darkPrimary.100`; outline 2px solid transparent, offset 0px; text Inter 13/18.57 550, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; icon 24 x 24, #ffffff `color.tempo.gray.50` |
| hover | background #bb73ff `color.tempo.darkPrimary.90`; text Inter 13/18.57 550, #f5f2f8 `color.tempo.neutralPrimary.10`; icon 24 x 24, #f5f2f8 `color.tempo.neutralPrimary.10` |
| focus-visible | outline 2px solid #f5f2f8 `color.tempo.neutralPrimary.10`, offset 0px |
| pressed | background #ca97ff `color.tempo.darkPrimary.80`; text Inter 13/18.57 550, #e2dfe6 `color.tempo.gray.100`; icon 24 x 24, #e2dfe6 `color.tempo.gray.100` |

![Play button (player) default](components/crops/player-play-default.png) ![Play button (player) hover](components/crops/player-play-hover.png) ![Play button (player) focus-visible](components/crops/player-play-focus-visible.png) ![Play button (player) pressed](components/crops/player-play-pressed.png)

#### Previous button
The player’s back-track icon button (aria-label "Back"); measured, never pressed. Read as `player-prev` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 32 x 32; radius 256px; background transparent; outline 2px solid transparent, offset 0px; text Inter 13/18.57 550, #706e73 `color.tempo.neutralPrimary.110`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; icon 24 x 24, #706e73 `color.tempo.neutralPrimary.110`; layers button.chakra-button.css-n97h1w 32.0x32.0 2px solid rgba(0, 0, 0, 0) offset 0px 256px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: button 32x32 radius 256px.

![Previous button default](components/crops/player-prev-default.png) ![Previous button hover](components/crops/player-prev-hover.png) ![Previous button pressed](components/crops/player-prev-pressed.png)

#### Next button
The player's next-track icon button; measured, never pressed. Read as `player-next` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 256px; background transparent; outline 2px solid transparent, offset 0px; text Inter 13/18.57 550, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; icon 24 x 24, #ffffff `color.tempo.gray.50`; layers button.chakra-button.css-n97h1w 32.0x32.0 2px solid rgba(0, 0, 0, 0) offset 0px 256px |
| hover | background #2e2c30 `color.tempo.gray.800`; text Inter 13/18.57 550, #f5f2f8 `color.tempo.neutralPrimary.10`; icon 24 x 24, #f5f2f8 `color.tempo.neutralPrimary.10`; layers none |
| focus-visible | outline 2px solid #ad47ff `color.tempo.darkPrimary.100`, offset 0px; layers button.chakra-button.css-n97h1w 32.0x32.0 2px solid rgb(173, 71, 255) offset 0px 256px |
| pressed | background #38373b `color.tempo.neutralPrimary.160`; text Inter 13/18.57 550, #e2dfe6 `color.tempo.gray.100`; icon 24 x 24, #e2dfe6 `color.tempo.gray.100`; layers none |

Child layers that carry the look: button 32x32 radius 256px.

![Next button default](components/crops/player-next-default.png) ![Next button hover](components/crops/player-next-hover.png) ![Next button focus-visible](components/crops/player-next-focus-visible.png) ![Next button pressed](components/crops/player-next-pressed.png)

#### Shuffle button
The player's shuffle icon button; measured, never toggled. Read as `player-shuffle` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 256px; background transparent; outline 2px solid transparent, offset 0px; text Inter 13/18.57 550, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; icon 24 x 24, #ffffff `color.tempo.gray.50`; layers button.chakra-button.css-n97h1w 32.0x32.0 2px solid rgba(0, 0, 0, 0) offset 0px 256px |
| hover | background #2e2c30 `color.tempo.gray.800`; text Inter 13/18.57 550, #f5f2f8 `color.tempo.neutralPrimary.10`; icon 24 x 24, #f5f2f8 `color.tempo.neutralPrimary.10`; layers none |
| focus-visible | outline 2px solid #ad47ff `color.tempo.darkPrimary.100`, offset 0px; layers button.chakra-button.css-n97h1w 32.0x32.0 2px solid rgb(173, 71, 255) offset 0px 256px |
| pressed | background #38373b `color.tempo.neutralPrimary.160`; text Inter 13/18.57 550, #e2dfe6 `color.tempo.gray.100`; icon 24 x 24, #e2dfe6 `color.tempo.gray.100`; layers none |

Child layers that carry the look: button 32x32 radius 256px.

![Shuffle button default](components/crops/player-shuffle-default.png) ![Shuffle button hover](components/crops/player-shuffle-hover.png) ![Shuffle button focus-visible](components/crops/player-shuffle-focus-visible.png) ![Shuffle button pressed](components/crops/player-shuffle-pressed.png)

#### Player overflow
The player's context-menu icon button; measured, never opened. Read as `player-more` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 256px; background transparent; outline 2px solid transparent, offset 0px; text Inter 13/18.57 550, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; icon 24 x 24, #ffffff `color.tempo.gray.50`; layers button.chakra-button.popper-wrapper 32.0x32.0 2px solid rgba(0, 0, 0, 0) offset 0px 256px |
| hover | background #2e2c30 `color.tempo.gray.800`; text Inter 13/18.57 550, #f5f2f8 `color.tempo.neutralPrimary.10`; icon 24 x 24, #f5f2f8 `color.tempo.neutralPrimary.10`; layers none |
| focus-visible | outline 2px solid #ad47ff `color.tempo.darkPrimary.100`, offset 0px; layers button.chakra-button.popper-wrapper 32.0x32.0 2px solid rgb(173, 71, 255) offset 0px 256px |
| pressed | text Inter 13/18.57 550, #bb73ff `color.tempo.darkPrimary.90`; icon 24 x 24, #bb73ff `color.tempo.darkPrimary.90` |

Child layers that carry the look: button 32x32 radius 256px.

![Player overflow default](components/crops/player-more-default.png) ![Player overflow hover](components/crops/player-more-hover.png) ![Player overflow focus-visible](components/crops/player-more-focus-visible.png) ![Player overflow pressed](components/crops/player-more-pressed.png)

### Signup banner

The lavender 'Live the music with Deezer' upsell strip pinned above the player bar.

#### Signup banner
The light-purple "Live the music with Deezer" upsell strip pinned above the player bar. Read as `signup-banner` on the artist page.

**Values (default).** size 1440 x 80; padding 16px; background #ead1ff; text Inter 20/24 700, #000000 `color.tempo.gray.900`; icon 24 x 24, #8a22de `color.tempo.lightPrimary.110`.

![Signup banner default](components/crops/signup-banner-default.png)

#### Banner CTA
The banner's purple "Sign up for free" pill; measured never followed. Read as `banner-cta` on the artist page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 166 x 48; padding 12px 24px; radius 16px; background #a238ff `color.tempo.lightPrimary.100`; outline 2px solid transparent, offset 0px; text Inter 15/22.5 550, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease |
| hover | background #8a22de `color.tempo.lightPrimary.110`; text Inter 15/22.5 550, #e2dfe6 `color.tempo.gray.100` |
| focus-visible | outline none |
| pressed | background #6908ae `color.tempo.lightPrimary.120`; outline none; text Inter 15/22.5 550, #d5d2d8 `color.tempo.neutralPrimary.30` |

![Banner CTA default](components/crops/banner-cta-default.png) ![Banner CTA hover](components/crops/banner-cta-hover.png) ![Banner CTA focus-visible](components/crops/banner-cta-focus-visible.png) ![Banner CTA pressed](components/crops/banner-cta-pressed.png)

### Login and signup

The dark account.deezer.com forms: wordmark, e-mail and password fields, show-password, submit, forgotten-password and social buttons — measured, never submitted.

#### Login logo
The Deezer wordmark over the form; links back to deezer.com, measured never followed. Read as `login-logo` on the login page.

**Values (default).** size 106.66 x 30; background transparent; text Inter 16/24 400, #ffffff `color.tempo.gray.50`; icon 106.66 x 30, #ffffff `color.tempo.gray.50`.

![Login logo default](components/crops/login-logo-default.png)

#### Email field
The login e-mail input; focused and typed into then cleared — never submitted. Read as `login-field-email` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 512 x 48; padding 0px 12px 0px 16px; border 2px solid transparent; radius 16px; background #242326 `color.tempo.neutralPrimary.180`; outline 2px solid transparent, offset 2px; text Inter 15/22.5 450, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; placeholder #ffffff `color.tempo.gray.50` |
| focused, filled | border 2px solid #ad47ff `color.tempo.darkPrimary.100`; background #2e2c30 `color.tempo.gray.800`; text Inter 15/22.5 450, #f5f2f8 `color.tempo.neutralPrimary.10`; placeholder #f5f2f8 `color.tempo.neutralPrimary.10` |

![Email field default](components/crops/login-field-email-default.png) ![Email field focused](components/crops/login-field-email-focused.png) ![Email field filled](components/crops/login-field-email-filled.png)

#### Password field
The login password input; focused and typed into then cleared — never submitted. Read as `login-field-password` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 512 x 48; padding 0px 44px 0px 16px; border 2px solid transparent; radius 16px; background #242326 `color.tempo.neutralPrimary.180`; outline 2px solid transparent, offset 2px; text Inter 15/22.5 450, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; placeholder #ffffff `color.tempo.gray.50` |
| focused, filled | border 2px solid #ad47ff `color.tempo.darkPrimary.100`; background #2e2c30 `color.tempo.gray.800`; text Inter 15/22.5 450, #f5f2f8 `color.tempo.neutralPrimary.10`; placeholder #f5f2f8 `color.tempo.neutralPrimary.10` |

![Password field default](components/crops/login-field-password-default.png) ![Password field focused](components/crops/login-field-password-focused.png) ![Password field filled](components/crops/login-field-password-filled.png)

#### Show-password button
The eye icon button inside the password field (a local reveal toggle); measured, never clicked. Read as `login-show-password` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 48 x 48; radius 256px; background transparent; outline 2px solid transparent, offset 0px; text Inter 15/22.5 550, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; icon 20 x 20, #ffffff `color.tempo.gray.50`; layers button.chakra-button.css-18xil4h 48.0x48.0 2px solid rgba(0, 0, 0, 0) offset 0px 256px |

Child layers that carry the look: button 48x48 radius 256px.

![Show-password button default](components/crops/login-show-password-default.png) ![Show-password button hover](components/crops/login-show-password-hover.png) ![Show-password button focus-visible](components/crops/login-show-password-focus-visible.png) ![Show-password button pressed](components/crops/login-show-password-pressed.png)

#### Log in submit
The login submit button; its states were measured but the button was never clicked — nothing was submitted. Read as `login-submit` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 512 x 48; padding 12px 24px; radius 16px; background #ad47ff `color.tempo.darkPrimary.100`; outline 2px solid transparent, offset 0px; text Inter 15/22.5 550, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease |
| hover | background #bb73ff `color.tempo.darkPrimary.90`; text Inter 15/22.5 550, #f5f2f8 `color.tempo.neutralPrimary.10` |
| focus-visible | outline 2px solid #f5f2f8 `color.tempo.neutralPrimary.10`, offset 0px |
| pressed | background #ca97ff `color.tempo.darkPrimary.80`; text Inter 15/22.5 550, #e2dfe6 `color.tempo.gray.100` |

![Log in submit default](components/crops/login-submit-default.png) ![Log in submit hover](components/crops/login-submit-hover.png) ![Log in submit focus-visible](components/crops/login-submit-focus-visible.png) ![Log in submit pressed](components/crops/login-submit-pressed.png)

#### Forgotten-password link
The "Forgotten password?" helper link; measured, never followed. Read as `login-forgot` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 512 x 17; background transparent; text Inter 14/normal 400, #a19fa4 `color.tempo.neutralPrimary.70` |
| focus-visible | outline 1px auto #ad47ff `color.tempo.darkPrimary.100`, offset 1px; layers a.chakra-form__helper-text.css-1u9opuw 512.0x17.0 1px auto rgb(173, 71, 255) offset 1px |

![Forgotten-password link default](components/crops/login-forgot-default.png) ![Forgotten-password link hover](components/crops/login-forgot-hover.png) ![Forgotten-password link focus-visible](components/crops/login-forgot-focus-visible.png) ![Forgotten-password link pressed](components/crops/login-forgot-pressed.png)

#### Signup link (login)
The "Sign up" action beside the form; measured, never followed. Read as `login-signup` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 53 x 17; radius 16px; background transparent; outline 2px solid transparent, offset 0px; text Inter 14/21 700, #ad47ff `color.tempo.darkPrimary.100`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; layers a.chakra-button.css-fo53qv 53.0x17.0 2px solid rgba(0, 0, 0, 0) offset 0px 16px |
| pressed | text Inter 14/21 700, #ca97ff `color.tempo.darkPrimary.80` |

Child layers that carry the look: a 53x17 radius 16px.

![Signup link (login) default](components/crops/login-signup-default.png) ![Signup link (login) hover](components/crops/login-signup-hover.png) ![Signup link (login) focus-visible](components/crops/login-signup-focus-visible.png) ![Signup link (login) pressed](components/crops/login-signup-pressed.png)

#### Social login button
A Google/Facebook/Apple round social sign-in button; measured, never followed. Read as `social-btn` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 48 x 48; border 1px solid #4e4c51 `color.tempo.gray.700`; radius 256px; background transparent; outline 1px solid transparent, offset 0px; text Inter 15/22.5 550, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; icon 24 x 24, #ffffff `color.tempo.gray.50` |
| hover | border 1px solid #59575c `color.tempo.neutralPrimary.130`; background #2e2c30 `color.tempo.gray.800`; text Inter 15/22.5 550, #f5f2f8 `color.tempo.neutralPrimary.10`; icon 24 x 24, #f5f2f8 `color.tempo.neutralPrimary.10` |
| focus-visible | border 1px solid #ad47ff `color.tempo.darkPrimary.100`; outline 1px solid #ad47ff `color.tempo.darkPrimary.100`, offset 0px |
| pressed | border 1px solid #656367 `color.tempo.gray.600`; background #38373b `color.tempo.neutralPrimary.160`; text Inter 15/22.5 550, #e2dfe6 `color.tempo.gray.100`; icon 24 x 24, #e2dfe6 `color.tempo.gray.100` |

![Social login button default](components/crops/social-btn-default.png) ![Social login button hover](components/crops/social-btn-hover.png) ![Social login button focus-visible](components/crops/social-btn-focus-visible.png) ![Social login button pressed](components/crops/social-btn-pressed.png)

#### Signup field
A signup form input; focused and typed into then cleared — never submitted. Read as `signup-field` on the signup page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 512 x 48; padding 0px 12px 0px 16px; border 2px solid transparent; radius 16px; background #242326 `color.tempo.neutralPrimary.180`; outline 2px solid transparent, offset 2px; text Inter 15/22.5 450, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; placeholder #706e73 `color.tempo.neutralPrimary.110` |
| focused, filled | border 2px solid #ad47ff `color.tempo.darkPrimary.100`; background #2e2c30 `color.tempo.gray.800`; text Inter 15/22.5 450, #f5f2f8 `color.tempo.neutralPrimary.10` |

![Signup field default](components/crops/signup-field-default.png) ![Signup field focused](components/crops/signup-field-focused.png) ![Signup field filled](components/crops/signup-field-filled.png)

#### Signup action
The signup form's submit action; its states were measured but it was never clicked — nothing was submitted. Read as `signup-cta` on the signup page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 512 x 48; padding 12px 24px; radius 16px; background #2e2c30 `color.tempo.gray.800`; outline 2px solid transparent, offset 0px; text Inter 15/22.5 550, #706e73 `color.tempo.neutralPrimary.110`; transition background-color 0.2s ease, border-color 0.2s ease, outline-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Signup action default](components/crops/signup-cta-default.png) ![Signup action hover](components/crops/signup-cta-hover.png) ![Signup action pressed](components/crops/signup-cta-pressed.png)

### Mobile (390 wide)

The phone surface at 390 wide: the mobile top bar, the burger nav overlay, the artist hero, the signup card and track rows.

#### Mobile top bar
The phone top bar: purple heart + DEEZER wordmark, Sign-up pill, hamburger. Read as `m-topbar` on the artist page at 390 wide.

**Values (default).** size 390 x 60; padding 0px 16px; background transparent; text Inter 14/normal 700, #ffffff `color.tempo.gray.50`; layers a.topbar-action.tempo-btn 0.0x0.0 T:1px solid rgb(85, 82, 87) / R:1px solid rgb(85, 82, 87) / B:1px solid rgb(85, 82, 87) / L:1px solid rgb(85, 82, 87) 12px; a.topbar-action.tempo-btn 95.0x37.0 rgb(162, 56, 255) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 12px; span.burger-line 25.0x3.0 rgb(248, 248, 249) rgba(0, 0, 0, 0.

Child layers that carry the look: a 0x0 border 1px solid #555257 radius 12px; a 95x37 background #a238ff `color.tempo.lightPrimary.100` border 1px solid transparent radius 12px; span 25x3 background #f8f8f9 shadow rgba(0, 0, 0, 0.1) 0px 4px 8px 0px, rgba(0, 0, 0, 0.1) 0px 0px 4px 0px.

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Mobile Sign up
The purple Sign-up pill in the phone top bar; measured never followed. Read as `m-signup` on the artist page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 95 x 37; padding 9px 20px; border 1px solid transparent; radius 12px; background #a238ff `color.tempo.lightPrimary.100`; text Inter 14/normal 700, #ffffff `color.tempo.gray.50`; transition background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, transform 0.2s ease |
| hover | background #9333e8 |
| pressed | size 90.25 x 35.15; background #9333e8; transform scale(0.95) |

![Mobile Sign up default](components/crops/m-signup-default.png) ![Mobile Sign up hover](components/crops/m-signup-hover.png) ![Mobile Sign up focus-visible](components/crops/m-signup-focus-visible.png) ![Mobile Sign up pressed](components/crops/m-signup-pressed.png)

#### Mobile hamburger
The burger icon that opens the phone nav overlay — a local UI toggle; the opened state was measured after clicking it. Read as `m-hamburger` on the artist page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 25 x 25; background transparent; text Inter 16/normal 400, #fdfcfe; layers span.burger-line 25.0x3.0 rgb(248, 248, 249) rgba(0, 0, 0, 0.1) 0px 4px 8px 0px, rgba(0, 0, 0, 0.1) 0px 0px 4px 0px; span.burger-line 25.0x3.0 rgb(248, 248, 249) rgba(0, 0, 0, 0.1) 0px 4px 8px 0px, rgba(0, 0, 0, 0.1) 0px 0px 4px 0px; span.burger-line 25.0x3.0 rgb(248, 248, 249) rgba(0, 0, 0, 0.1) 0px 4px 8px 0px, rgba(0, 0, 0, 0.1) 0px 0px 4px 0px; ul.nav.burger-menu-content 0.0x0.0 rgb(15, 13, 19 |
| opened | text Inter 20/normal 600, #fdfcfe; layers span.burger-line 19.8x19.8 rgb(248, 248, 249) rgba(0, 0, 0, 0.1) 0px 4px 8px 0px, rgba(0, 0, 0, 0.1) 0px 0px 4px 0px; span.burger-line 25.0x3.0 rgb(248, 248, 249) rgba(0, 0, 0, 0.1) 0px 4px 8px 0px, rgba(0, 0, 0, 0.1) 0px 0px 4px 0px; span.burger-line 19.8x19.8 rgb(248, 248, 249) rgba(0, 0, 0, 0.1) 0px 4px 8px 0px, rgba(0, 0, 0, 0.1) 0px 0px 4px 0px; ul.nav.burger-menu-content 390.0x844.0 rgb(15,  |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: span 25x3 background #f8f8f9 shadow rgba(0, 0, 0, 0.1) 0px 4px 8px 0px, rgba(0, 0, 0, 0.1) 0px 0px 4px 0px; span 25x3 background #f8f8f9 shadow rgba(0, 0, 0, 0.1) 0px 4px 8px 0px, rgba(0, 0, 0, 0.1) 0px 0px 4px 0px; span 25x3 background #f8f8f9 shadow rgba(0, 0, 0, 0.1) 0px 4px 8px 0px, rgba(0, 0, 0, 0.1) 0px 0px 4px 0px.

![Mobile hamburger default](components/crops/m-hamburger-default.png) ![Mobile hamburger hover](components/crops/m-hamburger-hover.png) ![Mobile hamburger pressed](components/crops/m-hamburger-pressed.png) ![Mobile hamburger opened](components/crops/m-hamburger-opened.png)

#### Mobile drawer
The nav overlay opened by the burger toggle; its links were never followed. Read as `m-drawer` on the artist page at 390 wide.

**Values (default).** size 390 x 844; padding 89px 0px 0px 0px; background #0f0d13; text Inter 20/normal 600, #fdfcfe.

![Mobile drawer default](components/crops/m-drawer-default.png)

#### Mobile artist name
The artist name over the phone hero image. Read as `m-hero-name` on the artist page at 390 wide.

**Values (default).** size 147 x 44; background transparent; text Deezer Product 40/44 700, #fdfcfe.

![Mobile artist name default](components/crops/m-hero-name-default.png)

#### Mobile signup card
The "Start listening on Deezer / Sign up to listen to this artist" card — the signed-out gate for playback. Read as `m-signup-card` on the artist page at 390 wide.

**Values (default).** size 221 x 46.38; background transparent; text Inter 16/19.2 700, #ffffff `color.tempo.gray.50`.

![Mobile signup card default](components/crops/m-signup-card-default.png)

#### Mobile track row
A track row in the phone list (thumb, title, artists, duration). Read as `m-track-row` on the artist page at 390 wide.

**Values (default).** size 390 x 48; padding 0px 16px; background transparent; text Inter 16/19.2 400, #fdfcfe.

![Mobile track row default](components/crops/m-track-row-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Deezer wordmark and heart, social sign-in glyphs, the player transport icons, the catalogue artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The signed-in Deezer lives behind account.deezer.com — playlists, library, Flow, downloads, settings and billing all need an account and were never reached. The dark catalog pages (/en/artist, /en/album, /en/playlist) are genuinely public signed-out app surfaces; playback itself was never started, so what happens after Play is unverified.

### Pages

- **The account.** Every post-login surface was never reached; the login and signup forms were measured as forms and never submitted.
- **Checkout and signup.** Every Try-for-free, Sign-up and payment/go.php action was measured, never followed.
- **Playback.** Play, Mix, queue, volume and shuffle controls were measured, never pressed; what playing a track does signed out is unverified.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **The header search navigates on type**: typing 'daft punk' routes to /search/<q>, so the field was measured last on its page and the results page itself is an unmeasured route.
- **menu-item focus-visible** is uncaptured: the overflow popover closes on blur before a keyboard focus can be held.

### Themes

Deezer paints a light surface (the home hero) and dark surfaces (the rest of the marketing pages, the catalog app, the account forms) rather than a user theme toggle — but the Tempo layer genuinely declares both `[data-theme="light"]` and `[data-theme="dark"]` semantics, so tokens.json keeps real light and dark sets.

### Fonts

- **Inter** (UI text), **Deezer Product** (marketing headings/mobile), **Deezer Brand** (the condensed marketing display) and **Deezer Headline VF** (app headings) are the served faces. They are served from Deezer's CDN; the style guide falls back to system sans.

### Screenshots

- The artist/album artwork, playlist covers, the Deezer wordmark and any photography in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Track titles, artist names and catalogue artwork are the product's content; only frames and components were measured.
