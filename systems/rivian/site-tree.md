# Rivian public site tree

Mapped from https://rivian.com/ on 2026-11-21 in headless Chromium at 1440×900, before screenshots. The homepage returned HTTP 200, title "Rivian: Electric Vehicles Designed For Adventure". Cookie banner (Ketch, labelled "privacy banner") was present. Reject All was clicked where the control was in the viewport; when it sat outside the viewport the banner was hidden after the click attempt so it would not cover the page. No form was submitted.

Sign-in is a wall. The header "Sign in" link points at `https://rivian.com/auth/login?app=rivian&rd=https%3A%2F%2Frivian.com%2F`. That branch stops there. Password was not submitted.

## Header chrome

| Control | Opens |
|---|---|
| Skip to main | `#main` on the current page |
| Home (logo) | https://rivian.com/ |
| Vehicles (button, `aria-expanded`) | Header mega-menu. See Vehicles. |
| Charging (button) | Header mega-menu. See Charging. |
| Technology (button) | Header mega-menu. See Technology. |
| Discover (button) | Header mega-menu. See Discover. |
| Gear Shop (button) | Header mega-menu. See Gear Shop. |
| Demo drive | https://rivian.com/demo-drive/book |
| Have a question? | Chat panel. The page loads an iframe at `https://rivian.com/leads/keep-up-open?style=narrow` and a Google reCAPTCHA enterprise frame. Not a form submit. The panel's own fields are not filled. |
| Sign in | Login wall. Stop. |
| Open (`#navbar-trigger-accordion`, `aria-controls="navbar-panel"`) | Mobile/narrow accordion panel. Same destinations as the mega-menus, collapsed into one panel. |

## Vehicles menu

| Control | Opens |
|---|---|
| Design yours (R1S) | https://rivian.com/configurations/builder?MODEL=R1S |
| Explore (R1S) | https://rivian.com/r1s |
| Design yours (R1T) | https://rivian.com/configurations/builder?MODEL=R1T |
| Explore (R1T) | https://rivian.com/r1t |
| Explore (R2) | https://rivian.com/r2 |
| Design yours (R2, also in the hero) | https://rivian.com/configurations/builder/r2 |
| Compare models | https://rivian.com/compare |
| Trade-in | https://rivian.com/trade-in/vehicle-info (a form page; not submitted) |
| Current offers | https://rivian.com/offers |
| Inventory | https://rivian.com/configurations/list. The page opens an empty postal-code dialog. The field was not filled and Continue was not clicked. |
| Pre-owned | https://rivian.com/configurations/list?INVENTORY_TYPE=PRE_OWNED_VEHICLE |
| Purchasing | https://rivian.com/experience/purchasing |
| Financing | https://rivian.com/support/financing-and-payments |
| Insurance | https://rivian.com/experience/insurance |
| R3 | https://rivian.com/r3 |
| Fleet | https://rivian.com/fleet |

## Charging menu

| Control | Opens |
|---|---|
| How charging works | https://rivian.com/experience/charging |
| Charging at home | Same page, anchor `#charging-home-paralax` |
| Plan a roadtrip | Same page, anchor `#trip-visualizer-form` (a form; not submitted) |
| Explore charging map | Same page, anchor `#map` |

## Technology menu

| Control | Opens |
|---|---|
| Digital experience | https://rivian.com/technology |
| Autonomy features | https://rivian.com/autonomy |
| Vehicle connectivity | https://rivian.com/connect-plus |

## Discover menu

| Control | Opens |
|---|---|
| Visit our spaces | https://rivian.com/spaces |
| Learn about service | https://rivian.com/experience/service |
| Get support | https://rivian.com/support |
| Our mission | https://rivian.com/our-company |
| Leadership | Same page, `#leadership` |
| Impact | https://rivian.com/scaling-responsibly |
| Investors | https://rivian.com/investors |
| Stories | https://rivian.com/stories |
| Newsroom | https://rivian.com/newsroom |
| Careers | https://careers.rivian.com/careers-home (other host; public) |

## Gear Shop menu

| Control | Opens |
|---|---|
| All gear | https://rivian.com/gear-shop |
| Wheels and tires | https://rivian.com/gear-shop/c/wheels-and-tires |
| Adventure gear | https://rivian.com/gear-shop/c/adventure-gear |
| Charging products | https://rivian.com/gear-shop/c/charging |
| Lifestyle | https://rivian.com/gear-shop/c/lifestyle |

## Homepage body

