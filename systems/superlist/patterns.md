# Patterns

## Marketing shell

The home page is a cream page, `rgb(255, 253, 249)`, with a 1200px content column. The desktop nav padding is `26px 50px`. Labels are Haffer XH SemiBold 16px in `rgb(24, 24, 36)`. The wordmark is a raster mark, 28px tall in the header, plus a wordmark vector. "Sign up" is the coral pill. "Sign in" is a text link to `https://app.superlist.com/`.

At 390 the header collapses to a Menu control. That open menu was not captured.

Screenshot: [home-light-default.png](screenshots/home-light-default.png), [home-light-phone.png](screenshots/home-light-phone.png).

## Hero

Eyebrow in Inter 11px, weight 600, letter-spacing 1.5px. Headline is Haffer XH Bold 68px, letter-spacing -3px. Body is Inter 18px, line-height 29.7px, `rgb(89, 87, 92)`. Actions sit in a row with a 24px gap: the coral pill, then "See how it works".

## Feature bands

Sections use 80px padding and an 80px gap. One band is sand, `rgb(240, 238, 234)`. One band is peach, `rgb(250, 238, 231)`. The closing band and the footer are `rgb(24, 24, 36)` with white type.

## Pricing

Three cards, Free, Basic, and Super, on the cream page. Yearly is selected by default and shows a 20% note. Prices read on the page were $0, $5, and $17. Upgrade links point at `https://app.superlist.com/settings/subscriptions`. That page was not opened.

Screenshot: [pricing-light-default.png](screenshots/pricing-light-default.png).

## Signed-out app

`https://app.superlist.com/` redirects to `/inbox` and paints a Flutter canvas. The accessibility tree reads a slide ("Start your next project in seconds using AI templates"), then "Let's get started", "Continue with Apple", and "Continue with email". Email opens a field labelled "Type your email" and a "Send link" button. The link was not sent. Apple was not followed. No screenshot of this surface is in the package: the preview browser did not produce frames, and a headless session was not started against the login.

## Blog and updates

Both keep the cream page and Haffer headlines. Blog h1 at 1440 was 64px, weight 600, letter-spacing -1.92px. Screenshots: [blog-light-default.png](screenshots/blog-light-default.png), [updates-light-default.png](screenshots/updates-light-default.png).
