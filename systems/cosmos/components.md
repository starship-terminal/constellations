# Cosmos components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from cosmos.so on 2026-11-12, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, submitted or paid for; the login card's fields were focused and filled then cleared, never sent; the sign-up and social links were never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (31 components, 89 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (90 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Explore | `/explore` | [default](screenshots/explore-light-default.png), [full](screenshots/explore-light-full.png) |
| Sequence | `/sequence` | [default](screenshots/sequence-light-default.png), [full](screenshots/sequence-light-full.png) |
| Shop | `/shop` | [default](screenshots/shop-light-default.png), [full](screenshots/shop-light-full.png) |
| Search | `/search` | [default](screenshots/search-light-default.png), [full](screenshots/search-light-full.png) |
| Brand page | `/brand/...` | [default](screenshots/brand-light-default.png), [full](screenshots/brand-light-full.png) |
| Profile page | `/profile/...` | [default](screenshots/profile-light-default.png), [full](screenshots/profile-light-full.png) |
| Careers | `/careers` | [default](screenshots/careers-light-default.png), [full](screenshots/careers-light-full.png) |
| Sign-in card | `/login` | [default](screenshots/login-light-default.png), [form-focus](screenshots/login-light-form-focus.png) |
| Sign-up start | `/start` | [default](screenshots/start-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Explore, phone | `/explore` | [default](screenshots/mobile-explore-light-default.png), [full](screenshots/mobile-explore-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the 44px menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-menu-row), [m-signup](#mobile-sign-up) |
| Auth form focus | /login | the username field's own focus — typed text was deleted again, never sent | [login-light-form-focus](screenshots/login-light-form-focus.png), [auth-input](#auth-field), [auth-next](#auth-next) |
| Auth Next enabled | /login | typing into both fields (name@example.com, sample-pass), then cleared — never submitted | [auth-next](#auth-next) enabled state |
| Explore tab bar | /explore | the tab selector never matched on this pass — the tab's measured states stand in | missed; see Gaps |
| Consent overlays | every page | none painted; generic overlay-hiding ran as defence-in-depth, never answered | nothing to hide |
| The signed-in product | cosmos.so | behind sign-in; the public /login card was measured, never used | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 16 components were given a real keyboard focus. 0 draw an outline ring: . The other 16 show no measured change: `nav-link`, `signup-cta`, `login-link`, `hero-search`, `join-cta`, `cat-tab`, `selected-card`, `element-tile`, `seq-card`, `forgot-link`, `auth-signup`, `footer-link`, `social-icon`, `m-menu-button`, `m-nav-item`, `m-signup`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-backdrop-filter, all, backdrop-filter, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | auth-next, footer-link, forgot-link, join-cta, login-link, m-menu-button, m-signup, nav-link and more |
| 0.2s | `cubic-bezier(0, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, scale, stroke, text-decoration-color | hero-search, qr-card |
| 0.3s | `cubic-bezier(0, 0, 0.2, 1)` | rotate, scale, transform, translate | m-menu-open |
| 0.5s | `cubic-bezier(0.22, 1, 0.36, 1)` | width | search-pill |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Auth panel](#auth-panel) | 344 x 289.02 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The 92px white header: the 32px Cosmos mark, the Sequence / Instagram / TikTok / X text links in secondary gray, and the Log in link + 48px black Sign up pill on the right.

#### Header
The sticky app header (hidden until painted): the flower mark, Explore / Sequence / Shop links, the search pill, Log in and Sign up. Read as `header` on the home page.

**Values (default).** size 1440 x 92; padding 24px 32px; background transparent; text cosmosOracle 15/22 500, lab(45.1621 1.47596 1.15491); layers div.pointer-events-none.absolute 1440.0x168.0; span._O9AMq_dot 6.5x6.5 lab(3.63782 -0.00000745058 0) 999px; span._O9AMq_dot 6.5x6.5 lab(3.63782 -0.00000745058 0) 999px; span._O9AMq_dot 6.5x6.5 lab(3.63782 -0.00000745058 0) 999px; span._O9AMq_dot 6.5x6.5 lab(3.63782 -0.00000745058 0) 999px; span._O9AMq_dot 6.5x6.5 lab(3.63782 -0.00000745058 0) 999px.

Child layers that carry the look: div 1440x168 image linear-gradient(lab(96.648 0.426352 1.20401) 0%, lab(96.648 0.426352 1.20401) 15%, rgba(24; span 6.5x6.5 background lab(3.63782 -0.00000745058 0) radius 999px; span 6.5x6.5 background lab(3.63782 -0.00000745058 0) radius 999px.

![Header default](components/crops/header-default.png)

#### Logo
The Cosmos flower mark anchor. Read as `logo` on the home page.

**Values (default).** size 32 x 32; background transparent; text cosmosOracle 16/24 400, lab(3.63782 -0.00000745058 0); layers span._O9AMq_dot 6.5x6.5 lab(3.63782 -0.00000745058 0) 999px; span._O9AMq_dot 6.5x6.5 lab(3.63782 -0.00000745058 0) 999px; span._O9AMq_dot 6.5x6.5 lab(3.63782 -0.00000745058 0) 999px; span._O9AMq_dot 6.5x6.5 lab(3.63782 -0.00000745058 0) 999px; span._O9AMq_dot 6.5x6.5 lab(3.63782 -0.00000745058 0) 999px; span._O9AMq_dot 6.5x6.5 lab(3.63782 -0.00000745058 0) 999px.

Child layers that carry the look: span 6.5x6.5 background lab(3.63782 -0.00000745058 0) radius 999px; span 6.5x6.5 background lab(3.63782 -0.00000745058 0) radius 999px; span 6.5x6.5 background lab(3.63782 -0.00000745058 0) radius 999px.

![Logo default](components/crops/logo-default.png)

#### Nav link
A header nav link (Explore / Sequence / Shop); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 51.7 x 22; background transparent; text cosmosOracle 15/22 500, lab(45.1621 1.47596 1.15491); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | text cosmosOracle 15/22 500, lab(3.63782 -0.00000745058 0) |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Sign-up pill
The black "Sign up" header pill; measured, never followed. Read as `signup-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 100.84 x 48; padding 16px 24px; border 1px solid transparent; radius 3.35544e+07px; background lab(3.63782 -0.00000745058 0); text cosmosOracle 15/22 500, lab(100 0 0); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | background lab(13.928 0 0) |

![Sign-up pill default](components/crops/signup-cta-default.png) ![Sign-up pill hover](components/crops/signup-cta-hover.png) ![Sign-up pill focus-visible](components/crops/signup-cta-focus-visible.png) ![Sign-up pill pressed](components/crops/signup-cta-pressed.png)

#### Log-in pill
The light "Log in" header pill; measured, never followed. Read as `login-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 89.92 x 48; padding 16px 24px; border 1px solid transparent; radius 3.35544e+07px; background transparent; text cosmosOracle 15/22 500, lab(45.1621 1.47596 1.15491); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | text cosmosOracle 15/22 500, lab(3.63782 -0.00000745058 0) |

![Log-in pill default](components/crops/login-link-default.png) ![Log-in pill hover](components/crops/login-link-hover.png) ![Log-in pill focus-visible](components/crops/login-link-focus-visible.png) ![Log-in pill pressed](components/crops/login-link-pressed.png)

### Home

The 72px cosmosOracle hero (the rotating-word link cycles search terms) over the 640 x 82 search pill, the black Join Cosmos for free CTA and the 25%-radius QR card.

#### Hero headline
The 72px display ("Find your next go-to outfit" — the object word rotates through saved categories). Read as `hero-h1` on the home page.

**Values (default).** size 1200 x 160; background transparent; text cosmosOracle 72/72 700, lab(3.63782 -0.00000745058 0); layers span.block.size-9 70.3x70.3 lab(95.1978 0.212193 0.601578) T:1px solid lab(96.648 0.426352 1.20401) / R:1px solid lab(96.648 0.426352 1.20401) / B:1px solid lab(96.648 0.426352 1.20401) / L:1px solid lab(96.648 0.426352 1.20401) 16px; span.block.size-9 70.3x70.3 lab(95.1978 0.212193 0.601578) T:1px solid lab(96.648 0.426352 1.20401) / R:1px solid lab(96.648 0.426352 1.20401) / B:1px solid lab(96.6.

Child layers that carry the look: span 70.3x70.3 background lab(95.1978 0.212193 0.601578) border 1px solid lab(96.648 0.426352 1.20401) radius 16px; span 70.3x70.3 background lab(95.1978 0.212193 0.601578) border 1px solid lab(96.648 0.426352 1.20401) radius 16px.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero search
The hero search pill ("Search for outfits"); measured, never used — it would open the search surface. Read as `hero-search` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 204.77 x 58; padding 4px; border 1px solid transparent; radius 3.35544e+07px; background transparent; text cosmosOracle 16/24 400, lab(3.63782 -0.00000745058 0); transition color 0.2s cubic-bezier(0, 0, 0.2, 1), background-color 0.2s cubic-bezier(0, 0, 0.2, 1), border-color 0.2s cubic-bezier(0, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0, 0, 0.2, 1), fill 0.2s cubic-bezier(0, 0, 0.2, 1), stroke 0.2s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0, 0, 0.2, 1) |

![Hero search default](components/crops/hero-search-default.png) ![Hero search hover](components/crops/hero-search-hover.png) ![Hero search focus-visible](components/crops/hero-search-focus-visible.png) ![Hero search pressed](components/crops/hero-search-pressed.png)

#### Join CTA
The black "Join Cosmos for free" pill; measured, never followed. Read as `join-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 200.83 x 56; padding 16px 24px; border 1px solid transparent; radius 3.35544e+07px; background lab(3.63782 -0.00000745058 0); text cosmosOracle 16/24 700, lab(100 0 0); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | background lab(13.928 0 0) |

![Join CTA default](components/crops/join-cta-default.png) ![Join CTA hover](components/crops/join-cta-hover.png) ![Join CTA focus-visible](components/crops/join-cta-focus-visible.png) ![Join CTA pressed](components/crops/join-cta-pressed.png)

#### Get-the-app card
The "Get the app" QR card fixed bottom-right. Read as `qr-card` on the home page.

**Values (default).** size 208.78 x 242; padding 12px 4px 0px 4px; border 1px solid oklch(0.1591 0.00000406586 none / 0.12); radius 25%; background lab(100 0 0); shadow rgba(0, 0, 0, 0.02) 0px 2px 12px 0px, rgba(0, 0, 0, 0.1) 0px 4px 16px 0px; text cosmosOracle 16/22.4 500, lab(3.63782 -0.00000745058 0); transition scale 0.2s cubic-bezier(0, 0, 0.2, 1); icon 20 x 20, lab(3.63782 -0.00000745058 0).

![Get-the-app card default](components/crops/qr-card-default.png)

### Explore and search

The /explore surface: the 56px floating search pill, the 40px radius-full category tabs, 20px section heads and the masonry of 3px-radius element tiles on paper gray. Search and brand pages reuse the same language.

#### Search field
The header search field (a suggested query in the placeholder); focused, never searched. Read as `search-pill` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 456 x 56; radius 3.35544e+07px; background transparent; shadow rgba(0, 0, 0, 0.05) 0px 1px 8px 0px; text cosmosOracle 14/19.6 400, lab(62.6934 0.986487 0.930774); transition width 0.5s cubic-bezier(0.22, 1, 0.36, 1); icon 20 x 20, lab(62.6934 0.986487 0.930774); layers div.pointer-events-auto.flex 456.0x56.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 8px 0px 3.35544e+07px; div.relative.-mr-[0.5px] 456.5x56.0 lab(98.6778 0.212163 0.601566) T:1px solid oklch(0.1591 0.00000406586 none / 0.12) / R:1px solid oklch(0.1591 0.00000406586 none / 0.12)  |
| hover | text cosmosOracle 14/19.6 400, lab(45.1621 1.47596 1.15491); layers div.pointer-events-auto.flex 456.0x56.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 8px 0px 3.35544e+07px; div.relative.-mr-[0.5px] 456.5x56.0 lab(97.6569 0.354469 0.127113) T:1px solid oklch(0.1591 0.00000406586 none / 0.12) / R:1px solid oklch(0.1591 0.00000406586 none / 0.12)  |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Search field default](components/crops/search-pill-default.png) ![Search field hover](components/crops/search-pill-hover.png) ![Search field pressed](components/crops/search-pill-pressed.png)

#### Category tab
A category chip in the explore rail (Fashion/Interiors/...); measured, never followed. Read as `cat-tab` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 88.73 x 40.02; padding 10px 20px; radius 3.35544e+07px; background transparent; text cosmosOracle 14/20.02 500, lab(62.6934 0.986487 0.930774) |
| hover, pressed | text cosmosOracle 14/20.02 500, lab(3.63782 -0.00000745058 0) |

![Category tab default](components/crops/cat-tab-default.png) ![Category tab hover](components/crops/cat-tab-hover.png) ![Category tab focus-visible](components/crops/cat-tab-focus-visible.png) ![Category tab pressed](components/crops/cat-tab-pressed.png)

#### Section heading
A section heading on /explore ("Selected by Cosmos" / "Explore elements"). Read as `section-h2` on the explore page.

**Values (default).** size 1376 x 23; background transparent; text cosmosOracle 20/23 400, lab(3.63782 -0.00000745058 0).

![Section heading default](components/crops/section-h2-default.png)

#### Selected card
A "Selected by Cosmos" carousel card (artwork, title, @handle and element count); measured, never followed. Read as `selected-card` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 365 x 200.98; background transparent; text cosmosOracle 32/48 800, lab(100 0 0); layers div.relative.flex 365.0x151.0 lab(95.1978 0.212193 0.601578) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.02) 0px 2px 12px 0px, rgba(0, 0, 0, 0.1) 0px 4px 16px 0px 16px; div.absolute.inset-0 365.0x151.0 oklab(0 0 0 / 0.35) |

Child layers that carry the look: div 365x151 background lab(95.1978 0.212193 0.601578) radius 16px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.02) 0px 2px 12px 0px, rgba(0, 0, 0, 0.1) `shadow.color.primary` 0px 4px 16px 0px; div 365x151 background oklab(0 0 0 / 0.35).

