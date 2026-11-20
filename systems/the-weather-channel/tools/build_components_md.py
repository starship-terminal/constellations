#!/usr/bin/env python3
"""Write components.md from the measured public states."""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
text = """# Components

Public chrome of The Weather Channel, measured on 2026-11-21 from weather.com. Signed out. One theme.

| Component | States | Where |
|---|---|---|
| Button | default, hover, focus-visible | Settings and Sign in in the news header. Maps chrome paints Sign in as a filled ink button. |
| Icon button | default | Phone Menu. Location search opener. |
| Link | default | Trend links, footer links, Privacy Policy link. |
| Text field | default, empty | "Search City or Zip Code" on the maps chrome. Location dialog field was opened and not typed. |
| Text area | not present | No public text area. |
| Select | not present | Units are chips, not a select. |
| Checkbox | not present | |
| Radio | not present | |
| Switch | not present | |
| Tabs | default, selected | Maps page tabs: Weather Details, US Satellite & Radar, World Satellites, Severe, Health. Phone bottom bar: Forecast, News, My Plans, Radar. |
| Menu | opened | Maps header menus (Severe Weather, Health & Wellness, Lifestyle). Settings dialog. |
| Tooltip | not captured | None held still. |
| Dialog | opened | Settings units dialog. Location search dialog was opened and not screenshotted. |
| Toast | not present | Sonner toast tokens are declared. No toast was shown. |
| Card | default | Story cards on news, science, and safety. |
| List row | default | Sidebar forecast links. |
| Table | not present | |
| Avatar | default | Privacy Settings person mark. |
| Badge | not present | Read-time labels are text, not badges. |

## Shared values

Page background is white. Text and the filled Sign in button are `#252422`. The selected sidebar item is `#3a61cc` with white text, 10px radius, 32px tall. Header controls are 40px pills. The Settings dialog is white, 16px radius, with a `rgba(37, 36, 34, 0.2)` shadow. Focus on Settings is a 2px `#3a61cc` ring.

## Gaps

- Login, signup, and forgot-password were not captured. `https://weather.com/login` shows an email field and a password field. The password was not submitted. There is no Google button and no Apple button.
- Location search was not typed into. Forecast pages that show a street address were not screenshotted.
- The root URL redirects to a geolocated forecast. That page was mapped and not screenshotted.
- Dark theme: not present on the public pages. Settings changes units and language.
- Hover and pressed colours beyond the Settings hover wash (`oklab` 7% black) were not given a hex. Pressed is Not captured.
- Disabled, loading, and error states of controls were not shown.
- Checkbox, radio, switch, text area, select, table, toast, and tooltip were not present or not reached.
- Declared dark semantic variables (`--background`, `--foreground`, status hsl pairs) are in the stylesheet and not painted on these light pages. They are not in the light token set.
"""
(HERE / "components.md").write_text(text)
print("wrote components.md")
