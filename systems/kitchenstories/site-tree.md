# Kitchen Stories public site tree

Mapped on 2026-11-21 from https://www.kitchenstories.com/ before the screenshots. The live magazine is German. `document.documentElement.lang` is `de`. English `/en` is the 410 page already in this package. The product paints one light theme: body background `rgb(255, 255, 255)`, type `Plus Jakarta Sans`. There is no `theme-color` meta. No dark switch is in the header or footer.

The consentmanager dialog (`#cmpbox`, role dialog) covers the homepage on first paint. Copy: "Welcome to kitchenstories.com!". Visible controls: Accept all, Ad-free for 3.99 € / month, Login, Customize your choice, Cookies, Privacy notice, Legal notice, Language: en. It was hidden in CSS and never answered. Accept all was not clicked. Customize your choice was not opened. The paid ad-free control was not clicked. Login inside the dialog was not clicked. No email, password, or code was typed. No form was submitted. No identity provider was clicked.

Desktop CSS viewport measured `innerWidth` 1440, `innerHeight` 900, `devicePixelRatio` 2. The preview resize request was 1440 by 900. The first resize report came back 1280 by 800, then the page reported 1440 by 900.

## Header

Present on the homepage. At 1440 the links are in the bar. `button.mobile-menu-toggle` and `button.desktop-menu-toggle` are in the DOM with zero size at this width. The painted desktop nav is the inline links.

| Control | Page | Destination or state |
|---|---|---|
| Wordmark (`a.custom-logo-link`) | https://www.kitchenstories.com/ | https://www.kitchenstories.com/ |
| Kitchen Stories (text next to the wordmark) | https://www.kitchenstories.com/ | https://www.kitchenstories.com/ |
| Rezepte | https://www.kitchenstories.com/ | https://www.kitchenstories.com/rezepte |
| Artikel | https://www.kitchenstories.com/ | https://www.kitchenstories.com/stories |
| App | https://www.kitchenstories.com/ | https://pages.kitchenstories.com/de/app |
| Plus | https://www.kitchenstories.com/ | https://pages.kitchenstories.com/de/plus |
| Unsere Partner | https://www.kitchenstories.com/ | https://www.kitchenstories.com/partners |
| Suche öffnen | https://www.kitchenstories.com/ | Opens the search field on the page. `aria-expanded` was false before the click. Placeholder "Suche …". Nothing typed. Nothing submitted. |
| Menü (`button.mobile-menu-toggle`, aria Navigation) | https://www.kitchenstories.com/ | Hidden at 1440. Opens the phone menu at 390. |

`nav.main-navigation` (`aria-label` Hauptmenü) holds only Rezepte, Artikel, App, Plus, and Unsere Partner. There is no account item in that menu.

## Consent dialog

Opened by the site on first paint. Stays on the page. Not a product page.

| Control | Opens |
|---|---|
| Accept all | In-dialog accept. Not clicked. |
| Ad-free for 3.99 € / month | Paid path. Not clicked. |
| Login | In-dialog login. Not clicked. Branch stops. |
| Customize your choice | Privacy choices. Not opened. |
| Cookies | In-dialog cookies link. Not clicked. |
| Privacy notice | https://www.kitchenstories.com/datenschutz |
| Legal notice | https://www.kitchenstories.com/impressum |
| Language: en | Language control inside the dialog. Not clicked. |
| privacy policy, privacy center, Privacy Center | In-dialog links with `href` `#`. Not clicked. |

## Homepage body

The page is a magazine feed. Recipe cards, author avatars, partner logos, and "Alle anzeigen" are content links, not chrome. One card of each template is enough. Checkout, rating, and cart controls were not on the homepage.

| Control | Opens |
|---|---|
| Zum Inhalt springen | https://www.kitchenstories.com/#main (skip link, 1 px, off screen) |
| Recipe of the day card | A recipe URL on www.kitchenstories.com, for example `/french-toast-auflauf-pekannussen-gebackener/321094` |
| Author name or avatar on a card | An author URL, for example `/author/emre-redaktion` |
| Alle anzeigen (Rezepte im Trend) | https://www.kitchenstories.com/rezepte |
| Partner logo row | `/partners/<slug>` on www.kitchenstories.com (enerbio, rugenwalder-muhle, riso-gallo, kluth, hitchcock) |
| Slide previous / next | In-page swiper. Stays on the homepage. |
| Sponsored recipe cards | Recipe URLs. Same template as the feed. |

