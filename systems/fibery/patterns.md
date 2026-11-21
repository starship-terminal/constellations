# Fibery patterns

Public site, 2026-11-21. The signed-in app was not captured.

## App shell

The marketing header is a wordmark, three hover menus (Solutions, Platform, Support), a Pricing link, Book a demo, Log in, and Sign up for free. On a 390-wide viewport the same links sit in a burger panel. See [home-light-default](screenshots/home-light-default.png) and [home-light-mobile-menu](screenshots/home-light-mobile-menu.png).

## Pricing

Yearly is the default. Monthly is a label in `PriceSwitcher`, not a separate page. Clicking Monthly repainted the cards to $15, $24 and $50 per user per month. Get started and Start free trial go to `/sign-up`, which was not submitted. See [pricing-light-monthly](screenshots/pricing-light-monthly.png).

## Search

No search field was found on the marketing home, templates, or blog pages. The public user guide at `the.fibery.io` paints an "AI Search" label. Its control was not isolated, so search is not captured.

## Auth wall

Log in and Sign up for free leave the marketing host for `https://fibery.io/login` and `https://fibery.io/sign-up`. The walk stopped there. See [login-review.json](login-review.json).
