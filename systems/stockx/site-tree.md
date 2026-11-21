# StockX public site tree

Mapped signed out on 2026-11-22 from [https://stockx.com](https://stockx.com). The first paint was the live shop, title "StockX: Sneakers, Streetwear, Trading Cards, Handbags, Watches". Desktop viewport measured 1440 by 900 CSS pixels, `devicePixelRatio` 2. `data-theme` was `dark`. The page is a live marketplace, not a parked domain and not a captcha wall.

Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider was clicked. No captcha was solved. Buy Now, Sell Now, Ask, Bid, Follow, and Size were not clicked. Search was not submitted. The AI Search switch was not toggled. The theme button was not clicked. `login-extracted` was not flipped. `catalog.json` and `webapps-manifest.json` were left alone. origin/main had no `systems/stockx/`.

Prices on the photographed pages were shown in USD. The locale button read Singapore | English | $ USD. It was not clicked.

## Header

Top navigation, 91px, background `#121212`. The logo is an inline SVG, 125px wide, fill `var(--colors-brand-primary)` which resolved to `#95C0A4`. Search is an 829 by 42 field, background `#242424`, 1px `#5F5F5F` border, radius 8px, placeholder "Search for brand, color, etc." An AI Search switch sits inside the field. It was not toggled.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Logo | link | `/` | photographed |
| Search | searchbox | not submitted | not typed. Stop. |
| AI Search | switch | inside the search field | not toggled |
| News | link | `https://stockx.com/news/` | not opened |
| About | link, new tab | `https://stockx.com/about/how-it-works/` | photographed |
| Help | link, new tab | `https://stockx.com/help/home` | not opened. Help and contact can print a phone. |
| Sell | link | `/sell` | not opened. Ask wall. Stop. |
| Sign Up \| Login | button | login and signup | not clicked. Stop. |

Category bar, 48px, label "Product Category Switcher". Labels are 16px Suisse Intl. Deals is `#EF6958`, 18px, weight 500. All is a button. The rest are links.

| Control | Destination | This pass |
|---|---|---|
| All | button, no href | not opened |
| Trending | `/search?sort=most-active` | not opened. Search. Stop. |
| New | `/search?sort=most-active` | not opened. Search. Stop. |
| Deals | `/dp/deals` | not opened |
| Men | `/browse/men` | not opened |
| Women | `/browse/women` | not opened |
| Kids | `/browse/kids` | not opened |
| Sneakers | `/category/sneakers` | photographed |
| Shoes | `/category/shoes` | not opened |
| Apparel | `/category/apparel` | not opened |
| Accessories | `/category/accessories` | not opened |
| Collectibles | `/category/collectibles` | not opened |
| Trading Cards | `/category/trading-cards` | not opened |
| More | `/category/electronics?sort=most-active` | not opened |

A floating button, "Switch to Light Mode", 56px, radius 100px, background `#393939`, sat pressed. It was not clicked. The dark theme is the one that was measured.

## Footer

`footer`, background `#393939`, color `#FAFAFA`, padding 32px 32px 0. The wordmark "StockX." is 32px. Column headings are 14px, weight 700. Links are 12px. The footer was read from the DOM after scrolling. It was not photographed, because the locale control and app-store links sit in the same band.

Brand columns, each a heading plus model links: Air Jordan (`/brands/jordan`), Adidas (`/brands/adidas`), New Balance (`/brands/new-balance`), Nike (`/brands/nike`), ASICS (`/brands/asics?category=sneakers`). Popular Releases links `/releases/upcoming?productType=sneakers` and a few product URLs. Collectibles, Apparel, and Accessories repeat category and brand links. Those columns were read and not opened.

| Control | Destination | This pass |
|---|---|---|
| About, How It Works | `https://stockx.com/about/how-it-works/` | photographed |
| Newsroom | `https://stockx.com/about/newsroom/` | not opened |
| Company | `https://stockx.com/about/company/` | opened, then discarded. Leadership names and portraits. |
| StockX Listings | `https://stockx.com/about/listings/` | not opened |
| StockX Live | `https://stockx.com/about/stockx-live/` | not opened |
| StockX Reviews | `https://stockx.com/about/reviews/` | not opened |
| StockX Media Network | `https://stockx.com/about/media-network/` | not opened |
| Sell, Selling Guide | `https://stockx.com/about/selling` | not opened. Ask wall. Stop. |
| Professional Tools | `https://stockx.com/about/professionalsellers/` | not opened |
| StockX Pro | `https://pro.stockx.com/` | not opened. Seller login. Stop. |
| Sponsored Asks | `https://stockx.com/about/sponsored-asks/` | not opened. Ask wall. Stop. |
| Developers | `https://developer.stockx.com/` | not opened |
| Give $10, Get $10 | `https://stockx.com/refer` | not opened. Referral signup. Stop. |
| Help, Help Center | `https://stockx.com/help/home` | not opened |
| Contact Us | `https://stockx.com/help/home?contactsupport=true` | not opened. Can print a phone. |
| Product Suggestions | `https://stockx.com/product-suggestion` | not opened. Form. Stop. |
| Size Guide | a help article | not opened |
| Careers | `https://careers.stockx.com/` | not opened |
| App Store, Google Play | store listings | not opened |
| Singapore \| English \| $ USD | button | not clicked |
| X, Facebook, Instagram, YouTube | external profiles | not opened |
| Terms | `/terms` | not opened |
| Privacy | `/privacy` | not opened |
| Guidelines | `https://stockx.com/lp/stockx-community-guidelines/` | not opened |
| Your Privacy Choices | button | not clicked |

## Pages photographed

| Page | URL |
|---|---|
| Homepage | `https://stockx.com/` |
| Sneakers | `https://stockx.com/category/sneakers` |
| Jordan 4 Retro Toro Bravo (2026) | `https://stockx.com/air-jordan-4-retro-toro-bravo-2026` |
| How It Works | `https://stockx.com/about/how-it-works/` |

## Where the walk stopped

Login and signup (Sign Up | Login, Login, Sign Up, Give $10 Get $10), sell and ask (Sell, Sell Now, Sponsored Asks, StockX Pro), buy and bid (Buy Now, Size), search submit (the search field, Trending, New), newsletter was not present on the homepage, contact and help, product suggestions, the locale picker, and the privacy-choices button. Company was opened and discarded because it shows leadership portraits. Follow was not clicked. No second regional store was opened.
