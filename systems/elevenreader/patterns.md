# ElevenReader patterns

How the measured components combine on elevenreader.io's public surface, read
from the screenshots and the component entries in
[components.md](components.md). Every captured surface paints the same light
theme: black ink on a white field with a `#F5F3F1` promo band, Inter for UI
and body, Waldenburg for display. Values are from the light set.

## The promo band and header

Every page opens on the announcement band
([promo-banner](components/crops/promo-banner-default.png), 1440 x 49 on
`#F5F3F1` with a 10%-black bottom hairline): centred copy in Inter 14px/500
and a white pill `Get this offer` CTA
([promo-cta](components/crops/promo-cta-default.png), 32px high, ring
shadow). Under it sits the 64px header
([header](components/crops/header-default.png), a 1304px column inside the
1440px field): the wordmark anchor
([logo](components/crops/logo-default.png), 164 x 36), the `Main` nav —
`Explore`, the `Discover` chevron trigger
([nav-discover](components/crops/nav-discover-default.png), a 36px square),
`Pricing`, `For Authors`, `Upload & Listen` — then a 1px-outlined `Sign in`
pill ([nav-signin](components/crops/nav-signin-default.png), 36px) and the
black `Start listening free` pill
([nav-cta](components/crops/nav-cta-default.png), 36px, `#000` → `#6E6E6E`
on hover). Nav links are transparent 9999px pills that fill `#F6F6F6` on
hover ([nav-link](components/crops/nav-link-default.png)). Pressing the
Discover trigger opens an 846 x 470 white mega-menu panel
([nav-dropdown](components/crops/nav-dropdown-default.png),
[home-light-menu](screenshots/home-light-menu.png)) with muted 14px/500
column headings ([menu-heading](components/crops/menu-heading-default.png)),
260px genre links ([menu-link](components/crops/menu-link-default.png)) and
a free-audiobook cover grid. Keyboard focus draws a 2px solid `#000` outline
at 2px offset on every control.

## The home hero and book orbit

The home page hero ([home-light-default](screenshots/home-light-default.png))
centres a 60px Waldenburg headline at -1.8px tracking
([hero-h1](components/crops/hero-h1-default.png), 508 x 120 — 40px at phone
width) over an 18px lede at 60% opacity
([hero-lede](components/crops/hero-lede-default.png)), then two 52px pills:
the black `Start listening free` ([hero-cta](components/crops/hero-cta-default.png))
and the white ring-shadowed secondary pill
([hero-cta-2](components/crops/hero-cta-2-default.png)). Below them a 3D
book-orbit carousel loops cover cards
([book-cover](components/crops/book-cover-default.png), 16px radius, covers
on a gray-300 backing) — motion-reduce sets its duration to 0
(`_meta.reducedMotion`).

## Home sections

Mid-page sections repeat one grammar
([home-light-full](screenshots/home-light-full.png)): a small Waldenburg
eyebrow at 24px/375 ([eyebrow](components/crops/eyebrow-default.png)), a
36px Waldenburg section heading at -0.36px tracking
([section-h3](components/crops/section-h3-default.png)), then content — book
rows with underline-on-hover title links
([book-link](components/crops/book-link-default.png)), genre filter chips
([genre-chip](components/crops/genre-chip-default.png), 44px white pills
with the ring shadow), ghost `View all` pills
([view-all](components/crops/view-all-default.png)) and a mid-page white
`Try it free` pill ([try-cta](components/crops/try-cta-default.png), 44px).
The FAQ is a stack of `<details>` cards on a `#FAF8F8` tint at a 20px radius
([faq-item](components/crops/faq-item-default.png), 780 x 67 closed → 796 x
159 open with a small lift shadow); the summary row is a 20px Waldenburg
question with a +/- indicator
([faq-summary](components/crops/faq-summary-default.png)).

## Explore and catalog rails

