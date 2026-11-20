# Epic Games components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from store.epicgames.com and www.epicgames.com on 2026-11-13 20:45, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page — including inside the <egs-navigation>/<egs-footer> shadow roots. Nothing was signed into, bought, downloaded or submitted; the sign-in form was never sent; Get, Add to Cart, Wishlist, Download and every purchase or provider action was measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (74 components, 208 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 14/20 500, #fffffff2`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (191 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every public surface paints `dark`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x (pages taller than the cap are chunked as `.partN`); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Discover (store home) | `/en-US/` | [default](screenshots/discover-dark-default.png), [full](screenshots/discover-dark-full.png), [search](screenshots/discover-dark-search.png) |
| Browse (legacy grid) | `/en-US/browse` | [default](screenshots/browse-dark-default.png), [full](screenshots/browse-dark-full.png) |
| Product page (Fortnite) | `/en-US/p/fortnite` | [default](screenshots/product-dark-default.png), [full](screenshots/product-dark-full.png) |
| Free Games | `/en-US/free-games` | [default](screenshots/freegames-dark-default.png), [full](screenshots/freegames-dark-full.png) |
| News | `/en-US/news` | [default](screenshots/news-dark-default.png), [full](screenshots/news-dark-full.png) |
| Launcher download | `/en-US/download` | [default](screenshots/download-dark-default.png), [full](screenshots/download-dark-full.png) |
| Sign in | `www.epicgames.com/id/login/epic` | [default](screenshots/signin-dark-default.png) |
| Marketing home | `www.epicgames.com/site/en-US/home` | [default](screenshots/sitehome-dark-default.png), [full](screenshots/sitehome-dark-full.png) |
| Support centre | `www.epicgames.com/help/en-US/` | [default](screenshots/help-dark-default.png), [full](screenshots/help-dark-full.png) |
| Discover, phone | `/en-US/ at 390` | [default](screenshots/mobile-discover-dark-default.png), [drawer](screenshots/mobile-discover-dark-drawer.png), [full](screenshots/mobile-discover-dark-full.png) |
| Product, phone | `/en-US/p/fortnite at 390` | [default](screenshots/mobile-product-dark-default.png), [full](screenshots/mobile-product-dark-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Consent/cookie layer | every page | hidden, never answered (no consent button was ever clicked) | hidden before every shot and reading |
| Cloudflare challenge | store.epicgames.com | an intermittent 'Just a moment...' gate; retried with fresh browser contexts until a real load — the check itself was never clicked | gaps where a page stayed gated |
| Search suggestions | Discover | the field's own focus, typed 'fort' then cleared — never submitted | [discover-dark-search](screenshots/discover-dark-search.png), [search-field](#search-field) |
| Sort listbox | /en-US/browse | the New Release control's own toggle — an option was never picked | [b-sort](#sort-dropdown) opened, [b-sort-item](#sort-option) |
| Filter accordion | /en-US/browse | the Genre group's own toggle — nothing was checked | [b-filter-group](#filter-accordion) opened, [b-checkbox](#filter-checkbox) |
| Mobile drawer | Discover at 390 | the hamburger's own toggle | [mobile-discover-dark-drawer](screenshots/mobile-discover-dark-drawer.png) |
| Signed-in product | an Epic account | every post-login surface, cart and checkout needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 33 components were given a real keyboard focus. 13 draw an outline ring: `store-tab` (1px solid rgba(255, 255, 255, 0.95) `color.foreground.primary`, offset 2px), `game-card` (1px solid #ffffff `color.background.fill.strong.default`, offset -1px), `b-page-link` (2px solid #ffffff `color.background.fill.strong.default`, offset 4px), `p-stage-next` (2px solid #ffffff `color.background.fill.strong.default`, offset -2px), `p-ratings-badge` (1px auto #101010, offset 1px), `p-follow` (2px solid #ffffff `color.background.fill.strong.default`, offset 4px), `n-card` (on a child: 1px auto rgb(16, 16, 16) offset 1px), `n-readmore` (1px auto #101010, offset 1px), `s-create` (2px solid #ffffff `color.background.fill.strong.default`, offset 4px), `w-tile` (on a child: 5px auto rgb(16, 16, 16) offset -2px), `w-explore` (5px auto #101010, offset -2px), `m-card` (1px auto #e59700, offset 1px), `d-cta` (1px auto #101010, offset 1px). 3 change only their border: `carousel-thumb`, `b-sort`, `b-filter-group`. The other 17 show no measured change: `pager-next`, `view-more`, `b-genre-card`, `b-card`, `b-wishlist`, `p-get`, `p-cart`, `p-wishlist`, `p-share`, `p-tag`, `p-sysreq-tab`, `fg-cta`, `fg-card`, `s-continue`, `s-console`, `s-social`, `h-tile`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover), including through the nav's shadow root. Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.12s | `cubic-bezier(0.65, 0, 0.35, 1)` | background-color, color | nav-distribute, nav-download, nav-signin |
| 0.125s | `ease-in-out` | background, background-color | b-filter-search, b-sort-item |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color | s-console, s-social |
| 0.2s | `ease` | border, border-color, color, transform | b-sort, carousel-thumb, p-follow, p-thumb, store-tab |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | box-shadow | s-dialog |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Hero slide](#hero-slide) | 868.75 x 488.67 | - | - | transparent | none | 0 |
| [Game card](#game-card) | 335.38 x 100 | - | 8px | transparent | none | 0 |
| [Grid game card](#grid-game-card) | 193.75 x 370.42 | - | - | transparent | none | 0 |
| [Genre card](#genre-card) | 255 x 229.8 | - | - | transparent | none | 0 |
| [Free game card](#free-game-card) | 346.67 x 301.41 | - | - | transparent | none | 0 |
| [Article card](#article-card) | 530 x 438.94 | - | - | transparent | none | 0 |
| [Sign-in dialog](#sign-in-dialog) | 562 x 972.19 | 1px solid rgba(255, 255, 255, 0.1) `color.background.fill.subdued.default` | 24px | #18181c `color.background.elevated.low` | none | 0 |
| [Product tile](#product-tile) | 480 x 868.5 | - | - | transparent | none | 0 |
| [Help tile](#help-tile) | 276.23 x 120 | - | - | transparent | none | 0 |

## Components

### Global navigation

The <egs-navigation> web component on every store page: the Epic mark, Distribute and locale controls, the translucent Sign-in pill and the #26bbff brand-blue Download — read through its open shadow root.

#### Global nav
The <egs-navigation> web component over every store page: Epic Games mark, STORE, Support, Distribute, the globe locale picker, Sign in and the blue Download pill. Shadow-DOM host; children measured through it. Read as `egs-nav` on the Discover page.

**Values (default).** size 1425 x 72; background transparent; text Inter 16/normal 400, rgba(255, 255, 255, 0.95) `color.foreground.primary`.

![Global nav default](components/crops/egs-nav-default.png)

#### Sign in button
The dark Sign-in pill in the global nav; links to the sign-in flow, measured never followed. Read as `nav-signin` on the Discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 71.97 x 32; padding 4px 12px; radius 6px; background rgba(255, 255, 255, 0.15) `color.background.fill.disabled.primary`; text Inter 14/24 500, #ffffff `color.background.fill.strong.default`; transition color 0.12s cubic-bezier(0.65, 0, 0.35, 1), background-color 0.12s cubic-bezier(0.65, 0, 0.35, 1) |
| hover, pressed | background rgba(255, 255, 255, 0.35) `color.background.fill.disabled.secondary` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Sign in button default](components/crops/nav-signin-default.png) ![Sign in button hover](components/crops/nav-signin-hover.png) ![Sign in button pressed](components/crops/nav-signin-pressed.png)

#### Download button
The blue Download pill in the global nav; measured never followed. Read as `nav-download` on the Discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 95.25 x 32; padding 4px 12px; radius 6px; background #26bbff `action.accent-brand`; text Inter 14/24 500, #000000 `color.border.focus.inverse`; transition color 0.12s cubic-bezier(0.65, 0, 0.35, 1), background-color 0.12s cubic-bezier(0.65, 0, 0.35, 1) |
| hover, pressed | background #72d3ff `action.accent-brand-hover` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Download button default](components/crops/nav-download-default.png) ![Download button hover](components/crops/nav-download-hover.png) ![Download button pressed](components/crops/nav-download-pressed.png)

#### Distribute menu
The Distribute dropdown in the global nav; measured, never opened. Read as `nav-distribute` on the Discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 116.81 x 41; padding 10px 16px; radius 8px; background transparent; text Inter 14/21 400, #ffffff `color.background.fill.strong.default`; transition color 0.12s cubic-bezier(0.65, 0, 0.35, 1), background-color 0.12s cubic-bezier(0.65, 0, 0.35, 1); icon 12 x 12, #ffffff `color.background.fill.strong.default` |
| hover | text Inter 14/21 400, rgba(255, 255, 255, 0.65) `color.border.strong.hover`; icon 12 x 12, rgba(255, 255, 255, 0.65) `color.border.strong.hover` |
| pressed | text Inter 14/21 400, rgba(255, 255, 255, 0.65) `color.border.strong.hover` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Distribute menu default](components/crops/nav-distribute-default.png) ![Distribute menu hover](components/crops/nav-distribute-hover.png) ![Distribute menu pressed](components/crops/nav-distribute-pressed.png)

#### Locale button
The globe locale picker in the global nav; measured, never opened. Read as `nav-locale` on the Discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; padding 4px; background transparent; text Inter 16/normal 400, rgba(255, 255, 255, 0.95) `color.foreground.primary`; icon 24 x 24, #ffffff `color.background.fill.strong.default` |
| hover, pressed | icon 24 x 24, rgba(255, 255, 255, 0.65) `color.border.strong.hover` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Locale button default](components/crops/nav-locale-default.png) ![Locale button hover](components/crops/nav-locale-hover.png) ![Locale button pressed](components/crops/nav-locale-pressed.png)

#### Global nav (mobile)
The <egs-navigation> at 390px. Read as `m-egs-nav` on the Discover page.

**Values (default).** size 390 x 72; background transparent; text Inter 16/normal 400, rgba(255, 255, 255, 0.95) `color.foreground.primary`.

![Global nav (mobile) default](components/crops/m-egs-nav-default.png)

### Store shell

The Discover/Browse/News tab bar under the nav on the #101014 canvas, and the store search field.

#### Store tab bar
The second bar under the global nav: search field plus Discover/Browse/News. Read as `store-tabs` on the Discover page.

**Values (default).** size 1425 x 100; padding 5px 0px; background #101014 `color.background.default`; text Inter 14/23.1 400, rgba(255, 255, 255, 0.95) `color.foreground.primary`.

![Store tab bar default](components/crops/store-tabs-default.png)

#### Store tab
The active "Discover" tab link; measured, never followed. Read as `store-tab` on the Discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 81.25 x 43.09; padding 10px; background transparent; text Inter 14/23.1 400, rgba(255, 255, 255, 0.95) `color.foreground.primary`; transition color 0.2s ease |
| focus-visible | radius 2px; outline 1px solid rgba(255, 255, 255, 0.95) `color.foreground.primary`, offset 2px; layers a._navLink_mrobj_135.active 81.3x43.1 1px solid rgba(255, 255, 255, 0.95) offset 2px 2px |

![Store tab default](components/crops/store-tab-default.png) ![Store tab hover](components/crops/store-tab-hover.png) ![Store tab focus-visible](components/crops/store-tab-focus-visible.png) ![Store tab pressed](components/crops/store-tab-pressed.png)

#### Search field
The "Search store" field in the store tab bar; focused and typed into then cleared — never submitted. Read as `search-field` on the Discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 230 x 40; padding 0px 13.6px 0px 39.95px; radius 9999px; background #202024 `color.background.elevated.medium`; text Arial 13.33/18.66 400, #ffffff `color.background.fill.strong.default`; placeholder rgba(255, 255, 255, 0.65) `color.border.strong.hover` |
| focused | background #404044 `color.neutral.400` |
| filled | padding 0px 40px 0px 39.95px; background #404044 `color.neutral.400` |

![Search field default](components/crops/search-field-default.png) ![Search field focused](components/crops/search-field-focused.png) ![Search field filled](components/crops/search-field-filled.png)

### Discover

The store home: the hero carousel with its Get CTA, thumbnails and pager, the shelf game cards with prices and wishlist corners, the View More ghost buttons.

#### Hero slide
The giant carousel slide (art + promo copy + Save Now) on Discover; measured, never followed. Read as `hero-slide` on the Discover page.

**Values (default).** size 868.75 x 488.67; background transparent; text Inter 16/normal 400, rgba(255, 255, 255, 0.95) `color.foreground.primary`; layers div::before.eds_370_127iqd00.eds_370_127iqd01 695pxx488.672px 0px 16px 16px 0px; button.eds_370_3ezmi30.eds_370_3ezmi31 111.3x48.0 rgb(255, 255, 255) 10px; button::before.eds_370_3ezmi30.eds_370_3ezmi31 119.25pxx56px T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) / L:2px solid rgb(255, 255, 255) 14px.

Child layers that carry the look: div::before 695pxx488.672px image linear-gradient(270deg, rgba(11, 11, 11, 0) 0%, #0b0b0b 100%) radius 0px 16px 16px 0px; button 111.3x48 background #ffffff `color.background.fill.strong.default` radius 10px; button::before 119.25pxx56px border 2px solid #ffffff `color.background.fill.strong.default` radius 14px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Hero CTA
The white "Save Now" pill on the hero slide; measured, never followed. Read as `hero-cta` on the Discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 111.25 x 48; padding 0px 20px; radius 10px; background #ffffff `color.background.fill.strong.default`; text Inter 14/19.6 500, rgba(0, 0, 0, 0.95) `color.foreground.inverse`; layers ::before rgba(0, 0, 0, 0) 2px none 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | background #a6a6a6 `color.background.fill.strong.hover` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Carousel rail item
A thumbnail button in the hero carousel rail ("Go to slide N"); measured, its own slide state pressed by hover only. Read as `carousel-thumb` on the Discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 180 x 78.95; padding 0px 10px 0px 0px; radius 8px; background #28282c `color.neutral.250`; text Inter 14/19.6 400, rgba(255, 255, 255, 0.95) `color.foreground.primary`; transition transform 0.2s ease |

![Carousel rail item default](components/crops/carousel-thumb-default.png) ![Carousel rail item hover](components/crops/carousel-thumb-hover.png) ![Carousel rail item focus-visible](components/crops/carousel-thumb-focus-visible.png) ![Carousel rail item pressed](components/crops/carousel-thumb-pressed.png)

#### Carousel pager
The right-chevron "Next page" rail control under a card shelf. Read as `pager-next` on the Discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 30 x 30; radius 9999px; background rgba(255, 255, 255, 0.15) `color.background.fill.disabled.primary`; text Inter 14/19.6 500, rgba(255, 255, 255, 0.95) `color.foreground.primary`; icon 20 x 20, rgba(255, 255, 255, 0.95) `color.foreground.primary`; layers ::before rgba(0, 0, 0, 0) 2px none 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | background rgba(255, 255, 255, 0.35) `color.background.fill.disabled.secondary` |

![Carousel pager default](components/crops/pager-next-default.png) ![Carousel pager hover](components/crops/pager-next-hover.png) ![Carousel pager focus-visible](components/crops/pager-next-focus-visible.png) ![Carousel pager pressed](components/crops/pager-next-pressed.png)

#### Game card
A store card (cover, title, price line, wishlist corner) in a Discover shelf; measured, never followed. Read as `game-card` on the Discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 335.38 x 100; radius 8px; background transparent; text Inter 16/normal 400, rgba(255, 255, 255, 0.95) `color.foreground.primary` |
| focus-visible | outline 1px solid #ffffff `color.background.fill.strong.default`, offset -1px; layers a._cardLink_1k614_83 335.4x100.0 1px solid rgb(255, 255, 255) offset -1px 8px |

![Game card default](components/crops/game-card-default.png) ![Game card hover](components/crops/game-card-hover.png) ![Game card focus-visible](components/crops/game-card-focus-visible.png) ![Game card pressed](components/crops/game-card-pressed.png)

#### Price line
The price/Free/Coming-Soon line inside a game card (region-priced, SGD on this run). Read as `card-price` on the Discover page.

**Values (default).** size 32.13 x 19.59; background transparent; text Inter 14/19.6 500, rgba(255, 255, 255, 0.95) `color.foreground.primary`.

![Price line default](components/crops/card-price-default.png)

#### Card wishlist button
The plus-corner "Add … to wishlist" icon button on a card; measured, never toggled. Read as `card-wishlist` on the Discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 48 x 48; radius 10px; background rgba(255, 255, 255, 0.15) `color.background.fill.disabled.primary`; text Inter 14/19.6 500, rgba(255, 255, 255, 0.95) `color.foreground.primary`; icon 20 x 20, rgba(255, 255, 255, 0.95) `color.foreground.primary`; layers ::before rgba(0, 0, 0, 0) 2px none 1; ::after rgba(0, 0, 0, 0) 0px none 1 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Card wishlist button hover](components/crops/card-wishlist-hover.png) ![Card wishlist button pressed](components/crops/card-wishlist-pressed.png)

#### View More
The shelf "View More" ghost button; measured, never followed. Read as `view-more` on the Discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 117.53 x 48; padding 0px 20px; radius 10px; background #ffffff `color.background.fill.strong.default`; text Inter 14/19.6 500, rgba(0, 0, 0, 0.95) `color.foreground.inverse`; layers ::before rgba(0, 0, 0, 0) 2px none 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | background #a6a6a6 `color.background.fill.strong.hover` |

![View More default](components/crops/view-more-default.png) ![View More hover](components/crops/view-more-hover.png) ![View More focus-visible](components/crops/view-more-focus-visible.png) ![View More pressed](components/crops/view-more-pressed.png)

### Browse (legacy grid)

The older /browse grid: the 'Popular Genres' heading, genre tiles, the New Release sort listbox, game cards, the Filters rail with its accordions, checkboxes and pagination.

#### Browse heading
"Popular Genres" — the display heading on the legacy browse page (a second "Browse" h1 is screen-reader-only). Read as `b-h1` on the Browse page.

**Values (default).** size 237 x 40; background transparent; text Inter Tight 32/40 900, #ffffff `color.background.fill.strong.default`.

![Browse heading default](components/crops/b-h1-default.png)

#### Genre card
A "Popular Genres" tile (art + label) linking to a filtered browse; measured, never followed. Read as `b-genre-card` on the Browse page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 255 x 229.8; background transparent; text Inter 16/26.4 400, #ffffff `color.background.fill.strong.default`; layers ::before rgba(0, 0, 0, 0) 1px none 1; a::before.css-c255xm 255pxx229.797px T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 4px; div.css-1u94dle 255.0x229.8 rgb(24, 24, 28) 12px; div::before.css-1u94dle 255pxx229.797px rgb(32, 32, 36); div.css-np40za 102.0x136.0 rgb(24, 24, 28) 4px; div.css-np40za 102.0x136.0 rgb(24, 24, 28)  |
| hover | layers ::before rgba(0, 0, 0, 0) 1px none 1; a::before.css-c255xm 255pxx229.797px T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 4px; div.css-1u94dle 255.0x229.8 rgb(24, 24, 28) 12px; div::before.css-1u94dle 255pxx229.797px rgb(64, 64, 68); div.css-np40za 102.0x136.0 rgb(24, 24, 28) 4px; div.css-np40za 102.0x136.0 rgb(24, 24, 28)  |
| focus-visible | layers ::before rgba(0, 0, 0, 0) 1px none 1; a::before.css-c255xm 255pxx229.797px T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, 255, 255) 4px; div.css-1u94dle 255.0x229.8 rgb(24, 24, 28) 12px; div::before.css-1u94dle 255pxx229.797px rgb(32, 32, 36); div.css-np40za 102.0x136.0 rgb(24, 24, 28) 4px; div.css-np40za 102.0x136.0 rgb(24,  |

Child layers that carry the look: a::before 255pxx229.797px border 1px solid transparent radius 4px; div 255x229.8 background #18181c `color.background.elevated.low` radius 12px; div::before 255pxx229.797px background #202024 `color.background.elevated.medium`.

![Genre card default](components/crops/b-genre-card-default.png) ![Genre card hover](components/crops/b-genre-card-hover.png) ![Genre card focus-visible](components/crops/b-genre-card-focus-visible.png) ![Genre card pressed](components/crops/b-genre-card-pressed.png)

#### Sort dropdown
The "New Release" sort control above the grid; opened with its own toggle for the listbox state — an option was never picked. Read as `b-sort` on the Browse page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 126.09 x 30; padding 0px 5px; border 1px solid transparent; background transparent; text Inter 14/19.6 400, #ffffff `color.background.fill.strong.default`; transition border 0.2s ease; icon 18 x 18, #ffffff `color.background.fill.strong.default` |
| focus-visible | border 1px solid #ffffff `color.background.fill.strong.default`; radius 4px |
| pressed | icon 18 x 18, rgba(255, 255, 255, 0.65) `color.border.strong.hover` |
| opened | border 1px solid #ffffff `color.background.fill.strong.default`; radius 4px |

![Sort dropdown default](components/crops/b-sort-default.png) ![Sort dropdown hover](components/crops/b-sort-hover.png) ![Sort dropdown focus-visible](components/crops/b-sort-focus-visible.png) ![Sort dropdown pressed](components/crops/b-sort-pressed.png) ![Sort dropdown opened](components/crops/b-sort-opened.png)

#### Sort option
An option inside the opened sort menu (button[role=menuitem]); measured, never picked. Read as `b-sort-item` on the Browse page.

**Values (default).** size 150.05 x 40.59; padding 10px 12px; radius 8px; background rgba(255, 255, 255, 0.15) `color.background.fill.disabled.primary`; text Inter 14/19.6 400, #ffffff `color.background.fill.strong.default`; transition background-color 0.125s ease-in-out; layers ::before rgba(0, 0, 0, 0) 1px none 1.

![Sort option default](components/crops/b-sort-item-default.png)

#### Grid game card
A game card in the legacy browse grid (cover, title, price, wishlist corner); measured, never followed. Read as `b-card` on the Browse page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 193.75 x 370.42; background transparent; text Inter 12/18 400, rgba(255, 255, 255, 0.65) `color.border.strong.hover`; layers ::before rgba(0, 0, 0, 0) 1px none 1; a::before.css-1k3j1r9 193.75pxx370.422px T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 4px; div.css-3f7x5i 193.8x258.3 8px; div::after.css-3f7x5i 193.75pxx258.328px rgb(255, 255, 255); div.eds_1xxntt80.eds_1be5iuz0 47.0x20.0 rgb(38, 187, 255) 9999px |
| focus-visible | layers ::before rgba(0, 0, 0, 0) 1px none 1; a::before.css-1k3j1r9 193.75pxx370.422px T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, 255, 255) 4px; div.css-3f7x5i 193.8x258.3 8px; div::after.css-3f7x5i 193.75pxx258.328px rgb(255, 255, 255); div.eds_1xxntt80.eds_1be5iuz0 47.0x20.0 rgb(38, 187, 255) 9999px |

Child layers that carry the look: a::before 193.75pxx370.422px border 1px solid transparent radius 4px; div 193.8x258.3 image linear-gradient(#202024 `color.background.elevated.medium`, #18181c `color.background.elev radius 8px; div::after 193.75pxx258.328px background #ffffff `color.background.fill.strong.default`.

![Grid game card default](components/crops/b-card-default.png) ![Grid game card hover](components/crops/b-card-hover.png) ![Grid game card focus-visible](components/crops/b-card-focus-visible.png) ![Grid game card pressed](components/crops/b-card-pressed.png)

#### Grid wishlist button
The "Add to Wishlist" corner button on a grid card; measured, never toggled. Read as `b-wishlist` on the Browse page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 44 x 44; background transparent; text Arial 13.33/normal 400, #ffffff `color.background.fill.strong.default`; icon 12 x 12, #ffffff `color.background.fill.strong.default`; layers div.css-8gd9c6 20.0x20.0 rgb(16, 16, 20) T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, 255, 255) 50% |

Child layers that carry the look: div 20x20 background #101014 `color.background.default` border 1px solid #ffffff `color.background.fill.strong.default` radius 50%.

![Grid wishlist button default](components/crops/b-wishlist-default.png) ![Grid wishlist button hover](components/crops/b-wishlist-hover.png) ![Grid wishlist button focus-visible](components/crops/b-wishlist-focus-visible.png) ![Grid wishlist button pressed](components/crops/b-wishlist-pressed.png)

#### Filters rail
The right-hand Filters aside: Events/Genre/Features/Types/Platform/Subscriptions accordions over a filter search. Read as `b-filters` on the Browse page.

**Values (default).** size 240 x 4509.72; background transparent; text Inter Tight 16/20 700, #ffffff `color.background.fill.strong.default`; icon 13 x 13, #ffffff `color.background.fill.strong.default`; layers div.css-15uavpg 240.0x500.0 rgb(32, 32, 36) T:1px solid rgba(255, 255, 255, 0.1) / R:1px solid rgba(255, 255, 255, 0.1) / B:1px solid rgba(255, 255, 255, 0.1) / L:1px solid rgba(255, 255, 255, 0.1) 12px; div::after.css-1n0v0ym 238pxx1px rgba(255, 255, 255, 0.15); input.css-7bziss 206.0x40.0 rgb(48, 48, 52) 4px; input::before.css-7bziss 100%x100% T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0.

Child layers that carry the look: div 240x500 background #202024 `color.background.elevated.medium` border 1px solid rgba(255, 255, 255, 0.1) `color.background.fill.subdued.default` radius 12px; div::after 238pxx1px background rgba(255, 255, 255, 0.15) `color.background.fill.disabled.primary`; input 206x40 background #303034 `color.background.elevated.high` radius 4px.

![Filters rail default](components/crops/b-filters-default.png)

#### Filter accordion
The "Genre" collapsible in the Filters rail; opened with its own toggle for the checkbox group — nothing was checked. Read as `b-filter-group` on the Browse page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 238 x 62; padding 20px 16px; border 1px solid transparent; background transparent; text Inter 14/19.6 400, #ffffff `color.background.fill.strong.default`; icon 20 x 20, rgba(255, 255, 255, 0.65) `color.border.strong.hover` |
| hover | background rgba(255, 255, 255, 0.15) `color.background.fill.disabled.primary` |
| focus-visible | border 1px solid #ffffff `color.background.fill.strong.default` |
| pressed, opened | background rgba(255, 255, 255, 0.15) `color.background.fill.disabled.primary` |

![Filter accordion default](components/crops/b-filter-group-default.png) ![Filter accordion hover](components/crops/b-filter-group-hover.png) ![Filter accordion focus-visible](components/crops/b-filter-group-focus-visible.png) ![Filter accordion pressed](components/crops/b-filter-group-pressed.png) ![Filter accordion opened](components/crops/b-filter-group-opened.png)

#### Filter checkbox
A checkbox row inside the opened Genre group (the control is a styled div, the input is visually hidden); never checked. Read as `b-checkbox` on the Browse page.

**Values (default).** size 206 x 24; background transparent; text Inter 14/19.6 400, rgba(255, 255, 255, 0.65) `color.border.strong.hover`; layers button.eds_52a16m7.eds_52a16m8 20.0x20.0 rgba(255, 255, 255, 0.05) T:1px solid rgba(255, 255, 255, 0.35) / R:1px solid rgba(255, 255, 255, 0.35) / B:1px solid rgba(255, 255, 255, 0.35) / L:1px solid rgba(255, 255, 255, 0.35) 4px.

Child layers that carry the look: button 20x20 background rgba(255, 255, 255, 0.05) `color.background.fill.faint` border 1px solid rgba(255, 255, 255, 0.35) `color.background.fill.disabled.secondary` radius 4px.

![Filter checkbox default](components/crops/b-checkbox-default.png)

#### Filter search
The "Filters" keyword field at the top of the rail; focused, never submitted. Read as `b-filter-search` on the Browse page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 206 x 40; padding 0px 30px 0px 40px; radius 4px; background #303034 `color.background.elevated.high`; text Arial 13.33/normal 400, #ffffff `color.background.fill.strong.default`; placeholder rgba(255, 255, 255, 0.65) `color.border.strong.hover`; layers ::before rgba(0, 0, 0, 0) 1px none 1 |
| focused | background #28282c `color.neutral.250`; transition background 0.125s ease-in-out |

![Filter search default](components/crops/b-filter-search-default.png) ![Filter search focused](components/crops/b-filter-search-focused.png)

#### Pagination
The numbered pagination under the grid. Read as `b-pagination` on the Browse page.

**Values (default).** size 823 x 30; background transparent; text Inter 14/19.6 400, #ffffff `color.background.fill.strong.default`; icon 12 x 12, #ffffff `color.background.fill.strong.default`; layers button::before.css-bp4ej3 30pxx30px rgba(255, 255, 255, 0.15) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 100%.

Child layers that carry the look: button::before 30pxx30px background rgba(255, 255, 255, 0.15) `color.background.fill.disabled.primary` border 1px solid transparent radius 100%.

![Pagination default](components/crops/b-pagination-default.png)

#### Page number
A page number inside the pagination; measured, never followed. Read as `b-page-link` on the Browse page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 27.2 x 19.59; padding 0px 10px; background transparent; text Inter 14/19.6 400, #ffffff `color.background.fill.strong.default` |
| focus-visible | radius 4px; outline 2px solid #ffffff `color.background.fill.strong.default`, offset 4px; layers a.eds_wy6w1n0.eds_1be5iuz0 27.2x19.6 2px solid rgb(255, 255, 255) offset 4px 4px |

![Page number default](components/crops/b-page-link-default.png) ![Page number hover](components/crops/b-page-link-hover.png) ![Page number focus-visible](components/crops/b-page-link-focus-visible.png) ![Page number pressed](components/crops/b-page-link-pressed.png)

### Product page

A game page (Fortnite): the title and ratings, sub-nav, stage art and thumbnails, the Get/Add-to-Cart/Wishlist column, price, share, tags, critic ratings, system requirements, add-ons and the follow control — measured, never followed.

#### Product title
The game title heading (Fortnite) at the top of the product page. Read as `p-title` on the product page.

**Values (default).** size 1068.75 x 48; background transparent; text Inter 40/48 700, rgba(255, 255, 255, 0.95) `color.foreground.primary`.

![Product title default](components/crops/p-title-default.png)

#### Rating block
The "4.3" Epic Player Ratings strip with its audience descriptors. Read as `p-rating` on the product page.

**Values (default).** size 535.73 x 20; background transparent; text Inter 14/19.6 400, rgba(255, 255, 255, 0.95) `color.foreground.primary`; icon 15 x 14, rgba(255, 255, 255, 0.95) `color.foreground.primary`.

![Rating block default](components/crops/p-rating-default.png)

#### Product tab
The active "Overview" tab in the product subnav (Overview/Add-Ons/Experiences/FAQ); measured, never followed. Read as `p-subnav` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 69 x 28; background transparent; text Inter 16/28 400, rgba(255, 255, 255, 0.95) `color.foreground.primary`; layers a::after._navLink_1x0oj_41._active_1x0oj_62 69pxx2px rgb(51, 191, 255) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: a::after 69pxx2px background #33bfff `color.palette.blue.400`.

![Product tab default](components/crops/p-subnav-default.png) ![Product tab hover](components/crops/p-subnav-hover.png) ![Product tab pressed](components/crops/p-subnav-pressed.png)

#### Gallery arrow
The right "Next image" arrow over the media stage; measured, never pressed. Read as `p-stage-next` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 56 x 56; padding 10px; background transparent; text Arial 13.33/normal 400, rgba(255, 255, 255, 0.95) `color.foreground.primary`; icon 36 x 36, rgba(255, 255, 255, 0.95) `color.foreground.primary` |
| focus-visible | radius 4px; outline 2px solid #ffffff `color.background.fill.strong.default`, offset -2px; layers button._stageButton_1361s_127 56.0x56.0 2px solid rgb(255, 255, 255) offset -2px 4px |

![Gallery arrow default](components/crops/p-stage-next-default.png) ![Gallery arrow hover](components/crops/p-stage-next-hover.png) ![Gallery arrow focus-visible](components/crops/p-stage-next-focus-visible.png) ![Gallery arrow pressed](components/crops/p-stage-next-pressed.png)

#### Gallery thumbnail
A thumbnail button in the media strip ("Slide N of 9"); measured, never pressed. Read as `p-thumb` on the product page.

**Values (default).** size 88.78 x 49.94; border 2px solid #ffffff `color.background.fill.strong.default`; radius 4px; background transparent; text Arial 13.33/normal 400, #000000 `color.border.focus.inverse`; transition border-color 0.2s ease.

![Gallery thumbnail default](components/crops/p-thumb-default.png)

#### Get button
The blue "Get" primary action in the buy panel; measured, never pressed. Read as `p-get` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 270 x 40; padding 0px 16px; radius 8px; background #33bfff `color.palette.blue.400`; text Inter 14/19.6 500, #0a2633 `color.palette.blue.100`; layers ::before rgba(0, 0, 0, 0) 2px none 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | background #69d0ff `color.palette.blue.500` |

![Get button default](components/crops/p-get-default.png) ![Get button hover](components/crops/p-get-hover.png) ![Get button focus-visible](components/crops/p-get-focus-visible.png) ![Get button pressed](components/crops/p-get-pressed.png)

#### Add to Cart
The square "Add to Cart" icon button beside Get; measured, never pressed. Read as `p-cart` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 311.66 x 40; padding 0px 16px; radius 8px; background #33bfff `color.palette.blue.400`; text Inter 14/19.6 500, #0a2633 `color.palette.blue.100`; layers ::before rgba(0, 0, 0, 0) 2px none 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | background #69d0ff `color.palette.blue.500` |

![Add to Cart default](components/crops/p-cart-default.png) ![Add to Cart hover](components/crops/p-cart-hover.png) ![Add to Cart focus-visible](components/crops/p-cart-focus-visible.png) ![Add to Cart pressed](components/crops/p-cart-pressed.png)

#### Wishlist button
The outlined "Wishlist" button under the buy panel; measured, never pressed. Read as `p-wishlist` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 320 x 40; padding 0px 16px; radius 8px; background rgba(255, 255, 255, 0.15) `color.background.fill.disabled.primary`; text Inter 14/19.6 500, rgba(255, 255, 255, 0.95) `color.foreground.primary`; icon 20 x 20, rgba(255, 255, 255, 0.95) `color.foreground.primary`; layers ::before rgba(0, 0, 0, 0) 2px none 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | background rgba(255, 255, 255, 0.35) `color.background.fill.disabled.secondary` |

![Wishlist button default](components/crops/p-wishlist-default.png) ![Wishlist button hover](components/crops/p-wishlist-hover.png) ![Wishlist button focus-visible](components/crops/p-wishlist-focus-visible.png) ![Wishlist button pressed](components/crops/p-wishlist-pressed.png)

#### Buy price
The "Free"/price line above the buy actions. Read as `p-price` on the product page.

**Values (default).** size 36.64 x 24; background transparent; text Inter 16/24 700, rgba(255, 255, 255, 0.95) `color.foreground.primary`.

![Buy price default](components/crops/p-price-default.png)

#### Share button
The "Share" ghost button beside Report in the buy rail; measured, never pressed. Read as `p-share` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 155 x 32; padding 0px 12px; radius 6px; background rgba(255, 255, 255, 0.15) `color.background.fill.disabled.primary`; text Inter 14/19.6 500, rgba(255, 255, 255, 0.95) `color.foreground.primary`; icon 20 x 20, rgba(255, 255, 255, 0.95) `color.foreground.primary`; layers ::before rgba(0, 0, 0, 0) 2px none 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | background rgba(255, 255, 255, 0.35) `color.background.fill.disabled.secondary` |

![Share button default](components/crops/p-share-default.png) ![Share button hover](components/crops/p-share-hover.png) ![Share button focus-visible](components/crops/p-share-focus-visible.png) ![Share button pressed](components/crops/p-share-pressed.png)

#### Tag chip
A genre tag chip under the description; links to a filtered browse, measured never followed. Read as `p-tag` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 58.38 x 24; padding 0px 10px; radius 9999px; background rgba(255, 255, 255, 0.15) `color.background.fill.disabled.primary`; text Inter 12/15.6 400, rgba(255, 255, 255, 0.95) `color.foreground.primary` |
| focus-visible | layers ::before rgba(0, 0, 0, 0) 2px none 1 |

![Tag chip default](components/crops/p-tag-default.png) ![Tag chip hover](components/crops/p-tag-hover.png) ![Tag chip focus-visible](components/crops/p-tag-focus-visible.png) ![Tag chip pressed](components/crops/p-tag-pressed.png)

#### Ratings badge
The age-ratings badge link (globalratings.com); measured, never followed. Read as `p-ratings-badge` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 46 x 78.78; background transparent; text Inter 16/normal 400, rgba(255, 255, 255, 0.95) `color.foreground.primary` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a._imageSlot_l9bj1_58._imageSlot_lg_l9bj1_63 46.0x78.8 1px auto rgb(16, 16, 16) offset 1px |

![Ratings badge default](components/crops/p-ratings-badge-default.png) ![Ratings badge hover](components/crops/p-ratings-badge-hover.png) ![Ratings badge focus-visible](components/crops/p-ratings-badge-focus-visible.png) ![Ratings badge pressed](components/crops/p-ratings-badge-pressed.png)

#### Section heading
A section heading inside the product overview. Read as `p-h2` on the product page.

**Values (default).** size 684.75 x 24; background transparent; text Inter 20/24 700, rgba(255, 255, 255, 0.95) `color.foreground.primary`.

![Section heading default](components/crops/p-h2-default.png)

#### Add-on row
An Add-Ons/Experiences row (art, title, Add-to-Cart, wishlist); measured, never followed. Read as `p-addon-row` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 367.66 x 44; background transparent; text Inter 12/15.6 400, rgba(255, 255, 255, 0.65) `color.border.strong.hover` |

![Add-on row default](components/crops/p-addon-row-default.png) ![Add-on row hover](components/crops/p-addon-row-hover.png)

#### Requirements tab
A platform tab in System Requirements; measured, never switched. Read as `p-sysreq-tab` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 61.97 x 40; background transparent; text Inter 14/19.6 400, rgba(255, 255, 255, 0.95) `color.foreground.primary`; layers ::before rgb(51, 191, 255) 0px none 1; button::before.eds_370_1lstq850.eds_370_j232ue0 61.9688pxx2px rgb(51, 191, 255) 2px |
| focus-visible | layers ::before rgb(51, 191, 255) 0px none 1; ::after rgba(0, 0, 0, 0) 2px none 1; button::before.eds_370_1lstq850.eds_370_j232ue0 61.9688pxx2px rgb(51, 191, 255) 2px; button::after.eds_370_1lstq850.eds_370_j232ue0 69.9688pxx24px T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) / L:2px solid rgb(255, 255, 255) 5px |

Child layers that carry the look: button::before 61.9688pxx2px background #33bfff `color.palette.blue.400` radius 2px.

![Requirements tab default](components/crops/p-sysreq-tab-default.png) ![Requirements tab hover](components/crops/p-sysreq-tab-hover.png) ![Requirements tab focus-visible](components/crops/p-sysreq-tab-focus-visible.png) ![Requirements tab pressed](components/crops/p-sysreq-tab-pressed.png)

#### Follow icon
A social icon link in Follow Us (Discord/homepage); measured, never followed. Read as `p-follow` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 28.64; background transparent; text Inter 16/26.4 400, rgba(255, 255, 255, 0.95) `color.foreground.primary`; transition color 0.2s ease, transform 0.2s ease; icon 28 x 28, rgba(255, 255, 255, 0.95) `color.foreground.primary` |
| hover | transform translate(0px, -1px) |
| focus-visible | radius 1px; outline 2px solid #ffffff `color.background.fill.strong.default`, offset 4px; transform translate(0px, -1px); layers a.eds_370_eifnjs0.eds_370_j232ue0 32.0x28.6 2px solid rgb(255, 255, 255) offset 4px 1px |
| pressed | transform translate(0px, -1px) |

![Follow icon default](components/crops/p-follow-default.png) ![Follow icon hover](components/crops/p-follow-hover.png) ![Follow icon focus-visible](components/crops/p-follow-focus-visible.png) ![Follow icon pressed](components/crops/p-follow-pressed.png)

### Free games

The Free Games page: the giveaway panel with its Install CTA, the Free Now/Coming Soon cards and badges.

#### Free Games heading
The "Free Games" display heading (the h1 itself is screen-reader-only). Read as `fg-h1` on the Free Games page.

**Values (default).** size 226 x 50; background transparent; text Inter Tight 40/50 900, #ffffff `color.background.fill.strong.default`.

![Free Games heading default](components/crops/fg-h1-default.png)

#### Giveaway CTA
The blue "Install Mobile and Claim Now" action in the Free Giveaway panel; links out to the mobile app, measured never followed. Read as `fg-cta` on the Free Games page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 264.84 x 40; padding 8px 16px; radius 8px; background #26bbff `action.accent-brand`; text Inter 14/19.6 500, #000000 `color.border.focus.inverse`; icon 20 x 20, #000000 `color.border.focus.inverse` |
| hover | background #72d3ff `action.accent-brand-hover` |
| focus-visible | layers ::before rgba(0, 0, 0, 0) 2px none 1 |

![Giveaway CTA default](components/crops/fg-cta-default.png) ![Giveaway CTA hover](components/crops/fg-cta-hover.png) ![Giveaway CTA focus-visible](components/crops/fg-cta-focus-visible.png) ![Giveaway CTA pressed](components/crops/fg-cta-pressed.png)

#### Free game card
A "Free Now"/"Coming Soon" game card on the free-games shelf; measured, never followed. Read as `fg-card` on the Free Games page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 346.67 x 301.41; background transparent; text Inter 12/15.99 700, #000000 `color.border.focus.inverse`; layers a::before.css-1k3j1r9 346.672pxx291.406px T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 4px; div.css-u3z0tz 346.7x195.0 8px; div::after.css-u3z0tz 346.672pxx195px rgb(255, 255, 255); div.css-82y1uz 346.7x26.0 rgb(38, 187, 255) |
| focus-visible | layers a::before.css-1k3j1r9 346.672pxx291.406px T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, 255, 255) 4px; div.css-u3z0tz 346.7x195.0 8px; div::after.css-u3z0tz 346.672pxx195px rgb(255, 255, 255); div.css-82y1uz 346.7x26.0 rgb(38, 187, 255) |

Child layers that carry the look: a::before 346.672pxx291.406px border 1px solid transparent radius 4px; div 346.7x195 image linear-gradient(#202024 `color.background.elevated.medium`, #18181c `color.background.elev radius 8px; div::after 346.672pxx195px background #ffffff `color.background.fill.strong.default`.

![Free game card default](components/crops/fg-card-default.png) ![Free game card hover](components/crops/fg-card-hover.png) ![Free game card focus-visible](components/crops/fg-card-focus-visible.png) ![Free game card pressed](components/crops/fg-card-pressed.png)

#### Free-now badge
The "Free Now - <date>" status label on a free-games card. Read as `fg-badge` on the Free Games page.

**Values (default).** size 240 x 20; background transparent; text Inter 16/26.4 400, rgba(255, 255, 255, 0.65) `color.border.strong.hover`.

![Free-now badge default](components/crops/fg-badge-default.png)

### News

The news index: heading, article cards and their Read more links.

#### News heading
The "Epic Games News" heading. Read as `n-h1` on the News page.

**Values (default).** size 1080 x 25.19; background transparent; text Inter 18/25.2 700, #ffffff `color.background.fill.strong.default`.

![News heading default](components/crops/n-h1-default.png)

#### Article card
A news article card (hero image, "Nd ago", headline, Read more); measured, never followed. Read as `n-card` on the News page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 530 x 438.94; background transparent; text Inter 9/normal 500, rgba(255, 255, 255, 0.65) `color.border.strong.hover`; layers div::after.css-1kqz5m5 530pxx298.125px; span.css-6xq2vb 81.0x21.0 B:1px solid rgba(255, 255, 255, 0.2) |
| focus-visible | layers a 530.0x298.1 1px auto rgb(16, 16, 16) offset 1px; div::after.css-1kqz5m5 530pxx298.125px; span.css-6xq2vb 81.0x21.0 B:1px solid rgba(255, 255, 255, 0.2) |

Child layers that carry the look: div::after 530pxx298.125px image linear-gradient(0deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.2)); span 81x21 border 1px solid rgba(255, 255, 255, 0.2).

![Article card default](components/crops/n-card-default.png) ![Article card hover](components/crops/n-card-hover.png) ![Article card focus-visible](components/crops/n-card-focus-visible.png) ![Article card pressed](components/crops/n-card-pressed.png)

#### Read more link
The "Read more" caption link inside an article card; measured, never followed. Read as `n-readmore` on the News page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 81 x 21; background transparent; text Inter 16/normal 400, #ffffff `color.background.fill.strong.default`; layers span.css-6xq2vb 81.0x21.0 B:1px solid rgba(255, 255, 255, 0.2) |
| hover | layers span.css-6xq2vb 81.0x21.0 B:1px solid rgba(255, 255, 255, 0.996) |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.css-1wb6qud 81.0x21.0 1px auto rgb(16, 16, 16) offset 1px; span.css-6xq2vb 81.0x21.0 B:1px solid rgba(255, 255, 255, 0.2) |

Child layers that carry the look: span 81x21 border 1px solid rgba(255, 255, 255, 0.2).

![Read more link default](components/crops/n-readmore-default.png) ![Read more link hover](components/crops/n-readmore-hover.png) ![Read more link focus-visible](components/crops/n-readmore-focus-visible.png) ![Read more link pressed](components/crops/n-readmore-pressed.png)

### Launcher download

The /download page: heading and the launcher download action.

#### Download heading
The "Download the Epic Games Launcher" heading (the h1 itself is screen-reader-only). Read as `d-h1` on the Download page.

**Values (default).** size 640 x 65; background transparent; text Inter Tight 52/65 900, #ffffff `color.background.fill.strong.default`.

![Download heading default](components/crops/d-h1-default.png)

#### Download CTA
The launcher download action (Windows/Mac); measured, never followed. Read as `d-cta` on the Download page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 176.48 x 20; background transparent; text Inter 14/19.6 500, #000000 `color.border.focus.inverse`; icon 20 x 20, #000000 `color.border.focus.inverse`; layers button.eds_14hl3lj9.eds_14hl3ljb 176.5x40.0 rgb(38, 187, 255) 8px |
| hover | layers button.eds_14hl3lj9.eds_14hl3ljb 176.5x40.0 rgb(114, 211, 255) 8px |
| focus-visible | outline 1px auto #101010, offset 1px; layers a 176.5x20.0 1px auto rgb(16, 16, 16) offset 1px; button.eds_14hl3lj9.eds_14hl3ljb 176.5x40.0 rgb(38, 187, 255) 8px |

Child layers that carry the look: button 176.5x40 background #26bbff `action.accent-brand` radius 8px.

![Download CTA default](components/crops/d-cta-default.png) ![Download CTA hover](components/crops/d-cta-hover.png) ![Download CTA focus-visible](components/crops/d-cta-focus-visible.png) ![Download CTA pressed](components/crops/d-cta-pressed.png)

### Sign-in dialog

The Epic account sign-in on www.epicgames.com/id: a MUI dialog with the mark, the Email field, a full-width Continue, console and social provider tiles — measured as a form, never submitted.

#### Sign-in dialog
The "Sign in to Epic Games" MUI modal (the MuiPaper card): Epic mark, e-mail field, Continue, console and social providers. Measured as a form, never submitted. Read as `s-dialog` on the sign-in page.

**Values (default).** size 562 x 972.19; border 1px solid rgba(255, 255, 255, 0.1) `color.background.fill.subdued.default`; radius 24px; background #18181c `color.background.elevated.low`; text Inter Tight 24/30 400, #ffffff `color.background.fill.strong.default`; transition box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 45 x 45, #ffffff `color.background.fill.strong.default`.

![Sign-in dialog default](components/crops/s-dialog-default.png)

#### Sign-in title
"Sign in to Epic Games" in the dialog. Read as `s-title` on the sign-in page.

**Values (default).** size 237 x 30; background transparent; text Inter Tight 24/30 400, #ffffff `color.background.fill.strong.default`.

![Sign-in title default](components/crops/s-title-default.png)

#### Email field
The "Email address" input; focused and typed into then cleared — never submitted. Read as `s-field-email` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 463 x 48; padding 13px 20px 12px 20px; radius 10px; background transparent; text Inter 16/22.4 400, #ffffff `color.background.fill.strong.default`; placeholder #aaaaae |
| focused, filled | size 461 x 48 |

![Email field default](components/crops/s-field-email-default.png) ![Email field focused](components/crops/s-field-email-focused.png) ![Email field filled](components/crops/s-field-email-filled.png)

#### Continue button
The blue "Continue" submit; its states were measured but it was never clicked — nothing was submitted. Read as `s-continue` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 464 x 48; padding 0px 20px; radius 10px; background #26bbff `action.accent-brand`; text Inter 16/22.4 500, #101014 `color.background.default`; layers ::before rgba(0, 0, 0, 0) 2px none 0 |
| hover | background #61cdff `action.accent-eds-hover` |
| focus-visible | layers ::before rgba(0, 0, 0, 0) 2px none 1 |

![Continue button default](components/crops/s-continue-default.png) ![Continue button hover](components/crops/s-continue-hover.png) ![Continue button focus-visible](components/crops/s-continue-focus-visible.png) ![Continue button pressed](components/crops/s-continue-pressed.png)

#### Create-account link
The "Create an account" link; measured, never followed. Read as `s-create` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 130.77 x 17; background transparent; text Inter 14/23.1 400, #26bbff `action.accent-brand` |
| focus-visible | radius 4px; outline 2px solid #ffffff `color.background.fill.strong.default`, offset 4px; layers a.MuiTypography-root.MuiTypography-inherit 130.8x17.0 2px solid rgb(255, 255, 255) offset 4px 4px |
| pressed | text Inter 14/23.1 400, #61cdff `action.accent-eds-hover` |

![Create-account link default](components/crops/s-create-default.png) ![Create-account link hover](components/crops/s-create-hover.png) ![Create-account link focus-visible](components/crops/s-create-focus-visible.png) ![Create-account link pressed](components/crops/s-create-pressed.png)

#### Console provider
A console sign-in tile (PlayStation/Xbox/Nintendo, MuiListItemButton divs); measured, never followed. Read as `s-console` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 149.33 x 102; padding 12px 0px; border 1px solid rgba(255, 255, 255, 0.05) `color.background.fill.faint`; radius 16px; background rgba(255, 255, 255, 0.05) `color.background.fill.faint`; text Inter 10/14 500, #ffffff `color.background.fill.strong.default`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #ffffff `color.background.fill.strong.default` |
| hover, focus-visible, pressed | background rgba(255, 255, 255, 0.16) |

![Console provider default](components/crops/s-console-default.png) ![Console provider hover](components/crops/s-console-hover.png) ![Console provider focus-visible](components/crops/s-console-focus-visible.png) ![Console provider pressed](components/crops/s-console-pressed.png)

#### Social provider
A "Other ways to sign in" provider tile (Google/Steam/Disney/Apple/Facebook/LEGO); measured, never followed. Read as `s-social` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 149.33 x 88; padding 12px 0px; border 1px solid rgba(255, 255, 255, 0.05) `color.background.fill.faint`; radius 16px; background rgba(255, 255, 255, 0.05) `color.background.fill.faint`; text Inter 10/14 500, #ffffff `color.background.fill.strong.default`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 23.86 x 23.72, rgba(255, 255, 255, 0.65) `color.border.strong.hover` |
| hover, focus-visible, pressed | background rgba(255, 255, 255, 0.16) |

![Social provider default](components/crops/s-social-default.png) ![Social provider hover](components/crops/s-social-hover.png) ![Social provider focus-visible](components/crops/s-social-focus-visible.png) ![Social provider pressed](components/crops/s-social-pressed.png)

### Marketing home

www.epicgames.com/site: the OpenSans marketing home with its giant product tiles and EXPLORE actions.

#### Product tile
A giant product tile (UNREAL ENGINE / FORTNITE / ROCKET LEAGUE / STORE) with its EXPLORE action on the OpenSans marketing home; measured, never followed. Read as `w-tile` on the marketing home page.

**Known-wrong reading.** The carousel rotated between states, so each state read a different tile (default UNREAL ENGINE, hover and focus-visible FORTNITE, pressed ROCKET LEAGUE): the state rows compare different elements. Only the default row describes one tile. Recapture needed.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 480 x 868.5; background transparent; text Inter_Bold 53.2/46.55 600, #ffffff `color.background.fill.strong.default`; layers a.btn.btn-primary 137.0x32.0 T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, 255, 255) rgba(0, 0, 0, 0.2) 2px 2px 2px 0px |
| focus-visible | layers a.btn.btn-primary 137.0x32.0 T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, 255, 255) rgba(0, 0, 0, 0.2) 2px 2px 2px 0px 5px auto rgb(16, 16, 16) offset -2px |

Child layers that carry the look: a 137x32 border 1px solid #ffffff `color.background.fill.strong.default` shadow rgba(0, 0, 0, 0.2) 2px 2px 2px 0px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Explore link
The EXPLORE caption on a product tile; measured, never followed. Read as `w-explore` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 137.05 x 32; padding 15px 25px; border 1px solid #ffffff `color.background.fill.strong.default`; background transparent; shadow rgba(0, 0, 0, 0.2) 2px 2px 2px 0px; text Helvetica Neue 18/24 400, #ffffff `color.background.fill.strong.default`; opacity 0 |
| hover | background #ffffff `color.background.fill.strong.default`; text Helvetica Neue 18/24 400, #222222 |
| focus-visible | outline 5px auto #101010, offset -2px |
| pressed | background #ffffff `color.background.fill.strong.default`; text Helvetica Neue 18/24 400, #222222 |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Wordmark
The Epic Games mark on the marketing page. Read as `w-wordmark` on the marketing home page.

Not on the page when it was captured.

### Support centre

epicgames.com/help: the dark support page — 'How can we help?', the search field, category tiles, the server-status chip and the chat launcher.

#### Help heading
"How can we help?" on the dark support centre. Read as `h-h1` on the support centre page.

**Values (default).** size 524.17 x 76.8; background transparent; text Inter 64/76.8 700, rgba(255, 255, 255, 0.95) `color.foreground.primary`.

![Help heading default](components/crops/h-h1-default.png)

#### Support search
The "Search support..." field; focused and typed into then cleared — never submitted. Read as `h-search` on the support centre page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 784 x 40; padding 0px 40px 0px 44px; border 1px solid rgba(255, 255, 255, 0.35) `color.background.fill.disabled.secondary`; radius 9999px; background rgba(255, 255, 255, 0.05) `color.background.fill.faint`; text Inter 14/19.6 400, rgba(255, 255, 255, 0.95) `color.foreground.primary`; placeholder rgba(255, 255, 255, 0.65) `color.border.strong.hover` |
| focused, filled | outline 2px solid #ffffff `color.background.fill.strong.default`, offset 2px |

![Support search default](components/crops/h-search-default.png) ![Support search focused](components/crops/h-search-focused.png) ![Support search filled](components/crops/h-search-filled.png)

#### Help tile
A support-category tile (Self-service/Explore topics/Games/Enterprise, a.Tile); measured, never followed. Read as `h-tile` on the support centre page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 276.23 x 120; background transparent; text Inter 20/24 700, rgba(255, 255, 255, 0.95) `color.foreground.primary`; icon 24 x 24, rgba(255, 255, 255, 0.95) `color.foreground.primary`; layers ::before rgba(0, 0, 0, 0) 2px none 1; a::before.Tile.GoToTile 284.234pxx128px T:2px solid rgba(0, 0, 0, 0) / R:2px solid rgba(0, 0, 0, 0) / B:2px solid rgba(0, 0, 0, 0) / L:2px solid rgba(0, 0, 0, 0) 20px; div.Tile__card.Tile__card--bottom 276.2x120.0 rgba(255, 255, 255, 0.05) 16px; div.Tile__inside-children 276.2x73.5 |
| hover | layers ::before rgba(0, 0, 0, 0) 2px none 1; a::before.Tile.GoToTile 284.234pxx128px T:2px solid rgba(0, 0, 0, 0) / R:2px solid rgba(0, 0, 0, 0) / B:2px solid rgba(0, 0, 0, 0) / L:2px solid rgba(0, 0, 0, 0) 20px; div.Tile__card.Tile__card--bottom 276.2x120.0 rgba(255, 255, 255, 0.1) 16px; div.Tile__inside-children 276.2x73.5 |
| focus-visible | layers ::before rgba(0, 0, 0, 0) 2px none 1; a::before.Tile.GoToTile 284.234pxx128px T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) / L:2px solid rgb(255, 255, 255) 20px; div.Tile__card.Tile__card--bottom 276.2x120.0 rgba(255, 255, 255, 0.1) 16px; div.Tile__inside-children 276.2x73.5 |

Child layers that carry the look: a::before 284.234pxx128px border 2px solid transparent radius 20px; div 276.2x120 background rgba(255, 255, 255, 0.05) `color.background.fill.faint` radius 16px; div 276.2x73.5 image linear-gradient(0deg, #000000 `color.border.focus.inverse`, rgba(0, 0, 0, 0.55) 67.5%, tra.

![Help tile default](components/crops/h-tile-default.png) ![Help tile hover](components/crops/h-tile-hover.png) ![Help tile focus-visible](components/crops/h-tile-focus-visible.png) ![Help tile pressed](components/crops/h-tile-pressed.png)

#### Server status chip
The "Server status" indicator, top right; measured never followed. Read as `h-status` on the support centre page.

**Values (default).** size 98.92 x 19.59; background transparent; text Inter 14/19.6 400, rgba(255, 255, 255, 0.95) `color.foreground.primary`.

![Server status chip default](components/crops/h-status-default.png)

#### Chat launcher
The round chat button bottom right; measured, never pressed. Read as `h-chat` on the support centre page.

**Known-wrong reading.** These readings are the "Back to top" button, not the chat launcher: `button:has(svg)` with `.last()` matched it. Recapture needed.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 150.09 x 48; padding 12px 20px; radius 8px; background rgba(255, 255, 255, 0.15) `color.background.fill.disabled.primary`; text Inter 14/21 400, #ffffff `color.background.fill.strong.default` |
| hover, pressed | background rgba(255, 255, 255, 0.35) `color.background.fill.disabled.secondary` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Chat launcher default](components/crops/h-chat-default.png) ![Chat launcher hover](components/crops/h-chat-hover.png) ![Chat launcher pressed](components/crops/h-chat-pressed.png)

### Mobile (390 wide)

The store at 390 x 844 at 2x: the condensed nav, hamburger and drawer, mobile hero and cards.

#### Hamburger
The mobile menu button; measured, the drawer itself is captured in screenshots. Read as `m-hamburger` on the Discover page at 390 wide.

**Known-wrong reading.** These readings are the "Epic Ecosystem Dropdown" button, not the mobile menu button: the selector's `button:has(svg)` fallback matched it first. Recapture needed.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 46 x 32; background transparent; text Inter 16/normal 400, rgba(255, 255, 255, 0.95) `color.foreground.primary`; icon 12 x 12, #ffffff `color.background.fill.strong.default` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Hamburger default](components/crops/m-hamburger-default.png) ![Hamburger hover](components/crops/m-hamburger-hover.png) ![Hamburger pressed](components/crops/m-hamburger-pressed.png)

#### Mobile hero card
The first card of the mobile store home. Read as `m-hero` on the Discover page at 390 wide.

**Values (default).** size 278.16 x 370.88; background transparent; text Inter 10/12 700, rgba(255, 255, 255, 0.95) `color.foreground.primary`; layers div::before.eds_370_127iqd00.eds_370_127iqd01 278.156pxx370.875px 16px; button.eds_370_3ezmi30.eds_370_3ezmi31 0.0x0.0 rgb(255, 255, 255) 10px; button::before.eds_370_3ezmi30.eds_370_3ezmi31 autoxauto T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) / L:2px solid rgb(255, 255, 255) 14px.

Child layers that carry the look: div::before 278.156pxx370.875px image linear-gradient(transparent 30%, rgba(11, 11, 11, 0.4) 60%, rgba(11, 11, 11, 0.9) 100%) radius 16px; button 0x0 background #ffffff `color.background.fill.strong.default` radius 10px; button::before autoxauto border 2px solid #ffffff `color.background.fill.strong.default` radius 14px.

![Mobile hero card default](components/crops/m-hero-default.png)

#### Mobile game card
A game card on the mobile discover feed. Read as `m-card` on the Discover page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 278.16 x 370.88; background transparent; text Inter 10/12 700, rgba(255, 255, 255, 0.95) `color.foreground.primary`; layers div::before.eds_370_127iqd00.eds_370_127iqd01 278.156pxx370.875px 16px 0px 0px 16px; button.eds_370_3ezmi30.eds_370_3ezmi31 0.0x0.0 rgb(255, 255, 255) 10px; button::before.eds_370_3ezmi30.eds_370_3ezmi31 autoxauto T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) / L:2px solid rgb(255, 255, 255) 14px; button.eds_370_3ezmi30.eds_370_3ezmi31 0.0x0.0 rgb |
| focus-visible | outline 1px auto #e59700, offset 1px; layers a._slideLink_1cvo7_107._slideLinkActive_1cvo7_124 278.2x370.9 1px auto rgb(229, 151, 0) offset 1px; div::before.eds_370_127iqd00.eds_370_127iqd01 278.156pxx370.875px 16px; button.eds_370_3ezmi30.eds_370_3ezmi31 0.0x0.0 rgb(255, 255, 255) 10px; button::before.eds_370_3ezmi30.eds_370_3ezmi31 autoxauto T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) /  |
| pressed | layers div::before.eds_370_127iqd00.eds_370_127iqd01 278.156pxx370.875px 16px; button.eds_370_3ezmi30.eds_370_3ezmi31 0.0x0.0 rgb(255, 255, 255) 10px; button::before.eds_370_3ezmi30.eds_370_3ezmi31 autoxauto T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) / L:2px solid rgb(255, 255, 255) 14px; button.eds_370_3ezmi30.eds_370_3ezmi31 0.0x0.0 rgba(255, 255, 2 |

Child layers that carry the look: div::before 278.156pxx370.875px image linear-gradient(transparent 30%, rgba(11, 11, 11, 0.4) 60%, rgba(11, 11, 11, 0.9) 100%) radius 16px 0px 0px 16px; button 0x0 background #ffffff `color.background.fill.strong.default` radius 10px; button::before autoxauto border 2px solid #ffffff `color.background.fill.strong.default` radius 14px.

![Mobile game card default](components/crops/m-card-default.png) ![Mobile game card hover](components/crops/m-card-hover.png) ![Mobile game card focus-visible](components/crops/m-card-focus-visible.png) ![Mobile game card pressed](components/crops/m-card-pressed.png)

#### Mobile search
The mobile search field; focused and typed into then cleared — never submitted. Read as `m-search` on the Discover page at 390 wide.

Not on the page when it was captured.

### Footer

The <egs-footer> web component at the bottom of every store page.

#### Global footer
The <egs-footer> web component at the bottom of every store page. Read as `egs-footer` on the Discover page.

**Values (default).** size 1425 x 878; padding 80px 64px; background #18181c `color.background.elevated.low`; text Inter 16/normal 400, rgba(255, 255, 255, 0.65) `color.border.strong.hover`.

![Global footer default](components/crops/egs-footer-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the glyphs in the crops and screenshots (the Epic mark, cart/wishlist/search glyphs, the platform and payment marks, game key art) are the product's artwork — Epic inlines them as component SVG inside hashed classes and web-component shadow roots rather than a liftable sprite. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The signed-in Epic lives behind the account — the game library, wishlist, cart, checkout, billing, refunds and account settings all need a login and were never reached. The store's browse/product/free-games surfaces and the sign-in dialog itself are genuinely public; the dialog was measured as a form and never submitted.

### Pages

- **The account.** Every post-login surface (library, wishlist, orders, settings) was never reached.
- **Cart and checkout.** Add to Cart, Get, Buy Now and every price/payment action was measured, never followed; the cart drawer and checkout are unmeasured.
- **Downloads.** The launcher Download action and the product download were never followed; no binary was fetched.
- **Provider sign-in.** The console/social provider tiles were measured, never followed; no OAuth flow was started.
- **Cloudflare.** Fresh headless contexts hit the 'Just a moment' challenge intermittently; captures retry on a fresh context and never keep a blocked page's reading.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover) so a state a script adds on mousedown (if any) is missing; on the few shadow-DOM controls the protocol could not reach, the state is recorded as failed rather than absent.
- **Disabled, error and loading states** were not seen on the public surface.
- **The Discover search field** was measured last on its page: typing into it opens a live results layer; it was typed into ('fort') and cleared, never submitted.
- **Zero-size targets.** A few page elements rendered 0 x 0 at capture (sr-only headings, hidden duplicate inputs, a collapsed help tile row); their nearest visible sibling was measured instead and the misses are recorded in raw/components-computed.json.

### Themes

Every public Epic surface paints one theme: the dark EGS palette on the store, sign-in, support and marketing pages. There is no light theme or toggle, so tokens.json carries a single `dark` set over the shared `core` scales. The store bundle's Lightning-CSS light/dark helper names resolve the same dark values on this surface.

### Fonts

- **Inter** (300/400/500/700) is every control and body line; **Inter Tight** (700/900) is the display face; **Recursive Mono** is the declared code face; **OpenSans** paints the www marketing home. They are served woff2; the style guide falls back to system sans.

### Screenshots

- Game key art, logos, the Epic mark and any photography in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- Full-page shots are chunked at the eight-chunk cap; mobile Discover and product pages needed `.part0`/`.part1` splits, and anything past the cap is a documented truncation.

### Content left out

- Game titles, artwork, prices (SGD on this run), news copy and ratings are the product's content; only frames and components were measured.
