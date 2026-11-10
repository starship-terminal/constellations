# Alo Yoga patterns

How the measured components combine on aloyoga.com's public surface, read
from the screenshots and the component entries in [components.md](components.md).
The shop paints one light theme; all values are from the light set unless noted.

## The shop chrome

A black promo strip ("JOIN TO SHOP", [promo-strip](components/crops/promo-strip-default.png))
sits above the 84px white header ([home-light-default](screenshots/home-light-default.png)):
lowercase `alo` wordmark, uppercase WOMEN/MEN/SHOES nav items (72×70 hit
areas, hover opens the mega-menu — [home-light-megamenu](screenshots/home-light-megamenu.png)),
then search, account and bag icons on the right. At 390px the bar compresses
to 57px and the links fold into a drawer opened by the hamburger
([mobile-home-light-menu](screenshots/mobile-home-light-menu.png),
[m-menu-open](components/crops/m-menu-open-opened.png)).

## Buttons and CTAs

Alo runs a two-button vocabulary: the filled black primary
(`--primary` #000, uppercase 13px tracking-wide) for Join now / Add to bag /
Sign in, and the hairline-outlined ghost for the sibling (Wishlist). Hero
buttons are 48px tall ([hero-button](components/crops/hero-button-default.png)),
the buy button a full-width 52px ([add-to-bag](components/crops/add-to-bag-default.png)),
size chips 40px ([size-button](components/crops/size-button-default.png)) with
the sold-out one struck through and tagged notify-me. Text links are the
quiet third option ("Size Guide", "Join Now", footer links).

## Product surfaces

Category discovery is tile-first: `a.image-grid__card` squares with a label
underlaid ([grid-card](components/crops/grid-card-default.png)). The shop grid
is `.PlpTile` cards — image, product name, price, a row of 26px colour dots
([swatch](components/crops/swatch-default.png), active gets the ring), an
"available in N colors" count and the "Join Now" member-price hook
([product-tile](components/crops/product-tile-default.png),
[shop-women-light-full](screenshots/shop-women-light-full.png)).

## Product page

The PDP puts the square 46px colour tiles first ([pdp-swatch](components/crops/pdp-swatch-default.png)),
then the 134×40 size chips — an out-of-stock chip is struck through — a "Size
Guide" trigger, and the stacked 52px pair: black ADD TO BAG above ghost ADD
TO WISHLIST ([wishlist-button](components/crops/wishlist-button-default.png),
[pdp-light-default](screenshots/pdp-light-default.png)). The PDP captured is
whichever product the grid listed first (`pdp_url` in
raw/components-computed.json).

## Forms

The public forms share one field: a 35px-tall hairline-bordered input
([email-input](components/crops/email-input-default.png) on the account gate,
the newsletter field in the footer). The login page stacks email + password +
full-width Sign in ([account-light-default](screenshots/account-light-default.png));
it was measured, typed into, and cleared — never submitted.

## Consent

The Osano consent manager paints a bottom drawer (Save / Accept All / Reject
Non-Essential) over every first-load page — captured as evidence
([home-light-consent](screenshots/home-light-consent.png)) then hidden for
all other captures. It is never answered.
