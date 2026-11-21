# Urban Outfitters site tree

Mapped 2026-11-22 from the public US storefront at https://www.urbanoutfitters.com/ in the T3 preview browser, incognito, desktop CSS viewport 1440×900 (devicePixelRatio 2) and phone CSS viewport 390×844 (devicePixelRatio 2). The shop is public. No dark-theme control was on the pages that were opened. No email, phone, code, password, or address was typed. No form was submitted. No identity provider was clicked. Checkout was not entered. A captcha on `/login` was not solved.

## Shell (desktop)

The header is 207px: a 45px promo strip, a utility row, the wordmark, search, then a 60px primary nav.

| Control | Opens |
|---|---|
| Skip to main content | in-page anchor `#u-skip-anchor` |
| Promo previous / next / pause | same-page carousel |
| Promo "Shop Now" and "See Details" | a shop page or https://www.urbanoutfitters.com/current-promotions |
| Sign Up For SMS | same-page anchor `#sms-sign-up`. Not submitted. |
| Gift Cards | page https://www.urbanoutfitters.com/gift-cards |
| UO Rewards | page https://urbanoutfitters.com/uo-rewards |
| Stores | page https://www.urbanoutfitters.com/stores |
| Sign In / Sign Up | dialog on the same page. Login wall. Branch stopped. |
| Logo | page https://www.urbanoutfitters.com/?ref=logo |
| Search field and search button | search overlay on the same page (trending queries and popular products). Not submitted. |
| Heart | page https://www.urbanoutfitters.com/account/hearted-products, which redirects to `/login`. That URL returned a captcha wall. Not solved. |
| Bag | page https://www.urbanoutfitters.com/cart |
| Shop with UO (chat bubble) | chat. Not opened. |

Primary nav. Each label is a link plus a menu-toggle button. Hovering Women's opened a mega-menu on the same page (1320×460 under the nav). The link itself opens the category page.

| Nav link | Page | Mega-menu (same page) |
|---|---|---|
| New | /new-arrivals | toggle present, not opened |
| Gifts | /gifts | toggle present, not opened |
| Women's | /womens-clothing | Shop by Category, Shop by Occasion, Trending, plus a promo tile |
| Men's | /mens-clothing | toggle present, not opened |
| Jeans | /jeans | toggle present, not opened |
| Shoes | /all-shoes | toggle present, not opened |
| Accessories | /all-accessories | toggle present, not opened |
| Home | /home | toggle present, not opened |
| Music | /vinyl-records-cassettes | toggle present, not opened |
| Beauty + Wellness | /beauty-products | toggle present, not opened |
| Brands | /shop-brands | toggle present, not opened |
| Extra 40% Off Sale | /sale | toggle present, not opened. The link text is red `#d83604`. |

Women's mega-menu links that were read: Shop All Women's, New, Best Sellers, Tops + Tees, Going Out Tops, Sweaters + Cardigans, Jeans, Graphic Tees, Dresses, Jackets + Fleece, Bottoms, Pants, Skirts + Skorts, Sweatpants, Intimates + Lounge, Matching Sets, Activewear, Accessories, Shoes, Vintage, Extra 40% Off Sale, Holiday Party Outfits, On Campus, Gameday, Concert + Festival, Going Out Shop, Everyday Essentials, At The Office, Top Rated, Tops under $30, Gifts for Her, Touch of Velvet, Basic Tops, Lace + Satin, Jewel Tones.

## Phone (390)

The utility row and the primary nav collapse. Search, heart, bag, and a button labelled Open navigation stay in the header. Open navigation opens an in-page drawer (`nav[aria-label=primary]`, about 332px wide), not a new URL. The drawer lists the same category links, each with a chevron. Close returns to the same page. Under the promo, the homepage shows a 2-column grid of category tiles (New, Gifts, Women's, Men's, Jeans, Shoes, Accessories, Home, Beauty + Wellness, Music, Brands, Sale).

## Home https://www.urbanoutfitters.com/

| Control | Opens |
|---|---|
| Promo banner | /new-arrivals or the slide's shop URL |
| Category tiles under the banner | the matching category page |
| Editorial tiles (sweaters, going-out tops, accessories, jackets) | curation or category pages |
| Product tray tiles | product page `/shop/<slug>` |
| Extra 40% Off Sale / Shop all | /sale |

## Category https://www.urbanoutfitters.com/womens-clothing

Public. Heading "Women's Clothing", product count beside it. Same-page controls: Shop by Category, Size, Color, Brand, Price, Free Pickup, Availability, All Filters, view density (3 / 4 / 6), sort (Featured and the other sort labels), pagination. A product tile opens `/shop/<slug>`. Filters were not submitted.

## Product https://www.urbanoutfitters.com/shop/bdg-kelly-so-soft-rolled-neck-cardigan

Public. Breadcrumb Women's / Tops + Tees / Sweaters + Cardigans. Same-page controls: colour swatches, size chips (XXS through XL), Size Guide, Get It Before It's Gone (add to bag), Add to Wish List, Free In-Store Pickup (asks for a size first), Details and other accordions. Add to bag was not clicked. Wish list was not opened. Pickup was not used.

## Bag, search, account

| Control or page | What it did |
|---|---|
| Search overlay | same page. Empty query. Trending chips and popular products. Not submitted. |
| /cart | empty bag. "Sign in to view bag items from your account" and "Proceed to Checkout". Checkout was not entered. |
| Sign In / Sign Up | dialog "Sign In" (475×620) with Mobile Number and Email tabs, empty phone field, country select, Keep Me Signed In, Next. Create an Account switches the same dialog to an empty signup form (email, mobile, style preference, Next). Neither form was typed or submitted. |
| /login | captcha wall ("We detected unusual activity"). Not solved. Hearted products was not reached. |

## Footer

Help, Quick Links, and Extras are disclosure buttons on the same page. Links read from the footer: Order Status and Start A Return (`#order-inquiry`), Returns + Exchanges, Shipping, Orders + Payments, FAQ, Contact Us, help topics, Student Discount (external), Brands, Gift Cards, Careers (urbn.com, new window), Shop Europe, Shop Canada, Newsroom, Affirm, Afterpay, Klarna, UO MRKT, UO Community, Creative Services, Join Me@UO, Store Locator, email and SMS anchors, Chat With Us, app stores, social sites, Privacy Policy, Terms of Use, CA Transparency, Accessibility, URBN.com, Support Code, Your Privacy Choices. None of those forms were submitted.