![Selected card default](components/crops/selected-card-default.png) ![Selected card hover](components/crops/selected-card-hover.png) ![Selected card focus-visible](components/crops/selected-card-focus-visible.png) ![Selected card pressed](components/crops/selected-card-pressed.png)

#### Element tile
A masonry tile in the Explore elements grid (rounded-element corners over the image); measured, never followed — opening it goes to the element. Read as `element-tile` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 1376 x 3500; radius 3px; background lab(96.648 0.426352 1.20401); text cosmosOracle 12/18 500, lab(100 0 0); icon 20 x 20, lab(100 0 0) |

![Element tile focus-visible](components/crops/element-tile-focus-visible.png) ![Element tile pressed](components/crops/element-tile-pressed.png)

### Sequence

The /sequence surface: the 88px display heading over sequence cards.

#### Sequence title
The "Sequence" page heading. Read as `seq-h1` on the sequence page.

**Values (default).** size 451.19 x 132; background transparent; text cosmosOracle 88/132 700, lab(3.63782 -0.00000745058 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Sequence card
An article card in the Sequence editorial list; measured, never followed. Read as `seq-card` on the sequence page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 32 x 32; background transparent; text cosmosOracle 16/24 400, lab(3.63782 -0.00000745058 0); layers span._O9AMq_dot 6.5x6.5 lab(3.63782 -0.00000745058 0) 999px; span._O9AMq_dot 6.5x6.5 lab(3.63782 -0.00000745058 0) 999px; span._O9AMq_dot 6.5x6.5 lab(3.63782 -0.00000745058 0) 999px; span._O9AMq_dot 6.5x6.5 lab(3.63782 -0.00000745058 0) 999px; span._O9AMq_dot 6.5x6.5 lab(3.63782 -0.00000745058 0) 999px; span._O9AMq_dot 6.5x6.5 lab(3.63782 -0.00000745058 0) 999px |

Child layers that carry the look: span 6.5x6.5 background lab(3.63782 -0.00000745058 0) radius 999px; span 6.5x6.5 background lab(3.63782 -0.00000745058 0) radius 999px; span 6.5x6.5 background lab(3.63782 -0.00000745058 0) radius 999px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Login

The public auth card on /login: the username-or-email and password fields, the visibility toggle, Forgot password, and the 56px Next pill — measured disabled and enabled (both fields typed, never submitted).

#### Auth panel
The "Welcome back" sign-in panel (username/email + password fields, the disabled-then-enabled Next, Forgot password, the sign up link) over the image collage; captured, never used. Read as `auth-card` on the login page.

**Values (default).** size 344 x 289.02; background transparent; text cosmosOracle 20/23 500, lab(0 0 0); icon 20 x 20, lab(0 0 0); layers label.group.flex 344.0x52.0 T:1px solid oklch(0.1591 0.00000406586 none / 0.12) / R:1px solid oklch(0.1591 0.00000406586 none / 0.12) / B:1px solid oklch(0.1591 0.00000406586 none / 0.12) / L:1px solid oklch(0.1591 0.00000406586 none / 0.12) 16px; label.group.flex 344.0x52.0 T:1px solid oklch(0.1591 0.00000406586 none / 0.12) / R:1px solid oklch(0.1591 0.00000406586 none / 0.12) / B:1px solid oklc.

Child layers that carry the look: label 344x52 border 1px solid oklch(0.1591 0.00000406586 none / 0.12) radius 16px; label 344x52 border 1px solid oklch(0.1591 0.00000406586 none / 0.12) radius 16px; button 344x56 background lab(95.1978 0.212193 0.601578) border 1px solid transparent radius 3.35544e+07px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Username field
The "Username or email" input; focused and given sample text that was deleted again — nothing sent. Read as `auth-input` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 310 x 18; background transparent; text cosmosOracle 15/22 400, lab(3.63782 -0.00000745058 0); placeholder lab(62.6934 0.986487 0.930774) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Password field
The Password input (with the reveal-eye button); focused and given sample text that was deleted again — nothing sent. Read as `auth-pass` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 310 x 18; padding 0px 32px 0px 0px; background transparent; text cosmosOracle 15/22 400, lab(3.63782 -0.00000745058 0); placeholder lab(62.6934 0.986487 0.930774) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Next button
The "Next" submit — greyed and disabled until both fields hold text (the enabled state is measured with the fields filled); never pressed. Read as `auth-next` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 344 x 56; padding 16px 24px; border 1px solid transparent; radius 3.35544e+07px; background lab(95.1978 0.212193 0.601578); text cosmosOracle 14/21 500, lab(62.6934 0.986487 0.930774); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| enabled | background lab(3.63782 -0.00000745058 0); text cosmosOracle 14/21 500, lab(100 0 0) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Forgot-password link
The "Forgot password?" link; measured, never followed. Read as `forgot-link` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 113.45 x 20.02; background transparent; text cosmosOracle 14/20.02 500, lab(70.884 0 0); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | text cosmosOracle 14/20.02 500, lab(3.63782 -0.00000745058 0) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Sign-up link
The "sign up" link on the auth panel; measured, never followed. Read as `auth-signup` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 45.23 x 17; background transparent; text cosmosOracle 14/22 400, lab(3.63782 -0.00000745058 0) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Footer

The light footer: the link columns, social icons and legal.

#### Footer
The footer (force-light): Discover links, the app badges, Follow-us socials and the Info legal row. Read as `footer` on the explore page.

**Values (default).** size 1440 x 276; background transparent; text cosmosOracle 16/24 500, lab(62.6934 0.986487 0.930774); layers span._O9AMq_dot 13.0x13.0 lab(3.63782 -0.00000745058 0) 999px; span._O9AMq_dot 13.0x13.0 lab(3.63782 -0.00000745058 0) 999px; span._O9AMq_dot 13.0x13.0 lab(3.63782 -0.00000745058 0) 999px; span._O9AMq_dot 13.0x13.0 lab(3.63782 -0.00000745058 0) 999px; span._O9AMq_dot 13.0x13.0 lab(3.63782 -0.00000745058 0) 999px; span._O9AMq_dot 13.0x13.0 lab(3.63782 -0.00000745058 0) 999px.

Child layers that carry the look: span 13x13 background lab(3.63782 -0.00000745058 0) radius 999px; span 13x13 background lab(3.63782 -0.00000745058 0) radius 999px; span 13x13 background lab(3.63782 -0.00000745058 0) radius 999px.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer link (Download app / Careers / Terms); measured, never followed. Read as `footer-link` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 72.56 x 24; background transparent; text cosmosOracle 16/24 500, lab(62.6934 0.986487 0.930774); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | text cosmosOracle 16/24 500, lab(3.63782 -0.00000745058 0) |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A social link in the footer (Instagram/TikTok/X). Read as `social-icon` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 72.56 x 24; background transparent; text cosmosOracle 16/24 500, lab(62.6934 0.986487 0.930774); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | text cosmosOracle 16/24 500, lab(3.63782 -0.00000745058 0) |

![Social link default](components/crops/social-icon-default.png) ![Social link hover](components/crops/social-icon-hover.png) ![Social link focus-visible](components/crops/social-icon-focus-visible.png) ![Social link pressed](components/crops/social-icon-pressed.png)

### Mobile (390 wide)

The same surface at phone width: the header shrinks to 68px with a 44px menu button, and the menu opens as a full overlay with nav rows and a 56px sign-up pill.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 68; padding 12px 16px; background transparent; text cosmosOracle 16/24 400, lab(3.63782 -0.00000745058 0); icon 100 x 16.84, lab(3.63782 -0.00000745058 0); layers div.pointer-events-none.absolute 390.0x112.0; a.relative.inline-flex 97.8x34.0 lab(3.63782 -0.00000745058 0) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 3.35544e+07px; span.absolute.block 14.0x1.5 lab(62.6934 0.986487 0.930774); span.absolute.block 14.0x1.5 lab(62.6934 0.986487 0.930774).

Child layers that carry the look: div 390x112 image linear-gradient(lab(96.648 0.426352 1.20401) 0%, lab(96.648 0.426352 1.20401) 15%, rgba(24; a 97.8x34 background lab(3.63782 -0.00000745058 0) border 1px solid transparent radius 3.35544e+07px; span 14x1.5 background lab(62.6934 0.986487 0.930774).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Menu button
The header menu button (xl:hidden) that opens the full overlay. Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 44 x 44; radius 3.35544e+07px; background transparent; text cosmosOracle 16/24 400, lab(3.63782 -0.00000745058 0); transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers span.absolute.block 14.0x1.5 lab(62.6934 0.986487 0.930774); span.absolute.block 14.0x1.5 lab(62.6934 0.986487 0.930774) |

Child layers that carry the look: span 14x1.5 background lab(62.6934 0.986487 0.930774); span 14x1.5 background lab(62.6934 0.986487 0.930774).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Mobile menu, open
The opened nav overlay: the Home / Explore / Sequence / Careers rows over the page with the Sign up pill at the foot. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 844; padding 0px 16px; background lab(100 0 0); shadow oklch(0.1591 0.00000406586 none / 0.12) 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 8px 0px; text cosmosOracle 32/35.2 500, lab(3.63782 -0.00000745058 0); transition transform 0.3s cubic-bezier(0, 0, 0.2, 1), translate 0.3s cubic-bezier(0, 0, 0.2, 1), scale 0.3s cubic-bezier(0, 0, 0.2, 1), rotate 0.3s cubic-bezier(0, 0, 0.2, 1); icon 100 x 16.84, lab(3.63782 -0.00000745058 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Mobile menu row
A row inside the opened nav overlay. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 358 x 69; padding 16px 0px; border B: 1px solid oklch(0.1591 0.00000406586 none / 0.12); background transparent; text cosmosOracle 32/35.2 500, lab(3.63782 -0.00000745058 0); layers a.border-primary.border-b 358.0x69.0 B:1px solid oklch(0.1591 0.00000406586 none / 0.12) |
| focus-visible | background lab(95.1978 0.212193 0.601578); layers none |

Child layers that carry the look: a 358x69 border 1px solid oklch(0.1591 0.00000406586 none / 0.12).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Mobile sign-up
The Sign up pill inside the mobile menu; measured, never followed. Read as `m-signup` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 358 x 56; padding 16px 24px; border 1px solid transparent; radius 3.35544e+07px; background lab(3.63782 -0.00000745058 0); text cosmosOracle 16/24 500, lab(100 0 0); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 358 x 104; background transparent; text cosmosOracle 32/32 700, lab(3.63782 -0.00000745058 0); layers span.block.size-9 39.6x39.6 lab(95.1978 0.212193 0.601578) T:1px solid lab(96.648 0.426352 1.20401) / R:1px solid lab(96.648 0.426352 1.20401) / B:1px solid lab(96.648 0.426352 1.20401) / L:1px solid lab(96.648 0.426352 1.20401) 12px; span.block.size-9 39.6x39.6 lab(95.1978 0.212193 0.601578) T:1px solid lab(96.648 0.426352 1.20401) / R:1px solid lab(96.648 0.426352 1.20401) / B:1px solid lab(96.6.

Child layers that carry the look: span 39.6x39.6 background lab(95.1978 0.212193 0.601578) border 1px solid lab(96.648 0.426352 1.20401) radius 12px; span 39.6x39.6 background lab(95.1978 0.212193 0.601578) border 1px solid lab(96.648 0.426352 1.20401) radius 12px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Cosmos mark, the social glyphs and the element imagery) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Everything behind the auth card — the saved-element feed, boards, clusters and settings — was never reached. The public /login card shows a username-or-email field, a password field with a visibility toggle, Forgot password and the Next pill; the fields were measured and Next was never pressed. What the product looks like past that card is not documented here.

### Pages

- **Sign up and start.** Join Cosmos for free, Sign up and the /start flow were measured or screenshotted, never followed past the first step; no account was created.
- **The login form** was focused and filled then cleared, never submitted — Next POSTs to Cosmos's own stack. The enabled state was read live after typing, then the fields were cleared.
- **Explore tab state.** The category tab-bar toggle selector never matched during the screenshot pass; the cat-tab component's measured states stand in, and the tab shot is missing.
- **Infinite feeds.** Search and profile pages report very tall scrollHeights (~23-24k px); full-page captures are bounded at 8 chunks and truncated there, recorded as a boundary.
- **External surfaces** (social profiles, the Instagram/TikTok/X links) are linked from the site but were never opened.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **The mega-menu auto-closes** a few seconds after it opens; each flyout-child state re-opened it with the Platform trigger before reading.

### Themes

The public surface paints a single light theme: data-theme stays "light" even under a forced prefers-color-scheme: dark emulation. The sheets declare a full --dark-* twin set (resolved into the export's dark theme from the same pass), plus .force-dark/.force-light section utilities — a declared dark mode the public pages never paint.

### Fonts

- **cosmosOracle** (700 on display headings, 400-500 elsewhere) is the single family; the @font-face blocks live in the same-origin Next.js sheets (harvested src list in raw/css-vars.json). The style guide falls back to system sans — the webfonts are licensed, not shipped.

### Screenshots

- The element imagery, brand/profile artwork and the Cosmos mark in the screenshots are the product's published content; only frames and components were measured.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Element imagery, masonry content, brand and profile artwork and marketing copy are the product's content; only frames and components were measured.
