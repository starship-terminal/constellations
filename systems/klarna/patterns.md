# Klarna patterns

How the public pages combine. Screenshots are in [screenshots/](screenshots). Signed-in product patterns are recorded as gaps, not drawn.

## Marketing shell

A white page, a sticky header, then a full-bleed hero. The header holds the wordmark, text nav pills (Shop and siblings), a round search button, a language control, and an ink Sign in pill. The hero is a campaign carousel. One stored frame is "Introducing Apple Upgrade" with a pink "Get the app" QR card over the art.

See [home-light-default](screenshots/home-light-default.png) and [home-light-nav-hover](screenshots/home-light-nav-hover.png).

Phone width drops the text nav into a menu. The stored phone shot is the closed header: [mobile-home-light-default](screenshots/mobile-home-light-default.png). The open menu overlay was not captured.

## Country picker

`/international/` is a public list of markets before a locale is chosen. It uses the same ink and pill language as the US site, on a white page. See [international-light-default](screenshots/international-light-default.png) and [mobile-international-light-default](screenshots/mobile-international-light-default.png).

## Search

Search is an overlay, not a results page in this capture. A round header button opens a white popover on a scrim. The field placeholder is "Search for any product or brand". Suggestion rows name a category or a brand (Clothing, Nike, Shoes, Apple). The query was not submitted, so there is no results grid, empty state, or filter bar.

See [home-light-search](screenshots/home-light-search.png).

## Help

Help home (`/us/help/`) is a search field ("Search anything") plus category links into `/us/help/<topic>/`. A topic page (Klarna Card) puts pill tabs across the top. "All" is the selected ink pill. Other tabs are outlined. Questions are full-width link rows with chevrons, not accordions. Article bodies were not opened.

See [help-light-default](screenshots/help-light-default.png) and [help-topic-light-default](screenshots/help-topic-light-default.png).

## Language and region

The header language control opens a dialog of market rows. It was opened and photographed ([home-light-language-menu](screenshots/home-light-language-menu.png)). Confirm was not submitted, so no locale change was applied.

## Sign-in boundary

Sign in in the header goes to `https://app.klarna.com/login?market=US&locale=en-US`. The page that loaded is a QR interstitial: "Continue securely in the Klarna app", with a "Continue on web?" Sign in control. That control was not followed. There is no typed email field in this capture.

See [signin-boundary-light-default](screenshots/signin-boundary-light-default.png).

## Product marketing, not the product

`/us/what-is-klarna/`, `/us/shopping/`, `/us/klarna-app/`, `/us/buyer-protection/`, `/us/personal-account/` and `/us/phishing/` are public explanations. They reuse the shell, display type, and pill buttons. They do not show balances, orders, or a checkout.

See [shopping-light-default](screenshots/shopping-light-default.png), [app-light-default](screenshots/app-light-default.png), [buyer-protection-light-default](screenshots/buyer-protection-light-default.png), [personal-account-light-default](screenshots/personal-account-light-default.png).

## What this capture does not include

Forms and validation, empty, loading and error states, destructive confirmation, toasts, data tables, onboarding, and the signed-in app shell are not on these pages. Payments, purchases, portfolio, savings, account and checkout sit behind the sign-in boundary above. Search filtering and results sit behind submitting the overlay. The cookie preference center sits behind the OneTrust banner, which was hidden and never opened.
