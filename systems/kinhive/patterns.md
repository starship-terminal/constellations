# Kinhive patterns

How the public pages combine the components, including the join and sign-in code step. Screenshots are in [screenshots/](screenshots).

## Marketing chrome

Every marketing page stacks three bands: a dark promo strip ("Kinhive is free, forever. Join today"), a 65px sticky header, then the page. The header holds the wordmark, Features and Use Cases menus, Pricing, About, Blog, Merch, Log in, and Join free. See [home-light-default](screenshots/home-light-default.png).

## Home hero

A full-bleed photograph with a butter card over the left third. The card holds an eyebrow, an Affairs headline, a short paragraph, an email field with an ink submit square, a sign-in link, and App Store / Google Play badges. The badges link out and were not followed. See [home-light-full](screenshots/home-light-full.png).

## Mega-menu

Features opens a panel under the header: four chartreuse chips (Intros, Cowork, Community, Daily prompts), a free-resources column, an also-in-Kinhive column, and a chocolate $0 card. Use Cases opens the same kind of panel. See [home-light-menu-features](screenshots/home-light-menu-features.png) and [home-light-menu-usecases](screenshots/home-light-menu-usecases.png).

## Pricing

One chartreuse "Every member" card at $0 and a raised "Buy us a coffee" card. No billing toggle. The coffee card's button was not followed. See [pricing-light-default](screenshots/pricing-light-default.png).

## Directory pages

Blog, templates, funding, and resources share a pattern: an Affairs headline, a short deck, then a card grid or filter chips. One blog article was captured ([blog-article-light-default](screenshots/blog-article-light-default.png)). The other articles and template files are the same templates.

## Auth edge

Join and sign-in leave the marketing chrome. A form sits on white at the left, a photograph at the right, with "Fewer, better introductions." set into the photo. The 2026-11-21 walk opened both walls empty and stopped. LinkedIn was visible and not clicked. Nothing was typed. See [signin-light-empty](screenshots/signin-light-empty.png), [join-light-empty](screenshots/join-light-empty.png), [mobile-signin-light-empty](screenshots/mobile-signin-light-empty.png), and [mobile-join-light-empty](screenshots/mobile-join-light-empty.png).

## Contact

A two-column page: copy and published addresses on the left, a canvas form on the right. The published addresses are the product's own. The form was not submitted. See [contact-light-default](screenshots/contact-light-default.png).

## Shop and cart

Product cards in a grid, prices under each. The cart button opens a drawer. The drawer was opened at 0 items and closed. Checkout was not started. See [shop-light-default](screenshots/shop-light-default.png) and [shop-light-cart](screenshots/shop-light-cart.png).

## Phone

At 390 the header keeps the wordmark, Join free, and an Open menu button. The drawer replaces the page. Pricing and the auth forms reflow to a single column. See [mobile-home-light-default](screenshots/mobile-home-light-default.png), [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [mobile-pricing-light-default](screenshots/mobile-pricing-light-default.png).

## Dark palette

The declared dark palette paints when `data-app-theme="system"` is set and the colour scheme is dark. The live document does not set the attribute, so a visitor in dark mode still sees the light page. [home-dark-default](screenshots/home-dark-default.png) is that declared palette, not a toggle the site offers.
