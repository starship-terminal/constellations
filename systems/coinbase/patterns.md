# Coinbase patterns

How the measured components compose coinbase.com's public surfaces — the CDS/styled-components marketing site (Singapore locale, `/en-sg`) and the login.coinbase.com sign-in boundary. Values are tokens from [tokens.json](tokens.json); every number was measured ([raw/measurements.md](raw/measurements.md)) unless it names a declared variable from [raw/css-vars.json](raw/css-vars.json).

## The promo row and sticky nav

A light-grey promo row (`promo-banner`, 1425 x 40, `bgSecondary #eef0f3` = `light.surface.raised`) sits above the nav, centred 16px CoinbaseSans with a navy link (`light.text.banner`, indigo-90 `#11206b`). Below it the sticky white header (`header`, 1425 x 117, z-index 5) rides a 1px bottom hairline (`light.border.subtle` = `bgLine`, fgMuted at 20%). Inside: the Coinbase logo (`logo`, 44 x 44), flat nav links (`nav-item`, ~101 x 44, CoinbaseSans 16/20 600, `light.text.nav` = fg `#0a0b0d`, radius-1000 hit areas), the grey "Sign in" ghost pill (`nav-signin`, ~101 x 44, `bgSecondary` fill) and the blue "Sign up" pill (`nav-cta`, 106 x 44). Focus on links draws `1px auto #101010` (`light.focus`); buttons draw a 2px `bgPrimary` outline.

## The pill CTAs

One control language across the site: `borderRadius-1000` (100000px, `component.control.radiusCta` 56px) pills — 44px in the nav, 56px for page CTAs. **Blue**: `nav-cta` (106 x 44, `bgPrimary #0052ff` = `light.accent`, white `light.text.onAccent` text) whose hover deepens to `bgBrandHovered rgba(0,72,224,.88)` (`light.accentHover`). **Dark**: the hero's "Sign up with Singpass" (`hero-cta`, 257 x 56) and the "See more assets" (`cta-dark`, 208 x 56) — `bgInverse #0a0b0d` fill → `rgba(17,18,20,.88)` on hover, white text. **Ghost**: `nav-signin` and the sign-in OAuth rows (`signin-oauth`/`signin-passkey`, 400 x 58) — transparent fill inside a `bgLine` hairline border.

## The hero and the dark asset band

The home hero sets 80px/80 CoinbaseDisplay (`hero-title`, 657 x 240, fg `light.text.primary`) over the white ground (`light.surface.page` = gray-0), next to the product app-mock artwork. Further down, the **dark asset band** (`dark-band`, 657 x 640, `light.surface.dark` = gray-100 `#0a0b0d`) is a `.coinbase.dark` theme island inside the light page: a carousel card (`carousel-card`, 1425 x 724, `#141519` = dark bgElevation1) and filter chips (`chip`, 117 x 44, `#282b31` fill, radius 56px, white text = `light.text.onDark`). A dark "See more assets" pill (`cta-dark`) links out to `/explore`, never followed. The promo carousel section (`section-title`, 544 x 48, 44/48 CoinbaseDisplay) heads content sections.

## Explore — the price table

`/en-sg/explore` opens with a 28px CoinbaseDisplay title (`explore-title`, 195 x 36) and a `bgSecondary` search field (`explore-search`, 309 x 42 — measured `focused`, a `0.2s ease-in-out` background/box-shadow transition = `core.motion.duration.ui`). The market table (`price-table`, 1002 x 816) rules 76px rows (`price-row`) on hairline borders; hover/focus/pressed all paint the same `rgba(247,248,249,.35)` wash. Figures sit in 16px CoinbaseSans (`price-figure`, 91 x 24); the sort affordance is a 12px icon (`sort-icon`); change values carry the declared `fgPositive #098551` / `fgNegative #cf202f` roles.

## Coinbase One, Prime and the rest

`/en-sg/one` repeats the home recipe: an 80px CoinbaseDisplay hero (`one-title`, 657 x 240) with a **blue** "Get Coinbase One" pill (`one-cta`, 235 x 56). `/en-sg/prime` opens wider (`prime-title`, 1361 x 192) with a dark CTA (`prime-cta`, 166 x 56). The remaining routes (business, advanced-trade, developer-platform, usdc, learn, about, careers, blog, legal/privacy, and the 2026-11-21 tree pages) are captured as screenshots. Their components share the same CDS chrome. `/en-sg/agents` and `/derivatives` paint a dark page, not the light home surface. The control map is [site-tree.md](site-tree.md).

## The footer band

The footer (`footer`, 1425 x 1230) is a light `bgAlternate #eef0f3` band — not dark: link columns of `fgMuted` CoinbaseText 16/24 rows (`footer-link`, 49 x 24 = `light.text.muted`, focus `1px auto #101010`), 16 x 27 social icons (`footer-social`) and a "Singapore · English" region selector (`footer-region`, 202 x 26). `hr` rules paint `bgLine` between blocks.

## The sign-in card (boundary)

`login.coinbase.com/signin` measured at rest: a centred 400px column (`signin-card`, 400 x 146 content measure) holding "Sign in to Coinbase" (28/36 CoinbaseDisplay), the email field (`signin-field`, 398 x 56, white fill inside a `bgLineHeavy rgba(91,97,110,.66)` border = `light.border.input`, CoinbaseSans 16/24 — focused once for its computed style, never typed), the blue Continue pill (`signin-submit`, 400 x 56, `#1460ff`), an OR divider on `bgLine` rules, and three OAuth rows (`signin-passkey`/`signin-oauth`, 400 x 58, transparent fill, `bgLine` border, radius-1000). No credentials were entered, nothing submitted, no OAuth/passkey flow started.

## The mobile pass

At 390 x 844 the desktop nav unmounts and `m-header` (390 x 129 — promo row plus the logo/hamburger bar) takes over with the `m-menu-button` toggle (44 x 47). Its own press opens the menu overlay (`m-menu-open`, 390 x 715): a **white** panel (the mobile menu is light, not dark) with 382 x 56 link rows (`m-menu-link`, CoinbaseSans 24/28, an `#e59700` amber focus outline — CoinbaseIcons focus colour). The mobile hero (`m-hero`, 358 x 156) drops the headline to 52px CoinbaseDisplay.
