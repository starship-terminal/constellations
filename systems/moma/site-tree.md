# MoMA site tree

Mapped 2026-11-21 from the public homepage at https://www.moma.org/, signed out, in headed Chrome. Desktop viewport measured 1440×900 at devicePixelRatio 1. Phone viewport measured 390×844 at devicePixelRatio 2. One light theme (`color-scheme: normal`). No theme switch.

The cookie bar was left in place on the first home shot, then hidden with CSS. Accept was never clicked. No email, password, code, phone, or address was typed. No form was submitted. Tickets, Donate, Join, and checkout were not entered.

The control map is also the shot list in [screenshots/](screenshots).

## Shell (desktop)

The header is two rows. The wordmark, Membership, Donate, and Tickets sit on the top row. Visit, Exhibitions and events, Art and artists, Store, and Search sit on the second row.

| Control | Opens |
|---|---|
| Wordmark (`a`, "Navigate to Homepage") | page https://www.moma.org/ |
| Visit (`button`, `aria-controls="visit-nav"`) | menu on the same page, role menu, full width. See [home-light-visit-menu](screenshots/home-light-visit-menu.png). |
| Exhibitions and events (`button`, `aria-controls="exhibitions-and-events-nav"`) | menu on the same page. See [home-light-exhibitions-menu](screenshots/home-light-exhibitions-menu.png). |
| Art and artists (`button`, `aria-controls="art-and-artists-nav"`) | menu on the same page. See [home-light-art-menu](screenshots/home-light-art-menu.png). |
| Store (`a`) | page https://store.moma.org/ (left the museum host). See [store-light-default](screenshots/store-light-default.png). |
| Search (`button`, `aria-controls="search-nav"`) | search disclosure on the same page. Form action `/search`, field `input[name=query]`, placeholder "Search moma.org". Not submitted. The painted panel did not survive a screenshot on this pass. |
| Membership (`button`, `aria-controls="membership-menu"`) | menu on the same page, 350px wide. See [home-light-membership-menu](screenshots/home-light-membership-menu.png). |
| Donate (`a`) | page https://donate.moma.org/. Not followed. |
| Tickets (`a`, brand blue) | page https://visit.moma.org/select. Not followed. |

Visit menu items, each a page:

| Item | Opens |
|---|---|
| Tickets | https://visit.moma.org/select (purchase). Not followed. |
| Locations, hours, and admission | https://www.moma.org/visit/ |
| Map, audio, and more | https://www.moma.org/visit/guide |
| Where to start | https://www.moma.org/visit/itineraries/ |
| Visitor guidelines and policies | https://www.moma.org/visit/visitor-guidelines-and-policies |
| Frequently asked questions | https://www.moma.org/visit/tips |
| Book a tour | https://www.moma.org/visit/tours |
| Restaurants | https://www.moma.org/visit/eating |
| Accessibility | https://www.moma.org/visit/accessibility |
| Discounts | https://www.moma.org/visit/discounts |
| Families | https://www.moma.org/visit/families |
| Visit MoMA PS1 | https://www.momaps1.org/ (leaves the host) |

Exhibitions and events menu items:

| Item | Opens |
|---|---|
| Current and upcoming exhibitions | https://www.moma.org/calendar/exhibitions |
| Exhibition history | https://www.moma.org/calendar/exhibitions/history |
| Events calendar | https://www.moma.org/calendar |
| Film series | https://www.moma.org/calendar/film |
| Performances | https://www.moma.org/calendar/?happening_filter=Performances&location=both |

Art and artists menu items:

| Item | Opens |
|---|---|
| Art | https://www.moma.org/collection/ |
| Artists | https://www.moma.org/artists/ |
| Audio | https://www.moma.org/audio/ |
| Magazine | https://www.moma.org/magazine/ |
| Art terms | https://www.moma.org/collection/terms/ |
| Online courses | https://www.coursera.org/moma (leaves the host) |
| Youtube | https://www.youtube.com/@themuseumofmodernart (leaves the host) |

Membership menu items:

| Item | Opens |
|---|---|
| Become a member | https://membership.moma.org/ (marketing). Not submitted. |
| Log in | https://www.moma.org/auth/login, which redirects to the auth host. Login wall. Branch stopped. |

## Phone (390)

The second nav row collapses. A button `[data-mobile-menu-trigger]` (hamburger, no aria-label) opens a drawer on the same page. Tickets stays in the header. The drawer lists Visit, Exhibitions and events, Art and artists (each a button that expands the same destinations as desktop), Store, Search, Donate, Become a member, and Log in. Close is the same button, now an X. See [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).

## Home https://www.moma.org/

