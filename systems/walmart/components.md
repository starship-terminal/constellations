# Components

Public signed-out Walmart, measured 2026-11-19. Values are token names. The product is light only.

## Button

Departments is a 32px chip, padding 6px 12px, radius `core.radius.pill`, 1px border `light.border.chip`, label 14px / 700 in `light.text.brand`. See [components/crops/button-department.png](components/crops/button-department.png).

A real pointer hover did not change its fill or border. Keyboard focus computed a 0px outline. Pressed and disabled were not captured. The declared primary fill is `light.action.accent-bg`, hover `#114ab6`, pressed `light.action.accent-pressed`. Those states were not seen on a control.

The EN language control is a 52px by 84px pill, fill `light.action.accent-bg`, label 16px / 700 white, radius 1000px. It sits in the header.

## Icon button

The search submit is 32px by 32px, radius `core.radius.round`, fill `light.action.search-bg`, white glyph. See [components/crops/icon-button-search.png](components/crops/icon-button-search.png).

The cart is a 64px by 52px header control, radius 32px, transparent fill, white label. See [components/crops/button-cart.png](components/crops/button-cart.png).

The favorite control on a product tile is 32px by 32px, radius 16px, white fill. It asks the shopper to sign in. It was not activated.

## Link

Product title links compute `light.text.link` with underline. Shop now on a hero card is 14px / 400 white with underline. Sign In is a link styled as a header control: 52px tall, padding 4px 16px 4px 12px, radius 32px, white text. See [components/crops/button-sign-in.png](components/crops/button-sign-in.png). It was not followed. The destination is identity.walmart.com.

## Text field

The search field is 52px tall, radius 9999px, padding 1px 40px 1px 24px, white fill, 16px EverydaySans, border-width 0. Placeholder: "Search everything at Walmart online and in store". See [components/crops/text-field-search.png](components/crops/text-field-search.png).

Keyboard focus computed a 1px auto outline `light.focus.ring`. Nothing was typed. No text area.

## Select, checkbox, radio, switch

Not present on the captured pages. Departments and Services look like menus and were not opened.

## Tabs

Not present.

## Menu

The phone header has a menu button. It was not opened. Departments was not opened.

## Tooltip, dialog, toast

A location dialog ("How do you want your items?") was open on first paint in the preview tab. It was closed by its close control. Its contents were not measured as a component. No tooltip or toast.

## Card

Hero cards are full-bleed photographs with white type and an underlined Shop now. Radius was not measured on the hero card. Product tiles are 208px wide, radius 0, no shadow, no border. The image is 208px square, radius 0.

## List row, table, avatar, badge

Not present as components. The price is a split span: dollar and cents at 14px / 700, dollars at 24px / 700, color `light.text.primary`. A "Rollbacks & more" mark is painted into hero art. Its CSS was not read.

## Nav chip

Pharmacy is a 32px chip, white fill, 1px border `light.border.chip`, radius 9999px, 14px / 400, color `rgb(0, 46, 153)`. See [components/crops/chip-nav.png](components/crops/chip-nav.png).

## Gaps

- Hover on Departments did not change computed styles. Declared hover fills are in the tokens and were not seen on a control.
- Pressed, disabled, loading, and error states were not captured.
- Focus on Departments was a 0px outline. Focus on the search field was a user-agent outline, not the 2px token.
- No select, checkbox, radio, switch, tabs, tooltip, toast, table, avatar, or text area on the captured pages.
- The location dialog was closed without measuring its controls.
- Sign-in was not entered. Help, Walmart+, and a missing route returned a bot block to headless Chromium.
- Dark theme is not present. A dark colour-scheme preference left the header blue and `color-scheme` at `normal`.
- Footer links were in the DOM and not on screen in the captured viewports. Their computed styles were not read.
