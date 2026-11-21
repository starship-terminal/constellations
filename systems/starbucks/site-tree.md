# Starbucks public site tree

Mapped from https://www.starbucks.com/ on 2026-11-21 in headless Chromium, signed out, before screenshots. Official consumer site is `www.starbucks.com` (Starbucks Coffee Company). Header links leave that host for the shop and for Auth0 sign-in. No email, password, card number, security code, location, or form was typed or submitted.

Widths planned for every reachable public state: desktop 1440×900 and phone 390×844. One theme: light (`color-scheme: normal`). No dark toggle on the public pages.

Cookie banner ("This site uses cookies, but not the kind you eat", buttons Change cookie settings and Agree) covers menu, rewards, gift, locator, and sign-in. It is hidden, never clicked, so no consent is posted.

## Header (every marketing page)

| Control | Opens |
|---|---|
| Logo "Home, Starbucks" | https://www.starbucks.com/ |
| MENU | https://www.starbucks.com/menu |
| REWARDS | https://www.starbucks.com/rewards |
| GIFT CARDS | https://www.starbucks.com/gift |
| STARBUCKS® SHOP | https://www.shop.starbucks.com/ (other host; mapped, not captured as this package) |
| Find a café | https://www.starbucks.com/store-locator (search UI only; a search that returns street addresses is not screenshotted) |
| Sign in | https://www.starbucks.com/account/signin then https://auth.starbucks.com/u/login (login wall; record and stop) |
| Join now | https://www.starbucks.com/account/create then https://auth.starbucks.com/u/signup (signup wall; record and stop) |

Phone width: the same links sit behind the header button "Open menu".

## Home

https://www.starbucks.com/

| Control | Opens |
|---|---|
| Start an order | /menu |
| See the holiday menu | /discover/featured-menu |
| Join now (promo) | /account/create (signup wall) |
| Learn more | https://about.starbucks.com/ (other host) |
| Listen now | https://starbucks.lnk.to/HolidayBlend (other host) |
| Shop now | https://www.shop.starbucks.com/ (other host) |
| Footer accordion buttons About Us, Careers, Social Impact, For Business Partners, Ways to Shop | expand the footer column; they do not navigate |

## Menu

https://www.starbucks.com/menu

Category links, each a public product grid:

| Group | Control | Opens |
|---|---|---|
| (side) | Previous | /menu/previous (empty signed-out state; Join now goes to signup wall) |
| (side) | Favorites | /menu/favorites (empty signed-out state; Join now goes to signup wall) |
| The Latest | Trending | /menu/the-latest/trending |
| The Latest | Holiday Classics | /menu/the-latest/holiday-classics |
| Coffee & Espresso | Hot Coffee & Espresso | /menu/coffee-espresso/hot-coffee-espresso |
| Coffee & Espresso | Cold Coffee & Espresso | /menu/coffee-espresso/cold-coffee-espresso |
| Protein | Protein Beverages | /menu/protein/protein-beverages |
| Tea | Chai, Matcha, Hot Tea, Iced Tea | /menu/tea/chai, /matcha, /hot-tea, /iced-tea |
| Refreshment | Refreshers, Energy Refreshers | /menu/refreshment/refreshers, /energy-refreshers |
| Frappuccino® Blended Beverage | Coffee Frappuccino®, Crème Frappuccino® | /menu/frappuccino-blended-beverage/coffee-frappuccino, /creme-frappuccino |
| Other Sips | Hot Chocolate, Lemonade & More; Bottled Beverages | /menu/other-sips/hot-chocolate-lemonade-more, /bottled-beverages |
| Food | Breakfast, Bakery, Treats, Lunch, Snacks | /menu/food/breakfast, /bakery, /treats, /lunch, /snacks |
| At-home coffee | Whole Bean, Starbucks VIA® Instant, Shopping Bag | /menu/at-home-coffee/whole-bean, /starbucks-via-instant, /shopping-bag |
| For item availability | Choose a café | /store-locator?source=menu (locator; not screenshotted once results show addresses) |

A product card opens /menu/product/{id}/{form}, for example /menu/product/407/hot (Caffè Latte). On that page:

| Control | Opens |
|---|---|
| Size radios Short, Tall, Grande, Venti | selected size on the same page |
| Milk and Espresso & Shot Options selects | same page |
| Quantity minus / Quantity add | same page |
| Customize | expands customizer sections (Milk, Flavors, Toppings, Cold Foams, Tea) on the same page; no dialog |
| Add to Order | starts an order; not submitted |
| See calories disclaimer | disclosure on the same page |
| Account (in the app chrome, not the marketing header) | a hidden hamburger item "Account sub-menu. Back to Main Menu"; not opened |
| Sign in / Join now in that chrome | login or signup wall |

## Rewards

https://www.starbucks.com/rewards

