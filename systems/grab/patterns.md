# Grab patterns

How the components in [components.md](components.md) combine into Grab's screens. Token paths are in
[tokens.json](tokens.json); the captures named here are in [screenshots/light/](screenshots/light). Grab has one theme, light.

## App shell and navigation

Home is a white page under a deep green header that holds a search field, a GrabCoins badge and the account avatar.
Below it sit two rows of 3D service icons (Transport, Food, Express, Mart and more, scrolling sideways with a page
indicator), two small shortcut cards (Finance, Ride to), promo cards and merchant cards. The tab bar has five items
with the scan button raised in its centre: Home, Moments, scan, Activity, Messages. It hides as Home scrolls. See
[01-home-tiles-search](screenshots/light/01-home-tiles-search.png) and [02-home-scrolled-cards](screenshots/light/02-home-scrolled-cards.png).

Each service is its own app inside the app, with its own header colour and, for GrabFood, its own tab bar (Discover,
Near Me, Offers, Cart):

| Layer | What sits there | Tokens |
|---|---|---|
| Header | Service colour behind the status bar: Home deep green, GrabFood blue, Transport and Offer Zone peach, Pickup green to teal | `color.bg.header`, `color.bg.headerEnd`, `color.service.food`, `color.service.peach` |
| Page | Lists, cards and forms on white, with grey bands between groups | `color.bg.page`, `color.bg.section` |
| Pushed page | A back arrow and a display-face title on white (Dietary preferences) or on mint (account) | `typography.title`, `color.bg.tint` |
| Sheet | Pre-prompts and flash deals over a dimmed page, rounded top corners | `color.surface.sheet`, `radius.sheet`, `color.bg.scrim` |
| Coach mark and tooltip | A white card over a scrim, or a deep green bubble, pointing at a control | `color.surface.sheet`, `color.surface.tooltip` |

The account page collapses its mint header into a compact title bar as it scrolls
([14-account-cards-list](screenshots/light/14-account-cards-list.png),
[15-account-scrolled-compact-header-new-badges](screenshots/light/15-account-scrolled-compact-header-new-badges.png)).

## Booking a ride

Transport opens on a peach header with Where to? and a Later pill, recent places and a grid of ride types
([03-transport-where-to-recents](screenshots/light/03-transport-where-to-recents.png)). Choosing a destination pushes a
page with a Now / Later segmented control, two stacked fields joined by a dotted line (pickup in blue, destination in
red), Recent / Suggested / Saved pill tabs and a list of places, each with a distance and a more button
([04-destination-focused-recent-tabs](screenshots/light/04-destination-focused-recent-tabs.png),
[05-destination-typed-suggestions](screenshots/light/05-destination-typed-suggestions.png)). The pickup step is a map
with a sheet of nearby points and a green Choose this pickup button
([06-pickup-map-sheet-primary-button](screenshots/light/06-pickup-map-sheet-primary-button.png), map masked). Ride options
list vehicles with price and wait time; the chosen one gets a green outline, and the payment row and Book Standard sit
fixed at the bottom ([07-ride-options-book-button-not-pressed](screenshots/light/07-ride-options-book-button-not-pressed.png)).

## Food and offers

GrabFood's home has a blue header with a search field and an Ask AI button, a banner, Delivery / Pickup / Dine Out
service chips, a dietary-preferences card, round category images and an orange flash-deals bar above its tab bar
([20-food-home-chips-categories-tabbar](screenshots/light/20-food-home-chips-categories-tabbar.png)). Tapping the bar
opens an orange sheet with a countdown in dark brown boxes over a list of merchants
([19-food-flash-deals-sheet-timer](screenshots/light/19-food-flash-deals-sheet-timer.png)). Offer Zone is a peach page of
membership cards and a two-column merchant grid with orange discount lines
([22-offer-zone-grid](screenshots/light/22-offer-zone-grid.png)). A merchant page puts a photo carousel above a white
card with the name in the display face, opening hours in green, tabs (Deals, Reviews, Photos, About) and voucher cards
with a compact Buy button ([08-merchant-page-tabs-voucher-buy](screenshots/light/08-merchant-page-tabs-voucher-buy.png)).

## Forms and validation

Forms are rows with an icon, a label and a trailing checkbox, a disclaimer with its own checkbox, and a full-width
button pinned at the bottom. Validation is a disabled button, not an error message: Save stays light grey until a
choice is made ([16-checkboxes-disabled-save](screenshots/light/16-checkboxes-disabled-save.png)). Focus is a darker
green border with a soft green halo ([04-destination-focused-recent-tabs](screenshots/light/04-destination-focused-recent-tabs.png)).
No error message was captured.

## Empty, loading and error states

The empty cart is a centred 3D illustration, a two-line display title, one grey line and a green text action
([21-cart-empty-state](screenshots/light/21-cart-empty-state.png)). A search that runs out of results ends with a centred
hint, If nothing caught your eye, and a lighter line under it
([18-search-results-nothing-caught-hint](screenshots/light/18-search-results-nothing-caught-hint.png)). Loading and
error states were not captured.

## Feedback and onboarding

Grab teaches with overlays. A notification pre-prompt is a sheet with an illustration and Yes / Later
([11-notification-preprompt-sheet-yes-later](screenshots/light/11-notification-preprompt-sheet-yes-later.png)); a coach
mark points at Work export with a Next button
([09-activity-coachmark-tooltip](screenshots/light/09-activity-coachmark-tooltip.png)); a deep green tooltip points at the
saved-posts button, and an Explore card floats above the tab bar
([13-moments-feed-tabs-chips-tooltip](screenshots/light/13-moments-feed-tabs-chips-tooltip.png)). A full-screen promo can
open over a service ([23-pickup-promo-interstitial](screenshots/light/23-pickup-promo-interstitial.png)). The toast that
followed Later was gone before its capture.

## Search and filtering

Search opens on a grey field with a green caret, filter chips (All, Transport, Food), Book a ride shortcuts, recent and
trending pills and recommended merchants
([17-search-focused-chips-recent-pills](screenshots/light/17-search-focused-chips-recent-pills.png)). Results filter by
a selected chip (Mart) and list outlets with offer cards
([18-search-results-nothing-caught-hint](screenshots/light/18-search-results-nothing-caught-hint.png)). In GrabFood the
service chips switch the whole page: Pickup turns the header green and shows a map strip over a list of nearby
restaurants ([24-pickup-chip-selected-map-list](screenshots/light/24-pickup-chip-selected-map-list.png), map masked).

## Data display

Activity lists trips and bills: a service icon, a coloured status (Cancelled red, Bill paid green), a title, a date in
grey, a price at the right and a blue Rebook link ([10-activity-list-status-labels](screenshots/light/10-activity-list-status-labels.png),
trip titles starting with the home address masked). Merchant rows show a square image, the name, a rating with a star,
price level, delivery fee and time ([19-food-flash-deals-sheet-timer](screenshots/light/19-food-flash-deals-sheet-timer.png)).
Settings rows are 52 pt apart with a value or a red New before the chevron
([14-account-cards-list](screenshots/light/14-account-cards-list.png)).