/explore ([explore-light-default](screenshots/explore-light-default.png))
leads with a 36px Waldenburg `Find your next audiobook` heading
([explore-h1](components/crops/explore-h1-default.png)) over coverflow
rails: a 16px/500 Inter rail heading
([rail-h2](components/crops/rail-h2-default.png)), 300px-wide cover cards
([coverflow-card](components/crops/coverflow-card-default.png), 2:3 covers
on the `#F0F0F0` hovered fill, `shadow-lg`, group-hover scale-105), 16px/500
title links ([book-title](components/crops/book-title-default.png)) and
14px `#767676` meta lines
([book-meta](components/crops/book-meta-default.png)) — author, length,
price. Genre links ([genre-link](components/crops/genre-link-default.png))
route to /genres/*. The same rails pattern repeats on /collections,
/genres, /free-audiobooks and /iconic-voices.

## The pricing surface

/pricing ([pricing-light-default](screenshots/pricing-light-default.png))
centres a 60px Waldenburg display title
([pricing-h1](components/crops/pricing-h1-default.png)) over a segmented
billing toggle on a sunken track: the selected segment is a 48px white pill
with the ring shadow carrying the green `Save 25%` chip
([billing-on](components/crops/billing-on-default.png),
[save-badge](components/crops/save-badge-default.png) — `#E1F5E0` fill,
`#307D18` text), the idle segment sits transparent with `#57534F` text
([billing-off](components/crops/billing-off-default.png); the toggled page
is [pricing-light-monthly](screenshots/pricing-light-monthly.png)). Below,
#FDFCFC plan cards at a 40px radius on a 1px `#EAE9E9` hairline
([plan-card](components/crops/plan-card-default.png), 584 x 722, 56px
padding) hold a 22px Waldenburg plan name
([plan-name](components/crops/plan-name-default.png)), a 36px price figure
([plan-price](components/crops/plan-price-default.png)), a 52px black pill
action ([plan-cta](components/crops/plan-cta-default.png)) and feature rows
([feature-li](components/crops/feature-li-default.png)).

## The audiobook detail page

A public audiobook page
([audiobook-light-default](screenshots/audiobook-light-default.png)) stacks
breadcrumb links ([ab-crumb](components/crops/ab-crumb-default.png), 36px
pills), the square 262px cover at an 8px radius
([ab-cover](components/crops/ab-cover-default.png)), a 36px Waldenburg
title ([ab-h1](components/crops/ab-h1-default.png)), the by-author link
([ab-author](components/crops/ab-author-default.png)), the `Audio only`
format chip ([ab-chip](components/crops/ab-chip-default.png)) and a 48px
`Preview` pill ([ab-preview](components/crops/ab-preview-default.png) —
measured, never pressed; a press plays audio). Related rows repeat the
book-link grammar ([ab-row](components/crops/ab-row-default.png)).

## Compare

/compare centres a 44px Waldenburg title
([cmp-h1](components/crops/cmp-h1-default.png)) over a 932px comparison
table ([cmp-table](components/crops/cmp-table-default.png)) of header cells
([cmp-th](components/crops/cmp-th-default.png)) and body cells
([cmp-td](components/crops/cmp-td-default.png)) with check/cross marks,
then 10px-radius links to in-depth comparisons
([cmp-link](components/crops/cmp-link-default.png)).

## The auth boundary cards

/reader/sign-in and /reader/sign-up are bare centred 360px columns on the
page field ([signin-card](components/crops/signin-card-default.png),
[signup-card](components/crops/signup-card-default.png) — the cards paint
nothing; white on white): the large wordmark, a Waldenburg heading, then
three stacked 40px pills — sunken `Sign in with Google`
([sso-google](components/crops/sso-google-default.png), `#F2F2F2` → 10%
black overlay on hover), inverse `Sign in with Apple`
([sso-apple](components/crops/sso-apple-default.png)) and outlined
`Sign in with email`
([signin-secondary](components/crops/signin-secondary-default.png)). The
email toggle expands the credential form (a local aria-expanded toggle):
40px pill inputs with a 1px `#E5E5E5` hairline and the focus-ring class
([email-field](components/crops/email-field-default.png),
[password-field](components/crops/password-field-default.png),
[signup-field](components/crops/signup-field-default.png)), a `Forgot
password` text button ([forgot-btn](components/crops/forgot-btn-default.png))
and the black submit pill
([signin-submit](components/crops/signin-submit-default.png)). The card
footer carries `Create account` ([create-link](components/crops/create-link-default.png))
and small legal copy ([signup-legal](components/crops/signup-legal-default.png)).
Nothing was ever submitted.

## The footer

The footer ([footer](components/crops/footer-default.png), 1440 x 967)
opens on a big `Footer` wordmark heading, then link columns under muted
13px/500 headings ([footer-col](components/crops/footer-col-default.png))
with `effect-focus-underline` links
([footer-link](components/crops/footer-link-default.png)), and a legal row
holding the `Cookie Settings` text button
([cookie-btn](components/crops/cookie-btn-default.png) — measured, never
pressed). On mobile the columns collapse into `<details>` accordions.

## Mobile at 390

At phone width ([mobile-home-light-default](screenshots/mobile-home-light-default.png))
the promo band stays but the header compresses to the wordmark plus a 40px
hamburger ([m-header](components/crops/m-header-default.png),
[m-menu-button](components/crops/m-menu-button-default.png)). The hamburger
opens a full-screen menu overlay
([m-menu-open](components/crops/m-menu-open-default.png), white, menu
elevation) of 24px nav rows ([m-nav-item](components/crops/m-nav-item-default.png))
plus the sign-in/CTA pills
([mobile-home-light-menu](screenshots/mobile-home-light-menu.png)). The
hero shrinks to 40px Waldenburg ([m-hero](components/crops/m-hero-default.png))
and the footer columns become `<details>` accordions
([m-footer-col](components/crops/m-footer-col-open.png),
[m-footer-summary](components/crops/m-footer-summary-default.png)).
