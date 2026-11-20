# Fable components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from fable.co on 2026-11-14, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, joined, bought or submitted; the sign-in form was never sent; every link and CTA was measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (81 components, 215 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `heldane 58/58 400, #161015`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (213 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the mode the page painted at capture: `light` for every page except /discover, which paints `dark`. The stylesheet also carries a scoped `.dark` token layer used by app reading/detail surfaces, but no captured public page presents it as a user theme toggle — the dark token set resolves those declarations separately from the discover page's paint. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Clubs index | `/clubs` | [default](screenshots/clubs-light-default.png), [full](screenshots/clubs-light-full.png), [search](screenshots/clubs-light-search.png) |
| Genre shelf | `/club/fantasy` | [default](screenshots/genre-light-default.png), [full](screenshots/genre-light-full.png) |
| Club detail | `/club/the-cozy-chaos-book-club-with-summer-england-372871533779?club_type=free` | [default](screenshots/club-light-default.png), [full](screenshots/club-light-full.png) |
| Books index | `/books` | [default](screenshots/books-light-default.png), [full](screenshots/books-light-full.png) |
| Book detail | `/book/heated-rivalry-by-rachel-reid-9780369748898` | [default](screenshots/book-light-default.png), [full](screenshots/book-light-full.png), [spoilers](screenshots/book-light-spoilers.png) |
| Discover cover wall | `/discover#b=...&src=home` | [default](screenshots/discover-dark-default.png) |
| Blog index | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Blog article | `/blog/how-to-start-a-book-club` | [default](screenshots/blogpost-light-default.png), [full](screenshots/blogpost-light-full.png) |
| Support | `/support` | [default](screenshots/support-light-default.png), [full](screenshots/support-light-full.png) |
| Sign in | `/signin` | [default](screenshots/signin-light-default.png) |
| Sign up | `/signup` | [default](screenshots/signup-light-default.png) |
| Community guidelines | `/community-guidelines` | [default](screenshots/guidelines-light-default.png), [full](screenshots/guidelines-light-full.png) |
| Not found | `a missing route` | [default](screenshots/notfound-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [nav](screenshots/mobile-home-light-nav.png) |
| Clubs, phone | `/clubs` | [default](screenshots/mobile-clubs-light-default.png), [full](screenshots/mobile-clubs-light-full.png) |
| Book, phone | `/book/heated-rivalry-by-rachel-reid-9780369748898` | [default](screenshots/mobile-book-light-default.png), [full](screenshots/mobile-book-light-full.png) |
| Discover, phone | `/discover` | [default](screenshots/mobile-discover-dark-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie consent | every page | any consent layer was hidden before the shot, never answered | hidden before every shot and reading |
| Club search modal | /clubs | the 'Find a club' search trigger's own open/close — a local dialog | [clubs-light-search](screenshots/clubs-light-search.png), [search-modal](#find-a-club-modal), [search-input](#search-input), [search-close](#modal-close-button) |
| Spoiler disclosure | /book/* | the spoiler pill's own toggle — reveals hidden review text locally | [book-light-spoilers](screenshots/book-light-spoilers.png), [spoiler-pill](#spoiler-disclosure) |
| Read more | /book/* | the 'Read more' toggle's own expansion — a local collapse | [read-more](#read-more-toggle) |
| Club FAQ accordion | /club/* | the FAQ question's own expand/collapse | [faq-q](#faq-question) |
| Mobile nav sheet | home page, phone width | the menu button's own toggle — a full-viewport sheet | [mobile-home-light-nav](screenshots/mobile-home-light-nav.png), [m-nav](#mobile-nav-sheet), [m-nav-link](#nav-sheet-link) |
| Sign-in fields | /signin | focused and filled with sample values then cleared — never submitted | [field-email](#email-field), [field-password](#password-field) |
| Signed-in product | a Fable account | every post-login surface (joined clubs, discussions, the reader, lists) needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 37 components were given a real keyboard focus. 33 draw an outline ring: `mkt-nav-link` (2px solid #116ecd, offset 4px), `mkt-signin` (2px solid #116ecd, offset 4px), `mkt-cart` (2px solid #116ecd, offset 4px), `getapp-hero` (2px solid #116ecd, offset 4px), `getapp-dark` (2px solid #116ecd, offset 4px), `getapp-cta` (2px solid #116ecd, offset 4px), `footer-link` (2px solid #116ecd, offset 4px), `cat-nav-link` (2px solid #0064c3 `color.royal.400`, offset 4px), `cat-signin` (2px solid #0064c3 `color.royal.400`, offset 2px), `search-trigger` (2px solid #0064c3 `color.royal.400`, offset 2px), `search-close` (2px solid #0064c3 `color.royal.400`, offset 2px), `genre-pill` (1px auto #101010, offset 1px), `genre-scroll` (1px auto #101010, offset 0px), `search-icon-btn` (1px auto #101010, offset 0px), `author-link` (1px auto #101010, offset 1px), `ratings-line` (1px auto #101010, offset 1px), `btn-primary` (2px solid #0064c3 `color.royal.400`, offset 2px), `btn-secondary` (2px solid #0064c3 `color.royal.400`, offset 2px), `spoiler-pill` (2px solid #0064c3 `color.royal.400`, offset 2px), `read-more` (1px auto #101010, offset 0px), `author-profile-btn` (2px solid #0064c3 `color.royal.400`, offset 2px), `join-cta` (2px solid #0064c3 `color.royal.400`, offset 2px), `share-btn` (2px solid #0064c3 `color.royal.400`, offset 2px), `faq-q` (1px auto #101010, offset 0px), `show-btn` (2px solid #116ecd, offset 4px), `submit-btn` (2px solid #116ecd, offset 4px), `sso-google` (2px solid #116ecd, offset 4px), `sso-apple` (2px solid #116ecd, offset 4px), `reset-link` (2px solid #116ecd, offset 4px), `signup-link` (2px solid #116ecd, offset 4px), `m-getapp` (2px solid #116ecd, offset 4px), `m-menu-btn` (2px solid #116ecd, offset 4px), `m-nav-link` (2px solid #116ecd, offset 4px). The other 4 show no measured change: `help-card`, `email-card`, `disc-random`, `disc-whatis`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `ease` | background-color, border-color, color, opacity | author-profile-btn, btn-primary, btn-secondary, cat-nav-link, cat-signin, icon-btn, icon-btn-book, join-cta and more |
| 0.2s | `ease` | background, background-color, border, box-shadow, color, opacity, transform | cat-header, disc-field, disc-random, disc-whatis, disc-wordmark, email-card, field-email, field-password and more |
| 0.4s | `ease-in-out` | transform | club-card |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Sign-in form](#sign-in-form) | 396 x 172 | - | - | transparent | none | 0 |
| [Find a club modal](#find-a-club-modal) | 480 x 497 | 1px solid rgba(7, 6, 7, 0.1) `color.dark.fade.10` | 24px | #ffffff `color.white.default` | rgba(0, 0, 0, 0.12) 0px -6px 16px 0px | 0 |
| [App download banner](#app-download-banner) | 1440 x 132 | - | - | #053829 `color.forest.300` | none | 0 |
| [Club card](#club-card) | 248 x 380 | - | - | transparent | none | 0 |
| [Club card (catalog)](#club-card-catalog) | 256 x 372 | - | 24px | transparent | none | 0 |
| [Book card](#book-card) | 167 x 290.5 | - | - | transparent | none | 0 |
| [Help card](#help-card) | 610 x 120 | - | - | transparent | none | 18px |

## Components

### Site chrome

Two header skins share the group: the emotion-styled marketing header on / (cream bar, wordmark, Clubs / Books / Library / Blog links, sign-in and cart icons) and the CSS-module catalog header on /clubs, /books, /book/* and /club/* (same links over a white bar).

#### Marketing header
The fixed transparent top bar over the green hero: Fable wordmark, Clubs/Books/Library/Blog links, the "Sign up or log in" and cart icons. Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 60; background transparent; shadow rgba(0, 0, 0, 0.04) 0px 2px 3px -2px; text Inter 14/14 600, #f7f4ee `color.pearl.extra.light`; icon 82 x 33, #000000; layers header.css-1vg9pjt 1440.0x60.0 rgba(0, 0, 0, 0.04) 0px 2px 3px -2px; div.css-1g7irsi 200.0x50.0 rgb(255, 255, 255) T:1px rgb(237, 237, 237) / R:1px rgb(237, 237, 237) / B:1px rgb(237, 237, 237) / L:1px rgb(237, 237, 237) rgba(0, 0, 0, 0.08) 0px 4px 12px 0px 12px; span.css-1pyn1fk 17.0x17.0 rgb(255, 255, 255) T:1px rgb(237, 237, 237) / L:1px rgb(237, 237, 237) 2px 0px 0px.

![Marketing header default](components/crops/mkt-header-default.png)

#### Fable logo (marketing)
The Fable mark-and-wordmark svg in the marketing header — a dark-green rounded square of rainbow book spines with cream letterforms. Read as `mkt-logo` on the home page.

**Values (default).** size 82 x 33; background transparent; text Inter 16/24 400, #000000; transition border 0.2s ease, background 0.2s ease, color 0.2s ease; icon 82 x 33, #000000.

![Fable logo (marketing) default](components/crops/mkt-logo-default.png)

#### Nav link (marketing)
A marketing header nav link; measured, never followed. Read as `mkt-nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 39.75 x 14; background transparent; text Inter 14/14 600, #f7f4ee `color.pearl.extra.light`; transition border 0.2s ease, background 0.2s ease, color 0.2s ease |
| hover | text Inter 14/14 600, #ededed |
| focus-visible | radius 4px; outline 2px solid #116ecd, offset 4px; layers a.css-101r1r7 39.8x14.0 2px solid rgb(17, 110, 205) offset 4px 4px |

![Nav link (marketing) default](components/crops/mkt-nav-link-default.png) ![Nav link (marketing) hover](components/crops/mkt-nav-link-hover.png) ![Nav link (marketing) focus-visible](components/crops/mkt-nav-link-focus-visible.png) ![Nav link (marketing) pressed](components/crops/mkt-nav-link-pressed.png)

#### Sign-in icon (marketing)
The 24px "Sign up or log in" icon button; its states were measured but it was never clicked — the sign-in flow is a gap, not a state. Read as `mkt-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 24 x 24; background transparent; text Inter 16/24 400, #000000; transition opacity 0.2s ease; icon 24 x 24, #000000 |
| hover | opacity 0.7 |
| focus-visible | radius 4px; outline 2px solid #116ecd, offset 4px; layers button.css-1r8kfqf 24.0x24.0 2px solid rgb(17, 110, 205) offset 4px 4px |
| pressed | opacity 0.7 |

![Sign-in icon (marketing) default](components/crops/mkt-signin-default.png) ![Sign-in icon (marketing) hover](components/crops/mkt-signin-hover.png) ![Sign-in icon (marketing) focus-visible](components/crops/mkt-signin-focus-visible.png) ![Sign-in icon (marketing) pressed](components/crops/mkt-signin-pressed.png)

#### Cart icon
The 32px "Shopping cart" icon button; measured, never clicked. Read as `mkt-cart` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 32 x 32; background transparent; text Inter 16/24 400, #000000; transition border 0.2s ease, background 0.2s ease, color 0.2s ease; icon 24 x 24, #000000 |
| focus-visible | radius 4px; outline 2px solid #116ecd, offset 4px; layers button.css-1q2s6jc 32.0x32.0 2px solid rgb(17, 110, 205) offset 4px 4px |

![Cart icon default](components/crops/mkt-cart-default.png) ![Cart icon hover](components/crops/mkt-cart-hover.png) ![Cart icon focus-visible](components/crops/mkt-cart-focus-visible.png) ![Cart icon pressed](components/crops/mkt-cart-pressed.png)

#### Catalog header
The fixed 60px catalog top bar: the heldane "Fable" wordmark, nav links (Clubs / Books / Library / Blog) and the sign-in icon. Read as `cat-header` on the club detail page.

**Values (default).** size 1440 x 60; padding 0px 32px; background transparent; text Inter 14/16 600, #1b1a1b `color.graphite.600`; transition background-color 0.2s ease, box-shadow 0.2s ease; icon 32 x 32, #1b1a1b `color.graphite.600`.

![Catalog header default](components/crops/cat-header-default.png)

#### Fable wordmark (catalog)
The catalog header wordmark link — heldane bold type, "Fable home". Read as `cat-logo` on the club detail page.

**Values (default).** size 81.33 x 32; background transparent; text heldane 24/24 700, #1b1a1b `color.graphite.600`; icon 32 x 32, #1b1a1b `color.graphite.600`.

![Fable wordmark (catalog) default](components/crops/cat-logo-default.png)

#### Catalog nav link
A catalog header nav link (Clubs) — a 60px-tall cell; measured, never followed. Read as `cat-nav-link` on the club detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 39.75 x 60; background transparent; text Inter 14/16 600, #1b1a1b `color.graphite.600`; transition opacity 0.15s ease |
| hover | opacity 0.8 |
| focus-visible | radius 2px; outline 2px solid #0064c3 `color.royal.400`, offset 4px; layers a.HeaderNav-module-scss-module__GmZ0Qq__link 39.8x60.0 2px solid rgb(0, 100, 195) offset 4px 2px |
| pressed | opacity 0.8 |

![Catalog nav link default](components/crops/cat-nav-link-default.png) ![Catalog nav link hover](components/crops/cat-nav-link-hover.png) ![Catalog nav link focus-visible](components/crops/cat-nav-link-focus-visible.png) ![Catalog nav link pressed](components/crops/cat-nav-link-pressed.png)

#### Sign-in icon (catalog)
The 36x36 "Sign up or log in" avatar icon linking to /signin; measured, never followed. Read as `cat-signin` on the club detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; background transparent; text Inter 16/normal 400, #1b1a1b `color.graphite.600`; transition opacity 0.15s ease; icon 24 x 24, #1b1a1b `color.graphite.600` |
| hover | opacity 0.7 |
| focus-visible | radius 9999px; outline 2px solid #0064c3 `color.royal.400`, offset 2px; layers a.HeaderUserMenu-module-scss-module__kVbIfG__signInIcon 36.0x36.0 2px solid rgb(0, 100, 195) offset 2px 9999px |
| pressed | opacity 0.7 |

![Sign-in icon (catalog) default](components/crops/cat-signin-default.png) ![Sign-in icon (catalog) hover](components/crops/cat-signin-hover.png) ![Sign-in icon (catalog) focus-visible](components/crops/cat-signin-focus-visible.png) ![Sign-in icon (catalog) pressed](components/crops/cat-signin-pressed.png)

### Home

The light marketing page on fable.co: the Heldane Display hero 'The modern app for every reader', the paired Get-the-app buttons, feature section headings, the Fortune press quote and the popular-clubs card rail.

#### Hero headline
"The modern app for every reader" — the Heldane Display 72px cream masthead on the forest-green cover-wall hero. Read as `hero-h1` on the home page.

**Values (default).** size 500 x 124; background transparent; text Heldane Display 72/62 500, #f7f4ee `color.pearl.extra.light`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero book cover
One book-cover tile in the hero cover wall, linking into the dark /discover app; measured, never followed. Read as `hero-cover` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 151 x 225; background transparent; text Inter 16/24 400, #000000; transition border 0.2s ease, background 0.2s ease, color 0.2s ease |

![Hero book cover default](components/crops/hero-cover-default.png) ![Hero book cover hover](components/crops/hero-cover-hover.png)

#### Get the app (hero)
The white "Get the app" pill on the green hero (radius 60, white-on-green); measured, never clicked. Read as `getapp-hero` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 160 x 52; border 2px solid #ffffff `color.white.default`; radius 60px; background #ffffff `color.white.default`; text Inter 14/21 600, #161015 `color.quote.theme.6`; transition border 0.2s ease, background 0.2s ease, color 0.2s ease |
| hover | border 2px solid #f9f9f9; background #f9f9f9; text Inter 14/21 600, #332e32 `component.skin.marketing.marketingPillHoverInk` |
| focus-visible | outline 2px solid #116ecd, offset 4px |
| pressed | border 2px solid #f9f9f9; background #f9f9f9; text Inter 14/21 600, #332e32 `component.skin.marketing.marketingPillHoverInk` |

![Get the app (hero) default](components/crops/getapp-hero-default.png) ![Get the app (hero) hover](components/crops/getapp-hero-hover.png) ![Get the app (hero) focus-visible](components/crops/getapp-hero-focus-visible.png) ![Get the app (hero) pressed](components/crops/getapp-hero-pressed.png)

#### Get the app (on light)
The dark-ink "Get the app" pill used on the light feature sections; measured, never clicked. Read as `getapp-dark` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 160 x 52; border 2px solid #292229 `color.graphite.default`; radius 60px; background #292229 `color.graphite.default`; text Inter 14/21 600, #ffffff `color.white.default`; transition border 0.2s ease, background 0.2s ease, color 0.2s ease |
| hover | border 2px solid #433944 `component.skin.marketing.marketingPillHoverFill`; background #433944 `component.skin.marketing.marketingPillHoverFill` |
| focus-visible | outline 2px solid #116ecd, offset 4px |
| pressed | border 2px solid #433944 `component.skin.marketing.marketingPillHoverFill`; background #433944 `component.skin.marketing.marketingPillHoverFill` |

![Get the app (on light) default](components/crops/getapp-dark-default.png) ![Get the app (on light) hover](components/crops/getapp-dark-hover.png) ![Get the app (on light) focus-visible](components/crops/getapp-dark-focus-visible.png) ![Get the app (on light) pressed](components/crops/getapp-dark-pressed.png)

#### Section headline
A Heldane Display 80px marketing section heading ("Track your books in one place"). Read as `section-h2` on the home page.

**Values (default).** size 580 x 150; background transparent; text Heldane Display 80/75 500, #292229 `color.graphite.default`.

![Section headline default](components/crops/section-h2-default.png)

#### Feature card heading
A 24px Inter semibold feature-card heading inside a marketing section. Read as `feature-h` on the home page.

**Values (default).** size 200 x 80; padding 8px 0px 16px 0px; background transparent; text Inter 24/28 600, #161015 `color.quote.theme.6`.

![Feature card heading default](components/crops/feature-h-default.png)

#### Press quote
The Fortune pull-quote — "A more thoughtful—and less toxic—social media app". Read as `fortune-quote` on the home page.

**Values (default).** size 560 x 293; background transparent; text Heldane Display 48/42 500, #f7f4ee `color.pearl.extra.light`; layers button.css-3u91k5 160.0x44.0 rgb(255, 255, 255) T:2px rgb(255, 255, 255) / R:2px rgb(255, 255, 255) / B:2px rgb(255, 255, 255) / L:2px rgb(255, 255, 255) 60px.

Child layers that carry the look: button 160x44 background #ffffff `color.white.default` border 2px #ffffff `color.white.default` radius 60px.

![Press quote default](components/crops/fortune-quote-default.png)

#### Club card
A "Popular clubs" card — hero image, club cover thumb, moderator line, member count. Read as `club-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 248 x 380; background transparent; text Inter 12/16 700, #3f383d; transition transform 0.4s ease-in-out; icon 14 x 14, #000000; layers div.css-1xixpw4 79.0x117.0 T:2px rgb(255, 255, 255) / R:2px rgb(255, 255, 255) / B:2px rgb(255, 255, 255) / L:2px rgb(255, 255, 255) 8px |
| hover | size 250.48 x 383.8; transform scale(1.01); icon 14.14 x 14.14, #000000; layers div.css-1xixpw4 79.8x118.2 T:2px rgb(255, 255, 255) / R:2px rgb(255, 255, 255) / B:2px rgb(255, 255, 255) / L:2px rgb(255, 255, 255) 8px |

Child layers that carry the look: div 79x117 border 2px #ffffff `color.white.default` radius 8px.

![Club card default](components/crops/club-card-default.png) ![Club card hover](components/crops/club-card-hover.png)

#### Get the app (closing CTA)
The "Get the app" pill in the closing call-to-action band; measured, never clicked. Read as `getapp-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 160 x 44; border 2px solid #ffffff `color.white.default`; radius 60px; background #ffffff `color.white.default`; text Inter 14/21 600, #161015 `color.quote.theme.6`; transition border 0.2s ease, background 0.2s ease, color 0.2s ease |
| hover | border 2px solid #f9f9f9; background #f9f9f9; text Inter 14/21 600, #332e32 `component.skin.marketing.marketingPillHoverInk` |
| focus-visible | outline 2px solid #116ecd, offset 4px |
| pressed | border 2px solid #f9f9f9; background #f9f9f9; text Inter 14/21 600, #332e32 `component.skin.marketing.marketingPillHoverInk` |

![Get the app (closing CTA) default](components/crops/getapp-cta-default.png) ![Get the app (closing CTA) hover](components/crops/getapp-cta-hover.png) ![Get the app (closing CTA) focus-visible](components/crops/getapp-cta-focus-visible.png) ![Get the app (closing CTA) pressed](components/crops/getapp-cta-pressed.png)

### Clubs index

The /clubs catalog page (CSS-module skin): headline, the sticky genre-pill rail with its scroll arrow, shelf headings, club cards and the carousel/search icon buttons.

#### Clubs headline
The /clubs masthead heading. Read as `clubs-h1` on the clubs index page.

**Values (default).** size 254 x 120; background transparent; text heldane 58/60 700, #1b1a1b `color.graphite.600`.

![Clubs headline default](components/crops/clubs-h1-default.png)

#### Club search trigger
The 440x52 search field-styled button opening the "Find a club" modal — an aria-haspopup="dialog" local toggle; the opened state was measured after clicking it. Read as `search-trigger` on the clubs index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 440 x 52; padding 0px 8px 0px 24px; radius 9999px; background #ffffff `color.white.default`; text Inter 14/20 400, #4b4649 `color.graphite.500`; icon 20 x 20, #000000 |
| focus-visible | outline 2px solid #0064c3 `color.royal.400`, offset 2px |

![Club search trigger default](components/crops/search-trigger-default.png) ![Club search trigger hover](components/crops/search-trigger-hover.png) ![Club search trigger focus-visible](components/crops/search-trigger-focus-visible.png) ![Club search trigger pressed](components/crops/search-trigger-pressed.png) ![Club search trigger opened](components/crops/search-trigger-opened.png)

#### Genre pill
A 46px genre pill link (Fantasy) in the scrollable genre strip; measured, never followed. Read as `genre-pill` on the clubs index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 102 x 46; padding 10px 20px; border 1px solid #b1acaf `color.graphite.300`; radius 9999px; background #ffffff `color.white.default`; text Inter 16/24 400, #1b1a1b `color.graphite.600` |
| hover | background #f8f8f8 `color.graphite.100` |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #f8f8f8 `color.graphite.100` |

![Genre pill default](components/crops/genre-pill-default.png) ![Genre pill hover](components/crops/genre-pill-hover.png) ![Genre pill focus-visible](components/crops/genre-pill-focus-visible.png) ![Genre pill pressed](components/crops/genre-pill-pressed.png)

#### Genre scroll arrow
The dark 40px arrow that scrolls the genre strip forward; measured, never clicked. Read as `genre-scroll` on the clubs index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 40 x 40; padding 1px 6px; radius 9999px; background #1b1a1b `color.graphite.600`; text Arial 13.33/normal 400, #000000; icon 20 x 20, #000000 |
| focus-visible | outline 1px auto #101010, offset 0px |

![Genre scroll arrow default](components/crops/genre-scroll-default.png) ![Genre scroll arrow hover](components/crops/genre-scroll-hover.png) ![Genre scroll arrow focus-visible](components/crops/genre-scroll-focus-visible.png) ![Genre scroll arrow pressed](components/crops/genre-scroll-pressed.png)

#### Search icon button
The cream 44px circular search affordance at the head of the genre strip; measured, never clicked. Read as `search-icon-btn` on the clubs index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44 x 44; padding 1px 6px; radius 9999px; background #f7f4eb `color.pearl.100`; text Arial 13.33/normal 400, #1b1a1b `color.graphite.600`; icon 20 x 20, #1b1a1b `color.graphite.600` |
| hover | background #ebe7d9 `color.pearl.200` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | background #ebe7d9 `color.pearl.200` |

![Search icon button default](components/crops/search-icon-btn-default.png) ![Search icon button hover](components/crops/search-icon-btn-hover.png) ![Search icon button focus-visible](components/crops/search-icon-btn-focus-visible.png) ![Search icon button pressed](components/crops/search-icon-btn-pressed.png)

#### Carousel arrow
A 40px round bordered IconButton (Previous <shelf>) stepping a club/book carousel; measured, never clicked. Read as `icon-btn` on the clubs index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 40 x 40; padding 1px 6px; border 1px solid rgba(7, 6, 7, 0.1) `color.dark.fade.10`; radius 9999px; background transparent; text Arial 13.33/normal 400, #1b1a1b `color.graphite.600`; transition background-color 0.15s ease, color 0.15s ease, opacity 0.15s ease, border-color 0.15s ease; opacity 0.5; icon 24 x 24, #1b1a1b `color.graphite.600` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Carousel arrow default](components/crops/icon-btn-default.png) ![Carousel arrow hover](components/crops/icon-btn-hover.png) ![Carousel arrow pressed](components/crops/icon-btn-pressed.png)

#### Club card (catalog)
A club card in a clubs-index shelf — image, moderator line, club name, member count; measured, never followed. Read as `club-card-cat` on the clubs index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 256 x 372; radius 24px; background transparent; text Inter 10/16 600, #1b1a1b `color.graphite.600`; icon 16 x 16, #1b1a1b `color.graphite.600`; layers div.StackedBookCover-module-scss-module__ZNm-FG__root.StackedBookCover-module-scss-module__ZNm-FG__constrainWidth 256.0x238.0 rgb(235, 231, 217) T:3px rgb(247, 244, 235) / R:3px rgb(247, 244, 235) / B:3px rgb(247, 244, 235) / L:3px rgb(247, 244, 235) 24px; div.StackedBookCover-module-scss-module__ZNm-FG__backCard.StackedBookCover-module-scss-module__ZNm-FG__backCard1 111.3x150.7 rgb(255, 255, 255) |

Child layers that carry the look: div 256x238 background #ebe7d9 `color.pearl.200` border 3px #f7f4eb `color.pearl.100` radius 24px; div 111.3x150.7 background #ffffff `color.white.default` image linear-gradient(#eeebdf, #eeebdf), none radius 8px shadow rgba(0, 0, 0, 0.28) 0px 8px 18px 0px; div 127.6x159.4 background #ffffff `color.white.default` image linear-gradient(#eeebdf, #eeebdf), none radius 8px shadow rgba(0, 0, 0, 0.28) 0px 8px 18px 0px.

![Club card (catalog) default](components/crops/club-card-cat-default.png) ![Club card (catalog) hover](components/crops/club-card-cat-hover.png)

#### Shelf heading
A clubs-index shelf heading (heldane) above a horizontal card rail. Read as `clubs-section-h` on the clubs index page.

**Values (default).** size 253.5 x 36; background transparent; text heldane 36/36 400, #1b1a1b `color.graphite.600`.

![Shelf heading default](components/crops/clubs-section-h-default.png)

### Club search modal

The 'Find a club' dialog opened from /clubs: overlay panel, search input and close button. A local, UI-only interaction.

#### Find a club modal
The centered Modal-module sheet opened by the search trigger: drag handle, "Find a club" title, close button, search input and an empty results prompt. Read as `search-modal` on the clubs index page.

**Values (default).** size 480 x 497; border 1px solid rgba(7, 6, 7, 0.1) `color.dark.fade.10`; radius 24px; background #ffffff `color.white.default`; shadow rgba(0, 0, 0, 0.12) 0px -6px 16px 0px; text Inter 18/23.4 600, #1b1a1b `color.graphite.600`; transform translate(-240px, -248.5px); icon 18 x 18, #1b1a1b `color.graphite.600`.

![Find a club modal default](components/crops/search-modal-default.png)

#### Search input
The search field inside the Find a club modal; focused, never submitted. Read as `search-input` on the clubs index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 430 x 41; padding 10px 12px 10px 36px; border 1px solid rgba(7, 6, 7, 0.1) `color.dark.fade.10`; radius 12px; background transparent; text Inter 15/normal 400, #1b1a1b `color.graphite.600`; placeholder #4b4649 `color.graphite.500` |
| focused | border 1px solid #1b1a1b `color.graphite.600` |

![Search input default](components/crops/search-input-default.png) ![Search input focused](components/crops/search-input-focused.png)

#### Modal close button
The icon-only close button in the modal header. Read as `search-close` on the clubs index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; padding 1px 6px; radius 9999px; background transparent; text Arial 13.33/normal 400, #1b1a1b `color.graphite.600`; icon 18 x 18, #1b1a1b `color.graphite.600` |
| hover | background #f7f4eb `color.pearl.100` |
| focus-visible, pressed | background #f7f4eb `color.pearl.100`; outline 2px solid #0064c3 `color.royal.400`, offset 2px |

![Modal close button default](components/crops/search-close-default.png) ![Modal close button hover](components/crops/search-close-hover.png) ![Modal close button focus-visible](components/crops/search-close-focus-visible.png) ![Modal close button pressed](components/crops/search-close-pressed.png)

### App-install prompt

The app-download banner on the book page and the App Store / Google Play badges it carries — measured, never followed.

#### App download banner
The app-install strip under the header with App Store and Play badges; the badge links are measured, never followed. Read as `app-banner` on the book detail page.

**Values (default).** size 1440 x 132; background #053829 `color.forest.300`; text heldane 32/28 400, #ffffff `color.white.default`.

![App download banner default](components/crops/app-banner-default.png)

#### Store badge
The App Store badge inside the download banner; measured, never followed. Read as `store-badge` on the book detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 68 x 23; background transparent; text Inter 16/normal 400, #0000ee |

![Store badge default](components/crops/store-badge-default.png) ![Store badge hover](components/crops/store-badge-hover.png)

### Book detail

The /book/* page: title, author link, ratings line, the primary/secondary action buttons, the spoiler disclosure and 'Read more' toggles (both toggled locally), the author profile button, book and club cards and the carousel arrow.

#### Book title
The book detail masthead title. Read as `book-h1` on the book detail page.

**Values (default).** size 706 x 48; background transparent; text heldane 46/48 700, #1b1a1b `color.graphite.600`.

![Book title default](components/crops/book-h1-default.png)

#### Author link
The author byline link in the book hero; measured, never followed. Read as `author-link` on the book detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 67.25 x 15; background transparent; text Inter 12/12 600, #1b1a1b `color.graphite.600` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.BookDetailHero-module-scss-module__mIHGba__authorLink 67.3x15.0 1px auto rgb(16, 16, 16) offset 1px |

![Author link default](components/crops/author-link-default.png) ![Author link hover](components/crops/author-link-hover.png) ![Author link focus-visible](components/crops/author-link-focus-visible.png) ![Author link pressed](components/crops/author-link-pressed.png)

#### Ratings line
The "66,098 Ratings" anchor linking to the reviews block; measured, never followed. Read as `ratings-line` on the book detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 87.5 x 20; background transparent; text Inter 12/12 600, #1b1a1b `color.graphite.600` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.BookDetailReviewLine-module-scss-module__ne1zFW__ratings 87.5x20.0 1px auto rgb(16, 16, 16) offset 1px |

![Ratings line default](components/crops/ratings-line-default.png) ![Ratings line hover](components/crops/ratings-line-hover.png) ![Ratings line focus-visible](components/crops/ratings-line-focus-visible.png) ![Ratings line pressed](components/crops/ratings-line-pressed.png)

#### Primary button
The dark 52px "Want to read" pill (Button-module primary, radius 9999); its states were measured but it was never clicked — saving to a shelf is signed-in functionality. Read as `btn-primary` on the book detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 361 x 52; padding 10px 20px; border 1px solid #1b1a1b `color.graphite.600`; radius 9999px; background #1b1a1b `color.graphite.600`; text Inter 14/normal 600, #ffffff `color.white.default`; transition background-color 0.15s ease, color 0.15s ease, opacity 0.15s ease, border-color 0.15s ease; icon 24 x 24, #ffffff `color.white.default` |
| hover | opacity 0.85 |
| focus-visible | outline 2px solid #0064c3 `color.royal.400`, offset 2px |
| pressed | opacity 0.85 |

![Primary button default](components/crops/btn-primary-default.png) ![Primary button hover](components/crops/btn-primary-hover.png) ![Primary button focus-visible](components/crops/btn-primary-focus-visible.png) ![Primary button pressed](components/crops/btn-primary-pressed.png)

#### Secondary button
The outlined "Read or listen free today" pill below the primary; measured, never clicked. Read as `btn-secondary` on the book detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 361 x 52; padding 10px 20px; border 1px solid #1b1a1b `color.graphite.600`; radius 9999px; background transparent; text Inter 14/normal 600, #1b1a1b `color.graphite.600`; transition background-color 0.15s ease, color 0.15s ease, opacity 0.15s ease, border-color 0.15s ease |
| hover | background #f7f4eb `color.pearl.100` |
| focus-visible | outline 2px solid #0064c3 `color.royal.400`, offset 2px |
| pressed | background #f7f4eb `color.pearl.100` |

![Secondary button default](components/crops/btn-secondary-default.png) ![Secondary button hover](components/crops/btn-secondary-hover.png) ![Secondary button focus-visible](components/crops/btn-secondary-focus-visible.png) ![Secondary button pressed](components/crops/btn-secondary-pressed.png)

#### Spoiler disclosure
The olive "May contain spoilers!" pill toggling the pre-published review text — a local disclosure; pressing it reveals the text, so it was measured at rest. Read as `spoiler-pill` on the book detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 136 x 28; padding 4px 12px; border 1px solid #526c03 `color.olive.500`; radius 9999px; background #526c03 `color.olive.500`; text Inter 10/normal 600, #ffffff `color.white.default`; transition background-color 0.15s ease, color 0.15s ease, opacity 0.15s ease, border-color 0.15s ease |
| focus-visible | outline 2px solid #0064c3 `color.royal.400`, offset 2px |
| pressed | opacity 0.85 |

![Spoiler disclosure default](components/crops/spoiler-pill-default.png) ![Spoiler disclosure hover](components/crops/spoiler-pill-hover.png) ![Spoiler disclosure focus-visible](components/crops/spoiler-pill-focus-visible.png) ![Spoiler disclosure pressed](components/crops/spoiler-pill-pressed.png)

#### Read more toggle
The inline "Read more" disclosure expanding the book description — a local toggle; the opened state was measured after clicking it. Read as `read-more` on the book detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 73.75 x 16; background transparent; text Inter 14/16 600, #4b4649 `color.graphite.500` |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.ExpandableText-module-scss-module__10317G__toggle 73.8x16.0 1px auto rgb(16, 16, 16) offset 0px |
| opened | size 66.75 x 16 |

![Read more toggle default](components/crops/read-more-default.png) ![Read more toggle hover](components/crops/read-more-hover.png) ![Read more toggle focus-visible](components/crops/read-more-focus-visible.png) ![Read more toggle pressed](components/crops/read-more-pressed.png) ![Read more toggle opened](components/crops/read-more-opened.png)

#### Author profile button
The outlined "View author profile" pill link; measured, never followed. Read as `author-profile-btn` on the book detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 171 x 40; padding 8px 16px; border 1px solid #1b1a1b `color.graphite.600`; radius 9999px; background transparent; text Inter 14/normal 600, #1b1a1b `color.graphite.600`; transition background-color 0.15s ease, color 0.15s ease, opacity 0.15s ease, border-color 0.15s ease |
| hover | background #f7f4eb `color.pearl.100` |
| focus-visible | outline 2px solid #0064c3 `color.royal.400`, offset 2px |
| pressed | background #f7f4eb `color.pearl.100` |

![Author profile button default](components/crops/author-profile-btn-default.png) ![Author profile button hover](components/crops/author-profile-btn-hover.png) ![Author profile button focus-visible](components/crops/author-profile-btn-focus-visible.png) ![Author profile button pressed](components/crops/author-profile-btn-pressed.png)

#### Book card
A book carousel item — cover image, title, author — linking to another book page; measured, never followed. Read as `book-card` on the book detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 167 x 290.5; background transparent; text Inter 12/16 500, #1b1a1b `color.graphite.600`; layers div.BookCover-module-scss-module__Q6C61G__cover.BookCarouselItem-module-scss-module__q4Pr7G__cover 167.0x250.5 rgb(235, 231, 217) 8px |

Child layers that carry the look: div 167x250.5 background #ebe7d9 `color.pearl.200` radius 8px.

![Book card default](components/crops/book-card-default.png) ![Book card hover](components/crops/book-card-hover.png)

#### Club card (book page)
A club card in the "clubs reading this" rail; measured, never followed. Read as `club-card-book` on the book detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 256 x 372; radius 24px; background transparent; text Inter 10/16 600, #1b1a1b `color.graphite.600`; icon 16 x 16, #1b1a1b `color.graphite.600`; layers div.StackedBookCover-module-scss-module__ZNm-FG__root.StackedBookCover-module-scss-module__ZNm-FG__constrainWidth 256.0x238.0 rgb(235, 231, 217) T:3px rgb(247, 244, 235) / R:3px rgb(247, 244, 235) / B:3px rgb(247, 244, 235) / L:3px rgb(247, 244, 235) 24px; div.StackedBookCover-module-scss-module__ZNm-FG__backCard.StackedBookCover-module-scss-module__ZNm-FG__backCard1 111.3x150.7 rgb(255, 255, 255) |

Child layers that carry the look: div 256x238 background #ebe7d9 `color.pearl.200` border 3px #f7f4eb `color.pearl.100` radius 24px; div 111.3x150.7 background #ffffff `color.white.default` image linear-gradient(#eeebdf, #eeebdf), none radius 8px shadow rgba(0, 0, 0, 0.28) 0px 8px 18px 0px; div 127.6x159.4 background #ffffff `color.white.default` image linear-gradient(#eeebdf, #eeebdf), none radius 8px shadow rgba(0, 0, 0, 0.28) 0px 8px 18px 0px.

![Club card (book page) default](components/crops/club-card-book-default.png) ![Club card (book page) hover](components/crops/club-card-book-hover.png)

#### Carousel arrow (book)
A 40px round bordered IconButton stepping the "Other books by" carousel; measured, never clicked. Read as `icon-btn-book` on the book detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 40 x 40; padding 1px 6px; border 1px solid rgba(7, 6, 7, 0.1) `color.dark.fade.10`; radius 9999px; background transparent; text Arial 13.33/normal 400, #1b1a1b `color.graphite.600`; transition background-color 0.15s ease, color 0.15s ease, opacity 0.15s ease, border-color 0.15s ease; opacity 0.5; icon 24 x 24, #1b1a1b `color.graphite.600` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Carousel arrow (book) default](components/crops/icon-btn-book-default.png) ![Carousel arrow (book) hover](components/crops/icon-btn-book-hover.png) ![Carousel arrow (book) pressed](components/crops/icon-btn-book-pressed.png)

### Club detail

The /club/* pages: club name and moderator line, the Join CTA (measured, never pressed), share button, section headings, the FAQ accordion (opened locally) and the club pick card.

#### Club name
The club masthead — heldane 46px bold "The Cozy Chaos Book Club". Read as `club-h1` on the club detail page.

**Values (default).** size 706 x 48; background transparent; text heldane 46/48 700, #1b1a1b `color.graphite.600`.

![Club name default](components/crops/club-h1-default.png)

#### Moderator line
The 14px Inter semibold moderator byline under the club name. Read as `club-sub` on the club detail page.

**Values (default).** size 186.2 x 16; background transparent; text Inter 14/16 600, #1b1a1b `color.graphite.600`.

![Moderator line default](components/crops/club-sub-default.png)

#### Join CTA
The dark "Download the app to join" pill — joining is app-only; measured, never followed. Read as `join-cta` on the club detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 224 x 52; padding 10px 20px; border 1px solid #1b1a1b `color.graphite.600`; radius 9999px; background #1b1a1b `color.graphite.600`; text Inter 14/normal 600, #ffffff `color.white.default`; transition background-color 0.15s ease, color 0.15s ease, opacity 0.15s ease, border-color 0.15s ease |
| hover | opacity 0.85 |
| focus-visible | outline 2px solid #0064c3 `color.royal.400`, offset 2px |
| pressed | opacity 0.85 |

![Join CTA default](components/crops/join-cta-default.png) ![Join CTA hover](components/crops/join-cta-hover.png) ![Join CTA focus-visible](components/crops/join-cta-focus-visible.png) ![Join CTA pressed](components/crops/join-cta-pressed.png)

#### Share button
The round share icon button ("Share The Cozy Chaos Book Club"); measured, never clicked. Read as `share-btn` on the club detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 52 x 52; padding 1px 6px; border 1px solid rgba(7, 6, 7, 0.1) `color.dark.fade.10`; radius 9999px; background transparent; text Arial 13.33/normal 400, #1b1a1b `color.graphite.600`; transition background-color 0.15s ease, border-color 0.15s ease; icon 24 x 24, #1b1a1b `color.graphite.600` |
| hover | border 1px solid #1b1a1b `color.graphite.600`; background #f7f4eb `color.pearl.100` |
| focus-visible | outline 2px solid #0064c3 `color.royal.400`, offset 2px |
| pressed | border 1px solid #1b1a1b `color.graphite.600`; background #f7f4eb `color.pearl.100` |

![Share button default](components/crops/share-btn-default.png) ![Share button hover](components/crops/share-btn-hover.png) ![Share button focus-visible](components/crops/share-btn-focus-visible.png) ![Share button pressed](components/crops/share-btn-pressed.png)

#### Club section heading
A heldane 36px club-page section heading ("About this club"). Read as `club-h2` on the club detail page.

**Values (default).** size 678 x 36; background transparent; text heldane 36/36 400, #1b1a1b `color.graphite.600`.

![Club section heading default](components/crops/club-h2-default.png)

#### FAQ question
A FAQ accordion question ("Are Fable book clubs free to join?") — a local toggle; the opened state was measured after clicking it. Read as `faq-q` on the club detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 678 x 72; padding 24px 0px; background transparent; text Inter 16/20 600, #1b1a1b `color.graphite.600`; icon 24 x 24, #1b1a1b `color.graphite.600` |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.FaqAccordion-module-scss-module__ffolAG__faqQuestion 678.0x72.0 1px auto rgb(16, 16, 16) offset 0px |

![FAQ question default](components/crops/faq-q-default.png) ![FAQ question hover](components/crops/faq-q-hover.png) ![FAQ question focus-visible](components/crops/faq-q-focus-visible.png) ![FAQ question pressed](components/crops/faq-q-pressed.png) ![FAQ question opened](components/crops/faq-q-opened.png)

#### Club pick card
A "Club picks" book card (CURRENTLY READING badge, cover, title); measured, never followed. Read as `book-card-club` on the club detail page.

**Values (default).** size 190 x 325; background transparent; text Inter 12/16 500, #1b1a1b `color.graphite.600`; layers div.BookCover-module-scss-module__Q6C61G__cover.BookCarouselItem-module-scss-module__q4Pr7G__cover 190.0x285.0 rgb(235, 231, 217) 8px.

Child layers that carry the look: div 190x285 background #ebe7d9 `color.pearl.200` radius 8px.

![Club pick card default](components/crops/book-card-club-default.png)

### Sign-in

The /signin panel: headline, e-mail and password fields (focused and filled with sample values then cleared — never submitted), show-password toggle, 'Login with email' submit, the Google and Apple SSO buttons (measured, never pressed) and the reset/sign-up links.

#### Sign-in headline
"Please log in" — the Heldane Display 26px heading over the sign-in card. Read as `signin-h1` on the sign-in page.

**Values (default).** size 125 x 28; background transparent; text Heldane Display 26/28 400, #161015 `color.quote.theme.6`.

![Sign-in headline default](components/crops/signin-h1-default.png)

#### Sign-in form
The sign-in form: email and password fields, show-password, the email submit and SSO buttons. Shot and measured at rest — never submitted. Read as `signin-panel` on the sign-in page.

**Values (default).** size 396 x 172; background transparent; text Inter 14/14 400, #847f7c; layers div.text-input.css-1ltccw 396.0x52.0 rgb(255, 255, 255) T:1px rgb(188, 188, 188) / R:1px rgb(188, 188, 188) / B:1px rgb(188, 188, 188) / L:1px rgb(188, 188, 188) 44px; div.text-input.css-yvrp3z 396.0x52.0 rgb(255, 255, 255) T:1px rgb(188, 188, 188) / R:1px rgb(188, 188, 188) / B:1px rgb(188, 188, 188) / L:1px rgb(188, 188, 188) 44px; button.css-f2o8q 48.0x40.0 rgb(255, 255, 255) 12px; button.css-1.

Child layers that carry the look: div 396x52 background #ffffff `color.white.default` border 1px #bcbcbc `component.skin.marketing.textInputBorder` radius 44px; div 396x52 background #ffffff `color.white.default` border 1px #bcbcbc `component.skin.marketing.textInputBorder` radius 44px; button 48x40 background #ffffff `color.white.default` radius 12px.

![Sign-in form default](components/crops/signin-panel-default.png)

#### Email field
The Email Address text input; focused and typed into then cleared — never submitted. Read as `field-email` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 394 x 50; padding 0px 14px; background transparent; text Inter 14/14 400, #161015 `color.quote.theme.6`; transition border 0.2s ease, background 0.2s ease, color 0.2s ease; placeholder #847f7c |
| focused, filled | outline 2px solid #116ecd, offset 2px; layers input.css-1r5n8r2 394.0x50.0 2px solid rgb(17, 110, 205) offset 2px |

![Email field default](components/crops/field-email-default.png) ![Email field focused](components/crops/field-email-focused.png) ![Email field filled](components/crops/field-email-filled.png)

#### Password field
The Password input with the inline Show button; focused and typed into then cleared — never submitted. Read as `field-password` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 394 x 50; padding 0px 14px; background transparent; text Inter 14/14 400, #161015 `color.quote.theme.6`; transition border 0.2s ease, background 0.2s ease, color 0.2s ease; placeholder #847f7c |
| focused, filled | outline 2px solid #116ecd, offset 2px; layers input.css-1r5n8r2 394.0x50.0 2px solid rgb(17, 110, 205) offset 2px |

![Password field default](components/crops/field-password-default.png) ![Password field focused](components/crops/field-password-focused.png) ![Password field filled](components/crops/field-password-filled.png)

#### Show password
The inline "Show" reveal button in the password field; measured, never clicked. Read as `show-btn` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 48 x 40; radius 12px; background #ffffff `color.white.default`; text Inter 14/14 400, #847f7c; transition border 0.2s ease, background 0.2s ease, color 0.2s ease; transform translate(0px, -20px) |
| focus-visible | outline 2px solid #116ecd, offset 4px |

![Show password default](components/crops/show-btn-default.png) ![Show password hover](components/crops/show-btn-hover.png) ![Show password focus-visible](components/crops/show-btn-focus-visible.png) ![Show password pressed](components/crops/show-btn-pressed.png)

#### Login with email
The dark "Login with email" submit; its states were measured but the button was never clicked — nothing was submitted. Read as `submit-btn` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 396 x 44; border 2px solid #292229 `color.graphite.default`; radius 60px; background #292229 `color.graphite.default`; text Inter 14/21 600, #ffffff `color.white.default`; transition border 0.2s ease, background 0.2s ease, color 0.2s ease |
| hover | border 2px solid #433944 `component.skin.marketing.marketingPillHoverFill`; background #433944 `component.skin.marketing.marketingPillHoverFill` |
| focus-visible | outline 2px solid #116ecd, offset 4px |
| pressed | border 2px solid #433944 `component.skin.marketing.marketingPillHoverFill`; background #433944 `component.skin.marketing.marketingPillHoverFill` |

![Login with email default](components/crops/submit-btn-default.png) ![Login with email hover](components/crops/submit-btn-hover.png) ![Login with email focus-visible](components/crops/submit-btn-focus-visible.png) ![Login with email pressed](components/crops/submit-btn-pressed.png)

#### Continue with Google
The white Google SSO button; measured, never clicked. Read as `sso-google` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 396 x 44; border 2px solid #161015 `color.quote.theme.6`; radius 60px; background #ffffff `color.white.default`; text Inter 14/21 600, #161015 `color.quote.theme.6`; transition border 0.2s ease, background 0.2s ease, color 0.2s ease; icon 20 x 20, #161015 `color.quote.theme.6` |
| hover | border 2px solid #2e272d; text Inter 14/21 600, #332e32 `component.skin.marketing.marketingPillHoverInk`; icon 20 x 20, #332e32 `component.skin.marketing.marketingPillHoverInk` |
| focus-visible | outline 2px solid #116ecd, offset 4px |
| pressed | border 2px solid #2e272d; text Inter 14/21 600, #332e32 `component.skin.marketing.marketingPillHoverInk`; icon 20 x 20, #332e32 `component.skin.marketing.marketingPillHoverInk` |

![Continue with Google default](components/crops/sso-google-default.png) ![Continue with Google hover](components/crops/sso-google-hover.png) ![Continue with Google focus-visible](components/crops/sso-google-focus-visible.png) ![Continue with Google pressed](components/crops/sso-google-pressed.png)

#### Continue with Apple
The white Apple SSO button; measured, never clicked. Read as `sso-apple` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 396 x 44; border 2px solid #161015 `color.quote.theme.6`; radius 60px; background #ffffff `color.white.default`; text Inter 14/21 600, #161015 `color.quote.theme.6`; transition border 0.2s ease, background 0.2s ease, color 0.2s ease; icon 20 x 24, #161015 `color.quote.theme.6` |
| hover | border 2px solid #2e272d; text Inter 14/21 600, #332e32 `component.skin.marketing.marketingPillHoverInk`; icon 20 x 24, #332e32 `component.skin.marketing.marketingPillHoverInk` |
| focus-visible | outline 2px solid #116ecd, offset 4px |
| pressed | border 2px solid #2e272d; text Inter 14/21 600, #332e32 `component.skin.marketing.marketingPillHoverInk`; icon 20 x 24, #332e32 `component.skin.marketing.marketingPillHoverInk` |

![Continue with Apple default](components/crops/sso-apple-default.png) ![Continue with Apple hover](components/crops/sso-apple-hover.png) ![Continue with Apple focus-visible](components/crops/sso-apple-focus-visible.png) ![Continue with Apple pressed](components/crops/sso-apple-pressed.png)

#### Reset link
The "Reset it" password-reset link styled as a bold inline button; measured, never clicked. Read as `reset-link` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 54 x 23; background transparent; text Inter 14/23 900, #161015 `color.quote.theme.6`; transition border 0.2s ease, background 0.2s ease, color 0.2s ease |
| hover | text Inter 14/23 900, #332e32 `component.skin.marketing.marketingPillHoverInk` |
| focus-visible | radius 4px; outline 2px solid #116ecd, offset 4px; layers button.css-p31fum 54.0x23.0 2px solid rgb(17, 110, 205) offset 4px 4px |
| pressed | text Inter 14/23 900, #332e32 `component.skin.marketing.marketingPillHoverInk` |

![Reset link default](components/crops/reset-link-default.png) ![Reset link hover](components/crops/reset-link-hover.png) ![Reset link focus-visible](components/crops/reset-link-focus-visible.png) ![Reset link pressed](components/crops/reset-link-pressed.png)

#### Sign up link
The "Sign up" link button under the SSO buttons; measured, never clicked. Read as `signup-link` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 52.25 x 23; background transparent; text Inter 14/23 600, #161015 `color.quote.theme.6`; transition border 0.2s ease, background 0.2s ease, color 0.2s ease |
| hover | text Inter 14/23 600, #332e32 `component.skin.marketing.marketingPillHoverInk` |
| focus-visible | radius 4px; outline 2px solid #116ecd, offset 4px; layers button.css-p31fum 52.3x23.0 2px solid rgb(17, 110, 205) offset 4px 4px |
| pressed | text Inter 14/23 600, #332e32 `component.skin.marketing.marketingPillHoverInk` |

![Sign up link default](components/crops/signup-link-default.png) ![Sign up link hover](components/crops/signup-link-hover.png) ![Sign up link focus-visible](components/crops/signup-link-focus-visible.png) ![Sign up link pressed](components/crops/signup-link-pressed.png)

### Support

The /support page: the forest-green masthead band, headline, help-topic cards and the e-mail card.

#### Support headline
The /support masthead heading on the forest-green band. Read as `support-h1` on the support page.

**Values (default).** size 358.13 x 60; background transparent; text Heldane Display 58/60 400, #e4adbb `color.quote.theme.5`.

![Support headline default](components/crops/support-h1-default.png)

#### Support masthead band
The forest-green support masthead band (rgb(6, 76, 55)) carrying the heading and intro. Read as `support-masthead` on the support page.

**Values (default).** size 358.13 x 60; background transparent; text Heldane Display 58/60 400, #e4adbb `color.quote.theme.5`.

![Support masthead band default](components/crops/support-masthead-default.png)

#### Help card
The "FAQs" help-card linking to help.fable.co; measured, never followed. Read as `help-card` on the support page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 610 x 120; padding 18px; background transparent; text Inter 18/24 600, #161015 `color.quote.theme.6`; transition border 0.2s ease, background 0.2s ease, color 0.2s ease; layers div.support-icon 71.4x84.0 rgb(249, 249, 249) 8px |

Child layers that carry the look: div 71.4x84 background #f9f9f9 radius 8px.

![Help card default](components/crops/help-card-default.png) ![Help card hover](components/crops/help-card-hover.png) ![Help card focus-visible](components/crops/help-card-focus-visible.png) ![Help card pressed](components/crops/help-card-pressed.png)

#### Email card
The "Email" help-card (mailto:support@fable.co); measured, never followed. Read as `email-card` on the support page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 610 x 120; padding 18px; background transparent; text Inter 18/24 600, #161015 `color.quote.theme.6`; transition border 0.2s ease, background 0.2s ease, color 0.2s ease; layers div.support-icon 71.4x84.0 rgb(249, 249, 249) 8px |

Child layers that carry the look: div 71.4x84 background #f9f9f9 radius 8px.

![Email card default](components/crops/email-card-default.png) ![Email card hover](components/crops/email-card-hover.png) ![Email card focus-visible](components/crops/email-card-focus-visible.png) ![Email card pressed](components/crops/email-card-pressed.png)

### Mobile (390 wide)

The phone surface at 390 wide: header, menu button and the full-viewport nav sheet it opens, the hero and club card, and the footer.

#### Mobile header
The phone top bar: Fable mark, "Sign up or log in" and cart icons. The off-canvas nav sheet is measured below in its opened state. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 60; background transparent; shadow rgba(0, 0, 0, 0.04) 0px 2px 3px -2px; text Inter 24/36 600, #070607 `color.black.default`; icon 82 x 33, #000000; layers header.css-1vg9pjt 390.0x60.0 rgba(0, 0, 0, 0.04) 0px 2px 3px -2px; div.css-1g7irsi 374.0x50.0 rgb(255, 255, 255) T:1px rgb(237, 237, 237) / R:1px rgb(237, 237, 237) / B:1px rgb(237, 237, 237) / L:1px rgb(237, 237, 237) rgba(0, 0, 0, 0.08) 0px 4px 12px 0px 12px; span.css-1pyn1fk 17.0x17.0 rgb(255, 255, 255) T:1px rgb(237, 237, 237) / L:1px rgb(237, 237, 237) 2px 0px 0px; div.css-ghxh7s 390.0x844.0.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile logo
The Fable mark-and-wordmark svg at 390 wide. Read as `m-logo` on the home page at 390 wide.

**Values (default).** size 82 x 33; background transparent; text Inter 16/24 400, #000000; transition border 0.2s ease, background 0.2s ease, color 0.2s ease; icon 82 x 33, #000000.

![Mobile logo default](components/crops/m-logo-default.png)

#### Mobile hero headline
The masthead at 390 wide. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 320 x 80; background transparent; text Heldane Display 46/40 500, #f7f4ee `color.pearl.extra.light`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile Get the app
The hero "Get the app" pill at 390 wide; measured, never clicked. Read as `m-getapp` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 160 x 52; border 2px solid #ffffff `color.white.default`; radius 60px; background #ffffff `color.white.default`; text Inter 14/21 600, #161015 `color.quote.theme.6`; transition border 0.2s ease, background 0.2s ease, color 0.2s ease |
| hover | border 2px solid #f9f9f9; background #f9f9f9; text Inter 14/21 600, #332e32 `component.skin.marketing.marketingPillHoverInk` |
| focus-visible | outline 2px solid #116ecd, offset 4px |
| pressed | border 2px solid #f9f9f9; background #f9f9f9; text Inter 14/21 600, #332e32 `component.skin.marketing.marketingPillHoverInk` |

![Mobile Get the app default](components/crops/m-getapp-default.png) ![Mobile Get the app hover](components/crops/m-getapp-hover.png) ![Mobile Get the app focus-visible](components/crops/m-getapp-focus-visible.png) ![Mobile Get the app pressed](components/crops/m-getapp-pressed.png)

#### Mobile club card
A Popular-clubs card at 390 wide. Read as `m-club-card` on the home page at 390 wide.

**Values (default).** size 316.89 x 380; background transparent; text Inter 10/12 700, #3f383d; icon 10 x 10, #000000; layers div.css-1xixpw4 85.0x136.0 T:2px rgb(255, 255, 255) / R:2px rgb(255, 255, 255) / B:2px rgb(255, 255, 255) / L:2px rgb(255, 255, 255) 8px.

Child layers that carry the look: div 85x136 border 2px #ffffff `color.white.default` radius 8px.

![Mobile club card default](components/crops/m-club-card-default.png)

#### Mobile footer
The near-black footer stacked at 390 wide. Read as `m-footer` on the home page at 390 wide.

**Values (default).** size 390 x 762; padding 80px 24px; background #070607 `color.black.default`; text Inter 18/24 600, #847f7c; icon 82 x 33, #ffffff `color.white.default`.

![Mobile footer default](components/crops/m-footer-default.png)

#### Mobile menu button
The hamburger div opening the off-canvas nav sheet; its rest states were measured and the sheet was opened once for the rows below. Read as `m-menu-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 18 x 16; background transparent; text Inter 16/24 400, #000000; layers span 18.0x2.0 rgb(22, 16, 21); span 18.0x2.0 rgb(22, 16, 21); span 18.0x2.0 rgb(22, 16, 21) |
| focus-visible | radius 4px; outline 2px solid #116ecd, offset 4px; layers div.css-1tnrd7z 18.0x16.0 2px solid rgb(17, 110, 205) offset 4px 4px; span 18.0x2.0 rgb(22, 16, 21); span 18.0x2.0 rgb(22, 16, 21); span 18.0x2.0 rgb(22, 16, 21) |

Child layers that carry the look: span 18x2 background #161015 `color.quote.theme.6`; span 18x2 background #161015 `color.quote.theme.6`; span 18x2 background #161015 `color.quote.theme.6`.

![Mobile menu button default](components/crops/m-menu-btn-default.png) ![Mobile menu button hover](components/crops/m-menu-btn-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-btn-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-btn-pressed.png)

#### Mobile nav sheet
The full-screen cream nav sheet slid in from x=-390: pill links (Clubs / Books / Library / Blog / Log in), footer links and the copyright line. Opened by clicking the hamburger — a local UI toggle. Read as `m-nav` on the home page at 390 wide.

**Values (default).** size 390 x 844; background #f7f4ee `color.pearl.extra.light`; text Inter 24/36 600, #070607 `color.black.default`; transition transform 0.2s ease.

![Mobile nav sheet default](components/crops/m-nav-default.png)

#### Nav sheet link
A pill link inside the opened nav sheet; measured while the sheet was open, never followed. Read as `m-nav-link` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 330 x 60; border 2px solid #ffffff `color.white.default`; radius 60px; background #ffffff `color.white.default`; text Inter 24/36 600, #070607 `color.black.default`; transition border 0.2s ease, background 0.2s ease, color 0.2s ease |
| hover | border 2px solid #f9f9f9; background #f9f9f9; text Inter 24/36 600, #332e32 `component.skin.marketing.marketingPillHoverInk` |
| focus-visible, pressed | border 2px solid #f9f9f9; background #f9f9f9; outline 2px solid #116ecd, offset 4px; text Inter 24/36 600, #332e32 `component.skin.marketing.marketingPillHoverInk` |

![Nav sheet link default](components/crops/m-nav-link-default.png) ![Nav sheet link hover](components/crops/m-nav-link-hover.png) ![Nav sheet link focus-visible](components/crops/m-nav-link-focus-visible.png) ![Nav sheet link pressed](components/crops/m-nav-link-pressed.png)

### Discover (dark)

The /discover cover wall — the only public page painted dark: a dimmed wall of book covers behind the wordmark, headline, book-search field, Shuffle/random button and 'What is this' control.

#### Cover wall
The /discover cover wall under its dark-green radial scrim (rgba(12, 92, 66, 0.85)); a whole-page dark surface, not a .dark-scope paint. Read as `disc-wall` on the discover page.

**Values (default).** size 1440 x 900; background transparent; image radial-gradient(120% 95% at 50% 32%, rgba(12, 92, 66, 0.85), transparent 64%), radial-gradient(85% 75% at 12% 4%, rgba(9, 74, 54, 0.6), transparent 62%), radial-gradient(80% 70% at 92% 100%, rgba(3, 4; text Heldane Display 20/20 600, #f7f4ee `color.pearl.extra.light`; icon 80.75 x 32.5, #f7f4ee `color.pearl.extra.light`.

![Cover wall default](components/crops/disc-wall-default.png)

#### Discover headline
"Find new books by browsing similar covers" — the Heldane Display 64px pearl masthead on the dark wall. Read as `disc-h1` on the discover page.

**Values (default).** size 1119.91 x 69.11; background transparent; text Heldane Display 64/69.12 500, #f7f4ee `color.pearl.extra.light`.

![Discover headline default](components/crops/disc-h1-default.png)

#### Book search field
The white 420x60 search pill ("Search for a book you love..."); focused and typed into then cleared — never submitted. Read as `disc-field` on the discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 420 x 60.19; padding 19.6px 30.8px 19.6px 61px; radius 60px; background #ffffff `color.white.default`; shadow rgba(12, 12, 12, 0.45) 0px 10px 34px 0px; text Inter 14/21 400, #161015 `color.quote.theme.6`; transition background 0.2s ease, color 0.2s ease, box-shadow 0.2s ease; placeholder rgba(22, 16, 21, 0.5) |
| focused, filled | shadow rgba(12, 12, 12, 0.45) 0px 10px 34px 0px, rgba(247, 244, 238, 0.7) 0px 0px 0px 3px |

![Book search field default](components/crops/disc-field-default.png) ![Book search field focused](components/crops/disc-field-focused.png) ![Book search field filled](components/crops/disc-field-filled.png)

#### Random button
The forest-400 "Random" pill shuffling the cover wall; measured, never clicked. Read as `disc-random` on the discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 126.78 x 50.38; padding 14.7px 22.4px; radius 999px; background #042119 `color.forest.400`; text Inter 14/21 500, #c5c1c5 `component.skin.discover.discoverPillInk`; transition border 0.2s ease, background 0.2s ease, color 0.2s ease; icon 17 x 17, #c5c1c5 `component.skin.discover.discoverPillInk` |
| hover, pressed | text Inter 14/21 500, #f7f4ee `color.pearl.extra.light`; icon 17 x 17, #f7f4ee `color.pearl.extra.light` |

![Random button default](components/crops/disc-random-default.png) ![Random button hover](components/crops/disc-random-hover.png) ![Random button focus-visible](components/crops/disc-random-focus-visible.png) ![Random button pressed](components/crops/disc-random-pressed.png)

#### What is this button
The matching "What is this?" pill; measured, never clicked. Read as `disc-whatis` on the discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 135.78 x 50.38; padding 14.7px 22.4px; radius 999px; background #042119 `color.forest.400`; text Inter 14/21 500, #c5c1c5 `component.skin.discover.discoverPillInk`; transition border 0.2s ease, background 0.2s ease, color 0.2s ease |
| hover, pressed | text Inter 14/21 500, #f7f4ee `color.pearl.extra.light` |

![What is this button default](components/crops/disc-whatis-default.png) ![What is this button hover](components/crops/disc-whatis-hover.png) ![What is this button focus-visible](components/crops/disc-whatis-focus-visible.png) ![What is this button pressed](components/crops/disc-whatis-pressed.png)

#### Fable wordmark (discover)
The fable wordmark link at the top of the dark wall; measured, never followed. Read as `disc-wordmark` on the discover page.

**Values (default).** size 80.75 x 32.5; background transparent; text Inter 16/16 500, #f7f4ee `color.pearl.extra.light`; transition border 0.2s ease, background 0.2s ease, color 0.2s ease; icon 80.75 x 32.5, #f7f4ee `color.pearl.extra.light`.

![Fable wordmark (discover) default](components/crops/disc-wordmark-default.png)

### Footer

The near-black page footer: link columns, legal links and the 'Your Privacy Choices' control.

#### Footer
The near-black footer: sitemap columns, social icons, legal links, "Your Privacy Choices". Read as `footer` on the home page.

**Values (default).** size 1440 x 507; padding 100px 52px; background #070607 `color.black.default`; text Inter 18/24 600, #847f7c.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer sitemap link; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 76.25 x 14; background transparent; text Inter 14/14 600, #ffffff `color.white.default`; transition border 0.2s ease, background 0.2s ease, color 0.2s ease |
| focus-visible | radius 4px; outline 2px solid #116ecd, offset 4px; layers a.css-1ge1xrf 76.3x14.0 2px solid rgb(17, 110, 205) offset 4px 4px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Your Privacy Choices
The footer's Osano "Your Privacy Choices" control; measured at rest — clicking it would open the consent manager, so it was never pressed. Read as `privacy-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 168 x 21; background transparent; text Inter 14/21 400, rgba(255, 255, 255, 0.5) `color.white.fade.50`; transition color 0.2s ease; icon 26 x 12, rgba(255, 255, 255, 0.5) `color.white.fade.50` |
| hover | text Inter 14/21 400, #ffffff `color.white.default`; icon 26 x 12, #ffffff `color.white.default` |

![Your Privacy Choices default](components/crops/privacy-btn-default.png) ![Your Privacy Choices hover](components/crops/privacy-btn-hover.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Fable wordmark, the person/sign-in glyph, the cart bag, the hamburger and search glyphs, the share mark, the star ratings, the App Store and Google Play badges) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Fable's product is the signed-in app: joined clubs, discussion threads, the reader, reading lists, streaks and stats — every post-login surface needs an account and was never reached. /signin and /signup are the only app surfaces a signed-out visitor sees, and they were measured as forms, never submitted; 'Continue with Google' and 'Continue with Apple' were never pressed.

### Pages

- **The account.** Every post-login surface was never reached; 'Join the club', 'Login with email', 'Sign up' and the SSO buttons were measured, never pressed; the App Store / Google Play badges were never followed.
- **E-commerce.** Fable sells ebooks; the cart icon, purchase flows and /checkout were never opened.
- **Club and book routes** are covered by one genre shelf (/club/fantasy), one public club and one book page; the other genre, club and book routes are the same templates, unmeasured.
- **Blog articles** are covered by one captured post (/blog/how-to-start-a-book-club); the other posts are the same template, unmeasured.
- **Legal pages** (/terms, /privacy, /copyright-policy) share the guidelines template; only /community-guidelines was shot.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading and validation states** were not seen on the public surface — the sign-in form was never submitted.

### Themes

Fable has no user theme toggle and no `prefers-color-scheme` switch on the public surface. Every captured page paints light except /discover, a standalone dark cover-wall page. The stylesheet additionally ships a scoped `.dark` custom-property layer used by app reading/detail surfaces; the dark token set resolves those declarations, but no public page applies the class — painted dark evidence is the discover page only.

### Fonts

- **Heldane Display** (`heldane`, every display heading and the marketing hero) and **Inter** (UI and body text) are the served faces; the stylesheet also declares reader faces (for the signed-in book reader). The style guide falls back to system serif/sans.

### Screenshots

- The book covers, club photography and article images in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article copy, club names, book descriptions and review text are the product's content; only frames and components were measured.
