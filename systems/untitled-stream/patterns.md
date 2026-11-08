# untitled.stream patterns

How the measured components combine into the marketing site's screens. Every value named here is a token in [tokens.json](tokens.json); the component entries are in [components.md](components.md) and the screens in [screenshots/](screenshots).

## Site chrome

Every marketing page hangs from a transparent top band with no wordmark (on home) or a small 112 px wordmark (on pricing): `body-semibold` nav links in `text.primary`, a `[membership]` link, and the one painted element — the `component.button.primary` black-gradient Enter App pill at 44 px, fully rounded. The header is a fixed `component.header` (88 px measured under a 152 px `layout.header-height` reservation) over `background.page` white.

- Desktop: [home-light-default](screenshots/home-light-default.png), [pricing-light-default](screenshots/pricing-light-default.png)
- Mobile: [mobile-home-light-default](screenshots/mobile-home-light-default.png) — no nav links render at 390 px; the header is tagline plus nothing

## Hero and the disc strip

The home hero is a centred `typography.super-title` statement ("A sacred place for your work-in-progress music") over the signature artwork: a horizontally overflowing strip of iridescent CD renders — `div.rounded-full` elements with webp `background-image`s, not image tags — nominally `component.disc` size 656 px on `background.shading` underlay (the strip animates them, so individual renders measure anywhere ~650–790 px). The discs are the only saturated colour on the page.

- [home-light-default](screenshots/home-light-default.png), [home-light-full](screenshots/home-light-full.png)
- [disc](components/crops/disc-default.png), [disc-carousel](components/crops/disc-carousel-default.png)

## Bottom pill bar

Home pins a frosted `component.pill-bar` (92 px) to the viewport bottom: `component.pill-bar.pill-bg` pills at 44 px for socials (Texting, Interviews, IG, X), the inverted We're hiring pill (`background.action` gradient + `text.on-action`), a Learn more control, and the iOS/Android/macOS platform pills with `text.primary` glyphs. It scrolls with nothing and blurs over content via `blur.*`.

- [home-light-default](screenshots/home-light-default.png)
- [pill-bar](components/crops/pill-bar-default.png), [hiring-cta](components/crops/hiring-cta-default.png)

## Feature sections

Below the strip, the page alternates `typography.title` section heads with `feature-video` panels (muted `background.surface` rounds playing UI loops) and `read-more`/`learn-more` subhead controls in `untitled-blue`. The footer closes with a `footnote` legal row and a cookie-settings control that re-mounts the consent card.

- [home-light-full](screenshots/home-light-full.png)
- [feature-video](components/crops/feature-video-default.png)

## Pricing rail and plan cards

Pricing is a two-part composition: a left `billing-toggle` rail (a full-height 122 x 536 column holding the Yearly/Monthly segment pills at `component.billing-toggle.option-height` 44 px; the held segment washes `component.billing-toggle.selected-bg` at `component.billing-toggle.selected-radius` 20 px) beside `component.plan-card` cards — `background.surface-raised` (#eee) rounds at `component.plan-card.radius` 20 px, 350 x 536, headed by bracketed names `[starter]`/`[membership]`, the price, and feature rows. The toggle is a local state swap; nothing submits.

- [pricing-light-default](screenshots/pricing-light-default.png), [pricing-light-full](screenshots/pricing-light-full.png)
- [billing-toggle](components/crops/billing-toggle-default.png), [plan-card-paid](components/crops/plan-card-paid-default.png), [billing-toggle-monthly](components/crops/billing-toggle-monthly-selected.png)

## Consent card

On first load a `dialog-scrim` mounts the "We value privacy" card — `component.consent-card` (500 px, 16 px radius, `surface-frost` 90% over white text) with pill buttons: Reject all (`consent-reject` 5% white fill), Customise, Accept all (`consent-accept` white fill, black text). It is the only dark-painted element on the light site. Its buttons are measured but intentionally never pressed — the consent endpoint 403s this client (see README, What to distrust), so page shots hide the card instead.

- [consent-card](components/crops/consent-card-default.png), [consent-button-reject](components/crops/consent-button-reject-default.png)

## Trust page

A text page: `super-title` title, `title` section heads, a `subhead` list, and an `untitled-blue` outbound link to Cloudflare. The whole page is typography plus `text.secondary` copy — no cards.

- [trust-light-default](screenshots/trust-light-default.png), [trust-light-full](screenshots/trust-light-full.png)

## Login card

`/login` centres a `component.login-card` (342 px controls): the 189 px Untitled mark, a `typography.title` "Log in to untitled", then three full-width pill controls at `login-card.oauth-height` 52 px — Continue with Google, Continue with Apple, Continue with phone — over `footnote` legal links. The card was measured and screenshotted; the controls were never activated and no credential was entered. Everything past it — the onboarding disc picker, the workspace — is uncaptured; the `dark` token set holds the app's declared palette only.

- [login-light-default](screenshots/login-light-default.png), [login-light-full](screenshots/login-light-full.png)
- [login-card](components/crops/login-card-default.png), [login-oauth-google](components/crops/login-oauth-google-default.png)
