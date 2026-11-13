# Cartesia patterns

How the measured components combine on cartesia.ai's public surface, read
from the screenshots and the component entries in
[components.md](components.md). The package covers three signed-out
surfaces: the Astro/Tailwind marketing site (light, with `.dark` islands
declared), the Clerk sign-in/sign-up cards on play.cartesia.ai (the only
playground surface reachable signed out) and the Mintlify docs app on
docs.cartesia.ai. Values are from the light set unless marked `dark`.

## The chrome

Every marketing page carries the same sticky chrome
([header](components/crops/header-default.png), 1440 x 64) on the
`#fefefe` field with a `#ededed` boundary hairline underneath: the
wordmark ([logo](components/crops/logo-default.png), ~140 x 20), the
`Products` mega-menu trigger
([nav-trigger](components/crops/nav-trigger-default.png)), plain links at
36px high ([nav-link](components/crops/nav-link-default.png)) that hover
onto the `#f3f2ef` muted fill, then `Sign In`
([nav-signin](components/crops/nav-signin-default.png)), `Talk to Sales`
([nav-sales](components/crops/nav-sales-default.png)) and the verdant
`Try Cartesia` pill ([nav-cta](components/crops/nav-cta-default.png),
120 x 36, `--radius-lg` 8px, `#309d4b` — hovering at 90% of the fill).
An announcement banner
([banner](components/crops/banner-default.png), ~37px) can sit above it.
The Products trigger opens on click — not hover — into a 624 x 162 panel
([nav-dropdown](components/crops/nav-dropdown-default.png),
[home-light-menu](screenshots/home-light-menu.png)) of 6px-radius links
([menu-link](components/crops/menu-link-default.png), 197 x 65) over a
12px padding. Keyboard focus draws a 2px solid `#a1a1a1` (`--ring`)
outline.

## The home hero and the voice orb

The home page opens on a PP Kyoto display headline
([hero-title](components/crops/hero-title-default.png), `40px/46px`,
865 x 92) over the lede
([hero-lede](components/crops/hero-lede-default.png)) and the signature
demo: the Talk-to-Skylar orb
([hero-orb](components/crops/hero-orb-default.png), a 245px full-radius
circle) ringed by 59px voice-chooser buttons
([voice-choose](components/crops/voice-choose-default.png), accessible
labels `Choose <name>, <role>`) with 40px carousel arrows
([voice-nav](components/crops/voice-nav-default.png), `Next voice`).
The orb is a live-agent entry point — its call was never started.
Beside it sits the customer-story media tile
([media-frame](components/crops/media-frame-default.png),
[story-card](components/crops/story-card-default.png), 559px squares).

## Marketing sections

Sections head in a 26px display face
([h2-display](components/crops/h2-display-default.png), 559 x 68). The
product grid pairs 571 x 378 cards
([product-card](components/crops/product-card-default.png)) over
1182 x 54 product rows
([product-row](components/crops/product-row-default.png)); text CTAs
([cta-link](components/crops/cta-link-default.png)) carry the verdant
link colour. The deployment accordion runs 74px-high triggers at an 8px
radius ([accordion-trigger](components/crops/accordion-trigger-default.png),
[accordion-content](components/crops/accordion-content-default.png))
animating on `--site-accordion-duration` (350ms); scroll reveals ride
`--site-reveal-*` (700ms, 60ms stagger). Sections alternate the light
field with `.dark` islands — see Themes.

## The voice surfaces

`/sonic` heads with the product display headline
([pd-h1](components/crops/pd-h1-default.png)) and the hero CTAs
([pd-cta](components/crops/pd-cta-default.png) at 40px high,
[pd-secondary](components/crops/pd-secondary-default.png)). The demo
stacks use-case chips ([usecase-chip](components/crops/usecase-chip-default.png),
144 x 30 pills at 12px) and voice/locale chips
([voice-chip](components/crops/voice-chip-default.png), 118 x 34). Play
controls come in three sizes: the 60 x 36 demo play
([play-btn](components/crops/play-btn-default.png)), the 32px square
sample buttons ([word-play](components/crops/word-play-default.png)) and
the 81px globe play on /voices
([globe-play](components/crops/globe-play-default.png)). The voice
picker is a local popover — opened for
[sonic-light-voice-menu](screenshots/sonic-light-voice-menu.png) — and
voice rows ([voice-row](components/crops/voice-row-default.png), 244 x
38) ring verdant on focus-visible where other controls ring `--ring`.
`/voices` lays the library over a globe of 19px locale dots
([globe-dot](components/crops/globe-dot-default.png), 50% radius) with
40px locale arrows ([globe-arrow](components/crops/globe-arrow-default.png))
and 38px globe voice rows
([globe-voice](components/crops/globe-voice-default.png)). Play controls
were pressed only for measurement; no audio was generated.

