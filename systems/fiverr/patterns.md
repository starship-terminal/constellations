# Fiverr patterns

How the measured components combine on fiverr.com's signed-out surface, read
from the screenshots and the component entries in
[components.md](components.md). The site paints one light theme; all values
are from the light set unless noted.

## The header suite

A white sticky bar tops every public page
([home-light-default](screenshots/home-light-default.png),
[mkt-header](components/crops/mkt-header-default.png), measured 1425 x 86 at
this viewport): the Fiverr wordmark ([mkt-logo](components/crops/mkt-logo-default.png)),
the "Sidebar menu" hamburger ([sidebar-btn](components/crops/sidebar-btn-default.png)),
"Connect to your AI" ([nav-ai](components/crops/nav-ai-default.png)), the "EN"
locale button ([nav-locale](components/crops/nav-locale-default.png)),
"Become a Seller" ([nav-seller](components/crops/nav-seller-default.png)),
"Sign in" ([nav-signin](components/crops/nav-signin-default.png)) and the
green "Join" pill ([nav-join](components/crops/nav-join-default.png)). A
category strip (Trending · Graphics & Design · Programming & Tech · Digital
Marketing · Video & Animation · Writing & Translation · Music & Audio ·
Business · Finance · AI Services · Personal Growth · Consulting · Data ·
Photography, [cat-nav](components/crops/cat-nav-default.png)) runs beneath.

The hamburger slides a ~480px drawer in from the left
([home-light-drawer](screenshots/home-light-drawer.png),
[drawer](components/crops/drawer-default.png)): "Browse categories", English
and "S$ SGD" locale rows, "Connect to your AI", then a black "Join Fiverr"
button and a bordered "Sign in" at its foot. Links were never followed.

## The hero and search band

The home hero sits on a deep-green field: the display headline "Our
freelancers will take it from here"
([hero-h1](components/crops/hero-h1-default.png)), then the dark-skinned
search form ([hero-search](components/crops/hero-search-default.png)) — a
component skin, not a site theme — with the search input
([hero-search-input](components/crops/hero-search-input-default.png)) and the
green circular submit ([hero-search-btn](components/crops/hero-search-btn-default.png)).
Below, a row of popular-service chips
([popular-chip](components/crops/popular-chip-default.png)) — Website
Development, Logo Design, Video Editing, AI Development, … — then category
card tiles and marketing sections
([section-h2](components/crops/section-h2-default.png)).

## The directory

/categories is a services directory
([categories-light-default](screenshots/categories-light-default.png)):
a "Fiverr Gigs® Directory" masthead over grouped top-category and
subcategory link columns ([dir-cat-link](components/crops/dir-cat-link-default.png),
[dir-sub-link](components/crops/dir-sub-link-default.png)). A subcategory
hub ([subcategory-logo-light-default](screenshots/subcategory-logo-light-default.png))
adds a breadcrumb and related-search chips
([related-chip](components/crops/related-chip-default.png)).

## The results grid

/search/gigs serves the public grid
([search-light-default](screenshots/search-light-default.png)): a "Results
for …" masthead ([search-h1](components/crops/search-h1-default.png)), a row
of filter dropdown triggers — Category, Service Options, Seller Details,
Budget, Delivery Time ([filter-btn](components/crops/filter-btn-default.png))
— and the "Sort by" control
([sort-btn](components/crops/sort-btn-default.png)). Gig cards repeat below
([gig-card](components/crops/gig-card-default.png)): a thumbnail, the seller
row with level badge ([seller-badge](components/crops/seller-badge-default.png)),
a star rating, a collect heart
([gig-heart](components/crops/gig-heart-default.png)) and the localized
starting price ([gig-price](components/crops/gig-price-default.png), "From
S$xx" for this client).

## The gig page

A live gig page ([gig-light-default](screenshots/gig-light-default.png))
pairs the "I will …" title ([gig-h1](components/crops/gig-h1-default.png))
and category breadcrumb with a gallery and a right-hand pricing card: the
Basic/Standard/Premium tablist
([pkg-tablist](components/crops/pkg-tablist-default.png)), the package price
([pkg-price](components/crops/pkg-price-default.png)), the green "Continue"
button ([gig-continue](components/crops/gig-continue-default.png)) and the
bordered "Contact me" ([gig-contact](components/crops/gig-contact-default.png)).
Below: the "Get to know" seller card
([seller-card](components/crops/seller-card-default.png)), an FAQ accordion
([faq-acc](components/crops/faq-acc-default.png)), reviews
([review-card](components/crops/review-card-default.png)) and related tags
([tag-chip](components/crops/tag-chip-default.png)). Continue leads to
checkout and was never pressed; Contact me fronts a sign-in wall.

## The auth edge

/join and /login are the only account surfaces a signed-out visitor sees
([join-light-default](screenshots/join-light-default.png),
[login-light-default](screenshots/login-light-default.png)): the
Continue-with-Google/Apple SSO buttons
([join-google](components/crops/join-google-default.png),
[login-google](components/crops/login-google-default.png)) over the
username/e-mail and password fields
([login-email](components/crops/login-email-default.png),
[login-password](components/crops/login-password-default.png)) and the
submit ([login-submit](components/crops/login-submit-default.png)). All
measured as forms — typed into, cleared, never submitted.

## Marketing pages

/logo-maker, /about-us, /start_selling and /cp/how-fiverr-works share the
masthead + CTA + section pattern
([lm-h1](components/crops/lm-h1-default.png),
[sell-h1](components/crops/sell-h1-default.png),
[hiw-h1](components/crops/hiw-h1-default.png)); /start_selling adds category
chips ([sell-cat](components/crops/sell-cat-default.png)) and how-it-works
adds an FAQ accordion ([hiw-faq](components/crops/hiw-faq-default.png)).

## The footer

A white footer ([footer](components/crops/footer-default.png)) carries
sitemap columns, social icons and the language/currency buttons
([footer-locale](components/crops/footer-locale-default.png),
[footer-currency](components/crops/footer-currency-default.png)).

## Mobile

At 390 wide the header collapses to hamburger + wordmark + Join
([m-topbar](components/crops/m-topbar-default.png)) and the drawer covers
the viewport ([mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png));
the hero, search and gig cards stack single-column
([mobile-search-light-default](screenshots/mobile-search-light-default.png)).
