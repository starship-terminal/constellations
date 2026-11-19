# Patterns

Public signed-out Resend, 2026-11-19, CSS viewport 1169 by 731. No screenshots: preview frames failed.

## Marketing shell

https://resend.com/ uses a sticky header, 58px, transparent, with an after-element class that can blur (`after:bg-black/60 after:backdrop-blur-md`) at opacity 0 at rest. Header text is Inter. Nav items are 14px / 500, `#a1a4a5`. "Log in" is a ghost 16px-radius button. "Get started" is the glass primary. The page background is `#000000`. `meta theme-color` is `#000000`.

The hero `h1` is Domaine, 96px / 400 / 96px, letter-spacing -0.96px, colour `#f0f0f0`, text "Email for developers". The lede under it is Inter 18px / 400 / 27px, `#a1a4a5`. Section `h2`s are aBCFavorit, 56px / 400 / 67.2px, letter-spacing -2.8px. A code sample uses Commit Mono Website at 14px, colour `#ebeced`, padding 16px 10px 16px 0.

The same black shell is on https://resend.com/pricing, https://resend.com/brand, https://resend.com/login and https://resend.com/signup.

## Pricing

https://resend.com/pricing opens with a Domaine `h1` at 76.8px. Four plan cards sit in a row at this width: Free $0 / mo, Pro $20 / mo, Scale $90 / mo, Custom Enterprise. Each card is 271px wide with 24px padding and a 16px radius. A volume control (3,000 through 3,000,000+) sits above the cards. No month/year switch was found in the button list.

## Auth

https://resend.com/login is a centered column on `#000000`. The `h1` is aBCFavorit 28px / 500 / 34px, letter-spacing -0.72px, "Log in to Resend". Google and GitHub buttons sit side by side at 248px, then an "or" divider, then email and password at 512px, then a full-width "Log In". Legal links point at /legal/terms-of-service and /legal/privacy-policy. Nothing was submitted.

https://resend.com/signup matches that column and adds password rules and a promo checkbox. "Create account" stays disabled (opacity 0.3) until the password meets both rules. Filling the fields enabled the button. The fields were then cleared. The form was not submitted.

## Docs

https://resend.com/docs redirects to https://resend.com/docs/introduction. The docs shell is a different product surface: Inter, page background `#09090b` in dark, main `#000000`, `h1` 36px / 600 `#dedede`. A left nav holds "Sign In" and "Get Started". Search is a button, "Search... ⌘K". Theme buttons are labelled "Switch to system theme", "Switch to light theme" and "Switch to dark theme". Light was clicked, measured, and dark was restored. An assistant panel is in the page. It was not used.

## Brand

https://resend.com/brand is the same marketing shell. It states the name rule ("Resend" with a capital R), offers logo SVG and PNG downloads, and prints the company address "2261 Market Street #5039, San Francisco, CA 94114". That address is published on the page. It is not a private reading. Logo files were not downloaded into this package.

## What was not entered

The signed-in dashboard, API key creation, billing, a card form, Google, and GitHub were not opened. A Stripe hCaptcha iframe is present on signup and was not interacted with.
