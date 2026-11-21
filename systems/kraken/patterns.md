# Kraken patterns

Public site only. Signed-in trading, deposit, and verification flows were not opened.

## App shell

The marketing shell is a sticky header (logo, product menus, Markets, About, search, language, Log in, Sign up) over a light page (`#f6f5f9`) and a multi-column footer. Screenshot: [screenshots/home-light-default.png](screenshots/home-light-default.png).

Phone width collapses the product menus into a menu button. Screenshot: [screenshots/mobile-home-light-default.png](screenshots/mobile-home-light-default.png).

## Navigation

Product names in the header are both links and menus. The map of what each item opens is [site-tree.md](site-tree.md).

## Search

Search is an overlay, not a page. It lists markets before a query is typed.

## Marketing page

Feature pages (`/pro`, `/features`, `/learn`, `/why-kraken`) share the same header, a large heading in Kraken-Brand, and a purple primary action. Screenshots: `pro-light-default.png`, `features-light-default.png`, `learn-light-default.png`.

## Price table

`/prices` is the public list. It is a marketing table, not the signed-in order book.

## Auth wall

Sign-in and sign-up are centered cards on the same page colour. What they ask for is [login-review.json](login-review.json). Screenshots: `sign-in-light-wall.png`, `sign-up-light-wall.png`. The branch stopped there.

## Not captured

Empty, loading, and error states of the signed-in app. Destructive confirmation. Feedback after a trade or deposit. Onboarding. Validation errors. Those need a signed-in session, which this capture does not have.
