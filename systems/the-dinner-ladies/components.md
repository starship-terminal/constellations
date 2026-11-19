# Components

Public marketing components on dinnerladies.com.au, measured 2026-11-19 at innerWidth 1169. States that were not on the page are gaps. No component crops: the preview browser returned "The browser is not producing screenshot frames".

## Button

Primary links use `a.button.button--primary`. Computed: background `#dd1f26`, text `#ffffff`, Denim SemiBold 15px, weight 600, letter-spacing 1px, uppercase, padding `0 30px`, height 47px, radius 0. The octagon class on OUR MENU paints `#dd1d1d` instead. CONTINUE READING paints `#2b261b`. Transition is `box-shadow 0.1s ease`.

CART is a separate control: `#dd1f26` fill, 15px, padding `10px 20px`, height 37px, radius 5px.

ADD TO CART on the product page is 17px, height 60px, with a 2px `#2b261b` border on the same red fill.

Hover, pressed, disabled and loading were not forced. The skip link and the empty-cart checkout button share the red button style but were not in the visible flow.

## Link

Header items are uppercase 15px, weight 600, letter-spacing 0.3px, padding `12px 8px`, colour `rgba(0, 0, 0, 0.75)`. The computed family is `"Demin SemiBold"`, a misspelling of Denim. Focus shows a 2px `rgba(0, 0, 0, 0.5)` outline and a `rgba(0, 0, 0, 0.3) 0 0 2px` shadow.

## Text field

Header search: background `#fff1e6`, 2px solid `#2b261b`, 20px weight 600, padding `15px 98px 15px 15px`, height 45px, radius 0, placeholder "Search".

Newsletter field in the footer: background `#ffffff`, font Arial 16px, radius 5px, height 45px, placeholder "Enter your email...". It was not filled and not submitted.

Suburb search on `/pages/delivery-info` is present (`address-finder-input`, placeholder "Select your suburb"). It was not typed into.

## Select

Sort on `/collections/all` is a native select (`.select__select`, 12px). Its open menu was not opened. Disabled and error states were not on the page.

## Collection chip

`a.collection-button` is 14px, weight 500, height 27px, padding 4px, 1px solid `#000`, radius 3px. The active chip (ALL DINNERS) fills `#dbe7ef`. Resting chips are transparent.

## Card

`.uf-product-card-wrapper` is a 2px solid `#000` box, radius 0, padding 4px. The title link is Denim SemiBold 20px weight 600. Best Seller is 12px weight 600, transparent background.

## Variant

Size labels on the product page are 17px Denim Medium weight 600, height 75px, padding `16px 0`, 2px solid `#2b261b`, radius 0. Selected fills `#dbe7ef`. Resting fills `#ffffff`. The declared `--variant-pills-radius` of 40px does not paint here.

## Accordion

`.uf__to-cook-accordion` is 38px, 2px solid `#000`, padding 18px, height 84px. It was not opened.

## Badge

Best Seller is text only, 12px. The declared `--badge-corner-radius` of 4rem was not seen on a painted badge.

## Quantity

The product quantity buttons are 45 by 60px, 18px, transparent. They were not pressed.

## Newsletter submit

`.newsletter-form__button` is 12px weight 600, `#dd1f26` fill, white text, padding `10px 15px`, height 31px, radius 5px, label SUBMIT. It was not clicked.

## Gaps

- Hover, pressed, disabled, loading and error were not on the page and were not forced.
- No checkbox, radio (the variant radios are visually hidden), switch, tabs, tooltip, dialog, toast, avatar or table of data. The delivery page has a one-row table whose background is `#fde4d1`.
- The cart drawer, menu drawer and search modal exist in the DOM and were not opened.
- No crops. Screenshot frames were unavailable.
