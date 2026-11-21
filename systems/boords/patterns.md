# Boords patterns

How the measured components combine on boords.com's public surface, read from
the screenshots and the component entries in [components.md](components.md).
The site paints one light theme over a white field; the footer is a near-black
section, not a second theme. All values are from the light set unless noted.

## The floating header

Every page opens under a floating white pill bar
([home-light-default](screenshots/home-light-default.png)): the header
([header](components/crops/header-default.png)) sits inset with a 9999px
radius and a soft white shadow, carrying the wordmark
([logo](components/crops/logo-default.png)), muted-ink nav links in matter
14.4px ([nav-link](components/crops/nav-link-default.png)) — Features ·
Resources · Success Stories · Pricing — a nav-menu-trigger that opens a
flyout ([nav-trigger-open](components/crops/nav-trigger-open-opened.png)),
and a dark `#121212` Try Boords Free CTA
([cta-demo](components/crops/cta-demo-default.png)) that fades to a 5% ink
fill on hover. Features and Resources open on hover
([home-light-features-menu](screenshots/home-light-features-menu.png),
[home-light-resources-menu](screenshots/home-light-resources-menu.png)).
On a phone, Open menu opens a near-black drawer
([mobile-home-light-menu](screenshots/mobile-home-light-menu.png)).

## The hero

The home hero centres a 64px matter display headline in ink
([hero-title](components/crops/hero-title-default.png)) over a grey lede
([hero-sub](components/crops/hero-sub-default.png)) and the action: a pill
outlined with a 1px amber `#e8aa42` border
([hero-cta](components/crops/hero-cta-default.png)) that darkens to `#d89b3c`
on hover. Below, feature sections alternate white and the `#f3f3e9` cream
card field ([feature-card](components/crops/feature-card-default.png), 24px
radius) with screenshots of the product; there are no heavy card borders —
whitespace and the ink/amber contrast do the work.

## Pricing

`/pricing` pairs a display title
([price-title](components/crops/price-title-default.png)) with a segmented
Monthly/Yearly tab ([billing-tab](components/crops/billing-tab-default.png),
white pill on a grey rail; toggled for
[pricing-light-yearly](screenshots/pricing-light-yearly.png)) and a row of
white 24px plan cards
([plan-card](components/crops/plan-card-default.png)) — Solo $39/$26, Pro
$69/$50, a tier each for Team and Enterprise — each holding a 20px ink price
figure ([plan-price](components/crops/plan-price-default.png)) and a pill CTA
with a heavy 3px `#121212` outline
([plan-cta](components/crops/plan-cta-default.png)). A feature comparison
sits below as accordion rows
([feature-row](components/crops/feature-row-default.png)) that open inline
([feature-row-open](components/crops/feature-row-open-opened.png)).

## The public script timer

`/script-timer` is a working free tool signed out
([script-timer-light-default](screenshots/script-timer-light-default.png)):
a big white textarea on a 16px radius
([timer-field](components/crops/timer-field-default.png)) takes a pasted
script ([script-timer-light-with-script](screenshots/script-timer-light-with-script.png)
shows it filled; the sample text was typed and cleared, never submitted) and
aria-pressed option toggles
([timer-toggle](components/crops/timer-toggle-default.png)) switch the
reading model — white fills on a 1px `rgba(18,18,18,.15)` hairline, 16px
radii.

## The footer

Every page ends in a near-black section
([footer](components/crops/footer-default.png)): the wordmark, link columns
in white matter ([footer-link](components/crops/footer-link-default.png)) —
Product · Features · Resources · Company · Social — a social icon row
([social-icon](components/crops/social-icon-default.png)) and legal, on
inner fills of `rgba(255,255,255,.1)`/`.06`.

## The mobile menu

At 390 the header compresses to the round menu button
([m-menu-button](components/crops/m-menu-button-default.png)); its own toggle
opens a full overlay ([mobile-home-light-menu](screenshots/mobile-home-light-menu.png)):
nav items as white pills ([m-nav-item](components/crops/m-nav-item-default.png))
over the near-black chrome, a mirror of the desktop menu. The script timer
and every page scale down the same way
([mobile-script-timer-light-default](screenshots/mobile-script-timer-light-default.png)).

## The signup and login shells

`/signup` on www 404s — the real signup lives on app.boords.com — and `/login`
renders the shell without form fields for this client. Both are boundaries:
the app is the product, and it sits behind login. /demo shows a 25-minute
call pitch over an embedded scheduler, never interacted with.
