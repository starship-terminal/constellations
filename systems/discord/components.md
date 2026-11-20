# Discord components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from discord.com on 2026-11-15, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted and no form was ever sent; nav links, category pills, Join/Log In buttons and Share were measured, never followed. The app surfaces paint their dark theme signed out; the marketing chrome inside them paints .theme-light, so both themes are real painted evidence.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (46 components, 99 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (98 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{state}.png`: there is no theme toggle signed out — the marketing pages paint the Webflow palette and the app surfaces paint .theme-dark.theme-darker, each captured as it renders. Desktop shots are 1440 x 900 at 1x; the phone surfaces are `mobile-{page}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-default.png), [full](screenshots/home-full.png) |
| Download | `/download` | [default](screenshots/download-default.png), [full](screenshots/download-full.png) |
| Nitro | `/nitro` | [default](screenshots/nitro-default.png), [full](screenshots/nitro-full.png) |
| Server discovery | `/servers` | [default](screenshots/servers-default.png), [full](screenshots/servers-full.png), [gaming-default](screenshots/servers-gaming-default.png), [gaming-full](screenshots/servers-gaming-full.png) |
| Gaming discovery | `/servers/gaming` | [default](screenshots/servers-gaming-default.png), [full](screenshots/servers-gaming-full.png) |
| Server detail | `/servers/midjourney-662267976984297473` | [default](screenshots/server-default.png), [full](screenshots/server-full.png) |
| Log in | `/login` | [default](screenshots/login-default.png), [full](screenshots/login-full.png) |
| Register | `/register` | [default](screenshots/register-default.png), [full](screenshots/register-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-default.png), [full](screenshots/mobile-home-full.png) |
| Discovery, phone | `/servers` | [default](screenshots/mobile-servers-default.png), [full](screenshots/mobile-servers-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Search field | /servers | the discovery search input was focused and filled ("fortnite", then deleted — the query runs client-side, nothing submitted) | [ds-search-input](#search-input) |
| Auth fields | /login and /register | the email fields were focused and filled (never submitted); focused and filled states recorded | [lg-email](#email-field), [rg-email](#register-email) |
| The signed-in app | a Discord account | joining servers, accepting invites, the whole client at /channels/* all need an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 15 components were given a real keyboard focus. 7 draw an outline ring: `mk-nav-download` (2px solid #ffffff `background.surface.high`, offset -2px), `mk-nav-login` (2px solid #5865f2 `badge.expressive.background`, offset 4px), `dl-cta` (1px solid #5865f2 `badge.expressive.background`, offset 1px), `nt-cta` (2px solid #5865f2 `badge.expressive.background`, offset 4px), `ds-tab` (2px solid #6aa8f4 `color.blue.new.30`, offset 2px), `ds-tab-all` (2px solid #6aa8f4 `color.blue.new.30`, offset 2px), `sv-share` (2px solid #6aa8f4 `color.blue.new.30`, offset 2px). The other 8 show no measured change: `mk-cta-download`, `mk-cta-open`, `sv-join`, `sv-chip`, `lg-submit`, `lg-forgot`, `lg-register`, `rg-submit`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.05s | `ease-in` | background-color, border-color, color, opacity | lg-submit, rg-submit |
| 0.2s | `ease-in-out` | background-color, border-color, box-shadow, color, none | ds-search-input, lg-email, mk-cta-open, sv-join |
| 0.25s | `ease` | background-color | mk-nav-login |
| 0.3s | `ease` | all | dl-cta, mk-cta-download |
| 0.4s | `ease` | background-color, font-variation-settings | dl-cta, mk-nav-download, nt-cta |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Server card](#server-card) | 322 x 362 | - | - | transparent | none | 0 |
| [Auth card](#auth-card) | 784 x 414 | - | 8px | #242429 `color.neutral.79` | rgba(0, 0, 0, 0.2) 0px 2px 10px 0px | 32px |
| [Nitro plan card](#nitro-plan-card) | 590 x 683.38 | - | 96px | #1a1a1e `background.card` | rgba(69, 42, 124, 0.1) 0px 2px 32px 0px | 32px 32px 56px 32px |
| [Mobile server card](#mobile-server-card) | 358 x 380 | - | - | transparent | none | 0 |

## Components

### Marketing chrome

The marketing top bar and footer (Ggsans, the Webflow build): the fixed nav with its section links and the white Log In pill.

#### Marketing nav
The fixed marketing top bar — Discord wordmark, section links, Log In pill. Read as `mk-nav` on the marketing home page.

**Values (default).** size 1440 x 80; background transparent; text Abcgintodiscord 16/22 500, #000000 `badge.inverted.background`; icon 16 x 16, #ffffff `background.surface.high`; layers a.skip-link.w-inline-block 205.0x48.0 #35ed7e `color.illo.green.40` 12px; div.nav_dd_content-wr.isnew 0.0x0.0 #5865f2 `badge.expressive.background` 40px; div.nav_dd_content-wr.isnew 0.0x0.0 #5865f2 `badge.expressive.background` 40px; div.nav_dd_link-group.is_2025 0.0x0.0 R:1px solid rgba(255, 255, 255, 0.1); div.nav_dd_content-wr.isnew 0.0x0.0 #5865f2 `badge.expressive.background` 40px; div.nav_dd.

Child layers that carry the look: a 205x48 background #35ed7e `color.illo.green.40` radius 12px; div 0x0 background #5865f2 `badge.expressive.background` radius 40px; div 0x0 background #5865f2 `badge.expressive.background` radius 40px.

![Marketing nav default](components/crops/mk-nav-default.png)

#### Nav link
The Download nav link; measured, never followed. Read as `mk-nav-download` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 110 x 39.2; padding 10px 16px; radius 12px; background transparent; text Abcgintodiscord 16/19.2 500, #ffffff `background.surface.high`; transition font-variation-settings 0.4s ease |
| hover | background #5865f2 `badge.expressive.background` |
| focus-visible | radius 1px; outline 2px solid #ffffff `background.surface.high`, offset -2px; layers a.nav_link 110.0x39.2 2px solid #ffffff `background.surface.high` offset -2px 1px |
| pressed | background #5865f2 `badge.expressive.background` |

![Nav link default](components/crops/mk-nav-download-default.png) ![Nav link hover](components/crops/mk-nav-download-hover.png) ![Nav link focus-visible](components/crops/mk-nav-download-focus-visible.png) ![Nav link pressed](components/crops/mk-nav-download-pressed.png)

#### Nav dropdown
The Discover nav dropdown trigger; measured, never opened through. Read as `mk-nav-drop` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 117 x 39.2; background transparent; text Abcgintodiscord 16/19.2 500, #ffffff `background.surface.high`; icon 16 x 16, #ffffff `background.surface.high`; layers div.nav_dd_content-wr.isnew 0.0x0.0 #5865f2 `badge.expressive.background` 40px |
| hover | layers div.nav_dd_trigger.w-dropdown-toggle 117.0x39.2 #5865f2 `badge.expressive.background` 12px; div.nav_dd_content-wr.isnew 203.0x167.2 #5865f2 `badge.expressive.background` 40px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: div 0x0 background #5865f2 `badge.expressive.background` radius 40px.

![Nav dropdown default](components/crops/mk-nav-drop-default.png) ![Nav dropdown hover](components/crops/mk-nav-drop-hover.png) ![Nav dropdown pressed](components/crops/mk-nav-drop-pressed.png)

#### Nav Log In
The white Log In pill in the nav; measured, never followed. Read as `mk-nav-login` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 80.5 x 39.19; padding 10px 16px; radius 16px; background #ffffff `background.surface.high`; text Abcgintodiscord 16/19.2 500, #000000 `badge.inverted.background`; transition background-color 0.25s ease |
| hover | background #c7c8ce `color.plum.6` |
| focus-visible | radius 1px; outline 2px solid #5865f2 `badge.expressive.background`, offset 4px |
| pressed | background #c7c8ce `color.plum.6` |

![Nav Log In default](components/crops/mk-nav-login-default.png) ![Nav Log In hover](components/crops/mk-nav-login-hover.png) ![Nav Log In focus-visible](components/crops/mk-nav-login-focus-visible.png) ![Nav Log In pressed](components/crops/mk-nav-login-pressed.png)

### Marketing hero

The home hero: the giant Ggsans display headline over the blurple gradient, the white Download CTA and the brand-fill Open-Discord button.

#### Hero display
"GROUP CHAT THAT’S ALL FUN & GAMES" — the hero display headline in Ggsans. Read as `mk-h1` on the marketing home page.

**Values (default).** size 491.19 x 144; background transparent; text Abcgintodiscordnord 56/48 700, #ffffff `background.surface.high`.

![Hero display default](components/crops/mk-h1-default.png)

#### Hero lede
The hero supporting paragraph. Read as `mk-lede` on the marketing home page.

**Values (default).** size 491.19 x 104; background transparent; text Abcgintodiscord 20/26 400, #ffffff `background.surface.high`.

![Hero lede default](components/crops/mk-lede-default.png)

#### Hero primary CTA
The "Download for …" white button; hover/focus measured, never followed (it would start a download). Read as `mk-cta-download` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 262.5 x 65; padding 15px 24px; radius 12px; background #ffffff `background.surface.high`; text Abcgintodiscord 20/26 400, #23272a `not.quite.black.default`; transition all 0.3s ease; icon 24 x 24, #23272a `not.quite.black.default` |
| hover, pressed | background #c7c8ce `color.plum.6`; shadow rgba(0, 0, 0, 0.2) 0px 8px 15px 0px |

![Hero primary CTA default](components/crops/mk-cta-download-default.png) ![Hero primary CTA hover](components/crops/mk-cta-download-hover.png) ![Hero primary CTA focus-visible](components/crops/mk-cta-download-focus-visible.png) ![Hero primary CTA pressed](components/crops/mk-cta-download-pressed.png)

#### Hero secondary CTA
The "Open Discord in your browser" brand-fill button; measured, never followed. Read as `mk-cta-open` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 324 x 65; padding 19.5px 24px; radius 12px; background #5865f2 `badge.expressive.background`; text Abcgintodiscord 20/26 400, #ffffff `background.surface.high`; transition none 0.2s ease-in-out; layers ::after transparent 0px none 0 |
| hover, pressed | layers ::after transparent 0px none 1 |

![Hero secondary CTA default](components/crops/mk-cta-open-default.png) ![Hero secondary CTA hover](components/crops/mk-cta-open-hover.png) ![Hero secondary CTA focus-visible](components/crops/mk-cta-open-focus-visible.png) ![Hero secondary CTA pressed](components/crops/mk-cta-open-pressed.png)

### Marketing page

The /download and /nitro pages: light marketing surfaces with their own headings, plan cards and CTAs.

#### Download heading
"Download Discord wherever you hang out" — the download page heading. Read as `dl-h1` on the download page.

**Values (default).** size 924 x 194.39; background transparent; text Abcgintodiscordnord 72/64.8 700, #ffffff `background.surface.high`.

![Download heading default](components/crops/dl-h1-default.png)

#### Download CTA
A platform download button; measured, never followed. Read as `dl-cta` on the download page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 228.5 x 48; padding 15px 24px 14px 24px; radius 12px; background transparent; text ABC Ginto Normal 16/20.8 500, #ffffff `background.surface.high`; transition all 0.3s ease, background-color 0.4s ease; icon 20 x 20, #ffffff `background.surface.high` |
| focus-visible | outline 1px solid #5865f2 `badge.expressive.background`, offset 1px; layers a.btn.download-button 228.5x48.0 1px solid #5865f2 `badge.expressive.background` offset 1px 12px |

![Download CTA default](components/crops/dl-cta-default.png) ![Download CTA hover](components/crops/dl-cta-hover.png) ![Download CTA focus-visible](components/crops/dl-cta-focus-visible.png) ![Download CTA pressed](components/crops/dl-cta-pressed.png)

#### Nitro heading
"UNLOCK A WORLD OF PERKS WITH NITRO" — the Nitro page display heading. Read as `nt-h1` on the nitro page.

**Values (default).** size 788 x 194.39; background transparent; text Abcgintodiscordnord 72/64.8 700, #ffffff `background.surface.high`.

![Nitro heading default](components/crops/nt-h1-default.png)

#### Nitro plan card
A Nitro plan/perk card on the marketing page. Read as `nt-card` on the nitro page.

**Values (default).** size 590 x 683.38; padding 32px 32px 56px 32px; radius 96px; background #1a1a1e `background.card`; shadow rgba(69, 42, 124, 0.1) 0px 2px 32px 0px; text Abcgintodiscordnord 36/36 700, #ffffff `background.surface.high`.

![Nitro plan card default](components/crops/nt-card-default.png)

#### Nitro CTA
A Nitro subscribe button; measured, never followed. Read as `nt-cta` on the nitro page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 121 x 48; padding 14.4px 24px 13.6px 24px; radius 12px; background #ffffff `background.surface.high`; text Abcgintodiscord 16/20.8 500, #000000 `badge.inverted.background`; transition background-color 0.4s ease |
| hover | background #c7c8ce `color.plum.6` |
| focus-visible | radius 1px; background #c7c8ce `color.plum.6`; outline 2px solid #5865f2 `badge.expressive.background`, offset 4px |
| pressed | background #c7c8ce `color.plum.6` |

![Nitro CTA default](components/crops/nt-cta-default.png) ![Nitro CTA hover](components/crops/nt-cta-hover.png) ![Nitro CTA focus-visible](components/crops/nt-cta-focus-visible.png) ![Nitro CTA pressed](components/crops/nt-cta-pressed.png)

### Server discovery

The /servers discovery page — app surface painted .theme-dark.theme-darker: the DISCOVERABLE SERVERS display heading, the search box and the category pill row.

#### Discovery heading
"DISCOVERABLE SERVERS" — the display-lg heading on the app discovery page (painted under .theme-dark.theme-darker). Read as `ds-h1` on the server discovery page.

**Values (default).** size 1440 x 56; padding 0px 8px; background transparent; text ABC Ginto Discord Nord 56/56 700, #ffffff `badge.expressive.background`.

![Discovery heading default](components/crops/ds-h1-default.png)

#### Search box
The "Search servers for games and interests" field wrapper on discovery. Read as `ds-search` on the server discovery page.

**Values (default).** size 640 x 64; background transparent; text gg sans 12/16 400, #ffffff `badge.expressive.background`; icon 24 x 24, #ffffff `badge.expressive.background`; layers div.searchBox__7pJSN.searchBarContainer__J-bNz 640.0x64.0 rgba(255, 255, 255, 0.12) `color.opacity.white.12` T:1px solid transparent / R:1px solid transparent / B:1px solid transparent / L:1px solid transparent 12px.

Child layers that carry the look: div 640x64 background rgba(255, 255, 255, 0.12) `color.opacity.white.12` border 1px solid transparent radius 12px.

![Search box default](components/crops/ds-search-default.png)

#### Search input
The discovery search input; the filled state types "fortnite" then deletes it — the query runs client-side, nothing is submitted or signed in. Read as `ds-search-input` on the server discovery page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 570 x 32; radius 3px; background transparent; text gg sans 16/16 400, #ffffff `badge.expressive.background`; transition border-color 0.2s ease-in-out; placeholder rgba(255, 255, 255, 0.75) |
| filled | size 419.61 x 32 |

![Search input default](components/crops/ds-search-input-default.png) ![Search input focused](components/crops/ds-search-input-focused.png) ![Search input filled](components/crops/ds-search-input-filled.png)

#### Category pill
A category filter pill (Gaming) — a real link to /servers/gaming; measured, never followed. Read as `ds-tab` on the server discovery page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 146.13 x 57.03; padding 16px 24px; border 1px solid transparent; radius 12px; background transparent; text gg sans 24/23.04 500, #ffffff `badge.expressive.background`; opacity 0.5; icon 16 x 16, #ffffff `badge.expressive.background` |
| hover | opacity none |
| focus-visible | outline 2px solid #6aa8f4 `color.blue.new.30`, offset 2px; opacity none |
| pressed | opacity none |

![Category pill default](components/crops/ds-tab-default.png) ![Category pill hover](components/crops/ds-tab-hover.png) ![Category pill focus-visible](components/crops/ds-tab-focus-visible.png) ![Category pill pressed](components/crops/ds-tab-pressed.png)

#### Category pill (All)
The "All" category pill — the selected state of the filter row. Read as `ds-tab-all` on the server discovery page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 96.56 x 57.03; padding 16px 24px; border 1px solid rgba(151, 151, 159, 0.12) `app.frame.border`; radius 12px; background rgba(151, 151, 159, 0.16) `color.opacity.16`; text gg sans 24/23.04 500, #ffffff `badge.expressive.background`; icon 16 x 16, #ffffff `badge.expressive.background`; layers ::before transparent 0px none 1 |
| focus-visible | outline 2px solid #6aa8f4 `color.blue.new.30`, offset 2px |

![Category pill (All) default](components/crops/ds-tab-all-default.png) ![Category pill (All) hover](components/crops/ds-tab-all-hover.png) ![Category pill (All) focus-visible](components/crops/ds-tab-all-focus-visible.png) ![Category pill (All) pressed](components/crops/ds-tab-all-pressed.png)

#### Category heading
The Gaming category discovery page heading. Read as `gs-h1` on the gaming discovery page.

**Values (default).** size 1440 x 56; padding 0px 8px; background transparent; text ABC Ginto Discord Nord 56/56 700, #ffffff `badge.expressive.background`.

![Category heading default](components/crops/gs-h1-default.png)

#### Category pill (selected)
The Gaming pill on /servers/gaming — the painted selected state. Read as `gs-tab-gaming` on the gaming discovery page.

**Values (default).** size 146.13 x 57.03; padding 16px 24px; border 1px solid rgba(151, 151, 159, 0.12) `app.frame.border`; radius 12px; background rgba(151, 151, 159, 0.16) `color.opacity.16`; text gg sans 24/23.04 500, #ffffff `badge.expressive.background`; icon 16 x 16, #ffffff `badge.expressive.background`; layers ::before transparent 0px none 1.

![Category pill (selected) default](components/crops/gs-tab-gaming-default.png)

### Server card

A discoverable-server card in the grid: banner art, squircle icon, name with verified badge, description and the Online/Members counts.

#### Server card
A discoverable-server card — banner art, icon, name, verified badge, description, member counts; hover measured, never followed. Read as `sc-card` on the server discovery page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 322 x 362; background transparent; text gg sans 20/24 600, #fbfbfb `badge.secondary.text`; icon 16 x 16, #23a559; layers article.guildItemContainer_OnY3sU 322.0x362.0 #202024 `background.base.low` T:1px solid rgba(151, 151, 159, 0.12) `app.frame.border` / R:1px solid rgba(151, 151, 159, 0.12) `app.frame.border` / B:1px solid rgba(151, 151, 159, 0.12) `app.frame.border` / L:1px solid rgba(151, 151, 159, 0.12) `app.frame.border` 8px; div.listIconContainer_OnY3sU 59.7x59.7 #202024 `background.base.low` 12.7893px; div.d |
| hover | layers article.guildItemContainer_OnY3sU 322.0x362.0 #242429 `background.surface.high` T:1px solid rgba(151, 151, 159, 0.44) `color.opacity.44` / R:1px solid rgba(151, 151, 159, 0.44) `color.opacity.44` / B:1px solid rgba(151, 151, 159, 0.44) `color.opacity.44` / L:1px solid rgba(151, 151, 159, 0.44) `color.opacity.44` rgba(0, 0, 0, 0.14) 0px 1px 4px 0px 8px; div.listIconContainer_OnY3sU 59.7x59.7 #24242 |

Child layers that carry the look: article 322x362 background #202024 `background.base.low` border 1px solid rgba(151, 151, 159, 0.12) `app.frame.border` radius 8px; div 59.7x59.7 background #202024 `background.base.low` radius 12.7893px; div 8x8 background #43b581 `mint.green` radius 50%.

![Server card default](components/crops/sc-card-default.png) ![Server card hover](components/crops/sc-card-hover.png)

#### Server name
The server name line inside the card, with its verified check. Read as `sc-name` on the server discovery page.

**Values (default).** size 99 x 24; background transparent; text gg sans 20/24 600, #fbfbfb `badge.secondary.text`.

![Server name default](components/crops/sc-name-default.png)

#### Member counts
The "N Online · N Members" line — the green presence dot plus counts. Read as `sc-members` on the server discovery page.

**Values (default).** size 115 x 18; background transparent; text gg sans 14/18 400, #efeff1 `color.neutral.5`.

![Member counts default](components/crops/sc-members-default.png)

#### Server icon
The squircle server icon overlapping the card banner. Read as `sc-icon` on the server discovery page.

**Values (default).** size 51.19 x 51.19; radius 8.53333px; background transparent; text gg sans 16/18.4 400, #efeff1 `color.neutral.5`.

![Server icon default](components/crops/sc-icon-default.png)

### Server detail

A /servers/<slug> detail page: banner, server name with verified badge, member counts, the brand-fill Join CTA, Share button and category chips.

#### Server banner
The server detail page banner art. Read as `sv-banner` on the server detail page.

**Values (default).** size 1440 x 600; background transparent; text gg sans 16/18.4 400, #efeff1 `color.neutral.5`.

![Server banner default](components/crops/sv-banner-default.png)

#### Server name
The server title with the verified badge — display type. Read as `sv-name` on the server detail page.

**Values (default).** size 264 x 32.19; background transparent; text ABC Ginto Discord Nord 28/32.2 700, #ffffff `badge.expressive.background`; icon 24 x 24, #23a559.

![Server name default](components/crops/sv-name-default.png)

#### Member counts
The "N Online · N Members" line under the name. Read as `sv-members` on the server detail page.

**Values (default).** size 89 x 18.19; background transparent; text gg sans 14/18.2 500, #96979e `color.neutral.29`.

![Member counts default](components/crops/sv-members-default.png)

#### Join CTA
The brand-fill "Join the Conversation" button; hover/focus measured, never followed — joining needs an account. Read as `sv-join` on the server detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 320 x 48; padding 0px 24px; radius 12px; background #5865f2 `color.blurple.50`; text gg sans 16/20.8 500, #ffffff `badge.expressive.background`; transition background-color 0.2s ease-in-out, color 0.2s ease-in-out, box-shadow 0.2s ease-in-out |
| hover | background #4752c4 `color.brand.560` |

![Join CTA default](components/crops/sv-join-default.png) ![Join CTA hover](components/crops/sv-join-hover.png) ![Join CTA focus-visible](components/crops/sv-join-focus-visible.png)

#### Share button
The Share button under the member counts; measured, never pressed. Read as `sv-share` on the server detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 320 x 44; padding 12px; radius 12px; background transparent; text gg sans 16/20 500, #efeff1 `color.neutral.5`; icon 16 x 16, #efeff1 `color.neutral.5` |
| focus-visible | outline 2px solid #6aa8f4 `color.blue.new.30`, offset 2px; layers button.trigger__sNXK6 320.0x44.0 2px solid #6aa8f4 `color.blue.new.30` offset 2px 12px |

![Share button default](components/crops/sv-share-default.png) ![Share button hover](components/crops/sv-share-hover.png) ![Share button focus-visible](components/crops/sv-share-focus-visible.png) ![Share button pressed](components/crops/sv-share-pressed.png)

#### Category chip
A category chip in the detail sidebar; measured, never followed. Read as `sv-chip` on the server detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 122 x 38; padding 10px 16px; radius 10px; background rgba(151, 151, 159, 0.12) `app.frame.border`; text gg sans 14/18 500, #efeff1 `color.neutral.5` |

![Category chip default](components/crops/sv-chip-default.png) ![Category chip hover](components/crops/sv-chip-hover.png) ![Category chip focus-visible](components/crops/sv-chip-focus-visible.png) ![Category chip pressed](components/crops/sv-chip-pressed.png)

#### About heading
The tracked ABOUT section label. Read as `sv-about` on the server detail page.

**Values (default).** size 800 x 28.8; background transparent; text ABC Ginto Discord Nord 24/28.8 700, #fbfbfb `badge.secondary.text`.

![About heading default](components/crops/sv-about-default.png)

### Sign-in / register

The auth surfaces on the animated brand backdrop: the Welcome-back card with its fields, brand-fill Log In submit, QR-code panel and the register card. Measured signed out; never submitted.

#### Auth card
The sign-in card on the animated brand backdrop — form fields left, QR panel right. Read as `lg-card` on the login page.

**Values (default).** size 784 x 414; padding 32px; radius 8px; background #242429 `background.surface.high`; shadow rgba(0, 0, 0, 0.2) 0px 2px 10px 0px; text gg sans 24/32 600, #fbfbfb `badge.secondary.text`; icon 16 x 16, #fbfbfb `badge.secondary.text`.

![Auth card default](components/crops/lg-card-default.png)

#### Sign-in heading
"Welcome back!" — the auth card heading. Read as `lg-h1` on the login page.

**Values (default).** size 156 x 32; background transparent; text gg sans 24/32 600, #fbfbfb `badge.secondary.text`.

![Sign-in heading default](components/crops/lg-h1-default.png)

#### Email field
The "Email or Phone Number" field; the filled state types an address then deletes it — nothing is submitted. Read as `lg-email` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 414 x 44; padding 12px 10px; radius 8px; background transparent; text gg sans 16/normal 400, #efeff1 `color.neutral.5`; transition border-color 0.2s ease-in-out; placeholder #8f9097 `color.neutral.31` |

![Email field default](components/crops/lg-email-default.png) ![Email field focused](components/crops/lg-email-focused.png) ![Email field filled](components/crops/lg-email-filled.png)

#### Password field
The password field with the reveal-button affordance; focused via a click-in, never filled. Read as `lg-pass` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 374 x 38; padding 1px 0px 1px 12px; background transparent; text gg sans 16/normal 400, #efeff1 `color.neutral.5`; placeholder #8f9097 `color.neutral.31` |

![Password field default](components/crops/lg-pass-default.png) ![Password field focused](components/crops/lg-pass-focused.png)

#### Log In button
The brand-fill Log In submit; hover/focus measured, never pressed — it would submit the sign-in. Read as `lg-submit` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 416 x 40; border 1px solid rgba(255, 255, 255, 0.08) `color.opacity.white.8`; radius 8px; background #5865f2 `color.blurple.50`; text gg sans 16/20 500, #ffffff `badge.expressive.background`; transition background-color 0.05s ease-in, color 0.05s ease-in, border-color 0.05s ease-in, opacity 0.05s ease-in |
| hover | background #4452bb `color.blurple.60`; transition background-color 0.15s ease-out, color 0.15s ease-out, border-color 0.15s ease-out, opacity 0.15s ease-out |

![Log In button default](components/crops/lg-submit-default.png) ![Log In button hover](components/crops/lg-submit-hover.png) ![Log In button focus-visible](components/crops/lg-submit-focus-visible.png)

#### Forgot link
The "Forgot your password?" link; measured, never followed. Read as `lg-forgot` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 135 x 18; background transparent; text gg sans 14/18 400, #798df9 `color.blurple.36` |

![Forgot link default](components/crops/lg-forgot-default.png) ![Forgot link hover](components/crops/lg-forgot-hover.png) ![Forgot link focus-visible](components/crops/lg-forgot-focus-visible.png) ![Forgot link pressed](components/crops/lg-forgot-pressed.png)

#### Register link
The "Need an account? Register" link; measured, never followed. Read as `lg-register` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 49 x 18; background transparent; text gg sans 14/18 400, #798df9 `color.blurple.36` |

![Register link default](components/crops/lg-register-default.png) ![Register link hover](components/crops/lg-register-hover.png) ![Register link focus-visible](components/crops/lg-register-focus-visible.png) ![Register link pressed](components/crops/lg-register-pressed.png)

#### QR panel
The "Log in with QR Code" panel on the card’s right. Read as `lg-qr` on the login page.

**Values (default).** size 240 x 322; background transparent; text gg sans 24/32 600, #fbfbfb `badge.secondary.text`; layers div.qrCodeContainer_d4-PpI.qrCode_FDXpbQ 176.0x176.0 #ffffff `badge.expressive.background` 4px.

Child layers that carry the look: div 176x176 background #ffffff `badge.expressive.background` radius 4px.

![QR panel default](components/crops/lg-qr-default.png)

#### Register heading
"Create an account" — the register card heading. Read as `rg-h1` on the register page.

**Values (default).** size 416 x 32; background transparent; text gg sans 24/32 600, #fbfbfb `badge.secondary.text`.

![Register heading default](components/crops/rg-h1-default.png)

#### Register email
The register email field; the filled state types an address then deletes it — nothing is submitted. Read as `rg-email` on the register page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 414 x 38; padding 1px 12px; background transparent; text gg sans 16/normal 400, #efeff1 `color.neutral.5`; placeholder #8f9097 `color.neutral.31` |

![Register email default](components/crops/rg-email-default.png) ![Register email focused](components/crops/rg-email-focused.png) ![Register email filled](components/crops/rg-email-filled.png)

#### Create Account
The Create Account submit; hover/focus measured, never pressed. Read as `rg-submit` on the register page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 416 x 40; border 1px solid rgba(255, 255, 255, 0.08) `color.opacity.white.8`; radius 8px; background #5865f2 `color.blurple.50`; text gg sans 16/20 500, #ffffff `badge.expressive.background`; transition background-color 0.05s ease-in, color 0.05s ease-in, border-color 0.05s ease-in, opacity 0.05s ease-in |
| hover | background #4452bb `color.blurple.60`; transition background-color 0.15s ease-out, color 0.15s ease-out, border-color 0.15s ease-out, opacity 0.15s ease-out |

![Create Account default](components/crops/rg-submit-default.png) ![Create Account hover](components/crops/rg-submit-hover.png) ![Create Account focus-visible](components/crops/rg-submit-focus-visible.png)

### Mobile (390 wide)

The phone surface at 390 wide: the marketing bar, discovery heading, search and a server card.

#### Mobile nav
The phone marketing bar over discovery. Read as `m-bar` on the server discovery page at 390 wide.

**Values (default).** size 342 x 64; background transparent; text ABC Ginto Discord 16/18.4 400, #ffffff `background.surface.high`; layers a.button_vOYBES.overlayFocusRing_vOYBES 0.0x0.0 #ffffff `background.surface.high` 12px; button.menuIcon__mQgbA 40.0x40.0 rgba(255, 255, 255, 0.1) 14px.

Child layers that carry the look: a 0x0 background #ffffff `background.surface.high` radius 12px; button 40x40 background rgba(255, 255, 255, 0.1) radius 14px.

![Mobile nav default](components/crops/m-bar-default.png)

#### Mobile heading
The DISCOVERABLE SERVERS display at 390px. Read as `m-h1` on the server discovery page at 390 wide.

**Values (default).** size 390 x 62.41; padding 0px 8px; background transparent; text ABC Ginto Discord Nord 31.2/31.2 700, #ffffff `background.surface.high`.

![Mobile heading default](components/crops/m-h1-default.png)

#### Mobile search
The discovery search field at 390px. Read as `m-search` on the server discovery page at 390 wide.

**Values (default).** size 358 x 64; padding 12px 16px; border 1px solid transparent; radius 12px; background rgba(255, 255, 255, 0.12) `color.opacity.white.12`; text gg sans 12/16 400, #ffffff `badge.expressive.background`; icon 24 x 24, #ffffff `badge.expressive.background`.

![Mobile search default](components/crops/m-search-default.png)

#### Mobile server card
A server card at 390px. Read as `m-card` on the server discovery page at 390 wide.

**Values (default).** size 358 x 380; background transparent; text gg sans 20/24 600, #fbfbfb `badge.secondary.text`; icon 16 x 16, #23a559; layers article.guildItemContainer_OnY3sU 358.0x380.0 #202024 `background.base.low` T:1px solid rgba(151, 151, 159, 0.12) `app.frame.border` / R:1px solid rgba(151, 151, 159, 0.12) `app.frame.border` / B:1px solid rgba(151, 151, 159, 0.12) `app.frame.border` / L:1px solid rgba(151, 151, 159, 0.12) `app.frame.border` 8px; div.listIconContainer_OnY3sU 66.4x66.4 #202024 `background.base.low` 14.2281px; div.d.

Child layers that carry the look: article 358x380 background #202024 `background.base.low` border 1px solid rgba(151, 151, 159, 0.12) `app.frame.border` radius 8px; div 66.4x66.4 background #202024 `background.base.low` radius 14.2281px; div 8x8 background #43b581 `mint.green` radius 50%.

![Mobile server card default](components/crops/m-card-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Clyde wordmark, the verified check, category glyphs, server icons and the QR code) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The whole client needs an account — /channels/@me redirects to /login, invites are not accepted, and joining a server, messages, guild settings and Nitro purchase all gate on sign-in. What is genuinely public signed out: the marketing site (/, /download, /nitro, /safety, /blog, /terms, /careers), the server-discovery pages (/servers, /servers/<category>, /servers/<slug-id>) and the auth cards (/login, /register). The Join and Log In buttons were measured, never pressed.

### Pages

- **Join, Log In and Share actions.** The server-detail Join and Share buttons and the auth submits gate on sign-in; they were measured at default/hover/focus-visible/pressed, never pressed.
- **Invite pages.** /invite/<code> returned a dark frame signed out in this pass (the invite card did not paint); recorded as a boundary.
- **Cookie banner.** A consent banner painted on first load; it was hidden for screenshots only — no consent choice was made.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

There is no theme toggle signed out. The app surfaces paint .theme-dark.theme-darker (verified #121214 base); the marketing chrome injected into them paints .theme-light, so both themes are measured live. The app's own light surface — what the account theme setting would paint on /channels/* — is declared in the stylesheets (.theme-light) but never renders signed out: the light.* tokens resolve the declared layer, honestly labelled.

### Fonts

- **gg sans** (the app's UI and body text), **ABC Ginto Discord Nord** (the display face — DISCOVERABLE SERVERS, hero and section headings), **ABC Ginto** (marketing display) and **gg mono** (declared code face) are the served families; the marketing pages run **Ggsans** under the Webflow build. They are served from Discord's CDN; the style guide falls back to system fonts.

### Screenshots

- Full-page shots are single document captures; the marketing pages' animated hero fields are motion media, frozen at capture time.
- Server names, descriptions, member counts, banners and icons are the servers' published content; screenshots are 256-colour PNGs, read exact colours from the tokens or the raw files.

### Content left out

- Server names, descriptions, banners, icons and member counts are the servers' published content; only frames and components were measured.
