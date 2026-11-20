# Oku patterns

How the public pages are built. Screenshots are 256-colour. The site tree is [site-tree.md](site-tree.md).

## App shell

A fixed 80px header on a white page. Logo left, text links centered, Sign in and Join at the right. No sidebar. Phone replaces the links with one menu button. See [home-light-default.png](screenshots/home-light-default.png) and [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

Dark is the same shell with the page at #131314 and the Join button inverted. See [home-dark-default.png](screenshots/home-dark-default.png). There is no theme control on the page. Dark follows the browser.

## Marketing home

One display line, two buttons (Join for free, App Store), a line drawing, then feature sections and a live activity feed of public books and profiles. The feed is other people's public reading activity. See [home-light-tile1.png](screenshots/home-light-tile1.png) onward for the sections below the fold.

## Explore

A heading and a grid of public book covers. No search field. See [explore-light-default.png](screenshots/explore-light-default.png).

## Pricing

Three columns: Free at $0, Premium at $35 / year, and a third plan at $125 / year. "Pay monthly" and "Pay yearly" are labels. Clicking them did not change the prices. Subscribe and Join for free go to the signup wall. See [pricing-light-default.png](screenshots/pricing-light-default.png).

## Book and profile

A public book page shows the cover, title, author, description, and three status buttons. Those buttons open the signup dialog. A public profile shows shelves. See [book-light-default.png](screenshots/book-light-default.png) and [profile-light-default.png](screenshots/profile-light-default.png).

## Review

A public review with a spoiler toggle. Opening it stays on the page. See [review-light-spoiler.png](screenshots/review-light-spoiler.png).

## Signup dialog

Join, the hero Join for free button, and a book status button open the same dialog. Escape closes it. The fields were left empty. See [home-light-join-dialog.png](screenshots/home-light-join-dialog.png).

## Walls

Sign in is a split page: form on the left, the line drawing on the right. See [signin-light-wall.png](screenshots/signin-light-wall.png). `/login` renders the 404. See [login-missing-light-default.png](screenshots/login-missing-light-default.png).

## Not on this surface

No form was submitted, so there is no validation error. No empty, loading, or error state was shown. No destructive confirmation. No search. No onboarding. Those stay not captured.
