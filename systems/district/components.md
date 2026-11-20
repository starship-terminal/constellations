# District components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from district.in on 2026-11-15, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, booked, bought or submitted; nav links, category tabs, filter chips, cards and Book buttons were measured, never followed or pressed. The public pages paint the light theme; the dark pass flips the product's own html[data-theme=dark] attribute, so both themes are real painted evidence.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (34 components, 65 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (65 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{state}.png`: `{page}-dark-*` shots flip the product's own html[data-theme=dark] attribute before capture. Desktop shots are 1440 x 900 at 1x; the phone surfaces are `mobile-{page}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [dark-default](screenshots/home-dark-default.png), [dark-full](screenshots/home-dark-full.png), [default](screenshots/home-default.png), [full](screenshots/home-full.png) |
| Home, dark | `/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png) |
| Movies | `/movies/` | [dark-default](screenshots/movies-dark-default.png), [dark-full](screenshots/movies-dark-full.png), [default](screenshots/movies-default.png), [full](screenshots/movies-full.png) |
| Movies, dark | `/movies/` | [default](screenshots/movies-dark-default.png), [full](screenshots/movies-dark-full.png) |
| Dining | `/dining/` | [default](screenshots/dining-default.png), [full](screenshots/dining-full.png) |
| Events | `/events/` | [default](screenshots/events-default.png), [full](screenshots/events-full.png) |
| Comedy | `/events/comedy` | [default](screenshots/comedy-default.png), [full](screenshots/comedy-full.png) |
| Stores | `/stores/` | [default](screenshots/stores-default.png), [full](screenshots/stores-full.png) |
| Play | `/play/` | [default](screenshots/play-default.png), [full](screenshots/play-full.png) |
| Artist | `/events/samay-raina/artist` | [default](screenshots/artist-default.png), [full](screenshots/artist-full.png) |
| Tickets | `/events/all-stars-live-apr12-2026-buy-tickets` | [default](screenshots/tickets-default.png), [full](screenshots/tickets-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-default.png), [full](screenshots/mobile-home-full.png) |
| Movies, phone | `/movies/` | [default](screenshots/mobile-movies-default.png), [full](screenshots/mobile-movies-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Dark theme | /, /movies/ | html[data-theme=dark] was applied and the repaint measured — the same attribute the DDS dark layer declares | [dk-body](#dark-body) |
| Booking | ticket page | the Book CTA and date pills were measured at every paintable state, never pressed — payment gates on the Zomato account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 7 components were given a real keyboard focus. 2 draw an outline ring: `mv-chip` (1px auto #101010 `color.semantics-dark-background-universal-inverse-strong`, offset 0px), `tk-book` (1px auto #101010 `color.semantics-dark-background-universal-inverse-strong`, offset 0px). The other 5 show no measured change: `nv-mark`, `nv-tab`, `nv-tab-active`, `nv-search`, `at-book`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | m-tab, nv-tab, nv-tab-active |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Mobile card](#mobile-card) | 364 x 271.75 | - | - | transparent | none | 0 |

## Components

### App chrome

The fixed app bar and footer: the District mark, the For you / Dining / Movies / Events / Comedy / Stores / Activities / Play tab row, the search affordance and location.

#### Top nav
The fixed app bar — District mark, category tabs, search and location. Read as `nv-bar` on the home feed page.

**Values (default).** size 1440 x 75; padding 8px 0px 12px 0px; border B: 1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary`; background #ffffff `color.background.primary`; text BeVietnamPro 16/24 600, #131316 `color.button.outline.border`; icon 32 x 32, #6444e4 `color.border-brand`.

![Top nav default](components/crops/nv-bar-default.png)

#### District mark
The District logo link in the top nav; measured, never followed. Read as `nv-mark` on the home feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 108 x 43.63; background transparent; text BeVietnamPro 16/24 400, #131316 `color.button.outline.border` |

