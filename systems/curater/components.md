# Curater components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from curater.org on 2026-11-12, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, submitted or downloaded; the search field and mobile controls were toggled locally, and hover/focus/pressed states were forced. The 'Log in or sign up', 'Sign in / Create account', Google SSO, Save and TasteScope controls were measured, never followed or pressed. The feed is an inner scroll area — the desktop full-page capture is bounded at the first 27,850px (57,550px on mobile), a documented boundary.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (47 components, 111 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (108 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every page paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Feed | `/feed` | [default](screenshots/feed-light-default.png), [full](screenshots/feed-light-full.png) |
| TasteScope | `/taste` | [default](screenshots/taste-light-default.png), [full](screenshots/taste-light-full.png) |
| Curation | `/curation/qDNMdxe5` | [default](screenshots/curation-light-default.png), [full](screenshots/curation-light-full.png) |
| Profile | `/ravi` | [default](screenshots/profile-light-default.png), [full](screenshots/profile-light-full.png) |
| Terms | `/terms` | [default](screenshots/terms-light-default.png), [full](screenshots/terms-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Feed, phone | `/feed` | [default](screenshots/mobile-feed-light-default.png), [full](screenshots/mobile-feed-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Search field | feed | the search toggle clicked locally; it stays open while the pointer is over it | [search-field](#search-field) |
| Mobile menu | home, phone width | the mobile menu button; the rail is always visible | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) |
| The signed-in app | past 'Log in or sign up' / SSO | the controls were measured, never followed | boundary; see Gaps |
| /feed full page | feed | 27,850px inner-scroll height (57,550px mobile) | bounded — documented boundary |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 21 components were given a real keyboard focus. 18 draw an outline ring: `nav-button` (2px solid oklch(0.871 0.006 286.286), offset 2px), `settings-btn` (2px solid oklch(0.871 0.006 286.286), offset 2px), `trend-card` (on a child: 2px solid oklch(0.871 0.006 286.286) offset 2px), `tab-button` (2px solid oklch(0.871 0.006 286.286), offset 2px), `search-toggle` (2px solid oklch(0.871 0.006 286.286), offset 2px), `login-btn` (2px solid oklch(0.871 0.006 286.286), offset 2px), `theme-card` (2px solid oklch(0.871 0.006 286.286), offset 2px), `curator-label` (2px solid oklch(0.871 0.006 286.286), offset 2px), `title-link` (2px solid oklch(0.871 0.006 286.286), offset 2px), `save-btn` (2px solid oklch(0.871 0.006 286.286), offset 2px), `album-link` (2px solid oklch(0.871 0.006 286.286), offset 2px), `back-btn` (2px solid oklch(0.871 0.006 286.286), offset 2px), `options-btn` (2px solid oklch(0.871 0.006 286.286), offset 2px), `sso-btn` (on a child: 2px solid oklch(0.871 0.006 286.286) offset 2px), `similar-btn` (2px solid oklch(0.871 0.006 286.286), offset 2px), `profile-item` (on a child: 2px solid oklch(0.871 0.006 286.286) offset 2px), `item-menu` (2px solid oklch(0.871 0.006 286.286), offset 2px), `m-nav-button` (2px solid oklch(0.871 0.006 286.286), offset 2px). The other 3 show no measured change: `signin-btn`, `tastescope-btn`, `m-signin-btn`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.19, 1, 0.22, 1)` | all, background-color, color, opacity, transform | card-thumb, curator-label, item-menu, m-signin-btn, nav-button, nav-button-active, save-btn, search-field and more |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Theme card](#theme-card) | 224 x 271 | - | - | transparent | none | 0 |
| [Trend card](#trend-card) | 544 x 492.39 | 1px solid #e8e7e7 | 24px | #ffffff `color.tailwind.white` | rgba(0, 0, 0, 0.02) 0px 14px 54px 0px | 80px 72px |
| [Profile item](#profile-item) | 268.27 x 380.27 | - | - | transparent | none | 0 |
| [Media tile](#media-tile) | 1080 x 540 | - | 20px | transparent | none | 0 |
| [Album tile](#album-tile) | 540 x 540 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The 48px desktop rail (48x328) and the header controls shared across the app: round 48px icon buttons that fill #f2f2f2 when their page is active, the 20px search toggle that reveals the 170x30 search field, the 64x40 feed tabs and the 'Log in or sign up' link.

#### Nav rail
The 48px-wide vertical icon rail (Home / Taste / Notifications / Profile / Create / Settings). Read as `nav-rail` on the home page.

**Values (default).** size 48 x 328; background transparent; text ABCDiatype 16/24 400, oklch(0.141 0.005 285.823); icon 20 x 20, oklch(0.552 0.016 285.938); layers div._newDigestIndicator_1psr6_136 8.0x8.0 rgb(226, 0, 0) 9999px.

Child layers that carry the look: div 8x8 background #e20000 `color.curater.red` radius 9999px.

![Nav rail default](components/crops/nav-rail-default.png)

#### Nav button
A 48x48 rail icon button (Home); measured, never followed. Read as `nav-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 48 x 48; radius 9999px; background transparent; text ABCDiatype 16/24 400, oklch(0.552 0.016 285.938); transition background-color 0.15s cubic-bezier(0.19, 1, 0.22, 1), color 0.15s cubic-bezier(0.19, 1, 0.22, 1); icon 20 x 20, oklch(0.552 0.016 285.938); layers div._newDigestIndicator_1psr6_136 8.0x8.0 rgb(226, 0, 0) 9999px |
| hover | background oklch(0.967 0.001 286.375); text ABCDiatype 16/24 400, oklch(0.141 0.005 285.823); icon 20 x 20, oklch(0.141 0.005 285.823); layers none |
| focus-visible | outline 2px solid oklch(0.871 0.006 286.286), offset 2px; layers a._navButton_1psr6_88 48.0x48.0 2px solid oklch(0.871 0.006 286.286) offset 2px 9999px; div._newDigestIndicator_1psr6_136 8.0x8.0 rgb(226, 0, 0) 9999px |
| pressed | background oklch(0.967 0.001 286.375); text ABCDiatype 16/24 400, oklch(0.141 0.005 285.823); icon 20 x 20, oklch(0.141 0.005 285.823); layers none |

Child layers that carry the look: div 8x8 background #e20000 `color.curater.red` radius 9999px.

![Nav button default](components/crops/nav-button-default.png) ![Nav button hover](components/crops/nav-button-hover.png) ![Nav button focus-visible](components/crops/nav-button-focus-visible.png) ![Nav button pressed](components/crops/nav-button-pressed.png)

#### Nav button, active
The active rail button (the .active sibling) — its highlighted state. Read as `nav-button-active` on the feed page.

**Values (default).** size 48 x 48; radius 9999px; background #f2f2f2 `color.curater.background`; text ABCDiatype 16/24 400, oklch(0.141 0.005 285.823); transition background-color 0.15s cubic-bezier(0.19, 1, 0.22, 1), color 0.15s cubic-bezier(0.19, 1, 0.22, 1); icon 20 x 20, oklch(0.141 0.005 285.823).

![Nav button, active default](components/crops/nav-button-active-default.png)

#### Settings button
The 48x48 settings gear at the rail foot; measured, never followed. Read as `settings-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 48 x 48; radius 9999px; background transparent; text ABCDiatype 16/24 400, oklch(0.552 0.016 285.938); transition background-color 0.15s cubic-bezier(0.19, 1, 0.22, 1), color 0.15s cubic-bezier(0.19, 1, 0.22, 1); icon 20 x 20, oklch(0.552 0.016 285.938) |
| hover | background oklch(0.967 0.001 286.375); text ABCDiatype 16/24 400, oklch(0.141 0.005 285.823); icon 20 x 20, oklch(0.141 0.005 285.823) |
| focus-visible | outline 2px solid oklch(0.871 0.006 286.286), offset 2px; layers button._settingsButton_1psr6_89 48.0x48.0 2px solid oklch(0.871 0.006 286.286) offset 2px 9999px |
| pressed | background oklch(0.967 0.001 286.375); text ABCDiatype 16/24 400, oklch(0.141 0.005 285.823); icon 20 x 20, oklch(0.141 0.005 285.823) |

![Settings button default](components/crops/settings-btn-default.png) ![Settings button hover](components/crops/settings-btn-hover.png) ![Settings button focus-visible](components/crops/settings-btn-focus-visible.png) ![Settings button pressed](components/crops/settings-btn-pressed.png)

#### Sign-in button
"Sign in or create account" — the 259x58 auth CTA; measured, never followed. Read as `signin-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 259.45 x 58; padding 16px 24px; border 1px solid oklch(0.95 0.004 286.32); radius 9999px; background oklch(1 0 0); shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text ABCDiatype 16/24 500, oklch(0.141 0.005 285.823); transition all 0.15s cubic-bezier(0.19, 1, 0.22, 1); icon 16 x 16, oklch(0.141 0.005 285.823) |
| hover | background #f2f2f2 `color.curater.background`; text ABCDiatype 16/24 500, oklch(0.21 0.006 285.885); icon 16 x 16, oklch(0.21 0.006 285.885) |
| pressed | background #f2f2f2 `color.curater.background`; text ABCDiatype 16/24 500, oklch(0.21 0.006 285.885); transform translate(0px, 2px); icon 16 x 16, oklch(0.21 0.006 285.885) |

![Sign-in button default](components/crops/signin-btn-default.png) ![Sign-in button hover](components/crops/signin-btn-hover.png) ![Sign-in button focus-visible](components/crops/signin-btn-focus-visible.png) ![Sign-in button pressed](components/crops/signin-btn-pressed.png)

#### Feed tab
A 40px feed tab (Featured / For You / More); measured, never activated. Read as `tab-button` on the feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 64.39 x 40; padding 8px 0px; background transparent; text ABCDiatype 16/24 500, oklch(0.141 0.005 285.823); transition color 0.15s cubic-bezier(0.19, 1, 0.22, 1) |
| focus-visible | outline 2px solid oklch(0.871 0.006 286.286), offset 2px; layers button._tabButton_n5s4s_56 64.4x40.0 2px solid oklch(0.871 0.006 286.286) offset 2px |

![Feed tab default](components/crops/tab-button-default.png) ![Feed tab hover](components/crops/tab-button-hover.png) ![Feed tab focus-visible](components/crops/tab-button-focus-visible.png) ![Feed tab pressed](components/crops/tab-button-pressed.png)

#### Search toggle
The 20x20 search icon that reveals the search field. Read as `search-toggle` on the feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 20 x 20; background transparent; text ABCDiatype 16/24 400, oklch(0.552 0.016 285.938); transition color 0.15s cubic-bezier(0.19, 1, 0.22, 1); icon 14 x 14, oklch(0.552 0.016 285.938) |
| hover | text ABCDiatype 16/24 400, oklch(0.141 0.005 285.823); icon 14 x 14, oklch(0.141 0.005 285.823) |
| focus-visible | outline 2px solid oklch(0.871 0.006 286.286), offset 2px; layers button._searchToggle_n5s4s_139 20.0x20.0 2px solid oklch(0.871 0.006 286.286) offset 2px |
| pressed | text ABCDiatype 16/24 400, oklch(0.141 0.005 285.823); icon 14 x 14, oklch(0.141 0.005 285.823) |

![Search toggle default](components/crops/search-toggle-default.png) ![Search toggle hover](components/crops/search-toggle-hover.png) ![Search toggle focus-visible](components/crops/search-toggle-focus-visible.png) ![Search toggle pressed](components/crops/search-toggle-pressed.png)

#### Login button
"Log in or sign up" — the header auth link; measured, never followed. Read as `login-btn` on the feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 102.08 x 21; background transparent; text ABCDiatype 14/21 400, #7c7c7c `color.curater.gray-medium` |
| hover | text ABCDiatype 14/21 400, oklch(0.141 0.005 285.823) |
| focus-visible | outline 2px solid oklch(0.871 0.006 286.286), offset 2px; layers a._signInButton_n5s4s_215 102.1x21.0 2px solid oklch(0.871 0.006 286.286) offset 2px |
| pressed | text ABCDiatype 14/21 400, oklch(0.141 0.005 285.823) |

![Login button default](components/crops/login-btn-default.png) ![Login button hover](components/crops/login-btn-hover.png) ![Login button focus-visible](components/crops/login-btn-focus-visible.png) ![Login button pressed](components/crops/login-btn-pressed.png)

#### Search field
The "Search curations..." input revealed by the toggle; focused locally, never submitted. Read as `search-field` on the feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 170 x 30; background transparent; text ABCDiatype 14/21 400, oklch(0.141 0.005 285.823); transition opacity 0.15s cubic-bezier(0.19, 1, 0.22, 1); placeholder #afafaf `color.curater.gray-light` |

![Search field default](components/crops/search-field-default.png) ![Search field focused](components/crops/search-field-focused.png)

### Home

The signed-out landing: the 'Sign in / Create account' 259x58 white pill, the trend header and the 544x492 trend card (24px radius, soft 0 14px 54px lift) with its 100px thumbs, headline, curator label and avatar.

#### Trending header
"Trending on Curater / What our community has been sharing lately" + the sign-in CTA. Read as `trend-header` on the home page.

**Values (default).** size 544 x 196; background transparent; text ABCDiatype 24/30 500, oklch(0.141 0.005 285.823); icon 16 x 16, oklch(0.141 0.005 285.823); layers button.w-full 259.5x58.0 oklch(1 0 0) T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) rgba(0, 0, 0, 0.05) 0px 1px 2px 0px 9999px.

