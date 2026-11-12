# Cake Equity patterns

How the measured components combine on cakeequity.com's public surface, read
from the screenshots and the component entries in
[components.md](components.md). The site is light-only; the two dark looks —
the `#18161a` footer and the `#0e0d12` Cake-MCP band — are regions painted on
the light page, not a theme. Values are from the light set unless marked
`dark`.

## The fixed navbar

Every marketing page carries the same chrome
([header](components/crops/header-default.png), 74px high, fixed): a white
bar with a near-invisible `rgba(0,0,0,0.2) 0 2px 20px -19px` drop holding the
`cake.` wordmark ([logo](components/crops/logo-default.png), 100 x 32), the
`Product`, `Solutions`, `Resources` and `Customers` mega-nav triggers
([nav-trigger](components/crops/nav-trigger-default.png), Inter 14/18.2
`#222`), the plain `Pricing` link
([nav-link](components/crops/nav-link-default.png) — `#222` that turns brand
`#4823ff` on hover), then a 50px-radius `Login` pill
([nav-login](components/crops/nav-login-default.png)), a violet-outlined
`Book a demo` ghost ([nav-demo](components/crops/nav-demo-default.png)) and
the 100px violet `#4823ff` `Get started free` pill
([nav-cta](components/crops/nav-cta-default.png), 44px high). Every fill
darkens to `#2b1599` on hover and press over 0.2s. The triggers open a
white 20px-radius mega-panel
([nav-dropdown](components/crops/nav-dropdown-default.png), 1008px wide,
`rgba(24,22,26,0.25) 0 0 20px -5px`) of feature links
([menu-link](components/crops/menu-link-default.png), Inter 16.8/26.9 600 —
hover paints the 10% plum wash `rgba(126,120,255,0.1)`);
[home-light-menu](screenshots/home-light-menu.png) shows it open. Keyboard
focus draws the 1px auto `#005fcc` Webflow/UA ring at ~1px offset on every
chrome item.

## The home hero

The home page opens on white with the announcement chip
([announce-pill](components/crops/announce-pill-default.png)): a 37px white
100px pill on a 1px `#ebe8f2` border — `Pulley is shutting down · How
managed migration works →` — whose tag segment paints an olive-to-rust
linear gradient. Then the 60px `The equity platform for growing startups`
display headline in Exposure Light at 60/66, -2px tracking, weight 400
([hero-title](components/crops/hero-title-default.png)), a 20/32 Inter 300
lede ([hero-sub](components/crops/hero-sub-default.png)) and the paired
actions: the violet `Get started free`
([hero-cta](components/crops/hero-cta-default.png), 59px high) beside the
transparent violet-ringed `Book a demo`
([hero-demo](components/crops/hero-demo-default.png)) — the ghost fills
`#2b1599` on hover over 0.4s instead of the primary's 0.2s. Sections below
open on small-caps Inter 600 eyebrows
([eyebrow](components/crops/eyebrow-default.png), 16/19.2 +0.8px at 50%
ink) and 44/44 Exposure heads ([section-h2](components/crops/section-h2-default.png)).

## The dark band

Mid-page, the Cake-MCP section inverts: a `#0e0d12` panel inset at a 28px
radius ([dark-section](components/crops/dark-section-default.png), 1296 x
635) carrying lemon `#e7ff6e` `dark` eyebrows (`CAKE MCP`, 14px 600 +0.7px
caps), white copy and rows separated by `rgba(244,244,244,0.18)` `dark`
hairlines. It is the only dark surface besides the footer — the site's one
break from the white/plum scheme.

## Pricing

