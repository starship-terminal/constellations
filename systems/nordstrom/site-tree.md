# Nordstrom public site tree

Mapped signed out on 2026-11-22 from [https://www.nordstrom.com](https://www.nordstrom.com). The browser stayed on [https://www.nordstrom.com/](https://www.nordstrom.com/). Title "Nordstrom Online & in Store: Shoes, Jewelry, Clothing, Makeup, Dresses". Headless Chromium, 1440 by 900 CSS pixels, `devicePixelRatio` 2. Visual viewport scale 1. Screenshots are 2880 by 1800. The shipping bar reads "Shipping outside of the U.S.?" and the country control reads Singapore. Prices on the product page read SGD. The page is a live shop, not a parked domain and not a captcha wall. Promo bar background `rgb(25, 26, 27)`. Body type is Brandon Text, 16px, color `rgb(25, 26, 27)`.

The shared preview browser was sent to [https://siteclosed.nordstrom.com/invitation.html](https://siteclosed.nordstrom.com/invitation.html) ("We've noticed some unusual activity"). That page printed a customer-service phone number. It was not saved. The walk continued in headless Chromium, which loaded the public shop.

Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider was clicked. No captcha was solved. Add to Bag was not clicked. The bag link points at `/shopping-bag` and was not opened. Sign In was not opened. Shop with AI was not opened. The Singapore country control was not opened. Get Email Updates was not filled. Search was not submitted. Order Status, price adjustment, card payment, and card management were not opened. `login-extracted` stays `not-started`.

`catalog.json` and `webapps-manifest.json` were left alone. origin/main had no `systems/nordstrom/`.

Tracking query strings (`origin`, `breadcrumb`, `jid`, `cid`, `cm_sp`, `recs_*`, `_ics`, `irclickid`) are not recorded.

## Promo bar

One dark strip sits above the logo, 41px, full width, background `rgb(25, 26, 27)`, type 16px, white.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Learn About International Shopping | link | [https://www.nordstrom.com/browse/customer-service/international-orders](https://www.nordstrom.com/browse/customer-service/international-orders) | listed, not opened |
| Singapore | button | country picker | not opened. Label is white, 18px |

## Header

Photographed: [home-light-1440.png](screenshots/home-light-1440.png).

The bar under the promo strip is white. The wordmark is an SVG, 198 by 25, served as a background image from `https://n.nordstrommedia.com/alias/nordstrom-logo.svg`. Saved as [icons/mark.svg](icons/mark.svg). Search is a field, 728 by 42, fill `rgb(240, 243, 245)`, radius 0, placeholder "Search for products or brands". It was not submitted.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Skip navigation | link | `#main-content-start` | not followed |
| Nordstrom Logo | link | [https://www.nordstrom.com/](https://www.nordstrom.com/) | home |
| Search | field | overlay | not submitted |
| Shop with AI | button | not opened | beta control, not opened |
| Sign In | button | not opened | login wall, stopped |
| Bag | link | [https://www.nordstrom.com/shopping-bag](https://www.nordstrom.com/shopping-bag) | bag wall, not opened. Visible count 0 |

Department labels are buttons. They open `#GlobalDesktopNavFlyout`. Those panels were read, not photographed as separate pages. Black Friday & Sale is `rgb(184, 0, 9)`. The other department labels are `rgb(25, 26, 27)`, 16px, weight 400.

## Pages opened

| Page | URL | Shot |
|---|---|---|
| Homepage | [https://www.nordstrom.com/](https://www.nordstrom.com/) | [home-light-1440.png](screenshots/home-light-1440.png) |
| Women's clothing | [https://www.nordstrom.com/browse/women/clothing](https://www.nordstrom.com/browse/women/clothing) | [collection-light-1440.png](screenshots/collection-light-1440.png) |
| Cashmere Crewneck Sweater | [https://www.nordstrom.com/s/nordstrom-cashmere-crew-nk-sweater/8688977](https://www.nordstrom.com/s/nordstrom-cashmere-crew-nk-sweater/8688977) | [product-light-1440.png](screenshots/product-light-1440.png) |
| About Us | [https://www.nordstrom.com/browse/about](https://www.nordstrom.com/browse/about) | [about-light-1440.png](screenshots/about-light-1440.png) |

The product page showed Add to Bag, size chips, and a sale price in SGD. Add to Bag was not clicked. Size chips were not clicked.

## Footer

Read from the homepage footer after the department menus. Columns: Customer Service, About Us, Stores & Services, Nordstrom Card & Rewards, Nordstrom, Inc., and a legal row. Get Email Updates was not filled. Apply for a Nordstrom Card, Pay My Bill, and Manage My Nordstrom Card were not opened. Order Status and Price Adjustments sit on account paths and were not opened.


### Black Friday & Sale

| Control | Destination |
|---|---|
| All Black Friday & Sale | [https://www.nordstrom.com/browse/sale](https://www.nordstrom.com/browse/sale) |
| Black Friday Deals | [https://www.nordstrom.com/browse/sale/black-friday](https://www.nordstrom.com/browse/sale/black-friday) |
| New Markdowns | [https://www.nordstrom.com/browse/sale/new-markdowns](https://www.nordstrom.com/browse/sale/new-markdowns) |
| Bestsellers | [https://www.nordstrom.com/browse/sale/bestsellers](https://www.nordstrom.com/browse/sale/bestsellers) |
| Cold Weather | [https://www.nordstrom.com/browse/sale/cold-weather-sale](https://www.nordstrom.com/browse/sale/cold-weather-sale) |
| Under $100 | [https://www.nordstrom.com/browse/sale/under-100](https://www.nordstrom.com/browse/sale/under-100) |
| Under $50 | [https://www.nordstrom.com/browse/sale/under-50](https://www.nordstrom.com/browse/sale/under-50) |
| Women | [https://www.nordstrom.com/browse/sale/women](https://www.nordstrom.com/browse/sale/women) |
| Clothing | [https://www.nordstrom.com/browse/sale/women/clothing](https://www.nordstrom.com/browse/sale/women/clothing) |
| Shoes | [https://www.nordstrom.com/browse/sale/women/shoes](https://www.nordstrom.com/browse/sale/women/shoes) |
| Handbags & Wallets | [https://www.nordstrom.com/browse/sale/women/handbags](https://www.nordstrom.com/browse/sale/women/handbags) |
| Jewelry | [https://www.nordstrom.com/browse/sale/women/jewelry](https://www.nordstrom.com/browse/sale/women/jewelry) |
| Accessories | [https://www.nordstrom.com/browse/sale/women/accessories](https://www.nordstrom.com/browse/sale/women/accessories) |
| Beauty | [https://www.nordstrom.com/browse/sale/beauty](https://www.nordstrom.com/browse/sale/beauty) |
| Contemporary | [https://www.nordstrom.com/browse/sale/women/contemporary](https://www.nordstrom.com/browse/sale/women/contemporary) |
| Plus | [https://www.nordstrom.com/browse/sale/women/plus-size](https://www.nordstrom.com/browse/sale/women/plus-size) |
| Petite | [https://www.nordstrom.com/browse/sale/women/petite](https://www.nordstrom.com/browse/sale/women/petite) |
| Maternity | [https://www.nordstrom.com/browse/sale/women/maternity](https://www.nordstrom.com/browse/sale/women/maternity) |
| Men | [https://www.nordstrom.com/browse/sale/men](https://www.nordstrom.com/browse/sale/men) |
| Clothing | [https://www.nordstrom.com/browse/sale/men/clothing](https://www.nordstrom.com/browse/sale/men/clothing) |
| Shoes | [https://www.nordstrom.com/browse/sale/men/shoes](https://www.nordstrom.com/browse/sale/men/shoes) |
| Accessories | [https://www.nordstrom.com/browse/sale/men/accessories](https://www.nordstrom.com/browse/sale/men/accessories) |
| Grooming & Cologne | [https://www.nordstrom.com/browse/sale/men/grooming](https://www.nordstrom.com/browse/sale/men/grooming) |
| Contemporary | [https://www.nordstrom.com/browse/sale/men/mens-contemporary](https://www.nordstrom.com/browse/sale/men/mens-contemporary) |
| Big & Tall | [https://www.nordstrom.com/browse/sale/men/big-tall](https://www.nordstrom.com/browse/sale/men/big-tall) |
| Fragrance | [https://www.nordstrom.com/browse/sale/beauty/fragrance](https://www.nordstrom.com/browse/sale/beauty/fragrance) |
| Makeup | [https://www.nordstrom.com/browse/sale/beauty/makeup](https://www.nordstrom.com/browse/sale/beauty/makeup) |
| Skin Care | [https://www.nordstrom.com/browse/sale/beauty/skincare](https://www.nordstrom.com/browse/sale/beauty/skincare) |
| Gifts & Sets | [https://www.nordstrom.com/browse/sale/beauty/gift-sets](https://www.nordstrom.com/browse/sale/beauty/gift-sets) |
| Tools & Brushes | [https://www.nordstrom.com/browse/sale/beauty/tools-brushes](https://www.nordstrom.com/browse/sale/beauty/tools-brushes) |
| Kids | [https://www.nordstrom.com/browse/sale/kids](https://www.nordstrom.com/browse/sale/kids) |
| Girls | [https://www.nordstrom.com/browse/sale/kids/girls](https://www.nordstrom.com/browse/sale/kids/girls) |
| Boys | [https://www.nordstrom.com/browse/sale/kids/boys](https://www.nordstrom.com/browse/sale/kids/boys) |
| Baby | [https://www.nordstrom.com/browse/sale/kids/baby](https://www.nordstrom.com/browse/sale/kids/baby) |
| Baby Gear & Essentials | [https://www.nordstrom.com/browse/sale/kids/baby-gear](https://www.nordstrom.com/browse/sale/kids/baby-gear) |
| Shoes | [https://www.nordstrom.com/browse/sale/kids/shoes](https://www.nordstrom.com/browse/sale/kids/shoes) |
| Toys | [https://www.nordstrom.com/browse/sale/kids/toys](https://www.nordstrom.com/browse/sale/kids/toys) |
| Designer | [https://www.nordstrom.com/browse/sale/designer](https://www.nordstrom.com/browse/sale/designer) |
| Women | [https://www.nordstrom.com/browse/sale/designer/women](https://www.nordstrom.com/browse/sale/designer/women) |
| Men | [https://www.nordstrom.com/browse/sale/designer/men](https://www.nordstrom.com/browse/sale/designer/men) |
| Home | [https://www.nordstrom.com/browse/sale/home](https://www.nordstrom.com/browse/sale/home) |
| Bedding | [https://www.nordstrom.com/browse/sale/home/bedding](https://www.nordstrom.com/browse/sale/home/bedding) |
| Decor | [https://www.nordstrom.com/browse/sale/home/decor](https://www.nordstrom.com/browse/sale/home/decor) |
| Tabletop & Kitchen | [https://www.nordstrom.com/browse/sale/home/tabletop-kitchen](https://www.nordstrom.com/browse/sale/home/tabletop-kitchen) |
| Gifts on Sale | [https://www.nordstrom.com/browse/sale/gifts](https://www.nordstrom.com/browse/sale/gifts) |
| Women | [https://www.nordstrom.com/browse/sale/gifts/women](https://www.nordstrom.com/browse/sale/gifts/women) |
| Men | [https://www.nordstrom.com/browse/sale/gifts/men](https://www.nordstrom.com/browse/sale/gifts/men) |
| Kids & Babies | [https://www.nordstrom.com/browse/sale/gifts/kids](https://www.nordstrom.com/browse/sale/gifts/kids) |
| Teens | [https://www.nordstrom.com/browse/sale/gifts/young-adult](https://www.nordstrom.com/browse/sale/gifts/young-adult) |
| All Sale | [https://www.nordstrom.com/browse/sale?campaign=wf12633522-del2-gnpt1](https://www.nordstrom.com/browse/sale?campaign=wf12633522-del2-gnpt1) |

### Holiday Gifts

| Control | Destination |
|---|---|
| All Holiday Gifts | [https://www.nordstrom.com/browse/holiday-gifts](https://www.nordstrom.com/browse/holiday-gifts) |
| Gift Guide | [https://www.nordstrom.com/browse/holiday-gifts/gift-guide](https://www.nordstrom.com/browse/holiday-gifts/gift-guide) |
| Top Gifts | [https://www.nordstrom.com/browse/holiday-gifts/gift-edit](https://www.nordstrom.com/browse/holiday-gifts/gift-edit) |
| Catalog Gifts | [https://www.nordstrom.com/browse/holiday-gifts/our-favorite-gifts](https://www.nordstrom.com/browse/holiday-gifts/our-favorite-gifts) |
| Holiday Pajamas | [https://www.nordstrom.com/browse/holiday-gifts/family-pajamas](https://www.nordstrom.com/browse/holiday-gifts/family-pajamas) |
| UGG Shop | [https://www.nordstrom.com/brands/ugg-australia](https://www.nordstrom.com/brands/ugg-australia) |
| Stocking Stuffers | [https://www.nordstrom.com/browse/holiday-gifts/stocking-stuffers](https://www.nordstrom.com/browse/holiday-gifts/stocking-stuffers) |
| Advent Calendars | [https://www.nordstrom.com/browse/holiday-gifts/advent-calendars](https://www.nordstrom.com/browse/holiday-gifts/advent-calendars) |
| Festive Events | [https://www.nordstrom.com/browse/holiday-gifts/events](https://www.nordstrom.com/browse/holiday-gifts/events) |
| Build Your Wish List | [https://www.nordstrom.com/my-account/wishlist](https://www.nordstrom.com/my-account/wishlist) |
| Toy Shop | [https://www.nordstrom.com/browse/kids/toys](https://www.nordstrom.com/browse/kids/toys) |
| Gifts for Her | [https://www.nordstrom.com/browse/gifts/for-her](https://www.nordstrom.com/browse/gifts/for-her) |
| Cozy & Cashmere Gifts | [https://www.nordstrom.com/browse/gifts/by-category/cozy/for-her](https://www.nordstrom.com/browse/gifts/by-category/cozy/for-her) |
| Beauty Gifts | [https://www.nordstrom.com/browse/beauty/gift-sets](https://www.nordstrom.com/browse/beauty/gift-sets) |
| Handbag Gifts | [https://www.nordstrom.com/browse/gifts/by-category/handbags](https://www.nordstrom.com/browse/gifts/by-category/handbags) |
| Jewelry & Watch Gifts | [https://www.nordstrom.com/browse/gifts/by-category/jewelry-lover-gifts/women](https://www.nordstrom.com/browse/gifts/by-category/jewelry-lover-gifts/women) |
| Gifts for Him | [https://www.nordstrom.com/browse/gifts/for-him](https://www.nordstrom.com/browse/gifts/for-him) |
| Cozy & Cashmere Gifts | [https://www.nordstrom.com/browse/gifts/by-category/cozy/for-him](https://www.nordstrom.com/browse/gifts/by-category/cozy/for-him) |
| Grooming Gifts | [https://www.nordstrom.com/browse/men/grooming/gift-sets](https://www.nordstrom.com/browse/men/grooming/gift-sets) |
| Jewelry & Watch Gifts | [https://www.nordstrom.com/browse/gifts/by-category/jewelry-lover-gifts/men](https://www.nordstrom.com/browse/gifts/by-category/jewelry-lover-gifts/men) |
| Gifts for Teens | [https://www.nordstrom.com/browse/gifts/young-adult](https://www.nordstrom.com/browse/gifts/young-adult) |
| Gifts for Kids & Babies | [https://www.nordstrom.com/browse/gifts/for-kids](https://www.nordstrom.com/browse/gifts/for-kids) |
| Gifts by Category | [https://www.nordstrom.com/browse/gifts/by-category](https://www.nordstrom.com/browse/gifts/by-category) |
| Home Gifts | [https://www.nordstrom.com/browse/gifts/by-category/home](https://www.nordstrom.com/browse/gifts/by-category/home) |
| Sports Fan Gifts | [https://www.nordstrom.com/browse/fan-shop](https://www.nordstrom.com/browse/fan-shop) |
| Tech Gifts | [https://www.nordstrom.com/browse/home/electronics](https://www.nordstrom.com/browse/home/electronics) |
| Sneaker Gifts | [https://www.nordstrom.com/browse/gifts/by-category/sneakers](https://www.nordstrom.com/browse/gifts/by-category/sneakers) |
| Gifts by Price | [https://www.nordstrom.com/browse/gifts/by-price](https://www.nordstrom.com/browse/gifts/by-price) |
| Gifts Under $50 | [https://www.nordstrom.com/browse/gifts/by-price/under-50](https://www.nordstrom.com/browse/gifts/by-price/under-50) |
| Gifts Under $100 | [https://www.nordstrom.com/browse/gifts/by-price/under-100](https://www.nordstrom.com/browse/gifts/by-price/under-100) |
| Luxury Gifts | [https://www.nordstrom.com/browse/gifts/by-price/luxe-gifts](https://www.nordstrom.com/browse/gifts/by-price/luxe-gifts) |
| Gifts on Sale | [https://www.nordstrom.com/browse/sale/gifts](https://www.nordstrom.com/browse/sale/gifts) |
| More Ways to Shop | [https://www.nordstrom.com/browse/gifts/other-recipients](https://www.nordstrom.com/browse/gifts/other-recipients) |
| For the Foodie | [https://www.nordstrom.com/browse/gifts/by-category/home/foodie-gifts](https://www.nordstrom.com/browse/gifts/by-category/home/foodie-gifts) |
| For the One Who Has Everything | [https://www.nordstrom.com/browse/gifts/other-recipients/unique-gifts](https://www.nordstrom.com/browse/gifts/other-recipients/unique-gifts) |
| For the Party Host | [https://www.nordstrom.com/browse/gifts/by-category/party-host-gifts](https://www.nordstrom.com/browse/gifts/by-category/party-host-gifts) |
| For the Traveler | [https://www.nordstrom.com/browse/gifts/by-category/travel](https://www.nordstrom.com/browse/gifts/by-category/travel) |
| Holiday Help | [https://www.nordstrom.com/browse/services](https://www.nordstrom.com/browse/services) |
| Gift Cards | [https://www.nordstrom.com/browse/customer-service/gift-card-info](https://www.nordstrom.com/browse/customer-service/gift-card-info) |
| Pickup & Delivery Options | [https://www.nordstrom.com/browse/services/shipping-methods-charges](https://www.nordstrom.com/browse/services/shipping-methods-charges) |
| Request a Look | [https://www.nordstrom.com/curation/request](https://www.nordstrom.com/curation/request) |
| Style Help | [https://www.nordstrom.com/browse/services/personal-stylists](https://www.nordstrom.com/browse/services/personal-stylists) |
| Track Your Order | [https://www.nordstrom.com/signin/order-lookup](https://www.nordstrom.com/signin/order-lookup) |
| Holiday Gifts | [https://www.nordstrom.com/browse/holiday-gifts?campaign=wf13131375-del98-gnpt](https://www.nordstrom.com/browse/holiday-gifts?campaign=wf13131375-del98-gnpt) |

### New & Now

| Control | Destination |
|---|---|
| All New & Now | [https://www.nordstrom.com/browse/new](https://www.nordstrom.com/browse/new) |
| Celebrating 125 Years | [https://www.nordstrom.com/browse/125-anniversary](https://www.nordstrom.com/browse/125-anniversary) |
| Sneaker Release Calendar | [https://www.nordstrom.com/browse/sneaker-releases](https://www.nordstrom.com/browse/sneaker-releases) |
| Experience Fine Jewelry | [https://www.nordstrom.com/browse/women/jewelry/fine/experience-fine](https://www.nordstrom.com/browse/women/jewelry/fine/experience-fine) |
| Women | [https://www.nordstrom.com/browse/women/new](https://www.nordstrom.com/browse/women/new) |
| Men | [https://www.nordstrom.com/browse/men/new](https://www.nordstrom.com/browse/men/new) |
| Beauty | [https://www.nordstrom.com/browse/beauty/new](https://www.nordstrom.com/browse/beauty/new) |
| Shoes | [https://www.nordstrom.com/browse/shoes/new](https://www.nordstrom.com/browse/shoes/new) |
| Accessories | [https://www.nordstrom.com/browse/accessories/new](https://www.nordstrom.com/browse/accessories/new) |
| Kids | [https://www.nordstrom.com/browse/kids/new](https://www.nordstrom.com/browse/kids/new) |
| Designer | [https://www.nordstrom.com/browse/designer/new](https://www.nordstrom.com/browse/designer/new) |
| The Edit | [https://www.nordstrom.com/browse/designer/the-edit](https://www.nordstrom.com/browse/designer/the-edit) |
| Home | [https://www.nordstrom.com/browse/home/new](https://www.nordstrom.com/browse/home/new) |
| Style Guide | [https://www.nordstrom.com/browse/style-guide](https://www.nordstrom.com/browse/style-guide) |
| Beauty Inspiration | [https://www.nordstrom.com/browse/style-guide/beauty](https://www.nordstrom.com/browse/style-guide/beauty) |
| Designer Style Guide | [https://www.nordstrom.com/browse/style-guide/designer](https://www.nordstrom.com/browse/style-guide/designer) |
| What's Hot Now | [https://www.nordstrom.com/browse/style-guide/trend-edit](https://www.nordstrom.com/browse/style-guide/trend-edit) |
| Cashmere Shop | [https://www.nordstrom.com/browse/women/cashmere](https://www.nordstrom.com/browse/women/cashmere) |
| Coat Shop | [https://www.nordstrom.com/browse/women/clothing/coats-jackets](https://www.nordstrom.com/browse/women/clothing/coats-jackets) |
| Cold Weather Shop | [https://www.nordstrom.com/browse/cold-weather/women](https://www.nordstrom.com/browse/cold-weather/women) |
| Gem Glam | [https://www.nordstrom.com/browse/style-guide/trend-edit/gem-glam](https://www.nordstrom.com/browse/style-guide/trend-edit/gem-glam) |
| Off Duty Opera | [https://www.nordstrom.com/browse/style-guide/trend-edit/opera](https://www.nordstrom.com/browse/style-guide/trend-edit/opera) |
| Winter Whites | [https://www.nordstrom.com/browse/style-guide/trend-edit/winter-white](https://www.nordstrom.com/browse/style-guide/trend-edit/winter-white) |
| New Brands & Collections | [https://www.nordstrom.com/browse/style-guide/new-brands](https://www.nordstrom.com/browse/style-guide/new-brands) |
| David Bowie Holiday Collection | [https://www.nordstrom.com/browse/style-guide/new-brands/david-bowie](https://www.nordstrom.com/browse/style-guide/new-brands/david-bowie) |
| Hello Molly | [https://www.nordstrom.com/brands/hello-molly](https://www.nordstrom.com/brands/hello-molly) |
| MANGO x Alex Consani | [https://www.nordstrom.com/brands/mango](https://www.nordstrom.com/brands/mango) |
| WAYF x Rose Lola | [https://www.nordstrom.com/brands/wayf](https://www.nordstrom.com/brands/wayf) |
| Women's Occasion | [https://www.nordstrom.com/browse/women/occasion](https://www.nordstrom.com/browse/women/occasion) |
| Casual Weekend | [https://www.nordstrom.com/browse/women/occasion/weekend](https://www.nordstrom.com/browse/women/occasion/weekend) |
| Cocktail | [https://www.nordstrom.com/browse/women/occasion/cocktail](https://www.nordstrom.com/browse/women/occasion/cocktail) |
| Party & Night Out | [https://www.nordstrom.com/browse/women/occasion/night-out](https://www.nordstrom.com/browse/women/occasion/night-out) |
| New Years Eve | [https://www.nordstrom.com/browse/holiday-party-outfits/women/holiday-night-out](https://www.nordstrom.com/browse/holiday-party-outfits/women/holiday-night-out) |
| Holiday Dressing | [https://www.nordstrom.com/browse/holiday-party-outfits/women](https://www.nordstrom.com/browse/holiday-party-outfits/women) |
| Vacation & Resort | [https://www.nordstrom.com/browse/vacation/women](https://www.nordstrom.com/browse/vacation/women) |
| Work | [https://www.nordstrom.com/browse/women/occasion/work](https://www.nordstrom.com/browse/women/occasion/work) |
| Wedding Guest | [https://www.nordstrom.com/browse/women/occasion/wedding-guest](https://www.nordstrom.com/browse/women/occasion/wedding-guest) |
| Men's Occasion | [https://www.nordstrom.com/browse/men/occasion](https://www.nordstrom.com/browse/men/occasion) |
| Coat Shop | [https://www.nordstrom.com/browse/men/clothing/coats-jackets](https://www.nordstrom.com/browse/men/clothing/coats-jackets) |
| Cold Weather Shop | [https://www.nordstrom.com/browse/cold-weather/men](https://www.nordstrom.com/browse/cold-weather/men) |
| Holiday Dressing | [https://www.nordstrom.com/browse/holiday-party-outfits/men](https://www.nordstrom.com/browse/holiday-party-outfits/men) |
| Vacation & Resort | [https://www.nordstrom.com/browse/vacation/men](https://www.nordstrom.com/browse/vacation/men) |
| Work | [https://www.nordstrom.com/browse/men/occasion/work](https://www.nordstrom.com/browse/men/occasion/work) |
| Women's Holiday Dressing | [https://www.nordstrom.com/browse/holiday-party-outfits/women?campaign=nov_gnpt_holidaydressing](https://www.nordstrom.com/browse/holiday-party-outfits/women?campaign=nov_gnpt_holidaydressing) |

### Women

| Control | Destination |
|---|---|
| All Women | [https://www.nordstrom.com/browse/women](https://www.nordstrom.com/browse/women) |
| Gifts for Her | [https://www.nordstrom.com/browse/gifts/for-her](https://www.nordstrom.com/browse/gifts/for-her) |
| New Arrivals | [https://www.nordstrom.com/browse/women/new](https://www.nordstrom.com/browse/women/new) |
| Cold-Weather Shop | [https://www.nordstrom.com/browse/cold-weather/women](https://www.nordstrom.com/browse/cold-weather/women) |
| UGG for Women | [https://www.nordstrom.com/brands/ugg-australia/women](https://www.nordstrom.com/brands/ugg-australia/women) |
| Under $100 | [https://www.nordstrom.com/browse/women/under-100](https://www.nordstrom.com/browse/women/under-100) |
| On Trend: Gem Glam | [https://www.nordstrom.com/browse/style-guide/trend-edit/gem-glam](https://www.nordstrom.com/browse/style-guide/trend-edit/gem-glam) |
| On Trend: Off-Duty Opera | [https://www.nordstrom.com/browse/style-guide/trend-edit/opera](https://www.nordstrom.com/browse/style-guide/trend-edit/opera) |
| On Trend: Winter Whites | [https://www.nordstrom.com/browse/style-guide/trend-edit/winter-white](https://www.nordstrom.com/browse/style-guide/trend-edit/winter-white) |
| Cashmere Shop | [https://www.nordstrom.com/browse/women/cashmere](https://www.nordstrom.com/browse/women/cashmere) |
| Nordstrom Made | [https://www.nordstrom.com/browse/nordstrom-made/women](https://www.nordstrom.com/browse/nordstrom-made/women) |
| Women's Black Friday Sale | [https://www.nordstrom.com/browse/sale/women](https://www.nordstrom.com/browse/sale/women) |
| Clothing | [https://www.nordstrom.com/browse/women/clothing](https://www.nordstrom.com/browse/women/clothing) |
| Activewear | [https://www.nordstrom.com/browse/activewear/women-clothing](https://www.nordstrom.com/browse/activewear/women-clothing) |
| Dresses | [https://www.nordstrom.com/browse/women/clothing/dresses](https://www.nordstrom.com/browse/women/clothing/dresses) |
| Coats & Jackets | [https://www.nordstrom.com/browse/women/clothing/coats-jackets](https://www.nordstrom.com/browse/women/clothing/coats-jackets) |
| Jeans & Denim | [https://www.nordstrom.com/browse/women/clothing/jeans](https://www.nordstrom.com/browse/women/clothing/jeans) |
| Jumpsuits & Rompers | [https://www.nordstrom.com/browse/women/clothing/jumpsuits-rompers](https://www.nordstrom.com/browse/women/clothing/jumpsuits-rompers) |
| Lingerie, Hosiery & Shapewear | [https://www.nordstrom.com/browse/women/clothing/underwear-lingerie](https://www.nordstrom.com/browse/women/clothing/underwear-lingerie) |
| Matching Sets | [https://www.nordstrom.com/browse/women/clothing/matching-sets](https://www.nordstrom.com/browse/women/clothing/matching-sets) |
| Pants & Leggings | [https://www.nordstrom.com/browse/women/clothing/pants](https://www.nordstrom.com/browse/women/clothing/pants) |
| Shorts | [https://www.nordstrom.com/browse/women/clothing/shorts](https://www.nordstrom.com/browse/women/clothing/shorts) |
| Skirts | [https://www.nordstrom.com/browse/women/clothing/skirts](https://www.nordstrom.com/browse/women/clothing/skirts) |
| Sleepwear & Loungewear | [https://www.nordstrom.com/browse/women/clothing/sleepwear-robes](https://www.nordstrom.com/browse/women/clothing/sleepwear-robes) |
| Suits & Separates | [https://www.nordstrom.com/browse/women/clothing/work-suits](https://www.nordstrom.com/browse/women/clothing/work-suits) |
| Sweaters | [https://www.nordstrom.com/browse/women/clothing/sweaters](https://www.nordstrom.com/browse/women/clothing/sweaters) |
| Sweatshirts & Hoodies | [https://www.nordstrom.com/browse/women/clothing/sweatshirts-hoodies](https://www.nordstrom.com/browse/women/clothing/sweatshirts-hoodies) |
| Swimwear & Cover-Ups | [https://www.nordstrom.com/browse/women/clothing/swimsuits](https://www.nordstrom.com/browse/women/clothing/swimsuits) |
| Tops | [https://www.nordstrom.com/browse/women/clothing/tops-tees](https://www.nordstrom.com/browse/women/clothing/tops-tees) |
| Casual | [https://www.nordstrom.com/browse/women/clothing/dresses/casual-dresses](https://www.nordstrom.com/browse/women/clothing/dresses/casual-dresses) |
| Cocktail | [https://www.nordstrom.com/browse/women/clothing/dresses/cocktail](https://www.nordstrom.com/browse/women/clothing/dresses/cocktail) |
| Formal | [https://www.nordstrom.com/browse/women/clothing/dresses/formal-dresses](https://www.nordstrom.com/browse/women/clothing/dresses/formal-dresses) |
| Guest of Wedding | [https://www.nordstrom.com/browse/women/clothing/dresses/wedding-guest](https://www.nordstrom.com/browse/women/clothing/dresses/wedding-guest) |
| Holiday | [https://www.nordstrom.com/browse/women/clothing/dresses/holiday-party-outfits](https://www.nordstrom.com/browse/women/clothing/dresses/holiday-party-outfits) |
| Mother of the Bride or Groom | [https://www.nordstrom.com/browse/women/clothing/dresses/mother-of-the-bride](https://www.nordstrom.com/browse/women/clothing/dresses/mother-of-the-bride) |
| Sweater | [https://www.nordstrom.com/browse/women/clothing/dresses/sweater-dress](https://www.nordstrom.com/browse/women/clothing/dresses/sweater-dress) |
| Vacation | [https://www.nordstrom.com/browse/women/clothing/dresses/vacation](https://www.nordstrom.com/browse/women/clothing/dresses/vacation) |
| Petite-Size Clothing | [https://www.nordstrom.com/browse/women/clothing/petite-size](https://www.nordstrom.com/browse/women/clothing/petite-size) |
| Plus-Size Clothing | [https://www.nordstrom.com/browse/women/clothing/plus-size](https://www.nordstrom.com/browse/women/clothing/plus-size) |
| Maternity | [https://www.nordstrom.com/browse/women/maternity](https://www.nordstrom.com/browse/women/maternity) |
| Shoes | [https://www.nordstrom.com/browse/women/shoes](https://www.nordstrom.com/browse/women/shoes) |
| Athletic & Sneakers | [https://www.nordstrom.com/browse/women/shoes/sneakers-athletic](https://www.nordstrom.com/browse/women/shoes/sneakers-athletic) |
| Boots | [https://www.nordstrom.com/browse/women/shoes/boots](https://www.nordstrom.com/browse/women/shoes/boots) |
| Comfort | [https://www.nordstrom.com/browse/women/shoes/comfort](https://www.nordstrom.com/browse/women/shoes/comfort) |
| Flats | [https://www.nordstrom.com/browse/women/shoes/flats](https://www.nordstrom.com/browse/women/shoes/flats) |
| Heels | [https://www.nordstrom.com/browse/women/shoes/heels](https://www.nordstrom.com/browse/women/shoes/heels) |
| Loafers & Oxfords | [https://www.nordstrom.com/browse/women/shoes/oxfords-loafers](https://www.nordstrom.com/browse/women/shoes/oxfords-loafers) |
| Sandals | [https://www.nordstrom.com/browse/women/shoes/sandals](https://www.nordstrom.com/browse/women/shoes/sandals) |
| Slippers | [https://www.nordstrom.com/browse/women/shoes/slippers](https://www.nordstrom.com/browse/women/shoes/slippers) |
| Beauty | [https://www.nordstrom.com/browse/beauty](https://www.nordstrom.com/browse/beauty) |
| Fragrance | [https://www.nordstrom.com/browse/beauty/fragrance](https://www.nordstrom.com/browse/beauty/fragrance) |
| Makeup | [https://www.nordstrom.com/browse/beauty/makeup](https://www.nordstrom.com/browse/beauty/makeup) |
| Skin Care | [https://www.nordstrom.com/browse/beauty/skincare](https://www.nordstrom.com/browse/beauty/skincare) |
| Hair Care | [https://www.nordstrom.com/browse/beauty/hair](https://www.nordstrom.com/browse/beauty/hair) |
| Handbags | [https://www.nordstrom.com/browse/women/handbags](https://www.nordstrom.com/browse/women/handbags) |
| Accessories | [https://www.nordstrom.com/browse/women/accessories](https://www.nordstrom.com/browse/women/accessories) |
| Jewelry | [https://www.nordstrom.com/browse/women/jewelry](https://www.nordstrom.com/browse/women/jewelry) |
| Designer | [https://www.nordstrom.com/browse/designer/women](https://www.nordstrom.com/browse/designer/women) |
| Shop by Occasion | [https://www.nordstrom.com/browse/women/occasion](https://www.nordstrom.com/browse/women/occasion) |
| Casual Weekend | [https://www.nordstrom.com/browse/women/occasion/weekend](https://www.nordstrom.com/browse/women/occasion/weekend) |
| Cocktail | [https://www.nordstrom.com/browse/women/occasion/cocktail](https://www.nordstrom.com/browse/women/occasion/cocktail) |
| Holiday Outfits | [https://www.nordstrom.com/browse/holiday-party-outfits/women](https://www.nordstrom.com/browse/holiday-party-outfits/women) |
| New Years Eve | [https://www.nordstrom.com/browse/holiday-party-outfits/women/holiday-night-out](https://www.nordstrom.com/browse/holiday-party-outfits/women/holiday-night-out) |
| Vacation & Resort | [https://www.nordstrom.com/browse/vacation/women](https://www.nordstrom.com/browse/vacation/women) |
| Work | [https://www.nordstrom.com/browse/women/occasion/work](https://www.nordstrom.com/browse/women/occasion/work) |
| Wedding Guest | [https://www.nordstrom.com/browse/women/occasion/wedding-guest](https://www.nordstrom.com/browse/women/occasion/wedding-guest) |
| Contemporary | [https://www.nordstrom.com/browse/women/contemporary](https://www.nordstrom.com/browse/women/contemporary) |
| New Arrivals | [https://www.nordstrom.com/browse/women/contemporary/new](https://www.nordstrom.com/browse/women/contemporary/new) |
| Clothing | [https://www.nordstrom.com/browse/women/contemporary/clothing](https://www.nordstrom.com/browse/women/contemporary/clothing) |
| Shoes | [https://www.nordstrom.com/browse/women/contemporary/shoes](https://www.nordstrom.com/browse/women/contemporary/shoes) |
| Accessories | [https://www.nordstrom.com/browse/women/contemporary/accessories](https://www.nordstrom.com/browse/women/contemporary/accessories) |
| Women's Sale | [https://www.nordstrom.com/browse/sale/women?campaign=wf12633522-del2-gnpt2](https://www.nordstrom.com/browse/sale/women?campaign=wf12633522-del2-gnpt2) |

### Men

| Control | Destination |
|---|---|
| All Men | [https://www.nordstrom.com/browse/men](https://www.nordstrom.com/browse/men) |
| Gifts for Him | [https://www.nordstrom.com/browse/gifts/for-him](https://www.nordstrom.com/browse/gifts/for-him) |
| New Arrivals | [https://www.nordstrom.com/browse/men/new](https://www.nordstrom.com/browse/men/new) |
| Under $50 | [https://www.nordstrom.com/browse/men/under-50](https://www.nordstrom.com/browse/men/under-50) |
| Under $100 | [https://www.nordstrom.com/browse/men/under-100](https://www.nordstrom.com/browse/men/under-100) |
| Cold-Weather Shop | [https://www.nordstrom.com/browse/cold-weather/men](https://www.nordstrom.com/browse/cold-weather/men) |
| Fall Wardrobe Essentials | [https://www.nordstrom.com/browse/men/mens-seasonal-style-essentials](https://www.nordstrom.com/browse/men/mens-seasonal-style-essentials) |
| UGG for Men | [https://www.nordstrom.com/brands/ugg-australia/men](https://www.nordstrom.com/brands/ugg-australia/men) |
| Nordstrom Made | [https://www.nordstrom.com/browse/nordstrom-made/men](https://www.nordstrom.com/browse/nordstrom-made/men) |
| Work | [https://www.nordstrom.com/browse/men/occasion/work](https://www.nordstrom.com/browse/men/occasion/work) |
| Men's Black Friday Sale | [https://www.nordstrom.com/browse/sale/men](https://www.nordstrom.com/browse/sale/men) |
| Clothing | [https://www.nordstrom.com/browse/men/clothing](https://www.nordstrom.com/browse/men/clothing) |
| Activewear | [https://www.nordstrom.com/browse/activewear/men-clothing](https://www.nordstrom.com/browse/activewear/men-clothing) |
| Blazers & Sport Coats | [https://www.nordstrom.com/browse/men/clothing/blazers-sportcoats](https://www.nordstrom.com/browse/men/clothing/blazers-sportcoats) |
| Coats & Jackets | [https://www.nordstrom.com/browse/men/clothing/coats-jackets](https://www.nordstrom.com/browse/men/clothing/coats-jackets) |
| Dress Shirts | [https://www.nordstrom.com/browse/men/clothing/shirts/business-casual-shirts](https://www.nordstrom.com/browse/men/clothing/shirts/business-casual-shirts) |
| Jeans & Denim | [https://www.nordstrom.com/browse/men/clothing/jeans](https://www.nordstrom.com/browse/men/clothing/jeans) |
| Lounge & Sleepwear | [https://www.nordstrom.com/browse/men/clothing/sleepwear-robes](https://www.nordstrom.com/browse/men/clothing/sleepwear-robes) |
| Pants | [https://www.nordstrom.com/browse/men/clothing/pants](https://www.nordstrom.com/browse/men/clothing/pants) |
| Polo Shirts | [https://www.nordstrom.com/browse/men/clothing/shirts/polo-shirts](https://www.nordstrom.com/browse/men/clothing/shirts/polo-shirts) |
| Shirts | [https://www.nordstrom.com/browse/men/clothing/shirts](https://www.nordstrom.com/browse/men/clothing/shirts) |
| Shorts | [https://www.nordstrom.com/browse/men/clothing/shorts](https://www.nordstrom.com/browse/men/clothing/shorts) |
| Suits & Separates | [https://www.nordstrom.com/browse/men/clothing/suits](https://www.nordstrom.com/browse/men/clothing/suits) |
| Sweaters | [https://www.nordstrom.com/browse/men/clothing/sweaters](https://www.nordstrom.com/browse/men/clothing/sweaters) |
| Sweatshirts & Hoodies | [https://www.nordstrom.com/browse/men/clothing/sweatshirts-hoodies](https://www.nordstrom.com/browse/men/clothing/sweatshirts-hoodies) |
| Swimwear | [https://www.nordstrom.com/browse/men/clothing/swimwear](https://www.nordstrom.com/browse/men/clothing/swimwear) |
| T-Shirts | [https://www.nordstrom.com/browse/men/clothing/shirts/tshirts](https://www.nordstrom.com/browse/men/clothing/shirts/tshirts) |
| Underwear, Undershirts & Socks | [https://www.nordstrom.com/browse/men/clothing/underwear-socks](https://www.nordstrom.com/browse/men/clothing/underwear-socks) |
| Shoes | [https://www.nordstrom.com/browse/men/shoes](https://www.nordstrom.com/browse/men/shoes) |
| Athletic & Sneakers | [https://www.nordstrom.com/browse/men/shoes/sneakers-athletic](https://www.nordstrom.com/browse/men/shoes/sneakers-athletic) |
| Boots | [https://www.nordstrom.com/browse/men/shoes/boots](https://www.nordstrom.com/browse/men/shoes/boots) |
| Comfort | [https://www.nordstrom.com/browse/men/shoes/comfort](https://www.nordstrom.com/browse/men/shoes/comfort) |
| Dress Shoes | [https://www.nordstrom.com/browse/men/shoes/dress](https://www.nordstrom.com/browse/men/shoes/dress) |
| Loafers & Slip-Ons | [https://www.nordstrom.com/browse/men/shoes/loafers-slip-ons](https://www.nordstrom.com/browse/men/shoes/loafers-slip-ons) |
| Oxfords | [https://www.nordstrom.com/browse/men/shoes/oxfords](https://www.nordstrom.com/browse/men/shoes/oxfords) |
| Sandals & Flip-Flops | [https://www.nordstrom.com/browse/men/shoes/sandals](https://www.nordstrom.com/browse/men/shoes/sandals) |
| Slippers | [https://www.nordstrom.com/browse/men/shoes/slippers](https://www.nordstrom.com/browse/men/shoes/slippers) |
| Accessories | [https://www.nordstrom.com/browse/men/accessories](https://www.nordstrom.com/browse/men/accessories) |
| Bags | [https://www.nordstrom.com/browse/men/accessories/bags-backpacks](https://www.nordstrom.com/browse/men/accessories/bags-backpacks) |
| Belts | [https://www.nordstrom.com/browse/men/accessories/belts](https://www.nordstrom.com/browse/men/accessories/belts) |
| Hats | [https://www.nordstrom.com/browse/men/accessories/hats](https://www.nordstrom.com/browse/men/accessories/hats) |
| Jewelry | [https://www.nordstrom.com/browse/men/jewelry](https://www.nordstrom.com/browse/men/jewelry) |
| Sunglasses & Eyewear | [https://www.nordstrom.com/browse/men/accessories/sunglasses](https://www.nordstrom.com/browse/men/accessories/sunglasses) |
| Ties & Pocket Squares | [https://www.nordstrom.com/browse/men/accessories/ties-pocket-squares](https://www.nordstrom.com/browse/men/accessories/ties-pocket-squares) |
| Wallets & Card Cases | [https://www.nordstrom.com/browse/men/accessories/wallets](https://www.nordstrom.com/browse/men/accessories/wallets) |
| Watches | [https://www.nordstrom.com/browse/men/jewelry/watches](https://www.nordstrom.com/browse/men/jewelry/watches) |
| Grooming & Cologne | [https://www.nordstrom.com/browse/men/grooming](https://www.nordstrom.com/browse/men/grooming) |
| Big & Tall | [https://www.nordstrom.com/browse/men/big-tall](https://www.nordstrom.com/browse/men/big-tall) |
| DXL Big + Tall | [https://www.nordstrom.com/browse/men/big-tall/dxl-big-tall](https://www.nordstrom.com/browse/men/big-tall/dxl-big-tall) |
| Designer | [https://www.nordstrom.com/browse/designer/men](https://www.nordstrom.com/browse/designer/men) |
| Contemporary | [https://www.nordstrom.com/browse/men/mens-contemporary](https://www.nordstrom.com/browse/men/mens-contemporary) |
| Shop by Occasion | [https://www.nordstrom.com/browse/men/occasion](https://www.nordstrom.com/browse/men/occasion) |
| Holiday Outfits | [https://www.nordstrom.com/browse/holiday-party-outfits/men](https://www.nordstrom.com/browse/holiday-party-outfits/men) |
| Wedding Guest | [https://www.nordstrom.com/browse/men/occasion/wedding-guest](https://www.nordstrom.com/browse/men/occasion/wedding-guest) |
| Shop by Activity | [https://www.nordstrom.com/browse/activewear/activities/men](https://www.nordstrom.com/browse/activewear/activities/men) |
| Golf | [https://www.nordstrom.com/browse/activewear/activities/golf/men](https://www.nordstrom.com/browse/activewear/activities/golf/men) |
| Run & Train | [https://www.nordstrom.com/browse/activewear/activities/running/men](https://www.nordstrom.com/browse/activewear/activities/running/men) |
| Tennis & Pickleball | [https://www.nordstrom.com/browse/activewear/activities/tennis/men](https://www.nordstrom.com/browse/activewear/activities/tennis/men) |
| Sports Fan Shop | [https://www.nordstrom.com/browse/fan-shop/men](https://www.nordstrom.com/browse/fan-shop/men) |
| Men's Sale | [https://www.nordstrom.com/browse/sale/men?campaign=wf12633522-del2-gnpt3](https://www.nordstrom.com/browse/sale/men?campaign=wf12633522-del2-gnpt3) |

### Beauty

| Control | Destination |
|---|---|
| All Beauty | [https://www.nordstrom.com/browse/beauty](https://www.nordstrom.com/browse/beauty) |
| New Arrivals | [https://www.nordstrom.com/browse/beauty/new](https://www.nordstrom.com/browse/beauty/new) |
| Beauty Inspiration | [https://www.nordstrom.com/browse/style-guide/beauty](https://www.nordstrom.com/browse/style-guide/beauty) |
| Bestsellers | [https://www.nordstrom.com/browse/beauty/bestsellers](https://www.nordstrom.com/browse/beauty/bestsellers) |
| Nordstrom Exclusives | [https://www.nordstrom.com/browse/beauty/nordstrom-exclusive](https://www.nordstrom.com/browse/beauty/nordstrom-exclusive) |
| Nordstrom Beauty Services & Events | [https://www.nordstrom.com/browse/beauty/services](https://www.nordstrom.com/browse/beauty/services) |
| Gifts with Purchase | [https://www.nordstrom.com/browse/beauty/gifts-with-purchase](https://www.nordstrom.com/browse/beauty/gifts-with-purchase) |
| Beauty Gifts & Sets | [https://www.nordstrom.com/browse/beauty/gift-sets](https://www.nordstrom.com/browse/beauty/gift-sets) |
| Beauty Black Friday Sale | [https://www.nordstrom.com/browse/sale/beauty](https://www.nordstrom.com/browse/sale/beauty) |
| Beauty Brands | [https://www.nordstrom.com/brands-list/beauty](https://www.nordstrom.com/brands-list/beauty) |
| Bobbi Brown | [https://www.nordstrom.com/brands/bobbi-brown--274](https://www.nordstrom.com/brands/bobbi-brown--274) |
| CHANEL | [https://www.nordstrom.com/brands/chanel--3503](https://www.nordstrom.com/brands/chanel--3503) |
| Charlotte Tilbury | [https://www.nordstrom.com/brands/charlotte-tilbury--70585](https://www.nordstrom.com/brands/charlotte-tilbury--70585) |
| Clinique | [https://www.nordstrom.com/brands/clinique--3550](https://www.nordstrom.com/brands/clinique--3550) |
| DIOR | [https://www.nordstrom.com/brands/dior--448/beauty](https://www.nordstrom.com/brands/dior--448/beauty) |
| Estée Lauder | [https://www.nordstrom.com/brands/estee-lauder--739](https://www.nordstrom.com/brands/estee-lauder--739) |
| Jo Malone London | [https://www.nordstrom.com/brands/jo-malone-london--26720](https://www.nordstrom.com/brands/jo-malone-london--26720) |
| La Mer | [https://www.nordstrom.com/brands/la-mer--9208](https://www.nordstrom.com/brands/la-mer--9208) |
| Lancôme | [https://www.nordstrom.com/brands/lancome--1434](https://www.nordstrom.com/brands/lancome--1434) |
| MAC Cosmetics | [https://www.nordstrom.com/brands/mac-cosmetics--1454](https://www.nordstrom.com/brands/mac-cosmetics--1454) |
| Maison Francis Kurkdjian | [https://www.nordstrom.com/brands/maison-francis-kurkdjian--68454319](https://www.nordstrom.com/brands/maison-francis-kurkdjian--68454319) |
| Parfums de Marly | [https://www.nordstrom.com/brands/parfums-de-marly](https://www.nordstrom.com/brands/parfums-de-marly) |
| Sisley Paris | [https://www.nordstrom.com/brands/sisley-paris](https://www.nordstrom.com/brands/sisley-paris) |
| TOM FORD | [https://www.nordstrom.com/brands/tom-ford--9495/beauty](https://www.nordstrom.com/brands/tom-ford--9495/beauty) |
| Victoria Beckham | [https://www.nordstrom.com/brands/victoria-beckham--15814319](https://www.nordstrom.com/brands/victoria-beckham--15814319) |
| Yves Saint Laurent | [https://www.nordstrom.com/brands/yves-saint-laurent--3544](https://www.nordstrom.com/brands/yves-saint-laurent--3544) |
| Fragrance | [https://www.nordstrom.com/browse/beauty/fragrance](https://www.nordstrom.com/browse/beauty/fragrance) |
| Cologne | [https://www.nordstrom.com/browse/men/grooming/cologne](https://www.nordstrom.com/browse/men/grooming/cologne) |
| Designer Fragrance | [https://www.nordstrom.com/browse/beauty/designer-beauty/fragrance](https://www.nordstrom.com/browse/beauty/designer-beauty/fragrance) |
| Niche Fragrance | [https://www.nordstrom.com/browse/beauty/fragrance/niche-fragrance](https://www.nordstrom.com/browse/beauty/fragrance/niche-fragrance) |
| Perfume | [https://www.nordstrom.com/browse/beauty/fragrance/perfume](https://www.nordstrom.com/browse/beauty/fragrance/perfume) |
| Rollerball & Travel Size | [https://www.nordstrom.com/browse/beauty/fragrance/rollerball](https://www.nordstrom.com/browse/beauty/fragrance/rollerball) |
| Body Mist & Hair Mist | [https://www.nordstrom.com/browse/beauty/fragrance/body-hair-mist](https://www.nordstrom.com/browse/beauty/fragrance/body-hair-mist) |
| Candles & Diffusers | [https://www.nordstrom.com/browse/home/decor/candles-diffusers](https://www.nordstrom.com/browse/home/decor/candles-diffusers) |
| Makeup | [https://www.nordstrom.com/browse/beauty/makeup](https://www.nordstrom.com/browse/beauty/makeup) |
| Eyes | [https://www.nordstrom.com/browse/beauty/makeup/eyes](https://www.nordstrom.com/browse/beauty/makeup/eyes) |
| Face | [https://www.nordstrom.com/browse/beauty/makeup/face](https://www.nordstrom.com/browse/beauty/makeup/face) |
| Lips | [https://www.nordstrom.com/browse/beauty/makeup/lips](https://www.nordstrom.com/browse/beauty/makeup/lips) |
| Nails | [https://www.nordstrom.com/browse/beauty/makeup/nails](https://www.nordstrom.com/browse/beauty/makeup/nails) |
| Brushes & Tools | [https://www.nordstrom.com/browse/beauty/makeup/brushes](https://www.nordstrom.com/browse/beauty/makeup/brushes) |
| Palettes | [https://www.nordstrom.com/browse/beauty/makeup/palettes](https://www.nordstrom.com/browse/beauty/makeup/palettes) |
| Skin Care | [https://www.nordstrom.com/browse/beauty/skincare](https://www.nordstrom.com/browse/beauty/skincare) |
| Cleansers | [https://www.nordstrom.com/browse/beauty/skincare/cleansers](https://www.nordstrom.com/browse/beauty/skincare/cleansers) |
| Exfoliators & Peels | [https://www.nordstrom.com/browse/beauty/skincare/exfoliators](https://www.nordstrom.com/browse/beauty/skincare/exfoliators) |
| Eye Creams & Treatments | [https://www.nordstrom.com/browse/beauty/skincare/eyes](https://www.nordstrom.com/browse/beauty/skincare/eyes) |
| Facial Masks | [https://www.nordstrom.com/browse/beauty/skincare/masks](https://www.nordstrom.com/browse/beauty/skincare/masks) |
| Face Moisturizers | [https://www.nordstrom.com/browse/beauty/skincare/face-moisturizers](https://www.nordstrom.com/browse/beauty/skincare/face-moisturizers) |
| Lip Balms & Treatments | [https://www.nordstrom.com/browse/beauty/skincare/lip-balms-treatments](https://www.nordstrom.com/browse/beauty/skincare/lip-balms-treatments) |
| Self Tanners | [https://www.nordstrom.com/browse/beauty/skincare/self-tanner](https://www.nordstrom.com/browse/beauty/skincare/self-tanner) |
| Serums & Treatments | [https://www.nordstrom.com/browse/beauty/skincare/serums-treatments](https://www.nordstrom.com/browse/beauty/skincare/serums-treatments) |
| Sunscreen | [https://www.nordstrom.com/browse/beauty/skincare/sunscreen](https://www.nordstrom.com/browse/beauty/skincare/sunscreen) |
| Toners | [https://www.nordstrom.com/browse/beauty/skincare/toners](https://www.nordstrom.com/browse/beauty/skincare/toners) |
| Tools & Devices | [https://www.nordstrom.com/browse/beauty/skincare/tools](https://www.nordstrom.com/browse/beauty/skincare/tools) |
| Gifts & Sets | [https://www.nordstrom.com/browse/beauty/gift-sets](https://www.nordstrom.com/browse/beauty/gift-sets) |
| Makeup Gifts & Sets | [https://www.nordstrom.com/browse/beauty/gift-sets/makeup](https://www.nordstrom.com/browse/beauty/gift-sets/makeup) |
| Skin Care Gifts & Sets | [https://www.nordstrom.com/browse/beauty/gift-sets/skincare](https://www.nordstrom.com/browse/beauty/gift-sets/skincare) |
| Fragrance Gifts & Sets | [https://www.nordstrom.com/browse/beauty/fragrance/gift-sets](https://www.nordstrom.com/browse/beauty/fragrance/gift-sets) |
| Hair Care Gifts & Sets | [https://www.nordstrom.com/browse/beauty/gift-sets/hair](https://www.nordstrom.com/browse/beauty/gift-sets/hair) |
| Stocking Stuffers | [https://www.nordstrom.com/browse/beauty/gift-sets/beauty-stocking-stuffers](https://www.nordstrom.com/browse/beauty/gift-sets/beauty-stocking-stuffers) |
| Hair Care | [https://www.nordstrom.com/browse/beauty/hair](https://www.nordstrom.com/browse/beauty/hair) |
| Bath & Body | [https://www.nordstrom.com/browse/beauty/bath-body](https://www.nordstrom.com/browse/beauty/bath-body) |
| Tools, Brushes & Makeup Bags | [https://www.nordstrom.com/browse/beauty/tools-brushes](https://www.nordstrom.com/browse/beauty/tools-brushes) |
| Men's Grooming | [https://www.nordstrom.com/browse/men/grooming](https://www.nordstrom.com/browse/men/grooming) |
| Travel & Mini Sizes | [https://www.nordstrom.com/browse/beauty/travel-size](https://www.nordstrom.com/browse/beauty/travel-size) |
| Natural Beauty | [https://www.nordstrom.com/browse/beauty/natural](https://www.nordstrom.com/browse/beauty/natural) |
| Wellness | [https://www.nordstrom.com/browse/beauty/beauty-wellness](https://www.nordstrom.com/browse/beauty/beauty-wellness) |
| Dermatologist Recommended | [https://www.nordstrom.com/browse/beauty/skincare/doctor-developed-skincare](https://www.nordstrom.com/browse/beauty/skincare/doctor-developed-skincare) |
| Korean Beauty | [https://www.nordstrom.com/browse/beauty/korean-beauty](https://www.nordstrom.com/browse/beauty/korean-beauty) |
| Designer Beauty | [https://www.nordstrom.com/browse/beauty/designer-beauty](https://www.nordstrom.com/browse/beauty/designer-beauty) |
| FSA/HSA Eligible Beauty | [https://www.nordstrom.com/browse/beauty/fsa-hsa-eligible](https://www.nordstrom.com/browse/beauty/fsa-hsa-eligible) |
| Beauty Sale | [https://www.nordstrom.com/browse/sale/beauty?campaign=wf12633522-del2-gnpt9](https://www.nordstrom.com/browse/sale/beauty?campaign=wf12633522-del2-gnpt9) |

### Shoes

| Control | Destination |
|---|---|
| All Shoes | [https://www.nordstrom.com/browse/shoes](https://www.nordstrom.com/browse/shoes) |
| New Arrivals | [https://www.nordstrom.com/browse/shoes/new](https://www.nordstrom.com/browse/shoes/new) |
| UGG Shoes | [https://www.nordstrom.com/brands/ugg-australia/shoes](https://www.nordstrom.com/brands/ugg-australia/shoes) |
| Gifts for the Sneaker Lover | [https://www.nordstrom.com/browse/gifts/by-category/sneakers](https://www.nordstrom.com/browse/gifts/by-category/sneakers) |
| Under $100 | [https://www.nordstrom.com/browse/shoes/under-100](https://www.nordstrom.com/browse/shoes/under-100) |
| Nordstrom Made Shoes | [https://www.nordstrom.com/browse/nordstrom-made/women/shoes](https://www.nordstrom.com/browse/nordstrom-made/women/shoes) |
| Sneaker Release Calendar | [https://www.nordstrom.com/browse/sneaker-releases](https://www.nordstrom.com/browse/sneaker-releases) |
| Now Featuring: On | [https://www.nordstrom.com/brands/on](https://www.nordstrom.com/brands/on) |
| On Trend: Shearling Shoes | [https://www.nordstrom.com/browse/style-guide/trend-edit/shearling-shoes](https://www.nordstrom.com/browse/style-guide/trend-edit/shearling-shoes) |
| On Trend: Dress Boots | [https://www.nordstrom.com/browse/style-guide/trend-edit/dress-boots](https://www.nordstrom.com/browse/style-guide/trend-edit/dress-boots) |
| Shoes Black Friday Sale | [https://www.nordstrom.com/browse/sale/shoes](https://www.nordstrom.com/browse/sale/shoes) |
| Women | [https://www.nordstrom.com/browse/women/shoes](https://www.nordstrom.com/browse/women/shoes) |
| Athletic & Sneakers | [https://www.nordstrom.com/browse/women/shoes/sneakers-athletic](https://www.nordstrom.com/browse/women/shoes/sneakers-athletic) |
| Booties | [https://www.nordstrom.com/browse/women/shoes/booties](https://www.nordstrom.com/browse/women/shoes/booties) |
| Boots | [https://www.nordstrom.com/browse/women/shoes/boots](https://www.nordstrom.com/browse/women/shoes/boots) |
| Clogs | [https://www.nordstrom.com/browse/women/shoes/clogs](https://www.nordstrom.com/browse/women/shoes/clogs) |
| Comfort | [https://www.nordstrom.com/browse/women/shoes/comfort](https://www.nordstrom.com/browse/women/shoes/comfort) |
| Dress Shoes | [https://www.nordstrom.com/browse/women/shoes/dress-shoes](https://www.nordstrom.com/browse/women/shoes/dress-shoes) |
| Flats | [https://www.nordstrom.com/browse/women/shoes/flats](https://www.nordstrom.com/browse/women/shoes/flats) |
| Heels | [https://www.nordstrom.com/browse/women/shoes/heels](https://www.nordstrom.com/browse/women/shoes/heels) |
| Loafers & Oxfords | [https://www.nordstrom.com/browse/women/shoes/oxfords-loafers](https://www.nordstrom.com/browse/women/shoes/oxfords-loafers) |
| Mules & Slides | [https://www.nordstrom.com/browse/women/shoes/mules-slides](https://www.nordstrom.com/browse/women/shoes/mules-slides) |
| Pumps | [https://www.nordstrom.com/browse/women/shoes/heels/pumps](https://www.nordstrom.com/browse/women/shoes/heels/pumps) |
| Slippers | [https://www.nordstrom.com/browse/women/shoes/slippers](https://www.nordstrom.com/browse/women/shoes/slippers) |
| Extended Sizes | [https://www.nordstrom.com/browse/women/shoes/extended-shoe-sizes](https://www.nordstrom.com/browse/women/shoes/extended-shoe-sizes) |
| Men | [https://www.nordstrom.com/browse/men/shoes](https://www.nordstrom.com/browse/men/shoes) |
| Athletic & Sneakers | [https://www.nordstrom.com/browse/men/shoes/sneakers-athletic](https://www.nordstrom.com/browse/men/shoes/sneakers-athletic) |
| Boots | [https://www.nordstrom.com/browse/men/shoes/boots](https://www.nordstrom.com/browse/men/shoes/boots) |
| Comfort | [https://www.nordstrom.com/browse/men/shoes/comfort](https://www.nordstrom.com/browse/men/shoes/comfort) |
| Dress Shoes | [https://www.nordstrom.com/browse/men/shoes/dress](https://www.nordstrom.com/browse/men/shoes/dress) |
| Loafers & Slip-Ons | [https://www.nordstrom.com/browse/men/shoes/loafers-slip-ons](https://www.nordstrom.com/browse/men/shoes/loafers-slip-ons) |
| Oxfords | [https://www.nordstrom.com/browse/men/shoes/oxfords](https://www.nordstrom.com/browse/men/shoes/oxfords) |
| Sandals & Flip-Flops | [https://www.nordstrom.com/browse/men/shoes/sandals](https://www.nordstrom.com/browse/men/shoes/sandals) |
| Slippers | [https://www.nordstrom.com/browse/men/shoes/slippers](https://www.nordstrom.com/browse/men/shoes/slippers) |
| Extended Sizes | [https://www.nordstrom.com/browse/men/shoes/extended-shoe-sizes](https://www.nordstrom.com/browse/men/shoes/extended-shoe-sizes) |
| Kids | [https://www.nordstrom.com/browse/kids/shoes](https://www.nordstrom.com/browse/kids/shoes) |
| Baby & Walker Shoes | [https://www.nordstrom.com/browse/kids/baby-walker-shoes](https://www.nordstrom.com/browse/kids/baby-walker-shoes) |
| Toddler (Sizes 7.5-12) | [https://www.nordstrom.com/browse/kids/shoes/toddler](https://www.nordstrom.com/browse/kids/shoes/toddler) |
| Little Kid (Sizes 12.5-3) | [https://www.nordstrom.com/browse/kids/shoes/little-kid](https://www.nordstrom.com/browse/kids/shoes/little-kid) |
| Big Kid (Sizes 3.5-7) | [https://www.nordstrom.com/browse/kids/shoes/big-kid](https://www.nordstrom.com/browse/kids/shoes/big-kid) |
| Girls' Shoes | [https://www.nordstrom.com/browse/kids/girls-shoes](https://www.nordstrom.com/browse/kids/girls-shoes) |
| Boys' Shoes | [https://www.nordstrom.com/browse/kids/boys-shoes](https://www.nordstrom.com/browse/kids/boys-shoes) |
| Athletic & Sneakers | [https://www.nordstrom.com/browse/kids/shoes/sneakers](https://www.nordstrom.com/browse/kids/shoes/sneakers) |
| Boots | [https://www.nordstrom.com/browse/kids/shoes/boots](https://www.nordstrom.com/browse/kids/shoes/boots) |
| Sandals | [https://www.nordstrom.com/browse/kids/shoes/sandals](https://www.nordstrom.com/browse/kids/shoes/sandals) |
| Slippers | [https://www.nordstrom.com/browse/kids/shoes/slippers](https://www.nordstrom.com/browse/kids/shoes/slippers) |
| Designer | [https://www.nordstrom.com/browse/shoes/designer](https://www.nordstrom.com/browse/shoes/designer) |
| Women | [https://www.nordstrom.com/browse/designer/women/shoes](https://www.nordstrom.com/browse/designer/women/shoes) |
| Men | [https://www.nordstrom.com/browse/designer/men/shoes](https://www.nordstrom.com/browse/designer/men/shoes) |
| Kids | [https://www.nordstrom.com/browse/designer/kids/shoes](https://www.nordstrom.com/browse/designer/kids/shoes) |
| Women's Contemporary Shoes | [https://www.nordstrom.com/browse/women/contemporary/shoes](https://www.nordstrom.com/browse/women/contemporary/shoes) |
| Men's Contemporary Shoes | [https://www.nordstrom.com/browse/men/mens-contemporary/shoes](https://www.nordstrom.com/browse/men/mens-contemporary/shoes) |
| Adaptive | [https://www.nordstrom.com/browse/adaptive-shoes](https://www.nordstrom.com/browse/adaptive-shoes) |
| Shoe Care & Accessories | [https://www.nordstrom.com/browse/shoes/care](https://www.nordstrom.com/browse/shoes/care) |
| Shoes Sale | [https://www.nordstrom.com/browse/sale/shoes?campaign=wf12633522-del2-gnpt7](https://www.nordstrom.com/browse/sale/shoes?campaign=wf12633522-del2-gnpt7) |

### Accessories

| Control | Destination |
|---|---|
| All Accessories | [https://www.nordstrom.com/browse/accessories](https://www.nordstrom.com/browse/accessories) |
| New Arrivals | [https://www.nordstrom.com/browse/accessories/new](https://www.nordstrom.com/browse/accessories/new) |
| Under $100 | [https://www.nordstrom.com/browse/accessories/under-100](https://www.nordstrom.com/browse/accessories/under-100) |
| Nordstrom Made Accessories | [https://www.nordstrom.com/browse/nordstrom-made/accessories](https://www.nordstrom.com/browse/nordstrom-made/accessories) |
| Cold-Weather Accessories | [https://www.nordstrom.com/browse/cold-weather/accessories](https://www.nordstrom.com/browse/cold-weather/accessories) |
| On Trend: Onyx Jewelry | [https://www.nordstrom.com/browse/style-guide/trend-edit/onyx-jewelry](https://www.nordstrom.com/browse/style-guide/trend-edit/onyx-jewelry) |
| Fine Jewelry Trunk Show | [https://www.nordstrom.com/browse/women/jewelry/trunk-shows](https://www.nordstrom.com/browse/women/jewelry/trunk-shows) |
| Accessories Gifts | [https://www.nordstrom.com/browse/gifts/by-category/accessories](https://www.nordstrom.com/browse/gifts/by-category/accessories) |
| Accessories Black Friday Sale | [https://www.nordstrom.com/browse/sale/accessories](https://www.nordstrom.com/browse/sale/accessories) |
| Women's Accessories | [https://www.nordstrom.com/browse/women/accessories](https://www.nordstrom.com/browse/women/accessories) |
| Belts | [https://www.nordstrom.com/browse/women/accessories/belts](https://www.nordstrom.com/browse/women/accessories/belts) |
| Hair Accessories | [https://www.nordstrom.com/browse/women/accessories/hair-accessories](https://www.nordstrom.com/browse/women/accessories/hair-accessories) |
| Hats | [https://www.nordstrom.com/browse/women/accessories/hats](https://www.nordstrom.com/browse/women/accessories/hats) |
| Scarves & Wraps | [https://www.nordstrom.com/browse/women/accessories/scarves-wraps](https://www.nordstrom.com/browse/women/accessories/scarves-wraps) |
| Women's Handbags | [https://www.nordstrom.com/browse/women/handbags](https://www.nordstrom.com/browse/women/handbags) |
| Backpacks | [https://www.nordstrom.com/browse/women/handbags/backpacks](https://www.nordstrom.com/browse/women/handbags/backpacks) |
| Belt Bags & Sling Bags | [https://www.nordstrom.com/browse/women/handbags/belt-bags-slings](https://www.nordstrom.com/browse/women/handbags/belt-bags-slings) |
| Clutches & Pouches | [https://www.nordstrom.com/browse/women/handbags/clutches](https://www.nordstrom.com/browse/women/handbags/clutches) |
| Crossbody Bags | [https://www.nordstrom.com/browse/women/handbags/crossbody](https://www.nordstrom.com/browse/women/handbags/crossbody) |
| Party Bags | [https://www.nordstrom.com/browse/women/handbags/evening-bags](https://www.nordstrom.com/browse/women/handbags/evening-bags) |
| Satchels | [https://www.nordstrom.com/browse/women/handbags/satchels](https://www.nordstrom.com/browse/women/handbags/satchels) |
| Shoulder Bags | [https://www.nordstrom.com/browse/women/handbags/shoulder-bags](https://www.nordstrom.com/browse/women/handbags/shoulder-bags) |
| Slouchy Bags | [https://www.nordstrom.com/browse/women/handbags/hobo](https://www.nordstrom.com/browse/women/handbags/hobo) |
| Tote Bags | [https://www.nordstrom.com/browse/women/handbags/totes](https://www.nordstrom.com/browse/women/handbags/totes) |
| Wallets & Card Cases | [https://www.nordstrom.com/browse/women/handbags/wallets](https://www.nordstrom.com/browse/women/handbags/wallets) |
| Women's Sunglasses & Eyewear | [https://www.nordstrom.com/browse/women/accessories/sunglasses](https://www.nordstrom.com/browse/women/accessories/sunglasses) |
| Designer Sunglasses & Eyewear | [https://www.nordstrom.com/browse/women/accessories/sunglasses/designer-sunglasses-eyewear](https://www.nordstrom.com/browse/women/accessories/sunglasses/designer-sunglasses-eyewear) |
| Women's Jewelry | [https://www.nordstrom.com/browse/women/jewelry](https://www.nordstrom.com/browse/women/jewelry) |
| Bracelets | [https://www.nordstrom.com/browse/women/jewelry/bracelets](https://www.nordstrom.com/browse/women/jewelry/bracelets) |
| Earrings | [https://www.nordstrom.com/browse/women/jewelry/earrings](https://www.nordstrom.com/browse/women/jewelry/earrings) |
| Necklaces | [https://www.nordstrom.com/browse/women/jewelry/necklaces](https://www.nordstrom.com/browse/women/jewelry/necklaces) |
| Rings | [https://www.nordstrom.com/browse/women/jewelry/rings](https://www.nordstrom.com/browse/women/jewelry/rings) |
| Watches | [https://www.nordstrom.com/browse/women/jewelry/watches](https://www.nordstrom.com/browse/women/jewelry/watches) |
| Women's Fine Jewelry | [https://www.nordstrom.com/browse/women/jewelry/fine](https://www.nordstrom.com/browse/women/jewelry/fine) |
| Bracelets | [https://www.nordstrom.com/browse/women/jewelry/fine/bracelets](https://www.nordstrom.com/browse/women/jewelry/fine/bracelets) |
| Earrings | [https://www.nordstrom.com/browse/women/jewelry/fine/earrings](https://www.nordstrom.com/browse/women/jewelry/fine/earrings) |
| Necklaces | [https://www.nordstrom.com/browse/women/jewelry/fine/necklaces](https://www.nordstrom.com/browse/women/jewelry/fine/necklaces) |
| Rings | [https://www.nordstrom.com/browse/women/jewelry/fine/rings](https://www.nordstrom.com/browse/women/jewelry/fine/rings) |
| Luxury Watches | [https://www.nordstrom.com/browse/women/jewelry/watches/luxury-watches](https://www.nordstrom.com/browse/women/jewelry/watches/luxury-watches) |
| Wedding & Engagement Rings | [https://www.nordstrom.com/browse/women/jewelry/fine/engagement-rings](https://www.nordstrom.com/browse/women/jewelry/fine/engagement-rings) |
| MUSE @ Nordstrom | [https://www.nordstrom.com/browse/women/jewelry/fine/muse](https://www.nordstrom.com/browse/women/jewelry/fine/muse) |
| Experience Fine Jewelry | [https://www.nordstrom.com/browse/women/jewelry/fine/experience-fine](https://www.nordstrom.com/browse/women/jewelry/fine/experience-fine) |
| Men's Sunglasses & Eyewear | [https://www.nordstrom.com/browse/men/accessories/sunglasses](https://www.nordstrom.com/browse/men/accessories/sunglasses) |
| Designer Sunglasses & Eyewear | [https://www.nordstrom.com/browse/men/accessories/sunglasses/designer-sunglasses-eyewear](https://www.nordstrom.com/browse/men/accessories/sunglasses/designer-sunglasses-eyewear) |
| Men's Accessories | [https://www.nordstrom.com/browse/men/accessories](https://www.nordstrom.com/browse/men/accessories) |
| Belts | [https://www.nordstrom.com/browse/men/accessories/belts](https://www.nordstrom.com/browse/men/accessories/belts) |
| Hats | [https://www.nordstrom.com/browse/men/accessories/hats](https://www.nordstrom.com/browse/men/accessories/hats) |
| Scarves | [https://www.nordstrom.com/browse/men/accessories/scarves](https://www.nordstrom.com/browse/men/accessories/scarves) |
| Ties & Pocket Squares | [https://www.nordstrom.com/browse/men/accessories/ties-pocket-squares](https://www.nordstrom.com/browse/men/accessories/ties-pocket-squares) |
| Men's Bags | [https://www.nordstrom.com/browse/men/accessories/bags-backpacks](https://www.nordstrom.com/browse/men/accessories/bags-backpacks) |
| Backpacks | [https://www.nordstrom.com/browse/men/accessories/bags-backpacks/backpacks](https://www.nordstrom.com/browse/men/accessories/bags-backpacks/backpacks) |
| Crossbody & Sling Bags | [https://www.nordstrom.com/browse/men/accessories/bags-backpacks/crossbody-sling](https://www.nordstrom.com/browse/men/accessories/bags-backpacks/crossbody-sling) |
| Wallets & Card Cases | [https://www.nordstrom.com/browse/men/accessories/wallets](https://www.nordstrom.com/browse/men/accessories/wallets) |
| Men's Jewelry & Watches | [https://www.nordstrom.com/browse/men/jewelry](https://www.nordstrom.com/browse/men/jewelry) |
| Fine Jewelry | [https://www.nordstrom.com/browse/men/jewelry/fine](https://www.nordstrom.com/browse/men/jewelry/fine) |
| Watches | [https://www.nordstrom.com/browse/men/jewelry/watches](https://www.nordstrom.com/browse/men/jewelry/watches) |
| Luxury Watches | [https://www.nordstrom.com/browse/men/jewelry/watches/luxury-watches](https://www.nordstrom.com/browse/men/jewelry/watches/luxury-watches) |
| Luggage & Travel Bags | [https://www.nordstrom.com/browse/home/luggage-travel](https://www.nordstrom.com/browse/home/luggage-travel) |
| Women's Designer Accessories | [https://www.nordstrom.com/browse/designer/women/accessories](https://www.nordstrom.com/browse/designer/women/accessories) |
| Men's Designer Accessories | [https://www.nordstrom.com/browse/designer/men/accessories](https://www.nordstrom.com/browse/designer/men/accessories) |
| Accessories Sale | [https://www.nordstrom.com/browse/sale/accessories?campaign=wf12633522-del2-gnpt5](https://www.nordstrom.com/browse/sale/accessories?campaign=wf12633522-del2-gnpt5) |

### Kids

| Control | Destination |
|---|---|
| All Kids | [https://www.nordstrom.com/browse/kids](https://www.nordstrom.com/browse/kids) |
| New Arrivals | [https://www.nordstrom.com/browse/kids/new](https://www.nordstrom.com/browse/kids/new) |
| Under $25 | [https://www.nordstrom.com/browse/kids/under-25](https://www.nordstrom.com/browse/kids/under-25) |
| Baby Shower Gifts | [https://www.nordstrom.com/browse/kids/baby/shower-gifts](https://www.nordstrom.com/browse/kids/baby/shower-gifts) |
| Nordstrom Made | [https://www.nordstrom.com/browse/nordstrom-made/kids](https://www.nordstrom.com/browse/nordstrom-made/kids) |
| UGG for Kids | [https://www.nordstrom.com/brands/ugg-australia/kids](https://www.nordstrom.com/brands/ugg-australia/kids) |
| Cold-Weather Shop | [https://www.nordstrom.com/browse/cold-weather/kids](https://www.nordstrom.com/browse/cold-weather/kids) |
| Kids' Black Friday Sale | [https://www.nordstrom.com/browse/sale/kids](https://www.nordstrom.com/browse/sale/kids) |
| Gifts for Kids | [https://www.nordstrom.com/browse/gifts/for-kids](https://www.nordstrom.com/browse/gifts/for-kids) |
| For Girls | [https://www.nordstrom.com/browse/gifts/for-kids/for-girls](https://www.nordstrom.com/browse/gifts/for-kids/for-girls) |
| For Boys | [https://www.nordstrom.com/browse/gifts/for-kids/for-boys](https://www.nordstrom.com/browse/gifts/for-kids/for-boys) |
| Stocking Stuffers | [https://www.nordstrom.com/browse/holiday-gifts/stocking-stuffers/kids](https://www.nordstrom.com/browse/holiday-gifts/stocking-stuffers/kids) |
| Toys | [https://www.nordstrom.com/browse/kids/toys](https://www.nordstrom.com/browse/kids/toys) |
| FAO Schwarz | [https://www.nordstrom.com/browse/kids/toys/fao-schwarz](https://www.nordstrom.com/browse/kids/toys/fao-schwarz) |
| Games | [https://www.nordstrom.com/browse/kids/toys/games](https://www.nordstrom.com/browse/kids/toys/games) |
| Pretend Play | [https://www.nordstrom.com/browse/kids/toys/pretend-play](https://www.nordstrom.com/browse/kids/toys/pretend-play) |
| Stuffed Animals | [https://www.nordstrom.com/browse/kids/toys/stuffed-animals](https://www.nordstrom.com/browse/kids/toys/stuffed-animals) |
| Jellycat | [https://www.nordstrom.com/brands/jellycat](https://www.nordstrom.com/brands/jellycat) |
| Kids' Shoes | [https://www.nordstrom.com/browse/kids/shoes](https://www.nordstrom.com/browse/kids/shoes) |
| Baby & Walker Shoes | [https://www.nordstrom.com/browse/kids/baby-walker-shoes](https://www.nordstrom.com/browse/kids/baby-walker-shoes) |
| Toddler (Sizes 7.5-12) | [https://www.nordstrom.com/browse/kids/shoes/toddler](https://www.nordstrom.com/browse/kids/shoes/toddler) |
| Little Kid (Sizes 12.5-3) | [https://www.nordstrom.com/browse/kids/shoes/little-kid](https://www.nordstrom.com/browse/kids/shoes/little-kid) |
| Big Kid (Sizes 3.5-7) | [https://www.nordstrom.com/browse/kids/shoes/big-kid](https://www.nordstrom.com/browse/kids/shoes/big-kid) |
| Girls' Clothing | [https://www.nordstrom.com/browse/kids/girls-clothing](https://www.nordstrom.com/browse/kids/girls-clothing) |
| Toddler & Little Girl (Sizes 2T-6X) | [https://www.nordstrom.com/browse/kids/girls/clothing-sizes-2t-6x](https://www.nordstrom.com/browse/kids/girls/clothing-sizes-2t-6x) |
| Girls (Sizes 7-20) | [https://www.nordstrom.com/browse/kids/girls/clothing-sizes-7-16](https://www.nordstrom.com/browse/kids/girls/clothing-sizes-7-16) |
| Tween | [https://www.nordstrom.com/browse/kids/girls/tween-clothing](https://www.nordstrom.com/browse/kids/girls/tween-clothing) |
| Girls' Accessories | [https://www.nordstrom.com/browse/kids/girls/accessories](https://www.nordstrom.com/browse/kids/girls/accessories) |
| Boys' Clothing | [https://www.nordstrom.com/browse/kids/boys-clothing](https://www.nordstrom.com/browse/kids/boys-clothing) |
| Toddler & Little Boy (Sizes 2T-7) | [https://www.nordstrom.com/browse/kids/boys/clothing-sizes-2t-7](https://www.nordstrom.com/browse/kids/boys/clothing-sizes-2t-7) |
| Boys (Sizes 8-20) | [https://www.nordstrom.com/browse/kids/boys/clothing-sizes-8-20](https://www.nordstrom.com/browse/kids/boys/clothing-sizes-8-20) |
| Boys' Accessories | [https://www.nordstrom.com/browse/kids/boys/accessories](https://www.nordstrom.com/browse/kids/boys/accessories) |
| Baby Clothing | [https://www.nordstrom.com/browse/kids/baby-clothing](https://www.nordstrom.com/browse/kids/baby-clothing) |
| Baby Girl Clothing (0-24M) | [https://www.nordstrom.com/browse/kids/baby/girl-clothing](https://www.nordstrom.com/browse/kids/baby/girl-clothing) |
| Baby Boy Clothing (0-24M) | [https://www.nordstrom.com/browse/kids/baby/boy-clothing](https://www.nordstrom.com/browse/kids/baby/boy-clothing) |
| Unisex Baby Clothing (0-24M) | [https://www.nordstrom.com/browse/kids/baby/unisex-clothing](https://www.nordstrom.com/browse/kids/baby/unisex-clothing) |
| Baby Gear & Essentials | [https://www.nordstrom.com/browse/kids/baby-gear](https://www.nordstrom.com/browse/kids/baby-gear) |
| Baby Carriers | [https://www.nordstrom.com/browse/kids/baby-gear/carriers](https://www.nordstrom.com/browse/kids/baby-gear/carriers) |
| Bath & Safety | [https://www.nordstrom.com/browse/kids/baby-gear/bath-safety](https://www.nordstrom.com/browse/kids/baby-gear/bath-safety) |
| Blankets & Swaddles | [https://www.nordstrom.com/browse/kids/baby-gear/blankets](https://www.nordstrom.com/browse/kids/baby-gear/blankets) |
| Car Seats | [https://www.nordstrom.com/browse/kids/baby-gear/car-seats](https://www.nordstrom.com/browse/kids/baby-gear/car-seats) |
| Diaper Bags | [https://www.nordstrom.com/browse/diaper-bags](https://www.nordstrom.com/browse/diaper-bags) |
| Feeding | [https://www.nordstrom.com/browse/kids/baby-gear/feeding](https://www.nordstrom.com/browse/kids/baby-gear/feeding) |
| High Chairs | [https://www.nordstrom.com/browse/kids/baby-gear/highchairs](https://www.nordstrom.com/browse/kids/baby-gear/highchairs) |
| Strollers | [https://www.nordstrom.com/browse/kids/baby-gear/strollers](https://www.nordstrom.com/browse/kids/baby-gear/strollers) |
| Baby Accessories | [https://www.nordstrom.com/browse/kids/baby/accessories](https://www.nordstrom.com/browse/kids/baby/accessories) |
| Holiday Outfits | [https://www.nordstrom.com/browse/holiday-party-outfits/kids](https://www.nordstrom.com/browse/holiday-party-outfits/kids) |
| Baby's First Holiday | [https://www.nordstrom.com/browse/kids/first-holiday](https://www.nordstrom.com/browse/kids/first-holiday) |
| Casual Holiday Outfits | [https://www.nordstrom.com/browse/holiday-party-outfits/kids/holiday-casual](https://www.nordstrom.com/browse/holiday-party-outfits/kids/holiday-casual) |
| Holiday Pajamas | [https://www.nordstrom.com/browse/holiday-gifts/family-pajamas/kids](https://www.nordstrom.com/browse/holiday-gifts/family-pajamas/kids) |
| Holiday Party Outfits | [https://www.nordstrom.com/browse/holiday-party-outfits/kids/holiday-party](https://www.nordstrom.com/browse/holiday-party-outfits/kids/holiday-party) |
| Shop by Occasion & Holidays | [https://www.nordstrom.com/browse/kids/occasion](https://www.nordstrom.com/browse/kids/occasion) |
| Special Occasions | [https://www.nordstrom.com/browse/kids/special-occasion](https://www.nordstrom.com/browse/kids/special-occasion) |
| Vacation & Warm Weather | [https://www.nordstrom.com/browse/vacation/kids](https://www.nordstrom.com/browse/vacation/kids) |
| Kids' Sale | [https://www.nordstrom.com/browse/sale/kids?campaign=wf12633522-del2-gnpt4](https://www.nordstrom.com/browse/sale/kids?campaign=wf12633522-del2-gnpt4) |

### Designer

| Control | Destination |
|---|---|
| All Designer | [https://www.nordstrom.com/browse/designer](https://www.nordstrom.com/browse/designer) |
| Luxury Gifts | [https://www.nordstrom.com/browse/gifts/by-price/luxe-gifts](https://www.nordstrom.com/browse/gifts/by-price/luxe-gifts) |
| Designer New Arrivals | [https://www.nordstrom.com/browse/designer/new](https://www.nordstrom.com/browse/designer/new) |
| Designer Style Guide | [https://www.nordstrom.com/browse/style-guide/designer](https://www.nordstrom.com/browse/style-guide/designer) |
| The Edit | [https://www.nordstrom.com/browse/designer/the-edit](https://www.nordstrom.com/browse/designer/the-edit) |
| New Designers to Nordstrom | [https://www.nordstrom.com/browse/designer/new-designer-brands](https://www.nordstrom.com/browse/designer/new-designer-brands) |
| Celebrations | [https://www.nordstrom.com/browse/designer/designer-event-dressing](https://www.nordstrom.com/browse/designer/designer-event-dressing) |
| Travel & Resort | [https://www.nordstrom.com/browse/designer/vacation](https://www.nordstrom.com/browse/designer/vacation) |
| Work | [https://www.nordstrom.com/browse/designer/tailoring](https://www.nordstrom.com/browse/designer/tailoring) |
| Cold Weather | [https://www.nordstrom.com/browse/designer/designer-cozy](https://www.nordstrom.com/browse/designer/designer-cozy) |
| Designer Sale | [https://www.nordstrom.com/browse/sale/designer](https://www.nordstrom.com/browse/sale/designer) |
| Designer Brands | [https://www.nordstrom.com/browse/designer/brands](https://www.nordstrom.com/browse/designer/brands) |
| Alaïa | [https://www.nordstrom.com/brands/alaia](https://www.nordstrom.com/brands/alaia) |
| Balenciaga | [https://www.nordstrom.com/brands/balenciaga](https://www.nordstrom.com/brands/balenciaga) |
| Bottega Veneta | [https://www.nordstrom.com/brands/bottega-veneta](https://www.nordstrom.com/brands/bottega-veneta) |
| Burberry | [https://www.nordstrom.com/brands/burberry](https://www.nordstrom.com/brands/burberry) |
| CHANEL | [https://www.nordstrom.com/brands/chanel/discover/chanel-fashion](https://www.nordstrom.com/brands/chanel/discover/chanel-fashion) |
| Chloé | [https://www.nordstrom.com/brands/chloe](https://www.nordstrom.com/brands/chloe) |
| Christian Louboutin | [https://www.nordstrom.com/brands/christian-louboutin](https://www.nordstrom.com/brands/christian-louboutin) |
| FERRAGAMO | [https://www.nordstrom.com/brands/ferragamo](https://www.nordstrom.com/brands/ferragamo) |
| Givenchy | [https://www.nordstrom.com/brands/givenchy](https://www.nordstrom.com/brands/givenchy) |
| Gucci | [https://www.nordstrom.com/brands/gucci](https://www.nordstrom.com/brands/gucci) |
| McQueen | [https://www.nordstrom.com/brands/mcqueen](https://www.nordstrom.com/brands/mcqueen) |
| Miu Miu | [https://www.nordstrom.com/brands/miu-miu](https://www.nordstrom.com/brands/miu-miu) |
| Moncler | [https://www.nordstrom.com/brands/moncler](https://www.nordstrom.com/brands/moncler) |
| Prada | [https://www.nordstrom.com/brands/prada](https://www.nordstrom.com/brands/prada) |
| Saint Laurent | [https://www.nordstrom.com/brands/saint-laurent](https://www.nordstrom.com/brands/saint-laurent) |
| The Row | [https://www.nordstrom.com/brands/the-row/store-locations](https://www.nordstrom.com/brands/the-row/store-locations) |
| TOM FORD | [https://www.nordstrom.com/brands/tom-ford](https://www.nordstrom.com/brands/tom-ford) |
| Women | [https://www.nordstrom.com/browse/designer/women](https://www.nordstrom.com/browse/designer/women) |
| Designer Clothing | [https://www.nordstrom.com/browse/designer/women/clothing](https://www.nordstrom.com/browse/designer/women/clothing) |
| Designer Shoes | [https://www.nordstrom.com/browse/designer/women/shoes](https://www.nordstrom.com/browse/designer/women/shoes) |
| Designer Handbags | [https://www.nordstrom.com/browse/designer/women/handbags](https://www.nordstrom.com/browse/designer/women/handbags) |
| Designer Dresses | [https://www.nordstrom.com/browse/designer/women/clothing/dresses](https://www.nordstrom.com/browse/designer/women/clothing/dresses) |
| Designer Jewelry & Watches | [https://www.nordstrom.com/browse/designer/women/jewelry](https://www.nordstrom.com/browse/designer/women/jewelry) |
| Designer Accessories | [https://www.nordstrom.com/browse/designer/women/accessories](https://www.nordstrom.com/browse/designer/women/accessories) |
| Men | [https://www.nordstrom.com/browse/designer/men](https://www.nordstrom.com/browse/designer/men) |
| Designer Clothing | [https://www.nordstrom.com/browse/designer/men/clothing](https://www.nordstrom.com/browse/designer/men/clothing) |
| Designer Shoes | [https://www.nordstrom.com/browse/designer/men/shoes](https://www.nordstrom.com/browse/designer/men/shoes) |
| Designer Accessories | [https://www.nordstrom.com/browse/designer/men/accessories](https://www.nordstrom.com/browse/designer/men/accessories) |
| Designer Beauty & Fragrance | [https://www.nordstrom.com/browse/beauty/designer-beauty](https://www.nordstrom.com/browse/beauty/designer-beauty) |
| SPACE: Emerging & Advanced Designer | [https://www.nordstrom.com/browse/designer/space](https://www.nordstrom.com/browse/designer/space) |
| Clothing | [https://www.nordstrom.com/browse/designer/space/ready-to-wear](https://www.nordstrom.com/browse/designer/space/ready-to-wear) |
| Dresses | [https://www.nordstrom.com/browse/designer/space/ready-to-wear/dresses](https://www.nordstrom.com/browse/designer/space/ready-to-wear/dresses) |
| Accessories | [https://www.nordstrom.com/browse/designer/space/accessories](https://www.nordstrom.com/browse/designer/space/accessories) |
| Shoes | [https://www.nordstrom.com/browse/designer/space/shoes](https://www.nordstrom.com/browse/designer/space/shoes) |
| Handbags | [https://www.nordstrom.com/browse/designer/space/handbags](https://www.nordstrom.com/browse/designer/space/handbags) |
| Men's Emerging & Advanced Designer | [https://www.nordstrom.com/browse/designer/mens-emerging](https://www.nordstrom.com/browse/designer/mens-emerging) |
| Clothing | [https://www.nordstrom.com/browse/designer/mens-emerging/clothing](https://www.nordstrom.com/browse/designer/mens-emerging/clothing) |
| Shoes | [https://www.nordstrom.com/browse/designer/mens-emerging/shoes](https://www.nordstrom.com/browse/designer/mens-emerging/shoes) |
| Accessories | [https://www.nordstrom.com/browse/designer/mens-emerging/accessories](https://www.nordstrom.com/browse/designer/mens-emerging/accessories) |
| Designer Sale | [https://www.nordstrom.com/browse/sale/designer?campaign=wf13456372-del24-gnpt](https://www.nordstrom.com/browse/sale/designer?campaign=wf13456372-del24-gnpt) |

### Home

| Control | Destination |
|---|---|
| All Home | [https://www.nordstrom.com/browse/home](https://www.nordstrom.com/browse/home) |
| New Arrivals | [https://www.nordstrom.com/browse/home/new](https://www.nordstrom.com/browse/home/new) |
| Under $100 | [https://www.nordstrom.com/browse/home/under-100](https://www.nordstrom.com/browse/home/under-100) |
| Nordstrom Made | [https://www.nordstrom.com/browse/nordstrom-made/home](https://www.nordstrom.com/browse/nordstrom-made/home) |
| Hosting Essentials | [https://www.nordstrom.com/browse/home/hosting-essentials](https://www.nordstrom.com/browse/home/hosting-essentials) |
| Fall Home | [https://www.nordstrom.com/browse/home/fall-harvest](https://www.nordstrom.com/browse/home/fall-harvest) |
| UGG for the Home | [https://www.nordstrom.com/brands/ugg-australia/home](https://www.nordstrom.com/brands/ugg-australia/home) |
| Home Black Friday Sale | [https://www.nordstrom.com/browse/sale/home](https://www.nordstrom.com/browse/sale/home) |
| Home Gifts | [https://www.nordstrom.com/browse/gifts/by-category/home](https://www.nordstrom.com/browse/gifts/by-category/home) |
| Advent Calendars | [https://www.nordstrom.com/browse/holiday-gifts/advent-calendars](https://www.nordstrom.com/browse/holiday-gifts/advent-calendars) |
| Cozy Gifts for Home | [https://www.nordstrom.com/browse/gifts/by-category/cozy/home](https://www.nordstrom.com/browse/gifts/by-category/cozy/home) |
| Foodie Gifts | [https://www.nordstrom.com/browse/gifts/by-category/home/foodie-gifts](https://www.nordstrom.com/browse/gifts/by-category/home/foodie-gifts) |
| For the Party Host | [https://www.nordstrom.com/browse/gifts/by-category/party-host-gifts](https://www.nordstrom.com/browse/gifts/by-category/party-host-gifts) |
| Housewarming Gifts | [https://www.nordstrom.com/browse/home/home/housewarming-gifts](https://www.nordstrom.com/browse/home/home/housewarming-gifts) |
| Tech Gifts | [https://www.nordstrom.com/browse/home/electronics](https://www.nordstrom.com/browse/home/electronics) |
| Wedding & Engagement Gifts | [https://www.nordstrom.com/browse/wedding/newlyweds](https://www.nordstrom.com/browse/wedding/newlyweds) |
| Holiday Decor | [https://www.nordstrom.com/browse/home/holiday-decor](https://www.nordstrom.com/browse/home/holiday-decor) |
| Holiday Candles & Diffusers | [https://www.nordstrom.com/browse/home/holiday-decor/candles-diffusers](https://www.nordstrom.com/browse/home/holiday-decor/candles-diffusers) |
| Holiday Kitchen & Dining | [https://www.nordstrom.com/browse/home/holiday-decor/tabletop-kitchen](https://www.nordstrom.com/browse/home/holiday-decor/tabletop-kitchen) |
| Ornaments & Toppers | [https://www.nordstrom.com/browse/home/holiday-decor/ornaments](https://www.nordstrom.com/browse/home/holiday-decor/ornaments) |
| Trees, Wreaths & Accessories | [https://www.nordstrom.com/browse/home/holiday-decor/trees](https://www.nordstrom.com/browse/home/holiday-decor/trees) |
| Bath | [https://www.nordstrom.com/browse/home/bath](https://www.nordstrom.com/browse/home/bath) |
| Bath Accessories | [https://www.nordstrom.com/browse/home/bath/bathroom-accessories](https://www.nordstrom.com/browse/home/bath/bathroom-accessories) |
| Towels | [https://www.nordstrom.com/browse/home/bath/towels](https://www.nordstrom.com/browse/home/bath/towels) |
| Bedding | [https://www.nordstrom.com/browse/home/bedding](https://www.nordstrom.com/browse/home/bedding) |
| Bedding Essentials & Pillows | [https://www.nordstrom.com/browse/home/bedding/basics](https://www.nordstrom.com/browse/home/bedding/basics) |
| Bedding Sets | [https://www.nordstrom.com/browse/home/bedding/sets](https://www.nordstrom.com/browse/home/bedding/sets) |
| Comforters, Coverlets & Quilts | [https://www.nordstrom.com/browse/home/bedding/comforters](https://www.nordstrom.com/browse/home/bedding/comforters) |
| Duvet Covers & Shams | [https://www.nordstrom.com/browse/home/bedding/duvet-covers](https://www.nordstrom.com/browse/home/bedding/duvet-covers) |
| Sheets | [https://www.nordstrom.com/browse/home/bedding/sheets](https://www.nordstrom.com/browse/home/bedding/sheets) |
| Blankets & Throws | [https://www.nordstrom.com/browse/home/bedding/blankets-throws](https://www.nordstrom.com/browse/home/bedding/blankets-throws) |
| Travel Essentials | [https://www.nordstrom.com/browse/home/travel-essentials](https://www.nordstrom.com/browse/home/travel-essentials) |
| Luggage & Travel Bags | [https://www.nordstrom.com/browse/home/luggage-travel](https://www.nordstrom.com/browse/home/luggage-travel) |
| Home Decor | [https://www.nordstrom.com/browse/home/decor](https://www.nordstrom.com/browse/home/decor) |
| Art Prints & Wall Decor | [https://www.nordstrom.com/browse/home/decor/wall](https://www.nordstrom.com/browse/home/decor/wall) |
| Books, Games & Puzzles | [https://www.nordstrom.com/browse/home/decor/books-games-puzzles](https://www.nordstrom.com/browse/home/decor/books-games-puzzles) |
| Decorative Accents | [https://www.nordstrom.com/browse/home/decor/accents](https://www.nordstrom.com/browse/home/decor/accents) |
| Decorative Pillows | [https://www.nordstrom.com/browse/home/decor/decorative-pillows](https://www.nordstrom.com/browse/home/decor/decorative-pillows) |
| Lighting & Lamps | [https://www.nordstrom.com/browse/home/decor/lighting](https://www.nordstrom.com/browse/home/decor/lighting) |
| Picture Frames | [https://www.nordstrom.com/browse/home/decor/picture-frames](https://www.nordstrom.com/browse/home/decor/picture-frames) |
| Rugs | [https://www.nordstrom.com/browse/home/decor/rugs](https://www.nordstrom.com/browse/home/decor/rugs) |
| Storage & Organization | [https://www.nordstrom.com/browse/home/decor/storage-organization](https://www.nordstrom.com/browse/home/decor/storage-organization) |
| Vases & Planters | [https://www.nordstrom.com/browse/home/decor/vases](https://www.nordstrom.com/browse/home/decor/vases) |
| Candles & Diffusers | [https://www.nordstrom.com/browse/home/decor/candles-diffusers](https://www.nordstrom.com/browse/home/decor/candles-diffusers) |
| Electronics & Speakers | [https://www.nordstrom.com/browse/home/electronics](https://www.nordstrom.com/browse/home/electronics) |
| Kitchen | [https://www.nordstrom.com/browse/home/kitchenware](https://www.nordstrom.com/browse/home/kitchenware) |
| Coffee & Tea Accessories | [https://www.nordstrom.com/browse/home/kitchenware/coffee-tea-accessories](https://www.nordstrom.com/browse/home/kitchenware/coffee-tea-accessories) |
| Cookware & Bakeware | [https://www.nordstrom.com/browse/home/kitchenware/cookware-bakeware](https://www.nordstrom.com/browse/home/kitchenware/cookware-bakeware) |
| Cutlery & Knives | [https://www.nordstrom.com/browse/home/kitchenware/kitchen-knives](https://www.nordstrom.com/browse/home/kitchenware/kitchen-knives) |
| Kitchen Linens | [https://www.nordstrom.com/browse/home/kitchenware/kitchen-linens](https://www.nordstrom.com/browse/home/kitchenware/kitchen-linens) |
| Small Appliances | [https://www.nordstrom.com/browse/home/kitchenware/appliances](https://www.nordstrom.com/browse/home/kitchenware/appliances) |
| Utensils & Gadgets | [https://www.nordstrom.com/browse/home/kitchenware/storage-gadgets](https://www.nordstrom.com/browse/home/kitchenware/storage-gadgets) |
| Tabletop & Dining | [https://www.nordstrom.com/browse/home/dining-entertainment](https://www.nordstrom.com/browse/home/dining-entertainment) |
| Bar Tools & Accessories | [https://www.nordstrom.com/browse/home/kitchenware/bar-tools](https://www.nordstrom.com/browse/home/kitchenware/bar-tools) |
| Dinnerware | [https://www.nordstrom.com/browse/home/dining-entertainment/dinnerware](https://www.nordstrom.com/browse/home/dining-entertainment/dinnerware) |
| Drinkware & Mugs | [https://www.nordstrom.com/browse/home/dining-entertainment/mugs](https://www.nordstrom.com/browse/home/dining-entertainment/mugs) |
| Glassware | [https://www.nordstrom.com/browse/home/dining-entertainment/drinkware-barware](https://www.nordstrom.com/browse/home/dining-entertainment/drinkware-barware) |
| Serveware | [https://www.nordstrom.com/browse/home/dining-entertainment/serveware](https://www.nordstrom.com/browse/home/dining-entertainment/serveware) |
| Pantry, Food & Candy | [https://www.nordstrom.com/browse/home/pantry](https://www.nordstrom.com/browse/home/pantry) |
| Water Bottles & Tumblers | [https://www.nordstrom.com/browse/home/water-bottles-tumblers](https://www.nordstrom.com/browse/home/water-bottles-tumblers) |
| Pet Accessories | [https://www.nordstrom.com/browse/home/pet-accessories](https://www.nordstrom.com/browse/home/pet-accessories) |
| Home Sale | [https://www.nordstrom.com/browse/sale/home?campaign=wf12633522-del2-gnpt6](https://www.nordstrom.com/browse/sale/home?campaign=wf12633522-del2-gnpt6) |

### Services

| Control | Destination |
|---|---|
| All Services | [https://www.nordstrom.com/browse/services](https://www.nordstrom.com/browse/services) |
| Celebrating 125 Years | [https://www.nordstrom.com/browse/125-anniversary](https://www.nordstrom.com/browse/125-anniversary) |
| About Us | [https://www.nordstrom.com/browse/about](https://www.nordstrom.com/browse/about) |
| Company History | [https://www.nordstrom.com/browse/about/company-history](https://www.nordstrom.com/browse/about/company-history) |
| Nordy Pod | [https://www.nordstrom.com/browse/about/nordy-podcast](https://www.nordstrom.com/browse/about/nordy-podcast) |
| Nordstrom Local | [https://www.nordstrom.com/browse/services/nordstrom-local](https://www.nordstrom.com/browse/services/nordstrom-local) |
| Nordstrom Restaurants | [https://www.nordstrom.com/browse/about/nordstrom-restaurants](https://www.nordstrom.com/browse/about/nordstrom-restaurants) |
| Our Impact | [https://www.nordstrom.com/browse/impact](https://www.nordstrom.com/browse/impact) |
| Find a Store | [https://www.nordstrom.com/stores](https://www.nordstrom.com/stores) |
| Shop Gift Cards | [https://www.nordstrom.com/browse/customer-service/gift-card-info](https://www.nordstrom.com/browse/customer-service/gift-card-info) |
| Check Gift Card Balance | [https://www.nordstrom.com/nordstrom-gift-cards](https://www.nordstrom.com/nordstrom-gift-cards) |
| Styling | [https://www.nordstrom.com/browse/services/personal-stylists](https://www.nordstrom.com/browse/services/personal-stylists) |
| Book an Appointment | [https://www.nordstrom.com/appointments](https://www.nordstrom.com/appointments) |
| Request a Look | [https://www.nordstrom.com/curation/request](https://www.nordstrom.com/curation/request) |
| Alterations | [https://www.nordstrom.com/browse/services/alterations](https://www.nordstrom.com/browse/services/alterations) |
| Bra Fitting | [https://www.nordstrom.com/browse/services/bra-fitting-services-and-guide](https://www.nordstrom.com/browse/services/bra-fitting-services-and-guide) |
| Beauty Services & Events | [https://www.nordstrom.com/browse/beauty/services](https://www.nordstrom.com/browse/beauty/services) |
| Shop with Purpose | [https://www.nordstrom.com/browse/impact/product](https://www.nordstrom.com/browse/impact/product) |
| AAPI Owned or Founded | [https://www.nordstrom.com/browse/diversity-at-nordstrom/asian-owned-founded](https://www.nordstrom.com/browse/diversity-at-nordstrom/asian-owned-founded) |
| Black Owned or Founded | [https://www.nordstrom.com/browse/support-black-owned-businesses](https://www.nordstrom.com/browse/support-black-owned-businesses) |
| Latinx & Hispanic Owned or Founded | [https://www.nordstrom.com/browse/diversity-at-nordstrom/latinx-owned-founded](https://www.nordstrom.com/browse/diversity-at-nordstrom/latinx-owned-founded) |
| Women-Owned & Founded | [https://www.nordstrom.com/browse/diversity-at-nordstrom/women-owned](https://www.nordstrom.com/browse/diversity-at-nordstrom/women-owned) |
| Nordstrom for Good | [https://www.nordstrom.com/browse/nordstrom-for-good/all](https://www.nordstrom.com/browse/nordstrom-for-good/all) |
| The Nordy Club | [https://www.nordstrom.com/browse/nordy-club](https://www.nordstrom.com/browse/nordy-club) |
| Build Your Wish List | [https://www.nordstrom.com/my-account/wishlist](https://www.nordstrom.com/my-account/wishlist) |
| Customer Service | [https://www.nordstrom.com/browse/customer-service](https://www.nordstrom.com/browse/customer-service) |
| Pickup & Delivery Options | [https://www.nordstrom.com/browse/services/shipping-methods-charges](https://www.nordstrom.com/browse/services/shipping-methods-charges) |
| Order Status | [https://www.nordstrom.com/my-account/order-lookup](https://www.nordstrom.com/my-account/order-lookup) |
| Return Policy & Exchanges | [https://www.nordstrom.com/browse/services/return-policy](https://www.nordstrom.com/browse/services/return-policy) |
| Learn More | [https://www.nordstrom.com/browse/impact/people/our-communities/shoes-that-fit](https://www.nordstrom.com/browse/impact/people/our-communities/shoes-that-fit) |

## Footer links

| Control | Destination |
|---|---|
| Privacy Policy | [https://www.nordstrom.com/browse/customer-service/policy/privacy](https://www.nordstrom.com/browse/customer-service/policy/privacy) |
| Customer Service | [https://www.nordstrom.com/browse/customer-service](https://www.nordstrom.com/browse/customer-service) |
| Contact Us | [https://www.nordstrom.com/browse/customer-service](https://www.nordstrom.com/browse/customer-service) |
| Order Status | [https://www.nordstrom.com/my-account/order-lookup](https://www.nordstrom.com/my-account/order-lookup) |
| Shipping | [https://www.nordstrom.com/browse/services/shipping-methods-charges](https://www.nordstrom.com/browse/services/shipping-methods-charges) |
| Return Policy & Exchanges | [https://www.nordstrom.com/browse/services/return-policy](https://www.nordstrom.com/browse/services/return-policy) |
| Price Adjustments | [https://www.nordstrom.com/my-account/price-adjustment](https://www.nordstrom.com/my-account/price-adjustment) |
| Gift Cards | [https://shop.giftcard.nordstrom.com/](https://shop.giftcard.nordstrom.com/) |
| FAQ | [https://www.nordstrom.com/browse/customer-service/frequently-asked-questions](https://www.nordstrom.com/browse/customer-service/frequently-asked-questions) |
| Product Recalls | [https://www.nordstrom.com/browse/customer-service/product-recalls](https://www.nordstrom.com/browse/customer-service/product-recalls) |
| About Us | [https://www.nordstrom.com/browse/about](https://www.nordstrom.com/browse/about) |
| All Brands | [https://www.nordstrom.com/brands-list](https://www.nordstrom.com/brands-list) |
| Careers | [https://careers.nordstrom.com/](https://careers.nordstrom.com/) |
| Our Impact | [https://www.nordstrom.com/browse/impact](https://www.nordstrom.com/browse/impact) |
| People & Culture | [https://careers.nordstrom.com/life-at-nordstrom](https://careers.nordstrom.com/life-at-nordstrom) |
| Get Email Updates | [https://www.nordstrom.com/my-account/marketing-email-opt-in](https://www.nordstrom.com/my-account/marketing-email-opt-in) |
| Nordy Podcast | [https://www.nordstrom.com/browse/about/nordy-podcast](https://www.nordstrom.com/browse/about/nordy-podcast) |
| Stores & Services | [https://www.nordstrom.com/browse/services](https://www.nordstrom.com/browse/services) |
| Find a Store | [https://www.nordstrom.com/stores](https://www.nordstrom.com/stores) |
| Free Style Help | [https://www.nordstrom.com/browse/services/personal-stylists/appointments](https://www.nordstrom.com/browse/services/personal-stylists/appointments) |
| Alterations & Tailoring | [https://www.nordstrom.com/browse/services/alterations](https://www.nordstrom.com/browse/services/alterations) |
| Nordstrom Spa Services | [https://www.nordstrom.com/browse/beauty/services/spa](https://www.nordstrom.com/browse/beauty/services/spa) |
| Nordstrom Restaurants | [https://www.nordstrom.com/browse/about/nordstrom-restaurants](https://www.nordstrom.com/browse/about/nordstrom-restaurants) |
| Nordstrom Local | [https://www.nordstrom.com/browse/services/nordstrom-local](https://www.nordstrom.com/browse/services/nordstrom-local) |
| The Nordy Club Rewards | [https://www.nordstrom.com/browse/nordy-club](https://www.nordstrom.com/browse/nordy-club) |
| Apply for a Nordstrom Card | [https://www.nordstrom.com/creditcard/entry?cc=AA1001](https://www.nordstrom.com/creditcard/entry?cc=AA1001) |
| Pay My Bill | [https://www.nordstromcard.com/en/pay-bill/make-a-transfer/form](https://www.nordstromcard.com/en/pay-bill/make-a-transfer/form) |
| Manage My Nordstrom Card | [https://www.nordstromcard.com/](https://www.nordstromcard.com/) |
| Nordstrom Rack | [https://www.nordstromrack.com/?sid=100054](https://www.nordstromrack.com/?sid=100054) |
| Investor Relations | [https://press.nordstrom.com/investor-relations](https://press.nordstrom.com/investor-relations) |
| Press Releases | [http://press.nordstrom.com/phoenix.zhtml?c=211996&p=irol-overview](http://press.nordstrom.com/phoenix.zhtml?c=211996&p=irol-overview) |
| Nordstrom Media Network | [https://www.nordstrom.com/browse/about/nordstrom-media-network](https://www.nordstrom.com/browse/about/nordstrom-media-network) |
| Nordstrom Affiliate | [https://www.nordstrom.com/browse/affiliate-program](https://www.nordstrom.com/browse/affiliate-program) |
| Download Our App | [https://www.nordstrom.com/browse/about/nordstrom-apps](https://www.nordstrom.com/browse/about/nordstrom-apps) |
| Instagram | [https://www.instagram.com/nordstrom/](https://www.instagram.com/nordstrom/) |
| Pinterest | [https://www.pinterest.com/nordstrom/](https://www.pinterest.com/nordstrom/) |
| X | [http://twitter.com/nordstrom](http://twitter.com/nordstrom) |
| Facebook | [https://www.facebook.com/Nordstrom](https://www.facebook.com/Nordstrom) |
| Connect with Us | [https://www.nordstrom.com/browse/about/socialmedia](https://www.nordstrom.com/browse/about/socialmedia) |
| Privacy | [https://www.nordstrom.com/browse/customer-service/policy/privacy](https://www.nordstrom.com/browse/customer-service/policy/privacy) |
| Your Privacy Options | [https://www.nordstrom.com/browse/policy/adjust-settings](https://www.nordstrom.com/browse/policy/adjust-settings) |
| Terms & Conditions | [https://www.nordstrom.com/browse/customer-service/policy/terms-conditions](https://www.nordstrom.com/browse/customer-service/policy/terms-conditions) |
| California Supply Chains Act | [https://www.nordstrom.com/browse/impact/resources/reporting/ctsc-disclosure](https://www.nordstrom.com/browse/impact/resources/reporting/ctsc-disclosure) |

## Where the walk stopped

Sign In, Shop with AI, the bag, search submit, the Singapore picker, Get Email Updates, Order Status, Price Adjustments, Apply for a Nordstrom Card, Pay My Bill, and Manage My Nordstrom Card were not opened. Add to Bag was not clicked. The bot wall at `siteclosed.nordstrom.com` was discarded because it printed a phone number.
