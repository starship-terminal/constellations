# Best Buy public site tree

Mapped signed out on 2026-11-22 from [https://www.bestbuy.com/](https://www.bestbuy.com/) in an incognito preview at 1440 by 900 CSS pixels, `devicePixelRatio` 2. The first response is a country picker, title "Best Buy International: Select your Country - Best Buy". United States was opened. That link is `https://www.bestbuy.com/?intl=nosplash`. Title: Best Buy | Official Online Store | Shop Now & Save. The page is a live store, not a parked domain and not a captcha wall.

Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider was clicked. No captcha was solved. No item was added to cart. Checkout was not opened. `login-extracted` stays `not-started`.

`catalog.json` and `webapps-manifest.json` were left alone. origin/main had no `systems/bestbuy/`.

Tracking query strings are not recorded. The public entry is the path without that query. Sign-in and create-account redirects append a `token` query. Those tokens are not recorded. Screenshots of those walls show the empty form, not the address bar.

## Country picker

| Control | Destination | This pass |
|---|---|---|
| Canada | [https://www.bestbuy.ca/en-ca](https://www.bestbuy.ca/en-ca) | not opened |
| United States | [https://www.bestbuy.com/?intl=nosplash](https://www.bestbuy.com/?intl=nosplash) | opened. This is the captured surface |
| See More Details | international-orders help topic | not opened |
| English, Français, Español | language buttons on the picker | not changed |

## Header

Photographed: [home-light-1440.png](screenshots/home-light-1440.png).

Two blue bars, both `rgb(0, 70, 190)`. The top bar is 73px. The utility bar is 60px.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Skip to content | link | `#headerskip` | not followed |
| Go to Product Search | link | `#autocomplete-search-bar` | not followed |
| Go to Footer | link | `#footer` | not followed |
| Assistive Survey | button | survey | not opened |
| Best Buy wordmark | link | [https://www.bestbuy.com](https://www.bestbuy.com) | home |
| Search Best Buy | text field | search | empty, not submitted |
| Submit search | button | search results | not clicked |
| Your store / Find a store | button | store locator | not opened. A later product page named a store, and that name was hidden before the product shot |
| Account / Sign in | button | account menu | opened, then Sign In was followed to the empty login wall |
| Cart, 0 items | link | `/cart` | checkout wall, not opened |
| Ask Blue | button | assistant | not opened |
| Shop | button | category menu | opened. Categories listed below. Submenus were not followed |
| Deals | button | deals menu | click did not replace the open Shop list in this session |
| Support & Services | button | support menu | same headless miss |
| Discover | button | discover menu | same headless miss |
| Gift Ideas | link | `/site/electronics/gift-ideas/abcat0010000.c?id=abcat0010000` | not opened |
| Black Friday Deals | link | `/black-friday` | not opened |
| Deal of the Day | link | `/site/misc/deal-of-the-day/pcmcat248000050016.c?id=pcmcat248000050016` | not opened |
| My Best Buy Memberships | link | `/site/electronics/best-buy-membership/pcmcat1679668833285.c?id=pcmcat1679668833285` | not opened |
| More | button | overflow links | opened |

More overflow, already in the header DOM when closed:

| Control | Destination |
|---|---|
| Credit Cards | `/site/misc/financing-rewards/pcmcat102500050032.c?id=pcmcat102500050032` |
| Gift Cards | `/site/electronics/gift-cards/cat09000.c?id=cat09000` |
| Trade-In | `/site/best-buy-trade-in/trade-in-offers/pcmcat1774297472214.c?id=pcmcat1774297472214` |
| Best Buy Business | `/site/electronics/bestbuy-business/pcmcat230900050001.c?id=pcmcat230900050001` |
| Best Buy Gamers | `/gamers` |

Shop menu, opened from the header. These are buttons, not followed:

Shop by Brand, TV & Home Theater, Computers & Tablets, Appliances, Video Games, Cell Phones, Cameras, Camcorders & Drones, Headphones, Home Audio & Speakers, Home, Furniture & Office, Wearable Technology, Smart Home, Security & Wi-Fi, Trading Cards, Collectibles & Toys, Health, Wellness & Personal Care, Sports, Fitness & E-Transportation.

### Account menu

Opened from Account. Guest copy: "Get more with a Best Buy account". Sign In and Create Account sit above account links. The links point at signed-in routes and were not opened.

| Control | Destination | This pass |
|---|---|---|
| Sign In | identity sign-in wall | empty wall photographed, then stopped |
| Create Account | identity create-account wall | empty wall photographed, then stopped |
| Learn more | shipping exclusions | not opened |
| Account | `/customer/myaccount` | not opened |
| Purchases | `/purchasehistory/purchases` | not opened |
| Payments | `/profile/c/billinginfo/cc` | not opened |
| My Best Buy Credit Card | `/services/ccdashboard` | not opened |
| Plans and Subscriptions | `/services/planlist` | not opened |
| Saved Items | `/site/customer/lists/manage/saveditems` | not opened |
| Account Settings | `/identity/accountSettings` | not opened |
| Support | `/support` | not opened |

## Homepage body

One public product was opened from a homepage doorbuster, SKU 6505727, "Sony - WH-1000XM5 Wireless Noise Cancelling Over-the-Ear Headphones - Black". Photographed: [product-light-1440.png](screenshots/product-light-1440.png). Add to cart was visible and was not clicked. Pickup and shipping rows that named a store and a same-day time were hidden before the shot. The sign-in prompt that opened on that page was closed without typing.

Category chips under "Shop deals by category" were not opened. The first ones:

| Control | Destination |
|---|---|
| Shop Top 100 Deals | `/site/sale-page/top-100-deals-this-season/pcmcat1765308864276.c?id=pcmcat1765308864276` |
| Apple | `/site/all-electronics-on-sale/all-apple-on-sale/pcmcat1688758488330.c?id=pcmcat1688758488330` |
| Exclusive Member Deals | `/site/best-buy-membership/member-deals/pcmcat1679678876400.c?id=pcmcat1679678876400` |
| TV & Home Theater | `/site/all-electronics-on-sale/all-tv-home-theater-on-sale/pcmcat1690836748285.c?id=pcmcat1690836748285` |
| Computers & Tablets | `/site/all-electronics-on-sale/all-computers-tablets-on-sale/pcmcat1632941704767.c?id=pcmcat1632941704767` |
| All Video Games | `/site/all-electronics-on-sale/all-video-games-on-sale/pcmcat1690896520374.c?id=pcmcat1690896520374` |
| Appliances | `/site/all-electronics-on-sale/all-appliances-on-sale/pcmcat1637009144989.c?id=pcmcat1637009144989` |
| Headphones | `/site/all-electronics-on-sale/headphones-on-sale/pcmcat1720706915460.c?id=pcmcat1720706915460` |

Hero "Shop now" goes to `/black-friday`. Not opened.

A homepage band says "Sign in" and "Create an account". Those were not used. The photographed walls came from the header account menu and from `https://www.bestbuy.com/identity/global/createAccount`.

## Footer

Read from the homepage DOM. Not photographed as its own shot. Social links leave the site and were not opened. The email field and Sign Up button are a subscribe wall. Nothing was typed and Sign Up was not clicked.

| Column | Control | Opens |
|---|---|---|
| Support | Visit our Support Center | [https://www.bestbuy.com/support](https://www.bestbuy.com/support) |
| Support | Check your Order Status | [https://www.bestbuy.com/profile/ss/orderlookup](https://www.bestbuy.com/profile/ss/orderlookup) |
| Support | Shipping, Delivery & Store Pickup | `/site/help-topics/shipping-delivery-store-pickup/pcmcat316000050003.c?id=pcmcat316000050003` |
| Support | Returns & Exchanges | `/site/help-topics/return-exchange-policy/pcmcat260800050014.c?id=pcmcat260800050014` |
| Support | Price Match Guarantee | `/site/help-topics/price-match-guarantee/pcmcat290300050002.c?id=pcmcat290300050002` |
| Order & Purchases | Product Recalls | `/site/help-topics/product-recalls/pcmcat114800050015.c?id=pcmcat114800050015` |
| Order & Purchases | Trade-In Program | [https://www.bestbuy.com/trade-in](https://www.bestbuy.com/trade-in) |
| Order & Purchases | Gift Cards | `/site/electronics/gift-cards/cat09000.c?id=cat09000` |
| Payment Options | My Best Buy Credit Card | `/site/misc/financing-rewards/pcmcat102500050032.c?id=pcmcat102500050032` |
| Payment Options | Pay Your Bill at Citibank | identity SSO sign-in. Not opened |
| Payment Options | Lease to Own | `/site/financing-rewards/progressive-leasing/pcmcat1535574988808.c?id=pcmcat1535574988808` |
| Payment Options | Buy Now, Pay Later | `/site/financing-rewards/zip/pcmcat1727878406362.c?id=pcmcat1727878406362` |
| Payment Options | Best Buy Business Financing | `/site/bestbuy-business/best-buy-business-financing/pcmcat1556029048796.c?id=pcmcat1556029048796` |
| Support & Services | Schedule a Service | [https://www.bestbuy.com/services/triage/home](https://www.bestbuy.com/services/triage/home) |
| Support & Services | Manage an Appointment | [https://www.bestbuy.com/dossier/service/appointmentfinder](https://www.bestbuy.com/dossier/service/appointmentfinder) |
| Support & Services | Protection & Support Plans | `/site/electronics/services/pcmcat1528819595254.c?id=pcmcat1528819595254` |
| Support & Services | Haul Away & Recycling | `/site/services/recycling/pcmcat149900050025.c?id=pcmcat149900050025` |
| Support & Services | Contact Us | [https://www.bestbuy.com/contact-us](https://www.bestbuy.com/contact-us) |
| Rewards & Membership | My Best Buy Memberships | membership page, same as the header link |
| Rewards & Membership | View Points & Certificates | `/profile/c/rwz/overview` |
| Rewards & Membership | Member Offers | [https://www.bestbuy.com/loyalty/catalog](https://www.bestbuy.com/loyalty/catalog) |
| Partnerships | Sell on Best Buy Marketplace | `/site/electronics/marketplace/pcmcat248200050007.c?id=pcmcat248200050007` |
| Partnerships | Advertise with Us | [https://www.bestbuyads.com/](https://www.bestbuyads.com/) |
| Partnerships | Affiliates: Creators & Publishers | `/site/misc/best-buy-affiliate-program/pcmcat198500050002.c?id=pcmcat198500050002` |
| Partnerships | Best Buy Health | [https://healthcare.bestbuy.com/](https://healthcare.bestbuy.com/) |
| Partnerships | Best Buy Education | `/site/bestbuy-business/bestbuy-education/pcmcat356600050000.c?id=pcmcat356600050000` |
| Partnerships | Best Buy Business | same as the header link |
| Partnerships | Partner+ | `/site/clp-bbfb/partner-plus/pcmcat1715699845027.c?id=pcmcat1715699845027` |
| About | Corporate Information | [https://corporate.bestbuy.com/](https://corporate.bestbuy.com/) |
| About | Careers | [https://jobs.bestbuy.com/bby](https://jobs.bestbuy.com/bby) |
| About | Corporate Responsibility | [https://corporate.bestbuy.com/our-goals/](https://corporate.bestbuy.com/our-goals/) |
| About | Sustainability | [https://corporate.bestbuy.com/sustainability/](https://corporate.bestbuy.com/sustainability/) |
| Account | Sign in or Create Account | [https://www.bestbuy.com/identity/global/signin](https://www.bestbuy.com/identity/global/signin) |
| Apps | Learn more | `/site/misc/mobile-app/pcmcat208500050016.c?id=pcmcat208500050016` |
| Social | YouTube | [https://www.youtube.com/user/bestbuy](https://www.youtube.com/user/bestbuy) |
| Social | Instagram | [https://instagram.com/bestbuy](https://instagram.com/bestbuy) |
| Social | TikTok | [https://www.tiktok.com/@bestbuy](https://www.tiktok.com/@bestbuy) |
| Social | Facebook | [https://www.facebook.com/bestbuy](https://www.facebook.com/bestbuy) |
| Social | Pinterest | [https://www.pinterest.com/bestbuy/](https://www.pinterest.com/bestbuy/) |
| Social | X | [https://www.x.com/BestBuy](https://www.x.com/BestBuy) |
| Region | Best Buy Canada | [https://www.bestbuy.ca/](https://www.bestbuy.ca/) |
| Legal | Accessibility | `/site/help-topics/accessibility/pcmcat1496336482680.c?id=pcmcat1496336482680` |
| Legal | Terms & Conditions | `/site/help-topics/terms-and-conditions/pcmcat204400050067.c?id=pcmcat204400050067` |
| Legal | Privacy | `/site/help-topics/privacy-policy/pcmcat204400050062.c?id=pcmcat204400050062` |
| Legal | Interest-Based Ads | `/site/privacy-policy/interest-based-ads/pcmcat204400050066.c?id=pcmcat204400050066` |
| Legal | State Privacy Rights | `/site/privacy-policy/state-privacy-rights/pcmcat204400050063.c?id=pcmcat204400050063` |
| Legal | Health Data Privacy | `/site/privacy-policy/health-data-privacy/pcmcat1709131468002.c?id=pcmcat1709131468002` |
| Legal | Do Not Sell/Share My Personal Information | `/sentry/landing?type=ca_donotsell` |
| Legal | Limit Use of My Sensitive Personal Information | `/sentry/landing?type=optout` |
| Legal | Targeted Advertising Opt Out | `/sentry/landing?type=donottarget` |
| Legal | CA Supply Chain Transparency Act | `/site/help-topics/ca-transparency-act/pcmcat263000050003.c?id=pcmcat263000050003` |
| Subscribe | Email field and Sign Up | subscribe wall. Not submitted |
| Feedback | Give feedback about our website | not opened |
| Feedback | Accessibility Survey | not opened |

## Pages photographed

| Page | URL | Width |
|---|---|---|
| Home | https://www.bestbuy.com/?intl=nosplash | 1440 |
| Public product | https://www.bestbuy.com/product/sony-wh-1000xm5-wireless-noise-cancelling-over-the-ear-headphones-black/J7XSRH5CXG/sku/6505727 | 1440 |
| Login wall | https://www.bestbuy.com/identity/global/signin | 1440 |
| Signup wall | https://www.bestbuy.com/identity/global/createAccount | 1440 |

Desktop viewport measured 1440 by 900, `devicePixelRatio` 2. PNG size is 2880 by 1800. Phone width was not captured.

## Stopped

Stopped at the empty login wall and the empty signup wall. Passkey, Apple, and Google were visible and were not clicked. The footer email Sign Up was not submitted. Cart, checkout, store locator, and Ask Blue were not opened.
