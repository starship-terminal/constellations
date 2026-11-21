# ALO Yoga site tree

Mapped from the public homepage `https://www.aloyoga.com/` on 2026-11-21, before screenshots. The server redirects that URL to `https://www.aloyoga.com/en-sg` (Singapore storefront, HTTP 200, title "ALO | Yoga leggings, clothes, and accessories for studio to street"). Signed out. Desktop viewport 1440x900. Mobile drawer read at 390x844.

Nothing was typed. No form was submitted. Account, wishlist, and sign-in controls that open a login or join wall are recorded and that branch stops.

## Chrome

| Control | Opens |
|---|---|
| Wordmark (header logo) | `/en-sg` home |
| Search icon (`#main-navbar-search-icon`, class `main-navbar__icon--search`) | In-page search drawer on `/en-sg`. Role `search`, placeholder "Search". Shows trending searches (socks, airlift, leggings, sweatpants, tops) and popular products. Close control `.searchform-close`. Does not navigate. |
| Account icon and "Sign in to get rewards" | Login wall. Direct navigation of `/en-sg/account` redirects to `https://www.aloyoga.com/en-sg/account/login?return_url=%2Fen-sg%2Faccount`. The page shows Join now and Sign in, with name, email, password, phone and birthday fields. Branch stops. Not typed. |
| Wishlist icon (`a[aria-label=Wishlist]`, `data-logged-out=true`) | Join / sign-in modal on the same URL (`alo-modal-container`: Join now, Sign in, name, email, password, phone, birthday). Branch stops. Not typed. |
| Cart icon (`a[aria-label=Cart]`) | `/en-sg/cart` |
| Language and ship-to (`button.sc-modal-trigger`, label shows Singapore) | Country / language dialog (`.sc-modal-trigger`). Probe click did not mount a readable dialog body beyond the trigger label. Not submitted. |
| Promo strip | Present above the nav ("EXTENDED RETURNS & EXCHANGES"). Not a separate page. |
| Osano cookie dialog | Mounts on first paint over `/en-sg`. Controls: Storage Preferences, Targeted Advertising, Personalization, Analytics, Save, Accept All, Reject Non-Essential, Close. Not clicked. Captured as it arrives, then hidden. |
| Skip to content | `#MainContent` on the current page |
| Play / pause (`a.play-pause-button`) | `javascript:void(0)`. Pauses a hero video. No navigation. |

## Desktop nav

Hover (class `navOpenOnHover`) opens a mega-menu in place. The item itself is also a link.

### Women

Control: `a.main-nav__item` `data-nav=women`. Click opens `/en-sg/collections/womens-shop-all`. Hover opens the mega-menu below.

