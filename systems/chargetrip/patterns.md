# Chargetrip patterns

How the measured components combine on chargetrip.com's public surfaces,
read from the screenshots and the component entries in
[components.md](components.md). The site paints one light theme — a warm
`#efede5` cream ground — with dark islands inside it; all values are from
the light set unless noted.

## The header and the Products flyout

Every marketing page opens under a 64px bar
([home-light-default](screenshots/home-light-default.png)) on the cream
ground: the wordmark anchor
([logo](components/crops/logo-default.png)) left, text nav items at 18px
Geist that pick up a translucent orange wash
(`rgba(221, 59, 0, 0.15)`, 24px-radius) on hover
([nav-item](components/crops/nav-item-hover.png)), and two 40px pills
right — the outlined **Sign in**
([nav-signin](components/crops/nav-signin-default.png)) and the dark
`#262322` **Contact sales**
([nav-cta](components/crops/nav-cta-default.png)). The **Products** item is
a menu trigger whose own press opens a 1376x816 mega panel — grouped link
cards (the No-code card is 453x776) on the cream field and a green status
dot
([menu-panel](components/crops/menu-panel-default.png),
[menu-card](components/crops/menu-card-default.png), the open state in
[home-light-menu](screenshots/home-light-menu.png)). Keyboard focus draws
a 1px auto outline — `#101010` on the header and footer controls,
`#005fcc` on the plan, slider and form controls, an oklch ring on the
sign-in pair.

## The hero band — the dark island

The home hero is a dark `#262322` band inside the cream page
([home-light-default](screenshots/home-light-default.png)): the 88px/78
Cirka headline in `#f4f3f2`
([hero-title](components/crops/hero-title-default.png)) over a lede in
52%-alpha warm white ([hero-sub](components/crops/hero-sub-default.png)),
then a CTA pair — the 48px orange **Book a demo**
([cta-accent](components/crops/cta-accent-default.png), 8px radius, with
two decorative orange discs painted behind the group) and the 48px
`#44403f` **Plan a route**
([cta-dark](components/crops/cta-dark-default.png)). Marketing CTAs do not
repaint on hover or press; the action read is all in the colour choice.
Sections below switch back to ink-on-cream at the 48px/48 step
([section-title](components/crops/section-title-default.png)).

## The pricing surface

/pricing/api keeps the dark-island headline ("Build for free and go live
with the best plan for you.", 88px Cirka,
[pricing-h1](components/crops/pricing-h1-default.png)) over a dark
customer-logo strip ([logo-chip](components/crops/logo-chip-default.png),
with a dashed `#44403f` baseline), then the plan columns: near-white
`#fffffb` 24px-radius cards ([plan-card](components/crops/plan-card-default.png))
next to the dark `#262322` 16px "Standard" card under the **Most popular**
tag ([plan-card-dark](components/crops/plan-card-dark-default.png),
[popular-tag](components/crops/popular-tag-default.png)). Prices are set
in Cirka at 48px; the dashed hairlines inside are `#e4e1d5` on the light
card and `#4d4846` on the dark one. Each card's 40px action is either the
orange **Get started** ([plan-cta](components/crops/plan-cta-default.png))
or a dark fill ([plan-cta-dark](components/crops/plan-cta-dark-default.png)).
A 313x12 usage slider estimates volume with a two-tone track — orange to
the thumb, `#44403f` past it
([range-slider](components/crops/range-slider-focused.png)) — and the
plan features list rows are 16px/22.4 check items
([check-item](components/crops/check-item-default.png)).

## The contact-sales form

/contact/sales pairs a 64px Cirka headline ("Grow your business with
routing.") with the only real form on the public surface: 40px fields —
text, email, tel, a styled select and a textarea
([form-input](components/crops/form-input-focused.png),
[form-select](components/crops/form-select-focused.png)) — a dark 40px
10px-radius **Submit** ([form-submit](components/crops/form-submit-hover.png),
which lifts `#262322` to `#59524f` on hover) and the white 12px-radius
"Book a demo · 30 minutes" card beside it
([demo-card](components/crops/demo-card-hover.png), with a 1.5px
`#fffffb` ring shadow on its icon). Fields were focused and typed, never
sent; the form's own field text is a near-black teal `rgb(7, 28, 31)`,
outside the ink ramp.

## The sign-in card — a second stack

account.chargetrip.io/sign-in is a different build: Tailwind v4 with
oklch colours and Geist for UI text, not the Framer bundle. Its 48px headline in
`Cirka, serif` sits on a cream-ish `oklch(0.9492 ...)` surface
([signin-h1](components/crops/signin-h1-default.png)); the 46px email
field focuses with a ring ([signin-input](components/crops/signin-input-focused.png)),
the dark **Continue** lightens to `oklch(0.8244 ...)` and shrinks to
scale(0.97) on press
([signin-continue](components/crops/signin-continue-pressed.png)), and the
secondary **Create account** is an outlined 40px action
([signin-create](components/crops/signin-create-default.png)). A
check-marked reassurance row runs under the panel
([signin-trust](components/crops/signin-trust-default.png)). The card was
measured and filled with a documented test address, never submitted —
everything past it is the authenticated boundary.

## The footer

The footer is a near-white 481px panel with 24px top corners floating on
the cream page ([footer](components/crops/footer-default.png)): muted
`#877f78` meta text and 16px/22.4 ink link columns
([footer-link](components/crops/footer-link-hover.png)) whose hover and
press both flip to the orange accent, social icons that do the same
([footer-social](components/crops/footer-social-hover.png)), the
newsletter **Sign up** action
([newsletter-cta](components/crops/newsletter-cta-default.png)) and the
"● Stable" status line with its `rgb(39, 136, 89)` green dot
([status-pill](components/crops/status-pill-default.png)).

## The mobile surface

At 390 wide the header compresses to the wordmark and an icon-only menu
trigger ([m-header](components/crops/m-header-default.png),
[m-menu-button](components/crops/m-menu-button-default.png)); its press
opens a full-height cream overlay of grouped cards
([m-menu-open](components/crops/m-menu-open-default.png),
[m-menu-card](components/crops/m-menu-card-default.png), the open state in
[mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png)).
The hero type steps down to fit ([m-hero](components/crops/m-hero-default.png))
and the same cream/ink/orange tokens carry every panel — no mobile-only
palette exists.
