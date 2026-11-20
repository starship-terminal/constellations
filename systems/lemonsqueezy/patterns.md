# Patterns

How the public Lemon Squeezy pages are put together. Captured 2026-11-18. The dashboard was not reached: new store signups are closed.

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

auth.lemonsqueezy.com/login is a centred card on white. Lemon mark, then Google and Twitter buttons, an "Or" divider, email, password, a purple submit, a remember-me checkbox, and three text links. OAuth was not followed.

A failed email/password submit paints a single red sentence under the email field: "These credentials do not match our records." The colour is `#f53d6b` (`--red-500`).

The register route redirects to a business-intent step: name, website, country select, Continue. Website URL is required. An empty submit shows the browser's native "Please fill out this field" tooltip.

[login](screenshots/login-light-default.png) [login error](screenshots/login-light-error.png) [register](screenshots/register-light-default.png) [register validation](screenshots/register-light-validation.png)

## Closed signup

Submitting the business-intent step with a testing name and `https://example.com` lands on `/signup/smp`. The page says Lemon Squeezy is closed to new store signups and recommends Stripe Managed Payments. The purple card has a "Get started" CTA. That CTA was measured and not followed.

[closed signup](screenshots/register-smp-light-default.png) [mobile](screenshots/mobile-register-smp-light-full.png)

## Customer orders login

app.lemonsqueezy.com/my-orders is a buyer portal. Unsigned, it shows a left-aligned "My Orders / Sign In" form and offers a magic link. The form was not submitted.

[my orders](screenshots/my-orders-light-default.png)

## What is not here

Products, orders, customers, settings and the rest of the merchant dashboard sit behind a store account. New store signups are closed, so those pages bounce to the merchant login and were not opened. Stripe Managed Payments onboarding, bank connect and payout KYC were not followed.
