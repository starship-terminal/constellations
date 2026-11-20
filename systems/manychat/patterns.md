# ManyChat patterns

How the components in [components.md](components.md) combine on the public marketing pages. Values are in [tokens.json](tokens.json). Crops are in [components/crops/](components/crops). Page captures are in [screenshots/](screenshots).

## The chrome band

Home carries two rows. A 68px black Creator World strip (`promo-banner`, 1440 x 68) sits above a 92px nav (`header-nav`). The nav holds a 151 x 28 wordmark, Product / Solutions / Agencies as divs, Pricing as an anchor, an EN div, a 100 x 44 Log in pill, and a 137 x 44 Get started pill. On the home photo that pill is white. On pricing it is `#0f0f0f`. Labels are CoFo Sans Mono, 12px. Pricing has no promo strip, so the nav starts at the top.

## The hero

The home headline is ManyChatGravity at 72px (7.2rem against the 10px root), 692 x 118, "Social smarter, not harder." The hero Get started pill is 150 x 48, fill `#fa0cf7`, radius 999px. The Instagram product page repeats the same display size: "Your Instagram just got smarter", 590 x 118.

## Pricing

`/pricing` sets the heading in Rooftop at 36px / 600. Monthly and Annual are labels, not buttons. Annual is the selected side in the default shot: a black pill, white CoFo Sans Mono label, 51 x 20. The Free card is 369 x 662, white, 24px radius, 32px padding, a `$0` price and a 305 x 48 `#0f0f0f` Start for free pill. Checkout was not opened. Selecting Monthly is in [pricing-light-monthly](screenshots/pricing-light-monthly.png).

## Guides

`/resources/how-to` is a public guide index, heading ManyChatGravity at 80px. A guide card measured 368 x 372. This is not the in-app template library. The 2026-11-21 signed-in walk opened My Templates and found an empty state, recorded in [login-review.json](login-review.json). Creating a template was not submitted.

## The footer

The home footer is 1440 x 942. Column links are Rooftop 12px. About was measured and not followed.

## Phone

At phone width the nav drops to 60px and the hero heading to 44px (358 x 72). The Get started pill is 129 x 32. The painted hamburger was not a selectable control, so the drawer is not in this package. The home phone viewport measured innerWidth 392. The pricing phone viewport measured 390.
