# Instacart public site tree

Mapped from https://www.instacart.com/ on 2026-11-21 in the T3 preview, incognito, signed out, before screenshots. The official product is https://www.instacart.com. The homepage stays on `/` and paints the marketing storefront. It does not redirect to `/store` when no account is signed in.

No email, password, phone, code, or address was typed. No form was submitted. No identity provider was clicked. No order was placed. The ZIP `94105` is already in the public storefront chrome when a hub loads. It was not typed or submitted in this walk.

Widths planned for every reachable public state: desktop 1440×900 and phone 390×844. One theme: light. `colorScheme` is `normal`. No dark toggle on the public pages.

The preview pane did not produce screenshot frames ("The browser is not producing screenshot frames"). The tree below is from the live DOM in that tab. Photographs are taken separately with the package's headless capture.

## Header (marketing pages)

Present on `/`, `/grocery-delivery`, `/categories/316-food`, `/business`, `/instacart-plus`, `/promos-and-coupons`, `/p/gift-cards`, `/ebt-snap`.

| Control | Opens |
|---|---|
| Open main menu | the departments drawer on the same page. Close main menu closes it. |
| Wordmark | https://www.instacart.com/ |
| Search (icon on category pages; field on the homepage) | focuses the search field on the same page. Not submitted. |
| Log in | login dialog on the same page, and `/login` is the same card as a route. Stop. |
| Sign up | signup card, and `/signup` is the same card as a route. Stop. |

## Homepage

https://www.instacart.com/

| Control | Opens |
|---|---|
| Sign up to get $0 delivery fee* | the signup card. Stop. |
| *Service and other fees apply… | https://www.instacart.com/help/section/360007996832/10684539136916 (help article; not a login) |
| Previous Retailers / Next Retailers | scrolls the store carousel on the same page. No dialog. |
| A store card (Costco, Sprouts, Safeway, and the rest) | `/store/{slug}/storefront`. Public storefront. Not checkout. |
| Location chip "San Francisco Bay Area" | the Find stores near you dialog. Address field is not typed. Use current location is not clicked. |
| Filter chips (All, EBT, Fastest, Offers, Low prices, Grocery, Alcohol, Pickup, No markups, Convenience, Wholesale, Retail) | filters the store list on the same page. |
| Show all | expands the store list on the same page. |
| Get the full Instacart experience | an `instacart.app.link` app download URL. Other host. Not opened. |
| FAQ questions (How does Instacart delivery…, How much does Instacart cost?, and four more) | expands that answer on the same page. |

## Main menu drawer

Opened by Open main menu. Three section buttons expand in the drawer. The link list is mounted with the drawer.

| Control | Opens |
|---|---|
| Departments | expands department links in the drawer |
| Food, Pantry, Seafood, Baked goods, Dairy, Fresh produce, Deli, Frozen food, Meat, Meat alternatives | `/categories/316-food` or `/categories/316-food/{id}-{slug}` |
| Beverages, Coffee, Juice, Soda, Tea, Water | `/categories/243-beverages` and children |
| Alcohol, Wine, Liquor, Beer | `/categories/2-alcohol` and children |
| Organic grocery | `/shop/organic-food` |
| More ways to shop | expands the second list in the drawer |
| Shop by location | `/grocery-delivery` |
| Shop online deals | `/store/hub/deals_tab` |
| Send gifts | `/store/hub/gifts` |
| Alcohol, Convenience, Ready meals | `/store/hub/alcohol`, `/store/hub/convenience`, `/store/hub/ready_meals` |
| Automotive, Baby supplies, Beauty, Clothing, Electronics, Flowers, Furniture, Health care, Home and garden, Household essentials, Ice, Office supplies, Party supplies, Personal care, Pet supplies, Sports | the matching `/categories/{id}-{slug}` page |
| Help | expands the third list in the drawer |
| Contact, Partner program | `/company/contact-us/` |
| Press | `https://instacart.com/company/newsroom` |
| Blog | `https://instacart.com/company/blog` |
| Help | `/help` |
| Careers | `https://instacart.careers` (other host; not captured) |
| Privacy | `/privacy` |
| Health Data Notice | `/p/health_privacy_policy` |
| Terms | `/terms` |
| Instacart+ | `/instacart-plus` |
| Advertise on Instacart | `https://ads.instacart.com` (other host; not captured) |
| Join the Retailer Network | `/company/retailer-platform/retailer-inquiries` |
| Gift cards | `/gift-cards` (redirects to `/p/gift-cards`) |
| Shoppers | `https://shoppers.instacart.com/` (other host; not captured) |
| Shopper locations | `https://shoppers.instacart.com/instacart-jobs` (other host; not captured) |
| Promos & Coupons | `/promos-and-coupons` |
| Grocery Budget Calculator | `/resources/grocery-budget-calculator` |
| Will Call Delivery | `/business/willcall` |
| United States Change | country dialog: United States, Canada, Close. Not submitted. |

