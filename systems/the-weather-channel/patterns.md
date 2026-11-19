# Patterns

Public signed-out pages only. Screenshots are in [screenshots/](screenshots/).

## App shell

Desktop ([today-light-default.png](screenshots/today-light-default.png)): an 80px left rail with the logo, Forecasts, Radar, Allergy Tracker, Air Quality Index, More, and Sign in. The top bar holds a dark location chip and the Today / Hourly / 10-Day / Monthly tabs. The main column is the condition hero, then Today's outlook and the hourly strip. A right column holds Air Quality Index and Health & Activities.

Phone ([today-light-phone.png](screenshots/today-light-phone.png), 390 CSS pixels): the rail collapses into a menu button. The location chip and Sign in sit in the header. Tabs wrap onto a second row. The hero stacks under the title.

## Search

Opening the location chip shows a field with placeholder "Search for a location", a 2px `#3a61cc` border, and radius 24px ([search-light-open.png](screenshots/search-light-open.png)). No location was submitted.

## Sign-in

[login-light-default.png](screenshots/login-light-default.png) is the empty public form: Continue with Google, email, password, and a disabled Sign in. Nothing was typed or submitted. The form does not ask for a phone number.

## Legal

[privacy-light-default.png](screenshots/privacy-light-default.png) is trust.weather.com. It uses a system font stack and a 60px heading, separate from the Inter forecast page.

## Not captured

Empty, loading, and error states of the forecast were not reached. No destructive confirmation appeared. Filtering is the unit radios in More, which were opened and not changed. Onboarding and a signed-in home were not entered.
