# Components

Measured on the public signed-out surfaces of X on 19 November 2026. Crops are absent: the preview browser returned "The browser is not producing screenshot frames", and headless Chromium received HTTP 403 on the login and missing routes. The legal pages are the only screenshots.

| Component | State captured | Evidence |
|---|---|---|
| Button, primary pill | Default, light fill on the dark login page. 46px tall, 9999px radius, #f8fafc fill, black 15px medium label | [raw/readings.json](raw/readings.json) login.phoneButton |
| Button, outline | Default on the missing-route shell. 40px, 1px rgba(255, 255, 255, 0.15) border, white 13px bold label | readings.json loggedOutShell.appleOutline |
| Button, Continue | Empty-field state. 48px pill, #262626 fill, #78716c label. Not pressed | readings.json login.continue |
| Button, Download PDF | Default on the legal pages. 48px, 48px radius, 2px #e8eff3 border | [screenshots/tos-light-1440.png](screenshots/tos-light-1440.png) |
| Google button | Third-party. 40px, 20px radius, white, #dadce0 border. Not an X control | readings.json login.googleButton |
| Link | Footer 11px #999999. Inline legal link #067acc. Show more #1d9bf0 | readings.json |
| Text field | Default, already focused on load. 62px, 6px radius, 2px #0ea5e9 border. Nothing typed | readings.json login.field |
| Card | QR card. #141414, 22px radius, 16px padding, shadow 0 4px 20px rgba(0,0,0,0.4) | readings.json login.qrCard |
| Icon button | About menu button is 0px at 1169px. Legal menu is 18px at 390. Not opened | readings.json about, legal measure |

## Gaps

Text area, select, checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, list row, table, avatar and badge were not on the pages that loaded. Hover, pressed, disabled-by-attribute, loading and error states were not forced. The signed-in app was not entered.
