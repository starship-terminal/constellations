# Google public site tree

Mapped on 2026-11-22 from the live public site, signed out. Official domain confirmed as `https://www.google.com/` (title "Google", wordmark, empty search field). `https://google.com` resolves there. This is Google Search, not a parked page and not a captcha wall.

Nothing was typed. No identity provider was clicked. No form was submitted. No captcha was solved. Next was not clicked. `login-extracted` stays `not-started`.

The homepage paints one light theme. `color-scheme` on the root was `normal`. A `prefers-color-scheme: dark` context still painted a white page. Dark theme is a Settings row ("Dark theme: Off" on desktop, "Device default" in the phone menu). It was not switched.

Gmail, Maps, YouTube and Drive appear as links in the apps menu. They were not opened and they are not this package.

## Homepage header (`https://www.google.com/?hl=en`)

Desktop 1440. A white bar. Left links, then the wordmark and search field in the page, then the right cluster.

| Control | Opens |
|---|---|
| About | `https://about.google/` Marketing home. Public. |
| Store | `https://store.google.com/` Google Store. Other host. Not photographed as a product page. |
| Gmail | `https://mail.google.com/mail/` Account wall. Not followed. Not this package. |
| Images | `https://www.google.com/imghp` Google Images homepage. Public empty search. |
| Google apps | Overlay panel, no account required. "Sign in to arrange apps." Grid of product links. Not followed into Gmail, Maps, YouTube or Drive. |
| Sign in | `https://accounts.google.com/ServiceLogin` Empty wall. Branch stopped. |

## Search

| Control | Opens |
|---|---|
| Search field | Focus opens a trending-searches panel under the field. No query was typed. No search was submitted. |
| Search by voice | Full-page dialog. "Waiting..." and a close control. Closed. Nothing spoken. |
| Search by image | Not opened. |
| Google Search | Submits the query. Not clicked. |
| I'm Feeling Lucky | Submits a lucky query. Not clicked. |

## Settings menu

Footer Settings is a button. It opens a menu on the homepage. It is not a separate page until a row is followed.

| Row | Opens |
|---|---|
| Search settings | `https://www.google.com/preferences` Public settings. SafeSearch, search customisation, language. Not saved. |
| Advanced search | `https://www.google.com/advanced_search` Public form. Fields left empty. Not submitted. |
| Your data in Search | `https://www.google.com/history/privacyadvisor/search/unauth` Unsigned data page. Not photographed. |
| Search history | `https://www.google.com/history/optout` History opt-out. Not photographed. |
| Search help | `https://support.google.com/websearch/` Support host. Not photographed. |
| Send feedback | Feedback dialog. Not opened. |
| Dark theme: Off | Theme toggle. Not switched. |

## Footer

| Control | Opens |
|---|---|
| Advertising | Redirects to `business.google.com` Google Ads. Other product. Not kept as this package. |
| Business | Redirects to `business.google.com` Business Profile. Other product. Not kept. |
| How Search works | `https://www.google.com/search/howsearchworks/` Public explainer. |
| Privacy | `https://policies.google.com/privacy` Public policy. |
| Terms | `https://policies.google.com/terms` Public terms. |
| Language links (简体中文, Bahasa Melayu, தமிழ்) | `setprefs` on the homepage. Not followed. |

Country label on this capture: Singapore. That is the edge location, not an account.

## Google apps panel

Opens from the grid button with no account. A white card. First rows: Account, Search, Maps, YouTube, News, Gmail, Meet, Chat, Contacts, Drive, Calendar, Play, Translate, Photos, Chrome, Shopping. The panel says "Sign in to arrange apps." Product links were not followed. Gmail, Maps, YouTube and Drive are other packages.

The same grid links to `https://about.google/products/`, which is public and was photographed.

## Phone (390)

The phone homepage replaces the desktop footer with a menu button, ALL and IMAGES tabs, a bell, the apps grid, and Sign in. The search field has add, AI mode, voice and camera icons. Trending searches sit under the field. Those rows were not opened.

| Control | Opens |
|---|---|
| Main menu | A sheet: Sign in, SafeSearch, Language, Dark theme, More settings, Help, Privacy Policy, Terms of Service. More settings was not followed. Dark theme was not switched. |
| Sign in | Same empty accounts wall, stacked for the phone. |
| Google apps | Same product grid. Not followed. |
| Notifications | `iga.google.com`. Not opened. |

## Auth walls

Photographed empty. Stopped there.

| Control | URL | What it asked |
|---|---|---|
| Sign in | `https://accounts.google.com/ServiceLogin?hl=en` | Email or phone, Forgot email?, Create account, Next. Field empty. |
| Create account | `https://accounts.google.com/signup?hl=en` | First name, Last name (optional), Next. Fields empty. A captcha response field was in the DOM. Not solved. Next not clicked. |
| Identity providers | Not present as buttons on the empty email step | Not clicked. |
| Gmail | `mail.google.com` | Not opened. |

The signed-in account, inbox, Drive, Maps and YouTube were not entered.
