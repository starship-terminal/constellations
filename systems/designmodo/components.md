# Components

Public signed-out Designmodo, measured 2026-11-21. Crops were not cut: the component evidence is the full-page shot named in each row, plus the computed style in [raw/components-computed.json](raw/components-computed.json).

| Component | States captured | Where | Not captured |
|---|---|---|---|
| Button, Sign Up | default | [home-light-default.png](screenshots/home-light-default.png). Fill #f49a40, label #ffffff, radius 999px, height 38.5px, padding 8px 18px, InterVariable 15/600. | hover, pressed, focus ring, disabled, loading |
| Button, Open App | default, hover | Same shot. Fill #27ae60, hover #1e8449, radius 999px, height 53px, padding 13px 28px, shadow 0 4px 9px rgba(39,174,96,0.15). | pressed, focus, disabled |
| Button, Login | default | [sign-in-light-default.png](screenshots/sign-in-light-default.png). Fill #2f80ed, radius 5px, height 38.5px. | hover, pressed. Not clicked. |
| Link, Log In | default | Header on the home shot. InterVariable 15/500, white on the dark hero. | hover |
| Text field | default, empty | Sign-in email and password. Height 50px, radius 5px, border 1px #e0e5eb, padding 14px 18px. Not filled. | focus, error, filled |
| Checkbox | default | Remember me (checked in the markup) and the privacy checkbox (unchecked). Values not read. | hover, focus |
| Menu | Apps, Articles, account, cart | [home-light-apps-menu.png](screenshots/home-light-apps-menu.png), [home-light-articles-menu.png](screenshots/home-light-articles-menu.png), [home-light-account-menu.png](screenshots/home-light-account-menu.png), [home-light-cart.png](screenshots/home-light-cart.png) | item hover |
| Dialog | Welcome back | [postcards-gallery-light-welcome.png](screenshots/postcards-gallery-light-welcome.png). Close was clicked. The dialog remained. | submitted login |
| Card | product card on home | Home shot, Postcards card. Radius not read on that node. | hover |
| Badge | Black Friday banner | Home shot. Colours not tokenised. | |

## Not present on the captured surface

Text area was on the contact form, which was not kept (it prints a street address). Select, radio, switch, tabs (the home product switch is present; its selected style was not measured), tooltip, toast, table, avatar, list row.

## Gaps

Focus-visible on Sign Up did not paint a ring. Pressed, disabled, loading and error states need a submit or an account, which this capture does not do. The phone menu open did not settle. See [site-tree.md](site-tree.md).
