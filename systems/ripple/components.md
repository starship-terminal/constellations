# Components

Public controls on ripple.com, measured 2026-11-21 at 1440×900 unless noted. Crops are 256-colour. Values are the computed styles in [raw/components-computed.json](raw/components-computed.json).

| Component | States | Crop | Values |
|---|---|---|---|
| Logo | default | [logo-default.png](components/crops/logo-default.png) | 93×24 link in an 80px white header |
| Nav trigger | default | visible in [home-light-default.png](screenshots/home-light-default.png) | 16px / 24px, weight 400, rippleBdsFont, color #000, radius 6px, height 36px |
| Nav CTA (Contact Sales) | default | [nav-cta-default.png](components/crops/nav-cta-default.png) | 40px pill, radius 9999px, padding 6px 18px, gradient border using primary-600 / primary-300 / primary-500 |
| Primary button | default, hover, focus | [hero-cta-default.png](components/crops/hero-cta-default.png) | 40px, radius 40px, text #f1f2f3, radial-gradient(#005bcc, #008cff 80%). Hover fill becomes #0067e5. Focus outline rgb(0, 95, 204) auto 1px |
| Icon button | default, focus | in the header crop | 40×40, radius 9999px, fill #f2f2f3. Focus ring is white 1px plus #006aff 3px |
| Search field | default, focused | [search-dialog-default.png](components/crops/search-dialog-default.png) | height 40px, radius 4px, fill #e4e5e7, text #586074, focus ring white 1px plus #006aff 3px |
| Menu | open | [menu-default.png](components/crops/menu-default.png) | full-width white panel, shadow 0 10px 20px rgba(0,0,0,0.05) |
| Language menu | open | [language-menu-default.png](components/crops/language-menu-default.png) | English and Português |
| FAQ item | open | [faq-item-open.png](components/crops/faq-item-open.png) | gray answer card with a close control |
| Contact cards | default | [contact-cards-default.png](components/crops/contact-cards-default.png) | four routing cards, no fields |
| Footer | default | in full-page shots | background #141a1f, text #fafafa, link hover #939a9f |
| Phone header | default | [m-header-default.png](components/crops/m-header-default.png) | 390 viewport |
| Phone menu | open | [m-menu-open.png](components/crops/m-menu-open.png) | six rows with chevrons |

## Gaps

| Checklist item | Status |
|---|---|
| Button | Captured (primary and Contact Sales) |
| Icon button | Captured (search, language) |
| Link | Captured (nav, footer, contact cards) |
| Text field | Captured empty (search). Sales and download forms were not filled |
| Text area | Not present on the captured pages |
| Select | Not captured. No public select was opened |
| Checkbox, radio, switch | Present only inside the cookie banner, which was hidden and not clicked |
| Tabs | Not present on the captured pages |
| Menu | Captured (Products mega menu, language menu, phone menu) |
| Tooltip | Not present |
| Dialog | Captured (search). FAQ answer is an inline panel, not a modal |
| Toast | Not present |
| Card | Captured (contact cards, menu promo cards) |
| List row | Captured (phone menu rows, search suggestions) |
| Table | Not present |
| Avatar | Not present as a component. Leadership portraits were not cropped |
| Badge | Not present |
| Disabled, loading, error | Not captured. The public pages did not show them |
| Hover and pressed on every control | Hover was read for the primary button, Contact Sales, and footer links. Pressed was not held |
