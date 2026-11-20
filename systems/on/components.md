# On components

Measured on www.on.com/en-sg/ on 2026-11-19, signed out, at 1440 x 900 unless a row says otherwise. Crops are cut from the page screenshots. Read the values from [tokens.json](tokens.json).

## Button

Default height 48px, padding 0 24px, radius 40px, On Bold 16/20, 1px border.

| State | What was read |
|---|---|
| Primary | Black fill, white text. Add to bag, Sign up now, Continue. [button-add-to-bag](components/crops/button-add-to-bag.png) |
| On a photograph | White fill, black text, class `_dark_`. [button-primary-on-photo](components/crops/button-primary-on-photo.png) |
| Outlined | Transparent fill, 1px black border. Select a size, Show filters |
| On a dark card | Outlined white, and a white fill with black text. [dialog-added-to-bag](components/crops/dialog-added-to-bag.png) |
| Focus-visible | 4px `#2f7efe` ring. Read by focusing a button. No focus crop: the preview browser took no frames, and the headless shots were not focused |
| Disabled | Opacity 0.25 on the same black fill, before a size is chosen |
| Pressed, hover, loading | Declared in the button stylesheet. Not held for a computed read |

## Icon button

48px circle. Search, bag, AI, and account in the desktop header. The phone bar uses the same 48px targets. [header-default](components/crops/header-default.png), [nav-mobile](components/crops/nav-mobile.png).

The close control is 40px, `#e5e5e5`, circle.

## Link

Nav links are On Bold 20/30, white over the hero and black on a light page. Footer links are 16/24 with 0.2px tracking. The privacy link in the dialog is 13.5px `#666666`. Unstyled links (skip link, logo link before the SVG paints) are the browser blue.

## Text field

Email field in the newsletter dialog: 64px tall, background `#0000000d`, text `#666666`, square corners, 16px On. Invalid and warning colours are declared (`#ed0000`, `#e15f14`) and were not shown, because the form was not submitted.

## Tabs

The shop activity row is 16px On Medium. The selected item is black with a 2px underline. The others are `#4d4d4d`. [tabs-activity](components/crops/tabs-activity.png).

Women's / Men's on the product page is a pair of 48px text buttons. The selected one reads as an outlined pill in the screenshot. Its computed border was 0, so the pill edge is painted by a sibling, not by the link itself.

## Menu

The size list is a 453px white panel, radius 4px, with the measured shadow. Rows are 56px. [menu-size-open](components/crops/menu-size-open.png).

The phone menu is a full-width white sheet. Shop, Sports, and Explore are 26px bold. Secondary links are 20px medium. [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).

## Dialog

The newsletter dialog is a centred card with an email field and a black Sign up now pill. It was closed and not submitted. [product-light-added](screenshots/product-light-added.png) shows it behind the bag card.

The added-to-bag card is 509px, black, radius 12px, white type, two pills. [dialog-added-to-bag](components/crops/dialog-added-to-bag.png).

## Card

Product cards on the grid are square-cornered. The title is 15.3px bold, the description 15.3px regular, the price 13.4px. A limited-edition label is On Mono 12px `#995c00`. [card-product](components/crops/card-product.png).

Editorial cards on the home page are 4px radius.

## List row

Size rows are 56px, full width of the panel, square, 16px On. An out-of-stock row keeps the same row and adds "No items left in stock" and "Notify me". That row was not opened.

Filter rows (Men, Women, Kids, product type) are 22px tall labels next to a 19px checkbox.

## Badge

The AI mark on the header icon is On Semi Mono 8px bold, white on black in the screenshot, measured as an 8px white chip with black type and 2px radius on a different badge node. Treat the header chip as observed in [header-default](components/crops/header-default.png). The amber BESTSELLER label is the product badge.

## Checkbox and radio

The filter column paints a 19px square checkbox with a 1px black border. The sort control is a radio whose input measured 1px. Neither was toggled.

## Gaps

- No dark theme on the public storefront.
- Search panel, account, order status, store locator, and checkout were not opened.
- The newsletter form was not submitted, so the error state of the email field is a declared colour only.
- Hover, pressed, and loading were declared and not held.
- Focus was read and not cropped.
- Tooltip, toast, table, avatar, switch, text area, and select were not on the captured pages.
- Icon SVGs other than the header logo were not extracted. The logo SVG in the DOM was a partial path, so it is not stored.
