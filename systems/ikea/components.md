# IKEA components

Public Singapore storefront, signed out, 2026-11-21. Crops that match a real control are in [components/crops/](components/crops): nav link, search field, header icon, login link, category card, Add to cart. A product-card selector landed on a 32px overlay and was deleted. Filter and sort buttons were not found by the selector used.

| Component | States seen | Where |
|---|---|---|
| Button, primary | default | Login wall, cookie sheet (sheet not clicked). Black pill, white label. |
| Button, secondary | default | Create account on the login wall. White pill, black stroke. |
| Icon button | default | Header cart, list, account, phone menu. |
| Link | default | Nav entry points, footer, underlined promo links. |
| Text field | default, focused | Search on the homepage. Email and password on the login wall. Not typed. |
| Text area | not present | No public text area on the captured pages. |
| Select | not captured | Sort and filter controls exist on the product list. States were not measured in this run. |
| Checkbox | not present | Not on the captured public pages. |
| Radio | not present | Not on the captured public pages. |
| Switch | not present | Not on the captured public pages. |
| Tabs | Observed | Products menu category chips. |
| Menu | opened | Products mega menu, phone menu drawer. |
| Tooltip | not present | Not seen. |
| Dialog | opened | Select store, country sheet. Closed without a choice. |
| Toast | not present | Not seen. |
| Card | default, hover, focus-visible | Category tile crop in [components/crops/](components/crops). Product photography cards are in the page screenshots. |
| List row | default | Phone menu rows, store list inside the store dialog. |
| Table | not present | Not on the captured pages. |
| Avatar | not present | Signed-out header uses an icon, not an avatar. |
| Badge | Observed | New and price labels on product cards in the homepage body. Colours are the commercial-message tokens. |

## Gaps

- Hover, focus-visible, pressed, disabled, loading and error were not measured as crops in this package. The colour tokens for hover and pressed exist as `--colour-interactive-*-bg-hover` and `-pressed`.
- Login and signup stop at `https://www.ikea.com/sg/en/profile/login/`. No field was filled.
- Cookie buttons were not clicked.
- Dark theme is not present on the public site.
