# Dub patterns

How the measured components combine on dub.co's public surface, read from the
screenshots and the component entries in [components.md](components.md).
dub.co is three surfaces signed out: the Next.js marketing site (Inter body,
Satoshi display, on the `#fafafa` field), the app.dub.co auth shell on /login
and /register (a plain system stack), and the Mintlify docs/help surface on
/docs and /help — the only place a real theme toggle exists. Values are from
the light set unless marked; the `dk-docs-*` entries are the docs surface's
dark theme.

## The marketing header

Every marketing page carries the same chrome on the `#fafafa` field
([nav](components/crops/nav-default.png)): the Dub wordmark
([logo](components/crops/logo-default.png), 61 x 32), the `Product`
mega-menu trigger ([nav-trigger](components/crops/nav-trigger-default.png),
Inter 14/20 500 `#404040`), the plain `Solutions`, `Customers`, `Pricing`
links ([nav-link](components/crops/nav-link-default.png)), a bordered
`Log in` ([nav-login](components/crops/nav-login-default.png), 1px
`#e5e5e5` border, 8px radius, 32px) and the black `Sign up` pill
([nav-cta](components/crops/nav-cta-default.png), `#000` fill, white text,
8px radius, 32px). Hovering the trigger opens the ~319px mega-menu panel
([nav-dropdown](components/crops/nav-dropdown-default.png), `#fafafa`
card, 12px radius) of product links
([menu-link](components/crops/menu-link-default.png),
[home-light-menu](screenshots/home-light-menu.png)). Buttons keep their
fill on hover and paint a 4px `#e5e5e5` box-shadow halo; keyboard focus is
the browser-default `auto 1px rgb(0, 95, 204)` outline.

## The home hero

The home page opens centred on `#fafafa`
([home-light-default](screenshots/home-light-default.png)): the
`Introducing our Startup Program` announcement pill
([hero-badge](components/crops/hero-badge-default.png), Inter 12/16 500),
the `Turn clicks into revenue` headline in Satoshi 48px / 55.2px at weight
500 on `#171717` ink ([hero-title](components/crops/hero-title-default.png)),
a 640px lede in Inter 20/28 `#525252`
([hero-lede](components/crops/hero-lede-default.png)), then the two
acquisition actions — `Start for free`
([hero-cta](components/crops/hero-cta-default.png), black fill, 38px, 8px
radius) and `Get a demo`
([hero-demo](components/crops/hero-demo-default.png), white fill, 1px
`#e5e5e5` border, same geometry). Below, a row of feature tabs
([hero-tab](components/crops/hero-tab-default.png), 1px `#e5e5e5` border,
8px radius) sits over the rendered dashboard mock
([demo-panel](components/crops/demo-panel-default.png), 882 x 567, white
on a 1px `#d4d4d4` border at 12px radius — a published illustration, not
the app).

## The pricing surface

/pricing ([pricing-light-default](screenshots/pricing-light-default.png))
centres the Satoshi h1
([pricing-h1](components/crops/pricing-h1-default.png), 48/55.2 at 500)
above the Monthly/Yearly toggle
([billing-toggle](components/crops/billing-toggle-default.png), 12px
radius, the yearly shot is
[pricing-light-yearly](screenshots/pricing-light-yearly.png)) and one
shared `#fafafa` plan panel
([plan-card](components/crops/plan-card-default.png), 1062 x 623, 1px
`#ededed` border, 12px radius) holding the three plans. Each column repeats
a plan name ([plan-name](components/crops/plan-name-default.png), Inter
16/24 500), a price figure
([plan-price](components/crops/plan-price-default.png), -0.28px tracking)
and a trial action
([plan-cta](components/crops/plan-cta-default.png)). A billing-FAQ
accordion closes the page
([faq-trigger](components/crops/faq-trigger-default.png), 56px rows).

## The compare and customers surfaces

/compare/bitly
([compare-light-default](screenshots/compare-light-default.png)) runs the
same grammar — a Satoshi 48px headline
([cmp-h1](components/crops/cmp-h1-default.png)) over the feature
comparison table ([cmp-table](components/crops/cmp-table-default.png),
[cmp-check](components/crops/cmp-check-default.png)). /customers
([customers-light-default](screenshots/customers-light-default.png))
pairs the headline
([cust-h1](components/crops/cust-h1-default.png)) with dark `#171717`
story cards ([customer-card](components/crops/customer-card-default.png),
12px radius, 0.5s flex-grow hover expansion at
cubic-bezier(0.215, 0.61, 0.355, 1)).

## The contact-sales form

