# Creative Market public site tree

Mapped signed out on 2026-11-21 from [https://creativemarket.com/](https://creativemarket.com/) in the T3 preview, incognito profile, CSS viewport 1440×900. `session.isAuthenticated` is false. The header shows Join and Log in, not an account avatar.

The CookieYes banner ("We value your privacy") was hidden and never answered. Reject All, Accept All, and Customize were not clicked. No email, password, phone, or code was typed. No form was submitted. No identity provider was clicked. No checkout was started. One theme: `data-theme="legacy"` (light). No dark toggle on the public homepage.

## Header, desktop 1440

The header is one row: search, wordmark, overflow, Join, Log in, Save 25%, cart. A second row is the category bar.

| Control | Opens |
|---|---|
| Search field, placeholder "Search millions of creative assets…" | Local field in `form.search-field.site-header-search`. Not submitted. The category control beside it reads All Categories. |
| Wordmark (`a.standard-logo`) | https://creativemarket.com/ |
| Overflow (`button[data-testid=header-overflow-trigger]`) | Menu `ul[data-testid=header-overflow-menu]`. See below. |
| Join | https://creativemarket.com/sign-up (signup wall; not followed past the wall) |
| Log in | https://creativemarket.com/sign-in (login wall; not submitted) |
| Save 25% | https://creativemarket.com/membership |
| Cart (`button[data-testid=header-cart]`, count 0) | Cart panel or page. Not used to check out. |

The signed-out DOM also holds a hidden user dropdown (My profile, My purchases, My collections, My likes, Messages, Notifications, Shop updates, Settings, Log out) and a hidden shop menu (Earnings, Shop profiles, Dashboard, Sales, Payouts & taxes, Products, Add a new product, Marketing tools, Discounts, Settings). Neither is painted. Add a new product points at `/account/products/new`. Those items are not offered on this signed-out surface.

## Overflow menu

Opened from the overflow button. Three links.

| Item | Opens |
|---|---|
| Enterprise | https://creativemarket.com/enterprise |
| Free Downloads | https://creativemarket.com/free-goods |
| Open a Shop | https://creativemarket.com/sell |

## Category bar

Hover opens a mega menu on the same page. The labelled link, when it has an href, also navigates.

| Control | Opens |
|---|---|
| FONTS | https://creativemarket.com/fonts, and a fonts mega menu (classifications, styles, aesthetics, eras, purpose, plus Enterprise Fonts, Free Fonts & More, Blog, Find by image at `/font-finder`, Find your font at `/creative-wingman`) |
| TEMPLATES | https://creativemarket.com/templates-themes, and a templates mega menu (presentations, job search, marketing, website themes, print, social, software, mockups) |
| GRAPHICS & ILLUSTRATIONS | https://creativemarket.com/graphics-illustrations, and a graphics mega menu (graphics, illustrations, icons, patterns, textures) |
| BRUSHES & EFFECTS | https://creativemarket.com/brushes-more, and a brushes mega menu (brushes, effects, software, plug-ins, palettes, gradients, shapes, presets) |
| MORE | No href. Mega menu: Photos (`/photos` and topics) and 3D (`/3d` and model types), plus See all memberships (`/membership`) |
| SALE | https://creativemarket.com/sale |
| INSPIRATION | No href. Mega menu: seasonal finds, font-alternative posts, Blog, Free Downloads, Design Trends (`/trends`), Staff Picks, Open a Shop, Plans & Pricing |
| ENTERPRISE | https://creativemarket.com/enterprise |

## Homepage body

https://creativemarket.com/

| Control | Opens |
|---|---|
| Hero, alt "Holiday Finds" | https://creativemarket.com/finds/holiday |
| Products from Featured Shops / Explore Products | https://creativemarket.com/search?featuredShops=1&sort=trending |
| A product card | that product, for example `/Pam9tka/292491471-Christmas-collage-cut-out-of-paper`. Shop name links to the shop, for example `/Pam9tka` |
| Popular Fonts / Explore Fonts | https://creativemarket.com/fonts |
| Staff Picks / Explore Staff Picks | https://creativemarket.com/search?staffPicks=1&sort=handpicked |
| Popular Photos / Explore Photos | https://creativemarket.com/photos |
| Popular Graphics | a graphics listing |
| Popular Procreate Brushes | a brushes listing |
| Popular Font Alternatives | blog posts such as `/blog/gotham-alternatives` |
| Start Earning with Creative Market | `/sell` and the ambassador page |
| A blog card under Tips, Tricks, and Trends | that post, for example `/blog/fall-color-of-the-season-golden-amber` |
| Newsletter email + SIGN UP | Customer.io form. Not submitted. |
| Licensing Questions? Let's Chat! | Chat launcher on the same page. Not opened. Dismiss was not clicked. |

## Footer

| Column | Control | Opens |
|---|---|---|
| Earn | Affiliate Partner Benefits | https://creativemarket.com/affiliates |
| Earn | Shop Benefits | https://creativemarket.com/sell |
| Earn | Become an Ambassador | https://ambassadors.creativemarket.com/ (other host; not captured) |
| Resources | Blog | https://creativemarket.com/blog |
| Resources | Collections | https://creativemarket.com/collections |
| Resources | Help Center | https://support.creativemarket.com/hc/en-us (other host; not captured) |
| Resources | Licenses | https://creativemarket.com/licenses/general |
| The Goods | Free Drops | https://creativemarket.com/free-goods |
| The Goods | Enterprise Sales | https://creativemarket.com/enterprise |
| Company | About | https://creativemarket.com/about |
| Company | Brand | https://creativemarket.com/brand |
| Company | Careers | https://creativemarket.com/careers |
| Check out More Fonts | Fontspring | https://fontspring.com/ (other host; not captured) |
| Check out More Fonts | Gotham, Futura, Avenir, Helvetica, Gilroy alternatives | those `/blog/*-alternatives` posts |
| Check out More Fonts | Fonts Sitemap | https://creativemarket.com/fonts/sitemap |
| Social | Dribbble, Pinterest, Facebook, X, Instagram | those public profiles (other hosts; not captured) |
| Legal | Privacy Policy | https://creativemarket.com/privacy |
| Legal | Terms of Service | https://creativemarket.com/terms |
| Legal | Chatbot Disclaimer | https://creativemarket.com/chatbotdisclaimer |
| Legal | Cookie Policy | https://creativemarket.com/cookiepolicy |
| Legal | Cookie Preferences (Do Not Sell/Share) | `javascript:void(0)`, the CookieYes preference center. Not opened. |

## Phone width

The header collapses. `button[data-testid=hamburger-menu-trigger]` is the menu control (hidden at 1440, where its box is 0 wide). A close control sits in `.mobile-menu-header__button--close-btn`. The drawer lists Fonts, Templates & Themes, Graphics, Photos, Illustrations, Icons, Mockups, Brushes & More, 3D, and More, then Join Creative Market and Log in.

The phone shots were requested at 390×844. Playwright reported `innerWidth` 394 and `innerHeight` 853, and the PNGs are 780×1688 (devicePixelRatio 2). They are labelled with that measured width.

## Stopped

Join, Log in, cart checkout, newsletter submit, identity providers, and the chat launcher are not followed into a submit. Add to cart and Buy now on a product page are not used.

`/sign-in` did not paint a form. Headless Chromium stayed on Cloudflare "Just a moment..." ("Performing security verification"). That page was not solved and was not screenshotted. `/sign-up` was not opened.
