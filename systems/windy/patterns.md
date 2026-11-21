# Patterns

The signed-out product is one map with panes that open over it. Screenshots are in [screenshots/](screenshots/). The control map is [site-tree.md](site-tree.md).

## Map shell

Search is top left. The wordmark sits top centre and animates (`animate-logo`, a background-position shift of 1728px). The right rail is Menu plus the layer list (Weather radar, Satellite, Wind, Rain, Temperature, and the rest) plus Altitude. The bottom bar is overlay chips, model chips, zoom, and the legend. The canvas behind them is not a token. The body colour behind a missing tile is `#888888`.

[screenshots/map-dark-default.png](screenshots/map-dark-default.png) is the desktop map. [screenshots/map-dark-phone.png](screenshots/map-dark-phone.png) is the same public map at 390px. Phone chrome replaces the right rail with a red menu disc and a short icon stack.

## Search

Focusing the field widens it and sets `onsearch` on the body, which hides the startup weather card and the article card. Typing a place name fills a result list of 16px rows. Choosing a city row opens the detail strip. The map URL then carries coordinates. Those coordinates are not stored in this package.

[screenshots/search-dark-results.png](screenshots/search-dark-results.png)

## Place detail

The detail strip docks to the bottom: a white 12px table of hours, temperature, rain, and wind, then a red footer of product tabs (Basic, Wave and Tide, Meteogram, Wind, Pollen and air quality, Airgram). Closing it returns to the map.

[screenshots/detail-dark-place.png](screenshots/detail-dark-place.png)

## Menu

Menu opens a 400px right pane on `#3c3c3c`. The top of the rail shows Go Premium (orange) and Login (charcoal). The pane lists favourites, alerts, settings, the plugin installer, the route planner, the uploader, and the layer catalogue.

[screenshots/menu-dark-open.png](screenshots/menu-dark-open.png)

Favorites and alerts open as empty public panes while signed out. They do not raise a login wall. Settings does not open a pane while signed out.

[screenshots/favorites-dark-empty.png](screenshots/favorites-dark-empty.png) and [screenshots/alerts-dark-empty.png](screenshots/alerts-dark-empty.png).

The plugin list and the uploader are public panes. No plugin was loaded and no file was chosen.

[screenshots/plugins-dark-list.png](screenshots/plugins-dark-list.png) and [screenshots/uploader-dark-empty.png](screenshots/uploader-dark-empty.png).

## Login

Login is a centred popup, not a separate marketing page. It asks for an email address and a password, then Google, Apple, and Facebook. Register Now swaps the same popup for email, username, password, confirm password, a newsletter checkbox, and a captcha. There is no email-only form. The fields were left empty. No provider was clicked. The captcha was not solved.

[screenshots/login-dark-empty.png](screenshots/login-dark-empty.png) and [screenshots/register-dark-empty.png](screenshots/register-dark-empty.png).
