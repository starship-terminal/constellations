# Patterns

Public Pedestal pages, light theme, 2026-11-19. Screenshots were not saved. The preview browser returned "The browser is not producing screenshot frames" on `preview_snapshot`.

## App shell

A fixed header, 48px, sits over the page. On the home hero its type is white and its background is transparent. The stylesheet default, used once the hero is gone, is page white (`#fafafa`) and ink (`#212121`). Left to right: the wordmark, Configure, four menu buttons, search, Universe, Cart. The wordmark is an inline SVG, 106 by 27 CSS pixels.

The footer holds a newsletter field (Email plus Notify me), a language select, and policy links. It was not the source of the token colours. Body copy under the footer still inherits the page ink.

## Home

Hero type is FK Display at 160px, white, letter-spacing -6.4px, one line per slide ("New colours. Same iconic silhouette"). A blue action sits at the bottom of the hero. Product notify buttons (ink, 74px) sit in the slide chrome. No dark theme toggle exists.

## Collection

All TV Stands. The title is FK Display 56px, capitalized, with a small count. Products are a radius-0 grid. Sort and Filters are square tiles at the edge of the grid. Filtering was not applied.

## Product

Viva, Bubble Gum. Title is FK Display 32px. Colour name is Suisse Intl 15px weight 600, capitalized. Colour chips are 24px circles. The selected chip is wider. Add to cart is the blue 74px button with the price in the same control. A shipping line sits above it. The form was not submitted.

## Cart

Empty drawer, not a full page, even at `/cart`. Title "Your cart" is Suisse Intl 19px weight 500. "Your cart is empty" is the same size at weight 400. The helper line is ink at 45%. A terms checkbox sits above a blue Checkout button. Checkout was not opened.

## Contact

Title "Contact" is FK Display 56px. The form is two pairs of 74px fields (Name, Order number, Email, Phone number) and a 154px Message area, then an ink Send button. Required fields are marked in the label. The form was not submitted. No validation error was shown.

## Account

`/account/login` leaves `www.pedestal.com` for Shopify Customer Account on `shopify.com`. That page is email plus a code. After the code, Orders is an empty welcome ("Ready to shop?") in Helvetica Neue on `#f6f6f6`. It does not use FK Display or Suisse Intl. Profile exists as a link and was not opened.

## What was not entered

No checkout, no card, no phone number, no address, no contact submit, no newsletter submit. The Shopify marketing checkbox was pre-checked and was unchecked before the email was sent.
