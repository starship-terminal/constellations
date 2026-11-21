# Components

Public signed-out Curater, 2026-11-21. Crops are cut from the raw captures. Values are token names where a token holds the same reading.

## Button

The signed-out action is a white pill, 58px tall, 16px type, weight 500, 1px border, radius 9999px.

| State | Evidence |
|---|---|
| default | [components/crops/button-signin-default.png](components/crops/button-signin-default.png) |
| hover | [components/crops/button-signin-hover.png](components/crops/button-signin-hover.png). Computed fill did not change |
| focus | [components/crops/button-signin-focus.png](components/crops/button-signin-focus.png). A separate ring width was not isolated |
| pressed | not captured |
| disabled | not captured. Add to my taste is disabled until sign-in, and was not measured as its own specimen |
| loading | not present on this control |

The phone search submit is a filled near-black pill: [components/crops/button-search-default.png](components/crops/button-search-default.png).

## Icon button

Desktop rail icons are 48px hit targets: Home, Feed, Taste Profile, Notifications, Profile, Create, Settings. Phone header icons are 40px: Feed, Taste Profile, Search, Menu. See [screenshots/home-light-default.png](screenshots/home-light-default.png) and [screenshots/mobile-home-light-default.png](screenshots/mobile-home-light-default.png).

## Link

Footer and legal links are text links to `/privacy` and `/terms`. Feed cards link to `/curation/<id>`. Curator names link to `/<handle>`. Tag chips link to `/feed?tag=<id>`.

## Text field

Feed search opens an inline field with placeholder "Search curations...". Phone search opens an overlay with placeholder "Type anything" and a Search submit. Nothing was submitted.

| State | Evidence |
|---|---|
| default | [components/crops/field-search-default.png](components/crops/field-search-default.png) |
| focus | [screenshots/feed-light-search-focus.png](screenshots/feed-light-search-focus.png) |
| error | not present |

## Tabs

Featured and For You are text tabs, 40px tall, 16px, weight 500. Featured is the default. See [screenshots/feed-light-default.png](screenshots/feed-light-default.png) and [screenshots/feed-light-for-you.png](screenshots/feed-light-for-you.png).

## Menu

Settings opens a 160px menu, 12px radius, 4px padding, white fill: Settings, Extension, Privacy, Terms, About, Sign in. See [components/crops/menu-settings-default.png](components/crops/menu-settings-default.png).

More on the feed opens Subscriptions, Contributors, and seven categories. See [components/crops/menu-more-default.png](components/crops/menu-more-default.png).

Phone Menu opens a sheet: Settings, Privacy, Terms, About, Sign in. Extension is desktop-only in that menu. See [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

## Dialog

Notifications, Profile, and Create open the same sign-in dialog: title "Sign in", a close button, and Continue with Google. Scrim is `rgba(0, 0, 0, 0.5)`. See [components/crops/dialog-signin-default.png](components/crops/dialog-signin-default.png). Google was not clicked.

## Card

Home digest cards and feed cards share a light surface, a large radius, a category label, a title, and a curator row. Count chips sit on the image. See [screenshots/feed-light-default.png](screenshots/feed-light-default.png).

## Badge

Feed cards show a numeric save count. The profile shows a yellow Curator chip. See [screenshots/profile-light-default.png](screenshots/profile-light-default.png).

## Avatar

Curator rows use a small circular avatar. No signed-in avatar was available.

## Gaps

Text area, select, checkbox, radio, switch, tooltip, toast, and table were not on the public surface. Toast CSS exists for Sonner and was not shown. Hover and pressed states of the pill were not a separate paint. Dark theme is not present.
