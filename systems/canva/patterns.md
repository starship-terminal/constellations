# Canva patterns

How the measured components combine on canva.com's public signed-out
surface, read from the screenshots and the component entries in
[components.md](components.md). The surface paints light, with one
genuinely dark band: the home header and hero sit inside `.theme.dark`
over a gradient media layer, and feature sections lower on the page carry
the same dark treatment — painted dark surfaces, not a user toggle. The
capture was served the Singapore region, so every price renders `S$`.

## The chrome: dark header over the gradient band

Every desktop page opens on an 80px header
([header](components/crops/header-default.png)): the Canva wordmark
([logo](components/crops/logo-default.png), ~90 x 32), the flyout
triggers `Design` / `Product` / `Plans` / `Business` / `Education` /
`Help` ([nav-trigger](components/crops/nav-trigger-default.png), 14/22
white at a 12px radius, taking a 20% purple-tint wash on hover and 15%
white on pressed), then the auth pair — `Sign up` as a 10px ghost button
([signup-cta](components/crops/signup-cta-default.png)) with a 20%-white
inset ring that fills 7% white on hover, and `Log in` as a 90%-white pill
([login-link](components/crops/login-link-default.png)) with ink text that
reaches 100% white on hover and drops to 80% pressed. On the home band
these sit inside `.theme.dark`; on the light product pages the same
structure repaints (Sign up goes purple, Log in keeps the white fill).

The `Design` trigger opens a 478px mega-menu
([nav-dropdown](components/crops/nav-dropdown-default.png)) — see
[home-light-menu](screenshots/home-light-menu.png): a white panel whose
left column paints a 32px left-corner radius, holding link groups
(Digital design: Docs / Sheets / Whiteboards / Presentations; then Print
design, Images, Videos) with 200 x 38 rows
([menu-link](components/crops/menu-link-default.png)) that take the 6%
ink wash on hover. The menu auto-closes a few seconds after opening —
each flyout reading re-opened it with the trigger first.

## The home hero and the tools showcase

The hero band is a gradient media layer, not a CSS fill — the
purple-to-teal field is painted by an image/video element behind the
content, so no flat colour token pretends to be it. On it: `What will
you design today?` in Canva Sans 80/88 regular
([hero-title](components/crops/hero-title-default.png), white over the
band), a 24/33.6 lede
([hero-sub](components/crops/hero-sub-default.png)) in the same
rgba(255,255,255,0.898), and `Start designing`
([hero-cta](components/crops/hero-cta-default.png), 192 x 56): the 90%
white fill at a 20px radius with ink 16/22 semibold text, transitioning
background/shadow/colour at 0.1s and shrinking ~0.99 pressed.

Below the band sits the tools showcase: pill tabs `AI`, `Presentations`,
`Social`, `Video`, `Print Shop`
([tool-tab](components/crops/tool-tab-default.png), 9999px radius,
18/24 semibold, 6% ink wash on hover) over a ~1332px media panel
([tool-panel](components/crops/tool-panel-default.png)) holding the
selected tool's artwork — the Presentations state is
[home-light-tools](screenshots/home-light-tools.png). The light sections
that follow mix in dark `.theme` feature cards
([feature-card](components/crops/feature-card-default.png), ~851 x 166)
with `Explore …` links
([explore-link](components/crops/explore-link-default.png)) drawn in the
same 90%-white-fill button language, and 56/61.6 section headings
([section-h2](components/crops/section-h2-default.png)).

## Pricing, in Singapore dollars

`/pricing` was served `S$` prices (the capture's documented geo
behaviour): a 64/70.4 `Plans and pricing` display
([pricing-h1](components/crops/pricing-h1-default.png)), the audience
tabs `Individuals and business` / `Education`
([plan-tab](components/crops/plan-tab-default.png), 142 x 64 pill rows —
focusing a tab auto-activates it, so the Education view swaps the whole
grid to `?tab=education`), and the Monthly/Yearly billing switch
([billing-switch](components/crops/pricing-light-billing.png for the
toggled Yearly state), a 40 x 24 `#8b3dff` pill with a layered-shadow
white thumb). Four white plan cards — Free `S$0`, Pro `S$165`, Business
`S$250`, Enterprise `Let's talk`
([plan-card](components/crops/plan-card-default.png) shows the measured
inner column; the white surface carries 16px radius) — each with a
~29px price figure
([plan-price](components/crops/plan-price-default.png)) and a purple 40px
action
([plan-cta](components/crops/plan-cta-default.png)): `#8b3dff` default,
`#7630d7` hover, `#612dae` pressed — the ramp the whole site draws its
actions from. Below, the feature-comparison rows
([feature-accordion](components/crops/feature-accordion-default.png),
1286 x 64 on the 14% ink wash at 14px radius) stay measured-closed; every
trial, demo and Contact-Sales action was never followed.