/contact/sales
([sales-light-default](screenshots/sales-light-default.png)) centres an
800px white card ([sales-card](components/crops/sales-card-default.png))
of the same field grammar as auth — 38px inputs on 1px `#d4d4d4` borders
at 6px radius ([sales-email](components/crops/sales-email-default.png)),
a 118px textarea
([sales-message](components/crops/sales-message-default.png)), selectable
topic pills ([sales-topic](components/crops/sales-topic-default.png), 75ms
colour transitions) and the `Send message` submit
([sales-submit](components/crops/sales-submit-default.png), painted
disabled-grey `#f5f5f5`/`#737373` at rest). Nothing was ever sent.

## The auth boundary

/login and /register paint the app.dub.co shell — centred 384px columns
([login-card](components/crops/login-card-default.png),
[register-card](components/crops/register-card-default.png)) in the plain
ui-sans-serif system stack, a 20/28 600 title, and the same field grammar:
the email input ([email-field](components/crops/email-field-default.png),
376 x 38, 6px radius, 1px `#d4d4d4` border that goes `#000` with a 1px
black ring on focus), the black `Log in with email` submit
([email-submit](components/crops/email-submit-default.png), 40px, 8px
radius) and three white SSO buttons
([oauth-google](components/crops/oauth-google-default.png),
[oauth-github](components/crops/oauth-github-default.png),
[oauth-saml](components/crops/oauth-saml-default.png), 1px `#e5e5e5`
borders, hover `#fafafa`). The `Sign up` switch link sits under the card
([auth-link](components/crops/auth-link-default.png)). These lead to the
authenticated workspace — the boundary, not the product.

## The docs surface

/docs and /help are Mintlify — a different chrome from the marketing site,
on the gray ramp. The 288px sticky sidebar
([docs-sidebar](components/crops/docs-sidebar-default.png)) holds group
labels (Inter 12/16 700 `#17191e`) and items
([docs-nav-item](components/crops/docs-nav-item-default.png), 14/20,
12px radius): the active one paints `#155dfc` text on a 10% blue
`oklab` wash. The `Search…` trigger is a 384 x 36 pill at 9999px radius on
a 3% ink wash ([docs-search](components/crops/docs-search-default.png),
10% on hover). The page head carries the h1
([docs-h1](components/crops/docs-h1-default.png), Satoshi 36/40 600
`#17191e`), the `Copy page` action
([docs-copy](components/crops/docs-copy-default.png), 1px `#dfe1e6`
border, 12px corner radius), a Yes/No feedback pair
([docs-feedback](components/crops/docs-feedback-default.png)) and card
links ([docs-card](components/crops/docs-card-default.png)). Focus rings
here are the product's own 1px `#155dfc`, not the browser blue.

### Docs dark — the one real theme toggle

The `Change theme preference` button
([docs-theme](components/crops/docs-theme-default.png), a 30px 9999px
round button on a 4% ink wash) opens a System/Light/Dark dropdown that
sets `dark` on `<html>` (localStorage isDarkMode). Dark re-binds the same
roles: `#090b10`/`#000` fields, `#25282d` hairlines, `#dfe1e6` h1 ink
([dk-docs-h1](components/crops/dk-docs-h1-default.png)), `#9fa1a6`
sidebar text ([dk-docs-sidebar](components/crops/dk-docs-sidebar-default.png)),
the search pill on a 3% white wash
([dk-docs-search](components/crops/dk-docs-search-default.png)) and the
Copy-page button on the `#090b10` canvas
([dk-docs-copy](components/crops/dk-docs-copy-default.png)) — captured in
[docs-dark-dark-default](screenshots/docs-dark-dark-default.png). The
10% primary wash under the active nav item is identical in both themes
([dk-docs-nav-item](components/crops/dk-docs-nav-item-default.png)).

## The footer

The marketing footer ([footer](components/crops/footer-default.png))
closes every page in the same neutral scheme: link columns
([footer-link](components/crops/footer-link-default.png), Inter 14/20
`#737373`, 75ms colour transitions) and 24px round social icon buttons
([social-link](components/crops/social-link-default.png), 9999px radius).

## Mobile (390 wide)

At phone width the chrome compresses to a 56px bar
([m-nav](components/crops/m-nav-default.png)) with a round menu button
([m-menu-button](components/crops/m-menu-button-default.png)) that opens
the menu overlay ([m-menu-open](components/crops/m-menu-open-default.png),
[mobile-home-light-menu](screenshots/mobile-home-light-menu.png)) of 24px
items at Inter 16/24 600
([m-nav-item](components/crops/m-nav-item-default.png)). The hero drops to
Satoshi 36/40 ([m-hero](components/crops/m-hero-default.png),
[mobile-home-light-default](screenshots/mobile-home-light-default.png)).
