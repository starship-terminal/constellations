# Depop public site tree

Mapped signed out on 2026-11-22 from [https://www.depop.com](https://www.depop.com). The first paint was the live shop, title "Depop - buy, sell, discover unique fashion". Desktop viewport measured 1440 by 900 CSS pixels, `devicePixelRatio` 2. No `data-theme` attribute. `color-scheme` was `normal`. The page is a live marketplace, not a parked domain and not a captcha wall.

Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider was clicked. No captcha was solved. Search was not submitted. Sell now, Sign up, and Log in were not opened. Likes and Bag were not opened. `login-extracted` was not flipped. `catalog.json` and `webapps-manifest.json` were left alone. origin/main had no `systems/depop/`.

Prices on the shop were shown in USD. Country links in the footer were read and not opened.

## Header

Top bar, 65px, background white. The wordmark is an inline SVG, 90 by 23, path fill `#E20020`. Search is a 605 by 40 field, background `#f3f3f3`, 2px `#262626` border, radius 30px, placeholder "Search for items, brands, or styles…". A rotating suggestion sits in the field. It was not typed.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Logo | link | `/` | photographed |
| Search | combobox | not submitted | not typed. Stop. |
| Search with a photo | button | camera search | not clicked |
| Likes | link | `/likes/` | not opened. Signed-in likes. Stop. |
| Bag | link | `/bag/` | not opened. Bag. Stop. |
| Sell now | link | `/signup/?redirect=/products/create/` | not opened. Signup and sell wall. Stop. |
| Sign up | link | `https://www.depop.com/signup/` | not opened. Stop. |
| Log in | link | `/login/?redirect=/` | not opened. Stop. |

Category bar, 56px, label "Main categories". Labels are 16px Aktiv Grotesk, color `#262626`. Sale paints `#e20020`. Each item is a menuitem button that opens a mega menu. The menu links were read from the DOM. They were not opened, except Women's, which is also a public category URL.

| Control | Destination read from the menu | This pass |
|---|---|---|
| Women | `/category/womens/` and subcategories under `/category/womens/` | category photographed |
| Men | `/category/mens/` | not opened |
| Kids | `/category/kids/` | not opened |
| Brands | `/brands/` and `/brands/a-z/` | not opened |
| Gifts | `/explore/holiday-gifts/` | not opened |
| Sports | `/explore/see-all-sportswear-us/` | not opened |
| Trending | `/explore/fall-trends-2026/` | not opened |
| Sale | `/category/womens/?isDiscounted=true` | not opened |

A floating "Get the Depop app" button sat over the homepage. Its dismiss control was clicked so the photograph shows the shop. The app store was not opened.

## Footer

`footer#footer` on the homepage. Column headings are buttons: Depop, Sell, Help, Site Information. Links are 16px, color `#262626`.

| Control | Destination | This pass |
|---|---|---|
| About us | `https://news.depop.com/who-we-are/about/` | photographed |
| Careers | `https://depopcareers.com/` | not opened |
| Blog | `/blog/` | not opened |
| News | `https://news.depop.com/` | not opened |
| Impact | `https://news.depop.com/impact/` | not opened |
| Sell on Depop | `/sell/` | not opened. Sell wall. Stop. |
| Shipping on Depop | `/shipping/` | not opened |
| Depop Affiliates | `/partners/depop-affiliates/` | not opened. Partner signup. Stop. |
| Become a Depop Insider | `/partners/depop-insider/` | not opened. Signup. Stop. |
| Depop Top Seller Program | `/sellers/top-seller-program/` | not opened. Seller program. Stop. |
| Help Center | `/help/` | not opened. Help can print a phone. |
| Safety Center | `/safety/` | not opened |
| Depop Status | `https://depopstatus.com/` | not opened |
| App, Play | `https://depop.app.link/get-the-app` | not opened |
| X, Instagram, TikTok | external profiles | not opened |
| Sitemaps | `/site-map/categories/` | not opened |
| Terms and Conditions | `/help/terms-of-service/` | not opened |
| Privacy | `/help/privacy-policy/` | not opened |
| Cookies | button | not clicked |
| Country links | Australia, Canada, France, Germany, Ireland, Italy, New Zealand, United Kingdom, United States | not opened |

Newsroom header, read on the About page: Who we are, Impact, Company news, Press enquiries, Media kit. Our leadership was not opened, because it shows named portraits. Press enquiries was not opened, because it can print a contact address.

## Pages photographed

| Page | URL | File |
|---|---|---|
| Homepage | `https://www.depop.com/` | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Women's category | `https://www.depop.com/category/womens/` | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| About | `https://news.depop.com/who-we-are/about/` | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |

The category file is cropped above the listing grid. Product URLs on that page carry a seller username, so individual listings were not photographed.

## Where the walk stopped

Login, signup, sell, bag, likes, checkout, and partner signup were not opened. Search was not submitted. No identity provider was clicked. No form was submitted. Leadership was not opened.
