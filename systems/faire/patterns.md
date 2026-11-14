# Faire patterns

How the measured components combine on faire.com's public signed-out surface,
read from the screenshots and the component entries in
[components.md](components.md). The site paints one light theme; the
`.fs-mode-on-surface` scope that re-keys the action/text roles for controls on
dark media is a token scope, not a second theme. All values are from the light
set unless noted.

## The header stack

Two bands top every page
([home-light-default](screenshots/home-light-default.png)). A dark `#333333`
promo strip ([promo-banner](components/crops/promo-banner-default.png)) can
carry a seasonal offer above the white header
([mkt-header](components/crops/mkt-header-default.png)): the FAIRE wordmark
([mkt-logo](components/crops/mkt-logo-default.png)), the bordered pill
"All categories" dropdown toggle
([all-categories-btn](components/crops/all-categories-btn-default.png)), the
rounded search field ([search-field](components/crops/search-field-default.png)),
the EN-US locale control ([locale-btn](components/crops/locale-btn-default.png)),
Blog and "Sign up to sell" text links
([nav-link](components/crops/nav-link-default.png),
[nav-sell](components/crops/nav-sell-default.png)), a text "Sign in"
([nav-signin](components/crops/nav-signin-default.png)) and the dark
`action.surface.default` "Sign up to buy" fs-button
([nav-signup-buy](components/crops/nav-signup-buy-default.png)). The toggle's
own pointer click opens the full-width categories menu panel
([categories-panel](components/crops/categories-panel-default.png),
[home-light-categories-menu](screenshots/home-light-categories-menu.png)) — the
menu paints no border or shadow of its own, the white field and 48px padding
do the grouping.

## The marketing hero

Home and every marketing page (/how-faire-works, /about, /large-retailers,
/point-of-sale/about, /markets, /affiliates) open with the same recipe: a serif
masthead — Nantes_fix on home at 52/64
([hero-h1](components/crops/hero-h1-default.png),
[hw-h1](components/crops/hw-h1-default.png),
[lr-h1](components/crops/lr-h1-default.png),
[markets-h1](components/crops/markets-h1-default.png),
[aff-h1](components/crops/aff-h1-default.png)) — over media or a coloured band,
then paired CTAs: a dark primary fs-button
([cta-primary](components/crops/cta-primary-default.png),
[hw-cta](components/crops/hw-cta-default.png),
[about-cta](components/crops/about-cta-default.png),
[lr-cta](components/crops/lr-cta-default.png),
[pos-cta](components/crops/pos-cta-default.png),
[markets-cta](components/crops/markets-cta-default.png),
[aff-cta](components/crops/aff-cta-default.png)) beside a hairline-bordered
secondary ([cta-secondary](components/crops/cta-secondary-default.png)) or a
plain text link ([cta-plain](components/crops/cta-plain-default.png)). Every
CTA opens the sign-up dialog; none was followed.

## The category teaser and supplier listings

Category pages (/category/Home Decor, /category/New Products) open with a GT
Canon masthead ([cat-h1](components/crops/cat-h1-default.png)) above a sub-nav
of category links ([cat-nav-link](components/crops/cat-nav-link-default.png)),
filter pills ([cat-filter-btn](components/crops/cat-filter-btn-default.png))
and grids of category cards
([category-card](components/crops/category-card-default.png)) and
[subcat-card](components/crops/subcat-card-default.png) tiles; product tiles
([product-tile](components/crops/product-tile-default.png)) deep-link into the
sign-up gate. The suppliers listings use a row layout
([supplier-row](components/crops/supplier-row-default.png)) with a filter
sidebar ([sup-filter-link](components/crops/sup-filter-link-hover.png));
the All Brands A-Z page lists plain rows
([supall-h1](components/crops/supall-h1-default.png),
[supall-row](components/crops/supall-row-default.png)). The Candles listing's
product grid never hydrates signed out — it holds its skeleton tiles beside
the real "Keep exploring" carousel and the olive CTA band, which is the
honest public state. Cloudflare intermittently challenges these routes —
several states are recorded missing rather than estimated.

## The brand storefront

/brand/b_d72c56fe is the deepest public content surface: a serif brand name
heading ([brand-h1](components/crops/brand-h1-default.png)), the circular brand
avatar ([brand-avatar](components/crops/brand-avatar-default.png)), a minimum
order badge ([min-order-badge](components/crops/min-order-badge-default.png)),
tab pills ([brand-tab](components/crops/brand-tab-default.png)), a grid of
product tiles ([brand-product-tile](components/crops/brand-product-tile-default.png))
and brand tile cards ([brand-tile](components/crops/brand-tile-default.png)).
The featured-brands row reuses the same pill idiom
([pill-tab](components/crops/pill-tab-default.png)) with the selected pill
painted dark. Public browsing ends at an email wall
([wall-email](components/crops/wall-email-default.png),
[wall-field](components/crops/wall-field-default.png)) — typed into and
cleared, never sent.

