# Zellerfeld components

Measured on the public storefront on 2026-11-21, signed out, headed Chrome.
Desktop 1440x900. Phone controls are the 390x844 rows. One theme.
Hover is a real pointer. Focus-visible is keyboard Tab. Pressed is
`CSS.forcePseudoState` with hover and active, so the control does not fire.
A crop is the element screenshot. Values are computed styles.

Shared values: page `#171717` (`light.background.page`), text `#ffffff`
(`light.text.primary`), muted white at 50% (`light.text.muted`), ember
`#ff5e3e` (`light.accent.default`), focus `#3773f5` (`light.focus.ring`),
control face white at 10% (`light.background.muted`). Phonic is the
control face. Lateral is the wordmark face. Exposure is the display face.

## nav-button

Opens the navigation drawer

Page: home. Role: icon button.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| default | resting | [crop](components/crops/nav-button-default.png) | rgba(255, 255, 255, 0.1) | rgb(255, 255, 255) | 4px | 36px |
| hover | mouse hover | [crop](components/crops/nav-button-hover.png) | rgba(255, 255, 255, 0.2) | rgb(255, 255, 255) | 4px | 36px |
| focus-visible | keyboard Tab | [crop](components/crops/nav-button-focus-visible.png) | rgba(255, 255, 255, 0.1) | rgb(255, 255, 255) | 4px | 36px |
| pressed | CDP forcePseudoState hover+active (no click) | [crop](components/crops/nav-button-pressed.png) | rgba(255, 255, 255, 0.2) | rgb(255, 255, 255) | 4px | 36px |

## wordmark