![District mark default](components/crops/nv-mark-default.png) ![District mark hover](components/crops/nv-mark-hover.png) ![District mark focus-visible](components/crops/nv-mark-focus-visible.png) ![District mark pressed](components/crops/nv-mark-pressed.png)

#### Category tab
The Movies tab in the top category row — a real link; measured, never followed. Read as `nv-tab` on the home feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 84 x 36; padding 8px; radius 9999px; background transparent; text BeVietnamPro 14/20 600, #545459 `color.button.secondary.border.pressed`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1); layers a.md:dds-px-2.dds-py-2 84.0x36.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px 9999px |

![Category tab default](components/crops/nv-tab-default.png) ![Category tab hover](components/crops/nv-tab-hover.png) ![Category tab focus-visible](components/crops/nv-tab-focus-visible.png) ![Category tab pressed](components/crops/nv-tab-pressed.png)

#### Category tab (For you)
The "For you" home tab — the selected state of the category row. Read as `nv-tab-active` on the home feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 84 x 36; padding 8px; radius 9999px; background #eae5ff `color.gradient-purple`; text BeVietnamPro 14/20 600, #231268 `color.text.accent.purple`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1) |

![Category tab (For you) default](components/crops/nv-tab-active-default.png) ![Category tab (For you) hover](components/crops/nv-tab-active-hover.png) ![Category tab (For you) focus-visible](components/crops/nv-tab-active-focus-visible.png) ![Category tab (For you) pressed](components/crops/nv-tab-active-pressed.png)

#### Search field
The search affordance linking to /search; hover/focus measured, never followed. Read as `nv-search` on the home feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 28 x 28; background transparent; text BeVietnamPro 16/24 400, #131316 `color.button.outline.border`; icon 18 x 18, #6444e4 `color.border-brand` |

![Search field default](components/crops/nv-search-default.png) ![Search field hover](components/crops/nv-search-hover.png) ![Search field focus-visible](components/crops/nv-search-focus-visible.png) ![Search field pressed](components/crops/nv-search-pressed.png)

#### Site footer
The District sitemap footer. Read as `ft-bar` on the home feed page.

**Values (default).** size 1440 x 410.5; background #1e1e20 `color.border.selection`; text BeVietnamPro 14/21 600, #eaeaeb; icon 79.56 x 32, #ffffff `color.background.primary`.

![Site footer default](components/crops/ft-bar-default.png)

### Home feed

The '/' For-you feed: the page heading and the section rails (artist headshots, movies, events).

#### Page heading
The home feed heading. Read as `hm-h1` on the home feed page.

**Values (default).** size 263 x 20; background transparent; text BeVietnamPro 24/20 600, #131316 `color.button.outline.border`.

![Page heading default](components/crops/hm-h1-default.png)

#### Section heading
A feed section heading (artists / movies / events rail). Read as `hm-section` on the home feed page.

**Values (default).** size 314 x 20; background transparent; text BeVietnamPro 24/20 600, #131316 `color.button.outline.border`.

![Section heading default](components/crops/hm-section-default.png)

### Content cards

The booking cards: movie cards (poster, title, certificate, language), circular artist cards and event cards with dates, venues and prices.

#### Movie card
A movie card — poster art, title, certificate and language; hover measured, never followed. Read as `mc-card` on the home feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 197.33 x 348.45; background transparent; text BeVietnamPro 16/22 600, #131316 `color.button.outline.border`; layers div.sm:dds-mx-[0px].dds-min-h-[282px] 197.3x348.5 T:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` / R:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` / B:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` / L:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` 16px |

