# Components

Measured on the public signed-out Singapore storefront, 2026-11-19. Element crops were not taken. The T3 preview browser returned "The browser is not producing screenshot frames", and headless Chromium received Access Denied.

| Component | What was measured | Evidence |
|---|---|---|
| Button | Black fill `#000000`, white label, 36px tall, padding 10px 20px, radius 0. Add to Cart, Apply, Go to Singapore. | [raw/components-computed.json](raw/components-computed.json) |
| Quiet button | Transparent fill, black label, same 36px box. Continue to Singapore. | same file |
| Disabled button | Send is `#f2f2f2` with `#999999` label while `disabled`. Not submitted. | same file |
| Link | Nav and footer links are 12px uppercase Helvetica_Reg, no underline. | same file |
| Text field | Newsletter first name, last name, and email: 41px, underline `1px solid #000000`, radius 0. Not submitted. | same file |
| Search | Header search input 44px, placeholder SEARCH, form border `1px solid #000000`. | same file |
| Select | Store country select, 41px, bottom border `1px solid #000000`. Not changed. | same file |
| Radio | 12px circle, 1px black border. Unchecked white, checked black. | same file |
| Checkbox | Native input is 1px and visually hidden. Selected colour shows a 16px check. | [icons/check.svg](icons/check.svg) |
| Menu | Highlights mega-menu and the 390px filter dialog, both on `#ffffffe6`. | same readings file |
| Product card | Image about 387 by 484. Title and price 12px. | same file |
| Icon button | Menu, search, and cart are 24px strokes. | [icons/](icons/) |

## Gaps

Text area, switch, tabs, tooltip, toast, table, avatar, and badge were not on the pages opened. Add to Cart hover did not change under a synthetic mouseover. A live validation error was not triggered, because the newsletter was not submitted. Focus on Add to Cart is a 2px `#999999` outline.
