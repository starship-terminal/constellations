# Spotify public site tree

Mapped on 2026-11-21 from [https://spotify.com](https://spotify.com) before the screenshots. The host redirects to [https://open.spotify.com/](https://open.spotify.com/). This machine resolved the marketing locale to Singapore English (`/sg-en/`). `document.documentElement` on the web player had class `encore-dark-theme` and `color-scheme: dark`. The marketing pages had `color-scheme: normal` and painted a black hero on a near-black page.

A cookie banner ("We and our partners use cookies") covered the first load. It was closed. Allow All was not clicked. No account setting was changed.

Nothing was typed. Google, Facebook, and Apple were not clicked. Continue and Next were not clicked. No form was submitted. No playback session was started. The signed-in app was not entered.

Desktop CSS viewport measured `innerWidth` 1440, `innerHeight` 900, `devicePixelRatio` 2. Phone CSS viewport measured `innerWidth` 390, `innerHeight` 844, `devicePixelRatio` 2, with an iPhone user agent. At 390, `spotify.com` serves the mobile marketing shell, not the desktop web player.

## Header, desktop web player

Present on [https://open.spotify.com/](https://open.spotify.com/).

| Control | Opens |
|---|---|
| Wordmark | https://open.spotify.com/ |
| Home | The signed-out home feed. Already on that page. |
| Search | https://open.spotify.com/search (Browse all). The field stays in the bar. Nothing typed. |
| Browse | Same search browse. |
| Premium | https://www.spotify.com/sg-en/premium/ |
| Support | https://support.spotify.com/ (off the marketing host). Not followed as a product page. |
| Download | https://www.spotify.com/sg-en/download/windows/ on this Mac. |
| Install App | https://open.spotify.com/download |
| Sign up | https://www.spotify.com/sg-en/signup |
| Log in | https://accounts.spotify.com/en/login |

## Homepage body

The signed-out player is a public preview: Your Library (empty prompts), trending songs, popular artists, popular albums. Cards are public content links. Play buttons were not clicked.

| Control | Opens |
|---|---|
| Create playlist | Stays on the signed-out preview. Not used to start an account. |
| Browse podcasts | https://open.spotify.com/genre/podcasts-web |
| A trending song card | A public album URL, for example `/album/47lGFW58QJPb3i2pM53Qni` |
| A popular artist | A public artist URL. The Weeknd was opened: `/artist/1Xyo4u8uXC1ZmMpatF05PJ` |
| Sign up free (preview bar) | The signup wall. Not submitted. |
| English | A language dialog, "Choose a language". Closed without picking another language. |

## Left rail and footer links

The rail holds Your Library, Create playlist, Browse podcasts, and the legal cluster.

| Control | Opens |
|---|---|
| Legal | https://www.spotify.com/sg-en/legal/ (not opened) |
| Safety & Privacy Center | https://www.spotify.com/sg-en/safetyandprivacy/ (not opened) |
| Privacy Policy | https://www.spotify.com/sg-en/legal/privacy-policy/ (not opened) |
| Cookies | https://www.spotify.com/sg-en/legal/cookies-policy/ (not opened) |
| About Ads | https://www.spotify.com/sg-en/legal/privacy-policy/ (not opened) |
| Accessibility | https://www.spotify.com/sg-en/accessibility/ (not opened) |
| English | The language dialog above. |

The marketing footer, read on the premium page, also lists About, Jobs, For the Record, For Artists, For creators, For authors, Developers, Advertising, Investors, Vendors, Support, Web Player, Free Mobile App, Import your music, Premium Individual, Duo, Family, Student, and Spotify Free. Off-host links were not followed. About, Free, Premium, and Download were opened.

## Marketing header

On premium, download, free, about, and the missing page.

| Control | Opens |
|---|---|
| Spotify wordmark | https://www.spotify.com/sg-en/ (redirects to the web player) |
| Premium plans | A menu of Individual, Duo, Family, Student, then the plans block on the premium page. |
| Support | https://support.spotify.com/ |
| Download | https://www.spotify.com/sg-en/download/ |
| Sign up | https://www.spotify.com/sg-en/signup |
| Log in | https://www.spotify.com/sg-en/login/ then https://accounts.spotify.com/en/login |
| Try 3 months for $0 | A purchase offer URL. Not followed. No plan was started. |
| Locale chip, 新加坡（简体中文) | https://www.spotify.com/sg-zh/ for the same path. Not followed. The chip was closed. |

## Phone

At 390 the homepage is the mobile shell: wordmark, Open App, a hamburger, a Premium offer card, trending songs, and a tab bar (Home, Search, Your Library, Premium).

| Control | Opens |
|---|---|
| Menu | A full-screen drawer: Log in, Sign up, Premium, Help, Download, Privacy, Terms. Closed with the X. |
| Open App | Not clicked. It leaves the browser for the native app. |
| Try 3 months for SGD 0 | Not clicked. |
| A popular artist | The public artist page, phone width. |
| Home, Search, Your Library, Premium | Tab bar. Premium goes to the marketing premium page. Search and Library were not used to start a session. |

## Walls this pass does not enter

| Control | Why it stops |
|---|---|
| Log in | https://accounts.spotify.com/en/login shows Welcome back, an empty email field, Continue, and Continue with Google, Facebook, and Apple. Nothing typed. Nothing submitted. No identity provider clicked. Shot: screenshots/public/login-dark-default.png. |
| Sign up | https://www.spotify.com/sg-en/signup shows Sign up to start listening, an empty email field (placeholder `name@domain.com`), Next, and Sign up with Google and Apple. Nothing typed. Next was not clicked. Shot: screenshots/public/signup-dark-default.png. |
| reCAPTCHA | Named on both walls. Not solved. |
| Try 3 months / Get Premium | Pricing photographed. No checkout. |
| Play, Follow, Create playlist | Visible on the public artist and home pages. Not clicked. Playback needs an account. |
| Open App | Not clicked. |

## Pages opened from the tree

| Control | Landed | Shot |
|---|---|---|
| Homepage | https://open.spotify.com/ | screenshots/public/web-home-dark-default.png |
| Language dialog | same page, dialog open | screenshots/public/web-home-dark-language.png |
| Search | https://open.spotify.com/search | screenshots/public/web-search-dark-default.png |
| Search field focused, empty | same page | screenshots/public/web-search-dark-focused.png |
| A public artist | /artist/1Xyo4u8uXC1ZmMpatF05PJ | screenshots/public/web-artist-dark-default.png |
| Premium | https://www.spotify.com/sg-en/premium/ | screenshots/public/premium-light-default.png |
| Premium plans | same page, plans block | screenshots/public/premium-light-plans.png |
| Download | https://www.spotify.com/sg-en/download/windows/ | screenshots/public/download-light-default.png |
| Free | https://www.spotify.com/sg-en/free/ | screenshots/public/free-light-default.png |
| About | https://www.spotify.com/sg-en/about-us/contact/ | screenshots/public/about-light-default.png |
| Missing page | /sg-en/this-page-is-not-real-404/ | screenshots/public/missing-light-default.png |
| Log in | https://accounts.spotify.com/en/login | screenshots/public/login-dark-default.png |
| Sign up | https://www.spotify.com/sg-en/signup | screenshots/public/signup-dark-default.png |
| Phone homepage | https://open.spotify.com/ at 390 | screenshots/public/web-home-dark-mobile.png |
| Phone menu | same page, drawer open | screenshots/public/web-home-dark-mobile-menu.png |
| Phone artist | same artist, 390 | screenshots/public/web-artist-dark-mobile.png |
| Phone premium | https://www.spotify.com/sg-en/premium/ at 390 | screenshots/public/premium-light-mobile.png |
