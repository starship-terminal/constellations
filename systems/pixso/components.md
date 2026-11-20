# Components

Values are computed styles from the signed-out pages on 19 November 2026, viewport 1169 by 731. There are no crops. `preview_snapshot` returned no frames.

## Button

Marketing primary, home hero `a.px-common-btn`: fill `rgba(0, 0, 0, 0.84)`, text `rgb(255, 255, 255)`, Figtree 14px weight 600, line-height 16.1px, padding 10px 20px, radius 8px, height 44px, border 1px solid `rgb(0, 0, 0)`, shadow `rgba(255, 255, 255, 0.3) 0px 0.8px 0px 0px inset`. Later "Get started" buttons of the same class were 40px tall.

Product primary, `a.up-button.up-primary`: fill `rgb(32, 34, 44)`, text white, 15px weight 650, padding 12px 22px, radius 9px, height 50px, border 1px solid transparent.

Product secondary, `a.up-button.up-secondary`: fill white, text `rgb(37, 45, 61)`, border 1px solid `rgb(211, 218, 232)`, same size and radius as the product primary.

Pricing table, `.price-module__version-header-item-btn`: height 34px, padding 10px 12px, radius 8px, 14px weight 400. "Get started" and "Contact us" are white with shadow `rgba(0, 0, 0, 0.1) 0px 1px 1px 0px, rgba(0, 0, 0, 0.4) 0px 0px 1px 0px`. "Upgrade" buttons are `rgb(34, 34, 34)` with white text and shadow `rgba(255, 255, 255, 0.3) 0px 1.5px 0px 0px inset`.

Login submit, `.btn--next`: fill `rgb(51, 111, 255)`, text white, Outfit 14px weight 500, padding 14px 0, radius 8px, height 40px, width 358px. Hover, pressed, disabled and loading were not shown.

## Link

Nav "Log in", `a.login-txt.login`: `rgb(61, 61, 61)`, Figtree 14px weight 500, line-height 20px, no fill.

Nav "Get started" uses the same class with white text, sitting on the dark header button behind it.

Login brand links (`.btn--brand`): `rgb(31, 97, 255)`, Outfit 14px weight 400 or 500, no fill.

Product text link "View full-size image": `rgb(52, 92, 218)`, 12px weight 400.

## Text field

Email, `.input--box`: white fill, Outfit 14px, padding 13px, radius 8px, height 40px, width 358px. While focused, border was 2px solid `rgb(31, 97, 255)`. Outline was `none`. Placeholder "Email".

Password, `.pw-input`: white fill, padding 14px, radius 8px, height 40px, border 1px solid `rgba(0, 0, 0, 0.1)`. Placeholder "Please enter the password". The visibility icon is `rgb(162, 164, 168)`.

The third-party rows (Google, NAVER) are 40px tall, radius 8px, border 1px solid `rgba(6, 6, 31, 0.09)`, label Outfit 14px weight 500.

Error, disabled and filled states were not shown. `--v2--color-border-input-error` is `#f43529` and was not on a field.

## Nav

`nav.pxn-navbar`: height 54px, fill `rgba(255, 255, 255, 0.8)`, text `rgb(30, 35, 48)`, Figtree. On the product page the same bar had `backdrop-filter: blur(16px)`. Dropdown cards were in the DOM at height 0. Their declared radius is 9px to 13px. An open menu was not measured.

## Login card

`.login-pixso--container__right`: white, width 474px, radius 12px, shadow `rgba(31, 19, 135, 0.04) 0px 8px 16px 0px, rgba(17, 30, 58, 0.2) 0px 0px 2px 0px`. Inner `.oversideSignin-page` padding is 50px 58px. Title `.oversea-page--title` is Outfit 28px weight 600, line-height 35px, `rgb(25, 25, 26)`. The hint "Don't have an account?" is `rgb(139, 140, 143)`, 14px, line-height 22px.

## Pricing columns

`.select-plan-item` is transparent, padding 18px, no radius and no shadow. Plan titles that were readable used white text at 20px weight 600 on a header whose own background computed to transparent, so the title colour is not a fill you can copy without the missing screenshot. Price figures such as `$18` are Figtree 16px weight 600, black.

## Gaps

No icon button, text area, select, checkbox, radio, switch, tabs, tooltip, dialog, toast, list row, table, avatar or badge was on the signed-out pages. Toast, mask, danger, success and warning colours exist as `--v2--` custom properties and were not seen on an element. Hover, pressed, disabled and error states of the buttons and fields were not triggered. The signed-in editor was not opened.
