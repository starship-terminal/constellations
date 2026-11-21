# The Weather Channel site tree

Mapped from the public site on 2026-11-21, before screenshots. Playwright drove headed Chrome (the headless client was stopped by an interstitial titled Challenge Validation). No email was typed. No password was submitted. No form was submitted. Location search was opened and not filled.

Place names, street addresses, and article headlines are omitted. A path that embeds a place id is written as `/l/[place-id]`.

## How the root behaves

`https://weather.com/` redirects to a geolocated local forecast. That page shows a place name and can show a street-level label ("Improve location precision"). It is mapped and not screenshotted.

The same root, when the interstitial does not clear, stays on `https://weather.com/` with the title Challenge Validation. That load is a boundary, not a page.

The US editorial chrome (news, science, safety, health) is the public surface that does not require a place. The older maps and legal chrome is a second public surface.

## Desktop header (editorial chrome)

Seen on `/news`, `/science`, `/safety`, and `/news/health-and-wellness`.

| Control | Opens |
|---|---|
| Logo | `https://weather.com/` (geolocated forecast; not screenshotted) |
| Search for a location (dialog) | Location search dialog. Placeholder: "Search for a location". Not typed. Not screenshotted, because results would be a place. |
| Settings (dialog) | Units dialog: Imperial, Metric, Hybrid, plus a language row. No account fields. |
| Sign in | `https://weather.com/login`. Login wall. Branch stops. |
| Today | `https://weather.com/redir` (place forecast; not screenshotted) |
| Hourly | `https://weather.com/weather/hourbyhour/l/` (place forecast; not screenshotted) |
| 10 Day, Monthly, Allergies, Air Quality, Cold & Flu, Radar | Place forecast routes of the same shape. Mapped, not screenshotted. |
| Top Stories | `https://weather.com/news` |
| Severe Weather | `https://weather.com/news/severe-weather` |
| Health & Wellness | `https://weather.com/news/health-and-wellness` |
| Thanksgiving | `https://weather.com/news/thanksgiving` |
| El Niño | `https://weather.com/news/el-nino` |
| Winter Outlook | `https://weather.com/news/winter` |
| Hurricanes | `https://weather.com/news/hurricane` |
| Tornadoes | `https://weather.com/news/tornadoes` |
| Wildfires | `https://weather.com/news/wildfires` |
| Home & Garden | `https://weather.com/news/home-garden` |
| Story cards | Dated article and video URLs under `/news`, `/forecast`, `/safety`. Public editorial pages. One article is captured as a specimen; the rest are the same template. |

There is no hamburger on this desktop header. The phone header has a Menu button (see Phone).

## Desktop header (maps and legal chrome)

Seen on `/maps`, `/login`, `/privacy-settings`, `/data-rights`, `/accessibility-statement`.

| Control | Opens |
|---|---|
| Home | `https://weather.com/` |
| Today, Hourly, 10 Day, Monthly, Radar | `https://weather.com/weather/{today,hourbyhour,tenday,monthly,radar}/l/[place-id]`. Place pages. Not screenshotted. |
| Video | A current video article (same template as news videos) |
| Explore | `https://weather.com/explore` |
| Severe Weather (menu) | Section menu, not a page |
| Health & Wellness (menu) | Section menu |
| Lifestyle (menu) | Section menu |
| Tornado Central | `https://weather.com/storms/tornado-central` |
| Safety & Prep | `https://weather.com/safety/index` |
| Allergy Tracker, Air Quality Index, Cold & Flu Tracker | `https://weather.com/forecast/{allergy,air-quality,cold-flu}/l/[place-id]`. Place pages. Not screenshotted. |
| Skin | `https://weather.com/health/skin-health` |
| Home & Garden | `https://weather.com/home-garden` |
| Pets & Animals | `https://weather.com/pets` |
| Recipes | `https://weather.com/home-garden/recipes` |
| Space & Skywatching | `https://weather.com/science/space` |
| Travel & Outdoors | `https://weather.com/travel` |
| Product Reviews & Deals | `https://weather.com/atmosphere` |
| Shop | `https://shop.weather.com/` (external shop) |
| Search City or Zip Code | A text field on the page. Not typed. Not submitted. |

## Pages visited

| Request | Landed | What it is | Screenshot |
|---|---|---|---|
| `https://weather.com/` | Geolocated `/today`, or Challenge Validation if the interstitial does not clear | Local forecast, or a bot wall | No |
| `https://weather.com/news` | `/news` | Top stories | Yes |
| `https://weather.com/maps` | `/maps/currentusweather` | US current weather map | Yes |
| `https://weather.com/science` | `/science` | Science index | Yes |
| `https://weather.com/safety` | `/safety` | Safety index | Yes |
| `https://weather.com/health` | `/news/health-and-wellness` | Health index | Yes |
| `https://weather.com/video` | `/news` | Redirects to news | Recorded as the news page |
| `https://weather.com/severe-weather` | `/severe-weather` | Severe weather index | Yes |
| `https://weather.com/storm-radar` | `/storm-radar` | Product promo, Sign In only | Yes |
| `https://weather.com/login` | `/login` | Email and password. No Google button. No Apple button. | Fields recorded. Page not screenshotted (password field). Branch stops. |
| `https://weather.com/signup` | Linked from login | Account creation | Not opened |
| `https://weather.com/forgot-password` | Linked from login | Recovery | Not opened |
| `https://weather.com/privacy-settings` | `/privacy-settings` | Privacy settings. Search field present, not typed. | Yes, if the page has no street address |
| `https://weather.com/data-rights` | `/data-rights` | Data rights, plus View Data Inventory | Yes |
| `https://weather.com/accessibility-statement` | `/accessibility-statement` | Accessibility statement | Yes |
| `https://weather.com/sitemap` | `/sitemap` | Date index: Today, Yesterday, This Week, Last Week, years | Yes |
| `https://weather.com/subscribe` | `/not-available` on an earlier probe | Unavailable | Not a product surface |

Footer links on the editorial pages, not walked as product screens: Trust Center and policies on `trust.weather.com`, Data Vendors, Feedback (`support.weather.com`), News Room and Weather Data APIs on `weathercompany.com`, Weather Underground.

## Login wall

`https://weather.com/login` shows a text field and a password field, plus Sign in, Sign up, and Forgot password. The known probe matches: email and password are present, the password was not submitted, and there is no Google button. This capture also found no Apple button. The branch stops at that URL.

## Location search

The editorial header button "Search for a location" opens a dialog with placeholder "Search for a location". The maps chrome has a "Search City or Zip Code" field. Neither was typed into. Forecast pages that show a street address are mapped and not screenshotted.

## Phone (390 x 844)

`https://weather.com/news` at phone width shows Menu, Search for a location, Sign in, and Dismiss. Menu is the phone equivalent of the desktop section nav. Sign in goes to `/login` and that branch stops. Search is the same location dialog and is not typed into.

## Theme

No theme switch was found on the public pages. Settings changes units and language, not light and dark. One theme is recorded.
