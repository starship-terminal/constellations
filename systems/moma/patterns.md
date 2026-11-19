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

## Search

The search control opens a field over a dimmed page. Placeholder "Search moma.org", 40px, colour `rgba(0, 0, 0, 0.54)`. Nothing was submitted. [home-light-search](screenshots/home-light-search.png).

## Login

`/auth/login` is a centered card: wordmark, "Log in or sign up for a free account", an underline email field, a black Continue button. Continue was not pressed. A second visit to the same URL hit a Cloudflare challenge and that launch stopped. [login-light-default](screenshots/login-light-default.png).
