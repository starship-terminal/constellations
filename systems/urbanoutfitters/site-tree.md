# Urban Outfitters site tree

Mapped 2026-11-22 from the public US storefront at [https://www.urbanoutfitters.com/](https://www.urbanoutfitters.com/) in the T3 preview browser, incognito. Desktop CSS viewport measured 1440 by 900, `devicePixelRatio` 2. Title "Urban Outfitters: Men’s & Women’s Clothing, Homeware & Decor".

A OneTrust privacy dialog was closed with Allow All. Nothing was typed. No email, phone, code, password, or address was entered. No form was submitted. No identity provider was clicked. Checkout was not entered. Add to bag was not clicked. Sign In / Sign Up was not opened. A captcha was not solved.

`catalog.json` and `webapps-manifest.json` were left alone. origin/main had no `systems/urbanoutfitters/`. A different product already lives at `systems/urban-outfitters/` and was not touched.

## Header

Photographed: [screenshots/home-light-1440.png](screenshots/home-light-1440.png).

The header is 207px. A 45px promo strip, a utility row, the wordmark, search, then a 60px primary nav.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Skip to main content | link | `#u-skip-anchor` | listed |
| Promo previous / next / pause | button | same-page carousel | listed |
| Promo Shop Now and See Details | link | a shop page, or [current promotions](https://www.urbanoutfitters.com/current-promotions) | listed |
| Sign Up For SMS | link | `#sms-sign-up` | not submitted |
| Gift Cards | link | [https://www.urbanoutfitters.com/gift-cards](https://www.urbanoutfitters.com/gift-cards) | listed |
| UO Rewards | link | [https://urbanoutfitters.com/uo-rewards](https://urbanoutfitters.com/uo-rewards) | listed |
| Stores | link | [https://www.urbanoutfitters.com/stores](https://www.urbanoutfitters.com/stores) | listed. Store locator can print addresses, so it was not opened. |
| Sign In / Sign Up | button | dialog on the same page | not opened. Login wall. Stopped. |
| Logo | link | [https://www.urbanoutfitters.com/?ref=logo](https://www.urbanoutfitters.com/?ref=logo) | home |
| Search | field | search overlay | not submitted |
| Heart | link | `/account/hearted-products` | not opened. Account wall. |
| Bag | link | [https://www.urbanoutfitters.com/cart](https://www.urbanoutfitters.com/cart) | not opened. Checkout was not entered. |
| Shop with UO | chat bubble | chat | not opened |

Primary nav. Each label is a link plus a menu-toggle button. Hovering Women's opened a mega-menu on the same page, 1320 by 460 under the nav. The link itself opens the category page.

| Nav link | Page | Mega-menu |
|---|---|---|
| New | [/new-arrivals](https://www.urbanoutfitters.com/new-arrivals) | toggle present, not opened |
| Gifts | [/gifts](https://www.urbanoutfitters.com/gifts) | toggle present, not opened |
| Women's | [/womens-clothing](https://www.urbanoutfitters.com/womens-clothing) | opened. Shop by Category, Shop by Occasion, Trending, plus a promo tile |
| Men's | [/mens-clothing](https://www.urbanoutfitters.com/mens-clothing) | toggle present, not opened |
| Jeans | [/jeans](https://www.urbanoutfitters.com/jeans) | toggle present, not opened |
| Shoes | [/all-shoes](https://www.urbanoutfitters.com/all-shoes) | toggle present, not opened |
| Accessories | [/all-accessories](https://www.urbanoutfitters.com/all-accessories) | toggle present, not opened |
| Home | [/home](https://www.urbanoutfitters.com/home) | toggle present, not opened |
| Music | [/vinyl-records-cassettes](https://www.urbanoutfitters.com/vinyl-records-cassettes) | toggle present, not opened |
| Beauty + Wellness | [/beauty-products](https://www.urbanoutfitters.com/beauty-products) | toggle present, not opened |
| Brands | [/shop-brands](https://www.urbanoutfitters.com/shop-brands) | toggle present, not opened |
| Extra 40% Off Sale | [/sale](https://www.urbanoutfitters.com/sale) | toggle present, not opened. The link colour is `#d83604`. |

Women's mega-menu links that were read: Shop All Women's, New, Best Sellers, Tops + Tees, Going Out Tops, Sweaters + Cardigans, Jeans, Graphic Tees, Dresses, Jackets + Fleece, Bottoms, Pants, Skirts + Skorts, Sweatpants, Intimates + Lounge, Matching Sets, Activewear, Accessories, Shoes, Vintage, Extra 40% Off Sale, Holiday Party Outfits, On Campus, Gameday, Concert + Festival, Going Out Shop, Everyday Essentials, At The Office, Top Rated, Tops under $30, Gifts for Her, Touch of Velvet, Basic Tops, Lace + Satin, Jewel Tones. Photographed: [screenshots/home-mega-light-1440.png](screenshots/home-mega-light-1440.png).

## Home

[https://www.urbanoutfitters.com/](https://www.urbanoutfitters.com/)

| Control | Opens |
|---|---|
| Promo banner | a shop URL, or the slide's category |
| Category tiles under the banner | the matching category page |
| Editorial tiles | curation or category pages |
| Product tray tiles | `/shop/<slug>` |

## Category

[https://www.urbanoutfitters.com/womens-clothing](https://www.urbanoutfitters.com/womens-clothing)

Public. Heading "Women's Clothing", 4573 products. Same-page controls: Shop by Category, Size, Color, Brand, Price, Free Pickup, Availability, All Filters, view density (3 / 4 / 6), sort (Featured and the other sort labels), pagination. A product tile opens `/shop/<slug>`. Filters were not submitted. Photographed: [screenshots/category-light-1440.png](screenshots/category-light-1440.png).

## Product

[https://www.urbanoutfitters.com/shop/bdg-kelly-so-soft-rolled-neck-cardigan](https://www.urbanoutfitters.com/shop/bdg-kelly-so-soft-rolled-neck-cardigan)

Public. Breadcrumb Women's / Tops + Tees / Sweaters + Cardigans. Same-page controls: colour swatches, size chips (XXS through XL), Size Guide, Get It Before It's Gone, Add to Wish List, Free In-Store Pickup. Get It Before It's Gone was not clicked. Wish list was not opened. Pickup was not used. Photographed: [screenshots/product-light-1440.png](screenshots/product-light-1440.png).

## Community

[https://www.urbanoutfitters.com/uo-community-blog](https://www.urbanoutfitters.com/uo-community-blog)

Public editorial page from the footer. Heading "UO Community". Browse labels: All UO Community, Newsroom, Gifting, UO Haul, Ways to Wear, UO Music, Community Cares, In the Know, Make Your Space, UO Beauty and Wellness. Photographed: [screenshots/about-light-1440.png](screenshots/about-light-1440.png).

## Footer

Help, Quick Links, and Extras are disclosure groups on the same page. Links read from the footer:

| Group | Links |
|---|---|
| Help | Order Status and Start A Return (`#order-inquiry`), Returns + Exchanges, Shipping, Orders + Payments, FAQ, Contact Us, help topics |
| Quick Links | Student Discount (external), Brands, Gift Cards, Careers (urbn.com, new window), Shop Europe, Shop Canada |
| Extras | Newsroom, Affirm, Afterpay, Klarna, UO MRKT, UO Community, Creative Services, Join Me@UO |
| Utility | Store Locator, Sign Up For Email, Sign Up For Texts, Chat With Us, app stores, social sites |
| Legal | Privacy Policy, Terms of Use, CA Transparency, Accessibility, URBN.com, Support Code, Your Privacy Choices |

None of those forms were submitted. Store Locator, Contact Us, and Chat With Us were not opened, because they can print an address, a phone number, or start a conversation.

## Where the walk stopped

Sign In / Sign Up was not opened. Hearted products was not opened. The bag and checkout were not entered. SMS, email, and text signup anchors were not submitted. Search was not submitted. Get It Before It's Gone was not clicked. Shop with UO chat was not opened.
