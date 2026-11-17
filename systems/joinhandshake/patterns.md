# Handshake patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## The marketing shell (light only)

Every joinhandshake.com page is a document-scrolling marketing page under a floating pill nav. The nav is a `nav.fixed` strip parked `--desktop-nav-top-offset` (24px) below the viewport top, 1440 x 56 (`hs-nav`, `layout.desktopNavHeight` 3.5rem): a centered `rounded-2xl` inner pill carrying the wordmark, the section items (`hs-nav-link`, 95 x 44, 14px), a "Sign up" button and a "Log in" link in the right rail. At rest over the hero the bar is transparent and its items paint white — `light.bg.nav` is `rgba(0,0,0,0)`, `light.fg.navLink` #ffffff — the ink-on-white treatment only appears once the page scrolls under it. Hovering a section item opens a mega menu panel under the bar (`home-light-nav-open`); the menu is opened by hover alone and closed by moving the pointer off, never by a click through.

The "Sign up" control is the site's signature element: a 80 x 40 lime pill (`hs-signup-button`, `light.button.primary.bg` #d3fb52, `light.button.primary.fg` #14151c ink, 14px medium) that darkens to #a1dd3b (`light.button.primary.hover`) on hover. "Log in" is a 74 x 40 white-text ghost (`hs-login-link`) beside it. Every page closes with the ink footer (`hs-footer`, `light.bg.footer` #14151c, `light.link.footer` #ffffff) — a rounded-top band of link columns.

## The homepage hero: headline + job-search form

The hero stacks an uppercase brand-face h1 — "LET'S FIND YOUR NEXT JOB", SansPlomb semibold (`hs-hero-h1`, 160px/128px at desktop; the 86px/68.8px copy is the one that paints at 1024 and 390) — over the job-search form (`hs-search-form`, a 920 x 88 `rounded-3xl` field row, `--content-max-width`-bounded). A rounded "Search jobs" submit sits inside the field's right end (`hs-search-button`, 56 x 56), and the type pills Full-time / Remote / Internship (`hs-filter-pill`, 14px) sit beneath. The form was measured at rest only: nothing was typed and it was never submitted (it would navigate into the app).

## Section bands and the 12-column grid

Page sections ride a 12-column grid — at 1440 the columns measure 116px each (`raw/layout.json` `grids`) inside `--container-*` clamps, with `--content-max-width` ~1140px for the article measure. Long index pages alternate their bands between `bg-neutral-0` white (#ffffff) and `bg-neutral-10` (#f3f4fa) — measured on /blog/ as painted `section` backgrounds — so cards and copy are grouped by fill, not by rules. Hero and marketing sections paint over the ink or a Framer `--token-*` accent field instead.

## The employers page: switcher, testimonials, FAQ

/employers/ opens with the same floating nav plus a dismissible notification band (height `--notification-banner-height`, dismissed locally by its own "Dismiss notification" button — captured open on the mobile homepage, absent once dismissed). The body pattern is a segmented feature switcher: Source / Automate / Brand / Measure tabs (`hs-segment-tab`, 120 x 44, selection carried by opacity) where a tab's own press swaps the published panel (`employers-light-tab-automate`). CTA pills (`hs-cta`, 120 x 40, 16px medium — a ghost treatment that inverts to white-on-ink on hover) and testimonial carousel dots (`hs-carousel-dot`, 8 x 8) fill out the page, closed by a FAQ accordion whose question buttons unfold answers (`employers-light-faq-open`, `pricing-light-faq-open`).

## Pricing tables and Marketo lead forms

/employers/pricing/ carries the plan comparison as a real `table` — `pricing-table` measures 1152 x 856 of `th`/`td` rows — under the feature-group tabs. The lead forms on /employers/request-more-info/ (502 x 466 card, `mkto-form`) and /career-centers/contact/ (728 x 921, `cc-form`) are Marketo's vendor stack mounted on publish: labelled fields and a submit, measured at rest. Nothing was typed, focused-submitted or sent — `mkto-select` was never found because Marketo renders its picklists as scripted dropdowns, not `<select>` elements.

## Students, careers, blog

/students/ pairs the same sign-up CTA (`stu-signup-button`, lime pill) with arrow-suffixed text links ("Find jobs and internships →", `stu-text-link`, `light.link.accent`) and a card carousel. /careers/ lists open roles behind a search field (`car-search-input`, 688 x 56), the departments filter dropdown (`car-dept-button`, 218 x 56, opened by its own press) and pagination. /blog/ is a searchable index: a 343 x 27 search field at 22px (`blog-search-input`), an 89 x 48 "Search" button (`blog-search-button`), uppercase 16px/600 category links (`blog-category-link`), then article cards (`blog-card`) down the alternating neutral bands.

## Legal pages

The legal sections (/legal/tos/, /privacy-policy/) keep a left rail of section links (`legal-nav-link`, 305 x 22, 16px at reduced opacity) with the current section painted at full weight/opacity (`legal-nav-active`, `light.nav.legalActive` #252630).

## The consumer app's access card

app.joinhandshake.com/access is a different product skin entirely — the Rosetta design layer served from handshake-production-cdn.joinhandshake.com. The "Log in or sign up" card carries a locale select (`app-locale-select`, a `rosetta-select` over a hidden native `<select>`), the "Enter your email" field (`app-email-field`), the full-width "Continue with email" `rosetta-button` (`app-continue-button`, 344 x 40, 15px/500 on `access.rosettaInteractive.*`), Google's GSI button as vendor furniture, then the "Sign up as an employer" link (`app-employer-link`, 15px) and the Terms/Privacy fine print (`app-tos-link`, 13px). The page paints `access.rosettaBg.primary` #ffffff with `access.rosettaFg.primary` #121212 ink.

## Mobile (390px)

At 390 the nav collapses to a 358 x 48 floating pill (`m-hs-topbar`, 16px inset, top offset 24px): wordmark, the compressed links and an icon-only "Open menu" button (`m-hs-hamburger`, 24 x 16). Its press opens a full-bleed sheet under the bar — `m-hs-drawer`, 390 x 772 fixed from y=72, carrying the section links and the right-rail CTAs (`mobile-home-light-drawer`). The hero form and sections reflow to the single column; the same light paint holds.

## Motion and focus

Transitions are Tailwind's `--default-transition-duration` 150ms on the `--ease-*` curves, with `--animate-pulse`/`--animate-spin` reserved for loading and skeleton states (`core.duration.default` 150ms). Nav items and CTA pills do a fast colour/inversion swap; the mega menu and the mobile sheet are instant panels. Focus-visible is a plain outline ring (measured on `hs-nav-link`, `hs-footer-link`, `stu-text-link`). The motion probe's honest caveat: **prefers-reduced-motion is ignored on every probed page** — all seven marketing routes kept their animations running under the emulated reduced-motion flag (`raw/motion.json`).

## The boundary beyond the marketing site

This package documents joinhandshake.com's signed-out pages and the consumer app's access card — nothing signed-in. app.joinhandshake.com/explore, /signup and the student registration flow never cleared the Cloudflare managed challenge (fresh-context retries across every run), and support.joinhandshake.com answered Cloudflare 403. /access and /login clear intermittently and were captured on the loads that did. Those surfaces are named here as blocked boundaries — no pixel, token or component in this package claims to describe them.