| Label | Opens |
|---|---|
| Shop All | `/en-sg/collections/womens-shop-all` |
| Leggings | `/en-sg/collections/womens-leggings` |
| Sweatshirts & Hoodies | `/en-sg/collections/womens-sweatshirts-hoodies` |
| Jackets & Coats | `/en-sg/collections/womens-jackets` |
| Matching Sets | `/en-sg/collections/best-sets-1` |
| Tops & Tanks | `/en-sg/collections/tops` |
| Sweatpants | `/en-sg/collections/sweatpants` |
| Pants & Trousers | `/en-sg/collections/pants` |
| Sports Bras | `/en-sg/collections/bras` |
| Shorts | `/en-sg/collections/womens-shorts` |
| Sweaters & Knitwear | `/en-sg/collections/sweaters` |
| Skirts | `/en-sg/collections/skirts` |
| Dresses | `/en-sg/collections/dresses` |
| Intimates | `/en-sg/collections/underwear` |
| Onesies | `/en-sg/collections/onesies` |
| New Arrivals | `/en-sg/collections/new-arrivals` |
| Best Sellers | `/en-sg/collections/bestsellers` |
| Travel in ALO | `/en-sg/collections/travel-in-alo` |
| Everyday Basics | `/en-sg/collections/elevated-basics` |
| Last Few Pieces | `/en-sg/collections/almost-gone-1` |
| Outerwear Edit | `/en-sg/pages/outerwear` |
| Leggings 101 | `/en-sg/pages/leggings` |
| New to ALO? Start Here | `/en-sg/pages/new-to-alo` |
| Deep Gravel | `/en-sg/collections/deep-gravel` |
| Moonshadow Blue | `/en-sg/collections/moonshadow-blue` |
| Espresso | `/en-sg/collections/espresso-1` |
| Frosted Pearl | `/en-sg/collections/frosted-pearl` |
| Rich Bordeaux | `/en-sg/collections/rich-bordeaux` |
| Navy | `/en-sg/collections/womens-navy` |
| Ivory | `/en-sg/collections/ivory` |
| Yoga | `/en-sg/collections/yoga` |
| Pilates | `/en-sg/collections/pilates` |
| Run | `/en-sg/collections/run` |
| Lounge | `/en-sg/collections/lounge-shop` |
| Train | `/en-sg/collections/train` |
| Court Sports | `/en-sg/collections/tennis-inspired` |
| Shop All | `/en-sg/collections/accessories-shop-all` |
| Hair Accessories | `/en-sg/collections/hair-accessories` |
| Hats | `/en-sg/collections/hats` |
| Socks | `/en-sg/collections/socks` |
| Bags | `/en-sg/collections/bag-collection` |
| Small Leather Goods | `/en-sg/collections/small-leather-goods` |
| Sunglasses | `/en-sg/collections/sunglasses` |
| Shoes | `/en-sg/collections/womens-shoes` |
| Yoga Mats & Equipment | `/en-sg/collections/yoga-gear` |
| Gift Cards | `/en-sg/collections/gift-cards` |

### Men

Control: `a.main-nav__item` `data-nav=men`. Click opens `/en-sg/collections/mens-shop-all`. Hover opens the mega-menu below.

| Label | Opens |
|---|---|
| Shop All | `/en-sg/collections/mens-shop-all` |
| Sweatshirts & Hoodies | `/en-sg/collections/mens-sweatshirts-hoodies` |
| Shirts | `/en-sg/collections/tees-tanks` |
| Sweatpants | `/en-sg/collections/mens-sweatpants` |
| Pants | `/en-sg/collections/mens-pants` |
| Jackets | `/en-sg/collections/mens-jackets` |
| Shorts | `/en-sg/collections/mens-shorts` |
| Sweaters | `/en-sg/collections/mens-sweaters` |
| Boxers | `/en-sg/collections/mens-underwear` |
| Best Sellers | `/en-sg/collections/mens-bestsellers` |
| New Arrivals | `/en-sg/collections/mens-new-arrivals` |
| Explore Men's | `/en-sg/pages/mens` |
| Almost Gone | `/en-sg/collections/mens-almost-gone` |
| New to ALO? Start Here | `/en-sg/pages/new-to-alo` |
| Train | `/en-sg/collections/mens-train` |
| Run | `/en-sg/collections/mens-run` |
| Tennis | `/en-sg/collections/mens-tennis` |
| Yoga | `/en-sg/collections/mens-yoga` |
| Recovery | `/en-sg/collections/mens-lounge-shop` |
| Shop All | `/en-sg/collections/accessories-shop-all` |
| Hats | `/en-sg/collections/hats` |
| Shoes | `/en-sg/collections/mens-shoes` |
| Socks | `/en-sg/collections/socks` |
| Yoga Mats & Equipment | `/en-sg/collections/yoga-gear` |
| Gift Cards | `/en-sg/collections/gift-cards` |

### Shoes

Control: `a.main-nav__item` `data-nav=shoes`. Click opens `/en-sg/collections/shoes`. Hover opens the mega-menu below.

| Label | Opens |
|---|---|
| Shop All | `/en-sg/collections/shoes` |
| Sneakers | `/en-sg/collections/sneakers` |
| Slippers & Slides | `/en-sg/collections/slides` |
| Boots | `/en-sg/collections/boots` |
| Explore The Collection | `/en-sg/pages/shoes` |
| ALO Sunset Sneaker | `/en-sg/products/a1219u-alo-sherpa-sunset-sneaker-mule-rich-chestnut-ivory` |
| ALO Malibu Boot | `/en-sg/products/a1172u-alo-aspen-lace-up-boot-winter-ivory` |
| Alo Runner | `/en-sg/products/a0590u-alo-runner-white-white` |