## Grocery delivery

https://www.instacart.com/grocery-delivery

Same header. Store cards open `/store/{slug}/storefront`. Show all expands the list. Log in in the body opens the login card. Stop.

## Food category

https://www.instacart.com/categories/316-food

| Control | Opens |
|---|---|
| Department chips (Alcohol, Beverages, Food, Fresh Produce, and the rest) | that category page |
| Brands, Nutrition | filter controls on the same page. Not submitted. |
| A store search card | `/store/{slug}/s?k=Food`. Public search. Not an order. |

## Online deals

https://www.instacart.com/store/hub/deals_tab

Storefront chrome: Main Menu, search field, address button reading the prefilled ZIP, Log in, cart (0 items). Popular, Alcohol, Floral Party and Gift, and School Supplies are hub tabs. A product tile opens a hub item query on the same deals collection. Cart is empty. Checkout is not started. Add is not used.

## Send gifts

https://www.instacart.com/store/hub/gifts

Same storefront chrome. A public gift hub. Checkout is not started.

## Help

https://www.instacart.com/help

| Control | Opens |
|---|---|
| Help Center wordmark | `/help/` |
| Log in, Sign up | the same auth cards. Stop. |
| Topic buttons (Promo not applying, Authorization holds, Adding a payment method, Add or modify tip, another payments question, Manage Instacart+, Instacart+ benefits) | that help article or a login wall if the article is account-only. Stop if it asks for an account. |
| Article rows (Terms of Promo Credit, Profile and Account Settings, Order in Progress, and the rest) | `/help/section/{id}` |

## Business

https://www.instacart.com/business

| Control | Opens |
|---|---|
| Contact our sales team | `/business/contact` (a sales form; not submitted) |
| Create free business account | an account-creation path. Stop. |

## Instacart+

https://www.instacart.com/instacart-plus

Try free for 14 days starts a trial. Not clicked.

## Promos

https://www.instacart.com/promos-and-coupons

Get started opens signup. Not clicked. View terms and conditions stays on the public promo copy.

## Gift cards

https://www.instacart.com/p/gift-cards

Send gift card and Log in and Redeem are purchase and account paths. Not clicked.

## EBT SNAP

https://www.instacart.com/ebt-snap

Marketing page. Store cards open public storefronts. No EBT card number is typed.

## Privacy and terms

https://www.instacart.com/privacy uses a legal header: Locations (`/grocery-delivery`), Careers (`/careers`), Blog (`http://news.instacart.com`), Help, Store (`/store`), Become a shopper (`shoppers.instacart.com`). In-page section links jump inside the policy.

https://www.instacart.com/terms is the public terms page.

## Login wall

https://www.instacart.com/login and the homepage Log in dialog.

| Control | Opens |
|---|---|
| Email field | local field. Not typed. |
| Continue | would submit the email. Not clicked. |
| Google, Facebook, Phone | identity providers. Not clicked. |
| Sign up | the signup card. Stop. |
| Close / Cancel | dismisses the dialog |

## Signup wall

https://www.instacart.com/signup

| Control | Opens |
|---|---|
| Email field | local field. Not typed. |
| Terms of Service, Privacy Policy | `/terms`, `/privacy` |
| Continue | would submit the email. Not clicked. |
| Google, Facebook, Phone | identity providers. Not clicked. |
| Create a free Instacart Business profile | `/business` |
| Log in | the login card. Stop. |

## Not on this surface

Signed-in navigation, account settings, and create-account beyond the empty signup card were not offered on the public pages. Cart checkout, payment, a street address, and the Plus trial were not opened. Other hosts (careers, ads, shoppers, app stores, company newsroom) were not captured.
