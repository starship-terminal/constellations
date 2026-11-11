# ASOS patterns

How the measured components combine on asos.com's public surface, read from
the screenshots and the component entries in [components.md](components.md).
The site paints one light theme; all values are from the light set unless noted.

## The shop chrome

A 30px top strip carries the deep-navy "Download our new app" button, Help &
FAQs and the "You're in Singapore" country picker
([app-strip](components/crops/app-strip-default.png),
[country-link](components/crops/country-link-default.png)). Under it sits the
140px black header block ([header](components/crops/header-default.png),
[home-light-default](screenshots/home-light-default.png)): lowercase `asos`
wordmark, the WOMEN/MEN floor tabs (60px, the active one underlined white),
a wide 38px white search field with an inline round button, and the account,
saved and bag icons on 50×60 targets. The 50px category nav row below
([nav-item](components/crops/nav-item-default.png)) is `display:none` on the
home page and appears everywhere else; hovering a button fills it deep navy
`#051a6e` and opens a ~1302px white flyout
([nav-flyout](components/crops/nav-flyout-default.png)). A black promo strip
with bordered WOMEN/MEN tabs ([promo-tab](components/crops/promo-tab-default.png))
carries the new-customer offer under the nav on every page. At 390px the
chrome compresses to a 50px bar: burger, wordmark, and search/account/saved/
bag icons ([m-header](components/crops/m-header-default.png)).

## Buttons and CTAs

ASOS's buttons are flat and square (0px radius, no shadows): white hero
buttons on imagery ([hero-cta](components/crops/hero-cta-default.png),
184×44, hover inverts to black), the `#018849` green buy button
([add-to-bag](components/crops/add-to-bag-default.png), hover `#006637`),
the ink `#2d2d2d` CONTINUE on the account gate
([continue-button](components/crops/continue-button-default.png), 48px,
hover black), and hairline-outlined ghosts (LOAD MORE
[load-more](components/crops/load-more-default.png), 54.5px; VIEW ALL
REVIEWS [reviews-cta](components/crops/reviews-cta-default.png), 44px).
Icon-only buttons go fully round: the 44px save heart
([save-button](components/crops/save-button-default.png)) and the 38px
search button. Keyboard focus draws a `#005fcc` ring, 1–5px depending on
the surface (`#0770cf` on my.asos.com). Text links stay default-anchor
`#0000ee`.

## Product surfaces

The category row on the grid is a carousel of 36px bordered pills
([cat-pill](components/crops/cat-pill-default.png)); sort and filter are
43px bar buttons ([sort-button](components/crops/sort-button-default.png),
[filter-button](components/crops/filter-button-default.png)) beside a quiet
"N styles found" count. Tiles are borderless
([product-tile](components/crops/product-tile-default.png), ~335×559, four
across at 1440): photography, a round save heart, name, price, and SELLING
FAST / MORE COLOURS status lines
([shop-women-light-default](screenshots/shop-women-light-default.png)).
Home and hub pages sell through full-bleed image tiles
([grid-tile](components/crops/grid-tile-default.png),
[hub-tile](components/crops/hub-tile-default.png)) — dark campaign cards
like "NEW HERE?" — and product rails
([hub-card](components/crops/hub-card-default.png)).

## Product page

The PDP keeps the buying column tight ([pdp-light-default](screenshots/pdp-light-default.png)):
title, price, a star-rating button, the light-blue `#cde2f5` promo band
([promo-banner](components/crops/promo-banner-default.png)), a COLOUR label,
a "Find your Fit Assistant size" link, and the native 38px size select
([size-select](components/crops/size-select-default.png)). The 44px pair —
green ADD TO BAG plus the round save heart — sits under it, then delivery
links and square 44px accordion rows (Size & Fit, Product Details…) that
toggle open ([pdp-accordion](components/crops/pdp-accordion-default.png),
[pdp-accordion-open](components/crops/pdp-accordion-open-opened.png)). The
gallery runs chevrons and a VIDEO button
([gallery-chevron](components/crops/gallery-chevron-default.png)); a
might-like rail and a reviews section close the page. The PDP captured is
whichever product the grid listed first (`pdp_url` in
raw/components-computed.json).

## Forms

The shop's fields are 38px bordered inputs ([search-input](components/crops/search-input-focused.png),
[size-select](components/crops/size-select-focused.png)); the my.asos.com
gate runs a taller variant — 44px email, 48px ink CONTINUE, 52px round
social buttons ([email-input](components/crops/email-input-default.png),
[social-button](components/crops/social-button-default.png),
[account-light-default](screenshots/account-light-default.png)). The gate
was measured, typed into, and cleared — never submitted.

## Mobile side panel

The burger opens a dark side panel ([mobile-home-light-menu](screenshots/mobile-home-light-menu.png)):
WOMEN/MEN tabs on top ([m-floor-tab](components/crops/m-floor-tab-default.png)),
a blue HOME row, then ~96px image rows for each category
([m-nav-link](components/crops/m-nav-link-default.png)) — uppercase tracked
labels over product photography.

## Consent

OneTrust paints a consent dialog over the first page load — captured as
evidence ([home-light-consent](screenshots/home-light-consent.png)) then
hidden for every other capture. It is never answered.
