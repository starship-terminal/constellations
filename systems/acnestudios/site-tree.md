# Acne Studios site tree

Mapped 2026-11-21 from the public home page in headless Chromium, before screenshots. The root `https://www.acnestudios.com/` redirects to the served locale storefront at `/sg/en/home` (Salesforce B2C Commerce, `Sites-acne_sg-Site`). This file names controls and destinations. It does not record email addresses, phone numbers, or place names.

Nothing in this map was submitted. Login, register, order lookup, and return lookup are walls: the URL is recorded and the branch stops.

## Shell

Desktop header (1440). Phone header (390) replaces the category row with Menu.

| Control | Opens | Then |
|---|---|---|
| Logo (header image link) | `/sg/en/home` | Page |
| WOMAN (`button`, `aria-controls="category-shop-woman"`) | Mega-menu dialog, full width, role `dialog` | Links below. Close returns to the page |
| MAN (`aria-controls="category-shop-man"`) | Mega-menu dialog | Links below |
| BAGS (`aria-controls="category-bags"`) | Mega-menu dialog | Links below |
| SCARVES (`aria-controls="category-scarves"`) | Mega-menu dialog | Links below |
| GIFTS (`aria-controls="category-gifts"`) | Mega-menu dialog | Two links, repeated in the panel |
| SEARCH (`aria-controls="search"`) | Search dialog | Search field plus suggestion links. Not submitted |
| HELP (`aria-controls="customer-service"`) | 360px drawer, role `dialog` | Live chat (offline in this session), a telephone link, a mailto link, Order status, Register a return, FAQs |
| ACCOUNT (`a`) | `/sg/en/account` | Redirects to `/sg/en/lookup?rurl=8`, the sign-in wall. Stop |
| Bag count (`aria-controls="cart"`) | Empty bag drawer, 360px, role `dialog` | Sign in and Register links (walls). No checkout control while the bag is empty |
| Menu (phone only, `aria-controls="navigation"`) | Full-screen navigation drawer | See Phone menu |
| Search (phone, `aria-controls="search"`) | Same search dialog | |
| Account (phone) | `/sg/en/account` | Same sign-in wall. Stop |
| Bag (phone, `aria-controls="cart"`) | Same empty bag drawer | |

Footer columns are disclosure buttons. Their links are in the DOM when closed.

| Control | Opens |
|---|---|
| Sign up | Newsletter email field in the footer. Not filled, not submitted |
| Contact Us (`aria-controls="contactUs"`) | Disclosure: live chat, a telephone link, a mailto link |
| Live chat | No panel mounted in this session (control read as offline) |
| Help (`aria-controls="help"`) | Contact us, Order status, Register a return, FAQs |
| Client services (`aria-controls="clientServices"`) | Services index, Account article, Find a store, Product care, Gift cards |
| Company (`aria-controls="company"`) | About, Press (off-site), Careers (off-site), Sustainability, Legal & Privacy |
| Shipping-to button (`COUNTRY_SELECTOR:OPEN`) | Country and language selector. The click event fires. The panel did not mount in headless Chromium on 2026-11-21. Not captured as an open state |
| Cookie Settings | OneTrust preference dialog (`#onetrust-pc-sdk`, about 480×694) over the cookie banner. Not submitted. Consent buttons are never clicked |
| Social row | Off-site: Instagram, Facebook, X, YouTube, Pinterest, Weibo |

The cookie banner (`#onetrust-banner-sdk`, "Your cookie settings") mounts on first paint unless its SDK is blocked. It offers Continue without accepting, Cookie settings, and Accept all cookies. None of those are clicked for the capture. Later shots hide the banner remove-only.

## WOMAN menu

| Link | Destination | Kind |
|---|---|---|
| New Arrivals | `/sg/en/woman/new-arrivals/` | Listing |
| Gifts for Her | `/sg/en/woman/gift-guide-selection/` | Listing |
| Winter Dressing | `/sg/en/woman/winter-capsule/` | Listing |
| Seasonal Denim | `/sg/en/woman/seasonal-denim/` | Listing |
| Scarf Personalisation | `/sg/en/scarves/personalised/` | Listing |
| View all (clothing) | `/sg/en/woman/clothing/` | Listing |
| Jeans | `/sg/en/woman/jeans/` | Listing |
| Outerwear | `/sg/en/woman/outerwear/` | Listing |
| Sweatshirts | `/sg/en/woman/sweatshirts/` | Listing |
| Knitwear | `/sg/en/woman/knitwear/` | Listing |
| Trousers | `/sg/en/woman/trousers/` | Listing |
| T-shirts | `/sg/en/woman/t-shirts/` | Listing |
| Shirts & Blouses | `/sg/en/woman/shirts-and-blouses/` | Listing |
| Dresses | `/sg/en/woman/dresses/` | Listing |
| Suit Jackets | `/sg/en/woman/suit-jackets/` | Listing |
| Shorts | `/sg/en/woman/shorts/` | Listing |
| Skirts | `/sg/en/woman/skirts/` | Listing |
| View all (shoes and accessories) | `/sg/en/woman/shoes-and-accessories/view-all-accessories/` | Listing |
| Scarves | `/sg/en/scarves/` | Listing |
| Bags | `/sg/en/bags/` | Listing |
| Hats | `/sg/en/woman/hats/` | Listing |
| Shoes | `/sg/en/woman/shoes/` | Listing |
| Small Leather Goods | `/sg/en/woman/small-leather-goods/` | Listing |
| Jewellery | `/sg/en/woman/jewellery/` | Listing |
| Eyewear | `/sg/en/woman/eyewear/` | Listing |
| Belts | `/sg/en/woman/belts/` | Listing |
| Objects | `/sg/en/objects/objects.html` | Listing (redirects to `/sg/en/objects/`) |
| SS27 | `/sg/en/woman/ss27/` | Campaign listing |
| FW26 | `/sg/en/woman/fw26/` | Campaign listing |

