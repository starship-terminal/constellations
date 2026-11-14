# Pages

expedia.com answers automation with a 429 "Bot or Not?" challenge, so the
pages were captured as Wayback snapshots served locally, painted with
Expedia's live travel-assets.com stylesheets and fonts. Geometry numbers below
are from [layout.json](layout.json); screenshots are in
[../screenshots](../screenshots).

## home (`/`)

Wayback `20260207171241 https://www.expedia.com/`, read signed out.

- 72 px global header: Expedia logo, Shop travel, USD currency, List your
  property, Support, Trips, notifications bell, Sign in. Sticky.
- Hero photograph with the Reckless XPD display title ("The one place you go
  to go places").
- The multi-product search card (1200 x 252 at 1440): product tabs (Stays,
  Flights, Cars, Packages, Things to do, Cruises), three uitk-field triggers —
  Where to?, Dates, Travelers — each 344 x 48, and the 83 x 48 blue Search
  button; a Bundle & Save checkbox under the row.
- A pale-blue promo band re-themed `data-theme-light="marketing-3"`.
- Deals carousels (uitk-carousel, items ~270 wide) with save hearts.
- Content column: 1248 px, centred (x 96 at 1440, x 336 at 1920), full-bleed
  at 1024 and 390. The search form's field row is a 4-column grid
  (344.3 x3 + 83, 12 px gap).
- Footer link columns.

## search (`/Hotel-Search`)

Wayback `20261030191926 https://www.expedia.com/Hotel-Search`, a public
results page for Toronto (221 properties).

- The same 72 px header, then a compact search form (`form#lodging_search_form`,
  1016 x 48) repeating the three fields inline.
- "Filter by stay types" segmented control (All stays / Hotels / Homes,
  selected-and-disabled radios) and the "Sort by recommended for you"
  uitk-pill.
- Left rail (~236 wide): a static Google-map card ("View in a map"), then the
  Filter by form — property-name field, Property class checkboxes, Guest
  rating radios, a compare-properties switch.
- Result cards (756 x 232): a 21:9 gallery with paging arrows and a save
  heart, VIP badge, name, amenity rows, "Fully refundable" / "Reserve now,
  pay later" lines, rating pill, urgency note ("We have N left"), nightly and
  total prices, "Sign in for extra savings" pill.

## home-i (`/`, hydrated)

The same archived home page run with Expedia's own JavaScript enabled. Its
GraphQL/API refetches fail on the local copy, but UI-only panels still open:

- Dates → the two-month calendar `uitk-dialog` (652 x 559) with a selected
  day, range chip and Done button.
- Travelers → the stepper menu (375 x 318).
- Where to? → the destination panel (376 x 510) with its search input.
- Flights tab → the two-leg flight form variant.

## mobile

The same two pages at 390 x 844, 2x DPR, iPhone UA, scripts blocked. The
search card stacks vertically (fields 58-342 wide); the calendar opens as a
sheet.
