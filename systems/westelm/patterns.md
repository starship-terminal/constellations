# West Elm patterns

How the loaded pages are put together. Captured 2026-11-21, signed out, headed Chrome, 1440x900 and 390x844. Shop, product, cart and favorites URLs returned HTTP 403 and are not patterns here.

## Shell

Desktop header is four bands: a brand strip, a utility row (search, wordmark, ACCOUNT, TRACK ORDER, MY STORE, FAVORITES, CART), a secondary text row, and a primary category row. A burgundy promo band sits under the nav on the home page. Phone width collapses this to a hamburger, search, wordmark, account and cart. [home-light-default](screenshots/home-light-default.png), [mobile-home-light-default](screenshots/mobile-home-light-default.png).

## Navigation

Hovering a primary category opens a white flyout. The category link itself goes to `/shop/…`, which 403'd. [home-light-nav-furniture](screenshots/home-light-nav-furniture.png). The phone drawer lists the same categories. [mobile-home-light-menu](screenshots/mobile-home-light-menu.png). The map of which control opens which page is [site-tree.md](site-tree.md).

## Sign-in wall

`/account/login.html` asks for an email, then CONTINUE WITH EMAIL, plus Continue with Google and Continue with Apple. No email was typed and neither social button was clicked. [login-light-default](screenshots/login-light-default.png). Track-order also shows a sign-in form above an order-number form. Neither was submitted. [track-order-light-default](screenshots/track-order-light-default.png).

## Registry marketing

A long editorial page with CREATE A REGISTRY, FIND A REGISTRY and MANAGE MY REGISTRY. Create and manage lead into account flows and were not followed. [registry-light-default](screenshots/registry-light-default.png).

## Store locator and customer service

`/stores/` is a public locator with a location field. No location was typed. `/customer-service/` is a link index. [stores-light-default](screenshots/stores-light-default.png), [customer-service-light-default](screenshots/customer-service-light-default.png).

## Footer

Grey fill `rgb(244, 244, 244)`, link columns, a signup field that was not filled. [home-light-full](screenshots/home-light-full.png).

## Not captured

Product listing, product detail, cart, favorites, search results, checkout, empty states of those pages, destructive confirmation, toast feedback, and onboarding. The 403 page itself ("SORRY") is a block, not a designed empty state, and was not kept as a screenshot.
