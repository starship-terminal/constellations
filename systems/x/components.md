# Components

Measured on the public signed-out surfaces of X. Values are from 19 November 2026, checked again on 21 November 2026. Crops are absent. The pages themselves are in [screenshots/](screenshots/).

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
| Dialog | Login and signup walls. 700 by 664, #141414, 24px radius. Photographed empty. Not submitted | [screenshots/login-dark-1440.png](screenshots/login-dark-1440.png) |
| Chip | News category chip. Selected chip is white on black, 32px, 9999px radius | [screenshots/news-dark-1440.png](screenshots/news-dark-1440.png) |

## Gaps

Text area, select, checkbox, radio, switch, tabs, menu, tooltip, toast, list row, table, avatar and badge were not measured as components. Hover, pressed, loading and error states were not forced. The signed-in app was not entered. login-extracted stays not-started.
