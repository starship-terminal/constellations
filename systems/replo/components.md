# Replo components

Public marketing surface of www.replo.app, captured 2026-11-21, signed out. One dark theme. Values are token names from [tokens.json](tokens.json). Crops were not cut for this pass: the states below were read from computed styles on the live home page ([raw/live.json](raw/live.json)) and from the full-page screenshots.

## Shell

| Component | States | Values |
|---|---|---|
| Header | default | Height `dark.component.header.height` (60px). Transparent fill. Text `dark.text`. |
| Nav button (Product, Solutions, Resources) | default, opened | 14px, height 36px, padding 8px 12px. Opens a menu in place. Hover, focus-visible, pressed: not captured. |
| Nav link (Customers, Pricing, Log in) | default | Transparent fill, text `dark.text`, 14px. Log in goes to the dashboard auth wall. |
| Primary button (Start for free) | default | Fill `dark.accent`, text `dark.accent-text`, height 36px, radius `core.radius.pill`, padding 0 16px. Opens signup. Not submitted. |
| Secondary button (Book a demo) | default | Fill `dark.page`, text `dark.text`, 1px border `dark.border`, radius pill. Opens /contact. |
| Footer | default | Repeats product, resource, and legal links on `dark.page`. |
| Mobile menu button | default, opened | `aria-label="Open menu"`. Opens the same menus as a drawer. See [mobile-home-dark-menu](screenshots/mobile-home-dark-menu.png). |

## Content

| Component | States | Values |
|---|---|---|
| Display heading | default | 56px / 59.36px, weight 500, family Archivo, color `dark.text`. |
| Body | default | 16px / 24px, weight 400, color `dark.text`. |
| Accordion | default, opened | Homepage groups expand in place. "Copy any website on the internet" was opened. See [home-dark-accordion](screenshots/home-dark-accordion.png). |
| Card | default | Surface `dark.surface` (`#0b0b0b`) and raised `dark.raised` (`#161616`) appear in the stylesheet and on section panels. |
| Link | default | In-page links use `dark.text`. No separate link colour was measured. |

## Gaps

- Hover, focus-visible, and pressed were not measured for each control. The primary and secondary buttons were read at rest only.
- Text field, text area, select, checkbox, radio, switch, tooltip, dialog, toast, table, avatar, and badge were not present as form controls on the marketing pages that were measured. The contact page may hold a form; it was not submitted and its fields were not measured as components.
- Disabled, loading, and error states were not present on the captured controls.
- The dashboard login wall shows email and password fields. That branch stopped. Those fields are not in this inventory.
- Icons were not extracted. The site icon is [icon.png](icon.png).