## Pricing

`/pricing` heads with the display title
([pricing-h1](components/crops/pricing-h1-default.png)) over four plan
cells ([plan-card](components/crops/plan-card-default.png), ~255 x 543,
24px side padding, 40px top) each carrying its name
([plan-name](components/crops/plan-name-default.png)) and a 207 x 36 CTA
([plan-cta](components/crops/plan-cta-default.png) verdant,
[plan-cta-alt](components/crops/plan-cta-alt-default.png) outlined). The
usage calculator is a 556 x 46 slider/input
([plan-slider](components/crops/plan-slider-default.png)); the plan tabs
(`plan-tab`) rendered zero-size at capture and are recorded missing.
FAQ items are native details/summary
([faq-trigger](components/crops/faq-trigger-default.png), 852 x 103,
48px side padding) — locally toggled, no accordion JS.

## The sign-in boundary

`play.cartesia.ai` is a Clerk app sharing the semantic layer: a centred
640px column ([login-card](components/crops/login-card-default.png),
[signup-card](components/crops/signup-card-default.png)) holds a 420 x
44 email field ([email-field](components/crops/email-field-default.png),
8px radius, `#ffffff` field fill on `#e4e3db` border), the verdant
`Continue` at 420 x 44 with a 12px radius
([continue-btn](components/crops/continue-btn-default.png)), icon-only
SSO buttons ([sso-btn](components/crops/sso-btn-default.png), ~206 x 44)
and a passkey button
([passkey-btn](components/crops/passkey-btn-default.png)). Fields were
never filled; nothing was submitted. Everything past this card — the
playground console — is the authenticated boundary.

## The docs surface

`docs.cartesia.ai` is a separate Mintlify application: its own header
([docs-header](components/crops/docs-header-default.png)), a 278 x 36
search pill ([docs-search](components/crops/docs-search-default.png)),
268 x 32 sidebar items at a 12px radius
([docs-nav-item](components/crops/docs-nav-item-default.png)) and a 36px
Inter page title ([docs-h1](components/crops/docs-h1-default.png)). Its
Inter face and token layer are recorded in raw/css-vars-docs.json but
kept out of tokens.json — a measured neighbour, not this system.

## Themes

The marketing site paints light and declares a `.dark` scope that
re-binds the same semantic roles: `#171715` field, `#cdc8c1` text, the
primary switching from verdant `#309d4b` to growth `#abd49e` on
near-black, borders turning white/10%. The dark set in tokens.json is
that re-binding, resolved inside a `.dark` wrapper by
tools/capture/vars.mjs; on the captured pages it paints only inside
dark islands, never page-wide.

## Mobile (390 wide)

At phone width the header keeps 64px
([m-header](components/crops/m-header-default.png)) with a 36px menu
toggle ([m-menu-button](components/crops/m-menu-button-default.png))
that opens a full-height overlay
([m-menu-open](components/crops/m-menu-open-default.png), 390 x 844,
[mobile-home-light-menu](screenshots/mobile-home-light-menu.png)) of
56px nav items ([m-nav-item](components/crops/m-nav-item-default.png)).
The hero drops to 32px PP Kyoto
([m-hero](components/crops/m-hero-default.png), 308 x 184); product
grids stack single-column
([mobile-sonic-light-full](screenshots/mobile-sonic-light-full.png)).

## Boundaries

- The playground behind sign-in (voice console, cloning, agents, API
  keys, billing) was never reached.
- The Talk to Skylar / Talk to Cartesia live-agent calls were never
  started; the voice demos were exercised only as far as their own
  play/select controls.
- No form was filled or submitted; no checkout or onboarding CTA was
  followed past its public landing.
- The consent island was hidden before every shot and never answered.
- Footer/nav routes beyond the captured set (/company, /integrations,
  /startups, the /product/* SEO pages, /speech-to-text-api,
  /voice-changer) are listed in the Gaps.
