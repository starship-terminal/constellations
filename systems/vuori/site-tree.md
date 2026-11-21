# Vuori public site tree

Mapped signed out on 2026-11-22 from [https://vuoriclothing.com/](https://vuoriclothing.com/) in an incognito preview at 1440 by 900 CSS pixels, `devicePixelRatio` 2. Title: Athletic Clothing & Activewear Apparel for Performance – Vuori. The page is the live Vuori shop, not a parked domain and not a captcha wall.

A shipping-destination dialog ("Welcome to United States") and a Privacy Settings cookie dialog covered the first paint. Both were closed so the public page could be photographed. Shop now and Change My Shipping Destination were not clicked. Accept All Cookies, Reject All, and Cookies Settings were not clicked. A later "Get 20% Off" chip was closed the same way. Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider was clicked. No captcha was solved. Select Size was not clicked. Bag was not opened. Checkout was not opened. `login-extracted` stays `not-started`.

`catalog.json` and `webapps-manifest.json` were left alone. origin/main had no `systems/vuori/`.

Tracking query strings are not recorded. Menus were opened with the keyboard on the homepage and read from the menu DOM. Each submenu link was not visited.

## Promo bar

Photographed: [home-light-1440.png](screenshots/home-light-1440.png). Height 34px. Background `#f8f8f8`. Text `#727272`, 12px. The marquee text changes between pages.

| Control | Opens | This pass |
|---|---|---|
| Free Standard Shipping With Orders Over $75 | no link of its own | read on the homepage |
| Built for Range \| Shop Women's Jackets & Vests | `/collections/womens-outerwear` | seen on Our Story, not opened from the bar |
| Sign Up | newsletter control | not opened, not submitted |
| Find a Store | `/apps/store-locator` | not opened |
| Gift Cards | `/products/giftcard` | not opened |
| US | country picker | not opened |

## Header

White bar, 80px, under the promo. The wordmark is 112 by 18. The mark is a 26 by 18 gradient. The letters are ink `#333333`. Gifting is the only department in `#811b28`. Search is a pill, 36px, 1px ink border, radius `3996px`. Ask AI is the same pill. Account, Saved, and Bag sit at the right.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Vuori Home | link | `/` | home |
| New | link, has a menu | `/collections/all-new` | menu read, collection not opened |
| Women | link, has a menu | `/collections/womens` | menu read, collection photographed |
| Men | link, has a menu | `/collections/mens` | menu read, collection not opened |
| Accessories | link, has a menu | `/collections/accessories` | menu read, collection not opened |
| Gifting | link, has a menu | `/pages/holiday-gifts` | menu read, page not opened |
| Explore | link, has a menu | `/pages/our-story` | menu read, Our Story photographed |
| Search Vuori | search box | search | not submitted |
| Ask AI | button | search assistant | not opened |
| Account | button | account menu | menu photographed, then the empty login wall |
| My Saved List | button | saved list | not opened |
| Bag, 0 items | button | bag | not opened. Checkout was not started |

The mobile menu is in the DOM at this width and is not the photographed chrome.

## New menu

| Control | Opens |
|---|---|
| New Arrivals | `/collections/all-new` |
| Women | `/collections/womens-new` |
| Men | `/collections/new` |
| Accessories | `/collections/accessories-new` |
| New To Vuori? Start Here. | `/pages/new-customer` |
| Men's New Arrivals | `/collections/new` |
| Women's New Arrivals | `/collections/womens-new` |
| The Vuori Leggings Guide | `/pages/the-vuori-leggings-guide` |

## Women's menu

| Column | Control | Opens |
|---|---|---|
| Featured | New Arrivals | `/collections/womens-new` |
| Featured | Best Sellers | `/collections/womens-best-sellers` |
| Featured | Matching Sets | `/collections/matching-sets` |
| Featured | The Vuori Leggings Guide | `/pages/the-vuori-leggings-guide` |
| Featured | Fleece Favorites | `/collections/womens-fleece-favorites` |
| Featured | The Anywhere Edit | `/collections/womens-travel` |
| Featured | New in Blue | `/collections/featured-in-blue` |
| Featured | Layers For Fall | `/collections/transitional-layers` |
| Featured | New To Vuori? Start Here. | `/pages/new-customer` |
| Featured | Sale | `/collections/womens-sale` |
| Clothing | Clothing | `/collections/womens` |
| Clothing | Dresses & Jumpsuits | `/collections/womens-dresses-jumpsuits` |
| Clothing | Hoodies & Sweatshirts | `/collections/womens-hoodies-and-sweatshirts` |
| Clothing | Jackets & Vests | `/collections/womens-outerwear` |
| Clothing | Joggers & Sweatpants | `/collections/womens-joggers` |
| Clothing | Leggings | `/collections/womens-leggings` |
| Clothing | Long Sleeve Tops | `/collections/womens-long-sleeve-tops` |
| Clothing | Pants & Trousers | `/collections/womens-pants` |
| Clothing | Short Sleeve Tops | `/collections/womens-short-sleeve-tops` |
| Clothing | Shorts & Skirts | `/collections/shorts-and-skirts` |
| Clothing | Sports Bras | `/collections/womens-sports-bras` |
| Clothing | Sweaters | `/collections/womens-sweaters` |
| Clothing | Tank Tops | `/collections/womens-tanks` |
| Accessories | Accessories | `/collections/womens-accessories` |
| Accessories | Bags & Travel | `/collections/womens-bags` |
| Accessories | Hats | `/collections/womens-hats` |
| Accessories | Socks | `/collections/socks` |
| Accessories | Shop All | `/collections/womens-accessories` |
| Collections | Daily Collection | `/collections/daily-collection` |
| Collections | DreamKnit™ Fabric | `/collections/womens-dreamknit-collection` |
| Collections | Restore Fleece Lounge | `/collections/womens-restore-collection` |
| Collections | Villa Collection | `/collections/villa-collection` |
| Collections | Vuori BlissBlend™ Fabric | `/collections/vuori-blissblend` |
| Activity | Golf | `/collections/womens-golf` |
| Activity | Hiking | `/collections/womens-hiking-collection` |
| Activity | Lounge | `/collections/womens-lounge` |
| Activity | Running | `/collections/womens-running` |
| Activity | Ski & Snow | `/collections/womens-snow` |
| Activity | Swim | `/collections/womens-swim-surf` |
| Activity | Tennis | `/collections/womens-tennis` |
| Activity | Training | `/collections/womens-training` |
| Activity | Travel | `/collections/womens-travel` |
| Activity | Yoga & Pilates | `/collections/womens-yoga` |
| Card | The Winter Fleece Drop | `/collections/womens-fleece-favorites` |

## Men's menu

| Column | Control | Opens |
|---|---|---|
| Featured | New Arrivals | `/collections/new` |
| Featured | Best Sellers | `/collections/best-sellers` |
| Featured | Our Favorite Joggers | `/collections/joggers` |
| Featured | New Styles: Sunday Track | `/collections/sunday-collection` |
| Featured | New in Blue | `/collections/featured-in-blue` |
| Featured | The Waffle Collection | `/collections/mens-waffle-collection` |
| Featured | Athletic Shorts Guide | `/pages/mens-athletic-shorts-guide` |
| Featured | New To Vuori? | `/pages/new-customer` |
| Featured | Sale | `/collections/sale` |
| Clothing | Clothing | `/collections/mens` |
| Clothing | Boardshorts & Swim | `/collections/boardshorts` |
| Clothing | Button Downs | `/collections/mens-button-downs` |
| Clothing | Hoodies & Sweatshirts | `/collections/mens-hoodies-and-sweatshirts` |
| Clothing | Jackets & Vests | `/collections/mens-outerwear` |
| Clothing | Joggers & Sweatpants | `/collections/joggers` |
| Clothing | Long Sleeve Shirts | `/collections/long-sleeve-tops` |
| Clothing | Pants | `/collections/pants` |
| Clothing | Polos | `/collections/polos-henleys` |
| Clothing | Short Sleeve Shirts | `/collections/short-sleeve-tees` |
| Clothing | Shorts | `/collections/shorts` |
| Clothing | Sweaters | `/collections/mens-sweaters` |
| Clothing | Tanks | `/collections/tanks` |
| Clothing | Underwear | `/collections/mens-underwear` |
| Accessories | Accessories | `/collections/mens-accessories` |
| Accessories | Bags & Travel | `/collections/mens-bags` |
| Accessories | Hats | `/collections/mens-hats` |
| Accessories | Socks | `/collections/socks` |
| Accessories | Shop All | `/collections/mens-accessories` |
| Collections | DreamKnit™ Fabric | `/collections/mens-dreamknit-collection` |
| Collections | Kore Shorts & Joggers | `/collections/kore-collection` |
| Collections | Seaside Cotton Fleece Lounge | `/collections/seaside-collection` |
| Collections | Strato Tech Tees | `/collections/mens-strato-tech-collection` |
| Collections | Sunday Sweat Sets | `/collections/sunday-collection` |
| Collections | Vuori Meta™ Pants & Shorts | `/collections/mens-meta-collection` |
| Activity | Golf | `/collections/mens-golf` |
| Activity | Hiking | `/collections/mens-hiking-collection` |
| Activity | Lounge | `/collections/mens-lounge` |
| Activity | Running | `/collections/running` |
| Activity | Ski & Snow | `/collections/mens-snow` |
| Activity | Swim | `/collections/swim` |
| Activity | Tennis | `/collections/mens-tennis` |
| Activity | Training | `/collections/training` |
| Activity | Travel | `/collections/travel` |
| Activity | Workwear | `/collections/mens-workwear` |
| Activity | Yoga | `/collections/yoga` |
| Card | The Winter Fleece Drop | `/collections/mens-fleece-favorites` |

## Accessories menu

| Control | Opens |
|---|---|
| Accessories | `/collections/accessories` |
| Bags | `/collections/bags` |
| Hair Accessories | `/collections/hair-accessories` |
| Hats | `/collections/hats` |
| Socks | `/collections/socks` |
| Yoga Mats + Equipment | `/collections/equipment` |
| Shop All | `/collections/accessories` |
| Sale | `/collections/accessories-sale` |
| Bags, Totes & Backpacks | `/collections/bags` |
| Fitness Accessories | `/collections/equipment` |

## Gifting menu

| Column | Control | Opens |
|---|---|---|
| Women | Women's Gift Guide | `/collections/womens-active-gifts` |
| Women | Active Gifts | `/collections/womens-active-gifts` |
| Women | Cozy Gifts | `/collections/womens-cozy-gifts` |
| Women | Travel Gifts | `/collections/womens-travel-ready-gifts` |
| Women | Best-Selling Gifts | `/collections/womens-best-sellers-gifts` |
| Women | Matching Sets | `/collections/womens-matching-set-gifts` |
| Women | Outerwear Gifts | `/collections/womens-outerwear-gifts` |
| Women | Stocking Stuffers | `/collections/womens-stocking-stuffer-gifts` |
| Women | Gifts Under $100 | `/collections/womens-gifts-under-100` |
| Men | Men's Gift Guide | `/collections/mens-active-gifts` |
| Men | Active Gifts | `/collections/mens-active-gifts` |
| Men | Cozy Gifts | `/collections/mens-cozy-gifts` |
| Men | Travel Gifts | `/collections/mens-travel-ready-gifts` |
| Men | Best-Selling Gifts | `/collections/mens-best-seller-gifts` |
| Men | Outerwear Gifts | `/collections/mens-outerwear-gifts` |
| Men | Stocking Stuffers | `/collections/mens-stocking-stuffer-gifts` |
| Men | Gifts Under $100 | `/collections/mens-gifts-under-100` |
| Cards | Gift Cards | `/products/giftcard` |

## Explore menu

| Control | Opens |
|---|---|
| ACTV Studio | `/pages/actv-studio` |
| Design Philosophy | `/pages/design-philosophy` |
| The Vuori Fabric Guide | `/pages/vuori-fabric-guide` |
| Events | `/pages/events` |
| New To Vuori? Start Here. | `/pages/new-customer` |
| Our Story | `/pages/our-story` |
| Store Locator | `/apps/store-locator` |
| V1 Community | `/pages/v1-community-program` |

## Account menu

Opened from the header Account button. The menu itself is public. The destination of Sign In is the empty wall.

| Control | Opens | This pass |
|---|---|---|
| Sign In or Create Account | `/account/login` | empty wall photographed, then stopped |
| My Dashboard | `/account/dashboard` | not opened |
| Order History | `/account/order-history` | not opened |
| My Profile | `/account/profile` | not opened |
| Addresses | `/account/profile` | not opened |
| Birthday | `/account/dashboard?birthday` | not opened |
| Returns | `https://returns.narvar.com/vuoriclothing/returns` | not opened |
| Support | `https://vuori.kustomer.help/` | not opened |

## Homepage body

The hero is a carousel. Slide 2 of 4 was on screen for the photograph: All-New Outerwear. Other slides were in the DOM and were not clicked through.

| Control | Opens | This pass |
|---|---|---|
| Shop Men's | `/collections/mens-outerwear` | not opened from the hero |
| Shop Women's | `/collections/womens-outerwear` | not opened from the hero |
| Shop Men's (snow slide) | `/collections/mens-snow` | not opened |
| Shop Women's (snow slide) | `/collections/womens-snow` | not opened |
| Shop Now | `/collections/mens-meta-collection` | not opened |
| Shop Women's Halo Styles | `/collections/womens-halo-styles` | not opened |
| Women's Taika Snow Bib | `/products/womens-taika-snow-bib-french-roast` | product page photographed |

## Footer

| Column | Control | Opens | This pass |
|---|---|---|---|
| Newsletter | Email | subscribe | not submitted |
| Newsletter | Sign Up | subscribe | not clicked |
| Support | FAQ | `https://help.vuoriclothing.com` | not opened |
| Support | Contact Us | help contact | not opened |
| Support | Order Status | order status form | not opened |
| Support | Returns | `https://returns.narvar.com/vuoriclothing/returns` | not opened |
| Support | Shipping | help shipping category | not opened |
| Support | Digital Gift Card | `/products/giftcard` | not opened |
| Support | Check Gift Card Balance | `/pages/check-gift-card-balance` | not opened |
| Company | Our Story | `/pages/our-story` | photographed from Explore |
| Company | Journal | `/blogs` | not opened |
| Company | Store Locator | `/apps/store-locator` | not opened |
| Company | Impact | `/pages/impact` | not opened |
| Company | Design Philosophy | `/pages/design-philosophy` | not opened |
| Company | Careers | `/pages/careers` | not opened |
| Company | Press Inquiries | `/pages/press-inquiries` | not opened |
| Company | Wholesale Inquiries | `https://vuori.kustomer.help/en_us/how-do-i-become-a-wholesaler-Sy0x0jjLw` | not opened |
| Other | Sign Up For Text Updates | text signup | not opened, not submitted |
| Other | Birthday Rewards Program | `/pages/birthday-program` | not opened |
| Other | Refer A Friend | `/pages/refer-a-friend` | not opened |
| Other | Digital Catalog | `/pages/digital-catalog` | not opened |
| Other | Catalog Request | `/pages/catalog-request` | not opened |
| Social | instagram | `https://www.instagram.com/vuoriclothing/` | not opened |
| Social | facebook | `https://www.facebook.com/vuoriclothing` | not opened |
| Social | pinterest | `http://www.pinterest.com/vuoriclothing` | not opened |
| Social | tiktok | `https://www.tiktok.com/@vuoriclothing` | not opened |
| Social | twitter | `http://www.twitter.com/vuoriclothing` | not opened |
| Social | youtube | `https://www.youtube.com/@Vuoriclothing` | not opened |
| Legal | Notice at Collection | `/pages/privacy-policy#collection` | not opened |
| Legal | Terms of Use | `/pages/terms-of-use` | not opened |
| Legal | Privacy Policy | `/pages/privacy-policy` | not opened |
| Legal | Cookie Policy | `/pages/cookie-policy` | not opened |
| Legal | Privacy Rights Request Form | `/pages/privacy-request-form` | not opened |
| Legal | Accessibility | `/pages/accessibility` | not opened |
| Legal | Cookies Settings | preference center | not opened |
| Legal | Sitemap | `/sitemap.html` | not opened |

## Where the walk stopped

Sign in and create account share [https://vuoriclothing.com/account/login](https://vuoriclothing.com/account/login). The email field was empty. Continue was not clicked. Continue with Shop was not clicked. Continue with Google was not clicked. The page names reCAPTCHA and it was not solved. Newsletter Sign Up, text updates, bag, and checkout were not opened.
