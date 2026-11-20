# Instacart components

Public signed-out components, measured on instacart.com. Emotion classes are hashes, so nothing here keys off a class name. Values are token names from [tokens.json](tokens.json).

## Button

Primary actions are full pills, fill `color.accent` (#108910), label `color.on-accent`, type `typography.button`.

| Variant | Where | Height | Crop |
|---|---|---|---|
| Header primary | Sign up | 40px | [button-primary-default](components/crops/button-primary-default.png) |
| Header secondary | Log in, white with a hairline | 40px | [button-secondary-default](components/crops/button-secondary-default.png) |
| Auth primary | Continue | 56px | [button-continue-default](components/crops/button-continue-default.png) |
| Social | Google, Facebook, Phone | 40px | [button-social-google](components/crops/button-social-google.png) |
| Business | Create free business account, periwinkle, not the consumer green | 56px | [button-business-default](components/crops/button-business-default.png) |
| Help | Connect with Instacart, near-black pill | 56px | [button-help-default](components/crops/button-help-default.png) |

States: hover and focus crops exist for the header, Continue and business buttons. The green fill often does not change on hover in headless Chromium. Pressed, disabled and loading were not shown. Focus on the email field darkens the border rather than drawing a separate ring. See [text-field-focus](components/crops/text-field-focus.png).

## Search

Homepage search is a 56px pill, placeholder "Search products and stores". Focus opens a white popover of top searches and trending tiles. See [search-default](components/crops/search-default.png), [search-focused](components/crops/search-focused.png) and [home-light-search-focused](screenshots/home-light-search-focused.png).

## Text field

Login email is 48px tall, about 8px radius, gray border, placeholder "Enter your email address". Focus darkens the border to near-black. See [text-field-default](components/crops/text-field-default.png) and [text-field-focus](components/crops/text-field-focus.png). Error state was not captured.

## Chip

Filter chips are 32px pills on a gray fill. Selected "All" is near-black with white type, visible on the homepage. The cropped EBT chip is the unselected state. See [chip-default](components/crops/chip-default.png) and [home-light-default](screenshots/home-light-default.png).

## Store card

White card, 12px radius, 1px border. Store logo, name in `color.text`, delivery time in `color.success`, gray meta. See [store-card-default](components/crops/store-card-default.png).

## Badge

Yellow deal chips use `color.deal` (#FFDC23) with near-black type. "Best seller" is a small dark label on the product photo. See [deals-light-default](screenshots/deals-light-default.png) and [badge-bestseller](components/crops/badge-bestseller.png).

## List row

Help center rows are full-width links with a chevron, on a white card over the warm page. See [list-row-default](components/crops/list-row-default.png) and [help-light-default](screenshots/help-light-default.png).

## Menu

The desktop departments drawer is a white panel over a dimmed page: Departments, More ways to shop, Help. See [home-light-departments](screenshots/home-light-departments.png). The mobile drawer was not captured.

## Gaps

Text area, select, checkbox, radio, switch, tooltip, toast, table, avatar, dialog and the signed-in account menu are not in this package. Icon buttons (Add plus, carousel arrows) are visible in screenshots and were not cropped. Instacart Business buttons are a second palette.
