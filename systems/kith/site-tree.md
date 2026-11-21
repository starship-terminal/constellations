# Kith public site tree

Mapped signed out on 2026-11-22 from [https://kith.com](https://kith.com). The first paint was the live shop, title "Kith – Homepage". Desktop viewport measured 1440 by 900 CSS pixels, `devicePixelRatio` 2. The page is a live store, not a parked domain and not a captcha wall.

A welcome dialog offered shipping from the United States, localized currency, and duty paid at checkout. Shop kith.com was clicked. That closed the dialog. It did not submit a form.

Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider was clicked. No captcha was solved. Select a size was not clicked. Add to cart was not reached. Cart was not opened. Account was not opened. Search was not submitted. Newsletter Continue and Submit were not clicked. `login-extracted` was not flipped. `catalog.json` and `webapps-manifest.json` were left alone. origin/main had no `systems/kith/`.

Tracking query strings are not recorded. Prices on the photographed pages were shown in SGD. The currency picker was not submitted.

## Header

`s-header`, 66px, padding 18px 24px. On the homepage it is fixed and transparent, labels white, over the hero. On interior pages it paints `#ffffff` with labels `#333333`. Nav labels are 12px Proxima Nova, weight 500, uppercase, letter-spacing 3px. The logo is an inline SVG, 54 by 23, class `icon--site-logo`. Account, Search, and Cart are 20px icon buttons.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Logo | link | `/` | photographed |
| New | button, drawer | drawer panel | read from the DOM. Not opened. |
| Mens | button, drawer | drawer panel | opened. Explore Mens was not followed. |
| Womens | button, drawer | drawer panel | read from the DOM. Not opened. |
| Kids | button, drawer | drawer panel | read from the DOM. Not opened. |
| Gifting | button, drawer | drawer panel | read from the DOM. Not opened. |
| End of Season Event | button, drawer | drawer panel | read from the DOM. Not opened. |
| Hospitality | button, drawer | drawer panel | read from the DOM. Not opened. |
| Account | button | account drawer | not opened. Login and signup wall. Stop. |
| Search | button | search drawer | not opened. Not submitted. |
| Cart, 0 items | button | cart drawer | not opened. Checkout stop. |

The drawer is 375px, white, opening under the header. Mens was opened and closed. Its top row, read while open: Explore Mens (`/pages/shop-mens`), Kith, Kith Ivy, Kith Records (`/collections/kith-records`), Kith Palette (`/collections/kith-palette`), New Arrivals, Footwear, Apparel, Accessories, Lifestyle (`/collections/mens-lifestyle`), Brands, and a feature card for Kith for the New York Knicks 2026 (`/collections/kith-for-the-new-york-knicks-2026`). Nested carets were not opened.

New, read from the DOM: Kith, Shop All, Brands (`/pages/brands`), Kith Classics (`/collections/kith-origins`), Disney | Kith Kids 15th Anniversary Collection (`/collections/disney-kith-kids-15th-anniversary-collection`).

Womens, read from the DOM: Explore Womens (`/pages/shop-womens`), Kith Women, Kith Ivy for Wilson Women, Kith Women Palette | Active, New Arrivals, Footwear, Apparel, Accessories, Lifestyle (`/collections/womens-lifestyle`), Brands, Kith Women for the New York Knicks 2026 (`/collections/kith-women-for-the-new-york-knicks-2026`).

Kids, read from the DOM: Explore Kids & Baby (`/pages/shop-kids`), Collections, Kith Kids, Kith Baby, Kith Kids Palette, Footwear (`/collections/kids-footwear`), Brands, Disney | Kith Kids 15th Anniversary Collection.

Gifting, read from the DOM: Gifts for Him (`/collections/gifts-for-him`), Kids & Baby Gifts (`/collections/kids-gifts`), Home Gifts & Books (`/collections/home-gifts`), Fragrance & Wellness Gifts (`/collections/fragrance-gifts-mb`), Stocking Stuffers (`/collections/stocking-stuffers`), Kith Gifts (`/collections/kith-gifts`). Gifts for Her was in an earlier DOM pass and was not in the top list of this pass.

End of Season Event, read from the DOM: Shop All Sale (`/collections/ea-end-of-season-event`), Mens Apparel, Mens Accessories, Womens Apparel, Womens Accessories, Footwear, Lifestyle, End of Season Event (`/collections/end-of-season-event`).

Hospitality, read from the DOM: Ronnie's Pronto Truck (`/pages/ronnie-s-pronto-truck`), Ronnie's Pronto (`/pages/ronnies-pronto`), Ronnie's (`/pages/ronnies-london`), Kith Ivy (`/pages/kith-ivy`), Treats (`/pages/treats-locations`), The Tonic Bar by Erewhon at Kith Women, PlantShed (`/pages/plantshed`), Sadelle's at Kith (`/pages/sadelles`). These pages can print a street address. Not opened.

Below the department list the drawer also holds Blog, Locations, Kith Treats, Social, Kith App (`/pages/kith-app`), Kinnect Foundation (`https://kinnectfoundation.org/`), and Kith Support. Blog, Locations, Kith Treats, and Social were read from the DOM and not opened. Locations and Kith Support can print a street address or a phone number. Not opened.

A site and currency picker sits in the drawer: Kith.com, Kith Canada, Kith Europe, Kith Japan, Kith UK, and a currency list. Not submitted.

## Footer

`footer.site-footer`, background `#f2f2f2`, padding 30px 24px, text `#333333`. Column headings are 10px, weight 700, uppercase. Not photographed, because Join our list sits in the first column and Submit was not clicked.

| Control | Destination | This pass |
|---|---|---|
| Text with us | SMS signup | not clicked. Stop. |
| Email | newsletter field | not typed. Stop. |
| Submit | submits the newsletter | not clicked. Stop. |
| About | `/pages/about` | photographed |
| FAQs | `/pages/faq` | followed. It left kith.com for the help center. Not photographed. |
| The Kith Loyalty Program | `/pages/kith-loyalty-program` | not opened. Signup wall. Stop. |
| Discover | `/blogs/discover` | not opened |
| Locations | `/pages/locations` | not opened. Can print street addresses. |
| Contact Us | `https://kithnyc.gorgias.help/en-US` | not opened. Contact pages can print a phone or address. |
| Kith Support | support drawer | not opened |
| Kith App | `/pages/kith-app` | not opened |
| Cookie Policy | `/pages/cookie-policy` | not opened |
| Privacy Statement | `/pages/privacy-policy` | not opened |
| California Privacy Statement | `/pages/california-privacy-statement` | not opened |
| Terms & Conditions | `/pages/terms-and-conditions` | not opened |
| Accessibility Statement | `/pages/accessibility-statement` | not opened |
| Data Request Form | `https://preferences.kith.com/` | not opened. Form. Stop. |
| Right of Withdrawal | Global-e help | external. Not opened. |
| Recall | `/pages/recall` | not opened |
| Instagram, Facebook, Twitter / X, Vimeo, TikTok, YouTube | external profiles | not opened |

## Pages photographed

| Page | URL |
|---|---|
| Homepage | `https://kith.com/` |
| Kith Winter 2026 | `https://kith.com/collections/kith-winter-2026` |
| Disney \| Kith Kids Woody Jacket | `https://kith.com/collections/disney-kith-kids-15th-anniversary-collection/products/khka010105-3029` |
| About | `https://kith.com/pages/about` |

## Where the walk stopped

Login and signup (Account, Loyalty Program), cart and checkout (Cart, Select a size, Add to cart), search submit, newsletter and SMS signup, the data request form, contact, locations, and hospitality pages that can print a street address. The welcome dialog was closed with Shop kith.com. A later newsletter popup was closed without typing. No second regional store was opened.
