# Calm patterns

How the measured components combine into screens. All values live in
[tokens.json](tokens.json); component entries are in
[components.md](components.md).

## Two painted surfaces, not a theme toggle

Calm paints two unrelated surfaces on the public site. The marketing pages
(`/`, `/family`, `/gift`, `/science`, `/mindfulness-tips`, `/terms`) are light:
photographic heroes, navy `#1a3e6f` ink on white sections, and fully-rounded
white pills for actions. The `/app/sleep`, `/app/meditate` and `/app/music`
pages are a dark signed-out preview of the real app shell: a scene-gradient
canvas, a black@30% icon rail and white labels. No switch is offered; `tokens.json`
keeps them as `light` and `dark` sets.

## The marketing header and hero

The header floats over the hero photograph behind a navy scrim
(`linear-gradient(#176293, transparent)`) that keeps the white items legible
— it is a gradient veil, not fully transparent chrome. Left: the 76x60
rounded-square app-icon logo (a blue-violet gradient tile — the tile is image artwork, not a CSS gradient — with
the white wordmark), then the nav items — plain styled-components `button`s
(Sleep, Stress & Anxiety, Mindfulness, Screening) — and the `Calm Health`
chevron trigger (120x22). Right: `Log In` (opens the login card) and the
200x56 white `Try Calm for Free` pill (100px radius, `#383838` ink), which
navigates to `/signup-flow`. The nav items are buttons that swap the view;
no dropdown panel paints in the captured pass — the panel evidence lives in
the mobile menu.

Under it: a full-bleed lake-and-mountain photograph, the 49.5px navy headline
"Calm your mind. Change your life." (768x74), a 28px lede, then a pair of
actions — the 335x58 gradient hero pill (`#2477AA` -> `#6461E0`, 100px
radius, white label) and an outline companion. Marketing sections repeat the
pattern: a 36px navy `h2`, then 352x247 section cards (`Stress less.` /
`Sleep more.` / `Live mindfully.`) that carry their Learn-more label inside.

## The dark preview shell (`/app/*`)

A real product shell served signed out. Left: the 240px rail (240x900) —
wordmark, then 192x48 icon-plus-label items (Home, Meditate, Sleep, Music,
Wisdom and more); the selected item carries a filled icon tile and a bolder (700)
label — every label paints white on the rail. The top bar holds the 48x48 search
icon link to `/app/search`, a translucent `Log In` pill (white@10% bg, white
ink, 100px radius) and the white `Try Calm for Free` pill (174x56, black
ink).

Content sections run on the scene-gradient canvas: a row of 26px-tall category pills
— the selected one white with navy ink, the rest black@30% with white ink —
then content rails of 300x256 cards (artwork, the 33x20 white `New` chip,
title and narrator) with 32x32 carousel chevrons and `See All` links. Two
upsell surfaces close the page: the mid-page subscribe banner (1153x76,
white@10% fill, 16px radius, one whole-anchor) and the bottom notify bar
(1425x92) carrying the 147x56 `Sign up today` gradient pill
(`#2477AA` -> `#6461E0`). Every play action leads to signup — the cards are
locked previews.

## The auth surfaces

`Log In` opens the auth card in place: a 544x596 white modal (16px radius,
`rgba(0,0,0,0.25) 0 8px 24px` shadow) over a dimmed backdrop. Inside, a navy
`Sign in with Email` pill (462x56, `#1a3e6f`), then white outline social
pills for Facebook, Apple and Google (same 462x56, 100px radius), Terms and
Privacy links, and a `Sign up` mode toggle; the 48x36 `modal-close` X sits
top-right. `Try Calm for Free` navigates to `/signup-flow?source=homepage`
instead — its landing stayed PerimeterX-blocked this capture, so the flow's
first step is recorded as a boundary, not a design.

## Calm Health (B2B)

`health.calm.com` is a separate WordPress surface — same Figtree stack, a
98px `nav.main-menu` bar with megamenu triggers (Solutions, Resources, About
Us), a `Log In` and the gradient `btn--primary` contact pill (150x41, the
measured three-stop `#4e4bb1` -> `#6461e0` -> `#60b4e7` ramp, 100px radius). Below the
hero, `custom-cards__card` tiles (378x119, white, 12px radius, a soft
`0 2px 12px rgba(0,0,0,0.08)` shadow) and a WP footer. The
`/calm-for-organizations/` page adds a public self-serve seat checkout.

## The help center and the footer

`/faq/web` is a Zendesk Guide help center themed to Calm — it is the one
surface that ships a declared token layer: the Garden `--zd-*` custom
properties (palette, font sizes, weights and families), captured raw and
emitted under the `zd` token group. The marketing footer closes every page:
a navy column block (1425x524) of link lists and the 18x19 social icon
anchors — no app-store badges paint on it.

## Mobile at 390px

The same header compresses to 375x64 (sticky, z:100): the 64x25 logo, the
180x52 `Try Calm for Free` pill and the 48x48 hamburger (`Open Mobile
menu`). The hamburger opens a full-screen panel — `nav[aria-label="Mobile
navigation menu"]`, 375x844, fixed at z:999 — painted with the brand
gradient (`#60B4E7` -> `#6461E0` top to bottom) under 24px white nav items
stacked at 61px pitch, a `Calm Health` submenu trigger, `Log In`, then the
333x52 `Try Calm for Free` and `Already have an account?` pills.

## Focus, motion, reduced motion

Keyboard focus draws a ring on 16 of the 27 focused components — `1px auto
#101010` nearly everywhere (nav, rail, tabs, cards, footer links), `2px solid
#f8d22d` on the health CTA and `1px #eccd37` on its card; the pills change
fill or text instead. Motion is short: `all 0.2s` on health chrome, `0.3s
ease-out` on the pills and links, `0.3s ease` opacity on the content cards,
`0.5s` on the login card and health cards. Under `prefers-reduced-motion`
the header's measured transition stays `0.3s ease-out` — the site does not
reduce it.

## Boundaries

The product lives behind the login card: playback, home feed, library,
check-ins, profile and checkout were never reached. `/signup-flow` stayed
PerimeterX-blocked; the signup pill and bar lead there and were never
followed. Pricing only appears inside the flow, on `/family` and `/gift`
(geolocated: SGD here), and on the public B2B organization checkout
($63.78/seat/year). The consent sheet was measured, then hidden — never
answered.
