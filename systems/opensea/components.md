# Components

Measured on signed-out opensea.io, dark theme, 2026-11-19. Crops are reconstructions of the computed boxes. They are not live pixels.

## Button

| State | Where | Values |
|---|---|---|
| Nav selected | Home | 32px tall, `#161616` face, 14px / 500, padding `0 12px 0 8px`, pill radius, gap 6px, `0.2s ease-out` |
| Nav rest | Explore, Search | Same box, transparent face |
| Sign in, desktop | Nav at 1440 | 32 x 76, transparent face, white label, padding `0 16px`, pill |
| Sign in, phone | Nav at 390 | 32 x 68, `#0086ff` face, white label, pill |
| Filter selected | All, Sale, Live & Upcoming | 28px tall, `#161616`, 1px `#2c2c2c`, 14px / 500, padding `0 10px`, pill |
| Filter rest | Listed, Past | 28px tall, `#0c0c0c`, 1px `#202020`, `#acacac` label, 14px / 400 |
| Get the app | Banner | 24px tall, `#0f0f0f`, 1px `#202020`, padding `0 6px`, pill |
| Buy Now | Item card footer | 49px tall, `#0086ff`, 14px / 500, radius 0. Not pressed |
| OAuth | Continue with Google | 48px tall, `#0c0c0c`, 1px `#202020`, radius 12px, 14px / 500, gap 8px. Hover `#161616` / `#2c2c2c`. Not pressed |
| Close | Dialog | 34px circle, 1px `#202020`, padding 4px. Hover showed no computed change |

Crops: [button-nav-selected.png](components/crops/button-nav-selected.png), [button-signin-desktop.png](components/crops/button-signin-desktop.png), [button-signin-phone.png](components/crops/button-signin-phone.png), [button-filter-selected.png](components/crops/button-filter-selected.png), [button-oauth.png](components/crops/button-oauth.png).

## Link

Terms links on `/tos` computed to `#83c3ff`, 16px gtAmerica. That is `--color-link` in dark, which aliases `--color-blue-1`. Light `--color-link` aliases `--color-blue-3` (`#0086ff`). Hover of a live link was not forced.

## Text field

Collection search is a 32px pill: wrap `#0c0c0c`, 1px `#202020`, padding `0 12px 0 8px`, input 14px. Placeholder "Search by item or trait". Transition `0.2s cubic-bezier(0.4, 0, 0.2, 1)`.

The connect dialog email field is a 56px control, radius 12px, same face and border, placeholder "Continue with email" at `#acacac`, caret `#ffffff`. Focused outline on the input was `none 1px #99c8ff`. The wrapper border stayed `1px #202020`. Nothing was typed.

Crop: [field-email.png](components/crops/field-email.png).

## Tabs

Collection tabs (Items, Holders, Traits, Activity, Analytics, About) are 56px tall, 16px, selected weight 500 and white, rest `#acacac`. No `::after` bar was computed. Discover categories are 32px text links, 16px, not pills. Drops uses the filter pill pair.

## Menu

More menu: 200px wide, `#0c0c0c`, 1px `#202020`, radius 12px, padding 4px. Rows are 33px, 14px / 400, padding `6px 8px`, radius 8px. The settings submenu is the same chrome at 176 x 307. Opening a settings URL bounced to the connect dialog.

Crop: [menu-row.png](components/crops/menu-row.png).

## Dialog

Connect with OpenSea: 480 x 706, `#080808`, 1px `#202020`, radius 12px, no shadow. Overlay `rgba(0, 0, 0, 0.6)`, which is `--color-overlay` in dark. Title is an h4, 24px / 500 / 30px. Legal line is 12px `#acacac`. Closed with Escape. No provider was chosen.

## Card

Item media is 257 x 257 on `#161616`, radius 0. The card shell is 257px wide with radius 8px. Home collection cards were full-bleed images (one measured 747 x 420) with a 32px / 48px title over them.

Crop: [card-media.png](components/crops/card-media.png).

## List row

Wallet rows: 57px tall (More Wallet Options 53px), padding 16px, gap 12px, 16px / 400. First row radius `12px 12px 0 0`, last row `0 0 12px 12px`. The list is `#0c0c0c` with 1px `#2c2c2c` and radius 12px. Activity events were links, not a table.

## Avatar

A collection avatar measured 63 x 63, radius 4px.

## Badge

Tools "BETA" was 16px gtAmerica text, not a filled chip. No filled badge was on the pages that loaded.

## Gaps

- Text area, select, checkbox, radio, and switch were not on the signed-out pages.
- Tooltip and toast are declared (z-index 810 and 910, Sonner tokens) and were not on screen.
- Pressed, disabled, loading, and error states were not shown.
- A live light theme was not switched. Settings was gated.
- Cookie preferences was listed in the settings menu and not opened.
- Help center is a separate skin. See the README.