Child layers that carry the look: div 197.3x348.5 border 1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` radius 16px.

![Movie card default](components/crops/mc-card-default.png) ![Movie card hover](components/crops/mc-card-hover.png)

#### Movie title
The title line inside a movie card. Read as `mc-title` on the home feed page.

**Values (default).** size 77.81 x 22; background transparent; text BeVietnamPro 16/22 600, #131316 `color.button.outline.border`.

![Movie title default](components/crops/mc-title-default.png)

#### Artist card
An artist card in the circular headshot rail (Samay Raina, ALAN WALKER…); hover measured, never followed. Read as `ar-card` on the home feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 190 x 222; background transparent; text BeVietnamPro 16/24 600, #131316 `color.button.outline.border` |

![Artist card default](components/crops/ar-card-default.png) ![Artist card hover](components/crops/ar-card-hover.png)

#### Event card
An event card with date and venue; hover measured, never followed. Read as `ev-card` on the home feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 236 x 325; background transparent; text BeVietnamPro 18/28 600, #f7f7f7 `color.button.primary.label.default`; layers div.dds-relative.dds-overflow-hidden 236.0x325.0 #ffffff `color.background.primary` T:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` / R:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` / B:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` / L:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` 24px; div.dds-absolute.dds-inset-0 234.0x323.0; div.dds-flex.dds-flex- |

Child layers that carry the look: div 236x325 background #ffffff `color.background.primary` border 1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` radius 24px; div 234x323 image linear-gradient(to top, rgba(0, 0, 0, 0.92) 0%, rgba(0, 0, 0, 0.6) 45%, transparent 100%); div 210x89 border 1px solid rgba(247, 247, 247, 0.2).

![Event card default](components/crops/ev-card-default.png) ![Event card hover](components/crops/ev-card-hover.png)

#### Listing movie card
A movie card on the listing grid; hover measured, never followed. Read as `mv-card` on the movies listing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 197.33 x 348.44; background transparent; text BeVietnamPro 16/22 600, #131316 `color.button.outline.border`; layers div.sm:dds-mx-[0px].dds-min-h-[282px] 197.3x348.4 T:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` / R:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` / B:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` / L:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` 16px |

Child layers that carry the look: div 197.3x348.4 border 1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` radius 16px.

![Listing movie card default](components/crops/mv-card-default.png) ![Listing movie card hover](components/crops/mv-card-hover.png)

#### Certificate badge
The censor-certificate chip on a movie card (U / UA13+ / A). Read as `mv-cert` on the movies listing page.

Not on the page when it was captured.

#### Listing event card
An event card on the listing; hover measured, never followed. Read as `ev-listcard` on the events listing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 236 x 325; background transparent; text BeVietnamPro 18/28 600, #f7f7f7 `color.button.primary.label.default`; layers div.dds-relative.dds-overflow-hidden 236.0x325.0 #ffffff `color.background.primary` T:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` / R:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` / B:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` / L:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` 24px; div.dds-absolute.dds-inset-0 234.0x323.0; div.dds-flex.dds-flex- |

Child layers that carry the look: div 236x325 background #ffffff `color.background.primary` border 1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` radius 24px; div 234x323 image linear-gradient(to top, rgba(0, 0, 0, 0.92) 0%, rgba(0, 0, 0, 0.6) 45%, transparent 100%); div 210x89 border 1px solid rgba(247, 247, 247, 0.2).

![Listing event card default](components/crops/ev-listcard-default.png) ![Listing event card hover](components/crops/ev-listcard-hover.png)

#### Event price
A "₹1499 onwards" price line on an event card. Read as `ev-price` on the events listing page.

**Values (default).** size 440 x 24; background transparent; text BeVietnamPro 16/24 700, #131316 `color.button.outline.border`.

![Event price default](components/crops/ev-price-default.png)

### Listing page

The listing surfaces (/movies/, /events/, /events/comedy): headings, language/format filter chips and card grids.

#### Movies heading
The "Movies in <city>" listing heading. Read as `mv-h1` on the movies listing page.

**Values (default).** size 700 x 60; background transparent; text BeVietnamPro 40/60 700, #131316 `color.button.outline.border`.

![Movies heading default](components/crops/mv-h1-default.png)

