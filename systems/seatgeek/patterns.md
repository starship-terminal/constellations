# SeatGeek patterns

Public signed-out pages, 19 November 2026. Viewport measured `1169×731` at `devicePixelRatio` 2, then `390×844` at the same ratio. No screenshots: the preview browser did not produce frames.

## App shell

Category pages (`/`, `/nfl-tickets`, `/concert-tickets`, `/cities`) paint a dark hero and a transparent header. About and Help paint a white header, background `#ffffff`.

Header height is `80px` at 1169px wide and `68px` at 390px. At 390px the Sports, Music, Shows and Cities links have height `0` (collapsed). Sign in stays a `40×78` glass pill.

Footer is white, padding `60px`, with a `1px` top hairline `rgba(0, 0, 0, 0.08)`.

## Search

Home search is a glass pill, placeholder "Search or ask anything", radius `100px`, height `46px`. It was not submitted. A second combobox input exists in the header DOM at height `64px` and was not the visible field.

## Filtering

`/nfl-tickets` and `/concert-tickets` show Location, Filter by date and Price as `32px` pills, radius `100px`, border `1px #dedddb`. The location pill was selected: background `#181818`, text `#ffffff`. The date and price panels were not opened.

## List

Event rows stack date (`17px` weight `700`), time (`#767575`), title (`17px` weight `700`) and a price pill. Team rows are `52px` links, radius `12px`. City guides are a plain link list.

Empty state on the home feed, geo-located to Singapore: "Sorry, there are no events near you." Size `17px`, weight `650`, color `#181818`.

## Marketing hero

Home h1 "Be good at seats" is `32px` / `46px` weight `700`, tracking `-0.32px`, white, on a `#120100` field with a `#3a0504` radial gradient. At 390px the same h1 is `26px`. Category h1s are `48px` / `56px`, weight `750` on NFL.

## Help

`/help` is a light page. H1 "How can we help?" computed at `81.83px` / `85.92px` weight `800` in the 1169px viewport. The composer is a white field, radius `20px`. Suggestion chips ("Where are my tickets?") are white, radius `18px`, `1px` `#dedddb` ring. The chat button is the brand coral. Nothing was submitted.

## Onboarding and account

The email dialog asked for an address and was closed. It was not submitted. `/login` returned a DataDome interstitial and was left. No account was created. No card, phone number or checkout was entered.

## Not captured

Signed-in account, seat map, checkout, seller flow, validation errors, destructive confirmation, toast feedback, and a painted dark theme.
