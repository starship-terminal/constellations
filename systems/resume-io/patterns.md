# Resume.io patterns

Signed-out marketing and the sign-in boundary, measured 2026-11-19. Screenshots are headless Chromium at 1440 by 900 and 390 by 844 after the cookie panel's "Essential only" control was clicked. The T3 preview tab (innerWidth 1169) supplied the computed styles. It could not produce screenshot frames.

## Marketing shell

A white 80px bar holds the wordmark, text links, a blue "Sign in" link, and a blue "Create my resume" button. The page ground is `light.background.page` (`#eff2f9`) on home, pricing, and about. The templates page paints a white ground. Content sits in `--container-width` (1120px).

[home](screenshots/home-light-default.png) leads with a large TT Commons headline, a blue word in the typed line, a primary button, and a pale secondary "Upload my resume" button. The right side is a product illustration, not the signed-in editor.

At 390px the bar collapses to the wordmark and a hamburger. The two hero buttons stack full width. See [home-light-mobile](screenshots/home-light-mobile.png). The menu was not opened.

## Pricing

[pricing](screenshots/pricing-light-default.png) is three white cards on the page ground: $2.95 7-day trial, $49.95 quarterly, $0.00 free plan. The first two cards use the primary button. The free card uses the ghost button. "Build Resume" was not followed. No card number was entered. The phone pass is [pricing-light-mobile](screenshots/pricing-light-mobile.png).

## Templates

[templates](screenshots/templates-light-default.png) is a centered 38px / 700 title, the same two hero buttons, then 36px-radius filter pills on `light.background.sunken`. Template thumbnails are document art inside `.templates-card`. "Use this template" links to `/app/create-resume` and were not followed.

## Other public pages

Examples, about, blog, and the AI builder page share the same bar and footer. The AI builder hero paints a dark indigo ground (`rgb(26, 28, 106)` in the headless shot). That colour was not read as a computed style in the preview tab, so it is not a token. About's h1 computed to 50px / 400 / 52px at innerWidth 1169, also not a declared `--font-*` step.

A missing route renders "Page not found · Resume.io". See [notfound](screenshots/notfound-light-default.png).

## Sign-in

`/app/auth/sign-in` is a centered column, not a card. The first step offers Facebook, Google, LinkedIn, and Email. Email opens a second step with one email field, Back, and Continue. The field was focused. No address was typed. Continue was not pressed. Social links were not followed. The shell uses TT Talent and the builder CSS custom properties (`--spacing-*`, `--font-*`, `--light-shadow-*`).

## Footer

Every marketing page ends in a `#0f141e` band with white link text and muted column titles. That band is the dark colour in this system. There is no theme switch on the signed-out pages.

## What was not entered

Create, upload, template, and pricing CTAs. Checkout. The email Continue button. Social sign-in. help.resume.io. Any download.
