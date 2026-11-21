# Airbnb public site tree

Mapped on 2026-11-21 from the signed-out homepage, before screenshots. `https://www.airbnb.com` geo-redirected to `https://www.airbnb.com.sg/` (title: "Airbnb | Holiday rentals, cabins, beach houses & more"). The same product, Singapore market. No cookie banner. Light theme only (`color-scheme: normal`). Stopped at the login dialog.

## Header

| Control | Opens |
|---|---|
| Logo, "Airbnb homepage" | `/` (this page) |
| Tab "All" | `/` |
| Tab "Homes" | `/homes` |
| Tab "Hotels" | `/hotels` |
| Tab "Experiences" | `/experiences` |
| Tab "Services" | `/services` |
| Globe button, "Log in or sign up" | Dialog "Log in or sign up" on this page. Phone number or email field, Continue, Continue with Google, Continue with Apple, Close. Wall. Not submitted. Identity providers not clicked. |
| Hamburger, "Main navigation menu" | Dropdown on this page: Languages & currency (button, empty href), Help Centre (`/help`), Become a host (button, "It's easy to start hosting and earn extra income."), Refer a host (`/refer?r=67`), Find a co-host (`/co-hosts/home`), Log in or sign up (`/signup_login`, same wall) |

## Search capsule

| Control | Opens |
|---|---|
| Where, search input, placeholder "Search destinations" | Opens a "Suggested destinations" list on this page: Nearby, plus places such as Kuala Lumpur, Malacca, Tokyo, Bangkok, Johor Bahru District, Osaka. No text typed. Search not submitted. |
| When, "Add dates" | Inline panel under the capsule. Tabs "Dates" and "Flexible". Dates shows a two-month calendar (November 2026, December 2026) with month arrows. Stays on `/`. |
| Who, "Add guests" | Inline panel under the capsule. Steppers for Adults (Ages 13 or above), Children (Ages 2–12), Infants (Under 2), Pets ("Bringing a service animal?"). Stays on `/`. |
| Search button | Submits the search. Not clicked. |

## Homepage body

| Control | Opens |
|---|---|
| Section title, for example "Homes in Johor Bahru District" | `/s/<place>/homes` with place id and flexible-date params (carousel "see all") |
| Listing card photo | `/rooms/<id>` with check-in, check-out and photo id query params |
| Heart, "Add to wishlist: …" | Login wall (not clicked this pass; prior capture found a sign-up sheet) |
| Rail previous / next | Scrolls the carousel on this page |
| "See all" at the end of a rail | Same `/s/<place>/homes` URL as the section title |

Rails seen above the fold: Homes in Johor Bahru District, Popular homes in Ho Chi Minh City, Places to stay in Batam. Further rails load on scroll.

## Confirmed public pages

Visited signed out, no wall:

| Path | What it is |
|---|---|
| `/homes` | Homes tab. Same shell as home, with home rails (Kuala Lumpur above the fold on this visit). |
| `/hotels` | Hotels tab. Title "Airbnb Hotels - Find and Book Hotels Worldwide". Hotel cards (Singapore above the fold). |
| `/help` | Help Centre. "Hi, how can we help?", search, "Browse all topics" (`/help/all-topics`), article links. "Log in or sign up" goes to `/login?redirect_url=/help`. Not followed. |
| `/host/homes` | Host landing. "Your home could make money on Airbnb". |

## Pages photographed from this tree

Public, no login: home (default, search-open, card-hover), `/experiences`, `/services`, a public `/s/Tokyo--Japan/homes` results page, one `/rooms/<id>` linked from those results, `/help`, `/host/homes`. Desktop 1440 and phone 390 for home and search.

Not entered: `/signup_login`, Continue, Google, Apple, wishlist, search submit, any form.
