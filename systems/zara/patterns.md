# Patterns

Public US storefront, signed out, refreshed 2026-11-21. Page shots are in [screenshots/](screenshots/). The control map is [site-tree.md](site-tree.md).

## Shell

A right column of uppercase links: SEARCH, BAG with a count, LOG IN, HELP. On the cart page the column also shows FAVORITES and PRE-OWNED. The wordmark is an inline SVG (`viewBox="0 0 132 55"`). The header element itself is `display: contents`. Open Menu is a hamburger that opens a drawer on the same page.

![Home](screenshots/home-light-default.png)

![Open menu](screenshots/home-light-menu.png)

## Location gate

www.zara.com/ lists a market and a language before a storefront loads. Singapore was preselected. United States and English were chosen, Remember selection was cleared, and Continue opened www.zara.com/us/. A cookie dialog was closed.

![Location gate](screenshots/location-gate-light-default.png)

## Catalog

The dresses grid is the category page captured this pass. A numbered subnav sits on the left. Product tiles show a name and a price at 11px uppercase once the grid is scrolled. FILTERS opens a right drawer. VIEW RESULTS was not clicked.

![Dresses](screenshots/category-light-default.png)

![Dresses grid](screenshots/category-light-grid.png)

## Product

Name at 15px uppercase, price at 15px uppercase (`$ 45.90` on the measured dress). ADD and Apple Pay sit under the price. Neither was clicked. Nothing was added to the bag.

![Product](screenshots/product-light-default.png)

## Search

A section column (Woman selected, Man, Kids) and a borderless input. Interest suggestions render under the field. No query was typed or submitted.

![Search, empty](screenshots/search-light-empty.png)

## Help

A title, a search field, FAQ rows, and topic columns. Account topics were not opened. The search field was not submitted.

![Help](screenshots/help-light-default.png)

## Empty bag

The cart URL loads signed out and shows "YOUR BAG IS EMPTY". Nothing was added. Checkout was not entered.

![Empty bag](screenshots/cart-light-empty.png)

## Logon

LOG IN leaves www.zara.com for account.zara.com/login/two-step. The form is an empty email field plus CONTINUE, then QR, Google, and Apple. It was photographed and not submitted. No email, code, phone, or address was entered. Identity providers were not clicked.

![Login wall, empty](screenshots/login-light-empty.png)

## 404

A made-up path renders "PAGE NOT FOUND", "This page is no longer available.", and GO TO HOMEPAGE.

![404](screenshots/error-light-404.png)

## Phone width

Home and the dresses page at a measured 390 by 844 CSS viewport, devicePixelRatio 2, desktop user agent. OPEN APP is a banner. The header keeps Open Menu, LOG IN, a search icon, and the bag count.

![Home at 390](screenshots/mobile-home-light-default.png)

![Dresses at 390](screenshots/mobile-category-light-default.png)
