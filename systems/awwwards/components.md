# Awwwards components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Screenshots were taken from awwwards.com on 2026-11-21, signed out, in headless Chrome at 1440 x 900 (the Mobile group at 390 x 844). Computed styles were read on 2026-11-11 from the same class selectors. Nothing was voted on, signed into, created, sent or submitted. The control map is [site-tree.md](site-tree.md).

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (36 components, 57 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (55 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the site paints one light theme. Desktop shots are 1440 x 900 at 1x, including the `-full` whole-page shots; mobile shots are `mobile-{page}-light-{state}.png` at 2x, so a 390-wide viewport — and a 390-wide full page — comes out 780 pixels wide. Read mobile sizes at half the pixels.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [arrival](screenshots/home-light-arrival.png), [default](screenshots/home-light-default.png), [explore-open](screenshots/home-light-explore-open.png), [full](screenshots/home-light-full.png) |
| Winners grid | `/websites/` | [default](screenshots/websites-light-default.png), [filter-open](screenshots/websites-light-filter-open.png), [full](screenshots/websites-light-full.png) |
| Nominees | `/websites/nominees/` | [default](screenshots/nominees-light-default.png), [full](screenshots/nominees-light-full.png) |
| Sites of the Day | `/websites/sites_of_the_day/` | [default](screenshots/sotd-light-default.png), [full](screenshots/sotd-light-full.png) |
| Sites of the Month | `/websites/sites_of_the_month/` | [default](screenshots/sotm-light-default.png), [full](screenshots/sotm-light-full.png) |
| Sites of the Year | `/websites/sites_of_the_year/` | [default](screenshots/soty-light-default.png), [full](screenshots/soty-light-full.png) |
| Honors | `/honors/winners` | [default](screenshots/honors-light-default.png), [full](screenshots/honors-light-full.png) |
| Most Awarded Profiles | `/winner-list/` | [default](screenshots/winners-light-default.png), [full](screenshots/winners-light-full.png) |
| Jury 2026 | `/jury/2026/` | [default](screenshots/jury-light-default.png), [full](screenshots/jury-light-full.png) |
| Annual Awards | `/annual-awards/` | [default](screenshots/awards-light-default.png), [full](screenshots/awards-light-full.png) |
| Site detail | `first /websites/ card whose page still has a Vote control` | [default](screenshots/site-light-default.png), [full](screenshots/site-light-full.png) |
| Collections | `/collections/` | [default](screenshots/collections-light-default.png), [full](screenshots/collections-light-full.png) |
| Library | `/library/` | [default](screenshots/library-light-default.png), [full](screenshots/library-light-full.png) |
| Elements | `/elements/` | [default](screenshots/elements-light-default.png), [full](screenshots/elements-light-full.png) |
| Directory | `/directory/` | [default](screenshots/directory-light-default.png), [full](screenshots/directory-light-full.png) |
| Academy | `/academy/` | [default](screenshots/academy-light-default.png), [full](screenshots/academy-light-full.png) |
| Jobs | `/jobs/` | [default](screenshots/jobs-light-default.png), [full](screenshots/jobs-light-full.png) |
| Market | `/market/` | [default](screenshots/market-light-default.png) |
| Be Pro | `/pro` | [default](screenshots/pro-light-default.png), [full](screenshots/pro-light-full.png) |
| Submit gate | `/submit/` | [default](screenshots/submit-light-default.png), [full](screenshots/submit-light-full.png) |
| User plans | `/plans/user-plans` | [default](screenshots/plans-light-default.png), [full](screenshots/plans-light-full.png) |
| Blog | `/blog/` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Conferences | `/conferences/` | [default](screenshots/conferences-light-default.png), [full](screenshots/conferences-light-full.png) |
| FAQs | `/faqs/` | [default](screenshots/faqs-light-default.png), [full](screenshots/faqs-light-full.png) |
| About | `/about-us/` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Contact | `/contact-us/` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Cookies policy | `/cookies-policy/` | [default](screenshots/cookies-light-default.png), [full](screenshots/cookies-light-full.png) |
| Legal terms | `/terms/` | [default](screenshots/terms-light-default.png), [full](screenshots/terms-light-full.png) |
| Privacy policy | `/privacy-policy/` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Winners grid, phone | `/websites/` | [default](screenshots/mobile-websites-light-default.png), [full](screenshots/mobile-websites-light-full.png) |
| Collections, phone | `/collections/` | [default](screenshots/mobile-collections-light-default.png), [full](screenshots/mobile-collections-light-full.png) |
| Directory, phone | `/directory/` | [default](screenshots/mobile-directory-light-default.png), [full](screenshots/mobile-directory-light-full.png) |
| Academy, phone | `/academy/` | [default](screenshots/mobile-academy-light-default.png), [full](screenshots/mobile-academy-light-full.png) |
| Jobs, phone | `/jobs/` | [default](screenshots/mobile-jobs-light-default.png), [full](screenshots/mobile-jobs-light-full.png) |
| Market, phone | `/market/` | [default](screenshots/mobile-market-light-default.png) |
| Blog, phone | `/blog/` | [default](screenshots/mobile-blog-light-default.png), [full](screenshots/mobile-blog-light-full.png) |
| Submit, phone | `/submit/` | [default](screenshots/mobile-submit-light-default.png), [full](screenshots/mobile-submit-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Arrival view | home, on load | the page as it arrives, before any consent or promo layer is hidden (nothing is ever answered) | [home-light-arrival](screenshots/home-light-arrival.png) |
| Explore dropdown | home header | the Explore control's own toggle | [home-light-explore-open](screenshots/home-light-explore-open.png) |
| Card hover layer | home site cards | not captured on 2026-11-21: the card hover timed out in headless Chrome | Not captured |
| Filter dropdown | winners grid | the first filter tab's own toggle | [websites-light-filter-open](screenshots/websites-light-filter-open.png), [filter-dropdown](#filter-dropdown) |
| Mobile menu | home, phone | the menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 7 components were given a real keyboard focus. 3 draw an outline ring: `nav-item` (1px auto #005fcc `measured.focus-ring`, offset 1px), `grid-card-link` (1px auto #005fcc `measured.focus-ring`, offset 1px), `footer-link` (1px auto #005fcc `measured.focus-ring`, offset 1px). The other 4 show no measured change: `submit-cta`, `vote-button`, `bepro-link`, `tag-chip`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): controls keep their shape — Awwwards answers hover with fill and outline swaps rather than scale or shadow. Nothing a real press would vote, submit or sign in was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.3s | `ease` | all, background, border, color | bepro-link, coll-card, filter-item, filter-option, grid-card, m-nav-link, nav-item, site-card and more |
| 0.6s | `ease` | all | filter-dropdown |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Site card](#site-card) | 658 x 493.5 | - | 14px | transparent | none | 0 |
| [Grid card](#grid-card) | 432 x 324 | - | 4px | transparent | none | 0 |
| [Collection card](#collection-card) | 139.8 x 42 | - | 8px | #f8f8f8 `color.neutral.avatarBg` | none | 0px 24px |
| [Plan/pricing card](#planpricing-card) | 1336 x 550.91 | - | - | transparent | none | 0 |
| [Mobile site card](#mobile-site-card) | 358 x 268.5 | - | - | transparent | none | 0 |
| [Score box](#score-box) | 69.38 x 83.72 | 1px solid #222222 `color.neutral.buttonBorder` | 8px | transparent | none | 0 |

## Components

### Shell and navigation

The header (wordmark, Explore/Directory/Academy/Jobs/Market nav, Log in / Sign Up, Be Pro, Submit Website).

#### Header
The top bar: wordmark, Explore/Directory/Academy/Jobs/Market nav, Log in / Sign Up / Be Pro / Submit Website. Read as `header` on the home page.

**Values (default).** size 1440 x 54; background transparent; text Inter Tight 14/28 500, #222222 `color.neutral.buttonBorder`; layers div.header-main__overlay 2880.0x1800.0 rgba(0, 0, 0, 0.7); div.header-main__container 1336.0x54.0 rgb(233, 233, 233) 8px; div.nav-header-main__dropdown 1336.0x0.0 rgb(237, 237, 237) 0px 0px 8px 8px; span.budget-tag.budget-tag--solid--black 0.0x0.0 rgb(34, 34, 34) 4px; span.budget-tag.budget-tag--small--solid--black 28.2x16.0 rgb(34, 34, 34) 4px; span::before.budget-tag.budget-tag--small--solid--bl.

Child layers that carry the look: div 2880x1800 background rgba(0, 0, 0, 0.7); div 1336x54 background #e9e9e9 `color.neutral.chipBg` radius 8px; div 1336x0 background #ededed `color.neutral.fieldBorder` radius 0px 0px 8px 8px.

![Header default](components/crops/header-default.png)

#### Logo
The wordmark link back to /. Read as `logo` on the home page.

**Values (default).** size 30 x 16; background transparent; text Inter Tight 14/28 400, #222222 `color.neutral.buttonBorder`; icon 30 x 16, #222222 `color.neutral.buttonBorder`.

![Logo default](components/crops/logo-default.png)

#### Nav link
A top-level nav link (Directory). Measured, never followed. Read as `nav-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 56.67 x 54; background transparent; text Inter Tight 14/28 500, #222222 `color.neutral.buttonBorder`; transition all 0.3s ease |
| hover | opacity 0.7 |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring`, offset 1px; layers a.nav-header-main__link 56.7x54.0 |
| pressed | opacity 0.7 |

![Nav link default](components/crops/nav-item-default.png) ![Nav link hover](components/crops/nav-item-hover.png) ![Nav link focus-visible](components/crops/nav-item-focus-visible.png) ![Nav link pressed](components/crops/nav-item-pressed.png)

#### Log in link
Log in in the site header. Measured, never followed — the click opens nothing headless and no login page exists signed-out. Read as `login-link` on the page.

Not on the page when it was captured.

#### Sign Up link
Sign Up in the site header. Measured, never followed. Read as `signup-link` on the page.

Not on the page when it was captured.

#### Submit Website button
The header CTA. Measured, never followed. Read as `submit-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 138.66 x 42; padding 0px 20px; border 1px solid #222222 `color.neutral.buttonBorder`; radius 8px; background transparent; text Inter Tight 14/42 500, #222222 `color.neutral.buttonBorder`; transition color 0.3s ease, background 0.3s ease, border 0.3s ease |
| hover, pressed | background #383838 `measured.action-hover`; text Inter Tight 14/42 500, #ffffff `color.neutral.buttonLabel` |

![Submit Website button default](components/crops/submit-cta-default.png) ![Submit Website button hover](components/crops/submit-cta-hover.png) ![Submit Website button focus-visible](components/crops/submit-cta-focus-visible.png) ![Submit Website button pressed](components/crops/submit-cta-pressed.png)

#### Be Pro link
The Be Pro upsell button in the header. Measured, never followed. Read as `bepro-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 80.02 x 42; padding 0px 20px; radius 8px; background #222222 `color.neutral.buttonBorder`; text Inter Tight 14/42 500, #ffffff `color.neutral.buttonLabel`; transition color 0.3s ease, background 0.3s ease, border 0.3s ease |
| hover, pressed | background #383838 `measured.action-hover` |

![Be Pro link default](components/crops/bepro-link-default.png) ![Be Pro link hover](components/crops/bepro-link-hover.png) ![Be Pro link focus-visible](components/crops/bepro-link-focus-visible.png) ![Be Pro link pressed](components/crops/bepro-link-pressed.png)

### Home

The Site of the Day hero card and the nominee cards below.

#### Section heading
"Site of the Day" heading over the first card. Read as `sotd-heading` on the home page.

**Values (default).** size 1336 x 359.47; background transparent; text Inter Tight 14/28 400, #222222 `color.neutral.buttonBorder`; layers strong.budget-tag.budget-tag--medium 98.7x23.0 T:1px solid rgba(34, 34, 34, 0.3) / R:1px solid rgba(34, 34, 34, 0.3) / B:1px solid rgba(34, 34, 34, 0.3) / L:1px solid rgba(34, 34, 34, 0.3) 4px; strong::before.link-underlined 70.2188pxx2px; strong::before.link-underlined 110.359pxx2px.

Child layers that carry the look: strong 98.7x23 border 1px solid rgba(34, 34, 34, 0.3) radius 4px; strong::before 70.2188pxx2px image linear-gradient(to right, #222222 `color.neutral.buttonBorder` 45%, rgba(34, 34, 34, 0.3) ; strong::before 110.359pxx2px image linear-gradient(to right, #222222 `color.neutral.buttonBorder` 45%, rgba(34, 34, 34, 0.3) .

![Section heading default](components/crops/sotd-heading-default.png)

#### Site card
A winning-site card: screenshot, title, author and rollover actions. Read as `site-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 658 x 493.5; radius 14px; background transparent; text Inter Tight 20.64/28 300, #222222 `color.neutral.buttonBorder`; transition all 0.3s ease; icon 14 x 11.89, #222222 `color.neutral.buttonBorder`; layers div.figure-rollover__hover 658.0x493.5; a.button.button--white--rounded 120.3x47.6 rgb(255, 255, 255) 8px |

Child layers that carry the look: div 658x493.5 image linear-gradient(0deg, rgba(0, 0, 0, 0.5) 0%, transparent 100%); a 120.3x47.6 background #ffffff `color.neutral.buttonLabel` radius 8px.

![Site card default](components/crops/site-card-default.png) ![Site card hover](components/crops/site-card-hover.png)

#### Card action
The "Vote Now" button revealed by hovering a site card; it stayed display:none under headless hover — see card-action on the site page instead. Read as `card-cta` on the home page.

Not on the page when it was captured.

### Winners grid

The /websites/ grid: the Awards/Category/Tag/Technology filter bar and the site cards.

#### Grid title
"Winning websites. Web Design Inspiration". Read as `grid-title` on the winners grid page.

**Values (default).** size 305.89 x 18.2; background transparent; text Inter Tight 14/18.2 600, #222222 `color.neutral.buttonBorder`; layers ::after rgba(0, 0, 0, 0) 1px none 1; h1::after.breadcrumb-filters__title autoxauto T:1px solid rgb(34, 34, 34) / R:1px solid rgb(34, 34, 34) / B:1px solid rgb(34, 34, 34) / L:1px solid rgb(34, 34, 34) 2px.

Child layers that carry the look: h1::after autoxauto border 1px solid #222222 `color.neutral.buttonBorder` radius 2px.

![Grid title default](components/crops/grid-title-default.png)

#### Filter tab
An Awards/Category/Tag/Technology filter tab on the winners grid. Read as `filter-item` on the winners grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 105.78 x 42; padding 0px 24px; radius 8px; background #f8f8f8 `color.neutral.avatarBg`; text Inter Tight 13.3/28 500, #222222 `color.neutral.buttonBorder`; transition all 0.3s ease; icon 8 x 8, #222222 `color.neutral.buttonBorder` |
| hover | background #ffffff `color.neutral.buttonLabel` |

![Filter tab default](components/crops/filter-item-default.png) ![Filter tab hover](components/crops/filter-item-hover.png)

#### Filter dropdown
The open sublist under a filter tab. Read as `filter-dropdown` on the winners grid page.

**Values (default).** size 280 x 346; padding 8px 8px 0px 8px; radius 8px; background #f8f8f8 `color.neutral.avatarBg`; shadow rgba(0, 0, 0, 0.2) 0px 0px 6px 0px; text Inter Tight 13.3/28 500, #222222 `color.neutral.buttonBorder`; transition all 0.6s ease.

![Filter dropdown default](components/crops/filter-dropdown-default.png)

#### Filter option
An option row inside the open filter dropdown. Measured, never followed. Read as `filter-option` on the winners grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 264 x 40; padding 0px 8px 0px 30px; radius 8px; background transparent; text Inter Tight 13.3/28 500, #222222 `color.neutral.buttonBorder`; transition all 0.3s ease; layers ::before rgba(0, 0, 0, 0) 1px none 1; ::after rgb(34, 34, 34) 0px none 0; a::before.nav-filters__subitem 12pxx12px T:1px solid rgb(167, 167, 167) / R:1px solid rgb(167, 167, 167) / B:1px solid rgb(167, 167, 167) / L:1px solid rgb(167, 167, 167) 50%; a::after.nav-filters__subitem 8pxx8px rgb(34, 34, 34) 50% |
| hover | background #ededed `color.neutral.fieldBorder`; layers ::before rgba(0, 0, 0, 0) 1px none 1; ::after rgb(34, 34, 34) 0px none 1 |

Child layers that carry the look: a::before 12pxx12px border 1px solid #a7a7a7 radius 50%; a::after 8pxx8px background #222222 `color.neutral.buttonBorder` radius 50%.

![Filter option default](components/crops/filter-option-default.png) ![Filter option hover](components/crops/filter-option-hover.png)

#### Grid card
A winning-site card on the winners grid. Read as `grid-card` on the winners grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 432 x 324; radius 4px; background transparent; text Inter Tight 15/28 300, #222222 `color.neutral.buttonBorder`; transition all 0.3s ease; icon 15 x 15, #222222 `color.neutral.buttonBorder`; layers div.figure-rollover__hover 432.0x324.0 |

Child layers that carry the look: div 432x324 image linear-gradient(0deg, rgba(0, 0, 0, 0.5) 0%, transparent 100%).

![Grid card default](components/crops/grid-card-default.png) ![Grid card hover](components/crops/grid-card-hover.png)

#### Grid card link
The card anchor to /sites/<slug>. Measured, never followed. Read as `grid-card-link` on the winners grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 432 x 324; background transparent; text Inter Tight 15/28 300, #222222 `color.neutral.buttonBorder` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring`, offset 1px; layers a.figure-rollover__link 432.0x324.0 |

![Grid card link default](components/crops/grid-card-link-default.png) ![Grid card link focus-visible](components/crops/grid-card-link-focus-visible.png)

### Site detail

A /sites/ entry: display title, jury score box, the gold Vote button and category tags.

#### Site title
Read as `site-title` on the site-detail page.

**Values (default).** size 1336 x 253.47; background transparent; text Inter Tight 126.73/126.73 600, #222222 `color.neutral.buttonBorder`.

![Site title default](components/crops/site-title-default.png)

#### Score box
The jury score panel (Design/Usability/Creativity/Content). Read as `score-box` on the site-detail page.

**Values (default).** size 69.38 x 83.72; border 1px solid #222222 `color.neutral.buttonBorder`; radius 8px; background transparent; text Inter Tight 13.97/13.97 500, #222222 `color.neutral.buttonBorder`.

![Score box default](components/crops/score-box-default.png)

#### Score note
Read as `score-note` on the site-detail page.

**Values (default).** size 45.03 x 30.44; background transparent; text Inter Tight 23.05/13.97 600, #222222 `color.neutral.buttonBorder`.

![Score note default](components/crops/score-note-default.png)

#### Vote button
The vote CTA; measured except a real press — voting records a score and is never clicked. Read as `vote-button` on the site-detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 190.52 x 60; padding 0px 15.6px; radius 8px; background #e3c352 `measured.action-award`; text Inter Tight 13/60 600, #222222 `color.neutral.buttonBorder`; transition all 0.3s ease |
| hover | opacity 0.8 |

![Vote button default](components/crops/vote-button-default.png) ![Vote button hover](components/crops/vote-button-hover.png) ![Vote button focus-visible](components/crops/vote-button-focus-visible.png)

#### Visit link
The external visit-site toolbar icon; the hover pass found it outside the viewport, so only the at-rest reading stands. Read as `visit-link` on the site-detail page.

**Values (default).** size 20 x 20; background transparent; text Inter Tight 14/28 300, #222222 `color.neutral.buttonBorder`; transition all 0.3s ease; icon 20 x 20, #222222 `color.neutral.buttonBorder`.

![Visit link default](components/crops/visit-link-default.png)

#### Tag chip
A category tag (Art & Illustration…) on the site detail page. Measured, never followed. Read as `tag-chip` on the site-detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 179.08 x 48; padding 0px 24px; border 1px solid #a7a7a7; radius 72px; background transparent; text Inter Tight 18/28 600, #222222 `color.neutral.buttonBorder`; transition color 0.3s ease, background 0.3s ease, border 0.3s ease |
| hover, pressed | border 1px solid #222222 `color.neutral.buttonBorder` |

![Tag chip default](components/crops/tag-chip-default.png) ![Tag chip hover](components/crops/tag-chip-hover.png) ![Tag chip focus-visible](components/crops/tag-chip-focus-visible.png) ![Tag chip pressed](components/crops/tag-chip-pressed.png)

#### Card action
A rollover action icon on a related-site card. Measured, never clicked. Read as `card-action` on the page.

Not on the page when it was captured.

### Collections

The curated collections index.

#### Collections title
Read as `coll-title` on the collections index page.

**Values (default).** size 99 x 18.2; background transparent; text Inter Tight 14/18.2 600, #222222 `color.neutral.buttonBorder`; layers ::after rgba(0, 0, 0, 0) 1px none 1; h1::after.breadcrumb-filters__title autoxauto T:1px solid rgb(34, 34, 34) / R:1px solid rgb(34, 34, 34) / B:1px solid rgb(34, 34, 34) / L:1px solid rgb(34, 34, 34) 2px.

Child layers that carry the look: h1::after autoxauto border 1px solid #222222 `color.neutral.buttonBorder` radius 2px.

![Collections title default](components/crops/coll-title-default.png)

#### Collection card
A curated-collection card. Measured, never followed. Read as `coll-card` on the collections index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 139.8 x 42; padding 0px 24px; radius 8px; background #f8f8f8 `color.neutral.avatarBg`; text Inter Tight 13.3/28 500, #222222 `color.neutral.buttonBorder`; transition all 0.3s ease; icon 17 x 17, #222222 `color.neutral.buttonBorder` |
| hover | background #ffffff `color.neutral.buttonLabel` |

![Collection card default](components/crops/coll-card-default.png) ![Collection card hover](components/crops/coll-card-hover.png)

### Submit gate

The public /submit/ page; nothing was submitted.

#### Submit title
Read as `submit-title` on the submit gate page.

**Values (default).** size 505.11 x 100.53; background transparent; text Inter Tight 41.88/50.26 600, #222222 `color.neutral.buttonBorder`.

![Submit title default](components/crops/submit-title-default.png)

#### Submit CTA
The first call-to-action on /submit/. Measured, never followed. Read as `submit-cta-2` on the page.

Not on the page when it was captured.

#### Plan/pricing card
A submission plan card where the page offers one. Read as `plan-card` on the submit gate page.

**Values (default).** size 1336 x 550.91; background transparent; text Inter Tight 29.29/38.08 600, #222222 `color.neutral.buttonBorder`; icon 20 x 20, #222222 `color.neutral.buttonBorder`; layers div.plan.plan--standard 432.0x550.9 rgb(255, 255, 255) 14px; a.button.button--large--outline--rounded 230.0x72.0 T:1px solid rgb(34, 34, 34) / R:1px solid rgb(34, 34, 34) / B:1px solid rgb(34, 34, 34) / L:1px solid rgb(34, 34, 34) 8px; div.plan.plan--pro 884.0x550.9 rgb(34, 34, 34) 14px; a.button.button--medium--outline--white--rounded 230.0x60.0 T:1px solid rgb(255, 255, 255) / R:1px solid rgb(25.

Child layers that carry the look: div 432x550.9 background #ffffff `color.neutral.buttonLabel` radius 14px; a 230x72 border 1px solid #222222 `color.neutral.buttonBorder` radius 8px; div 884x550.9 background #222222 `color.neutral.buttonBorder` radius 14px.

![Plan/pricing card default](components/crops/plan-card-default.png)

### Footer

The page footer and section links.

#### Footer
Read as `footer` on the home page.

**Values (default).** size 1440 x 407.38; background transparent; text Inter Tight 14/14 600, #222222 `color.neutral.buttonBorder`; icon 30 x 16, #222222 `color.neutral.buttonBorder`; layers div.footer__bottom 1336.0x71.2.

Child layers that carry the look: div 1336x71.2 image linear-gradient(to right, #222222 `color.neutral.buttonBorder` 0px, #222222 `color.neutral.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 58.77 x 17; background transparent; text Inter Tight 14/14 600, #222222 `color.neutral.buttonBorder` |
| hover | opacity 0.75 |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring`, offset 1px; layers a 58.8x17.0 |
| pressed | opacity 0.75 |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Mobile (390 wide)

The same surface at phone width, with the menu layer open.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 54; background #f8f8f8 `color.neutral.avatarBg`; text Inter Tight 14/28 300, #222222 `color.neutral.buttonBorder`; icon 16 x 16, #222222 `color.neutral.buttonBorder`.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 54 x 54; background transparent; text Inter Tight 14/28 400, #222222 `color.neutral.buttonBorder`; icon 16 x 16, #222222 `color.neutral.buttonBorder`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |

![Mobile menu button default](components/crops/m-menu-button-default.png) ![Mobile menu button hover](components/crops/m-menu-button-hover.png) ![Mobile menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The menu button after its own toggle; the crop is the open menu layer. Read as `m-menu-open` on the home page at 390 wide.

**Values (opened).** size 54 x 54; background transparent; text Inter Tight 14/28 400, #222222 `color.neutral.buttonBorder`; icon 16 x 16, #222222 `color.neutral.buttonBorder`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Mobile menu, open opened](components/crops/m-menu-open-opened.png)

#### Mobile nav link
A row inside the opened menu. Read as `m-nav-link` on the home page at 390 wide.

**Values (default).** size 390 x 54; padding 0px 16px; background transparent; text Inter Tight 14/28 400, #222222 `color.neutral.buttonBorder`; transition all 0.3s ease.

![Mobile nav link default](components/crops/m-nav-link-default.png)

#### Mobile site card
A winning-site card on mobile. Read as `m-site-card` on the home page at 390 wide.

**Values (default).** size 358 x 268.5; background transparent; text Inter Tight 18/28 300, #222222 `color.neutral.buttonBorder`.

![Mobile site card default](components/crops/m-site-card-default.png)

### Other



## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Awwwards' artwork (inline SVG). Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **Voting, submitting and anything behind sign-in.** The Vote button was measured but never clicked (a vote records a score). `/submit/` and `/contact-us/` were never submitted. `https://www.awwwards.com/login` asks for email or username and a password. Those fields were not filled. Google, Twitter, and Facebook on that page were not clicked. `/register` and `/forgot-password` were not opened.
- **Anything that sends or joins.** No form was submitted, no vote cast, no search query was run, no account was created, no consent choice was made.
- **The filter dropdown's innards** were measured at the first option only. Academy, Jobs, Market, Directory, and Jury have viewport screenshots. Their inner filters were not re-measured.
- **The card hover layer.** The Vote Now overlay stayed `display:none` under headless hover (recorded as a gap on `card-cta`/`card-action`). The 2026-11-21 recapture of `home-light-card-hover` timed out, so that file is gone.
- **Market full page.** `/market/` grows without bound. The capture keeps the viewport shot. The 8-chunk full-page tiles were not committed.
- **Unread token values** on pages that were only screenshotted (directory filters, job cards, course cards, legal type) are Not captured.
- **Headless access.** awwwards.com served headless Chrome a 200 on every captured route on 2026-11-21.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Keyboard focus on the mobile menu button** did not land (recorded as an error state on `m-menu-button`, not as evidence).
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

The site paints one light theme on every captured route; a `.dark` probe resolves every custom property identically. No dark or reduced-contrast mode is offered.

### Fonts

- **Inter Tight** is the single family — every measured component resolves to it, at declared weights 300-800 (`--font-light` to `--font-black`). Only one `@font-face` rule was captured; the variable font is self-hosted.

### Screenshots

- Winning-site thumbnails, nominee artwork and the Awwwards wordmark in the screenshots are third-party/site content. The site detail captured is whichever `/websites/` card first had open voting at run time (recorded as `site_url` in components-computed.json); another run may land on a different entry.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Winning-site thumbnails and nominee artwork are the entrants' content; only the frames and components were measured.
