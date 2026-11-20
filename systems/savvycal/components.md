# SavvyCal components

Measured on the public site on 2026-11-21, signed out. Values are computed styles. Crops are the element screenshots taken with those readings.

25 components, 68 crops.

## Inventory

| Component | Group | Page | States |
|---|---|---|---|
| Nav link | link | home | default, hover, focus-visible, pressed |
| Log in | link | home | default, hover, focus-visible, pressed |
| Sign up | button | home | default, hover, focus-visible, pressed |
| Hero CTA | button | home | default, hover, focus-visible, pressed |
| Secondary CTA | link | home | default, hover, focus-visible, pressed |
| Logo | link | home | default |
| FAQ summary | accordion | home | default, hover, focus-visible, pressed |
| FAQ open | accordion | home | default |
| Footer link | link | home | default, hover, focus-visible, pressed |
| Display heading | type | home | default |
| Annual billing | tabs | pricing | default, hover, focus-visible, pressed |
| Monthly billing | tabs | pricing | default, hover, focus-visible, pressed |
| Monthly selected | tabs | pricing | default |
| Plan CTA | button | pricing | default, hover, focus-visible, pressed |
| Search field | text field | integrations | default, focused |
| Filter pill | tabs | integrations | default, hover, focus-visible, pressed |
| Filter pill selected | tabs | integrations | default |
| Email field | text field | login | default, focused |
| Password field | text field | login | default, focused |
| Sign in submit | button | login | default, hover, focus-visible, pressed |
| Google sign-in | button | login | default, hover, focus-visible |
| Next month (missing) | icon button | demo | missing |
| Day cell | button | demo | default |
| Open menu | icon button | mobile-home | default, hover, focus-visible, pressed |
| Menu link | link | mobile-home | default |

## Shared values

Marketing pages paint oatmeal `#fcf7ed` as the page, sand `#f4ebda` as a raised band, orange `#f54320` as the accent, neon green `#b9ff78` on the login submit, and olive ink `#0c0c09` for text. Controls are pills (`border-radius` computed as a huge pixel value, tokenised as `9999px`). UI type is Inter Variable. Display type is GT Alpina Condensed.

## Gaps

- Text area, select, checkbox (beyond the login Remember me control, which was not measured), radio, switch, tooltip, dialog, toast, table, avatar, and badge are not present on the public marketing pages, or were not reached.
- The login Remember me control is a checkbox. It was visible. It was not measured. Not captured.
- Disabled, loading, and error states were not shown on the public pages. Not captured.
- Pressed colour did not differ from default under a CDP active state. Not captured as a distinct colour.
- Dark theme utilities exist in the login CSS. No control switched them. Not captured.
- Signed-in app screens sit behind https://savvycal.com/login. Not captured.