`/pricing` heads `Growth-friendly pricing, no complexity` at the same 60px
([pricing-h1](components/crops/pricing-h1-default.png)). The controls sit
in one row: a 200px white region `<select>` on a 100px pill
([country-select](components/crops/country-select-default.png), 1px
`#d9d9e0` border that turns `#3898ec` on focus — geo-defaulted to Singapore
in this capture) and the Yearly/Quarterly switch
([billing-toggle](components/crops/billing-toggle-default.png)): a 236px
white 999px rail on the same field border whose active half paints an ink
`#18161a` pill with a white label, a mint `#c6f0dc` `-20% save` pill riding
beside it. The plan grid holds white cards
([plan-card](components/crops/plan-card-default.png), 312 x 741): a
`#faf9ff` violet-tinted header under a 1px 10%-ink hairline, the plan name
at Inter 20/24 500, the price figure at 40/40 -1.6px
([plan-price](components/crops/plan-price-default.png)), and the violet
Start-free pill ([plan-cta](components/crops/plan-cta-default.png), 49px).
The featured tier swaps the header for an `#ede9ff` `Most popular` ribbon
([plan-badge](components/crops/plan-badge-default.png), 13px plum on the
tint) and draws a 1px 25% plum border. The hidden `.pp-hidden-fields`
calculator inputs behind the select are recorded missing, not painted
([calc-field](components.md)); the Quarterly state is in
[pricing-light-quarterly](screenshots/pricing-light-quarterly.png).

## Blog, features and demo

`/blog` heads `Cake blog` at 60px
([blog-h1](components/crops/blog-h1-default.png)) over collection cards —
the featured post a 693 x 696 frame whose image sits in a white 30px-radius
wrap ([collection-card](components/crops/collection-card-default.png)) and
whose title runs Exposure 44/44 -1px. `/features/cap-table` is one of ~25
sibling feature pages on the same template: the same 60px Exposure head
([feature-h1](components/crops/feature-h1-default.png)). `/demo-request`
pairs its `Discover why growing teams are switching to Cake.` head
([demo-h1](components/crops/demo-h1-default.png)) with the HubSpot form
embed ([demo-form](components/crops/demo-form-default.png)): a white 600px
card at a 20px radius whose inner fields are cross-origin third-party
paint — measured as a region, never filled.

## The hosted login

`app.cakeequity.com/login` redirects to Kinde-hosted auth
(authentication.cakeequity.com): a 496 x 609 white card at 16px on a light
grey page ([login-card](components/crops/login-card-default.png)) with a
24/32 -0.48px `Welcome back` ([login-title](components/crops/login-title-default.png)),
the 48px email field on a 1px `#ababab` border at 8px
([login-field](components/crops/login-field-default.png)), the `#5a38fd`
Continue button at 8px ([login-cta](components/crops/login-cta-default.png)
— a violet close to but not the marketing `#4823ff`), the `#f5f5f5` Google
and LinkedIn OAuth buttons ([login-oauth](components/crops/login-oauth-default.png),
hover `#ebebeb`, pressed `#dbdbdb`) and the `#1c029d` `Create one` link
([login-link](components/crops/login-link-default.png)). Focus draws a 2px
solid `#0054f0` ring offset 2px — a different ring than the marketing
pages' 1px auto `#005fcc`.

## The footer

Pages close on the `#18161a` footer
([footer](components/crops/footer-default.png), 659px): the office line,
link columns in Inter 16/16 300 white
([footer-link](components/crops/footer-link-default.png)) that turn
`#7e78ff` `dark` on hover, and social glyphs
([social-icon](components/crops/social-icon-default.png)).

## Mobile

At 390 the page forces a ~745px layout viewport —
`.comparison-grid{min-width:700px}` plus navbar chrome — so the real phone
experience is a horizontal pan
([mobile-home-light-default](screenshots/mobile-home-light-default.png)):
the 68px header ([m-header](components/crops/m-header-default.png)) keeps
the wordmark at left while the 48px hamburger
([m-menu-button](components/crops/m-menu-button-default.png), 4px radius)
sits at x~660 outside the 390 visual viewport. The opened menu is the
Webflow overlay ([mobile-home-light-menu](screenshots/mobile-home-light-menu.png)).
The display compresses to 52/57.2 ([m-hero](components/crops/m-hero-default.png)).

## Boundaries

The equity-management app — cap table, grants, scenario models, documents,
stakeholders, reports — sits behind app.cakeequity.com and was never
reached. The login card was captured as a surface, never filled or
submitted; every Get-started-free, Start-free and Book-a-demo action was
measured, never followed; the HubSpot embed is third-party paint. See the
Gaps section in [components.md](components.md).
