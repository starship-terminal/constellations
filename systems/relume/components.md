# Relume components

Public marketing surface of relume.ai, captured 2026-11-21, signed out. Component values that were read are in [tokens.json](tokens.json). States that were only seen, not measured, are Observed.

| Component | Present | States seen | Where |
|---|---|---|---|
| Button | yes | default (Start for free, measured) | [home-light-default.png](screenshots/home-light-default.png) |
| Icon button | yes | theme toggle, Open menu | theme button on the shell; phone menu in mobile-home shots |
| Link | yes | nav and footer links | home and footer |
| Text field | yes, on walls and forms | login email and password visible; not typed | [login-light-default.png](screenshots/login-light-default.png) |
| Text area | yes, homepage composer | empty. Not typed. | home hero |
| Select | not present as a native select | page-views control on pricing is a custom menu, not opened | pricing |
| Checkbox | yes | cookie preference and form checkboxes, not changed | contact and cookie dialog, not submitted |
| Radio | not present | | |
| Switch | yes | theme toggle, yearly billing control | shell; pricing |
| Tabs | yes | Publish pricing / Export pricing; Recent / Highlights | pricing-light-export-tab, showcase-light-highlights |
| Menu | yes | Products dropdown, library Preferences, phone overlay | home-light-products-menu, components-light-preferences, mobile-home-light-menu |
| Tooltip | not captured | none held open | |
| Dialog | yes | cookie banner (hidden, not accepted); login is a page, not a dialog | site-tree.md |
| Toast | not present on the public pages visited | | |
| Card | yes | product cards, library cards, plan cards | home, components, pricing |
| List row | yes | footer columns, docs sidebar | docs |
| Table | not present | | |
| Avatar | yes | showcase author menus, community credits (published names) | showcase |
| Badge | yes | BETA on Studio, NEW on product links | products menu |

## Gaps

- Hover, focus-visible, pressed, disabled, loading and error were not measured per control. Not captured.
- The signed-in builder, projects, billing and account settings are behind [https://www.relume.ai/app/login](https://www.relume.ai/app/login). Password was not submitted.
- Signup at `/app/signup` asks for an email. Not typed.
- Contact sales, affiliates and newsletter fields were not filled and not submitted.
- Cookie Accept, Reject and Save were not clicked. The banner was hidden.
- Google and SSO were not clicked.
- Motion durations and easings were not read. Not captured.
- Icon sizes and focus-ring width were not read. Not captured.
