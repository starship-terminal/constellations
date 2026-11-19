# Meiro patterns

How the measured components combine. Screenshots are the 1440×900 viewport unless the name starts with `mobile-`.

## Marketing chrome

A 1440×84 header, fill `page` (#0e0f0f), bottom radius 24px. The wordmark sits at the left. A nav pill, fill `surface` (#171818), radius 18px, padding 5px, holds Features, Use cases, Resources and Pricing in TT Hoves Medium 16/20, white. Login is a ghost control. Get started is the lime pill. At 390 the nav pill is gone and one 48px menu button sits at the right of a 72px header.

See [home-dark-default](screenshots/home-dark-default.png) and [mobile-home-dark-default](screenshots/mobile-home-dark-default.png).

## Hero

Display type is TT Hoves DemiBold 50/70, white, in two lines, with small inline illustrations between the words. The supporting line is TT Hoves Regular 20/30, `muted` (#ced1d1), 620px wide. The action is the lime pill, 56px tall. Under it, two notes at 15/21 in `muted`: a 10-day trial, and no card required. At 390 the display drops to 34/44.2.

## Pricing

An eyebrow in `accent` at 18/23.4, then the same 50/70 display. A billing control sits under the notes: a selected lime segment and two unselected labels. Three plan cards follow at 332px. The price is 34/47.6 white, the unit is 22/30.8 in `muted`, and the save line is `accent`. Each card ends in Start for free.

See [pricing-dark-default](screenshots/pricing-dark-default.png) and [pricing-dark-monthly](screenshots/pricing-dark-monthly.png).

## Use-case page

Same chrome and hero rhythm. The eyebrow names the audience (Meiro for Marketing) in `accent`. A numbered list of claims follows, index in `muted-soft` at 12px, title in DemiBold 20/26.

See [use-cases-marketing-dark-default](screenshots/use-cases-marketing-dark-default.png).

## Legal page

Same chrome. The title is the 50/70 display. Body copy is TT Hoves Regular 18/27 in `muted`. Links in the copy are the same size in `accent`.

See [privacy-dark-default](screenshots/privacy-dark-default.png), [terms-dark-default](screenshots/terms-dark-default.png), [refund-dark-default](screenshots/refund-dark-default.png).

## Sign-in

The app paints `page` full bleed, the wordmark centered, then a 520×370 card, fill `surface`, radius 30px, padding 30px 40px 40px. Title is TT Hoves 24/34 white. The email field, the lime-deep email button, an OR rule, and the Google button stack at 440×50. Legal links sit under the card at 13px in `muted-soft`.

Nothing was submitted. Continue with email was not pressed, so the next step of sign-up was not captured.

See [login-dark-default](screenshots/login-dark-default.png) and [mobile-login-dark-default](screenshots/mobile-login-dark-default.png).

## Reset and missing page

Forgot-password keeps the card and swaps the title and the button (Reset password, marketing lime). Reset-password, reached with no token, shows a new-password form and a Ready button. The app 404 is a centered 48px lime "404", a 32px title, and two buttons.

See [forgot-password-dark-default](screenshots/forgot-password-dark-default.png), [reset-password-dark-default](screenshots/reset-password-dark-default.png), [not-found-dark-default](screenshots/not-found-dark-default.png).

## What was not reached

The builder, a challenge, analytics, billing checkout, and any signed-in screen sit behind the sign-in card. Checkout was not opened. No card, phone, or identity was entered. Help Center (help.meiro.cc) returned Cloudflare error 1014 and was not captured. The roadmap at updates.meiro.cc is a Frill page, a different product, and was not captured.