Page: home. Role: link.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| default | resting | [crop](components/crops/wordmark-default.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 4px | 28px |
| hover | mouse hover | [crop](components/crops/wordmark-hover.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 4px | 28px |
| focus-visible | keyboard Tab | [crop](components/crops/wordmark-focus-visible.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 4px | 28px |

## create-link

Leaves for studio.zellerfeld.com

Page: home. Role: link.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| default | resting | [crop](components/crops/create-link-default.png) | rgba(0, 0, 0, 0) | rgb(255, 94, 62) | 4px | 36px |
| hover | mouse hover | [crop](components/crops/create-link-hover.png) | rgba(0, 0, 0, 0) | rgb(255, 94, 62) | 4px | 36px |
| focus-visible | focus failed | not captured |  |  |  |  |
| pressed | CDP forcePseudoState hover+active (no click) | [crop](components/crops/create-link-pressed.png) | rgba(0, 0, 0, 0) | rgb(255, 94, 62) | 4px | 36px |

## sign-in-button

Opens Clerk sign-in. Not clicked.

Page: home. Role: button.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| default | resting | [crop](components/crops/sign-in-button-default.png) | rgba(255, 255, 255, 0.1) | rgb(255, 255, 255) | 4px | 36px |
| hover | mouse hover | [crop](components/crops/sign-in-button-hover.png) | rgba(255, 255, 255, 0.2) | rgb(255, 255, 255) | 4px | 36px |
| focus-visible | keyboard Tab | [crop](components/crops/sign-in-button-focus-visible.png) | rgba(255, 255, 255, 0.1) | rgb(255, 255, 255) | 4px | 36px |
| pressed | CDP forcePseudoState hover+active (no click) | [crop](components/crops/sign-in-button-pressed.png) | rgba(255, 255, 255, 0.2) | rgb(255, 255, 255) | 4px | 36px |

## search-field

Page: home. Role: text field.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| default | resting | [crop](components/crops/search-field-default.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 8px | 36px |
| hover | mouse hover | [crop](components/crops/search-field-hover.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 8px | 36px |
| focus-visible | keyboard Tab | [crop](components/crops/search-field-focus-visible.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 8px | 36px |
| focused | click, not submitted | [crop](components/crops/search-field-focused.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 8px | 36px |
| filled | typed nike, not submitted, then cleared | [crop](components/crops/search-field-filled.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 8px | 36px |

## nav-drawer

Page: home. Role: menu.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| open | Open navigation click | [crop](components/crops/nav-drawer-open.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 0px | 900px |

## nav-link

Page: home. Role: link.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| default | resting | [crop](components/crops/nav-link-default.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 0px | 24px |
| hover | mouse hover | [crop](components/crops/nav-link-hover.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 0px | 24px |
| focus-visible | keyboard Tab | [crop](components/crops/nav-link-focus-visible.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 0px | 24px |
| pressed | CDP forcePseudoState hover+active (no click) | [crop](components/crops/nav-link-pressed.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 0px | 24px |

## sort-chip

Page: sneakers. Role: button.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| default | resting | [crop](components/crops/sort-chip-default.png) | rgb(255, 255, 255) | rgb(0, 0, 0) | 4px | 36px |
| hover | mouse hover | [crop](components/crops/sort-chip-hover.png) | oklab(0.999994 0.0000455678 0.0000200868 / 0.9) | rgb(0, 0, 0) | 4px | 36px |
| focus-visible | keyboard Tab | [crop](components/crops/sort-chip-focus-visible.png) | rgb(255, 255, 255) | rgb(0, 0, 0) | 4px | 36px |
| pressed | CDP forcePseudoState hover+active (no click) | [crop](components/crops/sort-chip-pressed.png) | oklab(0.999994 0.0000455678 0.0000200868 / 0.9) | rgb(0, 0, 0) | 4px | 36px |

## product-card

Page: sneakers. Role: card.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| default | resting | [crop](components/crops/product-card-default.png) | rgba(0, 0, 0, 0) | rgb(0, 0, 0) | 0px | auto |
| hover | mouse hover | [crop](components/crops/product-card-hover.png) | rgba(0, 0, 0, 0) | rgb(0, 0, 0) | 0px | auto |
| focus-visible | keyboard Tab | [crop](components/crops/product-card-focus-visible.png) | rgba(0, 0, 0, 0) | rgb(0, 0, 0) | 0px | auto |

## buy-button

Opens Fit Profile. Measured at rest. Not used to proceed.

Page: product. Role: button.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| default | resting | [crop](components/crops/buy-button-default.png) | rgb(255, 94, 62) | rgb(0, 0, 0) | 4px | 56px |
| hover | mouse hover | [crop](components/crops/buy-button-hover.png) | rgb(255, 94, 62) | rgb(0, 0, 0) | 4px | 56px |
| focus-visible | keyboard Tab | [crop](components/crops/buy-button-focus-visible.png) | rgb(255, 94, 62) | rgb(0, 0, 0) | 4px | 56px |
| pressed | CDP forcePseudoState hover+active (no click) | [crop](components/crops/buy-button-pressed.png) | rgb(255, 94, 62) | rgb(0, 0, 0) | 4px | 56px |

## wishlist-button

Opens sign-in. Not clicked here.

Page: product. Role: icon button.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| default | resting | [crop](components/crops/wishlist-button-default.png) | rgba(255, 255, 255, 0.1) | rgb(255, 255, 255) | 4px | 56px |
| hover | mouse hover | [crop](components/crops/wishlist-button-hover.png) | rgba(255, 255, 255, 0.2) | rgb(255, 255, 255) | 4px | 56px |
| focus-visible | keyboard Tab | [crop](components/crops/wishlist-button-focus-visible.png) | rgba(255, 255, 255, 0.1) | rgb(255, 255, 255) | 4px | 56px |
| pressed | CDP forcePseudoState hover+active (no click) | [crop](components/crops/wishlist-button-pressed.png) | rgba(255, 255, 255, 0.2) | rgb(255, 255, 255) | 4px | 56px |

## color-swatch

Page: product. Role: link.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| default | not captured: colour link not found | not captured |  |  |  |  |

## gallery-thumb

Page: product. Role: button.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| default | resting | [crop](components/crops/gallery-thumb-default.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 6px | 64px |
| hover | mouse hover | [crop](components/crops/gallery-thumb-hover.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 6px | 64px |
| focus-visible | keyboard Tab | [crop](components/crops/gallery-thumb-focus-visible.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 6px | 64px |

## accordion

Page: faq. Role: disclosure.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| default | closed summary | [crop](components/crops/accordion-default.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 0px | 84px |
| open | summary click | [crop](components/crops/accordion-open.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 0px | 84px |

## newsletter-field

Not filled. Not submitted.

Page: newsletter. Role: text field.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| default | resting | [crop](components/crops/newsletter-field-default.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 0px | 18px |
| hover | mouse hover | [crop](components/crops/newsletter-field-hover.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 0px | 18px |
| focus-visible | keyboard Tab | [crop](components/crops/newsletter-field-focus-visible.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 0px | 18px |

## newsletter-submit

Not clicked.

Page: newsletter. Role: button.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| default | resting | [crop](components/crops/newsletter-submit-default.png) | rgb(255, 94, 62) | rgb(0, 0, 0) | 4px | 36px |
| hover | mouse hover | [crop](components/crops/newsletter-submit-hover.png) | rgb(255, 94, 62) | rgb(0, 0, 0) | 4px | 36px |
| focus-visible | keyboard Tab | [crop](components/crops/newsletter-submit-focus-visible.png) | rgb(255, 94, 62) | rgb(0, 0, 0) | 4px | 36px |
| pressed | CDP forcePseudoState hover+active (no click) | [crop](components/crops/newsletter-submit-pressed.png) | rgb(255, 94, 62) | rgb(0, 0, 0) | 4px | 36px |

## footer-link

Page: faq. Role: link.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| default | resting | [crop](components/crops/footer-link-default.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 0px | auto |
| hover | mouse hover | [crop](components/crops/footer-link-hover.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 0px | auto |
| focus-visible | keyboard Tab | [crop](components/crops/footer-link-focus-visible.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 0px | auto |
| pressed | CDP forcePseudoState hover+active (no click) | [crop](components/crops/footer-link-pressed.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 0px | auto |

## mobile-nav-button

Bottom bar Menu. The desktop Open navigation button is hidden at 390.

Page: home. Role: icon button.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| default | resting | [crop](components/crops/mobile-nav-button-default.png) | rgba(0, 0, 0, 0) | oklab(0.999994 0.0000455678 0.0000200868 / 0.5) | 0px | 40px |
| focus-visible | keyboard Tab | [crop](components/crops/mobile-nav-button-focus-visible.png) | rgba(0, 0, 0, 0) | oklab(0.999994 0.0000455678 0.0000200868 / 0.5) | 0px | 40px |
| pressed | CDP forcePseudoState hover+active (no click) | [crop](components/crops/mobile-nav-button-pressed.png) | rgba(0, 0, 0, 0) | oklab(0.999994 0.0000455678 0.0000200868 / 0.5) | 0px | 40px |

## mobile-nav-drawer

Page: home. Role: menu.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| open | Open navigation | [crop](components/crops/mobile-nav-drawer-open.png) | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 0px | 844px |

## cookie-accept

Consent. Not clicked. Banner may already be hidden.

Page: home. Role: button.

| State | How | Crop | Face | Text | Radius | Height |
|---|---|---|---|---|---|---|
| default | not captured: banner hidden before this measure so consent is never clicked | not captured |  |  |  |  |

## Gaps

- Text area, select, checkbox, radio, switch, tabs, tooltip, toast, table, avatar, badge: not present on the public pages that were opened.
- Disabled and loading: not shown on a resting public control.
- Error on a field: not captured. No form was submitted.
- Cookie accept: the banner was removed before measurement so consent was never clicked. The cookie banner is in `screenshots/home-light-cookie.png`.
- Dark theme: not present.
- Signed-in account, cart, checkout, wishlist contents: behind the Clerk sign-in wall. Stopped.
