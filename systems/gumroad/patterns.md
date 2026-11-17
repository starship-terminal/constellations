# Gumroad patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## The hero header (light by default)

Every gumroad.com page opens with a bordered hero header — on Discover it measures 1440 x 217 (`nav-bar`, padding 32px 64px, a 1px black bottom border on the #f4f4f0 ground). Inside it: the GUMROAD wordmark link (`nav-logo`, 245 x 46.9, uppercased display type), a wide transparent "Search products" combobox (`nav-search`, 789 x 46, placeholder at 50% ink), the bordered "Log in" button (`nav-login`, 79 x 48) and the filled black "Start selling" CTA (`nav-start-selling`, 121 x 48) that lifts to the pink `--accent` with a hard 4px shadow on hover. A pill row of category links sits under the bar — plain links (`nav-category`) with the current one filled black (`nav-category-active`, "All"). The header is page-tall because it also carries each page's hero block.

## The bordered-section marketing pages

The landing, features, pricing and about pages are built from full-width bordered sections on the cream ground — each section divided by the same 1px black line, copy set in ABC Favorit. The landing hero centres a 96px display heading (`home-h1`, "Go from 0 to $1" at 96px/96 tracked -0.4px) over a bordered search box (`home-search` + `home-search-button`, black submit) that casts the `--box-shadow-1` hard offset. The page closes with a bordered email-capture form (`home-subscribe-form`, field `home-subscribe-input` plus its arrow submit) — measured, never submitted.

## The Discover grid

/discover layers a featured-products carousel over the market grid: the featured card (`discover-featured-card`, a large bordered showcase card with cover art) advanced by an unlabelled pair of 24px SVG pager arrows beside a "1 / 8" counter (`discover-pager-arrow`) — captured advanced as `discover-light-carousel`. The grid's own row of market tabs (`discover-tab`, `discover-tab-active` "Trending" filled black) sorts the cards; a "Tags" filters disclosure (`discover-filters`) opens checkbox rows (`discover-filter-checkbox`). Each product card (`discover-card`) is a bordered white card — cover image, title, star rating (`discover-card-rating`, 4.8) and a pink `--accent` price flag (`discover-card-price`, "SGD 171.34"). "Load more" (`discover-load-more`) appends rows; a currency select (`discover-currency-select`) re-prices the grid. The grid lazy-loads, so the full-page shot is bounded at eight chunks.

## The product page and checkout

A creator subdomain page (`ichigo.gumroad.com/l/ichigo-reader`) runs its own template on the shared sheet, with the creator's palette inlined on `:root` — this one paints white ground with a teal `--accent` #36a9ae and does not repaint under dark emulation. The layout is the product header (`product-header`) over a two-column body: description and ratings (`product-ratings`, `product-review-load` for more reviews) on one side, the purchase panel on the other — the tier card (`product-tier`, the "🍓💖🍰" tier at SGD 11.58/month), a native billing-term select (`product-term-select`, Monthly/Yearly), the "Subscribe" buy link (`product-buy`), "Add to wishlist" (`product-wishlist`) and the Share button (`product-share`) whose popover was captured open (`product-light-share`). A "Powered by Gumroad" footer (`product-footer`) closes it, currency select included.

The Subscribe link leads to the public checkout (gumroad.com/checkout with the product's option key): the order summary card (`checkout-summary`, qty and tier with Edit), a "Give as a gift?" switch (`checkout-gift-toggle`), then the fields — email (`checkout-email`), full name (`checkout-name`), country and currency selects (`checkout-country`, `checkout-currency`) — and the pay row (`checkout-pay`, PayPal shown). Everything was measured empty; nothing was filled or submitted.

## The auth card

/login and /signup centre a bordered card (`login-card`) on the ground: OAuth buttons (`login-oauth` — Apple, Google, X, Stripe), a divider, the 48px email (`login-email`) and password (`login-password`) fields on `--form-element-height`, the "Login" submit (`login-submit`) and the "Forgot your password?" link (`login-forgot`). The card was measured at rest and in dark; no credential was ever entered.

## Mobile (390px)

The phone surface keeps the cream ground and hard borders: the mobile header (`m-nav-bar`) shows the wordmark, the "Discover digital products from independent creators" strap and a menu button (`m-nav-menu-button`) that opens the nav panel — captured open as `mobile-home-light-menu`. Product cards flow full-width (`m-discover-card`, "THE ARCTIC MATRIX" at 390).

## Motion and focus

Transitions run the declared `--transition-duration` 150ms (`duration.default`) on `--default-transition-timing-function` (cubic-bezier(0.4, 0, 0.2, 1) — `ease.default`), with hover states animating `transform`/`translate`/`scale`/`rotate` — buttons and cards jump 4px on hover (`--button-hover-offset`) and pick up the hard shadow. The marquee loops are `motion-safe:`-gated: under prefers-reduced-motion the probe recorded 3 of 185 moving elements removed (`raw/motion.json`, behaviour "partial" — the `motion-reduce:transition-none`/`animate-none` utilities exist but most transitions keep running). Focus is a 1px auto outline in near-black (`focus.outline` — the accent-pink `rgb(255 144 232)` ring declared at 2px for fields).

## Theme architecture

The site declares `color-scheme: light dark` and repaints through `@media (prefers-color-scheme: dark)` — no in-page toggle, so OS-level emulation is the product's own theme control. `light` is the painted default: `--body-bg` #f4f4f0, `--color` #000, `--filled` #fff, borders at `--border-alpha` 1. The dark media block repaints `--body-bg` #242423, `--color` #ddd, `--filled` #000, `--border-alpha` 0.35 — the accent and status colours hold unchanged, so dark keeps the same pink on darker ground. Product and creator pages inline a light `:root` block over the shared sheet and never repaint: `product-light`/`product-dark` profiles in `raw/css-vars.json` document the pin, and no dark shots exist for them.

## The boundary beyond the signed-out surface

This package documents the public marketplace, not the product behind login. The seller dashboard (products, sales, payouts, analytics), the buyer library and account settings stayed signed out; the checkout stopped at the empty public form — no payment, account or post-purchase surface is claimed. The login/signup cards are evidence of the auth boundary's shape, nothing more.
