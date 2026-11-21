# Sonarworks patterns

How the public site combines the components. Screenshots are in [screenshots/](screenshots). The control map is [site-tree.md](site-tree.md).

## App shell

A black utility bar (56px) sits above a black primary row (104px at 1440). The utility bar holds Reviews, Blog, Help & Support, Company, and Log in. The primary row holds the wordmark, five product tabs, and Cart. Hovering Company opens a `#1e1f20` menu. Hovering a product tab opens a secondary bar. See [home-light-default](screenshots/home-light-default.png) and [home-light-company-menu](screenshots/home-light-company-menu.png).

At 390 the utility bar hides. Menu (`#menu-open-button`) sets the hash `#mobile-navigation` and reveals the same links. See [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).

## Hero and product cards

The home hero is a 44px Inter headline on white, then a three-column band of product cards. Each card is a photo with a title, a one-line description, and a Learn More pill (white on dark photos, black on the light card). See [home-light-default](screenshots/home-light-default.png).

## Pricing

The Pricing control goes to `/soundid-reference/pricing`, which redirected to `/black-friday` on 2026-11-21. The page is a sale grid of Buy now buttons. Those buttons were not followed. See [pricing-light-default](screenshots/pricing-light-default.png).

## Form

Contact is a dark form: email, title, message, Cancel, Send the message, and a captcha. It was not filled and not submitted. See [contacts-light-default](screenshots/contacts-light-default.png).

Login is a split wall: social buttons (Facebook, Google, Apple) and empty email and password fields on the left, an account-benefit list and Sign up on the right. The branch stops there. See [login-light-wall](screenshots/login-light-wall.png).

## List and search

Blog and reviews are published lists. Integrations, ebooks, and enabled devices are published catalogs. The store is a Shopify catalog. The cart was empty. No search query was typed.

## Empty, loading, error

The empty cart is the only empty state captured ([cart-light-default](screenshots/cart-light-default.png)). No loading skeleton and no error page were reached. Support (`support.sonarworks.com`) returned a Cloudflare challenge and was not captured.

## Onboarding and destructive confirmation

Not present on the public site. Account onboarding is behind `/account/signup`, which was not opened.
