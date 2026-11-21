# Reflect site tree

Mapped 2026-11-21 from the public homepage at https://reflect.app/, signed out, in headless Chromium. Desktop viewport measured 1440×900 at devicePixelRatio 2. Phone viewport measured 390×844 at devicePixelRatio 2. The marketing page paints one dark theme. `color-scheme` stayed `normal` when the browser asked for dark. Body background stayed `rgb(3, 0, 20)`.

No email, password, code, phone, or address was typed. No form was submitted. Google, Apple, Discord, and Twitter were not clicked. The newsletter Subscribe control was not clicked. The launch film was opened and closed. It was not played through.

The control map is also the shot list in [screenshots/](screenshots).

## Shell (desktop)

A wordmark sits left. A pill of links sits in the centre. Log in to Classic and Download sit right.

| Control | Opens |
|---|---|
| Wordmark (`a`, href `/home/`) | page https://reflect.app/home/ (same homepage) |
| Product (`a`, href `#connected`) | section on the same page |
| Pricing (`a`, href `#pricing`) | section on the same page. See [home-light-pricing](screenshots/home-light-pricing.png). |
| Company (`a`, href `#about`) | section on the same page. See [home-light-company](screenshots/home-light-company.png). |
| Blog (`a`) | page https://reflect.app/blog |
| Changelog (`a`) | https://github.com/team-reflect/reflect-open/releases (leaves the host). Not followed. |
| GitHub (`a`) | https://github.com/team-reflect/reflect-open (leaves the host). Not followed. |
| Log in to Classic (`a`, href `/auth`) | page https://reflect.app/auth. Login wall. Branch stopped. See [login-light-default](screenshots/login-light-default.png). |
| Download (`a`, href `/download`) | page https://reflect.app/download |

There is no desktop dropdown. Product, Pricing, and Company scroll the homepage.

## Phone (390)

The centre links collapse. A `.header-toggle` (three lines, no aria-label) opens `.header-nav`, a fixed full-viewport drawer with background `rgba(3, 0, 20, 0.9)`. Close is an X. The drawer lists Product, Pricing, Company, Blog, Changelog, GitHub, and Log in to Classic. Download stays in the header. See [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) and [mobile-home-light-default](screenshots/mobile-home-light-default.png).

## Home https://reflect.app/

| Control | Opens |
|---|---|
| Meet Reflect Open | https://github.com/team-reflect/reflect-open/releases. Not followed. |
| Download for Mac | page https://reflect.app/download |
| Get the iPhone & iPad app | https://apps.apple.com/us/app/reflect-open/id6787385615. Not followed. |
| Play the Reflect launch film (`button`) | video dialog on the same page. Close video dismisses it. See [home-light-video-dialog](screenshots/home-light-video-dialog.png). |
| Click to see AI magic | an on-page demo. Not a signed-in surface. |
| How privacy works | GitHub privacy doc. Not followed. |
| Claim your code | https://reflect.app/claim-reflect-open, which redirects to `/auth?redirect=/claim-reflect-open`. Same login wall. Not submitted. |
| See our values | https://reflect.academy/our-values. Leaves the host. Not followed. |
| Take the course | https://reflect.academy/. Leaves the host. Not followed. |
| Subscribe (newsletter) | same page. Not clicked. The email field was left empty. |

See [home-light-default](screenshots/home-light-default.png) and [home-light-full](screenshots/home-light-full.png).

## Footer (homepage)

Three columns: Product (Features, Pricing, Changelog, GitHub), Company (Our team, Our values, Blog), Resources (Downloads, Documentation, Privacy, Contact). Discord and X icons leave the host. A newsletter row asks for an email. The legal line is Privacy Policy and Terms and Conditions, plus "Reflect App, LLC. All rights reserved."

| Column | Opens |
|---|---|
| Features | https://reflect.app/#features |
| Pricing | https://reflect.app/#pricing |
| Changelog, GitHub | GitHub. Not followed. |
| Our team | https://reflect.academy/our-team |
| Our values | https://reflect.academy/our-values |
| Blog | https://reflect.app/blog |
| Downloads | https://reflect.app/download |
| Documentation | https://reflect.academy/ |
| Privacy (footer resources) | GitHub privacy doc |
| Contact | https://reflect.academy/contact-us |
| Privacy Policy | https://reflect.app/privacy |
| Terms and Conditions | https://reflect.app/terms |
| Discord | https://reflect.app/discord, which redirects to a Discord invite. Not followed into Discord. |
| X | https://x.com/reflectnotes |

See [home-light-footer](screenshots/home-light-footer.png).

## Pages captured

| Page | What else it opens |
|---|---|
| https://reflect.app/ | Homepage. Anchors for product, pricing, and company. Video dialog. Newsletter field left empty. |
| https://reflect.app/blog | Public blog. Tags are buttons: All Tags, Toolshed Interviews, Reflect Workflows, Articles, Product Updates. Articles was clicked. Nothing was typed. Login and Start Free Trial both go to `/auth`. See [blog-light-default](screenshots/blog-light-default.png) and [blog-light-articles](screenshots/blog-light-articles.png). Phone: [mobile-blog-light-default](screenshots/mobile-blog-light-default.png). |
| https://reflect.app/download | Platform download cards (macOS Apple Silicon, macOS Universal, Windows, Linux, iPhone & iPad). Cards were not clicked, so no binary was fetched. See [download-light-default](screenshots/download-light-default.png). |
| https://reflect.app/#pricing | On the homepage. Mac is Free. iPhone and iPad is "Paid subscription" with "See local pricing on the App Store." No dollar amount on the page. |
| https://reflect.app/privacy | Light document. Public legal copy. See [privacy-light-default](screenshots/privacy-light-default.png). |
| https://reflect.app/terms | Light document. See [terms-light-default](screenshots/terms-light-default.png). |
| https://reflect.app/not-found | Public 404 ("Oops", Back to home, Error 404). See [notfound-light-default](screenshots/notfound-light-default.png). |
| https://reflect.app/auth | Empty login wall. Also the destination of `/login`, Start Free Trial, and Claim your code. Google and Apple buttons were not clicked. The email field was empty. Continue was not clicked. See [login-light-default](screenshots/login-light-default.png). There is no separate signup page: `/signup` and `/register` 404, and the trial link lands on this same wall. |

## Stopped

Login and signup are the same empty wall at `/auth`. Identity providers were not clicked. No form was submitted. The signed-in app was not entered. `login-extracted` was left not-started.
