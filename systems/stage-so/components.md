# Components

The only product at stage.so on 19 November 2026 is a Spaceship domain listing. These are the controls on that page. Crops are cut from [screenshots/listing-desktop-default.png](screenshots/listing-desktop-default.png).

## Button

The Next control is `.domain__card-payment-cta`. It is 40px tall, radius 24px, padding 0 14px, background `#394eff`, text `#ffffff`, weight 700, size 16px. Focus and hover in headless Chromium left the background, shadow and outline unchanged (`outline: rgb(255, 255, 255) none 0px`).

![Next](components/crops/button-primary-default.png)

A disabled Submit offer button sits in a closed modal at 0×0. It was not opened. Its computed background was the same `#394eff`.

## Radio

Buy now is selected. Make offer is not. Each mark is `.gb-radio__mark`, 16×16, radius 9999px, white fill. The selected mark has a 5px solid `#394eff` outline. The resting mark has a 1px solid `rgba(7, 7, 12, 0.21)` outline. Labels are 16px weight 700, color `#575758`.

![Selected radio](components/crops/radio-selected.png)

## Link

"spaceship.com" in the caption is an anchor to https://www.spaceship.com/. Resting color is `rgba(255, 255, 255, 0.7)` with no underline. Hover adds `text-decoration-line: underline` and does not change the color.

## Text field

The offer amount `#offer-price-input` is on the card. At preview width 1169 it is 32px, weight 700, color `#2b2b2d`, no border. At headless 1440 it computed 38px. The dollar prefix is `#cbcbcc`. The offer modal fields (`#first-name-field`, `#last-name-field`, `#email-field`, `#phone-input`) are in the DOM at 0×0 with radius 8px and padding 0 12px. They were not shown.

## Card

`.domain__card` is white, radius 16px at 1169 and 1440, radius 8px at 390, with the measured inset and drop shadow. Padding is 24px at 1169, 24px 32px at 1440, and 0 16px 16px at 390. The "GET THIS DOMAIN" kicker is 14px, weight 500, letter-spacing 4px, uppercase. It is hidden at 390.

![Card](components/crops/card-default.png)

## Wordmark

The header image is the Spaceship logo, 165×28 CSS px, from the listing CDN. It is not a Stage.so mark.

![Wordmark](components/crops/wordmark-default.png)

## Gaps

- No Stage.so button, field, nav, dialog, toast, table, avatar, badge, tabs, menu, tooltip, checkbox, switch, or select was on the page.
- Hover and focus did not change the Next button's computed background. A pressed state was not measured.
- The offer modal, checkout, and any error, empty, or loading state were not opened.
- Dark and light theme toggles are not on the page. `color-scheme` on the root was `normal`.
- Reduced motion was not emulated. Computed transitions at rest were 0s.
