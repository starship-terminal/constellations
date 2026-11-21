# Components

Public MasterClass, signed out, measured on 2026-11-21. Crops are in [components/crops/](components/crops). Values are token names from [tokens.json](tokens.json). Computed readings are in [raw/components-computed.json](raw/components-computed.json).

## Button

The Get MasterClass link. Fill is `dark.accent.default` (`core.color.pink.500`, #e32652). Text is `dark.text.on-accent`. Radius is `core.radius.sm` (8px). Padding is 12px by 24px. Weight 600, size 16px, line height 20px, letter-spacing 0.16px, capitalize. Hover and pressed are `dark.accent.hover` and `dark.accent.pressed` in the stylesheet. A loading state was not shown. Disabled was not shown on a public control that could be held.

Crops: `button-default.png`, `button-hover.png`.

## Icon button

Carousel previous, next and pause. They sit on the hero. No separate icon set is kept (see Gaps).

## Link

Log In, Gifts and View Plans are quiet text links in `dark.text.primary`. The stylesheet's link hover is `dark.text` via `--mc-color-text-link-default-hover`, which resolves to neutral-400.

Crops: `link-default.png`, `link-hover.png`.

## Text field

Header search `#searchInput`, 44px tall, placeholder "What do you want to learn today?". The field chrome is the raised bar behind it (`dark.background.raised`). Newsletter and contact emails were not filled.

Crops: `search-default.png`, `search-focus.png`.

## Text area

Not present on the captured public pages. The At Work contact form uses single-line fields.

## Select

Not present as a native select on the captured pages. Browse is a menu, not a select.

## Checkbox

The homepage intent rows and the find-my-classes quiz use checkbox-like options. The quiz options are real checkboxes (`#option-0` and on). They were not submitted.

Crop: `checkbox-row-default.png`.

## Radio

The stylesheet declares `--mc-theme-radio-*`. No radio group was on the pages captured.

## Switch

Not present on the public pages.

## Tabs

Gift audience chips (For Dad, Foodies) and homepage category chips act as tabs. They filter in place. Checkout shows Membership, Account and Payment as steps, not tabs.

## Menu

Browse opens a dialog of category buttons plus View All Categories. Search opens a dialog of popular searches.

Crops: `menu-default.png`, `menu-item-hover.png`, `browse-button-default.png`.

## Tooltip

The stylesheet declares `--mc-theme-tooltip-*` (`dark.background.overlay`). No tooltip was held open on the public pages.

## Dialog

Watch Trailer opens a video dialog. Browse and search open dropdown dialogs. The promo strip is a banner, closed with Close banner.

## Toast

Not observed.

## Card

Class cards: image, New badge, instructor line, duration. Radius follows `core.radius.md` on the tile photos. Category pages repeat the same card.

Crop: `card-default.png`.

## List row

The homepage intent options are full-width rows. Help-centre articles are a link list.

## Table

Not present.

## Avatar

Instructor portraits are the card images. No account avatar is shown signed out.

## Badge

"New" on class cards, and the stylesheet's badge tokens (`--mc-theme-badge-bg` white, text black).

## Gaps

- Login and signup are a wall. `https://www.masterclass.com/auth/login` redirected to a Google sign-in. Google was not clicked. There is no site email field on that wall.
- Checkout account and payment, certificate signup, Executive apply, and the quiz after the first step were not entered.
- Newsletter, contact, phone and plan fields were not filled and not submitted.
- Dark is the only public theme. A light theme is not shipped on these pages.
- Radio, switch, text area, select, tooltip, toast, table and disabled controls were not present or not reachable.
- Icon artwork is not extracted ([docs/RIGHTS.md](../../docs/RIGHTS.md)).
- Pressed and focus-visible were not held on every control. Hover is captured for the primary button, the Log In link and a menu item.
