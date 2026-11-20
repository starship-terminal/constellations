# Components

Measured on the public US storefront, 2026-11-19, viewport 1169 by 731 at 2x. No crops: the preview browser produced no screenshot frames.

## Button

Primary. Geo dialog `.zds-button--primary.zds-button--small`. Background `#000000`, text `#ffffff`, height 32px, padding 2px 12px, radius 0, font 13px weight 300, uppercase. The account page CONTINUE (`.mds-button--primary`) matched those colours and the 32px height. It was not clicked.

Secondary. Product page `.product-detail-cart-buttons__add-to-cart.zds-button--secondary.zds-button--large`. Background `#ffffff`, text `#000000`, border 0.5px solid `#000000`, height 40px, padding 2px 12px, radius 0. Label changed from ADD to SELECT A SIZE when the size list opened. The button was not used to add the item.

Skip link. `.skip-to-content.zds-button--secondary.zds-button--small`. Same secondary colours, height 32px, border 0.5px solid black.

## Link

Header `.layout-actionable` links (SEARCH, BAG, LOG IN, HELP). 13px, weight 300, line-height 22px, uppercase, colour `#000000`, padding 5px 0, radius 0. The active bag link on the cart page computed weight 500.

## Text field

Search. `input.search-home-input`. 12px, weight 300, padding 8px 0, width 770px, radius 0, placeholder "What are you looking for?". Focus did not add a border in the computed style.

Help search. `.help-search-box__search-box-input` after focus. Border-bottom 1px solid `#000000`, height 32px, radius 0.

Account email. `input[name=username]`. Height 40px, padding 18px 0 2px, 13px weight 300. The field chrome `.mds-base-field__control` computed border 0.5px solid `rgb(121, 121, 121)`. The EMAIL label computed 12px, weight 300, colour `rgb(107, 107, 107)`, uppercase. Not submitted.

## Tabs

Search section buttons. Selected Woman: 12px, weight 500, letter-spacing 0.8px, uppercase, padding 8px 0 0. Unselected: weight 300.

## Dialog

Geo dialog wrapper `.zds-dialog__wrapper`. Background `#ffffff`, border 1px solid `rgb(204, 204, 204)`, padding 20px 20px 0, radius 0, box-shadow none, width 393px, height 262px. Title `.zds-dialog-title` 15px, weight 300, line-height 24px, uppercase.

Size list `.size-selector`. Background white, border 0.5px solid black, width 356px. Size buttons 20px tall, padding 2px 4px, label 12px weight 300 uppercase. No size was chosen.

## Card

Grid tile `.product-grid-product`. Image link 905 by 1357 at this viewport. The info block under the image had height 0, so name and price were not in the grid text. On search, the product name link computed 11px weight 300 uppercase.

## List row

Help `.zds-selection-cell`. Height 40px, padding 12px 0, label 12px weight 400.

## Empty and error

Empty bag title computed 12px, weight 300, uppercase. 404 title `.page-not-found-view__title` 15px weight 300 uppercase. Subtitle 12px weight 300.

## Gaps

Hover, pressed, disabled, loading, and error-validation states were not captured. Checkbox, radio, switch, select, text area, tooltip, toast, table, avatar, and badge were not on the measured pages. The category menu was in the DOM at height 0 and was not opened. No crops exist.
