# Spyglass patterns

## Marketing header

A fixed header, 59px at 1440. Wordmark on the left, pill nav in the centre (Product, Individuals, Businesses, Resources, Company), Sign in outline and Get 50% off primary on the right. At 390 the centre nav collapses to a 40px menu button and the primary stays. [home](screenshots/home-light-default.png), [phone](screenshots/home-light-phone.png).

## Prompt hero

Familjen Grotesk h1, a Geist lede, then a rounded prompt card with a submit icon button. Two buttons sit under it: Explore the product (outline) and Get Spyglass 50% off (primary). The prompt was not submitted.

## Pricing

Three plan columns on `/pricing`. The middle plan uses the primary button. The others use the outline button. CTAs link to `/sign-up?planTier=` and were not followed. [pricing](screenshots/pricing-light-default.png).

## FAQ

Category chips, then bordered rows. One row was opened. [faq](screenshots/faq-light-open.png).

## Sign-in

Split page. Left column is the form: Google, an or divider, email, disabled Continue, terms links, and a sign-up link. Right column is a product demo carousel. Email was not entered. Google was not clicked. [sign-in](screenshots/sign-in-light-default.png).

## Footer

A `#292929` panel, radius 8px, with six link columns. Link text is white at 80%. [pricing](screenshots/pricing-light-default.png) shows it at the bottom.

## Missing route

`/this-page-does-not-exist-capture` returns HTTP 404 as a plain text page, not the marketing shell. [missing](screenshots/missing-light-default.png).