## Templates and the product pages

`/templates` pairs the 64/70.4 `Free templates` title
([templates-h1](components/crops/templates-h1-default.png)) with a 46px
search field
([search-field](components/crops/search-field-default.png), white
container, focused only — no query was ever typed into a live search)
and a grid of category cards
([category-card](components/crops/category-card-default.png), 240 x 80):
image tiles linking `/presentations/templates/` and siblings.
`/presentations/templates/` shows the gallery itself; `/presentations`,
`/docs`, `/whiteboard`, `/create` and `/pro` are the product marketing
pages — each reuses the dark-band hero plus light feature-section rhythm
from home; `/features` is the index. All were captured as screenshots;
their marketing claims about the editor were never verified.

## The auth card

`/login` and `/signup` centre a white card
([auth-card](components/crops/auth-card-default.png)) over a dimmed
template collage ([login-light-default](screenshots/login-light-default.png)):
`Log in or sign up in seconds` (24/32 semibold), then `Continue with
Google` / `Facebook` / `email` — 304 x 40 secondary buttons
([oauth-button](components/crops/oauth-button-default.png)) whose only
border is the inset `rgba(53,65,90,0.2)` 1px ring, taking 6% / 14% ink
washes on hover/pressed — and `Continue another way`. Pressing
`Continue with email` once reveals the email step (a local UI move):
the 278 x 38 `username` field
([username-input](components/crops/username-input-default.png)) was
focused and given sample text that was deleted again, and the purple
`Continue` ([continue-button](components/crops/continue-button-default.png))
was measured, never pressed. Everything past that card — the editor,
Brand Kit, dashboards — is the package boundary.

## The light footer

Pages end on a footer that fades to `#f6f7f8`
([footer](components/crops/footer-default.png), 1420px of download links,
Product / Plans / About columns and legal): 14/22 link rows
([footer-link](components/crops/footer-link-default.png)) on the ink-wash
hover language, and a social icon row
([social-icon](components/crops/social-icon-default.png), 32px). The
footer is where the region shows: `English (US)` locale with Singapore
content.

## Mobile

At 390 the header keeps the wordmark plus a 32px burger
([m-header](components/crops/m-header-default.png),
[m-menu-button](components/crops/m-menu-button-default.png)). The menu
opens as a full 390 x 844 panel
([m-menu-open](components/crops/m-menu-open-default.png)) — see
[mobile-home-light-menu](screenshots/mobile-home-light-menu.png): 42px
nav rows (`Design` / `Product` / `Plans` / `Business` / `Education` /
`Help`, [m-nav-item](components/crops/m-nav-item-default.png)) in 21/26
type, then the auth pair — `Log in` purple, `Sign up` outlined
([m-signup](components/crops/m-signup-default.png), 322 x 40). The hero
display compresses to 45/49.5
([m-hero](components/crops/m-hero-default.png)). The menu's focus ring is
amber `#e59700` — a different ring than the desktop's.

## The state signature

Canva's interaction language is two washes and a hairline: on light,
hover is the 6% ink wash `rgba(64,79,109,0.06)` and pressed the 14%
`rgba(57,70,96,0.14)`; on the dark band hover is 7% white (or a 20%
purple tint on the nav triggers) and pressed 15% white. Secondary
actions carry no border — a 1px inset `rgba(53,65,90,0.2)` shadow ring
instead. Focus draws a real outline: `#99c8ff` light blue on the dark
band, `#005fcc` on light, `#e59700` amber inside the mobile menu — 1px
`auto` mostly, 2px on the nav trigger. Pressed buttons shrink ~0.99 via a
0.07s transform; other control transitions run 0.1s.

## Boundaries

Everything behind the auth card — the design editor, Brand Kit,
dashboards, teams, billing, account — was never reached and is not
inferred anywhere in this package. `/solutions/brand-management/`
returned Canva's generic 404 — recorded, not retried. Sign up, Get
started, Start a free trial, Contact Sales and the OAuth providers were
measured or screenshotted, never followed; no account was created, no
form submitted, no consent button clicked (the cookie banner was hidden
per capture). See the Gaps section in
[components.md](components.md).
