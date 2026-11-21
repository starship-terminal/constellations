# Supabase public site tree

Mapped on 2026-11-21 from the homepage, then photographed. Playwright, headless Chromium, signed out. `https://supabase.com/` returns 200. No form was submitted. No email, password, code, or address was typed. GitHub, ChatGPT, and SSO were not clicked. This is a refresh of the existing `systems/supabase` package. The signed-in dashboard was not entered. `login-extracted` stays not-started.

The marketing site follows the OS color scheme. A footer control opens a menu: System, Dark, Light. Dark is the color scheme used for the page shots. Light was selected once, photographed, then System was restored.

## Header

Desktop (1440). The wordmark goes to `/`.

| Control | Opens | Kind |
|---|---|---|
| Supabase home | `https://supabase.com/` | page |
| Product | Mega menu. Does not navigate by itself. | menu |
| Developers | Mega menu. Does not navigate by itself. | menu |
| Solutions | Mega menu. Does not navigate by itself. | menu |
| Pricing | `/pricing` | page |
| Docs | `/docs` | page |
| Blog | `/blog` | page |
| GitHub count | `https://github.com/supabase/supabase` | off site |
| Sign in | `https://supabase.com/dashboard` then `/dashboard/sign-in` | login wall. Stop. |
| Start your project | `https://supabase.com/dashboard/sign-up` | signup wall. Stop. |

Phone (390). A menu button opens a sheet. A Product select switches the sheet between Product, Developers, and Solutions. Sign in and Start your project sit at the bottom of the sheet. Both are the same walls.

## Product menu

| Item | Opens |
|---|---|
| Database | `/database` |
| Authentication | `/auth` |
| Storage | `/storage` |
| Edge Functions | `/edge-functions` |
| Compute | `/compute` |
| Realtime | `/realtime` |
| Vector | `/modules/vector` |
| Cron | `/modules/cron` |
| Queues | `/modules/queues` |
| Features | `/features` |
| Customer stories | `/customers` |
| Featured story | `/customers/lingodotdev` |
| Supabase vs Firebase | `/alternatives/supabase-vs-firebase` |
| Supabase vs Heroku Postgres | `/alternatives/supabase-vs-heroku-postgres` |
| Supabase vs Auth0 | `/alternatives/supabase-vs-auth0` |

## Developers menu

| Item | Opens |
|---|---|
| Documentation | `/docs` |
| Contribute | `/contribute` |
| Supabase Library | `/library` |
| Changelog | `/changelog` |
| Support | `/support` |
| Open Source | `/open-source` |
| Become a Partner | `/partners` |
| Partner Catalog | `/partners/catalog` |
| Careers | `/careers` |
| Events & Webinars | `/events` |
| Blog | `/blog` |

## Solutions menu

| Item | Opens |
|---|---|
| AI Builders | `/solutions/ai-builders` |
| No Code | `/solutions/no-code` |
| Beginners | `/solutions/beginners` |
| Developers | `/solutions/developers` |
| Postgres Devs | `/solutions/postgres-developers` |
| Vibe Coders | `/solutions/vibe-coders` |
| Hackathon Contestants | `/solutions/hackathon` |
| Startups | `/solutions/startups` |
| Agencies | `/solutions/agencies` |
| Enterprise | `/solutions/enterprise` |
| Innovation Teams | `/solutions/innovation-teams` |
| Hosted Postgres | `/solutions/hosted-postgres` |
| B2B SaaS | `/solutions/b2b-saas` |
| FinServ | `/solutions/finserv` |
| Healthcare | `/solutions/healthcare` |
| Agents | `/solutions/agents` |
| Switch from Firebase | `/solutions/switch-from-firebase` |
| Switch from Neon | `/solutions/switch-from-neon` |

## Footer

The footer repeats the product, solution, and company links, plus Twitter, GitHub, Discord, YouTube, TikTok, and Instagram. Company links include `/company`, `/careers`, `/ga`, `/legal`, `/privacy`, `/aup`, `/contact-us`, `/brand`, `/security`, `/regions`, and `https://status.supabase.com/`. A newsletter field ("Your email", Subscribe) was not filled and not submitted. A theme button opens System, Dark, and Light. Privacy Settings was not clicked.

## Home page interactions

| Control | What it does |
|---|---|
| Product, Developers, Solutions | Open the menus above. Stay on `/`. |
| Start your project (hero and header) | Signup wall. Stop. |
| Request a demo | `/contact/sales`. Form not submitted. |
| Customer story cards | `/customers/<slug>` |
| Theme | System, Dark, Light. Light was photographed. System restored. |

## Pricing

`/pricing` shows Free, Pro, Team, and Enterprise cards. Start for Free and Get Started go to the signup wall. Contact us goes to `/contact/sales`. Those links were not followed from this page. No checkout was opened.

## Docs

`/docs` is public. A Search button opens a "Search docs" field. Nothing was typed. Escape closed it.

## Login and signup walls

Reached from Sign in and Start your project. Fields were empty. The email placeholder reads `you@example.com`. The password placeholder is a row of dots, not a typed value. GitHub, ChatGPT, and SSO were not clicked. Sign in and Sign up were not clicked.

| URL | What it shows | Action |
|---|---|---|
| `https://supabase.com/dashboard` | Redirects to `/dashboard/sign-in?returnTo=/org` | Stop. Query not stored in the package. |
| Sign-in wall | Welcome back. Empty email and password. Continue with GitHub, Continue with ChatGPT, Continue with SSO. | Stop. |
| `https://supabase.com/dashboard/sign-up` | Get started. Same empty fields and the same three identity buttons. | Stop. |

Phone width shows the same empty walls without the quote panel. The signed-in product (projects, SQL, billing, team) is behind this wall.

## Public pages that loaded (200)

`/`, `/pricing`, `/docs`, `/database`, `/auth`, `/features`, `/blog`, `/customers`, `/company`, `/security`, `/solutions/enterprise`, `/brand`, `/changelog`, `/support`, `/contact/sales`, `https://status.supabase.com/`.

Homepage and pricing were also shot at 390. Login and signup were shot at 390 and left empty.