| Control | Opens |
|---|---|
| Design yours (hero) | https://rivian.com/configurations/builder/r2 |
| Book a drive (hero) | https://rivian.com/demo-drive |
| Explore more (Autonomy & AI Day) | https://rivian.com/events/autonomy-and-ai-day. The page shows an empty signup form. Fields were not filled and Sign up was not clicked. |
| See all offers | https://rivian.com/offers |
| Shop now (R1S inventory) | https://rivian.com/configurations/list with a featured R1S query |
| Shop now (holiday gift guide) | https://gearshop.rivian.com/pages/2026-holiday-gift-guide (other host) |
| Design your R1T / R1S | Builder URLs above |
| Previous slide / Next slide | In-page vehicle carousel. No navigation. |
| Explore R1S / R2 / R1T | Model pages above |
| Technology / Performance / Design (buttons) | In-page tabs on the homepage feature band |
| Explore the latest | https://rivian.com/technology |
| Explore R1S Tri / R1T Tri | https://rivian.com/r1s-tri and https://rivian.com/r1t-tri |
| Explore (space card) | A single space page. It shows a street address, so the branch was not captured. |
| See all locations | The locations index. It is a list of street addresses, so the branch was not captured. |
| Book a drive (space card) | A booking form. Not submitted. |
| Explore charging | https://rivian.com/experience/charging |
| Shop | Inventory filtered to R1S |
| Get updates | https://rivian.com/connect/tell-us-more (a form page; not submitted) |
| Trade in | Trade-in form page; not submitted |
| Service | https://rivian.com/experience/service |
| Subscribe (footer, twice) | Newsletter control. Not filled and not submitted. |
| Watch the video | In-page video dialog or player |
| Full offer details | Offer pages under https://rivian.com/offers/… |
| Select states | Support article on leasing regions (the homepage href carried ad-click query parameters; those are not stored) |

## Footer

| Control | Opens |
|---|---|
| R1T, R1S, R2, Fleet | Model and fleet pages |
| Shop new inventory | https://rivian.com/configurations/list |
| Shop pre-owned | Inventory with `INVENTORY_TYPE=PRE_OWNED_VEHICLE` |
| Spaces | https://rivian.com/spaces |
| Gear Shop | https://rivian.com/gear-shop |
| Our Company | https://rivian.com/our-company |
| Stories | https://rivian.com/stories |
| Pre-Owned | https://rivian.com/experience/pre-owned |
| Purchasing, Charging, Insurance, Service | Experience pages |
| Investors | https://rivian.com/investors |
| Careers | https://rivian.com/careers (redirects; the menu also links careers.rivian.com) |
| Support | https://rivian.com/support |
| Privacy | https://rivian.com/privacy |
| Data Privacy Notice | https://rivian.com/privacy/notice (banner link uses /en-US/privacy/notice) |
| Legal | https://rivian.com/legal |
| Rivian's Terms | https://rivian.com/legal/terms |
| Recalls | https://rivian.com/support/article/recall-information |
| Accessibility | https://rivian.com/accessibility |
| Your privacy choices | `https://rivian.com/null` (the live href is the string "null"; recorded, not followed as a page) |
| LinkedIn, Instagram, X, YouTube | Off-site social profiles. Not captured. |
| Locale links (`/en-CA`, `/fr-CA`, `/en-GB`, and other region prefixes) | Same site in another locale. US English is the capture. Other locales are the same chrome and were not recaptured. |

## Walls and forms (recorded, not entered)

| URL | Why it stops |
|---|---|
| https://rivian.com/auth/login | Email and password wall. Password was not submitted. |
| https://rivian.com/connect/tell-us-more | Updates form. Not filled. |
| https://rivian.com/trade-in/vehicle-info | Trade-in form. Not submitted. |
| https://rivian.com/demo-drive and /demo-drive/book | Booking flow. Not submitted. |
| Footer Subscribe | Newsletter. Not filled. |
| Charging "Plan a roadtrip" | Trip form on the charging page. Not submitted. |
| https://rivian.com/configurations/list | Postal-code dialog. Field left empty. Continue not clicked. |
| https://rivian.com/events/autonomy-and-ai-day | Signup form. Fields left empty. Sign up not clicked. |

## Cookie banner

| Control | What it does |
|---|---|
| Accept All | Consent accept. Not clicked. |
| Reject All | Consent reject. Clicked when reachable. |
| Manage Preferences | Opens cookie preference UI. Opened only to record the dialog, not to save preferences. |
| View Data Privacy Notice | https://rivian.com/en-US/privacy/notice |
| close banner | Dismisses the banner. |
