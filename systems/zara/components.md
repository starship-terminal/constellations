# Components

Measured on the public US storefront. Token values are from the 2026-11-19 computed styles, reconfirmed on 2026-11-21. Crops are from the 2026-11-21 shots at a measured 1440 by 900 CSS viewport, devicePixelRatio 2. Crops are 256-colour PNGs. Read colours from [tokens.json](tokens.json).

## Button

Primary. Location Continue and the account CONTINUE. Background `#000000`, text `#ffffff`, height 32px, padding 2px 12px, radius 0, font 13px weight 300, uppercase. The account page CONTINUE (`.mds-button--primary`) matched those colours and the 32px height. It was not clicked.

![Location Continue](components/crops/location-continue-default.png)

![Login Continue, empty form, not submitted](components/crops/login-continue-default.png)

Secondary. Product page ADD (`.product-detail-cart-buttons__add-to-cart.zds-button--secondary.zds-button--large`). Background `#ffffff`, text `#000000`, border 0.5px solid `#000000`, height 40px, padding 2px 12px, radius 0, font 13px weight 300. The button was not used to add the item. Apple Pay sits beside it and was not clicked.

![ADD](components/crops/add-button-default.png)

Skip link. `.skip-to-content.zds-button--secondary.zds-button--small`. Same secondary colours, height 32px, border 0.5px solid black. Not cropped this pass.

## Link

Header links (BAG, LOG IN, HELP). 13px, weight 300, line-height 22px, uppercase, colour `#000000`, padding 5px 0, radius 0. The active bag link on the cart page computed weight 500 on the earlier pass.

![Header links](components/crops/header-links-default.png)

SEARCH on the product page is a link with a thick underline.

![Search link](components/crops/search-link-default.png)

## Text field

Search. `input.search-home-input`. 12px, weight 300, padding 8px 0, radius 0, placeholder "What are you looking for?". See [screenshots/search-light-empty.png](screenshots/search-light-empty.png). No query was typed.

Help search. `.help-search-box__search-box-input` after focus, measured 2026-11-19. Border-bottom 1px solid `#000000`, height 32px, radius 0. Not re-focused this pass.

Account email. `input[name=username]`. Height 40px, padding 18px 0 2px, 13px weight 300. The field chrome `.mds-base-field__control` computed border 0.5px solid `rgb(121, 121, 121)`. The EMAIL label computed 12px, weight 300, colour `rgb(107, 107, 107)`, uppercase. Empty. Not submitted.

![Empty email field](components/crops/login-email-default.png)

## Tabs

Search section buttons. Selected Woman: 12px, weight 500, letter-spacing 0.8px, uppercase, padding 8px 0 0. Unselected: weight 300. See [screenshots/search-light-empty.png](screenshots/search-light-empty.png).

## Menu

Open Menu is a full-height drawer. Category tabs are uppercase. The WOMAN category link on the earlier pass computed Times New Roman at 24px, weight 400, letter-spacing -1px. See [site-tree.md](site-tree.md).

![Menu categories](components/crops/menu-categories-default.png)

## Category rail

Dresses subnav. Selected VIEW ALL computed 15px weight 500. Numbered rows through VELVET are in the crop. SECONDHAND sat below the crop.

![Category rail](components/crops/category-nav-default.png)

## Dialog

Filter drawer, opened from FILTERS on the dresses page. Sort, color, size, price, and collection. VIEW RESULTS was not clicked. Close returns to the grid.

![Filter drawer](components/crops/filter-panel-default.png)

Size list `.size-selector` was measured on 2026-11-19 (white, border 0.5px solid black, width 356px, size buttons 20px tall). It was not opened this pass. No size was chosen.

## Card

Product title and price. 15px, weight 300, line-height 24px, uppercase. The measured dress is ANIMAL PRINT TULLE DRESS at $ 45.90.

![Product title and price](components/crops/product-title-default.png)

Grid name and price computed 11px, weight 300, uppercase, line-height 16px on the scrolled dresses grid. See [screenshots/category-light-grid.png](screenshots/category-light-grid.png).

## List row

Help `.zds-selection-cell`. Height 40px, padding 12px 0, label 12px weight 400. Measured 2026-11-19. See [screenshots/help-light-default.png](screenshots/help-light-default.png).

## Empty and error

Empty bag title computed 12px, weight 300, uppercase. "YOUR BAG IS EMPTY".

![Empty bag](components/crops/empty-bag-default.png)

404 title `.page-not-found-view__title` 15px weight 300 uppercase. Subtitle 12px weight 300. See [screenshots/error-light-404.png](screenshots/error-light-404.png).

## Gaps

Hover, pressed, disabled, loading, and error-validation states were not captured. Text area, tooltip, toast, table, avatar, and badge were not on the measured pages. Filter checkboxes and the price slider were photographed and not measured as computed styles this pass. The size list was not reopened.
