# Endless Tools patterns

How the measured components combine on endlesstools.io's marketing surface
and app.endlesstools.io's signed-out shell, read from the screenshots and the
component entries in [components.md](components.md). Both surfaces paint one
dark theme; all values are from the dark set unless noted.

## The header

Every marketing page opens under a sticky 80px bar
([header](components/crops/header-default.png)): a transparent-to-dark band
that paints a gradient scrim `linear-gradient(rgb(0, 0, 0) 14.73%, rgba(0, 10,
10, 0))` over the content scrolling beneath
(`core.gradient.nav`, also exposed as `dark.surface.header-veil`). Inside the 1440px canvas the logo
([logo](components/crops/logo-default.png)) anchors the left, a plain **Log
in** link ([nav-login](components/crops/nav-login-default.png)) sits beside a
white 35px pill **Start for free** CTA
([nav-cta](components/crops/nav-cta-default.png)) — the inverted-action
convention the whole site follows — and the promo/testimonial card floats
fixed above the fold near the viewport's bottom. On the phone the bar
compresses to the same pattern at 390 wide ([m-header,
m-cta](components/crops/m-header-default.png)).

## The hero

The hero centres a 42px Inter Medium title — "A visual exploration tool for
graphic designers." ([hero-title](components/crops/hero-title-default.png)) —
with a decorative orbiting asset mark
([hero-mark](components/crops/hero-mark-default.png)), a muted `#959595`
lede ([hero-lede](components/crops/hero-lede-default.png)), and the one pink
moment on the whole surface: **Start creating free** on `#ff13b1` at pill
radius ([hero-cta](components/crops/hero-cta-default.png)); its hover lifts to
`#ff4bc4` and the press shrinks to `scale-95` on a 150ms ease.

## The asset strips

Below the hero, three repeated strips — **Use a library**, **Generate**,
**Bring your own** — pair a section title
([asset-title](components/crops/asset-title-default.png)) with a horizontal
run of square media thumbs
([asset-thumb](components/crops/asset-thumb-default.png)) on `#1e1e1e` tiles
at the smaller 16px thumb radius. They are the site's product-teaser motif:
the same card language the pricing block reuses at a bigger radius.

## The statement sections

Between the strips, single-column statements alternate with product stills:
"The hard part isn't making it.", "One workspace. Endless combinations.",
"From idea to production.", "Create once. Reuse everywhere.", "Teach ideas,
not software." — 42px title type ([section-title]) over editor video
stills ([editor-shot], the 1300x700 workspace stage in the "One
workspace" band) that preview the canvas without exposing it. The
pattern is restraint: one line of headline, one image, near-black
everywhere.

## The pricing block

The pricing section centres the billing toggle — **Yearly** / **Monthly**
pills ([billing-yearly](components/crops/billing-yearly-default.png),
[billing-monthly](components/crops/billing-monthly-default.png)) with a
`#ff3dae` **Save 20%** pill ([save-pill]) — over plan cards
([plan-card](components/crops/plan-card-default.png)): 356px `#121212`
columns at 33px radius under a `#222` ring, each carrying a tier chip
([plan-chip], [plan-chip-pro], [plan-chip-edu] — education alone gets the
`#2c5cff` blue), a price ([plan-price]), a feature list
([plan-feature]), and an inverted white-pill CTA
([plan-cta]). Team and education get their own CTAs on the same convention:
[team-cta] white, [edu-cta](components/crops/edu-cta-default.png) `#2c5cff`.

## The testimonial carousel

Social proof is a horizontal carousel of `#080808` cards
([social-card](components/crops/social-card-default.png)) — a quote, a
handle, an avatar on the 12px `rounded-fill` radius under a `#373737`
inset ring — with a single round arrow control
([carousel-prev](components/crops/carousel-prev-default.png)) and a fixed
promo card ([promo-card](components/crops/promo-card-default.png)) floating
over the fold. The carousel auto-advances, so two captures differ.

## The newsletter band

The close of home is **Stay in the loop** ([news-title]): a dark `#1e1e1e`
pill field at 38px under a `#2a2a2a` ring
([news-field](components/crops/news-field-default.png)), a white-pill submit
([news-submit](components/crops/news-submit-default.png)), and a tiny
rounded consent checkbox with its legal copy
([news-consent](components/crops/news-consent-default.png); the checkbox is
one of the only fully-round inputs). The form was measured and the checkbox
toggled for capture, never submitted.

## The login card

app.endlesstools.io/login centres a 450px card
([login-card](components/crops/login-card-default.png)) on the `#0a0a0a`
app field (`--color-black`, darker than marketing's `#000`): the logo
([login-logo]), a title ([login-title]), an email field in the same
`#1e1e1e`-under-`#2a2a2a` language ([login-field]), a full-width ink-inverse
**Send code** pill ([send-code](components/crops/send-code-default.png)),
and a **Log in with password** switch ([login-switch]) that re-renders the
card locally into the password form
([login-dark-password](screenshots/login-dark-password.png):
[login-password-field], [login-submit], [login-forgot]). Focus on the app
shell shows as a border swap to grey-1, not a ring; legal links sit under
the card ([login-legal]). No code was sent and no password entered.

## The legal pages

The privacy policy and terms render as long document pages under their own
header ([legal-header]) with a sign-in pill ([legal-signin]), a document
title ([legal-title]) and body copy ([legal-content]) with inline links
([legal-link]). At 14,086px and 16,366px tall their full-page shots exceed a
single GPU texture, so they were captured as part tiles and stitched into
[privacy-dark-full](screenshots/privacy-dark-full.png) and
[terms-dark-full](screenshots/terms-dark-full.png).

## The mobile layout

At 390 wide the page keeps the same order — header
([m-header]), hero ([m-hero]), asset cards
([m-asset-card]), plans ([m-plan-card]) — mostly single-columned with the
same tokens. The exception is pricing: the plan cards keep their wide
desktop columns inside a horizontally scrolling row rather than stacking,
so a phone swipes sideways through the tiers. The shots are at 2x device scale
([mobile-home-dark-default](screenshots/mobile-home-dark-default.png),
[mobile-login-dark-default](screenshots/mobile-login-dark-default.png)).
