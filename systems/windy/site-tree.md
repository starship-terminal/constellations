# Site tree

Public map at [windy.com](https://www.windy.com/), product `51.4.4.ind.c444`, signed out, 2026-11-21. The homepage is the map. Controls open panes on that map, or they leave the map. A login or signup wall ends the branch.

Paths below have no query string. The live map puts the camera in the query. That camera is the client location, so it is not recorded.

## From the homepage

| Control | Opens | Then |
|---|---|---|
| Login, top right | `/login`, popup `#plugin-login` | Stop. Email and password, then Google, Apple, and Facebook. Nothing typed. |
| Register Now, inside that popup | `/register`, same popup | Stop. Email, username, password, confirm password, a newsletter checkbox, and a captcha. Nothing typed. |
| Forgot Password? | `https://account.windy.com/reset` | Recorded, not opened. |
| Log in with Google, Apple, or Facebook | `https://account.windy.com/auth/google`, `/auth/apple`, `/auth/facebook` | Not clicked. |
| Sign up with Google, Apple, or Facebook | The same auth paths | Not clicked. |
| Go Premium | Not opened | Measured at rest. Checkout was not entered. |
| Menu | Menu pane `#plugin-menu`. The app writes the path as `/-Menu/menu` | Layer catalogue, plus the rows below. |
| Search field | Result list on the map | A public place name was typed. The first city row opened the detail strip. |
| Layer row (Wind, Rain, Temperature, and the rest) | Stays on the map and swaps the overlay | Wind was already selected. |
| More layers | Same menu pane | The layer catalogue. |
| Altitude | Stays on the map | No new pane on this pass. |
| My Favorites | `/-My-Favorites/favs`, pane `#plugin-favs` | Empty public pane. No account, no login wall. |
| My Alerts | `/-My-Alerts/alerts`, pane `#plugin-alerts` | Empty public pane with switches. Switches were not toggled. |
| Settings | Stays on the menu | The row has a click handler. Signed out, the pane does not change and no login wall appears. |
| Install Windy Plugin | `/plugins`, pane `#plugin-external-plugins` | Public plugin list. No plugin was loaded. |
| Route planner | `/route-planner` | URL changes. No separate pane was painted on this pass. No route was drawn. |
| Display KML, GPX, ... | `/uploader`, pane `#plugin-uploader` | Empty drop target, plus a public community list. No file was chosen. |
| Cookie consent | `#plugin-consent` | The pane says anonymous analytics are allowed and offers Ok and Change settings. Neither was clicked. |
| Weather news | `/articles` | Linked from the menu. Not opened on this pass. |
| Article card under the logo | `/articles/` plus a slug | A public article link. Not opened. |
| Help, Feedback, About us, Tutorials | `community.windy.com` or YouTube | External. Not followed. |
| Terms of Use, Privacy protection | `account.windy.com/agreements/` | External legal pages. Not opened. |
| App store badges | Apple, Google Play, Garmin | Not followed. |

The hyphenated paths above are how the app writes them (`/-My-Favorites/favs`, `/-My-Alerts/alerts`, `/-Menu/menu`). The table spells the label so a reader can find the control.

## What a login wall asks for

Login asks for an email address and a password, then a Login button, Register Now, Forgot Password?, and Log in with Google, Apple, and Facebook.

Register asks for an email address, a username, a password, a confirm password, and a newsletter checkbox. A captcha sits above Register. Sign up with Google, Apple, and Facebook sit below. The captcha was not solved. No field was filled. No provider was clicked.
