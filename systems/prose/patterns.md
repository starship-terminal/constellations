# Patterns

Public signed-out pages, measured 2026-11-19. No page screenshots: preview_snapshot failed with "The browser is not producing screenshot frames."

## Home

prose.com paints a 40px sale banner (#323429, 12px white text) over a 55px white nav. The hero heading is Saol light, 40px at 1440 and 32px at 390, colour #fff on desktop and #323429 on the phone. A promo dialog (radius 10px, cream #f9f7f2, max-width 340px) offers an email field and an "UNLOCK OFFER" pill. It was closed. The email was not submitted.

The footer is #161716 with 14px white links. One footer link, "Blog", computed as the browser default `rgb(0, 0, 238)` rather than the white used by "Contact us".

## Catalogue and product

/products/haircare titles in Saol 300, 40px, #4d523c. Product tiles are unbordered links. /products/custom-shampoo shows a $11.10 sale price (16px, weight 500, #323429) beside a struck $37.00 (14px, #6c6c6c). The purchase choice is a radio inside a 10px-radius cream card. "GET YOUR FORMULA" leaves the page for /consultation/category. That quiz was not started.

## Consultation gate

/consultation/category offers two 360×129 cards, "Custom Haircare" and "Custom Skincare", radius 10px, border #f1ece0. "Resume here" links to /signin. Neither card was clicked into the quiz.

## Sign-in

/account/nav redirects to /signin?next=/account/nav. The form is one email field on a cream section (#f9f7f2) with a disabled "SIGN IN" pill (#a6a6a6) until an address is entered. No address was entered.

## Subscribe

/the-salon is a marketing page, "COMMIT TO CUSTOM CARE", with the same formula pill and a "SIGN IN" link. No subscription was started.

## Widths

Desktop readings are 1440×900, devicePixelRatio 2, visualViewport scale 1. Phone readings are 390×844, same ratio and scale. The preview resize to 1440 first reported a 1280 viewport; the later computed read confirmed 1440.
