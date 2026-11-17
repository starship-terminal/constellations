# Patterns

How the public Lemon Squeezy pages are put together. Captured 2026-11-18, signed out.

## Marketing shell

A yellow banner sits above a purple nav. The banner is the shutdown notice. The nav holds the wordmark, Docs, Help, Sign in, and a white pill. On a 390px width the links collapse into a hamburger. The menu opens over the hero and lists Docs, Help and Sign in.

The hero is a full-width `--purple-600` band. The headline is Circular Pro Book, 80px, white. The primary action is a frosted white pill. Hover turns that pill yellow.

Below the hero the home page is a light FAQ: numbered questions, purple on hover and when open. The footer is the same purple as the hero, with muted white legal links.

[home](screenshots/home-light-default.png) [home full](screenshots/home-light-full.png) [mobile menu](screenshots/mobile-home-light-menu.png)

## Pricing

One published price, "5% + 50¢", on a light page with the same shell. Feature rows and a FAQ follow. There is no plan switcher and no checkout on this page.

[pricing](screenshots/pricing-light-default.png)

## Docs

docs.lemonsqueezy.com is a Mintlify site. It reuses the marketing banner and purple header, then a documentation bar (Documentation, Migration, Docs, API, Guides, search). The sidebar is a list of text rows. The selected row gets a grey fill (`#f7f7f8`).

[docs](screenshots/docs-light-default.png) [search](screenshots/docs-help-light-search.png)

## Sign-in card

auth.lemonsqueezy.com/login is a centred card on white. Lemon mark, then Google and Twitter buttons, an "Or" divider, email, password, a purple submit, a remember-me checkbox, and three text links. The card was measured at rest. Nothing was submitted. OAuth was not followed.

The register route redirects to a business-intent step: name, website, country select, Continue. That step was screenshotted and not submitted.

[login](screenshots/login-light-default.png) [register](screenshots/register-light-default.png)

## What is not here

The dashboard, product editor, payouts, customers, checkout and any confirmation live behind sign-in or a submit. They are listed in the catalog `capture.gaps` and were not captured.
