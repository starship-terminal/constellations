# Patterns

Public signed-out pages only. No screenshots: the preview browser did not produce frames.

## App shell

The marketing shell is an announcement strip plus a sticky nav. At 1440 the strip is 50px and the nav is 77px, background `rgba(255, 255, 255, 0.867)`, shadow `rgba(0, 0, 0, 0.02) 0px 1.9px 2.2px, rgba(0, 0, 0, 0.05) 0px 4.5px 5.3px`. Nav items are Platform, Solutions, Pricing, Resources, Customers, Company, then Get started, Request a demo and Log In. The bar content width is 1320 inside a 1440 page, with 60px side inset.

At innerWidth 390 the expense-page h1 drops from 40/50 (desktop on that page) to 25/30. The hamburger was not isolated.

## Hero

Homepage h1 is Sanomat 600, 45/54, `rgb(21, 0, 44)`: "Business travel & expense management. Solved." Under it, a prompt at Inter 300, 21/30, then six choice tiles. Unselected tiles are `rgb(240, 240, 255)`; the two that painted selected are `rgb(225, 226, 254)`. Tiles are 80px tall, radius 12px, label 15px ink.

## Pricing

Two plan cards sit in a row with `gap` 32px (`gap-x-8`). Navan Business says Free and links to `/get-started?source=Pricing`. Navan Enterprise says Let's talk and offers "Get a price quote". The quote control was not followed.

## FAQ

"Frequently Asked Questions" is Inter 700 at 28px. Each question is a button, Inter 300 at 19/25, ink `rgb(21, 0, 44)`. None was expanded, so the open answer style is a gap.

## Footer

Desktop footer is `rgb(21, 0, 44)`, padding-top 48px, 1095px tall on the pricing page. Links are white 13px weight 300.

## Sign-in boundary

`/signin` redirects to `login.navan.com` and paints "Welcome to Navan!" over `rgb(245, 245, 248)`. The form asks for an email, then Continue, a passkey button, Google and Apple. The email field was not filled. Continue, Google, Apple and the passkey button were not pressed. "Get started" on that page points at a signup URL and was not opened.

## Empty, loading, error, destructive

Not present on the marketing pages. The identifier page keeps error strings in the DOM at `display: none`. No destructive confirmation exists on these surfaces.
