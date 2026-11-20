# Patterns

The signed-out product is one map with panes that open over it. Screenshots are in [screenshots/](screenshots/).

## Map shell

Search is top left. The wordmark sits top centre and animates (`animate-logo`, a background-position shift of 1728px). The right rail is Menu plus the layer list (Weather radar, Satellite, Wind, Rain, Temperature, and the rest) plus Altitude. The bottom bar is overlay chips, model chips, zoom, and the legend. The canvas behind them is not a token. The body colour behind a missing tile is `#888888`.

[screenshots/map-dark-default.png](screenshots/map-dark-default.png) is the desktop map. [screenshots/map-dark-phone.png](screenshots/map-dark-phone.png) is the same URL at 390px.

## Search

Focusing the field widens it and sets `onsearch` on the body, which hides the startup weather card and the article card. Typing a place name fills a result list of 16px rows. Choosing "Oslo" opened `https://www.windy.com/59.913/10.739` and the detail strip.

[screenshots/search-dark-results.png](screenshots/search-dark-results.png)

## Place detail

The detail strip docks to the bottom: a white 12px table of hours, temperature, rain, and wind, then a red footer of product tabs (Basic, Wave and Tide, Meteogram, Wind, Pollen and air quality, Airgram). Closing it returns to the map.

[screenshots/detail-dark-oslo.png](screenshots/detail-dark-oslo.png)

## Menu

Menu opens a 400px right pane on `#3c3c3c`. The top of the rail, once the menu is open, shows Go Premium (orange) and Login (charcoal). The pane lists favourites, alerts, settings, the plugin, the route planner, and the layer catalogue. Favourites, alerts, and settings need an account. They were not entered.

[screenshots/menu-dark-open.png](screenshots/menu-dark-open.png)

## Login

Login is a centred popup, not a separate marketing page. It asks for an email address and a password, then Google, Apple, and Facebook. There is no email-only form. The fields were left empty and the popup was closed.

[screenshots/login-dark-empty.png](screenshots/login-dark-empty.png)
