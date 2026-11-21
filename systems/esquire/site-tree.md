# Esquire public site tree

Walked signed out on 2026-11-21 from [https://www.esquire.com/](https://www.esquire.com/). HTTP 200. Title "Esquire - Men's Fashion, Cocktails, Politics, Interviews, and Women". Desktop viewport 1440 by 900. Phone viewport 390 by 844. The page paints light (`color-scheme: normal`, `html` class `no-mobile no-tablet no-touch loaded`). No page-level theme switch.

Opened means the control was used and the result was read. Linked means the href was read and the destination was not followed in this walk. Sign-in, subscribe, newsletter, and identity-provider walls stop the branch. Nothing was typed. No form was submitted.

## Utility strip, desktop

A 32px strip sits above the wordmark. URL stays `/` unless noted.

| Control | Opens |
|---|---|
| US | A `[role="menu"]` labelled "Select location". Items: US `/`, UK `/uk/`, España `/es/`, Italia `/it/`, Japan `/jp/`. Edition pages. Not followed in this walk. |
| Newsletter | `https://www.esquire.com/newsletter-menu/`. Newsletter wall. Not submitted. |
| Search | A local field in a `form[role="search"]`. Input `name="global-nav-search-input"`, placeholder "Search...". Submit button `aria-label="Search"`. Typed nothing. Not submitted. The results page itself is `/search/`. |
| Wordmark | `/`. |
| Sign In | `/auth/csrf?action=login&return_url=https%3A%2F%2Fwww.esquire.com%2F`. Login wall. Not submitted. |
| Subscribe | `https://www.esquire.com/offers/premium-membership/` with a plan-option query and `cds_tracking_code=esqtopnav`. Plan page. Join and checkout were not followed. |

## Mega menu, desktop

The strip under the wordmark is `.megaMenu`. Each labelled item is a link. Each chevron is a button that opens `#global-nav-mega-menu-panel` and keeps the URL on `/`. Close is the same button, relabelled "Close … submenu".

| Control | Link | Panel items |
|---|---|---|
| Entertainment | `/entertainment/` | TV `/entertainment/tv/`, Movies `/entertainment/movies/`, Books `/entertainment/books/`, Music `/entertainment/music/`, Mavericks of Hollywood `/mavericks-of-hollywood-2025/`, Best of 2025 `/best-2025/`, Cover Stories `/cover-stories/`, View All Entertainment `/entertainment/` |
| What to Buy | `/best-products-to-buy/` | Style `/style/`, Grooming `/style/grooming/`, Tech `/lifestyle/tech/`, The Endorsement `/endorsement/`, Gifts `/gifts/`, Home `/home-decor/`, Awards `/esquire-awards/`, Sales `/sales-and-deals/`, Black Friday & Cyber Monday `/black-friday/`, View All What to Buy `/best-products-to-buy/` |
| Style | `/style/` | Fashion `/style/mens-fashion/`, Shoes `/mens-shoes/`, Sales `/sales-and-deals/`, Grooming `/style/grooming/`, Colognes `/colognes/`, Accessories `/style/mens-accessories/`, Dialed in `/dialed-in/`, Watches `/watches/`, Big Black Book `/style/big-black-book/`, Five Fits `/five-fits-with/`, The Endorsement `/endorsement/`, View All Style `/style/` |
| Lifestyle | `/lifestyle/` | Tech `/lifestyle/tech/`, Fitness and Health `/lifestyle/health/`, The Secret Lives of Men `/the-secret-lives-of-men/`, Travel `/travel/`, Fatherhood `/fatherhood-features/`, Cars `/lifestyle/cars/`, View All Lifestyle `/lifestyle/` |
| News and Politics | `/news-politics/` | Charlie P. Pierce Politics Blog `/news-politics/politics/`, What It Feels Like `/what-it-feels-like/`, What I've Learned `/what-ive-learned-legends/`, View All News and Politics `/news-politics/` |
| Video | `/videos/` | No chevron. |
| Food and Drinks | `/food-drink/food/` | Restaurants `/food-drink/restaurants/`, Bars `/food-drink/bars/`, Cocktail Recipes `/cocktail-recipes/`, View All Food and Drinks `/food-drink/food/` |
| More | button only | Sports `/sports/`, Member Exclusives (same offers URL as Subscribe, `cds_tracking_code=esqpanelnav`), For You `/for-you/` |

Story cards inside a panel are article links. They were not followed in this walk.

## Header, phone (390)

The bar is Newsletter, Subscribe, a hamburger that the capture kit opens as the drawer, the wordmark, and Search. Photographed in [mobile-home-light-default.png](screenshots/mobile-home-light-default.png) and [mobile-home-light-drawer.png](screenshots/mobile-home-light-drawer.png). The drawer keeps the URL on `/`.

The open drawer is a full-screen list, not a side overlay. Close is the circled X at the top left. Search is an inline field (placeholder "Search..."). Not typed. Not submitted.

| Control | Opens |
|---|---|
| Entertainment | Chevron. Same group as the desktop Entertainment panel. Not expanded in the photograph. |
| What to Buy | Chevron. Same group as desktop. |
| Style | Chevron. |
| Lifestyle | Chevron. |
| News and Politics | Chevron. |
| Video | `/videos/`. No chevron. |
| Food and Drinks | Chevron. |
| Sports | Chevron. |
| Member Exclusives | Chevron. Offers path. Not followed. |
| For You | `/for-you/`. No chevron. |
| My Bookmarks | `/my-stuff/`. Account wall. Not submitted. |
| X, TikTok, YouTube, Facebook, Instagram, Pinterest | Outbound social profiles along the bottom. Not followed. |

A second panel, `#sidepanel` (`aria-label="Sidebar Menu"`), stays `display: none` on the photographed drawer. Its DOM lists Subscribe (`shop.esquire.com`), My Bookmarks, section links, Archive (`classic.esquire.com`), Newsletter, About Us, Follow, Other Editions, Privacy Notice, and Terms Of Use. That panel was not the surface the hamburger opened.

## Homepage body

URL stays `/`. Pagination is in the feed: page 1 `/`, page 2 `/?page=2`, page 3 `/?page=3`, next `/?page=2`. Story cards link to articles. They were not followed in this walk. A newsletter field lower on the page has placeholder "Enter your email address". Not typed. Not submitted.

## Footer

| Control | Opens |
|---|---|
| Wordmark | `/` |
| x, tiktok, youtube, facebook, instagram, pinterest | Outbound social profiles. Not followed. |
| Newsletter | `/email/esquire-newsletter` |
| About Us | `/about/a26377/about-us/` |
| Media Kit | `http://www.esquiremediakit.com/r5/home.asp` |
| Press Room | `https://www.hearst.com/news` |
| Contact Us | `/about/a2159/contact-us/` |
| Community Guidelines | `/about/a26373/community-guidelines/` |
| Advertise Online | `/about/a39935/advertise-online/` |
| Customer Service | `/service` |
| Subscribe | Offers URL, `cds_tracking_code=esqfooter` |
| Events & Promotions | `/promotions/` |
| Giveaways | `http://sweepstakes.esquire.com` |
| Gift Subscription | `https://www.esquire.com/gift-subscriptions/` |
| Privacy Notice, CA notices, DAA opt out | Hearst privacy notice anchors |
| Terms of Use | Hearst terms |
| Site Map | `/sitemap/` |
| COOKIES CHOICES | `href="#"`. Consent dialog. Not answered. |

The footer also prints "A Part of Hearst Digital Media" and a commission and AI-use note. No theme switch. No settings page signed out.

## Walls

| Control | Stops at |
|---|---|
| Sign In | Hearst Mylo card at `https://www.mylo.id/login`. Empty email field, Continue, passkey note, Continue with Google, Continue with Facebook, Continue with Apple, Continue with Microsoft, User ID + Password. Not submitted. Identity providers not clicked. Photographed in [signin-light-default.png](screenshots/signin-light-default.png). |
| Subscribe, Member Exclusives, Gift Subscription | Offers and shop pages. Join and checkout not followed. |
| Newsletter | `/newsletter-menu/`. Public list of newsletters with Subscribe toggles left OFF. Not submitted. Photographed in [newsletter-light-default.png](screenshots/newsletter-light-default.png). |
| My Bookmarks | `/my-stuff/`. Account wall. Not opened past the wall. |
| COOKIES CHOICES | Consent dialog. Not answered. |

No email, password, phone, or code was typed. No identity provider was clicked. No form was submitted.
