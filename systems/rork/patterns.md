# Patterns

Public pages on rork.com, 19 November 2026. Desktop shots are 1440 by 900 CSS pixels, saved at 2x. The phone shot is 390 by 844 CSS pixels, saved at 2x.

The 2026-11-22 public tree is [site-tree.md](site-tree.md). Those shots use the `public-`, `nav-`, and `login-wall-` names in [screenshots/](screenshots/). The shots below are the 19 November set.

## Home

A centered wordmark, a short nav (Products, Resources, Pricing, App), and a white Sign in pill. The hero is "Be the next app founder" at 60px. Under it sits a 768px composer and a row of platform chips. A phone mock sits at the bottom of the first viewport.

[home-dark-default.png](screenshots/home-dark-default.png)

At 390px the hero drops to 48px and the nav collapses to a menu button. Sign in stays a white pill.

[home-dark-phone.png](screenshots/home-dark-phone.png)

## Sign in

The dialog opens over the home page. The first step lists Continue with Google, GitHub, Apple, and email. The email step asks for an address and says it will send a 6-digit code. That request was not sent.

[login-dark-providers.png](screenshots/login-dark-providers.png)

[login-dark-email.png](screenshots/login-dark-email.png)

`/auth` paints the same dialog. `/sign-in` and `/app` redirect to `/?next=…` and stay signed out.

## Pricing

`/pricing` opens a dialog, "Choose your Rork.", with Free ($0), Rork Pro ($20/mo), and Rork Max ($200/mo). Max is the orange card. The Upgrade buttons were not clicked.

[pricing-dark-default.png](screenshots/pricing-dark-default.png)

## FAQ, blog, Max, founders, reviews

| Page | Shot |
|---|---|
| FAQ | [faq-dark-default.png](screenshots/faq-dark-default.png), open row [faq-dark-open.png](screenshots/faq-dark-open.png) |
| Blog | [blog-dark-default.png](screenshots/blog-dark-default.png) |
| Max | [max-dark-default.png](screenshots/max-dark-default.png) |
| Founders | [founders-dark-default.png](screenshots/founders-dark-default.png) |
| Reviews | [reviews-dark-default.png](screenshots/reviews-dark-default.png) |

## Not entered

Google, GitHub, and Apple were not used. No email was submitted. No card, phone number, or checkout was opened. The signed-in builder was not reached.
