# Components

Measured on slite.com, signed out, on 2026-11-19. Values are computed styles. Crops are from the live public pages.

## Button

Start for free is the primary pill. Background `#2d2f34`, text `#fdfdfd`, UniversalSans 16px / 600, height 38px, padding 0 16px, radius 999px, no border, no shadow. See [button-primary-light-default](components/crops/button-primary-light-default.png).

Book demo is the ghost pill. Transparent fill, 2px border, text `#2d2f34`, same height and radius. See [button-secondary-light-default](components/crops/button-secondary-light-default.png).

Talk to us is the accent pill. Background `#f67748`, text `#ffffff`, 17px / 600, height 64px, padding 0 32px, radius 999px. See [button-accent-light-default](components/crops/button-accent-light-default.png).

Get started on pricing repeats the primary and ghost pills at the card width (337px and 339px). Contact Sales is the ghost. Continue with email on the create page is a different control: `#2e77e5`, 14px / 600, height 36px, radius 8px, padding 8px 12px. It was not pressed.

## Link

Nav links are UniversalSans 15px / 600, color `#3f434a`, padding 0 12px, height 32px, radius 999px. See [link-nav-light-default](components/crops/link-nav-light-default.png).

Terms and privacy on the create page are `#6a707c` and underlined.

## Text field

The sign-in email field is empty. Placeholder `name@company.com` in `#6a707c`, 13px, padding 0 12px. The label draws the box: 1px `#d8dadf`, radius 8px, height 42px. Focus moves a 2px outline of `rgb(69, 136, 237)` onto the label. The input itself keeps `outline: none`. See [field-email-light-default](components/crops/field-email-light-default.png) and [field-email-light-focus](components/crops/field-email-light-focus.png).

The workspace URL field sits in the same box, with a `.slite.com` suffix in `#6a707c`.

## Badge

New is `#f67748` with white text, 12px / 600, padding 0 6px, radius 6px, height 20px. See [badge-new-light-default](components/crops/badge-new-light-default.png).

## Switch

The pricing "Billed yearly" control is a checkbox with class `react-toggle`. Checked track is `#2d2f34`, 29 x 16, radius 16px. Thumb is `#fdfdfd`, 12 x 12, radius 50%. Unchecked track is `#6a707c`. Turning it off changed the Basic price from `$10` to `$12`. See [switch-checked-light-default](components/crops/switch-checked-light-default.png) and [switch-unchecked-light-default](components/crops/switch-unchecked-light-default.png).

## Card

The recommended plan is an orange frame (`#f67748`, radius 18px, padding 32px 2px 2px) around a white card. RECOMMENDED is 12px / 700, white. See [card-plan-light-default](components/crops/card-plan-light-default.png).

The sign-in card is `#fdfdfd`, 560px wide, padding 48px 60px, radius 16px, on a `#f9efe4` page. See [card-signin-light-default](components/crops/card-signin-light-default.png).

## Tabs

On features, Leverage insights is selected: 1px solid `#3f434a`, radius 50px, 19.2px / 500, padding 12px 16px, height 53px. The other two tabs are `#6a707c` with a transparent border.

## Menu

At 390, Open menu is a 48px button. The drawer rows are 18px / 600, height 48px, padding 0 25px 0 20px, full width. Book demo in the drawer is the orange pill, 342 x 54. See [home-light-menu](screenshots/home-light-menu.png).

## Gaps

- Hover, pressed, disabled, loading, and error were not on the public pages.
- Text area, select, radio, tooltip, toast, table, and avatar were not present.
- The signed-in sidebar, editor, and settings were not entered. `:root` still declares `--sidebar-item-*` tokens.
- OAuth rows were measured and not pressed.
