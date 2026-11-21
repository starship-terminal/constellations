# Rhone public site tree

Mapped signed out on 2026-11-22 from [https://www.rhone.com/](https://www.rhone.com/) in an incognito preview. The first paint was the Singapore storefront (title "Welcome to Rhone® | Rhone", HTTP path `/`). A later product open landed on the United States storefront of the same host. Desktop viewport measured 1440 by 900 CSS pixels, `devicePixelRatio` 2. The page is a live store, not a parked domain and not a captcha wall.

Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider was clicked. No captcha was solved. Add to bag was not clicked. Cart was not opened. Checkout was not opened. Search was not submitted. `login-extracted` was not flipped. `catalog.json` and `webapps-manifest.json` were left alone. origin/main had no `systems/rhone/`.

Tracking query strings are not recorded. The footer phone link is listed as a stop and is not copied as a number.

## Shipping bar

30px. Background `#1c1519`. Type 12px `#fbf9f9`.

| Control | Opens | This pass |
|---|---|---|
| Free shipping line | no link of its own | read on the homepage (Singapore copy) and on the product (United States copy) |
| Holiday shop slide | `/collections/gifts-for-him/` and `/pages/gift-guide/` | not opened |
| Previous / next | the other slide | not clicked |

## Courtesy bar

`.courtesy-nav`, 32px, background `#efedea`, type 16px Denim `#1c1519`.

| Control | Opens | This pass |
|---|---|---|
| Take 15% off | `#trigger:signup-modal-nav` | not opened. Signup wall. Stop. |
| Help center | `https://support.rhone.com/` | external. Not opened. |
| Gift cards | `/products/e-giftcard/` | not opened |
| Find a store | `/store-locator` | not opened. Store pages can print street addresses. |
| Country | country selector button | not opened. Not submitted. |

## Header

`.main-nav`, 101px including the courtesy bar, page color `#fbf9f9`, 1px border `#e3dfd9`. Department links are 16px Denim 500. The wordmark is an inline SVG, fill `#1c1519`, 74 by 20 in the header.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| New | link | `/collections/new-arrivals/` | not opened. Submenu read from the DOM. |
| Men | link | `/collections/mens-view-all/` | photographed |
| Women | link | `/collections/womens-view-all/` | not opened. Submenu read from the DOM. |
| Resale | link | `https://rerhone.rhone.com/` | external. Not opened. |
| Mental Fitness | link | `/pages/mental-fitness/` | not opened |
| Logo | link | `/` | home |
| Search | searchbox | in-header search | not submitted |
| Account | button | account wall | not opened. Stop. |
| Favorites | button | favorites | not opened. Stop if it asks to sign in. |
| Cart | button | cart | not opened. Checkout was not started. |

## New menu

Read from the homepage DOM. Not hovered open.

| Control | Opens |
|---|---|
| New arrivals | `/collections/new-arrivals/` |
| Best sellers this week | `/collections/best-sellers/` |
| The holiday shop | `/pages/gift-guide/` |
| The lounge edit | `/collections/dreamstate-dreamglow-collections/` |
| NBA x Rhone | `/collections/mens-rhone-x-nba-collection/` |
| New to Rhone? | `/pages/new-to-rhone/` |
| New for him | `/collections/mens-new-arrivals/` |
| New for her | `/collections/womens-new-arrivals/` |
| Winter well catalog | `/pages/catalogs/` |

## Men menu

The Men link itself opens `/collections/mens-view-all/`, photographed as [category-light-1440.png](screenshots/category-light-1440.png). The rest was read from the homepage DOM.

| Column | Control | Opens |
|---|---|---|
| Featured | New arrivals | `/collections/mens-new-arrivals/` |
| Featured | Best sellers | `/collections/mens-best-sellers/` |
| Featured | Commuter® | `/collections/mens-commuter-collection/` |
| Featured | New to Rhone? | `/pages/mens-new-to-rhone/` |
| Featured | NBA collection | `/collections/rhone-x-nba-collection/` |
| Featured | Gifts | `/collections/gifts-for-him/` |
| Clothing | Shop all | `/collections/mens-view-all/` |
| Clothing | Pants & trousers | `/collections/mens-view-all-pants/` |
| Clothing | Tops | `/collections/mens-view-all-tops/` |
| Clothing | Button-downs | `/collections/mens-button-down-shirts/` |
| Clothing | Hoodies & pullovers | `/collections/mens-hoodies-pullovers/` |
| Clothing | Joggers & sweatpants | `/collections/mens-joggers/` |
| Clothing | Outerwear | `/collections/mens-jackets-vests/` |
| Clothing | Polos | `/collections/mens-polo-shirts/` |
| Clothing | Sweaters & 1/4 Zips | `/collections/mens-sweaters/` |
| Clothing | Shorts | `/collections/mens-view-all-shorts/` |
| Clothing | Tees | `/collections/mens-tees-collection/` |
| Activity | Court sports | `/collections/mens-tennis/` |
| Activity | Golf | `/collections/mens-golf-apparel/` |
| Activity | Lounge | `/collections/mens-recover/` |
| Activity | Travel | `/collections/mens-traveling/` |
| Activity | Run | `/collections/mens-running/` |
| Activity | Workout | `/collections/mens-training/` |
| Activity | Workwear | `/collections/mens-commuting/` |
| Accessories | Accessories | `/collections/mens-view-all-accessories/` |

## Women menu

Read from the homepage DOM. Not opened.

| Column | Control | Opens |
|---|---|---|
| Featured | New arrivals | `/collections/womens-new-arrivals/` |
| Featured | Best sellers | `/collections/womens-best-sellers/` |
| Featured | DreamGlow® | `/collections/womens-dreamglow-collection/` |
| Featured | New to Rhone? | `/pages/womens-new-to-rhone/` |
| Featured | NBA collection | `/collections/rhone-x-nba-collection/` |
| Featured | Matching sets | `/collections/womens-matching-sets/` |
| Featured | Shop by color | `/collections/womens-dark-espresso/` |
| Featured | Gifts | `/collections/gifts-for-her/` |
| Clothing | Shop all | `/collections/womens-view-all/` |
| Clothing | Tops | `/collections/womens-view-all-tops/` |
| Clothing | Pants | `/collections/womens-view-all-bottoms/` |
| Clothing | Hoodies & pullovers | `/collections/womens-hoodies-jackets/` |
| Clothing | Leggings | `/collections/womens-leggings/` |
| Clothing | Outerwear | `/collections/womens-outerwear/` |
| Clothing | Shorts | `/collections/womens-shorts/` |
| Clothing | Skirts & dresses | `/collections/womens-skirts-dresses/` |
| Clothing | Sports bras | `/collections/womens-sports-bras/` |
| Clothing | Sweaters | `/collections/womens-sweaters/` |
| Clothing | Tanks & tees | `/collections/womens-tanks/` |
| Activity | Court sports | `/collections/womens-tennis/` |
| Activity | Golf | `/collections/womens-golf/` |
| Activity | Lounge | `/collections/womens-recovery/` |
| Activity | Run | `/collections/womens-running/` |
| Activity | Studio | `/collections/womens-studio/` |
| Activity | Travel | `/collections/womens-travel-collection/` |
| Accessories | Accessories | `/collections/womens-view-all-accessories/` |

## Homepage body

Photographed: [home-light-1440.png](screenshots/home-light-1440.png).

| Control | Opens | This pass |
|---|---|---|
| Shop men's | `/collections/mens-new-arrivals/` | not opened |
| Shop women's | `/collections/womens-new-arrivals/` | not opened |
| Shop new arrivals | `/collections/new-arrivals/` | not opened |
| Product tiles | `/products/...` | one product opened, below |
| Quick shop | in-page shop | not opened. Add to bag was not clicked. |
| Add to favorites | favorites | not clicked |

## Product opened

[https://www.rhone.com/products/mens-commuter-pant-slim/](https://www.rhone.com/products/mens-commuter-pant-slim/) as [product-light-1440.png](screenshots/product-light-1440.png). Title "Commuter® Pant - Slim". Add to bag is a button and was not clicked. Size chips and color swatches were not selected. Save to favorites was not clicked. Fit guide and size guide were not opened.

## About

Footer "About us" opens `/pages/about-us/`. Photographed: [about-light-1440.png](screenshots/about-light-1440.png). Title "About Rhone: Our Story, Mission & Forever Forward Ethos | Rhone".

## Footer

Read from the homepage DOM. The phone control is a `tel:` link. That branch stops. The number is not written here. The footer was not photographed, because that control sits in the footer.

| Group | Control | Opens | This pass |
|---|---|---|---|
| Support | Find a store | `/store-locator/` | not opened |
| Support | About us | `/pages/about-us/` | photographed |
| Support | Join community | `/pages/12-pursuits/` | not opened |
| Support | Live chat | `javascript:Kustomer.open()` | not clicked |
| Support | Submit a request | `https://support.rhone.com/contact/contact-us-SJhypqCHMe` | not opened. A form. Stop. |
| Support | Phone | `tel:` | stop. Not dialed. Number not copied. |
| Support | Wholesale & green grass orders | `/pages/wholesale-greengrass/` | not opened |
| Support | Corporate & group sales | `/pages/corporate-orders/` | not opened |
| Support | Help center | `https://support.rhone.com/` | not opened |
| Support | My account | `https://account.rhone.com/` | stop. Account wall. Not opened. |
| Support | Gift card balance | `/giftcardbalance/` | not opened. A form. |
| Support | Returns & exchanges | `/pages/returns/` | not opened |
| Support | EU Right of Withdrawal | `https://rhone.formstack.com/forms/right_of_withdrawal` | stop. A form. Not opened. |
| Community | LPGA partnership | `/pages/lpga-partner/` | not opened |
| Community | NBA partnership | `/pages/nba/` | not opened |
| Community | Rhone Pro Program | `/pages/rhone-pro-program/` | not opened |
| Community | Community discounts | `/pages/community-discounts/` | not opened |
| Company | Careers | `/pages/careers/` | not opened |
| Company | Press page | `/pages/press-page/` | not opened |
| Company | Resale | `https://rerhone.rhone.com/` | not opened |
| Company | Privacy Notice | `https://privacy.rhone.com/` | not opened |
| Company | Financial Incentive | `https://privacy.rhone.com/privacy-policy` | not opened |
| Company | Terms of use | `/pages/terms-of-use/` | not opened |
| Subscribe | email field and Subscribe | signup | not typed. Not submitted. Stop. |
| Social | Instagram, TikTok, Facebook | external profiles | not opened |

## Where the walk stopped

Account, favorites, Take 15% off, the footer Subscribe control, My account, the contact form, the withdrawal form, the phone link, Add to bag, and Cart. No password, email, code, phone, or address was typed.
