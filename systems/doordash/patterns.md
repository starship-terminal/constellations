# DoorDash patterns

How the measured components combine on doordash.com's signed-out surface,
read from the screenshots and the component entries in
[components.md](components.md). Every page is the product's own SSR output
rendered from an Internet Archive snapshot (live *.doordash.com
Cloudflare-blocks this client; snapshot ids in
[raw/archive-urls.json](raw/archive-urls.json)). The consumer stack is
consumer-web-next (Next.js SSR, styled-components) over the prism token
system; careersatdoordash.com is a separate WordPress/Tailwind stack.
Values are the `light` set unless marked.

## Signed-in shell (2026-11-20)

The signed-in consumer app keeps the red wordmark and a 64px header: address control labeled Your Address, a notification bell, and a cart pill that read 0 on this account ([signed-in-password-desktop](screenshots/signed-in-password-desktop.png)). Account pages add a left rail (Home, Grocery, Retail, Convenience, Browse All, Orders, Account). Account opens a menu with View Profile, Home, Pickup, Orders, Account, Saved stores, My rewards, Payment, Gift card, Help, and Sign out ([signed-in-account-menu-desktop](screenshots/signed-in-account-menu-desktop.png)). Sign out was not clicked.

Empty states are a single ink line on white. Orders says "No Previous Deliveries, Order Today!" ([signed-in-orders-desktop](screenshots/signed-in-orders-desktop.png), phone [signed-in-orders-phone](screenshots/signed-in-orders-phone.png)). Rewards centres a burger illustration under "No rewards...yet" ([signed-in-rewards-desktop](screenshots/signed-in-rewards-desktop.png)). Help repeats the empty-orders line and pins a Help Center chip ([signed-in-help-desktop](screenshots/signed-in-help-desktop.png)).

Settings stay on the same shell. Profile is a two-column form with Change Password and Manage Account as red text links; Save stays disabled until a field changes, and it was not pressed ([signed-in-profile-desktop](screenshots/signed-in-profile-desktop.png)). Change password is three empty fields and a disabled "Change my password" button ([signed-in-password-desktop](screenshots/signed-in-password-desktop.png)). Manage account offers Request Archive and Delete Account as red links; neither was followed ([signed-in-manage-account-desktop](screenshots/signed-in-manage-account-desktop.png)).

The only create surface opened was gift cards: a card carousel, a red Buy Gift Card button, and a disabled Redeem Gift Card field ([signed-in-gift-cards-desktop](screenshots/signed-in-gift-cards-desktop.png)). Neither button was used. Checkout, cart add, DashPass purchase, and address entry were not started. The walk is recorded in [login-review.json](login-review.json).

## The marketing hero