### Atelier

Control: `a.main-nav__item` `data-nav=atelier`. Click opens `/en-sg/collections/summer-atelier`. Hover opens the mega-menu below.

| Label | Opens |
|---|---|
| Explore Atelier | `/en-sg/pages/summer-atelier` |
| Bag Collection | `/en-sg/collections/bag-collection` |
| Small Leather Goods | `/en-sg/collections/small-leather-goods` |
| Sunglasses Collection | `/en-sg/collections/sunglasses` |
| Atelier Collection | `/en-sg/collections/summer-atelier` |
| ALO Intention Crystals | `/en-sg/collections/alo-intention-crystals` |
| Bag Campaign | `/en-sg/pages/bag-collection` |
| Sunglasses | `/en-sg/pages/sunglasses` |
| Atelier Campaign | `/en-sg/pages/summer-atelier` |

### Gift Guide

Control: `a.main-nav__item` `data-nav=gift guide`. Click opens `/en-sg/pages/gift-guide`. Hover opens the mega-menu below.

| Label | Opens |
|---|---|
| Shop All Gifts | `/en-sg/collections/gift-guide` |
| Gifts For Her | `/en-sg/collections/top-gifts-for-her` |
| Gifts For Him | `/en-sg/collections/top-gifts-for-him` |
| Top Rated Gifts | `/en-sg/collections/top-rated-gifts` |
| Gift Cards | `/en-sg/collections/gift-cards` |
| For The Jet Setter | `/en-sg/collections/travel-in-alo` |
| For The Homebody | `/en-sg/collections/lounge-shop` |
| For the Athlete | `/en-sg/collections/studio-staples-story` |

## Mobile chrome (390)

| Control | Opens |
|---|---|
| Hamburger (`button.navbar__toggler.hamburger`) | In-page drawer `.mobile-nav--open` on `/en-sg`. |
| Search (`button.navbar__toggler.mobile-search-button`) | Mobile search drawer. Same search field. Not submitted. |
| Account | Login wall. Branch stops. |
| Wishlist | Join / sign-in modal. Branch stops. |
| Cart | `/en-sg/cart` |
| Sign in (drawer CTA) | Login wall. Branch stops. |

Drawer links read after opening the hamburger:

| Label | Opens |
|---|---|
| Cart | `/en-sg/cart` |
| BEST SELLERS | `/en-sg/collections/bestsellers` |
| NEW ARRIVALS | `/en-sg/collections/new-arrivals` |
| SHOES | `/en-sg/collections/womens-shoes` |
| NEW TO ALO? START HERE | `/en-sg/pages/new-to-alo` |
| WOMEN'S | `/en-sg/collections/womens-shop-all` |
| NEW IN | `/en-sg/collections/new-arrivals` |
| MEN'S | `/en-sg/collections/mens-new-arrivals` |
| SHOP NEW IN | `/en-sg/collections/new-arrivals` |
| PANTS | `/en-sg/collections/pants` |
| SWEATSHIRTS | `/en-sg/collections/womens-sweatshirts-hoodies` |

## Footer

Headings read on the homepage: Customer Service, My Account, Information, Follow Us, Get the App, newsletter signup, Language and ship-to. Newsletter email field is not filled and not submitted.