Child layers that carry the look: button 259.5x58 background oklch(1 0 0) border 1px solid oklch(0.95 0.004 286.32) radius 9999px shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px.

![Trending header default](components/crops/trend-header-default.png)

#### Trend card
A 544x570 trending curation card: thumbnails, headline, description, curator avatars; measured, never followed. Read as `trend-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 544 x 492.39; padding 80px 72px; border 1px solid #e8e7e7; radius 24px; background #ffffff `color.tailwind.white`; shadow rgba(0, 0, 0, 0.02) 0px 14px 54px 0px; text ABCDiatype 24/30 500, oklch(0.141 0.005 285.823) |

![Trend card default](components/crops/trend-card-default.png) ![Trend card hover](components/crops/trend-card-hover.png) ![Trend card focus-visible](components/crops/trend-card-focus-visible.png) ![Trend card pressed](components/crops/trend-card-pressed.png)

#### Card thumbnail
A 100x100 curation thumbnail tile. Read as `card-thumb` on the home page.

**Values (default).** size 100.8 x 100.8; border 2px solid #ffffff `color.tailwind.white`; radius 16px; background transparent; text ABCDiatype 16/24 400, oklch(0.141 0.005 285.823); transition transform 0.15s cubic-bezier(0.19, 1, 0.22, 1); layers ::before rgba(0, 0, 0, 0.05) 0px none 1.

![Card thumbnail default](components/crops/card-thumb-default.png)

#### Card headline
The curation headline (h2, 398px wide). Read as `card-headline` on the home page.

**Values (default).** size 398 x 90; background transparent; text ABCDiatype 24/30 500, oklch(0.141 0.005 285.823).

![Card headline default](components/crops/card-headline-default.png)

#### Card description
The curator's description copy under the headline. Read as `card-desc` on the home page.

**Values (default).** size 398 x 120; background transparent; text ABCDiatype 16/24 400, #7c7c7c `color.curater.gray-medium`.

![Card description default](components/crops/card-desc-default.png)

#### Curated-by label
The "CURATED BY" micro-label. Read as `curated-label` on the home page.

**Values (default).** size 73.88 x 12; background transparent; text ABCDiatype 12/12 500, #afafaf `color.curater.gray-light`.

![Curated-by label default](components/crops/curated-label-default.png)

#### Curator avatar
A 24x24 curator avatar in the card. Read as `card-avatar` on the home page.

**Values (default).** size 24 x 24; border 2px solid #ffffff `color.tailwind.white`; radius 1600px; background #ffffff `color.tailwind.white`; text ABCDiatype 16/24 400, oklch(0.141 0.005 285.823).

![Curator avatar default](components/crops/card-avatar-default.png)

### Feed

The public /feed: 'Browse by themes' heading, 224x271 theme tiles, curator labels, 24px title links, the 28px Save chip, and the media items (1080x540) and album links (540x540).

#### Feed heading
"Browse by themes" — the feed section heading. Read as `feed-heading` on the feed page.

**Values (default).** size 1264 x 24; background transparent; text ABCDiatype 16/24 500, oklch(0.141 0.005 285.823).

![Feed heading default](components/crops/feed-heading-default.png)

#### Theme card
A 224x271 theme tile ("Visual Identity / 16 curations"); measured, never followed. Read as `theme-card` on the feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 224 x 271; background transparent; text ABCDiatype 14/14 500, oklch(0.141 0.005 285.823); layers div._thumb_2m4ag_63 224.0x224.0 rgb(249, 246, 246) 20px; img 112.0x112.0 rgb(242, 242, 242) rgba(0, 0, 0, 0.16) 0px 2px 12px 0px 8px; img 82.8x128.0 rgb(242, 242, 242) rgba(0, 0, 0, 0.16) 0px 2px 12px 0px 8px; img 112.0x112.0 rgb(242, 242, 242) rgba(0, 0, 0, 0.16) 0px 2px 12px 0px 8px; img 112.0x112.0 rgb(242, 242, 242) rgba(0, 0, 0, 0.16) 0px 2px 12px 0px 8px; img 112.0x111.9 rgb(242, 242, 242) r |
| focus-visible | outline 2px solid oklch(0.871 0.006 286.286), offset 2px; layers a._card_2m4ag_36 224.0x271.0 2px solid oklch(0.871 0.006 286.286) offset 2px; div._thumb_2m4ag_63 224.0x224.0 rgb(249, 246, 246) 20px; img 112.0x112.0 rgb(242, 242, 242) rgba(0, 0, 0, 0.16) 0px 2px 12px 0px 8px; img 82.8x128.0 rgb(242, 242, 242) rgba(0, 0, 0, 0.16) 0px 2px 12px 0px 8px; img 112.0x112.0 rgb(242, 242, 242) rgba(0, 0, 0, 0.16) 0px 2px 12px 0px 8px; img 112.0x112.0 rgb(242, 242, 242)  |

Child layers that carry the look: div 224x224 background #f9f6f6 `color.curater.gray-200` radius 20px; img 112x112 background #f2f2f2 `color.curater.background` radius 8px shadow rgba(0, 0, 0, 0.16) 0px 2px 12px 0px; img 82.8x128 background #f2f2f2 `color.curater.background` radius 8px shadow rgba(0, 0, 0, 0.16) 0px 2px 12px 0px.

![Theme card default](components/crops/theme-card-default.png) ![Theme card hover](components/crops/theme-card-hover.png) ![Theme card focus-visible](components/crops/theme-card-focus-visible.png) ![Theme card pressed](components/crops/theme-card-pressed.png)

#### Curator label
A curator chip ("Ravi", "Glauber") over a feed entry; measured, never followed. Read as `curator-label` on the feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 66.8 x 32; background transparent; text ABCDiatype 14/21 500, oklch(0.141 0.005 285.823); transition opacity 0.15s cubic-bezier(0.19, 1, 0.22, 1) |
| focus-visible | outline 2px solid oklch(0.871 0.006 286.286), offset 2px; layers a._curatorLabel_njeuw_60 66.8x32.0 2px solid oklch(0.871 0.006 286.286) offset 2px |

![Curator label default](components/crops/curator-label-default.png) ![Curator label hover](components/crops/curator-label-hover.png) ![Curator label focus-visible](components/crops/curator-label-focus-visible.png) ![Curator label pressed](components/crops/curator-label-pressed.png)

#### Curation title
The large editorial curation title link; measured, never followed. Read as `title-link` on the feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 415.45 x 212; background transparent; text ABCDiatype 24/30 500, oklch(0.141 0.005 285.823) |
| hover | opacity 0.7 |
| focus-visible | outline 2px solid oklch(0.871 0.006 286.286), offset 2px; layers a._titleLink_1l58y_93 415.5x212.0 2px solid oklch(0.871 0.006 286.286) offset 2px |
| pressed | opacity 0.7 |

![Curation title default](components/crops/title-link-default.png) ![Curation title hover](components/crops/title-link-hover.png) ![Curation title focus-visible](components/crops/title-link-focus-visible.png) ![Curation title pressed](components/crops/title-link-pressed.png)

#### Save button
The save/bookmark control ("1", "Add to my taste"); measured, never pressed. Read as `save-btn` on the feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 42.55 x 28; padding 4px 8px; border 1px solid oklch(0.95 0.004 286.32); radius 9999px; background oklch(1 0 0); shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text ABCDiatype 12/18 500, oklch(0.141 0.005 285.823); transition all 0.15s cubic-bezier(0.19, 1, 0.22, 1); icon 16 x 16, oklch(0.141 0.005 285.823) |
| hover | background #f2f2f2 `color.curater.background`; text ABCDiatype 12/18 500, oklch(0.21 0.006 285.885); icon 16 x 16, oklch(0.21 0.006 285.885) |
| focus-visible | outline 2px solid oklch(0.871 0.006 286.286), offset 2px |
| pressed | background #f2f2f2 `color.curater.background`; text ABCDiatype 12/18 500, oklch(0.21 0.006 285.885); transform translate(0px, 2px); icon 16 x 16, oklch(0.21 0.006 285.885) |

![Save button default](components/crops/save-btn-default.png) ![Save button hover](components/crops/save-btn-hover.png) ![Save button focus-visible](components/crops/save-btn-focus-visible.png) ![Save button pressed](components/crops/save-btn-pressed.png)

#### Media tile
A large media tile in the entry's mosaic (up to 1080x540). Read as `media-item` on the feed page.

**Values (default).** size 1080 x 540; radius 20px; background transparent; text ABCDiatype 16/24 400, oklch(0.141 0.005 285.823).

![Media tile default](components/crops/media-item-default.png)

#### Album tile
A 540x540 album tile ("ALBUM / 8 TRACKS"); measured, never followed. Read as `album-link` on the feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 540 x 540; background transparent; text ABCDiatype 12/12 500, #afafaf `color.curater.gray-light`; layers div._albumDisc_1l58y_210 540.0x540.0 rgb(249, 246, 246) 9999px; img._albumCover_1l58y_225 356.4x356.4 rgba(0, 0, 0, 0.04) 0px 2px 4px -1px, rgba(0, 0, 0, 0.12) 0px 12px 32px -4px 6px |
| hover | icon 20 x 20, oklch(0.141 0.005 285.823); layers div._albumDisc_1l58y_210 540.0x540.0 rgb(249, 246, 246) 9999px; img._albumCover_1l58y_225 356.4x356.4 rgba(0, 0, 0, 0.04) 0px 2px 4px -1px, rgba(0, 0, 0, 0.12) 0px 12px 32px -4px 6px; span._albumOverlay_1l58y_240 356.4x356.4 rgba(0, 0, 0, 0.45) 6px; div._bubble_x6xan_36 180.0x32.8 oklch(0.141 0.005 285.823) rgba(0, 0, 0, 0.04) 0px 2px 4px -1px, rgba(0, 0, 0, 0.12) 0px 12px 32px -4px 9999px |
| focus-visible | outline 2px solid oklch(0.871 0.006 286.286), offset 2px; layers a._albumLink_1l58y_187 540.0x540.0 2px solid oklch(0.871 0.006 286.286) offset 2px; div._albumDisc_1l58y_210 540.0x540.0 rgb(249, 246, 246) 9999px; img._albumCover_1l58y_225 356.4x356.4 rgba(0, 0, 0, 0.04) 0px 2px 4px -1px, rgba(0, 0, 0, 0.12) 0px 12px 32px -4px 6px |

Child layers that carry the look: div 540x540 background #f9f6f6 `color.curater.gray-200` radius 9999px; img 356.4x356.4 radius 6px shadow rgba(0, 0, 0, 0.04) 0px 2px 4px -1px, rgba(0, 0, 0, 0.12) 0px 12px 32px -4px.

![Album tile default](components/crops/album-link-default.png) ![Album tile hover](components/crops/album-link-hover.png) ![Album tile focus-visible](components/crops/album-link-focus-visible.png) ![Album tile pressed](components/crops/album-link-pressed.png)

### TasteScope

The /taste teaser (redirects to /taste/soon): white 20px copy in a 256px column over the 1360x900 WebGL BrandGlobe canvas. Playwright locators never resolve on this route — it is measured through main-world queries.

#### TasteScope panel
The "SOON / TasteScope — it captures all dimensions of your aesthetic identity" teaser panel. Read as `taste-desc` on the taste page.

**Values (default).** size 256 x 788; background transparent; text ABCDiatype 12/12 500, #afafaf `color.curater.gray-light`; layers p._soonText_19p2q_106 51.3x20.0 rgb(51, 51, 51) 9999px.

Child layers that carry the look: p 51.3x20 background #333333 `color.curater.gray-dark` radius 9999px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### TasteScope heading
The "TasteScope" teaser heading. Read as `taste-h4` on the taste page.

**Values (default).** size 256 x 27.5; background transparent; text ABCDiatype 20/27.5 500, #ffffff `color.tailwind.white`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### BrandGlobe canvas
The 1360x900 WebGL globe canvas behind the teaser. Read as `taste-canvas` on the taste page.

**Values (default).** size 1360 x 900; background transparent; text ABCDiatype 16/24 400, oklch(0.141 0.005 285.823).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Curation

A public curation detail (/curation/<id>): the 36px back and 32px options controls, the ~350px heading column, the 350x58 Google SSO button and the 'search similar on' Pinterest/Cosmos chips.

#### Back button
The 36x36 back-arrow button; measured, never followed. Read as `back-btn` on the curation page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 36 x 36; background transparent; text ABCDiatype 16/24 400, oklch(0.141 0.005 285.823); icon 16 x 16, oklch(0.141 0.005 285.823); layers span 36.0x36.0 oklch(1 0 0) T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) rgba(0, 0, 0, 0.05) 0px 1px 2px 0px 9999px |
| hover | icon 16 x 16, oklch(0.21 0.006 285.885); layers span 36.0x36.0 rgb(242, 242, 242) T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) rgba(0, 0, 0, 0.05) 0px 1px 2px 0px 9999px |
| focus-visible | outline 2px solid oklch(0.871 0.006 286.286), offset 2px; layers a._backButton_1fhe2_142 36.0x36.0 2px solid oklch(0.871 0.006 286.286) offset 2px; span 36.0x36.0 oklch(1 0 0) T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) rgba(0, 0, 0, 0.05) 0px 1px 2px 0px 9999px |

Child layers that carry the look: span 36x36 background oklch(1 0 0) border 1px solid oklch(0.95 0.004 286.32) radius 9999px shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px.

![Back button default](components/crops/back-btn-default.png) ![Back button hover](components/crops/back-btn-hover.png) ![Back button focus-visible](components/crops/back-btn-focus-visible.png) ![Back button pressed](components/crops/back-btn-pressed.png)

#### Options button
The 32x32 options (…) button. Read as `options-btn` on the curation page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; border 1px solid oklch(0.95 0.004 286.32); radius 9999px; background oklch(1 0 0); shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text ABCDiatype 16/24 400, oklch(0.141 0.005 285.823); icon 16 x 16, oklch(0.141 0.005 285.823) |
| hover | background oklch(0.967 0.001 286.375) |
| focus-visible | outline 2px solid oklch(0.871 0.006 286.286), offset 2px |
| pressed | background oklch(0.967 0.001 286.375) |

![Options button default](components/crops/options-btn-default.png) ![Options button hover](components/crops/options-btn-hover.png) ![Options button focus-visible](components/crops/options-btn-focus-visible.png) ![Options button pressed](components/crops/options-btn-pressed.png)

#### Curation title
The 350x240 editorial curation title (h1). Read as `curation-h1` on the curation page.

**Values (default).** size 350 x 240; background transparent; text ABCDiatype 24/30 500, oklch(0.141 0.005 285.823).

![Curation title default](components/crops/curation-h1-default.png)

#### SSO button
"Continue with Google" — the 350x58 SSO button; measured, never pressed. Read as `sso-btn` on the curation page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 350 x 58; background transparent; text ABCDiatype 16/24 500, oklch(0.141 0.005 285.823); icon 16 x 16, oklch(0.141 0.005 285.823); layers button.w-full 350.0x58.0 oklch(1 0 0) T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) rgba(0, 0, 0, 0.05) 0px 1px 2px 0px 9999px |
| hover | text ABCDiatype 16/24 500, oklch(0.21 0.006 285.885); icon 16 x 16, oklch(0.21 0.006 285.885); layers button.w-full 350.0x58.0 rgb(242, 242, 242) T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) rgba(0, 0, 0, 0.05) 0px 1px 2px 0px 9999px |
| focus-visible | layers button.w-full 350.0x58.0 oklch(1 0 0) T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) rgba(0, 0, 0, 0.05) 0px 1px 2px 0px 2px solid oklch(0.871 0.006 286.286) offset 2px 9999px |

Child layers that carry the look: button 350x58 background oklch(1 0 0) border 1px solid oklch(0.95 0.004 286.32) radius 9999px shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px.

![SSO button default](components/crops/sso-btn-default.png) ![SSO button hover](components/crops/sso-btn-hover.png) ![SSO button focus-visible](components/crops/sso-btn-focus-visible.png) ![SSO button pressed](components/crops/sso-btn-pressed.png)

#### Similar label
The "SEARCH SIMILAR ON" micro-heading. Read as `similar-label` on the curation page.

**Values (default).** size 350 x 12; background transparent; text ABCDiatype 12/12 500, #afafaf `color.curater.gray-light`.

![Similar label default](components/crops/similar-label-default.png)

#### Similar-search button
A 132x45 outbound similar-search button (Pinterest / Cosmos); measured, never followed. Read as `similar-btn` on the curation page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 132.78 x 45; padding 12px 16px; radius 9999px; background oklch(0.967 0.001 286.375); text ABCDiatype 14/21 500, #7c7c7c `color.curater.gray-medium`; transition background-color 0.15s cubic-bezier(0.19, 1, 0.22, 1), color 0.15s cubic-bezier(0.19, 1, 0.22, 1); icon 16 x 16, oklch(0.141 0.005 285.823) |
| hover | background oklch(0.32109 0.0000159743 none / 0.1); text ABCDiatype 14/21 500, oklch(0.141 0.005 285.823); icon 16 x 16, oklch(0.21 0.006 285.885) |
| focus-visible | outline 2px solid oklch(0.871 0.006 286.286), offset 2px |
| pressed | background oklch(0.32109 0.0000159743 none / 0.1); text ABCDiatype 14/21 500, oklch(0.141 0.005 285.823); icon 16 x 16, oklch(0.21 0.006 285.885) |

![Similar-search button default](components/crops/similar-btn-default.png) ![Similar-search button hover](components/crops/similar-btn-hover.png) ![Similar-search button focus-visible](components/crops/similar-btn-focus-visible.png) ![Similar-search button pressed](components/crops/similar-btn-pressed.png)

#### Pins label
The "PINS" micro-heading. Read as `pins-label` on the curation page.

**Values (default).** size 28.02 x 12; background transparent; text ABCDiatype 12/12 500, #afafaf `color.curater.gray-light`.

![Pins label default](components/crops/pins-label-default.png)

### Profile

A public profile (/ravi): the name, 28px avatar, the ~130x42 TasteScope header button, the bio column and the 268x380 item tiles with their 28px menu.

#### Profile name
The "Ravi Vasavan" profile heading. Read as `profile-name` on the profile page.

**Values (default).** size 93.2 x 24; background transparent; text ABCDiatype 16/24 500, oklch(0.141 0.005 285.823).

![Profile name default](components/crops/profile-name-default.png)

#### Profile avatar
The 28x28 profile avatar. Read as `profile-avatar` on the profile page.

**Values (default).** size 28 x 28; radius 9999px; background transparent; text ABCDiatype 16/24 400, oklch(0.141 0.005 285.823).

![Profile avatar default](components/crops/profile-avatar-default.png)

#### TasteScope button
The 129x42 "TasteScope" header button; measured, never followed. Read as `tastescope-btn` on the profile page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 129.84 x 42; padding 20px 16px; border 1px solid oklch(0.95 0.004 286.32); radius 9999px; background oklch(1 0 0); shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text ABCDiatype 14/14 500, oklch(0.141 0.005 285.823); transition all 0.15s cubic-bezier(0.19, 1, 0.22, 1); icon 16 x 16, oklch(0.141 0.005 285.823) |
| hover | background #f2f2f2 `color.curater.background`; text ABCDiatype 14/14 500, oklch(0.21 0.006 285.885); icon 16 x 16, oklch(0.21 0.006 285.885) |
| pressed | background #f2f2f2 `color.curater.background`; text ABCDiatype 14/14 500, oklch(0.21 0.006 285.885); transform translate(0px, 2px); icon 16 x 16, oklch(0.21 0.006 285.885) |

![TasteScope button default](components/crops/tastescope-btn-default.png) ![TasteScope button hover](components/crops/tastescope-btn-hover.png) ![TasteScope button focus-visible](components/crops/tastescope-btn-focus-visible.png) ![TasteScope button pressed](components/crops/tastescope-btn-pressed.png)

#### Profile bio
The curator's bio paragraph. Read as `profile-bio` on the profile page.

**Values (default).** size 379.19 x 156.73; background transparent; text ABCDiatype 16/22.4 500, oklch(0.141 0.005 285.823).

![Profile bio default](components/crops/profile-bio-default.png)

#### Profile item
A 268x380 profile curation item (category, title, saved mark, menu); measured, never followed. Read as `profile-item` on the profile page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 268.27 x 380.27; background transparent; text ABCDiatype 12/18 500, #afafaf `color.curater.gray-light`; icon 10 x 10, #afafaf `color.curater.gray-light`; layers div._imageContainer_19sub_46 268.3x268.3 oklch(0.967 0.001 286.375) 20px; span._userAvatar_19sub_325 16.0x16.0 rgb(212, 212, 212) 9999px; button._menuButton_19sub_40 28.0x28.0 rgba(0, 0, 0, 0.2) 9999px |
| focus-visible | layers a._link_19sub_50 268.3x380.3 2px solid oklch(0.871 0.006 286.286) offset 2px; div._imageContainer_19sub_46 268.3x268.3 oklch(0.967 0.001 286.375) 20px; span._userAvatar_19sub_325 16.0x16.0 rgb(212, 212, 212) 9999px; button._menuButton_19sub_40 28.0x28.0 rgba(0, 0, 0, 0.2) 9999px |

Child layers that carry the look: div 268.3x268.3 background oklch(0.967 0.001 286.375) radius 20px; span 16x16 background #d4d4d4 `color.curater.gray-muted` radius 9999px; button 28x28 background rgba(0, 0, 0, 0.2) radius 9999px.

![Profile item default](components/crops/profile-item-default.png) ![Profile item hover](components/crops/profile-item-hover.png) ![Profile item focus-visible](components/crops/profile-item-focus-visible.png) ![Profile item pressed](components/crops/profile-item-pressed.png)

#### Item title
The item's 268x60 title. Read as `item-title` on the profile page.

**Values (default).** size 268.27 x 60; background transparent; text ABCDiatype 16/20 500, oklch(0.141 0.005 285.823).

![Item title default](components/crops/item-title-default.png)

#### Item menu
The 28x28 item overflow menu; opened locally, never an action taken. Read as `item-menu` on the profile page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 28 x 28; radius 9999px; background rgba(0, 0, 0, 0.2); text ABCDiatype 16/24 400, #ffffff `color.tailwind.white`; transition opacity 0.15s cubic-bezier(0.19, 1, 0.22, 1), background-color 0.15s cubic-bezier(0.19, 1, 0.22, 1); opacity 0; icon 16 x 16, #ffffff `color.tailwind.white` |
| hover | background rgba(0, 0, 0, 0.9); opacity none |
| focus-visible | outline 2px solid oklch(0.871 0.006 286.286), offset 2px |
| pressed | background rgba(0, 0, 0, 0.9) |

![Item menu default](components/crops/item-menu-default.png) ![Item menu hover](components/crops/item-menu-hover.png) ![Item menu focus-visible](components/crops/item-menu-focus-visible.png) ![Item menu pressed](components/crops/item-menu-pressed.png)

### Legal

The /terms page: the ~560px heading and body column.

#### Legal heading
"Terms of Use" — the legal page heading. Read as `legal-h1` on the terms page.

**Values (default).** size 560 x 55.19; background transparent; text ABCDiatype 48/55.2 500, oklch(0.141 0.005 285.823).

![Legal heading default](components/crops/legal-h1-default.png)

#### Legal paragraph
A body paragraph of the terms text. Read as `legal-body` on the terms page.

**Values (default).** size 560 x 21; background transparent; text ABCDiatype 14/21 400, oklch(0.552 0.016 285.938).

![Legal paragraph default](components/crops/legal-body-default.png)

### Mobile (390 wide)

The same app at phone width: the 160x40 bottom nav bar of 40px buttons, the sign-in pill, heading and trend card.

#### Mobile nav rail
Read as `m-nav-rail` on the home page at 390 wide.

**Values (default).** size 160 x 40; background transparent; text ABCDiatype 16/24 400, oklch(0.141 0.005 285.823); icon 20 x 20, oklch(0.552 0.016 285.938).

![Mobile nav rail default](components/crops/m-nav-rail-default.png)

#### Mobile nav button
A rail icon button at 390px. Read as `m-nav-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 40 x 40; radius 9999px; background transparent; text ABCDiatype 16/24 400, oklch(0.552 0.016 285.938); icon 20 x 20, oklch(0.552 0.016 285.938) |
| focus-visible | outline 2px solid oklch(0.871 0.006 286.286), offset 2px; layers a._mobileNavButton_1psr6_242 40.0x40.0 2px solid oklch(0.871 0.006 286.286) offset 2px 9999px |

