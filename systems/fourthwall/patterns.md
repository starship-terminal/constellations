# Fourthwall patterns

How the public marketing site combines the measured pieces. Captured 2026-11-21, signed out, at 1440x900 and 390x844. The control-by-control map is [site-tree.md](site-tree.md).

## Shell

Desktop bar (`nav.nav-bar`): wordmark to `/`, Features (hover menu), Product catalog (off-site catalog), Pricing, Learn (hover menu), Log in, Start now. The bar is transparent over an ink hero. Type is paper, Suisse Intl 450. Start now is a white 12px-radius pill. [home](screenshots/home-default.png), [nav crop](components/crops/nav-default.png).

Phone: wordmark and a burger. The burger opens a full-screen ink menu with the same items, Features and Learn as accordions, plus Log in and Start now. [closed](screenshots/mobile-home-default.png), [open](screenshots/mobile-home-menu.png).

## Menus

Features is a mega menu: product links, a What's new card (Introducing Eli), and docs links. [desktop](screenshots/home-menu-features.png), [phone](screenshots/mobile-home-menu-features.png).

Learn is a mega menu: Get inspired, Designers, Help center, Blog, Discord, and the two app badges. [desktop](screenshots/home-menu-learn.png), [phone](screenshots/mobile-home-menu-learn.png).

Neither trigger navigates. Their hrefs are `#features` and `#learn`.

## Search

Search is a page at `/search`, not a dialog. Empty query shows "No matching results." The field was not filled and Search was not submitted. [shot](screenshots/home-search.png).

## Marketing page

A dark hero, a white pill, then a product rail, audience sections, an FAQ accordion, and an ink footer. Pricing uses the same shell, a yearly/monthly pill toggle, and two plan cards. The toggle was not clicked. [pricing](screenshots/pricing-default.png).

FAQ questions on the home page open in place. They do not navigate.

## Footer

Ink ground, four link columns (Product, Learn, Compare, plus social and legal). Footer type is paper at 50% opacity, weight 400. Destinations are listed in [site-tree.md](site-tree.md). Off-site hosts (docs, help, jobs, status, trust, Discord, stores) were not walked.

## Auth wall

Log in leaves fourthwall.com for `my-shop.fourthwall.com`, then Keycloak at `auth.fourthwall.com`. The empty form asks for Google, Apple, email and password. Start now and `/get-started` land on the registration wall: Google, Apple, or email. `/login` starts a download and does not paint.

The branch stopped on the empty wall. [login](screenshots/auth-login-desktop.png), [phone login](screenshots/auth-login-mobile.png), [registration](screenshots/get-started-default.png), [login-review.json](login-review.json).

## What was not entered

Signed-in dashboard, onboarding, checkout, newsletter, plan picker and survey. Chat was not opened past the bubble. No message was sent.
