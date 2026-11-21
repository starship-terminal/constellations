# Flighty

A public marketing site for a flight tracker. The homepage is white. A blue promo strip sits above a black wordmark. Pricing paints black with a purple plan button.

This file is hand-written. `make design-md` needs a catalog entry, and this PR does not edit catalog.json.

## Themes

Light is the homepage. Dark in the tokens is the pricing page and the 404 page, not a theme switch.

| Role | Light | Dark |
|---|---|---|
| page | #ffffff | #000000 |
| text | #000000 | #ffffff |
| muted | rgba(0, 0, 0, 0.65) | |
| banner | #12128c | |
| accent | #bf59f2 | #bf59f2 |

## Type

system-ui, then -apple-system, Segoe UI, Roboto, and the rest of the measured stack. Homepage h1 is 65px weight 700, line-height 78px, letter-spacing -1px. Nav labels are 15px weight 500. Body lede is 17px weight 500. The try button label is 17px weight 600.

## Geometry

Promo strip 39px. Get the app is 32px tall, radius 999px. Give Flighty a try is 44px tall, radius 40px. Try it for free is 40px tall, radius 50px, fill #bf59f2.

## Provenance

Captured 2026-11-21 from https://flighty.com, signed out, in headless Chromium. Desktop CSS viewport 1440x900 at devicePixelRatio 2. Phone homepage 390x844 at devicePixelRatio 2. Get the app dialog opened and closed. No form submitted.
