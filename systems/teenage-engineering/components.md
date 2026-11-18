# Components

Public marketing and store listing, measured signed out on 2026-11-19. Checkout, cart, and payment were not entered. The add-to-cart plus was measured and not pressed.

| Component | What was measured | Token |
|---|---|---|
| Button | Newsletter subscribe: face `#0f0e12`, label `#f5f5f5`, height 73px, radius 0, type 26.449px weight 300. Hover drops opacity to 0.7 and does not change the colour. Disabled face in button.css is `#b2b2b2` with a `#f5f5f5` label. The phone menu join button computed that grey face (`#b2b2b2`) with a `#0f0e12` label and a 7.959px radius | `light.component.button` |
| Icon button | Store add control is a 15px plus, transparent, black, radius 0. Its hit area is the 48px `--btn-min-click-area` after-box. It was not pressed | `core.size.click` |
| Link | Links inherit colour and have no underline by default. Footer and discreet links underline on hover. The 404 return link is underlined at rest, 26.449px, black. Hover did not change that colour | `core.typography.link-return` |
| Text field | Newsletter email: white face, black 1px border when focused, radius 0, height 60px, padding 22.041px 14.694px 7.347px, type 19.102px. Outline is none. Placeholder colour is `#7f7f7f` | `light.component.field` |
| Text area | Not on the pages that were open. form.css styles `textarea` with the same field tokens | gap |
| Select | Country select in the footer is a native select, opacity 0, sitting over a lowercase label. Focus underlines that label. No custom menu was opened | gap |
| Checkbox | Newsletter consent: 29px square, radius 0, 2px `#e5e5e5` border, white face. Checked state in form.css fills `#0f0e12` and draws a `#f5f5f5` tick. It was not checked | `core.size.checkbox` |
| Radio | Not present on the pages that were open | gap |
| Switch | Not present | gap |
| Tabs | Store category row (all products, pocket operators, field system) is a link list, not a tab widget. Selected state was not isolated | gap |
| Menu | Phone menu is a fixed black panel, white type, a search field at 10% white, and a grey join button. Desktop uses the icon header, not a dropdown | `light.background.stage` |
| Tooltip | Not shown | gap |
| Dialog | A country or region list is in the page text. It was not dismissed and no country was chosen, so it was not treated as a measured dialog | gap |
| Toast | Not shown. message tokens exist in the CSS (`--message-border-radius`, `--message-box-shadow`) and were not painted | gap |
| Card | Store tile: product image on `#f5f5f5` (`--product-background-color`), title at 19.102px, price, strikethrough discount, plus. Tile radius is 0 on desktop | `core.color.white` |
| List row | Phone menu footer rows (store, guides) with a chevron and a hairline. Divider colour is `#b2b2b2` | `light.border.divider` |
| Table | Not present | gap |
| Avatar | Not present | gap |
| Badge | `-30%` pill: `#0f0e12` face, white label, 13.225px, radius 9999px, padding 6.612px 9.918px, height 28px | `light.component.badge` |

## States

| State | Reading |
|---|---|
| Hover | Subscribe opacity 0.7. Link underline on discreet and footer links. Colour does not change |
| Focus | Email border becomes 1px solid `#000000`. Outline is none. form.css also names `--te-grey-400` for focus, and that custom property is not declared in root.css |
| Pressed | Not held |
| Disabled | Authored in button.css as `#b2b2b2` face. Seen as the phone join button |
| Selected | Checkbox checked fill is authored, not checked. Store category selection was not isolated |
| Error | `--error` `#c0262c` on `[aria-invalid=true]`. No form was submitted |
| Loading | Spinner is a 1s linear infinite ring. It was not on screen |

## Gaps

- Checkout, cart, payment, and account were not entered.
- No form was submitted, so validation, success, and error feedback were not seen.
- Radio, switch, tabs, tooltip, toast, table, and avatar were not on the public pages that were open.
- Dark theme: `color-scheme` was `normal` on every page. The product stage is black by design, not a dark theme switch.
- Hover colour on the add plus and the nav icons was not forced beyond the subscribe button and the 404 link.
