# Components

Public marketing chrome only. Values are computed styles from 2026-11-19. Crops are 2x element screenshots.

## Button

Primary. Yellow fill `#ffc800`, text `#3a032d`, radius 2px, padding `0 24px`, height 52px on the hero and 57px on `/ai` ("Try it today"). Font Output Sans 16px or 18px, weight 400. Hover on the visible hero button: `filter: brightness(0.95)`, background unchanged. Focus: `outline: none`, `box-shadow: none`.

Ghost. "Product Video" is transparent, same radius and padding, no border.

Outline, yellow. "View all Templates": 2px solid `#ffc800`, transparent fill, padding `12px 30px`, radius 0, height 53px.

Outline, plum. Footer "Continue with Superhuman Docs": 2px solid `#9d8196`, text `rgba(0, 0, 0, 0.5)`, radius 2px, height 57px.

Blog. "Read full post": 2px solid `#d3c7d0`, text `#5b3452`, radius 4px, padding `0 24px`, height 42px, GT Flexa 16px.

Pricing. "Get Started" labels compute to `rgba(16, 16, 16, 0.3)`, radius 4px, height 48px. The coloured card border is a separate frame (`2px #e9e3e7` on an outer box, white inner card).

Crops: [components/crops/button-primary-hover.png](components/crops/button-primary-hover.png), [components/crops/button-primary-focus.png](components/crops/button-primary-focus.png).

## Link

Nav links are Output Sans 16px, `#3a032d`, padding `0 16px`, no underline. Footer links use padding `13px 8px 3px`. Template card titles compute to user-agent `#0000ee`.

## Text field

Search on `/integrations`, `/templates`, `/docs` and `/community`: height 40px, background `#ffffff`, border `1px solid rgba(58, 3, 45, 0.2)`, radius 4px, padding `1px 2px 1px 24px`, Output Sans 18px, colour `#3a032d`. Placeholder text is the visible label ("Search integrations", "Search templates", "Search for an article", "Search spreadsheets").

## Select

A native `<select>` on directory pages computes to radius 4px and border `1px solid #d3c7d0`, with height 0 in the desktop layout. The visible filter is a custom control. Its open state was not captured.

## Card

Template card: white, radius 6px, shadow `rgba(0, 0, 0, 0.08) 0px 1px 6px 0px`, about 362x190 at 1440px.

Pricing plan card: white, radius 8px, padding `20px 15px`, shadow three layers of `rgba(58, 3, 45, 0.04)`.

Docs article card: white, radius 8px, no shadow, about 439px wide.

## Badge

"Popular" on the Plus plan: 12px Output Sans, weight 400, padding `0 8px`, colour `#ffffff`, background transparent on the text node. The pill behind it was not isolated.

## Menu

Product in the header is a button. Hover opens a panel of Rows AI, Integrations, Support Docs and Features. See [screenshots/product-light-nav-open.png](screenshots/product-light-nav-open.png).

## Gaps

- No icon button, text area, checkbox, radio, switch, tooltip, toast, avatar, or list row on the public pages.
- Dialog: Product Video was not opened.
- Tabs: Monthly / Annually is visible on `/pricing` and was not measured as its own control.
- Table: the comparison table is below the pricing viewport shot. Cell metrics were not read.
- Focus ring: keyboard focus on the primary CTA paints no outline.
- Pressed, disabled, loading and error states were not shown, except the faint pricing CTA colour noted above.
- Signed-in app components are out of reach. Login routes 404. See the README Gaps.
