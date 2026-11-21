# Polar public site tree

Mapped from https://polar.sh/ on 2026-11-21, signed out. The homepage returned 200. The title was "Polar — A billing platform for the intelligence era | Polar". This is a live marketing site, not a parked domain.

Marketing pages paint dark (`html` class `antialiased dark`). Docs at https://polar.sh/docs/introduction paint light until the theme control is used. `/signup` redirects to https://polar.sh/auth. `/login` and `/pricing` are 404s. Pricing lives at https://polar.sh/resources/pricing.

No email was typed. No password was typed. No code was typed. No form was submitted. Google, Apple and GitHub were not clicked. No checkout was started.

T3 `preview_snapshot` failed twice with "The browser is not producing screenshot frames." The tree and the shots were taken with headless Playwright after that.

## Header (desktop, 1440)

The wordmark and four labels sit in the bar. Features and Docs are hover menus. Blog and Company are links. Sign in and Get Started are buttons.

| Control | Opens | Stop? |
|---|---|---|
| Polar (wordmark) | `/` | |
| Features | A panel on the same page: Usage Billing, Subscriptions, Merchant of Record, Seats, Credits, Trials, Discounts, Cost Insights, Finance | Photographed open, then left |
| Docs | A panel on the same page: Integrate, Documentation, API, SDK, MCP, Framework Adapters, Products & Subscriptions, Checkouts, Usage Billing, Benefits, Finance & Payouts | Photographed open, then left |
| Blog | `/blog` | |
| Company | `/company` | |
| Sign in | A dialog on the same page: Google, Apple, GitHub, an empty email field, Sign in with email | Stop. Empty dialog only. Escape closes it. Identity providers were not clicked |
| Get Started | Same empty wall as Sign in (the footer "Get Started" is a link to `/signup`, which redirects to `/auth`) | Stop. Empty wall only |

## Homepage

The page is one long dark page. There is no dialog on load. The dashboard in the hero is a painted demo (Acme Inc, `joe@acme.com`, Visa ending 4242). Those strings are the site's own copy.

| Control | Opens | Stop? |
|---|---|---|
| Get Started (hero) | The same empty sign-in wall | Stop. Not followed into an account |
| Feature links under the hero | `/features/event-ingestion`, `/features/meters`, `/features/usage-billing`, `/features/credits`, `/features/cost-insights` | |
| Feature cards | `/features/usage-billing`, `/features/subscriptions`, `/features/merchant-of-record`, `/features/seats`, `/features/credits`, `/features/trials`, `/features/discounts`, `/features/cost-insights`, `/features/finance` | |
| Benefits card | `/docs/features/benefits` | |
| Read the Stilla AI story | `/customers/stilla-ai` | |
| Explore integrations | `/integrate` | |
| Read the field guide | `/field-guide` | |
| Request early access | `/field-guide` | Stop. The request form was not filled |
| Quote links | `https://x.com/...` | Off-site. Not opened |
| Contact Sales | `mailto:support@polar.sh` | Not opened |
| Apply now | `/startup-program` | The apply form was not filled and not submitted |
| Cookie Preferences | Footer link. Not opened as a settings change | |

## Mobile drawer (390)

The labels collapse. A button labelled "Toggle Sidebar" at the right of the bar opens a drawer.

| Control | Opens | Stop? |
|---|---|---|
| Overview | `/` | |
| Integrate | `/integrate` | |
| Documentation | `/docs` | |
| Pricing | `/resources/pricing` | |
| Blog | `/blog` | |
| Company | `/company` | |
| Open Source | `https://github.com/polarsource` | Off-site. Not opened |
| Polar on X | `https://x.com/polar_sh` | Off-site. Not opened |
| Login | The empty sign-in wall | Stop. Not followed |

## Docs

`/docs` redirects to `/docs/introduction`. The shell is Mintlify. The top row and the side list are links.

| Control | Opens |
|---|---|
| Documentation | `/docs/introduction` |
| Developer Resources | A docs section |
| API Reference | `/docs/api-reference` |
| Changelog | Docs changelog |
| Support | Docs support |
| Search | A search control labelled "Search... ⌘K". Nothing was typed |
| Theme | Switch to system theme, Switch to light theme, Switch to dark theme. Dark was opened, then light was restored |
| Dashboard (docs footer) | Not followed. It points at the signed-in app |

## Pricing

`/resources/pricing` is a public document. Sections are Introduction, Plans, Early Member, Additional Fees, Example, Dispute/Chargeback Fees. No checkout button was followed. `/pricing` is a 404.

## Footer

| Group | Items |
|---|---|
| Features | Usage Billing, Subscriptions, Seats, Credits, Trials, Discounts, Cost Insights, Finance, Merchant of Record |
| Resources | Integrate, Why Polar, Merchant of Record, Pricing, Downloads |
| Company | About Polar (`/company`), GitHub, X / Twitter, Brand Assets |
| Legal | Cookie Preferences |
| Support | Docs, Contact, Service Status |

GitHub, X and Service Status were not opened. Contact is a mailto and was not opened.

## Auth wall

| URL | Lands on | What it shows |
|---|---|---|
| `/signup` | `/auth` | Welcome to Polar. Google, Apple, GitHub, empty Email, Sign in with email |
| `/auth` | `/auth` | The same empty wall |
| `/login` | `/login` | 404, "We can't find the page you're looking for." |

The email field was empty. Sign in with email was not clicked. Identity providers were not clicked.
