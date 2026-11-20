# Care.com patterns

How the measured components combine on care.com's public signed-out surface,
read from the screenshots and the component entries in
[components.md](components.md). One theme paints: the white canvas with the
deep-green `#025747` and lime `#d0f5a3` brand pair, the dark-green footer
panel tokenised in the `dark` set.

## The fixed header — transparent over the hero, white on scroll

Every page carries the same chrome
([header](components/crops/header-default.png), 104px high, 32px side
padding). Over the hero photo the bar is transparent with white text — the
wordmark ([logo](components/crops/logo-default.png), 230 x 40), the `Find
care`, `Find jobs`, `List your business` and `Resources` triggers
([nav-trigger](components/crops/nav-trigger-default.png)) and `Log in`
([login-link](components/crops/login-link-default.png)) all compute
`#ffffff`; scrolling transitions the background to white with ink text at
300ms ease-in-out (the sticky-header rule in
[raw/components-computed.json](raw/components-computed.json) `_meta.sheets`).
The `Join now` pill adapts too: over the hero it is the lime capsule
([join-cta](components/crops/join-cta-default.png) — 40px high on a 20px
radius, `#d0f5a3` fill with `#025747` text, going `#e4ffb8` on hover and
the bright `#8ae718` on press), while on the white pages it paints the
inverse — a deep-green fill with the lime `#e4ffb8` label (see
[babysitters-light-default](screenshots/babysitters-light-default.png)).
The Find-care trigger opens a
white mega-menu panel 928 x 360
([nav-dropdown](components/crops/nav-dropdown-default.png),
[home-light-menu](screenshots/home-light-menu.png)): category tabs on the
left ([menu-item](components/crops/menu-item-default.png), 48px rows on an
8px radius) and green `#377a69` link rows on the right
([menu-link](components/crops/menu-link-default.png)).

## The home hero and search band

