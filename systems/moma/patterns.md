# MoMA patterns

Public marketing pages. One light theme. Desktop shots are 1440 by 900 at 1x. Phone shots are 390 wide at 2x.

## App shell

A white header, 166px tall at 1440. Wordmark left. Membership, Donate (`#eee`), and Tickets (`#00b7f2`) on the top row. Visit, Exhibitions and events, Art and artists, Store, and search on the second row. [home-light-default](screenshots/home-light-default.png).

On a 390-wide viewport the second row collapses into a menu button. Tickets stays. [mobile-home-light-default](screenshots/mobile-home-light-default.png).

The footer is `#444444`. Measured `rgb(68, 68, 68)` on `footer`.

## Home

A full-bleed hero, then a Welcome heading at 60px weight 900, a 22px line, hours in 18px regular, and a black Plan your visit button. Exhibition cards follow. [home-light-full](screenshots/home-light-full.png).

A cookie bar sits at the bottom. It was left unanswered. [home-light-cookie](screenshots/home-light-cookie.png).

## Visit

H1 "Locations, hours, and admission" at 60px. A gray band (`#eee` family) holds the location block, including the published street address. [visit-light-default](screenshots/visit-light-default.png).

## Exhibitions

H1 "In the galleries". A brand-yellow panel (`#fac300`, `--color--brand--6`) sits beside a collection image. [exhibitions-light-default](screenshots/exhibitions-light-default.png).

## Membership marketing

`https://membership.moma.org/` is a separate host with the same type. Four square cards in membership colours, each with Join or renew (black) and Gift it (white). Join was not pressed. [membership-light-default](screenshots/membership-light-default.png).

## Menus

Visit, Exhibitions and events, and Art and artists open full-width menus on the same page. Membership opens a short menu (Become a member, Log in). The phone hamburger opens a drawer with the same destinations. [home-light-visit-menu](screenshots/home-light-visit-menu.png), [home-light-exhibitions-menu](screenshots/home-light-exhibitions-menu.png), [home-light-art-menu](screenshots/home-light-art-menu.png), [home-light-membership-menu](screenshots/home-light-membership-menu.png), [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).

## Store

Store leaves www.moma.org for store.moma.org. The home is a promo carousel. New arrivals is a product grid with Categories, Product Type, and Price. A nonsense query returns an empty result. The cart, opened with nothing added, says the bag is empty. An offer dialog was closed. No email was typed and checkout was not entered. [store-light-default](screenshots/store-light-default.png), [store-listing-light-default](screenshots/store-listing-light-default.png), [store-search-empty-light-default](screenshots/store-search-empty-light-default.png), [store-cart-empty-light-default](screenshots/store-cart-empty-light-default.png).

## Search

The search control opens a field on the same page. Placeholder "Search moma.org". Nothing was submitted. The painted panel did not survive a screenshot on the 2026-11-21 pass. The earlier shot is [home-light-search](screenshots/home-light-search.png).

## Login

`/auth/login` redirects to the auth host and paints a centered card: wordmark, "Log in or sign up for a free account", an empty email field, a black Continue button. Continue was not pressed. Nothing was typed. [login-light-default](screenshots/login-light-default.png).

## Missing page

`/members/` is a 404 with Ruscha's *OOF*. [members-missing-light-default](screenshots/members-missing-light-default.png). Membership marketing stays at membership.moma.org.
