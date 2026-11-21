# Mercari public site tree

Mapped signed out on 2026-11-22 from [https://www.mercari.com](https://www.mercari.com). The first paint was the live US shop, title "Your Go-to Marketplace for Deals on Used & Secondhand Items". Desktop viewport measured 1440 by 900 CSS pixels, `devicePixelRatio` 2. The page is a live marketplace, not a parked domain and not a captcha wall.

A privacy bar offered Review details and Got it. Got it was clicked. That dismissed the bar. Nothing was typed into it.

Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider was clicked. No captcha was solved. Search was not submitted. Sign up, Log in, Sell, List an item, Notifications, and Cart were not clicked. `login-extracted` was not flipped. `catalog.json` and `webapps-manifest.json` were left alone. origin/main had no `systems/mercari/`.

Tracking query strings on app-download links are not recorded. The homepage notification badge read 3. That count is not stable chrome.

## Header

`header`, 77px, padding 0 40px. On the homepage it paints `#252b60` with a white wordmark and white labels. On Electronics, About, Brands, and the login wall it paints `#ffffff`, the wordmark is `#5356ee`, and Sign up and Log in are `#222222`. Sell on the homepage is a white 64 by 32 button, radius 4px, label `#222222`, 14px weight 600. On interior pages the same control reads List an item and paints `#5356ee` with a white label.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Mercari Logo | link | `/` | photographed on the homepage |
| Search for anything | search field plus Search button | search | not submitted |
| Download app | button | app download | not opened |
| Sign up | button | `/signup/` | not opened. Signup wall. Stop. |
| Log in | button | `/login/` | opened only to see the wall. Nothing typed. Stop. |
| Notifications | button | account | not opened. Login wall. Stop. |
| Cart | button | cart | not opened. Checkout-adjacent. Stop. |
| Sell | button | `/sell/` | not clicked. A direct open of `/sell/` redirected to the login wall. Stop. |

The category row sits under the header, 92px. Labels are 14px Averta, `#5356ee`. Visible at 1440 on the homepage:

| Control | Destination | This pass |
|---|---|---|
| Women | `/us/category/women-1/` | not opened |
| Men | `/us/category/men-2/` | not opened |
| Electronics | `/us/category/electronics-7/` | photographed |
| Toys | `/us/category/toys-1611/` | not opened |
| Gaming | `/us/category/gaming-84/` | not opened |
| Handbags | `/us/category/handbags-21/` | not opened |
| Home | `/us/category/home-4/` | not opened |
| Vintage | `/us/category/vintage-5/` | not opened |
| Beauty | `/us/category/beauty-6/` | not opened |
| Kids | `/us/category/kids-3/` | not opened |
| Sports | `/us/category/sports-8/` | not opened |
| Handmade | `/us/category/handmade-9/` | not opened |
| Office | `/us/category/office-2882/` | not opened |
| Pet | `/us/category/pet-143/` | not opened |
| Outdoor | `/us/category/outdoor-2633/` | not opened |
| Tools | `/us/category/tools-3170/` | not opened |
| Books | `/us/category/books-141/` | not opened |
| View all | `/us/browse-categories/` | not opened |

Interior pages replace that icon row with a text row: Brands, Discover Trends (`/us/trending/`), then the same categories, then View all. Brands was photographed as its own page.

The homepage promo is a link to `https://lp.us.mercari.com/free-shipping-50`. It was not opened.

## Footer

The link block paints `#252b60` with white text. Column labels are 16px, weight 600: SHOP, SELL, SUPPORT, COMPANY & POLICIES. Links are 14px, weight 400. A gray legal bar (`#f5f5f6`, 69px) sits under it. That bar prints a mailing address, so it is mapped here and left out of the photographs.

| Control | Destination | This pass |
|---|---|---|
| Trending | search with brand filters | not opened |
| Brands | `/us/brand/` | photographed |
| Categories | `/us/category/` | not opened |
| Deals | `/us/featured/mercari_us_deals/` | not opened |
| How it works | help center, making a purchase | not opened |
| Gift card exchange | `/us/try-gift-card-exchange/` | not opened |
| Coupons and Promotions | `https://lp.us.mercari.com/coupons-and-promotions` | external landing page. Not opened. |
| Create an account | `/signup/` | not opened. Signup wall. Stop. |
| Shop on | `https://japan.us.mercari.com/en` | other shop. Not opened. |
| How to sell | `/us/how-to-sell/` | not opened. Sell flow. Stop. |
| Packaging | help center article | not opened |
| Shipping | `/shipping/` | not opened |
| Getting paid | help center, payouts | not opened. Payouts. Stop. |
| Authenticate | `/us/authenticate/` | not opened |
| Contact Us | help center contact | not opened. Can ask for an email. Stop. |
| Help Center | `/us/help_center/` | not opened |
| Service Status | `https://status.mercari.com/` | external. Not opened. |
| Marketplace Guidelines | help center article | not opened |
| Safety Guidelines | help center, trust | not opened |
| Buyer Protection | help center article | not opened |
| Seller Protection | help center, seller protection | not opened |
| Refunds and Returns | help center, returns | not opened |
| About Us | `/about/` | photographed |
| Careers | `/careers/` | not opened |
| Policy Center | help center, trust | not opened |
| Privacy Policy | `/privacy/` | not opened |
| Terms of Service | `/tos/` | not opened |
| Licenses / Disclosures | `/licenses_disclosures/` | not opened |
| Cookie Preferences | cookie dialog | not reopened after Got it |
| Facebook, X, Instagram, TikTok, YouTube, Pinterest, Threads, Snapchat | social profiles | not opened |
| App store badges | app download | not opened |
| Venmo, enjoy now pay later | payment pages | not opened. Checkout-adjacent. Stop. |

## Pages photographed

| Page | URL |
|---|---|
| Homepage | `https://www.mercari.com/` |
| Electronics | `https://www.mercari.com/us/category/electronics-7/` |
| About | `https://www.mercari.com/about/` |
| All brands | `https://www.mercari.com/us/brand/` |

The Electronics photograph is cropped above "Top Electronics sellers". That row prints seller usernames. The homepage photograph is the first screen and does not include the legal bar.

## Where the walk stopped

Login and signup (Log in, Sign up, Create an account, Notifications), sell (Sell, List an item, `/sell/`, How to sell, Getting paid), cart and checkout, search submit, the newsletter was not present, Contact Us, payment pages, and the legal bar because it prints a mailing address. `/login/` shows an email field, Continue, Continue with Google, Continue with Facebook, and Continue with Apple, plus a reCAPTCHA notice. Nothing was typed. No identity provider was clicked. `/sell/` redirected to `/login/?login_callback=%2Fsell%2F` and was left. The privacy bar was dismissed with Got it. Nothing was submitted.
