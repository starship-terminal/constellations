# Cursor public site tree

Mapped on 2026-11-22 from the live public site, signed out. Official domain confirmed as [https://cursor.com](https://cursor.com) (wordmark Cursor, hero "Cursor is your coding agent for building ambitious software."). This is the public marketing site. [systems/cursor-desktop](../cursor-desktop) and [systems/cursor-ios](../cursor-ios) are different packages and were not edited.

Nothing was typed. No identity provider was clicked. No form was submitted. No captcha was solved. `login-extracted` stays `not-started`.

The marketing site paints one dark theme. `color-scheme` on the root was `dark`. There is no public theme toggle. The page background is `#14120b`. The accent declared as `--color-theme-accent` is `#f54e00`.

Desktop captures are 1440 by 900 CSS pixels at devicePixelRatio 1. The phone homepage and the phone menu are 390 by 844 CSS pixels at devicePixelRatio 2 (PNG width 780). A OneTrust cookie banner and a second in-page cookie card were removed in the page before the marketing screenshots. They were not accepted or rejected.

## Header, desktop

The logo links to `/home`. Sign in links to `/dashboard` and then to the login wall. Contact sales links to `/contact-sales`. Download links to `/download`.

Models, Product, and Resources are buttons (`aria-label` "Expand Menu") that reveal links already in the header markup. The destinations were read from the DOM. The menus were not photographed open.

| Menu | Destinations |
|---|---|
| Models | `/grok` (Grok), `/evals` (Evals) |
| Product | `/product` (Agents), `/cloud` (Cloud), `https://x.ai/bot` (Grok Bot), `/mobile` (Mobile), `/automate` (Automations), `/cli` (CLI), `/marketplace` (Marketplace), `/bugbot` (Review) |
| Resources | `/changelog`, `/blog`, `/docs`, `/community`, `https://cursor.com/help`, `/workshops`, `https://forum.cursor.com/`, `/careers` |

Enterprise and Pricing are direct links to `/enterprise` and `/pricing`.

## Header, phone (390)

Open navigation replaces the bar. The drawer lists Models, Product, Enterprise, Pricing, and Resources, plus Sign up (`/signup`) and Sign in (`/dashboard`). Photographed in [mobile-home-dark-menu.png](screenshots/mobile-home-dark-menu.png). Close is the same overlay. The drawer sections were not expanded.

## Homepage

`/` returned HTTP 200. Photographed in [home-dark-default.png](screenshots/home-dark-default.png) and, at phone width, [mobile-home-dark-default.png](screenshots/mobile-home-dark-default.png).

| Control | Opens |
|---|---|
| Download for macOS | `https://api2.cursor.sh/updates/download/golden/darwin-arm64/cursor/3.31`. A download URL. The file was not saved. |
| Get started | `/login`. Wall. Branch stopped after the empty login photograph. |
| Request a demo | `/contact-sales`. Not opened. |
| Learn about cloud agents | `/docs/cloud-agent`. Linked, not opened. |
| Download Grok Bot | `/download/bot`. Not opened. |
| Explore models | `/docs/models`. Linked, not opened. |
| Explore enterprise | `/enterprise`. Opened. |
| Changelog items | `/changelog/<slug>`. The index was opened. Individual posts were linked. |
| Join us | `/careers`. Linked, not opened. |
| Blog cards | `/blog/<slug>` and `https://x.ai/news/grok-4-7`. The index was opened. Posts were linked. |

The homepage hero is a product demo (agent windows, model names). It is a public demo, not a signed-in account.

## Pricing

`/pricing` returned HTTP 200. Photographed in [pricing-dark-default.png](screenshots/pricing-dark-default.png). Individual is the painted tab. Teams was not switched.

| Plan | Price painted | Control |
|---|---|---|
| Free | $0 / month | Get started |
| Plus | $8 / month | Get Plus |
| Premium | $30 / month | Get Premium. Marked most popular. |
| Super | $100 / month | Get Super |
| Ultra | $200 / month | Get Ultra. In the comparison table. |
| Teams | $30+ / user / month | Get Teams |
| Enterprise | Custom | Contact Sales |

Get started and the paid plan buttons were not followed into checkout.

## Download

`/download` returned HTTP 200. Photographed in [download-dark-default.png](screenshots/download-dark-default.png). Desktop, Terminal, and Web cards are on the page. The download list names macOS, Windows, and Linux builds for 3.31. The install links were not followed. The file was not saved.

## Other public pages opened

| Path | Result |
|---|---|
| `/product` | HTTP 200. [product-dark-default.png](screenshots/product-dark-default.png). |
| `/enterprise` | HTTP 200. [enterprise-dark-default.png](screenshots/enterprise-dark-default.png). |
| `/changelog` | HTTP 200. [changelog-dark-default.png](screenshots/changelog-dark-default.png). |
| `/blog` | HTTP 200. [blog-dark-default.png](screenshots/blog-dark-default.png). |
| `/this-page-does-not-exist` | HTTP 200 with a 404 page. [not-found-dark-default.png](screenshots/not-found-dark-default.png). Copy: "The page you're looking for has wandered off." |

## Footer

Read on the homepage. Not every link was opened.

| Column | Links |
|---|---|
| Product | Agents `/product`, Teams `/business/teams`, Enterprise, Pricing, Code Review `/bugbot`, CLI, Cloud Agents `/agents`, Composer `/composer`, Marketplace, Download |
| Resources | Changelog, Docs, Learn, Forum, Help, Workshops, Status `https://status.cursor.com/` |
| Company | Careers, Blog, Community, Students, Brand, Future, Anysphere `https://anysphere.inc/` |
| Legal | Terms of Service, Acceptable Use Policy, Grok Bot Terms, SpaceXSI Subscription Terms `https://x.ai/legal`, Privacy Policy, Cookie Policy, Data Use, Security |
| Connect | X, LinkedIn, YouTube |

Privacy choices is a button. It was not opened.

## Auth walls

Sign in on the marketing header goes to `/dashboard`, which redirects to `https://authenticator.cursor.sh/`. The empty wall was photographed in [login-dark-empty.png](screenshots/login-dark-empty.png). Title: Sign in. Heading: Welcome to Cursor. Fields seen and left empty: Email ("Your email address"). Actions seen and not used: Continue with Google, Continue with GitHub, Continue with Apple, Continue with Grok, Continue with X, Continue with email. Sign up is a link to `/sign-up` on the same host.

Clicking Sign up loaded a Cloudflare page titled "Just a moment..." with "Performing security verification" and a "Verify you are human" checkbox. The checkbox was not clicked. The captcha was not solved. The signup form was not reached. No signup screenshot was saved, because the page is a captcha wall rather than an empty form.

Headless Chromium could not load the login wall. It stopped on the same Cloudflare page. The login photograph is from the preview browser, scaled from a 2x frame to 1440 by 900.

`login-extracted` stays `not-started`.
