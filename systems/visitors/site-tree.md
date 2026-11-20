# Visitors site tree

Mapped on 2026-11-21 from https://visitors.now/ in the T3 preview, signed out. A control is listed with the page or interaction it opens. Routes that were not opened are marked not visited.

The browser stopped producing screenshot frames after the homepage scroll. Later routes were read as link lists on `/docs` and `/blog` before that stop, or as `fetch` status codes. They were not screenshotted.

## Homepage controls

| Control | Opens |
|---|---|
| Wordmark | `/` |
| Features | Menu, not a page. Four cards: Revenue (`/revenue-attribution`), Realtime (`/realtime`), Performance (`/performance`), Profiles (`/profiles`) |
| Pricing | `/#pricing` |
| Blog | `/blog` |
| Docs | `/docs` |
| Login | `/login` |
| Register | `/register` (account creation; not opened) |
| NEW / We hit $1K MRR | `/blog/1k-mrr` |
| Start 14 day free trial | `/register` |
| See demo | `/s/godly.website` |
| Logo strip | External: godly.website, endless.design, templedigitalgroup.com, inbound.new, fleet.ai, buildkite.com |
| Dashboard, Profiles, Funnels, Performance, Realtime | In-page demo tabs on the hero. They swap the marketing image. They do not open the app |
| Learn more (revenue) | `/revenue-attribution` |
| Learn more (realtime) | `/realtime` |
| Learn more (profiles) | `/profiles` |
| Learn more (performance) | `/performance` |
| Monthly / Yearly | In-page billing toggle on `#pricing`. Not submitted |
| FAQ rows | In-page expand. Questions were closed when mapped |
| Footer Home, Login, Register, Docs | `/`, `/login`, `/register`, `/docs` |
| Footer Revenue, Realtime, Performance, Profiles | The four feature pages |
| Footer Google Analytics, Plausible, Fathom | `/vs-google-analytics`, `/vs-plausible`, `/vs-fathom` |
| Footer Contact, Blog | `/contact`, `/blog` |
| Footer GDPR, Data policy, DPA, Privacy, Terms | `/gdpr`, `/data`, `/dpa`, `/privacy`, `/terms` |
| Status pill | https://status.visitors.now (external) |

## Auth

| URL | What it showed |
|---|---|
| `/login` | Login wall. Email field, disabled Continue with email, Google, GitHub, link to `/register`. Not submitted. Google and GitHub were not clicked |
| `/dashboard` | Redirects to `/login` when signed out (`fetch` was an opaque redirect) |
| `/account` | Opaque redirect, same class as `/dashboard` |
| `/register` | Linked from the homepage and the login card. Not opened. Creating an account is out of bounds |

## Docs tree (link list on `/docs`, pages not screenshotted)

Introduction `/docs`. Installation `/docs/installation` plus basic, nextjs, react, vuejs, nuxt, sveltekit, astro, angular. Subdomain tracking, custom events, identify, persist. Stripe, Dodo, RevenueCat. Account API and project API reference pages under `/docs/api/*` (list, create, delete, hostnames, blocked IPs, pathnames, realtime, members, invites, metrics, timeseries, pages, countries, cities, regions, browsers, devices, OS, referrers, UTMs, custom events, profiles).

## Blog (link list on `/blog`, posts not opened)

`/blog/introducing-the-api`, `/blog/dodo-payments-integration`, `/blog/revenuecat-integration`, `/blog/1k-mrr`, `/blog/introducing-revenue-attribution`, `/blog/introducing-funnels`, `/blog/google-analytics-alternatives`, `/blog/tech-stack`, `/blog/introducing-visitors`.

## Probes that 404

`/app`, `/projects`, `/setup`, `/onboarding`, `/settings`, `/p`.

## Signed-in app

Not reached. `/login` is a wall and `/dashboard` returns to it. No post-auth screen was opened, including the project setup screen a prior probe reported.