#### Filter chip
A language/format filter chip on the listing; measured, never toggled. Read as `mv-chip` on the movies listing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 56 x 32; padding 8px 12px; border 1px solid rgba(0, 0, 0, 0.24) `color.border.intense`; radius 6px; background #ffffff `color.background.primary`; text BeVietnamPro 12/16 500, #131316 `color.button.outline.border` |
| focus-visible | outline 1px auto #101010 `color.semantics-dark-background-universal-inverse-strong`, offset 0px |

![Filter chip default](components/crops/mv-chip-default.png) ![Filter chip hover](components/crops/mv-chip-hover.png) ![Filter chip focus-visible](components/crops/mv-chip-focus-visible.png) ![Filter chip pressed](components/crops/mv-chip-pressed.png)

#### Events heading
The events listing heading. Read as `ev-h1` on the events listing page.

**Values (default).** size 440 x 60; background transparent; text BeVietnamPro 40/60 700, #131316 `color.button.outline.border`.

![Events heading default](components/crops/ev-h1-default.png)

#### Comedy heading
The comedy events listing heading. Read as `cm-h1` on the comedy listing page.

**Values (default).** size 626.94 x 60; background transparent; text ui-sans-serif 40/60 700, #131316 `color.button.outline.border`.

![Comedy heading default](components/crops/cm-h1-default.png)

#### Filter control
A listing filter control; measured, never opened. Read as `cm-filter` on the comedy listing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 632 x 500; background transparent; text ui-sans-serif 12/20 600, #131316 `color.button.outline.border`; layers div.dds-flex.dds-flex-col 132.0x52.0 #f1f1f2 `color.background.secondary`; div::after.dds-flex.dds-flex-col 132pxx52px; div.dds-bg-surface-secondary.dds-flex 500.0x500.0 #f1f1f2 `color.background.secondary` 0px 20px 20px 0px; input 0.0x0.0 #ffffff `color.background.primary` T:1px solid rgba(0, 0, 0, 0.24) `color.border.intense` / R:1px solid rgba(0, 0, 0, 0.24) `color.border.intense` / B:1px solid |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: div 132x52 background #f1f1f2 `color.background.secondary`; div::after 132pxx52px image linear-gradient(to right, #d5ccff `color.surface.accent.purple` -70%, transparent); div 500x500 background #f1f1f2 `color.background.secondary` radius 0px 20px 20px 0px.

![Filter control default](components/crops/cm-filter-default.png) ![Filter control hover](components/crops/cm-filter-hover.png) ![Filter control pressed](components/crops/cm-filter-pressed.png)

### Event / artist detail

The artist page and the ticket page: display names, upcoming-show cards, date pills, prices and the Book CTAs — measured, never pressed (booking gates on the Zomato account).

#### Artist name
The artist page display name. Read as `at-h1` on the artist page page.

**Values (default).** size 350.58 x 40; background transparent; text ui-sans-serif 32/40 700, #131316 `color.button.outline.border`.

![Artist name default](components/crops/at-h1-default.png)

#### Show card
An upcoming-show card on the artist page; hover measured, never followed. Read as `at-show` on the artist page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 296 x 544; background transparent; text ui-sans-serif 16/24 400, #131316 `color.button.outline.border`; layers div.dds-min-w-[268px].md:dds-min-w-[296px] 296.0x544.0 T:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` / R:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` / B:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` / L:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` 16px; div.dds-absolute.dds-px-3 88.3x36.0 #ffffff `color.background.primary` T:1px solid rgba(0, 0, |

