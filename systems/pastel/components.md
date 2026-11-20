# Pastel components

Public surface only, measured 2026-11-20. The annotation canvas is behind [login](screenshots/login-light-default.png) and was not entered.

| Component | States captured | Where |
|---|---|---|
| Button, primary | default. Hover computed the same fill. | [button-primary-default](components/crops/button-primary-default.png), home |
| Button, signup | default | [button-signup-default](components/crops/button-signup-default.png) |
| Button, login | default | [button-login-default](components/crops/button-login-default.png) |
| Button, ghost | default | [button-secondary-default](components/crops/button-secondary-default.png) |
| Link | default in the header and announcement bar | [home-light-default](screenshots/home-light-default.png) |
| Menu | phone nav open | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [mobile-blog-light-menu](screenshots/mobile-blog-light-menu.png) |
| Tabs | Monthly and Annual on pricing | [plans-light-default](screenshots/plans-light-default.png), [plans-light-annual](screenshots/plans-light-annual.png) |
| Accordion | one FAQ question opened | [faq-light-open](screenshots/faq-light-open.png) |
| Card | plan cards, demo card | [pricing-cards-default](components/crops/pricing-cards-default.png), [card-demo-default](components/crops/card-demo-default.png) |
| Text field | visible on the login wall, not filled | [login-light-default](screenshots/login-light-default.png) |

## Shared values

Primary button: background `#165dfb`, text `#ffffff`, radius `10px`, height `46px`, Figtree 16/24 weight 500. Signup button: background `#454745`, radius `10px`, height 42px. Login button: 1px border `rgba(152, 152, 152, 0.45)`, radius `10px`. Plan card: background `#f5f5f4`, 1px border `rgba(80, 80, 80, 0.3)`, width 280px, no shadow.

## Gaps

Text area, select, checkbox, radio, switch, tooltip, dialog, toast, table, avatar, and badge were not present as product controls on the public pages. The login wall shows email and password fields and a Google button. Those were not focused, filled, or submitted, so their computed styles are Not captured. Disabled, loading, and error states were not shown. Pressed was not forced. Focus-visible landed on the announcement bar (outline `rgb(0, 95, 204) auto 1px`), not on the primary button. The status uptime graph did not open: the control's click timed out. Intercom was hidden, not opened.
