# GoFundMe patterns

How the measured components combine on gofundme.com's signed-out surface,
read from the screenshots and the component entries in
[components.md](components.md). The consumer site paints one light theme;
all values are from the light set unless noted.

## The chrome suite

Every consumer page stacks two bars at the top
([home-light-default](screenshots/home-light-default.png)): the
`hrt-global-promo-banner`
([mkt-promo](components/crops/mkt-promo-default.png)) on the
`color.surface.brand.medium` #CCF88E fill — "Introducing the Kind 50: Real
stories of those who defy the doomscroll." with a `See the list.` link and a
close icon-button — and the white sticky header
([mkt-header](components/crops/mkt-header-default.png)). The header pairs
the left group (Search control
[nav-search](components/crops/nav-search-default.png), the Donate
[nav-donate-dd](components/crops/nav-donate-dd-default.png) and Fundraise
dropdown triggers) with the centre GoFundMe mark
([mkt-logo](components/crops/mkt-logo-default.png)) and the right group
(About trigger
[nav-about-dd](components/crops/nav-about-dd-default.png), "Sign in"
[nav-signin](components/crops/nav-signin-default.png), the pill "Start a
GoFundMe"
[nav-start](components/crops/nav-start-default.png)).

A trigger opens its `hrt-header-dropdown-content` panel on hover
([home-light-menu-donate](screenshots/home-light-menu-donate.png),
[home-light-menu-fundraise](screenshots/home-light-menu-fundraise.png),
[home-light-menu-about](screenshots/home-light-menu-about.png)) — closed
panels stay mounted with `visibility:hidden`; the `--open` class is the real
state. The Donate/Fundraise panels are multi-column link groups; About is
the right-aligned single column
([nav-panel](components/crops/nav-panel-default.png)). Links were never
followed. At 390 wide the row collapses to the mark plus a nav toggle that
opens the full-height overlay
([mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png),
[m-drawer](components/crops/m-drawer-default.png)).

The footer ([footer](components/crops/footer-default.png)) closes every
page: sitemap columns, the "More resources" accordion
([footer-more](components/crops/footer-more-default.png)), social icons,
the "United States · English" locale control
([locale-btn](components/crops/locale-btn-default.png)) and the Transcend
"Manage Cookie Preferences" link
([cookie-btn](components/crops/cookie-btn-default.png)).

## The hero

The home hero centres on the white field: a "#1 crowdfunding platform" tag,
the display masthead "Where successful fundraisers start"
([hero-h1](components/crops/hero-h1-default.png)), the supporting line, and
the primary "Start a GoFundMe" button
([hero-cta](components/crops/hero-cta-default.png)) — `color.button.primary.surface`
#274A34 with `color.button.primary.text` #CCF88E on a full-radius pill.
Hero photography sits below the fold
([home-light-full](screenshots/home-light-full.png)).

## The fundraiser rails and cards

Home and /discover run rails and grids of fundraiser cards (a
`fundraiser-card_*` CSS-module block —
[fundraiser-card](components/crops/fundraiser-card-default.png),
[discover-light-default](screenshots/discover-light-default.png)): the
media block carrying a `fundraiser-card_mediaTag` location chip
([card-location](components/crops/card-location-default.png)), the
`fundraiser-card_title` h3
([card-title](components/crops/card-title-default.png)), the "$ raised"
line and the `fundraiser-card_progressBar` `progress` element with its
`hrt-goal-bar-label`
([card-goal-bar](components/crops/card-goal-bar-default.png)). Rails are
filtered by collection pills ("Happening worldwide"…,
[collection-btn](components/crops/collection-btn-default.png)) and paged by
carousel icon-buttons
([carousel-btn](components/crops/carousel-btn-default.png)); a pause-motion
control sits on the animated sections
([pause-motion-btn](components/crops/pause-motion-btn-default.png)). /s
serves the same cards with organiser `hrt-avatar`s
([s-avatar](components/crops/s-avatar-default.png),
[search-light-default](screenshots/search-light-default.png)).

## The fundraiser page

A /f/<slug> page stacks the campaign above the fold
([fundraiser-light-default](screenshots/fundraiser-light-default.png)): the
title ([f-title](components/crops/f-title-default.png)), the media viewer
with arrow icon-buttons
([f-media-nav](components/crops/f-media-nav-default.png)) and pagination
dots, the "$ raised of $ goal" line
([f-raised](components/crops/f-raised-default.png)) beside the
`progress-meter` / `hrt-progress-circle` goal element
([f-goal-bar](components/crops/f-goal-bar-default.png)), then the action
row — primary "Donate now"
([f-donate](components/crops/f-donate-default.png)) beside secondary
"Share" ([f-share](components/crops/f-share-default.png)) and "Message"
([f-message](components/crops/f-message-default.png)) — measured in every
state, never pressed. Below: the organiser row with `hrt-avatar`
([f-avatar](components/crops/f-avatar-default.png)), the story behind "Read
more" ([f-readmore](components/crops/f-readmore-default.png)), the
"Donations" section heading
([f-donations-h2](components/crops/f-donations-h2-default.png)) with its
supporter list, "Report fundraiser"
([f-report](components/crops/f-report-default.png)) and the related rail
with its collection pill
([f-collection](components/crops/f-collection-default.png)).

## The wizard and the auth edge

`/create/fundraiser/category` is the one interactive surface a signed-out
visitor can open
([create-light-default](screenshots/create-light-default.png)): the "Let's
begin your fundraising journey" masthead
([create-h1](components/crops/create-h1-default.png)), the country
`hrt-select-field` ([create-country](components/crops/create-country-default.png)),
the postcode `hrt-text-field`
([create-zip](components/crops/create-zip-default.png)) — typed into then
cleared — the category radio pills
([create-pill](components/crops/create-pill-default.png)) and "Continue"
([create-continue](components/crops/create-continue-default.png)), never
pressed. `/sign-in` is the auth shell's card
([sign-in-light-default](screenshots/sign-in-light-default.png)): "Welcome",
Sign-in-with-Google and Continue-with-Apple SSO buttons, the e-mail field
and "Continue" — measured as a form, never submitted (in headless the auth
island can hydrate to the card or stay an empty shell; both are recorded).

## The content stack

The /c/* marketing pages are a second public system — WordPress wp-* blocks
over an older hrt-base-* component layer
([pricing-light-default](screenshots/pricing-light-default.png),
[how-it-works-light-default](screenshots/how-it-works-light-default.png)):
the hero masthead ([price-h1](components/crops/price-h1-default.png)), the
"Individual or business / Certified nonprofit" audience toggles
([price-toggle](components/crops/price-toggle-default.png)), CSS-disclosure
FAQ rows ([price-faq](components/crops/price-faq-default.png)), wp-block
CTAs ([wp-button](components/crops/wp-button-default.png)) and the footer
language switcher
([wp-locale](components/crops/wp-locale-default.png)). Their values are
measured component tokens, not the consumer theme.
