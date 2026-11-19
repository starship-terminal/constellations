# Patterns

Screenshots are viewport captures at the measured CSS size, 1440 by 900 or 390 by 844, saved at 2x and reduced to 256 colours.

## App shell

The signed-out product home is a left nav plus a centered composer. The nav is 240px. The heading reads "What do you want to know?". Sign In sits at the bottom of the nav.

![Product home, light](screenshots/app-light-default.png)

The same page under a dark preference uses the dark token set. A sign-in sheet is also open in that shot.

![Product home, dark](screenshots/app-dark-default.png)

At 390px the nav is hidden behind a menu button. The composer sits at the bottom.

![Product home, phone](screenshots/app-light-phone.png)

![Phone menu open](screenshots/app-light-phone-sidebar.png)

## Marketing home

https://www.perplexity.ai/hub is a photographic hero, "AI for the curious", with See a demo and Try Perplexity in the header. The page background computed to `rgb(250, 248, 245)`. The token `--bg-base` on the same document is `#fbfbfb`.

![Hub](screenshots/hub-light-default.png)

![Hub, phone](screenshots/hub-light-phone.png)

## Pricing

https://www.perplexity.ai/hub/pricing shows Free, Pro, and Max. Prices on the page were $0, $17, and $167 per month when billed annually. Get started and Select were not followed. Get Pro and Get Max were not followed.

![Pricing](screenshots/pricing-light-default.png)

![Plans](screenshots/pricing-light-plans.png)

![Pricing, phone](screenshots/pricing-light-phone.png)

## Sign-in

Sign In opens a dialog. The form asks for an email and also offers Google, Apple, and SSO. Continue with email was not submitted, because the form is not email-only.

![Sign-in dialog](screenshots/signin-light-dialog.png)

## Other public pages

Enterprise, the terms page, and a missing hub route were captured as viewport shots.

![Enterprise](screenshots/enterprise-light-default.png)

![Terms](screenshots/terms-light-default.png)

![404](screenshots/missing-light-default.png)

## Empty

The signed-out sidebar shows "No projects" and "No recent sessions". Those are the empty states that were on the page.

## Loading, error, destructive confirm, search results

Not captured. No query was submitted, and no destructive action was available on the public pages.
