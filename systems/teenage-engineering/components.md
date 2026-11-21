# Components

Measured on the public teenage.engineering site, 2026-11-21, signed out, desktop 1440x900. Crops are in [components/crops/](components/crops/). Pressed was not captured: the CDP pseudo-state call failed on every control.

| Component | States captured | Notes |
|---|---|---|
| Logo link | default, hover, focus-visible | te-20, weight 100, colour #f1f2f2 on the black home |
| Nav link | default, hover, focus-visible | same type as the logo. Hover did not change the computed colour |
| Search button | default, hover, focus-visible | opens the in-page search field |
| Search field | default, hover, focus-visible, focused, filled | colour #f5f5f5, transparent background, 16px light |
| Checkout link | default, hover, focus-visible | same as nav link |
| Footer link | default, hover, focus-visible | weight 300, colour #e5e5e5 on the home footer |
| Store tile | default, hover, focus-visible | surface #f5f5f5, square corners, 382px tall at 1440 |
| Add to cart | default, hover, focus-visible | fill #0f0e12, text #f5f5f5, 73px tall, 26px light. Not submitted |
| Sold out | default, hover, focus-visible | transparent fill, #0f0e12 text. Does not navigate |
| Newsletter field | default, hover, focus-visible, focused, filled | white fill, 1px black border, 60px tall, 19px light. Sample text was cleared |
| Newsletter checkbox | default, hover, focus-visible | 29px, 2px #e5e5e5 border, black border on focus-visible |
| Subscribe | default, hover, focus-visible | same geometry as add to cart. Not submitted |
| Region select | default, hover, focus-visible | 1px #767676 border, black border on focus-visible |
| Menu item (phone) | default | 16px light, #f5f5f5, on the black menu |

## Not present

Text area, radio, switch, tabs, tooltip, toast, table, avatar, badge. The public store does not show them.

Dialog: search results render as an in-page panel, not a `dialog` element. The video.js player on a product page mounts its own controls. A closed video dialog reported no compatible source in headless.

## Gaps

- Pressed: Not captured. The reader could not force `:active`.
- Hover on text links: computed colour did not change. If the product uses an image swap, it is not in the computed style.
- Disabled, loading, error-on-field: not shown on the public pages. `--field-color-disabled` and `--error` are declared and tokenised, and were not seen on a control.
- Menu button crop failed (clip outside the image). The open menu is [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).
- Product tile link on `/products` measured a zero-size off-screen node. The store tile is the measured card.
