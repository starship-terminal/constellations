# Sephora public site tree

Mapped signed out on 2026-11-22 from [https://www.sephora.com](https://www.sephora.com). The browser stayed on [https://www.sephora.com/](https://www.sephora.com/). Title "Makeup, Skincare, Fragrance, Hair & Beauty Products | Sephora". Viewport 1440 by 900 CSS pixels, `devicePixelRatio` 2. Screenshots are 2880 by 1800.

A geo modal opened over the homepage: "Looks like you are trying to access Sephora.com (USA & Canada) from another country. This site does not ship to your country." The walk closed that modal and stayed on the USA and Canada storefront. Prices on the product page read USD. The page is a live shop, not a parked domain and not a captcha wall. Promo bar background `rgb(81, 2, 130)`. Department bar background `rgb(0, 0, 0)`. Body type is Helvetica Neue, 14px, color `rgb(0, 0, 0)`.

Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider was clicked. No captcha was solved. Add to Basket was not clicked. Sign In was not completed. The basket link points at `/basket` and was not opened. Loves points at `/profile/Lists` and was not opened. Search was not submitted. Email and text signup were not filled. Store locator and same-day delivery were not opened. `login-extracted` stays `not-started`.

`catalog.json` and `webapps-manifest.json` were left alone. origin/main had no `systems/sephora/`.

Tracking query strings (`icid2`, `ref`) are not recorded.

## Promo bar

One purple strip sits above the logo, 60px, full width, background `rgb(81, 2, 130)`, type 14px, white.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| App Exclusive! Save 30% on top brands through 11/22. DOWNLOAD NOW | link | [https://www.sephora.com/beauty/cyber-week-deals](https://www.sephora.com/beauty/cyber-week-deals) | listed, not opened |

## Header

Photographed: [home-light-1440.png](screenshots/home-light-1440.png).

The bar under the promo strip is white. The wordmark is an inline SVG, viewBox `0 0 125 17`, rendered about 147 by 17, fill `rgb(0, 0, 0)`. Saved as [icons/mark.svg](icons/mark.svg). Search is a pill, 318 by 34, fill `rgb(246, 246, 248)`, 1px black border, radius 9999px, placeholder "Search". It was not submitted.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Sephora Homepage | link | [https://www.sephora.com/](https://www.sephora.com/) | home |
| Search | field | typeahead | not submitted |
| AI Beauty Chat | button | not opened | chat wall, stopped |
| Shop Store & Delivery | button | store and location picker | not opened |
| Services & Events | button | not opened | not opened |
| Sign In | button | sign-in dialog | login wall, stopped. The dialog opened once and was closed without typing |
| Loves | link | [https://www.sephora.com/profile/Lists](https://www.sephora.com/profile/Lists) | account wall, not opened |
| Basket | link | [https://www.sephora.com/basket](https://www.sephora.com/basket) | bag wall, not opened |

## Department bar

Black strip, 44px, full width. Labels are white, 14px, weight 400. Sale & Offers is the same white as the other labels. Each item opens a menu. Those menus were read from the DOM, not photographed as separate pages.

| Label | Kind | Destination |
|---|---|---|
| Gifts & Value Sets | link | [https://www.sephora.com/shop/gifts](https://www.sephora.com/shop/gifts) |
| New | link | [https://www.sephora.com/beauty/new-beauty-products](https://www.sephora.com/beauty/new-beauty-products) |
| Makeup | link | [https://www.sephora.com/shop/makeup-cosmetics](https://www.sephora.com/shop/makeup-cosmetics) |
| Skincare | link | [https://www.sephora.com/shop/skincare](https://www.sephora.com/shop/skincare) |
| Fragrance | link | [https://www.sephora.com/shop/fragrance](https://www.sephora.com/shop/fragrance) |
| Hair | link | [https://www.sephora.com/shop/hair-products](https://www.sephora.com/shop/hair-products) |
| Bath & Body | link | [https://www.sephora.com/shop/bath-body](https://www.sephora.com/shop/bath-body) |
| Mini Size | link | [https://www.sephora.com/shop/travel-size-toiletries](https://www.sephora.com/shop/travel-size-toiletries) |
| Brands | link | [https://www.sephora.com/brands-list](https://www.sephora.com/brands-list) |
| Gift Cards | link | [https://www.sephora.com/beauty/giftcards](https://www.sephora.com/beauty/giftcards) |
| Sale & Offers | button | menu, first link [https://www.sephora.com/beauty/cyber-week-deals](https://www.sephora.com/beauty/cyber-week-deals) |

## Pages opened

| Page | URL | Shot |
|---|---|---|
| Homepage | [https://www.sephora.com/](https://www.sephora.com/) | [home-light-1440.png](screenshots/home-light-1440.png) |
| Makeup | [https://www.sephora.com/shop/makeup-cosmetics](https://www.sephora.com/shop/makeup-cosmetics) | [category-light-1440.png](screenshots/category-light-1440.png) |
| Pocket Blush | [https://www.sephora.com/product/pocket-blush-P517483](https://www.sephora.com/product/pocket-blush-P517483) | [product-light-1440.png](screenshots/product-light-1440.png) |
| About Us | [https://www.sephora.com/beauty/about-us](https://www.sephora.com/beauty/about-us) | not photographed. Preview frames stopped. Headless Chromium got Access Denied, so that shot was discarded |

The product page showed Add to Basket, a quantity control, color swatches, and a price of $25.00. Add to Basket was not clicked. The quantity control was not used. Color swatches were not clicked.

## Footer

Read from the homepage footer. Columns include Find a Store, Get the App, Get Sephora Texts, Sephora Credit Card Program, About Sephora, My Sephora, and Help. Region & Language lists United States - English, Canada - English, and Canada - Français. The copyright line reads "© 2026 Sephora USA, Inc."

A customer-service phone number is printed in the footer. It is not copied here. Email signup and text signup were not filled. Order Status, Purchase History, Account Settings, Beauty Insider, credit-card, and rewards links were not opened.

About Sephora in the footer points at [https://www.inside-sephora.com/en/about-sephora](https://www.inside-sephora.com/en/about-sephora). That host was not opened. The on-site About Us page at `/beauty/about-us` was opened instead.

## Menus read, not opened

Counts are unique label and path pairs in the DOM. Samples only.

### Gifts & Value Sets

30 links. Samples: All Gifts, Holiday Gift Guide, Gift Card, Value & Gift Sets, $15 and under, $25 and under, Makeup, Skincare, Hair, Fragrance.

### New

17 links. Samples: All New, Just Dropped, New Makeup, New Skincare, New Hair Care, New Fragrance, Bestsellers, Trending on Social, Clean Beauty.

### Makeup

82 links. Samples: All Makeup, Face, Foundation, Concealer, Eye, Mascara, Lip, Lipstick, Cheek, Blush. The Makeup landing was opened.

### Skincare

79 links. Samples: All Skincare, Moisturizers, Face Creams, Cleansers, Toners, Treatments. Not opened.

### Fragrance

45 links. Samples: All Fragrance, Women, Perfume, Men, Cologne, Value & Gift Sets. Not opened.

### Hair

76 links. Samples: All Hair, Shampoo & Conditioner, Treatments, Styling. Not opened.

### Bath & Body

42 links. Samples: All Bath & Body, Bath & Shower, Body Moisturizers, Sunscreen. Not opened.

### Mini Size

13 links. Samples: All Mini Size, Makeup, Skincare, Hair, Fragrance, Sephora Favorites, Luxe Minis. Not opened.

### Brands

41 links. Samples: Brands A-Z, SEPHORA COLLECTION, rhode, Dior, Kerastase, Summer Fridays. Not opened as a brand index. The rhode product page was opened from Makeup.

### Gift Cards

8 links. Samples: All Gift Cards, Digital Gift Cards (sephora.cashstar.com), Physical Gift Cards, Check Balance. Cashstar was not opened.

### Sale & Offers

9 links. Samples: Cyber Week Deals, All Sale, Makeup, Skincare, Hair Care, Fragrance, Beauty Offers. Not opened.
