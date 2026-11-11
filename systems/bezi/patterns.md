# Bezi patterns

How the measured components combine on bezi.com's public surface, read
from the screenshots and the component entries in [components.md](components.md).
The site paints one dark theme; all values are from the dark set unless noted.

## The shell

A floating pill header over the `#0d0d0d` starfield
([home-dark-default](screenshots/home-dark-default.png)): a translucent
`rgba(31,31,31,0.84)` bar with a 144px corner holding the BEZI ghost mark
([logo](components/crops/logo-default.png), 107 x 19), text links Studios /
Product / Pricing / Blog / Docs / Discord
([nav-link](components/crops/nav-link-default.png), 38px controls) and the
orange **TRY FOR FREE** pill ([cta](components/crops/cta-default.png), 154 x 39).
Under it a `#1c1c1c` announcement strip carries the orange "NEW" chip and the
"Bezi for Unreal Engine" line ([announcement](components/crops/announcement-default.png),
644 x 32). At 390px the bar holds the mark and a 14px hamburger that opens a
stacked menu sheet ([m-menu-open](components/crops/m-menu-open-opened.png),
[mobile-home-dark-menu-open](screenshots/mobile-home-dark-menu-open.png)).

## CTA vocabulary

One recipe repeats on every route: the `#f84503` orange fill with white text —
the 154 x 39 header pill ([cta](components/crops/cta-default.png)), the hero
button under the headline, and the near-black `rgba(0,0,0,0.84)` 127 x 48
variant inside the pastel Free band
([plan-cta](components/crops/plan-cta-default.png)). Secondary actions are
translucent white fills with a pixel-art orange arrow
([view-all](components/crops/view-all-default.png), `rgba(255,255,255,0.2)`,
110 x 43). Pressed states keep the fill; hover lifts the tools chip's corner
ticks a few pixels ([tools-button](components/crops/tools-button-hover.png)).

## Hero and announcement

The hero sets a two-line headline in The Future Medium at 53px/500 — "AI for
building real games, / not generating them."
([hero-title](components/crops/hero-title-default.png)) — over an
`rgba(255,255,255,0.5)` subtitle ([hero-sub](components/crops/hero-sub-default.png)),
with the orange CTA below and an animated product-window mock under the fold.
Section headlines stay compact at ~36px
([section-title](components/crops/section-title-default.png)). Feature
sections are indexed by corner-tick chips — "02. CONNECTED TOOLS" and siblings
— that draw their box as four 19px corner borders in
`rgba(242,241,236,0.32)` ([tools-button](components/crops/tools-button-default.png)).
The announcement strip is the site's one loud accent: an orange "NEW" chip on
a `#1c1c1c` bar under the header.

## Pricing

/pricing opens with an Inter Display title at 64px/500
([pricing-title](components/crops/pricing-title-default.png)) and an
Individual/Studio billing toggle — a dark segmented control with the selected
half in white ([pricing-dark-default](screenshots/pricing-dark-default.png)).
The Free trial band is the palette's loudest pastel: `color.pastel.sky`
`#7dadd1` with a near-black CTA, above three ink plan columns ($20 / $60 /
$180) whose RECOMMENDED middle column rings in orange
([plan-card](components/crops/plan-card-default.png), 366 x 499).

## Footer

A link grid over the same ground — Product, Company, socials
([footer](components/crops/footer-default.png)) — in the off-white
`#f2f1ec` at 50-100px links ([footer-link](components/crops/footer-link-default.png)),
36px social glyphs ([footer-social](components/crops/footer-social-default.png),
hover swells to ~40px) and muted legal links
([footer-legal](components/crops/footer-legal-default.png)). The closing band
above it joins a pastel CTA card with the wordmark
([home-dark-full](screenshots/home-dark-full.png)).
