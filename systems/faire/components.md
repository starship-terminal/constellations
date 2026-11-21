# Faire components

Public signed-out surface, measured 2026-11-21. Crops are from the page screenshots. Values are the computed styles in [raw/measurements.md](raw/measurements.md).

## Button

Primary action. Sign up to buy on the home header.

| State | Fill | Text | Radius | Height |
|---|---|---|---|---|
| default | #333333 | #ffffff | 4px | 40px |
| hover | #000000 | #ffffff | 4px | 40px |
| focus-visible | #333333, 2px #275ec5 outline, 1px offset | #ffffff | 4px | 40px |
| pressed | not captured | | | |
| disabled | not present on the public surface | | | |
| loading | not present | | | |

The Sign in submit inside the modal is the same fill at 48px tall and 340px wide.

Crop: [header-actions-default.png](components/crops/header-actions-default.png).

## Icon button

Previous slide and Next slide sit on the home carousels. They move the track and do not navigate. Sizes were not measured separately. Crop is the page shot [home-light-default.png](screenshots/home-light-default.png).

## Link

Nav links (Home decor and the rest of the category row) are 14px Graphik, #333333, no underline at rest. Footer links match that ink. Menu items in All categories are #161616.

## Text field

The sign-in email field is a 40px shell, 340px wide, 1px #dadada border, 4px radius, white fill. The input itself is transparent. Placeholder text is the product's sample, not a typed address. The field was not filled.

Crop: [dialog-signin-default.png](components/crops/dialog-signin-default.png).

## Text area

Not present on the captured public pages.

## Select

Not present as a native select. The language control is a list of buttons, not a select element. It was not activated.

## Checkbox, radio, switch

Not present on the captured public pages. The cookie preference center contains toggles. It was hidden and not used, so those controls are not captured.

## Tabs

Not present on the home page. Category pages use filter pills (All filters) rather than tabs.

## Menu

All categories opens a full-width white menu, 1440 by 712, no shadow, square corners. Items link to category pages. See [site-tree.md](site-tree.md).

Crop: [menu-categories-default.png](components/crops/menu-categories-default.png).

On phone, a menu control opens a drawer. Crop: [m-menu-default.png](components/crops/m-menu-default.png).

## Tooltip

Not captured. None stayed open during the tour.

## Dialog

Sign in opens a white dialog, 420 by 649, square corners, no shadow, at `/?signIn=1`. It asks for email and password, and offers Google and Apple. Those were not clicked. The form was not submitted.

## Toast

Not shown. Toastify's stylesheet is on the page. Its colours are vendor defaults and are not Faire semantic tokens.

## Card

Category and brand tiles are links. A category card link computed to 16px Graphik, #000000, 4px radius. Wholesale price is behind sign-in and was not opened.

## List row

Footer link rows and the category menu rows. No separate list component was measured.

## Table

Not present on the captured pages.

## Avatar

Not present on the signed-out pages.

## Badge

Filter pills (All filters) are 40px tall, 999px radius, white fill, 1px #dadada border. Seen on the category page [category-light-default.png](screenshots/category-light-default.png).

## Gaps

Pressed, disabled, loading, and error states were not held. Validation was not triggered because no form was submitted. Dark theme is not present on the public site. Signed-in catalog controls (cart, wholesale price, checkout) were not entered.
