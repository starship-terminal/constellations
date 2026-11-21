# Components

Public signed-out Walmart. Header controls measured 2026-11-19. Add, Add to cart, the Rollback badge, and the current price measured 2026-11-21. Values are token names. The product is light only.

## Button

Departments is a 32px chip, padding 6px 12px, radius `core.radius.pill`, 1px border `light.border.chip`, label 14px / 700 in `light.text.brand`. See [components/crops/button-department.png](components/crops/button-department.png).

A real pointer hover did not change its fill or border. Keyboard focus computed a 0px outline. Pressed and disabled were not captured.

Add on a toys tile is a blue pill, fill `light.action.accent-bg`, white label, radius 1000px. See [components/crops/button-add.png](components/crops/button-add.png). It was not clicked.

Add to cart on the product buy box computed 126 by 40, fill `rgb(0, 83, 226)`, white 16px / 700 EverydaySans, radius 1000px. See [components/crops/button-add-to-cart.png](components/crops/button-add-to-cart.png). It was not clicked.

The EN language control is a header pill, fill `light.action.accent-bg`, white label.

"Join Walmart+" on `/plus` is the same blue pill. It was not clicked.

## Icon button

The search submit is 32px by 32px, radius `core.radius.round`, fill `light.action.search-bg`, white glyph. See [components/crops/icon-button-search.png](components/crops/icon-button-search.png).

The cart is a 64px by 52px header control, radius 32px, transparent fill, white label `$0.00`. See [components/crops/button-cart.png](components/crops/button-cart.png). Checkout was not entered.

The favorite control on a product tile is a small heart. It was not activated.

## Link

Shop now on a hero card is underlined. Sign In is a header control that opens the account menu. See [components/crops/button-sign-in.png](components/crops/button-sign-in.png) and [screenshots/home-light-account-menu.png](screenshots/home-light-account-menu.png). The identity destination was followed only as far as the captcha.

## Text field

The search field is 52px tall, radius 9999px, padding 1px 40px 1px 24px, white fill, 16px EverydaySans, border-width 0. Placeholder: "Search everything at Walmart online and in store". On a 390 viewport the placeholder is "Search Walmart". See [components/crops/text-field-search.png](components/crops/text-field-search.png).

Keyboard focus computed a 1px auto outline `light.focus.ring`. Nothing was typed into the kept shots. No text area.

## Select, checkbox, radio, switch

The buy box has a selected "New" radio and an "Open Box" radio marked out of stock. Protection-plan checkboxes sit below Add to cart, empty. None were changed. No switch. No select.

## Tabs

Not present.

## Menu

Departments opens a left flyout of department links. Grocery opens a second list. Services opens a services flyout. The account menu is a white panel: Sign in or create account, Purchase History, Walmart+, Subscriptions, Language. The phone menu is a drawer with the same account rows plus Departments, Services, and Help. See [site-tree.md](site-tree.md) and [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

## Tooltip, dialog, toast

"Pickup or delivery?" opens a fulfillment dialog (Shipping, Pickup, Delivery). It was closed. No address was typed. Sparky opened itself on the product page and was closed. No toast.

## Card

Hero cards are photographs with white type and an underlined Shop now. Product tiles on the toys page are flat: image, heart, Rollback or Deal badge, Add or Options, then a green "Now" price and a gray was-price. No card shadow.

## Badge

Rollback is a red mark with a down arrow and the word Rollback. See [components/crops/badge-rollback.png](components/crops/badge-rollback.png). Deal is a second mark on the same row. "100+ bought since yesterday" and "Overall pick" are chips on the product page. Their CSS was not read as a separate token.

## Price

The current price is green: "Now" plus the dollars. The previous price is gray beside it. See [components/crops/price-now.png](components/crops/price-now.png). On the 2026-11-19 home tiles the price was a split black number (dollars 24px / 700, dollar sign and cents 14px / 700). Both patterns are in the live shop. The green "Now" matches `light.status.positive`.

## Nav chip

Pharmacy is a 32px chip, white fill, 1px border `light.border.chip`, radius 9999px, 14px / 400. See [components/crops/chip-nav.png](components/crops/chip-nav.png).

## Gaps

- Pressed, disabled, loading, and error states were not captured.
- Focus on Departments was a 0px outline. Focus on the search field was a user-agent outline.
- No switch, tabs, tooltip, toast, table, avatar, or text area on the captured pages.
- The fulfillment dialog was closed without measuring its controls.
- Sign-in and signup stopped at a captcha. Empty fields were not photographed.
- Search results, help, and a missing route returned a bot block.
- Dark theme is not present.
- Footer links were in the DOM and not on screen.
