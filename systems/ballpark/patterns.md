# Ballpark patterns

How the measured components combine on ballparkhq.com's public surface, read
from the screenshots and the component entries in [components.md](components.md).
The site paints one light theme; all values are from the light set unless noted.

## The shell

A fixed header block on the white ground ([home-light-default](screenshots/home-light-default.png)):
the Ballpark wordmark ([logo](components/crops/logo-default.png), 96 x 26), text links
Platform / Templates / Pricing, a **Solutions** flyout button
([nav-solutions](components/crops/nav-solutions-default.png), opened:
[nav-solutions-open](components/crops/nav-solutions-open-opened.png) and
[home-light-solutions-menu](screenshots/home-light-solutions-menu.png)), then a
white hairline **Sign in** and the near-black **Book a demo** pill — all controls
36px tall with a 7px radius. Above it sits the announcement strip on a
`#f9fafb` ground carrying the coral "NEW" chip
([announcement-bar](components/crops/announcement-bar-default.png)). At 390px the
bar is 72px with a 36px menu button that opens a full stacked sheet
([m-menu-open](components/crops/m-menu-open-opened.png),
[mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png)).

## CTA vocabulary

Two button recipes repeat on every route: the near-black `#111827` fill with
white text — 36px nav size ([nav-cta](components/crops/nav-cta-default.png)),
36px hero size ([cta-request](components/crops/cta-request-default.png)), the
wide 320px pricing row ([plan-cta](components/crops/plan-cta-default.png)) and
the navy sign-in submit ([signin-submit](components/crops/signin-submit-default.png),
`#0a4481`) — and the white hairline ghost at the same 36px/7-8px recipe
([nav-signin](components/crops/nav-signin-default.png),
[signin-google](components/crops/signin-google-default.png)). Pressed states
keep the fill; the Intercom launcher is the one round accent
([intercom-launcher](components/crops/intercom-launcher-default.png), `#0071b2`).

## Hero and announcement

The hero sets a two-line Inter Display headline at 96px/800
([hero-title](components/crops/hero-title-default.png)) over a quiet subtitle,
above a logo wall of customer wordmarks. Section headlines stay Inter Display at
42px/700 ([section-title](components/crops/section-title-default.png)). The
announcement strip is the site's one loud accent: a coral "NEW" chip on the
flame ramp (`#fc4a2b` family) next to a plain sentence.

## Stories and coach

Below the hero the home page runs a customer-stories carousel whose pagination
is a row of "Scroll to page N" dots ([carousel-dot](components/crops/carousel-dot-default.png))
and a working "Ask Coach" demo box — both mount only while their band is on
screen, so they were hunted by a scroll sweep; the 320px widget and its round
24px send button were measured, never pressed, while the demo's ask field is
a painted placeholder rather than a real input and is recorded missing.
Feature sections use tall ~367 x 600px image cards
linking the feature pages ([feature-card](components/crops/feature-card-default.png)),
measured, never followed.

## Pricing

/pricing opens with the same 96px/800 display headline
([pricing-title](components/crops/pricing-title-default.png)) and lays the
plans out as 384 x 594px white cards with a layered natural shadow and a 24px radius
([plan-card](components/crops/plan-card-default.png)), each carrying the wide
320px black plan CTA. See [pricing-light-full](screenshots/pricing-light-full.png).

## Forms

The sales page (/contact/sales) stacks 19-38px fields on a tinted ground
([contact-field](components/crops/contact-field-focused.png),
[contact-message](components/crops/contact-message-default.png)) under the black
submit. /sign-in is a centred card of 384px controls: hairline Google/SSO
ghosts, two 38px fields with oklab-grey borders
([signin-field](components/crops/signin-field-focused.png)), the navy submit
and a muted forgot link — everything measured, nothing submitted. See
[signin-light-default](screenshots/signin-light-default.png).

## Footer

A `#f9fafb` block ([footer](components/crops/footer-default.png), 1539px) of
link columns ([footer-link](components/crops/footer-link-default.png)), 36px
social icon buttons ([footer-social](components/crops/footer-social-default.png)),
an app-store rating row ([footer-rating](components/crops/footer-rating-default.png))
and the muted legal line ([footer-legal](components/crops/footer-legal-default.png)).
