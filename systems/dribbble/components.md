# Dribbble components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from dribbble.com on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. dribbble.com paints a single light surface in three CSS eras — the Rails-era mini-master bundle (Mona Sans, hardcoded values), Vite/Shoelace components with the --sl-* token layer re-bound to the Dribbble pink, and Algolia/intl-tel-input vendor styles. Nothing was signed into, filled, followed, liked or submitted; the only presses were the Explore dropdown and the mobile menu's own toggles. The signed-out feed is a teaser: it paints one shot card then a Sign-up-to-continue wall, which is a documented boundary.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (87 components, 245 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (242 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light` — dribbble.com declares no product dark theme (the only dark CSS scope re-binds the third-party Algolia search dropdown vars). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Shots feed | `/shots/popular` | [default](screenshots/shots-light-default.png), [full](screenshots/shots-light-full.png) |
| Shot detail | `/shots/27884620-…` | [default](screenshots/shot-light-default.png), [full](screenshots/shot-light-full.png) |
| Designer profile | `/Moonsight` | [default](screenshots/designer-light-default.png), [full](screenshots/designer-light-full.png) |
| Designers directory | `/designers` | [default](screenshots/designers-light-default.png), [full](screenshots/designers-light-full.png) |
| Jobs board | `/jobs` | [default](screenshots/jobs-light-default.png), [full](screenshots/jobs-light-full.png) |
| Search | `/search?q=logo` | [default](screenshots/search-light-default.png), [full](screenshots/search-light-full.png) |
| Stories (blog) | `/stories` | [default](screenshots/stories-light-default.png), [full](screenshots/stories-light-full.png) |
| Sign up | `/signup` | [default](screenshots/signup-light-default.png) |
| Log in | `/session/new` | [default](screenshots/login-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Shots feed, phone | `/shots/popular` | [default](screenshots/mobile-shots-light-default.png), [full](screenshots/mobile-shots-light-full.png) |
| Designer profile, phone | `/Moonsight` | [default](screenshots/mobile-designer-light-default.png), [full](screenshots/mobile-designer-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the header menu toggle's own press | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open) |
| Explore dropdown | every page | the nav trigger's own hover, never followed | [home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#nav-dropdown), [menu-link](#menu-link) |
| WELCOME20 promo banner | home | page content, measured where it sits; its Get-Started action was never pressed | [promo-banner](#promo-banner) |
| Project-brief card, Google One Tap and consent overlays | every page | hidden, never answered (no consent button was ever clicked, no OAuth flow started) | hidden before every shot and reading |
| Sign-up-to-continue wall | /shots/popular and the home feed | the signed-out feed's own boundary — measured, never followed | [shots-light-full](screenshots/shots-light-full.png), [wall-cta](#sign-up-wall) |
| Signed-in product | the post-login workspace | posting shots, following, hiring flows and dashboards live behind sign-in | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 48 components were given a real keyboard focus. 45 draw an outline ring: `nav-trigger` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `nav-link` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `signup-link` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `login-btn` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `menu-link` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `hero-cta` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `view-tab` (on a child: 2px solid rgb(13, 12, 34) offset 2px), `search-go` (2px solid #f3afe4 `focusRing.measured.color`, offset 0px), `tag-chip` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `shot-card` (on a child: 2px solid rgb(243, 175, 228) offset 1px), `shot-title` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `pro-badge` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `wall-cta` (1px solid #6e6d7a `color.measured.muted-2`, offset 1px), `category-tile` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `shot-author` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `shot-follow` (1px solid #6e6d7a `color.measured.muted-2`, offset 1px), `shot-cta` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `shot-icon-btn` (2px solid #f3afe4 `focusRing.measured.color`, offset 0px), `rail-btn` (2px solid #f3afe4 `focusRing.measured.color`, offset 0px), `profile-cta` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `profile-follow` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `profile-icon-btn` (2px solid #f3afe4 `focusRing.measured.color`, offset 0px), `profile-tab` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `profile-sort` (1px solid #6e6d7a `color.measured.muted-2`, offset 1px), `profile-shot-card` (on a child: 2px solid rgb(243, 175, 228) offset 1px), `topic-chip` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `designer-card` (on a child: 2px solid rgb(243, 175, 228) offset 1px), `designer-name` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `badge-select` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `designer-cta` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `bookmark-btn` (2px solid #f3afe4 `focusRing.measured.color`, offset 0px), `skill-chip-dark` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `skill-chip` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `job-apply` (2px solid #f3afe4 `focusRing.measured.color`, offset 0px), `related-link` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `filter-tab` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `filter-sort` (1px solid #6e6d7a `color.measured.muted-2`, offset 1px), `filters-btn` (1px solid #6e6d7a `color.measured.muted-2`, offset 1px), `grid-shot-card` (on a child: 2px solid rgb(243, 175, 228) offset 1px), `story-card` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `story-tag` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `continue-btn` (2px solid #f3afe4 `focusRing.measured.color`, offset 0px), `auth-link` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `footer-link` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px), `social-icon` (2px solid #f3afe4 `focusRing.measured.color`, offset 1px). 2 draw a focus ring as a shadow instead: `sort-select`, `filter-select`. The other 1 show no measured change: `scope-select`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.05s | `cubic-bezier(0.32, 0, 0.59, 0.03)` | background-color, border, border-radius, color, padding | bookmark-btn, continue-btn, designer-cta, hero-cta, job-apply, login-btn, profile-cta, profile-follow and more |
| 0.1s | `ease` | color | auth-link, badge-select, category-tile, designer-name, filter-tab, footer-link, logo, m-search and more |
| 0.1s | `ease-in-out` | color | promoted-tag |
| 0.15s | `ease-in-out` | -webkit-box-shadow, box-shadow | designer-card |
| 0.2s | `cubic-bezier(0.34, 1.56, 0.64, 1)` | -webkit-box-shadow, background-color, border, box-shadow, color | email-field, filter-select, signup-field, sort-select |
| 0.2s | `ease` | -webkit-box-shadow, all, background-color, box-shadow, color, outline | filter-sort, filters-btn, home-search, job-card, profile-sort, profile-tab, search-input, shot-follow and more |
| 0.2s | `ease-in-out` | opacity, visibility | nav-dropdown |
| 0.25s | `ease-out` | opacity, visibility | m-menu-open |
| 0.3s | `cubic-bezier(0.34, 1.56, 0.64, 1)` | -webkit-transform, transform | nav-dropdown |
| 0.4s | `ease-in-out` | opacity | footer, header, m-header |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Shot card](#shot-card) | 297 x 254.75 | - | - | transparent | none | 0 |
| [Grid shot card](#grid-shot-card) | 297 x 254.75 | - | - | transparent | none | 0 |
| [Designer card](#designer-card) | 1296 x 416.13 | 1px solid #f3f3f4 | 8px | #ffffff `color.neutral.0` | rgba(18, 22, 25, 0.02) 0px 1px 10px 0px | 28px |
| [Login card](#login-card) | 1024 x 804 | - | - | transparent | none | 0px 48px |
| [Signup card](#signup-card) | 1024 x 804 | - | - | transparent | none | 0px 48px |
| [Story card](#story-card) | 808.61 x 86.19 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The header on the white field: the script wordmark, the Explore/Hire-Talent/Get-Hired/Community dropdowns, the search field and scope selector on inner pages, Sign up and the dark Log-in pill.

#### Header
The site nav bar (div.site-nav): the script Dribbble wordmark, the Explore/Hire-Talent/Get-Hired/Community dropdown triggers, the pink Start-Project-Brief link, Sign up and the dark Log-in pill. Read as `header` on the home page.

**Values (default).** size 1440 x 92; background transparent; text Mona Sans 14/30 600, #060318 `color.measured.link`; transition opacity 0.4s ease-in-out; icon 89 x 25, #060318 `color.measured.link`; layers div.site-nav__dark-overlay 1440.0x900.0 rgba(0, 0, 0, 0.5); div::before.site-nav__wrapper 1440pxx92px rgb(255, 255, 255); span 0.0x0.0 rgb(6, 3, 24) 1e+07px; span 0.0x0.0 rgb(6, 3, 24) 1e+07px; span 0.0x0.0 rgb(6, 3, 24) 1e+07px; div.site-nav-search.site-nav-search--nav 0.0x0.0 rgb(255, 255, 255).

Child layers that carry the look: div 1440x900 background rgba(0, 0, 0, 0.5); div::before 1440pxx92px background #ffffff `color.neutral.0`; span 0x0 background #060318 `color.measured.link` radius 1e+07px.

![Header default](components/crops/header-default.png)

#### Logo
The script Dribbble wordmark anchor. Read as `logo` on the home page.

**Values (default).** size 89 x 25; background transparent; text Mona Sans 16/28 400, #060318 `color.measured.link`; transition color 0.1s ease; icon 89 x 25, #060318 `color.measured.link`.

![Logo default](components/crops/logo-default.png)

#### Nav trigger
The Explore link that opens the header dropdown on hover; hovered, never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 97.84 x 30; padding 0px 16px; background transparent; text Mona Sans 14/30 600, #060318 `color.measured.link`; layers ::after rgba(0, 0, 0, 0) 0px none 1; a::after.site-nav-main__link 9pxx8px |
| hover | text Mona Sans 14/30 600, #7b7194 `dribbble.nav.link-hover` |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px; layers ::after rgba(0, 0, 0, 0) 0px none 1; a.site-nav-main__link 97.8x30.0 2px solid rgb(243, 175, 228) offset 1px; a::after.site-nav-main__link 9pxx8px |
| pressed | text Mona Sans 14/30 600, #7b7194 `dribbble.nav.link-hover` |

Child layers that carry the look: a::after 9pxx8px image url(data:…).

![Nav trigger default](components/crops/nav-trigger-default.png) ![Nav trigger hover](components/crops/nav-trigger-hover.png) ![Nav trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav trigger pressed](components/crops/nav-trigger-pressed.png)

#### Nav item
The Community dropdown trigger. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 126.97 x 30; padding 0px 16px; background transparent; text Mona Sans 14/30 600, #060318 `color.measured.link`; layers ::after rgba(0, 0, 0, 0) 0px none 1; a::after.site-nav-main__link 9pxx8px |
| hover | text Mona Sans 14/30 600, #7b7194 `dribbble.nav.link-hover` |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px; layers ::after rgba(0, 0, 0, 0) 0px none 1; a.site-nav-main__link 127.0x30.0 2px solid rgb(243, 175, 228) offset 1px; a::after.site-nav-main__link 9pxx8px |
| pressed | text Mona Sans 14/30 600, #7b7194 `dribbble.nav.link-hover` |

Child layers that carry the look: a::after 9pxx8px image url(data:…).

![Nav item default](components/crops/nav-link-default.png) ![Nav item hover](components/crops/nav-link-hover.png) ![Nav item focus-visible](components/crops/nav-link-focus-visible.png) ![Nav item pressed](components/crops/nav-link-pressed.png)

#### Sign-up link
The plain Sign-up header action; measured never followed. Read as `signup-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 50.63 x 17; background transparent; text Mona Sans 14/17 700, #060318 `color.measured.link`; transition color 0.1s ease |
| hover | text Mona Sans 14/17 700, #7b7194 `dribbble.nav.link-hover` |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px; layers a.site-nav__signup.site-nav-hide-mobile 50.6x17.0 2px solid rgb(243, 175, 228) offset 1px |
| pressed | text Mona Sans 14/17 700, #7b7194 `dribbble.nav.link-hover` |

![Sign-up link default](components/crops/signup-link-default.png) ![Sign-up link hover](components/crops/signup-link-hover.png) ![Sign-up link focus-visible](components/crops/signup-link-focus-visible.png) ![Sign-up link pressed](components/crops/signup-link-pressed.png)

#### Log-in button
The dark Log-in pill (btn2--medium); measured never followed. Read as `login-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 89.2 x 48; padding 0px 24px; border 1px solid #0d0c22 `color.measured.ink`; radius 1e+07px; background #0d0c22 `color.measured.ink`; text Mona Sans 14/14 600, #ffffff `color.neutral.0`; transition color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), background-color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border-radius 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03); layers ::before rgb(13, 12, 34) 0px none 0; ::after rgba(0, 0, 0, 0) 1px none 0 |
| hover | border 1px solid #3d3d4e `dribbble.button.bg-hover`; background #3d3d4e `dribbble.button.bg-hover` |
| focus-visible | border 1px solid #3d3d4e `dribbble.button.bg-hover`; background #3d3d4e `dribbble.button.bg-hover`; outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px |
| pressed | border 1px solid #3d3d4e `dribbble.button.bg-hover`; background #3d3d4e `dribbble.button.bg-hover` |

![Log-in button default](components/crops/login-btn-default.png) ![Log-in button hover](components/crops/login-btn-hover.png) ![Log-in button focus-visible](components/crops/login-btn-focus-visible.png) ![Log-in button pressed](components/crops/login-btn-pressed.png)

#### Nav dropdown
The Explore dropdown panel (ul.site-nav-sub: Popular, New and Noteworthy, category links), opened by hovering its own trigger. Read as `nav-dropdown` on the home page.

**Values (default).** size 230 x 479; padding 24px; border 1px solid rgba(231, 231, 233, 0.5); radius 8px; background #ffffff `color.neutral.0`; shadow rgba(27, 32, 50, 0.1) 0px 15px 50px 0px; text Mona Sans 14/17 600, #060318 `color.measured.link`; transition opacity 0.2s ease-in-out, visibility 0.2s ease-in-out, transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), -webkit-transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1); icon 20 x 20, #060318 `color.measured.link`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Nav dropdown default](components/crops/nav-dropdown-default.png)

#### Menu link
A link inside the opened Explore dropdown (each state re-hovers the Explore trigger first). Read as `menu-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 180 x 32; padding 0px 0px 12px 0px; background transparent; text Mona Sans 14/17 600, #060318 `color.measured.link`; icon 20 x 20, #060318 `color.measured.link` |
| hover | text Mona Sans 14/17 600, #7b7194 `dribbble.nav.link-hover`; icon 20 x 20, #7b7194 `dribbble.nav.link-hover` |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px; layers a.site-nav-sub__link.site-nav-sub__link--bold 180.0x32.0 2px solid rgb(243, 175, 228) offset 1px |
| pressed | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px; text Mona Sans 14/17 600, #7b7194 `dribbble.nav.link-hover`; icon 20 x 20, #7b7194 `dribbble.nav.link-hover`; layers a.site-nav-sub__link.site-nav-sub__link--bold 180.0x32.0 2px solid rgb(243, 175, 228) offset 1px |

![Menu link default](components/crops/menu-link-default.png) ![Menu link hover](components/crops/menu-link-hover.png) ![Menu link focus-visible](components/crops/menu-link-focus-visible.png) ![Menu link pressed](components/crops/menu-link-pressed.png)

#### Header search field
The "What are you looking for?" header field on inner pages; focused only, never submitted. Read as `search-input` on the shots feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 388.58 x 54; padding 0px 0px 0px 24px; radius 12px; background transparent; text Mona Sans 14/28 400, #060318 `color.measured.link`; transition background-color 0.2s ease, outline 0.2s ease, color 0.2s ease, box-shadow 0.2s ease, -webkit-box-shadow 0.2s ease; placeholder #3a3546 `color.measured.muted` |

![Header search field default](components/crops/search-input-default.png) ![Header search field focused](components/crops/search-input-focused.png)

#### Scope dropdown
The Shots scope selector beside the header search field (site-nav-search__dropdown-trigger); its list was never opened. Read as `scope-select` on the shots feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 57.42 x 40; padding 0px 18.5px 0px 0px; radius 8px; background transparent; text Mona Sans 14/14 600, #3a3546 `color.measured.muted`; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover, pressed | text Mona Sans 14/14 600, #7b7194 `dribbble.nav.link-hover` |

![Scope dropdown default](components/crops/scope-select-default.png) ![Scope dropdown hover](components/crops/scope-select-hover.png) ![Scope dropdown focus-visible](components/crops/scope-select-focus-visible.png) ![Scope dropdown pressed](components/crops/scope-select-pressed.png)

### Home

The hire-focused landing page: the WELCOME20 strip, the 52px Mona Sans hero with its rotating pink word, the checklist, the dark brief CTA, the shot carousel, and the Shots/Designers/Services tabs over the big search field with its 40px pink Go circle and Popular tag chips.

#### Promo banner
The WELCOME20 offer strip under the header — page content, measured where it sits; its Get-Started action was never pressed. Read as `promo-banner` on the home page.

**Values (default).** size 1440 x 62; padding 0px 40px; background transparent; text Mona Sans 14/19.6 500, #0d0c22 `color.measured.ink`; icon 31 x 31, #7b7194 `dribbble.nav.link-hover`; layers div.announcements__container 1360.0x62.0 rgba(244, 215, 243, 0.3) T:1px solid rgb(250, 235, 249) / R:1px solid rgb(250, 235, 249) / B:1px solid rgb(250, 235, 249) / L:1px solid rgb(250, 235, 249) 1e+07px; a.btn2.btn2--x-small 101.8x32.0 rgb(255, 255, 255) T:1px solid rgb(231, 231, 233) / R:1px solid rgb(231, 231, 233) / B:1px solid rgb(231, 231, 233) / L:1px solid rgb(231, 231, 233) 1e+07px; a::be.

Child layers that carry the look: div 1360x62 background rgba(244, 215, 243, 0.3) `color.measured.promo-surface` border 1px solid #faebf9 radius 1e+07px; a 101.8x32 background #ffffff `color.neutral.0` border 1px solid #e7e7e9 radius 1e+07px; a::before 99.7656pxx30px background #ffffff `color.neutral.0`.

![Promo banner default](components/crops/promo-banner-default.png)

#### Hero headline
The "Work with the world's best" display headline; one word rotates and paints the Dribbble pink. Read as `hero-title` on the home page.

**Values (default).** size 618 x 124.78; background transparent; text Mona Sans 52/62.4 600, #0d0c22 `color.measured.ink`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero accent word
The rotating accent word inside the headline. Read as `hero-accent` on the home page.

**Values (default).** size 418.44 x 62.39; background transparent; text Mona Sans 52/62.4 600, #ea4c89 `color.pink.500`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Hero accent word default](components/crops/hero-accent-default.png)

#### Hero checklist item
A pink-check bullet under the hero (li.home-header__list-item). Read as `hero-check` on the home page.

**Values (default).** size 618 x 22; background transparent; text Mona Sans 16/21 400, #0d0c22 `color.measured.ink`; layers ::before rgba(234, 76, 137, 0.1) 0px none 1; li::before.home-header__list-item 23pxx21px rgba(234, 76, 137, 0.1) 50%.

Child layers that carry the look: li::before 23pxx21px background rgba(234, 76, 137, 0.1) radius 50%.

![Hero checklist item default](components/crops/hero-check-default.png)

#### Hero CTA
The "Start Your Project Brief" dark pill; measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 230.03 x 49; padding 0px 24px; border 1px solid #0d0c22 `color.measured.ink`; radius 1e+07px; background #0d0c22 `color.measured.ink`; text Mona Sans 14/14 700, #ffffff `color.neutral.0`; transition color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), background-color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border-radius 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03); icon 17 x 17, #ffffff `color.neutral.0`; layers ::before rgb(13, 12, 34) 0px none 0; ::after rgba(0, 0, 0, 0) 1px none 0 |
| hover | border 1px solid #3d3d4e `dribbble.button.bg-hover`; background #3d3d4e `dribbble.button.bg-hover` |
| focus-visible | border 1px solid #3d3d4e `dribbble.button.bg-hover`; background #3d3d4e `dribbble.button.bg-hover`; outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px |
| pressed | border 1px solid #3d3d4e `dribbble.button.bg-hover`; background #3d3d4e `dribbble.button.bg-hover` |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero media card
The shot media panel beside the hero copy (figure.home-header-media, the animated designer-work card). Read as `hero-media` on the home page.

**Values (default).** size 614 x 430; radius 24px; background #f3f3f6; text Mona Sans 12/28 500, #0d0c22 `color.measured.ink`.

![Hero media card default](components/crops/hero-media-default.png)

#### View tab
A Shots/Designers/Services tab (a segmented-control label) over the search strip. Read as `view-tab` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 100.14 x 40; background transparent; text Mona Sans 13/13 600, #3a3546 `color.measured.muted`; icon 18 x 18, #3a3546 `color.measured.muted`; layers input 20.0x20.0 rgb(184, 80, 154) T:1px solid rgb(120, 60, 106) / R:1px solid rgb(120, 60, 106) / B:1px solid rgb(120, 60, 106) / L:1px solid rgb(120, 60, 106) 50%; input::after 10pxx10px rgb(255, 255, 255) 50%; span 100.1x40.0 rgb(250, 249, 251) T:1px solid rgb(250, 249, 251) / R:1px solid rgb(250, 249, 251) / B:1px solid rgb(250, 249, 251) / L:1px solid rgb(250, 249, 251) 1e+07px |
| focus-visible | layers input 20.0x20.0 rgb(184, 80, 154) T:1px solid rgb(120, 60, 106) / R:1px solid rgb(120, 60, 106) / B:1px solid rgb(120, 60, 106) / L:1px solid rgb(120, 60, 106) 50%; input::after 10pxx10px rgb(255, 255, 255) 50%; span 100.1x40.0 rgb(250, 249, 251) T:1px solid rgb(250, 249, 251) / R:1px solid rgb(250, 249, 251) / B:1px solid rgb(250, 249, 251) / L:1px solid rgb(250, 249, 251) 2px solid rgb(13, 12, 3 |

Child layers that carry the look: input 20x20 background #b8509a border 1px solid #783c6a radius 50%; input::after 10pxx10px background #ffffff `color.neutral.0` radius 50%; span 100.1x40 background #faf9fb border 1px solid #faf9fb radius 1e+07px.

![View tab default](components/crops/view-tab-default.png) ![View tab hover](components/crops/view-tab-hover.png) ![View tab focus-visible](components/crops/view-tab-focus-visible.png) ![View tab pressed](components/crops/view-tab-pressed.png)

#### Search field
The "What type of design are you interested in?" pill field; focused only, never submitted. Read as `home-search` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 1234 x 54; padding 0px 0px 0px 24px; radius 12px; background transparent; text Mona Sans 14/28 400, #060318 `color.measured.link`; transition background-color 0.2s ease, outline 0.2s ease, color 0.2s ease, box-shadow 0.2s ease, -webkit-box-shadow 0.2s ease; placeholder #3a3546 `color.measured.muted` |

![Search field default](components/crops/home-search-default.png) ![Search field focused](components/crops/home-search-focused.png)

#### Search button
The pink circle search button (btn2--circle); measured never pressed. Read as `search-go` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; border 1px solid #ea4c89 `color.pink.500`; radius 50%; background #ea4c89 `color.pink.500`; text Mona Sans 13/13 600, #ffffff `color.neutral.0`; transition color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), background-color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border-radius 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03); icon 20 x 20, #ffffff `color.neutral.0`; layers ::before rgb(234, 76, 137) 0px none 0; ::after rgba(0, 0, 0, 0) 1px none 0 |
| hover | border 1px solid #ec5e95 `color.measured.pink-hover`; background #ec5e95 `color.measured.pink-hover` |
| focus-visible | border 1px solid #ec5e95 `color.measured.pink-hover`; background #ec5e95 `color.measured.pink-hover`; outline 2px solid #f3afe4 `focusRing.measured.color`, offset 0px |
| pressed | border 1px solid #ec5e95 `color.measured.pink-hover`; background #ec5e95 `color.measured.pink-hover` |

![Search button default](components/crops/search-go-default.png) ![Search button hover](components/crops/search-go-hover.png) ![Search button focus-visible](components/crops/search-go-focus-visible.png) ![Search button pressed](components/crops/search-go-pressed.png)

#### Tag chip
A Popular-search tag link under the field. Read as `tag-chip` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 93.53 x 31; padding 0px 16px; border 1px solid #e7e7e9; radius 1e+07px; background #ffffff `color.neutral.0`; text Mona Sans 12/12 400, #0d0c22 `color.measured.ink`; transition color 0.1s ease |
| hover | background #faf9fb |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px |
| pressed | background #faf9fb |

![Tag chip default](components/crops/tag-chip-default.png) ![Tag chip hover](components/crops/tag-chip-hover.png) ![Tag chip focus-visible](components/crops/tag-chip-focus-visible.png) ![Tag chip pressed](components/crops/tag-chip-pressed.png)

#### Sort control
The "Popular" sort dropdown; its list was never opened. Read as `sort-select` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 94.45 x 35; padding 0px 34px 0px 14px; border 1px solid rgba(219, 218, 222, 0.9) `color.measured.field-border`; radius 8px; background #ffffff `color.neutral.0`; shadow rgba(6, 3, 24, 0.01) 0px 4px 4px 0px; text Mona Sans 12/12 500, #0d0c22 `color.measured.ink`; transition color 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), border 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), background-color 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), -webkit-box-shadow 0.2s cubic-bezier(0.34, 1.56, 0.64, 1); layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover, focus-visible, pressed | border 1px solid rgba(158, 158, 167, 0.7); shadow rgba(6, 3, 24, 0.03) 0px 4px 4px 0px |

![Sort control default](components/crops/sort-select-default.png) ![Sort control hover](components/crops/sort-select-hover.png) ![Sort control focus-visible](components/crops/sort-select-focus-visible.png) ![Sort control pressed](components/crops/sort-select-pressed.png)

### Shot feed

The signed-out feed on /shots/popular: the teaser shot card (avatar, name, PRO+ chip, like/view counts) then the Sign-up-to-continue wall, with browse-category tiles below.

#### Shot card
The one card the signed-out feed paints before the wall: image, designer avatar + name, PRO/PRO+ badge, like and view counts. Read as `shot-card` on the shots feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 297 x 254.75; background transparent; text Mona Sans 14/20 500, #ffffff `color.neutral.0`; icon 16 x 16, #0d0c22 `color.measured.ink`; layers div::after.js-thumbnail-base.shot-thumbnail-base 297pxx222.75px; figure.js-thumbnail-placeholder.shot-thumbnail-placeholder 297.0x222.8 rgb(229, 226, 192); div.shot-thumbnail-overlay 297.0x222.8 8px; a.btn2.btn2--secondary-alt 34.0x34.0 rgb(255, 255, 255) T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, 255, 255) 50%; a::before |
| focus-visible | layers div::after.js-thumbnail-base.shot-thumbnail-base 297pxx222.75px; figure.js-thumbnail-placeholder.shot-thumbnail-placeholder 297.0x222.8 rgb(229, 226, 192); a.shot-thumbnail-link.dribbble-link 297.0x222.8 2px solid rgb(243, 175, 228) offset 1px; div.shot-thumbnail-overlay 297.0x222.8 8px; a.btn2.btn2--secondary-alt 34.0x34.0 rgb(255, 255, 255) T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 2 |

Child layers that carry the look: div::after 297pxx222.75px image linear-gradient(transparent 0%, transparent 8.1%, transparent 15.5%, rgba(0, 0, 0, 0.004) ; figure 297x222.8 background #e5e2c0; div 297x222.8 image linear-gradient(transparent 62%, rgba(0, 0, 0, 0.004) 63.94%, rgba(0, 0, 0, 0.016) 65.89%, radius 8px.

![Shot card default](components/crops/shot-card-default.png) ![Shot card hover](components/crops/shot-card-hover.png) ![Shot card focus-visible](components/crops/shot-card-focus-visible.png) ![Shot card pressed](components/crops/shot-card-pressed.png)

#### Shot card link
The card's shot link (the image anchor carrying the title). Read as `shot-title` on the shots feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 297 x 222.75; background transparent; text Mona Sans 14/28 400, #0d0c22 `color.measured.ink`; transition color 0.1s ease |
| hover | text Mona Sans 14/28 400, #3d3d4e `dribbble.button.bg-hover` |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px; layers a.shot-thumbnail-link.dribbble-link 297.0x222.8 2px solid rgb(243, 175, 228) offset 1px |
| pressed | text Mona Sans 14/28 400, #3d3d4e `dribbble.button.bg-hover` |

![Shot card link default](components/crops/shot-title-default.png) ![Shot card link hover](components/crops/shot-title-hover.png) ![Shot card link focus-visible](components/crops/shot-title-focus-visible.png) ![Shot card link pressed](components/crops/shot-title-pressed.png)

#### PRO badge
The small PRO/PRO+ membership chip on the card. Read as `pro-badge` on the shots feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 20; padding 0px 5px; radius 4px; background #ecebf0; text Mona Sans 9/20 800, #524b63; transition color 0.1s ease |
| hover | background #d8d6d5 |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px |
| pressed | background #d8d6d5 |

![PRO badge default](components/crops/pro-badge-default.png) ![PRO badge hover](components/crops/pro-badge-hover.png) ![PRO badge focus-visible](components/crops/pro-badge-focus-visible.png) ![PRO badge pressed](components/crops/pro-badge-pressed.png)

#### Like/view count
A heart/eye count on the shot card. Read as `stat-count` on the shots feed page.

**Values (default).** size 12.11 x 16; background transparent; text Mona Sans 12/16 500, #3d3d4e `dribbble.button.bg-hover`.

![Like/view count default](components/crops/stat-count-default.png)

#### Sign-up wall
The "Sign up to continue" pill that ends the signed-out feed; measured never followed — the signed-in feed is the boundary. Read as `wall-cta` on the shots feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 159 x 40; padding 10px 20px; radius 1e+07px; background #0d0c22 `color.measured.ink`; text Mona Sans 13/20 600, #ffffff `color.neutral.0`; transition color 0.2s ease |
| hover | background #565564 |
| focus-visible | background #565564; outline 1px solid #6e6d7a `color.measured.muted-2`, offset 1px |
| pressed | background #565564 |

![Sign-up wall default](components/crops/wall-cta-default.png) ![Sign-up wall hover](components/crops/wall-cta-hover.png) ![Sign-up wall focus-visible](components/crops/wall-cta-focus-visible.png) ![Sign-up wall pressed](components/crops/wall-cta-pressed.png)

#### Category tile
A browse-category tile (Branding, Illustration…) under the wall. Read as `category-tile` on the shots feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 101.44 x 36; padding 0px 16px; radius 1e+07px; background transparent; text Mona Sans 14/20 600, #0d0c22 `color.measured.ink`; transition color 0.1s ease |
| hover | text Mona Sans 14/20 600, #6e6d7a `color.measured.muted-2`; transition all 0.2s ease |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px; layers a 101.4x36.0 2px solid rgb(243, 175, 228) offset 1px 1e+07px |
| pressed | text Mona Sans 14/20 600, #6e6d7a `color.measured.muted-2`; transition all 0.2s ease |

![Category tile default](components/crops/category-tile-default.png) ![Category tile hover](components/crops/category-tile-hover.png) ![Category tile focus-visible](components/crops/category-tile-focus-visible.png) ![Category tile pressed](components/crops/category-tile-pressed.png)

### Shot detail

A public shot page: title, designer attribution with Follow, the dark Get-in-touch pill, like/save icon buttons, the big media frame and the right action rail.

#### Shot title
The shot page headline. Read as `shot-detail-title` on the shot detail page.

**Values (default).** size 1024 x 29; background transparent; text Mona Sans 24/29 600, #0d0c22 `color.measured.ink`.

![Shot title default](components/crops/shot-detail-title-default.png)

#### Shot author
The designer attribution row (avatar, name, Follow). Read as `shot-author` on the shot detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 48 x 48; background transparent; text Mona Sans 14/28 400, #0d0c22 `color.measured.ink`; transition color 0.1s ease |
| hover | text Mona Sans 14/28 400, #3d3d4e `dribbble.button.bg-hover` |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px; layers a.user-sticky-header__avatar.hoverable 48.0x48.0 2px solid rgb(243, 175, 228) offset 1px |
| pressed | text Mona Sans 14/28 400, #3d3d4e `dribbble.button.bg-hover` |

![Shot author default](components/crops/shot-author-default.png) ![Shot author hover](components/crops/shot-author-hover.png) ![Shot author focus-visible](components/crops/shot-author-focus-visible.png) ![Shot author pressed](components/crops/shot-author-pressed.png)

#### Follow button
The Follow action under the author; measured never pressed. Read as `shot-follow` on the shot detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32.39 x 14; radius 8px; background transparent; text Mona Sans 11/11 400, #6e6d7a `color.measured.muted-2`; transition color 0.2s ease |
| hover | text Mona Sans 11/11 400, #0d0c22 `color.measured.ink` |
| focus-visible | outline 1px solid #6e6d7a `color.measured.muted-2`, offset 1px; layers a.form-btn.follow 32.4x14.0 1px solid rgb(110, 109, 122) offset 1px 8px |
| pressed | text Mona Sans 11/11 400, #0d0c22 `color.measured.ink` |

![Follow button default](components/crops/shot-follow-default.png) ![Follow button hover](components/crops/shot-follow-hover.png) ![Follow button focus-visible](components/crops/shot-follow-focus-visible.png) ![Follow button pressed](components/crops/shot-follow-pressed.png)

#### Get-in-touch button
The dark hire pill on the shot page; measured never followed. Read as `shot-cta` on the shot detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 117.88 x 40; padding 0px 20px; border 1px solid #0d0c22 `color.measured.ink`; radius 1e+07px; background #0d0c22 `color.measured.ink`; text Mona Sans 13/13 600, #ffffff `color.neutral.0`; transition color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), background-color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border-radius 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03); layers ::before rgb(13, 12, 34) 0px none 0; ::after rgba(0, 0, 0, 0) 1px none 0 |
| hover | border 1px solid #3d3d4e `dribbble.button.bg-hover`; background #3d3d4e `dribbble.button.bg-hover` |
| focus-visible | border 1px solid #3d3d4e `dribbble.button.bg-hover`; background #3d3d4e `dribbble.button.bg-hover`; outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px |
| pressed | border 1px solid #3d3d4e `dribbble.button.bg-hover`; background #3d3d4e `dribbble.button.bg-hover` |

![Get-in-touch button default](components/crops/shot-cta-default.png) ![Get-in-touch button hover](components/crops/shot-cta-hover.png) ![Get-in-touch button focus-visible](components/crops/shot-cta-focus-visible.png) ![Get-in-touch button pressed](components/crops/shot-cta-pressed.png)

#### Like/save icon button
A heart/bookmark round button beside the CTA; measured never pressed. Read as `shot-icon-btn` on the shot detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; border 1px solid #e7e7e9; radius 50%; background #ffffff `color.neutral.0`; text Mona Sans 13/13 600, #0d0c22 `color.measured.ink`; transition color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), background-color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border-radius 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03); icon 16 x 16, #0d0c22 `color.measured.ink`; layers ::before rgb(255, 255, 255) 0px none 0; ::after rgba(0, 0, 0, 0) 1px none 0 |
| hover | border 1px solid #dbdbde |
| focus-visible | border 1px solid #dbdbde; outline 2px solid #f3afe4 `focusRing.measured.color`, offset 0px |
| pressed | border 1px solid #dbdbde |

![Like/save icon button default](components/crops/shot-icon-btn-default.png) ![Like/save icon button hover](components/crops/shot-icon-btn-hover.png) ![Like/save icon button focus-visible](components/crops/shot-icon-btn-focus-visible.png) ![Like/save icon button pressed](components/crops/shot-icon-btn-pressed.png)

#### Shot media
The big shot image frame (largest image in main). Read as `shot-media` on the shot detail page.

**Values (default).** size 1023.98 x 1281.03; radius 8px; background transparent; text Mona Sans 14/28 400, #0d0c22 `color.measured.ink`.

![Shot media default](components/crops/shot-media-default.png)

#### Action rail button
A button on the right-hand action rail (like/share/info). Read as `rail-btn` on the shot detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; border 1px solid #e7e7e9; radius 50%; background #ffffff `color.neutral.0`; text Mona Sans 11/18 600, #6e6d7a `color.measured.muted-2`; transition color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), background-color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border-radius 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03); icon 16 x 16, #0d0c22 `color.measured.ink`; layers ::before rgb(255, 255, 255) 0px none 0; ::after rgba(0, 0, 0, 0) 1px none 0 |
| hover | border 1px solid #dbdbde |
| focus-visible | border 1px solid #dbdbde; outline 2px solid #f3afe4 `focusRing.measured.color`, offset 0px |
| pressed | border 1px solid #dbdbde |

![Action rail button default](components/crops/rail-btn-default.png) ![Action rail button hover](components/crops/rail-btn-hover.png) ![Action rail button focus-visible](components/crops/rail-btn-focus-visible.png) ![Action rail button pressed](components/crops/rail-btn-pressed.png)

### Designer profile

A public designer/agency page: avatar, PRO stamp, name and headline, follower stats, Get-in-touch and Follow pills, the Work/Services tab bar and the shot work grid.

#### Profile avatar
The designer's round avatar. Read as `profile-avatar` on the designer profile page.

**Values (default).** size 80 x 80; radius 50%; background #fdfcfb; text Mona Sans 16/28 400, #0d0c22 `color.measured.ink`.

![Profile avatar default](components/crops/profile-avatar-default.png)

#### Profile name
The designer/agency display name heading. Read as `profile-name` on the designer profile page.

**Values (default).** size 305.3 x 38; background transparent; text Mona Sans 32/38 700, #0d0c22 `color.measured.ink`.

![Profile name default](components/crops/profile-name-default.png)

#### Profile headline
The designer's tagline block (masthead-intro h2) under the name. Read as `profile-headline` on the designer profile page.

**Values (default).** size 600 x 168; background transparent; text Mona Sans 48/56 700, #0d0c22 `color.measured.ink`.

![Profile headline default](components/crops/profile-headline-default.png)

#### Profile stat
A followers/following/likes stat (.masthead-stats .stat) under the headline. Read as `profile-stat` on the designer profile page.

**Values (default).** size 93.56 x 28; background transparent; text Mona Sans 16/28 400, #6e6d7a `color.measured.muted-2`.

![Profile stat default](components/crops/profile-stat-default.png)

#### Get-in-touch button
The dark hire pill on the profile; measured never followed. Read as `profile-cta` on the designer profile page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 131.72 x 48; padding 0px 24px; border 1px solid #0d0c22 `color.measured.ink`; radius 1e+07px; background #0d0c22 `color.measured.ink`; text Mona Sans 14/14 600, #ffffff `color.neutral.0`; transition color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), background-color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border-radius 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03); layers ::before rgb(13, 12, 34) 0px none 0; ::after rgba(0, 0, 0, 0) 1px none 0 |
| hover | border 1px solid #3d3d4e `dribbble.button.bg-hover`; background #3d3d4e `dribbble.button.bg-hover` |
| focus-visible | border 1px solid #3d3d4e `dribbble.button.bg-hover`; background #3d3d4e `dribbble.button.bg-hover`; outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px |
| pressed | border 1px solid #3d3d4e `dribbble.button.bg-hover`; background #3d3d4e `dribbble.button.bg-hover` |

![Get-in-touch button default](components/crops/profile-cta-default.png) ![Get-in-touch button hover](components/crops/profile-cta-hover.png) ![Get-in-touch button focus-visible](components/crops/profile-cta-focus-visible.png) ![Get-in-touch button pressed](components/crops/profile-cta-pressed.png)

#### Follow button
The white Follow pill; measured never pressed. Read as `profile-follow` on the designer profile page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 93.14 x 48; padding 0px 24px; border 1px solid #e7e7e9; radius 1e+07px; background #ffffff `color.neutral.0`; text Mona Sans 14/14 600, #0d0c22 `color.measured.ink`; transition color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), background-color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border-radius 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03); layers ::before rgb(255, 255, 255) 0px none 0; ::after rgba(0, 0, 0, 0) 1px none 0 |
| hover | border 1px solid #dbdbde |
| focus-visible | border 1px solid #dbdbde; outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px |
| pressed | border 1px solid #dbdbde |

![Follow button default](components/crops/profile-follow-default.png) ![Follow button hover](components/crops/profile-follow-hover.png) ![Follow button focus-visible](components/crops/profile-follow-focus-visible.png) ![Follow button pressed](components/crops/profile-follow-pressed.png)

#### Icon button
The icon-only action beside Follow (save/message); measured never pressed. Read as `profile-icon-btn` on the designer profile page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 48 x 48; border 1px solid #e7e7e9; radius 50%; background #ffffff `color.neutral.0`; text Mona Sans 14/14 600, #0d0c22 `color.measured.ink`; transition color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), background-color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border-radius 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03); icon 16 x 16, #0d0c22 `color.measured.ink`; layers ::before rgb(255, 255, 255) 0px none 0; ::after rgba(0, 0, 0, 0) 1px none 0 |
| hover | border 1px solid #dbdbde |
| focus-visible | border 1px solid #dbdbde; outline 2px solid #f3afe4 `focusRing.measured.color`, offset 0px |
| pressed | border 1px solid #dbdbde |

![Icon button default](components/crops/profile-icon-btn-default.png) ![Icon button hover](components/crops/profile-icon-btn-hover.png) ![Icon button focus-visible](components/crops/profile-icon-btn-focus-visible.png) ![Icon button pressed](components/crops/profile-icon-btn-pressed.png)

#### Profile tab
A tab in the Work/Services/Reviews/Collections bar. Read as `profile-tab` on the designer profile page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 67.45 x 36; padding 0px 16px; radius 1e+07px; background #f8f7f4; text Mona Sans 14/15 600, #0d0c22 `color.measured.ink`; transition all 0.2s ease |
| hover | background #f5f3f0 |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px |
| pressed | background #f5f3f0 |

![Profile tab default](components/crops/profile-tab-default.png) ![Profile tab hover](components/crops/profile-tab-hover.png) ![Profile tab focus-visible](components/crops/profile-tab-focus-visible.png) ![Profile tab pressed](components/crops/profile-tab-pressed.png)

#### Work sort control
The "Recent Shots" dropdown over the work grid; its list was never opened. Read as `profile-sort` on the designer profile page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 143.22 x 40; padding 18px 35px 18px 18px; border 1px solid rgba(231, 231, 233, 0.9); radius 8px; background #ffffff `color.neutral.0`; shadow rgba(0, 0, 0, 0.01) 0px 2px 2px 0px; text Mona Sans 14/19 500, #0d0c22 `color.measured.ink`; transition color 0.2s ease; icon 10 x 10, #0d0c22 `color.measured.ink` |
| hover | shadow rgba(0, 0, 0, 0.03) 0px 4px 4px 0px |
| focus-visible | outline 1px solid #6e6d7a `color.measured.muted-2`, offset 1px |
| pressed | shadow rgba(0, 0, 0, 0.03) 0px 4px 4px 0px |

![Work sort control default](components/crops/profile-sort-default.png) ![Work sort control hover](components/crops/profile-sort-hover.png) ![Work sort control focus-visible](components/crops/profile-sort-focus-visible.png) ![Work sort control pressed](components/crops/profile-sort-pressed.png)

#### Work grid card
A shot card in the designer's work grid. Read as `profile-shot-card` on the designer profile page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 400 x 300; background transparent; text Mona Sans 14/20 500, #ffffff `color.neutral.0`; icon 11 x 9, #ffffff `color.neutral.0`; layers div::after.js-thumbnail-base.shot-thumbnail-base 400pxx300px; figure.js-thumbnail-placeholder.shot-thumbnail-placeholder 400.0x300.0 rgb(242, 241, 242); div.is-motion.shot-thumbnail-extras-icon 21.0x21.0 rgba(0, 0, 0, 0.2) 50%; div.shot-thumbnail-overlay 400.0x300.0 8px; a.btn2.btn2--secondary-alt 34.0x34.0 rgb(255, 255, 255) T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px  |
| focus-visible | layers div::after.js-thumbnail-base.shot-thumbnail-base 400pxx300px; figure.js-thumbnail-placeholder.shot-thumbnail-placeholder 400.0x300.0 rgb(242, 241, 242); div.is-motion.shot-thumbnail-extras-icon 21.0x21.0 rgba(0, 0, 0, 0.2) 50%; a.animated-target 0.0x0.0 2px solid rgb(243, 175, 228) offset 1px; div.shot-thumbnail-overlay 400.0x300.0 8px; a.btn2.btn2--secondary-alt 34.0x34.0 rgb(255, 255, 255) T:1px |

Child layers that carry the look: div::after 400pxx300px image linear-gradient(transparent 0%, transparent 8.1%, transparent 15.5%, rgba(0, 0, 0, 0.004) ; figure 400x300 background #f2f1f2; div 21x21 background rgba(0, 0, 0, 0.2) radius 50%.

![Work grid card default](components/crops/profile-shot-card-default.png) ![Work grid card hover](components/crops/profile-shot-card-hover.png) ![Work grid card focus-visible](components/crops/profile-shot-card-focus-visible.png) ![Work grid card pressed](components/crops/profile-shot-card-pressed.png)

### Designers directory

The /designers hiring directory: topic chips, filter dropdowns, and the freelancer cards — avatar, name, PRO+/SELECT badges, star rating, projects count, rate, location, response time, a four-image work strip and skill chips including the dark certified chip.

#### Directory title
The "Hire Top Freelance Designers" heading. Read as `dir-h1` on the designers directory page.

**Values (default).** size 1296 x 29; background transparent; text Mona Sans 24/29 700, #0d0c22 `color.measured.ink`.

![Directory title default](components/crops/dir-h1-default.png)

#### Topic chip
A Popular topic link under the directory heading. Read as `topic-chip` on the designers directory page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 96.16 x 31; padding 0px 16px; border 1px solid #e7e7e9; radius 1e+07px; background #ffffff `color.neutral.0`; text Mona Sans 12/12 400, #0d0c22 `color.measured.ink`; transition color 0.1s ease |
| hover | background #faf9fb |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px |
| pressed | background #faf9fb |

![Topic chip default](components/crops/topic-chip-default.png) ![Topic chip hover](components/crops/topic-chip-hover.png) ![Topic chip focus-visible](components/crops/topic-chip-focus-visible.png) ![Topic chip pressed](components/crops/topic-chip-pressed.png)

#### Filter control
A filter dropdown over the directory (Categories/Budget/Location/Rating/More); its list was never opened. Read as `filter-select` on the designers directory page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 115.89 x 35; padding 0px 34px 0px 14px; border 1px solid rgba(219, 218, 222, 0.9) `color.measured.field-border`; radius 8px; background #ffffff `color.neutral.0`; shadow rgba(6, 3, 24, 0.01) 0px 4px 4px 0px; text Mona Sans 12/12 500, #0d0c22 `color.measured.ink`; transition color 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), border 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), background-color 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), -webkit-box-shadow 0.2s cubic-bezier(0.34, 1.56, 0.64, 1); layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover, focus-visible, pressed | border 1px solid rgba(158, 158, 167, 0.7); shadow rgba(6, 3, 24, 0.03) 0px 4px 4px 0px |

![Filter control default](components/crops/filter-select-default.png) ![Filter control hover](components/crops/filter-select-hover.png) ![Filter control focus-visible](components/crops/filter-select-focus-visible.png) ![Filter control pressed](components/crops/filter-select-pressed.png)

#### Designer card
A freelancer card (resume-user-card): avatar, name, PRO+/SELECT badges, star rating, projects count, rate, location, response time, work strip and skill chips. Read as `designer-card` on the designers directory page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 1296 x 416.13; padding 28px; border 1px solid #f3f3f4; radius 8px; background #ffffff `color.neutral.0`; shadow rgba(18, 22, 25, 0.02) 0px 1px 10px 0px; text Mona Sans 18/28 600, #0d0c22 `color.measured.ink`; transition box-shadow 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out; icon 11 x 11, #0d0c22 `color.measured.ink` |
| hover, pressed | shadow rgba(0, 0, 0, 0.1) 0px 8px 25px 0px |

![Designer card default](components/crops/designer-card-default.png) ![Designer card hover](components/crops/designer-card-hover.png) ![Designer card focus-visible](components/crops/designer-card-focus-visible.png) ![Designer card pressed](components/crops/designer-card-pressed.png)

#### Designer name
The freelancer's display name on the card. Read as `designer-name` on the designers directory page.

**Wrong element.** The name filter's /LAB|STUDIO/ matched inside "available", so these are the "15 Services available" meta line's values, not a designer name. The selector is fixed in tools/capture/public/measure.mjs; the entry needs a recapture.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 153.55 x 28; background transparent; text Mona Sans 14/28 500, #3a3546 `color.measured.muted`; transition color 0.1s ease; icon 17 x 17, #3a3546 `color.measured.muted` |
| hover | text Mona Sans 14/28 500, #3d3d4e `dribbble.button.bg-hover`; icon 17 x 17, #3d3d4e `dribbble.button.bg-hover` |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px; layers a.user-card-profile__subheading-item.user-card-profile__subheading-link 153.5x28.0 2px solid rgb(243, 175, 228) offset 1px |
| pressed | text Mona Sans 14/28 500, #3d3d4e `dribbble.button.bg-hover`; icon 17 x 17, #3d3d4e `dribbble.button.bg-hover` |

![Designer name default](components/crops/designer-name-default.png) ![Designer name hover](components/crops/designer-name-hover.png) ![Designer name focus-visible](components/crops/designer-name-focus-visible.png) ![Designer name pressed](components/crops/designer-name-pressed.png)

#### SELECT badge
The SELECT/PRO+ membership chip on the card. Read as `badge-select` on the designers directory page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 20; padding 0px 5px; radius 4px; background #ecebf0; text Mona Sans 9/20 800, #524b63; transition color 0.1s ease |
| hover | background #d8d6d5 |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px |
| pressed | background #d8d6d5 |

![SELECT badge default](components/crops/badge-select-default.png) ![SELECT badge hover](components/crops/badge-select-hover.png) ![SELECT badge focus-visible](components/crops/badge-select-focus-visible.png) ![SELECT badge pressed](components/crops/badge-select-pressed.png)

#### Star rating
The 4.9 (158) star-rating figure. Read as `rating` on the designers directory page.

**Values (default).** size 71.45 x 28; background transparent; text Mona Sans 14/28 600, #0d0c22 `color.measured.ink`; icon 11 x 11, #0d0c22 `color.measured.ink`.

![Star rating default](components/crops/rating-default.png)

#### Designer meta
A projects-completed / response-time / services meta item. Read as `designer-meta` on the designers directory page.

**Values (default).** size 157.59 x 28; background transparent; text Mona Sans 14/28 500, #3a3546 `color.measured.muted`; icon 17 x 17, #3a3546 `color.measured.muted`.

![Designer meta default](components/crops/designer-meta-default.png)

#### Promoted tag
The small "Promoted" disclosure label. Read as `promoted-tag` on the designers directory page.

**Values (default).** size 57.91 x 28; background transparent; text Mona Sans 12/28 700, #98959f; transition color 0.1s ease-in-out.

![Promoted tag default](components/crops/promoted-tag-default.png)

#### Get-in-touch button
The dark hire pill on the card; measured never followed. Read as `designer-cta` on the designers directory page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 117.88 x 40; padding 0px 20px; border 1px solid #0d0c22 `color.measured.ink`; radius 1e+07px; background #0d0c22 `color.measured.ink`; text Mona Sans 13/13 600, #ffffff `color.neutral.0`; transition color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), background-color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border-radius 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03); layers ::before rgb(13, 12, 34) 0px none 0; ::after rgba(0, 0, 0, 0) 1px none 0 |
| hover | border 1px solid #3d3d4e `dribbble.button.bg-hover`; background #3d3d4e `dribbble.button.bg-hover` |
| focus-visible | border 1px solid #3d3d4e `dribbble.button.bg-hover`; background #3d3d4e `dribbble.button.bg-hover`; outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px |
| pressed | border 1px solid #3d3d4e `dribbble.button.bg-hover`; background #3d3d4e `dribbble.button.bg-hover` |

![Get-in-touch button default](components/crops/designer-cta-default.png) ![Get-in-touch button hover](components/crops/designer-cta-hover.png) ![Get-in-touch button focus-visible](components/crops/designer-cta-focus-visible.png) ![Get-in-touch button pressed](components/crops/designer-cta-pressed.png)

#### Bookmark icon button
The icon-only save/bookmark button on the card; measured never pressed. Read as `bookmark-btn` on the designers directory page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; border 1px solid #e7e7e9; radius 50%; background #ffffff `color.neutral.0`; text Mona Sans 13/13 600, #0d0c22 `color.measured.ink`; transition color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), background-color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border-radius 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03); icon 16 x 16, #0d0c22 `color.measured.ink`; layers ::before rgb(255, 255, 255) 0px none 0; ::after rgba(0, 0, 0, 0) 1px none 0 |
| hover | border 1px solid #dbdbde |
| focus-visible | border 1px solid #dbdbde; outline 2px solid #f3afe4 `focusRing.measured.color`, offset 0px |
| pressed | border 1px solid #dbdbde |

![Bookmark icon button default](components/crops/bookmark-btn-default.png) ![Bookmark icon button hover](components/crops/bookmark-btn-hover.png) ![Bookmark icon button focus-visible](components/crops/bookmark-btn-focus-visible.png) ![Bookmark icon button pressed](components/crops/bookmark-btn-pressed.png)

#### Skill chip, dark
The dark certified chip ("Webflow Expert"). Read as `skill-chip-dark` on the designers directory page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 136.42 x 27; padding 0px 16px; border 1px solid #3a3546 `color.measured.muted`; radius 1e+07px; background #3a3546 `color.measured.muted`; text Mona Sans 11/14 700, #ffffff `color.neutral.0`; transition color 0.1s ease; icon 12 x 12, #ffffff `color.neutral.0` |
| hover | background #655c7a |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px |
| pressed | background #655c7a |

![Skill chip, dark default](components/crops/skill-chip-dark-default.png) ![Skill chip, dark hover](components/crops/skill-chip-dark-hover.png) ![Skill chip, dark focus-visible](components/crops/skill-chip-dark-focus-visible.png) ![Skill chip, dark pressed](components/crops/skill-chip-dark-pressed.png)

#### Skill chip
A light skill tag on the card. Read as `skill-chip` on the designers directory page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 95.78 x 31; padding 0px 16px; border 1px solid #e7e7e9; radius 1e+07px; background #ffffff `color.neutral.0`; text Mona Sans 12/12 400, #0d0c22 `color.measured.ink`; transition color 0.1s ease |
| hover | background #faf9fb |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px |
| pressed | background #faf9fb |

![Skill chip default](components/crops/skill-chip-default.png) ![Skill chip hover](components/crops/skill-chip-hover.png) ![Skill chip focus-visible](components/crops/skill-chip-focus-visible.png) ![Skill chip pressed](components/crops/skill-chip-pressed.png)

### Jobs board

The /jobs listings: posting cards with role, company, logo and remote/type tags, plus the apply action (measured, never followed).

#### Jobs title
The jobs-board heading. Read as `jobs-h1` on the jobs board page.

**Values (default).** size 732 x 152; background transparent; text Source Serif Pro 72/76 400, #0d0c22 `color.measured.ink`.

![Jobs title default](components/crops/jobs-h1-default.png)

#### Job card
A posting card: logo, role, company, location/type tags. Read as `job-card` on the jobs board page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 912 x 104; padding 24px; border 1px solid #f1f1f1; radius 8px; background #ffffff `color.neutral.0`; text Mona Sans 15/15 500, #0d0c22 `color.measured.ink`; transition background-color 0.2s ease; icon 14 x 22, #0d0c22 `color.measured.ink` |
| hover, pressed | shadow rgba(243, 243, 244, 0.65) 0px 8px 15px 0px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Job card default](components/crops/job-card-default.png) ![Job card hover](components/crops/job-card-hover.png) ![Job card pressed](components/crops/job-card-pressed.png)

#### Job title
A role title on a posting (h4.job-board-job-title inside li.job-list-item). Read as `job-title` on the jobs board page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 250.09 x 36; background transparent; text Mona Sans 22/36 500, #0d0c22 `color.measured.ink` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Job title default](components/crops/job-title-default.png) ![Job title hover](components/crops/job-title-hover.png) ![Job title pressed](components/crops/job-title-pressed.png)

#### Job tag
A remote/contract/location tag on the posting (span.location inside li.job-list-item). Read as `job-tag` on the jobs board page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 67.78 x 28; background transparent; text Mona Sans 12/28 700, #3d3d4e `dribbble.button.bg-hover`; icon 14 x 22, #0d0c22 `color.measured.ink` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Job tag default](components/crops/job-tag-default.png) ![Job tag hover](components/crops/job-tag-hover.png) ![Job tag pressed](components/crops/job-tag-pressed.png)

#### Apply button
The apply action; measured never followed. Read as `job-apply` on the jobs board page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 105.81 x 40; padding 0px 20px; border 1px solid #e7e7e9; radius 1e+07px; background #ffffff `color.neutral.0`; text Mona Sans 13/13 600, #0d0c22 `color.measured.ink`; transition color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), background-color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border-radius 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03); layers ::before rgb(255, 255, 255) 0px none 0; ::after rgba(0, 0, 0, 0) 1px none 0 |
| hover | border 1px solid #dbdbde |
| focus-visible | border 1px solid #dbdbde; outline 2px solid #f3afe4 `focusRing.measured.color`, offset 0px |
| pressed | border 1px solid #dbdbde |

![Apply button default](components/crops/job-apply-default.png) ![Apply button hover](components/crops/job-apply-hover.png) ![Apply button focus-visible](components/crops/job-apply-focus-visible.png) ![Apply button pressed](components/crops/job-apply-pressed.png)

### Search

The /search results page: the query heading, dictionary-style definition, Related links, the category filter tabs, the Popular sort and Filters controls, and the results shot-card grid.

#### Search title
The query heading ("Logo"). Read as `search-h1` on the search page.

**Values (default).** size 1408 x 38; background transparent; text Mona Sans 32/38 700, #0d0c22 `color.measured.ink`.

![Search title default](components/crops/search-h1-default.png)

#### Search description
The dictionary-style definition line under the query. Read as `search-desc` on the search page.

**Values (default).** size 732 x 56; padding 0px 16px; background transparent; text Mona Sans 16/28 400, #655c7a.

![Search description default](components/crops/search-desc-default.png)

#### Related link
A Related: tag link under the definition. Read as `related-link` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 57.52 x 17; background transparent; text Mona Sans 14/20 400, #0d0c22 `color.measured.ink`; transition color 0.1s ease |
| hover | text Mona Sans 14/20 400, #3d3d4e `dribbble.button.bg-hover` |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px; layers a 57.5x17.0 2px solid rgb(243, 175, 228) offset 1px |
| pressed | text Mona Sans 14/20 400, #3d3d4e `dribbble.button.bg-hover` |

![Related link default](components/crops/related-link-default.png) ![Related link hover](components/crops/related-link-hover.png) ![Related link focus-visible](components/crops/related-link-focus-visible.png) ![Related link pressed](components/crops/related-link-pressed.png)

#### Filter tab
A category tab over the results grid. Read as `filter-tab` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 90 x 36; padding 0px 16px; radius 1e+07px; background #f8f7f4; text Mona Sans 14/20 600, #0d0c22 `color.measured.ink`; transition color 0.1s ease |
| hover | background #f5f3f0; transition all 0.2s ease |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px |
| pressed | background #f5f3f0; transition all 0.2s ease |

![Filter tab default](components/crops/filter-tab-default.png) ![Filter tab hover](components/crops/filter-tab-hover.png) ![Filter tab focus-visible](components/crops/filter-tab-focus-visible.png) ![Filter tab pressed](components/crops/filter-tab-pressed.png)

#### Sort control
The "Popular" sort dropdown; its list was never opened. Read as `filter-sort` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 115 x 40; padding 18px 35px 18px 18px; border 1px solid rgba(231, 231, 233, 0.9); radius 8px; background #ffffff `color.neutral.0`; shadow rgba(0, 0, 0, 0.01) 0px 2px 2px 0px; text Mona Sans 14/19 500, #0d0c22 `color.measured.ink`; transition color 0.2s ease; icon 10 x 10, #0d0c22 `color.measured.ink` |
| hover | shadow rgba(0, 0, 0, 0.03) 0px 4px 4px 0px |
| focus-visible | outline 1px solid #6e6d7a `color.measured.muted-2`, offset 1px |
| pressed | shadow rgba(0, 0, 0, 0.03) 0px 4px 4px 0px |

![Sort control default](components/crops/filter-sort-default.png) ![Sort control hover](components/crops/filter-sort-hover.png) ![Sort control focus-visible](components/crops/filter-sort-focus-visible.png) ![Sort control pressed](components/crops/filter-sort-pressed.png)

#### Filters button
The Filters toggle at the end of the tab row; measured, its panel was never opened. Read as `filters-btn` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 98.45 x 40; padding 10px 20px; border 1px solid #e7e7e9; radius 1e+07px; background #ffffff `color.neutral.0`; text Mona Sans 13/16 600, #0d0c22 `color.measured.ink`; transition color 0.2s ease; icon 13 x 13, #0d0c22 `color.measured.ink` |
| hover | border 1px solid #dbdbde |
| focus-visible | border 1px solid #dbdbde; outline 1px solid #6e6d7a `color.measured.muted-2`, offset 1px |
| pressed | border 1px solid #dbdbde |

![Filters button default](components/crops/filters-btn-default.png) ![Filters button hover](components/crops/filters-btn-hover.png) ![Filters button focus-visible](components/crops/filters-btn-focus-visible.png) ![Filters button pressed](components/crops/filters-btn-pressed.png)

#### Grid shot card
A shot card in the results grid: image, avatar + name, PRO+ chip, like and view counts. Read as `grid-shot-card` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 297 x 254.75; background transparent; text Mona Sans 14/20 500, #ffffff `color.neutral.0`; icon 16 x 16, #0d0c22 `color.measured.ink`; layers div::after.js-thumbnail-base.shot-thumbnail-base 297pxx222.75px; figure.js-thumbnail-placeholder.shot-thumbnail-placeholder 297.0x222.8 rgb(255, 255, 255); div.shot-thumbnail-overlay 297.0x222.8 8px; a.btn2.btn2--secondary-alt 34.0x34.0 rgb(255, 255, 255) T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, 255, 255) 50%; a::before |
| focus-visible | layers div::after.js-thumbnail-base.shot-thumbnail-base 297pxx222.75px; figure.js-thumbnail-placeholder.shot-thumbnail-placeholder 297.0x222.8 rgb(255, 255, 255); a.shot-thumbnail-link.dribbble-link 297.0x222.8 2px solid rgb(243, 175, 228) offset 1px; div.shot-thumbnail-overlay 297.0x222.8 8px; a.btn2.btn2--secondary-alt 34.0x34.0 rgb(255, 255, 255) T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 2 |

Child layers that carry the look: div::after 297pxx222.75px image linear-gradient(transparent 0%, transparent 8.1%, transparent 15.5%, rgba(0, 0, 0, 0.004) ; figure 297x222.8 background #ffffff `color.neutral.0`; div 297x222.8 image linear-gradient(transparent 62%, rgba(0, 0, 0, 0.004) 63.94%, rgba(0, 0, 0, 0.016) 65.89%, radius 8px.

![Grid shot card default](components/crops/grid-shot-card-default.png) ![Grid shot card hover](components/crops/grid-shot-card-hover.png) ![Grid shot card focus-visible](components/crops/grid-shot-card-focus-visible.png) ![Grid shot card pressed](components/crops/grid-shot-card-pressed.png)

### Log in and sign up

The auth boundary pages, measured but never submitted: the split-layout Welcome-back login card with the Google SSO button and email field, and the signup card.

#### Login card
The "Welcome back" form card (auth-layout__content) on the split layout; never filled or submitted. The Continue-with-Google action is a Google-rendered GSI element — hidden as a third-party prompt like every other overlay, never answered, so it is documented as a gap rather than measured. Read as `login-card` on the log in page.

**Values (default).** size 1024 x 804; padding 0px 48px; background transparent; text Mona Sans 24/29 700, #0d0c22 `color.measured.ink`; icon 76 x 30, #0d0c22 `color.measured.ink`; layers div 0.0x0.0 1e+07px; div.nsm7Bb-HzV7m-LgbsSe.TzA9Ye-LgbsSe 0.0x0.0 rgb(255, 255, 255) T:1px solid rgb(218, 220, 224) / R:1px solid rgb(218, 220, 224) / B:1px solid rgb(218, 220, 224) / L:1px solid rgb(218, 220, 224) 20px; input.input2.input2--large 0.0x0.0 rgb(255, 255, 255) T:1px solid rgba(219, 218, 222, 0.9) / R:1px solid rgba(219, 218, 222, 0.9) / B:1px solid rgba(219, 218, 222, 0.9) / L:1px s.

Child layers that carry the look: div 0x0 image linear-gradient(-90deg, #f3f3f4 8%, #faf9fb 28%, #f3f3f4 70%) radius 1e+07px; div 0x0 background #ffffff `color.neutral.0` border 1px solid #dadce0 radius 20px; input 0x0 background #ffffff `color.neutral.0` border 1px solid rgba(219, 218, 222, 0.9) `color.measured.field-border` radius 8px.

![Login card default](components/crops/login-card-default.png)

#### Email field
The "Enter email or username" input; sample text was typed and deleted, nothing sent. Read as `email-field` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 310 x 47; padding 0px 16px; border 1px solid rgba(219, 218, 222, 0.9) `color.measured.field-border`; radius 8px; background #ffffff `color.neutral.0`; text Mona Sans 16/16 400, #0d0c22 `color.measured.ink`; transition color 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), border 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), background-color 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), -webkit-box-shadow 0.2s cubic-bezier(0.34, 1.56, 0.64, 1); placeholder #98959f |
| focused, filled | border 1px solid rgba(158, 158, 167, 0.7); shadow rgba(6, 3, 24, 0.03) 0px 4px 4px 0px |

![Email field default](components/crops/email-field-default.png) ![Email field focused](components/crops/email-field-focused.png) ![Email field filled](components/crops/email-field-filled.png)

#### Continue button
The dark Continue submit; measured, never pressed (a press would submit). Read as `continue-btn` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 310 x 48; padding 0px 24px; border 1px solid #0d0c22 `color.measured.ink`; radius 1e+07px; background #0d0c22 `color.measured.ink`; text Mona Sans 14/14 600, #ffffff `color.neutral.0`; transition color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), background-color 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), border-radius 0.05s cubic-bezier(0.32, 0, 0.59, 0.03), padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03); layers ::before rgb(13, 12, 34) 0px none 0; ::after rgba(0, 0, 0, 0) 1px none 0 |
| hover | border 1px solid #3d3d4e `dribbble.button.bg-hover`; background #3d3d4e `dribbble.button.bg-hover` |
| focus-visible | border 1px solid #3d3d4e `dribbble.button.bg-hover`; background #3d3d4e `dribbble.button.bg-hover`; outline 2px solid #f3afe4 `focusRing.measured.color`, offset 0px |
| pressed | border 1px solid #3d3d4e `dribbble.button.bg-hover`; background #3d3d4e `dribbble.button.bg-hover` |

![Continue button default](components/crops/continue-btn-default.png) ![Continue button hover](components/crops/continue-btn-hover.png) ![Continue button focus-visible](components/crops/continue-btn-focus-visible.png) ![Continue button pressed](components/crops/continue-btn-pressed.png)

#### Auth link
A Terms / Privacy / Sign-up link under the card actions. Read as `auth-link` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 34.22 x 15; background transparent; text Mona Sans 12/15 400, #7b7194 `dribbble.nav.link-hover`; transition color 0.1s ease |
| hover | text Mona Sans 12/15 400, #524b63 |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px; layers a 34.2x15.0 2px solid rgb(243, 175, 228) offset 1px |
| pressed | text Mona Sans 12/15 400, #524b63 |

![Auth link default](components/crops/auth-link-default.png) ![Auth link hover](components/crops/auth-link-hover.png) ![Auth link focus-visible](components/crops/auth-link-focus-visible.png) ![Auth link pressed](components/crops/auth-link-pressed.png)

#### Auth illustration panel
The painted half of the split layout (a shot fills it, credited bottom-right). Read as `auth-art` on the log in page.

**Values (default).** size 400 x 900; background transparent; text Mona Sans 14/17 400, #ffffff `color.neutral.0`.

![Auth illustration panel default](components/crops/auth-art-default.png)

#### Signup card
The "Welcome to Dribbble" form card; never filled or submitted. Read as `signup-card` on the sign up page.

**Values (default).** size 1024 x 804; padding 0px 48px; background transparent; text Mona Sans 24/29 700, #0d0c22 `color.measured.ink`; icon 76 x 30, #0d0c22 `color.measured.ink`; layers div 310.0x40.0 1e+07px; input.input2.input2--large 310.0x47.0 rgb(255, 255, 255) T:1px solid rgba(219, 218, 222, 0.9) / R:1px solid rgba(219, 218, 222, 0.9) / B:1px solid rgba(219, 218, 222, 0.9) / L:1px solid rgba(219, 218, 222, 0.9) 8px; button.btn2.btn2--medium 310.0x48.0 rgb(13, 12, 34) T:1px solid rgb(13, 12, 34) / R:1px solid rgb(13, 12, 34) / B:1px solid rgb(13, 12, 34) / L:1px solid rgb(13.

Child layers that carry the look: div 310x40 image linear-gradient(-90deg, #f3f3f4 8%, #faf9fb 28%, #f3f3f4 70%) radius 1e+07px; input 310x47 background #ffffff `color.neutral.0` border 1px solid rgba(219, 218, 222, 0.9) `color.measured.field-border` radius 8px; button 310x48 background #0d0c22 `color.measured.ink` border 1px solid #0d0c22 `color.measured.ink` radius 1e+07px.

![Signup card default](components/crops/signup-card-default.png)

#### Signup email field
The "Enter email address" input; focused only, never filled or submitted. Read as `signup-field` on the sign up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 310 x 47; padding 0px 16px; border 1px solid rgba(219, 218, 222, 0.9) `color.measured.field-border`; radius 8px; background #ffffff `color.neutral.0`; text Mona Sans 16/16 400, #0d0c22 `color.measured.ink`; transition color 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), border 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), background-color 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), -webkit-box-shadow 0.2s cubic-bezier(0.34, 1.56, 0.64, 1); placeholder #98959f |
| focused | border 1px solid rgba(158, 158, 167, 0.7); shadow rgba(6, 3, 24, 0.03) 0px 4px 4px 0px |

![Signup email field default](components/crops/signup-field-default.png) ![Signup email field focused](components/crops/signup-field-focused.png)

### Stories (blog)

The /stories editorial index: story cards with category tags.

#### Stories title
The blog's heading or featured story title. Read as `stories-h1` on the stories page.

**Values (default).** size 843.19 x 112; background transparent; text Mona Sans 48/56 700, #0d0c22 `color.measured.ink`.

![Stories title default](components/crops/stories-h1-default.png)

#### Story card
An article card in the blog index. Read as `story-card` on the stories page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 808.61 x 86.19; background transparent; text Mona Sans 36/43.2 500, #0d0c22 `color.measured.ink`; transition color 0.1s ease |
| hover | text Mona Sans 36/43.2 500, #ea64d9 |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px; layers a 808.6x86.2 2px solid rgb(243, 175, 228) offset 1px |
| pressed | text Mona Sans 36/43.2 500, #ea64d9 |

![Story card default](components/crops/story-card-default.png) ![Story card hover](components/crops/story-card-hover.png) ![Story card focus-visible](components/crops/story-card-focus-visible.png) ![Story card pressed](components/crops/story-card-pressed.png)

#### Story tag
A category link on the stories index (ul.blog-cat: Interviews, Inspiration, Process, Community). Read as `story-tag` on the stories page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 281.81 x 25; padding 2px 0px; background transparent; text Mona Sans 14/21 500, #0d0c22 `color.measured.ink`; transition color 0.1s ease |
| hover | text Mona Sans 14/21 500, #3d3d4e `dribbble.button.bg-hover` |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px; layers a 281.8x25.0 2px solid rgb(243, 175, 228) offset 1px |
| pressed | text Mona Sans 14/21 500, #3d3d4e `dribbble.button.bg-hover` |

![Story tag default](components/crops/story-tag-default.png) ![Story tag hover](components/crops/story-tag-hover.png) ![Story tag focus-visible](components/crops/story-tag-focus-visible.png) ![Story tag pressed](components/crops/story-tag-pressed.png)

### Footer

The footer: script wordmark, link columns, social icons and the legal row.

#### Footer
The footer: script wordmark, link columns (For designers/Hire designers/Company), social icons and the legal row. Read as `footer` on the home page.

**Values (default).** size 1440 x 508; background #ffffff `color.neutral.0`; text Mona Sans 14/28 500, #0d0c22 `color.measured.ink`; transition opacity 0.4s ease-in-out; icon 104 x 30, #0d0c22 `color.measured.ink`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A text link in the footer bottom bar (For designers / Hire talent / …); the category cards above it are measured separately. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 90.09 x 17; background transparent; text Mona Sans 14/20 600, #0d0c22 `color.measured.ink`; transition color 0.1s ease |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px; layers a.site-footer__link 90.1x17.0 2px solid rgb(243, 175, 228) offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social icon
A social-icon link in the footer. Read as `social-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 18 x 18; background transparent; text Mona Sans 16/28 400, #0d0c22 `color.measured.ink`; transition color 0.1s ease; icon 18 x 18, #0d0c22 `color.measured.ink` |
| focus-visible | outline 2px solid #f3afe4 `focusRing.measured.color`, offset 1px; layers a.site-footer__social-link 18.0x18.0 2px solid rgb(243, 175, 228) offset 1px |

![Social icon default](components/crops/social-icon-default.png) ![Social icon hover](components/crops/social-icon-hover.png) ![Social icon focus-visible](components/crops/social-icon-focus-visible.png) ![Social icon pressed](components/crops/social-icon-pressed.png)

### Mobile (390 wide)

The surface at phone width: the compact header, the menu toggle and panel, the stacked hero and search.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 58; background transparent; text Mona Sans 14/14 600, #ffffff `color.neutral.0`; transition opacity 0.4s ease-in-out; icon 89 x 25, #060318 `color.measured.link`; layers div.site-nav__dark-overlay 390.0x844.0 rgba(0, 0, 0, 0.5); div::before.site-nav__wrapper 390pxx58px rgb(255, 255, 255); span 24.0x3.0 rgb(6, 3, 24) 1e+07px; span 17.8x3.0 rgb(6, 3, 24) 1e+07px; span 12.0x3.0 rgb(6, 3, 24) 1e+07px; div.site-nav-search.site-nav-search--nav 0.0x0.0 rgb(255, 255, 255).

Child layers that carry the look: div 390x844 background rgba(0, 0, 0, 0.5); div::before 390pxx58px background #ffffff `color.neutral.0`; span 24x3 background #060318 `color.measured.link` radius 1e+07px.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The header menu toggle. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 36 x 29; padding 6px; background transparent; text Arial 13.33/normal 400, #000000 `color.neutral.1000`; layers span 24.0x3.0 rgb(6, 3, 24) 1e+07px; span 17.8x3.0 rgb(6, 3, 24) 1e+07px; span 12.0x3.0 rgb(6, 3, 24) 1e+07px.

Child layers that carry the look: span 24x3 background #060318 `color.measured.link` radius 1e+07px; span 17.8x3 background #060318 `color.measured.link` radius 1e+07px; span 12x3 background #060318 `color.measured.link` radius 1e+07px.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The header menu panel opened by its own toggle. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 319; background transparent; text Mona Sans 18/22 700, #060318 `color.measured.link`; transition opacity 0.25s ease-out, visibility 0.25s ease-out; icon 20 x 20, #060318 `color.measured.link`; layers div.site-nav-main__wrapper 390.0x319.0 rgb(255, 255, 255) T:1px solid rgb(231, 231, 233); a::after.site-nav-main__link 9pxx8px; ul.site-nav-sub 326.0x0.0 rgb(255, 255, 255); li::after.site-nav-sub__divider 326pxx1px rgb(216, 214, 213); a::after.site-nav-main__link 9pxx8px; ul.site-nav-sub.site-nav-sub--wide-format 326.0x0.0 rgb(255, 255, 255).

Child layers that carry the look: div 390x319 background #ffffff `color.neutral.0` border 1px solid #e7e7e9; a::after 9pxx8px image url(data:…); ul 326x0 background #ffffff `color.neutral.0`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 333 x 64.78; background transparent; text Mona Sans 27/32.4 600, #0d0c22 `color.measured.ink`.

![Mobile headline default](components/crops/m-hero-default.png)

#### Mobile search field
Read as `m-search` on the home page at 390 wide.

**Wrong element.** The union's `a[href*="/search"]` matched first, so this is the "dashboard" tag chip, not the search field. The selector is fixed in tools/capture/public/measure.mjs; the entry needs a recapture.

**Values (default).** size 98.48 x 31; padding 0px 16px; border 1px solid #e7e7e9; radius 1e+07px; background #ffffff `color.neutral.0`; text Mona Sans 13/13 400, #0d0c22 `color.measured.ink`; transition color 0.1s ease.

![Mobile search field default](components/crops/m-search-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the script Dribbble wordmark, the Google SSO glyph, the heart/eye/bookmark glyphs, the PRO badges and product illustrations) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Dribbble's product — posting and editing shots, following designers, liking and saving, the full personalized feed, messages, project briefs, hiring checkout and account settings — lives behind sign-in and was never reached. The signed-out feed on /shots/popular paints a single teaser card then a Sign-up-to-continue wall: the wall was measured as a component and never followed. Designer profiles, the designers directory, the jobs board, search, stories and the auth pages paint fully signed out.

### Pages

- **The feed beyond the wall.** The signed-out shot feed ends at the Sign-up-to-continue pill — a product boundary, not a capture failure; the page height does not grow on scroll.
- **Posting, following, liking, saving and hiring flows.** Every Follow, Get-in-touch, Apply, Post-a-job and brief CTA was measured, never followed or submitted.
- **The auth flows.** /session/new and /signup were captured as cards; fields were focused (sample text typed and deleted on the login email field) and the forms were never submitted, so the OAuth consent, verification and onboarding steps are uncaptured.
- **Individual designer and shot pages** were sampled (one profile, one shot); the catalog is huge and representative, not exhaustive.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover) so no real press ever ran; a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **Opened filter dropdowns** (Categories/Budget/Location/Rating/More, Popular sort, Filters panel, the Shots scope selector) were measured as controls but never opened — opening several fires navigation or panels the kit did not chase.

### Themes

dribbble.com paints one theme: light. No product dark mode is offered or declared; the only dark CSS scope in the bundles (`body.dark`, `body[data-theme='dark']`) re-binds the third-party Algolia autocomplete variables and is kept in raw/css-vars.json as evidence. The `dark` set in tokens.json names the ink surfaces the light page paints (the dark pills and the certified chip), in the same sense other packages record dark islands — not a user toggle.

### Fonts

- **Mona Sans** (the whole product stack, served via the Fontshare API stylesheet), **Source Serif 4** and **IBM Plex Mono** (served on the newer surfaces via Google Fonts) are the served faces; the style guide falls back to system sans.

### Screenshots

- Shot thumbnails, designer avatars and names, agency logos, story art and the Dribbble wordmark in the screenshots are the product's published public content — public designer names, handles and avatars are allowed; no private contact data is included.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Shot artwork, marketing copy, job descriptions and story text are the product's content; only frames and components were measured.
