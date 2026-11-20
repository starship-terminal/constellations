# Components

Measured on stocktwits.com, signed out, light theme, 2026-11-21. Crops are in [components/crops/](components/crops).

## button-primary

- default: backgroundColor rgb(0, 0, 0), color rgb(255, 255, 255), borderRadius 9999px, fontSize 15px, fontWeight 600, height 40px. Crop: [components/crops/button-primary-default.png](components/crops/button-primary-default.png). Page `/`.
- hover: backgroundColor rgb(44, 44, 46), color rgb(255, 255, 255), borderRadius 9999px, fontSize 15px, fontWeight 600, height 40px. Crop: [components/crops/button-primary-hover.png](components/crops/button-primary-hover.png). Page `/`.

## button-secondary

- default: backgroundColor rgb(255, 255, 255), color rgb(0, 0, 0), borderRadius 9999px, fontSize 15px, fontWeight 600, height 40px. Crop: [components/crops/button-secondary-default.png](components/crops/button-secondary-default.png). Page `/`.

## button-outline

- default: backgroundColor rgb(255, 255, 255), color rgb(0, 0, 0), borderRadius 9999px, fontSize 15px, fontWeight 600, height 40px. Crop: [components/crops/button-outline-default.png](components/crops/button-outline-default.png). Page `/`.

## link

- default: backgroundColor rgba(0, 0, 0, 0), color rgb(27, 102, 231), borderRadius 0px, fontSize 14px, fontWeight 400, height 18px. Crop: [components/crops/link-default.png](components/crops/link-default.png). Page `/`.

## nav-link

- default: backgroundColor rgba(0, 0, 0, 0), color rgb(0, 0, 0), borderRadius 0px, fontSize 13px, fontWeight 400, height 19.5px. Crop: [components/crops/nav-link-default.png](components/crops/nav-link-default.png). Page `/`.

## tab

- selected: backgroundColor rgba(0, 0, 0, 0), color rgb(0, 0, 0), borderRadius 0px, fontSize 16px, fontWeight 400, height 41px. Crop: [components/crops/tab-selected.png](components/crops/tab-selected.png). Page `/`.
- default: backgroundColor rgba(0, 0, 0, 0), color rgb(142, 142, 147), borderRadius 0px, fontSize 16px, fontWeight 400, height 41px. Crop: [components/crops/tab-default.png](components/crops/tab-default.png). Page `/`.

## search-field

- default: backgroundColor rgba(0, 0, 0, 0), color rgba(0, 0, 0, 0), borderRadius 0px, fontSize 16px, fontWeight 400, height 36px. Crop: [components/crops/search-field-default.png](components/crops/search-field-default.png). Page `/`.
- focus: backgroundColor rgba(0, 0, 0, 0), color rgba(0, 0, 0, 0), borderRadius 0px, fontSize 16px, fontWeight 400, height 36px. Crop: [components/crops/search-field-focus.png](components/crops/search-field-focus.png). Page `/`.

## Also measured, no crop

- Bullish chip: fill rgb(224, 247, 239), 14px semibold, pill. [raw/extra-readings.json](raw/extra-readings.json).
- Bearish chip: fill rgb(251, 230, 227), 14px semibold, pill.
- Text field on /signin: fill #f2f2f7, radius 8px, height 40px. Placeholder Email or Username. Nothing typed.
- Disabled Log In: fill #d1d1d6, white label, pill, 40px.

## Gaps

- Checkbox, radio, switch, select, text area, tooltip, toast, dialog (destructive): not present on the public pages that loaded, or not opened.
- Focus ring: the search field and the login field were focused. Computed outline did not change in the reading. Focus colour is Not captured.
- Pressed and loading: not held. Not captured.
- Dark theme: the product stayed on `data-theme=light` with `prefers-color-scheme: dark`. Not present as a public theme.
- Card radius: visible in screenshots, not read from a computed style. Not captured.
- Hover on Sign Up was read (fill #2c2c2e). Other hovers were not.
