# Lemni patterns

How the public pages combine the controls in [components.md](components.md). Captured signed out on 2026-11-18 at 1440 and 390.

## Marketing shell

A 50 px bar (64 px on the phone) sits over the page. Home paints it as a 40% wash of `#0d0d12`. Every other marketing page paints the bar the same `#f6f6f8` as the page. Links are Docs, Blog, Company, Community, Pricing, then Continue. Continue leaves the marketing host for `https://lemni.com/signup`, which redirects to the sign-in shell.

![Home](screenshots/home-dark-default.png)

On the phone the same links open as a full-screen dark list with a close control. The list was opened. Continue was not followed.

![Phone menu](screenshots/mobile-home-dark-menu-open.png)

The bottom of each marketing page is a link band, not a `<footer>` element: Home, Docs, Changelog, Pricing, Company, Blog, Community, Support, Brand, Privacy, Terms, and the social links.

![Home full](screenshots/home-dark-full.png)

## Dark hero

Home is the only dark page. The headline is `core.typography.display` in `#e3e8ff`. Under it, a glass black Continue pill and a glass Watch video pill. A violet decorative chip (`core.color.accent.violet`) appears in the art. It is not the button colour. Twelve elements run a 1 s `dots` transform loop. The loop does not stop under reduced motion.

![Home hero](screenshots/home-dark-default.png)

## Light inner page

Pricing, docs, blog, company, brand, changelog, support and privacy share one light ground (`light.background.page`). Headlines use TWK Lausanne 250 in black. Body and nav use the muted greys. There is no theme toggle. `prefers-color-scheme` does not flip these pages.

![Pricing](screenshots/pricing-light-default.png)

![Company](screenshots/company-light-default.png)

## Pricing

One plan column: a white card, a 46 px figure, a struck comparison in `#cacacd`, and a 340 × 40 black pill labelled Try For Free. The pill goes to sign-up. There is no public checkout form. Phone pricing stacks the same card.

![Pricing phone](screenshots/mobile-pricing-light-default.png)

## Docs

Public documentation, not the signed-in product. A horizontal section row (Basics, Knowledge, Agents, Actions, Inbox) and a left list of page names (Overview, Workplace, Members, Connections, Usage, Plans). The current section is black with a hairline. Side links are 13 px muted until hover.

![Docs](screenshots/docs-light-default.png)

![Docs phone](screenshots/mobile-docs-light-default.png)

`/docs/agents`, `/docs/knowledge`, `/docs/actions` and `/docs/inbox` are the same template. Only `/docs` was screenshotted.

## Sign-in boundary

`https://lemni.com/signin` (reached from `/signup`, `/login`, nav Continue and Try For Free) is a separate React shell on the apex host. Light ground, system-ui, a 32 px title, a Google button, an email field, and a black Continue bar at 12 px radius. The resting page was captured at 1440 and 390. Continue, Continue with Google, and any submit were not used.

![Sign-in](screenshots/signin-light-default.png)

![Sign-in phone](screenshots/mobile-signin-light-default.png)

## What is not a pattern here

Empty, loading and error states do not appear on the public pages. There is no search, no filter rail, no data table, no destructive confirm, and no onboarding outside the sign-in wall. The application form at `/company/apply` was not submitted. `community.lemni.com` returned an empty body. `app.lemni.com`, `go.lemni.com` and `dashboard.lemni.com` did not connect.
