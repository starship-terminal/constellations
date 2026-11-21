# Trip.com components

Public surface only, signed out, 2026-11-21. Values are token names from [tokens.json](tokens.json). Crops were not cut: the page screenshots are the evidence.

| Component | Where | States |
|---|---|---|
| Button, primary | Search on the hotel and flight cards | Default captured. Hover, focus-visible, pressed: Not captured. |
| Button, secondary | Sign in/register, Claim all, Flight + Hotel | Default captured in [home-light-default](screenshots/home-light-default.png) and [flights-light-default](screenshots/flights-light-default.png). |
| Button, disabled | Declared as `--compButtonDisabled*` | Not painted on the public pages captured. |
| Link | Header, left rail, footer | Default captured. |
| Text field | Where to?, Leaving from, Going to, header search | Default captured. Not typed into. Not submitted. |
| Radio | Flights Return / One-way / Multi-city; trains Single / Return | Default captured on [flights-light-default](screenshots/flights-light-default.png). |
| Checkbox | Flights Direct | Default captured. |
| Tabs | Search-card product tabs; support service-chat tabs; trains / coaches | Selected captured (Hotels & Homes underline; Flights tab selected on the flights page; support Flights chip). |
| Dialog | Language/currency; sign-in/register | Captured in [home-light-currency](screenshots/home-light-currency.png) and [home-light-signin](screenshots/home-light-signin.png). Not submitted. |
| Menu | Phone travel menu | Captured in [mobile-menu-light-menu](screenshots/mobile-menu-light-menu.png). |
| Card | New-user coupon cards, hotel promo banner | Default captured. |
| Badge | "New" on AI Lab, "1 night" pill | Default captured. |
| Text area, select, switch, tooltip, toast, table, avatar | | Not present on the public pages captured, or not reached. |

## Gaps

- Hover, focus-visible, and pressed states were not measured per control.
- No component crops. Layout evidence is the page screenshots.
- Sign-in dialog is a wall. Google, Apple, and Facebook were not clicked. No email was typed.
- Find bookings (`/passport/ordersearch/`) is an auth wall. Stopped.
- Train search fields arrived prefilled with station names. That screenshot was deleted so no location string is in the package. Trains page: Not captured.
