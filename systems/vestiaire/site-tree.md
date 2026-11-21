# Vestiaire Collective public site tree

Mapped signed out on 2026-11-22 from [https://www.vestiairecollective.com](https://www.vestiairecollective.com). The first paint redirected to [https://us.vestiairecollective.com/](https://us.vestiairecollective.com/). Title "Vestiaire Collective: Buy & sell designer second-hand fashion." Desktop viewport measured 1440 by 900 CSS pixels, `devicePixelRatio` 2. The page is a live store, not a parked domain and not a captcha wall.

A shopping-preference dialog opened on its own, titled "Select shopping preference", with Womenswear, Menswear, and Continue. Continue was not clicked. The dialog was hidden for the photographs so the page underneath could be read. A cookie bar offered Accept, Continue without accepting, and Close. Continue without accepting was clicked. It did not submit an email, a password, or an address.

Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider was clicked. No captcha was solved. Sign in, Sign up, Sell an item, the bag, Add to Bag, and Make an Offer were not clicked. Search was not submitted. `login-extracted` was not flipped. `catalog.json` and `webapps-manifest.json` were left alone. origin/main had no `systems/vestiaire/`.

Prices on the photographed pages were shown in SGD. The footer locale read Singapore (S$ SGD), English US. Location was not changed.

## Header

`header`, 132px, white, ink `rgb(30, 30, 30)`. The top row is 69px. The nav row is 62px. A hairline under the header sampled `#ececec`. Nav labels are 15px HelveticaNowText, weight 400, padding 20px 0px. Sale is the same size in `rgb(219, 33, 36)`.

The wordmark is an image, alt "Second hand store - Vestiaire Collective", 243 by 26, from `https://assets.vestiairecollective.com/a/fenx/v4.169.0/assets/img/home/vestiairecollective_logo.svg`. It links to `/`.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Search by brand, item... | button, 420 by 45, radius 33px, fill `#f5f5f5` | search | not opened. Not submitted. |
| Wordmark | link | `/` | photographed |
| Sell an item | button, 111 by 36, black fill, radius 2px | sell wall | not clicked. Stop. |
| Sign in | button | login wall | not clicked. Stop. |
| Sign up | button | signup wall | not clicked. Stop. |
| Bag | link, "You have no items in your bag. View bag." | `https://www.vestiairecollective.com/shop/checkout` | not opened. Checkout wall. Stop. |

Nav, left to right:

| Label | Destination | This pass |
|---|---|---|
| Just In | `/new-items/` | not opened |
| Designers | `/brands/` | not opened |
| Women | `/women/` | photographed |
| Men | `/men/` | not opened |
| We Love | `/we-love/` | not opened |
| Vintage | `/vintage/` | not opened |
| Bags | mega menu, no href of its own | menu read from the DOM |
| Watches and Jewelry | mega menu, no href of its own | menu read from the DOM |
| Children | `/kids/` | not opened |
| Express Delivery | `/g/express-delivery/` | not opened |
| Asia's Best | `/new-items/#country=HK-SG-AU-JP-KR` | not opened |
| Sale | `/c/flash-price-drops-10474/` | not opened |
| Inside Vestiaire | `/journal/our-concept-page/` | not opened |

The Women menu is a white panel under the nav, 1440 wide. It was opened and left. Column headings are 16px. Links are 15px, line height 26px, padding 4px 0px.

Homepage: Womenswear (`/womenswear`).

Bags (`/women-bags/`): New In, Handbags (`/women-bags/handbags/`), Shoulder Bags, Totes, Crossbody Bags, Clutch Bags, Belt Bags, Backpacks, Travel Bags, Satchels, All Bags.

Watches and Jewelry (`/women-jewellery/`): New In Watches (`/women-accessories/watches/`), New In Jewelry, Rings, Bracelets, Necklaces, Earrings, All Watches, All Jewelry.

Clothing (`/women-clothing/`): New In, Coats, Trench Coats, Jackets, Leather Jackets, Dresses, Knitwear, Tops, Skirts, Shorts, Pants, Jeans, Jumpsuits, Lingerie, Swimwear, All Clothing.

Shoes (`/women-shoes/`): New In, Heels, Ankle Boots, Boots, Sandals, Espadrilles, Mules and Clogs, Sneakers, Flat Shoes, Ballet Flats, Lace ups, All shoes.

Accessories (`/women-accessories/`): New In, Scarves, Silk handkerchief, Gloves, Hats, Wallets, Belts, Sunglasses, Purses, wallets and cases, All accessories.

Men, We Love, Vintage, Bags, Watches and Jewelry, Children, and Inside Vestiaire also hold menus in the header DOM. Those menus were not opened.

## Homepage

The homepage paints a red promo, then a photographic hero, then image rails.

| Block | Destination | This pass |
|---|---|---|
| Up to S$375 Off First 3 Orders | `/journal/save-extra-on-your-first-orders/` | not opened |
| Early Black Friday, Shop markdowns | `/c/sale-season-12238/` | not opened |
| Fresh Finds: Bags, Jewelry, Shoes, Accessories, Clothing | category listings | not opened |
| Now Trending, View all | `/we-love/` | not opened |

Product cards on the homepage name a brand, a title, a price, and a country. They do not print a seller username. A product page does. That page was opened, measured, and not photographed, because the first screen prints "Listed by" and a seller name.

## Footer

The footer is a black block. Column labels are 12px HelveticaNowText, weight 500, letter-spacing 1.8px, white, uppercase. Links are 14px, `rgb(171, 171, 171)`.

Our Services: Our concept (`/journal/our-concept-page/`), Concierge Service (`/journal/introducing-our-consignment-service/`).

Buy: Order tracking (`/my-account.shtml#commandes`, account wall, not opened), Our authentication service (`/journal/trust-expert-authentication`), Returns policy (`https://faq.vestiairecollective.com/hc/en-us/articles/360004969178`).

Sell: How to sell (`/journal/start-selling/`), Our selling advice (`/journal/tips-for-sellers-us/`), Sell an item (`/sell-clothes-online.shtml`, sell wall, not opened), Professional Seller Service (`/professional-sellers/`).

Help: Help Center (`https://faq.vestiairecollective.com/hc/en-us`), Contact us (`https://faq.vestiairecollective.com/hc/en-us/articles/360002463657-Contact-Us`). Contact us was not opened. It can print a phone number or an address.

Vestiaire Collective: About us (`https://www.vestiairecollective.com/journal/welcome-to-vestiaire-collective/`, photographed), Sustainability (`/journal/our-sustainability-manifesto/`), Impact Report (a PDF, not opened), Join the team (`https://careers.vestiairecollective.com/`, not opened), Fashion stories (`/journal/cat/fashion-stories/`).

Legal row: Accessibility Statement (`/accessibility-statement`), Legal Information, Terms, Privacy Policy and Cookies. Those last three sit on the FAQ host and were not opened.

Social, not opened: YouTube, Facebook, Instagram, Medium.

Country links, not opened: France, United Kingdom, United States, Germany, Spain, Italy.

## Pages photographed

| Page | URL |
|---|---|
| Homepage | `https://us.vestiairecollective.com/` |
| Women | `https://us.vestiairecollective.com/women/` |
| About us | `https://us.vestiairecollective.com/journal/welcome-to-vestiaire-collective/` |

## Where the walk stopped

Sign in, Sign up, Sell an item, the bag (checkout), Add to Bag, Make an Offer, search submit, the shopping-preference Continue, Order tracking, and Contact us. The cookie bar was dismissed with Continue without accepting. The preference dialog was hidden for the photographs and was not submitted. A product page was opened to measure Add to Bag and was not photographed, because it prints a seller username. Nothing was submitted.