| Control | Opens |
|---|---|
| Plan your visit | page https://www.moma.org/visit/ |
| Exhibition cards (Brancusi, Taking Back Our Space, and the others on the rail) | exhibition page `/calendar/exhibitions/<id>` |
| Previous slide / Next slide | in-page carousel, same page |
| Donate to the Modern Fund | https://donate.moma.org/. Not followed. |
| Find your favorites, and the artwork tiles | collection work pages `/collection/works/<id>` |
| View the calendar | https://www.moma.org/calendar |
| Event cards | event pages `/calendar/events/<id>` |
| Films, Families, Members, Talks chips | calendar filtered by happening |
| Shop at MoMA Design Store | https://store.moma.org/pages/stores |
| Get UNIQLO tickets | https://visit.moma.org/select/uniqlo. Not followed. |
| Magazine cards | `/magazine/articles/<id>` |
| Store promo tiles | store collection pages on store.moma.org |
| See what's on (PS1) | https://www.momaps1.org/ |
| Subscribe (footer, "Your email") | newsletter form. Not typed, not submitted. |

## Footer (every museum page)

About us (`/about/`), Support (`/support/`), Research (`/research/`), Teaching (`/teaching/`), Magazine (`/magazine/`), Log in (`/auth/login`, login wall).

MoMA location block links to `/visit/index`. The street line is published museum copy. MoMA PS1 links to https://www.momaps1.org/.

Privacy policy (`/about/about-this-site/#privacy-policy`), Terms of use (`/about/about-this-site/#terms-of-use`), Visitor guidelines and policies (`/visit/visitor-guidelines-and-policies`).

Social icons leave the site (Instagram, Facebook, X, Threads, TikTok, Spotify, WhatsApp, YouTube).

See [home-light-footer](screenshots/home-light-footer.png).

## Pages captured

| Page | What else it opens |
|---|---|
| https://www.moma.org/visit/ | Location anchors `#moma-info` and `#ps1-info`, Get directions (Google Maps, not followed), Book tickets (purchase, not followed), stores, restaurants, membership marketing, FAQ, guide, families, accessibility, film admission, tours. See [visit-light-default](screenshots/visit-light-default.png) and [mobile-visit-light-default](screenshots/mobile-visit-light-default.png). |
| https://www.moma.org/calendar/exhibitions | Exhibition cards open `/calendar/exhibitions/<id>`. No filter buttons on the captured view. See [exhibitions-light-default](screenshots/exhibitions-light-default.png). |
| https://www.moma.org/calendar/exhibitions/5910 | Brancusi. Floor link, artist page, catalogue (store product, not bought), audio playlist, magazine excerpts, installation images, related events. See [exhibition-light-default](screenshots/exhibition-light-default.png). |
| https://www.moma.org/collection/ | Search field "Search artists and works" (not submitted), checkboxes (Has image, On view, Recent acquisition, Uncatalogued works), type and date selects, artwork cards. See [collection-light-default](screenshots/collection-light-default.png). |
| https://www.moma.org/calendar | Event listing. See [calendar-light-default](screenshots/calendar-light-default.png). |
| https://store.moma.org/ | Design Store home. Nav: New, Gifts, Holiday, For the Home, Office, Tech, Apparel & Accessories, Prints & Artists, Books, Kids & Games, Only at MoMA, Sale. Account, wish list, and cart icons. An offer dialog ("Enjoy 10% Off") opened and was closed. The email field was not typed. Claim Your Offer was not pressed. See [store-light-default](screenshots/store-light-default.png). |
| https://store.moma.org/collections/new | Listing, 628 items. Categories, Product Type, and Price open filter controls on the same page. Sort By changes the listing. Product tiles open product pages. None were added to the bag. See [store-listing-light-default](screenshots/store-listing-light-default.png). |
| https://store.moma.org/search?q=zzzznotaproduct999 | Empty search. Title "0 results found". The page also shows a "This field is required" note on the footer email field. Nothing was typed into that field and Sign Up was not pressed. See [store-search-empty-light-default](screenshots/store-search-empty-light-default.png). |
| https://store.moma.org/cart | Empty cart. "Your shopping cart is empty." Checkout was not entered. See [store-cart-empty-light-default](screenshots/store-cart-empty-light-default.png). |
| https://www.moma.org/members/ | HTTP 404, "Page not found", Ruscha's *OOF*. See [members-missing-light-default](screenshots/members-missing-light-default.png). Membership marketing is https://membership.moma.org/. |

## Login wall (recorded, not entered)

| Control or URL | What loaded |
|---|---|
| Membership, Log in | Redirects from https://www.moma.org/auth/login to the auth host. Heading "Log in or sign up for a free account". Empty email field, Continue, "We'll email you a one-time code." No identity-provider buttons. Branch stopped. Nothing typed. Continue not pressed. See [login-light-default](screenshots/login-light-default.png). |
| Phone drawer, Log in | Same wall. Not followed from the phone shot. |

`login-extracted` stays not-started.
