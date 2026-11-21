# Components

Public signed-out controls measured on 2026-11-22. Hover, focus-visible, pressed, disabled, and loading were not measured this pass. Do not invent those states.

| Component | Where | Rest state |
|---|---|---|
| Nav pill | Homepage header | 52px tall, 26px radius, white fill, ink text, soft drop shadow. Crop: [components/crops/nav-default.png](components/crops/nav-default.png). |
| Primary pill | Header "Try Craft Free" | 36px tall, ink fill `#030302`, white label, 16px medium, padding 8px 14px, pill radius. |
| Hero pill | Hero "Try Craft Free" | 48px tall, padding 16px 32px. The painted fill on the collage is light. Read the header pill for the ink CTA. Crop: [components/crops/button-hero-default.png](components/crops/button-hero-default.png). |
| Menu | Product and Community buttons | Click opens a white panel under the nav. Product has eight links. Community has three external links. Crop: [components/crops/menu-product-default.png](components/crops/menu-product-default.png). |
| Heading | Homepage h1 | Untitled Serif 66px / 66px, weight 400, tracking -1.98px, ink. Crop: [components/crops/heading-hero-default.png](components/crops/heading-hero-default.png). |
| Body | Page | Untitled Sans 16px / 24px, weight 400, ink on beige. |
| Pricing card | `/pricing` | White and lilac cards, serif prices, pill "Get Started". Yearly is selected. Crop: [components/crops/card-pricing-default.png](components/crops/card-pricing-default.png). |
| Billing toggle | `/pricing` | Yearly and Monthly pills. Monthly was not switched. |
| Accordion | Homepage and pricing FAQ | Buttons expand in place. Not submitted. |
| Footer | Homepage | Ink panel, 24px radius, quiet link columns. |
| Phone drawer | 390 homepage | Full-height panel. Product expanded. Community collapsed. |
| Text field | `docs.craft.do` only | Empty email, placeholder "Your Email", 40 by 320. Nothing typed. |
| Auth button | Same wall | Continue, 40 by 320, radius 10px, fill `#2e6de9`, Inter 14px semibold. Crop: [components/crops/auth-continue-default.png](components/crops/auth-continue-default.png). |
| Identity buttons | Same wall | Google, Apple, Microsoft. Not clicked. |
| 404 | Missing path | Serif "Page Not Found \| 404" and a "Let us know" pill. Not clicked. |

Not present on the public pages that were measured: text area, select, checkbox (aside from a hidden captcha checkbox), radio, switch, tooltip, toast, table, avatar, badge. The docs editor, tasks, and calendar live behind the login wall and were not entered.
