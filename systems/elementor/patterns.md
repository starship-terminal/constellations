# Elementor patterns

How the measured components combine on elementor.com's public signed-out
surface, read from the screenshots and the component entries in
[components.md](components.md). The surface paints light on a strict
Kernel-Black / Blank-Canvas-White axis, carrying `.dark-mode` islands —
the photo hero, the dark card sections and the footer — where the same
named vars re-bind to their opposites. No colour rests anywhere: every
action is black (or white inside an island) until hover, when it floods
Neon-Loop `#ed01ee`.

## The chrome: a floating white pill

Every page opens on a header that is not a bar but a pill
([header](components/crops/header-default.png), 1248 x 72 on desktop,
358 x 64 on mobile): a white 24px-radius lozenge floating over the page
under a single soft shadow (`#000000 @ 5%`, 15px blur, 3px spread —
`core.shadow.header`). Inside: the Elementor wordmark
([logo](components/crops/logo-default.png), 184 x 32), the Products
mega-menu trigger and the Agency / Enterprise / Pricing / App-Builder
links — 16/22.4 Roobert rows in `#212121` that take a Syntax-Glow
`#fae4fa` tint at an 8px radius on hover
([nav-trigger](components/crops/nav-trigger-hover.png),
[nav-link](components/crops/nav-link-default.png)) — then the `En`
language selector, `Log in` as a plain link
([nav-login](components/crops/nav-login-default.png)) and `Get started`
as a black 48px pill at an 8px radius
([nav-cta](components/crops/nav-cta-default.png), 144 x 48, Roobert
18/25.2 500). The CTA's hover is the system's signature: the black fill
rebounds to Neon-Loop with no intermediate state.

The Products trigger opens a full-width mega-menu
([nav-dropdown](components/crops/nav-dropdown-default.png),
[home-light-menu](screenshots/home-light-menu.png)): the same white fill,
radius and shadow as the header it drops from, holding product link
columns (250 x 84 rows at 8px, `#fae4fa` on hover,
[menu-link](components/crops/menu-link-hover.png)) beside a featured tile
that paints the Codeberry gradient `297° #620856 → #1b0317`
([menu-feature](components/crops/menu-feature-default.png), 343 x 204).

## The dark hero island

The home hero is a `.dark-mode` island over a black photo stage
([home-light-default](screenshots/home-light-default.png)): the 88/96.8
Roobert 600 headline at -0.88px tracking paints white through the
re-bound vars ([hero-title](components/crops/hero-title-default.png)),
the 20/28 lede sits at `#f6f6f6`
([hero-lede](components/crops/hero-lede-default.png)), and Get started
inverts — the identical pill component now fills Blank-Canvas-White with
Kernel-Black text ([hero-cta](components/crops/hero-cta-default.png),
140 x 48), still rebounding to Neon-Loop with white text on hover. The
dark sections below the hero reuse the same island: black 16px-radius
tiles ([card](components/crops/card-default.png), 400 x 184, 24px
padding) with `#f6f6f6` text and 14/19.6 icon-list rows
([icon-item](components/crops/icon-item-default.png)).

Back on the light ground, calls to action repeat the same black pill
([cta-dark](components/crops/cta-dark-default.png)) — the system has
exactly one primary button shape (48px tall, 8px radius, 0/24 padding,
Roobert 18 500) whose fill flips between Kernel-Black and
Blank-Canvas-White by scope.

## Pricing

/pricing ([pricing-light-full](screenshots/pricing-light-full.png)) sets
a 20/26 Roobert 500 page title
([pricing-h1](components/crops/pricing-h1-default.png)) over a row of
white plan cards ([plan-card](components/crops/plan-card-default.png),
297 x 1024 at an 8px radius with a 1px `#d1d1d1` border — the one place a
card takes a real border). Each card stacks a 20/32 600 plan name
([plan-name](components/crops/plan-name-default.png)), a 40/40 600 price
([plan-price](components/crops/plan-price-default.png)), the Buy-now
action and the feature list. Two controls are distinctive:

- **Buy now** is the outline twin of the primary pill: 247 x 56 at 8px,
  transparent with a 2px Kernel-Black ring
  ([plan-cta](components/crops/plan-cta-default.png)), filling Neon-Loop
  on hover ([plan-cta](components/crops/plan-cta-hover.png)).
- **The variant toggle** is a grey well (`#ebebeb`) holding 34px white
  pills at 8px ([plan-toggle](components/crops/plan-toggle-default.png),
  Roobert 16/34 700) — measured, never switched into a purchase.

