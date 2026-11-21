# Components

Public Nomad storefront (`nomadgoods.com/sg/`), signed out, 2026-11-21. Crops were not cut: the capture recorded whole pages. States below are Observed in those pages unless a computed style is named.

## Inventory

| Component | Present | States seen | Evidence |
|---|---|---|---|
| Button | yes | default (Shop Now light pill, Sold Out dark pill) | [home](screenshots/home-light-default.png), [pdp](screenshots/pdp-light-default.png) |
| Icon button | yes | search, cart, notification, locale, menu close | [search](screenshots/home-light-search.png), [cart](screenshots/home-light-cart.png) |
| Link | yes | nav, footer, announcement | [home](screenshots/home-light-default.png) |
| Text field | yes | search empty, footer email empty (not filled) | [search](screenshots/home-light-search.png) |
| Text area | not present | | not on the public pages opened |
| Select | not captured | locale control opened but the list did not paint in the shot | [locale](screenshots/home-light-locale.png) |
| Checkbox | not captured | cookie preference checkboxes exist in the banner DOM; the banner was hidden, not opened | |
| Radio | not present | | |
| Switch | not present | | |
| Tabs | not present | PDP colour choices are swatches, not tabs | [pdp](screenshots/pdp-light-default.png) |
| Menu | yes | desktop Cases mega menu, phone burger | [menu](screenshots/home-light-menu-cases.png), [phone menu](screenshots/mobile-home-light-menu.png) |
| Tooltip | not present | | |
| Dialog | yes | Klaviyo signup (closed, not submitted), empty cart drawer | [signup](screenshots/home-light-signup.png), [cart](screenshots/home-light-cart.png) |
| Toast | not present | | no action was submitted |
| Card | yes | product tiles, feature deals | [cases](screenshots/cases-light-default.png) |
| List row | yes | phone menu rows, footer link columns | [phone menu](screenshots/mobile-home-light-menu.png) |
| Table | not present | | |
| Avatar | not present | community photos are product photography, not account avatars | |
| Badge | yes | NEW, HOT, BLACK FRIDAY pills in the menus | [menu](screenshots/home-light-menu-cases.png) |

## Shared values

- Primary button: Gotham-Bold 16 / 17.76, tracking -0.64px, height 48px, radius 100px, padding 0 24px. Dark face `#2f2f2f`, white label, 1px black border, inset shadow `rgb(14, 14, 14)`. Source: `raw/pdp-measured.json` and `buttons-FS3QHQ7I.css`.
- Light button: white gradient, inset white lip, outer hairline `rgba(0, 0, 0, 0.06)`. Source: Shop Now computed box-shadow in `raw/computed-roles.json`.
- Nav bar: white, 70px tall, radius 25px, horizontal padding 10px. Source: `raw/measured-chrome.json`.
- Body: Aleo 16 / 24, `#000` on `#f3f3f3`. Source: `raw/computed-roles.json`.

## Gaps

- Hover, focus-visible, pressed and disabled were not measured as separate crops. The dark button stylesheet declares an `:active` inset flip (`buttons-FS3QHQ7I.css`). That rule was read. It was not photographed.
- The Sale label's orange was seen in screenshots and was not a computed colour on the link (`rgb(0, 0, 0)`). Not captured as a token.
- No error, loading, toast, or validation state. No form was submitted.
- Account, checkout and the waitlist were not entered.