![Mobile nav button default](components/crops/m-nav-button-default.png) ![Mobile nav button hover](components/crops/m-nav-button-hover.png) ![Mobile nav button focus-visible](components/crops/m-nav-button-focus-visible.png) ![Mobile nav button pressed](components/crops/m-nav-button-pressed.png)

#### Mobile sign-in
The mobile sign-in CTA; measured, never followed. Read as `m-signin-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 259.45 x 58; padding 16px 24px; border 1px solid oklch(0.95 0.004 286.32); radius 9999px; background oklch(1 0 0); shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text ABCDiatype 16/24 500, oklch(0.141 0.005 285.823); transition all 0.15s cubic-bezier(0.19, 1, 0.22, 1); icon 16 x 16, oklch(0.141 0.005 285.823) |
| hover | background #f2f2f2 `color.curater.background`; text ABCDiatype 16/24 500, oklch(0.21 0.006 285.885); icon 16 x 16, oklch(0.21 0.006 285.885) |
| pressed | background #f2f2f2 `color.curater.background`; text ABCDiatype 16/24 500, oklch(0.21 0.006 285.885); transform translate(0px, 2px); icon 16 x 16, oklch(0.21 0.006 285.885) |

![Mobile sign-in default](components/crops/m-signin-btn-default.png) ![Mobile sign-in hover](components/crops/m-signin-btn-hover.png) ![Mobile sign-in focus-visible](components/crops/m-signin-btn-focus-visible.png) ![Mobile sign-in pressed](components/crops/m-signin-btn-pressed.png)

#### Mobile heading
Read as `m-heading` on the home page at 390 wide.

**Values (default).** size 358 x 90; padding 0px 48px; background transparent; text ABCDiatype 24/30 500, oklch(0.141 0.005 285.823).

![Mobile heading default](components/crops/m-heading-default.png)

#### Mobile trend card
A trend card at 390px width. Read as `m-trend-card` on the home page at 390 wide.

**Values (default).** size 358 x 455.59; padding 48px 24px 8px 24px; border 1px solid #e8e7e7; radius 24px; background #ffffff `color.tailwind.white`; shadow rgba(0, 0, 0, 0.02) 0px 14px 54px 0px; text ABCDiatype 20/27 500, oklch(0.141 0.005 285.823).

![Mobile trend card default](components/crops/m-trend-card-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the nav glyphs, the TasteScope mark, the Pinterest/Cosmos badges and the curation media) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The signed-in Curater app — creating curations, the TasteScope questionnaire, saving items, settings — was never reached. 'Log in or sign up', 'Sign in / Create account' and the Google SSO button are measured controls, never followed; every public surface is read-only. What the product looks like past the signed-out feed is not documented here.

### Pages

- **App and CTAs.** 'Log in or sign up', 'Sign in / Create account', Google SSO, Save, TasteScope and the Pinterest/Cosmos 'search similar' buttons were measured, never followed; no account exists on this surface.
- **Feed depth.** /feed scrolls in an inner container (not the document): the desktop full-page capture is bounded at the first 27,850px and mobile at 57,550px — the tail is a documented boundary, not missing content.
- **Other curations/profiles.** One curation (/curation/qDNMdxe5) and one profile (/ravi) were captured as representatives of their page types; the catalog's full range is not enumerated.
- **External surfaces** (Pinterest, Cosmos deep links, social profiles) are linked from the app but were never opened.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **The search field** was revealed by a local toggle click and left open; nothing was typed or submitted.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

One painted theme, no toggle: every page paints light (#fff page/cards over the #f2f2f2 app field, #09090b ink, #71717b muted). The only dark-looking surface is the TasteScope teaser's WebGL globe — a canvas asset, not a theme. tokens.json's light set holds the declared :root var layer (177 resolved vars); no dark set is emitted.

### Fonts

- **ABCDiatype** (500 headings/buttons/titles, 400 body) is the applied face on every measured component, with a long system fallback chain; its @font-face faces are declared in the app sheets and the files are not shipped in this package.

### Screenshots

- The curation media, theme imagery, avatars and the BrandGlobe canvas in the screenshots are the product's published content; only frames and components were measured.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The curation images, theme artwork, curator names and item titles are the product's content; only frames and components were measured.
