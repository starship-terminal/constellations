# Bio Sites patterns

How the measured components combine on biosites.com's public surface, read
from the screenshots and the component entries in
[components.md](components.md). The site paints one light theme — white
sections over a black page body; all values are from the light set unless
noted.

## The shell

A fixed `#navbar` div (not a header element) floats over the black hero
collage at 1440 x 97 with 40px of headroom
([home-light-default](screenshots/home-light-default.png)): the BIO.SITES
wordmark + "FROM SQUARESPACE" tagline left
([logo](components/crops/logo-default.png), 203 x 57), and a right cluster of
40px-tall, 40px-radius white pills — BLOG
([nav-link](components/crops/nav-link-default.png), 81 x 40), LOG IN
([nav-login](components/crops/nav-login-default.png), 89 x 40) and SIGN UP FOR
FREE ([nav-signup](components/crops/nav-signup-default.png), 155 x 40), all in
Clarkson 12px/500 small caps. Every pill inverts on hover and press — white
fill to black, black text to white. At 390px the bar shrinks to 64px, drops
BLOG and LOG IN, and keeps a black "SIGN UP" pill
([m-signup](components/crops/m-signup-default.png)); there is no hamburger and
no menu to open.

## The page body

The body paints `#000000` end to end
(`page-ground` in [components.md](components.md)); the white content is sections laid over
it. The hero is a two-part band: a tilted collage of persona-link screenshots
on the black, then a white strip carrying the Clarkson 35/500 headline "Your
brand, your storefront, one link."
([hero-title](components/crops/hero-title-default.png), 355 x 70), the `#6a6a6a`
subcopy ([hero-sub](components/crops/hero-sub-default.png), Clarkson 21/29)
and the CTA.

## CTA vocabulary

One recipe repeats: a black pill that inverts to white with a `#e6e6e6`
hairline on hover and press. The hero instance is the biggest — "Create a
free Bio Site" at 325 x 80 on a 46px radius, Clarkson 21px
([cta](components/crops/cta-default.png) /
[cta-hover](components/crops/cta-hover.png)) — and the same button recurs down
the page and at 64px in the mobile hero
([m-cta](components/crops/m-cta-default.png)). The nav pills run the same
inversion on a smaller 40px scale. Inside the persona carousel the recipe
softens: the card's "Get started ↗" link is a `rgba(0,0,0,0.25)` scrim pill
(305 x 46) that darkens to `rgba(0,0,0,0.5)` on hover
([card-cta](components/crops/card-cta-default.png)).

## Sections and the marquee

Four anchor links — STAND OUT / SELL / CONNECT / ANALYZE — ride a black band
in Clarkson 70/500 white caps with a 10px white dot bullet
([section-nav-link](components/crops/section-nav-link-default.png), 380 x 70);
they jump to the white content sections, each headed by a Clarkson 18/400
title ([section-title](components/crops/section-title-default.png)) — the same
family and weight logic repeats at every scale, from the 12px nav caps to the
70px marquee. An eyebrow label in 18.72px/500 caps ("TRUSTED BY MILLIONS OF")
sits over the persona carousel
([eyebrow](components/crops/eyebrow-default.png)). The carousel cards are the
one coloured surface: 325 x 480 with a 20px corner over `#4f566f` slate,
holding a white template preview and the scrim CTA
([persona-card](components/crops/persona-card-default.png)); the strip never
stops sliding, so the card-cta hover in the raw file is CDP-forced.

## Claim screen

`/editor` redirects to the signed-out claim page on a `#fafafa` ground with a
blurred collage behind it
([claim-light-default](screenshots/claim-light-default.png)): a Clarkson
32/400 `#1b1b1b` title "Claim your free username"
([claim-title](components/crops/claim-title-default.png)), then one component
— a 652 x 102 pill on a 50px radius with a `rgba(0,0,0,0.2)` hairline
([claim-field-wrap](components/crops/claim-field-wrap-default.png)) holding
the `bio.site/` prefix, the username input at Clarkson 36px with a `#9c9c9c`
placeholder ([claim-field](components/crops/claim-field-default.png)) and a
53px circular `#2a2a2a` arrow submit that sits at 0.2 opacity until the field
has text ([claim-submit](components/crops/claim-submit-default.png)). The
"Log In" pill top right is a 40px white pill on a 20px radius with a
`0 20px 60px rgba(0,0,0,0.24)` lift
([claim-login](components/crops/claim-login-default.png)); it and the claim
footer's 10px `#9c9c9c` legal links are the only components to show a visible
focus state — the browser's `auto` `#005fcc` ring
([claim-login-focus-visible](components/crops/claim-login-focus-visible.png)).
The field was never submitted.

## FAQ and footer

The FAQ is a static `<dl>` — every question row paints Clarkson 21/29 in
black with its answer always visible; there is no accordion state to measure
([faq-item](components/crops/faq-item-default.png)). The footer runs 673px of
white: the "BUILD YOUR FREE LINK IN BIO PAGE" CTA, then the giant
"BIO.SITE/YOURNAME ↗" call linking to /editor
([footer-cta](components/crops/footer-cta-default.png), 777 x 98), link
columns in Clarkson 18/500 ([footer-link](components/crops/footer-link-default.png))
and muted legal links ([footer-legal](components/crops/footer-legal-default.png))
under [footer](components/crops/footer-default.png).