Home opens on a full-bleed photo hero
([home-light-default](screenshots/home-light-default.png)): the left-aligned
display headline in NaN Druid Sans at 64px
([hero-title](components/crops/hero-title-default.png) — "Connecting
families with quality, local caregivers") over the ZIP search band: a text
input with `#707070` placeholder
([zip-field](components/crops/zip-field-default.png)) and the 56px lime
`Search` capsule ([search-cta](components/crops/search-cta-default.png),
28px radius, 20px Oceanic Grotesk label — same lime→`#8ae718` hover/press
behaviour as Join now; never pressed). Below, the "One membership"
section head in NaN Druid 48/56 with -1px tracking
([section-h2](components/crops/section-h2-default.png)) introduces the five
category cards ([category-card](components/crops/category-card-default.png),
188 x 214 white cards on a 27px radius — they take a `#f5f5f5` wash on
hover, `#e8e8e8` on press, and a `#4d9380` focus tone).

## Category landing pages

`/child-care`, `/senior-care`, `/pet-care`, `/housekeeping` and `/tutoring`
share one template ([child-care-light-full](screenshots/child-care-light-full.png)):
a white display title over a tinted panel ("Find child care on your
terms", NaN Druid 64px — [cat-h1](components/crops/cat-h1-default.png)),
then a grid of service cards
([service-card](components/crops/service-card-default.png), 608 x 512:
Nannies, Babysitters, Daycares) each with a green action
([service-cta](components/crops/service-cta-default.png), "Find
babysitters"), a member-review card quoting real families
([review-card](components/crops/review-card-default.png)) and a closed FAQ
accordion ([cat-faq](components/crops/cat-faq-default.png)).

## The public caregiver listing

`/babysitters` is a real public marketplace page
([babysitters-light-full](screenshots/babysitters-light-full.png)): a
display title ([listing-h1](components/crops/listing-h1-default.png), "Find
Local Babysitters"), an outlined toolbar — `City, State`
([city-button](components/crops/city-button-default.png)) and `Filter`
([filter-button](components/crops/filter-button-default.png), 32px rows) —
then "Here are some babysitters near you:" and the provider rows
([provider-card](components/crops/provider-card-default.png)): each a real
caregiver's public summary — first name + initial in 24px type, photo,
star rating, experience line, hourly rate, service chips
([care-tag](components/crops/care-tag-default.png), 24px pills) and a
`read more` bio expander
([read-more](components/crops/read-more-default.png)). The results page
through a 24px-item pager
([pagination](components/crops/pagination-default.png),
[page-item](components/crops/page-item-default.png), "1 2 3 4 5 … 6980").
Scrolling the results mounts the `Join Care.com` gate — a centred 420 x 436
dialog ([gate-dialog](components/crops/gate-dialog-default.png)) asking
"When do you need a babysitter?" with its own actions
([gate-cta](components/crops/gate-cta-default.png)); it was measured open
once, then hidden, never answered. A `learn more` text link
([learn-more](components/crops/learn-more-default.png)) and a second FAQ
block ([list-faq](components/crops/list-faq-default.png), toggled open for
[babysitters-light-faq](screenshots/babysitters-light-faq.png)) close the
page. Names and photos are the product's public marketplace data; no
contact details appear or were captured.

## Plans and pricing

`/app/vhp/plans-and-pricing` is the public membership page
([pricing-light-full](screenshots/pricing-light-full.png)): the `Flexible
plans that fit your life` title
([pricing-h1](components/crops/pricing-h1-default.png)) over three Premium
columns — monthly, quarterly, annual
([plan-card](components/crops/plan-card-default.png)) — each showing a 32px
price figure ([plan-price](components/crops/plan-price-default.png):
$39.99 / $25.99 / $13.99) and a Get-started action
([plan-cta](components/crops/plan-cta-default.png), 56px capsule) beside a
secondary outlined action ([plan-alt](components/crops/plan-alt-default.png)).
The `Senior Care Advisor` bundle ($349.99, includes 90 days of Premium)
paints as its own card, followed by the add-on grid —
`Feature your job post` $4.00, `Additional criminal background checks`,
`Social Media Check` $29.99, `Hiring Helper` $19.99
([addon-card](components/crops/addon-card-default.png), 624 x 188
contrast-toned cards) — and a billing FAQ
([pricing-faq](components/crops/pricing-faq-default.png)). Every purchase
action was measured, never followed to checkout.

## The auth boundary cards

`/vis/auth/login` paints the legacy sign-in card
([login-card](components/crops/login-card-default.png), ~311px wide, in
Proxima Nova — an older surface outside the MUI layer): an `EMAIL ADDRESS`
field ([login-email](components/crops/login-email-default.png)), a 50px
Continue action ([login-button](components/crops/login-button-default.png))
and the blue `#015ac8` `Log in without a password` link
([passwordless-link](components/crops/passwordless-link-default.png)).
`/app/vhp/get-started` is the join chooser
([join-card](components/crops/join-card-default.png)): `I need a caregiver`
/ `I want a care job` options with deep-green `Find care` / `Find jobs`
actions carrying the lime `#e4ffb8` label
([join-option](components/crops/join-option-default.png)). Both surfaces
were measured as boundary cards — nothing was typed, clicked through or
submitted, so the password step, two-factor screens and everything behind
them were never reached.

## The dark footer

The GlobalFooter is the page's one dark surface
([footer](components/crops/footer-default.png), 1440 x 887): link columns
in green-tinted white ([footer-link](components/crops/footer-link-default.png)),
the legal row and the social circle links
([social-icon](components/crops/social-icon-default.png), 48 x 56).

## Mobile at 390px

The same surface collapses to a 56px header
([m-header](components/crops/m-header-default.png)) with the wordmark and
the `Open menu` toggle ([m-menu-button](components/crops/m-menu-button-default.png)).
The toggle opens the full-screen CareMobileDrawer
([m-menu-open](components/crops/m-menu-open-default.png), 390 x 844):
`Find care`/`Find jobs`/`List your business`/`Resources` 56px rows
([m-nav-item](components/crops/m-nav-item-default.png)) with chevrons, an
outlined `Log in` and a deep-green `Join now` with the lime label
([mobile-home-light-menu](screenshots/mobile-home-light-menu.png)). The
hero headline keeps its NaN Druid display smaller at 390
([m-hero](components/crops/m-hero-default.png)).
