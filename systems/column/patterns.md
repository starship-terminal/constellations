# Column patterns

How the measured components compose column.com's public surfaces — the Gatsby/styled-components marketing site and the dashboard.column.com login boundary. Values are tokens from [tokens.json](tokens.json); every number was measured ([raw/measurements.md](raw/measurements.md)) unless it names a declared custom property from [raw/css-vars.json](raw/css-vars.json).

## The launch banner and header

Above the nav sits the launch banner (`promo-banner`, 1440 x 40): white 16px text (`light.text.banner`) over a 90deg blue-violet gradient — `#3e5199 → #5568ad` (`core.gradient.banner`, `light.surface.banner` reads its first stop). Below it the site header (`header`, 1440 x 62) holds the wordmark (`logo`, 86 x 19), the mega-menu triggers (`nav-item`, 111 x 37 — "Products"/"Developers", 14px `light.text.nav` = gray-900 `#12161e`), the "Sign in" link (`nav-ghost`, 77 x 38 — out to `dashboard.column.com`, never followed) and the nav CTA (`nav-cta`, 127 x 36): a white-50%-fill pill with `text.color` `#232730` (the declared `--btn-text-color-secondary`), radius 8px and a `rgba(87,90,100,0.12)` ring hairline; hover fills it solid white.

## The navy CTA language

The declared `--btn-*` set is the control contract: primary buttons paint `--btn-bg-primary` = blue-800 `#111a4a` (`light.accent`) with `--btn-text-color-primary` white (`light.text.onAccent`) and a `--btn-focus-ring-primary` blue-100 `#d4e3f7` ring (`light.focus`); hover/active hold the same navy per the declared `--btn-bg-primary-hover`/`-active`. The nav's painted CTA is subtler — the white-50% "Get started" pill above — and the navy "Sign up" choice inside its GetStartedMenu dropdown renders eager but `visibility:hidden`, so it is documented, not measured.

## The hero and home

The home hero is light: `hero-title` (486 x 114) sets **52px SuisseIntl semibold** (`font.size.hero`, `font.family.sans`, tracking −0.03em) in blue-800 navy over the white ground (`light.surface.card`), with `hero-cta` (98 x 36) below. The stats row tiles (`stat-figure`, 253 x 57 — "$4.5T+ annual transaction volume") lead into the dark band.

## The dark infrastructure band

`dark-band` (1416 x 3242) is the dark island inside the light theme: cyan-900 `#011821` fill (`light.surface.darkBand`, the `color-palette-inverted` binding), with the 48px heading "Flexible building blocks built on USD" (`dark-title`, 427 x 106) in `light.text.onDark` = cyan-200. Below it the 60px display heading (`section-title`, 1072 x 60 — "Start building today") closes the page.

## The product pages and their UI mocks

`/ach` opens with the 56px product headline (`ach-title`, 536 x 120), then `section-box` content cards (1280 x 443, radius 16, white-60% fill) and `product-screen` — a 430 x 531 rendered app frame inside the marketing page; measured as a frame, not claimed as the app. `/card-programs` mirrors it: `cards-title` (625 x 120) and the `cards-cta` button (139 x 36).

## The footer closer

`footer` (1416 x 1074) is a light-grey closer — gray-100 `#eeeff2` fill with a 1px `#e3e4e8` border and 12px radius — holding link columns, the logo block (`footer-logo`, 125 x 29) and the closer card links (`footer-link`, 344 x 209: the "Documentation"/"Get started" tiles, white-25% fill behind a 1px white ring).

## The sign-in form (boundary)

`dashboard.column.com/login` is a separate app surface on gray-50 `#f6f6f8`: `signin-card` (280 x 112) holds the email field (`signin-field`, 248 x 16 — the visible input inside a 280 x 40 label wrapper that carries the `--form-input-border` ring styling; measured `focused` only, nothing typed), the "Sign in"/"Continue" submit (`signin-submit`, 280 x 32, navy fill) and the "Sign in with a passkey" row (`signin-passkey`, 280 x 32). No credentials were entered and nothing was submitted or followed.

## The mobile pass

At 390 x 844 the header collapses to `m-header` (390 x 45) under the launch banner, with the `m-menu-button` hamburger (16 x 18). Its own press opens the overlay (`m-menu-open`, 390 x 799): 342 x 42 link rows (`m-menu-link`). The mobile hero (`m-hero`, 360 x 70) drops the headline to 32px.
