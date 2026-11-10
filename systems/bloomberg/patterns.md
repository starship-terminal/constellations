# Bloomberg patterns

How the measured components combine on bloomberg.com's public surface, read
from the screenshots and the component entries in [components.md](components.md).
The site paints one light theme; all values are from the light set unless noted.

## The black chrome stack

Three bars stack at the top of every news page
([home-light-default](screenshots/home-light-default.png)): a thin utility
strip ([utility-bar](components/crops/utility-bar-default.png), "Bloomberg the
Company & Its Products" · Terminal demo · Anywhere login · customer support),
then the 52px black logo bar ([logo-bar](components/crops/logo-bar-default.png))
with the wordmark, Sign In, the white bordered Subscribe button
([subscribe-nav](components/crops/subscribe-nav-default.png)) and a search
icon, then the section nav ([section-nav](components/crops/section-nav-default.png)):
Live TV · Markets · Finance · Economics · Industries · Tech · Politics ·
Businessweek · Opinion · Video, with a "US Edition" picker on the right. The
utility strip's first item toggles the company sitemap dropdown in place
([home-light-sitemap](screenshots/home-light-sitemap.png)).

## The securities ticker

Under the nav runs an edge-to-edge rail of index chips
([ticker-bar](components/crops/ticker-bar-default.png)): a "Top Securities"
label, then dark `#1c1c1c` 8px-radius pills
([ticker-pill](components/crops/ticker-pill-default.png)) carrying the index
name, last price and a gain/loss marker. Each pill links its quote page
([ticker-item](components/crops/ticker-item-default.png)) — measured, never
followed.

## The story grid

The front page is editorial blocks, not cards: a lead story
([hero-story](components/crops/hero-story-default.png)) with a big
BWHaasGrotesk headline ([hero-headline](components/crops/hero-headline-default.png)),
secondary stories beside it ([story-secondary](components/crops/story-secondary-default.png)),
dek paragraphs ([dek](components/crops/dek-default.png)), module titles
([section-title](components/crops/section-title-default.png)) over topic lanes
of media modules ([media-module](components/crops/media-module-default.png)).
Hairline `#e5e7eb` rules separate blocks; there are no card fills on the
front. The full page runs to ~13,000px
([home-light-full](screenshots/home-light-full.png)).

## The paywall

Articles render free up to a point — kicker
([article-kicker](components/crops/article-kicker-default.png)), headline
([article-headline](components/crops/article-headline-default.png)), byline
([byline](components/crops/byline-default.png)), lede media
([lede-media](components/crops/lede-media-default.png)) — then the fence: a
`#1c1c1c` band with white copy ("Get unlimited access…") and a white
Claim This Offer button ([paywall](components/crops/paywall-default.png),
[claim-offer](components/crops/claim-offer-default.png)). It is the boundary
of the public surface: measured at rest, never crossed. The article route's
screenshots were PerimeterX-blocked on this pass; the component readings stand.

## The quote page

A public quote page pairs the index name and ticker
([quote-title](components/crops/quote-title-default.png)) with a black Follow
toggle ([follow-button](components/crops/follow-button-default.png) — pressing
it needs an account, so it was never pressed), the last price and change in a
dark pill ([quote-price](components/crops/quote-price-default.png)) and a
key-statistics strip ([quote-stat](components/crops/quote-stat-default.png)),
see [quote-light-default](screenshots/quote-light-default.png).

## Gated surfaces

Live TV is a gated player: the video.js frame and schedule render
([live-player](components/crops/live-player-default.png)) but playback needs a
subscription — the resting gated state is the honest surface
([live-light-default](screenshots/live-light-default.png)). The Sign In button
mounts a `/account/iframe/login` sheet
([signin-sheet](components/crops/signin-sheet-default.png)); under PerimeterX
throttling the sheet renders the verification card, which is what
[home-light-signin](screenshots/home-light-signin.png) shows. Neither was ever
used.

## The offers pages

/subscriptions is a WordPress block surface with its own furniture: a
near-black hero block ([offer-hero](components/crops/offer-hero-default.png)),
the price line ([offer-price](components/crops/offer-price-default.png)), the
`#3523ff` rounded-8 Continue button
([offer-cta](components/crops/offer-cta-default.png)) and white rate-plan cards
with `#b3b3b3` hairlines ([plan-card](components/crops/plan-card-default.png),
[plan-cta](components/crops/plan-cta-default.png)), see
[subscriptions-light-default](screenshots/subscriptions-light-default.png).
Every CTA links toward checkout; none was followed.

## Focus and motion

Controls take a `1px auto #005fcc` focus ring (the same blue-family ring on
nav links, pills, buttons and footer links — see the shared values in
[components.md](components.md)). Measured transitions are short decelerations:
0.2–0.3s `cubic-bezier(0.4,0,0.2,1)` on fills and colours.
