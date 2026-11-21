# Make components

Public marketing site only, captured 2026-11-21 from https://www.make.com/. The signed-in product was not entered. Crops were not cut: the states below are the full screenshots that show them.

| Component | States seen | Where |
|---|---|---|
| Button, primary | default, hover (computed) | [home-light-default.png](screenshots/home-light-default.png). Hover background rgb(128, 59, 191) measured on Try it free. Pressed not captured. |
| Button, secondary | default | Talk to sales and Sign in on the same shot. |
| Icon button | default | Announcement close, phone menu, phone drawer close. [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png) |
| Link | default | Nav links, footer links, Forgot password on the login wall. |
| Text field | default, filled | Integrations search filled with "slack". [integrations-light-search.png](screenshots/integrations-light-search.png). Login email and password empty on the wall. |
| Text area | not present | No public textarea outside the signup captcha field, which was not interacted with. |
| Select | not present | Category is a button that opens a filter, not a native select. |
| Checkbox | not captured | Category checkboxes exist on the integrations filter. The cookie-consent checkboxes were not clicked. |
| Radio | not present | Not on the captured pages. |
| Switch | default | Verified Apps and Community Apps toggles on the integrations page. On and off were not both captured as separate states. |
| Tabs | default | Pricing Monthly billing / Annual billing. The annual click did not change the visible prices in the shot. Maia feature tabs were clicked; the viewport did not show a panel change. |
| Menu | open | Product mega menu. [home-light-product-menu.png](screenshots/home-light-product-menu.png). Phone drawer. [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png) |
| Tooltip | not present | Not opened. |
| Dialog | not captured | OneTrust preference center exists and was not opened. No product dialog was opened. |
| Toast | not present | Not on the public pages. |
| Card | default | Plan cards, integration result card, menu tiles. |
| List row | default | Phone nav rows, FAQ rows. |
| Table | not present | Not on the captured pages. |
| Avatar | not present | Not on the public marketing pages. |
| Badge | default | Save 15%, Popular, NEW on the product menu. |

## Gaps

- Signed-in app (scenario editor, org, grid) is behind https://www.make.com/login. That branch stopped.
- Signup is behind https://www.make.com/register and includes Google, Apple, GitHub, Facebook and a captcha. That branch stopped.
- Focus ring: the first Tab landed on the header host with outline none. Focus-visible is Not captured.
- Pressed, disabled, loading and error states of buttons and fields were not shown. No form was submitted, so validation errors are Not captured.
- Disabled text colour is Not captured.
- Overlay scrim colour is Not captured as a token. The product menu dims the page; the value was not read.
- Dark theme is not present. The FAQ and 404 use a dark section colour, not a theme toggle.
