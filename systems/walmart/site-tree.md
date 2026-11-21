# Walmart public site tree

Mapped on 2026-11-21 from the live public site, signed out. Official domain confirmed as `https://www.walmart.com/` (spark mark, title "Walmart | Save Money. Live better."). `https://walmart.com` redirects there. Nothing was typed into a secret field. No identity provider was clicked. No form was submitted. No captcha was solved. Checkout was not entered. `catalog.json` was not edited. `login-extracted` stays not-started.

The storefront paints one light theme. `color-scheme` is `normal`. A dark preference on the 2026-11-19 capture left the header blue.

## Auth walls

The empty login and signup fields were not photographed. The wall is a captcha, not a form.

| Control | Opens | Action |
|---|---|---|
| Header "Sign In Account", account menu "Sign in or create account" | `https://identity.walmart.com/account/login` | In-page click landed on `https://identity.walmart.com/blocked` with the title "Robot or human?". Not solved. No email, password, or code was typed. Identity providers were not clicked. |
| Direct open of `/account/login` and `https://identity.walmart.com/account/login` | Homepage, or `/blocked` | Headless Chromium bounced to the homepage. The preview tab hit the same captcha. Not solved. |
| `/account/signup` and `https://identity.walmart.com/account/signup` | `/blocked` | Not solved. |
| Account menu "Purchase History" | `/orders` | Not followed. Signed-in path. |
| Account menu "Subscriptions" | `/cp/subscriptions/4191733` | Listed, not opened. |
| Phone menu "Account", "My Items" | Signed-in paths | Not followed. |
| Footer "Delete Account" | `/account/login` | Not followed. |
| Sparky "Sign in" | Same identity wall | The dialog opened itself on the product page and was closed. Sign in was not clicked. |

## Homepage header (`https://www.walmart.com/`)

Desktop, left to right: spark logo to `/`, "Pickup or delivery?" (fulfillment dialog: Shipping, Pickup, Delivery, and an add-address control), search (placeholder "Search everything at Walmart online and in store"), Search, EN, Reorder My Items, Sign In Account, cart `$0.00`.

| Control | Opens |
|---|---|
| Pickup or delivery? | A fulfillment dialog. It was closed. No address was typed. Shots that showed a store street were discarded. |
| Search | The field. A later submit of a product query reached `/search` and the next frame was `/blocked`. That results page was not kept. |
| EN | Language. Not changed. |
| Reorder My Items | A signed-in path. Not followed. |
| Sign In Account | Account menu, then the identity wall. |
| Cart `$0.00` | Cart. Checkout was not entered. |
| Departments | A left flyout. See below. |
| Services | A flyout. See below. |

Secondary chips under the bar, each a link: Rollbacks & More (`/shop/savings`), Pharmacy (`/cp/pharmacy/5431`), Thanksgiving (`/cp/holiday-food/7998220`), Holiday Shop (`/cp/christmas-shop/1386088`), Get it Fast (`/cp/get-it-fast/6545138`), Gifting (`/cp/3131907`), Toys (`/cp/toys/4171`), New Arrivals (`/cp/new-arrivals/2593086`), Meals Made Easy (`/cp/dinner-tonight/5681029`), Only at Walmart (`/cp/only-at-walmart/2119250`), Credit Card (`/cp/9435689`), Walmart+ (`/plus`).

### Departments

All Departments (`/all-departments`), Rollbacks & More, Holiday Shop, Grocery, Clothing Shoes & Accessories, Baby, Pharmacy Health & Wellness, Home Garden & Tools, Electronics, Gaming & Movies, Auto & Tires, Personal Care, Beauty, Toys & Outdoor Play, Household Essentials, Pets, School Office & Art Supplies, Sports & Outdoors, Collectibles Books & Music, Party Supplies, Resold.

Grocery opens a submenu: All Grocery (`/cp/food/976759`), Holiday Desserts, Meals Made Easy, Weekly Essentials, Recipe Inspiration (`/i/recipe-library`), Meat & Seafood, Fresh Produce, Frozen, Bakery, Snacks, Dairy, Beverages, Breakfast, Baking, Global Cuisine, Alcohol.

A headless screenshot of this flyout was a blank white panel and was discarded. The list above is from the preview snapshot.

### Services

All Services (`/services`), Auto Care Center, Pharmacy, Vision & Optical, Insurance & Benefits, Registry Lists & Gifts, Custom Cakes, Photo Services, Financial Services, Protection Home & Tech, Subscriptions, Walmart Business, Shopping simplified.

The headless flyout shot was blank and was discarded. A direct load of `/services` was `/blocked`.

### Account menu

Sign in or create account, Purchase History, Walmart+, Subscriptions, Language. Photographed closed over the homepage. Only the identity link was followed, and it stopped at the captcha.

## Footer

Read from the homepage DOM. A scrolled screenshot did not show the link row, so there is no footer image.

All Departments, Store Directory, Careers (`https://careers.walmart.com/`), Our Company (`https://corporate.walmart.com/`), Sell on Walmart.com (`https://marketplace.walmart.com/`), Help, Product Recalls, Accessibility, Tax Exempt Program, Get the Walmart App, Safety Data Sheet, Terms of Use, Privacy Notice, California Supply Chain Act, Your Privacy Choices, Notice at Collection, AdChoices, Consumer Health Data Privacy Notices, Learn about Spark Driver, Brand Shop Directory, Walmart Business, #IYWYK, Delete Account. Copyright line: © 2026 Walmart. A feedback prompt sits above the links. It was not submitted.

## Pages opened

| Page | What it is |
|---|---|
| `https://www.walmart.com/` | Storefront home. Blue bar, hero cards, department icon row. |
| `https://www.walmart.com/cp/toys/4171` | Toys category. Reached by an in-page click. Title "Toys for Kids - Walmart.com". Hero, Rollback badges, Add pills, split prices. A later direct load was `/blocked`. |
| `https://www.walmart.com/ip/Huffy-12-Rock-It-Kids-Bike-Fits-Riders-37-42-EZ-Build-Cobalt-Blue/19875902620` | A public product page, reached from the toys grid. Buy box kept. Add to cart was not clicked. |
| `https://www.walmart.com/plus` | Walmart+ marketing, phone width. Title "Walmart+ Membership | Start Your 30-Day Trial". Join Walmart+ was not clicked. A headless direct load of `/plus` was `/blocked`. |
| `https://corporate.walmart.com/` and the privacy notice | Kept from the 2026-11-19 capture. Not re-shot on this pass. |

## Phone

390 by 844. Homepage: menu, spark, "Search Walmart", cart `$0.00`, a second row "Pickup or delivery?", one hero card, a department icon row.

The menu button opens a drawer: Sign in or create account, Language, Country language and currency, Walmart+, Purchase History, My Items, Account, Subscriptions, Help, Departments, Services, Give Feedback. The drawer was photographed. No row was followed.

The phone inner page is `/plus`. A phone click of the Toys chip landed on `/blocked` and was not solved.

## Stopped

Direct loads of search, help, services, all-departments, a missing route, signup, and a later toys click returned "Robot or human?" at `/blocked`. Those shots were discarded. Search results, the 404, and help were not captured. Checkout was not entered.
