# Components

Public controls measured on scale.com on 2026-11-21 at 1440×900, plus the states visible in screenshots. Values are token names where a token exists. A state that was not reached is Not captured.

Crops live in [components/crops/](components/crops/).

| Component | States | Evidence |
|---|---|---|
| Button (primary) | default, hover, focus-visible | [button-primary-default.png](components/crops/button-primary-default.png). Fill `light.component.button.primary.bg` #000000, text #ffffff, height 40px, radius 8px, 16px Aeonik. Hover and focus-visible did not change fill or text in the computed reading. |
| Button (secondary, Log In) | default, hover | [button-secondary-default.png](components/crops/button-secondary-default.png). Transparent fill, text `light.nav.loginText` #929292, radius 8px, 14px. Hover did not change the computed colour. |
| Link | default | Header and footer links. Colour follows `light.text` on marketing pages. Docs links use a blue that matches `:root --primary` 0 108 255. A separate link token on marketing was not measured. |
| Text field | default, focus | [text-field-default.png](components/crops/text-field-default.png), [text-field-focus.png](components/crops/text-field-focus.png). White fill, #171717 text, 14px, radius 8px. The demo form was not submitted. |
| Text area | default | Observed on /off-the-shelf-data ("Tell us what you are looking for"). Not measured separately. |
| Select | default | [select-default.png](components/crops/select-default.png). Same field recipe as the text field. The menu was not opened. |
| Checkbox | not present | Not on the public marketing pages captured. The login wall has no product checkbox. |
| Radio | not present | Not on the captured public pages. |
| Switch | not present | Not on the captured public pages. |
| Tabs | selected | Automotive modality tabs, Donovan product tabs, healthcare tabs, docs theme menu. [automotive-light-image-tab.png](screenshots/automotive-light-image-tab.png), [donovan-light-agentic-rag.png](screenshots/donovan-light-agentic-rag.png). |
| Menu | open | Products, Solutions, Research, Resources mega-menus. [home-light-products-menu.png](screenshots/home-light-products-menu.png). Phone drawer: [mobile-home-light-menu-open.png](screenshots/mobile-home-light-menu-open.png). Docs theme menu: [docs-light-theme-menu.png](screenshots/docs-light-theme-menu.png). |
| Tooltip | not captured | None stayed open long enough to measure. |
| Dialog | open | Blog search dialog. [blog-light-search-open.png](screenshots/blog-light-search-open.png). OneTrust cookie dialog was hidden and not captured as a product dialog. |
| Toast | not present | No toast appeared. Forms were not submitted, so success and error toasts were not reached. |
| Card | default | Docs cards and pricing-style panels on product pages. [docs-light-default.png](screenshots/docs-light-default.png). |
| List row | default | Blog search results and blog index rows. |
| Table | not present | No data table on the public marketing pages. |
| Avatar | not present | Staff portraits appear in photography, not as an avatar component. |
| Badge | observed | Blog category chips (Healthcare, Policy). Not measured. |

## Shared values

Page #ffffff, text #000000, primary action #000000 on #ffffff, control radius 8px, control height 40px, body 16/24 Aeonik. Header height 88px at 1440.

## Gaps

- Pressed, disabled, loading, and error states: Not captured. Submitting a form or holding a press that navigates was out of scope.
- Hover on the primary button did not change computed fill or text. A motion-only hover, if any, was not isolated.
- Login wall controls (Google, GitHub, email, password) were photographed and not measured, because that branch stops at the wall.
- Signed-in dashboard components: Not captured. https://dashboard.scale.com/login is the wall.
