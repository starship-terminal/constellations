# Pixso components

Public site only, captured 2026-11-21 from https://pixso.net/. The signed-in editor (`/app/`, `/editor/`) was not opened. Crops were not cut: component evidence is the full screenshots plus computed styles named below.

| Component | States seen | Evidence |
|---|---|---|
| Button (Get started) | default, hover | [screenshots/home-light-default.png](screenshots/home-light-default.png), [screenshots/home-light-cta-hover.png](screenshots/home-light-cta-hover.png). Fill `core.color.button` #202125, text white, radius 7px, height 34px. |
| Link (Pricing, Log in) | default | Header link ink `#1e2330`, Log in `#3d3d3d`, Figtree 14/500. |
| Text field | default, focus | Contact name field: fill `#f7f7f9`, radius 6px, height 40px. Login email, resting: 1px `rgba(0,0,0,.1)` border, radius 8px. Focus: 2px `rgb(31, 97, 255)`. Not filled. Not submitted. |
| Menu | open | Product, AI design, Resources & learning, Enterprise. [screenshots/home-light-product-menu.png](screenshots/home-light-product-menu.png) and the sibling menu shots. |
| Card | default | Community resource cards and plugin cards on `/community/home` and `/plugins/`. |
| Dialog | not present | No public dialog opened. Contact is a page, not a dialog. |
| Tabs | observed | Help center section links and community classify links. Values not read per tab. |

## Gaps

- Icon button, text area, select, checkbox, radio, switch, tooltip, toast, table, avatar, badge: not captured. Not present on the public pages that were opened, or present only inside the signed-in editor.
- Pressed, disabled, loading, error, selected: Not captured. No public control was held in those states, and no form was submitted.
- Dark theme: not present.
- Signed-in editor components: Not captured. Login wall at `/user/login/`.
