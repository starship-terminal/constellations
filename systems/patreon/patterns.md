# Patterns

Signed-out public pages, measured 2026-11-19. Screenshots were not saved: the preview browser did not produce frames, and headless Playwright hit a Cloudflare challenge.

## Marketing header

On `/`, `/pricing` and `/product/paid-membership` the header is transparent over a pale backdrop of `rgba(255, 255, 255, 0.6)`. At 1440 it holds Creators, Features, Pricing, Resources, Updates, the wordmark, Find a Creator, Log in and Get Started. Nav buttons are 47px tall, radius 30px, white text. Log in is a white outline pill. Get Started is a white fill with black text.

At 390 the same header is 115px tall and shows Open menu, the wordmark, Log in and Get Started. The pills grow to radius 40px and 16px type.

## Hero

The home h1 computed to 187.5px, weight 250, line-height 183.75px, letter-spacing -11.25px, white, at a 7.5px root. The heading's text nodes were empty in the DOM because the words are split across animated spans. Section bands behind the page computed to `rgb(148, 187, 255)`, `rgb(149, 173, 203)` and `rgb(113, 160, 255)`.

At 390 the h1 computed to 64px, line-height 62.72px, letter-spacing -3.84px. `--font-size-h1` at that width was `6.4rem` with a 10px root.

## Pricing

`/pricing` title: "Patreon Pricing Plans — Patreon". H1 "Start Your Patreon for Free" uses the same 187.5px / 250 / -11.25px display style, white. A later h2 "Patreon pricing" is 30px, weight 400, line-height 45px, black. The "10%" figure is 72px, weight 250, letter-spacing -2.88px. The in-page Get started is a black pill, 47px, radius 30px, white text.

## Product page

`/product/paid-membership` uses the same header and the same display h1 ("Fans get more You get paid", white, 187.5px, weight 250). Section fills match the home bands.

## Login wall

`/login` is a different app. Title: "Log in or sign up | Patreon". Page background `rgb(2, 2, 2)`, text white, font ABC Oracle Plus Variable, root font-size 16px. The card is a 400px column: h1 26px / 500, two SSO buttons, an Email field, Continue, and "Need help signing in?". This is the signup wall. It was measured and not submitted.

## Footer

At 390 the site footer is black, padding 48px 34px, white links. Column links are 24px / 300. Social links are 18px / 350. The footer also prints a postal address. That address is not copied here.

## Gaps

App shell after login, forms with validation, empty, loading and error states, destructive confirmation, search results, tables and onboarding sit behind the signup wall or were not rendered. No dark marketing theme was switched on.
