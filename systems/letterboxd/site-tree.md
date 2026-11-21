# Letterboxd public site tree

Mapped on 2026-11-21 from https://letterboxd.com/ before the screenshots. `document.documentElement.lang` is `en`. The product paints one dark field: body background `rgb(20, 24, 28)`, type `GraphikWeb`. There is no `theme-color` meta and no dark switch in the header or footer.

Desktop CSS viewport measured `innerWidth` 1440, `innerHeight` 900, `devicePixelRatio` 2 in the preview tab. The preview resize request was 1440 by 900. The first resize report came back 1280 by 800, then the page reported 1440 by 900. Headless captures used a 1440 by 900 viewport at device scale 1, and a 390 by 844 viewport at device scale 2.

No consent dialog covered the homepage. A hidden footer item says "Cookies". It was not opened. A Turnstile dialog ("Security check. We've detected a massive gravitational anomaly.") appeared in one headless run when Create account was clicked. It was not solved. That click was abandoned.

## Header

Present on the homepage. At 1440 the links are in the bar.

| Control | Page | Destination or state |
|---|---|---|
| Wordmark (`a.logo`) | https://letterboxd.com/ | https://letterboxd.com/ |
| Sign in | https://letterboxd.com/ | https://letterboxd.com/sign-in/ |
| Create account | https://letterboxd.com/ | Colorbox overlay on the homepage (`#cboxContent`, "Join Letterboxd"). The URL becomes `/?register=true`. |
| Films | https://letterboxd.com/ | https://letterboxd.com/films/ |
| Lists | https://letterboxd.com/ | https://letterboxd.com/lists/ |
| Members | https://letterboxd.com/ | https://letterboxd.com/members/ |
| Journal | https://letterboxd.com/ | https://letterboxd.com/journal/ |
| Search (`#search-q`, form action `/search/`) | https://letterboxd.com/ | Field is already in the bar. Nothing typed. Nothing submitted. |

`nav.main-nav` holds Sign in, Create account, Films, Lists, Members, and Journal. There is no account menu when signed out.

## Homepage body

The page is a film poster feed plus marketing panels. Poster cards are content links. One film and one list are enough.

| Control | Opens |
|---|---|
| Get started, it's free | Same Create account overlay as the header. |
| iOS, Apple TV and Android | https://letterboxd.com/apps/ |
| Poster card | A public film URL, for example `/film/club-kid/` |
| Letterboxd lets you panels | `/welcome/` anchors, or `/pro/` for the diary panel |
| Popular reviews this week | https://letterboxd.com/reviews/popular/this/week/ |
| Popular lists | A public list URL, for example `/official/list/letterboxds-top-500-films/` |
| Popular reviewers | A public member profile. Not opened as a personal page. The members index was opened instead. |

## Footer

| Control | Opens |
|---|---|
| About | https://letterboxd.com/about/ |
| Pro | https://letterboxd.com/pro/ |
| News | https://letterboxd.com/journal/ |
| Apps | https://letterboxd.com/apps/ |
| Help | https://support.letterboxd.com/ (off host, not followed) |
| Year in Review | https://letterboxd.com/year-in-review/ (not opened) |
| Gifts | https://letterboxd.com/gift-guide/ (not opened) |
| Terms | https://letterboxd.com/legal/terms-of-use/ (not opened) |
| API | https://letterboxd.com/api-beta/ (not opened) |
| Contact | https://letterboxd.com/contact/ |
| Instagram, Threads, X, Bluesky, Facebook, TikTok, YouTube | Off site. Not followed. |
| Film data | https://letterboxd.com/about/film-data/ (not opened) |
| TMDB | https://www.themoviedb.org/ (off site, not followed) |
| Mobile site | https://letterboxd.com/# (in-page, not followed) |
| Your Privacy Choices | https://letterboxd.com/privacy-choices/ (not opened) |
| Privacy Notice | https://letterboxd.com/legal/privacy-notice/ (not opened) |
| Cookies | Same privacy-choices URL. Not opened. |

## Phone

At 390 the header collapses to Sign in, a hamburger (`a.replace`, text "Open/Close menu"), and search. The hamburger opens the same nav: Create account, Films, Lists, Members, Journal. Shot: screenshots/mobile-home-light-menu.png.

## Walls this pass does not enter

| Control | Why it stops |
|---|---|
| Sign in | https://letterboxd.com/sign-in/ shows an empty username and password form. Nothing typed. Nothing submitted. No identity provider on the form. Shot: screenshots/signin-light-default.png. |
| Create account | Overlay with empty email, username, and password fields, plus an age checkbox. Nothing typed. Nothing checked. Nothing submitted. Shot: screenshots/signup-light-default.png. |
| Reset password | Linked from the sign-in form. Not clicked. |
| Turnstile security check | Appeared once in headless Chromium over the homepage. Not solved. |
| Pro and Patron subscribe | Pricing page photographed. No plan was started. |
| Sign in to log, rate or review | On the film page. Not clicked. |

## Pages opened from the tree

| Control | Landed | Shot |
|---|---|---|
| Homepage | https://letterboxd.com/ | screenshots/home-light-default.png |
| Films | /films/ | screenshots/films-light-default.png |
| A public film | /film/the-hunger-games-sunrise-on-the-reaping/ | screenshots/film-light-default.png |
| Lists | /lists/ | screenshots/lists-light-default.png |
| A public list | /official/list/letterboxds-top-500-films/ | screenshots/list-light-default.png |
| Members | /members/ | screenshots/members-light-default.png |
| Journal | /journal/ | screenshots/journal-light-default.png |
| About | /about/ | screenshots/about-light-default.png |
| Pro | /pro/ | screenshots/pro-light-default.png |
| Apps | /apps/ | screenshots/apps-light-default.png |
| Contact | /contact/ | screenshots/contact-light-default.png |
| Welcome | /welcome/ | screenshots/welcome-light-default.png |
| Missing page | /this-page-is-not-real-404/ | screenshots/missing-light-default.png |
| Sign in | /sign-in/ | screenshots/signin-light-default.png |
| Create account | overlay | screenshots/signup-light-default.png |
| Phone homepage | same host, 390 | screenshots/mobile-home-light-default.png |
| Phone film | same film, 390 | screenshots/mobile-film-light-default.png |