Feature rows are 14/19.6 `#212121` with a drawn check ::before
([feature-row](components/crops/feature-row-default.png),
[pricing-light-plans](screenshots/pricing-light-plans.png)).

## The contact popup

/contact ([contact-light-full](screenshots/contact-light-full.png))
grids 400 x 280 option cards at a 16px radius on Grey-200 `#f6f6f6`
([contact-card](components/crops/contact-card-default.png)); hover drops
the fill and draws a 1px black ring instead
([contact-card](components/crops/contact-card-hover.png)). A card opens
an Elementor popup dialog
([contact-light-form](screenshots/contact-light-form.png),
[form-popup](components/crops/form-popup-default.png), 602 x 721) —
white, carrying 40/52 900 display type over a form of 40.4px fields:
1px `#d1d1d1` borders at a 4px radius that tighten to black with a
`#e2e2e2` 6px glow on focus
([field-name](components/crops/field-name-focused.png),
[field-message](components/crops/field-message-default.png) at
107.6px tall), a 16px acceptance checkbox
([checkbox](components/crops/checkbox-selected.png)) and the black 48px
Submit ([submit-btn](components/crops/submit-btn-default.png)). Nothing
was sent; the name field was sample-filled and deleted.

## FAQ

/faq ([faq-light-full](screenshots/faq-light-full.png)) opens on the
72/79.2 Roobert 600 title at -0.72px
([faq-h1](components/crops/faq-h1-default.png)). Each accordion row is a
1024px 20/28 700 question in `#212121` with an 80px right pad and a drawn
plus ::after ([faq-item](components/crops/faq-item-default.png)); the row
keeps its shape open
([faq-item-open](components/crops/faq-item-open-default.png),
[faq-light-open](screenshots/faq-light-open.png)) while the answer
expands on a 0.5s grid-template-rows transition
([faq-answer](components/crops/faq-answer-default.png)).

## The footer: the last dark island

The dsm-footer is the third island
([footer](components/crops/footer-default.png), 1440 x 672, 96px side
padding on Kernel-Black): white wordmark gradients, 14px link columns in
`#f6f6f6` ([footer-link](components/crops/footer-link-default.png)) and
social glyphs ([social-icon](components/crops/social-icon-default.png)).
Links transition background-colour at 0.2s like every CTA.

## Mobile

At 390 x 844 the chrome compacts but keeps its shape
([mobile-home-light-default](screenshots/mobile-home-light-default.png)):
the same floating pill at 358 x 64
([m-header](components/crops/m-header-default.png)), the wordmark
shrunk to 144 x 28, and an `e-n-menu-toggle` hamburger
([m-menu-button](components/crops/m-menu-button-default.png)) that opens
a full-height white sheet
([m-menu-open](components/crops/m-menu-open-default.png), 390 x 844 at
8px radius, [mobile-home-light-menu](screenshots/mobile-home-light-menu.png))
of 52.6px rows separated by `#d1d1d1` bottom hairlines
([m-nav-item](components/crops/m-nav-item-default.png)). The hero
compacts to the same black island
([m-hero](components/crops/m-hero-default.png)); pricing stacks the plan
cards full-width
([mobile-pricing-light-full](screenshots/mobile-pricing-light-full.png)).

## The state signature

Two moves carry every interaction: **fills rebound to Neon-Loop**
(every primary action — nav CTA, hero CTA, dark CTA, plan CTA, submit —
goes `#ed01ee` on hover and pressed; on keyboard focus they all do the
same except the submit, which keeps its black fill under the focus
ring), and **rows tint Syntax-Glow** (`#fae4fa` under hovered menu links
and nav triggers — a desktop pattern; the measured mobile menu item
stays white on hover, only its chevron glyph darkening). Focus draws a
2px auto `#005fcc` outline offset 2px on every control focus could be
landed on (16 of 17 attempted; `faq-item` and the checkbox ring at 1px;
the mobile nav item's ring lands on its child dropdown button, not the
row). The nav trigger never took keyboard focus in headless Chromium —
recorded as a failed state, not a no-ring reading. Motion is short: 0.2s
ease on button fills, 0.3s on links and toggles, 0.4s transforms on the
accordion marker, 0.5s on the answer's height.

## Boundaries

Everything past auth was never reached: the Elementor editor and the
my.elementor.com dashboard sit behind Log in and Get started (both
measured, never followed); Buy now would open checkout and was never
pressed; the contact submit was measured, never pressed; the Cookiebot
consent dialog was hidden per capture, never answered; the Angie chat
widget and promo popup were closed or hidden. What this package covers is
the marketing surface — the editor's own design system remains unknown.
