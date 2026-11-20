# FlowMapp patterns

How the measured components combine into the real pages. Values are the measured ones in [components.md](components.md) and [raw/measurements.md](raw/measurements.md); tokens in [tokens.json](tokens.json). The screenshots under [screenshots/](screenshots) show each pattern in place.

## Site chrome

Every marketing page carries a floating white top bar (~70px inside an 82px header, white at 80% over a soft `rgba(120,124,132,0.19)` shadow, 12px radius): the FlowMapp wordmark left, then "Try Demo Project" (a header link to the published read-only demo on app.flowmapp.com — measured, never followed), the **Features** trigger which opens the `.nav__pop` flyout (a 377x490 white panel of icon+name+description rows for Sitemap, User flow, Wireframes, Content, Estimation & invoice — captured open on `home-light-features-menu`), Use cases, Pricing, Help and Blog links, then a plain "Log in" (bordered ghost that inverts to black-on-hover) and the black "Try for free" 12px-radius pill (which inverts to a light-steel-bordered ghost on hover). Nav links sit on an 8px radius and tint to `--bg` #f6f8fa on hover. At 390px the links collapse behind a burger that opens a white overlay menu (`mobile-home-light-menu`).

## The hero

A centered masthead pattern on `home-light-default`: the "Over 400,000 users" trust eyebrow with stacked user avatars, a 72px/700 Inter heading ("Visual platform for planning UX and pitching web design"), then the signature **dodger-blue pill** — a 1600px-radius `#0080ff` button wrapped in a translucent `rgba(0,128,255,0.2)` halo (the `--dodger-blue-20` ring painted as a border/shadow). Beneath, a row of trusted-by marks (Google, Adobe, Deloitte, Wix… greyscale wordmarks). Section grammar repeats: a white eyebrow tag, a mid-size heading, muted standfirst, then the section's grid of `home-card` tiles on the `--bg` #f6f8fa field.

## Pricing

`/pricing` pairs a white pill **billing switcher** (Monthly / "Annual (45% off)", the active side painting a white button over the `#f6f8fa` track at a 25.6px radius — captured with the monthly tab active on `pricing-light-billed-monthly`) with four plan cards on 24px-radius white surfaces: Free ($0), Pro ($15/$8.25), **Team** — the featured card inverted to solid black with the same dodger-blue pill CTA — and Agency ($99). Plan features render as `plan-row` rows; the FAQ is a `faq-q`/`faq-a` disclosure list (captured opened on `pricing-light-faq-open`).

## Feature and content pages

`/features/sitemap`, `/features/userflow`, `/features/wireframes` and the use-case pages repeat one anatomy: a 96px/700 display heading, a lede, the same dodger-blue CTA pill, then `feat-card` tiles and prose blocks. `/blog` lists article cards; `/reviews` lists testimonial tiles; `/contact-us` is a centered white form card (name/email/message fields, a submit button — measured and typed into then cleared, never submitted). `/security`, `/privacy`, `/terms` are long-form prose pages on the same chrome.

## Signed-out app forms

`app.flowmapp.com` paints its own palette (`--primary-basic-blue` #0050ff on the `--neutral-gray-*` field). `/signin`, `/signup` and `/restore` share one anatomy: the FlowMapp mark, a heading ("Log In"), a sub-line, 374x56 `#f5f5f5` fields on 16px radii, a full-width submit and a Google SSO button. The sign-in submit sits **disabled** on #9fb8f9 until both fields validate, then paints the primary blue — both fills were measured, and the button was never clicked. The contact form follows the same field grammar.

## Shared demo project

`app.flowmapp.com/share/projects/215285` is the product's own read-only surface, linked from the marketing header: a dark floating toolbar (menu, page dropdown, zoom controls — `sh-toolbar-btn` at 12px radius), the sitemap canvas tiling `sh-card` page cards (95px-wide white cards, 2px `#1f1f1f` border, 16px radius) connected by `sh-blocks` flow lines, Structure/Estimation tabs, "Log In"/"Sign Up" pills, and a `rgba(0,0,0,0.56)` toast popup ("Hi, Log In or Sign Up to start planning amazing websites!") at 14px radius. The user-flow viewer shares the chrome with `uf-card` flow tiles and `uf-tag` colour-coded tags. Card geometry was measured at the viewer's captured 60% zoom — real px at that zoom, not a canonical size.

## Mobile

At 390px the nav collapses to a burger (white overlay menu on `mobile-home-light-menu`), the masthead drops to ~40px, plan cards stack single-column and the share viewer keeps its toolbar + canvas (mobile sitemap shot captured). The mobile login pass hit an app-domain anti-bot challenge — recorded as a gap, not bypassed.

## Motion and focus

Controls carry a measured `0.3s ease` transition on background-color/color/border-color (nav links, CTAs, tabs). Focus-visible paints the UAG outline where styled — the per-component focus rows in [components.md](components.md) record which rings paint where; `pressed` states were forced via `CSS.forcePseudoState` so script-driven mousedown looks are uncaptured. `prefers-reduced-motion` results are recorded in `raw/components-computed.json` `_meta.reducedMotion`.
