# Components

Public signed-out components measured on luluandgeorgia.com on 2026-11-21. Crops are in [components/crops/](components/crops). Colours are computed styles. The site paints square corners and one ink.

| Component | Status | Evidence |
|---|---|---|
| Button | captured | Add to cart is 40px, fill #1a1713, label #ffffff, weight 800. [default](components/crops/atc-default.png), [hover](components/crops/atc-hover.png), [focus](components/crops/atc-focus.png), [pressed](components/crops/atc-pressed.png). Hover and pressed did not change the fill. Focus is a keyboard focus (Shift+Tab, then Tab) after the pointer moved away. |
| Icon button | captured | Account 22px and bag 23px in the header. [account](components/crops/icon-account-default.png), [bag](components/crops/icon-cart-default.png). The wishlist button beside add to cart was not found by the measure pass, so it has no reading. |
| Link | captured | Category links are 11px uppercase, 1.2px tracking, ink #1a1713. Sale is #b11515. [furniture](components/crops/nav-link-default.png). Account drawer link in [account-link](components/crops/account-link-default.png). |
| Text field | captured | Header search is 44px, fill #ebebeb, placeholder #747474, radius 0. [default](components/crops/search-default.png), [focus](components/crops/search-focus.png). The field was not typed into. Quantity on the product page is 28x40. [qty](components/crops/qty-default.png). |
| Text area | not present | No textarea on the signed-out pages. |
| Select | not captured | A variant select exists in the DOM (`select.product-variants`) and was not visible on the Sachs dining table page, which paints a single price. |
| Checkbox | observed | The Shop sign-in page paints "Email me with news and offers" checked. That page is shopify.com, not the storefront. It was not measured as a store token. See [login-light-default](screenshots/login-light-default.png). |
| Radio | not present | No radio on the signed-out storefront pages. |
| Switch | not present | No switch on the signed-out pages. |
| Tabs | not present | Product details are a disclosure (Shipping & Returns), not tabs. |
| Menu | captured | The furniture mega-menu, the account drawer, and the filter drawer. [furniture](screenshots/home-light-nav.png), [account](screenshots/home-light-account.png), [filter](screenshots/collection-light-filter.png). |
| Tooltip | not present | No tooltip was painted. |
| Dialog | captured | Filter drawer and account drawer are side panels, not centred dialogs. [filter](screenshots/collection-light-filter.png). |
| Toast | not present | No toast was painted. |
| Card | captured | Collection product cards. [card](components/crops/product-card-default.png). Search suggestions in [home-light-search](screenshots/home-light-search.png). |
| List row | captured | Filter groups are rows with a plus. [filter](screenshots/collection-light-filter.png). |
| Table | not present | No data table on the public pages. |
| Avatar | not present | No avatar on the signed-out storefront. |
| Badge | observed | Search suggestions paint Exclusive and New chips. The badge selector matched the whole product card (324x421), so `badge` in raw/ and its crop are the card, not the chip. Recapture needed. See [home-light-search](screenshots/home-light-search.png). |
| Hero button | not captured | "Shop bestsellers" is visible in the home screenshot and was not a stable locator during measurement (the hero is a carousel). See [home-light-default](screenshots/home-light-default.png). |

## States

Hover was a real pointer hover and pressed was forced (`CSS.forcePseudoState`) on add to cart. The computed fill stayed #1a1713. Focus is a keyboard focus (Shift+Tab, then Tab) taken after the pointer moved away. The 2026-11-21 reading says `:focus-visible` matched, and the fill did not change. Disabled was not painted. Loading was not painted. A validation error was not produced, because the login form was not submitted and add to cart was not clicked.
