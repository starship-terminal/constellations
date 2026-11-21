# GlossGenius patterns

How the measured components combine into the real pages. Values are the measured ones in [components.md](components.md) and [raw/measurements.md](raw/measurements.md); tokens in [tokens.json](tokens.json). The screenshots under [screenshots/](screenshots) show each pattern in place.

## Site chrome

Every marketing page carries the `.header_new` top bar: the serif GlossGenius wordmark left, then the **How it works** trigger which opens the feature mega-menu — a Webflow `w-dropdown` holding a category tab rail (Agents, Booking & Scheduling, Marketing & CRM, Payments & POS, Staff & Business, EMR) with icon+link rows — then **Businesses** (a second dropdown: Beauty, Wellness, Medspa, Health, Fitness), **Pricing** and **Resources** (About, Get a demo, Blog, Learning Center, Contact Support, Careers, Free Data Transfer), then a plain "Log in" (to app.glossgenius.com/login, photographed empty, never submitted), the dark "Book a demo" pill and "Start free trial". A fixed `.gg-support-btn` chat bubble pins to the corner of every page. At 390px the links collapse behind a burger that opens the mobile menu (`mobile-home-light-menu`). The control map is [site-tree.md](site-tree.md).

## The hero

A centered masthead pattern on `home-light-default`: an eyebrow line, the display heading ("Scheduling, payments, and admin. Handled."), a muted standfirst, then the CTA pills — "Start free trial" and "Get a demo" on fully-round radii. Section grammar repeats down the page: an eyebrow tag, a section heading, muted lede, then a grid of cards or a product mock on the gloss-white field.

## Pricing

`/pricing` pairs a Monthly/Annual **billing switch** (a checkbox-backed `.toggle_new`, "save up to 14%" — the page loads annual-checked; the click selects Monthly, captured on `pricing-light-monthly`) with a **plan-tier picker** (the Beauty & Wellness / Medspa & Aesthetics `.dropdown_new--pricing-tiers`, captured open on `pricing-light-tiers-menu` — options measured, never activated). Plan cards sit on white rounded surfaces; the "Most popular" **Gold** card carries an amber tag. Below, the compare table navigates plans via `.pricing-table-nav__plan` chips and the FAQ is a native `<details>/<summary>` `accordion-item` list (captured opened on `pricing-light-faq-open`).

## Feature, audience and content pages

`/online-booking`, `/payment-processing`, `/ai-business-tools`, the `/for-*` audience pages and `/customers/*` repeat one anatomy: a display heading, a lede, the same CTA pills, then card tiles, product mocks and testimonial blocks. `/about` is brand prose; `/blog` lists article cards and one article was captured; `/legal/privacy` is long-form prose on the same chrome. `/contact-us` is a help-options page; `/get-demo` and `/free-trial` are the signup-intent forms.

## The demo form

`/get-demo` is a two-step Webflow form inside a `.card-main` card: step 1 (`#email-form`) is the "How big is your team?" `label.radio_new` pills (Just me / 2-4 / 5-9 / 10+) plus a "Get a demo" link that reveals step 2. Step 1 was photographed. No radio was chosen. Step 2 was not opened and was not typed into. Submit was not pressed.

## Signed-out app forms

`app.glossgenius.com` paints the glossDS layer (`--content-primary` ink, `--surface-*` fields, 1000px `--button-*-radius` pills). `/login`, `/signup` and `/forgot-password` share one anatomy: the GlossGenius mark, a heading ("Welcome back!" / "Let's get started" / "Password recovery"), empty fields, then a full-width primary submit. The fields were photographed empty. Nothing was typed. The submits were measured at rest and on hover, focus and forced press, and were never clicked. There is no identity-provider button on these walls. The signed-in app was not entered. The empty-wall record is [login-review.json](login-review.json).

## The published booking site

The published booking site captured here is bookings.glossgenius.com. Its own token family (`--button-*`, `--text-*`, `--space-*`, `--chip-*`, `--input-*` under `.tokens_glossDS__*` classes) paints a business nav (Services, About, Team, Shop, Contact, Book Now) and a service list with a **Select a Professional** menu (opened on `book-services-light-pro-menu`, no option chosen). Select on a service row was not clicked. The BOOK bar stayed at BOOK 0 SERVICE and was not pressed. `/booking-flow` was photographed with both selects closed (`book-flow-light-default`). Choosing a professional or a category starts a booking, so the calendar, time slots, details and payment were not reached.

## Mobile

At 390px the nav collapses to a burger (the menu captured on `mobile-home-light-menu`), the masthead drops a step, and the booking site's service list and the empty signup wall hold their single-column flow. Mobile passes covered home, signup and the booking services list. A phone pricing pass was not recaptured on 2026-11-21.

## Motion and focus

Controls carry a measured transition on color/background/border (nav links, pills, accordion rows); the declared transitions are listed in `raw/measurements.md`. Focus-visible paints a ring where styled — the per-component focus rows in [components.md](components.md) record which rings paint where; `pressed` states were forced via `CSS.forcePseudoState` so script-driven mousedown looks are uncaptured. `prefers-reduced-motion` results are recorded in `raw/components-computed.json` `_meta.reducedMotion`.