| Control | Opens |
|---|---|
| Star buttons 25, 60, 100, 200, 300, 400 | selected reward tier on the same page |
| Join now | /account/create (signup wall) |
| View details (Delta) | https://www.deltastarbucks.com/ (other host) |
| View details (Marriott) | /rewards/partnerships/marriottbonvoy |
| Join and Link / Unlink your accounts on the partnership page | /account/signin or /account/create with a return URL (wall; stop) |
| download the app | https://starbucks.app.link/ (other host) |
| Check out the FAQs | https://about.starbucks.com/starbucks-rewards-faq/ (other host) |
| Terms | /terms/rewards |

## Gift cards

https://www.starbucks.com/gift

| Control | Opens |
|---|---|
| Category headings FEATURED, THANKSGIVING, BIRTHDAY, ZODIAC, THANK YOU, CELEBRATION, HOLIDAY | anchors or /gift/category/{name} |
| See all (Featured) | /gift/category/featured |
| A card (Thanksgiving, and the same pattern for the others) | /gift/{id}, for example /gift/00000208 |
| Next slide | carousel on the same page |
| Check balance | dialog "Check balance" with Card number and Security code. Not filled. Not submitted. |
| eGift history | account wall if it requires sign-in; not followed into a session |
| FAQ buttons (Do Starbucks gift cards expire?, and the others) | expand on the same page |
| Gift from your phone / More ways to gift | /how-to-gift-a-starbucks-gift-card |
| Shop now (bulk) | https://www.starbuckscardb2b.com/ (other host) |
| On a card page: amount select, recipient name, recipient email, note, sender name, sender email, Add another recipient, Checkout | form. Not filled. Not submitted. |

## Store locator (mapped, not screenshotted)

https://www.starbucks.com/store-locator redirects to a map query. Controls: order-type radios, search "Find a café", Submit search term, Filter, map camera controls. A search that lists cafés shows street addresses, so this page is mapped and not screenshotted. Store detail URLs are not opened.

## Ordering and delivery

| Control | Opens |
|---|---|
| Footer Order and Pick Up Options | /stores-and-ordering |
| Classic Café, Drive-thru, Reserve, Delivery, Groceries anchors | in-page sections |
| Find a Classic Café | /store-locator (not screenshotted) |
| Starbucks Reserve® | https://www.starbucksreserve.com/ (other host) |
| DoorDash, Grubhub, Uber Eats | other hosts |
| Footer Delivery | /stores-and-ordering/delivery |
| FAQ buttons on delivery | expand on the same page |
| Start an order / Order with the app | https://starbucks.app.link/ (other host) |
| Footer Order on the App | /download-app (App Store and Google Play links; not followed into stores) |

## Contact, legal, business

| Control | Opens |
|---|---|
| Footer Contact Us | /contact (mailto links to published press and investor addresses; those strings are not copied into the package) |
| Customer Service Site | https://customerservice.starbucks.com/ (other host) |
| Privacy Notice | /terms/privacy-notice redirects to /privacy |
| Terms of Use | /terms/starbucks-terms-of-use |
| Consumer Health Privacy Notice | /consumer-health-data-privacy-notice |
| Do Not Sell or Share My Personal Information | /personal-information (email field and Submit; not filled, not submitted) |
| Accessibility (footer) | https://about.starbucks.com/accessibility/ (other host; dialogs for search, region, nav) |
| Landlord Support Center | /business/landlord-faq then child pages /eft-direct-deposit, /contacting-starbucks, /account-management, /landlord-billing, /1099-frequently-asked-questions |
| Suppliers | /business/suppliers (standard buttons expand on the page) |
| /responsibility/reporting-hub | styled 404 "We can't find the page you're looking for." |

## Login and signup walls (stop)

| URL | What it shows | Stop |
|---|---|---|
| https://www.starbucks.com/account/signin | redirects to https://auth.starbucks.com/u/login | email (username) and password fields, Show password, Forgot your password?, Keep me signed in, Sign in, Join now. Password not submitted. Email not typed. |
| https://www.starbucks.com/account/create | redirects to https://auth.starbucks.com/u/signup | first name, last name, email, password, optional email opt-in, terms checkbox. Not filled. Not submitted. |
| /account/settings, /rewards/my-rewards | redirect to sign-in with a returnUrl | stop |
| /account/cards, /menu/favorites, /menu/previous | public empty state plus Sign in / Join now | the empty page is reachable; the sign-in control is a wall |

An error banner "Something went wrong on our end" with Got it appeared on the sign-in page during mapping. It is the product's own error, not a submitted form.

## Other hosts (mapped, not this package)

about.starbucks.com, shop.starbucks.com, archive.starbucks.com, investor.starbucks.com, customerservice.starbucks.com, careers.starbucks.com, alumni.starbucks.com, athome.starbucks.com, starbuckscardb2b.com, starbucksreserve.com, social profiles. Newsletter email fields on about.starbucks.com are not filled.
