# Lemni patterns

How the pages combine the controls in [components.md](components.md). Public marketing only, 2026-11-21, 1440 and 390. The map of controls is [site-tree.md](site-tree.md).

## Marketing shell

A 50 px bar (64 px on the phone) sits over the page. Home paints it as a 40% wash of `#0d0d12`. Every other marketing page paints the bar the same `#f6f6f8` as the page. Links are Docs, Blog, Company, Community, Pricing, then Continue. Continue leaves the marketing host for `https://lemni.com/signup`, which redirects to the sign-in shell.

![Home](screenshots/home-dark-default.png)

On the phone the same links open as a full-screen dark list with a close control. The list was opened. Continue was not followed.

![Phone menu](screenshots/mobile-home-dark-menu-open.png)

The bottom of each marketing page is a link band, not a `<footer>` element: Home, Docs, Changelog, Pricing, Company, Blog, Community, Support, Brand, Privacy, Terms, and the social links.

![Home full](screenshots/home-dark-full.png)

## Dark hero

Home and changelog paint dark. The headline is `core.typography.display` in `#e3e8ff`. Under it, a glass black Continue pill and a glass Watch video pill. Watch Video opens a YouTube embed on the same page. A violet decorative chip (`core.color.accent.violet`) appears in the art. It is not the button colour. Twelve elements run a 1 s `dots` transform loop. The loop does not stop under reduced motion.

![Home hero](screenshots/home-dark-default.png)

## Light inner page

Pricing, docs, blog, company, brand, support, privacy and terms share one light ground (`light.background.page`). Changelog uses the dark ground. Headlines use TWK Lausanne 250 in black on the light pages. Body and nav use the muted greys. There is no theme toggle. `prefers-color-scheme` does not flip these pages.

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

`https://lemni.com/signin` is where `/signup` lands. Nav Continue and Try For Free point at `/signup`. Light ground, system-ui, a 32 px title, a Google button, an empty email field, and a black Continue bar at 12 px radius. Continue with Google was not clicked. Nothing was typed. Continue was not clicked. `/login` did not load a form.

![Sign-in](screenshots/signin-light-default.png)

![Sign-in phone](screenshots/mobile-signin-light-default.png)

## Changelog

The changelog paints the same dark ground as home. It is the second dark marketing page. An email field sits on it. Nothing was typed and the form was not submitted.

![Changelog](screenshots/changelog-dark-default.png)

## What is not a pattern here

The workplace app, onboarding, empty inbox, and checkout sit behind the sign-in wall and were not entered. The application form at `/company/apply` was left empty. `community.lemni.com` failed TLS. Error and destructive confirm were not shown.
