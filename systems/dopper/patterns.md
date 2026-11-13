# Dopper patterns

How the measured components combine on www.dopper.com and
shop.dopper.com's public signed-out surfaces, read from the screenshots
and the component entries in [components.md](components.md). The surface
paints light only; the darkBlue mobile menu and the deep-sea/darkBlue
bands are brand-painted surfaces, not a theme. Prices render `EUR`.

## The chrome: white header, shadow-DOM nav, yellow flyout

Every desktop page opens on a 110px white header
([header](components/crops/header-default.png)): the `dopper.` wordmark
([logo](components/crops/logo-default.png), 200 x 47), flyout triggers
`Bottle` / `Travel Mug` / `Tap` / `Mission` / `Get Involved`
([nav-trigger](components/crops/nav-trigger-default.png)), plain links
(Impact report, Find a Store, For Businesses, EN — [nav-link](components/crops/nav-link-default.png))
and the bag button ([bag-button](components/crops/bag-button-default.png),
60 x 62). The whole nav lives inside `dopper-navigation`'s shadow root —
the custom element's box is 0x0 while its children carry the layout; on
shop.dopper.com the same chrome repaints above a catalog nav row
([shop-nav](components/crops/shop-nav-default.png), 1360 x 27).

The `Bottle` trigger opens a full-viewport `#fed200` yellow mega-menu — see
[home-light-menu](screenshots/home-light-menu.png): Travel Mug / Bottle /
Tap / Map / Community tabs over feature columns, "Buy a bottle" and
"Customise 60+ bottles" CTAs and a product photo. The `flyout`,
`flyout-tab` and `flyout-card` measurements are misidentified — they read
the static "Explore our solutions" section, which carries the same card
copy (their entries are marked missing in [components.md](components.md);
a re-measure is queued). The menu closes on blur.

## The hero and the home story

Home opens on a full-bleed video hero: "Whatever the season" in the
Dopper display face ([hero-display](components/crops/hero-display-default.png),
425 x 144 white over footage) with two pills — `Watch now` in deep-sea
([btn-dark](components/crops/btn-dark-default.png), 174 x 51) and
`Shop our collection` outlined ([btn-outline](components/crops/btn-outline-default.png),
245 x 51). Below: the collections tab showcase
([collection-tab](components/crops/collection-tab-default.png), 250 x 445 cards
under a 1324 x 58 heading), the impact calculator, content cards
([content-card](components/crops/content-card-default.png), 787 x 597)
and the sand footer with the newsletter band
([footer](components/crops/footer-default.png), 1440 x 737; fields
[newsletter-input](components/crops/newsletter-input-default.png), 400 x 54).

## The shop: catalog nav, filters, product grid

shop.dopper.com (Magento 2, `Dopper/dopper_b2c`) adds a 27px catalog nav
row and hero tiles with 173 x 54 darkBlue CTAs
([shop-hero-button](components/crops/shop-hero-button-default.png)). On /bottles a
259 x 80 centred "Bottles" title ([plp-h1](components/crops/plp-h1-default.png))
sits above the teal `+ Filters` pill
([filters-button](components/crops/filters-button-default.png), 156 x 52)
and — open on desktop — a 1360 x 348 light-blue filter sheet
([filter-panel](components/crops/filter-panel-default.png)) of custom
radio rows ([filter-radio](components/crops/filter-radio-default.png)),
colour swatches ([filter-swatch](components/crops/filter-swatch-default.png),
155 x 129), checkbox rows ([filter-checkbox](components/crops/filter-checkbox-default.png))
and a 54px close ([filter-close](components/crops/filter-close-default.png)).
Product cards ([product-card](components/crops/product-card-default.png),
340 x 656) carry badge chips, names and EUR prices
([product-price](components/crops/product-price-default.png)).

## The product page configurator

/dopper-original-pacific-blue lays breadcrumb
([breadcrumb](components/crops/breadcrumb-default.png)), gallery,
415px title/price column and option rows — `Choose collection`,
`Select your pattern`, `Accessories`
([pdp-option](components/crops/pdp-option-default.png), 107 x 25, links
to filtered views — measured at rest) — above the 203 x 54 darkBlue
`Add to cart` ([add-to-cart](components/crops/add-to-cart-default.png),
default/hover/focus/pressed captured; never really clicked) and icon
feature rows ([pdp-feature](components/crops/pdp-feature-default.png)).

## Cart and login: the Magento pair

The empty cart centres a "Your cart" display
([cart-title](components/crops/cart-title-default.png)) over a 1440 x 93
darkBlue-3 continue-shopping strip ([cart-strip](components/crops/cart-strip-default.png))
with a 202 x 54 `Back to shop` CTA
([cart-cta](components/crops/cart-cta-default.png)). The login page pairs
a darkBlue "Registered Customers" card
([login-card](components/crops/login-card-default.png), 534 x 489:
[email](components/crops/login-email-default.png) and
[password](components/crops/login-password-default.png) fields at 54px,
a 56px Sign in, Remember Me,
[Forgot link](components/crops/login-link-default.png)) beside a
light-blue "New Customers" card ([new-card](components/crops/new-card-default.png))
with a 257 x 56 `Create an Account`. Fields were typed into and cleared —
nothing sent.

## Mobile (390 wide)

At phone width the header shrinks to wordmark + sand burger
([m-header](components/crops/m-header-default.png), 390 x 125;
[m-burger](components/crops/m-burger-default.png), 45 x 45) which opens
a 390 x 844 darkBlue full-screen menu
([m-menu-open](components/crops/m-menu-open-default.png)) of nav rows
([m-nav-item](components/crops/m-nav-item-default.png)) and pills
([m-menu-pill](components/crops/m-menu-pill-default.png), 195 x 54).
The PLP filters open as a full sheet; the hero display drops to
390 x 106. See [mobile-home-light-menu](screenshots/mobile-home-light-menu.png)
and [mobile-category-light-filter](screenshots/mobile-category-light-filter.png).

## The state signature

- **Buttons** are 54–56px darkBlue/deep-sea/white pills; pressed states
  were CDP-forced where shadow DOM allows.
- **Focus** paints real outlines — the measured focus rings per control
  are in [components.md](components.md)'s Shared values.
- **Hovers** shift fills along the declared tints (darkBlue →
  darkBlue-1, etc.) rather than inventing new hues.
- **Radius** language: the declared 4/8/16/20px scale — pills, CTAs,
  cards, fields and chips all measure the 20px step; only the colour
  swatches (100%) and icon circles go rounder.
