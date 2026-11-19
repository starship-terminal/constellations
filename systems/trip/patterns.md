# Patterns

Public signed-out pages only. No screenshots: see [components.md](components.md).

## Home

`https://sg.trip.com/?locale=en-sg`. White header bar, 66px content height, full width. Logo at the left, 133 by 32 px. Right side: language/currency, Find bookings, and a brand-blue Sign in/register pill (34px tall, radius 4px, padding 8px).

Below that, a hero slogan `.slogan-desc`: "Every check-in is a new beginning", 700 40px/48px Trip Geom, white, on a photo banner whose container computed to `rgb(211, 211, 211)` where the image had not painted as a flat fill. USP line under it is 400 14px/18px white.

The search card sits on the banner: white, radius 16px, the two-layer shadow in `light.shadow.search-card`, width 1096px at 1440. Product tabs across the top, then one field row (destination, dates, guests) and a Search button at the right, 48 by 106 px. A line under the card links "Sign in or register" in brand blue.

The page continues with coupon cards (radius 8px, soft shadow) and a grey footer (`rgb(245, 247, 250)`). Document height was 4615 px at 1440 by 900.

## Hotels

`https://sg.trip.com/hotels/`. Body background `#f6f7fa`. Heading "Hotels" is 700 48px/48px Trip Geom, white, on a banner. The same search row sits under it, wider (about 1097 px), with a 1px `#c5c5c5` border on the field group. Hotel cards follow: image on top, radius 8px, a score line, name, and address. Search was not submitted.

## Customer support

`https://sg.trip.com/pages/support/`. A cyan band (`#047c88`, 316px tall) holds "Customer support" at 700 48px/68px white, and two buttons: Search Bookings (white wireframe, 36px) and Sign in or register (white fill, cyan text `#047c88`). Below the band, FAQ chips in a row (Hot topics, Booking & price, Ticketing & payment, Booking query) on `#f5f7fa`.

## Sign in

`https://sg.trip.com/account/signin`. A two-panel card. Left, white, 474 px: "Sign in/register", an email field, a disabled Continue with email button until the field is valid, then Google (vendor blue `#4285f4`), Apple, and Facebook (white, 1px `#d4d7de` border), each 378 by 56 px, radius 4px. Right, `#f6f7fa`, 384 px: QR instructions. The email field was focused for the border colour and left empty. No provider button was pressed.

## What was not entered

Bookings, checkout, payment, phone verification, and account creation. The Search button was not clicked. Results, filters, and the map were not opened.