## MAN menu

Same groups as WOMAN, under `/sg/en/man/…`, without dresses or skirts. Gifts for Him is `/sg/en/man/gift-guide-selection/`. View all clothing is `/sg/en/man/clothing/`. View all accessories is `/sg/en/man/shoes-and-accessories/view-all-accessories/`. Shirts is `/sg/en/man/shirts/`.

## BAGS menu

| Link | Destination |
|---|---|
| View all / style view all | `/sg/en/bags/` |
| All Bag Lines | `/sg/en/bags/all-lines/` |
| Camero | `/sg/en/bags/camero/` |
| Multipocket | `/sg/en/bags/multipocket/` |
| Musubi | `/sg/en/bags/musubi/` |
| Shoulder Bags | `/sg/en/bags/shoulder-bags/` |
| Top Handle Bags | `/sg/en/bags/top-handle-bags/` |
| Backpacks | `/sg/en/bags/backpack/` |
| Crossbody Bags | `/sg/en/all-bag-lines/crossbody/` |
| Totes | `/sg/en/bags/totes/` |
| Micro Bags | `/sg/en/bags/micro/` |
| Small Leather Goods | `/sg/en/woman/small-leather-goods/` |

## SCARVES menu

| Link | Destination |
|---|---|
| View all | `/sg/en/scarves/` |
| All Scarf Lines | `/sg/en/scarves/all-lines/` |
| Personalised Scarves | `/sg/en/scarves/personalised/` |
| Cashmere | `/sg/en/scarves/cashmere/` |
| Alpaca | `/sg/en/scarves/alpaca/` |
| Wool | `/sg/en/scarves/wool/` |
| Mohair | `/sg/en/scarves/mohair/` |
| Silk | `/sg/en/scarves/silk/` |
| Check | `/sg/en/scarves/checked/` |
| Solid | `/sg/en/scarves/solid/` |
| Logo | `/sg/en/all-scarf-lines/logo/` |
| Printed | `/sg/en/scarves/printed/` |

## GIFTS menu

| Link | Destination |
|---|---|
| Gifts for Her | `/sg/en/woman/gift-guide-selection/` |
| Gifts for Him | `/sg/en/man/gift-guide-selection/` |

## Search dialog

Suggestions (not typed, not submitted): Outerwear, Knitwear, Bags, Scarves, Jeans, each to `/sg/en/search?q=<word>`. Suggested products are product links with `?g=woman` or `?g=man`.

## Home page

Hero and editorial tiles, in addition to the shell:

| Control | Destination |
|---|---|
| Women's gift guide | `/sg/en/woman/gift-guide-selection/` |
| Men's gift guide | `/sg/en/man/gift-guide-selection/` |
| Product tiles in the hero | One product page each (template below) |
| Women's new arrivals | `/sg/en/woman/new-arrivals/` |
| Men's new arrivals | `/sg/en/man/new-arrivals/` |
| Women's jeans | `/sg/en/woman/jeans/` |
| Bags | `/sg/en/bags/` |
| Scarves | `/sg/en/scarves/` |
| Men's jeans | `/sg/en/man/jeans/` |
| Acne Paper tile | `/sg/en/acne-paper/palais-royal-open.html` redirects to `/sg/en/acne-paper/palais-royal/` |
| Hussein Chalayan | `/sg/en/hussein-chalayan/` |
| SS27 | `/sg/en/woman/ss27/` |
| Scarf personalisation | `/sg/en/scarves/personalised/` |
| FW26 runway | `/sg/en/woman/fw26-runway/` |
| Acne Paper Autoportrait | `/sg/en/acne-paper-autoportrait/acne-paper-autoportrait.html` redirects to `/sg/en/acne-paper-autoportrait/` |
| Acne Studios par Frédéric Malle | `/sg/en/acne-studios-par-frederic-malle/` |

Carousel Previous and Next move the hero. They do not open a new page.

## Listing page

Reached from any category link above. Shared template.

