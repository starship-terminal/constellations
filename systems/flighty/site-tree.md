# Flighty public site tree

Walked signed out on 2026-11-21 from [https://flighty.com/](https://flighty.com/) (title "Flighty — Live Flight Tracker: Get flight alerts faster than the airlines", canonical `https://flighty.com/`). Desktop CSS viewport 1440×900. No page-level theme switch. The page paints light (`color-scheme: normal`, body background `rgb(255, 255, 255)`).

Opened means the control was used and the result was photographed or the destination loaded. Linked means the href was read on the homepage and the page was not opened in this pass. Query strings on social links are stripped in this file.

There is no header Sign in, Log in, or Sign up. The product is the iOS app. "Get the app" and "Give Flighty a try" open an in-page download dialog. They do not open an account form.

## Top promo

A bar above the nav. The whole bar is one link.

| Control | Opens |
|---|---|
| NEW! Flighty Airports View Live | `https://www.flighty.com/airports` |

## Header, desktop

The wordmark (data-framer-name "flighty") is a link to `./` and stays on the marketing home.

These are plain links. None has `aria-haspopup`. None opens a menu.

| Control | Opens |
|---|---|
| Pricing | `/pricing` |
| Gift Cards | `/gift-cards` |
| Passport | `/passport` |
| Airports | `https://flighty.com/airports` |
| Help Center | `/help` |
| Get the app | No href. Click opens a fixed overlay (z-index 10) on `/`. The overlay shows a QR code, the line "or download on Mac", and one link to `https://apps.apple.com/app/flighty-live-flight-tracker/id1358823008`. That App Store link was not followed. Clicking the page behind the overlay closes it. |

A grid named Content sits in the navbar with height 0 until the nav is expanded. Its links, read from the DOM:

| Control | Opens |
|---|---|
| Pricing | `/pricing` |
| About | `/about` |
| Press | `/press` |
| Support | `/` (same marketing home) |
| Gift Cards | `/gift-cards` |
| Businesses | `/business` |

## Homepage anchors

These stay on `/` and scroll.

| Control | Opens |
|---|---|
| Preflight | `/#before-fly` |
| At the airport | `/#at-the-airport` |
| After landing | `/#after-fly` |

## Homepage actions

| Control | Opens |
|---|---|
| Give Flighty a try (White and Black variants) | No href. Same download overlay as Get the app. Not an account form. |
| Download | `https://apps.apple.com/app/apple-store/id1358823008` with campaign query. Not followed. |
| Flighty Airports | `https://www.flighty.com/airports` |
| With Flighty Airports | `https://www.flighty.com/airports` |
| Go Live | `https://flighty.com/airports/tv` |

## Cookie banner

A Framer banner, fixed, bottom. Copy: "We use cookies to enhance your experience, analyze site traffic and deliver personalized content." Controls: Cookie Settings (button, aria-label "Cookie Trigger"), Reject (`#__framer-cookie-component-button-reject`), Accept (`#__framer-cookie-component-button-accept`). None of these were clicked. Screenshots hide the banner with CSS so the page underneath can be read.

## Footer

| Control | Opens |
|---|---|
| Pricing | `/pricing` |
| Passport | `/passport` |
| Gift Cards | `/gift-cards` |
| Airports | `https://www.flighty.com/airports` |
| Flighty Insiders | `/insiders` |
| FlightRadar24 | `/compare/flightradar24` |
| TripIt | `/compare/tripit` |
| Airline Apps | `/compare/airline-apps` |
| FlightAware | `/compare/flightaware` |
| App In The Air | `/compare/app-in-the-air` |
| About | `/about` |
| Press | `/press` |
| Careers | `/careers` |
| Privacy Policy | `/legal/privacy` |
| Terms of Service | `/legal/terms` |
| Help Center | `/help` |
| Business | `/business` |
| Facebook | `https://www.facebook.com/flightyapp/` (external, not followed) |
| X | `https://x.com/flighty` (external, not followed) |
| Instagram | `https://www.instagram.com/flightyapp/` (external, not followed) |
| LinkedIn | `https://www.linkedin.com/company/flighty/` (external, not followed) |

## Account

No login, signup, or identity-provider control was on the homepage. `/login`, `/signin`, `/sign-in`, and `/account` were requested as documents only, to see whether a wall exists. They were not filled in.
