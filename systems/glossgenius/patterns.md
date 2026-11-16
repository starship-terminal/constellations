# GlossGenius patterns

How the measured components combine into the real pages. Values are the measured ones in [components.md](components.md) and [raw/measurements.md](raw/measurements.md); tokens in [tokens.json](tokens.json). The screenshots under [screenshots/](screenshots) show each pattern in place.

## Site chrome

Every marketing page carries the `.header_new` top bar: the serif GlossGenius wordmark left, then the **How it works** trigger which opens the feature mega-menu — a Webflow `w-dropdown` holding a category tab rail (Agents, Booking & Scheduling, Marketing & CRM, Payments & POS, Staff & Business, EMR) with icon+link rows — then **Businesses** (a second dropdown: Beauty, Wellness, Medspa, Health, Fitness), **Pricing** and **Resources**, then a plain "Log in" (to app.glossgenius.com — measured, never followed), the dark "Book a demo" pill and "Start free trial". A fixed `.gg-support-btn` chat bubble pins to the corner of every page — measured, never opened. At 390px the links collapse behind a burger that opens the mobile menu (`mobile-home-light-menu`).

## The hero

A centered masthead pattern on `home-light-default`: an eyebrow line, the display heading ("Scheduling, payments, and admin. Handled."), a muted standfirst, then the CTA pills — "Start free trial" and "Get a demo" on fully-round radii. Section grammar repeats down the page: an eyebrow tag, a section heading, muted lede, then a grid of cards or a product mock on the gloss-white field.

## Pricing

`/pricing` pairs a Monthly/Annual **billing switch** (a checkbox-backed `.toggle_new`, "save up to 14%" — the page loads annual-checked; the click selects Monthly, captured on `pricing-light-monthly`) with a **plan-tier picker** (the Beauty & Wellness / Medspa & Aesthetics `.dropdown_new--pricing-tiers`, captured open on `pricing-light-tiers-menu` — options measured, never activated). Plan cards sit on white rounded surfaces; the "Most popular" **Gold** card carries an amber tag. Below, the compare table navigates plans via `.pricing-table-nav__plan` chips and the FAQ is a native `<details>/<summary>` `accordion-item` list (captured opened on `pricing-light-faq-open`).

## Feature, audience and content pages

`/online-booking`, `/payment-processing`, `/ai-business-tools`, the `/for-*` audience pages and `/customers/*` repeat one anatomy: a display heading, a lede, the same CTA pills, then card tiles, product mocks and testimonial blocks. `/about` is brand prose; `/blog` lists article cards and one article was captured; `/legal/privacy` is long-form prose on the same chrome. `/contact-us` is a help-options page; `/get-demo` and `/free-trial` are the signup-intent forms.

## The demo form

`/get-demo` is a two-step Webflow form inside a `.card-main` card: step 1 (`#email-form`) is the "How big is your team?" `label.radio_new` pills (Just me / 2-4 / 5-9 / 10+) plus a "Get a demo" link that reveals step 2 (`form.form-new` inside `.get-demo-form-step-2`, display:none until the link runs) — `.input_new` text, e-mail and telephone fields, native `.input_new--select` dropdowns and a "Submit". The step link was measured, never activated; step 2's fields were read with the wrapper unhidden — focused and typed into then cleared; the submit was measured in every state, never pressed.

## Signed-out app forms

`app.glossgenius.com` paints the glossDS layer (`--content-primary` ink, `--surface-*` fields, 1000px `--button-*-radius` pills). `/login`, `/signup` and `/forgot-password` share one anatomy: the GlossGenius mark, a heading ("Welcome back!" / "Let's get started" / "Password recovery"), BaseInput fields (e-mail, password, name, phone), a professional-confirmation checkbox and "Add Promo Code" on signup, then a full-width primary submit. The submits were measured at rest and on hover/focus/forced-press — never clicked. The app root redirects to `/calendar` behind sign-in and was excluded as a boundary.

## The published booking site

Every GlossGenius business gets a public booking website at `<name>.glossgenius.com`; honeyhivesalon.glossgenius.com stands in for the surface. Its own token family (`--button-*`, `--text-*`, `--space-*`, `--chip-*`, `--input-*` under `.tokens_glossDS__*` classes, re-skinned per layout variant) paints: a business nav (About, Our Team, Services, Portfolio, Shop, Contact, BOOK NOW), the service list with a **"Select a Professional"** react-select (captured open on `book-services-light-pro-menu` — the `.gg-dropdown__menu` lists the business's pros, never chosen), service cards each with a **Select** button that marks it (the header becomes "BOOK 1 SERVICE" — `book-services-light-selected`), and the BOOK bar leading to `/book`. The date-picker step runs a SELECT SERVICE / DATE & TIME / YOUR DETAILS stepper over a month calendar with time slots and a "Next" button — browsed read-only (`book-services-light-book-calendar`, `-book-slots`); no slot was confirmed, Next never pressed, the details form never reached.

## Mobile

At 390px the nav collapses to a burger (the menu captured on `mobile-home-light-menu`), the masthead drops a step, plan cards stack single-column, and the booking site's service list and signup form hold their single-column flow. Mobile passes covered home, pricing, signup and the booking services list.

## Motion and focus

Controls carry a measured transition on color/background/border (nav links, pills, accordion rows); the declared transitions are listed in `raw/measurements.md`. Focus-visible paints a ring where styled — the per-component focus rows in [components.md](components.md) record which rings paint where; `pressed` states were forced via `CSS.forcePseudoState` so script-driven mousedown looks are uncaptured. `prefers-reduced-motion` results are recorded in `raw/components-computed.json` `_meta.reducedMotion`.
