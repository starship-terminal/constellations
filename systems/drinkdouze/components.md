# Douze components

Signed-out public storefront, 2026-11-21. Values are token names. Measurements are in [raw/measurements.json](raw/measurements.json). Crops are 1x and the boxes were estimated. See [README.md](README.md) "What to distrust".

## Announcement

Copy: "FREE DELIVERY IN MAINLAND FRANCE FOR ORDERS OVER €50". Height `size.announcement` (36px). Ink `text.primary`. Crop: [components/crops/announcement-default.png](components/crops/announcement-default.png).

## Header

`store-header`, height `size.header` (57px). Logo link `size.logo` wide (70px, height 23px, not a separate token). Nav link: `typography.nav`, uppercase, `text.primary`, transparent background. Crop: [components/crops/header-default.png](components/crops/header-default.png), [components/crops/nav-link-default.png](components/crops/nav-link-default.png).

Phone header: burger `aria-controls=mobile-menu-drawer`, logo, login, cart. Crop: [components/crops/m-header-default.png](components/crops/m-header-default.png).

## Mobile menu

Drawer opened from the burger. Links in `typography` heading scale (h4 class on the anchors). Account link is the login wall. Crop: [components/crops/m-menu-drawer-default.png](components/crops/m-menu-drawer-default.png).

## Cart drawer

`#mini-cart`, opened by the cart icon without leaving the page. Empty state: "Your cart is empty" and START SHOPPING. Crop: [components/crops/cart-drawer-default.png](components/crops/cart-drawer-default.png). Empty cart page crop: [components/crops/empty-cart-default.png](components/crops/empty-cart-default.png).

## Search drawer

`#search-drawer`, form GET `/en/search`. No visible trigger at 1440 or 1000. Crop taken from a programmatic open: [components/crops/search-drawer-default.png](components/crops/search-drawer-default.png).

## Button

Primary: `component.button.bg` (`color.dusk`), `component.button.text` (`color.onAccent`), `component.button.radius` (`radius.none`), horizontal padding `space.buttonX` (15px) or `space.buttonXWide` (20px on add-to-cart). Label `typography.button`, uppercase. Declared height `size.button` (52px). Computed small height `size.buttonSmall` (44px), which is what `component.button.height` aliases.

Hover on add-to-cart: white label, dusk background, white border. Focus: outline none, shadow `rgba(0, 0, 0, 0.15) 0px 4px 8px 0px`. Not a ring.

Crops: [components/crops/hero-cta-default.png](components/crops/hero-cta-default.png), [components/crops/add-to-cart-default.png](components/crops/add-to-cart-default.png).

## Filter tabs

`.tabs-nav__item`. Selected: dusk fill, white label, `radius.pill` (999px), padding 8px 16px, height 44px. Idle tabs sit beside it. URL does not change. Crops: [components/crops/filter-tabs-default.png](components/crops/filter-tabs-default.png), [components/crops/filter-tabs-selected.png](components/crops/filter-tabs-selected.png).

## Product card

`.product-item`. Radius `radius.block` (45px). Width about 399px on the shop grid at 1440. No separate title or price reading (those selectors returned null).

## PDP buy box

Pack radios `option1`: 6 / 12 / 24 cans. Purchase options: ONE-TIME PURCHASE (active) and SUBSCRIPTION −10%. ADD TO CART is the primary button. Not submitted.

Crops: [components/crops/pdp-buybox-default.png](components/crops/pdp-buybox-default.png), [components/crops/pack-picker-default.png](components/crops/pack-picker-default.png), [components/crops/pack-picker-selected.png](components/crops/pack-picker-selected.png), [components/crops/purchase-option-selected.png](components/crops/purchase-option-selected.png).

## FAQ accordion

`button.collapsible-toggle`. Closed by default. Opened item: "HOW DO I CREATE MY CUSTOMER ACCOUNT?" with `aria-expanded=true`. Crops: [components/crops/faq-accordion-default.png](components/crops/faq-accordion-default.png), [components/crops/faq-accordion-open.png](components/crops/faq-accordion-open.png).

## Login card

Sable card, `radius.block`. Fields computed to 16px radius (`radius.blockReduced`), 52px tall, 1px dusk border. Nothing was typed into them. Submit is a square dusk button. Crops: [components/crops/login-card-default.png](components/crops/login-card-default.png), [components/crops/login-email-default.png](components/crops/login-email-default.png), [components/crops/login-submit-default.png](components/crops/login-submit-default.png).

## Contact form

Name, email, message, SUBMIT. Not filled. Crop: [components/crops/contact-form-default.png](components/crops/contact-form-default.png).

## Subscription builder

Product picker, pack sizes, add-a-product, subscribe. Not submitted. Crop: [components/crops/subscription-builder-default.png](components/crops/subscription-builder-default.png).

## Locale popover

Footer button ENGLISH controls `footer-locale-selector`. Buttons `locale_code=fr` and `locale_code=en`. Not submitted. No crop: the 1440 shot did not clearly show the popover.

## Shared values

| Role | Token |
|---|---|
| Page | `background.page` |
| Surface | `background.surface` |
| Text | `text.primary` |
| On button | `text.onAccent` |
| Hero ink | `text.onHero` |
| Border | `border.default` |
| Button radius | `radius.none` |
| Card radius | `radius.block` |
| Tab radius | `radius.pill` |

## Gaps

- Desktop SHOP menu panel: `aria-controls=desktop-menu-1` has no node.
- Newsletter popup: control is hidden and the popup node is absent.
- Visible search trigger: not found. Drawer exists.
- Field radius: computed 16px on the login fields. Not re-read on contact or stockist fields.
- Focus ring: not painted.
- Distinct error colour: declared error triplet matches success.
- Dark theme: not on the public site.
- Hover and pressed states for nav, tabs, and fields: not measured, except add-to-cart hover and focus.
- Icon set: not extracted. Brand artwork stays on the site.
- Crop alignment: estimated, not re-checked.
