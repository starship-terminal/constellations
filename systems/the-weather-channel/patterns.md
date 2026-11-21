# Patterns

Public pages only. The control map is [site-tree.md](site-tree.md).

## App shell

The editorial pages (`/news`, `/science`, `/safety`, `/news/health-and-wellness`) use a white header, a left sidebar of forecast links, and a story grid. The selected section is a blue pill. Phone width replaces the sidebar with a Menu button and a bottom bar (Forecast, News, My Plans, Radar).

[screenshots/news-light-default.png](screenshots/news-light-default.png) shows the desktop shell. [screenshots/mobile-news-light-default.png](screenshots/mobile-news-light-default.png) shows the phone shell. The location control in both is painted over so a place name is not stored.

## Maps shell

`/maps` lands on `/maps/currentusweather`. A left rail lists Home, Today, Hourly, 10 Day, Monthly, Radar, Video, and Explore. Section menus sit below it. The main column is a map with tabs. Sign in is a filled black button. Search is an empty field.

[screenshots/maps-light-default.png](screenshots/maps-light-default.png)

## Settings

Settings opens a units dialog (Imperial, Metric, Hybrid) and a language row. It does not open an account form.

[screenshots/news-light-settings.png](screenshots/news-light-settings.png)

## Search

Location search opens a dialog. The maps chrome has "Search City or Zip Code" on the page. Neither was typed into. Forecast results that would show a street address were not captured.

## Empty, loading, error

Ad slots on the maps page render as empty gray rectangles. The sitemap is a short date index. No product error state was reached. The bot interstitial (title Challenge Validation) blocked `https://weather.com/` in headed Chrome and is recorded as a boundary in [site-tree.md](site-tree.md).

## Login wall

Sign in goes to `https://weather.com/login`. That branch stops. The page was not screenshotted because it shows a password field.

## Destructive confirmation, feedback, onboarding

Not present on the public pages that were reached.
