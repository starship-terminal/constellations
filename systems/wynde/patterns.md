# Patterns

Public pages only. Screenshots are 256-colour PNGs. Read colours from [tokens.json](tokens.json).

## Home

A white page, a 64 px header, and a 1280 px column at the 1440 read (80 px inset). Header background `rgba(255, 255, 255, 0.95)`. Wordmark left. Features, Pricing, and Watch demo in the middle. Log in and Get started for free on the right. The map of which control opens which page is [site-tree.md](site-tree.md).

The hero is a `#edf1f5` panel, radius 24 px. Display type is Suisse Int'l Bold 68 px. The lede is Inter 18 px weight 500, `#505459`. Two pills sit under it.

![Home fold](screenshots/home-light-viewport.png)

Below the fold: a grey marquee line, method tiles, a green audience band (`#00604a`, radius 24 px, lime headline `#efffb7`), a savings comparison, a navy reports band (`#012b4b`, headline `#def0ff`), quotes on `#edf0f4`, a security block, and pricing.

![Home, full page, clipped at the document height](screenshots/home-light-default.png)

The product mock in the hero (cards, heatmaps, "Mastercard *5573") is an illustration, not the app.

## Pricing

Three white cards, radius 20 px, padding 24 px 20 px, 411 px wide at 1440. A 1 px `::after` border in `rgb(237, 240, 244)` draws the hairline. Start is Free. Team is $175 / mo in Suisse Int'l Medium 28 px, with an orange name. Enterprise says Talk to us, with a white Contact sales pill (200 by 48 px, radius 52 px, `::after` border `rgb(218, 223, 229)`) and a blue name `#00528d`. Contact sales has no href. The annual control was measured off. Plan buttons were not followed.

![Pricing](screenshots/home-light-pricing.png)

## Phone

At 390 px the desktop nav hides (`min-width: 1024 px` is the Framer breakpoint). The header is the wordmark and a 32 px menu button. Hero type drops to 44 px. The two pills go full width (294 px in the live read).

![Home at 390](screenshots/home-light-phone.png)

The open menu is a white fixed panel, 390 by 271. It lists Features, Pricing, Watch demo, a full-width Log in pill, and a full-width Get started pill. Close is an x in the header.

![Home menu at 390](screenshots/home-light-phone-menu.png)

## Legal

Terms and privacy are Inter. The title is 32 px weight 700, line-height 64 px. Body is 18 px, line-height 36 px. Last updated 16 Feb 2024. No form. The phone width of terms is captured too.

![Terms](screenshots/terms-light-default.png)

![Privacy](screenshots/privacy-light-default.png)

![Terms at 390](screenshots/terms-light-phone.png)

## Missing route

https://wynde.io/this-page-does-not-exist-wynde-9f3a is Framer's "Page not found" empty state, title "Page Not Found | Framer". It is not a Wynde layout. The headless PNG is white. That reading is not tokenised.

![Framer empty state](screenshots/not-found-framer.png)

## Login boundary

https://app.wynde.io redirects to https://app.wynde.io/login. The screen says "Sign in to Wynde", has an empty email field (placeholder "Enter your email here"), a blue Continue button (`rgb(0, 102, 255)`, pill, radius 9999 px, 32 px tall), and "Sign in with Google". Nothing was typed or pressed. `/signup` is not a form. It says "Failed to load data". Measurements are in [raw/login-boundary.json](raw/login-boundary.json). The empty wall is photographed.

![Login wall, empty](screenshots/login-light-default.png)
