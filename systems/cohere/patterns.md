# Cohere patterns

How the measured components compose cohere.com's public surfaces — the Next.js/Tailwind v3/Sanity marketing site and the dashboard.cohere.com login boundary. Values are tokens from [tokens.json](tokens.json); every number was measured ([raw/measurements.md](raw/measurements.md)) unless it names a declared utility from [raw/css-vars.json](raw/css-vars.json).

## The promo banner and header

Above the nav sits a dismissible pureBlack banner (`promo-banner`, 1440 x 48, `light.surface.banner`): white 16px text (`light.text.banner`) and a close button (`banner-close`, measured through a hover `rotate-90` — a local dismiss that only hides the strip). Below it the nav bar (`header`, 1440 x 60) holds the wordmark (`logo`, 118 x 24), flat nav links (`nav-item`, ~81 x 32, 14px pureBlack = `light.text.nav`, `0.2s` ease-in-out), a "Sign in" link (`nav-signin`, 42 x 32 — a link out to `dashboard.cohere.com`, never followed) and the nav CTA (`nav-cta`, 139 x 36). Focus on nav controls draws a `1px auto #101010` outline (`light.focus`).

## The gradient pill CTAs

One control language across the site: `radius.full` 9999px pills, 53.2px tall at the 18px label size (`nav-cta` is the 36px-tall compact variant). **Dark** (`cta-dark`, `nav-cta`): `neutral-15` `#17171c` fill (`light.accent`) → pureBlack on hover, white text (`light.text.onAccent`), focus swaps a transparent 2px border to `neutral-95` (`light.focusAlt`). **Light** (`cta-light`, `hero-cta`, `footer-cta`, `north-cta`, `command-cta`): white fill, `#17171c` text — the product-page heroes pair the white pill with their dark bands. Every pill carries the `ease-button-gradient` `::before` layer — a 270deg `quartz-500 #d18ee2 → coral-500 #ff7759` sweep (`core.gradient.cta`) revealed through a sliding mask — and swaps `background-color,color` in `0.3s ease` (`motion.duration.measuredControl`, `motion.curve.button`). `cta-dark`'s own hover state is uncaptured (the hover animation re-renders the node mid-measure; recorded as an error state) but the identical swap is measured on `nav-cta`.

## The hero and home

The home hero is light: `hero-title` (1128 x 192) sets 96px CohereText (`font.family.displayMeasured`, `font.size.hero`) in volcanic-900 `#212121` (`light.text.primary`) over the pureWhite ground (`light.surface.page`), with the light `hero-cta` pill (152 x 53.2). Below: the customer logo marquee (`marquee-logo`, 148 x 52 tiles) and content sections built on `callout-card` (437 x 493, `radius.card` 22px) whose painted child carries the `#f0eee9` marble fill (`light.surface.raised`). `page-ground` records the whole page at 1440 x 8680.

## Pricing and FAQ

`/pricing` opens with the 72px headline (`pricing-title`, `font.size.h1Pricing`, volcanic-900). The rate table rows carry 18px figures (`price-rate`, 46 x 21) under a two-state tab control (`price-tab` on / `price-tab-off`, ~160 x 34, 16px, 0.15s ease-in-out) — measured in both states without switching the tab. Below, the FAQ accordion rows (`faq-item`, 660 x 61, 18px volcanic-900 on transparent) expand locally; `faq-item-open` records the opened state of the first row.

## The product page heroes

`/north` and `/command` open on **dark hero islands** inside the light theme: `north-title` (1128 x 144) and `command-title` (1128 x 216) set white 72px CohereText over the dark band, with the light `north-cta` (146 x 53.2) and `command-cta` (185 x 53.2) pills below.

## The footer bands

The footer (`footer`, 1440 x 1430) is two stacked islands. First the **green CTA band** (`light.surface.band` `#355146`): white 60px "Ready to put AI to work?" (`section-title`, 675 x 60) and the light `footer-cta` pill (185 x 53.2). Then the **dark band** (`light.surface.dark` `neutral-15 #17171c`): link columns whose rows separate on 1px `#525260` borders (`light.border.onDark`) with `neutral-95 #fafafa` 14px links (`footer-link` = `light.text.onDark`), 24 x 24 social icons (`footer-social`), and — painted just above the `<footer>` element, captured page-wide — the SOC2/GDPR/ISO certification anchors (`footer-badge`, 120 x 140).

## The sign-in card (boundary)

`dashboard.cohere.com/welcome/login` measured at rest: `signin-card` (566 x 235) holds the OAuth rows (`signin-oauth`, 281 x 40, `radius 4px`, 1px `#dadce0` = `light.border.subtle`, white fill, `#616161` 1px focus outline = `light.focusOnDark`), the email field (`signin-field`, 566 x 60, 1px `#bdbdbd` = `light.border.input`, measured `focused` only — nothing typed) and the Log-in button (`signin-submit`, 130 x 40) whose painted child spans carry the `#39594d` green fill. No credentials were entered and nothing was submitted or followed.

## The mobile pass

At 390 x 844 the desktop nav unmounts and `m-header` (390 x 60) takes over with the `m-menu-button` hamburger (32 x 32). Its own press opens the menu overlay (`m-menu-open`, 390 x 683): a white panel with 358 x 44 link rows (`m-menu-link`, 24px, `0.5s` clip-path transition, an `#e59700` amber focus outline), over the `.bg-black/20` scrim (`light.overlay.scrim` — volcanic-900 at 20%). The mobile hero (`m-hero`, 358 x 120) drops to 60px.
