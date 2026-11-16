# Fiverr patterns

How the measured components combine on fiverr.com's signed-out surface, read
from the screenshots and the component entries in
[components.md](components.md). The site paints one light theme; all values
are from the light set unless noted.

This pass measured the home page in full. PerimeterX gated the component
pass on the other pages — their entries in components.md are recorded as
deferred — so the patterns below cite each page's shipped screenshot where a
component crop or reading is not yet published.

## The header suite

A white sticky bar tops every public page
([home-light-default](screenshots/home-light-default.png),
[mkt-header](components/crops/mkt-header-default.png), measured 1425 x 86 at
this viewport): the Fiverr wordmark
([mkt-logo](components/crops/mkt-logo-default.png)), the "Sidebar menu"
hamburger (recorded as `sidebar-btn` in components.md — a crop was not
saved), "Connect to your AI"
([nav-ai](components/crops/nav-ai-default.png)), the "EN" locale button
([nav-locale](components/crops/nav-locale-default.png)), "Become a Seller"
([nav-seller](components/crops/nav-seller-default.png)), "Sign in"
([nav-signin](components/crops/nav-signin-default.png)) and the dark "Join"
button ([nav-join](components/crops/nav-join-default.png)). A category strip
(Trending · Graphics & Design · Programming & Tech · Digital Marketing ·
Video & Animation · Writing & Translation · Music & Audio · Business ·
Finance · AI Services · Personal Growth · Consulting · Data · Photography,
[cat-nav](components/crops/cat-nav-default.png)) runs beneath.

The hamburger slides a ~480px drawer in from the left
([home-light-drawer](screenshots/home-light-drawer.png)): "Browse
categories", English and "S$ SGD" locale rows, "Connect to your AI", then a
black "Join Fiverr" button and a bordered "Sign in" at its foot. Links were
never followed. The drawer's own component readings (`drawer`,
`drawer-item`, `drawer-join`) are deferred — the toggle's `opened` state
could not be held for a clean read on this pass.

## The hero and search band

The home hero sits on a deep-green field: the display headline "Our
freelancers will take it from here"
([hero-h1](components/crops/hero-h1-default.png)), then the dark-skinned
search form ([hero-search](components/crops/hero-search-default.png)) — a
component skin, not a site theme — with the search input
([hero-search-input](components/crops/hero-search-input-default.png)) and
its dark submit
([hero-search-btn](components/crops/hero-search-btn-default.png)).
Below, a row of popular-service chips
([popular-chip](components/crops/popular-chip-default.png)) — Website
Development, Logo Design, Video Editing, AI Development, … — then category
card tiles ([cat-card](components/crops/cat-card-default.png)) and
marketing sections
([section-h2](components/crops/section-h2-default.png)).

## The directory

/categories is a services directory
([categories-light-default](screenshots/categories-light-default.png)):
a "Fiverr Gigs® Directory" masthead over grouped top-category and
subcategory link columns. A subcategory hub
([subcategory-logo-light-default](screenshots/subcategory-logo-light-default.png))
adds a breadcrumb and related-search chips. The directory's component
readings (`dir-h2`, `dir-cat-link`, `dir-sub-link`, `breadcrumb`,
`related-chip`) are deferred — the page screenshots carry the layout; see
the Gaps in components.md.

## The results grid

/search/gigs serves the public grid
([search-light-default](screenshots/search-light-default.png)): a "Results
for …" masthead, a row of filter dropdown triggers — Category, Service
Options, Seller Details, Budget, Delivery Time — and the "Sort by" control.
Gig cards repeat below: a thumbnail, the seller row with level badge, a
star rating, a collect heart and the localized starting price ("From S$xx"
for this client). The grid's component readings (`search-h1`, `filter-btn`,
`sort-btn`, `gig-card`, `gig-heart`, `gig-price`, `seller-badge`) are
deferred.

## The gig page

A live gig page ([gig-light-default](screenshots/gig-light-default.png),
[mobile-gig-light-default](screenshots/mobile-gig-light-default.png) at 390
wide) pairs the "I will …" title and category breadcrumb with a gallery and
a right-hand pricing card: the Basic/Standard/Premium tablist, the package
price, the dark "Continue" button and the bordered "Contact me". Below: the
"Get to know" seller card, an FAQ accordion, reviews and related tags.
Continue leads to checkout and was never pressed; Contact me fronts a
sign-in wall. The gig page's component readings (`gig-h1`, `pkg-tablist`,
`pkg-tab`, `pkg-price`, `gig-continue`, `gig-contact`, `seller-card`,
`faq-acc`, `review-card`, `tag-chip`) are deferred — the shots show the
layout but no per-component values are published yet.

## The auth edge

/join and /login are the only account surfaces a signed-out visitor sees
([join-light-default](screenshots/join-light-default.png),
[login-light-default](screenshots/login-light-default.png)): the
Continue-with-Google/Apple SSO buttons over the username/e-mail and
password fields and the submit. PerimeterX gated both pages this pass, so
the auth components (`join-panel`, `join-google`, `join-apple`,
`join-email-btn`, `join-field`, `login-panel`, `login-google`,
`login-email`, `login-password`, `login-submit`) are deferred — the page
shots carry the layout; nothing was submitted.

## Marketing pages

/logo-maker, /about-us, /start_selling, /cp/how-fiverr-works and the footer
legal portal share the masthead + CTA + section pattern
([logo-maker-light-default](screenshots/logo-maker-light-default.png),
[about-light-default](screenshots/about-light-default.png),
[selling-light-default](screenshots/selling-light-default.png),
[how-it-works-light-default](screenshots/how-it-works-light-default.png),
[legal-light-default](screenshots/legal-light-default.png));
/start_selling adds category chips and how-it-works adds an FAQ accordion.
Their component readings (`lm-h1`, `lm-cta`, `about-h1`, `about-cta`,
`sell-h1`, `sell-cta`, `sell-cat`, `hiw-h1`, `hiw-step`, `hiw-faq`) are
deferred.

## The footer

A white footer ([footer](components/crops/footer-default.png)) carries
sitemap columns, social icons and the language/currency buttons
([footer-locale](components/crops/footer-locale-default.png),
[footer-currency](components/crops/footer-currency-default.png),
[footer-link](components/crops/footer-link-default.png)).

## Mobile

At 390 wide the header collapses to hamburger + wordmark + Join
([mobile-home-light-default](screenshots/mobile-home-light-default.png))
and the drawer covers the viewport
([mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png));
the hero, search and gig cards stack single-column
([mobile-search-light-default](screenshots/mobile-search-light-default.png),
[mobile-gig-light-default](screenshots/mobile-gig-light-default.png),
[mobile-join-light-default](screenshots/mobile-join-light-default.png)).
The mobile component readings (`m-topbar`, `m-menu-btn`, `m-drawer`,
`m-hero-h1`, `m-search-input`) are deferred.
