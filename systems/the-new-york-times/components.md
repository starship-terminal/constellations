# Components

Public signed-out chrome only. Values are computed styles from 2026-11-19. Crops were not taken: `preview_snapshot` returned "The browser is not producing screenshot frames."

## Button

Homepage Subscribe and Log in share a painted face: background `#567b95`, border `1px solid #326891`, white Franklin 11px weight 700, letter-spacing 0.55px, uppercase, padding 8px 12px, radius 3px, height 29px.

Continue to checkout is ink `#121212`, white Franklin 16px weight 600, height 44px, width 295px, radius 4px.

Login Continue is the same ink, white Franklin 16px weight 700, height 44px, radius 3px, width 450px at innerWidth 1169 and 358px at innerWidth 390.

Continue with Google and Continue with Apple are white, `1px solid #000000`, Franklin 16px weight 400, height 44px, radius 3px. They were not clicked.

The token button (`--tpl-theme-button-*`) declares a 3px radius, 44px standard height, pressed opacity 12%, and disabled opacity 40%. Those pressed and disabled values were not painted.

## Link

Section links are Franklin 14px weight 500, `#121212`, letter-spacing 0.1px. The selected edition is Franklin 11px weight 600, letter-spacing 1.4px, uppercase, `#121212`. Unselected editions are `#5a5a5a` weight 500.

Learn more is Franklin 14px weight 600, `#121212`, no underline. Legal links on the login page are Franklin 14px, `#000000`, underlined. Footer links are 12px `#767676`, underlined.

## Text field

Login email field: height 44px, padding 0 12px, radius 3px, Franklin 16px weight 500, white fill. The wrap is `1px solid #000000`, radius 3px, height 46px. The field was empty.

Homepage search, after the search button was opened: input height 31px, Franklin 14px, color `#333333`, wrap `1px solid #000000` plus `box-shadow: 0 0 0 1px #000000`, radius 3px. Focus outline was `none`. No query was submitted.

## Radio

Offer radios are 16 by 16, radius 50%, border `1px solid #000000`, white fill, accent-color `auto`. The checked fill was not a distinct computed colour.

## Tabs

Monthly and Yearly are buttons, not `role=tab`. Selected Monthly is Franklin 16px weight 600, `#121212`, padding 14px 0 9px, height 42px, radius 0. Yearly is weight 400, `#727272`. No underline was on the button or its children.

## Badge

BEST VALUE is Franklin 11px weight 600, letter-spacing 8%, padding 5px 8px 4px, radius 20px, color `#000000`, background transparent.

## Card

Offer cards are white. The unselected card border is `1px solid #dbdbdb`. The selected card's computed border was `0px`. Radius 0. Padding 20px 10px.

## Icon button

The search control is a 34 by 33 button with a 16px magnifying glass, path fill `#333333`. See [icons/search.svg](icons/search.svg).

## Text area, select, checkbox, switch, tooltip, menu, table, avatar

Not present on the measured pages.

## Dialog, toast

Declared in `--tpl-theme-dialog-*` and `--tpl-theme-toast-*`. No dialog or toast was opened. Dialog backdrop `#12121299`, radius 3px, padding 2rem, max-width 536px. Toast background `#f8f8f8`, radius 3px, min-height 56px.

## Gaps

- Hover, pressed, disabled, loading, and error were not painted.
- No validation error was triggered. The email field was not submitted.
- The section drawer was not opened.
- No element crops. Screenshot frames were unavailable.
