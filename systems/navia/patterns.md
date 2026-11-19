# Navia patterns

Public signed-out surfaces only. Measured 2026-11-19 in the T3 preview browser at 1169 by 731, device pixel ratio 2. Screenshot frames failed, so these notes describe computed layout, not images.

## Marketing home

`https://www.thenavia.com/` (the apex `thenavia.com` redirects here). Cream page `#faf4e6`. A fixed nav, 69px tall, padding `0 58.4453px`, transparent. Logo at the left, links Platform, Pricing, Resources, and a yellow pill, Get started, linking to `app.thenavia.com`.

The hero is white text on a section whose own background computed as transparent. The h1 is Lora, 3.5rem, weight 400, white. A yellow pill and a white pill sit under it. Later sections alternate cream, white (`.section.is-white`) and ink (`.section.is-dark`, white text). A handwriting line, Notemakersmark, yellow, 7rem, letter-spacing -6px, reads over the ink band.

The content column `.container-large` measured 1052px wide, inset 58px, which matches `.padding-global` at 5%.

## Pricing

Three plans in a row on the home page, each 330px. Basic is free, Business is $49/mo on the ink highlight card, Growth is $79/mo. Sign up links go to `app.thenavia.com` and were not followed from the cards.

## Blog and article

`/blog` uses the same cream page and a 5rem Lora title. Article cards link to `/blog/...`. One article was opened. Its title is 4rem Lora, the body column is 849px, Public Sans at 1rem, and inline links are orange.

## Contact

`/contact-us` is a cream page with a 4rem Lora title and a Webflow form. Fields are first name, last name, email, phone, a topic select and a message. The submit is an orange pill with ink text. The form was not filled and not submitted. A phone field is present, so this is not an email-only signup.

## Legal

`/privacy-policy` uses the same cream page, 4rem title and 849px body column. `/terms-and-conditions` is linked from the footer and was not opened. The privacy page already showed the legal pattern.

## App gate

`https://app.thenavia.com/` is a cream screen, centered, max-width card with 32px padding. Lora title at 28px, weight 500, letter-spacing -0.28px. The lede is `#5a544c`. Two buttons: Sign In (white, `#dfd5c0` border) and Sign Up (orange). Neither was pressed. There is no email field on this screen.

## Not captured

- Desktop 1440 and phone 390. The preview tab was a 1169 fill viewport and could not be resized after frames failed.
- Dark theme. The marketing site has a dark nav token set and ink sections. It has no page-level dark theme. The app stylesheet's `.dark` block was not applied.
- Signed-in app, checkout, booking. Book a demo links to a Google Calendar appointment page and was not opened. Get started links to the app gate and was not submitted.