The home page ([home-light-default](screenshots/home-light-default.png))
opens on the campaign field — a 1440 x 650 band in the DoorDash red
`color.action.primary.default` (#eb1700) with the Sign In / Sign Up pair
floating top-right, no separate top bar
([hero-band](components/crops/hero-band-default.png)). Sign In is the
solid red pill — #eb1700 fill, white text
([signin-btn](components/crops/signin-btn-default.png)); Sign Up is the
inverted pill — white fill, ink text
([signup-btn](components/crops/signup-btn-default.png)).
Centred on the field: the DOORDASH wordmark
([logo](components/crops/logo-default.png)), the uppercase condensed
campaign headline `$0 DELIVERY FEE ON FIRST ORDER` in TTNormsProCond-Blk
at 900 ([hero-title](components/crops/hero-title-default.png)) with the
fees-disclaimer line under it
([hero-sub](components/crops/hero-sub-default.png)), then the two address
gates as white pills on `elevation-2` shadows — `Sign in for saved
address` ([address-pill](components/crops/address-pill-default.png), a
sign-in gate, never pressed) and `Use current Location`
([location-pill](components/crops/location-pill-default.png), a
geolocation prompt, never pressed). Food photography frames the edges;
the layout is symmetric about the headline.

## The value props and CTA bands

Below the hero the page is a rail of recruitment cards and tinted CTA
sections ([home-light-full](screenshots/home-light-full.png)). Three
`value-prop-card`s sit side by side
([value-prop-card](components/crops/value-prop-card-default.png), 360 x
410): a blue-tinted blob illustration, a bold heading ("Become a
Dasher"), a copy line and a red text CTA
([card-cta](components/crops/card-cta-default.png)). Mid-page
`CTASplash` bands ([cta-band](components/crops/cta-band-default.png),
1440 x 600) alternate white and subdued tints (`#fdf0ed` pink,
`#f0f8ff`-family blues): a left-aligned title
([cta-band-title](components/crops/cta-band-title-default.png)), copy
([cta-band-copy](components/crops/cta-band-copy-default.png)) and the
red primary pill ([cta-btn](components/crops/cta-btn-default.png),
40px high, radius-full, #eb1700). One band is a full-bleed grocery
photograph with the copy on it. The grammar repeats for Dashers
("Sign up to dash and get paid") and merchants ("Grow your business
with DoorDash").

## The SEO directory

Every directory surface ends in the tabbed link section "Get more from
your neighborhood" ([home-light-cuisines](screenshots/home-light-cuisines.png)):
a centred h2 ([section-title](components/crops/section-title-default.png)),
three tabs — Top Cities / Top Cuisines / Top Chains — where the selected
tab carries a 3px `border.selected` ink underline
([tab-selected](components/crops/tab-selected-default.png)) and idle
tabs sit grey ([tab-idle](components/crops/tab-idle-default.png)).
Under the tab bar, columns of city/cuisine links
([dir-link](components/crops/dir-link-default.png)) and a `See more`
reveal ([show-more](components/crops/show-more-default.png)). The
same directory grammar fills /food-delivery/ (country pills, "Popular
Cities" columns — [food-delivery-light-default](screenshots/food-delivery-light-default.png))
and the /en-US/business/ alphabetical merchant index
([business-light-default](screenshots/business-light-default.png)).
The promos page wraps the same directory under a teal hero carrying
the address-search gate ([address-field](components/crops/address-field-default.png),
408 x 56 — focused for measurement, never filled or submitted;
[promos-light-default](screenshots/promos-light-default.png)).

## The restaurant directory

/en-US/restaurants-near-me/
([restaurants-light-default](screenshots/restaurants-light-default.png))
centres a DD Norms h1 ("Discover the Best Restaurants Near Me"), a
subhead and the full-width red `Sign in to order` gate
([nearby-cta](components/crops/nearby-cta-default.png), 759 x 40 —
measured, never pressed) with a `Search nearby` text link under it.
The cards run three-up: each `rest-card`
([rest-card](components/crops/rest-card-default.png), 448 x 274) is a
/store/… anchor holding a rounded photo, the name
([rest-card-title](components/crops/rest-card-title-default.png)) and
the `4.8 (6k+) • 0.7 mi • 21 min` rating/ETA line
([rest-card-sub](components/crops/rest-card-sub-default.png)), plus
promo chips — an offer badge ([offer-badge](components/crops/offer-badge-default.png))
and a "Top 10%" leaderboard badge
([leaderboard-badge](components/crops/leaderboard-badge-default.png)) —
and a `Popular Items` disclosure
([popular-btn](components/crops/popular-btn-default.png)). The list
pages through a paginated carousel
([pagination](components/crops/pagination-default.png)) and ends in an
SEO FAQ accordion ([faq-block](components/crops/faq-block-default.png))
and internal-link columns ([internal-link](components/crops/internal-link-default.png)).

## The storefront

/en-US/store/… ([store-light-default](screenshots/store-light-default.png))
is the real consumer shell read-only: the sticky `Header`
([app-header](components/crops/app-header-default.png), 1440 x 64)
with the red wordmark ([app-logo](components/crops/app-logo-default.png)),
a `Search DoorDash` field, the "Your Address" gate
([address-btn](components/crops/address-btn-default.png), never pressed),
the Delivery/Pickup segmented toggle and the cart icon button with its
red badge ([cart-btn](components/crops/cart-btn-default.png)) and bell
([bell-btn](components/crops/bell-btn-default.png)). The left rail is
the icon side-nav ([sidenav-toggle](components/crops/sidenav-toggle-default.png),
Home / Grocery / Retail / Convenience / Browse All above `Sign up or
Login`). The store header puts the cover photo under a breadcrumb
([breadcrumb](components/crops/breadcrumb-default.png)), the circular
store avatar, the h1 ([store-name](components/crops/store-name-default.png)),
the rating/award Store Info card with a `more` disclosure
([store-meta](components/crops/store-meta-default.png)), the
Delivery/Pickup toggle ([fulfil-toggle](components/crops/fulfil-toggle-default.png);
the toggled page is [store-light-pickup](screenshots/store-light-pickup.png))
and a `Group Order` action
([group-order](components/crops/group-order-default.png)). Menu items
tile in the virtualised grid ([menu-item](components/crops/menu-item-default.png),
450px rows at a 16px radius) each with the round red `+` quick-add
([quick-add](components/crops/quick-add-default.png), 32px — NEVER
pressed: a press starts a cart) beside the recommended carousel
([rec-section](components/crops/rec-section-default.png)). The cookie
banner was un-hidden for one reading and re-hidden, never answered
([cookie-banner](components/crops/cookie-banner-default.png)).

## The app-shell catalog pages

The HSA/FSA and seasonal catalog routes
([hsa-light-default](screenshots/hsa-light-default.png),
[seasonal-light-default](screenshots/seasonal-light-default.png)) render
the same consumer chrome — header, search, address pill, Delivery/Pickup,
cart, side-nav — with the catalogue body stuck on the product's loading
spinner: the archived page's client-side fetch hits live API endpoints
the archive cannot serve. That is the honest archived boundary: the shell
is real painted product, the body is a spinner. DashPass's student page
is the same shell plus the full footer
([dashpass-light-default](screenshots/dashpass-light-default.png)).

## The careers site

careersatdoordash.com ([careers-light-default](screenshots/careers-light-default.png))
is a WordPress/Tailwind stack, not prism: a `bg-pinot-noir`-family
header ([car-header](components/crops/car-header-default.png)) with the
nav links ([car-nav-link](components/crops/car-nav-link-default.png)),
a red `Search Jobs` pill ([car-btn](components/crops/car-btn-default.png)),
a team-photo hero, and the red `Careers` band with the condensed white
headline "BUILD BEYOND WHAT YOU THOUGHT POSSIBLE."
([car-h1](components/crops/car-h1-default.png)). It shares the brand
red and the wordmark but none of the prism tokens.

## The footer

The marketing footer ([footer](components/crops/footer-default.png),
1160 x 952) runs four link columns (Get to Know Us / Let Us Help You /
Doing Business / Do More) of quiet ink links
([footer-link](components/crops/footer-link-default.png)), the App
Store and Google Play badges
([appstore-badge](components/crops/appstore-badge-default.png)), a
language select ([language-select](components/crops/language-select-default.png))
and the social icon row
([social-btn](components/crops/social-btn-default.png)) above the legal
strip.

## Mobile

At 390 wide ([mobile-home-light-default](screenshots/mobile-home-light-default.png),
[mobile-home-light-full](screenshots/mobile-home-light-full.png)) the
hero keeps the same construction — Sign In/Sign Up pills top-right,
wordmark, condensed headline, the two address pills — with the value
cards stacked ([m-topbar](components/crops/m-topbar-default.png),
[m-identity-btn](components/crops/m-identity-btn-default.png),
[m-hero](components/crops/m-hero-default.png)). The storefront at 390
keeps the desktop side-nav shell
([mobile-store-light-default](screenshots/mobile-store-light-default.png)).