## Footer

| Control | Opens |
|---|---|
| Facebook | https://www.facebook.com/KitchenStoriesOfficial.de (off site, not followed) |
| Instagram | https://www.instagram.com/kitchenstories_official (off site, not followed) |
| tiktok | https://www.tiktok.com/@kitchenstories_official (off site, not followed) |
| Youtube | https://www.youtube.com/user/1kitchenstories (off site, not followed) |
| Pinterest | https://de.pinterest.com/kitchenstories/ (off site, not followed) |
| linkedin | https://www.linkedin.com/company/kitchenstories (off site, not followed) |
| Jobs – wir stellen ein! | https://pages.kitchenstories.com/de/career |
| Über uns | https://pages.kitchenstories.com/de/about |
| Team | https://www.kitchenstories.com/team |
| Kollaborationen | https://pages.kitchenstories.com/de/collaboration |
| Unsere App | https://pages.kitchenstories.com/de/app |
| Plus Neu | https://pages.kitchenstories.com/de/plus |
| Impressum | https://www.kitchenstories.com/impressum |
| AGB | https://www.kitchenstories.com/agb |
| Datenschutzcenter | https://www.kitchenstories.com/?cmpscreencustom (consent center query; not opened) |
| Datenschutzerklärung | https://www.kitchenstories.com/datenschutz |
| Kontakt | https://www.kitchenstories.com/kontakt |
| KI bei FUNKE Digital | https://www.kitchenstories.com/kuenstliche-intelligenz-bei-funke-digital-warum-und-wie-wir-sie-einsetzen |
| Werbemöglichkeiten | https://business.kitchenstories.com/ (off host, not followed) |
| Business Blog | https://business.kitchenstories.com/blog (off host, not followed) |
| Kontaktaufnahme | https://business.kitchenstories.com/#kontakt (off host, not followed) |
| hello@kitchenstories.de | mailto. Not opened. |
| FUNKE wordmark | https://www.funkemedien.de/de/ (off site, not followed) |

The footer prints a Berlin office address and a phone number as text, next to the mailto. There is no newsletter form in the footer DOM. The only forms on the homepage are two search forms (`input[name=s]`, method get).

## Phone

At 390 the same header links move behind Menü. That control is the visible `button.mobile-menu-toggle`. It opens an in-page menu. Escape closes it. Login is not in that menu.

## Walls this pass does not enter

| Control | Why it stops |
|---|---|
| Consent Login | Identity wall inside `#cmpbox`. Not clicked. |
| Ad-free for 3.99 € / month | Paid path. Not clicked. |
| Plus, Jetzt kostenlos starten | https://www.kitchenstories.com/de/checkout redirects to /checkout and paints a public 404. No payment form. Shot: screenshots/checkout-missing-light-default.png. |
| Website login | https://www.kitchenstories.com/login redirects to /profile. The page says website login has moved to the app. No email, password, or code field. App Store and Google Play badges were not clicked. Shots: screenshots/profile-light-default.png and screenshots/mobile-profile-light-default.png. |
| Newsletter signup | No newsletter form on the homepage. Not submitted. |
| Recipe rating submit and cart | Not submitted. |

## Pages opened from the tree

| Control | Landed | Shot |
|---|---|---|
| Homepage | https://www.kitchenstories.com/ | screenshots/home-light-default.png |
| Suche öffnen | same page, search field open, empty | screenshots/home-light-search-open.png |
| Menü at 390 | same page, overlay | screenshots/mobile-home-light-menu.png |
| Rezepte | /rezepte | screenshots/recipes-light-default.png |
| Artikel | /stories | screenshots/stories-light-default.png |
| App | pages.kitchenstories.com/de/app | screenshots/app-light-default.png |
| Plus | pages.kitchenstories.com/de/plus | screenshots/plus-light-default.png |
| Unsere Partner | /partners | screenshots/partners-light-default.png |
| Kollaborationen | pages.kitchenstories.com/de/collaboration | screenshots/collaboration-light-default.png |
| /login | /profile | screenshots/profile-light-default.png |
| /de/checkout | /checkout 404 | screenshots/checkout-missing-light-default.png |
