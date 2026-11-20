# Mapbox patterns

Public signed-out pages only. The account console was not opened.

## Marketing shell

The desktop nav is `nav.nav_navbar.color-mode-light`. Log in is a text link. Sign up is a blue pill (`#007afc`, radius 100px). Products, Solutions, Developers, Company, and Resources are local toggles (`button.nav_link-toggle`). [screenshots/home-light-menu.png](screenshots/home-light-menu.png) shows the Products menu open. At 390 the toggle is `a.nav_menu-toggle`, shown in [screenshots/mobile-home-light-menu-open.png](screenshots/mobile-home-light-menu-open.png).

## Hero

The home headline is Cera Pro 56px / 70px, weight 700, colour `#0e1012`. The primary action paints on `.button_inner` (`#007afc`, white text, 52px tall, pill). Hover lifts it to `#3195ff`. The stroke action beside it ("Contact us") fills `#eff7ff` on hover. See [screenshots/home-light-default.png](screenshots/home-light-default.png).

## Pricing

[screenshots/pricing-light-default.png](screenshots/pricing-light-default.png) is a long public page (about 13450px). Product links sit in `a.pricing_subnav-link`. A usage range (`input.product-sku_range-input`) is the visible calculator control. The matching number input is `display: none`. Nothing was purchased.

## Contact

[screenshots/contact-light-default.png](screenshots/contact-light-default.png) mounts a HubSpot form. The request type is `input.hsfc-TextInput[role=combobox]`. It was focused and opened. No option was chosen. The form was not submitted. There is no text area.

## Docs

docs.mapbox.com is a separate shell (Open Sans, `data-theme="light"`). Sign in and Sign up point at account.mapbox.com and were not followed. The search button opens a public dialog, shown in [screenshots/docs-light-search.png](screenshots/docs-light-search.png). [screenshots/docs-gljs-light-default.png](screenshots/docs-gljs-light-default.png) is the GL JS guides page. [screenshots/docs-style-light-default.png](screenshots/docs-style-light-default.png) is the public style-spec layers page.

## Consent

OneTrust mounts `#onetrust-banner-sdk` ("We care about your privacy"). It was hidden with `display: none`. Accept, Reject, and Cookie Settings were never clicked.
