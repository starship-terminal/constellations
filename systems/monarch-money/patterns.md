# Patterns

How the public Monarch pages are built. The signed-in product is not in this package.

## Marketing frame

Every marketing page opens with a 32px orange announcement strip, then a white pill bar. The bar holds the butterfly wordmark, Features, For Couples, For Professionals, Pricing, Download, a white Sign in pill and an orange Sign up pill. On a phone the links collapse into a menu button and Sign up stays. [Home](screenshots/home-light-default.png), [phone](screenshots/mobile-home-light-default.png).

The page ground is gray 2 (`#f6f5f3`). Display headings are 48px, weight 350, tracking -3.2px. The home hero is a full-bleed photograph with a pale card and an orange pill over it. Headless Chromium cannot play the Mux video in that photograph. The error card was hidden before the shot. The video is not evidence.

## Pricing

Two white plan columns, Core and Plus, beside a product photograph. Core is $8.33/month billed annually. Plus is $16.67/month. Both end in an orange pill, "Try Monarch free for 7 days". That link was measured and not followed. A billing menu sits on the annual price. It was not opened. FAQ rows sit below, closed. [Pricing](screenshots/pricing-light-default.png).

## Sign-in boundary

`https://app.monarch.com/login` is a parchment page with one white card. The card has Sign in, a Stay signed in switch, Continue with Apple, Continue with Google, an email field, a password field, a half-orange Sign in button, and a Sign up link. Nothing was typed. Apple, Google, Forgot password and Sign up were not pressed. [Sign in](screenshots/signin-light-default.png), [phone](screenshots/mobile-signin-light-default.png).

`https://app.monarch.com/signup` is the same wall with an email field that already shows the site's placeholder `email@address.com`, a Sign up with email button, and a product demo image. The form was not filled. The demo image is marketing artwork, not a signed-in capture. [Sign up](screenshots/signup-light-default.png).

## What this frame does not include

Accounts, transactions, budgets, goals, reports, advice, settings, bank linking, checkout and the household app are behind the wall. They are not in these screenshots.
