# Endel patterns

How the measured components combine on endel.io's and app.endel.io's public
surfaces, read from the screenshots and the component entries in
[components.md](components.md). Both hosts paint one dark theme over a pure
black field; all values are from the dark set unless noted.

## The scrim header

Every marketing page opens under a fixed 72px bar
([home-dark-default](screenshots/home-dark-default.png)) whose only paint is
a black-to-65%-to-transparent gradient — the scrim that keeps the bar
readable over scrolled content
([header](components/crops/header-default.png)). Inside it: the 40x40 Endel
mark linking home ([logo](components/crops/logo-default.png)), text nav
links at 22px/28 (ADHD, Sleep, Focus, Relax, Activity) that only underline on
hover ([nav-link](components/crops/nav-link-hover.png)), the **More**
MenuButton whose press opens a flyout of grouped links inside the header
itself ([home-dark-menu-open](screenshots/home-dark-menu-open.png),
[nav-more-open](components/crops/nav-more-open-opened.png)), and two 44px
12px-radius buttons: **Try Today** in `#262626` carrying the product's one
special effect — a white `0 0 15px` glow that survives hover and press
([btn-try](components/crops/btn-try-default.png)) — and **Sign In** in the
same fill without the glow
([btn-signin](components/crops/btn-signin-default.png)). Every grey button
steps its fill from `#262626` to `#808080` on hover and pressed, on a 200ms
background/border transition.

## The hero and the marketing sections

The home hero centres the 60px/72 wordmark "Endel" at 0.35px tracking
([hero-title](components/crops/hero-title-default.png)) — the `--title-h1`
step — over a product still with a 72px white round play button laid on it
([play-button](components/crops/play-button-default.png), 100px radius,
black 36px glyph). Sections below use the 44px/56 `--title-h2` step
([section-title](components/crops/section-title-default.png)) and text
links at 22px/28 (**Try Now**, [try-now](components/crops/try-now-default.png))
or 18px/24 (**Learn More**, [learn-more](components/crops/learn-more-default.png)).
Content width is the declared grid: the 1280px container, 64px gutters,
24px gaps, 12 columns — a soundscape card is exactly `--cols-3` at
270x270 ([soundscape-card](components/crops/soundscape-card-default.png)),
an FAQ row the full `--cols-12` at 1152px
([accordion-title](components/crops/accordion-title-default.png)).

## The FAQ accordion

Product pages end in an FAQ of full-grid rows: each a 76px `#191919`
12px-radius button, 22px/28 question text, a 24px chevron that rotates on a
200ms transform
([accordion-title](components/crops/accordion-title-opened.png)). The open
row's answer panel is the same `#191919` fill with 22px/28 `#bfbfbf` muted
text ([accordion-content](components/crops/accordion-content-opened.png)).
Rows take a quieter hover step than buttons — `#191919` to `#262626`, where
plain buttons climb the full ladder to `#808080`.

## The footer

The footer is a 569px block inside the container
([footer](components/crops/footer-default.png)): link columns (Explore,
product pages) at 18px/24 white
([footer-link](components/crops/footer-link-default.png)), a newsletter row
whose 466x56 field — exactly `--cols-5` — rests on a `#808080` 2px border
next to a matching `#262626` Subscribe button, store badges, 24px social
icons ([footer-social](components/crops/footer-social-default.png)), and a
1px `#191919` hairline over the legal line — Privacy Policy and Impressum
at 18px/24 `#bfbfbf` that brighten to white on hover
([footer-legal](components/crops/footer-legal-hover.png)).

## The signed-out explore page

app.endel.io's root opens signed out on the same system
([app-explore-dark-default](screenshots/app-explore-dark-default.png)): the
app header carries the 158x44 **FREEMIUM** account chip — a 1px `#808080`
bordered pill with 12px `#e0e0e0` text
([user-button](components/crops/user-button-default.png)) — and the app's
own Sign In button. Below, a 956x320 (`--cols-10`) carousel banner with a
24px corner and a 2px `rgba(255,255,255,0.15)` inset outline promotes the
special offer ([banner](components/crops/banner-default.png)), paged by
12px `50%` dots ([banner-dot](components/crops/banner-dot-default.png)).
Scenario tags are 56px 100px-radius `#262626` pills
([scenario-pill](components/crops/scenario-pill-default.png)); soundscapes
list as 956x56 rows ([soundscape-row](components/crops/soundscape-row-default.png));
and the fixed mini player at the bottom is a 400x88 `#191919` 100px-radius
pill over a black scrim gradient, holding a paused soundscape and transport
([mini-player](components/crops/mini-player-default.png)) — audio was never
started.

## The player

The public player at `/player/focus`
([app-player-dark-default](screenshots/app-player-dark-default.png)) frames
the visualizer between a 168px header — a `#2b2b2b` inner bar, the
soundscape title at 28px ([player-title](components/crops/player-title-default.png))
and the 44px icon-only close button — and a footer of mode icons
([button-mode](components/crops/button-mode-default.png), the active one
filling to a 56px disc,
[button-mode-active](components/crops/button-mode-active-default.png)),
56px round `#191919` transports
([player-control](components/crops/player-control-default.png)) that step
to `#808080` on hover, the 129x5 two-tone volume slider
([volume](components/crops/volume-default.png)), a 100px-radius **Set
Timer** pill ([btn-set-timer](components/crops/btn-set-timer-default.png))
and the 20px-top-corner **Explore** sheet edge
([btn-explore](components/crops/btn-explore-default.png)).

## The Set Timer sheet

Set Timer opens the app's bottom sheet over an `rgba(0,0,0,0.8)` scrim
([app-player-dark-timer-open](screenshots/app-player-dark-timer-open.png)):
a 300x300 `#191919` panel at 32px radius
([timer-dialog](components/crops/timer-dialog-opened.png)) with duration
chips, the 300x56 `#262626` **Unlock** row bordered in white — the premium
upsell that starts checkout, measured never pressed
([btn-unlock](components/crops/btn-unlock-opened.png)) — and a Done row.
The sheet slides in on a 300ms cubic-bezier(0.25,0.46,0.45,0.94); Escape or
Done closes it.

## The sign-in card

The header's Sign In navigates in-app to a public auth page
([app-login-dark-default](screenshots/app-login-dark-default.png)): a
centred card — 564px wide, exactly `--cols-6` — holding the "Sign In or
Register" head at 44px, a 62px email field resting on a `#808080` border
that goes white on focus
([input-email-login](components/crops/input-email-login-focused.png)), the
564x56 **Continue** button in `#262626` with a white border
([btn-continue](components/crops/btn-continue-default.png)), and two 180x56
icon-only OAuth buttons ([btn-oauth](components/crops/btn-oauth-default.png)).
Nothing was entered or sent.

## Mobile

At 390 the surfaces stack to one column: the header shrinks to 56px
([m-header](components/crops/m-header-default.png)) with the mark, a small
Try Today and the 81x36 **Menu** button — `#262626`, 12px radius, a 12px
label ([m-menu-button](components/crops/m-menu-button-default.png)) — whose
press opens the full-screen nav inside the header
([mobile-home-dark-menu-open](screenshots/mobile-home-dark-menu-open.png),
[m-menu-flyout](components/crops/m-menu-flyout-default.png)). The hero
drops to the `--title-h3` step at 36px/42
([m-hero-title](components/crops/m-hero-title-default.png)).