Child layers that carry the look: div 296x544 border 1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` radius 16px; div 88.3x36 background #ffffff `color.background.primary` border 1px solid rgba(0, 0, 0, 0.1) radius 7px shadow rgba(0, 0, 0, 0.25) 0px 4px 4px 0px.

![Show card default](components/crops/at-show-default.png) ![Show card hover](components/crops/at-show-hover.png)

#### Book CTA
The booking link on the artist page — the show card itself navigates to the ticket page; measured at every paintable state, never followed — booking gates on the Zomato account. Read as `at-book` on the artist page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 296 x 544; background transparent; text ui-sans-serif 16/24 400, #131316 `color.button.outline.border`; layers div.dds-min-w-[268px].md:dds-min-w-[296px] 296.0x544.0 T:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` / R:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` / B:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` / L:1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` 16px; div.dds-absolute.dds-px-3 88.3x36.0 #ffffff `color.background.primary` T:1px solid rgba(0, 0, |

Child layers that carry the look: div 296x544 border 1px solid rgba(0, 0, 0, 0.08) `color.border.card.primary` radius 16px; div 88.3x36 background #ffffff `color.background.primary` border 1px solid rgba(0, 0, 0, 0.1) radius 7px shadow rgba(0, 0, 0, 0.25) 0px 4px 4px 0px.

![Book CTA default](components/crops/at-book-default.png) ![Book CTA hover](components/crops/at-book-hover.png) ![Book CTA focus-visible](components/crops/at-book-focus-visible.png) ![Book CTA pressed](components/crops/at-book-pressed.png)

#### Event title
The event detail title on the ticket page. Read as `tk-h1` on the ticket page page.

**Values (default).** size 169.13 x 38; background transparent; text ui-sans-serif 28/normal 700, #131316 `color.button.outline.border`.

![Event title default](components/crops/tk-h1-default.png)

#### Date pill
A date/time selector pill; measured, never confirmed. Read as `tk-date` on the ticket page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 162.13 x 20; background transparent; text ui-sans-serif 16/20 600, #6d49fd `color.border.accent.purple` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Date pill default](components/crops/tk-date-default.png) ![Date pill hover](components/crops/tk-date-hover.png) ![Date pill pressed](components/crops/tk-date-pressed.png)

#### Ticket price
The ticket price line. Read as `tk-price` on the ticket page page.

**Values (default).** size 41.19 x 24; background transparent; text ui-sans-serif 18/20 700, #131316 `color.button.outline.border`.

![Ticket price default](components/crops/tk-price-default.png)

#### Book button
The primary Book/Proceed CTA; hover/focus measured, never pressed — payment gates on the Zomato account. Read as `tk-book` on the ticket page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 162.97 x 52; padding 4px 32px; radius 12px; background #131316 `color.button.outline.border`; text ui-sans-serif 16/24 600, #ffffff `color.background.primary` |
| hover | background #1e1e20 `color.border.selection` |
| focus-visible | outline 1px auto #101010 `color.semantics-dark-background-universal-inverse-strong`, offset 0px |

![Book button default](components/crops/tk-book-default.png) ![Book button hover](components/crops/tk-book-hover.png) ![Book button focus-visible](components/crops/tk-book-focus-visible.png)

### Dark theme (data-theme=dark)

The same surfaces with the DDS dark theme applied through html[data-theme=dark] — the attribute the product's own theme layer resolves.

#### Dark body
The page background with data-theme=dark applied — the real dark surface the DDS declares. Read as `dk-body` on the home feed, dark page.

**Values (default).** size 1440 x 4254.58; background #131316 `color.background.primary`; text BeVietnamPro 16/24 600, #f7f7f7 `color.border.selection`; icon 32 x 32, #6444e4 `color.border-brand`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Dark nav
The top nav under the dark theme. Read as `dk-nav` on the home feed, dark page.

**Values (default).** size 1440 x 75; padding 8px 0px 12px 0px; border B: 1px solid rgba(255, 255, 255, 0.08) `color.border.subtle`; background #131316 `color.background.primary`; text BeVietnamPro 16/24 600, #f7f7f7 `color.border.selection`; icon 32 x 32, #6444e4 `color.border-brand`.

![Dark nav default](components/crops/dk-nav-default.png)

#### Dark card
A content card under the dark theme. Read as `dk-card` on the home feed, dark page.

**Values (default).** size 197.33 x 348.45; background transparent; text BeVietnamPro 16/22 600, #f7f7f7 `color.border.selection`; layers div.sm:dds-mx-[0px].dds-min-h-[282px] 197.3x348.5 T:1px solid rgba(255, 255, 255, 0.08) `color.border.subtle` / R:1px solid rgba(255, 255, 255, 0.08) `color.border.subtle` / B:1px solid rgba(255, 255, 255, 0.08) `color.border.subtle` / L:1px solid rgba(255, 255, 255, 0.08) `color.border.subtle` 16px.

Child layers that carry the look: div 197.3x348.5 border 1px solid rgba(255, 255, 255, 0.08) `color.border.subtle` radius 16px.

![Dark card default](components/crops/dk-card-default.png)

### Mobile (390 wide)

The phone surface at 390 wide: the app bar, a category tab and a content card.

#### Mobile nav
The phone app bar at 390px. Read as `m-bar` on the movies listing page at 390 wide.

**Values (default).** size 390 x 60; padding 8px 0px 0px 0px; background #ffffff `color.background.primary`; text BeVietnamPro 16/24 600, #131316 `color.button.outline.border`; icon 32 x 32, #6444e4 `color.border-brand`.

![Mobile nav default](components/crops/m-bar-default.png)

#### Mobile tab
A category tab at 390px. Read as `m-tab` on the movies listing page at 390 wide.

**Values (default).** size 84 x 60; padding 8px; radius 8px; background transparent; text BeVietnamPro 14/20 600, #545459 `color.button.secondary.border.pressed`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #545459 `color.button.secondary.border.pressed`; layers a.md:dds-px-2.dds-py-2 84.0x60.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px 8px.

![Mobile tab default](components/crops/m-tab-default.png)

#### Mobile card
A content card at 390px. Read as `m-card` on the movies listing page at 390 wide.

**Values (default).** size 364 x 271.75; background transparent; text BeVietnamPro 16/24 600, #131316 `color.button.outline.border`.

![Mobile card default](components/crops/m-card-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the District mark, the category tab icons, certificate chips and card artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Booking and payment need the Zomato account — the Book/Proceed CTAs lead to sign-in and checkout, which were never opened. What is genuinely public signed out: the home feed (/), the category listings (/movies/, /dining/, /events/, /stores/, /activities/, /play/, /events/comedy), artist pages (/events/<slug>/artist) and ticket pages (/events/<slug>-buy-tickets) with their dates and prices. The Book buttons were measured, never pressed.

### Pages

- **Book and Proceed actions.** The ticket-page Book buttons and the checkout they start gate on the Zomato account; they were measured at default/hover/focus-visible, never pressed.
- **Search and checkout flows.** The nav search affordance links to /search and the booking flow continues into sign-in; neither was followed — the query box, seat picker and payment forms are an authenticated boundary.
- **Dark pass.** The feed sections keep baked gradient art under html[data-theme=dark]; the repainted chrome and cards are the dark evidence, noted per component.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

There is no theme toggle signed out, but the DDS layer ships both themes: html[data-theme=light] is the default paint and html[data-theme=dark] is a complete declared dark block. The dark pass applies the attribute the product resolves — verified repainted chrome and cards — so dark.* tokens are measured dark paint, not a declared guess.

### Fonts

- **BeVietnamPro** (the UI face — nav, cards, filters, prices) and **PassengerSerif** (the display serif used for feature headings) are the served families, read from the @font-face declarations in the served sheets; the style guide falls back to system fonts.

### Screenshots

- Full-page shots are single document captures; the marketing pages' animated hero fields are motion media, frozen at capture time.
- Movie, artist and event names, posters, venues, dates and prices are the listings' published content; screenshots are 256-colour PNGs, read exact colours from the tokens or the raw files.

### Content left out

- Movie, artist and event names, posters, venues, dates and prices are the listings' published content; only frames and components were measured.