| Label | Opens |
|---|---|
| Help Center | `/en-sg/pages/help-center` |
| Track My Order | `/en-sg/pages/track-my-order` |
| Shipping | `/en-sg/pages/orders-and-shipping-support` |
| Returns & Exchanges | `/en-sg/pages/returns-support` |
| Gift Card | `/en-sg/collections/gift-cards` |
| Gift Card Balance | `/en-sg/pages/gift-card-balance` |
| Size Guide | `/en-sg/pages/size-chart` |
| Reviews | `/en-sg/pages/reviews` |
| Login or Register | `/en-sg/account` (login or account wall, branch stops) |
| Order History | `/en-sg/account` (login or account wall, branch stops) |
| Shipping & Billing | `/en-sg/account/addresses` (login or account wall, branch stops) |
| ALO Access | `/en-sg/pages/access` |
| We Are ALO | `/en-sg/pages/we-are-alo` |
| Blog | `/en-sg/blogs/alo-blog` |
| Yoga Studios | `/en-sg/pages/studios` |
| Stores | `/en-sg/pages/stores` |
| Events | `/en-sg/pages/alo-events` |
| Pro Program | `/en-sg/pages/proprogram` |
| Careers | `/en-sg/pages/careers` |
| ALO Wellness Club | `https://www.alomoves.com/` |
| ALO Gives | `/en-sg/pages/alo-gives` |
| ALO Foundation | `/en-sg/pages/alo-foundation` |
| Privacy Policy | `/en-sg/pages/privacy-policy` |
| Terms | `/en-sg/pages/terms-of-use` |
| Privacy | `/en-sg/pages/privacy-policy` |
| Cookie Policy | `/en-sg/pages/cookie-policy` |
| Cookie Preferences | `/en-sg` |

## Homepage body

Hero and editorial tiles on `/en-sg`, after the nav. Image-only tiles whose accessible name was a CSS rule are omitted.

| Label | Opens |
|---|---|
| DEEP GRAVEL A darker take on your favorite neutral. Shop Deep Gravel | `/en-sg/collections/deep-gravel` |
| IVORY A soft, warm shade with timeless appeal. Shop Ivory | `/en-sg/collections/ivory` |
| FROSTED PEARL A soft, pearlescent shade with subtle sheen. Shop Frosted Pearl | `/en-sg/collections/frosted-pearl` |
| ESPRESSO A deeply saturated shade with all-year appeal. Shop Espresso | `/en-sg/collections/espresso-1` |
| MOONSHADOW BLUE Enter a new phase in this sleek and celestial shade. Shop Moonsh | `/en-sg/collections/moonshadow-blue` |
| Lounge | `/en-sg/collections/lounge-shop` |
| Run | `/en-sg/collections/run` |
| Train | `/en-sg/collections/train` |
| Yoga | `/en-sg/collections/yoga` |
| Pilates | `/en-sg/collections/pilates` |
| Court Sports | `/en-sg/collections/tennis-inspired` |
| Track My Order | `/en-sg/pages/track-my-order` |
| Shipping | `/en-sg/pages/orders-and-shipping-support` |
| Returns & Exchanges | `/en-sg/pages/returns-support` |
| Gift Card | `/en-sg/collections/gift-cards` |
| Gift Card Balance | `/en-sg/pages/gift-card-balance` |
| Size Guide | `/en-sg/pages/size-chart` |
| Reviews | `/en-sg/pages/reviews` |
| Login or Register | `/en-sg/account` |

## Login and signup walls (branch stops)

These URLs and dialogs were reached or confirmed as the next hop. No field was typed. No code was sent. Google and Apple were not clicked. No account was created.

| Entry | Stop |
|---|---|
| Account icon, footer Login or Register, footer Order History, mobile Sign in | `https://www.aloyoga.com/en-sg/account` redirects toward `https://www.aloyoga.com/en-sg/account/login` (email and password). |
| Footer Shipping and Billing | `/en-sg/account/addresses` (account wall). |
| Wishlist icon | Join / sign-in modal (name, email, password, phone, birthday). |
| ALO Access | `/en-sg/pages/access` is a public marketing page in the tree. Any join or plan form on it is not filled. |

## Capture set

Pages captured at desktop 1440x900 and phone 390x844, plus the interactions that stay on the public side:

- Home, with consent dialog, women mega-menu, search drawer.
- One collection from each nav family: women shop all, men shop all, shoes, atelier, gift guide.
- One product page discovered from the women grid (not hardcoded).
- New to ALO, empty cart, help center, size guide, stores locator, we are ALO.
- Account login URL recorded and screenshotted as a wall only. Not typed.
- Mobile: home, hamburger drawer, search drawer, women grid, product page, cart.

Not captured, with the reason: checkout and bag contents (nothing added to bag); signed-in account, order history, addresses; newsletter, join, birthday, phone, and plan fields (forms not submitted); country dialog body if it does not mount; dark theme (none offered on the storefront).
