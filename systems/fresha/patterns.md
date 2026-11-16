# Fresha patterns

How the measured components combine into the real pages. Values are the measured ones in [components.md](components.md) and [raw/measurements.md](raw/measurements.md); tokens in [tokens.json](tokens.json). The screenshots under [screenshots/](screenshots) show each pattern in place.

## Site chrome

Every www.fresha.com consumer page carries the same 72px header (measured `shell-header` 1440x72): the lowercase "fresha" wordmark left, then Log in and For business links, a bordered "Menu ≡" pill that opens the menu drawer (`home-light-menu`), and a black "Get the app" pill on the right. The header stays transparent-over-content at the top of the home page. On /for-business and /pricing the same shell carries the B2B nav: a "Business types" button that opens a 588x391 flyout of business-category links (`for-business-light-flyout`), plus Solutions, Pricing, Contact sales and the black "Try for free" / "Get a demo" CTAs — 48px-tall black pills. At 390px the header compresses to a sticky bar with the wordmark, the search pill and an icon "Menu" button (`m-header`, `m-menu-button`).

## The marketplace hero and search

The consumer home opens on a full-bleed display hero: a giant Roobert heading ("Book beauty and wellness appointments" style), then the signature **search pill** — a single white rounded bar split into three fields: "Hair Salon" (treatment), "Current location" and "Any time", closed by a round black search button (measured `search-treatment-field`, `search-location-field`, `search-when-control`, `search-button`). Focus in the treatment field drops a suggestions popover (`home-light-search-focus`, `search-suggestions`). Below the hero, marketing bands alternate recommended-venue card carousels (`venue-card` 322x285 with a photo block, name, 5.0 rating badge, area and category), category chips, an app-promo band and the fat link footer.

## Venue and booking

A venue profile (`/a/<slug>`) stacks: breadcrumb, a photo gallery with its own arrow buttons (`gallery-button`), the venue title with tabs (Services, Reviews, About — `venue-tab`), then a two-column layout: service rows on the left (each with its own black "Book" pill — `service-row`, `service-book-button`) and a sticky summary column on the right. The services section scrolls to reveal the full list (`venue-light-services`). Reviews carry a big score block (`review-score`), per-reviewer cards (`review-card`) and a staff avatar row (`staff-avatar`); an opening-hours table (`hours-table`) sits in the About column.

Choosing a service enters the booking wizard at `/booking` — the signed-out boundary: a step header ("Choose services" — `booking-header`, `booking-step`), category pills (`booking-category-pill`), service rows with their own Add checkboxes (`booking-add-button`) and a 444x756 white cart summary (`booking-cart`) with a Continue button that was never pressed. One service was ticked for the capture then unticked (`booking-light-ticked`); nothing was booked and no payment step was reached.

## Sign-in shells

`/user-flow` is the customer-or-business chooser: a back button, a chooser card and a language button. `/auth` is the consumer sign-in: the 374x46 email field on a 12px radius ("We'll send you a verification code" — typed into, shown filled, then cleared; `auth-light-filled`), a black Continue pill, an SSO row (Google / Facebook / Apple), a passkey button and cross-links. partners.fresha.com's professional sign-in shares the anatomy on a centered card (394x46 field, Continue, SSO) and is the one place a second theme paints: it sets `data-theme="auto"`, so under `prefers-color-scheme: dark` the page inverts to the dark palette (`partner-signin-dark-default`). Nothing was submitted; no OAuth, SSO or passkey flow was started.

## B2B marketing and pricing

`/for-business` and `/pricing` share the marketing anatomy: a display hero with a black CTA pair (Get a demo, a "watch film" outline button), a grid of square business-type tiles (`business-type-card` 379x379), a stat row and the FAQ. `/pricing` lays four plan cards (`plan-card` 277x368.5) with price blocks (`plan-price`), CTAs (`plan-cta`) and a feature row list (`feature-row`) with small info icons (`info-icon`); the FAQ is a disclosure list — one item was opened for `pricing-light-faq-open`.

## The legacy LP microsite

`/lp/en/bt/*` is Fresha's older marketplace front-end — a separate stylesheet with literal values (no token vars): an LP header with its own search strip, a category hero ("Find Hair Salons near me"), a city chip rail (`lp-category-chip`), then on browse pages venue cards (`lp-venue-card` 381x543 with photo, rating count, category and "from S$" price line — `lp-price`), a "Show on map" button (`lp-map-button`) and pagination (`lp-pagination`). The category hub `/lp/en/bt/hair-salons` and the Singapore browse page were both captured, desktop and 390.

## Help, careers, app

`/help-center` leads with a 654x60 search pill (`help-search`, focused only) over topic tiles (`topic-card`) and article rows (`article-link`). `/careers`, `/blog` and `/download-app` share the B2B chrome; `/cookies` is a prose page on the consumer shell.

## Themes

One painted theme per surface: **light** everywhere except the partner sign-in, where `data-theme="auto"` honours the OS and paints **dark**. A third scope, `[data-theme=accent]` (violet), is declared in the partner and B2B sheets for tinted sections but no signed-out element was observed carrying it. The consumer and B2B sheets also declare dark values that nothing signed out switches to — all kept in tokens.json as declared evidence.

## Motion and focus

The Panda system declares `durations.*` (.1s–1s) and `easings.*` (five cubic-beziers); measured transitions sit at 0.18–0.2s on colour/transform (search pill, buttons, flyout). prefers-reduced-motion is only partially honoured: home, venue and LP reduce some motion; pricing, for-business, help, auth and partner ignore it ([raw/motion.json](raw/motion.json)). Keyboard focus paints a ring two ways: most Panda controls fade in a `::before` pill shadow (white 2px + near-black 4px, opacity 0 to 1) while their 2px outline stays transparent; the LP map button shows a solid 2px outline instead (see the Focus line in components.md). Pressed states were forced via `CSS.forcePseudoState`; the solid CTAs shrink ~4% rather than recolour.
