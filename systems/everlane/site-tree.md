# Everlane public site tree

Mapped signed out on 2026-11-22 from [https://www.everlane.com/](https://www.everlane.com/) in an incognito preview at 1440 by 900 CSS pixels, `devicePixelRatio` 2. Title: Everlane. The page is a live Shopify store, not a parked domain and not a captcha wall.

Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider was clicked. No captcha was solved. Nothing was added to bag. Checkout was not opened. `login-extracted` stays `not-started`.

`catalog.json` and `webapps-manifest.json` were left alone. origin/main had no `systems/everlane/`. Refero already has an interpreted `refero/everlane/` style. That is not this package.

Tracking query strings are not recorded. Account links drop `buyer_flags` and the OAuth query. Country rows in the region picker are `#` anchors on the homepage. They are a picker, not pages, and are not listed one by one.

The department nav on the photographed homepage is the women's set. The men's set is in the same header drawer and is listed below. Menus were read from the homepage DOM. Each submenu was not hovered open.

## Announcement bar

Photographed: [home-light-1440.png](screenshots/home-light-1440.png). Height 32px. Three slides. The homepage shot shows the cashmere slide on `#12344b`. The product shot shows the shipping slide on `#c8c0b8`.

| Control | Opens | This pass |
|---|---|---|
| Shop Women | `/collections/womens-black-friday-sale` | not opened |
| Shop Men | `/collections/mens-black-friday-sale` | not opened |
| Shop Now | `/collections/shop-better-priced-cashmere` | not opened |
| Enjoy free shipping on U.S orders over $75 | no link of its own | read on the product page |

## Header

Two rows under the announcement bar. The wordmark row is white, 40px. Women, Men, Sustainability, and Stores sit at the left. Search, Account, and Bag sit at the right. The department row is 33px.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Skip to content | link | `#MainContent` | not followed |
| Women | link | `/pages/womens` | not opened |
| Men | link | `/pages/mens` | not opened |
| Sustainability | link | `/pages/sustainability` | not opened |
| Stores | link | `https://blog.everlane.com/stores` | not opened |
| Everlane | link | `/` | home |
| Search | link | `/search` | not opened, not submitted |
| Account | button | `https://account.everlane.com/authentication/login` | empty wall photographed, then stopped |
| Bag | button | empty bag drawer on the same page | drawer was in the DOM, not opened. Checkout was not started |

## Department row

These links sit in the homepage header for the women's set. The label navigates. The submenu button does not.

| Control | Opens |
|---|---|
| Priced Better | `/collections/shop-better-priced-cashmere` |
| Gift Guide | `/collections/womens-gift-shop` |
| New | `/collections/womens-new-arrivals` |
| Cult Favorites | `/collections/womens-best-sellers` |
| Clothing | `/collections/womens-all` |
| Sweaters | `/collections/womens-sweaters` |
| Denim | `/collections/womens-jeans` |
| Tees | `/collections/womens-tees` |
| Shoes | `/collections/womens-shoes` |
| Accessories | `/collections/womens-all-accessories` |
| Sale | `/collections/womens-sale` |

### Priced Better

| Control | Opens |
|---|---|
| $48 & Up Cashmere | `/collections/shop-better-priced-cashmere` |
| Shop More at Better Prices | `/collections/womens-better-prices-shop` |
| Explore More | `/pages/better-priced-cashmere` |

### Gift Guide

| Control | Opens |
|---|---|
| Explore The Gift Guide | `/pages/the-better-gift-guide` |
| Gifts For Her | `/collections/womens-gift-shop` |
| Sweaters | `/collections/womens-gifts-better-sweaters` |
| Best-Selling Gifts | `/collections/best-selling-gifts` |
| Under $100 | `/collections/womens-gifts-under-100` |
| Luxe Gifts | `/collections/womens-self-gifting` |
| Accessories | `/collections/better-accessories-gifts` |
| Gifts For Him | `/collections/mens-gift-shop` |

### New

| Control | Opens |
|---|---|
| All New Arrivals | `/collections/womens-new-arrivals` |
| Scenes From Fall | `/collections/womens-clothes-shoes-fall-edit-002` |
| Collegium x Everlane | `/collections/collegium-x-everlane-shoes` |
| Somewhere West | `/collections/womens-clothes-shoes-fall-edit-001` |
| Better Prices Shop | `/collections/womens-better-prices-shop` |
| Sweater Edit | `/collections/womens-sweaters` |
| Corduroy Shop | `/collections/womens-all?fq=Fabric%3ACorduroy&page=1` |
| Natural Fiber Shop | `/collections/everlane-shop-natural-fibers` |
| Shop Now | `/collections/womens-black-friday-sale` |

### Cult Favorites

| Control | Opens |
|---|---|
| All Cult Favorites | `/collections/womens-best-sellers` |
| Cult Favorites Lookbook | `/pages/cult-favorites-lookbook` |

### Clothing

| Control | Opens |
|---|---|
| All Clothing | `/collections/womens-all` |
| Tops | `/collections/womens-tops` |
| Tees | `/collections/womens-tees` |
| Sweaters | `/collections/womens-sweaters` |
| Denim | `/collections/womens-jeans` |
| Pants | `/collections/womens-pants-trousers` |
| Outerwear | `/collections/womens-outerwear` |
| Fleece & Loungewear | `/collections/womens-active-lounge` |
| Dresses | `/collections/womens-dresses` |
| Shorts & Skirts | `/collections/womens-skirts-shorts` |
| Intimates | `/collections/womens-intimates` |

### Sweaters

| Control | Opens |
|---|---|
| All Sweaters | `/collections/womens-sweaters` |
| Cashmere | `/collections/womens-sweaters?fq=Fabric%3ACashmere` |
| Alpaca | `/collections/alpaca-sweaters` |
| Wool | `/collections/womens-wool-sweaters` |
| Cotton | `/collections/womens-cotton-sweaters` |
| Cardigan | `/collections/womens-sweaters?fq=Style%3ACardigans` |
| Crew | `/collections/womens-sweaters?fq=Neckline%3ACrew+Neck` |
| V-Neck | `/collections/womens-sweaters?fq=Neckline%3AV-Neck` |
| Turtleneck | `/collections/womens-sweaters?fq=Neckline%3ATurtleneck` |

### Denim

| Control | Opens |
|---|---|
| All Denim | `/collections/womens-jeans` |
| Denim Shorts | `/collections/womens-shorts-denim` |
| Straight Jeans | `/collections/womens-straight-jeans` |
| Wide Leg Jeans | `/collections/womens-wide-leg-jeans` |
| Barrel Jeans | `/collections/womens-barrel-jeans` |
| Baggy & Relaxed Jeans | `/collections/womens-baggy-jeans` |
| High Rise Jeans | `/collections/womens-high-rise-jeans` |
| Mid Rise Jeans | `/collections/womens-mid-rise-jeans` |
| Low Rise Jeans | `/collections/womens-low-rise-jeans` |

### Tees

| Control | Opens |
|---|---|
| All Tees | `/collections/womens-tees` |
| Tee Bundles | `/collections/womens-tee-bundles` |
| Tees & Tanks | `/collections/womens-tees` |
| Sweatshirts | `/collections/womens-active-lounge?fq=Style%3ASweatshirts` |
| Tops | `/collections/womens-tees?page=1&fq=Style%3ATops` |
| Tanks | `/collections/womens-tank-tops` |

### Shoes

| Control | Opens |
|---|---|
| All Shoes | `/collections/womens-shoes` |
| Collegium x Everlane | `/collections/collegium-x-everlane-shoes` |
| Sneakers | `/collections/womens-sneakers` |
| Loafers | `/collections/womens-loafers` |
| Boots | `/collections/womens-boots` |
| Flats | `/collections/womens-flats` |
| Heels | `/collections/womens-heels` |
| Sandals | `/collections/womens-spring-summer-sandals` |
| Made In Italy Collection | `/collections/made-in-italy-footwear-collection` |

### Accessories

| Control | Opens |
|---|---|
| All Accessories | `/collections/womens-all-accessories` |
| All Bags | `/collections/womens-bags` |
| Totes | `/collections/womens-totes` |
| Backpacks | `/collections/womens-backpacks` |
| Weekenders | `/collections/womens-all-accessories?fq=Style%3AWeekenders%2FDuffles` |
| Hats & Scarves | `/collections/womens-hats-beanies-scarves` |

### Sale

| Control | Opens |
|---|---|
| Shop Black Friday | `/collections/womens-black-friday-sale` |
| Under $100 | `/collections/womens-black-friday-sale-under-100` |
| $100-$150 | `/collections/womens-black-friday-sale-100-150` |
| $150-$200 | `/collections/womens-black-friday-sale-150-200` |
| $200-$250 | `/collections/womens-black-friday-sale-200-250` |
| Best Deals | `/collections/black-friday-best-deals` |
| All Sale | `/collections/womens-sale` |
| New to Sale | `/collections/womens-new-sale` |
| Sale Tees | `/collections/womens-sale?page=1&fq=Category%3ATees+%26+Tanks` |
| Sale Tops | `/collections/womens-sale?page=1&fq=Category%3ATops` |
| Sale Sweaters | `/collections/womens-sale?page=1&fq=Category%3ASweaters` |
| Sale Denim | `/collections/womens-sale?fq=Category%3ADenim&page=1` |
| Sale Pants | `/collections/womens-sale?page=1&fq=Category%3ABottoms` |
| Sale Outerwear | `/collections/womens-sale?page=1&fq=Category%3AOuterwear` |
| Sale Dresses | `/collections/womens-sale?page=1&fq=Category%3ADresses` |
| Sale Shoes & Accessories | `/collections/womens-sale?page=1&fq=Category%3ASandals%2CBoots%2CFlats+%26+Heels%2CAccessories%2CFootwear` |

## Men's header set

Read from the same homepage header drawer. Not photographed as the open menu.

| Control | Opens |
|---|---|
| Home | `/pages/mens` |
| Gift Guide | men's gift submenu |
| New | men's new submenu |
| Cult Favorites | men's cult submenu |
| Clothing | men's clothing submenu |
| Sweaters | men's sweaters submenu |
| Tees | men's tees submenu |
| Shirts | men's shirts submenu |
| Pants | `/collections/mens-chinos-khakis` |
| Accessories | men's accessories submenu |
| Sale | men's sale submenu |

The drawer also lists men's bags at `/collections/mens-bags` and `/collections/mens-travel-bags`, and gifts at `/collections/mens-gift-shop`, `/collections/mens-gifts-better-sweaters`, `/collections/best-selling-gifts-for-him`, and `/collections/gifts-under-100`.

## Homepage tiles

These sit in the main column, under the hero. One product tile was opened.

| Control | Opens | This pass |
|---|---|---|
| Shop Women | `/collections/womens-black-friday-sale` | not opened from the hero |
| Shop Men | men's sale collection | not opened |
| The Box-Cut Tee in Essential Cotton | `/products/womens-organic-cotton-box-cut-tee-peyote` | photographed |
| Cashmere Slim Crew Sweater | `/products/womens-cashmere-slim-crew-sweater-canvas` | not opened |
| Cashmere Half-Zip | `/products/f-swtr-eca-hzip-pc-nvy` | not opened |
| Utility Cigarette Pant | `/products/womens-utility-cigarette-pant-black` | not opened |

## Footer

Columns: Account, Company, Get Help, Connect. The email field is the subscribe wall. Subscribe was not clicked.

| Control | Opens | Stop? |
|---|---|---|
| Manage Account | `https://account.everlane.com/profile` | redirects to the login wall |
| Sign up | `https://account.everlane.com/profile` | same wall. No separate signup form |
| Redeem a gift card | `/pages/redeem` | not opened |
| About | `/pages/about` | not opened |
| Environmental Initiatives | `/pages/sustainability` | not opened |
| DEI | `/pages/dei` | not opened |
| Careers | `/pages/careers` | not opened |
| Accessibility | `/` | same homepage, not a separate page in this pass |
| Help Center | `https://support.everlane.com/` | not opened |
| Live Chat | `/#chat-with-us-digital-genius` | not opened |
| Return Policy | `https://support.everlane.com/what-is-your-return-policy-H1fMnra0s` | not opened. Analytics query dropped |
| Shipping Info | `https://support.everlane.com/en_us/what-are-your-shipping-methods-HJkCniTXel` | not opened |
| Bulk Orders | `/pages/bulk` | not opened |
| EU Right of Withdrawal | `https://service.global-e.com/Categories/how-do-i-exercise-my-right-of-withdrawal` | not opened |
| EU Legal Guarantee | `/pages/eu-legal-guarantee` | not opened |
| Instagram | `https://www.instagram.com/everlane/` | not opened |
| TikTok | `https://www.tiktok.com/@everlane` | not opened |
| YouTube | `https://www.youtube.com/everlane` | not opened |
| Pinterest | `https://www.pinterest.com/everlane/` | not opened |
| Affiliates | `/pages/affiliates` | not opened |
| Our Stores | `https://blog.everlane.com/stores` | not opened |
| Privacy Policy | `/policies/privacy-policy` and `/pages/privacy` | not opened |
| Terms | `/pages/terms` | not opened |
| CA Supply Chain Transparency | `/pages/supply-chain` | not opened |
| Vendor Code of Conduct | `/pages/vendor-code` | not opened |
| Email address / Subscribe | newsletter form | subscribe wall, not submitted |
| SG/SGD | region picker | not changed. Country rows are `#` anchors |
| Cookies settings | consent control | not submitted |
| Need Help? Chat with us | chat | not opened |

## Where this pass stopped

Login, signup, checkout, and subscribe. Account and Sign up both land on one empty email wall at `account.everlane.com`. Continue with Shop was visible and was not clicked. The bag drawer was not opened. The footer email was left empty.