## The editorial pages

/news is a serif masthead ([news-h1](components/crops/news-h1-default.png))
plus a grid of press-card links
([news-card](components/crops/news-card-default.png)) and CTAs
([news-cta](components/crops/news-cta-default.png)); /about and /careers use
the same masthead-plus-section rhythm
([about-h1](components/crops/about-h1-default.png),
[about-h2](components/crops/about-h2-default.png),
[careers-h1](components/crops/careers-h1-default.png),
[careers-cta](components/crops/careers-cta-default.png)). /support centres a
help search field ([help-search](components/crops/help-search-default.png),
[help-h1](components/crops/help-h1-default.png)) over topic links
([help-link](components/crops/help-link-default.png)).

## The application form

/apply is a stepper: an icon-only back button
([back-btn](components/crops/back-btn-default.png)) and a GT Canon "Welcome!"
heading ([apply-heading](components/crops/apply-heading-default.png)) above
boxed fs-fields — [field-firstname](components/crops/field-firstname-default.png),
[field-lastname](components/crops/field-lastname-default.png),
[field-email](components/crops/field-email-default.png),
the phone field with its country-code prefix button
([field-phone](components/crops/field-phone-default.png),
[phone-code-btn](components/crops/phone-code-btn-default.png)),
[field-password](components/crops/field-password-default.png) with the
show/hide toggle ([show-password](components/crops/show-password-default.png)) —
then the terms and marketing checkboxes
([checkbox-terms](components/crops/checkbox-terms-default.png),
[checkbox-marketing](components/crops/checkbox-marketing-default.png)) and the
dark Next fs-button ([next-btn](components/crops/next-btn-default.png)).
Fields were focused and filled then cleared; Next was measured, never clicked
to submit.

## The auth dialogs

`?signIn=1` and `?signUp=1` mount fs-modals over the home page — the deepest
surface reachable without an account. The 420px sign-in dialog
([signin-dialog](components/crops/signin-dialog-default.png)) holds the email
and password fields ([signin-email](components/crops/signin-email-default.png),
[signin-password](components/crops/signin-password-default.png)) with a
show-password toggle
([signin-show-password](components/crops/signin-show-password-default.png)),
the dark Sign in fs-button
([signin-submit](components/crops/signin-submit-default.png)), Google and
Apple SSO ([signin-google](components/crops/signin-google-default.png),
[signin-apple](components/crops/signin-apple-default.png)), a sign-up link
([signin-signup-link](components/crops/signin-signup-link-default.png)) and
the X close ([signin-close](components/crops/signin-close-default.png)). The
500px sign-up dialog ([signup-dialog](components/crops/signup-dialog-default.png))
is the same shape with a business-email field
([signup-email](components/crops/signup-email-default.png)),
[signup-submit](components/crops/signup-submit-default.png),
[signup-google](components/crops/signup-google-default.png),
[signup-signin-link](components/crops/signup-signin-link-default.png) and
[signup-close](components/crops/signup-close-default.png); the observed
sign-up dialog mounts no Apple button — recorded missing, not estimated.
Every product tile's href is a `?signUp=product` URL: the whole marketplace
sits behind this dialog.

## The mobile header and drawer

At 390 the header collapses to the wordmark, a magnifier button
([m-search-btn](components/crops/m-search-btn-default.png)) and Menu
([m-menu-btn](components/crops/m-menu-btn-default.png)) over
[m-topbar](components/crops/m-topbar-default.png). The magnifier opens a
search overlay with its own field
([m-search](components/crops/m-search-default.png)); Menu's own toggle slides
the nav drawer ([m-drawer](components/crops/m-drawer-default.png),
[mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png)): a dark
account block (FAIRE wordmark, Sign up to buy / Sign in / Sign up to sell
rows) over the light category list — a dark-bold section style, not a second
theme. The hero reflows to a single column
([m-hero-h1](components/crops/m-hero-h1-default.png)).

## The footer

Every page ends in a light footer
([footer](components/crops/footer-default.png)): sitemap columns of plain text
links ([footer-link](components/crops/footer-link-default.png)) under section
headings, social icons and the locale/country controls. A dark-bold olive CTA
band ("Ready to start buying wholesale online?") can sit directly above it on
the listing pages — a section style, not a theme.

## The boundary

Everything past the sign-up dialog — search results, product detail, cart,
checkout, account, the brand portal — requires a Faire account and is a
documented boundary, not a gap in the capture. The OneTrust consent layer was
hidden on every shot, never answered; the Cloudflare Turnstile interstitial
was waited out, never solved.
