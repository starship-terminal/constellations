# Square components

Public marketing site only, captured 2026-11-21 from https://squareup.com/us/en. Signed-in dashboard components are behind the login wall and are Not captured.

## What was seen

- [about-light-default.png](screenshots/about-light-default.png)
- [banking-light-default.png](screenshots/banking-light-default.png)
- [banking-light-full.png](screenshots/banking-light-full.png)
- [cart-light-default.png](screenshots/cart-light-default.png)
- [cart-light-full.png](screenshots/cart-light-full.png)
- [contact-light-default.png](screenshots/contact-light-default.png)
- [contact-light-field-focused.png](screenshots/contact-light-field-focused.png)
- [hardware-light-default.png](screenshots/hardware-light-default.png)
- [hardware-light-full.png](screenshots/hardware-light-full.png)
- [help-light-default.png](screenshots/help-light-default.png)
- [help-light-full.png](screenshots/help-light-full.png)
- [help-light-search-focused.png](screenshots/help-light-search-focused.png)
- [home-light-business-menu.png](screenshots/home-light-business-menu.png)
- [home-light-cart.png](screenshots/home-light-cart.png)
- [home-light-default.png](screenshots/home-light-default.png)
- [home-light-full.png](screenshots/home-light-full.png)
- [home-light-products-menu.png](screenshots/home-light-products-menu.png)
- [home-light-products-payments.png](screenshots/home-light-products-payments.png)
- [home-light-whats-new.png](screenshots/home-light-whats-new.png)
- [legal-light-default.png](screenshots/legal-light-default.png)
- [login-light-default.png](screenshots/login-light-default.png)
- [login-light-full.png](screenshots/login-light-full.png)
- [mobile-hardware-light-default.png](screenshots/mobile-hardware-light-default.png)
- [mobile-help-light-default.png](screenshots/mobile-help-light-default.png)
- [mobile-home-light-default.png](screenshots/mobile-home-light-default.png)
- [mobile-home-light-full.png](screenshots/mobile-home-light-full.png)
- [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png)
- [mobile-login-light-default.png](screenshots/mobile-login-light-default.png)
- [mobile-pricing-light-default.png](screenshots/mobile-pricing-light-default.png)
- [mobile-pricing-light-full.png](screenshots/mobile-pricing-light-full.png)
- [payments-light-default.png](screenshots/payments-light-default.png)
- [payments-light-full.png](screenshots/payments-light-full.png)
- [pos-light-default.png](screenshots/pos-light-default.png)
- [pos-light-full.png](screenshots/pos-light-full.png)
- [pricing-light-default.png](screenshots/pricing-light-default.png)
- [pricing-light-full.png](screenshots/pricing-light-full.png)
- [restaurants-light-default.png](screenshots/restaurants-light-default.png)
- [restaurants-light-full.png](screenshots/restaurants-light-full.png)
- [software-light-default.png](screenshots/software-light-default.png)

## Inventory

| Component | On the public site | States captured | Gap |
|---|---|---|---|
| Button | Pill "Get started" and quiet "Contact sales" | default in screenshots | hover, focus-visible, pressed, disabled, loading: Not captured as separate crops |
| Icon button | Cart, carousel previous/next, mobile menu | default | hover and pressed: Not captured |
| Link | Header, footer, in-page | default | hover colour is `inherit` in the token file; a distinct hover style was not measured |
| Text field | Help search, contact form | focused screenshot where the page loaded | filled, error, disabled: Not captured. No text was typed |
| Text area | Contact form, if present | not separately cropped | Not captured |
| Select | Country switcher in the footer | opened enough to see Canada | options not captured as a component crop |
| Checkbox | Cookie dialog (hidden, not accepted) | Not captured | consent control was not clicked |
| Radio | Not seen on the captured pages | not present on the captured surface | |
| Switch | Not seen | not present on the captured surface | |
| Tabs | Homepage audience stats | default | selected state: Not captured as its own crop |
| Menu | Business types, Products, What's new, cart popover | open screenshots | item hover: Not captured |
| Tooltip | Not seen | not present on the captured surface | |
| Dialog | Cookie preferences on first paint | hidden, not accepted, so no committed screenshot of the dialog body | Not captured |
| Toast | Not seen | not present on the captured surface | |
| Card | Plan cards, hardware cards | default in page screenshots | hover: Not captured |
| List row | Footer link columns, help articles | default | |
| Table | Not seen on the captured marketing pages | not present on the captured surface | |
| Avatar | "Ask our team" faces in the launcher | observed in the homepage screenshot | not cropped |
| Badge | "BEST VALUE" on Square Plus | observed on the homepage | not cropped |

## Shared values

Taken from [tokens.json](tokens.json), not from screenshots.

- Page and surface are `#ffffff` in light and `#000000` in the declared dark set.
- Text is `#000000` on light and `#ffffff` on dark. Muted is `#707070` (light) and `#999999` (dark).
- Primary actions are black pills with white type, radius 50px on the live "Get started" link (computed on the homepage). The token `--action-variant-button-border-radius` is the design-system radius, recorded in `core.radius.button`.
- Focus colour token is the form-field focus custom property: `#000000` light, `#ffffff` dark. Focus ring width was not measured. Not captured as a crop.
- Motion durations: 150ms quick, 300ms default, 400ms slow. Easings are the four cubic-bezier tokens in `core.motion.easing`.

## Gaps

- Dashboard, POS, banking account, payroll and any signed-in screen: auth wall. Branch stopped at login and signup. Not captured.
- Dark theme as a painted page: the public homepage does not set `data-color-mode=dark`. Dark tokens are declared values, not a live screenshot.
- Hover, pressed, disabled, loading and error states were not forced into crops in this capture. Not captured.
- Cookie dialog was hidden rather than accepted. Its controls are Not captured.
