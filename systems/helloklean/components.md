# Components

Measured from helloklean.com's public signed-out pages. A crop is the element as painted. A value is the computed style, not a colour read off the PNG.

## Inventory

| Component | Where | Size | Fill | Text | Radius | Crop |
|---|---|---|---|---|---|---|
| logo | home | 206 x 29.84 | rgba(0, 0, 0, 0) | rgb(29, 29, 31) | 0px | [crop](components/crops/logo-default.png) |
| announcement | home | 1440 x 30 | rgb(29, 29, 31) | rgb(255, 255, 255) | 0px | [crop](components/crops/announcement-default.png) |
| nav-cta | home | 56.13 x 18 | rgba(0, 0, 0, 0) | rgb(29, 29, 31) | 0px | [crop](components/crops/nav-cta-default.png) |
| hero-cta | home | 171.08 x 40 | rgb(29, 29, 31) | rgb(245, 244, 241) | 25px | [crop](components/crops/hero-cta-default.png) |
| hero-title | home | 970 x 41.8 | rgba(0, 0, 0, 0) | rgb(29, 29, 31) | 0px | [crop](components/crops/hero-title-default.png) |
| menu-button | home | 22 x 14 | rgba(0, 0, 0, 0) | rgb(0, 0, 0) | 0px | [crop](components/crops/menu-button-default.png) |
| search-button | home | 26 x 30 | rgba(0, 0, 0, 0) | rgb(0, 0, 0) | 0px | [crop](components/crops/search-button-default.png) |
| cart-button | home | 20 x 26 | rgba(0, 0, 0, 0) | rgb(29, 29, 31) | 0px | [crop](components/crops/cart-button-default.png) |
| account-link | home | 18 x 25 | rgba(0, 0, 0, 0) | rgb(29, 29, 31) | 0px | [crop](components/crops/account-link-default.png) |
| product-card | shop | 150.03 x 34 | rgb(245, 244, 241) | rgb(29, 29, 31) | 25px | [crop](components/crops/product-card-default.png) |
| product-title | product | 370 x 33 | rgba(0, 0, 0, 0) | rgb(29, 29, 31) | 0px | [crop](components/crops/product-title-default.png) |
| product-price | product | 92.64 x 14.39 | rgba(0, 0, 0, 0) | rgb(29, 29, 31) | 0px | [crop](components/crops/product-price-default.png) |
| add-to-cart | product | 95.7 x 38 | rgb(245, 244, 241) | rgb(29, 29, 31) | 25px | [crop](components/crops/add-to-cart-default.png) |
| variant | no visible match | | | | | |
| accordion | product | 370 x 58.59 | rgba(0, 0, 0, 0) | rgb(0, 0, 0) | 0px | [crop](components/crops/accordion-default.png) |
| faq-row | faq | 22 x 14 | rgba(0, 0, 0, 0) | rgb(0, 0, 0) | 0px | [crop](components/crops/faq-row-default.png) |
| text-field | contact | 239 x 38 | rgb(245, 244, 241) | rgb(0, 0, 0) | 25px | [crop](components/crops/text-field-default.png) |
| submit | contact | 60.25 x 22 | rgba(0, 0, 0, 0) | rgb(29, 29, 31) | 3px | [crop](components/crops/submit-default.png) |
| footer-link | no visible match | | | | | |
| newsletter-field | home | 400.3 x 38 | rgba(0, 0, 0, 0) | rgb(245, 244, 241) | 0px | [crop](components/crops/newsletter-field-default.png) |
| cart-empty | cart | 1440 x 341.8 | rgba(0, 0, 0, 0) | rgb(29, 29, 31) | 0px | [crop](components/crops/cart-empty-default.png) |

## States

Hover and focus-visible were read where the element accepted them. Pressed states were not forced, so a script-applied active style is not in this file. Disabled, loading and error states do not render on the public pages that were measured.

## Gaps

Several selectors landed on the wrong painted control. Treat the crop as the evidence, not the component name.

- `nav-cta` is the Shop All text link (56 x 18), not the header Shop Skin Filter pill.
- `hero-cta` is the cart's Continue Shopping pill, measured on the cart page, not the home hero's Shop the sale pill.
- `product-card` is the header Shop Skin Filter pill (150 x 34), not a shop-grid card. The grid is in [shop-light-default](screenshots/shop-light-default.png).
- `add-to-cart` is the footer Subscribe pill, not the product Start now control.
- `faq-row` is the hamburger glyph (22 x 14), not an FAQ question. The FAQ row is in [faq-light-default](screenshots/faq-light-default.png).
- `variant` and `footer-link` missed. Colour swatches and supply cards are in [product-light-default](screenshots/product-light-default.png). Footer links are in [cart-light-default](screenshots/cart-light-default.png).
- `text-field` is the contact Name field. The newsletter field is `newsletter-field`.
- Checkbox, radio, switch, tooltip, toast and avatar were not measured as their own entries. The contact form shows a select, a checkbox and a textarea in [contact-light-default](screenshots/contact-light-default.png). Size pills and purchase radios are in [shampoo-light-default](screenshots/shampoo-light-default.png).
- Account screens at account.helloklean.com were opened in the owner's browser and not saved: the preview host stopped producing frames.
- Checkout, payment and address forms were not entered. Consent banners were hidden, never accepted or rejected.

Crops on disk: 57.
