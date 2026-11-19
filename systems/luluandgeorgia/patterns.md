# Patterns

How the public storefront is put together. Screenshots are in [screenshots/](screenshots).

## App shell

A 40px announcement bar sits above a white header. The wordmark is left, search is a wide grey field, and account, showroom, wishlist, and bag are icon buttons on the right. A utility row (Bestsellers, Collaborations, Inspiration, Trade, Contract, Design Services, Registry) sits under the search. Category links are a third row, uppercase, with Sale in red at the end. Phone width collapses the category row into a menu icon. See [home-light-default](screenshots/home-light-default.png) and [mobile-home-light-default](screenshots/mobile-home-light-default.png).

## Collection

A serif heading, pill-shaped category chips with a hairline, then an All filters button and a product grid. The filter drawer is a left panel with plus rows and a black Apply button. Apply was not pressed. See [collection-light-default](screenshots/collection-light-default.png) and [collection-light-filter](screenshots/collection-light-filter.png).

## Product

A lifestyle image, a studio image, then the title, price, quantity, a black Add to cart, and a bordered wishlist square. Add to cart was measured and not clicked. See [product-light-default](screenshots/product-light-default.png).

## Search

Typing in the header opens a suggestion panel. The query was typed and cleared. The results URL `/search?q=rug` was opened as a public page, which is a navigation, not a form post from this capture. See [home-light-search](screenshots/home-light-search.png) and [search-light-default](screenshots/search-light-default.png).

## Account

The account icon opens a drawer with Sign in / Create account, Trade login, My registry, and My wishlist. None of those links were followed from the drawer. `/account/login` redirects to a Shop sign-in page on shopify.com. Continue with shop was not clicked. The email field was filled with `reader@example.com` and cleared. See [home-light-account](screenshots/home-light-account.png) and [login-light-default](screenshots/login-light-default.png).

## Empty cart

The bag icon opens a drawer. Nothing was added. See [home-light-cart](screenshots/home-light-cart.png).

## Not on the signed-out surface

Checkout, an order confirmation, a validation error, a destructive confirmation, and onboarding sit behind sign-in or a submit. They were not captured.
