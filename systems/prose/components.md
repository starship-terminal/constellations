# Components

Public marketing only, measured 2026-11-19 on prose.com. Computed styles at 1440×900 unless a row says 390. No crops: the preview browser returned "The browser is not producing screenshot frames."

| Component | Where | Measured | Gap |
|---|---|---|---|
| Button, filled | Home and product "GET YOUR FORMULA" | 48px tall, padding 15px 32px, radius 60px, bg #323429, text #fff, Simplon Mono 12px/14.4px, weight 500, tracking 0.96px, uppercase, border 1px #323429, transition 0.3s background, color, font-size | Hover colour is in the class (`any-hover:bg-primary-100`) and was not computed, because hover was not applied |
| Button, inverse | White pill on the dark hero | bg #fff, text #323429, border #fff, same size and radius | |
| Button, promo | Product page second "GET YOUR FORMULA" | bg #f69371, text #323429, border #f69371, same pill | |
| Button, disabled | Sign-in "SIGN IN" with an empty email | bg #a6a6a6, text #fff, disabled attribute set | Loading state not shown |
| Text button | "SHOP ALL HAIR", "LEARN MORE" | Simplon Mono 12px, uppercase, tracking 0.96px, transparent background, no border | |
| Link | Nav "Haircare" | Simplon Norm 14px, weight 400, #323429, tracking 0.28px, no underline | |
| Text field | Home promo email, then dismissed | 56px tall, padding 8px 16px, radius 0, bg #fff, border 1px #eaeaea, placeholder "Enter email address" | Not submitted |
| Text field, underline | /signin email | Input itself has no border. Wrapper ::after is 2px solid #323429. Label is Simplon Norm 16px #6c6c6c | Not submitted. Error state not reached |
| Radio | Product purchase option | 18×18, appearance auto. The option card is bg #f9f7f2, border 1px #e2d9c2, radius 10px, padding 16px 12px | Selected versus unselected not compared |
| Choice card | /consultation/category | 360×129, radius 10px, border 1px #f1ece0, image 101×127, title 14px #323429, transition 0.2s border-color | Pressed state not measured. Quiz was not started |
| Dialog | Home promo, then closed | role=dialog, radius 10px, max-width 340px, bg #f9f7f2, open animation contentShow 0.25s cubic-bezier(.16, 1, .3, 1) | Closed before a screenshot. Email was not submitted |
| Nav | Header | Sticky. Banner 40px #323429. Nav row 55px. Header 95px. Nav surface #fff with shadow 0 2px 3px #b4b4b433 | |
| Menu, desktop | Haircare menu, aria-expanded true | Panel absolute, full width, 345px tall, category label Simplon Mono 12px uppercase #6c6c6c, link Simplon Norm 16px #323429, opacity transition 0.2s | |
| Menu, phone | Open menu at 390×844 | Drawer .menu-open, bg #fff, 390×804, height transition 0.56s cubic-bezier(0.52, 0.16, 0.24, 1). Category title Saol 300 20px #323429 | |
| Accordion | /faq summary | Simplon Norm 16px. Opened once. Content colour #000, 16px | One item only |
| Badge | Home product tiles say "Bestseller" and "New" in the link text | Not isolated as its own element on the catalogue page | Colour of the badge chip not measured |
| Toast | Sonner stylesheet is inlined | Declared, not shown. Light theme --normal-bg #fff, --error-bg hsl(359, 100%, 97%) | No toast fired |
| Tabs, switch, checkbox, select, tooltip, table, avatar | | | Not present on the public pages that were opened |

## Gaps

- Hover, pressed, and focus-visible styles are declared (`any-hover`, `focus-visible:outline-primary-300`, `focus-visible:outline-2`). The one focused control measured, the white "GET YOUR FORMULA", showed the browser outline `rgb(229, 151, 0) auto 1px` with offset 1px. That colour is not a Prose custom property.
- Disabled, error, loading, and validation were not produced. Nothing was submitted.
- No dark theme. The fetched root stylesheet has no `.dark`, `data-theme`, or `prefers-color-scheme` rule.
