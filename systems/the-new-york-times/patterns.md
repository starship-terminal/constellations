# Patterns

Signed-out public pages, measured 2026-11-19. No page screenshot exists. [screenshots/home-light-unavailable.png](screenshots/home-light-unavailable.png) is a label.

## Homepage

https://www.nytimes.com/ at innerWidth 1169, innerHeight 731, devicePixelRatio 2.

The first 271px is an advertisement slot, background `#f8f8f8`. Product chrome starts under it.

The masthead is 165px tall, transparent, with 35px of side padding. Edition links sit in a row (U.S. selected). Subscribe and Log in sit at the right in the blue face. The wordmark is a black SVG, 485 by 64, under that row. The date is Franklin 14px `#121212`. Section links (U.S., World, Business, Arts) are Franklin 14px weight 500.

A lead story uses Cheltenham 22px weight 700, `#121212`, with an Imperial 14px summary in `#5a5a5a` and a Franklin 10px uppercase kicker in `#727272`.

Search opens in the masthead as a text field and a GO button in the same blue face. The query was not submitted.

## Subscription offer

https://www.nytimes.com/subscription at the same 1169 viewport. `html` carried `tpl-always-light`.

The painted hero is Cheltenham 48px weight 300, `#363636`, line-height 52.8px: "With unlimited access / comes unlimited discovery."

Monthly and Yearly sit above two offer cards. The sale price is Franklin 18px `#000000`. The struck price is Franklin 18px `#888888`. The billing line is Franklin 14px `#666666`. Continue to checkout is the ink button. It was not followed. No card was entered.

## Login

https://myaccount.nytimes.com/auth/login. Desktop innerWidth 1169. Phone innerWidth 390, innerHeight 844, devicePixelRatio 2.

White page. Cheltenham 30px / 40px title: "Log in or create an account." Email label, empty field, ink Continue, an "or" divider, then Google, Apple, and a work-or-school SSO link. None of those were used. At 390px the card is the full 390px width and Continue is 358px wide. The title size stayed 30px.

## Gaps

- No signed-in article, no paywall body, no checkout.
- Dark theme was declared and not painted.
- 1440 CSS pixels were not reached.
- Reduced motion was not measured.
