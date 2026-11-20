# ClassPass components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from classpass.com on 2026-11-16, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, searched for, booked or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (50 components, 113 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `norms 14/14 500, #000`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (110 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the marketing site paints one light theme (the footer is a black island inside it). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages (1x on desktop, 2x on mobile); mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Search | `/search` | [default](screenshots/search-light-default.png), [filter-open](screenshots/search-light-filter-open.png), [full](screenshots/search-light-full.png) |
| Plans | `/plans` | [default](screenshots/plans-light-default.png), [full](screenshots/plans-light-full.png) |
| Features | `/features` | [default](screenshots/features-light-default.png), [full](screenshots/features-light-full.png) |
| How ClassPass works | `/how-classpass-works` | [default](screenshots/how-light-default.png), [full](screenshots/how-light-full.png) |
| Fitness | `/fitness` | [default](screenshots/fitness-light-default.png), [full](screenshots/fitness-light-full.png) |
| Gifts | `/gifts` | [default](screenshots/gifts-light-default.png), [full](screenshots/gifts-light-full.png) |
| Reviews | `/try/reviews` | [default](screenshots/reviews-light-default.png), [full](screenshots/reviews-light-full.png) |
| Partners | `/partners` | [default](screenshots/partners-light-default.png), [full](screenshots/partners-light-full.png) |
| Corporate wellness | `/corporate-wellness` | [default](screenshots/corp-light-default.png), [full](screenshots/corp-light-full.png) |
| About | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Contact | `/contact` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Terms | `/legal/terms-and-conditions` | [default](screenshots/terms-light-default.png) |
| Sign-in (boundary) | `/login` | [default](screenshots/signin-light-default.png) |
| Walkthrough (boundary) | `/walkthrough` | [default](screenshots/walk-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu-open](screenshots/mobile-home-light-menu-open.png) |
| Search, phone | `/search` | [default](screenshots/mobile-search-light-default.png), [full](screenshots/mobile-search-light-full.png) |
| Plans, phone | `/plans` | [default](screenshots/mobile-plans-light-default.png), [full](screenshots/mobile-plans-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Products menu, open | header, desktop | the nav item's own press | [home-light-menu](screenshots/home-light-menu.png), [menu-panel](#nav-menu) |
| Activity filter, open | search page | the filter button's own press | [search-light-filter-open](screenshots/search-light-filter-open.png), [filter-panel](#filter-panel) |
| Mobile menu, open | header, phone | the menu trigger's own press | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-menu-open](#mobile-menu-open) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 15 components were given a real keyboard focus (a further 2 could not be driven: `nav-login`, `nav-cta`). 15 show a visible focus state: `nav-item` (visible change in backgroundColor), `nav-dropdown` (visible change in backgroundColor), `footer-link` (1px auto #101010, offset 1px), `footer-social` (1px auto #101010, offset 1px), `filter-pill` (2px solid rgb(0, 85, 255) offset 0px on button.NdbE21qLuZOtwHTH6gip.TqHQqCBFnxwMo5dWH9VJ (child layer)), `filter-multi` (2px solid rgb(0, 85, 255) offset 0px on button.NdbE21qLuZOtwHTH6gip (child layer)), `universal-cta` (2px solid #0055ff `color.blue.500`, offset 1px), `faq-question` (1px auto #101010, offset 0px), `cms-cta` (1px auto rgb(16, 16, 16) offset 1px on a (child layer)), `signin-submit` (2px solid #0055ff `color.blue.500`, offset 0px), `signin-apple` (2px solid #0055ff `color.blue.500`, offset 0px), `signin-google` (2px solid #0055ff `color.blue.500`, offset 0px), `signin-forgot` (1px auto #101010, offset 1px), `walk-cta` (2px solid #0055ff `color.blue.500`, offset 0px), `m-menu-link` (visible change in backgroundColor).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): the blue controls step down the accent ramp — the CTA and sign-in submit go #0055ff -> #004de6 on hover -> #0044cc pressed; the dark buttons (walkthrough Next) go #111 -> #040404 -> #000; nav items keep their #f7f7f7 wash across hover, focus and press. Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.3s | `ease` | background-color, border-color, color | footer-link, footer-social, logo, m-menu-link, menu-card, nav-item, nav-login, signin-apple and more |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan slide (default)](#plan-slide-default) | 266.66 x 148 | - | 18px | #ffffff `color.paper.0` | rgba(1, 85, 254, 0.1) 0px 5px 16px 0px | 24px |
| [Venue card](#venue-card) | 790 x 112 | - | 5px | #ffffff `color.paper.0` | rgba(0, 0, 0, 0.32) 0px 8px 24px 0px | 0 |
| [Filter panel](#filter-panel) | 380 x 349 | - | 8px | #ffffff `color.paper.0` | rgba(0, 0, 0, 0.24) 0px 4px 12px 0px | 0 |
| [Hero activity card](#hero-activity-card) | 185 x 225 | - | 25px | rgba(0, 0, 0, 0.08) `color.black-alpha.8` | none | 0 |

## Components

### Shell and navigation

The white header bar, its Products flyout and the blue sign-up pill.

#### Header
The 64px top bar: wordmark, Search/Plans links, the "How it works" dropdown, Gifts/List-my-business/Corporate-wellness links, Log in and the promo CTA. Read as `header` on the home page.

**Values (default).** size 1440 x 64; background #ffffff `color.paper.0`; shadow rgba(0, 0, 0, 0.08) 0px 2px 10px 0px; text norms 36/40 500, #000000 `color.ink.900`; icon 24 x 24, #000000 `color.ink.900`.

![Header default](components/crops/header-default.png)

#### Logo
The ClassPass wordmark anchor. Read as `logo` on the home page.

**Values (default).** size 124 x 64; padding 0px 16px; background transparent; image url(…); text norms 36/40 500, #000000 `color.ink.900`; transition background-color 0.3s ease, color 0.3s ease.

![Logo default](components/crops/logo-default.png)

#### Nav link
A plain header link (Plans). Read as `nav-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 66 x 64; padding 0px 16px; background transparent; text norms 14/20 500, #000000 `color.ink.900`; transition background-color 0.3s ease, color 0.3s ease |
| hover, focus-visible, pressed | background #f7f7f7 `color.gray.100`; child paint a: size 66.0x64.0; background #f7f7f7 `color.gray.100` |

![Nav link default](components/crops/nav-item-default.png) ![Nav link hover](components/crops/nav-item-hover.png) ![Nav link focus-visible](components/crops/nav-item-focus-visible.png) ![Nav link pressed](components/crops/nav-item-pressed.png)

#### Nav dropdown
The "How it works" menu trigger (aria-haspopup=menu); its own press opens the link menu (opened state). Read as `nav-dropdown` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 138 x 64; padding 0px 16px; background transparent; text norms 14/20 500, #000000 `color.ink.900`; icon 24 x 24, #000000 `color.ink.900` |
| hover, focus-visible, pressed, opened | background #f7f7f7 `color.gray.100`; child paint button.NavDesktopDropdown_Button__R5NHb: size 138.0x64.0; background #f7f7f7 `color.gray.100` |

![Nav dropdown default](components/crops/nav-dropdown-default.png) ![Nav dropdown hover](components/crops/nav-dropdown-hover.png) ![Nav dropdown focus-visible](components/crops/nav-dropdown-focus-visible.png) ![Nav dropdown pressed](components/crops/nav-dropdown-pressed.png) ![Nav dropdown opened](components/crops/nav-dropdown-opened.png)

#### Nav menu
The "How it works" dropdown panel (Walkthrough / How ClassPass works / Features links), held open by the trigger toggle. Read as `menu-panel` on the home page.

Kept from an earlier run: the 2026-11-16 recapture did not find this component, so these readings may not match the current page or script.

**Values (default).** size 200 x 121; background #ffffff `color.paper.0`; shadow rgba(0, 0, 0, 0.08) 0px 2px 10px 0px; text norms 14/20 500, #000000 `color.ink.900`.

![Nav menu default](components/crops/menu-panel-default.png)

#### Menu item
A link row inside the open nav menu. Read as `menu-card` on the home page.

Kept from an earlier run: the 2026-11-16 recapture did not find this component, so these readings may not match the current page or script.

**Values (default).** size 200 x 60; padding 20px 16px; background transparent; wrapper div.NavDesktopDropdown_Items__MGAQs: shadow rgba(0, 0, 0, 0.08) 0px 2px 10px 0px; text norms 14/20 500, #000000 `color.ink.900`; transition background-color 0.3s ease, color 0.3s ease.

![Menu item default](components/crops/menu-card-default.png)

#### Log-in link
The header "Log in" link; measured never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 71 x 64; padding 0px 16px; background transparent; text norms 14/20 500, #000000 `color.ink.900`; transition background-color 0.3s ease, color 0.3s ease |
| pressed | background #f7f7f7 `color.gray.100`; child paint a: size 71.0x64.0; background #f7f7f7 `color.gray.100` |

![Log-in link default](components/crops/nav-login-default.png) ![Log-in link hover](components/crops/nav-login-hover.png) ![Log-in link pressed](components/crops/nav-login-pressed.png)

#### Nav CTA
The "💥 Get 14 days free 💥" promo button; links to /walkthrough, measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 149 x 53; background transparent; text norms 16/16 500, #ffffff `color.paper.0` |

Child layers that carry the look: span 149x40 background #0055ff `color.blue.500` border 1px solid #0055ff `color.blue.500` radius 9999px.

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

### Home

The rotating-word hero in Circuit, its translucent cards and the search box.

#### Hero title
"One app for <rotating word>" — the circuit display headline (the activity word cycles). Read as `hero-title` on the home page.

**Values (default).** size 1440 x 408; background transparent; text circuit 40/53 500, #000000 `color.ink.900`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero subcopy
The norms lede under the display headline. Read as `hero-sub` on the home page.

**Values (default).** size 514 x 48; background transparent; text norms 20/24 400, #000000 `color.ink.900`.

![Hero subcopy default](components/crops/hero-sub-default.png)

#### Hero activity card
One of the rotating activity photo cards beside the headline (the deck cycles). Read as `hero-card` on the home page.

**Values (default).** size 185 x 225; radius 25px; background rgba(0, 0, 0, 0.08) `color.black-alpha.8`; text norms 16/24 400, #000000 `color.ink.900`.

![Hero activity card default](components/crops/hero-card-default.png)

#### Page ground
The html element's own painted fill — the white ground under every section (body itself is transparent). Read as `page-ground` on the home page.

**Values (default).** size 1440 x 900; background #ffffff `color.paper.0`; text norms 36/40 500, #000000 `color.ink.900`; icon 24 x 24, #000000 `color.ink.900`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Public search

The venue search surface: comboboxes, filter pills, the dropdown panel and venue rows. Nothing was submitted.

#### Search box
The activity + location combobox pair on the public results page. Read as `search-box` on the search page.

**Values (default).** size 549 x 64; padding 12px 16px; background #ffffff `color.paper.0`; text norms 14/20 400, #000000 `color.ink.900`; icon 24 x 24, #000000 `color.ink.900`.

![Search box default](components/crops/search-box-default.png)

#### Activity field
The "Yoga, pilates, massage…" combobox field; filled with sample text then deleted, never searched. Read as `search-field` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 217.5 x 20; padding 0px 0px 0px 8px; radius 3px; background transparent; text norms 14/20 400, #000000 `color.ink.900`; placeholder #757575 `color.gray.500` |

![Activity field default](components/crops/search-field-default.png) ![Activity field focused](components/crops/search-field-focused.png) ![Activity field filled](components/crops/search-field-filled.png)

#### Location field
The "City, neighborhood" combobox, prefilled with the detected area — focused only so the prefilled value survives. Read as `search-loc` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 217.5 x 20; padding 0px 0px 0px 8px; radius 3px; background transparent; text norms 14/20 400, #000000 `color.ink.900`; placeholder #757575 `color.gray.500` |

![Location field default](components/crops/search-loc-default.png) ![Location field focused](components/crops/search-loc-focused.png)

#### Vertical pill
The "Fitness" vertical pill in the filter bar; its press opens the verticals switcher. Read as `filter-pill` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 128 x 38; padding 0px 16px 0px 0px; background transparent; text norms 14/20 500, #0055ff `color.blue.500`; icon 24 x 24, #0055ff `color.blue.500` |
| hover | child paint button.NdbE21qLuZOtwHTH6gip.TqHQqCBFnxwMo5dWH9VJ: background #f7f7f7 `color.gray.100` |
| focus-visible | child paint button.NdbE21qLuZOtwHTH6gip.TqHQqCBFnxwMo5dWH9VJ: outline 2px solid rgb(0, 85, 255) offset 0px |

Child layers that carry the look: button 112x32 background #ffffff `color.paper.0` border 1px solid #d6d6d6 `color.gray.300` radius 16px.

![Vertical pill default](components/crops/filter-pill-default.png) ![Vertical pill hover](components/crops/filter-pill-hover.png) ![Vertical pill focus-visible](components/crops/filter-pill-focus-visible.png) ![Vertical pill pressed](components/crops/filter-pill-pressed.png)

#### Filter dropdown
The "Activities" multi-select trigger; its own press opens the option panel (opened state). Read as `filter-multi` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 142 x 38; padding 0px 16px 0px 0px; background transparent; text norms 14/20 500, #000000 `color.ink.900`; icon 24 x 24, #000000 `color.ink.900` |
| hover | child paint button.NdbE21qLuZOtwHTH6gip: background #f7f7f7 `color.gray.100` |
| focus-visible | child paint button.NdbE21qLuZOtwHTH6gip: outline 2px solid rgb(0, 85, 255) offset 0px |
| opened | child paint button.NdbE21qLuZOtwHTH6gip: background #f7f7f7 `color.gray.100`; outline 2px solid rgb(0, 85, 255) offset 0px; div.efln90Mt5oP0x_l3_09w: size 380.0x349.0; background #ffffff `color.paper.0`; radius 8px; shadow rgba(0, 0, 0, 0.24) 0px 4px 12px 0px; span.xt0rRErSJCGHBs8HoZFQ: size 18.0x18.0; border 1px solid #d6d6d6 `color.gray.300`; radius 3px; span.xt0rRErSJCGHBs8HoZFQ: size 18.0x18.0; border 1px solid #d6d6d6 `color.gray.300`; radius 3px; span.xt0rRErSJCGHBs8HoZFQ: size 18.0x18.0; border 1px solid #d6d6d6 `color.gray.300`; radius 3px; span.xt0rRErSJCGHBs8HoZFQ: size 18.0x18.0; border 1px solid #d6d6d6 `color.gray.300`; radius 3px; span.xt0rRErSJCGHBs8HoZFQ: size 18.0x18.0; border 1px solid #d6d6d6 `color.gray.300`; radius 3px; span.xt0rRErSJCGHBs8HoZFQ: size 18.0x18.0; border 1px solid #d6d6d6 `color.gray.300`; radius 3px; span.xt0rRErSJCGHBs8HoZFQ: size 18.0x18.0; border 1px solid #d6d6d6 `color.gray.300`; radius 3px; span.xt0rRErSJCGHBs8HoZFQ: size 18.0x18.0; border 1px solid #d6d6d6 `color.gray.300`; radius 3px; span.xt0rRErSJCGHBs8HoZFQ: size 18.0x18.0; border 1px solid #d6d6d6 `color.gray.300`; radius 3px; span.xt0rRErSJCGHBs8HoZFQ: size 18.0x18.0; border 1px solid #d6d6d6 `color.gray.300`; radius 3px; span.xt0rRErSJCGHBs8HoZFQ: size 18.0x18.0; border 1px solid #d6d6d6 `color.gray.300`; radius 3px; span.xt0rRErSJCGHBs8HoZFQ: size 18.0x18.0; border 1px solid #d6d6d6 `color.gray.300`; radius 3px |

Child layers that carry the look: button 126x32 background #ffffff `color.paper.0` border 1px solid #d6d6d6 `color.gray.300` radius 16px.

![Filter dropdown default](components/crops/filter-multi-default.png) ![Filter dropdown hover](components/crops/filter-multi-hover.png) ![Filter dropdown focus-visible](components/crops/filter-multi-focus-visible.png) ![Filter dropdown pressed](components/crops/filter-multi-pressed.png) ![Filter dropdown opened](components/crops/filter-multi-opened.png)

#### Filter panel
The opened Activities option panel. Read as `filter-panel` on the search page.

**Values (default).** size 380 x 349; background transparent; text norms 14/20 400, #000000 `color.ink.900`.

Child layers that carry the look: div 380x349 background #ffffff `color.paper.0` radius 8px shadow rgba(0, 0, 0, 0.24) 0px 4px 12px 0px; span 18x18 border 1px solid #d6d6d6 `color.gray.300` radius 3px; span 18x18 border 1px solid #d6d6d6 `color.gray.300` radius 3px.

![Filter panel default](components/crops/filter-panel-default.png)

#### Venue card
A studio result card (photo, name, rating, distance); links to the public venue page, hovered never followed. Read as `venue-card` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 790 x 112; background transparent; text norms 12/16 700, #999999 `color.gray.400`; icon 24 x 24, #999999 `color.gray.400` |

Child layers that carry the look: div 168x112 border 1px solid rgba(0, 0, 0, 0.1) `color.black-alpha.10` radius 5px; div 0x0 background #ffffff `color.paper.0` radius 5px shadow rgba(0, 0, 0, 0.32) 0px 8px 24px 0px; div::after autoxauto border 8px solid transparent.

![Venue card default](components/crops/venue-card-default.png) ![Venue card hover](components/crops/venue-card-hover.png)

#### Star rating
The "4.8 (27500+)" star-rating row inside a venue card. Read as `venue-rating` on the search page.

**Values (default).** size 103.08 x 20; background transparent; text norms 14/20 500, #000000 `color.ink.900`; icon 12.08 x 11.06, #0055ff `color.blue.500`.

![Star rating default](components/crops/venue-rating-default.png)

#### Universal CTA
The "Get 14 days free" pill rendered with the bt--primary classes; links to /walkthrough, never followed. Read as `universal-cta` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 149 x 40; padding 12px 16px 10px 16px; border 1px solid #0055ff `color.blue.500`; radius 999px; background #0055ff `color.blue.500`; text norms 16/16 500, #ffffff `color.paper.0`; transition color 0.3s ease, background-color 0.3s ease, border-color 0.3s ease |
| hover | border 1px solid #004de6 `color.blue.600`; background #004de6 `color.blue.600`; child paint a.bt.bt--primary: background #004de6 `color.blue.600`; border 1px solid #004de6 `color.blue.600` |
| focus-visible | outline 2px solid #0055ff `color.blue.500`, offset 1px; child paint a.bt.bt--primary: outline 2px solid rgb(0, 85, 255) offset 1px |
| pressed | border 1px solid #0044cc `color.blue.700`; background #0044cc `color.blue.700`; child paint a.bt.bt--primary: background #0044cc `color.blue.700`; border 1px solid #0044cc `color.blue.700` |

![Universal CTA default](components/crops/universal-cta-default.png) ![Universal CTA hover](components/crops/universal-cta-hover.png) ![Universal CTA focus-visible](components/crops/universal-cta-focus-visible.png) ![Universal CTA pressed](components/crops/universal-cta-pressed.png)

### Plans and pricing

The public plan carousel, the price/pill card stack and the FAQ accordion.

#### Section title
The first section heading on the plans page (norms 24px). Read as `section-title` on the plans page.

Kept from an earlier run: the 2026-11-16 recapture did not find this component, so these readings may not match the current page or script.

**Values (default).** size 654 x 57.59; background transparent; text norms 24/28.8 400, #000000 `color.ink.900`.

![Section title default](components/crops/section-title-default.png)

#### Plans title
"Pick a plan that works for you" in 60px circuit. Read as `plans-h1` on the plans page.

**Values (default).** size 728 x 124.81; background transparent; text circuit 60/62.4 400, #000000 `color.ink.900`.

![Plans title default](components/crops/plans-h1-default.png)

#### Plan slide (default)
The recommended "45 credits" plan slide (the DEFAULT pill); prices render in the detected locale (SGD here). Read as `plan-slide` on the plans page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 266.66 x 148; padding 24px; radius 18px; background #ffffff `color.paper.0`; shadow rgba(1, 85, 254, 0.1) 0px 5px 16px 0px; text norms 16/24 700, #000000 `color.ink.900` |

![Plan slide (default) default](components/crops/plan-slide-default.png) ![Plan slide (default) hover](components/crops/plan-slide-hover.png)

#### Plan price
The "SGD 99 /mo" price row inside a slide. Read as `plan-price` on the plans page.

**Values (default).** size 117.41 x 36; background transparent; wrapper div.AvailablePlansCarousel_slide__mKeZE: shadow rgba(1, 85, 254, 0.1) 0px 5px 16px 0px; text norms 36/40 700, #000000 `color.ink.900`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan pill
The DEFAULT tag on the recommended slide. Read as `plan-pill` on the plans page.

**Values (default).** size 79 x 20; padding 2px 12px; background transparent; wrapper div.AvailablePlansCarousel_slide__mKeZE: shadow rgba(1, 85, 254, 0.1) 0px 5px 16px 0px; text norms 12/16 500, #000000 `color.ink.900`.

Child layers that carry the look: div::after 79pxx28px background #c0e0ff `color.blue.100` radius 14px.

![Plan pill default](components/crops/plan-pill-default.png)

#### Location selector
The detected-market pill pricing is quoted in; a locale control, never toggled. Read as `loc-selector` on the plans page.

**Values (default).** size 992 x 24; background transparent; text norms 16/24 400, #0055ff `color.blue.500`.

![Location selector default](components/crops/loc-selector-default.png)

#### FAQ question
An FAQ accordion trigger; its own press opens the answer (opened state). Read as `faq-question` on the plans page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 952 x 34; background transparent; text norms 18/18 400, #000000 `color.ink.900`; icon 18 x 18, #000000 `color.ink.900` |
| focus-visible | outline 1px auto #101010, offset 0px; child paint div: size 952.0x34.0; outline 1px auto rgb(16, 16, 16) offset 0px |

![FAQ question default](components/crops/faq-question-default.png) ![FAQ question hover](components/crops/faq-question-hover.png) ![FAQ question focus-visible](components/crops/faq-question-focus-visible.png) ![FAQ question pressed](components/crops/faq-question-pressed.png) ![FAQ question opened](components/crops/faq-question-opened.png)

#### Page CTA
A CMS call-to-action in the plans body; never followed. Read as `cms-cta` on the plans page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 327 x 50; background transparent; text norms 16/24 500, #ffffff `color.paper.0` |
| hover | child paint span.Button_button__8B4nB.Button_buttonColor-mkt-black__RenB_: background #040404 `color.ink.750`; border 1px solid #040404 `color.ink.750` |
| focus-visible | child paint a: size 327.0x16.0; outline 1px auto rgb(16, 16, 16) offset 1px |

Child layers that carry the look: span 327x50 background #111111 `color.ink.800` border 1px solid #111111 `color.ink.800` radius 9999px.

![Page CTA default](components/crops/cms-cta-default.png) ![Page CTA hover](components/crops/cms-cta-hover.png) ![Page CTA focus-visible](components/crops/cms-cta-focus-visible.png) ![Page CTA pressed](components/crops/cms-cta-pressed.png)

### Sign-in page (boundary)

classpass.com/login's public sign-in card: fields were focused and filled with placeholder text only; nothing was submitted.

#### Sign-in title
"Welcome back" on the public sign-in card. Read as `signin-title` on the sign-in page.

**Values (default).** size 400 x 32; background transparent; wrapper div.Login_loginForm__wb_4M: shadow rgba(0, 0, 0, 0.24) 0px 4px 12px 0px; text norms 28/32 500, #000000 `color.ink.900`.

![Sign-in title default](components/crops/signin-title-default.png)

#### E-mail field
The e-mail input; filled with the documented test address then deleted, Log in never pressed. Read as `signin-email` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 42; padding 8px 16px; border 1px solid #e7e7e7 `color.gray.200`; radius 4px; background #ffffff `color.paper.0`; wrapper div.Login_loginForm__wb_4M: shadow rgba(0, 0, 0, 0.24) 0px 4px 12px 0px; text norms 18/24 400, #000000 `color.ink.900`; placeholder #000000 `color.ink.900` |
| focused, filled | border 1px solid #1a5ee5 `color.blue.400`; child paint input.Login_input__jJDhI: border 1px solid #1a5ee5 `color.blue.400` |

![E-mail field default](components/crops/signin-email-default.png) ![E-mail field focused](components/crops/signin-email-focused.png) ![E-mail field filled](components/crops/signin-email-filled.png)

#### Password field
The password input; focused only, never filled. Read as `signin-pass` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 42; padding 8px 16px; border 1px solid #e7e7e7 `color.gray.200`; radius 4px; background #ffffff `color.paper.0`; wrapper div.Login_loginForm__wb_4M: shadow rgba(0, 0, 0, 0.24) 0px 4px 12px 0px; text norms 18/24 400, #000000 `color.ink.900`; placeholder #000000 `color.ink.900` |
| focused | border 1px solid #1a5ee5 `color.blue.400`; child paint input.Login_input__jJDhI: border 1px solid #1a5ee5 `color.blue.400` |

![Password field default](components/crops/signin-pass-default.png) ![Password field focused](components/crops/signin-pass-focused.png)

#### Log-in button
The primary "Log in" submit; measured in all non-submitting states, never pressed for real. Read as `signin-submit` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 48; padding 16px 0px 14px 0px; border 1px solid #0055ff `color.blue.500`; radius 9999px; background #0055ff `color.blue.500`; wrapper div.Login_loginForm__wb_4M: shadow rgba(0, 0, 0, 0.24) 0px 4px 12px 0px; text norms 16/16 500, #ffffff `color.paper.0`; transition color 0.3s ease, background-color 0.3s ease, border-color 0.3s ease |
| hover | border 1px solid #004de6 `color.blue.600`; background #004de6 `color.blue.600`; child paint button.Button_button__8B4nB.Button_buttonColor-primary__SYZoa: background #004de6 `color.blue.600`; border 1px solid #004de6 `color.blue.600` |
| focus-visible | outline 2px solid #0055ff `color.blue.500`, offset 0px; child paint button.Button_button__8B4nB.Button_buttonColor-primary__SYZoa: outline 2px solid rgb(0, 85, 255) offset 0px |
| pressed | border 1px solid #0044cc `color.blue.700`; background #0044cc `color.blue.700`; child paint button.Button_button__8B4nB.Button_buttonColor-primary__SYZoa: background #0044cc `color.blue.700`; border 1px solid #0044cc `color.blue.700` |

![Log-in button default](components/crops/signin-submit-default.png) ![Log-in button hover](components/crops/signin-submit-hover.png) ![Log-in button focus-visible](components/crops/signin-submit-focus-visible.png) ![Log-in button pressed](components/crops/signin-submit-pressed.png)

#### Apple sign-in
The "Sign in with Apple" OAuth button; never followed. Read as `signin-apple` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 400 x 48; padding 16px 0px 14px 0px; border 1px solid #d6d6d6 `color.gray.300`; radius 9999px; background #ffffff `color.paper.0`; wrapper div.Login_loginForm__wb_4M: shadow rgba(0, 0, 0, 0.24) 0px 4px 12px 0px; text norms 16/16 500, #000000 `color.ink.900`; transition color 0.3s ease, background-color 0.3s ease, border-color 0.3s ease; icon 20 x 20, #000000 `color.ink.900` |
| focus-visible | outline 2px solid #0055ff `color.blue.500`, offset 0px; child paint button.Button_button__8B4nB.Button_buttonRounded__o8JOm: outline 2px solid rgb(0, 85, 255) offset 0px |

![Apple sign-in default](components/crops/signin-apple-default.png) ![Apple sign-in hover](components/crops/signin-apple-hover.png) ![Apple sign-in focus-visible](components/crops/signin-apple-focus-visible.png) ![Apple sign-in pressed](components/crops/signin-apple-pressed.png)

#### Google sign-in
The "Sign in with Google" OAuth button; never followed. Read as `signin-google` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 400 x 48; padding 16px 0px 14px 0px; border 1px solid #d6d6d6 `color.gray.300`; radius 9999px; background #ffffff `color.paper.0`; wrapper div.Login_loginForm__wb_4M: shadow rgba(0, 0, 0, 0.24) 0px 4px 12px 0px; text norms 16/16 500, #000000 `color.ink.900`; transition color 0.3s ease, background-color 0.3s ease, border-color 0.3s ease; icon 16 x 16, #000000 `color.ink.900` |
| focus-visible | outline 2px solid #0055ff `color.blue.500`, offset 0px; child paint button.Button_button__8B4nB.Button_buttonRounded__o8JOm: outline 2px solid rgb(0, 85, 255) offset 0px |

![Google sign-in default](components/crops/signin-google-default.png) ![Google sign-in hover](components/crops/signin-google-hover.png) ![Google sign-in focus-visible](components/crops/signin-google-focus-visible.png) ![Google sign-in pressed](components/crops/signin-google-pressed.png)

#### Forgot-password link
The "Forgot your password?" link; never followed. Read as `signin-forgot` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 400 x 24; background transparent; wrapper div.Login_loginForm__wb_4M: shadow rgba(0, 0, 0, 0.24) 0px 4px 12px 0px; text norms 16/24 400, #1a5ee5 `color.blue.400`; transition background-color 0.3s ease, color 0.3s ease |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.Login_forgotPassword__W9SlG: size 400.0x24.0; outline 1px auto rgb(16, 16, 16) offset 1px |

![Forgot-password link default](components/crops/signin-forgot-default.png) ![Forgot-password link hover](components/crops/signin-forgot-hover.png) ![Forgot-password link focus-visible](components/crops/signin-forgot-focus-visible.png) ![Forgot-password link pressed](components/crops/signin-forgot-pressed.png)

### Trial onboarding (boundary)

classpass.com/walkthrough's public onboarding carousel, read but never advanced past its first step.

#### Trial title
"What your trial includes" — the first onboarding card, the entry the promo CTAs link to. Read as `walk-title` on the walkthrough page.

**Values (default).** size 547.98 x 28; background transparent; text norms 20/28 500, #000000 `color.ink.900`.

![Trial title default](components/crops/walk-title-default.png)

#### Step CTA
The black "Next" step button; measured in all non-submitting states, never pressed — pressing advances account creation. Read as `walk-cta` on the walkthrough page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 208 x 48; padding 12px 16px 10px 16px; border 1px solid #111111 `color.ink.800`; radius 9999px; background #111111 `color.ink.800`; text norms 16/24 500, #ffffff `color.paper.0`; transition color 0.3s ease, background-color 0.3s ease, border-color 0.3s ease |
| hover | border 1px solid #040404 `color.ink.750`; background #040404 `color.ink.750`; child paint button.Button_button__8B4nB.Button_buttonColor-mkt-black__RenB_: background #040404 `color.ink.750`; border 1px solid #040404 `color.ink.750` |
| focus-visible | outline 2px solid #0055ff `color.blue.500`, offset 0px; child paint button.Button_button__8B4nB.Button_buttonColor-mkt-black__RenB_: outline 2px solid rgb(0, 85, 255) offset 0px |
| pressed | border 1px solid #000000 `color.ink.900`; background #000000 `color.ink.900`; child paint button.Button_button__8B4nB.Button_buttonColor-mkt-black__RenB_: background #000000 `color.ink.900`; border 1px solid #000000 `color.ink.900` |

![Step CTA default](components/crops/walk-cta-default.png) ![Step CTA hover](components/crops/walk-cta-hover.png) ![Step CTA focus-visible](components/crops/walk-cta-focus-visible.png) ![Step CTA pressed](components/crops/walk-cta-pressed.png)

#### Benefit slide
A "What your trial includes" benefit slide (icon + heading + body). Read as `walk-slide` on the walkthrough page.

**Values (default).** size 595.98 x 676; padding 0px 24px; background transparent; text norms 20/28 500, #000000 `color.ink.900`.

![Benefit slide default](components/crops/walk-slide-default.png)

#### Step dots
The onboarding progress dots (the first is active). Read as `walk-dots` on the walkthrough page.

**Values (default).** size 40 x 24; background transparent; text norms 16/24 400, #000000 `color.ink.900`.

Child layers that carry the look: button 8x8 background #000000 `color.ink.900` radius 100%; button 8x8 background #d6d6d6 `color.gray.300` radius 100%; button 8x8 background #d6d6d6 `color.gray.300` radius 100%.

![Step dots default](components/crops/walk-dots-default.png)

### Footer

The black footer block, its link columns, social icons and app-store badges.

#### Footer
The footer band: link columns, the app-store badges, social icons, the legal subfooter. Read as `footer` on the home page.

**Values (default).** size 1440 x 581; padding 64px 100px; background #000000 `color.ink.900`; text norms 18/24 500, #ffffff `color.paper.0`; icon 24 x 24, #ffffff `color.paper.0`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 64 x 16; background transparent; text norms 16/24 400, #ffffff `color.paper.0`; transition background-color 0.3s ease, color 0.3s ease |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a: size 64.0x16.0; outline 1px auto rgb(16, 16, 16) offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A footer social icon link (Facebook). Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 28 x 12; background transparent; text norms 12/16 500, #ffffff `color.paper.0`; transition background-color 0.3s ease, color 0.3s ease; icon 28 x 28, #ffffff `color.paper.0` |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a: size 28.0x12.0; outline 1px auto rgb(16, 16, 16) offset 1px |

![Social link default](components/crops/footer-social-default.png) ![Social link hover](components/crops/footer-social-hover.png) ![Social link focus-visible](components/crops/footer-social-focus-visible.png) ![Social link pressed](components/crops/footer-social-pressed.png)

#### App-store badge
An app-store badge link in the footer; never followed. Read as `app-badge` on the home page.

Kept from an earlier run: the 2026-11-16 recapture did not find this component, so these readings may not match the current page or script.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 117 x 12; background transparent; text norms 12/12 500, #ffffff `color.paper.0`; icon 117 x 38, #ffffff `color.paper.0` |

![App-store badge default](components/crops/app-badge-default.png) ![App-store badge hover](components/crops/app-badge-hover.png)

### Mobile (390 wide)

The same surface at phone width, with its promo banner and menu overlay.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 64; background #ffffff `color.paper.0`; shadow rgba(0, 0, 0, 0.08) 0px 2px 10px 0px; text norms 36/40 500, #000000 `color.ink.900`.

![Mobile header default](components/crops/m-header-default.png)

#### Promo banner
The yellow "Get 14 days free" promo bar at this width; captured as UI, its Close never pressed. Read as `m-banner` on the home page at 390 wide.

**Values (default).** size 390 x 48; padding 8px 40px; background #fce172 `color.yellow.300`; text norms 16/24 500, #000000 `color.ink.900`; icon 24 x 24, #000000 `color.ink.900`.

![Promo banner default](components/crops/m-banner-default.png)

#### Menu button
The hamburger at the bar's right edge; its own press opens the menu overlay. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 56 x 64; background transparent; text norms 14/20 400, #000000 `color.ink.900`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The menu overlay after the toggler's own press. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 844; background #ffffff `color.paper.0`; text norms 20/28.57 400, #000000 `color.ink.900`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Menu link
A link row inside the open mobile menu. Read as `m-menu-link` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 358 x 60.56; padding 16px; background transparent; text norms 20/28.57 400, #000000 `color.ink.900`; transition background-color 0.3s ease, color 0.3s ease |
| hover, focus-visible, pressed | background #f7f7f7 `color.gray.100`; child paint a: size 358.0x60.6; background #f7f7f7 `color.gray.100` |

![Menu link default](components/crops/m-menu-link-default.png) ![Menu link hover](components/crops/m-menu-link-hover.png) ![Menu link focus-visible](components/crops/m-menu-link-focus-visible.png) ![Menu link pressed](components/crops/m-menu-link-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 390 x 119; background transparent; text circuit 30/26 500, #000000 `color.ink.900`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are ClassPass's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **The product itself.** ClassPass's booking flow, member search results and account pages are behind sign-in or a plan purchase; /login's card was measured but never submitted, and /walkthrough was captured as a boundary, never completed.
- **Anything that searches, books or signs in.** No class was searched for or booked, no form was submitted, no account was created or signed into; the Sign-in / Sign-up / Next / Book / Search actions were never followed. The search and filter controls were opened but never run.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

The marketing site paints one light theme on every captured route and declares no dark variant (the footer is a black island inside the light theme, not a theme switch).

### Fonts

- **The UI fonts** are webfonts the site declares (9 @font-face entries — norms regular/500/700, circuit, hiragino; `fonts` in [raw/css-vars.json](raw/css-vars.json)); the font files themselves are not committed.
- Photography, venue imagery and wordmark artwork in the screenshots are ClassPass's property.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The studio/venue photography, partner logos and the wordmark are ClassPass's content; only the frames and components were measured.