| Control | Opens |
|---|---|
| Product card | Product page. First card on women's new arrivals on this date: `/sg/en/wool-sweater-with-logo-blue-multi/C60119-ALD.html?g=woman` |
| FILTER (`aria-controls="filter-state-container"`) | 360px dialog: sort (Newest, Price high to low, Price low to high, Popularity) and facet groups (type, colour, and further facets below the fold). Choosing a facet reloads the listing. Sort and one facet are local listing state, not a checkout |
| LOAD MORE | Appends another product row on the same listing. No navigation |
| Hero Previous / Next | Moves the listing banner |

## Product page

| Control | Opens |
|---|---|
| Colour swatch | Same template, another colour URL |
| Size guide (`aria-controls="sizeguide-state-container"`) | Dialog over the page (measurements). Close returns to the product |
| Size cell (XXS through XXXL on this product) | Selected size. Local toggle. Sold-out sizes show Get notified |
| Get notified | Not opened. It asks for contact details |
| ADD TO BAG | Not clicked. It mutates the bag |
| WISHLIST | Not clicked. The menu's wishlist URL is an account wall |
| Delivery and returns (`aria-controls="deliveryEstimates"`) | 360px dialog with a postal-code field. Field not filled. Check not clicked |
| Gift wrapping (`aria-controls="giftwrapping"`) | 360px dialog. No form |
| Pick up in store (`aria-controls="storePickup"`) | 360px dialog. Store list stays behind a size selection. No store search submitted |

## Client services and help

| From | Destination | Stop? |
|---|---|---|
| Client services index | `/sg/en/client-services/` | No |
| Account article | `/sg/en/client-services/account.html` | No. Editorial, not the account app |
| Book appointment | `/sg/en/client-services/store-appointment.html` | Form not submitted |
| Pick up in-store | `/sg/en/client-services/pickup-in-store.html` | No |
| Find a store | `/sg/en/stores/` and `/sg/en/stores/stores.html` (same page) | Store list is public. No address is copied into this file |
| Personalised items | `/sg/en/client-services/personalised-items.html` | No |
| Product care | `/sg/en/client-services/productcare.html` | No |
| Gift wrapping article | `/sg/en/client-services/packaging.html` | No |
| Gift card | `/sg/en/gift-card/GIFT-CARD.html` | Amount and recipient fields not filled, not submitted |
| Contact us | `/sg/en/help/contact-us.html` | Form not submitted |
| FAQs | `/sg/en/help/faq.html` | Accordion items are on-page |
| Size guide article | `/sg/en/help/size-guide.html` | No |
| Order status | `/sg/en/shopping-help/get-order-status` | Form (order number, order email). Not filled. Stop |
| Register a return | `/sg/en/shopping-help/register-return` | Same lookup form. Not filled. Stop |
| Order tracking article | `/sg/en/shopping-help/order-status.html` | Editorial link from the services page |
| Shipping and returns | `/help/faq.html` with an accordion hash | FAQ anchor |

## Company

| Link | Destination | Note |
|---|---|---|
| About | `/sg/en/about/about.html` | Public |
| Sustainability | `/sg/en/company/sustainability/` | Public (the `.html` URL redirects) |
| Legal & Privacy | `/sg/en/companyfolder/company__terms-of-use.html` | Public |
| Press | `http://press.acnestudios.com/` | Off-site press room. Public, separate host |
| Careers | `https://www.acnestudios.com/sg/en/company/careers/careers.html` | Redirects to `https://careers.acnestudios.com/`. Off-site. Its cookie banner is not clicked |

## Phone menu

Menu opens `#navigation` (full viewport drawer).

| Control | Opens |
|---|---|
| Close | Dismisses the drawer |
| Search | `#search` |
| WOMAN | `category-shop-woman-state-container` inside the drawer. Same links as the desktop menu |
| MAN | `category-shop-man-state-container` |
| BAGS | `category-bags-state-container` |
| SCARVES | `category-scarves-state-container` |
| GIFTS | `category-gifts-state-container` |
| Wishlist | `/sg/en/account/wishlist?rurl=5` | Account wall. Stop |
| Account | `account-state-container`: Orders, My account, My information, Wishlist, Log out, Sign in (`/sg/en/my-account`), Register (`/sg/en/register-account`). Every one of those is an account wall. Stop |
| Stores | Demandware `Stores-Start`, same store directory |
| Shipping-to | Same country selector event. Panel did not mount |
| Help | `mobileCustomerServiceMenu`: chat, telephone, mailto, order status, register a return, size guide, FAQs, and the client-services links |

## Walls (URL recorded, branch stopped)

| Entry | Lands on | Why stopped |
|---|---|---|
| ACCOUNT, Sign in, bag drawer Sign in | `/sg/en/lookup?rurl=8` | Email field, then continue. Not filled |
| Register, bag drawer Register | `/sg/en/register-account` redirects to the same lookup | A previous session already passed an email and was asked for a password, a date of birth, and a phone. Not retyped. Not submitted |
| Wishlist, Orders, My account, My information, Log out | Account URLs with `rurl` | Signed-in only |
| Order status, Register a return | Lookup forms | Not filled, not submitted |
| Get notified, newsletter, gift-card recipient, appointment, postal code | Contact or address fields | Not filled, not submitted |
| Google or Apple on the lookup page | Third-party sign-in | Not clicked |
